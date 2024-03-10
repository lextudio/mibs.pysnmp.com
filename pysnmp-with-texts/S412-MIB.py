"""SNMP MIB module (S412-MIB) expressed in pysnmp data model.

This Python module is designed to be imported and executed by the
pysnmp library.

See https://www.pysnmp.com/pysnmp for further information.

Notes
-----
ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S412-MIB
Produced by pysmi-1.3.3 at Sun Mar 10 11:43:41 2024
On host MacBook-Pro.local platform Darwin version 23.4.0 by user lextm
Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]
"""
if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint,
 ConstraintsUnion) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint",
    "ConstraintsUnion")

# Import SMI symbols from the MIBs this MIB depends on

(NotificationGroup,
 ModuleCompliance) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "NotificationGroup",
    "ModuleCompliance")

(Integer32,
 NotificationType,
 Gauge32,
 mgmt,
 MibIdentifier,
 ObjectIdentity,
 private,
 enterprises,
 Bits,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 iso,
 Counter32,
 TimeTicks,
 ModuleIdentity,
 IpAddress,
 Unsigned32,
 Counter64,
 internet,
 NotificationType) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Integer32",
    "NotificationType",
    "Gauge32",
    "mgmt",
    "MibIdentifier",
    "ObjectIdentity",
    "private",
    "enterprises",
    "Bits",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "iso",
    "Counter32",
    "TimeTicks",
    "ModuleIdentity",
    "IpAddress",
    "Unsigned32",
    "Counter64",
    "internet",
    "NotificationType")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Asentria_ObjectIdentity = ObjectIdentity
asentria = _Asentria_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052)
)
_S412_ObjectIdentity = ObjectIdentity
s412 = _S412_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41)
)
_Device_ObjectIdentity = ObjectIdentity
device = _Device_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1)
)
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 1),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialNumber.setDescription("""\
8-character serial number
""")
_FirmwareVersion_Type = DisplayString
_FirmwareVersion_Object = MibScalar
firmwareVersion = _FirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 2),
    _FirmwareVersion_Type()
)
firmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareVersion.setStatus("mandatory")
if mibBuilder.loadTexts:
    firmwareVersion.setDescription("""\
Firmware version text string
""")
_SiteID_Type = DisplayString
_SiteID_Object = MibScalar
siteID = _SiteID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 3),
    _SiteID_Type()
)
siteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    siteID.setStatus("mandatory")
if mibBuilder.loadTexts:
    siteID.setDescription("""\
Site Identifier, up to 12 characters.
""")
_SnmpManager_Type = IpAddress
_SnmpManager_Object = MibScalar
snmpManager = _SnmpManager_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 4),
    _SnmpManager_Type()
)
snmpManager.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManager.setStatus("deprecated")
if mibBuilder.loadTexts:
    snmpManager.setDescription("""\
This is snmp manager #1
""")
_ForceTraps_Type = Integer32
_ForceTraps_Object = MibScalar
forceTraps = _ForceTraps_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 6),
    _ForceTraps_Type()
)
forceTraps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    forceTraps.setStatus("mandatory")
if mibBuilder.loadTexts:
    forceTraps.setDescription("""\
Any write non-zero forces set of traps to be send to the SNMP Manager
""")
_ThisTrapText_Type = DisplayString
_ThisTrapText_Object = MibScalar
thisTrapText = _ThisTrapText_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 7),
    _ThisTrapText_Type()
)
thisTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thisTrapText.setStatus("mandatory")
if mibBuilder.loadTexts:
    thisTrapText.setDescription("""\
A text string included in all traps
""")
_AlarmStatus_Type = DisplayString
_AlarmStatus_Object = MibScalar
alarmStatus = _AlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 8),
    _AlarmStatus_Type()
)
alarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmStatus.setStatus("mandatory")
if mibBuilder.loadTexts:
    alarmStatus.setDescription("""\
A text status of all alarms
""")
_SnmpManager1_Type = IpAddress
_SnmpManager1_Object = MibScalar
snmpManager1 = _SnmpManager1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 9),
    _SnmpManager1_Type()
)
snmpManager1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManager1.setStatus("mandatory")
if mibBuilder.loadTexts:
    snmpManager1.setDescription("""\
SNMP manager #1
""")
_SnmpManager2_Type = IpAddress
_SnmpManager2_Object = MibScalar
snmpManager2 = _SnmpManager2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 10),
    _SnmpManager2_Type()
)
snmpManager2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManager2.setStatus("mandatory")
if mibBuilder.loadTexts:
    snmpManager2.setDescription("""\
SNMP manager #2
""")
_SnmpManager3_Type = IpAddress
_SnmpManager3_Object = MibScalar
snmpManager3 = _SnmpManager3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 11),
    _SnmpManager3_Type()
)
snmpManager3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManager3.setStatus("mandatory")
if mibBuilder.loadTexts:
    snmpManager3.setDescription("""\
SNMP manager #3
""")
_SnmpManager4_Type = IpAddress
_SnmpManager4_Object = MibScalar
snmpManager4 = _SnmpManager4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 12),
    _SnmpManager4_Type()
)
snmpManager4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpManager4.setStatus("mandatory")
if mibBuilder.loadTexts:
    snmpManager4.setDescription("""\
SNMP manager #4
""")
_StatusRepeatHours_Type = Integer32
_StatusRepeatHours_Object = MibScalar
statusRepeatHours = _StatusRepeatHours_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 13),
    _StatusRepeatHours_Type()
)
statusRepeatHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    statusRepeatHours.setStatus("mandatory")
if mibBuilder.loadTexts:
    statusRepeatHours.setDescription("""\
0=none, 1-24 Number of Hours between Status Traps being Sent
""")
_SerialTimeout_Type = Integer32
_SerialTimeout_Object = MibScalar
serialTimeout = _SerialTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 14),
    _SerialTimeout_Type()
)
serialTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTimeout.setStatus("mandatory")
if mibBuilder.loadTexts:
    serialTimeout.setDescription("""\
5-30, Minutes of non-activity timeout on serial setup
""")
_PowerupTrapsend_Type = Integer32
_PowerupTrapsend_Object = MibScalar
powerupTrapsend = _PowerupTrapsend_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 15),
    _PowerupTrapsend_Type()
)
powerupTrapsend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    powerupTrapsend.setStatus("mandatory")
if mibBuilder.loadTexts:
    powerupTrapsend.setDescription("""\
0-no, 1-yes, send traps for all sensors on powerup
""")
_NetlossTrapsend_Type = Integer32
_NetlossTrapsend_Object = MibScalar
netlossTrapsend = _NetlossTrapsend_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 16),
    _NetlossTrapsend_Type()
)
netlossTrapsend.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netlossTrapsend.setStatus("mandatory")
if mibBuilder.loadTexts:
    netlossTrapsend.setDescription("""\
0-no, 1-yes, send traps for detected netloss and back up
""")
_BuildID_Type = DisplayString
_BuildID_Object = MibScalar
buildID = _BuildID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 1, 17),
    _BuildID_Type()
)
buildID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    buildID.setStatus("mandatory")
if mibBuilder.loadTexts:
    buildID.setDescription("""\
5-chars max text for build identifier
""")
_Contacts_ObjectIdentity = ObjectIdentity
contacts = _Contacts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2)
)
_Contact1_ObjectIdentity = ObjectIdentity
contact1 = _Contact1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 1)
)
_Contact1Name_Type = DisplayString
_Contact1Name_Object = MibScalar
contact1Name = _Contact1Name_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 1, 1),
    _Contact1Name_Type()
)
contact1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact1Name.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact1Name.setDescription("""\
Name for contact, up to 30 characters
""")
_Contact1State_Type = Integer32
_Contact1State_Object = MibScalar
contact1State = _Contact1State_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 1, 2),
    _Contact1State_Type()
)
contact1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact1State.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact1State.setDescription("""\
Current State of Contact, 0-open 1-closed
""")
_Contact1AlarmEnable_Type = Integer32
_Contact1AlarmEnable_Object = MibScalar
contact1AlarmEnable = _Contact1AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 1, 3),
    _Contact1AlarmEnable_Type()
)
contact1AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact1AlarmEnable.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact1AlarmEnable.setDescription("""\
0-alarms disabled 1-alarms enabled
""")
_Contact1ActiveDirection_Type = Integer32
_Contact1ActiveDirection_Object = MibScalar
contact1ActiveDirection = _Contact1ActiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 1, 4),
    _Contact1ActiveDirection_Type()
)
contact1ActiveDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact1ActiveDirection.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact1ActiveDirection.setDescription("""\
0-alarm on open 1-alarm on closed
""")
_Contact1Threshold_Type = Integer32
_Contact1Threshold_Object = MibScalar
contact1Threshold = _Contact1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 1, 5),
    _Contact1Threshold_Type()
)
contact1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact1Threshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact1Threshold.setDescription("""\
Number of seconds that the contact must remain in a state before generating a
trap, range 0-255
""")
_Contact1ReturnNormalTrap_Type = Integer32
_Contact1ReturnNormalTrap_Object = MibScalar
contact1ReturnNormalTrap = _Contact1ReturnNormalTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 1, 6),
    _Contact1ReturnNormalTrap_Type()
)
contact1ReturnNormalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact1ReturnNormalTrap.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact1ReturnNormalTrap.setDescription("""\
0-return to normal traps not sent, 1-sent
""")
_Contact1TrapRepeat_Type = Integer32
_Contact1TrapRepeat_Object = MibScalar
contact1TrapRepeat = _Contact1TrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 1, 7),
    _Contact1TrapRepeat_Type()
)
contact1TrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact1TrapRepeat.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact1TrapRepeat.setDescription("""\
0-no repeats. 1-255 number of minutes between repeats of alarm traps.
""")
_Contact1Severity_Type = Integer32
_Contact1Severity_Object = MibScalar
contact1Severity = _Contact1Severity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 1, 8),
    _Contact1Severity_Type()
)
contact1Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact1Severity.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact1Severity.setDescription("""\
1-minor 2-major 3-critical 4-severe 5-warning
""")
_Contact2_ObjectIdentity = ObjectIdentity
contact2 = _Contact2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 2)
)
_Contact2Name_Type = DisplayString
_Contact2Name_Object = MibScalar
contact2Name = _Contact2Name_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 2, 1),
    _Contact2Name_Type()
)
contact2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact2Name.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact2Name.setDescription("""\
Name for contact, up to 30 characters
""")
_Contact2State_Type = Integer32
_Contact2State_Object = MibScalar
contact2State = _Contact2State_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 2, 2),
    _Contact2State_Type()
)
contact2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact2State.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact2State.setDescription("""\
Current State of Contact, 0-open 1-closed
""")
_Contact2AlarmEnable_Type = Integer32
_Contact2AlarmEnable_Object = MibScalar
contact2AlarmEnable = _Contact2AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 2, 3),
    _Contact2AlarmEnable_Type()
)
contact2AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact2AlarmEnable.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact2AlarmEnable.setDescription("""\
0-no alarms 1-alarms enabled
""")
_Contact2ActiveDirection_Type = Integer32
_Contact2ActiveDirection_Object = MibScalar
contact2ActiveDirection = _Contact2ActiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 2, 4),
    _Contact2ActiveDirection_Type()
)
contact2ActiveDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact2ActiveDirection.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact2ActiveDirection.setDescription("""\
0-alarm on open 1-alarm on closed
""")
_Contact2Threshold_Type = Integer32
_Contact2Threshold_Object = MibScalar
contact2Threshold = _Contact2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 2, 5),
    _Contact2Threshold_Type()
)
contact2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact2Threshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact2Threshold.setDescription("""\
Number of seconds must be in a state to be 'open' or 'closed'
""")
_Contact2ReturnNormalTrap_Type = Integer32
_Contact2ReturnNormalTrap_Object = MibScalar
contact2ReturnNormalTrap = _Contact2ReturnNormalTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 2, 6),
    _Contact2ReturnNormalTrap_Type()
)
contact2ReturnNormalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact2ReturnNormalTrap.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact2ReturnNormalTrap.setDescription("""\
0-not sent, 1-sent
""")
_Contact2TrapRepeat_Type = Integer32
_Contact2TrapRepeat_Object = MibScalar
contact2TrapRepeat = _Contact2TrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 2, 7),
    _Contact2TrapRepeat_Type()
)
contact2TrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact2TrapRepeat.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact2TrapRepeat.setDescription("""\
0-no repeats. 1-255 number of minutes between repeats of alarm traps
""")
_Contact2Severity_Type = Integer32
_Contact2Severity_Object = MibScalar
contact2Severity = _Contact2Severity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 2, 8),
    _Contact2Severity_Type()
)
contact2Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact2Severity.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact2Severity.setDescription("""\
1-minor 2-major 3-critical 4-severe 5-warning
""")
_Contact3_ObjectIdentity = ObjectIdentity
contact3 = _Contact3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 3)
)
_Contact3Name_Type = DisplayString
_Contact3Name_Object = MibScalar
contact3Name = _Contact3Name_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 3, 1),
    _Contact3Name_Type()
)
contact3Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact3Name.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact3Name.setDescription("""\
Name for contact, up to 30 characters
""")
_Contact3State_Type = Integer32
_Contact3State_Object = MibScalar
contact3State = _Contact3State_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 3, 2),
    _Contact3State_Type()
)
contact3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact3State.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact3State.setDescription("""\
Current State of Contact, 0-open 1-closed
""")
_Contact3AlarmEnable_Type = Integer32
_Contact3AlarmEnable_Object = MibScalar
contact3AlarmEnable = _Contact3AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 3, 3),
    _Contact3AlarmEnable_Type()
)
contact3AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact3AlarmEnable.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact3AlarmEnable.setDescription("""\
0-no alarms 1-alarms enabled
""")
_Contact3ActiveDirection_Type = Integer32
_Contact3ActiveDirection_Object = MibScalar
contact3ActiveDirection = _Contact3ActiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 3, 4),
    _Contact3ActiveDirection_Type()
)
contact3ActiveDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact3ActiveDirection.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact3ActiveDirection.setDescription("""\
0-alarm on open 1-alarm on closed
""")
_Contact3Threshold_Type = Integer32
_Contact3Threshold_Object = MibScalar
contact3Threshold = _Contact3Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 3, 5),
    _Contact3Threshold_Type()
)
contact3Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact3Threshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact3Threshold.setDescription("""\
Number of seconds must be in a state to be 'open' or 'closed'
""")
_Contact3ReturnNormalTrap_Type = Integer32
_Contact3ReturnNormalTrap_Object = MibScalar
contact3ReturnNormalTrap = _Contact3ReturnNormalTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 3, 6),
    _Contact3ReturnNormalTrap_Type()
)
contact3ReturnNormalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact3ReturnNormalTrap.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact3ReturnNormalTrap.setDescription("""\
0-not sent, 1-sent
""")
_Contact3TrapRepeat_Type = Integer32
_Contact3TrapRepeat_Object = MibScalar
contact3TrapRepeat = _Contact3TrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 3, 7),
    _Contact3TrapRepeat_Type()
)
contact3TrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact3TrapRepeat.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact3TrapRepeat.setDescription("""\
0-no repeats. 1-255 number of minutes between repeats of alarm traps
""")
_Contact3Severity_Type = Integer32
_Contact3Severity_Object = MibScalar
contact3Severity = _Contact3Severity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 3, 8),
    _Contact3Severity_Type()
)
contact3Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact3Severity.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact3Severity.setDescription("""\
1-minor 2-major 3-critical 4-severe 5-warning
""")
_Contact4_ObjectIdentity = ObjectIdentity
contact4 = _Contact4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 4)
)
_Contact4Name_Type = DisplayString
_Contact4Name_Object = MibScalar
contact4Name = _Contact4Name_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 4, 1),
    _Contact4Name_Type()
)
contact4Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact4Name.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact4Name.setDescription("""\
Name for contact, up to 30 characters
""")
_Contact4State_Type = Integer32
_Contact4State_Object = MibScalar
contact4State = _Contact4State_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 4, 2),
    _Contact4State_Type()
)
contact4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact4State.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact4State.setDescription("""\
Current State of Contact, 0-open 1-closed
""")
_Contact4AlarmEnable_Type = Integer32
_Contact4AlarmEnable_Object = MibScalar
contact4AlarmEnable = _Contact4AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 4, 3),
    _Contact4AlarmEnable_Type()
)
contact4AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact4AlarmEnable.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact4AlarmEnable.setDescription("""\
0-no alarms 1-alarms enabled
""")
_Contact4ActiveDirection_Type = Integer32
_Contact4ActiveDirection_Object = MibScalar
contact4ActiveDirection = _Contact4ActiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 4, 4),
    _Contact4ActiveDirection_Type()
)
contact4ActiveDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact4ActiveDirection.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact4ActiveDirection.setDescription("""\
0-alarm on open 1-alarm on closed
""")
_Contact4Threshold_Type = Integer32
_Contact4Threshold_Object = MibScalar
contact4Threshold = _Contact4Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 4, 5),
    _Contact4Threshold_Type()
)
contact4Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact4Threshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact4Threshold.setDescription("""\
Number of seconds must be in a state to be 'open' or 'closed'
""")
_Contact4ReturnNormalTrap_Type = Integer32
_Contact4ReturnNormalTrap_Object = MibScalar
contact4ReturnNormalTrap = _Contact4ReturnNormalTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 4, 6),
    _Contact4ReturnNormalTrap_Type()
)
contact4ReturnNormalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact4ReturnNormalTrap.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact4ReturnNormalTrap.setDescription("""\
0-not sent, 1-sent
""")
_Contact4TrapRepeat_Type = Integer32
_Contact4TrapRepeat_Object = MibScalar
contact4TrapRepeat = _Contact4TrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 4, 7),
    _Contact4TrapRepeat_Type()
)
contact4TrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact4TrapRepeat.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact4TrapRepeat.setDescription("""\
0-no repeats. 1-255 number of minutes between repeats of alarm traps
""")
_Contact4Severity_Type = Integer32
_Contact4Severity_Object = MibScalar
contact4Severity = _Contact4Severity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 4, 8),
    _Contact4Severity_Type()
)
contact4Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact4Severity.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact4Severity.setDescription("""\
1-minor 2-major 3-critical 4-severe 5-warning
""")
_Contact5_ObjectIdentity = ObjectIdentity
contact5 = _Contact5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 5)
)
_Contact5Name_Type = DisplayString
_Contact5Name_Object = MibScalar
contact5Name = _Contact5Name_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 5, 1),
    _Contact5Name_Type()
)
contact5Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact5Name.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact5Name.setDescription("""\
Name for contact, up to 30 characters
""")
_Contact5State_Type = Integer32
_Contact5State_Object = MibScalar
contact5State = _Contact5State_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 5, 2),
    _Contact5State_Type()
)
contact5State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact5State.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact5State.setDescription("""\
Current State of Contact, 0-open 1-closed
""")
_Contact5AlarmEnable_Type = Integer32
_Contact5AlarmEnable_Object = MibScalar
contact5AlarmEnable = _Contact5AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 5, 3),
    _Contact5AlarmEnable_Type()
)
contact5AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact5AlarmEnable.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact5AlarmEnable.setDescription("""\
0-no alarms 1-alarms enabled
""")
_Contact5ActiveDirection_Type = Integer32
_Contact5ActiveDirection_Object = MibScalar
contact5ActiveDirection = _Contact5ActiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 5, 4),
    _Contact5ActiveDirection_Type()
)
contact5ActiveDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact5ActiveDirection.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact5ActiveDirection.setDescription("""\
0-alarm on open 1-alarm on closed
""")
_Contact5Threshold_Type = Integer32
_Contact5Threshold_Object = MibScalar
contact5Threshold = _Contact5Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 5, 5),
    _Contact5Threshold_Type()
)
contact5Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact5Threshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact5Threshold.setDescription("""\
Number of seconds must be in a state to be 'open' or 'closed'
""")
_Contact5ReturnNormalTrap_Type = Integer32
_Contact5ReturnNormalTrap_Object = MibScalar
contact5ReturnNormalTrap = _Contact5ReturnNormalTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 5, 6),
    _Contact5ReturnNormalTrap_Type()
)
contact5ReturnNormalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact5ReturnNormalTrap.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact5ReturnNormalTrap.setDescription("""\
0-not sent, 1-sent
""")
_Contact5TrapRepeat_Type = Integer32
_Contact5TrapRepeat_Object = MibScalar
contact5TrapRepeat = _Contact5TrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 5, 7),
    _Contact5TrapRepeat_Type()
)
contact5TrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact5TrapRepeat.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact5TrapRepeat.setDescription("""\
0-no repeats. 1-255 number of minutes between repeats of alarm traps
""")
_Contact5Severity_Type = Integer32
_Contact5Severity_Object = MibScalar
contact5Severity = _Contact5Severity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 5, 8),
    _Contact5Severity_Type()
)
contact5Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact5Severity.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact5Severity.setDescription("""\
1-minor 2-major 3-critical 4-severe 5-warning
""")
_Contact6_ObjectIdentity = ObjectIdentity
contact6 = _Contact6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 6)
)
_Contact6Name_Type = DisplayString
_Contact6Name_Object = MibScalar
contact6Name = _Contact6Name_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 6, 1),
    _Contact6Name_Type()
)
contact6Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact6Name.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact6Name.setDescription("""\
Name for contact, up to 30 characters
""")
_Contact6State_Type = Integer32
_Contact6State_Object = MibScalar
contact6State = _Contact6State_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 6, 2),
    _Contact6State_Type()
)
contact6State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    contact6State.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact6State.setDescription("""\
Current State of Contact, 0-open 1-closed
""")
_Contact6AlarmEnable_Type = Integer32
_Contact6AlarmEnable_Object = MibScalar
contact6AlarmEnable = _Contact6AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 6, 3),
    _Contact6AlarmEnable_Type()
)
contact6AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact6AlarmEnable.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact6AlarmEnable.setDescription("""\
0-no alarms 1-alarms enabled
""")
_Contact6ActiveDirection_Type = Integer32
_Contact6ActiveDirection_Object = MibScalar
contact6ActiveDirection = _Contact6ActiveDirection_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 6, 4),
    _Contact6ActiveDirection_Type()
)
contact6ActiveDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact6ActiveDirection.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact6ActiveDirection.setDescription("""\
0-alarm on open 1-alarm on closed
""")
_Contact6Threshold_Type = Integer32
_Contact6Threshold_Object = MibScalar
contact6Threshold = _Contact6Threshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 6, 5),
    _Contact6Threshold_Type()
)
contact6Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact6Threshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact6Threshold.setDescription("""\
Number of seconds must be in a state to be 'open' or 'closed'
""")
_Contact6ReturnNormalTrap_Type = Integer32
_Contact6ReturnNormalTrap_Object = MibScalar
contact6ReturnNormalTrap = _Contact6ReturnNormalTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 6, 6),
    _Contact6ReturnNormalTrap_Type()
)
contact6ReturnNormalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact6ReturnNormalTrap.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact6ReturnNormalTrap.setDescription("""\
0-not sent, 1-sent
""")
_Contact6TrapRepeat_Type = Integer32
_Contact6TrapRepeat_Object = MibScalar
contact6TrapRepeat = _Contact6TrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 6, 7),
    _Contact6TrapRepeat_Type()
)
contact6TrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact6TrapRepeat.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact6TrapRepeat.setDescription("""\
0-no repeats. 1-255 number of minutes between repeats of alarm traps.
""")
_Contact6Severity_Type = Integer32
_Contact6Severity_Object = MibScalar
contact6Severity = _Contact6Severity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 2, 6, 8),
    _Contact6Severity_Type()
)
contact6Severity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    contact6Severity.setStatus("mandatory")
if mibBuilder.loadTexts:
    contact6Severity.setDescription("""\
1-minor 2-major 3-critical 4-severe 5-warning
""")
_Relays_ObjectIdentity = ObjectIdentity
relays = _Relays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 3)
)
_Relay1_ObjectIdentity = ObjectIdentity
relay1 = _Relay1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 3, 1)
)
_Relay1Name_Type = DisplayString
_Relay1Name_Object = MibScalar
relay1Name = _Relay1Name_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 3, 1, 1),
    _Relay1Name_Type()
)
relay1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1Name.setStatus("mandatory")
if mibBuilder.loadTexts:
    relay1Name.setDescription("""\
Name for relay, up to 30 characters
""")
_Relay1CurrentState_Type = Integer32
_Relay1CurrentState_Object = MibScalar
relay1CurrentState = _Relay1CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 3, 1, 2),
    _Relay1CurrentState_Type()
)
relay1CurrentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1CurrentState.setStatus("mandatory")
if mibBuilder.loadTexts:
    relay1CurrentState.setDescription("""\
0-opened, 1-closed
""")
_Relay1PowerupState_Type = Integer32
_Relay1PowerupState_Object = MibScalar
relay1PowerupState = _Relay1PowerupState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 3, 1, 3),
    _Relay1PowerupState_Type()
)
relay1PowerupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay1PowerupState.setStatus("mandatory")
if mibBuilder.loadTexts:
    relay1PowerupState.setDescription("""\
0-opened, 1-closed
""")
_Relay2_ObjectIdentity = ObjectIdentity
relay2 = _Relay2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 3, 2)
)
_Relay2Name_Type = DisplayString
_Relay2Name_Object = MibScalar
relay2Name = _Relay2Name_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 3, 2, 1),
    _Relay2Name_Type()
)
relay2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2Name.setStatus("mandatory")
if mibBuilder.loadTexts:
    relay2Name.setDescription("""\
Name for relay, up to 30 characters
""")
_Relay2CurrentState_Type = Integer32
_Relay2CurrentState_Object = MibScalar
relay2CurrentState = _Relay2CurrentState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 3, 2, 2),
    _Relay2CurrentState_Type()
)
relay2CurrentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2CurrentState.setStatus("mandatory")
if mibBuilder.loadTexts:
    relay2CurrentState.setDescription("""\
0-opened, 1-closed
""")
_Relay2PowerupState_Type = Integer32
_Relay2PowerupState_Object = MibScalar
relay2PowerupState = _Relay2PowerupState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 3, 2, 3),
    _Relay2PowerupState_Type()
)
relay2PowerupState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay2PowerupState.setStatus("mandatory")
if mibBuilder.loadTexts:
    relay2PowerupState.setDescription("""\
0-opened, 1-closed
""")
_Tempsensor_ObjectIdentity = ObjectIdentity
tempsensor = _Tempsensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4)
)
_TempValue_Type = Integer32
_TempValue_Object = MibScalar
tempValue = _TempValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 1),
    _TempValue_Type()
)
tempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tempValue.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempValue.setDescription("""\
Current Temperature Value, in C or F based on 1.3.6.1.4.1.3052.41.4.10
""")
_TempAlarmEnable_Type = Integer32
_TempAlarmEnable_Object = MibScalar
tempAlarmEnable = _TempAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 2),
    _TempAlarmEnable_Type()
)
tempAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempAlarmEnable.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempAlarmEnable.setDescription("""\
0=alarms disabled, 1=alarms enabled
""")
_TempHighLevel_Type = Integer32
_TempHighLevel_Object = MibScalar
tempHighLevel = _TempHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 3),
    _TempHighLevel_Type()
)
tempHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHighLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempHighLevel.setDescription("""\
Level at which the High alarm goes active
""")
_TempVeryHighLevel_Type = Integer32
_TempVeryHighLevel_Object = MibScalar
tempVeryHighLevel = _TempVeryHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 4),
    _TempVeryHighLevel_Type()
)
tempVeryHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempVeryHighLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempVeryHighLevel.setDescription("""\
Level at which the Very High alarm goes active
""")
_TempLowLevel_Type = Integer32
_TempLowLevel_Object = MibScalar
tempLowLevel = _TempLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 5),
    _TempLowLevel_Type()
)
tempLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempLowLevel.setDescription("""\
Level at which the Low alarm goes active
""")
_TempVeryLowLevel_Type = Integer32
_TempVeryLowLevel_Object = MibScalar
tempVeryLowLevel = _TempVeryLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 6),
    _TempVeryLowLevel_Type()
)
tempVeryLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempVeryLowLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempVeryLowLevel.setDescription("""\
Level at which the Very Low alarm goes active
""")
_TempAlarmThreshold_Type = Integer32
_TempAlarmThreshold_Object = MibScalar
tempAlarmThreshold = _TempAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 7),
    _TempAlarmThreshold_Type()
)
tempAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempAlarmThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempAlarmThreshold.setDescription("""\
Seconds must be in a range to be an alarm
""")
_TempReturnNormalTrap_Type = Integer32
_TempReturnNormalTrap_Object = MibScalar
tempReturnNormalTrap = _TempReturnNormalTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 8),
    _TempReturnNormalTrap_Type()
)
tempReturnNormalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempReturnNormalTrap.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempReturnNormalTrap.setDescription("""\
0-not sent, 1-send trap on return to normal range
""")
_TempTrapRepeat_Type = Integer32
_TempTrapRepeat_Object = MibScalar
tempTrapRepeat = _TempTrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 9),
    _TempTrapRepeat_Type()
)
tempTrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempTrapRepeat.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempTrapRepeat.setDescription("""\
0-no repeats. 1-255 number of minutes between repeats of alarm traps.
""")
_TempMode_Type = Integer32
_TempMode_Object = MibScalar
tempMode = _TempMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 10),
    _TempMode_Type()
)
tempMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempMode.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempMode.setDescription("""\
0=all temp readings and levels in degrees F, 1=in degrees C
""")
_TempHighSeverity_Type = Integer32
_TempHighSeverity_Object = MibScalar
tempHighSeverity = _TempHighSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 11),
    _TempHighSeverity_Type()
)
tempHighSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempHighSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempHighSeverity.setDescription("""\
High Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_TempVeryHighSeverity_Type = Integer32
_TempVeryHighSeverity_Object = MibScalar
tempVeryHighSeverity = _TempVeryHighSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 12),
    _TempVeryHighSeverity_Type()
)
tempVeryHighSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempVeryHighSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempVeryHighSeverity.setDescription("""\
Very High Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_TempLowSeverity_Type = Integer32
_TempLowSeverity_Object = MibScalar
tempLowSeverity = _TempLowSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 13),
    _TempLowSeverity_Type()
)
tempLowSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempLowSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempLowSeverity.setDescription("""\
Low Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_TempVeryLowSeverity_Type = Integer32
_TempVeryLowSeverity_Object = MibScalar
tempVeryLowSeverity = _TempVeryLowSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 14),
    _TempVeryLowSeverity_Type()
)
tempVeryLowSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempVeryLowSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempVeryLowSeverity.setDescription("""\
Very Low Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_TempName_Type = DisplayString
_TempName_Object = MibScalar
tempName = _TempName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 4, 15),
    _TempName_Type()
)
tempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tempName.setStatus("mandatory")
if mibBuilder.loadTexts:
    tempName.setDescription("""\
Name for temperature sensor, up to 30 characters
""")
_Humiditysensor_ObjectIdentity = ObjectIdentity
humiditysensor = _Humiditysensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5)
)
_HumidityValue_Type = Integer32
_HumidityValue_Object = MibScalar
humidityValue = _HumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 1),
    _HumidityValue_Type()
)
humidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    humidityValue.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityValue.setDescription("""\
Current Relative Humidity Value (0-100%)
""")
_HumidityAlarmEnable_Type = Integer32
_HumidityAlarmEnable_Object = MibScalar
humidityAlarmEnable = _HumidityAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 2),
    _HumidityAlarmEnable_Type()
)
humidityAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityAlarmEnable.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityAlarmEnable.setDescription("""\
0=alarms disabled, 1=alarms enabled
""")
_HumidityHighLevel_Type = Integer32
_HumidityHighLevel_Object = MibScalar
humidityHighLevel = _HumidityHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 3),
    _HumidityHighLevel_Type()
)
humidityHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityHighLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityHighLevel.setDescription("""\
Level at which the High alarm goes active
""")
_HumidityVeryHighLevel_Type = Integer32
_HumidityVeryHighLevel_Object = MibScalar
humidityVeryHighLevel = _HumidityVeryHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 4),
    _HumidityVeryHighLevel_Type()
)
humidityVeryHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityVeryHighLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityVeryHighLevel.setDescription("""\
Level at which the Very High alarm goes active
""")
_HumidityLowLevel_Type = Integer32
_HumidityLowLevel_Object = MibScalar
humidityLowLevel = _HumidityLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 5),
    _HumidityLowLevel_Type()
)
humidityLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityLowLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityLowLevel.setDescription("""\
Level at which the Low alarm goes active
""")
_HumidityVeryLowLevel_Type = Integer32
_HumidityVeryLowLevel_Object = MibScalar
humidityVeryLowLevel = _HumidityVeryLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 6),
    _HumidityVeryLowLevel_Type()
)
humidityVeryLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityVeryLowLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityVeryLowLevel.setDescription("""\
Level at which the Very Low alarm goes active
""")
_HumidityAlarmThreshold_Type = Integer32
_HumidityAlarmThreshold_Object = MibScalar
humidityAlarmThreshold = _HumidityAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 7),
    _HumidityAlarmThreshold_Type()
)
humidityAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityAlarmThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityAlarmThreshold.setDescription("""\
Seconds must be in a range to be an alarm
""")
_HumidityReturnNormalTrap_Type = Integer32
_HumidityReturnNormalTrap_Object = MibScalar
humidityReturnNormalTrap = _HumidityReturnNormalTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 8),
    _HumidityReturnNormalTrap_Type()
)
humidityReturnNormalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityReturnNormalTrap.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityReturnNormalTrap.setDescription("""\
0-not sent, 1-send trap on return to normal range
""")
_HumidityTrapRepeat_Type = Integer32
_HumidityTrapRepeat_Object = MibScalar
humidityTrapRepeat = _HumidityTrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 9),
    _HumidityTrapRepeat_Type()
)
humidityTrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityTrapRepeat.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityTrapRepeat.setDescription("""\
0-no repeats. 1-255 number of minutes between repeats of alarm traps.
""")
_HumidityHighSeverity_Type = Integer32
_HumidityHighSeverity_Object = MibScalar
humidityHighSeverity = _HumidityHighSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 10),
    _HumidityHighSeverity_Type()
)
humidityHighSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityHighSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityHighSeverity.setDescription("""\
High Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_HumidityVeryHighSeverity_Type = Integer32
_HumidityVeryHighSeverity_Object = MibScalar
humidityVeryHighSeverity = _HumidityVeryHighSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 11),
    _HumidityVeryHighSeverity_Type()
)
humidityVeryHighSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityVeryHighSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityVeryHighSeverity.setDescription("""\
Very High Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_HumidityLowSeverity_Type = Integer32
_HumidityLowSeverity_Object = MibScalar
humidityLowSeverity = _HumidityLowSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 12),
    _HumidityLowSeverity_Type()
)
humidityLowSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityLowSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityLowSeverity.setDescription("""\
Low Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_HumidityVeryLowSeverity_Type = Integer32
_HumidityVeryLowSeverity_Object = MibScalar
humidityVeryLowSeverity = _HumidityVeryLowSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 13),
    _HumidityVeryLowSeverity_Type()
)
humidityVeryLowSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityVeryLowSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityVeryLowSeverity.setDescription("""\
Very Low Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_HumidityName_Type = DisplayString
_HumidityName_Object = MibScalar
humidityName = _HumidityName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 5, 14),
    _HumidityName_Type()
)
humidityName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    humidityName.setStatus("mandatory")
if mibBuilder.loadTexts:
    humidityName.setDescription("""\
Name for humidity sensor, up to 30 characters
""")
_Passthrough_ObjectIdentity = ObjectIdentity
passthrough = _Passthrough_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6)
)
_PtNeedPassword_Type = Integer32
_PtNeedPassword_Object = MibScalar
ptNeedPassword = _PtNeedPassword_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 1),
    _PtNeedPassword_Type()
)
ptNeedPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptNeedPassword.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptNeedPassword.setDescription("""\
0-no 1-yes, is password required for passthrough connection.
""")
_PtSayLoginText_Type = Integer32
_PtSayLoginText_Object = MibScalar
ptSayLoginText = _PtSayLoginText_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 2),
    _PtSayLoginText_Type()
)
ptSayLoginText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptSayLoginText.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptSayLoginText.setDescription("""\
0-no 1-yes, is passthrough login text displayed on connection.
""")
_PtLoginText_Type = DisplayString
_PtLoginText_Object = MibScalar
ptLoginText = _PtLoginText_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 3),
    _PtLoginText_Type()
)
ptLoginText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptLoginText.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptLoginText.setDescription("""\
0-24 char string which may be displayed on socket connection. Requires that
ptSayLoginText be enabled to display this string.
""")
_PtSaySiteID_Type = Integer32
_PtSaySiteID_Object = MibScalar
ptSaySiteID = _PtSaySiteID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 4),
    _PtSaySiteID_Type()
)
ptSaySiteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptSaySiteID.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptSaySiteID.setDescription("""\
0-no 1-yes, is SiteID displayed on pass through connection.
""")
_PtUsername_Type = DisplayString
_PtUsername_Object = MibScalar
ptUsername = _PtUsername_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 5),
    _PtUsername_Type()
)
ptUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptUsername.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptUsername.setDescription("""\
0-16 char string for Username used in serial passthrough connections
""")
_PtPassword_Type = DisplayString
_PtPassword_Object = MibScalar
ptPassword = _PtPassword_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 6),
    _PtPassword_Type()
)
ptPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptPassword.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptPassword.setDescription("""\
0-16 char string for Password used in serial passthrough connections
""")
_PtTimeout_Type = Integer32
_PtTimeout_Object = MibScalar
ptTimeout = _PtTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 7),
    _PtTimeout_Type()
)
ptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptTimeout.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptTimeout.setDescription("""\
number of minutes (1-255) of idle activity (both directions) which causes
disconnect. 0-never
""")
_PtEscChar_Type = Integer32
_PtEscChar_Object = MibScalar
ptEscChar = _PtEscChar_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 8),
    _PtEscChar_Type()
)
ptEscChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptEscChar.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptEscChar.setDescription("""\
ASCII character code (e.g, Escape=27) which if entered on the tcp port three
times in a row causes disconnect. 0-none
""")
_PtLfstripToPort_Type = Integer32
_PtLfstripToPort_Object = MibScalar
ptLfstripToPort = _PtLfstripToPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 9),
    _PtLfstripToPort_Type()
)
ptLfstripToPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptLfstripToPort.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptLfstripToPort.setDescription("""\
0-no 1-yes linefeed characters received on TCP connection are removed from
stream to serial port
""")
_PtLfstripFromPort_Type = Integer32
_PtLfstripFromPort_Object = MibScalar
ptLfstripFromPort = _PtLfstripFromPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 10),
    _PtLfstripFromPort_Type()
)
ptLfstripFromPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptLfstripFromPort.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptLfstripFromPort.setDescription("""\
0-no 1-yes linefeed characters received on serial port are removed from stream
to TCP connection
""")
_PtSerialBaudrate_Type = Integer32
_PtSerialBaudrate_Object = MibScalar
ptSerialBaudrate = _PtSerialBaudrate_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 11),
    _PtSerialBaudrate_Type()
)
ptSerialBaudrate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptSerialBaudrate.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptSerialBaudrate.setDescription("""\
300 600 1200 2400 4800 9600 19200 baud are allowed values
""")
_PtSerialWordlength_Type = Integer32
_PtSerialWordlength_Object = MibScalar
ptSerialWordlength = _PtSerialWordlength_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 12),
    _PtSerialWordlength_Type()
)
ptSerialWordlength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptSerialWordlength.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptSerialWordlength.setDescription("""\
7 or 8 bit word selection
""")
_PtSerialParity_Type = DisplayString
_PtSerialParity_Object = MibScalar
ptSerialParity = _PtSerialParity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 13),
    _PtSerialParity_Type()
)
ptSerialParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptSerialParity.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptSerialParity.setDescription("""\
N E O are allowed values for parity (none, even, odd) [a single-character
string]
""")
_PtTCPPortnumber_Type = Integer32
_PtTCPPortnumber_Object = MibScalar
ptTCPPortnumber = _PtTCPPortnumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 6, 14),
    _PtTCPPortnumber_Type()
)
ptTCPPortnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ptTCPPortnumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    ptTCPPortnumber.setDescription("""\
IP port number for passthrough connection (range 1024-65534)
""")
_Ftp_ObjectIdentity = ObjectIdentity
ftp = _Ftp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 7)
)
_FtpUsername_Type = DisplayString
_FtpUsername_Object = MibScalar
ftpUsername = _FtpUsername_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 7, 1),
    _FtpUsername_Type()
)
ftpUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpUsername.setStatus("mandatory")
if mibBuilder.loadTexts:
    ftpUsername.setDescription("""\
0-16 char string for Username used in ftp server for updates
""")
_FtpPassword_Type = DisplayString
_FtpPassword_Object = MibScalar
ftpPassword = _FtpPassword_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 7, 2),
    _FtpPassword_Type()
)
ftpPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPassword.setStatus("mandatory")
if mibBuilder.loadTexts:
    ftpPassword.setDescription("""\
0-16 char string for Password used in ftp server for updates
""")
_Analog_ObjectIdentity = ObjectIdentity
analog = _Analog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8)
)
_Analog1_ObjectIdentity = ObjectIdentity
analog1 = _Analog1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1)
)
_Analog1Value_Type = Integer32
_Analog1Value_Object = MibScalar
analog1Value = _Analog1Value_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 1),
    _Analog1Value_Type()
)
analog1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog1Value.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1Value.setDescription("""\
Value of current analog reading, in 1/100 volt, +- 9999 range
""")
_Analog1AlarmEnable_Type = Integer32
_Analog1AlarmEnable_Object = MibScalar
analog1AlarmEnable = _Analog1AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 2),
    _Analog1AlarmEnable_Type()
)
analog1AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1AlarmEnable.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1AlarmEnable.setDescription("""\
0=no alarms, 1=send alarms
""")
_Analog1HighLevel_Type = Integer32
_Analog1HighLevel_Object = MibScalar
analog1HighLevel = _Analog1HighLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 3),
    _Analog1HighLevel_Type()
)
analog1HighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1HighLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1HighLevel.setDescription("""\
Level at which the High alarm goes active
""")
_Analog1VeryHighLevel_Type = Integer32
_Analog1VeryHighLevel_Object = MibScalar
analog1VeryHighLevel = _Analog1VeryHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 4),
    _Analog1VeryHighLevel_Type()
)
analog1VeryHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1VeryHighLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1VeryHighLevel.setDescription("""\
Level at which the Very High alarm goes active
""")
_Analog1LowLevel_Type = Integer32
_Analog1LowLevel_Object = MibScalar
analog1LowLevel = _Analog1LowLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 5),
    _Analog1LowLevel_Type()
)
analog1LowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1LowLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1LowLevel.setDescription("""\
Level at which the Low alarm goes active
""")
_Analog1VeryLowLevel_Type = Integer32
_Analog1VeryLowLevel_Object = MibScalar
analog1VeryLowLevel = _Analog1VeryLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 6),
    _Analog1VeryLowLevel_Type()
)
analog1VeryLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1VeryLowLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1VeryLowLevel.setDescription("""\
Level at which the Very Low alarm goes active
""")
_Analog1AlarmThreshold_Type = Integer32
_Analog1AlarmThreshold_Object = MibScalar
analog1AlarmThreshold = _Analog1AlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 7),
    _Analog1AlarmThreshold_Type()
)
analog1AlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1AlarmThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1AlarmThreshold.setDescription("""\
Seconds must be in a range to be an alarm
""")
_Analog1ReturnNormalTrap_Type = Integer32
_Analog1ReturnNormalTrap_Object = MibScalar
analog1ReturnNormalTrap = _Analog1ReturnNormalTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 8),
    _Analog1ReturnNormalTrap_Type()
)
analog1ReturnNormalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1ReturnNormalTrap.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1ReturnNormalTrap.setDescription("""\
0-not sent, 1-send trap on return to normal range
""")
_Analog1TrapRepeat_Type = Integer32
_Analog1TrapRepeat_Object = MibScalar
analog1TrapRepeat = _Analog1TrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 9),
    _Analog1TrapRepeat_Type()
)
analog1TrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1TrapRepeat.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1TrapRepeat.setDescription("""\
0-no repeats else number of minutes between repeats of trap
""")
_Analog1HighSeverity_Type = Integer32
_Analog1HighSeverity_Object = MibScalar
analog1HighSeverity = _Analog1HighSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 10),
    _Analog1HighSeverity_Type()
)
analog1HighSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1HighSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1HighSeverity.setDescription("""\
High Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_Analog1VeryHighSeverity_Type = Integer32
_Analog1VeryHighSeverity_Object = MibScalar
analog1VeryHighSeverity = _Analog1VeryHighSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 11),
    _Analog1VeryHighSeverity_Type()
)
analog1VeryHighSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1VeryHighSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1VeryHighSeverity.setDescription("""\
Very High Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_Analog1LowSeverity_Type = Integer32
_Analog1LowSeverity_Object = MibScalar
analog1LowSeverity = _Analog1LowSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 12),
    _Analog1LowSeverity_Type()
)
analog1LowSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1LowSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1LowSeverity.setDescription("""\
Low Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_Analog1VeryLowSeverity_Type = Integer32
_Analog1VeryLowSeverity_Object = MibScalar
analog1VeryLowSeverity = _Analog1VeryLowSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 13),
    _Analog1VeryLowSeverity_Type()
)
analog1VeryLowSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1VeryLowSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1VeryLowSeverity.setDescription("""\
Very Low Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_Analog1Name_Type = DisplayString
_Analog1Name_Object = MibScalar
analog1Name = _Analog1Name_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 1, 14),
    _Analog1Name_Type()
)
analog1Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog1Name.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog1Name.setDescription("""\
Name for analog sensor 1, up to 30 characters
""")
_Analog2_ObjectIdentity = ObjectIdentity
analog2 = _Analog2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2)
)
_Analog2Value_Type = Integer32
_Analog2Value_Object = MibScalar
analog2Value = _Analog2Value_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 1),
    _Analog2Value_Type()
)
analog2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog2Value.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2Value.setDescription("""\
Value of current analog reading, in 1/100 volt, +- 9999 range
""")
_Analog2AlarmEnable_Type = Integer32
_Analog2AlarmEnable_Object = MibScalar
analog2AlarmEnable = _Analog2AlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 2),
    _Analog2AlarmEnable_Type()
)
analog2AlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2AlarmEnable.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2AlarmEnable.setDescription("""\
0=no alarms, 1=send alarms
""")
_Analog2HighLevel_Type = Integer32
_Analog2HighLevel_Object = MibScalar
analog2HighLevel = _Analog2HighLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 3),
    _Analog2HighLevel_Type()
)
analog2HighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2HighLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2HighLevel.setDescription("""\
Level at which the High alarm goes active
""")
_Analog2VeryHighLevel_Type = Integer32
_Analog2VeryHighLevel_Object = MibScalar
analog2VeryHighLevel = _Analog2VeryHighLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 4),
    _Analog2VeryHighLevel_Type()
)
analog2VeryHighLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2VeryHighLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2VeryHighLevel.setDescription("""\
Level at which the Very High alarm goes active
""")
_Analog2LowLevel_Type = Integer32
_Analog2LowLevel_Object = MibScalar
analog2LowLevel = _Analog2LowLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 5),
    _Analog2LowLevel_Type()
)
analog2LowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2LowLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2LowLevel.setDescription("""\
Level at which the Low alarm goes active
""")
_Analog2VeryLowLevel_Type = Integer32
_Analog2VeryLowLevel_Object = MibScalar
analog2VeryLowLevel = _Analog2VeryLowLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 6),
    _Analog2VeryLowLevel_Type()
)
analog2VeryLowLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2VeryLowLevel.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2VeryLowLevel.setDescription("""\
Level at which the Very Low alarm goes active
""")
_Analog2AlarmThreshold_Type = Integer32
_Analog2AlarmThreshold_Object = MibScalar
analog2AlarmThreshold = _Analog2AlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 7),
    _Analog2AlarmThreshold_Type()
)
analog2AlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2AlarmThreshold.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2AlarmThreshold.setDescription("""\
Seconds must be in a range to be an alarm
""")
_Analog2ReturnNormalTrap_Type = Integer32
_Analog2ReturnNormalTrap_Object = MibScalar
analog2ReturnNormalTrap = _Analog2ReturnNormalTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 8),
    _Analog2ReturnNormalTrap_Type()
)
analog2ReturnNormalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2ReturnNormalTrap.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2ReturnNormalTrap.setDescription("""\
0-not sent, 1-send trap on return to normal range
""")
_Analog2TrapRepeat_Type = Integer32
_Analog2TrapRepeat_Object = MibScalar
analog2TrapRepeat = _Analog2TrapRepeat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 9),
    _Analog2TrapRepeat_Type()
)
analog2TrapRepeat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2TrapRepeat.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2TrapRepeat.setDescription("""\
0-no repeats else number of minutes between repeats of trap
""")
_Analog2HighSeverity_Type = Integer32
_Analog2HighSeverity_Object = MibScalar
analog2HighSeverity = _Analog2HighSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 10),
    _Analog2HighSeverity_Type()
)
analog2HighSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2HighSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2HighSeverity.setDescription("""\
High Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_Analog2VeryHighSeverity_Type = Integer32
_Analog2VeryHighSeverity_Object = MibScalar
analog2VeryHighSeverity = _Analog2VeryHighSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 11),
    _Analog2VeryHighSeverity_Type()
)
analog2VeryHighSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2VeryHighSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2VeryHighSeverity.setDescription("""\
Very High Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_Analog2LowSeverity_Type = Integer32
_Analog2LowSeverity_Object = MibScalar
analog2LowSeverity = _Analog2LowSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 12),
    _Analog2LowSeverity_Type()
)
analog2LowSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2LowSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2LowSeverity.setDescription("""\
Low Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_Analog2VeryLowSeverity_Type = Integer32
_Analog2VeryLowSeverity_Object = MibScalar
analog2VeryLowSeverity = _Analog2VeryLowSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 13),
    _Analog2VeryLowSeverity_Type()
)
analog2VeryLowSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2VeryLowSeverity.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2VeryLowSeverity.setDescription("""\
Very Low Level Severity 1-minor 2-major 3-critical 4-severe 5-warning
""")
_Analog2Name_Type = DisplayString
_Analog2Name_Object = MibScalar
analog2Name = _Analog2Name_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 8, 2, 14),
    _Analog2Name_Type()
)
analog2Name.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    analog2Name.setStatus("mandatory")
if mibBuilder.loadTexts:
    analog2Name.setDescription("""\
Name for analog sensor 2, up to 30 characters
""")
_EventSensorStatus_ObjectIdentity = ObjectIdentity
eventSensorStatus = _EventSensorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 10)
)
_EsPointTable_Object = MibTable
esPointTable = _EsPointTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 10, 1)
)
if mibBuilder.loadTexts:
    esPointTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    esPointTable.setDescription("""\
 This table organizes 4 basic attributes of points. A point is a particular
sensor on an EventSensor (e.g., temperature, humidity, contact closure 2, relay
5, etc.). The 4 point attributes are its name, whether it's in its event state,
the point's value as a number and its value as a string. Points are referenced
by a point index. The point index is a string of 3 numbers separated by
periods. It contains all the information necessary for getting a piece of data
off an event sensor; namely, which EventSensor, point class, and which-sensor-
of-that-class (a.k.a. point).
""")
_EsPointEntry_Object = MibTableRow
esPointEntry = _EsPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 10, 1, 1)
)
esPointEntry.setIndexNames(
    (0, "S412-MIB", "esIndexES"),
    (0, "S412-MIB", "esIndexPC"),
    (0, "S412-MIB", "esIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    esPointEntry.setDescription("""\
Entry for EventSensor point table
""")
_EsIndexES_Type = Integer32
_EsIndexES_Object = MibTableColumn
esIndexES = _EsIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 10, 1, 1, 1),
    _EsIndexES_Type()
)
esIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexES.setStatus("mandatory")
if mibBuilder.loadTexts:
    esIndexES.setDescription("""\
The part of the point index that refers to an EventSensor. The point index is a
string of 3 numbers separated by periods. It contains all the information
necessary for getting a piece of data off an event sensor; namely, which
EventSensor, point class, and which-sensor-of-that-class (a.k.a. point). This
object's allowable values are 1 through 4, which refer to attached
EventSensors. The number corresponding to an EventSensor is determined by the
user at the initial configuration time. If there is an internal sensor in the
unit, it will always be the first item in the Sensor Events setup menu. For
example, if a new EventSensor is configured as the 2nd entry AFTER the internal
EventSensor (if one exists) in the Sensor Events Setup Menu, then that
EventSensor will be known from then on as EventSensor 2. All point indeces with
esIndexES=2 will now refer to that particular EventSensor.
""")
_EsIndexPC_Type = Integer32
_EsIndexPC_Object = MibTableColumn
esIndexPC = _EsIndexPC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 10, 1, 1, 2),
    _EsIndexPC_Type()
)
esIndexPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPC.setStatus("mandatory")
if mibBuilder.loadTexts:
    esIndexPC.setDescription("""\
The part of the point index that refers to point class. The point index is a
string of 3 numbers separated by periods. It contains all the information
necessary for getting a piece of data off an event sensor; namely, which
EventSensor, point class, and which-sensor-of-that-class (a.k.a. point). The
values for this object are: 1=temperature sensor 2=contact closure 3=humidity
sensor 4=noise sensor 5=analog input 6=relay
""")
_EsIndexPoint_Type = Integer32
_EsIndexPoint_Object = MibTableColumn
esIndexPoint = _EsIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 10, 1, 1, 3),
    _EsIndexPoint_Type()
)
esIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPoint.setStatus("mandatory")
if mibBuilder.loadTexts:
    esIndexPoint.setDescription("""\
The part of the point index that delineates which sensor on the EventSensor. So
this combined with esIndexPC (Point Class or type) and esIndexES (which
EventSensor) uniquely defines each point (sensor or relay) attached to a unit.
For example, if esIndexES is 3, esIndexPC is 1 and esIndexPoint is 4 then this
is the Fourth Temperature Sensor on EventSensor number 3.
""")
_EsPointName_Type = DisplayString
_EsPointName_Object = MibTableColumn
esPointName = _EsPointName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 10, 1, 1, 4),
    _EsPointName_Type()
)
esPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointName.setStatus("mandatory")
if mibBuilder.loadTexts:
    esPointName.setDescription("""\
The name of the point on an EventSensor. For example, 'AC temp' (in the case of
the temperature sensor on an EventSensor). There can be multiple points of the
same point class on an EventSensor (e.g., 8 contact closures) and multiple
sensor classes on an EventSensor (e.g., temperature, contact closure,
humidity). If the point referenced by a given point index is solitary (e.g.,
temperature sensor, because there can be only one on an EventSensor), then this
object reads as '<EventSensor name>'. Setting this object for solitary point
indices sets the EventSensor name only. On the other hand, if a given point is
among other points of the same point class on an EventSensor, then this object
reads as '<Sensor name>'. Setting this object for these NON- solitary point
indices sets the sensor name only - not the EventSensor name.
""")
_EsPointInEventState_Type = Integer32
_EsPointInEventState_Object = MibTableColumn
esPointInEventState = _EsPointInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 10, 1, 1, 5),
    _EsPointInEventState_Type()
)
esPointInEventState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointInEventState.setStatus("mandatory")
if mibBuilder.loadTexts:
    esPointInEventState.setDescription("""\
A number referring to the event state of a point on an EventSensor. This number
can have different meanings depending on the point class. If the point class is
temperature, humidity, or analog input, then the values of this object are:
1=very low 2=low 3=normal 4=high 5=very high For contact closures and relays
the values of this object are: 1=point in event state 2=point in normal state
For any point class and any point, if the event state is undefined, then the
value of this object is 0. For any point class except relay, this object is
read-only. For relays, setting this object to 1 puts the relay into its open
state. Setting it to 2 puts the relay into its closed state.
""")


class _EsPointValueInt_Type(Integer32):
    """Custom type esPointValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_EsPointValueInt_Type.__name__ = "Integer32"
_EsPointValueInt_Object = MibTableColumn
esPointValueInt = _EsPointValueInt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 10, 1, 1, 6),
    _EsPointValueInt_Type()
)
esPointValueInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointValueInt.setStatus("mandatory")
if mibBuilder.loadTexts:
    esPointValueInt.setDescription("""\
A number referring to the value of a point on an EventSensor. If the point
class is temperature, then this object is the temperature in its configured
scale (default is Fahrenheit). If the point class is contact closure or relay,
then this object is either 0 (open) or 1 (closed). If the point class is
humidity, then this object is the percent relative humidity. If the point class
is analog input, then this object is the signed input value in tenths of the
configured units. For any point class except relay, this object is read-only.
For relays, setting this object to 1 closes the relay, while setting it to 0
opens it. This works regardless of the control mode of the relay.
""")
_EsPointValueStr_Type = DisplayString
_EsPointValueStr_Object = MibTableColumn
esPointValueStr = _EsPointValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 10, 1, 1, 7),
    _EsPointValueStr_Type()
)
esPointValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointValueStr.setStatus("mandatory")
if mibBuilder.loadTexts:
    esPointValueStr.setDescription("""\
A string referring to the value of a point on an EventSensor. For contact
closures and relays this object is either 'Open' or 'Closed'. For temperature
and humidity point classes, this object is the string representation of the
esPointValueInt object. For temperature, 'C' or 'F' is including in the string
to indicate scale. For analog inputs, this object is the string representation
of the plus/minus input in volts.
""")
_EventSensorConfig_ObjectIdentity = ObjectIdentity
eventSensorConfig = _EventSensorConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11)
)
_EsNumberEventSensors_Type = Integer32
_EsNumberEventSensors_Object = MibScalar
esNumberEventSensors = _EsNumberEventSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 1),
    _EsNumberEventSensors_Type()
)
esNumberEventSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberEventSensors.setStatus("mandatory")
if mibBuilder.loadTexts:
    esNumberEventSensors.setDescription("""\
The number of EventSensors recognized by the s412 Range: 0-4
""")
_EsTable_Object = MibTable
esTable = _EsTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2)
)
if mibBuilder.loadTexts:
    esTable.setStatus("mandatory")
if mibBuilder.loadTexts:
    esTable.setDescription("""\
The table of what EventSensors are attached to the unit
""")
_EsEntry_Object = MibTableRow
esEntry = _EsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1)
)
esEntry.setIndexNames(
    (0, "S412-MIB", "esIndex"),
)
if mibBuilder.loadTexts:
    esEntry.setStatus("mandatory")
if mibBuilder.loadTexts:
    esEntry.setDescription("""\
Table entry for EventSensor table
""")
_EsIndex_Type = Integer32
_EsIndex_Object = MibTableColumn
esIndex = _EsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 1),
    _EsIndex_Type()
)
esIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndex.setStatus("mandatory")
if mibBuilder.loadTexts:
    esIndex.setDescription("""\
This number refers to an EventSensor; it has the same meaning as the esIndexES
object (see above), except that this object is used only within the esTable
branch. This object's allowable values are 1 through 4, which refer to
additional attached EventSensors. The number corresponding to an EventSensor is
determined by the user at the initial configuration time.
""")
_EsID_Type = DisplayString
_EsID_Object = MibTableColumn
esID = _EsID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 2),
    _EsID_Type()
)
esID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esID.setStatus("mandatory")
if mibBuilder.loadTexts:
    esID.setDescription("""\
The factory-assigned ID of the EventSensor
""")
_EsNumberTempSensors_Type = Integer32
_EsNumberTempSensors_Object = MibTableColumn
esNumberTempSensors = _EsNumberTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 3),
    _EsNumberTempSensors_Type()
)
esNumberTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberTempSensors.setStatus("mandatory")
if mibBuilder.loadTexts:
    esNumberTempSensors.setDescription("""\
The number of temperature sensors on the EventSensor
""")
_EsTempReportingMode_Type = DisplayString
_EsTempReportingMode_Object = MibTableColumn
esTempReportingMode = _EsTempReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 4),
    _EsTempReportingMode_Type()
)
esTempReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTempReportingMode.setStatus("mandatory")
if mibBuilder.loadTexts:
    esTempReportingMode.setDescription("""\
Description of how temperature values should be interpreted.
""")
_EsNumberCCs_Type = Integer32
_EsNumberCCs_Object = MibTableColumn
esNumberCCs = _EsNumberCCs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 5),
    _EsNumberCCs_Type()
)
esNumberCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberCCs.setStatus("mandatory")
if mibBuilder.loadTexts:
    esNumberCCs.setDescription("""\
The number of contact closures on the EventSensor.
""")
_EsCCReportingMode_Type = DisplayString
_EsCCReportingMode_Object = MibTableColumn
esCCReportingMode = _EsCCReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 6),
    _EsCCReportingMode_Type()
)
esCCReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCReportingMode.setStatus("mandatory")
if mibBuilder.loadTexts:
    esCCReportingMode.setDescription("""\
Description of how CC values should be interpreted.
""")
_EsNumberHumidSensors_Type = Integer32
_EsNumberHumidSensors_Object = MibTableColumn
esNumberHumidSensors = _EsNumberHumidSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 7),
    _EsNumberHumidSensors_Type()
)
esNumberHumidSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberHumidSensors.setStatus("mandatory")
if mibBuilder.loadTexts:
    esNumberHumidSensors.setDescription("""\
The number of humidity sensors on the EventSensor.
""")
_EsHumidReportingMode_Type = DisplayString
_EsHumidReportingMode_Object = MibTableColumn
esHumidReportingMode = _EsHumidReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 8),
    _EsHumidReportingMode_Type()
)
esHumidReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esHumidReportingMode.setStatus("mandatory")
if mibBuilder.loadTexts:
    esHumidReportingMode.setDescription("""\
Description of how humidity sensor values should be interpreted.
""")
_EsNumberAnalog_Type = Integer32
_EsNumberAnalog_Object = MibTableColumn
esNumberAnalog = _EsNumberAnalog_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 13),
    _EsNumberAnalog_Type()
)
esNumberAnalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberAnalog.setStatus("mandatory")
if mibBuilder.loadTexts:
    esNumberAnalog.setDescription("""\
The number of analog inputs on the EventSensor.
""")
_EsAnalogReportingMode_Type = DisplayString
_EsAnalogReportingMode_Object = MibTableColumn
esAnalogReportingMode = _EsAnalogReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 14),
    _EsAnalogReportingMode_Type()
)
esAnalogReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogReportingMode.setStatus("mandatory")
if mibBuilder.loadTexts:
    esAnalogReportingMode.setDescription("""\
Description of how analog input values should be interpreted.
""")
_EsNumberRelayOutputs_Type = Integer32
_EsNumberRelayOutputs_Object = MibTableColumn
esNumberRelayOutputs = _EsNumberRelayOutputs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 15),
    _EsNumberRelayOutputs_Type()
)
esNumberRelayOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberRelayOutputs.setStatus("mandatory")
if mibBuilder.loadTexts:
    esNumberRelayOutputs.setDescription("""\
The number of relay outputs on the EventSensor
""")
_EsRelayReportingMode_Type = DisplayString
_EsRelayReportingMode_Object = MibTableColumn
esRelayReportingMode = _EsRelayReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 11, 2, 1, 16),
    _EsRelayReportingMode_Type()
)
esRelayReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esRelayReportingMode.setStatus("mandatory")
if mibBuilder.loadTexts:
    esRelayReportingMode.setDescription("""\
Description of how relay output values should be interpreted.
""")
_Techsupport_ObjectIdentity = ObjectIdentity
techsupport = _Techsupport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 99)
)
_TechsupportIPAddress_Type = IpAddress
_TechsupportIPAddress_Object = MibScalar
techsupportIPAddress = _TechsupportIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 99, 1),
    _TechsupportIPAddress_Type()
)
techsupportIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techsupportIPAddress.setStatus("mandatory")
if mibBuilder.loadTexts:
    techsupportIPAddress.setDescription("""\
May read or Set IP Address, takes effect on restart
""")
_TechsupportNetMask_Type = IpAddress
_TechsupportNetMask_Object = MibScalar
techsupportNetMask = _TechsupportNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 99, 2),
    _TechsupportNetMask_Type()
)
techsupportNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techsupportNetMask.setStatus("mandatory")
if mibBuilder.loadTexts:
    techsupportNetMask.setDescription("""\
May read or Set NetMask, takes effect on restart
""")
_TechsupportRouter_Type = IpAddress
_TechsupportRouter_Object = MibScalar
techsupportRouter = _TechsupportRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 99, 3),
    _TechsupportRouter_Type()
)
techsupportRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techsupportRouter.setStatus("mandatory")
if mibBuilder.loadTexts:
    techsupportRouter.setDescription("""\
May read or Set Router IP Address, takes effect on restart
""")
_TechsupportRestart_Type = Integer32
_TechsupportRestart_Object = MibScalar
techsupportRestart = _TechsupportRestart_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 99, 4),
    _TechsupportRestart_Type()
)
techsupportRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techsupportRestart.setStatus("mandatory")
if mibBuilder.loadTexts:
    techsupportRestart.setDescription("""\
Reads as 0, any Write resets unit so new IP, Netmask, Router may be used
""")
_TechsupportVersionNumber_Type = DisplayString
_TechsupportVersionNumber_Object = MibScalar
techsupportVersionNumber = _TechsupportVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 99, 5),
    _TechsupportVersionNumber_Type()
)
techsupportVersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    techsupportVersionNumber.setStatus("mandatory")
if mibBuilder.loadTexts:
    techsupportVersionNumber.setDescription("""\
Version Number of Firmware
""")
_Mibend_ObjectIdentity = ObjectIdentity
mibend = _Mibend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 41, 100)
)
_MibendObject_Type = Integer32
_MibendObject_Object = MibScalar
mibendObject = _MibendObject_Object(
    (1, 3, 6, 1, 4, 1, 3052, 41, 100, 1),
    _MibendObject_Type()
)
mibendObject.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mibendObject.setStatus("mandatory")
if mibBuilder.loadTexts:
    mibendObject.setDescription("""\
An object after all active mib items, to help some managers compile
""")

# Managed Objects groups


# Notification objects

contact1ActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20001)
)
contact1ActiveTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact1Name"),
        ("S412-MIB", "contact1State"))
)
if mibBuilder.loadTexts:
    contact1ActiveTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact1ActiveTrap.setDescription("""\
Sent to show Contact 1 is in the alarm state
""")

contact2ActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20002)
)
contact2ActiveTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact2Name"),
        ("S412-MIB", "contact2State"))
)
if mibBuilder.loadTexts:
    contact2ActiveTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact2ActiveTrap.setDescription("""\
Sent to show Contact 2 is in the alarm state
""")

contact3ActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20003)
)
contact3ActiveTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact3Name"),
        ("S412-MIB", "contact3State"))
)
if mibBuilder.loadTexts:
    contact3ActiveTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact3ActiveTrap.setDescription("""\
Sent to show Contact 3 is in the alarm state
""")

contact4ActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20004)
)
contact4ActiveTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact4Name"),
        ("S412-MIB", "contact4State"))
)
if mibBuilder.loadTexts:
    contact4ActiveTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact4ActiveTrap.setDescription("""\
Sent to show Contact 4 is in the alarm state
""")

contact5ActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20005)
)
contact5ActiveTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact5Name"),
        ("S412-MIB", "contact5State"))
)
if mibBuilder.loadTexts:
    contact5ActiveTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact5ActiveTrap.setDescription("""\
Sent to show Contact 5 is in the alarm state
""")

contact6ActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20006)
)
contact6ActiveTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact6Name"),
        ("S412-MIB", "contact6State"))
)
if mibBuilder.loadTexts:
    contact6ActiveTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact6ActiveTrap.setDescription("""\
Sent to show Contact 6 is in the alarm state
""")

tempHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20010)
)
tempHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "tempValue"))
)
if mibBuilder.loadTexts:
    tempHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    tempHighTrap.setDescription("""\
Sent to show Temp exceeded High Temp Threshold
""")

tempVeryHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20011)
)
tempVeryHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "tempValue"))
)
if mibBuilder.loadTexts:
    tempVeryHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    tempVeryHighTrap.setDescription("""\
Sent to show Temp exceeded Very High Temp Threshold
""")

tempLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20012)
)
tempLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "tempValue"))
)
if mibBuilder.loadTexts:
    tempLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    tempLowTrap.setDescription("""\
Sent to show Temp went below Low Temp Threshold
""")

tempVeryLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20013)
)
tempVeryLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "tempValue"))
)
if mibBuilder.loadTexts:
    tempVeryLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    tempVeryLowTrap.setDescription("""\
Sent to show Temp went below Very Low Temp Threshold
""")

humidityHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20020)
)
humidityHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "humidityValue"))
)
if mibBuilder.loadTexts:
    humidityHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    humidityHighTrap.setDescription("""\
Sent to show humidity exceeded High humidity Threshold
""")

humidityVeryHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20021)
)
humidityVeryHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "humidityValue"))
)
if mibBuilder.loadTexts:
    humidityVeryHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    humidityVeryHighTrap.setDescription("""\
Sent to show humidity exceeded Very High humidity Threshold
""")

humidityLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20022)
)
humidityLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "humidityValue"))
)
if mibBuilder.loadTexts:
    humidityLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    humidityLowTrap.setDescription("""\
Sent to show humidity went below Low humidity Threshold
""")

humidityVeryLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20023)
)
humidityVeryLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "humidityValue"))
)
if mibBuilder.loadTexts:
    humidityVeryLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    humidityVeryLowTrap.setDescription("""\
Sent to show humidity went below Very Low humidity Threshold
""")

analog1HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20030)
)
analog1HighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "analog1Name"),
        ("S412-MIB", "analog1Value"))
)
if mibBuilder.loadTexts:
    analog1HighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    analog1HighTrap.setDescription("""\
Sent to show analog1 exceeded High analog1 Threshold
""")

analog1VeryHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20031)
)
analog1VeryHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "analog1Name"),
        ("S412-MIB", "analog1Value"))
)
if mibBuilder.loadTexts:
    analog1VeryHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    analog1VeryHighTrap.setDescription("""\
Sent to show analog1 exceeded Very High analog1 Threshold
""")

analog1LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20032)
)
analog1LowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "analog1Name"),
        ("S412-MIB", "analog1Value"))
)
if mibBuilder.loadTexts:
    analog1LowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    analog1LowTrap.setDescription("""\
Sent to show analog1 went below Low analog1 Threshold
""")

analog1VeryLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20033)
)
analog1VeryLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "analog1Name"),
        ("S412-MIB", "analog1Value"))
)
if mibBuilder.loadTexts:
    analog1VeryLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    analog1VeryLowTrap.setDescription("""\
Sent to show analog1 went below Very Low analog1 Threshold
""")

analog2HighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20040)
)
analog2HighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "analog2Name"),
        ("S412-MIB", "analog2Value"))
)
if mibBuilder.loadTexts:
    analog2HighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    analog2HighTrap.setDescription("""\
Sent to show analog2 exceeded High analog2 Threshold
""")

analog2VeryHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20041)
)
analog2VeryHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "analog2Name"),
        ("S412-MIB", "analog2Value"))
)
if mibBuilder.loadTexts:
    analog2VeryHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    analog2VeryHighTrap.setDescription("""\
Sent to show analog2 exceeded Very High analog2 Threshold
""")

analog2LowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20042)
)
analog2LowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "analog2Name"),
        ("S412-MIB", "analog2Value"))
)
if mibBuilder.loadTexts:
    analog2LowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    analog2LowTrap.setDescription("""\
Sent to show analog2 went below Low analog2 Threshold
""")

analog2VeryLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20043)
)
analog2VeryLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "analog2Name"),
        ("S412-MIB", "analog2Value"))
)
if mibBuilder.loadTexts:
    analog2VeryLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    analog2VeryLowTrap.setDescription("""\
Sent to show analog2 went below Very Low analog2 Threshold
""")

contactESActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20101)
)
contactESActiveTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    contactESActiveTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contactESActiveTrap.setDescription("""\
Sent to show EventSensor contact is in the alarm state
""")

tempESHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20110)
)
tempESHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    tempESHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    tempESHighTrap.setDescription("""\
Sent to show Temp exceeded High Threshold on an EventSensor
""")

tempESVeryHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20111)
)
tempESVeryHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    tempESVeryHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    tempESVeryHighTrap.setDescription("""\
Sent to show Temp exceeded Very High Threshold on an EventSensor
""")

tempESLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20112)
)
tempESLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    tempESLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    tempESLowTrap.setDescription("""\
Sent to show Temp went below Low Threshold on an EventSensor
""")

tempESVeryLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20113)
)
tempESVeryLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    tempESVeryLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    tempESVeryLowTrap.setDescription("""\
Sent to show Temp went below Very Low Threshold on an EventSensor
""")

humidityESHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20120)
)
humidityESHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    humidityESHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    humidityESHighTrap.setDescription("""\
Sent to show humidity exceeded High Threshold on an EventSensor
""")

humidityESVeryHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20121)
)
humidityESVeryHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    humidityESVeryHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    humidityESVeryHighTrap.setDescription("""\
Sent to show humidity exceeded Very High Threshold on an EventSensor
""")

humidityESLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20122)
)
humidityESLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    humidityESLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    humidityESLowTrap.setDescription("""\
Sent to show humidity went below Low Threshold on an EventSensor
""")

humidityESVeryLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20123)
)
humidityESVeryLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    humidityESVeryLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    humidityESVeryLowTrap.setDescription("""\
Sent to show humidity went below Very Low Threshold on an EventSensor
""")

voltageESHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20130)
)
voltageESHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    voltageESHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    voltageESHighTrap.setDescription("""\
Sent to show voltage exceeded High Threshold on an EventSensor
""")

voltageESVeryHighTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20131)
)
voltageESVeryHighTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    voltageESVeryHighTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    voltageESVeryHighTrap.setDescription("""\
Sent to show voltage exceeded Very High Threshold on an EventSensor
""")

voltageESLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20132)
)
voltageESLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    voltageESLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    voltageESLowTrap.setDescription("""\
Sent to show voltage went below Low Threshold on an EventSensor
""")

voltageESVeryLowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 20133)
)
voltageESVeryLowTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    voltageESVeryLowTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    voltageESVeryLowTrap.setDescription("""\
Sent to show voltage went below Very Low Threshold on an EventSensor
""")

contact1NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21001)
)
contact1NormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact1Name"),
        ("S412-MIB", "contact1State"))
)
if mibBuilder.loadTexts:
    contact1NormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact1NormalTrap.setDescription("""\
Sent to show Contact 1 is in the normal state
""")

contact2NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21002)
)
contact2NormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact2Name"),
        ("S412-MIB", "contact2State"))
)
if mibBuilder.loadTexts:
    contact2NormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact2NormalTrap.setDescription("""\
Sent to show Contact 2 is in the normal state
""")

contact3NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21003)
)
contact3NormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact3Name"),
        ("S412-MIB", "contact3State"))
)
if mibBuilder.loadTexts:
    contact3NormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact3NormalTrap.setDescription("""\
Sent to show Contact 3 is in the normal state
""")

contact4NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21004)
)
contact4NormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact4Name"),
        ("S412-MIB", "contact4State"))
)
if mibBuilder.loadTexts:
    contact4NormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact4NormalTrap.setDescription("""\
Sent to show Contact 4 is in the normal state
""")

contact5NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21005)
)
contact5NormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact5Name"),
        ("S412-MIB", "contact5State"))
)
if mibBuilder.loadTexts:
    contact5NormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact5NormalTrap.setDescription("""\
Sent to show Contact 5 is in the normal state
""")

contact6NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21006)
)
contact6NormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "contact6Name"),
        ("S412-MIB", "contact6State"))
)
if mibBuilder.loadTexts:
    contact6NormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contact6NormalTrap.setDescription("""\
Sent to show Contact 6 is in the normal state
""")

tempNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21010)
)
tempNormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "tempValue"))
)
if mibBuilder.loadTexts:
    tempNormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    tempNormalTrap.setDescription("""\
Sent to show Temp went back to Normal range
""")

humidityNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21020)
)
humidityNormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "humidityValue"))
)
if mibBuilder.loadTexts:
    humidityNormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    humidityNormalTrap.setDescription("""\
Sent to show Humidity went back to Normal range
""")

analog1NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21030)
)
analog1NormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "analog1Name"),
        ("S412-MIB", "analog1Value"))
)
if mibBuilder.loadTexts:
    analog1NormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    analog1NormalTrap.setDescription("""\
Sent to show analog1 went back to Normal range
""")

analog2NormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21040)
)
analog2NormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "analog2Name"),
        ("S412-MIB", "analog2Value"))
)
if mibBuilder.loadTexts:
    analog2NormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    analog2NormalTrap.setDescription("""\
Sent to show analog2 went back to Normal range
""")

contactESNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21101)
)
contactESNormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    contactESNormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    contactESNormalTrap.setDescription("""\
Send to show EventSensor contact has returned to normal state
""")

tempESNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21110)
)
tempESNormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    tempESNormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    tempESNormalTrap.setDescription("""\
Sent to show EventSensor Temp went back to Normal range
""")

humidityESNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21120)
)
humidityESNormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    humidityESNormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    humidityESNormalTrap.setDescription("""\
Sent to show EventSensor Humidity went back to Normal range
""")

voltageESNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 21130)
)
voltageESNormalTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"),
        ("S412-MIB", "esPointName"),
        ("S412-MIB", "esPointValueInt"),
        ("S412-MIB", "esIndexES"),
        ("S412-MIB", "esIndexPoint"))
)
if mibBuilder.loadTexts:
    voltageESNormalTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    voltageESNormalTrap.setDescription("""\
Sent to show EventSensor voltage went back to Normal range
""")

testTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 41, 0, 22000)
)
testTrap.setObjects(
      *(("S412-MIB", "thisTrapText"),
        ("S412-MIB", "siteID"))
)
if mibBuilder.loadTexts:
    testTrap.setStatus(
        ""
    )
if mibBuilder.loadTexts:
    testTrap.setDescription("""\
Sent for testing the SNMP interface
""")


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S412-MIB",
    **{"asentria": asentria,
       "s412": s412,
       "contact1ActiveTrap": contact1ActiveTrap,
       "contact2ActiveTrap": contact2ActiveTrap,
       "contact3ActiveTrap": contact3ActiveTrap,
       "contact4ActiveTrap": contact4ActiveTrap,
       "contact5ActiveTrap": contact5ActiveTrap,
       "contact6ActiveTrap": contact6ActiveTrap,
       "tempHighTrap": tempHighTrap,
       "tempVeryHighTrap": tempVeryHighTrap,
       "tempLowTrap": tempLowTrap,
       "tempVeryLowTrap": tempVeryLowTrap,
       "humidityHighTrap": humidityHighTrap,
       "humidityVeryHighTrap": humidityVeryHighTrap,
       "humidityLowTrap": humidityLowTrap,
       "humidityVeryLowTrap": humidityVeryLowTrap,
       "analog1HighTrap": analog1HighTrap,
       "analog1VeryHighTrap": analog1VeryHighTrap,
       "analog1LowTrap": analog1LowTrap,
       "analog1VeryLowTrap": analog1VeryLowTrap,
       "analog2HighTrap": analog2HighTrap,
       "analog2VeryHighTrap": analog2VeryHighTrap,
       "analog2LowTrap": analog2LowTrap,
       "analog2VeryLowTrap": analog2VeryLowTrap,
       "contactESActiveTrap": contactESActiveTrap,
       "tempESHighTrap": tempESHighTrap,
       "tempESVeryHighTrap": tempESVeryHighTrap,
       "tempESLowTrap": tempESLowTrap,
       "tempESVeryLowTrap": tempESVeryLowTrap,
       "humidityESHighTrap": humidityESHighTrap,
       "humidityESVeryHighTrap": humidityESVeryHighTrap,
       "humidityESLowTrap": humidityESLowTrap,
       "humidityESVeryLowTrap": humidityESVeryLowTrap,
       "voltageESHighTrap": voltageESHighTrap,
       "voltageESVeryHighTrap": voltageESVeryHighTrap,
       "voltageESLowTrap": voltageESLowTrap,
       "voltageESVeryLowTrap": voltageESVeryLowTrap,
       "contact1NormalTrap": contact1NormalTrap,
       "contact2NormalTrap": contact2NormalTrap,
       "contact3NormalTrap": contact3NormalTrap,
       "contact4NormalTrap": contact4NormalTrap,
       "contact5NormalTrap": contact5NormalTrap,
       "contact6NormalTrap": contact6NormalTrap,
       "tempNormalTrap": tempNormalTrap,
       "humidityNormalTrap": humidityNormalTrap,
       "analog1NormalTrap": analog1NormalTrap,
       "analog2NormalTrap": analog2NormalTrap,
       "contactESNormalTrap": contactESNormalTrap,
       "tempESNormalTrap": tempESNormalTrap,
       "humidityESNormalTrap": humidityESNormalTrap,
       "voltageESNormalTrap": voltageESNormalTrap,
       "testTrap": testTrap,
       "device": device,
       "serialNumber": serialNumber,
       "firmwareVersion": firmwareVersion,
       "siteID": siteID,
       "snmpManager": snmpManager,
       "forceTraps": forceTraps,
       "thisTrapText": thisTrapText,
       "alarmStatus": alarmStatus,
       "snmpManager1": snmpManager1,
       "snmpManager2": snmpManager2,
       "snmpManager3": snmpManager3,
       "snmpManager4": snmpManager4,
       "statusRepeatHours": statusRepeatHours,
       "serialTimeout": serialTimeout,
       "powerupTrapsend": powerupTrapsend,
       "netlossTrapsend": netlossTrapsend,
       "buildID": buildID,
       "contacts": contacts,
       "contact1": contact1,
       "contact1Name": contact1Name,
       "contact1State": contact1State,
       "contact1AlarmEnable": contact1AlarmEnable,
       "contact1ActiveDirection": contact1ActiveDirection,
       "contact1Threshold": contact1Threshold,
       "contact1ReturnNormalTrap": contact1ReturnNormalTrap,
       "contact1TrapRepeat": contact1TrapRepeat,
       "contact1Severity": contact1Severity,
       "contact2": contact2,
       "contact2Name": contact2Name,
       "contact2State": contact2State,
       "contact2AlarmEnable": contact2AlarmEnable,
       "contact2ActiveDirection": contact2ActiveDirection,
       "contact2Threshold": contact2Threshold,
       "contact2ReturnNormalTrap": contact2ReturnNormalTrap,
       "contact2TrapRepeat": contact2TrapRepeat,
       "contact2Severity": contact2Severity,
       "contact3": contact3,
       "contact3Name": contact3Name,
       "contact3State": contact3State,
       "contact3AlarmEnable": contact3AlarmEnable,
       "contact3ActiveDirection": contact3ActiveDirection,
       "contact3Threshold": contact3Threshold,
       "contact3ReturnNormalTrap": contact3ReturnNormalTrap,
       "contact3TrapRepeat": contact3TrapRepeat,
       "contact3Severity": contact3Severity,
       "contact4": contact4,
       "contact4Name": contact4Name,
       "contact4State": contact4State,
       "contact4AlarmEnable": contact4AlarmEnable,
       "contact4ActiveDirection": contact4ActiveDirection,
       "contact4Threshold": contact4Threshold,
       "contact4ReturnNormalTrap": contact4ReturnNormalTrap,
       "contact4TrapRepeat": contact4TrapRepeat,
       "contact4Severity": contact4Severity,
       "contact5": contact5,
       "contact5Name": contact5Name,
       "contact5State": contact5State,
       "contact5AlarmEnable": contact5AlarmEnable,
       "contact5ActiveDirection": contact5ActiveDirection,
       "contact5Threshold": contact5Threshold,
       "contact5ReturnNormalTrap": contact5ReturnNormalTrap,
       "contact5TrapRepeat": contact5TrapRepeat,
       "contact5Severity": contact5Severity,
       "contact6": contact6,
       "contact6Name": contact6Name,
       "contact6State": contact6State,
       "contact6AlarmEnable": contact6AlarmEnable,
       "contact6ActiveDirection": contact6ActiveDirection,
       "contact6Threshold": contact6Threshold,
       "contact6ReturnNormalTrap": contact6ReturnNormalTrap,
       "contact6TrapRepeat": contact6TrapRepeat,
       "contact6Severity": contact6Severity,
       "relays": relays,
       "relay1": relay1,
       "relay1Name": relay1Name,
       "relay1CurrentState": relay1CurrentState,
       "relay1PowerupState": relay1PowerupState,
       "relay2": relay2,
       "relay2Name": relay2Name,
       "relay2CurrentState": relay2CurrentState,
       "relay2PowerupState": relay2PowerupState,
       "tempsensor": tempsensor,
       "tempValue": tempValue,
       "tempAlarmEnable": tempAlarmEnable,
       "tempHighLevel": tempHighLevel,
       "tempVeryHighLevel": tempVeryHighLevel,
       "tempLowLevel": tempLowLevel,
       "tempVeryLowLevel": tempVeryLowLevel,
       "tempAlarmThreshold": tempAlarmThreshold,
       "tempReturnNormalTrap": tempReturnNormalTrap,
       "tempTrapRepeat": tempTrapRepeat,
       "tempMode": tempMode,
       "tempHighSeverity": tempHighSeverity,
       "tempVeryHighSeverity": tempVeryHighSeverity,
       "tempLowSeverity": tempLowSeverity,
       "tempVeryLowSeverity": tempVeryLowSeverity,
       "tempName": tempName,
       "humiditysensor": humiditysensor,
       "humidityValue": humidityValue,
       "humidityAlarmEnable": humidityAlarmEnable,
       "humidityHighLevel": humidityHighLevel,
       "humidityVeryHighLevel": humidityVeryHighLevel,
       "humidityLowLevel": humidityLowLevel,
       "humidityVeryLowLevel": humidityVeryLowLevel,
       "humidityAlarmThreshold": humidityAlarmThreshold,
       "humidityReturnNormalTrap": humidityReturnNormalTrap,
       "humidityTrapRepeat": humidityTrapRepeat,
       "humidityHighSeverity": humidityHighSeverity,
       "humidityVeryHighSeverity": humidityVeryHighSeverity,
       "humidityLowSeverity": humidityLowSeverity,
       "humidityVeryLowSeverity": humidityVeryLowSeverity,
       "humidityName": humidityName,
       "passthrough": passthrough,
       "ptNeedPassword": ptNeedPassword,
       "ptSayLoginText": ptSayLoginText,
       "ptLoginText": ptLoginText,
       "ptSaySiteID": ptSaySiteID,
       "ptUsername": ptUsername,
       "ptPassword": ptPassword,
       "ptTimeout": ptTimeout,
       "ptEscChar": ptEscChar,
       "ptLfstripToPort": ptLfstripToPort,
       "ptLfstripFromPort": ptLfstripFromPort,
       "ptSerialBaudrate": ptSerialBaudrate,
       "ptSerialWordlength": ptSerialWordlength,
       "ptSerialParity": ptSerialParity,
       "ptTCPPortnumber": ptTCPPortnumber,
       "ftp": ftp,
       "ftpUsername": ftpUsername,
       "ftpPassword": ftpPassword,
       "analog": analog,
       "analog1": analog1,
       "analog1Value": analog1Value,
       "analog1AlarmEnable": analog1AlarmEnable,
       "analog1HighLevel": analog1HighLevel,
       "analog1VeryHighLevel": analog1VeryHighLevel,
       "analog1LowLevel": analog1LowLevel,
       "analog1VeryLowLevel": analog1VeryLowLevel,
       "analog1AlarmThreshold": analog1AlarmThreshold,
       "analog1ReturnNormalTrap": analog1ReturnNormalTrap,
       "analog1TrapRepeat": analog1TrapRepeat,
       "analog1HighSeverity": analog1HighSeverity,
       "analog1VeryHighSeverity": analog1VeryHighSeverity,
       "analog1LowSeverity": analog1LowSeverity,
       "analog1VeryLowSeverity": analog1VeryLowSeverity,
       "analog1Name": analog1Name,
       "analog2": analog2,
       "analog2Value": analog2Value,
       "analog2AlarmEnable": analog2AlarmEnable,
       "analog2HighLevel": analog2HighLevel,
       "analog2VeryHighLevel": analog2VeryHighLevel,
       "analog2LowLevel": analog2LowLevel,
       "analog2VeryLowLevel": analog2VeryLowLevel,
       "analog2AlarmThreshold": analog2AlarmThreshold,
       "analog2ReturnNormalTrap": analog2ReturnNormalTrap,
       "analog2TrapRepeat": analog2TrapRepeat,
       "analog2HighSeverity": analog2HighSeverity,
       "analog2VeryHighSeverity": analog2VeryHighSeverity,
       "analog2LowSeverity": analog2LowSeverity,
       "analog2VeryLowSeverity": analog2VeryLowSeverity,
       "analog2Name": analog2Name,
       "eventSensorStatus": eventSensorStatus,
       "esPointTable": esPointTable,
       "esPointEntry": esPointEntry,
       "esIndexES": esIndexES,
       "esIndexPC": esIndexPC,
       "esIndexPoint": esIndexPoint,
       "esPointName": esPointName,
       "esPointInEventState": esPointInEventState,
       "esPointValueInt": esPointValueInt,
       "esPointValueStr": esPointValueStr,
       "eventSensorConfig": eventSensorConfig,
       "esNumberEventSensors": esNumberEventSensors,
       "esTable": esTable,
       "esEntry": esEntry,
       "esIndex": esIndex,
       "esID": esID,
       "esNumberTempSensors": esNumberTempSensors,
       "esTempReportingMode": esTempReportingMode,
       "esNumberCCs": esNumberCCs,
       "esCCReportingMode": esCCReportingMode,
       "esNumberHumidSensors": esNumberHumidSensors,
       "esHumidReportingMode": esHumidReportingMode,
       "esNumberAnalog": esNumberAnalog,
       "esAnalogReportingMode": esAnalogReportingMode,
       "esNumberRelayOutputs": esNumberRelayOutputs,
       "esRelayReportingMode": esRelayReportingMode,
       "techsupport": techsupport,
       "techsupportIPAddress": techsupportIPAddress,
       "techsupportNetMask": techsupportNetMask,
       "techsupportRouter": techsupportRouter,
       "techsupportRestart": techsupportRestart,
       "techsupportVersionNumber": techsupportVersionNumber,
       "mibend": mibend,
       "mibendObject": mibendObject}
)
