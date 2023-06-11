# Deployment

Back to Readme [here](README.md)

# Table Of Contents

- [ElephantSQL Database](#elephantsql-database)
- [AWS For Static Files and Images](#aws-for-static-files-and-images)
- [Fork Repository](#fork-repository)
- [Workspace](#workspace)
- [Heroku Deployment](#heroku-deployment)
- [Update Repository](#update-repository)

<br>

## ElephantSQL Database

1. Log in to ElephantSQL.com to access your dashboard
2. Click “Create New Instance”
3. Set up your plan
   - Give your plan a Name (this is commonly the name of the project)
   - Select the Tiny Turtle (Free) plan
   - You can leave the Tags field blank
4. Select “Select Region”
5. Select a data center near you <br>
   If you receive a message saying "Error: No cluster available in your-chosen-data-center yet", choose another region.
6. Then click “Review” and then “Create instance”.
7. Return to the ElephantSQL dashboard and click on the database instance name for this project.
8. In the URL section, click the copy icon to copy the database URL to add to Heroku Config Vars.

## AWS For Static Files and Images

1. Create an S3 bucket to store all static files and images by navigating to the S3 dashboard in the AWS console and clicking on the "Create bucket" button.
2. Configure the bucket's permissions to allow public access to the static files and images. This can be done by navigating to the bucket's permissions tab and adding a new policy that grants read access to everyone.
3. Install the boto3 and django-storages packages in the Django project.
4. Update the Django project's settings to use S3 as the storage backend for static files and images. Then use these to update the settings environment variables and the Heroku Config Vars.

## Fork Repository

1. Login to GitHub.
2. Access the [BitWise-DRF](https://github.com/Joe-Collins-1986/BitWise-DRF).
3. Click the Fork button at the top of the page.

## Workspace

1. Open your prefered workspace (Visual Studio Code, etc...).

Following instructions are for Visual Studio Code:

2.  Open the Command Palette and search Git Clone.
3.  Provide the URL of the copied BitWise-DRF repository.
4.  Choose a directory on your local computer where you want to clone the repository.
5.  cd into project file.
6.  Create a virtual environment with:

        python -m venv venv

7.  Activate the virtual env:

- For windows:

        venv\Scripts\activate

- For Mac: source

        venv/bin/activate

8.  Install the dependencies:

        pip install -r requirements.txt

9.  Create a .env.py file in the root directory of the project.
10. Add the following environment variables to the .env file:

        import os

        os.environ["DATABASE_URL"] = "ENTER ELEPHANTSQL URL"
        os.environ["SECRET_KEY"] = "GENERATE AND ADD A SECTRET KEY"

        os.environ["AWS_ACCESS_KEY_ID"] = "ENTER AWS KEY"
        os.environ["AWS_SECRET_ACCESS_KEY"] = "ENTER AWS ACCESS KEY"
        os.environ["AWS_STORAGE_BUCKET_NAME"] = "ENTER AWS BUCKET NAME"

**IMPORTANT:** Do not commit these changes yet.

11. Create a .gitignore file in the root directory of the project.
12. Add env.py to gitignore.
13. Add and commit changes.
14. Create a superuser:

        python manage.py createsuperuser

15. Migrate to Database:

        python manage.py makemigrations
        python manage.py migrate

16. Run server:

        python manage.py runserver

## Heroku Deployment

1. In the console enter pip3 freeze > requirements.txt to update the requirements.txt file with necessary modules used in the code.
2. Log in to [Heroku](https://id.heroku.com/login) and create an account.
3. Click 'Create new app' button.
4. Enter a unique name for your app and select your region then click 'Create app'.
5. Go the 'Settings' tab.
6. Click 'Reveal Config Vars'.
7. In the Config Vars enter:

   AWS Environment Variables:

   - AWS_ACCESS_KEY_ID = "ENTER AWS KEY"
   - AWS_SECRET_ACCESS_KEY = "ENTER AWS ACCESS KEY"
   - AWS_STORAGE_BUCKET_NAME = "ENTER AWS BUCKET NAME"

   <br>

   ElephantSQL Database Environment Variables:

   - DATABASE_URL = "ENTER ELEPHANTSQL URL"

   Other Environment Variables:

   <br>

   - ALLOWED_HOST = "HEROKU API HOST URL"
   - SECRET_KEY = "GENERATE AND ADD A SECTRET KEY"

   <br>

8. Go to the 'Deploy' tab.
9. Select 'GitHub' as the deployment method and click 'Connect to GitHub'.
10. Search for the GitHub Repository name and hit 'Connect'.
11. Click 'Automatic Deploys' to get Heroku to update automatically when GitPod changes are pushed to GitHub.
12. Click 'Deploy Branch' to launch the project to Heroku for the first time.
13. Click 'View' to go to live app.

## Update Repository

1. When adding a new feature create a separate branch to work in safely typing into the terminal "git branch 'name of required feature/update'".
2. Checkout the branch with "git checkout 'name of required feature/update'".
3. Make updates and test using "python manage.py runserver".
4. Once testing is complete add to Git staging area using "git add ."
5. Commit the changes and add a useful explanation of what action was done to track the history in GitHub using "git commit -m 'explanation of update'".
6. Once the feature is complete, fully tested, and ready to be added to the main branch first go to the main branch using "git checkout main".
7. Merge the feature branch into the main using "git merge 'name of required feature/update'".
8. Confirm merge was successful and then if it is not going to be re-used delete the feature branch using "git branch -d 'name of required feature/update'". (If deleting a branch with commits not merged to main delete with -D instead of -d)
9. Use "git push" to push the commits to GitHub. These will then appear in the live website if Heroku is set to automatic deplyment and linked to my Github.
