# AWS Automation with python
Learning *AWS automation with python* from ACloud Guru 

## In order to follow this tutorial make sure you have following things installed
- aws configure --profile profile_name
- boto3
- python 3
- click

## Boto3 Library for managing AWS Resources
### Resources: 
 - Object oriented interface to AWS. A high level abstraction
 - Every resources has a number of attributes and methods
 - Resources themselves can also be conceptually split into *Service Resources (sqs,s3,ec2)* and *individual resources (sqs.Queue or s3.Bucket)*. Service Resources do not have         identifiers or attributes

 ### Identifiers and attributes
  - Identifiers: 
    - A unique value that is used to call actions on the resources
    - Resources must have at least one identifiers except for top level service resources(s3,sqs)

### Actions
 - An action is a method which makes a call to the service.
 - Actions automatically set the resource identifiers as parameters, but allow you to pass additional parameters via keyword arguments


### Features
we have included following features
 - Add click module to pass argument and grouping the methods
 - List bucket
 - list contentes of a buckets

