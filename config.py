# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

class BaseConfig(object):

    # Can be set to 'MasterUser' or 'ServicePrincipal'
    AUTHENTICATION_MODE = 'MasterUser'

    # Workspace Id in which the report is present
    WORKSPACE_ID = '9fba3e4e-05e6-400a-817a-b3f50f8636bd'
    
    # Report Id for which Embed token needs to be generated
    REPORT_ID = '0d7dcfbc-077e-4978-be48-29e124726c27'
    
    # Id of the Azure tenant in which AAD app and Power BI report is hosted. Required only for ServicePrincipal authentication mode.
    TENANT_ID = ''
    
    # Client Id (Application Id) of the AAD app
    CLIENT_ID = 'd6f8fed9-2db0-41c2-85d8-8a80b258e876'
    
    # Client Secret (App Secret) of the AAD app. Required only for ServicePrincipal authentication mode.
    CLIENT_SECRET = ''
    
    # Scope Base of AAD app. Use the below configuration to use all the permissions provided in the AAD app through Azure portal.
    SCOPE_BASE = ['https://analysis.windows.net/powerbi/api/.default']
    
    # URL used for initiating authorization request
    AUTHORITY_URL = 'https://login.microsoftonline.com/organizations'
    
    # Master user email address. Required only for MasterUser authentication mode.
    POWER_BI_USER = 'eslam.mohamed@smartlytics.co.uk'
    
    # Master user email password. Required only for MasterUser authentication mode.
    POWER_BI_PASS = 'Baw_1@4050'