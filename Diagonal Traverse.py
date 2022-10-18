#Time Complexity:: O(m*n)-each element in the 2D matrix is visited once
#Space Complexity:: O(n*m) for the new result array
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        n=len(mat[0]) #no. of columns
        m=len(mat) #no. of rows
        result=[0]*n*m #creating result list
        
        r=0
        c=0
        flag=1 #initializing flag to traverse up
        index=0
        while(index<len(result)):
            result[index] = mat[r][c] #adding the element from the matrix after changing index
            
            #up
            if flag==1: #checks if next move is upwards
                if c+1>n-1: #boundary condition checks if there is a another column on the right
                    r+=1
                    flag=0
                elif r-1<0: #boundary condition checks if there is a another row above
                    c+=1
                    flag=0
                else: #moves diagonally up
                    r-=1
                    c+=1
            #down
            else:
                if r+1>m-1: #boundary condition checks if there is a another row on the bottom
                    c+=1
                    flag=1
                elif c-1<0: #boundary condition checks if there is a another column on the left
                    r+=1
                    flag=1
                else: #moves diagonally down
                    c-=1
                    r+=1
            index+=1 #changes the index to store the matrix value
        return result
                    
            
        