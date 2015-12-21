(define-syntax when 
  (syntax-rules()
    ((when x expr ...)
     (if x 
         (begin expr ...)))))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(define-syntax unless 
  (syntax-rules()
    ((unless x expr ...)
     (if (not x) (begin expr ...)))))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  (define-syntax for
    (syntax-rules (in as)
      ((for element in list body ...)
       (map (lambda (element)
              body ...)
            list))
      ((for list as element body ...)
       (for element in list body ...))))
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  (define-syntax while
    (syntax-rules ()
      ((while condition body ...)
       (let loop ()
         (if condition
             (begin
               body ...
               (loop)))))))
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  (define-syntax repeat
    (syntax-rules (until)
      ((repeat (expr ...) until x)
       (let loop ()
         expr ...
         (if (not x) (loop))))))
  ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
  (define-syntax cout
    (syntax-rules ()
      ((cout args ...)
       (letrec ((rec (lambda (lst i)
                       (cond ((not (null? lst)) (if (even? i)
                                                    (cond ((equal? (car lst) 'endl) (newline))
                                                          (else (display (car lst)))))
                                                (rec (cdr lst) (+ i 1)))))))
         (rec (list 'args ... '()) 1)))))
  