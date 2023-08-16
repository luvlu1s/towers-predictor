import random

def predict_safe_space(client_seed, round_id, tile_amount):
    random.seed(client_seed)
    
    predictions = []
    for col in range(7):
        grid = [['❓', '❓', '❓'],
                ['❓', '❓', '❓'],
                ['❓', '❓', '❓'],
                ['❓', '❓', '❓'],
                ['❓', '❓', '❓'],
                ['❓', '❓', '❓'],
                ['❓', '❓', '❓'],
                ['❓', '❓', '❓']]
        
        count = 0
        while count < tile_amount:
            row = random.randint(0, 2)
            if grid[count][row] != '✅':
                grid[count][row] = '✅'
                count += 1
        
        safe_space_row = random.randint(0, 2)
        predictions.append((col + 1, safe_space_row + 1))
    
    return predictions

client_seed = "Your Client Seed Here"
round_id = "Your Round ID Here"
tile_amount = 3 #depending of difficulty

predictions = predict_safe_space(client_seed, round_id, tile_amount)
for col, row in predictions:
    print(f"Predicted Safe Space for Column {col}: Row {row}")
