(define-macro (mystery-macro expr old new)
    (mystery-helper expr old new))

(define (mystery-helper e o n)
  (if (pair? e)
      (cons (mystery-helper (car e) o n) (mystery-helper (cdr e) o n))
      (if (eq? e o) n e)))

(define-macro (assign sym1 sym2 expr1 expr2)
    (list 'begin
        (list 'define 'tmp expr1)
        (list 'define sym1 expr2)
        (list 'define sym2 'tmp)
    )
)

(define-macro (switch expr cases)
  `(let ((val ,expr))
     (cond
       ,@(map (lambda (case)
                `((equal? val ,(car case)) ,(car (cdr case))))
              cases))))


(switch (+ 1 1) (
    (1 (print 'a))
    (2 (print 'b))
    (3 (print 'c))
    )
)