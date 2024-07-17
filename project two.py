import hashlib

def generate_short_url(long_url):
    
    
    hash_object = hashlib.md5(long_url.encode())
    hex_hash = hash_object.hexdigest()
    
    # Take the first 8 characters

    short_url = hex_hash[:8]
    
    return short_url

def main():
    long_url = input("Enter the long URL: ")
    short_url = generate_short_url(long_url)
    print(f"Short URL for '{long_url}': https://short.url/{short_url}")

if __name__ == "__main__":
    main()