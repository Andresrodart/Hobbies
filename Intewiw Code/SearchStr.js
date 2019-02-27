var strCurrencies = function (str, strings) {
    let ocurrencies;
    strings.forEach(element => {
        if(element.search(str)) ocurrencies++;
    });
    return ocurrencies;
}
