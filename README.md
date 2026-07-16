# Smart-campus-Guide-System-SCGS-

🗺️ MUST Smart Campus Guide System (MSCGS)
�
�
Load image
Load image
A digital campus navigation and information system for Mbeya University of Science and
Technology (MUST). MSCGS helps students, staff, and visitors find campus locations quickly
through an interactive map, location search, detailed place information, and walking directions.
In one sentence: MSCGS is a "Google Maps for MUST campus" — type a place name, see what it
is, where it is, and how to walk there.
Repository: github.com/mtundudev/mscgs
License: MIT
Table of Contents
Project Overview
Problem Statement
Objectives
System Users & Roles
Core Features (Version 1)
Technology Stack
Database Design
Entity Relationship Overview
Project Structure
Getting Started
Environment Variables
API Documentation
Branching & Collaboration Workflow
Development Roadmap
Non-Functional Requirements
Contributing
Glossary
Status & Next Steps
License
Project Overview
Every semester, new students, staff, and visitors struggle to find their way around MUST —
lecture rooms, laboratories, and offices are hard to locate without local knowledge. MSCGS
solves this with a central, always-up-to-date digital guide: open the app, search for a place,
and get clear directions to it.
Problem Statement
New students often struggle to identify the location of key facilities on campus.
Students waste valuable time searching for lecture rooms, laboratories, and offices.
Visitors are frequently unaware of where to go to access specific services.
There is no single, easy-to-use system that guides users to the correct location.
Example: A first-year student is looking for the Computer Engineering Laboratory but has
no way of knowing where it is located on campus.
Objectives
Main objective: design and develop a system that enables students and visitors to locate
places within MUST easily, accurately, and quickly.
Specific objectives — the system shall:
Display an interactive map of the campus
Allow users to search for a specific location
Provide detailed information about each building or office
Provide directions from one point to another within campus
Help new students familiarize themselves with the campus environment
System Users & Roles
Role
Capabilities
Student
Search locations, view the map, get directions, view office/facility info
Administrator
Add, update, and delete locations; manage categories and feedback
Visitor
View key campus locations and public info without an account
Core Features (Version 1)
A. Campus Map
Interactive map with building markers, including: Main Gate, Library, ICT Building,
Engineering Block, Administration Block.
B. Location Search
Code
C. Location Details
Each location record includes: Name, Category, Description, Photo,
Coordinates (latitude, longitude), Working hours.
D. Navigation
Code
Technology Stack
Layer
Technology
Backend
FastAPI, PostgreSQL, SQLAlchemy, Alembic, JWT Authentication
Frontend (Option 1)
React (web)
Frontend (Option 2)
Flutter (mobile — Android & iOS)
Map
OpenStreetMap data + Leaflet.js
Infrastructure
Docker, Docker Compose
Database Design
users
Field
Type / Notes
id
Primary key, integer
name
String
email
String, unique
password
String (hashed)
role
Enum — student / administrator / visitor
locations
Field
Type / Notes
id
Primary key, integer
name
String
category
Foreign key → categories.id
description
Text
latitude
Float
longitude
Float
image
String (path or URL)
categories
Field
Type / Notes
id
Primary key, integer
name
String — e.g. Office, Laboratory, Lecture Hall, Accommodation
feedback
Field
Type / Notes
id
Primary key, integer
user_id
Foreign key → users.id
location_id
Foreign key → locations.id
message
Text
rating
Integer
Entity Relationship Overview
Code
One category groups many locations. One location can receive many feedback entries. Each
feedback entry belongs to exactly one user.
Project Structure
Code
Getting Started
Clone the repo:
Bash
Copy the environment template and fill in your own values:
Bash
Start the stack with Docker:
Bash
Open the interactive API docs (Swagger UI):
Code
Environment Variables
Variable
Description
DATABASE_URL
PostgreSQL connection string
SECRET_KEY
Secret used to sign JWT tokens
ACCESS_TOKEN_EXPIRE_MINUTES
JWT token lifetime
ALGORITHM
JWT signing algorithm (e.g. HS256)
See .env.example for a ready-to-copy template. Never commit a real .env file.
API Documentation
FastAPI auto-generates interactive documentation once the app is running:
Swagger UI: /docs
ReDoc: /redoc
Branching & Collaboration Workflow
main — always stable, deployable code only. No direct commits.
dev — integration branch where finished features land before main.
feature/<short-name> — one branch per feature or task, branched from dev.
Workflow for each task:
git checkout dev && git pull
git checkout -b feature/your-feature-name
Commit small, focused changes with clear messages.
Push your branch and open a Pull Request into dev.
At least one collaborator reviews before merging.
Development Roadmap
Phase
Deliverables
Phase 1
Database design, FastAPI project setup, Location CRUD API
Phase 2
Map integration, search system
Phase 3
Navigation feature, mobile application
Non-Functional Requirements
Performance: search results return in under 1 second on normal campus connectivity
Usability: a first-time user can find a location with no training
Availability: accessible during all university operating hours
Security: only authenticated Administrators can create/edit/delete locations; passwords are hashed, never stored in plain text
Scalability: schema supports future growth without redesign
Maintainability: clear layered structure (models → schemas → services → routers)
Contributing
See CONTRIBUTING.md for branch naming, commit conventions, and the
Pull Request checklist.
Glossary
Term
Meaning
API
Application Programming Interface — how the frontend talks to the backend
CRUD
Create, Read, Update, Delete
ORM
Object-Relational Mapper — database tables as code objects
JWT
JSON Web Token — secure identity token after login
ERD
Entity Relationship Diagram
Endpoint
A specific URL the app calls to perform an action
Coordinates
Latitude/longitude pinpointing an exact spot
Schema
The structure/shape of stored data
Status & Next Steps
Current stage: database design and FastAPI project scaffold complete.
Next steps:
[ ] Draw the full ERD with cardinality notation
[ ] Implement SQLAlchemy models for locations, categories, users, feedback
[ ] Build Location CRUD API endpoints
[ ] Integrate map + search (Phase 2)
[ ] Add navigation + mobile app (Phase 3)
Full project documentation (problem statement, use-case walkthrough, and detailed
specifications) is available in docs/MSCGS_Project_Documentation.pdf.
License
This project is licensed under the MIT License — free to use, modify, and
distribute, provided the original copyright notice is retained.
