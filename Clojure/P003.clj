(ns P003)

(defn prime?
  [n]
  (= 2 (reduce + (for [i (range 1 (inc n))]
                   (if (zero? (mod n i))
                     1
                     0)))))

(defn num-iter
  []
  (iterate inc 2))

(defn greatest-prime-of
  [number]
  (reduce max (filter #(and (zero? (mod number %)) (prime? %))
                      (take-while #(< % (Math/sqrt number)) (num-iter)))))
