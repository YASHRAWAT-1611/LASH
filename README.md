# LASH
LASH PROGRAMMING LANGUAGE DOCUMENTATION

Introduction

Lash is a simple, object-oriented programming language inspired by Python, C++, and Java. It is designed for readability and ease of use while maintaining powerful object-oriented features. Lash eliminates the need for "self" when accessing attributes and methods within a class, making it similar to C++ and Java.

1. Basic Syntax

Lash uses a simple and clean syntax where variable declarations do not require var or =. The type is inferred automatically.

1.1 Variable

![image1](image-4.png)

No need for = or var
Type is inferred automatically.
Strings are enclosed in double quotes " ".
Numbers, floats, and booleans do not require special declaration.

1.2 Type Casting

![image2](image-1.png)

to_num converts to an integer.
to_str converts to a string.
to_float converts to a float.

2. Input & Output

2.1 Displaying Output

![image3](image-2.png)

2.2 Taking User Input

![image4](image-3.png)

Default values can be provided: city ask "Enter city:" "New York"
Multipe values: x, y ask "Enter two numbers; "

2.2.1 HOW ask WORKS IN LASH ?

The "ask" function in Lash is used to take user input in a simple and intuitive way. It works similarly to "input()" in other languages but has additional features like default values and multiple inputs.

2.2.2 HOW ask RETURNS VALUES ?

By default, ask returns a string.
If you want a number, you need to convert it using to_num.

![image70](image-70.png)

2.2.3 DEFAULT VALUES IN ask

If the user presses Enter without typing anything, ask can return a default value.

![image71](image-71.png)

Example Input & Output
![image72](image-72.png)

If the user enters "Los Angeles", the output will be:
![image73](image-73.png)

2.2.4 Multiple Inputs in One Line

Lash allows you to space-separate multiple inputs in a single ask.
![image74](image-74.png)

Example Input & Output
![image75](image-75.png)

The user enters 5 10, and ask splits the input into x and y.
They are converted to numbers using to_num.

3. Operators

3.1 Airthmetic Operators

+ , - , * , / , % , **

![image5](image-5.png)

3.2 Comaprison Operators

= , != , > , < , >= , <= 

![image6](image-6.png)

Example

![image7](image-7.png)

3.3 Logical Operators

and , or , not

![image8](image-8.png)

Example

![image9](image-9.png)

3.4 Assignment Operators

![image50](image-50.png)

4. Control Flow

4.1 If-Else Statements

![image10](image-10.png)

4.2 If-Elseif-Else Statements

![image11](image-11.png)

4.3 Loops

Repeat (for loop)
![image12](image-12.png)

Loop (while loop) 
![image13](image-13.png)

4.4 Breaking and Continuing Loops

4.4.1 Stop (Break) - Exit the loop early
![image60](image-60.png)

4.4.2 Skip (Continue) - Skip current itreation
![image61](image-61.png)

5. Functions

Lash should have a simple and clean function syntax. No need for def or complex syntax—just use a keyword like fn

5.1 Definig & Calling Functions

![image14](image-14.png)

5.2 Returning Values

![image15](image-15.png)

5.3 Function with/without parameters

a.Functions without parameters
![image65](image-65.png)

b.Functions with parameters
![image66](image-66.png)

5.4 Functions with Return Value
![image67](image-67.png)

5.5 Default Parameter Values
![image68](image-68.png)

5.6 Recursive Function
![image69](image-69.png)


6. Arrays, Sets, Dictionary Functions

Lash arrays should be simple and easy to manipulate. Here’s how arrays work in Lash, along with useful built-in functions.

6.1 Creating and Accessing Arrays

![image16](image-16.png)

6.2 Modifying Arrays

![image17](image-17.png)

6.3 Array Operations

Adding Elements
![image39](image-39.png)

Removing Elements
![image40](image-40.png)

Checking Array Length
![image41](image-41.png)

Searching
![image42](image-42.png)

Sorting
![image43](image-43.png)
By default, sort() sorts numbers in ascending order.

Sorting in descending order:
![image44](image-44.png)

Reversing Array
![image45](image-45.png)

Finding Index of an Element
![image46](image-46.png)

Counting Occurrences of an Element
![image47](image-47.png)

Joining Arrays
![image48](image-48.png)

Slicing Array
![image49](image-49.png)



6.4 Multi-Dimensional Arrays (Matrices)

Lash should support multi-dimensional arrays for matrices and sets for unique values.

A multi-dimensional array is just an array of arrays.
![image35](image-35.png)

6.4.1 Multi-Dimensional Arrays(Matrices) Operations


Looping Through a Multi-Dimensional Array

![image36](image-36.png)

Getting the Number of Rows & Columns

![image37](image-37.png)

Transposing 

![image38](image-38.png)

6.5 Sets (Unique Values)

A set is a collection of unique elements.

![image23](image-23.png)

6.5.1 Set Operations

Adding Elements

![image29](image-29.png)

Removing Elements

![image30](image-30.png)

Checking Membership

![image31](image-31.png)

Set Union (Combine Two Sets)

![image32](image-32.png)

Set Intersection (Common Elements)

![image33](image-33.png)

Set Difference (Elements in A but Not in B)

![image34](image-34.png)

6.6 Dictionary (Key-Value Pairs)

![image24](image-24.png)

6.7 Tuples

![image28](image-28.png)

7. Strings and its Functions

Strings can be defined as variables are created.
![image51](image-51.png)

7.1 String Functions

Finding length of a string
![inage52](image-52.png)

Changing Case
![image53](image-53.png)

Checking if a string contains another string
![image54](image-54.png)

Replacing parts of a string
![image55](image-55.png)

Splitting a string into a list
![image56](image-56.png)

Joining a list into string
![image57](image-57.png)

Trimming Whitespace
![image58](image-58.png)

Getting a Substring
![image59](image-59.png)

8. Object-Oriented Programming (OOP)

Lash should have a simple and readable way to define and use classes and objects, avoiding unnecessary complexity.

8.1 Defining a Class

Lash uses class to define a class and fn for methods.

![image19](image-19.png)

No self!
Directly access name and age inside the class.

8.2 Crating Objects 

Objects are created like in C++/Java, without new.

![image20](image-20.png)

8.3 Modifying Attributes

Direct access, just like in Java/C++.

![image76](image-76.png)

8.4 Class Methods (Static Methods Like Java)

Class methods work like static methods in Java.

![image77](image-77.png)

8.5 Private Attributes & Methods

Prefix with _ to make attributes/methods private (like C++ private).

![image78](image-78.png)

_balance can’t be accessed directly outside the class.

8.5 Inheritance

No need for super – attributes are inherited directly.

![image25](image-25.png)

8.6 Encapsulation

![image26](image-26.png)

8.7 Polymorphism

![image27](image-27.png)

9. Error Handling

9.1 Try-Catch Mechanism

![image21](image-21.png)

Conclusion

Lash is designed to be easy to learn while supporting powerful OOP features like Java and C++. It simplifies syntax while keeping familiar programming paradigms. Happy coding in Lash!