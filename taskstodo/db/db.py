from .table import Table
from .storage import Storage
class DB:
    def __init__(self,storage: Storage):
        """
        initialize a new database with appropriate storage 
        """
        self._storage=storage
        self._tables={}

    def table(self,name):
        """
        Get access to a specific named table
        Returns a table if it exists
        Creates a new table if it does not exist
        """
        if name in self._tables:
            return _tables[name]

        return Table(name,self._storage)

    def drop(self,name):
        if name in self._tables: 
           _tables[name].truncate()
           del _tables[name]

        else:
            raise ValueError(f"No such table {name}")
    
    def clean(self):
        self._storage.write({})
        self._tables.clear()
