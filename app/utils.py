from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'],deprecated='True')


def hass_password(password:str):
    return pwd_context.hash(password)


def verfiy_passwords(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)