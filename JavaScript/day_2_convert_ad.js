function convert_add(arr){
    let s=0;
    for(let i in arr){
        i=parseInt(arr[i]);
        s=s+i;
    }
    return s;
}
let x=convert_add(["1","2","3","5"]);
console.log(x);