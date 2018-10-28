; задача 1
(define (count x xs)
  (cond
    ((null? xs) 0)
    ((equal? (car xs) x)(+ 1(count x(cdr xs))))
    (else (count x(cdr xs)))))

; задача 2
(define (replace pred? proc xs)
  (cond
    ((null? xs)(list))
    ((pred? (car xs))(cons (proc (car xs))(replace pred? proc (cdr xs))))
    (else (cons (car xs) (replace pred? proc (cdr xs))))))

; задача 3
(define (replicate x n)
  (cond
    ((zero? n) (list ))
    (else (append (replicate x (- n 1)) (list x)))))

; задача 4
(define (cycle xs n)
  (define (helper xss xs n)
    (cond
      ((zero? n) xss)
      (else (helper (append xs xss) xs (- n 1)))))
  (helper (list ) xs n))

; задача 5
(define (and-fold . args)
  (cond
    (equal? ((a b c) (#t)) #t)
    (else #f)))