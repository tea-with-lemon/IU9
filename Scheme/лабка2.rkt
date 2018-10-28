;;convertor   
(define (list-head lst k)
  (if (= k 0)'()
      (cons (car lst) (list-head (cdr lst)(- k 1)))))

(define (vector-head vec k)
  (list->vector(list-head (vector->list vec)k)))

(define (vector-tail vec k)
  (list->vector(list-tail (vector->list vec)k)))

(define (vector-add el vec)
  (list->vector(cons el (vector->list vec))))

(define (veсtor-concat vec1 vec2)
  (list->vector (append (vector->list vec1) (vector->list vec2))))

(define (string-head s k)
  (substring s 0 k))

(define (string-tail s k)
  (substring s k (string-length s)))

(define (string-add el s)
  (list->string (cons el (string->list s))))
  



;;1 chast'
(define (ref xs index . el)
  (cond
    ((list? xs)
     (if (>= index (length xs))
         #f
      (if (null? el)
          (list-ref xs index)
          (append (list-head xs index) (cons (car el) (list-tail xs index))))))
    ((vector? xs)
     (if (>= index (vector-length xs))
         #f
         (if (null? el)
             (vector-ref xs index)
             (veсtor-concat (vector-head xs index) (vector-add (car el)(vector-tail xs index))))))
    ((string? xs)
     (if (>= index (string-length xs))
         #f
         (if (null? el)
             (string-ref xs index)
             (if (char? (car el))
                 (string-append (string-head xs index)(string-add (car el) (string-tail xs index)))
                 #f))))
    (else #f)))

;;tests
(ref '(1 2 3) 1)
(ref #(1 2 3) 1)
(ref "123" 1)  
(ref "123" 3)
(ref '(1 2 3) 1 0) 
(ref #(1 2 3) 1 0)  
(ref #(1 2 3) 1 #\0)
(ref "123" 1 #\0)   
(ref "123" 1 0)     
(ref "123" 3)       
  
