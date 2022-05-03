# ClimbUp

Repo for PDX Code guild captstone

## Overview
------

ClimbUp will be a social media app focusing on sharing climbing information, scheduling meet ups and general social media features, posting, liking, etc

### Technologies used

* Django 3.1
* VueJS 3.0
* Bootstrap v5.0

## Features
------

- User System
  - [x] User sign up form
  - [x] User log out
  - [ ] Update profile
  - [ ] Delete Profile
- Posts
  - [x] Create a post
  - [ ] Delete a post
  - [x] Mark themselves as going to another users post
- [x] Public homepage with posts from other users and the user
- [x] Profile home page with user's posts, photos, information

## Data Model
----
* City
  * name (charfield)
* Post
  * title (charfield)
  * text (textfield)
  * city (foreignkey to City)
  * author (foreignkey to User)
  * attendees (many-to-many with User)
  * post_image(imagefield)
  * created_date (datetimefield)
  * scheduled_date (datetimefield)
  * likes(manytomany to user)
* User (extends built-in user)
  * profile picture (ImageField)
  * city(foreignkey to City )

## Pages
-------
- Index
  - greeting
  - list of posts
    -likes on post
  - button for creating a new post
  - header
    - link to profile page
    - log-in link if not logged in
    - log-out link if logged in
- New Post
  - form with all the Post model fields
  - image field for uploading photos to posts 
  - city field
- Post Detail
  - edit post
  - delete post
    - stretch- comment on post
- Registration
  -user registration form using django forms
  -imagefield for profile picture
- Login
  - login form
  - welcome message displaying on main page after redirect
- Profile page
  - display users posts chronologically
  - fixed navbar at top displaying current page and current user
  - fixed sidenav with new post link, homepage link, notifications, logout
## Schedule
----
* Week 1
    * ~~create models for Posts~~
    * ~~create models for Users~~
    * ~~create index template and view~~
    * ~~show test posts in page~~
    * ~~add forms for new posts, photos & signup~~
    * ~~add profile homepage with own users posts~~
    * ~~added modal for adding new city~~
* Week 2
    * fix issues from week 1
    * add ability to sort by city in the homepage
      * use BT Icon for sort BTN which opens modal for filtering
    **strech
      * add following page to only see other climbers you follow
    * ~add ability to mark self on other user post~
    * ~begin styling for readability~
    * ~edit post~
    * ~delete post~
    * ~like other user posts~
    * public page with all posts in city of User 
* Week 3
    * Fix recurring issues from weeks 1/2
    * finish any styling on app


* TinyMCE editor for post text