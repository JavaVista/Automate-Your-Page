#Javi's Stage 2 Submission

def create_html(title, heading, description):
    '''Creates the 1st part of my html structure'''
    html_title ='''
        <div class="title">
            <h2>''' + title
    if title == '': #removes tag if title is empty
            html_title ='''
        <div class="title">
            ''' + title
    html_heading = '''</h2>
            <div class="heading">
            <h3>''' + heading
    if title == '': #removes closing tag if title is empty
            html_heading = '''<div class="heading">
                <h3>''' + heading
    html_description = '''</h3>
            </div>
            <div class="description">
            <p>''' + description
    html_bottom = '''</p>
            </div>
        </div>'''
    html_text =html_title + html_heading + html_description + html_bottom #adds the above html tags with the text location in the list
    return html_text


my_title_headings_descriptions = [['Telling Computers What to Do','Computers are Different', 'Machines are designed to do a few things like a toaster. Unless you physically alter these machines, they will only be able to do those things.Computers are different because they need instructions to tell it what to compute. <em>Computers</em> can be programmed to do anything we want, as long as we can write a program that specifies a specific sequence of instructions. <p class="img"><strong>A PC vs a Toaster:</strong></p> <p class="img"><img src= "images/pcvstoaster.png" title="PC vs Toaster" alt="A PC vs a Toaster">'],
                                   ['','A Programming Language that has Grammar', 'A <em>Programming Language</em> is what programmers use to tell a computer what to do. Programing Languages have Grammar like Human Languages.  A <em>Grammar</em> is a specification of what is "correct" and what is "incorrect." People can often understand sentences that are not technically "correct," but computers cannot because they are not smart enough. Therefore, you will have to write the <em>Programing Language</em> code with the "correct" <em>Grammar</em> according to the according to the Programing Language Syntax or it will no run in the Computer.'],
                                   ['','Instructions with a Computers Program', 'A <em>Computer Program</em> are steps and instructions that a Computer can follow. A web browser, a game and apps in a mobile phone are examples of computer programs or even the print statement in computer language like <em>Python</em>. <em>Python</em> is a programming language that uses a Python Interpreter that converts the code you wrote as set of step instruction that the Computer can understand and execute.'],
                                   ['Programming Seriously with Python','What is a Variable in Python?', 'A Python <em>"Variables"</em> are nothing but reserved memory locations to store values. This means that when you create a variable you reserve some space in memory. Variables give programmers a way to give names to values. If <span>my_variable</span> is a variable with a value of <span>2</span>, then the following code would print out <span>4</span>: <span>print my_variable + my_variable</span>'],
                                   ['','Variable and different ways to assign values', 'We can assign the value <span>2</span> to the variable <span>my_variable</span> by writing code like this: <span>my_variable = 2</span> In Python, <span>2</span> is a number while <span>"2"</span> is a string.The code <span>2 + 2</span> would give <span>4</span>.The code <span>"2" + "2"</span> would give <span>"22"</span>. We can even change the value of a variable by re-assigning it to a different value later. More Examples: the line <span>2 + 3 = 5</span>, the equals sign means "is the same as". The plus <span>+</span> mean concatenate in other word in a chain together. A comma <span>,</span> means pairs. Square Brackets <span>[ ]</span> gives a location of a string character. Using the colon <span>:</span> on a square brackets it gives the start and end of a location. Using a location number position. Also called indexing. In the line <span>my_variable = 5</span>, the equals <span>=</span> sign means "takes the value".'],
                                   ['','Function also called a Procedure', 'A <em>"Function"</em> is a block of organized, reusable code that is used to perform a single, related action. Functions are made by starting a line of code with the keyword <span>def</span> and then giving a function name followed by the function parameters in parentheses <span>( )</span>. parameters are what go inside the parentheses. Parameters are variables use in the function definitions that is a "handle" that allows the code in the function to access the arguments for a particular These parameters will eventually be replaced by actual values when the function is used (called). <p class="img"><strong>Here is an example of a Function:</strong></p> <p class="img"><img src= "images/function.png" title="Function" alt="Function example">'],
                                   ['','How do functions help to avoid repetition?', 'Functions are tools that programmers can create and reuse forever! Once you\'ve defined a function once, you never have to define it again.'],
                                   ['','Loops & Recursion', ' You can tell a computer to repeat a bit of code between point A and point B, until the time comes that you need it to stop. Such a thing is called a <em>Loop</em>. There are two types of loops in Python, <span>for</span> and <span>while</span>. <em>Recursion</em> means; defining something in terms of itself, usually at some smaller scale, perhaps multiple times, to achieve your objective. <p class="img"><strong> Recursion & Loops examples:</strong></p> <p class="img"><img src= "images/loops.png" title="Loops" alt="Recursion & Loops">']]

#-------------------------------------------------------------------------------
# This functions are here for when I need them & not used within the final output
# I submitted them for you to just review and to see if I creating them correctly

def get_title(concept):
    title_location = concept[0][0]
    return title_location

def get_heading(concept):
     heading_location = concept[0][1]
     return heading_location

def get_description(concept):
    description_location = concept[0][2]
    return description_location

#-------------------------------------------------------------------------------

def make_html(notes):
    '''Code that generates the full html page and the actual notes in the list'''
    list_title = notes[0]
    list_heading = notes[1]
    list_description = notes[2]
    notes = create_html(list_title, list_heading, list_description)
    return notes


def make_html_for_all_notes(list_of_items):
    '''function that takes all html plus the top and bottom of the full page and
     insert all notes at once'''
    html_start = '''<!DOCTYPE html>
<html>
<!-- Stage 2 submission. -->
<head>
<link rel="stylesheet" href="style.css">
<title>Javi's Important Notions</title>
</head>
<body>
    <div class="page">
        <h1>Notions that are Important</h1>'''
    html_end = '''
    </div>
</body>
</html>'''
    html_page = html_start
    for item in list_of_items:
       page_html = make_html(item)
       html_page += page_html
    return html_page + html_end


print make_html_for_all_notes(my_title_headings_descriptions)
