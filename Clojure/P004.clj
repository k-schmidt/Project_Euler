(ns P004)

(defn cartesian-product
  [min max]
  (for [x (range min max)
        y (range min max)]
    ((* x y))))

(def three-digit-cartesian-product
  (cartesian-product 1 1000))

(defn palindrome?
  [n]
  (= (clojure.string/reverse (str n)) (str n)))

(defn -main
  []
  (reduce max (for [x three-digit-cartesian-product
                    y x]
                (if (palindrome? y)
                  y
                  0))))
