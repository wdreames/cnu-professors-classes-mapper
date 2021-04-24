# cnu-professors-classes-mapper

This is a program that creates a list of all the classes taught by a professor at CNU. The program can also list all the professors that teach a specific class at CNU. 

During runtime, the proram will ask the user if they would like to see information on classes, professors, or both:
* Entering "classes" would output all of the teachers that teach a specific class. For example, the line, ```CPSC 327  {'Perkins, Keith', 'Selfridge, Justin'}```, would indicate that CPSC 327 has been taught by Keith Perkins, and Justin Selfridge). 
* Entering "professors" would output all of the classes each professor teaches. For example, the line, ```Phelps, William {'CPSC 250L', 'CPSC 250', 'DATA 201'}```, would indicate that William Phelps has taught CPSC 250, CPSC 250L, and DATA 201. 
* Entering "both" will display both lists of data.


## Usage

```
python professor-class-mapper.py 
```
