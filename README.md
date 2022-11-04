# AlphaK

November 2021 - Present

Machine learning software that can detect handwritten digits on a homework organizer

# How it Works
Data entry can be very time consuming to do manually, so AlphaK offers a faster solution: a machine learning alogrithm. 

The program will take in an image of a homework sheet, and extract the information needed for data entry.

# Implementation

Images of homework sheets are obtained: using a phone scanner or other software:

<img src="https://user-images.githubusercontent.com/90977640/199877144-86aab7c5-2e34-4cd4-84e6-20f002523eb5.png" width=60% height=50%>

Location of name and Student ID are found:

<img src="https://user-images.githubusercontent.com/90977640/199623382-356dcd95-c230-4548-9f4d-bb0873188340.png" width=60% height=50%>

Location of homework sheet boxes are found:

<img src="https://user-images.githubusercontent.com/90977640/199623347-cd805ac7-5f96-4862-8f4e-1f5c8b43f618.png" width=60% height=50%>

Each segment of the image is run though machine learning software:

<img src="https://user-images.githubusercontent.com/90977640/199623463-7400338f-c535-41ad-aac2-4c3c93f894ae.png" width=50% height=50%> <img src="https://user-images.githubusercontent.com/90977640/199623526-9ff2ea6d-9f34-4dbb-901e-4847d5171bb0.png" width=40% height=50%>

Computer Output:

<img src="https://user-images.githubusercontent.com/90977640/199623500-1da562ce-7d01-40c2-ba73-130b7539aaa1.png" width=70% height=50%>

# CNN Models
I made two seperate models to get extract the scores from the images. One was for just for the 6, 7, 8 and 9 digits (Model 1) {for scores}, and another was for all 0-9 digits (Model 2) {for times}.

**Model 1**

Used only 6s, 7s, 8s, and 9s on MNIST 28x28 handwritten digit dataset. Used a lot of image augmentation to create more training data.

<img src="https://user-images.githubusercontent.com/90977640/199878094-181d18fc-19e7-44d0-9ed4-1eaed0a1f026.jpg" width=24% height=50%> <img src="https://user-images.githubusercontent.com/90977640/199878093-d15476c7-a151-46f8-ae1e-012b48dc5029.jpg" width=24% height=50%> <img src="https://user-images.githubusercontent.com/90977640/199878092-34796663-8276-431b-8427-f7c6832a4a35.jpg" width=24% height=50%> <img src="https://user-images.githubusercontent.com/90977640/199878090-6d93a01e-5b32-4fc2-b671-58fad673127f.jpg" width=24% height=50%>

**Model 2**

Used all images from MNIST database, and did not have to use as much image augmentaion.

