Feature: Confirming that the tip calculator form displays

    Scenario: check that the form displays
        When I go to the tip calculator
        Then I should see the calculator form

    Scenario: check that the form submits successfully
        When I go to the tip calculator
        And I submit the form with a valid total and tip percentage
        Then I should see the results page

    Scenerio: check that person gets the correct tip
        When I enter $50 and a 20% tip
        Then I should see $10 on the result page

    Scenerio: check that a person doesn't enter a non-valid value for meal
        When I enter non-valid number
        Then I should see an error

    Scenerio: check that a person doesn't enter a non-valid value for tip
        When I enter a non-valid number
        Then I should see an error
        
