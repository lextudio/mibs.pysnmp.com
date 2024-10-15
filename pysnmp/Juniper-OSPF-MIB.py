# SNMP MIB module (Juniper-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:52 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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


# MODULE-IDENTITY

juniOspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14)
)
juniOspfMIB.setRevisions(
        ("2002-09-16 21:44",
         "2002-04-05 21:20",
         "2000-05-23 00:00",
         "1999-09-28 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_JuniOspfObjects_ObjectIdentity = ObjectIdentity
juniOspfObjects = _JuniOspfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1)
)
_JuniOspfGeneralGroup_ObjectIdentity = ObjectIdentity
juniOspfGeneralGroup = _JuniOspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1)
)


class _JuniOspfProcessId_Type(Integer32):
    """Custom type juniOspfProcessId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniOspfProcessId_Type.__name__ = "Integer32"
_JuniOspfProcessId_Object = MibScalar
juniOspfProcessId = _JuniOspfProcessId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 1),
    _JuniOspfProcessId_Type()
)
juniOspfProcessId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfProcessId.setStatus("current")


class _JuniOspfMaxPathSplits_Type(Integer32):
    """Custom type juniOspfMaxPathSplits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_JuniOspfMaxPathSplits_Type.__name__ = "Integer32"
_JuniOspfMaxPathSplits_Object = MibScalar
juniOspfMaxPathSplits = _JuniOspfMaxPathSplits_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 2),
    _JuniOspfMaxPathSplits_Type()
)
juniOspfMaxPathSplits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfMaxPathSplits.setStatus("current")


class _JuniOspfSpfHoldInterval_Type(Integer32):
    """Custom type juniOspfSpfHoldInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_JuniOspfSpfHoldInterval_Type.__name__ = "Integer32"
_JuniOspfSpfHoldInterval_Object = MibScalar
juniOspfSpfHoldInterval = _JuniOspfSpfHoldInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 3),
    _JuniOspfSpfHoldInterval_Type()
)
juniOspfSpfHoldInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfSpfHoldInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniOspfSpfHoldInterval.setUnits("seconds")
_JuniOspfNumActiveAreas_Type = Counter32
_JuniOspfNumActiveAreas_Object = MibScalar
juniOspfNumActiveAreas = _JuniOspfNumActiveAreas_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 4),
    _JuniOspfNumActiveAreas_Type()
)
juniOspfNumActiveAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfNumActiveAreas.setStatus("current")
_JuniOspfSpfTime_Type = Counter32
_JuniOspfSpfTime_Object = MibScalar
juniOspfSpfTime = _JuniOspfSpfTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 5),
    _JuniOspfSpfTime_Type()
)
juniOspfSpfTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfSpfTime.setStatus("current")


class _JuniOspfRefBw_Type(Unsigned32):
    """Custom type juniOspfRefBw based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_JuniOspfRefBw_Type.__name__ = "Unsigned32"
_JuniOspfRefBw_Object = MibScalar
juniOspfRefBw = _JuniOspfRefBw_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 6),
    _JuniOspfRefBw_Type()
)
juniOspfRefBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfRefBw.setStatus("current")
if mibBuilder.loadTexts:
    juniOspfRefBw.setUnits("bits per second")
_JuniOspfAutoVlink_Type = TruthValue
_JuniOspfAutoVlink_Object = MibScalar
juniOspfAutoVlink = _JuniOspfAutoVlink_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 7),
    _JuniOspfAutoVlink_Type()
)
juniOspfAutoVlink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfAutoVlink.setStatus("current")


class _JuniOspfIntraDistance_Type(Integer32):
    """Custom type juniOspfIntraDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniOspfIntraDistance_Type.__name__ = "Integer32"
_JuniOspfIntraDistance_Object = MibScalar
juniOspfIntraDistance = _JuniOspfIntraDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 8),
    _JuniOspfIntraDistance_Type()
)
juniOspfIntraDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfIntraDistance.setStatus("current")


class _JuniOspfInterDistance_Type(Integer32):
    """Custom type juniOspfInterDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniOspfInterDistance_Type.__name__ = "Integer32"
_JuniOspfInterDistance_Object = MibScalar
juniOspfInterDistance = _JuniOspfInterDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 9),
    _JuniOspfInterDistance_Type()
)
juniOspfInterDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfInterDistance.setStatus("current")


class _JuniOspfExtDistance_Type(Integer32):
    """Custom type juniOspfExtDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniOspfExtDistance_Type.__name__ = "Integer32"
_JuniOspfExtDistance_Object = MibScalar
juniOspfExtDistance = _JuniOspfExtDistance_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 10),
    _JuniOspfExtDistance_Type()
)
juniOspfExtDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfExtDistance.setStatus("current")
_JuniOspfHelloPktsRcv_Type = Counter32
_JuniOspfHelloPktsRcv_Object = MibScalar
juniOspfHelloPktsRcv = _JuniOspfHelloPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 11),
    _JuniOspfHelloPktsRcv_Type()
)
juniOspfHelloPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfHelloPktsRcv.setStatus("current")
_JuniOspfDDPktsRcv_Type = Counter32
_JuniOspfDDPktsRcv_Object = MibScalar
juniOspfDDPktsRcv = _JuniOspfDDPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 12),
    _JuniOspfDDPktsRcv_Type()
)
juniOspfDDPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfDDPktsRcv.setStatus("current")
_JuniOspfLsrPktsRcv_Type = Counter32
_JuniOspfLsrPktsRcv_Object = MibScalar
juniOspfLsrPktsRcv = _JuniOspfLsrPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 13),
    _JuniOspfLsrPktsRcv_Type()
)
juniOspfLsrPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfLsrPktsRcv.setStatus("current")
_JuniOspfLsuPktsRcv_Type = Counter32
_JuniOspfLsuPktsRcv_Object = MibScalar
juniOspfLsuPktsRcv = _JuniOspfLsuPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 14),
    _JuniOspfLsuPktsRcv_Type()
)
juniOspfLsuPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfLsuPktsRcv.setStatus("current")
_JuniOspfLsAckPktsRcv_Type = Counter32
_JuniOspfLsAckPktsRcv_Object = MibScalar
juniOspfLsAckPktsRcv = _JuniOspfLsAckPktsRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 15),
    _JuniOspfLsAckPktsRcv_Type()
)
juniOspfLsAckPktsRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfLsAckPktsRcv.setStatus("current")
_JuniOspfTotalRcv_Type = Counter32
_JuniOspfTotalRcv_Object = MibScalar
juniOspfTotalRcv = _JuniOspfTotalRcv_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 16),
    _JuniOspfTotalRcv_Type()
)
juniOspfTotalRcv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfTotalRcv.setStatus("current")
_JuniOspfLsaDiscardCnt_Type = Counter32
_JuniOspfLsaDiscardCnt_Object = MibScalar
juniOspfLsaDiscardCnt = _JuniOspfLsaDiscardCnt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 17),
    _JuniOspfLsaDiscardCnt_Type()
)
juniOspfLsaDiscardCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfLsaDiscardCnt.setStatus("current")
_JuniOspfHelloPktsSent_Type = Counter32
_JuniOspfHelloPktsSent_Object = MibScalar
juniOspfHelloPktsSent = _JuniOspfHelloPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 18),
    _JuniOspfHelloPktsSent_Type()
)
juniOspfHelloPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfHelloPktsSent.setStatus("current")
_JuniOspfDDPktsSent_Type = Counter32
_JuniOspfDDPktsSent_Object = MibScalar
juniOspfDDPktsSent = _JuniOspfDDPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 19),
    _JuniOspfDDPktsSent_Type()
)
juniOspfDDPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfDDPktsSent.setStatus("current")
_JuniOspfLsrPktsSent_Type = Counter32
_JuniOspfLsrPktsSent_Object = MibScalar
juniOspfLsrPktsSent = _JuniOspfLsrPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 20),
    _JuniOspfLsrPktsSent_Type()
)
juniOspfLsrPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfLsrPktsSent.setStatus("current")
_JuniOspfLsuPktsSent_Type = Counter32
_JuniOspfLsuPktsSent_Object = MibScalar
juniOspfLsuPktsSent = _JuniOspfLsuPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 21),
    _JuniOspfLsuPktsSent_Type()
)
juniOspfLsuPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfLsuPktsSent.setStatus("current")
_JuniOspfLsAckPktsSent_Type = Counter32
_JuniOspfLsAckPktsSent_Object = MibScalar
juniOspfLsAckPktsSent = _JuniOspfLsAckPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 22),
    _JuniOspfLsAckPktsSent_Type()
)
juniOspfLsAckPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfLsAckPktsSent.setStatus("current")
_JuniOspfErrPktsSent_Type = Counter32
_JuniOspfErrPktsSent_Object = MibScalar
juniOspfErrPktsSent = _JuniOspfErrPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 23),
    _JuniOspfErrPktsSent_Type()
)
juniOspfErrPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfErrPktsSent.setStatus("current")
_JuniOspfTotalSent_Type = Counter32
_JuniOspfTotalSent_Object = MibScalar
juniOspfTotalSent = _JuniOspfTotalSent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 24),
    _JuniOspfTotalSent_Type()
)
juniOspfTotalSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfTotalSent.setStatus("current")
_JuniOspfCsumErrPkts_Type = Counter32
_JuniOspfCsumErrPkts_Object = MibScalar
juniOspfCsumErrPkts = _JuniOspfCsumErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 25),
    _JuniOspfCsumErrPkts_Type()
)
juniOspfCsumErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfCsumErrPkts.setStatus("current")
_JuniOspfAllocFailNbr_Type = Counter32
_JuniOspfAllocFailNbr_Object = MibScalar
juniOspfAllocFailNbr = _JuniOspfAllocFailNbr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 26),
    _JuniOspfAllocFailNbr_Type()
)
juniOspfAllocFailNbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfAllocFailNbr.setStatus("current")
_JuniOspfAllocFailLsa_Type = Counter32
_JuniOspfAllocFailLsa_Object = MibScalar
juniOspfAllocFailLsa = _JuniOspfAllocFailLsa_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 27),
    _JuniOspfAllocFailLsa_Type()
)
juniOspfAllocFailLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfAllocFailLsa.setStatus("current")
_JuniOspfAllocFailLsd_Type = Counter32
_JuniOspfAllocFailLsd_Object = MibScalar
juniOspfAllocFailLsd = _JuniOspfAllocFailLsd_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 28),
    _JuniOspfAllocFailLsd_Type()
)
juniOspfAllocFailLsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfAllocFailLsd.setStatus("current")
_JuniOspfAllocFailDbRequest_Type = Counter32
_JuniOspfAllocFailDbRequest_Object = MibScalar
juniOspfAllocFailDbRequest = _JuniOspfAllocFailDbRequest_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 29),
    _JuniOspfAllocFailDbRequest_Type()
)
juniOspfAllocFailDbRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfAllocFailDbRequest.setStatus("current")
_JuniOspfAllocFailRtx_Type = Counter32
_JuniOspfAllocFailRtx_Object = MibScalar
juniOspfAllocFailRtx = _JuniOspfAllocFailRtx_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 30),
    _JuniOspfAllocFailRtx_Type()
)
juniOspfAllocFailRtx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfAllocFailRtx.setStatus("current")
_JuniOspfAllocFailAck_Type = Counter32
_JuniOspfAllocFailAck_Object = MibScalar
juniOspfAllocFailAck = _JuniOspfAllocFailAck_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 31),
    _JuniOspfAllocFailAck_Type()
)
juniOspfAllocFailAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfAllocFailAck.setStatus("current")
_JuniOspfAllocFailDbPkt_Type = Counter32
_JuniOspfAllocFailDbPkt_Object = MibScalar
juniOspfAllocFailDbPkt = _JuniOspfAllocFailDbPkt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 32),
    _JuniOspfAllocFailDbPkt_Type()
)
juniOspfAllocFailDbPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfAllocFailDbPkt.setStatus("current")
_JuniOspfAllocFailCirc_Type = Counter32
_JuniOspfAllocFailCirc_Object = MibScalar
juniOspfAllocFailCirc = _JuniOspfAllocFailCirc_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 33),
    _JuniOspfAllocFailCirc_Type()
)
juniOspfAllocFailCirc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfAllocFailCirc.setStatus("current")
_JuniOspfAllocFailPkt_Type = Counter32
_JuniOspfAllocFailPkt_Object = MibScalar
juniOspfAllocFailPkt = _JuniOspfAllocFailPkt_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 34),
    _JuniOspfAllocFailPkt_Type()
)
juniOspfAllocFailPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfAllocFailPkt.setStatus("current")
_JuniOspfOperState_Type = TruthValue
_JuniOspfOperState_Object = MibScalar
juniOspfOperState = _JuniOspfOperState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 35),
    _JuniOspfOperState_Type()
)
juniOspfOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfOperState.setStatus("current")


class _JuniOspfVpnRouteTag_Type(Unsigned32):
    """Custom type juniOspfVpnRouteTag based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JuniOspfVpnRouteTag_Type.__name__ = "Unsigned32"
_JuniOspfVpnRouteTag_Object = MibScalar
juniOspfVpnRouteTag = _JuniOspfVpnRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 36),
    _JuniOspfVpnRouteTag_Type()
)
juniOspfVpnRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfVpnRouteTag.setStatus("current")


class _JuniOspfDomainId_Type(Unsigned32):
    """Custom type juniOspfDomainId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_JuniOspfDomainId_Type.__name__ = "Unsigned32"
_JuniOspfDomainId_Object = MibScalar
juniOspfDomainId = _JuniOspfDomainId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 37),
    _JuniOspfDomainId_Type()
)
juniOspfDomainId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfDomainId.setStatus("current")
_JuniOspfMplsTeRtrIdIfIndex_Type = InterfaceIndexOrZero
_JuniOspfMplsTeRtrIdIfIndex_Object = MibScalar
juniOspfMplsTeRtrIdIfIndex = _JuniOspfMplsTeRtrIdIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 1, 38),
    _JuniOspfMplsTeRtrIdIfIndex_Type()
)
juniOspfMplsTeRtrIdIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfMplsTeRtrIdIfIndex.setStatus("current")
_JuniOspfAreaTable_Object = MibTable
juniOspfAreaTable = _JuniOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    juniOspfAreaTable.setStatus("current")
_JuniOspfAreaEntry_Object = MibTableRow
juniOspfAreaEntry = _JuniOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    juniOspfAreaEntry.setStatus("current")


class _JuniOspfAreaType_Type(Integer32):
    """Custom type juniOspfAreaType based on Integer32"""
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


_JuniOspfAreaType_Type.__name__ = "Integer32"
_JuniOspfAreaType_Object = MibTableColumn
juniOspfAreaType = _JuniOspfAreaType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 2, 1, 1),
    _JuniOspfAreaType_Type()
)
juniOspfAreaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfAreaType.setStatus("current")
_JuniOspfAreaTeCapable_Type = TruthValue
_JuniOspfAreaTeCapable_Object = MibTableColumn
juniOspfAreaTeCapable = _JuniOspfAreaTeCapable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 2, 1, 2),
    _JuniOspfAreaTeCapable_Type()
)
juniOspfAreaTeCapable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniOspfAreaTeCapable.setStatus("current")
_JuniOspfIfTable_Object = MibTable
juniOspfIfTable = _JuniOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7)
)
if mibBuilder.loadTexts:
    juniOspfIfTable.setStatus("current")
_JuniOspfIfEntry_Object = MibTableRow
juniOspfIfEntry = _JuniOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1)
)
if mibBuilder.loadTexts:
    juniOspfIfEntry.setStatus("current")


class _JuniOspfIfCost_Type(Integer32):
    """Custom type juniOspfIfCost based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JuniOspfIfCost_Type.__name__ = "Integer32"
_JuniOspfIfCost_Object = MibTableColumn
juniOspfIfCost = _JuniOspfIfCost_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 1),
    _JuniOspfIfCost_Type()
)
juniOspfIfCost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfIfCost.setStatus("current")
_JuniOspfIfMask_Type = IpAddress
_JuniOspfIfMask_Object = MibTableColumn
juniOspfIfMask = _JuniOspfIfMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 2),
    _JuniOspfIfMask_Type()
)
juniOspfIfMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfIfMask.setStatus("current")


class _JuniOspfIfPassiveFlag_Type(Integer32):
    """Custom type juniOspfIfPassiveFlag based on Integer32"""
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


_JuniOspfIfPassiveFlag_Type.__name__ = "Integer32"
_JuniOspfIfPassiveFlag_Object = MibTableColumn
juniOspfIfPassiveFlag = _JuniOspfIfPassiveFlag_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 3),
    _JuniOspfIfPassiveFlag_Type()
)
juniOspfIfPassiveFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfIfPassiveFlag.setStatus("current")
_JuniOspfIfNbrCount_Type = Counter32
_JuniOspfIfNbrCount_Object = MibTableColumn
juniOspfIfNbrCount = _JuniOspfIfNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 4),
    _JuniOspfIfNbrCount_Type()
)
juniOspfIfNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfIfNbrCount.setStatus("current")
_JuniOspfIfAdjNbrCount_Type = Counter32
_JuniOspfIfAdjNbrCount_Object = MibTableColumn
juniOspfIfAdjNbrCount = _JuniOspfIfAdjNbrCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 5),
    _JuniOspfIfAdjNbrCount_Type()
)
juniOspfIfAdjNbrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfIfAdjNbrCount.setStatus("current")


class _JuniOspfIfMd5AuthKey_Type(OctetString):
    """Custom type juniOspfIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniOspfIfMd5AuthKey_Type.__name__ = "OctetString"
_JuniOspfIfMd5AuthKey_Object = MibTableColumn
juniOspfIfMd5AuthKey = _JuniOspfIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 6),
    _JuniOspfIfMd5AuthKey_Type()
)
juniOspfIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfIfMd5AuthKey.setStatus("current")


class _JuniOspfIfMd5AuthKeyId_Type(Integer32):
    """Custom type juniOspfIfMd5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniOspfIfMd5AuthKeyId_Type.__name__ = "Integer32"
_JuniOspfIfMd5AuthKeyId_Object = MibTableColumn
juniOspfIfMd5AuthKeyId = _JuniOspfIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 7, 1, 7),
    _JuniOspfIfMd5AuthKeyId_Type()
)
juniOspfIfMd5AuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfIfMd5AuthKeyId.setStatus("current")
_JuniOspfIfBFDTable_Object = MibTable
juniOspfIfBFDTable = _JuniOspfIfBFDTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 8)
)
if mibBuilder.loadTexts:
    juniOspfIfBFDTable.setStatus("current")
_JuniOspfIfBFDEntry_Object = MibTableRow
juniOspfIfBFDEntry = _JuniOspfIfBFDEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 8, 1)
)
if mibBuilder.loadTexts:
    juniOspfIfBFDEntry.setStatus("current")


class _JuniOspfIfBfdEnable_Type(TruthValue):
    """Custom type juniOspfIfBfdEnable based on TruthValue"""


_JuniOspfIfBfdEnable_Object = MibTableColumn
juniOspfIfBfdEnable = _JuniOspfIfBfdEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 8, 1, 1),
    _JuniOspfIfBfdEnable_Type()
)
juniOspfIfBfdEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfIfBfdEnable.setStatus("current")


class _JuniOspfIfBfdMinRxInterval_Type(Integer32):
    """Custom type juniOspfIfBfdMinRxInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_JuniOspfIfBfdMinRxInterval_Type.__name__ = "Integer32"
_JuniOspfIfBfdMinRxInterval_Object = MibTableColumn
juniOspfIfBfdMinRxInterval = _JuniOspfIfBfdMinRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 8, 1, 2),
    _JuniOspfIfBfdMinRxInterval_Type()
)
juniOspfIfBfdMinRxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfIfBfdMinRxInterval.setStatus("current")


class _JuniOspfIfBfdMinTxInterval_Type(Integer32):
    """Custom type juniOspfIfBfdMinTxInterval based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 65535),
    )


_JuniOspfIfBfdMinTxInterval_Type.__name__ = "Integer32"
_JuniOspfIfBfdMinTxInterval_Object = MibTableColumn
juniOspfIfBfdMinTxInterval = _JuniOspfIfBfdMinTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 8, 1, 3),
    _JuniOspfIfBfdMinTxInterval_Type()
)
juniOspfIfBfdMinTxInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfIfBfdMinTxInterval.setStatus("current")


class _JuniOspfIfBfdMultiplier_Type(Integer32):
    """Custom type juniOspfIfBfdMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniOspfIfBfdMultiplier_Type.__name__ = "Integer32"
_JuniOspfIfBfdMultiplier_Object = MibTableColumn
juniOspfIfBfdMultiplier = _JuniOspfIfBfdMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 8, 1, 4),
    _JuniOspfIfBfdMultiplier_Type()
)
juniOspfIfBfdMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfIfBfdMultiplier.setStatus("current")
_JuniOspfVirtIfTable_Object = MibTable
juniOspfVirtIfTable = _JuniOspfVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 9)
)
if mibBuilder.loadTexts:
    juniOspfVirtIfTable.setStatus("current")
_JuniOspfVirtIfEntry_Object = MibTableRow
juniOspfVirtIfEntry = _JuniOspfVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 9, 1)
)
if mibBuilder.loadTexts:
    juniOspfVirtIfEntry.setStatus("current")


class _JuniOspfVirtIfMd5AuthKey_Type(OctetString):
    """Custom type juniOspfVirtIfMd5AuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniOspfVirtIfMd5AuthKey_Type.__name__ = "OctetString"
_JuniOspfVirtIfMd5AuthKey_Object = MibTableColumn
juniOspfVirtIfMd5AuthKey = _JuniOspfVirtIfMd5AuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 9, 1, 1),
    _JuniOspfVirtIfMd5AuthKey_Type()
)
juniOspfVirtIfMd5AuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfVirtIfMd5AuthKey.setStatus("current")


class _JuniOspfVirtIfMd5AuthKeyId_Type(Integer32):
    """Custom type juniOspfVirtIfMd5AuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_JuniOspfVirtIfMd5AuthKeyId_Type.__name__ = "Integer32"
_JuniOspfVirtIfMd5AuthKeyId_Object = MibTableColumn
juniOspfVirtIfMd5AuthKeyId = _JuniOspfVirtIfMd5AuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 9, 1, 2),
    _JuniOspfVirtIfMd5AuthKeyId_Type()
)
juniOspfVirtIfMd5AuthKeyId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfVirtIfMd5AuthKeyId.setStatus("current")
_JuniOspfNbrTable_Object = MibTable
juniOspfNbrTable = _JuniOspfNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 10)
)
if mibBuilder.loadTexts:
    juniOspfNbrTable.setStatus("current")
_JuniOspfNbrEntry_Object = MibTableRow
juniOspfNbrEntry = _JuniOspfNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 10, 1)
)
if mibBuilder.loadTexts:
    juniOspfNbrEntry.setStatus("current")
_JuniOspfNbrLocalIpAddr_Type = IpAddress
_JuniOspfNbrLocalIpAddr_Object = MibTableColumn
juniOspfNbrLocalIpAddr = _JuniOspfNbrLocalIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 10, 1, 1),
    _JuniOspfNbrLocalIpAddr_Type()
)
juniOspfNbrLocalIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfNbrLocalIpAddr.setStatus("current")
_JuniOspfNbrDR_Type = IpAddress
_JuniOspfNbrDR_Object = MibTableColumn
juniOspfNbrDR = _JuniOspfNbrDR_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 10, 1, 2),
    _JuniOspfNbrDR_Type()
)
juniOspfNbrDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfNbrDR.setStatus("current")
_JuniOspfNbrBDR_Type = IpAddress
_JuniOspfNbrBDR_Object = MibTableColumn
juniOspfNbrBDR = _JuniOspfNbrBDR_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 10, 1, 3),
    _JuniOspfNbrBDR_Type()
)
juniOspfNbrBDR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfNbrBDR.setStatus("current")
_JuniOspfSummImportTable_Object = MibTable
juniOspfSummImportTable = _JuniOspfSummImportTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15)
)
if mibBuilder.loadTexts:
    juniOspfSummImportTable.setStatus("current")
_JuniOspfSummImportEntry_Object = MibTableRow
juniOspfSummImportEntry = _JuniOspfSummImportEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15, 1)
)
juniOspfSummImportEntry.setIndexNames(
    (0, "Juniper-OSPF-MIB", "juniOspfSummAggNet"),
    (0, "Juniper-OSPF-MIB", "juniOspfSummAggMask"),
)
if mibBuilder.loadTexts:
    juniOspfSummImportEntry.setStatus("current")
_JuniOspfSummAggNet_Type = IpAddress
_JuniOspfSummAggNet_Object = MibTableColumn
juniOspfSummAggNet = _JuniOspfSummAggNet_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15, 1, 1),
    _JuniOspfSummAggNet_Type()
)
juniOspfSummAggNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfSummAggNet.setStatus("current")
_JuniOspfSummAggMask_Type = IpAddress
_JuniOspfSummAggMask_Object = MibTableColumn
juniOspfSummAggMask = _JuniOspfSummAggMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15, 1, 2),
    _JuniOspfSummAggMask_Type()
)
juniOspfSummAggMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfSummAggMask.setStatus("current")


class _JuniOspfSummAdminStat_Type(Integer32):
    """Custom type juniOspfSummAdminStat based on Integer32"""
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


_JuniOspfSummAdminStat_Type.__name__ = "Integer32"
_JuniOspfSummAdminStat_Object = MibTableColumn
juniOspfSummAdminStat = _JuniOspfSummAdminStat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15, 1, 3),
    _JuniOspfSummAdminStat_Type()
)
juniOspfSummAdminStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfSummAdminStat.setStatus("current")
_JuniOspfSummRowStatus_Type = RowStatus
_JuniOspfSummRowStatus_Object = MibTableColumn
juniOspfSummRowStatus = _JuniOspfSummRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 15, 1, 4),
    _JuniOspfSummRowStatus_Type()
)
juniOspfSummRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfSummRowStatus.setStatus("current")
_JuniOspfMd5IntfTable_Object = MibTable
juniOspfMd5IntfTable = _JuniOspfMd5IntfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16)
)
if mibBuilder.loadTexts:
    juniOspfMd5IntfTable.setStatus("current")
_JuniOspfMd5IntfEntry_Object = MibTableRow
juniOspfMd5IntfEntry = _JuniOspfMd5IntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16, 1)
)
juniOspfMd5IntfEntry.setIndexNames(
    (0, "OSPF-MIB", "ospfIfIpAddress"),
    (0, "OSPF-MIB", "ospfAddressLessIf"),
    (0, "Juniper-OSPF-MIB", "juniOspfMd5IntfKeyId"),
)
if mibBuilder.loadTexts:
    juniOspfMd5IntfEntry.setStatus("current")


class _JuniOspfMd5IntfKeyId_Type(Integer32):
    """Custom type juniOspfMd5IntfKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniOspfMd5IntfKeyId_Type.__name__ = "Integer32"
_JuniOspfMd5IntfKeyId_Object = MibTableColumn
juniOspfMd5IntfKeyId = _JuniOspfMd5IntfKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16, 1, 1),
    _JuniOspfMd5IntfKeyId_Type()
)
juniOspfMd5IntfKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfMd5IntfKeyId.setStatus("current")
_JuniOspfMd5IntfKeyActive_Type = TruthValue
_JuniOspfMd5IntfKeyActive_Object = MibTableColumn
juniOspfMd5IntfKeyActive = _JuniOspfMd5IntfKeyActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16, 1, 2),
    _JuniOspfMd5IntfKeyActive_Type()
)
juniOspfMd5IntfKeyActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfMd5IntfKeyActive.setStatus("deprecated")


class _JuniOspfMd5IntfAuthKey_Type(OctetString):
    """Custom type juniOspfMd5IntfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniOspfMd5IntfAuthKey_Type.__name__ = "OctetString"
_JuniOspfMd5IntfAuthKey_Object = MibTableColumn
juniOspfMd5IntfAuthKey = _JuniOspfMd5IntfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16, 1, 3),
    _JuniOspfMd5IntfAuthKey_Type()
)
juniOspfMd5IntfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfMd5IntfAuthKey.setStatus("current")
_JuniOspfMd5IntfRowStatus_Type = RowStatus
_JuniOspfMd5IntfRowStatus_Object = MibTableColumn
juniOspfMd5IntfRowStatus = _JuniOspfMd5IntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 16, 1, 4),
    _JuniOspfMd5IntfRowStatus_Type()
)
juniOspfMd5IntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfMd5IntfRowStatus.setStatus("current")
_JuniOspfMd5VirtIntfTable_Object = MibTable
juniOspfMd5VirtIntfTable = _JuniOspfMd5VirtIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17)
)
if mibBuilder.loadTexts:
    juniOspfMd5VirtIntfTable.setStatus("current")
_JuniOspfMd5VirtIntfEntry_Object = MibTableRow
juniOspfMd5VirtIntfEntry = _JuniOspfMd5VirtIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1)
)
juniOspfMd5VirtIntfEntry.setIndexNames(
    (0, "Juniper-OSPF-MIB", "juniOspfMd5VirtIntfAreaId"),
    (0, "Juniper-OSPF-MIB", "juniOspfMd5VirtIntfNeighbor"),
    (0, "Juniper-OSPF-MIB", "juniOspfMd5VirtIntfKeyId"),
)
if mibBuilder.loadTexts:
    juniOspfMd5VirtIntfEntry.setStatus("current")
_JuniOspfMd5VirtIntfAreaId_Type = IpAddress
_JuniOspfMd5VirtIntfAreaId_Object = MibTableColumn
juniOspfMd5VirtIntfAreaId = _JuniOspfMd5VirtIntfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 1),
    _JuniOspfMd5VirtIntfAreaId_Type()
)
juniOspfMd5VirtIntfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfMd5VirtIntfAreaId.setStatus("current")
_JuniOspfMd5VirtIntfNeighbor_Type = IpAddress
_JuniOspfMd5VirtIntfNeighbor_Object = MibTableColumn
juniOspfMd5VirtIntfNeighbor = _JuniOspfMd5VirtIntfNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 2),
    _JuniOspfMd5VirtIntfNeighbor_Type()
)
juniOspfMd5VirtIntfNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfMd5VirtIntfNeighbor.setStatus("current")


class _JuniOspfMd5VirtIntfKeyId_Type(Integer32):
    """Custom type juniOspfMd5VirtIntfKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_JuniOspfMd5VirtIntfKeyId_Type.__name__ = "Integer32"
_JuniOspfMd5VirtIntfKeyId_Object = MibTableColumn
juniOspfMd5VirtIntfKeyId = _JuniOspfMd5VirtIntfKeyId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 3),
    _JuniOspfMd5VirtIntfKeyId_Type()
)
juniOspfMd5VirtIntfKeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfMd5VirtIntfKeyId.setStatus("current")
_JuniOspfMd5VirtIntfKeyActive_Type = TruthValue
_JuniOspfMd5VirtIntfKeyActive_Object = MibTableColumn
juniOspfMd5VirtIntfKeyActive = _JuniOspfMd5VirtIntfKeyActive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 4),
    _JuniOspfMd5VirtIntfKeyActive_Type()
)
juniOspfMd5VirtIntfKeyActive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfMd5VirtIntfKeyActive.setStatus("deprecated")


class _JuniOspfMd5VirtIntfAuthKey_Type(OctetString):
    """Custom type juniOspfMd5VirtIntfAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_JuniOspfMd5VirtIntfAuthKey_Type.__name__ = "OctetString"
_JuniOspfMd5VirtIntfAuthKey_Object = MibTableColumn
juniOspfMd5VirtIntfAuthKey = _JuniOspfMd5VirtIntfAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 5),
    _JuniOspfMd5VirtIntfAuthKey_Type()
)
juniOspfMd5VirtIntfAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfMd5VirtIntfAuthKey.setStatus("current")
_JuniOspfMd5VirtIntfRowStatus_Type = RowStatus
_JuniOspfMd5VirtIntfRowStatus_Object = MibTableColumn
juniOspfMd5VirtIntfRowStatus = _JuniOspfMd5VirtIntfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 17, 1, 6),
    _JuniOspfMd5VirtIntfRowStatus_Type()
)
juniOspfMd5VirtIntfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfMd5VirtIntfRowStatus.setStatus("current")
_JuniOspfNetworkRangeTable_Object = MibTable
juniOspfNetworkRangeTable = _JuniOspfNetworkRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18)
)
if mibBuilder.loadTexts:
    juniOspfNetworkRangeTable.setStatus("current")
_JuniOspfNetworkRangeEntry_Object = MibTableRow
juniOspfNetworkRangeEntry = _JuniOspfNetworkRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18, 1)
)
juniOspfNetworkRangeEntry.setIndexNames(
    (0, "Juniper-OSPF-MIB", "juniOspfNetRangeNet"),
    (0, "Juniper-OSPF-MIB", "juniOspfNetRangeMask"),
    (0, "Juniper-OSPF-MIB", "juniOspfNetRangeAreaId"),
)
if mibBuilder.loadTexts:
    juniOspfNetworkRangeEntry.setStatus("current")
_JuniOspfNetRangeNet_Type = IpAddress
_JuniOspfNetRangeNet_Object = MibTableColumn
juniOspfNetRangeNet = _JuniOspfNetRangeNet_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18, 1, 1),
    _JuniOspfNetRangeNet_Type()
)
juniOspfNetRangeNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfNetRangeNet.setStatus("current")
_JuniOspfNetRangeMask_Type = IpAddress
_JuniOspfNetRangeMask_Object = MibTableColumn
juniOspfNetRangeMask = _JuniOspfNetRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18, 1, 2),
    _JuniOspfNetRangeMask_Type()
)
juniOspfNetRangeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfNetRangeMask.setStatus("current")
_JuniOspfNetRangeAreaId_Type = IpAddress
_JuniOspfNetRangeAreaId_Object = MibTableColumn
juniOspfNetRangeAreaId = _JuniOspfNetRangeAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18, 1, 3),
    _JuniOspfNetRangeAreaId_Type()
)
juniOspfNetRangeAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniOspfNetRangeAreaId.setStatus("current")
_JuniOspfNetRangeRowStatus_Type = RowStatus
_JuniOspfNetRangeRowStatus_Object = MibTableColumn
juniOspfNetRangeRowStatus = _JuniOspfNetRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 1, 18, 1, 4),
    _JuniOspfNetRangeRowStatus_Type()
)
juniOspfNetRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniOspfNetRangeRowStatus.setStatus("current")
_JuniOspfConformance_ObjectIdentity = ObjectIdentity
juniOspfConformance = _JuniOspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4)
)
_JuniOspfCompliances_ObjectIdentity = ObjectIdentity
juniOspfCompliances = _JuniOspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 1)
)
_JuniOspfGroups_ObjectIdentity = ObjectIdentity
juniOspfGroups = _JuniOspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2)
)
ospfAreaEntry.registerAugmentions(
    ("Juniper-OSPF-MIB",
     "juniOspfAreaEntry")
)
juniOspfAreaEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("Juniper-OSPF-MIB",
     "juniOspfIfEntry")
)
juniOspfIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("Juniper-OSPF-MIB",
     "juniOspfIfBFDEntry")
)
juniOspfIfBFDEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("Juniper-OSPF-MIB",
     "juniOspfVirtIfEntry")
)
juniOspfVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
ospfNbrEntry.registerAugmentions(
    ("Juniper-OSPF-MIB",
     "juniOspfNbrEntry")
)
juniOspfNbrEntry.setIndexNames(*ospfNbrEntry.getIndexNames())

# Managed Objects groups

juniOspfBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 1)
)
juniOspfBasicGroup.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfProcessId"),
        ("Juniper-OSPF-MIB", "juniOspfMaxPathSplits"),
        ("Juniper-OSPF-MIB", "juniOspfSpfHoldInterval"),
        ("Juniper-OSPF-MIB", "juniOspfNumActiveAreas"),
        ("Juniper-OSPF-MIB", "juniOspfSpfTime"),
        ("Juniper-OSPF-MIB", "juniOspfRefBw"),
        ("Juniper-OSPF-MIB", "juniOspfAutoVlink"),
        ("Juniper-OSPF-MIB", "juniOspfIntraDistance"),
        ("Juniper-OSPF-MIB", "juniOspfInterDistance"),
        ("Juniper-OSPF-MIB", "juniOspfExtDistance"),
        ("Juniper-OSPF-MIB", "juniOspfHelloPktsRcv"),
        ("Juniper-OSPF-MIB", "juniOspfDDPktsRcv"),
        ("Juniper-OSPF-MIB", "juniOspfLsrPktsRcv"),
        ("Juniper-OSPF-MIB", "juniOspfLsuPktsRcv"),
        ("Juniper-OSPF-MIB", "juniOspfLsAckPktsRcv"),
        ("Juniper-OSPF-MIB", "juniOspfTotalRcv"),
        ("Juniper-OSPF-MIB", "juniOspfLsaDiscardCnt"),
        ("Juniper-OSPF-MIB", "juniOspfHelloPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfDDPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfLsrPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfLsuPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfLsAckPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfErrPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfTotalSent"),
        ("Juniper-OSPF-MIB", "juniOspfCsumErrPkts"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailNbr"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailLsa"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailLsd"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailDbRequest"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailRtx"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailAck"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailDbPkt"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailCirc"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailPkt"),
        ("Juniper-OSPF-MIB", "juniOspfOperState"))
)
if mibBuilder.loadTexts:
    juniOspfBasicGroup.setStatus("obsolete")

juniOspfIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 2)
)
juniOspfIfGroup.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfIfCost"),
        ("Juniper-OSPF-MIB", "juniOspfIfMask"),
        ("Juniper-OSPF-MIB", "juniOspfIfPassiveFlag"),
        ("Juniper-OSPF-MIB", "juniOspfIfNbrCount"),
        ("Juniper-OSPF-MIB", "juniOspfIfAdjNbrCount"),
        ("Juniper-OSPF-MIB", "juniOspfIfMd5AuthKey"),
        ("Juniper-OSPF-MIB", "juniOspfIfMd5AuthKeyId"))
)
if mibBuilder.loadTexts:
    juniOspfIfGroup.setStatus("current")

juniOspfAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 3)
)
juniOspfAreaGroup.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfAreaType"),
        ("Juniper-OSPF-MIB", "juniOspfAreaTeCapable"))
)
if mibBuilder.loadTexts:
    juniOspfAreaGroup.setStatus("current")

juniOspfVirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 4)
)
juniOspfVirtIfGroup.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfVirtIfMd5AuthKey"),
        ("Juniper-OSPF-MIB", "juniOspfVirtIfMd5AuthKeyId"))
)
if mibBuilder.loadTexts:
    juniOspfVirtIfGroup.setStatus("current")

juniOspfNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 5)
)
juniOspfNbrGroup.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfNbrLocalIpAddr"),
        ("Juniper-OSPF-MIB", "juniOspfNbrDR"),
        ("Juniper-OSPF-MIB", "juniOspfNbrBDR"))
)
if mibBuilder.loadTexts:
    juniOspfNbrGroup.setStatus("current")

juniOspfSummImportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 6)
)
juniOspfSummImportGroup.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfSummAggNet"),
        ("Juniper-OSPF-MIB", "juniOspfSummAggMask"),
        ("Juniper-OSPF-MIB", "juniOspfSummAdminStat"),
        ("Juniper-OSPF-MIB", "juniOspfSummRowStatus"))
)
if mibBuilder.loadTexts:
    juniOspfSummImportGroup.setStatus("current")

juniOspfMd5IntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 7)
)
juniOspfMd5IntfGroup.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfMd5IntfKeyId"),
        ("Juniper-OSPF-MIB", "juniOspfMd5IntfKeyActive"),
        ("Juniper-OSPF-MIB", "juniOspfMd5IntfAuthKey"),
        ("Juniper-OSPF-MIB", "juniOspfMd5IntfRowStatus"))
)
if mibBuilder.loadTexts:
    juniOspfMd5IntfGroup.setStatus("current")

juniOspfMd5VirtIntfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 8)
)
juniOspfMd5VirtIntfGroup.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfMd5VirtIntfAreaId"),
        ("Juniper-OSPF-MIB", "juniOspfMd5VirtIntfNeighbor"),
        ("Juniper-OSPF-MIB", "juniOspfMd5VirtIntfKeyId"),
        ("Juniper-OSPF-MIB", "juniOspfMd5VirtIntfKeyActive"),
        ("Juniper-OSPF-MIB", "juniOspfMd5VirtIntfAuthKey"),
        ("Juniper-OSPF-MIB", "juniOspfMd5VirtIntfRowStatus"))
)
if mibBuilder.loadTexts:
    juniOspfMd5VirtIntfGroup.setStatus("current")

juniOspfNetRangeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 9)
)
juniOspfNetRangeGroup.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfNetRangeNet"),
        ("Juniper-OSPF-MIB", "juniOspfNetRangeMask"),
        ("Juniper-OSPF-MIB", "juniOspfNetRangeAreaId"),
        ("Juniper-OSPF-MIB", "juniOspfNetRangeRowStatus"))
)
if mibBuilder.loadTexts:
    juniOspfNetRangeGroup.setStatus("current")

juniOspfBasicGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 10)
)
juniOspfBasicGroup2.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfProcessId"),
        ("Juniper-OSPF-MIB", "juniOspfMaxPathSplits"),
        ("Juniper-OSPF-MIB", "juniOspfSpfHoldInterval"),
        ("Juniper-OSPF-MIB", "juniOspfNumActiveAreas"),
        ("Juniper-OSPF-MIB", "juniOspfSpfTime"),
        ("Juniper-OSPF-MIB", "juniOspfRefBw"),
        ("Juniper-OSPF-MIB", "juniOspfAutoVlink"),
        ("Juniper-OSPF-MIB", "juniOspfIntraDistance"),
        ("Juniper-OSPF-MIB", "juniOspfInterDistance"),
        ("Juniper-OSPF-MIB", "juniOspfExtDistance"),
        ("Juniper-OSPF-MIB", "juniOspfHelloPktsRcv"),
        ("Juniper-OSPF-MIB", "juniOspfDDPktsRcv"),
        ("Juniper-OSPF-MIB", "juniOspfLsrPktsRcv"),
        ("Juniper-OSPF-MIB", "juniOspfLsuPktsRcv"),
        ("Juniper-OSPF-MIB", "juniOspfLsAckPktsRcv"),
        ("Juniper-OSPF-MIB", "juniOspfTotalRcv"),
        ("Juniper-OSPF-MIB", "juniOspfLsaDiscardCnt"),
        ("Juniper-OSPF-MIB", "juniOspfHelloPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfDDPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfLsrPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfLsuPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfLsAckPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfErrPktsSent"),
        ("Juniper-OSPF-MIB", "juniOspfTotalSent"),
        ("Juniper-OSPF-MIB", "juniOspfCsumErrPkts"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailNbr"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailLsa"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailLsd"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailDbRequest"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailRtx"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailAck"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailDbPkt"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailCirc"),
        ("Juniper-OSPF-MIB", "juniOspfAllocFailPkt"),
        ("Juniper-OSPF-MIB", "juniOspfOperState"),
        ("Juniper-OSPF-MIB", "juniOspfVpnRouteTag"),
        ("Juniper-OSPF-MIB", "juniOspfDomainId"),
        ("Juniper-OSPF-MIB", "juniOspfMplsTeRtrIdIfIndex"))
)
if mibBuilder.loadTexts:
    juniOspfBasicGroup2.setStatus("current")

juniOspfIfBFDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 2, 11)
)
juniOspfIfBFDGroup.setObjects(
      *(("Juniper-OSPF-MIB", "juniOspfIfBfdEnable"),
        ("Juniper-OSPF-MIB", "juniOspfIfBfdMinRxInterval"),
        ("Juniper-OSPF-MIB", "juniOspfIfBfdMinTxInterval"),
        ("Juniper-OSPF-MIB", "juniOspfIfBfdMultiplier"))
)
if mibBuilder.loadTexts:
    juniOspfIfBFDGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniOspfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniOspfCompliance.setStatus(
        "obsolete"
    )

juniOspfCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniOspfCompliance2.setStatus(
        "obsolete"
    )

juniOspfCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 14, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniOspfCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-OSPF-MIB",
    **{"juniOspfMIB": juniOspfMIB,
       "juniOspfObjects": juniOspfObjects,
       "juniOspfGeneralGroup": juniOspfGeneralGroup,
       "juniOspfProcessId": juniOspfProcessId,
       "juniOspfMaxPathSplits": juniOspfMaxPathSplits,
       "juniOspfSpfHoldInterval": juniOspfSpfHoldInterval,
       "juniOspfNumActiveAreas": juniOspfNumActiveAreas,
       "juniOspfSpfTime": juniOspfSpfTime,
       "juniOspfRefBw": juniOspfRefBw,
       "juniOspfAutoVlink": juniOspfAutoVlink,
       "juniOspfIntraDistance": juniOspfIntraDistance,
       "juniOspfInterDistance": juniOspfInterDistance,
       "juniOspfExtDistance": juniOspfExtDistance,
       "juniOspfHelloPktsRcv": juniOspfHelloPktsRcv,
       "juniOspfDDPktsRcv": juniOspfDDPktsRcv,
       "juniOspfLsrPktsRcv": juniOspfLsrPktsRcv,
       "juniOspfLsuPktsRcv": juniOspfLsuPktsRcv,
       "juniOspfLsAckPktsRcv": juniOspfLsAckPktsRcv,
       "juniOspfTotalRcv": juniOspfTotalRcv,
       "juniOspfLsaDiscardCnt": juniOspfLsaDiscardCnt,
       "juniOspfHelloPktsSent": juniOspfHelloPktsSent,
       "juniOspfDDPktsSent": juniOspfDDPktsSent,
       "juniOspfLsrPktsSent": juniOspfLsrPktsSent,
       "juniOspfLsuPktsSent": juniOspfLsuPktsSent,
       "juniOspfLsAckPktsSent": juniOspfLsAckPktsSent,
       "juniOspfErrPktsSent": juniOspfErrPktsSent,
       "juniOspfTotalSent": juniOspfTotalSent,
       "juniOspfCsumErrPkts": juniOspfCsumErrPkts,
       "juniOspfAllocFailNbr": juniOspfAllocFailNbr,
       "juniOspfAllocFailLsa": juniOspfAllocFailLsa,
       "juniOspfAllocFailLsd": juniOspfAllocFailLsd,
       "juniOspfAllocFailDbRequest": juniOspfAllocFailDbRequest,
       "juniOspfAllocFailRtx": juniOspfAllocFailRtx,
       "juniOspfAllocFailAck": juniOspfAllocFailAck,
       "juniOspfAllocFailDbPkt": juniOspfAllocFailDbPkt,
       "juniOspfAllocFailCirc": juniOspfAllocFailCirc,
       "juniOspfAllocFailPkt": juniOspfAllocFailPkt,
       "juniOspfOperState": juniOspfOperState,
       "juniOspfVpnRouteTag": juniOspfVpnRouteTag,
       "juniOspfDomainId": juniOspfDomainId,
       "juniOspfMplsTeRtrIdIfIndex": juniOspfMplsTeRtrIdIfIndex,
       "juniOspfAreaTable": juniOspfAreaTable,
       "juniOspfAreaEntry": juniOspfAreaEntry,
       "juniOspfAreaType": juniOspfAreaType,
       "juniOspfAreaTeCapable": juniOspfAreaTeCapable,
       "juniOspfIfTable": juniOspfIfTable,
       "juniOspfIfEntry": juniOspfIfEntry,
       "juniOspfIfCost": juniOspfIfCost,
       "juniOspfIfMask": juniOspfIfMask,
       "juniOspfIfPassiveFlag": juniOspfIfPassiveFlag,
       "juniOspfIfNbrCount": juniOspfIfNbrCount,
       "juniOspfIfAdjNbrCount": juniOspfIfAdjNbrCount,
       "juniOspfIfMd5AuthKey": juniOspfIfMd5AuthKey,
       "juniOspfIfMd5AuthKeyId": juniOspfIfMd5AuthKeyId,
       "juniOspfIfBFDTable": juniOspfIfBFDTable,
       "juniOspfIfBFDEntry": juniOspfIfBFDEntry,
       "juniOspfIfBfdEnable": juniOspfIfBfdEnable,
       "juniOspfIfBfdMinRxInterval": juniOspfIfBfdMinRxInterval,
       "juniOspfIfBfdMinTxInterval": juniOspfIfBfdMinTxInterval,
       "juniOspfIfBfdMultiplier": juniOspfIfBfdMultiplier,
       "juniOspfVirtIfTable": juniOspfVirtIfTable,
       "juniOspfVirtIfEntry": juniOspfVirtIfEntry,
       "juniOspfVirtIfMd5AuthKey": juniOspfVirtIfMd5AuthKey,
       "juniOspfVirtIfMd5AuthKeyId": juniOspfVirtIfMd5AuthKeyId,
       "juniOspfNbrTable": juniOspfNbrTable,
       "juniOspfNbrEntry": juniOspfNbrEntry,
       "juniOspfNbrLocalIpAddr": juniOspfNbrLocalIpAddr,
       "juniOspfNbrDR": juniOspfNbrDR,
       "juniOspfNbrBDR": juniOspfNbrBDR,
       "juniOspfSummImportTable": juniOspfSummImportTable,
       "juniOspfSummImportEntry": juniOspfSummImportEntry,
       "juniOspfSummAggNet": juniOspfSummAggNet,
       "juniOspfSummAggMask": juniOspfSummAggMask,
       "juniOspfSummAdminStat": juniOspfSummAdminStat,
       "juniOspfSummRowStatus": juniOspfSummRowStatus,
       "juniOspfMd5IntfTable": juniOspfMd5IntfTable,
       "juniOspfMd5IntfEntry": juniOspfMd5IntfEntry,
       "juniOspfMd5IntfKeyId": juniOspfMd5IntfKeyId,
       "juniOspfMd5IntfKeyActive": juniOspfMd5IntfKeyActive,
       "juniOspfMd5IntfAuthKey": juniOspfMd5IntfAuthKey,
       "juniOspfMd5IntfRowStatus": juniOspfMd5IntfRowStatus,
       "juniOspfMd5VirtIntfTable": juniOspfMd5VirtIntfTable,
       "juniOspfMd5VirtIntfEntry": juniOspfMd5VirtIntfEntry,
       "juniOspfMd5VirtIntfAreaId": juniOspfMd5VirtIntfAreaId,
       "juniOspfMd5VirtIntfNeighbor": juniOspfMd5VirtIntfNeighbor,
       "juniOspfMd5VirtIntfKeyId": juniOspfMd5VirtIntfKeyId,
       "juniOspfMd5VirtIntfKeyActive": juniOspfMd5VirtIntfKeyActive,
       "juniOspfMd5VirtIntfAuthKey": juniOspfMd5VirtIntfAuthKey,
       "juniOspfMd5VirtIntfRowStatus": juniOspfMd5VirtIntfRowStatus,
       "juniOspfNetworkRangeTable": juniOspfNetworkRangeTable,
       "juniOspfNetworkRangeEntry": juniOspfNetworkRangeEntry,
       "juniOspfNetRangeNet": juniOspfNetRangeNet,
       "juniOspfNetRangeMask": juniOspfNetRangeMask,
       "juniOspfNetRangeAreaId": juniOspfNetRangeAreaId,
       "juniOspfNetRangeRowStatus": juniOspfNetRangeRowStatus,
       "juniOspfConformance": juniOspfConformance,
       "juniOspfCompliances": juniOspfCompliances,
       "juniOspfCompliance": juniOspfCompliance,
       "juniOspfCompliance2": juniOspfCompliance2,
       "juniOspfCompliance3": juniOspfCompliance3,
       "juniOspfGroups": juniOspfGroups,
       "juniOspfBasicGroup": juniOspfBasicGroup,
       "juniOspfIfGroup": juniOspfIfGroup,
       "juniOspfAreaGroup": juniOspfAreaGroup,
       "juniOspfVirtIfGroup": juniOspfVirtIfGroup,
       "juniOspfNbrGroup": juniOspfNbrGroup,
       "juniOspfSummImportGroup": juniOspfSummImportGroup,
       "juniOspfMd5IntfGroup": juniOspfMd5IntfGroup,
       "juniOspfMd5VirtIntfGroup": juniOspfMd5VirtIntfGroup,
       "juniOspfNetRangeGroup": juniOspfNetRangeGroup,
       "juniOspfBasicGroup2": juniOspfBasicGroup2,
       "juniOspfIfBFDGroup": juniOspfIfBFDGroup}
)
