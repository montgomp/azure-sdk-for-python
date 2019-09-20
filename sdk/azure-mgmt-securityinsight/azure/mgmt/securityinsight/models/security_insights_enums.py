# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class AggregationsKind(str, Enum):

    cases_aggregation = "CasesAggregation"


class AlertRuleKind(str, Enum):

    scheduled = "Scheduled"
    microsoft_security_incident_creation = "MicrosoftSecurityIncidentCreation"
    fusion = "Fusion"


class DataTypeStatus(str, Enum):

    exist = "Exist"
    not_exist = "NotExist"


class TemplateStatus(str, Enum):

    installed = "Installed"  #: Alert rule template installed. and can not use more then once
    available = "Available"  #: Alert rule template is available.
    not_available = "NotAvailable"  #: Alert rule template is not available


class AttackTactic(str, Enum):

    initial_access = "InitialAccess"
    execution = "Execution"
    persistence = "Persistence"
    privilege_escalation = "PrivilegeEscalation"
    defense_evasion = "DefenseEvasion"
    credential_access = "CredentialAccess"
    discovery = "Discovery"
    lateral_movement = "LateralMovement"
    collection = "Collection"
    exfiltration = "Exfiltration"
    command_and_control = "CommandAndControl"
    impact = "Impact"


class TriggerOperator(str, Enum):

    greater_than = "GreaterThan"
    less_than = "LessThan"
    equal = "Equal"
    not_equal = "NotEqual"


class AlertSeverity(str, Enum):

    high = "High"  #: High severity
    medium = "Medium"  #: Medium severity
    low = "Low"  #: Low severity
    informational = "Informational"  #: Informational severity


class CloseReason(str, Enum):

    resolved = "Resolved"  #: Case was resolved
    dismissed = "Dismissed"  #: Case was dismissed
    true_positive = "TruePositive"  #: Case was true positive
    false_positive = "FalsePositive"  #: Case was false positive
    other = "Other"  #: Case was closed for another reason


class CaseSeverity(str, Enum):

    critical = "Critical"  #: Critical severity
    high = "High"  #: High severity
    medium = "Medium"  #: Medium severity
    low = "Low"  #: Low severity
    informational = "Informational"  #: Informational severity


class CaseStatus(str, Enum):

    draft = "Draft"  #: Case that wasn't promoted yet to active
    new = "New"  #: An active case which isn't handled currently
    in_progress = "InProgress"  #: An active case which is handled
    closed = "Closed"  #: A non active case


class DataTypeState(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class DataConnectorKind(str, Enum):

    azure_active_directory = "AzureActiveDirectory"
    azure_security_center = "AzureSecurityCenter"
    microsoft_cloud_app_security = "MicrosoftCloudAppSecurity"
    threat_intelligence = "ThreatIntelligence"
    office365 = "Office365"
    amazon_web_services_cloud_trail = "AmazonWebServicesCloudTrail"
    azure_advanced_threat_protection = "AzureAdvancedThreatProtection"
    microsoft_defender_advanced_threat_protection = "MicrosoftDefenderAdvancedThreatProtection"


class EntityKind(str, Enum):

    account = "Account"  #: Entity represents account in the system.
    host = "Host"  #: Entity represents host in the system.
    file = "File"  #: Entity represents file in the system.
    azure_resource = "AzureResource"  #: Entity represents azure resource in the system.
    cloud_application = "CloudApplication"  #: Entity represents cloud application in the system.
    dns_resolution = "DnsResolution"  #: Entity represents dns resolution in the system.
    file_hash = "FileHash"  #: Entity represents file hash in the system.
    ip = "Ip"  #: Entity represents ip in the system.
    malware = "Malware"  #: Entity represents malware in the system.
    process = "Process"  #: Entity represents process in the system.
    registry_key = "RegistryKey"  #: Entity represents registry key in the system.
    registry_value = "RegistryValue"  #: Entity represents registry value in the system.
    security_group = "SecurityGroup"  #: Entity represents security group in the system.
    url = "Url"  #: Entity represents url in the system.
    security_alert = "SecurityAlert"  #: Entity represents security alert in the system.
    bookmark = "Bookmark"  #: Entity represents bookmark in the system.


class EntityType(str, Enum):

    account = "Account"  #: Entity represents account in the system.
    host = "Host"  #: Entity represents host in the system.
    file = "File"  #: Entity represents file in the system.
    azure_resource = "AzureResource"  #: Entity represents azure resource in the system.
    cloud_application = "CloudApplication"  #: Entity represents cloud application in the system.
    dns = "DNS"  #: Entity represents dns in the system.
    file_hash = "FileHash"  #: Entity represents file hash in the system.
    ip = "IP"  #: Entity represents ip in the system.
    malware = "Malware"  #: Entity represents malware in the system.
    process = "Process"  #: Entity represents process in the system.
    registry_key = "RegistryKey"  #: Entity represents registry key in the system.
    registry_value = "RegistryValue"  #: Entity represents registry value in the system.
    security_group = "SecurityGroup"  #: Entity represents security group in the system.
    url = "URL"  #: Entity represents url in the system.
    security_alert = "SecurityAlert"  #: Entity represents security alert in the system.
    hunting_bookmark = "HuntingBookmark"  #: Entity represents HuntingBookmark in the system.


class FileHashAlgorithm(str, Enum):

    unknown = "Unknown"  #: Unknown hash algorithm
    md5 = "MD5"  #: MD5 hash type
    sha1 = "SHA1"  #: SHA1 hash type
    sha256 = "SHA256"  #: SHA256 hash type
    sha256_ac = "SHA256AC"  #: SHA256 Authenticode hash type


class OSFamily(str, Enum):

    linux = "Linux"  #: Host with Linux operating system.
    windows = "Windows"  #: Host with Windows operating system.
    android = "Android"  #: Host with Android operating system.
    ios = "IOS"  #: Host with IOS operating system.


class MicrosoftSecurityProductName(str, Enum):

    microsoft_cloud_app_security = "Microsoft Cloud App Security"
    azure_security_center = "Azure Security Center"
    azure_advanced_threat_protection = "Azure Advanced Threat Protection"
    azure_active_directory_identity_protection = "Azure Active Directory Identity Protection"


class ElevationToken(str, Enum):

    default = "Default"  #: Default elevation token
    full = "Full"  #: Full elevation token
    limited = "Limited"  #: Limited elevation token


class RegistryHive(str, Enum):

    hkey_local_machine = "HKEY_LOCAL_MACHINE"  #: HKEY_LOCAL_MACHINE
    hkey_classes_root = "HKEY_CLASSES_ROOT"  #: HKEY_CLASSES_ROOT
    hkey_current_config = "HKEY_CURRENT_CONFIG"  #: HKEY_CURRENT_CONFIG
    hkey_users = "HKEY_USERS"  #: HKEY_USERS
    hkey_current_user_local_settings = "HKEY_CURRENT_USER_LOCAL_SETTINGS"  #: HKEY_CURRENT_USER_LOCAL_SETTINGS
    hkey_performance_data = "HKEY_PERFORMANCE_DATA"  #: HKEY_PERFORMANCE_DATA
    hkey_performance_nlstext = "HKEY_PERFORMANCE_NLSTEXT"  #: HKEY_PERFORMANCE_NLSTEXT
    hkey_performance_text = "HKEY_PERFORMANCE_TEXT"  #: HKEY_PERFORMANCE_TEXT
    hkey_a = "HKEY_A"  #: HKEY_A
    hkey_current_user = "HKEY_CURRENT_USER"  #: HKEY_CURRENT_USER


class RegistryValueKind(str, Enum):

    none = "None"  #: None
    unknown = "Unknown"  #: Unknown value type
    string = "String"  #: String value type
    expand_string = "ExpandString"  #: ExpandString value type
    binary = "Binary"  #: Binary value type
    dword = "DWord"  #: DWord value type
    multi_string = "MultiString"  #: MultiString value type
    qword = "QWord"  #: QWord value type


class ConfidenceLevel(str, Enum):

    unknown = "Unknown"  #: Unknown confidence, the is the default value
    low = "Low"  #: Low confidence, meaning we have some doubts this is indeed malicious or part of an attack
    high = "High"  #: High confidence that the alert is true positive malicious


class ConfidenceScoreStatus(str, Enum):

    not_applicable = "NotApplicable"  #: Score will not be calculated for this alert as it is not supported by virtual analyst
    in_process = "InProcess"  #: No score was set yet and calculation is in progress
    not_final = "NotFinal"  #: Score is calculated and shown as part of the alert, but may be updated again at a later time following the processing of additional data
    final = "Final"  #: Final score was calculated and available


class KillChainIntent(str, Enum):

    unknown = "Unknown"  #: The default value.
    probing = "Probing"  #: Probing could be an attempt to access a certain resource regardless of a malicious intent or a failed attempt to gain access to a target system to gather information prior to exploitation. This step is usually detected as an attempt originating from outside the network in attempt to scan the target system and find a way in.
    exploitation = "Exploitation"  #: Exploitation is the stage where an attacker manage to get foothold on the attacked resource. This stage is applicable not only for compute hosts, but also for resources such as user accounts, certificates etc. Adversaries will often be able to control the resource after this stage.
    persistence = "Persistence"  #: Persistence is any access, action, or configuration change to a system that gives an adversary a persistent presence on that system. Adversaries will often need to maintain access to systems through interruptions such as system restarts, loss of credentials, or other failures that would require a remote access tool to restart or alternate backdoor for them to regain access.
    privilege_escalation = "PrivilegeEscalation"  #: Privilege escalation is the result of actions that allow an adversary to obtain a higher level of permissions on a system or network. Certain tools or actions require a higher level of privilege to work and are likely necessary at many points throughout an operation. User accounts with permissions to access specific systems or perform specific functions necessary for adversaries to achieve their objective may also be considered an escalation of privilege.
    defense_evasion = "DefenseEvasion"  #: Defense evasion consists of techniques an adversary may use to evade detection or avoid other defenses. Sometimes these actions are the same as or variations of techniques in other categories that have the added benefit of subverting a particular defense or mitigation.
    credential_access = "CredentialAccess"  #: Credential access represents techniques resulting in access to or control over system, domain, or service credentials that are used within an enterprise environment. Adversaries will likely attempt to obtain legitimate credentials from users or administrator accounts (local system administrator or domain users with administrator access) to use within the network. With sufficient access within a network, an adversary can create accounts for later use within the environment.
    discovery = "Discovery"  #: Discovery consists of techniques that allow the adversary to gain knowledge about the system and internal network. When adversaries gain access to a new system, they must orient themselves to what they now have control of and what benefits operating from that system give to their current objective or overall goals during the intrusion. The operating system provides many native tools that aid in this post-compromise information-gathering phase.
    lateral_movement = "LateralMovement"  #: Lateral movement consists of techniques that enable an adversary to access and control remote systems on a network and could, but does not necessarily, include execution of tools on remote systems. The lateral movement techniques could allow an adversary to gather information from a system without needing additional tools, such as a remote access tool. An adversary can use lateral movement for many purposes, including remote Execution of tools, pivoting to additional systems, access to specific information or files, access to additional credentials, or to cause an effect.
    execution = "Execution"  #: The execution tactic represents techniques that result in execution of adversary-controlled code on a local or remote system. This tactic is often used in conjunction with lateral movement to expand access to remote systems on a network.
    collection = "Collection"  #: Collection consists of techniques used to identify and gather information, such as sensitive files, from a target network prior to exfiltration. This category also covers locations on a system or network where the adversary may look for information to exfiltrate.
    exfiltration = "Exfiltration"  #: Exfiltration refers to techniques and attributes that result or aid in the adversary removing files and information from a target network. This category also covers locations on a system or network where the adversary may look for information to exfiltrate.
    command_and_control = "CommandAndControl"  #: The command and control tactic represents how adversaries communicate with systems under their control within a target network.
    impact = "Impact"  #: The impact intent primary objective is to directly reduce the availability or integrity of a system, service, or network; including manipulation of data to impact a business or operational process. This would often refer to techniques such as ransom-ware, defacement, data manipulation and others.


class AlertStatus(str, Enum):

    unknown = "Unknown"  #: Unknown value
    new = "New"  #: New alert
    resolved = "Resolved"  #: Alert closed after handling
    dismissed = "Dismissed"  #: Alert dismissed as false positive
    in_progress = "InProgress"  #: Alert is being handled


class SettingKind(str, Enum):

    ueba_settings = "UebaSettings"
    toggle_settings = "ToggleSettings"


class LicenseStatus(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"


class StatusInMcas(str, Enum):

    enabled = "Enabled"
    disabled = "Disabled"
