# SNMP MIB module (HPN-ICF-RMON-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-RMON-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:01:42 2024
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

(hpnicfrmonExtend,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfrmonExtend")

(OwnerString,) = mibBuilder.importSymbols(
    "IF-MIB",
    "OwnerString")

(EntryStatus,) = mibBuilder.importSymbols(
    "RMON-MIB",
    "EntryStatus")

(trapDestEntry,
 trapDestIndex) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "trapDestEntry",
    "trapDestIndex")

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

hpnicfperformance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4)
)
hpnicfperformance.setRevisions(
        ("2003-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpnicfrmonExtendEventsV2_ObjectIdentity = ObjectIdentity
hpnicfrmonExtendEventsV2 = _HpnicfrmonExtendEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 0)
)
if mibBuilder.loadTexts:
    hpnicfrmonExtendEventsV2.setStatus("current")
_HpnicfprialarmTable_Object = MibTable
hpnicfprialarmTable = _HpnicfprialarmTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1)
)
if mibBuilder.loadTexts:
    hpnicfprialarmTable.setStatus("current")
_HpnicfprialarmEntry_Object = MibTableRow
hpnicfprialarmEntry = _HpnicfprialarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1)
)
hpnicfprialarmEntry.setIndexNames(
    (0, "HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmIndex"),
)
if mibBuilder.loadTexts:
    hpnicfprialarmEntry.setStatus("current")


class _HpnicfprialarmIndex_Type(Integer32):
    """Custom type hpnicfprialarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpnicfprialarmIndex_Type.__name__ = "Integer32"
_HpnicfprialarmIndex_Object = MibTableColumn
hpnicfprialarmIndex = _HpnicfprialarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 1),
    _HpnicfprialarmIndex_Type()
)
hpnicfprialarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfprialarmIndex.setStatus("current")
_HpnicfprialarmInterval_Type = Integer32
_HpnicfprialarmInterval_Object = MibTableColumn
hpnicfprialarmInterval = _HpnicfprialarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 2),
    _HpnicfprialarmInterval_Type()
)
hpnicfprialarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmInterval.setStatus("current")
_HpnicfprialarmVariable_Type = DisplayString
_HpnicfprialarmVariable_Object = MibTableColumn
hpnicfprialarmVariable = _HpnicfprialarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 3),
    _HpnicfprialarmVariable_Type()
)
hpnicfprialarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmVariable.setStatus("current")
_HpnicfprialarmSympol_Type = DisplayString
_HpnicfprialarmSympol_Object = MibTableColumn
hpnicfprialarmSympol = _HpnicfprialarmSympol_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 4),
    _HpnicfprialarmSympol_Type()
)
hpnicfprialarmSympol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmSympol.setStatus("current")


class _HpnicfprialarmSampleType_Type(Integer32):
    """Custom type hpnicfprialarmSampleType based on Integer32"""
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


_HpnicfprialarmSampleType_Type.__name__ = "Integer32"
_HpnicfprialarmSampleType_Object = MibTableColumn
hpnicfprialarmSampleType = _HpnicfprialarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 5),
    _HpnicfprialarmSampleType_Type()
)
hpnicfprialarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmSampleType.setStatus("current")
_HpnicfprialarmValue_Type = Integer32
_HpnicfprialarmValue_Object = MibTableColumn
hpnicfprialarmValue = _HpnicfprialarmValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 6),
    _HpnicfprialarmValue_Type()
)
hpnicfprialarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfprialarmValue.setStatus("current")


class _HpnicfprialarmStartupAlarm_Type(Integer32):
    """Custom type hpnicfprialarmStartupAlarm based on Integer32"""
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


_HpnicfprialarmStartupAlarm_Type.__name__ = "Integer32"
_HpnicfprialarmStartupAlarm_Object = MibTableColumn
hpnicfprialarmStartupAlarm = _HpnicfprialarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 7),
    _HpnicfprialarmStartupAlarm_Type()
)
hpnicfprialarmStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmStartupAlarm.setStatus("current")
_HpnicfprialarmRisingThreshold_Type = Integer32
_HpnicfprialarmRisingThreshold_Object = MibTableColumn
hpnicfprialarmRisingThreshold = _HpnicfprialarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 8),
    _HpnicfprialarmRisingThreshold_Type()
)
hpnicfprialarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmRisingThreshold.setStatus("current")
_HpnicfprialarmFallingThreshold_Type = Integer32
_HpnicfprialarmFallingThreshold_Object = MibTableColumn
hpnicfprialarmFallingThreshold = _HpnicfprialarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 9),
    _HpnicfprialarmFallingThreshold_Type()
)
hpnicfprialarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmFallingThreshold.setStatus("current")


class _HpnicfprialarmRisingEventIndex_Type(Integer32):
    """Custom type hpnicfprialarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfprialarmRisingEventIndex_Type.__name__ = "Integer32"
_HpnicfprialarmRisingEventIndex_Object = MibTableColumn
hpnicfprialarmRisingEventIndex = _HpnicfprialarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 10),
    _HpnicfprialarmRisingEventIndex_Type()
)
hpnicfprialarmRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmRisingEventIndex.setStatus("current")


class _HpnicfprialarmFallingEventIndex_Type(Integer32):
    """Custom type hpnicfprialarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfprialarmFallingEventIndex_Type.__name__ = "Integer32"
_HpnicfprialarmFallingEventIndex_Object = MibTableColumn
hpnicfprialarmFallingEventIndex = _HpnicfprialarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 11),
    _HpnicfprialarmFallingEventIndex_Type()
)
hpnicfprialarmFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmFallingEventIndex.setStatus("current")
_HpnicfprialarmStatCycle_Type = Integer32
_HpnicfprialarmStatCycle_Object = MibTableColumn
hpnicfprialarmStatCycle = _HpnicfprialarmStatCycle_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 12),
    _HpnicfprialarmStatCycle_Type()
)
hpnicfprialarmStatCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmStatCycle.setStatus("current")


class _HpnicfprialarmStatType_Type(Integer32):
    """Custom type hpnicfprialarmStatType based on Integer32"""
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


_HpnicfprialarmStatType_Type.__name__ = "Integer32"
_HpnicfprialarmStatType_Object = MibTableColumn
hpnicfprialarmStatType = _HpnicfprialarmStatType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 13),
    _HpnicfprialarmStatType_Type()
)
hpnicfprialarmStatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmStatType.setStatus("current")
_HpnicfprialarmOwner_Type = OwnerString
_HpnicfprialarmOwner_Object = MibTableColumn
hpnicfprialarmOwner = _HpnicfprialarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 14),
    _HpnicfprialarmOwner_Type()
)
hpnicfprialarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmOwner.setStatus("current")
_HpnicfprialarmStatus_Type = EntryStatus
_HpnicfprialarmStatus_Object = MibTableColumn
hpnicfprialarmStatus = _HpnicfprialarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 4, 1, 1, 15),
    _HpnicfprialarmStatus_Type()
)
hpnicfprialarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfprialarmStatus.setStatus("current")
_HpnicfrmonEnableTable_Object = MibTable
hpnicfrmonEnableTable = _HpnicfrmonEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 5)
)
if mibBuilder.loadTexts:
    hpnicfrmonEnableTable.setStatus("current")
_HpnicfrmonEnableEntry_Object = MibTableRow
hpnicfrmonEnableEntry = _HpnicfrmonEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 5, 1)
)
hpnicfrmonEnableEntry.setIndexNames(
    (0, "HPN-ICF-RMON-EXT-MIB", "hpnicfrmonEnableIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfrmonEnableEntry.setStatus("current")


class _HpnicfrmonEnableIfIndex_Type(Integer32):
    """Custom type hpnicfrmonEnableIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HpnicfrmonEnableIfIndex_Type.__name__ = "Integer32"
_HpnicfrmonEnableIfIndex_Object = MibTableColumn
hpnicfrmonEnableIfIndex = _HpnicfrmonEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 5, 1, 1),
    _HpnicfrmonEnableIfIndex_Type()
)
hpnicfrmonEnableIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfrmonEnableIfIndex.setStatus("current")


class _HpnicfrmonEnableStatus_Type(Integer32):
    """Custom type hpnicfrmonEnableStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_HpnicfrmonEnableStatus_Type.__name__ = "Integer32"
_HpnicfrmonEnableStatus_Object = MibTableColumn
hpnicfrmonEnableStatus = _HpnicfrmonEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 5, 1, 2),
    _HpnicfrmonEnableStatus_Type()
)
hpnicfrmonEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfrmonEnableStatus.setStatus("current")
_HpnicfTrapDestTable_Object = MibTable
hpnicfTrapDestTable = _HpnicfTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 6)
)
if mibBuilder.loadTexts:
    hpnicfTrapDestTable.setStatus("current")
_HpnicfTrapDestEntry_Object = MibTableRow
hpnicfTrapDestEntry = _HpnicfTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 6, 1)
)
if mibBuilder.loadTexts:
    hpnicfTrapDestEntry.setStatus("current")


class _HpnicfTrapDestVersion_Type(Integer32):
    """Custom type hpnicfTrapDestVersion based on Integer32"""
    defaultValue = 1

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
        *(("snmpv1", 1),
          ("snmpv2", 2),
          ("snmpv3andauthen", 3),
          ("snmpv3andnoauthen", 4),
          ("snmpv3andpriv", 5))
    )


_HpnicfTrapDestVersion_Type.__name__ = "Integer32"
_HpnicfTrapDestVersion_Object = MibTableColumn
hpnicfTrapDestVersion = _HpnicfTrapDestVersion_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 6, 1, 1),
    _HpnicfTrapDestVersion_Type()
)
hpnicfTrapDestVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfTrapDestVersion.setStatus("current")
trapDestEntry.registerAugmentions(
    ("HPN-ICF-RMON-EXT-MIB",
     "hpnicfTrapDestEntry")
)
hpnicfTrapDestEntry.setIndexNames(*trapDestEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hpnicfpririsingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 0, 1)
)
hpnicfpririsingAlarm.setObjects(
      *(("HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmIndex"),
        ("HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmSympol"),
        ("HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmSampleType"),
        ("HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmValue"),
        ("HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfpririsingAlarm.setStatus(
        "current"
    )

hpnicfprifallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 8, 4, 0, 2)
)
hpnicfprifallingAlarm.setObjects(
      *(("HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmIndex"),
        ("HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmSympol"),
        ("HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmSampleType"),
        ("HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmValue"),
        ("HPN-ICF-RMON-EXT-MIB", "hpnicfprialarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    hpnicfprifallingAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-RMON-EXT-MIB",
    **{"hpnicfrmonExtendEventsV2": hpnicfrmonExtendEventsV2,
       "hpnicfpririsingAlarm": hpnicfpririsingAlarm,
       "hpnicfprifallingAlarm": hpnicfprifallingAlarm,
       "hpnicfperformance": hpnicfperformance,
       "hpnicfprialarmTable": hpnicfprialarmTable,
       "hpnicfprialarmEntry": hpnicfprialarmEntry,
       "hpnicfprialarmIndex": hpnicfprialarmIndex,
       "hpnicfprialarmInterval": hpnicfprialarmInterval,
       "hpnicfprialarmVariable": hpnicfprialarmVariable,
       "hpnicfprialarmSympol": hpnicfprialarmSympol,
       "hpnicfprialarmSampleType": hpnicfprialarmSampleType,
       "hpnicfprialarmValue": hpnicfprialarmValue,
       "hpnicfprialarmStartupAlarm": hpnicfprialarmStartupAlarm,
       "hpnicfprialarmRisingThreshold": hpnicfprialarmRisingThreshold,
       "hpnicfprialarmFallingThreshold": hpnicfprialarmFallingThreshold,
       "hpnicfprialarmRisingEventIndex": hpnicfprialarmRisingEventIndex,
       "hpnicfprialarmFallingEventIndex": hpnicfprialarmFallingEventIndex,
       "hpnicfprialarmStatCycle": hpnicfprialarmStatCycle,
       "hpnicfprialarmStatType": hpnicfprialarmStatType,
       "hpnicfprialarmOwner": hpnicfprialarmOwner,
       "hpnicfprialarmStatus": hpnicfprialarmStatus,
       "hpnicfrmonEnableTable": hpnicfrmonEnableTable,
       "hpnicfrmonEnableEntry": hpnicfrmonEnableEntry,
       "hpnicfrmonEnableIfIndex": hpnicfrmonEnableIfIndex,
       "hpnicfrmonEnableStatus": hpnicfrmonEnableStatus,
       "hpnicfTrapDestTable": hpnicfTrapDestTable,
       "hpnicfTrapDestEntry": hpnicfTrapDestEntry,
       "hpnicfTrapDestVersion": hpnicfTrapDestVersion}
)
