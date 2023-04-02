import requests


def get_sparc_result(query):
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://wave.ttu.edu/ajax.php'
    payload = {"action": 'getQuery', "query": query,
               "editor":
                   """ sorts
                   #people={tommy,alex,john,daniel,sarah,peter,lino}.
                   #policy= {if_a_book_is_lost_the_borrower_must_pay_for_the_cost_of_the_book_plus_a_processing_fee}.
                   #book={book1,book2}.
                   #book_categories={drama, crime, fantasy, scientific}.
                   #day={monday, tuesday, wednesday, thursday, friday, saturday, sunday, weekdays, weekends}.
                   #hours={morning_8_to_6pm, morning_8_to_12pm}.
                   predicates
                   categories(#book_categories,#book).
                   book_author(#people,#book).
                   opening_hours(#day,#hours).
                   lost_book_policy(#policy).
                   rules
                   opening_hours(weekdays, morning_8_to_6pm).
                   opening_hours(weekends, morning_8_to_12pm).
                   lost_book_policy(If_a_book_is_lost_the_borrower_must_pay_for_the_cost_of_the_book_plus_a_processing_fee). 
                   """}

    x = requests.post(url, headers=headers, data=payload)
    print(x.text)
    return x.text
