import pytest
from taskstodo.db import JSONStorage

@pytest.fixture
def tempdir():
    return r"C:\Users\RAASI\Desktop\week3Mlcopy2\taskstodo\temp.db"

@pytest.fixture
def jsonstorage():
    return JSONStorage(r"C:\Users\RAASI\Desktop\week3Mlcopy2\taskstodo\temp.db")