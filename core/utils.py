from core.file_manager import read

def get_next_id(filename: str):
    all_rows = read(filename=filename)
    if all_rows:
        try:
            return int(all_rows[-1][0]) + 1
        except (ValueError, IndexError) as e:
            print(f"Warning: Could not get ID from last row due to: {e}")
            return 1
    return 1