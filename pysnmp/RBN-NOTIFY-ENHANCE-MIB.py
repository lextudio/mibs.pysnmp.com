# SNMP MIB module (RBN-NOTIFY-ENHANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RBN-NOTIFY-ENHANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:45:18 2024
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

(dsx1LineStatus,
 dsx1LineStatusLastChange) = mibBuilder.importSymbols(
    "DS1-MIB",
    "dsx1LineStatus",
    "dsx1LineStatusLastChange")

(dsx3LineStatus,
 dsx3LineStatusLastChange) = mibBuilder.importSymbols(
    "DS3-MIB",
    "dsx3LineStatus",
    "dsx3LineStatusLastChange")

(ifAdminStatus,
 ifHighSpeed,
 ifIndex,
 ifOperStatus,
 ifSpeed) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAdminStatus",
    "ifHighSpeed",
    "ifIndex",
    "ifOperStatus",
    "ifSpeed")

(rbnCardAlarmDateAndTime,
 rbnCardAlarmDescription,
 rbnCardAlarmId,
 rbnCardAlarmProbableCause,
 rbnCardAlarmServiceAffecting,
 rbnCardAlarmSeverity,
 rbnCardAlarmType) = mibBuilder.importSymbols(
    "RBN-CARDMON-MIB",
    "rbnCardAlarmDateAndTime",
    "rbnCardAlarmDescription",
    "rbnCardAlarmId",
    "rbnCardAlarmProbableCause",
    "rbnCardAlarmServiceAffecting",
    "rbnCardAlarmSeverity",
    "rbnCardAlarmType")

(rbnDsx1AlarmServiceAffecting,
 rbnDsx1AlarmSeverity) = mibBuilder.importSymbols(
    "RBN-DS1-MIB",
    "rbnDsx1AlarmServiceAffecting",
    "rbnDsx1AlarmSeverity")

(rbnDsx3AlarmServiceAffecting,
 rbnDsx3AlarmSeverity) = mibBuilder.importSymbols(
    "RBN-DS3-MIB",
    "rbnDsx3AlarmServiceAffecting",
    "rbnDsx3AlarmSeverity")

(rbnMgmt,) = mibBuilder.importSymbols(
    "RBN-SMI",
    "rbnMgmt")

(RbnSlot,) = mibBuilder.importSymbols(
    "RBN-TC",
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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rbnNotifyEnhanceMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36)
)
rbnNotifyEnhanceMIB.setRevisions(
        ("2009-03-23 17:00",
         "2005-05-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RbnNotifyEnhanceMIBNotifications_ObjectIdentity = ObjectIdentity
rbnNotifyEnhanceMIBNotifications = _RbnNotifyEnhanceMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 0)
)
_RbnNotifyEnhanceMIBObjects_ObjectIdentity = ObjectIdentity
rbnNotifyEnhanceMIBObjects = _RbnNotifyEnhanceMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 1)
)
_RbnNEGeneral_ObjectIdentity = ObjectIdentity
rbnNEGeneral = _RbnNEGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 1, 1)
)
_RbnNESlot_Type = RbnSlot
_RbnNESlot_Object = MibScalar
rbnNESlot = _RbnNESlot_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 1, 1, 1),
    _RbnNESlot_Type()
)
rbnNESlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnNESlot.setStatus("current")


class _RbnNECardName_Type(DisplayString):
    """Custom type rbnNECardName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbnNECardName_Type.__name__ = "DisplayString"
_RbnNECardName_Object = MibScalar
rbnNECardName = _RbnNECardName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 1, 1, 2),
    _RbnNECardName_Type()
)
rbnNECardName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnNECardName.setStatus("current")


class _RbnNECardOp_Type(Integer32):
    """Custom type rbnNECardOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("insert", 1),
          ("other", 3),
          ("remove", 2))
    )


_RbnNECardOp_Type.__name__ = "Integer32"
_RbnNECardOp_Object = MibScalar
rbnNECardOp = _RbnNECardOp_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 1, 1, 3),
    _RbnNECardOp_Type()
)
rbnNECardOp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnNECardOp.setStatus("current")


class _RbnNECircuitId_Type(DisplayString):
    """Custom type rbnNECircuitId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RbnNECircuitId_Type.__name__ = "DisplayString"
_RbnNECircuitId_Object = MibScalar
rbnNECircuitId = _RbnNECircuitId_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 1, 1, 4),
    _RbnNECircuitId_Type()
)
rbnNECircuitId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnNECircuitId.setStatus("current")
_RbnNEGroupName_Type = SnmpAdminString
_RbnNEGroupName_Object = MibScalar
rbnNEGroupName = _RbnNEGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 1, 1, 5),
    _RbnNEGroupName_Type()
)
rbnNEGroupName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    rbnNEGroupName.setStatus("current")
_RbnNotifyEnhanceMIBConformance_ObjectIdentity = ObjectIdentity
rbnNotifyEnhanceMIBConformance = _RbnNotifyEnhanceMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 2)
)
_RbnNotifyEnhanceMIBGroups_ObjectIdentity = ObjectIdentity
rbnNotifyEnhanceMIBGroups = _RbnNotifyEnhanceMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 2, 1)
)
_RbnNotifyEnhanceMIBCompliances_ObjectIdentity = ObjectIdentity
rbnNotifyEnhanceMIBCompliances = _RbnNotifyEnhanceMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 2, 2)
)

# Managed Objects groups

rbnNotifyEnhanceMIBObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 2, 1, 1)
)
rbnNotifyEnhanceMIBObjectGroup.setObjects(
      *(("RBN-NOTIFY-ENHANCE-MIB", "rbnNESlot"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECardName"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECardOp"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECircuitId"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNEGroupName"))
)
if mibBuilder.loadTexts:
    rbnNotifyEnhanceMIBObjectGroup.setStatus("current")


# Notification objects

rbnNEentConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 0, 1)
)
rbnNEentConfigChange.setObjects(
      *(("RBN-NOTIFY-ENHANCE-MIB", "rbnNESlot"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECardName"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECardOp"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    rbnNEentConfigChange.setStatus(
        "current"
    )

rbnNECardAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 0, 2)
)
rbnNECardAlarm.setObjects(
      *(("RBN-CARDMON-MIB", "rbnCardAlarmId"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmType"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmDateAndTime"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmDescription"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmProbableCause"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmSeverity"),
        ("RBN-CARDMON-MIB", "rbnCardAlarmServiceAffecting"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECardName"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    rbnNECardAlarm.setStatus(
        "current"
    )

rbnNElinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 0, 3)
)
rbnNElinkDown.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifSpeed"),
        ("IF-MIB", "ifHighSpeed"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECircuitId"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    rbnNElinkDown.setStatus(
        "current"
    )

rbnNElinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 0, 4)
)
rbnNElinkUp.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifSpeed"),
        ("IF-MIB", "ifHighSpeed"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECircuitId"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    rbnNElinkUp.setStatus(
        "current"
    )

rbnNEdsx1LineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 0, 5)
)
rbnNEdsx1LineStatusChange.setObjects(
      *(("DS1-MIB", "dsx1LineStatus"),
        ("DS1-MIB", "dsx1LineStatusLastChange"),
        ("RBN-DS1-MIB", "rbnDsx1AlarmSeverity"),
        ("RBN-DS1-MIB", "rbnDsx1AlarmServiceAffecting"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECircuitId"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    rbnNEdsx1LineStatusChange.setStatus(
        "current"
    )

rbnNEdsx3LineStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 0, 6)
)
rbnNEdsx3LineStatusChange.setObjects(
      *(("DS3-MIB", "dsx3LineStatus"),
        ("DS3-MIB", "dsx3LineStatusLastChange"),
        ("RBN-DS3-MIB", "rbnDsx3AlarmSeverity"),
        ("RBN-DS3-MIB", "rbnDsx3AlarmServiceAffecting"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECircuitId"),
        ("SNMPv2-MIB", "sysName"))
)
if mibBuilder.loadTexts:
    rbnNEdsx3LineStatusChange.setStatus(
        "current"
    )


# Notifications groups

rbnNotifyEnhanceMIBNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 2, 1, 2)
)
rbnNotifyEnhanceMIBNotificationGroup.setObjects(
      *(("RBN-NOTIFY-ENHANCE-MIB", "rbnNEentConfigChange"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNECardAlarm"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNElinkDown"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNElinkUp"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNEdsx1LineStatusChange"),
        ("RBN-NOTIFY-ENHANCE-MIB", "rbnNEdsx3LineStatusChange"))
)
if mibBuilder.loadTexts:
    rbnNotifyEnhanceMIBNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

rbnNotifyEnhanceMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rbnNotifyEnhanceMIBCompliance.setStatus(
        "deprecated"
    )

rbnNotifyEnhanceMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2352, 2, 36, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rbnNotifyEnhanceMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RBN-NOTIFY-ENHANCE-MIB",
    **{"rbnNotifyEnhanceMIB": rbnNotifyEnhanceMIB,
       "rbnNotifyEnhanceMIBNotifications": rbnNotifyEnhanceMIBNotifications,
       "rbnNEentConfigChange": rbnNEentConfigChange,
       "rbnNECardAlarm": rbnNECardAlarm,
       "rbnNElinkDown": rbnNElinkDown,
       "rbnNElinkUp": rbnNElinkUp,
       "rbnNEdsx1LineStatusChange": rbnNEdsx1LineStatusChange,
       "rbnNEdsx3LineStatusChange": rbnNEdsx3LineStatusChange,
       "rbnNotifyEnhanceMIBObjects": rbnNotifyEnhanceMIBObjects,
       "rbnNEGeneral": rbnNEGeneral,
       "rbnNESlot": rbnNESlot,
       "rbnNECardName": rbnNECardName,
       "rbnNECardOp": rbnNECardOp,
       "rbnNECircuitId": rbnNECircuitId,
       "rbnNEGroupName": rbnNEGroupName,
       "rbnNotifyEnhanceMIBConformance": rbnNotifyEnhanceMIBConformance,
       "rbnNotifyEnhanceMIBGroups": rbnNotifyEnhanceMIBGroups,
       "rbnNotifyEnhanceMIBObjectGroup": rbnNotifyEnhanceMIBObjectGroup,
       "rbnNotifyEnhanceMIBNotificationGroup": rbnNotifyEnhanceMIBNotificationGroup,
       "rbnNotifyEnhanceMIBCompliances": rbnNotifyEnhanceMIBCompliances,
       "rbnNotifyEnhanceMIBCompliance": rbnNotifyEnhanceMIBCompliance,
       "rbnNotifyEnhanceMIBCompliance2": rbnNotifyEnhanceMIBCompliance2}
)
