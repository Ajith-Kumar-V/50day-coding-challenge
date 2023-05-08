function only_floats(a, b){
    if (((a%1)!=0)&&((b%1)!=0)){
        return 2;
    }
    if (((a%1)!=0)||((b%1)!=0)){
        return 1;
    }
    //if ((b%1)!=0){
      //  return 1;
    //}
    else{
        return 0;
    }
}
let a=12 ;
let b=23;
let output=only_floats(a,b);
console.log(output);