"""
HTML FORM BUILDER: 
Creating HTML forms is a very tedious process at large scales. 
It requires copying elements and creating random attributes such as 
‘id’ and ‘name’ in radio buttons. It also requires adding special 
characters such as ‘\n’ to make the file readable for developers and 
‘<br>’ for formatting the form. Since HTML is a relatively syntactically
 simple language, a computer can do a much better job at creating these
 forms.  
 
 This program attempts to automate the task of creating contact 
 forms, ‘test.html’ is a file in the same directory as the main python 
 file. It has the base templating of a contact form, and the python 
 script reads the existing HTML elements to see what IDs are already
 taken and writes to the file to add HTML new elements. Four elements
 can be added to the html form: select (dropdowns), radio buttons, 
 text inputs and date inputs Users can  generate base HTML code this 
 way in seconds by following the program’s prompts. 

"""


def generate_random_string(length=8): 
    """
    Function that generates a random string for id/name of HTML radio element
    Default Length: 8 Characters 
    """
    import random 
    allUpperCase = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    allLowerCase = [chr(x) for x in range(ord('a'), ord('z')+1)]
    allNum = [chr(x) for x in range(ord('0'), ord('9'))]
    # List comprehensions that generate all letters and numbers as choices for random string generator 
    randstring=""
    # Create a random string that function will add to. 
    for i in range(0, length-1):
    # Iterate through number random selections you want to make
        firstRand = random.randint(0,2)
        #Make first random guess which will decide whether character will be uppercase, lowercase or number
        if(firstRand ==0): 
            secondRand = random.randint(0, len(allUpperCase)-1)
            randstring+=allUpperCase[secondRand]
            #Make another random guess within uppercase and add character to string
        elif(firstRand==1): 
            secondRand = random.randint(0, len(allLowerCase)-1)
            randstring+=allLowerCase[secondRand]
            #Make another random guess within lowercase and add character to string
        else:
            secondRand = random.randint(0, len(allNum)-1)
            randstring+=allNum[secondRand]
            #Make another random guess within number and add character to string

    return randstring
     
def filter_radio_elements(radioEls):
    """
    Function that filters existing radio elements and gets their name and id values
    (Called in the main function)
    
    @parameter radioEls passed that contains all the radio elements in test.html 
    """
    radioNameId =[]
    for i in radioEls:
        #iterate through radioEls with for loop        
        indexOfName = i.index('name')
        #Get the index of the substring name attribute of the element
        indexOfId = i.index('id')
        #Get the index of the substring id attribute of the element 
        nameStr=i[indexOfName:]
        #Slice the name string to begin at the name substring 
        idStr=i[indexOfId:]
        #Slice the id string to begin at the id substring 
        innerNameFirstOcc = nameStr.find('"')+1
        #Find the " character index and add 1 to the index so when you split string, you split exclusive of the first occurrence of "
        innerNameSecondOcc = nameStr.find('"', innerNameFirstOcc)
        #Find the next occurrence starting at the first occurrence (prevent repeats)
        innerIdFirstOcc = idStr.find('"')+1
        #Find the " character index and add 1 to the index so when you split string, you split exclusive of the first occurrence of "
        innerIdSecondOcc = idStr.find('"', innerIdFirstOcc)
        #Find the next occurrence starting at the first occurrence (prevent repeats)
        name = nameStr[innerNameFirstOcc:innerNameSecondOcc]
        idof = idStr[innerIdFirstOcc:innerIdSecondOcc]
        #Get the value in between the quotes for both name/id
        radioNameId.append(name)
        radioNameId.append(idof)
        #append both to list to be checked. 
    return radioNameId


def delete_elements_tobe_readded(deleteEls=[]):
    """
    Function that deletes necessary elements     
    @parameter  deleteEls contains elements to be deleted
    """

    fp = open('test.html', 'r')
    #open the file in read mode
    lines = fp.readlines()
    #read all lines
    
    fp =open("test.html", 'w')
    #open the file in write mode

    for number, line in enumerate(lines):
        #for each line check if the index of the line is in deleteEls, if it is don't write it to overwritten version of file
        if number not in deleteEls:
            fp.write(line)
    fp.close()  
    #close the file

def form_builder():
    """
    Main Form Builder Function, executes the main program
    """
    fileoutput = open('cps109_a1_output.txt', 'w')
    print("----- Welcome To The MILLIE HTML FORM BUILDER ---------\n")
    fileoutput.write("----- Welcome To The MILLIE HTML FORM BUILDER ---------\n")

    while(True):
        #While loop that continues until the user decides to exit the program. 
        optionChoice = int(input("Select your options from below by entering a number:\n 2. Add to your existing your form(file should be in this directory and be called test.html) \n 3. Exit the program \n"))
        fileoutput.write("Select your options from below by entering a number:\n 2. Add to your existing your form(file should be in this directory and be called test.html) \n 3. Exit the program \n")
        fileoutput.write(str(optionChoice))
        fileoutput.write("\n")
        #User is given option choices about whether they would like to add to a form or exit the program. 
        if(optionChoice == 3):
            print("\n \n PLEASE SEE test.html FILE IN SAME DIRECTORY")
            fileoutput.write("\n \n PLEASE SEE test.html FILE IN SAME DIRECTORY")
            #If the user decides to exit, break the loop and end the program.
            break; 
            
        elif(optionChoice ==2):
            #If the user decides to build/use a form...
            file = open('test.html')
            #Open test.html in read mode
            if(file.closed):
                #Check to make sure file opened otherwise return an error. 
                return "File Error, could not open"
            
            whichFormVar = {"formTitle":"", "selectNum":0, "textNum":0, "dateNum":0, "mcNum":0 }
            #Create a dictionary to keep track of how many elements there are...
            radioEls = []
            #Initialize a list to get all radio elements in below for loop
            deleteEls=[]
            #Initialize a list to get all lines we would like to delete and then re-add at the end. 
            x=0
            #Initialize a counter for the for loop to keep track of index of line in file. 
            for lineFile in file: 
                
                lineFile = (lineFile).replace("\n", "")
                #Iterate through the lines in the file and get rid of \n which show up in values
                
                #Lines are predefined (what is on each), ie: line 1 is formtitle
                if(x==1):
                    whichFormVar['formTitle'] = lineFile
                elif(x==2):
                    whichFormVar['selectNum'] = int(lineFile.replace("#ofselect: ", ""))
                    #filter by replacing key words to get predefined values in the file
                elif(x==3):
                    whichFormVar['textNum'] = int(lineFile.replace("#oftext: ", ""))
                elif(x==4):
                    whichFormVar['dateNum'] = int(lineFile.replace("#ofdate: ", ""))
                elif(x==5):
                    whichFormVar['mcNum'] = int(lineFile.replace("#ofmc: ", ""))
                else:
                    if('radio' in lineFile):
                        #if radio is in the file, the element is a radio button and we make note of it by adding to a list
                        radioEls.append(lineFile)
                    if('</div>' in lineFile or '</html>' in lineFile or '</body>' in lineFile or '<input type="submit">' in lineFile or '</form>' in lineFile):
                        deleteEls.append(x)
                        #we need to replace certain elements and then re-add them at the end because they must be at the end of the file
                x+=1
            
            file.close()
            #Close the file 
            radioNameId = filter_radio_elements(radioEls)
            #Perform radio element filtering to make a list of ids/names already used
            
            delete_elements_tobe_readded(deleteEls)
            #Delete elements to be readded
            
            totalElements = whichFormVar['selectNum'] + whichFormVar['textNum'] + whichFormVar['dateNum'] + whichFormVar['mcNum']
            #Calculate the total elements 
            print(f"Your form information is as follows: \n Form Title: {whichFormVar['formTitle']} \n Total # of Elements: {totalElements} \n # of Select Inputs: {whichFormVar['selectNum']} \n # of Text Inputs: {whichFormVar['textNum']} \n # of Date Inputs:{whichFormVar['dateNum']} \n # of MC Input: {whichFormVar['mcNum']} \n    ")
            #Present form information to user (total elements, title etc...)
            fileoutput.write(f"Your form information is as follows: \n Form Title: {whichFormVar['formTitle']} \n Total # of Elements: {totalElements} \n # of Select Inputs: {whichFormVar['selectNum']} \n # of Text Inputs: {whichFormVar['textNum']} \n # of Date Inputs:{whichFormVar['dateNum']} \n # of MC Input: {whichFormVar['mcNum']} \n    ")
            elementToAdd = int(input("What would you like to add to your form? (Enter Number):\n 1.Select/Dropdown  \n 2.Text Input \n 3. Date Input \n 4. Multiple Choice/Radio Button \n"))
            fileoutput.write("What would you like to add to your form? (Enter Number):\n 1.Select/Dropdown  \n 2.Text Input \n 3. Date Input \n 4. Multiple Choice/Radio Button \n")
            fileoutput.write(str(elementToAdd))
            fileoutput.write("\n")
            #Prompt user to allow input to what the user wants to add to form
            labelOfElement = input("Please enter the label for your element...\n")  
            fileoutput.write("Please enter the label for your element...\n")
            fileoutput.write(labelOfElement)
            fileoutput.write("\n")
            
            #Prompt user for label input for element
            file = open('test.html', 'a')
            #open test.html file and add to it 'a'
            if(file.closed):
                return "File Error, could not open"
            #check that file opened 
            
            file.write(f"<label> {labelOfElement} </label><br>\n")
            #write label to file
            
            """
            Depending on what type of element to add, write it to the file and then increment corresponding
            element in dictionary by 1 
            """
            if(elementToAdd ==2):
                file.write("<input type='text'><br>\n")
                whichFormVar['textNum']+=1
            elif(elementToAdd == 3):
                file.write("<input type='date'><br>\n")
                whichFormVar['dateNum']+=1
            elif(elementToAdd ==1):
                file.write("<select>\n")
                whichFormVar['selectNum']+=1
                numOfChoices = int(input("How many options in select? \n"))
                fileoutput.write("How many options in select? \n")
                fileoutput.write(str(numOfChoices))
                fileoutput.write("\n")
                #Prompt user to get how many options
                x=0
                while(x<numOfChoices):
                    """ Iterate through options and 
                    prompt user to type in """
                    
                    choice_name = input(f"Choice #{x+1}: ")
                    fileoutput.write(f"Choice #{x+1}: ")
                    fileoutput.write(str(choice_name))
                    fileoutput.write("\n")
                    file.write(f"<option>{choice_name}</option><br>\n")
                    x+=1
                file.write("</select><br>\n")
            else:
                numOfChoices = int(input("How many options in radio? \n"))
                fileoutput.write("How many options in radio? \n ")
                fileoutput.write(str(numOfChoices))
                fileoutput.write("\n")
                whichFormVar['mcNum']+=1
                nameGen = generate_random_string(7)
                #In a radio html element, there is a name attribute that links all options together. 
                while(nameGen in radioNameId):
                    #Generate a random name until you produce a unique one (not already used)
                    nameGen = generate_random_string(7)
                x=0
                
                
                while(x<numOfChoices):
                    #Collect different choices
                    choice_name = input(f"Choice #{x+1}: ")
                    fileoutput.write(f"Choice #{x+1}: ")
                    fileoutput.write(str(choice_name))
                    fileoutput.write("\n")
                    idGen = generate_random_string()
                    #
                    while(idGen in radioNameId):
                        #Generate a random id until you produce a unique one (not already used)
                        idGen = generate_random_string()
                    file.write(f"<input type='radio' name=\"{nameGen}\" id=\"{idGen}\"><label>{choice_name}</label><br>\n")
                    #write radio and attributes to file
                    x+=1
                
            file.write('<input type="submit"> \n </form> \n </div> \n </body> \n</html>\n')
            #write submit button to the html form
            
            file.close()
            #Close the file
            
            fp = open('test.html', 'r')
            lines = fp.readlines()
            #open the file and read the lines 
            lines[2] = f"#ofselect: {whichFormVar['selectNum']}\n"
            lines[3] = f"#oftext: {whichFormVar['textNum']}\n"
            lines[4] = f"#ofdate: {whichFormVar['dateNum']}\n"
            lines[5] = f"#ofmc: {whichFormVar['mcNum']}\n"
            #overwrite the lines with new information
            fp = open('test.html', 'w')
            #open file in write mode
            fp.writelines(lines)
            fp.close()
            #write lines and close file. 
    fileoutput.close()
    
if __name__ == "__main__":
    form_builder()  # Calling the main function to start the builder


            


            
                
            
                
                
            
            
            
            