from conexao import Conexao
class BuscaDados:
    server =".\SQLEXPRESS"
    database ="STAGE_AREA"
    username ="SA"
    password ="ERPM"
    string_conexao='Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    con=Conexao(string_conexao)
    sql = "SELECT * FROM STG_LOJAS "
    rs=con.consultar("SELECT * FROM STG_LOJAS")
    for linha in rs:
        print (linha.EMPRESA_USUARIA)
    con.fechar()