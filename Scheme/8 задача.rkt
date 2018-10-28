(define-syntax trace-ex
  (syntax-rules ()
    ((_ expression)
     (begin
       (write (quote expression))
       (display " => ") 
       (let ((result expression))
         (write result)
         (newline)
         result)))))

(define (pack xs)
  (define (helper xs ys)
    (cond
      ((null? xs) (list ys))
      ((or (null? ys) (equal? (car xs) (car ys))) (helper (cdr xs) (cons (car xs) ys)))
      (else (append (list ys) (helper (cdr xs)(list (car xs)))))))
  (helper xs '()))

(define (encode xs)
  (define (helper xs ys)
    (cond
      ((null? xs) ys)
      (else (helper (cdr xs)(cons (list (caar xs)(length (car xs))) ys)))))
  (reverse(helper (pack xs) '())))

(define (unpack xs)
  (define (replicate x n)
    (cond
      (( > n 0)(cons x (replicate x ( - n 1))))
      ((zero? n) '())))
  (if (null? xs) xs
  (cons (replicate (caar xs) (cadar xs)) (unpack (cdr xs)))))

(define (decode xs)
  (define (replicate x n)
    (cond
      (( > n 0)(cons x (replicate x ( - n 1))))
      ((zero? n) '())))
  (if (null? xs) xs
  (append (replicate (caar xs) (cadar xs)) (decode (cdr xs)))))

