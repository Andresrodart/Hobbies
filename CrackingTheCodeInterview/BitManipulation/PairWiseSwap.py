def pairWiseSwap(n: 'int') -> 'int':
	mask_even = 2863311530 	#10101010101010101010101010101010
	mask_odd = 1431655765 	#01010101010101010101010101010101
	return ((n & mask_even) >> 1) | ((n & mask_odd) << 1)