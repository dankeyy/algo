-- returns number of character repetitions. aaa bbbb c -> 341 
import Data.List

solve :: String -> String
solve = concatMap (show . length) . group . concat . words

main :: IO ()
main = getLine >>= (putStrLn . solve)