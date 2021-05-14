
import Data.List ( group, sort )
import Control.Monad ( ap )

import qualified Data.Set as Set

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
g = ap ((==) . length . Set.fromList) length