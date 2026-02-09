from app.data_management import Repository

def db_checker(repo:Repository):
    # Check the cards_id and slots is not repeated and continuous for each user

    users = repo.search_all_user()

    for user in users:
        
        card_set = set()
        cards = repo.search_cards(user['user_id'])

        for card in cards:
            card_set.add(card['card_id'])

        slots = repo.search_slots(user['user_id'])

        # no repeated slot
        for slot in slots:
            if slot['slot'] in card_set:
                return False
            else:
                card_set.add(slot['slot'])
        
        # make sure it's continuous
        for i in range(1, len(card_set)+1):
            if i not in card_set:
                return False
        
    return True