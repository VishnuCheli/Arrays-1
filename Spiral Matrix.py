#Time Complexity:: O(m*n)-traversing all the elements in the 2D matrix
#Space Complexity:: O(m*n)-new result array is created
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n=len(matrix[0]) #columns
        m=len(matrix) #rows
        result=[0]*(m*n) #initialize new reuslt array
        
        l=0 #initialize left pointer
        r=n-1 #initialize right pointer
        t=0 #initialize top pointer
        b=m-1 #initialize bottom pointer
        index=0
        
        while (index<(m*n)):
            for i in range(l,r+1,1): #left to right
                result[index]=matrix[t][i]
                index+=1
            t+=1
            for j in range(t,b+1,1): #top to bottom
                result[index]=matrix[j][r]
                index+=1
            r-=1
            
            if index==(m*n): #edge case to control the index out of range error as index goes 1 over the length of the result array
                break
            
            for k in range(r,l-1,-1): #right to left
                result[index]=matrix[b][k]
                index+=1
            b-=1
            for p in range(b,t-1,-1): #bottom to top
                result[index]=matrix[p][l]
                index+=1
            l+=1
        return result
                
            
                