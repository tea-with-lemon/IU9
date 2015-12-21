(define-syntax when 
  (syntax-rules()
    ((when a expr ...)
     (if a 
         (begin expr ...)))))

(define-syntax unless 
  (syntax-rules()
    ((unless a expr ...)
     (if (not a) (begin expr ...)))))

(define-syntax for 
  (syntax-rules (in as)
    ((for i in lst expr ...)
     (for-each (lambda (i) expr ...)
          lst))
    ((for lst as i expr ...)
     (for i in lst expr ...))))

(define-syntax while
  (syntax-rules ()
    ((while a expr ...)
     (let loop ()
       (if a (begin expr ... (loop)))))))

(define-syntax repeat
  (syntax-rules (until)
    ((repeat (expr ...) until a)
     (let loop ()
        expr ...
       (if (not a) (loop))))))

(define-syntax cout
  (syntax-rules ()
    ((cout args ...)
     (letrec ((rec (lambda (lst i)
                     (cond ((not (null? lst)) (if (even? i)
                                                  (cond ((equal? (car lst) 'endl) (newline))
                                                        (else (display (car lst))))) 
                                              (rec (cdr lst) (+ i 1)))))))
       (rec (list 'args ... '()) 1)))))