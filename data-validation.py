from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Required,Annotated

## firast pydantic model we created  --> step 1
class patient(BaseModel):
    name: Annotated[str,Field(min_length=3,max_length=50,title="name of patient",description="name of patient in the description",examples=["Deepak","Vikas","Rahul"])] ## min length and max length
    email:EmailStr
    age: int
    linkedin_url:AnyUrl
    weight: float=Field(gt=0,lt=1000) ## gt means greater than and lt means less than
    height: float=Field(gt=0,lt=10)
    married: Optional[bool]= False
    allergys:Annotated[Optional[List[str]],Field(max_length=5)]
    contact_deatils:Dict[str,str]


## step 2 make the object of the pydantic model

patient_info={
    'name':"Deepak",
    'email':"deepak@gamil.com",
              'age':23,
              'linkedin_url':"https://www.linkedin.com/in/deepak-kumar-123456789/",
              
            #   'age':"23",  ### pydantic is samrt enough to convert the string to int
              'weight':70.5,
              'height':5.8,
                # 'married':True,
                'allergys':["pollen","dust","cats","dogs","pollen"],
                'contact_deatils':{
                    # "email":"deepak@gmail",
                    "phone":"1234567890"
                }
              }


## step 3 pass the data to the pydantic model
patient1= patient(**patient_info) # unpacking the dictionary witjh **



## step 4 agive object to the function as parameter


def insert_user_data(patient:patient):
    print(patient.name)
    print(patient.name.title())
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.height)
    print(patient.married)
    print(patient.allergys)
    print(patient.contact_deatils)
    print("Data is inserted into the database")


insert_user_data(patient1)