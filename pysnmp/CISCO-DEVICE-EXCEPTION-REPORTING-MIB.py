# SNMP MIB module (CISCO-DEVICE-EXCEPTION-REPORTING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DEVICE-EXCEPTION-REPORTING-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:57:55 2024
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoDevExcepReportMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 224)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDevExcepReportMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDevExcepReportMIBObjects = _CiscoDevExcepReportMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1)
)
_CderExceptionData_ObjectIdentity = ObjectIdentity
cderExceptionData = _CderExceptionData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1)
)


class _CderMaxExceptionRecords_Type(Unsigned32):
    """Custom type cderMaxExceptionRecords based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_CderMaxExceptionRecords_Type.__name__ = "Unsigned32"
_CderMaxExceptionRecords_Object = MibScalar
cderMaxExceptionRecords = _CderMaxExceptionRecords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 1),
    _CderMaxExceptionRecords_Type()
)
cderMaxExceptionRecords.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cderMaxExceptionRecords.setStatus("current")


class _CderNotificationEnabled_Type(TruthValue):
    """Custom type cderNotificationEnabled based on TruthValue"""


_CderNotificationEnabled_Object = MibScalar
cderNotificationEnabled = _CderNotificationEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 2),
    _CderNotificationEnabled_Type()
)
cderNotificationEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cderNotificationEnabled.setStatus("current")
_CderNotificationsSent_Type = Counter32
_CderNotificationsSent_Object = MibScalar
cderNotificationsSent = _CderNotificationsSent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 3),
    _CderNotificationsSent_Type()
)
cderNotificationsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cderNotificationsSent.setStatus("current")
_CderNotificationsDropped_Type = Counter32
_CderNotificationsDropped_Object = MibScalar
cderNotificationsDropped = _CderNotificationsDropped_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 4),
    _CderNotificationsDropped_Type()
)
cderNotificationsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cderNotificationsDropped.setStatus("current")
_CderExceptionTable_Object = MibTable
cderExceptionTable = _CderExceptionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cderExceptionTable.setStatus("current")
_CderExceptionEntry_Object = MibTableRow
cderExceptionEntry = _CderExceptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1)
)
cderExceptionEntry.setIndexNames(
    (0, "CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepTableIndex"),
)
if mibBuilder.loadTexts:
    cderExceptionEntry.setStatus("current")


class _CderExcepTableIndex_Type(Unsigned32):
    """Custom type cderExcepTableIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CderExcepTableIndex_Type.__name__ = "Unsigned32"
_CderExcepTableIndex_Object = MibTableColumn
cderExcepTableIndex = _CderExcepTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 1),
    _CderExcepTableIndex_Type()
)
cderExcepTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cderExcepTableIndex.setStatus("current")


class _CderExcepId_Type(SnmpAdminString):
    """Custom type cderExcepId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CderExcepId_Type.__name__ = "SnmpAdminString"
_CderExcepId_Object = MibTableColumn
cderExcepId = _CderExcepId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 2),
    _CderExcepId_Type()
)
cderExcepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cderExcepId.setStatus("current")
_CderExcepHostAddressType_Type = InetAddressType
_CderExcepHostAddressType_Object = MibTableColumn
cderExcepHostAddressType = _CderExcepHostAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 3),
    _CderExcepHostAddressType_Type()
)
cderExcepHostAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cderExcepHostAddressType.setStatus("current")
_CderExcepHostAddress_Type = InetAddress
_CderExcepHostAddress_Object = MibTableColumn
cderExcepHostAddress = _CderExcepHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 4),
    _CderExcepHostAddress_Type()
)
cderExcepHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cderExcepHostAddress.setStatus("current")


class _CderExcepPriorityDescription_Type(SnmpAdminString):
    """Custom type cderExcepPriorityDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CderExcepPriorityDescription_Type.__name__ = "SnmpAdminString"
_CderExcepPriorityDescription_Object = MibTableColumn
cderExcepPriorityDescription = _CderExcepPriorityDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 5),
    _CderExcepPriorityDescription_Type()
)
cderExcepPriorityDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cderExcepPriorityDescription.setStatus("current")
_CderExcepTime_Type = TimeStamp
_CderExcepTime_Object = MibTableColumn
cderExcepTime = _CderExcepTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 6),
    _CderExcepTime_Type()
)
cderExcepTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cderExcepTime.setStatus("current")


class _CderExcepData_Type(OctetString):
    """Custom type cderExcepData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_CderExcepData_Type.__name__ = "OctetString"
_CderExcepData_Object = MibTableColumn
cderExcepData = _CderExcepData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 7),
    _CderExcepData_Type()
)
cderExcepData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cderExcepData.setStatus("current")
_CderExcepReportedBy_Type = SnmpAdminString
_CderExcepReportedBy_Object = MibTableColumn
cderExcepReportedBy = _CderExcepReportedBy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 1, 1, 5, 1, 8),
    _CderExcepReportedBy_Type()
)
cderExcepReportedBy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cderExcepReportedBy.setStatus("current")
_CderMIBNotifPrefix_ObjectIdentity = ObjectIdentity
cderMIBNotifPrefix = _CderMIBNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 2)
)
_CderMIBNotifications_ObjectIdentity = ObjectIdentity
cderMIBNotifications = _CderMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 2, 0)
)
_CiscoDEReportMIBConformance_ObjectIdentity = ObjectIdentity
ciscoDEReportMIBConformance = _CiscoDEReportMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 3)
)
_CiscoDEReportMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDEReportMIBCompliances = _CiscoDEReportMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 3, 1)
)
_CiscoDEReportMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDEReportMIBGroups = _CiscoDEReportMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 3, 2)
)

# Managed Objects groups

ciscoDERExceptionDataGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 3, 2, 1)
)
ciscoDERExceptionDataGroup.setObjects(
      *(("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderMaxExceptionRecords"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderNotificationEnabled"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderNotificationsSent"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderNotificationsDropped"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepId"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepHostAddressType"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepHostAddress"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepPriorityDescription"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepTime"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepData"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepReportedBy"))
)
if mibBuilder.loadTexts:
    ciscoDERExceptionDataGroup.setStatus("current")


# Notification objects

cderMonitoredExceptionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 2, 0, 1)
)
cderMonitoredExceptionEvent.setObjects(
      *(("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepId"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepHostAddressType"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepHostAddress"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepPriorityDescription"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepTime"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepData"),
        ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderExcepReportedBy"))
)
if mibBuilder.loadTexts:
    cderMonitoredExceptionEvent.setStatus(
        "current"
    )


# Notifications groups

ciscoDERExceptionGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 3, 2, 2)
)
ciscoDERExceptionGroup.setObjects(
    ("CISCO-DEVICE-EXCEPTION-REPORTING-MIB", "cderMonitoredExceptionEvent")
)
if mibBuilder.loadTexts:
    ciscoDERExceptionGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoDEReportMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 224, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDEReportMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DEVICE-EXCEPTION-REPORTING-MIB",
    **{"ciscoDevExcepReportMIB": ciscoDevExcepReportMIB,
       "ciscoDevExcepReportMIBObjects": ciscoDevExcepReportMIBObjects,
       "cderExceptionData": cderExceptionData,
       "cderMaxExceptionRecords": cderMaxExceptionRecords,
       "cderNotificationEnabled": cderNotificationEnabled,
       "cderNotificationsSent": cderNotificationsSent,
       "cderNotificationsDropped": cderNotificationsDropped,
       "cderExceptionTable": cderExceptionTable,
       "cderExceptionEntry": cderExceptionEntry,
       "cderExcepTableIndex": cderExcepTableIndex,
       "cderExcepId": cderExcepId,
       "cderExcepHostAddressType": cderExcepHostAddressType,
       "cderExcepHostAddress": cderExcepHostAddress,
       "cderExcepPriorityDescription": cderExcepPriorityDescription,
       "cderExcepTime": cderExcepTime,
       "cderExcepData": cderExcepData,
       "cderExcepReportedBy": cderExcepReportedBy,
       "cderMIBNotifPrefix": cderMIBNotifPrefix,
       "cderMIBNotifications": cderMIBNotifications,
       "cderMonitoredExceptionEvent": cderMonitoredExceptionEvent,
       "ciscoDEReportMIBConformance": ciscoDEReportMIBConformance,
       "ciscoDEReportMIBCompliances": ciscoDEReportMIBCompliances,
       "ciscoDEReportMIBCompliance": ciscoDEReportMIBCompliance,
       "ciscoDEReportMIBGroups": ciscoDEReportMIBGroups,
       "ciscoDERExceptionDataGroup": ciscoDERExceptionDataGroup,
       "ciscoDERExceptionGroup": ciscoDERExceptionGroup}
)
