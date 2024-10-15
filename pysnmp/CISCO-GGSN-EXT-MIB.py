# SNMP MIB module (CISCO-GGSN-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-GGSN-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:48 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(TimeIntervalMin,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "TimeIntervalMin")

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

ciscoGgsnExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647)
)
ciscoGgsnExtMIB.setRevisions(
        ("2011-03-18 00:00",
         "2010-06-11 00:00",
         "2009-09-17 00:00",
         "2009-01-30 00:00",
         "2008-01-29 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoGgsnExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoGgsnExtMIBNotifs = _CiscoGgsnExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 0)
)
_CiscoGgsnExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoGgsnExtMIBObjects = _CiscoGgsnExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1)
)
_CiscoGgsnExtStatistics_ObjectIdentity = ObjectIdentity
ciscoGgsnExtStatistics = _CiscoGgsnExtStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1)
)
_CGgsnExtNoWaitSgsnLocalDelPDPs_Type = Counter32
_CGgsnExtNoWaitSgsnLocalDelPDPs_Object = MibScalar
cGgsnExtNoWaitSgsnLocalDelPDPs = _CGgsnExtNoWaitSgsnLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 1),
    _CGgsnExtNoWaitSgsnLocalDelPDPs_Type()
)
cGgsnExtNoWaitSgsnLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtNoWaitSgsnLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtNoWaitSgsnLocalDelPDPs.setUnits("PDP Context")
_CGgsnExtNoReqSgsnLocalDelPDPs_Type = Counter32
_CGgsnExtNoReqSgsnLocalDelPDPs_Object = MibScalar
cGgsnExtNoReqSgsnLocalDelPDPs = _CGgsnExtNoReqSgsnLocalDelPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 2),
    _CGgsnExtNoReqSgsnLocalDelPDPs_Type()
)
cGgsnExtNoReqSgsnLocalDelPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtNoReqSgsnLocalDelPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtNoReqSgsnLocalDelPDPs.setUnits("PDP Context")
_CGgsnExtSentPdpUpdateReqs_Type = Counter32
_CGgsnExtSentPdpUpdateReqs_Object = MibScalar
cGgsnExtSentPdpUpdateReqs = _CGgsnExtSentPdpUpdateReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 3),
    _CGgsnExtSentPdpUpdateReqs_Type()
)
cGgsnExtSentPdpUpdateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtSentPdpUpdateReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtSentPdpUpdateReqs.setUnits("messages")
_CGgsnExtRcvdSuccPdpUpdateResponses_Type = Counter32
_CGgsnExtRcvdSuccPdpUpdateResponses_Object = MibScalar
cGgsnExtRcvdSuccPdpUpdateResponses = _CGgsnExtRcvdSuccPdpUpdateResponses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 4),
    _CGgsnExtRcvdSuccPdpUpdateResponses_Type()
)
cGgsnExtRcvdSuccPdpUpdateResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtRcvdSuccPdpUpdateResponses.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtRcvdSuccPdpUpdateResponses.setUnits("messages")
_CGgsnExtRcvdCoaMsgs_Type = Counter32
_CGgsnExtRcvdCoaMsgs_Object = MibScalar
cGgsnExtRcvdCoaMsgs = _CGgsnExtRcvdCoaMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 5),
    _CGgsnExtRcvdCoaMsgs_Type()
)
cGgsnExtRcvdCoaMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtRcvdCoaMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtRcvdCoaMsgs.setUnits("messages")
_CGgsnExtDiscardedCoaMsgs_Type = Counter32
_CGgsnExtDiscardedCoaMsgs_Object = MibScalar
cGgsnExtDiscardedCoaMsgs = _CGgsnExtDiscardedCoaMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 6),
    _CGgsnExtDiscardedCoaMsgs_Type()
)
cGgsnExtDiscardedCoaMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtDiscardedCoaMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtDiscardedCoaMsgs.setUnits("messages")
_CGgsnExtSentCoaUpdateReqs_Type = Counter32
_CGgsnExtSentCoaUpdateReqs_Object = MibScalar
cGgsnExtSentCoaUpdateReqs = _CGgsnExtSentCoaUpdateReqs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 7),
    _CGgsnExtSentCoaUpdateReqs_Type()
)
cGgsnExtSentCoaUpdateReqs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtSentCoaUpdateReqs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtSentCoaUpdateReqs.setUnits("messages")
_CGgsnExtSentErrorIndications_Type = Counter32
_CGgsnExtSentErrorIndications_Object = MibScalar
cGgsnExtSentErrorIndications = _CGgsnExtSentErrorIndications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 8),
    _CGgsnExtSentErrorIndications_Type()
)
cGgsnExtSentErrorIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtSentErrorIndications.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtSentErrorIndications.setUnits("messages")
_CGgsnExtRcvdErrorIndications_Type = Counter32
_CGgsnExtRcvdErrorIndications_Object = MibScalar
cGgsnExtRcvdErrorIndications = _CGgsnExtRcvdErrorIndications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 9),
    _CGgsnExtRcvdErrorIndications_Type()
)
cGgsnExtRcvdErrorIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtRcvdErrorIndications.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtRcvdErrorIndications.setUnits("messages")
_CGgsnExtTotalDtEnabled_Type = Counter32
_CGgsnExtTotalDtEnabled_Object = MibScalar
cGgsnExtTotalDtEnabled = _CGgsnExtTotalDtEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 10),
    _CGgsnExtTotalDtEnabled_Type()
)
cGgsnExtTotalDtEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTotalDtEnabled.setStatus("current")
_CGgsnExtRcvdDtPdpErrorIndications_Type = Counter32
_CGgsnExtRcvdDtPdpErrorIndications_Object = MibScalar
cGgsnExtRcvdDtPdpErrorIndications = _CGgsnExtRcvdDtPdpErrorIndications_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 11),
    _CGgsnExtRcvdDtPdpErrorIndications_Type()
)
cGgsnExtRcvdDtPdpErrorIndications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtRcvdDtPdpErrorIndications.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtRcvdDtPdpErrorIndications.setUnits("messages")
_CGgsnExtTotalDtUpdFailDeletedPDPs_Type = Counter32
_CGgsnExtTotalDtUpdFailDeletedPDPs_Object = MibScalar
cGgsnExtTotalDtUpdFailDeletedPDPs = _CGgsnExtTotalDtUpdFailDeletedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 12),
    _CGgsnExtTotalDtUpdFailDeletedPDPs_Type()
)
cGgsnExtTotalDtUpdFailDeletedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTotalDtUpdFailDeletedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtTotalDtUpdFailDeletedPDPs.setUnits("PDP Context")
_CGgsnExtThruputStatsTable_Object = MibTable
cGgsnExtThruputStatsTable = _CGgsnExtThruputStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 13)
)
if mibBuilder.loadTexts:
    cGgsnExtThruputStatsTable.setStatus("current")
_CGgsnExtThruputStatsEntry_Object = MibTableRow
cGgsnExtThruputStatsEntry = _CGgsnExtThruputStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 13, 1)
)
cGgsnExtThruputStatsEntry.setIndexNames(
    (0, "CISCO-GGSN-EXT-MIB", "cGgsnExtThruputInterval"),
)
if mibBuilder.loadTexts:
    cGgsnExtThruputStatsEntry.setStatus("current")


class _CGgsnExtThruputInterval_Type(Integer32):
    """Custom type cGgsnExtThruputInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGgsnExtThruputInterval_Type.__name__ = "Integer32"
_CGgsnExtThruputInterval_Object = MibTableColumn
cGgsnExtThruputInterval = _CGgsnExtThruputInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 13, 1, 1),
    _CGgsnExtThruputInterval_Type()
)
cGgsnExtThruputInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnExtThruputInterval.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtThruputInterval.setUnits("minutes")


class _CGgsnExtThruputLastCollected_Type(Integer32):
    """Custom type cGgsnExtThruputLastCollected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CGgsnExtThruputLastCollected_Type.__name__ = "Integer32"
_CGgsnExtThruputLastCollected_Object = MibTableColumn
cGgsnExtThruputLastCollected = _CGgsnExtThruputLastCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 13, 1, 2),
    _CGgsnExtThruputLastCollected_Type()
)
cGgsnExtThruputLastCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtThruputLastCollected.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtThruputLastCollected.setUnits("minutes")
_CGgsnExtUpstreamByteCount_Type = CounterBasedGauge64
_CGgsnExtUpstreamByteCount_Object = MibTableColumn
cGgsnExtUpstreamByteCount = _CGgsnExtUpstreamByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 13, 1, 3),
    _CGgsnExtUpstreamByteCount_Type()
)
cGgsnExtUpstreamByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtUpstreamByteCount.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtUpstreamByteCount.setUnits("bytes")
_CGgsnExtDownstreamByteCount_Type = CounterBasedGauge64
_CGgsnExtDownstreamByteCount_Object = MibTableColumn
cGgsnExtDownstreamByteCount = _CGgsnExtDownstreamByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 13, 1, 4),
    _CGgsnExtDownstreamByteCount_Type()
)
cGgsnExtDownstreamByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtDownstreamByteCount.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtDownstreamByteCount.setUnits("bytes")
_CGgsnExtUpstreamPktCount_Type = Gauge32
_CGgsnExtUpstreamPktCount_Object = MibTableColumn
cGgsnExtUpstreamPktCount = _CGgsnExtUpstreamPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 13, 1, 5),
    _CGgsnExtUpstreamPktCount_Type()
)
cGgsnExtUpstreamPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtUpstreamPktCount.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtUpstreamPktCount.setUnits("packets")
_CGgsnExtDownstreamPktCount_Type = Gauge32
_CGgsnExtDownstreamPktCount_Object = MibTableColumn
cGgsnExtDownstreamPktCount = _CGgsnExtDownstreamPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 13, 1, 6),
    _CGgsnExtDownstreamPktCount_Type()
)
cGgsnExtDownstreamPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtDownstreamPktCount.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtDownstreamPktCount.setUnits("packets")
_CGgsnExtPdpNonExistentMsgs_Type = Counter32
_CGgsnExtPdpNonExistentMsgs_Object = MibScalar
cGgsnExtPdpNonExistentMsgs = _CGgsnExtPdpNonExistentMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 14),
    _CGgsnExtPdpNonExistentMsgs_Type()
)
cGgsnExtPdpNonExistentMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtPdpNonExistentMsgs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtPdpNonExistentMsgs.setUnits("messages")
_CGgsnExtCallRateStatsTable_Object = MibTable
cGgsnExtCallRateStatsTable = _CGgsnExtCallRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 15)
)
if mibBuilder.loadTexts:
    cGgsnExtCallRateStatsTable.setStatus("current")
_CGgsnExtCallRateStatsEntry_Object = MibTableRow
cGgsnExtCallRateStatsEntry = _CGgsnExtCallRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 15, 1)
)
cGgsnExtCallRateStatsEntry.setIndexNames(
    (0, "CISCO-GGSN-EXT-MIB", "cGgsnExtCallRateStatsInterval"),
)
if mibBuilder.loadTexts:
    cGgsnExtCallRateStatsEntry.setStatus("current")


class _CGgsnExtCallRateStatsInterval_Type(Unsigned32):
    """Custom type cGgsnExtCallRateStatsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGgsnExtCallRateStatsInterval_Type.__name__ = "Unsigned32"
_CGgsnExtCallRateStatsInterval_Object = MibTableColumn
cGgsnExtCallRateStatsInterval = _CGgsnExtCallRateStatsInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 15, 1, 1),
    _CGgsnExtCallRateStatsInterval_Type()
)
cGgsnExtCallRateStatsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnExtCallRateStatsInterval.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtCallRateStatsInterval.setUnits("minutes")


class _CGgsnExtCallRateLastCollected_Type(Unsigned32):
    """Custom type cGgsnExtCallRateLastCollected based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CGgsnExtCallRateLastCollected_Type.__name__ = "Unsigned32"
_CGgsnExtCallRateLastCollected_Object = MibTableColumn
cGgsnExtCallRateLastCollected = _CGgsnExtCallRateLastCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 15, 1, 2),
    _CGgsnExtCallRateLastCollected_Type()
)
cGgsnExtCallRateLastCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtCallRateLastCollected.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtCallRateLastCollected.setUnits("minutes")
_CGgsnExtCreatedPDPs_Type = Gauge32
_CGgsnExtCreatedPDPs_Object = MibTableColumn
cGgsnExtCreatedPDPs = _CGgsnExtCreatedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 15, 1, 3),
    _CGgsnExtCreatedPDPs_Type()
)
cGgsnExtCreatedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtCreatedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtCreatedPDPs.setUnits("PDP Context")
_CGgsnExtDeletedPDPs_Type = Gauge32
_CGgsnExtDeletedPDPs_Object = MibTableColumn
cGgsnExtDeletedPDPs = _CGgsnExtDeletedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 15, 1, 4),
    _CGgsnExtDeletedPDPs_Type()
)
cGgsnExtDeletedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtDeletedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtDeletedPDPs.setUnits("PDP Context")
_CGgsnExtHistCallRateStatsTable_Object = MibTable
cGgsnExtHistCallRateStatsTable = _CGgsnExtHistCallRateStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 16)
)
if mibBuilder.loadTexts:
    cGgsnExtHistCallRateStatsTable.setStatus("current")
_CGgsnExtHistCallRateStatsEntry_Object = MibTableRow
cGgsnExtHistCallRateStatsEntry = _CGgsnExtHistCallRateStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 16, 1)
)
cGgsnExtHistCallRateStatsEntry.setIndexNames(
    (0, "CISCO-GGSN-EXT-MIB", "cGgsnExtHistCallRateIndex"),
)
if mibBuilder.loadTexts:
    cGgsnExtHistCallRateStatsEntry.setStatus("current")


class _CGgsnExtHistCallRateIndex_Type(Unsigned32):
    """Custom type cGgsnExtHistCallRateIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CGgsnExtHistCallRateIndex_Type.__name__ = "Unsigned32"
_CGgsnExtHistCallRateIndex_Object = MibTableColumn
cGgsnExtHistCallRateIndex = _CGgsnExtHistCallRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 16, 1, 1),
    _CGgsnExtHistCallRateIndex_Type()
)
cGgsnExtHistCallRateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnExtHistCallRateIndex.setStatus("current")


class _CGgsnExtHistCallRateInterval_Type(TimeIntervalMin):
    """Custom type cGgsnExtHistCallRateInterval based on TimeIntervalMin"""
    subtypeSpec = TimeIntervalMin.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGgsnExtHistCallRateInterval_Type.__name__ = "TimeIntervalMin"
_CGgsnExtHistCallRateInterval_Object = MibTableColumn
cGgsnExtHistCallRateInterval = _CGgsnExtHistCallRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 16, 1, 2),
    _CGgsnExtHistCallRateInterval_Type()
)
cGgsnExtHistCallRateInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtHistCallRateInterval.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtHistCallRateInterval.setUnits("minutes")
_CGgsnExtHistCallRateLastCollected_Type = TimeStamp
_CGgsnExtHistCallRateLastCollected_Object = MibTableColumn
cGgsnExtHistCallRateLastCollected = _CGgsnExtHistCallRateLastCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 16, 1, 3),
    _CGgsnExtHistCallRateLastCollected_Type()
)
cGgsnExtHistCallRateLastCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtHistCallRateLastCollected.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtHistCallRateLastCollected.setUnits("minutes")
_CGgsnExtHistCreatedPDPs_Type = Counter32
_CGgsnExtHistCreatedPDPs_Object = MibTableColumn
cGgsnExtHistCreatedPDPs = _CGgsnExtHistCreatedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 16, 1, 4),
    _CGgsnExtHistCreatedPDPs_Type()
)
cGgsnExtHistCreatedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtHistCreatedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtHistCreatedPDPs.setUnits("PDP Context")
_CGgsnExtHistDeletedPDPs_Type = Counter32
_CGgsnExtHistDeletedPDPs_Object = MibTableColumn
cGgsnExtHistDeletedPDPs = _CGgsnExtHistDeletedPDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 16, 1, 5),
    _CGgsnExtHistDeletedPDPs_Type()
)
cGgsnExtHistDeletedPDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtHistDeletedPDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtHistDeletedPDPs.setUnits("PDP Context")
_CGgsnExtHistThruputStatsTable_Object = MibTable
cGgsnExtHistThruputStatsTable = _CGgsnExtHistThruputStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 17)
)
if mibBuilder.loadTexts:
    cGgsnExtHistThruputStatsTable.setStatus("current")
_CGgsnExtHistThruputStatsEntry_Object = MibTableRow
cGgsnExtHistThruputStatsEntry = _CGgsnExtHistThruputStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 17, 1)
)
cGgsnExtHistThruputStatsEntry.setIndexNames(
    (0, "CISCO-GGSN-EXT-MIB", "cGgsnExtHistThruputIndex"),
    (0, "CISCO-GGSN-EXT-MIB", "cGgsnExtHistThruputInterval"),
)
if mibBuilder.loadTexts:
    cGgsnExtHistThruputStatsEntry.setStatus("current")


class _CGgsnExtHistThruputIndex_Type(Unsigned32):
    """Custom type cGgsnExtHistThruputIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CGgsnExtHistThruputIndex_Type.__name__ = "Unsigned32"
_CGgsnExtHistThruputIndex_Object = MibTableColumn
cGgsnExtHistThruputIndex = _CGgsnExtHistThruputIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 17, 1, 1),
    _CGgsnExtHistThruputIndex_Type()
)
cGgsnExtHistThruputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnExtHistThruputIndex.setStatus("current")


class _CGgsnExtHistThruputInterval_Type(TimeIntervalMin):
    """Custom type cGgsnExtHistThruputInterval based on TimeIntervalMin"""
    subtypeSpec = TimeIntervalMin.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_CGgsnExtHistThruputInterval_Type.__name__ = "TimeIntervalMin"
_CGgsnExtHistThruputInterval_Object = MibTableColumn
cGgsnExtHistThruputInterval = _CGgsnExtHistThruputInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 17, 1, 2),
    _CGgsnExtHistThruputInterval_Type()
)
cGgsnExtHistThruputInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnExtHistThruputInterval.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtHistThruputInterval.setUnits("minutes")
_CGgsnExtHistThruputLastCollected_Type = TimeStamp
_CGgsnExtHistThruputLastCollected_Object = MibTableColumn
cGgsnExtHistThruputLastCollected = _CGgsnExtHistThruputLastCollected_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 17, 1, 3),
    _CGgsnExtHistThruputLastCollected_Type()
)
cGgsnExtHistThruputLastCollected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtHistThruputLastCollected.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtHistThruputLastCollected.setUnits("minutes")
_CGgsnExtHistUpstreamByteCount_Type = Counter64
_CGgsnExtHistUpstreamByteCount_Object = MibTableColumn
cGgsnExtHistUpstreamByteCount = _CGgsnExtHistUpstreamByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 17, 1, 4),
    _CGgsnExtHistUpstreamByteCount_Type()
)
cGgsnExtHistUpstreamByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtHistUpstreamByteCount.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtHistUpstreamByteCount.setUnits("bytes")
_CGgsnExtHistDownstreamByteCount_Type = Counter64
_CGgsnExtHistDownstreamByteCount_Object = MibTableColumn
cGgsnExtHistDownstreamByteCount = _CGgsnExtHistDownstreamByteCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 17, 1, 5),
    _CGgsnExtHistDownstreamByteCount_Type()
)
cGgsnExtHistDownstreamByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtHistDownstreamByteCount.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtHistDownstreamByteCount.setUnits("bytes")
_CGgsnExtHistUpstreamPktCount_Type = Counter32
_CGgsnExtHistUpstreamPktCount_Object = MibTableColumn
cGgsnExtHistUpstreamPktCount = _CGgsnExtHistUpstreamPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 17, 1, 6),
    _CGgsnExtHistUpstreamPktCount_Type()
)
cGgsnExtHistUpstreamPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtHistUpstreamPktCount.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtHistUpstreamPktCount.setUnits("packets")
_CGgsnExtHistDownstreamPktCount_Type = Counter32
_CGgsnExtHistDownstreamPktCount_Object = MibTableColumn
cGgsnExtHistDownstreamPktCount = _CGgsnExtHistDownstreamPktCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 17, 1, 7),
    _CGgsnExtHistDownstreamPktCount_Type()
)
cGgsnExtHistDownstreamPktCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtHistDownstreamPktCount.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtHistDownstreamPktCount.setUnits("packets")
_CGgsnExtSubscriberTable_Object = MibTable
cGgsnExtSubscriberTable = _CGgsnExtSubscriberTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 18)
)
if mibBuilder.loadTexts:
    cGgsnExtSubscriberTable.setStatus("current")
_CGgsnExtSubscriberEntry_Object = MibTableRow
cGgsnExtSubscriberEntry = _CGgsnExtSubscriberEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 18, 1)
)
cGgsnExtSubscriberEntry.setIndexNames(
    (0, "CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberMsisdn"),
)
if mibBuilder.loadTexts:
    cGgsnExtSubscriberEntry.setStatus("current")


class _CGgsnExtSubscriberMsisdn_Type(SnmpAdminString):
    """Custom type cGgsnExtSubscriberMsisdn based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_CGgsnExtSubscriberMsisdn_Type.__name__ = "SnmpAdminString"
_CGgsnExtSubscriberMsisdn_Object = MibTableColumn
cGgsnExtSubscriberMsisdn = _CGgsnExtSubscriberMsisdn_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 18, 1, 1),
    _CGgsnExtSubscriberMsisdn_Type()
)
cGgsnExtSubscriberMsisdn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberMsisdn.setStatus("current")


class _CGgsnExtSubscriberTid_Type(SnmpAdminString):
    """Custom type cGgsnExtSubscriberTid based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_CGgsnExtSubscriberTid_Type.__name__ = "SnmpAdminString"
_CGgsnExtSubscriberTid_Object = MibTableColumn
cGgsnExtSubscriberTid = _CGgsnExtSubscriberTid_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 18, 1, 2),
    _CGgsnExtSubscriberTid_Type()
)
cGgsnExtSubscriberTid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberTid.setStatus("current")
_CGgsnExtSubscriberMSAddrType_Type = InetAddressType
_CGgsnExtSubscriberMSAddrType_Object = MibTableColumn
cGgsnExtSubscriberMSAddrType = _CGgsnExtSubscriberMSAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 18, 1, 3),
    _CGgsnExtSubscriberMSAddrType_Type()
)
cGgsnExtSubscriberMSAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberMSAddrType.setStatus("current")
_CGgsnExtSubscriberMSAddr_Type = InetAddress
_CGgsnExtSubscriberMSAddr_Object = MibTableColumn
cGgsnExtSubscriberMSAddr = _CGgsnExtSubscriberMSAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 18, 1, 4),
    _CGgsnExtSubscriberMSAddr_Type()
)
cGgsnExtSubscriberMSAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberMSAddr.setStatus("current")


class _CGgsnExtSubscriberSource_Type(Integer32):
    """Custom type cGgsnExtSubscriberSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("pdpAddrSrcDhcp", 5),
          ("pdpAddrSrcIpcp", 6),
          ("pdpAddrSrcLocalPool", 3),
          ("pdpAddrSrcNone", 1),
          ("pdpAddrSrcRadius", 4),
          ("pdpAddrSrcStatic", 2))
    )


_CGgsnExtSubscriberSource_Type.__name__ = "Integer32"
_CGgsnExtSubscriberSource_Object = MibTableColumn
cGgsnExtSubscriberSource = _CGgsnExtSubscriberSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 18, 1, 5),
    _CGgsnExtSubscriberSource_Type()
)
cGgsnExtSubscriberSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberSource.setStatus("current")
_CGgsnExtSubscriberSGSNAddrType_Type = InetAddressType
_CGgsnExtSubscriberSGSNAddrType_Object = MibTableColumn
cGgsnExtSubscriberSGSNAddrType = _CGgsnExtSubscriberSGSNAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 18, 1, 6),
    _CGgsnExtSubscriberSGSNAddrType_Type()
)
cGgsnExtSubscriberSGSNAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberSGSNAddrType.setStatus("current")
_CGgsnExtSubscriberSGSNAddr_Type = InetAddress
_CGgsnExtSubscriberSGSNAddr_Object = MibTableColumn
cGgsnExtSubscriberSGSNAddr = _CGgsnExtSubscriberSGSNAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 18, 1, 7),
    _CGgsnExtSubscriberSGSNAddr_Type()
)
cGgsnExtSubscriberSGSNAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberSGSNAddr.setStatus("current")


class _CGgsnExtSubscriberAPN_Type(SnmpAdminString):
    """Custom type cGgsnExtSubscriberAPN based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_CGgsnExtSubscriberAPN_Type.__name__ = "SnmpAdminString"
_CGgsnExtSubscriberAPN_Object = MibTableColumn
cGgsnExtSubscriberAPN = _CGgsnExtSubscriberAPN_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 18, 1, 8),
    _CGgsnExtSubscriberAPN_Type()
)
cGgsnExtSubscriberAPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberAPN.setStatus("current")
_CGgsnExtTotalCreatedv4v6Pdps_Type = Counter32
_CGgsnExtTotalCreatedv4v6Pdps_Object = MibScalar
cGgsnExtTotalCreatedv4v6Pdps = _CGgsnExtTotalCreatedv4v6Pdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 19),
    _CGgsnExtTotalCreatedv4v6Pdps_Type()
)
cGgsnExtTotalCreatedv4v6Pdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTotalCreatedv4v6Pdps.setStatus("current")
_CGgsnExtTotalDeletedv4v6Pdps_Type = Counter32
_CGgsnExtTotalDeletedv4v6Pdps_Object = MibScalar
cGgsnExtTotalDeletedv4v6Pdps = _CGgsnExtTotalDeletedv4v6Pdps_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 20),
    _CGgsnExtTotalDeletedv4v6Pdps_Type()
)
cGgsnExtTotalDeletedv4v6Pdps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTotalDeletedv4v6Pdps.setStatus("current")
_CiscoGgsnExtTraceStatistics_ObjectIdentity = ObjectIdentity
ciscoGgsnExtTraceStatistics = _CiscoGgsnExtTraceStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21)
)
_CGgsnExtTraceActivatedSessions_Type = Counter32
_CGgsnExtTraceActivatedSessions_Object = MibScalar
cGgsnExtTraceActivatedSessions = _CGgsnExtTraceActivatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 1),
    _CGgsnExtTraceActivatedSessions_Type()
)
cGgsnExtTraceActivatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceActivatedSessions.setStatus("current")
_CGgsnExtTraceSignalActivations_Type = Counter32
_CGgsnExtTraceSignalActivations_Object = MibScalar
cGgsnExtTraceSignalActivations = _CGgsnExtTraceSignalActivations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 2),
    _CGgsnExtTraceSignalActivations_Type()
)
cGgsnExtTraceSignalActivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceSignalActivations.setStatus("current")
_CGgsnExtTraceMgmtActivations_Type = Counter32
_CGgsnExtTraceMgmtActivations_Object = MibScalar
cGgsnExtTraceMgmtActivations = _CGgsnExtTraceMgmtActivations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 3),
    _CGgsnExtTraceMgmtActivations_Type()
)
cGgsnExtTraceMgmtActivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceMgmtActivations.setStatus("current")
_CGgsnExtTraceNewSesActivations_Type = Counter32
_CGgsnExtTraceNewSesActivations_Object = MibScalar
cGgsnExtTraceNewSesActivations = _CGgsnExtTraceNewSesActivations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 4),
    _CGgsnExtTraceNewSesActivations_Type()
)
cGgsnExtTraceNewSesActivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceNewSesActivations.setStatus("current")
_CGgsnExtTraceActSesActivations_Type = Counter32
_CGgsnExtTraceActSesActivations_Object = MibScalar
cGgsnExtTraceActSesActivations = _CGgsnExtTraceActSesActivations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 5),
    _CGgsnExtTraceActSesActivations_Type()
)
cGgsnExtTraceActSesActivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceActSesActivations.setStatus("current")
_CGgsnExtTraceSignalActivFailures_Type = Counter32
_CGgsnExtTraceSignalActivFailures_Object = MibScalar
cGgsnExtTraceSignalActivFailures = _CGgsnExtTraceSignalActivFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 6),
    _CGgsnExtTraceSignalActivFailures_Type()
)
cGgsnExtTraceSignalActivFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceSignalActivFailures.setStatus("current")
_CGgsnExtTraceMgmtActivFailures_Type = Counter32
_CGgsnExtTraceMgmtActivFailures_Object = MibScalar
cGgsnExtTraceMgmtActivFailures = _CGgsnExtTraceMgmtActivFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 7),
    _CGgsnExtTraceMgmtActivFailures_Type()
)
cGgsnExtTraceMgmtActivFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceMgmtActivFailures.setStatus("current")
_CGgsnExtTraceDeactivatedSessions_Type = Counter32
_CGgsnExtTraceDeactivatedSessions_Object = MibScalar
cGgsnExtTraceDeactivatedSessions = _CGgsnExtTraceDeactivatedSessions_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 8),
    _CGgsnExtTraceDeactivatedSessions_Type()
)
cGgsnExtTraceDeactivatedSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceDeactivatedSessions.setStatus("current")
_CGgsnExtTraceSignalDeactivations_Type = Counter32
_CGgsnExtTraceSignalDeactivations_Object = MibScalar
cGgsnExtTraceSignalDeactivations = _CGgsnExtTraceSignalDeactivations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 9),
    _CGgsnExtTraceSignalDeactivations_Type()
)
cGgsnExtTraceSignalDeactivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceSignalDeactivations.setStatus("current")
_CGgsnExtTraceMgmtDeactivations_Type = Counter32
_CGgsnExtTraceMgmtDeactivations_Object = MibScalar
cGgsnExtTraceMgmtDeactivations = _CGgsnExtTraceMgmtDeactivations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 10),
    _CGgsnExtTraceMgmtDeactivations_Type()
)
cGgsnExtTraceMgmtDeactivations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceMgmtDeactivations.setStatus("current")
_CGgsnExtTraceSignalDeactivFailures_Type = Counter32
_CGgsnExtTraceSignalDeactivFailures_Object = MibScalar
cGgsnExtTraceSignalDeactivFailures = _CGgsnExtTraceSignalDeactivFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 11),
    _CGgsnExtTraceSignalDeactivFailures_Type()
)
cGgsnExtTraceSignalDeactivFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceSignalDeactivFailures.setStatus("current")
_CGgsnExtTraceMgmtDeactivFailures_Type = Counter32
_CGgsnExtTraceMgmtDeactivFailures_Object = MibScalar
cGgsnExtTraceMgmtDeactivFailures = _CGgsnExtTraceMgmtDeactivFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 21, 12),
    _CGgsnExtTraceMgmtDeactivFailures_Type()
)
cGgsnExtTraceMgmtDeactivFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceMgmtDeactivFailures.setStatus("current")
_CiscoGgsnExtTraceXmlStatistics_ObjectIdentity = ObjectIdentity
ciscoGgsnExtTraceXmlStatistics = _CiscoGgsnExtTraceXmlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 22)
)
_CGgsnExtTraceTotalXmlFiles_Type = Counter32
_CGgsnExtTraceTotalXmlFiles_Object = MibScalar
cGgsnExtTraceTotalXmlFiles = _CGgsnExtTraceTotalXmlFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 22, 1),
    _CGgsnExtTraceTotalXmlFiles_Type()
)
cGgsnExtTraceTotalXmlFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceTotalXmlFiles.setStatus("current")
_CGgsnExtTraceTotalXmlFailNotifFiles_Type = Counter32
_CGgsnExtTraceTotalXmlFailNotifFiles_Object = MibScalar
cGgsnExtTraceTotalXmlFailNotifFiles = _CGgsnExtTraceTotalXmlFailNotifFiles_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 22, 2),
    _CGgsnExtTraceTotalXmlFailNotifFiles_Type()
)
cGgsnExtTraceTotalXmlFailNotifFiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceTotalXmlFailNotifFiles.setStatus("current")
_CGgsnExtTraceXmlFileTransSucc_Type = Counter32
_CGgsnExtTraceXmlFileTransSucc_Object = MibScalar
cGgsnExtTraceXmlFileTransSucc = _CGgsnExtTraceXmlFileTransSucc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 22, 3),
    _CGgsnExtTraceXmlFileTransSucc_Type()
)
cGgsnExtTraceXmlFileTransSucc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceXmlFileTransSucc.setStatus("current")
_CGgsnExtTraceXmlFileTransPri_Type = Counter32
_CGgsnExtTraceXmlFileTransPri_Object = MibScalar
cGgsnExtTraceXmlFileTransPri = _CGgsnExtTraceXmlFileTransPri_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 22, 4),
    _CGgsnExtTraceXmlFileTransPri_Type()
)
cGgsnExtTraceXmlFileTransPri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceXmlFileTransPri.setStatus("current")
_CGgsnExtTraceXmlFileTransSec_Type = Counter32
_CGgsnExtTraceXmlFileTransSec_Object = MibScalar
cGgsnExtTraceXmlFileTransSec = _CGgsnExtTraceXmlFileTransSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 22, 5),
    _CGgsnExtTraceXmlFileTransSec_Type()
)
cGgsnExtTraceXmlFileTransSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceXmlFileTransSec.setStatus("current")
_CGgsnExtTraceXmlFileTotalTransFails_Type = Counter32
_CGgsnExtTraceXmlFileTotalTransFails_Object = MibScalar
cGgsnExtTraceXmlFileTotalTransFails = _CGgsnExtTraceXmlFileTotalTransFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 22, 6),
    _CGgsnExtTraceXmlFileTotalTransFails_Type()
)
cGgsnExtTraceXmlFileTotalTransFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceXmlFileTotalTransFails.setStatus("current")
_CGgsnExtTraceXmlFileTransPriFails_Type = Counter32
_CGgsnExtTraceXmlFileTransPriFails_Object = MibScalar
cGgsnExtTraceXmlFileTransPriFails = _CGgsnExtTraceXmlFileTransPriFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 22, 7),
    _CGgsnExtTraceXmlFileTransPriFails_Type()
)
cGgsnExtTraceXmlFileTransPriFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceXmlFileTransPriFails.setStatus("current")
_CGgsnExtTraceXmlFileTransRetries_Type = Counter32
_CGgsnExtTraceXmlFileTransRetries_Object = MibScalar
cGgsnExtTraceXmlFileTransRetries = _CGgsnExtTraceXmlFileTransRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 22, 8),
    _CGgsnExtTraceXmlFileTransRetries_Type()
)
cGgsnExtTraceXmlFileTransRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceXmlFileTransRetries.setStatus("current")
_CGgsnExtTraceXmlFileTransSecFails_Type = Counter32
_CGgsnExtTraceXmlFileTransSecFails_Object = MibScalar
cGgsnExtTraceXmlFileTransSecFails = _CGgsnExtTraceXmlFileTransSecFails_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 22, 9),
    _CGgsnExtTraceXmlFileTransSecFails_Type()
)
cGgsnExtTraceXmlFileTransSecFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceXmlFileTransSecFails.setStatus("current")
_CGgsnExtConditionalIEMissingMsgs_Type = Counter32
_CGgsnExtConditionalIEMissingMsgs_Object = MibScalar
cGgsnExtConditionalIEMissingMsgs = _CGgsnExtConditionalIEMissingMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 23),
    _CGgsnExtConditionalIEMissingMsgs_Type()
)
cGgsnExtConditionalIEMissingMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtConditionalIEMissingMsgs.setStatus("current")
_CGgsnExtInvalidReplyPeerMsgs_Type = Counter32
_CGgsnExtInvalidReplyPeerMsgs_Object = MibScalar
cGgsnExtInvalidReplyPeerMsgs = _CGgsnExtInvalidReplyPeerMsgs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 1, 24),
    _CGgsnExtInvalidReplyPeerMsgs_Type()
)
cGgsnExtInvalidReplyPeerMsgs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtInvalidReplyPeerMsgs.setStatus("current")
_CiscoGgsnExtConfigurations_ObjectIdentity = ObjectIdentity
ciscoGgsnExtConfigurations = _CiscoGgsnExtConfigurations_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2)
)


class _CGgsnExtAaaAccountInterPeriod_Type(Unsigned32):
    """Custom type cGgsnExtAaaAccountInterPeriod based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(15, 71582),
    )


_CGgsnExtAaaAccountInterPeriod_Type.__name__ = "Unsigned32"
_CGgsnExtAaaAccountInterPeriod_Object = MibScalar
cGgsnExtAaaAccountInterPeriod = _CGgsnExtAaaAccountInterPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 1),
    _CGgsnExtAaaAccountInterPeriod_Type()
)
cGgsnExtAaaAccountInterPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtAaaAccountInterPeriod.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtAaaAccountInterPeriod.setUnits("minutes")


class _CGgsnExtDfpCpuLoad_Type(Unsigned32):
    """Custom type cGgsnExtDfpCpuLoad based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 75),
    )


_CGgsnExtDfpCpuLoad_Type.__name__ = "Unsigned32"
_CGgsnExtDfpCpuLoad_Object = MibScalar
cGgsnExtDfpCpuLoad = _CGgsnExtDfpCpuLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 2),
    _CGgsnExtDfpCpuLoad_Type()
)
cGgsnExtDfpCpuLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtDfpCpuLoad.setStatus("current")


class _CGgsnExtDfpMemLoad_Type(Unsigned32):
    """Custom type cGgsnExtDfpMemLoad based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 75),
    )


_CGgsnExtDfpMemLoad_Type.__name__ = "Unsigned32"
_CGgsnExtDfpMemLoad_Object = MibScalar
cGgsnExtDfpMemLoad = _CGgsnExtDfpMemLoad_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 3),
    _CGgsnExtDfpMemLoad_Type()
)
cGgsnExtDfpMemLoad.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtDfpMemLoad.setStatus("current")


class _CGgsnExtThruputHistory_Type(Unsigned32):
    """Custom type cGgsnExtThruputHistory based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 100),
    )


_CGgsnExtThruputHistory_Type.__name__ = "Unsigned32"
_CGgsnExtThruputHistory_Object = MibScalar
cGgsnExtThruputHistory = _CGgsnExtThruputHistory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 4),
    _CGgsnExtThruputHistory_Type()
)
cGgsnExtThruputHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtThruputHistory.setStatus("current")


class _CGgsnExtCallRateInterval_Type(TimeIntervalMin):
    """Custom type cGgsnExtCallRateInterval based on TimeIntervalMin"""
    defaultValue = 0

    subtypeSpec = TimeIntervalMin.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CGgsnExtCallRateInterval_Type.__name__ = "TimeIntervalMin"
_CGgsnExtCallRateInterval_Object = MibScalar
cGgsnExtCallRateInterval = _CGgsnExtCallRateInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 5),
    _CGgsnExtCallRateInterval_Type()
)
cGgsnExtCallRateInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtCallRateInterval.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtCallRateInterval.setUnits("minutes")


class _CGgsnExtCallRateHistory_Type(Unsigned32):
    """Custom type cGgsnExtCallRateHistory based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_CGgsnExtCallRateHistory_Type.__name__ = "Unsigned32"
_CGgsnExtCallRateHistory_Object = MibScalar
cGgsnExtCallRateHistory = _CGgsnExtCallRateHistory_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 6),
    _CGgsnExtCallRateHistory_Type()
)
cGgsnExtCallRateHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtCallRateHistory.setStatus("current")


class _CGgsnExtPrepaidStandAlone_Type(TruthValue):
    """Custom type cGgsnExtPrepaidStandAlone based on TruthValue"""


_CGgsnExtPrepaidStandAlone_Object = MibScalar
cGgsnExtPrepaidStandAlone = _CGgsnExtPrepaidStandAlone_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 7),
    _CGgsnExtPrepaidStandAlone_Type()
)
cGgsnExtPrepaidStandAlone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtPrepaidStandAlone.setStatus("current")


class _CGgsnExtRedundancyEnabled_Type(TruthValue):
    """Custom type cGgsnExtRedundancyEnabled based on TruthValue"""


_CGgsnExtRedundancyEnabled_Object = MibScalar
cGgsnExtRedundancyEnabled = _CGgsnExtRedundancyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 8),
    _CGgsnExtRedundancyEnabled_Type()
)
cGgsnExtRedundancyEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtRedundancyEnabled.setStatus("current")


class _CGgsnExtChargSyncWindowSvcSeqnum_Type(Unsigned32):
    """Custom type cGgsnExtChargSyncWindowSvcSeqnum based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200),
    )


_CGgsnExtChargSyncWindowSvcSeqnum_Type.__name__ = "Unsigned32"
_CGgsnExtChargSyncWindowSvcSeqnum_Object = MibScalar
cGgsnExtChargSyncWindowSvcSeqnum = _CGgsnExtChargSyncWindowSvcSeqnum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 9),
    _CGgsnExtChargSyncWindowSvcSeqnum_Type()
)
cGgsnExtChargSyncWindowSvcSeqnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtChargSyncWindowSvcSeqnum.setStatus("current")


class _CGgsnExtChargSyncWindowCdrSeqnum_Type(Unsigned32):
    """Custom type cGgsnExtChargSyncWindowCdrSeqnum based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_CGgsnExtChargSyncWindowCdrSeqnum_Type.__name__ = "Unsigned32"
_CGgsnExtChargSyncWindowCdrSeqnum_Object = MibScalar
cGgsnExtChargSyncWindowCdrSeqnum = _CGgsnExtChargSyncWindowCdrSeqnum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 10),
    _CGgsnExtChargSyncWindowCdrSeqnum_Type()
)
cGgsnExtChargSyncWindowCdrSeqnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtChargSyncWindowCdrSeqnum.setStatus("current")


class _CGgsnExtChargSynWindowGtppSeqnum_Type(Unsigned32):
    """Custom type cGgsnExtChargSynWindowGtppSeqnum based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_CGgsnExtChargSynWindowGtppSeqnum_Type.__name__ = "Unsigned32"
_CGgsnExtChargSynWindowGtppSeqnum_Object = MibScalar
cGgsnExtChargSynWindowGtppSeqnum = _CGgsnExtChargSynWindowGtppSeqnum_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 11),
    _CGgsnExtChargSynWindowGtppSeqnum_Type()
)
cGgsnExtChargSynWindowGtppSeqnum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtChargSynWindowGtppSeqnum.setStatus("current")


class _CGgsnExtTraceBufferLimit_Type(Unsigned32):
    """Custom type cGgsnExtTraceBufferLimit based on Unsigned32"""
    defaultValue = 3000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2000, 10000),
    )


_CGgsnExtTraceBufferLimit_Type.__name__ = "Unsigned32"
_CGgsnExtTraceBufferLimit_Object = MibScalar
cGgsnExtTraceBufferLimit = _CGgsnExtTraceBufferLimit_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 12),
    _CGgsnExtTraceBufferLimit_Type()
)
cGgsnExtTraceBufferLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtTraceBufferLimit.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtTraceBufferLimit.setUnits("Bytes")


class _CGgsnExtTraceXmlTransferInterval_Type(Unsigned32):
    """Custom type cGgsnExtTraceXmlTransferInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_CGgsnExtTraceXmlTransferInterval_Type.__name__ = "Unsigned32"
_CGgsnExtTraceXmlTransferInterval_Object = MibScalar
cGgsnExtTraceXmlTransferInterval = _CGgsnExtTraceXmlTransferInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 13),
    _CGgsnExtTraceXmlTransferInterval_Type()
)
cGgsnExtTraceXmlTransferInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtTraceXmlTransferInterval.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtTraceXmlTransferInterval.setUnits("seconds")
_CGgsnExtSubscriberTraceProfileTable_Object = MibTable
cGgsnExtSubscriberTraceProfileTable = _CGgsnExtSubscriberTraceProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 14)
)
if mibBuilder.loadTexts:
    cGgsnExtSubscriberTraceProfileTable.setStatus("current")
_CGgsnExtSubscriberTraceProfileEntry_Object = MibTableRow
cGgsnExtSubscriberTraceProfileEntry = _CGgsnExtSubscriberTraceProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 14, 1)
)
cGgsnExtSubscriberTraceProfileEntry.setIndexNames(
    (0, "CISCO-GGSN-EXT-MIB", "cGgsnExtTraceProfile"),
)
if mibBuilder.loadTexts:
    cGgsnExtSubscriberTraceProfileEntry.setStatus("current")


class _CGgsnExtTraceProfile_Type(SnmpAdminString):
    """Custom type cGgsnExtTraceProfile based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CGgsnExtTraceProfile_Type.__name__ = "SnmpAdminString"
_CGgsnExtTraceProfile_Object = MibTableColumn
cGgsnExtTraceProfile = _CGgsnExtTraceProfile_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 14, 1, 1),
    _CGgsnExtTraceProfile_Type()
)
cGgsnExtTraceProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnExtTraceProfile.setStatus("current")
_CGgsnExtTracePrimaryUrl_Type = DisplayString
_CGgsnExtTracePrimaryUrl_Object = MibTableColumn
cGgsnExtTracePrimaryUrl = _CGgsnExtTracePrimaryUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 14, 1, 2),
    _CGgsnExtTracePrimaryUrl_Type()
)
cGgsnExtTracePrimaryUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnExtTracePrimaryUrl.setStatus("current")
_CGgsnExtTraceSecondaryUrl_Type = DisplayString
_CGgsnExtTraceSecondaryUrl_Object = MibTableColumn
cGgsnExtTraceSecondaryUrl = _CGgsnExtTraceSecondaryUrl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 14, 1, 3),
    _CGgsnExtTraceSecondaryUrl_Type()
)
cGgsnExtTraceSecondaryUrl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnExtTraceSecondaryUrl.setStatus("current")


class _CGgsnExtTraceInfoTxFailRetry_Type(Unsigned32):
    """Custom type cGgsnExtTraceInfoTxFailRetry based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_CGgsnExtTraceInfoTxFailRetry_Type.__name__ = "Unsigned32"
_CGgsnExtTraceInfoTxFailRetry_Object = MibTableColumn
cGgsnExtTraceInfoTxFailRetry = _CGgsnExtTraceInfoTxFailRetry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 14, 1, 4),
    _CGgsnExtTraceInfoTxFailRetry_Type()
)
cGgsnExtTraceInfoTxFailRetry.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnExtTraceInfoTxFailRetry.setStatus("current")


class _CGgsnExtTraceInfoTxFailRetryInterval_Type(Unsigned32):
    """Custom type cGgsnExtTraceInfoTxFailRetryInterval based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 180),
    )


_CGgsnExtTraceInfoTxFailRetryInterval_Type.__name__ = "Unsigned32"
_CGgsnExtTraceInfoTxFailRetryInterval_Object = MibTableColumn
cGgsnExtTraceInfoTxFailRetryInterval = _CGgsnExtTraceInfoTxFailRetryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 14, 1, 5),
    _CGgsnExtTraceInfoTxFailRetryInterval_Type()
)
cGgsnExtTraceInfoTxFailRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnExtTraceInfoTxFailRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtTraceInfoTxFailRetryInterval.setUnits("seconds")
_CGgsnExtTraceRowStatus_Type = RowStatus
_CGgsnExtTraceRowStatus_Object = MibTableColumn
cGgsnExtTraceRowStatus = _CGgsnExtTraceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 2, 14, 1, 6),
    _CGgsnExtTraceRowStatus_Type()
)
cGgsnExtTraceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cGgsnExtTraceRowStatus.setStatus("current")
_CiscoGgsnExtStatus_ObjectIdentity = ObjectIdentity
ciscoGgsnExtStatus = _CiscoGgsnExtStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3)
)
_CGgsnExtGtpPppRegenCreatedIntfs_Type = Gauge32
_CGgsnExtGtpPppRegenCreatedIntfs_Object = MibScalar
cGgsnExtGtpPppRegenCreatedIntfs = _CGgsnExtGtpPppRegenCreatedIntfs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 1),
    _CGgsnExtGtpPppRegenCreatedIntfs_Type()
)
cGgsnExtGtpPppRegenCreatedIntfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtGtpPppRegenCreatedIntfs.setStatus("current")
_CGgsnExtGtpDtActivePDPs_Type = Gauge32
_CGgsnExtGtpDtActivePDPs_Object = MibScalar
cGgsnExtGtpDtActivePDPs = _CGgsnExtGtpDtActivePDPs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 2),
    _CGgsnExtGtpDtActivePDPs_Type()
)
cGgsnExtGtpDtActivePDPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtGtpDtActivePDPs.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtGtpDtActivePDPs.setUnits("PDP Context")
_CGgsnExtActivatedMs_Type = Gauge32
_CGgsnExtActivatedMs_Object = MibScalar
cGgsnExtActivatedMs = _CGgsnExtActivatedMs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 3),
    _CGgsnExtActivatedMs_Type()
)
cGgsnExtActivatedMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtActivatedMs.setStatus("current")
_CGgsnExtActivatedv4v6Gtpv0Pdp_Type = Gauge32
_CGgsnExtActivatedv4v6Gtpv0Pdp_Object = MibScalar
cGgsnExtActivatedv4v6Gtpv0Pdp = _CGgsnExtActivatedv4v6Gtpv0Pdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 4),
    _CGgsnExtActivatedv4v6Gtpv0Pdp_Type()
)
cGgsnExtActivatedv4v6Gtpv0Pdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtActivatedv4v6Gtpv0Pdp.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtActivatedv4v6Gtpv0Pdp.setUnits("PDP Context")
_CGgsnExtActivatedv4v6Gtpv1Pdp_Type = Gauge32
_CGgsnExtActivatedv4v6Gtpv1Pdp_Object = MibScalar
cGgsnExtActivatedv4v6Gtpv1Pdp = _CGgsnExtActivatedv4v6Gtpv1Pdp_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 5),
    _CGgsnExtActivatedv4v6Gtpv1Pdp_Type()
)
cGgsnExtActivatedv4v6Gtpv1Pdp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtActivatedv4v6Gtpv1Pdp.setStatus("current")
if mibBuilder.loadTexts:
    cGgsnExtActivatedv4v6Gtpv1Pdp.setUnits("PDP Context")
_CGgsnExtActivatedv4v6MobileStations_Type = Gauge32
_CGgsnExtActivatedv4v6MobileStations_Object = MibScalar
cGgsnExtActivatedv4v6MobileStations = _CGgsnExtActivatedv4v6MobileStations_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 6),
    _CGgsnExtActivatedv4v6MobileStations_Type()
)
cGgsnExtActivatedv4v6MobileStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtActivatedv4v6MobileStations.setStatus("current")
_CiscoGgsnExtTraceStatusTable_Object = MibTable
ciscoGgsnExtTraceStatusTable = _CiscoGgsnExtTraceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 7)
)
if mibBuilder.loadTexts:
    ciscoGgsnExtTraceStatusTable.setStatus("current")
_CiscoGgsnExtTraceStatusEntry_Object = MibTableRow
ciscoGgsnExtTraceStatusEntry = _CiscoGgsnExtTraceStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 7, 1)
)
ciscoGgsnExtTraceStatusEntry.setIndexNames(
    (0, "CISCO-GGSN-EXT-MIB", "cGgsnExtTraceStatusImsi"),
)
if mibBuilder.loadTexts:
    ciscoGgsnExtTraceStatusEntry.setStatus("current")


class _CGgsnExtTraceStatusImsi_Type(SnmpAdminString):
    """Custom type cGgsnExtTraceStatusImsi based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CGgsnExtTraceStatusImsi_Type.__name__ = "SnmpAdminString"
_CGgsnExtTraceStatusImsi_Object = MibTableColumn
cGgsnExtTraceStatusImsi = _CGgsnExtTraceStatusImsi_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 7, 1, 1),
    _CGgsnExtTraceStatusImsi_Type()
)
cGgsnExtTraceStatusImsi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cGgsnExtTraceStatusImsi.setStatus("current")


class _CGgsnExtTraceStatusImei_Type(SnmpAdminString):
    """Custom type cGgsnExtTraceStatusImei based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_CGgsnExtTraceStatusImei_Type.__name__ = "SnmpAdminString"
_CGgsnExtTraceStatusImei_Object = MibTableColumn
cGgsnExtTraceStatusImei = _CGgsnExtTraceStatusImei_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 7, 1, 2),
    _CGgsnExtTraceStatusImei_Type()
)
cGgsnExtTraceStatusImei.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceStatusImei.setStatus("current")


class _CGgsnExtTraceStatusSource_Type(Integer32):
    """Custom type cGgsnExtTraceStatusSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("management", 2),
          ("signaling", 1))
    )


_CGgsnExtTraceStatusSource_Type.__name__ = "Integer32"
_CGgsnExtTraceStatusSource_Object = MibTableColumn
cGgsnExtTraceStatusSource = _CGgsnExtTraceStatusSource_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 7, 1, 3),
    _CGgsnExtTraceStatusSource_Type()
)
cGgsnExtTraceStatusSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceStatusSource.setStatus("current")


class _CGgsnExtTraceStatusReference_Type(SnmpAdminString):
    """Custom type cGgsnExtTraceStatusReference based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_CGgsnExtTraceStatusReference_Type.__name__ = "SnmpAdminString"
_CGgsnExtTraceStatusReference_Object = MibTableColumn
cGgsnExtTraceStatusReference = _CGgsnExtTraceStatusReference_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 3, 7, 1, 4),
    _CGgsnExtTraceStatusReference_Type()
)
cGgsnExtTraceStatusReference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cGgsnExtTraceStatusReference.setStatus("current")
_CiscoGgsnExtNotifMgmt_ObjectIdentity = ObjectIdentity
ciscoGgsnExtNotifMgmt = _CiscoGgsnExtNotifMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 4)
)


class _CGgsnExtTraceNotifEnable_Type(TruthValue):
    """Custom type cGgsnExtTraceNotifEnable based on TruthValue"""


_CGgsnExtTraceNotifEnable_Object = MibScalar
cGgsnExtTraceNotifEnable = _CGgsnExtTraceNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 4, 1),
    _CGgsnExtTraceNotifEnable_Type()
)
cGgsnExtTraceNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cGgsnExtTraceNotifEnable.setStatus("current")
_CiscoGgsnExtNotifInfo_ObjectIdentity = ObjectIdentity
ciscoGgsnExtNotifInfo = _CiscoGgsnExtNotifInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 5)
)
_CGgsnExtSubscriberMcc_Type = Unsigned32
_CGgsnExtSubscriberMcc_Object = MibScalar
cGgsnExtSubscriberMcc = _CGgsnExtSubscriberMcc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 5, 1),
    _CGgsnExtSubscriberMcc_Type()
)
cGgsnExtSubscriberMcc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberMcc.setStatus("current")
_CGgsnExtSubscriberMnc_Type = Unsigned32
_CGgsnExtSubscriberMnc_Object = MibScalar
cGgsnExtSubscriberMnc = _CGgsnExtSubscriberMnc_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 5, 2),
    _CGgsnExtSubscriberMnc_Type()
)
cGgsnExtSubscriberMnc.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberMnc.setStatus("current")
_CGgsnExtSubscriberTraceId_Type = Unsigned32
_CGgsnExtSubscriberTraceId_Object = MibScalar
cGgsnExtSubscriberTraceId = _CGgsnExtSubscriberTraceId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 5, 3),
    _CGgsnExtSubscriberTraceId_Type()
)
cGgsnExtSubscriberTraceId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnExtSubscriberTraceId.setStatus("current")
_CGgsnExtSubscrTraceFailReason_Type = DisplayString
_CGgsnExtSubscrTraceFailReason_Object = MibScalar
cGgsnExtSubscrTraceFailReason = _CGgsnExtSubscrTraceFailReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 1, 5, 4),
    _CGgsnExtSubscrTraceFailReason_Type()
)
cGgsnExtSubscrTraceFailReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    cGgsnExtSubscrTraceFailReason.setStatus("current")
_CiscoGgsnExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoGgsnExtMIBConform = _CiscoGgsnExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2)
)
_CGgsnExtMIBCompliances_ObjectIdentity = ObjectIdentity
cGgsnExtMIBCompliances = _CGgsnExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 1)
)
_CGgsnExtMIBGroups_ObjectIdentity = ObjectIdentity
cGgsnExtMIBGroups = _CGgsnExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2)
)

# Managed Objects groups

cGgsnExtStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 1)
)
cGgsnExtStatisticsGroup.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtNoWaitSgsnLocalDelPDPs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtNoReqSgsnLocalDelPDPs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSentPdpUpdateReqs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtRcvdSuccPdpUpdateResponses"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtRcvdCoaMsgs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtDiscardedCoaMsgs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSentCoaUpdateReqs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSentErrorIndications"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtRcvdErrorIndications"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTotalDtEnabled"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtRcvdDtPdpErrorIndications"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTotalDtUpdFailDeletedPDPs"))
)
if mibBuilder.loadTexts:
    cGgsnExtStatisticsGroup.setStatus("current")

cGgsnExtStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 2)
)
cGgsnExtStatusGroup.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtGtpPppRegenCreatedIntfs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtGtpDtActivePDPs"))
)
if mibBuilder.loadTexts:
    cGgsnExtStatusGroup.setStatus("deprecated")

cGgsnExtConfigurationsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 3)
)
cGgsnExtConfigurationsGroup.setObjects(
    ("CISCO-GGSN-EXT-MIB", "cGgsnExtAaaAccountInterPeriod")
)
if mibBuilder.loadTexts:
    cGgsnExtConfigurationsGroup.setStatus("deprecated")

cGgsnExtThruputGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 4)
)
cGgsnExtThruputGroup.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtThruputLastCollected"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtUpstreamByteCount"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtDownstreamByteCount"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtUpstreamPktCount"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtDownstreamPktCount"))
)
if mibBuilder.loadTexts:
    cGgsnExtThruputGroup.setStatus("current")

cGgsnExtStatusGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 5)
)
cGgsnExtStatusGroupRev1.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtGtpPppRegenCreatedIntfs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtGtpDtActivePDPs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtActivatedMs"))
)
if mibBuilder.loadTexts:
    cGgsnExtStatusGroupRev1.setStatus("current")

cGgsnExtConfigurationsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 6)
)
cGgsnExtConfigurationsGroupRev1.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtAaaAccountInterPeriod"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtDfpCpuLoad"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtDfpMemLoad"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtThruputHistory"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtCallRateInterval"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtCallRateHistory"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtPrepaidStandAlone"))
)
if mibBuilder.loadTexts:
    cGgsnExtConfigurationsGroupRev1.setStatus("current")

cGgsnExtStatisticsGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 7)
)
cGgsnExtStatisticsGroupRev1.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtPdpNonExistentMsgs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtCallRateLastCollected"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtCreatedPDPs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtDeletedPDPs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtHistCallRateInterval"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtHistCallRateLastCollected"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtHistCreatedPDPs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtHistDeletedPDPs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtHistThruputLastCollected"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtHistUpstreamByteCount"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtHistDownstreamByteCount"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtHistUpstreamPktCount"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtHistDownstreamPktCount"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberTid"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberMSAddrType"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberMSAddr"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberSource"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberSGSNAddrType"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberSGSNAddr"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberAPN"))
)
if mibBuilder.loadTexts:
    cGgsnExtStatisticsGroupRev1.setStatus("current")

cGgsnExtConfigurationsGroupRev1Sup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 8)
)
cGgsnExtConfigurationsGroupRev1Sup1.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtRedundancyEnabled"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtChargSyncWindowSvcSeqnum"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtChargSyncWindowCdrSeqnum"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtChargSynWindowGtppSeqnum"))
)
if mibBuilder.loadTexts:
    cGgsnExtConfigurationsGroupRev1Sup1.setStatus("current")

cGgsnExtStatisticsGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 9)
)
cGgsnExtStatisticsGroupSup1.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtTotalCreatedv4v6Pdps"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTotalDeletedv4v6Pdps"))
)
if mibBuilder.loadTexts:
    cGgsnExtStatisticsGroupSup1.setStatus("current")

cGgsnExtStatusGroupSup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 10)
)
cGgsnExtStatusGroupSup1.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtActivatedv4v6Gtpv0Pdp"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtActivatedv4v6Gtpv1Pdp"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtActivatedv4v6MobileStations"))
)
if mibBuilder.loadTexts:
    cGgsnExtStatusGroupSup1.setStatus("current")

cGgsnExtStatisticsGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 11)
)
cGgsnExtStatisticsGroupSup2.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceActivatedSessions"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceSignalActivations"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceMgmtActivations"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceNewSesActivations"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceActSesActivations"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceSignalActivFailures"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceMgmtActivFailures"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceDeactivatedSessions"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceSignalDeactivations"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceMgmtDeactivations"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceSignalDeactivFailures"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceMgmtDeactivFailures"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceTotalXmlFiles"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceTotalXmlFailNotifFiles"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceXmlFileTransSucc"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceXmlFileTransPri"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceXmlFileTransSec"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceXmlFileTotalTransFails"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceXmlFileTransPriFails"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceXmlFileTransRetries"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceXmlFileTransSecFails"))
)
if mibBuilder.loadTexts:
    cGgsnExtStatisticsGroupSup2.setStatus("current")

cGgsnExtConfigurationsGroupRev1Sup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 12)
)
cGgsnExtConfigurationsGroupRev1Sup2.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceBufferLimit"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceXmlTransferInterval"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceNotifEnable"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTracePrimaryUrl"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceSecondaryUrl"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceInfoTxFailRetry"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceInfoTxFailRetryInterval"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceRowStatus"))
)
if mibBuilder.loadTexts:
    cGgsnExtConfigurationsGroupRev1Sup2.setStatus("current")

cGgsnExtStatusGroupSup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 13)
)
cGgsnExtStatusGroupSup2.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceStatusImei"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceStatusSource"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtTraceStatusReference"))
)
if mibBuilder.loadTexts:
    cGgsnExtStatusGroupSup2.setStatus("current")

cGgsnExtNotificationInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 15)
)
cGgsnExtNotificationInfoGroup.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberMcc"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberMnc"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberTraceId"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscrTraceFailReason"))
)
if mibBuilder.loadTexts:
    cGgsnExtNotificationInfoGroup.setStatus("current")

cGgsnExtStatisticsGroupSup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 16)
)
cGgsnExtStatisticsGroupSup3.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtConditionalIEMissingMsgs"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtInvalidReplyPeerMsgs"))
)
if mibBuilder.loadTexts:
    cGgsnExtStatisticsGroupSup3.setStatus("current")


# Notification objects

cGgsnExtSubsTraceFailNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 0, 1)
)
cGgsnExtSubsTraceFailNotif.setObjects(
      *(("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberMcc"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberMnc"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscriberTraceId"),
        ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubscrTraceFailReason"))
)
if mibBuilder.loadTexts:
    cGgsnExtSubsTraceFailNotif.setStatus(
        "current"
    )


# Notifications groups

cGgsnExtNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 2, 14)
)
cGgsnExtNotificationsGroup.setObjects(
    ("CISCO-GGSN-EXT-MIB", "cGgsnExtSubsTraceFailNotif")
)
if mibBuilder.loadTexts:
    cGgsnExtNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

cGgsnExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cGgsnExtMIBCompliance.setStatus(
        "deprecated"
    )

cGgsnExtMIBComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 1, 2)
)
if mibBuilder.loadTexts:
    cGgsnExtMIBComplianceRev1.setStatus(
        "deprecated"
    )

cGgsnExtMIBComplianceRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 1, 3)
)
if mibBuilder.loadTexts:
    cGgsnExtMIBComplianceRev2.setStatus(
        "deprecated"
    )

cGgsnExtMIBComplianceRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 1, 4)
)
if mibBuilder.loadTexts:
    cGgsnExtMIBComplianceRev3.setStatus(
        "deprecated"
    )

cGgsnExtMIBComplianceRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 647, 2, 1, 5)
)
if mibBuilder.loadTexts:
    cGgsnExtMIBComplianceRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-GGSN-EXT-MIB",
    **{"ciscoGgsnExtMIB": ciscoGgsnExtMIB,
       "ciscoGgsnExtMIBNotifs": ciscoGgsnExtMIBNotifs,
       "cGgsnExtSubsTraceFailNotif": cGgsnExtSubsTraceFailNotif,
       "ciscoGgsnExtMIBObjects": ciscoGgsnExtMIBObjects,
       "ciscoGgsnExtStatistics": ciscoGgsnExtStatistics,
       "cGgsnExtNoWaitSgsnLocalDelPDPs": cGgsnExtNoWaitSgsnLocalDelPDPs,
       "cGgsnExtNoReqSgsnLocalDelPDPs": cGgsnExtNoReqSgsnLocalDelPDPs,
       "cGgsnExtSentPdpUpdateReqs": cGgsnExtSentPdpUpdateReqs,
       "cGgsnExtRcvdSuccPdpUpdateResponses": cGgsnExtRcvdSuccPdpUpdateResponses,
       "cGgsnExtRcvdCoaMsgs": cGgsnExtRcvdCoaMsgs,
       "cGgsnExtDiscardedCoaMsgs": cGgsnExtDiscardedCoaMsgs,
       "cGgsnExtSentCoaUpdateReqs": cGgsnExtSentCoaUpdateReqs,
       "cGgsnExtSentErrorIndications": cGgsnExtSentErrorIndications,
       "cGgsnExtRcvdErrorIndications": cGgsnExtRcvdErrorIndications,
       "cGgsnExtTotalDtEnabled": cGgsnExtTotalDtEnabled,
       "cGgsnExtRcvdDtPdpErrorIndications": cGgsnExtRcvdDtPdpErrorIndications,
       "cGgsnExtTotalDtUpdFailDeletedPDPs": cGgsnExtTotalDtUpdFailDeletedPDPs,
       "cGgsnExtThruputStatsTable": cGgsnExtThruputStatsTable,
       "cGgsnExtThruputStatsEntry": cGgsnExtThruputStatsEntry,
       "cGgsnExtThruputInterval": cGgsnExtThruputInterval,
       "cGgsnExtThruputLastCollected": cGgsnExtThruputLastCollected,
       "cGgsnExtUpstreamByteCount": cGgsnExtUpstreamByteCount,
       "cGgsnExtDownstreamByteCount": cGgsnExtDownstreamByteCount,
       "cGgsnExtUpstreamPktCount": cGgsnExtUpstreamPktCount,
       "cGgsnExtDownstreamPktCount": cGgsnExtDownstreamPktCount,
       "cGgsnExtPdpNonExistentMsgs": cGgsnExtPdpNonExistentMsgs,
       "cGgsnExtCallRateStatsTable": cGgsnExtCallRateStatsTable,
       "cGgsnExtCallRateStatsEntry": cGgsnExtCallRateStatsEntry,
       "cGgsnExtCallRateStatsInterval": cGgsnExtCallRateStatsInterval,
       "cGgsnExtCallRateLastCollected": cGgsnExtCallRateLastCollected,
       "cGgsnExtCreatedPDPs": cGgsnExtCreatedPDPs,
       "cGgsnExtDeletedPDPs": cGgsnExtDeletedPDPs,
       "cGgsnExtHistCallRateStatsTable": cGgsnExtHistCallRateStatsTable,
       "cGgsnExtHistCallRateStatsEntry": cGgsnExtHistCallRateStatsEntry,
       "cGgsnExtHistCallRateIndex": cGgsnExtHistCallRateIndex,
       "cGgsnExtHistCallRateInterval": cGgsnExtHistCallRateInterval,
       "cGgsnExtHistCallRateLastCollected": cGgsnExtHistCallRateLastCollected,
       "cGgsnExtHistCreatedPDPs": cGgsnExtHistCreatedPDPs,
       "cGgsnExtHistDeletedPDPs": cGgsnExtHistDeletedPDPs,
       "cGgsnExtHistThruputStatsTable": cGgsnExtHistThruputStatsTable,
       "cGgsnExtHistThruputStatsEntry": cGgsnExtHistThruputStatsEntry,
       "cGgsnExtHistThruputIndex": cGgsnExtHistThruputIndex,
       "cGgsnExtHistThruputInterval": cGgsnExtHistThruputInterval,
       "cGgsnExtHistThruputLastCollected": cGgsnExtHistThruputLastCollected,
       "cGgsnExtHistUpstreamByteCount": cGgsnExtHistUpstreamByteCount,
       "cGgsnExtHistDownstreamByteCount": cGgsnExtHistDownstreamByteCount,
       "cGgsnExtHistUpstreamPktCount": cGgsnExtHistUpstreamPktCount,
       "cGgsnExtHistDownstreamPktCount": cGgsnExtHistDownstreamPktCount,
       "cGgsnExtSubscriberTable": cGgsnExtSubscriberTable,
       "cGgsnExtSubscriberEntry": cGgsnExtSubscriberEntry,
       "cGgsnExtSubscriberMsisdn": cGgsnExtSubscriberMsisdn,
       "cGgsnExtSubscriberTid": cGgsnExtSubscriberTid,
       "cGgsnExtSubscriberMSAddrType": cGgsnExtSubscriberMSAddrType,
       "cGgsnExtSubscriberMSAddr": cGgsnExtSubscriberMSAddr,
       "cGgsnExtSubscriberSource": cGgsnExtSubscriberSource,
       "cGgsnExtSubscriberSGSNAddrType": cGgsnExtSubscriberSGSNAddrType,
       "cGgsnExtSubscriberSGSNAddr": cGgsnExtSubscriberSGSNAddr,
       "cGgsnExtSubscriberAPN": cGgsnExtSubscriberAPN,
       "cGgsnExtTotalCreatedv4v6Pdps": cGgsnExtTotalCreatedv4v6Pdps,
       "cGgsnExtTotalDeletedv4v6Pdps": cGgsnExtTotalDeletedv4v6Pdps,
       "ciscoGgsnExtTraceStatistics": ciscoGgsnExtTraceStatistics,
       "cGgsnExtTraceActivatedSessions": cGgsnExtTraceActivatedSessions,
       "cGgsnExtTraceSignalActivations": cGgsnExtTraceSignalActivations,
       "cGgsnExtTraceMgmtActivations": cGgsnExtTraceMgmtActivations,
       "cGgsnExtTraceNewSesActivations": cGgsnExtTraceNewSesActivations,
       "cGgsnExtTraceActSesActivations": cGgsnExtTraceActSesActivations,
       "cGgsnExtTraceSignalActivFailures": cGgsnExtTraceSignalActivFailures,
       "cGgsnExtTraceMgmtActivFailures": cGgsnExtTraceMgmtActivFailures,
       "cGgsnExtTraceDeactivatedSessions": cGgsnExtTraceDeactivatedSessions,
       "cGgsnExtTraceSignalDeactivations": cGgsnExtTraceSignalDeactivations,
       "cGgsnExtTraceMgmtDeactivations": cGgsnExtTraceMgmtDeactivations,
       "cGgsnExtTraceSignalDeactivFailures": cGgsnExtTraceSignalDeactivFailures,
       "cGgsnExtTraceMgmtDeactivFailures": cGgsnExtTraceMgmtDeactivFailures,
       "ciscoGgsnExtTraceXmlStatistics": ciscoGgsnExtTraceXmlStatistics,
       "cGgsnExtTraceTotalXmlFiles": cGgsnExtTraceTotalXmlFiles,
       "cGgsnExtTraceTotalXmlFailNotifFiles": cGgsnExtTraceTotalXmlFailNotifFiles,
       "cGgsnExtTraceXmlFileTransSucc": cGgsnExtTraceXmlFileTransSucc,
       "cGgsnExtTraceXmlFileTransPri": cGgsnExtTraceXmlFileTransPri,
       "cGgsnExtTraceXmlFileTransSec": cGgsnExtTraceXmlFileTransSec,
       "cGgsnExtTraceXmlFileTotalTransFails": cGgsnExtTraceXmlFileTotalTransFails,
       "cGgsnExtTraceXmlFileTransPriFails": cGgsnExtTraceXmlFileTransPriFails,
       "cGgsnExtTraceXmlFileTransRetries": cGgsnExtTraceXmlFileTransRetries,
       "cGgsnExtTraceXmlFileTransSecFails": cGgsnExtTraceXmlFileTransSecFails,
       "cGgsnExtConditionalIEMissingMsgs": cGgsnExtConditionalIEMissingMsgs,
       "cGgsnExtInvalidReplyPeerMsgs": cGgsnExtInvalidReplyPeerMsgs,
       "ciscoGgsnExtConfigurations": ciscoGgsnExtConfigurations,
       "cGgsnExtAaaAccountInterPeriod": cGgsnExtAaaAccountInterPeriod,
       "cGgsnExtDfpCpuLoad": cGgsnExtDfpCpuLoad,
       "cGgsnExtDfpMemLoad": cGgsnExtDfpMemLoad,
       "cGgsnExtThruputHistory": cGgsnExtThruputHistory,
       "cGgsnExtCallRateInterval": cGgsnExtCallRateInterval,
       "cGgsnExtCallRateHistory": cGgsnExtCallRateHistory,
       "cGgsnExtPrepaidStandAlone": cGgsnExtPrepaidStandAlone,
       "cGgsnExtRedundancyEnabled": cGgsnExtRedundancyEnabled,
       "cGgsnExtChargSyncWindowSvcSeqnum": cGgsnExtChargSyncWindowSvcSeqnum,
       "cGgsnExtChargSyncWindowCdrSeqnum": cGgsnExtChargSyncWindowCdrSeqnum,
       "cGgsnExtChargSynWindowGtppSeqnum": cGgsnExtChargSynWindowGtppSeqnum,
       "cGgsnExtTraceBufferLimit": cGgsnExtTraceBufferLimit,
       "cGgsnExtTraceXmlTransferInterval": cGgsnExtTraceXmlTransferInterval,
       "cGgsnExtSubscriberTraceProfileTable": cGgsnExtSubscriberTraceProfileTable,
       "cGgsnExtSubscriberTraceProfileEntry": cGgsnExtSubscriberTraceProfileEntry,
       "cGgsnExtTraceProfile": cGgsnExtTraceProfile,
       "cGgsnExtTracePrimaryUrl": cGgsnExtTracePrimaryUrl,
       "cGgsnExtTraceSecondaryUrl": cGgsnExtTraceSecondaryUrl,
       "cGgsnExtTraceInfoTxFailRetry": cGgsnExtTraceInfoTxFailRetry,
       "cGgsnExtTraceInfoTxFailRetryInterval": cGgsnExtTraceInfoTxFailRetryInterval,
       "cGgsnExtTraceRowStatus": cGgsnExtTraceRowStatus,
       "ciscoGgsnExtStatus": ciscoGgsnExtStatus,
       "cGgsnExtGtpPppRegenCreatedIntfs": cGgsnExtGtpPppRegenCreatedIntfs,
       "cGgsnExtGtpDtActivePDPs": cGgsnExtGtpDtActivePDPs,
       "cGgsnExtActivatedMs": cGgsnExtActivatedMs,
       "cGgsnExtActivatedv4v6Gtpv0Pdp": cGgsnExtActivatedv4v6Gtpv0Pdp,
       "cGgsnExtActivatedv4v6Gtpv1Pdp": cGgsnExtActivatedv4v6Gtpv1Pdp,
       "cGgsnExtActivatedv4v6MobileStations": cGgsnExtActivatedv4v6MobileStations,
       "ciscoGgsnExtTraceStatusTable": ciscoGgsnExtTraceStatusTable,
       "ciscoGgsnExtTraceStatusEntry": ciscoGgsnExtTraceStatusEntry,
       "cGgsnExtTraceStatusImsi": cGgsnExtTraceStatusImsi,
       "cGgsnExtTraceStatusImei": cGgsnExtTraceStatusImei,
       "cGgsnExtTraceStatusSource": cGgsnExtTraceStatusSource,
       "cGgsnExtTraceStatusReference": cGgsnExtTraceStatusReference,
       "ciscoGgsnExtNotifMgmt": ciscoGgsnExtNotifMgmt,
       "cGgsnExtTraceNotifEnable": cGgsnExtTraceNotifEnable,
       "ciscoGgsnExtNotifInfo": ciscoGgsnExtNotifInfo,
       "cGgsnExtSubscriberMcc": cGgsnExtSubscriberMcc,
       "cGgsnExtSubscriberMnc": cGgsnExtSubscriberMnc,
       "cGgsnExtSubscriberTraceId": cGgsnExtSubscriberTraceId,
       "cGgsnExtSubscrTraceFailReason": cGgsnExtSubscrTraceFailReason,
       "ciscoGgsnExtMIBConform": ciscoGgsnExtMIBConform,
       "cGgsnExtMIBCompliances": cGgsnExtMIBCompliances,
       "cGgsnExtMIBCompliance": cGgsnExtMIBCompliance,
       "cGgsnExtMIBComplianceRev1": cGgsnExtMIBComplianceRev1,
       "cGgsnExtMIBComplianceRev2": cGgsnExtMIBComplianceRev2,
       "cGgsnExtMIBComplianceRev3": cGgsnExtMIBComplianceRev3,
       "cGgsnExtMIBComplianceRev4": cGgsnExtMIBComplianceRev4,
       "cGgsnExtMIBGroups": cGgsnExtMIBGroups,
       "cGgsnExtStatisticsGroup": cGgsnExtStatisticsGroup,
       "cGgsnExtStatusGroup": cGgsnExtStatusGroup,
       "cGgsnExtConfigurationsGroup": cGgsnExtConfigurationsGroup,
       "cGgsnExtThruputGroup": cGgsnExtThruputGroup,
       "cGgsnExtStatusGroupRev1": cGgsnExtStatusGroupRev1,
       "cGgsnExtConfigurationsGroupRev1": cGgsnExtConfigurationsGroupRev1,
       "cGgsnExtStatisticsGroupRev1": cGgsnExtStatisticsGroupRev1,
       "cGgsnExtConfigurationsGroupRev1Sup1": cGgsnExtConfigurationsGroupRev1Sup1,
       "cGgsnExtStatisticsGroupSup1": cGgsnExtStatisticsGroupSup1,
       "cGgsnExtStatusGroupSup1": cGgsnExtStatusGroupSup1,
       "cGgsnExtStatisticsGroupSup2": cGgsnExtStatisticsGroupSup2,
       "cGgsnExtConfigurationsGroupRev1Sup2": cGgsnExtConfigurationsGroupRev1Sup2,
       "cGgsnExtStatusGroupSup2": cGgsnExtStatusGroupSup2,
       "cGgsnExtNotificationsGroup": cGgsnExtNotificationsGroup,
       "cGgsnExtNotificationInfoGroup": cGgsnExtNotificationInfoGroup,
       "cGgsnExtStatisticsGroupSup3": cGgsnExtStatisticsGroupSup3}
)
