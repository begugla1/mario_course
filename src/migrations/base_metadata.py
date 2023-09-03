from sqlalchemy import MetaData

from api.database import Base
from api.auth.models import *


metadata: MetaData = Base.metadata
