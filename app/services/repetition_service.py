from typing import List
from app.models import Repetition
from app.repositories import RepetitionRepository

repository = RepetitionRepository()

class RepetitionService:
    """ Clase que se encarga de CRUD de repetitions """
    
    def save(self, repetition: Repetition) -> Repetition:
        # Guarda una nueva repetición en la base de datos
        return repository.save(repetition)
    
    def update(self, repetition: Repetition, id: int) -> Repetition:
        # Actualiza una repetición existente por su ID
        return repository.update(repetition, id)
    
    def delete(self, repetition: Repetition) -> None:
        # Elimina una repetición de la base de datos
        repository.delete(repetition)
    
    def all(self) -> List[Repetition]:
        # Devuelve una lista con todas las repeticiones
        return repository.all()
    
    def find(self, id: int) -> Repetition:
        # Encuentra una repetición por su ID
        return repository.find(id)
