Release Notes
=====================

Find here the new main features in the last versions.

Version 2.8.13 (Aug. 26th, 2017)
-----------------------------------

**Sales role**

- A 4-step sales process including Flight Confirmation.
- Pricing profiles intervals: you can now had a specific pricing profiles for flights occuring at short notice.
- Pricing profiles period calendar: you can define which profile is used by default in any period of time in a dedicated calendar.
- You can define a fixed fee for empty legs in the pricing profile and a specific minimum flight time for empty legs.
- You can now link accounts between them.
- Charter prices appear in the Cube export.

**Ops role**

- No more limitation on the number of crew in a roster
- Layout and Wording changes for expiry dates.
- Default expiry dates entries: a new pilot will have the default items with today’s date upon creation.

Version 2.8.10 (May 26th, 2017)
-------------------------------

**Sales role**

- Log for Reservation status change: time and person in charge is registered in the log of the reservation when the status is modified.

**Ops Role**

- Update Duty Start in a crew’s planning if the hour differs from the duration before flight registered in the FTL parameters.
- In the optimization algorithms, a new duty counter threshold is added, set by default to 95 hours in any 14 consecutive days.

Version 2.8.8 (Apr. 26th, 2017)
--------------------------------

**Sales role**

- Update of the Customer Structure with **Accounts** and **Contacts**:
    - Customers are treated as “Accounts”
    - Account could be either “Companies” or “Individuals”
    - Passengers are “Contacts” with a simplified form

- The customer list have an option to display Accounts, Contacts, or Both, and show which individuals or contacts is linked to an account.

**Pilot App**

- Pilots can now see the Next Available Check In in the Schedules/Duties page.

Version 2.8.4 (Mar. 16th, 2017)
---------------------------------

**Sales role**

- Empty legs are dissociated from Additional services so you can more precisely set the info you want show in your sales documents.
- Multi currency: you will find in your reservation a mean to change currency right under the total price. 
- You can manually edit the exchange rate in the reservation.
- The default exchange rates can be either fixed or updated live with the official rate from the European Central Bank. 
- The default exchanges rate can be set in the menu: pricing/ currencies list.
- All times are indicated with their reference: UTC or Local.
- The Customer form has been updated with new fields: 
    - Catering / Newspaper Preferences
    - Special Pricing Considerations
    - Family Information
    - Business Information
    - Likes
    - Dislikes

**OPS Role**

- You can now edit all flights items from the Calendar view.
- Please note that Sales team won’t get a notification but the reservation is updated accordingly.
- Quick access to Pending, Conflicts and Deleted legs in the future in the upper part of the Calendar view.
- Crew Changes and Aircraft maintenace are displayed in the Calendar view.
- Customizable Check List: you can create a Check List with the items you of your process and fil it per leg.
- FTL report: more complete with 7 days duty counter displayed by day.
- Ground staff planning and Pilot App access.

**Pilot App**

- You can enter the Fuel in the refueler unit, the pilot app makes automatically the conversion, given the density if needed.

Version 2.8.2 (Jan. 31th, 2017)
-----------------------------------

- You can add a flight attendant to your trip.
- Flight attendant are provided access to the pilot app.
- They have the same layout as for pilot and can see the schedule and catering remarks made there.
- A subcharter section is accessible in the calendar view to see “3rd. party charter” for awareness
- You can unset a FBO if handling is not needed (for an empty flight for instance).

Version 2.8.1 (Jan. 15th, 2017)
----------------------------------

This is a major release with new features and many changes in the architecture of our system.

**Sales role**

- Multi pricing: you can have more than one Pricing profile for your environment channel (B2B). Go to Pricing/ Pricing Profile and create a new pricing profile. Set a name and add a new channel set to B2B. Upon creation, you can copy content from another profile and update it. In the reservation, you can switch between up to 3 profiles set on B2B channel: leg prices and additional services are updated upon switching.

For further understanding about channels:

- B2B is for reservations made by you on your environment
- B2C is for reservation coming from our website OpenJet.com
- Agency is for reservation from travel agencies and Amadeus.

- Show details on a price:  If you get your mouse on the pie symbol next to the leg price in the Green portion for price, a bubble box will show you the details used for leg price calculation.

- Flight Numbers: If you provide us with your specific pattern to assign flight numbers, the flight number will be automatically generated for each reservation. Charter dedicated data are now sorted in the chronological order and show date

- View manager: in each table with data such as the Customer List, you can create a new view and choose displayed data columns in this view. Thus you can customize the date you want to export.

**OPS role**

- Expiration dates now have a control date to save initial occurence date and a free text for details. Expirations items are now ordered in the combo box.

- Calendar View. In the Settings section, you can select respectively from left to right: which tails are displayed, the airport code used (IATA, ICAO or FAA), date and duration on display, which types of flight are displayed, which flight status are displayed.

You can change dates on the upper left corner:

- The first icon is a date picker: the chosen date will appear on the leftmost day in the view.
- The simple arrow are to change dates by one day and the double arrow to change dates of the duration displayed.

- Click on a leg to edit it in a drawer on the right side.  Status are in the same as in the old flight list. You can interact on some flight status to edit the data in the corresponding tab. For each item you change in the drawer, click on save to update the database.

Version 2.7.1 (Dec. 12th, 2016)
-----------------------------------

- Link to ACU-K-WIK database.
- Link to PPS software.
- Link to CAMP software.

**PilotApp**

- Added PAX weight.

Version 2.7.0 (Oct. 28th, 2016)
----------------------------------

**PilotApp**

- Available on AppStore.
- See tutorial and details: Pilot App Tutorial.

**OPS role**

- Planning: it is not possible to assign the same person twice on an activity.

**Sales role**

- Edit ProForma.
- Comments in reservations are exportable in the Cube Export.

Version 2.6.0 (Aug. 17th, 2016)
----------------------------------

Customizable Start Page according to User role: 

- OPS : Dashboard, Flight List or planning overview.
- Sales : Dashboard or reservation list.

**Chief Pilot role**

- New format for FTL report

**Sales/Admin role**

- New reservation lists.
- Correction of spelling error on boarding pass.
- Data exports: – Yearly, monthly and weekly Revenue report – Legs list reports with filter on crew/tail
- Update of customer typification.

**OPS role**

- Resolution of a bug related to FTL calculation

Version 2.5.7 (Jun. 23th, 2016)
-------------------------------

- New Charter document customization. See Reservation section.

Version 2.5.6 (Jun. 10th, 2016)
-------------------------------

- New weight units management.
- Expiration dates can now be set for all crew on expiration date page. See Crew section.
- Flight list date filter. See Flight ops section.
