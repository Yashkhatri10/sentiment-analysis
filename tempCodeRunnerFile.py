review = entry1.get()
        review = re.sub('[^a-zA-Z]',' ',review)
        review = review.split()
        review = [r.lower() for r in review]
        ps = PorterStemmer()
        all_stopwords = stopwords.words('english')
        all_stopwords.remove('not')
        review = [ps.stem(word) for word in review if not word in set(all_stopwords)]
        review = ' '.join(review)
        X = vect.transform([review])
        y_pred = classifier.predict(X)