
-- Add a new Table  to store patient diseases
CREATE TABLE IF NOT EXISTS patient_diseases (
    id SERIAL PRIMARY KEY,
    patient_id INT REFERENCES patients(id),
    disease_id INT,
    diagnosis_date DATE NOT NULL,
    recovery_date DATE
);

-- Add a new column to store patient addresses
ALTER TABLE patients ADD COLUMN IF NOT EXISTS address TEXT;

-- Add a new column to doctors with a default value
ALTER TABLE doctors ADD COLUMN IF NOT EXISTS hospital_affiliation VARCHAR(100) DEFAULT 'Independent';

-- Add an index on disease_id for performance
CREATE INDEX IF NOT EXISTS idx_disease_id ON patient_diseases (disease_id);

-- Create a trigger to auto-update recovery_date when a new diagnosis is added
CREATE OR REPLACE FUNCTION set_recovery_date() RETURNS TRIGGER AS $$
BEGIN
    IF NEW.recovery_date IS NULL THEN
        NEW.recovery_date := NEW.diagnosis_date + INTERVAL '14 days';
    END IF;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS trigger_set_recovery_date ON patient_diseases;
CREATE TRIGGER trigger_set_recovery_date
BEFORE INSERT ON patient_diseases
FOR EACH ROW
EXECUTE FUNCTION set_recovery_date();
