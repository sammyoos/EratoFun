EratoFun
========

Exploration of the Sieve of Eratosthenes
----------------------------------------


A number of years ago I was playing with the Sieve of Eratosthenes and 
noticed that when iterating through the list of integers and marking the
composites that the gaps between numbers that were marked by that particular
prime, had interesting patterns.  I found the following properties:
- the first composite knocked out was always the square of the prime
- the gaps were were always even multiples of the prime being iterated
- the gaps had very distictive similarities

The page displayed at http://sammyoos.github.io/EratoFun shows this pattern
as best as I could to demonstrate the similarities.  I have, for some time,
tried to figure if the numbers are predictable, but so far have not had success.

The page displayed, shows the gap between composites knocked out by each 
prime being interated over (divided by two because all the gaps are even).  Each
row is also shifted over by one, to highlight the similarities between the rows.

_Sam_


Interesting Bit
---------------


I'm sure someone a fair bit smarter than me has already discovered this,
but in case not...

**Sammy's Conjecture**

For all primes, take the gap "g" between the square of that prime "p" and the next integer 
"c" that would be marked as a composite of that prime (and had not already been marked as a
composite of a smaller prime) by the Sieve of Eratosthenes, and you get the following
equation for the successive prime number "p'":

p' = p + g/p

Interestingly, then, c must equal p x p' as g = c - p * p

So, once the sieve has been completed for all primes less than or equal to P, the sieve
provides three ways to determine the next prime (in order of increasing complexity):

1. the next unmarked integer in the sieve array (Step #4 here: [wikipedia.org/wiki/Sieve_of_Eratosthenes](http://en.wikipedia.org/wiki/Sieve_of_Eratosthenes#Algorithm_description ))
2. p' = p + g / p (as shown above)
3. p' = c / p

It follows that #2 and #3 are valid iff p' = p + g/p.

