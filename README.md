# Prediction-of-Students-Performance-and-Analysis
# ReadMe file of the product
The STUDENTPERFORMANCE folder contains the data set used in the production of the data science product (StudentPerformance.csv), the pickle file (student_performance_model.pkl), a requirements.txt file detailing the packages that must be installed in order to run Python, the code for creating the prediction model in the Jupyter notebook (model.ipynb), Home.py, app fastapi.py, and Dockerignore.

## How to install the ACADEMIC PERFORMANCE PREDICTOR APP

### Run with Docker

2. The docker software tool needs to be installed in order to run this

3. Open a new terminal and make sure you are in the app folder directory. Run  
```bash 
docker build -t academic_performance . 
```  
to build the image

4. Then run
```bash 
docker run -p 8501:8501 academic_performance
```   
to run the image.

5. Open your browser and lunch http://localhost:8501


## Run without Docker
2. make sure python 3.x and pip is installed on the pc 

3. open a new terminal and make sure you are in the app folder directory. Run 

**windows:**
```bash 
python -m venv  venv
```  
**Macos/linux:**
```bash
  virtualenv venv
```
to create an python packages environment.
4. Activate the environment by running

**windows:**
```bash
  venv\Scripts\activate
```

**Macos/linux:**
```bash
  source venv/bin/activate
```

4. Install packages

```bash
  pip install -r requirements.txt
```

4. Start the fastapi server

```bash
  uvicorn app_fastapi:app --port 8000 
```
5. Start the streamlit server

```bash
  streamlit run --server.enableCORS=false Home.py --server.port=8501 
```

6. Open your browser and lunch http://localhost:8501



