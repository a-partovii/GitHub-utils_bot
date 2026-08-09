def adjust_files_menu(list_name:str, file_path:str):
    _ = {
    "1": {"label": f"Show {list_name}", "action": lambda: print_in_columns(read_file(file_path))},
    "2": {"label": f"Add new usernames to {list_name}", "action": lambda:""},
    "3": {"label": f"Remove usernames from {list_name}", "action": lambda:""},
    "4": {"label": f"Reset {list_name}", "action": lambda: ""},
    "0": {"label": "Exit menu", "action": ""}
}
    show_menu(_)

# ---------------------------------------------------------------------
config_submenu = {
    "1": {"label": "Adjust Blacklist", "action": ""},
    "2": {"label": "Adjust Whitelist", "action": ""},
    "3": {"label": "Adjust Greylist", "action": ""},
    "4": {"label": "Manage GitHub tokens", "action": ""}
    # "0": {"label": "Back to main menu", "action": return_to_main},
}
