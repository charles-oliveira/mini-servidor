import requests 

def fetch_content(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Resposta do Servidor:")
            print(response.text)
        else:
            print(f"Falha ao acessar {url}. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao tentar acessar {url}: {e}")

if __name__ == '__main__':
    base_url = 'http://192.168.3.2:8080' 
    endpoints = ['', '404', '500']

    for endpoint in endpoints:
        url = f'{base_url}/{endpoint}'
        print(f"Acessando {url}")
        fetch_content(url)
        print()
