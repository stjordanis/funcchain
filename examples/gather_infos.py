from langchain.pydantic_v1 import BaseModel

from funcchain import chain


class Task(BaseModel):
    name: str
    description: str
    difficulty: str
    keywords: list[str]


def gather_infos(task_input: str) -> Task:
    """
    TASK_INPUT:
    {task_input}

    Based on this task input, gather all task infos.
    """
    return chain()


def main():
    task_input = input("\nEnter task input: ")

    task = gather_infos(task_input)

    print("\nTASK\n")
    print("NAME:", task.name)
    print("DESCRIPTION:", task.description)
    print("DIFFICULTY:", task.difficulty)
    print("KEYWORDS:", task.keywords)


if __name__ == "__main__":
    main()
