Feature: Press Execute button
    Execute order to comprobate that execute
    As a user
    I want to count the words in the textfield

    Scenario: Sentence "Hello World"
        Given the sentence "Hello World"
        When I press in button execute
        Then I see the counter of words with "[(1, u'world'), (1, u'hello')]"
        And I see the textfield in blank

    Scenario: Sentence "Hello Hello Hello"
        Given the sentence "Hello Hello Hello"
        When I press in button execute
        Then I see the counter of words with "[(3, u'hello')]"
        And I see the textfield in blank

    Scenario: Sentence "Hello Hello Hello World"
        Given the sentence "Hello Hello Hello"
        When I press in button execute
        Then I see the counter of words with "[(3, u'hello'), (1, u'world')]"
	And I see the textfield in blank

    Scenario: Sentence "House Ta454ble chair CHAIr"
        Given the sentence "Hello Hello Hello"
        When I press in button execute
        Then I see the counter of words with "[(2, u'chair'), (1, u'house')]"
	And I see the textfield in blank

    Scenario: Sentence "cAt ?* table Tree TREE 1234 duC?^^K"
        Given the sentence "Hello Hello Hello"
        When I press in button execute
        Then I see the counter of words with "[(2, u'tree'), (1, u'table'), (1, u'duck'), (1, u'cat')]"
	And I see the textfield in blank
