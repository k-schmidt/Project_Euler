(ns P002)

(def fib-seq-iterate
  (map first (iterate
              (fn [[a b]] [b (+ a b)]) [0 1])))

(defn -main
  []
  (apply + (filter even? (take-while (partial > 4000000) fib-seq-iterate))))
