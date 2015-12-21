(define (selection-sort pred? lst)
  (define (poisk lst a)            
    (cond ((null? lst) a)
          ((pred? (car lst) a) (poisk (cdr lst)(car lst)))
          (else (poisk (cdr lst) a))))
  (define (remove lst a)              
  (cond ((null? lst) '())           
        ((equal? (car lst) a) (cdr lst))   
        (else (cons (car lst)(remove (cdr lst) a)))))
  (if (null? lst) '()
      (cons (poisk lst (car lst))
            (selection-sort pred?(remove lst (poisk lst (car lst)))))))






(define (insertion-sort pred? lst)
  (define (insert x lst)
    (if (null? lst) (list x)
        (if (pred? x (car lst))
            (cons x lst)
            (cons (car lst) (insert x (cdr lst))))))
  (if (null? lst)'()
      (insert (car lst)
              (insertion-sort pred? (cdr lst)))))