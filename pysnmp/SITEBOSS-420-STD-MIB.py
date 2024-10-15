# SNMP MIB module (SITEBOSS-420-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/SITEBOSS-420-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:52:29 2024
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

s420 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42)
)
s420.setRevisions(
        ("2013-06-13 01:07",
         "2012-03-01 01:05",
         "2012-03-01 01:04",
         "2009-03-08 09:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Notification_ObjectIdentity = ObjectIdentity
notification = _Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 0)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 1)
)
_EventSensorStatus_ObjectIdentity = ObjectIdentity
eventSensorStatus = _EventSensorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 1, 1)
)
_EsPointTable_Object = MibTable
esPointTable = _EsPointTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 1, 1, 1)
)
if mibBuilder.loadTexts:
    esPointTable.setStatus("current")
_EsPointEntry_Object = MibTableRow
esPointEntry = _EsPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 1, 1, 1, 1)
)
esPointEntry.setIndexNames(
    (0, "SITEBOSS-420-STD-MIB", "esIndexES"),
    (0, "SITEBOSS-420-STD-MIB", "esIndexPC"),
    (0, "SITEBOSS-420-STD-MIB", "esIndexPoint"),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 1, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 1, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 1, 1, 1, 1, 3),
    _EsIndexPoint_Type()
)
esIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPoint.setStatus("current")
_EsPointName_Type = DisplayString
_EsPointName_Object = MibTableColumn
esPointName = _EsPointName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 1, 1, 1, 1, 4),
    _EsPointName_Type()
)
esPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointName.setStatus("current")
_EsPointInEventState_Type = Integer32
_EsPointInEventState_Object = MibTableColumn
esPointInEventState = _EsPointInEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 1, 1, 1, 1, 5),
    _EsPointInEventState_Type()
)
esPointInEventState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointInEventState.setStatus("current")


class _EsPointValueInt_Type(Integer32):
    """Custom type esPointValueInt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_EsPointValueInt_Type.__name__ = "Integer32"
_EsPointValueInt_Object = MibTableColumn
esPointValueInt = _EsPointValueInt_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 1, 1, 1, 1, 6),
    _EsPointValueInt_Type()
)
esPointValueInt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointValueInt.setStatus("current")
_EsPointValueStr_Type = DisplayString
_EsPointValueStr_Object = MibTableColumn
esPointValueStr = _EsPointValueStr_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 1, 1, 1, 1, 7),
    _EsPointValueStr_Type()
)
esPointValueStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esPointValueStr.setStatus("current")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2)
)
_EventSensorPointConfig_ObjectIdentity = ObjectIdentity
eventSensorPointConfig = _EventSensorPointConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2)
)
_EsPointConfigTempTable_Object = MibTable
esPointConfigTempTable = _EsPointConfigTempTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1)
)
if mibBuilder.loadTexts:
    esPointConfigTempTable.setStatus("current")
_EsPointConfigTempEntry_Object = MibTableRow
esPointConfigTempEntry = _EsPointConfigTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1)
)
esPointConfigTempEntry.setIndexNames(
    (0, "SITEBOSS-420-STD-MIB", "espcTempIndexES"),
    (0, "SITEBOSS-420-STD-MIB", "espcTempIndexPoint"),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 2),
    _EspcTempIndexPoint_Type()
)
espcTempIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcTempIndexPoint.setStatus("current")
_EspcTempEnable_Type = DisplayString
_EspcTempEnable_Object = MibTableColumn
espcTempEnable = _EspcTempEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 3),
    _EspcTempEnable_Type()
)
espcTempEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempEnable.setStatus("current")
_EspcTempName_Type = DisplayString
_EspcTempName_Object = MibTableColumn
espcTempName = _EspcTempName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 4),
    _EspcTempName_Type()
)
espcTempName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempName.setStatus("current")
_EspcTempScale_Type = DisplayString
_EspcTempScale_Object = MibTableColumn
espcTempScale = _EspcTempScale_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 5),
    _EspcTempScale_Type()
)
espcTempScale.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempScale.setStatus("current")
_EspcTempDeadband_Type = Integer32
_EspcTempDeadband_Object = MibTableColumn
espcTempDeadband = _EspcTempDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 6),
    _EspcTempDeadband_Type()
)
espcTempDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempDeadband.setStatus("current")
_EspcTempVHighTemp_Type = Integer32
_EspcTempVHighTemp_Object = MibTableColumn
espcTempVHighTemp = _EspcTempVHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 7),
    _EspcTempVHighTemp_Type()
)
espcTempVHighTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVHighTemp.setStatus("current")
_EspcTempVHighClass_Type = DisplayString
_EspcTempVHighClass_Object = MibTableColumn
espcTempVHighClass = _EspcTempVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 9),
    _EspcTempVHighClass_Type()
)
espcTempVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVHighClass.setStatus("current")
_EspcTempHighTemp_Type = Integer32
_EspcTempHighTemp_Object = MibTableColumn
espcTempHighTemp = _EspcTempHighTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 10),
    _EspcTempHighTemp_Type()
)
espcTempHighTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempHighTemp.setStatus("current")
_EspcTempHighClass_Type = DisplayString
_EspcTempHighClass_Object = MibTableColumn
espcTempHighClass = _EspcTempHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 13),
    _EspcTempHighClass_Type()
)
espcTempHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempHighClass.setStatus("current")
_EspcTempLowTemp_Type = Integer32
_EspcTempLowTemp_Object = MibTableColumn
espcTempLowTemp = _EspcTempLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 17),
    _EspcTempLowTemp_Type()
)
espcTempLowTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempLowTemp.setStatus("current")
_EspcTempLowClass_Type = DisplayString
_EspcTempLowClass_Object = MibTableColumn
espcTempLowClass = _EspcTempLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 20),
    _EspcTempLowClass_Type()
)
espcTempLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempLowClass.setStatus("current")
_EspcTempVLowTemp_Type = Integer32
_EspcTempVLowTemp_Object = MibTableColumn
espcTempVLowTemp = _EspcTempVLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 21),
    _EspcTempVLowTemp_Type()
)
espcTempVLowTemp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVLowTemp.setStatus("current")
_EspcTempVLowClass_Type = DisplayString
_EspcTempVLowClass_Object = MibTableColumn
espcTempVLowClass = _EspcTempVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 24),
    _EspcTempVLowClass_Type()
)
espcTempVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempVLowClass.setStatus("current")
_EspcTempActions_Type = DisplayString
_EspcTempActions_Object = MibTableColumn
espcTempActions = _EspcTempActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 1, 1, 25),
    _EspcTempActions_Type()
)
espcTempActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcTempActions.setStatus("current")
_EsPointConfigCCTable_Object = MibTable
esPointConfigCCTable = _EsPointConfigCCTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2)
)
if mibBuilder.loadTexts:
    esPointConfigCCTable.setStatus("current")
_EsPointConfigCCEntry_Object = MibTableRow
esPointConfigCCEntry = _EsPointConfigCCEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1)
)
esPointConfigCCEntry.setIndexNames(
    (0, "SITEBOSS-420-STD-MIB", "espcCCIndexES"),
    (0, "SITEBOSS-420-STD-MIB", "espcCCIndexPoint"),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 2),
    _EspcCCIndexPoint_Type()
)
espcCCIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcCCIndexPoint.setStatus("current")
_EspcCCEnable_Type = DisplayString
_EspcCCEnable_Object = MibTableColumn
espcCCEnable = _EspcCCEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 3),
    _EspcCCEnable_Type()
)
espcCCEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEnable.setStatus("current")
_EspcCCName_Type = DisplayString
_EspcCCName_Object = MibTableColumn
espcCCName = _EspcCCName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 4),
    _EspcCCName_Type()
)
espcCCName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCName.setStatus("current")
_EspcCCEventState_Type = DisplayString
_EspcCCEventState_Object = MibTableColumn
espcCCEventState = _EspcCCEventState_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 5),
    _EspcCCEventState_Type()
)
espcCCEventState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEventState.setStatus("current")
_EspcCCThreshold_Type = Integer32
_EspcCCThreshold_Object = MibTableColumn
espcCCThreshold = _EspcCCThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 6),
    _EspcCCThreshold_Type()
)
espcCCThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCThreshold.setStatus("current")
_EspcCCActions_Type = DisplayString
_EspcCCActions_Object = MibTableColumn
espcCCActions = _EspcCCActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 7),
    _EspcCCActions_Type()
)
espcCCActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCActions.setStatus("current")
_EspcCCEventClass_Type = DisplayString
_EspcCCEventClass_Object = MibTableColumn
espcCCEventClass = _EspcCCEventClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 9),
    _EspcCCEventClass_Type()
)
espcCCEventClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCEventClass.setStatus("current")
_EspcCCNormalClass_Type = DisplayString
_EspcCCNormalClass_Object = MibTableColumn
espcCCNormalClass = _EspcCCNormalClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 12),
    _EspcCCNormalClass_Type()
)
espcCCNormalClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalClass.setStatus("current")
_EspcCCAlarmAlias_Type = DisplayString
_EspcCCAlarmAlias_Object = MibTableColumn
espcCCAlarmAlias = _EspcCCAlarmAlias_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 13),
    _EspcCCAlarmAlias_Type()
)
espcCCAlarmAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCAlarmAlias.setStatus("current")
_EspcCCNormalAlias_Type = DisplayString
_EspcCCNormalAlias_Object = MibTableColumn
espcCCNormalAlias = _EspcCCNormalAlias_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 2, 1, 14),
    _EspcCCNormalAlias_Type()
)
espcCCNormalAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcCCNormalAlias.setStatus("current")
_EsPointConfigHumidTable_Object = MibTable
esPointConfigHumidTable = _EsPointConfigHumidTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3)
)
if mibBuilder.loadTexts:
    esPointConfigHumidTable.setStatus("current")
_EsPointConfigHumidEntry_Object = MibTableRow
esPointConfigHumidEntry = _EsPointConfigHumidEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1)
)
esPointConfigHumidEntry.setIndexNames(
    (0, "SITEBOSS-420-STD-MIB", "espcHumidIndexES"),
    (0, "SITEBOSS-420-STD-MIB", "espcHumidIndexPoint"),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 2),
    _EspcHumidIndexPoint_Type()
)
espcHumidIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcHumidIndexPoint.setStatus("current")
_EspcHumidEnable_Type = DisplayString
_EspcHumidEnable_Object = MibTableColumn
espcHumidEnable = _EspcHumidEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 3),
    _EspcHumidEnable_Type()
)
espcHumidEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidEnable.setStatus("current")
_EspcHumidName_Type = DisplayString
_EspcHumidName_Object = MibTableColumn
espcHumidName = _EspcHumidName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 4),
    _EspcHumidName_Type()
)
espcHumidName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidName.setStatus("current")
_EspcHumidDeadband_Type = Integer32
_EspcHumidDeadband_Object = MibTableColumn
espcHumidDeadband = _EspcHumidDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 5),
    _EspcHumidDeadband_Type()
)
espcHumidDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidDeadband.setStatus("current")
_EspcHumidVHighHumid_Type = Integer32
_EspcHumidVHighHumid_Object = MibTableColumn
espcHumidVHighHumid = _EspcHumidVHighHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 6),
    _EspcHumidVHighHumid_Type()
)
espcHumidVHighHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVHighHumid.setStatus("current")
_EspcHumidVHighClass_Type = DisplayString
_EspcHumidVHighClass_Object = MibTableColumn
espcHumidVHighClass = _EspcHumidVHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 8),
    _EspcHumidVHighClass_Type()
)
espcHumidVHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVHighClass.setStatus("current")
_EspcHumidHighHumid_Type = Integer32
_EspcHumidHighHumid_Object = MibTableColumn
espcHumidHighHumid = _EspcHumidHighHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 9),
    _EspcHumidHighHumid_Type()
)
espcHumidHighHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidHighHumid.setStatus("current")
_EspcHumidHighClass_Type = DisplayString
_EspcHumidHighClass_Object = MibTableColumn
espcHumidHighClass = _EspcHumidHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 12),
    _EspcHumidHighClass_Type()
)
espcHumidHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidHighClass.setStatus("current")
_EspcHumidLowHumid_Type = Integer32
_EspcHumidLowHumid_Object = MibTableColumn
espcHumidLowHumid = _EspcHumidLowHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 16),
    _EspcHumidLowHumid_Type()
)
espcHumidLowHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidLowHumid.setStatus("current")
_EspcHumidLowClass_Type = DisplayString
_EspcHumidLowClass_Object = MibTableColumn
espcHumidLowClass = _EspcHumidLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 19),
    _EspcHumidLowClass_Type()
)
espcHumidLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidLowClass.setStatus("current")
_EspcHumidVLowHumid_Type = Integer32
_EspcHumidVLowHumid_Object = MibTableColumn
espcHumidVLowHumid = _EspcHumidVLowHumid_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 20),
    _EspcHumidVLowHumid_Type()
)
espcHumidVLowHumid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVLowHumid.setStatus("current")
_EspcHumidVLowClass_Type = DisplayString
_EspcHumidVLowClass_Object = MibTableColumn
espcHumidVLowClass = _EspcHumidVLowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 23),
    _EspcHumidVLowClass_Type()
)
espcHumidVLowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidVLowClass.setStatus("current")
_EspcHumidActions_Type = DisplayString
_EspcHumidActions_Object = MibTableColumn
espcHumidActions = _EspcHumidActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 3, 1, 24),
    _EspcHumidActions_Type()
)
espcHumidActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcHumidActions.setStatus("current")
_EsPointConfigAITable_Object = MibTable
esPointConfigAITable = _EsPointConfigAITable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5)
)
if mibBuilder.loadTexts:
    esPointConfigAITable.setStatus("current")
_EsPointConfigAIEntry_Object = MibTableRow
esPointConfigAIEntry = _EsPointConfigAIEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1)
)
esPointConfigAIEntry.setIndexNames(
    (0, "SITEBOSS-420-STD-MIB", "espcHumidIndexES"),
    (0, "SITEBOSS-420-STD-MIB", "espcHumidIndexPoint"),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 2),
    _EspcAIIndexPoint_Type()
)
espcAIIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcAIIndexPoint.setStatus("current")
_EspcAIEnable_Type = DisplayString
_EspcAIEnable_Object = MibTableColumn
espcAIEnable = _EspcAIEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 3),
    _EspcAIEnable_Type()
)
espcAIEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIEnable.setStatus("current")
_EspcAIName_Type = DisplayString
_EspcAIName_Object = MibTableColumn
espcAIName = _EspcAIName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 4),
    _EspcAIName_Type()
)
espcAIName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIName.setStatus("current")
_EspcAIDeadband_Type = Integer32
_EspcAIDeadband_Object = MibTableColumn
espcAIDeadband = _EspcAIDeadband_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 5),
    _EspcAIDeadband_Type()
)
espcAIDeadband.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIDeadband.setStatus("current")
_EspcAIVhighValue_Type = Integer32
_EspcAIVhighValue_Object = MibTableColumn
espcAIVhighValue = _EspcAIVhighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 6),
    _EspcAIVhighValue_Type()
)
espcAIVhighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVhighValue.setStatus("current")
_EspcAIVhighClass_Type = DisplayString
_EspcAIVhighClass_Object = MibTableColumn
espcAIVhighClass = _EspcAIVhighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 8),
    _EspcAIVhighClass_Type()
)
espcAIVhighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVhighClass.setStatus("current")
_EspcAIHighValue_Type = Integer32
_EspcAIHighValue_Object = MibTableColumn
espcAIHighValue = _EspcAIHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 9),
    _EspcAIHighValue_Type()
)
espcAIHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIHighValue.setStatus("current")
_EspcAIHighClass_Type = DisplayString
_EspcAIHighClass_Object = MibTableColumn
espcAIHighClass = _EspcAIHighClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 12),
    _EspcAIHighClass_Type()
)
espcAIHighClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIHighClass.setStatus("current")
_EspcAILowValue_Type = Integer32
_EspcAILowValue_Object = MibTableColumn
espcAILowValue = _EspcAILowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 16),
    _EspcAILowValue_Type()
)
espcAILowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAILowValue.setStatus("current")
_EspcAILowClass_Type = DisplayString
_EspcAILowClass_Object = MibTableColumn
espcAILowClass = _EspcAILowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 19),
    _EspcAILowClass_Type()
)
espcAILowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAILowClass.setStatus("current")
_EspcAIVlowValue_Type = Integer32
_EspcAIVlowValue_Object = MibTableColumn
espcAIVlowValue = _EspcAIVlowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 20),
    _EspcAIVlowValue_Type()
)
espcAIVlowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVlowValue.setStatus("current")
_EspcAIVlowClass_Type = DisplayString
_EspcAIVlowClass_Object = MibTableColumn
espcAIVlowClass = _EspcAIVlowClass_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 23),
    _EspcAIVlowClass_Type()
)
espcAIVlowClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIVlowClass.setStatus("current")
_EspcAIActions_Type = DisplayString
_EspcAIActions_Object = MibTableColumn
espcAIActions = _EspcAIActions_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 24),
    _EspcAIActions_Type()
)
espcAIActions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIActions.setStatus("current")
_EspcAIConvUnitName_Type = DisplayString
_EspcAIConvUnitName_Object = MibTableColumn
espcAIConvUnitName = _EspcAIConvUnitName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 25),
    _EspcAIConvUnitName_Type()
)
espcAIConvUnitName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvUnitName.setStatus("current")
_EspcAIConvLowValue_Type = Integer32
_EspcAIConvLowValue_Object = MibTableColumn
espcAIConvLowValue = _EspcAIConvLowValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 26),
    _EspcAIConvLowValue_Type()
)
espcAIConvLowValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvLowValue.setStatus("current")
_EspcAIConvLowUnit_Type = Integer32
_EspcAIConvLowUnit_Object = MibTableColumn
espcAIConvLowUnit = _EspcAIConvLowUnit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 27),
    _EspcAIConvLowUnit_Type()
)
espcAIConvLowUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvLowUnit.setStatus("current")
_EspcAIConvHighValue_Type = Integer32
_EspcAIConvHighValue_Object = MibTableColumn
espcAIConvHighValue = _EspcAIConvHighValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 28),
    _EspcAIConvHighValue_Type()
)
espcAIConvHighValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvHighValue.setStatus("current")
_EspcAIConvHighUnit_Type = Integer32
_EspcAIConvHighUnit_Object = MibTableColumn
espcAIConvHighUnit = _EspcAIConvHighUnit_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 5, 1, 29),
    _EspcAIConvHighUnit_Type()
)
espcAIConvHighUnit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcAIConvHighUnit.setStatus("current")
_EsPointConfigRelayTable_Object = MibTable
esPointConfigRelayTable = _EsPointConfigRelayTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 6)
)
if mibBuilder.loadTexts:
    esPointConfigRelayTable.setStatus("current")
_EsPointConfigRelayEntry_Object = MibTableRow
esPointConfigRelayEntry = _EsPointConfigRelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 6, 1)
)
esPointConfigRelayEntry.setIndexNames(
    (0, "SITEBOSS-420-STD-MIB", "espcRelayIndexES"),
    (0, "SITEBOSS-420-STD-MIB", "espcRelayIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointConfigRelayEntry.setStatus("current")


class _EspcRelayIndexES_Type(Integer32):
    """Custom type espcRelayIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EspcRelayIndexES_Type.__name__ = "Integer32"
_EspcRelayIndexES_Object = MibTableColumn
espcRelayIndexES = _EspcRelayIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 6, 1, 1),
    _EspcRelayIndexES_Type()
)
espcRelayIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcRelayIndexES.setStatus("current")


class _EspcRelayIndexPoint_Type(Integer32):
    """Custom type espcRelayIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EspcRelayIndexPoint_Type.__name__ = "Integer32"
_EspcRelayIndexPoint_Object = MibTableColumn
espcRelayIndexPoint = _EspcRelayIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 6, 1, 2),
    _EspcRelayIndexPoint_Type()
)
espcRelayIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    espcRelayIndexPoint.setStatus("current")
_EspcRelayEnable_Type = DisplayString
_EspcRelayEnable_Object = MibTableColumn
espcRelayEnable = _EspcRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 6, 1, 3),
    _EspcRelayEnable_Type()
)
espcRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcRelayEnable.setStatus("current")
_EspcRelayName_Type = DisplayString
_EspcRelayName_Object = MibTableColumn
espcRelayName = _EspcRelayName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 2, 6, 1, 4),
    _EspcRelayName_Type()
)
espcRelayName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    espcRelayName.setStatus("current")
_Network_ObjectIdentity = ObjectIdentity
network = _Network_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4)
)
_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 1)
)
_IpAddress_Type = IpAddress
_IpAddress_Object = MibScalar
ipAddress = _IpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 1, 1),
    _IpAddress_Type()
)
ipAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipAddress.setStatus("current")
_SubnetMask_Type = IpAddress
_SubnetMask_Object = MibScalar
subnetMask = _SubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 1, 2),
    _SubnetMask_Type()
)
subnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetMask.setStatus("current")
_Router_Type = IpAddress
_Router_Object = MibScalar
router = _Router_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 1, 3),
    _Router_Type()
)
router.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    router.setStatus("current")
_Snmp_ObjectIdentity = ObjectIdentity
snmp = _Snmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 8)
)
_SnmpReadCommunity_Type = DisplayString
_SnmpReadCommunity_Object = MibScalar
snmpReadCommunity = _SnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 8, 2),
    _SnmpReadCommunity_Type()
)
snmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpReadCommunity.setStatus("current")
_SnmpWriteCommunity_Type = DisplayString
_SnmpWriteCommunity_Object = MibScalar
snmpWriteCommunity = _SnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 8, 3),
    _SnmpWriteCommunity_Type()
)
snmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpWriteCommunity.setStatus("current")
_SnmpTrapCommunity_Type = DisplayString
_SnmpTrapCommunity_Object = MibScalar
snmpTrapCommunity = _SnmpTrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 8, 4),
    _SnmpTrapCommunity_Type()
)
snmpTrapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTrapCommunity.setStatus("current")
_SnmpServerTable_Object = MibTable
snmpServerTable = _SnmpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 8, 6)
)
if mibBuilder.loadTexts:
    snmpServerTable.setStatus("current")
_SnmpServerEntry_Object = MibTableRow
snmpServerEntry = _SnmpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 8, 6, 1)
)
snmpServerEntry.setIndexNames(
    (0, "SITEBOSS-420-STD-MIB", "snmpServerIndex"),
)
if mibBuilder.loadTexts:
    snmpServerEntry.setStatus("current")


class _SnmpServerIndex_Type(Integer32):
    """Custom type snmpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_SnmpServerIndex_Type.__name__ = "Integer32"
_SnmpServerIndex_Object = MibTableColumn
snmpServerIndex = _SnmpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 8, 6, 1, 1),
    _SnmpServerIndex_Type()
)
snmpServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpServerIndex.setStatus("current")
_SnmpServer_Type = IpAddress
_SnmpServer_Object = MibTableColumn
snmpServer = _SnmpServer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 8, 6, 1, 2),
    _SnmpServer_Type()
)
snmpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpServer.setStatus("current")
_SnmpTestTrap_Type = DisplayString
_SnmpTestTrap_Object = MibScalar
snmpTestTrap = _SnmpTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 8, 7),
    _SnmpTestTrap_Type()
)
snmpTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpTestTrap.setStatus("current")
_Email_ObjectIdentity = ObjectIdentity
email = _Email_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17)
)
_EmailServer_Type = IpAddress
_EmailServer_Object = MibScalar
emailServer = _EmailServer_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17, 1),
    _EmailServer_Type()
)
emailServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailServer.setStatus("current")
_EmailDomain_Type = DisplayString
_EmailDomain_Object = MibScalar
emailDomain = _EmailDomain_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17, 2),
    _EmailDomain_Type()
)
emailDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailDomain.setStatus("current")
_EmailAuthEnable_Type = DisplayString
_EmailAuthEnable_Object = MibScalar
emailAuthEnable = _EmailAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17, 3),
    _EmailAuthEnable_Type()
)
emailAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailAuthEnable.setStatus("current")
_EmailAuthUsername_Type = DisplayString
_EmailAuthUsername_Object = MibScalar
emailAuthUsername = _EmailAuthUsername_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17, 4),
    _EmailAuthUsername_Type()
)
emailAuthUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailAuthUsername.setStatus("current")
_EmailAuthPassword_Type = DisplayString
_EmailAuthPassword_Object = MibScalar
emailAuthPassword = _EmailAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17, 5),
    _EmailAuthPassword_Type()
)
emailAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailAuthPassword.setStatus("current")
_EmailTable_Object = MibTable
emailTable = _EmailTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17, 6)
)
if mibBuilder.loadTexts:
    emailTable.setStatus("current")
_EmailEntry_Object = MibTableRow
emailEntry = _EmailEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17, 6, 1)
)
emailEntry.setIndexNames(
    (0, "SITEBOSS-420-STD-MIB", "emailIndex"),
)
if mibBuilder.loadTexts:
    emailEntry.setStatus("current")


class _EmailIndex_Type(Integer32):
    """Custom type emailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_EmailIndex_Type.__name__ = "Integer32"
_EmailIndex_Object = MibTableColumn
emailIndex = _EmailIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17, 6, 1, 1),
    _EmailIndex_Type()
)
emailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    emailIndex.setStatus("current")
_EmailAddress_Type = DisplayString
_EmailAddress_Object = MibTableColumn
emailAddress = _EmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17, 6, 1, 2),
    _EmailAddress_Type()
)
emailAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailAddress.setStatus("current")
_EmailTestMail_Type = DisplayString
_EmailTestMail_Object = MibScalar
emailTestMail = _EmailTestMail_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 4, 17, 7),
    _EmailTestMail_Type()
)
emailTestMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emailTestMail.setStatus("current")
_DateTime_ObjectIdentity = ObjectIdentity
dateTime = _DateTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 8)
)
_Date_Type = DisplayString
_Date_Object = MibScalar
date = _Date_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 8, 1),
    _Date_Type()
)
date.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    date.setStatus("current")
_Time_Type = DisplayString
_Time_Object = MibScalar
time = _Time_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 8, 2),
    _Time_Type()
)
time.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    time.setStatus("current")
_Autodst_Type = DisplayString
_Autodst_Object = MibScalar
autodst = _Autodst_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 8, 3),
    _Autodst_Type()
)
autodst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    autodst.setStatus("current")
_Action_ObjectIdentity = ObjectIdentity
action = _Action_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 14)
)
_ActionSystemAlertAction_Type = DisplayString
_ActionSystemAlertAction_Object = MibScalar
actionSystemAlertAction = _ActionSystemAlertAction_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 14, 1),
    _ActionSystemAlertAction_Type()
)
actionSystemAlertAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionSystemAlertAction.setStatus("current")
_ActionPowerupAlertEnable_Type = DisplayString
_ActionPowerupAlertEnable_Object = MibScalar
actionPowerupAlertEnable = _ActionPowerupAlertEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 14, 2),
    _ActionPowerupAlertEnable_Type()
)
actionPowerupAlertEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionPowerupAlertEnable.setStatus("current")
_ActionRTNAlertsEnable_Type = DisplayString
_ActionRTNAlertsEnable_Object = MibScalar
actionRTNAlertsEnable = _ActionRTNAlertsEnable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 14, 3),
    _ActionRTNAlertsEnable_Type()
)
actionRTNAlertsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionRTNAlertsEnable.setStatus("current")
_ActionAlarmRepeatFrequency_Type = Integer32
_ActionAlarmRepeatFrequency_Object = MibScalar
actionAlarmRepeatFrequency = _ActionAlarmRepeatFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 14, 4),
    _ActionAlarmRepeatFrequency_Type()
)
actionAlarmRepeatFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    actionAlarmRepeatFrequency.setStatus("current")
_Sys_ObjectIdentity = ObjectIdentity
sys = _Sys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 16)
)
_SysSerial_Type = DisplayString
_SysSerial_Object = MibScalar
sysSerial = _SysSerial_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 16, 1),
    _SysSerial_Type()
)
sysSerial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSerial.setStatus("current")
_SysVersion_Type = DisplayString
_SysVersion_Object = MibScalar
sysVersion = _SysVersion_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 16, 2),
    _SysVersion_Type()
)
sysVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysVersion.setStatus("current")
_SysBuild_Type = DisplayString
_SysBuild_Object = MibScalar
sysBuild = _SysBuild_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 16, 3),
    _SysBuild_Type()
)
sysBuild.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysBuild.setStatus("current")
_SysSitename_Type = DisplayString
_SysSitename_Object = MibScalar
sysSitename = _SysSitename_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 16, 4),
    _SysSitename_Type()
)
sysSitename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSitename.setStatus("current")
_SysProduct_Type = DisplayString
_SysProduct_Object = MibScalar
sysProduct = _SysProduct_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 16, 5),
    _SysProduct_Type()
)
sysProduct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysProduct.setStatus("current")
_ThisTrapText_Type = DisplayString
_ThisTrapText_Object = MibScalar
thisTrapText = _ThisTrapText_Object(
    (1, 3, 6, 1, 4, 1, 3052, 42, 2, 16, 6),
    _ThisTrapText_Type()
)
thisTrapText.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    thisTrapText.setStatus("current")

# Managed Objects groups


# Notification objects

s420PowerUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 42, 20000)
)
s420PowerUpTrap.setObjects(
      *(("SITEBOSS-420-STD-MIB", "thisTrapText"),
        ("SITEBOSS-420-STD-MIB", "sysSitename"))
)
if mibBuilder.loadTexts:
    s420PowerUpTrap.setStatus(
        "current"
    )

s420ContactTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 42, 20001)
)
s420ContactTrap.setObjects(
      *(("SITEBOSS-420-STD-MIB", "thisTrapText"),
        ("SITEBOSS-420-STD-MIB", "sysSitename"))
)
if mibBuilder.loadTexts:
    s420ContactTrap.setStatus(
        "current"
    )

s420TempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 42, 20010)
)
s420TempTrap.setObjects(
      *(("SITEBOSS-420-STD-MIB", "thisTrapText"),
        ("SITEBOSS-420-STD-MIB", "sysSitename"))
)
if mibBuilder.loadTexts:
    s420TempTrap.setStatus(
        "current"
    )

s420HumidTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 42, 20020)
)
s420HumidTrap.setObjects(
      *(("SITEBOSS-420-STD-MIB", "thisTrapText"),
        ("SITEBOSS-420-STD-MIB", "sysSitename"))
)
if mibBuilder.loadTexts:
    s420HumidTrap.setStatus(
        "current"
    )

s420TestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 42, 22000)
)
s420TestTrap.setObjects(
      *(("SITEBOSS-420-STD-MIB", "thisTrapText"),
        ("SITEBOSS-420-STD-MIB", "sysSitename"))
)
if mibBuilder.loadTexts:
    s420TestTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SITEBOSS-420-STD-MIB",
    **{"s420": s420,
       "notification": notification,
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
       "config": config,
       "eventSensorPointConfig": eventSensorPointConfig,
       "esPointConfigTempTable": esPointConfigTempTable,
       "esPointConfigTempEntry": esPointConfigTempEntry,
       "espcTempIndexES": espcTempIndexES,
       "espcTempIndexPoint": espcTempIndexPoint,
       "espcTempEnable": espcTempEnable,
       "espcTempName": espcTempName,
       "espcTempScale": espcTempScale,
       "espcTempDeadband": espcTempDeadband,
       "espcTempVHighTemp": espcTempVHighTemp,
       "espcTempVHighClass": espcTempVHighClass,
       "espcTempHighTemp": espcTempHighTemp,
       "espcTempHighClass": espcTempHighClass,
       "espcTempLowTemp": espcTempLowTemp,
       "espcTempLowClass": espcTempLowClass,
       "espcTempVLowTemp": espcTempVLowTemp,
       "espcTempVLowClass": espcTempVLowClass,
       "espcTempActions": espcTempActions,
       "esPointConfigCCTable": esPointConfigCCTable,
       "esPointConfigCCEntry": esPointConfigCCEntry,
       "espcCCIndexES": espcCCIndexES,
       "espcCCIndexPoint": espcCCIndexPoint,
       "espcCCEnable": espcCCEnable,
       "espcCCName": espcCCName,
       "espcCCEventState": espcCCEventState,
       "espcCCThreshold": espcCCThreshold,
       "espcCCActions": espcCCActions,
       "espcCCEventClass": espcCCEventClass,
       "espcCCNormalClass": espcCCNormalClass,
       "espcCCAlarmAlias": espcCCAlarmAlias,
       "espcCCNormalAlias": espcCCNormalAlias,
       "esPointConfigHumidTable": esPointConfigHumidTable,
       "esPointConfigHumidEntry": esPointConfigHumidEntry,
       "espcHumidIndexES": espcHumidIndexES,
       "espcHumidIndexPoint": espcHumidIndexPoint,
       "espcHumidEnable": espcHumidEnable,
       "espcHumidName": espcHumidName,
       "espcHumidDeadband": espcHumidDeadband,
       "espcHumidVHighHumid": espcHumidVHighHumid,
       "espcHumidVHighClass": espcHumidVHighClass,
       "espcHumidHighHumid": espcHumidHighHumid,
       "espcHumidHighClass": espcHumidHighClass,
       "espcHumidLowHumid": espcHumidLowHumid,
       "espcHumidLowClass": espcHumidLowClass,
       "espcHumidVLowHumid": espcHumidVLowHumid,
       "espcHumidVLowClass": espcHumidVLowClass,
       "espcHumidActions": espcHumidActions,
       "esPointConfigAITable": esPointConfigAITable,
       "esPointConfigAIEntry": esPointConfigAIEntry,
       "espcAIIndexES": espcAIIndexES,
       "espcAIIndexPoint": espcAIIndexPoint,
       "espcAIEnable": espcAIEnable,
       "espcAIName": espcAIName,
       "espcAIDeadband": espcAIDeadband,
       "espcAIVhighValue": espcAIVhighValue,
       "espcAIVhighClass": espcAIVhighClass,
       "espcAIHighValue": espcAIHighValue,
       "espcAIHighClass": espcAIHighClass,
       "espcAILowValue": espcAILowValue,
       "espcAILowClass": espcAILowClass,
       "espcAIVlowValue": espcAIVlowValue,
       "espcAIVlowClass": espcAIVlowClass,
       "espcAIActions": espcAIActions,
       "espcAIConvUnitName": espcAIConvUnitName,
       "espcAIConvLowValue": espcAIConvLowValue,
       "espcAIConvLowUnit": espcAIConvLowUnit,
       "espcAIConvHighValue": espcAIConvHighValue,
       "espcAIConvHighUnit": espcAIConvHighUnit,
       "esPointConfigRelayTable": esPointConfigRelayTable,
       "esPointConfigRelayEntry": esPointConfigRelayEntry,
       "espcRelayIndexES": espcRelayIndexES,
       "espcRelayIndexPoint": espcRelayIndexPoint,
       "espcRelayEnable": espcRelayEnable,
       "espcRelayName": espcRelayName,
       "network": network,
       "ethernet": ethernet,
       "ipAddress": ipAddress,
       "subnetMask": subnetMask,
       "router": router,
       "snmp": snmp,
       "snmpReadCommunity": snmpReadCommunity,
       "snmpWriteCommunity": snmpWriteCommunity,
       "snmpTrapCommunity": snmpTrapCommunity,
       "snmpServerTable": snmpServerTable,
       "snmpServerEntry": snmpServerEntry,
       "snmpServerIndex": snmpServerIndex,
       "snmpServer": snmpServer,
       "snmpTestTrap": snmpTestTrap,
       "email": email,
       "emailServer": emailServer,
       "emailDomain": emailDomain,
       "emailAuthEnable": emailAuthEnable,
       "emailAuthUsername": emailAuthUsername,
       "emailAuthPassword": emailAuthPassword,
       "emailTable": emailTable,
       "emailEntry": emailEntry,
       "emailIndex": emailIndex,
       "emailAddress": emailAddress,
       "emailTestMail": emailTestMail,
       "dateTime": dateTime,
       "date": date,
       "time": time,
       "autodst": autodst,
       "action": action,
       "actionSystemAlertAction": actionSystemAlertAction,
       "actionPowerupAlertEnable": actionPowerupAlertEnable,
       "actionRTNAlertsEnable": actionRTNAlertsEnable,
       "actionAlarmRepeatFrequency": actionAlarmRepeatFrequency,
       "sys": sys,
       "sysSerial": sysSerial,
       "sysVersion": sysVersion,
       "sysBuild": sysBuild,
       "sysSitename": sysSitename,
       "sysProduct": sysProduct,
       "thisTrapText": thisTrapText,
       "s420PowerUpTrap": s420PowerUpTrap,
       "s420ContactTrap": s420ContactTrap,
       "s420TempTrap": s420TempTrap,
       "s420HumidTrap": s420HumidTrap,
       "s420TestTrap": s420TestTrap}
)
