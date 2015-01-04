#!/usr/bin/python
"""
erato.py

Create table to investigate output from Sieve of Eratosthenes
See README.md for more information

to execute:
> python erato.py > index.html

to document:
> pydoc -w ./erato.py
"""

from __future__ import print_function
import pprint
pp = pprint.PrettyPrinter(indent=4)


def printDocHeader():
	print( """
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">

		<title>EratoFun Data Table</title>

		<style>
			body { font-family: sans-serif; }
			table { border-collapse: collapse; }
			td { border-right-style: solid; border-left-style: solid; padding: 2px; }
			td.breakPat { background: LightGrey; }
		</style>

	</head>

<body>

<h1>Sieve of Eratosthenes</h1>

<table id="EratoData">
	<tbody>
""" )


def printDocFooter():
	print( """
</tbody> </table> </body>
</html>
""" )



def startSieve( maxPrimeCandidate = 3000, maxColumnCount = 100 ):
	max_domain = maxPrimeCandidate*maxPrimeCandidate
	max_half_domain = max_domain / 2

	erato = [ 0 for i in range( max_half_domain + 1 ) ]


	# index will be related to candidate as follows
	# index = (int)(candidate/2)
	# and only odd numbers will be evaluated
	# the number 2 is prime, but will not be considered

	#column_count = 0
	indent = 0
	initial_index = 0
	candidate = 3


	printDocHeader()
	while( candidate < maxPrimeCandidate ):
		initial_index = initial_index + 1
		if( erato[initial_index] == 0 ):
			print( '<tr><th>%s</th>' % candidate, end='' )

			column_count = indent
			indent = indent + 1
			print( '<td colspan="%d">&nbsp;</td>' % indent, end='' )

			increment = 1
			index = ( candidate * candidate ) / 2
			erato[index]=candidate
			index = index + candidate

			while( index <= max_half_domain ):
				if( erato[index] != 0 ):
					increment = increment + 1
				else:
					if( column_count <= maxColumnCount ):
						column_count = column_count + 1
						print( '<td class=c%03d>%s</td>' % ( increment, increment ), end='' )
					erato[index]=candidate
					increment = 1

				index = index + candidate
			print( '</tr>' )
			#pp.pprint( erato )
		candidate = candidate + 2
		print( '' )

	printDocFooter()
                    

startSieve( maxPrimeCandidate = 3000, maxColumnCount = 100 )


# vim: set noexpandtab ts=4 sw=4 foldmethod=marker:
