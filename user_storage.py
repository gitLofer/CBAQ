import bisect
import pickle

def add_user_id(user_id, user_list):
    user_list.append(user_id)
    save_users(user_list)
    return

def remove_user_id(user_id, user_list):
    try:
        del user_list[user_list.index(user_id)]
        save_users(user_list)
        return
    except EOFError:
        print("EOF Error!")
        return

def load_users():
    with open('users.pkl', 'rb') as filehandle:
        user_list = pickle.load(filehandle)
    return user_list

def save_users(user_list):
    with open('users.pkl', 'wb') as filehandle:
        pickle.dump(user_list, filehandle)
    return

def user_lang(user_id, user_list):
    for x in user_list:
        if x == user_id:
            return 'EN'
    return 'RS'
