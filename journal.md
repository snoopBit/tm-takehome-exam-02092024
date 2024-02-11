# **Project Journal**
>*This document encapsulates all of my thought process while taking the take home exam.*

<br />

## **Executive Summary**
| Day | Task | Description |
| -------- | -------- | -------- |
| 1 | **GitHub Repository Creation** | <ul><li>Managed to refresh my memory again on basic GitHub repo creation considerations and project structure</li></ul> |
| 1 | **Model Deployment and Optimization** | <ul><li>This time the Jupyter notebook was provided, so it was easier to start the exam</li><li>I was able to understand the model development process from cleaning to model tuning.</li><li>I managed to deploy the HTTP-based API on a compute engine VM using my personal account, since I had no additional access to the provided GCP project to create VM's there. |
| 2 | **Data ETL Pipeline** | <ul><li>Had to refresh my memory on how dagster works</li><li>Decided to work on individual ops functions first</li><li>Managed to make the code work without the use of dagster decorators. Still trying to figure out how to resolve the issue with the dagster decorators</li></ul> |
| 3 | **Data ETL Pipeline** | <ul><li>Finished editing the load.py file</li><li>Managed to make the dagster web app work for a little while before bugging out.</li><li>Finished documentation by creating diagrams and putting in last journal entries before submission.</li></ul> |
<br />

## **Day 1**

### **GitHub Repository Creation**
- I just recalled my work from before and used the provided project structure template. It looked similar to what I did before.

### **Model Deployment and Optimization**
- Based on the results and as stated by the model developer/s in the summary section, the model to be deployed would be one which garnered the least false negatives. In this case, the tuned decision trees would suffice.
- I did try to further improve the decision trees classifier by following the suggestion to just use variables that are correlated to the target variable but after grid search, the accuracy did not improve. However, if this were to be deployed, my suggestion would to still use the model that I fitted with just correlated variables since it would use fewer variables, hence would incur less cost in the long run (at the price of less accuracy).
- Unfortunately, the provided GCP project did not allow me to create compute engine VM's there so I proceeded to create a VM using my personal account.
- The API deployment was relatively easy thanks to readily available guides on Youtube and even comprehensive docs from Google.
- I encountered errors when I executed tests locally, specifically when trying to load the model pkl file, but resolved it by making sure that the joblib versions matched in the environment where I serialized the model and where I deserialized it.
- I thought of how my app.py script would fit with the given ETL script templates. I decided that I would just use my script, which can perform inference one set of values in JSON format at a time (one user at a time) and try to utilize the pandas apply function to implement it to all rows.
---
<br />

## **Day 2**

### **Data ETL Pipeline**
- My plan of attack for this was to check out each file one by one. I also looked by order of which the functions were performed in the ETL pipeline: raw data extraction (extract), model inference (transform), then processed data dumping (load). The jobs.py file only used functions from the files under the ops folder so there was nothing to edit there. I figured that I should edit the extract.py file first since it would be the first step of the pipeline.
- This was my first time using the GCP Cloud Storage service so I had to read and watch some tutorials online first. Although I do have some AWS S3 experience, I still had to familiarize myself with the interface and what options to select to finally navigate to the buckets dashboard.
- I'm not sure if putting the service account credentials JSON file is the best practice but I put it in the same directory as the extract.py and transform.py files.
- I encountered an error when I first tried to run the extract.py file. It had to do with the importing of the settings.py module. I had to put in additional lines of code to make the importing work.
- Since I was still not given additional access to work on the provided GCP project, I just created buckets in my own GCP project to push through with the exam. I just used general purpose ones since this is just for demo purposes.
- Thanks to comprehensive GCP guides, I managed to make my data extraction script work. However, I can't make the whole extract.py file work since there's an error related to the usage of the Out() objects under the op decorator. I'm still not sure what to do about it.
- For now, I continued my work by filling the missing lines of code in the transform.py file.
- I included a folder to show that my code works despite not running when the whole file is executed.
---
<br />

## **Day 3**

### **Data ETL Pipeline**
- Adding the missing lines of code in the load.py file made me appreciate again the online guides since there are plenty of them. I was able to easily upload my files to a BigQuery table.
- BigQuery reminds me of the data warehouse + data querying service that we use at work.
- I managed to make the dagster web app work properly, where it showed the job pipeline. It was a matter of tweaking the decorator arguments from the extract.py file. I also had to change the job name definition inside the repos.py and schedules.py files since it was the job name was wrong. It used a placeholder value instead of "bank_etl_job" which was defined inside the jobs.py file.
- For some reason, the web app encountered an error again despite me triple checking everything. I did not have enough time so I decided to push through with the deployment to the GCP VM.
- I wished I knew a better way to upload the whole directory. What I did was manual uploading of all files and creation of directories then moving them to their respective file paths one-by-one.
- After installing all necessary packages, executing dagit worked fine, except it also showed the error that I encountered in my local machine. It had to do with not properly finding the defined job "bank_etl_job", which puzzled me again.
- Documentation was the last part that I focused on. I made sure that my code worked before I documented everything. It was fun trying to encapsulate everything into an easy-to-understand diagram.
- Overall, I really appreciated this exercise since it made me learn a lot of new things (from figuring out proper configurations in a new cloud services platform to using the said platform's SDK for calling on its services)
---
<br />

