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
        return {"Id": self.id, "Título": self.titulo, "Descrição": self.descricao}
    
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
                self.todos = [Todo(**item) for item in data]
            except Exception:
                self.todos = []

    def _save(self) -> None:
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.todos], f, ensure_ascii=False, indent=2)

    def list_cards(self) -> List[Todo]:
        return self.todos

    def add_card(self, title: str, description: str = "") -> Todo:

        title = title.strip()
        if not title:
            raise ValueError("O Título não pode ser vazio")
        next_id = 1 + max((t.id for t in self.todos), default=0)
        todo = Todo(next_id, title, description.strip())
        self.todos.append(todo)
        self._save()
        return todo

    def delete_card(self, id: int) -> None:
        for i, t in enumerate(self.todos):
            if t.id == id:
                del self.todos[i]
                self._save()
                return
        raise ValueError(f"Não existe card com esse id:{id}")
