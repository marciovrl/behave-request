#language:en

@getPosts @posts
Feature: Get in Posts

    Background: Use endpoint posts
        Given use endpoint posts

    Scenario: Get item Post
        When I want to read the posts
        Then I get all items registered posts

    @not_implemented
    Scenario: Get id item Post
        When I want to read the item "id" in Posts
        Then I only get item information "id" in registered posts