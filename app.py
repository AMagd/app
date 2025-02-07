import streamlit as st
import numpy as np
import plotly.graph_objects as go

# Function to compute cumulative sum
def cumulative_sum(points, mean):
    cumsum = []
    for i in range(len(points)):
        if i==0:
            cumsum.append(mean - points[i])
        else:
            cumsum.append(cumsum[i-1] + (mean - points[i]))
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
            
            # Create first plot: Points with mean and ±2SD lines
            fig1 = go.Figure()

            fig1.add_trace(go.Scatter(x=list(range(len(points))), y=points, mode='lines+markers', name='Points', hovertemplate='%{y:.2f}<extra></extra>'))
            fig1.add_trace(go.Scatter(x=[0, len(points)-1], y=[mean, mean], mode='lines', name='Mean', line=dict(color='red'), hovertemplate='Mean: %{y:.2f}<extra></extra>'))
            fig1.add_trace(go.Scatter(x=[0, len(points)-1], y=[mean + 2*sd, mean + 2*sd], mode='lines', name='Mean + 2SD', line=dict(color='green', dash='dash'), hovertemplate='Mean + 2SD: %{y:.2f}<extra></extra>'))
            fig1.add_trace(go.Scatter(x=[0, len(points)-1], y=[mean - 2*sd, mean - 2*sd], mode='lines', name='Mean - 2SD', line=dict(color='green', dash='dash'), hovertemplate='Mean - 2SD: %{y:.2f}<extra></extra>'))
            
            fig1.update_layout(title={'text': f'Points with Mean and ±2SD<br>Mean: {mean:.2f}, SD: {sd:.2f}', 'x': 0.5},
                            xaxis_title='Index',
                            yaxis_title='Value'
                            )

            # Create second plot: Cumulative sum
            fig2 = go.Figure()

            fig2.add_trace(go.Scatter(x=list(range(len(cumsum))), y=cumsum, mode='lines+markers', name='Cumulative Sum', line=dict(color='blue'), hovertemplate='%{y:.2f}<extra></extra>'))
            fig2.add_trace(go.Scatter(x=[0, len(cumsum)-1], y=[mean, mean], mode='lines', name='Mean', line=dict(color='red'), hovertemplate='Mean: %{y:.2f}<extra></extra>'))

            fig2.update_layout(title={'text': f'Cumulative Sum<br>Mean: {mean:.2f}', 'x': 0.5},
                            xaxis_title='Index',
                            yaxis_title='Value'
                            )

            st.plotly_chart(fig1)
            st.plotly_chart(fig2)
        else:
            st.error("Please enter both sets of points.")

if __name__ == '__main__':
    main()
