# SNMP MIB module (CISCO-TELNET-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TELNET-SERVER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:41 2024
# On host MacBook-Pro.local platform Darwin version 24.0.0 by user lextm
# Using Python version 3.12.0 (main, Nov 14 2023, 23:52:11) [Clang 15.0.0 (clang-1500.0.40.1)]

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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoTelnetServerMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 630)
)
ciscoTelnetServerMIB.setRevisions(
        ("2007-05-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoTelnetServerMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoTelnetServerMIBNotifs = _CiscoTelnetServerMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 0)
)
_CiscoTelnetServerMIBObjects_ObjectIdentity = ObjectIdentity
ciscoTelnetServerMIBObjects = _CiscoTelnetServerMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1)
)
_CiscoTelnetServerConfigObjects_ObjectIdentity = ObjectIdentity
ciscoTelnetServerConfigObjects = _CiscoTelnetServerConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1)
)
_CtsTelnetActivation_Type = TruthValue
_CtsTelnetActivation_Object = MibScalar
ctsTelnetActivation = _CtsTelnetActivation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1, 1),
    _CtsTelnetActivation_Type()
)
ctsTelnetActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsTelnetActivation.setStatus("current")
_CtsSessionEndedNotifEnable_Type = TruthValue
_CtsSessionEndedNotifEnable_Object = MibScalar
ctsSessionEndedNotifEnable = _CtsSessionEndedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1, 2),
    _CtsSessionEndedNotifEnable_Type()
)
ctsSessionEndedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsSessionEndedNotifEnable.setStatus("current")
_CtsSessionStartedNotifEnable_Type = TruthValue
_CtsSessionStartedNotifEnable_Object = MibScalar
ctsSessionStartedNotifEnable = _CtsSessionStartedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1, 3),
    _CtsSessionStartedNotifEnable_Type()
)
ctsSessionStartedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsSessionStartedNotifEnable.setStatus("current")
_CtsSessionDeniedNotifEnable_Type = TruthValue
_CtsSessionDeniedNotifEnable_Object = MibScalar
ctsSessionDeniedNotifEnable = _CtsSessionDeniedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1, 4),
    _CtsSessionDeniedNotifEnable_Type()
)
ctsSessionDeniedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctsSessionDeniedNotifEnable.setStatus("current")
_CtsSessionFailureNotifEnable_Type = TruthValue
_CtsSessionFailureNotifEnable_Object = MibScalar
ctsSessionFailureNotifEnable = _CtsSessionFailureNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 1, 5),
    _CtsSessionFailureNotifEnable_Type()
)
ctsSessionFailureNotifEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsSessionFailureNotifEnable.setStatus("current")
_CiscoTelnetServerStatusObjects_ObjectIdentity = ObjectIdentity
ciscoTelnetServerStatusObjects = _CiscoTelnetServerStatusObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2)
)
_CtsSessionsTable_Object = MibTable
ctsSessionsTable = _CtsSessionsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ctsSessionsTable.setStatus("current")
_CtsSessionsEntry_Object = MibTableRow
ctsSessionsEntry = _CtsSessionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1)
)
ctsSessionsEntry.setIndexNames(
    (0, "CISCO-TELNET-SERVER-MIB", "ctsSessionID"),
)
if mibBuilder.loadTexts:
    ctsSessionsEntry.setStatus("current")
_CtsSessionID_Type = Unsigned32
_CtsSessionID_Object = MibTableColumn
ctsSessionID = _CtsSessionID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 1),
    _CtsSessionID_Type()
)
ctsSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctsSessionID.setStatus("current")
_CtsSessionDescription_Type = SnmpAdminString
_CtsSessionDescription_Object = MibTableColumn
ctsSessionDescription = _CtsSessionDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 2),
    _CtsSessionDescription_Type()
)
ctsSessionDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsSessionDescription.setStatus("current")
_CtsSessionClientAddressType_Type = InetAddressType
_CtsSessionClientAddressType_Object = MibTableColumn
ctsSessionClientAddressType = _CtsSessionClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 3),
    _CtsSessionClientAddressType_Type()
)
ctsSessionClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsSessionClientAddressType.setStatus("current")
_CtsSessionsClientAddress_Type = InetAddress
_CtsSessionsClientAddress_Object = MibTableColumn
ctsSessionsClientAddress = _CtsSessionsClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 4),
    _CtsSessionsClientAddress_Type()
)
ctsSessionsClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsSessionsClientAddress.setStatus("current")
_CtsSessionPID_Type = Unsigned32
_CtsSessionPID_Object = MibTableColumn
ctsSessionPID = _CtsSessionPID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 5),
    _CtsSessionPID_Type()
)
ctsSessionPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsSessionPID.setStatus("current")
_CtsSessionUserID_Type = SnmpAdminString
_CtsSessionUserID_Object = MibTableColumn
ctsSessionUserID = _CtsSessionUserID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 6),
    _CtsSessionUserID_Type()
)
ctsSessionUserID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsSessionUserID.setStatus("current")
_CtsSessionTcpPort_Type = InetPortNumber
_CtsSessionTcpPort_Object = MibTableColumn
ctsSessionTcpPort = _CtsSessionTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 1, 2, 1, 1, 7),
    _CtsSessionTcpPort_Type()
)
ctsSessionTcpPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctsSessionTcpPort.setStatus("current")
_CiscoTelnetServerMIBConform_ObjectIdentity = ObjectIdentity
ciscoTelnetServerMIBConform = _CiscoTelnetServerMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 2)
)
_CiscoTelnetServerMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoTelnetServerMIBCompliances = _CiscoTelnetServerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 1)
)
_CiscoTelnetServerMIBGroups_ObjectIdentity = ObjectIdentity
ciscoTelnetServerMIBGroups = _CiscoTelnetServerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 2)
)

# Managed Objects groups

ctsMIBSessionsObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 2, 1)
)
ctsMIBSessionsObjectGroup.setObjects(
      *(("CISCO-TELNET-SERVER-MIB", "ctsSessionDescription"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionClientAddressType"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionsClientAddress"),
        ("CISCO-TELNET-SERVER-MIB", "ctsTelnetActivation"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionPID"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionUserID"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionTcpPort"))
)
if mibBuilder.loadTexts:
    ctsMIBSessionsObjectGroup.setStatus("current")

ctsSessionNotifsControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 2, 3)
)
ctsSessionNotifsControlGroup.setObjects(
      *(("CISCO-TELNET-SERVER-MIB", "ctsSessionEndedNotifEnable"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionStartedNotifEnable"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionDeniedNotifEnable"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionFailureNotifEnable"))
)
if mibBuilder.loadTexts:
    ctsSessionNotifsControlGroup.setStatus("current")


# Notification objects

ctsSessionEnded = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 0, 1)
)
ctsSessionEnded.setObjects(
      *(("CISCO-TELNET-SERVER-MIB", "ctsSessionClientAddressType"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionsClientAddress"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionUserID"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionTcpPort"))
)
if mibBuilder.loadTexts:
    ctsSessionEnded.setStatus(
        "current"
    )

ctsSessionStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 0, 2)
)
ctsSessionStarted.setObjects(
      *(("CISCO-TELNET-SERVER-MIB", "ctsSessionClientAddressType"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionsClientAddress"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionUserID"))
)
if mibBuilder.loadTexts:
    ctsSessionStarted.setStatus(
        "current"
    )

ctsSessionDenied = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 0, 3)
)
ctsSessionDenied.setObjects(
      *(("CISCO-TELNET-SERVER-MIB", "ctsSessionClientAddressType"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionsClientAddress"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionTcpPort"))
)
if mibBuilder.loadTexts:
    ctsSessionDenied.setStatus(
        "current"
    )

ctsSessionLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 0, 4)
)
ctsSessionLoginFailure.setObjects(
      *(("CISCO-TELNET-SERVER-MIB", "ctsSessionClientAddressType"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionsClientAddress"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionUserID"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionTcpPort"))
)
if mibBuilder.loadTexts:
    ctsSessionLoginFailure.setStatus(
        "current"
    )


# Notifications groups

ctsMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 2, 2)
)
ctsMIBNotificationGroup.setObjects(
      *(("CISCO-TELNET-SERVER-MIB", "ctsSessionEnded"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionStarted"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionDenied"),
        ("CISCO-TELNET-SERVER-MIB", "ctsSessionLoginFailure"))
)
if mibBuilder.loadTexts:
    ctsMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoTelnetServerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 630, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoTelnetServerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TELNET-SERVER-MIB",
    **{"ciscoTelnetServerMIB": ciscoTelnetServerMIB,
       "ciscoTelnetServerMIBNotifs": ciscoTelnetServerMIBNotifs,
       "ctsSessionEnded": ctsSessionEnded,
       "ctsSessionStarted": ctsSessionStarted,
       "ctsSessionDenied": ctsSessionDenied,
       "ctsSessionLoginFailure": ctsSessionLoginFailure,
       "ciscoTelnetServerMIBObjects": ciscoTelnetServerMIBObjects,
       "ciscoTelnetServerConfigObjects": ciscoTelnetServerConfigObjects,
       "ctsTelnetActivation": ctsTelnetActivation,
       "ctsSessionEndedNotifEnable": ctsSessionEndedNotifEnable,
       "ctsSessionStartedNotifEnable": ctsSessionStartedNotifEnable,
       "ctsSessionDeniedNotifEnable": ctsSessionDeniedNotifEnable,
       "ctsSessionFailureNotifEnable": ctsSessionFailureNotifEnable,
       "ciscoTelnetServerStatusObjects": ciscoTelnetServerStatusObjects,
       "ctsSessionsTable": ctsSessionsTable,
       "ctsSessionsEntry": ctsSessionsEntry,
       "ctsSessionID": ctsSessionID,
       "ctsSessionDescription": ctsSessionDescription,
       "ctsSessionClientAddressType": ctsSessionClientAddressType,
       "ctsSessionsClientAddress": ctsSessionsClientAddress,
       "ctsSessionPID": ctsSessionPID,
       "ctsSessionUserID": ctsSessionUserID,
       "ctsSessionTcpPort": ctsSessionTcpPort,
       "ciscoTelnetServerMIBConform": ciscoTelnetServerMIBConform,
       "ciscoTelnetServerMIBCompliances": ciscoTelnetServerMIBCompliances,
       "ciscoTelnetServerMIBCompliance": ciscoTelnetServerMIBCompliance,
       "ciscoTelnetServerMIBGroups": ciscoTelnetServerMIBGroups,
       "ctsMIBSessionsObjectGroup": ctsMIBSessionsObjectGroup,
       "ctsMIBNotificationGroup": ctsMIBNotificationGroup,
       "ctsSessionNotifsControlGroup": ctsSessionNotifsControlGroup}
)
