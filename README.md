# Pi_Finder.py
How big is Pi? Well, not too big because 4 is greater than Pi. So ,theoretically, your name is somewhere in Pi. Pi Finder.py finds where in Pi a given string is located. First off, everything behind the scenes is calculated in hexidecimal. The input string that Pi Finder is searching for converts that input string to hex using ASCII standards. Pi is calculated using the Bailey Borwein Plouffe formula, a generator function that yields the nth digit of Pi in hexidecimal form. From there is it pretty much just a sequential search one digit of pi at a time. As to why I wrote it in python, well that's because I Pi Finder.py sounds alot better and cooler than Pi Finder.c. Since Python is not that great for multithreading I think this could be sped up using C with multithreading, having each thread calculate a digit of pi.

## Warning(kind of)
Pi is a really big, it takes about 5 hours for this program to calculate 10^6 digits of pi. So odds are that if you run this program looking for your name or anything it will take a while. This is more of a theoretical project with no real practical application. I mostly rely on the test cases as proof that it works and don't really run the program itself. 

## Installing and Running
You really only need the pi_finder.py script and Python installed and you are good to go. Just run it from the command line, give it a string to look for and it'll start searching. You'll need Pytest to run the test cases if you really want to.

## Test Cases
Again, since this is more of a theoretical project, I rely heavily on my tests to prove that Pi Finder works as intended

This first test only tests that my BBP function accurately generates the first million digits of Pi in hex. I feel confident in saying that if the first million are correct then digits past the first million are correct by the principle of induction. This test takes about 5 hours so I wouldn't reccomend running it.
![mil_digits_test](https://user-images.githubusercontent.com/38610139/55774807-9330b280-5a4b-11e9-9b03-af191cc09793.png)

The other three tests just test the functionality of the program. Converting ints to hex strings, turning the input into its hex string representation, and searching for a given string in Pi.
![other_tests](https://user-images.githubusercontent.com/38610139/55774941-13571800-5a4c-11e9-8fe2-d99ecb2b9e41.png)

