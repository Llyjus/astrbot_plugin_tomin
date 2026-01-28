from pydantic import BaseModel, Field, field_validator
from app.schemas import Invalid_input


class Gacha_input(BaseModel):
    user_id: str
    fund_spent: int #= Field(ge=10, 
    #                    le=100, 
    #                    description="招募资金必须在10到100之间！")
    
    times: int #= Field(ge=1, le=100,
                      # description="招募次数必须在1到100之间！")
    @field_validator('fund_spent')
    @classmethod
    def validate_fund_spent(cls, v):
        if v > 100 or v < 10:
            raise Invalid_input('招募资金不能大于100或小于10！')
        return v

    @field_validator('times')
    @classmethod
    def validate_times(cls, v):
        if v > 100 or v < 1:
            raise Invalid_input('招募次数不能大于100或小于1！')
        return v
    
