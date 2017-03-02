from passlib.context import CryptContext

pwd_context = CryptContext(
    schemes=['bcrypt'],
    deprecated='auto'
)


def hash_password(pwd):
    return pwd_context.hash(pwd)


def check_password(pwd, hashed_pwd):
    return pwd_context.verify(pwd, hashed_pwd)

USERS = {
    'dummy': hash_password('123'),
    'admin': hash_password('admin'),
}

GROUPS = {'admin': ['group:admins']}


def group_finder(userid, request):
    if userid in USERS:
        return GROUPS.get(userid, [])
