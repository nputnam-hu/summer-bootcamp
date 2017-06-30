### Day 4 Hacktime
- There are folders with different example solutions of the various problems, look through them so that you can better help students who are struggling with them
- The skeletons directory will be the one students will get the zip for from google drive and unzip in their local directory
- bootcamp.py is a helper file that can be imported to use functions that are beyond the scope of the project.  Students should feel free to look into it if they want to see under the hood
- Common error messages and their meanings:


| Error | Translation |
| ------ | ------ |
| SyntaxError: EOL while scanning string literal | Student has an unclosed string quote somewhere |
| File "water_1.py", line 4,bottles = minutes * 12,^ SyntaxError: invalid syntax | Student has an error on line 3 such as an unclosed parantheses |
| TypeError: 'str' object is not callable | Student forgot the `%` for print syntax |
| python: can't open file 'water_1.py2': [Errno 2] No such file or directory | Student misspelled file name when trying to run it | 
IndexError: list index out of range | Student tried to access a list index that does not exist|
