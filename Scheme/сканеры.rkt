;<SignInteger>::= <Sign><UnsignInteger>|<UnsignInteger>.
;<UnsignInteger>::=<Digit>|<Digit><UnsignInteger>.
;<Digit>::='0'|'1'|...|'9'.
;<Sign>::='+"|'-'.

(define (digit d)
  (cond
    ((char-numeric? d) (- (char->integer d) (char->integer #\0)))
    (else (+ 10 (- (char->integer (char-downcase d)) (char->integer #\a))))))

