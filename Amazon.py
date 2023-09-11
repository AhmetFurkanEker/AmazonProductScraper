import requests
from bs4 import BeautifulSoup

url = []
veriler = [
]

def get_url():
    global url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    Url = 'https://www.amazon.com.tr/s?k=gaming+laptop&rh=n%3A12601898031&_encoding=UTF8&ref=sn_gfs_co_computers_O_3'

    response = requests.get(Url, headers=headers)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, 'lxml')
        ürünler = soup.find_all("div", attrs="a-section a-spacing-base")
        for ürün in ürünler:
            link = ürün.find_all("div", attrs="a-section a-spacing-none a-spacing-top-small s-title-instructions-style")
            for i in link:
                link = i.find("a", attrs="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
                ürün_link = link.get('href')
                amzn_link = "https://www.amazon.com.tr/"
                all_link = amzn_link + ürün_link
                url.append(all_link)
    else:
        print('Sayfa yüklenirken bir hata oluştu. Hata kodu:', response.status_code)


def descriptions():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
    }

    for URL in url:
        response = requests.get(URL, headers=headers)
        if response.status_code == 200:
            html_content = response.text
            product_link = BeautifulSoup(html_content, 'lxml')
            descriptions_product = product_link.find_all("div", attrs={"class": "a-column a-span6"})
            for detail in descriptions_product:
                details = detail.find_all('tr')
                if details:
                    for i in details:
                        try:
                            label = i.find("th", attrs={"class": "a-color-secondary a-size-base prodDetSectionEntry"})
                            label_value = i.find("td", attrs={"class": "a-size-base prodDetAttrValue"})
                            if label and label_value:
                                print(label.text + "==" + label_value.text)
                                
                        except:
                            print("Hata")
                else:
                    print("----------------------------------")
        else:
            print('Sayfa yüklenirken bir hata oluştu. Hata kodu:', response.status_code)

get_url()
descriptions()
