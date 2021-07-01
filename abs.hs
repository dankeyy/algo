
import Data.Foldable ( Foldable(toList) )
import Control.Monad

import Control.Applicative
-- implement abs

abs1 :: [Int] -> [Int]
abs1 = map (\x -> x * signum x)

abs1_5 :: [Int] -> [Int]
abs1_5 = map (ap (*) signum)

abs1_5_5 :: [Int] -> [Int]
abs1_5_5 = map ((*) <*> signum)

abs2 :: [Int] -> [Int]
abs2 list = [x * signum x | x <- list]

abs3 :: [Int] -> [Int]
abs3 list = [if x < 0 then x * (-1) else x | x <- list]