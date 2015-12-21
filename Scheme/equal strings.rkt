
(define ==
  (lambda (x y)
    (if (and (string? x) (string? y))
        (string=? x y)
        (if (or (string? x) (string? y))
            (= 1 0)
            (equal? x y)))))
