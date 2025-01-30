Business Lookup Tool for Licensing and Compliance
This project is a Streamlit-based tool designed for the Directorate of Licensing and Compliance to assist billers in accurately assigning business categories, calculating charges, and ensuring the correct processing of business licenses. The tool supports easy lookup of business categories and their corresponding charges based on location and size. It is optimized for use by billers and can be accessed via a web interface on both desktop and mobile devices.

Features
Business Lookup: Billers can input a business category and instantly retrieve the relevant information, including charges based on location (CBD, Estates, Townships) and business size (Large, Medium, Small).
Dynamic Search: The tool dynamically matches the entered business category with available options and displays the results.
User-friendly Interface: The tool is designed for simplicity, providing a clean interface for quick searches.
County Branding: The app includes the county logo and is customized to reflect the official branding.
Responsive: Optimized for use on both desktop and mobile devices for billers to access on the go.
Installation
Prerequisites
Before running this tool, ensure you have the following installed:

Python (version 3.7 or higher)
Streamlit
pandas
Installing Dependencies
Install Streamlit: If you don't have Streamlit installed, you can install it using pip:

bash
Copy
Edit
pip install streamlit
Install pandas: If pandas is not installed, use pip to install it as well:

bash
Copy
Edit
pip install pandas
Additional Libraries: You may also need additional libraries depending on your requirements (e.g., numpy for numeric operations, matplotlib for plotting). You can install them using pip as needed.

Clone the Repository
Clone the repository to your local machine:

bash
Copy
Edit
git clone https://github.com/your-username/business-lookup-tool.git
cd business-lookup-tool
Running the App
To run the app, navigate to the project directory and use the following command:

bash
Copy
Edit
streamlit run business_lookup_tool.py
This will start the Streamlit app and open it in your default browser. You should now be able to interact with the tool.

Features and Functionality
Welcome Screen: When you start the tool, a welcome message from the Directorate of Licensing and Compliance will be displayed.

Business Category Input: You can enter a business category (e.g., Butchery, Car Wash, etc.), and the tool will display matching records with corresponding business size (Large, Medium, Small), location (CBD, Estates, Townships), and charge.

Responsive Interface: The app adjusts to the size of the screen, ensuring it's accessible from both desktop and mobile devices.

Search Results: The results are displayed in a table format that includes the following columns:

Code: The business code.
Business Category: The name or description of the business.
Size: The size of the business (Large, Medium, Small).
Location: The location where the business operates (CBD, Estates, Townships).
Charge: The charge corresponding to the business category and location.
Configuration
The app uses a .streamlit/config.toml file to configure the appearance and theme of the app. The file contains settings for:

Theme: Light mode with a white background.
Colors: Custom primary and background colors.
Layout: Centered content for a cleaner user interface.
You can adjust these settings in the config.toml file to suit your branding or aesthetic preferences.

Customizing the Tool
If you wish to add more business categories or modify the pricing, simply update the business_categories.csv file in the project directory. The CSV file should include the following columns:

code: The unique code for the business category.
business category: The name or description of the business category.
location: The location of the business (CBD, Estates, Townships).
charge: The charge for the business category in the respective location.
Size: The size of the business (Large, Medium, Small).
Once you've made the necessary changes, reload the app to reflect the updates.

Deploying the App
You can deploy the Streamlit app using various platforms like:

Streamlit Cloud: Upload your app to Streamlit Cloud for easy sharing.
Heroku: Deploy your Streamlit app on Heroku for a more robust solution.
AWS/GCP: For advanced deployment, you can host the app on cloud platforms like AWS or Google Cloud.
Contributing
Feel free to fork the repository and make contributions! If you find a bug or have suggestions for improvements, please open an issue or submit a pull request.

License
This project is licensed under the MIT License - see the LICENSE file for details.
