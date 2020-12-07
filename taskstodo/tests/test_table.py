import pytest
from taskstodo.db import Table,Storage
from taskstodo.db.query import where
import threading
import time
from random import randint

def test_table_insert(jsonstorage):
    table = Table("test",jsonstorage)
    d={'name':'Ram','age':21}
    id = table.insert(d)
    assert id== '1'
    assert table.get(id) == d

def test_table_insert_multiple(jsonstorage):
    table = Table("test2",jsonstorage)
    d=[{'name':'Ram','age':21},{'name':'Mohan','age':18}]
    ids = table.insert_multiple(d)
    assert ids== ['1','2']
    assert table.get(ids[0]) == d[0]
    assert table.get(ids[1]) == d[1]

def test_search(jsonstorage):
    table = Table("test3",jsonstorage)
    d=[{'name':'Ram','age':21},{'name':'Mohan','age':18}]
    ids = table.insert_multiple(d)
    l=table.search(where('age')==21)
    assert len(l)==1
    assert l[0]==d[0]

    l=table.search((where('age')==21) | (where('age')==18))
    assert len(l)==2
    assert l[0]==d[0]
    assert l[1]==d[1]

def test_simultaneous(jsonstorage):

    def insert(table):
        x=randint(1,100)
        table.insert({'data':x})

    table = Table("test_sim",jsonstorage)
    try:
        l=[]
        for i in range(5):
            t=threading.Thread(target=insert,args=(table,) )
            l.append(t)
            t.start()

        for t in l:
            t.join()

        except:
            print("Error:unable to start thread")
    



