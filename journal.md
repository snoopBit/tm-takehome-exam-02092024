# **Project Journal**
>*This document encapsulates all of my thought process while taking the take home exam.*

<br />

## **Executive Summary**
| Day | Task | Description |
| -------- | -------- | -------- |
| 1 | **GitHub Repository Creation** | <ul><li>Managed to refresh my memory again on basic GitHub repo creation considerations and project structure</li></ul> |
| 1 | **Model Deployment and Optimization** | <ul><li>This time the Jupyter notebook was provided, so it was easier to start the exam</li><li>I was able to understand the model development process from cleaning to model tuning.</li><li>I managed to deploy the HTTP-based API on a compute engine VM using my personal account, since I had no additional access to the provided GCP project to create VM's there. |
| 2 | **Data ETL Pipeline** | <ul><li>Placeholder</li></ul> |
| 3 | **Data ETL Pipeline** | <ul><li>Placeholder</li></ul> |
<br />

## **Day 1**

### **GitHub Repository Creation**
- I just recalled my work from before and used the provided project structure template. It looked similar to what I did before.

### **Model Deployment and Optimization**
- Based on the results and as stated by the model developer/s in the summary section, the model to be deployed would be one which garnered the least false negatives. In this case, the tuned decision trees would suffice.
- Unfortunately, the provided GCP project did not allow me to create compute engine VM's there so I proceeded to create a VM using my personal account.
- The API deployment was relatively easy thanks to readily available guides on Youtube and even comprehensive docs from Google.
- I encountered errors when I executed tests locally, specifically when trying to load the model pkl file, but resolved it by making sure that the joblib versions matched in the environment where I serialized the model and where I deserialized it.
- I thought of how my app.py script would fit with the given ETL script templates. I decided that I would just use my script, which can perform inference one set of values in JSON format at a time (one user at a time) and try to utilize the pandas apply function to implement it to all rows.
---
<br />

## **Day 2**

### **Data ETL Pipeline**
- Placeholder
---
<br />

## **Day 3**

### **Data ETL Pipeline**
- Placeholder
---
<br />

