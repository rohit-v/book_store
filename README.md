Yello Books
==========
#### Objective 
Your assignment is to implement a bookstore REST API. 

#### Brief 
Jane, an avid reader from Chicago, has a great idea. She wants to build a marketplace that allows her and her friends to self-publish their adventures and sell them online to other readers. The profits would then be collected and donated to purchase medical supplies for charity. 
Tasks 
• Implement assignment using: 
- Language: Your choice 
- Framework: Your choice Implement a REST API returning JSON or XML based on the Content-Type 
header 
- Implement a custom user model with a "author pseudonym" field 
Implement a book model. Each book should have a title, description, author (your custom user model), cover image and price 
- Choose the data type for each field that makes the most sense 
- Implement REST endpoints for the books resource 
- No authentication required O Allows only GET (List/Detail) operations 
- Make the List resource searchable with query parameters 
- Provide REST resources for the authenticated user 
- Implement the typical CRUD operations for this resource 
- Implement an endpoint to unpublish a book (DELETE) 
- Demonstrate all the endpoints work 
### Bonus: 
- Provide an endpoint to authenticate with the API using username, password and 
return a JWT 
- Make sure the user “Anonymous” is unable to publish their work on Yello Books 

#### Prerequisites
- Python 3.7
- pip

#### Setup
```
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Visit the running application at http://127.0.0.1:8000/api on POSTMAN to get started.

#### Testing
```
Wiki link for endpoints and screenshots with responses.
```
https://github.com/rohit-v/book_store/wiki/List-of-endpoints-and-working

#### Third-Party Documentation
- https://docs.djangoproject.com/en/3.0/
