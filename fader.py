#!/usr/bin/python
# to run: python fader.py > 
# then: firefox fader.html

primeNum = 0
numSteps = 3

outputFormat = 'td.c%03d { background: #%02x%02x%02x; color: #%02x%02x%02x; }'

color1 = [ 0xFF, 0xFF, 0xFF ]
color2 = [ 0xFF, 0x20, 0x20 ]
color3 = [ 0xFF, 0xB5, 0x20 ]
color4 = [ 0xFF, 0xFF, 0x20 ]
color5 = [ 0x20, 0xFF, 0x20 ]
color6 = [ 0x40, 0x40, 0xFF ]
color7 = [ 0x60, 0x20, 0xA0 ]



def fader ( steps, c1, c2, recurNum ):
	inc = map( lambda i:float(c2[i]-c1[i])/float( steps-1 ), range(0,3))

	for i in range(0,steps-1):
		inc1 = c1[0] + int(float(i)*inc[0])
		inc2 = c1[1] + int(float(i)*inc[1])
		inc3 = c1[2] + int(float(i)*inc[2])

		print( outputFormat % ( recurNum, 
				inc1, inc2, inc3,
				(inc1+0x80)%0x100,
				(inc2+0x80)%0x100,
				(inc3+0x80)%0x100 ))
		recurNum += 1

	#print( outputFormat % ( recurNum, c2[0], c2[1], c2[2] ))
	return( recurNum )

primeNum = fader(  steps = numSteps, c1 = color1, c2 = color2, recurNum = primeNum )
primeNum = fader(  steps = numSteps, c1 = color2, c2 = color3, recurNum = primeNum )
primeNum = fader(  steps = numSteps, c1 = color3, c2 = color4, recurNum = primeNum )
primeNum = fader(  steps = numSteps, c1 = color4, c2 = color5, recurNum = primeNum )
primeNum = fader(  steps = numSteps, c1 = color5, c2 = color6, recurNum = primeNum )
primeNum = fader(  steps = numSteps, c1 = color6, c2 = color7, recurNum = primeNum )

# vim: set noexpandtab ts=4 sw=4 foldmethod=marker:
