# SNMP MIB module (TN3270E-RT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TN3270E-RT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:05:29 2024
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

(IANATn3270eAddrType,
 IANATn3270eAddress) = mibBuilder.importSymbols(
    "IANATn3270eTC-MIB",
    "IANATn3270eAddrType",
    "IANATn3270eAddress")

(snanauMIB,) = mibBuilder.importSymbols(
    "SNA-NAU-MIB",
    "snanauMIB")

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

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp")

(tn3270eClientGroupName,
 tn3270eResMapElementType,
 tn3270eSrvrConfIndex) = mibBuilder.importSymbols(
    "TN3270E-MIB",
    "tn3270eClientGroupName",
    "tn3270eResMapElementType",
    "tn3270eSrvrConfIndex")


# MODULE-IDENTITY

tn3270eRtMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 34, 9)
)
tn3270eRtMIB.setRevisions(
        ("2006-01-13 00:00",
         "1998-07-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Tn3270eRtNotifications_ObjectIdentity = ObjectIdentity
tn3270eRtNotifications = _Tn3270eRtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 9, 0)
)
_Tn3270eRtObjects_ObjectIdentity = ObjectIdentity
tn3270eRtObjects = _Tn3270eRtObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 9, 1)
)
_Tn3270eRtCollCtlTable_Object = MibTable
tn3270eRtCollCtlTable = _Tn3270eRtCollCtlTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1)
)
if mibBuilder.loadTexts:
    tn3270eRtCollCtlTable.setStatus("current")
_Tn3270eRtCollCtlEntry_Object = MibTableRow
tn3270eRtCollCtlEntry = _Tn3270eRtCollCtlEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1)
)
tn3270eRtCollCtlEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eSrvrConfIndex"),
    (0, "TN3270E-MIB", "tn3270eClientGroupName"),
)
if mibBuilder.loadTexts:
    tn3270eRtCollCtlEntry.setStatus("current")


class _Tn3270eRtCollCtlType_Type(OctetString):
    """Custom type tn3270eRtCollCtlType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_Tn3270eRtCollCtlType_Type.__name__ = "OctetString"
_Tn3270eRtCollCtlType_Object = MibTableColumn
tn3270eRtCollCtlType = _Tn3270eRtCollCtlType_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 2),
    _Tn3270eRtCollCtlType_Type()
)
tn3270eRtCollCtlType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlType.setStatus("current")


class _Tn3270eRtCollCtlSPeriod_Type(Unsigned32):
    """Custom type tn3270eRtCollCtlSPeriod based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_Tn3270eRtCollCtlSPeriod_Type.__name__ = "Unsigned32"
_Tn3270eRtCollCtlSPeriod_Object = MibTableColumn
tn3270eRtCollCtlSPeriod = _Tn3270eRtCollCtlSPeriod_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 3),
    _Tn3270eRtCollCtlSPeriod_Type()
)
tn3270eRtCollCtlSPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlSPeriod.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlSPeriod.setUnits("seconds")


class _Tn3270eRtCollCtlSPMult_Type(Unsigned32):
    """Custom type tn3270eRtCollCtlSPMult based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5760),
    )


_Tn3270eRtCollCtlSPMult_Type.__name__ = "Unsigned32"
_Tn3270eRtCollCtlSPMult_Object = MibTableColumn
tn3270eRtCollCtlSPMult = _Tn3270eRtCollCtlSPMult_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 4),
    _Tn3270eRtCollCtlSPMult_Type()
)
tn3270eRtCollCtlSPMult.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlSPMult.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlSPMult.setUnits("period")


class _Tn3270eRtCollCtlThreshHigh_Type(Unsigned32):
    """Custom type tn3270eRtCollCtlThreshHigh based on Unsigned32"""
    defaultValue = 0


_Tn3270eRtCollCtlThreshHigh_Object = MibTableColumn
tn3270eRtCollCtlThreshHigh = _Tn3270eRtCollCtlThreshHigh_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 5),
    _Tn3270eRtCollCtlThreshHigh_Type()
)
tn3270eRtCollCtlThreshHigh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlThreshHigh.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlThreshHigh.setUnits("seconds")


class _Tn3270eRtCollCtlThreshLow_Type(Unsigned32):
    """Custom type tn3270eRtCollCtlThreshLow based on Unsigned32"""
    defaultValue = 0


_Tn3270eRtCollCtlThreshLow_Object = MibTableColumn
tn3270eRtCollCtlThreshLow = _Tn3270eRtCollCtlThreshLow_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 6),
    _Tn3270eRtCollCtlThreshLow_Type()
)
tn3270eRtCollCtlThreshLow.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlThreshLow.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlThreshLow.setUnits("seconds")


class _Tn3270eRtCollCtlIdleCount_Type(Unsigned32):
    """Custom type tn3270eRtCollCtlIdleCount based on Unsigned32"""
    defaultValue = 1


_Tn3270eRtCollCtlIdleCount_Object = MibTableColumn
tn3270eRtCollCtlIdleCount = _Tn3270eRtCollCtlIdleCount_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 7),
    _Tn3270eRtCollCtlIdleCount_Type()
)
tn3270eRtCollCtlIdleCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlIdleCount.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlIdleCount.setUnits("transactions")


class _Tn3270eRtCollCtlBucketBndry1_Type(Unsigned32):
    """Custom type tn3270eRtCollCtlBucketBndry1 based on Unsigned32"""
    defaultValue = 10


_Tn3270eRtCollCtlBucketBndry1_Object = MibTableColumn
tn3270eRtCollCtlBucketBndry1 = _Tn3270eRtCollCtlBucketBndry1_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 8),
    _Tn3270eRtCollCtlBucketBndry1_Type()
)
tn3270eRtCollCtlBucketBndry1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlBucketBndry1.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlBucketBndry1.setUnits("tenths of seconds")


class _Tn3270eRtCollCtlBucketBndry2_Type(Unsigned32):
    """Custom type tn3270eRtCollCtlBucketBndry2 based on Unsigned32"""
    defaultValue = 20


_Tn3270eRtCollCtlBucketBndry2_Object = MibTableColumn
tn3270eRtCollCtlBucketBndry2 = _Tn3270eRtCollCtlBucketBndry2_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 9),
    _Tn3270eRtCollCtlBucketBndry2_Type()
)
tn3270eRtCollCtlBucketBndry2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlBucketBndry2.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlBucketBndry2.setUnits("tenths of seconds")


class _Tn3270eRtCollCtlBucketBndry3_Type(Unsigned32):
    """Custom type tn3270eRtCollCtlBucketBndry3 based on Unsigned32"""
    defaultValue = 50


_Tn3270eRtCollCtlBucketBndry3_Object = MibTableColumn
tn3270eRtCollCtlBucketBndry3 = _Tn3270eRtCollCtlBucketBndry3_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 10),
    _Tn3270eRtCollCtlBucketBndry3_Type()
)
tn3270eRtCollCtlBucketBndry3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlBucketBndry3.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlBucketBndry3.setUnits("tenths of seconds")


class _Tn3270eRtCollCtlBucketBndry4_Type(Unsigned32):
    """Custom type tn3270eRtCollCtlBucketBndry4 based on Unsigned32"""
    defaultValue = 100


_Tn3270eRtCollCtlBucketBndry4_Object = MibTableColumn
tn3270eRtCollCtlBucketBndry4 = _Tn3270eRtCollCtlBucketBndry4_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 11),
    _Tn3270eRtCollCtlBucketBndry4_Type()
)
tn3270eRtCollCtlBucketBndry4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlBucketBndry4.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlBucketBndry4.setUnits("tenths of seconds")
_Tn3270eRtCollCtlRowStatus_Type = RowStatus
_Tn3270eRtCollCtlRowStatus_Object = MibTableColumn
tn3270eRtCollCtlRowStatus = _Tn3270eRtCollCtlRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 1, 1, 12),
    _Tn3270eRtCollCtlRowStatus_Type()
)
tn3270eRtCollCtlRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tn3270eRtCollCtlRowStatus.setStatus("current")
_Tn3270eRtDataTable_Object = MibTable
tn3270eRtDataTable = _Tn3270eRtDataTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2)
)
if mibBuilder.loadTexts:
    tn3270eRtDataTable.setStatus("current")
_Tn3270eRtDataEntry_Object = MibTableRow
tn3270eRtDataEntry = _Tn3270eRtDataEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1)
)
tn3270eRtDataEntry.setIndexNames(
    (0, "TN3270E-MIB", "tn3270eSrvrConfIndex"),
    (0, "TN3270E-MIB", "tn3270eClientGroupName"),
    (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddrType"),
    (0, "TN3270E-RT-MIB", "tn3270eRtDataClientAddress"),
    (0, "TN3270E-RT-MIB", "tn3270eRtDataClientPort"),
)
if mibBuilder.loadTexts:
    tn3270eRtDataEntry.setStatus("current")
_Tn3270eRtDataClientAddrType_Type = IANATn3270eAddrType
_Tn3270eRtDataClientAddrType_Object = MibTableColumn
tn3270eRtDataClientAddrType = _Tn3270eRtDataClientAddrType_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 1),
    _Tn3270eRtDataClientAddrType_Type()
)
tn3270eRtDataClientAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eRtDataClientAddrType.setStatus("current")
_Tn3270eRtDataClientAddress_Type = IANATn3270eAddress
_Tn3270eRtDataClientAddress_Object = MibTableColumn
tn3270eRtDataClientAddress = _Tn3270eRtDataClientAddress_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 2),
    _Tn3270eRtDataClientAddress_Type()
)
tn3270eRtDataClientAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eRtDataClientAddress.setStatus("current")


class _Tn3270eRtDataClientPort_Type(Unsigned32):
    """Custom type tn3270eRtDataClientPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Tn3270eRtDataClientPort_Type.__name__ = "Unsigned32"
_Tn3270eRtDataClientPort_Object = MibTableColumn
tn3270eRtDataClientPort = _Tn3270eRtDataClientPort_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 3),
    _Tn3270eRtDataClientPort_Type()
)
tn3270eRtDataClientPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tn3270eRtDataClientPort.setStatus("current")


class _Tn3270eRtDataAvgRt_Type(Gauge32):
    """Custom type tn3270eRtDataAvgRt based on Gauge32"""
    defaultValue = 0


_Tn3270eRtDataAvgRt_Object = MibTableColumn
tn3270eRtDataAvgRt = _Tn3270eRtDataAvgRt_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 4),
    _Tn3270eRtDataAvgRt_Type()
)
tn3270eRtDataAvgRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataAvgRt.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtDataAvgRt.setUnits("tenths of seconds")


class _Tn3270eRtDataAvgIpRt_Type(Gauge32):
    """Custom type tn3270eRtDataAvgIpRt based on Gauge32"""
    defaultValue = 0


_Tn3270eRtDataAvgIpRt_Object = MibTableColumn
tn3270eRtDataAvgIpRt = _Tn3270eRtDataAvgIpRt_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 5),
    _Tn3270eRtDataAvgIpRt_Type()
)
tn3270eRtDataAvgIpRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataAvgIpRt.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtDataAvgIpRt.setUnits("tenths of seconds")
_Tn3270eRtDataAvgCountTrans_Type = Gauge32
_Tn3270eRtDataAvgCountTrans_Object = MibTableColumn
tn3270eRtDataAvgCountTrans = _Tn3270eRtDataAvgCountTrans_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 6),
    _Tn3270eRtDataAvgCountTrans_Type()
)
tn3270eRtDataAvgCountTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataAvgCountTrans.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtDataAvgCountTrans.setUnits("transactions")
_Tn3270eRtDataIntTimeStamp_Type = DateAndTime
_Tn3270eRtDataIntTimeStamp_Object = MibTableColumn
tn3270eRtDataIntTimeStamp = _Tn3270eRtDataIntTimeStamp_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 7),
    _Tn3270eRtDataIntTimeStamp_Type()
)
tn3270eRtDataIntTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataIntTimeStamp.setStatus("current")
_Tn3270eRtDataTotalRts_Type = Counter32
_Tn3270eRtDataTotalRts_Object = MibTableColumn
tn3270eRtDataTotalRts = _Tn3270eRtDataTotalRts_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 8),
    _Tn3270eRtDataTotalRts_Type()
)
tn3270eRtDataTotalRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataTotalRts.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtDataTotalRts.setUnits("tenths of seconds")
_Tn3270eRtDataTotalIpRts_Type = Counter32
_Tn3270eRtDataTotalIpRts_Object = MibTableColumn
tn3270eRtDataTotalIpRts = _Tn3270eRtDataTotalIpRts_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 9),
    _Tn3270eRtDataTotalIpRts_Type()
)
tn3270eRtDataTotalIpRts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataTotalIpRts.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtDataTotalIpRts.setUnits("tenths of seconds")
_Tn3270eRtDataCountTrans_Type = Counter32
_Tn3270eRtDataCountTrans_Object = MibTableColumn
tn3270eRtDataCountTrans = _Tn3270eRtDataCountTrans_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 10),
    _Tn3270eRtDataCountTrans_Type()
)
tn3270eRtDataCountTrans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataCountTrans.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtDataCountTrans.setUnits("transactions")
_Tn3270eRtDataCountDrs_Type = Counter32
_Tn3270eRtDataCountDrs_Object = MibTableColumn
tn3270eRtDataCountDrs = _Tn3270eRtDataCountDrs_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 11),
    _Tn3270eRtDataCountDrs_Type()
)
tn3270eRtDataCountDrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataCountDrs.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtDataCountDrs.setUnits("definite responses")


class _Tn3270eRtDataElapsRndTrpSq_Type(Unsigned32):
    """Custom type tn3270eRtDataElapsRndTrpSq based on Unsigned32"""
    defaultValue = 0


_Tn3270eRtDataElapsRndTrpSq_Object = MibTableColumn
tn3270eRtDataElapsRndTrpSq = _Tn3270eRtDataElapsRndTrpSq_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 12),
    _Tn3270eRtDataElapsRndTrpSq_Type()
)
tn3270eRtDataElapsRndTrpSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataElapsRndTrpSq.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtDataElapsRndTrpSq.setUnits("tenths of seconds squared")


class _Tn3270eRtDataElapsIpRtSq_Type(Unsigned32):
    """Custom type tn3270eRtDataElapsIpRtSq based on Unsigned32"""
    defaultValue = 0


_Tn3270eRtDataElapsIpRtSq_Object = MibTableColumn
tn3270eRtDataElapsIpRtSq = _Tn3270eRtDataElapsIpRtSq_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 13),
    _Tn3270eRtDataElapsIpRtSq_Type()
)
tn3270eRtDataElapsIpRtSq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataElapsIpRtSq.setStatus("current")
if mibBuilder.loadTexts:
    tn3270eRtDataElapsIpRtSq.setUnits("tenths of seconds squared")
_Tn3270eRtDataBucket1Rts_Type = Counter32
_Tn3270eRtDataBucket1Rts_Object = MibTableColumn
tn3270eRtDataBucket1Rts = _Tn3270eRtDataBucket1Rts_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 14),
    _Tn3270eRtDataBucket1Rts_Type()
)
tn3270eRtDataBucket1Rts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataBucket1Rts.setStatus("current")
_Tn3270eRtDataBucket2Rts_Type = Counter32
_Tn3270eRtDataBucket2Rts_Object = MibTableColumn
tn3270eRtDataBucket2Rts = _Tn3270eRtDataBucket2Rts_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 15),
    _Tn3270eRtDataBucket2Rts_Type()
)
tn3270eRtDataBucket2Rts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataBucket2Rts.setStatus("current")
_Tn3270eRtDataBucket3Rts_Type = Counter32
_Tn3270eRtDataBucket3Rts_Object = MibTableColumn
tn3270eRtDataBucket3Rts = _Tn3270eRtDataBucket3Rts_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 16),
    _Tn3270eRtDataBucket3Rts_Type()
)
tn3270eRtDataBucket3Rts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataBucket3Rts.setStatus("current")
_Tn3270eRtDataBucket4Rts_Type = Counter32
_Tn3270eRtDataBucket4Rts_Object = MibTableColumn
tn3270eRtDataBucket4Rts = _Tn3270eRtDataBucket4Rts_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 17),
    _Tn3270eRtDataBucket4Rts_Type()
)
tn3270eRtDataBucket4Rts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataBucket4Rts.setStatus("current")
_Tn3270eRtDataBucket5Rts_Type = Counter32
_Tn3270eRtDataBucket5Rts_Object = MibTableColumn
tn3270eRtDataBucket5Rts = _Tn3270eRtDataBucket5Rts_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 18),
    _Tn3270eRtDataBucket5Rts_Type()
)
tn3270eRtDataBucket5Rts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataBucket5Rts.setStatus("current")


class _Tn3270eRtDataRtMethod_Type(Integer32):
    """Custom type tn3270eRtDataRtMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("responses", 1),
          ("timingMark", 2))
    )


_Tn3270eRtDataRtMethod_Type.__name__ = "Integer32"
_Tn3270eRtDataRtMethod_Object = MibTableColumn
tn3270eRtDataRtMethod = _Tn3270eRtDataRtMethod_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 19),
    _Tn3270eRtDataRtMethod_Type()
)
tn3270eRtDataRtMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataRtMethod.setStatus("current")
_Tn3270eRtDataDiscontinuityTime_Type = TimeStamp
_Tn3270eRtDataDiscontinuityTime_Object = MibTableColumn
tn3270eRtDataDiscontinuityTime = _Tn3270eRtDataDiscontinuityTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 2, 1, 20),
    _Tn3270eRtDataDiscontinuityTime_Type()
)
tn3270eRtDataDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tn3270eRtDataDiscontinuityTime.setStatus("current")
_Tn3270eRtSpinLock_Type = TestAndIncr
_Tn3270eRtSpinLock_Object = MibScalar
tn3270eRtSpinLock = _Tn3270eRtSpinLock_Object(
    (1, 3, 6, 1, 2, 1, 34, 9, 1, 3),
    _Tn3270eRtSpinLock_Type()
)
tn3270eRtSpinLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tn3270eRtSpinLock.setStatus("current")
_Tn3270eRtConformance_ObjectIdentity = ObjectIdentity
tn3270eRtConformance = _Tn3270eRtConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 9, 3)
)
_Tn3270eRtGroups_ObjectIdentity = ObjectIdentity
tn3270eRtGroups = _Tn3270eRtGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 9, 3, 1)
)
_Tn3270eRtCompliances_ObjectIdentity = ObjectIdentity
tn3270eRtCompliances = _Tn3270eRtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 9, 3, 2)
)

# Managed Objects groups

tn3270eRtGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 1)
)
tn3270eRtGroup.setObjects(
      *(("TN3270E-RT-MIB", "tn3270eRtCollCtlType"),
        ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPeriod"),
        ("TN3270E-RT-MIB", "tn3270eRtCollCtlSPMult"),
        ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshHigh"),
        ("TN3270E-RT-MIB", "tn3270eRtCollCtlThreshLow"),
        ("TN3270E-RT-MIB", "tn3270eRtCollCtlIdleCount"),
        ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry1"),
        ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry2"),
        ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry3"),
        ("TN3270E-RT-MIB", "tn3270eRtCollCtlBucketBndry4"),
        ("TN3270E-RT-MIB", "tn3270eRtCollCtlRowStatus"),
        ("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"),
        ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"),
        ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"),
        ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"),
        ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"),
        ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"),
        ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"),
        ("TN3270E-RT-MIB", "tn3270eRtSpinLock"))
)
if mibBuilder.loadTexts:
    tn3270eRtGroup.setStatus("current")


# Notification objects

tn3270eRtExceeded = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 9, 0, 1)
)
tn3270eRtExceeded.setObjects(
      *(("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"),
        ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"))
)
if mibBuilder.loadTexts:
    tn3270eRtExceeded.setStatus(
        "current"
    )

tn3270eRtOkay = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 9, 0, 2)
)
tn3270eRtOkay.setObjects(
      *(("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"),
        ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"))
)
if mibBuilder.loadTexts:
    tn3270eRtOkay.setStatus(
        "current"
    )

tn3270eRtCollStart = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 9, 0, 3)
)
tn3270eRtCollStart.setObjects(
      *(("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"),
        ("TN3270E-MIB", "tn3270eResMapElementType"))
)
if mibBuilder.loadTexts:
    tn3270eRtCollStart.setStatus(
        "current"
    )

tn3270eRtCollEnd = NotificationType(
    (1, 3, 6, 1, 2, 1, 34, 9, 0, 4)
)
tn3270eRtCollEnd.setObjects(
      *(("TN3270E-RT-MIB", "tn3270eRtDataDiscontinuityTime"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgRt"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgIpRt"),
        ("TN3270E-RT-MIB", "tn3270eRtDataAvgCountTrans"),
        ("TN3270E-RT-MIB", "tn3270eRtDataIntTimeStamp"),
        ("TN3270E-RT-MIB", "tn3270eRtDataTotalRts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataTotalIpRts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataCountTrans"),
        ("TN3270E-RT-MIB", "tn3270eRtDataCountDrs"),
        ("TN3270E-RT-MIB", "tn3270eRtDataElapsRndTrpSq"),
        ("TN3270E-RT-MIB", "tn3270eRtDataElapsIpRtSq"),
        ("TN3270E-RT-MIB", "tn3270eRtDataBucket1Rts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataBucket2Rts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataBucket3Rts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataBucket4Rts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataBucket5Rts"),
        ("TN3270E-RT-MIB", "tn3270eRtDataRtMethod"))
)
if mibBuilder.loadTexts:
    tn3270eRtCollEnd.setStatus(
        "current"
    )


# Notifications groups

tn3270eRtNotGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 34, 9, 3, 1, 2)
)
tn3270eRtNotGroup.setObjects(
      *(("TN3270E-RT-MIB", "tn3270eRtExceeded"),
        ("TN3270E-RT-MIB", "tn3270eRtOkay"),
        ("TN3270E-RT-MIB", "tn3270eRtCollStart"),
        ("TN3270E-RT-MIB", "tn3270eRtCollEnd"))
)
if mibBuilder.loadTexts:
    tn3270eRtNotGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tn3270eRtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 9, 3, 2, 1)
)
if mibBuilder.loadTexts:
    tn3270eRtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN3270E-RT-MIB",
    **{"tn3270eRtMIB": tn3270eRtMIB,
       "tn3270eRtNotifications": tn3270eRtNotifications,
       "tn3270eRtExceeded": tn3270eRtExceeded,
       "tn3270eRtOkay": tn3270eRtOkay,
       "tn3270eRtCollStart": tn3270eRtCollStart,
       "tn3270eRtCollEnd": tn3270eRtCollEnd,
       "tn3270eRtObjects": tn3270eRtObjects,
       "tn3270eRtCollCtlTable": tn3270eRtCollCtlTable,
       "tn3270eRtCollCtlEntry": tn3270eRtCollCtlEntry,
       "tn3270eRtCollCtlType": tn3270eRtCollCtlType,
       "tn3270eRtCollCtlSPeriod": tn3270eRtCollCtlSPeriod,
       "tn3270eRtCollCtlSPMult": tn3270eRtCollCtlSPMult,
       "tn3270eRtCollCtlThreshHigh": tn3270eRtCollCtlThreshHigh,
       "tn3270eRtCollCtlThreshLow": tn3270eRtCollCtlThreshLow,
       "tn3270eRtCollCtlIdleCount": tn3270eRtCollCtlIdleCount,
       "tn3270eRtCollCtlBucketBndry1": tn3270eRtCollCtlBucketBndry1,
       "tn3270eRtCollCtlBucketBndry2": tn3270eRtCollCtlBucketBndry2,
       "tn3270eRtCollCtlBucketBndry3": tn3270eRtCollCtlBucketBndry3,
       "tn3270eRtCollCtlBucketBndry4": tn3270eRtCollCtlBucketBndry4,
       "tn3270eRtCollCtlRowStatus": tn3270eRtCollCtlRowStatus,
       "tn3270eRtDataTable": tn3270eRtDataTable,
       "tn3270eRtDataEntry": tn3270eRtDataEntry,
       "tn3270eRtDataClientAddrType": tn3270eRtDataClientAddrType,
       "tn3270eRtDataClientAddress": tn3270eRtDataClientAddress,
       "tn3270eRtDataClientPort": tn3270eRtDataClientPort,
       "tn3270eRtDataAvgRt": tn3270eRtDataAvgRt,
       "tn3270eRtDataAvgIpRt": tn3270eRtDataAvgIpRt,
       "tn3270eRtDataAvgCountTrans": tn3270eRtDataAvgCountTrans,
       "tn3270eRtDataIntTimeStamp": tn3270eRtDataIntTimeStamp,
       "tn3270eRtDataTotalRts": tn3270eRtDataTotalRts,
       "tn3270eRtDataTotalIpRts": tn3270eRtDataTotalIpRts,
       "tn3270eRtDataCountTrans": tn3270eRtDataCountTrans,
       "tn3270eRtDataCountDrs": tn3270eRtDataCountDrs,
       "tn3270eRtDataElapsRndTrpSq": tn3270eRtDataElapsRndTrpSq,
       "tn3270eRtDataElapsIpRtSq": tn3270eRtDataElapsIpRtSq,
       "tn3270eRtDataBucket1Rts": tn3270eRtDataBucket1Rts,
       "tn3270eRtDataBucket2Rts": tn3270eRtDataBucket2Rts,
       "tn3270eRtDataBucket3Rts": tn3270eRtDataBucket3Rts,
       "tn3270eRtDataBucket4Rts": tn3270eRtDataBucket4Rts,
       "tn3270eRtDataBucket5Rts": tn3270eRtDataBucket5Rts,
       "tn3270eRtDataRtMethod": tn3270eRtDataRtMethod,
       "tn3270eRtDataDiscontinuityTime": tn3270eRtDataDiscontinuityTime,
       "tn3270eRtSpinLock": tn3270eRtSpinLock,
       "tn3270eRtConformance": tn3270eRtConformance,
       "tn3270eRtGroups": tn3270eRtGroups,
       "tn3270eRtGroup": tn3270eRtGroup,
       "tn3270eRtNotGroup": tn3270eRtNotGroup,
       "tn3270eRtCompliances": tn3270eRtCompliances,
       "tn3270eRtCompliance": tn3270eRtCompliance}
)
