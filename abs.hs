
import Data.Foldable ( Foldable(toList) )
-- implement abs

abs1 :: [Int] -> [Int]
abs1 = map (\x -> x * signum x)

abs2 :: [Int] -> [Int]
abs2 lst = [x * signum x | x <- lst]

abs3 :: [Int] -> [Int]
abs3 lst = [if x < 0 then x * (-1) else x | x <- lst]
