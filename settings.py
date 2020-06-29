# *************** Sqlite3 Database Configuration *****************************
TRACK_WORDS = ["#coronavirus"]
TABLE_NAME = "Twitter_covid19"
TABLE_ATTRIBUTES = "id_str VARCHAR(255), created_at DATETIME, text VARCHAR(255), \
                    user_location VARCHAR(255), longitude DOUBLE, latitude DOUBLE,sentiment VARCHAR(255), \
                     label VARCHAR(255)"
# ************************* Model Configuration ****************************

Model = "Model/SVM_model.pkl"

# ************************ API Configuration *******************************
ACCESS_TOEKN = "890424087021060097-GHgnuIOcPYV7bgSS7aLEwTy87OddQwb"
ACCESS_TOKEN_SECRET = "8M0cWYlImUH2Z9EmRDSX2eObUuYgL4jgvovT58UAWaPEW"
API_KEY = "I1j1R1UPs4O9rsUZB3sgHeAIr"
API_SECRET_KEY = "9K29IY4ZFx7NEsfkls9MSo77O2IYitmqi4U80KksDHH5DfMuSB"
GOOGLE_API_KEY = "AIzaSyB-6fHe6PiWisRDD1zRnuRKbiypE5ufMqA"
