import streamlit as st
import pandas as pd

"""
Go to terminal and type streamlit run hdb_recommendation_app.py
"""


# Load the saved association rules model
rules = pd.read_pickle('./model/association_rules.pkl')

# Load the original dataset to get the necessary columns for user input
association_2017_2020_df = pd.read_csv('./output_data/output.csv')


# Streamlit application --------------------------------
st.title('HDB Resale Flat Recommendation')

# User inputs 
 # User inputs This is the Drop-down menus for the user to select options for each attribute
flat_type = st.selectbox('Select Flat Type', ['No preference'] + list(association_2017_2020_df['flat_type'].unique()))
town = st.selectbox('Select Town', ['No preference'] + list(association_2017_2020_df['town'].unique()))
floor_area = st.selectbox('Select Floor Area Category', ['No preference', '<50sqm', '50-100sqm', '100-150sqm', '>150sqm'])
price_category = st.selectbox('Select Price Category', ['No preference', '<200K', '200K-500K', '500K-800K', '>1mil'])
distance_to_mrt = st.selectbox('Select Distance to MRT', ['No preference', 'Very Close (0-100m)', 'Close (100m-500m)', 'Moderate (500m-1km)', 'Long (>1km)'])
remaining_lease_category = st.selectbox('Select Remaining Lease Category', ['No preference', '55-65', '65-75', '75-85', '>85'])

# Submit button - when clicked
if st.button('Submit'):
    # Create a user profile based on inputs
    #Create a user profile based on inputs
    # This creates a dictionary with the user's selected options
    user_input = {
        'flat_type': flat_type if flat_type != 'No preference' else None,
        'town': town if town != 'No preference' else None,
        'floor_area_category': floor_area if floor_area != 'No preference' else None,
        'price_category': price_category if price_category != 'No preference' else None,
        'distance_to_mrt_category': distance_to_mrt if distance_to_mrt != 'No preference' else None,
        'new_remaining_lease_category': remaining_lease_category if remaining_lease_category != 'No preference' else None
    }

    # Filter the dataset based on user inputs
    filtered_df = association_2017_2020_df.copy()
    # print(filtered_df.head(3))
    # Loop through each key-value pair in the user_input dictionary
    for key, value in user_input.items():
        if value is not None:# Check if the user provided a value for this filter criterion
            # Filter the DataFrame to include only rows where the value in the column (key) matches the user's selected value (value).
            filtered_df = filtered_df[filtered_df[key] == value] 

    # # # Convert the input to the same format as the one-hot encoded dataframe
    # # user_encoded = pd.DataFrame([user_input])
    # # user_encoded = pd.get_dummies(user_encoded)
    # # user_encoded = user_encoded.reindex(columns=encoded_df.columns, fill_value=0)

    # # Find the matching rules based on user input
    # matching_rules = rules[rules['antecedents'].apply(lambda x: all(item in user_encoded.columns[user_encoded.loc[0] == 1] for item in x))]

    # Sort and get the top 3 matching rules by confidence
    # top_3_rules = matching_rules.sort_values(by='confidence', ascending=False).head(3)
    top_3_rules = rules.head(3)

    # Display recommendations
    if not filtered_df.empty: # If matching rows are found
        st.write('Here are some HDB flats that match your criteria:')
        for index, row in filtered_df.iterrows():
            st.write(f"**Town**: {row['town']}")
            st.write(f"**Address**: {row['block']} {row['street_name']}")
            st.write(f"**Flat Type**: {row['flat_type']}")
            st.write(f"**Storey Range**: {row['storey_range']}")
            st.write(f"**Floor Area**: {row['floor_area_category']}")
            st.write(f"**Remaining Lease**: {row['new_remaining_lease_category']}")
            st.write(f"**Price Range**: {row['price_category']}")
            st.write(f"**Nearest MRT**: {row['nearest_mrt_stations']}")
            st.write(f"**Distance to MRT**: {row['distance_to_mrt_category']}")
            # st.write(matching_rules.head())
            for idx, rule in top_3_rules.iterrows():
                st.write(f"**Antecedent**: {', '.join(list(rule['antecedents']))}")
                st.write(f"**Consequent**: {', '.join(list(rule['consequents']))}")
                st.write(f"**Support**: {rule['support']:.2f}")
                st.write(f"**Confidence**: {rule['confidence']:.2f}")
                st.write(f"**Lift**: {rule['lift']:.2f}")
                st.write("---")
            # if not matching_rules.empty:
                     
        # # Displaying the association rule metrics
        # if not matching_rules.empty:
        #     st.write("### Matching Association Rules")
        #     for idx, rule in matching_rules.iterrows():
        #         st.write(f"**Rule {idx + 1}:**")
        #         st.write(f"- **Antecedent**: {', '.join(list(rule['antecedents']))}")
        #         st.write(f"- **Consequent**: {', '.join(list(rule['consequents']))}")
        #         st.write(f"- **Support**: {rule['support']:.2f}")
        #         st.write(f"- **Confidence**: {rule['confidence']:.2f}")
        #         st.write(f"- **Lift**: {rule['lift']:.2f}")
        #         st.write("---")
    else:
        st.write("No matching recommendation found.")
