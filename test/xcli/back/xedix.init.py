import time as tm

# Open commits.txt for appending data with UTF-8 encoding
with open("commits.txt", "a", encoding="utf-8") as commits_file:

    # Define the current time at the start, so it's available for both file processing and commit message
    current_time = tm.strftime("%H:%M %Y/%m/%d")
    current_time_only = tm.strftime("%H:%M")
    
    
    current_date_only = tm.strftime("%Y/%m/%d")
    
    # Create a list to store file names
    file_names = []

    # Get file names from the user until 'xcli commit' is entered
    exit = False
    print("⚡ Welcome to 'xcli' - Let's start adding files to the commit.\n")
    while True:
        
        file_name = input("📄 File name (or 'xcli commit' or 'xcli exit'): ").strip()

        if file_name.lower() == "xcli commit":
            break

        if file_name.lower() == "xcli exit":
            exit = True
            break
        
        file_names.append(file_name)

    # Write the files to commits.txt
    if(exit):
        print("🚪 Exiting 'xcli' - No files added to the commit.")
    else:    
        for file_name in file_names:
            commits_file.write(f"file: {file_name} [{current_time}]")
            commits_file.write("\n")
         # Commit message at the end
        message = input("📝 Commit message (some description): ").strip()
        commits_file.write(f"\nfiles changed: {', '.join(file_names)}"+"\n")
        commits_file.write(f"commit: \"{message}\" at {current_time_only} on {current_date_only}")
        branch = input("🌿 Change branch(y/n): ").strip()

        if branch.lower() == "y":
            name = input("🌿 Branch name(or 'xcli exit' to exit): ").strip()
            
            # Last chance to exit
            if name.lower() == "xcli exit":
                print("🚪 Exiting 'xcli' - No files added to the commit.")
            else:    
                commits_file.write(f"\nbranch: \"{name}\" at {current_time_only} on {current_date_only}\n")
                commits_file.write("=" * 50 +"\n")  # Separator   
                print("✅ Commit saved in 'commits.txt'.")
        else:
            print("✅ Commit saved in 'commits.txt'.")