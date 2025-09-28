from extract import get_usuarios, get_posts
import pandas as pd

def format_users():
    """Formtea la estructura json de users a una nueva"""
    usuarios = pd.json_normalize(get_usuarios())
    list_usuarios = []
    for usuario in usuarios.itertuples():
        list_usuarios.append({'id': usuario.id, 
        'name': usuario.name, 
        'username': usuario.username, 
        'address': f"{usuario._7}, {usuario._8}, {usuario._9}",
        'zipcode': usuario._10,
        'geo': f"{usuario._11}, {usuario._12}", 
        'phone': usuario.phone,
        'website': usuario.website, 
        'company_name': usuario._13,
        'company_carchPhase': usuario._14,
        'company_bs': usuario._15,
        })
        
    return list_usuarios

def get_usuarios_df():
    """Regraza un DataFrame de usuarios"""
    return pd.json_normalize(format_users())

def get_posts_df():
    """Regraza un DataFrame de posts"""
    return pd.json_normalize(get_posts())
