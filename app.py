import streamlit as st
import pandas as pd
import pickle

# Load the trained model
model = joblib.load('Model.pkl')
# Load dataset
df = pd.read_csv('comapany.csv')

def filter_cars_by_company(selected_company, df):
    sorted_df = df.sort_values(['company', 'name'], ascending=True)
    filtered_cars = sorted_df[sorted_df['company'] == selected_company]['name'].unique()
    return filtered_cars


# Create the web app
def main():
    # Set the title and description
    st.title('Car Price Prediction')
    st.write('Enter the details of the car to predict its price.')

    # Get user inputs
    company = st.selectbox('Company Name', sorted(df['company'].unique()))
    name = st.selectbox('Car Name', filter_cars_by_company(company, df))
    year = st.number_input('Year', min_value=1900, step=1)
    km_driven = st.number_input('Kilometers Driven',step=1000)
    fuel = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG', 'LPG', 'Electric'])
    seller_type = st.selectbox('Seller Type',['Individual', 'Dealer', 'Trustmark Dealer'])
    transmission = st.selectbox('Transmission', ['Manual', 'Automatic'])
    owner = st.selectbox('Owner',['First Owner', 'Second Owner','Third Owner','Fourth & Above Owner','Test Drive Car'])

    
    data = pd.DataFrame({'name': name,
                            'company': company,
                            'year': year,
                            'km_driven': km_driven,
                            'fuel': fuel,
                            'seller_type': seller_type,
                            'transmission': transmission,
                            'owner': owner}, index=[0])

    if st.button('Predict Price'):
        # Make predictions
        predictions = model.predict(data)
        predicted_price = "{:.2f}".format(predictions[0])
        st.success(f'Price of the car is {predicted_price} INR')


# Run the web app
if __name__ == '__main__':
    main()
