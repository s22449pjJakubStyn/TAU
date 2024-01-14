Feature: Anime Page Dropdown Menu

  Scenario Outline: Verify dropdown menu and clicking specific anime result on Wbijam on <browser> browser
    Given I open the website "https://wbijam.pl" using "<browser>" browser
    When I click on accept cookies button
    And I hover specific dropdown menu
    And I click specific anime pannel
    Then I should be on the correct anime subpage

    Examples:
      | browser |
      | Chrome  |
      | Edge |