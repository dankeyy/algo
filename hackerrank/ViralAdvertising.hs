import Data.List ( foldl' )
-- https://www.hackerrank.com/challenges/strange-advertising

cumulative :: Int -> Int
cumulative n = sum $ foldl' (\(x:xs) _ -> (x*3) `div` 2 : (x:xs)) [2] [2..n]

main :: IO ()
main = print . cumulative . read =<< getLine