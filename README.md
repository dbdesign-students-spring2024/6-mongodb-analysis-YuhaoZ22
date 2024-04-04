# Data Analysis Report on Airbnb Listings in Columbus, Ohio

## Part 1: Data Selection and Import

### Data Source

This report utilizes Airbnb data for Columbus, Ohio, USA, for the year 2023. The dataset, sourced in CSV format, was obtained from [Inside Airbnb](https://insideairbnb.com/get-the-data), which provides detailed datasets for Airbnb listings across various locations worldwide.

### Raw Data

The dataset contains detailed information about Airbnb listings in Columbus, including identifiers, listing URLs, names, host details, and various metrics related to the listings' quality and guest experiences. Here's a glimpse at the first few rows of the dataset:

| id      | listing_url                                | scrape_id      | last_scraped | source     | ... | reviews_per_month |
|---------|--------------------------------------------|----------------|--------------|------------|-----|-------------------|
| 90676   | [Link](https://www.airbnb.com/rooms/90676) | 20231225202549| 2023-12-26   | city scrape| ... | 4.88              |
| 543140  | [Link](https://www.airbnb.com/rooms/543140)| 20231225202549| 2023-12-25   | city scrape| ... | 0.96              |
| 591101  | [Link](https://www.airbnb.com/rooms/591101)| 20231225202549| 2023-12-26   | city scrape| ... | 2.14              |
| 923248  | [Link](https://www.airbnb.com/rooms/923248) | 20231225202549| 2023-12-25   | city scrape| ... | 2.64              |
| 927867  | [Link](https://www.airbnb.com/rooms/927867) | 20231225202549| 2023-12-25   | city scrape| ... | 0.61              |
| 1183297 | [Link](https://www.airbnb.com/rooms/1183297)| 20231225202549| 2023-12-26   | city scrape| ... | 3.12              |
| 1217678 | [Link](https://www.airbnb.com/rooms/1217678)| 20231225202549| 2023-12-25   | city scrape| ... | 1.82              |
| 1286887 | [Link](https://www.airbnb.com/rooms/1286887)| 20231225202549| 2023-12-26   | city scrape| ... | 1.42              |
| 1336145 | [Link](https://www.airbnb.com/rooms/1336145)| 20231225202549| 2023-12-25   | city scrape| ... | 1.43              |



(Note: The table is truncated for brevity.)

### Data Scrubbing

[Raw Data](data/listings.csv)

[Clean Data](data/listings_clean.csv)

The data scrubbing process included several modifications to prepare the dataset for analysis:

- **Deleted Empty Columns:** Columns such as `description`, `neighbourhood_group_cleansed`, `bedrooms` and `calendar_updated` were removed due to being empty or containing redundant information.
- **Transfer `t/f` to `YES/No`**: Make it more easier to be understood 

The cleaned dataset, named `listings_clean.csv`, was optimized for database import and analysis.

## Part 2: Data Analysis in MongoDB
1. show exactly two documents from the `listings` collection in any order.

```
db.listings.find().limit(2)
```
Outputs:

```
[
  {
    _id: ObjectId('660e4b23b6515eb2057e1bc7'),
    id: 90676,
    listing_url: 'https://www.airbnb.com/rooms/90676',
    scrape_id: Long('20231225202549'),
    last_scraped: '2023-12-26',
    source: 'city scrape',
    name: 'Home in Columbus · ★4.82 · 3 bedrooms · 3 beds · 2 baths',
    neighborhood_overview: "The Short North Italianate Cottage is located in the Short North/ Italian Village neighborhood. Italian Village offers a plethora of breweries, coffee shops, and restaurants tucked within the neighborhood boarders and the Short North is a mile of Columbus's best art galleries, restaurants, nightlife, pubs, and shops! Less than a mile to OSU!!!",
    picture_url: 'https://a0.muscache.com/pictures/950e43cd-53f3-4f6a-8c36-cb123b5580f4.jpg',
    host_id: 483306,
    host_url: 'https://www.airbnb.com/users/show/483306',
    host_name: 'Audra & Lacey',
    host_since: '2011-04-04',
    host_location: 'Columbus, OH',
    host_about: 'Active, young professionals who love to travel and socialize! Audra loves to run, workout, and sip on adult beverages. \n' +
      'Lacey loves to workout, check out local music & restaurants, and rescue any stray animal she sees. \n',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'YES',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/483306/profile_pic/1413761624/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/483306/profile_pic/1413761624/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 3,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone', 'work_email']",
    host_has_profile_pic: 'YES',
    host_identity_verified: 'YES',
    neighbourhood: 'Columbus, Ohio, United States',
    neighbourhood_cleansed: 'Near North/University',
    latitude: 39.98366,
    longitude: -83.00252,
    property_type: 'Entire home',
    room_type: 'Entire home/apt',
    accommodates: 6,
    bathrooms: '',
    bathrooms_text: '2 baths',
    beds: 3,
    amenities: '[]',
    price: '$132.00',
    minimum_nights: 1,
    maximum_nights: 365,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 1,
    minimum_maximum_nights: 365,
    maximum_maximum_nights: 365,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 365,
    has_availability: 'YES',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    calendar_last_scraped: '2023-12-26',
    number_of_reviews: 726,
    number_of_reviews_ltm: 101,
    number_of_reviews_l30d: 9,
    first_review: '2011-10-11',
    last_review: '2023-12-17',
    review_scores_rating: 4.82,
    review_scores_accuracy: 4.85,
    review_scores_cleanliness: 4.82,
    review_scores_checkin: 4.93,
    review_scores_communication: 4.88,
    review_scores_location: 4.93,
    review_scores_value: 4.77,
    license: '2022-2475',
    instant_bookable: 'NO',
    calculated_host_listings_count: 3,
    calculated_host_listings_count_entire_homes: 3,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 4.88
  },
  {
    _id: ObjectId('660e4b23b6515eb2057e1bc8'),
    id: 543140,
    listing_url: 'https://www.airbnb.com/rooms/543140',
    scrape_id: Long('20231225202549'),
    last_scraped: '2023-12-25',
    source: 'city scrape',
    name: 'Home in Columbus · ★4.70 · 1 bedroom · 1 bed · 1 shared bath',
    neighborhood_overview: 'We are close to a lot of things!',
    picture_url: 'https://a0.muscache.com/pictures/e720cdf0-e36b-45e0-b340-72ab94f97db1.jpg',
    host_id: 2350409,
    host_url: 'https://www.airbnb.com/users/show/2350409',
    host_name: 'Edward',
    host_since: '2012-05-11',
    host_location: 'Columbus, OH',
    host_about: 'Hello, hello.\n' +
      '\n' +
      'About me: pretty easy going, basically.\n' +
      'Hobbies include gardening, woodworking, running, boxing, science, writing, photography, and some others.\n' +
      '\n' +
      'That is all.',
    host_response_time: 'within an hour',
    host_response_rate: '90%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'YES',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/7d46ebbe-c34a-46ff-b688-9243f44c4114.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/7d46ebbe-c34a-46ff-b688-9243f44c4114.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 3,
    host_total_listings_count: 4,
    host_verifications: "['email', 'phone', 'work_email']",
    host_has_profile_pic: 'YES',
    host_identity_verified: 'NO',
    neighbourhood: 'Columbus, Ohio, United States',
    neighbourhood_cleansed: 'Near North/University',
    latitude: 40.01114,
    longitude: -83.01005,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1 shared bath',
    beds: 1,
    amenities: '[]',
    price: '$29.00',
    minimum_nights: 7,
    maximum_nights: 1125,
    minimum_minimum_nights: 7,
    maximum_minimum_nights: 7,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 7,
    maximum_nights_avg_ntm: 1125,
    has_availability: 'YES',
    availability_30: 16,
    availability_60: 25,
    availability_90: 52,
    availability_365: 327,
    calendar_last_scraped: '2023-12-25',
    number_of_reviews: 133,
    number_of_reviews_ltm: 10,
    number_of_reviews_l30d: 1,
    first_review: '2012-07-31',
    last_review: '2023-12-09',
    review_scores_rating: 4.7,
    review_scores_accuracy: 4.75,
    review_scores_cleanliness: 4.33,
    review_scores_checkin: 4.93,
    review_scores_communication: 4.89,
    review_scores_location: 4.77,
    review_scores_value: 4.79,
    license: '2019-1344',
    instant_bookable: 'NO',
    calculated_host_listings_count: 3,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 3,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.96
  }
]
```

2. Show exactly 10 documents in any order, but "prettyprint" in easier to read format, using the pretty() function.
```
db.listings.find().limit(10).pretty()
```

```
[
  {
    _id: ObjectId('660e4b23b6515eb2057e1bc7'),
    id: 90676,
    listing_url: 'https://www.airbnb.com/rooms/90676',
    scrape_id: Long('20231225202549'),
    last_scraped: '2023-12-26',
    source: 'city scrape',
    name: 'Home in Columbus · ★4.82 · 3 bedrooms · 3 beds · 2 baths',
    neighborhood_overview: "The Short North Italianate Cottage is located in the Short North/ Italian Village neighborhood. Italian Village offers a plethora of breweries, coffee shops, and restaurants tucked within the neighborhood boarders and the Short North is a mile of Columbus's best art galleries, restaurants, nightlife, pubs, and shops! Less than a mile to OSU!!!",
    picture_url: 'https://a0.muscache.com/pictures/950e43cd-53f3-4f6a-8c36-cb123b5580f4.jpg',
    host_id: 483306,
    host_url: 'https://www.airbnb.com/users/show/483306',
    host_name: 'Audra & Lacey',
    host_since: '2011-04-04',
    host_location: 'Columbus, OH',
    host_about: 'Active, young professionals who love to travel and socialize! Audra loves to run, workout, and sip on adult beverages. \n' +
      'Lacey loves to workout, check out local music & restaurants, and rescue any stray animal she sees. \n',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'YES',
    host_thumbnail_url: 'https://a0.muscache.com/im/users/483306/profile_pic/1413761624/original.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/users/483306/profile_pic/1413761624/original.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 3,
    host_total_listings_count: 3,
    host_verifications: "['email', 'phone', 'work_email']",
    host_has_profile_pic: 'YES',
    host_identity_verified: 'YES',
    neighbourhood: 'Columbus, Ohio, United States',
    neighbourhood_cleansed: 'Near North/University',
    latitude: 39.98366,
    longitude: -83.00252,
    property_type: 'Entire home',
    room_type: 'Entire home/apt',
    accommodates: 6,
    bathrooms: '',
    bathrooms_text: '2 baths',
    beds: 3,
    amenities: '[]',
    price: '$132.00',
    minimum_nights: 1,
    maximum_nights: 365,
    minimum_minimum_nights: 1,
    maximum_minimum_nights: 1,
    minimum_maximum_nights: 365,
    maximum_maximum_nights: 365,
    minimum_nights_avg_ntm: 1,
    maximum_nights_avg_ntm: 365,
    has_availability: 'YES',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    calendar_last_scraped: '2023-12-26',
    number_of_reviews: 726,
    number_of_reviews_ltm: 101,
    number_of_reviews_l30d: 9,
    first_review: '2011-10-11',
    last_review: '2023-12-17',
    review_scores_rating: 4.82,
    review_scores_accuracy: 4.85,
    review_scores_cleanliness: 4.82,
    review_scores_checkin: 4.93,
    review_scores_communication: 4.88,
    review_scores_location: 4.93,
    review_scores_value: 4.77,
    license: '2022-2475',
    instant_bookable: 'NO',
    calculated_host_listings_count: 3,
    calculated_host_listings_count_entire_homes: 3,
    calculated_host_listings_count_private_rooms: 0,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 4.88
  },
  {
    _id: ObjectId('660e4b23b6515eb2057e1bc8'),
    id: 543140,
    listing_url: 'https://www.airbnb.com/rooms/543140',
    scrape_id: Long('20231225202549'),
    last_scraped: '2023-12-25',
    source: 'city scrape',
    name: 'Home in Columbus · ★4.70 · 1 bedroom · 1 bed · 1 shared bath',
    neighborhood_overview: 'We are close to a lot of things!',
    picture_url: 'https://a0.muscache.com/pictures/e720cdf0-e36b-45e0-b340-72ab94f97db1.jpg',
    host_id: 2350409,
    host_url: 'https://www.airbnb.com/users/show/2350409',
    host_name: 'Edward',
    host_since: '2012-05-11',
    host_location: 'Columbus, OH',
    host_about: 'Hello, hello.\n' +
      '\n' +
      'About me: pretty easy going, basically.\n' +
      'Hobbies include gardening, woodworking, running, boxing, science, writing, photography, and some others.\n' +
      '\n' +
      'That is all.',
    host_response_time: 'within an hour',
    host_response_rate: '90%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'YES',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/7d46ebbe-c34a-46ff-b688-9243f44c4114.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/7d46ebbe-c34a-46ff-b688-9243f44c4114.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 3,
    host_total_listings_count: 4,
    host_verifications: "['email', 'phone', 'work_email']",
    host_has_profile_pic: 'YES',
    host_identity_verified: 'NO',
    neighbourhood: 'Columbus, Ohio, United States',
    neighbourhood_cleansed: 'Near North/University',
    latitude: 40.01114,
    longitude: -83.01005,
    property_type: 'Private room in home',
    room_type: 'Private room',
    accommodates: 1,
    bathrooms: '',
    bathrooms_text: '1 shared bath',
    beds: 1,
    amenities: '[]',
    price: '$29.00',
    minimum_nights: 7,
    maximum_nights: 1125,
    minimum_minimum_nights: 7,
    maximum_minimum_nights: 7,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 7,
    maximum_nights_avg_ntm: 1125,
    has_availability: 'YES',
    availability_30: 16,
    availability_60: 25,
    availability_90: 52,
    availability_365: 327,
    calendar_last_scraped: '2023-12-25',
    number_of_reviews: 133,
    number_of_reviews_ltm: 10,
    number_of_reviews_l30d: 1,
    first_review: '2012-07-31',
    last_review: '2023-12-09',
    review_scores_rating: 4.7,
    review_scores_accuracy: 4.75,
    review_scores_cleanliness: 4.33,
    review_scores_checkin: 4.93,
    review_scores_communication: 4.89,
    review_scores_location: 4.77,
    review_scores_value: 4.79,
    license: '2019-1344',
    instant_bookable: 'NO',
    calculated_host_listings_count: 3,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 3,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 0.96
  },
  {
    _id: ObjectId('660e4b23b6515eb2057e1bc9'),
    id: 591101,
    listing_url: 'https://www.airbnb.com/rooms/591101',
    scrape_id: Long('20231225202549'),
    last_scraped: '2023-12-26',
    source: 'city scrape',
    name: 'Loft in Columbus · ★4.92 · 1 bedroom · 1 bed · 1 private bath',
    neighborhood_overview: 'A historic neighborhood of beautiful victorian homes on lovely tree lined streets, located just a short walk from the downtown, the Main Library, Art Museum and Topiary Park (great for walking or jogging).  <br />There are plenty of places to eat, drink and have fun only a few steps away ( coffee house, pizza parlor, tavern, restaurant, brewery and more.)',
    picture_url: 'https://a0.muscache.com/pictures/32b28442-ddf3-435d-8135-a504b86ff23a.jpg',
    host_id: 2889677,
    host_url: 'https://www.airbnb.com/users/show/2889677',
    host_name: 'Gail',
    host_since: '2012-07-10',
    host_location: 'Columbus, OH',
    host_about: "My husband Eric and I are both artists, sharing studio space in our house. We have 2 daughters and 3 grandchildren, all of whom live in Columbus.  I've been a yoga teacher since 1988. I have taught at Yoga on High since it's inception in 2000 and earned my certification from Yoga Alliance of ERYT 1500 at Yoga on High. I love sharing this ancient practice with all kinds of people. I have seen it have profound effects on people's lives. It is an honor and a responsibility for which I am very grateful. \n" +
      ' Eric and I have lived in this historic home for over 35 years, in what we consider the best neighborhood in the city, Olde Towne. We love sharing our home with friends and now airbnb guests. We enjoy walking in the woods, gardening, biking, kayaking, reading and, of course, practicing yoga. \n' +
      "We also love to travel. We've been told we are easy guests. We like to take care of ourselves and not add unduly to our hosts workload. Car camping is a favorite vacation of ours.\n" +
      " I'd say our airbnb hosting style is also casual: I try to think of anything a guest might need and supply it, so they can have a relaxed stay with us. We have maps of the neighborhood and menus for the local cafes and the bakery in a notebook in The Loft. We try to help out with rides when we can. We have a table in The Loft that is perfect for working or dining. A guest set up her sewing machine up there.\n" +
      'My favorite quote is from Emmanuel: "Your life is not your master, it is your child." Let us host your next visit to Columbus as you create your perfect visit.',
    host_response_time: 'within an hour',
    host_response_rate: '100%',
    host_acceptance_rate: '100%',
    host_is_superhost: 'YES',
    host_thumbnail_url: 'https://a0.muscache.com/im/pictures/user/e7975b19-3cbd-4f4d-9f34-340eaaf9e0aa.jpg?aki_policy=profile_small',
    host_picture_url: 'https://a0.muscache.com/im/pictures/user/e7975b19-3cbd-4f4d-9f34-340eaaf9e0aa.jpg?aki_policy=profile_x_medium',
    host_neighbourhood: '',
    host_listings_count: 1,
    host_total_listings_count: 1,
    host_verifications: "['email', 'phone']",
    host_has_profile_pic: 'YES',
    host_identity_verified: 'NO',
    neighbourhood: 'Columbus, Ohio, United States',
    neighbourhood_cleansed: 'Near East',
    latitude: 39.96041,
    longitude: -82.98005,
    property_type: 'Private room in loft',
    room_type: 'Private room',
    accommodates: 2,
    bathrooms: '',
    bathrooms_text: '1 private bath',
    beds: 1,
    amenities: '[]',
    price: '$110.00',
    minimum_nights: 2,
    maximum_nights: 30,
    minimum_minimum_nights: 2,
    maximum_minimum_nights: 2,
    minimum_maximum_nights: 1125,
    maximum_maximum_nights: 1125,
    minimum_nights_avg_ntm: 2,
    maximum_nights_avg_ntm: 1125,
    has_availability: 'YES',
    availability_30: 0,
    availability_60: 0,
    availability_90: 0,
    availability_365: 0,
    calendar_last_scraped: '2023-12-26',
    number_of_reviews: 296,
    number_of_reviews_ltm: 19,
    number_of_reviews_l30d: 0,
    first_review: '2012-08-10',
    last_review: '2023-11-12',
    review_scores_rating: 4.92,
    review_scores_accuracy: 4.93,
    review_scores_cleanliness: 4.93,
    review_scores_checkin: 4.96,
    review_scores_communication: 4.91,
    review_scores_location: 4.89,
    review_scores_value: 4.88,
    license: '2019-1230',
    instant_bookable: 'NO',
    calculated_host_listings_count: 1,
    calculated_host_listings_count_entire_homes: 0,
    calculated_host_listings_count_private_rooms: 1,
    calculated_host_listings_count_shared_rooms: 0,
    reviews_per_month: 2.14
  }
]
```


3.Choose two hosts (by reffering to their host_id values) who are superhosts (available in the host_is_superhost field), and show all of the listings offered by both of the two hosts.
Hosts I chose: the two whose host_id are (6466841, 10776491)
```
db.listings.find(
  {
    host_is_superhost: "YES",
    host_id: { $in: [6466841, 10776491] }
  },
  {
    _id: 0,
    name: 1,
    price: 1,
    neighbourhood: 1,
    host_name: 1,
    host_is_superhost: 1
  }
)
```
Outputs:
```
[
  {
    name: 'Home in Columbus · ★4.90 · 3 bedrooms · 4 beds · 2.5 baths',
    host_name: 'Catherine & Bryan',
    host_is_superhost: 'YES',
    neighbourhood: 'Columbus, Ohio, United States',
    price: '$181.00'
  },
  {
    name: 'Townhouse in Columbus · ★4.89 · 2 bedrooms · 2 beds · 2.5 baths',
    host_name: 'Catherine & Bryan',
    host_is_superhost: 'YES',
    neighbourhood: 'Columbus, Ohio, United States',
    price: '$190.00'
  },
  {
    name: 'Townhouse in Columbus · ★4.89 · 2 bedrooms · 2 beds · 2.5 baths',
    host_name: 'Catherine & Bryan',
    host_is_superhost: 'YES',
    neighbourhood: 'Columbus, Ohio, United States',
    price: '$193.00'
  },
  {
    name: 'Home in Columbus · ★4.85 · 4 bedrooms · 4 beds · 5 baths',
    host_name: 'Catherine & Bryan',
    host_is_superhost: 'YES',
    neighbourhood: 'Columbus, Ohio, United States',
    price: '$483.00'
  }
]
```

4. find all the unique host_name values

```
db.listings.distinct("host_name")
```
Output:
```
[
  '50 Lincoln',
  'Aamna',
  'Aaron',
  'Aba',
  'Abbie',
  'Abel',
  'Abeselom',
  'Abigail',
  'Abigail & HomeTeam Vacation Rentals',
  'Abraham',
  'Ad',
  'Adam',
  'Adam And Jaime',
  'Adekunle',
  'Adellina',
  'Adrian',
  'Adriana',
  'Advent',
  'Aerial',
  'Ahmed',
  'Aisa',
  'Aishia',
  'Akhil',
  'Akin',
  'Al',
  'Alan',
  'Alberto',
  'Alex',
  'Alexander',
  'Alexandra',
  'Alexandrea',
  'Alexandro',
  'Alissa',
  'Alix',
  'Aliza',
  'Allan',
  'Allison',
  'Alyssa',
  'Amadou',
  'Amanda',
  'Amber',
  'Amie',
  'Amina',
  'Amir',
  'Amy',
  'Amy And Kevin',
  'Andora',
  'Andrew',
  'Andy',
  'Anereis',
  'Angelica',
  'Angelo',
  'Angie And Sonia',
  'Anh',
  'Anica',
  'Anita',
  'Anna',
  'Anne',
  'Annette And TJ',
  'Annie',
  'Anthony',
  'Anton',
  'April',
  'Aregai',
  'Ariana',
  'Arleigh',
  'Arman',
  'Ashlee',
  'Ashleigh',
  'Ashley',
  'Ashley And Clint',
  'Asia',
  'Audra & Lacey',
  'August',
  'Avishkar',
  'Aziza',
  'Babatunde',
  'Bailee',
  'Barbara',
  'Beau',
  'Bella',
  'Ben',
  'Ben & Melissa',
  'Benjamin',
  'Benson',
  'Bernard',
  'Beth',
  'Bianca',
  'Bill',
  'Billy',
  'BlackFrog',
  'Bob',
  'Bob And Abby',
  'Bonnie',
  'Boris',
  'Bracken Ridge',
  'Brad',
  'Bradley',
  'Brandon',
  'Brandy',
  ... 620 more items
]
```

5.Find all of the places that have more than 2 beds in a neighborhood of your choice (referred to as either the neighborhood or neighbourhood_group_cleansed fields in the data file), ordered by review_scores_rating descending.

```mongodb
db.listings.find(
  {
    beds: { $gt: 2 },
    neighbourhood_cleansed: "Near North/University"
  },
  {
    _id: 0,
    name: 1,
    beds: 1,
    review_scores_rating: 1,
    price: 1
  }
).sort({ review_scores_rating: -1 })
```
Output:
```
[
  {
    name: 'Home in Columbus · 3 bedrooms · 3 beds · 1 bath',
    beds: 3,
    price: '$99.00',
    review_scores_rating: ''
  },
  {
    name: 'Loft in Columbus · 3 bedrooms · 7 beds · 2 baths',
    beds: 7,
    price: '$182.00',
    review_scores_rating: ''
  },
  {
    name: 'Townhouse in Columbus · 2 bedrooms · 4 beds · 2 baths',
    beds: 4,
    price: '$286.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · 3 bedrooms · 3 beds · 1 bath',
    beds: 3,
    price: '$118.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · 3 bedrooms · 3 beds · 2.5 baths',
    beds: 3,
    price: '$225.00',
    review_scores_rating: ''
  },
  {
    name: 'Townhouse in Columbus · 3 bedrooms · 3 beds · 1 bath',
    beds: 3,
    price: '$192.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · 2 bedrooms · 6 beds · 2 baths',
    beds: 6,
    price: '$126.00',
    review_scores_rating: ''
  },
  {
    name: 'Rental unit in Columbus · 2 bedrooms · 3 beds · 1 bath',
    beds: 3,
    price: '$165.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · 3 bedrooms · 4 beds · 2 baths',
    beds: 4,
    price: '$250.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · 3 bedrooms · 3 beds · 1.5 baths',
    beds: 3,
    price: '$120.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · 3 bedrooms · 3 beds · 2 baths',
    beds: 3,
    price: '$124.00',
    review_scores_rating: ''
  },
  {
    name: 'Townhouse in Columbus · 6 bedrooms · 7 beds · 2.5 baths',
    beds: 7,
    price: '$293.00',
    review_scores_rating: ''
  },
  {
    name: 'Townhouse in Columbus · ★New · 3 bedrooms · 3 beds · 2 baths',
    beds: 3,
    price: '$298.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · 4 bedrooms · 5 beds · 3.5 baths',
    beds: 5,
    price: '$165.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · 5 bedrooms · 6 beds · 3 baths',
    beds: 6,
    price: '$769.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · 4 bedrooms · 11 beds · 3.5 baths',
    beds: 11,
    price: '$989.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · 3 bedrooms · 3 beds · 2.5 baths',
    beds: 3,
    price: '$263.00',
    review_scores_rating: ''
  },
  {
    name: 'Rental unit in Columbus · ★New · 4 bedrooms · 4 beds · 1 bath',
    beds: 4,
    price: '$135.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · ★New · 4 bedrooms · 12 beds · 4 baths',
    beds: 12,
    price: '$265.00',
    review_scores_rating: ''
  },
  {
    name: 'Home in Columbus · ★New · 5 bedrooms · 5 beds · 2.5 baths',
    beds: 5,
    price: '$149.00',
    review_scores_rating: ''
  }
]
```


6. show the number of listings per host
```
db.listings.aggregate([
  {
    $group: {
      _id: "$host_id",
      host_name: { $first: "$host_name" },
      number_of_listings: { $sum: 1 }
    }
  },
  {
    $project: {
      _id: 0,
      host_id: "$_id",
      host_name: 1,
      number_of_listings: 1
    }
  }
])
```

```
[
  { host_name: 'Rashed', number_of_listings: 1, host_id: 552434649 },
  { host_name: 'Sadio', number_of_listings: 1, host_id: 390404025 },
  { host_name: 'Em', number_of_listings: 1, host_id: 165216442 },
  { host_name: 'Janet', number_of_listings: 1, host_id: 550835820 },
  { host_name: 'Davide', number_of_listings: 1, host_id: 3932716 },
  { host_name: 'Khari', number_of_listings: 1, host_id: 168776178 },
  {
    host_name: 'Kelly And Jennifer',
    number_of_listings: 4,
    host_id: 22716273
  },
  { host_name: 'Avishkar', number_of_listings: 1, host_id: 180557196 },
  {
    host_name: 'Elliot & Home Team Vacation Rentals',
    number_of_listings: 2,
    host_id: 117085097
  },
  { host_name: 'Tammy', number_of_listings: 1, host_id: 418589032 },
  { host_name: 'Joshua', number_of_listings: 1, host_id: 110350460 },
  { host_name: 'Dawit', number_of_listings: 1, host_id: 546530918 },
  { host_name: 'Saravanan', number_of_listings: 1, host_id: 122358868 },
  { host_name: 'Andora', number_of_listings: 1, host_id: 275645688 },
  { host_name: 'Shannon', number_of_listings: 1, host_id: 18609556 },
  { host_name: 'Malachi', number_of_listings: 1, host_id: 520001894 },
  { host_name: 'Akhil', number_of_listings: 1, host_id: 376454213 },
  { host_name: 'Rupak', number_of_listings: 1, host_id: 6792229 },
  { host_name: 'Ellie', number_of_listings: 1, host_id: 397413106 },
  { host_name: 'Shreesha', number_of_listings: 1, host_id: 20418203 }
]
```


7. find the average `review_scores_rating` per neighborhood, and only show those that are `4` or above, sorted in descending order of rating.
```mongodb
db.listings.aggregate([
  { $group: { _id: "$neighbourhood_cleansed", averageRating: { $avg: "$review_scores_rating" } } },
  { $match: { averageRating: { $gte: 4 } } },
  { $sort: { averageRating: -1 } }
])
```
Outputs:
```
[
  { _id: 'Hayden Run', averageRating: 4.9725 },
  { _id: 'West Scioto', averageRating: 4.948 },
  { _id: 'Far South', averageRating: 4.945 },
  { _id: 'Rocky Fork-Blacklick', averageRating: 4.892083333333333 },
  { _id: 'Hilltop', averageRating: 4.872173913043478 },
  { _id: 'Far West', averageRating: 4.865 },
  { _id: 'West Olentangy', averageRating: 4.855555555555556 },
  { _id: 'Clintonville', averageRating: 4.8542708333333335 },
  { _id: 'Far North', averageRating: 4.851666666666667 },
  { _id: 'Far Northwest', averageRating: 4.843684210526316 },
  { _id: 'Franklinton', averageRating: 4.833050847457627 },
  { _id: 'Westland', averageRating: 4.8325 },
  { _id: 'Eastland/Brice', averageRating: 4.831764705882353 },
  { _id: 'Near East', averageRating: 4.801159420289855 },
  { _id: 'Northwest', averageRating: 4.800476190476191 },
  { _id: 'Near North/University', averageRating: 4.797562913907284 },
  { _id: 'North Linden', averageRating: 4.772156862745098 },
  { _id: 'Northland', averageRating: 4.761571428571429 },
  { _id: 'Eastmoor/Walnut Ridge', averageRating: 4.760545454545454 },
  { _id: 'Near South', averageRating: 4.758611111111111 }
]
```