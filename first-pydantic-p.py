from pydantic import BaseModel

## firast pydantic model we created  --> step 1
class patient(BaseModel):
    name: str
    age: int
    weight: float


## step 2 make the object of the pydantic model

patient_info={'name':"Deepak",
              'age':23,
              'weight':70.5
              }


## step 3 pass the data to the pydantic model
patient1= patient(**patient_info) # unpacking the dictionary witjh **



## step 4 agive object to the function as parameter


def insert_user_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print("Data is inserted into the database")


insert_user_data(patient1)


""" Above code is the basic example of the pydantic model and how to use it in the function as a parameter and how to pass the data to the pydantic model and how to unpack the dictionary with ** and how to use the pydantic model in the function as a parameter and how to access the data from the pydantic model 


This is used for the type validation for now but in the future we will see the data validation also"""