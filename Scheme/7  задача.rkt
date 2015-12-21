(define udalit '(#\space #\tab #\newline))
;1 phase
(define (string-trim-left str)
  (let it_be ((lst (string->list str)))
    (cond
      ((memq (car lst) udalit) (it_be (cdr lst)))
      (else (list->string lst)))))

(define (string-trim-right str)
  (let her_go ((lst (reverse (string->list str))))
    (cond
      ((memq (car lst) udalit) (her_go (cdr lst)))
      (else (list->string (reverse lst))))))

(define (string-trim str)
  (string-trim-right (string-trim-left str)))

;2 phase
 (define (string-prefix? a b)
  (let cycle ((i 0))
    (cond
      ((>= i (string-length a)) #t)
      ((>= i (string-length b)) #f)
      ((char=? (string-ref a i) (string-ref b i))
        (cycle (+ i 1)))
      (else #f))))

(define (string-suffix? a b)
  (define (reverse-str k)
    (list->string (reverse (string->list k))))
  (string-prefix? (reverse-str a) (reverse-str b)))

