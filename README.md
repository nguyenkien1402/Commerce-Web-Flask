# Commercial-Web-Flask
A purly Flask commercial web app, using machine leanring to automatically label the uploaded images.
This project has made with the purpose to demonstrate all the google technologies. Some technologies are included:
  - Google App Engine
  - Firebase Storage 
  - Firebase Authentication
  - Firebase Database
  - Google Storage Bucket
  - Google Pub/Sub
  - Google AutoML
  - Google Vision API
  - Stripe
  - Google Cloud Function

## Setup and Installation Guide

1.  Go to [Google Console](https://console.cloud.google.com/) to create new project.
2.  Search credentails and create the new credential, download credential file as a *.json file
3.  Go to [Firebase Console](https://console.firebase.google.com/) and create new project. Copy the credential information and note somewhere to use later
4.  Install Google SDK, Python with seperate environment. If you don't mind to run in local environment, so install the all the necessary libraries from **requirements.txt** with the command: **pip install -r requirements.txt**
5.  Go to [Google Console](https://console.cloud.google.com/), select the menu storage and create a new bucket
6.  Go to [Google Console](https://console.cloud.google.com/), select pub-sub and create the following topic
    -   new-product
    -   payment-process
    -   payment-completion
7.  Go to app.py and change the **os.environ['GOOGLE_APPLICATION_CREDENTIALS']=="path/to/your-credential.json**
8.  Go to **static/initFirebase.js** and change the parameters to your firebase credential which you have when create the firebase application
9.  Go to [Google Console](https://console.cloud.google.com/), select the **cloud function** and create the two function
    -   First function: upload_image, copy the code in the main.py from the upload_image folder and choose HTTP as a trigger
    -   Second function: detect_label, copy the code in the main.py from the dectect_label folder and choose Pub/Sub as a trigger
10. Go to [Stripe Dashboard](https://dashboard.stripe.com/login?redirect=%2F), create new project and change get the API key, change the API key in the stripe.js to the new API key.
11. Go to [Google Console](https://console.cloud.google.com/), select App Engine and following the instruction
12. Active the Google and Email authentication in Firebase Console.
13. Deploy the application with google cloud sdk by following the command:
    -   **gcloud init**
    -   **gcloud app deploy**
    
The workflow of the application:
1.  User go the application and use google account as authentication
2.  Click to the sell button and upload the image.
3.  When user click the submit, the image will be stored in google storage, the detail is stored in firebase database, also the google cloud function will automatically detect the label for the image and assign the label for data.
4.  Customer can click add to cart to add the product to the cart
5.  Go to the cart and choose checkout
6.  Enter information and pay with the stripe.

The detail of how I constructed the application which integrate Google technologies will coming soon.

Some images of the application
## Home Page ##
![Home page 1](/images/image_2.png)
![Home page 2](/images/image_1.png)

## Checkout ##
![Checkout](/images/image_3.png)

## Stripe Payment ##
![Checkout](/images/image_5.png)

