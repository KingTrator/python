def pudim():
    import requests
    url = 'http://pudim.com.br'
    try:
        _ = requests.get(url, timeout=30)    # O uso do "undercore" "_" é para deixar claro que essa variável
                                            # está sendo intencionalmente ignorada.
        print('\033[1;32mO site pudim está disponível :D\033[m')
    except requests.ConnectionError:
        print('\033[1;31mO site pudim não está disponível TT\033[m')


pudim()