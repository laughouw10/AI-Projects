"""
File: validEmailAddress.py
Name: 
----------------------------
This file shows what a feature vector is
and what a weight vector is for valid email 
address classifier. You will use a given 
weight vector to classify what is the percentage
of correct classification.

Accuracy of this model: TODO:
"""

WEIGHT = [                           # The weight vector selected by Jerry
	[0.4],                           # (see assignment handout for more details)
	[0.4],
	[0.2],
	[0.2],
	[0.9],
	[-0.65],
	[0.1],
	[0.1],
	[0.1],
	[-0.7]
]

DATA_FILE = 'is_valid_email.txt'     # This is the file name to be processed


def main():
	maybe_email_list = read_in_data()
    accuracy = 0
	for maybe_email in maybe_email_list:
		feature_vector = feature_extractor(maybe_email)
        ans = 0
		for i in range(len(WEIGHT)):
            ans += feature_vector[i] * WEIGHT[i]
        if ans > 0 and i > 12:
            accuracy += 1
        return accuracy / 26

def feature_extractor(maybe_email):
	"""
	:param maybe_email: str, the string to be processed
	:return: list, feature vector with value 0's and 1's
	"""
	feature_vector = [0] * len(WEIGHT)
	for i in range(len(feature_vector)):
		if i == 0:
			feature_vector[i] = 1 if '@' in maybe_email else 0
		elif i == 1:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' not in maybe_email.split('@')[0] else 0
		elif i == 2:
            if feature_vector[0]:
                feature_vector[i] =1 if maybe_email[0] != "@" else 0
        elif i == 3:
            if feature_vector[0]:
                feature_vector[i] =1 if maybe_email[-1] == "@" else 0
        elif i == 4:
			if feature_vector[0]:
				feature_vector[i] = 1 if '.' in maybe_email.split('@')[1] else 0
        elif i == 5:
			feature_vector[i] = 1 if ' ' not in maybe_email else 0
        elif i == 6:
			feature_vector[i] = 1 if '.com' in maybe_email else 0   
        elif i == 7:
			feature_vector[i] = 1 if '.edu' in maybe_email else 0  
        elif i == 8:
			feature_vector[i] = 1 if '.tw' in maybe_email else 0  
        elif i == 9:
			feature_vector[i] = 1 if len(maybe_email) > 10 else 0  
            
	return feature_vector


def read_in_data():
	"""
	:return: list, containing strings that may be valid email addresses
	"""
	# TODO:
    list = []
	with open(DATA_FILE, 'r') as f:
        for line in f:
            list.append(line)
        return list


if __name__ == '__main__':
	main()
