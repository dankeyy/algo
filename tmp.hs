
import Data.List ( group, sort )

rowSumOddNumbers :: Integer -> Integer
rowSumOddNumbers x = sum [start, start+2..end]
  where
    sq = x ^ 2
    start = sq -x +1
    end = sq +x -1


ro :: String -> Int
ro = length . filter ((>1) . length) . group . sort