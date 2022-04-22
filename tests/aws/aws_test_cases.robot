*** Settings ***
Documentation   Some tests for AWS S3
Library         BuiltIn
Library         BucketVerification.py  ${ACCESS_KEY_ID}  ${SECRET_ACCESS_KEY}  ${REGION_NAME}


*** Variables ***
${ACCESS_KEY_ID}=       test_access_key_id
${SECRET_ACCESS_KEY}=   test_secret_access_key
${REGION_NAME}=         us-east-1
${BUCKET}=              test_bucket


*** Test Cases ***
Get bucket function should return an empty list if credentials are invalid
    ${expected}=    Create List
    ${actual}=      Get Bucket List
    Should Not Be True     ${actual}

Verify bucket encryption function should return 'Invalid credentials' if credentials are invalid
    ${expected}=    Set Variable    Invalid credentials
    ${actual}=      Verify Bucket Encryption    ${BUCKET}
    Should Be Equal As Strings      ${actual}   ${expected}