# SNMP MIB module (BRCD-FCIP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/BRCD-FCIP-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:48:36 2024
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

(bcsi,) = mibBuilder.importSymbols(
    "Brocade-REG-MIB",
    "bcsi")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 mib_2) = mibBuilder.importSymbols(
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
    "mib-2")

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

fcipExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1588, 4)
)
fcipExtMIB.setRevisions(
        ("2009-06-19 15:05",
         "2013-04-26 11:33")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BrcdCompressionRatio(Unsigned32, TextualConvention):
    status = "current"
    displayHint = "d"


# MIB Managed Objects in the order of their OIDs

_FcipExtendedLinkTable_Object = MibTable
fcipExtendedLinkTable = _FcipExtendedLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1)
)
if mibBuilder.loadTexts:
    fcipExtendedLinkTable.setStatus("current")
_FcipExtendedLinkEntry_Object = MibTableRow
fcipExtendedLinkEntry = _FcipExtendedLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1)
)
fcipExtendedLinkEntry.setIndexNames(
    (0, "BRCD-FCIP-EXT-MIB", "fcipExtendedLinkIfIndex"),
)
if mibBuilder.loadTexts:
    fcipExtendedLinkEntry.setStatus("current")
_FcipExtendedLinkIfIndex_Type = InterfaceIndex
_FcipExtendedLinkIfIndex_Object = MibTableColumn
fcipExtendedLinkIfIndex = _FcipExtendedLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 1),
    _FcipExtendedLinkIfIndex_Type()
)
fcipExtendedLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkIfIndex.setStatus("current")
_FcipExtendedLinkTcpRetransmits_Type = Counter64
_FcipExtendedLinkTcpRetransmits_Object = MibTableColumn
fcipExtendedLinkTcpRetransmits = _FcipExtendedLinkTcpRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 2),
    _FcipExtendedLinkTcpRetransmits_Type()
)
fcipExtendedLinkTcpRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkTcpRetransmits.setStatus("current")
_FcipExtendedLinkTcpDroppedPackets_Type = Counter64
_FcipExtendedLinkTcpDroppedPackets_Object = MibTableColumn
fcipExtendedLinkTcpDroppedPackets = _FcipExtendedLinkTcpDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 3),
    _FcipExtendedLinkTcpDroppedPackets_Type()
)
fcipExtendedLinkTcpDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkTcpDroppedPackets.setStatus("current")
_FcipExtendedLinkCompressionRatio_Type = BrcdCompressionRatio
_FcipExtendedLinkCompressionRatio_Object = MibTableColumn
fcipExtendedLinkCompressionRatio = _FcipExtendedLinkCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 4),
    _FcipExtendedLinkCompressionRatio_Type()
)
fcipExtendedLinkCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkCompressionRatio.setStatus("current")
if mibBuilder.loadTexts:
    fcipExtendedLinkCompressionRatio.setUnits("compression ratio")
_FcipExtendedLinkTcpSmoothedRTT_Type = Integer32
_FcipExtendedLinkTcpSmoothedRTT_Object = MibTableColumn
fcipExtendedLinkTcpSmoothedRTT = _FcipExtendedLinkTcpSmoothedRTT_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 5),
    _FcipExtendedLinkTcpSmoothedRTT_Type()
)
fcipExtendedLinkTcpSmoothedRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkTcpSmoothedRTT.setStatus("current")
if mibBuilder.loadTexts:
    fcipExtendedLinkTcpSmoothedRTT.setUnits("milliseconds")
_FcipExtendedLinkRawBytes_Type = Counter64
_FcipExtendedLinkRawBytes_Object = MibTableColumn
fcipExtendedLinkRawBytes = _FcipExtendedLinkRawBytes_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 6),
    _FcipExtendedLinkRawBytes_Type()
)
fcipExtendedLinkRawBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkRawBytes.setStatus("current")
_FcipExtendedLinkCompressedBytes_Type = Counter64
_FcipExtendedLinkCompressedBytes_Object = MibTableColumn
fcipExtendedLinkCompressedBytes = _FcipExtendedLinkCompressedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 7),
    _FcipExtendedLinkCompressedBytes_Type()
)
fcipExtendedLinkCompressedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkCompressedBytes.setStatus("current")
_FcipExtendedLinkConnectedCount_Type = Counter64
_FcipExtendedLinkConnectedCount_Object = MibTableColumn
fcipExtendedLinkConnectedCount = _FcipExtendedLinkConnectedCount_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 8),
    _FcipExtendedLinkConnectedCount_Type()
)
fcipExtendedLinkConnectedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkConnectedCount.setStatus("current")
_FcipExtendedLinkRtxRtxTO_Type = Counter64
_FcipExtendedLinkRtxRtxTO_Object = MibTableColumn
fcipExtendedLinkRtxRtxTO = _FcipExtendedLinkRtxRtxTO_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 9),
    _FcipExtendedLinkRtxRtxTO_Type()
)
fcipExtendedLinkRtxRtxTO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkRtxRtxTO.setStatus("current")
_FcipExtendedLinkRtxDupAck_Type = Counter64
_FcipExtendedLinkRtxDupAck_Object = MibTableColumn
fcipExtendedLinkRtxDupAck = _FcipExtendedLinkRtxDupAck_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 10),
    _FcipExtendedLinkRtxDupAck_Type()
)
fcipExtendedLinkRtxDupAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkRtxDupAck.setStatus("current")
_FcipExtendedLinkDupAck_Type = Counter64
_FcipExtendedLinkDupAck_Object = MibTableColumn
fcipExtendedLinkDupAck = _FcipExtendedLinkDupAck_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 11),
    _FcipExtendedLinkDupAck_Type()
)
fcipExtendedLinkDupAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkDupAck.setStatus("current")
_FcipExtendedLinkRtt_Type = Integer32
_FcipExtendedLinkRtt_Object = MibTableColumn
fcipExtendedLinkRtt = _FcipExtendedLinkRtt_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 12),
    _FcipExtendedLinkRtt_Type()
)
fcipExtendedLinkRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkRtt.setStatus("current")
if mibBuilder.loadTexts:
    fcipExtendedLinkRtt.setUnits("milliseconds")
_FcipExtendedLinkOoo_Type = Counter64
_FcipExtendedLinkOoo_Object = MibTableColumn
fcipExtendedLinkOoo = _FcipExtendedLinkOoo_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 13),
    _FcipExtendedLinkOoo_Type()
)
fcipExtendedLinkOoo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkOoo.setStatus("current")
_FcipExtendedLinkSlowStarts_Type = Counter64
_FcipExtendedLinkSlowStarts_Object = MibTableColumn
fcipExtendedLinkSlowStarts = _FcipExtendedLinkSlowStarts_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 1, 1, 14),
    _FcipExtendedLinkSlowStarts_Type()
)
fcipExtendedLinkSlowStarts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fcipExtendedLinkSlowStarts.setStatus("current")
_FcipConnStatsTable_Object = MibTable
fcipConnStatsTable = _FcipConnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2)
)
if mibBuilder.loadTexts:
    fcipConnStatsTable.setStatus("current")
_FcipConnStatsEntry_Object = MibTableRow
fcipConnStatsEntry = _FcipConnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2, 1)
)
fcipConnStatsEntry.setIndexNames(
    (0, "BRCD-FCIP-EXT-MIB", "xfcipEntityId"),
    (0, "BRCD-FCIP-EXT-MIB", "xfcipLinkIndex"),
)
if mibBuilder.loadTexts:
    fcipConnStatsEntry.setStatus("current")


class _XfcipEntityId_Type(OctetString):
    """Custom type xfcipEntityId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_XfcipEntityId_Type.__name__ = "OctetString"
_XfcipEntityId_Object = MibTableColumn
xfcipEntityId = _XfcipEntityId_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2, 1, 1),
    _XfcipEntityId_Type()
)
xfcipEntityId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xfcipEntityId.setStatus("current")
_XfcipLinkIfIndex_Type = InterfaceIndex
_XfcipLinkIfIndex_Object = MibTableColumn
xfcipLinkIfIndex = _XfcipLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2, 1, 2),
    _XfcipLinkIfIndex_Type()
)
xfcipLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfcipLinkIfIndex.setStatus("current")


class _XfcipLinkIndex_Type(Unsigned32):
    """Custom type xfcipLinkIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_XfcipLinkIndex_Type.__name__ = "Unsigned32"
_XfcipLinkIndex_Object = MibTableColumn
xfcipLinkIndex = _XfcipLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2, 1, 3),
    _XfcipLinkIndex_Type()
)
xfcipLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xfcipLinkIndex.setStatus("current")
_XfcipExtendedLinkTcpRetransmits_Type = Counter64
_XfcipExtendedLinkTcpRetransmits_Object = MibTableColumn
xfcipExtendedLinkTcpRetransmits = _XfcipExtendedLinkTcpRetransmits_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2, 1, 4),
    _XfcipExtendedLinkTcpRetransmits_Type()
)
xfcipExtendedLinkTcpRetransmits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfcipExtendedLinkTcpRetransmits.setStatus("current")
_XfcipExtendedLinkTcpDroppedPackets_Type = Counter64
_XfcipExtendedLinkTcpDroppedPackets_Object = MibTableColumn
xfcipExtendedLinkTcpDroppedPackets = _XfcipExtendedLinkTcpDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2, 1, 5),
    _XfcipExtendedLinkTcpDroppedPackets_Type()
)
xfcipExtendedLinkTcpDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfcipExtendedLinkTcpDroppedPackets.setStatus("current")
_XfcipExtendedLinkCompressionRatio_Type = BrcdCompressionRatio
_XfcipExtendedLinkCompressionRatio_Object = MibTableColumn
xfcipExtendedLinkCompressionRatio = _XfcipExtendedLinkCompressionRatio_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2, 1, 6),
    _XfcipExtendedLinkCompressionRatio_Type()
)
xfcipExtendedLinkCompressionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfcipExtendedLinkCompressionRatio.setStatus("current")
if mibBuilder.loadTexts:
    xfcipExtendedLinkCompressionRatio.setUnits("compression ratio")
_XfcipExtendedLinkTcpSmoothedRTT_Type = Integer32
_XfcipExtendedLinkTcpSmoothedRTT_Object = MibTableColumn
xfcipExtendedLinkTcpSmoothedRTT = _XfcipExtendedLinkTcpSmoothedRTT_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2, 1, 7),
    _XfcipExtendedLinkTcpSmoothedRTT_Type()
)
xfcipExtendedLinkTcpSmoothedRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfcipExtendedLinkTcpSmoothedRTT.setStatus("current")
if mibBuilder.loadTexts:
    xfcipExtendedLinkTcpSmoothedRTT.setUnits("milliseconds")
_XfcipExtendedLinkRawBytes_Type = Counter64
_XfcipExtendedLinkRawBytes_Object = MibTableColumn
xfcipExtendedLinkRawBytes = _XfcipExtendedLinkRawBytes_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2, 1, 8),
    _XfcipExtendedLinkRawBytes_Type()
)
xfcipExtendedLinkRawBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfcipExtendedLinkRawBytes.setStatus("current")
_XfcipExtendedLinkCompressedBytes_Type = Counter64
_XfcipExtendedLinkCompressedBytes_Object = MibTableColumn
xfcipExtendedLinkCompressedBytes = _XfcipExtendedLinkCompressedBytes_Object(
    (1, 3, 6, 1, 4, 1, 1588, 4, 2, 1, 9),
    _XfcipExtendedLinkCompressedBytes_Type()
)
xfcipExtendedLinkCompressedBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfcipExtendedLinkCompressedBytes.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCD-FCIP-EXT-MIB",
    **{"BrcdCompressionRatio": BrcdCompressionRatio,
       "fcipExtMIB": fcipExtMIB,
       "fcipExtendedLinkTable": fcipExtendedLinkTable,
       "fcipExtendedLinkEntry": fcipExtendedLinkEntry,
       "fcipExtendedLinkIfIndex": fcipExtendedLinkIfIndex,
       "fcipExtendedLinkTcpRetransmits": fcipExtendedLinkTcpRetransmits,
       "fcipExtendedLinkTcpDroppedPackets": fcipExtendedLinkTcpDroppedPackets,
       "fcipExtendedLinkCompressionRatio": fcipExtendedLinkCompressionRatio,
       "fcipExtendedLinkTcpSmoothedRTT": fcipExtendedLinkTcpSmoothedRTT,
       "fcipExtendedLinkRawBytes": fcipExtendedLinkRawBytes,
       "fcipExtendedLinkCompressedBytes": fcipExtendedLinkCompressedBytes,
       "fcipExtendedLinkConnectedCount": fcipExtendedLinkConnectedCount,
       "fcipExtendedLinkRtxRtxTO": fcipExtendedLinkRtxRtxTO,
       "fcipExtendedLinkRtxDupAck": fcipExtendedLinkRtxDupAck,
       "fcipExtendedLinkDupAck": fcipExtendedLinkDupAck,
       "fcipExtendedLinkRtt": fcipExtendedLinkRtt,
       "fcipExtendedLinkOoo": fcipExtendedLinkOoo,
       "fcipExtendedLinkSlowStarts": fcipExtendedLinkSlowStarts,
       "fcipConnStatsTable": fcipConnStatsTable,
       "fcipConnStatsEntry": fcipConnStatsEntry,
       "xfcipEntityId": xfcipEntityId,
       "xfcipLinkIfIndex": xfcipLinkIfIndex,
       "xfcipLinkIndex": xfcipLinkIndex,
       "xfcipExtendedLinkTcpRetransmits": xfcipExtendedLinkTcpRetransmits,
       "xfcipExtendedLinkTcpDroppedPackets": xfcipExtendedLinkTcpDroppedPackets,
       "xfcipExtendedLinkCompressionRatio": xfcipExtendedLinkCompressionRatio,
       "xfcipExtendedLinkTcpSmoothedRTT": xfcipExtendedLinkTcpSmoothedRTT,
       "xfcipExtendedLinkRawBytes": xfcipExtendedLinkRawBytes,
       "xfcipExtendedLinkCompressedBytes": xfcipExtendedLinkCompressedBytes}
)
