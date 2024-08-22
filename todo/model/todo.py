class Todo:
    def __init__(self,code_id:int,title:str,description:str,) -> None:
        self.code_id:int = code_id
        self.title:str = title
        self.description:str = description
        self.completed:bool = False
        self.tags: list[str] = []
        
    def mark_completed(self):
        self.completed=True
    
    def add_tag(self, tag:str):
        if tag not in self.tags:
            self.tags.append(tag)
    
    def __str__(self) -> str:
        return {self.code_id} - {self.title}
    
class TodoBook:
    def __init__(self, todos:dict) -> None:
        self.todos: dict(int,Todo) = {}
    
    def add_todo(self,title:str,description:str) ->int:
        code_id = len(self.todos) + 1
        code_id= Todo(code_id:int, title:str, description:str)
        todos = {code_id:Todo}
        return code_id

    def pending_todos(self) -> list:Todo
    return [todo for todo in self.todos.values() if not todo.completed]
        