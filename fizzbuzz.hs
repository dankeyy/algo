
fizzbuzz :: IO ()
fizzbuzz = mapM_ putStrLn
  [
    max 
    (show x) 
    (concat [fb | (n, fb) <- [(3, "Fizz"),(5, "Buzz")], x `mod` n == 0])
    | x <- [1..100]
  ]