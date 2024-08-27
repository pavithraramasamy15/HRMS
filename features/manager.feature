Feature: Vignani ELE Manager setupaccount 
            
    Background:		
        given I am on the Vignani Manager setupaccount 
        
    Scenario Outline: Perform Successful manager setupaccount and  Add candidates
        when I enter values in "<Password>" and enter values in "<Confrimpassword>" in respective fields and then click complete button
        when I navigate to the candidates in the navigation Bar
        when I click Add candidate  button
        when I select Discipline from dropdown values,enter "<CandidateName>",enter "<Email>",enter "<Contactnumber>",select jobid from dropdownvalues,and select groupid from dropdown values
        then I clicking the save button and displays an created candidate Successful message
        when I click the assign in the navigation Bar
        then I select jobid in dropdown values,view users under jobid,select packages,view carts
        then I click save button and displays an success message  assign packages to the candidate

        Examples:
        |Password|Confrimpassword|CandidateName|Email|Contactnumber|
        |<Password>|<Confrimpassword>|<CandidateName>|<Email>|<Contactnumber>|
