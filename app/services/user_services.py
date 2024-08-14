from app.models import User
from app.repositories import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def get_all(self) -> list[User]:
        users= self.repository.get_all()
        return list(users)
    
    def get_all_inicial(self, inicial) -> list[User]:
        users = self.repository.get_all()
        return [x for x in users if x.nombre[0].lower()==inicial.lower()]
    
    def get_by_id(self, id)-> User:
        return self.repository.get_by_id(id)

    def create(self, entity: User)-> User:
        return self.repository.create(entity)

    def update(self, id, User) -> User:
        return self.repository.update(id, User)

    def delete(self, id)->bool:
        return self.repository.delete(id)
    