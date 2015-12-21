(define-syntax my-if
  (syntax-rules()
    ((_ pred? true false)
    (force (or(and pred? (delay true)) (delay false))))))