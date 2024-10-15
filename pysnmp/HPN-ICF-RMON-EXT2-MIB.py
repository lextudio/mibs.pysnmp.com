# SNMP MIB module (HPN-ICF-RMON-EXT2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-RMON-EXT2-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:43 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

(EntryStatus,
 OwnerString) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus",
    "OwnerString")

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

hpnicfRmonExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125)
)
hpnicfRmonExt.setRevisions(
        ("2012-06-19 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfRmonExtEvent_ObjectIdentity = ObjectIdentity
hpnicfRmonExtEvent = _HpnicfRmonExtEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 0)
)
if mibBuilder.loadTexts:
    hpnicfRmonExtEvent.setStatus("current")
_HpnicfRmonExtAlarmTable_Object = MibTable
hpnicfRmonExtAlarmTable = _HpnicfRmonExtAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1)
)
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmTable.setStatus("current")
_HpnicfRmonExtAlarmEntry_Object = MibTableRow
hpnicfRmonExtAlarmEntry = _HpnicfRmonExtAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1)
)
hpnicfRmonExtAlarmEntry.setIndexNames(
    (0, "HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmIndex"),
)
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmEntry.setStatus("current")


class _HpnicfRmonExtAlarmIndex_Type(Integer32):
    """Custom type hpnicfRmonExtAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfRmonExtAlarmIndex_Type.__name__ = "Integer32"
_HpnicfRmonExtAlarmIndex_Object = MibTableColumn
hpnicfRmonExtAlarmIndex = _HpnicfRmonExtAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 1),
    _HpnicfRmonExtAlarmIndex_Type()
)
hpnicfRmonExtAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmIndex.setStatus("current")


class _HpnicfRmonExtAlarmInterval_Type(Integer32):
    """Custom type hpnicfRmonExtAlarmInterval based on Integer32"""
    defaultValue = 1800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_HpnicfRmonExtAlarmInterval_Type.__name__ = "Integer32"
_HpnicfRmonExtAlarmInterval_Object = MibTableColumn
hpnicfRmonExtAlarmInterval = _HpnicfRmonExtAlarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 2),
    _HpnicfRmonExtAlarmInterval_Type()
)
hpnicfRmonExtAlarmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmInterval.setStatus("current")
_HpnicfRmonExtAlarmVariable_Type = DisplayString
_HpnicfRmonExtAlarmVariable_Object = MibTableColumn
hpnicfRmonExtAlarmVariable = _HpnicfRmonExtAlarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 3),
    _HpnicfRmonExtAlarmVariable_Type()
)
hpnicfRmonExtAlarmVariable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmVariable.setStatus("current")
_HpnicfRmonExtAlarmSympol_Type = DisplayString
_HpnicfRmonExtAlarmSympol_Object = MibTableColumn
hpnicfRmonExtAlarmSympol = _HpnicfRmonExtAlarmSympol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 4),
    _HpnicfRmonExtAlarmSympol_Type()
)
hpnicfRmonExtAlarmSympol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmSympol.setStatus("current")


class _HpnicfRmonExtAlarmSampleType_Type(Integer32):
    """Custom type hpnicfRmonExtAlarmSampleType based on Integer32"""
    defaultValue = 1

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
          ("deltaValue", 2),
          ("speedValue", 3))
    )


_HpnicfRmonExtAlarmSampleType_Type.__name__ = "Integer32"
_HpnicfRmonExtAlarmSampleType_Object = MibTableColumn
hpnicfRmonExtAlarmSampleType = _HpnicfRmonExtAlarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 5),
    _HpnicfRmonExtAlarmSampleType_Type()
)
hpnicfRmonExtAlarmSampleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmSampleType.setStatus("current")
_HpnicfRmonExtAlarmValue_Type = Integer32
_HpnicfRmonExtAlarmValue_Object = MibTableColumn
hpnicfRmonExtAlarmValue = _HpnicfRmonExtAlarmValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 6),
    _HpnicfRmonExtAlarmValue_Type()
)
hpnicfRmonExtAlarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmValue.setStatus("current")


class _HpnicfRmonExtAlarmStartupAlarm_Type(Integer32):
    """Custom type hpnicfRmonExtAlarmStartupAlarm based on Integer32"""
    defaultValue = 3

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


_HpnicfRmonExtAlarmStartupAlarm_Type.__name__ = "Integer32"
_HpnicfRmonExtAlarmStartupAlarm_Object = MibTableColumn
hpnicfRmonExtAlarmStartupAlarm = _HpnicfRmonExtAlarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 7),
    _HpnicfRmonExtAlarmStartupAlarm_Type()
)
hpnicfRmonExtAlarmStartupAlarm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmStartupAlarm.setStatus("current")


class _HpnicfRmonExtAlarmRisingThreshold_Type(Integer32):
    """Custom type hpnicfRmonExtAlarmRisingThreshold based on Integer32"""
    defaultValue = 1


_HpnicfRmonExtAlarmRisingThreshold_Object = MibTableColumn
hpnicfRmonExtAlarmRisingThreshold = _HpnicfRmonExtAlarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 8),
    _HpnicfRmonExtAlarmRisingThreshold_Type()
)
hpnicfRmonExtAlarmRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmRisingThreshold.setStatus("current")


class _HpnicfRmonExtAlarmFallingThreshold_Type(Integer32):
    """Custom type hpnicfRmonExtAlarmFallingThreshold based on Integer32"""
    defaultValue = 0


_HpnicfRmonExtAlarmFallingThreshold_Object = MibTableColumn
hpnicfRmonExtAlarmFallingThreshold = _HpnicfRmonExtAlarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 9),
    _HpnicfRmonExtAlarmFallingThreshold_Type()
)
hpnicfRmonExtAlarmFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmFallingThreshold.setStatus("current")


class _HpnicfRmonExtAlarmRisingEvtIndex_Type(Integer32):
    """Custom type hpnicfRmonExtAlarmRisingEvtIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRmonExtAlarmRisingEvtIndex_Type.__name__ = "Integer32"
_HpnicfRmonExtAlarmRisingEvtIndex_Object = MibTableColumn
hpnicfRmonExtAlarmRisingEvtIndex = _HpnicfRmonExtAlarmRisingEvtIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 10),
    _HpnicfRmonExtAlarmRisingEvtIndex_Type()
)
hpnicfRmonExtAlarmRisingEvtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmRisingEvtIndex.setStatus("current")


class _HpnicfRmonExtAlarmFallingEvtIndex_Type(Integer32):
    """Custom type hpnicfRmonExtAlarmFallingEvtIndex based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfRmonExtAlarmFallingEvtIndex_Type.__name__ = "Integer32"
_HpnicfRmonExtAlarmFallingEvtIndex_Object = MibTableColumn
hpnicfRmonExtAlarmFallingEvtIndex = _HpnicfRmonExtAlarmFallingEvtIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 11),
    _HpnicfRmonExtAlarmFallingEvtIndex_Type()
)
hpnicfRmonExtAlarmFallingEvtIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmFallingEvtIndex.setStatus("current")


class _HpnicfRmonExtAlarmStatCycle_Type(Integer32):
    """Custom type hpnicfRmonExtAlarmStatCycle based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967),
    )


_HpnicfRmonExtAlarmStatCycle_Type.__name__ = "Integer32"
_HpnicfRmonExtAlarmStatCycle_Object = MibTableColumn
hpnicfRmonExtAlarmStatCycle = _HpnicfRmonExtAlarmStatCycle_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 12),
    _HpnicfRmonExtAlarmStatCycle_Type()
)
hpnicfRmonExtAlarmStatCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmStatCycle.setStatus("current")


class _HpnicfRmonExtAlarmStatType_Type(Integer32):
    """Custom type hpnicfRmonExtAlarmStatType based on Integer32"""
    defaultValue = 1

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


_HpnicfRmonExtAlarmStatType_Type.__name__ = "Integer32"
_HpnicfRmonExtAlarmStatType_Object = MibTableColumn
hpnicfRmonExtAlarmStatType = _HpnicfRmonExtAlarmStatType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 13),
    _HpnicfRmonExtAlarmStatType_Type()
)
hpnicfRmonExtAlarmStatType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmStatType.setStatus("current")
_HpnicfRmonExtAlarmOwner_Type = OwnerString
_HpnicfRmonExtAlarmOwner_Object = MibTableColumn
hpnicfRmonExtAlarmOwner = _HpnicfRmonExtAlarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 14),
    _HpnicfRmonExtAlarmOwner_Type()
)
hpnicfRmonExtAlarmOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmOwner.setStatus("current")
_HpnicfRmonExtAlarmStatus_Type = EntryStatus
_HpnicfRmonExtAlarmStatus_Object = MibTableColumn
hpnicfRmonExtAlarmStatus = _HpnicfRmonExtAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 1, 1, 15),
    _HpnicfRmonExtAlarmStatus_Type()
)
hpnicfRmonExtAlarmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfRmonExtAlarmStatus.setStatus("current")

# Managed Objects groups


# Notification objects

hpnicfRmonExtRisingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 0, 1)
)
hpnicfRmonExtRisingAlarm.setObjects(
      *(("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmIndex"),
        ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmSympol"),
        ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmSampleType"),
        ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmValue"),
        ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfRmonExtRisingAlarm.setStatus(
        "current"
    )

hpnicfRmonExtFallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 125, 0, 2)
)
hpnicfRmonExtFallingAlarm.setObjects(
      *(("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmIndex"),
        ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmSympol"),
        ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmSampleType"),
        ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmValue"),
        ("HPN-ICF-RMON-EXT2-MIB", "hpnicfRmonExtAlarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfRmonExtFallingAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-RMON-EXT2-MIB",
    **{"hpnicfRmonExt": hpnicfRmonExt,
       "hpnicfRmonExtEvent": hpnicfRmonExtEvent,
       "hpnicfRmonExtRisingAlarm": hpnicfRmonExtRisingAlarm,
       "hpnicfRmonExtFallingAlarm": hpnicfRmonExtFallingAlarm,
       "hpnicfRmonExtAlarmTable": hpnicfRmonExtAlarmTable,
       "hpnicfRmonExtAlarmEntry": hpnicfRmonExtAlarmEntry,
       "hpnicfRmonExtAlarmIndex": hpnicfRmonExtAlarmIndex,
       "hpnicfRmonExtAlarmInterval": hpnicfRmonExtAlarmInterval,
       "hpnicfRmonExtAlarmVariable": hpnicfRmonExtAlarmVariable,
       "hpnicfRmonExtAlarmSympol": hpnicfRmonExtAlarmSympol,
       "hpnicfRmonExtAlarmSampleType": hpnicfRmonExtAlarmSampleType,
       "hpnicfRmonExtAlarmValue": hpnicfRmonExtAlarmValue,
       "hpnicfRmonExtAlarmStartupAlarm": hpnicfRmonExtAlarmStartupAlarm,
       "hpnicfRmonExtAlarmRisingThreshold": hpnicfRmonExtAlarmRisingThreshold,
       "hpnicfRmonExtAlarmFallingThreshold": hpnicfRmonExtAlarmFallingThreshold,
       "hpnicfRmonExtAlarmRisingEvtIndex": hpnicfRmonExtAlarmRisingEvtIndex,
       "hpnicfRmonExtAlarmFallingEvtIndex": hpnicfRmonExtAlarmFallingEvtIndex,
       "hpnicfRmonExtAlarmStatCycle": hpnicfRmonExtAlarmStatCycle,
       "hpnicfRmonExtAlarmStatType": hpnicfRmonExtAlarmStatType,
       "hpnicfRmonExtAlarmOwner": hpnicfRmonExtAlarmOwner,
       "hpnicfRmonExtAlarmStatus": hpnicfRmonExtAlarmStatus}
)
