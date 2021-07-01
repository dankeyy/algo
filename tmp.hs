{-# LANGUAGE LambdaCase #-}
-- {-# LANGUAGE LambdaCase #-}

import Data.List

import Data.List.Split
import Control.Monad
import Data.Ord
import Data.Function
import Control.Applicative

import qualified Data.Set as Set

import Data.Complex

-- {-# LANGUAGE LambdaCase #-}

rowSumOddNumbers :: Integer -> Integer
rowSumOddNumbers x = sum [start, start+2..end]
  where
    sq = x ^ 2
    start = sq -x +1
    end = sq +x -1


-- ro :: String -> Int
-- ro = length . filter ((>1) . length) . group . sort

f :: String -> Bool
f x = length (Set.fromList x) == length x 

g :: String -> Bool
g = (==) . length . Set.fromList <*> length


subtractedDiffs:: Num a => [a] -> [a]
subtractedDiffs = zipWith (-) <*> tail

-- diffs :: [b] -> [(b,b)]
-- diffs x = zip x (tail x)
  
lowestGappedCoins :: Num b => Ord b => [b] -> (b, b)
lowestGappedCoins = minimumBy (comparing differences) . adjacentPairings . sort
  where
    differences = abs . uncurry (-)
    adjacentPairings = zip <*> tail


{-# LANGUAGE LambdaCase #-}

parenthesisDepth :: String -> Int
parenthesisDepth = maximum
      . scanl (+) 0
      . map (\case '(' ->  1 
                   ')' -> -1 
                   _   ->  0)


splitOn' :: String -> String -> [String]
splitOn' delims s = start : if null end then [] else splitOn' delims (tail end)
  where (start, end) = break (`elem` delims) s


inArray :: [String] -> [String] -> [String]
inArray a1 a2 = if any null (a1, a2) 
                then []
                else nub $ sort $ filter (`isSub`  unwords a2) a1
  where isSub sub string = any (sub `isPrefixOf`) (tails string)



aoc2015d3 :: Char -> (Int, Int)
aoc2015d3 c = case c of 
  '^' -> ( 0,  1)
  'v' -> ( 0, -1) 
  '<' -> (-1,  0)
  '>' -> ( 1,  0)
  _ -> error $ c : "invalid character"

