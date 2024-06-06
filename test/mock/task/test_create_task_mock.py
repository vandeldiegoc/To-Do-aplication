import pytest

# Define el fixture


@pytest.fixture(
    scope="module",
    name="data_create_taskdto",
    params=[
        # Test case 1: create task DTO with all properties
        {
            "task_id": "ID_de_la_tarea",
            "name": "Nombre_de_la_tarea",
            "description": "Descripción_de_la_tarea",
            "deadline": False,
            "start_date": "2023-09-20T12:00:00Z",
            "finish_date": "2023-09-21T15:30:00Z",
            "status": "active",
            "tag": ["etiqueta1", "etiqueta2"],
        },
        # Test case 2: create task DTO without tag
        {
            "name": "Nombre_de_la_tarea",
            "description": "Descripción_de_la_tarea",
            "deadline": False,
            "start_date": "2023-09-20T12:00:00Z",
            "finish_date": "2023-09-21T15:30:00Z",
            "status": "active",
        },
    ],
    ids=["create task DTO with all properties", "create task DTO without tag"],
)
def create_task_dto_dic(request):
    return request.param
