
rules :: [(Int, String)]
rules = [(3, "fizz"), (5, "buzz")]


divisibleBy :: Integral a => a -> a -> Bool
divisibleBy n m = mod n m == 0

infix 0 <|>
(<|>) :: [a] -> [a] -> [a]
n <|> [] = n
_ <|> xs = xs

----------------------------------------------------------------

fb1 :: [String]
fb1 = 
  [
    max
    (show n) 
    (concat [fizzbuzz | (r, fizzbuzz) <- rules, n `divisibleBy` r])
    | n <- [1..]
  ]

main13 :: IO ()
main13 = mapM_ putStrLn $ take 100 fb1

----------------------------------------------------------------

fb2 :: Int -> String
fb2 n = show n <|> concat [ fizzbuzz | (r, fizzbuzz) <- rules, n `divisibleBy` r ]


main2 :: IO ()
main2 = mapM_ (putStrLn . fb2) [1..100]

----------------------------------------------------------------

fb3 :: [String]
fb3 = zipWith3 (\n f b -> n <|> (f ++ b))
              (map show [1..])
              (cycle ["", "", "fizz"]) 
              (cycle ["", "", "", "", "buzz"]) 
