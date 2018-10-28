(define ok '(1 2 3))
(define (my-fold-left op lst)
  (if (null? (cdr lst)) (car lst)
      (let* ((k (op (car lst) (cadr lst)))
             (lst (cons k (cddr lst))))
        (my-fold-left op lst))))
 
 
(define (make-multi-vector sizes . args)
  (set! lst sizes)
  (let ((v (make-vector (my-fold-left * sizes))))
    (if (= (length args) 1) 
        (begin
          (vector-fill! v (car args)) 
          v)
        v)))
 
(define lst '())
 
(define (multi-vector? m)
  (> (length lst) 1))
 
(define (multi-vector-set! m indices k)
  (set-vector m indices lst (vector-length m) 0 k))
 
(define (multi-vector-ref m indices)
  (ref-vector m indices lst (vector-length m) 0))
 
(define (set-vector m indices lst a b k)
  (if (null? indices)
      (vector-set! m b k)
      (let* ((a (/ a (car lst)))
             (b (+ b (* a (car indices)))))
        (set-vector m (cdr indices) (cdr lst) a b k))))
 
(define (ref-vector m indices lst a b)
  (if (null? indices) 
      (vector-ref m b)
      (let* ((a (/ a (car lst)))
             (b (+ b (* a (car indices)))))
        (ref-vector m (cdr indices) (cdr lst) a b))))