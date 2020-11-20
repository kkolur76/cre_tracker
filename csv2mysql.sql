CREATE DATABASE IF NOT EXISTS re_markets;
USE re_markets;
SET GLOBAL local_infile = true;

-- drop table if exists unemployment;
create table if not exists unemployment( -- GEO_ID, NAME, DP03_0009PE
	msa VARCHAR(255) PRIMARY KEY, 
    msa_name VARCHAR(255), 
    unemployed_PE FLOAT 
);

drop table if exists population;
create table if not exists population ( -- GEO_ID, NAME, DP05_0001E, DP05_0005PE-DP05_0017PE, 
	msa_id VARCHAR(255) PRIMARY KEY, 
    CONSTRAINT population_fk FOREIGN KEY (msa_id) REFERENCES unemployment(msa), 
    msa_name VARCHAR(255), 
    total_ppl INT,
    ppl_lessthan5_PE FLOAT,
    ppl_5to9_PE FLOAT,
    ppl_10to14_PE FLOAT,
    ppl_15to19_PE FLOAT,
    ppl_20to24_PE FLOAT,
    ppl_25to34_PE FLOAT,
    ppl_35to44_PE FLOAT,
    ppl_45to54_PE FLOAT,
    ppl_55to59_PE FLOAT,
    ppl_60to64_PE FLOAT,
    ppl_65to74_PE FLOAT,
    ppl_75to84_PE FLOAT,
    ppl_morethan85_PE FLOAT
);

drop table if exists job_diversity;
create table if not exists job_diversity ( -- GEO_ID, NAME, DP03_0033PE-DP05_0045PE, 
	msa_id VARCHAR(255) PRIMARY KEY, 
    CONSTRAINT job_diversity_fk FOREIGN KEY (msa_id) REFERENCES unemployment(msa),
    msa_name VARCHAR(255), 
    agriculture_PE FLOAT,
    construction_PE FLOAT,
    manufacturing_PE FLOAT,
    wholesale_PE FLOAT,
    retail_PE FLOAT,
    transportation_PE FLOAT,
    IT_PE FLOAT,
    business_PE FLOAT,
    scientific_PE FLOAT,
    educational_PE FLOAT,
    entertainment_PE FLOAT,
    other_PE FLOAT,
    public_admin_PE FLOAT
);

drop table if exists rental_vacancy;
create table if not exists rental_vacancy ( -- GEO_ID, NAME, DP04_0005E
	msa_id VARCHAR(255) PRIMARY KEY, 
    CONSTRAINT rental_vacancy_fk FOREIGN KEY (msa_id) REFERENCES unemployment(msa), 
    msa_name VARCHAR(255), 
    rental_vacancy_PE FLOAT 
);

drop table if exists median_rent;
create table if not exists median_rent ( -- GEO_ID, NAME, S2503_C05_024E
	msa_id VARCHAR(255) PRIMARY KEY, 
    CONSTRAINT median_rent_fk FOREIGN KEY (msa_id) REFERENCES unemployment(msa), 
    msa_name VARCHAR(255), 
    median_rent FLOAT 
);

-- SELECT HOST, USER FROM mysql.user ;
-- LOAD DATA LOCAL INFILE '/Users/keshav/Downloads/Unemployment/ACSDP1Y2019.DP03_data_with_overlays_2020-11-09T163108.csv'
-- INTO TABLE unemployment FIELDS TERMINATED BY ','
-- ENCLOSED BY '"' LINES TERMINATED BY '\n';
