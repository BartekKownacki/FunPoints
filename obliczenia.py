import mysql.connector
mydb = mysql.connector.connect(host='mysqlserver_ip', user='user1', password='userpasswd', database='punkty')
mycursor = mydb.cursor()

class Obliczenia:

    def suma():
        mycursor.execute("SELECT sum_of_fun_points FROM suma_punktow")
        myresult = mycursor.fetchone()
        for row in myresult:
            x = row
        return x


    def dodawanie():
        mycursor.execute("SELECT sum_of_fun_points FROM suma_punktow")
        myresult = mycursor.fetchone()
        for row in myresult:
            x = row
        sql = "UPDATE suma_punktow SET sum_of_fun_points = %s WHERE lp=1 "
        val = (x + 1,)
        mycursor.execute(sql, val)
        mydb.commit()
        return x+1

    def odejmowanie():
        mycursor.execute("SELECT sum_of_fun_points FROM suma_punktow")
        myresult = mycursor.fetchone()
        for row in myresult:
            x = row
        sql = "UPDATE suma_punktow SET sum_of_fun_points = %s WHERE lp=1 "
        val = (x - 1,)
        mycursor.execute(sql, val)
        mydb.commit()
        return x - 1
