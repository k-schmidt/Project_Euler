#lang racket

(define (prime? p m)
  (if (null? p) m
      (if (zero? (remainder m (first p)))
          #false
          (prime? (rest p) m))))

(define (prime-number-index x)
  (let ([p '(2)])
    (for ([i (in-naturals 1)])
      (if (prime? p i)
          (cons i p)