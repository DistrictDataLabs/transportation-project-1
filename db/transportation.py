from sqlalchemy import create_engine
from resources import dbs
dbd='mysql'
tdb=dbs[dbd]
engine=create_engine('%s://%s:%s@%s:%s/%s' % \
                     (dbd
                      , tdb['user'], tdb['pw']
                     ,tdb['host'],tdb['port']
                     ,tdb['db'] ))
#conn=engine.connect()
from sqlalchemy.engine.reflection import Inspector
insp=Inspector(engine)#(conn)
from sqlalchemy import MetaData
md=MetaData(engine);md.reflect()

def get_table_info(tbl_nm):
    """returns a dict with keys 'attrib' for each col"""
    for ti in insp.get_columns(tbl_nm):
        yield ti

from sqlalchemy.sql import and_,select
from sqlalchemy import Table
flights=md.tables['flights']


def select_flights(origin,dest,analysis_columns
                   ,whereclause=[]):
    """mixNmatch strings with sqlalchemy objs in the args"""
    return flights.select(analysis_columns\
      ,and_(flights.c.ORIGIN==origin,flights.c.DEST==dest
            ,*whereclause))



# def sql_dec(func_returning_sqlable):
#     """takes in a sqlalchemy statement obj and gives a sql str"""
#     def sqlw(*args,**kwargs):
#         return str(literalquery(func_returning_sqlable(*args,**kwargs)))
#     return sqlw
#>>to sql.py
#sql_dec(select_flights) instend of the following
# def select_flights_sql(*args,**kwargs):
#     return str(literalquery(select_flights(*args,**kwargs)))


from datetime import datetime
from decimal import Decimal
#http://stackoverflow.com/questions/5631078/sqlalchemy-print-the-actual-query
def literalquery(statement, dialect=None):
    """Generate an SQL expression string with bound parameters rendered inline
    for the given SQLAlchemy statement.

    WARNING: This method of escaping is insecure, incomplete, and for debugging
    purposes only. Executing SQL statements with inline-rendered user values is
    extremely insecure.
    """
    import sqlalchemy.orm
    if isinstance(statement, sqlalchemy.orm.Query):
        if dialect is None:
            dialect = statement.session.get_bind(
                statement._mapper_zero_or_none()
            ).dialect
        statement = statement.statement
    if dialect is None:
        dialect = getattr(statement.bind, 'dialect', None)
    if dialect is None:
        from sqlalchemy.dialects import mysql
        dialect = mysql.dialect()

    Compiler = type(statement._compiler(dialect))

    class LiteralCompiler(Compiler):
        visit_bindparam = Compiler.render_literal_bindparam

        def render_literal_value(self, value, type_):
            if isinstance(value, (Decimal, long)):
                return str(value)
            elif isinstance(value, datetime):
                return repr(str(value))
            else:  # fallback
                value = super(LiteralCompiler, self).render_literal_value(
                    value, type_,
                )
                if isinstance(value, unicode):
                    return value.encode('UTF-8')
                else:
                    return value

    return LiteralCompiler(dialect, statement)
