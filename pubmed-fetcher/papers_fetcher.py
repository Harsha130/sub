import logging
from Bio import Entrez

# Set your email address (NCBI requires this for tracking usage)
Entrez.email = "your.email@example.com"

def fetch_pubmed_ids(query, retmax=20):
    """
    Fetches PubMed IDs based on a search query.
    
    Args:
        query (str): The PubMed search query.
        retmax (int): Maximum number of results to return.
    
    Returns:
        list: A list of PubMed IDs as strings.
    """
    try:
        handle = Entrez.esearch(db="pubmed", term=query, retmax=retmax)
        record = Entrez.read(handle)
        id_list = record.get("IdList", [])
        logging.debug(f"Fetched PubMed IDs: {id_list}")
        return id_list
    except Exception as e:
        logging.error(f"Error fetching PubMed IDs for query '{query}': {e}")
        return []

def fetch_paper_details(pubmed_id):
    """
    Fetches detailed information for a given PubMed ID.
    
    Args:
        pubmed_id (str): The PubMed ID.
    
    Returns:
        dict: Parsed details of the paper.
    """
    try:
        handle = Entrez.efetch(db="pubmed", id=pubmed_id, retmode="xml")
        records = Entrez.read(handle)
        logging.debug(f"Fetched details for PubMed ID {pubmed_id}: {records}")
        return records
    except Exception as e:
        logging.error(f"Error fetching details for PubMed ID {pubmed_id}: {e}")
        return None
