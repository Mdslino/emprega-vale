# Import all the models, so that Base has them before being
# imported by Alembic
from emprega_vale.db.base_class import Base
from emprega_vale.models.group import Group
from emprega_vale.models.auth import User

__all__ = ['Group', 'User', 'Base']
