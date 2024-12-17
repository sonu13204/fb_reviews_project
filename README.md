# **Facebook Page Reviews API with FastAPI**

This project allows you to fetch reviews for multiple Facebook pages and reply to specific reviews using Facebook Graph API. It is implemented using **FastAPI** and is easily configurable through environment variables.

---

## **Features**

- **Fetch Facebook Page Reviews**: Retrieve all reviews from one or multiple Facebook pages.
- **Reply to Reviews**: Post replies to specific reviews using Facebook Graph API.
- **Easy Configuration**: Manage access tokens and API URLs through a `.env` file.

---

## **Table of Contents**

1. [Setup Instructions](#setup-instructions)
2. [Environment Variables](#environment-variables)
3. [API Endpoints](#api-endpoints)
4. [How to Use](#how-to-use)
5. [Run the Application](#run-the-application)
6. [Dependencies](#dependencies)
7. [Example Project Directory](#example-project-directory)
8. [Notes](#notes)
9. [Author](#author)
10. [License](#license)

---

## **1. Setup Instructions**

Follow these steps to set up and run the project:

### **Step 1: Clone the Repository**

```bash
git clone https://github.com/sonu13204/fb_reviews_project.git
cd fb-reviews-fastapi
```

## **Step 2: Create a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate       # For Linux/Mac
venv\Scripts\activate          # For Windows
```

## **Step 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

## **Step 4: Configure the Environment Variables**
Create a `.env` file in the root directory and add the following:
```bash
USER_API_TOKEN=your_user_api_token
BASE_FB_URL=https://graph.facebook.com/v18.0
PAGE_1_ID=your_page_id
PAGE_1_TOKEN=your_page_access_token
```

## **Step 5: Run the FastAPI Server**
```bash
uvicorn main:app --reload
```

## **Example `.env` file:**
```bash
USER_API_TOKEN=EAAH1ZC....example_token
BASE_FB_URL=https://graph.facebook.com/v18.0
PAGE_1_ID=1234567890
PAGE_1_TOKEN=EAAH2D....page_access_token
```
