(ns P001)

(defn multiple-of-3?
  [n]
  (zero? (mod n 3)))

(defn multiple-of-5?
  [n]
  (zero? (mod n 5)))

(defn multiples-of-3-and-5
  [m]
  (loop [n 0 sum 0]
    (if (= n m)
      sum
      (if (or (multiple-of-3? n) (multiple-of-5? n))
        (recur (inc n) (+ sum n))
        (recur (inc n) sum)))))

(multiples-of-3-and-5 1000)
