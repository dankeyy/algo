import Data.List ( intercalate )

-- https://www.hackerrank.com/challenges/apple-and-orange/problem
applesAndOranges :: Int -> Int -> Int -> Int -> [Int] -> [Int] -> [Int]
applesAndOranges s t a b apples oranges = [fellOnHouse a apples, fellOnHouse b oranges]
  where
    fellOnHouse sourceTree = length . filter inHouseRange . positionsBy sourceTree
      where
        positionsBy treeLocation = map (+treeLocation) -- a | b --check
        inHouseRange fruitPos = fruitPos >= s && fruitPos <= t


main :: IO ()
main = do
  [s:t:_, a:b:_, _, apples, oranges] <- map parseLine . lines <$> getContents 
  pprint $ applesAndOranges s t a b apples oranges
  
    where 
      parseLine = map (read :: String -> Int) . words 
      pprint res = putStrLn $ intercalate "\n" $ map show res