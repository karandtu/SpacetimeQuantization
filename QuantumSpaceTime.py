# File: quantize_spacetime.py
# A Python script exploring the quantization of spacetime
import numpy as np

class QuantumSpacetime:
    def __init__(self, grid_size, planck_length):
        """
        Initialize a quantum spacetime grid.

        :param grid_size: The size of the spacetime grid (N x N).
        :param planck_length: The Planck length, the smallest unit of spacetime.
        """
        self.grid_size = grid_size
        self.planck_length = planck_length
        self.spacetime = np.zeros((grid_size, grid_size))  # Initialize spacetime grid

    def apply_quantum_fluctuations(self):
        """
        Simulate quantum fluctuations in spacetime.

        Updates the spacetime grid by adding random fluctuations at Planck scales.
        """
        fluctuations = np.random.normal(loc=0, scale=self.planck_length, size=self.spacetime.shape)
        self.spacetime += fluctuations

    def calculate_curvature(self):
        """
        Calculate spacetime curvature based on the fluctuations.

        :return: A matrix representing curvature at each point.
        """
        curvature = np.gradient(np.gradient(self.spacetime, axis=0), axis=1)
        return curvature

    def display_spacetime(self):
        """
        Display the spacetime grid values.

        :return: None
        """
        print("Spacetime grid values:")
        print(self.spacetime)

    def simulate(self, steps):
        """
        Run a simulation of quantum spacetime for a given number of steps.

        :param steps: Number of simulation steps.
        :return: List of curvature matrices for each step.
        """
        curvatures = []
        for step in range(steps):
            print(f"\nSimulation step {step + 1}:")
            self.apply_quantum_fluctuations()
            self.display_spacetime()
            curvature = self.calculate_curvature()
            curvatures.append(curvature)
            print("Calculated curvature:")
            print(curvature)
        return curvatures

if __name__ == "__main__":
    print("\nWelcome to the Quantum Spacetime Simulator!\n")
    grid_size = int(input("Enter the grid size for the spacetime (e.g., 10): "))
    planck_length = float(input("Enter the Planck length (e.g., 1.616e-35): "))
    steps = int(input("Enter the number of simulation steps: "))

    quantum_spacetime = QuantumSpacetime(grid_size, planck_length)
    curvatures = quantum_spacetime.simulate(steps)

    print("\nSimulation complete.")
