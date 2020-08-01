#leetcode
def floodFill(image, sr, sc, newColor):
    color = image[sr][sc]
    def fun(image,sr,sc,newColor,color):
        if(image[sr][sc]==color and image[sr][sc]!=newColor):
            image[sr][sc] = newColor
            if(sr>=1):
                fun(image,sr-1,sc,newColor,color)
            if(sr+1<len(image)):
                fun(image,sr+1,sc,newColor,color)
            if(sc+1<len(image[0])):
                fun(image,sr,sc+1,newColor,color)
            if(sc>=1):
                fun(image,sr,sc-1,newColor,color)
            return image
        else:
            return image
    return(fun(image,sr,sc,newColor,color))



print(floodFill([[0,0,0],[0,1,1]],1,1,1))
