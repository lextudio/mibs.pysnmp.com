# SNMP MIB module (DL80-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DL80-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:33 2024
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
 ObjectName,
 NotificationType,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "ObjectName",
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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

_Omnitronix_ObjectIdentity = ObjectIdentity
omnitronix = _Omnitronix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052)
)
_Dl80_ObjectIdentity = ObjectIdentity
dl80 = _Dl80_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 7)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 7, 1)
)
_EventSensorStatus_ObjectIdentity = ObjectIdentity
eventSensorStatus = _EventSensorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 7, 1, 1)
)
_EsPointTable_Object = MibTable
esPointTable = _EsPointTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    esPointTable.setStatus("mandatory")
_EsPointEntry_Object = MibTableRow
esPointEntry = _EsPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 1, 1, 1, 1)
)
esPointEntry.setIndexNames(
    (0, "DL80-STD-MIB", "esIndexES"),
    (0, "DL80-STD-MIB", "esIndexPC"),
    (0, "DL80-STD-MIB", "esIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointEntry.setStatus("mandatory")


class _EsIndexES_Type(Integer32):
    """Custom type esIndexES based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EsIndexES_Type.__name__ = "Integer32"
_EsIndexES_Object = MibTableColumn
esIndexES = _EsIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 1, 1, 1, 1, 1),
    _EsIndexES_Type()
)
esIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexES.setStatus("mandatory")


class _EsIndexPC_Type(Integer32):
    """Custom type esIndexPC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_EsIndexPC_Type.__name__ = "Integer32"
_EsIndexPC_Object = MibTableColumn
esIndexPC = _EsIndexPC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 1, 1, 1, 1, 2),
    _EsIndexPC_Type()
)
esIndexPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPC.setStatus("mandatory")


class _EsIndexPoint_Type(Integer32):
    """Custom type esIndexPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EsIndexPoint_Type.__name__ = "Integer32"
_EsIndexPoint_Object = MibTableColumn
esIndexPoint = _EsIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 1, 1, 1, 1, 3),
    _EsIndexPoint_Type()
)
esIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPoint.setStatus("mandatory")
_EsPointName_Type = DisplayString
_EsPointName_Object = MibTableColumn
esPointName = _EsPointName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 1, 1, 1, 1, 4),
    _EsPointName_Type()
)
esPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointName.setStatus("mandatory")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 7, 2)
)
_EventSensorBasics_ObjectIdentity = ObjectIdentity
eventSensorBasics = _EventSensorBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 7, 2, 1)
)
_EsNumberEventSensors_Type = Integer32
_EsNumberEventSensors_Object = MibScalar
esNumberEventSensors = _EsNumberEventSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 2, 1, 1),
    _EsNumberEventSensors_Type()
)
esNumberEventSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberEventSensors.setStatus("mandatory")
_EsTable_Object = MibTable
esTable = _EsTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 2, 1, 2)
)
if mibBuilder.loadTexts:
    esTable.setStatus("mandatory")
_EsEntry_Object = MibTableRow
esEntry = _EsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 2, 1, 2, 1)
)
esEntry.setIndexNames(
    (0, "DL80-STD-MIB", "esIndex"),
)
if mibBuilder.loadTexts:
    esEntry.setStatus("mandatory")


class _EsIndex_Type(Integer32):
    """Custom type esIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_EsIndex_Type.__name__ = "Integer32"
_EsIndex_Object = MibTableColumn
esIndex = _EsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 2, 1, 2, 1, 1),
    _EsIndex_Type()
)
esIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndex.setStatus("mandatory")
_EsName_Type = DisplayString
_EsName_Object = MibTableColumn
esName = _EsName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 2, 1, 2, 1, 2),
    _EsName_Type()
)
esName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esName.setStatus("mandatory")
_EsID_Type = DisplayString
_EsID_Object = MibTableColumn
esID = _EsID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 2, 1, 2, 1, 3),
    _EsID_Type()
)
esID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esID.setStatus("mandatory")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 7, 2, 8)
)
_Clock_Type = DisplayString
_Clock_Object = MibScalar
clock = _Clock_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 2, 8, 1),
    _Clock_Type()
)
clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clock.setStatus("mandatory")
_ProductIds_ObjectIdentity = ObjectIdentity
productIds = _ProductIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 7, 3)
)
_SiteID_Type = DisplayString
_SiteID_Object = MibScalar
siteID = _SiteID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 3, 1),
    _SiteID_Type()
)
siteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    siteID.setStatus("mandatory")
_StockTrapString_Type = DisplayString
_StockTrapString_Object = MibScalar
stockTrapString = _StockTrapString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 3, 3),
    _StockTrapString_Type()
)
stockTrapString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stockTrapString.setStatus("mandatory")
_TrapEventTypeNumber_Type = Integer32
_TrapEventTypeNumber_Object = MibScalar
trapEventTypeNumber = _TrapEventTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 3, 4),
    _TrapEventTypeNumber_Type()
)
trapEventTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventTypeNumber.setStatus("mandatory")
_TrapEventTypeName_Type = DisplayString
_TrapEventTypeName_Object = MibScalar
trapEventTypeName = _TrapEventTypeName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 3, 5),
    _TrapEventTypeName_Type()
)
trapEventTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventTypeName.setStatus("mandatory")


class _TrapIncludedValue_Type(Integer32):
    """Custom type trapIncludedValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-32768, 32767),
    )


_TrapIncludedValue_Type.__name__ = "Integer32"
_TrapIncludedValue_Object = MibScalar
trapIncludedValue = _TrapIncludedValue_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 3, 6),
    _TrapIncludedValue_Type()
)
trapIncludedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIncludedValue.setStatus("mandatory")
_TrapIncludedString_Type = DisplayString
_TrapIncludedString_Object = MibScalar
trapIncludedString = _TrapIncludedString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 3, 7),
    _TrapIncludedString_Type()
)
trapIncludedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIncludedString.setStatus("mandatory")
_TrapTypeString_Type = DisplayString
_TrapTypeString_Object = MibScalar
trapTypeString = _TrapTypeString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 3, 8),
    _TrapTypeString_Type()
)
trapTypeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapTypeString.setStatus("mandatory")
_TrapEventClassNumber_Type = Integer32
_TrapEventClassNumber_Object = MibScalar
trapEventClassNumber = _TrapEventClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 3, 9),
    _TrapEventClassNumber_Type()
)
trapEventClassNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventClassNumber.setStatus("mandatory")
_TrapEventClassName_Type = Integer32
_TrapEventClassName_Object = MibScalar
trapEventClassName = _TrapEventClassName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 7, 3, 10),
    _TrapEventClassName_Type()
)
trapEventClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventClassName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dl80StockContactClosureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 110)
)
dl80StockContactClosureTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    dl80StockContactClosureTrap.setStatus(
        ""
    )

dl80StockTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 120)
)
dl80StockTempTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    dl80StockTempTrap.setStatus(
        ""
    )

dl80StockHumidityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 130)
)
dl80StockHumidityTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    dl80StockHumidityTrap.setStatus(
        ""
    )

dl80StockAnalogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 140)
)
dl80StockAnalogTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    dl80StockAnalogTrap.setStatus(
        ""
    )

dl80UserTrap180 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 180)
)
dl80UserTrap180.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap180.setStatus(
        ""
    )

dl80StockDbasePfullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 501)
)
dl80StockDbasePfullTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"),
        ("DL80-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl80StockDbasePfullTrap.setStatus(
        ""
    )

dl80StockDataAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 503)
)
dl80StockDataAlarmTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"),
        ("DL80-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl80StockDataAlarmTrap.setStatus(
        ""
    )

dl80StockNoDataAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 505)
)
dl80StockNoDataAlarmTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"),
        ("DL80-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl80StockNoDataAlarmTrap.setStatus(
        ""
    )

dl80StockSchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 506)
)
dl80StockSchedTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"),
        ("DL80-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl80StockSchedTrap.setStatus(
        ""
    )

dl80StockImmediateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 507)
)
dl80StockImmediateTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"),
        ("DL80-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl80StockImmediateTrap.setStatus(
        ""
    )

dl80StockSocketLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 508)
)
dl80StockSocketLostTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"),
        ("DL80-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl80StockSocketLostTrap.setStatus(
        ""
    )

dl80StockCTSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 510)
)
dl80StockCTSTrap.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "stockTrapString"),
        ("DL80-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl80StockCTSTrap.setStatus(
        ""
    )

dl80UserTrap1000 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1000)
)
dl80UserTrap1000.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1000.setStatus(
        ""
    )

dl80UserTrap1001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1001)
)
dl80UserTrap1001.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1001.setStatus(
        ""
    )

dl80UserTrap1002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1002)
)
dl80UserTrap1002.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1002.setStatus(
        ""
    )

dl80UserTrap1003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1003)
)
dl80UserTrap1003.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1003.setStatus(
        ""
    )

dl80UserTrap1004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1004)
)
dl80UserTrap1004.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1004.setStatus(
        ""
    )

dl80UserTrap1005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1005)
)
dl80UserTrap1005.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1005.setStatus(
        ""
    )

dl80UserTrap1006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1006)
)
dl80UserTrap1006.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1006.setStatus(
        ""
    )

dl80UserTrap1007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1007)
)
dl80UserTrap1007.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1007.setStatus(
        ""
    )

dl80UserTrap1008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1008)
)
dl80UserTrap1008.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1008.setStatus(
        ""
    )

dl80UserTrap1009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1009)
)
dl80UserTrap1009.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1009.setStatus(
        ""
    )

dl80UserTrap1010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1010)
)
dl80UserTrap1010.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1010.setStatus(
        ""
    )

dl80UserTrap1011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1011)
)
dl80UserTrap1011.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1011.setStatus(
        ""
    )

dl80UserTrap1012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1012)
)
dl80UserTrap1012.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1012.setStatus(
        ""
    )

dl80UserTrap1013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1013)
)
dl80UserTrap1013.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1013.setStatus(
        ""
    )

dl80UserTrap1014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1014)
)
dl80UserTrap1014.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1014.setStatus(
        ""
    )

dl80UserTrap1015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1015)
)
dl80UserTrap1015.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1015.setStatus(
        ""
    )

dl80UserTrap1016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1016)
)
dl80UserTrap1016.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1016.setStatus(
        ""
    )

dl80UserTrap1017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1017)
)
dl80UserTrap1017.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1017.setStatus(
        ""
    )

dl80UserTrap1018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1018)
)
dl80UserTrap1018.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1018.setStatus(
        ""
    )

dl80UserTrap1019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1019)
)
dl80UserTrap1019.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1019.setStatus(
        ""
    )

dl80UserTrap1020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1020)
)
dl80UserTrap1020.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1020.setStatus(
        ""
    )

dl80UserTrap1021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1021)
)
dl80UserTrap1021.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1021.setStatus(
        ""
    )

dl80UserTrap1022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1022)
)
dl80UserTrap1022.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1022.setStatus(
        ""
    )

dl80UserTrap1023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1023)
)
dl80UserTrap1023.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1023.setStatus(
        ""
    )

dl80UserTrap1024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1024)
)
dl80UserTrap1024.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1024.setStatus(
        ""
    )

dl80UserTrap1025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1025)
)
dl80UserTrap1025.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1025.setStatus(
        ""
    )

dl80UserTrap1026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1026)
)
dl80UserTrap1026.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1026.setStatus(
        ""
    )

dl80UserTrap1027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1027)
)
dl80UserTrap1027.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1027.setStatus(
        ""
    )

dl80UserTrap1028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1028)
)
dl80UserTrap1028.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1028.setStatus(
        ""
    )

dl80UserTrap1029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1029)
)
dl80UserTrap1029.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1029.setStatus(
        ""
    )

dl80UserTrap1030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1030)
)
dl80UserTrap1030.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1030.setStatus(
        ""
    )

dl80UserTrap1031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1031)
)
dl80UserTrap1031.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1031.setStatus(
        ""
    )

dl80UserTrap1032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1032)
)
dl80UserTrap1032.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1032.setStatus(
        ""
    )

dl80UserTrap1033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1033)
)
dl80UserTrap1033.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1033.setStatus(
        ""
    )

dl80UserTrap1034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1034)
)
dl80UserTrap1034.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1034.setStatus(
        ""
    )

dl80UserTrap1035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1035)
)
dl80UserTrap1035.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1035.setStatus(
        ""
    )

dl80UserTrap1036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1036)
)
dl80UserTrap1036.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1036.setStatus(
        ""
    )

dl80UserTrap1037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1037)
)
dl80UserTrap1037.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1037.setStatus(
        ""
    )

dl80UserTrap1038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1038)
)
dl80UserTrap1038.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1038.setStatus(
        ""
    )

dl80UserTrap1039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1039)
)
dl80UserTrap1039.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1039.setStatus(
        ""
    )

dl80UserTrap1040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1040)
)
dl80UserTrap1040.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1040.setStatus(
        ""
    )

dl80UserTrap1041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1041)
)
dl80UserTrap1041.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1041.setStatus(
        ""
    )

dl80UserTrap1042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1042)
)
dl80UserTrap1042.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1042.setStatus(
        ""
    )

dl80UserTrap1043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1043)
)
dl80UserTrap1043.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1043.setStatus(
        ""
    )

dl80UserTrap1044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1044)
)
dl80UserTrap1044.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1044.setStatus(
        ""
    )

dl80UserTrap1045 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1045)
)
dl80UserTrap1045.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1045.setStatus(
        ""
    )

dl80UserTrap1046 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1046)
)
dl80UserTrap1046.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1046.setStatus(
        ""
    )

dl80UserTrap1047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1047)
)
dl80UserTrap1047.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1047.setStatus(
        ""
    )

dl80UserTrap1048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1048)
)
dl80UserTrap1048.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1048.setStatus(
        ""
    )

dl80UserTrap1049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1049)
)
dl80UserTrap1049.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1049.setStatus(
        ""
    )

dl80UserTrap1050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1050)
)
dl80UserTrap1050.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1050.setStatus(
        ""
    )

dl80UserTrap1051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1051)
)
dl80UserTrap1051.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1051.setStatus(
        ""
    )

dl80UserTrap1052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1052)
)
dl80UserTrap1052.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1052.setStatus(
        ""
    )

dl80UserTrap1053 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1053)
)
dl80UserTrap1053.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1053.setStatus(
        ""
    )

dl80UserTrap1054 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1054)
)
dl80UserTrap1054.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1054.setStatus(
        ""
    )

dl80UserTrap1055 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1055)
)
dl80UserTrap1055.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1055.setStatus(
        ""
    )

dl80UserTrap1056 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1056)
)
dl80UserTrap1056.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1056.setStatus(
        ""
    )

dl80UserTrap1057 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1057)
)
dl80UserTrap1057.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1057.setStatus(
        ""
    )

dl80UserTrap1058 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1058)
)
dl80UserTrap1058.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1058.setStatus(
        ""
    )

dl80UserTrap1059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1059)
)
dl80UserTrap1059.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1059.setStatus(
        ""
    )

dl80UserTrap1060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1060)
)
dl80UserTrap1060.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1060.setStatus(
        ""
    )

dl80UserTrap1061 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1061)
)
dl80UserTrap1061.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1061.setStatus(
        ""
    )

dl80UserTrap1062 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1062)
)
dl80UserTrap1062.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1062.setStatus(
        ""
    )

dl80UserTrap1063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1063)
)
dl80UserTrap1063.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1063.setStatus(
        ""
    )

dl80UserTrap1064 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1064)
)
dl80UserTrap1064.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1064.setStatus(
        ""
    )

dl80UserTrap1065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1065)
)
dl80UserTrap1065.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1065.setStatus(
        ""
    )

dl80UserTrap1066 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1066)
)
dl80UserTrap1066.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1066.setStatus(
        ""
    )

dl80UserTrap1067 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1067)
)
dl80UserTrap1067.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1067.setStatus(
        ""
    )

dl80UserTrap1068 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1068)
)
dl80UserTrap1068.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1068.setStatus(
        ""
    )

dl80UserTrap1069 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1069)
)
dl80UserTrap1069.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1069.setStatus(
        ""
    )

dl80UserTrap1070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1070)
)
dl80UserTrap1070.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1070.setStatus(
        ""
    )

dl80UserTrap1071 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1071)
)
dl80UserTrap1071.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1071.setStatus(
        ""
    )

dl80UserTrap1072 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1072)
)
dl80UserTrap1072.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1072.setStatus(
        ""
    )

dl80UserTrap1073 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1073)
)
dl80UserTrap1073.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1073.setStatus(
        ""
    )

dl80UserTrap1074 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1074)
)
dl80UserTrap1074.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1074.setStatus(
        ""
    )

dl80UserTrap1075 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1075)
)
dl80UserTrap1075.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1075.setStatus(
        ""
    )

dl80UserTrap1076 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1076)
)
dl80UserTrap1076.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1076.setStatus(
        ""
    )

dl80UserTrap1077 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1077)
)
dl80UserTrap1077.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1077.setStatus(
        ""
    )

dl80UserTrap1078 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1078)
)
dl80UserTrap1078.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1078.setStatus(
        ""
    )

dl80UserTrap1079 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1079)
)
dl80UserTrap1079.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1079.setStatus(
        ""
    )

dl80UserTrap1080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1080)
)
dl80UserTrap1080.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1080.setStatus(
        ""
    )

dl80UserTrap1081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1081)
)
dl80UserTrap1081.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1081.setStatus(
        ""
    )

dl80UserTrap1082 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1082)
)
dl80UserTrap1082.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1082.setStatus(
        ""
    )

dl80UserTrap1083 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1083)
)
dl80UserTrap1083.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1083.setStatus(
        ""
    )

dl80UserTrap1084 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1084)
)
dl80UserTrap1084.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1084.setStatus(
        ""
    )

dl80UserTrap1085 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1085)
)
dl80UserTrap1085.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1085.setStatus(
        ""
    )

dl80UserTrap1086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1086)
)
dl80UserTrap1086.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1086.setStatus(
        ""
    )

dl80UserTrap1087 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1087)
)
dl80UserTrap1087.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1087.setStatus(
        ""
    )

dl80UserTrap1088 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1088)
)
dl80UserTrap1088.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1088.setStatus(
        ""
    )

dl80UserTrap1089 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1089)
)
dl80UserTrap1089.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1089.setStatus(
        ""
    )

dl80UserTrap1090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1090)
)
dl80UserTrap1090.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1090.setStatus(
        ""
    )

dl80UserTrap1091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1091)
)
dl80UserTrap1091.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1091.setStatus(
        ""
    )

dl80UserTrap1092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1092)
)
dl80UserTrap1092.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1092.setStatus(
        ""
    )

dl80UserTrap1093 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1093)
)
dl80UserTrap1093.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1093.setStatus(
        ""
    )

dl80UserTrap1094 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1094)
)
dl80UserTrap1094.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1094.setStatus(
        ""
    )

dl80UserTrap1095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1095)
)
dl80UserTrap1095.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1095.setStatus(
        ""
    )

dl80UserTrap1096 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1096)
)
dl80UserTrap1096.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1096.setStatus(
        ""
    )

dl80UserTrap1097 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1097)
)
dl80UserTrap1097.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1097.setStatus(
        ""
    )

dl80UserTrap1098 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1098)
)
dl80UserTrap1098.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1098.setStatus(
        ""
    )

dl80UserTrap1099 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1099)
)
dl80UserTrap1099.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1099.setStatus(
        ""
    )

dl80UserTrap1100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1100)
)
dl80UserTrap1100.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1100.setStatus(
        ""
    )

dl80UserTrap1101 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1101)
)
dl80UserTrap1101.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1101.setStatus(
        ""
    )

dl80UserTrap1102 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1102)
)
dl80UserTrap1102.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1102.setStatus(
        ""
    )

dl80UserTrap1103 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1103)
)
dl80UserTrap1103.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1103.setStatus(
        ""
    )

dl80UserTrap1104 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1104)
)
dl80UserTrap1104.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1104.setStatus(
        ""
    )

dl80UserTrap1105 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1105)
)
dl80UserTrap1105.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1105.setStatus(
        ""
    )

dl80UserTrap1106 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1106)
)
dl80UserTrap1106.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1106.setStatus(
        ""
    )

dl80UserTrap1107 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1107)
)
dl80UserTrap1107.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1107.setStatus(
        ""
    )

dl80UserTrap1108 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1108)
)
dl80UserTrap1108.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1108.setStatus(
        ""
    )

dl80UserTrap1109 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1109)
)
dl80UserTrap1109.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1109.setStatus(
        ""
    )

dl80UserTrap1110 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1110)
)
dl80UserTrap1110.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1110.setStatus(
        ""
    )

dl80UserTrap1111 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1111)
)
dl80UserTrap1111.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1111.setStatus(
        ""
    )

dl80UserTrap1112 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1112)
)
dl80UserTrap1112.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1112.setStatus(
        ""
    )

dl80UserTrap1113 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1113)
)
dl80UserTrap1113.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1113.setStatus(
        ""
    )

dl80UserTrap1114 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1114)
)
dl80UserTrap1114.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1114.setStatus(
        ""
    )

dl80UserTrap1115 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1115)
)
dl80UserTrap1115.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1115.setStatus(
        ""
    )

dl80UserTrap1116 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1116)
)
dl80UserTrap1116.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1116.setStatus(
        ""
    )

dl80UserTrap1117 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1117)
)
dl80UserTrap1117.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1117.setStatus(
        ""
    )

dl80UserTrap1118 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1118)
)
dl80UserTrap1118.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1118.setStatus(
        ""
    )

dl80UserTrap1119 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1119)
)
dl80UserTrap1119.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1119.setStatus(
        ""
    )

dl80UserTrap1120 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1120)
)
dl80UserTrap1120.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1120.setStatus(
        ""
    )

dl80UserTrap1121 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1121)
)
dl80UserTrap1121.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1121.setStatus(
        ""
    )

dl80UserTrap1122 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1122)
)
dl80UserTrap1122.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1122.setStatus(
        ""
    )

dl80UserTrap1123 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1123)
)
dl80UserTrap1123.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1123.setStatus(
        ""
    )

dl80UserTrap1124 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1124)
)
dl80UserTrap1124.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1124.setStatus(
        ""
    )

dl80UserTrap1125 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1125)
)
dl80UserTrap1125.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1125.setStatus(
        ""
    )

dl80UserTrap1126 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1126)
)
dl80UserTrap1126.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1126.setStatus(
        ""
    )

dl80UserTrap1127 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1127)
)
dl80UserTrap1127.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1127.setStatus(
        ""
    )

dl80UserTrap1128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1128)
)
dl80UserTrap1128.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1128.setStatus(
        ""
    )

dl80UserTrap1129 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1129)
)
dl80UserTrap1129.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1129.setStatus(
        ""
    )

dl80UserTrap1130 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1130)
)
dl80UserTrap1130.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1130.setStatus(
        ""
    )

dl80UserTrap1131 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1131)
)
dl80UserTrap1131.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1131.setStatus(
        ""
    )

dl80UserTrap1132 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1132)
)
dl80UserTrap1132.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1132.setStatus(
        ""
    )

dl80UserTrap1133 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1133)
)
dl80UserTrap1133.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1133.setStatus(
        ""
    )

dl80UserTrap1134 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1134)
)
dl80UserTrap1134.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1134.setStatus(
        ""
    )

dl80UserTrap1135 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1135)
)
dl80UserTrap1135.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1135.setStatus(
        ""
    )

dl80UserTrap1136 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1136)
)
dl80UserTrap1136.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1136.setStatus(
        ""
    )

dl80UserTrap1137 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1137)
)
dl80UserTrap1137.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1137.setStatus(
        ""
    )

dl80UserTrap1138 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1138)
)
dl80UserTrap1138.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1138.setStatus(
        ""
    )

dl80UserTrap1139 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1139)
)
dl80UserTrap1139.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1139.setStatus(
        ""
    )

dl80UserTrap1140 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1140)
)
dl80UserTrap1140.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1140.setStatus(
        ""
    )

dl80UserTrap1141 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1141)
)
dl80UserTrap1141.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1141.setStatus(
        ""
    )

dl80UserTrap1142 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1142)
)
dl80UserTrap1142.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1142.setStatus(
        ""
    )

dl80UserTrap1143 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1143)
)
dl80UserTrap1143.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1143.setStatus(
        ""
    )

dl80UserTrap1144 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1144)
)
dl80UserTrap1144.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1144.setStatus(
        ""
    )

dl80UserTrap1145 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1145)
)
dl80UserTrap1145.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1145.setStatus(
        ""
    )

dl80UserTrap1146 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1146)
)
dl80UserTrap1146.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1146.setStatus(
        ""
    )

dl80UserTrap1147 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1147)
)
dl80UserTrap1147.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1147.setStatus(
        ""
    )

dl80UserTrap1148 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1148)
)
dl80UserTrap1148.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1148.setStatus(
        ""
    )

dl80UserTrap1149 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1149)
)
dl80UserTrap1149.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1149.setStatus(
        ""
    )

dl80UserTrap1150 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1150)
)
dl80UserTrap1150.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1150.setStatus(
        ""
    )

dl80UserTrap1151 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1151)
)
dl80UserTrap1151.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1151.setStatus(
        ""
    )

dl80UserTrap1152 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1152)
)
dl80UserTrap1152.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1152.setStatus(
        ""
    )

dl80UserTrap1153 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1153)
)
dl80UserTrap1153.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1153.setStatus(
        ""
    )

dl80UserTrap1154 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1154)
)
dl80UserTrap1154.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1154.setStatus(
        ""
    )

dl80UserTrap1155 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1155)
)
dl80UserTrap1155.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1155.setStatus(
        ""
    )

dl80UserTrap1156 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1156)
)
dl80UserTrap1156.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1156.setStatus(
        ""
    )

dl80UserTrap1157 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1157)
)
dl80UserTrap1157.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1157.setStatus(
        ""
    )

dl80UserTrap1158 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1158)
)
dl80UserTrap1158.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1158.setStatus(
        ""
    )

dl80UserTrap1159 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1159)
)
dl80UserTrap1159.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1159.setStatus(
        ""
    )

dl80UserTrap1161 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1161)
)
dl80UserTrap1161.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1161.setStatus(
        ""
    )

dl80UserTrap1162 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1162)
)
dl80UserTrap1162.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1162.setStatus(
        ""
    )

dl80UserTrap1163 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1163)
)
dl80UserTrap1163.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1163.setStatus(
        ""
    )

dl80UserTrap1164 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1164)
)
dl80UserTrap1164.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1164.setStatus(
        ""
    )

dl80UserTrap1165 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1165)
)
dl80UserTrap1165.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1165.setStatus(
        ""
    )

dl80UserTrap1166 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1166)
)
dl80UserTrap1166.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1166.setStatus(
        ""
    )

dl80UserTrap1167 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1167)
)
dl80UserTrap1167.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1167.setStatus(
        ""
    )

dl80UserTrap1168 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1168)
)
dl80UserTrap1168.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1168.setStatus(
        ""
    )

dl80UserTrap1169 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1169)
)
dl80UserTrap1169.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1169.setStatus(
        ""
    )

dl80UserTrap1170 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1170)
)
dl80UserTrap1170.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1170.setStatus(
        ""
    )

dl80UserTrap1171 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1171)
)
dl80UserTrap1171.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1171.setStatus(
        ""
    )

dl80UserTrap1172 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1172)
)
dl80UserTrap1172.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1172.setStatus(
        ""
    )

dl80UserTrap1173 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1173)
)
dl80UserTrap1173.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1173.setStatus(
        ""
    )

dl80UserTrap1174 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1174)
)
dl80UserTrap1174.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1174.setStatus(
        ""
    )

dl80UserTrap1175 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1175)
)
dl80UserTrap1175.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1175.setStatus(
        ""
    )

dl80UserTrap1176 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1176)
)
dl80UserTrap1176.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1176.setStatus(
        ""
    )

dl80UserTrap1177 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1177)
)
dl80UserTrap1177.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1177.setStatus(
        ""
    )

dl80UserTrap1178 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1178)
)
dl80UserTrap1178.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1178.setStatus(
        ""
    )

dl80UserTrap1179 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1179)
)
dl80UserTrap1179.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1179.setStatus(
        ""
    )

dl80UserTrap1180 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1180)
)
dl80UserTrap1180.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1180.setStatus(
        ""
    )

dl80UserTrap1181 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1181)
)
dl80UserTrap1181.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1181.setStatus(
        ""
    )

dl80UserTrap1182 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1182)
)
dl80UserTrap1182.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1182.setStatus(
        ""
    )

dl80UserTrap1183 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1183)
)
dl80UserTrap1183.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1183.setStatus(
        ""
    )

dl80UserTrap1184 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1184)
)
dl80UserTrap1184.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1184.setStatus(
        ""
    )

dl80UserTrap1185 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1185)
)
dl80UserTrap1185.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1185.setStatus(
        ""
    )

dl80UserTrap1186 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1186)
)
dl80UserTrap1186.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1186.setStatus(
        ""
    )

dl80UserTrap1187 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1187)
)
dl80UserTrap1187.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1187.setStatus(
        ""
    )

dl80UserTrap1188 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1188)
)
dl80UserTrap1188.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1188.setStatus(
        ""
    )

dl80UserTrap1189 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1189)
)
dl80UserTrap1189.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1189.setStatus(
        ""
    )

dl80UserTrap1190 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1190)
)
dl80UserTrap1190.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1190.setStatus(
        ""
    )

dl80UserTrap1191 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1191)
)
dl80UserTrap1191.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1191.setStatus(
        ""
    )

dl80UserTrap1192 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1192)
)
dl80UserTrap1192.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1192.setStatus(
        ""
    )

dl80UserTrap1193 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1193)
)
dl80UserTrap1193.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1193.setStatus(
        ""
    )

dl80UserTrap1194 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1194)
)
dl80UserTrap1194.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1194.setStatus(
        ""
    )

dl80UserTrap1195 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1195)
)
dl80UserTrap1195.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1195.setStatus(
        ""
    )

dl80UserTrap1196 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1196)
)
dl80UserTrap1196.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1196.setStatus(
        ""
    )

dl80UserTrap1197 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1197)
)
dl80UserTrap1197.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1197.setStatus(
        ""
    )

dl80UserTrap1198 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1198)
)
dl80UserTrap1198.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1198.setStatus(
        ""
    )

dl80UserTrap1199 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 7, 0, 1199)
)
dl80UserTrap1199.setObjects(
      *(("DL80-STD-MIB", "siteID"),
        ("DL80-STD-MIB", "esIndex"),
        ("DL80-STD-MIB", "esName"),
        ("DL80-STD-MIB", "trapEventTypeNumber"),
        ("DL80-STD-MIB", "trapEventTypeName"),
        ("DL80-STD-MIB", "esIndexPoint"),
        ("DL80-STD-MIB", "esPointName"),
        ("DL80-STD-MIB", "esID"),
        ("DL80-STD-MIB", "clock"),
        ("DL80-STD-MIB", "trapIncludedValue"),
        ("DL80-STD-MIB", "trapIncludedString"),
        ("DL80-STD-MIB", "trapEventClassNumber"),
        ("DL80-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl80UserTrap1199.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DL80-STD-MIB",
    **{"omnitronix": omnitronix,
       "dl80": dl80,
       "dl80StockContactClosureTrap": dl80StockContactClosureTrap,
       "dl80StockTempTrap": dl80StockTempTrap,
       "dl80StockHumidityTrap": dl80StockHumidityTrap,
       "dl80StockAnalogTrap": dl80StockAnalogTrap,
       "dl80UserTrap180": dl80UserTrap180,
       "dl80StockDbasePfullTrap": dl80StockDbasePfullTrap,
       "dl80StockDataAlarmTrap": dl80StockDataAlarmTrap,
       "dl80StockNoDataAlarmTrap": dl80StockNoDataAlarmTrap,
       "dl80StockSchedTrap": dl80StockSchedTrap,
       "dl80StockImmediateTrap": dl80StockImmediateTrap,
       "dl80StockSocketLostTrap": dl80StockSocketLostTrap,
       "dl80StockCTSTrap": dl80StockCTSTrap,
       "dl80UserTrap1000": dl80UserTrap1000,
       "dl80UserTrap1001": dl80UserTrap1001,
       "dl80UserTrap1002": dl80UserTrap1002,
       "dl80UserTrap1003": dl80UserTrap1003,
       "dl80UserTrap1004": dl80UserTrap1004,
       "dl80UserTrap1005": dl80UserTrap1005,
       "dl80UserTrap1006": dl80UserTrap1006,
       "dl80UserTrap1007": dl80UserTrap1007,
       "dl80UserTrap1008": dl80UserTrap1008,
       "dl80UserTrap1009": dl80UserTrap1009,
       "dl80UserTrap1010": dl80UserTrap1010,
       "dl80UserTrap1011": dl80UserTrap1011,
       "dl80UserTrap1012": dl80UserTrap1012,
       "dl80UserTrap1013": dl80UserTrap1013,
       "dl80UserTrap1014": dl80UserTrap1014,
       "dl80UserTrap1015": dl80UserTrap1015,
       "dl80UserTrap1016": dl80UserTrap1016,
       "dl80UserTrap1017": dl80UserTrap1017,
       "dl80UserTrap1018": dl80UserTrap1018,
       "dl80UserTrap1019": dl80UserTrap1019,
       "dl80UserTrap1020": dl80UserTrap1020,
       "dl80UserTrap1021": dl80UserTrap1021,
       "dl80UserTrap1022": dl80UserTrap1022,
       "dl80UserTrap1023": dl80UserTrap1023,
       "dl80UserTrap1024": dl80UserTrap1024,
       "dl80UserTrap1025": dl80UserTrap1025,
       "dl80UserTrap1026": dl80UserTrap1026,
       "dl80UserTrap1027": dl80UserTrap1027,
       "dl80UserTrap1028": dl80UserTrap1028,
       "dl80UserTrap1029": dl80UserTrap1029,
       "dl80UserTrap1030": dl80UserTrap1030,
       "dl80UserTrap1031": dl80UserTrap1031,
       "dl80UserTrap1032": dl80UserTrap1032,
       "dl80UserTrap1033": dl80UserTrap1033,
       "dl80UserTrap1034": dl80UserTrap1034,
       "dl80UserTrap1035": dl80UserTrap1035,
       "dl80UserTrap1036": dl80UserTrap1036,
       "dl80UserTrap1037": dl80UserTrap1037,
       "dl80UserTrap1038": dl80UserTrap1038,
       "dl80UserTrap1039": dl80UserTrap1039,
       "dl80UserTrap1040": dl80UserTrap1040,
       "dl80UserTrap1041": dl80UserTrap1041,
       "dl80UserTrap1042": dl80UserTrap1042,
       "dl80UserTrap1043": dl80UserTrap1043,
       "dl80UserTrap1044": dl80UserTrap1044,
       "dl80UserTrap1045": dl80UserTrap1045,
       "dl80UserTrap1046": dl80UserTrap1046,
       "dl80UserTrap1047": dl80UserTrap1047,
       "dl80UserTrap1048": dl80UserTrap1048,
       "dl80UserTrap1049": dl80UserTrap1049,
       "dl80UserTrap1050": dl80UserTrap1050,
       "dl80UserTrap1051": dl80UserTrap1051,
       "dl80UserTrap1052": dl80UserTrap1052,
       "dl80UserTrap1053": dl80UserTrap1053,
       "dl80UserTrap1054": dl80UserTrap1054,
       "dl80UserTrap1055": dl80UserTrap1055,
       "dl80UserTrap1056": dl80UserTrap1056,
       "dl80UserTrap1057": dl80UserTrap1057,
       "dl80UserTrap1058": dl80UserTrap1058,
       "dl80UserTrap1059": dl80UserTrap1059,
       "dl80UserTrap1060": dl80UserTrap1060,
       "dl80UserTrap1061": dl80UserTrap1061,
       "dl80UserTrap1062": dl80UserTrap1062,
       "dl80UserTrap1063": dl80UserTrap1063,
       "dl80UserTrap1064": dl80UserTrap1064,
       "dl80UserTrap1065": dl80UserTrap1065,
       "dl80UserTrap1066": dl80UserTrap1066,
       "dl80UserTrap1067": dl80UserTrap1067,
       "dl80UserTrap1068": dl80UserTrap1068,
       "dl80UserTrap1069": dl80UserTrap1069,
       "dl80UserTrap1070": dl80UserTrap1070,
       "dl80UserTrap1071": dl80UserTrap1071,
       "dl80UserTrap1072": dl80UserTrap1072,
       "dl80UserTrap1073": dl80UserTrap1073,
       "dl80UserTrap1074": dl80UserTrap1074,
       "dl80UserTrap1075": dl80UserTrap1075,
       "dl80UserTrap1076": dl80UserTrap1076,
       "dl80UserTrap1077": dl80UserTrap1077,
       "dl80UserTrap1078": dl80UserTrap1078,
       "dl80UserTrap1079": dl80UserTrap1079,
       "dl80UserTrap1080": dl80UserTrap1080,
       "dl80UserTrap1081": dl80UserTrap1081,
       "dl80UserTrap1082": dl80UserTrap1082,
       "dl80UserTrap1083": dl80UserTrap1083,
       "dl80UserTrap1084": dl80UserTrap1084,
       "dl80UserTrap1085": dl80UserTrap1085,
       "dl80UserTrap1086": dl80UserTrap1086,
       "dl80UserTrap1087": dl80UserTrap1087,
       "dl80UserTrap1088": dl80UserTrap1088,
       "dl80UserTrap1089": dl80UserTrap1089,
       "dl80UserTrap1090": dl80UserTrap1090,
       "dl80UserTrap1091": dl80UserTrap1091,
       "dl80UserTrap1092": dl80UserTrap1092,
       "dl80UserTrap1093": dl80UserTrap1093,
       "dl80UserTrap1094": dl80UserTrap1094,
       "dl80UserTrap1095": dl80UserTrap1095,
       "dl80UserTrap1096": dl80UserTrap1096,
       "dl80UserTrap1097": dl80UserTrap1097,
       "dl80UserTrap1098": dl80UserTrap1098,
       "dl80UserTrap1099": dl80UserTrap1099,
       "dl80UserTrap1100": dl80UserTrap1100,
       "dl80UserTrap1101": dl80UserTrap1101,
       "dl80UserTrap1102": dl80UserTrap1102,
       "dl80UserTrap1103": dl80UserTrap1103,
       "dl80UserTrap1104": dl80UserTrap1104,
       "dl80UserTrap1105": dl80UserTrap1105,
       "dl80UserTrap1106": dl80UserTrap1106,
       "dl80UserTrap1107": dl80UserTrap1107,
       "dl80UserTrap1108": dl80UserTrap1108,
       "dl80UserTrap1109": dl80UserTrap1109,
       "dl80UserTrap1110": dl80UserTrap1110,
       "dl80UserTrap1111": dl80UserTrap1111,
       "dl80UserTrap1112": dl80UserTrap1112,
       "dl80UserTrap1113": dl80UserTrap1113,
       "dl80UserTrap1114": dl80UserTrap1114,
       "dl80UserTrap1115": dl80UserTrap1115,
       "dl80UserTrap1116": dl80UserTrap1116,
       "dl80UserTrap1117": dl80UserTrap1117,
       "dl80UserTrap1118": dl80UserTrap1118,
       "dl80UserTrap1119": dl80UserTrap1119,
       "dl80UserTrap1120": dl80UserTrap1120,
       "dl80UserTrap1121": dl80UserTrap1121,
       "dl80UserTrap1122": dl80UserTrap1122,
       "dl80UserTrap1123": dl80UserTrap1123,
       "dl80UserTrap1124": dl80UserTrap1124,
       "dl80UserTrap1125": dl80UserTrap1125,
       "dl80UserTrap1126": dl80UserTrap1126,
       "dl80UserTrap1127": dl80UserTrap1127,
       "dl80UserTrap1128": dl80UserTrap1128,
       "dl80UserTrap1129": dl80UserTrap1129,
       "dl80UserTrap1130": dl80UserTrap1130,
       "dl80UserTrap1131": dl80UserTrap1131,
       "dl80UserTrap1132": dl80UserTrap1132,
       "dl80UserTrap1133": dl80UserTrap1133,
       "dl80UserTrap1134": dl80UserTrap1134,
       "dl80UserTrap1135": dl80UserTrap1135,
       "dl80UserTrap1136": dl80UserTrap1136,
       "dl80UserTrap1137": dl80UserTrap1137,
       "dl80UserTrap1138": dl80UserTrap1138,
       "dl80UserTrap1139": dl80UserTrap1139,
       "dl80UserTrap1140": dl80UserTrap1140,
       "dl80UserTrap1141": dl80UserTrap1141,
       "dl80UserTrap1142": dl80UserTrap1142,
       "dl80UserTrap1143": dl80UserTrap1143,
       "dl80UserTrap1144": dl80UserTrap1144,
       "dl80UserTrap1145": dl80UserTrap1145,
       "dl80UserTrap1146": dl80UserTrap1146,
       "dl80UserTrap1147": dl80UserTrap1147,
       "dl80UserTrap1148": dl80UserTrap1148,
       "dl80UserTrap1149": dl80UserTrap1149,
       "dl80UserTrap1150": dl80UserTrap1150,
       "dl80UserTrap1151": dl80UserTrap1151,
       "dl80UserTrap1152": dl80UserTrap1152,
       "dl80UserTrap1153": dl80UserTrap1153,
       "dl80UserTrap1154": dl80UserTrap1154,
       "dl80UserTrap1155": dl80UserTrap1155,
       "dl80UserTrap1156": dl80UserTrap1156,
       "dl80UserTrap1157": dl80UserTrap1157,
       "dl80UserTrap1158": dl80UserTrap1158,
       "dl80UserTrap1159": dl80UserTrap1159,
       "dl80UserTrap1161": dl80UserTrap1161,
       "dl80UserTrap1162": dl80UserTrap1162,
       "dl80UserTrap1163": dl80UserTrap1163,
       "dl80UserTrap1164": dl80UserTrap1164,
       "dl80UserTrap1165": dl80UserTrap1165,
       "dl80UserTrap1166": dl80UserTrap1166,
       "dl80UserTrap1167": dl80UserTrap1167,
       "dl80UserTrap1168": dl80UserTrap1168,
       "dl80UserTrap1169": dl80UserTrap1169,
       "dl80UserTrap1170": dl80UserTrap1170,
       "dl80UserTrap1171": dl80UserTrap1171,
       "dl80UserTrap1172": dl80UserTrap1172,
       "dl80UserTrap1173": dl80UserTrap1173,
       "dl80UserTrap1174": dl80UserTrap1174,
       "dl80UserTrap1175": dl80UserTrap1175,
       "dl80UserTrap1176": dl80UserTrap1176,
       "dl80UserTrap1177": dl80UserTrap1177,
       "dl80UserTrap1178": dl80UserTrap1178,
       "dl80UserTrap1179": dl80UserTrap1179,
       "dl80UserTrap1180": dl80UserTrap1180,
       "dl80UserTrap1181": dl80UserTrap1181,
       "dl80UserTrap1182": dl80UserTrap1182,
       "dl80UserTrap1183": dl80UserTrap1183,
       "dl80UserTrap1184": dl80UserTrap1184,
       "dl80UserTrap1185": dl80UserTrap1185,
       "dl80UserTrap1186": dl80UserTrap1186,
       "dl80UserTrap1187": dl80UserTrap1187,
       "dl80UserTrap1188": dl80UserTrap1188,
       "dl80UserTrap1189": dl80UserTrap1189,
       "dl80UserTrap1190": dl80UserTrap1190,
       "dl80UserTrap1191": dl80UserTrap1191,
       "dl80UserTrap1192": dl80UserTrap1192,
       "dl80UserTrap1193": dl80UserTrap1193,
       "dl80UserTrap1194": dl80UserTrap1194,
       "dl80UserTrap1195": dl80UserTrap1195,
       "dl80UserTrap1196": dl80UserTrap1196,
       "dl80UserTrap1197": dl80UserTrap1197,
       "dl80UserTrap1198": dl80UserTrap1198,
       "dl80UserTrap1199": dl80UserTrap1199,
       "status": status,
       "eventSensorStatus": eventSensorStatus,
       "esPointTable": esPointTable,
       "esPointEntry": esPointEntry,
       "esIndexES": esIndexES,
       "esIndexPC": esIndexPC,
       "esIndexPoint": esIndexPoint,
       "esPointName": esPointName,
       "config": config,
       "eventSensorBasics": eventSensorBasics,
       "esNumberEventSensors": esNumberEventSensors,
       "esTable": esTable,
       "esEntry": esEntry,
       "esIndex": esIndex,
       "esName": esName,
       "esID": esID,
       "time": time,
       "clock": clock,
       "productIds": productIds,
       "siteID": siteID,
       "stockTrapString": stockTrapString,
       "trapEventTypeNumber": trapEventTypeNumber,
       "trapEventTypeName": trapEventTypeName,
       "trapIncludedValue": trapIncludedValue,
       "trapIncludedString": trapIncludedString,
       "trapTypeString": trapTypeString,
       "trapEventClassNumber": trapEventClassNumber,
       "trapEventClassName": trapEventClassName}
)
