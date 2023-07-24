### APIs ###

Version  | Date | Author | Notes |
:-------:|:----:|:-------|:-----:|
0.1 |24 July 2023| Ken Dizon | Initial version |


# API Libraries
try: 
    import requests
    from bs4 import BeautifulSoup
    # visuals
    from pprint import pprint
    from IPython.core.display import display, HTML

    print('Bs4 Documentation:', 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/')
    print("Libraries imported successfully!")
except ImportError:
    print("Libraries not installed. Please install it to use this library.")
    

# Website
url = 'www.google.com'
print(url[0])

# Extract using Bs4
response = requests.get(joola_url[1])
soup = BeautifulSoup(response.text, "html.parser")

# Look at whole HTLM and search for the element
print(soup.prettify())


# Creating a list to store words/products/names
element_list = []
X2 = []

# element extraction
elements = soup.find_all("heading/div", class_="someText")
element_list.extend([element.text.strip()
                          for element in elements])
#or
X2 = [tag.text.strip().replace('text ', '')
                  for tag in soup.find_all('heading/div',
                                           class_='someText')]


# Create a DataFrame from the scraped data
data = {"X1": elements, "X2": X2}
df = pd.DataFrame(data)