# Social Site API

This project provides a set of RESTful APIs for a social site where users can register, log in, post discussions with text and images, 
and interact with each other's posts through comments and likes. Users can also follow each other, and search for posts based on hashtags or text content.




## Features

User Registration and Login
User Management (Create, Update, Delete, List)
Discussion Management (Create, Update, Delete, List, Search by Tags and Text)
Follow System
Comment and Like System for Posts
View Count for Posts
Post Search using Hashtags


## Requirements

- Python 3.8+
- Django 3.2+
- Django REST framework


## Installation


1. Clone the repository:

- ```git clone <repository-url> ```
-  ``` cd <repository-directory> ```




2. Create and activate a virtual environment:

- ```python3 -m venv venv```
- ```source venv/bin/activate```  # On Windows use `venv\Scripts\activate`



3. Install the dependencies:

- ```pip install -r requirements.txt```



4. Apply migrations:

- ```python manage.py migrate```



5. Create a superuser:

- ```python manage.py createsuperuser```



6. Run the development server:

- ```python manage.py runserver```




## API Endpoints

### User Endpoints

 - Create User: POST /api/signup/
 - Login User: POST /api/login/
 - Update User: PUT /api/users/update_user/
 - Delete User: DELETE /api/users/delete_user/
 - List Users: GET /api/users/list_users/
 - Search User by Name: GET /api/users/get_user/?name=<name>


### Post Discussion Endpoints
 - Create Post Discussion: POST /api/posts/post_create/
 - Update Post Discussion: PUT /api/posts/update_post/
 - Delete Post Discussion: DELETE /api/posts/delete_post/
 - Get Post Discussions by Tag: GET /api/posts/posts_tag/?tag=<tag>
 - Get Post Discussions by Text: GET /api/posts/posts_text/?text=<text>




## Postman Requests
### 1. SignUp

 - POST /api/signup/
 - Content-Type: application/json
 - Request :
```json
{
    "email": "rahulsheoran@email.com",
    "name": "Rahul Sheoran",
    "mobile_no": "4444444444444",
    "password" : "RahulSheoran"
}
```

### 2. Login
 - POST /api/login/
 - Content-Type: application/json
 - Request : 
```json
{
    "email": "mohit@email.com",
    "password" : "MohitSheoran"
}
```
- Response : 
```json
{
    "user": {
        "id": 7,
        "name": "Mohit Beniwal",
        "mobile_no": "555555555",
        "email": "mohit@email.com",
        "created_on": "2024-06-12T15:03:18.564833Z",
        "updated_on": "2024-06-13T06:21:02.811229Z",
        "is_staff": true,
        "is_active": true,
        "is_superuser": true
    }
}
```

### 3. Update User

 - PUT /api/users/update_user/
 - Content-Type: application/json
 - Request :
```json
{
    "email": "rahulsheoran12@email.com",
    "new_mobile_no": "555555222",
    "mobile_no": "5555555551"
}
```
 - Response :
```json
{
    "message": "Successfully Updated",
    "user": {
        "id": 6,
        "name": "Rahul Kumar",
        "mobile_no": "555555222",
        "email": "rahulsheoran12@email.com",
        "created_on": "2024-06-12T14:59:41.105324Z",
        "updated_on": "2024-06-13T12:46:29.523498Z",
        "is_staff": false,
        "is_active": true,
        "is_superuser": true
    }
}
```

### 4. Delete User
 - DELETE /api/users/delete_user/
 - Content-Type: application/json
 - Request :
``` json
{
    "email": "mohit11@emailll.com",
    "mobile_no": "55333555555533"
}
```
- Response : 
```json
{
    "message": "Successfully Deleted"
}
```

### 5. List Users
- GET /api/users/list_users/
- Response : 
```json

[
    {
        "id": 1,
        "name": "Ankit",
        "mobile_no": "11111111",
        "email": "ankit@email.com",
        "created_on": "2024-06-12T14:51:32.929622Z",
        "updated_on": "2024-06-12T14:51:32.929660Z",
        "is_staff": true,
        "is_active": true,
        "is_superuser": true
    },
    {
        "id": 2,
        "name": "Ankit_kinha_4",
        "mobile_no": "1234567894",
        "email": "ankitkinha_5@example.com",
        "created_on": "2024-06-12T14:53:11.108685Z",
        "updated_on": "2024-06-12T14:53:11.108746Z",
        "is_staff": false,
        "is_active": true,
        "is_superuser": true
    }
]
```

### 6. Get User
- GET /api/users/get_user/?name=Rahul
- Response :
``` json
[
    {
        "id": 5,
        "name": "rahul",
        "mobile_no": "33333333",
        "email": "rahul@email.com",
        "created_on": "2024-06-12T14:58:13.025470Z",
        "updated_on": "2024-06-12T14:58:13.025537Z",
        "is_staff": false,
        "is_active": true,
        "is_superuser": true
    },
    {
        "id": 6,
        "name": "Rahul Kumar",
        "mobile_no": "5555555551",
        "email": "rahulsheoran12@email.com",
        "created_on": "2024-06-12T14:59:41.105324Z",
        "updated_on": "2024-06-12T16:30:38.803832Z",
        "is_staff": false,
        "is_active": true,
        "is_superuser": true
    }
]
```

### 7. Create Post 
- POST /api/posts/post_create/
- Request :
```json
{
    "user": 1,
    "text": "seventh post",
    "image": null
}
```
- Response :
```json
{
    "id": 7,
    "user": 1,
    "text": "seventh post",
    "image": null,
    "created_on": "2024-06-13T12:47:18.298468Z",
    "updated_on": "2024-06-13T12:47:18.298539Z",
    "view_count": 0
}
```

### 8. Update Post 
- PUT /api/posts/update_post/
- Request :
``` json
  {
    "post": 2,
    "text": "updated_text",
    "image": null
}
```
- Response :
```json
{
    "id": 2,
    "user": 1,
    "text": "updated_text",
    "image": null,
    "created_on": "2024-06-13T11:24:33.271978Z",
    "updated_on": "2024-06-13T12:40:04.878607Z",
    "view_count": 0
}
```

### 9. Delete Post
- DELETE /api/posts/delete_post/
- Request :

```json
{
    "post":1
}
```

- Response
```json
{
    "message": "Successfully Deleted"
}
```

### 10. Get Post By Tag
- GET /api/posts/posts_tag/?tag=tag1
- Response :

```json
[
    {
        "id": 2,
        "user": 1,
        "text": "updated_text",
        "image": null,
        "created_on": "2024-06-13T11:24:33.271978Z",
        "updated_on": "2024-06-13T12:40:04.878607Z",
        "view_count": 0
    }
]
```

### 11. Get Post By Text 
- GET /api/posts/posts_text/?text=new
- Response :
```json
[
    {
        "id": 6,
        "user": 1,
        "text": "six",
        "image": null,
        "created_on": "2024-06-13T11:53:47.482641Z",
        "updated_on": "2024-06-13T11:53:47.482688Z",
        "view_count": 0
    }
]
```



## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License
This project is licensed under the MIT License.




## 

This README provides an overview of the project's functionalities, installation instructions, and details on how to interact with the API endpoints. 
Adjust the repository URL and any specific details as needed.























































































