from pathlib import Path
import asyncio
import httpx

from app.schemas import Timeout, Invalid_input, Request_error, App_error, Infra_error
from app.services import Avatar_service
from app.data_management import Repository, connection


async def get_avatar(user_id, 
                     avatar_loc, 
                     platform, 
                     connect=None,
                     *,
                     avatar_ser = Avatar_service,
                     repository = Repository) -> dict:
    # check if avatar exists and valid, 
    # if not, get new avatar and update record
    result = {'error': None, 'avatar_loc': ''}
    try:
        if connect is None:
            connect = connection()
        with connect as conn:
            repo = repository(conn=conn)
            avt_ser = avatar_ser(repo=repo)
            avt_status = avt_ser.check_avatar(user_id)

            if avt_status:
                return {'error': None, 'avatar_loc': str(Path(avatar_loc) / f'{user_id}.jpg')}
            

            path = Path(avatar_loc) / f'{user_id}.jpg'
            path.parent.mkdir(parents=True, exist_ok=True)
            path.unlink(missing_ok=True)

            if avatar_dict.get(platform, ):

                try:
                    avatar_bytes = await avatar_dict[platform](user_id)
                    path.write_bytes(avatar_bytes)
                    result['avatar_loc'] = str(path)
                except Exception as e:
                    print('debug: error happened')
                    raise Request_error(f"获取头像失败：{str(e)}") from e
            
            else:   
                raise Invalid_input(f'平台错误：{platform}')
        
            avt_ser.update_avatar_record(user_id, avt_status)
        
    
    except App_error as e:
        result['error'] = str(e)

    except Infra_error as e:
        result['error'] = str(e)

    except Exception as e:
        result['error'] = f'未知错误：{str(e)}'


    return result




async def get_avatar_qq(user_id):
    #delete old avatar if exist, then get new avatar


    url = f'https://q1.qlogo.cn/g?b=qq&nk={user_id}&s=640'

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()
            return response.content
            
        except (httpx.RequestError, httpx.HTTPStatusError) as e:
            raise Timeout(f"获取头像失败：{str(e)}") from e
          



avatar_dict = {
            'qq': get_avatar_qq
        }