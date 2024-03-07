def detect_anomalies_moving_average(data, window_size, threshold):
    anomalies = []
    for i in range(len(data) - window_size + 1):
        window = data[i:i+window_size]
        avg = sum(window) / window_size
        if abs(data[i + window_size - 1] - avg) > threshold:
            anomalies.append(data[i + window_size - 1])
    return anomalies

# Example usage:
data = [10, 15, 12, 18, 5, 20, 25, 30, 35, 40, 100]
anomalies = detect_anomalies_moving_average(data, window_size=3, threshold=10)
print("Anomalies:", anomalies)
