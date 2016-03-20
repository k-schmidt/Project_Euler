#lang racket

(define DATA-PATH
  (build-path (current-directory) "data" "008.dat"))

(define DATA-STRING-LIST
  (string->list
   (string-replace (file->string DATA-PATH)
                   "\n"
                   "")))

(define (string->number-list data) 
  (map (lambda (x)
         (string->number (string x)))
       data))

(define (take-n n data)
  (cond
    ((< (length data) n) '())
    ((null? data) '())
    (else (cons (take data n) (take-n n (drop data 1))))))

(define (multi-list-elements data)
  (cond
    ((null? data) '())
    (else
     (cons (apply * (car data)) (multi-list-elements (cdr data))))))

(define (max l)
  (if (null? l)
      #f
      (foldl (lambda (a b) (if (> a b) a b))
             (car l)
             (cdr l))))

(define (largest-product-of-13-ints data)
  (max (multi-list-elements (take-n 13 (string->number-list data)))))

(largest-product-of-13-ints DATA-STRING-LIST)