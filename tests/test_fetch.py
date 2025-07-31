# Importing required functions from the fetch module
from pubmed_scraper.fetch import search_pubmed, fetch_details, parse_papers
from pubmed_scraper.utils import save_to_csv

# Define the search query and how many papers you want to fetch
query = "covid"  # This is the keyword we want to search in PubMed
max_results = 10  # This is the maximum number of articles we want

# Step 1: Search PubMed for papers related to the query
print(f"Searching PubMed for '{query}' papers...")
ids = search_pubmed(query, max_results)
print("Found PubMed IDs:", ids)

# Step 2: Fetch detailed information for each PubMed ID
print("\nFetching paper details...")
papers = fetch_details(ids)

# Step 3: Parse the XML data to extract titles, authors, etc.
print("\nParsing papers...")
parsed_data = parse_papers(papers)

# Step 4: Save the parsed data into a CSV file
output_file = "output.csv"
print(f"\nWriting to {output_file}...")
save_to_csv(parsed_data, output_file)

# Final confirmation
print("✅ Done. Check output.csv")

