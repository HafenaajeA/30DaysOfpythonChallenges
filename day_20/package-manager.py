# Day 20 of  30 days of python challenges

# 1. Read this url and find the 10 most frequent words. romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

import requests

from collections import Counter
from string import punctuation

def get_most_frequent_words(url):
    # Fetch the text from URL
    response = requests.get(url)
    text = response.text.lower()
    
    # Remove punctuation and split into words
    for char in punctuation:
        text = text.replace(char, ' ')
    words = text.split()
    
    # Count words and get top 10
    word_counts = Counter(words)
    # Filter out empty strings and single-character words
    filtered_counts = {word: count for word, count in word_counts.items() 
                      if len(word) > 1}
    
    # Convert filtered dictionary back to Counter
    return Counter(filtered_counts).most_common(10)

# URL for Romeo and Juliet text
romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'

# Get and print the most frequent words
most_common_words = get_most_frequent_words(romeo_and_juliet)
print("\nThe 10 most frequent words in Romeo and Juliet are:")
for word, count in most_common_words:
    print(f"{word}: {count} times")

# 2.Read the cats API and cats_api = 'https://api.thecatapi.com/v1/breeds' and find :

    # the min, max, mean, median, standard deviation of cats' weight in metric units.
    # the min, max, mean, median, standard deviation of cats' lifespan in years.
    # Create a frequency table of country and breed of cats

import numpy as np
import pandas as pd

def analyze_cats_data():
    cats_api = 'https://api.thecatapi.com/v1/breeds'
    response = requests.get(cats_api)
    cats_data = response.json()
    
    # Convert to pandas DataFrame
    df = pd.DataFrame(cats_data)
    
    # Extract weight ranges and convert to numeric values
    weights = df['weight'].apply(lambda x: x['metric']).str.split('-', expand=True).astype(float)
    weight_mean = weights.mean(axis=1)
    
    # Extract lifespan ranges and convert to numeric values
    lifespan = df['life_span'].str.split('-', expand=True).astype(float)
    lifespan_mean = lifespan.mean(axis=1)
    
    # Calculate statistics
    weight_stats = {
        'min': weight_mean.min(),
        'max': weight_mean.max(),
        'mean': weight_mean.mean(),
        'median': weight_mean.median(),
        'std': weight_mean.std()
    }
    
    lifespan_stats = {
        'min': lifespan_mean.min(),
        'max': lifespan_mean.max(),
        'mean': lifespan_mean.mean(),
        'median': lifespan_mean.median(),
        'std': lifespan_mean.std()
    }
    
    # Create frequency table of country and breed
    country_breed_freq = pd.DataFrame({
        'breed': df['name'],
        'country': df['origin']
    }).groupby('country').count()
    
    # Print results
    print("\nCat Weight Statistics (in kg):")
    for stat, value in weight_stats.items():
        print(f"{stat.capitalize()}: {value:.2f}")
    
    print("\nCat Lifespan Statistics (in years):")
    for stat, value in lifespan_stats.items():
        print(f"{stat.capitalize()}: {value:.2f}")
    
    print("\nBreeds by Country:")
    print(country_breed_freq)

# Call the function
analyze_cats_data()


# 3. Read the countries API and find

    # the 10 largest countries
    # the 10 most spoken languages
    # the total number of languages in the countries API

def analyze_countries_data():
    # Fetch data from countries API
    countries_api = 'https://restcountries.com/v3.1/all'
    response = requests.get(countries_api)
    countries_data = response.json()
    
    # Convert to DataFrame
    df = pd.DataFrame(countries_data)
    
    # Find 10 largest countries by area
    largest_countries = df.nlargest(10, 'area')[['name', 'area']]
    largest_countries['name'] = largest_countries['name'].apply(lambda x: x['common'])
    
    # Process languages
    all_languages = []
    for languages in df['languages'].dropna():
        all_languages.extend(languages.values())
    
    # Count language frequencies
    language_counter = Counter(all_languages)
    most_common_languages = language_counter.most_common(10)
    
    # Print results
    print("\n10 Largest Countries:")
    for _, row in largest_countries.iterrows():
        print(f"{row['name']}: {row['area']:,.2f} sq km")
    
    print("\n10 Most Spoken Languages:")
    for lang, count in most_common_languages:
        print(f"{lang}: {count} countries")
    
    print(f"\nTotal number of languages: {len(set(all_languages))}")

# Call the function
analyze_countries_data()


#4. UCI is one of the most common places to get data sets for data science and machine learning. Read the content of UCL (https://archive.ics.uci.edu/ml/datasets.php). Without additional libraries it will be difficult, so you may try it with BeautifulSoup4

from bs4 import BeautifulSoup
import requests

def scrape_uci_datasets():
    # URL of UCI ML Repository
    url = 'https://archive.ics.uci.edu/ml/datasets.php'
    
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Check for any HTTP errors
        
        # Create BeautifulSoup object
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find the table containing datasets
        datasets_table = soup.find('table', {'border': '1'})
        
        if datasets_table:
            # Extract all dataset rows
            rows = datasets_table.find_all('tr')[1:]  # Skip header row
            
            print("\nUCI Machine Learning Repository Datasets:")
            print("-" * 50)
            
            for row in rows[:10]:  # Show first 10 datasets
                cols = row.find_all('td')
                if len(cols) >= 2:
                    name = cols[0].text.strip()
                    data_types = cols[1].text.strip()
                    print(f"Dataset: {name}")
                    print(f"Data Types: {data_types}")
                    print("-" * 30)
                    
            print(f"\nTotal number of datasets found: {len(rows)}")
            
        else:
            print("Could not find the datasets table on the page")
            
    except requests.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function
scrape_uci_datasets()

