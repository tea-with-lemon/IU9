(define break
  (lambda (arg)
    (let ((exit-procedure
           (lambda (continuation)
             (set! resume-computation (lambda () (continuation arg)))
             (write-line "Execution paused. Try (resume-computation)")
             ((escaper (lambda () arg))))))
      (call/cc exit-procedure))))

(define escape-thunk (lambda () "escape-thunk Initialized"))

(define escape-thunk-init (lambda (continue) (set! escape-thunk continue)))

((call/cc escape-thunk-init))

(define escaper
  (lambda (procedure)
    (lambda args
      (escape-thunk (lambda () (apply procedure args))))))