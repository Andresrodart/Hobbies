"""
	input: List of equations of sums
		[
			[a, s, 3, w], 	# a = s + 3 + w
			[b, s], 		# b = s
			[s, 3],			# s = 3
			[w = 6 + 8]		# w = 6 + 8
			[y = w + b + s]	# y = w + b + s
		]
	output: a dictionary of values of variables
		{
			a: 20,
			b: 3,
			w: 14,
			y: 20
		}
"""
class equ:
	def __init__(self, equ:[str]):
		self.equ = equ
		self.vars = set()
		for i in range(1, len(equ)): 
			if not equ[i].isdigit(): self.vars.add(equ[i])
	def __lt__(self, other):
		return len(self.vars) < len(other.vars)
	def __str__(self):
		return str("{} : {}".format(self.equ, self.vars))
	def __repr__(self):
		return str("{} : {}".format(self.equ, self.vars))

def resolveEquations(equations: 'List[List[srt]]') -> 'Dict':
	dic_by_vars = {}
	max_num_of_vars = 0
	for equation in equations:
		equation = equ(equation)
		key = len(equation.vars)
		dic_by_vars[key] = dic_by_vars.get(key, []).append(equation)
		max_num_of_vars = max(max_num_of_vars, key)
	for equation in dic_by_vars[0]