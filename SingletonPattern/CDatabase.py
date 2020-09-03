class Database():

    __objDatabase = None

    def __init__( self ):
        if Database.__objDatabase != None:
             raise Exception("This class is a singleton!")
        else:
            Database.__objDatabase = self

    @classmethod
    def getInstance( cls ):
        if( cls.__objDatabase == None ):
            print( "First Instance" )
            cls.__objDatabase = Database()
        
        return cls.__objDatabase