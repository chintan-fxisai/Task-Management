export const add_to_localestorage = (data)=>{
    
    localStorage.setItem('access_token', JSON.stringify(data.access_token));
    localStorage.setItem('refresh_token', JSON.stringify(data.refresh_token))
    localStorage.setItem('user', JSON.stringify(data.user));
}

export const clear_localestorage = ()=>{
    localStorage.clear();
}

export const get_from_localestorage = (key)=>{
    return localStorage.getItem(key);
}

export const is_active = () => {
    return get_from_localestorage('user');
}

