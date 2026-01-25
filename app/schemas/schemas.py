from pydantic import BaseModel, Field, field_validator

class Gacha_input(BaseModel):
    user_id: str
    fund_spent: int = Field(ge=10, 
                       le=100, 
                       description="招募资金必须在10到100之间！")
    
    times: int = Field(ge=1, le=100,
                       description="招募次数必须在1到100之间！")
    # @field_validator('bonus')
    # @classmethod
    # def validate_bonus(cls, v):
    #     if v > 100:
    #         raise ValueError('招募资金不能大于100！')

