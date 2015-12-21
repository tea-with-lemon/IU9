(define (difference_squares x y)
    (list '* (list '- x y) (list '+ x y)))

(define (difference_cubes x y)
    (list '* (list '- x y) (list '+ (list 'expt x 2) (list '* x y) (list 'expt y 2))))

(define (summ_cubes x y)
    (list '* (list '+ x y) (list '+ (list 'expt x 2) (list '- (list '* x y)) (list 'expt y 2))))

(define (factorize xs)
  (cond
    ((null? xs) xs)
    ((equal? (car(cdr(cdr(car(cdr xs))))) 2) (let ((x (car(cdr(car(cdr xs))))) (y (car(cdr(car(cdr(cdr xs))))))) (difference_squares x y)))
    ((equal? (car(cdr(cdr(car(cdr xs))))) 3) (cond ((equal? (car xs) '-) (let ((x (car(cdr(car(cdr xs))))) (y (car(cdr(car(cdr(cdr xs))))))) (difference_cubes x y)))
                                                   ((equal? (car xs) '+) (let ((x (car(cdr(car(cdr xs))))) (y (car(cdr(car(cdr(cdr xs))))))) (summ_cubes x y)))))))