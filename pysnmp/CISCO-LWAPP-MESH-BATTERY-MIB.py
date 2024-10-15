# SNMP MIB module (CISCO-LWAPP-MESH-BATTERY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-LWAPP-MESH-BATTERY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:04:41 2024
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

(cLApName,
 cLApSysMacAddress) = mibBuilder.importSymbols(
    "CISCO-LWAPP-AP-MIB",
    "cLApName",
    "cLApSysMacAddress")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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

ciscoLwappMeshBatteryMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 620)
)
ciscoLwappMeshBatteryMIB.setRevisions(
        ("2010-09-08 00:00",
         "2007-02-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoLwappMeshBatteryMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoLwappMeshBatteryMIBNotifs = _CiscoLwappMeshBatteryMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 0)
)
_CiscoLwappMeshBatteryMIBObjects_ObjectIdentity = ObjectIdentity
ciscoLwappMeshBatteryMIBObjects = _CiscoLwappMeshBatteryMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1)
)
_CiscoLwappMeshBatteryInfo_ObjectIdentity = ObjectIdentity
ciscoLwappMeshBatteryInfo = _CiscoLwappMeshBatteryInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1)
)
_ClMeshNodeBatteryTable_Object = MibTable
clMeshNodeBatteryTable = _ClMeshNodeBatteryTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1)
)
if mibBuilder.loadTexts:
    clMeshNodeBatteryTable.setStatus("current")
_ClMeshNodeBatteryEntry_Object = MibTableRow
clMeshNodeBatteryEntry = _ClMeshNodeBatteryEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1)
)
clMeshNodeBatteryEntry.setIndexNames(
    (0, "CISCO-LWAPP-AP-MIB", "cLApSysMacAddress"),
)
if mibBuilder.loadTexts:
    clMeshNodeBatteryEntry.setStatus("current")


class _ClMeshNodeBatteryModelName_Type(SnmpAdminString):
    """Custom type clMeshNodeBatteryModelName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClMeshNodeBatteryModelName_Type.__name__ = "SnmpAdminString"
_ClMeshNodeBatteryModelName_Object = MibTableColumn
clMeshNodeBatteryModelName = _ClMeshNodeBatteryModelName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 1),
    _ClMeshNodeBatteryModelName_Type()
)
clMeshNodeBatteryModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryModelName.setStatus("current")


class _ClMeshNodeBatteryStatus_Type(Integer32):
    """Custom type clMeshNodeBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("acfail", 5),
          ("low", 4),
          ("missing", 7),
          ("normal", 2),
          ("overloaded", 3),
          ("replace", 6),
          ("unknown", 1))
    )


_ClMeshNodeBatteryStatus_Type.__name__ = "Integer32"
_ClMeshNodeBatteryStatus_Object = MibTableColumn
clMeshNodeBatteryStatus = _ClMeshNodeBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 2),
    _ClMeshNodeBatteryStatus_Type()
)
clMeshNodeBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryStatus.setStatus("current")


class _ClMeshNodeBatteryChargingState_Type(Integer32):
    """Custom type clMeshNodeBatteryChargingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("charged", 5),
          ("charging", 3),
          ("disabled", 2),
          ("discharging", 4),
          ("unknown", 1))
    )


_ClMeshNodeBatteryChargingState_Type.__name__ = "Integer32"
_ClMeshNodeBatteryChargingState_Object = MibTableColumn
clMeshNodeBatteryChargingState = _ClMeshNodeBatteryChargingState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 3),
    _ClMeshNodeBatteryChargingState_Type()
)
clMeshNodeBatteryChargingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryChargingState.setStatus("deprecated")
_ClMeshNodeBatteryChargingLevel_Type = Integer32
_ClMeshNodeBatteryChargingLevel_Object = MibTableColumn
clMeshNodeBatteryChargingLevel = _ClMeshNodeBatteryChargingLevel_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 4),
    _ClMeshNodeBatteryChargingLevel_Type()
)
clMeshNodeBatteryChargingLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryChargingLevel.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeBatteryChargingLevel.setUnits("%")
_ClMeshNodeBatteryRemainingCapacity_Type = Unsigned32
_ClMeshNodeBatteryRemainingCapacity_Object = MibTableColumn
clMeshNodeBatteryRemainingCapacity = _ClMeshNodeBatteryRemainingCapacity_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 5),
    _ClMeshNodeBatteryRemainingCapacity_Type()
)
clMeshNodeBatteryRemainingCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryRemainingCapacity.setStatus("deprecated")
if mibBuilder.loadTexts:
    clMeshNodeBatteryRemainingCapacity.setUnits("minutes")


class _ClMeshNodeBatterySwVersion_Type(SnmpAdminString):
    """Custom type clMeshNodeBatterySwVersion based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClMeshNodeBatterySwVersion_Type.__name__ = "SnmpAdminString"
_ClMeshNodeBatterySwVersion_Object = MibTableColumn
clMeshNodeBatterySwVersion = _ClMeshNodeBatterySwVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 6),
    _ClMeshNodeBatterySwVersion_Type()
)
clMeshNodeBatterySwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatterySwVersion.setStatus("current")


class _ClMeshNodeBatterySerialNumber_Type(SnmpAdminString):
    """Custom type clMeshNodeBatterySerialNumber based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClMeshNodeBatterySerialNumber_Type.__name__ = "SnmpAdminString"
_ClMeshNodeBatterySerialNumber_Object = MibTableColumn
clMeshNodeBatterySerialNumber = _ClMeshNodeBatterySerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 7),
    _ClMeshNodeBatterySerialNumber_Type()
)
clMeshNodeBatterySerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatterySerialNumber.setStatus("current")
_ClMeshNodeBatteryInputVoltage_Type = Unsigned32
_ClMeshNodeBatteryInputVoltage_Object = MibTableColumn
clMeshNodeBatteryInputVoltage = _ClMeshNodeBatteryInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 8),
    _ClMeshNodeBatteryInputVoltage_Type()
)
clMeshNodeBatteryInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryInputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeBatteryInputVoltage.setUnits("milliVolts")
_ClMeshNodeBatteryOutputVoltage_Type = Unsigned32
_ClMeshNodeBatteryOutputVoltage_Object = MibTableColumn
clMeshNodeBatteryOutputVoltage = _ClMeshNodeBatteryOutputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 9),
    _ClMeshNodeBatteryOutputVoltage_Type()
)
clMeshNodeBatteryOutputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryOutputVoltage.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeBatteryOutputVoltage.setUnits("milliVolts")
_ClMeshNodeBatteryOutputPower_Type = Unsigned32
_ClMeshNodeBatteryOutputPower_Object = MibTableColumn
clMeshNodeBatteryOutputPower = _ClMeshNodeBatteryOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 10),
    _ClMeshNodeBatteryOutputPower_Type()
)
clMeshNodeBatteryOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeBatteryOutputPower.setUnits("milliWatts")
_ClMeshNodeBatteryInternalVoltage_Type = Unsigned32
_ClMeshNodeBatteryInternalVoltage_Object = MibTableColumn
clMeshNodeBatteryInternalVoltage = _ClMeshNodeBatteryInternalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 11),
    _ClMeshNodeBatteryInternalVoltage_Type()
)
clMeshNodeBatteryInternalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryInternalVoltage.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeBatteryInternalVoltage.setUnits("milliVolts")
_ClMeshNodeBatteryTemperature_Type = Integer32
_ClMeshNodeBatteryTemperature_Object = MibTableColumn
clMeshNodeBatteryTemperature = _ClMeshNodeBatteryTemperature_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 12),
    _ClMeshNodeBatteryTemperature_Type()
)
clMeshNodeBatteryTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryTemperature.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeBatteryTemperature.setUnits("degree Celsius")
_ClMeshNodeBatteryCurrent_Type = Unsigned32
_ClMeshNodeBatteryCurrent_Object = MibTableColumn
clMeshNodeBatteryCurrent = _ClMeshNodeBatteryCurrent_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 13),
    _ClMeshNodeBatteryCurrent_Type()
)
clMeshNodeBatteryCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryCurrent.setStatus("deprecated")
if mibBuilder.loadTexts:
    clMeshNodeBatteryCurrent.setUnits("milliAmps")
_ClMeshNodeBatteryCurrentValue_Type = Integer32
_ClMeshNodeBatteryCurrentValue_Object = MibTableColumn
clMeshNodeBatteryCurrentValue = _ClMeshNodeBatteryCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 1, 1, 1, 14),
    _ClMeshNodeBatteryCurrentValue_Type()
)
clMeshNodeBatteryCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clMeshNodeBatteryCurrentValue.setStatus("current")
if mibBuilder.loadTexts:
    clMeshNodeBatteryCurrentValue.setUnits("milliAmps")
_CiscoLwappMeshBatteryNotifControlConfig_ObjectIdentity = ObjectIdentity
ciscoLwappMeshBatteryNotifControlConfig = _CiscoLwappMeshBatteryNotifControlConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 2)
)


class _ClMeshBatteryAlarmEnabled_Type(TruthValue):
    """Custom type clMeshBatteryAlarmEnabled based on TruthValue"""


_ClMeshBatteryAlarmEnabled_Object = MibScalar
clMeshBatteryAlarmEnabled = _ClMeshBatteryAlarmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 1, 2, 1),
    _ClMeshBatteryAlarmEnabled_Type()
)
clMeshBatteryAlarmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clMeshBatteryAlarmEnabled.setStatus("current")
_CiscoLwappMeshBatteryMIBConform_ObjectIdentity = ObjectIdentity
ciscoLwappMeshBatteryMIBConform = _CiscoLwappMeshBatteryMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2)
)
_CiscoLwappMeshBatteryMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoLwappMeshBatteryMIBCompliances = _CiscoLwappMeshBatteryMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1)
)
_CiscoLwappMeshBatteryMIBGroups_ObjectIdentity = ObjectIdentity
ciscoLwappMeshBatteryMIBGroups = _CiscoLwappMeshBatteryMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2)
)

# Managed Objects groups

ciscoLwappMeshBatteryInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 1)
)
ciscoLwappMeshBatteryInfoGroup.setObjects(
      *(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryModelName"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingState"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingLevel"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryRemainingCapacity"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySwVersion"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySerialNumber"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInputVoltage"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputVoltage"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputPower"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInternalVoltage"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryTemperature"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryCurrent"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshBatteryInfoGroup.setStatus("deprecated")

ciscoLwappMeshBatteryNotifsConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 2)
)
ciscoLwappMeshBatteryNotifsConfigGroup.setObjects(
    ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshBatteryAlarmEnabled")
)
if mibBuilder.loadTexts:
    ciscoLwappMeshBatteryNotifsConfigGroup.setStatus("current")

ciscoLwappMeshBatteryInfoGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 4)
)
ciscoLwappMeshBatteryInfoGroupRev1.setObjects(
      *(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryModelName"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingState"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingLevel"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryRemainingCapacity"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySwVersion"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySerialNumber"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInputVoltage"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputVoltage"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputPower"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInternalVoltage"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryTemperature"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryCurrentValue"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshBatteryInfoGroupRev1.setStatus("deprecated")

ciscoLwappMeshBatteryInfoGroupRev2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 5)
)
ciscoLwappMeshBatteryInfoGroupRev2.setObjects(
      *(("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryModelName"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryChargingLevel"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySwVersion"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatterySerialNumber"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInputVoltage"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputVoltage"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryOutputPower"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryInternalVoltage"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryTemperature"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryCurrentValue"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshBatteryInfoGroupRev2.setStatus("current")


# Notification objects

ciscoLwappMeshBatteryAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 0, 1)
)
ciscoLwappMeshBatteryAlarm.setObjects(
      *(("CISCO-LWAPP-AP-MIB", "cLApName"),
        ("CISCO-LWAPP-MESH-BATTERY-MIB", "clMeshNodeBatteryStatus"))
)
if mibBuilder.loadTexts:
    ciscoLwappMeshBatteryAlarm.setStatus(
        "current"
    )


# Notifications groups

ciscoLwappMeshBatteryNotifsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 2, 3)
)
ciscoLwappMeshBatteryNotifsGroup.setObjects(
    ("CISCO-LWAPP-MESH-BATTERY-MIB", "ciscoLwappMeshBatteryAlarm")
)
if mibBuilder.loadTexts:
    ciscoLwappMeshBatteryNotifsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ciscoLwappMeshBatteryMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshBatteryMIBCompliance.setStatus(
        "deprecated"
    )

ciscoLwappMeshBatteryMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshBatteryMIBComplianceRev1.setStatus(
        "deprecated"
    )

ciscoLwappMeshBatteryMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 620, 2, 1, 3)
)
if mibBuilder.loadTexts:
    ciscoLwappMeshBatteryMIBComplianceRev2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-LWAPP-MESH-BATTERY-MIB",
    **{"ciscoLwappMeshBatteryMIB": ciscoLwappMeshBatteryMIB,
       "ciscoLwappMeshBatteryMIBNotifs": ciscoLwappMeshBatteryMIBNotifs,
       "ciscoLwappMeshBatteryAlarm": ciscoLwappMeshBatteryAlarm,
       "ciscoLwappMeshBatteryMIBObjects": ciscoLwappMeshBatteryMIBObjects,
       "ciscoLwappMeshBatteryInfo": ciscoLwappMeshBatteryInfo,
       "clMeshNodeBatteryTable": clMeshNodeBatteryTable,
       "clMeshNodeBatteryEntry": clMeshNodeBatteryEntry,
       "clMeshNodeBatteryModelName": clMeshNodeBatteryModelName,
       "clMeshNodeBatteryStatus": clMeshNodeBatteryStatus,
       "clMeshNodeBatteryChargingState": clMeshNodeBatteryChargingState,
       "clMeshNodeBatteryChargingLevel": clMeshNodeBatteryChargingLevel,
       "clMeshNodeBatteryRemainingCapacity": clMeshNodeBatteryRemainingCapacity,
       "clMeshNodeBatterySwVersion": clMeshNodeBatterySwVersion,
       "clMeshNodeBatterySerialNumber": clMeshNodeBatterySerialNumber,
       "clMeshNodeBatteryInputVoltage": clMeshNodeBatteryInputVoltage,
       "clMeshNodeBatteryOutputVoltage": clMeshNodeBatteryOutputVoltage,
       "clMeshNodeBatteryOutputPower": clMeshNodeBatteryOutputPower,
       "clMeshNodeBatteryInternalVoltage": clMeshNodeBatteryInternalVoltage,
       "clMeshNodeBatteryTemperature": clMeshNodeBatteryTemperature,
       "clMeshNodeBatteryCurrent": clMeshNodeBatteryCurrent,
       "clMeshNodeBatteryCurrentValue": clMeshNodeBatteryCurrentValue,
       "ciscoLwappMeshBatteryNotifControlConfig": ciscoLwappMeshBatteryNotifControlConfig,
       "clMeshBatteryAlarmEnabled": clMeshBatteryAlarmEnabled,
       "ciscoLwappMeshBatteryMIBConform": ciscoLwappMeshBatteryMIBConform,
       "ciscoLwappMeshBatteryMIBCompliances": ciscoLwappMeshBatteryMIBCompliances,
       "ciscoLwappMeshBatteryMIBCompliance": ciscoLwappMeshBatteryMIBCompliance,
       "ciscoLwappMeshBatteryMIBComplianceRev1": ciscoLwappMeshBatteryMIBComplianceRev1,
       "ciscoLwappMeshBatteryMIBComplianceRev2": ciscoLwappMeshBatteryMIBComplianceRev2,
       "ciscoLwappMeshBatteryMIBGroups": ciscoLwappMeshBatteryMIBGroups,
       "ciscoLwappMeshBatteryInfoGroup": ciscoLwappMeshBatteryInfoGroup,
       "ciscoLwappMeshBatteryNotifsConfigGroup": ciscoLwappMeshBatteryNotifsConfigGroup,
       "ciscoLwappMeshBatteryNotifsGroup": ciscoLwappMeshBatteryNotifsGroup,
       "ciscoLwappMeshBatteryInfoGroupRev1": ciscoLwappMeshBatteryInfoGroupRev1,
       "ciscoLwappMeshBatteryInfoGroupRev2": ciscoLwappMeshBatteryInfoGroupRev2}
)
