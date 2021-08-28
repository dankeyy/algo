import Data.List ( group )
import Control.Arrow ( (&&&) )
import Data.Bifunctor ( first )

-- finding the longest subsequence of increasing & following elements in the list, returning the length of that subseq along with its first index

adjacentPairings :: [a] -> [(a, a)]
adjacentPairings = zip <*> tail

subEq1 :: (Int, Int) -> Bool
subEq1 = uncurry $ (==) . succ


longestTrue :: [Bool] -> (Int, Int)
longestTrue = go 0 (0, 0) . map (head &&& length) . group
  where
    go :: Int -> (Int, Int) -> [(Bool, Int)] -> (Int, Int)
    go idx best [] = best
    go idx best@(count, i) ((truth, n) : xls) -- n == length, truth == (True/False) values from head
        | truth && n > count = go (idx + n) (n, idx) xls
        | otherwise          = go (idx + n) best xls


solve :: [Int] -> (Int, Int)
solve = first succ . longestTrue . map subEq1. adjacentPairings


main :: IO () 
main = print $ solve [7,6,9,10,11,15,16,12,5,6,7,8,9,7,2,3,4]
-- outputs (5 -length, 8 - starting index) because 5,6,7,8,9 is the longest increasing subseq, starting from 8 with a length of 5 
