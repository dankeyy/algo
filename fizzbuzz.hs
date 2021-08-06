
rules = [(3, "fizz"), (5, "buzz")]

divisibleBy n m = mod n m == 0

n <|> [] = show n
_ <|> xs = concat xs
----------------------------------------------------------------

fb1 :: IO ()
fb1 = mapM_ putStrLn
  [
    max
    (show x) 
    (concat [fizzbuzz | (n, fizzbuzz) <- rules, x `divisibleBy` n])
    | x <- [1..100]
  ]

----------------------------------------------------------------

fb2 :: Int -> String
fb2 n = n <|> [ fizzbuzz | (r, fizzbuzz) <- rules, n `divisibleBy` r]


main2 ::IO ()
main2 = mapM_ (putStrLn . fb2) [1..100]

----------------------------------------------------------------

