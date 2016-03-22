#lang racket

#|
What is the greatest product of four adjacent numbers in the same direction in the 20x20 grid?
|#

(require racket/string)

(define DATA-PATH
  (build-path (current-directory) "data" "008.dat"))

(define DATA-STRING-LIST
  (string->list
   (string-replace (file->string DATA-PATH) "\n" "")))

(define (zip l)
  (map cons l (for*/list ((i (in-range 1 21))
                 (j (in-range 1 21)))
                (list j i))))
