def main():
    import argparse
    from pubmed_scraper.fetch import search_pubmed, fetch_details, parse_papers
    import logging

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="Fetch PubMed papers")
    parser.add_argument("--query", required=True, help="Search query for PubMed")
    parser.add_argument("--file", default="output.csv", help="Output CSV filename")
    parser.add_argument("--debug", action="store_true", help="Enable debug logging")

    args = parser.parse_args()

    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    logging.info("Searching PubMed...")
    ids = search_pubmed(args.query)
    logging.info("Fetching paper details...")
    xml = fetch_details(ids)
    logging.info("Parsing papers...")
    papers = parse_papers(xml)

    # Save to CSV
    import csv
    with open(args.file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=papers[0].keys())
        writer.writeheader()
        writer.writerows(papers)

    print("✅ Results written to", args.file)
