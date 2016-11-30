(ns P005)

(def divisible-by-20
  (iterate (partial + 20) 20))

(defn divisible-by-range-20
  [n]
  (let [range-20 (range 1 21)]
    (every? #(zero? (mod n %)) range-20)))

(defn -main
  []
  (first (filter #(divisible-by-range-20 %) divisible-by-20)))
