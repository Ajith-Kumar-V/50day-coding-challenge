const reader=require('readline').createInterface({
    input:process.stdin,
    output:process.stdout
});
let quest=()=>reader.question("Enter the Mail ID : ",mail=>{
    let arraya=mail.split("@");
    console.log(arraya[0])
})
quest()