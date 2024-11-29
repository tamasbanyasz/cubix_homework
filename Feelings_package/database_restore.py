import shutil
from datetime import datetime


def restore_database(backup_file, input_datetime, target_db):
    """Restore SQL database"""
    
    input_format = '%Y-%m-%d %H:%M:%S'

    dt = datetime.strptime(input_datetime, input_format)

    output_format = '%Y%m%d_%H%M%S'

    formatted_datetime = dt.strftime(output_format)

    backup_path = f"{backup_file}/backup_feelingdb.db_{formatted_datetime}.db"
    print(f"Path: {backup_path}")
    
    try:
        shutil.copy2(backup_path, target_db)
        print(f"Database restore successful from {backup_file} to {target_db}")
    except Exception as e:
        print(f"Error restoring database: {e}")

