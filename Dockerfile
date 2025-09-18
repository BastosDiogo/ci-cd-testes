FROM python:3.12

WORKDIR /app

COPY . .

CMD ["python", "-m", "unittest", "tests.test_contract"]