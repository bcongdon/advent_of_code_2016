//
//  11.swift
//
//
//  Created by Benjamin Congdon on 12/11/16.
//
//

//import Foundation

let part1_chips = [2, 1, 2, 1, 1]
let part1_gens = [1, 1, 1, 1, 1]
let part2_chips = part1_chips + [1, 1]
let part2_gens = part1_gens + [1, 1]

struct State {
    var chips: [Int]
    var gens: [Int]
    var elevator: Int
    var steps: Int
}

func is_valid(state: State) -> Bool {
    if(!((1 ... 4) ~= state.elevator)) {
        return false
    }
    for (idx, f) in state.chips.enumerate() {
        if f != state.gens[idx] && state.gens.contains(f){
            return false
        }
    }
    return true;
}

func solved(state: State) -> Bool {
    for c in state.chips + state.gens {
        if c != 4 {
            return false
        }
    }
    return true
}
func floor_count(arr: [Int]) -> [Int] {
    return (1...4).map({
        (floor: Int) -> Int in
        return arr.reduce(0) {prev, i in prev + (i == floor ? 1 : 0)}
    })
}

func generalize(state: State) -> String {
    //    return String(state.chips + state.gens) + String(state.elevator)
    return String(floor_count(state.chips) + floor_count(state.gens)) + String(state.elevator)
}

func bfs(start: State) -> Int {
    var bfs_q = [start]
    var seen = Set<String>()
    while bfs_q.count > 0 {
        let state = bfs_q.removeAtIndex(0)
        if (seen.contains(generalize(state)) || !is_valid(state)){
            continue
        }
        else if solved(state) {
            return state.steps
        }
        else {
            seen.insert(generalize(state))
        }
        //        print(bfs_q.count)
        var combined = state.chips + state.gens
        for i in (0..<combined.count) {
            if combined[i] != state.elevator {
                continue
            }
            combined[i] -= 1
            bfs_q.append(State(chips: Array(combined[0..<state.chips.count]),
                gens: Array(combined[state.chips.count..<combined.count]),
                elevator: state.elevator - 1, steps: state.steps + 1))
            combined[i] += 2
            
            bfs_q.append(State(chips: Array(combined[0..<state.chips.count]),
                gens: Array(combined[state.chips.count..<combined.count]),
                elevator: state.elevator + 1, steps: state.steps + 1))
            combined[i] -= 1
            for j in ((i + 1) ..< combined.count) {
                if combined[j] != state.elevator {
                    continue
                }
                combined[i] -= 1
                combined[j] -= 1
                bfs_q.append(State(chips: Array(combined[0..<state.chips.count]),
                    gens: Array(combined[state.chips.count..<combined.count]),
                    elevator: state.elevator - 1, steps: state.steps + 1))
                combined[i] += 2
                combined[j] += 2
                bfs_q.append(State(chips: Array(combined[0..<state.chips.count]),
                    gens: Array(combined[state.chips.count..<combined.count]),
                    elevator: state.elevator + 1, steps: state.steps + 1))
                combined[i] -= 1
                combined[j] -= 1
            }
            
        }
    }
    return -1
}

let state1 = State(chips: part1_chips, gens: part1_gens, elevator: 1, steps: 0)
let state2 = State(chips: part2_chips, gens: part2_gens, elevator: 1, steps: 0)

print("Part 1: \(bfs(state1))")
print("Part 2: \(bfs(state2))")