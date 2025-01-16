(define (over-or-under num1 num2) (cond 
  ((< num1 num2) -1)
  ((= num1 num2) 0)
  (else 1)
))

(define (make-adder num) (define (adder x) (+ x num)) adder)

(define (composed f g) (define (fg x) (f (g x))) fg)

(define (repeat f n)
  (define (repeat_n n x)
    (if (= n 0) x (f (repeat_n (- n 1) x))))
  (define (func x)
    (repeat_n n x))
  func)

(define (max a b)
  (if (> a b)
      a
      b))

(define (min a b)
  (if (> a b)
      b
      a))

(define (gcd a b) 
  (if (= 0 (modulo (max a b) (min a b)))
      (min a b)
      (gcd (min a b) (modulo (max a b) (min a b)))
  ))
