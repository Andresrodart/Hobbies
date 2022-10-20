/*

Say you already have `sleep`, a function you can await to halt execution for some number of `ms` before resuming.
​
Using `sleep`, write a wrapper around `fetch` called `refetch` that lets a user pass in the usual fetch arguments, plus a number of `retries` and an initial retry `delay` in ms.
​
`refetch` calls fetch, and if fetch doesn't throw an exception, it returns the response. If fetch throws an exception, refetch waits for `delay` ms and retries the request. If fetch throws another exception, it waits for twice as long as before, then retries the request. It keeps doing this until fetch doesn't throw an exception, in which case it returns the response, or until it runs out of retries, in which case it returns `undefined`.
​
The signature of `fetch` is `(url: string, options: {}): Promise<Response>`. You can choose any function signature for `refetch`, but the closer it is to `fetch`'s signature the better.


*/

async function refetch(url: string, options: {}, retries: number, delay: number): Promise<Response| undefined> {
  try {
    const res = await fetch(url, options);
    console.log(res)
    return res;
  } catch (error) {
    if(retries > 0){
      console.log(`missing retries ${retries}, delay: ${delay}`)
      await sleep(delay);
      return refetch(url, options, retries -1, delay * 2);
    }else{
      return undefined;
    }
  }
}

function sleep(ms: number) {
  return new Promise(resolve => setTimeout(resolve, ms))
}

async function test () {
  const res = await refetch('http://www.google.com', {}, 3, 1000)
  console.log(res)
}

test()