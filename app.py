import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Function to compute cumulative sum
def cumulative_sum(points, mean):
    cumsum = [mean]
    for i in range(1, len(points)):
        cumsum.append(cumsum[-1] + (points[i] - points[i-1]))
    return cumsum

# Streamlit app
def main():
    st.title("Point Statistics and Cumulative Sum Plotter")

    # User input for points to plot
    points_input = st.text_area("Enter points to plot separated by commas (e.g., 1, 2, 3, 4):")
    
    # User input for points to compute mean and std
    stats_points_input = st.text_area("Enter points to compute mean and std separated by commas (e.g., 1, 2, 3, 4):")
    
    if st.button("Plot"):
        if points_input and stats_points_input:
            points = list(map(float, points_input.split(',')))
            stats_points = list(map(float, stats_points_input.split(',')))
            mean = np.mean(stats_points)
            sd = np.std(stats_points)
            
            # Calculate cumulative sum
            cumsum = cumulative_sum(points, mean)
            
            # Create plots
            fig, axs = plt.subplots(2, 1, figsize=(10, 8))
            
            # First plot: Points with mean and ±2SD lines
            axs[0].plot(points, 'o-', label='Points')
            axs[0].axhline(y=mean, color='r', linestyle='-', label='Mean')
            axs[0].axhline(y=mean + 2*sd, color='g', linestyle='--', label='Mean + 2SD')
            axs[0].axhline(y=mean - 2*sd, color='g', linestyle='--', label='Mean - 2SD')
            axs[0].legend()
            axs[0].set_title('Points with Mean and ±2SD')
            
            # Second plot: Cumulative sum
            axs[1].plot(cumsum, 'o-', label='Cumulative Sum')
            axs[1].legend()
            axs[1].set_title('Cumulative Sum')
            
            st.pyplot(fig)
        else:
            st.error("Please enter both sets of points.")

if __name__ == '__main__':
    main()
