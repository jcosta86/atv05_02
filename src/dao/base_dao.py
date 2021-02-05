from src.dao.session import Session
from src.models.base_model import BaseModel

class BaseDao:
    def __init__(self, type_model: BaseModel):
        self.__type_model = type_model

    def save(self, model: object) -> object:
        with Session() as session:
            session.add(model)
            session.commit()
            session.refresh(model)
            return model

    def read_all(self) -> list:
        with Session() as session:
            return session.query(self.__type_model).all()
            
    def read_by_id(self, id_: int) -> object:
        with Session() as session:
            return session.query(self.__type_model).filter_by(id_=id_).first()
    
    def delete(self, model) -> None:
        with Session() as session:
            session.delete(model)
            session.commit()