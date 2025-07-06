import pandas as pd
import numpy as np

def simulate_ab_test(n=10000, seed=42):
    np.random.seed(seed)
    
    df = pd.DataFrame({
        "user_id": np.arange(n),
        "group": np.random.choice(["control", "treatment"], size=n),
        "flight_route": np.random.choice(["AMS-JFK", "LHR-DXB", "CDG-SIN"], size=n),
        "device_type": np.random.choice(["mobile", "desktop"], size=n),
        "time_on_page": np.random.normal(45, 15, n).clip(5, 120),
    })
    
    def simulate_booking(row):
        base_rate = 0.06
        lift = 0.02 if row['group'] == 'treatment' else 0
        if row['device_type'] == 'mobile':
            lift += 0.01
        prob = base_rate + lift
        return np.random.rand() < prob

    df["booked"] = df.apply(simulate_booking, axis=1).astype(int)
    return df

if __name__ == "__main__":
    df = simulate_ab_test()
    df.to_csv("data/ab_simulated_flights.csv", index=False)
    print("Simulation complete. Data saved to data/ab_simulated_flights.csv")
