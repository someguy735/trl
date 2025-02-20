from duckduckgo_search import DDGS

def search_duckduckgo(query: str, max_results: int = 5) -> list:
    """
    Perform a search using DuckDuckGo and return results
    
    Args:
        query (str): Search query
        max_results (int): Maximum number of results to return
    
    Returns:
        list: List of search results
    """
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=max_results)]
            return results
    except Exception as e:
        print(f"Error performing search: {e}")
        return []

def search_duckduckgo_without_docs(query: str, max_results: int = 5) -> list:
    try:
        with DDGS() as ddgs:
            results = [r for r in ddgs.text(query, max_results=max_results)]
            return results
    except Exception as e:
        print(f"Error performing search: {e}")
        return []