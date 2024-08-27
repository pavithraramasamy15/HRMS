Feature: Vignani ELE Admin Login Screen		
            
    Background:		
        given I am on the Vignani page
    
    Scenario Outline: Successful Login and Add Questions 
        when I input "<Email>" and "<Password>"  and press the submit  button
        then I should be redirected to the Admin dashboard and the page title should be VignaniELE
        when I navigate to the Questions in the navigation Bar
        when I click Add Questions button
        when I select Discipline in dropdown, select subject in dropdown,select type ,select difficulty,enter "<Questions>" in textbox,enter "<optionA>",enter "<optionB>",enter "<optionC>",enter "<optionD>",select Answer in dropdown,select Weightage in dropdown
        when I click create button
        then the question created successfully with the message and "<question>" should be in questionslist
        when I select the question to changes  in  questions "<ques>"
        when I click the Actions icon to edit the question 
        when I click the edit option and edit the changes in questions
        then I click the Update button and see the  successfully updated questions pop up message



    



        Examples:
        |        Email                | Password      |  Questions  |  optionA  |  optionB  | optionC  |  optionD  |
        |       <email>               | <password>    | <Questions> |  <optionA> | <optionB> | <optionC> | <optionD> |


