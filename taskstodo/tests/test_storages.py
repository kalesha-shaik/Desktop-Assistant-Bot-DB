import pytest
from taskstodo.db.storage import JSONStorage
doc = {"student":{"name":"Ram"}}

def test_json(tempdir):
    storage = JSONStorage(tempdir)
    storage.write(doc)
    assert storage.read()==doc,"Did not write what was intended"
    storage.close()
