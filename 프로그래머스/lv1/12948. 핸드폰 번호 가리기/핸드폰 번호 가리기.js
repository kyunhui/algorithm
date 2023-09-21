function solution(phone_number) {
    var answer = '';
    for(let i = 0; i < phone_number.length-4; i++){
        answer += "*"
    }
    var temp = phone_number.substr(phone_number.length-4, phone_number.length)
    answer += temp
    return answer;
}