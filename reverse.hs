
import Data.List ( foldl' )


rev1 :: [a] -> [a]
rev1 l = [l !! i | i <- [len - 1, len - 2 ..0]]
  where len = length l

rev2 :: [a] -> [a]
rev2 = foldl' (flip (:)) []