import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from typing import Annotated
from annotated_types import MinLen, MaxLen

from pydantic import BaseModel, EmailStr

class CreateUser(BaseModel):
    username: Annotated[str, MinLen(3), MaxLen(20)]
    email: EmailStr