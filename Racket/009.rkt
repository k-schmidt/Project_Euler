#lang racket

#|
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
|#

(define (find-c i j)
  (sqrt (+ (sqr i) (sqr j))))

(define (pythagorean-triple)
  (for* ((i (in-range 3 999 3))
         (j (in-range 4 1000 4))
         #:when (= (+ i j (find-c i j)) 1000))
    (display (* i j (find-c i j)))))
