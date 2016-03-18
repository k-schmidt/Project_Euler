#lang racket

#|What is the smallest positive number that is evenly
divisible by all of the numbers from 1 to 20?
|#

(define (non-factors x)
  (for/list ([i (in-range 2 x)]
    #:unless (equal? (remainder x i) 0))
    i))

(define (is-not-divisible-by i m)
  (if (null? i) m
      (if (zero? (remainder m (first i)))
          (is-not-divisible-by (rest i) m)
          #false)))

(define (small-multi x)
  (let ([j (non-factors x)])
    (for/first ([k (in-naturals 1)]
                 #:when (is-not-divisible-by j (* k x)))
      (* k x))))