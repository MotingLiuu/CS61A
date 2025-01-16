(define (ascending? s)
    (if (< (length s) 2) 
        #t
        (if (> (car s) (car (cdr s)))
            #f
            (ascending? (cdr s))
        )
    )
)
(define (my-filter pred s) 
    (if (= 0 (length s))
        s
    (if (pred (car s))
        (cons (car s) (my-filter pred (cdr s)))
        (my-filter pred (cdr s))
    )
    )
)

(define (interleave lst1 lst2) 
    (cond 
        ((null? lst1) lst2)
        ((null? lst2) lst1)
        (else (append (list (car lst1) (car lst2)) (interleave (cdr lst1) (cdr lst2))))
    )
)

(define (no-repeats s)
    (if (<= (length s) 1)
        s
        (cons (car s)
            (no-repeats 
                (my-filter (lambda (x) (not (= (car s) x)))
                    (cdr s)
                )
            )
        )
    )
)
