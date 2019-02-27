function leftRect(f, r, m, a, b, n) {
	var sum = 0;
	var dx = (b-a)/n;
	for (var x = a; n > 0; n--, x += dx)
		sum += f(x, r, m);
	return sum * dx;
}
 
function rightRect(f, r, m, a, b, n){
	var sum = 0;
	var dx = (b-a)/n;
	for (var x = a + dx; n > 0; n--, x += dx)
		sum += f(x, r, m);
	return sum * dx;
}
 
function midRect(f, r, m, a, b, n){
	var sum = 0;
	var dx = (b-a)/n;
	for (var x = a + (dx / 2); n > 0; n--, x += dx)
		sum += f(x, r, m);
	return sum * dx;
}
function trapezium(f, r, m, a, b, n){
	var dx = (b-a)/n;
	var x = a;
	var sum = f(a, r, m);
	for(var i = 1; i < n; i++){
		a += dx;
		sum += f(a, r, m)*2;
	}
	sum += f(b, r, m);
	return 0.5 * dx * sum;
}
function simpson(f, r, m, a, b, n){
	var dx = (b-a)/n;
	var sum1 = f(a + dx/2, r, m);
	var sum2 = 0;
	for(var i = 1; i < n; i++){
		sum1 += f(a + dx*i + dx/2, r, m);
		sum2 += f(a + dx*i, r, m);
	}
	return (dx/6) * (f(a, r, m) + f(b, r, m) + 4*sum1 + 2*sum2);
}

function f1(x, r, m){
	return ( Math.exp(-.5 * Math.pow( (x-m) / r, 2)) / (r * Math.sqrt(Math.PI * 2)) );
}

console.log(leftRect(f1, .2, .4, 3, 4, 70));
console.log(rightRect(f1, .2, .4, 3, 4, 70));
console.log(midRect(f1, .2, .4, 3, 3, 70));
console.log(trapezium(f1, .2, .4, 3, 4 , 70));
console.log(simpson(f1, .2, .4, 3, 4 , 70));