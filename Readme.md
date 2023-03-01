# Scraper API

## Description

This project scrapes Google Finance for stock data, then parses the data and stores it in a Relational Database (we're using MySQL).
We then hosts api endpoints with the relevant stock data through DB queries.

## Tech Stack

*	Backend: Python, FastAPI
	*	Libraries: SQLAlchemy, BeautifulSoup, Asyncio, Threading, Aiohttp

<br>

*	Frontend: JavaScript, React, CSS
	*	Libraries:	Axios

## Installation

`git clone https://github.com/ganton000/scraper_project.git`

*	Start up backend server:
	*	`cd backend`
	*	`pip install -r requirements.txt`
	*	`uvicorn main:app --reload --host localhost --port 8000`

*	Start up client-side server:
	*	`cd frontend`
	*	`npm install`
	*	`npm run start`


## Code Example

Show what the library does as concisely as possible.

## Tests

Describe and show how to run the tests with code examples.

## In Progress

*	Dockerize

*	Migrate to Cloud