_     _____ ____  ____ ___ _____
| |   | ____|  _ \|  _ \_ _|_   _|
| |   |  _| | | | | | | | |  | |
| |___| |___| |_| | |_| | |  | |
|_____|_____|____/|____/___| |_|
_________________________________
Written by Rameez Saiyid

The following django project tries to accomplish the following:

High level description:
You are required to make a small reddit-like site that uses Linkedin as it’s posts/links.
On reddit you can submit a link on the site and then others can come in and upvote/downvote the posts/links.
The submissions here are the logged in users’ Linkedin profile information, such that when a user logs in through Linkedin,
their profile information is displayed as a submission. Then other logged in users can come and upvote/downvote that submission.

Required Flow:
I will be mainly testing this flow:
0 - First page is basically just a sign in button. I shouldn’t be able to view any submissions if I’m not logged in.
1 - Sign in button will ask me to sign in through Linkedin (Linkedin OAuth).
2 - Once signed in I can see my profile and other profiles listed on top of each other, reddit style.
2.5 - The profile information just shows basic profile information, (First name, last name, headline, a way to click to go view
the profile on the linkedin page)
3 - I can upvote/downvote other submissions without any limitations (in reddit you can only upvote once, but I don’t expect that
from your code)
4 - If I refresh the page, the scores that are there stay there. This means that it should be stored in the database.

Other requirements:
1 - The backend must be coded in Python. Here you have two options, either you use Django or Flask (technically you can just
use sockets).
2 - It goes without saying but you must use the Linkedin API.
3 - You must include a README file in your submission telling me how to run the code.
4 - You can ask others for help all you want, but I will be asking you about your code in the interview after this one
(if you submit a working webapp). Failure to explain your code could result in a rejection.


The project is accomplished with the following layout:
The main url is: /score/
    This should display a page showing a sign in button, which once clicked will redirect the user to the LinkedIn
    authentication page, where they must sign in and accept my app's access to their profile.

    Upon clicking accept, the user is redirected to the site, which has obtained the authentication code from LinkedIn
    and has to use that to obtain the access token. The token will allow the app to get the user's data

    Once the access token is acquired, the app gets whatever fields it can about the user (profile name, profile url,
    display picture url, headline) through GET requests to the LinkedIn API and parses the returned JSON content into
    the database.

    This is done unless the user's id already exists in the database, otherwise the app just redirects to /score/main/
    which displays the scoreboard of users.

    /score/main/ will display a list of the 10 most recent users to have signed into the site.

    Next to each user is a score and respective upvote/downvote buttons. Clicking either of these buttons calls
    a url on the page like so: /user_id/upvote
    This calls a function in views.py to increment/decrement the score parameter of the respective user and redirects
    the user back to the /score/main/ page.

    Each user's name is a hyperlink to their public linked profile, if that field was not granted permission by the user,
    then the hyperlink takes the user to https://linkedin.com

    Each user's display picture from LinkedIn is also showed, if that field was not granted permission by the user,
    then the display picture is of a generic one.

Setup:
    The project uses no dependencies besides the included python and django packages.

    The virtualenvironment for the project is located in /ledditEnv/ as my versions of Python and Django are 2.7 and
    1.11.11, respectively.

    Once activated, just run the django server by:
        python manage.py runserver 8080

    and direct your browser to: localhost:8080/score/

    In case you need it, the superuser account is:
    User: admin
    Pass: admin123
    
