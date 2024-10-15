# SNMP MIB module (TP5000E) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TP5000E
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:43 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,
 ifNumber) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifNumber")

(InetAddressIPv6,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
 iso,
 snmpModules) = mibBuilder.importSymbols(
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
    "iso",
    "snmpModules")

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(ACTIONONLY,
 EnableValue,
 ONVALUETYPE,
 TP5000MODULEID,
 YESVALUETYPE,
 symmDeviceDependent) = mibBuilder.importSymbols(
    "SYMM-COMMON-SMI",
    "ACTIONONLY",
    "EnableValue",
    "ONVALUETYPE",
    "TP5000MODULEID",
    "YESVALUETYPE",
    "symmDeviceDependent")


# MODULE-IDENTITY

tp5000e = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1)
)
tp5000e.setRevisions(
        ("2018-03-22 04:37",)
)


# Types definitions



class TP5000LEDID(Integer32):
    """Custom type TP5000LEDID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20)
        )
    )
    namedValues = NamedValues(
        *(("act", 7),
          ("alarm", 8),
          ("alm", 4),
          ("bta", 1),
          ("btb", 2),
          ("eth1", 9),
          ("eth2", 10),
          ("gpsOrGnss", 5),
          ("holdover", 11),
          ("mgmt", 6),
          ("pwra", 13),
          ("pwrb", 14),
          ("ref", 12),
          ("shelfAlarm", 18),
          ("shelfBatA", 16),
          ("shelfBatB", 17),
          ("shelfMgmt", 19),
          ("shelfPower", 15),
          ("shelfRef", 20),
          ("sys", 3))
    )





class TP5000LEDTYPE(Integer32):
    """Custom type TP5000LEDTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("amber", 6),
          ("amberblink", 7),
          ("green", 4),
          ("greenblink", 5),
          ("off", 0),
          ("on", 1),
          ("red", 2),
          ("redblink", 3))
    )





class ALARMLEVELTYPE(Integer32):
    """Custom type ALARMLEVELTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("clear", 0),
          ("critical", 2),
          ("event", 5),
          ("major", 3),
          ("minor", 4))
    )





class TP5000IOCPORTID(Integer32):
    """Custom type TP5000IOCPORTID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5)
        )
    )
    namedValues = NamedValues(
        *(("eth1", 1),
          ("eth2", 2),
          ("none", 5))
    )





class TP5000IMAGEACTIVE(Integer32):
    """Custom type TP5000IMAGEACTIVE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )





class TP5000INTRAIPSET(Integer32):
    """Custom type TP5000INTRAIPSET based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setA", 0),
          ("setB", 1),
          ("setC", 2))
    )





class TP5000PACKETSERVICE(Integer32):
    """Custom type TP5000PACKETSERVICE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ntpProbe", 4),
          ("ntpServer", 3),
          ("ptpGM", 1),
          ("ptpProbe", 2))
    )





class TP5000SSMOPTION(Integer32):
    """Custom type TP5000SSMOPTION based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("option1", 1),
          ("option2", 2))
    )





class TP5000REFQUALIFICATION(Integer32):
    """Custom type TP5000REFQUALIFICATION based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("disqualified", 2),
          ("qualified", 1),
          ("selected", 3))
    )





class TP5000REFTIMINGMODE(Integer32):
    """Custom type TP5000REFTIMINGMODE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("frequency", 2),
          ("time", 1))
    )





class TP5000REFSELECTMODE(Integer32):
    """Custom type TP5000REFSELECTMODE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("manual", 1),
          ("priority", 2),
          ("ssm", 3))
    )





class TP5000SERVOCTL(Integer32):
    """Custom type TP5000SERVOCTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 6),
          ("extHoldover", 9),
          ("fail", 7),
          ("fasttrack", 3),
          ("freerun", 2),
          ("holdover", 5),
          ("localFreerun", 10),
          ("localHoldover", 11),
          ("normaltrack", 4),
          ("offline", 8),
          ("warmup", 1))
    )





class TP5000TRANSIENT(Integer32):
    """Custom type TP5000TRANSIENT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("stateEvent", 0),
          ("transientEvent", 1))
    )





class TP5000IOPORTID(Integer32):
    """Custom type TP5000IOPORTID based on Integer32"""
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
        *(("none", 5),
          ("port1", 1),
          ("port2", 2),
          ("port3", 3),
          ("port4", 4))
    )





class TP5000IOTYPE(Integer32):
    """Custom type TP5000IOTYPE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )





class TP5000SSMVALUE(Integer32):
    """Custom type TP5000SSMVALUE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )




# TEXTUAL-CONVENTIONS



class DateAndTime(OctetString, TextualConvention):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d:1d.1d,1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
        ValueSizeConstraint(11, 11),
    )



class TLatAndLon(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d:1d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )



class TAntHeight(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a2d.1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class TLocalTimeOffset(OctetString, TextualConvention):
    status = "current"
    displayHint = "1a1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )



class TSsm(Integer32, TextualConvention):
    status = "current"
    displayHint = "x"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_Tp5000eSystemStatus_ObjectIdentity = ObjectIdentity
tp5000eSystemStatus = _Tp5000eSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1)
)
_Tp5000eLedTable_Object = MibTable
tp5000eLedTable = _Tp5000eLedTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tp5000eLedTable.setStatus("current")
_Tp5000eLedEntry_Object = MibTableRow
tp5000eLedEntry = _Tp5000eLedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 1, 1)
)
tp5000eLedEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TP5000E", "tp5000eLedID"),
)
if mibBuilder.loadTexts:
    tp5000eLedEntry.setStatus("current")
_Tp5000eLedID_Type = TP5000LEDID
_Tp5000eLedID_Object = MibTableColumn
tp5000eLedID = _Tp5000eLedID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 1, 1, 1),
    _Tp5000eLedID_Type()
)
tp5000eLedID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eLedID.setStatus("current")
_Tp5000eLedStatus_Type = TP5000LEDTYPE
_Tp5000eLedStatus_Object = MibTableColumn
tp5000eLedStatus = _Tp5000eLedStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 1, 1, 2),
    _Tp5000eLedStatus_Type()
)
tp5000eLedStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eLedStatus.setStatus("current")
_Tp5000eHWStatusTable_Object = MibTable
tp5000eHWStatusTable = _Tp5000eHWStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 2)
)
if mibBuilder.loadTexts:
    tp5000eHWStatusTable.setStatus("current")
_Tp5000eHWStatusEntry_Object = MibTableRow
tp5000eHWStatusEntry = _Tp5000eHWStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 2, 1)
)
tp5000eHWStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TP5000E", "tp5000eHWStatusIndex"),
)
if mibBuilder.loadTexts:
    tp5000eHWStatusEntry.setStatus("current")


class _Tp5000eHWStatusIndex_Type(Integer32):
    """Custom type tp5000eHWStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Tp5000eHWStatusIndex_Type.__name__ = "Integer32"
_Tp5000eHWStatusIndex_Object = MibTableColumn
tp5000eHWStatusIndex = _Tp5000eHWStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 2, 1, 1),
    _Tp5000eHWStatusIndex_Type()
)
tp5000eHWStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eHWStatusIndex.setStatus("current")
_Tp5000eHWStatusInfo_Type = DisplayString
_Tp5000eHWStatusInfo_Object = MibTableColumn
tp5000eHWStatusInfo = _Tp5000eHWStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 2, 1, 2),
    _Tp5000eHWStatusInfo_Type()
)
tp5000eHWStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eHWStatusInfo.setStatus("current")
_Tp5000eModUpTimeTable_Object = MibTable
tp5000eModUpTimeTable = _Tp5000eModUpTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 3)
)
if mibBuilder.loadTexts:
    tp5000eModUpTimeTable.setStatus("current")
_Tp5000eModUpTimeEntry_Object = MibTableRow
tp5000eModUpTimeEntry = _Tp5000eModUpTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 3, 1)
)
tp5000eModUpTimeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TP5000E", "tp5000eModUpTimeIndex"),
)
if mibBuilder.loadTexts:
    tp5000eModUpTimeEntry.setStatus("current")


class _Tp5000eModUpTimeIndex_Type(Integer32):
    """Custom type tp5000eModUpTimeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Tp5000eModUpTimeIndex_Type.__name__ = "Integer32"
_Tp5000eModUpTimeIndex_Object = MibTableColumn
tp5000eModUpTimeIndex = _Tp5000eModUpTimeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 3, 1, 1),
    _Tp5000eModUpTimeIndex_Type()
)
tp5000eModUpTimeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eModUpTimeIndex.setStatus("current")
_Tp5000eModuleUpTime_Type = DisplayString
_Tp5000eModuleUpTime_Object = MibTableColumn
tp5000eModuleUpTime = _Tp5000eModuleUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 3, 1, 2),
    _Tp5000eModuleUpTime_Type()
)
tp5000eModuleUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eModuleUpTime.setStatus("current")
_Tp5000eModWarmUpTable_Object = MibTable
tp5000eModWarmUpTable = _Tp5000eModWarmUpTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 4)
)
if mibBuilder.loadTexts:
    tp5000eModWarmUpTable.setStatus("current")
_Tp5000eModWarmUpEntry_Object = MibTableRow
tp5000eModWarmUpEntry = _Tp5000eModWarmUpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 4, 1)
)
tp5000eModWarmUpEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TP5000E", "tp5000eModWarmUpIndex"),
)
if mibBuilder.loadTexts:
    tp5000eModWarmUpEntry.setStatus("current")


class _Tp5000eModWarmUpIndex_Type(Integer32):
    """Custom type tp5000eModWarmUpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Tp5000eModWarmUpIndex_Type.__name__ = "Integer32"
_Tp5000eModWarmUpIndex_Object = MibTableColumn
tp5000eModWarmUpIndex = _Tp5000eModWarmUpIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 4, 1, 1),
    _Tp5000eModWarmUpIndex_Type()
)
tp5000eModWarmUpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eModWarmUpIndex.setStatus("current")
_Tp5000eModWarmUpStatus_Type = DisplayString
_Tp5000eModWarmUpStatus_Object = MibTableColumn
tp5000eModWarmUpStatus = _Tp5000eModWarmUpStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 4, 1, 2),
    _Tp5000eModWarmUpStatus_Type()
)
tp5000eModWarmUpStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eModWarmUpStatus.setStatus("current")
_Tp5000eModStatusTable_Object = MibTable
tp5000eModStatusTable = _Tp5000eModStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 5)
)
if mibBuilder.loadTexts:
    tp5000eModStatusTable.setStatus("current")
_Tp5000eModStatusEntry_Object = MibTableRow
tp5000eModStatusEntry = _Tp5000eModStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 5, 1)
)
tp5000eModStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TP5000E", "tp5000eModStatusIndex"),
)
if mibBuilder.loadTexts:
    tp5000eModStatusEntry.setStatus("current")


class _Tp5000eModStatusIndex_Type(Integer32):
    """Custom type tp5000eModStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Tp5000eModStatusIndex_Type.__name__ = "Integer32"
_Tp5000eModStatusIndex_Object = MibTableColumn
tp5000eModStatusIndex = _Tp5000eModStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 5, 1, 1),
    _Tp5000eModStatusIndex_Type()
)
tp5000eModStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eModStatusIndex.setStatus("current")
_Tp5000eModStatusInfo_Type = DisplayString
_Tp5000eModStatusInfo_Object = MibTableColumn
tp5000eModStatusInfo = _Tp5000eModStatusInfo_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 1, 5, 1, 2),
    _Tp5000eModStatusInfo_Type()
)
tp5000eModStatusInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eModStatusInfo.setStatus("current")
_Tp5000eAlarmAndEvent_ObjectIdentity = ObjectIdentity
tp5000eAlarmAndEvent = _Tp5000eAlarmAndEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2)
)
_Tp5000eActAlarmTable_Object = MibTable
tp5000eActAlarmTable = _Tp5000eActAlarmTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tp5000eActAlarmTable.setStatus("current")
_Tp5000eActAlarmEntry_Object = MibTableRow
tp5000eActAlarmEntry = _Tp5000eActAlarmEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 1, 1)
)
tp5000eActAlarmEntry.setIndexNames(
    (0, "TP5000E", "tp5000eActAlarmIndex"),
)
if mibBuilder.loadTexts:
    tp5000eActAlarmEntry.setStatus("current")


class _Tp5000eActAlarmIndex_Type(Integer32):
    """Custom type tp5000eActAlarmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_Tp5000eActAlarmIndex_Type.__name__ = "Integer32"
_Tp5000eActAlarmIndex_Object = MibTableColumn
tp5000eActAlarmIndex = _Tp5000eActAlarmIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 1, 1, 1),
    _Tp5000eActAlarmIndex_Type()
)
tp5000eActAlarmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActAlarmIndex.setStatus("current")
_Tp5000eActAlarmModID_Type = TP5000MODULEID
_Tp5000eActAlarmModID_Object = MibTableColumn
tp5000eActAlarmModID = _Tp5000eActAlarmModID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 1, 1, 2),
    _Tp5000eActAlarmModID_Type()
)
tp5000eActAlarmModID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActAlarmModID.setStatus("current")
_Tp5000eActAlarmID_Type = Unsigned32
_Tp5000eActAlarmID_Object = MibTableColumn
tp5000eActAlarmID = _Tp5000eActAlarmID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 1, 1, 3),
    _Tp5000eActAlarmID_Type()
)
tp5000eActAlarmID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActAlarmID.setStatus("current")
_Tp5000eActAlarmInternalIndex_Type = Unsigned32
_Tp5000eActAlarmInternalIndex_Object = MibTableColumn
tp5000eActAlarmInternalIndex = _Tp5000eActAlarmInternalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 1, 1, 4),
    _Tp5000eActAlarmInternalIndex_Type()
)
tp5000eActAlarmInternalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActAlarmInternalIndex.setStatus("current")
_Tp5000eActAlarmDateTime_Type = DisplayString
_Tp5000eActAlarmDateTime_Object = MibTableColumn
tp5000eActAlarmDateTime = _Tp5000eActAlarmDateTime_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 1, 1, 5),
    _Tp5000eActAlarmDateTime_Type()
)
tp5000eActAlarmDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActAlarmDateTime.setStatus("current")
_Tp5000eActAlarmSeverity_Type = ALARMLEVELTYPE
_Tp5000eActAlarmSeverity_Object = MibTableColumn
tp5000eActAlarmSeverity = _Tp5000eActAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 1, 1, 6),
    _Tp5000eActAlarmSeverity_Type()
)
tp5000eActAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActAlarmSeverity.setStatus("current")
_Tp5000eActAlarmDesc_Type = DisplayString
_Tp5000eActAlarmDesc_Object = MibTableColumn
tp5000eActAlarmDesc = _Tp5000eActAlarmDesc_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 1, 1, 7),
    _Tp5000eActAlarmDesc_Type()
)
tp5000eActAlarmDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActAlarmDesc.setStatus("current")
_Tp5000eActEventTable_Object = MibTable
tp5000eActEventTable = _Tp5000eActEventTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tp5000eActEventTable.setStatus("current")
_Tp5000eActEventEntry_Object = MibTableRow
tp5000eActEventEntry = _Tp5000eActEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 2, 1)
)
tp5000eActEventEntry.setIndexNames(
    (0, "TP5000E", "tp5000eActEventIndex"),
)
if mibBuilder.loadTexts:
    tp5000eActEventEntry.setStatus("current")


class _Tp5000eActEventIndex_Type(Integer32):
    """Custom type tp5000eActEventIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_Tp5000eActEventIndex_Type.__name__ = "Integer32"
_Tp5000eActEventIndex_Object = MibTableColumn
tp5000eActEventIndex = _Tp5000eActEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 2, 1, 1),
    _Tp5000eActEventIndex_Type()
)
tp5000eActEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActEventIndex.setStatus("current")
_Tp5000eActEventModID_Type = TP5000MODULEID
_Tp5000eActEventModID_Object = MibTableColumn
tp5000eActEventModID = _Tp5000eActEventModID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 2, 1, 2),
    _Tp5000eActEventModID_Type()
)
tp5000eActEventModID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActEventModID.setStatus("current")
_Tp5000eActEventID_Type = Unsigned32
_Tp5000eActEventID_Object = MibTableColumn
tp5000eActEventID = _Tp5000eActEventID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 2, 1, 3),
    _Tp5000eActEventID_Type()
)
tp5000eActEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActEventID.setStatus("current")
_Tp5000eActEventInternlIndex_Type = Unsigned32
_Tp5000eActEventInternlIndex_Object = MibTableColumn
tp5000eActEventInternlIndex = _Tp5000eActEventInternlIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 2, 1, 4),
    _Tp5000eActEventInternlIndex_Type()
)
tp5000eActEventInternlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActEventInternlIndex.setStatus("current")
_Tp5000eActEventDateTime_Type = DisplayString
_Tp5000eActEventDateTime_Object = MibTableColumn
tp5000eActEventDateTime = _Tp5000eActEventDateTime_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 2, 1, 5),
    _Tp5000eActEventDateTime_Type()
)
tp5000eActEventDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActEventDateTime.setStatus("current")
_Tp5000eActEventDesc_Type = DisplayString
_Tp5000eActEventDesc_Object = MibTableColumn
tp5000eActEventDesc = _Tp5000eActEventDesc_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 2, 1, 6),
    _Tp5000eActEventDesc_Type()
)
tp5000eActEventDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eActEventDesc.setStatus("current")
_Tp5000eAlarmConfigTable_Object = MibTable
tp5000eAlarmConfigTable = _Tp5000eAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tp5000eAlarmConfigTable.setStatus("current")
_Tp5000eAlarmConfigEntry_Object = MibTableRow
tp5000eAlarmConfigEntry = _Tp5000eAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 3, 1)
)
tp5000eAlarmConfigEntry.setIndexNames(
    (0, "TP5000E", "tp5000eAlarmConfigIndex"),
)
if mibBuilder.loadTexts:
    tp5000eAlarmConfigEntry.setStatus("current")


class _Tp5000eAlarmConfigIndex_Type(Integer32):
    """Custom type tp5000eAlarmConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_Tp5000eAlarmConfigIndex_Type.__name__ = "Integer32"
_Tp5000eAlarmConfigIndex_Object = MibTableColumn
tp5000eAlarmConfigIndex = _Tp5000eAlarmConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 3, 1, 1),
    _Tp5000eAlarmConfigIndex_Type()
)
tp5000eAlarmConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eAlarmConfigIndex.setStatus("current")
_Tp5000eAlarmConfigAID_Type = Unsigned32
_Tp5000eAlarmConfigAID_Object = MibTableColumn
tp5000eAlarmConfigAID = _Tp5000eAlarmConfigAID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 3, 1, 2),
    _Tp5000eAlarmConfigAID_Type()
)
tp5000eAlarmConfigAID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eAlarmConfigAID.setStatus("current")
_Tp5000eAlarmLevelSetting_Type = ALARMLEVELTYPE
_Tp5000eAlarmLevelSetting_Object = MibTableColumn
tp5000eAlarmLevelSetting = _Tp5000eAlarmLevelSetting_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 3, 1, 3),
    _Tp5000eAlarmLevelSetting_Type()
)
tp5000eAlarmLevelSetting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eAlarmLevelSetting.setStatus("current")


class _Tp5000eAlarmSettingDelay_Type(Integer32):
    """Custom type tp5000eAlarmSettingDelay based on Integer32"""
    defaultValue = 0


_Tp5000eAlarmSettingDelay_Object = MibTableColumn
tp5000eAlarmSettingDelay = _Tp5000eAlarmSettingDelay_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 3, 1, 4),
    _Tp5000eAlarmSettingDelay_Type()
)
tp5000eAlarmSettingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eAlarmSettingDelay.setStatus("current")
if mibBuilder.loadTexts:
    tp5000eAlarmSettingDelay.setUnits("second")


class _Tp5000eEnableAlarmState_Type(EnableValue):
    """Custom type tp5000eEnableAlarmState based on EnableValue"""
    defaultValue = 2


_Tp5000eEnableAlarmState_Object = MibTableColumn
tp5000eEnableAlarmState = _Tp5000eEnableAlarmState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 3, 1, 5),
    _Tp5000eEnableAlarmState_Type()
)
tp5000eEnableAlarmState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eEnableAlarmState.setStatus("current")
_Tp5000eAlarmConfigDesc_Type = DisplayString
_Tp5000eAlarmConfigDesc_Object = MibTableColumn
tp5000eAlarmConfigDesc = _Tp5000eAlarmConfigDesc_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 3, 1, 6),
    _Tp5000eAlarmConfigDesc_Type()
)
tp5000eAlarmConfigDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eAlarmConfigDesc.setStatus("current")
_Tp5000eNumofStandingAlarm_Type = Integer32
_Tp5000eNumofStandingAlarm_Object = MibScalar
tp5000eNumofStandingAlarm = _Tp5000eNumofStandingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 4),
    _Tp5000eNumofStandingAlarm_Type()
)
tp5000eNumofStandingAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNumofStandingAlarm.setStatus("current")
_Tp5000eMessageGenerate_Type = ONVALUETYPE
_Tp5000eMessageGenerate_Object = MibScalar
tp5000eMessageGenerate = _Tp5000eMessageGenerate_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 2, 5),
    _Tp5000eMessageGenerate_Type()
)
tp5000eMessageGenerate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eMessageGenerate.setStatus("current")
_Tp5000eGlobalConfig_ObjectIdentity = ObjectIdentity
tp5000eGlobalConfig = _Tp5000eGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3)
)
_Tp5000eLogFileConfigTable_Object = MibTable
tp5000eLogFileConfigTable = _Tp5000eLogFileConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tp5000eLogFileConfigTable.setStatus("current")
_Tp5000eLogFileConfigEntry_Object = MibTableRow
tp5000eLogFileConfigEntry = _Tp5000eLogFileConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 1, 1)
)
tp5000eLogFileConfigEntry.setIndexNames(
    (0, "TP5000E", "tp5000eLogFileConfigIndex"),
)
if mibBuilder.loadTexts:
    tp5000eLogFileConfigEntry.setStatus("current")


class _Tp5000eLogFileConfigIndex_Type(Integer32):
    """Custom type tp5000eLogFileConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_Tp5000eLogFileConfigIndex_Type.__name__ = "Integer32"
_Tp5000eLogFileConfigIndex_Object = MibTableColumn
tp5000eLogFileConfigIndex = _Tp5000eLogFileConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 1, 1, 1),
    _Tp5000eLogFileConfigIndex_Type()
)
tp5000eLogFileConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eLogFileConfigIndex.setStatus("current")
_Tp5000eLogFileTypeName_Type = DisplayString
_Tp5000eLogFileTypeName_Object = MibTableColumn
tp5000eLogFileTypeName = _Tp5000eLogFileTypeName_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 1, 1, 2),
    _Tp5000eLogFileTypeName_Type()
)
tp5000eLogFileTypeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eLogFileTypeName.setStatus("current")


class _Tp5000eLogFileBufferSize_Type(Unsigned32):
    """Custom type tp5000eLogFileBufferSize based on Unsigned32"""
    defaultValue = 100


_Tp5000eLogFileBufferSize_Object = MibTableColumn
tp5000eLogFileBufferSize = _Tp5000eLogFileBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 1, 1, 3),
    _Tp5000eLogFileBufferSize_Type()
)
tp5000eLogFileBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eLogFileBufferSize.setStatus("current")
if mibBuilder.loadTexts:
    tp5000eLogFileBufferSize.setUnits("Kbyte")
_Tp5000eRemoteSyslogTable_Object = MibTable
tp5000eRemoteSyslogTable = _Tp5000eRemoteSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 2)
)
if mibBuilder.loadTexts:
    tp5000eRemoteSyslogTable.setStatus("current")
_Tp5000eRemoteSyslogEntry_Object = MibTableRow
tp5000eRemoteSyslogEntry = _Tp5000eRemoteSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 2, 1)
)
tp5000eRemoteSyslogEntry.setIndexNames(
    (0, "TP5000E", "tp5000eRemoteSyslogIndex"),
)
if mibBuilder.loadTexts:
    tp5000eRemoteSyslogEntry.setStatus("current")


class _Tp5000eRemoteSyslogIndex_Type(Integer32):
    """Custom type tp5000eRemoteSyslogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Tp5000eRemoteSyslogIndex_Type.__name__ = "Integer32"
_Tp5000eRemoteSyslogIndex_Object = MibTableColumn
tp5000eRemoteSyslogIndex = _Tp5000eRemoteSyslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 2, 1, 1),
    _Tp5000eRemoteSyslogIndex_Type()
)
tp5000eRemoteSyslogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eRemoteSyslogIndex.setStatus("current")


class _Tp5000eRemoteSyslogState_Type(EnableValue):
    """Custom type tp5000eRemoteSyslogState based on EnableValue"""
    defaultValue = 2


_Tp5000eRemoteSyslogState_Object = MibTableColumn
tp5000eRemoteSyslogState = _Tp5000eRemoteSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 2, 1, 2),
    _Tp5000eRemoteSyslogState_Type()
)
tp5000eRemoteSyslogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRemoteSyslogState.setStatus("current")
_Tp5000eRemoteSyslogAddr_Type = IpAddress
_Tp5000eRemoteSyslogAddr_Object = MibTableColumn
tp5000eRemoteSyslogAddr = _Tp5000eRemoteSyslogAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 2, 1, 3),
    _Tp5000eRemoteSyslogAddr_Type()
)
tp5000eRemoteSyslogAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRemoteSyslogAddr.setStatus("current")
_Tp5000eRedundTable_Object = MibTable
tp5000eRedundTable = _Tp5000eRedundTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tp5000eRedundTable.setStatus("current")
_Tp5000eRedundEntry_Object = MibTableRow
tp5000eRedundEntry = _Tp5000eRedundEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 3, 1)
)
tp5000eRedundEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TP5000E", "tp5000eRedundModuleID"),
)
if mibBuilder.loadTexts:
    tp5000eRedundEntry.setStatus("current")
_Tp5000eRedundModuleID_Type = TP5000MODULEID
_Tp5000eRedundModuleID_Object = MibTableColumn
tp5000eRedundModuleID = _Tp5000eRedundModuleID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 3, 1, 1),
    _Tp5000eRedundModuleID_Type()
)
tp5000eRedundModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eRedundModuleID.setStatus("current")
_Tp5000eRedundModState_Type = EnableValue
_Tp5000eRedundModState_Object = MibTableColumn
tp5000eRedundModState = _Tp5000eRedundModState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 3, 1, 2),
    _Tp5000eRedundModState_Type()
)
tp5000eRedundModState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRedundModState.setStatus("current")
_Tp5000eRedundActivePort_Type = TP5000IOCPORTID
_Tp5000eRedundActivePort_Object = MibTableColumn
tp5000eRedundActivePort = _Tp5000eRedundActivePort_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 3, 1, 3),
    _Tp5000eRedundActivePort_Type()
)
tp5000eRedundActivePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRedundActivePort.setStatus("current")
_Tp5000eImageTable_Object = MibTable
tp5000eImageTable = _Tp5000eImageTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 4)
)
if mibBuilder.loadTexts:
    tp5000eImageTable.setStatus("current")
_Tp5000eImageEntry_Object = MibTableRow
tp5000eImageEntry = _Tp5000eImageEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 4, 1)
)
tp5000eImageEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TP5000E", "tp5000eImageIndex"),
)
if mibBuilder.loadTexts:
    tp5000eImageEntry.setStatus("current")


class _Tp5000eImageIndex_Type(Integer32):
    """Custom type tp5000eImageIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Tp5000eImageIndex_Type.__name__ = "Integer32"
_Tp5000eImageIndex_Object = MibTableColumn
tp5000eImageIndex = _Tp5000eImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 4, 1, 1),
    _Tp5000eImageIndex_Type()
)
tp5000eImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eImageIndex.setStatus("current")
_Tp5000eImageNextBoot_Type = YESVALUETYPE
_Tp5000eImageNextBoot_Object = MibTableColumn
tp5000eImageNextBoot = _Tp5000eImageNextBoot_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 4, 1, 2),
    _Tp5000eImageNextBoot_Type()
)
tp5000eImageNextBoot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eImageNextBoot.setStatus("current")


class _Tp5000eImageID_Type(Integer32):
    """Custom type tp5000eImageID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_Tp5000eImageID_Type.__name__ = "Integer32"
_Tp5000eImageID_Object = MibTableColumn
tp5000eImageID = _Tp5000eImageID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 4, 1, 3),
    _Tp5000eImageID_Type()
)
tp5000eImageID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eImageID.setStatus("current")
_Tp5000eImageCurrState_Type = TP5000IMAGEACTIVE
_Tp5000eImageCurrState_Object = MibTableColumn
tp5000eImageCurrState = _Tp5000eImageCurrState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 4, 1, 4),
    _Tp5000eImageCurrState_Type()
)
tp5000eImageCurrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eImageCurrState.setStatus("current")
_Tp5000eImageInfoMsg_Type = DisplayString
_Tp5000eImageInfoMsg_Object = MibTableColumn
tp5000eImageInfoMsg = _Tp5000eImageInfoMsg_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 4, 1, 5),
    _Tp5000eImageInfoMsg_Type()
)
tp5000eImageInfoMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eImageInfoMsg.setStatus("current")
_Tp5000eRebootTable_Object = MibTable
tp5000eRebootTable = _Tp5000eRebootTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 5)
)
if mibBuilder.loadTexts:
    tp5000eRebootTable.setStatus("current")
_Tp5000eRebootEntry_Object = MibTableRow
tp5000eRebootEntry = _Tp5000eRebootEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 5, 1)
)
tp5000eRebootEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TP5000E", "tp5000eRebootIndex"),
)
if mibBuilder.loadTexts:
    tp5000eRebootEntry.setStatus("current")


class _Tp5000eRebootIndex_Type(Integer32):
    """Custom type tp5000eRebootIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Tp5000eRebootIndex_Type.__name__ = "Integer32"
_Tp5000eRebootIndex_Object = MibTableColumn
tp5000eRebootIndex = _Tp5000eRebootIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 5, 1, 1),
    _Tp5000eRebootIndex_Type()
)
tp5000eRebootIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eRebootIndex.setStatus("current")
_Tp5000eRebootAction_Type = ACTIONONLY
_Tp5000eRebootAction_Object = MibTableColumn
tp5000eRebootAction = _Tp5000eRebootAction_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 5, 1, 2),
    _Tp5000eRebootAction_Type()
)
tp5000eRebootAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRebootAction.setStatus("current")
_Tp5000eAuthRADIUSTable_Object = MibTable
tp5000eAuthRADIUSTable = _Tp5000eAuthRADIUSTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 6)
)
if mibBuilder.loadTexts:
    tp5000eAuthRADIUSTable.setStatus("current")
_Tp5000eAuthRADIUSEntry_Object = MibTableRow
tp5000eAuthRADIUSEntry = _Tp5000eAuthRADIUSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 6, 1)
)
tp5000eAuthRADIUSEntry.setIndexNames(
    (0, "TP5000E", "tp5000eAuthRADIUSIndex"),
)
if mibBuilder.loadTexts:
    tp5000eAuthRADIUSEntry.setStatus("current")


class _Tp5000eAuthRADIUSIndex_Type(Integer32):
    """Custom type tp5000eAuthRADIUSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Tp5000eAuthRADIUSIndex_Type.__name__ = "Integer32"
_Tp5000eAuthRADIUSIndex_Object = MibTableColumn
tp5000eAuthRADIUSIndex = _Tp5000eAuthRADIUSIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 6, 1, 1),
    _Tp5000eAuthRADIUSIndex_Type()
)
tp5000eAuthRADIUSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eAuthRADIUSIndex.setStatus("current")
_Tp5000eServerRADIUSIPAddress_Type = IpAddress
_Tp5000eServerRADIUSIPAddress_Object = MibTableColumn
tp5000eServerRADIUSIPAddress = _Tp5000eServerRADIUSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 6, 1, 2),
    _Tp5000eServerRADIUSIPAddress_Type()
)
tp5000eServerRADIUSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eServerRADIUSIPAddress.setStatus("current")
_Tp5000eAuthRADIUSKey_Type = DisplayString
_Tp5000eAuthRADIUSKey_Object = MibTableColumn
tp5000eAuthRADIUSKey = _Tp5000eAuthRADIUSKey_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 6, 1, 3),
    _Tp5000eAuthRADIUSKey_Type()
)
tp5000eAuthRADIUSKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eAuthRADIUSKey.setStatus("current")
_Tp5000eAssetNum_Type = DisplayString
_Tp5000eAssetNum_Object = MibScalar
tp5000eAssetNum = _Tp5000eAssetNum_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 7),
    _Tp5000eAssetNum_Type()
)
tp5000eAssetNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eAssetNum.setStatus("current")
_Tp5000eIntraCommIPSet_Type = TP5000INTRAIPSET
_Tp5000eIntraCommIPSet_Object = MibScalar
tp5000eIntraCommIPSet = _Tp5000eIntraCommIPSet_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 8),
    _Tp5000eIntraCommIPSet_Type()
)
tp5000eIntraCommIPSet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIntraCommIPSet.setStatus("current")
_Tp5000eRadiusState_Type = EnableValue
_Tp5000eRadiusState_Object = MibScalar
tp5000eRadiusState = _Tp5000eRadiusState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 9),
    _Tp5000eRadiusState_Type()
)
tp5000eRadiusState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRadiusState.setStatus("current")
_Tp5000eLastConfig_Type = DisplayString
_Tp5000eLastConfig_Object = MibScalar
tp5000eLastConfig = _Tp5000eLastConfig_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 3, 10),
    _Tp5000eLastConfig_Type()
)
tp5000eLastConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eLastConfig.setStatus("current")
_Tp5000eGlobalService_ObjectIdentity = ObjectIdentity
tp5000eGlobalService = _Tp5000eGlobalService_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4)
)
_Tp5000ePacketServiceTable_Object = MibTable
tp5000ePacketServiceTable = _Tp5000ePacketServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    tp5000ePacketServiceTable.setStatus("current")
_Tp5000ePacketServiceEntry_Object = MibTableRow
tp5000ePacketServiceEntry = _Tp5000ePacketServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4, 1, 1)
)
tp5000ePacketServiceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TP5000E", "tp5000ePacketServiceIndex"),
)
if mibBuilder.loadTexts:
    tp5000ePacketServiceEntry.setStatus("current")


class _Tp5000ePacketServiceIndex_Type(Integer32):
    """Custom type tp5000ePacketServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Tp5000ePacketServiceIndex_Type.__name__ = "Integer32"
_Tp5000ePacketServiceIndex_Object = MibTableColumn
tp5000ePacketServiceIndex = _Tp5000ePacketServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4, 1, 1, 1),
    _Tp5000ePacketServiceIndex_Type()
)
tp5000ePacketServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000ePacketServiceIndex.setStatus("current")
_Tp5000ePacketServiceMode_Type = TP5000PACKETSERVICE
_Tp5000ePacketServiceMode_Object = MibTableColumn
tp5000ePacketServiceMode = _Tp5000ePacketServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4, 1, 1, 2),
    _Tp5000ePacketServiceMode_Type()
)
tp5000ePacketServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000ePacketServiceMode.setStatus("current")
_Tp5000eSSMOptionTable_Object = MibTable
tp5000eSSMOptionTable = _Tp5000eSSMOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4, 2)
)
if mibBuilder.loadTexts:
    tp5000eSSMOptionTable.setStatus("current")
_Tp5000eSSMOptionEntry_Object = MibTableRow
tp5000eSSMOptionEntry = _Tp5000eSSMOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4, 2, 1)
)
tp5000eSSMOptionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TP5000E", "tp5000eSSMOptionIndex"),
)
if mibBuilder.loadTexts:
    tp5000eSSMOptionEntry.setStatus("current")


class _Tp5000eSSMOptionIndex_Type(Integer32):
    """Custom type tp5000eSSMOptionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Tp5000eSSMOptionIndex_Type.__name__ = "Integer32"
_Tp5000eSSMOptionIndex_Object = MibTableColumn
tp5000eSSMOptionIndex = _Tp5000eSSMOptionIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4, 2, 1, 1),
    _Tp5000eSSMOptionIndex_Type()
)
tp5000eSSMOptionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eSSMOptionIndex.setStatus("current")
_Tp5000eSSMOption_Type = TP5000SSMOPTION
_Tp5000eSSMOption_Object = MibTableColumn
tp5000eSSMOption = _Tp5000eSSMOption_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4, 2, 1, 2),
    _Tp5000eSSMOption_Type()
)
tp5000eSSMOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eSSMOption.setStatus("current")


class _Tp5000ePTPClientDataTableLock_Type(Integer32):
    """Custom type tp5000ePTPClientDataTableLock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("unlocked", 0))
    )


_Tp5000ePTPClientDataTableLock_Type.__name__ = "Integer32"
_Tp5000ePTPClientDataTableLock_Object = MibScalar
tp5000ePTPClientDataTableLock = _Tp5000ePTPClientDataTableLock_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4, 3),
    _Tp5000ePTPClientDataTableLock_Type()
)
tp5000ePTPClientDataTableLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000ePTPClientDataTableLock.setStatus("current")


class _Tp5000ePacketServiceExtendedMode_Type(Integer32):
    """Custom type tp5000ePacketServiceExtendedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1),
          ("notavailable", 3))
    )


_Tp5000ePacketServiceExtendedMode_Type.__name__ = "Integer32"
_Tp5000ePacketServiceExtendedMode_Object = MibScalar
tp5000ePacketServiceExtendedMode = _Tp5000ePacketServiceExtendedMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 4, 4),
    _Tp5000ePacketServiceExtendedMode_Type()
)
tp5000ePacketServiceExtendedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000ePacketServiceExtendedMode.setStatus("current")
_Tp5000ePTPClientMgmt_ObjectIdentity = ObjectIdentity
tp5000ePTPClientMgmt = _Tp5000ePTPClientMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 5)
)
_Tp5000eReferenceStatus_ObjectIdentity = ObjectIdentity
tp5000eReferenceStatus = _Tp5000eReferenceStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 6)
)
_Tp5000eInputPQLTable_Object = MibTable
tp5000eInputPQLTable = _Tp5000eInputPQLTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 6, 1)
)
if mibBuilder.loadTexts:
    tp5000eInputPQLTable.setStatus("current")
_Tp5000eInputPQLEntry_Object = MibTableRow
tp5000eInputPQLEntry = _Tp5000eInputPQLEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 6, 1, 1)
)
tp5000eInputPQLEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TP5000E", "tp5000eInputRefName"),
)
if mibBuilder.loadTexts:
    tp5000eInputPQLEntry.setStatus("current")
_Tp5000eInputRefName_Type = DisplayString
_Tp5000eInputRefName_Object = MibTableColumn
tp5000eInputRefName = _Tp5000eInputRefName_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 6, 1, 1, 1),
    _Tp5000eInputRefName_Type()
)
tp5000eInputRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eInputRefName.setStatus("current")
_Tp5000eInputRefActualPQL_Type = Integer32
_Tp5000eInputRefActualPQL_Object = MibTableColumn
tp5000eInputRefActualPQL = _Tp5000eInputRefActualPQL_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 6, 1, 1, 2),
    _Tp5000eInputRefActualPQL_Type()
)
tp5000eInputRefActualPQL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eInputRefActualPQL.setStatus("current")
_Tp5000eInputRefQualified_Type = TP5000REFQUALIFICATION
_Tp5000eInputRefQualified_Object = MibTableColumn
tp5000eInputRefQualified = _Tp5000eInputRefQualified_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 6, 1, 1, 3),
    _Tp5000eInputRefQualified_Type()
)
tp5000eInputRefQualified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eInputRefQualified.setStatus("current")
_Tp5000eSymmMetrics_ObjectIdentity = ObjectIdentity
tp5000eSymmMetrics = _Tp5000eSymmMetrics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 6, 2)
)
_Tp5000eRefConfig_ObjectIdentity = ObjectIdentity
tp5000eRefConfig = _Tp5000eRefConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 7)
)
_Tp5000eRefTimingMode_Type = TP5000REFTIMINGMODE
_Tp5000eRefTimingMode_Object = MibScalar
tp5000eRefTimingMode = _Tp5000eRefTimingMode_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 7, 1),
    _Tp5000eRefTimingMode_Type()
)
tp5000eRefTimingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRefTimingMode.setStatus("current")
_Tp5000eRefSelectionCriteria_Type = TP5000REFSELECTMODE
_Tp5000eRefSelectionCriteria_Object = MibScalar
tp5000eRefSelectionCriteria = _Tp5000eRefSelectionCriteria_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 7, 2),
    _Tp5000eRefSelectionCriteria_Type()
)
tp5000eRefSelectionCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRefSelectionCriteria.setStatus("current")
_Tp5000eRefConfigTable_Object = MibTable
tp5000eRefConfigTable = _Tp5000eRefConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 7, 3)
)
if mibBuilder.loadTexts:
    tp5000eRefConfigTable.setStatus("current")
_Tp5000eRefConfigEntry_Object = MibTableRow
tp5000eRefConfigEntry = _Tp5000eRefConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 7, 3, 1)
)
tp5000eRefConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TP5000E", "tp5000eRefName"),
)
if mibBuilder.loadTexts:
    tp5000eRefConfigEntry.setStatus("current")
_Tp5000eRefName_Type = DisplayString
_Tp5000eRefName_Object = MibTableColumn
tp5000eRefName = _Tp5000eRefName_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 7, 3, 1, 1),
    _Tp5000eRefName_Type()
)
tp5000eRefName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eRefName.setStatus("current")
_Tp5000eRefState_Type = EnableValue
_Tp5000eRefState_Object = MibTableColumn
tp5000eRefState = _Tp5000eRefState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 7, 3, 1, 2),
    _Tp5000eRefState_Type()
)
tp5000eRefState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRefState.setStatus("current")
_Tp5000eRefPriority_Type = Integer32
_Tp5000eRefPriority_Object = MibTableColumn
tp5000eRefPriority = _Tp5000eRefPriority_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 7, 3, 1, 3),
    _Tp5000eRefPriority_Type()
)
tp5000eRefPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRefPriority.setStatus("current")
_Tp5000eRefPQLState_Type = EnableValue
_Tp5000eRefPQLState_Object = MibTableColumn
tp5000eRefPQLState = _Tp5000eRefPQLState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 7, 3, 1, 4),
    _Tp5000eRefPQLState_Type()
)
tp5000eRefPQLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRefPQLState.setStatus("current")


class _Tp5000eRefPQL_Type(Integer32):
    """Custom type tp5000eRefPQL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_Tp5000eRefPQL_Type.__name__ = "Integer32"
_Tp5000eRefPQL_Object = MibTableColumn
tp5000eRefPQL = _Tp5000eRefPQL_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 7, 3, 1, 5),
    _Tp5000eRefPQL_Type()
)
tp5000eRefPQL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eRefPQL.setStatus("current")
_Tp5000eClock_ObjectIdentity = ObjectIdentity
tp5000eClock = _Tp5000eClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8)
)
_Tp5000eClockStatus_ObjectIdentity = ObjectIdentity
tp5000eClockStatus = _Tp5000eClockStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 1)
)
_Tp5000eClockStatusTable_Object = MibTable
tp5000eClockStatusTable = _Tp5000eClockStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    tp5000eClockStatusTable.setStatus("current")
_Tp5000eClockStatusEntry_Object = MibTableRow
tp5000eClockStatusEntry = _Tp5000eClockStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 1, 1, 1)
)
tp5000eClockStatusEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "TP5000E", "tp5000eClockStatusIndex"),
)
if mibBuilder.loadTexts:
    tp5000eClockStatusEntry.setStatus("current")


class _Tp5000eClockStatusIndex_Type(Integer32):
    """Custom type tp5000eClockStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_Tp5000eClockStatusIndex_Type.__name__ = "Integer32"
_Tp5000eClockStatusIndex_Object = MibTableColumn
tp5000eClockStatusIndex = _Tp5000eClockStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 1, 1, 1, 1),
    _Tp5000eClockStatusIndex_Type()
)
tp5000eClockStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eClockStatusIndex.setStatus("current")
_Tp5000eServoControlStatus_Type = TP5000SERVOCTL
_Tp5000eServoControlStatus_Object = MibTableColumn
tp5000eServoControlStatus = _Tp5000eServoControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 1, 1, 1, 2),
    _Tp5000eServoControlStatus_Type()
)
tp5000eServoControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eServoControlStatus.setStatus("current")
_Tp5000ePhaseOffset_Type = DisplayString
_Tp5000ePhaseOffset_Object = MibTableColumn
tp5000ePhaseOffset = _Tp5000ePhaseOffset_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 1, 1, 1, 3),
    _Tp5000ePhaseOffset_Type()
)
tp5000ePhaseOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000ePhaseOffset.setStatus("current")
_Tp5000eClockConfig_ObjectIdentity = ObjectIdentity
tp5000eClockConfig = _Tp5000eClockConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 2)
)


class _Tp5000eBridgingTime_Type(Unsigned32):
    """Custom type tp5000eBridgingTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 200000),
    )


_Tp5000eBridgingTime_Type.__name__ = "Unsigned32"
_Tp5000eBridgingTime_Object = MibScalar
tp5000eBridgingTime = _Tp5000eBridgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 2, 1),
    _Tp5000eBridgingTime_Type()
)
tp5000eBridgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eBridgingTime.setStatus("current")
if mibBuilder.loadTexts:
    tp5000eBridgingTime.setUnits("Second")
_Tp5000eAutoSync_Type = EnableValue
_Tp5000eAutoSync_Object = MibScalar
tp5000eAutoSync = _Tp5000eAutoSync_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 2, 2),
    _Tp5000eAutoSync_Type()
)
tp5000eAutoSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eAutoSync.setStatus("current")
_Tp5000eSync_Type = DisplayString
_Tp5000eSync_Object = MibScalar
tp5000eSync = _Tp5000eSync_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 2, 3),
    _Tp5000eSync_Type()
)
tp5000eSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eSync.setStatus("current")


class _Tp5000eHoldoverExceededTimeQz_Type(Unsigned32):
    """Custom type tp5000eHoldoverExceededTimeQz based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000000),
    )


_Tp5000eHoldoverExceededTimeQz_Type.__name__ = "Unsigned32"
_Tp5000eHoldoverExceededTimeQz_Object = MibScalar
tp5000eHoldoverExceededTimeQz = _Tp5000eHoldoverExceededTimeQz_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 2, 4),
    _Tp5000eHoldoverExceededTimeQz_Type()
)
tp5000eHoldoverExceededTimeQz.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eHoldoverExceededTimeQz.setStatus("current")
if mibBuilder.loadTexts:
    tp5000eHoldoverExceededTimeQz.setUnits("Seconds")


class _Tp5000eHoldoverExceededTimeRb_Type(Unsigned32):
    """Custom type tp5000eHoldoverExceededTimeRb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3000000),
    )


_Tp5000eHoldoverExceededTimeRb_Type.__name__ = "Unsigned32"
_Tp5000eHoldoverExceededTimeRb_Object = MibScalar
tp5000eHoldoverExceededTimeRb = _Tp5000eHoldoverExceededTimeRb_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 8, 2, 5),
    _Tp5000eHoldoverExceededTimeRb_Type()
)
tp5000eHoldoverExceededTimeRb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eHoldoverExceededTimeRb.setStatus("current")
if mibBuilder.loadTexts:
    tp5000eHoldoverExceededTimeRb.setUnits("Seconds")
_Tp5000eHardwareHierarchy_ObjectIdentity = ObjectIdentity
tp5000eHardwareHierarchy = _Tp5000eHardwareHierarchy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9)
)
_Tp5000eIfTable_Object = MibTable
tp5000eIfTable = _Tp5000eIfTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 1)
)
if mibBuilder.loadTexts:
    tp5000eIfTable.setStatus("current")
_Tp5000eIfEntry_Object = MibTableRow
tp5000eIfEntry = _Tp5000eIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 1, 1)
)
tp5000eIfEntry.setIndexNames(
    (0, "TP5000E", "tp5000eIfIndex"),
)
if mibBuilder.loadTexts:
    tp5000eIfEntry.setStatus("current")


class _Tp5000eIfIndex_Type(Integer32):
    """Custom type tp5000eIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Tp5000eIfIndex_Type.__name__ = "Integer32"
_Tp5000eIfIndex_Object = MibTableColumn
tp5000eIfIndex = _Tp5000eIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 1, 1, 1),
    _Tp5000eIfIndex_Type()
)
tp5000eIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eIfIndex.setStatus("current")
_Tp5000eIfModuleID_Type = TP5000MODULEID
_Tp5000eIfModuleID_Object = MibTableColumn
tp5000eIfModuleID = _Tp5000eIfModuleID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 1, 1, 2),
    _Tp5000eIfModuleID_Type()
)
tp5000eIfModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eIfModuleID.setStatus("current")
_Tp5000eIfPortID_Type = Integer32
_Tp5000eIfPortID_Object = MibTableColumn
tp5000eIfPortID = _Tp5000eIfPortID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 1, 1, 3),
    _Tp5000eIfPortID_Type()
)
tp5000eIfPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eIfPortID.setStatus("current")
_Tp5000eIfTableIndex_Type = Unsigned32
_Tp5000eIfTableIndex_Object = MibTableColumn
tp5000eIfTableIndex = _Tp5000eIfTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 1, 1, 4),
    _Tp5000eIfTableIndex_Type()
)
tp5000eIfTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eIfTableIndex.setStatus("current")
_Tp5000eEntPhysicalTable_Object = MibTable
tp5000eEntPhysicalTable = _Tp5000eEntPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 2)
)
if mibBuilder.loadTexts:
    tp5000eEntPhysicalTable.setStatus("current")
_Tp5000eEntPhysicalEntry_Object = MibTableRow
tp5000eEntPhysicalEntry = _Tp5000eEntPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 2, 1)
)
tp5000eEntPhysicalEntry.setIndexNames(
    (0, "TP5000E", "tp5000eEntPhysicalIndex"),
)
if mibBuilder.loadTexts:
    tp5000eEntPhysicalEntry.setStatus("current")


class _Tp5000eEntPhysicalIndex_Type(Integer32):
    """Custom type tp5000eEntPhysicalIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Tp5000eEntPhysicalIndex_Type.__name__ = "Integer32"
_Tp5000eEntPhysicalIndex_Object = MibTableColumn
tp5000eEntPhysicalIndex = _Tp5000eEntPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 2, 1, 1),
    _Tp5000eEntPhysicalIndex_Type()
)
tp5000eEntPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eEntPhysicalIndex.setStatus("current")
_Tp5000eEntPhysicalModuleID_Type = TP5000MODULEID
_Tp5000eEntPhysicalModuleID_Object = MibTableColumn
tp5000eEntPhysicalModuleID = _Tp5000eEntPhysicalModuleID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 2, 1, 2),
    _Tp5000eEntPhysicalModuleID_Type()
)
tp5000eEntPhysicalModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eEntPhysicalModuleID.setStatus("current")
_Tp5000eEntPhysicalStackID_Type = Integer32
_Tp5000eEntPhysicalStackID_Object = MibTableColumn
tp5000eEntPhysicalStackID = _Tp5000eEntPhysicalStackID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 2, 1, 3),
    _Tp5000eEntPhysicalStackID_Type()
)
tp5000eEntPhysicalStackID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eEntPhysicalStackID.setStatus("current")
_Tp5000eEntPhysicalChassisID_Type = Integer32
_Tp5000eEntPhysicalChassisID_Object = MibTableColumn
tp5000eEntPhysicalChassisID = _Tp5000eEntPhysicalChassisID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 2, 1, 4),
    _Tp5000eEntPhysicalChassisID_Type()
)
tp5000eEntPhysicalChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eEntPhysicalChassisID.setStatus("current")
_Tp5000eEntPhysicalPartIndex_Type = Integer32
_Tp5000eEntPhysicalPartIndex_Object = MibTableColumn
tp5000eEntPhysicalPartIndex = _Tp5000eEntPhysicalPartIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 2, 1, 5),
    _Tp5000eEntPhysicalPartIndex_Type()
)
tp5000eEntPhysicalPartIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eEntPhysicalPartIndex.setStatus("current")
_Tp5000eEntPhysicalTableIndex_Type = Integer32
_Tp5000eEntPhysicalTableIndex_Object = MibTableColumn
tp5000eEntPhysicalTableIndex = _Tp5000eEntPhysicalTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 9, 2, 1, 6),
    _Tp5000eEntPhysicalTableIndex_Type()
)
tp5000eEntPhysicalTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eEntPhysicalTableIndex.setStatus("current")
_Tp5000eVlanConfig_ObjectIdentity = ObjectIdentity
tp5000eVlanConfig = _Tp5000eVlanConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10)
)
_Tp5000eNonfixedVlanTable_Object = MibTable
tp5000eNonfixedVlanTable = _Tp5000eNonfixedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1)
)
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanTable.setStatus("current")
_Tp5000eNonfixedVlanEntry_Object = MibTableRow
tp5000eNonfixedVlanEntry = _Tp5000eNonfixedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1)
)
tp5000eNonfixedVlanEntry.setIndexNames(
    (0, "TP5000E", "tp5000eNonfixedVlanIndex"),
)
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanEntry.setStatus("current")


class _Tp5000eNonfixedVlanIndex_Type(Integer32):
    """Custom type tp5000eNonfixedVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_Tp5000eNonfixedVlanIndex_Type.__name__ = "Integer32"
_Tp5000eNonfixedVlanIndex_Object = MibTableColumn
tp5000eNonfixedVlanIndex = _Tp5000eNonfixedVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1, 1),
    _Tp5000eNonfixedVlanIndex_Type()
)
tp5000eNonfixedVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanIndex.setStatus("current")
_Tp5000eNonfixedVlanIfIndex_Type = Unsigned32
_Tp5000eNonfixedVlanIfIndex_Object = MibTableColumn
tp5000eNonfixedVlanIfIndex = _Tp5000eNonfixedVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1, 2),
    _Tp5000eNonfixedVlanIfIndex_Type()
)
tp5000eNonfixedVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanIfIndex.setStatus("current")
_Tp5000eNonfixedVlanModuleID_Type = TP5000MODULEID
_Tp5000eNonfixedVlanModuleID_Object = MibTableColumn
tp5000eNonfixedVlanModuleID = _Tp5000eNonfixedVlanModuleID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1, 3),
    _Tp5000eNonfixedVlanModuleID_Type()
)
tp5000eNonfixedVlanModuleID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanModuleID.setStatus("current")
_Tp5000eNonfixedVlanPortID_Type = Integer32
_Tp5000eNonfixedVlanPortID_Object = MibTableColumn
tp5000eNonfixedVlanPortID = _Tp5000eNonfixedVlanPortID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1, 4),
    _Tp5000eNonfixedVlanPortID_Type()
)
tp5000eNonfixedVlanPortID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanPortID.setStatus("current")


class _Tp5000eNonfixedVlanId_Type(Integer32):
    """Custom type tp5000eNonfixedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Tp5000eNonfixedVlanId_Type.__name__ = "Integer32"
_Tp5000eNonfixedVlanId_Object = MibTableColumn
tp5000eNonfixedVlanId = _Tp5000eNonfixedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1, 5),
    _Tp5000eNonfixedVlanId_Type()
)
tp5000eNonfixedVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanId.setStatus("current")


class _Tp5000eNonfixedVlanPriority_Type(Integer32):
    """Custom type tp5000eNonfixedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Tp5000eNonfixedVlanPriority_Type.__name__ = "Integer32"
_Tp5000eNonfixedVlanPriority_Object = MibTableColumn
tp5000eNonfixedVlanPriority = _Tp5000eNonfixedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1, 6),
    _Tp5000eNonfixedVlanPriority_Type()
)
tp5000eNonfixedVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanPriority.setStatus("current")
_Tp5000eNonfixedVlanIPv4Addr_Type = IpAddress
_Tp5000eNonfixedVlanIPv4Addr_Object = MibTableColumn
tp5000eNonfixedVlanIPv4Addr = _Tp5000eNonfixedVlanIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1, 7),
    _Tp5000eNonfixedVlanIPv4Addr_Type()
)
tp5000eNonfixedVlanIPv4Addr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanIPv4Addr.setStatus("current")
_Tp5000eNonfixedVlanNetmask_Type = IpAddress
_Tp5000eNonfixedVlanNetmask_Object = MibTableColumn
tp5000eNonfixedVlanNetmask = _Tp5000eNonfixedVlanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1, 8),
    _Tp5000eNonfixedVlanNetmask_Type()
)
tp5000eNonfixedVlanNetmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanNetmask.setStatus("current")
_Tp5000eNonfixedVlanState_Type = EnableValue
_Tp5000eNonfixedVlanState_Object = MibTableColumn
tp5000eNonfixedVlanState = _Tp5000eNonfixedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1, 9),
    _Tp5000eNonfixedVlanState_Type()
)
tp5000eNonfixedVlanState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanState.setStatus("current")
_Tp5000eNonfixedVlanRowStatus_Type = RowStatus
_Tp5000eNonfixedVlanRowStatus_Object = MibTableColumn
tp5000eNonfixedVlanRowStatus = _Tp5000eNonfixedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 1, 1, 10),
    _Tp5000eNonfixedVlanRowStatus_Type()
)
tp5000eNonfixedVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanRowStatus.setStatus("current")
_Tp5000eFixedVlanTable_Object = MibTable
tp5000eFixedVlanTable = _Tp5000eFixedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 2)
)
if mibBuilder.loadTexts:
    tp5000eFixedVlanTable.setStatus("current")
_Tp5000eFixedVlanEntry_Object = MibTableRow
tp5000eFixedVlanEntry = _Tp5000eFixedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 2, 1)
)
tp5000eFixedVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TP5000E", "tp5000eFixedVlanIndex"),
)
if mibBuilder.loadTexts:
    tp5000eFixedVlanEntry.setStatus("current")


class _Tp5000eFixedVlanIndex_Type(Integer32):
    """Custom type tp5000eFixedVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Tp5000eFixedVlanIndex_Type.__name__ = "Integer32"
_Tp5000eFixedVlanIndex_Object = MibTableColumn
tp5000eFixedVlanIndex = _Tp5000eFixedVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 2, 1, 1),
    _Tp5000eFixedVlanIndex_Type()
)
tp5000eFixedVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eFixedVlanIndex.setStatus("current")


class _Tp5000eFixedVlanId_Type(Integer32):
    """Custom type tp5000eFixedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Tp5000eFixedVlanId_Type.__name__ = "Integer32"
_Tp5000eFixedVlanId_Object = MibTableColumn
tp5000eFixedVlanId = _Tp5000eFixedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 2, 1, 2),
    _Tp5000eFixedVlanId_Type()
)
tp5000eFixedVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eFixedVlanId.setStatus("current")


class _Tp5000eFixedVlanPriority_Type(Integer32):
    """Custom type tp5000eFixedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Tp5000eFixedVlanPriority_Type.__name__ = "Integer32"
_Tp5000eFixedVlanPriority_Object = MibTableColumn
tp5000eFixedVlanPriority = _Tp5000eFixedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 2, 1, 3),
    _Tp5000eFixedVlanPriority_Type()
)
tp5000eFixedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eFixedVlanPriority.setStatus("current")
_Tp5000eFixedVlanIPv4Addr_Type = IpAddress
_Tp5000eFixedVlanIPv4Addr_Object = MibTableColumn
tp5000eFixedVlanIPv4Addr = _Tp5000eFixedVlanIPv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 2, 1, 4),
    _Tp5000eFixedVlanIPv4Addr_Type()
)
tp5000eFixedVlanIPv4Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eFixedVlanIPv4Addr.setStatus("current")
_Tp5000eFixedVlanNetmask_Type = IpAddress
_Tp5000eFixedVlanNetmask_Object = MibTableColumn
tp5000eFixedVlanNetmask = _Tp5000eFixedVlanNetmask_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 2, 1, 5),
    _Tp5000eFixedVlanNetmask_Type()
)
tp5000eFixedVlanNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eFixedVlanNetmask.setStatus("current")
_Tp5000eFixedVlanGateway_Type = IpAddress
_Tp5000eFixedVlanGateway_Object = MibTableColumn
tp5000eFixedVlanGateway = _Tp5000eFixedVlanGateway_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 2, 1, 6),
    _Tp5000eFixedVlanGateway_Type()
)
tp5000eFixedVlanGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eFixedVlanGateway.setStatus("current")
_Tp5000eFixedVlanState_Type = EnableValue
_Tp5000eFixedVlanState_Object = MibTableColumn
tp5000eFixedVlanState = _Tp5000eFixedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 2, 1, 7),
    _Tp5000eFixedVlanState_Type()
)
tp5000eFixedVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eFixedVlanState.setStatus("current")
_Tp5000eVlanModeTable_Object = MibTable
tp5000eVlanModeTable = _Tp5000eVlanModeTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 3)
)
if mibBuilder.loadTexts:
    tp5000eVlanModeTable.setStatus("current")
_Tp5000eVlanModeEntry_Object = MibTableRow
tp5000eVlanModeEntry = _Tp5000eVlanModeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 3, 1)
)
tp5000eVlanModeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TP5000E", "tp5000eVlanModeIndex"),
)
if mibBuilder.loadTexts:
    tp5000eVlanModeEntry.setStatus("current")


class _Tp5000eVlanModeIndex_Type(Integer32):
    """Custom type tp5000eVlanModeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Tp5000eVlanModeIndex_Type.__name__ = "Integer32"
_Tp5000eVlanModeIndex_Object = MibTableColumn
tp5000eVlanModeIndex = _Tp5000eVlanModeIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 3, 1, 1),
    _Tp5000eVlanModeIndex_Type()
)
tp5000eVlanModeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eVlanModeIndex.setStatus("current")
_Tp5000eVlanModeModuleID_Type = TP5000MODULEID
_Tp5000eVlanModeModuleID_Object = MibTableColumn
tp5000eVlanModeModuleID = _Tp5000eVlanModeModuleID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 3, 1, 2),
    _Tp5000eVlanModeModuleID_Type()
)
tp5000eVlanModeModuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eVlanModeModuleID.setStatus("current")
_Tp5000eVlanModePortID_Type = Integer32
_Tp5000eVlanModePortID_Object = MibTableColumn
tp5000eVlanModePortID = _Tp5000eVlanModePortID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 3, 1, 3),
    _Tp5000eVlanModePortID_Type()
)
tp5000eVlanModePortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eVlanModePortID.setStatus("current")
_Tp5000eVlanModeValue_Type = EnableValue
_Tp5000eVlanModeValue_Object = MibTableColumn
tp5000eVlanModeValue = _Tp5000eVlanModeValue_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 3, 1, 4),
    _Tp5000eVlanModeValue_Type()
)
tp5000eVlanModeValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eVlanModeValue.setStatus("current")
_Tp5000eIPv6NonfixedVlanTable_Object = MibTable
tp5000eIPv6NonfixedVlanTable = _Tp5000eIPv6NonfixedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4)
)
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanTable.setStatus("current")
_Tp5000eIPv6NonfixedVlanEntry_Object = MibTableRow
tp5000eIPv6NonfixedVlanEntry = _Tp5000eIPv6NonfixedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1)
)
tp5000eIPv6NonfixedVlanEntry.setIndexNames(
    (0, "TP5000E", "tp5000eIPv6NonfixedVlanIndex"),
)
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanEntry.setStatus("current")


class _Tp5000eIPv6NonfixedVlanIndex_Type(Integer32):
    """Custom type tp5000eIPv6NonfixedVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_Tp5000eIPv6NonfixedVlanIndex_Type.__name__ = "Integer32"
_Tp5000eIPv6NonfixedVlanIndex_Object = MibTableColumn
tp5000eIPv6NonfixedVlanIndex = _Tp5000eIPv6NonfixedVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1, 1),
    _Tp5000eIPv6NonfixedVlanIndex_Type()
)
tp5000eIPv6NonfixedVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanIndex.setStatus("current")
_Tp5000eIPv6NonfixedVlanIfIndex_Type = Unsigned32
_Tp5000eIPv6NonfixedVlanIfIndex_Object = MibTableColumn
tp5000eIPv6NonfixedVlanIfIndex = _Tp5000eIPv6NonfixedVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1, 2),
    _Tp5000eIPv6NonfixedVlanIfIndex_Type()
)
tp5000eIPv6NonfixedVlanIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanIfIndex.setStatus("current")
_Tp5000eIPv6NonfixedVlanModuleID_Type = TP5000MODULEID
_Tp5000eIPv6NonfixedVlanModuleID_Object = MibTableColumn
tp5000eIPv6NonfixedVlanModuleID = _Tp5000eIPv6NonfixedVlanModuleID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1, 3),
    _Tp5000eIPv6NonfixedVlanModuleID_Type()
)
tp5000eIPv6NonfixedVlanModuleID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanModuleID.setStatus("current")
_Tp5000eIPv6NonfixedVlanPortID_Type = Integer32
_Tp5000eIPv6NonfixedVlanPortID_Object = MibTableColumn
tp5000eIPv6NonfixedVlanPortID = _Tp5000eIPv6NonfixedVlanPortID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1, 4),
    _Tp5000eIPv6NonfixedVlanPortID_Type()
)
tp5000eIPv6NonfixedVlanPortID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanPortID.setStatus("current")


class _Tp5000eIPv6NonfixedVlanId_Type(Integer32):
    """Custom type tp5000eIPv6NonfixedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_Tp5000eIPv6NonfixedVlanId_Type.__name__ = "Integer32"
_Tp5000eIPv6NonfixedVlanId_Object = MibTableColumn
tp5000eIPv6NonfixedVlanId = _Tp5000eIPv6NonfixedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1, 5),
    _Tp5000eIPv6NonfixedVlanId_Type()
)
tp5000eIPv6NonfixedVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanId.setStatus("current")


class _Tp5000eIPv6NonfixedVlanPriority_Type(Integer32):
    """Custom type tp5000eIPv6NonfixedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Tp5000eIPv6NonfixedVlanPriority_Type.__name__ = "Integer32"
_Tp5000eIPv6NonfixedVlanPriority_Object = MibTableColumn
tp5000eIPv6NonfixedVlanPriority = _Tp5000eIPv6NonfixedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1, 6),
    _Tp5000eIPv6NonfixedVlanPriority_Type()
)
tp5000eIPv6NonfixedVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanPriority.setStatus("current")
_Tp5000eIPv6NonfixedVlanAddr_Type = InetAddressIPv6
_Tp5000eIPv6NonfixedVlanAddr_Object = MibTableColumn
tp5000eIPv6NonfixedVlanAddr = _Tp5000eIPv6NonfixedVlanAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1, 7),
    _Tp5000eIPv6NonfixedVlanAddr_Type()
)
tp5000eIPv6NonfixedVlanAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanAddr.setStatus("current")


class _Tp5000eIPv6NonfixedVlanPrefix_Type(Integer32):
    """Custom type tp5000eIPv6NonfixedVlanPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Tp5000eIPv6NonfixedVlanPrefix_Type.__name__ = "Integer32"
_Tp5000eIPv6NonfixedVlanPrefix_Object = MibTableColumn
tp5000eIPv6NonfixedVlanPrefix = _Tp5000eIPv6NonfixedVlanPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1, 8),
    _Tp5000eIPv6NonfixedVlanPrefix_Type()
)
tp5000eIPv6NonfixedVlanPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanPrefix.setStatus("current")
_Tp5000eIPv6NonfixedVlanState_Type = EnableValue
_Tp5000eIPv6NonfixedVlanState_Object = MibTableColumn
tp5000eIPv6NonfixedVlanState = _Tp5000eIPv6NonfixedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1, 9),
    _Tp5000eIPv6NonfixedVlanState_Type()
)
tp5000eIPv6NonfixedVlanState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanState.setStatus("current")
_Tp5000eIPv6NonfixedVlanRowStatus_Type = RowStatus
_Tp5000eIPv6NonfixedVlanRowStatus_Object = MibTableColumn
tp5000eIPv6NonfixedVlanRowStatus = _Tp5000eIPv6NonfixedVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 4, 1, 10),
    _Tp5000eIPv6NonfixedVlanRowStatus_Type()
)
tp5000eIPv6NonfixedVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanRowStatus.setStatus("current")
_Tp5000eIPv6FixedVlanTable_Object = MibTable
tp5000eIPv6FixedVlanTable = _Tp5000eIPv6FixedVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 5)
)
if mibBuilder.loadTexts:
    tp5000eIPv6FixedVlanTable.setStatus("current")
_Tp5000eIPv6FixedVlanEntry_Object = MibTableRow
tp5000eIPv6FixedVlanEntry = _Tp5000eIPv6FixedVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 5, 1)
)
tp5000eIPv6FixedVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "TP5000E", "tp5000eIPv6FixedVlanIndex"),
)
if mibBuilder.loadTexts:
    tp5000eIPv6FixedVlanEntry.setStatus("current")


class _Tp5000eIPv6FixedVlanIndex_Type(Integer32):
    """Custom type tp5000eIPv6FixedVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_Tp5000eIPv6FixedVlanIndex_Type.__name__ = "Integer32"
_Tp5000eIPv6FixedVlanIndex_Object = MibTableColumn
tp5000eIPv6FixedVlanIndex = _Tp5000eIPv6FixedVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 5, 1, 1),
    _Tp5000eIPv6FixedVlanIndex_Type()
)
tp5000eIPv6FixedVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tp5000eIPv6FixedVlanIndex.setStatus("current")


class _Tp5000eIPv6FixedVlanId_Type(Integer32):
    """Custom type tp5000eIPv6FixedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_Tp5000eIPv6FixedVlanId_Type.__name__ = "Integer32"
_Tp5000eIPv6FixedVlanId_Object = MibTableColumn
tp5000eIPv6FixedVlanId = _Tp5000eIPv6FixedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 5, 1, 2),
    _Tp5000eIPv6FixedVlanId_Type()
)
tp5000eIPv6FixedVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIPv6FixedVlanId.setStatus("current")


class _Tp5000eIPv6FixedVlanPriority_Type(Integer32):
    """Custom type tp5000eIPv6FixedVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_Tp5000eIPv6FixedVlanPriority_Type.__name__ = "Integer32"
_Tp5000eIPv6FixedVlanPriority_Object = MibTableColumn
tp5000eIPv6FixedVlanPriority = _Tp5000eIPv6FixedVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 5, 1, 3),
    _Tp5000eIPv6FixedVlanPriority_Type()
)
tp5000eIPv6FixedVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIPv6FixedVlanPriority.setStatus("current")
_Tp5000eIPv6FixedVlanAddr_Type = InetAddressIPv6
_Tp5000eIPv6FixedVlanAddr_Object = MibTableColumn
tp5000eIPv6FixedVlanAddr = _Tp5000eIPv6FixedVlanAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 5, 1, 4),
    _Tp5000eIPv6FixedVlanAddr_Type()
)
tp5000eIPv6FixedVlanAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIPv6FixedVlanAddr.setStatus("current")


class _Tp5000eIPv6FixedVlanPrefix_Type(Integer32):
    """Custom type tp5000eIPv6FixedVlanPrefix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_Tp5000eIPv6FixedVlanPrefix_Type.__name__ = "Integer32"
_Tp5000eIPv6FixedVlanPrefix_Object = MibTableColumn
tp5000eIPv6FixedVlanPrefix = _Tp5000eIPv6FixedVlanPrefix_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 5, 1, 5),
    _Tp5000eIPv6FixedVlanPrefix_Type()
)
tp5000eIPv6FixedVlanPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIPv6FixedVlanPrefix.setStatus("current")
_Tp5000eIPv6FixedVlanDefaultRouter_Type = InetAddressIPv6
_Tp5000eIPv6FixedVlanDefaultRouter_Object = MibTableColumn
tp5000eIPv6FixedVlanDefaultRouter = _Tp5000eIPv6FixedVlanDefaultRouter_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 5, 1, 6),
    _Tp5000eIPv6FixedVlanDefaultRouter_Type()
)
tp5000eIPv6FixedVlanDefaultRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIPv6FixedVlanDefaultRouter.setStatus("current")
_Tp5000eIPv6FixedVlanState_Type = EnableValue
_Tp5000eIPv6FixedVlanState_Object = MibTableColumn
tp5000eIPv6FixedVlanState = _Tp5000eIPv6FixedVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 10, 5, 1, 7),
    _Tp5000eIPv6FixedVlanState_Type()
)
tp5000eIPv6FixedVlanState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIPv6FixedVlanState.setStatus("current")
_Tp5000eAlarmNotification_ObjectIdentity = ObjectIdentity
tp5000eAlarmNotification = _Tp5000eAlarmNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11)
)
_Tp5000eNotifyElements_ObjectIdentity = ObjectIdentity
tp5000eNotifyElements = _Tp5000eNotifyElements_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1)
)
_Tp5000eNotifyModuleId_Type = TP5000MODULEID
_Tp5000eNotifyModuleId_Object = MibScalar
tp5000eNotifyModuleId = _Tp5000eNotifyModuleId_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1, 1),
    _Tp5000eNotifyModuleId_Type()
)
tp5000eNotifyModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNotifyModuleId.setStatus("current")
_Tp5000eNotifyAlarmEventID_Type = Unsigned32
_Tp5000eNotifyAlarmEventID_Object = MibScalar
tp5000eNotifyAlarmEventID = _Tp5000eNotifyAlarmEventID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1, 2),
    _Tp5000eNotifyAlarmEventID_Type()
)
tp5000eNotifyAlarmEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNotifyAlarmEventID.setStatus("current")
_Tp5000eNotifyIndex_Type = Unsigned32
_Tp5000eNotifyIndex_Object = MibScalar
tp5000eNotifyIndex = _Tp5000eNotifyIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1, 3),
    _Tp5000eNotifyIndex_Type()
)
tp5000eNotifyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNotifyIndex.setStatus("current")
_Tp5000eNotifySeverity_Type = ALARMLEVELTYPE
_Tp5000eNotifySeverity_Object = MibScalar
tp5000eNotifySeverity = _Tp5000eNotifySeverity_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1, 4),
    _Tp5000eNotifySeverity_Type()
)
tp5000eNotifySeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNotifySeverity.setStatus("current")
_Tp5000eNotifyTransient_Type = TP5000TRANSIENT
_Tp5000eNotifyTransient_Object = MibScalar
tp5000eNotifyTransient = _Tp5000eNotifyTransient_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1, 5),
    _Tp5000eNotifyTransient_Type()
)
tp5000eNotifyTransient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNotifyTransient.setStatus("current")
_Tp5000eNotifyDateTime_Type = DisplayString
_Tp5000eNotifyDateTime_Object = MibScalar
tp5000eNotifyDateTime = _Tp5000eNotifyDateTime_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1, 6),
    _Tp5000eNotifyDateTime_Type()
)
tp5000eNotifyDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNotifyDateTime.setStatus("current")
_Tp5000eNotifyDescription_Type = DisplayString
_Tp5000eNotifyDescription_Object = MibScalar
tp5000eNotifyDescription = _Tp5000eNotifyDescription_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1, 7),
    _Tp5000eNotifyDescription_Type()
)
tp5000eNotifyDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNotifyDescription.setStatus("current")
_Tp5000eNotifyClientAddr_Type = IpAddress
_Tp5000eNotifyClientAddr_Object = MibScalar
tp5000eNotifyClientAddr = _Tp5000eNotifyClientAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1, 8),
    _Tp5000eNotifyClientAddr_Type()
)
tp5000eNotifyClientAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNotifyClientAddr.setStatus("current")
_Tp5000eNotifySequenceNum_Type = Unsigned32
_Tp5000eNotifySequenceNum_Object = MibScalar
tp5000eNotifySequenceNum = _Tp5000eNotifySequenceNum_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1, 9),
    _Tp5000eNotifySequenceNum_Type()
)
tp5000eNotifySequenceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNotifySequenceNum.setStatus("current")
_Tp5000eNotifyClientClockID_Type = DisplayString
_Tp5000eNotifyClientClockID_Object = MibScalar
tp5000eNotifyClientClockID = _Tp5000eNotifyClientClockID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 1, 10),
    _Tp5000eNotifyClientClockID_Type()
)
tp5000eNotifyClientClockID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eNotifyClientClockID.setStatus("current")
_Tp5000eIPv6GlobalConfig_ObjectIdentity = ObjectIdentity
tp5000eIPv6GlobalConfig = _Tp5000eIPv6GlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12)
)
_SnmpIPv4IPv6ManagerTable_Object = MibTable
snmpIPv4IPv6ManagerTable = _SnmpIPv4IPv6ManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 1)
)
if mibBuilder.loadTexts:
    snmpIPv4IPv6ManagerTable.setStatus("current")
_SnmpIPv4IPv6ManagerEntry_Object = MibTableRow
snmpIPv4IPv6ManagerEntry = _SnmpIPv4IPv6ManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 1, 1)
)
snmpIPv4IPv6ManagerEntry.setIndexNames(
    (0, "TP5000E", "snmpIPv4IPv6ManagerIndex"),
)
if mibBuilder.loadTexts:
    snmpIPv4IPv6ManagerEntry.setStatus("current")


class _SnmpIPv4IPv6ManagerIndex_Type(Integer32):
    """Custom type snmpIPv4IPv6ManagerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SnmpIPv4IPv6ManagerIndex_Type.__name__ = "Integer32"
_SnmpIPv4IPv6ManagerIndex_Object = MibTableColumn
snmpIPv4IPv6ManagerIndex = _SnmpIPv4IPv6ManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 1, 1, 1),
    _SnmpIPv4IPv6ManagerIndex_Type()
)
snmpIPv4IPv6ManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    snmpIPv4IPv6ManagerIndex.setStatus("current")
_SnmpIPv4IPv6ManagerID_Type = DisplayString
_SnmpIPv4IPv6ManagerID_Object = MibTableColumn
snmpIPv4IPv6ManagerID = _SnmpIPv4IPv6ManagerID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 1, 1, 2),
    _SnmpIPv4IPv6ManagerID_Type()
)
snmpIPv4IPv6ManagerID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpIPv4IPv6ManagerID.setStatus("current")
_SnmpIPv4IPv6ManagerAddress_Type = DisplayString
_SnmpIPv4IPv6ManagerAddress_Object = MibTableColumn
snmpIPv4IPv6ManagerAddress = _SnmpIPv4IPv6ManagerAddress_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 1, 1, 3),
    _SnmpIPv4IPv6ManagerAddress_Type()
)
snmpIPv4IPv6ManagerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpIPv4IPv6ManagerAddress.setStatus("current")
_SnmpIPv4IPv6ManagerEngineID_Type = DisplayString
_SnmpIPv4IPv6ManagerEngineID_Object = MibTableColumn
snmpIPv4IPv6ManagerEngineID = _SnmpIPv4IPv6ManagerEngineID_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 1, 1, 4),
    _SnmpIPv4IPv6ManagerEngineID_Type()
)
snmpIPv4IPv6ManagerEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snmpIPv4IPv6ManagerEngineID.setStatus("current")
_SnmpIPv4IPv6ManagerRowStatus_Type = RowStatus
_SnmpIPv4IPv6ManagerRowStatus_Object = MibTableColumn
snmpIPv4IPv6ManagerRowStatus = _SnmpIPv4IPv6ManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 1, 1, 5),
    _SnmpIPv4IPv6ManagerRowStatus_Type()
)
snmpIPv4IPv6ManagerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snmpIPv4IPv6ManagerRowStatus.setStatus("current")
_Tp5000eIPv4IPv6RemoteSyslogTable_Object = MibTable
tp5000eIPv4IPv6RemoteSyslogTable = _Tp5000eIPv4IPv6RemoteSyslogTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 2)
)
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6RemoteSyslogTable.setStatus("current")
_Tp5000eIPv4IPv6RemoteSyslogEntry_Object = MibTableRow
tp5000eIPv4IPv6RemoteSyslogEntry = _Tp5000eIPv4IPv6RemoteSyslogEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 2, 1)
)
tp5000eIPv4IPv6RemoteSyslogEntry.setIndexNames(
    (0, "TP5000E", "tp5000eIPv4IPv6RemoteSyslogIndex"),
)
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6RemoteSyslogEntry.setStatus("current")


class _Tp5000eIPv4IPv6RemoteSyslogIndex_Type(Integer32):
    """Custom type tp5000eIPv4IPv6RemoteSyslogIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_Tp5000eIPv4IPv6RemoteSyslogIndex_Type.__name__ = "Integer32"
_Tp5000eIPv4IPv6RemoteSyslogIndex_Object = MibTableColumn
tp5000eIPv4IPv6RemoteSyslogIndex = _Tp5000eIPv4IPv6RemoteSyslogIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 2, 1, 1),
    _Tp5000eIPv4IPv6RemoteSyslogIndex_Type()
)
tp5000eIPv4IPv6RemoteSyslogIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6RemoteSyslogIndex.setStatus("current")


class _Tp5000eIPv4IPv6RemoteSyslogState_Type(EnableValue):
    """Custom type tp5000eIPv4IPv6RemoteSyslogState based on EnableValue"""
    defaultValue = 2


_Tp5000eIPv4IPv6RemoteSyslogState_Object = MibTableColumn
tp5000eIPv4IPv6RemoteSyslogState = _Tp5000eIPv4IPv6RemoteSyslogState_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 2, 1, 2),
    _Tp5000eIPv4IPv6RemoteSyslogState_Type()
)
tp5000eIPv4IPv6RemoteSyslogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6RemoteSyslogState.setStatus("current")
_Tp5000eIPv4IPv6RemoteSyslogAddr_Type = DisplayString
_Tp5000eIPv4IPv6RemoteSyslogAddr_Object = MibTableColumn
tp5000eIPv4IPv6RemoteSyslogAddr = _Tp5000eIPv4IPv6RemoteSyslogAddr_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 2, 1, 3),
    _Tp5000eIPv4IPv6RemoteSyslogAddr_Type()
)
tp5000eIPv4IPv6RemoteSyslogAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6RemoteSyslogAddr.setStatus("current")
_Tp5000eIPv4IPv6AuthRADIUSTable_Object = MibTable
tp5000eIPv4IPv6AuthRADIUSTable = _Tp5000eIPv4IPv6AuthRADIUSTable_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 3)
)
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6AuthRADIUSTable.setStatus("current")
_Tp5000eIPv4IPv6AuthRADIUSEntry_Object = MibTableRow
tp5000eIPv4IPv6AuthRADIUSEntry = _Tp5000eIPv4IPv6AuthRADIUSEntry_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 3, 1)
)
tp5000eIPv4IPv6AuthRADIUSEntry.setIndexNames(
    (0, "TP5000E", "tp5000eIPv4IPv6AuthRADIUSIndex"),
)
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6AuthRADIUSEntry.setStatus("current")


class _Tp5000eIPv4IPv6AuthRADIUSIndex_Type(Integer32):
    """Custom type tp5000eIPv4IPv6AuthRADIUSIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_Tp5000eIPv4IPv6AuthRADIUSIndex_Type.__name__ = "Integer32"
_Tp5000eIPv4IPv6AuthRADIUSIndex_Object = MibTableColumn
tp5000eIPv4IPv6AuthRADIUSIndex = _Tp5000eIPv4IPv6AuthRADIUSIndex_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 3, 1, 1),
    _Tp5000eIPv4IPv6AuthRADIUSIndex_Type()
)
tp5000eIPv4IPv6AuthRADIUSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6AuthRADIUSIndex.setStatus("current")
_Tp5000eIPv4IPv6ServerRADIUSIPAddress_Type = DisplayString
_Tp5000eIPv4IPv6ServerRADIUSIPAddress_Object = MibTableColumn
tp5000eIPv4IPv6ServerRADIUSIPAddress = _Tp5000eIPv4IPv6ServerRADIUSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 3, 1, 2),
    _Tp5000eIPv4IPv6ServerRADIUSIPAddress_Type()
)
tp5000eIPv4IPv6ServerRADIUSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6ServerRADIUSIPAddress.setStatus("current")
_Tp5000eIPv4IPv6AuthRADIUSKey_Type = DisplayString
_Tp5000eIPv4IPv6AuthRADIUSKey_Object = MibTableColumn
tp5000eIPv4IPv6AuthRADIUSKey = _Tp5000eIPv4IPv6AuthRADIUSKey_Object(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 12, 3, 1, 3),
    _Tp5000eIPv4IPv6AuthRADIUSKey_Type()
)
tp5000eIPv4IPv6AuthRADIUSKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6AuthRADIUSKey.setStatus("current")
_Tp5000eConformance_ObjectIdentity = ObjectIdentity
tp5000eConformance = _Tp5000eConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13)
)
if mibBuilder.loadTexts:
    tp5000eConformance.setStatus("current")
_Tp5000eCompliances_ObjectIdentity = ObjectIdentity
tp5000eCompliances = _Tp5000eCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 1)
)
_Tp5000eUocGroups_ObjectIdentity = ObjectIdentity
tp5000eUocGroups = _Tp5000eUocGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2)
)

# Managed Objects groups

tp5000eLEDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 1)
)
tp5000eLEDGroup.setObjects(
      *(("TP5000E", "tp5000eLedID"),
        ("TP5000E", "tp5000eLedStatus"))
)
if mibBuilder.loadTexts:
    tp5000eLEDGroup.setStatus("current")

tp5000eHWGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 2)
)
tp5000eHWGroup.setObjects(
    ("TP5000E", "tp5000eHWStatusInfo")
)
if mibBuilder.loadTexts:
    tp5000eHWGroup.setStatus("current")

tp5000eModeUpTimeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 3)
)
tp5000eModeUpTimeGroup.setObjects(
    ("TP5000E", "tp5000eModuleUpTime")
)
if mibBuilder.loadTexts:
    tp5000eModeUpTimeGroup.setStatus("current")

tp5000eModWarmUpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 4)
)
tp5000eModWarmUpGroup.setObjects(
    ("TP5000E", "tp5000eModWarmUpStatus")
)
if mibBuilder.loadTexts:
    tp5000eModWarmUpGroup.setStatus("current")

tp5000eModStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 5)
)
tp5000eModStatusGroup.setObjects(
    ("TP5000E", "tp5000eModStatusInfo")
)
if mibBuilder.loadTexts:
    tp5000eModStatusGroup.setStatus("current")

tp5000eActiveAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 6)
)
tp5000eActiveAlarmGroup.setObjects(
      *(("TP5000E", "tp5000eActAlarmIndex"),
        ("TP5000E", "tp5000eActAlarmModID"),
        ("TP5000E", "tp5000eActAlarmID"),
        ("TP5000E", "tp5000eActAlarmDateTime"),
        ("TP5000E", "tp5000eActAlarmSeverity"),
        ("TP5000E", "tp5000eActAlarmDesc"),
        ("TP5000E", "tp5000eActAlarmInternalIndex"))
)
if mibBuilder.loadTexts:
    tp5000eActiveAlarmGroup.setStatus("current")

tp5000eActiveEventGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 7)
)
tp5000eActiveEventGroup.setObjects(
      *(("TP5000E", "tp5000eActEventIndex"),
        ("TP5000E", "tp5000eActEventModID"),
        ("TP5000E", "tp5000eActEventID"),
        ("TP5000E", "tp5000eActEventInternlIndex"),
        ("TP5000E", "tp5000eActEventDateTime"),
        ("TP5000E", "tp5000eActEventDesc"))
)
if mibBuilder.loadTexts:
    tp5000eActiveEventGroup.setStatus("current")

tp5000eAlarmConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 8)
)
tp5000eAlarmConfigGroup.setObjects(
      *(("TP5000E", "tp5000eAlarmConfigIndex"),
        ("TP5000E", "tp5000eAlarmConfigAID"),
        ("TP5000E", "tp5000eAlarmLevelSetting"),
        ("TP5000E", "tp5000eAlarmSettingDelay"),
        ("TP5000E", "tp5000eEnableAlarmState"),
        ("TP5000E", "tp5000eAlarmConfigDesc"))
)
if mibBuilder.loadTexts:
    tp5000eAlarmConfigGroup.setStatus("current")

tp5000eGeneralAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 9)
)
tp5000eGeneralAlarmGroup.setObjects(
      *(("TP5000E", "tp5000eNumofStandingAlarm"),
        ("TP5000E", "tp5000eMessageGenerate"))
)
if mibBuilder.loadTexts:
    tp5000eGeneralAlarmGroup.setStatus("current")

tp5000eLogFileConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 10)
)
tp5000eLogFileConfigGroup.setObjects(
      *(("TP5000E", "tp5000eLogFileConfigIndex"),
        ("TP5000E", "tp5000eLogFileTypeName"),
        ("TP5000E", "tp5000eLogFileBufferSize"))
)
if mibBuilder.loadTexts:
    tp5000eLogFileConfigGroup.setStatus("current")

tp5000eRemoteSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 11)
)
tp5000eRemoteSyslogGroup.setObjects(
      *(("TP5000E", "tp5000eRemoteSyslogIndex"),
        ("TP5000E", "tp5000eRemoteSyslogState"),
        ("TP5000E", "tp5000eRemoteSyslogAddr"))
)
if mibBuilder.loadTexts:
    tp5000eRemoteSyslogGroup.setStatus("current")

tp5000eRedundGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 12)
)
tp5000eRedundGroup.setObjects(
      *(("TP5000E", "tp5000eRedundModuleID"),
        ("TP5000E", "tp5000eRedundModState"),
        ("TP5000E", "tp5000eRedundActivePort"))
)
if mibBuilder.loadTexts:
    tp5000eRedundGroup.setStatus("current")

tp5000eImageGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 13)
)
tp5000eImageGroup.setObjects(
      *(("TP5000E", "tp5000eImageID"),
        ("TP5000E", "tp5000eImageNextBoot"),
        ("TP5000E", "tp5000eImageCurrState"),
        ("TP5000E", "tp5000eImageInfoMsg"))
)
if mibBuilder.loadTexts:
    tp5000eImageGroup.setStatus("current")

tp5000eRebootGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 15)
)
tp5000eRebootGroup.setObjects(
    ("TP5000E", "tp5000eRebootAction")
)
if mibBuilder.loadTexts:
    tp5000eRebootGroup.setStatus("current")

tp5000eRadiusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 16)
)
tp5000eRadiusGroup.setObjects(
      *(("TP5000E", "tp5000eAuthRADIUSIndex"),
        ("TP5000E", "tp5000eServerRADIUSIPAddress"),
        ("TP5000E", "tp5000eAuthRADIUSKey"),
        ("TP5000E", "tp5000eRadiusState"))
)
if mibBuilder.loadTexts:
    tp5000eRadiusGroup.setStatus("current")

tp5000eAssetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 17)
)
tp5000eAssetGroup.setObjects(
      *(("TP5000E", "tp5000eAssetNum"),
        ("TP5000E", "tp5000eIntraCommIPSet"),
        ("TP5000E", "tp5000eSSMOption"))
)
if mibBuilder.loadTexts:
    tp5000eAssetGroup.setStatus("current")

tp5000ePacketServiceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 18)
)
tp5000ePacketServiceGroup.setObjects(
      *(("TP5000E", "tp5000ePacketServiceMode"),
        ("TP5000E", "tp5000ePTPClientDataTableLock"),
        ("TP5000E", "tp5000ePacketServiceExtendedMode"))
)
if mibBuilder.loadTexts:
    tp5000ePacketServiceGroup.setStatus("current")

tp5000eReferenceStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 19)
)
tp5000eReferenceStatusGroup.setObjects(
      *(("TP5000E", "tp5000eInputRefName"),
        ("TP5000E", "tp5000eInputRefActualPQL"),
        ("TP5000E", "tp5000eInputRefQualified"))
)
if mibBuilder.loadTexts:
    tp5000eReferenceStatusGroup.setStatus("current")

tp5000eReferenceConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 20)
)
tp5000eReferenceConfigGroup.setObjects(
      *(("TP5000E", "tp5000eRefTimingMode"),
        ("TP5000E", "tp5000eRefSelectionCriteria"),
        ("TP5000E", "tp5000eRefName"),
        ("TP5000E", "tp5000eRefState"),
        ("TP5000E", "tp5000eRefPriority"),
        ("TP5000E", "tp5000eRefPQLState"),
        ("TP5000E", "tp5000eRefPQL"))
)
if mibBuilder.loadTexts:
    tp5000eReferenceConfigGroup.setStatus("current")

tp5000eClockStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 21)
)
tp5000eClockStatusGroup.setObjects(
      *(("TP5000E", "tp5000ePhaseOffset"),
        ("TP5000E", "tp5000eServoControlStatus"))
)
if mibBuilder.loadTexts:
    tp5000eClockStatusGroup.setStatus("current")

tp5000eClockConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 22)
)
tp5000eClockConfigGroup.setObjects(
      *(("TP5000E", "tp5000eBridgingTime"),
        ("TP5000E", "tp5000eAutoSync"),
        ("TP5000E", "tp5000eSync"),
        ("TP5000E", "tp5000eHoldoverExceededTimeQz"),
        ("TP5000E", "tp5000eHoldoverExceededTimeRb"))
)
if mibBuilder.loadTexts:
    tp5000eClockConfigGroup.setStatus("current")

tp5000eModuleIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 23)
)
tp5000eModuleIfGroup.setObjects(
      *(("TP5000E", "tp5000eIfIndex"),
        ("TP5000E", "tp5000eIfModuleID"),
        ("TP5000E", "tp5000eIfPortID"),
        ("TP5000E", "tp5000eIfTableIndex"))
)
if mibBuilder.loadTexts:
    tp5000eModuleIfGroup.setStatus("current")

tp5000eModuleEntityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 24)
)
tp5000eModuleEntityGroup.setObjects(
      *(("TP5000E", "tp5000eEntPhysicalIndex"),
        ("TP5000E", "tp5000eEntPhysicalModuleID"),
        ("TP5000E", "tp5000eEntPhysicalStackID"),
        ("TP5000E", "tp5000eEntPhysicalChassisID"),
        ("TP5000E", "tp5000eEntPhysicalPartIndex"),
        ("TP5000E", "tp5000eEntPhysicalTableIndex"))
)
if mibBuilder.loadTexts:
    tp5000eModuleEntityGroup.setStatus("current")

tp5000eFixedVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 25)
)
tp5000eFixedVlanGroup.setObjects(
      *(("TP5000E", "tp5000eFixedVlanId"),
        ("TP5000E", "tp5000eFixedVlanPriority"),
        ("TP5000E", "tp5000eFixedVlanIPv4Addr"),
        ("TP5000E", "tp5000eFixedVlanNetmask"),
        ("TP5000E", "tp5000eFixedVlanGateway"),
        ("TP5000E", "tp5000eFixedVlanState"))
)
if mibBuilder.loadTexts:
    tp5000eFixedVlanGroup.setStatus("current")

tp5000eNonfixedVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 26)
)
tp5000eNonfixedVlanGroup.setObjects(
      *(("TP5000E", "tp5000eNonfixedVlanIfIndex"),
        ("TP5000E", "tp5000eNonfixedVlanModuleID"),
        ("TP5000E", "tp5000eNonfixedVlanPortID"),
        ("TP5000E", "tp5000eNonfixedVlanId"),
        ("TP5000E", "tp5000eNonfixedVlanPriority"),
        ("TP5000E", "tp5000eNonfixedVlanIPv4Addr"),
        ("TP5000E", "tp5000eNonfixedVlanNetmask"),
        ("TP5000E", "tp5000eNonfixedVlanRowStatus"),
        ("TP5000E", "tp5000eNonfixedVlanState"))
)
if mibBuilder.loadTexts:
    tp5000eNonfixedVlanGroup.setStatus("current")

tp5000eNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 27)
)
tp5000eNotifyGroup.setObjects(
      *(("TP5000E", "tp5000eNotifyModuleId"),
        ("TP5000E", "tp5000eNotifyAlarmEventID"),
        ("TP5000E", "tp5000eNotifyIndex"),
        ("TP5000E", "tp5000eNotifySeverity"),
        ("TP5000E", "tp5000eNotifyTransient"),
        ("TP5000E", "tp5000eNotifyDateTime"),
        ("TP5000E", "tp5000eNotifyDescription"),
        ("TP5000E", "tp5000eNotifyClientAddr"),
        ("TP5000E", "tp5000eNotifySequenceNum"),
        ("TP5000E", "tp5000eNotifyClientClockID"))
)
if mibBuilder.loadTexts:
    tp5000eNotifyGroup.setStatus("current")

tp5000eVlanModeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 29)
)
tp5000eVlanModeGroup.setObjects(
      *(("TP5000E", "tp5000eVlanModeModuleID"),
        ("TP5000E", "tp5000eVlanModeValue"),
        ("TP5000E", "tp5000eVlanModePortID"))
)
if mibBuilder.loadTexts:
    tp5000eVlanModeGroup.setStatus("current")

tp5000eLastConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 30)
)
tp5000eLastConfigGroup.setObjects(
    ("TP5000E", "tp5000eLastConfig")
)
if mibBuilder.loadTexts:
    tp5000eLastConfigGroup.setStatus("current")

tp5000eIPv6NonfixedVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 31)
)
tp5000eIPv6NonfixedVlanGroup.setObjects(
      *(("TP5000E", "tp5000eIPv6NonfixedVlanIfIndex"),
        ("TP5000E", "tp5000eIPv6NonfixedVlanModuleID"),
        ("TP5000E", "tp5000eIPv6NonfixedVlanPortID"),
        ("TP5000E", "tp5000eIPv6NonfixedVlanId"),
        ("TP5000E", "tp5000eIPv6NonfixedVlanPriority"),
        ("TP5000E", "tp5000eIPv6NonfixedVlanAddr"),
        ("TP5000E", "tp5000eIPv6NonfixedVlanPrefix"),
        ("TP5000E", "tp5000eIPv6NonfixedVlanState"),
        ("TP5000E", "tp5000eIPv6NonfixedVlanRowStatus"))
)
if mibBuilder.loadTexts:
    tp5000eIPv6NonfixedVlanGroup.setStatus("current")

tp5000eIPv6FixedVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 32)
)
tp5000eIPv6FixedVlanGroup.setObjects(
      *(("TP5000E", "tp5000eIPv6FixedVlanId"),
        ("TP5000E", "tp5000eIPv6FixedVlanPriority"),
        ("TP5000E", "tp5000eIPv6FixedVlanAddr"),
        ("TP5000E", "tp5000eIPv6FixedVlanPrefix"),
        ("TP5000E", "tp5000eIPv6FixedVlanDefaultRouter"),
        ("TP5000E", "tp5000eIPv6FixedVlanState"))
)
if mibBuilder.loadTexts:
    tp5000eIPv6FixedVlanGroup.setStatus("current")

tp5000eIPv4IPv6SnmpManagerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 33)
)
tp5000eIPv4IPv6SnmpManagerGroup.setObjects(
      *(("TP5000E", "snmpIPv4IPv6ManagerID"),
        ("TP5000E", "snmpIPv4IPv6ManagerAddress"),
        ("TP5000E", "snmpIPv4IPv6ManagerEngineID"))
)
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6SnmpManagerGroup.setStatus("current")

tp5000eIPv4IPv6RemoteSyslogGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 34)
)
tp5000eIPv4IPv6RemoteSyslogGroup.setObjects(
      *(("TP5000E", "tp5000eIPv4IPv6RemoteSyslogState"),
        ("TP5000E", "tp5000eIPv4IPv6RemoteSyslogAddr"))
)
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6RemoteSyslogGroup.setStatus("current")

tp5000eIPv4IPv6AuthRADIUSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 35)
)
tp5000eIPv4IPv6AuthRADIUSGroup.setObjects(
      *(("TP5000E", "tp5000eIPv4IPv6ServerRADIUSIPAddress"),
        ("TP5000E", "tp5000eIPv4IPv6AuthRADIUSKey"))
)
if mibBuilder.loadTexts:
    tp5000eIPv4IPv6AuthRADIUSGroup.setStatus("current")


# Notification objects

tp5000eTrapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 2)
)
tp5000eTrapAlarm.setObjects(
      *(("TP5000E", "tp5000eNotifyModuleId"),
        ("TP5000E", "tp5000eNotifyAlarmEventID"),
        ("TP5000E", "tp5000eNotifyIndex"),
        ("TP5000E", "tp5000eNotifySeverity"),
        ("TP5000E", "tp5000eNotifyTransient"),
        ("TP5000E", "tp5000eNotifyDateTime"),
        ("TP5000E", "tp5000eNotifyDescription"),
        ("TP5000E", "tp5000eNotifySequenceNum"))
)
if mibBuilder.loadTexts:
    tp5000eTrapAlarm.setStatus(
        "current"
    )

tp5000eTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 3)
)
tp5000eTrapEvent.setObjects(
      *(("TP5000E", "tp5000eNotifyModuleId"),
        ("TP5000E", "tp5000eNotifyAlarmEventID"),
        ("TP5000E", "tp5000eNotifyIndex"),
        ("TP5000E", "tp5000eNotifySeverity"),
        ("TP5000E", "tp5000eNotifyTransient"),
        ("TP5000E", "tp5000eNotifyDateTime"),
        ("TP5000E", "tp5000eNotifyDescription"),
        ("TP5000E", "tp5000eNotifySequenceNum"))
)
if mibBuilder.loadTexts:
    tp5000eTrapEvent.setStatus(
        "current"
    )

tp5000eClientNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 4)
)
tp5000eClientNotification.setObjects(
      *(("TP5000E", "tp5000eNotifyModuleId"),
        ("TP5000E", "tp5000eNotifyAlarmEventID"),
        ("TP5000E", "tp5000eNotifyIndex"),
        ("TP5000E", "tp5000eNotifySeverity"),
        ("TP5000E", "tp5000eNotifyTransient"),
        ("TP5000E", "tp5000eNotifyDateTime"),
        ("TP5000E", "tp5000eNotifyDescription"),
        ("TP5000E", "tp5000eNotifyClientAddr"),
        ("TP5000E", "tp5000eNotifySequenceNum"))
)
if mibBuilder.loadTexts:
    tp5000eClientNotification.setStatus(
        "current"
    )

tp5000ePtpMgmtEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 11, 5)
)
tp5000ePtpMgmtEvent.setObjects(
      *(("TP5000E", "tp5000eNotifyModuleId"),
        ("TP5000E", "tp5000eNotifyAlarmEventID"),
        ("TP5000E", "tp5000eNotifyIndex"),
        ("TP5000E", "tp5000eNotifySeverity"),
        ("TP5000E", "tp5000eNotifyTransient"),
        ("TP5000E", "tp5000eNotifyDateTime"),
        ("TP5000E", "tp5000eNotifyDescription"),
        ("TP5000E", "tp5000eNotifyClientClockID"),
        ("TP5000E", "tp5000eNotifySequenceNum"))
)
if mibBuilder.loadTexts:
    tp5000ePtpMgmtEvent.setStatus(
        "current"
    )


# Notifications groups

tp5000eNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 2, 28)
)
tp5000eNotificationGroup.setObjects(
      *(("TP5000E", "tp5000eTrapAlarm"),
        ("TP5000E", "tp5000eTrapEvent"),
        ("TP5000E", "tp5000eClientNotification"),
        ("TP5000E", "tp5000ePtpMgmtEvent"))
)
if mibBuilder.loadTexts:
    tp5000eNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tp5000eBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9070, 1, 2, 5, 7, 1, 13, 1, 1)
)
if mibBuilder.loadTexts:
    tp5000eBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TP5000E",
    **{"TP5000LEDID": TP5000LEDID,
       "TP5000LEDTYPE": TP5000LEDTYPE,
       "ALARMLEVELTYPE": ALARMLEVELTYPE,
       "TP5000IOCPORTID": TP5000IOCPORTID,
       "TP5000IMAGEACTIVE": TP5000IMAGEACTIVE,
       "TP5000INTRAIPSET": TP5000INTRAIPSET,
       "TP5000PACKETSERVICE": TP5000PACKETSERVICE,
       "TP5000SSMOPTION": TP5000SSMOPTION,
       "TP5000REFQUALIFICATION": TP5000REFQUALIFICATION,
       "TP5000REFTIMINGMODE": TP5000REFTIMINGMODE,
       "TP5000REFSELECTMODE": TP5000REFSELECTMODE,
       "TP5000SERVOCTL": TP5000SERVOCTL,
       "TP5000TRANSIENT": TP5000TRANSIENT,
       "TP5000IOPORTID": TP5000IOPORTID,
       "TP5000IOTYPE": TP5000IOTYPE,
       "TP5000SSMVALUE": TP5000SSMVALUE,
       "DateAndTime": DateAndTime,
       "TLatAndLon": TLatAndLon,
       "TAntHeight": TAntHeight,
       "TLocalTimeOffset": TLocalTimeOffset,
       "TSsm": TSsm,
       "tp5000e": tp5000e,
       "tp5000eSystemStatus": tp5000eSystemStatus,
       "tp5000eLedTable": tp5000eLedTable,
       "tp5000eLedEntry": tp5000eLedEntry,
       "tp5000eLedID": tp5000eLedID,
       "tp5000eLedStatus": tp5000eLedStatus,
       "tp5000eHWStatusTable": tp5000eHWStatusTable,
       "tp5000eHWStatusEntry": tp5000eHWStatusEntry,
       "tp5000eHWStatusIndex": tp5000eHWStatusIndex,
       "tp5000eHWStatusInfo": tp5000eHWStatusInfo,
       "tp5000eModUpTimeTable": tp5000eModUpTimeTable,
       "tp5000eModUpTimeEntry": tp5000eModUpTimeEntry,
       "tp5000eModUpTimeIndex": tp5000eModUpTimeIndex,
       "tp5000eModuleUpTime": tp5000eModuleUpTime,
       "tp5000eModWarmUpTable": tp5000eModWarmUpTable,
       "tp5000eModWarmUpEntry": tp5000eModWarmUpEntry,
       "tp5000eModWarmUpIndex": tp5000eModWarmUpIndex,
       "tp5000eModWarmUpStatus": tp5000eModWarmUpStatus,
       "tp5000eModStatusTable": tp5000eModStatusTable,
       "tp5000eModStatusEntry": tp5000eModStatusEntry,
       "tp5000eModStatusIndex": tp5000eModStatusIndex,
       "tp5000eModStatusInfo": tp5000eModStatusInfo,
       "tp5000eAlarmAndEvent": tp5000eAlarmAndEvent,
       "tp5000eActAlarmTable": tp5000eActAlarmTable,
       "tp5000eActAlarmEntry": tp5000eActAlarmEntry,
       "tp5000eActAlarmIndex": tp5000eActAlarmIndex,
       "tp5000eActAlarmModID": tp5000eActAlarmModID,
       "tp5000eActAlarmID": tp5000eActAlarmID,
       "tp5000eActAlarmInternalIndex": tp5000eActAlarmInternalIndex,
       "tp5000eActAlarmDateTime": tp5000eActAlarmDateTime,
       "tp5000eActAlarmSeverity": tp5000eActAlarmSeverity,
       "tp5000eActAlarmDesc": tp5000eActAlarmDesc,
       "tp5000eActEventTable": tp5000eActEventTable,
       "tp5000eActEventEntry": tp5000eActEventEntry,
       "tp5000eActEventIndex": tp5000eActEventIndex,
       "tp5000eActEventModID": tp5000eActEventModID,
       "tp5000eActEventID": tp5000eActEventID,
       "tp5000eActEventInternlIndex": tp5000eActEventInternlIndex,
       "tp5000eActEventDateTime": tp5000eActEventDateTime,
       "tp5000eActEventDesc": tp5000eActEventDesc,
       "tp5000eAlarmConfigTable": tp5000eAlarmConfigTable,
       "tp5000eAlarmConfigEntry": tp5000eAlarmConfigEntry,
       "tp5000eAlarmConfigIndex": tp5000eAlarmConfigIndex,
       "tp5000eAlarmConfigAID": tp5000eAlarmConfigAID,
       "tp5000eAlarmLevelSetting": tp5000eAlarmLevelSetting,
       "tp5000eAlarmSettingDelay": tp5000eAlarmSettingDelay,
       "tp5000eEnableAlarmState": tp5000eEnableAlarmState,
       "tp5000eAlarmConfigDesc": tp5000eAlarmConfigDesc,
       "tp5000eNumofStandingAlarm": tp5000eNumofStandingAlarm,
       "tp5000eMessageGenerate": tp5000eMessageGenerate,
       "tp5000eGlobalConfig": tp5000eGlobalConfig,
       "tp5000eLogFileConfigTable": tp5000eLogFileConfigTable,
       "tp5000eLogFileConfigEntry": tp5000eLogFileConfigEntry,
       "tp5000eLogFileConfigIndex": tp5000eLogFileConfigIndex,
       "tp5000eLogFileTypeName": tp5000eLogFileTypeName,
       "tp5000eLogFileBufferSize": tp5000eLogFileBufferSize,
       "tp5000eRemoteSyslogTable": tp5000eRemoteSyslogTable,
       "tp5000eRemoteSyslogEntry": tp5000eRemoteSyslogEntry,
       "tp5000eRemoteSyslogIndex": tp5000eRemoteSyslogIndex,
       "tp5000eRemoteSyslogState": tp5000eRemoteSyslogState,
       "tp5000eRemoteSyslogAddr": tp5000eRemoteSyslogAddr,
       "tp5000eRedundTable": tp5000eRedundTable,
       "tp5000eRedundEntry": tp5000eRedundEntry,
       "tp5000eRedundModuleID": tp5000eRedundModuleID,
       "tp5000eRedundModState": tp5000eRedundModState,
       "tp5000eRedundActivePort": tp5000eRedundActivePort,
       "tp5000eImageTable": tp5000eImageTable,
       "tp5000eImageEntry": tp5000eImageEntry,
       "tp5000eImageIndex": tp5000eImageIndex,
       "tp5000eImageNextBoot": tp5000eImageNextBoot,
       "tp5000eImageID": tp5000eImageID,
       "tp5000eImageCurrState": tp5000eImageCurrState,
       "tp5000eImageInfoMsg": tp5000eImageInfoMsg,
       "tp5000eRebootTable": tp5000eRebootTable,
       "tp5000eRebootEntry": tp5000eRebootEntry,
       "tp5000eRebootIndex": tp5000eRebootIndex,
       "tp5000eRebootAction": tp5000eRebootAction,
       "tp5000eAuthRADIUSTable": tp5000eAuthRADIUSTable,
       "tp5000eAuthRADIUSEntry": tp5000eAuthRADIUSEntry,
       "tp5000eAuthRADIUSIndex": tp5000eAuthRADIUSIndex,
       "tp5000eServerRADIUSIPAddress": tp5000eServerRADIUSIPAddress,
       "tp5000eAuthRADIUSKey": tp5000eAuthRADIUSKey,
       "tp5000eAssetNum": tp5000eAssetNum,
       "tp5000eIntraCommIPSet": tp5000eIntraCommIPSet,
       "tp5000eRadiusState": tp5000eRadiusState,
       "tp5000eLastConfig": tp5000eLastConfig,
       "tp5000eGlobalService": tp5000eGlobalService,
       "tp5000ePacketServiceTable": tp5000ePacketServiceTable,
       "tp5000ePacketServiceEntry": tp5000ePacketServiceEntry,
       "tp5000ePacketServiceIndex": tp5000ePacketServiceIndex,
       "tp5000ePacketServiceMode": tp5000ePacketServiceMode,
       "tp5000eSSMOptionTable": tp5000eSSMOptionTable,
       "tp5000eSSMOptionEntry": tp5000eSSMOptionEntry,
       "tp5000eSSMOptionIndex": tp5000eSSMOptionIndex,
       "tp5000eSSMOption": tp5000eSSMOption,
       "tp5000ePTPClientDataTableLock": tp5000ePTPClientDataTableLock,
       "tp5000ePacketServiceExtendedMode": tp5000ePacketServiceExtendedMode,
       "tp5000ePTPClientMgmt": tp5000ePTPClientMgmt,
       "tp5000eReferenceStatus": tp5000eReferenceStatus,
       "tp5000eInputPQLTable": tp5000eInputPQLTable,
       "tp5000eInputPQLEntry": tp5000eInputPQLEntry,
       "tp5000eInputRefName": tp5000eInputRefName,
       "tp5000eInputRefActualPQL": tp5000eInputRefActualPQL,
       "tp5000eInputRefQualified": tp5000eInputRefQualified,
       "tp5000eSymmMetrics": tp5000eSymmMetrics,
       "tp5000eRefConfig": tp5000eRefConfig,
       "tp5000eRefTimingMode": tp5000eRefTimingMode,
       "tp5000eRefSelectionCriteria": tp5000eRefSelectionCriteria,
       "tp5000eRefConfigTable": tp5000eRefConfigTable,
       "tp5000eRefConfigEntry": tp5000eRefConfigEntry,
       "tp5000eRefName": tp5000eRefName,
       "tp5000eRefState": tp5000eRefState,
       "tp5000eRefPriority": tp5000eRefPriority,
       "tp5000eRefPQLState": tp5000eRefPQLState,
       "tp5000eRefPQL": tp5000eRefPQL,
       "tp5000eClock": tp5000eClock,
       "tp5000eClockStatus": tp5000eClockStatus,
       "tp5000eClockStatusTable": tp5000eClockStatusTable,
       "tp5000eClockStatusEntry": tp5000eClockStatusEntry,
       "tp5000eClockStatusIndex": tp5000eClockStatusIndex,
       "tp5000eServoControlStatus": tp5000eServoControlStatus,
       "tp5000ePhaseOffset": tp5000ePhaseOffset,
       "tp5000eClockConfig": tp5000eClockConfig,
       "tp5000eBridgingTime": tp5000eBridgingTime,
       "tp5000eAutoSync": tp5000eAutoSync,
       "tp5000eSync": tp5000eSync,
       "tp5000eHoldoverExceededTimeQz": tp5000eHoldoverExceededTimeQz,
       "tp5000eHoldoverExceededTimeRb": tp5000eHoldoverExceededTimeRb,
       "tp5000eHardwareHierarchy": tp5000eHardwareHierarchy,
       "tp5000eIfTable": tp5000eIfTable,
       "tp5000eIfEntry": tp5000eIfEntry,
       "tp5000eIfIndex": tp5000eIfIndex,
       "tp5000eIfModuleID": tp5000eIfModuleID,
       "tp5000eIfPortID": tp5000eIfPortID,
       "tp5000eIfTableIndex": tp5000eIfTableIndex,
       "tp5000eEntPhysicalTable": tp5000eEntPhysicalTable,
       "tp5000eEntPhysicalEntry": tp5000eEntPhysicalEntry,
       "tp5000eEntPhysicalIndex": tp5000eEntPhysicalIndex,
       "tp5000eEntPhysicalModuleID": tp5000eEntPhysicalModuleID,
       "tp5000eEntPhysicalStackID": tp5000eEntPhysicalStackID,
       "tp5000eEntPhysicalChassisID": tp5000eEntPhysicalChassisID,
       "tp5000eEntPhysicalPartIndex": tp5000eEntPhysicalPartIndex,
       "tp5000eEntPhysicalTableIndex": tp5000eEntPhysicalTableIndex,
       "tp5000eVlanConfig": tp5000eVlanConfig,
       "tp5000eNonfixedVlanTable": tp5000eNonfixedVlanTable,
       "tp5000eNonfixedVlanEntry": tp5000eNonfixedVlanEntry,
       "tp5000eNonfixedVlanIndex": tp5000eNonfixedVlanIndex,
       "tp5000eNonfixedVlanIfIndex": tp5000eNonfixedVlanIfIndex,
       "tp5000eNonfixedVlanModuleID": tp5000eNonfixedVlanModuleID,
       "tp5000eNonfixedVlanPortID": tp5000eNonfixedVlanPortID,
       "tp5000eNonfixedVlanId": tp5000eNonfixedVlanId,
       "tp5000eNonfixedVlanPriority": tp5000eNonfixedVlanPriority,
       "tp5000eNonfixedVlanIPv4Addr": tp5000eNonfixedVlanIPv4Addr,
       "tp5000eNonfixedVlanNetmask": tp5000eNonfixedVlanNetmask,
       "tp5000eNonfixedVlanState": tp5000eNonfixedVlanState,
       "tp5000eNonfixedVlanRowStatus": tp5000eNonfixedVlanRowStatus,
       "tp5000eFixedVlanTable": tp5000eFixedVlanTable,
       "tp5000eFixedVlanEntry": tp5000eFixedVlanEntry,
       "tp5000eFixedVlanIndex": tp5000eFixedVlanIndex,
       "tp5000eFixedVlanId": tp5000eFixedVlanId,
       "tp5000eFixedVlanPriority": tp5000eFixedVlanPriority,
       "tp5000eFixedVlanIPv4Addr": tp5000eFixedVlanIPv4Addr,
       "tp5000eFixedVlanNetmask": tp5000eFixedVlanNetmask,
       "tp5000eFixedVlanGateway": tp5000eFixedVlanGateway,
       "tp5000eFixedVlanState": tp5000eFixedVlanState,
       "tp5000eVlanModeTable": tp5000eVlanModeTable,
       "tp5000eVlanModeEntry": tp5000eVlanModeEntry,
       "tp5000eVlanModeIndex": tp5000eVlanModeIndex,
       "tp5000eVlanModeModuleID": tp5000eVlanModeModuleID,
       "tp5000eVlanModePortID": tp5000eVlanModePortID,
       "tp5000eVlanModeValue": tp5000eVlanModeValue,
       "tp5000eIPv6NonfixedVlanTable": tp5000eIPv6NonfixedVlanTable,
       "tp5000eIPv6NonfixedVlanEntry": tp5000eIPv6NonfixedVlanEntry,
       "tp5000eIPv6NonfixedVlanIndex": tp5000eIPv6NonfixedVlanIndex,
       "tp5000eIPv6NonfixedVlanIfIndex": tp5000eIPv6NonfixedVlanIfIndex,
       "tp5000eIPv6NonfixedVlanModuleID": tp5000eIPv6NonfixedVlanModuleID,
       "tp5000eIPv6NonfixedVlanPortID": tp5000eIPv6NonfixedVlanPortID,
       "tp5000eIPv6NonfixedVlanId": tp5000eIPv6NonfixedVlanId,
       "tp5000eIPv6NonfixedVlanPriority": tp5000eIPv6NonfixedVlanPriority,
       "tp5000eIPv6NonfixedVlanAddr": tp5000eIPv6NonfixedVlanAddr,
       "tp5000eIPv6NonfixedVlanPrefix": tp5000eIPv6NonfixedVlanPrefix,
       "tp5000eIPv6NonfixedVlanState": tp5000eIPv6NonfixedVlanState,
       "tp5000eIPv6NonfixedVlanRowStatus": tp5000eIPv6NonfixedVlanRowStatus,
       "tp5000eIPv6FixedVlanTable": tp5000eIPv6FixedVlanTable,
       "tp5000eIPv6FixedVlanEntry": tp5000eIPv6FixedVlanEntry,
       "tp5000eIPv6FixedVlanIndex": tp5000eIPv6FixedVlanIndex,
       "tp5000eIPv6FixedVlanId": tp5000eIPv6FixedVlanId,
       "tp5000eIPv6FixedVlanPriority": tp5000eIPv6FixedVlanPriority,
       "tp5000eIPv6FixedVlanAddr": tp5000eIPv6FixedVlanAddr,
       "tp5000eIPv6FixedVlanPrefix": tp5000eIPv6FixedVlanPrefix,
       "tp5000eIPv6FixedVlanDefaultRouter": tp5000eIPv6FixedVlanDefaultRouter,
       "tp5000eIPv6FixedVlanState": tp5000eIPv6FixedVlanState,
       "tp5000eAlarmNotification": tp5000eAlarmNotification,
       "tp5000eNotifyElements": tp5000eNotifyElements,
       "tp5000eNotifyModuleId": tp5000eNotifyModuleId,
       "tp5000eNotifyAlarmEventID": tp5000eNotifyAlarmEventID,
       "tp5000eNotifyIndex": tp5000eNotifyIndex,
       "tp5000eNotifySeverity": tp5000eNotifySeverity,
       "tp5000eNotifyTransient": tp5000eNotifyTransient,
       "tp5000eNotifyDateTime": tp5000eNotifyDateTime,
       "tp5000eNotifyDescription": tp5000eNotifyDescription,
       "tp5000eNotifyClientAddr": tp5000eNotifyClientAddr,
       "tp5000eNotifySequenceNum": tp5000eNotifySequenceNum,
       "tp5000eNotifyClientClockID": tp5000eNotifyClientClockID,
       "tp5000eTrapAlarm": tp5000eTrapAlarm,
       "tp5000eTrapEvent": tp5000eTrapEvent,
       "tp5000eClientNotification": tp5000eClientNotification,
       "tp5000ePtpMgmtEvent": tp5000ePtpMgmtEvent,
       "tp5000eIPv6GlobalConfig": tp5000eIPv6GlobalConfig,
       "snmpIPv4IPv6ManagerTable": snmpIPv4IPv6ManagerTable,
       "snmpIPv4IPv6ManagerEntry": snmpIPv4IPv6ManagerEntry,
       "snmpIPv4IPv6ManagerIndex": snmpIPv4IPv6ManagerIndex,
       "snmpIPv4IPv6ManagerID": snmpIPv4IPv6ManagerID,
       "snmpIPv4IPv6ManagerAddress": snmpIPv4IPv6ManagerAddress,
       "snmpIPv4IPv6ManagerEngineID": snmpIPv4IPv6ManagerEngineID,
       "snmpIPv4IPv6ManagerRowStatus": snmpIPv4IPv6ManagerRowStatus,
       "tp5000eIPv4IPv6RemoteSyslogTable": tp5000eIPv4IPv6RemoteSyslogTable,
       "tp5000eIPv4IPv6RemoteSyslogEntry": tp5000eIPv4IPv6RemoteSyslogEntry,
       "tp5000eIPv4IPv6RemoteSyslogIndex": tp5000eIPv4IPv6RemoteSyslogIndex,
       "tp5000eIPv4IPv6RemoteSyslogState": tp5000eIPv4IPv6RemoteSyslogState,
       "tp5000eIPv4IPv6RemoteSyslogAddr": tp5000eIPv4IPv6RemoteSyslogAddr,
       "tp5000eIPv4IPv6AuthRADIUSTable": tp5000eIPv4IPv6AuthRADIUSTable,
       "tp5000eIPv4IPv6AuthRADIUSEntry": tp5000eIPv4IPv6AuthRADIUSEntry,
       "tp5000eIPv4IPv6AuthRADIUSIndex": tp5000eIPv4IPv6AuthRADIUSIndex,
       "tp5000eIPv4IPv6ServerRADIUSIPAddress": tp5000eIPv4IPv6ServerRADIUSIPAddress,
       "tp5000eIPv4IPv6AuthRADIUSKey": tp5000eIPv4IPv6AuthRADIUSKey,
       "tp5000eConformance": tp5000eConformance,
       "tp5000eCompliances": tp5000eCompliances,
       "tp5000eBasicCompliance": tp5000eBasicCompliance,
       "tp5000eUocGroups": tp5000eUocGroups,
       "tp5000eLEDGroup": tp5000eLEDGroup,
       "tp5000eHWGroup": tp5000eHWGroup,
       "tp5000eModeUpTimeGroup": tp5000eModeUpTimeGroup,
       "tp5000eModWarmUpGroup": tp5000eModWarmUpGroup,
       "tp5000eModStatusGroup": tp5000eModStatusGroup,
       "tp5000eActiveAlarmGroup": tp5000eActiveAlarmGroup,
       "tp5000eActiveEventGroup": tp5000eActiveEventGroup,
       "tp5000eAlarmConfigGroup": tp5000eAlarmConfigGroup,
       "tp5000eGeneralAlarmGroup": tp5000eGeneralAlarmGroup,
       "tp5000eLogFileConfigGroup": tp5000eLogFileConfigGroup,
       "tp5000eRemoteSyslogGroup": tp5000eRemoteSyslogGroup,
       "tp5000eRedundGroup": tp5000eRedundGroup,
       "tp5000eImageGroup": tp5000eImageGroup,
       "tp5000eRebootGroup": tp5000eRebootGroup,
       "tp5000eRadiusGroup": tp5000eRadiusGroup,
       "tp5000eAssetGroup": tp5000eAssetGroup,
       "tp5000ePacketServiceGroup": tp5000ePacketServiceGroup,
       "tp5000eReferenceStatusGroup": tp5000eReferenceStatusGroup,
       "tp5000eReferenceConfigGroup": tp5000eReferenceConfigGroup,
       "tp5000eClockStatusGroup": tp5000eClockStatusGroup,
       "tp5000eClockConfigGroup": tp5000eClockConfigGroup,
       "tp5000eModuleIfGroup": tp5000eModuleIfGroup,
       "tp5000eModuleEntityGroup": tp5000eModuleEntityGroup,
       "tp5000eFixedVlanGroup": tp5000eFixedVlanGroup,
       "tp5000eNonfixedVlanGroup": tp5000eNonfixedVlanGroup,
       "tp5000eNotifyGroup": tp5000eNotifyGroup,
       "tp5000eNotificationGroup": tp5000eNotificationGroup,
       "tp5000eVlanModeGroup": tp5000eVlanModeGroup,
       "tp5000eLastConfigGroup": tp5000eLastConfigGroup,
       "tp5000eIPv6NonfixedVlanGroup": tp5000eIPv6NonfixedVlanGroup,
       "tp5000eIPv6FixedVlanGroup": tp5000eIPv6FixedVlanGroup,
       "tp5000eIPv4IPv6SnmpManagerGroup": tp5000eIPv4IPv6SnmpManagerGroup,
       "tp5000eIPv4IPv6RemoteSyslogGroup": tp5000eIPv4IPv6RemoteSyslogGroup,
       "tp5000eIPv4IPv6AuthRADIUSGroup": tp5000eIPv4IPv6AuthRADIUSGroup}
)
