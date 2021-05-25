# Projeto de Software 2020.1 part II
## Professor Baldoino Fonseca dos Santos

## Código inicial -> src/main.py

### Code Smells

1. Long Method:
  1.1 The size of the parameter list
	1.2 You are getting several values from an object and
	passing these values as parameters in a method call
	1.3 You have a group of parameters that
	naturally go together - Data Clumps
	1.4 A method is trying to do too much
	1.5 The amount of switch statement for dispatching
	and handling request
	1.6 The amount of switch statement to gather data from
	numerous classes with different interfaces
	1.7 The amount of switch statement to gather data from
	numerous classes with different interfaces
	
2. Large Class:
	Fields and methods

3. Shotgun Surgery:
	When every time you make a kind of change, you have to make a lot of
	Little changes to a lot of different classes

4. Feature Envy:
	A method that seems more interested in a class
	other than the one it actually is in.

5. Lazy Class:
	A class that is not doing enough to pay for itself.

6. Message Chains:
	Example: object.getE().getD().getC().getB().getA().getValue();

*7. Indecent Exposure:
	Methods or classes that ought not to be visible to clients are
	publicly visible to them
