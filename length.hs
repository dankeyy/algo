-- implementing length
len1 :: [a] -> Int
len1 lst = sum [ 1 | _ <- lst]

len2 :: [a] -> Int
len2 lst = if null lst then 0 else 1 + len2 (tail lst) 

len3 :: [a] -> Int
len3 = sum . map (const 1)

len4 :: [a] -> Int
len4 [] = 0
len4 (x:xs) = 1 + len4 xs

len5 :: [a] -> Int
len5 = foldr (\_ -> (+) 1) 0

len6 :: [a] -> Int
len6 = foldr ((+) . const 1) 0

len7 :: [a] -> Int
len7 = foldr (const succ) 0
