import shutil
from datetime import datetime


def restore_database(backup_file, input_datetime, target_db):
    """Restore SQL database"""
    
# A dátum formátuma, amit át szeretnénk alakítani
    input_format = '%Y-%m-%d %H:%M:%S'

# Átalakítjuk a bemeneti stringet datetime objektummá
    dt = datetime.strptime(input_datetime, input_format)

# A kívánt kimeneti formátum
    output_format = '%Y%m%d_%H%M%S'

# Az átalakított időpont formázása
    formatted_datetime = dt.strftime(output_format)

    backup_path = f"{backup_file}/backup_feelingdb.db_{formatted_datetime}.db"
    print(f"Path: {backup_path}")
    
    try:
        # A mentett fájl másolása a céltárhelyre
        shutil.copy2(backup_path, target_db)
        print(f"Database restore successful from {backup_file} to {target_db}")
    except Exception as e:
        print(f"Error restoring database: {e}")

# Példa használat
