import requests
import streamlit as st

class CurrencyConvert:
    def __init__(self):
        st.title("Dollar 2 Indian Rupee Currency Converter")
        self.currency = st.selectbox("Select the currency",["USD","INR"])
        self.amount = st.number_input(f"Enter the amount in {self.currency}",min_value = 0.0, step= 0.1 )
        self.exchange_currency = self.get_exchange_rate()


    def get_exchange_rate(self):
        
        URL = f'https://api.exchangerate-api.com/v4/latest/INR'
        try:
            response = requests.get(URL, timeout=5)
            response.raise_for_status()

            data = response.json()

            
                    
            rates = data.get("rates", {})
            usd_inr = rates.get("USD", None) 
            inr_usd = 1/usd_inr if usd_inr else None

            return {"USDINR": usd_inr,"INRUSD": inr_usd}

        except Exception as e:
            st.error("USD to INR rate not found in the response.")
            return None


    def currency_conversion(self):
        if self.exchange_currency:
            if self.currency == "USD":
                st.write(f"1 USD is equal to {self.exchange_currency['INRUSD']:.2f} INR")
                converted_amount = self.amount * self.exchange_currency["INRUSD"]
                st.write(f"{self.amount:} INR is equal to {converted_amount:.2f} USD")
            else:      
                st.write(f"1 INR is equal to {self.exchange_currency['USDINR']:.2f} USD")  
                converted_amount = self.amount * self.exchange_currency["USDINR"]
                st.write(f"{self.amount:} INR is equal to {converted_amount:.2f} USD") 
          
cc = CurrencyConvert()  
cc.currency_conversion()