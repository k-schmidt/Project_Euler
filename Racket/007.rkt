#lang racket

#| What is the 10,001st prime number?
Not a very fast solution
|#

(define INIT-PRIMES '(2))

(define (prime? primes a)
  (cond
    [(null? primes) #true]
    [(not (zero? (remainder a (first primes)))) (prime? (rest primes) a)]
    [else #false]))

(define (get-prime nth primes a)
  (cond
    [(equal? nth (length primes)) (first primes)]
    [(prime? primes a) (get-prime nth (cons a primes) (add1 a))]
    [else (get-prime nth primes (add1 a))]))

(define (nth-prime n)
  (get-prime n INIT-PRIMES 3))

(nth-prime 10001)