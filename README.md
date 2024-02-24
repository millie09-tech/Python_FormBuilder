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
