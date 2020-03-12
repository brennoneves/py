import pyodbc
class Conexao(object):
    _db=None    
    def __init__(self, connect):
        self._db = pyodbc.connect(connect)
    def manipular(self, sql):
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except:
            return False
        return True
    def consultar(self, sql):
        rs=None
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            rs=cur.fetchall()
        except:
            return None
        return rs
def proximaPK(self, tabela, chave):
    sql='select max('+chave+') from '+tabela
    rs = self.consultar(sql)
    pk = rs[0][0]  
    return pk+1
def fechar(self):
    self._db.close()

'''
server =".\SQLEXPRESS"
database ="STAGE_AREA"
username ="SA"
password ="ERPM"
string_conexao='Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
con=Conexao(string_conexao)
sql = "SELECT * FROM STG_LOJAS "
rs=con.consultar("SELECT * FROM STG_LOJAS")
for linha in rs:
    print (linha.NOME)
con.fechar()
'''