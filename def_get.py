def get_summ(one, two, delimeter='&'):
	return one.upper() + str.upper(delimeter) + str.upper(two)

one1="learn"
two2="python"
print(get_summ(one1, two2))