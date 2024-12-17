from fastapi import FastAPI, HTTPException
from services.facebook_service import fetch_reviews_for_all_pages, reply_to_review, fetch_pages

app = FastAPI()

@app.get("/pages")
async def get_pages():
    """API to fetch details for all Facebook pages."""
    return fetch_pages()

@app.get("/reviews")
async def get_reviews():
    """API to fetch reviews for all Facebook pages."""
    return fetch_reviews_for_all_pages()

@app.post("/reviews/{review_id}/reply")
async def post_reply(review_id: str, message: str, access_token: str):
    """
    API to reply to a specific Facebook review.
    
    Args:
        review_id (str): The ID of the review to reply to.
        message (str): The reply message.
        access_token (str): The Page Access Token.

    Returns:
        dict: Success or error response.
    """
    response = reply_to_review(review_id, message, access_token)
    if response.get("success"):
        return {"message": "Reply posted successfully", "response": response["response"]}
    else:
        raise HTTPException(status_code=400, detail=response["error"])