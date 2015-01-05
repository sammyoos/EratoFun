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
			td.breakPat { background: DarkKhaki; }
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

def processNewPrime( prime, erato, prev, indent ):
	global maxColumnCount
	global maxHalfDomain

	# nothing left to display
	if( indent > maxColumnCount ):
		return( None )

	print( '<tr><th>%s</th>' % prime, end='' )
	print( '<td colspan="%d">&nbsp;</td>' % indent, end='' )

	gap = 1
	column_count = indent
	first = int(( prime * prime ) / 2)
	erato[first]=prime

	curr = []
	prevIdx = 1
	patternBroken = True if( prev is None ) else False

	for index in xrange( first+prime, maxHalfDomain+1, prime ):
		if( erato[index] != 0 ):
			gap += 1
		else:
			if( column_count <= maxColumnCount ):
				column_count += 1
				curr.append( gap )

				if( not patternBroken and gap != prev[prevIdx] ):
					patternBroken = True
				else:
					prevIdx += 1

				if( patternBroken ):
					print( '<td class=breakPat>%s</td>' % gap, end='' )
				else:
					print( '<td>%s</td>' % gap, end='' )

			erato[index]=prime
			gap = 1

	print( '</tr>' )
	#print( '!--', curr, '--!' )
	return( curr )


# index will be related to candidate as follows
# index = (int)(candidate/2)
# and only odd numbers will be evaluated
# the number 2 is prime, but will not be considered
def startSieve():
	global maxPrimeCandidate
	global maxHalfDomain

	sieve = [ 0 for i in range( maxHalfDomain + 1 ) ]
	prev = None
	rowIndent = 0
	initialIndex = 0
	printDocHeader()

	for candidate in xrange( 3, maxPrimeCandidate, 2 ):
		initialIndex += 1
		if( sieve[initialIndex] == 0 ):
			rowIndent += 1
			prev = processNewPrime( candidate, sieve, prev, rowIndent )
			if( prev is None ):
				break
		print( '' )

	printDocFooter()
                    

maxPrimeCandidate = 10000
maxColumnCount = 500
maxHalfDomain = maxPrimeCandidate*maxPrimeCandidate / 2

startSieve()
# vim: set noexpandtab ts=4 sw=4 foldmethod=marker:
