#!/usr/bin/python
import pprint
pp = pprint.PrettyPrinter(indent=4)

max_candidate = 100
max_domain = max_candidate*max_candidate
max_half_domain = max_domain / 2

erato = [ 0 for i in range( max_half_domain + 1 ) ]


# index will be related to candidate as follows
# index = (int)(candidate/2)
# and only odd numbers will be evaluated
# the number 2 is prime, but will not be considered

initial_index = 0
candidate = 3

print """
<html>
<body>
<table>
"""

while( candidate < max_candidate ):
	initial_index = initial_index + 1
	if( erato[initial_index] != 0 ):
		print '<!-- skipping non-prime ', candidate, ' continuing... -->'
	else:
		print '<tr><th>', candidate, '</th>'

		increment = 1
		index = ( candidate * candidate ) / 2
		#print '<td> ', candidate, ' => ', index*2+1, '</td>'
		erato[index]=candidate
		index = index + candidate

		while( index <= max_half_domain ):
			if( erato[index] != 0 ):
				increment = increment + 1
			else:
				#print '<td> ', candidate, ' => ', index*2+1, '</td>'
				print '<td>', increment, '</td>'
				erato[index]=candidate
				increment = 1

			index = index + candidate
		print '</tr>'
		#pp.pprint( erato )
	candidate = candidate + 2

                    
print """
</table>
</body>
</html>
"""




# vim: set noexpandtab ts=4 sw=4 foldmethod=marker:
