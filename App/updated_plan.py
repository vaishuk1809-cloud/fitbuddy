def update_plan(current_plan, new_goal):
    current_plan["goal"] = new_goal
    current_plan["updated"] = True

    return current_plan
