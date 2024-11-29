import shutil
import os


  

def backup_database(source_db, backup_dir):
    """SQLite adatbázis mentése"""
    
    # Ellenőrizzük, hogy létezik-e a mentési könyvtár, ha nem, létrehozzuk
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    # A mentéshez új fájl nevet készítünk az aktuális dátummal
    backup_filename = os.path.join(backup_dir, f"backup_{os.path.basename(source_db)}_{get_timestamp()}.db")
    
    try:
        # A mentés fájllal való másolása
        shutil.copy2(source_db, backup_filename)
        print(f"Database backup successful: {backup_filename}")
    except Exception as e:
        print(f"Error creating backup: {e}")
        
def get_timestamp():
    """Visszaadja az aktuális időpontot YYYYMMDD_HHMMSS formátumban"""
    from datetime import datetime
    return datetime.now().strftime("%Y%m%d_%H%M%S")

# Példa használat

