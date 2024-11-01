# Import the pyshorteners library
import pyshorteners


def shorten_url(long_url):
    """
    Shortens a given URL using the TinyURL service.

    Args:
        long_url (str): The original URL that needs to be shortened.

    Returns:
        str: The shortened URL.

    Raises:
        Exception: If there is an issue with shortening the URL.
    """
    # Initialize the Shortener class from pyshorteners with the TinyURL API
    try:
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(long_url)
        return short_url
    except Exception as e:
        print("Error occurred while shortening the URL:", e)
        return None


def main():
    """
    Main function that prompts the user to enter a URL,
    shortens it, and displays the shortened version.
    """
    # Prompt the user to enter a long URL
    long_url = input("Enter the URL to be shortened: ")

    # Shorten the URL
    short_url = shorten_url(long_url)

    # Display the shortened URL if successful
    if short_url:
        print("Shortened URL:", short_url)
    else:
        print("Failed to shorten the URL.")


if __name__ == "__main__":
    main()
