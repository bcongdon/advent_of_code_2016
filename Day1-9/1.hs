import Data.List.Split
import Data.List

import qualified Data.Text as Text



data Direction = R | L deriving Show

turn compass dir = mod (compass + case dir of R -> 1
                                              L -> -1) 4

move prev (dir, n) = case last prev of
                    (compass, x, y) -> case turn compass dir of
                        0 -> [(0, x, y + i) | i <- [0..n]]
                        1 -> [(1, x + i, y) | i <- [0..n]]
                        2 -> [(2, x, y - i) | i <- [0..n]]
                        3 -> [(3, x - i, y) | i <- [0..n]]

part1 steps = 
    foldr (++) [] $ scanl move [(0, 0, 0)] steps



firstDup (x:xs) =
    case elem x xs of
        True -> x
        False -> firstDup xs

main = do
    input <- readFile "1.txt"
    let steps = [case head str of
                                'L' -> (L, read (tail str) :: Int)
                                'R' -> (R, read (tail str) :: Int)
                | str <- splitOn ", " input]
    let (_, x, y) = last $ part1 steps
    print $ "Part 1: " ++ show (x + y)
    -- let (dx, dy) = part2 steps
    -- print $ part1 steps
    -- print $  part1 steps
    -- print $ "Part 2: " ++ show (dx + dy)
