import bisect
import pickle

def add_user_id(user_id, user_list):
    if user_list == []:
        user_list.append(user_id)
    else:
        user_list = bisect.bisect_left(user_list, user_id)
    save_users(user_list)
    return

def remove_user_id(user_id, user_list):
    try:
        del user_list[bisect.bisect_left(user_list, user_id)]
        save_users(user_list)
        return
    except EOFError:
        return

def load_users():
    with open('users.data', 'rb') as filehandle:
        try:
            user_list = pickle.load(filehandle)
        except EOFError:
            user_list = []
        return user_list

def save_users(user_list):
    with open('users.data', 'wb') as filehandle:
        pickle.dump(user_list, filehandle)
        return

def user_lang(user_id, user_list):
    for x in user_list:
        if x == user_id:
            return 'EN'
    return 'RS'
