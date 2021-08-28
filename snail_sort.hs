import Data.List ( transpose )

snail :: [[a]] -> [a]
snail [] = []
snail (x:xs) = x ++ (snail . reverse . transpose) xs

main :: IO ()
main = print $ snail [[1, 2, 3], [8, 9, 4], [7, 6, 5]]