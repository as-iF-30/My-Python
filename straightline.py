def checkStraightLine(coordinates):
    if(len(coordinates)==2):
        return True
    else:
        try:
            a = (coordinates[1][1] - coordinates [0][1])/(coordinates[1][0] - coordinates[0][0])
        except:
            a  = 0
        b = coordinates[0]
        for i in range(2,len(coordinates)):
            try:
                c = (coordinates[i][1] - b[1])/(coordinates[i][0]- b[0])
            except:
                c = 0
            if(c!=a):
                return False
    return True

print(checkStraightLine([[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]))
