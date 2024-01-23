
const month_days= 28
const year_days= month_days*12

//일자로 바꿔주는 함수
const getTotalDays=(date)=>{
    const [year,month,day] = date.split(".").map(Number)
    const result= year*year_days + month* month_days + day
    return result
}
function solution(today, terms, privacies) {
    //terms 객체화
    const terms_table= new Map()
    terms.forEach((element)=> {
        const [type, month]= element.split(' ') //배열구조분해
        terms_table.set(type,Number(month)*month_days) //key-value set
    } )
    
    const answer=privacies.map((info, index)=>{
        const [createdAt,createdType]= info.split(" ")
        const gap= getTotalDays(today)- getTotalDays(createdAt)
        if(gap>= terms_table[createdType])
            return index+1
    })
    
   return answer
}