# 1D-DW
This folder contains Kivy Code for our App, as well as the current desc file that you're reading now which contains the info about what this 1D-DW project is about.

#### Authors: 
Lee Gui An

Tey Siew Wen

Tan Tiang Teck

Merrick Tay Yu Jie

Stephanie Lim Ann Tian Yuan

## Background and problems to be solved
Singapore is an increasingly air-conditioned nation - and rooms that are air-conditioned are often not ventilated often, resulting in possible degradation of air quality indoors.
This is corroborated by the study, Asthma in the Past, Present and the Future, http://www.annals.edu.sg/pdf/46VolNo3Mar2017/V46N3p81.pdf, which has findings that show that “Eighty percent of local university students have allergen sensitization and 18% reported asthma." According to the authors, even "non-residents in Singapore develop increasing rates of sensitization and atopy year on year when they move here, suggesting that the environment in Singapore is contributing to this allergic phenomenon.” 

## Proposed solution
Build an IOT device to determine indoor air quality measures
  - Device leverages sensors available for the Raspberry Pi to take measurements
  - Computes relative quality measurement
  - Logs to Firebase with averaged measurements over a half-hour period
  - Provides recommendations on air quality
  - Use of machine learning facilties such as TensorFlow /sklearn module for predictive qualitative assessments of air quality

## How to use the mobile application, how the system works, UI of the mobile application, etc



## Schematics or diagram of the whole system and individual components of the system
We are using the following sensors for collecting data of air quality:
  - MHQ-135 Air Quality Sensor
  - DHT-22 Temp/Humidity Sensor

## Benefits of the proposed solutions
- IOT-enabled device allows for remote collection of air quality data and monitoring
- Predicts periodically recurring spikes in pollutants and prompts investigation
- Allows users to pre-empt periods of poor air quality with corrective action
- Relatively small footprint allows users to install them in schools/homes/offices easily to build collection of data for prediction and corrective action
