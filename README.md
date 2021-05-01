# DSPD Project
## Facial expression recognition

Phase II:

- A neural network with 62% accuracy on test set
- A simple flask API to consume the model and perform prediction
- Dockerization of the flask app

Phase III:

- Moved 62% accurate Model and Flask Application to AWS Cloud , You can use this curl Request below here 

        curl --location --request POST 'https://dspd-service.lhth73asbhl1c.us-west-2.cs.amazonlightsail.com/predict' --form 'file=@"sad3.jpeg"'
        
- Trained a ResNet-50 model with 70% accuracy. The Notebook for that model has also attached
- Performed Quantization using tflite and reduced 10x size.
- Performed Pruning and reduced the model size by 50% but the accuracy got reduced from 70% to 54%.

Phase IV:

- Interpretability - Create a report on how various iterations of the model improved over time and in which areas it lacks including confusion matrix etc
- Polish flask application: Improve the business logic by integrating database and exposing end to end APIs as was mentioned in the Vision doc
- Test model generalization on different data sets specially including minority and under respresented groups.
- Iterate on model quality to strike a reasonable accuracy to size balance.
- Expose the final model through the flask application already on cloud


*Doesn't include the training and test data to reduce repo size, can be furnished upon request*

Group members:
Daniyal Raza 19839
Babar Shamsi 19840
Aisha Ghori Pathan 18297
