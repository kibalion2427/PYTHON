#app.py is a dummy CRUD API with SQLite
#I use SQLAlchemy as an ORM for SQLite
#MarshMallow to Serialize and Deserialize json
#Flask as a framework to create the host the server for the API

You can access to these API methods with POSTMAN or SOAPUI

To set up this project follow these next steps:

1. Inside a terminal, get into the project path that you download and use these commands
    python      To open a python console
    >>from app import db
    >>db.create_all()

2. Run the server with the command
    python app.py
    
3. Open Postman or SOAPUI to use the methods GET, POST, PUT or DELETE and test this API


