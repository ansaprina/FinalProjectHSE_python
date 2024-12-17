import streamlit as st
from datetime import datetime, timedelta, time
from classes.restaurant import Restaurant, take_table, release_table


if 'restaurant' not in st.session_state:
    st.session_state['restaurant'] = Restaurant()

restaurant = st.session_state['restaurant']


def check_time(start_time, end_time):
    if start_time > end_time:
        st.error("Start time cannot be greater than end time")
        return False
    elif end_time < start_time:
        st.error("End time cannot be less than start time")
        return False
    elif start_time < time(9, 0) or start_time > time(22, 0):
        st.error("Please select time after 9:00 and before 22:00")
        return False
    elif end_time > time(23, 0) or end_time < time(10, 0):
        st.error("Please select time after 10:00 and before 23:00")
        return False
    return True


def table_management_page():
    st.header("Table Management Page")
    st.text("Manage restaurant: add and delete tables")

    table_name = st.text_input("Table name")
    number_seats = st.number_input("Number of seats", min_value=1, step=1)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Add table"):
            result_table = restaurant.add_table(table_name, number_seats)
            if result_table is None:
                st.error("There has already been added a table with such name. Change the name")
            else:
                st.success(f"The table {table_name} has been added")
                st.write("## Current Tables")
                for table in restaurant.tables:
                    st.write(f"{table.name} - Seats: {table.seats}")

    with col2:
        if st.button("Delete table"):
            result_table = restaurant.delete_table(table_name)
            if result_table is None:
                st.success(f"The table {table_name} has been deleted")
            else:
                st.error(result_table)
                st.write("## Current Tables")
                for table in restaurant.tables:
                    st.write(
                        f"{table.name} - Seats: {table.seats}")


def booking_page():
    st.header("Booking Page")
    st.text("Enter booking details to reserve a table")

    guest_name = st.text_input("Guest name")
    phone_number = st.text_input("Phone number")
    num_guests = st.number_input("Number of guests", min_value=1, step=1)
    date = st.date_input("Date", min_value=datetime.now().date() + timedelta(days=1))
    start_time = st.time_input("Start time")

    if start_time < time(9, 0) or start_time > time(22, 0):
        st.error("Please select time after 9:00 and before 22:00")

    end_time = st.time_input("End time")

    if end_time > time(23, 0) or end_time < time(10, 0):
        st.error("Please select time after 10:00 and before 23:00")

    if st.button("Book table"):
        if check_time(start_time, end_time) and guest_name != "" and phone_number != "":
            result_booking = restaurant.add_booking(guest_name, phone_number, date, start_time, end_time, num_guests)
            if result_booking is None:
                st.error("There are no available tables for this date and time")
            else:
                st.success(f" The table {result_booking.table.name} has been booked for {result_booking.guest.name}")
        else:
            st.error("Please check the correctness of the input data")


def restaurant_status_page():
    st.header("Restaurant Status Page")
    st.write("Booking information and cancellation, checking tables' availability, taking and releasing the table")

    col1, col2 = st.columns(2)

    n = 1

    with col1:
        st.write("## Current Tables")
        for table in restaurant.tables:
            n += 1
            st.write(f"{table.name} - Seats: {table.seats} - Availability: {table.is_available}")
            if not table.is_available:

                colm1, colm2 = st.columns(2)

                with colm1:
                    if st.button("Release table", key=f"Release_table_{n}"):
                        res_table = release_table(table)
                        st.success(res_table)
                with colm2:
                    if st.button("Delete table", key=f"Delete_table_{n}"):
                        res_table = restaurant.delete_table(table.name)
                        st.success(res_table)
            else:
                if st.button("Delete table", key=f"Delete_table_{n}"):
                    res_table = restaurant.delete_table(table.name)
                    st.success(res_table)

    k = 1

    with col2:
        st.write("## Current Bookings")
        for booking in restaurant.bookings:
            k += 1
            bookings = booking.get_details()
            if bookings != {}:
                if bookings['date'] == datetime.now().strftime("%Y-%m-%d") \
                        and bookings['end time'] >= datetime.now().strftime("%H:%M")\
                        or bookings['date'] > datetime.now().strftime("%Y-%m-%d"):
                    st.write(bookings)
                    if st.button(f"Delete booking {booking.guest.name}", key=f"delete_booking_{k}"):
                        result_booking = restaurant.delete_booking(booking)
                        st.success(result_booking)

    st.write("## Find available tables to take")
    number_guests_new = st.number_input("Number of guests", min_value=1, step=1)
    res_new = restaurant.get_available_tables(number_guests_new, False, datetime.now().date(), datetime.now().time())

    m = 1

    if not res_new:
        st.error("There are no available tables")
    else:
        for table in res_new:
            m += 1
            st.write(f"{table.name} - Seats: {table.seats}")
            if st.button("Take table", key=f"Take_table_{m}"):
                res_taken = take_table(table)
                st.success(res_taken)


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Table Management Page", "Booking Page", "Restaurant Status Page"])


if page == "Table Management Page":
    table_management_page()
elif page == "Booking Page":
    booking_page()
elif page == "Restaurant Status Page":
    restaurant_status_page()
