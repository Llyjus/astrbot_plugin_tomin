from pydantic import BaseModel, Field, field_validator
from typing import Optional
from app.schemas import Invalid_input
from app.schemas.inter_util.text_dict import band_dict
from app.schemas.inter_util.place_dict import place_dict


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
        if v > 50 or v < 10:
            raise Invalid_input('招募资金不能大于50或小于10！')
        return v

    @field_validator('times')
    @classmethod
    def validate_times(cls, v):
        if v > 10 or v < 1:
            raise Invalid_input('招募次数不能大于10或小于1！')
        return v
    


class Card_input(BaseModel):
    band: Optional[str]=None
    rarity: Optional[int]=None
    card_id: Optional[int]=None

    @field_validator('band')
    @classmethod
    def validate_band(cls, v):
        if not v in band_dict:
            raise Invalid_input('不存在该乐队！')
        else:
            v = band_dict[v]

        return v

    @field_validator('rarity')
    @classmethod
    def validate_rarity(cls, v):
        if v < 1 or v > 6:
            raise Invalid_input('rarity必须在1~6之间！')

        return v
    

    


class Funds_reward_input(BaseModel):
    fund_amount: int

    @field_validator('fund_amount')
    @classmethod
    def validate_fund_amount(cls, v):
        if v < 0:
            raise Invalid_input('奖励资金必须为正数！')
        elif v > 100:
            raise Invalid_input('给的太多了！')   
        return v
    


class Working_input(BaseModel):
    card_id: int
    place: str
    hours: int

    @field_validator('place')
    @classmethod
    def validate_place(cls, v):
        if v not in place_dict:
            raise Invalid_input('不存在该工作地点！')
        return place_dict[v]

    @field_validator('hours')
    @classmethod
    def validate_hours(cls, v):
        if v < 1 or v > 8:
            raise Invalid_input('工作时间必须在1~8小时之间！')
        return v