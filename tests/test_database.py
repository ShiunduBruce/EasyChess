from database.database import Database
import random


class TestDatabase:

    # Test create database
    def testCreateTable(self):
        database = Database()
        database.dropTable()

        # Assert creation of database
        assert database.createTable() == True
        # Database already exists
        for i in range(5):
            assert False == database.createTable()

    # Test insert of records
    def testInsert(self):
        # Test correct values passed
        database = Database()
        # Remove the previos table
        database.dropTable()
        database.createTable()

        # Correct values passed
        for i in range(10):
            moves = random.randrange(100, 3000)
            won = random.choice([True, False])
            assert True == database.insert(moves, won)

        # Wrong values passed
        for i in range(10):
            moves = random.randrange(100, 3000)
            won = random.choice([True, False])
            assert False == database.insert(str(moves), int(won))

        # This functionality never fails
        def testDropTable(self):
            database = Database()
            assert True == database.dropTable()

            for _ in range(100):
                assert True == database.dropTable()

        # This functionality never fails
    def testClose(self):
        database = Database()
        assert True == database.close()
        # Always fails as it is already closed
        for _ in range(100):
            assert False == database.close()

        # Test select of records
    def testSelectAll(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # Test when lenght is zero
        for _ in range(5):
            assert 0 == len(database.selectAll())

        # Test when there is one or more
        for i in range(100):
            moves = random.randrange(100, 3000)
            won = random.choice([True, False])
            database.insert(moves, won)
            assert i + 1 == len(database.selectAll())

    # Test count of records
    def testSelectCountAll(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # Test when lenght is zero
        for _ in range(5):
            assert 0 == database.selectCountAll()

        # Test when there is one or more
        for i in range(10, 100):
            moves = random.randrange(100, 3000)
            won = random.choice([True, False])
            database.insert(moves, won)
            assert i - 9 == database.selectCountAll()

    def testSelectRecentGames(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # Test when we want recent games and there is none
        for i in range(1, 5):
            assert -1 == database.selectRecentGames(i)

        # Insert 5 records
        for _ in range(5):
            moves = random.randrange(100, 3000)
            won = random.choice([True, False])
            database.insert(moves, won)
        
        # Test when we want games and there is less than what we want
        for i in range(6, 10):
            assert -1 == database.selectRecentGames(i)

        # Test when we want games and there is enough in database
        for i in range(5):
            assert i == len(database.selectRecentGames(i))

    def testSelectWins(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # Test when there is zero records and zero wins
        assert 0 == len(database.selectWins())

        # Test when there is more records and zero wins
        for _ in range(5):
            database.insert(random.randrange(100, 3000), False)
            assert 0 == len(database.selectWins())

        # Test when there is 1 or more wins
        for i in range(5):
            database.insert(random.randrange(100, 3000), True)
            assert i + 1 == len(database.selectWins())

    def testSelectLosses(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # Test when there is zero records and zero losses
        assert 0 == len(database.selectLosses())

        # Test when there is more records and zero losses
        for _ in range(5):
            database.insert(random.randrange(100, 3000), True)
            assert 0 == len(database.selectLosses())

        # Test when there is 1 or more losses
        for i in range(5):
            database.insert(random.randrange(100, 3000), False)
            assert i + 1 == len(database.selectLosses())

    def testSelectCountWins(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # Test when there is zero records and zero wins
        assert 0 == database.selectCountWins()

        # Test when there is more records and zero wins
        for _ in range(5):
            database.insert(random.randrange(100, 3000), False)
            assert 0 == database.selectCountWins()

        # Test when there is 1 or more wins
        for i in range(5):
            database.insert(random.randrange(100, 3000), True)
            assert i + 1 == database.selectCountWins()

    def testSelectCountLosses(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # Test when there is zero records and zero losses
        assert 0 == database.selectCountLosses()

        # Test when there is more records and zero losses
        for _ in range(5):
            database.insert(random.randrange(100, 3000), True)
            assert 0 == database.selectCountLosses()

        # Test when there is 1 or more losses
        for i in range(5):
            database.insert(random.randrange(100, 3000), False)
            assert i + 1 == database.selectCountLosses()

    def testSelectFastesWin(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # When there is no record
        assert None == database.selectFastesWin()

        # Just losses and no wins
        for _ in range(5):
            database.insert(random.randrange(100, 3000), False)
            assert None == database.selectFastesWin()

        # Some wins
        for i in range(1, 100):
            database.insert(i, True)
            assert 1 == database.selectFastesWin()
            
    def testSelectFastesLoss(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # When there is no loss
        assert None == database.selectFastestLoss()

        # Just wins and no losses
        for _ in range(5):
            database.insert(random.randrange(100, 3000), True)
            assert None == database.selectFastestLoss()

        # Some losses
        for i in range(1, 100):
            database.insert(i, False)
            assert 1 == database.selectFastestLoss()

    def testSelectSlowestWin(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # When there is no record
        assert None == database.selectSlowestWin()

        # Just losses and no wins
        for _ in range(5):
            database.insert(random.randrange(100, 3000), False)
            assert None == database.selectSlowestWin()

        # Some wins
        for i in reversed(range(1, 100)):
            database.insert(i, True)
            assert 99 == database.selectSlowestWin()

    def testSelectSlowestLoss(self):
        database = Database()
        database.dropTable()
        database.createTable()

        # When there is no record
        assert None == database.selectSlowestLoss()

        # Just wins and no loss
        for _ in range(5):
            database.insert(random.randrange(100, 3000), True)
            assert None == database.selectSlowestLoss()

        # Some wins
        for i in reversed(range(1, 100)):
            database.insert(i, False)
            assert 99 == database.selectSlowestLoss()

    def testSelectTopWins(self):        
        database = Database()
        database.dropTable()
        database.createTable()

        # When there is no record
        assert -1 == database.selectTopWins(1)

        # Just losses and no wins
        for _ in range(5):
            database.insert(random.randrange(100, 3000), False)
            assert -1 == database.selectTopWins(4)

        # Some wins
        for i in range(1, 100):
            database.insert(i, True)
            assert i == database.selectTopWins(i)[0][1]

        # Check the return is equivalent to the requested
        for i in range(1, 10):
            assert i == len(database.selectTopWins(i))

    def testSelectTopLosses(self):        
        database = Database()
        database.dropTable()
        database.createTable()

        # When there is no record
        assert -1 == database.selectTopLosses(1)

        # Just wins and no losses
        for _ in range(5):
            database.insert(random.randrange(100, 3000), True)
            assert -1 == database.selectTopLosses(4)

        # Some lossess
        # Confirm they are orderd well
        for i in reversed(range(1, 100)):
            database.insert(i, False)
            assert i == database.selectTopLosses(1)[0][1]

        # Check the return is equivalent to the requested
        for i in range(1, 10):
            assert i == len(database.selectTopLosses(i))
