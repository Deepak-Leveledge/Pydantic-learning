from pydantic import BaseModel
from typing import List,Dict,Optional,Required

## firast pydantic model we created  --> step 1
class patient(BaseModel):
    name: str
    age: int
    weight: float
    height: float
    married: Optional[bool]= False
    allergys:Optional[List[str]]=None
    contact_deatils:Dict[str,str]


## step 2 make the object of the pydantic model

patient_info={
    # 'name':"Deepak",
              'age':23,
            #   'age':"23",  ### pydantic is samrt enough to convert the string to int
              'weight':70.5,
              'height':5.8,
                # 'married':True,
                # 'allergys':["pollen","dust"],
                'contact_deatils':{
                    "email":"deepak@gmail",
                    "phone":"1234567890"
                }
              }


## step 3 pass the data to the pydantic model
patient1= patient(**patient_info) # unpacking the dictionary witjh **



## step 4 agive object to the function as parameter


def insert_user_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergys)
    print(patient.contact_deatils)
    print("Data is inserted into the database")


insert_user_data(patient1)