from flask import Flask, request

app = Flask(__name__)

climates = {
    94538: "cloudy, 25°C",
    94539: "sunny, 25°C",
    94540: "windy, 26°C",
    94541: "rainy, 22°C",
    94542: "warmer, 20°C"
}

@app.route("/climate", methods=["GET"])
def get_climate():
    zipcode = request.args.get("zipcode")
    if zipcode:
        zipcode = int(zipcode)
        climate = climates.get(zipcode)
        if climate:
            return "The climate in the zipcode {} is {}".format(zipcode, climate)
        else:
            return "Climate information for the zipcode {} not found".format(zipcode)
    else:
        return "Zipcode not provided"

if __name__ == '__main__':
    app.run()