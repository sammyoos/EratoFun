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

def cssFader( steps, c1, c2 ):
	outputFormat = 'td.c%03d { background: #%02x%02x%02x; color: #%02x%02x%02x; }'
	inc = map( lambda i:float(c2[i]-c1[i])/float( steps-1 ), range(0,3))

	for i in range(0,steps-1):
		inc1 = c1[0] + int(float(i)*inc[0])
		inc2 = c1[1] + int(float(i)*inc[1])
		inc3 = c1[2] + int(float(i)*inc[2])
		print( outputFormat % ( i, 
				inc1, inc2, inc3,
				(inc1+0x80)%0x100,
				(inc2+0x80)%0x100,
				(inc3+0x80)%0x100 ))
		i += 1
	return( i )



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
""" )

	cssFader( 10, [ 0x00, 0x00, 0x00 ], [ 0xFF, 0xFF, 0xFF ] )

	print( """
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

def printRow( row, broken ):
	if( row is None ):
		return

	indent = row.pop()
	prime  = row.pop()

	print( '<tr><th>%s</th>' % prime, end='' )
	print( '<td colspan="%d">&nbsp;</td>' % indent, end='' )

	for i in row:
		if broken < 0:
			print( '<td class=breakPat>%s</td>' % i, end='' )
		else:
			print( '<td class=c%03i>%s</td>' % (i,i), end='' )
			broken -= 1

	print( '</tr>' )


def processNewPrime( prime, erato, prev, indent ):
	global maxColumnCount
	global maxHalfDomain

	if( indent > maxColumnCount ):
		print( '<!-- indent is larger than maxColumnCount (%i > %i)'%(indent, maxColumnCount))
		return( None )

	gap = 1
	column_count = indent + 1
	first = int(( prime * prime ) / 2)
	erato[first]=prime

	# the last element will be the prime number being evaluated
	# this is just to make it easier to pass back and forth
	# between functions
	curr = [ ]
	prevIdx = 1
	broken = False

	for index in xrange( first+prime, maxHalfDomain+1, prime ):
		if( erato[index] != 0 ):
			gap += 1
		else:
			if( column_count <= maxColumnCount ):
				column_count += 1
				curr.append( gap )

				if( not broken and prev is not None and gap == prev[prevIdx] ):
					prevIdx += 1
				else:
					broken = True

			erato[index]=prime
			gap = 1

	curr.append( prime  )
	curr.append( indent )
	printRow( prev, prevIdx-1 )
	return( curr )


# index will be related to candidate as follows
# index = (int)(candidate/2)
# and only odd numbers will be evaluated
# the number 2 is prime, but will not be considered
def startSieve():
	global maxPrimeCandidate
	global maxHalfDomain

	sieve = [ 0 for i in range( maxHalfDomain + 1 ) ]
	gapList = None
	rowIndent = 0
	initialIndex = 0
	printDocHeader()

	for candidate in xrange( 3, maxPrimeCandidate, 2 ):
		initialIndex += 1
		if( sieve[initialIndex] == 0 ):
			rowIndent += 1
			gapList = processNewPrime( candidate, sieve, gapList, rowIndent )
			if( gapList is None ):
				break
		print( '' )

	printRow( gapList, maxHalfDomain )
	printDocFooter()
                    

maxPrimeCandidate = 10000
maxColumnCount = 300
maxHalfDomain = maxPrimeCandidate*maxPrimeCandidate / 2

startSieve()
# vim: set noexpandtab ts=4 sw=4 foldmethod=marker:
