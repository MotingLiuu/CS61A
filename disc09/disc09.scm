(define (fit total n)
    (define (f total n k)
        (if (and (= n 0) (= total 0))
            #t
            (if (< total (* k k))
            #f
            (or (f (- total (* k k))
                    (- n 1)
                    (+ k 1)
                ) 
                    (f total
                    n
                    (+ k 1)
                )
            )
            )
        )
    )
    (f total n 1)
)

(define list1 (list '(a b) 'c 'd '(e)))
(define list2 '((a b) c d (e)))
(define list3 (cons (cons 'a (cons 'b ())) (cons 'c (cons 'd (cons (cons 'e ()) ())))))

;;; Return a list of pairs containing the elements of s.
    ;;;
    ;;; scm> (pair-up '(3 4 5 6 7 8))
    ;;; ((3 4) (5 6) (7 8))
    ;;; scm> (pair-up '(3 4 5 6 7 8 9))
    ;;; ((3 4) (5 6) (7 8 9))
(define (pair-up s)
    (if (<= (length s) 3)
        (list s)
        (cons (list (car s) (car (cdr s)))
            (pair-up (cdr (cdr s)))
        )
    )
)

(expect (pair-up '(3 4 5 6 7 8)) ((3 4) (5 6) (7 8)) )
(expect (pair-up '(3 4 5 6 7 8 9)) ((3 4) (5 6) (7 8 9)) )