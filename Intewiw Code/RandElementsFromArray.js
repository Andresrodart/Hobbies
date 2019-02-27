//Given N (an array of elements, send k eleement)
var kRandElem = function(array,k){
    if (array.length === 0 || k === 0)
        return new Array();
    if(array.length <= k)
        return array;
    let kElements = [];
    let pElements = array.length; 
    
    for (let i = 0; i < k; i++) {
        let index = Math.trunc(Math.random() * pElements--);
        kElements.push(array[index]);
        array[index] = array[array.length - 1];
        array[array.length - 1] = kElements[i];
    }
    return kElements;
} 


var myArray = [0, 1, 2, 3, 4];
console.log(kRandElem(myArray, 3));
