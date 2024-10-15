# SNMP MIB module (SITEBOSS-350-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SITEBOSS-350-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:28 2024
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

(asentria,) = mibBuilder.importSymbols(
    "ASENTRIA-ROOT-MIB",
    "asentria")

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

s350 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18)
)
s350.setRevisions(
        ("2014-12-11 04:11",
         "2014-10-16 04:10",
         "2014-10-03 04:09",
         "2014-08-14 04:08",
         "2014-07-03 04:07",
         "2014-06-24 04:06",
         "2014-06-17 04:05",
         "2014-04-11 04:04",
         "2014-01-17 04:03",
         "2013-12-04 04:02",
         "2013-10-16 04:01",
         "2013-08-19 04:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S350Notifications_ObjectIdentity = ObjectIdentity
s350Notifications = _S350Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1)
)
_EventSensorStatus_ObjectIdentity = ObjectIdentity
eventSensorStatus = _EventSensorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1)
)
_EsPointTable_Object = MibTable
esPointTable = _EsPointTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    esPointTable.setStatus("current")
_EsPointEntry_Object = MibTableRow
esPointEntry = _EsPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1)
)
esPointEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "esIndexES"),
    (0, "SITEBOSS-350-STD-MIB", "esIndexPC"),
    (0, "SITEBOSS-350-STD-MIB", "esIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointEntry.setStatus("current")


class _EsIndexES_Type(Integer32):
    """Custom type esIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EsIndexES_Type.__name__ = "Integer32"
_EsIndexES_Object = MibTableColumn
esIndexES = _EsIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1, 1),
    _EsIndexES_Type()
)
esIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexES.setStatus("current")


class _EsIndexPC_Type(Integer32):
    """Custom type esIndexPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_EsIndexPC_Type.__name__ = "Integer32"
_EsIndexPC_Object = MibTableColumn
esIndexPC = _EsIndexPC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1, 2),
    _EsIndexPC_Type()
)
esIndexPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPC.setStatus("current")


class _EsIndexPoint_Type(Integer32):
    """Custom type esIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EsIndexPoint_Type.__name__ = "Integer32"
_EsIndexPoint_Object = MibTableColumn
esIndexPoint = _EsIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1, 3),
    _EsIndexPoint_Type()
)
esIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPoint.setStatus("current")
_EsPointName_Type = DisplayString
_EsPointName_Object = MibTableColumn
esPointName = _EsPointName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1, 4),
    _EsPointName_Type()
)
esPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointName.setStatus("current")
_EsPointInEventState_Type = Integer32
_EsPointInEventState_Object = MibTableColumn
esPointInEventState = _EsPointInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1, 5),
    _EsPointInEventState_Type()
)
esPointInEventState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointInEventState.setStatus("current")


class _EsPointValueInt_Type(Integer32):
    """Custom type esPointValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_EsPointValueInt_Type.__name__ = "Integer32"
_EsPointValueInt_Object = MibTableColumn
esPointValueInt = _EsPointValueInt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1, 6),
    _EsPointValueInt_Type()
)
esPointValueInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointValueInt.setStatus("current")
_EsPointValueStr_Type = DisplayString
_EsPointValueStr_Object = MibTableColumn
esPointValueStr = _EsPointValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1, 7),
    _EsPointValueStr_Type()
)
esPointValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointValueStr.setStatus("current")
_EsPointTimeLastChange_Type = DisplayString
_EsPointTimeLastChange_Object = MibTableColumn
esPointTimeLastChange = _EsPointTimeLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1, 8),
    _EsPointTimeLastChange_Type()
)
esPointTimeLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointTimeLastChange.setStatus("current")
_EsPointTimetickLastChange_Type = TimeTicks
_EsPointTimetickLastChange_Object = MibTableColumn
esPointTimetickLastChange = _EsPointTimetickLastChange_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1, 9),
    _EsPointTimetickLastChange_Type()
)
esPointTimetickLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointTimetickLastChange.setStatus("current")
_EsPointAliasValueStr_Type = DisplayString
_EsPointAliasValueStr_Object = MibTableColumn
esPointAliasValueStr = _EsPointAliasValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 1, 1, 1, 10),
    _EsPointAliasValueStr_Type()
)
esPointAliasValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointAliasValueStr.setStatus("current")
_DataEventStatus_ObjectIdentity = ObjectIdentity
dataEventStatus = _DataEventStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 2)
)
_DeStatusTable_Object = MibTable
deStatusTable = _DeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 2, 1)
)
if mibBuilder.loadTexts:
    deStatusTable.setStatus("current")
_DeStatusEntry_Object = MibTableRow
deStatusEntry = _DeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 2, 1, 1)
)
deStatusEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "deStatusIndex"),
)
if mibBuilder.loadTexts:
    deStatusEntry.setStatus("current")


class _DeStatusIndex_Type(Integer32):
    """Custom type deStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_DeStatusIndex_Type.__name__ = "Integer32"
_DeStatusIndex_Object = MibTableColumn
deStatusIndex = _DeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 2, 1, 1, 1),
    _DeStatusIndex_Type()
)
deStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusIndex.setStatus("current")
_DeStatusName_Type = DisplayString
_DeStatusName_Object = MibTableColumn
deStatusName = _DeStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 2, 1, 1, 2),
    _DeStatusName_Type()
)
deStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusName.setStatus("current")
_DeStatusCounter_Type = Integer32
_DeStatusCounter_Object = MibTableColumn
deStatusCounter = _DeStatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 2, 1, 1, 3),
    _DeStatusCounter_Type()
)
deStatusCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusCounter.setStatus("current")
_DeStatusThreshold_Type = Integer32
_DeStatusThreshold_Object = MibTableColumn
deStatusThreshold = _DeStatusThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 2, 1, 1, 4),
    _DeStatusThreshold_Type()
)
deStatusThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deStatusThreshold.setStatus("current")
_PowerDistributionStatus_ObjectIdentity = ObjectIdentity
powerDistributionStatus = _PowerDistributionStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5)
)
_PdConfig_Type = DisplayString
_PdConfig_Object = MibScalar
pdConfig = _PdConfig_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 1),
    _PdConfig_Type()
)
pdConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdConfig.setStatus("current")
_PdNextGen_ObjectIdentity = ObjectIdentity
pdNextGen = _PdNextGen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4)
)
_PdnTable_Object = MibTable
pdnTable = _PdnTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1)
)
if mibBuilder.loadTexts:
    pdnTable.setStatus("current")
_PdnEntry_Object = MibTableRow
pdnEntry = _PdnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1)
)
pdnEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "pdnIndexPD"),
    (0, "SITEBOSS-350-STD-MIB", "pdnIndexOutput"),
)
if mibBuilder.loadTexts:
    pdnEntry.setStatus("current")


class _PdnIndexPD_Type(Integer32):
    """Custom type pdnIndexPD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_PdnIndexPD_Type.__name__ = "Integer32"
_PdnIndexPD_Object = MibTableColumn
pdnIndexPD = _PdnIndexPD_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 1),
    _PdnIndexPD_Type()
)
pdnIndexPD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIndexPD.setStatus("current")


class _PdnIndexOutput_Type(Integer32):
    """Custom type pdnIndexOutput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_PdnIndexOutput_Type.__name__ = "Integer32"
_PdnIndexOutput_Object = MibTableColumn
pdnIndexOutput = _PdnIndexOutput_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 2),
    _PdnIndexOutput_Type()
)
pdnIndexOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIndexOutput.setStatus("current")
_PdnConfig_Type = DisplayString
_PdnConfig_Object = MibTableColumn
pdnConfig = _PdnConfig_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 3),
    _PdnConfig_Type()
)
pdnConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnConfig.setStatus("current")
_PdnMainCurrentInEventState_Type = DisplayString
_PdnMainCurrentInEventState_Object = MibTableColumn
pdnMainCurrentInEventState = _PdnMainCurrentInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 4),
    _PdnMainCurrentInEventState_Type()
)
pdnMainCurrentInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainCurrentInEventState.setStatus("current")
_PdnMainCurrentValue_Type = Integer32
_PdnMainCurrentValue_Object = MibTableColumn
pdnMainCurrentValue = _PdnMainCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 5),
    _PdnMainCurrentValue_Type()
)
pdnMainCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainCurrentValue.setStatus("current")
_PdnMainCurrentValueStr_Type = DisplayString
_PdnMainCurrentValueStr_Object = MibTableColumn
pdnMainCurrentValueStr = _PdnMainCurrentValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 6),
    _PdnMainCurrentValueStr_Type()
)
pdnMainCurrentValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainCurrentValueStr.setStatus("current")
_PdnMainCurrentDeadband_Type = Integer32
_PdnMainCurrentDeadband_Object = MibTableColumn
pdnMainCurrentDeadband = _PdnMainCurrentDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 7),
    _PdnMainCurrentDeadband_Type()
)
pdnMainCurrentDeadband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainCurrentDeadband.setStatus("current")
_PdnMainCurrentVHighCurrent_Type = Integer32
_PdnMainCurrentVHighCurrent_Object = MibTableColumn
pdnMainCurrentVHighCurrent = _PdnMainCurrentVHighCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 8),
    _PdnMainCurrentVHighCurrent_Type()
)
pdnMainCurrentVHighCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainCurrentVHighCurrent.setStatus("current")
_PdnMainCurrentHighCurrent_Type = Integer32
_PdnMainCurrentHighCurrent_Object = MibTableColumn
pdnMainCurrentHighCurrent = _PdnMainCurrentHighCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 9),
    _PdnMainCurrentHighCurrent_Type()
)
pdnMainCurrentHighCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainCurrentHighCurrent.setStatus("current")
_PdnMainCurrentLowCurrent_Type = Integer32
_PdnMainCurrentLowCurrent_Object = MibTableColumn
pdnMainCurrentLowCurrent = _PdnMainCurrentLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 10),
    _PdnMainCurrentLowCurrent_Type()
)
pdnMainCurrentLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainCurrentLowCurrent.setStatus("current")
_PdnMainCurrentVLowCurrent_Type = Integer32
_PdnMainCurrentVLowCurrent_Object = MibTableColumn
pdnMainCurrentVLowCurrent = _PdnMainCurrentVLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 11),
    _PdnMainCurrentVLowCurrent_Type()
)
pdnMainCurrentVLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainCurrentVLowCurrent.setStatus("current")
_PdnMainVoltageInEventState_Type = DisplayString
_PdnMainVoltageInEventState_Object = MibTableColumn
pdnMainVoltageInEventState = _PdnMainVoltageInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 12),
    _PdnMainVoltageInEventState_Type()
)
pdnMainVoltageInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainVoltageInEventState.setStatus("current")
_PdnMainVoltageValue_Type = Integer32
_PdnMainVoltageValue_Object = MibTableColumn
pdnMainVoltageValue = _PdnMainVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 13),
    _PdnMainVoltageValue_Type()
)
pdnMainVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainVoltageValue.setStatus("current")
_PdnMainVoltageValueStr_Type = DisplayString
_PdnMainVoltageValueStr_Object = MibTableColumn
pdnMainVoltageValueStr = _PdnMainVoltageValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 14),
    _PdnMainVoltageValueStr_Type()
)
pdnMainVoltageValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainVoltageValueStr.setStatus("current")
_PdnMainVoltageDeadband_Type = Integer32
_PdnMainVoltageDeadband_Object = MibTableColumn
pdnMainVoltageDeadband = _PdnMainVoltageDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 15),
    _PdnMainVoltageDeadband_Type()
)
pdnMainVoltageDeadband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainVoltageDeadband.setStatus("current")
_PdnMainVoltageVHighVoltage_Type = Integer32
_PdnMainVoltageVHighVoltage_Object = MibTableColumn
pdnMainVoltageVHighVoltage = _PdnMainVoltageVHighVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 16),
    _PdnMainVoltageVHighVoltage_Type()
)
pdnMainVoltageVHighVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainVoltageVHighVoltage.setStatus("current")
_PdnMainVoltageHighVoltage_Type = Integer32
_PdnMainVoltageHighVoltage_Object = MibTableColumn
pdnMainVoltageHighVoltage = _PdnMainVoltageHighVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 17),
    _PdnMainVoltageHighVoltage_Type()
)
pdnMainVoltageHighVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainVoltageHighVoltage.setStatus("current")
_PdnMainVoltageLowVoltage_Type = Integer32
_PdnMainVoltageLowVoltage_Object = MibTableColumn
pdnMainVoltageLowVoltage = _PdnMainVoltageLowVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 18),
    _PdnMainVoltageLowVoltage_Type()
)
pdnMainVoltageLowVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainVoltageLowVoltage.setStatus("current")
_PdnMainVoltageVLowVoltage_Type = Integer32
_PdnMainVoltageVLowVoltage_Object = MibTableColumn
pdnMainVoltageVLowVoltage = _PdnMainVoltageVLowVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 19),
    _PdnMainVoltageVLowVoltage_Type()
)
pdnMainVoltageVLowVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainVoltageVLowVoltage.setStatus("current")
_PdnMainPowerValue_Type = Integer32
_PdnMainPowerValue_Object = MibTableColumn
pdnMainPowerValue = _PdnMainPowerValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 20),
    _PdnMainPowerValue_Type()
)
pdnMainPowerValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainPowerValue.setStatus("current")
_PdnMainPowerValueStr_Type = DisplayString
_PdnMainPowerValueStr_Object = MibTableColumn
pdnMainPowerValueStr = _PdnMainPowerValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 21),
    _PdnMainPowerValueStr_Type()
)
pdnMainPowerValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainPowerValueStr.setStatus("current")
_PdnOutputCurrentInEventState_Type = DisplayString
_PdnOutputCurrentInEventState_Object = MibTableColumn
pdnOutputCurrentInEventState = _PdnOutputCurrentInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 22),
    _PdnOutputCurrentInEventState_Type()
)
pdnOutputCurrentInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputCurrentInEventState.setStatus("current")
_PdnOutputCurrentValue_Type = Integer32
_PdnOutputCurrentValue_Object = MibTableColumn
pdnOutputCurrentValue = _PdnOutputCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 23),
    _PdnOutputCurrentValue_Type()
)
pdnOutputCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputCurrentValue.setStatus("current")
_PdnOutputCurrentValueStr_Type = DisplayString
_PdnOutputCurrentValueStr_Object = MibTableColumn
pdnOutputCurrentValueStr = _PdnOutputCurrentValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 24),
    _PdnOutputCurrentValueStr_Type()
)
pdnOutputCurrentValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputCurrentValueStr.setStatus("current")
_PdnOutputCurrentDeadband_Type = Integer32
_PdnOutputCurrentDeadband_Object = MibTableColumn
pdnOutputCurrentDeadband = _PdnOutputCurrentDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 25),
    _PdnOutputCurrentDeadband_Type()
)
pdnOutputCurrentDeadband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputCurrentDeadband.setStatus("current")
_PdnOutputCurrentVHighCurrent_Type = Integer32
_PdnOutputCurrentVHighCurrent_Object = MibTableColumn
pdnOutputCurrentVHighCurrent = _PdnOutputCurrentVHighCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 26),
    _PdnOutputCurrentVHighCurrent_Type()
)
pdnOutputCurrentVHighCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputCurrentVHighCurrent.setStatus("current")
_PdnOutputCurrentHighCurrent_Type = Integer32
_PdnOutputCurrentHighCurrent_Object = MibTableColumn
pdnOutputCurrentHighCurrent = _PdnOutputCurrentHighCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 27),
    _PdnOutputCurrentHighCurrent_Type()
)
pdnOutputCurrentHighCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputCurrentHighCurrent.setStatus("current")
_PdnOutputCurrentLowCurrent_Type = Integer32
_PdnOutputCurrentLowCurrent_Object = MibTableColumn
pdnOutputCurrentLowCurrent = _PdnOutputCurrentLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 28),
    _PdnOutputCurrentLowCurrent_Type()
)
pdnOutputCurrentLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputCurrentLowCurrent.setStatus("current")
_PdnOutputCurrentVLowCurrent_Type = Integer32
_PdnOutputCurrentVLowCurrent_Object = MibTableColumn
pdnOutputCurrentVLowCurrent = _PdnOutputCurrentVLowCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 29),
    _PdnOutputCurrentVLowCurrent_Type()
)
pdnOutputCurrentVLowCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputCurrentVLowCurrent.setStatus("current")
_PdnOutputFuseInEventState_Type = DisplayString
_PdnOutputFuseInEventState_Object = MibTableColumn
pdnOutputFuseInEventState = _PdnOutputFuseInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 30),
    _PdnOutputFuseInEventState_Type()
)
pdnOutputFuseInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputFuseInEventState.setStatus("current")
_PdnOutputFuseValueStr_Type = DisplayString
_PdnOutputFuseValueStr_Object = MibTableColumn
pdnOutputFuseValueStr = _PdnOutputFuseValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 31),
    _PdnOutputFuseValueStr_Type()
)
pdnOutputFuseValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputFuseValueStr.setStatus("current")
_PdnMainCombinedStatus_Type = DisplayString
_PdnMainCombinedStatus_Object = MibTableColumn
pdnMainCombinedStatus = _PdnMainCombinedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 32),
    _PdnMainCombinedStatus_Type()
)
pdnMainCombinedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnMainCombinedStatus.setStatus("current")
_PdnOutputCombinedStatusBlock1_Type = DisplayString
_PdnOutputCombinedStatusBlock1_Object = MibTableColumn
pdnOutputCombinedStatusBlock1 = _PdnOutputCombinedStatusBlock1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 33),
    _PdnOutputCombinedStatusBlock1_Type()
)
pdnOutputCombinedStatusBlock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputCombinedStatusBlock1.setStatus("current")
_PdnOutputCombinedStatusBlock2_Type = DisplayString
_PdnOutputCombinedStatusBlock2_Object = MibTableColumn
pdnOutputCombinedStatusBlock2 = _PdnOutputCombinedStatusBlock2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 34),
    _PdnOutputCombinedStatusBlock2_Type()
)
pdnOutputCombinedStatusBlock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnOutputCombinedStatusBlock2.setStatus("current")
_PdnDeviceCurrentValue_Type = Integer32
_PdnDeviceCurrentValue_Object = MibTableColumn
pdnDeviceCurrentValue = _PdnDeviceCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 35),
    _PdnDeviceCurrentValue_Type()
)
pdnDeviceCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDeviceCurrentValue.setStatus("current")
_PdnDeviceCurrentValueStr_Type = DisplayString
_PdnDeviceCurrentValueStr_Object = MibTableColumn
pdnDeviceCurrentValueStr = _PdnDeviceCurrentValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 4, 1, 1, 36),
    _PdnDeviceCurrentValueStr_Type()
)
pdnDeviceCurrentValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDeviceCurrentValueStr.setStatus("current")
_PdSystem_ObjectIdentity = ObjectIdentity
pdSystem = _PdSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 5)
)
_PdSystemCurrent_Type = DisplayString
_PdSystemCurrent_Object = MibScalar
pdSystemCurrent = _PdSystemCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 5, 1),
    _PdSystemCurrent_Type()
)
pdSystemCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdSystemCurrent.setStatus("current")
_PdSystemPower_Type = DisplayString
_PdSystemPower_Object = MibScalar
pdSystemPower = _PdSystemPower_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 5, 5, 2),
    _PdSystemPower_Type()
)
pdSystemPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdSystemPower.setStatus("current")
_FuelSensorStatus_ObjectIdentity = ObjectIdentity
fuelSensorStatus = _FuelSensorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 6)
)
_FsStatusTable_Object = MibTable
fsStatusTable = _FsStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fsStatusTable.setStatus("current")
_FsStatusEntry_Object = MibTableRow
fsStatusEntry = _FsStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 6, 1, 1)
)
fsStatusEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "fsStatusIndex"),
)
if mibBuilder.loadTexts:
    fsStatusEntry.setStatus("current")


class _FsStatusIndex_Type(Integer32):
    """Custom type fsStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsStatusIndex_Type.__name__ = "Integer32"
_FsStatusIndex_Object = MibTableColumn
fsStatusIndex = _FsStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 6, 1, 1, 1),
    _FsStatusIndex_Type()
)
fsStatusIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusIndex.setStatus("current")
_FsStatusName_Type = DisplayString
_FsStatusName_Object = MibTableColumn
fsStatusName = _FsStatusName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 6, 1, 1, 2),
    _FsStatusName_Type()
)
fsStatusName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusName.setStatus("current")
_FsStatusDeviceState_Type = DisplayString
_FsStatusDeviceState_Object = MibTableColumn
fsStatusDeviceState = _FsStatusDeviceState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 6, 1, 1, 3),
    _FsStatusDeviceState_Type()
)
fsStatusDeviceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusDeviceState.setStatus("current")
_FsStatusVolumeValueString_Type = DisplayString
_FsStatusVolumeValueString_Object = MibTableColumn
fsStatusVolumeValueString = _FsStatusVolumeValueString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 6, 1, 1, 4),
    _FsStatusVolumeValueString_Type()
)
fsStatusVolumeValueString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusVolumeValueString.setStatus("current")
_FsStatusVolumePercentLevel_Type = DisplayString
_FsStatusVolumePercentLevel_Object = MibTableColumn
fsStatusVolumePercentLevel = _FsStatusVolumePercentLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 6, 1, 1, 7),
    _FsStatusVolumePercentLevel_Type()
)
fsStatusVolumePercentLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusVolumePercentLevel.setStatus("current")
_FsStatusVolumeInEventState_Type = DisplayString
_FsStatusVolumeInEventState_Object = MibTableColumn
fsStatusVolumeInEventState = _FsStatusVolumeInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 6, 1, 1, 8),
    _FsStatusVolumeInEventState_Type()
)
fsStatusVolumeInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusVolumeInEventState.setStatus("current")
_FsStatusCombined_Type = DisplayString
_FsStatusCombined_Object = MibTableColumn
fsStatusCombined = _FsStatusCombined_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 6, 1, 1, 9),
    _FsStatusCombined_Type()
)
fsStatusCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStatusCombined.setStatus("current")
_WirelessModemStatus_ObjectIdentity = ObjectIdentity
wirelessModemStatus = _WirelessModemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7)
)
_WmsStatus_Type = DisplayString
_WmsStatus_Object = MibScalar
wmsStatus = _WmsStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 1),
    _WmsStatus_Type()
)
wmsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsStatus.setStatus("current")
_WmsSignal_Type = DisplayString
_WmsSignal_Object = MibScalar
wmsSignal = _WmsSignal_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 2),
    _WmsSignal_Type()
)
wmsSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsSignal.setStatus("current")
_WmsRSSI_Type = DisplayString
_WmsRSSI_Object = MibScalar
wmsRSSI = _WmsRSSI_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 3),
    _WmsRSSI_Type()
)
wmsRSSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsRSSI.setStatus("current")
_WmsBER_Type = DisplayString
_WmsBER_Object = MibScalar
wmsBER = _WmsBER_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 4),
    _WmsBER_Type()
)
wmsBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsBER.setStatus("current")
_WmsUpdated_Type = DisplayString
_WmsUpdated_Object = MibScalar
wmsUpdated = _WmsUpdated_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 5),
    _WmsUpdated_Type()
)
wmsUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsUpdated.setStatus("current")
_WmsRegistration_Type = DisplayString
_WmsRegistration_Object = MibScalar
wmsRegistration = _WmsRegistration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 6),
    _WmsRegistration_Type()
)
wmsRegistration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsRegistration.setStatus("current")
_WmsLAC_Type = DisplayString
_WmsLAC_Object = MibScalar
wmsLAC = _WmsLAC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 7),
    _WmsLAC_Type()
)
wmsLAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsLAC.setStatus("current")
_WmsCellID_Type = DisplayString
_WmsCellID_Object = MibScalar
wmsCellID = _WmsCellID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 8),
    _WmsCellID_Type()
)
wmsCellID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsCellID.setStatus("current")
_WmsIMSI_Type = DisplayString
_WmsIMSI_Object = MibScalar
wmsIMSI = _WmsIMSI_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 9),
    _WmsIMSI_Type()
)
wmsIMSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsIMSI.setStatus("current")
_WmsPhnum_Type = DisplayString
_WmsPhnum_Object = MibScalar
wmsPhnum = _WmsPhnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 10),
    _WmsPhnum_Type()
)
wmsPhnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsPhnum.setStatus("current")
_WmsLocalIP_Type = DisplayString
_WmsLocalIP_Object = MibScalar
wmsLocalIP = _WmsLocalIP_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 11),
    _WmsLocalIP_Type()
)
wmsLocalIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsLocalIP.setStatus("current")
_WmsMgfID_Type = DisplayString
_WmsMgfID_Object = MibScalar
wmsMgfID = _WmsMgfID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 12),
    _WmsMgfID_Type()
)
wmsMgfID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsMgfID.setStatus("current")
_WmsModelID_Type = DisplayString
_WmsModelID_Object = MibScalar
wmsModelID = _WmsModelID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 13),
    _WmsModelID_Type()
)
wmsModelID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsModelID.setStatus("current")
_WmsIMEI_Type = DisplayString
_WmsIMEI_Object = MibScalar
wmsIMEI = _WmsIMEI_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 14),
    _WmsIMEI_Type()
)
wmsIMEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsIMEI.setStatus("current")
_WmsRevID_Type = DisplayString
_WmsRevID_Object = MibScalar
wmsRevID = _WmsRevID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 15),
    _WmsRevID_Type()
)
wmsRevID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsRevID.setStatus("current")
_WmsNetName_Type = DisplayString
_WmsNetName_Object = MibScalar
wmsNetName = _WmsNetName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 16),
    _WmsNetName_Type()
)
wmsNetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsNetName.setStatus("current")
_WmsGPRSStatus_Type = DisplayString
_WmsGPRSStatus_Object = MibScalar
wmsGPRSStatus = _WmsGPRSStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 17),
    _WmsGPRSStatus_Type()
)
wmsGPRSStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsGPRSStatus.setStatus("current")
_WmsBand_Type = DisplayString
_WmsBand_Object = MibScalar
wmsBand = _WmsBand_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 18),
    _WmsBand_Type()
)
wmsBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsBand.setStatus("current")
_WmsChannel_Type = DisplayString
_WmsChannel_Object = MibScalar
wmsChannel = _WmsChannel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 19),
    _WmsChannel_Type()
)
wmsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsChannel.setStatus("current")
_WmsCountryCode_Type = DisplayString
_WmsCountryCode_Object = MibScalar
wmsCountryCode = _WmsCountryCode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 20),
    _WmsCountryCode_Type()
)
wmsCountryCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsCountryCode.setStatus("current")
_WmsNetCode_Type = DisplayString
_WmsNetCode_Object = MibScalar
wmsNetCode = _WmsNetCode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 21),
    _WmsNetCode_Type()
)
wmsNetCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsNetCode.setStatus("current")
_WmsPLMNColor_Type = DisplayString
_WmsPLMNColor_Object = MibScalar
wmsPLMNColor = _WmsPLMNColor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 22),
    _WmsPLMNColor_Type()
)
wmsPLMNColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsPLMNColor.setStatus("current")
_WmsBScolor_Type = DisplayString
_WmsBScolor_Object = MibScalar
wmsBScolor = _WmsBScolor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 23),
    _WmsBScolor_Type()
)
wmsBScolor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsBScolor.setStatus("current")
_WmsMpRACH_Type = DisplayString
_WmsMpRACH_Object = MibScalar
wmsMpRACH = _WmsMpRACH_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 24),
    _WmsMpRACH_Type()
)
wmsMpRACH.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsMpRACH.setStatus("current")
_WmsMinRxLevel_Type = DisplayString
_WmsMinRxLevel_Object = MibScalar
wmsMinRxLevel = _WmsMinRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 25),
    _WmsMinRxLevel_Type()
)
wmsMinRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsMinRxLevel.setStatus("current")
_WmsBaseCoeff_Type = DisplayString
_WmsBaseCoeff_Object = MibScalar
wmsBaseCoeff = _WmsBaseCoeff_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 26),
    _WmsBaseCoeff_Type()
)
wmsBaseCoeff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsBaseCoeff.setStatus("current")
_WmsSIMStatus_Type = DisplayString
_WmsSIMStatus_Object = MibScalar
wmsSIMStatus = _WmsSIMStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 27),
    _WmsSIMStatus_Type()
)
wmsSIMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsSIMStatus.setStatus("current")
_WmsICCID_Type = DisplayString
_WmsICCID_Object = MibScalar
wmsICCID = _WmsICCID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 28),
    _WmsICCID_Type()
)
wmsICCID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsICCID.setStatus("current")
_WmsModemType_Type = DisplayString
_WmsModemType_Object = MibScalar
wmsModemType = _WmsModemType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 7, 29),
    _WmsModemType_Type()
)
wmsModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wmsModemType.setStatus("current")
_AcPowerMonitorStatus_ObjectIdentity = ObjectIdentity
acPowerMonitorStatus = _AcPowerMonitorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8)
)
_AcpmStatusTable_Object = MibTable
acpmStatusTable = _AcpmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1)
)
if mibBuilder.loadTexts:
    acpmStatusTable.setStatus("current")
_AcpmStatusEntry_Object = MibTableRow
acpmStatusEntry = _AcpmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1)
)
acpmStatusEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "acpmsIndex"),
)
if mibBuilder.loadTexts:
    acpmStatusEntry.setStatus("current")


class _AcpmsIndex_Type(Integer32):
    """Custom type acpmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmsIndex_Type.__name__ = "Integer32"
_AcpmsIndex_Object = MibTableColumn
acpmsIndex = _AcpmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 1),
    _AcpmsIndex_Type()
)
acpmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsIndex.setStatus("current")
_AcpmsName_Type = DisplayString
_AcpmsName_Object = MibTableColumn
acpmsName = _AcpmsName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 2),
    _AcpmsName_Type()
)
acpmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsName.setStatus("current")
_AcpmsAvgVoltageValueStr_Type = DisplayString
_AcpmsAvgVoltageValueStr_Object = MibTableColumn
acpmsAvgVoltageValueStr = _AcpmsAvgVoltageValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 3),
    _AcpmsAvgVoltageValueStr_Type()
)
acpmsAvgVoltageValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgVoltageValueStr.setStatus("current")
_AcpmsAvgVoltageMinStr_Type = DisplayString
_AcpmsAvgVoltageMinStr_Object = MibTableColumn
acpmsAvgVoltageMinStr = _AcpmsAvgVoltageMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 4),
    _AcpmsAvgVoltageMinStr_Type()
)
acpmsAvgVoltageMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgVoltageMinStr.setStatus("current")
_AcpmsAvgVoltageMaxStr_Type = DisplayString
_AcpmsAvgVoltageMaxStr_Object = MibTableColumn
acpmsAvgVoltageMaxStr = _AcpmsAvgVoltageMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 5),
    _AcpmsAvgVoltageMaxStr_Type()
)
acpmsAvgVoltageMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgVoltageMaxStr.setStatus("current")
_AcpmsAvgVoltageAvgStr_Type = DisplayString
_AcpmsAvgVoltageAvgStr_Object = MibTableColumn
acpmsAvgVoltageAvgStr = _AcpmsAvgVoltageAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 6),
    _AcpmsAvgVoltageAvgStr_Type()
)
acpmsAvgVoltageAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgVoltageAvgStr.setStatus("current")
_AcpmsAvgVoltageInEventState_Type = DisplayString
_AcpmsAvgVoltageInEventState_Object = MibTableColumn
acpmsAvgVoltageInEventState = _AcpmsAvgVoltageInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 7),
    _AcpmsAvgVoltageInEventState_Type()
)
acpmsAvgVoltageInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgVoltageInEventState.setStatus("current")
_AcpmsVoltagePhaseAValueStr_Type = DisplayString
_AcpmsVoltagePhaseAValueStr_Object = MibTableColumn
acpmsVoltagePhaseAValueStr = _AcpmsVoltagePhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 8),
    _AcpmsVoltagePhaseAValueStr_Type()
)
acpmsVoltagePhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsVoltagePhaseAValueStr.setStatus("current")
_AcpmsVoltagePhaseBValueStr_Type = DisplayString
_AcpmsVoltagePhaseBValueStr_Object = MibTableColumn
acpmsVoltagePhaseBValueStr = _AcpmsVoltagePhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 9),
    _AcpmsVoltagePhaseBValueStr_Type()
)
acpmsVoltagePhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsVoltagePhaseBValueStr.setStatus("current")
_AcpmsVoltagePhaseCValueStr_Type = DisplayString
_AcpmsVoltagePhaseCValueStr_Object = MibTableColumn
acpmsVoltagePhaseCValueStr = _AcpmsVoltagePhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 10),
    _AcpmsVoltagePhaseCValueStr_Type()
)
acpmsVoltagePhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsVoltagePhaseCValueStr.setStatus("current")
_AcpmsAvgCurrentValueStr_Type = DisplayString
_AcpmsAvgCurrentValueStr_Object = MibTableColumn
acpmsAvgCurrentValueStr = _AcpmsAvgCurrentValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 11),
    _AcpmsAvgCurrentValueStr_Type()
)
acpmsAvgCurrentValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgCurrentValueStr.setStatus("current")
_AcpmsAvgCurrentMinStr_Type = DisplayString
_AcpmsAvgCurrentMinStr_Object = MibTableColumn
acpmsAvgCurrentMinStr = _AcpmsAvgCurrentMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 12),
    _AcpmsAvgCurrentMinStr_Type()
)
acpmsAvgCurrentMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgCurrentMinStr.setStatus("current")
_AcpmsAvgCurrentMaxStr_Type = DisplayString
_AcpmsAvgCurrentMaxStr_Object = MibTableColumn
acpmsAvgCurrentMaxStr = _AcpmsAvgCurrentMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 13),
    _AcpmsAvgCurrentMaxStr_Type()
)
acpmsAvgCurrentMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgCurrentMaxStr.setStatus("current")
_AcpmsAvgCurrentAvgStr_Type = DisplayString
_AcpmsAvgCurrentAvgStr_Object = MibTableColumn
acpmsAvgCurrentAvgStr = _AcpmsAvgCurrentAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 14),
    _AcpmsAvgCurrentAvgStr_Type()
)
acpmsAvgCurrentAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgCurrentAvgStr.setStatus("current")
_AcpmsAvgCurrentInEventState_Type = DisplayString
_AcpmsAvgCurrentInEventState_Object = MibTableColumn
acpmsAvgCurrentInEventState = _AcpmsAvgCurrentInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 15),
    _AcpmsAvgCurrentInEventState_Type()
)
acpmsAvgCurrentInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgCurrentInEventState.setStatus("current")
_AcpmsCurrentPhaseAValueStr_Type = DisplayString
_AcpmsCurrentPhaseAValueStr_Object = MibTableColumn
acpmsCurrentPhaseAValueStr = _AcpmsCurrentPhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 16),
    _AcpmsCurrentPhaseAValueStr_Type()
)
acpmsCurrentPhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsCurrentPhaseAValueStr.setStatus("current")
_AcpmsCurrentPhaseBValueStr_Type = DisplayString
_AcpmsCurrentPhaseBValueStr_Object = MibTableColumn
acpmsCurrentPhaseBValueStr = _AcpmsCurrentPhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 17),
    _AcpmsCurrentPhaseBValueStr_Type()
)
acpmsCurrentPhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsCurrentPhaseBValueStr.setStatus("current")
_AcpmsCurrentPhaseCValueStr_Type = DisplayString
_AcpmsCurrentPhaseCValueStr_Object = MibTableColumn
acpmsCurrentPhaseCValueStr = _AcpmsCurrentPhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 18),
    _AcpmsCurrentPhaseCValueStr_Type()
)
acpmsCurrentPhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsCurrentPhaseCValueStr.setStatus("current")
_AcpmsAvgFreqValueStr_Type = DisplayString
_AcpmsAvgFreqValueStr_Object = MibTableColumn
acpmsAvgFreqValueStr = _AcpmsAvgFreqValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 19),
    _AcpmsAvgFreqValueStr_Type()
)
acpmsAvgFreqValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgFreqValueStr.setStatus("current")
_AcpmsAvgFreqMinStr_Type = DisplayString
_AcpmsAvgFreqMinStr_Object = MibTableColumn
acpmsAvgFreqMinStr = _AcpmsAvgFreqMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 20),
    _AcpmsAvgFreqMinStr_Type()
)
acpmsAvgFreqMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgFreqMinStr.setStatus("current")
_AcpmsAvgFreqMaxStr_Type = DisplayString
_AcpmsAvgFreqMaxStr_Object = MibTableColumn
acpmsAvgFreqMaxStr = _AcpmsAvgFreqMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 21),
    _AcpmsAvgFreqMaxStr_Type()
)
acpmsAvgFreqMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgFreqMaxStr.setStatus("current")
_AcpmsAvgFreqAvgStr_Type = DisplayString
_AcpmsAvgFreqAvgStr_Object = MibTableColumn
acpmsAvgFreqAvgStr = _AcpmsAvgFreqAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 22),
    _AcpmsAvgFreqAvgStr_Type()
)
acpmsAvgFreqAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgFreqAvgStr.setStatus("current")
_AcpmsAvgFreqInEventState_Type = DisplayString
_AcpmsAvgFreqInEventState_Object = MibTableColumn
acpmsAvgFreqInEventState = _AcpmsAvgFreqInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 23),
    _AcpmsAvgFreqInEventState_Type()
)
acpmsAvgFreqInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAvgFreqInEventState.setStatus("current")
_AcpmsTRPValueStr_Type = DisplayString
_AcpmsTRPValueStr_Object = MibTableColumn
acpmsTRPValueStr = _AcpmsTRPValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 24),
    _AcpmsTRPValueStr_Type()
)
acpmsTRPValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRPValueStr.setStatus("current")
_AcpmsTRPMinStr_Type = DisplayString
_AcpmsTRPMinStr_Object = MibTableColumn
acpmsTRPMinStr = _AcpmsTRPMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 25),
    _AcpmsTRPMinStr_Type()
)
acpmsTRPMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRPMinStr.setStatus("current")
_AcpmsTRPMaxStr_Type = DisplayString
_AcpmsTRPMaxStr_Object = MibTableColumn
acpmsTRPMaxStr = _AcpmsTRPMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 26),
    _AcpmsTRPMaxStr_Type()
)
acpmsTRPMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRPMaxStr.setStatus("current")
_AcpmsTRPAvgStr_Type = DisplayString
_AcpmsTRPAvgStr_Object = MibTableColumn
acpmsTRPAvgStr = _AcpmsTRPAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 27),
    _AcpmsTRPAvgStr_Type()
)
acpmsTRPAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRPAvgStr.setStatus("current")
_AcpmsTRPInEventState_Type = DisplayString
_AcpmsTRPInEventState_Object = MibTableColumn
acpmsTRPInEventState = _AcpmsTRPInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 28),
    _AcpmsTRPInEventState_Type()
)
acpmsTRPInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRPInEventState.setStatus("current")
_AcpmsRPPhaseAValueStr_Type = DisplayString
_AcpmsRPPhaseAValueStr_Object = MibTableColumn
acpmsRPPhaseAValueStr = _AcpmsRPPhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 29),
    _AcpmsRPPhaseAValueStr_Type()
)
acpmsRPPhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRPPhaseAValueStr.setStatus("current")
_AcpmsRPPhaseBValueStr_Type = DisplayString
_AcpmsRPPhaseBValueStr_Object = MibTableColumn
acpmsRPPhaseBValueStr = _AcpmsRPPhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 30),
    _AcpmsRPPhaseBValueStr_Type()
)
acpmsRPPhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRPPhaseBValueStr.setStatus("current")
_AcpmsRPPhaseCValueStr_Type = DisplayString
_AcpmsRPPhaseCValueStr_Object = MibTableColumn
acpmsRPPhaseCValueStr = _AcpmsRPPhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 31),
    _AcpmsRPPhaseCValueStr_Type()
)
acpmsRPPhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRPPhaseCValueStr.setStatus("current")
_AcpmsCombined_Type = DisplayString
_AcpmsCombined_Object = MibTableColumn
acpmsCombined = _AcpmsCombined_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 32),
    _AcpmsCombined_Type()
)
acpmsCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsCombined.setStatus("current")
_AcpmsTPFValueStr_Type = DisplayString
_AcpmsTPFValueStr_Object = MibTableColumn
acpmsTPFValueStr = _AcpmsTPFValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 33),
    _AcpmsTPFValueStr_Type()
)
acpmsTPFValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTPFValueStr.setStatus("current")
_AcpmsTPFMinStr_Type = DisplayString
_AcpmsTPFMinStr_Object = MibTableColumn
acpmsTPFMinStr = _AcpmsTPFMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 34),
    _AcpmsTPFMinStr_Type()
)
acpmsTPFMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTPFMinStr.setStatus("current")
_AcpmsTPFMaxStr_Type = DisplayString
_AcpmsTPFMaxStr_Object = MibTableColumn
acpmsTPFMaxStr = _AcpmsTPFMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 35),
    _AcpmsTPFMaxStr_Type()
)
acpmsTPFMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTPFMaxStr.setStatus("current")
_AcpmsTPFAvgStr_Type = DisplayString
_AcpmsTPFAvgStr_Object = MibTableColumn
acpmsTPFAvgStr = _AcpmsTPFAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 36),
    _AcpmsTPFAvgStr_Type()
)
acpmsTPFAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTPFAvgStr.setStatus("current")
_AcpmsTPFInEventState_Type = DisplayString
_AcpmsTPFInEventState_Object = MibTableColumn
acpmsTPFInEventState = _AcpmsTPFInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 37),
    _AcpmsTPFInEventState_Type()
)
acpmsTPFInEventState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTPFInEventState.setStatus("current")
_AcpmsPFPhaseAValueStr_Type = DisplayString
_AcpmsPFPhaseAValueStr_Object = MibTableColumn
acpmsPFPhaseAValueStr = _AcpmsPFPhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 38),
    _AcpmsPFPhaseAValueStr_Type()
)
acpmsPFPhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsPFPhaseAValueStr.setStatus("current")
_AcpmsPFPhaseBValueStr_Type = DisplayString
_AcpmsPFPhaseBValueStr_Object = MibTableColumn
acpmsPFPhaseBValueStr = _AcpmsPFPhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 39),
    _AcpmsPFPhaseBValueStr_Type()
)
acpmsPFPhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsPFPhaseBValueStr.setStatus("current")
_AcpmsPFPhaseCValueStr_Type = DisplayString
_AcpmsPFPhaseCValueStr_Object = MibTableColumn
acpmsPFPhaseCValueStr = _AcpmsPFPhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 40),
    _AcpmsPFPhaseCValueStr_Type()
)
acpmsPFPhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsPFPhaseCValueStr.setStatus("current")
_AcpmsTRcPValueStr_Type = DisplayString
_AcpmsTRcPValueStr_Object = MibTableColumn
acpmsTRcPValueStr = _AcpmsTRcPValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 41),
    _AcpmsTRcPValueStr_Type()
)
acpmsTRcPValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRcPValueStr.setStatus("current")
_AcpmsTRcPMinStr_Type = DisplayString
_AcpmsTRcPMinStr_Object = MibTableColumn
acpmsTRcPMinStr = _AcpmsTRcPMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 42),
    _AcpmsTRcPMinStr_Type()
)
acpmsTRcPMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRcPMinStr.setStatus("current")
_AcpmsTRcPMaxStr_Type = DisplayString
_AcpmsTRcPMaxStr_Object = MibTableColumn
acpmsTRcPMaxStr = _AcpmsTRcPMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 43),
    _AcpmsTRcPMaxStr_Type()
)
acpmsTRcPMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRcPMaxStr.setStatus("current")
_AcpmsTRcPAvgStr_Type = DisplayString
_AcpmsTRcPAvgStr_Object = MibTableColumn
acpmsTRcPAvgStr = _AcpmsTRcPAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 44),
    _AcpmsTRcPAvgStr_Type()
)
acpmsTRcPAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTRcPAvgStr.setStatus("current")
_AcpmsRcPPhaseAValueStr_Type = DisplayString
_AcpmsRcPPhaseAValueStr_Object = MibTableColumn
acpmsRcPPhaseAValueStr = _AcpmsRcPPhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 45),
    _AcpmsRcPPhaseAValueStr_Type()
)
acpmsRcPPhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRcPPhaseAValueStr.setStatus("current")
_AcpmsRcPPhaseBValueStr_Type = DisplayString
_AcpmsRcPPhaseBValueStr_Object = MibTableColumn
acpmsRcPPhaseBValueStr = _AcpmsRcPPhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 46),
    _AcpmsRcPPhaseBValueStr_Type()
)
acpmsRcPPhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRcPPhaseBValueStr.setStatus("current")
_AcpmsRcPPhaseCValueStr_Type = DisplayString
_AcpmsRcPPhaseCValueStr_Object = MibTableColumn
acpmsRcPPhaseCValueStr = _AcpmsRcPPhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 47),
    _AcpmsRcPPhaseCValueStr_Type()
)
acpmsRcPPhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsRcPPhaseCValueStr.setStatus("current")
_AcpmsTAPValueStr_Type = DisplayString
_AcpmsTAPValueStr_Object = MibTableColumn
acpmsTAPValueStr = _AcpmsTAPValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 48),
    _AcpmsTAPValueStr_Type()
)
acpmsTAPValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTAPValueStr.setStatus("current")
_AcpmsTAPMinStr_Type = DisplayString
_AcpmsTAPMinStr_Object = MibTableColumn
acpmsTAPMinStr = _AcpmsTAPMinStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 49),
    _AcpmsTAPMinStr_Type()
)
acpmsTAPMinStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTAPMinStr.setStatus("current")
_AcpmsTAPMaxStr_Type = DisplayString
_AcpmsTAPMaxStr_Object = MibTableColumn
acpmsTAPMaxStr = _AcpmsTAPMaxStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 50),
    _AcpmsTAPMaxStr_Type()
)
acpmsTAPMaxStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTAPMaxStr.setStatus("current")
_AcpmsTAPAvgStr_Type = DisplayString
_AcpmsTAPAvgStr_Object = MibTableColumn
acpmsTAPAvgStr = _AcpmsTAPAvgStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 51),
    _AcpmsTAPAvgStr_Type()
)
acpmsTAPAvgStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTAPAvgStr.setStatus("current")
_AcpmsAPPhaseAValueStr_Type = DisplayString
_AcpmsAPPhaseAValueStr_Object = MibTableColumn
acpmsAPPhaseAValueStr = _AcpmsAPPhaseAValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 52),
    _AcpmsAPPhaseAValueStr_Type()
)
acpmsAPPhaseAValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAPPhaseAValueStr.setStatus("current")
_AcpmsAPPhaseBValueStr_Type = DisplayString
_AcpmsAPPhaseBValueStr_Object = MibTableColumn
acpmsAPPhaseBValueStr = _AcpmsAPPhaseBValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 53),
    _AcpmsAPPhaseBValueStr_Type()
)
acpmsAPPhaseBValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAPPhaseBValueStr.setStatus("current")
_AcpmsAPPhaseCValueStr_Type = DisplayString
_AcpmsAPPhaseCValueStr_Object = MibTableColumn
acpmsAPPhaseCValueStr = _AcpmsAPPhaseCValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 54),
    _AcpmsAPPhaseCValueStr_Type()
)
acpmsAPPhaseCValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsAPPhaseCValueStr.setStatus("current")
_AcpmsTotalEnergyWh_Type = Integer32
_AcpmsTotalEnergyWh_Object = MibTableColumn
acpmsTotalEnergyWh = _AcpmsTotalEnergyWh_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 55),
    _AcpmsTotalEnergyWh_Type()
)
acpmsTotalEnergyWh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTotalEnergyWh.setStatus("current")
_AcpmsTotalEnergyVAR_Type = Integer32
_AcpmsTotalEnergyVAR_Object = MibTableColumn
acpmsTotalEnergyVAR = _AcpmsTotalEnergyVAR_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 56),
    _AcpmsTotalEnergyVAR_Type()
)
acpmsTotalEnergyVAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTotalEnergyVAR.setStatus("current")
_AcpmsTotalEnergyVA_Type = Integer32
_AcpmsTotalEnergyVA_Object = MibTableColumn
acpmsTotalEnergyVA = _AcpmsTotalEnergyVA_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 8, 1, 1, 57),
    _AcpmsTotalEnergyVA_Type()
)
acpmsTotalEnergyVA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmsTotalEnergyVA.setStatus("current")
_BatteryMonitorStatus_ObjectIdentity = ObjectIdentity
batteryMonitorStatus = _BatteryMonitorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10)
)
_BmStatusTable_Object = MibTable
bmStatusTable = _BmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1)
)
if mibBuilder.loadTexts:
    bmStatusTable.setStatus("current")
_BmStatusEntry_Object = MibTableRow
bmStatusEntry = _BmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1)
)
bmStatusEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmsIndex"),
)
if mibBuilder.loadTexts:
    bmStatusEntry.setStatus("current")


class _BmsIndex_Type(Integer32):
    """Custom type bmsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmsIndex_Type.__name__ = "Integer32"
_BmsIndex_Object = MibTableColumn
bmsIndex = _BmsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 1),
    _BmsIndex_Type()
)
bmsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsIndex.setStatus("current")
_BmsEnable_Type = DisplayString
_BmsEnable_Object = MibTableColumn
bmsEnable = _BmsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 2),
    _BmsEnable_Type()
)
bmsEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsEnable.setStatus("current")
_BmsName_Type = DisplayString
_BmsName_Object = MibTableColumn
bmsName = _BmsName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 3),
    _BmsName_Type()
)
bmsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsName.setStatus("current")
_BmsState_Type = DisplayString
_BmsState_Object = MibTableColumn
bmsState = _BmsState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 4),
    _BmsState_Type()
)
bmsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsState.setStatus("current")
_BmsStringState_Type = DisplayString
_BmsStringState_Object = MibTableColumn
bmsStringState = _BmsStringState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 5),
    _BmsStringState_Type()
)
bmsStringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsStringState.setStatus("current")
_BmsTempValue_Type = DisplayString
_BmsTempValue_Object = MibTableColumn
bmsTempValue = _BmsTempValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 6),
    _BmsTempValue_Type()
)
bmsTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsTempValue.setStatus("current")
_BmsTempValueStr_Type = DisplayString
_BmsTempValueStr_Object = MibTableColumn
bmsTempValueStr = _BmsTempValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 7),
    _BmsTempValueStr_Type()
)
bmsTempValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsTempValueStr.setStatus("current")
_BmsTempEvent_Type = DisplayString
_BmsTempEvent_Object = MibTableColumn
bmsTempEvent = _BmsTempEvent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 8),
    _BmsTempEvent_Type()
)
bmsTempEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsTempEvent.setStatus("current")
_BmsDiffTempValue_Type = Integer32
_BmsDiffTempValue_Object = MibTableColumn
bmsDiffTempValue = _BmsDiffTempValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 9),
    _BmsDiffTempValue_Type()
)
bmsDiffTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsDiffTempValue.setStatus("current")
_BmsDiffTempValueStr_Type = DisplayString
_BmsDiffTempValueStr_Object = MibTableColumn
bmsDiffTempValueStr = _BmsDiffTempValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 10),
    _BmsDiffTempValueStr_Type()
)
bmsDiffTempValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsDiffTempValueStr.setStatus("current")
_BmsDiffTempEvent_Type = DisplayString
_BmsDiffTempEvent_Object = MibTableColumn
bmsDiffTempEvent = _BmsDiffTempEvent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 11),
    _BmsDiffTempEvent_Type()
)
bmsDiffTempEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsDiffTempEvent.setStatus("current")
_BmsVoltageValue_Type = DisplayString
_BmsVoltageValue_Object = MibTableColumn
bmsVoltageValue = _BmsVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 12),
    _BmsVoltageValue_Type()
)
bmsVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsVoltageValue.setStatus("current")
_BmsVoltageEvent_Type = DisplayString
_BmsVoltageEvent_Object = MibTableColumn
bmsVoltageEvent = _BmsVoltageEvent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 13),
    _BmsVoltageEvent_Type()
)
bmsVoltageEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsVoltageEvent.setStatus("current")
_BmsDiffVoltValue_Type = DisplayString
_BmsDiffVoltValue_Object = MibTableColumn
bmsDiffVoltValue = _BmsDiffVoltValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 14),
    _BmsDiffVoltValue_Type()
)
bmsDiffVoltValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsDiffVoltValue.setStatus("current")
_BmsDiffVoltEvent_Type = DisplayString
_BmsDiffVoltEvent_Object = MibTableColumn
bmsDiffVoltEvent = _BmsDiffVoltEvent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 15),
    _BmsDiffVoltEvent_Type()
)
bmsDiffVoltEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsDiffVoltEvent.setStatus("current")
_BmsCurrentValue_Type = DisplayString
_BmsCurrentValue_Object = MibTableColumn
bmsCurrentValue = _BmsCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 16),
    _BmsCurrentValue_Type()
)
bmsCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsCurrentValue.setStatus("current")
_BmsChargingCurrentEvent_Type = DisplayString
_BmsChargingCurrentEvent_Object = MibTableColumn
bmsChargingCurrentEvent = _BmsChargingCurrentEvent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 17),
    _BmsChargingCurrentEvent_Type()
)
bmsChargingCurrentEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsChargingCurrentEvent.setStatus("current")
_BmsDischargingCurrentEvent_Type = DisplayString
_BmsDischargingCurrentEvent_Object = MibTableColumn
bmsDischargingCurrentEvent = _BmsDischargingCurrentEvent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 18),
    _BmsDischargingCurrentEvent_Type()
)
bmsDischargingCurrentEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsDischargingCurrentEvent.setStatus("current")
_BmsChargeLevelValue_Type = DisplayString
_BmsChargeLevelValue_Object = MibTableColumn
bmsChargeLevelValue = _BmsChargeLevelValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 19),
    _BmsChargeLevelValue_Type()
)
bmsChargeLevelValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsChargeLevelValue.setStatus("current")
_BmsChargeLevelEvent_Type = DisplayString
_BmsChargeLevelEvent_Object = MibTableColumn
bmsChargeLevelEvent = _BmsChargeLevelEvent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 20),
    _BmsChargeLevelEvent_Type()
)
bmsChargeLevelEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsChargeLevelEvent.setStatus("current")
_BmsJarHealthValue_Type = DisplayString
_BmsJarHealthValue_Object = MibTableColumn
bmsJarHealthValue = _BmsJarHealthValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 21),
    _BmsJarHealthValue_Type()
)
bmsJarHealthValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsJarHealthValue.setStatus("current")
_BmsJarHealthEvent_Type = DisplayString
_BmsJarHealthEvent_Object = MibTableColumn
bmsJarHealthEvent = _BmsJarHealthEvent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 22),
    _BmsJarHealthEvent_Type()
)
bmsJarHealthEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsJarHealthEvent.setStatus("current")
_BmsCombined_Type = DisplayString
_BmsCombined_Object = MibTableColumn
bmsCombined = _BmsCombined_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 1, 1, 23),
    _BmsCombined_Type()
)
bmsCombined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmsCombined.setStatus("current")
_BmsJarStatusTable_Object = MibTable
bmsJarStatusTable = _BmsJarStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 2)
)
if mibBuilder.loadTexts:
    bmsJarStatusTable.setStatus("current")
_BmJarStatusEntry_Object = MibTableRow
bmJarStatusEntry = _BmJarStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 2, 1)
)
bmJarStatusEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmjsIndexBM"),
    (0, "SITEBOSS-350-STD-MIB", "bmjsIndexJar"),
)
if mibBuilder.loadTexts:
    bmJarStatusEntry.setStatus("current")


class _BmjsIndexBM_Type(Integer32):
    """Custom type bmjsIndexBM based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmjsIndexBM_Type.__name__ = "Integer32"
_BmjsIndexBM_Object = MibTableColumn
bmjsIndexBM = _BmjsIndexBM_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 2, 1, 1),
    _BmjsIndexBM_Type()
)
bmjsIndexBM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmjsIndexBM.setStatus("current")


class _BmjsIndexJar_Type(Integer32):
    """Custom type bmjsIndexJar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_BmjsIndexJar_Type.__name__ = "Integer32"
_BmjsIndexJar_Object = MibTableColumn
bmjsIndexJar = _BmjsIndexJar_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 2, 1, 2),
    _BmjsIndexJar_Type()
)
bmjsIndexJar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmjsIndexJar.setStatus("current")
_BmjsVoltageValue_Type = DisplayString
_BmjsVoltageValue_Object = MibTableColumn
bmjsVoltageValue = _BmjsVoltageValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 2, 1, 3),
    _BmjsVoltageValue_Type()
)
bmjsVoltageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmjsVoltageValue.setStatus("current")
_BmjsTempValue_Type = DisplayString
_BmjsTempValue_Object = MibTableColumn
bmjsTempValue = _BmjsTempValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 2, 1, 4),
    _BmjsTempValue_Type()
)
bmjsTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmjsTempValue.setStatus("current")
_BmjsAdmittanceValue_Type = Integer32
_BmjsAdmittanceValue_Object = MibTableColumn
bmjsAdmittanceValue = _BmjsAdmittanceValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 2, 1, 5),
    _BmjsAdmittanceValue_Type()
)
bmjsAdmittanceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmjsAdmittanceValue.setStatus("current")
_BmjsAdmittanceChangeValue_Type = Integer32
_BmjsAdmittanceChangeValue_Object = MibTableColumn
bmjsAdmittanceChangeValue = _BmjsAdmittanceChangeValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 1, 10, 2, 1, 6),
    _BmjsAdmittanceChangeValue_Type()
)
bmjsAdmittanceChangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmjsAdmittanceChangeValue.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2)
)
_EventSensorBasics_ObjectIdentity = ObjectIdentity
eventSensorBasics = _EventSensorBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1)
)
_EsNumberEventSensors_Type = Integer32
_EsNumberEventSensors_Object = MibScalar
esNumberEventSensors = _EsNumberEventSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 1),
    _EsNumberEventSensors_Type()
)
esNumberEventSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberEventSensors.setStatus("current")
_EsTable_Object = MibTable
esTable = _EsTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2)
)
if mibBuilder.loadTexts:
    esTable.setStatus("current")
_EsEntry_Object = MibTableRow
esEntry = _EsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1)
)
esEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "esIndex"),
)
if mibBuilder.loadTexts:
    esEntry.setStatus("current")


class _EsIndex_Type(Integer32):
    """Custom type esIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EsIndex_Type.__name__ = "Integer32"
_EsIndex_Object = MibTableColumn
esIndex = _EsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 1),
    _EsIndex_Type()
)
esIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndex.setStatus("current")
_EsName_Type = DisplayString
_EsName_Object = MibTableColumn
esName = _EsName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 2),
    _EsName_Type()
)
esName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esName.setStatus("current")
_EsID_Type = DisplayString
_EsID_Object = MibTableColumn
esID = _EsID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 3),
    _EsID_Type()
)
esID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esID.setStatus("current")
_EsNumberTempSensors_Type = Integer32
_EsNumberTempSensors_Object = MibTableColumn
esNumberTempSensors = _EsNumberTempSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 4),
    _EsNumberTempSensors_Type()
)
esNumberTempSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberTempSensors.setStatus("current")
_EsTempReportingMode_Type = DisplayString
_EsTempReportingMode_Object = MibTableColumn
esTempReportingMode = _EsTempReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 5),
    _EsTempReportingMode_Type()
)
esTempReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTempReportingMode.setStatus("current")
_EsNumberCCs_Type = Integer32
_EsNumberCCs_Object = MibTableColumn
esNumberCCs = _EsNumberCCs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 6),
    _EsNumberCCs_Type()
)
esNumberCCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberCCs.setStatus("current")
_EsCCReportingMode_Type = DisplayString
_EsCCReportingMode_Object = MibTableColumn
esCCReportingMode = _EsCCReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 7),
    _EsCCReportingMode_Type()
)
esCCReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCReportingMode.setStatus("current")
_EsNumberHumidSensors_Type = Integer32
_EsNumberHumidSensors_Object = MibTableColumn
esNumberHumidSensors = _EsNumberHumidSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 8),
    _EsNumberHumidSensors_Type()
)
esNumberHumidSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberHumidSensors.setStatus("current")
_EsHumidReportingMode_Type = DisplayString
_EsHumidReportingMode_Object = MibTableColumn
esHumidReportingMode = _EsHumidReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 9),
    _EsHumidReportingMode_Type()
)
esHumidReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esHumidReportingMode.setStatus("current")
_EsNumberNoiseSensors_Type = Integer32
_EsNumberNoiseSensors_Object = MibTableColumn
esNumberNoiseSensors = _EsNumberNoiseSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 10),
    _EsNumberNoiseSensors_Type()
)
esNumberNoiseSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberNoiseSensors.setStatus("current")
_EsNoiseReportingMode_Type = DisplayString
_EsNoiseReportingMode_Object = MibTableColumn
esNoiseReportingMode = _EsNoiseReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 11),
    _EsNoiseReportingMode_Type()
)
esNoiseReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNoiseReportingMode.setStatus("current")
_EsNumberAirflowSensors_Type = Integer32
_EsNumberAirflowSensors_Object = MibTableColumn
esNumberAirflowSensors = _EsNumberAirflowSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 12),
    _EsNumberAirflowSensors_Type()
)
esNumberAirflowSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberAirflowSensors.setStatus("current")
_EsAirflowReportingMode_Type = DisplayString
_EsAirflowReportingMode_Object = MibTableColumn
esAirflowReportingMode = _EsAirflowReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 13),
    _EsAirflowReportingMode_Type()
)
esAirflowReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAirflowReportingMode.setStatus("current")
_EsNumberAnalog_Type = Integer32
_EsNumberAnalog_Object = MibTableColumn
esNumberAnalog = _EsNumberAnalog_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 14),
    _EsNumberAnalog_Type()
)
esNumberAnalog.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberAnalog.setStatus("current")
_EsAnalogReportingMode_Type = DisplayString
_EsAnalogReportingMode_Object = MibTableColumn
esAnalogReportingMode = _EsAnalogReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 15),
    _EsAnalogReportingMode_Type()
)
esAnalogReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogReportingMode.setStatus("current")
_EsNumberOutputs_Type = Integer32
_EsNumberOutputs_Object = MibTableColumn
esNumberOutputs = _EsNumberOutputs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 16),
    _EsNumberOutputs_Type()
)
esNumberOutputs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberOutputs.setStatus("current")
_EsOutputReportingMode_Type = DisplayString
_EsOutputReportingMode_Object = MibTableColumn
esOutputReportingMode = _EsOutputReportingMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 17),
    _EsOutputReportingMode_Type()
)
esOutputReportingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esOutputReportingMode.setStatus("current")
_EsTempCombinedStatus_Type = DisplayString
_EsTempCombinedStatus_Object = MibTableColumn
esTempCombinedStatus = _EsTempCombinedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 18),
    _EsTempCombinedStatus_Type()
)
esTempCombinedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esTempCombinedStatus.setStatus("current")
_EsCCCombinedStatusBlock1_Type = DisplayString
_EsCCCombinedStatusBlock1_Object = MibTableColumn
esCCCombinedStatusBlock1 = _EsCCCombinedStatusBlock1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 19),
    _EsCCCombinedStatusBlock1_Type()
)
esCCCombinedStatusBlock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock1.setStatus("current")
_EsCCCombinedStatusBlock2_Type = DisplayString
_EsCCCombinedStatusBlock2_Object = MibTableColumn
esCCCombinedStatusBlock2 = _EsCCCombinedStatusBlock2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 20),
    _EsCCCombinedStatusBlock2_Type()
)
esCCCombinedStatusBlock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock2.setStatus("current")
_EsCCCombinedStatusBlock3_Type = DisplayString
_EsCCCombinedStatusBlock3_Object = MibTableColumn
esCCCombinedStatusBlock3 = _EsCCCombinedStatusBlock3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 21),
    _EsCCCombinedStatusBlock3_Type()
)
esCCCombinedStatusBlock3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock3.setStatus("current")
_EsCCCombinedStatusBlock4_Type = DisplayString
_EsCCCombinedStatusBlock4_Object = MibTableColumn
esCCCombinedStatusBlock4 = _EsCCCombinedStatusBlock4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 22),
    _EsCCCombinedStatusBlock4_Type()
)
esCCCombinedStatusBlock4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock4.setStatus("current")
_EsCCCombinedStatusBlock5_Type = DisplayString
_EsCCCombinedStatusBlock5_Object = MibTableColumn
esCCCombinedStatusBlock5 = _EsCCCombinedStatusBlock5_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 23),
    _EsCCCombinedStatusBlock5_Type()
)
esCCCombinedStatusBlock5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock5.setStatus("current")
_EsCCCombinedStatusBlock6_Type = DisplayString
_EsCCCombinedStatusBlock6_Object = MibTableColumn
esCCCombinedStatusBlock6 = _EsCCCombinedStatusBlock6_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 24),
    _EsCCCombinedStatusBlock6_Type()
)
esCCCombinedStatusBlock6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock6.setStatus("current")
_EsCCCombinedStatusBlock7_Type = DisplayString
_EsCCCombinedStatusBlock7_Object = MibTableColumn
esCCCombinedStatusBlock7 = _EsCCCombinedStatusBlock7_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 25),
    _EsCCCombinedStatusBlock7_Type()
)
esCCCombinedStatusBlock7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock7.setStatus("current")
_EsCCCombinedStatusBlock8_Type = DisplayString
_EsCCCombinedStatusBlock8_Object = MibTableColumn
esCCCombinedStatusBlock8 = _EsCCCombinedStatusBlock8_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 26),
    _EsCCCombinedStatusBlock8_Type()
)
esCCCombinedStatusBlock8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esCCCombinedStatusBlock8.setStatus("current")
_EsHumidCombinedStatus_Type = DisplayString
_EsHumidCombinedStatus_Object = MibTableColumn
esHumidCombinedStatus = _EsHumidCombinedStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 27),
    _EsHumidCombinedStatus_Type()
)
esHumidCombinedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esHumidCombinedStatus.setStatus("current")
_EsAnalogCombinedStatusBlock1_Type = DisplayString
_EsAnalogCombinedStatusBlock1_Object = MibTableColumn
esAnalogCombinedStatusBlock1 = _EsAnalogCombinedStatusBlock1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 28),
    _EsAnalogCombinedStatusBlock1_Type()
)
esAnalogCombinedStatusBlock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock1.setStatus("current")
_EsAnalogCombinedStatusBlock2_Type = DisplayString
_EsAnalogCombinedStatusBlock2_Object = MibTableColumn
esAnalogCombinedStatusBlock2 = _EsAnalogCombinedStatusBlock2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 29),
    _EsAnalogCombinedStatusBlock2_Type()
)
esAnalogCombinedStatusBlock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock2.setStatus("current")
_EsAnalogCombinedStatusBlock3_Type = DisplayString
_EsAnalogCombinedStatusBlock3_Object = MibTableColumn
esAnalogCombinedStatusBlock3 = _EsAnalogCombinedStatusBlock3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 30),
    _EsAnalogCombinedStatusBlock3_Type()
)
esAnalogCombinedStatusBlock3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock3.setStatus("current")
_EsAnalogCombinedStatusBlock4_Type = DisplayString
_EsAnalogCombinedStatusBlock4_Object = MibTableColumn
esAnalogCombinedStatusBlock4 = _EsAnalogCombinedStatusBlock4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 31),
    _EsAnalogCombinedStatusBlock4_Type()
)
esAnalogCombinedStatusBlock4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock4.setStatus("current")
_EsAnalogCombinedStatusBlock5_Type = DisplayString
_EsAnalogCombinedStatusBlock5_Object = MibTableColumn
esAnalogCombinedStatusBlock5 = _EsAnalogCombinedStatusBlock5_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 32),
    _EsAnalogCombinedStatusBlock5_Type()
)
esAnalogCombinedStatusBlock5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock5.setStatus("current")
_EsAnalogCombinedStatusBlock6_Type = DisplayString
_EsAnalogCombinedStatusBlock6_Object = MibTableColumn
esAnalogCombinedStatusBlock6 = _EsAnalogCombinedStatusBlock6_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 33),
    _EsAnalogCombinedStatusBlock6_Type()
)
esAnalogCombinedStatusBlock6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esAnalogCombinedStatusBlock6.setStatus("current")
_EsOutputCombinedStatusBlock1_Type = DisplayString
_EsOutputCombinedStatusBlock1_Object = MibTableColumn
esOutputCombinedStatusBlock1 = _EsOutputCombinedStatusBlock1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 34),
    _EsOutputCombinedStatusBlock1_Type()
)
esOutputCombinedStatusBlock1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esOutputCombinedStatusBlock1.setStatus("current")
_EsOutputCombinedStatusBlock2_Type = DisplayString
_EsOutputCombinedStatusBlock2_Object = MibTableColumn
esOutputCombinedStatusBlock2 = _EsOutputCombinedStatusBlock2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 2, 1, 35),
    _EsOutputCombinedStatusBlock2_Type()
)
esOutputCombinedStatusBlock2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esOutputCombinedStatusBlock2.setStatus("current")
_EsNewSensors_Type = DisplayString
_EsNewSensors_Object = MibScalar
esNewSensors = _EsNewSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 1, 3),
    _EsNewSensors_Type()
)
esNewSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNewSensors.setStatus("current")
_EventSensorPointConfig_ObjectIdentity = ObjectIdentity
eventSensorPointConfig = _EventSensorPointConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2)
)
_EsPointConfigTempTable_Object = MibTable
esPointConfigTempTable = _EsPointConfigTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1)
)
if mibBuilder.loadTexts:
    esPointConfigTempTable.setStatus("current")
_EsPointConfigTempEntry_Object = MibTableRow
esPointConfigTempEntry = _EsPointConfigTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1)
)
esPointConfigTempEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "espcTempIndexES"),
    (0, "SITEBOSS-350-STD-MIB", "espcTempIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigTempEntry.setStatus("current")


class _EspcTempIndexES_Type(Integer32):
    """Custom type espcTempIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcTempIndexES_Type.__name__ = "Integer32"
_EspcTempIndexES_Object = MibTableColumn
espcTempIndexES = _EspcTempIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 1),
    _EspcTempIndexES_Type()
)
espcTempIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcTempIndexES.setStatus("current")


class _EspcTempIndexPoint_Type(Integer32):
    """Custom type espcTempIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcTempIndexPoint_Type.__name__ = "Integer32"
_EspcTempIndexPoint_Object = MibTableColumn
espcTempIndexPoint = _EspcTempIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 2),
    _EspcTempIndexPoint_Type()
)
espcTempIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcTempIndexPoint.setStatus("current")
_EspcTempEnable_Type = DisplayString
_EspcTempEnable_Object = MibTableColumn
espcTempEnable = _EspcTempEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 3),
    _EspcTempEnable_Type()
)
espcTempEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempEnable.setStatus("current")
_EspcTempScale_Type = DisplayString
_EspcTempScale_Object = MibTableColumn
espcTempScale = _EspcTempScale_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 4),
    _EspcTempScale_Type()
)
espcTempScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempScale.setStatus("current")
_EspcTempDeadband_Type = DisplayString
_EspcTempDeadband_Object = MibTableColumn
espcTempDeadband = _EspcTempDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 5),
    _EspcTempDeadband_Type()
)
espcTempDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempDeadband.setStatus("current")
_EspcTempVHighTemp_Type = DisplayString
_EspcTempVHighTemp_Object = MibTableColumn
espcTempVHighTemp = _EspcTempVHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 6),
    _EspcTempVHighTemp_Type()
)
espcTempVHighTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVHighTemp.setStatus("current")
_EspcTempVHighActions_Type = DisplayString
_EspcTempVHighActions_Object = MibTableColumn
espcTempVHighActions = _EspcTempVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 7),
    _EspcTempVHighActions_Type()
)
espcTempVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVHighActions.setStatus("current")
_EspcTempVHighTrapnum_Type = Integer32
_EspcTempVHighTrapnum_Object = MibTableColumn
espcTempVHighTrapnum = _EspcTempVHighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 8),
    _EspcTempVHighTrapnum_Type()
)
espcTempVHighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVHighTrapnum.setStatus("current")
_EspcTempVHighClass_Type = DisplayString
_EspcTempVHighClass_Object = MibTableColumn
espcTempVHighClass = _EspcTempVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 9),
    _EspcTempVHighClass_Type()
)
espcTempVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVHighClass.setStatus("current")
_EspcTempHighTemp_Type = DisplayString
_EspcTempHighTemp_Object = MibTableColumn
espcTempHighTemp = _EspcTempHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 10),
    _EspcTempHighTemp_Type()
)
espcTempHighTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempHighTemp.setStatus("current")
_EspcTempHighActions_Type = DisplayString
_EspcTempHighActions_Object = MibTableColumn
espcTempHighActions = _EspcTempHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 11),
    _EspcTempHighActions_Type()
)
espcTempHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempHighActions.setStatus("current")
_EspcTempHighTrapnum_Type = Integer32
_EspcTempHighTrapnum_Object = MibTableColumn
espcTempHighTrapnum = _EspcTempHighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 12),
    _EspcTempHighTrapnum_Type()
)
espcTempHighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempHighTrapnum.setStatus("current")
_EspcTempHighClass_Type = DisplayString
_EspcTempHighClass_Object = MibTableColumn
espcTempHighClass = _EspcTempHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 13),
    _EspcTempHighClass_Type()
)
espcTempHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempHighClass.setStatus("current")
_EspcTempNormalActions_Type = DisplayString
_EspcTempNormalActions_Object = MibTableColumn
espcTempNormalActions = _EspcTempNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 14),
    _EspcTempNormalActions_Type()
)
espcTempNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempNormalActions.setStatus("current")
_EspcTempNormalTrapnum_Type = Integer32
_EspcTempNormalTrapnum_Object = MibTableColumn
espcTempNormalTrapnum = _EspcTempNormalTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 15),
    _EspcTempNormalTrapnum_Type()
)
espcTempNormalTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempNormalTrapnum.setStatus("current")
_EspcTempNormalClass_Type = DisplayString
_EspcTempNormalClass_Object = MibTableColumn
espcTempNormalClass = _EspcTempNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 16),
    _EspcTempNormalClass_Type()
)
espcTempNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempNormalClass.setStatus("current")
_EspcTempLowTemp_Type = DisplayString
_EspcTempLowTemp_Object = MibTableColumn
espcTempLowTemp = _EspcTempLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 17),
    _EspcTempLowTemp_Type()
)
espcTempLowTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempLowTemp.setStatus("current")
_EspcTempLowActions_Type = DisplayString
_EspcTempLowActions_Object = MibTableColumn
espcTempLowActions = _EspcTempLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 18),
    _EspcTempLowActions_Type()
)
espcTempLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempLowActions.setStatus("current")
_EspcTempLowTrapnum_Type = Integer32
_EspcTempLowTrapnum_Object = MibTableColumn
espcTempLowTrapnum = _EspcTempLowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 19),
    _EspcTempLowTrapnum_Type()
)
espcTempLowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempLowTrapnum.setStatus("current")
_EspcTempLowClass_Type = DisplayString
_EspcTempLowClass_Object = MibTableColumn
espcTempLowClass = _EspcTempLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 20),
    _EspcTempLowClass_Type()
)
espcTempLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempLowClass.setStatus("current")
_EspcTempVLowTemp_Type = DisplayString
_EspcTempVLowTemp_Object = MibTableColumn
espcTempVLowTemp = _EspcTempVLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 21),
    _EspcTempVLowTemp_Type()
)
espcTempVLowTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVLowTemp.setStatus("current")
_EspcTempVLowActions_Type = DisplayString
_EspcTempVLowActions_Object = MibTableColumn
espcTempVLowActions = _EspcTempVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 22),
    _EspcTempVLowActions_Type()
)
espcTempVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVLowActions.setStatus("current")
_EspcTempVLowTrapnum_Type = Integer32
_EspcTempVLowTrapnum_Object = MibTableColumn
espcTempVLowTrapnum = _EspcTempVLowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 23),
    _EspcTempVLowTrapnum_Type()
)
espcTempVLowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVLowTrapnum.setStatus("current")
_EspcTempVLowClass_Type = DisplayString
_EspcTempVLowClass_Object = MibTableColumn
espcTempVLowClass = _EspcTempVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 1, 1, 24),
    _EspcTempVLowClass_Type()
)
espcTempVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVLowClass.setStatus("current")
_EsPointConfigCCTable_Object = MibTable
esPointConfigCCTable = _EsPointConfigCCTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2)
)
if mibBuilder.loadTexts:
    esPointConfigCCTable.setStatus("current")
_EsPointConfigCCEntry_Object = MibTableRow
esPointConfigCCEntry = _EsPointConfigCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1)
)
esPointConfigCCEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "espcCCIndexES"),
    (0, "SITEBOSS-350-STD-MIB", "espcCCIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigCCEntry.setStatus("current")


class _EspcCCIndexES_Type(Integer32):
    """Custom type espcCCIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcCCIndexES_Type.__name__ = "Integer32"
_EspcCCIndexES_Object = MibTableColumn
espcCCIndexES = _EspcCCIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 1),
    _EspcCCIndexES_Type()
)
espcCCIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcCCIndexES.setStatus("current")


class _EspcCCIndexPoint_Type(Integer32):
    """Custom type espcCCIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcCCIndexPoint_Type.__name__ = "Integer32"
_EspcCCIndexPoint_Object = MibTableColumn
espcCCIndexPoint = _EspcCCIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 2),
    _EspcCCIndexPoint_Type()
)
espcCCIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcCCIndexPoint.setStatus("current")
_EspcCCEnable_Type = DisplayString
_EspcCCEnable_Object = MibTableColumn
espcCCEnable = _EspcCCEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 3),
    _EspcCCEnable_Type()
)
espcCCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEnable.setStatus("current")
_EspcCCName_Type = DisplayString
_EspcCCName_Object = MibTableColumn
espcCCName = _EspcCCName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 4),
    _EspcCCName_Type()
)
espcCCName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCName.setStatus("current")
_EspcCCEventState_Type = DisplayString
_EspcCCEventState_Object = MibTableColumn
espcCCEventState = _EspcCCEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 5),
    _EspcCCEventState_Type()
)
espcCCEventState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEventState.setStatus("current")


class _EspcCCThreshold_Type(Integer32):
    """Custom type espcCCThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EspcCCThreshold_Type.__name__ = "Integer32"
_EspcCCThreshold_Object = MibTableColumn
espcCCThreshold = _EspcCCThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 6),
    _EspcCCThreshold_Type()
)
espcCCThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCThreshold.setStatus("current")
_EspcCCEventActions_Type = DisplayString
_EspcCCEventActions_Object = MibTableColumn
espcCCEventActions = _EspcCCEventActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 7),
    _EspcCCEventActions_Type()
)
espcCCEventActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEventActions.setStatus("current")
_EspcCCEventTrapnum_Type = Integer32
_EspcCCEventTrapnum_Object = MibTableColumn
espcCCEventTrapnum = _EspcCCEventTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 8),
    _EspcCCEventTrapnum_Type()
)
espcCCEventTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEventTrapnum.setStatus("current")
_EspcCCEventClass_Type = DisplayString
_EspcCCEventClass_Object = MibTableColumn
espcCCEventClass = _EspcCCEventClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 9),
    _EspcCCEventClass_Type()
)
espcCCEventClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEventClass.setStatus("current")
_EspcCCNormalActions_Type = DisplayString
_EspcCCNormalActions_Object = MibTableColumn
espcCCNormalActions = _EspcCCNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 10),
    _EspcCCNormalActions_Type()
)
espcCCNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalActions.setStatus("current")
_EspcCCNormalTrapnum_Type = Integer32
_EspcCCNormalTrapnum_Object = MibTableColumn
espcCCNormalTrapnum = _EspcCCNormalTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 11),
    _EspcCCNormalTrapnum_Type()
)
espcCCNormalTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalTrapnum.setStatus("current")
_EspcCCNormalClass_Type = DisplayString
_EspcCCNormalClass_Object = MibTableColumn
espcCCNormalClass = _EspcCCNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 12),
    _EspcCCNormalClass_Type()
)
espcCCNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalClass.setStatus("current")
_EspcCCAlarmAlias_Type = DisplayString
_EspcCCAlarmAlias_Object = MibTableColumn
espcCCAlarmAlias = _EspcCCAlarmAlias_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 13),
    _EspcCCAlarmAlias_Type()
)
espcCCAlarmAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCAlarmAlias.setStatus("current")
_EspcCCNormalAlias_Type = DisplayString
_EspcCCNormalAlias_Object = MibTableColumn
espcCCNormalAlias = _EspcCCNormalAlias_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 14),
    _EspcCCNormalAlias_Type()
)
espcCCNormalAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalAlias.setStatus("current")


class _EspcCCNormalThreshold_Type(Integer32):
    """Custom type espcCCNormalThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EspcCCNormalThreshold_Type.__name__ = "Integer32"
_EspcCCNormalThreshold_Object = MibTableColumn
espcCCNormalThreshold = _EspcCCNormalThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 15),
    _EspcCCNormalThreshold_Type()
)
espcCCNormalThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalThreshold.setStatus("current")
_EspcCCOverrideGlobalReminder_Type = DisplayString
_EspcCCOverrideGlobalReminder_Object = MibTableColumn
espcCCOverrideGlobalReminder = _EspcCCOverrideGlobalReminder_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 16),
    _EspcCCOverrideGlobalReminder_Type()
)
espcCCOverrideGlobalReminder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCOverrideGlobalReminder.setStatus("current")
_EspcCCReminderInterval_Type = Integer32
_EspcCCReminderInterval_Object = MibTableColumn
espcCCReminderInterval = _EspcCCReminderInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 2, 1, 17),
    _EspcCCReminderInterval_Type()
)
espcCCReminderInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCReminderInterval.setStatus("current")
_EsPointConfigHumidTable_Object = MibTable
esPointConfigHumidTable = _EsPointConfigHumidTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3)
)
if mibBuilder.loadTexts:
    esPointConfigHumidTable.setStatus("current")
_EsPointConfigHumidEntry_Object = MibTableRow
esPointConfigHumidEntry = _EsPointConfigHumidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1)
)
esPointConfigHumidEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "espcHumidIndexES"),
    (0, "SITEBOSS-350-STD-MIB", "espcHumidIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigHumidEntry.setStatus("current")


class _EspcHumidIndexES_Type(Integer32):
    """Custom type espcHumidIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcHumidIndexES_Type.__name__ = "Integer32"
_EspcHumidIndexES_Object = MibTableColumn
espcHumidIndexES = _EspcHumidIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 1),
    _EspcHumidIndexES_Type()
)
espcHumidIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcHumidIndexES.setStatus("current")


class _EspcHumidIndexPoint_Type(Integer32):
    """Custom type espcHumidIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcHumidIndexPoint_Type.__name__ = "Integer32"
_EspcHumidIndexPoint_Object = MibTableColumn
espcHumidIndexPoint = _EspcHumidIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 2),
    _EspcHumidIndexPoint_Type()
)
espcHumidIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcHumidIndexPoint.setStatus("current")
_EspcHumidEnable_Type = DisplayString
_EspcHumidEnable_Object = MibTableColumn
espcHumidEnable = _EspcHumidEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 3),
    _EspcHumidEnable_Type()
)
espcHumidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidEnable.setStatus("current")
_EspcHumidDeadband_Type = Integer32
_EspcHumidDeadband_Object = MibTableColumn
espcHumidDeadband = _EspcHumidDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 4),
    _EspcHumidDeadband_Type()
)
espcHumidDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidDeadband.setStatus("current")
_EspcHumidVHighHumid_Type = Integer32
_EspcHumidVHighHumid_Object = MibTableColumn
espcHumidVHighHumid = _EspcHumidVHighHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 5),
    _EspcHumidVHighHumid_Type()
)
espcHumidVHighHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVHighHumid.setStatus("current")
_EspcHumidVHighActions_Type = DisplayString
_EspcHumidVHighActions_Object = MibTableColumn
espcHumidVHighActions = _EspcHumidVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 6),
    _EspcHumidVHighActions_Type()
)
espcHumidVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVHighActions.setStatus("current")
_EspcHumidVHighTrapnum_Type = Integer32
_EspcHumidVHighTrapnum_Object = MibTableColumn
espcHumidVHighTrapnum = _EspcHumidVHighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 7),
    _EspcHumidVHighTrapnum_Type()
)
espcHumidVHighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVHighTrapnum.setStatus("current")
_EspcHumidVHighClass_Type = DisplayString
_EspcHumidVHighClass_Object = MibTableColumn
espcHumidVHighClass = _EspcHumidVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 8),
    _EspcHumidVHighClass_Type()
)
espcHumidVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVHighClass.setStatus("current")
_EspcHumidHighHumid_Type = Integer32
_EspcHumidHighHumid_Object = MibTableColumn
espcHumidHighHumid = _EspcHumidHighHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 9),
    _EspcHumidHighHumid_Type()
)
espcHumidHighHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidHighHumid.setStatus("current")
_EspcHumidHighActions_Type = DisplayString
_EspcHumidHighActions_Object = MibTableColumn
espcHumidHighActions = _EspcHumidHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 10),
    _EspcHumidHighActions_Type()
)
espcHumidHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidHighActions.setStatus("current")
_EspcHumidHighTrapnum_Type = Integer32
_EspcHumidHighTrapnum_Object = MibTableColumn
espcHumidHighTrapnum = _EspcHumidHighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 11),
    _EspcHumidHighTrapnum_Type()
)
espcHumidHighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidHighTrapnum.setStatus("current")
_EspcHumidHighClass_Type = DisplayString
_EspcHumidHighClass_Object = MibTableColumn
espcHumidHighClass = _EspcHumidHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 12),
    _EspcHumidHighClass_Type()
)
espcHumidHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidHighClass.setStatus("current")
_EspcHumidNormalActions_Type = DisplayString
_EspcHumidNormalActions_Object = MibTableColumn
espcHumidNormalActions = _EspcHumidNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 13),
    _EspcHumidNormalActions_Type()
)
espcHumidNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidNormalActions.setStatus("current")
_EspcHumidNormalTrapnum_Type = Integer32
_EspcHumidNormalTrapnum_Object = MibTableColumn
espcHumidNormalTrapnum = _EspcHumidNormalTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 14),
    _EspcHumidNormalTrapnum_Type()
)
espcHumidNormalTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidNormalTrapnum.setStatus("current")
_EspcHumidNormalClass_Type = DisplayString
_EspcHumidNormalClass_Object = MibTableColumn
espcHumidNormalClass = _EspcHumidNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 15),
    _EspcHumidNormalClass_Type()
)
espcHumidNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidNormalClass.setStatus("current")
_EspcHumidLowHumid_Type = Integer32
_EspcHumidLowHumid_Object = MibTableColumn
espcHumidLowHumid = _EspcHumidLowHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 16),
    _EspcHumidLowHumid_Type()
)
espcHumidLowHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidLowHumid.setStatus("current")
_EspcHumidLowActions_Type = DisplayString
_EspcHumidLowActions_Object = MibTableColumn
espcHumidLowActions = _EspcHumidLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 17),
    _EspcHumidLowActions_Type()
)
espcHumidLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidLowActions.setStatus("current")
_EspcHumidLowTrapnum_Type = Integer32
_EspcHumidLowTrapnum_Object = MibTableColumn
espcHumidLowTrapnum = _EspcHumidLowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 18),
    _EspcHumidLowTrapnum_Type()
)
espcHumidLowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidLowTrapnum.setStatus("current")
_EspcHumidLowClass_Type = DisplayString
_EspcHumidLowClass_Object = MibTableColumn
espcHumidLowClass = _EspcHumidLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 19),
    _EspcHumidLowClass_Type()
)
espcHumidLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidLowClass.setStatus("current")
_EspcHumidVLowHumid_Type = Integer32
_EspcHumidVLowHumid_Object = MibTableColumn
espcHumidVLowHumid = _EspcHumidVLowHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 20),
    _EspcHumidVLowHumid_Type()
)
espcHumidVLowHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVLowHumid.setStatus("current")
_EspcHumidVLowActions_Type = DisplayString
_EspcHumidVLowActions_Object = MibTableColumn
espcHumidVLowActions = _EspcHumidVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 21),
    _EspcHumidVLowActions_Type()
)
espcHumidVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVLowActions.setStatus("current")
_EspcHumidVLowTrapnum_Type = Integer32
_EspcHumidVLowTrapnum_Object = MibTableColumn
espcHumidVLowTrapnum = _EspcHumidVLowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 22),
    _EspcHumidVLowTrapnum_Type()
)
espcHumidVLowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVLowTrapnum.setStatus("current")
_EspcHumidVLowClass_Type = DisplayString
_EspcHumidVLowClass_Object = MibTableColumn
espcHumidVLowClass = _EspcHumidVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 3, 1, 23),
    _EspcHumidVLowClass_Type()
)
espcHumidVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVLowClass.setStatus("current")
_EsPointConfigAITable_Object = MibTable
esPointConfigAITable = _EsPointConfigAITable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5)
)
if mibBuilder.loadTexts:
    esPointConfigAITable.setStatus("current")
_EsPointConfigAIEntry_Object = MibTableRow
esPointConfigAIEntry = _EsPointConfigAIEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1)
)
esPointConfigAIEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "espcHumidIndexES"),
    (0, "SITEBOSS-350-STD-MIB", "espcHumidIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigAIEntry.setStatus("current")


class _EspcAIIndexES_Type(Integer32):
    """Custom type espcAIIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcAIIndexES_Type.__name__ = "Integer32"
_EspcAIIndexES_Object = MibTableColumn
espcAIIndexES = _EspcAIIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 1),
    _EspcAIIndexES_Type()
)
espcAIIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcAIIndexES.setStatus("current")


class _EspcAIIndexPoint_Type(Integer32):
    """Custom type espcAIIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcAIIndexPoint_Type.__name__ = "Integer32"
_EspcAIIndexPoint_Object = MibTableColumn
espcAIIndexPoint = _EspcAIIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 2),
    _EspcAIIndexPoint_Type()
)
espcAIIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcAIIndexPoint.setStatus("current")
_EspcAIEnable_Type = DisplayString
_EspcAIEnable_Object = MibTableColumn
espcAIEnable = _EspcAIEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 3),
    _EspcAIEnable_Type()
)
espcAIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIEnable.setStatus("current")
_EspcAIDeadband_Type = DisplayString
_EspcAIDeadband_Object = MibTableColumn
espcAIDeadband = _EspcAIDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 5),
    _EspcAIDeadband_Type()
)
espcAIDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIDeadband.setStatus("current")
_EspcAIVhighValue_Type = DisplayString
_EspcAIVhighValue_Object = MibTableColumn
espcAIVhighValue = _EspcAIVhighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 6),
    _EspcAIVhighValue_Type()
)
espcAIVhighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVhighValue.setStatus("current")
_EspcAIVhighActions_Type = DisplayString
_EspcAIVhighActions_Object = MibTableColumn
espcAIVhighActions = _EspcAIVhighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 7),
    _EspcAIVhighActions_Type()
)
espcAIVhighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVhighActions.setStatus("current")
_EspcAIVhighTrapnum_Type = Integer32
_EspcAIVhighTrapnum_Object = MibTableColumn
espcAIVhighTrapnum = _EspcAIVhighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 8),
    _EspcAIVhighTrapnum_Type()
)
espcAIVhighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVhighTrapnum.setStatus("current")
_EspcAIVhighClass_Type = DisplayString
_EspcAIVhighClass_Object = MibTableColumn
espcAIVhighClass = _EspcAIVhighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 9),
    _EspcAIVhighClass_Type()
)
espcAIVhighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVhighClass.setStatus("current")
_EspcAIHighValue_Type = DisplayString
_EspcAIHighValue_Object = MibTableColumn
espcAIHighValue = _EspcAIHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 10),
    _EspcAIHighValue_Type()
)
espcAIHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIHighValue.setStatus("current")
_EspcAIHighActions_Type = DisplayString
_EspcAIHighActions_Object = MibTableColumn
espcAIHighActions = _EspcAIHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 11),
    _EspcAIHighActions_Type()
)
espcAIHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIHighActions.setStatus("current")
_EspcAIHighTrapnum_Type = Integer32
_EspcAIHighTrapnum_Object = MibTableColumn
espcAIHighTrapnum = _EspcAIHighTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 12),
    _EspcAIHighTrapnum_Type()
)
espcAIHighTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIHighTrapnum.setStatus("current")
_EspcAIHighClass_Type = DisplayString
_EspcAIHighClass_Object = MibTableColumn
espcAIHighClass = _EspcAIHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 13),
    _EspcAIHighClass_Type()
)
espcAIHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIHighClass.setStatus("current")
_EspcAINormalActions_Type = DisplayString
_EspcAINormalActions_Object = MibTableColumn
espcAINormalActions = _EspcAINormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 14),
    _EspcAINormalActions_Type()
)
espcAINormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAINormalActions.setStatus("current")
_EspcAINormalTrapnum_Type = Integer32
_EspcAINormalTrapnum_Object = MibTableColumn
espcAINormalTrapnum = _EspcAINormalTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 15),
    _EspcAINormalTrapnum_Type()
)
espcAINormalTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAINormalTrapnum.setStatus("current")
_EspcAINormalClass_Type = DisplayString
_EspcAINormalClass_Object = MibTableColumn
espcAINormalClass = _EspcAINormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 16),
    _EspcAINormalClass_Type()
)
espcAINormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAINormalClass.setStatus("current")
_EspcAILowValue_Type = DisplayString
_EspcAILowValue_Object = MibTableColumn
espcAILowValue = _EspcAILowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 17),
    _EspcAILowValue_Type()
)
espcAILowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAILowValue.setStatus("current")
_EspcAILowActions_Type = DisplayString
_EspcAILowActions_Object = MibTableColumn
espcAILowActions = _EspcAILowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 18),
    _EspcAILowActions_Type()
)
espcAILowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAILowActions.setStatus("current")
_EspcAILowTrapnum_Type = Integer32
_EspcAILowTrapnum_Object = MibTableColumn
espcAILowTrapnum = _EspcAILowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 19),
    _EspcAILowTrapnum_Type()
)
espcAILowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAILowTrapnum.setStatus("current")
_EspcAILowClass_Type = DisplayString
_EspcAILowClass_Object = MibTableColumn
espcAILowClass = _EspcAILowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 20),
    _EspcAILowClass_Type()
)
espcAILowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAILowClass.setStatus("current")
_EspcAIVlowValue_Type = DisplayString
_EspcAIVlowValue_Object = MibTableColumn
espcAIVlowValue = _EspcAIVlowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 21),
    _EspcAIVlowValue_Type()
)
espcAIVlowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVlowValue.setStatus("current")
_EspcAIVlowActions_Type = DisplayString
_EspcAIVlowActions_Object = MibTableColumn
espcAIVlowActions = _EspcAIVlowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 22),
    _EspcAIVlowActions_Type()
)
espcAIVlowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVlowActions.setStatus("current")
_EspcAIVlowTrapnum_Type = Integer32
_EspcAIVlowTrapnum_Object = MibTableColumn
espcAIVlowTrapnum = _EspcAIVlowTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 23),
    _EspcAIVlowTrapnum_Type()
)
espcAIVlowTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVlowTrapnum.setStatus("current")
_EspcAIVlowClass_Type = DisplayString
_EspcAIVlowClass_Object = MibTableColumn
espcAIVlowClass = _EspcAIVlowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 24),
    _EspcAIVlowClass_Type()
)
espcAIVlowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVlowClass.setStatus("current")
_EspcAIConvUnitName_Type = DisplayString
_EspcAIConvUnitName_Object = MibTableColumn
espcAIConvUnitName = _EspcAIConvUnitName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 25),
    _EspcAIConvUnitName_Type()
)
espcAIConvUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvUnitName.setStatus("current")
_EspcAIConvHighValue_Type = DisplayString
_EspcAIConvHighValue_Object = MibTableColumn
espcAIConvHighValue = _EspcAIConvHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 26),
    _EspcAIConvHighValue_Type()
)
espcAIConvHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvHighValue.setStatus("current")
_EspcAIConvHighUnit_Type = DisplayString
_EspcAIConvHighUnit_Object = MibTableColumn
espcAIConvHighUnit = _EspcAIConvHighUnit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 27),
    _EspcAIConvHighUnit_Type()
)
espcAIConvHighUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvHighUnit.setStatus("current")
_EspcAIConvLowValue_Type = DisplayString
_EspcAIConvLowValue_Object = MibTableColumn
espcAIConvLowValue = _EspcAIConvLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 29),
    _EspcAIConvLowValue_Type()
)
espcAIConvLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvLowValue.setStatus("current")
_EspcAIConvLowUnit_Type = DisplayString
_EspcAIConvLowUnit_Object = MibTableColumn
espcAIConvLowUnit = _EspcAIConvLowUnit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 30),
    _EspcAIConvLowUnit_Type()
)
espcAIConvLowUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvLowUnit.setStatus("current")
_EspcAIDisplayFormat_Type = DisplayString
_EspcAIDisplayFormat_Object = MibTableColumn
espcAIDisplayFormat = _EspcAIDisplayFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 5, 1, 32),
    _EspcAIDisplayFormat_Type()
)
espcAIDisplayFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIDisplayFormat.setStatus("current")
_EsPointConfigOutputTable_Object = MibTable
esPointConfigOutputTable = _EsPointConfigOutputTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6)
)
if mibBuilder.loadTexts:
    esPointConfigOutputTable.setStatus("current")
_EsPointConfigOutputEntry_Object = MibTableRow
esPointConfigOutputEntry = _EsPointConfigOutputEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1)
)
esPointConfigOutputEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "espcOutputIndexES"),
    (0, "SITEBOSS-350-STD-MIB", "espcOutputIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigOutputEntry.setStatus("current")


class _EspcOutputIndexES_Type(Integer32):
    """Custom type espcOutputIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcOutputIndexES_Type.__name__ = "Integer32"
_EspcOutputIndexES_Object = MibTableColumn
espcOutputIndexES = _EspcOutputIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 1),
    _EspcOutputIndexES_Type()
)
espcOutputIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcOutputIndexES.setStatus("current")


class _EspcOutputIndexPoint_Type(Integer32):
    """Custom type espcOutputIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcOutputIndexPoint_Type.__name__ = "Integer32"
_EspcOutputIndexPoint_Object = MibTableColumn
espcOutputIndexPoint = _EspcOutputIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 2),
    _EspcOutputIndexPoint_Type()
)
espcOutputIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcOutputIndexPoint.setStatus("current")
_EspcOutputEnable_Type = DisplayString
_EspcOutputEnable_Object = MibTableColumn
espcOutputEnable = _EspcOutputEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 3),
    _EspcOutputEnable_Type()
)
espcOutputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputEnable.setStatus("current")
_EspcOutputActiveState_Type = DisplayString
_EspcOutputActiveState_Object = MibTableColumn
espcOutputActiveState = _EspcOutputActiveState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 4),
    _EspcOutputActiveState_Type()
)
espcOutputActiveState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveState.setStatus("current")
_EspcOutputType_Type = DisplayString
_EspcOutputType_Object = MibTableColumn
espcOutputType = _EspcOutputType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 5),
    _EspcOutputType_Type()
)
espcOutputType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcOutputType.setStatus("current")
_EspcOutputAliasValue_Type = DisplayString
_EspcOutputAliasValue_Object = MibTableColumn
espcOutputAliasValue = _EspcOutputAliasValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 6),
    _EspcOutputAliasValue_Type()
)
espcOutputAliasValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcOutputAliasValue.setStatus("current")
_EspcOutputAliasColor_Type = DisplayString
_EspcOutputAliasColor_Object = MibTableColumn
espcOutputAliasColor = _EspcOutputAliasColor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 7),
    _EspcOutputAliasColor_Type()
)
espcOutputAliasColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcOutputAliasColor.setStatus("current")
_EspcOutputActiveAlias_Type = DisplayString
_EspcOutputActiveAlias_Object = MibTableColumn
espcOutputActiveAlias = _EspcOutputActiveAlias_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 10),
    _EspcOutputActiveAlias_Type()
)
espcOutputActiveAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveAlias.setStatus("current")
_EspcOutputActiveColor_Type = DisplayString
_EspcOutputActiveColor_Object = MibTableColumn
espcOutputActiveColor = _EspcOutputActiveColor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 11),
    _EspcOutputActiveColor_Type()
)
espcOutputActiveColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveColor.setStatus("current")
_EspcOutputActiveActions_Type = DisplayString
_EspcOutputActiveActions_Object = MibTableColumn
espcOutputActiveActions = _EspcOutputActiveActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 12),
    _EspcOutputActiveActions_Type()
)
espcOutputActiveActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveActions.setStatus("current")


class _EspcOutputActiveTrapnum_Type(Integer32):
    """Custom type espcOutputActiveTrapnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 1199),
    )


_EspcOutputActiveTrapnum_Type.__name__ = "Integer32"
_EspcOutputActiveTrapnum_Object = MibTableColumn
espcOutputActiveTrapnum = _EspcOutputActiveTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 13),
    _EspcOutputActiveTrapnum_Type()
)
espcOutputActiveTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveTrapnum.setStatus("current")
_EspcOutputActiveClass_Type = DisplayString
_EspcOutputActiveClass_Object = MibTableColumn
espcOutputActiveClass = _EspcOutputActiveClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 14),
    _EspcOutputActiveClass_Type()
)
espcOutputActiveClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputActiveClass.setStatus("current")
_EspcOutputInactiveAlias_Type = DisplayString
_EspcOutputInactiveAlias_Object = MibTableColumn
espcOutputInactiveAlias = _EspcOutputInactiveAlias_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 20),
    _EspcOutputInactiveAlias_Type()
)
espcOutputInactiveAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputInactiveAlias.setStatus("current")
_EspcOutputInactiveColor_Type = DisplayString
_EspcOutputInactiveColor_Object = MibTableColumn
espcOutputInactiveColor = _EspcOutputInactiveColor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 21),
    _EspcOutputInactiveColor_Type()
)
espcOutputInactiveColor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputInactiveColor.setStatus("current")
_EspcOutputInactiveActions_Type = DisplayString
_EspcOutputInactiveActions_Object = MibTableColumn
espcOutputInactiveActions = _EspcOutputInactiveActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 22),
    _EspcOutputInactiveActions_Type()
)
espcOutputInactiveActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputInactiveActions.setStatus("current")


class _EspcOutputInactiveTrapnum_Type(Integer32):
    """Custom type espcOutputInactiveTrapnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 1199),
    )


_EspcOutputInactiveTrapnum_Type.__name__ = "Integer32"
_EspcOutputInactiveTrapnum_Object = MibTableColumn
espcOutputInactiveTrapnum = _EspcOutputInactiveTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 23),
    _EspcOutputInactiveTrapnum_Type()
)
espcOutputInactiveTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputInactiveTrapnum.setStatus("current")
_EspcOutputInactiveClass_Type = DisplayString
_EspcOutputInactiveClass_Object = MibTableColumn
espcOutputInactiveClass = _EspcOutputInactiveClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 2, 6, 1, 24),
    _EspcOutputInactiveClass_Type()
)
espcOutputInactiveClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcOutputInactiveClass.setStatus("current")
_SerialPorts_ObjectIdentity = ObjectIdentity
serialPorts = _SerialPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3)
)
_NumberPorts_Type = Integer32
_NumberPorts_Object = MibScalar
numberPorts = _NumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 1),
    _NumberPorts_Type()
)
numberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberPorts.setStatus("current")
_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 2)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("current")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 2, 1)
)
portConfigEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "portConfigIndex"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("current")


class _PortConfigIndex_Type(Integer32):
    """Custom type portConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_PortConfigIndex_Type.__name__ = "Integer32"
_PortConfigIndex_Object = MibTableColumn
portConfigIndex = _PortConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 2, 1, 1),
    _PortConfigIndex_Type()
)
portConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portConfigIndex.setStatus("current")
_PortConfigBaud_Type = Integer32
_PortConfigBaud_Object = MibTableColumn
portConfigBaud = _PortConfigBaud_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 2, 1, 2),
    _PortConfigBaud_Type()
)
portConfigBaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigBaud.setStatus("current")
_PortConfigDataFormat_Type = Integer32
_PortConfigDataFormat_Object = MibTableColumn
portConfigDataFormat = _PortConfigDataFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 2, 1, 3),
    _PortConfigDataFormat_Type()
)
portConfigDataFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDataFormat.setStatus("current")
_PortConfigStripPtOutputLfs_Type = Integer32
_PortConfigStripPtOutputLfs_Object = MibTableColumn
portConfigStripPtOutputLfs = _PortConfigStripPtOutputLfs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 2, 1, 4),
    _PortConfigStripPtOutputLfs_Type()
)
portConfigStripPtOutputLfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigStripPtOutputLfs.setStatus("current")
_PortConfigStripPtInputLfs_Type = Integer32
_PortConfigStripPtInputLfs_Object = MibTableColumn
portConfigStripPtInputLfs = _PortConfigStripPtInputLfs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 2, 1, 5),
    _PortConfigStripPtInputLfs_Type()
)
portConfigStripPtInputLfs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigStripPtInputLfs.setStatus("current")
_PortConfigId_Type = DisplayString
_PortConfigId_Object = MibTableColumn
portConfigId = _PortConfigId_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 2, 1, 27),
    _PortConfigId_Type()
)
portConfigId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigId.setStatus("current")
_PortConfigMode_Type = DisplayString
_PortConfigMode_Object = MibTableColumn
portConfigMode = _PortConfigMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 2, 1, 28),
    _PortConfigMode_Type()
)
portConfigMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigMode.setStatus("current")
_PortConfigHsk_Type = DisplayString
_PortConfigHsk_Object = MibTableColumn
portConfigHsk = _PortConfigHsk_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 3, 2, 1, 29),
    _PortConfigHsk_Type()
)
portConfigHsk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigHsk.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4)
)
_Interface_ObjectIdentity = ObjectIdentity
interface = _Interface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1)
)
_Ethernet1_ObjectIdentity = ObjectIdentity
ethernet1 = _Ethernet1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1)
)
_Eth1Mode_Type = DisplayString
_Eth1Mode_Object = MibScalar
eth1Mode = _Eth1Mode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 1),
    _Eth1Mode_Type()
)
eth1Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1Mode.setStatus("current")
_Eth1Address_Type = IpAddress
_Eth1Address_Object = MibScalar
eth1Address = _Eth1Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 2),
    _Eth1Address_Type()
)
eth1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1Address.setStatus("current")
_Eth1SubnetMask_Type = IpAddress
_Eth1SubnetMask_Object = MibScalar
eth1SubnetMask = _Eth1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 3),
    _Eth1SubnetMask_Type()
)
eth1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1SubnetMask.setStatus("current")
_Eth1Router_Type = IpAddress
_Eth1Router_Object = MibScalar
eth1Router = _Eth1Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 4),
    _Eth1Router_Type()
)
eth1Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1Router.setStatus("current")
_Eth1VLAN_ObjectIdentity = ObjectIdentity
eth1VLAN = _Eth1VLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5)
)
_Eth1VLAN1_ObjectIdentity = ObjectIdentity
eth1VLAN1 = _Eth1VLAN1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 1)
)
_Eth1VLAN1ID_Type = Integer32
_Eth1VLAN1ID_Object = MibScalar
eth1VLAN1ID = _Eth1VLAN1ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 1, 1),
    _Eth1VLAN1ID_Type()
)
eth1VLAN1ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN1ID.setStatus("current")
_Eth1VLAN1Priority_Type = Integer32
_Eth1VLAN1Priority_Object = MibScalar
eth1VLAN1Priority = _Eth1VLAN1Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 1, 2),
    _Eth1VLAN1Priority_Type()
)
eth1VLAN1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN1Priority.setStatus("current")
_Eth1VLAN1Address_Type = IpAddress
_Eth1VLAN1Address_Object = MibScalar
eth1VLAN1Address = _Eth1VLAN1Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 1, 3),
    _Eth1VLAN1Address_Type()
)
eth1VLAN1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN1Address.setStatus("current")
_Eth1VLAN1SubnetMask_Type = IpAddress
_Eth1VLAN1SubnetMask_Object = MibScalar
eth1VLAN1SubnetMask = _Eth1VLAN1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 1, 4),
    _Eth1VLAN1SubnetMask_Type()
)
eth1VLAN1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN1SubnetMask.setStatus("current")
_Eth1VLAN1Router_Type = IpAddress
_Eth1VLAN1Router_Object = MibScalar
eth1VLAN1Router = _Eth1VLAN1Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 1, 5),
    _Eth1VLAN1Router_Type()
)
eth1VLAN1Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN1Router.setStatus("current")
_Eth1VLAN2_ObjectIdentity = ObjectIdentity
eth1VLAN2 = _Eth1VLAN2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 2)
)
_Eth1VLAN2ID_Type = Integer32
_Eth1VLAN2ID_Object = MibScalar
eth1VLAN2ID = _Eth1VLAN2ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 2, 1),
    _Eth1VLAN2ID_Type()
)
eth1VLAN2ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN2ID.setStatus("current")
_Eth1VLAN2Priority_Type = Integer32
_Eth1VLAN2Priority_Object = MibScalar
eth1VLAN2Priority = _Eth1VLAN2Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 2, 2),
    _Eth1VLAN2Priority_Type()
)
eth1VLAN2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN2Priority.setStatus("current")
_Eth1VLAN2Address_Type = IpAddress
_Eth1VLAN2Address_Object = MibScalar
eth1VLAN2Address = _Eth1VLAN2Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 2, 3),
    _Eth1VLAN2Address_Type()
)
eth1VLAN2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN2Address.setStatus("current")
_Eth1VLAN2SubnetMask_Type = IpAddress
_Eth1VLAN2SubnetMask_Object = MibScalar
eth1VLAN2SubnetMask = _Eth1VLAN2SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 2, 4),
    _Eth1VLAN2SubnetMask_Type()
)
eth1VLAN2SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN2SubnetMask.setStatus("current")
_Eth1VLAN2Router_Type = IpAddress
_Eth1VLAN2Router_Object = MibScalar
eth1VLAN2Router = _Eth1VLAN2Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 2, 5),
    _Eth1VLAN2Router_Type()
)
eth1VLAN2Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN2Router.setStatus("current")
_Eth1VLAN3_ObjectIdentity = ObjectIdentity
eth1VLAN3 = _Eth1VLAN3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 3)
)
_Eth1VLAN3ID_Type = Integer32
_Eth1VLAN3ID_Object = MibScalar
eth1VLAN3ID = _Eth1VLAN3ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 3, 1),
    _Eth1VLAN3ID_Type()
)
eth1VLAN3ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN3ID.setStatus("current")
_Eth1VLAN3Priority_Type = Integer32
_Eth1VLAN3Priority_Object = MibScalar
eth1VLAN3Priority = _Eth1VLAN3Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 3, 2),
    _Eth1VLAN3Priority_Type()
)
eth1VLAN3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN3Priority.setStatus("current")
_Eth1VLAN3Address_Type = IpAddress
_Eth1VLAN3Address_Object = MibScalar
eth1VLAN3Address = _Eth1VLAN3Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 3, 3),
    _Eth1VLAN3Address_Type()
)
eth1VLAN3Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN3Address.setStatus("current")
_Eth1VLAN3SubnetMask_Type = IpAddress
_Eth1VLAN3SubnetMask_Object = MibScalar
eth1VLAN3SubnetMask = _Eth1VLAN3SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 3, 4),
    _Eth1VLAN3SubnetMask_Type()
)
eth1VLAN3SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN3SubnetMask.setStatus("current")
_Eth1VLAN3Router_Type = IpAddress
_Eth1VLAN3Router_Object = MibScalar
eth1VLAN3Router = _Eth1VLAN3Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 3, 5),
    _Eth1VLAN3Router_Type()
)
eth1VLAN3Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN3Router.setStatus("current")
_Eth1VLAN4_ObjectIdentity = ObjectIdentity
eth1VLAN4 = _Eth1VLAN4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 4)
)
_Eth1VLAN4ID_Type = Integer32
_Eth1VLAN4ID_Object = MibScalar
eth1VLAN4ID = _Eth1VLAN4ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 4, 1),
    _Eth1VLAN4ID_Type()
)
eth1VLAN4ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN4ID.setStatus("current")
_Eth1VLAN4Priority_Type = Integer32
_Eth1VLAN4Priority_Object = MibScalar
eth1VLAN4Priority = _Eth1VLAN4Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 4, 2),
    _Eth1VLAN4Priority_Type()
)
eth1VLAN4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN4Priority.setStatus("current")
_Eth1VLAN4Address_Type = IpAddress
_Eth1VLAN4Address_Object = MibScalar
eth1VLAN4Address = _Eth1VLAN4Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 4, 3),
    _Eth1VLAN4Address_Type()
)
eth1VLAN4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN4Address.setStatus("current")
_Eth1VLAN4SubnetMask_Type = IpAddress
_Eth1VLAN4SubnetMask_Object = MibScalar
eth1VLAN4SubnetMask = _Eth1VLAN4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 4, 4),
    _Eth1VLAN4SubnetMask_Type()
)
eth1VLAN4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN4SubnetMask.setStatus("current")
_Eth1VLAN4Router_Type = IpAddress
_Eth1VLAN4Router_Object = MibScalar
eth1VLAN4Router = _Eth1VLAN4Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 4, 5),
    _Eth1VLAN4Router_Type()
)
eth1VLAN4Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN4Router.setStatus("current")
_Eth1VLAN5_ObjectIdentity = ObjectIdentity
eth1VLAN5 = _Eth1VLAN5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 5)
)
_Eth1VLAN5ID_Type = Integer32
_Eth1VLAN5ID_Object = MibScalar
eth1VLAN5ID = _Eth1VLAN5ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 5, 1),
    _Eth1VLAN5ID_Type()
)
eth1VLAN5ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN5ID.setStatus("current")
_Eth1VLAN5Priority_Type = Integer32
_Eth1VLAN5Priority_Object = MibScalar
eth1VLAN5Priority = _Eth1VLAN5Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 5, 2),
    _Eth1VLAN5Priority_Type()
)
eth1VLAN5Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN5Priority.setStatus("current")
_Eth1VLAN5Address_Type = IpAddress
_Eth1VLAN5Address_Object = MibScalar
eth1VLAN5Address = _Eth1VLAN5Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 5, 3),
    _Eth1VLAN5Address_Type()
)
eth1VLAN5Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN5Address.setStatus("current")
_Eth1VLAN5SubnetMask_Type = IpAddress
_Eth1VLAN5SubnetMask_Object = MibScalar
eth1VLAN5SubnetMask = _Eth1VLAN5SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 5, 4),
    _Eth1VLAN5SubnetMask_Type()
)
eth1VLAN5SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN5SubnetMask.setStatus("current")
_Eth1VLAN5Router_Type = IpAddress
_Eth1VLAN5Router_Object = MibScalar
eth1VLAN5Router = _Eth1VLAN5Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 5, 5),
    _Eth1VLAN5Router_Type()
)
eth1VLAN5Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN5Router.setStatus("current")
_Eth1VLAN6_ObjectIdentity = ObjectIdentity
eth1VLAN6 = _Eth1VLAN6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 6)
)
_Eth1VLAN6ID_Type = Integer32
_Eth1VLAN6ID_Object = MibScalar
eth1VLAN6ID = _Eth1VLAN6ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 6, 1),
    _Eth1VLAN6ID_Type()
)
eth1VLAN6ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN6ID.setStatus("current")
_Eth1VLAN6Priority_Type = Integer32
_Eth1VLAN6Priority_Object = MibScalar
eth1VLAN6Priority = _Eth1VLAN6Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 6, 2),
    _Eth1VLAN6Priority_Type()
)
eth1VLAN6Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN6Priority.setStatus("current")
_Eth1VLAN6Address_Type = IpAddress
_Eth1VLAN6Address_Object = MibScalar
eth1VLAN6Address = _Eth1VLAN6Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 6, 3),
    _Eth1VLAN6Address_Type()
)
eth1VLAN6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN6Address.setStatus("current")
_Eth1VLAN6SubnetMask_Type = IpAddress
_Eth1VLAN6SubnetMask_Object = MibScalar
eth1VLAN6SubnetMask = _Eth1VLAN6SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 6, 4),
    _Eth1VLAN6SubnetMask_Type()
)
eth1VLAN6SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN6SubnetMask.setStatus("current")
_Eth1VLAN6Router_Type = IpAddress
_Eth1VLAN6Router_Object = MibScalar
eth1VLAN6Router = _Eth1VLAN6Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 5, 6, 5),
    _Eth1VLAN6Router_Type()
)
eth1VLAN6Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1VLAN6Router.setStatus("current")
_Eth1MAC_Type = DisplayString
_Eth1MAC_Object = MibScalar
eth1MAC = _Eth1MAC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 6),
    _Eth1MAC_Type()
)
eth1MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1MAC.setStatus("current")
_Eth1IPv6_ObjectIdentity = ObjectIdentity
eth1IPv6 = _Eth1IPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7)
)
_Eth1IPv6Mode_Type = DisplayString
_Eth1IPv6Mode_Object = MibScalar
eth1IPv6Mode = _Eth1IPv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7, 1),
    _Eth1IPv6Mode_Type()
)
eth1IPv6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1IPv6Mode.setStatus("current")
_Eth1IPv6Static_ObjectIdentity = ObjectIdentity
eth1IPv6Static = _Eth1IPv6Static_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7, 2)
)
_Eth1IPv6StaticAddress_Type = DisplayString
_Eth1IPv6StaticAddress_Object = MibScalar
eth1IPv6StaticAddress = _Eth1IPv6StaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7, 2, 1),
    _Eth1IPv6StaticAddress_Type()
)
eth1IPv6StaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1IPv6StaticAddress.setStatus("current")
_Eth1IPv6StaticRouter_Type = DisplayString
_Eth1IPv6StaticRouter_Object = MibScalar
eth1IPv6StaticRouter = _Eth1IPv6StaticRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7, 2, 2),
    _Eth1IPv6StaticRouter_Type()
)
eth1IPv6StaticRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth1IPv6StaticRouter.setStatus("current")
_Eth1IPv6Auto_ObjectIdentity = ObjectIdentity
eth1IPv6Auto = _Eth1IPv6Auto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7, 3)
)
_Eth1IPv6AutoAddress1_Type = DisplayString
_Eth1IPv6AutoAddress1_Object = MibScalar
eth1IPv6AutoAddress1 = _Eth1IPv6AutoAddress1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7, 3, 1),
    _Eth1IPv6AutoAddress1_Type()
)
eth1IPv6AutoAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1IPv6AutoAddress1.setStatus("current")
_Eth1IPv6AutoAddress2_Type = DisplayString
_Eth1IPv6AutoAddress2_Object = MibScalar
eth1IPv6AutoAddress2 = _Eth1IPv6AutoAddress2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7, 3, 2),
    _Eth1IPv6AutoAddress2_Type()
)
eth1IPv6AutoAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1IPv6AutoAddress2.setStatus("current")
_Eth1IPv6AutoAddress3_Type = DisplayString
_Eth1IPv6AutoAddress3_Object = MibScalar
eth1IPv6AutoAddress3 = _Eth1IPv6AutoAddress3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7, 3, 3),
    _Eth1IPv6AutoAddress3_Type()
)
eth1IPv6AutoAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1IPv6AutoAddress3.setStatus("current")
_Eth1IPv6AutoAddress4_Type = DisplayString
_Eth1IPv6AutoAddress4_Object = MibScalar
eth1IPv6AutoAddress4 = _Eth1IPv6AutoAddress4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7, 3, 4),
    _Eth1IPv6AutoAddress4_Type()
)
eth1IPv6AutoAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1IPv6AutoAddress4.setStatus("current")
_Eth1IPv6LinkLocalAddress_Type = DisplayString
_Eth1IPv6LinkLocalAddress_Object = MibScalar
eth1IPv6LinkLocalAddress = _Eth1IPv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 1, 7, 4),
    _Eth1IPv6LinkLocalAddress_Type()
)
eth1IPv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth1IPv6LinkLocalAddress.setStatus("current")
_Ethernet2_ObjectIdentity = ObjectIdentity
ethernet2 = _Ethernet2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2)
)
_Eth2Mode_Type = DisplayString
_Eth2Mode_Object = MibScalar
eth2Mode = _Eth2Mode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 1),
    _Eth2Mode_Type()
)
eth2Mode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2Mode.setStatus("current")
_Eth2Address_Type = IpAddress
_Eth2Address_Object = MibScalar
eth2Address = _Eth2Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 2),
    _Eth2Address_Type()
)
eth2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2Address.setStatus("current")
_Eth2SubnetMask_Type = IpAddress
_Eth2SubnetMask_Object = MibScalar
eth2SubnetMask = _Eth2SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 3),
    _Eth2SubnetMask_Type()
)
eth2SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2SubnetMask.setStatus("current")
_Eth2Router_Type = IpAddress
_Eth2Router_Object = MibScalar
eth2Router = _Eth2Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 4),
    _Eth2Router_Type()
)
eth2Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2Router.setStatus("current")
_Eth2VLAN_ObjectIdentity = ObjectIdentity
eth2VLAN = _Eth2VLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5)
)
_Eth2VLAN1_ObjectIdentity = ObjectIdentity
eth2VLAN1 = _Eth2VLAN1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 1)
)
_Eth2VLAN1ID_Type = Integer32
_Eth2VLAN1ID_Object = MibScalar
eth2VLAN1ID = _Eth2VLAN1ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 1, 1),
    _Eth2VLAN1ID_Type()
)
eth2VLAN1ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN1ID.setStatus("current")
_Eth2VLAN1Priority_Type = Integer32
_Eth2VLAN1Priority_Object = MibScalar
eth2VLAN1Priority = _Eth2VLAN1Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 1, 2),
    _Eth2VLAN1Priority_Type()
)
eth2VLAN1Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN1Priority.setStatus("current")
_Eth2VLAN1Address_Type = IpAddress
_Eth2VLAN1Address_Object = MibScalar
eth2VLAN1Address = _Eth2VLAN1Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 1, 3),
    _Eth2VLAN1Address_Type()
)
eth2VLAN1Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN1Address.setStatus("current")
_Eth2VLAN1SubnetMask_Type = IpAddress
_Eth2VLAN1SubnetMask_Object = MibScalar
eth2VLAN1SubnetMask = _Eth2VLAN1SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 1, 4),
    _Eth2VLAN1SubnetMask_Type()
)
eth2VLAN1SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN1SubnetMask.setStatus("current")
_Eth2VLAN1Router_Type = IpAddress
_Eth2VLAN1Router_Object = MibScalar
eth2VLAN1Router = _Eth2VLAN1Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 1, 5),
    _Eth2VLAN1Router_Type()
)
eth2VLAN1Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN1Router.setStatus("current")
_Eth2VLAN2_ObjectIdentity = ObjectIdentity
eth2VLAN2 = _Eth2VLAN2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 2)
)
_Eth2VLAN2ID_Type = Integer32
_Eth2VLAN2ID_Object = MibScalar
eth2VLAN2ID = _Eth2VLAN2ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 2, 1),
    _Eth2VLAN2ID_Type()
)
eth2VLAN2ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN2ID.setStatus("current")
_Eth2VLAN2Priority_Type = Integer32
_Eth2VLAN2Priority_Object = MibScalar
eth2VLAN2Priority = _Eth2VLAN2Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 2, 2),
    _Eth2VLAN2Priority_Type()
)
eth2VLAN2Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN2Priority.setStatus("current")
_Eth2VLAN2Address_Type = IpAddress
_Eth2VLAN2Address_Object = MibScalar
eth2VLAN2Address = _Eth2VLAN2Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 2, 3),
    _Eth2VLAN2Address_Type()
)
eth2VLAN2Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN2Address.setStatus("current")
_Eth2VLAN2SubnetMask_Type = IpAddress
_Eth2VLAN2SubnetMask_Object = MibScalar
eth2VLAN2SubnetMask = _Eth2VLAN2SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 2, 4),
    _Eth2VLAN2SubnetMask_Type()
)
eth2VLAN2SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN2SubnetMask.setStatus("current")
_Eth2VLAN2Router_Type = IpAddress
_Eth2VLAN2Router_Object = MibScalar
eth2VLAN2Router = _Eth2VLAN2Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 2, 5),
    _Eth2VLAN2Router_Type()
)
eth2VLAN2Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN2Router.setStatus("current")
_Eth2VLAN3_ObjectIdentity = ObjectIdentity
eth2VLAN3 = _Eth2VLAN3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 3)
)
_Eth2VLAN3ID_Type = Integer32
_Eth2VLAN3ID_Object = MibScalar
eth2VLAN3ID = _Eth2VLAN3ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 3, 1),
    _Eth2VLAN3ID_Type()
)
eth2VLAN3ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN3ID.setStatus("current")
_Eth2VLAN3Priority_Type = Integer32
_Eth2VLAN3Priority_Object = MibScalar
eth2VLAN3Priority = _Eth2VLAN3Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 3, 2),
    _Eth2VLAN3Priority_Type()
)
eth2VLAN3Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN3Priority.setStatus("current")
_Eth2VLAN3Address_Type = IpAddress
_Eth2VLAN3Address_Object = MibScalar
eth2VLAN3Address = _Eth2VLAN3Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 3, 3),
    _Eth2VLAN3Address_Type()
)
eth2VLAN3Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN3Address.setStatus("current")
_Eth2VLAN3SubnetMask_Type = IpAddress
_Eth2VLAN3SubnetMask_Object = MibScalar
eth2VLAN3SubnetMask = _Eth2VLAN3SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 3, 4),
    _Eth2VLAN3SubnetMask_Type()
)
eth2VLAN3SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN3SubnetMask.setStatus("current")
_Eth2VLAN3Router_Type = IpAddress
_Eth2VLAN3Router_Object = MibScalar
eth2VLAN3Router = _Eth2VLAN3Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 3, 5),
    _Eth2VLAN3Router_Type()
)
eth2VLAN3Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN3Router.setStatus("current")
_Eth2VLAN4_ObjectIdentity = ObjectIdentity
eth2VLAN4 = _Eth2VLAN4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 4)
)
_Eth2VLAN4ID_Type = Integer32
_Eth2VLAN4ID_Object = MibScalar
eth2VLAN4ID = _Eth2VLAN4ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 4, 1),
    _Eth2VLAN4ID_Type()
)
eth2VLAN4ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN4ID.setStatus("current")
_Eth2VLAN4Priority_Type = Integer32
_Eth2VLAN4Priority_Object = MibScalar
eth2VLAN4Priority = _Eth2VLAN4Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 4, 2),
    _Eth2VLAN4Priority_Type()
)
eth2VLAN4Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN4Priority.setStatus("current")
_Eth2VLAN4Address_Type = IpAddress
_Eth2VLAN4Address_Object = MibScalar
eth2VLAN4Address = _Eth2VLAN4Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 4, 3),
    _Eth2VLAN4Address_Type()
)
eth2VLAN4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN4Address.setStatus("current")
_Eth2VLAN4SubnetMask_Type = IpAddress
_Eth2VLAN4SubnetMask_Object = MibScalar
eth2VLAN4SubnetMask = _Eth2VLAN4SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 4, 4),
    _Eth2VLAN4SubnetMask_Type()
)
eth2VLAN4SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN4SubnetMask.setStatus("current")
_Eth2VLAN4Router_Type = IpAddress
_Eth2VLAN4Router_Object = MibScalar
eth2VLAN4Router = _Eth2VLAN4Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 4, 5),
    _Eth2VLAN4Router_Type()
)
eth2VLAN4Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN4Router.setStatus("current")
_Eth2VLAN5_ObjectIdentity = ObjectIdentity
eth2VLAN5 = _Eth2VLAN5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 5)
)
_Eth2VLAN5ID_Type = Integer32
_Eth2VLAN5ID_Object = MibScalar
eth2VLAN5ID = _Eth2VLAN5ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 5, 1),
    _Eth2VLAN5ID_Type()
)
eth2VLAN5ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN5ID.setStatus("current")
_Eth2VLAN5Priority_Type = Integer32
_Eth2VLAN5Priority_Object = MibScalar
eth2VLAN5Priority = _Eth2VLAN5Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 5, 2),
    _Eth2VLAN5Priority_Type()
)
eth2VLAN5Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN5Priority.setStatus("current")
_Eth2VLAN5Address_Type = IpAddress
_Eth2VLAN5Address_Object = MibScalar
eth2VLAN5Address = _Eth2VLAN5Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 5, 3),
    _Eth2VLAN5Address_Type()
)
eth2VLAN5Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN5Address.setStatus("current")
_Eth2VLAN5SubnetMask_Type = IpAddress
_Eth2VLAN5SubnetMask_Object = MibScalar
eth2VLAN5SubnetMask = _Eth2VLAN5SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 5, 4),
    _Eth2VLAN5SubnetMask_Type()
)
eth2VLAN5SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN5SubnetMask.setStatus("current")
_Eth2VLAN5Router_Type = IpAddress
_Eth2VLAN5Router_Object = MibScalar
eth2VLAN5Router = _Eth2VLAN5Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 5, 5),
    _Eth2VLAN5Router_Type()
)
eth2VLAN5Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN5Router.setStatus("current")
_Eth2VLAN6_ObjectIdentity = ObjectIdentity
eth2VLAN6 = _Eth2VLAN6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 6)
)
_Eth2VLAN6ID_Type = Integer32
_Eth2VLAN6ID_Object = MibScalar
eth2VLAN6ID = _Eth2VLAN6ID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 6, 1),
    _Eth2VLAN6ID_Type()
)
eth2VLAN6ID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN6ID.setStatus("current")
_Eth2VLAN6Priority_Type = Integer32
_Eth2VLAN6Priority_Object = MibScalar
eth2VLAN6Priority = _Eth2VLAN6Priority_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 6, 2),
    _Eth2VLAN6Priority_Type()
)
eth2VLAN6Priority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN6Priority.setStatus("current")
_Eth2VLAN6Address_Type = IpAddress
_Eth2VLAN6Address_Object = MibScalar
eth2VLAN6Address = _Eth2VLAN6Address_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 6, 3),
    _Eth2VLAN6Address_Type()
)
eth2VLAN6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN6Address.setStatus("current")
_Eth2VLAN6SubnetMask_Type = IpAddress
_Eth2VLAN6SubnetMask_Object = MibScalar
eth2VLAN6SubnetMask = _Eth2VLAN6SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 6, 4),
    _Eth2VLAN6SubnetMask_Type()
)
eth2VLAN6SubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN6SubnetMask.setStatus("current")
_Eth2VLAN6Router_Type = IpAddress
_Eth2VLAN6Router_Object = MibScalar
eth2VLAN6Router = _Eth2VLAN6Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 5, 6, 5),
    _Eth2VLAN6Router_Type()
)
eth2VLAN6Router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2VLAN6Router.setStatus("current")
_Eth2MAC_Type = DisplayString
_Eth2MAC_Object = MibScalar
eth2MAC = _Eth2MAC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 6),
    _Eth2MAC_Type()
)
eth2MAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2MAC.setStatus("current")
_Eth2IPv6_ObjectIdentity = ObjectIdentity
eth2IPv6 = _Eth2IPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7)
)
_Eth2IPv6Mode_Type = DisplayString
_Eth2IPv6Mode_Object = MibScalar
eth2IPv6Mode = _Eth2IPv6Mode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7, 1),
    _Eth2IPv6Mode_Type()
)
eth2IPv6Mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2IPv6Mode.setStatus("current")
_Eth2IPv6Static_ObjectIdentity = ObjectIdentity
eth2IPv6Static = _Eth2IPv6Static_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7, 2)
)
_Eth2IPv6StaticAddress_Type = DisplayString
_Eth2IPv6StaticAddress_Object = MibScalar
eth2IPv6StaticAddress = _Eth2IPv6StaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7, 2, 1),
    _Eth2IPv6StaticAddress_Type()
)
eth2IPv6StaticAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2IPv6StaticAddress.setStatus("current")
_Eth2IPv6StaticRouter_Type = DisplayString
_Eth2IPv6StaticRouter_Object = MibScalar
eth2IPv6StaticRouter = _Eth2IPv6StaticRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7, 2, 2),
    _Eth2IPv6StaticRouter_Type()
)
eth2IPv6StaticRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eth2IPv6StaticRouter.setStatus("current")
_Eth2IPv6Auto_ObjectIdentity = ObjectIdentity
eth2IPv6Auto = _Eth2IPv6Auto_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7, 3)
)
_Eth2IPv6AutoAddress1_Type = DisplayString
_Eth2IPv6AutoAddress1_Object = MibScalar
eth2IPv6AutoAddress1 = _Eth2IPv6AutoAddress1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7, 3, 1),
    _Eth2IPv6AutoAddress1_Type()
)
eth2IPv6AutoAddress1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2IPv6AutoAddress1.setStatus("current")
_Eth2IPv6AutoAddress2_Type = DisplayString
_Eth2IPv6AutoAddress2_Object = MibScalar
eth2IPv6AutoAddress2 = _Eth2IPv6AutoAddress2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7, 3, 2),
    _Eth2IPv6AutoAddress2_Type()
)
eth2IPv6AutoAddress2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2IPv6AutoAddress2.setStatus("current")
_Eth2IPv6AutoAddress3_Type = DisplayString
_Eth2IPv6AutoAddress3_Object = MibScalar
eth2IPv6AutoAddress3 = _Eth2IPv6AutoAddress3_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7, 3, 3),
    _Eth2IPv6AutoAddress3_Type()
)
eth2IPv6AutoAddress3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2IPv6AutoAddress3.setStatus("current")
_Eth2IPv6AutoAddress4_Type = DisplayString
_Eth2IPv6AutoAddress4_Object = MibScalar
eth2IPv6AutoAddress4 = _Eth2IPv6AutoAddress4_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7, 3, 4),
    _Eth2IPv6AutoAddress4_Type()
)
eth2IPv6AutoAddress4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2IPv6AutoAddress4.setStatus("current")
_Eth2IPv6LinkLocalAddress_Type = DisplayString
_Eth2IPv6LinkLocalAddress_Object = MibScalar
eth2IPv6LinkLocalAddress = _Eth2IPv6LinkLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 1, 1, 2, 7, 4),
    _Eth2IPv6LinkLocalAddress_Type()
)
eth2IPv6LinkLocalAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eth2IPv6LinkLocalAddress.setStatus("current")
_DefaultRouter_Type = DisplayString
_DefaultRouter_Object = MibScalar
defaultRouter = _DefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 2),
    _DefaultRouter_Type()
)
defaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    defaultRouter.setStatus("current")
_DnsTable_Object = MibTable
dnsTable = _DnsTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 3)
)
if mibBuilder.loadTexts:
    dnsTable.setStatus("current")
_DnsEntry_Object = MibTableRow
dnsEntry = _DnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 3, 1)
)
dnsEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "dnsIndex"),
)
if mibBuilder.loadTexts:
    dnsEntry.setStatus("current")


class _DnsIndex_Type(Integer32):
    """Custom type dnsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DnsIndex_Type.__name__ = "Integer32"
_DnsIndex_Object = MibTableColumn
dnsIndex = _DnsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 3, 1, 1),
    _DnsIndex_Type()
)
dnsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsIndex.setStatus("current")
_DnsAddress_Type = IpAddress
_DnsAddress_Object = MibTableColumn
dnsAddress = _DnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 3, 1, 2),
    _DnsAddress_Type()
)
dnsAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsAddress.setStatus("current")
_Hostname_Type = DisplayString
_Hostname_Object = MibScalar
hostname = _Hostname_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 4),
    _Hostname_Type()
)
hostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostname.setStatus("current")
_HostTable_Object = MibTable
hostTable = _HostTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 5)
)
if mibBuilder.loadTexts:
    hostTable.setStatus("current")
_HostEntry_Object = MibTableRow
hostEntry = _HostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 5, 1)
)
hostEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "hostIndex"),
)
if mibBuilder.loadTexts:
    hostEntry.setStatus("current")


class _HostIndex_Type(Integer32):
    """Custom type hostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HostIndex_Type.__name__ = "Integer32"
_HostIndex_Object = MibTableColumn
hostIndex = _HostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 5, 1, 1),
    _HostIndex_Type()
)
hostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIndex.setStatus("current")
_HostDeclaration_Type = DisplayString
_HostDeclaration_Object = MibTableColumn
hostDeclaration = _HostDeclaration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 5, 1, 2),
    _HostDeclaration_Type()
)
hostDeclaration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hostDeclaration.setStatus("current")
_NcpDuplex_Type = Integer32
_NcpDuplex_Object = MibScalar
ncpDuplex = _NcpDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 6),
    _NcpDuplex_Type()
)
ncpDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpDuplex.setStatus("current")
_NcpTimeout_Type = Integer32
_NcpTimeout_Object = MibScalar
ncpTimeout = _NcpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 7),
    _NcpTimeout_Type()
)
ncpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ncpTimeout.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8)
)
_SnmpAgentEnable_Type = DisplayString
_SnmpAgentEnable_Object = MibScalar
snmpAgentEnable = _SnmpAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 1),
    _SnmpAgentEnable_Type()
)
snmpAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpAgentEnable.setStatus("current")
_SnmpNotificationTx_ObjectIdentity = ObjectIdentity
snmpNotificationTx = _SnmpNotificationTx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 7)
)
_SnmpNtfnAttempts_Type = Integer32
_SnmpNtfnAttempts_Object = MibScalar
snmpNtfnAttempts = _SnmpNtfnAttempts_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 7, 1),
    _SnmpNtfnAttempts_Type()
)
snmpNtfnAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNtfnAttempts.setStatus("current")
_SnmpNtfnTimeout_Type = Integer32
_SnmpNtfnTimeout_Object = MibScalar
snmpNtfnTimeout = _SnmpNtfnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 7, 2),
    _SnmpNtfnTimeout_Type()
)
snmpNtfnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNtfnTimeout.setStatus("current")
_SnmpNtfnCycles_Type = Integer32
_SnmpNtfnCycles_Object = MibScalar
snmpNtfnCycles = _SnmpNtfnCycles_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 7, 3),
    _SnmpNtfnCycles_Type()
)
snmpNtfnCycles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNtfnCycles.setStatus("current")
_SnmpNtfnSnooze_Type = Integer32
_SnmpNtfnSnooze_Object = MibScalar
snmpNtfnSnooze = _SnmpNtfnSnooze_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 7, 4),
    _SnmpNtfnSnooze_Type()
)
snmpNtfnSnooze.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpNtfnSnooze.setStatus("current")
_SnmpProxy_ObjectIdentity = ObjectIdentity
snmpProxy = _SnmpProxy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 8)
)
_SnmpProxyTable_Object = MibTable
snmpProxyTable = _SnmpProxyTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 8, 1)
)
if mibBuilder.loadTexts:
    snmpProxyTable.setStatus("current")
_SnmpProxyEntry_Object = MibTableRow
snmpProxyEntry = _SnmpProxyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 8, 1, 1)
)
snmpProxyEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "snmpProxyIndex"),
)
if mibBuilder.loadTexts:
    snmpProxyEntry.setStatus("current")


class _SnmpProxyIndex_Type(Integer32):
    """Custom type snmpProxyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SnmpProxyIndex_Type.__name__ = "Integer32"
_SnmpProxyIndex_Object = MibTableColumn
snmpProxyIndex = _SnmpProxyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 8, 1, 1, 1),
    _SnmpProxyIndex_Type()
)
snmpProxyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpProxyIndex.setStatus("current")
_SnmpProxyEgressOIDBranch_Type = DisplayString
_SnmpProxyEgressOIDBranch_Object = MibTableColumn
snmpProxyEgressOIDBranch = _SnmpProxyEgressOIDBranch_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 8, 1, 1, 2),
    _SnmpProxyEgressOIDBranch_Type()
)
snmpProxyEgressOIDBranch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyEgressOIDBranch.setStatus("current")
_SnmpProxyIP_Type = DisplayString
_SnmpProxyIP_Object = MibTableColumn
snmpProxyIP = _SnmpProxyIP_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 8, 1, 1, 3),
    _SnmpProxyIP_Type()
)
snmpProxyIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyIP.setStatus("current")


class _SnmpProxyPort_Type(Integer32):
    """Custom type snmpProxyPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SnmpProxyPort_Type.__name__ = "Integer32"
_SnmpProxyPort_Object = MibTableColumn
snmpProxyPort = _SnmpProxyPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 8, 1, 1, 4),
    _SnmpProxyPort_Type()
)
snmpProxyPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyPort.setStatus("current")
_SnmpProxyIngressOIDBranch_Type = DisplayString
_SnmpProxyIngressOIDBranch_Object = MibTableColumn
snmpProxyIngressOIDBranch = _SnmpProxyIngressOIDBranch_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 8, 1, 1, 5),
    _SnmpProxyIngressOIDBranch_Type()
)
snmpProxyIngressOIDBranch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyIngressOIDBranch.setStatus("current")
_SnmpProxyName_Type = DisplayString
_SnmpProxyName_Object = MibTableColumn
snmpProxyName = _SnmpProxyName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 8, 1, 1, 6),
    _SnmpProxyName_Type()
)
snmpProxyName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpProxyName.setStatus("current")
_SnmpPoll_ObjectIdentity = ObjectIdentity
snmpPoll = _SnmpPoll_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9)
)
_SnmpPMode_Type = DisplayString
_SnmpPMode_Object = MibScalar
snmpPMode = _SnmpPMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 1),
    _SnmpPMode_Type()
)
snmpPMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPMode.setStatus("current")
_SnmpPRequestTable_Object = MibTable
snmpPRequestTable = _SnmpPRequestTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4)
)
if mibBuilder.loadTexts:
    snmpPRequestTable.setStatus("current")
_SnmpPRequestEntry_Object = MibTableRow
snmpPRequestEntry = _SnmpPRequestEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1)
)
snmpPRequestEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "snmpPRequestIndex"),
)
if mibBuilder.loadTexts:
    snmpPRequestEntry.setStatus("current")


class _SnmpPRequestIndex_Type(Integer32):
    """Custom type snmpPRequestIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_SnmpPRequestIndex_Type.__name__ = "Integer32"
_SnmpPRequestIndex_Object = MibTableColumn
snmpPRequestIndex = _SnmpPRequestIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1, 1),
    _SnmpPRequestIndex_Type()
)
snmpPRequestIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPRequestIndex.setStatus("current")
_SnmpPRequestDescription_Type = DisplayString
_SnmpPRequestDescription_Object = MibTableColumn
snmpPRequestDescription = _SnmpPRequestDescription_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1, 2),
    _SnmpPRequestDescription_Type()
)
snmpPRequestDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPRequestDescription.setStatus("current")
_SnmpPRequestAgent_Type = DisplayString
_SnmpPRequestAgent_Object = MibTableColumn
snmpPRequestAgent = _SnmpPRequestAgent_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1, 3),
    _SnmpPRequestAgent_Type()
)
snmpPRequestAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPRequestAgent.setStatus("current")
_SnmpPRequestReadcom_Type = DisplayString
_SnmpPRequestReadcom_Object = MibTableColumn
snmpPRequestReadcom = _SnmpPRequestReadcom_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1, 4),
    _SnmpPRequestReadcom_Type()
)
snmpPRequestReadcom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPRequestReadcom.setStatus("current")
_SnmpPRequestOID_Type = DisplayString
_SnmpPRequestOID_Object = MibTableColumn
snmpPRequestOID = _SnmpPRequestOID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1, 5),
    _SnmpPRequestOID_Type()
)
snmpPRequestOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPRequestOID.setStatus("current")


class _SnmpPRequestPeriod_Type(Integer32):
    """Custom type snmpPRequestPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SnmpPRequestPeriod_Type.__name__ = "Integer32"
_SnmpPRequestPeriod_Object = MibTableColumn
snmpPRequestPeriod = _SnmpPRequestPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1, 6),
    _SnmpPRequestPeriod_Type()
)
snmpPRequestPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpPRequestPeriod.setStatus("current")
_SnmpPRequestResultStatus_Type = DisplayString
_SnmpPRequestResultStatus_Object = MibTableColumn
snmpPRequestResultStatus = _SnmpPRequestResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1, 10),
    _SnmpPRequestResultStatus_Type()
)
snmpPRequestResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPRequestResultStatus.setStatus("current")
_SnmpPRequestResultValue_Type = DisplayString
_SnmpPRequestResultValue_Object = MibTableColumn
snmpPRequestResultValue = _SnmpPRequestResultValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1, 11),
    _SnmpPRequestResultValue_Type()
)
snmpPRequestResultValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPRequestResultValue.setStatus("current")
_SnmpPRequestResultTime_Type = DisplayString
_SnmpPRequestResultTime_Object = MibTableColumn
snmpPRequestResultTime = _SnmpPRequestResultTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1, 12),
    _SnmpPRequestResultTime_Type()
)
snmpPRequestResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPRequestResultTime.setStatus("current")
_SnmpPRequestResultType_Type = DisplayString
_SnmpPRequestResultType_Object = MibTableColumn
snmpPRequestResultType = _SnmpPRequestResultType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 8, 9, 4, 1, 13),
    _SnmpPRequestResultType_Type()
)
snmpPRequestResultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpPRequestResultType.setStatus("current")
_FtpPush_ObjectIdentity = ObjectIdentity
ftpPush = _FtpPush_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9)
)
_FtpPushEnable_Type = DisplayString
_FtpPushEnable_Object = MibScalar
ftpPushEnable = _FtpPushEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 1),
    _FtpPushEnable_Type()
)
ftpPushEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushEnable.setStatus("current")
_FtpPushServer_Type = DisplayString
_FtpPushServer_Object = MibScalar
ftpPushServer = _FtpPushServer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 2),
    _FtpPushServer_Type()
)
ftpPushServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushServer.setStatus("current")
_FtpPushAccount_Type = DisplayString
_FtpPushAccount_Object = MibScalar
ftpPushAccount = _FtpPushAccount_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 5),
    _FtpPushAccount_Type()
)
ftpPushAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushAccount.setStatus("current")
_FtpPushDirectory_Type = DisplayString
_FtpPushDirectory_Object = MibScalar
ftpPushDirectory = _FtpPushDirectory_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 6),
    _FtpPushDirectory_Type()
)
ftpPushDirectory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushDirectory.setStatus("current")
_FtpPushperiod_Type = Integer32
_FtpPushperiod_Object = MibScalar
ftpPushperiod = _FtpPushperiod_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 7),
    _FtpPushperiod_Type()
)
ftpPushperiod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushperiod.setStatus("current")
_FtpPushPushFileTable_Object = MibTable
ftpPushPushFileTable = _FtpPushPushFileTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 8)
)
if mibBuilder.loadTexts:
    ftpPushPushFileTable.setStatus("current")
_FtpPushPushFileEntry_Object = MibTableRow
ftpPushPushFileEntry = _FtpPushPushFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 8, 1)
)
ftpPushPushFileEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "ftpPushPushFileIndex"),
)
if mibBuilder.loadTexts:
    ftpPushPushFileEntry.setStatus("current")


class _FtpPushPushFileIndex_Type(Integer32):
    """Custom type ftpPushPushFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FtpPushPushFileIndex_Type.__name__ = "Integer32"
_FtpPushPushFileIndex_Object = MibTableColumn
ftpPushPushFileIndex = _FtpPushPushFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 8, 1, 1),
    _FtpPushPushFileIndex_Type()
)
ftpPushPushFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpPushPushFileIndex.setStatus("current")
_FtpPushPushFile_Type = DisplayString
_FtpPushPushFile_Object = MibTableColumn
ftpPushPushFile = _FtpPushPushFile_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 8, 1, 2),
    _FtpPushPushFile_Type()
)
ftpPushPushFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushPushFile.setStatus("current")
_FtpPushPushAudit_Type = DisplayString
_FtpPushPushAudit_Object = MibScalar
ftpPushPushAudit = _FtpPushPushAudit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 9),
    _FtpPushPushAudit_Type()
)
ftpPushPushAudit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushPushAudit.setStatus("current")
_FtpPushPushAlarms_Type = DisplayString
_FtpPushPushAlarms_Object = MibScalar
ftpPushPushAlarms = _FtpPushPushAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 10),
    _FtpPushPushAlarms_Type()
)
ftpPushPushAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushPushAlarms.setStatus("current")
_FtpPushRemoteFileTable_Object = MibTable
ftpPushRemoteFileTable = _FtpPushRemoteFileTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 11)
)
if mibBuilder.loadTexts:
    ftpPushRemoteFileTable.setStatus("current")
_FtpPushRemoteFileEntry_Object = MibTableRow
ftpPushRemoteFileEntry = _FtpPushRemoteFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 11, 1)
)
ftpPushRemoteFileEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "ftpPushRemoteFileIndex"),
)
if mibBuilder.loadTexts:
    ftpPushRemoteFileEntry.setStatus("current")


class _FtpPushRemoteFileIndex_Type(Integer32):
    """Custom type ftpPushRemoteFileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FtpPushRemoteFileIndex_Type.__name__ = "Integer32"
_FtpPushRemoteFileIndex_Object = MibTableColumn
ftpPushRemoteFileIndex = _FtpPushRemoteFileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 11, 1, 1),
    _FtpPushRemoteFileIndex_Type()
)
ftpPushRemoteFileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ftpPushRemoteFileIndex.setStatus("current")
_FtpPushRemoteFileName_Type = DisplayString
_FtpPushRemoteFileName_Object = MibTableColumn
ftpPushRemoteFileName = _FtpPushRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 11, 1, 2),
    _FtpPushRemoteFileName_Type()
)
ftpPushRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushRemoteFileName.setStatus("current")
_FtpPushRemoteAlarmName_Type = DisplayString
_FtpPushRemoteAlarmName_Object = MibScalar
ftpPushRemoteAlarmName = _FtpPushRemoteAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 12),
    _FtpPushRemoteAlarmName_Type()
)
ftpPushRemoteAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushRemoteAlarmName.setStatus("current")
_FtpPushPassive_Type = DisplayString
_FtpPushPassive_Object = MibScalar
ftpPushPassive = _FtpPushPassive_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 13),
    _FtpPushPassive_Type()
)
ftpPushPassive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushPassive.setStatus("current")
_FtpPushIncludeDate_Type = DisplayString
_FtpPushIncludeDate_Object = MibScalar
ftpPushIncludeDate = _FtpPushIncludeDate_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 14),
    _FtpPushIncludeDate_Type()
)
ftpPushIncludeDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushIncludeDate.setStatus("current")
_FtpPushIncludeTime_Type = DisplayString
_FtpPushIncludeTime_Object = MibScalar
ftpPushIncludeTime = _FtpPushIncludeTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 15),
    _FtpPushIncludeTime_Type()
)
ftpPushIncludeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushIncludeTime.setStatus("current")
_FtpPushIncludeSeq_Type = DisplayString
_FtpPushIncludeSeq_Object = MibScalar
ftpPushIncludeSeq = _FtpPushIncludeSeq_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 16),
    _FtpPushIncludeSeq_Type()
)
ftpPushIncludeSeq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushIncludeSeq.setStatus("current")
_FtpPushPermissions_Type = DisplayString
_FtpPushPermissions_Object = MibScalar
ftpPushPermissions = _FtpPushPermissions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 9, 17),
    _FtpPushPermissions_Type()
)
ftpPushPermissions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ftpPushPermissions.setStatus("current")
_Routing_ObjectIdentity = ObjectIdentity
routing = _Routing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 11)
)
_EthRoutingEnable_Type = DisplayString
_EthRoutingEnable_Object = MibScalar
ethRoutingEnable = _EthRoutingEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 11, 2),
    _EthRoutingEnable_Type()
)
ethRoutingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethRoutingEnable.setStatus("current")
_EthRoutingNATEnable_Type = DisplayString
_EthRoutingNATEnable_Object = MibScalar
ethRoutingNATEnable = _EthRoutingNATEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 11, 3),
    _EthRoutingNATEnable_Type()
)
ethRoutingNATEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethRoutingNATEnable.setStatus("current")
_NetSecurity_ObjectIdentity = ObjectIdentity
netSecurity = _NetSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 12)
)
_IpRestriction_ObjectIdentity = ObjectIdentity
ipRestriction = _IpRestriction_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 12, 1)
)
_IpRestrictionTable_Object = MibTable
ipRestrictionTable = _IpRestrictionTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 12, 1, 1)
)
if mibBuilder.loadTexts:
    ipRestrictionTable.setStatus("current")
_IpRestrictionEntry_Object = MibTableRow
ipRestrictionEntry = _IpRestrictionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 12, 1, 1, 1)
)
ipRestrictionEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "ipRestrictionIndex"),
)
if mibBuilder.loadTexts:
    ipRestrictionEntry.setStatus("current")


class _IpRestrictionIndex_Type(Integer32):
    """Custom type ipRestrictionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_IpRestrictionIndex_Type.__name__ = "Integer32"
_IpRestrictionIndex_Object = MibTableColumn
ipRestrictionIndex = _IpRestrictionIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 12, 1, 1, 1, 1),
    _IpRestrictionIndex_Type()
)
ipRestrictionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipRestrictionIndex.setStatus("current")
_IpRestrictionEnable_Type = DisplayString
_IpRestrictionEnable_Object = MibTableColumn
ipRestrictionEnable = _IpRestrictionEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 12, 1, 1, 1, 2),
    _IpRestrictionEnable_Type()
)
ipRestrictionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRestrictionEnable.setStatus("current")
_IpRestrictionMask_Type = DisplayString
_IpRestrictionMask_Object = MibTableColumn
ipRestrictionMask = _IpRestrictionMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 12, 1, 1, 1, 3),
    _IpRestrictionMask_Type()
)
ipRestrictionMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipRestrictionMask.setStatus("current")
_Trap_ObjectIdentity = ObjectIdentity
trap = _Trap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 14)
)
_TrapInclude_ObjectIdentity = ObjectIdentity
trapInclude = _TrapInclude_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 14, 1)
)
_TrapIncludeDateTime_Type = DisplayString
_TrapIncludeDateTime_Object = MibScalar
trapIncludeDateTime = _TrapIncludeDateTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 14, 1, 1),
    _TrapIncludeDateTime_Type()
)
trapIncludeDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeDateTime.setStatus("current")
_TrapIncludeSiteName_Type = DisplayString
_TrapIncludeSiteName_Object = MibScalar
trapIncludeSiteName = _TrapIncludeSiteName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 14, 1, 2),
    _TrapIncludeSiteName_Type()
)
trapIncludeSiteName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeSiteName.setStatus("current")
_TrapIncludeSensorID_Type = DisplayString
_TrapIncludeSensorID_Object = MibScalar
trapIncludeSensorID = _TrapIncludeSensorID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 14, 1, 3),
    _TrapIncludeSensorID_Type()
)
trapIncludeSensorID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeSensorID.setStatus("current")
_TrapIncludeUDName_Type = DisplayString
_TrapIncludeUDName_Object = MibScalar
trapIncludeUDName = _TrapIncludeUDName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 14, 1, 4),
    _TrapIncludeUDName_Type()
)
trapIncludeUDName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeUDName.setStatus("current")
_TrapIncludeUDState_Type = DisplayString
_TrapIncludeUDState_Object = MibScalar
trapIncludeUDState = _TrapIncludeUDState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 14, 1, 5),
    _TrapIncludeUDState_Type()
)
trapIncludeUDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeUDState.setStatus("current")
_TrapIncludeSourceAddress_Type = IpAddress
_TrapIncludeSourceAddress_Object = MibScalar
trapIncludeSourceAddress = _TrapIncludeSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 14, 1, 6),
    _TrapIncludeSourceAddress_Type()
)
trapIncludeSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapIncludeSourceAddress.setStatus("current")
_TrapAuthFailEnable_Type = DisplayString
_TrapAuthFailEnable_Object = MibScalar
trapAuthFailEnable = _TrapAuthFailEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 14, 2),
    _TrapAuthFailEnable_Type()
)
trapAuthFailEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapAuthFailEnable.setStatus("current")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16)
)
_WirelessMode_Type = DisplayString
_WirelessMode_Object = MibScalar
wirelessMode = _WirelessMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 1),
    _WirelessMode_Type()
)
wirelessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessMode.setStatus("current")
_WirelessAPN_Type = DisplayString
_WirelessAPN_Object = MibScalar
wirelessAPN = _WirelessAPN_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 2),
    _WirelessAPN_Type()
)
wirelessAPN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessAPN.setStatus("current")
_WirelessIdleTimeout_Type = Integer32
_WirelessIdleTimeout_Object = MibScalar
wirelessIdleTimeout = _WirelessIdleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 3),
    _WirelessIdleTimeout_Type()
)
wirelessIdleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessIdleTimeout.setStatus("current")
_WirelessPIN_Type = DisplayString
_WirelessPIN_Object = MibScalar
wirelessPIN = _WirelessPIN_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 5),
    _WirelessPIN_Type()
)
wirelessPIN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessPIN.setStatus("current")
_WirelessDRE_Type = DisplayString
_WirelessDRE_Object = MibScalar
wirelessDRE = _WirelessDRE_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 9),
    _WirelessDRE_Type()
)
wirelessDRE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessDRE.setStatus("current")
_WirelessPPPUsername_Type = DisplayString
_WirelessPPPUsername_Object = MibScalar
wirelessPPPUsername = _WirelessPPPUsername_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 10),
    _WirelessPPPUsername_Type()
)
wirelessPPPUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessPPPUsername.setStatus("current")
_WirelessFirewall_Type = DisplayString
_WirelessFirewall_Object = MibScalar
wirelessFirewall = _WirelessFirewall_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 11),
    _WirelessFirewall_Type()
)
wirelessFirewall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessFirewall.setStatus("current")
_WirelessKeepaliveThreshold_Type = Integer32
_WirelessKeepaliveThreshold_Object = MibScalar
wirelessKeepaliveThreshold = _WirelessKeepaliveThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 12),
    _WirelessKeepaliveThreshold_Type()
)
wirelessKeepaliveThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessKeepaliveThreshold.setStatus("current")
_WirelessPPPDebug_Type = DisplayString
_WirelessPPPDebug_Object = MibScalar
wirelessPPPDebug = _WirelessPPPDebug_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 13),
    _WirelessPPPDebug_Type()
)
wirelessPPPDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessPPPDebug.setStatus("current")
_WirelessConnectivity_ObjectIdentity = ObjectIdentity
wirelessConnectivity = _WirelessConnectivity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 20)
)
_WirelessConnEnable_Type = DisplayString
_WirelessConnEnable_Object = MibScalar
wirelessConnEnable = _WirelessConnEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 20, 1),
    _WirelessConnEnable_Type()
)
wirelessConnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessConnEnable.setStatus("current")
_WirelessConnCheckInterval_Type = Integer32
_WirelessConnCheckInterval_Object = MibScalar
wirelessConnCheckInterval = _WirelessConnCheckInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 20, 2),
    _WirelessConnCheckInterval_Type()
)
wirelessConnCheckInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessConnCheckInterval.setStatus("current")
_WirelessConnFailThreshold_Type = Integer32
_WirelessConnFailThreshold_Object = MibScalar
wirelessConnFailThreshold = _WirelessConnFailThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 20, 3),
    _WirelessConnFailThreshold_Type()
)
wirelessConnFailThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessConnFailThreshold.setStatus("current")
_WirelessConnIP1_Type = IpAddress
_WirelessConnIP1_Object = MibScalar
wirelessConnIP1 = _WirelessConnIP1_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 20, 10),
    _WirelessConnIP1_Type()
)
wirelessConnIP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessConnIP1.setStatus("current")
_WirelessConnIP2_Type = IpAddress
_WirelessConnIP2_Object = MibScalar
wirelessConnIP2 = _WirelessConnIP2_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 16, 20, 11),
    _WirelessConnIP2_Type()
)
wirelessConnIP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wirelessConnIP2.setStatus("current")
_Email_ObjectIdentity = ObjectIdentity
email = _Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 17)
)
_EmailServer_Type = DisplayString
_EmailServer_Object = MibScalar
emailServer = _EmailServer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 17, 1),
    _EmailServer_Type()
)
emailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailServer.setStatus("current")
_EmailDomain_Type = DisplayString
_EmailDomain_Object = MibScalar
emailDomain = _EmailDomain_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 17, 2),
    _EmailDomain_Type()
)
emailDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailDomain.setStatus("current")
_EmailAuthEnable_Type = DisplayString
_EmailAuthEnable_Object = MibScalar
emailAuthEnable = _EmailAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 17, 3),
    _EmailAuthEnable_Type()
)
emailAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailAuthEnable.setStatus("current")
_NetAdvanced_ObjectIdentity = ObjectIdentity
netAdvanced = _NetAdvanced_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 18)
)
_ArpFilter_Type = Integer32
_ArpFilter_Object = MibScalar
arpFilter = _ArpFilter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 18, 1),
    _ArpFilter_Type()
)
arpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpFilter.setStatus("current")
_Web_ObjectIdentity = ObjectIdentity
web = _Web_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 19)
)
_WebEnable_Type = DisplayString
_WebEnable_Object = MibScalar
webEnable = _WebEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 19, 1),
    _WebEnable_Type()
)
webEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webEnable.setStatus("current")
_WebPort_Type = Integer32
_WebPort_Object = MibScalar
webPort = _WebPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 19, 2),
    _WebPort_Type()
)
webPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webPort.setStatus("current")
_WebTimeout_Type = Integer32
_WebTimeout_Object = MibScalar
webTimeout = _WebTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 19, 3),
    _WebTimeout_Type()
)
webTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webTimeout.setStatus("current")
_Ipv6_ObjectIdentity = ObjectIdentity
ipv6 = _Ipv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 21)
)
_Ipv6DefaultRouter_Type = DisplayString
_Ipv6DefaultRouter_Object = MibScalar
ipv6DefaultRouter = _Ipv6DefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 21, 1),
    _Ipv6DefaultRouter_Type()
)
ipv6DefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipv6DefaultRouter.setStatus("current")
_Cpe_ObjectIdentity = ObjectIdentity
cpe = _Cpe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22)
)
_CpeTable_Object = MibTable
cpeTable = _CpeTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1)
)
if mibBuilder.loadTexts:
    cpeTable.setStatus("current")
_CpeEntry_Object = MibTableRow
cpeEntry = _CpeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1)
)
cpeEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "cpeIndex"),
)
if mibBuilder.loadTexts:
    cpeEntry.setStatus("current")


class _CpeIndex_Type(Integer32):
    """Custom type cpeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_CpeIndex_Type.__name__ = "Integer32"
_CpeIndex_Object = MibTableColumn
cpeIndex = _CpeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 1),
    _CpeIndex_Type()
)
cpeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeIndex.setStatus("current")
_CpeHost_Type = DisplayString
_CpeHost_Object = MibTableColumn
cpeHost = _CpeHost_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 2),
    _CpeHost_Type()
)
cpeHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeHost.setStatus("current")
_CpeName_Type = DisplayString
_CpeName_Object = MibTableColumn
cpeName = _CpeName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 3),
    _CpeName_Type()
)
cpeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeName.setStatus("current")
_CpeDescription_Type = DisplayString
_CpeDescription_Object = MibTableColumn
cpeDescription = _CpeDescription_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 4),
    _CpeDescription_Type()
)
cpeDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeDescription.setStatus("current")
_CpeKeepalive_Type = Integer32
_CpeKeepalive_Object = MibTableColumn
cpeKeepalive = _CpeKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 5),
    _CpeKeepalive_Type()
)
cpeKeepalive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeKeepalive.setStatus("current")
_CpeThreshold_Type = Integer32
_CpeThreshold_Object = MibTableColumn
cpeThreshold = _CpeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 6),
    _CpeThreshold_Type()
)
cpeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeThreshold.setStatus("current")
_CpeEventReminderInterval_Type = Integer32
_CpeEventReminderInterval_Object = MibTableColumn
cpeEventReminderInterval = _CpeEventReminderInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 7),
    _CpeEventReminderInterval_Type()
)
cpeEventReminderInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeEventReminderInterval.setStatus("current")
_CpeKeepaliveTicks_Type = Integer32
_CpeKeepaliveTicks_Object = MibTableColumn
cpeKeepaliveTicks = _CpeKeepaliveTicks_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 20),
    _CpeKeepaliveTicks_Type()
)
cpeKeepaliveTicks.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeKeepaliveTicks.setStatus("current")
_CpePingSize_Type = Integer32
_CpePingSize_Object = MibTableColumn
cpePingSize = _CpePingSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 21),
    _CpePingSize_Type()
)
cpePingSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpePingSize.setStatus("current")
_CpeInfoReset_Type = Integer32
_CpeInfoReset_Object = MibTableColumn
cpeInfoReset = _CpeInfoReset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 30),
    _CpeInfoReset_Type()
)
cpeInfoReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpeInfoReset.setStatus("current")
_CpeInfoNumReq_Type = Integer32
_CpeInfoNumReq_Object = MibTableColumn
cpeInfoNumReq = _CpeInfoNumReq_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 31),
    _CpeInfoNumReq_Type()
)
cpeInfoNumReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoNumReq.setStatus("current")
_CpeInfoNumGoodResp_Type = Integer32
_CpeInfoNumGoodResp_Object = MibTableColumn
cpeInfoNumGoodResp = _CpeInfoNumGoodResp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 32),
    _CpeInfoNumGoodResp_Type()
)
cpeInfoNumGoodResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoNumGoodResp.setStatus("current")
_CpeInfoNumBadResp_Type = Integer32
_CpeInfoNumBadResp_Object = MibTableColumn
cpeInfoNumBadResp = _CpeInfoNumBadResp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 33),
    _CpeInfoNumBadResp_Type()
)
cpeInfoNumBadResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoNumBadResp.setStatus("current")
_CpeInfoNumLostResp_Type = Integer32
_CpeInfoNumLostResp_Object = MibTableColumn
cpeInfoNumLostResp = _CpeInfoNumLostResp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 34),
    _CpeInfoNumLostResp_Type()
)
cpeInfoNumLostResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoNumLostResp.setStatus("current")
_CpeInfoPercentLoss_Type = DisplayString
_CpeInfoPercentLoss_Object = MibTableColumn
cpeInfoPercentLoss = _CpeInfoPercentLoss_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 35),
    _CpeInfoPercentLoss_Type()
)
cpeInfoPercentLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoPercentLoss.setStatus("current")
_CpeInfoPercentBad_Type = DisplayString
_CpeInfoPercentBad_Object = MibTableColumn
cpeInfoPercentBad = _CpeInfoPercentBad_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 4, 22, 1, 1, 36),
    _CpeInfoPercentBad_Type()
)
cpeInfoPercentBad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpeInfoPercentBad.setStatus("current")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 8)
)
_Clock_Type = DisplayString
_Clock_Object = MibScalar
clock = _Clock_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 8, 1),
    _Clock_Type()
)
clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clock.setStatus("current")
_Console_ObjectIdentity = ObjectIdentity
console = _Console_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 10)
)
_ConsoleDuplex_Type = DisplayString
_ConsoleDuplex_Object = MibScalar
consoleDuplex = _ConsoleDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 10, 1),
    _ConsoleDuplex_Type()
)
consoleDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleDuplex.setStatus("current")
_ConsoleTimeout_Type = Integer32
_ConsoleTimeout_Object = MibScalar
consoleTimeout = _ConsoleTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 10, 2),
    _ConsoleTimeout_Type()
)
consoleTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleTimeout.setStatus("current")
_ConsoleConfirm_Type = DisplayString
_ConsoleConfirm_Object = MibScalar
consoleConfirm = _ConsoleConfirm_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 10, 7),
    _ConsoleConfirm_Type()
)
consoleConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleConfirm.setStatus("current")
_UnitSecurity_ObjectIdentity = ObjectIdentity
unitSecurity = _UnitSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11)
)
_SecCore_ObjectIdentity = ObjectIdentity
secCore = _SecCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 1)
)
_ScShowPasswordPrompt_Type = DisplayString
_ScShowPasswordPrompt_Object = MibScalar
scShowPasswordPrompt = _ScShowPasswordPrompt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 1, 1),
    _ScShowPasswordPrompt_Type()
)
scShowPasswordPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scShowPasswordPrompt.setStatus("current")
_ScConsoleLoginRequired_Type = DisplayString
_ScConsoleLoginRequired_Object = MibScalar
scConsoleLoginRequired = _ScConsoleLoginRequired_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 1, 2),
    _ScConsoleLoginRequired_Type()
)
scConsoleLoginRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scConsoleLoginRequired.setStatus("current")
_ScAuthMode_Type = DisplayString
_ScAuthMode_Object = MibScalar
scAuthMode = _ScAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 1, 7),
    _ScAuthMode_Type()
)
scAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scAuthMode.setStatus("current")
_ScRightsGroup_Type = DisplayString
_ScRightsGroup_Object = MibScalar
scRightsGroup = _ScRightsGroup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 1, 8),
    _ScRightsGroup_Type()
)
scRightsGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scRightsGroup.setStatus("current")
_ScSecret_Type = DisplayString
_ScSecret_Object = MibScalar
scSecret = _ScSecret_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 1, 9),
    _ScSecret_Type()
)
scSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scSecret.setStatus("current")
_SecUserTable_Object = MibTable
secUserTable = _SecUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2)
)
if mibBuilder.loadTexts:
    secUserTable.setStatus("current")
_SecUserEntry_Object = MibTableRow
secUserEntry = _SecUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1)
)
secUserEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "secUserIndex"),
)
if mibBuilder.loadTexts:
    secUserEntry.setStatus("current")


class _SecUserIndex_Type(Integer32):
    """Custom type secUserIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_SecUserIndex_Type.__name__ = "Integer32"
_SecUserIndex_Object = MibTableColumn
secUserIndex = _SecUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 1),
    _SecUserIndex_Type()
)
secUserIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secUserIndex.setStatus("current")
_SecUserEnable_Type = DisplayString
_SecUserEnable_Object = MibTableColumn
secUserEnable = _SecUserEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 2),
    _SecUserEnable_Type()
)
secUserEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserEnable.setStatus("current")
_SecUserConnectVia_Type = DisplayString
_SecUserConnectVia_Object = MibTableColumn
secUserConnectVia = _SecUserConnectVia_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 5),
    _SecUserConnectVia_Type()
)
secUserConnectVia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserConnectVia.setStatus("current")
_SecUserLoginTo_Type = DisplayString
_SecUserLoginTo_Object = MibTableColumn
secUserLoginTo = _SecUserLoginTo_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 6),
    _SecUserLoginTo_Type()
)
secUserLoginTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserLoginTo.setStatus("current")
_SecUserAccessFile_Type = DisplayString
_SecUserAccessFile_Object = MibTableColumn
secUserAccessFile = _SecUserAccessFile_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 7),
    _SecUserAccessFile_Type()
)
secUserAccessFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserAccessFile.setStatus("current")
_SecUserPTEscapeTo_Type = DisplayString
_SecUserPTEscapeTo_Object = MibTableColumn
secUserPTEscapeTo = _SecUserPTEscapeTo_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 9),
    _SecUserPTEscapeTo_Type()
)
secUserPTEscapeTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserPTEscapeTo.setStatus("current")
_SecUserRights_Type = DisplayString
_SecUserRights_Object = MibTableColumn
secUserRights = _SecUserRights_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 11),
    _SecUserRights_Type()
)
secUserRights.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserRights.setStatus("current")
_SecUserEventsReadAccess_Type = DisplayString
_SecUserEventsReadAccess_Object = MibTableColumn
secUserEventsReadAccess = _SecUserEventsReadAccess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 13),
    _SecUserEventsReadAccess_Type()
)
secUserEventsReadAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserEventsReadAccess.setStatus("current")
_SecUserAuditReadAccess_Type = DisplayString
_SecUserAuditReadAccess_Object = MibTableColumn
secUserAuditReadAccess = _SecUserAuditReadAccess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 14),
    _SecUserAuditReadAccess_Type()
)
secUserAuditReadAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserAuditReadAccess.setStatus("current")
_SecUserEventsWriteAccess_Type = DisplayString
_SecUserEventsWriteAccess_Object = MibTableColumn
secUserEventsWriteAccess = _SecUserEventsWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 16),
    _SecUserEventsWriteAccess_Type()
)
secUserEventsWriteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserEventsWriteAccess.setStatus("current")
_SecUserAuditWriteAccess_Type = DisplayString
_SecUserAuditWriteAccess_Object = MibTableColumn
secUserAuditWriteAccess = _SecUserAuditWriteAccess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 17),
    _SecUserAuditWriteAccess_Type()
)
secUserAuditWriteAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserAuditWriteAccess.setStatus("current")
_SecUserExpiration_Type = DisplayString
_SecUserExpiration_Object = MibTableColumn
secUserExpiration = _SecUserExpiration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 18),
    _SecUserExpiration_Type()
)
secUserExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserExpiration.setStatus("current")
_SecUserChallengeConsoleMode_Type = DisplayString
_SecUserChallengeConsoleMode_Object = MibTableColumn
secUserChallengeConsoleMode = _SecUserChallengeConsoleMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 24),
    _SecUserChallengeConsoleMode_Type()
)
secUserChallengeConsoleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserChallengeConsoleMode.setStatus("current")


class _SecUserChallengeExpiration_Type(Integer32):
    """Custom type secUserChallengeExpiration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 180),
    )


_SecUserChallengeExpiration_Type.__name__ = "Integer32"
_SecUserChallengeExpiration_Object = MibTableColumn
secUserChallengeExpiration = _SecUserChallengeExpiration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 2, 1, 27),
    _SecUserChallengeExpiration_Type()
)
secUserChallengeExpiration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserChallengeExpiration.setStatus("current")
_SecFactory_ObjectIdentity = ObjectIdentity
secFactory = _SecFactory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 3)
)
_SfEnable_Type = DisplayString
_SfEnable_Object = MibScalar
sfEnable = _SfEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 3, 1),
    _SfEnable_Type()
)
sfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfEnable.setStatus("current")
_SfSecret_Type = DisplayString
_SfSecret_Object = MibScalar
sfSecret = _SfSecret_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 11, 3, 2),
    _SfSecret_Type()
)
sfSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sfSecret.setStatus("current")
_Event_ObjectIdentity = ObjectIdentity
event = _Event_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12)
)
_EvCore_ObjectIdentity = ObjectIdentity
evCore = _EvCore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1)
)
_EvClassNameTable_Object = MibTable
evClassNameTable = _EvClassNameTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 1)
)
if mibBuilder.loadTexts:
    evClassNameTable.setStatus("current")
_EvClassNameEntry_Object = MibTableRow
evClassNameEntry = _EvClassNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 1, 1)
)
evClassNameEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "evClassNameIndex"),
)
if mibBuilder.loadTexts:
    evClassNameEntry.setStatus("current")


class _EvClassNameIndex_Type(Integer32):
    """Custom type evClassNameIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_EvClassNameIndex_Type.__name__ = "Integer32"
_EvClassNameIndex_Object = MibTableColumn
evClassNameIndex = _EvClassNameIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 1, 1, 1),
    _EvClassNameIndex_Type()
)
evClassNameIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evClassNameIndex.setStatus("current")
_EvClassName_Type = DisplayString
_EvClassName_Object = MibTableColumn
evClassName = _EvClassName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 1, 1, 2),
    _EvClassName_Type()
)
evClassName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evClassName.setStatus("current")


class _EvReminderInterval_Type(Integer32):
    """Custom type evReminderInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EvReminderInterval_Type.__name__ = "Integer32"
_EvReminderInterval_Object = MibScalar
evReminderInterval = _EvReminderInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 2),
    _EvReminderInterval_Type()
)
evReminderInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evReminderInterval.setStatus("current")
_EvLog_ObjectIdentity = ObjectIdentity
evLog = _EvLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 3)
)
_EvLogEnable_Type = DisplayString
_EvLogEnable_Object = MibScalar
evLogEnable = _EvLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 3, 1),
    _EvLogEnable_Type()
)
evLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogEnable.setStatus("current")
_EvLogStoreAlarm_Type = DisplayString
_EvLogStoreAlarm_Object = MibScalar
evLogStoreAlarm = _EvLogStoreAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 3, 2),
    _EvLogStoreAlarm_Type()
)
evLogStoreAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogStoreAlarm.setStatus("current")
_EvLogMaxSize_Type = Integer32
_EvLogMaxSize_Object = MibScalar
evLogMaxSize = _EvLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 3, 3),
    _EvLogMaxSize_Type()
)
evLogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogMaxSize.setStatus("current")
_EvLogStoreSensor_Type = DisplayString
_EvLogStoreSensor_Object = MibScalar
evLogStoreSensor = _EvLogStoreSensor_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 3, 4),
    _EvLogStoreSensor_Type()
)
evLogStoreSensor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogStoreSensor.setStatus("current")
_EvLogTimeStampAlarms_Type = DisplayString
_EvLogTimeStampAlarms_Object = MibScalar
evLogTimeStampAlarms = _EvLogTimeStampAlarms_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 3, 5),
    _EvLogTimeStampAlarms_Type()
)
evLogTimeStampAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogTimeStampAlarms.setStatus("current")
_EvLogPrependName_Type = DisplayString
_EvLogPrependName_Object = MibScalar
evLogPrependName = _EvLogPrependName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 3, 6),
    _EvLogPrependName_Type()
)
evLogPrependName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLogPrependName.setStatus("current")
_EvMgmt_ObjectIdentity = ObjectIdentity
evMgmt = _EvMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 4)
)
_EvMgmtReprocess_Type = DisplayString
_EvMgmtReprocess_Object = MibScalar
evMgmtReprocess = _EvMgmtReprocess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 1, 4, 3),
    _EvMgmtReprocess_Type()
)
evMgmtReprocess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evMgmtReprocess.setStatus("current")
_EvSched1_ObjectIdentity = ObjectIdentity
evSched1 = _EvSched1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5)
)
_EvSched1Enable_Type = DisplayString
_EvSched1Enable_Object = MibScalar
evSched1Enable = _EvSched1Enable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 1),
    _EvSched1Enable_Type()
)
evSched1Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Enable.setStatus("current")
_EvSched1Actions_Type = DisplayString
_EvSched1Actions_Object = MibScalar
evSched1Actions = _EvSched1Actions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 2),
    _EvSched1Actions_Type()
)
evSched1Actions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Actions.setStatus("current")
_EvSched1Message_Type = DisplayString
_EvSched1Message_Object = MibScalar
evSched1Message = _EvSched1Message_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 3),
    _EvSched1Message_Type()
)
evSched1Message.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Message.setStatus("current")
_EvSched1TrapNum_Type = Integer32
_EvSched1TrapNum_Object = MibScalar
evSched1TrapNum = _EvSched1TrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 4),
    _EvSched1TrapNum_Type()
)
evSched1TrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1TrapNum.setStatus("current")
_EvSched1Class_Type = DisplayString
_EvSched1Class_Object = MibScalar
evSched1Class = _EvSched1Class_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 5),
    _EvSched1Class_Type()
)
evSched1Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Class.setStatus("current")
_EvSched1Sunday_Type = DisplayString
_EvSched1Sunday_Object = MibScalar
evSched1Sunday = _EvSched1Sunday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 6),
    _EvSched1Sunday_Type()
)
evSched1Sunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Sunday.setStatus("current")
_EvSched1Monday_Type = DisplayString
_EvSched1Monday_Object = MibScalar
evSched1Monday = _EvSched1Monday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 7),
    _EvSched1Monday_Type()
)
evSched1Monday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Monday.setStatus("current")
_EvSched1Tuesday_Type = DisplayString
_EvSched1Tuesday_Object = MibScalar
evSched1Tuesday = _EvSched1Tuesday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 8),
    _EvSched1Tuesday_Type()
)
evSched1Tuesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Tuesday.setStatus("current")
_EvSched1Wednesday_Type = DisplayString
_EvSched1Wednesday_Object = MibScalar
evSched1Wednesday = _EvSched1Wednesday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 9),
    _EvSched1Wednesday_Type()
)
evSched1Wednesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Wednesday.setStatus("current")
_EvSched1Thursday_Type = DisplayString
_EvSched1Thursday_Object = MibScalar
evSched1Thursday = _EvSched1Thursday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 10),
    _EvSched1Thursday_Type()
)
evSched1Thursday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Thursday.setStatus("current")
_EvSched1Friday_Type = DisplayString
_EvSched1Friday_Object = MibScalar
evSched1Friday = _EvSched1Friday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 11),
    _EvSched1Friday_Type()
)
evSched1Friday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Friday.setStatus("current")
_EvSched1Saturday_Type = DisplayString
_EvSched1Saturday_Object = MibScalar
evSched1Saturday = _EvSched1Saturday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 12),
    _EvSched1Saturday_Type()
)
evSched1Saturday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Saturday.setStatus("current")
_EvSched1Exclusions_Type = DisplayString
_EvSched1Exclusions_Object = MibScalar
evSched1Exclusions = _EvSched1Exclusions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 5, 13),
    _EvSched1Exclusions_Type()
)
evSched1Exclusions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched1Exclusions.setStatus("current")
_EvSched2_ObjectIdentity = ObjectIdentity
evSched2 = _EvSched2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6)
)
_EvSched2Enable_Type = DisplayString
_EvSched2Enable_Object = MibScalar
evSched2Enable = _EvSched2Enable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 1),
    _EvSched2Enable_Type()
)
evSched2Enable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Enable.setStatus("current")
_EvSched2Actions_Type = DisplayString
_EvSched2Actions_Object = MibScalar
evSched2Actions = _EvSched2Actions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 2),
    _EvSched2Actions_Type()
)
evSched2Actions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Actions.setStatus("current")
_EvSched2Message_Type = DisplayString
_EvSched2Message_Object = MibScalar
evSched2Message = _EvSched2Message_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 3),
    _EvSched2Message_Type()
)
evSched2Message.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Message.setStatus("current")
_EvSched2TrapNum_Type = Integer32
_EvSched2TrapNum_Object = MibScalar
evSched2TrapNum = _EvSched2TrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 4),
    _EvSched2TrapNum_Type()
)
evSched2TrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2TrapNum.setStatus("current")
_EvSched2Class_Type = DisplayString
_EvSched2Class_Object = MibScalar
evSched2Class = _EvSched2Class_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 5),
    _EvSched2Class_Type()
)
evSched2Class.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Class.setStatus("current")
_EvSched2Sunday_Type = DisplayString
_EvSched2Sunday_Object = MibScalar
evSched2Sunday = _EvSched2Sunday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 6),
    _EvSched2Sunday_Type()
)
evSched2Sunday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Sunday.setStatus("current")
_EvSched2Monday_Type = DisplayString
_EvSched2Monday_Object = MibScalar
evSched2Monday = _EvSched2Monday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 7),
    _EvSched2Monday_Type()
)
evSched2Monday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Monday.setStatus("current")
_EvSched2Tuesday_Type = DisplayString
_EvSched2Tuesday_Object = MibScalar
evSched2Tuesday = _EvSched2Tuesday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 8),
    _EvSched2Tuesday_Type()
)
evSched2Tuesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Tuesday.setStatus("current")
_EvSched2Wednesday_Type = DisplayString
_EvSched2Wednesday_Object = MibScalar
evSched2Wednesday = _EvSched2Wednesday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 9),
    _EvSched2Wednesday_Type()
)
evSched2Wednesday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Wednesday.setStatus("current")
_EvSched2Thursday_Type = DisplayString
_EvSched2Thursday_Object = MibScalar
evSched2Thursday = _EvSched2Thursday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 10),
    _EvSched2Thursday_Type()
)
evSched2Thursday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Thursday.setStatus("current")
_EvSched2Friday_Type = DisplayString
_EvSched2Friday_Object = MibScalar
evSched2Friday = _EvSched2Friday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 11),
    _EvSched2Friday_Type()
)
evSched2Friday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Friday.setStatus("current")
_EvSched2Saturday_Type = DisplayString
_EvSched2Saturday_Object = MibScalar
evSched2Saturday = _EvSched2Saturday_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 12),
    _EvSched2Saturday_Type()
)
evSched2Saturday.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Saturday.setStatus("current")
_EvSched2Exclusions_Type = DisplayString
_EvSched2Exclusions_Object = MibScalar
evSched2Exclusions = _EvSched2Exclusions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 6, 13),
    _EvSched2Exclusions_Type()
)
evSched2Exclusions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSched2Exclusions.setStatus("current")
_EvShskLowTable_Object = MibTable
evShskLowTable = _EvShskLowTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 7)
)
if mibBuilder.loadTexts:
    evShskLowTable.setStatus("current")
_EvShskLowEntry_Object = MibTableRow
evShskLowEntry = _EvShskLowEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 7, 1)
)
evShskLowEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "evShskLowIndex"),
)
if mibBuilder.loadTexts:
    evShskLowEntry.setStatus("current")


class _EvShskLowIndex_Type(Integer32):
    """Custom type evShskLowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EvShskLowIndex_Type.__name__ = "Integer32"
_EvShskLowIndex_Object = MibTableColumn
evShskLowIndex = _EvShskLowIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 7, 1, 1),
    _EvShskLowIndex_Type()
)
evShskLowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evShskLowIndex.setStatus("current")
_EvShskLowEnable_Type = DisplayString
_EvShskLowEnable_Object = MibTableColumn
evShskLowEnable = _EvShskLowEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 7, 1, 2),
    _EvShskLowEnable_Type()
)
evShskLowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskLowEnable.setStatus("current")
_EvShskLowActions_Type = DisplayString
_EvShskLowActions_Object = MibTableColumn
evShskLowActions = _EvShskLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 7, 1, 3),
    _EvShskLowActions_Type()
)
evShskLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskLowActions.setStatus("current")
_EvShskLowMessage_Type = DisplayString
_EvShskLowMessage_Object = MibTableColumn
evShskLowMessage = _EvShskLowMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 7, 1, 4),
    _EvShskLowMessage_Type()
)
evShskLowMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskLowMessage.setStatus("current")
_EvShskLowClass_Type = DisplayString
_EvShskLowClass_Object = MibTableColumn
evShskLowClass = _EvShskLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 7, 1, 5),
    _EvShskLowClass_Type()
)
evShskLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskLowClass.setStatus("current")
_EvShskLowTrapNum_Type = Integer32
_EvShskLowTrapNum_Object = MibTableColumn
evShskLowTrapNum = _EvShskLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 7, 1, 6),
    _EvShskLowTrapNum_Type()
)
evShskLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskLowTrapNum.setStatus("current")
_EvShskHighTable_Object = MibTable
evShskHighTable = _EvShskHighTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 8)
)
if mibBuilder.loadTexts:
    evShskHighTable.setStatus("current")
_EvShskHighEntry_Object = MibTableRow
evShskHighEntry = _EvShskHighEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 8, 1)
)
evShskHighEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "evShskHighIndex"),
)
if mibBuilder.loadTexts:
    evShskHighEntry.setStatus("current")


class _EvShskHighIndex_Type(Integer32):
    """Custom type evShskHighIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_EvShskHighIndex_Type.__name__ = "Integer32"
_EvShskHighIndex_Object = MibTableColumn
evShskHighIndex = _EvShskHighIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 8, 1, 1),
    _EvShskHighIndex_Type()
)
evShskHighIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    evShskHighIndex.setStatus("current")
_EvShskHighEnable_Type = DisplayString
_EvShskHighEnable_Object = MibTableColumn
evShskHighEnable = _EvShskHighEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 8, 1, 2),
    _EvShskHighEnable_Type()
)
evShskHighEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskHighEnable.setStatus("current")
_EvShskHighActions_Type = DisplayString
_EvShskHighActions_Object = MibTableColumn
evShskHighActions = _EvShskHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 8, 1, 3),
    _EvShskHighActions_Type()
)
evShskHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskHighActions.setStatus("current")
_EvShskHighMessage_Type = DisplayString
_EvShskHighMessage_Object = MibTableColumn
evShskHighMessage = _EvShskHighMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 8, 1, 4),
    _EvShskHighMessage_Type()
)
evShskHighMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskHighMessage.setStatus("current")
_EvShskHighClass_Type = DisplayString
_EvShskHighClass_Object = MibTableColumn
evShskHighClass = _EvShskHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 8, 1, 5),
    _EvShskHighClass_Type()
)
evShskHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskHighClass.setStatus("current")
_EvShskHighTrapNum_Type = Integer32
_EvShskHighTrapNum_Object = MibTableColumn
evShskHighTrapNum = _EvShskHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 8, 1, 6),
    _EvShskHighTrapNum_Type()
)
evShskHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evShskHighTrapNum.setStatus("current")
_EvNoSensor_ObjectIdentity = ObjectIdentity
evNoSensor = _EvNoSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 9)
)
_EvNoSensorTimeout_Type = Integer32
_EvNoSensorTimeout_Object = MibScalar
evNoSensorTimeout = _EvNoSensorTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 9, 1),
    _EvNoSensorTimeout_Type()
)
evNoSensorTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoSensorTimeout.setStatus("current")
_EvNoSensorActions_Type = DisplayString
_EvNoSensorActions_Object = MibScalar
evNoSensorActions = _EvNoSensorActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 9, 2),
    _EvNoSensorActions_Type()
)
evNoSensorActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoSensorActions.setStatus("current")
_EvNoSensorTrapNum_Type = Integer32
_EvNoSensorTrapNum_Object = MibScalar
evNoSensorTrapNum = _EvNoSensorTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 9, 3),
    _EvNoSensorTrapNum_Type()
)
evNoSensorTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoSensorTrapNum.setStatus("current")
_EvNoSensorClass_Type = DisplayString
_EvNoSensorClass_Object = MibScalar
evNoSensorClass = _EvNoSensorClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 9, 4),
    _EvNoSensorClass_Type()
)
evNoSensorClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evNoSensorClass.setStatus("current")
_FuelSensor_ObjectIdentity = ObjectIdentity
fuelSensor = _FuelSensor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11)
)
_FuelSensorGeneralTable_Object = MibTable
fuelSensorGeneralTable = _FuelSensorGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1)
)
if mibBuilder.loadTexts:
    fuelSensorGeneralTable.setStatus("current")
_FsGenEntry_Object = MibTableRow
fsGenEntry = _FsGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1)
)
fsGenEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "fsGenIndex"),
)
if mibBuilder.loadTexts:
    fsGenEntry.setStatus("current")


class _FsGenIndex_Type(Integer32):
    """Custom type fsGenIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsGenIndex_Type.__name__ = "Integer32"
_FsGenIndex_Object = MibTableColumn
fsGenIndex = _FsGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 1),
    _FsGenIndex_Type()
)
fsGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsGenIndex.setStatus("current")
_FsGenName_Type = DisplayString
_FsGenName_Object = MibTableColumn
fsGenName = _FsGenName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 2),
    _FsGenName_Type()
)
fsGenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenName.setStatus("current")
_FsGenSensorType_Type = DisplayString
_FsGenSensorType_Object = MibTableColumn
fsGenSensorType = _FsGenSensorType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 3),
    _FsGenSensorType_Type()
)
fsGenSensorType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSensorType.setStatus("current")
_FsGenDistanceUnit_Type = DisplayString
_FsGenDistanceUnit_Object = MibTableColumn
fsGenDistanceUnit = _FsGenDistanceUnit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 4),
    _FsGenDistanceUnit_Type()
)
fsGenDistanceUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenDistanceUnit.setStatus("current")
_FsGenRawValueTop_Type = DisplayString
_FsGenRawValueTop_Object = MibTableColumn
fsGenRawValueTop = _FsGenRawValueTop_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 5),
    _FsGenRawValueTop_Type()
)
fsGenRawValueTop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenRawValueTop.setStatus("current")
_FsGenTopOffset_Type = DisplayString
_FsGenTopOffset_Object = MibTableColumn
fsGenTopOffset = _FsGenTopOffset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 6),
    _FsGenTopOffset_Type()
)
fsGenTopOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenTopOffset.setStatus("current")
_FsGenRawValueBottom_Type = DisplayString
_FsGenRawValueBottom_Object = MibTableColumn
fsGenRawValueBottom = _FsGenRawValueBottom_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 7),
    _FsGenRawValueBottom_Type()
)
fsGenRawValueBottom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenRawValueBottom.setStatus("current")
_FsGenBottomOffset_Type = DisplayString
_FsGenBottomOffset_Object = MibTableColumn
fsGenBottomOffset = _FsGenBottomOffset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 8),
    _FsGenBottomOffset_Type()
)
fsGenBottomOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenBottomOffset.setStatus("current")


class _FsGenInputES_Type(Integer32):
    """Custom type fsGenInputES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_FsGenInputES_Type.__name__ = "Integer32"
_FsGenInputES_Object = MibTableColumn
fsGenInputES = _FsGenInputES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 9),
    _FsGenInputES_Type()
)
fsGenInputES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenInputES.setStatus("current")


class _FsGenInputPoint_Type(Integer32):
    """Custom type fsGenInputPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_FsGenInputPoint_Type.__name__ = "Integer32"
_FsGenInputPoint_Object = MibTableColumn
fsGenInputPoint = _FsGenInputPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 10),
    _FsGenInputPoint_Type()
)
fsGenInputPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenInputPoint.setStatus("current")
_FsGenFilterAveraging_Type = Integer32
_FsGenFilterAveraging_Object = MibTableColumn
fsGenFilterAveraging = _FsGenFilterAveraging_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 11),
    _FsGenFilterAveraging_Type()
)
fsGenFilterAveraging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenFilterAveraging.setStatus("current")
_FsGenSysrepEnable_Type = DisplayString
_FsGenSysrepEnable_Object = MibTableColumn
fsGenSysrepEnable = _FsGenSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 12),
    _FsGenSysrepEnable_Type()
)
fsGenSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSysrepEnable.setStatus("current")
_FsGenSysrepThreshold_Type = DisplayString
_FsGenSysrepThreshold_Object = MibTableColumn
fsGenSysrepThreshold = _FsGenSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 13),
    _FsGenSysrepThreshold_Type()
)
fsGenSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSysrepThreshold.setStatus("current")
_FsGenSysrepLimit_Type = Integer32
_FsGenSysrepLimit_Object = MibTableColumn
fsGenSysrepLimit = _FsGenSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 14),
    _FsGenSysrepLimit_Type()
)
fsGenSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSysrepLimit.setStatus("current")


class _FsGenSysrepPackage_Type(Integer32):
    """Custom type fsGenSysrepPackage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsGenSysrepPackage_Type.__name__ = "Integer32"
_FsGenSysrepPackage_Object = MibTableColumn
fsGenSysrepPackage = _FsGenSysrepPackage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 15),
    _FsGenSysrepPackage_Type()
)
fsGenSysrepPackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSysrepPackage.setStatus("current")
_FsGenSysrepType_Type = DisplayString
_FsGenSysrepType_Object = MibTableColumn
fsGenSysrepType = _FsGenSysrepType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 16),
    _FsGenSysrepType_Type()
)
fsGenSysrepType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenSysrepType.setStatus("current")
_FsGenEnable_Type = DisplayString
_FsGenEnable_Object = MibTableColumn
fsGenEnable = _FsGenEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 1, 1, 17),
    _FsGenEnable_Type()
)
fsGenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsGenEnable.setStatus("current")
_FuelSensorTankTable_Object = MibTable
fuelSensorTankTable = _FuelSensorTankTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 2)
)
if mibBuilder.loadTexts:
    fuelSensorTankTable.setStatus("current")
_FsTankEntry_Object = MibTableRow
fsTankEntry = _FsTankEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 2, 1)
)
fsTankEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "fsTankIndex"),
)
if mibBuilder.loadTexts:
    fsTankEntry.setStatus("current")


class _FsTankIndex_Type(Integer32):
    """Custom type fsTankIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsTankIndex_Type.__name__ = "Integer32"
_FsTankIndex_Object = MibTableColumn
fsTankIndex = _FsTankIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 2, 1, 1),
    _FsTankIndex_Type()
)
fsTankIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTankIndex.setStatus("current")
_FsTankHeight_Type = DisplayString
_FsTankHeight_Object = MibTableColumn
fsTankHeight = _FsTankHeight_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 2, 1, 2),
    _FsTankHeight_Type()
)
fsTankHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankHeight.setStatus("current")
_FsTankDimA_Type = DisplayString
_FsTankDimA_Object = MibTableColumn
fsTankDimA = _FsTankDimA_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 2, 1, 3),
    _FsTankDimA_Type()
)
fsTankDimA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankDimA.setStatus("current")
_FsTankDimB_Type = DisplayString
_FsTankDimB_Object = MibTableColumn
fsTankDimB = _FsTankDimB_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 2, 1, 4),
    _FsTankDimB_Type()
)
fsTankDimB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankDimB.setStatus("current")
_FsTankVolume_Type = DisplayString
_FsTankVolume_Object = MibTableColumn
fsTankVolume = _FsTankVolume_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 2, 1, 5),
    _FsTankVolume_Type()
)
fsTankVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankVolume.setStatus("current")
_FsTankVolumeUnit_Type = DisplayString
_FsTankVolumeUnit_Object = MibTableColumn
fsTankVolumeUnit = _FsTankVolumeUnit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 2, 1, 6),
    _FsTankVolumeUnit_Type()
)
fsTankVolumeUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankVolumeUnit.setStatus("current")
_FsTankShape_Type = DisplayString
_FsTankShape_Object = MibTableColumn
fsTankShape = _FsTankShape_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 2, 1, 7),
    _FsTankShape_Type()
)
fsTankShape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTankShape.setStatus("current")
_FuelSensorCustomTankTable_Object = MibTable
fuelSensorCustomTankTable = _FuelSensorCustomTankTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 3)
)
if mibBuilder.loadTexts:
    fuelSensorCustomTankTable.setStatus("current")
_FsCustomTankEntry_Object = MibTableRow
fsCustomTankEntry = _FsCustomTankEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 3, 1)
)
fsCustomTankEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "fsCustomTankIndexFS"),
    (0, "SITEBOSS-350-STD-MIB", "fsCustomTankIndexDatum"),
)
if mibBuilder.loadTexts:
    fsCustomTankEntry.setStatus("current")


class _FsCustomTankIndexFS_Type(Integer32):
    """Custom type fsCustomTankIndexFS based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsCustomTankIndexFS_Type.__name__ = "Integer32"
_FsCustomTankIndexFS_Object = MibTableColumn
fsCustomTankIndexFS = _FsCustomTankIndexFS_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 3, 1, 1),
    _FsCustomTankIndexFS_Type()
)
fsCustomTankIndexFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCustomTankIndexFS.setStatus("current")


class _FsCustomTankIndexDatum_Type(Integer32):
    """Custom type fsCustomTankIndexDatum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_FsCustomTankIndexDatum_Type.__name__ = "Integer32"
_FsCustomTankIndexDatum_Object = MibTableColumn
fsCustomTankIndexDatum = _FsCustomTankIndexDatum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 3, 1, 2),
    _FsCustomTankIndexDatum_Type()
)
fsCustomTankIndexDatum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsCustomTankIndexDatum.setStatus("current")
_FsCustomTankHeight_Type = DisplayString
_FsCustomTankHeight_Object = MibTableColumn
fsCustomTankHeight = _FsCustomTankHeight_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 3, 1, 3),
    _FsCustomTankHeight_Type()
)
fsCustomTankHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCustomTankHeight.setStatus("current")
_FsCustomTankVolume_Type = DisplayString
_FsCustomTankVolume_Object = MibTableColumn
fsCustomTankVolume = _FsCustomTankVolume_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 3, 1, 4),
    _FsCustomTankVolume_Type()
)
fsCustomTankVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsCustomTankVolume.setStatus("current")
_FuelSensorVolumeTable_Object = MibTable
fuelSensorVolumeTable = _FuelSensorVolumeTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4)
)
if mibBuilder.loadTexts:
    fuelSensorVolumeTable.setStatus("current")
_FsVolumeEntry_Object = MibTableRow
fsVolumeEntry = _FsVolumeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1)
)
fsVolumeEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "fsVolumeIndex"),
)
if mibBuilder.loadTexts:
    fsVolumeEntry.setStatus("current")


class _FsVolumeIndex_Type(Integer32):
    """Custom type fsVolumeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsVolumeIndex_Type.__name__ = "Integer32"
_FsVolumeIndex_Object = MibTableColumn
fsVolumeIndex = _FsVolumeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 1),
    _FsVolumeIndex_Type()
)
fsVolumeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsVolumeIndex.setStatus("current")
_FsVolumeEnable_Type = DisplayString
_FsVolumeEnable_Object = MibTableColumn
fsVolumeEnable = _FsVolumeEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 2),
    _FsVolumeEnable_Type()
)
fsVolumeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeEnable.setStatus("current")
_FsVolumeDeadband_Type = DisplayString
_FsVolumeDeadband_Object = MibTableColumn
fsVolumeDeadband = _FsVolumeDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 3),
    _FsVolumeDeadband_Type()
)
fsVolumeDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeDeadband.setStatus("current")
_FsVolumeVHighValue_Type = DisplayString
_FsVolumeVHighValue_Object = MibTableColumn
fsVolumeVHighValue = _FsVolumeVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 4),
    _FsVolumeVHighValue_Type()
)
fsVolumeVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVHighValue.setStatus("current")
_FsVolumeVHighActions_Type = DisplayString
_FsVolumeVHighActions_Object = MibTableColumn
fsVolumeVHighActions = _FsVolumeVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 5),
    _FsVolumeVHighActions_Type()
)
fsVolumeVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVHighActions.setStatus("current")


class _FsVolumeVHighTrapNum_Type(Integer32):
    """Custom type fsVolumeVHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(519, 1199),
    )


_FsVolumeVHighTrapNum_Type.__name__ = "Integer32"
_FsVolumeVHighTrapNum_Object = MibTableColumn
fsVolumeVHighTrapNum = _FsVolumeVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 6),
    _FsVolumeVHighTrapNum_Type()
)
fsVolumeVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVHighTrapNum.setStatus("current")
_FsVolumeVHighClass_Type = DisplayString
_FsVolumeVHighClass_Object = MibTableColumn
fsVolumeVHighClass = _FsVolumeVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 7),
    _FsVolumeVHighClass_Type()
)
fsVolumeVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVHighClass.setStatus("current")
_FsVolumeHighValue_Type = DisplayString
_FsVolumeHighValue_Object = MibTableColumn
fsVolumeHighValue = _FsVolumeHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 8),
    _FsVolumeHighValue_Type()
)
fsVolumeHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeHighValue.setStatus("current")
_FsVolumeHighActions_Type = DisplayString
_FsVolumeHighActions_Object = MibTableColumn
fsVolumeHighActions = _FsVolumeHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 9),
    _FsVolumeHighActions_Type()
)
fsVolumeHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeHighActions.setStatus("current")


class _FsVolumeHighTrapNum_Type(Integer32):
    """Custom type fsVolumeHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(519, 1199),
    )


_FsVolumeHighTrapNum_Type.__name__ = "Integer32"
_FsVolumeHighTrapNum_Object = MibTableColumn
fsVolumeHighTrapNum = _FsVolumeHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 10),
    _FsVolumeHighTrapNum_Type()
)
fsVolumeHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeHighTrapNum.setStatus("current")
_FsVolumeHighClass_Type = DisplayString
_FsVolumeHighClass_Object = MibTableColumn
fsVolumeHighClass = _FsVolumeHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 11),
    _FsVolumeHighClass_Type()
)
fsVolumeHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeHighClass.setStatus("current")
_FsVolumeNormalActions_Type = DisplayString
_FsVolumeNormalActions_Object = MibTableColumn
fsVolumeNormalActions = _FsVolumeNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 12),
    _FsVolumeNormalActions_Type()
)
fsVolumeNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeNormalActions.setStatus("current")


class _FsVolumeNormalTrapNum_Type(Integer32):
    """Custom type fsVolumeNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(519, 1199),
    )


_FsVolumeNormalTrapNum_Type.__name__ = "Integer32"
_FsVolumeNormalTrapNum_Object = MibTableColumn
fsVolumeNormalTrapNum = _FsVolumeNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 13),
    _FsVolumeNormalTrapNum_Type()
)
fsVolumeNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeNormalTrapNum.setStatus("current")
_FsVolumeNormalClass_Type = DisplayString
_FsVolumeNormalClass_Object = MibTableColumn
fsVolumeNormalClass = _FsVolumeNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 14),
    _FsVolumeNormalClass_Type()
)
fsVolumeNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeNormalClass.setStatus("current")
_FsVolumeLowValue_Type = DisplayString
_FsVolumeLowValue_Object = MibTableColumn
fsVolumeLowValue = _FsVolumeLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 15),
    _FsVolumeLowValue_Type()
)
fsVolumeLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeLowValue.setStatus("current")
_FsVolumeLowActions_Type = DisplayString
_FsVolumeLowActions_Object = MibTableColumn
fsVolumeLowActions = _FsVolumeLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 16),
    _FsVolumeLowActions_Type()
)
fsVolumeLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeLowActions.setStatus("current")


class _FsVolumeLowTrapNum_Type(Integer32):
    """Custom type fsVolumeLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(519, 1199),
    )


_FsVolumeLowTrapNum_Type.__name__ = "Integer32"
_FsVolumeLowTrapNum_Object = MibTableColumn
fsVolumeLowTrapNum = _FsVolumeLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 17),
    _FsVolumeLowTrapNum_Type()
)
fsVolumeLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeLowTrapNum.setStatus("current")
_FsVolumeLowClass_Type = DisplayString
_FsVolumeLowClass_Object = MibTableColumn
fsVolumeLowClass = _FsVolumeLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 18),
    _FsVolumeLowClass_Type()
)
fsVolumeLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeLowClass.setStatus("current")
_FsVolumeVLowValue_Type = DisplayString
_FsVolumeVLowValue_Object = MibTableColumn
fsVolumeVLowValue = _FsVolumeVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 19),
    _FsVolumeVLowValue_Type()
)
fsVolumeVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVLowValue.setStatus("current")
_FsVolumeVLowActions_Type = DisplayString
_FsVolumeVLowActions_Object = MibTableColumn
fsVolumeVLowActions = _FsVolumeVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 20),
    _FsVolumeVLowActions_Type()
)
fsVolumeVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVLowActions.setStatus("current")


class _FsVolumeVLowTrapNum_Type(Integer32):
    """Custom type fsVolumeVLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(519, 1199),
    )


_FsVolumeVLowTrapNum_Type.__name__ = "Integer32"
_FsVolumeVLowTrapNum_Object = MibTableColumn
fsVolumeVLowTrapNum = _FsVolumeVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 21),
    _FsVolumeVLowTrapNum_Type()
)
fsVolumeVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVLowTrapNum.setStatus("current")
_FsVolumeVLowClass_Type = DisplayString
_FsVolumeVLowClass_Object = MibTableColumn
fsVolumeVLowClass = _FsVolumeVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 4, 1, 22),
    _FsVolumeVLowClass_Type()
)
fsVolumeVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsVolumeVLowClass.setStatus("current")
_FuelSensorDisconnectTable_Object = MibTable
fuelSensorDisconnectTable = _FuelSensorDisconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5)
)
if mibBuilder.loadTexts:
    fuelSensorDisconnectTable.setStatus("current")
_FsDiscEntry_Object = MibTableRow
fsDiscEntry = _FsDiscEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1)
)
fsDiscEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "fsDiscIndex"),
)
if mibBuilder.loadTexts:
    fsDiscEntry.setStatus("current")


class _FsDiscIndex_Type(Integer32):
    """Custom type fsDiscIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsDiscIndex_Type.__name__ = "Integer32"
_FsDiscIndex_Object = MibTableColumn
fsDiscIndex = _FsDiscIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1, 1),
    _FsDiscIndex_Type()
)
fsDiscIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDiscIndex.setStatus("current")
_FsDiscEnable_Type = DisplayString
_FsDiscEnable_Object = MibTableColumn
fsDiscEnable = _FsDiscEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1, 2),
    _FsDiscEnable_Type()
)
fsDiscEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscEnable.setStatus("current")
_FsDiscHighValue_Type = DisplayString
_FsDiscHighValue_Object = MibTableColumn
fsDiscHighValue = _FsDiscHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1, 3),
    _FsDiscHighValue_Type()
)
fsDiscHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscHighValue.setStatus("current")
_FsDiscLowValue_Type = DisplayString
_FsDiscLowValue_Object = MibTableColumn
fsDiscLowValue = _FsDiscLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1, 4),
    _FsDiscLowValue_Type()
)
fsDiscLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscLowValue.setStatus("current")
_FsDiscActions_Type = DisplayString
_FsDiscActions_Object = MibTableColumn
fsDiscActions = _FsDiscActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1, 5),
    _FsDiscActions_Type()
)
fsDiscActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscActions.setStatus("current")


class _FsDiscTrapNum_Type(Integer32):
    """Custom type fsDiscTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(515, 1199),
    )


_FsDiscTrapNum_Type.__name__ = "Integer32"
_FsDiscTrapNum_Object = MibTableColumn
fsDiscTrapNum = _FsDiscTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1, 6),
    _FsDiscTrapNum_Type()
)
fsDiscTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscTrapNum.setStatus("current")
_FsDiscClass_Type = DisplayString
_FsDiscClass_Object = MibTableColumn
fsDiscClass = _FsDiscClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1, 7),
    _FsDiscClass_Type()
)
fsDiscClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscClass.setStatus("current")
_FsDiscNormalActions_Type = DisplayString
_FsDiscNormalActions_Object = MibTableColumn
fsDiscNormalActions = _FsDiscNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1, 8),
    _FsDiscNormalActions_Type()
)
fsDiscNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscNormalActions.setStatus("current")


class _FsDiscNormalTrapNum_Type(Integer32):
    """Custom type fsDiscNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(515, 1199),
    )


_FsDiscNormalTrapNum_Type.__name__ = "Integer32"
_FsDiscNormalTrapNum_Object = MibTableColumn
fsDiscNormalTrapNum = _FsDiscNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1, 9),
    _FsDiscNormalTrapNum_Type()
)
fsDiscNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscNormalTrapNum.setStatus("current")
_FsDiscNormalClass_Type = DisplayString
_FsDiscNormalClass_Object = MibTableColumn
fsDiscNormalClass = _FsDiscNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 5, 1, 10),
    _FsDiscNormalClass_Type()
)
fsDiscNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDiscNormalClass.setStatus("current")
_FuelSensorSuddenChangeTable_Object = MibTable
fuelSensorSuddenChangeTable = _FuelSensorSuddenChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 6)
)
if mibBuilder.loadTexts:
    fuelSensorSuddenChangeTable.setStatus("current")
_FsSuddenChangeEntry_Object = MibTableRow
fsSuddenChangeEntry = _FsSuddenChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 6, 1)
)
fsSuddenChangeEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "fsSuddenChangeIndex"),
)
if mibBuilder.loadTexts:
    fsSuddenChangeEntry.setStatus("current")


class _FsSuddenChangeIndex_Type(Integer32):
    """Custom type fsSuddenChangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsSuddenChangeIndex_Type.__name__ = "Integer32"
_FsSuddenChangeIndex_Object = MibTableColumn
fsSuddenChangeIndex = _FsSuddenChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 6, 1, 1),
    _FsSuddenChangeIndex_Type()
)
fsSuddenChangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSuddenChangeIndex.setStatus("current")
_FsSuddenChangeEnable_Type = DisplayString
_FsSuddenChangeEnable_Object = MibTableColumn
fsSuddenChangeEnable = _FsSuddenChangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 6, 1, 2),
    _FsSuddenChangeEnable_Type()
)
fsSuddenChangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSuddenChangeEnable.setStatus("current")


class _FsSuddenChangeTime_Type(Integer32):
    """Custom type fsSuddenChangeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 360),
    )


_FsSuddenChangeTime_Type.__name__ = "Integer32"
_FsSuddenChangeTime_Object = MibTableColumn
fsSuddenChangeTime = _FsSuddenChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 6, 1, 3),
    _FsSuddenChangeTime_Type()
)
fsSuddenChangeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSuddenChangeTime.setStatus("current")
_FsSuddenChangeAmplitude_Type = DisplayString
_FsSuddenChangeAmplitude_Object = MibTableColumn
fsSuddenChangeAmplitude = _FsSuddenChangeAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 6, 1, 4),
    _FsSuddenChangeAmplitude_Type()
)
fsSuddenChangeAmplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSuddenChangeAmplitude.setStatus("current")
_FsSuddenChangeActions_Type = DisplayString
_FsSuddenChangeActions_Object = MibTableColumn
fsSuddenChangeActions = _FsSuddenChangeActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 6, 1, 5),
    _FsSuddenChangeActions_Type()
)
fsSuddenChangeActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSuddenChangeActions.setStatus("current")


class _FsSuddenChangeTrapNum_Type(Integer32):
    """Custom type fsSuddenChangeTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(527, 1199),
    )


_FsSuddenChangeTrapNum_Type.__name__ = "Integer32"
_FsSuddenChangeTrapNum_Object = MibTableColumn
fsSuddenChangeTrapNum = _FsSuddenChangeTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 6, 1, 6),
    _FsSuddenChangeTrapNum_Type()
)
fsSuddenChangeTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSuddenChangeTrapNum.setStatus("current")
_FsSuddenChangeClass_Type = DisplayString
_FsSuddenChangeClass_Object = MibTableColumn
fsSuddenChangeClass = _FsSuddenChangeClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 6, 1, 7),
    _FsSuddenChangeClass_Type()
)
fsSuddenChangeClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSuddenChangeClass.setStatus("current")
_FuelSensorSlowChangeTable_Object = MibTable
fuelSensorSlowChangeTable = _FuelSensorSlowChangeTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 7)
)
if mibBuilder.loadTexts:
    fuelSensorSlowChangeTable.setStatus("current")
_FsSlowChangeEntry_Object = MibTableRow
fsSlowChangeEntry = _FsSlowChangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 7, 1)
)
fsSlowChangeEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "fsSlowChangeIndex"),
)
if mibBuilder.loadTexts:
    fsSlowChangeEntry.setStatus("current")


class _FsSlowChangeIndex_Type(Integer32):
    """Custom type fsSlowChangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsSlowChangeIndex_Type.__name__ = "Integer32"
_FsSlowChangeIndex_Object = MibTableColumn
fsSlowChangeIndex = _FsSlowChangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 7, 1, 1),
    _FsSlowChangeIndex_Type()
)
fsSlowChangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSlowChangeIndex.setStatus("current")
_FsSlowChangeEnable_Type = DisplayString
_FsSlowChangeEnable_Object = MibTableColumn
fsSlowChangeEnable = _FsSlowChangeEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 7, 1, 2),
    _FsSlowChangeEnable_Type()
)
fsSlowChangeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSlowChangeEnable.setStatus("current")


class _FsSlowChangeTime_Type(Integer32):
    """Custom type fsSlowChangeTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 168),
    )


_FsSlowChangeTime_Type.__name__ = "Integer32"
_FsSlowChangeTime_Object = MibTableColumn
fsSlowChangeTime = _FsSlowChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 7, 1, 3),
    _FsSlowChangeTime_Type()
)
fsSlowChangeTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSlowChangeTime.setStatus("current")
_FsSlowChangeAmplitude_Type = DisplayString
_FsSlowChangeAmplitude_Object = MibTableColumn
fsSlowChangeAmplitude = _FsSlowChangeAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 7, 1, 4),
    _FsSlowChangeAmplitude_Type()
)
fsSlowChangeAmplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSlowChangeAmplitude.setStatus("current")
_FsSlowChangeActions_Type = DisplayString
_FsSlowChangeActions_Object = MibTableColumn
fsSlowChangeActions = _FsSlowChangeActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 7, 1, 5),
    _FsSlowChangeActions_Type()
)
fsSlowChangeActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSlowChangeActions.setStatus("current")


class _FsSlowChangeTrapNum_Type(Integer32):
    """Custom type fsSlowChangeTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(528, 1199),
    )


_FsSlowChangeTrapNum_Type.__name__ = "Integer32"
_FsSlowChangeTrapNum_Object = MibTableColumn
fsSlowChangeTrapNum = _FsSlowChangeTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 7, 1, 6),
    _FsSlowChangeTrapNum_Type()
)
fsSlowChangeTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSlowChangeTrapNum.setStatus("current")
_FsSlowChangeClass_Type = DisplayString
_FsSlowChangeClass_Object = MibTableColumn
fsSlowChangeClass = _FsSlowChangeClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 7, 1, 7),
    _FsSlowChangeClass_Type()
)
fsSlowChangeClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsSlowChangeClass.setStatus("current")
_FuelSensorLevelsAutoAdjustTable_Object = MibTable
fuelSensorLevelsAutoAdjustTable = _FuelSensorLevelsAutoAdjustTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 8)
)
if mibBuilder.loadTexts:
    fuelSensorLevelsAutoAdjustTable.setStatus("current")
_FsLAAEntry_Object = MibTableRow
fsLAAEntry = _FsLAAEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 8, 1)
)
fsLAAEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "fsLAAIndex"),
)
if mibBuilder.loadTexts:
    fsLAAEntry.setStatus("current")


class _FsLAAIndex_Type(Integer32):
    """Custom type fsLAAIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FsLAAIndex_Type.__name__ = "Integer32"
_FsLAAIndex_Object = MibTableColumn
fsLAAIndex = _FsLAAIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 8, 1, 1),
    _FsLAAIndex_Type()
)
fsLAAIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsLAAIndex.setStatus("current")
_FsLAAEnable_Type = DisplayString
_FsLAAEnable_Object = MibTableColumn
fsLAAEnable = _FsLAAEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 8, 1, 2),
    _FsLAAEnable_Type()
)
fsLAAEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLAAEnable.setStatus("current")
_FsLAAEventEnable_Type = DisplayString
_FsLAAEventEnable_Object = MibTableColumn
fsLAAEventEnable = _FsLAAEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 8, 1, 3),
    _FsLAAEventEnable_Type()
)
fsLAAEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLAAEventEnable.setStatus("current")


class _FsLAAEventThreshold_Type(Integer32):
    """Custom type fsLAAEventThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 50),
    )


_FsLAAEventThreshold_Type.__name__ = "Integer32"
_FsLAAEventThreshold_Object = MibTableColumn
fsLAAEventThreshold = _FsLAAEventThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 8, 1, 4),
    _FsLAAEventThreshold_Type()
)
fsLAAEventThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLAAEventThreshold.setStatus("current")
_FsLAAEventActions_Type = DisplayString
_FsLAAEventActions_Object = MibTableColumn
fsLAAEventActions = _FsLAAEventActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 8, 1, 5),
    _FsLAAEventActions_Type()
)
fsLAAEventActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLAAEventActions.setStatus("current")
_FsLAAEventClass_Type = DisplayString
_FsLAAEventClass_Object = MibTableColumn
fsLAAEventClass = _FsLAAEventClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 8, 1, 6),
    _FsLAAEventClass_Type()
)
fsLAAEventClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLAAEventClass.setStatus("current")


class _FsLAAEventTrapNum_Type(Integer32):
    """Custom type fsLAAEventTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(544, 1199),
    )


_FsLAAEventTrapNum_Type.__name__ = "Integer32"
_FsLAAEventTrapNum_Object = MibTableColumn
fsLAAEventTrapNum = _FsLAAEventTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 11, 8, 1, 7),
    _FsLAAEventTrapNum_Type()
)
fsLAAEventTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsLAAEventTrapNum.setStatus("current")
_AcPowerMonitor_ObjectIdentity = ObjectIdentity
acPowerMonitor = _AcPowerMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12)
)
_AcpmGeneralTable_Object = MibTable
acpmGeneralTable = _AcpmGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1)
)
if mibBuilder.loadTexts:
    acpmGeneralTable.setStatus("current")
_AcpmGenEntry_Object = MibTableRow
acpmGenEntry = _AcpmGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1)
)
acpmGenEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "acpmGenIndex"),
)
if mibBuilder.loadTexts:
    acpmGenEntry.setStatus("current")


class _AcpmGenIndex_Type(Integer32):
    """Custom type acpmGenIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmGenIndex_Type.__name__ = "Integer32"
_AcpmGenIndex_Object = MibTableColumn
acpmGenIndex = _AcpmGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1, 1),
    _AcpmGenIndex_Type()
)
acpmGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmGenIndex.setStatus("current")
_AcpmGenDevice_Type = DisplayString
_AcpmGenDevice_Object = MibTableColumn
acpmGenDevice = _AcpmGenDevice_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1, 2),
    _AcpmGenDevice_Type()
)
acpmGenDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenDevice.setStatus("current")
_AcpmGenName_Type = DisplayString
_AcpmGenName_Object = MibTableColumn
acpmGenName = _AcpmGenName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1, 3),
    _AcpmGenName_Type()
)
acpmGenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenName.setStatus("current")


class _AcpmGenAddress_Type(Integer32):
    """Custom type acpmGenAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 247),
    )


_AcpmGenAddress_Type.__name__ = "Integer32"
_AcpmGenAddress_Object = MibTableColumn
acpmGenAddress = _AcpmGenAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1, 4),
    _AcpmGenAddress_Type()
)
acpmGenAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenAddress.setStatus("current")


class _AcpmGenPtRatio_Type(Integer32):
    """Custom type acpmGenPtRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AcpmGenPtRatio_Type.__name__ = "Integer32"
_AcpmGenPtRatio_Object = MibTableColumn
acpmGenPtRatio = _AcpmGenPtRatio_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1, 5),
    _AcpmGenPtRatio_Type()
)
acpmGenPtRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenPtRatio.setStatus("current")


class _AcpmGenCtRatio_Type(Integer32):
    """Custom type acpmGenCtRatio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AcpmGenCtRatio_Type.__name__ = "Integer32"
_AcpmGenCtRatio_Object = MibTableColumn
acpmGenCtRatio = _AcpmGenCtRatio_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1, 6),
    _AcpmGenCtRatio_Type()
)
acpmGenCtRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenCtRatio.setStatus("current")
_AcpmGenPowerType_Type = DisplayString
_AcpmGenPowerType_Object = MibTableColumn
acpmGenPowerType = _AcpmGenPowerType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1, 7),
    _AcpmGenPowerType_Type()
)
acpmGenPowerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenPowerType.setStatus("current")


class _AcpmGenSysrepPackage_Type(Integer32):
    """Custom type acpmGenSysrepPackage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_AcpmGenSysrepPackage_Type.__name__ = "Integer32"
_AcpmGenSysrepPackage_Object = MibTableColumn
acpmGenSysrepPackage = _AcpmGenSysrepPackage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1, 8),
    _AcpmGenSysrepPackage_Type()
)
acpmGenSysrepPackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenSysrepPackage.setStatus("current")
_AcpmGenSysrepType_Type = DisplayString
_AcpmGenSysrepType_Object = MibTableColumn
acpmGenSysrepType = _AcpmGenSysrepType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1, 9),
    _AcpmGenSysrepType_Type()
)
acpmGenSysrepType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenSysrepType.setStatus("current")
_AcpmGenEnable_Type = DisplayString
_AcpmGenEnable_Object = MibTableColumn
acpmGenEnable = _AcpmGenEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 1, 1, 10),
    _AcpmGenEnable_Type()
)
acpmGenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmGenEnable.setStatus("current")
_AcpmAvgVoltageTable_Object = MibTable
acpmAvgVoltageTable = _AcpmAvgVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2)
)
if mibBuilder.loadTexts:
    acpmAvgVoltageTable.setStatus("current")
_AcpmAvgVoltageEntry_Object = MibTableRow
acpmAvgVoltageEntry = _AcpmAvgVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1)
)
acpmAvgVoltageEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "acpmAvgVoltageIndex"),
)
if mibBuilder.loadTexts:
    acpmAvgVoltageEntry.setStatus("current")


class _AcpmAvgVoltageIndex_Type(Integer32):
    """Custom type acpmAvgVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmAvgVoltageIndex_Type.__name__ = "Integer32"
_AcpmAvgVoltageIndex_Object = MibTableColumn
acpmAvgVoltageIndex = _AcpmAvgVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 1),
    _AcpmAvgVoltageIndex_Type()
)
acpmAvgVoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmAvgVoltageIndex.setStatus("current")
_AcpmAvgVoltageEnable_Type = DisplayString
_AcpmAvgVoltageEnable_Object = MibTableColumn
acpmAvgVoltageEnable = _AcpmAvgVoltageEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 2),
    _AcpmAvgVoltageEnable_Type()
)
acpmAvgVoltageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageEnable.setStatus("current")
_AcpmAvgVoltageDeadband_Type = DisplayString
_AcpmAvgVoltageDeadband_Object = MibTableColumn
acpmAvgVoltageDeadband = _AcpmAvgVoltageDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 3),
    _AcpmAvgVoltageDeadband_Type()
)
acpmAvgVoltageDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageDeadband.setStatus("current")
_AcpmAvgVoltageVHighValue_Type = DisplayString
_AcpmAvgVoltageVHighValue_Object = MibTableColumn
acpmAvgVoltageVHighValue = _AcpmAvgVoltageVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 4),
    _AcpmAvgVoltageVHighValue_Type()
)
acpmAvgVoltageVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVHighValue.setStatus("current")
_AcpmAvgVoltageVHighActions_Type = DisplayString
_AcpmAvgVoltageVHighActions_Object = MibTableColumn
acpmAvgVoltageVHighActions = _AcpmAvgVoltageVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 5),
    _AcpmAvgVoltageVHighActions_Type()
)
acpmAvgVoltageVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVHighActions.setStatus("current")


class _AcpmAvgVoltageVHighTrapNum_Type(Integer32):
    """Custom type acpmAvgVoltageVHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(520, 1199),
    )


_AcpmAvgVoltageVHighTrapNum_Type.__name__ = "Integer32"
_AcpmAvgVoltageVHighTrapNum_Object = MibTableColumn
acpmAvgVoltageVHighTrapNum = _AcpmAvgVoltageVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 6),
    _AcpmAvgVoltageVHighTrapNum_Type()
)
acpmAvgVoltageVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVHighTrapNum.setStatus("current")
_AcpmAvgVoltageVHighClass_Type = DisplayString
_AcpmAvgVoltageVHighClass_Object = MibTableColumn
acpmAvgVoltageVHighClass = _AcpmAvgVoltageVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 7),
    _AcpmAvgVoltageVHighClass_Type()
)
acpmAvgVoltageVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVHighClass.setStatus("current")
_AcpmAvgVoltageHighValue_Type = DisplayString
_AcpmAvgVoltageHighValue_Object = MibTableColumn
acpmAvgVoltageHighValue = _AcpmAvgVoltageHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 8),
    _AcpmAvgVoltageHighValue_Type()
)
acpmAvgVoltageHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageHighValue.setStatus("current")
_AcpmAvgVoltageHighActions_Type = DisplayString
_AcpmAvgVoltageHighActions_Object = MibTableColumn
acpmAvgVoltageHighActions = _AcpmAvgVoltageHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 9),
    _AcpmAvgVoltageHighActions_Type()
)
acpmAvgVoltageHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageHighActions.setStatus("current")


class _AcpmAvgVoltageHighTrapNum_Type(Integer32):
    """Custom type acpmAvgVoltageHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(520, 1199),
    )


_AcpmAvgVoltageHighTrapNum_Type.__name__ = "Integer32"
_AcpmAvgVoltageHighTrapNum_Object = MibTableColumn
acpmAvgVoltageHighTrapNum = _AcpmAvgVoltageHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 10),
    _AcpmAvgVoltageHighTrapNum_Type()
)
acpmAvgVoltageHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageHighTrapNum.setStatus("current")
_AcpmAvgVoltageHighClass_Type = DisplayString
_AcpmAvgVoltageHighClass_Object = MibTableColumn
acpmAvgVoltageHighClass = _AcpmAvgVoltageHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 11),
    _AcpmAvgVoltageHighClass_Type()
)
acpmAvgVoltageHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageHighClass.setStatus("current")
_AcpmAvgVoltageNormalActions_Type = DisplayString
_AcpmAvgVoltageNormalActions_Object = MibTableColumn
acpmAvgVoltageNormalActions = _AcpmAvgVoltageNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 12),
    _AcpmAvgVoltageNormalActions_Type()
)
acpmAvgVoltageNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageNormalActions.setStatus("current")


class _AcpmAvgVoltageNormalTrapNum_Type(Integer32):
    """Custom type acpmAvgVoltageNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(520, 1199),
    )


_AcpmAvgVoltageNormalTrapNum_Type.__name__ = "Integer32"
_AcpmAvgVoltageNormalTrapNum_Object = MibTableColumn
acpmAvgVoltageNormalTrapNum = _AcpmAvgVoltageNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 13),
    _AcpmAvgVoltageNormalTrapNum_Type()
)
acpmAvgVoltageNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageNormalTrapNum.setStatus("current")
_AcpmAvgVoltageNormalClass_Type = DisplayString
_AcpmAvgVoltageNormalClass_Object = MibTableColumn
acpmAvgVoltageNormalClass = _AcpmAvgVoltageNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 14),
    _AcpmAvgVoltageNormalClass_Type()
)
acpmAvgVoltageNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageNormalClass.setStatus("current")
_AcpmAvgVoltageLowValue_Type = DisplayString
_AcpmAvgVoltageLowValue_Object = MibTableColumn
acpmAvgVoltageLowValue = _AcpmAvgVoltageLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 15),
    _AcpmAvgVoltageLowValue_Type()
)
acpmAvgVoltageLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageLowValue.setStatus("current")
_AcpmAvgVoltageLowActions_Type = DisplayString
_AcpmAvgVoltageLowActions_Object = MibTableColumn
acpmAvgVoltageLowActions = _AcpmAvgVoltageLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 16),
    _AcpmAvgVoltageLowActions_Type()
)
acpmAvgVoltageLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageLowActions.setStatus("current")


class _AcpmAvgVoltageLowTrapNum_Type(Integer32):
    """Custom type acpmAvgVoltageLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(520, 1199),
    )


_AcpmAvgVoltageLowTrapNum_Type.__name__ = "Integer32"
_AcpmAvgVoltageLowTrapNum_Object = MibTableColumn
acpmAvgVoltageLowTrapNum = _AcpmAvgVoltageLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 17),
    _AcpmAvgVoltageLowTrapNum_Type()
)
acpmAvgVoltageLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageLowTrapNum.setStatus("current")
_AcpmAvgVoltageLowClass_Type = DisplayString
_AcpmAvgVoltageLowClass_Object = MibTableColumn
acpmAvgVoltageLowClass = _AcpmAvgVoltageLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 18),
    _AcpmAvgVoltageLowClass_Type()
)
acpmAvgVoltageLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageLowClass.setStatus("current")
_AcpmAvgVoltageVLowValue_Type = DisplayString
_AcpmAvgVoltageVLowValue_Object = MibTableColumn
acpmAvgVoltageVLowValue = _AcpmAvgVoltageVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 19),
    _AcpmAvgVoltageVLowValue_Type()
)
acpmAvgVoltageVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVLowValue.setStatus("current")
_AcpmAvgVoltageVLowActions_Type = DisplayString
_AcpmAvgVoltageVLowActions_Object = MibTableColumn
acpmAvgVoltageVLowActions = _AcpmAvgVoltageVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 20),
    _AcpmAvgVoltageVLowActions_Type()
)
acpmAvgVoltageVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVLowActions.setStatus("current")


class _AcpmAvgVoltageVLowTrapNum_Type(Integer32):
    """Custom type acpmAvgVoltageVLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(520, 1199),
    )


_AcpmAvgVoltageVLowTrapNum_Type.__name__ = "Integer32"
_AcpmAvgVoltageVLowTrapNum_Object = MibTableColumn
acpmAvgVoltageVLowTrapNum = _AcpmAvgVoltageVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 21),
    _AcpmAvgVoltageVLowTrapNum_Type()
)
acpmAvgVoltageVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVLowTrapNum.setStatus("current")
_AcpmAvgVoltageVLowClass_Type = DisplayString
_AcpmAvgVoltageVLowClass_Object = MibTableColumn
acpmAvgVoltageVLowClass = _AcpmAvgVoltageVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 22),
    _AcpmAvgVoltageVLowClass_Type()
)
acpmAvgVoltageVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageVLowClass.setStatus("current")
_AcpmAvgVoltageSysrepEnable_Type = DisplayString
_AcpmAvgVoltageSysrepEnable_Object = MibTableColumn
acpmAvgVoltageSysrepEnable = _AcpmAvgVoltageSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 23),
    _AcpmAvgVoltageSysrepEnable_Type()
)
acpmAvgVoltageSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageSysrepEnable.setStatus("current")
_AcpmAvgVoltageSysrepThreshold_Type = DisplayString
_AcpmAvgVoltageSysrepThreshold_Object = MibTableColumn
acpmAvgVoltageSysrepThreshold = _AcpmAvgVoltageSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 24),
    _AcpmAvgVoltageSysrepThreshold_Type()
)
acpmAvgVoltageSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageSysrepThreshold.setStatus("current")
_AcpmAvgVoltageSysrepLimit_Type = Integer32
_AcpmAvgVoltageSysrepLimit_Object = MibTableColumn
acpmAvgVoltageSysrepLimit = _AcpmAvgVoltageSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 2, 1, 25),
    _AcpmAvgVoltageSysrepLimit_Type()
)
acpmAvgVoltageSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgVoltageSysrepLimit.setStatus("current")
_AcpmAvgCurrentTable_Object = MibTable
acpmAvgCurrentTable = _AcpmAvgCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3)
)
if mibBuilder.loadTexts:
    acpmAvgCurrentTable.setStatus("current")
_AcpmAvgCurrentEntry_Object = MibTableRow
acpmAvgCurrentEntry = _AcpmAvgCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1)
)
acpmAvgCurrentEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "acpmAvgCurrentIndex"),
)
if mibBuilder.loadTexts:
    acpmAvgCurrentEntry.setStatus("current")


class _AcpmAvgCurrentIndex_Type(Integer32):
    """Custom type acpmAvgCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmAvgCurrentIndex_Type.__name__ = "Integer32"
_AcpmAvgCurrentIndex_Object = MibTableColumn
acpmAvgCurrentIndex = _AcpmAvgCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 1),
    _AcpmAvgCurrentIndex_Type()
)
acpmAvgCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmAvgCurrentIndex.setStatus("current")
_AcpmAvgCurrentEnable_Type = DisplayString
_AcpmAvgCurrentEnable_Object = MibTableColumn
acpmAvgCurrentEnable = _AcpmAvgCurrentEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 2),
    _AcpmAvgCurrentEnable_Type()
)
acpmAvgCurrentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentEnable.setStatus("current")
_AcpmAvgCurrentDeadband_Type = DisplayString
_AcpmAvgCurrentDeadband_Object = MibTableColumn
acpmAvgCurrentDeadband = _AcpmAvgCurrentDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 3),
    _AcpmAvgCurrentDeadband_Type()
)
acpmAvgCurrentDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentDeadband.setStatus("current")
_AcpmAvgCurrentVHighValue_Type = DisplayString
_AcpmAvgCurrentVHighValue_Object = MibTableColumn
acpmAvgCurrentVHighValue = _AcpmAvgCurrentVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 4),
    _AcpmAvgCurrentVHighValue_Type()
)
acpmAvgCurrentVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVHighValue.setStatus("current")
_AcpmAvgCurrentVHighActions_Type = DisplayString
_AcpmAvgCurrentVHighActions_Object = MibTableColumn
acpmAvgCurrentVHighActions = _AcpmAvgCurrentVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 5),
    _AcpmAvgCurrentVHighActions_Type()
)
acpmAvgCurrentVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVHighActions.setStatus("current")


class _AcpmAvgCurrentVHighTrapNum_Type(Integer32):
    """Custom type acpmAvgCurrentVHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(521, 1199),
    )


_AcpmAvgCurrentVHighTrapNum_Type.__name__ = "Integer32"
_AcpmAvgCurrentVHighTrapNum_Object = MibTableColumn
acpmAvgCurrentVHighTrapNum = _AcpmAvgCurrentVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 6),
    _AcpmAvgCurrentVHighTrapNum_Type()
)
acpmAvgCurrentVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVHighTrapNum.setStatus("current")
_AcpmAvgCurrentVHighClass_Type = DisplayString
_AcpmAvgCurrentVHighClass_Object = MibTableColumn
acpmAvgCurrentVHighClass = _AcpmAvgCurrentVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 7),
    _AcpmAvgCurrentVHighClass_Type()
)
acpmAvgCurrentVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVHighClass.setStatus("current")
_AcpmAvgCurrentHighValue_Type = DisplayString
_AcpmAvgCurrentHighValue_Object = MibTableColumn
acpmAvgCurrentHighValue = _AcpmAvgCurrentHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 8),
    _AcpmAvgCurrentHighValue_Type()
)
acpmAvgCurrentHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentHighValue.setStatus("current")
_AcpmAvgCurrentHighActions_Type = DisplayString
_AcpmAvgCurrentHighActions_Object = MibTableColumn
acpmAvgCurrentHighActions = _AcpmAvgCurrentHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 9),
    _AcpmAvgCurrentHighActions_Type()
)
acpmAvgCurrentHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentHighActions.setStatus("current")


class _AcpmAvgCurrentHighTrapNum_Type(Integer32):
    """Custom type acpmAvgCurrentHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(521, 1199),
    )


_AcpmAvgCurrentHighTrapNum_Type.__name__ = "Integer32"
_AcpmAvgCurrentHighTrapNum_Object = MibTableColumn
acpmAvgCurrentHighTrapNum = _AcpmAvgCurrentHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 10),
    _AcpmAvgCurrentHighTrapNum_Type()
)
acpmAvgCurrentHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentHighTrapNum.setStatus("current")
_AcpmAvgCurrentHighClass_Type = DisplayString
_AcpmAvgCurrentHighClass_Object = MibTableColumn
acpmAvgCurrentHighClass = _AcpmAvgCurrentHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 11),
    _AcpmAvgCurrentHighClass_Type()
)
acpmAvgCurrentHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentHighClass.setStatus("current")
_AcpmAvgCurrentNormalActions_Type = DisplayString
_AcpmAvgCurrentNormalActions_Object = MibTableColumn
acpmAvgCurrentNormalActions = _AcpmAvgCurrentNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 12),
    _AcpmAvgCurrentNormalActions_Type()
)
acpmAvgCurrentNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentNormalActions.setStatus("current")


class _AcpmAvgCurrentNormalTrapNum_Type(Integer32):
    """Custom type acpmAvgCurrentNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(521, 1199),
    )


_AcpmAvgCurrentNormalTrapNum_Type.__name__ = "Integer32"
_AcpmAvgCurrentNormalTrapNum_Object = MibTableColumn
acpmAvgCurrentNormalTrapNum = _AcpmAvgCurrentNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 13),
    _AcpmAvgCurrentNormalTrapNum_Type()
)
acpmAvgCurrentNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentNormalTrapNum.setStatus("current")
_AcpmAvgCurrentNormalClass_Type = DisplayString
_AcpmAvgCurrentNormalClass_Object = MibTableColumn
acpmAvgCurrentNormalClass = _AcpmAvgCurrentNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 14),
    _AcpmAvgCurrentNormalClass_Type()
)
acpmAvgCurrentNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentNormalClass.setStatus("current")
_AcpmAvgCurrentLowValue_Type = DisplayString
_AcpmAvgCurrentLowValue_Object = MibTableColumn
acpmAvgCurrentLowValue = _AcpmAvgCurrentLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 15),
    _AcpmAvgCurrentLowValue_Type()
)
acpmAvgCurrentLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentLowValue.setStatus("current")
_AcpmAvgCurrentLowActions_Type = DisplayString
_AcpmAvgCurrentLowActions_Object = MibTableColumn
acpmAvgCurrentLowActions = _AcpmAvgCurrentLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 16),
    _AcpmAvgCurrentLowActions_Type()
)
acpmAvgCurrentLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentLowActions.setStatus("current")


class _AcpmAvgCurrentLowTrapNum_Type(Integer32):
    """Custom type acpmAvgCurrentLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(521, 1199),
    )


_AcpmAvgCurrentLowTrapNum_Type.__name__ = "Integer32"
_AcpmAvgCurrentLowTrapNum_Object = MibTableColumn
acpmAvgCurrentLowTrapNum = _AcpmAvgCurrentLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 17),
    _AcpmAvgCurrentLowTrapNum_Type()
)
acpmAvgCurrentLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentLowTrapNum.setStatus("current")
_AcpmAvgCurrentLowClass_Type = DisplayString
_AcpmAvgCurrentLowClass_Object = MibTableColumn
acpmAvgCurrentLowClass = _AcpmAvgCurrentLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 18),
    _AcpmAvgCurrentLowClass_Type()
)
acpmAvgCurrentLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentLowClass.setStatus("current")
_AcpmAvgCurrentVLowValue_Type = DisplayString
_AcpmAvgCurrentVLowValue_Object = MibTableColumn
acpmAvgCurrentVLowValue = _AcpmAvgCurrentVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 19),
    _AcpmAvgCurrentVLowValue_Type()
)
acpmAvgCurrentVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVLowValue.setStatus("current")
_AcpmAvgCurrentVLowActions_Type = DisplayString
_AcpmAvgCurrentVLowActions_Object = MibTableColumn
acpmAvgCurrentVLowActions = _AcpmAvgCurrentVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 20),
    _AcpmAvgCurrentVLowActions_Type()
)
acpmAvgCurrentVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVLowActions.setStatus("current")


class _AcpmAvgCurrentVLowTrapNum_Type(Integer32):
    """Custom type acpmAvgCurrentVLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(521, 1199),
    )


_AcpmAvgCurrentVLowTrapNum_Type.__name__ = "Integer32"
_AcpmAvgCurrentVLowTrapNum_Object = MibTableColumn
acpmAvgCurrentVLowTrapNum = _AcpmAvgCurrentVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 21),
    _AcpmAvgCurrentVLowTrapNum_Type()
)
acpmAvgCurrentVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVLowTrapNum.setStatus("current")
_AcpmAvgCurrentVLowClass_Type = DisplayString
_AcpmAvgCurrentVLowClass_Object = MibTableColumn
acpmAvgCurrentVLowClass = _AcpmAvgCurrentVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 22),
    _AcpmAvgCurrentVLowClass_Type()
)
acpmAvgCurrentVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentVLowClass.setStatus("current")
_AcpmAvgCurrentSysrepEnable_Type = DisplayString
_AcpmAvgCurrentSysrepEnable_Object = MibTableColumn
acpmAvgCurrentSysrepEnable = _AcpmAvgCurrentSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 23),
    _AcpmAvgCurrentSysrepEnable_Type()
)
acpmAvgCurrentSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentSysrepEnable.setStatus("current")
_AcpmAvgCurrentSysrepThreshold_Type = DisplayString
_AcpmAvgCurrentSysrepThreshold_Object = MibTableColumn
acpmAvgCurrentSysrepThreshold = _AcpmAvgCurrentSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 24),
    _AcpmAvgCurrentSysrepThreshold_Type()
)
acpmAvgCurrentSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentSysrepThreshold.setStatus("current")
_AcpmAvgCurrentSysrepLimit_Type = Integer32
_AcpmAvgCurrentSysrepLimit_Object = MibTableColumn
acpmAvgCurrentSysrepLimit = _AcpmAvgCurrentSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 3, 1, 25),
    _AcpmAvgCurrentSysrepLimit_Type()
)
acpmAvgCurrentSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmAvgCurrentSysrepLimit.setStatus("current")
_AcpmFreqTable_Object = MibTable
acpmFreqTable = _AcpmFreqTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4)
)
if mibBuilder.loadTexts:
    acpmFreqTable.setStatus("current")
_AcpmFreqEntry_Object = MibTableRow
acpmFreqEntry = _AcpmFreqEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1)
)
acpmFreqEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "acpmFreqIndex"),
)
if mibBuilder.loadTexts:
    acpmFreqEntry.setStatus("current")


class _AcpmFreqIndex_Type(Integer32):
    """Custom type acpmFreqIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmFreqIndex_Type.__name__ = "Integer32"
_AcpmFreqIndex_Object = MibTableColumn
acpmFreqIndex = _AcpmFreqIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 1),
    _AcpmFreqIndex_Type()
)
acpmFreqIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmFreqIndex.setStatus("current")
_AcpmFreqEnable_Type = DisplayString
_AcpmFreqEnable_Object = MibTableColumn
acpmFreqEnable = _AcpmFreqEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 2),
    _AcpmFreqEnable_Type()
)
acpmFreqEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqEnable.setStatus("current")
_AcpmFreqDeadband_Type = DisplayString
_AcpmFreqDeadband_Object = MibTableColumn
acpmFreqDeadband = _AcpmFreqDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 3),
    _AcpmFreqDeadband_Type()
)
acpmFreqDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqDeadband.setStatus("current")
_AcpmFreqVHighValue_Type = DisplayString
_AcpmFreqVHighValue_Object = MibTableColumn
acpmFreqVHighValue = _AcpmFreqVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 4),
    _AcpmFreqVHighValue_Type()
)
acpmFreqVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVHighValue.setStatus("current")
_AcpmFreqVHighActions_Type = DisplayString
_AcpmFreqVHighActions_Object = MibTableColumn
acpmFreqVHighActions = _AcpmFreqVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 5),
    _AcpmFreqVHighActions_Type()
)
acpmFreqVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVHighActions.setStatus("current")


class _AcpmFreqVHighTrapNum_Type(Integer32):
    """Custom type acpmFreqVHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(522, 1199),
    )


_AcpmFreqVHighTrapNum_Type.__name__ = "Integer32"
_AcpmFreqVHighTrapNum_Object = MibTableColumn
acpmFreqVHighTrapNum = _AcpmFreqVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 6),
    _AcpmFreqVHighTrapNum_Type()
)
acpmFreqVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVHighTrapNum.setStatus("current")
_AcpmFreqVHighClass_Type = DisplayString
_AcpmFreqVHighClass_Object = MibTableColumn
acpmFreqVHighClass = _AcpmFreqVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 7),
    _AcpmFreqVHighClass_Type()
)
acpmFreqVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVHighClass.setStatus("current")
_AcpmFreqHighValue_Type = DisplayString
_AcpmFreqHighValue_Object = MibTableColumn
acpmFreqHighValue = _AcpmFreqHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 8),
    _AcpmFreqHighValue_Type()
)
acpmFreqHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqHighValue.setStatus("current")
_AcpmFreqHighActions_Type = DisplayString
_AcpmFreqHighActions_Object = MibTableColumn
acpmFreqHighActions = _AcpmFreqHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 9),
    _AcpmFreqHighActions_Type()
)
acpmFreqHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqHighActions.setStatus("current")


class _AcpmFreqHighTrapNum_Type(Integer32):
    """Custom type acpmFreqHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(522, 1199),
    )


_AcpmFreqHighTrapNum_Type.__name__ = "Integer32"
_AcpmFreqHighTrapNum_Object = MibTableColumn
acpmFreqHighTrapNum = _AcpmFreqHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 10),
    _AcpmFreqHighTrapNum_Type()
)
acpmFreqHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqHighTrapNum.setStatus("current")
_AcpmFreqHighClass_Type = DisplayString
_AcpmFreqHighClass_Object = MibTableColumn
acpmFreqHighClass = _AcpmFreqHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 11),
    _AcpmFreqHighClass_Type()
)
acpmFreqHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqHighClass.setStatus("current")
_AcpmFreqNormalActions_Type = DisplayString
_AcpmFreqNormalActions_Object = MibTableColumn
acpmFreqNormalActions = _AcpmFreqNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 12),
    _AcpmFreqNormalActions_Type()
)
acpmFreqNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqNormalActions.setStatus("current")


class _AcpmFreqNormalTrapNum_Type(Integer32):
    """Custom type acpmFreqNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(522, 1199),
    )


_AcpmFreqNormalTrapNum_Type.__name__ = "Integer32"
_AcpmFreqNormalTrapNum_Object = MibTableColumn
acpmFreqNormalTrapNum = _AcpmFreqNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 13),
    _AcpmFreqNormalTrapNum_Type()
)
acpmFreqNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqNormalTrapNum.setStatus("current")
_AcpmFreqNormalClass_Type = DisplayString
_AcpmFreqNormalClass_Object = MibTableColumn
acpmFreqNormalClass = _AcpmFreqNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 14),
    _AcpmFreqNormalClass_Type()
)
acpmFreqNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqNormalClass.setStatus("current")
_AcpmFreqLowValue_Type = DisplayString
_AcpmFreqLowValue_Object = MibTableColumn
acpmFreqLowValue = _AcpmFreqLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 15),
    _AcpmFreqLowValue_Type()
)
acpmFreqLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqLowValue.setStatus("current")
_AcpmFreqLowActions_Type = DisplayString
_AcpmFreqLowActions_Object = MibTableColumn
acpmFreqLowActions = _AcpmFreqLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 16),
    _AcpmFreqLowActions_Type()
)
acpmFreqLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqLowActions.setStatus("current")


class _AcpmFreqLowTrapNum_Type(Integer32):
    """Custom type acpmFreqLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(522, 1199),
    )


_AcpmFreqLowTrapNum_Type.__name__ = "Integer32"
_AcpmFreqLowTrapNum_Object = MibTableColumn
acpmFreqLowTrapNum = _AcpmFreqLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 17),
    _AcpmFreqLowTrapNum_Type()
)
acpmFreqLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqLowTrapNum.setStatus("current")
_AcpmFreqLowClass_Type = DisplayString
_AcpmFreqLowClass_Object = MibTableColumn
acpmFreqLowClass = _AcpmFreqLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 18),
    _AcpmFreqLowClass_Type()
)
acpmFreqLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqLowClass.setStatus("current")
_AcpmFreqVLowValue_Type = DisplayString
_AcpmFreqVLowValue_Object = MibTableColumn
acpmFreqVLowValue = _AcpmFreqVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 19),
    _AcpmFreqVLowValue_Type()
)
acpmFreqVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVLowValue.setStatus("current")
_AcpmFreqVLowActions_Type = DisplayString
_AcpmFreqVLowActions_Object = MibTableColumn
acpmFreqVLowActions = _AcpmFreqVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 20),
    _AcpmFreqVLowActions_Type()
)
acpmFreqVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVLowActions.setStatus("current")


class _AcpmFreqVLowTrapNum_Type(Integer32):
    """Custom type acpmFreqVLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(522, 1199),
    )


_AcpmFreqVLowTrapNum_Type.__name__ = "Integer32"
_AcpmFreqVLowTrapNum_Object = MibTableColumn
acpmFreqVLowTrapNum = _AcpmFreqVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 21),
    _AcpmFreqVLowTrapNum_Type()
)
acpmFreqVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVLowTrapNum.setStatus("current")
_AcpmFreqVLowClass_Type = DisplayString
_AcpmFreqVLowClass_Object = MibTableColumn
acpmFreqVLowClass = _AcpmFreqVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 22),
    _AcpmFreqVLowClass_Type()
)
acpmFreqVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqVLowClass.setStatus("current")
_AcpmFreqSysrepEnable_Type = DisplayString
_AcpmFreqSysrepEnable_Object = MibTableColumn
acpmFreqSysrepEnable = _AcpmFreqSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 23),
    _AcpmFreqSysrepEnable_Type()
)
acpmFreqSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqSysrepEnable.setStatus("current")
_AcpmFreqSysrepThreshold_Type = DisplayString
_AcpmFreqSysrepThreshold_Object = MibTableColumn
acpmFreqSysrepThreshold = _AcpmFreqSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 24),
    _AcpmFreqSysrepThreshold_Type()
)
acpmFreqSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqSysrepThreshold.setStatus("current")
_AcpmFreqSysrepLimit_Type = Integer32
_AcpmFreqSysrepLimit_Object = MibTableColumn
acpmFreqSysrepLimit = _AcpmFreqSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 4, 1, 25),
    _AcpmFreqSysrepLimit_Type()
)
acpmFreqSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmFreqSysrepLimit.setStatus("current")
_AcpmTotalRealPowerTable_Object = MibTable
acpmTotalRealPowerTable = _AcpmTotalRealPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5)
)
if mibBuilder.loadTexts:
    acpmTotalRealPowerTable.setStatus("current")
_AcpmTRPEntry_Object = MibTableRow
acpmTRPEntry = _AcpmTRPEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1)
)
acpmTRPEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "acpmTRPIndex"),
)
if mibBuilder.loadTexts:
    acpmTRPEntry.setStatus("current")


class _AcpmTRPIndex_Type(Integer32):
    """Custom type acpmTRPIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmTRPIndex_Type.__name__ = "Integer32"
_AcpmTRPIndex_Object = MibTableColumn
acpmTRPIndex = _AcpmTRPIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 1),
    _AcpmTRPIndex_Type()
)
acpmTRPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmTRPIndex.setStatus("current")
_AcpmTRPEnable_Type = DisplayString
_AcpmTRPEnable_Object = MibTableColumn
acpmTRPEnable = _AcpmTRPEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 2),
    _AcpmTRPEnable_Type()
)
acpmTRPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPEnable.setStatus("current")
_AcpmTRPDeadband_Type = DisplayString
_AcpmTRPDeadband_Object = MibTableColumn
acpmTRPDeadband = _AcpmTRPDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 3),
    _AcpmTRPDeadband_Type()
)
acpmTRPDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPDeadband.setStatus("current")
_AcpmTRPVHighValue_Type = DisplayString
_AcpmTRPVHighValue_Object = MibTableColumn
acpmTRPVHighValue = _AcpmTRPVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 4),
    _AcpmTRPVHighValue_Type()
)
acpmTRPVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVHighValue.setStatus("current")
_AcpmTRPVHighActions_Type = DisplayString
_AcpmTRPVHighActions_Object = MibTableColumn
acpmTRPVHighActions = _AcpmTRPVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 5),
    _AcpmTRPVHighActions_Type()
)
acpmTRPVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVHighActions.setStatus("current")


class _AcpmTRPVHighTrapNum_Type(Integer32):
    """Custom type acpmTRPVHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(523, 1199),
    )


_AcpmTRPVHighTrapNum_Type.__name__ = "Integer32"
_AcpmTRPVHighTrapNum_Object = MibTableColumn
acpmTRPVHighTrapNum = _AcpmTRPVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 6),
    _AcpmTRPVHighTrapNum_Type()
)
acpmTRPVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVHighTrapNum.setStatus("current")
_AcpmTRPVHighClass_Type = DisplayString
_AcpmTRPVHighClass_Object = MibTableColumn
acpmTRPVHighClass = _AcpmTRPVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 7),
    _AcpmTRPVHighClass_Type()
)
acpmTRPVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVHighClass.setStatus("current")
_AcpmTRPHighValue_Type = DisplayString
_AcpmTRPHighValue_Object = MibTableColumn
acpmTRPHighValue = _AcpmTRPHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 8),
    _AcpmTRPHighValue_Type()
)
acpmTRPHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPHighValue.setStatus("current")
_AcpmTRPHighActions_Type = DisplayString
_AcpmTRPHighActions_Object = MibTableColumn
acpmTRPHighActions = _AcpmTRPHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 9),
    _AcpmTRPHighActions_Type()
)
acpmTRPHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPHighActions.setStatus("current")


class _AcpmTRPHighTrapNum_Type(Integer32):
    """Custom type acpmTRPHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(523, 1199),
    )


_AcpmTRPHighTrapNum_Type.__name__ = "Integer32"
_AcpmTRPHighTrapNum_Object = MibTableColumn
acpmTRPHighTrapNum = _AcpmTRPHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 10),
    _AcpmTRPHighTrapNum_Type()
)
acpmTRPHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPHighTrapNum.setStatus("current")
_AcpmTRPHighClass_Type = DisplayString
_AcpmTRPHighClass_Object = MibTableColumn
acpmTRPHighClass = _AcpmTRPHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 11),
    _AcpmTRPHighClass_Type()
)
acpmTRPHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPHighClass.setStatus("current")
_AcpmTRPNormalActions_Type = DisplayString
_AcpmTRPNormalActions_Object = MibTableColumn
acpmTRPNormalActions = _AcpmTRPNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 12),
    _AcpmTRPNormalActions_Type()
)
acpmTRPNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPNormalActions.setStatus("current")


class _AcpmTRPNormalTrapNum_Type(Integer32):
    """Custom type acpmTRPNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(523, 1199),
    )


_AcpmTRPNormalTrapNum_Type.__name__ = "Integer32"
_AcpmTRPNormalTrapNum_Object = MibTableColumn
acpmTRPNormalTrapNum = _AcpmTRPNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 13),
    _AcpmTRPNormalTrapNum_Type()
)
acpmTRPNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPNormalTrapNum.setStatus("current")
_AcpmTRPNormalClass_Type = DisplayString
_AcpmTRPNormalClass_Object = MibTableColumn
acpmTRPNormalClass = _AcpmTRPNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 14),
    _AcpmTRPNormalClass_Type()
)
acpmTRPNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPNormalClass.setStatus("current")
_AcpmTRPLowValue_Type = DisplayString
_AcpmTRPLowValue_Object = MibTableColumn
acpmTRPLowValue = _AcpmTRPLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 15),
    _AcpmTRPLowValue_Type()
)
acpmTRPLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPLowValue.setStatus("current")
_AcpmTRPLowActions_Type = DisplayString
_AcpmTRPLowActions_Object = MibTableColumn
acpmTRPLowActions = _AcpmTRPLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 16),
    _AcpmTRPLowActions_Type()
)
acpmTRPLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPLowActions.setStatus("current")


class _AcpmTRPLowTrapNum_Type(Integer32):
    """Custom type acpmTRPLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(523, 1199),
    )


_AcpmTRPLowTrapNum_Type.__name__ = "Integer32"
_AcpmTRPLowTrapNum_Object = MibTableColumn
acpmTRPLowTrapNum = _AcpmTRPLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 17),
    _AcpmTRPLowTrapNum_Type()
)
acpmTRPLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPLowTrapNum.setStatus("current")
_AcpmTRPLowClass_Type = DisplayString
_AcpmTRPLowClass_Object = MibTableColumn
acpmTRPLowClass = _AcpmTRPLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 18),
    _AcpmTRPLowClass_Type()
)
acpmTRPLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPLowClass.setStatus("current")
_AcpmTRPVLowValue_Type = DisplayString
_AcpmTRPVLowValue_Object = MibTableColumn
acpmTRPVLowValue = _AcpmTRPVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 19),
    _AcpmTRPVLowValue_Type()
)
acpmTRPVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVLowValue.setStatus("current")
_AcpmTRPVLowActions_Type = DisplayString
_AcpmTRPVLowActions_Object = MibTableColumn
acpmTRPVLowActions = _AcpmTRPVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 20),
    _AcpmTRPVLowActions_Type()
)
acpmTRPVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVLowActions.setStatus("current")


class _AcpmTRPVLowTrapNum_Type(Integer32):
    """Custom type acpmTRPVLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(523, 1199),
    )


_AcpmTRPVLowTrapNum_Type.__name__ = "Integer32"
_AcpmTRPVLowTrapNum_Object = MibTableColumn
acpmTRPVLowTrapNum = _AcpmTRPVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 21),
    _AcpmTRPVLowTrapNum_Type()
)
acpmTRPVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVLowTrapNum.setStatus("current")
_AcpmTRPVLowClass_Type = DisplayString
_AcpmTRPVLowClass_Object = MibTableColumn
acpmTRPVLowClass = _AcpmTRPVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 22),
    _AcpmTRPVLowClass_Type()
)
acpmTRPVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPVLowClass.setStatus("current")
_AcpmTRPSysrepEnable_Type = DisplayString
_AcpmTRPSysrepEnable_Object = MibTableColumn
acpmTRPSysrepEnable = _AcpmTRPSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 23),
    _AcpmTRPSysrepEnable_Type()
)
acpmTRPSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPSysrepEnable.setStatus("current")
_AcpmTRPSysrepThreshold_Type = DisplayString
_AcpmTRPSysrepThreshold_Object = MibTableColumn
acpmTRPSysrepThreshold = _AcpmTRPSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 24),
    _AcpmTRPSysrepThreshold_Type()
)
acpmTRPSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPSysrepThreshold.setStatus("current")
_AcpmTRPSysrepLimit_Type = Integer32
_AcpmTRPSysrepLimit_Object = MibTableColumn
acpmTRPSysrepLimit = _AcpmTRPSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 5, 1, 25),
    _AcpmTRPSysrepLimit_Type()
)
acpmTRPSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTRPSysrepLimit.setStatus("current")
_AcpmDisconnectTable_Object = MibTable
acpmDisconnectTable = _AcpmDisconnectTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 6)
)
if mibBuilder.loadTexts:
    acpmDisconnectTable.setStatus("current")
_AcpmDisconnectEntry_Object = MibTableRow
acpmDisconnectEntry = _AcpmDisconnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 6, 1)
)
acpmDisconnectEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "acpmDisconnectIndex"),
)
if mibBuilder.loadTexts:
    acpmDisconnectEntry.setStatus("current")


class _AcpmDisconnectIndex_Type(Integer32):
    """Custom type acpmDisconnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmDisconnectIndex_Type.__name__ = "Integer32"
_AcpmDisconnectIndex_Object = MibTableColumn
acpmDisconnectIndex = _AcpmDisconnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 6, 1, 1),
    _AcpmDisconnectIndex_Type()
)
acpmDisconnectIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmDisconnectIndex.setStatus("current")
_AcpmDisconnectEnable_Type = DisplayString
_AcpmDisconnectEnable_Object = MibTableColumn
acpmDisconnectEnable = _AcpmDisconnectEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 6, 1, 2),
    _AcpmDisconnectEnable_Type()
)
acpmDisconnectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectEnable.setStatus("current")
_AcpmDisconnectActions_Type = DisplayString
_AcpmDisconnectActions_Object = MibTableColumn
acpmDisconnectActions = _AcpmDisconnectActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 6, 1, 3),
    _AcpmDisconnectActions_Type()
)
acpmDisconnectActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectActions.setStatus("current")


class _AcpmDisconnectTrapNum_Type(Integer32):
    """Custom type acpmDisconnectTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(524, 1199),
    )


_AcpmDisconnectTrapNum_Type.__name__ = "Integer32"
_AcpmDisconnectTrapNum_Object = MibTableColumn
acpmDisconnectTrapNum = _AcpmDisconnectTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 6, 1, 4),
    _AcpmDisconnectTrapNum_Type()
)
acpmDisconnectTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectTrapNum.setStatus("current")
_AcpmDisconnectClass_Type = DisplayString
_AcpmDisconnectClass_Object = MibTableColumn
acpmDisconnectClass = _AcpmDisconnectClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 6, 1, 5),
    _AcpmDisconnectClass_Type()
)
acpmDisconnectClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectClass.setStatus("current")
_AcpmDisconnectNormalActions_Type = DisplayString
_AcpmDisconnectNormalActions_Object = MibTableColumn
acpmDisconnectNormalActions = _AcpmDisconnectNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 6, 1, 6),
    _AcpmDisconnectNormalActions_Type()
)
acpmDisconnectNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectNormalActions.setStatus("current")


class _AcpmDisconnectNormalTrapNum_Type(Integer32):
    """Custom type acpmDisconnectNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(524, 1199),
    )


_AcpmDisconnectNormalTrapNum_Type.__name__ = "Integer32"
_AcpmDisconnectNormalTrapNum_Object = MibTableColumn
acpmDisconnectNormalTrapNum = _AcpmDisconnectNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 6, 1, 7),
    _AcpmDisconnectNormalTrapNum_Type()
)
acpmDisconnectNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectNormalTrapNum.setStatus("current")
_AcpmDisconnectNormalClass_Type = DisplayString
_AcpmDisconnectNormalClass_Object = MibTableColumn
acpmDisconnectNormalClass = _AcpmDisconnectNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 6, 1, 8),
    _AcpmDisconnectNormalClass_Type()
)
acpmDisconnectNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmDisconnectNormalClass.setStatus("current")
_AcpmTotalPowerFactorTable_Object = MibTable
acpmTotalPowerFactorTable = _AcpmTotalPowerFactorTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7)
)
if mibBuilder.loadTexts:
    acpmTotalPowerFactorTable.setStatus("current")
_AcpmTPFEntry_Object = MibTableRow
acpmTPFEntry = _AcpmTPFEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1)
)
acpmTPFEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "acpmTPFIndex"),
)
if mibBuilder.loadTexts:
    acpmTPFEntry.setStatus("current")


class _AcpmTPFIndex_Type(Integer32):
    """Custom type acpmTPFIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_AcpmTPFIndex_Type.__name__ = "Integer32"
_AcpmTPFIndex_Object = MibTableColumn
acpmTPFIndex = _AcpmTPFIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 1),
    _AcpmTPFIndex_Type()
)
acpmTPFIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acpmTPFIndex.setStatus("current")
_AcpmTPFEnable_Type = DisplayString
_AcpmTPFEnable_Object = MibTableColumn
acpmTPFEnable = _AcpmTPFEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 2),
    _AcpmTPFEnable_Type()
)
acpmTPFEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFEnable.setStatus("current")
_AcpmTPFDeadband_Type = DisplayString
_AcpmTPFDeadband_Object = MibTableColumn
acpmTPFDeadband = _AcpmTPFDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 3),
    _AcpmTPFDeadband_Type()
)
acpmTPFDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFDeadband.setStatus("current")
_AcpmTPFNormalActions_Type = DisplayString
_AcpmTPFNormalActions_Object = MibTableColumn
acpmTPFNormalActions = _AcpmTPFNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 4),
    _AcpmTPFNormalActions_Type()
)
acpmTPFNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFNormalActions.setStatus("current")
_AcpmTPFNormalTrapNum_Type = Integer32
_AcpmTPFNormalTrapNum_Object = MibTableColumn
acpmTPFNormalTrapNum = _AcpmTPFNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 5),
    _AcpmTPFNormalTrapNum_Type()
)
acpmTPFNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFNormalTrapNum.setStatus("current")
_AcpmTPFNormalClass_Type = DisplayString
_AcpmTPFNormalClass_Object = MibTableColumn
acpmTPFNormalClass = _AcpmTPFNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 6),
    _AcpmTPFNormalClass_Type()
)
acpmTPFNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFNormalClass.setStatus("current")
_AcpmTPFLowValue_Type = DisplayString
_AcpmTPFLowValue_Object = MibTableColumn
acpmTPFLowValue = _AcpmTPFLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 7),
    _AcpmTPFLowValue_Type()
)
acpmTPFLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFLowValue.setStatus("current")
_AcpmTPFLowActions_Type = DisplayString
_AcpmTPFLowActions_Object = MibTableColumn
acpmTPFLowActions = _AcpmTPFLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 8),
    _AcpmTPFLowActions_Type()
)
acpmTPFLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFLowActions.setStatus("current")
_AcpmTPFLowTrapNum_Type = Integer32
_AcpmTPFLowTrapNum_Object = MibTableColumn
acpmTPFLowTrapNum = _AcpmTPFLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 9),
    _AcpmTPFLowTrapNum_Type()
)
acpmTPFLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFLowTrapNum.setStatus("current")
_AcpmTPFLowClass_Type = DisplayString
_AcpmTPFLowClass_Object = MibTableColumn
acpmTPFLowClass = _AcpmTPFLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 10),
    _AcpmTPFLowClass_Type()
)
acpmTPFLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFLowClass.setStatus("current")
_AcpmTPFVLowValue_Type = DisplayString
_AcpmTPFVLowValue_Object = MibTableColumn
acpmTPFVLowValue = _AcpmTPFVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 11),
    _AcpmTPFVLowValue_Type()
)
acpmTPFVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFVLowValue.setStatus("current")
_AcpmTPFVLowActions_Type = DisplayString
_AcpmTPFVLowActions_Object = MibTableColumn
acpmTPFVLowActions = _AcpmTPFVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 12),
    _AcpmTPFVLowActions_Type()
)
acpmTPFVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFVLowActions.setStatus("current")
_AcpmTPFVLowTrapNum_Type = Integer32
_AcpmTPFVLowTrapNum_Object = MibTableColumn
acpmTPFVLowTrapNum = _AcpmTPFVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 13),
    _AcpmTPFVLowTrapNum_Type()
)
acpmTPFVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFVLowTrapNum.setStatus("current")
_AcpmTPFVLowClass_Type = DisplayString
_AcpmTPFVLowClass_Object = MibTableColumn
acpmTPFVLowClass = _AcpmTPFVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 14),
    _AcpmTPFVLowClass_Type()
)
acpmTPFVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFVLowClass.setStatus("current")
_AcpmTPFSysrepEnable_Type = DisplayString
_AcpmTPFSysrepEnable_Object = MibTableColumn
acpmTPFSysrepEnable = _AcpmTPFSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 15),
    _AcpmTPFSysrepEnable_Type()
)
acpmTPFSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFSysrepEnable.setStatus("current")
_AcpmTPFSysrepThreshold_Type = DisplayString
_AcpmTPFSysrepThreshold_Object = MibTableColumn
acpmTPFSysrepThreshold = _AcpmTPFSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 16),
    _AcpmTPFSysrepThreshold_Type()
)
acpmTPFSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFSysrepThreshold.setStatus("current")
_AcpmTPFSysrepLimit_Type = Integer32
_AcpmTPFSysrepLimit_Object = MibTableColumn
acpmTPFSysrepLimit = _AcpmTPFSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 12, 7, 1, 17),
    _AcpmTPFSysrepLimit_Type()
)
acpmTPFSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acpmTPFSysrepLimit.setStatus("current")
_BatteryMonitor_ObjectIdentity = ObjectIdentity
batteryMonitor = _BatteryMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14)
)
_BatteryMonitorGeneralTable_Object = MibTable
batteryMonitorGeneralTable = _BatteryMonitorGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 1)
)
if mibBuilder.loadTexts:
    batteryMonitorGeneralTable.setStatus("current")
_BmGenEntry_Object = MibTableRow
bmGenEntry = _BmGenEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 1, 1)
)
bmGenEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmGenIndex"),
)
if mibBuilder.loadTexts:
    bmGenEntry.setStatus("current")


class _BmGenIndex_Type(Integer32):
    """Custom type bmGenIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmGenIndex_Type.__name__ = "Integer32"
_BmGenIndex_Object = MibTableColumn
bmGenIndex = _BmGenIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 1, 1, 1),
    _BmGenIndex_Type()
)
bmGenIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmGenIndex.setStatus("current")
_BmGenEnable_Type = DisplayString
_BmGenEnable_Object = MibTableColumn
bmGenEnable = _BmGenEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 1, 1, 2),
    _BmGenEnable_Type()
)
bmGenEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmGenEnable.setStatus("current")
_BmGenName_Type = DisplayString
_BmGenName_Object = MibTableColumn
bmGenName = _BmGenName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 1, 1, 3),
    _BmGenName_Type()
)
bmGenName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmGenName.setStatus("current")


class _BmGenBatteryQuantity_Type(Integer32):
    """Custom type bmGenBatteryQuantity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_BmGenBatteryQuantity_Type.__name__ = "Integer32"
_BmGenBatteryQuantity_Object = MibTableColumn
bmGenBatteryQuantity = _BmGenBatteryQuantity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 1, 1, 4),
    _BmGenBatteryQuantity_Type()
)
bmGenBatteryQuantity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmGenBatteryQuantity.setStatus("current")


class _BmGenBatteryCapacity_Type(Integer32):
    """Custom type bmGenBatteryCapacity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 500),
    )


_BmGenBatteryCapacity_Type.__name__ = "Integer32"
_BmGenBatteryCapacity_Object = MibTableColumn
bmGenBatteryCapacity = _BmGenBatteryCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 1, 1, 5),
    _BmGenBatteryCapacity_Type()
)
bmGenBatteryCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmGenBatteryCapacity.setStatus("current")
_BmGenBatteryNominalVoltage_Type = DisplayString
_BmGenBatteryNominalVoltage_Object = MibTableColumn
bmGenBatteryNominalVoltage = _BmGenBatteryNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 1, 1, 6),
    _BmGenBatteryNominalVoltage_Type()
)
bmGenBatteryNominalVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmGenBatteryNominalVoltage.setStatus("current")


class _BmGenSysrepPackage_Type(Integer32):
    """Custom type bmGenSysrepPackage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_BmGenSysrepPackage_Type.__name__ = "Integer32"
_BmGenSysrepPackage_Object = MibTableColumn
bmGenSysrepPackage = _BmGenSysrepPackage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 1, 1, 7),
    _BmGenSysrepPackage_Type()
)
bmGenSysrepPackage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmGenSysrepPackage.setStatus("current")
_BmGenSysrepType_Type = DisplayString
_BmGenSysrepType_Object = MibTableColumn
bmGenSysrepType = _BmGenSysrepType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 1, 1, 8),
    _BmGenSysrepType_Type()
)
bmGenSysrepType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmGenSysrepType.setStatus("current")
_BatteryMonitorDeviceTable_Object = MibTable
batteryMonitorDeviceTable = _BatteryMonitorDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 2)
)
if mibBuilder.loadTexts:
    batteryMonitorDeviceTable.setStatus("current")
_BmDeviceEntry_Object = MibTableRow
bmDeviceEntry = _BmDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 2, 1)
)
bmDeviceEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmDeviceIndex"),
)
if mibBuilder.loadTexts:
    bmDeviceEntry.setStatus("current")


class _BmDeviceIndex_Type(Integer32):
    """Custom type bmDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmDeviceIndex_Type.__name__ = "Integer32"
_BmDeviceIndex_Object = MibTableColumn
bmDeviceIndex = _BmDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 2, 1, 1),
    _BmDeviceIndex_Type()
)
bmDeviceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmDeviceIndex.setStatus("current")
_BmDeviceType_Type = DisplayString
_BmDeviceType_Object = MibTableColumn
bmDeviceType = _BmDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 2, 1, 2),
    _BmDeviceType_Type()
)
bmDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDeviceType.setStatus("current")


class _BmDeviceES_Type(Integer32):
    """Custom type bmDeviceES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_BmDeviceES_Type.__name__ = "Integer32"
_BmDeviceES_Object = MibTableColumn
bmDeviceES = _BmDeviceES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 2, 1, 3),
    _BmDeviceES_Type()
)
bmDeviceES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDeviceES.setStatus("current")
_BmDeviceIP_Type = IpAddress
_BmDeviceIP_Object = MibTableColumn
bmDeviceIP = _BmDeviceIP_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 2, 1, 4),
    _BmDeviceIP_Type()
)
bmDeviceIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDeviceIP.setStatus("current")
_BmDeviceReadcom_Type = DisplayString
_BmDeviceReadcom_Object = MibTableColumn
bmDeviceReadcom = _BmDeviceReadcom_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 2, 1, 5),
    _BmDeviceReadcom_Type()
)
bmDeviceReadcom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDeviceReadcom.setStatus("current")


class _BmDeviceInputString_Type(Integer32):
    """Custom type bmDeviceInputString based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BmDeviceInputString_Type.__name__ = "Integer32"
_BmDeviceInputString_Object = MibTableColumn
bmDeviceInputString = _BmDeviceInputString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 2, 1, 6),
    _BmDeviceInputString_Type()
)
bmDeviceInputString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDeviceInputString.setStatus("current")


class _BmDeviceCTSize_Type(Integer32):
    """Custom type bmDeviceCTSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 999),
    )


_BmDeviceCTSize_Type.__name__ = "Integer32"
_BmDeviceCTSize_Object = MibTableColumn
bmDeviceCTSize = _BmDeviceCTSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 2, 1, 7),
    _BmDeviceCTSize_Type()
)
bmDeviceCTSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDeviceCTSize.setStatus("current")
_BatteryMonitorTempTable_Object = MibTable
batteryMonitorTempTable = _BatteryMonitorTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3)
)
if mibBuilder.loadTexts:
    batteryMonitorTempTable.setStatus("current")
_BmTempEntry_Object = MibTableRow
bmTempEntry = _BmTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1)
)
bmTempEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmTempIndex"),
)
if mibBuilder.loadTexts:
    bmTempEntry.setStatus("current")


class _BmTempIndex_Type(Integer32):
    """Custom type bmTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmTempIndex_Type.__name__ = "Integer32"
_BmTempIndex_Object = MibTableColumn
bmTempIndex = _BmTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 1),
    _BmTempIndex_Type()
)
bmTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmTempIndex.setStatus("current")
_BmTempEnable_Type = DisplayString
_BmTempEnable_Object = MibTableColumn
bmTempEnable = _BmTempEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 2),
    _BmTempEnable_Type()
)
bmTempEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempEnable.setStatus("current")
_BmTempDeadband_Type = DisplayString
_BmTempDeadband_Object = MibTableColumn
bmTempDeadband = _BmTempDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 3),
    _BmTempDeadband_Type()
)
bmTempDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempDeadband.setStatus("current")
_BmTempScale_Type = DisplayString
_BmTempScale_Object = MibTableColumn
bmTempScale = _BmTempScale_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 4),
    _BmTempScale_Type()
)
bmTempScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempScale.setStatus("current")
_BmTempHighValue_Type = DisplayString
_BmTempHighValue_Object = MibTableColumn
bmTempHighValue = _BmTempHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 5),
    _BmTempHighValue_Type()
)
bmTempHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempHighValue.setStatus("current")
_BmTempHighActions_Type = DisplayString
_BmTempHighActions_Object = MibTableColumn
bmTempHighActions = _BmTempHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 6),
    _BmTempHighActions_Type()
)
bmTempHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempHighActions.setStatus("current")


class _BmTempHighTrapNum_Type(Integer32):
    """Custom type bmTempHighTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(530, 1199),
    )


_BmTempHighTrapNum_Type.__name__ = "Integer32"
_BmTempHighTrapNum_Object = MibTableColumn
bmTempHighTrapNum = _BmTempHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 7),
    _BmTempHighTrapNum_Type()
)
bmTempHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempHighTrapNum.setStatus("current")
_BmTempHighClass_Type = DisplayString
_BmTempHighClass_Object = MibTableColumn
bmTempHighClass = _BmTempHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 8),
    _BmTempHighClass_Type()
)
bmTempHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempHighClass.setStatus("current")
_BmTempNormalActions_Type = DisplayString
_BmTempNormalActions_Object = MibTableColumn
bmTempNormalActions = _BmTempNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 9),
    _BmTempNormalActions_Type()
)
bmTempNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempNormalActions.setStatus("current")


class _BmTempNormalTrapNum_Type(Integer32):
    """Custom type bmTempNormalTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(530, 1199),
    )


_BmTempNormalTrapNum_Type.__name__ = "Integer32"
_BmTempNormalTrapNum_Object = MibTableColumn
bmTempNormalTrapNum = _BmTempNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 10),
    _BmTempNormalTrapNum_Type()
)
bmTempNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempNormalTrapNum.setStatus("current")
_BmTempNormalClass_Type = DisplayString
_BmTempNormalClass_Object = MibTableColumn
bmTempNormalClass = _BmTempNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 11),
    _BmTempNormalClass_Type()
)
bmTempNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempNormalClass.setStatus("current")
_BmTempLowValue_Type = DisplayString
_BmTempLowValue_Object = MibTableColumn
bmTempLowValue = _BmTempLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 12),
    _BmTempLowValue_Type()
)
bmTempLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempLowValue.setStatus("current")
_BmTempLowActions_Type = DisplayString
_BmTempLowActions_Object = MibTableColumn
bmTempLowActions = _BmTempLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 13),
    _BmTempLowActions_Type()
)
bmTempLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempLowActions.setStatus("current")


class _BmTempLowTrapNum_Type(Integer32):
    """Custom type bmTempLowTrapNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(530, 1199),
    )


_BmTempLowTrapNum_Type.__name__ = "Integer32"
_BmTempLowTrapNum_Object = MibTableColumn
bmTempLowTrapNum = _BmTempLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 14),
    _BmTempLowTrapNum_Type()
)
bmTempLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempLowTrapNum.setStatus("current")
_BmTempLowClass_Type = DisplayString
_BmTempLowClass_Object = MibTableColumn
bmTempLowClass = _BmTempLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 15),
    _BmTempLowClass_Type()
)
bmTempLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempLowClass.setStatus("current")
_BmTempSysrepEnable_Type = DisplayString
_BmTempSysrepEnable_Object = MibTableColumn
bmTempSysrepEnable = _BmTempSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 16),
    _BmTempSysrepEnable_Type()
)
bmTempSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempSysrepEnable.setStatus("current")
_BmTempSysrepThreshold_Type = DisplayString
_BmTempSysrepThreshold_Object = MibTableColumn
bmTempSysrepThreshold = _BmTempSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 17),
    _BmTempSysrepThreshold_Type()
)
bmTempSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempSysrepThreshold.setStatus("current")
_BmTempSysrepLimit_Type = Integer32
_BmTempSysrepLimit_Object = MibTableColumn
bmTempSysrepLimit = _BmTempSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 3, 1, 18),
    _BmTempSysrepLimit_Type()
)
bmTempSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmTempSysrepLimit.setStatus("current")
_BatteryMonitorDiffTempTable_Object = MibTable
batteryMonitorDiffTempTable = _BatteryMonitorDiffTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4)
)
if mibBuilder.loadTexts:
    batteryMonitorDiffTempTable.setStatus("current")
_BmDiffTempEntry_Object = MibTableRow
bmDiffTempEntry = _BmDiffTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1)
)
bmDiffTempEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmDiffTempIndex"),
)
if mibBuilder.loadTexts:
    bmDiffTempEntry.setStatus("current")


class _BmDiffTempIndex_Type(Integer32):
    """Custom type bmDiffTempIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmDiffTempIndex_Type.__name__ = "Integer32"
_BmDiffTempIndex_Object = MibTableColumn
bmDiffTempIndex = _BmDiffTempIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 1),
    _BmDiffTempIndex_Type()
)
bmDiffTempIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmDiffTempIndex.setStatus("current")
_BmDiffTempEnable_Type = DisplayString
_BmDiffTempEnable_Object = MibTableColumn
bmDiffTempEnable = _BmDiffTempEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 2),
    _BmDiffTempEnable_Type()
)
bmDiffTempEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempEnable.setStatus("current")
_BmDiffTempDeadband_Type = Integer32
_BmDiffTempDeadband_Object = MibTableColumn
bmDiffTempDeadband = _BmDiffTempDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 3),
    _BmDiffTempDeadband_Type()
)
bmDiffTempDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempDeadband.setStatus("current")
_BmDiffTempVHighValue_Type = Integer32
_BmDiffTempVHighValue_Object = MibTableColumn
bmDiffTempVHighValue = _BmDiffTempVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 4),
    _BmDiffTempVHighValue_Type()
)
bmDiffTempVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempVHighValue.setStatus("current")
_BmDiffTempVHighActions_Type = DisplayString
_BmDiffTempVHighActions_Object = MibTableColumn
bmDiffTempVHighActions = _BmDiffTempVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 5),
    _BmDiffTempVHighActions_Type()
)
bmDiffTempVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempVHighActions.setStatus("current")
_BmDiffTempVHighTrapNum_Type = Integer32
_BmDiffTempVHighTrapNum_Object = MibTableColumn
bmDiffTempVHighTrapNum = _BmDiffTempVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 6),
    _BmDiffTempVHighTrapNum_Type()
)
bmDiffTempVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempVHighTrapNum.setStatus("current")
_BmDiffTempVHighClass_Type = DisplayString
_BmDiffTempVHighClass_Object = MibTableColumn
bmDiffTempVHighClass = _BmDiffTempVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 7),
    _BmDiffTempVHighClass_Type()
)
bmDiffTempVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempVHighClass.setStatus("current")
_BmDiffTempHighValue_Type = Integer32
_BmDiffTempHighValue_Object = MibTableColumn
bmDiffTempHighValue = _BmDiffTempHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 8),
    _BmDiffTempHighValue_Type()
)
bmDiffTempHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempHighValue.setStatus("current")
_BmDiffTempHighActions_Type = DisplayString
_BmDiffTempHighActions_Object = MibTableColumn
bmDiffTempHighActions = _BmDiffTempHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 9),
    _BmDiffTempHighActions_Type()
)
bmDiffTempHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempHighActions.setStatus("current")
_BmDiffTempHighTrapNum_Type = Integer32
_BmDiffTempHighTrapNum_Object = MibTableColumn
bmDiffTempHighTrapNum = _BmDiffTempHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 10),
    _BmDiffTempHighTrapNum_Type()
)
bmDiffTempHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempHighTrapNum.setStatus("current")
_BmDiffTempHighClass_Type = DisplayString
_BmDiffTempHighClass_Object = MibTableColumn
bmDiffTempHighClass = _BmDiffTempHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 11),
    _BmDiffTempHighClass_Type()
)
bmDiffTempHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempHighClass.setStatus("current")
_BmDiffTempNormalActions_Type = DisplayString
_BmDiffTempNormalActions_Object = MibTableColumn
bmDiffTempNormalActions = _BmDiffTempNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 12),
    _BmDiffTempNormalActions_Type()
)
bmDiffTempNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempNormalActions.setStatus("current")
_BmDiffTempNormalTrapNum_Type = Integer32
_BmDiffTempNormalTrapNum_Object = MibTableColumn
bmDiffTempNormalTrapNum = _BmDiffTempNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 13),
    _BmDiffTempNormalTrapNum_Type()
)
bmDiffTempNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempNormalTrapNum.setStatus("current")
_BmDiffTempNormalClass_Type = DisplayString
_BmDiffTempNormalClass_Object = MibTableColumn
bmDiffTempNormalClass = _BmDiffTempNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 14),
    _BmDiffTempNormalClass_Type()
)
bmDiffTempNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempNormalClass.setStatus("current")
_BmDiffTempSysrepEnable_Type = DisplayString
_BmDiffTempSysrepEnable_Object = MibTableColumn
bmDiffTempSysrepEnable = _BmDiffTempSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 15),
    _BmDiffTempSysrepEnable_Type()
)
bmDiffTempSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempSysrepEnable.setStatus("current")
_BmDiffTempSysrepThreshold_Type = Integer32
_BmDiffTempSysrepThreshold_Object = MibTableColumn
bmDiffTempSysrepThreshold = _BmDiffTempSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 16),
    _BmDiffTempSysrepThreshold_Type()
)
bmDiffTempSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempSysrepThreshold.setStatus("current")
_BmDiffTempSysrepLimit_Type = Integer32
_BmDiffTempSysrepLimit_Object = MibTableColumn
bmDiffTempSysrepLimit = _BmDiffTempSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 4, 1, 17),
    _BmDiffTempSysrepLimit_Type()
)
bmDiffTempSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffTempSysrepLimit.setStatus("current")
_BatteryMonitorVoltageTable_Object = MibTable
batteryMonitorVoltageTable = _BatteryMonitorVoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5)
)
if mibBuilder.loadTexts:
    batteryMonitorVoltageTable.setStatus("current")
_BmVoltageEntry_Object = MibTableRow
bmVoltageEntry = _BmVoltageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1)
)
bmVoltageEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmVoltageIndex"),
)
if mibBuilder.loadTexts:
    bmVoltageEntry.setStatus("current")


class _BmVoltageIndex_Type(Integer32):
    """Custom type bmVoltageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmVoltageIndex_Type.__name__ = "Integer32"
_BmVoltageIndex_Object = MibTableColumn
bmVoltageIndex = _BmVoltageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 1),
    _BmVoltageIndex_Type()
)
bmVoltageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmVoltageIndex.setStatus("current")
_BmVoltageEnable_Type = DisplayString
_BmVoltageEnable_Object = MibTableColumn
bmVoltageEnable = _BmVoltageEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 2),
    _BmVoltageEnable_Type()
)
bmVoltageEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageEnable.setStatus("current")
_BmVoltageDeadband_Type = DisplayString
_BmVoltageDeadband_Object = MibTableColumn
bmVoltageDeadband = _BmVoltageDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 3),
    _BmVoltageDeadband_Type()
)
bmVoltageDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageDeadband.setStatus("current")
_BmVoltageVHighValue_Type = DisplayString
_BmVoltageVHighValue_Object = MibTableColumn
bmVoltageVHighValue = _BmVoltageVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 4),
    _BmVoltageVHighValue_Type()
)
bmVoltageVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageVHighValue.setStatus("current")
_BmVoltageVHighActions_Type = DisplayString
_BmVoltageVHighActions_Object = MibTableColumn
bmVoltageVHighActions = _BmVoltageVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 5),
    _BmVoltageVHighActions_Type()
)
bmVoltageVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageVHighActions.setStatus("current")
_BmVoltageVHighTrapNum_Type = Integer32
_BmVoltageVHighTrapNum_Object = MibTableColumn
bmVoltageVHighTrapNum = _BmVoltageVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 6),
    _BmVoltageVHighTrapNum_Type()
)
bmVoltageVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageVHighTrapNum.setStatus("current")
_BmVoltageVHighClass_Type = DisplayString
_BmVoltageVHighClass_Object = MibTableColumn
bmVoltageVHighClass = _BmVoltageVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 7),
    _BmVoltageVHighClass_Type()
)
bmVoltageVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageVHighClass.setStatus("current")
_BmVoltageHighValue_Type = DisplayString
_BmVoltageHighValue_Object = MibTableColumn
bmVoltageHighValue = _BmVoltageHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 8),
    _BmVoltageHighValue_Type()
)
bmVoltageHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageHighValue.setStatus("current")
_BmVoltageHighActions_Type = DisplayString
_BmVoltageHighActions_Object = MibTableColumn
bmVoltageHighActions = _BmVoltageHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 9),
    _BmVoltageHighActions_Type()
)
bmVoltageHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageHighActions.setStatus("current")
_BmVoltageHighTrapNum_Type = Integer32
_BmVoltageHighTrapNum_Object = MibTableColumn
bmVoltageHighTrapNum = _BmVoltageHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 10),
    _BmVoltageHighTrapNum_Type()
)
bmVoltageHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageHighTrapNum.setStatus("current")
_BmVoltageHighClass_Type = DisplayString
_BmVoltageHighClass_Object = MibTableColumn
bmVoltageHighClass = _BmVoltageHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 11),
    _BmVoltageHighClass_Type()
)
bmVoltageHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageHighClass.setStatus("current")
_BmVoltageNormalActions_Type = DisplayString
_BmVoltageNormalActions_Object = MibTableColumn
bmVoltageNormalActions = _BmVoltageNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 12),
    _BmVoltageNormalActions_Type()
)
bmVoltageNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageNormalActions.setStatus("current")
_BmVoltageNormalTrapNum_Type = Integer32
_BmVoltageNormalTrapNum_Object = MibTableColumn
bmVoltageNormalTrapNum = _BmVoltageNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 13),
    _BmVoltageNormalTrapNum_Type()
)
bmVoltageNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageNormalTrapNum.setStatus("current")
_BmVoltageNormalClass_Type = DisplayString
_BmVoltageNormalClass_Object = MibTableColumn
bmVoltageNormalClass = _BmVoltageNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 14),
    _BmVoltageNormalClass_Type()
)
bmVoltageNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageNormalClass.setStatus("current")
_BmVoltageLowValue_Type = DisplayString
_BmVoltageLowValue_Object = MibTableColumn
bmVoltageLowValue = _BmVoltageLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 15),
    _BmVoltageLowValue_Type()
)
bmVoltageLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageLowValue.setStatus("current")
_BmVoltageLowActions_Type = DisplayString
_BmVoltageLowActions_Object = MibTableColumn
bmVoltageLowActions = _BmVoltageLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 16),
    _BmVoltageLowActions_Type()
)
bmVoltageLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageLowActions.setStatus("current")
_BmVoltageLowTrapNum_Type = Integer32
_BmVoltageLowTrapNum_Object = MibTableColumn
bmVoltageLowTrapNum = _BmVoltageLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 17),
    _BmVoltageLowTrapNum_Type()
)
bmVoltageLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageLowTrapNum.setStatus("current")
_BmVoltageLowClass_Type = DisplayString
_BmVoltageLowClass_Object = MibTableColumn
bmVoltageLowClass = _BmVoltageLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 18),
    _BmVoltageLowClass_Type()
)
bmVoltageLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageLowClass.setStatus("current")
_BmVoltageVLowValue_Type = DisplayString
_BmVoltageVLowValue_Object = MibTableColumn
bmVoltageVLowValue = _BmVoltageVLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 19),
    _BmVoltageVLowValue_Type()
)
bmVoltageVLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageVLowValue.setStatus("current")
_BmVoltageVLowActions_Type = DisplayString
_BmVoltageVLowActions_Object = MibTableColumn
bmVoltageVLowActions = _BmVoltageVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 20),
    _BmVoltageVLowActions_Type()
)
bmVoltageVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageVLowActions.setStatus("current")
_BmVoltageVLowTrapNum_Type = Integer32
_BmVoltageVLowTrapNum_Object = MibTableColumn
bmVoltageVLowTrapNum = _BmVoltageVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 21),
    _BmVoltageVLowTrapNum_Type()
)
bmVoltageVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageVLowTrapNum.setStatus("current")
_BmVoltageVLowClass_Type = DisplayString
_BmVoltageVLowClass_Object = MibTableColumn
bmVoltageVLowClass = _BmVoltageVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 22),
    _BmVoltageVLowClass_Type()
)
bmVoltageVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageVLowClass.setStatus("current")
_BmVoltageSysrepEnable_Type = DisplayString
_BmVoltageSysrepEnable_Object = MibTableColumn
bmVoltageSysrepEnable = _BmVoltageSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 23),
    _BmVoltageSysrepEnable_Type()
)
bmVoltageSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageSysrepEnable.setStatus("current")
_BmVoltageSysrepThreshold_Type = DisplayString
_BmVoltageSysrepThreshold_Object = MibTableColumn
bmVoltageSysrepThreshold = _BmVoltageSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 24),
    _BmVoltageSysrepThreshold_Type()
)
bmVoltageSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageSysrepThreshold.setStatus("current")
_BmVoltageSysrepLimit_Type = Integer32
_BmVoltageSysrepLimit_Object = MibTableColumn
bmVoltageSysrepLimit = _BmVoltageSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 5, 1, 25),
    _BmVoltageSysrepLimit_Type()
)
bmVoltageSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmVoltageSysrepLimit.setStatus("current")
_BatteryMonitorDiffVoltTable_Object = MibTable
batteryMonitorDiffVoltTable = _BatteryMonitorDiffVoltTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6)
)
if mibBuilder.loadTexts:
    batteryMonitorDiffVoltTable.setStatus("current")
_BmDiffVoltEntry_Object = MibTableRow
bmDiffVoltEntry = _BmDiffVoltEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1)
)
bmDiffVoltEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmDiffVoltIndex"),
)
if mibBuilder.loadTexts:
    bmDiffVoltEntry.setStatus("current")


class _BmDiffVoltIndex_Type(Integer32):
    """Custom type bmDiffVoltIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmDiffVoltIndex_Type.__name__ = "Integer32"
_BmDiffVoltIndex_Object = MibTableColumn
bmDiffVoltIndex = _BmDiffVoltIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 1),
    _BmDiffVoltIndex_Type()
)
bmDiffVoltIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmDiffVoltIndex.setStatus("current")
_BmDiffVoltEnable_Type = DisplayString
_BmDiffVoltEnable_Object = MibTableColumn
bmDiffVoltEnable = _BmDiffVoltEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 2),
    _BmDiffVoltEnable_Type()
)
bmDiffVoltEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltEnable.setStatus("current")
_BmDiffVoltDeadband_Type = DisplayString
_BmDiffVoltDeadband_Object = MibTableColumn
bmDiffVoltDeadband = _BmDiffVoltDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 3),
    _BmDiffVoltDeadband_Type()
)
bmDiffVoltDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltDeadband.setStatus("current")
_BmDiffVoltVHighValue_Type = DisplayString
_BmDiffVoltVHighValue_Object = MibTableColumn
bmDiffVoltVHighValue = _BmDiffVoltVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 4),
    _BmDiffVoltVHighValue_Type()
)
bmDiffVoltVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltVHighValue.setStatus("current")
_BmDiffVoltVHighActions_Type = DisplayString
_BmDiffVoltVHighActions_Object = MibTableColumn
bmDiffVoltVHighActions = _BmDiffVoltVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 5),
    _BmDiffVoltVHighActions_Type()
)
bmDiffVoltVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltVHighActions.setStatus("current")
_BmDiffVoltVHighTrapNum_Type = Integer32
_BmDiffVoltVHighTrapNum_Object = MibTableColumn
bmDiffVoltVHighTrapNum = _BmDiffVoltVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 6),
    _BmDiffVoltVHighTrapNum_Type()
)
bmDiffVoltVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltVHighTrapNum.setStatus("current")
_BmDiffVoltVHighClass_Type = DisplayString
_BmDiffVoltVHighClass_Object = MibTableColumn
bmDiffVoltVHighClass = _BmDiffVoltVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 7),
    _BmDiffVoltVHighClass_Type()
)
bmDiffVoltVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltVHighClass.setStatus("current")
_BmDiffVoltHighValue_Type = DisplayString
_BmDiffVoltHighValue_Object = MibTableColumn
bmDiffVoltHighValue = _BmDiffVoltHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 8),
    _BmDiffVoltHighValue_Type()
)
bmDiffVoltHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltHighValue.setStatus("current")
_BmDiffVoltHighActions_Type = DisplayString
_BmDiffVoltHighActions_Object = MibTableColumn
bmDiffVoltHighActions = _BmDiffVoltHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 9),
    _BmDiffVoltHighActions_Type()
)
bmDiffVoltHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltHighActions.setStatus("current")
_BmDiffVoltHighTrapNum_Type = Integer32
_BmDiffVoltHighTrapNum_Object = MibTableColumn
bmDiffVoltHighTrapNum = _BmDiffVoltHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 10),
    _BmDiffVoltHighTrapNum_Type()
)
bmDiffVoltHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltHighTrapNum.setStatus("current")
_BmDiffVoltHighClass_Type = DisplayString
_BmDiffVoltHighClass_Object = MibTableColumn
bmDiffVoltHighClass = _BmDiffVoltHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 11),
    _BmDiffVoltHighClass_Type()
)
bmDiffVoltHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltHighClass.setStatus("current")
_BmDiffVoltNormalActions_Type = DisplayString
_BmDiffVoltNormalActions_Object = MibTableColumn
bmDiffVoltNormalActions = _BmDiffVoltNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 12),
    _BmDiffVoltNormalActions_Type()
)
bmDiffVoltNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltNormalActions.setStatus("current")
_BmDiffVoltNormalTrapNum_Type = Integer32
_BmDiffVoltNormalTrapNum_Object = MibTableColumn
bmDiffVoltNormalTrapNum = _BmDiffVoltNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 13),
    _BmDiffVoltNormalTrapNum_Type()
)
bmDiffVoltNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltNormalTrapNum.setStatus("current")
_BmDiffVoltNormalClass_Type = DisplayString
_BmDiffVoltNormalClass_Object = MibTableColumn
bmDiffVoltNormalClass = _BmDiffVoltNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 14),
    _BmDiffVoltNormalClass_Type()
)
bmDiffVoltNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltNormalClass.setStatus("current")
_BmDiffVoltSysrepEnable_Type = DisplayString
_BmDiffVoltSysrepEnable_Object = MibTableColumn
bmDiffVoltSysrepEnable = _BmDiffVoltSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 15),
    _BmDiffVoltSysrepEnable_Type()
)
bmDiffVoltSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltSysrepEnable.setStatus("current")
_BmDiffVoltSysrepThreshold_Type = DisplayString
_BmDiffVoltSysrepThreshold_Object = MibTableColumn
bmDiffVoltSysrepThreshold = _BmDiffVoltSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 16),
    _BmDiffVoltSysrepThreshold_Type()
)
bmDiffVoltSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltSysrepThreshold.setStatus("current")
_BmDiffVoltSysrepLimit_Type = Integer32
_BmDiffVoltSysrepLimit_Object = MibTableColumn
bmDiffVoltSysrepLimit = _BmDiffVoltSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 6, 1, 17),
    _BmDiffVoltSysrepLimit_Type()
)
bmDiffVoltSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDiffVoltSysrepLimit.setStatus("current")
_BatteryMonitorChargingCurrentTable_Object = MibTable
batteryMonitorChargingCurrentTable = _BatteryMonitorChargingCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7)
)
if mibBuilder.loadTexts:
    batteryMonitorChargingCurrentTable.setStatus("current")
_BmChargingCurrentEntry_Object = MibTableRow
bmChargingCurrentEntry = _BmChargingCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1)
)
bmChargingCurrentEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmChargingCurrentIndex"),
)
if mibBuilder.loadTexts:
    bmChargingCurrentEntry.setStatus("current")


class _BmChargingCurrentIndex_Type(Integer32):
    """Custom type bmChargingCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmChargingCurrentIndex_Type.__name__ = "Integer32"
_BmChargingCurrentIndex_Object = MibTableColumn
bmChargingCurrentIndex = _BmChargingCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 1),
    _BmChargingCurrentIndex_Type()
)
bmChargingCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmChargingCurrentIndex.setStatus("current")
_BmChargingCurrentEnable_Type = DisplayString
_BmChargingCurrentEnable_Object = MibTableColumn
bmChargingCurrentEnable = _BmChargingCurrentEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 2),
    _BmChargingCurrentEnable_Type()
)
bmChargingCurrentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentEnable.setStatus("current")
_BmChargingCurrentDeadband_Type = DisplayString
_BmChargingCurrentDeadband_Object = MibTableColumn
bmChargingCurrentDeadband = _BmChargingCurrentDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 3),
    _BmChargingCurrentDeadband_Type()
)
bmChargingCurrentDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentDeadband.setStatus("current")
_BmChargingCurrentVHighValue_Type = DisplayString
_BmChargingCurrentVHighValue_Object = MibTableColumn
bmChargingCurrentVHighValue = _BmChargingCurrentVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 4),
    _BmChargingCurrentVHighValue_Type()
)
bmChargingCurrentVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentVHighValue.setStatus("current")
_BmChargingCurrentVHighActions_Type = DisplayString
_BmChargingCurrentVHighActions_Object = MibTableColumn
bmChargingCurrentVHighActions = _BmChargingCurrentVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 5),
    _BmChargingCurrentVHighActions_Type()
)
bmChargingCurrentVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentVHighActions.setStatus("current")
_BmChargingCurrentVHighTrapNum_Type = Integer32
_BmChargingCurrentVHighTrapNum_Object = MibTableColumn
bmChargingCurrentVHighTrapNum = _BmChargingCurrentVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 6),
    _BmChargingCurrentVHighTrapNum_Type()
)
bmChargingCurrentVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentVHighTrapNum.setStatus("current")
_BmChargingCurrentVHighClass_Type = DisplayString
_BmChargingCurrentVHighClass_Object = MibTableColumn
bmChargingCurrentVHighClass = _BmChargingCurrentVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 7),
    _BmChargingCurrentVHighClass_Type()
)
bmChargingCurrentVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentVHighClass.setStatus("current")
_BmChargingCurrentHighValue_Type = DisplayString
_BmChargingCurrentHighValue_Object = MibTableColumn
bmChargingCurrentHighValue = _BmChargingCurrentHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 8),
    _BmChargingCurrentHighValue_Type()
)
bmChargingCurrentHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentHighValue.setStatus("current")
_BmChargingCurrentHighActions_Type = DisplayString
_BmChargingCurrentHighActions_Object = MibTableColumn
bmChargingCurrentHighActions = _BmChargingCurrentHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 9),
    _BmChargingCurrentHighActions_Type()
)
bmChargingCurrentHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentHighActions.setStatus("current")
_BmChargingCurrentHighTrapNum_Type = Integer32
_BmChargingCurrentHighTrapNum_Object = MibTableColumn
bmChargingCurrentHighTrapNum = _BmChargingCurrentHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 10),
    _BmChargingCurrentHighTrapNum_Type()
)
bmChargingCurrentHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentHighTrapNum.setStatus("current")
_BmChargingCurrentHighClass_Type = DisplayString
_BmChargingCurrentHighClass_Object = MibTableColumn
bmChargingCurrentHighClass = _BmChargingCurrentHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 11),
    _BmChargingCurrentHighClass_Type()
)
bmChargingCurrentHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentHighClass.setStatus("current")
_BmChargingCurrentNormalActions_Type = DisplayString
_BmChargingCurrentNormalActions_Object = MibTableColumn
bmChargingCurrentNormalActions = _BmChargingCurrentNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 12),
    _BmChargingCurrentNormalActions_Type()
)
bmChargingCurrentNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentNormalActions.setStatus("current")
_BmChargingCurrentNormalTrapNum_Type = Integer32
_BmChargingCurrentNormalTrapNum_Object = MibTableColumn
bmChargingCurrentNormalTrapNum = _BmChargingCurrentNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 13),
    _BmChargingCurrentNormalTrapNum_Type()
)
bmChargingCurrentNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentNormalTrapNum.setStatus("current")
_BmChargingCurrentNormalClass_Type = DisplayString
_BmChargingCurrentNormalClass_Object = MibTableColumn
bmChargingCurrentNormalClass = _BmChargingCurrentNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 14),
    _BmChargingCurrentNormalClass_Type()
)
bmChargingCurrentNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentNormalClass.setStatus("current")
_BmChargingCurrentSysrepEnable_Type = DisplayString
_BmChargingCurrentSysrepEnable_Object = MibTableColumn
bmChargingCurrentSysrepEnable = _BmChargingCurrentSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 15),
    _BmChargingCurrentSysrepEnable_Type()
)
bmChargingCurrentSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentSysrepEnable.setStatus("current")
_BmChargingCurrentSysrepThreshold_Type = DisplayString
_BmChargingCurrentSysrepThreshold_Object = MibTableColumn
bmChargingCurrentSysrepThreshold = _BmChargingCurrentSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 16),
    _BmChargingCurrentSysrepThreshold_Type()
)
bmChargingCurrentSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentSysrepThreshold.setStatus("current")
_BmChargingCurrentSysrepLimit_Type = Integer32
_BmChargingCurrentSysrepLimit_Object = MibTableColumn
bmChargingCurrentSysrepLimit = _BmChargingCurrentSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 7, 1, 17),
    _BmChargingCurrentSysrepLimit_Type()
)
bmChargingCurrentSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargingCurrentSysrepLimit.setStatus("current")
_BatteryMonitorDischargingCurrentTable_Object = MibTable
batteryMonitorDischargingCurrentTable = _BatteryMonitorDischargingCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8)
)
if mibBuilder.loadTexts:
    batteryMonitorDischargingCurrentTable.setStatus("current")
_BmDischargingCurrentEntry_Object = MibTableRow
bmDischargingCurrentEntry = _BmDischargingCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1)
)
bmDischargingCurrentEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmDischargingCurrentIndex"),
)
if mibBuilder.loadTexts:
    bmDischargingCurrentEntry.setStatus("current")


class _BmDischargingCurrentIndex_Type(Integer32):
    """Custom type bmDischargingCurrentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmDischargingCurrentIndex_Type.__name__ = "Integer32"
_BmDischargingCurrentIndex_Object = MibTableColumn
bmDischargingCurrentIndex = _BmDischargingCurrentIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 1),
    _BmDischargingCurrentIndex_Type()
)
bmDischargingCurrentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmDischargingCurrentIndex.setStatus("current")
_BmDischargingCurrentEnable_Type = DisplayString
_BmDischargingCurrentEnable_Object = MibTableColumn
bmDischargingCurrentEnable = _BmDischargingCurrentEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 2),
    _BmDischargingCurrentEnable_Type()
)
bmDischargingCurrentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentEnable.setStatus("current")
_BmDischargingCurrentDeadband_Type = DisplayString
_BmDischargingCurrentDeadband_Object = MibTableColumn
bmDischargingCurrentDeadband = _BmDischargingCurrentDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 3),
    _BmDischargingCurrentDeadband_Type()
)
bmDischargingCurrentDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentDeadband.setStatus("current")
_BmDischargingCurrentVHighValue_Type = DisplayString
_BmDischargingCurrentVHighValue_Object = MibTableColumn
bmDischargingCurrentVHighValue = _BmDischargingCurrentVHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 4),
    _BmDischargingCurrentVHighValue_Type()
)
bmDischargingCurrentVHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentVHighValue.setStatus("current")
_BmDischargingCurrentVHighActions_Type = DisplayString
_BmDischargingCurrentVHighActions_Object = MibTableColumn
bmDischargingCurrentVHighActions = _BmDischargingCurrentVHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 5),
    _BmDischargingCurrentVHighActions_Type()
)
bmDischargingCurrentVHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentVHighActions.setStatus("current")
_BmDischargingCurrentVHighTrapNum_Type = Integer32
_BmDischargingCurrentVHighTrapNum_Object = MibTableColumn
bmDischargingCurrentVHighTrapNum = _BmDischargingCurrentVHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 6),
    _BmDischargingCurrentVHighTrapNum_Type()
)
bmDischargingCurrentVHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentVHighTrapNum.setStatus("current")
_BmDischargingCurrentVHighClass_Type = DisplayString
_BmDischargingCurrentVHighClass_Object = MibTableColumn
bmDischargingCurrentVHighClass = _BmDischargingCurrentVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 7),
    _BmDischargingCurrentVHighClass_Type()
)
bmDischargingCurrentVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentVHighClass.setStatus("current")
_BmDischargingCurrentHighValue_Type = DisplayString
_BmDischargingCurrentHighValue_Object = MibTableColumn
bmDischargingCurrentHighValue = _BmDischargingCurrentHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 8),
    _BmDischargingCurrentHighValue_Type()
)
bmDischargingCurrentHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentHighValue.setStatus("current")
_BmDischargingCurrentHighActions_Type = DisplayString
_BmDischargingCurrentHighActions_Object = MibTableColumn
bmDischargingCurrentHighActions = _BmDischargingCurrentHighActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 9),
    _BmDischargingCurrentHighActions_Type()
)
bmDischargingCurrentHighActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentHighActions.setStatus("current")
_BmDischargingCurrentHighTrapNum_Type = Integer32
_BmDischargingCurrentHighTrapNum_Object = MibTableColumn
bmDischargingCurrentHighTrapNum = _BmDischargingCurrentHighTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 10),
    _BmDischargingCurrentHighTrapNum_Type()
)
bmDischargingCurrentHighTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentHighTrapNum.setStatus("current")
_BmDischargingCurrentHighClass_Type = DisplayString
_BmDischargingCurrentHighClass_Object = MibTableColumn
bmDischargingCurrentHighClass = _BmDischargingCurrentHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 11),
    _BmDischargingCurrentHighClass_Type()
)
bmDischargingCurrentHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentHighClass.setStatus("current")
_BmDischargingCurrentNormalActions_Type = DisplayString
_BmDischargingCurrentNormalActions_Object = MibTableColumn
bmDischargingCurrentNormalActions = _BmDischargingCurrentNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 12),
    _BmDischargingCurrentNormalActions_Type()
)
bmDischargingCurrentNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentNormalActions.setStatus("current")
_BmDischargingCurrentNormalTrapNum_Type = Integer32
_BmDischargingCurrentNormalTrapNum_Object = MibTableColumn
bmDischargingCurrentNormalTrapNum = _BmDischargingCurrentNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 13),
    _BmDischargingCurrentNormalTrapNum_Type()
)
bmDischargingCurrentNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentNormalTrapNum.setStatus("current")
_BmDischargingCurrentNormalClass_Type = DisplayString
_BmDischargingCurrentNormalClass_Object = MibTableColumn
bmDischargingCurrentNormalClass = _BmDischargingCurrentNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 14),
    _BmDischargingCurrentNormalClass_Type()
)
bmDischargingCurrentNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentNormalClass.setStatus("current")
_BmDischargingCurrentSysrepEnable_Type = DisplayString
_BmDischargingCurrentSysrepEnable_Object = MibTableColumn
bmDischargingCurrentSysrepEnable = _BmDischargingCurrentSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 15),
    _BmDischargingCurrentSysrepEnable_Type()
)
bmDischargingCurrentSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentSysrepEnable.setStatus("current")
_BmDischargingCurrentSysrepThreshold_Type = DisplayString
_BmDischargingCurrentSysrepThreshold_Object = MibTableColumn
bmDischargingCurrentSysrepThreshold = _BmDischargingCurrentSysrepThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 16),
    _BmDischargingCurrentSysrepThreshold_Type()
)
bmDischargingCurrentSysrepThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentSysrepThreshold.setStatus("current")
_BmDischargingCurrentSysrepLimit_Type = Integer32
_BmDischargingCurrentSysrepLimit_Object = MibTableColumn
bmDischargingCurrentSysrepLimit = _BmDischargingCurrentSysrepLimit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 8, 1, 17),
    _BmDischargingCurrentSysrepLimit_Type()
)
bmDischargingCurrentSysrepLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmDischargingCurrentSysrepLimit.setStatus("current")
_BatteryMonitorChargeLevelTable_Object = MibTable
batteryMonitorChargeLevelTable = _BatteryMonitorChargeLevelTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9)
)
if mibBuilder.loadTexts:
    batteryMonitorChargeLevelTable.setStatus("current")
_BmChargeLevelEntry_Object = MibTableRow
bmChargeLevelEntry = _BmChargeLevelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1)
)
bmChargeLevelEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmChargeLevelIndex"),
)
if mibBuilder.loadTexts:
    bmChargeLevelEntry.setStatus("current")


class _BmChargeLevelIndex_Type(Integer32):
    """Custom type bmChargeLevelIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmChargeLevelIndex_Type.__name__ = "Integer32"
_BmChargeLevelIndex_Object = MibTableColumn
bmChargeLevelIndex = _BmChargeLevelIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 1),
    _BmChargeLevelIndex_Type()
)
bmChargeLevelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmChargeLevelIndex.setStatus("current")
_BmChargeLevelEnable_Type = DisplayString
_BmChargeLevelEnable_Object = MibTableColumn
bmChargeLevelEnable = _BmChargeLevelEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 2),
    _BmChargeLevelEnable_Type()
)
bmChargeLevelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelEnable.setStatus("current")
_BmChargeLevelNormalActions_Type = DisplayString
_BmChargeLevelNormalActions_Object = MibTableColumn
bmChargeLevelNormalActions = _BmChargeLevelNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 3),
    _BmChargeLevelNormalActions_Type()
)
bmChargeLevelNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelNormalActions.setStatus("current")
_BmChargeLevelNormalTrapNum_Type = Integer32
_BmChargeLevelNormalTrapNum_Object = MibTableColumn
bmChargeLevelNormalTrapNum = _BmChargeLevelNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 4),
    _BmChargeLevelNormalTrapNum_Type()
)
bmChargeLevelNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelNormalTrapNum.setStatus("current")
_BmChargeLevelNormalClass_Type = DisplayString
_BmChargeLevelNormalClass_Object = MibTableColumn
bmChargeLevelNormalClass = _BmChargeLevelNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 5),
    _BmChargeLevelNormalClass_Type()
)
bmChargeLevelNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelNormalClass.setStatus("current")
_BmChargeLevelLowActions_Type = DisplayString
_BmChargeLevelLowActions_Object = MibTableColumn
bmChargeLevelLowActions = _BmChargeLevelLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 6),
    _BmChargeLevelLowActions_Type()
)
bmChargeLevelLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelLowActions.setStatus("current")
_BmChargeLevelLowTrapNum_Type = Integer32
_BmChargeLevelLowTrapNum_Object = MibTableColumn
bmChargeLevelLowTrapNum = _BmChargeLevelLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 7),
    _BmChargeLevelLowTrapNum_Type()
)
bmChargeLevelLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelLowTrapNum.setStatus("current")
_BmChargeLevelLowClass_Type = DisplayString
_BmChargeLevelLowClass_Object = MibTableColumn
bmChargeLevelLowClass = _BmChargeLevelLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 8),
    _BmChargeLevelLowClass_Type()
)
bmChargeLevelLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelLowClass.setStatus("current")
_BmChargeLevelVLowActions_Type = DisplayString
_BmChargeLevelVLowActions_Object = MibTableColumn
bmChargeLevelVLowActions = _BmChargeLevelVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 9),
    _BmChargeLevelVLowActions_Type()
)
bmChargeLevelVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelVLowActions.setStatus("current")
_BmChargeLevelVLowTrapNum_Type = Integer32
_BmChargeLevelVLowTrapNum_Object = MibTableColumn
bmChargeLevelVLowTrapNum = _BmChargeLevelVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 10),
    _BmChargeLevelVLowTrapNum_Type()
)
bmChargeLevelVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelVLowTrapNum.setStatus("current")
_BmChargeLevelVLowClass_Type = DisplayString
_BmChargeLevelVLowClass_Object = MibTableColumn
bmChargeLevelVLowClass = _BmChargeLevelVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 11),
    _BmChargeLevelVLowClass_Type()
)
bmChargeLevelVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelVLowClass.setStatus("current")
_BmChargeLevelSysrepEnable_Type = DisplayString
_BmChargeLevelSysrepEnable_Object = MibTableColumn
bmChargeLevelSysrepEnable = _BmChargeLevelSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 9, 1, 12),
    _BmChargeLevelSysrepEnable_Type()
)
bmChargeLevelSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmChargeLevelSysrepEnable.setStatus("current")
_BatteryMonitorJarHealthTable_Object = MibTable
batteryMonitorJarHealthTable = _BatteryMonitorJarHealthTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10)
)
if mibBuilder.loadTexts:
    batteryMonitorJarHealthTable.setStatus("current")
_BmJarHealthEntry_Object = MibTableRow
bmJarHealthEntry = _BmJarHealthEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1)
)
bmJarHealthEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "bmJarHealthIndex"),
)
if mibBuilder.loadTexts:
    bmJarHealthEntry.setStatus("current")


class _BmJarHealthIndex_Type(Integer32):
    """Custom type bmJarHealthIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_BmJarHealthIndex_Type.__name__ = "Integer32"
_BmJarHealthIndex_Object = MibTableColumn
bmJarHealthIndex = _BmJarHealthIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 1),
    _BmJarHealthIndex_Type()
)
bmJarHealthIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmJarHealthIndex.setStatus("current")
_BmJarHealthEnable_Type = DisplayString
_BmJarHealthEnable_Object = MibTableColumn
bmJarHealthEnable = _BmJarHealthEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 2),
    _BmJarHealthEnable_Type()
)
bmJarHealthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthEnable.setStatus("current")
_BmJarHealthNormalActions_Type = DisplayString
_BmJarHealthNormalActions_Object = MibTableColumn
bmJarHealthNormalActions = _BmJarHealthNormalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 3),
    _BmJarHealthNormalActions_Type()
)
bmJarHealthNormalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthNormalActions.setStatus("current")
_BmJarHealthNormalTrapNum_Type = Integer32
_BmJarHealthNormalTrapNum_Object = MibTableColumn
bmJarHealthNormalTrapNum = _BmJarHealthNormalTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 4),
    _BmJarHealthNormalTrapNum_Type()
)
bmJarHealthNormalTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthNormalTrapNum.setStatus("current")
_BmJarHealthNormalClass_Type = DisplayString
_BmJarHealthNormalClass_Object = MibTableColumn
bmJarHealthNormalClass = _BmJarHealthNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 5),
    _BmJarHealthNormalClass_Type()
)
bmJarHealthNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthNormalClass.setStatus("current")
_BmJarHealthLowActions_Type = DisplayString
_BmJarHealthLowActions_Object = MibTableColumn
bmJarHealthLowActions = _BmJarHealthLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 6),
    _BmJarHealthLowActions_Type()
)
bmJarHealthLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthLowActions.setStatus("current")
_BmJarHealthLowTrapNum_Type = Integer32
_BmJarHealthLowTrapNum_Object = MibTableColumn
bmJarHealthLowTrapNum = _BmJarHealthLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 7),
    _BmJarHealthLowTrapNum_Type()
)
bmJarHealthLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthLowTrapNum.setStatus("current")
_BmJarHealthLowClass_Type = DisplayString
_BmJarHealthLowClass_Object = MibTableColumn
bmJarHealthLowClass = _BmJarHealthLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 8),
    _BmJarHealthLowClass_Type()
)
bmJarHealthLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthLowClass.setStatus("current")
_BmJarHealthVLowActions_Type = DisplayString
_BmJarHealthVLowActions_Object = MibTableColumn
bmJarHealthVLowActions = _BmJarHealthVLowActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 9),
    _BmJarHealthVLowActions_Type()
)
bmJarHealthVLowActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthVLowActions.setStatus("current")
_BmJarHealthVLowTrapNum_Type = Integer32
_BmJarHealthVLowTrapNum_Object = MibTableColumn
bmJarHealthVLowTrapNum = _BmJarHealthVLowTrapNum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 10),
    _BmJarHealthVLowTrapNum_Type()
)
bmJarHealthVLowTrapNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthVLowTrapNum.setStatus("current")
_BmJarHealthVLowClass_Type = DisplayString
_BmJarHealthVLowClass_Object = MibTableColumn
bmJarHealthVLowClass = _BmJarHealthVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 11),
    _BmJarHealthVLowClass_Type()
)
bmJarHealthVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthVLowClass.setStatus("current")
_BmJarHealthSysrepEnable_Type = DisplayString
_BmJarHealthSysrepEnable_Object = MibTableColumn
bmJarHealthSysrepEnable = _BmJarHealthSysrepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 14, 10, 1, 12),
    _BmJarHealthSysrepEnable_Type()
)
bmJarHealthSysrepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bmJarHealthSysrepEnable.setStatus("current")
_EvLocation_ObjectIdentity = ObjectIdentity
evLocation = _EvLocation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 15)
)
_EvLocationEnable_Type = DisplayString
_EvLocationEnable_Object = MibScalar
evLocationEnable = _EvLocationEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 15, 1),
    _EvLocationEnable_Type()
)
evLocationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLocationEnable.setStatus("current")


class _EvLocationTimeout_Type(Integer32):
    """Custom type evLocationTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 60),
    )


_EvLocationTimeout_Type.__name__ = "Integer32"
_EvLocationTimeout_Object = MibScalar
evLocationTimeout = _EvLocationTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 15, 2),
    _EvLocationTimeout_Type()
)
evLocationTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLocationTimeout.setStatus("current")
_EvLocationActions_Type = DisplayString
_EvLocationActions_Object = MibScalar
evLocationActions = _EvLocationActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 15, 3),
    _EvLocationActions_Type()
)
evLocationActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLocationActions.setStatus("current")
_EvLocationMsgSuccess_Type = DisplayString
_EvLocationMsgSuccess_Object = MibScalar
evLocationMsgSuccess = _EvLocationMsgSuccess_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 15, 4),
    _EvLocationMsgSuccess_Type()
)
evLocationMsgSuccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLocationMsgSuccess.setStatus("current")
_EvLocationMsgFail_Type = DisplayString
_EvLocationMsgFail_Object = MibScalar
evLocationMsgFail = _EvLocationMsgFail_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 15, 5),
    _EvLocationMsgFail_Type()
)
evLocationMsgFail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLocationMsgFail.setStatus("current")
_EvLocationIncludeLocation_Type = DisplayString
_EvLocationIncludeLocation_Object = MibScalar
evLocationIncludeLocation = _EvLocationIncludeLocation_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 15, 6),
    _EvLocationIncludeLocation_Type()
)
evLocationIncludeLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLocationIncludeLocation.setStatus("current")


class _EvLocationTrapnum_Type(Integer32):
    """Custom type evLocationTrapnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(541, 1199),
    )


_EvLocationTrapnum_Type.__name__ = "Integer32"
_EvLocationTrapnum_Object = MibScalar
evLocationTrapnum = _EvLocationTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 15, 7),
    _EvLocationTrapnum_Type()
)
evLocationTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLocationTrapnum.setStatus("current")
_EvLocationClass_Type = DisplayString
_EvLocationClass_Object = MibScalar
evLocationClass = _EvLocationClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 15, 8),
    _EvLocationClass_Type()
)
evLocationClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evLocationClass.setStatus("current")
_EvReset_ObjectIdentity = ObjectIdentity
evReset = _EvReset_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 16)
)
_EvResetEnable_Type = DisplayString
_EvResetEnable_Object = MibScalar
evResetEnable = _EvResetEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 16, 1),
    _EvResetEnable_Type()
)
evResetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetEnable.setStatus("current")


class _EvResetDelay_Type(Integer32):
    """Custom type evResetDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_EvResetDelay_Type.__name__ = "Integer32"
_EvResetDelay_Object = MibScalar
evResetDelay = _EvResetDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 16, 2),
    _EvResetDelay_Type()
)
evResetDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetDelay.setStatus("current")
_EvResetActions_Type = DisplayString
_EvResetActions_Object = MibScalar
evResetActions = _EvResetActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 16, 3),
    _EvResetActions_Type()
)
evResetActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetActions.setStatus("current")
_EvResetMessage_Type = DisplayString
_EvResetMessage_Object = MibScalar
evResetMessage = _EvResetMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 16, 4),
    _EvResetMessage_Type()
)
evResetMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetMessage.setStatus("current")


class _EvResetTrapnum_Type(Integer32):
    """Custom type evResetTrapnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(543, 1199),
    )


_EvResetTrapnum_Type.__name__ = "Integer32"
_EvResetTrapnum_Object = MibScalar
evResetTrapnum = _EvResetTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 16, 5),
    _EvResetTrapnum_Type()
)
evResetTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetTrapnum.setStatus("current")
_EvResetClass_Type = DisplayString
_EvResetClass_Object = MibScalar
evResetClass = _EvResetClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 16, 6),
    _EvResetClass_Type()
)
evResetClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evResetClass.setStatus("current")
_EvSleep_ObjectIdentity = ObjectIdentity
evSleep = _EvSleep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 17)
)
_EvSleepEnable_Type = DisplayString
_EvSleepEnable_Object = MibScalar
evSleepEnable = _EvSleepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 17, 1),
    _EvSleepEnable_Type()
)
evSleepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSleepEnable.setStatus("current")
_EvSleepActions_Type = DisplayString
_EvSleepActions_Object = MibScalar
evSleepActions = _EvSleepActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 17, 3),
    _EvSleepActions_Type()
)
evSleepActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSleepActions.setStatus("current")
_EvSleepMessage_Type = DisplayString
_EvSleepMessage_Object = MibScalar
evSleepMessage = _EvSleepMessage_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 17, 4),
    _EvSleepMessage_Type()
)
evSleepMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSleepMessage.setStatus("current")


class _EvSleepTrapnum_Type(Integer32):
    """Custom type evSleepTrapnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(542, 1199),
    )


_EvSleepTrapnum_Type.__name__ = "Integer32"
_EvSleepTrapnum_Object = MibScalar
evSleepTrapnum = _EvSleepTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 17, 5),
    _EvSleepTrapnum_Type()
)
evSleepTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSleepTrapnum.setStatus("current")
_EvSleepClass_Type = DisplayString
_EvSleepClass_Object = MibScalar
evSleepClass = _EvSleepClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 17, 6),
    _EvSleepClass_Type()
)
evSleepClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evSleepClass.setStatus("current")
_EvGlobal_ObjectIdentity = ObjectIdentity
evGlobal = _EvGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 18)
)
_EvGlobalActions_Type = DisplayString
_EvGlobalActions_Object = MibScalar
evGlobalActions = _EvGlobalActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 18, 2),
    _EvGlobalActions_Type()
)
evGlobalActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evGlobalActions.setStatus("current")


class _EvGlobalTrapnum_Type(Integer32):
    """Custom type evGlobalTrapnum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1199),
    )


_EvGlobalTrapnum_Type.__name__ = "Integer32"
_EvGlobalTrapnum_Object = MibScalar
evGlobalTrapnum = _EvGlobalTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 18, 3),
    _EvGlobalTrapnum_Type()
)
evGlobalTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    evGlobalTrapnum.setStatus("current")
_AccessControl_ObjectIdentity = ObjectIdentity
accessControl = _AccessControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21)
)
_AcActions_Type = DisplayString
_AcActions_Object = MibScalar
acActions = _AcActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 2),
    _AcActions_Type()
)
acActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acActions.setStatus("current")
_AcTrapnum_Type = Integer32
_AcTrapnum_Object = MibScalar
acTrapnum = _AcTrapnum_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 3),
    _AcTrapnum_Type()
)
acTrapnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acTrapnum.setStatus("current")
_AcClass_Type = DisplayString
_AcClass_Object = MibScalar
acClass = _AcClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 4),
    _AcClass_Type()
)
acClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acClass.setStatus("current")
_AccessControlDeviceTable_Object = MibTable
accessControlDeviceTable = _AccessControlDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10)
)
if mibBuilder.loadTexts:
    accessControlDeviceTable.setStatus("current")
_AccessControlDeviceEntry_Object = MibTableRow
accessControlDeviceEntry = _AccessControlDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1)
)
accessControlDeviceEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "acdIndex"),
)
if mibBuilder.loadTexts:
    accessControlDeviceEntry.setStatus("current")


class _AcdIndex_Type(Integer32):
    """Custom type acdIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcdIndex_Type.__name__ = "Integer32"
_AcdIndex_Object = MibTableColumn
acdIndex = _AcdIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1, 1),
    _AcdIndex_Type()
)
acdIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acdIndex.setStatus("current")
_AcdEnable_Type = DisplayString
_AcdEnable_Object = MibTableColumn
acdEnable = _AcdEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1, 2),
    _AcdEnable_Type()
)
acdEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdEnable.setStatus("current")
_AcdName_Type = DisplayString
_AcdName_Object = MibTableColumn
acdName = _AcdName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1, 3),
    _AcdName_Type()
)
acdName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdName.setStatus("current")
_AcdReader_Type = DisplayString
_AcdReader_Object = MibTableColumn
acdReader = _AcdReader_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1, 4),
    _AcdReader_Type()
)
acdReader.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdReader.setStatus("current")
_AcdWiegandES_Type = Integer32
_AcdWiegandES_Object = MibTableColumn
acdWiegandES = _AcdWiegandES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1, 6),
    _AcdWiegandES_Type()
)
acdWiegandES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdWiegandES.setStatus("current")
_AcdRelayType_Type = DisplayString
_AcdRelayType_Object = MibTableColumn
acdRelayType = _AcdRelayType_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1, 7),
    _AcdRelayType_Type()
)
acdRelayType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdRelayType.setStatus("current")
_AcdRelayES_Type = Integer32
_AcdRelayES_Object = MibTableColumn
acdRelayES = _AcdRelayES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1, 8),
    _AcdRelayES_Type()
)
acdRelayES.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdRelayES.setStatus("current")
_AcdRelayPoint_Type = Integer32
_AcdRelayPoint_Object = MibTableColumn
acdRelayPoint = _AcdRelayPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1, 9),
    _AcdRelayPoint_Type()
)
acdRelayPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdRelayPoint.setStatus("current")


class _AcdOpenTime_Type(Integer32):
    """Custom type acdOpenTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 25),
    )


_AcdOpenTime_Type.__name__ = "Integer32"
_AcdOpenTime_Object = MibTableColumn
acdOpenTime = _AcdOpenTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1, 10),
    _AcdOpenTime_Type()
)
acdOpenTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdOpenTime.setStatus("current")


class _AcdUserGroup_Type(Integer32):
    """Custom type acdUserGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcdUserGroup_Type.__name__ = "Integer32"
_AcdUserGroup_Object = MibTableColumn
acdUserGroup = _AcdUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 10, 1, 11),
    _AcdUserGroup_Type()
)
acdUserGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acdUserGroup.setStatus("current")
_AccessControlUserTable_Object = MibTable
accessControlUserTable = _AccessControlUserTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11)
)
if mibBuilder.loadTexts:
    accessControlUserTable.setStatus("current")
_AccessControlUserEntry_Object = MibTableRow
accessControlUserEntry = _AccessControlUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1)
)
accessControlUserEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "acuIndexUserGroup"),
    (0, "SITEBOSS-350-STD-MIB", "acuIndexUser"),
)
if mibBuilder.loadTexts:
    accessControlUserEntry.setStatus("current")


class _AcuIndexUserGroup_Type(Integer32):
    """Custom type acuIndexUserGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_AcuIndexUserGroup_Type.__name__ = "Integer32"
_AcuIndexUserGroup_Object = MibTableColumn
acuIndexUserGroup = _AcuIndexUserGroup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 1),
    _AcuIndexUserGroup_Type()
)
acuIndexUserGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acuIndexUserGroup.setStatus("current")


class _AcuIndexUser_Type(Integer32):
    """Custom type acuIndexUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_AcuIndexUser_Type.__name__ = "Integer32"
_AcuIndexUser_Object = MibTableColumn
acuIndexUser = _AcuIndexUser_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 2),
    _AcuIndexUser_Type()
)
acuIndexUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acuIndexUser.setStatus("current")
_AcuEnable_Type = DisplayString
_AcuEnable_Object = MibTableColumn
acuEnable = _AcuEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 3),
    _AcuEnable_Type()
)
acuEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuEnable.setStatus("current")
_AcuName_Type = DisplayString
_AcuName_Object = MibTableColumn
acuName = _AcuName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 4),
    _AcuName_Type()
)
acuName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuName.setStatus("current")
_AcuSn_Type = DisplayString
_AcuSn_Object = MibTableColumn
acuSn = _AcuSn_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 5),
    _AcuSn_Type()
)
acuSn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuSn.setStatus("current")
_AcuSunBegin_Type = DisplayString
_AcuSunBegin_Object = MibTableColumn
acuSunBegin = _AcuSunBegin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 6),
    _AcuSunBegin_Type()
)
acuSunBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuSunBegin.setStatus("current")
_AcuSunEnd_Type = DisplayString
_AcuSunEnd_Object = MibTableColumn
acuSunEnd = _AcuSunEnd_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 7),
    _AcuSunEnd_Type()
)
acuSunEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuSunEnd.setStatus("current")
_AcuMonBegin_Type = DisplayString
_AcuMonBegin_Object = MibTableColumn
acuMonBegin = _AcuMonBegin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 8),
    _AcuMonBegin_Type()
)
acuMonBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuMonBegin.setStatus("current")
_AcuMonEnd_Type = DisplayString
_AcuMonEnd_Object = MibTableColumn
acuMonEnd = _AcuMonEnd_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 9),
    _AcuMonEnd_Type()
)
acuMonEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuMonEnd.setStatus("current")
_AcuTueBegin_Type = DisplayString
_AcuTueBegin_Object = MibTableColumn
acuTueBegin = _AcuTueBegin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 10),
    _AcuTueBegin_Type()
)
acuTueBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuTueBegin.setStatus("current")
_AcuTueEnd_Type = DisplayString
_AcuTueEnd_Object = MibTableColumn
acuTueEnd = _AcuTueEnd_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 11),
    _AcuTueEnd_Type()
)
acuTueEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuTueEnd.setStatus("current")
_AcuWedBegin_Type = DisplayString
_AcuWedBegin_Object = MibTableColumn
acuWedBegin = _AcuWedBegin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 12),
    _AcuWedBegin_Type()
)
acuWedBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuWedBegin.setStatus("current")
_AcuWedEnd_Type = DisplayString
_AcuWedEnd_Object = MibTableColumn
acuWedEnd = _AcuWedEnd_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 13),
    _AcuWedEnd_Type()
)
acuWedEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuWedEnd.setStatus("current")
_AcuThuBegin_Type = DisplayString
_AcuThuBegin_Object = MibTableColumn
acuThuBegin = _AcuThuBegin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 14),
    _AcuThuBegin_Type()
)
acuThuBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuThuBegin.setStatus("current")
_AcuThuEnd_Type = DisplayString
_AcuThuEnd_Object = MibTableColumn
acuThuEnd = _AcuThuEnd_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 15),
    _AcuThuEnd_Type()
)
acuThuEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuThuEnd.setStatus("current")
_AcuFriBegin_Type = DisplayString
_AcuFriBegin_Object = MibTableColumn
acuFriBegin = _AcuFriBegin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 16),
    _AcuFriBegin_Type()
)
acuFriBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuFriBegin.setStatus("current")
_AcuFriEnd_Type = DisplayString
_AcuFriEnd_Object = MibTableColumn
acuFriEnd = _AcuFriEnd_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 17),
    _AcuFriEnd_Type()
)
acuFriEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuFriEnd.setStatus("current")
_AcuSatBegin_Type = DisplayString
_AcuSatBegin_Object = MibTableColumn
acuSatBegin = _AcuSatBegin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 18),
    _AcuSatBegin_Type()
)
acuSatBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuSatBegin.setStatus("current")
_AcuSatEnd_Type = DisplayString
_AcuSatEnd_Object = MibTableColumn
acuSatEnd = _AcuSatEnd_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 12, 21, 11, 1, 19),
    _AcuSatEnd_Type()
)
acuSatEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acuSatEnd.setStatus("current")
_Action_ObjectIdentity = ObjectIdentity
action = _Action_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14)
)
_ActionSched_ObjectIdentity = ObjectIdentity
actionSched = _ActionSched_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 3)
)
_ActionSchedEnable_Type = DisplayString
_ActionSchedEnable_Object = MibScalar
actionSchedEnable = _ActionSchedEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 3, 1),
    _ActionSchedEnable_Type()
)
actionSchedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionSchedEnable.setStatus("current")
_ActionSchedBegin_Type = DisplayString
_ActionSchedBegin_Object = MibScalar
actionSchedBegin = _ActionSchedBegin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 3, 2),
    _ActionSchedBegin_Type()
)
actionSchedBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionSchedBegin.setStatus("current")
_ActionSchedEnd_Type = DisplayString
_ActionSchedEnd_Object = MibScalar
actionSchedEnd = _ActionSchedEnd_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 3, 3),
    _ActionSchedEnd_Type()
)
actionSchedEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionSchedEnd.setStatus("current")
_ActionSchedWeekdaysOnly_Type = DisplayString
_ActionSchedWeekdaysOnly_Object = MibScalar
actionSchedWeekdaysOnly = _ActionSchedWeekdaysOnly_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 3, 4),
    _ActionSchedWeekdaysOnly_Type()
)
actionSchedWeekdaysOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionSchedWeekdaysOnly.setStatus("current")
_ActionAsentria_ObjectIdentity = ObjectIdentity
actionAsentria = _ActionAsentria_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 4)
)
_ActionAsentriaRequireAck_Type = DisplayString
_ActionAsentriaRequireAck_Object = MibScalar
actionAsentriaRequireAck = _ActionAsentriaRequireAck_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 4, 1),
    _ActionAsentriaRequireAck_Type()
)
actionAsentriaRequireAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionAsentriaRequireAck.setStatus("current")
_ActionAsentriaVersion_Type = DisplayString
_ActionAsentriaVersion_Object = MibScalar
actionAsentriaVersion = _ActionAsentriaVersion_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 4, 2),
    _ActionAsentriaVersion_Type()
)
actionAsentriaVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionAsentriaVersion.setStatus("current")
_ActionAsentriaTCPPort_Type = Integer32
_ActionAsentriaTCPPort_Object = MibScalar
actionAsentriaTCPPort = _ActionAsentriaTCPPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 4, 3),
    _ActionAsentriaTCPPort_Type()
)
actionAsentriaTCPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionAsentriaTCPPort.setStatus("current")
_ActionHostTable_Object = MibTable
actionHostTable = _ActionHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 6)
)
if mibBuilder.loadTexts:
    actionHostTable.setStatus("current")
_ActionHostEntry_Object = MibTableRow
actionHostEntry = _ActionHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 6, 1)
)
actionHostEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "actionHostIndex"),
)
if mibBuilder.loadTexts:
    actionHostEntry.setStatus("current")


class _ActionHostIndex_Type(Integer32):
    """Custom type actionHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ActionHostIndex_Type.__name__ = "Integer32"
_ActionHostIndex_Object = MibTableColumn
actionHostIndex = _ActionHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 6, 1, 1),
    _ActionHostIndex_Type()
)
actionHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionHostIndex.setStatus("current")
_ActionHost_Type = DisplayString
_ActionHost_Object = MibTableColumn
actionHost = _ActionHost_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 6, 1, 2),
    _ActionHost_Type()
)
actionHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionHost.setStatus("current")
_ActionEmailTable_Object = MibTable
actionEmailTable = _ActionEmailTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 7)
)
if mibBuilder.loadTexts:
    actionEmailTable.setStatus("current")
_ActionEmailEntry_Object = MibTableRow
actionEmailEntry = _ActionEmailEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 7, 1)
)
actionEmailEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "actionEmailIndex"),
)
if mibBuilder.loadTexts:
    actionEmailEntry.setStatus("current")


class _ActionEmailIndex_Type(Integer32):
    """Custom type actionEmailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ActionEmailIndex_Type.__name__ = "Integer32"
_ActionEmailIndex_Object = MibTableColumn
actionEmailIndex = _ActionEmailIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 7, 1, 1),
    _ActionEmailIndex_Type()
)
actionEmailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionEmailIndex.setStatus("current")
_ActionEmail_Type = DisplayString
_ActionEmail_Object = MibTableColumn
actionEmail = _ActionEmail_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 7, 1, 2),
    _ActionEmail_Type()
)
actionEmail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionEmail.setStatus("current")
_ActionParseError_Type = DisplayString
_ActionParseError_Object = MibScalar
actionParseError = _ActionParseError_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 14, 8),
    _ActionParseError_Type()
)
actionParseError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    actionParseError.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16)
)
_SysTime_ObjectIdentity = ObjectIdentity
sysTime = _SysTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 1)
)
_SysTimeAutoDST_Type = DisplayString
_SysTimeAutoDST_Object = MibScalar
sysTimeAutoDST = _SysTimeAutoDST_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 1, 1),
    _SysTimeAutoDST_Type()
)
sysTimeAutoDST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeAutoDST.setStatus("current")
_SysTimeGMTOffset_Type = Integer32
_SysTimeGMTOffset_Object = MibScalar
sysTimeGMTOffset = _SysTimeGMTOffset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 1, 2),
    _SysTimeGMTOffset_Type()
)
sysTimeGMTOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeGMTOffset.setStatus("current")
_SysTimeGMTDirection_Type = DisplayString
_SysTimeGMTDirection_Object = MibScalar
sysTimeGMTDirection = _SysTimeGMTDirection_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 1, 3),
    _SysTimeGMTDirection_Type()
)
sysTimeGMTDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeGMTDirection.setStatus("current")
_SysTimeNet_ObjectIdentity = ObjectIdentity
sysTimeNet = _SysTimeNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 1, 4)
)
_SysTimeNetEnable_Type = DisplayString
_SysTimeNetEnable_Object = MibScalar
sysTimeNetEnable = _SysTimeNetEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 1, 4, 1),
    _SysTimeNetEnable_Type()
)
sysTimeNetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeNetEnable.setStatus("current")
_SysTimeNetHostTable_Object = MibTable
sysTimeNetHostTable = _SysTimeNetHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 1, 4, 2)
)
if mibBuilder.loadTexts:
    sysTimeNetHostTable.setStatus("current")
_SysTimeNetHostEntry_Object = MibTableRow
sysTimeNetHostEntry = _SysTimeNetHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 1, 4, 2, 1)
)
sysTimeNetHostEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "sysTimeNetHostIndex"),
)
if mibBuilder.loadTexts:
    sysTimeNetHostEntry.setStatus("current")


class _SysTimeNetHostIndex_Type(Integer32):
    """Custom type sysTimeNetHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SysTimeNetHostIndex_Type.__name__ = "Integer32"
_SysTimeNetHostIndex_Object = MibTableColumn
sysTimeNetHostIndex = _SysTimeNetHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 1, 4, 2, 1, 1),
    _SysTimeNetHostIndex_Type()
)
sysTimeNetHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysTimeNetHostIndex.setStatus("current")
_SysTimeNetHost_Type = DisplayString
_SysTimeNetHost_Object = MibTableColumn
sysTimeNetHost = _SysTimeNetHost_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 1, 4, 2, 1, 2),
    _SysTimeNetHost_Type()
)
sysTimeNetHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeNetHost.setStatus("current")
_SysPT_ObjectIdentity = ObjectIdentity
sysPT = _SysPT_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 2)
)
_SysPTTimeout_Type = Integer32
_SysPTTimeout_Object = MibScalar
sysPTTimeout = _SysPTTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 2, 1),
    _SysPTTimeout_Type()
)
sysPTTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPTTimeout.setStatus("current")
_SysPTEndPause_Type = Integer32
_SysPTEndPause_Object = MibScalar
sysPTEndPause = _SysPTEndPause_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 2, 2),
    _SysPTEndPause_Type()
)
sysPTEndPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPTEndPause.setStatus("current")
_SysPTJoinable_Type = DisplayString
_SysPTJoinable_Object = MibScalar
sysPTJoinable = _SysPTJoinable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 2, 3),
    _SysPTJoinable_Type()
)
sysPTJoinable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPTJoinable.setStatus("current")
_SysMTU_Type = Integer32
_SysMTU_Object = MibScalar
sysMTU = _SysMTU_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 3),
    _SysMTU_Type()
)
sysMTU.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysMTU.setStatus("current")
_SysAnswerString_Type = DisplayString
_SysAnswerString_Object = MibScalar
sysAnswerString = _SysAnswerString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 4),
    _SysAnswerString_Type()
)
sysAnswerString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAnswerString.setStatus("current")
_SysEventFileID_Type = DisplayString
_SysEventFileID_Object = MibScalar
sysEventFileID = _SysEventFileID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 6),
    _SysEventFileID_Type()
)
sysEventFileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEventFileID.setStatus("current")
_SysEscapeCharacter_Type = Integer32
_SysEscapeCharacter_Object = MibScalar
sysEscapeCharacter = _SysEscapeCharacter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 7),
    _SysEscapeCharacter_Type()
)
sysEscapeCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysEscapeCharacter.setStatus("current")
_SysTimeStamp_ObjectIdentity = ObjectIdentity
sysTimeStamp = _SysTimeStamp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 8)
)
_SysTimeStampTimeFormat_Type = DisplayString
_SysTimeStampTimeFormat_Object = MibScalar
sysTimeStampTimeFormat = _SysTimeStampTimeFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 8, 1),
    _SysTimeStampTimeFormat_Type()
)
sysTimeStampTimeFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeStampTimeFormat.setStatus("current")
_SysTimeStampDateFormat_Type = DisplayString
_SysTimeStampDateFormat_Object = MibScalar
sysTimeStampDateFormat = _SysTimeStampDateFormat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 8, 2),
    _SysTimeStampDateFormat_Type()
)
sysTimeStampDateFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeStampDateFormat.setStatus("current")
_SysTimeStampSpaceAfter_Type = DisplayString
_SysTimeStampSpaceAfter_Object = MibScalar
sysTimeStampSpaceAfter = _SysTimeStampSpaceAfter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 8, 3),
    _SysTimeStampSpaceAfter_Type()
)
sysTimeStampSpaceAfter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeStampSpaceAfter.setStatus("current")
_SysLog_ObjectIdentity = ObjectIdentity
sysLog = _SysLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 9)
)
_SysLogMode_Type = DisplayString
_SysLogMode_Object = MibScalar
sysLogMode = _SysLogMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 9, 1),
    _SysLogMode_Type()
)
sysLogMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogMode.setStatus("current")
_SysLoghost_Type = DisplayString
_SysLoghost_Object = MibScalar
sysLoghost = _SysLoghost_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 9, 2),
    _SysLoghost_Type()
)
sysLoghost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLoghost.setStatus("current")
_SysLogFilter_Type = DisplayString
_SysLogFilter_Object = MibScalar
sysLogFilter = _SysLogFilter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 9, 3),
    _SysLogFilter_Type()
)
sysLogFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogFilter.setStatus("current")
_SysLogFileSize_Type = Integer32
_SysLogFileSize_Object = MibScalar
sysLogFileSize = _SysLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 9, 4),
    _SysLogFileSize_Type()
)
sysLogFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogFileSize.setStatus("current")
_SysLogFileCount_Type = Integer32
_SysLogFileCount_Object = MibScalar
sysLogFileCount = _SysLogFileCount_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 9, 5),
    _SysLogFileCount_Type()
)
sysLogFileCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogFileCount.setStatus("current")
_SysLogListenPort_Type = Integer32
_SysLogListenPort_Object = MibScalar
sysLogListenPort = _SysLogListenPort_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 9, 6),
    _SysLogListenPort_Type()
)
sysLogListenPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogListenPort.setStatus("current")
_SysCRDB_ObjectIdentity = ObjectIdentity
sysCRDB = _SysCRDB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10)
)
_SysCRDBCapacity_Type = Integer32
_SysCRDBCapacity_Object = MibScalar
sysCRDBCapacity = _SysCRDBCapacity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10, 1),
    _SysCRDBCapacity_Type()
)
sysCRDBCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRDBCapacity.setStatus("current")
_SysCRDBPercentFull_Type = Integer32
_SysCRDBPercentFull_Object = MibScalar
sysCRDBPercentFull = _SysCRDBPercentFull_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10, 2),
    _SysCRDBPercentFull_Type()
)
sysCRDBPercentFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRDBPercentFull.setStatus("current")
_SysCRDBFileIDTable_Object = MibTable
sysCRDBFileIDTable = _SysCRDBFileIDTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10, 3)
)
if mibBuilder.loadTexts:
    sysCRDBFileIDTable.setStatus("current")
_SysCRDBFileIDEntry_Object = MibTableRow
sysCRDBFileIDEntry = _SysCRDBFileIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10, 3, 1)
)
sysCRDBFileIDEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "sysCRDBFileIDIndex"),
)
if mibBuilder.loadTexts:
    sysCRDBFileIDEntry.setStatus("current")


class _SysCRDBFileIDIndex_Type(Integer32):
    """Custom type sysCRDBFileIDIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SysCRDBFileIDIndex_Type.__name__ = "Integer32"
_SysCRDBFileIDIndex_Object = MibTableColumn
sysCRDBFileIDIndex = _SysCRDBFileIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10, 3, 1, 1),
    _SysCRDBFileIDIndex_Type()
)
sysCRDBFileIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRDBFileIDIndex.setStatus("current")
_SysCRDBFileID_Type = DisplayString
_SysCRDBFileID_Object = MibTableColumn
sysCRDBFileID = _SysCRDBFileID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10, 3, 1, 2),
    _SysCRDBFileID_Type()
)
sysCRDBFileID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCRDBFileID.setStatus("current")
_SysCRDBFileEnforceMinTable_Object = MibTable
sysCRDBFileEnforceMinTable = _SysCRDBFileEnforceMinTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10, 4)
)
if mibBuilder.loadTexts:
    sysCRDBFileEnforceMinTable.setStatus("current")
_SysCRDBFileEnforceMinEntry_Object = MibTableRow
sysCRDBFileEnforceMinEntry = _SysCRDBFileEnforceMinEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10, 4, 1)
)
sysCRDBFileEnforceMinEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "sysCRDBFileEnforceMinIndex"),
)
if mibBuilder.loadTexts:
    sysCRDBFileEnforceMinEntry.setStatus("current")


class _SysCRDBFileEnforceMinIndex_Type(Integer32):
    """Custom type sysCRDBFileEnforceMinIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_SysCRDBFileEnforceMinIndex_Type.__name__ = "Integer32"
_SysCRDBFileEnforceMinIndex_Object = MibTableColumn
sysCRDBFileEnforceMinIndex = _SysCRDBFileEnforceMinIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10, 4, 1, 1),
    _SysCRDBFileEnforceMinIndex_Type()
)
sysCRDBFileEnforceMinIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysCRDBFileEnforceMinIndex.setStatus("current")
_SysCRDBFileEnforceMin_Type = DisplayString
_SysCRDBFileEnforceMin_Object = MibTableColumn
sysCRDBFileEnforceMin = _SysCRDBFileEnforceMin_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 10, 4, 1, 2),
    _SysCRDBFileEnforceMin_Type()
)
sysCRDBFileEnforceMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCRDBFileEnforceMin.setStatus("current")
_SysCharMask_Type = OctetString
_SysCharMask_Object = MibScalar
sysCharMask = _SysCharMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 11),
    _SysCharMask_Type()
)
sysCharMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCharMask.setStatus("current")
_SysPrompt_Type = DisplayString
_SysPrompt_Object = MibScalar
sysPrompt = _SysPrompt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 12),
    _SysPrompt_Type()
)
sysPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysPrompt.setStatus("current")
_SysBootStatus_Type = DisplayString
_SysBootStatus_Object = MibScalar
sysBootStatus = _SysBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 13),
    _SysBootStatus_Type()
)
sysBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysBootStatus.setStatus("current")
_SysLoc_ObjectIdentity = ObjectIdentity
sysLoc = _SysLoc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 14)
)
_SysLocLatitude_Type = DisplayString
_SysLocLatitude_Object = MibScalar
sysLocLatitude = _SysLocLatitude_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 14, 1),
    _SysLocLatitude_Type()
)
sysLocLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocLatitude.setStatus("current")
_SysLocLongitude_Type = DisplayString
_SysLocLongitude_Object = MibScalar
sysLocLongitude = _SysLocLongitude_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 14, 2),
    _SysLocLongitude_Type()
)
sysLocLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocLongitude.setStatus("current")
_SysLocXOffset_Type = DisplayString
_SysLocXOffset_Object = MibScalar
sysLocXOffset = _SysLocXOffset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 14, 3),
    _SysLocXOffset_Type()
)
sysLocXOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocXOffset.setStatus("current")
_SysLocYOffset_Type = DisplayString
_SysLocYOffset_Object = MibScalar
sysLocYOffset = _SysLocYOffset_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 14, 4),
    _SysLocYOffset_Type()
)
sysLocYOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocYOffset.setStatus("current")
_SysLocAngle_Type = DisplayString
_SysLocAngle_Object = MibScalar
sysLocAngle = _SysLocAngle_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 14, 5),
    _SysLocAngle_Type()
)
sysLocAngle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocAngle.setStatus("current")
_SysLocAltitude_Type = DisplayString
_SysLocAltitude_Object = MibScalar
sysLocAltitude = _SysLocAltitude_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 14, 6),
    _SysLocAltitude_Type()
)
sysLocAltitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLocAltitude.setStatus("current")
_SysSleep_ObjectIdentity = ObjectIdentity
sysSleep = _SysSleep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16)
)
_SysSleepEnable_Type = DisplayString
_SysSleepEnable_Object = MibScalar
sysSleepEnable = _SysSleepEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 1),
    _SysSleepEnable_Type()
)
sysSleepEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepEnable.setStatus("current")
_SysSleepSleep_ObjectIdentity = ObjectIdentity
sysSleepSleep = _SysSleepSleep_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 2)
)
_SysSleepForceSleep_Type = DisplayString
_SysSleepForceSleep_Object = MibScalar
sysSleepForceSleep = _SysSleepForceSleep_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 2, 1),
    _SysSleepForceSleep_Type()
)
sysSleepForceSleep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepForceSleep.setStatus("current")


class _SysSleepSleepTimer_Type(Integer32):
    """Custom type sysSleepSleepTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 240),
    )


_SysSleepSleepTimer_Type.__name__ = "Integer32"
_SysSleepSleepTimer_Object = MibScalar
sysSleepSleepTimer = _SysSleepSleepTimer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 2, 2),
    _SysSleepSleepTimer_Type()
)
sysSleepSleepTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepSleepTimer.setStatus("current")
_SysSleepWake_ObjectIdentity = ObjectIdentity
sysSleepWake = _SysSleepWake_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 3)
)


class _SysSleepWakeTimerNormal_Type(Integer32):
    """Custom type sysSleepWakeTimerNormal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10800),
    )


_SysSleepWakeTimerNormal_Type.__name__ = "Integer32"
_SysSleepWakeTimerNormal_Object = MibScalar
sysSleepWakeTimerNormal = _SysSleepWakeTimerNormal_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 3, 1),
    _SysSleepWakeTimerNormal_Type()
)
sysSleepWakeTimerNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepWakeTimerNormal.setStatus("current")


class _SysSleepWakeTimerMotion_Type(Integer32):
    """Custom type sysSleepWakeTimerMotion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10800),
    )


_SysSleepWakeTimerMotion_Type.__name__ = "Integer32"
_SysSleepWakeTimerMotion_Object = MibScalar
sysSleepWakeTimerMotion = _SysSleepWakeTimerMotion_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 3, 2),
    _SysSleepWakeTimerMotion_Type()
)
sysSleepWakeTimerMotion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepWakeTimerMotion.setStatus("current")
_SysSleepWakeMotionEnable_Type = DisplayString
_SysSleepWakeMotionEnable_Object = MibScalar
sysSleepWakeMotionEnable = _SysSleepWakeMotionEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 3, 3),
    _SysSleepWakeMotionEnable_Type()
)
sysSleepWakeMotionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepWakeMotionEnable.setStatus("current")
_SysSleepWakeScheduledEnable_Type = DisplayString
_SysSleepWakeScheduledEnable_Object = MibScalar
sysSleepWakeScheduledEnable = _SysSleepWakeScheduledEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 3, 4),
    _SysSleepWakeScheduledEnable_Type()
)
sysSleepWakeScheduledEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepWakeScheduledEnable.setStatus("current")
_SysSleepWakeScheduledTimeOfDay_Type = DisplayString
_SysSleepWakeScheduledTimeOfDay_Object = MibScalar
sysSleepWakeScheduledTimeOfDay = _SysSleepWakeScheduledTimeOfDay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 3, 5),
    _SysSleepWakeScheduledTimeOfDay_Type()
)
sysSleepWakeScheduledTimeOfDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepWakeScheduledTimeOfDay.setStatus("current")
_SysSleepPowerDetectCC_ObjectIdentity = ObjectIdentity
sysSleepPowerDetectCC = _SysSleepPowerDetectCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 4)
)
_SysSleepPowerDetectCCEnable_Type = DisplayString
_SysSleepPowerDetectCCEnable_Object = MibScalar
sysSleepPowerDetectCCEnable = _SysSleepPowerDetectCCEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 4, 1),
    _SysSleepPowerDetectCCEnable_Type()
)
sysSleepPowerDetectCCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepPowerDetectCCEnable.setStatus("current")
_SysSleepPowerDetectCCPowerOnState_Type = DisplayString
_SysSleepPowerDetectCCPowerOnState_Object = MibScalar
sysSleepPowerDetectCCPowerOnState = _SysSleepPowerDetectCCPowerOnState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 4, 2),
    _SysSleepPowerDetectCCPowerOnState_Type()
)
sysSleepPowerDetectCCPowerOnState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepPowerDetectCCPowerOnState.setStatus("current")


class _SysSleepPowerDetectCCThreshold_Type(Integer32):
    """Custom type sysSleepPowerDetectCCThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SysSleepPowerDetectCCThreshold_Type.__name__ = "Integer32"
_SysSleepPowerDetectCCThreshold_Object = MibScalar
sysSleepPowerDetectCCThreshold = _SysSleepPowerDetectCCThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 16, 4, 3),
    _SysSleepPowerDetectCCThreshold_Type()
)
sysSleepPowerDetectCCThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSleepPowerDetectCCThreshold.setStatus("current")
_SysFileTransfer_ObjectIdentity = ObjectIdentity
sysFileTransfer = _SysFileTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 17)
)
_SysFileTransferStatus_Type = DisplayString
_SysFileTransferStatus_Object = MibScalar
sysFileTransferStatus = _SysFileTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 17, 1),
    _SysFileTransferStatus_Type()
)
sysFileTransferStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFileTransferStatus.setStatus("current")
_SysFileTransferURL_Type = DisplayString
_SysFileTransferURL_Object = MibScalar
sysFileTransferURL = _SysFileTransferURL_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 17, 2),
    _SysFileTransferURL_Type()
)
sysFileTransferURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFileTransferURL.setStatus("current")
_SysFileTransferUsername_Type = DisplayString
_SysFileTransferUsername_Object = MibScalar
sysFileTransferUsername = _SysFileTransferUsername_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 17, 3),
    _SysFileTransferUsername_Type()
)
sysFileTransferUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFileTransferUsername.setStatus("current")
_SysFileTransferPassword_Type = DisplayString
_SysFileTransferPassword_Object = MibScalar
sysFileTransferPassword = _SysFileTransferPassword_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 17, 4),
    _SysFileTransferPassword_Type()
)
sysFileTransferPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysFileTransferPassword.setStatus("current")
_SysUpdate_ObjectIdentity = ObjectIdentity
sysUpdate = _SysUpdate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 18)
)
_SysUpdateStatus_Type = DisplayString
_SysUpdateStatus_Object = MibScalar
sysUpdateStatus = _SysUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 16, 18, 1),
    _SysUpdateStatus_Type()
)
sysUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysUpdateStatus.setStatus("current")
_AuditLog_ObjectIdentity = ObjectIdentity
auditLog = _AuditLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17)
)
_AuditLogEnable_Type = DisplayString
_AuditLogEnable_Object = MibScalar
auditLogEnable = _AuditLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 1),
    _AuditLogEnable_Type()
)
auditLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogEnable.setStatus("current")
_AuditLogStoreResets_Type = DisplayString
_AuditLogStoreResets_Object = MibScalar
auditLogStoreResets = _AuditLogStoreResets_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 2),
    _AuditLogStoreResets_Type()
)
auditLogStoreResets.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreResets.setStatus("current")
_AuditLogStoreCommands_Type = DisplayString
_AuditLogStoreCommands_Object = MibScalar
auditLogStoreCommands = _AuditLogStoreCommands_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 3),
    _AuditLogStoreCommands_Type()
)
auditLogStoreCommands.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreCommands.setStatus("current")
_AuditLogStoreOutputs_Type = DisplayString
_AuditLogStoreOutputs_Object = MibScalar
auditLogStoreOutputs = _AuditLogStoreOutputs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 4),
    _AuditLogStoreOutputs_Type()
)
auditLogStoreOutputs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreOutputs.setStatus("current")
_AuditLogStoreAlarmActions_Type = DisplayString
_AuditLogStoreAlarmActions_Object = MibScalar
auditLogStoreAlarmActions = _AuditLogStoreAlarmActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 5),
    _AuditLogStoreAlarmActions_Type()
)
auditLogStoreAlarmActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreAlarmActions.setStatus("current")
_AuditLogStorePwdFailures_Type = DisplayString
_AuditLogStorePwdFailures_Object = MibScalar
auditLogStorePwdFailures = _AuditLogStorePwdFailures_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 6),
    _AuditLogStorePwdFailures_Type()
)
auditLogStorePwdFailures.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStorePwdFailures.setStatus("current")
_AuditLogStoreLogins_Type = DisplayString
_AuditLogStoreLogins_Object = MibScalar
auditLogStoreLogins = _AuditLogStoreLogins_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 7),
    _AuditLogStoreLogins_Type()
)
auditLogStoreLogins.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreLogins.setStatus("current")
_AuditLogStoreSHSK_Type = DisplayString
_AuditLogStoreSHSK_Object = MibScalar
auditLogStoreSHSK = _AuditLogStoreSHSK_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 8),
    _AuditLogStoreSHSK_Type()
)
auditLogStoreSHSK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreSHSK.setStatus("current")
_AuditLogStorePassthrough_Type = DisplayString
_AuditLogStorePassthrough_Object = MibScalar
auditLogStorePassthrough = _AuditLogStorePassthrough_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 9),
    _AuditLogStorePassthrough_Type()
)
auditLogStorePassthrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStorePassthrough.setStatus("current")
_AuditLogStoreInactivity_Type = DisplayString
_AuditLogStoreInactivity_Object = MibScalar
auditLogStoreInactivity = _AuditLogStoreInactivity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 10),
    _AuditLogStoreInactivity_Type()
)
auditLogStoreInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStoreInactivity.setStatus("current")
_AuditLogStorePolling_Type = DisplayString
_AuditLogStorePolling_Object = MibScalar
auditLogStorePolling = _AuditLogStorePolling_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 11),
    _AuditLogStorePolling_Type()
)
auditLogStorePolling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogStorePolling.setStatus("current")
_AuditLogMaxSize_Type = Integer32
_AuditLogMaxSize_Object = MibScalar
auditLogMaxSize = _AuditLogMaxSize_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 12),
    _AuditLogMaxSize_Type()
)
auditLogMaxSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogMaxSize.setStatus("current")
_AuditLogSoreSleepActivity_Type = DisplayString
_AuditLogSoreSleepActivity_Object = MibScalar
auditLogSoreSleepActivity = _AuditLogSoreSleepActivity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 17, 13),
    _AuditLogSoreSleepActivity_Type()
)
auditLogSoreSleepActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    auditLogSoreSleepActivity.setStatus("current")
_Scripting_ObjectIdentity = ObjectIdentity
scripting = _Scripting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18)
)
_ScrGlobalEnable_Type = DisplayString
_ScrGlobalEnable_Object = MibScalar
scrGlobalEnable = _ScrGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 1),
    _ScrGlobalEnable_Type()
)
scrGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrGlobalEnable.setStatus("current")
_ScrDTRCtrlPortEnableTable_Object = MibTable
scrDTRCtrlPortEnableTable = _ScrDTRCtrlPortEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 2)
)
if mibBuilder.loadTexts:
    scrDTRCtrlPortEnableTable.setStatus("current")
_ScrDTRCtrlPortEnableEntry_Object = MibTableRow
scrDTRCtrlPortEnableEntry = _ScrDTRCtrlPortEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 2, 1)
)
scrDTRCtrlPortEnableEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "scrDTRCtrlPortEnableIndex"),
)
if mibBuilder.loadTexts:
    scrDTRCtrlPortEnableEntry.setStatus("current")


class _ScrDTRCtrlPortEnableIndex_Type(Integer32):
    """Custom type scrDTRCtrlPortEnableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_ScrDTRCtrlPortEnableIndex_Type.__name__ = "Integer32"
_ScrDTRCtrlPortEnableIndex_Object = MibTableColumn
scrDTRCtrlPortEnableIndex = _ScrDTRCtrlPortEnableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 2, 1, 1),
    _ScrDTRCtrlPortEnableIndex_Type()
)
scrDTRCtrlPortEnableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrDTRCtrlPortEnableIndex.setStatus("current")
_ScrDTRCtrlPortEnable_Type = DisplayString
_ScrDTRCtrlPortEnable_Object = MibTableColumn
scrDTRCtrlPortEnable = _ScrDTRCtrlPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 2, 1, 2),
    _ScrDTRCtrlPortEnable_Type()
)
scrDTRCtrlPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrDTRCtrlPortEnable.setStatus("current")
_ScrTable_Object = MibTable
scrTable = _ScrTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3)
)
if mibBuilder.loadTexts:
    scrTable.setStatus("current")
_ScrEntry_Object = MibTableRow
scrEntry = _ScrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1)
)
scrEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "scrIndex"),
)
if mibBuilder.loadTexts:
    scrEntry.setStatus("current")


class _ScrIndex_Type(Integer32):
    """Custom type scrIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_ScrIndex_Type.__name__ = "Integer32"
_ScrIndex_Object = MibTableColumn
scrIndex = _ScrIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1, 1),
    _ScrIndex_Type()
)
scrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrIndex.setStatus("current")
_ScrEnable_Type = DisplayString
_ScrEnable_Object = MibTableColumn
scrEnable = _ScrEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1, 2),
    _ScrEnable_Type()
)
scrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrEnable.setStatus("current")
_ScrName_Type = DisplayString
_ScrName_Object = MibTableColumn
scrName = _ScrName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1, 3),
    _ScrName_Type()
)
scrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrName.setStatus("current")
_ScrFilename_Type = DisplayString
_ScrFilename_Object = MibTableColumn
scrFilename = _ScrFilename_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1, 4),
    _ScrFilename_Type()
)
scrFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrFilename.setStatus("current")
_ScrRunAlways_Type = DisplayString
_ScrRunAlways_Object = MibTableColumn
scrRunAlways = _ScrRunAlways_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1, 5),
    _ScrRunAlways_Type()
)
scrRunAlways.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrRunAlways.setStatus("current")
_ScrRunAtStartup_Type = DisplayString
_ScrRunAtStartup_Object = MibTableColumn
scrRunAtStartup = _ScrRunAtStartup_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1, 6),
    _ScrRunAtStartup_Type()
)
scrRunAtStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrRunAtStartup.setStatus("current")
_ScrRunScheduled_Type = DisplayString
_ScrRunScheduled_Object = MibTableColumn
scrRunScheduled = _ScrRunScheduled_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1, 7),
    _ScrRunScheduled_Type()
)
scrRunScheduled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrRunScheduled.setStatus("current")
_ScrScheduleTime_Type = DisplayString
_ScrScheduleTime_Object = MibTableColumn
scrScheduleTime = _ScrScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1, 8),
    _ScrScheduleTime_Type()
)
scrScheduleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrScheduleTime.setStatus("current")
_ScrArguments_Type = DisplayString
_ScrArguments_Object = MibTableColumn
scrArguments = _ScrArguments_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1, 9),
    _ScrArguments_Type()
)
scrArguments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrArguments.setStatus("current")
_ScrRepeatInterval_Type = Integer32
_ScrRepeatInterval_Object = MibTableColumn
scrRepeatInterval = _ScrRepeatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 3, 1, 10),
    _ScrRepeatInterval_Type()
)
scrRepeatInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrRepeatInterval.setStatus("current")
_ScrVolatileStringTable_Object = MibTable
scrVolatileStringTable = _ScrVolatileStringTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 4)
)
if mibBuilder.loadTexts:
    scrVolatileStringTable.setStatus("current")
_ScrVolatileStringEntry_Object = MibTableRow
scrVolatileStringEntry = _ScrVolatileStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 4, 1)
)
scrVolatileStringEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "scrVolatileStringIndex"),
)
if mibBuilder.loadTexts:
    scrVolatileStringEntry.setStatus("current")


class _ScrVolatileStringIndex_Type(Integer32):
    """Custom type scrVolatileStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ScrVolatileStringIndex_Type.__name__ = "Integer32"
_ScrVolatileStringIndex_Object = MibTableColumn
scrVolatileStringIndex = _ScrVolatileStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 4, 1, 1),
    _ScrVolatileStringIndex_Type()
)
scrVolatileStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrVolatileStringIndex.setStatus("current")
_ScrVolatileString_Type = DisplayString
_ScrVolatileString_Object = MibTableColumn
scrVolatileString = _ScrVolatileString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 4, 1, 2),
    _ScrVolatileString_Type()
)
scrVolatileString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrVolatileString.setStatus("current")
_ScrVolatileIntTable_Object = MibTable
scrVolatileIntTable = _ScrVolatileIntTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 5)
)
if mibBuilder.loadTexts:
    scrVolatileIntTable.setStatus("current")
_ScrVolatileIntEntry_Object = MibTableRow
scrVolatileIntEntry = _ScrVolatileIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 5, 1)
)
scrVolatileIntEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "scrVolatileIntIndex"),
)
if mibBuilder.loadTexts:
    scrVolatileIntEntry.setStatus("current")


class _ScrVolatileIntIndex_Type(Integer32):
    """Custom type scrVolatileIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ScrVolatileIntIndex_Type.__name__ = "Integer32"
_ScrVolatileIntIndex_Object = MibTableColumn
scrVolatileIntIndex = _ScrVolatileIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 5, 1, 1),
    _ScrVolatileIntIndex_Type()
)
scrVolatileIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrVolatileIntIndex.setStatus("current")


class _ScrVolatileInt_Type(Integer32):
    """Custom type scrVolatileInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ScrVolatileInt_Type.__name__ = "Integer32"
_ScrVolatileInt_Object = MibTableColumn
scrVolatileInt = _ScrVolatileInt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 5, 1, 2),
    _ScrVolatileInt_Type()
)
scrVolatileInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrVolatileInt.setStatus("current")
_ScrNonVolatileStringTable_Object = MibTable
scrNonVolatileStringTable = _ScrNonVolatileStringTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 6)
)
if mibBuilder.loadTexts:
    scrNonVolatileStringTable.setStatus("current")
_ScrNonVolatileStringEntry_Object = MibTableRow
scrNonVolatileStringEntry = _ScrNonVolatileStringEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 6, 1)
)
scrNonVolatileStringEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "scrNonVolatileStringIndex"),
)
if mibBuilder.loadTexts:
    scrNonVolatileStringEntry.setStatus("current")


class _ScrNonVolatileStringIndex_Type(Integer32):
    """Custom type scrNonVolatileStringIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ScrNonVolatileStringIndex_Type.__name__ = "Integer32"
_ScrNonVolatileStringIndex_Object = MibTableColumn
scrNonVolatileStringIndex = _ScrNonVolatileStringIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 6, 1, 1),
    _ScrNonVolatileStringIndex_Type()
)
scrNonVolatileStringIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrNonVolatileStringIndex.setStatus("current")
_ScrNonVolatileString_Type = DisplayString
_ScrNonVolatileString_Object = MibTableColumn
scrNonVolatileString = _ScrNonVolatileString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 6, 1, 2),
    _ScrNonVolatileString_Type()
)
scrNonVolatileString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrNonVolatileString.setStatus("current")
_ScrNonVolatileIntTable_Object = MibTable
scrNonVolatileIntTable = _ScrNonVolatileIntTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 7)
)
if mibBuilder.loadTexts:
    scrNonVolatileIntTable.setStatus("current")
_ScrNonVolatileIntEntry_Object = MibTableRow
scrNonVolatileIntEntry = _ScrNonVolatileIntEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 7, 1)
)
scrNonVolatileIntEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "scrNonVolatileIntIndex"),
)
if mibBuilder.loadTexts:
    scrNonVolatileIntEntry.setStatus("current")


class _ScrNonVolatileIntIndex_Type(Integer32):
    """Custom type scrNonVolatileIntIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_ScrNonVolatileIntIndex_Type.__name__ = "Integer32"
_ScrNonVolatileIntIndex_Object = MibTableColumn
scrNonVolatileIntIndex = _ScrNonVolatileIntIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 7, 1, 1),
    _ScrNonVolatileIntIndex_Type()
)
scrNonVolatileIntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    scrNonVolatileIntIndex.setStatus("current")


class _ScrNonVolatileInt_Type(Integer32):
    """Custom type scrNonVolatileInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ScrNonVolatileInt_Type.__name__ = "Integer32"
_ScrNonVolatileInt_Object = MibTableColumn
scrNonVolatileInt = _ScrNonVolatileInt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 18, 7, 1, 2),
    _ScrNonVolatileInt_Type()
)
scrNonVolatileInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scrNonVolatileInt.setStatus("current")
_Generator_ObjectIdentity = ObjectIdentity
generator = _Generator_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19)
)
_GenSet_ObjectIdentity = ObjectIdentity
genSet = _GenSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1)
)
_GenSetEnable_Type = DisplayString
_GenSetEnable_Object = MibScalar
genSetEnable = _GenSetEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 1),
    _GenSetEnable_Type()
)
genSetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetEnable.setStatus("current")
_GenSetRelay_ObjectIdentity = ObjectIdentity
genSetRelay = _GenSetRelay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2)
)


class _GenSetRelayEs_Type(Integer32):
    """Custom type genSetRelayEs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_GenSetRelayEs_Type.__name__ = "Integer32"
_GenSetRelayEs_Object = MibScalar
genSetRelayEs = _GenSetRelayEs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2, 1),
    _GenSetRelayEs_Type()
)
genSetRelayEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetRelayEs.setStatus("current")


class _GenSetRelayPoint_Type(Integer32):
    """Custom type genSetRelayPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_GenSetRelayPoint_Type.__name__ = "Integer32"
_GenSetRelayPoint_Object = MibScalar
genSetRelayPoint = _GenSetRelayPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2, 2),
    _GenSetRelayPoint_Type()
)
genSetRelayPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetRelayPoint.setStatus("current")
_GenSetRelayRunningstate_Type = DisplayString
_GenSetRelayRunningstate_Object = MibScalar
genSetRelayRunningstate = _GenSetRelayRunningstate_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2, 3),
    _GenSetRelayRunningstate_Type()
)
genSetRelayRunningstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetRelayRunningstate.setStatus("current")
_GenSetRelayTable_Object = MibTable
genSetRelayTable = _GenSetRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2, 5)
)
if mibBuilder.loadTexts:
    genSetRelayTable.setStatus("current")
_GenSetRelayTableEntry_Object = MibTableRow
genSetRelayTableEntry = _GenSetRelayTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2, 5, 1)
)
genSetRelayTableEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "genSetRelayTableIndex"),
)
if mibBuilder.loadTexts:
    genSetRelayTableEntry.setStatus("current")


class _GenSetRelayTableIndex_Type(Integer32):
    """Custom type genSetRelayTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_GenSetRelayTableIndex_Type.__name__ = "Integer32"
_GenSetRelayTableIndex_Object = MibTableColumn
genSetRelayTableIndex = _GenSetRelayTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2, 5, 1, 1),
    _GenSetRelayTableIndex_Type()
)
genSetRelayTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genSetRelayTableIndex.setStatus("current")
_GenSetRelayTableEnable_Type = DisplayString
_GenSetRelayTableEnable_Object = MibTableColumn
genSetRelayTableEnable = _GenSetRelayTableEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2, 5, 1, 2),
    _GenSetRelayTableEnable_Type()
)
genSetRelayTableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetRelayTableEnable.setStatus("current")


class _GenSetRelayTableEs_Type(Integer32):
    """Custom type genSetRelayTableEs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_GenSetRelayTableEs_Type.__name__ = "Integer32"
_GenSetRelayTableEs_Object = MibTableColumn
genSetRelayTableEs = _GenSetRelayTableEs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2, 5, 1, 3),
    _GenSetRelayTableEs_Type()
)
genSetRelayTableEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetRelayTableEs.setStatus("current")


class _GenSetRelayTablePoint_Type(Integer32):
    """Custom type genSetRelayTablePoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 13),
    )


_GenSetRelayTablePoint_Type.__name__ = "Integer32"
_GenSetRelayTablePoint_Object = MibTableColumn
genSetRelayTablePoint = _GenSetRelayTablePoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2, 5, 1, 4),
    _GenSetRelayTablePoint_Type()
)
genSetRelayTablePoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetRelayTablePoint.setStatus("current")
_GenSetRelayTableRunningstate_Type = DisplayString
_GenSetRelayTableRunningstate_Object = MibTableColumn
genSetRelayTableRunningstate = _GenSetRelayTableRunningstate_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 2, 5, 1, 5),
    _GenSetRelayTableRunningstate_Type()
)
genSetRelayTableRunningstate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetRelayTableRunningstate.setStatus("current")
_GenSetCC_ObjectIdentity = ObjectIdentity
genSetCC = _GenSetCC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 3)
)
_GenSetCCEnable_Type = DisplayString
_GenSetCCEnable_Object = MibScalar
genSetCCEnable = _GenSetCCEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 3, 1),
    _GenSetCCEnable_Type()
)
genSetCCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetCCEnable.setStatus("current")


class _GenSetCCEs_Type(Integer32):
    """Custom type genSetCCEs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_GenSetCCEs_Type.__name__ = "Integer32"
_GenSetCCEs_Object = MibScalar
genSetCCEs = _GenSetCCEs_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 3, 2),
    _GenSetCCEs_Type()
)
genSetCCEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetCCEs.setStatus("current")


class _GenSetCCPoint_Type(Integer32):
    """Custom type genSetCCPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_GenSetCCPoint_Type.__name__ = "Integer32"
_GenSetCCPoint_Object = MibScalar
genSetCCPoint = _GenSetCCPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 3, 3),
    _GenSetCCPoint_Type()
)
genSetCCPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetCCPoint.setStatus("current")
_GenSetCCRunningState_Type = DisplayString
_GenSetCCRunningState_Object = MibScalar
genSetCCRunningState = _GenSetCCRunningState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 3, 4),
    _GenSetCCRunningState_Type()
)
genSetCCRunningState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetCCRunningState.setStatus("current")


class _GenSetCCDelay_Type(Integer32):
    """Custom type genSetCCDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_GenSetCCDelay_Type.__name__ = "Integer32"
_GenSetCCDelay_Object = MibScalar
genSetCCDelay = _GenSetCCDelay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 1, 3, 5),
    _GenSetCCDelay_Type()
)
genSetCCDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genSetCCDelay.setStatus("current")
_GenRun_ObjectIdentity = ObjectIdentity
genRun = _GenRun_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2)
)
_GenRunMode_Type = DisplayString
_GenRunMode_Object = MibScalar
genRunMode = _GenRunMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 1),
    _GenRunMode_Type()
)
genRunMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRunMode.setStatus("current")
_GenRunSched_Type = DisplayString
_GenRunSched_Object = MibScalar
genRunSched = _GenRunSched_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 2),
    _GenRunSched_Type()
)
genRunSched.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRunSched.setStatus("current")


class _GenRunDuration_Type(Integer32):
    """Custom type genRunDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 3600),
    )


_GenRunDuration_Type.__name__ = "Integer32"
_GenRunDuration_Object = MibScalar
genRunDuration = _GenRunDuration_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 3),
    _GenRunDuration_Type()
)
genRunDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRunDuration.setStatus("current")


class _GenRunForce_Type(Integer32):
    """Custom type genRunForce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_GenRunForce_Type.__name__ = "Integer32"
_GenRunForce_Object = MibScalar
genRunForce = _GenRunForce_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 4),
    _GenRunForce_Type()
)
genRunForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRunForce.setStatus("current")
_GenRunReqasm_Type = DisplayString
_GenRunReqasm_Object = MibScalar
genRunReqasm = _GenRunReqasm_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 5),
    _GenRunReqasm_Type()
)
genRunReqasm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRunReqasm.setStatus("current")
_GenRunStatus_Type = DisplayString
_GenRunStatus_Object = MibScalar
genRunStatus = _GenRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 6),
    _GenRunStatus_Type()
)
genRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    genRunStatus.setStatus("current")
_GenRunNonstartEvent_ObjectIdentity = ObjectIdentity
genRunNonstartEvent = _GenRunNonstartEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 7)
)
_GenRunNonstartEventEnable_Type = DisplayString
_GenRunNonstartEventEnable_Object = MibScalar
genRunNonstartEventEnable = _GenRunNonstartEventEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 7, 1),
    _GenRunNonstartEventEnable_Type()
)
genRunNonstartEventEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRunNonstartEventEnable.setStatus("current")
_GenRunNonstartEventActions_Type = DisplayString
_GenRunNonstartEventActions_Object = MibScalar
genRunNonstartEventActions = _GenRunNonstartEventActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 7, 2),
    _GenRunNonstartEventActions_Type()
)
genRunNonstartEventActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRunNonstartEventActions.setStatus("current")


class _GenRunNonstartEventTrap_Type(Integer32):
    """Custom type genRunNonstartEventTrap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(536, 1199),
    )


_GenRunNonstartEventTrap_Type.__name__ = "Integer32"
_GenRunNonstartEventTrap_Object = MibScalar
genRunNonstartEventTrap = _GenRunNonstartEventTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 7, 3),
    _GenRunNonstartEventTrap_Type()
)
genRunNonstartEventTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRunNonstartEventTrap.setStatus("current")
_GenRunNonstartEventClass_Type = DisplayString
_GenRunNonstartEventClass_Object = MibScalar
genRunNonstartEventClass = _GenRunNonstartEventClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 19, 2, 7, 4),
    _GenRunNonstartEventClass_Type()
)
genRunNonstartEventClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    genRunNonstartEventClass.setStatus("current")
_Calendar_ObjectIdentity = ObjectIdentity
calendar = _Calendar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20)
)
_SchedTable_Object = MibTable
schedTable = _SchedTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1)
)
if mibBuilder.loadTexts:
    schedTable.setStatus("current")
_SchedEntry_Object = MibTableRow
schedEntry = _SchedEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1)
)
schedEntry.setIndexNames(
    (0, "SITEBOSS-350-STD-MIB", "schedIndex"),
)
if mibBuilder.loadTexts:
    schedEntry.setStatus("current")


class _SchedIndex_Type(Integer32):
    """Custom type schedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_SchedIndex_Type.__name__ = "Integer32"
_SchedIndex_Object = MibTableColumn
schedIndex = _SchedIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 1),
    _SchedIndex_Type()
)
schedIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedIndex.setStatus("current")
_SchedEnable_Type = DisplayString
_SchedEnable_Object = MibTableColumn
schedEnable = _SchedEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 2),
    _SchedEnable_Type()
)
schedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedEnable.setStatus("current")
_SchedStart_Type = DisplayString
_SchedStart_Object = MibTableColumn
schedStart = _SchedStart_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 3),
    _SchedStart_Type()
)
schedStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedStart.setStatus("current")
_SchedRepeatMode_Type = DisplayString
_SchedRepeatMode_Object = MibTableColumn
schedRepeatMode = _SchedRepeatMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 4),
    _SchedRepeatMode_Type()
)
schedRepeatMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatMode.setStatus("current")


class _SchedRepeatFreq_Type(Integer32):
    """Custom type schedRepeatFreq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 400),
    )


_SchedRepeatFreq_Type.__name__ = "Integer32"
_SchedRepeatFreq_Object = MibTableColumn
schedRepeatFreq = _SchedRepeatFreq_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 5),
    _SchedRepeatFreq_Type()
)
schedRepeatFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatFreq.setStatus("current")
_SchedRepeatEndMode_Type = DisplayString
_SchedRepeatEndMode_Object = MibTableColumn
schedRepeatEndMode = _SchedRepeatEndMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 6),
    _SchedRepeatEndMode_Type()
)
schedRepeatEndMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatEndMode.setStatus("current")


class _SchedRepeatEndAfter_Type(Integer32):
    """Custom type schedRepeatEndAfter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_SchedRepeatEndAfter_Type.__name__ = "Integer32"
_SchedRepeatEndAfter_Object = MibTableColumn
schedRepeatEndAfter = _SchedRepeatEndAfter_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 7),
    _SchedRepeatEndAfter_Type()
)
schedRepeatEndAfter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatEndAfter.setStatus("current")
_SchedRepeatEndOn_Type = DisplayString
_SchedRepeatEndOn_Object = MibTableColumn
schedRepeatEndOn = _SchedRepeatEndOn_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 8),
    _SchedRepeatEndOn_Type()
)
schedRepeatEndOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatEndOn.setStatus("current")
_SchedRepeatWeeklySun_Type = DisplayString
_SchedRepeatWeeklySun_Object = MibTableColumn
schedRepeatWeeklySun = _SchedRepeatWeeklySun_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 9),
    _SchedRepeatWeeklySun_Type()
)
schedRepeatWeeklySun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatWeeklySun.setStatus("current")
_SchedRepeatWeeklyMon_Type = DisplayString
_SchedRepeatWeeklyMon_Object = MibTableColumn
schedRepeatWeeklyMon = _SchedRepeatWeeklyMon_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 10),
    _SchedRepeatWeeklyMon_Type()
)
schedRepeatWeeklyMon.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatWeeklyMon.setStatus("current")
_SchedRepeatWeeklyTue_Type = DisplayString
_SchedRepeatWeeklyTue_Object = MibTableColumn
schedRepeatWeeklyTue = _SchedRepeatWeeklyTue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 11),
    _SchedRepeatWeeklyTue_Type()
)
schedRepeatWeeklyTue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatWeeklyTue.setStatus("current")
_SchedRepeatWeeklyWed_Type = DisplayString
_SchedRepeatWeeklyWed_Object = MibTableColumn
schedRepeatWeeklyWed = _SchedRepeatWeeklyWed_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 12),
    _SchedRepeatWeeklyWed_Type()
)
schedRepeatWeeklyWed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatWeeklyWed.setStatus("current")
_SchedRepeatWeeklyThu_Type = DisplayString
_SchedRepeatWeeklyThu_Object = MibTableColumn
schedRepeatWeeklyThu = _SchedRepeatWeeklyThu_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 13),
    _SchedRepeatWeeklyThu_Type()
)
schedRepeatWeeklyThu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatWeeklyThu.setStatus("current")
_SchedRepeatWeeklyFri_Type = DisplayString
_SchedRepeatWeeklyFri_Object = MibTableColumn
schedRepeatWeeklyFri = _SchedRepeatWeeklyFri_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 14),
    _SchedRepeatWeeklyFri_Type()
)
schedRepeatWeeklyFri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatWeeklyFri.setStatus("current")
_SchedRepeatWeeklySat_Type = DisplayString
_SchedRepeatWeeklySat_Object = MibTableColumn
schedRepeatWeeklySat = _SchedRepeatWeeklySat_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 15),
    _SchedRepeatWeeklySat_Type()
)
schedRepeatWeeklySat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatWeeklySat.setStatus("current")
_SchedRepeatMonthlyMode_Type = DisplayString
_SchedRepeatMonthlyMode_Object = MibTableColumn
schedRepeatMonthlyMode = _SchedRepeatMonthlyMode_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 16),
    _SchedRepeatMonthlyMode_Type()
)
schedRepeatMonthlyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatMonthlyMode.setStatus("current")
_SchedRepeatMonthlyDates_Type = DisplayString
_SchedRepeatMonthlyDates_Object = MibTableColumn
schedRepeatMonthlyDates = _SchedRepeatMonthlyDates_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 17),
    _SchedRepeatMonthlyDates_Type()
)
schedRepeatMonthlyDates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatMonthlyDates.setStatus("current")
_SchedRepeatMonthlyOnThe_Type = DisplayString
_SchedRepeatMonthlyOnThe_Object = MibTableColumn
schedRepeatMonthlyOnThe = _SchedRepeatMonthlyOnThe_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 18),
    _SchedRepeatMonthlyOnThe_Type()
)
schedRepeatMonthlyOnThe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatMonthlyOnThe.setStatus("current")
_SchedRepeatMonthlyOnDay_Type = DisplayString
_SchedRepeatMonthlyOnDay_Object = MibTableColumn
schedRepeatMonthlyOnDay = _SchedRepeatMonthlyOnDay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 19),
    _SchedRepeatMonthlyOnDay_Type()
)
schedRepeatMonthlyOnDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatMonthlyOnDay.setStatus("current")
_SchedRepeatYearlyJan_Type = DisplayString
_SchedRepeatYearlyJan_Object = MibTableColumn
schedRepeatYearlyJan = _SchedRepeatYearlyJan_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 20),
    _SchedRepeatYearlyJan_Type()
)
schedRepeatYearlyJan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyJan.setStatus("current")
_SchedRepeatYearlyFeb_Type = DisplayString
_SchedRepeatYearlyFeb_Object = MibTableColumn
schedRepeatYearlyFeb = _SchedRepeatYearlyFeb_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 21),
    _SchedRepeatYearlyFeb_Type()
)
schedRepeatYearlyFeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyFeb.setStatus("current")
_SchedRepeatYearlyMar_Type = DisplayString
_SchedRepeatYearlyMar_Object = MibTableColumn
schedRepeatYearlyMar = _SchedRepeatYearlyMar_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 22),
    _SchedRepeatYearlyMar_Type()
)
schedRepeatYearlyMar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyMar.setStatus("current")
_SchedRepeatYearlyApr_Type = DisplayString
_SchedRepeatYearlyApr_Object = MibTableColumn
schedRepeatYearlyApr = _SchedRepeatYearlyApr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 23),
    _SchedRepeatYearlyApr_Type()
)
schedRepeatYearlyApr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyApr.setStatus("current")
_SchedRepeatYearlyMay_Type = DisplayString
_SchedRepeatYearlyMay_Object = MibTableColumn
schedRepeatYearlyMay = _SchedRepeatYearlyMay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 24),
    _SchedRepeatYearlyMay_Type()
)
schedRepeatYearlyMay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyMay.setStatus("current")
_SchedRepeatYearlyJun_Type = DisplayString
_SchedRepeatYearlyJun_Object = MibTableColumn
schedRepeatYearlyJun = _SchedRepeatYearlyJun_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 25),
    _SchedRepeatYearlyJun_Type()
)
schedRepeatYearlyJun.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyJun.setStatus("current")
_SchedRepeatYearlyJul_Type = DisplayString
_SchedRepeatYearlyJul_Object = MibTableColumn
schedRepeatYearlyJul = _SchedRepeatYearlyJul_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 26),
    _SchedRepeatYearlyJul_Type()
)
schedRepeatYearlyJul.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyJul.setStatus("current")
_SchedRepeatYearlyAug_Type = DisplayString
_SchedRepeatYearlyAug_Object = MibTableColumn
schedRepeatYearlyAug = _SchedRepeatYearlyAug_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 27),
    _SchedRepeatYearlyAug_Type()
)
schedRepeatYearlyAug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyAug.setStatus("current")
_SchedRepeatYearlySep_Type = DisplayString
_SchedRepeatYearlySep_Object = MibTableColumn
schedRepeatYearlySep = _SchedRepeatYearlySep_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 28),
    _SchedRepeatYearlySep_Type()
)
schedRepeatYearlySep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlySep.setStatus("current")
_SchedRepeatYearlyOct_Type = DisplayString
_SchedRepeatYearlyOct_Object = MibTableColumn
schedRepeatYearlyOct = _SchedRepeatYearlyOct_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 29),
    _SchedRepeatYearlyOct_Type()
)
schedRepeatYearlyOct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyOct.setStatus("current")
_SchedRepeatYearlyNov_Type = DisplayString
_SchedRepeatYearlyNov_Object = MibTableColumn
schedRepeatYearlyNov = _SchedRepeatYearlyNov_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 30),
    _SchedRepeatYearlyNov_Type()
)
schedRepeatYearlyNov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyNov.setStatus("current")
_SchedRepeatYearlyDec_Type = DisplayString
_SchedRepeatYearlyDec_Object = MibTableColumn
schedRepeatYearlyDec = _SchedRepeatYearlyDec_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 31),
    _SchedRepeatYearlyDec_Type()
)
schedRepeatYearlyDec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyDec.setStatus("current")
_SchedRepeatYearlyOnThe_Type = DisplayString
_SchedRepeatYearlyOnThe_Object = MibTableColumn
schedRepeatYearlyOnThe = _SchedRepeatYearlyOnThe_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 32),
    _SchedRepeatYearlyOnThe_Type()
)
schedRepeatYearlyOnThe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyOnThe.setStatus("current")
_SchedRepeatYearlyOnDay_Type = DisplayString
_SchedRepeatYearlyOnDay_Object = MibTableColumn
schedRepeatYearlyOnDay = _SchedRepeatYearlyOnDay_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 33),
    _SchedRepeatYearlyOnDay_Type()
)
schedRepeatYearlyOnDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    schedRepeatYearlyOnDay.setStatus("current")
_SchedNextTrigger_Type = DisplayString
_SchedNextTrigger_Object = MibTableColumn
schedNextTrigger = _SchedNextTrigger_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 2, 20, 1, 1, 34),
    _SchedNextTrigger_Type()
)
schedNextTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schedNextTrigger.setStatus("current")
_ProductIds_ObjectIdentity = ObjectIdentity
productIds = _ProductIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3)
)
_SiteName_Type = DisplayString
_SiteName_Object = MibScalar
siteName = _SiteName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3, 1),
    _SiteName_Type()
)
siteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteName.setStatus("current")
_ThisProduct_Type = DisplayString
_ThisProduct_Object = MibScalar
thisProduct = _ThisProduct_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3, 2),
    _ThisProduct_Type()
)
thisProduct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    thisProduct.setStatus("current")
_StockTrapString_Type = DisplayString
_StockTrapString_Object = MibScalar
stockTrapString = _StockTrapString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3, 3),
    _StockTrapString_Type()
)
stockTrapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stockTrapString.setStatus("current")
_TrapEventTypeNumber_Type = Integer32
_TrapEventTypeNumber_Object = MibScalar
trapEventTypeNumber = _TrapEventTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3, 4),
    _TrapEventTypeNumber_Type()
)
trapEventTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventTypeNumber.setStatus("current")
_TrapEventTypeName_Type = DisplayString
_TrapEventTypeName_Object = MibScalar
trapEventTypeName = _TrapEventTypeName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3, 5),
    _TrapEventTypeName_Type()
)
trapEventTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventTypeName.setStatus("current")


class _TrapIncludedValue_Type(Integer32):
    """Custom type trapIncludedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483648, 2147483647),
    )


_TrapIncludedValue_Type.__name__ = "Integer32"
_TrapIncludedValue_Object = MibScalar
trapIncludedValue = _TrapIncludedValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3, 6),
    _TrapIncludedValue_Type()
)
trapIncludedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIncludedValue.setStatus("current")
_TrapIncludedString_Type = DisplayString
_TrapIncludedString_Object = MibScalar
trapIncludedString = _TrapIncludedString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3, 7),
    _TrapIncludedString_Type()
)
trapIncludedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIncludedString.setStatus("current")
_TrapTypeString_Type = DisplayString
_TrapTypeString_Object = MibScalar
trapTypeString = _TrapTypeString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3, 8),
    _TrapTypeString_Type()
)
trapTypeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTypeString.setStatus("current")
_TrapEventClassNumber_Type = Integer32
_TrapEventClassNumber_Object = MibScalar
trapEventClassNumber = _TrapEventClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3, 9),
    _TrapEventClassNumber_Type()
)
trapEventClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventClassNumber.setStatus("current")
_TrapEventClassName_Type = DisplayString
_TrapEventClassName_Object = MibScalar
trapEventClassName = _TrapEventClassName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 3, 10),
    _TrapEventClassName_Type()
)
trapEventClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventClassName.setStatus("current")
_KeyInterface_Type = DisplayString
_KeyInterface_Object = MibScalar
keyInterface = _KeyInterface_Object(
    (1, 3, 6, 1, 4, 1, 3052, 18, 4),
    _KeyInterface_Type()
)
keyInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    keyInterface.setStatus("current")

# Managed Objects groups


# Notification objects

s350StockContactClosureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 110)
)
s350StockContactClosureTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockContactClosureTrap.setStatus(
        "current"
    )

s350StockTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 120)
)
s350StockTempTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockTempTrap.setStatus(
        "current"
    )

s350StockHumidityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 130)
)
s350StockHumidityTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockHumidityTrap.setStatus(
        "current"
    )

s350StockAnalogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 140)
)
s350StockAnalogTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockAnalogTrap.setStatus(
        "current"
    )

s350StockOutputTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 150)
)
s350StockOutputTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockOutputTrap.setStatus(
        "current"
    )

s350StockPDCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 180)
)
s350StockPDCurrentTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockPDCurrentTrap.setStatus(
        "current"
    )

s350StockPDVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 190)
)
s350StockPDVoltageTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockPDVoltageTrap.setStatus(
        "current"
    )

s350StockPDFuseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 210)
)
s350StockPDFuseTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockPDFuseTrap.setStatus(
        "current"
    )

s350StockSchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 506)
)
s350StockSchedTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockSchedTrap.setStatus(
        "current"
    )

s350StockImmediateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 507)
)
s350StockImmediateTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockImmediateTrap.setStatus(
        "current"
    )

s350StockCTSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 510)
)
s350StockCTSTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockCTSTrap.setStatus(
        "current"
    )

s350CPEDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 511)
)
s350CPEDownTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350CPEDownTrap.setStatus(
        "current"
    )

s350FuelSensorDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 515)
)
s350FuelSensorDisconnectTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350FuelSensorDisconnectTrap.setStatus(
        "current"
    )

s350FuelSensorVolumeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 519)
)
s350FuelSensorVolumeTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350FuelSensorVolumeTrap.setStatus(
        "current"
    )

s350ACPowerMonitorAvgVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 520)
)
s350ACPowerMonitorAvgVoltageTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350ACPowerMonitorAvgVoltageTrap.setStatus(
        "current"
    )

s350ACPowerMonitorAvgCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 521)
)
s350ACPowerMonitorAvgCurrentTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350ACPowerMonitorAvgCurrentTrap.setStatus(
        "current"
    )

s350ACPowerMonitorFrequencyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 522)
)
s350ACPowerMonitorFrequencyTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350ACPowerMonitorFrequencyTrap.setStatus(
        "current"
    )

s350ACPowerMonitorTRPTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 523)
)
s350ACPowerMonitorTRPTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350ACPowerMonitorTRPTrap.setStatus(
        "current"
    )

s350ACPowerMonitorDisconnectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 524)
)
s350ACPowerMonitorDisconnectTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350ACPowerMonitorDisconnectTrap.setStatus(
        "current"
    )

s350StockScriptTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 526)
)
s350StockScriptTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350StockScriptTrap.setStatus(
        "current"
    )

s350FuelSensorVolumeSuddenChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 527)
)
s350FuelSensorVolumeSuddenChangeTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350FuelSensorVolumeSuddenChangeTrap.setStatus(
        "current"
    )

s350FuelSensorVolumeSlowChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 528)
)
s350FuelSensorVolumeSlowChangeTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350FuelSensorVolumeSlowChangeTrap.setStatus(
        "current"
    )

s350BattMonStringTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 530)
)
s350BattMonStringTemperatureTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350BattMonStringTemperatureTrap.setStatus(
        "current"
    )

s350BattMonStringDiffTemperatureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 531)
)
s350BattMonStringDiffTemperatureTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350BattMonStringDiffTemperatureTrap.setStatus(
        "current"
    )

s350BattMonStringVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 532)
)
s350BattMonStringVoltageTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350BattMonStringVoltageTrap.setStatus(
        "current"
    )

s350BattMonStringChargeLevelTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 533)
)
s350BattMonStringChargeLevelTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350BattMonStringChargeLevelTrap.setStatus(
        "current"
    )

s350BattMonStringChargingCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 534)
)
s350BattMonStringChargingCurrentTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350BattMonStringChargingCurrentTrap.setStatus(
        "current"
    )

s350BattMonStringDischargingCurrentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 535)
)
s350BattMonStringDischargingCurrentTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350BattMonStringDischargingCurrentTrap.setStatus(
        "current"
    )

s350GeneratorNonStartTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 536)
)
s350GeneratorNonStartTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350GeneratorNonStartTrap.setStatus(
        "current"
    )

s350BattMonStringDifferentialVoltageTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 537)
)
s350BattMonStringDifferentialVoltageTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350BattMonStringDifferentialVoltageTrap.setStatus(
        "current"
    )

s350BattMonStringJarHealthTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 538)
)
s350BattMonStringJarHealthTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350BattMonStringJarHealthTrap.setStatus(
        "current"
    )

s350CameraTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 539)
)
s350CameraTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350CameraTrap.setStatus(
        "current"
    )

s350ACTotalPowerFactorTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 540)
)
s350ACTotalPowerFactorTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350ACTotalPowerFactorTrap.setStatus(
        "current"
    )

s350LocationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 541)
)
s350LocationTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350LocationTrap.setStatus(
        "current"
    )

s350SleepTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 542)
)
s350SleepTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350SleepTrap.setStatus(
        "current"
    )

s350ResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 543)
)
s350ResetTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350ResetTrap.setStatus(
        "current"
    )

s350FuelSensorLevelsAutoAdjustTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 544)
)
s350FuelSensorLevelsAutoAdjustTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350FuelSensorLevelsAutoAdjustTrap.setStatus(
        "current"
    )

s350AccessControlTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 547)
)
s350AccessControlTrap.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "stockTrapString"),
        ("SITEBOSS-350-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    s350AccessControlTrap.setStatus(
        "current"
    )

s350UserTrap1000 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1000)
)
s350UserTrap1000.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1000.setStatus(
        "current"
    )

s350UserTrap1001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1001)
)
s350UserTrap1001.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1001.setStatus(
        "current"
    )

s350UserTrap1002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1002)
)
s350UserTrap1002.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1002.setStatus(
        "current"
    )

s350UserTrap1003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1003)
)
s350UserTrap1003.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1003.setStatus(
        "current"
    )

s350UserTrap1004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1004)
)
s350UserTrap1004.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1004.setStatus(
        "current"
    )

s350UserTrap1005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1005)
)
s350UserTrap1005.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1005.setStatus(
        "current"
    )

s350UserTrap1006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1006)
)
s350UserTrap1006.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1006.setStatus(
        "current"
    )

s350UserTrap1007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1007)
)
s350UserTrap1007.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1007.setStatus(
        "current"
    )

s350UserTrap1008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1008)
)
s350UserTrap1008.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1008.setStatus(
        "current"
    )

s350UserTrap1009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1009)
)
s350UserTrap1009.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1009.setStatus(
        "current"
    )

s350UserTrap1010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1010)
)
s350UserTrap1010.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1010.setStatus(
        "current"
    )

s350UserTrap1011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1011)
)
s350UserTrap1011.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1011.setStatus(
        "current"
    )

s350UserTrap1012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1012)
)
s350UserTrap1012.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1012.setStatus(
        "current"
    )

s350UserTrap1013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1013)
)
s350UserTrap1013.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1013.setStatus(
        "current"
    )

s350UserTrap1014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1014)
)
s350UserTrap1014.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1014.setStatus(
        "current"
    )

s350UserTrap1015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1015)
)
s350UserTrap1015.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1015.setStatus(
        "current"
    )

s350UserTrap1016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1016)
)
s350UserTrap1016.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1016.setStatus(
        "current"
    )

s350UserTrap1017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1017)
)
s350UserTrap1017.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1017.setStatus(
        "current"
    )

s350UserTrap1018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1018)
)
s350UserTrap1018.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1018.setStatus(
        "current"
    )

s350UserTrap1019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1019)
)
s350UserTrap1019.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1019.setStatus(
        "current"
    )

s350UserTrap1020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1020)
)
s350UserTrap1020.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1020.setStatus(
        "current"
    )

s350UserTrap1021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1021)
)
s350UserTrap1021.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1021.setStatus(
        "current"
    )

s350UserTrap1022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1022)
)
s350UserTrap1022.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1022.setStatus(
        "current"
    )

s350UserTrap1023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1023)
)
s350UserTrap1023.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1023.setStatus(
        "current"
    )

s350UserTrap1024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1024)
)
s350UserTrap1024.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1024.setStatus(
        "current"
    )

s350UserTrap1025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1025)
)
s350UserTrap1025.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1025.setStatus(
        "current"
    )

s350UserTrap1026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1026)
)
s350UserTrap1026.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1026.setStatus(
        "current"
    )

s350UserTrap1027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1027)
)
s350UserTrap1027.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1027.setStatus(
        "current"
    )

s350UserTrap1028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1028)
)
s350UserTrap1028.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1028.setStatus(
        "current"
    )

s350UserTrap1029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1029)
)
s350UserTrap1029.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1029.setStatus(
        "current"
    )

s350UserTrap1030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1030)
)
s350UserTrap1030.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1030.setStatus(
        "current"
    )

s350UserTrap1031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1031)
)
s350UserTrap1031.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1031.setStatus(
        "current"
    )

s350UserTrap1032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1032)
)
s350UserTrap1032.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1032.setStatus(
        "current"
    )

s350UserTrap1033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1033)
)
s350UserTrap1033.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1033.setStatus(
        "current"
    )

s350UserTrap1034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1034)
)
s350UserTrap1034.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1034.setStatus(
        "current"
    )

s350UserTrap1035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1035)
)
s350UserTrap1035.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1035.setStatus(
        "current"
    )

s350UserTrap1036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1036)
)
s350UserTrap1036.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1036.setStatus(
        "current"
    )

s350UserTrap1037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1037)
)
s350UserTrap1037.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1037.setStatus(
        "current"
    )

s350UserTrap1038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1038)
)
s350UserTrap1038.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1038.setStatus(
        "current"
    )

s350UserTrap1039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1039)
)
s350UserTrap1039.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1039.setStatus(
        "current"
    )

s350UserTrap1040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1040)
)
s350UserTrap1040.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1040.setStatus(
        "current"
    )

s350UserTrap1041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1041)
)
s350UserTrap1041.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1041.setStatus(
        "current"
    )

s350UserTrap1042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1042)
)
s350UserTrap1042.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1042.setStatus(
        "current"
    )

s350UserTrap1043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1043)
)
s350UserTrap1043.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1043.setStatus(
        "current"
    )

s350UserTrap1044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1044)
)
s350UserTrap1044.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1044.setStatus(
        "current"
    )

s350UserTrap1045 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1045)
)
s350UserTrap1045.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1045.setStatus(
        "current"
    )

s350UserTrap1046 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1046)
)
s350UserTrap1046.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1046.setStatus(
        "current"
    )

s350UserTrap1047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1047)
)
s350UserTrap1047.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1047.setStatus(
        "current"
    )

s350UserTrap1048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1048)
)
s350UserTrap1048.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1048.setStatus(
        "current"
    )

s350UserTrap1049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1049)
)
s350UserTrap1049.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1049.setStatus(
        "current"
    )

s350UserTrap1050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1050)
)
s350UserTrap1050.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1050.setStatus(
        "current"
    )

s350UserTrap1051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1051)
)
s350UserTrap1051.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1051.setStatus(
        "current"
    )

s350UserTrap1052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1052)
)
s350UserTrap1052.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1052.setStatus(
        "current"
    )

s350UserTrap1053 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1053)
)
s350UserTrap1053.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1053.setStatus(
        "current"
    )

s350UserTrap1054 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1054)
)
s350UserTrap1054.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1054.setStatus(
        "current"
    )

s350UserTrap1055 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1055)
)
s350UserTrap1055.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1055.setStatus(
        "current"
    )

s350UserTrap1056 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1056)
)
s350UserTrap1056.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1056.setStatus(
        "current"
    )

s350UserTrap1057 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1057)
)
s350UserTrap1057.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1057.setStatus(
        "current"
    )

s350UserTrap1058 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1058)
)
s350UserTrap1058.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1058.setStatus(
        "current"
    )

s350UserTrap1059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1059)
)
s350UserTrap1059.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1059.setStatus(
        "current"
    )

s350UserTrap1060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1060)
)
s350UserTrap1060.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1060.setStatus(
        "current"
    )

s350UserTrap1061 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1061)
)
s350UserTrap1061.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1061.setStatus(
        "current"
    )

s350UserTrap1062 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1062)
)
s350UserTrap1062.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1062.setStatus(
        "current"
    )

s350UserTrap1063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1063)
)
s350UserTrap1063.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1063.setStatus(
        "current"
    )

s350UserTrap1064 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1064)
)
s350UserTrap1064.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1064.setStatus(
        "current"
    )

s350UserTrap1065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1065)
)
s350UserTrap1065.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1065.setStatus(
        "current"
    )

s350UserTrap1066 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1066)
)
s350UserTrap1066.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1066.setStatus(
        "current"
    )

s350UserTrap1067 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1067)
)
s350UserTrap1067.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1067.setStatus(
        "current"
    )

s350UserTrap1068 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1068)
)
s350UserTrap1068.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1068.setStatus(
        "current"
    )

s350UserTrap1069 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1069)
)
s350UserTrap1069.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1069.setStatus(
        "current"
    )

s350UserTrap1070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1070)
)
s350UserTrap1070.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1070.setStatus(
        "current"
    )

s350UserTrap1071 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1071)
)
s350UserTrap1071.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1071.setStatus(
        "current"
    )

s350UserTrap1072 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1072)
)
s350UserTrap1072.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1072.setStatus(
        "current"
    )

s350UserTrap1073 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1073)
)
s350UserTrap1073.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1073.setStatus(
        "current"
    )

s350UserTrap1074 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1074)
)
s350UserTrap1074.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1074.setStatus(
        "current"
    )

s350UserTrap1075 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1075)
)
s350UserTrap1075.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1075.setStatus(
        "current"
    )

s350UserTrap1076 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1076)
)
s350UserTrap1076.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1076.setStatus(
        "current"
    )

s350UserTrap1077 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1077)
)
s350UserTrap1077.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1077.setStatus(
        "current"
    )

s350UserTrap1078 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1078)
)
s350UserTrap1078.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1078.setStatus(
        "current"
    )

s350UserTrap1079 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1079)
)
s350UserTrap1079.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1079.setStatus(
        "current"
    )

s350UserTrap1080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1080)
)
s350UserTrap1080.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1080.setStatus(
        "current"
    )

s350UserTrap1081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1081)
)
s350UserTrap1081.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1081.setStatus(
        "current"
    )

s350UserTrap1082 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1082)
)
s350UserTrap1082.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1082.setStatus(
        "current"
    )

s350UserTrap1083 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1083)
)
s350UserTrap1083.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1083.setStatus(
        "current"
    )

s350UserTrap1084 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1084)
)
s350UserTrap1084.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1084.setStatus(
        "current"
    )

s350UserTrap1085 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1085)
)
s350UserTrap1085.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1085.setStatus(
        "current"
    )

s350UserTrap1086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1086)
)
s350UserTrap1086.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1086.setStatus(
        "current"
    )

s350UserTrap1087 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1087)
)
s350UserTrap1087.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1087.setStatus(
        "current"
    )

s350UserTrap1088 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1088)
)
s350UserTrap1088.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1088.setStatus(
        "current"
    )

s350UserTrap1089 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1089)
)
s350UserTrap1089.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1089.setStatus(
        "current"
    )

s350UserTrap1090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1090)
)
s350UserTrap1090.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1090.setStatus(
        "current"
    )

s350UserTrap1091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1091)
)
s350UserTrap1091.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1091.setStatus(
        "current"
    )

s350UserTrap1092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1092)
)
s350UserTrap1092.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1092.setStatus(
        "current"
    )

s350UserTrap1093 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1093)
)
s350UserTrap1093.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1093.setStatus(
        "current"
    )

s350UserTrap1094 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1094)
)
s350UserTrap1094.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1094.setStatus(
        "current"
    )

s350UserTrap1095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1095)
)
s350UserTrap1095.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1095.setStatus(
        "current"
    )

s350UserTrap1096 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1096)
)
s350UserTrap1096.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1096.setStatus(
        "current"
    )

s350UserTrap1097 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1097)
)
s350UserTrap1097.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1097.setStatus(
        "current"
    )

s350UserTrap1098 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1098)
)
s350UserTrap1098.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1098.setStatus(
        "current"
    )

s350UserTrap1099 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1099)
)
s350UserTrap1099.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1099.setStatus(
        "current"
    )

s350UserTrap1100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1100)
)
s350UserTrap1100.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1100.setStatus(
        "current"
    )

s350UserTrap1101 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1101)
)
s350UserTrap1101.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1101.setStatus(
        "current"
    )

s350UserTrap1102 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1102)
)
s350UserTrap1102.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1102.setStatus(
        "current"
    )

s350UserTrap1103 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1103)
)
s350UserTrap1103.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1103.setStatus(
        "current"
    )

s350UserTrap1104 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1104)
)
s350UserTrap1104.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1104.setStatus(
        "current"
    )

s350UserTrap1105 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1105)
)
s350UserTrap1105.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1105.setStatus(
        "current"
    )

s350UserTrap1106 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1106)
)
s350UserTrap1106.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1106.setStatus(
        "current"
    )

s350UserTrap1107 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1107)
)
s350UserTrap1107.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1107.setStatus(
        "current"
    )

s350UserTrap1108 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1108)
)
s350UserTrap1108.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1108.setStatus(
        "current"
    )

s350UserTrap1109 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1109)
)
s350UserTrap1109.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1109.setStatus(
        "current"
    )

s350UserTrap1110 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1110)
)
s350UserTrap1110.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1110.setStatus(
        "current"
    )

s350UserTrap1111 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1111)
)
s350UserTrap1111.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1111.setStatus(
        "current"
    )

s350UserTrap1112 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1112)
)
s350UserTrap1112.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1112.setStatus(
        "current"
    )

s350UserTrap1113 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1113)
)
s350UserTrap1113.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1113.setStatus(
        "current"
    )

s350UserTrap1114 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1114)
)
s350UserTrap1114.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1114.setStatus(
        "current"
    )

s350UserTrap1115 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1115)
)
s350UserTrap1115.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1115.setStatus(
        "current"
    )

s350UserTrap1116 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1116)
)
s350UserTrap1116.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1116.setStatus(
        "current"
    )

s350UserTrap1117 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1117)
)
s350UserTrap1117.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1117.setStatus(
        "current"
    )

s350UserTrap1118 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1118)
)
s350UserTrap1118.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1118.setStatus(
        "current"
    )

s350UserTrap1119 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1119)
)
s350UserTrap1119.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1119.setStatus(
        "current"
    )

s350UserTrap1120 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1120)
)
s350UserTrap1120.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1120.setStatus(
        "current"
    )

s350UserTrap1121 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1121)
)
s350UserTrap1121.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1121.setStatus(
        "current"
    )

s350UserTrap1122 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1122)
)
s350UserTrap1122.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1122.setStatus(
        "current"
    )

s350UserTrap1123 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1123)
)
s350UserTrap1123.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1123.setStatus(
        "current"
    )

s350UserTrap1124 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1124)
)
s350UserTrap1124.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1124.setStatus(
        "current"
    )

s350UserTrap1125 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1125)
)
s350UserTrap1125.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1125.setStatus(
        "current"
    )

s350UserTrap1126 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1126)
)
s350UserTrap1126.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1126.setStatus(
        "current"
    )

s350UserTrap1127 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1127)
)
s350UserTrap1127.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1127.setStatus(
        "current"
    )

s350UserTrap1128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1128)
)
s350UserTrap1128.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1128.setStatus(
        "current"
    )

s350UserTrap1129 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1129)
)
s350UserTrap1129.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1129.setStatus(
        "current"
    )

s350UserTrap1130 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1130)
)
s350UserTrap1130.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1130.setStatus(
        "current"
    )

s350UserTrap1131 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1131)
)
s350UserTrap1131.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1131.setStatus(
        "current"
    )

s350UserTrap1132 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1132)
)
s350UserTrap1132.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1132.setStatus(
        "current"
    )

s350UserTrap1133 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1133)
)
s350UserTrap1133.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1133.setStatus(
        "current"
    )

s350UserTrap1134 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1134)
)
s350UserTrap1134.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1134.setStatus(
        "current"
    )

s350UserTrap1135 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1135)
)
s350UserTrap1135.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1135.setStatus(
        "current"
    )

s350UserTrap1136 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1136)
)
s350UserTrap1136.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1136.setStatus(
        "current"
    )

s350UserTrap1137 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1137)
)
s350UserTrap1137.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1137.setStatus(
        "current"
    )

s350UserTrap1138 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1138)
)
s350UserTrap1138.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1138.setStatus(
        "current"
    )

s350UserTrap1139 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1139)
)
s350UserTrap1139.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1139.setStatus(
        "current"
    )

s350UserTrap1140 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1140)
)
s350UserTrap1140.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1140.setStatus(
        "current"
    )

s350UserTrap1141 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1141)
)
s350UserTrap1141.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1141.setStatus(
        "current"
    )

s350UserTrap1142 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1142)
)
s350UserTrap1142.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1142.setStatus(
        "current"
    )

s350UserTrap1143 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1143)
)
s350UserTrap1143.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1143.setStatus(
        "current"
    )

s350UserTrap1144 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1144)
)
s350UserTrap1144.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1144.setStatus(
        "current"
    )

s350UserTrap1145 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1145)
)
s350UserTrap1145.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1145.setStatus(
        "current"
    )

s350UserTrap1146 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1146)
)
s350UserTrap1146.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1146.setStatus(
        "current"
    )

s350UserTrap1147 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1147)
)
s350UserTrap1147.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1147.setStatus(
        "current"
    )

s350UserTrap1148 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1148)
)
s350UserTrap1148.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1148.setStatus(
        "current"
    )

s350UserTrap1149 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1149)
)
s350UserTrap1149.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1149.setStatus(
        "current"
    )

s350UserTrap1150 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1150)
)
s350UserTrap1150.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1150.setStatus(
        "current"
    )

s350UserTrap1151 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1151)
)
s350UserTrap1151.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1151.setStatus(
        "current"
    )

s350UserTrap1152 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1152)
)
s350UserTrap1152.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1152.setStatus(
        "current"
    )

s350UserTrap1153 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1153)
)
s350UserTrap1153.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1153.setStatus(
        "current"
    )

s350UserTrap1154 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1154)
)
s350UserTrap1154.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1154.setStatus(
        "current"
    )

s350UserTrap1155 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1155)
)
s350UserTrap1155.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1155.setStatus(
        "current"
    )

s350UserTrap1156 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1156)
)
s350UserTrap1156.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1156.setStatus(
        "current"
    )

s350UserTrap1157 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1157)
)
s350UserTrap1157.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1157.setStatus(
        "current"
    )

s350UserTrap1158 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1158)
)
s350UserTrap1158.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1158.setStatus(
        "current"
    )

s350UserTrap1159 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1159)
)
s350UserTrap1159.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1159.setStatus(
        "current"
    )

s350UserTrap1160 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1160)
)
s350UserTrap1160.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1160.setStatus(
        "current"
    )

s350UserTrap1161 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1161)
)
s350UserTrap1161.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1161.setStatus(
        "current"
    )

s350UserTrap1162 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1162)
)
s350UserTrap1162.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1162.setStatus(
        "current"
    )

s350UserTrap1163 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1163)
)
s350UserTrap1163.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1163.setStatus(
        "current"
    )

s350UserTrap1164 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1164)
)
s350UserTrap1164.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1164.setStatus(
        "current"
    )

s350UserTrap1165 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1165)
)
s350UserTrap1165.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1165.setStatus(
        "current"
    )

s350UserTrap1166 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1166)
)
s350UserTrap1166.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1166.setStatus(
        "current"
    )

s350UserTrap1167 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1167)
)
s350UserTrap1167.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1167.setStatus(
        "current"
    )

s350UserTrap1168 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1168)
)
s350UserTrap1168.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1168.setStatus(
        "current"
    )

s350UserTrap1169 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1169)
)
s350UserTrap1169.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1169.setStatus(
        "current"
    )

s350UserTrap1170 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1170)
)
s350UserTrap1170.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1170.setStatus(
        "current"
    )

s350UserTrap1171 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1171)
)
s350UserTrap1171.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1171.setStatus(
        "current"
    )

s350UserTrap1172 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1172)
)
s350UserTrap1172.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1172.setStatus(
        "current"
    )

s350UserTrap1173 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1173)
)
s350UserTrap1173.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1173.setStatus(
        "current"
    )

s350UserTrap1174 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1174)
)
s350UserTrap1174.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1174.setStatus(
        "current"
    )

s350UserTrap1175 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1175)
)
s350UserTrap1175.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1175.setStatus(
        "current"
    )

s350UserTrap1176 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1176)
)
s350UserTrap1176.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1176.setStatus(
        "current"
    )

s350UserTrap1177 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1177)
)
s350UserTrap1177.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1177.setStatus(
        "current"
    )

s350UserTrap1178 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1178)
)
s350UserTrap1178.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1178.setStatus(
        "current"
    )

s350UserTrap1179 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1179)
)
s350UserTrap1179.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1179.setStatus(
        "current"
    )

s350UserTrap1180 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1180)
)
s350UserTrap1180.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1180.setStatus(
        "current"
    )

s350UserTrap1181 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1181)
)
s350UserTrap1181.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1181.setStatus(
        "current"
    )

s350UserTrap1182 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1182)
)
s350UserTrap1182.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1182.setStatus(
        "current"
    )

s350UserTrap1183 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1183)
)
s350UserTrap1183.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1183.setStatus(
        "current"
    )

s350UserTrap1184 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1184)
)
s350UserTrap1184.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1184.setStatus(
        "current"
    )

s350UserTrap1185 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1185)
)
s350UserTrap1185.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1185.setStatus(
        "current"
    )

s350UserTrap1186 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1186)
)
s350UserTrap1186.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1186.setStatus(
        "current"
    )

s350UserTrap1187 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1187)
)
s350UserTrap1187.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1187.setStatus(
        "current"
    )

s350UserTrap1188 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1188)
)
s350UserTrap1188.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1188.setStatus(
        "current"
    )

s350UserTrap1189 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1189)
)
s350UserTrap1189.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1189.setStatus(
        "current"
    )

s350UserTrap1190 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1190)
)
s350UserTrap1190.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1190.setStatus(
        "current"
    )

s350UserTrap1191 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1191)
)
s350UserTrap1191.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1191.setStatus(
        "current"
    )

s350UserTrap1192 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1192)
)
s350UserTrap1192.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1192.setStatus(
        "current"
    )

s350UserTrap1193 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1193)
)
s350UserTrap1193.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1193.setStatus(
        "current"
    )

s350UserTrap1194 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1194)
)
s350UserTrap1194.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1194.setStatus(
        "current"
    )

s350UserTrap1195 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1195)
)
s350UserTrap1195.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1195.setStatus(
        "current"
    )

s350UserTrap1196 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1196)
)
s350UserTrap1196.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1196.setStatus(
        "current"
    )

s350UserTrap1197 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1197)
)
s350UserTrap1197.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1197.setStatus(
        "current"
    )

s350UserTrap1198 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1198)
)
s350UserTrap1198.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1198.setStatus(
        "current"
    )

s350UserTrap1199 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 18, 0, 1199)
)
s350UserTrap1199.setObjects(
      *(("SITEBOSS-350-STD-MIB", "siteName"),
        ("SITEBOSS-350-STD-MIB", "esIndex"),
        ("SITEBOSS-350-STD-MIB", "esName"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventTypeName"),
        ("SITEBOSS-350-STD-MIB", "esIndexPoint"),
        ("SITEBOSS-350-STD-MIB", "esPointName"),
        ("SITEBOSS-350-STD-MIB", "esID"),
        ("SITEBOSS-350-STD-MIB", "clock"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedValue"),
        ("SITEBOSS-350-STD-MIB", "trapIncludedString"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassNumber"),
        ("SITEBOSS-350-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    s350UserTrap1199.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SITEBOSS-350-STD-MIB",
    **{"s350": s350,
       "s350Notifications": s350Notifications,
       "s350StockContactClosureTrap": s350StockContactClosureTrap,
       "s350StockTempTrap": s350StockTempTrap,
       "s350StockHumidityTrap": s350StockHumidityTrap,
       "s350StockAnalogTrap": s350StockAnalogTrap,
       "s350StockOutputTrap": s350StockOutputTrap,
       "s350StockPDCurrentTrap": s350StockPDCurrentTrap,
       "s350StockPDVoltageTrap": s350StockPDVoltageTrap,
       "s350StockPDFuseTrap": s350StockPDFuseTrap,
       "s350StockSchedTrap": s350StockSchedTrap,
       "s350StockImmediateTrap": s350StockImmediateTrap,
       "s350StockCTSTrap": s350StockCTSTrap,
       "s350CPEDownTrap": s350CPEDownTrap,
       "s350FuelSensorDisconnectTrap": s350FuelSensorDisconnectTrap,
       "s350FuelSensorVolumeTrap": s350FuelSensorVolumeTrap,
       "s350ACPowerMonitorAvgVoltageTrap": s350ACPowerMonitorAvgVoltageTrap,
       "s350ACPowerMonitorAvgCurrentTrap": s350ACPowerMonitorAvgCurrentTrap,
       "s350ACPowerMonitorFrequencyTrap": s350ACPowerMonitorFrequencyTrap,
       "s350ACPowerMonitorTRPTrap": s350ACPowerMonitorTRPTrap,
       "s350ACPowerMonitorDisconnectTrap": s350ACPowerMonitorDisconnectTrap,
       "s350StockScriptTrap": s350StockScriptTrap,
       "s350FuelSensorVolumeSuddenChangeTrap": s350FuelSensorVolumeSuddenChangeTrap,
       "s350FuelSensorVolumeSlowChangeTrap": s350FuelSensorVolumeSlowChangeTrap,
       "s350BattMonStringTemperatureTrap": s350BattMonStringTemperatureTrap,
       "s350BattMonStringDiffTemperatureTrap": s350BattMonStringDiffTemperatureTrap,
       "s350BattMonStringVoltageTrap": s350BattMonStringVoltageTrap,
       "s350BattMonStringChargeLevelTrap": s350BattMonStringChargeLevelTrap,
       "s350BattMonStringChargingCurrentTrap": s350BattMonStringChargingCurrentTrap,
       "s350BattMonStringDischargingCurrentTrap": s350BattMonStringDischargingCurrentTrap,
       "s350GeneratorNonStartTrap": s350GeneratorNonStartTrap,
       "s350BattMonStringDifferentialVoltageTrap": s350BattMonStringDifferentialVoltageTrap,
       "s350BattMonStringJarHealthTrap": s350BattMonStringJarHealthTrap,
       "s350CameraTrap": s350CameraTrap,
       "s350ACTotalPowerFactorTrap": s350ACTotalPowerFactorTrap,
       "s350LocationTrap": s350LocationTrap,
       "s350SleepTrap": s350SleepTrap,
       "s350ResetTrap": s350ResetTrap,
       "s350FuelSensorLevelsAutoAdjustTrap": s350FuelSensorLevelsAutoAdjustTrap,
       "s350AccessControlTrap": s350AccessControlTrap,
       "s350UserTrap1000": s350UserTrap1000,
       "s350UserTrap1001": s350UserTrap1001,
       "s350UserTrap1002": s350UserTrap1002,
       "s350UserTrap1003": s350UserTrap1003,
       "s350UserTrap1004": s350UserTrap1004,
       "s350UserTrap1005": s350UserTrap1005,
       "s350UserTrap1006": s350UserTrap1006,
       "s350UserTrap1007": s350UserTrap1007,
       "s350UserTrap1008": s350UserTrap1008,
       "s350UserTrap1009": s350UserTrap1009,
       "s350UserTrap1010": s350UserTrap1010,
       "s350UserTrap1011": s350UserTrap1011,
       "s350UserTrap1012": s350UserTrap1012,
       "s350UserTrap1013": s350UserTrap1013,
       "s350UserTrap1014": s350UserTrap1014,
       "s350UserTrap1015": s350UserTrap1015,
       "s350UserTrap1016": s350UserTrap1016,
       "s350UserTrap1017": s350UserTrap1017,
       "s350UserTrap1018": s350UserTrap1018,
       "s350UserTrap1019": s350UserTrap1019,
       "s350UserTrap1020": s350UserTrap1020,
       "s350UserTrap1021": s350UserTrap1021,
       "s350UserTrap1022": s350UserTrap1022,
       "s350UserTrap1023": s350UserTrap1023,
       "s350UserTrap1024": s350UserTrap1024,
       "s350UserTrap1025": s350UserTrap1025,
       "s350UserTrap1026": s350UserTrap1026,
       "s350UserTrap1027": s350UserTrap1027,
       "s350UserTrap1028": s350UserTrap1028,
       "s350UserTrap1029": s350UserTrap1029,
       "s350UserTrap1030": s350UserTrap1030,
       "s350UserTrap1031": s350UserTrap1031,
       "s350UserTrap1032": s350UserTrap1032,
       "s350UserTrap1033": s350UserTrap1033,
       "s350UserTrap1034": s350UserTrap1034,
       "s350UserTrap1035": s350UserTrap1035,
       "s350UserTrap1036": s350UserTrap1036,
       "s350UserTrap1037": s350UserTrap1037,
       "s350UserTrap1038": s350UserTrap1038,
       "s350UserTrap1039": s350UserTrap1039,
       "s350UserTrap1040": s350UserTrap1040,
       "s350UserTrap1041": s350UserTrap1041,
       "s350UserTrap1042": s350UserTrap1042,
       "s350UserTrap1043": s350UserTrap1043,
       "s350UserTrap1044": s350UserTrap1044,
       "s350UserTrap1045": s350UserTrap1045,
       "s350UserTrap1046": s350UserTrap1046,
       "s350UserTrap1047": s350UserTrap1047,
       "s350UserTrap1048": s350UserTrap1048,
       "s350UserTrap1049": s350UserTrap1049,
       "s350UserTrap1050": s350UserTrap1050,
       "s350UserTrap1051": s350UserTrap1051,
       "s350UserTrap1052": s350UserTrap1052,
       "s350UserTrap1053": s350UserTrap1053,
       "s350UserTrap1054": s350UserTrap1054,
       "s350UserTrap1055": s350UserTrap1055,
       "s350UserTrap1056": s350UserTrap1056,
       "s350UserTrap1057": s350UserTrap1057,
       "s350UserTrap1058": s350UserTrap1058,
       "s350UserTrap1059": s350UserTrap1059,
       "s350UserTrap1060": s350UserTrap1060,
       "s350UserTrap1061": s350UserTrap1061,
       "s350UserTrap1062": s350UserTrap1062,
       "s350UserTrap1063": s350UserTrap1063,
       "s350UserTrap1064": s350UserTrap1064,
       "s350UserTrap1065": s350UserTrap1065,
       "s350UserTrap1066": s350UserTrap1066,
       "s350UserTrap1067": s350UserTrap1067,
       "s350UserTrap1068": s350UserTrap1068,
       "s350UserTrap1069": s350UserTrap1069,
       "s350UserTrap1070": s350UserTrap1070,
       "s350UserTrap1071": s350UserTrap1071,
       "s350UserTrap1072": s350UserTrap1072,
       "s350UserTrap1073": s350UserTrap1073,
       "s350UserTrap1074": s350UserTrap1074,
       "s350UserTrap1075": s350UserTrap1075,
       "s350UserTrap1076": s350UserTrap1076,
       "s350UserTrap1077": s350UserTrap1077,
       "s350UserTrap1078": s350UserTrap1078,
       "s350UserTrap1079": s350UserTrap1079,
       "s350UserTrap1080": s350UserTrap1080,
       "s350UserTrap1081": s350UserTrap1081,
       "s350UserTrap1082": s350UserTrap1082,
       "s350UserTrap1083": s350UserTrap1083,
       "s350UserTrap1084": s350UserTrap1084,
       "s350UserTrap1085": s350UserTrap1085,
       "s350UserTrap1086": s350UserTrap1086,
       "s350UserTrap1087": s350UserTrap1087,
       "s350UserTrap1088": s350UserTrap1088,
       "s350UserTrap1089": s350UserTrap1089,
       "s350UserTrap1090": s350UserTrap1090,
       "s350UserTrap1091": s350UserTrap1091,
       "s350UserTrap1092": s350UserTrap1092,
       "s350UserTrap1093": s350UserTrap1093,
       "s350UserTrap1094": s350UserTrap1094,
       "s350UserTrap1095": s350UserTrap1095,
       "s350UserTrap1096": s350UserTrap1096,
       "s350UserTrap1097": s350UserTrap1097,
       "s350UserTrap1098": s350UserTrap1098,
       "s350UserTrap1099": s350UserTrap1099,
       "s350UserTrap1100": s350UserTrap1100,
       "s350UserTrap1101": s350UserTrap1101,
       "s350UserTrap1102": s350UserTrap1102,
       "s350UserTrap1103": s350UserTrap1103,
       "s350UserTrap1104": s350UserTrap1104,
       "s350UserTrap1105": s350UserTrap1105,
       "s350UserTrap1106": s350UserTrap1106,
       "s350UserTrap1107": s350UserTrap1107,
       "s350UserTrap1108": s350UserTrap1108,
       "s350UserTrap1109": s350UserTrap1109,
       "s350UserTrap1110": s350UserTrap1110,
       "s350UserTrap1111": s350UserTrap1111,
       "s350UserTrap1112": s350UserTrap1112,
       "s350UserTrap1113": s350UserTrap1113,
       "s350UserTrap1114": s350UserTrap1114,
       "s350UserTrap1115": s350UserTrap1115,
       "s350UserTrap1116": s350UserTrap1116,
       "s350UserTrap1117": s350UserTrap1117,
       "s350UserTrap1118": s350UserTrap1118,
       "s350UserTrap1119": s350UserTrap1119,
       "s350UserTrap1120": s350UserTrap1120,
       "s350UserTrap1121": s350UserTrap1121,
       "s350UserTrap1122": s350UserTrap1122,
       "s350UserTrap1123": s350UserTrap1123,
       "s350UserTrap1124": s350UserTrap1124,
       "s350UserTrap1125": s350UserTrap1125,
       "s350UserTrap1126": s350UserTrap1126,
       "s350UserTrap1127": s350UserTrap1127,
       "s350UserTrap1128": s350UserTrap1128,
       "s350UserTrap1129": s350UserTrap1129,
       "s350UserTrap1130": s350UserTrap1130,
       "s350UserTrap1131": s350UserTrap1131,
       "s350UserTrap1132": s350UserTrap1132,
       "s350UserTrap1133": s350UserTrap1133,
       "s350UserTrap1134": s350UserTrap1134,
       "s350UserTrap1135": s350UserTrap1135,
       "s350UserTrap1136": s350UserTrap1136,
       "s350UserTrap1137": s350UserTrap1137,
       "s350UserTrap1138": s350UserTrap1138,
       "s350UserTrap1139": s350UserTrap1139,
       "s350UserTrap1140": s350UserTrap1140,
       "s350UserTrap1141": s350UserTrap1141,
       "s350UserTrap1142": s350UserTrap1142,
       "s350UserTrap1143": s350UserTrap1143,
       "s350UserTrap1144": s350UserTrap1144,
       "s350UserTrap1145": s350UserTrap1145,
       "s350UserTrap1146": s350UserTrap1146,
       "s350UserTrap1147": s350UserTrap1147,
       "s350UserTrap1148": s350UserTrap1148,
       "s350UserTrap1149": s350UserTrap1149,
       "s350UserTrap1150": s350UserTrap1150,
       "s350UserTrap1151": s350UserTrap1151,
       "s350UserTrap1152": s350UserTrap1152,
       "s350UserTrap1153": s350UserTrap1153,
       "s350UserTrap1154": s350UserTrap1154,
       "s350UserTrap1155": s350UserTrap1155,
       "s350UserTrap1156": s350UserTrap1156,
       "s350UserTrap1157": s350UserTrap1157,
       "s350UserTrap1158": s350UserTrap1158,
       "s350UserTrap1159": s350UserTrap1159,
       "s350UserTrap1160": s350UserTrap1160,
       "s350UserTrap1161": s350UserTrap1161,
       "s350UserTrap1162": s350UserTrap1162,
       "s350UserTrap1163": s350UserTrap1163,
       "s350UserTrap1164": s350UserTrap1164,
       "s350UserTrap1165": s350UserTrap1165,
       "s350UserTrap1166": s350UserTrap1166,
       "s350UserTrap1167": s350UserTrap1167,
       "s350UserTrap1168": s350UserTrap1168,
       "s350UserTrap1169": s350UserTrap1169,
       "s350UserTrap1170": s350UserTrap1170,
       "s350UserTrap1171": s350UserTrap1171,
       "s350UserTrap1172": s350UserTrap1172,
       "s350UserTrap1173": s350UserTrap1173,
       "s350UserTrap1174": s350UserTrap1174,
       "s350UserTrap1175": s350UserTrap1175,
       "s350UserTrap1176": s350UserTrap1176,
       "s350UserTrap1177": s350UserTrap1177,
       "s350UserTrap1178": s350UserTrap1178,
       "s350UserTrap1179": s350UserTrap1179,
       "s350UserTrap1180": s350UserTrap1180,
       "s350UserTrap1181": s350UserTrap1181,
       "s350UserTrap1182": s350UserTrap1182,
       "s350UserTrap1183": s350UserTrap1183,
       "s350UserTrap1184": s350UserTrap1184,
       "s350UserTrap1185": s350UserTrap1185,
       "s350UserTrap1186": s350UserTrap1186,
       "s350UserTrap1187": s350UserTrap1187,
       "s350UserTrap1188": s350UserTrap1188,
       "s350UserTrap1189": s350UserTrap1189,
       "s350UserTrap1190": s350UserTrap1190,
       "s350UserTrap1191": s350UserTrap1191,
       "s350UserTrap1192": s350UserTrap1192,
       "s350UserTrap1193": s350UserTrap1193,
       "s350UserTrap1194": s350UserTrap1194,
       "s350UserTrap1195": s350UserTrap1195,
       "s350UserTrap1196": s350UserTrap1196,
       "s350UserTrap1197": s350UserTrap1197,
       "s350UserTrap1198": s350UserTrap1198,
       "s350UserTrap1199": s350UserTrap1199,
       "status": status,
       "eventSensorStatus": eventSensorStatus,
       "esPointTable": esPointTable,
       "esPointEntry": esPointEntry,
       "esIndexES": esIndexES,
       "esIndexPC": esIndexPC,
       "esIndexPoint": esIndexPoint,
       "esPointName": esPointName,
       "esPointInEventState": esPointInEventState,
       "esPointValueInt": esPointValueInt,
       "esPointValueStr": esPointValueStr,
       "esPointTimeLastChange": esPointTimeLastChange,
       "esPointTimetickLastChange": esPointTimetickLastChange,
       "esPointAliasValueStr": esPointAliasValueStr,
       "dataEventStatus": dataEventStatus,
       "deStatusTable": deStatusTable,
       "deStatusEntry": deStatusEntry,
       "deStatusIndex": deStatusIndex,
       "deStatusName": deStatusName,
       "deStatusCounter": deStatusCounter,
       "deStatusThreshold": deStatusThreshold,
       "powerDistributionStatus": powerDistributionStatus,
       "pdConfig": pdConfig,
       "pdNextGen": pdNextGen,
       "pdnTable": pdnTable,
       "pdnEntry": pdnEntry,
       "pdnIndexPD": pdnIndexPD,
       "pdnIndexOutput": pdnIndexOutput,
       "pdnConfig": pdnConfig,
       "pdnMainCurrentInEventState": pdnMainCurrentInEventState,
       "pdnMainCurrentValue": pdnMainCurrentValue,
       "pdnMainCurrentValueStr": pdnMainCurrentValueStr,
       "pdnMainCurrentDeadband": pdnMainCurrentDeadband,
       "pdnMainCurrentVHighCurrent": pdnMainCurrentVHighCurrent,
       "pdnMainCurrentHighCurrent": pdnMainCurrentHighCurrent,
       "pdnMainCurrentLowCurrent": pdnMainCurrentLowCurrent,
       "pdnMainCurrentVLowCurrent": pdnMainCurrentVLowCurrent,
       "pdnMainVoltageInEventState": pdnMainVoltageInEventState,
       "pdnMainVoltageValue": pdnMainVoltageValue,
       "pdnMainVoltageValueStr": pdnMainVoltageValueStr,
       "pdnMainVoltageDeadband": pdnMainVoltageDeadband,
       "pdnMainVoltageVHighVoltage": pdnMainVoltageVHighVoltage,
       "pdnMainVoltageHighVoltage": pdnMainVoltageHighVoltage,
       "pdnMainVoltageLowVoltage": pdnMainVoltageLowVoltage,
       "pdnMainVoltageVLowVoltage": pdnMainVoltageVLowVoltage,
       "pdnMainPowerValue": pdnMainPowerValue,
       "pdnMainPowerValueStr": pdnMainPowerValueStr,
       "pdnOutputCurrentInEventState": pdnOutputCurrentInEventState,
       "pdnOutputCurrentValue": pdnOutputCurrentValue,
       "pdnOutputCurrentValueStr": pdnOutputCurrentValueStr,
       "pdnOutputCurrentDeadband": pdnOutputCurrentDeadband,
       "pdnOutputCurrentVHighCurrent": pdnOutputCurrentVHighCurrent,
       "pdnOutputCurrentHighCurrent": pdnOutputCurrentHighCurrent,
       "pdnOutputCurrentLowCurrent": pdnOutputCurrentLowCurrent,
       "pdnOutputCurrentVLowCurrent": pdnOutputCurrentVLowCurrent,
       "pdnOutputFuseInEventState": pdnOutputFuseInEventState,
       "pdnOutputFuseValueStr": pdnOutputFuseValueStr,
       "pdnMainCombinedStatus": pdnMainCombinedStatus,
       "pdnOutputCombinedStatusBlock1": pdnOutputCombinedStatusBlock1,
       "pdnOutputCombinedStatusBlock2": pdnOutputCombinedStatusBlock2,
       "pdnDeviceCurrentValue": pdnDeviceCurrentValue,
       "pdnDeviceCurrentValueStr": pdnDeviceCurrentValueStr,
       "pdSystem": pdSystem,
       "pdSystemCurrent": pdSystemCurrent,
       "pdSystemPower": pdSystemPower,
       "fuelSensorStatus": fuelSensorStatus,
       "fsStatusTable": fsStatusTable,
       "fsStatusEntry": fsStatusEntry,
       "fsStatusIndex": fsStatusIndex,
       "fsStatusName": fsStatusName,
       "fsStatusDeviceState": fsStatusDeviceState,
       "fsStatusVolumeValueString": fsStatusVolumeValueString,
       "fsStatusVolumePercentLevel": fsStatusVolumePercentLevel,
       "fsStatusVolumeInEventState": fsStatusVolumeInEventState,
       "fsStatusCombined": fsStatusCombined,
       "wirelessModemStatus": wirelessModemStatus,
       "wmsStatus": wmsStatus,
       "wmsSignal": wmsSignal,
       "wmsRSSI": wmsRSSI,
       "wmsBER": wmsBER,
       "wmsUpdated": wmsUpdated,
       "wmsRegistration": wmsRegistration,
       "wmsLAC": wmsLAC,
       "wmsCellID": wmsCellID,
       "wmsIMSI": wmsIMSI,
       "wmsPhnum": wmsPhnum,
       "wmsLocalIP": wmsLocalIP,
       "wmsMgfID": wmsMgfID,
       "wmsModelID": wmsModelID,
       "wmsIMEI": wmsIMEI,
       "wmsRevID": wmsRevID,
       "wmsNetName": wmsNetName,
       "wmsGPRSStatus": wmsGPRSStatus,
       "wmsBand": wmsBand,
       "wmsChannel": wmsChannel,
       "wmsCountryCode": wmsCountryCode,
       "wmsNetCode": wmsNetCode,
       "wmsPLMNColor": wmsPLMNColor,
       "wmsBScolor": wmsBScolor,
       "wmsMpRACH": wmsMpRACH,
       "wmsMinRxLevel": wmsMinRxLevel,
       "wmsBaseCoeff": wmsBaseCoeff,
       "wmsSIMStatus": wmsSIMStatus,
       "wmsICCID": wmsICCID,
       "wmsModemType": wmsModemType,
       "acPowerMonitorStatus": acPowerMonitorStatus,
       "acpmStatusTable": acpmStatusTable,
       "acpmStatusEntry": acpmStatusEntry,
       "acpmsIndex": acpmsIndex,
       "acpmsName": acpmsName,
       "acpmsAvgVoltageValueStr": acpmsAvgVoltageValueStr,
       "acpmsAvgVoltageMinStr": acpmsAvgVoltageMinStr,
       "acpmsAvgVoltageMaxStr": acpmsAvgVoltageMaxStr,
       "acpmsAvgVoltageAvgStr": acpmsAvgVoltageAvgStr,
       "acpmsAvgVoltageInEventState": acpmsAvgVoltageInEventState,
       "acpmsVoltagePhaseAValueStr": acpmsVoltagePhaseAValueStr,
       "acpmsVoltagePhaseBValueStr": acpmsVoltagePhaseBValueStr,
       "acpmsVoltagePhaseCValueStr": acpmsVoltagePhaseCValueStr,
       "acpmsAvgCurrentValueStr": acpmsAvgCurrentValueStr,
       "acpmsAvgCurrentMinStr": acpmsAvgCurrentMinStr,
       "acpmsAvgCurrentMaxStr": acpmsAvgCurrentMaxStr,
       "acpmsAvgCurrentAvgStr": acpmsAvgCurrentAvgStr,
       "acpmsAvgCurrentInEventState": acpmsAvgCurrentInEventState,
       "acpmsCurrentPhaseAValueStr": acpmsCurrentPhaseAValueStr,
       "acpmsCurrentPhaseBValueStr": acpmsCurrentPhaseBValueStr,
       "acpmsCurrentPhaseCValueStr": acpmsCurrentPhaseCValueStr,
       "acpmsAvgFreqValueStr": acpmsAvgFreqValueStr,
       "acpmsAvgFreqMinStr": acpmsAvgFreqMinStr,
       "acpmsAvgFreqMaxStr": acpmsAvgFreqMaxStr,
       "acpmsAvgFreqAvgStr": acpmsAvgFreqAvgStr,
       "acpmsAvgFreqInEventState": acpmsAvgFreqInEventState,
       "acpmsTRPValueStr": acpmsTRPValueStr,
       "acpmsTRPMinStr": acpmsTRPMinStr,
       "acpmsTRPMaxStr": acpmsTRPMaxStr,
       "acpmsTRPAvgStr": acpmsTRPAvgStr,
       "acpmsTRPInEventState": acpmsTRPInEventState,
       "acpmsRPPhaseAValueStr": acpmsRPPhaseAValueStr,
       "acpmsRPPhaseBValueStr": acpmsRPPhaseBValueStr,
       "acpmsRPPhaseCValueStr": acpmsRPPhaseCValueStr,
       "acpmsCombined": acpmsCombined,
       "acpmsTPFValueStr": acpmsTPFValueStr,
       "acpmsTPFMinStr": acpmsTPFMinStr,
       "acpmsTPFMaxStr": acpmsTPFMaxStr,
       "acpmsTPFAvgStr": acpmsTPFAvgStr,
       "acpmsTPFInEventState": acpmsTPFInEventState,
       "acpmsPFPhaseAValueStr": acpmsPFPhaseAValueStr,
       "acpmsPFPhaseBValueStr": acpmsPFPhaseBValueStr,
       "acpmsPFPhaseCValueStr": acpmsPFPhaseCValueStr,
       "acpmsTRcPValueStr": acpmsTRcPValueStr,
       "acpmsTRcPMinStr": acpmsTRcPMinStr,
       "acpmsTRcPMaxStr": acpmsTRcPMaxStr,
       "acpmsTRcPAvgStr": acpmsTRcPAvgStr,
       "acpmsRcPPhaseAValueStr": acpmsRcPPhaseAValueStr,
       "acpmsRcPPhaseBValueStr": acpmsRcPPhaseBValueStr,
       "acpmsRcPPhaseCValueStr": acpmsRcPPhaseCValueStr,
       "acpmsTAPValueStr": acpmsTAPValueStr,
       "acpmsTAPMinStr": acpmsTAPMinStr,
       "acpmsTAPMaxStr": acpmsTAPMaxStr,
       "acpmsTAPAvgStr": acpmsTAPAvgStr,
       "acpmsAPPhaseAValueStr": acpmsAPPhaseAValueStr,
       "acpmsAPPhaseBValueStr": acpmsAPPhaseBValueStr,
       "acpmsAPPhaseCValueStr": acpmsAPPhaseCValueStr,
       "acpmsTotalEnergyWh": acpmsTotalEnergyWh,
       "acpmsTotalEnergyVAR": acpmsTotalEnergyVAR,
       "acpmsTotalEnergyVA": acpmsTotalEnergyVA,
       "batteryMonitorStatus": batteryMonitorStatus,
       "bmStatusTable": bmStatusTable,
       "bmStatusEntry": bmStatusEntry,
       "bmsIndex": bmsIndex,
       "bmsEnable": bmsEnable,
       "bmsName": bmsName,
       "bmsState": bmsState,
       "bmsStringState": bmsStringState,
       "bmsTempValue": bmsTempValue,
       "bmsTempValueStr": bmsTempValueStr,
       "bmsTempEvent": bmsTempEvent,
       "bmsDiffTempValue": bmsDiffTempValue,
       "bmsDiffTempValueStr": bmsDiffTempValueStr,
       "bmsDiffTempEvent": bmsDiffTempEvent,
       "bmsVoltageValue": bmsVoltageValue,
       "bmsVoltageEvent": bmsVoltageEvent,
       "bmsDiffVoltValue": bmsDiffVoltValue,
       "bmsDiffVoltEvent": bmsDiffVoltEvent,
       "bmsCurrentValue": bmsCurrentValue,
       "bmsChargingCurrentEvent": bmsChargingCurrentEvent,
       "bmsDischargingCurrentEvent": bmsDischargingCurrentEvent,
       "bmsChargeLevelValue": bmsChargeLevelValue,
       "bmsChargeLevelEvent": bmsChargeLevelEvent,
       "bmsJarHealthValue": bmsJarHealthValue,
       "bmsJarHealthEvent": bmsJarHealthEvent,
       "bmsCombined": bmsCombined,
       "bmsJarStatusTable": bmsJarStatusTable,
       "bmJarStatusEntry": bmJarStatusEntry,
       "bmjsIndexBM": bmjsIndexBM,
       "bmjsIndexJar": bmjsIndexJar,
       "bmjsVoltageValue": bmjsVoltageValue,
       "bmjsTempValue": bmjsTempValue,
       "bmjsAdmittanceValue": bmjsAdmittanceValue,
       "bmjsAdmittanceChangeValue": bmjsAdmittanceChangeValue,
       "config": config,
       "eventSensorBasics": eventSensorBasics,
       "esNumberEventSensors": esNumberEventSensors,
       "esTable": esTable,
       "esEntry": esEntry,
       "esIndex": esIndex,
       "esName": esName,
       "esID": esID,
       "esNumberTempSensors": esNumberTempSensors,
       "esTempReportingMode": esTempReportingMode,
       "esNumberCCs": esNumberCCs,
       "esCCReportingMode": esCCReportingMode,
       "esNumberHumidSensors": esNumberHumidSensors,
       "esHumidReportingMode": esHumidReportingMode,
       "esNumberNoiseSensors": esNumberNoiseSensors,
       "esNoiseReportingMode": esNoiseReportingMode,
       "esNumberAirflowSensors": esNumberAirflowSensors,
       "esAirflowReportingMode": esAirflowReportingMode,
       "esNumberAnalog": esNumberAnalog,
       "esAnalogReportingMode": esAnalogReportingMode,
       "esNumberOutputs": esNumberOutputs,
       "esOutputReportingMode": esOutputReportingMode,
       "esTempCombinedStatus": esTempCombinedStatus,
       "esCCCombinedStatusBlock1": esCCCombinedStatusBlock1,
       "esCCCombinedStatusBlock2": esCCCombinedStatusBlock2,
       "esCCCombinedStatusBlock3": esCCCombinedStatusBlock3,
       "esCCCombinedStatusBlock4": esCCCombinedStatusBlock4,
       "esCCCombinedStatusBlock5": esCCCombinedStatusBlock5,
       "esCCCombinedStatusBlock6": esCCCombinedStatusBlock6,
       "esCCCombinedStatusBlock7": esCCCombinedStatusBlock7,
       "esCCCombinedStatusBlock8": esCCCombinedStatusBlock8,
       "esHumidCombinedStatus": esHumidCombinedStatus,
       "esAnalogCombinedStatusBlock1": esAnalogCombinedStatusBlock1,
       "esAnalogCombinedStatusBlock2": esAnalogCombinedStatusBlock2,
       "esAnalogCombinedStatusBlock3": esAnalogCombinedStatusBlock3,
       "esAnalogCombinedStatusBlock4": esAnalogCombinedStatusBlock4,
       "esAnalogCombinedStatusBlock5": esAnalogCombinedStatusBlock5,
       "esAnalogCombinedStatusBlock6": esAnalogCombinedStatusBlock6,
       "esOutputCombinedStatusBlock1": esOutputCombinedStatusBlock1,
       "esOutputCombinedStatusBlock2": esOutputCombinedStatusBlock2,
       "esNewSensors": esNewSensors,
       "eventSensorPointConfig": eventSensorPointConfig,
       "esPointConfigTempTable": esPointConfigTempTable,
       "esPointConfigTempEntry": esPointConfigTempEntry,
       "espcTempIndexES": espcTempIndexES,
       "espcTempIndexPoint": espcTempIndexPoint,
       "espcTempEnable": espcTempEnable,
       "espcTempScale": espcTempScale,
       "espcTempDeadband": espcTempDeadband,
       "espcTempVHighTemp": espcTempVHighTemp,
       "espcTempVHighActions": espcTempVHighActions,
       "espcTempVHighTrapnum": espcTempVHighTrapnum,
       "espcTempVHighClass": espcTempVHighClass,
       "espcTempHighTemp": espcTempHighTemp,
       "espcTempHighActions": espcTempHighActions,
       "espcTempHighTrapnum": espcTempHighTrapnum,
       "espcTempHighClass": espcTempHighClass,
       "espcTempNormalActions": espcTempNormalActions,
       "espcTempNormalTrapnum": espcTempNormalTrapnum,
       "espcTempNormalClass": espcTempNormalClass,
       "espcTempLowTemp": espcTempLowTemp,
       "espcTempLowActions": espcTempLowActions,
       "espcTempLowTrapnum": espcTempLowTrapnum,
       "espcTempLowClass": espcTempLowClass,
       "espcTempVLowTemp": espcTempVLowTemp,
       "espcTempVLowActions": espcTempVLowActions,
       "espcTempVLowTrapnum": espcTempVLowTrapnum,
       "espcTempVLowClass": espcTempVLowClass,
       "esPointConfigCCTable": esPointConfigCCTable,
       "esPointConfigCCEntry": esPointConfigCCEntry,
       "espcCCIndexES": espcCCIndexES,
       "espcCCIndexPoint": espcCCIndexPoint,
       "espcCCEnable": espcCCEnable,
       "espcCCName": espcCCName,
       "espcCCEventState": espcCCEventState,
       "espcCCThreshold": espcCCThreshold,
       "espcCCEventActions": espcCCEventActions,
       "espcCCEventTrapnum": espcCCEventTrapnum,
       "espcCCEventClass": espcCCEventClass,
       "espcCCNormalActions": espcCCNormalActions,
       "espcCCNormalTrapnum": espcCCNormalTrapnum,
       "espcCCNormalClass": espcCCNormalClass,
       "espcCCAlarmAlias": espcCCAlarmAlias,
       "espcCCNormalAlias": espcCCNormalAlias,
       "espcCCNormalThreshold": espcCCNormalThreshold,
       "espcCCOverrideGlobalReminder": espcCCOverrideGlobalReminder,
       "espcCCReminderInterval": espcCCReminderInterval,
       "esPointConfigHumidTable": esPointConfigHumidTable,
       "esPointConfigHumidEntry": esPointConfigHumidEntry,
       "espcHumidIndexES": espcHumidIndexES,
       "espcHumidIndexPoint": espcHumidIndexPoint,
       "espcHumidEnable": espcHumidEnable,
       "espcHumidDeadband": espcHumidDeadband,
       "espcHumidVHighHumid": espcHumidVHighHumid,
       "espcHumidVHighActions": espcHumidVHighActions,
       "espcHumidVHighTrapnum": espcHumidVHighTrapnum,
       "espcHumidVHighClass": espcHumidVHighClass,
       "espcHumidHighHumid": espcHumidHighHumid,
       "espcHumidHighActions": espcHumidHighActions,
       "espcHumidHighTrapnum": espcHumidHighTrapnum,
       "espcHumidHighClass": espcHumidHighClass,
       "espcHumidNormalActions": espcHumidNormalActions,
       "espcHumidNormalTrapnum": espcHumidNormalTrapnum,
       "espcHumidNormalClass": espcHumidNormalClass,
       "espcHumidLowHumid": espcHumidLowHumid,
       "espcHumidLowActions": espcHumidLowActions,
       "espcHumidLowTrapnum": espcHumidLowTrapnum,
       "espcHumidLowClass": espcHumidLowClass,
       "espcHumidVLowHumid": espcHumidVLowHumid,
       "espcHumidVLowActions": espcHumidVLowActions,
       "espcHumidVLowTrapnum": espcHumidVLowTrapnum,
       "espcHumidVLowClass": espcHumidVLowClass,
       "esPointConfigAITable": esPointConfigAITable,
       "esPointConfigAIEntry": esPointConfigAIEntry,
       "espcAIIndexES": espcAIIndexES,
       "espcAIIndexPoint": espcAIIndexPoint,
       "espcAIEnable": espcAIEnable,
       "espcAIDeadband": espcAIDeadband,
       "espcAIVhighValue": espcAIVhighValue,
       "espcAIVhighActions": espcAIVhighActions,
       "espcAIVhighTrapnum": espcAIVhighTrapnum,
       "espcAIVhighClass": espcAIVhighClass,
       "espcAIHighValue": espcAIHighValue,
       "espcAIHighActions": espcAIHighActions,
       "espcAIHighTrapnum": espcAIHighTrapnum,
       "espcAIHighClass": espcAIHighClass,
       "espcAINormalActions": espcAINormalActions,
       "espcAINormalTrapnum": espcAINormalTrapnum,
       "espcAINormalClass": espcAINormalClass,
       "espcAILowValue": espcAILowValue,
       "espcAILowActions": espcAILowActions,
       "espcAILowTrapnum": espcAILowTrapnum,
       "espcAILowClass": espcAILowClass,
       "espcAIVlowValue": espcAIVlowValue,
       "espcAIVlowActions": espcAIVlowActions,
       "espcAIVlowTrapnum": espcAIVlowTrapnum,
       "espcAIVlowClass": espcAIVlowClass,
       "espcAIConvUnitName": espcAIConvUnitName,
       "espcAIConvHighValue": espcAIConvHighValue,
       "espcAIConvHighUnit": espcAIConvHighUnit,
       "espcAIConvLowValue": espcAIConvLowValue,
       "espcAIConvLowUnit": espcAIConvLowUnit,
       "espcAIDisplayFormat": espcAIDisplayFormat,
       "esPointConfigOutputTable": esPointConfigOutputTable,
       "esPointConfigOutputEntry": esPointConfigOutputEntry,
       "espcOutputIndexES": espcOutputIndexES,
       "espcOutputIndexPoint": espcOutputIndexPoint,
       "espcOutputEnable": espcOutputEnable,
       "espcOutputActiveState": espcOutputActiveState,
       "espcOutputType": espcOutputType,
       "espcOutputAliasValue": espcOutputAliasValue,
       "espcOutputAliasColor": espcOutputAliasColor,
       "espcOutputActiveAlias": espcOutputActiveAlias,
       "espcOutputActiveColor": espcOutputActiveColor,
       "espcOutputActiveActions": espcOutputActiveActions,
       "espcOutputActiveTrapnum": espcOutputActiveTrapnum,
       "espcOutputActiveClass": espcOutputActiveClass,
       "espcOutputInactiveAlias": espcOutputInactiveAlias,
       "espcOutputInactiveColor": espcOutputInactiveColor,
       "espcOutputInactiveActions": espcOutputInactiveActions,
       "espcOutputInactiveTrapnum": espcOutputInactiveTrapnum,
       "espcOutputInactiveClass": espcOutputInactiveClass,
       "serialPorts": serialPorts,
       "numberPorts": numberPorts,
       "portConfigTable": portConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigIndex": portConfigIndex,
       "portConfigBaud": portConfigBaud,
       "portConfigDataFormat": portConfigDataFormat,
       "portConfigStripPtOutputLfs": portConfigStripPtOutputLfs,
       "portConfigStripPtInputLfs": portConfigStripPtInputLfs,
       "portConfigId": portConfigId,
       "portConfigMode": portConfigMode,
       "portConfigHsk": portConfigHsk,
       "network": network,
       "interface": interface,
       "ethernet": ethernet,
       "ethernet1": ethernet1,
       "eth1Mode": eth1Mode,
       "eth1Address": eth1Address,
       "eth1SubnetMask": eth1SubnetMask,
       "eth1Router": eth1Router,
       "eth1VLAN": eth1VLAN,
       "eth1VLAN1": eth1VLAN1,
       "eth1VLAN1ID": eth1VLAN1ID,
       "eth1VLAN1Priority": eth1VLAN1Priority,
       "eth1VLAN1Address": eth1VLAN1Address,
       "eth1VLAN1SubnetMask": eth1VLAN1SubnetMask,
       "eth1VLAN1Router": eth1VLAN1Router,
       "eth1VLAN2": eth1VLAN2,
       "eth1VLAN2ID": eth1VLAN2ID,
       "eth1VLAN2Priority": eth1VLAN2Priority,
       "eth1VLAN2Address": eth1VLAN2Address,
       "eth1VLAN2SubnetMask": eth1VLAN2SubnetMask,
       "eth1VLAN2Router": eth1VLAN2Router,
       "eth1VLAN3": eth1VLAN3,
       "eth1VLAN3ID": eth1VLAN3ID,
       "eth1VLAN3Priority": eth1VLAN3Priority,
       "eth1VLAN3Address": eth1VLAN3Address,
       "eth1VLAN3SubnetMask": eth1VLAN3SubnetMask,
       "eth1VLAN3Router": eth1VLAN3Router,
       "eth1VLAN4": eth1VLAN4,
       "eth1VLAN4ID": eth1VLAN4ID,
       "eth1VLAN4Priority": eth1VLAN4Priority,
       "eth1VLAN4Address": eth1VLAN4Address,
       "eth1VLAN4SubnetMask": eth1VLAN4SubnetMask,
       "eth1VLAN4Router": eth1VLAN4Router,
       "eth1VLAN5": eth1VLAN5,
       "eth1VLAN5ID": eth1VLAN5ID,
       "eth1VLAN5Priority": eth1VLAN5Priority,
       "eth1VLAN5Address": eth1VLAN5Address,
       "eth1VLAN5SubnetMask": eth1VLAN5SubnetMask,
       "eth1VLAN5Router": eth1VLAN5Router,
       "eth1VLAN6": eth1VLAN6,
       "eth1VLAN6ID": eth1VLAN6ID,
       "eth1VLAN6Priority": eth1VLAN6Priority,
       "eth1VLAN6Address": eth1VLAN6Address,
       "eth1VLAN6SubnetMask": eth1VLAN6SubnetMask,
       "eth1VLAN6Router": eth1VLAN6Router,
       "eth1MAC": eth1MAC,
       "eth1IPv6": eth1IPv6,
       "eth1IPv6Mode": eth1IPv6Mode,
       "eth1IPv6Static": eth1IPv6Static,
       "eth1IPv6StaticAddress": eth1IPv6StaticAddress,
       "eth1IPv6StaticRouter": eth1IPv6StaticRouter,
       "eth1IPv6Auto": eth1IPv6Auto,
       "eth1IPv6AutoAddress1": eth1IPv6AutoAddress1,
       "eth1IPv6AutoAddress2": eth1IPv6AutoAddress2,
       "eth1IPv6AutoAddress3": eth1IPv6AutoAddress3,
       "eth1IPv6AutoAddress4": eth1IPv6AutoAddress4,
       "eth1IPv6LinkLocalAddress": eth1IPv6LinkLocalAddress,
       "ethernet2": ethernet2,
       "eth2Mode": eth2Mode,
       "eth2Address": eth2Address,
       "eth2SubnetMask": eth2SubnetMask,
       "eth2Router": eth2Router,
       "eth2VLAN": eth2VLAN,
       "eth2VLAN1": eth2VLAN1,
       "eth2VLAN1ID": eth2VLAN1ID,
       "eth2VLAN1Priority": eth2VLAN1Priority,
       "eth2VLAN1Address": eth2VLAN1Address,
       "eth2VLAN1SubnetMask": eth2VLAN1SubnetMask,
       "eth2VLAN1Router": eth2VLAN1Router,
       "eth2VLAN2": eth2VLAN2,
       "eth2VLAN2ID": eth2VLAN2ID,
       "eth2VLAN2Priority": eth2VLAN2Priority,
       "eth2VLAN2Address": eth2VLAN2Address,
       "eth2VLAN2SubnetMask": eth2VLAN2SubnetMask,
       "eth2VLAN2Router": eth2VLAN2Router,
       "eth2VLAN3": eth2VLAN3,
       "eth2VLAN3ID": eth2VLAN3ID,
       "eth2VLAN3Priority": eth2VLAN3Priority,
       "eth2VLAN3Address": eth2VLAN3Address,
       "eth2VLAN3SubnetMask": eth2VLAN3SubnetMask,
       "eth2VLAN3Router": eth2VLAN3Router,
       "eth2VLAN4": eth2VLAN4,
       "eth2VLAN4ID": eth2VLAN4ID,
       "eth2VLAN4Priority": eth2VLAN4Priority,
       "eth2VLAN4Address": eth2VLAN4Address,
       "eth2VLAN4SubnetMask": eth2VLAN4SubnetMask,
       "eth2VLAN4Router": eth2VLAN4Router,
       "eth2VLAN5": eth2VLAN5,
       "eth2VLAN5ID": eth2VLAN5ID,
       "eth2VLAN5Priority": eth2VLAN5Priority,
       "eth2VLAN5Address": eth2VLAN5Address,
       "eth2VLAN5SubnetMask": eth2VLAN5SubnetMask,
       "eth2VLAN5Router": eth2VLAN5Router,
       "eth2VLAN6": eth2VLAN6,
       "eth2VLAN6ID": eth2VLAN6ID,
       "eth2VLAN6Priority": eth2VLAN6Priority,
       "eth2VLAN6Address": eth2VLAN6Address,
       "eth2VLAN6SubnetMask": eth2VLAN6SubnetMask,
       "eth2VLAN6Router": eth2VLAN6Router,
       "eth2MAC": eth2MAC,
       "eth2IPv6": eth2IPv6,
       "eth2IPv6Mode": eth2IPv6Mode,
       "eth2IPv6Static": eth2IPv6Static,
       "eth2IPv6StaticAddress": eth2IPv6StaticAddress,
       "eth2IPv6StaticRouter": eth2IPv6StaticRouter,
       "eth2IPv6Auto": eth2IPv6Auto,
       "eth2IPv6AutoAddress1": eth2IPv6AutoAddress1,
       "eth2IPv6AutoAddress2": eth2IPv6AutoAddress2,
       "eth2IPv6AutoAddress3": eth2IPv6AutoAddress3,
       "eth2IPv6AutoAddress4": eth2IPv6AutoAddress4,
       "eth2IPv6LinkLocalAddress": eth2IPv6LinkLocalAddress,
       "defaultRouter": defaultRouter,
       "dnsTable": dnsTable,
       "dnsEntry": dnsEntry,
       "dnsIndex": dnsIndex,
       "dnsAddress": dnsAddress,
       "hostname": hostname,
       "hostTable": hostTable,
       "hostEntry": hostEntry,
       "hostIndex": hostIndex,
       "hostDeclaration": hostDeclaration,
       "ncpDuplex": ncpDuplex,
       "ncpTimeout": ncpTimeout,
       "snmp": snmp,
       "snmpAgentEnable": snmpAgentEnable,
       "snmpNotificationTx": snmpNotificationTx,
       "snmpNtfnAttempts": snmpNtfnAttempts,
       "snmpNtfnTimeout": snmpNtfnTimeout,
       "snmpNtfnCycles": snmpNtfnCycles,
       "snmpNtfnSnooze": snmpNtfnSnooze,
       "snmpProxy": snmpProxy,
       "snmpProxyTable": snmpProxyTable,
       "snmpProxyEntry": snmpProxyEntry,
       "snmpProxyIndex": snmpProxyIndex,
       "snmpProxyEgressOIDBranch": snmpProxyEgressOIDBranch,
       "snmpProxyIP": snmpProxyIP,
       "snmpProxyPort": snmpProxyPort,
       "snmpProxyIngressOIDBranch": snmpProxyIngressOIDBranch,
       "snmpProxyName": snmpProxyName,
       "snmpPoll": snmpPoll,
       "snmpPMode": snmpPMode,
       "snmpPRequestTable": snmpPRequestTable,
       "snmpPRequestEntry": snmpPRequestEntry,
       "snmpPRequestIndex": snmpPRequestIndex,
       "snmpPRequestDescription": snmpPRequestDescription,
       "snmpPRequestAgent": snmpPRequestAgent,
       "snmpPRequestReadcom": snmpPRequestReadcom,
       "snmpPRequestOID": snmpPRequestOID,
       "snmpPRequestPeriod": snmpPRequestPeriod,
       "snmpPRequestResultStatus": snmpPRequestResultStatus,
       "snmpPRequestResultValue": snmpPRequestResultValue,
       "snmpPRequestResultTime": snmpPRequestResultTime,
       "snmpPRequestResultType": snmpPRequestResultType,
       "ftpPush": ftpPush,
       "ftpPushEnable": ftpPushEnable,
       "ftpPushServer": ftpPushServer,
       "ftpPushAccount": ftpPushAccount,
       "ftpPushDirectory": ftpPushDirectory,
       "ftpPushperiod": ftpPushperiod,
       "ftpPushPushFileTable": ftpPushPushFileTable,
       "ftpPushPushFileEntry": ftpPushPushFileEntry,
       "ftpPushPushFileIndex": ftpPushPushFileIndex,
       "ftpPushPushFile": ftpPushPushFile,
       "ftpPushPushAudit": ftpPushPushAudit,
       "ftpPushPushAlarms": ftpPushPushAlarms,
       "ftpPushRemoteFileTable": ftpPushRemoteFileTable,
       "ftpPushRemoteFileEntry": ftpPushRemoteFileEntry,
       "ftpPushRemoteFileIndex": ftpPushRemoteFileIndex,
       "ftpPushRemoteFileName": ftpPushRemoteFileName,
       "ftpPushRemoteAlarmName": ftpPushRemoteAlarmName,
       "ftpPushPassive": ftpPushPassive,
       "ftpPushIncludeDate": ftpPushIncludeDate,
       "ftpPushIncludeTime": ftpPushIncludeTime,
       "ftpPushIncludeSeq": ftpPushIncludeSeq,
       "ftpPushPermissions": ftpPushPermissions,
       "routing": routing,
       "ethRoutingEnable": ethRoutingEnable,
       "ethRoutingNATEnable": ethRoutingNATEnable,
       "netSecurity": netSecurity,
       "ipRestriction": ipRestriction,
       "ipRestrictionTable": ipRestrictionTable,
       "ipRestrictionEntry": ipRestrictionEntry,
       "ipRestrictionIndex": ipRestrictionIndex,
       "ipRestrictionEnable": ipRestrictionEnable,
       "ipRestrictionMask": ipRestrictionMask,
       "trap": trap,
       "trapInclude": trapInclude,
       "trapIncludeDateTime": trapIncludeDateTime,
       "trapIncludeSiteName": trapIncludeSiteName,
       "trapIncludeSensorID": trapIncludeSensorID,
       "trapIncludeUDName": trapIncludeUDName,
       "trapIncludeUDState": trapIncludeUDState,
       "trapIncludeSourceAddress": trapIncludeSourceAddress,
       "trapAuthFailEnable": trapAuthFailEnable,
       "wireless": wireless,
       "wirelessMode": wirelessMode,
       "wirelessAPN": wirelessAPN,
       "wirelessIdleTimeout": wirelessIdleTimeout,
       "wirelessPIN": wirelessPIN,
       "wirelessDRE": wirelessDRE,
       "wirelessPPPUsername": wirelessPPPUsername,
       "wirelessFirewall": wirelessFirewall,
       "wirelessKeepaliveThreshold": wirelessKeepaliveThreshold,
       "wirelessPPPDebug": wirelessPPPDebug,
       "wirelessConnectivity": wirelessConnectivity,
       "wirelessConnEnable": wirelessConnEnable,
       "wirelessConnCheckInterval": wirelessConnCheckInterval,
       "wirelessConnFailThreshold": wirelessConnFailThreshold,
       "wirelessConnIP1": wirelessConnIP1,
       "wirelessConnIP2": wirelessConnIP2,
       "email": email,
       "emailServer": emailServer,
       "emailDomain": emailDomain,
       "emailAuthEnable": emailAuthEnable,
       "netAdvanced": netAdvanced,
       "arpFilter": arpFilter,
       "web": web,
       "webEnable": webEnable,
       "webPort": webPort,
       "webTimeout": webTimeout,
       "ipv6": ipv6,
       "ipv6DefaultRouter": ipv6DefaultRouter,
       "cpe": cpe,
       "cpeTable": cpeTable,
       "cpeEntry": cpeEntry,
       "cpeIndex": cpeIndex,
       "cpeHost": cpeHost,
       "cpeName": cpeName,
       "cpeDescription": cpeDescription,
       "cpeKeepalive": cpeKeepalive,
       "cpeThreshold": cpeThreshold,
       "cpeEventReminderInterval": cpeEventReminderInterval,
       "cpeKeepaliveTicks": cpeKeepaliveTicks,
       "cpePingSize": cpePingSize,
       "cpeInfoReset": cpeInfoReset,
       "cpeInfoNumReq": cpeInfoNumReq,
       "cpeInfoNumGoodResp": cpeInfoNumGoodResp,
       "cpeInfoNumBadResp": cpeInfoNumBadResp,
       "cpeInfoNumLostResp": cpeInfoNumLostResp,
       "cpeInfoPercentLoss": cpeInfoPercentLoss,
       "cpeInfoPercentBad": cpeInfoPercentBad,
       "time": time,
       "clock": clock,
       "console": console,
       "consoleDuplex": consoleDuplex,
       "consoleTimeout": consoleTimeout,
       "consoleConfirm": consoleConfirm,
       "unitSecurity": unitSecurity,
       "secCore": secCore,
       "scShowPasswordPrompt": scShowPasswordPrompt,
       "scConsoleLoginRequired": scConsoleLoginRequired,
       "scAuthMode": scAuthMode,
       "scRightsGroup": scRightsGroup,
       "scSecret": scSecret,
       "secUserTable": secUserTable,
       "secUserEntry": secUserEntry,
       "secUserIndex": secUserIndex,
       "secUserEnable": secUserEnable,
       "secUserConnectVia": secUserConnectVia,
       "secUserLoginTo": secUserLoginTo,
       "secUserAccessFile": secUserAccessFile,
       "secUserPTEscapeTo": secUserPTEscapeTo,
       "secUserRights": secUserRights,
       "secUserEventsReadAccess": secUserEventsReadAccess,
       "secUserAuditReadAccess": secUserAuditReadAccess,
       "secUserEventsWriteAccess": secUserEventsWriteAccess,
       "secUserAuditWriteAccess": secUserAuditWriteAccess,
       "secUserExpiration": secUserExpiration,
       "secUserChallengeConsoleMode": secUserChallengeConsoleMode,
       "secUserChallengeExpiration": secUserChallengeExpiration,
       "secFactory": secFactory,
       "sfEnable": sfEnable,
       "sfSecret": sfSecret,
       "event": event,
       "evCore": evCore,
       "evClassNameTable": evClassNameTable,
       "evClassNameEntry": evClassNameEntry,
       "evClassNameIndex": evClassNameIndex,
       "evClassName": evClassName,
       "evReminderInterval": evReminderInterval,
       "evLog": evLog,
       "evLogEnable": evLogEnable,
       "evLogStoreAlarm": evLogStoreAlarm,
       "evLogMaxSize": evLogMaxSize,
       "evLogStoreSensor": evLogStoreSensor,
       "evLogTimeStampAlarms": evLogTimeStampAlarms,
       "evLogPrependName": evLogPrependName,
       "evMgmt": evMgmt,
       "evMgmtReprocess": evMgmtReprocess,
       "evSched1": evSched1,
       "evSched1Enable": evSched1Enable,
       "evSched1Actions": evSched1Actions,
       "evSched1Message": evSched1Message,
       "evSched1TrapNum": evSched1TrapNum,
       "evSched1Class": evSched1Class,
       "evSched1Sunday": evSched1Sunday,
       "evSched1Monday": evSched1Monday,
       "evSched1Tuesday": evSched1Tuesday,
       "evSched1Wednesday": evSched1Wednesday,
       "evSched1Thursday": evSched1Thursday,
       "evSched1Friday": evSched1Friday,
       "evSched1Saturday": evSched1Saturday,
       "evSched1Exclusions": evSched1Exclusions,
       "evSched2": evSched2,
       "evSched2Enable": evSched2Enable,
       "evSched2Actions": evSched2Actions,
       "evSched2Message": evSched2Message,
       "evSched2TrapNum": evSched2TrapNum,
       "evSched2Class": evSched2Class,
       "evSched2Sunday": evSched2Sunday,
       "evSched2Monday": evSched2Monday,
       "evSched2Tuesday": evSched2Tuesday,
       "evSched2Wednesday": evSched2Wednesday,
       "evSched2Thursday": evSched2Thursday,
       "evSched2Friday": evSched2Friday,
       "evSched2Saturday": evSched2Saturday,
       "evSched2Exclusions": evSched2Exclusions,
       "evShskLowTable": evShskLowTable,
       "evShskLowEntry": evShskLowEntry,
       "evShskLowIndex": evShskLowIndex,
       "evShskLowEnable": evShskLowEnable,
       "evShskLowActions": evShskLowActions,
       "evShskLowMessage": evShskLowMessage,
       "evShskLowClass": evShskLowClass,
       "evShskLowTrapNum": evShskLowTrapNum,
       "evShskHighTable": evShskHighTable,
       "evShskHighEntry": evShskHighEntry,
       "evShskHighIndex": evShskHighIndex,
       "evShskHighEnable": evShskHighEnable,
       "evShskHighActions": evShskHighActions,
       "evShskHighMessage": evShskHighMessage,
       "evShskHighClass": evShskHighClass,
       "evShskHighTrapNum": evShskHighTrapNum,
       "evNoSensor": evNoSensor,
       "evNoSensorTimeout": evNoSensorTimeout,
       "evNoSensorActions": evNoSensorActions,
       "evNoSensorTrapNum": evNoSensorTrapNum,
       "evNoSensorClass": evNoSensorClass,
       "fuelSensor": fuelSensor,
       "fuelSensorGeneralTable": fuelSensorGeneralTable,
       "fsGenEntry": fsGenEntry,
       "fsGenIndex": fsGenIndex,
       "fsGenName": fsGenName,
       "fsGenSensorType": fsGenSensorType,
       "fsGenDistanceUnit": fsGenDistanceUnit,
       "fsGenRawValueTop": fsGenRawValueTop,
       "fsGenTopOffset": fsGenTopOffset,
       "fsGenRawValueBottom": fsGenRawValueBottom,
       "fsGenBottomOffset": fsGenBottomOffset,
       "fsGenInputES": fsGenInputES,
       "fsGenInputPoint": fsGenInputPoint,
       "fsGenFilterAveraging": fsGenFilterAveraging,
       "fsGenSysrepEnable": fsGenSysrepEnable,
       "fsGenSysrepThreshold": fsGenSysrepThreshold,
       "fsGenSysrepLimit": fsGenSysrepLimit,
       "fsGenSysrepPackage": fsGenSysrepPackage,
       "fsGenSysrepType": fsGenSysrepType,
       "fsGenEnable": fsGenEnable,
       "fuelSensorTankTable": fuelSensorTankTable,
       "fsTankEntry": fsTankEntry,
       "fsTankIndex": fsTankIndex,
       "fsTankHeight": fsTankHeight,
       "fsTankDimA": fsTankDimA,
       "fsTankDimB": fsTankDimB,
       "fsTankVolume": fsTankVolume,
       "fsTankVolumeUnit": fsTankVolumeUnit,
       "fsTankShape": fsTankShape,
       "fuelSensorCustomTankTable": fuelSensorCustomTankTable,
       "fsCustomTankEntry": fsCustomTankEntry,
       "fsCustomTankIndexFS": fsCustomTankIndexFS,
       "fsCustomTankIndexDatum": fsCustomTankIndexDatum,
       "fsCustomTankHeight": fsCustomTankHeight,
       "fsCustomTankVolume": fsCustomTankVolume,
       "fuelSensorVolumeTable": fuelSensorVolumeTable,
       "fsVolumeEntry": fsVolumeEntry,
       "fsVolumeIndex": fsVolumeIndex,
       "fsVolumeEnable": fsVolumeEnable,
       "fsVolumeDeadband": fsVolumeDeadband,
       "fsVolumeVHighValue": fsVolumeVHighValue,
       "fsVolumeVHighActions": fsVolumeVHighActions,
       "fsVolumeVHighTrapNum": fsVolumeVHighTrapNum,
       "fsVolumeVHighClass": fsVolumeVHighClass,
       "fsVolumeHighValue": fsVolumeHighValue,
       "fsVolumeHighActions": fsVolumeHighActions,
       "fsVolumeHighTrapNum": fsVolumeHighTrapNum,
       "fsVolumeHighClass": fsVolumeHighClass,
       "fsVolumeNormalActions": fsVolumeNormalActions,
       "fsVolumeNormalTrapNum": fsVolumeNormalTrapNum,
       "fsVolumeNormalClass": fsVolumeNormalClass,
       "fsVolumeLowValue": fsVolumeLowValue,
       "fsVolumeLowActions": fsVolumeLowActions,
       "fsVolumeLowTrapNum": fsVolumeLowTrapNum,
       "fsVolumeLowClass": fsVolumeLowClass,
       "fsVolumeVLowValue": fsVolumeVLowValue,
       "fsVolumeVLowActions": fsVolumeVLowActions,
       "fsVolumeVLowTrapNum": fsVolumeVLowTrapNum,
       "fsVolumeVLowClass": fsVolumeVLowClass,
       "fuelSensorDisconnectTable": fuelSensorDisconnectTable,
       "fsDiscEntry": fsDiscEntry,
       "fsDiscIndex": fsDiscIndex,
       "fsDiscEnable": fsDiscEnable,
       "fsDiscHighValue": fsDiscHighValue,
       "fsDiscLowValue": fsDiscLowValue,
       "fsDiscActions": fsDiscActions,
       "fsDiscTrapNum": fsDiscTrapNum,
       "fsDiscClass": fsDiscClass,
       "fsDiscNormalActions": fsDiscNormalActions,
       "fsDiscNormalTrapNum": fsDiscNormalTrapNum,
       "fsDiscNormalClass": fsDiscNormalClass,
       "fuelSensorSuddenChangeTable": fuelSensorSuddenChangeTable,
       "fsSuddenChangeEntry": fsSuddenChangeEntry,
       "fsSuddenChangeIndex": fsSuddenChangeIndex,
       "fsSuddenChangeEnable": fsSuddenChangeEnable,
       "fsSuddenChangeTime": fsSuddenChangeTime,
       "fsSuddenChangeAmplitude": fsSuddenChangeAmplitude,
       "fsSuddenChangeActions": fsSuddenChangeActions,
       "fsSuddenChangeTrapNum": fsSuddenChangeTrapNum,
       "fsSuddenChangeClass": fsSuddenChangeClass,
       "fuelSensorSlowChangeTable": fuelSensorSlowChangeTable,
       "fsSlowChangeEntry": fsSlowChangeEntry,
       "fsSlowChangeIndex": fsSlowChangeIndex,
       "fsSlowChangeEnable": fsSlowChangeEnable,
       "fsSlowChangeTime": fsSlowChangeTime,
       "fsSlowChangeAmplitude": fsSlowChangeAmplitude,
       "fsSlowChangeActions": fsSlowChangeActions,
       "fsSlowChangeTrapNum": fsSlowChangeTrapNum,
       "fsSlowChangeClass": fsSlowChangeClass,
       "fuelSensorLevelsAutoAdjustTable": fuelSensorLevelsAutoAdjustTable,
       "fsLAAEntry": fsLAAEntry,
       "fsLAAIndex": fsLAAIndex,
       "fsLAAEnable": fsLAAEnable,
       "fsLAAEventEnable": fsLAAEventEnable,
       "fsLAAEventThreshold": fsLAAEventThreshold,
       "fsLAAEventActions": fsLAAEventActions,
       "fsLAAEventClass": fsLAAEventClass,
       "fsLAAEventTrapNum": fsLAAEventTrapNum,
       "acPowerMonitor": acPowerMonitor,
       "acpmGeneralTable": acpmGeneralTable,
       "acpmGenEntry": acpmGenEntry,
       "acpmGenIndex": acpmGenIndex,
       "acpmGenDevice": acpmGenDevice,
       "acpmGenName": acpmGenName,
       "acpmGenAddress": acpmGenAddress,
       "acpmGenPtRatio": acpmGenPtRatio,
       "acpmGenCtRatio": acpmGenCtRatio,
       "acpmGenPowerType": acpmGenPowerType,
       "acpmGenSysrepPackage": acpmGenSysrepPackage,
       "acpmGenSysrepType": acpmGenSysrepType,
       "acpmGenEnable": acpmGenEnable,
       "acpmAvgVoltageTable": acpmAvgVoltageTable,
       "acpmAvgVoltageEntry": acpmAvgVoltageEntry,
       "acpmAvgVoltageIndex": acpmAvgVoltageIndex,
       "acpmAvgVoltageEnable": acpmAvgVoltageEnable,
       "acpmAvgVoltageDeadband": acpmAvgVoltageDeadband,
       "acpmAvgVoltageVHighValue": acpmAvgVoltageVHighValue,
       "acpmAvgVoltageVHighActions": acpmAvgVoltageVHighActions,
       "acpmAvgVoltageVHighTrapNum": acpmAvgVoltageVHighTrapNum,
       "acpmAvgVoltageVHighClass": acpmAvgVoltageVHighClass,
       "acpmAvgVoltageHighValue": acpmAvgVoltageHighValue,
       "acpmAvgVoltageHighActions": acpmAvgVoltageHighActions,
       "acpmAvgVoltageHighTrapNum": acpmAvgVoltageHighTrapNum,
       "acpmAvgVoltageHighClass": acpmAvgVoltageHighClass,
       "acpmAvgVoltageNormalActions": acpmAvgVoltageNormalActions,
       "acpmAvgVoltageNormalTrapNum": acpmAvgVoltageNormalTrapNum,
       "acpmAvgVoltageNormalClass": acpmAvgVoltageNormalClass,
       "acpmAvgVoltageLowValue": acpmAvgVoltageLowValue,
       "acpmAvgVoltageLowActions": acpmAvgVoltageLowActions,
       "acpmAvgVoltageLowTrapNum": acpmAvgVoltageLowTrapNum,
       "acpmAvgVoltageLowClass": acpmAvgVoltageLowClass,
       "acpmAvgVoltageVLowValue": acpmAvgVoltageVLowValue,
       "acpmAvgVoltageVLowActions": acpmAvgVoltageVLowActions,
       "acpmAvgVoltageVLowTrapNum": acpmAvgVoltageVLowTrapNum,
       "acpmAvgVoltageVLowClass": acpmAvgVoltageVLowClass,
       "acpmAvgVoltageSysrepEnable": acpmAvgVoltageSysrepEnable,
       "acpmAvgVoltageSysrepThreshold": acpmAvgVoltageSysrepThreshold,
       "acpmAvgVoltageSysrepLimit": acpmAvgVoltageSysrepLimit,
       "acpmAvgCurrentTable": acpmAvgCurrentTable,
       "acpmAvgCurrentEntry": acpmAvgCurrentEntry,
       "acpmAvgCurrentIndex": acpmAvgCurrentIndex,
       "acpmAvgCurrentEnable": acpmAvgCurrentEnable,
       "acpmAvgCurrentDeadband": acpmAvgCurrentDeadband,
       "acpmAvgCurrentVHighValue": acpmAvgCurrentVHighValue,
       "acpmAvgCurrentVHighActions": acpmAvgCurrentVHighActions,
       "acpmAvgCurrentVHighTrapNum": acpmAvgCurrentVHighTrapNum,
       "acpmAvgCurrentVHighClass": acpmAvgCurrentVHighClass,
       "acpmAvgCurrentHighValue": acpmAvgCurrentHighValue,
       "acpmAvgCurrentHighActions": acpmAvgCurrentHighActions,
       "acpmAvgCurrentHighTrapNum": acpmAvgCurrentHighTrapNum,
       "acpmAvgCurrentHighClass": acpmAvgCurrentHighClass,
       "acpmAvgCurrentNormalActions": acpmAvgCurrentNormalActions,
       "acpmAvgCurrentNormalTrapNum": acpmAvgCurrentNormalTrapNum,
       "acpmAvgCurrentNormalClass": acpmAvgCurrentNormalClass,
       "acpmAvgCurrentLowValue": acpmAvgCurrentLowValue,
       "acpmAvgCurrentLowActions": acpmAvgCurrentLowActions,
       "acpmAvgCurrentLowTrapNum": acpmAvgCurrentLowTrapNum,
       "acpmAvgCurrentLowClass": acpmAvgCurrentLowClass,
       "acpmAvgCurrentVLowValue": acpmAvgCurrentVLowValue,
       "acpmAvgCurrentVLowActions": acpmAvgCurrentVLowActions,
       "acpmAvgCurrentVLowTrapNum": acpmAvgCurrentVLowTrapNum,
       "acpmAvgCurrentVLowClass": acpmAvgCurrentVLowClass,
       "acpmAvgCurrentSysrepEnable": acpmAvgCurrentSysrepEnable,
       "acpmAvgCurrentSysrepThreshold": acpmAvgCurrentSysrepThreshold,
       "acpmAvgCurrentSysrepLimit": acpmAvgCurrentSysrepLimit,
       "acpmFreqTable": acpmFreqTable,
       "acpmFreqEntry": acpmFreqEntry,
       "acpmFreqIndex": acpmFreqIndex,
       "acpmFreqEnable": acpmFreqEnable,
       "acpmFreqDeadband": acpmFreqDeadband,
       "acpmFreqVHighValue": acpmFreqVHighValue,
       "acpmFreqVHighActions": acpmFreqVHighActions,
       "acpmFreqVHighTrapNum": acpmFreqVHighTrapNum,
       "acpmFreqVHighClass": acpmFreqVHighClass,
       "acpmFreqHighValue": acpmFreqHighValue,
       "acpmFreqHighActions": acpmFreqHighActions,
       "acpmFreqHighTrapNum": acpmFreqHighTrapNum,
       "acpmFreqHighClass": acpmFreqHighClass,
       "acpmFreqNormalActions": acpmFreqNormalActions,
       "acpmFreqNormalTrapNum": acpmFreqNormalTrapNum,
       "acpmFreqNormalClass": acpmFreqNormalClass,
       "acpmFreqLowValue": acpmFreqLowValue,
       "acpmFreqLowActions": acpmFreqLowActions,
       "acpmFreqLowTrapNum": acpmFreqLowTrapNum,
       "acpmFreqLowClass": acpmFreqLowClass,
       "acpmFreqVLowValue": acpmFreqVLowValue,
       "acpmFreqVLowActions": acpmFreqVLowActions,
       "acpmFreqVLowTrapNum": acpmFreqVLowTrapNum,
       "acpmFreqVLowClass": acpmFreqVLowClass,
       "acpmFreqSysrepEnable": acpmFreqSysrepEnable,
       "acpmFreqSysrepThreshold": acpmFreqSysrepThreshold,
       "acpmFreqSysrepLimit": acpmFreqSysrepLimit,
       "acpmTotalRealPowerTable": acpmTotalRealPowerTable,
       "acpmTRPEntry": acpmTRPEntry,
       "acpmTRPIndex": acpmTRPIndex,
       "acpmTRPEnable": acpmTRPEnable,
       "acpmTRPDeadband": acpmTRPDeadband,
       "acpmTRPVHighValue": acpmTRPVHighValue,
       "acpmTRPVHighActions": acpmTRPVHighActions,
       "acpmTRPVHighTrapNum": acpmTRPVHighTrapNum,
       "acpmTRPVHighClass": acpmTRPVHighClass,
       "acpmTRPHighValue": acpmTRPHighValue,
       "acpmTRPHighActions": acpmTRPHighActions,
       "acpmTRPHighTrapNum": acpmTRPHighTrapNum,
       "acpmTRPHighClass": acpmTRPHighClass,
       "acpmTRPNormalActions": acpmTRPNormalActions,
       "acpmTRPNormalTrapNum": acpmTRPNormalTrapNum,
       "acpmTRPNormalClass": acpmTRPNormalClass,
       "acpmTRPLowValue": acpmTRPLowValue,
       "acpmTRPLowActions": acpmTRPLowActions,
       "acpmTRPLowTrapNum": acpmTRPLowTrapNum,
       "acpmTRPLowClass": acpmTRPLowClass,
       "acpmTRPVLowValue": acpmTRPVLowValue,
       "acpmTRPVLowActions": acpmTRPVLowActions,
       "acpmTRPVLowTrapNum": acpmTRPVLowTrapNum,
       "acpmTRPVLowClass": acpmTRPVLowClass,
       "acpmTRPSysrepEnable": acpmTRPSysrepEnable,
       "acpmTRPSysrepThreshold": acpmTRPSysrepThreshold,
       "acpmTRPSysrepLimit": acpmTRPSysrepLimit,
       "acpmDisconnectTable": acpmDisconnectTable,
       "acpmDisconnectEntry": acpmDisconnectEntry,
       "acpmDisconnectIndex": acpmDisconnectIndex,
       "acpmDisconnectEnable": acpmDisconnectEnable,
       "acpmDisconnectActions": acpmDisconnectActions,
       "acpmDisconnectTrapNum": acpmDisconnectTrapNum,
       "acpmDisconnectClass": acpmDisconnectClass,
       "acpmDisconnectNormalActions": acpmDisconnectNormalActions,
       "acpmDisconnectNormalTrapNum": acpmDisconnectNormalTrapNum,
       "acpmDisconnectNormalClass": acpmDisconnectNormalClass,
       "acpmTotalPowerFactorTable": acpmTotalPowerFactorTable,
       "acpmTPFEntry": acpmTPFEntry,
       "acpmTPFIndex": acpmTPFIndex,
       "acpmTPFEnable": acpmTPFEnable,
       "acpmTPFDeadband": acpmTPFDeadband,
       "acpmTPFNormalActions": acpmTPFNormalActions,
       "acpmTPFNormalTrapNum": acpmTPFNormalTrapNum,
       "acpmTPFNormalClass": acpmTPFNormalClass,
       "acpmTPFLowValue": acpmTPFLowValue,
       "acpmTPFLowActions": acpmTPFLowActions,
       "acpmTPFLowTrapNum": acpmTPFLowTrapNum,
       "acpmTPFLowClass": acpmTPFLowClass,
       "acpmTPFVLowValue": acpmTPFVLowValue,
       "acpmTPFVLowActions": acpmTPFVLowActions,
       "acpmTPFVLowTrapNum": acpmTPFVLowTrapNum,
       "acpmTPFVLowClass": acpmTPFVLowClass,
       "acpmTPFSysrepEnable": acpmTPFSysrepEnable,
       "acpmTPFSysrepThreshold": acpmTPFSysrepThreshold,
       "acpmTPFSysrepLimit": acpmTPFSysrepLimit,
       "batteryMonitor": batteryMonitor,
       "batteryMonitorGeneralTable": batteryMonitorGeneralTable,
       "bmGenEntry": bmGenEntry,
       "bmGenIndex": bmGenIndex,
       "bmGenEnable": bmGenEnable,
       "bmGenName": bmGenName,
       "bmGenBatteryQuantity": bmGenBatteryQuantity,
       "bmGenBatteryCapacity": bmGenBatteryCapacity,
       "bmGenBatteryNominalVoltage": bmGenBatteryNominalVoltage,
       "bmGenSysrepPackage": bmGenSysrepPackage,
       "bmGenSysrepType": bmGenSysrepType,
       "batteryMonitorDeviceTable": batteryMonitorDeviceTable,
       "bmDeviceEntry": bmDeviceEntry,
       "bmDeviceIndex": bmDeviceIndex,
       "bmDeviceType": bmDeviceType,
       "bmDeviceES": bmDeviceES,
       "bmDeviceIP": bmDeviceIP,
       "bmDeviceReadcom": bmDeviceReadcom,
       "bmDeviceInputString": bmDeviceInputString,
       "bmDeviceCTSize": bmDeviceCTSize,
       "batteryMonitorTempTable": batteryMonitorTempTable,
       "bmTempEntry": bmTempEntry,
       "bmTempIndex": bmTempIndex,
       "bmTempEnable": bmTempEnable,
       "bmTempDeadband": bmTempDeadband,
       "bmTempScale": bmTempScale,
       "bmTempHighValue": bmTempHighValue,
       "bmTempHighActions": bmTempHighActions,
       "bmTempHighTrapNum": bmTempHighTrapNum,
       "bmTempHighClass": bmTempHighClass,
       "bmTempNormalActions": bmTempNormalActions,
       "bmTempNormalTrapNum": bmTempNormalTrapNum,
       "bmTempNormalClass": bmTempNormalClass,
       "bmTempLowValue": bmTempLowValue,
       "bmTempLowActions": bmTempLowActions,
       "bmTempLowTrapNum": bmTempLowTrapNum,
       "bmTempLowClass": bmTempLowClass,
       "bmTempSysrepEnable": bmTempSysrepEnable,
       "bmTempSysrepThreshold": bmTempSysrepThreshold,
       "bmTempSysrepLimit": bmTempSysrepLimit,
       "batteryMonitorDiffTempTable": batteryMonitorDiffTempTable,
       "bmDiffTempEntry": bmDiffTempEntry,
       "bmDiffTempIndex": bmDiffTempIndex,
       "bmDiffTempEnable": bmDiffTempEnable,
       "bmDiffTempDeadband": bmDiffTempDeadband,
       "bmDiffTempVHighValue": bmDiffTempVHighValue,
       "bmDiffTempVHighActions": bmDiffTempVHighActions,
       "bmDiffTempVHighTrapNum": bmDiffTempVHighTrapNum,
       "bmDiffTempVHighClass": bmDiffTempVHighClass,
       "bmDiffTempHighValue": bmDiffTempHighValue,
       "bmDiffTempHighActions": bmDiffTempHighActions,
       "bmDiffTempHighTrapNum": bmDiffTempHighTrapNum,
       "bmDiffTempHighClass": bmDiffTempHighClass,
       "bmDiffTempNormalActions": bmDiffTempNormalActions,
       "bmDiffTempNormalTrapNum": bmDiffTempNormalTrapNum,
       "bmDiffTempNormalClass": bmDiffTempNormalClass,
       "bmDiffTempSysrepEnable": bmDiffTempSysrepEnable,
       "bmDiffTempSysrepThreshold": bmDiffTempSysrepThreshold,
       "bmDiffTempSysrepLimit": bmDiffTempSysrepLimit,
       "batteryMonitorVoltageTable": batteryMonitorVoltageTable,
       "bmVoltageEntry": bmVoltageEntry,
       "bmVoltageIndex": bmVoltageIndex,
       "bmVoltageEnable": bmVoltageEnable,
       "bmVoltageDeadband": bmVoltageDeadband,
       "bmVoltageVHighValue": bmVoltageVHighValue,
       "bmVoltageVHighActions": bmVoltageVHighActions,
       "bmVoltageVHighTrapNum": bmVoltageVHighTrapNum,
       "bmVoltageVHighClass": bmVoltageVHighClass,
       "bmVoltageHighValue": bmVoltageHighValue,
       "bmVoltageHighActions": bmVoltageHighActions,
       "bmVoltageHighTrapNum": bmVoltageHighTrapNum,
       "bmVoltageHighClass": bmVoltageHighClass,
       "bmVoltageNormalActions": bmVoltageNormalActions,
       "bmVoltageNormalTrapNum": bmVoltageNormalTrapNum,
       "bmVoltageNormalClass": bmVoltageNormalClass,
       "bmVoltageLowValue": bmVoltageLowValue,
       "bmVoltageLowActions": bmVoltageLowActions,
       "bmVoltageLowTrapNum": bmVoltageLowTrapNum,
       "bmVoltageLowClass": bmVoltageLowClass,
       "bmVoltageVLowValue": bmVoltageVLowValue,
       "bmVoltageVLowActions": bmVoltageVLowActions,
       "bmVoltageVLowTrapNum": bmVoltageVLowTrapNum,
       "bmVoltageVLowClass": bmVoltageVLowClass,
       "bmVoltageSysrepEnable": bmVoltageSysrepEnable,
       "bmVoltageSysrepThreshold": bmVoltageSysrepThreshold,
       "bmVoltageSysrepLimit": bmVoltageSysrepLimit,
       "batteryMonitorDiffVoltTable": batteryMonitorDiffVoltTable,
       "bmDiffVoltEntry": bmDiffVoltEntry,
       "bmDiffVoltIndex": bmDiffVoltIndex,
       "bmDiffVoltEnable": bmDiffVoltEnable,
       "bmDiffVoltDeadband": bmDiffVoltDeadband,
       "bmDiffVoltVHighValue": bmDiffVoltVHighValue,
       "bmDiffVoltVHighActions": bmDiffVoltVHighActions,
       "bmDiffVoltVHighTrapNum": bmDiffVoltVHighTrapNum,
       "bmDiffVoltVHighClass": bmDiffVoltVHighClass,
       "bmDiffVoltHighValue": bmDiffVoltHighValue,
       "bmDiffVoltHighActions": bmDiffVoltHighActions,
       "bmDiffVoltHighTrapNum": bmDiffVoltHighTrapNum,
       "bmDiffVoltHighClass": bmDiffVoltHighClass,
       "bmDiffVoltNormalActions": bmDiffVoltNormalActions,
       "bmDiffVoltNormalTrapNum": bmDiffVoltNormalTrapNum,
       "bmDiffVoltNormalClass": bmDiffVoltNormalClass,
       "bmDiffVoltSysrepEnable": bmDiffVoltSysrepEnable,
       "bmDiffVoltSysrepThreshold": bmDiffVoltSysrepThreshold,
       "bmDiffVoltSysrepLimit": bmDiffVoltSysrepLimit,
       "batteryMonitorChargingCurrentTable": batteryMonitorChargingCurrentTable,
       "bmChargingCurrentEntry": bmChargingCurrentEntry,
       "bmChargingCurrentIndex": bmChargingCurrentIndex,
       "bmChargingCurrentEnable": bmChargingCurrentEnable,
       "bmChargingCurrentDeadband": bmChargingCurrentDeadband,
       "bmChargingCurrentVHighValue": bmChargingCurrentVHighValue,
       "bmChargingCurrentVHighActions": bmChargingCurrentVHighActions,
       "bmChargingCurrentVHighTrapNum": bmChargingCurrentVHighTrapNum,
       "bmChargingCurrentVHighClass": bmChargingCurrentVHighClass,
       "bmChargingCurrentHighValue": bmChargingCurrentHighValue,
       "bmChargingCurrentHighActions": bmChargingCurrentHighActions,
       "bmChargingCurrentHighTrapNum": bmChargingCurrentHighTrapNum,
       "bmChargingCurrentHighClass": bmChargingCurrentHighClass,
       "bmChargingCurrentNormalActions": bmChargingCurrentNormalActions,
       "bmChargingCurrentNormalTrapNum": bmChargingCurrentNormalTrapNum,
       "bmChargingCurrentNormalClass": bmChargingCurrentNormalClass,
       "bmChargingCurrentSysrepEnable": bmChargingCurrentSysrepEnable,
       "bmChargingCurrentSysrepThreshold": bmChargingCurrentSysrepThreshold,
       "bmChargingCurrentSysrepLimit": bmChargingCurrentSysrepLimit,
       "batteryMonitorDischargingCurrentTable": batteryMonitorDischargingCurrentTable,
       "bmDischargingCurrentEntry": bmDischargingCurrentEntry,
       "bmDischargingCurrentIndex": bmDischargingCurrentIndex,
       "bmDischargingCurrentEnable": bmDischargingCurrentEnable,
       "bmDischargingCurrentDeadband": bmDischargingCurrentDeadband,
       "bmDischargingCurrentVHighValue": bmDischargingCurrentVHighValue,
       "bmDischargingCurrentVHighActions": bmDischargingCurrentVHighActions,
       "bmDischargingCurrentVHighTrapNum": bmDischargingCurrentVHighTrapNum,
       "bmDischargingCurrentVHighClass": bmDischargingCurrentVHighClass,
       "bmDischargingCurrentHighValue": bmDischargingCurrentHighValue,
       "bmDischargingCurrentHighActions": bmDischargingCurrentHighActions,
       "bmDischargingCurrentHighTrapNum": bmDischargingCurrentHighTrapNum,
       "bmDischargingCurrentHighClass": bmDischargingCurrentHighClass,
       "bmDischargingCurrentNormalActions": bmDischargingCurrentNormalActions,
       "bmDischargingCurrentNormalTrapNum": bmDischargingCurrentNormalTrapNum,
       "bmDischargingCurrentNormalClass": bmDischargingCurrentNormalClass,
       "bmDischargingCurrentSysrepEnable": bmDischargingCurrentSysrepEnable,
       "bmDischargingCurrentSysrepThreshold": bmDischargingCurrentSysrepThreshold,
       "bmDischargingCurrentSysrepLimit": bmDischargingCurrentSysrepLimit,
       "batteryMonitorChargeLevelTable": batteryMonitorChargeLevelTable,
       "bmChargeLevelEntry": bmChargeLevelEntry,
       "bmChargeLevelIndex": bmChargeLevelIndex,
       "bmChargeLevelEnable": bmChargeLevelEnable,
       "bmChargeLevelNormalActions": bmChargeLevelNormalActions,
       "bmChargeLevelNormalTrapNum": bmChargeLevelNormalTrapNum,
       "bmChargeLevelNormalClass": bmChargeLevelNormalClass,
       "bmChargeLevelLowActions": bmChargeLevelLowActions,
       "bmChargeLevelLowTrapNum": bmChargeLevelLowTrapNum,
       "bmChargeLevelLowClass": bmChargeLevelLowClass,
       "bmChargeLevelVLowActions": bmChargeLevelVLowActions,
       "bmChargeLevelVLowTrapNum": bmChargeLevelVLowTrapNum,
       "bmChargeLevelVLowClass": bmChargeLevelVLowClass,
       "bmChargeLevelSysrepEnable": bmChargeLevelSysrepEnable,
       "batteryMonitorJarHealthTable": batteryMonitorJarHealthTable,
       "bmJarHealthEntry": bmJarHealthEntry,
       "bmJarHealthIndex": bmJarHealthIndex,
       "bmJarHealthEnable": bmJarHealthEnable,
       "bmJarHealthNormalActions": bmJarHealthNormalActions,
       "bmJarHealthNormalTrapNum": bmJarHealthNormalTrapNum,
       "bmJarHealthNormalClass": bmJarHealthNormalClass,
       "bmJarHealthLowActions": bmJarHealthLowActions,
       "bmJarHealthLowTrapNum": bmJarHealthLowTrapNum,
       "bmJarHealthLowClass": bmJarHealthLowClass,
       "bmJarHealthVLowActions": bmJarHealthVLowActions,
       "bmJarHealthVLowTrapNum": bmJarHealthVLowTrapNum,
       "bmJarHealthVLowClass": bmJarHealthVLowClass,
       "bmJarHealthSysrepEnable": bmJarHealthSysrepEnable,
       "evLocation": evLocation,
       "evLocationEnable": evLocationEnable,
       "evLocationTimeout": evLocationTimeout,
       "evLocationActions": evLocationActions,
       "evLocationMsgSuccess": evLocationMsgSuccess,
       "evLocationMsgFail": evLocationMsgFail,
       "evLocationIncludeLocation": evLocationIncludeLocation,
       "evLocationTrapnum": evLocationTrapnum,
       "evLocationClass": evLocationClass,
       "evReset": evReset,
       "evResetEnable": evResetEnable,
       "evResetDelay": evResetDelay,
       "evResetActions": evResetActions,
       "evResetMessage": evResetMessage,
       "evResetTrapnum": evResetTrapnum,
       "evResetClass": evResetClass,
       "evSleep": evSleep,
       "evSleepEnable": evSleepEnable,
       "evSleepActions": evSleepActions,
       "evSleepMessage": evSleepMessage,
       "evSleepTrapnum": evSleepTrapnum,
       "evSleepClass": evSleepClass,
       "evGlobal": evGlobal,
       "evGlobalActions": evGlobalActions,
       "evGlobalTrapnum": evGlobalTrapnum,
       "accessControl": accessControl,
       "acActions": acActions,
       "acTrapnum": acTrapnum,
       "acClass": acClass,
       "accessControlDeviceTable": accessControlDeviceTable,
       "accessControlDeviceEntry": accessControlDeviceEntry,
       "acdIndex": acdIndex,
       "acdEnable": acdEnable,
       "acdName": acdName,
       "acdReader": acdReader,
       "acdWiegandES": acdWiegandES,
       "acdRelayType": acdRelayType,
       "acdRelayES": acdRelayES,
       "acdRelayPoint": acdRelayPoint,
       "acdOpenTime": acdOpenTime,
       "acdUserGroup": acdUserGroup,
       "accessControlUserTable": accessControlUserTable,
       "accessControlUserEntry": accessControlUserEntry,
       "acuIndexUserGroup": acuIndexUserGroup,
       "acuIndexUser": acuIndexUser,
       "acuEnable": acuEnable,
       "acuName": acuName,
       "acuSn": acuSn,
       "acuSunBegin": acuSunBegin,
       "acuSunEnd": acuSunEnd,
       "acuMonBegin": acuMonBegin,
       "acuMonEnd": acuMonEnd,
       "acuTueBegin": acuTueBegin,
       "acuTueEnd": acuTueEnd,
       "acuWedBegin": acuWedBegin,
       "acuWedEnd": acuWedEnd,
       "acuThuBegin": acuThuBegin,
       "acuThuEnd": acuThuEnd,
       "acuFriBegin": acuFriBegin,
       "acuFriEnd": acuFriEnd,
       "acuSatBegin": acuSatBegin,
       "acuSatEnd": acuSatEnd,
       "action": action,
       "actionSched": actionSched,
       "actionSchedEnable": actionSchedEnable,
       "actionSchedBegin": actionSchedBegin,
       "actionSchedEnd": actionSchedEnd,
       "actionSchedWeekdaysOnly": actionSchedWeekdaysOnly,
       "actionAsentria": actionAsentria,
       "actionAsentriaRequireAck": actionAsentriaRequireAck,
       "actionAsentriaVersion": actionAsentriaVersion,
       "actionAsentriaTCPPort": actionAsentriaTCPPort,
       "actionHostTable": actionHostTable,
       "actionHostEntry": actionHostEntry,
       "actionHostIndex": actionHostIndex,
       "actionHost": actionHost,
       "actionEmailTable": actionEmailTable,
       "actionEmailEntry": actionEmailEntry,
       "actionEmailIndex": actionEmailIndex,
       "actionEmail": actionEmail,
       "actionParseError": actionParseError,
       "sys": sys,
       "sysTime": sysTime,
       "sysTimeAutoDST": sysTimeAutoDST,
       "sysTimeGMTOffset": sysTimeGMTOffset,
       "sysTimeGMTDirection": sysTimeGMTDirection,
       "sysTimeNet": sysTimeNet,
       "sysTimeNetEnable": sysTimeNetEnable,
       "sysTimeNetHostTable": sysTimeNetHostTable,
       "sysTimeNetHostEntry": sysTimeNetHostEntry,
       "sysTimeNetHostIndex": sysTimeNetHostIndex,
       "sysTimeNetHost": sysTimeNetHost,
       "sysPT": sysPT,
       "sysPTTimeout": sysPTTimeout,
       "sysPTEndPause": sysPTEndPause,
       "sysPTJoinable": sysPTJoinable,
       "sysMTU": sysMTU,
       "sysAnswerString": sysAnswerString,
       "sysEventFileID": sysEventFileID,
       "sysEscapeCharacter": sysEscapeCharacter,
       "sysTimeStamp": sysTimeStamp,
       "sysTimeStampTimeFormat": sysTimeStampTimeFormat,
       "sysTimeStampDateFormat": sysTimeStampDateFormat,
       "sysTimeStampSpaceAfter": sysTimeStampSpaceAfter,
       "sysLog": sysLog,
       "sysLogMode": sysLogMode,
       "sysLoghost": sysLoghost,
       "sysLogFilter": sysLogFilter,
       "sysLogFileSize": sysLogFileSize,
       "sysLogFileCount": sysLogFileCount,
       "sysLogListenPort": sysLogListenPort,
       "sysCRDB": sysCRDB,
       "sysCRDBCapacity": sysCRDBCapacity,
       "sysCRDBPercentFull": sysCRDBPercentFull,
       "sysCRDBFileIDTable": sysCRDBFileIDTable,
       "sysCRDBFileIDEntry": sysCRDBFileIDEntry,
       "sysCRDBFileIDIndex": sysCRDBFileIDIndex,
       "sysCRDBFileID": sysCRDBFileID,
       "sysCRDBFileEnforceMinTable": sysCRDBFileEnforceMinTable,
       "sysCRDBFileEnforceMinEntry": sysCRDBFileEnforceMinEntry,
       "sysCRDBFileEnforceMinIndex": sysCRDBFileEnforceMinIndex,
       "sysCRDBFileEnforceMin": sysCRDBFileEnforceMin,
       "sysCharMask": sysCharMask,
       "sysPrompt": sysPrompt,
       "sysBootStatus": sysBootStatus,
       "sysLoc": sysLoc,
       "sysLocLatitude": sysLocLatitude,
       "sysLocLongitude": sysLocLongitude,
       "sysLocXOffset": sysLocXOffset,
       "sysLocYOffset": sysLocYOffset,
       "sysLocAngle": sysLocAngle,
       "sysLocAltitude": sysLocAltitude,
       "sysSleep": sysSleep,
       "sysSleepEnable": sysSleepEnable,
       "sysSleepSleep": sysSleepSleep,
       "sysSleepForceSleep": sysSleepForceSleep,
       "sysSleepSleepTimer": sysSleepSleepTimer,
       "sysSleepWake": sysSleepWake,
       "sysSleepWakeTimerNormal": sysSleepWakeTimerNormal,
       "sysSleepWakeTimerMotion": sysSleepWakeTimerMotion,
       "sysSleepWakeMotionEnable": sysSleepWakeMotionEnable,
       "sysSleepWakeScheduledEnable": sysSleepWakeScheduledEnable,
       "sysSleepWakeScheduledTimeOfDay": sysSleepWakeScheduledTimeOfDay,
       "sysSleepPowerDetectCC": sysSleepPowerDetectCC,
       "sysSleepPowerDetectCCEnable": sysSleepPowerDetectCCEnable,
       "sysSleepPowerDetectCCPowerOnState": sysSleepPowerDetectCCPowerOnState,
       "sysSleepPowerDetectCCThreshold": sysSleepPowerDetectCCThreshold,
       "sysFileTransfer": sysFileTransfer,
       "sysFileTransferStatus": sysFileTransferStatus,
       "sysFileTransferURL": sysFileTransferURL,
       "sysFileTransferUsername": sysFileTransferUsername,
       "sysFileTransferPassword": sysFileTransferPassword,
       "sysUpdate": sysUpdate,
       "sysUpdateStatus": sysUpdateStatus,
       "auditLog": auditLog,
       "auditLogEnable": auditLogEnable,
       "auditLogStoreResets": auditLogStoreResets,
       "auditLogStoreCommands": auditLogStoreCommands,
       "auditLogStoreOutputs": auditLogStoreOutputs,
       "auditLogStoreAlarmActions": auditLogStoreAlarmActions,
       "auditLogStorePwdFailures": auditLogStorePwdFailures,
       "auditLogStoreLogins": auditLogStoreLogins,
       "auditLogStoreSHSK": auditLogStoreSHSK,
       "auditLogStorePassthrough": auditLogStorePassthrough,
       "auditLogStoreInactivity": auditLogStoreInactivity,
       "auditLogStorePolling": auditLogStorePolling,
       "auditLogMaxSize": auditLogMaxSize,
       "auditLogSoreSleepActivity": auditLogSoreSleepActivity,
       "scripting": scripting,
       "scrGlobalEnable": scrGlobalEnable,
       "scrDTRCtrlPortEnableTable": scrDTRCtrlPortEnableTable,
       "scrDTRCtrlPortEnableEntry": scrDTRCtrlPortEnableEntry,
       "scrDTRCtrlPortEnableIndex": scrDTRCtrlPortEnableIndex,
       "scrDTRCtrlPortEnable": scrDTRCtrlPortEnable,
       "scrTable": scrTable,
       "scrEntry": scrEntry,
       "scrIndex": scrIndex,
       "scrEnable": scrEnable,
       "scrName": scrName,
       "scrFilename": scrFilename,
       "scrRunAlways": scrRunAlways,
       "scrRunAtStartup": scrRunAtStartup,
       "scrRunScheduled": scrRunScheduled,
       "scrScheduleTime": scrScheduleTime,
       "scrArguments": scrArguments,
       "scrRepeatInterval": scrRepeatInterval,
       "scrVolatileStringTable": scrVolatileStringTable,
       "scrVolatileStringEntry": scrVolatileStringEntry,
       "scrVolatileStringIndex": scrVolatileStringIndex,
       "scrVolatileString": scrVolatileString,
       "scrVolatileIntTable": scrVolatileIntTable,
       "scrVolatileIntEntry": scrVolatileIntEntry,
       "scrVolatileIntIndex": scrVolatileIntIndex,
       "scrVolatileInt": scrVolatileInt,
       "scrNonVolatileStringTable": scrNonVolatileStringTable,
       "scrNonVolatileStringEntry": scrNonVolatileStringEntry,
       "scrNonVolatileStringIndex": scrNonVolatileStringIndex,
       "scrNonVolatileString": scrNonVolatileString,
       "scrNonVolatileIntTable": scrNonVolatileIntTable,
       "scrNonVolatileIntEntry": scrNonVolatileIntEntry,
       "scrNonVolatileIntIndex": scrNonVolatileIntIndex,
       "scrNonVolatileInt": scrNonVolatileInt,
       "generator": generator,
       "genSet": genSet,
       "genSetEnable": genSetEnable,
       "genSetRelay": genSetRelay,
       "genSetRelayEs": genSetRelayEs,
       "genSetRelayPoint": genSetRelayPoint,
       "genSetRelayRunningstate": genSetRelayRunningstate,
       "genSetRelayTable": genSetRelayTable,
       "genSetRelayTableEntry": genSetRelayTableEntry,
       "genSetRelayTableIndex": genSetRelayTableIndex,
       "genSetRelayTableEnable": genSetRelayTableEnable,
       "genSetRelayTableEs": genSetRelayTableEs,
       "genSetRelayTablePoint": genSetRelayTablePoint,
       "genSetRelayTableRunningstate": genSetRelayTableRunningstate,
       "genSetCC": genSetCC,
       "genSetCCEnable": genSetCCEnable,
       "genSetCCEs": genSetCCEs,
       "genSetCCPoint": genSetCCPoint,
       "genSetCCRunningState": genSetCCRunningState,
       "genSetCCDelay": genSetCCDelay,
       "genRun": genRun,
       "genRunMode": genRunMode,
       "genRunSched": genRunSched,
       "genRunDuration": genRunDuration,
       "genRunForce": genRunForce,
       "genRunReqasm": genRunReqasm,
       "genRunStatus": genRunStatus,
       "genRunNonstartEvent": genRunNonstartEvent,
       "genRunNonstartEventEnable": genRunNonstartEventEnable,
       "genRunNonstartEventActions": genRunNonstartEventActions,
       "genRunNonstartEventTrap": genRunNonstartEventTrap,
       "genRunNonstartEventClass": genRunNonstartEventClass,
       "calendar": calendar,
       "schedTable": schedTable,
       "schedEntry": schedEntry,
       "schedIndex": schedIndex,
       "schedEnable": schedEnable,
       "schedStart": schedStart,
       "schedRepeatMode": schedRepeatMode,
       "schedRepeatFreq": schedRepeatFreq,
       "schedRepeatEndMode": schedRepeatEndMode,
       "schedRepeatEndAfter": schedRepeatEndAfter,
       "schedRepeatEndOn": schedRepeatEndOn,
       "schedRepeatWeeklySun": schedRepeatWeeklySun,
       "schedRepeatWeeklyMon": schedRepeatWeeklyMon,
       "schedRepeatWeeklyTue": schedRepeatWeeklyTue,
       "schedRepeatWeeklyWed": schedRepeatWeeklyWed,
       "schedRepeatWeeklyThu": schedRepeatWeeklyThu,
       "schedRepeatWeeklyFri": schedRepeatWeeklyFri,
       "schedRepeatWeeklySat": schedRepeatWeeklySat,
       "schedRepeatMonthlyMode": schedRepeatMonthlyMode,
       "schedRepeatMonthlyDates": schedRepeatMonthlyDates,
       "schedRepeatMonthlyOnThe": schedRepeatMonthlyOnThe,
       "schedRepeatMonthlyOnDay": schedRepeatMonthlyOnDay,
       "schedRepeatYearlyJan": schedRepeatYearlyJan,
       "schedRepeatYearlyFeb": schedRepeatYearlyFeb,
       "schedRepeatYearlyMar": schedRepeatYearlyMar,
       "schedRepeatYearlyApr": schedRepeatYearlyApr,
       "schedRepeatYearlyMay": schedRepeatYearlyMay,
       "schedRepeatYearlyJun": schedRepeatYearlyJun,
       "schedRepeatYearlyJul": schedRepeatYearlyJul,
       "schedRepeatYearlyAug": schedRepeatYearlyAug,
       "schedRepeatYearlySep": schedRepeatYearlySep,
       "schedRepeatYearlyOct": schedRepeatYearlyOct,
       "schedRepeatYearlyNov": schedRepeatYearlyNov,
       "schedRepeatYearlyDec": schedRepeatYearlyDec,
       "schedRepeatYearlyOnThe": schedRepeatYearlyOnThe,
       "schedRepeatYearlyOnDay": schedRepeatYearlyOnDay,
       "schedNextTrigger": schedNextTrigger,
       "productIds": productIds,
       "siteName": siteName,
       "thisProduct": thisProduct,
       "stockTrapString": stockTrapString,
       "trapEventTypeNumber": trapEventTypeNumber,
       "trapEventTypeName": trapEventTypeName,
       "trapIncludedValue": trapIncludedValue,
       "trapIncludedString": trapIncludedString,
       "trapTypeString": trapTypeString,
       "trapEventClassNumber": trapEventClassNumber,
       "trapEventClassName": trapEventClassName,
       "keyInterface": keyInterface}
)
