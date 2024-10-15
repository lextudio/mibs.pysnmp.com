# SNMP MIB module (ZHONE-GEN-INTERFACE-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-GEN-INTERFACE-CONFIG-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:31 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(zhoneInterfaceConfig,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneInterfaceConfig",
    "zhoneModules")

(ZhoneAlarmSeverity,
 ZhoneRowStatus) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneAlarmSeverity",
    "ZhoneRowStatus")


# MODULE-IDENTITY

alarmConfigMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1)
)
alarmConfigMib.setRevisions(
        ("2010-12-07 02:37",
         "2008-02-26 06:25")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlarmConfigTable_Object = MibTable
alarmConfigTable = _AlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1)
)
if mibBuilder.loadTexts:
    alarmConfigTable.setStatus("current")
_AlarmConfigEntry_Object = MibTableRow
alarmConfigEntry = _AlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1)
)
alarmConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alarmConfigEntry.setStatus("current")
_AlarmConfigBitRateThreshold_Type = TruthValue
_AlarmConfigBitRateThreshold_Object = MibTableColumn
alarmConfigBitRateThreshold = _AlarmConfigBitRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 1),
    _AlarmConfigBitRateThreshold_Type()
)
alarmConfigBitRateThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmConfigBitRateThreshold.setStatus("current")
_AlarmConfigBitRateThresholdValue_Type = Integer32
_AlarmConfigBitRateThresholdValue_Object = MibTableColumn
alarmConfigBitRateThresholdValue = _AlarmConfigBitRateThresholdValue_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 2),
    _AlarmConfigBitRateThresholdValue_Type()
)
alarmConfigBitRateThresholdValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmConfigBitRateThresholdValue.setStatus("current")
_AlarmConfigBitRateThresholdHoldtime_Type = Integer32
_AlarmConfigBitRateThresholdHoldtime_Object = MibTableColumn
alarmConfigBitRateThresholdHoldtime = _AlarmConfigBitRateThresholdHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 3),
    _AlarmConfigBitRateThresholdHoldtime_Type()
)
alarmConfigBitRateThresholdHoldtime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmConfigBitRateThresholdHoldtime.setStatus("current")
_AlarmConfigStatusTrap_Type = TruthValue
_AlarmConfigStatusTrap_Object = MibTableColumn
alarmConfigStatusTrap = _AlarmConfigStatusTrap_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 4),
    _AlarmConfigStatusTrap_Type()
)
alarmConfigStatusTrap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmConfigStatusTrap.setStatus("current")
_AlarmConfigAdminUp_Type = TruthValue
_AlarmConfigAdminUp_Object = MibTableColumn
alarmConfigAdminUp = _AlarmConfigAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 5),
    _AlarmConfigAdminUp_Type()
)
alarmConfigAdminUp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmConfigAdminUp.setStatus("current")
_AlarmConfigAlarmSeverity_Type = ZhoneAlarmSeverity
_AlarmConfigAlarmSeverity_Object = MibTableColumn
alarmConfigAlarmSeverity = _AlarmConfigAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 6),
    _AlarmConfigAlarmSeverity_Type()
)
alarmConfigAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmConfigAlarmSeverity.setStatus("current")
_AlarmConfigRowStatus_Type = ZhoneRowStatus
_AlarmConfigRowStatus_Object = MibTableColumn
alarmConfigRowStatus = _AlarmConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 1, 1, 7),
    _AlarmConfigRowStatus_Type()
)
alarmConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alarmConfigRowStatus.setStatus("current")
_AlarmConfigTraps_ObjectIdentity = ObjectIdentity
alarmConfigTraps = _AlarmConfigTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 2)
)
_AlarmConfigTrapPrefix_ObjectIdentity = ObjectIdentity
alarmConfigTrapPrefix = _AlarmConfigTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 2, 0)
)
if mibBuilder.loadTexts:
    alarmConfigTrapPrefix.setStatus("current")

# Managed Objects groups


# Notification objects

zhoneAlarmConfigThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 2, 0, 1)
)
if mibBuilder.loadTexts:
    zhoneAlarmConfigThresholdTrap.setStatus(
        "current"
    )

zhoneAlarmConfigThresholdClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 3, 13, 1, 2, 0, 2)
)
if mibBuilder.loadTexts:
    zhoneAlarmConfigThresholdClearTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-GEN-INTERFACE-CONFIG-MIB",
    **{"alarmConfigMib": alarmConfigMib,
       "alarmConfigTable": alarmConfigTable,
       "alarmConfigEntry": alarmConfigEntry,
       "alarmConfigBitRateThreshold": alarmConfigBitRateThreshold,
       "alarmConfigBitRateThresholdValue": alarmConfigBitRateThresholdValue,
       "alarmConfigBitRateThresholdHoldtime": alarmConfigBitRateThresholdHoldtime,
       "alarmConfigStatusTrap": alarmConfigStatusTrap,
       "alarmConfigAdminUp": alarmConfigAdminUp,
       "alarmConfigAlarmSeverity": alarmConfigAlarmSeverity,
       "alarmConfigRowStatus": alarmConfigRowStatus,
       "alarmConfigTraps": alarmConfigTraps,
       "alarmConfigTrapPrefix": alarmConfigTrapPrefix,
       "zhoneAlarmConfigThresholdTrap": zhoneAlarmConfigThresholdTrap,
       "zhoneAlarmConfigThresholdClearTrap": zhoneAlarmConfigThresholdClearTrap}
)
