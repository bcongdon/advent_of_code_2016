valid_tri :: (Integral a) => [a] -> Bool
valid_tri x = m < (s - m)
    where m = maximum x
          s = sum x

count :: [Bool] -> Int
count = length . filter (True==)

line_to_int :: [Char] -> [Int]
line_to_int l = [read i | i <- (words l)]

main = do 
    input <- readFile "3.txt"
    let tris = map line_to_int $ lines input
    let num_valid = count $ map valid_tri tris
    putStrLn $ "Part 1: " ++ show num_valid
    return 0