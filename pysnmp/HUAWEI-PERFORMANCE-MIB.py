# SNMP MIB module (HUAWEI-PERFORMANCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-PERFORMANCE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:05:28 2024
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

(hwInternetProtocol,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwInternetProtocol")

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

(EntryStatus,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RmonExtend_ObjectIdentity = ObjectIdentity
rmonExtend = _RmonExtend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4)
)
_RmonExtendEventsV2_ObjectIdentity = ObjectIdentity
rmonExtendEventsV2 = _RmonExtendEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 0)
)
if mibBuilder.loadTexts:
    rmonExtendEventsV2.setStatus("current")
_Performance_ObjectIdentity = ObjectIdentity
performance = _Performance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4)
)
_PrialarmTable_Object = MibTable
prialarmTable = _PrialarmTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1)
)
if mibBuilder.loadTexts:
    prialarmTable.setStatus("mandatory")
_PrialarmEntry_Object = MibTableRow
prialarmEntry = _PrialarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1)
)
prialarmEntry.setIndexNames(
    (0, "HUAWEI-PERFORMANCE-MIB", "prialarmIndex"),
)
if mibBuilder.loadTexts:
    prialarmEntry.setStatus("mandatory")


class _PrialarmIndex_Type(Integer32):
    """Custom type prialarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrialarmIndex_Type.__name__ = "Integer32"
_PrialarmIndex_Object = MibTableColumn
prialarmIndex = _PrialarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 1),
    _PrialarmIndex_Type()
)
prialarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prialarmIndex.setStatus("mandatory")
_PrialarmInterval_Type = Integer32
_PrialarmInterval_Object = MibTableColumn
prialarmInterval = _PrialarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 2),
    _PrialarmInterval_Type()
)
prialarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmInterval.setStatus("mandatory")
_PrialarmVariable_Type = DisplayString
_PrialarmVariable_Object = MibTableColumn
prialarmVariable = _PrialarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 3),
    _PrialarmVariable_Type()
)
prialarmVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmVariable.setStatus("mandatory")
_PrialarmSympol_Type = DisplayString
_PrialarmSympol_Object = MibTableColumn
prialarmSympol = _PrialarmSympol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 4),
    _PrialarmSympol_Type()
)
prialarmSympol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmSympol.setStatus("mandatory")


class _PrialarmSampleType_Type(Integer32):
    """Custom type prialarmSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("absoluteValue", 1),
          ("changeratioValue", 3),
          ("deltaValue", 2))
    )


_PrialarmSampleType_Type.__name__ = "Integer32"
_PrialarmSampleType_Object = MibTableColumn
prialarmSampleType = _PrialarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 5),
    _PrialarmSampleType_Type()
)
prialarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmSampleType.setStatus("mandatory")
_PrialarmValue_Type = Integer32
_PrialarmValue_Object = MibTableColumn
prialarmValue = _PrialarmValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 6),
    _PrialarmValue_Type()
)
prialarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prialarmValue.setStatus("mandatory")


class _PrialarmStartupAlarm_Type(Integer32):
    """Custom type prialarmStartupAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fallingAlarm", 2),
          ("risingAlarm", 1),
          ("risingOrFallingAlarm", 3))
    )


_PrialarmStartupAlarm_Type.__name__ = "Integer32"
_PrialarmStartupAlarm_Object = MibTableColumn
prialarmStartupAlarm = _PrialarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 7),
    _PrialarmStartupAlarm_Type()
)
prialarmStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmStartupAlarm.setStatus("mandatory")
_PrialarmRisingThreshold_Type = Integer32
_PrialarmRisingThreshold_Object = MibTableColumn
prialarmRisingThreshold = _PrialarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 8),
    _PrialarmRisingThreshold_Type()
)
prialarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmRisingThreshold.setStatus("mandatory")
_PrialarmFallingThreshold_Type = Integer32
_PrialarmFallingThreshold_Object = MibTableColumn
prialarmFallingThreshold = _PrialarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 9),
    _PrialarmFallingThreshold_Type()
)
prialarmFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmFallingThreshold.setStatus("mandatory")


class _PrialarmRisingEventIndex_Type(Integer32):
    """Custom type prialarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrialarmRisingEventIndex_Type.__name__ = "Integer32"
_PrialarmRisingEventIndex_Object = MibTableColumn
prialarmRisingEventIndex = _PrialarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 10),
    _PrialarmRisingEventIndex_Type()
)
prialarmRisingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmRisingEventIndex.setStatus("mandatory")


class _PrialarmFallingEventIndex_Type(Integer32):
    """Custom type prialarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PrialarmFallingEventIndex_Type.__name__ = "Integer32"
_PrialarmFallingEventIndex_Object = MibTableColumn
prialarmFallingEventIndex = _PrialarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 11),
    _PrialarmFallingEventIndex_Type()
)
prialarmFallingEventIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmFallingEventIndex.setStatus("mandatory")
_PrialarmStatCycle_Type = Integer32
_PrialarmStatCycle_Object = MibTableColumn
prialarmStatCycle = _PrialarmStatCycle_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 12),
    _PrialarmStatCycle_Type()
)
prialarmStatCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmStatCycle.setStatus("mandatory")


class _PrialarmStatType_Type(Integer32):
    """Custom type prialarmStatType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("during", 2),
          ("forever", 1))
    )


_PrialarmStatType_Type.__name__ = "Integer32"
_PrialarmStatType_Object = MibTableColumn
prialarmStatType = _PrialarmStatType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 13),
    _PrialarmStatType_Type()
)
prialarmStatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmStatType.setStatus("mandatory")
_PrialarmOwner_Type = OwnerString
_PrialarmOwner_Object = MibTableColumn
prialarmOwner = _PrialarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 14),
    _PrialarmOwner_Type()
)
prialarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmOwner.setStatus("mandatory")
_PrialarmStatus_Type = EntryStatus
_PrialarmStatus_Object = MibTableColumn
prialarmStatus = _PrialarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 4, 1, 1, 15),
    _PrialarmStatus_Type()
)
prialarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prialarmStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects

pririsingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 0, 1)
)
pririsingAlarm.setObjects(
      *(("HUAWEI-PERFORMANCE-MIB", "prialarmIndex"),
        ("HUAWEI-PERFORMANCE-MIB", "prialarmSympol"),
        ("HUAWEI-PERFORMANCE-MIB", "prialarmSampleType"),
        ("HUAWEI-PERFORMANCE-MIB", "prialarmValue"),
        ("HUAWEI-PERFORMANCE-MIB", "prialarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    pririsingAlarm.setStatus(
        "current"
    )

prifallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 1, 3, 4, 0, 2)
)
prifallingAlarm.setObjects(
      *(("HUAWEI-PERFORMANCE-MIB", "prialarmIndex"),
        ("HUAWEI-PERFORMANCE-MIB", "prialarmSympol"),
        ("HUAWEI-PERFORMANCE-MIB", "prialarmSampleType"),
        ("HUAWEI-PERFORMANCE-MIB", "prialarmValue"),
        ("HUAWEI-PERFORMANCE-MIB", "prialarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    prifallingAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-PERFORMANCE-MIB",
    **{"rmonExtend": rmonExtend,
       "rmonExtendEventsV2": rmonExtendEventsV2,
       "pririsingAlarm": pririsingAlarm,
       "prifallingAlarm": prifallingAlarm,
       "performance": performance,
       "prialarmTable": prialarmTable,
       "prialarmEntry": prialarmEntry,
       "prialarmIndex": prialarmIndex,
       "prialarmInterval": prialarmInterval,
       "prialarmVariable": prialarmVariable,
       "prialarmSympol": prialarmSympol,
       "prialarmSampleType": prialarmSampleType,
       "prialarmValue": prialarmValue,
       "prialarmStartupAlarm": prialarmStartupAlarm,
       "prialarmRisingThreshold": prialarmRisingThreshold,
       "prialarmFallingThreshold": prialarmFallingThreshold,
       "prialarmRisingEventIndex": prialarmRisingEventIndex,
       "prialarmFallingEventIndex": prialarmFallingEventIndex,
       "prialarmStatCycle": prialarmStatCycle,
       "prialarmStatType": prialarmStatType,
       "prialarmOwner": prialarmOwner,
       "prialarmStatus": prialarmStatus}
)
