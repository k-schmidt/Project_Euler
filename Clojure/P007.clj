(ns P007)

(defn prime?
  [n]
  (cond (<= n 1) false
        (= n 2) true
        :else (loop [f 2]
                (cond (zero? (mod n f)) false
                      (> f (Math/sqrt n)) true
                      :else (recur (inc f))))))

(defn -main
  ([](-main 10001))
  ([n] (first (drop (dec n) (filter prime? (iterate inc 1))))))
