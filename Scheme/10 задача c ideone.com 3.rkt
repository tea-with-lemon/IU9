(define (productl sum xs)
    (if (list? xs)
        (if (null? xs)
	    sum
	    (if (= (car xs) 0)
		(productl sum (cdr xs))
		(productl (* sum (car xs)) (cdr xs))))
	sum))
 
(define (proverkal? xs)
    (if (null? xs)
	(and 
	    (integer? (car xs))
	    (<= 0 (car xs))
	    (proverkal? (cdr xs)))))
 
(define (make-multi-vector xs . arg)
    (let ((n (length xs))
	(r (productl 1 xs)))
	(if (and (not (null? xs)) (proverkal? xs))
	    (list->vector (cons n (append xs (vector->list
		(if (null? arg)
		    (make-vector r)
		    (make-vector r (car arg)))))))
	    "error")))
 
(define (productv v sum n)
    (if (= n 0)
	sum
	(if (= (vector-ref v n) 0)
	    (productv v sum (- n 1))
	    (productv v (* sum (vector-ref v n)) (- n 1)))))
 
(define (proverkav? v n)
    (if (= n 0)
	#t
	(and 
	    (integer? (vector-ref v n))
	    (<= 0 (vector-ref v n))
	    (proverkav? v (- n 1)))))
 
(define (multi-vector? v)
    (and (vector? v)
	 (< (vector-ref v 0) (vector-length v))
	 (proverkav? v (vector-ref v 0))
         (= (+ 1 (vector-ref v 0) (productv v 1 (vector-ref v 0))) (vector-length v))))
 
(define (proverkar v v2 n)
    (if (< 0 n)
	(and 
	    (> (vector-ref v n) (vector-ref v2 (- n 1))) 
	    (proverkar v v2 (- n 1)))
	#t))
 
(define (productr v v2 n sum sum2)
    (if (= n 0)
	sum
	(productr v v2 (- n 1) 
	    (+ sum (* sum2 (vector-ref v2 (- n 1)))) 
	    (if (= sum2 0)
		sum2
		(* sum2 (vector-ref v n))))))
 
(define (multi-vector-ref v xs)
    (and (multi-vector? v)
	 (proverkar v (list->vector xs) (vector-ref v 0))
	 (= (length xs) (vector-ref v 0))
	 (vector-ref v (+ 1 (vector-ref v 0) (productr v (list->vector xs) (vector-ref v 0) 0 1)))))
 
(define (multi-vector-set! v xs k)
    (if (and (multi-vector? v)
	     (proverkar v (list->vector xs) (vector-ref v 0))
	     (= (length xs) (vector-ref v 0))
	     (vector-set! v (+ 1 (vector-ref v 0) (productr v (list->vector xs) (vector-ref v 0) 0 1)) k))
	#f))