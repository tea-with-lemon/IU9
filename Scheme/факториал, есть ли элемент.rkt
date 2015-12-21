(define (factorial n)
	(cond
;факториал 0! равен 1
		((= n 0) 1)
;факториал n! равен (n-1)!*n
		((* (factorial (- n 1)) n))))

(define (power x n)
	(cond
          ((= n 0) 1)
          ((* x (power x (- n 1))))))

(define (family el list)
  (and
   (not (null? list))
   (or (equal? el (car list))
       (family el (cdr list)))))

