#lang racket

(define (non-factors x)
  (for/list ([i (in-range 2 x)]
    #:unless (equal? (remainder x i) 0))
    i))

(define (is not-divisible-by i m)
  (cond
    [(= i 1) #true]
    [else (cond
            [(= (remainder m i) 0) #false]
            [else (is-not-divisible-by (sub1 i) m)])]))

(define (recur-divisible i x)
  (for ([y (in-list i)]
    #:break (not (zero? (remainder x y))))
    (display x)))

(define (small-multi x)
  (for*/first ([i (in-list (non-factors x))]
               #:when (is-not-divisible-by i (* x i)))
    (* i x)))
