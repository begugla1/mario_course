from sqlalchemy import MetaData

from database import Base
from api.auth.models import *


metadata: MetaData = Base.metadata
