(define (count x xs)
  (define (iter list b)
    (cond
      ((null? list) b)
      ((equal? x (car list)) (iter (cdr list) (+ b 1)))
      (else (iter (cdr list) b))))
  (iter xs 0))

;(count 'a '(a b c a))
;(count 'b '(a c d))
;(count 'a '())

(define (replace pred func xs)
  (define (iter result list)
    (cond
      ((null? list) result)
      ((pred (car list)) (iter (cons (func (car list)) result) (cdr list)))
       (else (iter (cons (car list) result) (cdr list)))))
  (reverse (iter `() xs)))

;(replace zero? (lambda (x) (+ x 1)) '(0 1 2 3 0))
;(replace odd?  (lambda (x) (* 2 x)) '(1 2 3 4 5 6))
;(replace even? (lambda (x) (/ x 2)) '(1 3 5 7))
;(replace (lambda (x) (> 0 x)) exp '()) 


(define (replicate x n)
  (define (iter list count)
    (if (> n count)
        (iter (cons x list) (+ count 1))
        list))
  (iter `() 0))

;(replicate 'a 5)
;(replicate '(a b) 3)
;(replicate 'a 0)


(define (cycle xs n)
  (define (iter list count)
    (if (> n count)
        (iter (append list xs) (+ count 1))
        list))
  (iter '() 0))

;(cycle '(0 1) 3)
;(cycle '(a b c) 3)
;(cycle '() 0)      


(define (and-fold . args)
  (define (iter list)
    (cond
      (not(null? list))
      ((car args))
      (else (iter (cdr list)))))
  (iter args))

(define (or-fold . args)
  (define (iter list)
    (cond
      ((null? list))
      (not (car args))
      (else (iter (cdr list)))))
  (iter args))

;(and-fold #f #f #f)
;(and-fold #t #f #f)
;(and-fold #t #t #f)
;(and-fold #t #t #t)
;(and-fold)

;(or-fold #f #f #f)
;(or-fold #t #f #f)
;(or-fold #t #t #f)
;(or-fold #t #t #t)


(define (find-number a b c)
  (define (iter count)
    (cond
      ((= (remainder count c) 0) count)
      ((< count b) (iter (+ count 1)))
      (else #f)))
      (iter a))

;(find-number 0 5 2)
;(find-number 7 9 3)
;(find-number 3 7 9)


(define (f x) (* x 2))
(define (g x) (* x 3))
(define (h x) (- x))

(define (p res func) (lambda (x) (res (func x))))

;((p f g) 1)

(define (o . args)
  (define (iter res list)
    (if(null? list)
         res
         (iter (p res (car list))  (cdr list))))
  (if (null? args)
      (lambda (x) (+ x 0))
      (iter (car args)  (cdr args))))
;((o) 1)



        