#language:en

@post
Feature: Endpoint Post


    Background: Use endpoint posts
        Given use endpoint "/posts/"
        
        Scenario: Get item Post
            When I want to read the posts
            Then I get the code "200"

        @not_implemented
        Scenario: Get id item Post
            When I want to read the item "id" in Posts
            Then I get the code "200"
        
        Scenario: Add item Post
            When add item Post
            Then I get the code "201"

        @not_implemented
        Scenario: Delete item Post
            When delete item Post
            Then I get the code "200"