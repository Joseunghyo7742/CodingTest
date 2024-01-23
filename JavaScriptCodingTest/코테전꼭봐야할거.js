//배열 순회 배열.forEach
a=[1,3,45,2,10]
a.forEach((e,i)=> {
  console.log(e,i)
})

//공백 기반 split
const str="Hello world";
const ret=str.split(" ");
str.split("")
console.log("ret",ret)

//배열을 문자열로 만들기 또는 합치기 Array.join ('seperator')
//arr.length가 0이면 빈 문자열 반환
const b = ret.join(' something ')
console.log(b)

//find

//findIndex

//includes

//substring

//slice

//Object.keys

//Object.values

//Object.entries

//Math.round

//Math.ceil

//Math.floor

//Math.abs

//정렬 sort
let numbers=[3,1,2,9,2]
numbers= numbers.sort((a,b)=> a-b) //오름차순 정렬
console.log(numbers)
numbers = numbers.sort((a,b)=> (a-b)*-1) //내림차순 정렬
console.log(numbers)
