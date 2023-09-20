function solution(code) {
    var answer = '';
    var ret = '';
    var mode = 0;
    var idx = 0;
    for(let i = 0; i<code.length; i++){
        if(mode == 0){
            if(code[i]!="1"){
                if(i % 2 == 0){
                    ret = ret + code[i]
                    continue
                }
            }
            else if (code[i] == 1){
                mode = 1
                continue
            }
        }
        else if (mode == 1){
            if(code[i] != 1){
                if(i % 2 != 0){
                    ret = ret + code[i]
                    continue
                }
            }
            else if(code[i] ==1) {
                mode = 0
                continue
            }
        }
    }
    if(ret===''){
        answer = "EMPTY"
    }else{
        answer = ret
    }

    return answer;
}