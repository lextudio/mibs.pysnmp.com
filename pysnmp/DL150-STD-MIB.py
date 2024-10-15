# SNMP MIB module (DL150-STD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DL150-STD-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:29:31 2024
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
_Dl150_ObjectIdentity = ObjectIdentity
dl150 = _Dl150_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 6)
)
_Status_ObjectIdentity = ObjectIdentity
status = _Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 6, 1)
)
_EventSensorStatus_ObjectIdentity = ObjectIdentity
eventSensorStatus = _EventSensorStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 6, 1, 1)
)
_EsPointTable_Object = MibTable
esPointTable = _EsPointTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 1, 1, 1)
)
if mibBuilder.loadTexts:
    esPointTable.setStatus("mandatory")
_EsPointEntry_Object = MibTableRow
esPointEntry = _EsPointEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 1, 1, 1, 1)
)
esPointEntry.setIndexNames(
    (0, "DL150-STD-MIB", "esIndexES"),
    (0, "DL150-STD-MIB", "esIndexPC"),
    (0, "DL150-STD-MIB", "esIndexPoint"),
)
if mibBuilder.loadTexts:
    esPointEntry.setStatus("mandatory")
_EsIndexES_Type = Integer32
_EsIndexES_Object = MibTableColumn
esIndexES = _EsIndexES_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 1, 1, 1, 1, 1),
    _EsIndexES_Type()
)
esIndexES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexES.setStatus("mandatory")
_EsIndexPC_Type = Integer32
_EsIndexPC_Object = MibTableColumn
esIndexPC = _EsIndexPC_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 1, 1, 1, 1, 2),
    _EsIndexPC_Type()
)
esIndexPC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPC.setStatus("mandatory")
_EsIndexPoint_Type = Integer32
_EsIndexPoint_Object = MibTableColumn
esIndexPoint = _EsIndexPoint_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 1, 1, 1, 1, 3),
    _EsIndexPoint_Type()
)
esIndexPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndexPoint.setStatus("mandatory")
_EsPointName_Type = DisplayString
_EsPointName_Object = MibTableColumn
esPointName = _EsPointName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 1, 1, 1, 1, 4),
    _EsPointName_Type()
)
esPointName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    esPointName.setStatus("mandatory")
_Config_ObjectIdentity = ObjectIdentity
config = _Config_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 6, 2)
)
_EventSensorBasics_ObjectIdentity = ObjectIdentity
eventSensorBasics = _EventSensorBasics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 6, 2, 1)
)
_EsNumberEventSensors_Type = Integer32
_EsNumberEventSensors_Object = MibScalar
esNumberEventSensors = _EsNumberEventSensors_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 2, 1, 1),
    _EsNumberEventSensors_Type()
)
esNumberEventSensors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esNumberEventSensors.setStatus("mandatory")
_EsTable_Object = MibTable
esTable = _EsTable_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 2, 1, 2)
)
if mibBuilder.loadTexts:
    esTable.setStatus("mandatory")
_EsEntry_Object = MibTableRow
esEntry = _EsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 2, 1, 2, 1)
)
esEntry.setIndexNames(
    (0, "DL150-STD-MIB", "esIndex"),
)
if mibBuilder.loadTexts:
    esEntry.setStatus("mandatory")
_EsIndex_Type = Integer32
_EsIndex_Object = MibTableColumn
esIndex = _EsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 2, 1, 2, 1, 1),
    _EsIndex_Type()
)
esIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esIndex.setStatus("mandatory")
_EsName_Type = DisplayString
_EsName_Object = MibTableColumn
esName = _EsName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 2, 1, 2, 1, 2),
    _EsName_Type()
)
esName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esName.setStatus("mandatory")
_EsID_Type = DisplayString
_EsID_Object = MibTableColumn
esID = _EsID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 2, 1, 2, 1, 3),
    _EsID_Type()
)
esID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    esID.setStatus("mandatory")
_Time_ObjectIdentity = ObjectIdentity
time = _Time_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 6, 2, 8)
)
_Clock_Type = DisplayString
_Clock_Object = MibScalar
clock = _Clock_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 2, 8, 1),
    _Clock_Type()
)
clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clock.setStatus("mandatory")
_ProductIds_ObjectIdentity = ObjectIdentity
productIds = _ProductIds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3052, 6, 3)
)
_SiteID_Type = DisplayString
_SiteID_Object = MibScalar
siteID = _SiteID_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 3, 1),
    _SiteID_Type()
)
siteID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    siteID.setStatus("mandatory")
_StockTrapString_Type = DisplayString
_StockTrapString_Object = MibScalar
stockTrapString = _StockTrapString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 3, 3),
    _StockTrapString_Type()
)
stockTrapString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    stockTrapString.setStatus("mandatory")
_TrapEventTypeNumber_Type = Integer32
_TrapEventTypeNumber_Object = MibScalar
trapEventTypeNumber = _TrapEventTypeNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 3, 4),
    _TrapEventTypeNumber_Type()
)
trapEventTypeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapEventTypeNumber.setStatus("mandatory")
_TrapEventTypeName_Type = DisplayString
_TrapEventTypeName_Object = MibScalar
trapEventTypeName = _TrapEventTypeName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 3, 5),
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
    (1, 3, 6, 1, 4, 1, 3052, 6, 3, 6),
    _TrapIncludedValue_Type()
)
trapIncludedValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIncludedValue.setStatus("mandatory")
_TrapIncludedString_Type = DisplayString
_TrapIncludedString_Object = MibScalar
trapIncludedString = _TrapIncludedString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 3, 7),
    _TrapIncludedString_Type()
)
trapIncludedString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIncludedString.setStatus("mandatory")
_TrapTypeString_Type = DisplayString
_TrapTypeString_Object = MibScalar
trapTypeString = _TrapTypeString_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 3, 8),
    _TrapTypeString_Type()
)
trapTypeString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapTypeString.setStatus("mandatory")
_TrapEventClassNumber_Type = Integer32
_TrapEventClassNumber_Object = MibScalar
trapEventClassNumber = _TrapEventClassNumber_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 3, 9),
    _TrapEventClassNumber_Type()
)
trapEventClassNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapEventClassNumber.setStatus("mandatory")
_TrapEventClassName_Type = Integer32
_TrapEventClassName_Object = MibScalar
trapEventClassName = _TrapEventClassName_Object(
    (1, 3, 6, 1, 4, 1, 3052, 6, 3, 10),
    _TrapEventClassName_Type()
)
trapEventClassName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapEventClassName.setStatus("mandatory")

# Managed Objects groups


# Notification objects

dl150StockContactClosureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 110)
)
dl150StockContactClosureTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    dl150StockContactClosureTrap.setStatus(
        ""
    )

dl150StockTempTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 120)
)
dl150StockTempTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    dl150StockTempTrap.setStatus(
        ""
    )

dl150StockHumidityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 130)
)
dl150StockHumidityTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    dl150StockHumidityTrap.setStatus(
        ""
    )

dl150StockAnalogTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 140)
)
dl150StockAnalogTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"))
)
if mibBuilder.loadTexts:
    dl150StockAnalogTrap.setStatus(
        ""
    )

dl150StockDbasePfullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 501)
)
dl150StockDbasePfullTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"),
        ("DL150-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl150StockDbasePfullTrap.setStatus(
        ""
    )

dl150StockDataAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 503)
)
dl150StockDataAlarmTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"),
        ("DL150-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl150StockDataAlarmTrap.setStatus(
        ""
    )

dl150StockNoDataAlarmTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 505)
)
dl150StockNoDataAlarmTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"),
        ("DL150-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl150StockNoDataAlarmTrap.setStatus(
        ""
    )

dl150StockSchedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 506)
)
dl150StockSchedTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"),
        ("DL150-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl150StockSchedTrap.setStatus(
        ""
    )

dl150StockImmediateTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 507)
)
dl150StockImmediateTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"),
        ("DL150-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl150StockImmediateTrap.setStatus(
        ""
    )

dl150StockSocketLostTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 508)
)
dl150StockSocketLostTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"),
        ("DL150-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl150StockSocketLostTrap.setStatus(
        ""
    )

dl150StockCTSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 510)
)
dl150StockCTSTrap.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "stockTrapString"),
        ("DL150-STD-MIB", "trapTypeString"))
)
if mibBuilder.loadTexts:
    dl150StockCTSTrap.setStatus(
        ""
    )

dl150UserTrap1000 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1000)
)
dl150UserTrap1000.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1000.setStatus(
        ""
    )

dl150UserTrap1001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1001)
)
dl150UserTrap1001.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1001.setStatus(
        ""
    )

dl150UserTrap1002 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1002)
)
dl150UserTrap1002.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1002.setStatus(
        ""
    )

dl150UserTrap1003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1003)
)
dl150UserTrap1003.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1003.setStatus(
        ""
    )

dl150UserTrap1004 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1004)
)
dl150UserTrap1004.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1004.setStatus(
        ""
    )

dl150UserTrap1005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1005)
)
dl150UserTrap1005.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1005.setStatus(
        ""
    )

dl150UserTrap1006 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1006)
)
dl150UserTrap1006.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1006.setStatus(
        ""
    )

dl150UserTrap1007 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1007)
)
dl150UserTrap1007.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1007.setStatus(
        ""
    )

dl150UserTrap1008 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1008)
)
dl150UserTrap1008.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1008.setStatus(
        ""
    )

dl150UserTrap1009 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1009)
)
dl150UserTrap1009.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1009.setStatus(
        ""
    )

dl150UserTrap1010 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1010)
)
dl150UserTrap1010.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1010.setStatus(
        ""
    )

dl150UserTrap1011 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1011)
)
dl150UserTrap1011.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1011.setStatus(
        ""
    )

dl150UserTrap1012 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1012)
)
dl150UserTrap1012.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1012.setStatus(
        ""
    )

dl150UserTrap1013 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1013)
)
dl150UserTrap1013.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1013.setStatus(
        ""
    )

dl150UserTrap1014 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1014)
)
dl150UserTrap1014.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1014.setStatus(
        ""
    )

dl150UserTrap1015 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1015)
)
dl150UserTrap1015.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1015.setStatus(
        ""
    )

dl150UserTrap1016 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1016)
)
dl150UserTrap1016.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1016.setStatus(
        ""
    )

dl150UserTrap1017 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1017)
)
dl150UserTrap1017.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1017.setStatus(
        ""
    )

dl150UserTrap1018 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1018)
)
dl150UserTrap1018.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1018.setStatus(
        ""
    )

dl150UserTrap1019 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1019)
)
dl150UserTrap1019.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1019.setStatus(
        ""
    )

dl150UserTrap1020 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1020)
)
dl150UserTrap1020.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1020.setStatus(
        ""
    )

dl150UserTrap1021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1021)
)
dl150UserTrap1021.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1021.setStatus(
        ""
    )

dl150UserTrap1022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1022)
)
dl150UserTrap1022.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1022.setStatus(
        ""
    )

dl150UserTrap1023 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1023)
)
dl150UserTrap1023.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1023.setStatus(
        ""
    )

dl150UserTrap1024 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1024)
)
dl150UserTrap1024.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1024.setStatus(
        ""
    )

dl150UserTrap1025 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1025)
)
dl150UserTrap1025.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1025.setStatus(
        ""
    )

dl150UserTrap1026 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1026)
)
dl150UserTrap1026.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1026.setStatus(
        ""
    )

dl150UserTrap1027 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1027)
)
dl150UserTrap1027.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1027.setStatus(
        ""
    )

dl150UserTrap1028 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1028)
)
dl150UserTrap1028.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1028.setStatus(
        ""
    )

dl150UserTrap1029 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1029)
)
dl150UserTrap1029.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1029.setStatus(
        ""
    )

dl150UserTrap1030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1030)
)
dl150UserTrap1030.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1030.setStatus(
        ""
    )

dl150UserTrap1031 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1031)
)
dl150UserTrap1031.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1031.setStatus(
        ""
    )

dl150UserTrap1032 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1032)
)
dl150UserTrap1032.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1032.setStatus(
        ""
    )

dl150UserTrap1033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1033)
)
dl150UserTrap1033.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1033.setStatus(
        ""
    )

dl150UserTrap1034 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1034)
)
dl150UserTrap1034.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1034.setStatus(
        ""
    )

dl150UserTrap1035 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1035)
)
dl150UserTrap1035.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1035.setStatus(
        ""
    )

dl150UserTrap1036 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1036)
)
dl150UserTrap1036.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1036.setStatus(
        ""
    )

dl150UserTrap1037 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1037)
)
dl150UserTrap1037.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1037.setStatus(
        ""
    )

dl150UserTrap1038 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1038)
)
dl150UserTrap1038.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1038.setStatus(
        ""
    )

dl150UserTrap1039 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1039)
)
dl150UserTrap1039.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1039.setStatus(
        ""
    )

dl150UserTrap1040 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1040)
)
dl150UserTrap1040.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1040.setStatus(
        ""
    )

dl150UserTrap1041 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1041)
)
dl150UserTrap1041.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1041.setStatus(
        ""
    )

dl150UserTrap1042 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1042)
)
dl150UserTrap1042.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1042.setStatus(
        ""
    )

dl150UserTrap1043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1043)
)
dl150UserTrap1043.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1043.setStatus(
        ""
    )

dl150UserTrap1044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1044)
)
dl150UserTrap1044.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1044.setStatus(
        ""
    )

dl150UserTrap1045 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1045)
)
dl150UserTrap1045.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1045.setStatus(
        ""
    )

dl150UserTrap1046 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1046)
)
dl150UserTrap1046.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1046.setStatus(
        ""
    )

dl150UserTrap1047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1047)
)
dl150UserTrap1047.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1047.setStatus(
        ""
    )

dl150UserTrap1048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1048)
)
dl150UserTrap1048.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1048.setStatus(
        ""
    )

dl150UserTrap1049 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1049)
)
dl150UserTrap1049.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1049.setStatus(
        ""
    )

dl150UserTrap1050 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1050)
)
dl150UserTrap1050.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1050.setStatus(
        ""
    )

dl150UserTrap1051 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1051)
)
dl150UserTrap1051.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1051.setStatus(
        ""
    )

dl150UserTrap1052 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1052)
)
dl150UserTrap1052.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1052.setStatus(
        ""
    )

dl150UserTrap1053 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1053)
)
dl150UserTrap1053.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1053.setStatus(
        ""
    )

dl150UserTrap1054 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1054)
)
dl150UserTrap1054.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1054.setStatus(
        ""
    )

dl150UserTrap1055 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1055)
)
dl150UserTrap1055.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1055.setStatus(
        ""
    )

dl150UserTrap1056 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1056)
)
dl150UserTrap1056.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1056.setStatus(
        ""
    )

dl150UserTrap1057 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1057)
)
dl150UserTrap1057.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1057.setStatus(
        ""
    )

dl150UserTrap1058 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1058)
)
dl150UserTrap1058.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1058.setStatus(
        ""
    )

dl150UserTrap1059 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1059)
)
dl150UserTrap1059.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1059.setStatus(
        ""
    )

dl150UserTrap1060 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1060)
)
dl150UserTrap1060.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1060.setStatus(
        ""
    )

dl150UserTrap1061 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1061)
)
dl150UserTrap1061.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1061.setStatus(
        ""
    )

dl150UserTrap1062 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1062)
)
dl150UserTrap1062.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1062.setStatus(
        ""
    )

dl150UserTrap1063 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1063)
)
dl150UserTrap1063.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1063.setStatus(
        ""
    )

dl150UserTrap1064 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1064)
)
dl150UserTrap1064.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1064.setStatus(
        ""
    )

dl150UserTrap1065 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1065)
)
dl150UserTrap1065.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1065.setStatus(
        ""
    )

dl150UserTrap1066 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1066)
)
dl150UserTrap1066.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1066.setStatus(
        ""
    )

dl150UserTrap1067 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1067)
)
dl150UserTrap1067.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1067.setStatus(
        ""
    )

dl150UserTrap1068 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1068)
)
dl150UserTrap1068.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1068.setStatus(
        ""
    )

dl150UserTrap1069 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1069)
)
dl150UserTrap1069.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1069.setStatus(
        ""
    )

dl150UserTrap1070 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1070)
)
dl150UserTrap1070.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1070.setStatus(
        ""
    )

dl150UserTrap1071 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1071)
)
dl150UserTrap1071.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1071.setStatus(
        ""
    )

dl150UserTrap1072 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1072)
)
dl150UserTrap1072.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1072.setStatus(
        ""
    )

dl150UserTrap1073 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1073)
)
dl150UserTrap1073.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1073.setStatus(
        ""
    )

dl150UserTrap1074 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1074)
)
dl150UserTrap1074.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1074.setStatus(
        ""
    )

dl150UserTrap1075 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1075)
)
dl150UserTrap1075.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1075.setStatus(
        ""
    )

dl150UserTrap1076 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1076)
)
dl150UserTrap1076.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1076.setStatus(
        ""
    )

dl150UserTrap1077 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1077)
)
dl150UserTrap1077.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1077.setStatus(
        ""
    )

dl150UserTrap1078 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1078)
)
dl150UserTrap1078.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1078.setStatus(
        ""
    )

dl150UserTrap1079 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1079)
)
dl150UserTrap1079.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1079.setStatus(
        ""
    )

dl150UserTrap1080 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1080)
)
dl150UserTrap1080.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1080.setStatus(
        ""
    )

dl150UserTrap1081 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1081)
)
dl150UserTrap1081.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1081.setStatus(
        ""
    )

dl150UserTrap1082 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1082)
)
dl150UserTrap1082.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1082.setStatus(
        ""
    )

dl150UserTrap1083 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1083)
)
dl150UserTrap1083.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1083.setStatus(
        ""
    )

dl150UserTrap1084 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1084)
)
dl150UserTrap1084.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1084.setStatus(
        ""
    )

dl150UserTrap1085 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1085)
)
dl150UserTrap1085.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1085.setStatus(
        ""
    )

dl150UserTrap1086 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1086)
)
dl150UserTrap1086.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1086.setStatus(
        ""
    )

dl150UserTrap1087 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1087)
)
dl150UserTrap1087.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1087.setStatus(
        ""
    )

dl150UserTrap1088 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1088)
)
dl150UserTrap1088.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1088.setStatus(
        ""
    )

dl150UserTrap1089 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1089)
)
dl150UserTrap1089.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1089.setStatus(
        ""
    )

dl150UserTrap1090 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1090)
)
dl150UserTrap1090.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1090.setStatus(
        ""
    )

dl150UserTrap1091 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1091)
)
dl150UserTrap1091.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1091.setStatus(
        ""
    )

dl150UserTrap1092 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1092)
)
dl150UserTrap1092.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1092.setStatus(
        ""
    )

dl150UserTrap1093 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1093)
)
dl150UserTrap1093.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1093.setStatus(
        ""
    )

dl150UserTrap1094 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1094)
)
dl150UserTrap1094.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1094.setStatus(
        ""
    )

dl150UserTrap1095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1095)
)
dl150UserTrap1095.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1095.setStatus(
        ""
    )

dl150UserTrap1096 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1096)
)
dl150UserTrap1096.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1096.setStatus(
        ""
    )

dl150UserTrap1097 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1097)
)
dl150UserTrap1097.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1097.setStatus(
        ""
    )

dl150UserTrap1098 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1098)
)
dl150UserTrap1098.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1098.setStatus(
        ""
    )

dl150UserTrap1099 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1099)
)
dl150UserTrap1099.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1099.setStatus(
        ""
    )

dl150UserTrap1100 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1100)
)
dl150UserTrap1100.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1100.setStatus(
        ""
    )

dl150UserTrap1101 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1101)
)
dl150UserTrap1101.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1101.setStatus(
        ""
    )

dl150UserTrap1102 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1102)
)
dl150UserTrap1102.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1102.setStatus(
        ""
    )

dl150UserTrap1103 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1103)
)
dl150UserTrap1103.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1103.setStatus(
        ""
    )

dl150UserTrap1104 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1104)
)
dl150UserTrap1104.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1104.setStatus(
        ""
    )

dl150UserTrap1105 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1105)
)
dl150UserTrap1105.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1105.setStatus(
        ""
    )

dl150UserTrap1106 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1106)
)
dl150UserTrap1106.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1106.setStatus(
        ""
    )

dl150UserTrap1107 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1107)
)
dl150UserTrap1107.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1107.setStatus(
        ""
    )

dl150UserTrap1108 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1108)
)
dl150UserTrap1108.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1108.setStatus(
        ""
    )

dl150UserTrap1109 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1109)
)
dl150UserTrap1109.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1109.setStatus(
        ""
    )

dl150UserTrap1110 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1110)
)
dl150UserTrap1110.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1110.setStatus(
        ""
    )

dl150UserTrap1111 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1111)
)
dl150UserTrap1111.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1111.setStatus(
        ""
    )

dl150UserTrap1112 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1112)
)
dl150UserTrap1112.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1112.setStatus(
        ""
    )

dl150UserTrap1113 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1113)
)
dl150UserTrap1113.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1113.setStatus(
        ""
    )

dl150UserTrap1114 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1114)
)
dl150UserTrap1114.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1114.setStatus(
        ""
    )

dl150UserTrap1115 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1115)
)
dl150UserTrap1115.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1115.setStatus(
        ""
    )

dl150UserTrap1116 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1116)
)
dl150UserTrap1116.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1116.setStatus(
        ""
    )

dl150UserTrap1117 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1117)
)
dl150UserTrap1117.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1117.setStatus(
        ""
    )

dl150UserTrap1118 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1118)
)
dl150UserTrap1118.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1118.setStatus(
        ""
    )

dl150UserTrap1119 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1119)
)
dl150UserTrap1119.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1119.setStatus(
        ""
    )

dl150UserTrap1120 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1120)
)
dl150UserTrap1120.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1120.setStatus(
        ""
    )

dl150UserTrap1121 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1121)
)
dl150UserTrap1121.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1121.setStatus(
        ""
    )

dl150UserTrap1122 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1122)
)
dl150UserTrap1122.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1122.setStatus(
        ""
    )

dl150UserTrap1123 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1123)
)
dl150UserTrap1123.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1123.setStatus(
        ""
    )

dl150UserTrap1124 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1124)
)
dl150UserTrap1124.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1124.setStatus(
        ""
    )

dl150UserTrap1125 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1125)
)
dl150UserTrap1125.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1125.setStatus(
        ""
    )

dl150UserTrap1126 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1126)
)
dl150UserTrap1126.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1126.setStatus(
        ""
    )

dl150UserTrap1127 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1127)
)
dl150UserTrap1127.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1127.setStatus(
        ""
    )

dl150UserTrap1128 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1128)
)
dl150UserTrap1128.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1128.setStatus(
        ""
    )

dl150UserTrap1129 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1129)
)
dl150UserTrap1129.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1129.setStatus(
        ""
    )

dl150UserTrap1130 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1130)
)
dl150UserTrap1130.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1130.setStatus(
        ""
    )

dl150UserTrap1131 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1131)
)
dl150UserTrap1131.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1131.setStatus(
        ""
    )

dl150UserTrap1132 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1132)
)
dl150UserTrap1132.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1132.setStatus(
        ""
    )

dl150UserTrap1133 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1133)
)
dl150UserTrap1133.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1133.setStatus(
        ""
    )

dl150UserTrap1134 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1134)
)
dl150UserTrap1134.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1134.setStatus(
        ""
    )

dl150UserTrap1135 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1135)
)
dl150UserTrap1135.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1135.setStatus(
        ""
    )

dl150UserTrap1136 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1136)
)
dl150UserTrap1136.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1136.setStatus(
        ""
    )

dl150UserTrap1137 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1137)
)
dl150UserTrap1137.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1137.setStatus(
        ""
    )

dl150UserTrap1138 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1138)
)
dl150UserTrap1138.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1138.setStatus(
        ""
    )

dl150UserTrap1139 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1139)
)
dl150UserTrap1139.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1139.setStatus(
        ""
    )

dl150UserTrap1140 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1140)
)
dl150UserTrap1140.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1140.setStatus(
        ""
    )

dl150UserTrap1141 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1141)
)
dl150UserTrap1141.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1141.setStatus(
        ""
    )

dl150UserTrap1142 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1142)
)
dl150UserTrap1142.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1142.setStatus(
        ""
    )

dl150UserTrap1143 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1143)
)
dl150UserTrap1143.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1143.setStatus(
        ""
    )

dl150UserTrap1144 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1144)
)
dl150UserTrap1144.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1144.setStatus(
        ""
    )

dl150UserTrap1145 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1145)
)
dl150UserTrap1145.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1145.setStatus(
        ""
    )

dl150UserTrap1146 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1146)
)
dl150UserTrap1146.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1146.setStatus(
        ""
    )

dl150UserTrap1147 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1147)
)
dl150UserTrap1147.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1147.setStatus(
        ""
    )

dl150UserTrap1148 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1148)
)
dl150UserTrap1148.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1148.setStatus(
        ""
    )

dl150UserTrap1149 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1149)
)
dl150UserTrap1149.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1149.setStatus(
        ""
    )

dl150UserTrap1150 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1150)
)
dl150UserTrap1150.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1150.setStatus(
        ""
    )

dl150UserTrap1151 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1151)
)
dl150UserTrap1151.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1151.setStatus(
        ""
    )

dl150UserTrap1152 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1152)
)
dl150UserTrap1152.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1152.setStatus(
        ""
    )

dl150UserTrap1153 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1153)
)
dl150UserTrap1153.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1153.setStatus(
        ""
    )

dl150UserTrap1154 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1154)
)
dl150UserTrap1154.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1154.setStatus(
        ""
    )

dl150UserTrap1155 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1155)
)
dl150UserTrap1155.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1155.setStatus(
        ""
    )

dl150UserTrap1156 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1156)
)
dl150UserTrap1156.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1156.setStatus(
        ""
    )

dl150UserTrap1157 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1157)
)
dl150UserTrap1157.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1157.setStatus(
        ""
    )

dl150UserTrap1158 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1158)
)
dl150UserTrap1158.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1158.setStatus(
        ""
    )

dl150UserTrap1159 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1159)
)
dl150UserTrap1159.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1159.setStatus(
        ""
    )

dl150UserTrap1160 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1160)
)
dl150UserTrap1160.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1160.setStatus(
        ""
    )

dl150UserTrap1161 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1161)
)
dl150UserTrap1161.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1161.setStatus(
        ""
    )

dl150UserTrap1162 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1162)
)
dl150UserTrap1162.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1162.setStatus(
        ""
    )

dl150UserTrap1163 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1163)
)
dl150UserTrap1163.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1163.setStatus(
        ""
    )

dl150UserTrap1164 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1164)
)
dl150UserTrap1164.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1164.setStatus(
        ""
    )

dl150UserTrap1165 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1165)
)
dl150UserTrap1165.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1165.setStatus(
        ""
    )

dl150UserTrap1166 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1166)
)
dl150UserTrap1166.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1166.setStatus(
        ""
    )

dl150UserTrap1167 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1167)
)
dl150UserTrap1167.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1167.setStatus(
        ""
    )

dl150UserTrap1168 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1168)
)
dl150UserTrap1168.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1168.setStatus(
        ""
    )

dl150UserTrap1169 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1169)
)
dl150UserTrap1169.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1169.setStatus(
        ""
    )

dl150UserTrap1170 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1170)
)
dl150UserTrap1170.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1170.setStatus(
        ""
    )

dl150UserTrap1171 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1171)
)
dl150UserTrap1171.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1171.setStatus(
        ""
    )

dl150UserTrap1172 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1172)
)
dl150UserTrap1172.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1172.setStatus(
        ""
    )

dl150UserTrap1173 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1173)
)
dl150UserTrap1173.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1173.setStatus(
        ""
    )

dl150UserTrap1174 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1174)
)
dl150UserTrap1174.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1174.setStatus(
        ""
    )

dl150UserTrap1175 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1175)
)
dl150UserTrap1175.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1175.setStatus(
        ""
    )

dl150UserTrap1176 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1176)
)
dl150UserTrap1176.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1176.setStatus(
        ""
    )

dl150UserTrap1177 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1177)
)
dl150UserTrap1177.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1177.setStatus(
        ""
    )

dl150UserTrap1178 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1178)
)
dl150UserTrap1178.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1178.setStatus(
        ""
    )

dl150UserTrap1179 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1179)
)
dl150UserTrap1179.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1179.setStatus(
        ""
    )

dl150UserTrap1180 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1180)
)
dl150UserTrap1180.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1180.setStatus(
        ""
    )

dl150UserTrap1181 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1181)
)
dl150UserTrap1181.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1181.setStatus(
        ""
    )

dl150UserTrap1182 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1182)
)
dl150UserTrap1182.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1182.setStatus(
        ""
    )

dl150UserTrap1183 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1183)
)
dl150UserTrap1183.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1183.setStatus(
        ""
    )

dl150UserTrap1184 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1184)
)
dl150UserTrap1184.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1184.setStatus(
        ""
    )

dl150UserTrap1185 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1185)
)
dl150UserTrap1185.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1185.setStatus(
        ""
    )

dl150UserTrap1186 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1186)
)
dl150UserTrap1186.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1186.setStatus(
        ""
    )

dl150UserTrap1187 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1187)
)
dl150UserTrap1187.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1187.setStatus(
        ""
    )

dl150UserTrap1188 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1188)
)
dl150UserTrap1188.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1188.setStatus(
        ""
    )

dl150UserTrap1189 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1189)
)
dl150UserTrap1189.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1189.setStatus(
        ""
    )

dl150UserTrap1190 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1190)
)
dl150UserTrap1190.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1190.setStatus(
        ""
    )

dl150UserTrap1191 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1191)
)
dl150UserTrap1191.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1191.setStatus(
        ""
    )

dl150UserTrap1192 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1192)
)
dl150UserTrap1192.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1192.setStatus(
        ""
    )

dl150UserTrap1193 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1193)
)
dl150UserTrap1193.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1193.setStatus(
        ""
    )

dl150UserTrap1194 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1194)
)
dl150UserTrap1194.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1194.setStatus(
        ""
    )

dl150UserTrap1195 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1195)
)
dl150UserTrap1195.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1195.setStatus(
        ""
    )

dl150UserTrap1196 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1196)
)
dl150UserTrap1196.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1196.setStatus(
        ""
    )

dl150UserTrap1197 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1197)
)
dl150UserTrap1197.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1197.setStatus(
        ""
    )

dl150UserTrap1198 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1198)
)
dl150UserTrap1198.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1198.setStatus(
        ""
    )

dl150UserTrap1199 = NotificationType(
    (1, 3, 6, 1, 4, 1, 3052, 6, 0, 1199)
)
dl150UserTrap1199.setObjects(
      *(("DL150-STD-MIB", "siteID"),
        ("DL150-STD-MIB", "esIndex"),
        ("DL150-STD-MIB", "esName"),
        ("DL150-STD-MIB", "trapEventTypeNumber"),
        ("DL150-STD-MIB", "trapEventTypeName"),
        ("DL150-STD-MIB", "esIndexPoint"),
        ("DL150-STD-MIB", "esPointName"),
        ("DL150-STD-MIB", "esID"),
        ("DL150-STD-MIB", "clock"),
        ("DL150-STD-MIB", "trapIncludedValue"),
        ("DL150-STD-MIB", "trapIncludedString"),
        ("DL150-STD-MIB", "trapEventClassNumber"),
        ("DL150-STD-MIB", "trapEventClassName"))
)
if mibBuilder.loadTexts:
    dl150UserTrap1199.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DL150-STD-MIB",
    **{"omnitronix": omnitronix,
       "dl150": dl150,
       "dl150StockContactClosureTrap": dl150StockContactClosureTrap,
       "dl150StockTempTrap": dl150StockTempTrap,
       "dl150StockHumidityTrap": dl150StockHumidityTrap,
       "dl150StockAnalogTrap": dl150StockAnalogTrap,
       "dl150StockDbasePfullTrap": dl150StockDbasePfullTrap,
       "dl150StockDataAlarmTrap": dl150StockDataAlarmTrap,
       "dl150StockNoDataAlarmTrap": dl150StockNoDataAlarmTrap,
       "dl150StockSchedTrap": dl150StockSchedTrap,
       "dl150StockImmediateTrap": dl150StockImmediateTrap,
       "dl150StockSocketLostTrap": dl150StockSocketLostTrap,
       "dl150StockCTSTrap": dl150StockCTSTrap,
       "dl150UserTrap1000": dl150UserTrap1000,
       "dl150UserTrap1001": dl150UserTrap1001,
       "dl150UserTrap1002": dl150UserTrap1002,
       "dl150UserTrap1003": dl150UserTrap1003,
       "dl150UserTrap1004": dl150UserTrap1004,
       "dl150UserTrap1005": dl150UserTrap1005,
       "dl150UserTrap1006": dl150UserTrap1006,
       "dl150UserTrap1007": dl150UserTrap1007,
       "dl150UserTrap1008": dl150UserTrap1008,
       "dl150UserTrap1009": dl150UserTrap1009,
       "dl150UserTrap1010": dl150UserTrap1010,
       "dl150UserTrap1011": dl150UserTrap1011,
       "dl150UserTrap1012": dl150UserTrap1012,
       "dl150UserTrap1013": dl150UserTrap1013,
       "dl150UserTrap1014": dl150UserTrap1014,
       "dl150UserTrap1015": dl150UserTrap1015,
       "dl150UserTrap1016": dl150UserTrap1016,
       "dl150UserTrap1017": dl150UserTrap1017,
       "dl150UserTrap1018": dl150UserTrap1018,
       "dl150UserTrap1019": dl150UserTrap1019,
       "dl150UserTrap1020": dl150UserTrap1020,
       "dl150UserTrap1021": dl150UserTrap1021,
       "dl150UserTrap1022": dl150UserTrap1022,
       "dl150UserTrap1023": dl150UserTrap1023,
       "dl150UserTrap1024": dl150UserTrap1024,
       "dl150UserTrap1025": dl150UserTrap1025,
       "dl150UserTrap1026": dl150UserTrap1026,
       "dl150UserTrap1027": dl150UserTrap1027,
       "dl150UserTrap1028": dl150UserTrap1028,
       "dl150UserTrap1029": dl150UserTrap1029,
       "dl150UserTrap1030": dl150UserTrap1030,
       "dl150UserTrap1031": dl150UserTrap1031,
       "dl150UserTrap1032": dl150UserTrap1032,
       "dl150UserTrap1033": dl150UserTrap1033,
       "dl150UserTrap1034": dl150UserTrap1034,
       "dl150UserTrap1035": dl150UserTrap1035,
       "dl150UserTrap1036": dl150UserTrap1036,
       "dl150UserTrap1037": dl150UserTrap1037,
       "dl150UserTrap1038": dl150UserTrap1038,
       "dl150UserTrap1039": dl150UserTrap1039,
       "dl150UserTrap1040": dl150UserTrap1040,
       "dl150UserTrap1041": dl150UserTrap1041,
       "dl150UserTrap1042": dl150UserTrap1042,
       "dl150UserTrap1043": dl150UserTrap1043,
       "dl150UserTrap1044": dl150UserTrap1044,
       "dl150UserTrap1045": dl150UserTrap1045,
       "dl150UserTrap1046": dl150UserTrap1046,
       "dl150UserTrap1047": dl150UserTrap1047,
       "dl150UserTrap1048": dl150UserTrap1048,
       "dl150UserTrap1049": dl150UserTrap1049,
       "dl150UserTrap1050": dl150UserTrap1050,
       "dl150UserTrap1051": dl150UserTrap1051,
       "dl150UserTrap1052": dl150UserTrap1052,
       "dl150UserTrap1053": dl150UserTrap1053,
       "dl150UserTrap1054": dl150UserTrap1054,
       "dl150UserTrap1055": dl150UserTrap1055,
       "dl150UserTrap1056": dl150UserTrap1056,
       "dl150UserTrap1057": dl150UserTrap1057,
       "dl150UserTrap1058": dl150UserTrap1058,
       "dl150UserTrap1059": dl150UserTrap1059,
       "dl150UserTrap1060": dl150UserTrap1060,
       "dl150UserTrap1061": dl150UserTrap1061,
       "dl150UserTrap1062": dl150UserTrap1062,
       "dl150UserTrap1063": dl150UserTrap1063,
       "dl150UserTrap1064": dl150UserTrap1064,
       "dl150UserTrap1065": dl150UserTrap1065,
       "dl150UserTrap1066": dl150UserTrap1066,
       "dl150UserTrap1067": dl150UserTrap1067,
       "dl150UserTrap1068": dl150UserTrap1068,
       "dl150UserTrap1069": dl150UserTrap1069,
       "dl150UserTrap1070": dl150UserTrap1070,
       "dl150UserTrap1071": dl150UserTrap1071,
       "dl150UserTrap1072": dl150UserTrap1072,
       "dl150UserTrap1073": dl150UserTrap1073,
       "dl150UserTrap1074": dl150UserTrap1074,
       "dl150UserTrap1075": dl150UserTrap1075,
       "dl150UserTrap1076": dl150UserTrap1076,
       "dl150UserTrap1077": dl150UserTrap1077,
       "dl150UserTrap1078": dl150UserTrap1078,
       "dl150UserTrap1079": dl150UserTrap1079,
       "dl150UserTrap1080": dl150UserTrap1080,
       "dl150UserTrap1081": dl150UserTrap1081,
       "dl150UserTrap1082": dl150UserTrap1082,
       "dl150UserTrap1083": dl150UserTrap1083,
       "dl150UserTrap1084": dl150UserTrap1084,
       "dl150UserTrap1085": dl150UserTrap1085,
       "dl150UserTrap1086": dl150UserTrap1086,
       "dl150UserTrap1087": dl150UserTrap1087,
       "dl150UserTrap1088": dl150UserTrap1088,
       "dl150UserTrap1089": dl150UserTrap1089,
       "dl150UserTrap1090": dl150UserTrap1090,
       "dl150UserTrap1091": dl150UserTrap1091,
       "dl150UserTrap1092": dl150UserTrap1092,
       "dl150UserTrap1093": dl150UserTrap1093,
       "dl150UserTrap1094": dl150UserTrap1094,
       "dl150UserTrap1095": dl150UserTrap1095,
       "dl150UserTrap1096": dl150UserTrap1096,
       "dl150UserTrap1097": dl150UserTrap1097,
       "dl150UserTrap1098": dl150UserTrap1098,
       "dl150UserTrap1099": dl150UserTrap1099,
       "dl150UserTrap1100": dl150UserTrap1100,
       "dl150UserTrap1101": dl150UserTrap1101,
       "dl150UserTrap1102": dl150UserTrap1102,
       "dl150UserTrap1103": dl150UserTrap1103,
       "dl150UserTrap1104": dl150UserTrap1104,
       "dl150UserTrap1105": dl150UserTrap1105,
       "dl150UserTrap1106": dl150UserTrap1106,
       "dl150UserTrap1107": dl150UserTrap1107,
       "dl150UserTrap1108": dl150UserTrap1108,
       "dl150UserTrap1109": dl150UserTrap1109,
       "dl150UserTrap1110": dl150UserTrap1110,
       "dl150UserTrap1111": dl150UserTrap1111,
       "dl150UserTrap1112": dl150UserTrap1112,
       "dl150UserTrap1113": dl150UserTrap1113,
       "dl150UserTrap1114": dl150UserTrap1114,
       "dl150UserTrap1115": dl150UserTrap1115,
       "dl150UserTrap1116": dl150UserTrap1116,
       "dl150UserTrap1117": dl150UserTrap1117,
       "dl150UserTrap1118": dl150UserTrap1118,
       "dl150UserTrap1119": dl150UserTrap1119,
       "dl150UserTrap1120": dl150UserTrap1120,
       "dl150UserTrap1121": dl150UserTrap1121,
       "dl150UserTrap1122": dl150UserTrap1122,
       "dl150UserTrap1123": dl150UserTrap1123,
       "dl150UserTrap1124": dl150UserTrap1124,
       "dl150UserTrap1125": dl150UserTrap1125,
       "dl150UserTrap1126": dl150UserTrap1126,
       "dl150UserTrap1127": dl150UserTrap1127,
       "dl150UserTrap1128": dl150UserTrap1128,
       "dl150UserTrap1129": dl150UserTrap1129,
       "dl150UserTrap1130": dl150UserTrap1130,
       "dl150UserTrap1131": dl150UserTrap1131,
       "dl150UserTrap1132": dl150UserTrap1132,
       "dl150UserTrap1133": dl150UserTrap1133,
       "dl150UserTrap1134": dl150UserTrap1134,
       "dl150UserTrap1135": dl150UserTrap1135,
       "dl150UserTrap1136": dl150UserTrap1136,
       "dl150UserTrap1137": dl150UserTrap1137,
       "dl150UserTrap1138": dl150UserTrap1138,
       "dl150UserTrap1139": dl150UserTrap1139,
       "dl150UserTrap1140": dl150UserTrap1140,
       "dl150UserTrap1141": dl150UserTrap1141,
       "dl150UserTrap1142": dl150UserTrap1142,
       "dl150UserTrap1143": dl150UserTrap1143,
       "dl150UserTrap1144": dl150UserTrap1144,
       "dl150UserTrap1145": dl150UserTrap1145,
       "dl150UserTrap1146": dl150UserTrap1146,
       "dl150UserTrap1147": dl150UserTrap1147,
       "dl150UserTrap1148": dl150UserTrap1148,
       "dl150UserTrap1149": dl150UserTrap1149,
       "dl150UserTrap1150": dl150UserTrap1150,
       "dl150UserTrap1151": dl150UserTrap1151,
       "dl150UserTrap1152": dl150UserTrap1152,
       "dl150UserTrap1153": dl150UserTrap1153,
       "dl150UserTrap1154": dl150UserTrap1154,
       "dl150UserTrap1155": dl150UserTrap1155,
       "dl150UserTrap1156": dl150UserTrap1156,
       "dl150UserTrap1157": dl150UserTrap1157,
       "dl150UserTrap1158": dl150UserTrap1158,
       "dl150UserTrap1159": dl150UserTrap1159,
       "dl150UserTrap1160": dl150UserTrap1160,
       "dl150UserTrap1161": dl150UserTrap1161,
       "dl150UserTrap1162": dl150UserTrap1162,
       "dl150UserTrap1163": dl150UserTrap1163,
       "dl150UserTrap1164": dl150UserTrap1164,
       "dl150UserTrap1165": dl150UserTrap1165,
       "dl150UserTrap1166": dl150UserTrap1166,
       "dl150UserTrap1167": dl150UserTrap1167,
       "dl150UserTrap1168": dl150UserTrap1168,
       "dl150UserTrap1169": dl150UserTrap1169,
       "dl150UserTrap1170": dl150UserTrap1170,
       "dl150UserTrap1171": dl150UserTrap1171,
       "dl150UserTrap1172": dl150UserTrap1172,
       "dl150UserTrap1173": dl150UserTrap1173,
       "dl150UserTrap1174": dl150UserTrap1174,
       "dl150UserTrap1175": dl150UserTrap1175,
       "dl150UserTrap1176": dl150UserTrap1176,
       "dl150UserTrap1177": dl150UserTrap1177,
       "dl150UserTrap1178": dl150UserTrap1178,
       "dl150UserTrap1179": dl150UserTrap1179,
       "dl150UserTrap1180": dl150UserTrap1180,
       "dl150UserTrap1181": dl150UserTrap1181,
       "dl150UserTrap1182": dl150UserTrap1182,
       "dl150UserTrap1183": dl150UserTrap1183,
       "dl150UserTrap1184": dl150UserTrap1184,
       "dl150UserTrap1185": dl150UserTrap1185,
       "dl150UserTrap1186": dl150UserTrap1186,
       "dl150UserTrap1187": dl150UserTrap1187,
       "dl150UserTrap1188": dl150UserTrap1188,
       "dl150UserTrap1189": dl150UserTrap1189,
       "dl150UserTrap1190": dl150UserTrap1190,
       "dl150UserTrap1191": dl150UserTrap1191,
       "dl150UserTrap1192": dl150UserTrap1192,
       "dl150UserTrap1193": dl150UserTrap1193,
       "dl150UserTrap1194": dl150UserTrap1194,
       "dl150UserTrap1195": dl150UserTrap1195,
       "dl150UserTrap1196": dl150UserTrap1196,
       "dl150UserTrap1197": dl150UserTrap1197,
       "dl150UserTrap1198": dl150UserTrap1198,
       "dl150UserTrap1199": dl150UserTrap1199,
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
