from flask import Flask, render_template, request
from loan_handler import give_loan

app = Flask(__name__)

@app.route("/loan", methods=["GET", "POST"])
def loan():
    if request.method == "POST":
        to_address = request.form['to_address']
        amount = float(request.form['amount'])

        result = give_loan(to_address, amount)

        if isinstance(result, dict):
            return f"""
                <h3>{result['status']}</h3>
                <p><b>Transaction Hash:</b> {result['tx_hash']}</p>
                <p><b>To:</b> {result['to']}</p>
                <p><b>Amount:</b> {result['amount']} ETH</p>
                <p><b>Time:</b> {result['timestamp']}</p>
                <p><b>Admin Balance:</b> {result['admin_balance']} ETH</p>
                <p><b>User Balance:</b> {result['user_balance']} ETH</p>
                <a href='/'>Go Home</a>
            """
        else:
            return f"<h3>{result}</h3><a href='/loan'>Try Again</a>"

    return render_template("loan.html")

if __name__ == "__main__":
    app.run(debug=True)
