def init():
    import os
    global pars
    pars = {
        'data_dir': os.getcwd()+'/',
        'url_base': 'https://www.indeed.com/',
        'url_base2': 'https://www.indeed.com',
        'id_location': 'text-input-where',
        'id_search': 'text-input-what',
        }
    return 0

init()

                
