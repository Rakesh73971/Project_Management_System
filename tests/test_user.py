from app import schemas
from app.config import settings
import jwt

def test_create_user(client):
    res = client.post(
        "/users/",
        json={
            'name': 'Rakesh',
            'email':'hello123@gmail.com',
            'password':'password123'
        }
    )
    print(res.json())  # Always print when debugging
    new_user = schemas.UserResponse(**res.json())
    assert new_user.email == 'hello123@gmail.com'


