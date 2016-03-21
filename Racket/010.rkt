#lang racket

#|
Find the sum of all primes below two million.
|#

(define (divides? a b)
  (= (modulo a b) 0))

(define (sieve n)
  (local
    ((define lst (rest (build-list n add1)))
     (define (remove-multiples lst)
       (cond
         ((> (first lst) (floor (sqrt n))) lst)
         ((cons (first lst)
                (remove-multiples (filter (lambda (i) (not (divides? i (first lst))))
                                          lst)))))))
    (remove-multiples lst)))

(apply + (sieve 2000000))