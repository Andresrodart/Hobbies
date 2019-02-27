function minimumNumber(n, password) {
    let result = 4;
    if (password.search(/[abcdefghijklmnopqrstuvwxyz]/) != -1) result--;
    if (password.search(/[ABCDEFGHIJKLMNOPQRSTUVWXYZ]/) != -1) result--;
    if (password.search(/[0123456789]/) != -1) result--;
    if (password.search(/[!@#$%^&*()+-]/) != -1) result--;                  //NOTE the '-' symbol has to be the last one to avoid problems of interpretation
    if (n < 6) return (n > 3 && result >= (6 -n))? result : (6 - n);
    return result;
}


console.log(minimumNumber(7, "AUzs-nV"));