# if age is greater then 60 then in the contact details there has to be emergency number if not we will not creste the pateient


from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
from typing import List,Dict,Optional,Required,Annotated

## firast pydantic model we created  --> step 1
class patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str]


    # @field_validator('email')
    # @classmethod
    # def email_validator(cls,value):


    #     valid_domains=["hdfc.com","icici.com"]
    #     domain_name=value.split("@")[-1]

    #     if domain_name not in valid_domains:
    #         raise ValueError("Invalid email domain")
    #     return value
    


    # @field_validator('name')
    # @classmethod
    # def tranform_name(cls,value):
    #     return value.upper()



    @model_validator(mode="after")
    def validate_emergency_contact(cls,model):
        if model.age > 60 and "emergency_contact" not in model.contact_details:
                raise ValueError("Emergency contact is required for patients above 60 years of age")
        return model
    


    


   



## step 2 make the object of the pydantic model

patient_info={
    'name':"Deepak",
    'email':"deepak@hdfc.com",
              'age':65,
              'weight':70.5,
                'married':True,
                'allergies':["pollen","dust","cats","dogs","pollen"],
                'contact_details':{
                    # "email":"deepak@gmail",
                    "phone":"1234567890",
                    "emergency_contact":"9876543210"
                }
              }


## step 3 pass the data to the pydantic model
patient1= patient(**patient_info) # unpacking the dictionary witjh **



## step 4 agive object to the function as parameter


def insert_user_data(patient:patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.weight)
    print(patient.allergies)
    print(patient.contact_details)
    print("Data is inserted into the database")


insert_user_data(patient1)


## Feils validator is worked on two mode of the pydantic model
## that is after mode and before mode
## before mode is used to validate the data before the data is passed to the pydantic model
## and after mode is used to validate the data after the data is passed to the pydantic model
