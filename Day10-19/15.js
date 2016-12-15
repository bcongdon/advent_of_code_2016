'use strict'
var fs = require('fs')

function parse_input(inp) {
  var setup = []
  for(var i = 0; i < inp.length; i++){
    var arr = inp[i].split(' ')
    if(arr.length < 10) continue;
    setup.push({lim: parseInt(arr[3]), pos: parseInt(arr[11])})
  }
  return setup
}

function check_solution(setup, time) {
  for(var i = 0; i < setup.length; i++){
    if((setup[i].pos + time + i + 1) % setup[i].lim != 0) {
      return false;
    }
  }
  return true;
}

function first_drop_time(setup){
  var i = 0;
  while(1){
    if(check_solution(setup, i)){
      return i;
    }
    i++
  }
}

fs.readFile('15.txt', {encoding: 'utf-8'}, (err, data) => {
  if(!err){
    var setup = parse_input(data.split('\n'))
    console.log("Part 1: " + first_drop_time(setup))
    setup.push({lim: 11, pos: 0})
    console.log("Part 2: " + first_drop_time(setup))
  }
})