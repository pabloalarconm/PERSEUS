import random
from datetime import datetime, timedelta
import pandas as pd
import numpy as np
import os

RNG_SEED = 42

# SNOMEDannotations:

SNOMED_UNITS = {
    "cm": {"code": "258672001", "display": "Centimeter (qualifier value)"},
    "kg": {"code": "258683005", "display": "Kilogram (qualifier value)"},
    "µmol/L": {"code": "258773002", "display": "Micromole per liter (qualifier value)"},
    "presence": {"code": "410668003", "display": "Presence (qualifier value)"},
    "qualitative": {"code": "370125004", "display": "Qualitative (qualifier value)"}
}

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

SEX_CODES = [
    {"code": "248153007", "display": "Male"},
    {"code": "248152002", "display": "Female"}
]

SNOMED_DIAGNOSES = [
    {"code": "37183000", "display": "Cystinuria, type 1"},
    {"code": "907460000", "display": "Polycystic kidney disease"},
    {"code": "74400008", "display": "Appendicitis"},
    {"code": "473392002", "display": "Hypertensive nephrosclerosis"},
    {"code": "35455006", "display": "Acute tubular necrosis"},
    {"code": "770414008", "display": "Alport syndrome"},
]

SNOMED_PHENOTYPES = [
    {"code": "29738008", "display": "Proteinuria"},
    {"code": "84229001", "display": "Fatigue"},
    {"code": "2472002", "display": "Anuria"},
    {"code": "247355005", "display": "Flank pain"},
]

SNOMED_PROCEDURES = [
    {"code": "708929007", "display": "Robot assisted laparoscopic partial nephrectomy"},
    {"code": "289754003", "display": "Total nephrectomy"},
    {"code": "80146002", "display": "Appendectomy"}
]
SNOMED_STRUCTURES = [
    {"code": "181414000", "display": "Entire kidney"},
    {"code": "66754008", "display": "Appendix"}
]

GENETIC_VARIANTS = [
    {
        "hgvs": "NM_000092.5(COL4A4):c.3979G>A (p.Val1327Met)",
        "label": "RCV002051783.5",
        "url": "https://www.ncbi.nlm.nih.gov/clinvar/RCV001262386/"
    },
    {
        "hgvs": "NM_000458.4(HNF1B):c.494G>A (p.Arg165His)",
        "label": "RCV001262386.13",
        "url": "https://www.ncbi.nlm.nih.gov/clinvar/RCV002051783/"
    },
]

# Date utils:
def random_date(start, end):
    if end <= start:
        return start
    return start + timedelta(days=random.randint(0, (end - start).days))

# Patient generator:
def generate_patient(pid, now):
    patient = {"patient_id": pid}

    # Birth/Sex/Country
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

    # Examination (height/weight)
    exam_dt = dob + timedelta(days=365 * random.randint(1, 60))
    exam_dt = min(exam_dt, now)
    patient["exam_date"] = exam_dt.date().isoformat()
    patient["height_value"] = round(random.normalvariate(170, 10), 1)
    patient["height_unit_code"] = SNOMED_UNITS["cm"]["code"]
    patient["weight_value"] = round(random.normalvariate(70, 15), 1)
    patient["weight_unit_code"] = SNOMED_UNITS["kg"]["code"]

    # Phenotype
    if random.random() < 0.3:
        ph = random.choice(SNOMED_DIAGNOSES)
        patient.update({
            "phenotype_code": ph["code"],
            "phenotype_display": ph["display"],
            "phenotype_date": random_date(exam_dt, now).date().isoformat()
        })

    # Symptoms_onset
    if random.random() < 0.6:
        pheno = random.choice(SNOMED_PHENOTYPES)
        patient.update({
            "symptom_onset_date": random_date(exam_dt, now).date().isoformat(),
            "symptom_code": pheno["code"]
        })

    # Laboratory
    lab_dt = random_date(exam_dt, now)
    patient.update({
        "lab_date": lab_dt.date().isoformat(),
        "lab_process_code": "113075003",
        "lab_process_target": "15373003",
        "lab_value": round(random.uniform(60, 150), 2),
        "lab_unit_code": SNOMED_UNITS["µmol/L"]["code"]
    })

    # Genetics
    if random.random() < 0.5:
        gv = random.choice(GENETIC_VARIANTS)
        patient.update({
            "genetic_test_hgvs": gv["hgvs"],
            "genetic_test_label": gv["label"],
            "genetic_test_url": gv["url"]
        })

    # Diagnosis
    if random.random() < 0.5:
        diag = random.choice(SNOMED_DIAGNOSES)
        patient.update({
            "diagnosis_code": diag["code"],
            "diagnosis_display": diag["display"],
            "diagnosis_date": random_date(exam_dt, now).date().isoformat()
        })

    # Surgery
    if patient.get("diagnosis_code") and random.random() < 0.3:
        proc = random.choice(SNOMED_PROCEDURES)
        struct = random.choice(SNOMED_STRUCTURES)
        patient.update({
            "procedure_code": proc["code"],
            "procedure_display": proc["display"],
            "anatomic_structure_code": struct["code"],
            "anatomic_structure_display": struct["display"],
            "surgery_date": random_date(datetime.fromisoformat(patient["diagnosis_date"]), now).date().isoformat()
        })

    return patient

def generate_patients(n, seed=RNG_SEED):
    random.seed(seed)
    np.random.seed(seed)
    now = datetime.now()
    return pd.DataFrame([generate_patient(f"00{str(i).zfill(4)}", now) for i in range(1, n + 1)])

# Generalized table extractor:
def extract_table(df, cols_map, model):
    sub = df[list(cols_map.keys())].copy()
    sub.rename(columns=cols_map, inplace=True)
    sub["model"] = model
    return sub


import os

if __name__ == "__main__":

    # Generate synthetic patients
    df = generate_patients(100)
    os.makedirs("data", exist_ok=True)

    # Save the full dataset
    df.to_csv("data/synthetic_ALL.csv", index=False)

    # Define mappings for extracted tables
    mappings = {
        "birthdate": {
            "cols": {"patient_id": "pid", "birth_date": "value"},
            "model": "Birthdate",
        },
        "sex": {
            "cols": {"patient_id": "pid", "sex_code": "valueIRI", "sex_display": "value"},
            "model": "Sex",
        },
        "country": {
            "cols": {
                "patient_id": "pid",
                "country_of_birth_code": "valueIRI",
                "country_of_birth_display": "value",
            },
            "model": "Country",
        },
        "height": {
            "cols": {
                "patient_id": "pid",
                "exam_date": "startdate",
                "height_value": "value",
                "height_unit_code": "unit",
            },
            "model": "Examination",
        },
        "weight": {
            "cols": {
                "patient_id": "pid",
                "exam_date": "startdate",
                "weight_value": "value",
                "weight_unit_code": "unit",
            },
            "model": "Examination",
        },
        "lab": {
            "cols": {
                "patient_id": "pid",
                "lab_date": "startdate",
                "lab_process_code": "activity",
                "lab_process_target": "target",
                "lab_value": "value",
                "lab_unit_code": "unit",
            },
            "model": "Laboratory",
        },
        "genetics": {
            "cols": {
                "patient_id": "pid",
                "genetic_test_hgvs": "comments",
                "genetic_test_label": "value",
                "genetic_test_url": "valueIRI",
            },
            "model": "Genetics",
        },
        "diagnosis": {
            "cols": {
                "patient_id": "pid",
                "diagnosis_date": "startdate",
                "diagnosis_code": "valueIRI",
                "diagnosis_display": "value",
            },
            "model": "Diagnosis",
        },
        "surgery": {
            "cols": {
                "patient_id": "pid",
                "surgery_date": "startdate",
                "procedure_code": "activity",
                "anatomic_structure_code": "target",
            },
            "model": "Surgery",
        },
    }

    # Extract and save each table with its model column
    for name, spec in mappings.items():
        table = extract_table(df, spec["cols"], spec["model"])
        table.to_csv(f"data/{spec['model']}.csv", index=False)

    # Special case: combine height + weight into one Examination file
    table_height = extract_table(df, mappings["height"]["cols"], mappings["height"]["model"])
    table_weight = extract_table(df, mappings["weight"]["cols"], mappings["weight"]["model"])
    table_examination = pd.concat([table_height, table_weight], ignore_index=True)
    table_examination.to_csv("data/Examination.csv", index=False)

    print("✅ All CSVs saved in 'data/' with model information included")


