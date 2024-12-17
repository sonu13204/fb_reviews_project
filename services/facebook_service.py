import requests
from config import BASE_FB_URL, PAGES, USER_API_TOKEN

def fetch_pages():
    """Fetch details of all pages(page_id, access_token, title)"""
    url = f"{BASE_FB_URL}/me/accounts"
    params = {"access_token": USER_API_TOKEN}
    response = requests.get(url, params=params)
    return response

def fetch_reviews(page_id: str, access_token: str):
    """Fetch reviews from a specific Facebook page."""
    url = f"{BASE_FB_URL}/{page_id}/ratings"
    params = {"access_token": access_token}
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": response.json()}

def fetch_reviews_for_all_pages():
    """Fetch reviews for all pages."""
    reviews = {}
    for page in PAGES:
        page_id = page["id"]
        token = page["token"]
        reviews[page_id] = fetch_reviews(page_id, token)
    return reviews

def reply_to_review(review_id: str, message: str, access_token: str):
    """Reply to a specific review."""
    url = f"{BASE_FB_URL}/{review_id}/comments"
    params = {"message": message, "access_token": access_token}
    
    response = requests.post(url, params=params)
    return response.json()
