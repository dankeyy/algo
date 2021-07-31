import Data.List ( intercalate )
import Data.List.Split ( splitOn )
import Text.Printf ( printf )

-- https://www.hackerrank.com/challenges/time-conversion/problem
timeConversion :: String -> String
timeConversion s = intercalate ":" $ printf "%02d" <$> (militaryHour:rest)
  where
    format = drop 8 s
    (h:rest) = map (read :: String -> Int) (splitOn ":" $ take 8 s)
    militaryHour 
      | format == "AM" && h == 12  = 0 
      | format == "PM" && h /= 12  = h + 12
      | otherwise                  = h

main :: IO ()
main = interact timeConversion