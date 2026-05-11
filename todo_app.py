from typing import List, Any, Dict
import os
import json

DATA_FILE = "todos.json"

class Todo:
    
    def init(self, id: int, titulo: str, descricao: str = "") -> None:
        self.id = id
        self.titulo = titulo
        self.descricao = descricao

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "titulo": self.titulo, "descricao": self.descricao}
    
class TodoManager:

    def __init__(self, path: str = DATA_FILE) -> None:
        self.path = path
        self.todos: List[Todo] = []
        self._load()

    def _load(self) -> None:
        if os.path.exists(self.path):
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                # Reconstrói objetos Todo a partir dos dicionários armazenados
                self.todos = [Todo(**item) for item in data]
            except Exception:
                # Se o arquivo estiver corrompido ou ilegível, inicia vazio
                self.todos = []