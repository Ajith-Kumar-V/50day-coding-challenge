function register_check(objectt){
    let count=0;
    for(let xn in objectt){
        if((objectt[xn]=="yes")||(objectt[xn]=="Yes")){
            count+=1;
        }
    }
    return count;
}
let para={'Michael':'Yes','John':'yes','Peter':'no','Mary':"yes"};
let output=register_check(para);
console.log(output);