
## Run Project
* To run the project go to the project root folder if the databse file is empty.
* run: python run_migrate_command.py command on the project root folder, import it to your 
* sql lite DB and run: python run_migrate_command.py command the second time to create database
* table and migrate the whole json files data to the database.
* to run server,run: uvicorn planning_app.main:app --reload in the project root folder

## Coding Style And Approach
* FIRST METHOD :
*  was the naive approach, it worked well and the endpoints was similar to 
* the data records given but it has some draw backs like: the project being so tightly 
* coupled being inter dependent,  individual isRequired and Optional skills which is supposed 
* to be only eleven instead appearing multple time in the database causing redundancy and 
* Normaization error.
* SECOND METHOD:
* Is the Dynamic loosely coupled approch, what I did first was to write a 
* code that separate the Plannning.json file into three tables, Planning table, PlanSkills, and Skill
* mapping them to their respective ID's. and having them into three different json files.
* then I used dynamic method to import and read the three json files and map them to their individual 
* database tables.
* BENEFITS: 
* It eleminated redundancy 
* Made the project loosely coupled and dyanimic


## Improvement 
   Beacuse of time I was unable to add configure docker-compose and pylint for the development enviroment

# Backend Coding Challenge

At aspaara a squad of superheroes works on giving superpowers to planning teams.
Through our product dashboard, we give insights into data – a true super-vision
superpower. Join forces with us and build a dashboard of the future!

![aspaara superhero](aspaara_superhero.png)

## Goal

Create a simple backend application that provides an API for a dashboard which
allows a planner to get insights into client and planning information.

You will find the corresponding data that needs to be imported into the database
in `planning.json`, which contains around 10k records.

## Requirements

1. Create proper database tables that can fit the data model.
2. Create a script that imports the data into the database (sqlite).
3. Create REST APIs to get the planning data from the database.
    1. The APIs don't need to be complete, just create what you can in the
       available time.
    2. Please include at least one example on how to do each of the following:
        1. pagination
        2. sorting
        3. filtering / searching

## Data Model

* ID: integer (unique, required)
* Original ID: string (unique, required)
* Talent ID: string (optional)
* Talent Name: string (optional)
* Talent Grade: string (optional)
* Booking Grade: string (optional)
* Operating Unit: string (required)
* Office City: string (optional)
* Office Postal Code: string (required)
* Job Manager Name: string (optional)
* Job Manager ID: string (optional)
* Total Hours: float (required)
* Start Date: datetime (required)
* End Date: datetime (required)
* Client Name: string (optional)
* Client ID: string (required)
* Industry: string (optional)
* Required Skills: array of key-value pair (optional)
* Optional Skills: array of key-value pair (optional)
* Is Unassigned: boolean

## Preferred Tech Stack

* Python 3.8+
* FastAPI
* SQLAlchemy

## Submission

* Please fork the project, commit and push your implementation and add
  `sundara.amancharla@aspaara.com` as a contributor.
* Please update the README with any additional details or steps that are
  required to run your implementation.
* We understand that there is a limited amount of time, so it does not have to
  be perfect or 100% finished. Plan to spend no more than 2-3 hours on it.

For any additional questions on the task please feel free to email
`sundara.amancharla@aspaara.com`.


* 
