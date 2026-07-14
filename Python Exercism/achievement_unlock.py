def unlock_achievement(before_xp, ach_xp, ach_name):    
    after_unlock_xp = before_xp + ach_xp
    print(after_unlock_xp) # The player's xp after the achievement is unlocked (The sum of before_xp and ach_xp)
    alert = f"Achievement Unlocked: {ach_name}"
    print(f"Achievement Unlocked: {ach_name}") # An alert message that says "Achievement Unlocked: ACHIEVEMENT_NAME", where ACHIEVEMENT_NAME is the name of the achievement
    return after_unlock_xp, alert