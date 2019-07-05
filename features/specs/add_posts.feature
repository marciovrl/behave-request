#language:en 

@postPosts
Feature: Add item Post

    Background: Use endpoint posts
        Given use endpoint posts
        
    Scenario: Add item Post
        When add item Post
        Then I see inserted item