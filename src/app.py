import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

# config
st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.title("Data Visualization Tool")

    # Upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
    
    if uploaded_file is not None:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(uploaded_file)
        
        # Display the DataFrame
        st.write("Preview of the uploaded data:")
        st.write(df.head())

        # Select features for comparison
        selected_features = st.multiselect("Select features for comparison", df.columns)

        if not selected_features:
            st.warning("Please select at least one feature for comparison.")
        else:
            # Type checking
            if not all(df[feature].dtype in (int, float) for feature in selected_features):
                st.error("Selected features must be numeric for visualization.")
            else:
                # Choose the type of chart
                chart_type = st.selectbox("Select the type of chart", ["Line Chart", "Bar Chart", "Scatter Plot",
                                                                       "Bubble Chart", "Pie Chart", "Histogram",
                                                                       "Heatmap", "Polar Chart"])

                # Generate and display the chart based on user selections
                if chart_type == "Line Chart":
                    generate_line_chart(df, selected_features)
                elif chart_type == "Bar Chart":
                    generate_bar_chart(df, selected_features)
                elif chart_type == "Scatter Plot":
                    generate_scatter_plot(df, selected_features)
                elif chart_type == "Bubble Chart":
                    generate_bubble_chart(df, selected_features)
                elif chart_type == "Pie Chart":
                    generate_pie_chart(df, selected_features)
                elif chart_type == "Histogram":
                    generate_histogram(df, selected_features[0])
                elif chart_type == "Heatmap":
                    generate_heatmap(df, selected_features)
                elif chart_type == "Polar Chart":
                    generate_polar_chart(df, selected_features)

def generate_line_chart(df, selected_features):
    plt.figure(figsize=(10, 6))
    for feature in selected_features:
        plt.plot(df.index, df[feature], label=feature)

    plt.xlabel("Index")
    plt.ylabel("Values")
    plt.title("Line Chart")
    plt.legend()
    st.pyplot()

def generate_bar_chart(df, selected_features):
    fig = px.bar(df, x=df.index, y=selected_features, barmode="group")
    fig.update_layout(title="Bar Chart", xaxis_title="Index", yaxis_title="Values")
    st.plotly_chart(fig)

def generate_scatter_plot(df, selected_features):
    fig = px.scatter(df, x=selected_features[0], y=selected_features[1], title="Scatter Plot",
                     labels={selected_features[0]: selected_features[0], selected_features[1]: selected_features[1]})
    st.plotly_chart(fig)

def generate_bubble_chart(df, selected_features):
    fig = px.scatter(df, x=selected_features[0], y=selected_features[1], size=selected_features[2],
                     title="Bubble Chart", labels={selected_features[0]: selected_features[0],
                                                  selected_features[1]: selected_features[1],
                                                  selected_features[2]: selected_features[2]})
    st.plotly_chart(fig)

def generate_pie_chart(df, selected_features):
    fig = px.pie(df, names=selected_features, title="Pie Chart", hole=0.3)
    st.plotly_chart(fig)

def generate_histogram(df, selected_feature):
    plt.figure(figsize=(10, 6))
    plt.hist(df[selected_feature], bins=20, edgecolor='black')
    plt.xlabel(selected_feature)
    plt.ylabel("Frequency")
    plt.title("Histogram")
    st.pyplot()

def generate_heatmap(df, selected_features):
    fig = px.imshow(df[selected_features].corr(), title="Heatmap")
    st.plotly_chart(fig)

def generate_polar_chart(df, selected_features):
    fig = px.line_polar(df, r=selected_features[0], theta=df.index, title="Polar Chart")
    st.plotly_chart(fig)
    
if __name__ == "__main__":
    main()