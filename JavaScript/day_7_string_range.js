const read=require('readline').createInterface({
    input:process.stdin,
    output:process.stdout
});
(function(){
    read.question("Enter the Number : ",number=>{
        let arr=[]
        number=parseInt(number);
        for(let i=0;i<number;i++){
            arr.push(i);
        }
        console.log(arr.join("."));
    })
})();