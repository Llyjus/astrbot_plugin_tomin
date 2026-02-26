from time import time


from app.data_management import Repository
from app.schemas import *



class Service():
    def __init__(self, repo: Repository):
        self.repo = repo

    def ensure_user_exists(self, user_id):
        user = self.repo.search_user(user_id)
        if user == None:
            self.repo.add_user(user_id)



class Card_service(Service):

    def __init__(self, repo:Repository):
        super().__init__(repo)




    def get_avail_cards_id(self, user_id, number) -> dict:
        
        # Return a list of slots need to be filled

        result_s = self.repo.search_slots(user_id)
            
        result_c = self.repo.search_card_last(user_id)

        result = {'cards_id':[],
                  'slots':[]}
        
        if result_c == None:
            for i in range(1, number + 1):
                result['cards_id'].append(i)
            return result


        # Slot
        for i in result_s:

            result['slots'].append(i['slot'])
            result['cards_id'].append(i['slot'])
            number -= 1
            if number <= 0:
                break
            
        # Still has number

        #save pos in slotss
        for i in range(1, number + 1):


            result['cards_id'].append(result_c['card_id']+i)

        
        return result
    
    
        


    def delete_slots(self, user_id, slot_list:list):

        slots = []

        for slot in slot_list:
            #slot tuple list
            slots.append((user_id, slot))

        self.repo.delete_slots(slots)




    def set_slots(self, user_id, slot_list:list):
        # after: Delete/Send card to other user

        # set the slots 
        # larger than the last card_id in cards

        last_card = self.repo.search_card_last(user_id)

        if last_card == None:
            value_id = 0

        else:
            value_id = last_card['card_id']

        slots = []

        largest = 0

        for card_id in slot_list:
            if card_id < value_id:
                slots.append((user_id, card_id))
            elif card_id > largest:
                largest = card_id


        # delete the illegal id in slot
        if largest != 0:
                

                # The largest card has deleted
                # so check if there is illegal slot
                cards_id = self.repo.search_slots(user_id)

                deletion = []

                for card_id in cards_id:
                    if value_id < card_id['slot']:
                        deletion.append((user_id, card_id['slot']))
                self.repo.delete_slots(deletion)


        # insert
        self.repo.add_slots(slots)
    










class Fund_service(Service):

    def __init__(self, repo:Repository):
        super().__init__(repo)



    def fund_check(self, user_id, fund_spent):
        result = self.repo.search_user(user_id)

        if result['fund'] < fund_spent:
            raise Not_enough_fund(f"你没有足够的资金！你目前的资金是：{result['fund']}")
        
        return True
    
    def fund_search(self, user_id):

        result = self.repo.search_user(user_id)

        return result['fund']
        
class Sign_in_service(Service):

    def __init__(self, repo:Repository):
        super().__init__(repo)

    def check_availability(self, user_id, time_now = None):

        result = self.repo.search_sign_in(user_id)

        if time_now is None:
            time_now = int(time())

        date = (time_now + 8 * 3600) // 86400

        # register
        if result == None:
 
            self.repo.add_sign_in(user_id, date, time_now)

            self.repo.add_fund(user_id, 10)
            return '今日首次打卡成功！+10资金\n'
        
        # check date
        elif result['date'] == date and result['count'] < 5:
                
                try:
            
                    self.repo.update_sign_in_count(user_id, time_now)
                except Exception as e:

                    seconds = result["timestamp"] + 4*3600 - time_now + 1

                    if seconds < 0:
                        raise e
                    
                    minutes = seconds // 60
                    hours = minutes // 60
                    
                    raise Cooldown(f'还未到冷却时间！{hours}小时{minutes % 60}分钟后再试吧！')
                return '打卡成功！今日已打卡次数：' + str(result['count'] + 1)

        elif result['date'] != date:
            # new date

            past_date = result['date']

            self.repo.update_sign_in_date(user_id, date, past_date, time_now)
        
            self.repo.add_fund(user_id, 10)
            return '今日首次打卡成功！+10资金\n'
        

        elif result['count'] >= 5:
            raise Cooldown('今日签到次数已达上限！')
        
        else:
            seconds = result["timestamp"] + 4*3600 - time_now
            minutes = seconds // 60
            hours = minutes // 60 + 1
            raise Cooldown(f'还未到冷却时间！{hours}小时{minutes % 60}分钟后再试吧！')














class Card_storage_service(Service):

    def __init__(self, repo):
        super().__init__(repo)



    def card_search_by_id(self, user_id, card_id):

        result:dict = self.repo.search_card(card_id=card_id, user_id=user_id)
        
        if result is None:
            raise Card_not_found('没有找到该卡牌！猪...')
        


        return result




    def cards_search_by_user(self, user_id):

        result = self.repo.search_cards(user_id=user_id)

        if result == []:
            raise Card_not_found('还没有卡牌呢！猪...')
        

        return result
    



    def card_send_to_user(self, giver_id, card_id, accepter_id ):
        
        # make sure it exist
        _card = self.card_search_by_id(card_id=card_id, user_id=giver_id)
        
        car_ser = Card_service(self.repo).get_avail_cards_id(accepter_id, 1)
        self.repo.set_card_user(car_ser['cards_id'][0], accepter_id, card_id, giver_id)
        
        return car_ser['slots']




    def cards_search_by_rarity(self, user_id, rarity):
        result:list = self.repo.search_cards_by_rarity(user_id=user_id, rarity=rarity)
        if result == []:
            raise Card_not_found('没有该稀有度的卡牌呢！猪...')
        

        return result
    


    
    def cards_search_by_band(self, user_id, o_band):
        result:list = self.repo.search_cards_by_band(user_id=user_id, o_band=o_band)
        if result == []:
            raise Card_not_found('没有该乐队的角色呢！猪...')

        return result
    


    def cards_search_by_band_rarity(self, user_id, o_band, rarity):
        result:list = self.repo.search_cards_by_band_rariry(user_id=user_id, 
                                                            o_band=o_band, 
                                                            rarity=rarity)
        if result == []:
            raise Card_not_found('没有匹配的角色呢！猪...')

        return result





    def sell_card(self, user_id, card_id):
        
        # make sure it exist
        _card = self.card_search_by_id(user_id=user_id, 
                                       card_id=card_id)

        rarity = _card['rarity']
        
        map = fund_map

        fund_gained = map[rarity]

        self.repo.delete_cards([(card_id, user_id)])

        self.repo.add_fund(user_id, fund_gained)

        return fund_gained
    
    
    def sell_cards_by_rarity(self, user_id, rarity):

        fund_gained = 0

        map = fund_map

        #Search cards below the rarity
        cards_id = []
        cards_list_length = 0

        for i in range(1, rarity+1): 
        
            result = self.repo.search_cards_by_rarity(user_id=user_id, rarity=i)
            for card in result:
                cards_id.append((card['card_id'], user_id))

                # Calculate fund gained
                cards_appended = len(cards_id) - cards_list_length

                fund_gained += map[i] * cards_appended

                cards_list_length = len(cards_id)


        if cards_id == []:
            raise Card_not_found('没有该稀有度以下的卡牌呢！猪...')
        
        # Delete cards and add fund
        self.repo.delete_cards(cards_id)
        self.repo.add_fund(user_id, fund_gained)

        cards_id = [card_id for card_id, user_id in cards_id]

        return {'cards_sold':cards_list_length, 'fund_gain': fund_gained, 'cards_id_list':cards_id}
    


class Avatar_service(Service):

    def __init__(self, repo):
        super().__init__(repo)



    def check_avatar(self, user_id, gap = 3 * 24 * 3600):

        result = self.repo.search_avatar(user_id)
        time_now = int(time())
        _gap = gap

        if result == None:
            return None
        elif time_now - result['update_time'] >= _gap:
            return False
        else:
            return True

    def update_avatar_record(self, user_id, result):
        if result is None:
            self.repo.add_avatar(user_id, int(time()))
        elif result == False:
            self.repo.update_avatar(user_id, int(time()))
        else:
            self.repo.update_avatar(user_id, int(time()))
        return True
        















class Working_service(Service):

    def __init__(self, repo):
        super().__init__(repo)


    def start_working(self, user_id, card_id, space, end_time, reward_fund):

        card = self.repo.search_card(card_id, user_id)
        if not card:
            raise Card_not_found('没有该卡牌呢！猪...')

        status = self.repo.search_working_by_card(user_id, card_id)
        if status:
            raise Already_in_working('该卡牌正在工作中！猪...')
        self.repo.add_working(card['card_uid'], space, end_time, reward_fund)
    
    def search_working_by_user(self, user_id):

        result = self.repo.search_working_by_user(user_id)
        return result
    
    def search_working_by_card(self, user_id, card_id):

        result = self.repo.search_working_by_card(user_id, card_id)
        return result

    def search_working_space_status(self):

        result = self.repo.search_space_worker()
        return result

    def delete_working(self, user_id, card_id):

        card = self.repo.search_card(card_id, user_id)
        if not card:
            raise Card_not_found('没有该卡牌呢！猪...')

        self.repo.delete_working(card['card_uid'])