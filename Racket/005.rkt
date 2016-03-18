#lang racket

(define (non-factors x)
  (for/list ([i (in-range 2 x)]
    #:unless (equal? (remainder x i) 0))
    i))

(define (recur-divisible i x)
  (for ([y (in-list i)]
    #:break (not (zero? (remainder x y))))
    (display x)))

(define (small-multi x)
  (for*/first ([i (in-naturals 2)]
               [y (in-list (non-factors x))]
               #:when (zero? (modulo (* i x) y)))
    (* i x)))
