//
//  10.swift
//  
//
//  Created by Benjamin Congdon on 12/12/16.
//
//

import Foundation

struct Edge {
    var lo: Int
    var hi: Int
    var isBotLo: Bool
    var isBotHi: Bool
}

func process_bots(commands: [String]) -> [Int] {
    var bots: [Int:[Int]] = [:]
    for i in (0...500){
        bots[i] = []
    }
    var output: [Int] = [Int](count: 100, repeatedValue: 0)
    var edges: [Int:Edge] = [:]
    for cmd in commands.map({$0.componentsSeparatedByString(" ")}) {
        if(cmd[0] == "value") {
            let idx = Int(cmd.last!)!
            if(bots[idx] != nil) {
                bots[idx]!.append(Int(cmd[1])!)
            }
            else{
                bots[idx] = [Int(cmd[1])!]
            }
        }
        else {
            let lo = Int(cmd[6])!
            let hi = Int(cmd.last!)!
            edges[Int(cmd[1])!] = Edge(lo: lo, hi: hi,
                isBotLo: cmd[5] == "bot", isBotHi: cmd[10] == "bot")
        }
    }
    while(bots.count > 0) {
        var bot = -1
        var inv = [Int]()
        for (k, v) in bots {
            if v.count == 2 {
                bot = k
                inv = v
                break
            }
        }
        if bot < 0 {
            break
        }
        bots[bot] = []
        if inv.contains(61) && inv.contains(17) {
            print("Part 1: " + String(bot))
        }
        let e = edges[bot]!
        if e.isBotLo {
            bots[e.lo]!.append(inv.minElement()!)
        }
        else{
            output[e.lo] = inv.minElement()!
        }
        if e.isBotHi {
            bots[e.hi]!.append(inv.maxElement()!)
        }
        else {
            output[e.hi] = inv.maxElement()!
        }
    }
    return output
}

let text: String
do {
    text = try String(contentsOfFile: "10.txt")    
}
catch {
    text = ""
}

let o = process_bots(text.componentsSeparatedByString("\n"))
print("Part 2: " + String(o[0] * o[1] * o[2]))