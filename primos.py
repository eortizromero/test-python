# -*- encoding: utf-8 -*-
# code by: Edgar Ortiz, https://github.com/eortizromero/

# Run script with:
# python primos.py
description = "Press Ctrl + C to exit."

def es_primo(num):
	n = sum([int(i) for i in str(num)])	
	if num < 2:
		return "%r No es primo ... %s" % (num, description)
	for i in range(2, num):
		if num % i == 0 and n % i == 0:
			return ""
		else:
			return "sum(%r) = %r Es primo... %s" % (num, n, description)
n = 0
while True:
	print es_primo(n)
	n += 1

