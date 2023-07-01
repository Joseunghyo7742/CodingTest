function solution(num_list, n) {
    let answer = 0;
    if(num_list.includes(n))
        answer=1;
    return answer;
}

//다른사람 풀이
const solution=(l,n)=>+(l.includes(n))