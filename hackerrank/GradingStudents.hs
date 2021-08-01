import Control.Monad ( replicateM_ )

-- https://www.hackerrank.com/challenges/grading/problem

finalGrade:: Int -> Int
finalGrade g
  | g > 35 && gmod5 > 2 = g + 5 - gmod5
  | otherwise = g
  where gmod5 = g `mod` 5

main :: IO ()
main = readLn >>= flip replicateM_ (print . finalGrade =<< readLn)
