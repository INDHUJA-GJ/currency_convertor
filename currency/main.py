from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        d = {'AED': 22.53, 'ARS': 0.48, 'AWG': 45.96, 'AUD': 55.06, 'AFN': 0.93, 'ALL': 0.81, 'AOA': 0.16,
                 'AMD': 0.21,
                 'AZN': 48.73, 'ANG': 45.99,

                 'BBD': 40.86, 'BMD': 82.73, 'BSD': 82.46, 'BOB': 11.94, 'BRL': 15.59, 'BAM': 44.84, 'BHD': 218.97,
                 'BGN': 44.82,
                 'BDT': 0.77, 'BYN': 33.08,
                 'BZD': 41.12, 'BTN': 1.00, 'BWP': 6.08, 'BND': 61.55, 'BIF': 0.029,
                 'CLP': 0.093, 'COP': 0.017, 'CZK': 3.61, 'CAD': 60.19, 'CHF': 88.79, 'CNY': 11.82, 'CRC': 0.16,
                 'CUP': 3.45,
                 'CDF': 0.036,
                 'DOP': 1.49, 'DKK': 11.77, 'DZD': 0.61, 'DJF': 0.47,
                 'EUR': 87.65, 'EGP': 3.36, 'ERN': 154.23, 'ETB': 1.53,
                 'FJD': 37.50, 'FKP': 92.25,
                 'GMD': 1.33, 'GBP': 100.47, 'GHS': 9.16, 'GEL': 32.62, 'GTQ': 10.62, 'GNF': 0.0096, 'GYD': 0.39,
                 'GIP': 102.85,
                 'GGP': 103.11,
                 'HRK': 11.64, 'HUF': 0.22, 'HTG': 0.58, 'HNL': 3.36, 'HKD': 10.06,
                 'ISK': 0.58, 'ILS': 23.89, 'IQD': 0.057, 'IRR': 0.0020, 'IDR': 0.0055, 'IMP': 102.821,
                 'JOD': 116.64, 'JMD': 0.54, 'JPY': 0.60, 'JEP': 102.63,
                 'KES': 0.69, 'KWD': 269.14, 'KHR': 0.02, 'KZT': 0.81, 'KPW': 0.092, 'KRW': 0.063, 'KGS': 0.95,
                 'KYD': 99.44,
                 'LYD': 17.11, 'LBP': 0.055, 'LAK': 0.0047, 'LSL': 4.26, 'LRD': 0.49, 'LYD': 17.24, 'LKR': 0.27,
                 'MDL': 4.28, 'MKD': 1.42, 'MZN': 1.30,
                 'MAD': 7.87, 'MUR': 1.87, 'MXN': 4.18, 'MYR': 18.33, 'MNT': 0.025,
                 'NAD': 5.56, 'NGN': 0.19, 'NOK': 8.36, 'NZD': 52.69, 'NPR': 0.63, 'NIO': 2.27, 'NOK': 7.62,
                 'OMR': 214.45,
                 'PEN': 21.52, 'PLN': 18.69, 'PYG': 0.011, 'PKR': 0.29, 'PAB': 82.87, 'PHP': 1.49,
                 'QAR': 22.72,
                 'RON': 17.82, 'RSD': 0.75, 'RUB': 1.28,
                 'SAR': 22.01, 'SEK': 7.95, 'SCR': 6.33, 'SZL': 4.26, 'SVC': 9.47, 'SHP': 102.821, 'SGD': 61.62,
                 'SBD': 9.94,
                 'SOS': 0.15, 'SRD': 2.22, 'SYP': 0.06,
                 'TND': 26.21, 'TRY': 4.44, 'TWD': 2.70, 'THB': 2.42, 'TTD': 12.21, 'TVD': 54.8255,
                 'UGX': 0.023, 'UAH': 2.24, 'USD': 82.84, 'UYU': 2.13, 'UZS': 0.0072,
                 'VEF': 0.0000543713, 'VND': 0.0035, 'YER': 0.33, 'ZWD': 0.2273,
                 'XAF': 0.13, 'XPF': 0.73, 'XCD': 30.46, 'XOF': 0.14, 'ZAR': 4.69,
                 }
        amount = request.form['amount']
        am= float(amount)
        curr1 = request.form['curr1']
        curr2 = request.form['curr2']
        if curr1 == curr2:
            amt = am
        elif curr2 == "INR":
            amt = d[curr2] * am
        elif curr1 == 'INR':
            amt = (1 / d[curr2]) * am
        else:
            amt = (d[curr1] / d[curr2]) * am
        result = amt
        print(result)
        return render_template('home.html', result=amt)


    else:
        return  render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
