Feature: Vignani ELE OrgAdmin setupaccount 
            
    Background:		
        given I am on the Vignani orgadmin setupaccount 

    Scenario Outline: Perform Successful orgadmin setupaccount and  Add managers
        when I  enter "<Password>" and enter "<Confrimpassword>" in respective fields and click complete button
        when I navigate to the managers in the navigation Bar
        when I click Add manager button
        when I enter"<ManagerName>",enter"<Email>" and enter"<Phonenumber>" in the respective fields
        then I click save button and displays an created Successful message

       Examples:
       |Password|Confrimpassword|ManagerName|Email|Phonenumber|
       |<Password>|<Confrimpassword>|<ManagerName>|<Email>|<Phonenumber>|






