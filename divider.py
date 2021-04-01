import random
class LengthObject:
  def __init__(self, name, length):
    self.name = name
    self.length = length
    
mainObjectArray = []


class LaserColumn:
  def __init__(self, laserIndexList, laserTotal):
    self.laserIndexList = laserIndexList
    self.laserTotal = laserTotal
    
def organizeArray (nameArray, numberOfColumns):
  #Find length of all curves
  objectArray = createLengthArray(nameArray)
  #Sort lengths
  objectArray.sort(key=lambda x: x.length)
  #divide lasers into arrays
  arrayOfArrays = sortIntoArrays(objectArray, numberOfColumns)
  #Return array of arrays 
  print(arrayOfArrays)

def createLengthArray (nameArray):
  #addobject to main Array 
  for name in nameArray:
    object = bpy.data.objects[name]
    mainObjectArray.append(findLengthOfCurves(object))
  #return array
  return mainObjectArray
    
       
def findLengthOfCurves (object):
  #return length/name object
  ob = object
  me = ob.data
  bm = bmesh.from_edit_mesh(me)    

  perimeter = [e for e in bm.edges if e.is_boundary]  
  ret = edge_line_segments(bm, edges=perimeter, tol_angle=radians(5))
  segments = [(sum(e.calc_length() for e in s), s)
        for s in ret["segments"]]
  segments.sort(key=lambda s: s[0])
  #pathlength
  segmentsnumber = 0
  #compute Path length
  for i, (length, edges) in enumerate(segments):
  
     for e in edges:
        e.select = i == len(segments) - 1 
        segmentsnumber = e.calc_length() + segmentsnumber
  #return to object mode    
  newLengthObject = LengthObject(object.name, segmentsnumber)
  
  return newLengthObject

def sortIntoArrays (objectArray, numberOfColumns):
  #Get largest and divide into columns "numberOfColumns" Times
  #delete the one you added eachtime
  columnList = []
  ArrayOfArrays = []
  objectArrayLength = len(objectArray) - numberOfColumns
  
  for index in range(0, numberOfColumns):
    nameArray = [objectArray[0].name]
    laserLength = objectArray[0].length
    newLaserColumn = LaserColumn(nameArray, laserLength) 
    columnList.append(newLaserColumn)
    removeItem(objectArray, True)
    
  for index in range(0, objectArrayLength):
    columnList.sort(key=lambda x: x.laserTotal)
    sC = columnList[0]
    sO = objectArray[-1]
    sOname = sO.name
    sOlength = sO.length
    sCNumber = sC.laserTotal
    sCarray = sC.laserIndexList
    sCarray.append(sOname)
    sC.laserIndexList = sCarray
    sC.laserTotal = int(sCNumber) + int(sOlength)
    removeItem(objectArray, False)
    
  numbertotals = []
  for column in columnList:
    ArrayOfArrays.append(column.laserIndexList)
  for column in columnList:
    numbertotals.append(column.laserTotal)
  print(numbertotals)
  return ArrayOfArrays
    

    
  
    
def removeItem (array, front):
    #if true delete first in array
    if front:
      array.pop(0)
    #if false delete last in array
    else:
      array.pop()
    
#### SORTING FUNCTION END USE: organizeArray(Namelist, column#)

objectArray = []
numberArray = []
nameArray = ['frog0', 'frog1', 'frog2', 'frog3', 'frog4', 'frog5', 'frog6', 'frog7', 'frog8', 'frog9', 'frog10', 'frog11', 'frog12', 'frog13', 'frog14', 'frog15', 'frog16', 'frog17', 'frog18', 'frog19', 'frog20', 'frog21', 'frog22', 'frog23', 'frog24', 'frog25', 'frog26', 'frog27', 'frog28', 'frog29', 'frog30', 'frog31', 'frog32', 'frog33', 'frog34']
for name in nameArray: 
  newnumber = random.randint(0,200)
  newLengthObject = LengthObject(name, newnumber)
  numberArray.append(name)
  numberArray.append(newnumber)

  objectArray.append(newLengthObject)

objectArray.sort(key=lambda object: object.length, reverse=True)
  #divide lasers into arrays
arrayOfArrays = sortIntoArrays(objectArray, 6)
  #Return array of arrays
print(arrayOfArrays) 

print(numberArray)
