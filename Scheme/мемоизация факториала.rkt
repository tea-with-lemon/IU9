(define memoized-factorial
  (let ((memo '()))
    (lambda (n)
      (let ((memoized (assq n memo)))
        (if memoized
            (cadr memoized)
            (let ((val (if (<= n 1) 1 (* (memoized-factorial (- n 1)) n))))
              (set! memo
                    (cons (list n val) memo))
              val))))))

;(memoized-factorial 10)
;(memoized-factorial 50)

(define-syntax lazy-cons
  (syntax-rules ()
  ((_ a b) (cons a (delay b)))))

(define (lazy-cdr ls) (force (cdr ls)))
(define lazy-car car)

;(lazy-cdr (lazy-cons 5 10))
;(lazy-car (lazy-cons 5 10))

(define (lazy-ref ls n)
  (if (zero? n) (lazy-car ls)
      (lazy-ref (lazy-cdr ls) (- n 1))))

(define (lazy-head ls n)
  (if (= n 0)
      '()
      (cons (lazy-car ls) (lazy-head (lazy-cdr ls) (- n 1)))))

(define (naturals_start a)
  (lazy-cons a (naturals_start (+ 1 a))))

(define naturals
  (naturals_start 0))

;(lazy-head naturals 12)

(define (fact-gen n)
  (if (<= n 1)
      (lazy-cons 1 (fact-gen 1))
      (lazy-cons n (* (fact-gen (- n 1)) n))
  )
)

(define (lazy-factorial n)
  (lazy-ref (fact-gen n) n))

;(lazy-factorial 10)

(begin
  (display (memoized-factorial 0)) (newline)
  (display (memoized-factorial 1)) (newline)
  (display (memoized-factorial 2)) (newline)
  (display (memoized-factorial 3)) (newline)
  (display (memoized-factorial 4)) (newline)
  (display (memoized-factorial 5)) (newline)
  (display (memoized-factorial 6)) (newline)
  (display (memoized-factorial 7)) (newline)
  (display (memoized-factorial 8)) (newline)
  (display (memoized-factorial 9)) (newline)
  (display (memoized-factorial 10)) (newline)
  (display (memoized-factorial 50)) (newline)
  (display (memoized-factorial 100)) (newline))