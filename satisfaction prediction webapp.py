import numpy as np
import pickle
import streamlit as st

## loading the saved model
loaded_model = pickle.load(open('C:/Users/ARNAB MANNA/Desktop/airline_satisfaction/trained_model.sav','rb'))

## creating a function

def airline_satisfaction(input_data) :
    # changing input data into numpy array
    input_data_as_numpy_Array = np.array(input_data,dtype=object)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_Array.reshape(1, -1)
    prediction = loaded_model.predict(input_data_reshaped)
    if (prediction[0] == 0):
        return 'The person is not satisfied'
    else:
        return 'The Person is satisfied'

def main() :

    ## giving a title
    st.title('Airline Passanger Satisfaction Prediction Application')
    ## getting the input data from user
    st.text("**Please give these answer in numerical values**")
    try :
        Age = st.text_input('Enter your age')
        FlightDistance = st.text_input('Enter flight distance of this journey')
        DepartureDelay = st.text_input('How much time flight delayed in minutes when it departs?')
        st.text("**Please give these answer with 0-5 number. Note that: Here 0 indicates strongly dis-satisfied and 5 indicates fully satisfied**")
        DepartureandArrivalTimeConvenience = st.text_input('How much you satisfied with departure/arrival time conveniency in flight?')
        CheckinService = st.text_input("How much you satisfied with check in service in flight?")
        OnlineBoarding = st.text_input('How much you satisfied with online boarding service in flight?')
        GateLocation = st.text_input('How much you satisfied with gate location in flight?')
        OnboardService = st.text_input('How much you satisfied with boarding service in flight?')
        SeatComfort = st.text_input('How much you satisfied with your seat in flight?')
        LegRoomService = st.text_input('How much you satisfied with leg room service in flight?')
        Cleanliness = st.text_input('How much you satisfied with cleanliness in flight?')
        FoodandDrink = st.text_input('How much you satisfied with food and drink service in flight?')
        InflightService = st.text_input('How much you satisfied with wifi service in flight')
        InflightWifiService = st.text_input('How much you satisfied with wifi service in flight?')
        InflightEntertainment = st.text_input('How much you satisfied with entertainment in flight?')
        BaggageHandling = st.text_input('How much you satisfied with baggage handling?')
        st.text('**Please give these answer with either 0 or 1 . Note that, here 0 indicates no and 1 indicates yes**')
        Gender_Male = st.text_input('Are you male?')
        CustomerType_Returning = st.text_input('Are you returning in flight?')
        TypeofTravel_Personal = st.text_input('Are you travelling in flight for your personal purpose?')
        Class_Economy = st.text_input('Are you belongs to economy class?')
        Class_EconomyPlus = st.text_input('Are you belongs to economy plus class?')


        ## code for prediction
        satisfaction = ''
        ## creating a button for prediction
        if st.button('PREDICT') :
            st.text("Airline passenger satisfaction prediction result")
            satisfaction = airline_satisfaction([Age,FlightDistance,DepartureDelay,DepartureandArrivalTimeConvenience,CheckinService,OnlineBoarding,GateLocation,OnboardService,SeatComfort,LegRoomService,Cleanliness,FoodandDrink,InflightService,InflightWifiService,InflightEntertainment,BaggageHandling,Gender_Male,CustomerType_Returning,TypeofTravel_Personal,Class_Economy,Class_EconomyPlus])
            st.success(satisfaction)
    except Exception as e:
        st.text(e)



if __name__ == '__main__' :
    main()




