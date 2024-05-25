from typing import List
from app.models import User
from app.repositories import UserRepository
from app.services import SecurityManager, WerkzeugSecurity

repository = UserRepository()

class UserService:
    """ Clase que se encarga de CRUD de usuarios """
    
    def __init__(self) -> None:
        # Inicializa el servicio de seguridad para el manejo de contraseñas
        self.__security = SecurityManager(WerkzeugSecurity())

    def save(self, user: User) -> User:
        # Genera un hash de la contraseña antes de guardar el usuario
        user.password = self.__security.generate_password(user.password)
        return repository.save(user)
    
    def update(self, user: User, id: int) -> User:
        # Actualiza la información de un usuario existente por su ID
        return repository.update(user, id)
    
    def delete(self, user: User) -> None:
        # Elimina un usuario de la base de datos
        repository.delete(user)
    
    def all(self) -> List[User]:
        # Devuelve una lista con todos los usuarios
        return repository.all()
    
    def find(self, id: int) -> User:
        # Encuentra un usuario por su ID
        return repository.find(id)
    
    def find_by_username(self, username: str) -> User:
        # Encuentra un usuario por su nombre de usuario
        return repository.find_by_username(username)
    
    def find_by_email(self, email: str) -> User:
        # Encuentra un usuario por su correo electrónico
        return repository.find_by_email(email)

    def check_auth(self, username: str, password: str) -> bool:
        # Verifica la autenticidad del usuario comprobando su contraseña
        user = self.find_by_username(username)
        if user is not None:
            return self.__security.check_password(user.password, password)
        else:
            return False
