#!/usr/bin/python

from __future__ import print_function
import pprint
pp = pprint.PrettyPrinter(indent=4)

max_candidate = 10000
max_domain = max_candidate*max_candidate
max_half_domain = max_domain / 2

erato = [ 0 for i in range( max_half_domain + 1 ) ]


# index will be related to candidate as follows
# index = (int)(candidate/2)
# and only odd numbers will be evaluated
# the number 2 is prime, but will not be considered

max_col_count = 500
column_count = 0
indent = 0
initial_index = 0
candidate = 3

print( """
<!DOCTYPE html>
<html>
	<head>
		<meta http-equiv="Content-type" content="text/html; charset=utf-8">
		<meta name="viewport" content="width=device-width, initial-scale=1">

		<title>EratoFun Data Table</title>


		<!-- Latest compiled and minified CSS -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css">

		<!-- Optional theme -->
		<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap-theme.min.css">

		<!-- Latest compiled and minified JavaScript -->
		<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>

		<script type="text/javascript">
			<!--
			$(document).ready(function()
			{
				$('#EratoData').columnHover({eachCell:true, hoverClass:'betterhover', includeSpans:true });
			});
			-->
		</script>		

		<link rel="stylesheet" type="text/css" href="style.css" />
		<link rel="stylesheet" type="text/css" href="fader.css" />
	</head>

<body>

<h1>Sieve of Eratosthenes</h1>

<table id="EratoData">
	<tbody>
""" )

candNum = 0
while( candidate < max_candidate ):
	initial_index = initial_index + 1
	if( erato[initial_index] != 0 ):
		print( '<!-- skipping non-prime %s continuing... -->' % candidate )
	else:
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
				if( column_count <= max_col_count ):
					column_count = column_count + 1
					print( '<td class=c%03d>%s</td>' % ( increment, increment ), end='' )
				erato[index]=candidate
				increment = 1

			index = index + candidate
		print( '</tr>' )
		#pp.pprint( erato )
	candidate = candidate + 2
	print( '' )

                    
print( """
</tbody> </table> </body>
</html>
""" )




# vim: set noexpandtab ts=4 sw=4 foldmethod=marker:
