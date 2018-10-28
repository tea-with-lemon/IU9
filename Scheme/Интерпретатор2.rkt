(load "юнит тест.scm")
(define (interpret vec data-st)
  (define (point-interpret ind data-st return-st dictionary)
    (if (= ind (vector-length vec))
        data-st
        (let ((elem (vector-ref vec ind)))
          (cond ((number? elem) (point-interpret (+ ind 1) (cons elem data-st) return-st dictionary))
                ((equal? elem 'drop) (point-interpret (+ ind 1) (cdr data-st) return-st dictionary))
                ((equal? elem 'swap) (point-interpret (+ ind 1) (cons (cadr data-st) (cons (car data-st) (cddr data-st))) return-st dictionary))
                ((equal? elem 'dup) (point-interpret (+ ind 1) (cons (car data-st) data-st) return-st dictionary))
                ((equal? elem 'over) (point-interpret (+ ind 1) (cons (cadr data-st) data-st) return-st dictionary))
                ((equal? elem 'rot) (point-interpret (+ ind 1) (append (list (caddr data-st) (cadr data-st) (car data-st)) (cdddr data-st)) return-st dictionary))
                ((equal? elem 'depth) (point-interpret (+ ind 1) (cons (length data-st) data-st) return-st dictionary))
                ((member elem '(+ - * /)) (point-interpret (+ ind 1) (cons (eval (list elem (cadr data-st) (car data-st)) (interaction-environment)) (cddr data-st)) return-st dictionary))
                ((equal? elem 'mod) (point-interpret (+ ind 1) (cons (remainder (cadr data-st) (car data-st)) (cddr data-st)) return-st dictionary))
                ((equal? elem 'neg) (point-interpret (+ ind 1) (cons (- (car data-st)) (cdr data-st)) return-st dictionary))
                ((member elem '(= < >)) (point-interpret (+ ind 1) (cons (if (eval (list elem (cadr data-st) (car data-st)) (interaction-environment))
                                                                             -1
                                                                             0) (cddr data-st)) return-st dictionary))
                ((equal? elem 'not) (point-interpret (+ ind 1) (cons (if (= (car data-st) 0)
                                                                         -1
                                                                         0) (cdr data-st)) return-st dictionary))
                ((equal? elem 'and) (point-interpret (+ ind 1) (cons (if (and (= (car data-st) -1) (= (cadr data-st) -1))
                                                                         -1
                                                                         0))))
                ((equal? elem 'or) (point-interpret (+ ind 1) (cons (if (or (= (car data-st) -1) (= (cadr data-st) -1))
                                                                        -1
                                                                        0))))
                ((equal? elem 'define) (point-interpret (def-count vec ind) data-st return-st (cons (list (vector-ref vec (+ ind 1)) (+ ind 2)) dictionary)))
                ((or (equal? elem 'end) (equal? elem 'exit)) (point-interpret (car return-st) data-st (cdr return-st) dictionary))
                ((equal? elem 'if) (point-interpret (if (not (= (car data-st) 0))
                                                        (+ ind 1)
                                                        (if-count vec ind)) (cdr data-st) return-st dictionary))
                ((equal? elem 'endif) (point-interpret (+ ind 1) data-st return-st dictionary))
                (else (point-interpret (cadr (assoc elem dictionary)) data-st (cons (+ ind 1) return-st) dictionary))))))
  (point-interpret 0 data-st '() '()))

(define (def-count vec ind)
  (if (equal? (vector-ref vec ind) 'end)
      (+ ind 1)
      (def-count vec (+ ind 1))))

(define (if-count vec ind)
  (if (equal? (vector-ref vec ind) 'endif)
      (+ ind 1)
      (if-count vec (+ ind 1))))


(define the-tests
  ( list 
(test (interpret #(   define abs 
                          dup 0 < 
                          if neg endif 
                      end 
                      9 abs 
                      -9 abs ) (quote ())) '(9 9))

(test (interpret #(   define =0? dup 0 = end 
                      define <0? dup 0 < end 
                      define signum 
                          =0? if exit endif 
                          <0? if drop -1 exit endif 
                          drop 
                          1 
                      end 
                      0 signum 
                      -5 signum 
                      10 signum ) (quote ())) '(1 -1 0))

(test (interpret #(   define — 1 - end 
                      define =0? dup 0 = end 
                      define =1? dup 1 = end 
                      define factorial 
                          =0? if drop 1 exit endif 
                          =1? if drop 1 exit endif 
                          dup — 
                          factorial 
                          * 
                      end 
                      0 factorial 
                      1 factorial 
                      2 factorial 
                      3 factorial 
                      4 factorial ) (quote ())) '(24 6 2 1 1))

(test (interpret #(   define =0? dup 0 = end 
                      define =1? dup 1 = end 
                      define — 1 - end 
                      define fib 
                          =0? if drop 0 exit endif 
                          =1? if drop 1 exit endif 
                          — dup 
                          — fib 
                          swap fib 
                          + 
                      end
                      define make-fib 
                          dup 0 < if drop exit endif 
                          dup fib 
                          swap — 
                          make-fib 
                      end 
                      10 make-fib ) (quote ())) '(0 1 1 2 3 5 8 13 21 34 55))

(test (interpret #(   define =0? dup 0 = end 
                      define gcd 
                          =0? if drop exit endif 
                          swap over mod 
                          gcd 
                      end 
                      90 99 gcd 
                      234 8100 gcd ) '()) '(18 9))))

(run-tests the-tests)