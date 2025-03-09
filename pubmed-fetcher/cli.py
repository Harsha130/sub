import argparse
import logging
import papers_fetcher

def parse_args():
    """
    Parses command-line arguments for the PubMed fetcher tool.

    Returns:
        argparse.Namespace: Parsed arguments with attributes:
            - query (str): PubMed search query.
            - debug (bool): Flag to enable debug output.
            - file (str or None): CSV output file name (if provided).
    """
    parser = argparse.ArgumentParser(
        description="Fetch Research Papers from PubMed and export details to CSV"
    )

    # Required positional argument for the PubMed query
    parser.add_argument(
        "query",
        type=str,
        help="PubMed search query string"
    )

    # Optional debug flag for verbose logging
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Enable debug output"
    )

    # Optional file argument to specify output CSV file name
    parser.add_argument(
        "-f", "--file",
        type=str,
        metavar="OUTPUT_FILE",
        help="Specify the output CSV file name"
    )

    return parser.parse_args()

def main():
    args = parse_args()

    # Enable debug logging if requested
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
        logging.debug("Debug mode enabled")
    else:
        logging.basicConfig(level=logging.INFO)

    logging.info(f"Query: {args.query}")

    # Fetch PubMed IDs based on the query
    pubmed_ids = papers_fetcher.fetch_pubmed_ids(args.query)
    logging.info(f"Found {len(pubmed_ids)} PubMed IDs")
    
    # For now, we simply print the IDs to the console.
    print("Retrieved PubMed IDs:")
    for pubmed_id in pubmed_ids:
        print(pubmed_id)

    # Here, you could add further logic to fetch paper details,
    # write to CSV if a file is provided, etc.
    if args.file:
        print(f"Output CSV file: {args.file}")
    else:
        print("No output file specified. Results are printed above.")

if __name__ == "__main__":
    main()

