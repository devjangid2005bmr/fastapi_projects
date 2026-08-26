from datetime import datetime, timedelta, timezone

import jwt
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


app = FastAPI()


# =========================================================
# 1. JWT CONFIGURATION
# =========================================================

SECRET_KEY = "my-super-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


# =========================================================
# 2. OAUTH2 SCHEME
# =========================================================

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="login"
)


# =========================================================
# 3. FAKE USER
# =========================================================

fake_user = {
    "username": "dev",
    "password": "1234"
}


# =========================================================
# 4. CREATE JWT
# =========================================================

def create_access_token(username: str):

    expire = datetime.now(timezone.utc) + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": username,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# =========================================================
# 5. LOGIN
# =========================================================

@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):

    if (
        form_data.username != fake_user["username"]
        or form_data.password != fake_user["password"]
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        form_data.username
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


# =========================================================
# 6. GET CURRENT USER
# =========================================================

def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except jwt.InvalidTokenError:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )


# =========================================================
# 7. PROTECTED ROUTE
# =========================================================

@app.get("/profile")
def profile(
    current_user: str = Depends(get_current_user)
):

    return {
        "message": "You are authenticated!",
        "username": current_user
    }