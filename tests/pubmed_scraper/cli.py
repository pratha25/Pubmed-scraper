import argparse
import csv
import logging
from pubmed_scraper.fetch import search_pubmed, fetch_details, parse_papers

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers with non-academic authors.")
    parser.add_argument("--query", "-q", required=True, help="PubMed search query")
    parser.add_argument("--file", "-f", help="CSV filename to save results")
    parser.add_argument("--debug", "-d", action="store_true", help="Enable debug output")

    args = parser.parse_args()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG)

    try:
        logging.info("Searching PubMed...")
        ids = search_pubmed(args.query, 20)
        if not ids:
            print("No papers found for this query.")
            return

        logging.info("Fetching paper details...")
        xml = fetch_details(ids)

        logging.info("Parsing papers...")
        papers = parse_papers(xml)

        if args.file:
            with open(args.file, "w", newline="", encoding="utf-8") as file:
                writer = csv.DictWriter(file, fieldnames=[
                    "PubmedID", "Title", "Publication Date",
                    "NonAcademicAuthors", "Affiliations"
                ])
                writer.writeheader()
                for paper in papers:
                    writer.writerow(paper)
            print(f"✅ Results written to {args.file}")
        else:
            for paper in papers:
                print(paper)

    except Exception as e:
        logging.exception("An error occurred:")
        print("❌ Failed to fetch papers:", str(e))
