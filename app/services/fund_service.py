from app.data_management import Repository

class Fund_service():

    def __init__(self, repo:Repository):
        self.repo = repo


    def fund_check(self, user_id, fund_spent):
        result = self.repo.search_user(user_id)

        if result['fund'] < fund_spent:
            raise ValueError(f'你没有足够的资金！你目前的资金是：{result['fund']}')
        
        return True