#language:en

@deletePosts @posts
Feature: Delete item Post

    Background: Use endpoint posts
        Given use endpoint posts

    @not_implemented
    Scenario: Delete item Post
        When delete item Post
        Then Item is deleted