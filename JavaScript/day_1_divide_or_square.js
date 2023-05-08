const reader=require('readline').createInterface({
    input:process.stdin,
    output:process.stdout
});
reader.question("Enter the number : ",number=>{
    number=parseFloat(number);
    if(number%5==0){
        number=Math.pow(number,0.5);
        number=number.toFixed(2);
        console.log(number);
    }
    else{
        number=number%5;
        console.log(number);
    }
});