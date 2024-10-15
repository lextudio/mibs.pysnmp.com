# SNMP MIB module (HH3C-RMON-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-RMON-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:54:45 2024
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

(hh3crmonExtend,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3crmonExtend")

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

hh3cperformance = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4)
)
hh3cperformance.setRevisions(
        ("2003-03-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hh3crmonExtendEventsV2_ObjectIdentity = ObjectIdentity
hh3crmonExtendEventsV2 = _Hh3crmonExtendEventsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 0)
)
if mibBuilder.loadTexts:
    hh3crmonExtendEventsV2.setStatus("current")
_Hh3cprialarmTable_Object = MibTable
hh3cprialarmTable = _Hh3cprialarmTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1)
)
if mibBuilder.loadTexts:
    hh3cprialarmTable.setStatus("current")
_Hh3cprialarmEntry_Object = MibTableRow
hh3cprialarmEntry = _Hh3cprialarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1)
)
hh3cprialarmEntry.setIndexNames(
    (0, "HH3C-RMON-EXT-MIB", "hh3cprialarmIndex"),
)
if mibBuilder.loadTexts:
    hh3cprialarmEntry.setStatus("current")


class _Hh3cprialarmIndex_Type(Integer32):
    """Custom type hh3cprialarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_Hh3cprialarmIndex_Type.__name__ = "Integer32"
_Hh3cprialarmIndex_Object = MibTableColumn
hh3cprialarmIndex = _Hh3cprialarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 1),
    _Hh3cprialarmIndex_Type()
)
hh3cprialarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cprialarmIndex.setStatus("current")
_Hh3cprialarmInterval_Type = Integer32
_Hh3cprialarmInterval_Object = MibTableColumn
hh3cprialarmInterval = _Hh3cprialarmInterval_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 2),
    _Hh3cprialarmInterval_Type()
)
hh3cprialarmInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmInterval.setStatus("current")
_Hh3cprialarmVariable_Type = DisplayString
_Hh3cprialarmVariable_Object = MibTableColumn
hh3cprialarmVariable = _Hh3cprialarmVariable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 3),
    _Hh3cprialarmVariable_Type()
)
hh3cprialarmVariable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmVariable.setStatus("current")
_Hh3cprialarmSympol_Type = DisplayString
_Hh3cprialarmSympol_Object = MibTableColumn
hh3cprialarmSympol = _Hh3cprialarmSympol_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 4),
    _Hh3cprialarmSympol_Type()
)
hh3cprialarmSympol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmSympol.setStatus("current")


class _Hh3cprialarmSampleType_Type(Integer32):
    """Custom type hh3cprialarmSampleType based on Integer32"""
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


_Hh3cprialarmSampleType_Type.__name__ = "Integer32"
_Hh3cprialarmSampleType_Object = MibTableColumn
hh3cprialarmSampleType = _Hh3cprialarmSampleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 5),
    _Hh3cprialarmSampleType_Type()
)
hh3cprialarmSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmSampleType.setStatus("current")
_Hh3cprialarmValue_Type = Integer32
_Hh3cprialarmValue_Object = MibTableColumn
hh3cprialarmValue = _Hh3cprialarmValue_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 6),
    _Hh3cprialarmValue_Type()
)
hh3cprialarmValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cprialarmValue.setStatus("current")


class _Hh3cprialarmStartupAlarm_Type(Integer32):
    """Custom type hh3cprialarmStartupAlarm based on Integer32"""
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


_Hh3cprialarmStartupAlarm_Type.__name__ = "Integer32"
_Hh3cprialarmStartupAlarm_Object = MibTableColumn
hh3cprialarmStartupAlarm = _Hh3cprialarmStartupAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 7),
    _Hh3cprialarmStartupAlarm_Type()
)
hh3cprialarmStartupAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmStartupAlarm.setStatus("current")
_Hh3cprialarmRisingThreshold_Type = Integer32
_Hh3cprialarmRisingThreshold_Object = MibTableColumn
hh3cprialarmRisingThreshold = _Hh3cprialarmRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 8),
    _Hh3cprialarmRisingThreshold_Type()
)
hh3cprialarmRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmRisingThreshold.setStatus("current")
_Hh3cprialarmFallingThreshold_Type = Integer32
_Hh3cprialarmFallingThreshold_Object = MibTableColumn
hh3cprialarmFallingThreshold = _Hh3cprialarmFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 9),
    _Hh3cprialarmFallingThreshold_Type()
)
hh3cprialarmFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmFallingThreshold.setStatus("current")


class _Hh3cprialarmRisingEventIndex_Type(Integer32):
    """Custom type hh3cprialarmRisingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cprialarmRisingEventIndex_Type.__name__ = "Integer32"
_Hh3cprialarmRisingEventIndex_Object = MibTableColumn
hh3cprialarmRisingEventIndex = _Hh3cprialarmRisingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 10),
    _Hh3cprialarmRisingEventIndex_Type()
)
hh3cprialarmRisingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmRisingEventIndex.setStatus("current")


class _Hh3cprialarmFallingEventIndex_Type(Integer32):
    """Custom type hh3cprialarmFallingEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3cprialarmFallingEventIndex_Type.__name__ = "Integer32"
_Hh3cprialarmFallingEventIndex_Object = MibTableColumn
hh3cprialarmFallingEventIndex = _Hh3cprialarmFallingEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 11),
    _Hh3cprialarmFallingEventIndex_Type()
)
hh3cprialarmFallingEventIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmFallingEventIndex.setStatus("current")
_Hh3cprialarmStatCycle_Type = Integer32
_Hh3cprialarmStatCycle_Object = MibTableColumn
hh3cprialarmStatCycle = _Hh3cprialarmStatCycle_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 12),
    _Hh3cprialarmStatCycle_Type()
)
hh3cprialarmStatCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmStatCycle.setStatus("current")


class _Hh3cprialarmStatType_Type(Integer32):
    """Custom type hh3cprialarmStatType based on Integer32"""
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


_Hh3cprialarmStatType_Type.__name__ = "Integer32"
_Hh3cprialarmStatType_Object = MibTableColumn
hh3cprialarmStatType = _Hh3cprialarmStatType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 13),
    _Hh3cprialarmStatType_Type()
)
hh3cprialarmStatType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmStatType.setStatus("current")
_Hh3cprialarmOwner_Type = OwnerString
_Hh3cprialarmOwner_Object = MibTableColumn
hh3cprialarmOwner = _Hh3cprialarmOwner_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 14),
    _Hh3cprialarmOwner_Type()
)
hh3cprialarmOwner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmOwner.setStatus("current")
_Hh3cprialarmStatus_Type = EntryStatus
_Hh3cprialarmStatus_Object = MibTableColumn
hh3cprialarmStatus = _Hh3cprialarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 4, 1, 1, 15),
    _Hh3cprialarmStatus_Type()
)
hh3cprialarmStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cprialarmStatus.setStatus("current")
_Hh3crmonEnableTable_Object = MibTable
hh3crmonEnableTable = _Hh3crmonEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 5)
)
if mibBuilder.loadTexts:
    hh3crmonEnableTable.setStatus("current")
_Hh3crmonEnableEntry_Object = MibTableRow
hh3crmonEnableEntry = _Hh3crmonEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 5, 1)
)
hh3crmonEnableEntry.setIndexNames(
    (0, "HH3C-RMON-EXT-MIB", "hh3crmonEnableIfIndex"),
)
if mibBuilder.loadTexts:
    hh3crmonEnableEntry.setStatus("current")


class _Hh3crmonEnableIfIndex_Type(Integer32):
    """Custom type hh3crmonEnableIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Hh3crmonEnableIfIndex_Type.__name__ = "Integer32"
_Hh3crmonEnableIfIndex_Object = MibTableColumn
hh3crmonEnableIfIndex = _Hh3crmonEnableIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 5, 1, 1),
    _Hh3crmonEnableIfIndex_Type()
)
hh3crmonEnableIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3crmonEnableIfIndex.setStatus("current")


class _Hh3crmonEnableStatus_Type(Integer32):
    """Custom type hh3crmonEnableStatus based on Integer32"""
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


_Hh3crmonEnableStatus_Type.__name__ = "Integer32"
_Hh3crmonEnableStatus_Object = MibTableColumn
hh3crmonEnableStatus = _Hh3crmonEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 5, 1, 2),
    _Hh3crmonEnableStatus_Type()
)
hh3crmonEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3crmonEnableStatus.setStatus("current")
_Hh3cTrapDestTable_Object = MibTable
hh3cTrapDestTable = _Hh3cTrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 6)
)
if mibBuilder.loadTexts:
    hh3cTrapDestTable.setStatus("current")
_Hh3cTrapDestEntry_Object = MibTableRow
hh3cTrapDestEntry = _Hh3cTrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 6, 1)
)
if mibBuilder.loadTexts:
    hh3cTrapDestEntry.setStatus("current")


class _Hh3cTrapDestVersion_Type(Integer32):
    """Custom type hh3cTrapDestVersion based on Integer32"""
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


_Hh3cTrapDestVersion_Type.__name__ = "Integer32"
_Hh3cTrapDestVersion_Object = MibTableColumn
hh3cTrapDestVersion = _Hh3cTrapDestVersion_Object(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 6, 1, 1),
    _Hh3cTrapDestVersion_Type()
)
hh3cTrapDestVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cTrapDestVersion.setStatus("current")
trapDestEntry.registerAugmentions(
    ("HH3C-RMON-EXT-MIB",
     "hh3cTrapDestEntry")
)
hh3cTrapDestEntry.setIndexNames(*trapDestEntry.getIndexNames())

# Managed Objects groups


# Notification objects

hh3cpririsingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 0, 1)
)
hh3cpririsingAlarm.setObjects(
      *(("HH3C-RMON-EXT-MIB", "hh3cprialarmIndex"),
        ("HH3C-RMON-EXT-MIB", "hh3cprialarmSympol"),
        ("HH3C-RMON-EXT-MIB", "hh3cprialarmSampleType"),
        ("HH3C-RMON-EXT-MIB", "hh3cprialarmValue"),
        ("HH3C-RMON-EXT-MIB", "hh3cprialarmRisingThreshold"))
)
if mibBuilder.loadTexts:
    hh3cpririsingAlarm.setStatus(
        "current"
    )

hh3cprifallingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 25506, 8, 4, 0, 2)
)
hh3cprifallingAlarm.setObjects(
      *(("HH3C-RMON-EXT-MIB", "hh3cprialarmIndex"),
        ("HH3C-RMON-EXT-MIB", "hh3cprialarmSympol"),
        ("HH3C-RMON-EXT-MIB", "hh3cprialarmSampleType"),
        ("HH3C-RMON-EXT-MIB", "hh3cprialarmValue"),
        ("HH3C-RMON-EXT-MIB", "hh3cprialarmFallingThreshold"))
)
if mibBuilder.loadTexts:
    hh3cprifallingAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-RMON-EXT-MIB",
    **{"hh3crmonExtendEventsV2": hh3crmonExtendEventsV2,
       "hh3cpririsingAlarm": hh3cpririsingAlarm,
       "hh3cprifallingAlarm": hh3cprifallingAlarm,
       "hh3cperformance": hh3cperformance,
       "hh3cprialarmTable": hh3cprialarmTable,
       "hh3cprialarmEntry": hh3cprialarmEntry,
       "hh3cprialarmIndex": hh3cprialarmIndex,
       "hh3cprialarmInterval": hh3cprialarmInterval,
       "hh3cprialarmVariable": hh3cprialarmVariable,
       "hh3cprialarmSympol": hh3cprialarmSympol,
       "hh3cprialarmSampleType": hh3cprialarmSampleType,
       "hh3cprialarmValue": hh3cprialarmValue,
       "hh3cprialarmStartupAlarm": hh3cprialarmStartupAlarm,
       "hh3cprialarmRisingThreshold": hh3cprialarmRisingThreshold,
       "hh3cprialarmFallingThreshold": hh3cprialarmFallingThreshold,
       "hh3cprialarmRisingEventIndex": hh3cprialarmRisingEventIndex,
       "hh3cprialarmFallingEventIndex": hh3cprialarmFallingEventIndex,
       "hh3cprialarmStatCycle": hh3cprialarmStatCycle,
       "hh3cprialarmStatType": hh3cprialarmStatType,
       "hh3cprialarmOwner": hh3cprialarmOwner,
       "hh3cprialarmStatus": hh3cprialarmStatus,
       "hh3crmonEnableTable": hh3crmonEnableTable,
       "hh3crmonEnableEntry": hh3crmonEnableEntry,
       "hh3crmonEnableIfIndex": hh3crmonEnableIfIndex,
       "hh3crmonEnableStatus": hh3crmonEnableStatus,
       "hh3cTrapDestTable": hh3cTrapDestTable,
       "hh3cTrapDestEntry": hh3cTrapDestEntry,
       "hh3cTrapDestVersion": hh3cTrapDestVersion}
)
