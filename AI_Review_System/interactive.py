"""
File: interactive.py
Name: 
------------------------
This file uses the function interactivePrompt
from util.py to predict the reviews input by 
users through Console. Remember to read the weights
and build a Dict[str: float]
"""
from util import interactivePrompt
from submission import extractWordFeatures

def main():
	weights = {}
	with open("weights", "r") as f:
		for line in f:
			lst = line.split()
			weights[lst[0]] = float(lst[1])
	featureExtractor = extractWordFeatures
	interactivePrompt(featureExtractor, weights)



	# ans = 0
	# x = input("your input: ")
	# lst = x.split()
	# d1={}
	# for word in lst:
	# 	if word in d1:
	# 		d1[word] += 1
	# 	else:
	# 		d1[word] = 1
	# d2={}
	# with open("weights", "r") as f:
	# 	for line in f:
	# 		lst = line.split()
	# 		if lst[0] in d1:
	# 			d2[lst[0]] = float(lst[1])
	# for key in d1:
	# 	ans += d2[key] * d1[key]
	# if ans > 0:
	# 	print("Prediction: 1")
	# else:
	# 	print("Prediction: 0")



if __name__ == '__main__':
	main()