# Unit 2: A multisensorial counter
#### By Angelos & Paula
![image](https://user-images.githubusercontent.com/89135778/146809644-e51813aa-4eaa-4374-bd85-ecf4c0aa9bd5.png)  
Design and implement a multisensorial counter (0-9) for a client that does not know the roman numbers. It should allow the user to count up and down from a set start.


# Criterion A: Planning

## Problem definition:
We need to design and implement a multisensorial counter that can count from 0 to 9 up and down from a set number. The client doesn’t know the roman numbers and has a disability. 
The product is being developed because it is important to be inclusive with everyone and we all have the right to be able to count from 0 to 9. There are many similar products that allow disabled users to count numbers, such as watches, traffic lights etc.

## Proposed Solution:
### Design statement:
We will design and implement a multisensorial counter (0-9) for a client that does not know the roman numbers. Specifically, the numbers from 0 to 9 will be presented with light and with sound. So everyone, including disabled people will be able to receive the information. The program will be based on binary code and is constructed using the software Python 3.0. It will take 3 weeks to make and will be evaluated according to the criteria A Planning, B Solution Overview, and C Development.


### Justify the software selected:
Python is one of the most accessible programming languages because it is not complicated and has simplified syntax very similar to the English language, which is perfect for beginners. According to PYPL and ZDNet [1], [2], Python is one of the most popular languages with about 30% of programmers use Python as their main programming language, so there is a big Internet community to ask for help. Also, its codes can be easily written and executed much faster than other programming languages. Python is an open source and has a lot of  tools, like functions or libraries to complement the code, so you can do practically anything with your code. It is also friendly for the programmers and the users, making it possible to be read even by people who are not programmers. It is easy to implement data structures in Python with built-in insert, append functions. Also, there is a large library of built-in functions in Python.
Finally, we will use an online conversor from Python to C so we can use our program in Arduino. 

[1] Tung, Liam. “Programming Languages: Python Just Took a Big Jump Forward.” ZDNet, ZDNet, 6 Oct. 2021, https://www.zdnet.com/article/programming-languages-python-just-took-a-big-jump-forward/

[2] “PYPL Popularity of Programming Language Index.” Index, https://pypl.github.io/PYPL.html


### Justify the structure of the proposed solution:
Our program has the typical type and it is easy to understand. There are comments on each step, so someone who reads the code can understand easily what is happening. Also, there are functions that make the code simple and variables with names that are understandable.

## Success Criteria
1. The counter has to count from 0 to 9, upwards and downwards.
2. All digits (0-9) will be presented with light and sound at the same time
3. Dots ( · ) will be represented with a light bulb and a sound that last 0.4 seconds, while the lines ( - ) will be represented with a light bulb and a sound that last 1 second.

## What is the personal relevance of the program? Why did you pick the theme?
We want to be inclusive and give opportunities to everyone. So, it is important that all people in the world have access to counting methods. Everyone has the right to have a counter, it shouldn’t matter having a disability. 
That is why we included light bulbs and sound, so that everyone will be able to understand it.
We chose a mix of binary and morse code for our counting system because it can be understandable for all and we personally like the idea of reading lines ( - ) and dots ( · ), as some spies and special forces.

# Criterion B: Design
| Decimal     | 0       | 1       | 2       | 3       | 4       | 5       | 6       | 7       | 8       | 9       |
|-------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| Binary      | 0       | 1       | 10      | 11      | 100     | 101     | 110     | 111     | 1000    | 1001    |
| Our program | · · · · | · · · - | · · - · | · · - - | · - · · | · - · - | · - - · | · - - - | - · · · | - · · - |

#### Fig.1: Comparision table of numerical systems

This table represents a conversion from decimal numbers to binary numbers, which then are converted to our own system where:
Dots (·) will be represented with a light bulb and a sound that last 0.5 seconds.
Lines (-) will be represented with a light bulb and a sound that last 3 seconds.

## System diagram
![image](https://user-images.githubusercontent.com/89135778/146818297-b8fd4a93-f886-44e4-8e13-9d272ff51344.png)

#### Fig 2: System diagram of the proposed solution  
This is the System Diagram. You can see how the program is operated in a computer HP with its specifications, with the operating system of Windows 10. The programme used to run this project is PyCharm Edu and the archive's name is counter.py. The code asks the user to input the starting number and to decide if they want to count downwards or upwards. Then, it processes the data and finally outputs sound and light to represent the numbers. 

## Test Plan
| Test                                              | Description                                                 | Procedure                                                          | Expected output                                                          |
|---------------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------|--------------------------------------------------------------------------|
| Unit test of the sound                            | This test is evaluating the function  for the sound.        | 1. Run the program sound.py 2. Select the direction and number.    | Sounds are heard and are numbers in our numerical system.                |
| Unit test of the light                            | This test is evaluating the function  for the lights.       | 1. Run the program light.py 2. Select the direction and number.    | Lights are seen and are numbers in our numerical system.                 |
| Unit test of the light and sound at the same time | This test is evaluating the function  for sound and lights. | 1. Run the program project2.py 2. Select the direction and number. | Sounds and lights are displayed and are numbers in our numerical system. |

This is a list of steps, table, or flow chart specifying the process for testing the solution with the inputs and expected outputs.


## Flow diagrams
![image](https://user-images.githubusercontent.com/89135778/146826227-7b536cbc-d6ee-46d8-93a0-b402d68bf5be.png)
#### Fig 3: Flow diagram 1 showing the counter upwards or downwards

![image](https://user-images.githubusercontent.com/89135778/146826414-073ed578-d887-4afe-b286-41d1e01f43ce.png)
#### Fig 4: Flow diagram 2 showing the counter upwards or downwards with a starting number

![image](https://user-images.githubusercontent.com/89135778/146826889-0e059f04-71d3-4d5c-8168-0244daca6d95.png)
#### Fig 5: Flow diagram 3 showing the counter in Binary Morse system upwards or downwards

## User Interface Sketch
![image](https://user-images.githubusercontent.com/89135778/146828883-67bc57c5-711a-4db1-9fef-ac41668e372f.png)
#### Fig 6: Arduino webpage with our program

## Record of Tasks
| Task No | Planned Action                                                    | Planned Outcome                                                                                  | Time estimate | Target completion date | Criterion       |
|---------|-------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|---------------|------------------------|-----------------|
| 1       | Write problem definition, proposed solution and success criteria. | For having clear ideas about the project, the design, the software and the goals.                | 40min         | Dec 8                  | A - Planning    |
| 2       | Create system diagram                                             | To have a clear idea of the hardware and software requirements for the proposed solution.        | 10min         | Dec 9                  | B - Design      |
| 3       | Create flow diagrams                                              | To have clear ideas on how to code and how the programme would work.                             | 40min         | Dec 14                 | B - Design      |
| 4       | Think about test plan                                             | For having clear goals and what to expect.                                                       | 10min         | Dec 14                 | B - Design      |
| 5       | Code the base of the program                                      | There are different python codes for our program.                                                | 30min         | Dec 14                 | C - Development |
| 6       | Make some improvements in the code                                | General improvements.                                                                            | 1h            | Dec 15                 | C - Development |
| 7       | Improve user intuitive instructions                               | Change some codes so it is easier to the user to understand the game, based on the previous test | 20min         | Dec 15                 | C - Development |
| 8       | Write tools and techniques used in the program                    | So they can be accessible all time and anyones knows the resources used.                         | 30min         | Dec 15                 | C - Development |
| 9       | Convert Python code to C and Arduino                              | Arduino Tinkercad uses C language for running its programs so we have converted our Python code. | 1h            | Dec 17                 | C - Development |
| 10      | Make some improvements in the Arduino code                        | Adding light and sound and changing their duration                                               | 2h            | Dec 18                 | C - Development |
| 11      | User interface sketch                                             | Photo of Arduino as the user interface sketch                                                    | 5min          | Dec 18                 | B - Design      |

# Criterion C: Development
## Existing tools
- Python
- C Language
- Converter from Python to C Language [1] 
- Arduino Platform [2]
- GitHub [3]

#### Links:
[1] https://pythoncsharp.com/  
[2] https://www.tinkercad.com/dashboard  
[3] https://github.com/  

## a) List of techniques used
#### - Variables
Variables are used for storing values as if the user wants to go upwards or downwards and the number he will start counting.
#### - Conditions: If, elif, else statements
With the if, elif and else statements we make sure that there are not incorrect values given by the user in the variables. Then we use them to run our program correctly.
#### - While loops
We use the while loops to create a repetition of instructions and to make sure all the correct numbers are shown.
#### - For loops
We use the while loops to create a repetition of instructions during a concrete time.
#### - Input instruction
We use this to create variables by an instruction given by the user. 
#### - Print instruction
We use the print instruction to give messages to the user and show the result of the counting.
#### - Data Encoding
Computers use data encoding to store and retrieve meaningful information as data.
#### - Functions
Modules of code to run when it’s convenient and do a specific task inside the program.

## b) Development


