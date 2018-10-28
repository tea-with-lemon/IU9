;1
(define (my-range a b d)
  (cond
      ((<= (- b a) 0)'())
      (else (cons a (my-range (+ a d) b d)))))
;2
(define (my-flatten xs)
  (cond
    ((null? xs)'())
    ((list? (car xs)) (my-flatten(append (car xs) (my-flatten(cdr xs)))))
    (else (append (list(car xs)) (my-flatten(cdr xs))))))
;3
(define (my-element? x xs)
  (and
   (not (null? xs))
   (or (equal? x (car xs))
       (my-element? x (cdr xs)))))
;4
(define (my-filter pred? xs)
  (define (iter buf list)
    (cond
      ((null? list) buf)
      ((pred? (car list)) (iter (cons (car list) buf) (cdr list)))
      (else (iter buf (cdr list)))))
  (reverse(iter '() xs)))
;5
(define (my-fold-left op xs)
  (if (=(length xs) 1)(car xs)
      (my-fold-left op (cons (op (car xs)(cadr xs)) (cddr xs)))))
;6
(define (my-fold-right op xs)
  (if (=(length xs) 2) (op (car xs)(cadr xs))
      (op (car xs) (my-fold-right op(cdr xs)))))







