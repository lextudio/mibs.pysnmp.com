# SNMP MIB module (RBN-SFP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-SFP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:22 2024
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

(IANAItuEventType,
 IANAItuProbableCause) = mibBuilder.importSymbols(
    "IANA-ITU-ALARM-TC-MIB",
    "IANAItuEventType",
    "IANAItuProbableCause")

(ItuPerceivedSeverity,) = mibBuilder.importSymbols(
    "ITU-ALARM-TC-MIB",
    "ItuPerceivedSeverity")

(RbnAlarmId,
 RbnAlarmServiceAffecting) = mibBuilder.importSymbols(
    "RBN-ALARM-TC",
    "RbnAlarmId",
    "RbnAlarmServiceAffecting")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnPort,
 RbnSlot) = mibBuilder.importSymbols(
    "RBN-TC",
    "RbnPort",
    "RbnSlot")

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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rbnSfpMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49)
)
rbnSfpMonMIB.setRevisions(
        ("2008-08-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnSfpMonMIBNotifications_ObjectIdentity = ObjectIdentity
rbnSfpMonMIBNotifications = _RbnSfpMonMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 0)
)
_RbnSfpMonMIBObjects_ObjectIdentity = ObjectIdentity
rbnSfpMonMIBObjects = _RbnSfpMonMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1)
)
_RbnSfpAlarmActiveTable_Object = MibTable
rbnSfpAlarmActiveTable = _RbnSfpAlarmActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1)
)
if mibBuilder.loadTexts:
    rbnSfpAlarmActiveTable.setStatus("current")
_RbnSfpAlarmActiveEntry_Object = MibTableRow
rbnSfpAlarmActiveEntry = _RbnSfpAlarmActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1)
)
rbnSfpAlarmActiveEntry.setIndexNames(
    (0, "RBN-SFP-MIB", "rbnSfpActiveAlarmIndex"),
)
if mibBuilder.loadTexts:
    rbnSfpAlarmActiveEntry.setStatus("current")


class _RbnSfpActiveAlarmIndex_Type(Unsigned32):
    """Custom type rbnSfpActiveAlarmIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_RbnSfpActiveAlarmIndex_Type.__name__ = "Unsigned32"
_RbnSfpActiveAlarmIndex_Object = MibTableColumn
rbnSfpActiveAlarmIndex = _RbnSfpActiveAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 1),
    _RbnSfpActiveAlarmIndex_Type()
)
rbnSfpActiveAlarmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rbnSfpActiveAlarmIndex.setStatus("current")
_RbnSfpAlarmCardSlot_Type = RbnSlot
_RbnSfpAlarmCardSlot_Object = MibTableColumn
rbnSfpAlarmCardSlot = _RbnSfpAlarmCardSlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 2),
    _RbnSfpAlarmCardSlot_Type()
)
rbnSfpAlarmCardSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSfpAlarmCardSlot.setStatus("current")
_RbnSfpAlarmPort_Type = RbnPort
_RbnSfpAlarmPort_Object = MibTableColumn
rbnSfpAlarmPort = _RbnSfpAlarmPort_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 3),
    _RbnSfpAlarmPort_Type()
)
rbnSfpAlarmPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSfpAlarmPort.setStatus("current")
_RbnSfpAlarmId_Type = RbnAlarmId
_RbnSfpAlarmId_Object = MibTableColumn
rbnSfpAlarmId = _RbnSfpAlarmId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 4),
    _RbnSfpAlarmId_Type()
)
rbnSfpAlarmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSfpAlarmId.setStatus("current")
_RbnSfpAlarmSeverity_Type = ItuPerceivedSeverity
_RbnSfpAlarmSeverity_Object = MibTableColumn
rbnSfpAlarmSeverity = _RbnSfpAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 5),
    _RbnSfpAlarmSeverity_Type()
)
rbnSfpAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSfpAlarmSeverity.setStatus("current")
_RbnSfpAlarmType_Type = IANAItuEventType
_RbnSfpAlarmType_Object = MibTableColumn
rbnSfpAlarmType = _RbnSfpAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 6),
    _RbnSfpAlarmType_Type()
)
rbnSfpAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSfpAlarmType.setStatus("current")
_RbnSfpAlarmDateAndTime_Type = DateAndTime
_RbnSfpAlarmDateAndTime_Object = MibTableColumn
rbnSfpAlarmDateAndTime = _RbnSfpAlarmDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 7),
    _RbnSfpAlarmDateAndTime_Type()
)
rbnSfpAlarmDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSfpAlarmDateAndTime.setStatus("current")


class _RbnSfpAlarmDescription_Type(SnmpAdminString):
    """Custom type rbnSfpAlarmDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RbnSfpAlarmDescription_Type.__name__ = "SnmpAdminString"
_RbnSfpAlarmDescription_Object = MibTableColumn
rbnSfpAlarmDescription = _RbnSfpAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 8),
    _RbnSfpAlarmDescription_Type()
)
rbnSfpAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSfpAlarmDescription.setStatus("current")
_RbnSfpAlarmProbableCause_Type = IANAItuProbableCause
_RbnSfpAlarmProbableCause_Object = MibTableColumn
rbnSfpAlarmProbableCause = _RbnSfpAlarmProbableCause_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 9),
    _RbnSfpAlarmProbableCause_Type()
)
rbnSfpAlarmProbableCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSfpAlarmProbableCause.setStatus("current")
_RbnSfpAlarmServiceAffecting_Type = RbnAlarmServiceAffecting
_RbnSfpAlarmServiceAffecting_Object = MibTableColumn
rbnSfpAlarmServiceAffecting = _RbnSfpAlarmServiceAffecting_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 1, 1, 1, 10),
    _RbnSfpAlarmServiceAffecting_Type()
)
rbnSfpAlarmServiceAffecting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rbnSfpAlarmServiceAffecting.setStatus("current")
_RbnSfpMonMIBConformance_ObjectIdentity = ObjectIdentity
rbnSfpMonMIBConformance = _RbnSfpMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 2)
)
_RbnSfpMonMIBGroups_ObjectIdentity = ObjectIdentity
rbnSfpMonMIBGroups = _RbnSfpMonMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 2, 1)
)
_RbnSfpMonMIBCompliances_ObjectIdentity = ObjectIdentity
rbnSfpMonMIBCompliances = _RbnSfpMonMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 2, 2)
)

# Managed Objects groups

rbnSfpMonMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 2, 1, 1)
)
rbnSfpMonMIBObjectGroup.setObjects(
      *(("RBN-SFP-MIB", "rbnSfpAlarmCardSlot"),
        ("RBN-SFP-MIB", "rbnSfpAlarmPort"),
        ("RBN-SFP-MIB", "rbnSfpAlarmId"),
        ("RBN-SFP-MIB", "rbnSfpAlarmType"),
        ("RBN-SFP-MIB", "rbnSfpAlarmDateAndTime"),
        ("RBN-SFP-MIB", "rbnSfpAlarmDescription"),
        ("RBN-SFP-MIB", "rbnSfpAlarmProbableCause"),
        ("RBN-SFP-MIB", "rbnSfpAlarmSeverity"),
        ("RBN-SFP-MIB", "rbnSfpAlarmServiceAffecting"))
)
if mibBuilder.loadTexts:
    rbnSfpMonMIBObjectGroup.setStatus("current")


# Notification objects

rbnSfpAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 0, 1)
)
rbnSfpAlarm.setObjects(
      *(("RBN-SFP-MIB", "rbnSfpAlarmCardSlot"),
        ("RBN-SFP-MIB", "rbnSfpAlarmPort"),
        ("RBN-SFP-MIB", "rbnSfpAlarmId"),
        ("RBN-SFP-MIB", "rbnSfpAlarmSeverity"),
        ("RBN-SFP-MIB", "rbnSfpAlarmType"),
        ("RBN-SFP-MIB", "rbnSfpAlarmDateAndTime"),
        ("RBN-SFP-MIB", "rbnSfpAlarmDescription"),
        ("RBN-SFP-MIB", "rbnSfpAlarmProbableCause"))
)
if mibBuilder.loadTexts:
    rbnSfpAlarm.setStatus(
        "current"
    )


# Notifications groups

rbnSfpMonMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 2, 1, 2)
)
rbnSfpMonMIBNotificationGroup.setObjects(
    ("RBN-SFP-MIB", "rbnSfpAlarm")
)
if mibBuilder.loadTexts:
    rbnSfpMonMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnSfpMonMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 49, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnSfpMonMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-SFP-MIB",
    **{"rbnSfpMonMIB": rbnSfpMonMIB,
       "rbnSfpMonMIBNotifications": rbnSfpMonMIBNotifications,
       "rbnSfpAlarm": rbnSfpAlarm,
       "rbnSfpMonMIBObjects": rbnSfpMonMIBObjects,
       "rbnSfpAlarmActiveTable": rbnSfpAlarmActiveTable,
       "rbnSfpAlarmActiveEntry": rbnSfpAlarmActiveEntry,
       "rbnSfpActiveAlarmIndex": rbnSfpActiveAlarmIndex,
       "rbnSfpAlarmCardSlot": rbnSfpAlarmCardSlot,
       "rbnSfpAlarmPort": rbnSfpAlarmPort,
       "rbnSfpAlarmId": rbnSfpAlarmId,
       "rbnSfpAlarmSeverity": rbnSfpAlarmSeverity,
       "rbnSfpAlarmType": rbnSfpAlarmType,
       "rbnSfpAlarmDateAndTime": rbnSfpAlarmDateAndTime,
       "rbnSfpAlarmDescription": rbnSfpAlarmDescription,
       "rbnSfpAlarmProbableCause": rbnSfpAlarmProbableCause,
       "rbnSfpAlarmServiceAffecting": rbnSfpAlarmServiceAffecting,
       "rbnSfpMonMIBConformance": rbnSfpMonMIBConformance,
       "rbnSfpMonMIBGroups": rbnSfpMonMIBGroups,
       "rbnSfpMonMIBObjectGroup": rbnSfpMonMIBObjectGroup,
       "rbnSfpMonMIBNotificationGroup": rbnSfpMonMIBNotificationGroup,
       "rbnSfpMonMIBCompliances": rbnSfpMonMIBCompliances,
       "rbnSfpMonMIBCompliance": rbnSfpMonMIBCompliance}
)
