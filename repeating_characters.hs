-- returns number of character repetitions. aaabbbbc -> 341 
import Data.List

solve :: String -> String
solve = concatMap (show. length) . group . concat . words

main :: IO ()
main = do 
    word <- getLine
    putStrLn $ solve word