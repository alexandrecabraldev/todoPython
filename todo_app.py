from typing import Any, Dict


class Todo:
    
    def init(self, id: int, titulo: str, descricao: str = "") -> None:
        self.id = id
        self.titulo = titulo
        self.descricao = descricao

    def to_dict(self) -> Dict[str, Any]:
        return {"id": self.id, "titulo": self.titulo, "descricao": self.descricao}