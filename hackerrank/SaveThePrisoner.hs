import Control.Monad (replicateM_)

-- https://www.hackerrank.com/challenges/save-the-prisoner/


-- naive but intuitive 
-- f :: Int -> Int -> Int -> Int
-- f n m s = last . take m . drop (s-1) $ cycle [1..n]


saveThePrisoner :: Int -> Int -> Int -> Int
saveThePrisoner n m s = let res = (s - 1 + m) `mod` n
  in case res of
    0 -> n
    _ -> res


main :: IO ()
main = readLn >>= flip replicateM_ ( 
  do
    (n:m:s:_) <- map read . words <$> getLine
    print $ saveThePrisoner n m s 
  )