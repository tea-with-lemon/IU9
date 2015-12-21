(define (newton f fn  x0 ε)
  (if (<= (abs(f x0)) ε)
       x0
       (newton f fn ( - x0 ( / (f x0) (fn x0))) ε)))

(define ideal (/ (+ 1 (sqrt 5)) 2))
(define (c b a)(/ (- a b) ideal))
(define (golden f x0 x1 ε)
  (if (< (abs (- x1 x0)) ε)
      (/ (+ x0 x1) 2)
      (if (>= (f (- x1 (c x0 x1))) (f (+ x0 (c x0 x1))))
          (golden f (- x1 (c x0 x1)) x1 ε)
          (golden f x0 (+ x0 (c x0 x1)) ε))))
      
;test
(round
 (newton (lambda (x) (* x x)) 
         (lambda (x) (* 2 x)) 
         1.0 1e-8))
  
(round
 (newton (lambda (x) (+ (* x x) (* 4 x) 4)) 
         (lambda (x) (+ (* 2 x) 4)) 
         5.0 1e-8))
  
(round (golden (lambda (x) (* x x)) 
               -2.0 2.0 1e-08))
  
(round (golden (lambda (x) (+ (* x x) (* 4 x) 4)) 
               -5.0 5.0 1e-06))




                       

