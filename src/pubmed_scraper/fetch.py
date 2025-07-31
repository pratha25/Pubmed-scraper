import requests
import xml.etree.ElementTree as ET
from typing import List, Dict

def search_pubmed(query: str, max_results: int = 10) -> List[str]:
    """
    Search PubMed for articles matching the query.
    
    Args:
        query (str): The search term.
        max_results (int): Maximum number of articles to fetch.

    Returns:
        List[str]: List of PubMed IDs.
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    ids = response.json()["esearchresult"]["idlist"]
    return ids

def fetch_details(pubmed_ids: List[str]) -> str:
    """
    Fetch full article details for given PubMed IDs.

    Args:
        pubmed_ids (List[str]): List of PubMed IDs.

    Returns:
        str: Raw XML data as string.
    """
    url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        "db": "pubmed",
        "id": ",".join(pubmed_ids),
        "retmode": "xml"
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.text

def parse_papers(xml_data: str) -> List[Dict[str, str]]:
    """
    Parse the XML data and extract article details with non-academic authors.

    Args:
        xml_data (str): XML content string.

    Returns:
        List[Dict[str, str]]: List of paper information dictionaries.
    """
    root = ET.fromstring(xml_data)
    papers = []

    for article in root.findall(".//PubmedArticle"):
        pubmed_id = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year") or "Unknown"
        authors_data = article.findall(".//Author")

        non_academic_authors = []
        affiliations = []

        for author in authors_data:
            last = author.findtext("LastName")
            fore = author.findtext("ForeName")
            aff = author.findtext(".//AffiliationInfo/Affiliation")

            full_name = f"{fore} {last}" if fore and last else None
            if full_name and aff:
                if not any(word in aff.lower() for word in ["university", "college", "institute", "hospital", ".edu", "school", "department"]):
                    non_academic_authors.append(full_name)
                    affiliations.append(aff)

        papers.append({
            "PubmedID": pubmed_id or "N/A",
            "Title": title or "N/A",
            "Publication Date": pub_date,
            "NonAcademicAuthors": ", ".join(non_academic_authors) or "None",
            "Affiliations": ", ".join(set(affiliations)) or "None"
        })

    return papers
