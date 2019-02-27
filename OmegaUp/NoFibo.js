const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});


function noFibo(){
    let fibo = 3, a = 1, b = 2, val= 0, ans = '';
    
    rl.on('line', (input) => {
        val = input;
        for(let i = 3;i < val; i++){
            if (i == fibo){
                a = b;
                b = fibo;
                fibo = a + b;
            }else
                ans += i + ' ';
                
        }
        console.log( ans );
        rl.close();
    });
}

noFibo();