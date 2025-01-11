import requests;

def repos_with_most_stars():
    search_url = "https://api.github.com/search/repositories"
    param = {"q" : "stars:>50000"}
    response = requests.get(search_url, params=param)
    response_json = response.json()["items"]
    #Just prints ouut the exact response that we got
    #print(response.text)
    #Need to convert to dictonary
    return response_json


if __name__ == "__main__":
    results = repos_with_most_stars()
    #print(len(results))
    for result in results:
        language = result["language"]
        stars = result["stargazers_count"]
        name = result["name"]
        print(name, " is a ", language, " repo with ", stars, " stars")