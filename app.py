from Package import app

if __name__ == '__main__':
    app.run(host='localhost',debug=True,port=5000)
else:
    app.run()


