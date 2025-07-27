from flask import Flask, render_template, request
from withdraw_handler import withdraw_funds  # Make sure this file is in the same directory

app = Flask(__name__)

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        from_address = request.form["from_address"]
        from_private_key = request.form["from_private_key"]
        to_address = request.form["to_address"]
        amount = float(request.form["amount"])

        result = withdraw_funds(from_address, from_private_key, to_address, amount)

        if "error" in result:
            return f"<h3>Error:</h3><p>{result['error']}</p><a href='/withdraw'>Go Back</a>"

        return f"""
            <h3>Withdrawal Successful</h3>
            <p><b>Transaction Hash:</b> {result['tx_hash']}</p>
            <p><b>From (Bank Account):</b> {result['from_address']}</p>
            <p><b>To (User Account):</b> {result['to_address']}</p>
            <p><b>Amount:</b> {result['amount_eth']} ETH</p>
            <p><b>Sender Balance:</b> {result['sender_new_balance']} ETH</p>
            <p><b>Recipient Balance:</b> {result['recipient_new_balance']} ETH</p>
            <p><b>Timestamp:</b> {result['timestamp']}</p>
            <a href='/withdraw'>Make Another Withdrawal</a>
        """

    return render_template("withdraw.html")

if __name__ == "__main__":
    app.run(debug=True)
