(ns P006)

(def take-first-one-hundred
  (take 100 (iterate inc 1)))

(defn sum-squares
  [n-seq]
  (apply + (map #(* % %) n-seq)))

(defn square-sum
  [n-seq]
  (let [sum (reduce + n-seq)]
    (* sum sum)))

(defn -main
  [n-seq]
  (- (square-sum n-seq)
     (sum-squares n-seq)))
