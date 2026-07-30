from datetime import datetime, UTC, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from jose import JWTError, jwt

from passlib.context import CryptContext

# ==============================
# JWT Configuration
# ==============================

SECRET_KEY = "CHANGE_THIS_TO_A_LONG_RANDOM_SECRET"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 60

# ==============================
# Password Hashing
# ==============================

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


# ==============================
# Password Functions
# ==============================

def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(
    plain_password: str,
    hashed_password: str,
) -> bool:
    return pwd_context.verify(
        plain_password,
        hashed_password,
    )


# ==============================
# JWT Creation
# ==============================

def create_access_token(data: dict):

    payload = data.copy()

    expire = datetime.now(UTC) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload.update({"exp": expire})

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM,
    )

    return token


# ==============================
# JWT Validation
# ==============================

def get_current_user(
    token: str = Depends(oauth2_scheme),
):

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
    )

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM],
        )

        username = payload.get("sub")

        role = payload.get("role")

        if username is None:
            raise credentials_exception

        return {
            "sub": username,
            "role": role,
        }

    except JWTError:
        raise credentials_exception


# ==============================
# RBAC
# ==============================

def admin_required(
    current_user=Depends(get_current_user),
):

    if current_user["role"] != "admin":

        raise HTTPException(
            status_code=403,
            detail="Admin access required",
        )

    return current_user