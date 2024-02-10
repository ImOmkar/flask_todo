> create virutal environment
> activate virtual environment
> go to root directory - flask_todo.
> run pip install -m requirements.txt to install packages from that txt file.

<!-- skip, if you already know. -->
> install sqlite or sqlite viewer extension in vscode to see the db tables
> delete and re create db if you want.
    > run python command in terminal inside root directory - (flask_todo) not the project directory (flask_todo) and enter below lines
    > from flask_todo import app, db
    > app.app_context().push() #this will create emtpy instance folder in root
    > db.create_all() #this will add site.db file inside instance folder
    > if you want to delete all the tables from db, enter below command.
    > db.drop_all()
<!-- skip, if you already know. -->

>  inside root directory, run python run.py to start the server


# project structure
- flask_todo > - root directory
    - flask_todo > - project directory
        - templates >
            - base.html
            - home.html
            - todos.html
            - create.html
            - update.html
        - __init__.py
        - forms.py
        - models.py
        - routes.py
    - instance >
        - site.db
    - run.py



