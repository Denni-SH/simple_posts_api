DATA_SUPERADMIN_INPUT = {
    'username': 'admin', 'email': 'admin@admin.com', 'password': 'admin123',
}
DATA_POST_INPUT = {
    "title": "First post", "text": "Hello world!"
}
DATA_POST_OUTPUT = {
    'id': 1,
    'title': 'First post',
    'text': 'Hello world!',
    'likes': 0,
    'author': 1,
}

DATA_POSTS = [
    {
        "title": "First post", "text": "Hello world!"
    },
    {
        "title": "Second post", "text": "Hello world2!"
    },
    {
        "title": "Third post", "text": "Hello world3!"
    },
]

DATA_POST_WITHOUT_TITLE = {
    "text": "Hello world!"
}

DATA_POST_GET_INPUT = {"pk": 1}
DATA_POST_GET_OUTPUT = {
    'id': 1,
    'title': 'First post',
    'text': 'Hello world!',
    'likes': 0,
    'author': 1,
}
DATA_POST_UPDATE_INPUT = {
    "title": "Changed title!"
}
DATA_POST_UPDATE_OUTPUT = {
    'id': 1,
    'title': 'Changed title!',
    'text': 'Hello world!',
    'likes': 0,
    'author': 1,
}

DATA_POST_LIST = {
    "count": 3,
    "next": None,
    "previous": None,
    "results": [
        {
            "id": 1,
            "title": "First post",
            "text": "Hello world!",
            "likes": 0,
            "author": 1,
        },
        {
            "id": 2,
            "title": "Second post",
            "text": "Hello world2!",
            "likes": 0,
            "author": 1,
        },
        {
            "id": 3,
            "title": "Third post",
            "text": "Hello world3!",
            "likes": 0,
            "author": 1,
        },
    ],
}
