# SNMP MIB module (HUAWEI-IPLPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-IPLPM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:07 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwIplpmMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328)
)
hwIplpmMib.setRevisions(
        ("2014-04-25 20:00",
         "2013-10-25 20:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWIplpmLossStatsErrorInfo(Integer32, TextualConvention):
    status = "current"
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
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("aSynClock", 6),
          ("dataErr", 3),
          ("diffAuth", 4),
          ("diffIntvl", 5),
          ("incomplete", 7),
          ("init", 0),
          ("noRecvData", 2),
          ("ok", 1),
          ("portIsDown", 8))
    )



# MIB Managed Objects in the order of their OIDs

_HwIplpmObjects_ObjectIdentity = ObjectIdentity
hwIplpmObjects = _HwIplpmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1)
)
_HwIplpmConfiguration_ObjectIdentity = ObjectIdentity
hwIplpmConfiguration = _HwIplpmConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1)
)
_HwIplpmGlobalConfiguration_ObjectIdentity = ObjectIdentity
hwIplpmGlobalConfiguration = _HwIplpmGlobalConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 1)
)
_HwIplpmGlobalTable_ObjectIdentity = ObjectIdentity
hwIplpmGlobalTable = _HwIplpmGlobalTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 1, 1)
)


class _HwIplpmLossMeasureEnable_Type(Integer32):
    """Custom type hwIplpmLossMeasureEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwIplpmLossMeasureEnable_Type.__name__ = "Integer32"
_HwIplpmLossMeasureEnable_Object = MibScalar
hwIplpmLossMeasureEnable = _HwIplpmLossMeasureEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 1, 1, 1),
    _HwIplpmLossMeasureEnable_Type()
)
hwIplpmLossMeasureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIplpmLossMeasureEnable.setStatus("current")


class _HwIplpmLossMeasureColorFlag_Type(Integer32):
    """Custom type hwIplpmLossMeasureColorFlag based on Integer32"""

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flagsBit0", 1),
          ("tosBit6", 2),
          ("tosBit7", 3))
    )


_HwIplpmLossMeasureColorFlag_Type.__name__ = "Integer32"
_HwIplpmLossMeasureColorFlag_Object = MibScalar
hwIplpmLossMeasureColorFlag = _HwIplpmLossMeasureColorFlag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 1, 1, 2),
    _HwIplpmLossMeasureColorFlag_Type()
)
hwIplpmLossMeasureColorFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIplpmLossMeasureColorFlag.setStatus("current")


class _HwIplpmLossMeasureInterval_Type(Integer32):
    """Custom type hwIplpmLossMeasureInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              60,
              600)
        )
    )
    namedValues = NamedValues(
        *(("interval10s", 10),
          ("interval1s", 1),
          ("interval600s", 600),
          ("interval60s", 60))
    )


_HwIplpmLossMeasureInterval_Type.__name__ = "Integer32"
_HwIplpmLossMeasureInterval_Object = MibScalar
hwIplpmLossMeasureInterval = _HwIplpmLossMeasureInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 1, 1, 3),
    _HwIplpmLossMeasureInterval_Type()
)
hwIplpmLossMeasureInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIplpmLossMeasureInterval.setStatus("current")


class _HwIplpmLossMeasureAlarmEnable_Type(Integer32):
    """Custom type hwIplpmLossMeasureAlarmEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwIplpmLossMeasureAlarmEnable_Type.__name__ = "Integer32"
_HwIplpmLossMeasureAlarmEnable_Object = MibScalar
hwIplpmLossMeasureAlarmEnable = _HwIplpmLossMeasureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 1, 1, 4),
    _HwIplpmLossMeasureAlarmEnable_Type()
)
hwIplpmLossMeasureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIplpmLossMeasureAlarmEnable.setStatus("current")
_HwIplpmInterfaceConguration_ObjectIdentity = ObjectIdentity
hwIplpmInterfaceConguration = _HwIplpmInterfaceConguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2)
)
_HwIplpmIntfConfigTable_Object = MibTable
hwIplpmIntfConfigTable = _HwIplpmIntfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwIplpmIntfConfigTable.setStatus("current")
_HwIplpmIntfConfigEntry_Object = MibTableRow
hwIplpmIntfConfigEntry = _HwIplpmIntfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2, 1, 1)
)
hwIplpmIntfConfigEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmIntfIfIndex"),
)
if mibBuilder.loadTexts:
    hwIplpmIntfConfigEntry.setStatus("current")


class _HwIplpmIntfIfIndex_Type(Integer32):
    """Custom type hwIplpmIntfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwIplpmIntfIfIndex_Type.__name__ = "Integer32"
_HwIplpmIntfIfIndex_Object = MibTableColumn
hwIplpmIntfIfIndex = _HwIplpmIntfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2, 1, 1, 1),
    _HwIplpmIntfIfIndex_Type()
)
hwIplpmIntfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmIntfIfIndex.setStatus("current")


class _HwIplpmIntfInterval_Type(Integer32):
    """Custom type hwIplpmIntfInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              60,
              600)
        )
    )
    namedValues = NamedValues(
        *(("interval10s", 10),
          ("interval1s", 1),
          ("interval600s", 600),
          ("interval60s", 60))
    )


_HwIplpmIntfInterval_Type.__name__ = "Integer32"
_HwIplpmIntfInterval_Object = MibTableColumn
hwIplpmIntfInterval = _HwIplpmIntfInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2, 1, 1, 2),
    _HwIplpmIntfInterval_Type()
)
hwIplpmIntfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIplpmIntfInterval.setStatus("current")


class _HwIplpmIntfAuthKeyId_Type(Integer32):
    """Custom type hwIplpmIntfAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwIplpmIntfAuthKeyId_Type.__name__ = "Integer32"
_HwIplpmIntfAuthKeyId_Object = MibTableColumn
hwIplpmIntfAuthKeyId = _HwIplpmIntfAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2, 1, 1, 3),
    _HwIplpmIntfAuthKeyId_Type()
)
hwIplpmIntfAuthKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIplpmIntfAuthKeyId.setStatus("current")


class _HwIplpmIntfAuthType_Type(Integer32):
    """Custom type hwIplpmIntfAuthType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hmacsha256", 1),
          ("none", 2))
    )


_HwIplpmIntfAuthType_Type.__name__ = "Integer32"
_HwIplpmIntfAuthType_Object = MibTableColumn
hwIplpmIntfAuthType = _HwIplpmIntfAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2, 1, 1, 4),
    _HwIplpmIntfAuthType_Type()
)
hwIplpmIntfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIplpmIntfAuthType.setStatus("current")


class _HwIplpmIntfAuthKey_Type(OctetString):
    """Custom type hwIplpmIntfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 392),
    )


_HwIplpmIntfAuthKey_Type.__name__ = "OctetString"
_HwIplpmIntfAuthKey_Object = MibTableColumn
hwIplpmIntfAuthKey = _HwIplpmIntfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2, 1, 1, 5),
    _HwIplpmIntfAuthKey_Type()
)
hwIplpmIntfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIplpmIntfAuthKey.setStatus("current")


class _HwIplpmIntfLossMeasureEnable_Type(Integer32):
    """Custom type hwIplpmIntfLossMeasureEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwIplpmIntfLossMeasureEnable_Type.__name__ = "Integer32"
_HwIplpmIntfLossMeasureEnable_Object = MibTableColumn
hwIplpmIntfLossMeasureEnable = _HwIplpmIntfLossMeasureEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2, 1, 1, 6),
    _HwIplpmIntfLossMeasureEnable_Type()
)
hwIplpmIntfLossMeasureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIplpmIntfLossMeasureEnable.setStatus("current")


class _HwIplpmIntfLossMeasureAlarmEnable_Type(Integer32):
    """Custom type hwIplpmIntfLossMeasureAlarmEnable based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_HwIplpmIntfLossMeasureAlarmEnable_Type.__name__ = "Integer32"
_HwIplpmIntfLossMeasureAlarmEnable_Object = MibTableColumn
hwIplpmIntfLossMeasureAlarmEnable = _HwIplpmIntfLossMeasureAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2, 1, 1, 7),
    _HwIplpmIntfLossMeasureAlarmEnable_Type()
)
hwIplpmIntfLossMeasureAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwIplpmIntfLossMeasureAlarmEnable.setStatus("current")
_HwIplpmIntfConfigRowStatus_Type = RowStatus
_HwIplpmIntfConfigRowStatus_Object = MibTableColumn
hwIplpmIntfConfigRowStatus = _HwIplpmIntfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 1, 2, 1, 1, 8),
    _HwIplpmIntfConfigRowStatus_Type()
)
hwIplpmIntfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwIplpmIntfConfigRowStatus.setStatus("current")
_HwIplpmStatistics_ObjectIdentity = ObjectIdentity
hwIplpmStatistics = _HwIplpmStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2)
)
_HwIplpmGlobalStatsInfo_ObjectIdentity = ObjectIdentity
hwIplpmGlobalStatsInfo = _HwIplpmGlobalStatsInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 1)
)
_HwIplpmGlobalLatestPeriodNo_Type = Counter64
_HwIplpmGlobalLatestPeriodNo_Object = MibScalar
hwIplpmGlobalLatestPeriodNo = _HwIplpmGlobalLatestPeriodNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 1, 1),
    _HwIplpmGlobalLatestPeriodNo_Type()
)
hwIplpmGlobalLatestPeriodNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalLatestPeriodNo.setStatus("current")
_HwIplpmGlobalLatestHisRecordNo_Type = Integer32
_HwIplpmGlobalLatestHisRecordNo_Object = MibScalar
hwIplpmGlobalLatestHisRecordNo = _HwIplpmGlobalLatestHisRecordNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 1, 2),
    _HwIplpmGlobalLatestHisRecordNo_Type()
)
hwIplpmGlobalLatestHisRecordNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalLatestHisRecordNo.setStatus("current")
_HwIplpmBoardEntityTable_Object = MibTable
hwIplpmBoardEntityTable = _HwIplpmBoardEntityTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hwIplpmBoardEntityTable.setStatus("current")
_HwIplpmBoardEntityEntry_Object = MibTableRow
hwIplpmBoardEntityEntry = _HwIplpmBoardEntityEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 2, 1)
)
hwIplpmBoardEntityEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmBoardNumber"),
)
if mibBuilder.loadTexts:
    hwIplpmBoardEntityEntry.setStatus("current")


class _HwIplpmBoardNumber_Type(Integer32):
    """Custom type hwIplpmBoardNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_HwIplpmBoardNumber_Type.__name__ = "Integer32"
_HwIplpmBoardNumber_Object = MibTableColumn
hwIplpmBoardNumber = _HwIplpmBoardNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 2, 1, 1),
    _HwIplpmBoardNumber_Type()
)
hwIplpmBoardNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmBoardNumber.setStatus("current")
_HwIplpmBoardPhysicalIndex_Type = Integer32
_HwIplpmBoardPhysicalIndex_Object = MibTableColumn
hwIplpmBoardPhysicalIndex = _HwIplpmBoardPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 2, 1, 2),
    _HwIplpmBoardPhysicalIndex_Type()
)
hwIplpmBoardPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmBoardPhysicalIndex.setStatus("current")
_HwIplpmGlobalStatsTable_Object = MibTable
hwIplpmGlobalStatsTable = _HwIplpmGlobalStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 3)
)
if mibBuilder.loadTexts:
    hwIplpmGlobalStatsTable.setStatus("current")
_HwIplpmGlobalStatsEntry_Object = MibTableRow
hwIplpmGlobalStatsEntry = _HwIplpmGlobalStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 3, 1)
)
hwIplpmGlobalStatsEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmGlobalPeriodHigh"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmGlobalPeriodLow"),
)
if mibBuilder.loadTexts:
    hwIplpmGlobalStatsEntry.setStatus("current")
_HwIplpmGlobalPeriodHigh_Type = Unsigned32
_HwIplpmGlobalPeriodHigh_Object = MibTableColumn
hwIplpmGlobalPeriodHigh = _HwIplpmGlobalPeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 3, 1, 1),
    _HwIplpmGlobalPeriodHigh_Type()
)
hwIplpmGlobalPeriodHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmGlobalPeriodHigh.setStatus("current")
_HwIplpmGlobalPeriodLow_Type = Unsigned32
_HwIplpmGlobalPeriodLow_Object = MibTableColumn
hwIplpmGlobalPeriodLow = _HwIplpmGlobalPeriodLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 3, 1, 2),
    _HwIplpmGlobalPeriodLow_Type()
)
hwIplpmGlobalPeriodLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmGlobalPeriodLow.setStatus("current")
_HwIplpmGlobalLossStatsErrInfo_Type = HWIplpmLossStatsErrorInfo
_HwIplpmGlobalLossStatsErrInfo_Object = MibTableColumn
hwIplpmGlobalLossStatsErrInfo = _HwIplpmGlobalLossStatsErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 3, 1, 3),
    _HwIplpmGlobalLossStatsErrInfo_Type()
)
hwIplpmGlobalLossStatsErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalLossStatsErrInfo.setStatus("current")


class _HwIplpmGlobalPeriodClock_Type(OctetString):
    """Custom type hwIplpmGlobalPeriodClock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmGlobalPeriodClock_Type.__name__ = "OctetString"
_HwIplpmGlobalPeriodClock_Object = MibTableColumn
hwIplpmGlobalPeriodClock = _HwIplpmGlobalPeriodClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 3, 1, 4),
    _HwIplpmGlobalPeriodClock_Type()
)
hwIplpmGlobalPeriodClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalPeriodClock.setStatus("current")
_HwIplpmGlobalLossPkts_Type = Counter64
_HwIplpmGlobalLossPkts_Object = MibTableColumn
hwIplpmGlobalLossPkts = _HwIplpmGlobalLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 3, 1, 5),
    _HwIplpmGlobalLossPkts_Type()
)
hwIplpmGlobalLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalLossPkts.setStatus("current")
_HwIplpmGlobalLossRatio_Type = Integer32
_HwIplpmGlobalLossRatio_Object = MibTableColumn
hwIplpmGlobalLossRatio = _HwIplpmGlobalLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 3, 1, 6),
    _HwIplpmGlobalLossRatio_Type()
)
hwIplpmGlobalLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalLossRatio.setStatus("current")
_HwIplpmLinkPeriodNoTable_Object = MibTable
hwIplpmLinkPeriodNoTable = _HwIplpmLinkPeriodNoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 4)
)
if mibBuilder.loadTexts:
    hwIplpmLinkPeriodNoTable.setStatus("current")
_HwIplpmLinkPeriodNoEntry_Object = MibTableRow
hwIplpmLinkPeriodNoEntry = _HwIplpmLinkPeriodNoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 4, 1)
)
hwIplpmLinkPeriodNoEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmIntfIfIndex"),
)
if mibBuilder.loadTexts:
    hwIplpmLinkPeriodNoEntry.setStatus("current")
_HwIplpmLinkLatestPeriodNo_Type = Counter64
_HwIplpmLinkLatestPeriodNo_Object = MibTableColumn
hwIplpmLinkLatestPeriodNo = _HwIplpmLinkLatestPeriodNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 4, 1, 1),
    _HwIplpmLinkLatestPeriodNo_Type()
)
hwIplpmLinkLatestPeriodNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkLatestPeriodNo.setStatus("current")
_HwIplpmLinkLatestHisRecordNo_Type = Integer32
_HwIplpmLinkLatestHisRecordNo_Object = MibTableColumn
hwIplpmLinkLatestHisRecordNo = _HwIplpmLinkLatestHisRecordNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 4, 1, 2),
    _HwIplpmLinkLatestHisRecordNo_Type()
)
hwIplpmLinkLatestHisRecordNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkLatestHisRecordNo.setStatus("current")
_HwIplpmLinkLossStatsTable_Object = MibTable
hwIplpmLinkLossStatsTable = _HwIplpmLinkLossStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 5)
)
if mibBuilder.loadTexts:
    hwIplpmLinkLossStatsTable.setStatus("current")
_HwIplpmLinkLossStatsEntry_Object = MibTableRow
hwIplpmLinkLossStatsEntry = _HwIplpmLinkLossStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 5, 1)
)
hwIplpmLinkLossStatsEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmIntfIfIndex"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmLinkPeriodHigh"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmLinkPeriodLow"),
)
if mibBuilder.loadTexts:
    hwIplpmLinkLossStatsEntry.setStatus("current")
_HwIplpmLinkPeriodHigh_Type = Unsigned32
_HwIplpmLinkPeriodHigh_Object = MibTableColumn
hwIplpmLinkPeriodHigh = _HwIplpmLinkPeriodHigh_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 5, 1, 1),
    _HwIplpmLinkPeriodHigh_Type()
)
hwIplpmLinkPeriodHigh.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmLinkPeriodHigh.setStatus("current")
_HwIplpmLinkPeriodLow_Type = Unsigned32
_HwIplpmLinkPeriodLow_Object = MibTableColumn
hwIplpmLinkPeriodLow = _HwIplpmLinkPeriodLow_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 5, 1, 2),
    _HwIplpmLinkPeriodLow_Type()
)
hwIplpmLinkPeriodLow.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmLinkPeriodLow.setStatus("current")
_HwIplpmLinkLossStatsErrInfo_Type = HWIplpmLossStatsErrorInfo
_HwIplpmLinkLossStatsErrInfo_Object = MibTableColumn
hwIplpmLinkLossStatsErrInfo = _HwIplpmLinkLossStatsErrInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 5, 1, 3),
    _HwIplpmLinkLossStatsErrInfo_Type()
)
hwIplpmLinkLossStatsErrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkLossStatsErrInfo.setStatus("current")


class _HwIplpmLinkPeriodClock_Type(OctetString):
    """Custom type hwIplpmLinkPeriodClock based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmLinkPeriodClock_Type.__name__ = "OctetString"
_HwIplpmLinkPeriodClock_Object = MibTableColumn
hwIplpmLinkPeriodClock = _HwIplpmLinkPeriodClock_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 5, 1, 4),
    _HwIplpmLinkPeriodClock_Type()
)
hwIplpmLinkPeriodClock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkPeriodClock.setStatus("current")
_HwIplpmLinkForwardLossPkts_Type = Counter64
_HwIplpmLinkForwardLossPkts_Object = MibTableColumn
hwIplpmLinkForwardLossPkts = _HwIplpmLinkForwardLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 5, 1, 5),
    _HwIplpmLinkForwardLossPkts_Type()
)
hwIplpmLinkForwardLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkForwardLossPkts.setStatus("current")
_HwIplpmLinkForwardLossRatio_Type = Integer32
_HwIplpmLinkForwardLossRatio_Object = MibTableColumn
hwIplpmLinkForwardLossRatio = _HwIplpmLinkForwardLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 5, 1, 6),
    _HwIplpmLinkForwardLossRatio_Type()
)
hwIplpmLinkForwardLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkForwardLossRatio.setStatus("current")
_HwIplpmLinkBackwardLossPkts_Type = Counter64
_HwIplpmLinkBackwardLossPkts_Object = MibTableColumn
hwIplpmLinkBackwardLossPkts = _HwIplpmLinkBackwardLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 5, 1, 7),
    _HwIplpmLinkBackwardLossPkts_Type()
)
hwIplpmLinkBackwardLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkBackwardLossPkts.setStatus("current")
_HwIplpmLinkBackwardLossRatio_Type = Integer32
_HwIplpmLinkBackwardLossRatio_Object = MibTableColumn
hwIplpmLinkBackwardLossRatio = _HwIplpmLinkBackwardLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 5, 1, 8),
    _HwIplpmLinkBackwardLossRatio_Type()
)
hwIplpmLinkBackwardLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkBackwardLossRatio.setStatus("current")
_HwIplpmPortQosQueStatsTable_Object = MibTable
hwIplpmPortQosQueStatsTable = _HwIplpmPortQosQueStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6)
)
if mibBuilder.loadTexts:
    hwIplpmPortQosQueStatsTable.setStatus("current")
_HwIplpmPortQosQueStatsEntry_Object = MibTableRow
hwIplpmPortQosQueStatsEntry = _HwIplpmPortQosQueStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6, 1)
)
hwIplpmPortQosQueStatsEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmIntfIfIndex"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmLinkPeriodHigh"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmLinkPeriodLow"),
)
if mibBuilder.loadTexts:
    hwIplpmPortQosQueStatsEntry.setStatus("current")
_HwIplpmPortQosQ0LossRatio_Type = Integer32
_HwIplpmPortQosQ0LossRatio_Object = MibTableColumn
hwIplpmPortQosQ0LossRatio = _HwIplpmPortQosQ0LossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6, 1, 1),
    _HwIplpmPortQosQ0LossRatio_Type()
)
hwIplpmPortQosQ0LossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortQosQ0LossRatio.setStatus("current")
_HwIplpmPortQosQ1LossRatio_Type = Integer32
_HwIplpmPortQosQ1LossRatio_Object = MibTableColumn
hwIplpmPortQosQ1LossRatio = _HwIplpmPortQosQ1LossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6, 1, 2),
    _HwIplpmPortQosQ1LossRatio_Type()
)
hwIplpmPortQosQ1LossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortQosQ1LossRatio.setStatus("current")
_HwIplpmPortQosQ2LossRatio_Type = Integer32
_HwIplpmPortQosQ2LossRatio_Object = MibTableColumn
hwIplpmPortQosQ2LossRatio = _HwIplpmPortQosQ2LossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6, 1, 3),
    _HwIplpmPortQosQ2LossRatio_Type()
)
hwIplpmPortQosQ2LossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortQosQ2LossRatio.setStatus("current")
_HwIplpmPortQosQ3LossRatio_Type = Integer32
_HwIplpmPortQosQ3LossRatio_Object = MibTableColumn
hwIplpmPortQosQ3LossRatio = _HwIplpmPortQosQ3LossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6, 1, 4),
    _HwIplpmPortQosQ3LossRatio_Type()
)
hwIplpmPortQosQ3LossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortQosQ3LossRatio.setStatus("current")
_HwIplpmPortQosQ4LossRatio_Type = Integer32
_HwIplpmPortQosQ4LossRatio_Object = MibTableColumn
hwIplpmPortQosQ4LossRatio = _HwIplpmPortQosQ4LossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6, 1, 5),
    _HwIplpmPortQosQ4LossRatio_Type()
)
hwIplpmPortQosQ4LossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortQosQ4LossRatio.setStatus("current")
_HwIplpmPortQosQ5LossRatio_Type = Integer32
_HwIplpmPortQosQ5LossRatio_Object = MibTableColumn
hwIplpmPortQosQ5LossRatio = _HwIplpmPortQosQ5LossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6, 1, 6),
    _HwIplpmPortQosQ5LossRatio_Type()
)
hwIplpmPortQosQ5LossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortQosQ5LossRatio.setStatus("current")
_HwIplpmPortQosQ6LossRatio_Type = Integer32
_HwIplpmPortQosQ6LossRatio_Object = MibTableColumn
hwIplpmPortQosQ6LossRatio = _HwIplpmPortQosQ6LossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6, 1, 7),
    _HwIplpmPortQosQ6LossRatio_Type()
)
hwIplpmPortQosQ6LossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortQosQ6LossRatio.setStatus("current")
_HwIplpmPortQosQ7LossRatio_Type = Integer32
_HwIplpmPortQosQ7LossRatio_Object = MibTableColumn
hwIplpmPortQosQ7LossRatio = _HwIplpmPortQosQ7LossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6, 1, 8),
    _HwIplpmPortQosQ7LossRatio_Type()
)
hwIplpmPortQosQ7LossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortQosQ7LossRatio.setStatus("current")
_HwIplpmPortUserQueLossRatio_Type = Integer32
_HwIplpmPortUserQueLossRatio_Object = MibTableColumn
hwIplpmPortUserQueLossRatio = _HwIplpmPortUserQueLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 6, 1, 9),
    _HwIplpmPortUserQueLossRatio_Type()
)
hwIplpmPortUserQueLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortUserQueLossRatio.setStatus("current")
_HwIplpmPortFlowStatsTable_Object = MibTable
hwIplpmPortFlowStatsTable = _HwIplpmPortFlowStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 7)
)
if mibBuilder.loadTexts:
    hwIplpmPortFlowStatsTable.setStatus("current")
_HwIplpmPortFlowStatsEntry_Object = MibTableRow
hwIplpmPortFlowStatsEntry = _HwIplpmPortFlowStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 7, 1)
)
hwIplpmPortFlowStatsEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmIntfIfIndex"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmLinkPeriodHigh"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmLinkPeriodLow"),
)
if mibBuilder.loadTexts:
    hwIplpmPortFlowStatsEntry.setStatus("current")
_HwIplpmPortInputLossRatio_Type = Integer32
_HwIplpmPortInputLossRatio_Object = MibTableColumn
hwIplpmPortInputLossRatio = _HwIplpmPortInputLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 7, 1, 1),
    _HwIplpmPortInputLossRatio_Type()
)
hwIplpmPortInputLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortInputLossRatio.setStatus("current")
_HwIplpmPortOutputLossRatio_Type = Integer32
_HwIplpmPortOutputLossRatio_Object = MibTableColumn
hwIplpmPortOutputLossRatio = _HwIplpmPortOutputLossRatio_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 2, 7, 1, 2),
    _HwIplpmPortOutputLossRatio_Type()
)
hwIplpmPortOutputLossRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmPortOutputLossRatio.setStatus("current")
_HwIplpmHistoryRecord_ObjectIdentity = ObjectIdentity
hwIplpmHistoryRecord = _HwIplpmHistoryRecord_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3)
)
_HwIplpmGlobalHisRecordTable_Object = MibTable
hwIplpmGlobalHisRecordTable = _HwIplpmGlobalHisRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwIplpmGlobalHisRecordTable.setStatus("current")
_HwIplpmGlobalHisRecordEntry_Object = MibTableRow
hwIplpmGlobalHisRecordEntry = _HwIplpmGlobalHisRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 1, 1)
)
hwIplpmGlobalHisRecordEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmGlobalHisRecordNo"),
)
if mibBuilder.loadTexts:
    hwIplpmGlobalHisRecordEntry.setStatus("current")


class _HwIplpmGlobalHisRecordNo_Type(Integer32):
    """Custom type hwIplpmGlobalHisRecordNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwIplpmGlobalHisRecordNo_Type.__name__ = "Integer32"
_HwIplpmGlobalHisRecordNo_Object = MibTableColumn
hwIplpmGlobalHisRecordNo = _HwIplpmGlobalHisRecordNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 1, 1, 1),
    _HwIplpmGlobalHisRecordNo_Type()
)
hwIplpmGlobalHisRecordNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmGlobalHisRecordNo.setStatus("current")
_HwIplpmGlobalLossRatioMax_Type = Integer32
_HwIplpmGlobalLossRatioMax_Object = MibTableColumn
hwIplpmGlobalLossRatioMax = _HwIplpmGlobalLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 1, 1, 2),
    _HwIplpmGlobalLossRatioMax_Type()
)
hwIplpmGlobalLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalLossRatioMax.setStatus("current")
_HwIplpmGlobalLossRatioMin_Type = Integer32
_HwIplpmGlobalLossRatioMin_Object = MibTableColumn
hwIplpmGlobalLossRatioMin = _HwIplpmGlobalLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 1, 1, 3),
    _HwIplpmGlobalLossRatioMin_Type()
)
hwIplpmGlobalLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalLossRatioMin.setStatus("current")
_HwIplpmGlobalTotalLossPkts_Type = Counter64
_HwIplpmGlobalTotalLossPkts_Object = MibTableColumn
hwIplpmGlobalTotalLossPkts = _HwIplpmGlobalTotalLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 1, 1, 4),
    _HwIplpmGlobalTotalLossPkts_Type()
)
hwIplpmGlobalTotalLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalTotalLossPkts.setStatus("current")
_HwIplpmGlobalTotalRecvPkts_Type = Counter64
_HwIplpmGlobalTotalRecvPkts_Object = MibTableColumn
hwIplpmGlobalTotalRecvPkts = _HwIplpmGlobalTotalRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 1, 1, 5),
    _HwIplpmGlobalTotalRecvPkts_Type()
)
hwIplpmGlobalTotalRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalTotalRecvPkts.setStatus("current")


class _HwIplpmGlobalHisRecStartTime_Type(OctetString):
    """Custom type hwIplpmGlobalHisRecStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmGlobalHisRecStartTime_Type.__name__ = "OctetString"
_HwIplpmGlobalHisRecStartTime_Object = MibTableColumn
hwIplpmGlobalHisRecStartTime = _HwIplpmGlobalHisRecStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 1, 1, 6),
    _HwIplpmGlobalHisRecStartTime_Type()
)
hwIplpmGlobalHisRecStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalHisRecStartTime.setStatus("current")


class _HwIplpmGlobalHisRecEndTime_Type(OctetString):
    """Custom type hwIplpmGlobalHisRecEndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmGlobalHisRecEndTime_Type.__name__ = "OctetString"
_HwIplpmGlobalHisRecEndTime_Object = MibTableColumn
hwIplpmGlobalHisRecEndTime = _HwIplpmGlobalHisRecEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 1, 1, 7),
    _HwIplpmGlobalHisRecEndTime_Type()
)
hwIplpmGlobalHisRecEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalHisRecEndTime.setStatus("current")
_HwIplpmGlobalValidStatDataNum_Type = Integer32
_HwIplpmGlobalValidStatDataNum_Object = MibTableColumn
hwIplpmGlobalValidStatDataNum = _HwIplpmGlobalValidStatDataNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 1, 1, 8),
    _HwIplpmGlobalValidStatDataNum_Type()
)
hwIplpmGlobalValidStatDataNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmGlobalValidStatDataNum.setStatus("current")
_HwIplpmLinkHisRecordEntryTable_Object = MibTable
hwIplpmLinkHisRecordEntryTable = _HwIplpmLinkHisRecordEntryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwIplpmLinkHisRecordEntryTable.setStatus("current")
_HwIplpmLinkHisRecordEntryEntry_Object = MibTableRow
hwIplpmLinkHisRecordEntryEntry = _HwIplpmLinkHisRecordEntryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1)
)
hwIplpmLinkHisRecordEntryEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmIntfIfIndex"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmLinkHisRecordNo"),
)
if mibBuilder.loadTexts:
    hwIplpmLinkHisRecordEntryEntry.setStatus("current")


class _HwIplpmLinkHisRecordNo_Type(Integer32):
    """Custom type hwIplpmLinkHisRecordNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwIplpmLinkHisRecordNo_Type.__name__ = "Integer32"
_HwIplpmLinkHisRecordNo_Object = MibTableColumn
hwIplpmLinkHisRecordNo = _HwIplpmLinkHisRecordNo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 1),
    _HwIplpmLinkHisRecordNo_Type()
)
hwIplpmLinkHisRecordNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmLinkHisRecordNo.setStatus("current")
_HwIplpmLinkForwardLossRatioMax_Type = Integer32
_HwIplpmLinkForwardLossRatioMax_Object = MibTableColumn
hwIplpmLinkForwardLossRatioMax = _HwIplpmLinkForwardLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 2),
    _HwIplpmLinkForwardLossRatioMax_Type()
)
hwIplpmLinkForwardLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkForwardLossRatioMax.setStatus("current")
_HwIplpmLinkForwardLossRatioMin_Type = Integer32
_HwIplpmLinkForwardLossRatioMin_Object = MibTableColumn
hwIplpmLinkForwardLossRatioMin = _HwIplpmLinkForwardLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 3),
    _HwIplpmLinkForwardLossRatioMin_Type()
)
hwIplpmLinkForwardLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkForwardLossRatioMin.setStatus("current")
_HwIplpmLinkForwardTotalLossPkts_Type = Counter64
_HwIplpmLinkForwardTotalLossPkts_Object = MibTableColumn
hwIplpmLinkForwardTotalLossPkts = _HwIplpmLinkForwardTotalLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 4),
    _HwIplpmLinkForwardTotalLossPkts_Type()
)
hwIplpmLinkForwardTotalLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkForwardTotalLossPkts.setStatus("current")
_HwIplpmLinkForwardTotalRecvPkts_Type = Counter64
_HwIplpmLinkForwardTotalRecvPkts_Object = MibTableColumn
hwIplpmLinkForwardTotalRecvPkts = _HwIplpmLinkForwardTotalRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 5),
    _HwIplpmLinkForwardTotalRecvPkts_Type()
)
hwIplpmLinkForwardTotalRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkForwardTotalRecvPkts.setStatus("current")
_HwIplpmLinkBackwardLossRatioMax_Type = Integer32
_HwIplpmLinkBackwardLossRatioMax_Object = MibTableColumn
hwIplpmLinkBackwardLossRatioMax = _HwIplpmLinkBackwardLossRatioMax_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 6),
    _HwIplpmLinkBackwardLossRatioMax_Type()
)
hwIplpmLinkBackwardLossRatioMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkBackwardLossRatioMax.setStatus("current")
_HwIplpmLinkBackwardLossRatioMin_Type = Integer32
_HwIplpmLinkBackwardLossRatioMin_Object = MibTableColumn
hwIplpmLinkBackwardLossRatioMin = _HwIplpmLinkBackwardLossRatioMin_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 7),
    _HwIplpmLinkBackwardLossRatioMin_Type()
)
hwIplpmLinkBackwardLossRatioMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkBackwardLossRatioMin.setStatus("current")
_HwIplpmLinkBackwardTotalLossPkts_Type = Counter64
_HwIplpmLinkBackwardTotalLossPkts_Object = MibTableColumn
hwIplpmLinkBackwardTotalLossPkts = _HwIplpmLinkBackwardTotalLossPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 8),
    _HwIplpmLinkBackwardTotalLossPkts_Type()
)
hwIplpmLinkBackwardTotalLossPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkBackwardTotalLossPkts.setStatus("current")
_HwIplpmLinkBackwardTotalRecvPkts_Type = Counter64
_HwIplpmLinkBackwardTotalRecvPkts_Object = MibTableColumn
hwIplpmLinkBackwardTotalRecvPkts = _HwIplpmLinkBackwardTotalRecvPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 9),
    _HwIplpmLinkBackwardTotalRecvPkts_Type()
)
hwIplpmLinkBackwardTotalRecvPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkBackwardTotalRecvPkts.setStatus("current")


class _HwIplpmLinkHisRecordStartTime_Type(OctetString):
    """Custom type hwIplpmLinkHisRecordStartTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmLinkHisRecordStartTime_Type.__name__ = "OctetString"
_HwIplpmLinkHisRecordStartTime_Object = MibTableColumn
hwIplpmLinkHisRecordStartTime = _HwIplpmLinkHisRecordStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 10),
    _HwIplpmLinkHisRecordStartTime_Type()
)
hwIplpmLinkHisRecordStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkHisRecordStartTime.setStatus("current")


class _HwIplpmLinkHisRecordEndTime_Type(OctetString):
    """Custom type hwIplpmLinkHisRecordEndTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmLinkHisRecordEndTime_Type.__name__ = "OctetString"
_HwIplpmLinkHisRecordEndTime_Object = MibTableColumn
hwIplpmLinkHisRecordEndTime = _HwIplpmLinkHisRecordEndTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 11),
    _HwIplpmLinkHisRecordEndTime_Type()
)
hwIplpmLinkHisRecordEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkHisRecordEndTime.setStatus("current")
_HwIplpmLinkValidStatDataNum_Type = Integer32
_HwIplpmLinkValidStatDataNum_Object = MibTableColumn
hwIplpmLinkValidStatDataNum = _HwIplpmLinkValidStatDataNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 3, 2, 1, 12),
    _HwIplpmLinkValidStatDataNum_Type()
)
hwIplpmLinkValidStatDataNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLinkValidStatDataNum.setStatus("current")
_HwIplpmFwdPathSearch_ObjectIdentity = ObjectIdentity
hwIplpmFwdPathSearch = _HwIplpmFwdPathSearch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4)
)
_HwIplpmGateWaySearchTable_Object = MibTable
hwIplpmGateWaySearchTable = _HwIplpmGateWaySearchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwIplpmGateWaySearchTable.setStatus("current")
_HwIplpmGateWaySearchEntry_Object = MibTableRow
hwIplpmGateWaySearchEntry = _HwIplpmGateWaySearchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1)
)
hwIplpmGateWaySearchEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmNetAddress"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmNetMask"),
)
if mibBuilder.loadTexts:
    hwIplpmGateWaySearchEntry.setStatus("current")
_HwIplpmNetAddress_Type = IpAddress
_HwIplpmNetAddress_Object = MibTableColumn
hwIplpmNetAddress = _HwIplpmNetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 1),
    _HwIplpmNetAddress_Type()
)
hwIplpmNetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmNetAddress.setStatus("current")
_HwIplpmNetMask_Type = IpAddress
_HwIplpmNetMask_Object = MibTableColumn
hwIplpmNetMask = _HwIplpmNetMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 2),
    _HwIplpmNetMask_Type()
)
hwIplpmNetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmNetMask.setStatus("current")
_HwIplpmNetIfIndex_Type = Integer32
_HwIplpmNetIfIndex_Object = MibTableColumn
hwIplpmNetIfIndex = _HwIplpmNetIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 3),
    _HwIplpmNetIfIndex_Type()
)
hwIplpmNetIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfIndex.setStatus("current")


class _HwIplpmNetIfName_Type(OctetString):
    """Custom type hwIplpmNetIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwIplpmNetIfName_Type.__name__ = "OctetString"
_HwIplpmNetIfName_Object = MibTableColumn
hwIplpmNetIfName = _HwIplpmNetIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 4),
    _HwIplpmNetIfName_Type()
)
hwIplpmNetIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfName.setStatus("current")


class _HwIplpmNetIfMacAddress_Type(OctetString):
    """Custom type hwIplpmNetIfMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmNetIfMacAddress_Type.__name__ = "OctetString"
_HwIplpmNetIfMacAddress_Object = MibTableColumn
hwIplpmNetIfMacAddress = _HwIplpmNetIfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 5),
    _HwIplpmNetIfMacAddress_Type()
)
hwIplpmNetIfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfMacAddress.setStatus("current")
_HwIplpmNetIfAddress_Type = IpAddress
_HwIplpmNetIfAddress_Object = MibTableColumn
hwIplpmNetIfAddress = _HwIplpmNetIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 6),
    _HwIplpmNetIfAddress_Type()
)
hwIplpmNetIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfAddress.setStatus("current")
_HwIplpmNetIfMask_Type = IpAddress
_HwIplpmNetIfMask_Object = MibTableColumn
hwIplpmNetIfMask = _HwIplpmNetIfMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 7),
    _HwIplpmNetIfMask_Type()
)
hwIplpmNetIfMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfMask.setStatus("current")


class _HwIplpmNetIfVpnName_Type(OctetString):
    """Custom type hwIplpmNetIfVpnName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmNetIfVpnName_Type.__name__ = "OctetString"
_HwIplpmNetIfVpnName_Object = MibTableColumn
hwIplpmNetIfVpnName = _HwIplpmNetIfVpnName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 8),
    _HwIplpmNetIfVpnName_Type()
)
hwIplpmNetIfVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfVpnName.setStatus("current")
_HwIplpmNetIfVrf_Type = Integer32
_HwIplpmNetIfVrf_Object = MibTableColumn
hwIplpmNetIfVrf = _HwIplpmNetIfVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 9),
    _HwIplpmNetIfVrf_Type()
)
hwIplpmNetIfVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfVrf.setStatus("current")
_HwIplpmNetIfVlan_Type = Integer32
_HwIplpmNetIfVlan_Object = MibTableColumn
hwIplpmNetIfVlan = _HwIplpmNetIfVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 10),
    _HwIplpmNetIfVlan_Type()
)
hwIplpmNetIfVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfVlan.setStatus("current")


class _HwIplpmNetSystemMac_Type(OctetString):
    """Custom type hwIplpmNetSystemMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmNetSystemMac_Type.__name__ = "OctetString"
_HwIplpmNetSystemMac_Object = MibTableColumn
hwIplpmNetSystemMac = _HwIplpmNetSystemMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 11),
    _HwIplpmNetSystemMac_Type()
)
hwIplpmNetSystemMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetSystemMac.setStatus("current")
_HwIplpmNetIfVrrpVip_Type = IpAddress
_HwIplpmNetIfVrrpVip_Object = MibTableColumn
hwIplpmNetIfVrrpVip = _HwIplpmNetIfVrrpVip_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 12),
    _HwIplpmNetIfVrrpVip_Type()
)
hwIplpmNetIfVrrpVip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfVrrpVip.setStatus("current")


class _HwIplpmNetIfVrrpMac_Type(OctetString):
    """Custom type hwIplpmNetIfVrrpMac based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmNetIfVrrpMac_Type.__name__ = "OctetString"
_HwIplpmNetIfVrrpMac_Object = MibTableColumn
hwIplpmNetIfVrrpMac = _HwIplpmNetIfVrrpMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 13),
    _HwIplpmNetIfVrrpMac_Type()
)
hwIplpmNetIfVrrpMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfVrrpMac.setStatus("current")


class _HwIplpmNetIfVrrpState_Type(Integer32):
    """Custom type hwIplpmNetIfVrrpState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("backup", 2),
          ("initialize", 1),
          ("master", 3),
          ("notexist", 255))
    )


_HwIplpmNetIfVrrpState_Type.__name__ = "Integer32"
_HwIplpmNetIfVrrpState_Object = MibTableColumn
hwIplpmNetIfVrrpState = _HwIplpmNetIfVrrpState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 14),
    _HwIplpmNetIfVrrpState_Type()
)
hwIplpmNetIfVrrpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfVrrpState.setStatus("current")
_HwIplpmNetIfHostAddress_Type = IpAddress
_HwIplpmNetIfHostAddress_Object = MibTableColumn
hwIplpmNetIfHostAddress = _HwIplpmNetIfHostAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 1, 1, 15),
    _HwIplpmNetIfHostAddress_Type()
)
hwIplpmNetIfHostAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmNetIfHostAddress.setStatus("current")
_HwIplpmHostInfoSearchTable_Object = MibTable
hwIplpmHostInfoSearchTable = _HwIplpmHostInfoSearchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 2)
)
if mibBuilder.loadTexts:
    hwIplpmHostInfoSearchTable.setStatus("current")
_HwIplpmHostInfoSearchEntry_Object = MibTableRow
hwIplpmHostInfoSearchEntry = _HwIplpmHostInfoSearchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 2, 1)
)
hwIplpmHostInfoSearchEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmHostIpAddress"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmHostVrf"),
)
if mibBuilder.loadTexts:
    hwIplpmHostInfoSearchEntry.setStatus("current")
_HwIplpmHostIpAddress_Type = IpAddress
_HwIplpmHostIpAddress_Object = MibTableColumn
hwIplpmHostIpAddress = _HwIplpmHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 2, 1, 1),
    _HwIplpmHostIpAddress_Type()
)
hwIplpmHostIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmHostIpAddress.setStatus("current")
_HwIplpmHostVrf_Type = Integer32
_HwIplpmHostVrf_Object = MibTableColumn
hwIplpmHostVrf = _HwIplpmHostVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 2, 1, 2),
    _HwIplpmHostVrf_Type()
)
hwIplpmHostVrf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmHostVrf.setStatus("current")
_HwIplpmHostIfIndex_Type = Integer32
_HwIplpmHostIfIndex_Object = MibTableColumn
hwIplpmHostIfIndex = _HwIplpmHostIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 2, 1, 3),
    _HwIplpmHostIfIndex_Type()
)
hwIplpmHostIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmHostIfIndex.setStatus("current")


class _HwIplpmHostIfName_Type(OctetString):
    """Custom type hwIplpmHostIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwIplpmHostIfName_Type.__name__ = "OctetString"
_HwIplpmHostIfName_Object = MibTableColumn
hwIplpmHostIfName = _HwIplpmHostIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 2, 1, 4),
    _HwIplpmHostIfName_Type()
)
hwIplpmHostIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmHostIfName.setStatus("current")


class _HwIplpmHostMacAddress_Type(OctetString):
    """Custom type hwIplpmHostMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_HwIplpmHostMacAddress_Type.__name__ = "OctetString"
_HwIplpmHostMacAddress_Object = MibTableColumn
hwIplpmHostMacAddress = _HwIplpmHostMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 2, 1, 5),
    _HwIplpmHostMacAddress_Type()
)
hwIplpmHostMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmHostMacAddress.setStatus("current")
_HwIplpmHostVlan_Type = Integer32
_HwIplpmHostVlan_Object = MibTableColumn
hwIplpmHostVlan = _HwIplpmHostVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 2, 1, 6),
    _HwIplpmHostVlan_Type()
)
hwIplpmHostVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmHostVlan.setStatus("current")
_HwIplpmHostCeVlan_Type = Integer32
_HwIplpmHostCeVlan_Object = MibTableColumn
hwIplpmHostCeVlan = _HwIplpmHostCeVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 2, 1, 7),
    _HwIplpmHostCeVlan_Type()
)
hwIplpmHostCeVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmHostCeVlan.setStatus("current")
_HwIplpmLocalIpSearchTable_Object = MibTable
hwIplpmLocalIpSearchTable = _HwIplpmLocalIpSearchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 3)
)
if mibBuilder.loadTexts:
    hwIplpmLocalIpSearchTable.setStatus("current")
_HwIplpmLocalIpSearchEntry_Object = MibTableRow
hwIplpmLocalIpSearchEntry = _HwIplpmLocalIpSearchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 3, 1)
)
hwIplpmLocalIpSearchEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmLocalIpAddress"),
)
if mibBuilder.loadTexts:
    hwIplpmLocalIpSearchEntry.setStatus("current")
_HwIplpmLocalIpAddress_Type = IpAddress
_HwIplpmLocalIpAddress_Object = MibTableColumn
hwIplpmLocalIpAddress = _HwIplpmLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 3, 1, 1),
    _HwIplpmLocalIpAddress_Type()
)
hwIplpmLocalIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmLocalIpAddress.setStatus("current")
_HwIplpmLocalIfIndex_Type = Integer32
_HwIplpmLocalIfIndex_Object = MibTableColumn
hwIplpmLocalIfIndex = _HwIplpmLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 3, 1, 2),
    _HwIplpmLocalIfIndex_Type()
)
hwIplpmLocalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLocalIfIndex.setStatus("current")


class _HwIplpmLocalIfType_Type(Integer32):
    """Custom type hwIplpmLocalIfType based on Integer32"""
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
        *(("ethernet", 1),
          ("ethtrunk", 2),
          ("other", 4),
          ("vlanif", 3))
    )


_HwIplpmLocalIfType_Type.__name__ = "Integer32"
_HwIplpmLocalIfType_Object = MibTableColumn
hwIplpmLocalIfType = _HwIplpmLocalIfType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 3, 1, 3),
    _HwIplpmLocalIfType_Type()
)
hwIplpmLocalIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLocalIfType.setStatus("current")
_HwIplpmLocalIfVrf_Type = Integer32
_HwIplpmLocalIfVrf_Object = MibTableColumn
hwIplpmLocalIfVrf = _HwIplpmLocalIfVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 3, 1, 4),
    _HwIplpmLocalIfVrf_Type()
)
hwIplpmLocalIfVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLocalIfVrf.setStatus("current")


class _HwIplpmLocalPortList_Type(OctetString):
    """Custom type hwIplpmLocalPortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_HwIplpmLocalPortList_Type.__name__ = "OctetString"
_HwIplpmLocalPortList_Object = MibTableColumn
hwIplpmLocalPortList = _HwIplpmLocalPortList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 3, 1, 5),
    _HwIplpmLocalPortList_Type()
)
hwIplpmLocalPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmLocalPortList.setStatus("current")
_HwIplpmIpRouteSearchTable_Object = MibTable
hwIplpmIpRouteSearchTable = _HwIplpmIpRouteSearchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 4)
)
if mibBuilder.loadTexts:
    hwIplpmIpRouteSearchTable.setStatus("current")
_HwIplpmIpRouteSearchEntry_Object = MibTableRow
hwIplpmIpRouteSearchEntry = _HwIplpmIpRouteSearchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 4, 1)
)
hwIplpmIpRouteSearchEntry.setIndexNames(
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmDestIpAddress"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmDestMask"),
    (0, "HUAWEI-IPLPM-MIB", "hwIplpmDestVrf"),
)
if mibBuilder.loadTexts:
    hwIplpmIpRouteSearchEntry.setStatus("current")
_HwIplpmDestIpAddress_Type = IpAddress
_HwIplpmDestIpAddress_Object = MibTableColumn
hwIplpmDestIpAddress = _HwIplpmDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 4, 1, 1),
    _HwIplpmDestIpAddress_Type()
)
hwIplpmDestIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmDestIpAddress.setStatus("current")
_HwIplpmDestMask_Type = IpAddress
_HwIplpmDestMask_Object = MibTableColumn
hwIplpmDestMask = _HwIplpmDestMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 4, 1, 2),
    _HwIplpmDestMask_Type()
)
hwIplpmDestMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmDestMask.setStatus("current")
_HwIplpmDestVrf_Type = Integer32
_HwIplpmDestVrf_Object = MibTableColumn
hwIplpmDestVrf = _HwIplpmDestVrf_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 4, 1, 3),
    _HwIplpmDestVrf_Type()
)
hwIplpmDestVrf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwIplpmDestVrf.setStatus("current")
_HwIplpmRouteDstAddr_Type = IpAddress
_HwIplpmRouteDstAddr_Object = MibTableColumn
hwIplpmRouteDstAddr = _HwIplpmRouteDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 4, 1, 4),
    _HwIplpmRouteDstAddr_Type()
)
hwIplpmRouteDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmRouteDstAddr.setStatus("current")
_HwIplpmRouteDstMask_Type = IpAddress
_HwIplpmRouteDstMask_Object = MibTableColumn
hwIplpmRouteDstMask = _HwIplpmRouteDstMask_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 4, 1, 5),
    _HwIplpmRouteDstMask_Type()
)
hwIplpmRouteDstMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmRouteDstMask.setStatus("current")
_HwIplpmRouteIfIndex_Type = Integer32
_HwIplpmRouteIfIndex_Object = MibTableColumn
hwIplpmRouteIfIndex = _HwIplpmRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 4, 1, 6),
    _HwIplpmRouteIfIndex_Type()
)
hwIplpmRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmRouteIfIndex.setStatus("current")
_HwIplpmOutPortIfIndex_Type = Integer32
_HwIplpmOutPortIfIndex_Object = MibTableColumn
hwIplpmOutPortIfIndex = _HwIplpmOutPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 1, 4, 4, 1, 7),
    _HwIplpmOutPortIfIndex_Type()
)
hwIplpmOutPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIplpmOutPortIfIndex.setStatus("current")
_HwIplpmTraps_ObjectIdentity = ObjectIdentity
hwIplpmTraps = _HwIplpmTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 2)
)
_HwIplpmConformance_ObjectIdentity = ObjectIdentity
hwIplpmConformance = _HwIplpmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 3)
)
_HwIplpmCompliances_ObjectIdentity = ObjectIdentity
hwIplpmCompliances = _HwIplpmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 3, 1)
)
_HwIplpmGroups_ObjectIdentity = ObjectIdentity
hwIplpmGroups = _HwIplpmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 3, 3)
)

# Managed Objects groups

hwIplpmGlobalConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 3, 3, 1)
)
hwIplpmGlobalConfigGroup.setObjects(
      *(("HUAWEI-IPLPM-MIB", "hwIplpmLossMeasureColorFlag"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLossMeasureInterval"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLossMeasureEnable"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmIntfLossMeasureAlarmEnable"))
)
if mibBuilder.loadTexts:
    hwIplpmGlobalConfigGroup.setStatus("current")

hwIplpmInterfacelConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 3, 3, 2)
)
hwIplpmInterfacelConfigGroup.setObjects(
      *(("HUAWEI-IPLPM-MIB", "hwIplpmIntfConfigRowStatus"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmIntfInterval"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmIntfAuthKeyId"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmIntfAuthType"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmIntfAuthKey"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmIntfLossMeasureEnable"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLossMeasureAlarmEnable"))
)
if mibBuilder.loadTexts:
    hwIplpmInterfacelConfigGroup.setStatus("current")

hwIplpmStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 3, 3, 3)
)
hwIplpmStatisticsGroup.setObjects(
      *(("HUAWEI-IPLPM-MIB", "hwIplpmLinkPeriodClock"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardLossPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkBackwardLossPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkLossStatsErrInfo"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmBoardPhysicalIndex"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortUserQueLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkBackwardLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossStatsErrInfo"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalPeriodClock"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ0LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ1LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ2LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ3LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ4LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ5LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ6LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ7LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortInputLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortOutputLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLatestPeriodNo"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLatestHisRecordNo"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkLatestPeriodNo"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkLatestHisRecordNo"))
)
if mibBuilder.loadTexts:
    hwIplpmStatisticsGroup.setStatus("current")

hwIplpmHistoryRecordGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 3, 3, 4)
)
hwIplpmHistoryRecordGroup.setObjects(
      *(("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossRatioMax"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossRatioMin"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalTotalLossPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalTotalRecvPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardLossRatioMax"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardLossRatioMin"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardTotalLossPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardTotalRecvPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkBackwardLossRatioMax"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkBackwardLossRatioMin"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkBackwardTotalLossPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalValidStatDataNum"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkValidStatDataNum"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkBackwardTotalRecvPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalHisRecStartTime"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalHisRecEndTime"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkHisRecordStartTime"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkHisRecordEndTime"))
)
if mibBuilder.loadTexts:
    hwIplpmHistoryRecordGroup.setStatus("current")

hwIplpmFwdPathSearchGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 3, 3, 5)
)
hwIplpmFwdPathSearchGroup.setObjects(
      *(("HUAWEI-IPLPM-MIB", "hwIplpmNetIfIndex"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfName"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfMacAddress"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfAddress"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfMask"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfVpnName"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfVrf"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfVlan"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetSystemMac"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmHostIfIndex"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmHostIfName"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmHostMacAddress"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmHostVlan"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmHostCeVlan"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLocalIfIndex"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLocalIfType"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLocalIfVrf"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLocalPortList"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmRouteIfIndex"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmRouteDstAddr"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmRouteDstMask"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmOutPortIfIndex"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfVrrpVip"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfVrrpMac"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfVrrpState"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmNetIfHostAddress"))
)
if mibBuilder.loadTexts:
    hwIplpmFwdPathSearchGroup.setStatus("current")


# Notification objects

hwIplpmGlobalLossRatioExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 2, 1)
)
hwIplpmGlobalLossRatioExceed.setObjects(
      *(("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLatestPeriodNo"))
)
if mibBuilder.loadTexts:
    hwIplpmGlobalLossRatioExceed.setStatus(
        "current"
    )

hwIplpmGlobalLossRatioRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 2, 2)
)
hwIplpmGlobalLossRatioRecovery.setObjects(
      *(("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLatestPeriodNo"))
)
if mibBuilder.loadTexts:
    hwIplpmGlobalLossRatioRecovery.setStatus(
        "current"
    )

hwIplpmLinkForwardLossRatioExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 2, 3)
)
hwIplpmLinkForwardLossRatioExceed.setObjects(
      *(("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardLossPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ0LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ1LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ2LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ3LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ4LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ5LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ6LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortQosQ7LossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortUserQueLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmPortOutputLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkLatestPeriodNo"))
)
if mibBuilder.loadTexts:
    hwIplpmLinkForwardLossRatioExceed.setStatus(
        "current"
    )

hwIplpmLinkForwardLossRatioRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 2, 4)
)
hwIplpmLinkForwardLossRatioRecovery.setObjects(
      *(("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardLossPkts"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardLossRatio"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkLatestPeriodNo"))
)
if mibBuilder.loadTexts:
    hwIplpmLinkForwardLossRatioRecovery.setStatus(
        "current"
    )


# Notifications groups

hwIplpmTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 3, 3, 6)
)
hwIplpmTrapsGroup.setObjects(
      *(("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardLossRatioExceed"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmLinkForwardLossRatioRecovery"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossRatioRecovery"),
        ("HUAWEI-IPLPM-MIB", "hwIplpmGlobalLossRatioExceed"))
)
if mibBuilder.loadTexts:
    hwIplpmTrapsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwIplpmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 328, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwIplpmCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-IPLPM-MIB",
    **{"HWIplpmLossStatsErrorInfo": HWIplpmLossStatsErrorInfo,
       "hwIplpmMib": hwIplpmMib,
       "hwIplpmObjects": hwIplpmObjects,
       "hwIplpmConfiguration": hwIplpmConfiguration,
       "hwIplpmGlobalConfiguration": hwIplpmGlobalConfiguration,
       "hwIplpmGlobalTable": hwIplpmGlobalTable,
       "hwIplpmLossMeasureEnable": hwIplpmLossMeasureEnable,
       "hwIplpmLossMeasureColorFlag": hwIplpmLossMeasureColorFlag,
       "hwIplpmLossMeasureInterval": hwIplpmLossMeasureInterval,
       "hwIplpmLossMeasureAlarmEnable": hwIplpmLossMeasureAlarmEnable,
       "hwIplpmInterfaceConguration": hwIplpmInterfaceConguration,
       "hwIplpmIntfConfigTable": hwIplpmIntfConfigTable,
       "hwIplpmIntfConfigEntry": hwIplpmIntfConfigEntry,
       "hwIplpmIntfIfIndex": hwIplpmIntfIfIndex,
       "hwIplpmIntfInterval": hwIplpmIntfInterval,
       "hwIplpmIntfAuthKeyId": hwIplpmIntfAuthKeyId,
       "hwIplpmIntfAuthType": hwIplpmIntfAuthType,
       "hwIplpmIntfAuthKey": hwIplpmIntfAuthKey,
       "hwIplpmIntfLossMeasureEnable": hwIplpmIntfLossMeasureEnable,
       "hwIplpmIntfLossMeasureAlarmEnable": hwIplpmIntfLossMeasureAlarmEnable,
       "hwIplpmIntfConfigRowStatus": hwIplpmIntfConfigRowStatus,
       "hwIplpmStatistics": hwIplpmStatistics,
       "hwIplpmGlobalStatsInfo": hwIplpmGlobalStatsInfo,
       "hwIplpmGlobalLatestPeriodNo": hwIplpmGlobalLatestPeriodNo,
       "hwIplpmGlobalLatestHisRecordNo": hwIplpmGlobalLatestHisRecordNo,
       "hwIplpmBoardEntityTable": hwIplpmBoardEntityTable,
       "hwIplpmBoardEntityEntry": hwIplpmBoardEntityEntry,
       "hwIplpmBoardNumber": hwIplpmBoardNumber,
       "hwIplpmBoardPhysicalIndex": hwIplpmBoardPhysicalIndex,
       "hwIplpmGlobalStatsTable": hwIplpmGlobalStatsTable,
       "hwIplpmGlobalStatsEntry": hwIplpmGlobalStatsEntry,
       "hwIplpmGlobalPeriodHigh": hwIplpmGlobalPeriodHigh,
       "hwIplpmGlobalPeriodLow": hwIplpmGlobalPeriodLow,
       "hwIplpmGlobalLossStatsErrInfo": hwIplpmGlobalLossStatsErrInfo,
       "hwIplpmGlobalPeriodClock": hwIplpmGlobalPeriodClock,
       "hwIplpmGlobalLossPkts": hwIplpmGlobalLossPkts,
       "hwIplpmGlobalLossRatio": hwIplpmGlobalLossRatio,
       "hwIplpmLinkPeriodNoTable": hwIplpmLinkPeriodNoTable,
       "hwIplpmLinkPeriodNoEntry": hwIplpmLinkPeriodNoEntry,
       "hwIplpmLinkLatestPeriodNo": hwIplpmLinkLatestPeriodNo,
       "hwIplpmLinkLatestHisRecordNo": hwIplpmLinkLatestHisRecordNo,
       "hwIplpmLinkLossStatsTable": hwIplpmLinkLossStatsTable,
       "hwIplpmLinkLossStatsEntry": hwIplpmLinkLossStatsEntry,
       "hwIplpmLinkPeriodHigh": hwIplpmLinkPeriodHigh,
       "hwIplpmLinkPeriodLow": hwIplpmLinkPeriodLow,
       "hwIplpmLinkLossStatsErrInfo": hwIplpmLinkLossStatsErrInfo,
       "hwIplpmLinkPeriodClock": hwIplpmLinkPeriodClock,
       "hwIplpmLinkForwardLossPkts": hwIplpmLinkForwardLossPkts,
       "hwIplpmLinkForwardLossRatio": hwIplpmLinkForwardLossRatio,
       "hwIplpmLinkBackwardLossPkts": hwIplpmLinkBackwardLossPkts,
       "hwIplpmLinkBackwardLossRatio": hwIplpmLinkBackwardLossRatio,
       "hwIplpmPortQosQueStatsTable": hwIplpmPortQosQueStatsTable,
       "hwIplpmPortQosQueStatsEntry": hwIplpmPortQosQueStatsEntry,
       "hwIplpmPortQosQ0LossRatio": hwIplpmPortQosQ0LossRatio,
       "hwIplpmPortQosQ1LossRatio": hwIplpmPortQosQ1LossRatio,
       "hwIplpmPortQosQ2LossRatio": hwIplpmPortQosQ2LossRatio,
       "hwIplpmPortQosQ3LossRatio": hwIplpmPortQosQ3LossRatio,
       "hwIplpmPortQosQ4LossRatio": hwIplpmPortQosQ4LossRatio,
       "hwIplpmPortQosQ5LossRatio": hwIplpmPortQosQ5LossRatio,
       "hwIplpmPortQosQ6LossRatio": hwIplpmPortQosQ6LossRatio,
       "hwIplpmPortQosQ7LossRatio": hwIplpmPortQosQ7LossRatio,
       "hwIplpmPortUserQueLossRatio": hwIplpmPortUserQueLossRatio,
       "hwIplpmPortFlowStatsTable": hwIplpmPortFlowStatsTable,
       "hwIplpmPortFlowStatsEntry": hwIplpmPortFlowStatsEntry,
       "hwIplpmPortInputLossRatio": hwIplpmPortInputLossRatio,
       "hwIplpmPortOutputLossRatio": hwIplpmPortOutputLossRatio,
       "hwIplpmHistoryRecord": hwIplpmHistoryRecord,
       "hwIplpmGlobalHisRecordTable": hwIplpmGlobalHisRecordTable,
       "hwIplpmGlobalHisRecordEntry": hwIplpmGlobalHisRecordEntry,
       "hwIplpmGlobalHisRecordNo": hwIplpmGlobalHisRecordNo,
       "hwIplpmGlobalLossRatioMax": hwIplpmGlobalLossRatioMax,
       "hwIplpmGlobalLossRatioMin": hwIplpmGlobalLossRatioMin,
       "hwIplpmGlobalTotalLossPkts": hwIplpmGlobalTotalLossPkts,
       "hwIplpmGlobalTotalRecvPkts": hwIplpmGlobalTotalRecvPkts,
       "hwIplpmGlobalHisRecStartTime": hwIplpmGlobalHisRecStartTime,
       "hwIplpmGlobalHisRecEndTime": hwIplpmGlobalHisRecEndTime,
       "hwIplpmGlobalValidStatDataNum": hwIplpmGlobalValidStatDataNum,
       "hwIplpmLinkHisRecordEntryTable": hwIplpmLinkHisRecordEntryTable,
       "hwIplpmLinkHisRecordEntryEntry": hwIplpmLinkHisRecordEntryEntry,
       "hwIplpmLinkHisRecordNo": hwIplpmLinkHisRecordNo,
       "hwIplpmLinkForwardLossRatioMax": hwIplpmLinkForwardLossRatioMax,
       "hwIplpmLinkForwardLossRatioMin": hwIplpmLinkForwardLossRatioMin,
       "hwIplpmLinkForwardTotalLossPkts": hwIplpmLinkForwardTotalLossPkts,
       "hwIplpmLinkForwardTotalRecvPkts": hwIplpmLinkForwardTotalRecvPkts,
       "hwIplpmLinkBackwardLossRatioMax": hwIplpmLinkBackwardLossRatioMax,
       "hwIplpmLinkBackwardLossRatioMin": hwIplpmLinkBackwardLossRatioMin,
       "hwIplpmLinkBackwardTotalLossPkts": hwIplpmLinkBackwardTotalLossPkts,
       "hwIplpmLinkBackwardTotalRecvPkts": hwIplpmLinkBackwardTotalRecvPkts,
       "hwIplpmLinkHisRecordStartTime": hwIplpmLinkHisRecordStartTime,
       "hwIplpmLinkHisRecordEndTime": hwIplpmLinkHisRecordEndTime,
       "hwIplpmLinkValidStatDataNum": hwIplpmLinkValidStatDataNum,
       "hwIplpmFwdPathSearch": hwIplpmFwdPathSearch,
       "hwIplpmGateWaySearchTable": hwIplpmGateWaySearchTable,
       "hwIplpmGateWaySearchEntry": hwIplpmGateWaySearchEntry,
       "hwIplpmNetAddress": hwIplpmNetAddress,
       "hwIplpmNetMask": hwIplpmNetMask,
       "hwIplpmNetIfIndex": hwIplpmNetIfIndex,
       "hwIplpmNetIfName": hwIplpmNetIfName,
       "hwIplpmNetIfMacAddress": hwIplpmNetIfMacAddress,
       "hwIplpmNetIfAddress": hwIplpmNetIfAddress,
       "hwIplpmNetIfMask": hwIplpmNetIfMask,
       "hwIplpmNetIfVpnName": hwIplpmNetIfVpnName,
       "hwIplpmNetIfVrf": hwIplpmNetIfVrf,
       "hwIplpmNetIfVlan": hwIplpmNetIfVlan,
       "hwIplpmNetSystemMac": hwIplpmNetSystemMac,
       "hwIplpmNetIfVrrpVip": hwIplpmNetIfVrrpVip,
       "hwIplpmNetIfVrrpMac": hwIplpmNetIfVrrpMac,
       "hwIplpmNetIfVrrpState": hwIplpmNetIfVrrpState,
       "hwIplpmNetIfHostAddress": hwIplpmNetIfHostAddress,
       "hwIplpmHostInfoSearchTable": hwIplpmHostInfoSearchTable,
       "hwIplpmHostInfoSearchEntry": hwIplpmHostInfoSearchEntry,
       "hwIplpmHostIpAddress": hwIplpmHostIpAddress,
       "hwIplpmHostVrf": hwIplpmHostVrf,
       "hwIplpmHostIfIndex": hwIplpmHostIfIndex,
       "hwIplpmHostIfName": hwIplpmHostIfName,
       "hwIplpmHostMacAddress": hwIplpmHostMacAddress,
       "hwIplpmHostVlan": hwIplpmHostVlan,
       "hwIplpmHostCeVlan": hwIplpmHostCeVlan,
       "hwIplpmLocalIpSearchTable": hwIplpmLocalIpSearchTable,
       "hwIplpmLocalIpSearchEntry": hwIplpmLocalIpSearchEntry,
       "hwIplpmLocalIpAddress": hwIplpmLocalIpAddress,
       "hwIplpmLocalIfIndex": hwIplpmLocalIfIndex,
       "hwIplpmLocalIfType": hwIplpmLocalIfType,
       "hwIplpmLocalIfVrf": hwIplpmLocalIfVrf,
       "hwIplpmLocalPortList": hwIplpmLocalPortList,
       "hwIplpmIpRouteSearchTable": hwIplpmIpRouteSearchTable,
       "hwIplpmIpRouteSearchEntry": hwIplpmIpRouteSearchEntry,
       "hwIplpmDestIpAddress": hwIplpmDestIpAddress,
       "hwIplpmDestMask": hwIplpmDestMask,
       "hwIplpmDestVrf": hwIplpmDestVrf,
       "hwIplpmRouteDstAddr": hwIplpmRouteDstAddr,
       "hwIplpmRouteDstMask": hwIplpmRouteDstMask,
       "hwIplpmRouteIfIndex": hwIplpmRouteIfIndex,
       "hwIplpmOutPortIfIndex": hwIplpmOutPortIfIndex,
       "hwIplpmTraps": hwIplpmTraps,
       "hwIplpmGlobalLossRatioExceed": hwIplpmGlobalLossRatioExceed,
       "hwIplpmGlobalLossRatioRecovery": hwIplpmGlobalLossRatioRecovery,
       "hwIplpmLinkForwardLossRatioExceed": hwIplpmLinkForwardLossRatioExceed,
       "hwIplpmLinkForwardLossRatioRecovery": hwIplpmLinkForwardLossRatioRecovery,
       "hwIplpmConformance": hwIplpmConformance,
       "hwIplpmCompliances": hwIplpmCompliances,
       "hwIplpmCompliance": hwIplpmCompliance,
       "hwIplpmGroups": hwIplpmGroups,
       "hwIplpmGlobalConfigGroup": hwIplpmGlobalConfigGroup,
       "hwIplpmInterfacelConfigGroup": hwIplpmInterfacelConfigGroup,
       "hwIplpmStatisticsGroup": hwIplpmStatisticsGroup,
       "hwIplpmHistoryRecordGroup": hwIplpmHistoryRecordGroup,
       "hwIplpmFwdPathSearchGroup": hwIplpmFwdPathSearchGroup,
       "hwIplpmTrapsGroup": hwIplpmTrapsGroup}
)
