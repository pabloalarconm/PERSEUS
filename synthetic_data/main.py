import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np

RNG_SEED = 42

# SNOMED CT units (example qualifier value codes)
SNOMED_UNITS = {
    "cm": {"code": "258672001", "display": "Centimeter (qualifier value)"},
    "kg": {"code": "258683005", "display": "Kilogram (qualifier value)"},
    "µmol/L": {"code": "258773002", "display": "Micromole per liter (qualifier value)"},
    "presence": {"code": "410668003", "display": "Presence (qualifier value)"},
    "qualitative": {"code": "370125004", "display": "Qualitative (qualifier value)"}
}

# SNOMED countries (examples)
SNOMED_COUNTRIES = [
    {"code": "223369002", "display": "Spain"},
    {"code": "22335008", "display": "United States of America"},
    {"code": "223367000", "display": "United Kingdom"},
    {"code": "223368005", "display": "France"},
    {"code": "223366009", "display": "Germany"},
    {"code": "223370001", "display": "Brazil"},
    {"code": "223371002", "display": "Mexico"},
    {"code": "223372009", "display": "India"},
    {"code": "223373004", "display": "Nigeria"},
    {"code": "223374005", "display": "China"},
]

# SNOMED sex codes
SEX_CODES = [
    {"code": "248153007", "display": "Male"},
    {"code": "248152002", "display": "Female"},
    {"code": "32570681000036106", "display": "Other gender (qualifier value)"}
]

# SNOMED diagnoses / phenotypes
SNOMED_DIAGNOSES = [
    {"code": "37183000", "display": "Cystinuria, type 1"},
    {"code": "907460000", "display": "Polycystic kidney disease"},
    {"code": "74400008", "display": "Appendicitis"}
]

# SNOMED procedures / anatomical structures
SNOMED_PROCEDURES = [
    {"code": "708929007", "display": "Robot assisted laparoscopic partial nephrectomy"},
    {"code": "289754003", "display": "Total nephrectomy"},
    {"code": "80146002", "display": "Appendectomy"}
]
SNOMED_STRUCTURES = [
    {"code": "181414000", "display": "Entire kidney"},
    {"code": "66754008", "display": "Appendix"}
]

# Genetic variant examples (HGVS notation + URL)
GENETIC_VARIANTS = [
    {
        "hgvs": "NM_000123.4:c.345G>A",
        "label": "ExampleVariant1",
        "url": "https://www.ncbi.nlm.nih.gov/clinvar/RCV000000001/"
    },
    {
        "hgvs": "NM_000456.3:c.789T>C",
        "label": "Variant2",
        "url": "https://www.ncbi.nlm.nih.gov/clinvar/RCV000000002/"
    },
    {
        "hgvs": "NM_001234.5:c.12_13del",
        "label": "DelVariant",
        "url": "https://www.ncbi.nlm.nih.gov/clinvar/RCV000000003/"
    }
]

def random_date(start, end):
    if end <= start:
        return start
    delta = end - start
    return start + timedelta(days=random.randint(0, delta.days))

def generate_patient(pid, now):
    patient = {"patient_id": pid}

    # Birth info
    dob = datetime(random.randint(1950, now.year - 1),
                   random.randint(1, 12),
                   random.randint(1, 28))
    patient["birth_date"] = dob.date().isoformat()
    country = random.choice(SNOMED_COUNTRIES)
    patient["country_of_birth_code"] = country["code"]
    patient["country_of_birth_display"] = country["display"]
    sex = random.choice(SEX_CODES)
    patient["sex_code"] = sex["code"]
    patient["sex_display"] = sex["display"]

    # First confirmed visit
    fv = random_date(dob + timedelta(days=1), now)
    patient["first_visit_date"] = fv.date().isoformat()

    # Examination (height / weight)
    age_years = random.randint(1, 60)
    exam_dt = dob + timedelta(days=365 * age_years)
    if exam_dt > now:
        exam_dt = now
    patient["exam_date"] = exam_dt.date().isoformat()

    height = round(random.normalvariate(170, 10), 1)
    weight = round(random.normalvariate(70, 15), 1)
    patient["height_value"] = height
    patient["height_unit_code"] = SNOMED_UNITS["cm"]["code"]
    patient["height_unit_display"] = SNOMED_UNITS["cm"]["display"]
    patient["weight_value"] = weight
    patient["weight_unit_code"] = SNOMED_UNITS["kg"]["code"]
    patient["weight_unit_display"] = SNOMED_UNITS["kg"]["display"]

    # Phenotype (optional)
    if random.random() < 0.3:
        ph = random.choice(SNOMED_DIAGNOSES)
        patient["phenotype_code"] = ph["code"]
        patient["phenotype_display"] = ph["display"]
        patient["phenotype_date"] = random_date(exam_dt, now).date().isoformat()
    else:
        patient["phenotype_code"] = None
        patient["phenotype_display"] = None
        patient["phenotype_date"] = None

    # Symptom onset (optional)
    if random.random() < 0.6:
        so = random_date(exam_dt, now)
        patient["symptom_onset_date"] = so.date().isoformat()
        patient["symptom_note"] = random.choice(["flank pain", "hematuria", "abdominal pain", "none"])
    else:
        patient["symptom_onset_date"] = None
        patient["symptom_note"] = None

    # Laboratory test (Creatinine)
    lab_dt = random_date(exam_dt, now)
    patient["lab_date"] = lab_dt.date().isoformat()
    patient["lab_process_code"] = "113075003"
    patient["lab_process_display"] = "Creatinine measurement, serum"
    patient["molecular_target"] = "CREATININE"
    patient["lab_value"] = round(random.uniform(60, 150), 2)
    patient["lab_unit_code"] = SNOMED_UNITS["µmol/L"]["code"]
    patient["lab_unit_display"] = SNOMED_UNITS["µmol/L"]["display"]

    # Genetic test (optional)
    if random.random() < 0.5:
        gv = random.choice(GENETIC_VARIANTS)
        patient["genetic_test_hgvs"] = gv["hgvs"]
        patient["genetic_test_label"] = gv["label"]
        patient["genetic_test_url"] = gv["url"]
    else:
        patient["genetic_test_hgvs"] = None
        patient["genetic_test_label"] = None
        patient["genetic_test_url"] = None

    # Diagnosis (optional)
    if random.random() < 0.5:
        diag = random.choice(SNOMED_DIAGNOSES)
        patient["diagnosis_code"] = diag["code"]
        patient["diagnosis_display"] = diag["display"]
        patient["diagnosis_date"] = random_date(exam_dt, now).date().isoformat()
    else:
        patient["diagnosis_code"] = None
        patient["diagnosis_display"] = None
        patient["diagnosis_date"] = None

    # Surgery (optional)
    if patient["diagnosis_code"] and random.random() < 0.3:
        proc = random.choice(SNOMED_PROCEDURES)
        struct = random.choice(SNOMED_STRUCTURES)
        patient["procedure_code"] = proc["code"]
        patient["procedure_display"] = proc["display"]
        patient["anatomic_structure_code"] = struct["code"]
        patient["anatomic_structure_display"] = struct["display"]
        surgery_dt = random_date(datetime.fromisoformat(patient["diagnosis_date"]), now)
        patient["surgery_date"] = surgery_dt.date().isoformat()
    else:
        patient["procedure_code"] = None
        patient["procedure_display"] = None
        patient["anatomic_structure_code"] = None
        patient["anatomic_structure_display"] = None
        patient["surgery_date"] = None

    return patient

def generate_patients(n=10, seed=RNG_SEED):
    random.seed(seed)
    np.random.seed(seed)
    now = datetime.now()
    pat_list = [generate_patient(f"P{str(i).zfill(4)}", now) for i in range(1, n + 1)]
    df = pd.DataFrame(pat_list)
    return df

def extract_height_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    From the full synthetic patients DataFrame, extract a new table
    with columns: pid, date, value, unit (height).
    """
    height_df = df[["patient_id", "exam_date", "height_value", "height_unit_display"]].copy()
    height_df.rename(
        columns={
            "patient_id": "pid",
            "exam_date": "date",
            "height_value": "value",
            "height_unit_display": "unit",
        },
        inplace=True,
    )
    return height_df

if __name__ == "__main__":
    # Generate full synthetic patient dataset
    df = generate_patients(n=10)
    print("Full synthetic dataset:\n", df.head(), "\n")
    df.to_csv("synthetic_patients_genetic.csv", index=False)

    # Extract height-only dataset
    height_table = extract_height_table(df)
    print("Height table:\n", height_table.head(), "\n")
    height_table.to_csv("synthetic_patients_height.csv", index=False)
