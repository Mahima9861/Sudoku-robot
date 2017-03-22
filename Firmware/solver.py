
# update of one column		
	
def search_column(mat, num_column):
        """ Fill a vector with the numbers already found of the column num_column 
        Parameters:
        -----------
        mat: the matrix unsolved
        num_column: the number of the treated column
        Return:
        -------
        vect: the vector with the numbers already found
        """
        vect = []
        for i in range( len(mat) ):
                if (len( mat[i][num_column] ) == 1):
                        vect = vect + [mat[i][num_column]]
        return vect
	
def update_column(mat, num_column, vect,c):
        """ Verefy in the vector of possibilities if there are the numbers on the vector which returned by search_column
        and if it's the case remove the numbers
        Parameters:
        -----------
        mat: the matrix unsolved
        num_column: the number of the treated column
        vect: the vector with the numbers already found
        c: indicator to know if all the vector of possibilities are reduced to maximum
        Return:
        -------
        c: if c=1 the function modified mat and it has to continu, if not the function is not anymore used
        """
        for k in range( len( vect) ):
                for i in range( len( mat ) ):
                        if (len( mat[i][num_column] ) != 1):
                                for j in range( len( mat[i][num_column] ) ):
                                        if (mat[i][num_column][j] == vect[k][0]):
                                                del( mat[i][num_column][j] )
                                                c = 1
                                                break # quit the loop to avoid error seqfull
        return c

# update of one line

def search_line(mat, num_line):
        """ same than search_column but with a line"""
        vect = []
        for i in range( len( mat[0] ) ):
                if (len( mat[num_line][i] ) == 1):
                        vect = vect + [mat[num_line][i]]
        return vect
	
def update_line(mat, num_line, vect,c):
        """ same than update_column but with a line"""
        for k in range( len( vect) ):
                for i in range( len( mat[0] ) ):
                        if (len( mat[num_line][i] ) != 1):
                                for j in range( len( mat[num_line][i] ) ):
                                        if (mat[num_line][i][j] == vect[k][0]):
                                                del( mat[num_line][i][j] )

                                                c = 1
                                                break
        return c


# update of one bloc 

def identify_bloc(num):
        """ Delimitate the blocs
        Parameter:
        ----------
        num: the identifier of a bloc
        Return:
        -------
        a vector with the coordonate of bloc
        """
        if (num == 1):
                return [ [0,1,2], [0,1,2] ] # bloc at the top on the left
        elif (num == 2):
                return [ [0,1,2], [3,4,5] ] # bloc at the top in the midle
        elif (num == 3):
                return [ [0,1,2], [6,7,8] ] # bloc at the top on the right
        elif (num == 4):
                return [ [3,4,5], [0,1,2] ]
        elif (num == 5):
                return [ [3,4,5], [3,4,5] ]
        elif (num == 6):
                return [ [3,4,5], [6,7,8] ]
        elif (num == 7):
                return [ [6,7,8], [0,1,2] ]
        elif (num == 8):
                return [ [6,7,8], [3,4,5] ]
        else:
                return [ [6,7,8], [6,7,8] ] # bloc at the bottom on the right

def search_bloc(mat, bloc):
        """ same than serach_column with a bloc
        Parameter: bloc (coordonate od bloc) replace num_column
        """
        vect = []
        for i in bloc[0]:
                for j in bloc[1]:
                        if (len( mat[i][j] ) == 1):
                                vect = vect + [mat[i][j]]
        return vect

def update_bloc(mat, bloc, vect,c):
        """ same than update_column with a bloc
        Parameter: bloc (coordonate od bloc) replace num_column
        """
        for k in range( len( vect) ):
                for i in bloc[0]:
                        for j in bloc[1]:
                                if (len( mat[i][j] ) != 1):
                                        for l in range( len( mat[i][j] ) ):
                                                if (mat[i][j][l] == vect[k][0]):
                                                        del( mat[i][j][l] )
                                                        c = 1
                                                        break
        return c

# resume

def resume_line(mat, c):
        """ Update the matrix for all the lines
        Parameters:
        -----------
        mat: the matrix unsolved
        c: indicator to know if all the vector of possibilities are reduced to maximum
        Return:
        -------
        if c=1 the function modified mat and it has to continu, if not the function is not anymore used
        until the second upadte (cf update_column2); but it's true if only the three functions return c=0
        """
        for i in range(len(mat)):
                vect = []
                vect = search_line(mat, i)
                c = update_line(mat, i, vect, c)
        return c

def resume_column(mat, c):
        """ same than resume_line with a column"""
        for i in range(len(mat[0])):
                vect = []
                vect = search_column(mat, i)
                c = update_column(mat, i, vect, c)
        return c

def resume_bloc(mat, c):
        """ same than resume_line with a bloc"""
        for i in range(1,10):
                bloc = []
                bloc = identify_bloc(i)
                vect = []
                vect = search_bloc(mat, bloc)
                c = update_bloc(mat, bloc, vect, c)
        return c

# second way to update

def update_line2(mat, num_line):
        """ we search if there is un vector which has a unique number in a line. If it's the case,
            we replace the vector by this unique number
        Parameters:
        -----------
        mat: the matrix unsolved
        num_column: the number of the treated column
        Return:
        -------
        nothing
        """
        for i in range(1,10):
                k = -1 # variable used like a memory
                for j in range( len( mat[0] ) ):
                        if ( len( mat[num_line][j] ) != 1 ): # it's the vector is egal to [number] so the vextor is already optimal
                                for n in range(len( mat[num_line][j] )):
                                        if ( mat[num_line][j][n] == i):
                                                if ( k == -1):
                                                        k = j # if k is egal to -1, so it's the first time that we found the number i, 
                                                              # then we memorize the number of the line which has i
                                                else: # if k is different to -1, then there are two vector which have the number i => we quit this iteration
                                                        k = -2
                                                        break
                        elif (mat[num_line][j] == [i]): # if mat[num_line][j] = [i], then we quit the iteration
                                k = -2
                                break
                if ( k != -1 and k != -2 ):
                        mat[num_line][k] = [i]

                        


def update_column2(mat, num_column):
        """ same than update_lines with a column"""
        for i in range(1,10):
                k = -1
                for j in range( len( mat ) ):
                        if ( len( mat[j][num_column] ) != 1 ): 
                                for n in range(len( mat[j][num_column] )):
                                        if ( mat[j][num_column][n] == i):
                                                if ( k == -1):
                                                        k = j
                                                else:
                                                        k = -2
                                                        break
                        elif (mat[j][num_column] == [i]): 
                                k = -2
                                break
                if ( k != -1 and k != -2 ):
                        mat[k][num_column] = [i]

def update_bloc2(mat, bloc):
        """ same than update_lines with a bloc"""
        for k in range(1,10):
                l = -1
                m = 0 #second memory needed bcause it has to coordinate
                for i in bloc[0]:
                        for j in bloc[1]:
                                if ( len( mat[i][j] ) != 1 ):
                                        for n in range(len( mat[i][j] )):
                                                if ( mat[i][j][n] == i):
                                                        if ( l == -1):
                                                                l = i
                                                                m = j
                                                        else:
                                                                l = -2
                                                                break
                                                elif (mat[i][j] == [k]):
                                                        l = -2
                                                        break
                if ( l != -1 and l != -2 ):
                        print("bloc")
                        mat[l][m] = [k]
# security

def security_line( mat, num_line):
        """ Verify if there is a number twice and if there is a number which is not correct in one line
        Parameters:
        -----------
        mat: the matrix unsolved
        num_line: the number of the treated line
        Return:
        -------
        nothing
        """
        vect = [0]
        for i in range( len( mat[0] ) ):
                num = mat[num_line][i]
                if (num<0 or num>9):
                        print("bad number at", num_line, i)
                        exit()
                elif ( num!=0):
                        for j in range(len(vect)):
                                if (num == vect[j]):
                                        print("there is a number twice in the line ",num_line)
                                        exit()
                                vect = vect + [num]


def security_column( mat, num_column):
        """ same than update_lines with a column"""
        vect = [0]
        for i in range(len( mat ) ):
                num = mat[i][num_column]
                if ( num!=0):
                        for j in range(len(vect)):
                                if (num == vect[j]):
                                        print("there is a number twice in the column",num_column)
                                        exit()
                                vect = vect + [num]

def security_bloc( mat, n):
        """ same than update_lines with a bloc"""
        vect = [0]
        bloc = identify_bloc(n)
        for i in bloc[0]:
                        for j in bloc[1]:
                                num = mat[i][j]
                                if ( num!=0):
                                        for j in range(len(vect)):
                                                if (num == vect[j]):
                                                        print("there is a number twice in the bloc", n)
                                                        exit()
                                                vect = vect + [num]

def security(mat):
        """ verify if there are faults in the matrix
        Parameter:
        ----------
        mat: the matrix unsolved
        Return:
        -------
        nothing
        """
        for i in range(9):
                security_line(mat,i)
                security_column(mat,i)
                security_bloc(mat,i+1)
                
# resolver

def init( mat):
        """ transforme the matrix to be used in the algo: change the numbers different to 0 in vector
        of this number and replaced 0 by the vector [1,2,3,4,5,6,7,8,9]
        Parameter:
        ----------
        mat: matrix with numbers as parameters
        Return:
        -------
        mat: matrix used in the algo with vectors as parameters
        """
        for i in range(len(mat)):
                for j in range(len(mat[0])):
                        if (mat[i][j] == 0):
                                mat[i][j] = [1,2,3,4,5,6,7,8,9] # replace the zero by a vector with all the posibilities
                        else:
                                mat[i][j] =[ mat[i][j] ] # transform a whole number in a vector 
        return mat

def test_end(mat):
        """ verify if the sudoku is solved
        Parameter:
        ----------
        mat: sudoku which is bieng solved
        Returns:
        --------
        1 if it solved
        0 if not
        """
        for i in range( len(mat) ):
                for j in range( len( mat[0]) ):
                        if (len(mat[i][j]) != 1):
                                return 1
        return 0

def transform(mat):
        """ replace the vector of one number by this number
        Parameter:
        ----------
        mat: completed matrix with vectors as parameters
        Return:
        -------
        mat: same matrix with numbers as parameters
        """
        for i in range( len(mat) ):
                for j in range( len( mat[0]) ):
                        mat[i][j] = mat[i][j][0]
        return mat

def resolver(mat):
        """ Take the uncompleted sudoku and return it completed
        Parameter:
        ----------
        mat: a matrix 9 by 9 with zeros instead the white cases
        Return:
        -------
        mat: the same matrix with the zeros which are replaced by the correct numbers
        """
        security(mat)
        init( mat)
        secur = 0
        while(test_end(mat) or secur == 100):
                secur = secur +1
                c = 1
                while( c==1):
                        c = 0
                        c = resume_line(mat, c)
                        c = resume_column(mat, c)
                        c = resume_bloc(mat, c)
                        
                for i in range(len(mat)):
                        update_line2(mat, i)
                        
                while( c==1):
                        c = 0
                        c = resume_line(mat, c)
                        c = resume_column(mat, c)
                        c = resume_bloc(mat, c)
                c = 1
                        
                for i in range(len(mat[0])):
                        k = 0
                        update_column2(mat, i)
                        
                while( c==1):
                        c = 0
                        c = resume_line(mat, c)
                        c = resume_column(mat, c)
                        c = resume_bloc(mat, c)
                c = 1
                        
                for i in range(1,10):
                        bloc = []
                        bloc = identify_bloc(i)
                        update_bloc2(mat, bloc)

        mat = transform(mat)
        return mat
                























