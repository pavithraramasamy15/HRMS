Feature: Vignani ELE Admin Login Screen		
            
    Background:		
        Given I am on the Vignani login page		
            
    
    Scenario Outline: Perform Successful Login and  Add organization 
        Then I should able to see the login page elements for login page verification
        When I enter "<Email>" and "<Password>" in the respective fields and clicked on Signin button
        Then the login page should be redirected to the Trainee dashboard and I should see the title for the login page verification
        When I navigate to the organization in the navigation Bar
        When I click Add organization button
        When I Enter "<OrganizationName>", Select Domain in Dropdown values, Enter "<OrganizationAddress>", Enter "<EmailAddress>"
        Then I click the save button
        Then I click logout button

        
        
        

        Examples:
            |Email|Password|OrganizationName|OrganizationAddress|EmailAddress|
            |<email>|<password>|<Organization_Name>|<Organization_Address>|<Email_Address>|


    

        
        
        
    
        
       