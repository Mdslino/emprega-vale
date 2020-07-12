from typing import TYPE_CHECKING

from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy_utils import EmailType

from emprega_vale.db.base_class import Base

if TYPE_CHECKING:
    from .group import Group  # noqa: F401


class User(Base):
    email = Column(EmailType, nullable=False, unique=True, index=True)
    password = Column(String(1024), nullable=False)
    group_id = Column(Integer, ForeignKey('group.id'), nullable=False)
    group = relationship('Group', uselist=False, lazy='joined')

    def __str__(self):
        return f'User(id={self.id}, email={self.email}, group={self.group.name})'
