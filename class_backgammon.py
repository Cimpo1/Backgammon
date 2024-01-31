'''
David Cimpoiasu , 2130140
R. Vincent , instructor
Advanced Programming , section 2
Final Project
'''


class pieces(object): #class for pieces on board
    '''Class for pieces on board'''
    
    def __init__(self, number, color, location, lane): #initializes the piece with a number, color, location, and lane
        '''Initializes the piece with a number, color, location, and lane'''
        self.number = number #number of the piece
        self.color = color #color of the piece (black or white)
        self.id = self.color + str(self.number) #id of the piece 
        self.location = location #location of the piece
        self.lane = lane #lane of the piece
        
    def __str__(self): #returns the id of the piece
        '''Returns the id of the piece'''
        return self.id
    
    def move(self, location, lane): #moves the piece to a new location
        '''Moves the piece to a new location'''
        self.location = location #sets the location of the piece to the new location
        self.lane = lane #sets the lane of the piece to the new lane
        
    def __repr__(self): #returns the id of the piece and its location and lane
        return self.id + ' ' + str(self.location) + ' ' + str(self.lane) 
    
class lane(object): #class for each lane on the board
    '''Class for each lane on the board'''
    
    def __init__(self, number, pieces = [], color = None): #initializes the lane with a number, pieces, and color
        '''Initializes the lane with a number, pieces, and color'''
        self.number = number #number of the lane
        self.id = 'lane' + str(self.number) #id of the lane
        self.pieces = pieces.copy() #list of pieces in the lane
        self.length = len(self.pieces) #length of the lane
        self.color = color #color of the lane
            
        
    def __str__(self): #returns the id of the lane
        '''Returns the id of the lane'''
        return self.id
    
    def add_piece(self, piece): #adds a piece to the lane
        '''Adds a piece to the lane'''
        
        if self.color != None and self.color != piece.color: #if the color of the piece is different than the color of the lane, raise an error
            raise ValueError('Cannot add piece of different color to lane' + str(self.number)) 
        
        if self.color == None: #if the lane is empty, set the color of the lane to the color of the piece
            self.color = piece.color
            
        self.pieces.append(piece) #add the piece to the lane
        self.length += 1 #increase the length of the lane by 1
        
    def remove_piece(self, piece): #removes a piece from the lane
        '''Removes a piece from the lane'''
        
        self.pieces.remove(piece) #remove the piece from the lane
        self.length -= 1 #decrease the length of the lane by 1
        if self.length == 0: #if the length of the lane is 0, set the color of the lane to None
            self.color = None 
        
    def get(self): #returns list of pieces in lane
        '''Returns list of pieces in lane'''
        
        return self.pieces 
    
    def __repr__(self): #returns the id of the lane and the number of pieces in it
        '''Returns the id of the lane and the number of pieces in it'''
        return self.id + ' ' + str(self.pieces)
        
        
        
    
    
    
    