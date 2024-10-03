import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to get the HTML content of the webpage
def get_page_content(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.content
    else:
        print(f"Failed to retrieve the content. Status code: {response.status_code}")
        return None

# Function to extract product information (name, price, rating) from a single page
def extract_product_info(content):
    soup = BeautifulSoup(content, 'html.parser')
    
    products = []
    
    # Example for extracting product info (this structure may vary based on the website)
    for product in soup.find_all('div', class_='product-item'):  # Use the correct class or tag based on the website
        try:
            name = product.find('h2', class_='product-title').text.strip()  # Example class, adjust based on actual site
            price = product.find('span', class_='price').text.strip()       # Adjust based on actual site structure
            rating = product.find('span', class_='rating').text.strip()     # Adjust based on actual site structure
            products.append([name, price, rating])
        except AttributeError:
            continue  # In case any element is missing, skip the product
    
    return products

# Function to save the extracted information to a CSV file
def save_to_csv(products, filename):
    df = pd.DataFrame(products, columns=['Name', 'Price', 'Rating'])
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

# Main function to execute the scraping
def main():
    url = 'https://www.example.com/products-page'  # Replace with the actual e-commerce URL
    content = get_page_content(url)
    
    if content:
        products = extract_product_info(content)
        
        if products:
            save_to_csv(products, 'products.csv')
        else:
            print("No products found on the page.")
    else:
        print("Failed to retrieve page content.")

if __name__ == '__main__':
    main()
