import sqlite3 as sql
from database.Logger import Logger
#This class stores data from the model training
#It provides quick statiistcs from the model
#With this class we can gauge the performance of our model
#Possible improvements includes adding a difficulty level 
#The table is automatically created on creatin an instance

class Database:
    def __init__(self):
        self.logger = Logger('databaseLog.txt')
        self.logger.overwrite_logging('a','databaseLog.log')

        try:
            self.conn = sql.connect('EasyChess.db')
            self.cursor = self.conn.cursor()
            self.logger.info('Connection and database created successfully')
        except:
            self.logger.info('Failed to conect or create database. Both could be in existance')

    #Difficulty level 1-easy, 2-Medium, 3-Hard
    def createTable(self):
        try:
            self.cursor.execute('DROP TABLE IF EXISTS EasyChess')
            self.cursor.execute('''CREATE TABLE EasyChess
            (ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Moves        INT,
            Won            Bool,
            player_Name           TEXT,
            Complete         Bool,
            created_at     DEFAULT CURRENT_TIMESTAMP);''')
            self.logger.info('Easychess table created successfully')
            return True
        except:
            self.logger.warning('FAILED TO CREATE THE TABLE. THE TABLE MAY ALREADY EXIST')
            return False
    
    #Insert records into the database
    def insert(self, Moves, won, player_name = 'Player', Complete=True):
        try:
            val = (player_name, won, Moves, Complete)
            query = "INSERT INTO EasyChess (player_Name, won, Moves,Complete) \
            VALUES {}".format(val)
            self.cursor.execute(query)
            self.logger.info('One recored inserted successfully')
            return True
        except:
           self.logger.warning('INSERTION OF RECORDS FAILED')
           return False

    #Close the database connection
    def close(self):
        try:
            self.conn.commit()
            self.conn.close()
            self.logger.info('Database connection closed')
            return True
        except:
           self.logger.warning('FAILED TO  CLOSE DATABASE CONNECTION')
           return False


    #Returns an array of records, in tuples
    def selectAll(self):
        try:
            query = 'select * from EasyChess'
            self.cursor.execute(query)
            self.logger.info('All records successfully selected')
            return self.cursor.fetchall()
        except:
            self.logger.warning('UNABLE TO SELECT ALL RECORDS FROM DATABASE')
            return -1

    #Counts all the number of games records stored
    def selectCountAll(self):
        try:
            query = 'select count(*) from EasyChess'
            self.cursor.execute(query)
            totalRecords = self.cursor.fetchone()[0]
            self.logger.info('{} Total record count from db'.format(totalRecords))
            return totalRecords
        except:
            self.logger.warning('UNABLE TO SELECT ALL RECORDS FROM DATABASE')
            return -1

    #Selects the most recent games
    def selectRecentGames(self, records):
        try:
            query  = 'select * from EasyChess order by created_at desc limit {}'.format(records)
            self.cursor.execute(query)
            self.logger.info('{} most recent game records selected from db'.format(records))
            return self.cursor.fetchall()
        except:
            self.logger.warning('UNABLE TO SELECT MOST RECENT RECORDS FROM DATABASE WITH LIMIT {}'.format(records))
            return -1

    #Selects the most recent wins
    def selectRecentWins(self, records):
        try:
            query  = 'select * from EasyChess where won <> 0 order by created_at desc limit {}'.format(records)
            self.cursor.execute(query)
            self.logger.info('Recent game wins selected from db with limit {}'.format(records))
            return self.cursor.fetchall()
        except:
            self.logger.warning('UNABLE TO SELECT MOST RECENT WINS FROM DATABASE WITH LIMIT {}'.format(records))
            return -1

    #Selects the most recent losses
    def selectRecentLosses(self, records):
        try:
            query  = 'select * from EasyChess where won = 0 order by created_at desc limit {}'.format(records)
            self.cursor.execute(query)
            self.logger.info('Recent game losses selected from db with limit {}'.format(records))
            return self.cursor.fetchall()
        except:
            self.logger.warning('UNABLE TO SELECT MOST RECENT WINS FROM DATABASE WITH LIMIT {}'.format(records))
            return -1

    #Select records won by computer
    def selectWins(self):
        try:
            query  = 'select * from EasyChess where won <> 0'
            self.cursor.execute(query)
            self.logger.info('{} All game wins selected from db')
            return self.cursor.fetchall()
        except:
            self.logger.warning('UNABLE TO SELECT ALL WINS FROM DATABASE')
            return -1

    #Counts all the losses
    def selectLosses(self):
        try:
            query  = 'select * from EasyChess where won = 0'
            self.cursor.execute(query)
            self.logger.info('{} All game losses selected from db')
            return self.cursor.fetchall()
        except:
            self.logger.warning('UNABLE TO COUNT ALL WINS FROM DATABASE')
            return -1

    #Counts the number of wins 
    def selectCountWins(self):
        try:
            query  = 'select count(*) from EasyChess where won <> 0'
            self.cursor.execute(query)
            self.logger.info('All game wins counted from db')
            return self.cursor.fetchone()[0]
        except:
            self.logger.warning('UNABLE TO COUNT ALL WINS FROM DATABASE')
            return -1

    #Counts the number of lossess
    def selectCountLosses(self):
        try:
            query  = 'select count(*) from EasyChess where won = 0'
            self.cursor.execute(query)
            self.logger.info('All game losses counted from db')
            return self.cursor.fetchone()[0]
        except:
            self.logger.warning('UNABLE TO COUNT ALL WINS FROM DATABASE')
            return -1

    #Select the fastest win 
    def selectFastesWin(self):
        try:
            query  = 'select min(moves) from EasyChess where won <> 0'
            self.cursor.execute(query)
            self.logger.info('Fastest win selected from db')
            return self.cursor.fetchone()[0]
        except:
            self.logger.warning('UNABLE TO GET FASTEST WIN FROM THE DATABASE')
            return -1

    
    #Select the fastest loss
    def selectFastestLoss(self):
        try:
            query  = 'select min(moves) from EasyChess where won = 0'
            self.cursor.execute(query)
            self.logger.info('Fastest loss selected from db')
            return self.cursor.fetchone()[0]
        except:
            self.logger.warning('UNABLE TO GET FASTEST LOSS FROM THE DATABASE')
            return -1
    
    #Select the slowest win
    def selectSlowestWin(self):
        try:
            query  = 'select max(moves) from EasyChess where won <> 0'
            self.cursor.execute(query)
            self.logger.info('Slowest win selected from db')
            return self.cursor.fetchone()[0]
        except:
            self.logger.warning('UNABLE TO GET SLOWEST WIN FROM THE DATABASE')
            return -1

    #Select the slowest loss
    def selectSlowestLoss(self):
        try:
            query  = 'select max(moves) from EasyChess where won = 0'
            self.cursor.execute(query)
            self.logger.info('Slowest loss selected from db')
            return self.cursor.fetchone()[0]
        except:
            self.logger.warning('UNABLE TO GET SLOWEST LOSS FROM THE DATABASE')
            return -1

    #Select the top wins
    def selectTopWins(self, records):
        try:
            query  = 'select * from EasyChess where won <> 0 order by moves limit {}'.format(records)
            self.cursor.execute(query)
            self.logger.info('Top wins with limit {} selected from db'.format(records))
            return self.cursor.fetchall()
        except:
            self.logger.warning('UNABLE TO GET TOP WINS FROM THE DATABASE WITH LIMIT {}'.format(records))
            return -1

    #Select the top wins
    def selectTopLosses(self, records):
        try:
            query  = 'select * from EasyChess where won = 0 order by moves limit {}'.format(records)
            self.cursor.execute(query)
            self.logger.info('Top losses with limit {} selected from db'.format(records))
            return self.cursor.fetchall()
        except:
            self.logger.warning('UNABLE TO GET TOP LOSSES FROM THE DATABASE WITH LIMIT {}'.format(records))
            return -1