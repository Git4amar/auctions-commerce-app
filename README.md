# Auctions (A Full Stack Commerce Application)
### Developer: Amarpreet S. Bir, California, USA
### Video Demo:  [Auctions (length - 4:43)](https://youtu.be/HarK5nold6U)
### Technology Stack:
- Python3
- Django
- HTML
- CSS
- Bootstrap
- SQL

### Demo Setup Instructions:
Note: A small SQLite3 demo database has been intialized for demo purposes
1.  **Required**: [Download and Install](https://www.python.org/downloads/) Python 3.10 or up 
2.  [Git clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) the repository to your local machine
3. Change directory (cd) into the project folder with the following structure
    ```
    ├── README.md
    ├── auctions
    ├── commerce
    ├── db.sqlite3
    └── manage.py
    ```
    
4. Setup a virtual environment

        python3 -m venv .venv
        source .venv/bin/activate
5. Install Django (Python Framework)

        python3 -m pip install django
6. Start a local server as follows

        python3 manage.py runserver

7. Open the local server link in any web browser
    
    [http://localhost:8000/](http://localhost:8000/) or [http://127.0.0.1:8000/](http://localhost:8000/)
8. Register with any demo credentials and explore the application functionality.

### Key Functionalities:
- Homepage (default route) shows all the active listings. Click any listing to view its details.
- Navigate to categories in top menu bar to view categorized listings
- **User Registration and Login**
- Logged in users **can create new auction listings** (for free item images try [pixabay](https://pixabay.com/))
- Logged in users **can add/remove any active listing to their watchlist**. Navigate to watchlist in top menu bar to view it.
- Logged in users **can place a bid for an item** (Note: A successful bid must be larger than the starting bid, otherwise user will get a error message stating the same)
- Logged in users **can open/close their own listing items**. When a listing is closed the highest bidder will be notified in their account.
- Logged in users **can leave comments/replies on a listing**.
- Admins can login and create, delete, or edit a listing or comment.

    Run to create admin account:

        python3 manage.py createsuperuser

    Go to [http://localhost:8000/admin](http://localhost:8000/admin) and login as admin