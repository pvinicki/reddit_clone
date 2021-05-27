# REDDIT CLONE

## SUMMARY
Web application made with python and django. Clones the popular site "Reddit". Implements user login/registration, posts, comments and upvotes/downvotes.


## BUILDING THE PROJECT
Running the project requires python and django installed on your machine. Most linux distributions come with python preinstalled.

```
sudo pip install --upgrade pip
pip install django
yum upgrade
```

After installing django navigate to the "mysite" folder and do:
```
python manage.py runserver
```

You should see this output on the commandline:
```
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

May 27, 2021 - 15:50:53
Django version 3.2, using settings 'mysite.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Now copy and paste the development server URL (http://127.0.0.1:8000/) into your browser to access the site
