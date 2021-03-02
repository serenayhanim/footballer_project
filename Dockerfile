FROM python:3.8
WORKDIR /serenay
COPY requirements.txt . 
RUN pip install --user -r requirements.txt
RUN pip install --user --upgrade git+https://github.com/twintproject/twint.git@origin/master#egg=twint
# COPY src/data_scrape.py .
# COPY accounts.csv .
CMD [ "python", "src/data_collection/data_scrape.py"]

