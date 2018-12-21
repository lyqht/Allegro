# Allegro
This is a school project that utilizes Kivy & Python language to make a basic GUI that syncs real-time data from temperature, humidity and ambient light sensors from Firebase and displays it to the user.

#### Group Members: 
- Lee Gui An (piroton)
- Tey Siew Wen (lyqht)
- Tan Tiang Teck
- Merrick Tay Yu Jie 
- Stephanie Lim Ann Tian Yuan

# Introduction: What is 10.009? 
10.009 The Digital World is an introductory course to computer science offered for freshmores studying in SUTD. In this course, we learn basic Python coding skills, data analysing, as well as Kivy. 1D is a major project of this course, where we were tasked to define a problem of concern and propose a solution that utilizes IoT technology to ameliorate the problem. Particularly, the deliverables are expected to be  a beautiful, elegant working Kivy GUI and a poster explaining how the GUI works.

The text below this paragraph consists of our problem statement as well as the implementation of our code and hardware. 

## Background of the Problem

Laundry room hazards are issues that have been easily overlooked. For example, there could be leakage from the washing machine hose, or that there could be accumulation of lint in the hose which could result in a fire. Detergents could also be forgotten to be sealed, resulting in contamination of air, which could pose a risk to the users' health, and it also affect the fabric condition of the laundry. Hence we propose a Kivy App that has a simple interface for users to access remotely and monitor the condition of their laundry room. 

## Proposed solution
We will build an IOT device that computes relative air quality, ambient light, temperature and humidity measurements, into an overall relative score known as the Brisk Score:
  - Device leverages sensors available for the Raspberry Pi to take measurements (refer to poster)
  - The higher the Brisk Score is, the less likely the user should be drying their clothes on that day. 
  - Logs to Firebase with averaged measurements over 5-min periods
  - Provides feedback on state of laundry room and also whether the user should do laundry today. 

## Benefits of the proposed solutions
- IOT-enabled device allows for remote collection of laundry room condition data and monitoring
- Based on the trend of the brisk score against the elapsed time since the app starts monitoring the state of the laundry room, the app prompts investigation on the user's end if there could be a firehazard due to machine hose blockage or biohazard risk due to exposed detergents. 

## Rooms for Improvement
Due to lack of time, and thus lack of training data, we were unable to implement machine learning facilties such as TensorFlow /sklearn module this time for predictive qualitative assessments of the Brisk score. However, having a machine learning algorithm would better allow users to pre-empt periods of bad laundry conditions and also allows for a larger range of more specific feedback for the user. For example, with enough data, the model may be able to suggest the exact timing that the laundry will take to dry if they choose to dry it in the current weather and laundry room condition. 

