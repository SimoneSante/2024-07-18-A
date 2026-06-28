from database.DB_connect import DBConnect
from model.gene import Gene
from model.interaction import Interaction


class DAO():

    @staticmethod
    def get_all_genes():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                    FROM genes"""
            cursor.execute(query)

            for row in cursor:
                result.append(Gene(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_all_interactions():
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """SELECT * 
                       FROM interactions"""
            cursor.execute(query)

            for row in cursor:
                result.append(Interaction(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_archi(c,b):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select i.* 
                        from interactions i, classification c, classification c1
                        where i.GeneID1 In (select  g.GeneID 
                                            FROM  genes g
                                            where %s<= g.Chromosome and g.Chromosome<=%s)
                        and i.GeneID2 in (select  g.GeneID 
                                            FROM  genes g
                                            where %s<= g.Chromosome and g.Chromosome<=%s)
                        and c.GeneID =i.GeneID1 and c1.GeneID=i.GeneID2 AND c.Localization =c1.Localization and 
                        i.GeneID1 != i.GeneID2 """

            cursor.execute(query,[c,b,c,b])

            for row in cursor:
                result.append(Interaction(**row))

            cursor.close()
            cnx.close()
        return result

    @staticmethod
    def get_nodi(c,b):
        cnx = DBConnect.get_connection()
        result = []
        if cnx is None:
            print("Connessione fallita")
        else:
            cursor = cnx.cursor(dictionary=True)
            query = """select  g.*
                        FROM  genes g
                        where %s<= g.Chromosome and g.Chromosome<=%s"""

            cursor.execute(query,(c,b))

            for row in cursor:
                result.append(Gene(**row))

            cursor.close()
            cnx.close()
        return result