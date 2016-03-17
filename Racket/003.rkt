#lang racket

;; What is the largest prime factor of the number 600851475143?

(define (sieve x)
  (sieve-iter x 2))

(define (sieve-iter x max-prime)
  (if (> x max-prime)
      (if (= (remainder x max-prime) 0)
          (sieve-iter (/ x max-prime) 2)
          (sieve-iter x (add1 max-prime)))
      (display max-prime)))

(sieve 600851475143)
