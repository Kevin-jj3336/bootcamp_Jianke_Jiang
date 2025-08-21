# Data Storage Workflow

This stage homework demonstrates a simple data storage and validation workflow:  
1. Save a DataFrame in **CSV** and **Parquet** formats.  
2. Reload both files and validate them.  
3. Refactor I/O logic into reusable utility functions.  
4. Document the data storage design and usage.  

# Folder Strucutre
.
├── data/
│   ├── raw/         
│   └── processed/   
├── notebooks/
│   └── stage05_data-storage_lecture-notebook.ipynb
├── stage05_data-storage_homework-starter.ipynb
├── .env              
└── README.md


# Format Used 
- CSV (stored in data/raw/): Human-readable, easy to inspect and share.
- Parquet (stored in data/processed/): Columnar storage, smaller size and faster reads, better for analytics and large-scale processing.

# Write to CSV and Parquet
- write_df(df, os.path.join(os.getenv("DATA_DIR_RAW"), "sample.csv"))
- write_df(df, os.path.join(os.getenv("DATA_DIR_PROCESSED"), "sample.parquet"))

# read from CSV and Parquet
- csv_df = read_df(os.path.join(os.getenv("DATA_DIR_RAW"), "sample.csv"))
- pq_df  = read_df(os.path.join(os.getenv("DATA_DIR_PROCESSED"), "sample.parquet"))
