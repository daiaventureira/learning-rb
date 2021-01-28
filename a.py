def r(n):
	if n == 1:
		return ['()']
	
	xs = r(n - 1)
	rs = []

	for x in xs:
		rs.append(x + '()')
		rs.append('()' + x)
		rs.append('(' + x + ')')

	return sorted(list(set(rs)))

for i in range(5):
	x = r(i + 1)
	print(len(x), x)


