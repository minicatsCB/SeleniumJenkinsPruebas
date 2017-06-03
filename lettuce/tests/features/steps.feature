Feature: Enter Text
    In order to enter text
    As a user
    I want to write one sentence

    Scenario: Sentence "Hello World"
        Given the textfield in blank
        When I enter the sentence "Hello World"
        Then I see "Hello World" in the textfield

    Scenario: Sentence "Hello Hello Hello Hello Hello"
        Given the textfield in blank
        When I enter the sentence "Hello Hello Hello"
        Then I see "Hello Hello Hello" in the textfield

    Scenario: Sentence "Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello"
        Given the textfield in blank
        When I enter the sentence "Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello"
        Then I see "Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hell" in the textfield