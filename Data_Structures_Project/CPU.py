#Class for the CPU data

class Cpu:            #Class information of CPU objects

  def __init__(self): #Constructor
    self.__name = ""    
    self.__brand = ""
    self.__corecount = 0
    self.__price = 0
    self.__maxclock = 0
    self.__TDP = 0
    self.__ID = 0
    
  #Methods for name variable
  def set_name(self, name):    #Method for defining the CPU name  -Amer Belal
    assert name == str(name) 
    self.__name = name  
      
  def get_name(self):          #Method for recieved the name of the CPU  -Amer Belal
    return self.__name

  #Methods for brand variable
  def set_brand(self, brand):   #Method for defining the brand name  -Amer Belal
    assert brand == str(brand)
    self.__brand = brand

  def get_brand(self):           #Method for retrieving the brand name  -Amer Belal
    return self.__brand
    
  #Methods for corecount variable -Eric Price
  def set_corecount(self, corecount): #Method for defining the core count
    assert corecount == int(corecount)
    self.__corecount = corecount
    
  def get_corecount(self): #Method for retrieving core count
    return self.__corecount
  
  #Methods for price variable -Eric Price
  def set_price(self, price): #Method for defining the core count
    assert price == (price)
    self.__price = price
 
  def get_price(self): #Method for retrieving core count
    return self.__price
    
  #Methods for maxclock variable -  Carlos Z
  def set_maxclock(self, maxclock): #Method to retrive maxclock speed
    assert maxclock == float(maxclock)
    self.__maxclock = maxclock      

  def get_maxclock(self): #Method to get maxclock speed -  Carlos Z
    return self.__maxclock

  #Methods for TDP variable   -  Carlos Z
  def set_TDP(self, TDP):  #Methog to retrive TDP
    assert TDP == int(TDP)
    self.__TDP = TDP

  def get_TDP(self):  #Method to get TDP -  Carlos Z
    return self.__TDP

  #Methods for ID variable -Eric Price  
  def set_ID(self, ID):  #Methog to retrive ID
    assert ID == int(ID)
    self.__ID = ID

  def get_ID(self):  #Method to get ID
    return self.__ID

  #Method to print the CPU statistics. - ALL
  def prnt_CPU(self): 

    print("\n",(self.get_name()),(self.get_brand()) , " $" ,(self.get_price()) , " " , (self.get_maxclock()) , "GHz " , (self.get_TDP()) , 'W \n')
  
#=============================
 