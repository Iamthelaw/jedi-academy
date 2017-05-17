# "Human" Resource service for Jedi Order

[Try on Heroku](https://jedi-academy.herokuapp.com)

## About
This system should do such things as:
- Searching and saving info about candidates on a planets
- Selecting candidates to be padawans by theyr exams
- Notification succeded candidates via intergalactic email service

## Models
- Candidate
    - name
    - planet
    - age
    - email
- Jedi
    - name
    - planet
- Planet
    - name
- Exam
    - unique Order code
    - list of questions

> Jedi, Planet & Exam can be added throught admin

## Pages
- Index (Contains two buttons 'for jedi' & 'for candidate')
- Canidate pages
    - Page for saving new candidate
    - Page where candidate takes quiz
    - Success page after completing quiz
    - Candidate detail info page
- Jedi pages
    - List of all jedi with padawans counter
    - Jedi who have at least 1 padawan listing
    - Form for selecting current jedi
