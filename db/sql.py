

def sql_dec(func_returning_sqlable):
    """takes in a sqlalchemy statement obj and gives a sql str"""
    def sqlw(*args,**kwargs):
        return str(literalquery(func_returning_sqlable(*args,**kwargs)))
    return sqlw
