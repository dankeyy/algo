
import Data.List ( group )
import Data.Char ( toLower )

-- task 1: double letters in a given string with the exception of "aeiou" letters
-- task 2: undouble those letters

undoubleLetter :: [Char] -> [Char]
undoubleLetter = map head . group . map toLower

doubleLetter :: [Char] -> [Char]
doubleLetter = concatMap (\x -> if x `elem` "aeiou" then [x] else replicate 2 x)

-- half baked undouble alternatives
ud2 :: String -> String
ud2 = concatMap bisect . group 
  where
    bisect x = take ((length x + 1) `div` 2) x


ud3:: String -> String
ud3 = concatMap (\x -> take ((length x + 1) `div` 2) x) . group 