import requests
import logging
from typing import List, Optional
import xml.etree.ElementTree as ET

# Function to fetch PubMed IDs based on a search query
def fetch_paper_ids_from_pubmed(query: str, max_results: int = 10) -> List[str]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
    params = {
        'db': 'pubmed',
        'term': query,
        'retmax': max_results,  # Limit the number of results
        'usehistory': 'y',      # Use history for retrieving large result sets
        'retmode': 'xml'
    }

    # Log the query and parameters
    logging.debug(f"Fetching PubMed IDs for query: {query} with parameters: {params}")

    try:
        # Send the request to fetch paper IDs
        response = requests.get(base_url, params=params)

        # Check if the response status is successful
        if response.status_code == 200:
            logging.info(f"Successfully fetched paper IDs for query: {query}")
            
            # Parse the XML response to extract paper IDs
            root = ET.fromstring(response.content)
            
            # Extract the list of paper IDs from the XML response
            id_list = [id_tag.text for id_tag in root.findall(".//Id")]

            logging.debug(f"Fetched {len(id_list)} paper IDs")
            return id_list
        else:
            logging.error(f"Error fetching paper IDs: {response.status_code}")
            return []
    except requests.exceptions.RequestException as e:
        # Log the error if the request fails
        logging.error(f"Request failed: {e}")
        return []

# Function to send the request and get the paper's XML data
def fetch_xml_data(pubmed_id: str) -> Optional[ET.Element]:
    base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"
    params = {
        'db': 'pubmed',
        'id': pubmed_id,
        'retmode': 'xml'
    }

    # Log the request details
    logging.debug(f"Fetching XML data for PubMed ID: {pubmed_id} with parameters: {params}")

    try:
        # Send the request to fetch detailed paper information
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Check if the response status is successful
        if response.status_code == 200:
            logging.info(f"Successfully fetched XML data for PubMed ID: {pubmed_id}")
            return ET.fromstring(response.content)  # Return the XML root element
        else:
            logging.error(f"Error fetching paper details for PubMed ID {pubmed_id}: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        # Log the error if the request fails
        logging.error(f"Request failed for PubMed ID {pubmed_id}: {e}")
        return None