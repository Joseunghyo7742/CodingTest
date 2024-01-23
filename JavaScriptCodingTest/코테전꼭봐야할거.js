//배열 순회 배열.forEach
a=[1,3,45,2,10]
a.forEach((e,i)=> {
  console.log(e,i)
})
//배열 순회 for of
for (let A of a) {
  console.log(A)
}

//String.split => array
const str="Hello world";
const ret=str.split(" ");
str.split("")
console.log("ret",ret)

//배열을 문자열로 만들기 또는 합치기 Array.join ('seperator')
//arr.length가 0이면 빈 문자열 반환
const b = ret.join(' something ')
console.log(b)

//Array.find() : 배열에서 콜백함수를 만족하는 첫 번째 '요소'를 반환, 없으면 undefined
const test= [1,2,3,4]
const find= test.find((a,i)=> a>i)
console.log("find",find)

//Array.findIndex: 배열에서 판별함수를 만족하는 첫 번째 요소의 '인덱스' 없으면 -1 반환
const test1=[ 5,4,12]
const callbackFn= (e)=> e>6
console.log(test1.findIndex(callbackFn))

//Array.indexOf(searchElement, fromIndex): 배열에 주어진 요소를 찾을 수 있는 첫 번째 인덱스 반환, 없으면 -1 반환.
const test2= ['ant','bison','camel','bison','aa']
console.log(test2.indexOf('ant'))
console.log("test2",test2.indexOf('bison',3)) //3번인덱스부터 셈.
const test3= "helloworld"
console.log("test3", test3.indexOf("o"))
  //* fromIndex
    // 검색을 시작할 인덱스. 음수 인덱스는 끝부터 거꾸로 센다. 
  //findIndex와의 차이. 
    //inexOf() 배열, 문자열에서 일치하는 요소를 찾을 때, 찾고 싶은 값을 바로 넣는다. 
    //findIndex는 배열에서 찾을 때. 함수를 넣는다.

//Array.includes(searchE,fromIndex): 배열의 항목에 특정 값이 포함되었는지 true or false
const test4= [1,2,3]
console.log(test4.includes())

//String.substring(indexStart[,indexEnd])
const str2= "Mozilla"
console.log(str2.substring(0,4))
console.log(str2.substring(3))

//String.slice(beginIndex[,endIndex]): 문자열의 일부 추출 ->새문자열 반환
const str3="The quick brown fox"
console.log(str3.slice(10))
console.log(str3.slice(-3))
console.log(str3.slice(0,4))

  //* substring과 slice 차이 
    //- substring은 startIndex가 endIndex보다 크면 자동으로 자리 바꿈. slice는 빈문자열

//Object.keys : 주어진 객체의 속성 이름들을 배열로 반환
const obj1 ={
  a:"sth",
  b: 42,
  c: false
}
console.log(Object.keys(obj1)) // Array["a","b","c"]

//Object.values: 주어진 객체의 속성 값을 배열로 반환
console.log(Object.values(obj1))

//Object.entries: 주어진 객체의 속성 키& 값 배열로 반환
console.log(Object.entries(obj1)) //Array[["a",'sth'],['b',42]..] 


//Object.fromEntries() : 키값 쌍의 목록을 객체로 바꿈
const entries= Object.entries(obj1)
const obj2= Object.fromEntries(entries)
console.log(obj2)

//Math.round: 입력값을 반올림한 수와 가장 가까운 정수 값 반환
console.log(Math.round(0.9))
console.log(Math.round(-5.5)) 

//Math.ceil:  주어진 수보다 >= 중 가장 작은 정수
console.log(Math.ceil(5.4)) //6

//Math.floor: 주어진 수보다 <= 중 가장 큰 정수
console.log(Math.floor(5.05)) //5

//Math.abs

//정렬 sort(정렬 기준 콜백함수)
  //* a>b  양수, a<b 음수 
let numbers=[100,3,1,2,9,2] //

console.log("정렬실수",numbers.sort()) // 정렬하기 전에 배열 내의 값을 내부적으로 문자열로 변환
//문자열 대소비교에서는 첫 번째 글자가 크면 뒤가 아무리 더 큰 글자가 있어도 결과 영향 x

numbers= numbers.sort((a,b)=> a-b) //오름차순 정렬
console.log(numbers)
numbers = numbers.sort((a,b)=> (a-b)*-1) //내림차순 정렬
console.log(numbers)


//Array.filter(callbackFn) :콜백함수 통과요소로 구성된 배열, 없으면 빈배열
  //얕은 복사: 원본 객체와 같은 참조를 고유하는 복사, 복사본 변경시 원본도 변경될 수 있다. 
const test6 = numbers.filter( e=> e%2 ==0) 
console.log(test6, numbers)


//Array.reduce(callback[,intialValue])
  //callback( 누적반환값, 처리할 현재요소, 처리할현재인덱스, 호출한 배열)
const test7= [1,2,3,4,5]
const res= test7.reduce((total,e)=> total+e, 100)
console.log(res)

//Date
const date= new Date(1999,2,4) //월은 0부터 시작
console.log(date)
const dateTest= new Date('2022.01.05')
console.log(dateTest)

const date2= "1999.02.03"
const arrrr= date2.split(".").map(Number) 
console.log(arrrr)


