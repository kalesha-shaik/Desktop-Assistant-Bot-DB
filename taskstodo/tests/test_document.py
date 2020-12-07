import pytest
from taskstodo.db import Document

def test_document():
    d={'name':'Ram'}
    doc =Document(1,d)

    assert doc.id == 1
    assert doc.name == 'Ram'
