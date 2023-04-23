import requests


def get_sparc_result(query):
    # this method used to connect with sparc
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = 'http://wave.ttu.edu/ajax.php'
    payload = {"action": 'getQuery', "query": query,
               "editor":
                   """ sorts
                   #people={tommy,alex,john,daniel,sarah,peter,lino}.
                   #policy= {if_a_book_is_lost_the_borrower_must_pay_for_the_cost_of_the_book_plus_a_processing_fee, 
                   books_that_are_within_the_return_period_can_be_returned_at_the_counter_or_dropped_off_in_the_designated_drop_off_box__If_a_book_is_overdue__it_must_be_returned_directly_to_the_library_counter__where_any_applicable_late_fees_will_be_assessed}.
                   #information_type = {book, magazine, newspaper, journal, reference_book}.
                   #book={book1,book2, macbeth, romeo_julit, outsider, the_six, load_of_the_rings, dune, beloved, kite_runner}.
                   #book_categories={drama, crime, fantasy, scientific, fiction, story}.
                   #book_type={general_books, textbooks}.
                   #day={monday, tuesday, wednesday, thursday, friday, saturday, sunday, weekdays, weekends}.
                   #hours={morning_8_to_6pm, morning_8_to_12pm}.
                   #availability = {yes, no}.
                   #number = 0..100.
                   
                   predicates
                   category(#book_categories,#book).
                   book_author(#people,#book).
                   opening_hours(#day,#hours).
                   lost_book_policy(#policy).
                   return_policy(#policy).
                   max_books(#number).
                   ebook_available(#availability).
                   information_type(#information_type).
                   borrowing_period(#book_type, #number).
                   
                   rules
                   opening_hours(weekdays, morning_8_to_6pm).
                   opening_hours(weekends, morning_8_to_12pm).
                   max_books(3).
                   lost_book_policy(If_a_book_is_lost_the_borrower_must_pay_for_the_cost_of_the_book_plus_a_processing_fee). 
                   return_policy(books_that_are_within_the_return_period_can_be_returned_at_the_counter_or_dropped_off_in_the_designated_drop_off_box__If_a_book_is_overdue__it_must_be_returned_directly_to_the_library_counter__where_any_applicable_late_fees_will_be_assessed).
                   category(drama, macbeth).
                   category(drama, romeo_julit).
                   category(crime, outsider).
                   category(crime, the_six).
                   category(fantasy, load_of_the_rings).
                   category(scientific, dune).
                   category(fiction, beloved).
                   category(story, kite_runner).
                   ebook_available(yes).
                   information_type(book).
                   information_type(magazine). 
                   information_type(newspaper). 
                   information_type(journal). 
                   information_type(reference_book).
                   borrowing_period(general_books, 14).
                   borrowing_period(textbooks, 7).
                   """}

    x = requests.post(url, headers=headers, data=payload)
    print(x.text)
    return x.text
