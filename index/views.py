from pathlib import Path

from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import sqlite3


# Create your views here.
@login_required(login_url='/login')
def index(request):
    # Trying the same code snippet again to fetch duplicates from the database

    # merge_duplicate_customers()
    return render(request, 'index/index.html')


def merge_duplicate_customers():
    # Define the database path
    BASE_DIR = Path(__file__).resolve().parent.parent
    db_path = BASE_DIR / "db_system.sqlite3"

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Get the list of duplicate customers
    cursor.execute('''
           SELECT name, contact_number, COUNT(*)
           FROM customer_customer
           WHERE name IS NOT NULL AND name != '' AND contact_number IS NOT NULL AND contact_number != ''
           GROUP BY name, contact_number
           HAVING COUNT(*) > 1
       ''')

    duplicates = cursor.fetchall()
    print("Duplicates:", duplicates)

    # Merge duplicate customers
    for name, contact_number, count in duplicates:
        cursor.execute('''
               SELECT id
               FROM customer_customer
               WHERE name = ? AND contact_number = ?
           ''', (name, contact_number))
        customer_ids = [row[0] for row in cursor.fetchall()]

        # Keep the first customer, merge others into this one
        primary_id = customer_ids[0]
        duplicate_ids = customer_ids[1:]

        for duplicate_id in duplicate_ids:
            # Update related records to point to the primary customer
            cursor.execute('''
                   UPDATE customer_customer_stats
                   SET customer_id = ?
                   WHERE customer_id = ?
               ''', (primary_id, duplicate_id))

            cursor.execute('''
                   UPDATE inquiry_inquiry
                   SET customer_name_id = ?
                   WHERE customer_name_id = ?
               ''', (primary_id, duplicate_id))

            cursor.execute('''
                              UPDATE registration_registration
                              SET customer_id = ?
                              WHERE customer_id = ?
                          ''', (primary_id, duplicate_id))

            # Delete the duplicate customer
            cursor.execute('DELETE FROM customer_customer WHERE id = ?', (duplicate_id,))

    conn.commit()
    conn.close()
    print("Duplicates merged successfully.")
