(ns ann.core)

(defn- dot-product
  [v1 v2]
  (reduce + (map * v1 v2)))

(defn random-weights
  "Generate n random positive OR negative weights"
  [n]
  (take n (repeatedly #(- 0.5 (rand)))))

(defn perceptron []
  {:weights []
   :learning-rate 0.1})

(defn threshold? [n]
  (if (> n 0) 1 -1))

(defn update-weights [perceptron])

(defn feed-forward [perceptron])
