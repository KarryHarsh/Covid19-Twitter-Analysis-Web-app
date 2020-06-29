# *************** Sqlite3 Database Configuration *****************************
TRACK_WORDS = ["#coronavirus"]
TABLE_NAME = "Twitter_covid19"
TABLE_ATTRIBUTES = "id_str VARCHAR(255), created_at DATETIME, text VARCHAR(255), \
                    user_location VARCHAR(255), longitude DOUBLE, latitude DOUBLE,sentiment VARCHAR(255), \
                     label VARCHAR(255)"
# ************************* Model Configuration ****************************

Model = "Model/SVM_model.pkl"

# ************************ API Configuration *******************************
ACCESS_TOEKN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
ACCESS_TOKEN_SECRET = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
API_SECRET_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
GOOGLE_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
