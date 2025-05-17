"""
Utility functions for the automation script
"""

import random
import string

def generate_random_search_term(min_length=10, max_length=15):
    """
    Generate a random search term with the specified length
    
    Args:
        min_length (int): Minimum length of the search term
        max_length (int): Maximum length of the search term
        
    Returns:
        str: A random search term
    """
    # Define character sets
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    chars = lowercase_letters + digits
    
    # Generate a random length between min and max
    length = random.randint(min_length, max_length)
    
    # Generate the random search term
    search_term = ''.join(random.choice(chars) for _ in range(length))
    
    return search_term

def format_time(seconds):
    """
    Format seconds into a human-readable time string
    
    Args:
        seconds (int): Number of seconds
        
    Returns:
        str: Formatted time string
    """
    minutes, secs = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    
    if hours > 0:
        return f"{hours}h {minutes}m {secs}s"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"