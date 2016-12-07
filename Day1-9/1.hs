import Data.List.Split
import qualified Data.Text as Text


data Direction = R | L deriving Show

main = do
    input <- readFile "1.txt"
    let steps = [case head str of
                                'L' -> (L, read (tail str) :: Int)
                                'R' -> (R, read (tail str) :: Int)
                | str <- splitOn ", " input]
    print $ steps
