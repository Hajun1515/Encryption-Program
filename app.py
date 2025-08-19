from flask import Flask, render_template, request, session
import string
import random
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)  # untuk session

# ---------------- Halaman Utama ----------------
@app.route("/")
def home_page():
    return render_template('index.html')

# ---------------- ENKRIPSI ----------------
@app.route("/encrypt", methods=["GET", "POST"])
def encrypt():
    name_program = 'Encrypt Program'
    chiper_text = ''
    plain_text = ''

    if request.method == "POST":
        # daftar karakter
        chars = list(string.punctuation + string.digits + string.ascii_letters)

        # buat key acak
        key = chars.copy()
        random.shuffle(key)

        # simpan key di session
        session['key'] = key
        session['last_chiper_text'] = chiper_text  # simpan hasil enkripsi terakhir


        # ambil teks asli dari form
        plain_text = request.form.get("teks", "")
        for letter in plain_text:
            if letter in chars:
                index = chars.index(letter)
                chiper_text += key[index]
            else:
                chiper_text += letter  # biarkan karakter yg tidak ada di chars

    return render_template(
        "encrypt.html",
        name_program=name_program,
        plain_text=plain_text,
        chiper_text=chiper_text
    )

# ---------------- DEKRIPSI ----------------
@app.route("/decrypt", methods=["GET", "POST"])
def decrypt():
    name_program = 'Decrypt Program'
    plain_text = ''
    chiper_text = ''

    # kalau POST, berarti dari tombol decrypt atau dari halaman decrypt langsung
    if request.method == "POST":
        # ambil teks terenkripsi dari form
        chiper_text = request.form.get('teks', '')

        # ambil key dari session
        key = session.get('key')
        if not key:
            return "Key untuk dekripsi tidak ditemukan. Silakan enkripsi teks dulu!"

        # daftar karakter asli
        chars = list(string.punctuation + string.digits + string.ascii_letters)

        # proses dekripsi
        for letter in chiper_text:
            if letter in key:
                index = key.index(letter)
                plain_text += chars[index]
            else:
                plain_text += letter

    return render_template(
        "decrypt.html",
        name_program=name_program,
        chiper_text=chiper_text,
        plain_text=plain_text
    )


@app.route('/decimal')
def biner():
    name_program =  'Decimal to biner program'
    return render_template('decimal.html', name_program=name_program)



if __name__ == "__main__":
    app.run(debug=True)
