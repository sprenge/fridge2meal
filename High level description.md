# Abstract
The goal of the fridge2meal application is to get proposals of recipies based on left-over ingredients that you have at home.  The choices of recipies can be influenced by the user in the following way :
- The user can select a subset of cookbook from a database of cookbooks
- The user can list which ingredients are always present (like salt, peper, ...)
- The user can list which ingredients should be avoided for whatever reason
- The user can list body deficiencies like vitames, minerals.
- The user can indicate preferences like low calorie meals, preparation time, energy cost.

The application keeps tracks of selected meal and tries to contribute to a varied diet and the reduction of food waste.

# Application architecture
Fridge2meal is composed of the following components :
- An app that can be installed on a smart phone
- The frontend service
- The database backend
- The business logic service
- Database population via an excel sheet

Here is a short description of each component, more details will follow in this document.

## Smart phone app
The purpose of the app is the identify your left-over ingredients, select your target cookbooks and preferences and present recipe proposals to the app user.  It is mandatory to enter username, password and server (which identifies the frontend application) at least once, typically after the installation of the app on your smartphone.

The app itself is a rather dumb/brainless application.  The list of ingredients, proposal recipies and cookbooks is requested to the frontend application (running in the cloud).  Communication via the app and the frontend is via a so called rest API interface, captured in a openapi 3.0 specification.

## Frontend service
The frontend service is a piece of software that runs typically on a cloud server.  It mediates between the Smart phone app and the rest of the components.

## Backend database

The database consists of two parts :

* the cooking database contains all the cookbooks organised in tables (book, ingredients, recipes, ...)
* the user database storing all the preferences and choices (e.g. ingredients in the fridge) and also the user credentials.


## Business logic

The business logic will serve as the brain for the fridge2meal application.  It will create a recipe list based on the user input (preferences/list of ingredients/book selection) and the cooking database.

## Database population via an excel sheet

The database backend can be populated with data (ingredients, recipies, books, ...).  Another way to populate the database is via an excel sheet that is formatted according to strict rules.

# detailed architecture


## database backend

## cooking part

Entity - relationship diagram

![[Pasted image 20230110202434.png]]



