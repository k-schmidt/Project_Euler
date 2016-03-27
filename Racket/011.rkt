#lang racket                                                                    
                                                                                
#|                                                                              
What is the greatest product of four adjacent numbers in the same direction in the 20x20 grid?
|#                                                                              
                                                                                
(require racket/string)                                                         
                                                                                
;;(define DATA-PATH                                                               
;;  (build-path (current-directory) "data" "011.dat"))                            

(define DATA-PATH
  (build-path "Documents" "Project_Euler" "Racket" "data" "011.dat"))

(define DATA-STRING-LIST                                                        
  (string-split                                                                 
    (string-replace (file->string DATA-PATH) "\n" " ") " "))                    
                                                                                
(define (remove-space l)                                                        
  (cond                                                                         
    ((null? l) '())                                                             
    (else (cons (list (car l) (cadr l)) (remove-space (cdddr l))))))            
                                                                                
(define (string->number-list data)                                              
  (map (lambda (x) (string->number x))                                                    
       data))                                                                   
                                                                                
(define (zip-hash l)                                                                 
  (make-hash
   (map (lambda (x y) (list x y))
        (for*/list ((i (in-range 1 21))                                   
                    (j (in-range 1 21)))                                  
          (list j i))
        (string->number-list l))))
  
(zip-hash DATA-STRING-LIST)
(car (hash-ref (zip-hash DATA-STRING-LIST) '(1 1)))