Homework files for Python Beginning course
=====================

[Milestone 1 “Back to school”](milestone_1)
-----------------------------------
File [equations.py](milestone_1/equations.py) contains a solver for quadratic equations.
The user enters an equation as a string, and it’s need to extract coefficients (using only the functions to work with a string) and calculate the answer with the quadratic formula.

_Topics:_
*	_Variables and Built-in Functions_
*	_Boolean, None, and Strings_
  

[Milestone 2 “Secret messages”](milestone_2)
-----------------------------------
Here there are two Python files [encrypt.py](milestone_2/encrypt.py) and [decrypt.py](milestone_2/decrypt.py). 
File [encrypt.py](milestone_2/encrypt.py) can read the user message and the key, then encrypt this message using the Caesar cipher and output the results.
File [decrypt.py](milestone_2/decrypt.py) decrypts message encrypted with the Caesar cipher (it needs the user message and the key for it) and also outputs the results.

_Topics:_
*	_Conditions and Loops_
* _Functions_
  

[Milestone 3 “Pascal's Triangle”](milestone_3)
-----------------------------------
Here there is a file [triangle.py](milestone_3/triangle.py) with a function, which returns the triangle as a list of lists with the specified number of rows (Pascal's Triangle).
In the same file, there is also logic to get the number of rows from command line arguments and print the resulting triangle to the console.

_Topics:_
*	_Scope. Tuples_
*	_Lists_
  

[Milestone 4 “Trade-offs”](milestone_4)
-----------------------------------
In this case file [trade_offs.py](milestone_4/Trade_offs.py) contains the functions to find the pair (or pairs) of elements in some list that sum up to the `target`` value.
First one solves this problem in a brute-force manner with a double for-loop.
Second function does the same as the first one, but with lower time complexity.

_Topics:_
*	_Sets and Dictionaries_
*	_Complexity of Algorithms_
  

[Milestone 5 “Ancient, Inc.”](milestone_5)
-----------------------------------
Contains a program [generate_data.py](milestone_5/generate_data.py), which can generate synthetic data with Faker package and write data to [database.csv](milestone_5/database.csv) file. 
Another program here is [report.py](milestone_5/report.py) that can take as arguments from the command line the database file name and some criterion (in this case it’s month) and print the search result as a report.

_Topics:_
*	_Context Managers and Files_
*	_Decorators_
  

Milestone 6 “Bookkeeping”
-----------------------------------
**This repository** with files organized in the certain structure is the homework task.

_Topics:_
*	_Git_
*	_Modules and packages. Projects_


Milestone 7 “Ancient, Inc. 2”
-----------------------------------
Here there are several files. 
In [server.py]() a simple **flask** server is implemented. 
It has that will have 2 defined endpoints. 
The response is a JSON-encoded report. 
The server was tested locally on port 5000. 
Database for this case is [database.csv] ()
[utils.py]() is a module with some functions that were used to complete response with data from database due to requests.
[fetch_report.py] conteins a cli-utility to query the API using **requests** library. 

_Topics:_
*	_API. Clients_
*	_Servers_




