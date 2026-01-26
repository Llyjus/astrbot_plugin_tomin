from app.data_management.repository.repository import Repository
from app.data_management.repository.connection import connection

class Card_service():

    def __init__(self, repo:Repository):
        self.repo = repo


    def user_exists(self, user_id):
        user = self.repo.search_user(user_id)
        if user == None:
            self.repo.add_user(user_id)



    def get_avail_cards_id(self, user_id, number) -> list:
        
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
                return result
            
        # Still has number

        #save pos in slotss
        for i in range(1, number + 1):


            result['cards_id'].append(result_c['card_id']+i)

        return result
        






    def fill_slots(self, user_id, slot_list:list):

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

                if cards_id == []:
                    return

                deletion = []

                for card_id in cards_id:
                    if value_id < card_id['slot']:
                        deletion.append((user_id, card_id['slot']))
                self.repo.delete_slots(deletion)


        # insert
        self.repo.add_slots(user_id, card_id)
    
