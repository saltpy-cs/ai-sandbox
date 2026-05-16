Feature: View People
    As a user
    I want to see the list of passengers on the titanic in the UI
    so that I can know who was on board

    @AIS-1
    Scenario: Read all users via API
        Given the titanic API is running on localhost:5000
        When I send an API request to http://localhost:5000/api/1/passenger
        Then I get a list of the 887 passengers on the titanic when it sank

    @AIS-2
    Scenario: Read a single passenger using its id
        Given the titanic API is running on localhost:5000
        When I send an API request to http://localhost:5000/api/1/passenger/1
        Then I get the information about the passenger with id 1

    @AIS-2
    Scenario: Request a passenger that does not exist
        Given the titanic API is running on localhost:5000
        When I send an API request to http://localhost:5000/api/1/passenger/99999
        Then I get a 404 response
