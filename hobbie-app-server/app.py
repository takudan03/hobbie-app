from flask import Flask, request, render_template
from pymongo import MongoClient
import os

app = Flask(__name__)

try:

    # MongoDB Connection String
    # application.config["MONGO_URI"]='mongodb://' + os.environ['MONGODB_USERNAME'] + ':' + os.environ['MONGODB_PASSWORD'] + '@' + os.environ['MONGODB_HOSTNAME'] + ':27017/' + os.environ['MONGODB_DATABASE']    
    # app.config['MONGO_URI'] = os.getenv("MONGO_URI")
    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    # iF NO AUTH USE
    # client = MongoClient("mongodb://localhost:27017")

    # If there is auth, you can specify these as env variables and use:
    client = MongoClient(host=os.getenv("MONGO_URI"), username=os.getenv("MONGO_INITDB_ROOT_USERNAME"), password=os.getenv("MONGO_INITDB_ROOT_PASSWORD"))

    db = client.test
except:
    print("Error connecting to the DB")

existingEntries = []


@app.route("/",  methods=["GET", "POST"])
def hello():
    if request.method == "POST":
        # getting input from form using the specified IDs
        firstName = request.form.get("form-firstname")
        lastName = request.form.get("form-lastname")
        hobies = request.form.get("form-hobbies")

        # create JSON object with info to post to DB
        newDbEntry = {'firstName': firstName,
                      'lastName': lastName, 'hobbies': hobies}
        print(newDbEntry)
        try:
            result = db.myCollection.insert_one(newDbEntry)
            print(result)
            exitsingEntries = db.myCollection.find()
        except:
            print("Error posting to DB")
        return render_template("index.html", existingEntries=existingEntries)
    try:
        exitsingEntries = db.myCollection.find()
    except:
        print("Error retrieving existing entries")
    return render_template("index.html", existingEntries=existingEntries)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
