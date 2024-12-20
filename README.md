# Visitor Experiences at Sepilok Orangutan Sanctuary: Sentiment Analysis

[![Static Badge](https://img.shields.io/badge/Back_to_Portfolio_Page-red?style=for-the-badge&logo=github&labelColor=black)](https://izzad2413.github.io/nazmirulizzadnassir.github.io/)

![Project Design Thumbnail-modified](https://github.com/user-attachments/assets/d212530f-8549-4570-9a8a-b30e7a00749b)

## Table of Contents 

- [Background Overview](#background-overview)
- [Problem Statement](#problem-statement)
- [Objective](#objective)
- [Built With](#built-with)
- [Data Source](#data-source)
- [Methodology](#methodology)
- [Result and Impact](#result-and-impact)
- [Challenges and Solutions](#challenges-and-solutions)
- [How to Use](#how-to-use)
- [Acknowledgement](#acknowledgement)

## Background Overview

Malaysia will be showcasing its sustainable and ecotourism offerings at Fitur 2023, with a focus on the state of Sabah as the prime representative of ecotourism in the country. The Malaysian Tourism Promotion Board, along with Dato' Akmal Che Mustafa, the Ambassador of Malaysia in Spain, and Ms Noredah Othman, CEO of Sabah Tourism, will present Malaysia's nature tourism, sustainable tourism, and slow travel options. Sabah, renowned for its tropical forests, coral reefs, and Mount Kinabalu, aims to provide an authentic ecotourism experience. Malaysia's National Ecotourism Plan emphasizes the protection, preservation, and conservation of nature, culture, and heritage, promoting respectful interactions between visitors and local communities. The country offers various ecotourism destinations, including Sepilok Orangutan Sanctuary, Mulu National Park, Belum Rainforest Resort, and Rantau Abang Turtle Hatchery, all recognized for their conservation efforts. With its rich biodiversity, Malaysia provides a captivating blend of tradition, nature, and delicious cuisine, making it a must-visit destination for Spanish travelers seeking a unique experience in Southeast Asia. (Tourism Malaysia, 2023)

## Problem Statement

The goal is to do sentiment analysis on the remarks and reviews left by visitors to Malaysia's Sepilok Orangutan Sanctuary. The investigation seeks to comprehend the general attitude that visitors have towards their experiences at the sanctuary. Positive features can be found by analysing the emotion, improving guest satisfaction and revealing prospective areas for improvement. The results of this research will be used to assess the success of the sanctuary's conservation efforts, visitor participation, and overall guest experience. This analysis will also offer insightful information for future planning and marketing initiatives.

## Objective

The objective is to conduct sentiment analysis on the comments and reviews of guests visiting the Sepilok Orangutan Sanctuary in Malaysia. The analysis aims to understand the overall sentiment expressed by guests regarding their experiences at the sanctuary.

## Built With

![My Skills](https://go-skill-icons.vercel.app/api/icons?i=vscode,python,playwright,scikitlearn,streamlit,nltk&titles=true)


## Data Source
Data obtained from TripAdvisor platform through web scraping. 

## Methodology

- **Data Collection:** The dataset is scrap from TripaAdvisor traveller reviews on Sepilok Orangutan Rehabilitation Centre, Sabah. With a total of 3657 samples, the four (4) possible features that may be relevant for insights would be the rating review, the date of review, the category of reviewer & the text review.
- **Preprocessing:** All features were retained, with reviewer_rating converted to integer, review_date to date type, Na in reviewer_category replaced with "Not Specify," and a new reviewer_sentiment feature created based on reviewer_rating. The text_review is later used tokenization, remove stopwords, and remove special characters & numbers for text analysis.
- **Model Development:** The text_review is processed again using WordNetLemmatizer and converted into a numeric matrix using CountVectorizer. Random Forest (RF), Decision Tree (DT), and Multilayer Perceptron (MLP) were tested with optimized parameters.
- **Model Evaluation:** The models were evaluated using accuracy, precision, recall, F1-score, and confusion matrix.
- **Deployment:** The best-performing model was deployed using Streamlit.

## Result and Impact

- **Visitor Sentiment and Satisfaction:** 85% of visitors expressed positive sentiment, with couples being the largest visitor category.
- **Visitor Trends:** Visits peaked in 2017 but sharply declined after the COVID-19 pandemic, with April, July, and August being the busiest months.
- **Text Analysis:** WordCloud analysis of text_review by sentiment shows common words—positive: "sanctuary," "centre," "great," "animal"; neutral: "people," "good," "place," "sanctuary"; negative: "place," "zoo," "people."
- **Best Model Prediction** The RF model performs the best out of all the models that were tested.

## Challenges and Solutions

- **Data Scraping:** TripAdvisor's dynamic website posed challenges, resolved by using Python and Playwright for efficient data collection.
- **Model Building:** Lack of custom model-building skills was addressed by leveraging open-source libraries like scikit-learn.
- **Model Deployment:** Difficulty hosting models online was overcome by deploying them with the free and user-friendly Streamlit framework.
  
## How to Use

To test the application, click this link: [Sentiment Analyzer at Sepilok Orangutan Sanctuary](https://nlp-sentiment-analysis-sepilok-co5cthyrwy3sowxbevmhrp.streamlit.app/)

## Acknowledgement

- Tourism Malaysia. (2023, January 19). Malaysia positions itself as a sustainable destination at Fitur and presents for the first time the ecotourism offer of the state of Sabah. Tourism Malaysia. [https://www.tourism.gov.my/media/view/malaysia-positions-itself-as-a-sustainable-destination-at-fitur-and-presents-for-the-first-time-the-ecotourism-offer-of-the-state-of-sabah](https://www.tourism.gov.my/media/view/malaysia-positions-itself-as-a-sustainable-destination-at-fitur-and-presents-for-the-first-time-the-ecotourism-offer-of-the-state-of-sabah)

