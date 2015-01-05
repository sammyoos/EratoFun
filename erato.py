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
<table id="EratoData"><tbody>
""" )


def printDocFooter():
	print( """
</tbody> </table> </body>
</html>
""" )

def processNewPrime( prime, erato, indent, searchDomain, maxColumnCount ):

	# nothing left to display
	if( indent > maxColumnCount ):
		return( False )

	print( '<tr><th>%s</th>' % prime, end='' )
	print( '<td colspan="%d">&nbsp;</td>' % indent, end='' )

	gap = 1
	column_count = indent
	first = int(( prime * prime ) / 2)
	erato[first]=prime

	for index in xrange( first+prime, searchDomain+1, prime ):
		if( erato[index] != 0 ):
			gap += 1
		else:
			if( column_count <= maxColumnCount ):
				column_count += 1
				print( '<td class=c%03d>%s</td>' % ( gap, gap ), end='' )
			erato[index]=prime
			gap = 1

	print( '</tr>' )
	return( True )


def startSieve( maxPrimeCandidate = 3000, maxColumnCount = 100 ):
	maxHalfDomain = maxPrimeCandidate*maxPrimeCandidate / 2

	sieve = [ 0 for i in range( maxHalfDomain + 1 ) ]


	# index will be related to candidate as follows
	# index = (int)(candidate/2)
	# and only odd numbers will be evaluated
	# the number 2 is prime, but will not be considered

	rowIndent = 0
	initialIndex = 0

	printDocHeader()
	for candidate in xrange( 3, maxPrimeCandidate, 2 ):
		initialIndex += 1
		if( sieve[initialIndex] == 0 ):
			rowIndent += 1
			if( not processNewPrime( candidate, sieve, rowIndent, maxHalfDomain, maxColumnCount )):
				break
		print( '' )

	printDocFooter()
                    

startSieve( maxPrimeCandidate = 10000, maxColumnCount = 300 )


# vim: set noexpandtab ts=4 sw=4 foldmethod=marker:
