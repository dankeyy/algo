
roman :: Integer -> String
roman 0 = ""
roman n = letter ++ roman (n - closestNum)
  where 
    (closestNum, letter) = head $ filter ((<=n) . fst) romanTable
    romanTable = zip [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]