def parse_kills_data(filepath):
    kills_info = {}
    with open(filepath, 'r') as file:
        for line in file:
            parts = line.strip().split(" - ")
            if len(parts) == 2:
                name, kills = parts
                kills_info[name] = int(kills.replace(",", ""))
    return kills_info

def parse_xp_hp_data(filepath):
    xp_hp_info = {}
    with open(filepath, 'r') as file:
        next(file)  # Skip header
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 4:
                name = ' '.join(parts[:-3])
                exp, hp, ratio = [int(part.replace(",", "")) if i < 2 else float(part.replace(",", "")) for i, part in enumerate(parts[-3:])]
                xp_hp_info[name] = {"exp": exp, "hp": hp, "ratio": ratio}
    return xp_hp_info

def merge_data(kills_info, xp_hp_info):
    merged_data = []
    for name, kills in kills_info.items():
        if name in xp_hp_info:
            data = xp_hp_info[name]
            total_xp = data["exp"] * kills
            merged_data.append({
                "name": name,
                "xp each": data["exp"],
                "hp": data["hp"],
                "ratio": data["ratio"],
                "kills": kills,
                "total xp": total_xp,
            })
    return merged_data

def main():
    kills_filepath = 'kills2.txt'
    xp_hp_filepath = 'list2.txt'
    
    kills_info = parse_kills_data(kills_filepath)
    xp_hp_info = parse_xp_hp_data(xp_hp_filepath)
    merged_data = merge_data(kills_info, xp_hp_info)
    
    # Output merged data
    with open('merged_dataset.csv', 'w') as f:
        f.write("name,xp each,hp,ratio,kills,total xp\n")
        for creature in merged_data:
            f.write(f'{creature["name"]},{creature["xp each"]},{creature["hp"]},{creature["ratio"]},{creature["kills"]},{creature["total xp"]}\n')
    
    print("Merged dataset has been created as 'merged_dataset.csv'.")

if __name__ == "__main__":
    main()
