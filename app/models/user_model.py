from app.models import DatabaseConector

class User(DatabaseConector):
    @classmethod
    def check_database(cls):
        cls.get_conn_cur()
        query = """
            CREATE TABLE IF NOT EXISTS users(
                id  BIGSERIAL   PRIMARY KEY,
                name VARCHAR(50)    NOT NULL,
                age INTEGER NOT NULL,
                eyeColor    VARCHAR(50) NOT NULL,
                company VARCHAR(50) NOT NULL,
                email   VARCHAR(100) NOT NULL,
                profilePic  VARCHAR NOT NULL
            );
        """
        cls.cur.execute(query)
        
        
        cls.commit_and_close()

    @classmethod
    def add_data(cls):
        cls.get_conn_cur()

        query = """
            INSERT INTO 
                users(name,age,eyeColor,company,email,profilePic)
            
            VALUES
                ('John',22,'Green','Dialog','john@dialog.com','https://br.web.img3.acsta.net/pictures/19/02/04/20/58/4023772.jpg'),
                ('Clara',16,'Brown','Dialog','clara@dialog.com','https://pbs.twimg.com/profile_images/1261359377161879552/Kouh2WCe_400x400.jpg'),
                ('Mariana',18,'Blue','Dialog','mariana@dialog.com','https://upload.wikimedia.org/wikipedia/commons/7/77/Clara_Rugaard_at_the_premiere_of_Teen_Spirit%2C_2018_Toronto_Film_Festival_%2844028939874%29_%28cropped%29.jpg'),
                ('Bianca',16,'Brown','Dialog','bianca@dialog.com','https://br.web.img2.acsta.net/c_310_420/pictures/19/11/04/19/16/2044962.jpg'),
                ('Julia',29,'Brown','Dialog','Julia@dialog.com','https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpVJdawHSWpyHMK2OMyGZEX7gQLRtm2waQ9w&usqp=CAU'),
                ('João',44,'Brown','Dialog','joao@dialog.com','https://conteudo.imguol.com.br/c/noticias/d0/2020/06/03/valter-teria-provocado-prejuizo-de-r-1-milhao-a-bancos-digitais-1591221370503_v2_450x450.jpg'),
                ('Guilher',20,'Green','Dialog','guilher@dialog.com','https://emc.acidadeon.com/dbimagens/joao_gomes_1200x675_05112021154833.jpg');
            
               
                """

        cls.cur.execute(query)
        cls.commit_and_close()

    @classmethod
    def get_all(cls):
        cls.get_conn_cur()
        query = 'SELECT * FROM users'
        cls.cur.execute(query)
        response = cls.cur.fetchall()
        return response

    @classmethod
    def get_one(cls,userId):
        cls.get_conn_cur()
        query = "SELECT * FROM users WHERE id = %s"
        query_values = [str(userId)]
        print('*'*20)
        print(userId)
        print('*'*20)

        cls.cur.execute(query,query_values)
        response = cls.cur.fetchone()
        cls.commit_and_close()
        return response
        




        
