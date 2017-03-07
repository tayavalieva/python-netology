import vk
from requests import ReadTimeout
from vk.exceptions import VkAPIError
import pandas as pd


user_id = 'iamniketas'
app_id = '5894070'
login = 'taya.skachkova@gmail.com'
password = ''
session = vk.AuthSession(app_id=app_id, user_login=login, user_password=password)
api = vk.API(session)


def get_followers_list(user_id):
    followers_list = []
    need_to_load = True
    while need_to_load:
        try:
            offset = len(followers_list)
            list_to_add = api.users.getFollowers(user_ids=user_id, offset=offset)['items']
            followers_list.append(list_to_add)
            need_to_load = len(list_to_add) > 0
        except:
            pass
    return followers_list


def get_fans_list(user_id):
    followers_list = get_followers_list(user_id)
    friends_list = api.friends.get(user_ids = user_id)
    fans_list = followers_list + friends_list
    return fans_list

def get_fans_groups_dict(fans_list):
    success_count = 0
    fail_count = 0
    fans_groups_dict = {}
    for fan in fans_list:
        try:
            groups_list = api.groups.get(user_id = fan)
            success_count += 1
            for group in groups_list:
                if group in fans_groups_dict:
                    fans_groups_dict[group] += 1
                else:
                    fans_groups_dict[group] = 1
        except VkAPIError as e:
            fail_count += 1
        except ReadTimeout as e:
            fail_count += 1
            #print('При обработке пользователя с ID {} возникла ошибка: {}.'.format(fan, e))
    print('{} ID обработаны успешно.{} ID не удалось обработать.'.format(success_count,fail_count))
    return fans_groups_dict

def get_group_name(group_id):
    try:
        group_name = api.groups.getById(group_ids = group_id)[0]['name']
        return group_name
    except ReadTimeout as e:
        return ""

def create_dataframe(fans_groups_dict):
    df = pd.DataFrame(list(fans_groups_dict.items()), columns=['GroupID', 'FansNumber'])
    df = df.sort_values(by=["FansNumber"], ascending=False).head(100)
    df['GroupName'] = df['GroupID'].map(get_group_name)
    return df

df = create_dataframe(get_fans_groups_dict(get_fans_list(user_id)))
df.to_json("groups.json")


#df.to_csv('groups.csv', encoding="utf-8")

#df = pd.read_csv("groups.csv")







