import math


def calculations(targets,data):
    optimum = []
    slopes = []
    inters = []
    avg_deviance = []
    if len(targets) == len(data):
        del data[-1]
    if len(targets) == len(data):
        print("ERROR!")
        return()
    for i in range(len(targets) - 1):
        if (targets[i][0] - targets[i+1][0]) == 0:
            m = (targets[i][1] - targets[i+1][1]) / .0000001
            b = ((targets[i][0] * targets[i+1][1]) - targets[i+1][0] * targets[i][1]) / .0000001
            optimum.append((m,b))
            break
        m = (targets[i][1] - targets[i+1][1]) / (targets[i][0] - targets[i+1][0])
        b = ((targets[i][0] * targets[i+1][1]) - targets[i+1][0] * targets[i][1]) / (targets[i][0] - targets[i+1][0])
        optimum.append((m,b))
    
    for i in range(len(optimum)):
        slopes.append(optimum[i][0])
        inters.append(optimum[i][1])
    
    for i in range(len(optimum)):
        x_values = []
        y_values = []
        for j in range(len(data[i])):
            x_values.append(data[i][j][0])
            y_values.append(data[i][j][1])
        x1, x2 = min(x_values), max(x_values)
        y1, y2 = slopes[i] * x1 + inters[i], slopes[i] * x2 + inters[i]
        total_deviance = 0
        for k in range(len(x_values)):
            x = x_values[k]
            y = y_values[k]
            # Expected y value on the line for this x
            expected_y = slopes[i] * x + inters[i]
            deviance = abs(y - expected_y)
            total_deviance += deviance
        avg_deviance.append(total_deviance / len(data[i]))
            
        

    
    total = 0
    for i in range(len(avg_deviance)):
        total += avg_deviance[i]
    try:
        total_deviance = total/len(avg_deviance)
    except:
        total_deviance = 0
    
    if total_deviance > 100:
        return f"Slow down! Your avg deviance was {str(round(total_deviance,2))}"
    elif total_deviance > 50:
        return f"Oh no! Your avg deviance was {str(round(total_deviance,2))}!"
    elif total_deviance > 30:
        return f"Too much wrist. avg deviance = {str(round(total_deviance,2))}"
    else:
        return f"Nice! Your avg deviance was only {str(round(total_deviance,2))}!"
    
    
    
    
if __name__ == '__main__':
    #calculations(targets, 0)
    pass
    
    
    