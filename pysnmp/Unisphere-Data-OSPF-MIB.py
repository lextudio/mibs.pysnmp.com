# SNMP MIB module (Unisphere-Data-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:12 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ospfAddressLessIf,
 ospfAreaEntry,
 ospfIfEntry,
 ospfIfIpAddress,
 ospfNbrEntry,
 ospfVirtIfEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "ospfAddressLessIf",
    "ospfAreaEntry",
    "ospfIfEntry",
    "ospfIfIpAddress",
    "ospfNbrEntry",
    "ospfVirtIfEntry")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdOspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14)
)
usdOspfMIB.setRevisions(
        ("2002-04-05 21:20",
         "2000-05-23 00:00",
         "1999-09-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_UsdOspfObjects_ObjectIdentity = ObjectIdentity
usdOspfObjects = _UsdOspfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1)
)
_UsdOspfGeneralGroup_ObjectIdentity = ObjectIdentity
usdOspfGeneralGroup = _UsdOspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1)
)


class _UsdOspfProcessId_Type(Integer32):
    """Custom type usdOspfProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_UsdOspfProcessId_Type.__name__ = "Integer32"
_UsdOspfProcessId_Object = MibScalar
usdOspfProcessId = _UsdOspfProcessId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 1),
    _UsdOspfProcessId_Type()
)
usdOspfProcessId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfProcessId.setStatus("current")


class _UsdOspfMaxPathSplits_Type(Integer32):
    """Custom type usdOspfMaxPathSplits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_UsdOspfMaxPathSplits_Type.__name__ = "Integer32"
_UsdOspfMaxPathSplits_Object = MibScalar
usdOspfMaxPathSplits = _UsdOspfMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 2),
    _UsdOspfMaxPathSplits_Type()
)
usdOspfMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfMaxPathSplits.setStatus("current")


class _UsdOspfSpfHoldInterval_Type(Integer32):
    """Custom type usdOspfSpfHoldInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_UsdOspfSpfHoldInterval_Type.__name__ = "Integer32"
_UsdOspfSpfHoldInterval_Object = MibScalar
usdOspfSpfHoldInterval = _UsdOspfSpfHoldInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 3),
    _UsdOspfSpfHoldInterval_Type()
)
usdOspfSpfHoldInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfSpfHoldInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdOspfSpfHoldInterval.setUnits("seconds")
_UsdOspfNumActiveAreas_Type = Counter32
_UsdOspfNumActiveAreas_Object = MibScalar
usdOspfNumActiveAreas = _UsdOspfNumActiveAreas_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 4),
    _UsdOspfNumActiveAreas_Type()
)
usdOspfNumActiveAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfNumActiveAreas.setStatus("current")
_UsdOspfSpfTime_Type = Counter32
_UsdOspfSpfTime_Object = MibScalar
usdOspfSpfTime = _UsdOspfSpfTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 5),
    _UsdOspfSpfTime_Type()
)
usdOspfSpfTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfSpfTime.setStatus("current")


class _UsdOspfRefBw_Type(Unsigned32):
    """Custom type usdOspfRefBw based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_UsdOspfRefBw_Type.__name__ = "Unsigned32"
_UsdOspfRefBw_Object = MibScalar
usdOspfRefBw = _UsdOspfRefBw_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 6),
    _UsdOspfRefBw_Type()
)
usdOspfRefBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfRefBw.setStatus("current")
if mibBuilder.loadTexts:
    usdOspfRefBw.setUnits("bits per second")
_UsdOspfAutoVlink_Type = TruthValue
_UsdOspfAutoVlink_Object = MibScalar
usdOspfAutoVlink = _UsdOspfAutoVlink_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 7),
    _UsdOspfAutoVlink_Type()
)
usdOspfAutoVlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfAutoVlink.setStatus("current")


class _UsdOspfIntraDistance_Type(Integer32):
    """Custom type usdOspfIntraDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdOspfIntraDistance_Type.__name__ = "Integer32"
_UsdOspfIntraDistance_Object = MibScalar
usdOspfIntraDistance = _UsdOspfIntraDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 8),
    _UsdOspfIntraDistance_Type()
)
usdOspfIntraDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfIntraDistance.setStatus("current")


class _UsdOspfInterDistance_Type(Integer32):
    """Custom type usdOspfInterDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdOspfInterDistance_Type.__name__ = "Integer32"
_UsdOspfInterDistance_Object = MibScalar
usdOspfInterDistance = _UsdOspfInterDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 9),
    _UsdOspfInterDistance_Type()
)
usdOspfInterDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfInterDistance.setStatus("current")


class _UsdOspfExtDistance_Type(Integer32):
    """Custom type usdOspfExtDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UsdOspfExtDistance_Type.__name__ = "Integer32"
_UsdOspfExtDistance_Object = MibScalar
usdOspfExtDistance = _UsdOspfExtDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 10),
    _UsdOspfExtDistance_Type()
)
usdOspfExtDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfExtDistance.setStatus("current")
_UsdOspfHelloPktsRcv_Type = Counter32
_UsdOspfHelloPktsRcv_Object = MibScalar
usdOspfHelloPktsRcv = _UsdOspfHelloPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 11),
    _UsdOspfHelloPktsRcv_Type()
)
usdOspfHelloPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfHelloPktsRcv.setStatus("current")
_UsdOspfDDPktsRcv_Type = Counter32
_UsdOspfDDPktsRcv_Object = MibScalar
usdOspfDDPktsRcv = _UsdOspfDDPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 12),
    _UsdOspfDDPktsRcv_Type()
)
usdOspfDDPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfDDPktsRcv.setStatus("current")
_UsdOspfLsrPktsRcv_Type = Counter32
_UsdOspfLsrPktsRcv_Object = MibScalar
usdOspfLsrPktsRcv = _UsdOspfLsrPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 13),
    _UsdOspfLsrPktsRcv_Type()
)
usdOspfLsrPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfLsrPktsRcv.setStatus("current")
_UsdOspfLsuPktsRcv_Type = Counter32
_UsdOspfLsuPktsRcv_Object = MibScalar
usdOspfLsuPktsRcv = _UsdOspfLsuPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 14),
    _UsdOspfLsuPktsRcv_Type()
)
usdOspfLsuPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfLsuPktsRcv.setStatus("current")
_UsdOspfLsAckPktsRcv_Type = Counter32
_UsdOspfLsAckPktsRcv_Object = MibScalar
usdOspfLsAckPktsRcv = _UsdOspfLsAckPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 15),
    _UsdOspfLsAckPktsRcv_Type()
)
usdOspfLsAckPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfLsAckPktsRcv.setStatus("current")
_UsdOspfTotalRcv_Type = Counter32
_UsdOspfTotalRcv_Object = MibScalar
usdOspfTotalRcv = _UsdOspfTotalRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 16),
    _UsdOspfTotalRcv_Type()
)
usdOspfTotalRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfTotalRcv.setStatus("current")
_UsdOspfLsaDiscardCnt_Type = Counter32
_UsdOspfLsaDiscardCnt_Object = MibScalar
usdOspfLsaDiscardCnt = _UsdOspfLsaDiscardCnt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 17),
    _UsdOspfLsaDiscardCnt_Type()
)
usdOspfLsaDiscardCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfLsaDiscardCnt.setStatus("current")
_UsdOspfHelloPktsSent_Type = Counter32
_UsdOspfHelloPktsSent_Object = MibScalar
usdOspfHelloPktsSent = _UsdOspfHelloPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 18),
    _UsdOspfHelloPktsSent_Type()
)
usdOspfHelloPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfHelloPktsSent.setStatus("current")
_UsdOspfDDPktsSent_Type = Counter32
_UsdOspfDDPktsSent_Object = MibScalar
usdOspfDDPktsSent = _UsdOspfDDPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 19),
    _UsdOspfDDPktsSent_Type()
)
usdOspfDDPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfDDPktsSent.setStatus("current")
_UsdOspfLsrPktsSent_Type = Counter32
_UsdOspfLsrPktsSent_Object = MibScalar
usdOspfLsrPktsSent = _UsdOspfLsrPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 20),
    _UsdOspfLsrPktsSent_Type()
)
usdOspfLsrPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfLsrPktsSent.setStatus("current")
_UsdOspfLsuPktsSent_Type = Counter32
_UsdOspfLsuPktsSent_Object = MibScalar
usdOspfLsuPktsSent = _UsdOspfLsuPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 21),
    _UsdOspfLsuPktsSent_Type()
)
usdOspfLsuPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfLsuPktsSent.setStatus("current")
_UsdOspfLsAckPktsSent_Type = Counter32
_UsdOspfLsAckPktsSent_Object = MibScalar
usdOspfLsAckPktsSent = _UsdOspfLsAckPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 22),
    _UsdOspfLsAckPktsSent_Type()
)
usdOspfLsAckPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfLsAckPktsSent.setStatus("current")
_UsdOspfErrPktsSent_Type = Counter32
_UsdOspfErrPktsSent_Object = MibScalar
usdOspfErrPktsSent = _UsdOspfErrPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 23),
    _UsdOspfErrPktsSent_Type()
)
usdOspfErrPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfErrPktsSent.setStatus("current")
_UsdOspfTotalSent_Type = Counter32
_UsdOspfTotalSent_Object = MibScalar
usdOspfTotalSent = _UsdOspfTotalSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 24),
    _UsdOspfTotalSent_Type()
)
usdOspfTotalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfTotalSent.setStatus("current")
_UsdOspfCsumErrPkts_Type = Counter32
_UsdOspfCsumErrPkts_Object = MibScalar
usdOspfCsumErrPkts = _UsdOspfCsumErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 25),
    _UsdOspfCsumErrPkts_Type()
)
usdOspfCsumErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfCsumErrPkts.setStatus("current")
_UsdOspfAllocFailNbr_Type = Counter32
_UsdOspfAllocFailNbr_Object = MibScalar
usdOspfAllocFailNbr = _UsdOspfAllocFailNbr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 26),
    _UsdOspfAllocFailNbr_Type()
)
usdOspfAllocFailNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfAllocFailNbr.setStatus("current")
_UsdOspfAllocFailLsa_Type = Counter32
_UsdOspfAllocFailLsa_Object = MibScalar
usdOspfAllocFailLsa = _UsdOspfAllocFailLsa_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 27),
    _UsdOspfAllocFailLsa_Type()
)
usdOspfAllocFailLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfAllocFailLsa.setStatus("current")
_UsdOspfAllocFailLsd_Type = Counter32
_UsdOspfAllocFailLsd_Object = MibScalar
usdOspfAllocFailLsd = _UsdOspfAllocFailLsd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 28),
    _UsdOspfAllocFailLsd_Type()
)
usdOspfAllocFailLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfAllocFailLsd.setStatus("current")
_UsdOspfAllocFailDbRequest_Type = Counter32
_UsdOspfAllocFailDbRequest_Object = MibScalar
usdOspfAllocFailDbRequest = _UsdOspfAllocFailDbRequest_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 29),
    _UsdOspfAllocFailDbRequest_Type()
)
usdOspfAllocFailDbRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfAllocFailDbRequest.setStatus("current")
_UsdOspfAllocFailRtx_Type = Counter32
_UsdOspfAllocFailRtx_Object = MibScalar
usdOspfAllocFailRtx = _UsdOspfAllocFailRtx_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 30),
    _UsdOspfAllocFailRtx_Type()
)
usdOspfAllocFailRtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfAllocFailRtx.setStatus("current")
_UsdOspfAllocFailAck_Type = Counter32
_UsdOspfAllocFailAck_Object = MibScalar
usdOspfAllocFailAck = _UsdOspfAllocFailAck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 31),
    _UsdOspfAllocFailAck_Type()
)
usdOspfAllocFailAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfAllocFailAck.setStatus("current")
_UsdOspfAllocFailDbPkt_Type = Counter32
_UsdOspfAllocFailDbPkt_Object = MibScalar
usdOspfAllocFailDbPkt = _UsdOspfAllocFailDbPkt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 32),
    _UsdOspfAllocFailDbPkt_Type()
)
usdOspfAllocFailDbPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfAllocFailDbPkt.setStatus("current")
_UsdOspfAllocFailCirc_Type = Counter32
_UsdOspfAllocFailCirc_Object = MibScalar
usdOspfAllocFailCirc = _UsdOspfAllocFailCirc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 33),
    _UsdOspfAllocFailCirc_Type()
)
usdOspfAllocFailCirc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfAllocFailCirc.setStatus("current")
_UsdOspfAllocFailPkt_Type = Counter32
_UsdOspfAllocFailPkt_Object = MibScalar
usdOspfAllocFailPkt = _UsdOspfAllocFailPkt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 34),
    _UsdOspfAllocFailPkt_Type()
)
usdOspfAllocFailPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfAllocFailPkt.setStatus("current")
_UsdOspfOperState_Type = TruthValue
_UsdOspfOperState_Object = MibScalar
usdOspfOperState = _UsdOspfOperState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 35),
    _UsdOspfOperState_Type()
)
usdOspfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfOperState.setStatus("current")


class _UsdOspfVpnRouteTag_Type(Unsigned32):
    """Custom type usdOspfVpnRouteTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_UsdOspfVpnRouteTag_Type.__name__ = "Unsigned32"
_UsdOspfVpnRouteTag_Object = MibScalar
usdOspfVpnRouteTag = _UsdOspfVpnRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 36),
    _UsdOspfVpnRouteTag_Type()
)
usdOspfVpnRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfVpnRouteTag.setStatus("current")


class _UsdOspfDomainId_Type(Unsigned32):
    """Custom type usdOspfDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_UsdOspfDomainId_Type.__name__ = "Unsigned32"
_UsdOspfDomainId_Object = MibScalar
usdOspfDomainId = _UsdOspfDomainId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 37),
    _UsdOspfDomainId_Type()
)
usdOspfDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfDomainId.setStatus("current")
_UsdOspfMplsTeRtrIdIfIndex_Type = InterfaceIndex
_UsdOspfMplsTeRtrIdIfIndex_Object = MibScalar
usdOspfMplsTeRtrIdIfIndex = _UsdOspfMplsTeRtrIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 38),
    _UsdOspfMplsTeRtrIdIfIndex_Type()
)
usdOspfMplsTeRtrIdIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfMplsTeRtrIdIfIndex.setStatus("current")
_UsdOspfAreaTable_Object = MibTable
usdOspfAreaTable = _UsdOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    usdOspfAreaTable.setStatus("current")
_UsdOspfAreaEntry_Object = MibTableRow
usdOspfAreaEntry = _UsdOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    usdOspfAreaEntry.setStatus("current")


class _UsdOspfAreaType_Type(Integer32):
    """Custom type usdOspfAreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nssaArea", 3),
          ("stubArea", 2),
          ("transitArea", 1))
    )


_UsdOspfAreaType_Type.__name__ = "Integer32"
_UsdOspfAreaType_Object = MibTableColumn
usdOspfAreaType = _UsdOspfAreaType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 2, 1, 1),
    _UsdOspfAreaType_Type()
)
usdOspfAreaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfAreaType.setStatus("current")
_UsdOspfAreaTeCapable_Type = TruthValue
_UsdOspfAreaTeCapable_Object = MibTableColumn
usdOspfAreaTeCapable = _UsdOspfAreaTeCapable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 2, 1, 2),
    _UsdOspfAreaTeCapable_Type()
)
usdOspfAreaTeCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdOspfAreaTeCapable.setStatus("current")
_UsdOspfIfTable_Object = MibTable
usdOspfIfTable = _UsdOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7)
)
if mibBuilder.loadTexts:
    usdOspfIfTable.setStatus("current")
_UsdOspfIfEntry_Object = MibTableRow
usdOspfIfEntry = _UsdOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1)
)
if mibBuilder.loadTexts:
    usdOspfIfEntry.setStatus("current")


class _UsdOspfIfCost_Type(Integer32):
    """Custom type usdOspfIfCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_UsdOspfIfCost_Type.__name__ = "Integer32"
_UsdOspfIfCost_Object = MibTableColumn
usdOspfIfCost = _UsdOspfIfCost_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 1),
    _UsdOspfIfCost_Type()
)
usdOspfIfCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfIfCost.setStatus("current")
_UsdOspfIfMask_Type = IpAddress
_UsdOspfIfMask_Object = MibTableColumn
usdOspfIfMask = _UsdOspfIfMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 2),
    _UsdOspfIfMask_Type()
)
usdOspfIfMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfIfMask.setStatus("current")


class _UsdOspfIfPassiveFlag_Type(Integer32):
    """Custom type usdOspfIfPassiveFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UsdOspfIfPassiveFlag_Type.__name__ = "Integer32"
_UsdOspfIfPassiveFlag_Object = MibTableColumn
usdOspfIfPassiveFlag = _UsdOspfIfPassiveFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 3),
    _UsdOspfIfPassiveFlag_Type()
)
usdOspfIfPassiveFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfIfPassiveFlag.setStatus("current")
_UsdOspfIfNbrCount_Type = Counter32
_UsdOspfIfNbrCount_Object = MibTableColumn
usdOspfIfNbrCount = _UsdOspfIfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 4),
    _UsdOspfIfNbrCount_Type()
)
usdOspfIfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfIfNbrCount.setStatus("current")
_UsdOspfIfAdjNbrCount_Type = Counter32
_UsdOspfIfAdjNbrCount_Object = MibTableColumn
usdOspfIfAdjNbrCount = _UsdOspfIfAdjNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 5),
    _UsdOspfIfAdjNbrCount_Type()
)
usdOspfIfAdjNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfIfAdjNbrCount.setStatus("current")


class _UsdOspfIfMd5AuthKey_Type(OctetString):
    """Custom type usdOspfIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UsdOspfIfMd5AuthKey_Type.__name__ = "OctetString"
_UsdOspfIfMd5AuthKey_Object = MibTableColumn
usdOspfIfMd5AuthKey = _UsdOspfIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 6),
    _UsdOspfIfMd5AuthKey_Type()
)
usdOspfIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfIfMd5AuthKey.setStatus("current")


class _UsdOspfIfMd5AuthKeyId_Type(Integer32):
    """Custom type usdOspfIfMd5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsdOspfIfMd5AuthKeyId_Type.__name__ = "Integer32"
_UsdOspfIfMd5AuthKeyId_Object = MibTableColumn
usdOspfIfMd5AuthKeyId = _UsdOspfIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 7),
    _UsdOspfIfMd5AuthKeyId_Type()
)
usdOspfIfMd5AuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfIfMd5AuthKeyId.setStatus("current")
_UsdOspfVirtIfTable_Object = MibTable
usdOspfVirtIfTable = _UsdOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 9)
)
if mibBuilder.loadTexts:
    usdOspfVirtIfTable.setStatus("current")
_UsdOspfVirtIfEntry_Object = MibTableRow
usdOspfVirtIfEntry = _UsdOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 9, 1)
)
if mibBuilder.loadTexts:
    usdOspfVirtIfEntry.setStatus("current")


class _UsdOspfVirtIfMd5AuthKey_Type(OctetString):
    """Custom type usdOspfVirtIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UsdOspfVirtIfMd5AuthKey_Type.__name__ = "OctetString"
_UsdOspfVirtIfMd5AuthKey_Object = MibTableColumn
usdOspfVirtIfMd5AuthKey = _UsdOspfVirtIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 9, 1, 1),
    _UsdOspfVirtIfMd5AuthKey_Type()
)
usdOspfVirtIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfVirtIfMd5AuthKey.setStatus("current")


class _UsdOspfVirtIfMd5AuthKeyId_Type(Integer32):
    """Custom type usdOspfVirtIfMd5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsdOspfVirtIfMd5AuthKeyId_Type.__name__ = "Integer32"
_UsdOspfVirtIfMd5AuthKeyId_Object = MibTableColumn
usdOspfVirtIfMd5AuthKeyId = _UsdOspfVirtIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 9, 1, 2),
    _UsdOspfVirtIfMd5AuthKeyId_Type()
)
usdOspfVirtIfMd5AuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfVirtIfMd5AuthKeyId.setStatus("current")
_UsdOspfNbrTable_Object = MibTable
usdOspfNbrTable = _UsdOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 10)
)
if mibBuilder.loadTexts:
    usdOspfNbrTable.setStatus("current")
_UsdOspfNbrEntry_Object = MibTableRow
usdOspfNbrEntry = _UsdOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 10, 1)
)
if mibBuilder.loadTexts:
    usdOspfNbrEntry.setStatus("current")
_UsdOspfNbrLocalIpAddr_Type = IpAddress
_UsdOspfNbrLocalIpAddr_Object = MibTableColumn
usdOspfNbrLocalIpAddr = _UsdOspfNbrLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 10, 1, 1),
    _UsdOspfNbrLocalIpAddr_Type()
)
usdOspfNbrLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfNbrLocalIpAddr.setStatus("current")
_UsdOspfNbrDR_Type = IpAddress
_UsdOspfNbrDR_Object = MibTableColumn
usdOspfNbrDR = _UsdOspfNbrDR_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 10, 1, 2),
    _UsdOspfNbrDR_Type()
)
usdOspfNbrDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfNbrDR.setStatus("current")
_UsdOspfNbrBDR_Type = IpAddress
_UsdOspfNbrBDR_Object = MibTableColumn
usdOspfNbrBDR = _UsdOspfNbrBDR_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 10, 1, 3),
    _UsdOspfNbrBDR_Type()
)
usdOspfNbrBDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfNbrBDR.setStatus("current")
_UsdOspfSummImportTable_Object = MibTable
usdOspfSummImportTable = _UsdOspfSummImportTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15)
)
if mibBuilder.loadTexts:
    usdOspfSummImportTable.setStatus("current")
_UsdOspfSummImportEntry_Object = MibTableRow
usdOspfSummImportEntry = _UsdOspfSummImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15, 1)
)
usdOspfSummImportEntry.setIndexNames(
    (0, "Unisphere-Data-OSPF-MIB", "usdOspfSummAggNet"),
    (0, "Unisphere-Data-OSPF-MIB", "usdOspfSummAggMask"),
)
if mibBuilder.loadTexts:
    usdOspfSummImportEntry.setStatus("current")
_UsdOspfSummAggNet_Type = IpAddress
_UsdOspfSummAggNet_Object = MibTableColumn
usdOspfSummAggNet = _UsdOspfSummAggNet_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15, 1, 1),
    _UsdOspfSummAggNet_Type()
)
usdOspfSummAggNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfSummAggNet.setStatus("current")
_UsdOspfSummAggMask_Type = IpAddress
_UsdOspfSummAggMask_Object = MibTableColumn
usdOspfSummAggMask = _UsdOspfSummAggMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15, 1, 2),
    _UsdOspfSummAggMask_Type()
)
usdOspfSummAggMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfSummAggMask.setStatus("current")


class _UsdOspfSummAdminStat_Type(Integer32):
    """Custom type usdOspfSummAdminStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_UsdOspfSummAdminStat_Type.__name__ = "Integer32"
_UsdOspfSummAdminStat_Object = MibTableColumn
usdOspfSummAdminStat = _UsdOspfSummAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15, 1, 3),
    _UsdOspfSummAdminStat_Type()
)
usdOspfSummAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfSummAdminStat.setStatus("current")
_UsdOspfSummRowStatus_Type = RowStatus
_UsdOspfSummRowStatus_Object = MibTableColumn
usdOspfSummRowStatus = _UsdOspfSummRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15, 1, 4),
    _UsdOspfSummRowStatus_Type()
)
usdOspfSummRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfSummRowStatus.setStatus("current")
_UsdOspfMd5IntfTable_Object = MibTable
usdOspfMd5IntfTable = _UsdOspfMd5IntfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16)
)
if mibBuilder.loadTexts:
    usdOspfMd5IntfTable.setStatus("current")
_UsdOspfMd5IntfEntry_Object = MibTableRow
usdOspfMd5IntfEntry = _UsdOspfMd5IntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16, 1)
)
usdOspfMd5IntfEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
    (0, "Unisphere-Data-OSPF-MIB", "usdOspfMd5IntfKeyId"),
)
if mibBuilder.loadTexts:
    usdOspfMd5IntfEntry.setStatus("current")


class _UsdOspfMd5IntfKeyId_Type(Integer32):
    """Custom type usdOspfMd5IntfKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsdOspfMd5IntfKeyId_Type.__name__ = "Integer32"
_UsdOspfMd5IntfKeyId_Object = MibTableColumn
usdOspfMd5IntfKeyId = _UsdOspfMd5IntfKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16, 1, 1),
    _UsdOspfMd5IntfKeyId_Type()
)
usdOspfMd5IntfKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfMd5IntfKeyId.setStatus("current")
_UsdOspfMd5IntfKeyActive_Type = TruthValue
_UsdOspfMd5IntfKeyActive_Object = MibTableColumn
usdOspfMd5IntfKeyActive = _UsdOspfMd5IntfKeyActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16, 1, 2),
    _UsdOspfMd5IntfKeyActive_Type()
)
usdOspfMd5IntfKeyActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfMd5IntfKeyActive.setStatus("current")


class _UsdOspfMd5IntfAuthKey_Type(OctetString):
    """Custom type usdOspfMd5IntfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UsdOspfMd5IntfAuthKey_Type.__name__ = "OctetString"
_UsdOspfMd5IntfAuthKey_Object = MibTableColumn
usdOspfMd5IntfAuthKey = _UsdOspfMd5IntfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16, 1, 3),
    _UsdOspfMd5IntfAuthKey_Type()
)
usdOspfMd5IntfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfMd5IntfAuthKey.setStatus("current")
_UsdOspfMd5IntfRowStatus_Type = RowStatus
_UsdOspfMd5IntfRowStatus_Object = MibTableColumn
usdOspfMd5IntfRowStatus = _UsdOspfMd5IntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16, 1, 4),
    _UsdOspfMd5IntfRowStatus_Type()
)
usdOspfMd5IntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfMd5IntfRowStatus.setStatus("current")
_UsdOspfMd5VirtIntfTable_Object = MibTable
usdOspfMd5VirtIntfTable = _UsdOspfMd5VirtIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17)
)
if mibBuilder.loadTexts:
    usdOspfMd5VirtIntfTable.setStatus("current")
_UsdOspfMd5VirtIntfEntry_Object = MibTableRow
usdOspfMd5VirtIntfEntry = _UsdOspfMd5VirtIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1)
)
usdOspfMd5VirtIntfEntry.setIndexNames(
    (0, "Unisphere-Data-OSPF-MIB", "usdOspfMd5VirtIntfAreaId"),
    (0, "Unisphere-Data-OSPF-MIB", "usdOspfMd5VirtIntfNeighbor"),
    (0, "Unisphere-Data-OSPF-MIB", "usdOspfMd5VirtIntfKeyId"),
)
if mibBuilder.loadTexts:
    usdOspfMd5VirtIntfEntry.setStatus("current")
_UsdOspfMd5VirtIntfAreaId_Type = IpAddress
_UsdOspfMd5VirtIntfAreaId_Object = MibTableColumn
usdOspfMd5VirtIntfAreaId = _UsdOspfMd5VirtIntfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 1),
    _UsdOspfMd5VirtIntfAreaId_Type()
)
usdOspfMd5VirtIntfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfMd5VirtIntfAreaId.setStatus("current")
_UsdOspfMd5VirtIntfNeighbor_Type = IpAddress
_UsdOspfMd5VirtIntfNeighbor_Object = MibTableColumn
usdOspfMd5VirtIntfNeighbor = _UsdOspfMd5VirtIntfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 2),
    _UsdOspfMd5VirtIntfNeighbor_Type()
)
usdOspfMd5VirtIntfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfMd5VirtIntfNeighbor.setStatus("current")


class _UsdOspfMd5VirtIntfKeyId_Type(Integer32):
    """Custom type usdOspfMd5VirtIntfKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UsdOspfMd5VirtIntfKeyId_Type.__name__ = "Integer32"
_UsdOspfMd5VirtIntfKeyId_Object = MibTableColumn
usdOspfMd5VirtIntfKeyId = _UsdOspfMd5VirtIntfKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 3),
    _UsdOspfMd5VirtIntfKeyId_Type()
)
usdOspfMd5VirtIntfKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfMd5VirtIntfKeyId.setStatus("current")
_UsdOspfMd5VirtIntfKeyActive_Type = TruthValue
_UsdOspfMd5VirtIntfKeyActive_Object = MibTableColumn
usdOspfMd5VirtIntfKeyActive = _UsdOspfMd5VirtIntfKeyActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 4),
    _UsdOspfMd5VirtIntfKeyActive_Type()
)
usdOspfMd5VirtIntfKeyActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfMd5VirtIntfKeyActive.setStatus("current")


class _UsdOspfMd5VirtIntfAuthKey_Type(OctetString):
    """Custom type usdOspfMd5VirtIntfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_UsdOspfMd5VirtIntfAuthKey_Type.__name__ = "OctetString"
_UsdOspfMd5VirtIntfAuthKey_Object = MibTableColumn
usdOspfMd5VirtIntfAuthKey = _UsdOspfMd5VirtIntfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 5),
    _UsdOspfMd5VirtIntfAuthKey_Type()
)
usdOspfMd5VirtIntfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfMd5VirtIntfAuthKey.setStatus("current")
_UsdOspfMd5VirtIntfRowStatus_Type = RowStatus
_UsdOspfMd5VirtIntfRowStatus_Object = MibTableColumn
usdOspfMd5VirtIntfRowStatus = _UsdOspfMd5VirtIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 6),
    _UsdOspfMd5VirtIntfRowStatus_Type()
)
usdOspfMd5VirtIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfMd5VirtIntfRowStatus.setStatus("current")
_UsdOspfNetworkRangeTable_Object = MibTable
usdOspfNetworkRangeTable = _UsdOspfNetworkRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18)
)
if mibBuilder.loadTexts:
    usdOspfNetworkRangeTable.setStatus("current")
_UsdOspfNetworkRangeEntry_Object = MibTableRow
usdOspfNetworkRangeEntry = _UsdOspfNetworkRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18, 1)
)
usdOspfNetworkRangeEntry.setIndexNames(
    (0, "Unisphere-Data-OSPF-MIB", "usdOspfNetRangeNet"),
    (0, "Unisphere-Data-OSPF-MIB", "usdOspfNetRangeMask"),
    (0, "Unisphere-Data-OSPF-MIB", "usdOspfNetRangeAreaId"),
)
if mibBuilder.loadTexts:
    usdOspfNetworkRangeEntry.setStatus("current")
_UsdOspfNetRangeNet_Type = IpAddress
_UsdOspfNetRangeNet_Object = MibTableColumn
usdOspfNetRangeNet = _UsdOspfNetRangeNet_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18, 1, 1),
    _UsdOspfNetRangeNet_Type()
)
usdOspfNetRangeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfNetRangeNet.setStatus("current")
_UsdOspfNetRangeMask_Type = IpAddress
_UsdOspfNetRangeMask_Object = MibTableColumn
usdOspfNetRangeMask = _UsdOspfNetRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18, 1, 2),
    _UsdOspfNetRangeMask_Type()
)
usdOspfNetRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfNetRangeMask.setStatus("current")
_UsdOspfNetRangeAreaId_Type = IpAddress
_UsdOspfNetRangeAreaId_Object = MibTableColumn
usdOspfNetRangeAreaId = _UsdOspfNetRangeAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18, 1, 3),
    _UsdOspfNetRangeAreaId_Type()
)
usdOspfNetRangeAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdOspfNetRangeAreaId.setStatus("current")
_UsdOspfNetRangeRowStatus_Type = RowStatus
_UsdOspfNetRangeRowStatus_Object = MibTableColumn
usdOspfNetRangeRowStatus = _UsdOspfNetRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18, 1, 4),
    _UsdOspfNetRangeRowStatus_Type()
)
usdOspfNetRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdOspfNetRangeRowStatus.setStatus("current")
_UsdOspfConformance_ObjectIdentity = ObjectIdentity
usdOspfConformance = _UsdOspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4)
)
_UsdOspfCompliances_ObjectIdentity = ObjectIdentity
usdOspfCompliances = _UsdOspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 1)
)
_UsdOspfGroups_ObjectIdentity = ObjectIdentity
usdOspfGroups = _UsdOspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2)
)
ospfAreaEntry.registerAugmentions(
    ("Unisphere-Data-OSPF-MIB",
     "usdOspfAreaEntry")
)
usdOspfAreaEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("Unisphere-Data-OSPF-MIB",
     "usdOspfIfEntry")
)
usdOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("Unisphere-Data-OSPF-MIB",
     "usdOspfVirtIfEntry")
)
usdOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
ospfNbrEntry.registerAugmentions(
    ("Unisphere-Data-OSPF-MIB",
     "usdOspfNbrEntry")
)
usdOspfNbrEntry.setIndexNames(*ospfNbrEntry.getIndexNames())

# Managed Objects groups

usdOspfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 1)
)
usdOspfBasicGroup.setObjects(
      *(("Unisphere-Data-OSPF-MIB", "usdOspfProcessId"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMaxPathSplits"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfSpfHoldInterval"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfNumActiveAreas"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfSpfTime"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfRefBw"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAutoVlink"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfIntraDistance"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfInterDistance"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfExtDistance"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfHelloPktsRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfDDPktsRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsrPktsRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsuPktsRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsAckPktsRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfTotalRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsaDiscardCnt"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfHelloPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfDDPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsrPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsuPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsAckPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfErrPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfTotalSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfCsumErrPkts"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailNbr"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailLsa"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailLsd"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailDbRequest"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailRtx"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailAck"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailDbPkt"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailCirc"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailPkt"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfOperState"))
)
if mibBuilder.loadTexts:
    usdOspfBasicGroup.setStatus("obsolete")

usdOspfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 2)
)
usdOspfIfGroup.setObjects(
      *(("Unisphere-Data-OSPF-MIB", "usdOspfIfCost"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfIfMask"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfIfPassiveFlag"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfIfNbrCount"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfIfAdjNbrCount"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfIfMd5AuthKey"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfIfMd5AuthKeyId"))
)
if mibBuilder.loadTexts:
    usdOspfIfGroup.setStatus("current")

usdOspfAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 3)
)
usdOspfAreaGroup.setObjects(
      *(("Unisphere-Data-OSPF-MIB", "usdOspfAreaType"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAreaTeCapable"))
)
if mibBuilder.loadTexts:
    usdOspfAreaGroup.setStatus("current")

usdOspfVirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 4)
)
usdOspfVirtIfGroup.setObjects(
      *(("Unisphere-Data-OSPF-MIB", "usdOspfVirtIfMd5AuthKey"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfVirtIfMd5AuthKeyId"))
)
if mibBuilder.loadTexts:
    usdOspfVirtIfGroup.setStatus("current")

usdOspfNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 5)
)
usdOspfNbrGroup.setObjects(
      *(("Unisphere-Data-OSPF-MIB", "usdOspfNbrLocalIpAddr"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfNbrDR"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfNbrBDR"))
)
if mibBuilder.loadTexts:
    usdOspfNbrGroup.setStatus("current")

usdOspfSummImportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 6)
)
usdOspfSummImportGroup.setObjects(
      *(("Unisphere-Data-OSPF-MIB", "usdOspfSummAggNet"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfSummAggMask"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfSummAdminStat"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfSummRowStatus"))
)
if mibBuilder.loadTexts:
    usdOspfSummImportGroup.setStatus("current")

usdOspfMd5IntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 7)
)
usdOspfMd5IntfGroup.setObjects(
      *(("Unisphere-Data-OSPF-MIB", "usdOspfMd5IntfKeyId"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMd5IntfKeyActive"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMd5IntfAuthKey"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMd5IntfRowStatus"))
)
if mibBuilder.loadTexts:
    usdOspfMd5IntfGroup.setStatus("current")

usdOspfMd5VirtIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 8)
)
usdOspfMd5VirtIntfGroup.setObjects(
      *(("Unisphere-Data-OSPF-MIB", "usdOspfMd5VirtIntfAreaId"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMd5VirtIntfNeighbor"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMd5VirtIntfKeyId"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMd5VirtIntfKeyActive"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMd5VirtIntfAuthKey"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMd5VirtIntfRowStatus"))
)
if mibBuilder.loadTexts:
    usdOspfMd5VirtIntfGroup.setStatus("current")

usdOspfNetRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 9)
)
usdOspfNetRangeGroup.setObjects(
      *(("Unisphere-Data-OSPF-MIB", "usdOspfNetRangeNet"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfNetRangeMask"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfNetRangeAreaId"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfNetRangeRowStatus"))
)
if mibBuilder.loadTexts:
    usdOspfNetRangeGroup.setStatus("current")

usdOspfBasicGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 10)
)
usdOspfBasicGroup2.setObjects(
      *(("Unisphere-Data-OSPF-MIB", "usdOspfProcessId"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMaxPathSplits"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfSpfHoldInterval"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfNumActiveAreas"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfSpfTime"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfRefBw"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAutoVlink"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfIntraDistance"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfInterDistance"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfExtDistance"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfHelloPktsRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfDDPktsRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsrPktsRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsuPktsRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsAckPktsRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfTotalRcv"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsaDiscardCnt"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfHelloPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfDDPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsrPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsuPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfLsAckPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfErrPktsSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfTotalSent"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfCsumErrPkts"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailNbr"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailLsa"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailLsd"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailDbRequest"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailRtx"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailAck"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailDbPkt"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailCirc"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfAllocFailPkt"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfOperState"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfVpnRouteTag"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfDomainId"),
        ("Unisphere-Data-OSPF-MIB", "usdOspfMplsTeRtrIdIfIndex"))
)
if mibBuilder.loadTexts:
    usdOspfBasicGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdOspfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdOspfCompliance.setStatus(
        "obsolete"
    )

usdOspfCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdOspfCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-OSPF-MIB",
    **{"usdOspfMIB": usdOspfMIB,
       "usdOspfObjects": usdOspfObjects,
       "usdOspfGeneralGroup": usdOspfGeneralGroup,
       "usdOspfProcessId": usdOspfProcessId,
       "usdOspfMaxPathSplits": usdOspfMaxPathSplits,
       "usdOspfSpfHoldInterval": usdOspfSpfHoldInterval,
       "usdOspfNumActiveAreas": usdOspfNumActiveAreas,
       "usdOspfSpfTime": usdOspfSpfTime,
       "usdOspfRefBw": usdOspfRefBw,
       "usdOspfAutoVlink": usdOspfAutoVlink,
       "usdOspfIntraDistance": usdOspfIntraDistance,
       "usdOspfInterDistance": usdOspfInterDistance,
       "usdOspfExtDistance": usdOspfExtDistance,
       "usdOspfHelloPktsRcv": usdOspfHelloPktsRcv,
       "usdOspfDDPktsRcv": usdOspfDDPktsRcv,
       "usdOspfLsrPktsRcv": usdOspfLsrPktsRcv,
       "usdOspfLsuPktsRcv": usdOspfLsuPktsRcv,
       "usdOspfLsAckPktsRcv": usdOspfLsAckPktsRcv,
       "usdOspfTotalRcv": usdOspfTotalRcv,
       "usdOspfLsaDiscardCnt": usdOspfLsaDiscardCnt,
       "usdOspfHelloPktsSent": usdOspfHelloPktsSent,
       "usdOspfDDPktsSent": usdOspfDDPktsSent,
       "usdOspfLsrPktsSent": usdOspfLsrPktsSent,
       "usdOspfLsuPktsSent": usdOspfLsuPktsSent,
       "usdOspfLsAckPktsSent": usdOspfLsAckPktsSent,
       "usdOspfErrPktsSent": usdOspfErrPktsSent,
       "usdOspfTotalSent": usdOspfTotalSent,
       "usdOspfCsumErrPkts": usdOspfCsumErrPkts,
       "usdOspfAllocFailNbr": usdOspfAllocFailNbr,
       "usdOspfAllocFailLsa": usdOspfAllocFailLsa,
       "usdOspfAllocFailLsd": usdOspfAllocFailLsd,
       "usdOspfAllocFailDbRequest": usdOspfAllocFailDbRequest,
       "usdOspfAllocFailRtx": usdOspfAllocFailRtx,
       "usdOspfAllocFailAck": usdOspfAllocFailAck,
       "usdOspfAllocFailDbPkt": usdOspfAllocFailDbPkt,
       "usdOspfAllocFailCirc": usdOspfAllocFailCirc,
       "usdOspfAllocFailPkt": usdOspfAllocFailPkt,
       "usdOspfOperState": usdOspfOperState,
       "usdOspfVpnRouteTag": usdOspfVpnRouteTag,
       "usdOspfDomainId": usdOspfDomainId,
       "usdOspfMplsTeRtrIdIfIndex": usdOspfMplsTeRtrIdIfIndex,
       "usdOspfAreaTable": usdOspfAreaTable,
       "usdOspfAreaEntry": usdOspfAreaEntry,
       "usdOspfAreaType": usdOspfAreaType,
       "usdOspfAreaTeCapable": usdOspfAreaTeCapable,
       "usdOspfIfTable": usdOspfIfTable,
       "usdOspfIfEntry": usdOspfIfEntry,
       "usdOspfIfCost": usdOspfIfCost,
       "usdOspfIfMask": usdOspfIfMask,
       "usdOspfIfPassiveFlag": usdOspfIfPassiveFlag,
       "usdOspfIfNbrCount": usdOspfIfNbrCount,
       "usdOspfIfAdjNbrCount": usdOspfIfAdjNbrCount,
       "usdOspfIfMd5AuthKey": usdOspfIfMd5AuthKey,
       "usdOspfIfMd5AuthKeyId": usdOspfIfMd5AuthKeyId,
       "usdOspfVirtIfTable": usdOspfVirtIfTable,
       "usdOspfVirtIfEntry": usdOspfVirtIfEntry,
       "usdOspfVirtIfMd5AuthKey": usdOspfVirtIfMd5AuthKey,
       "usdOspfVirtIfMd5AuthKeyId": usdOspfVirtIfMd5AuthKeyId,
       "usdOspfNbrTable": usdOspfNbrTable,
       "usdOspfNbrEntry": usdOspfNbrEntry,
       "usdOspfNbrLocalIpAddr": usdOspfNbrLocalIpAddr,
       "usdOspfNbrDR": usdOspfNbrDR,
       "usdOspfNbrBDR": usdOspfNbrBDR,
       "usdOspfSummImportTable": usdOspfSummImportTable,
       "usdOspfSummImportEntry": usdOspfSummImportEntry,
       "usdOspfSummAggNet": usdOspfSummAggNet,
       "usdOspfSummAggMask": usdOspfSummAggMask,
       "usdOspfSummAdminStat": usdOspfSummAdminStat,
       "usdOspfSummRowStatus": usdOspfSummRowStatus,
       "usdOspfMd5IntfTable": usdOspfMd5IntfTable,
       "usdOspfMd5IntfEntry": usdOspfMd5IntfEntry,
       "usdOspfMd5IntfKeyId": usdOspfMd5IntfKeyId,
       "usdOspfMd5IntfKeyActive": usdOspfMd5IntfKeyActive,
       "usdOspfMd5IntfAuthKey": usdOspfMd5IntfAuthKey,
       "usdOspfMd5IntfRowStatus": usdOspfMd5IntfRowStatus,
       "usdOspfMd5VirtIntfTable": usdOspfMd5VirtIntfTable,
       "usdOspfMd5VirtIntfEntry": usdOspfMd5VirtIntfEntry,
       "usdOspfMd5VirtIntfAreaId": usdOspfMd5VirtIntfAreaId,
       "usdOspfMd5VirtIntfNeighbor": usdOspfMd5VirtIntfNeighbor,
       "usdOspfMd5VirtIntfKeyId": usdOspfMd5VirtIntfKeyId,
       "usdOspfMd5VirtIntfKeyActive": usdOspfMd5VirtIntfKeyActive,
       "usdOspfMd5VirtIntfAuthKey": usdOspfMd5VirtIntfAuthKey,
       "usdOspfMd5VirtIntfRowStatus": usdOspfMd5VirtIntfRowStatus,
       "usdOspfNetworkRangeTable": usdOspfNetworkRangeTable,
       "usdOspfNetworkRangeEntry": usdOspfNetworkRangeEntry,
       "usdOspfNetRangeNet": usdOspfNetRangeNet,
       "usdOspfNetRangeMask": usdOspfNetRangeMask,
       "usdOspfNetRangeAreaId": usdOspfNetRangeAreaId,
       "usdOspfNetRangeRowStatus": usdOspfNetRangeRowStatus,
       "usdOspfConformance": usdOspfConformance,
       "usdOspfCompliances": usdOspfCompliances,
       "usdOspfCompliance": usdOspfCompliance,
       "usdOspfCompliance2": usdOspfCompliance2,
       "usdOspfGroups": usdOspfGroups,
       "usdOspfBasicGroup": usdOspfBasicGroup,
       "usdOspfIfGroup": usdOspfIfGroup,
       "usdOspfAreaGroup": usdOspfAreaGroup,
       "usdOspfVirtIfGroup": usdOspfVirtIfGroup,
       "usdOspfNbrGroup": usdOspfNbrGroup,
       "usdOspfSummImportGroup": usdOspfSummImportGroup,
       "usdOspfMd5IntfGroup": usdOspfMd5IntfGroup,
       "usdOspfMd5VirtIntfGroup": usdOspfMd5VirtIntfGroup,
       "usdOspfNetRangeGroup": usdOspfNetRangeGroup,
       "usdOspfBasicGroup2": usdOspfBasicGroup2}
)
