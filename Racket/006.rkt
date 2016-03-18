#lang racket

#| Find the difference between the sum of the squares of the first
one hundred natural numbers and the square of the sum.
|#

(define (sum-reduce max)
  (for/sum ([x (in-range (add1 max))])
    x))

(define (sum-sqr max)
  (for/sum ([x (in-range (add1 max))])
    (sqr x)))

(define (sqr-reduce-diff max)
  (- (sqr (sum-reduce max)) (sum-sqr max)))