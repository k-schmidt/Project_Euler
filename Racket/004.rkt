#lang racket

;; Find the largest palindrome made from the product of two 3-digit numbers.

(define (equal-reverse x)
  (let ([y (string->list (number->string x))])
  (equal? y (reverse y))))

(define (greatest-palindrome x y)
  (apply max
   (for*/list ([i (in-range x 2 -1)]
              [j (in-range y 2 -1)]
              #:when (equal-reverse (* i j)))
              (* i j))))
