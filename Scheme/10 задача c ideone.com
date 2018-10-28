;------help procedures------

(define (list-product lst)
  (if (null? lst)
    1
    (* (car lst) (list-product (cdr lst)))))

(define (get-filled-list len el)
  (if (zero? len)
    '()
    (cons el (get-filled-list (- len 1) el))))

(define (get-filled-list-fast len el)
  (define (iter lst l)
    (if (<= (* l 2) len)
      (iter (append lst lst) (* l 2))
      (append (get-filled-list (- len l) el) lst)))
  (iter (list el) 1))

(define (get-vector len el)
  (apply vector (get-filled-list-fast len el)))

(define (get-prod-list lst)
  (if (null? lst)
    '()
    (let ((last-prod (get-prod-list (cdr lst))))
      (if (null? last-prod)
        (cons (car lst) '())
        (cons (* (car lst) (car last-prod)) last-prod)))))

;---------------------------

;Note: we will keep the offset for each dimension nor size of it;
;The first element of offset-list if the length of multi-vector
(define (make-multi-vector sizes . el)
  (if (null? el)
    (cons (append (get-prod-list sizes) (list 1)) (get-vector (list-product sizes) '()))
    (cons (append (get-prod-list sizes) (list 1)) (get-vector (list-product sizes) (car el)))))

(define (multi-vector? m)
  (and (pair? m) (list? (car m)) (vector? (cdr m))))

(define (multi-vector-ref m indices)
  (define (offset offsets indices)
    (if (null? offsets)
      0
      (+ (* (car offsets) (car indices)) (offset (cdr offsets) (cdr indices)))))
  (vector-ref (cdr m) (offset (cdr (car m)) indices)))

(define (multi-vector-set! m indices x)
  (define (offset offsets indices)
    (if (null? offsets)
      0
      (+ (* (car offsets) (car indices)) (offset (cdr offsets) (cdr indices)))))
  (vector-set! (cdr m) (offset (cdr (car m)) indices) x))

(begin
  (write (eval (read) (interaction-environment)))
  (newline))