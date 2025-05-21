# def insert_user_data(name:str,age:int):

#     print(name)
#     print(age)

#     print("user data is inserted into the database")


# insert_user_data("Deepak","twenty-three")


"""And the  one solution is  for theabove problem is to use the type hinting 


type hinting is just for the giving you the information not for producing the error so if you by nmistaly add the different type it will  not throw the error to you



so the pyhton type hiniting is not good for the type validation"""


## after type hinting we can see the type of the parameter 
# insert_user_data("Deepak",23)

## there is not type validation in the fuction 
## let take and example if senor developer want to add the type validation and he except the user of another junior program to entyer the age is the number format  but the junior developer has only see the function name and paramerter name and age is passing on that if the developer did not know what type of data to add then there will me the problem in the produyction phase and wroing data will me add in the data base 



def insert_user_data(name:str,age:int):
    if type(name)== str and type(age)== int: ## now this method is write for adding validation but not good for the saclability
        print(name)
        print(age)  
    else:
        raise TypeError("name should be string and age should be int")


    print("user data is inserted into the database")


insert_user_data("Deepak",23)





""" 
By default there is no type validation in the python and if you want to add the type validation then you have to write the code for that and this is not good for the scalability and also not good for the production phase"""


"""
--------------->
now this proble is sloved by the pydantic library"""




"""
1 problem  is ---> Type validation 
2 problem is ---> Data validation
"""



## for data validation 
def insert_user_data(name:str,age:int):
    if type(name)== str and type(age)== int: ## now this method is write for adding validation but not good for the saclability
        if age<0:
            raise ValueError("age should be greater than 0")
        if len(name)<3:
            raise ValueError("name should be greater than 3")
        print(name)
        print(age)  
    else:
        raise TypeError("name should be string and age should be int")


    print("user data is inserted into the database")


insert_user_data("Deepak",23)