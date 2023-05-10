const reader = require("readline").createInterface({
  input: process.stdin,
  output: process.stdout,
});
reader.question("Enter the number : ", num => {
    let hig = 0;
    for (let i in num) {
        val=num[i]
        val=parseInt(val)
        if (val % 2 != 0) {
            hig = Math.max(hig, val);
        }
    }
    console.log(hig);
});
