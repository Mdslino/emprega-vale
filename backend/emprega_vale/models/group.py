from sqlalchemy import Column, String

from emprega_vale.db.base_class import Base


class Group(Base):
    name = Column(String(50), nullable=False)

    def __str__(self):
        return f'Group(id={self.id}, name={self.name})'
