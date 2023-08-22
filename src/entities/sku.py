import numpy as np

from src.constraints import (
    SKU_PRICE_RANGE, 
    SKU_SIZE_RANGE, 
    COGS_RANGE
)

class SKU:
    def __init__(self) -> None:
        self.seasonality = self.generate_random_seasonality()
        self.price = np.random.uniform(*SKU_PRICE_RANGE)
        self.size = np.random.uniform(*SKU_SIZE_RANGE)
        self.cogs = self.price * np.random.uniform(*COGS_RANGE)

    def generate_random_seasonality(self, length=365):
        """
        Generate a random seasonality pattern using both sine and cosine, normalized between 0 and 1.

        Parameters:
        - length: Number of days for which the seasonality pattern is generated.

        Returns:
        - A numpy array containing the seasonality pattern.
        """
        # Generate random frequencies and phases for the sine and cosine waves
        freq_sine = np.random.uniform(0.0, 0.05)
        phase_sine = np.random.uniform(0, 2 * np.pi)
        
        freq_cosine = np.random.uniform(0.0, 0.05)
        phase_cosine = np.random.uniform(0, 2 * np.pi)

        # Generate the seasonality pattern using the sine and cosine waves
        seasonality = np.sin(np.linspace(0, 2 * np.pi * freq_sine * length, length) + phase_sine) + \
                    np.cos(np.linspace(0, 2 * np.pi * freq_cosine * length, length) + phase_cosine)

        # Normalize the values between 0 and 1
        seasonality = (seasonality - seasonality.min()) / (seasonality.max() - seasonality.min())

        return seasonality
    

if __name__ == "__main__":
    import matplotlib.pyplot as plt

    sku = SKU()
    plt.plot(sku.seasonality)
    plt.show()