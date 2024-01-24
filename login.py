import json
import requests
import time



# gets the user statistics using their username
def getUserStats(username):
    print("getUserStats:")
    print(username)
    # headers = {
    #     "Authorization": "Bearer " + main.access_token,
    #     "Accept": "application/json",
    #     "Content-Type": "application/json",
    # }
    query = '''
        query ($name: String) {
            User(name: $name) {
                id
                name
                about
                statistics {
                    anime {
                        count
                        meanScore
                        minutesWatched
                        episodesWatched
                        statuses {
                            status
                            count
                        }
                        genres(sort: COUNT_DESC) {
                            genre
                            count
                        }
                        tags(sort: COUNT_DESC) {
                            tag {
                                name
                            }
                            count
                        }
                    }
                }
            }
        }
    '''

    url = 'https://graphql.anilist.co'

    variables = {
        'name': username
    }

    response = requests.post(
        url, json={"query": query, "variables": variables}
    )
    if response.status_code == 429:
        wait_time = int(response.headers.get('retry-after', 0))
        time.sleep(wait_time + 1)

    else:
        response.raise_for_status()

        # wait a bit to not overload AniList API
        time.sleep(0.20)
        return response.json()



# gets the user's anime list from the id found in get user list
def getUserAnimeList(userID):
    print("getUserAnimeList: ")
    print(userID)
    query = """\
      query ($user_id: Int, $page: Int = 1, $per_page: Int = 25) 
      {
       anime: Page(page: $page, perPage: $per_page) 
       {
           pageInfo 
           {
               total
               currentPage
               lastPage
           }
           mediaList(userId: $user_id, sort: UPDATED_TIME_DESC, type: ANIME) 
           {
               id
               status
               score(format: POINT_100)
               progress
               repeat
               priority
               startedAt 
               {
                   year
                   month
                   day
               }
               completedAt 
               {
                   year
                   month
                   day
               }
               updatedAt
               createdAt
               media 
               {
                   type
                   id
                   title 
                   {
                       romaji
                       english
                       native
                   }
                    staff(sort: FAVOURITES_DESC) {
                        edges {
                             node {
                                name {
                                    first
                                    full
                                    native
                                    last
                                }
                            id
                        }
                        role
                    }
                    }
                   siteUrl
                   episodes
                   description
                   format
                   status
                   duration
                   genres
                   isAdult
                   tags 
                   {
                       name
                   }
                   studios 
                   {
                       nodes 
                       {
                           name
                       }
                   }
                   startDate 
                   {
                       year
                       month
                       day
                   }
                   endDate 
                   {
                       year
                       month
                       day
                   }
                   season
                   seasonYear
                   seasonInt
                   countryOfOrigin
                   coverImage 
                   {
                       medium
                       large
                       extraLarge
                   }
                   bannerImage
                   source
                   hashtag
                   synonyms
                   meanScore
                   averageScore
                   popularity
                   rankings 
                   {
                       type
                       allTime
                       format
                       rank
                       year
                       season
                   }
                   nextAiringEpisode 
                   {
                       timeUntilAiring
                       airingAt
                       episode
                   }
                   trailer 
                   {
                       id
                       thumbnail
                       site
                   }
               }
           }
       }
       }
       """

    url = 'https://graphql.anilist.co'

    variables = {
        'user_id': userID
    }
    response = requests.post(
        url,
        json={'query': query, 'variables': variables}
    )

    file = json.loads(response.text)

    # print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
    return file


# gets the user ID
def getUserID(username):
    print(getUserStats(username)["data"])
    userID = getUserStats(username)["data"]["User"]["id"]
    return userID
