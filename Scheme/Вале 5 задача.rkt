(define (my-element? x xs)
  (if (null? xs)
      #f
      (cond
        ((equal? x (car xs)))
        (else (my-element? x (cdr xs))))))
(my-element? 1 '(3 2 1))
(my-element? 4 '(3 2 1))

(define (my-range a b d)
  (cond
    ((and (< a b) (< (+ a d) b)) (cons a (my-range (+ a d) b d)))
    (else (cons a '()))))
(my-range  0 11 3)
(my-range 0 10 1)

(define (my-filter pred? xs)
  (if (null? xs)
      '()
      (if (pred? (car xs))
          (cons (car xs) (my-filter pred? (cdr xs)))
          (my-filter pred? (cdr xs)))))
(my-filter odd? (my-range 0 10 1))
(my-filter (lambda (x) (= (remainder x 3) 0)) (my-range 0 13 1))


(define (my-fold-right op xs)
    (define (right prev op xs)
      (if (not (null? xs))
          (right (op (car xs) prev) op (cdr xs))
          prev))
    (right (car (reverse xs)) op (cdr (reverse xs))))
(my-fold-right expt     '(2 3 4))


 (define (my-fold-left op xs)
    (define (fold prev op xs)
      (if (not (null? xs))
      (fold (op prev (car xs)) op (cdr xs))
      prev))
       (fold (car xs) op (cdr xs)))
 (my-fold-left  quotient '(16 2 2 2 2))


(define (my-flatten xs )
  (define (open ys)
    (if (null? ys)
        '()
  (if   (null? (cdr ys))
        (if (not (list? (car ys)))
       (cons (car ys) '())
       (open (append (car ys) '())))
  (if (list? (car ys))
      (open  (append (car ys) (cdr ys)))
            (cons (car ys) (open (cdr ys)))))))
  (open xs))
(my-flatten '((1) 2 (3 (4 5)) 6))