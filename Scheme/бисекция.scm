(define (bisection f a b ε)
  (define c (/(+ b a)2))
  (cond
    ((< (abs(f a)) ε) a)
    ((< (abs(f b)) ε) b)
    ((> (* (f a) (f c)) 0)(bisection f b c ε))
    (else (bisection f a c ε))))
    
