# Write Data in Google Sheets using Python and the Google Sheets API

## Store data to google sheet using `FORM`

### Step 1: Create a new project on the [Google Cloud Console](https://console.cloud.google.com)
To interact with the Google Sheet using python and the Google Sheet API, we have to create a new project on the Google Cloud Console. We have to enable the `Google Drive API` and `Google Sheets API` and use the credentials received to interact with the Google Sheet using python to create the project.

### Step2: Enable API's
To enable the Google Drive and the Google Sheets API, click on Go to `API overview`. On clicking Go to API overview, it will take to the `API dashboard`. To enable API's, we must click on the `library button` to show all available APIs.

### Step 3: Create a Service Account
1. Go to the credentials section by clicking on Credentials.
2. At the top, click on 1Create Credentials1.
3. On clicking Create Credentials, we will select `Service account`.
4. On creating a service account, we have to fill some details for the service account.
5. Now that the account is created, it's time to assign a role to the account, we will give it an Editor role.

### Step4: Get the Credentials
1. Click on the Service account you just created.
2. At the top, click on `KEYS`.
3. Click on `ADD KEY` and click on Create a `new key`.
4. On creating the key, we will be provided with options for the key type. Just go ahead and click on JSON.

### Step5: Add the Google Sheets API
1. Go to the API and overview.
2. Go to Enable API and services.
3. Search for the `Google Sheets API` and enable it.
