const fs = require('fs').readFileSync(process.platform ==="linux" ? "/dev/stdin": __dirname+"/input.txt" )
const input= fs.toString().trim()
const digit= input.length

let result=0
for (let i =1; i<digit ; i++){
  const count= 9*Math.pow(10,i-1)
  result+= count*i
}

//마지막 자리수 더하기
const s= Math.pow(10,digit-1)
const extra= digit*(Number(input)-s+1)
result+= extra

console.log(result)