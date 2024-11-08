import numpy as np

# Function to calculate mean and standard deviation
def calculate_mean_std(data):
    mean = np.mean(data)
    std_dev = np.std(data)
    return mean, std_dev

# Function to calculate Z-scores and check for anomalies
def find_anomalies(traffic_sizes):
    mean, std_dev = calculate_mean_std(traffic_sizes)
    anomalies = []
    
    for size in traffic_sizes:
        z_score = (size - mean) / std_dev
        if z_score > 3 or z_score < -3:
            anomalies.append((size, z_score))
    
    return anomalies

# Main program
def main():
    # Input traffic sizes in the format: a,b,c,d,e,...
    input_data = input("Enter traffic sizes separated by commas (e.g., 517.36,471.45,505.92): ")
    # Convert the input string to a list of floats
    traffic_sizes = [float(size.strip()) for size in input_data.split(',')]
    
    # Find anomalies
    anomalies = find_anomalies(traffic_sizes)
    
    # Output results
    if anomalies:
        print("\nAnomalous Traffic Sizes:")
        for size, z_score in anomalies:
            print(f"Traffic Size: {size}, Z-Score: {z_score:.2f} - Anomaly Detected!")
    else:
        print("\nNo anomalies detected.")

if __name__ == "__main__":
    main()
