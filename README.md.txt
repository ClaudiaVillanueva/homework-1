Students database

This program provides a database enginge, it loads student records from a file 
named "Students.txt". Student records on the input file must contain the following
tab-separated fields:

StudentId	Lastname	FirstName	GraduationYear	GraduationTerm	Program

After loading the file, the program asks the user to type a query.

"Enter your query:"

INPUT
The following queries are supported:

all                 Print all student records.
lastname [prefix]   Print student records whose lastname starts with the provided prefix.
graduating [year]   Print student records graduating on the provided year.
summary [year]      Print a summary of programs, student count and percentage graduating on
                    or after the provided year.

OUTPUT
The program prints all information from a student in the following format:

ID	FIRST	LAST	GRAD_YEAR	GRAD_TERM	DEGREE

EXAMPLES

Enter your query: lastname a

ID	   FIRST	LAST	   GRAD_YEAR   GRAD_TERM   DEGREE
101030   Daisy	Anthony  2020	   Fall	   MSBA
101980   Taniya	Ayers	   2019	   Spring	   MST
102000   Davon	Adkins   2019	   Fall	   MBA