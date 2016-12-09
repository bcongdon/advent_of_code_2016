import Data.List.Split
import Data.List

import qualified Data.Text as Text



data Direction = R | L deriving Show

turn compass dir = mod (compass + case dir of R -> 1
                                              L -> -1) 4

move prev (dir, n) = case last prev of
                    (compass, x, y) -> case turn compass dir of
                        0 -> [(0, x, y + i) | i <- [1..n]]
                        1 -> [(1, x + i, y) | i <- [1..n]]
                        2 -> [(2, x, y - i) | i <- [1..n]]
                        3 -> [(3, x - i, y) | i <- [1..n]]

part1 steps = 
    foldr (++) [] $ scanl move [(0, 0, 0)] steps

posOf (_, x, y) = (x, y)

part2 res =
    firstDup $ map posOf res

taxiDist x y = abs(x) + abs(y)

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
    let path = part1 steps
    let (_, x, y) = last path
    let p1res = taxiDist x y
    print $ "Part 1: " ++ show p1res
    let (dx, dy) = part2 path
    let p2res = taxiDist dx dy
    print $ "Part 2: " ++ show p2res
