// Write a function in JavaScript called `humanSize` that takes a non-negative number of `bytes` and returns a string with the equivalent number of 'B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', or 'YB', between [0, 1000), with at most 1 digit of precision after the decimal. If the number of `bytes` is >= 1000 YB, return this number in YB, for example 5120 YB. For example, your function might return '107.3MB' or 20.6 kb

// Write this function **without** writing a separate case for each byte prefix, and **without** using `Math.log` or `Math.pow`.

/*
  x -> 
  x // 1000 -> 0 <= y < 1000 

  57 / 1000 -> 0.057 0





*/
// function auxHumanSize(computerSpace: number, iteration: number, postString: Array<string>): string{
//   if(iteration === 8 || computerSpace < 1000){
//     return computerSpace.toFixed(1) + postString[iteration]
//   }
//   return auxHumanSize(computerSpace / 1000, iteration + 1, postString);
// }

function humanSize(bytes: number): string{
  const suffixes = ['B', 'kB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB','YB'];
  for (const suffix of suffixes) {
    if(bytes < 1000){
      return bytes.toFixed(1) + suffix;
    }else{
      bytes /= 1000;
    }
  }

  return (bytes * 1000).toFixed(1) + suffixes[suffixes.length - 1];
}

console.log(humanSize(568330324324324324233432423432000000000000))