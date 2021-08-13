

primes :: [Int]
primes = sieve [2..]


sieve :: [Int] -> [Int]
sieve [] = []
sieve (x:xs) = x : sieve [n | n <- xs, mod n x /= 0]


twins :: [(Int, Int)]
twins = filter (\(x, y) -> y - x == 2) $ zip primes (tail primes)
