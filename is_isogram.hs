import Data.Char ( toLower )
import Data.List ( (\\) )
import qualified Data.Set as Set

-- is a given string an isogram

isogram1 :: String -> Bool
isogram1 x = length (Set.fromList s) == length s
  where s = map toLower x


isogram2 :: String -> Bool
isogram2 = null . (\\ ['a'..'z']) . map toLower