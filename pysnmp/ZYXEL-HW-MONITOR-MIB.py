# SNMP MIB module (ZYXEL-HW-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZYXEL-HW-MONITOR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:21:57 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelHwMonitor = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelHwMonitorStatus_ObjectIdentity = ObjectIdentity
zyxelHwMonitorStatus = _ZyxelHwMonitorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1)
)
_ZyxelHwMonitorFanRpmTable_Object = MibTable
zyxelHwMonitorFanRpmTable = _ZyxelHwMonitorFanRpmTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 1)
)
if mibBuilder.loadTexts:
    zyxelHwMonitorFanRpmTable.setStatus("current")
_ZyxelHwMonitorFanRpmEntry_Object = MibTableRow
zyxelHwMonitorFanRpmEntry = _ZyxelHwMonitorFanRpmEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 1, 1)
)
zyxelHwMonitorFanRpmEntry.setIndexNames(
    (0, "ZYXEL-HW-MONITOR-MIB", "zyHwMonitorFanRpmIndex"),
)
if mibBuilder.loadTexts:
    zyxelHwMonitorFanRpmEntry.setStatus("current")
_ZyHwMonitorFanRpmIndex_Type = Integer32
_ZyHwMonitorFanRpmIndex_Object = MibTableColumn
zyHwMonitorFanRpmIndex = _ZyHwMonitorFanRpmIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 1, 1, 1),
    _ZyHwMonitorFanRpmIndex_Type()
)
zyHwMonitorFanRpmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyHwMonitorFanRpmIndex.setStatus("current")
_ZyHwMonitorFanRpmDescription_Type = DisplayString
_ZyHwMonitorFanRpmDescription_Object = MibTableColumn
zyHwMonitorFanRpmDescription = _ZyHwMonitorFanRpmDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 1, 1, 2),
    _ZyHwMonitorFanRpmDescription_Type()
)
zyHwMonitorFanRpmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorFanRpmDescription.setStatus("current")
_ZyHwMonitorFanRpmCurrentValue_Type = Integer32
_ZyHwMonitorFanRpmCurrentValue_Object = MibTableColumn
zyHwMonitorFanRpmCurrentValue = _ZyHwMonitorFanRpmCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 1, 1, 3),
    _ZyHwMonitorFanRpmCurrentValue_Type()
)
zyHwMonitorFanRpmCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorFanRpmCurrentValue.setStatus("current")
_ZyHwMonitorFanRpmMaxValue_Type = Integer32
_ZyHwMonitorFanRpmMaxValue_Object = MibTableColumn
zyHwMonitorFanRpmMaxValue = _ZyHwMonitorFanRpmMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 1, 1, 4),
    _ZyHwMonitorFanRpmMaxValue_Type()
)
zyHwMonitorFanRpmMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorFanRpmMaxValue.setStatus("current")
_ZyHwMonitorFanRpmMinValue_Type = Integer32
_ZyHwMonitorFanRpmMinValue_Object = MibTableColumn
zyHwMonitorFanRpmMinValue = _ZyHwMonitorFanRpmMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 1, 1, 5),
    _ZyHwMonitorFanRpmMinValue_Type()
)
zyHwMonitorFanRpmMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorFanRpmMinValue.setStatus("current")
_ZyHwMonitorFanRpmLowThreshold_Type = Integer32
_ZyHwMonitorFanRpmLowThreshold_Object = MibTableColumn
zyHwMonitorFanRpmLowThreshold = _ZyHwMonitorFanRpmLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 1, 1, 6),
    _ZyHwMonitorFanRpmLowThreshold_Type()
)
zyHwMonitorFanRpmLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorFanRpmLowThreshold.setStatus("current")
_ZyHwMonitorFanRpmStatus_Type = DisplayString
_ZyHwMonitorFanRpmStatus_Object = MibTableColumn
zyHwMonitorFanRpmStatus = _ZyHwMonitorFanRpmStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 1, 1, 7),
    _ZyHwMonitorFanRpmStatus_Type()
)
zyHwMonitorFanRpmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorFanRpmStatus.setStatus("current")
_ZyxelHwMonitorTemperatureTable_Object = MibTable
zyxelHwMonitorTemperatureTable = _ZyxelHwMonitorTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelHwMonitorTemperatureTable.setStatus("current")
_ZyxelHwMonitorTemperatureEntry_Object = MibTableRow
zyxelHwMonitorTemperatureEntry = _ZyxelHwMonitorTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 2, 1)
)
zyxelHwMonitorTemperatureEntry.setIndexNames(
    (0, "ZYXEL-HW-MONITOR-MIB", "zyHwMonitorTemperatureIndex"),
)
if mibBuilder.loadTexts:
    zyxelHwMonitorTemperatureEntry.setStatus("current")
_ZyHwMonitorTemperatureIndex_Type = Integer32
_ZyHwMonitorTemperatureIndex_Object = MibTableColumn
zyHwMonitorTemperatureIndex = _ZyHwMonitorTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 2, 1, 1),
    _ZyHwMonitorTemperatureIndex_Type()
)
zyHwMonitorTemperatureIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyHwMonitorTemperatureIndex.setStatus("current")
_ZyHwMonitorTemperatureDescription_Type = DisplayString
_ZyHwMonitorTemperatureDescription_Object = MibTableColumn
zyHwMonitorTemperatureDescription = _ZyHwMonitorTemperatureDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 2, 1, 2),
    _ZyHwMonitorTemperatureDescription_Type()
)
zyHwMonitorTemperatureDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorTemperatureDescription.setStatus("current")
_ZyHwMonitorTemperatureCurrentValue_Type = Integer32
_ZyHwMonitorTemperatureCurrentValue_Object = MibTableColumn
zyHwMonitorTemperatureCurrentValue = _ZyHwMonitorTemperatureCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 2, 1, 3),
    _ZyHwMonitorTemperatureCurrentValue_Type()
)
zyHwMonitorTemperatureCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorTemperatureCurrentValue.setStatus("current")
_ZyHwMonitorTemperatureMaxValue_Type = Integer32
_ZyHwMonitorTemperatureMaxValue_Object = MibTableColumn
zyHwMonitorTemperatureMaxValue = _ZyHwMonitorTemperatureMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 2, 1, 4),
    _ZyHwMonitorTemperatureMaxValue_Type()
)
zyHwMonitorTemperatureMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorTemperatureMaxValue.setStatus("current")
_ZyHwMonitorTemperatureMinValue_Type = Integer32
_ZyHwMonitorTemperatureMinValue_Object = MibTableColumn
zyHwMonitorTemperatureMinValue = _ZyHwMonitorTemperatureMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 2, 1, 5),
    _ZyHwMonitorTemperatureMinValue_Type()
)
zyHwMonitorTemperatureMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorTemperatureMinValue.setStatus("current")
_ZyHwMonitorTemperatureHighThreshold_Type = Integer32
_ZyHwMonitorTemperatureHighThreshold_Object = MibTableColumn
zyHwMonitorTemperatureHighThreshold = _ZyHwMonitorTemperatureHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 2, 1, 6),
    _ZyHwMonitorTemperatureHighThreshold_Type()
)
zyHwMonitorTemperatureHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorTemperatureHighThreshold.setStatus("current")
_ZyHwMonitorTemperatureStatus_Type = DisplayString
_ZyHwMonitorTemperatureStatus_Object = MibTableColumn
zyHwMonitorTemperatureStatus = _ZyHwMonitorTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 2, 1, 7),
    _ZyHwMonitorTemperatureStatus_Type()
)
zyHwMonitorTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorTemperatureStatus.setStatus("current")
_ZyxelHwMonitorVoltageTable_Object = MibTable
zyxelHwMonitorVoltageTable = _ZyxelHwMonitorVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 3)
)
if mibBuilder.loadTexts:
    zyxelHwMonitorVoltageTable.setStatus("current")
_ZyxelHwMonitorVoltageEntry_Object = MibTableRow
zyxelHwMonitorVoltageEntry = _ZyxelHwMonitorVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 3, 1)
)
zyxelHwMonitorVoltageEntry.setIndexNames(
    (0, "ZYXEL-HW-MONITOR-MIB", "zyHwMonitorVoltageIndex"),
)
if mibBuilder.loadTexts:
    zyxelHwMonitorVoltageEntry.setStatus("current")
_ZyHwMonitorVoltageIndex_Type = Integer32
_ZyHwMonitorVoltageIndex_Object = MibTableColumn
zyHwMonitorVoltageIndex = _ZyHwMonitorVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 3, 1, 1),
    _ZyHwMonitorVoltageIndex_Type()
)
zyHwMonitorVoltageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyHwMonitorVoltageIndex.setStatus("current")
_ZyHwMonitorVoltageDescription_Type = DisplayString
_ZyHwMonitorVoltageDescription_Object = MibTableColumn
zyHwMonitorVoltageDescription = _ZyHwMonitorVoltageDescription_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 3, 1, 2),
    _ZyHwMonitorVoltageDescription_Type()
)
zyHwMonitorVoltageDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorVoltageDescription.setStatus("current")
_ZyHwMonitorVoltageCurrentValue_Type = Integer32
_ZyHwMonitorVoltageCurrentValue_Object = MibTableColumn
zyHwMonitorVoltageCurrentValue = _ZyHwMonitorVoltageCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 3, 1, 3),
    _ZyHwMonitorVoltageCurrentValue_Type()
)
zyHwMonitorVoltageCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorVoltageCurrentValue.setStatus("current")
_ZyHwMonitorVoltageMaxValue_Type = Integer32
_ZyHwMonitorVoltageMaxValue_Object = MibTableColumn
zyHwMonitorVoltageMaxValue = _ZyHwMonitorVoltageMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 3, 1, 4),
    _ZyHwMonitorVoltageMaxValue_Type()
)
zyHwMonitorVoltageMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorVoltageMaxValue.setStatus("current")
_ZyHwMonitorVoltageMinValue_Type = Integer32
_ZyHwMonitorVoltageMinValue_Object = MibTableColumn
zyHwMonitorVoltageMinValue = _ZyHwMonitorVoltageMinValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 3, 1, 5),
    _ZyHwMonitorVoltageMinValue_Type()
)
zyHwMonitorVoltageMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorVoltageMinValue.setStatus("current")
_ZyHwMonitorVoltageNominalValue_Type = Integer32
_ZyHwMonitorVoltageNominalValue_Object = MibTableColumn
zyHwMonitorVoltageNominalValue = _ZyHwMonitorVoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 3, 1, 6),
    _ZyHwMonitorVoltageNominalValue_Type()
)
zyHwMonitorVoltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorVoltageNominalValue.setStatus("current")
_ZyHwMonitorVoltageLowThreshold_Type = Integer32
_ZyHwMonitorVoltageLowThreshold_Object = MibTableColumn
zyHwMonitorVoltageLowThreshold = _ZyHwMonitorVoltageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 3, 1, 7),
    _ZyHwMonitorVoltageLowThreshold_Type()
)
zyHwMonitorVoltageLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorVoltageLowThreshold.setStatus("current")
_ZyHwMonitorVoltageStatus_Type = DisplayString
_ZyHwMonitorVoltageStatus_Object = MibTableColumn
zyHwMonitorVoltageStatus = _ZyHwMonitorVoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 3, 1, 8),
    _ZyHwMonitorVoltageStatus_Type()
)
zyHwMonitorVoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorVoltageStatus.setStatus("current")
_ZyxelHwMonitorPowerSource_ObjectIdentity = ObjectIdentity
zyxelHwMonitorPowerSource = _ZyxelHwMonitorPowerSource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 4)
)
_ZyHwMonitorPowerSourceMode_Type = DisplayString
_ZyHwMonitorPowerSourceMode_Object = MibScalar
zyHwMonitorPowerSourceMode = _ZyHwMonitorPowerSourceMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 4, 1),
    _ZyHwMonitorPowerSourceMode_Type()
)
zyHwMonitorPowerSourceMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorPowerSourceMode.setStatus("current")
_ZyxelHwMonitorPowerSourceTable_Object = MibTable
zyxelHwMonitorPowerSourceTable = _ZyxelHwMonitorPowerSourceTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 4, 2)
)
if mibBuilder.loadTexts:
    zyxelHwMonitorPowerSourceTable.setStatus("current")
_ZyxelHwMonitorPowerSourceEntry_Object = MibTableRow
zyxelHwMonitorPowerSourceEntry = _ZyxelHwMonitorPowerSourceEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 4, 2, 1)
)
zyxelHwMonitorPowerSourceEntry.setIndexNames(
    (0, "ZYXEL-HW-MONITOR-MIB", "zyHwMonitorPowerSourceIndex"),
)
if mibBuilder.loadTexts:
    zyxelHwMonitorPowerSourceEntry.setStatus("current")
_ZyHwMonitorPowerSourceIndex_Type = Integer32
_ZyHwMonitorPowerSourceIndex_Object = MibTableColumn
zyHwMonitorPowerSourceIndex = _ZyHwMonitorPowerSourceIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 4, 2, 1, 1),
    _ZyHwMonitorPowerSourceIndex_Type()
)
zyHwMonitorPowerSourceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zyHwMonitorPowerSourceIndex.setStatus("current")
_ZyHwMonitorPowerSourceType_Type = DisplayString
_ZyHwMonitorPowerSourceType_Object = MibTableColumn
zyHwMonitorPowerSourceType = _ZyHwMonitorPowerSourceType_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 4, 2, 1, 2),
    _ZyHwMonitorPowerSourceType_Type()
)
zyHwMonitorPowerSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorPowerSourceType.setStatus("current")
_ZyHwMonitorPowerSourceStatus_Type = DisplayString
_ZyHwMonitorPowerSourceStatus_Object = MibTableColumn
zyHwMonitorPowerSourceStatus = _ZyHwMonitorPowerSourceStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 1, 4, 2, 1, 3),
    _ZyHwMonitorPowerSourceStatus_Type()
)
zyHwMonitorPowerSourceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zyHwMonitorPowerSourceStatus.setStatus("current")
_ZyxelHwMonitorNotifications_ObjectIdentity = ObjectIdentity
zyxelHwMonitorNotifications = _ZyxelHwMonitorNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 2)
)

# Managed Objects groups


# Notification objects

zyHwMonitorFanSpeedOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 2, 1)
)
zyHwMonitorFanSpeedOutOfRange.setObjects(
      *(("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorFanRpmIndex"),
        ("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorFanRpmDescription"))
)
if mibBuilder.loadTexts:
    zyHwMonitorFanSpeedOutOfRange.setStatus(
        "current"
    )

zyHwMonitorTemperatureOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 2, 2)
)
zyHwMonitorTemperatureOutOfRange.setObjects(
      *(("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorTemperatureIndex"),
        ("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorTemperatureDescription"))
)
if mibBuilder.loadTexts:
    zyHwMonitorTemperatureOutOfRange.setStatus(
        "current"
    )

zyHwMonitorPowerSupplyVoltageOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 2, 3)
)
zyHwMonitorPowerSupplyVoltageOutOfRange.setObjects(
      *(("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorVoltageIndex"),
        ("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorVoltageDescription"))
)
if mibBuilder.loadTexts:
    zyHwMonitorPowerSupplyVoltageOutOfRange.setStatus(
        "current"
    )

zyHwMonitorBackupPowerSupplyInUse = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 2, 4)
)
if mibBuilder.loadTexts:
    zyHwMonitorBackupPowerSupplyInUse.setStatus(
        "current"
    )

zyHwMonitorDyingGasp = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 2, 5)
)
if mibBuilder.loadTexts:
    zyHwMonitorDyingGasp.setStatus(
        "current"
    )

zyHwMonitorFanAirFlowInconsistency = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 2, 6)
)
if mibBuilder.loadTexts:
    zyHwMonitorFanAirFlowInconsistency.setStatus(
        "current"
    )

zyHwMonitorFanSpeedOutOfRangeRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 2, 7)
)
zyHwMonitorFanSpeedOutOfRangeRecovered.setObjects(
      *(("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorFanRpmIndex"),
        ("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorFanRpmDescription"))
)
if mibBuilder.loadTexts:
    zyHwMonitorFanSpeedOutOfRangeRecovered.setStatus(
        "current"
    )

zyHwMonitorTemperatureOutOfRangeRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 2, 8)
)
zyHwMonitorTemperatureOutOfRangeRecovered.setObjects(
      *(("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorTemperatureIndex"),
        ("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorTemperatureDescription"))
)
if mibBuilder.loadTexts:
    zyHwMonitorTemperatureOutOfRangeRecovered.setStatus(
        "current"
    )

zyHwMonitorPowerSupplyVoltageOutOfRangeRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 26, 2, 9)
)
zyHwMonitorPowerSupplyVoltageOutOfRangeRecovered.setObjects(
      *(("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorVoltageIndex"),
        ("ZYXEL-HW-MONITOR-MIB", "zyHwMonitorVoltageDescription"))
)
if mibBuilder.loadTexts:
    zyHwMonitorPowerSupplyVoltageOutOfRangeRecovered.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-HW-MONITOR-MIB",
    **{"zyxelHwMonitor": zyxelHwMonitor,
       "zyxelHwMonitorStatus": zyxelHwMonitorStatus,
       "zyxelHwMonitorFanRpmTable": zyxelHwMonitorFanRpmTable,
       "zyxelHwMonitorFanRpmEntry": zyxelHwMonitorFanRpmEntry,
       "zyHwMonitorFanRpmIndex": zyHwMonitorFanRpmIndex,
       "zyHwMonitorFanRpmDescription": zyHwMonitorFanRpmDescription,
       "zyHwMonitorFanRpmCurrentValue": zyHwMonitorFanRpmCurrentValue,
       "zyHwMonitorFanRpmMaxValue": zyHwMonitorFanRpmMaxValue,
       "zyHwMonitorFanRpmMinValue": zyHwMonitorFanRpmMinValue,
       "zyHwMonitorFanRpmLowThreshold": zyHwMonitorFanRpmLowThreshold,
       "zyHwMonitorFanRpmStatus": zyHwMonitorFanRpmStatus,
       "zyxelHwMonitorTemperatureTable": zyxelHwMonitorTemperatureTable,
       "zyxelHwMonitorTemperatureEntry": zyxelHwMonitorTemperatureEntry,
       "zyHwMonitorTemperatureIndex": zyHwMonitorTemperatureIndex,
       "zyHwMonitorTemperatureDescription": zyHwMonitorTemperatureDescription,
       "zyHwMonitorTemperatureCurrentValue": zyHwMonitorTemperatureCurrentValue,
       "zyHwMonitorTemperatureMaxValue": zyHwMonitorTemperatureMaxValue,
       "zyHwMonitorTemperatureMinValue": zyHwMonitorTemperatureMinValue,
       "zyHwMonitorTemperatureHighThreshold": zyHwMonitorTemperatureHighThreshold,
       "zyHwMonitorTemperatureStatus": zyHwMonitorTemperatureStatus,
       "zyxelHwMonitorVoltageTable": zyxelHwMonitorVoltageTable,
       "zyxelHwMonitorVoltageEntry": zyxelHwMonitorVoltageEntry,
       "zyHwMonitorVoltageIndex": zyHwMonitorVoltageIndex,
       "zyHwMonitorVoltageDescription": zyHwMonitorVoltageDescription,
       "zyHwMonitorVoltageCurrentValue": zyHwMonitorVoltageCurrentValue,
       "zyHwMonitorVoltageMaxValue": zyHwMonitorVoltageMaxValue,
       "zyHwMonitorVoltageMinValue": zyHwMonitorVoltageMinValue,
       "zyHwMonitorVoltageNominalValue": zyHwMonitorVoltageNominalValue,
       "zyHwMonitorVoltageLowThreshold": zyHwMonitorVoltageLowThreshold,
       "zyHwMonitorVoltageStatus": zyHwMonitorVoltageStatus,
       "zyxelHwMonitorPowerSource": zyxelHwMonitorPowerSource,
       "zyHwMonitorPowerSourceMode": zyHwMonitorPowerSourceMode,
       "zyxelHwMonitorPowerSourceTable": zyxelHwMonitorPowerSourceTable,
       "zyxelHwMonitorPowerSourceEntry": zyxelHwMonitorPowerSourceEntry,
       "zyHwMonitorPowerSourceIndex": zyHwMonitorPowerSourceIndex,
       "zyHwMonitorPowerSourceType": zyHwMonitorPowerSourceType,
       "zyHwMonitorPowerSourceStatus": zyHwMonitorPowerSourceStatus,
       "zyxelHwMonitorNotifications": zyxelHwMonitorNotifications,
       "zyHwMonitorFanSpeedOutOfRange": zyHwMonitorFanSpeedOutOfRange,
       "zyHwMonitorTemperatureOutOfRange": zyHwMonitorTemperatureOutOfRange,
       "zyHwMonitorPowerSupplyVoltageOutOfRange": zyHwMonitorPowerSupplyVoltageOutOfRange,
       "zyHwMonitorBackupPowerSupplyInUse": zyHwMonitorBackupPowerSupplyInUse,
       "zyHwMonitorDyingGasp": zyHwMonitorDyingGasp,
       "zyHwMonitorFanAirFlowInconsistency": zyHwMonitorFanAirFlowInconsistency,
       "zyHwMonitorFanSpeedOutOfRangeRecovered": zyHwMonitorFanSpeedOutOfRangeRecovered,
       "zyHwMonitorTemperatureOutOfRangeRecovered": zyHwMonitorTemperatureOutOfRangeRecovered,
       "zyHwMonitorPowerSupplyVoltageOutOfRangeRecovered": zyHwMonitorPowerSupplyVoltageOutOfRangeRecovered}
)
