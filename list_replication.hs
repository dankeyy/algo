
solve :: Int -> [a] -> [a]
solve n = concatMap (replicate n)

main :: IO ()
main = print $ solve 3 [1..10]