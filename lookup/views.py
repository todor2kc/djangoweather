from django.shortcuts import render

def home(request):
    import json
    import requests

    if request.method == "POST":
        zipcode = request.POST['zipcode']
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zipcode + "&distance=5&API_KEY=A9E82420-2A6A-4890-ABE9-74714FD6CC8A")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "error.."

        if api[0]["Category"]["Name"] == "Good":
            category_description = "0 - 50 Good"
            category_color = "good"
        elif api[0]["Category"]["Name"] == "Moderate":
            category_description = "51 - 100 Moderate"
            category_color = "moderate"
        elif api[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
            category_description = "101 - 150 Unhealthy for Sensitive Groups (USG)"
            category_color = "usg"
        elif api[0]["Category"]["Name"] == "Unhealthy":
            category_description = "151 - 200 Unhealthy"
            category_color = "unhealthy"
        elif api[0]["Category"]["Name"] == "Very Unhealthy":
            category_description = "201 - 300 Very Unhealthy"
            category_color = "veryunhealthy"
        elif api[0]["Category"]["Name"] == "Hazardous":
            category_description = "301 - 500 Hazardous"
            category_color = "hazardous"

        return render(request, 'home.html', {
            "api": api, 
            "category_description": category_description, 
            "category_color": category_color 
            }) # ovde moze da ide dictionery
    else:
        api_request = requests.get("https://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=89129&distance=5&API_KEY=A9E82420-2A6A-4890-ABE9-74714FD6CC8A")
        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "error.."

        if api[0]["Category"]["Name"] == "Good":
            category_description = "0 - 50 Good"
            category_color = "good"
        elif api[0]["Category"]["Name"] == "Moderate":
            category_description = "51 - 100 Moderate"
            category_color = "moderate"
        elif api[0]["Category"]["Name"] == "Unhealthy for Sensitive Groups":
            category_description = "101 - 150 Unhealthy for Sensitive Groups (USG)"
            category_color = "usg"
        elif api[0]["Category"]["Name"] == "Unhealthy":
            category_description = "151 - 200 Unhealthy"
            category_color = "unhealthy"
        elif api[0]["Category"]["Name"] == "Very Unhealthy":
            category_description = "201 - 300 Very Unhealthy"
            category_color = "veryunhealthy"
        elif api[0]["Category"]["Name"] == "Hazardous":
            category_description = "301 - 500 Hazardous"
            category_color = "hazardous"

        return render(request, 'home.html', {
            "api": api, 
            "category_description": category_description, 
            "category_color": category_color 
            }) # ovde moze da ide dictionery


def about(request):
    return render(request, 'about.html', {})