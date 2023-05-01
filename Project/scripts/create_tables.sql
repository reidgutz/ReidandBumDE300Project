DROP TABLE IF EXISTS heart_data;
CREATE TABLE heart_data (
    id SERIAL PRIMARY KEY,
    age NUMERIC,
    sex NUMERIC,
    cp NUMERIC,
    trestbps NUMERIC,
    chol NUMERIC,
    fbs NUMERIC,
    restecg NUMERIC,
    thalach NUMERIC,
    exang NUMERIC,
    oldpeak NUMERIC,
    slope NUMERIC,
    ca NUMERIC,
    thal NUMERIC,
    target NUMERIC
);
