
solve1 :: [a] -> [a]
solve1 = map snd . filter (even . fst) . zip [0..] 

solve2 :: [a] -> [a]
solve2 lst = [x | x <- lst, i <- [0..], even i]

solve3 :: [a] -> [a]
solve3 (_:x:xs) = x : solve3 xs
solve3 _ = []