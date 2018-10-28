(define (map1/x xs)
  (call/cc
   (lambda (escape)
     (begin
       (define (helper1/x ys)
        ;
        ;
        ; 
         (if (zero? (car ys) (escape #f))
       (helper xs)))))))

(define (fib n)
  (if (< n 2)
      n
      (+ (fib (- n 1)) (- n 2))))

;,time (fib 30) => 0,65
;,time (fib 32) => 1,65
;,time (+ (fib 30)(fib 32)) => 2,25

(define count
  (let ((n 0))
    (lambda ()
      (begin
        (set! n (+ n 1))
        n))))
;> (count)
;1
;> (count)
;2

(define fibm
  (let ((memo '()))
    (lambda (n)
      (let ((memoized (assq n memo)))
        (if memoized
            (cadr memoized)
            (let ((new-value (if (< n 2)
                                 n
                                 (+ (fib (- n 1)) (- n 2)))))
              (set! memo
                    (cons (list n new-value) memo))
              new-value))))))
;(fibm 30)=>0,0025
;(fibm 32)=>0,0025
;(+ (fib 30)(fib 32)) => 0,0025

;прочитать про ленивые(отложенные) вычисления(lazy, delayed)
;нестрогие вычисления(non-strict)

(define x 0)
(define y (delay(/ 1 x)))
(length (list x y)) ;=> 2


(define-syntax lazy-cons
  (syntax-rules ()
    ((_ a b) (cons a (delay b)))))
(define (lazy-cdr ls) (force (cdr ls)))
(define (lazy-car car))


(define-syntax lazy-cons
  (syntax-rules ()
    ((_ a b) (cons a (delay b)))))
(define lazy-car car) 
(define (lazy-cdr p) (force (cdr p)))
(define (lazy-ref xs k)
  (if (zero?  k ) (lazy-car xs)
      (lazy-ref (lazy-cdr xs)( - k 1))))


;бесконечный список чисел Фибббоначи
(define-syntax lazy-cons
  (syntax-rules ()
    ((_ a b) (cons a (delay b)))))

(define (lazy-cdr ls) (force (cdr ls)))
(define lazy-car car)

(define (lazy-ref ls n)
  (if zero n?) (lazy-car ls)
  (lazy-ref (lazy-car ls) (- n 1)))

(define (fib-gen a b)
  (lazy-cons a (fib-gen b (+ a b))))

(define (lazy-fib n)
  (lazy-ref (fib-gen 0 1) n))




