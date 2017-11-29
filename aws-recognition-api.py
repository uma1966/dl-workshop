
import boto3
import base64
import os.path


if __name__ == "__main__":
    fileName = 'c:/Users/Uwe/Documents/Architektentag/customer.jpg'
    bucket = 'com.enbw.techlab.ai.images'

    client = boto3.client('rekognition', 'eu-west-1')

#    response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}},MinConfidence=10)

    with open(fileName, "rb") as image_file:
#        encoded_image = base64.b64encode(image_file.read())

        response = client.detect_labels(Image={'Bytes': image_file.read() }, MinConfidence=10)

    print('Detected labels for ' + fileName)
    for label in response['Labels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))
