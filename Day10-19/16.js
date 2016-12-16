'use strict';

function generate_data(inp, len){
  while(inp.length < len) {
    var mir = inp.split('').reverse().map((x) => {
      return x == '0' ? '1' : '0'
    })
    inp += '0' + mir.join('')
  }
  return inp.slice(0, len);
}

function checksum(cs){
  while(cs.length % 2 == 0) {
    var new_cs = ''
    for(var i = 0; i < cs.length; i += 2) {
      new_cs += cs[i] == cs[i+1] ? '1' : '0'
    }
    cs = new_cs
  }
  return cs
}

console.log(checksum(generate_data('10000', 20)) == '01100')
console.log('Part 1: ' + checksum(generate_data('10111011111001111', 272)))
console.log('Part 1: ' + checksum(generate_data('10111011111001111', 35651584)))
