# SNMP MIB module (RTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:35 2024
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
 TAddress,
 TDomain,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TAddress",
    "TDomain",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")

(Utf8String,) = mibBuilder.importSymbols(
    "SYSAPPL-MIB",
    "Utf8String")


# MODULE-IDENTITY

rtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 87)
)
rtpMIB.setRevisions(
        ("2000-10-02 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RtpMIBObjects_ObjectIdentity = ObjectIdentity
rtpMIBObjects = _RtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 87, 1)
)
_RtpSessionNewIndex_Type = TestAndIncr
_RtpSessionNewIndex_Object = MibScalar
rtpSessionNewIndex = _RtpSessionNewIndex_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 1),
    _RtpSessionNewIndex_Type()
)
rtpSessionNewIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rtpSessionNewIndex.setStatus("current")
_RtpSessionInverseTable_Object = MibTable
rtpSessionInverseTable = _RtpSessionInverseTable_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 2)
)
if mibBuilder.loadTexts:
    rtpSessionInverseTable.setStatus("current")
_RtpSessionInverseEntry_Object = MibTableRow
rtpSessionInverseEntry = _RtpSessionInverseEntry_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 2, 1)
)
rtpSessionInverseEntry.setIndexNames(
    (0, "RTP-MIB", "rtpSessionDomain"),
    (0, "RTP-MIB", "rtpSessionRemAddr"),
    (0, "RTP-MIB", "rtpSessionLocAddr"),
    (0, "RTP-MIB", "rtpSessionIndex"),
)
if mibBuilder.loadTexts:
    rtpSessionInverseEntry.setStatus("current")
_RtpSessionInverseStartTime_Type = TimeStamp
_RtpSessionInverseStartTime_Object = MibTableColumn
rtpSessionInverseStartTime = _RtpSessionInverseStartTime_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 2, 1, 1),
    _RtpSessionInverseStartTime_Type()
)
rtpSessionInverseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSessionInverseStartTime.setStatus("current")
_RtpSessionTable_Object = MibTable
rtpSessionTable = _RtpSessionTable_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3)
)
if mibBuilder.loadTexts:
    rtpSessionTable.setStatus("current")
_RtpSessionEntry_Object = MibTableRow
rtpSessionEntry = _RtpSessionEntry_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1)
)
rtpSessionEntry.setIndexNames(
    (0, "RTP-MIB", "rtpSessionIndex"),
)
if mibBuilder.loadTexts:
    rtpSessionEntry.setStatus("current")


class _RtpSessionIndex_Type(Integer32):
    """Custom type rtpSessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RtpSessionIndex_Type.__name__ = "Integer32"
_RtpSessionIndex_Object = MibTableColumn
rtpSessionIndex = _RtpSessionIndex_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 1),
    _RtpSessionIndex_Type()
)
rtpSessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtpSessionIndex.setStatus("current")
_RtpSessionDomain_Type = TDomain
_RtpSessionDomain_Object = MibTableColumn
rtpSessionDomain = _RtpSessionDomain_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 2),
    _RtpSessionDomain_Type()
)
rtpSessionDomain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtpSessionDomain.setStatus("current")
_RtpSessionRemAddr_Type = TAddress
_RtpSessionRemAddr_Object = MibTableColumn
rtpSessionRemAddr = _RtpSessionRemAddr_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 3),
    _RtpSessionRemAddr_Type()
)
rtpSessionRemAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtpSessionRemAddr.setStatus("current")
_RtpSessionLocAddr_Type = TAddress
_RtpSessionLocAddr_Object = MibTableColumn
rtpSessionLocAddr = _RtpSessionLocAddr_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 4),
    _RtpSessionLocAddr_Type()
)
rtpSessionLocAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSessionLocAddr.setStatus("current")
_RtpSessionIfIndex_Type = InterfaceIndex
_RtpSessionIfIndex_Object = MibTableColumn
rtpSessionIfIndex = _RtpSessionIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 5),
    _RtpSessionIfIndex_Type()
)
rtpSessionIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtpSessionIfIndex.setStatus("current")
_RtpSessionSenderJoins_Type = Counter32
_RtpSessionSenderJoins_Object = MibTableColumn
rtpSessionSenderJoins = _RtpSessionSenderJoins_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 6),
    _RtpSessionSenderJoins_Type()
)
rtpSessionSenderJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSessionSenderJoins.setStatus("current")
_RtpSessionReceiverJoins_Type = Counter32
_RtpSessionReceiverJoins_Object = MibTableColumn
rtpSessionReceiverJoins = _RtpSessionReceiverJoins_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 7),
    _RtpSessionReceiverJoins_Type()
)
rtpSessionReceiverJoins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSessionReceiverJoins.setStatus("current")
_RtpSessionByes_Type = Counter32
_RtpSessionByes_Object = MibTableColumn
rtpSessionByes = _RtpSessionByes_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 8),
    _RtpSessionByes_Type()
)
rtpSessionByes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSessionByes.setStatus("current")
_RtpSessionStartTime_Type = TimeStamp
_RtpSessionStartTime_Object = MibTableColumn
rtpSessionStartTime = _RtpSessionStartTime_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 9),
    _RtpSessionStartTime_Type()
)
rtpSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSessionStartTime.setStatus("current")
_RtpSessionMonitor_Type = TruthValue
_RtpSessionMonitor_Object = MibTableColumn
rtpSessionMonitor = _RtpSessionMonitor_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 10),
    _RtpSessionMonitor_Type()
)
rtpSessionMonitor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSessionMonitor.setStatus("current")
_RtpSessionRowStatus_Type = RowStatus
_RtpSessionRowStatus_Object = MibTableColumn
rtpSessionRowStatus = _RtpSessionRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 3, 1, 11),
    _RtpSessionRowStatus_Type()
)
rtpSessionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rtpSessionRowStatus.setStatus("current")
_RtpSenderInverseTable_Object = MibTable
rtpSenderInverseTable = _RtpSenderInverseTable_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 4)
)
if mibBuilder.loadTexts:
    rtpSenderInverseTable.setStatus("current")
_RtpSenderInverseEntry_Object = MibTableRow
rtpSenderInverseEntry = _RtpSenderInverseEntry_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 4, 1)
)
rtpSenderInverseEntry.setIndexNames(
    (0, "RTP-MIB", "rtpSessionDomain"),
    (0, "RTP-MIB", "rtpSenderAddr"),
    (0, "RTP-MIB", "rtpSessionIndex"),
    (0, "RTP-MIB", "rtpSenderSSRC"),
)
if mibBuilder.loadTexts:
    rtpSenderInverseEntry.setStatus("current")
_RtpSenderInverseStartTime_Type = TimeStamp
_RtpSenderInverseStartTime_Object = MibTableColumn
rtpSenderInverseStartTime = _RtpSenderInverseStartTime_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 4, 1, 1),
    _RtpSenderInverseStartTime_Type()
)
rtpSenderInverseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSenderInverseStartTime.setStatus("current")
_RtpSenderTable_Object = MibTable
rtpSenderTable = _RtpSenderTable_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5)
)
if mibBuilder.loadTexts:
    rtpSenderTable.setStatus("current")
_RtpSenderEntry_Object = MibTableRow
rtpSenderEntry = _RtpSenderEntry_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1)
)
rtpSenderEntry.setIndexNames(
    (0, "RTP-MIB", "rtpSessionIndex"),
    (0, "RTP-MIB", "rtpSenderSSRC"),
)
if mibBuilder.loadTexts:
    rtpSenderEntry.setStatus("current")
_RtpSenderSSRC_Type = Unsigned32
_RtpSenderSSRC_Object = MibTableColumn
rtpSenderSSRC = _RtpSenderSSRC_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 1),
    _RtpSenderSSRC_Type()
)
rtpSenderSSRC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtpSenderSSRC.setStatus("current")
_RtpSenderCNAME_Type = Utf8String
_RtpSenderCNAME_Object = MibTableColumn
rtpSenderCNAME = _RtpSenderCNAME_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 2),
    _RtpSenderCNAME_Type()
)
rtpSenderCNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSenderCNAME.setStatus("current")
_RtpSenderAddr_Type = TAddress
_RtpSenderAddr_Object = MibTableColumn
rtpSenderAddr = _RtpSenderAddr_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 3),
    _RtpSenderAddr_Type()
)
rtpSenderAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSenderAddr.setStatus("current")
_RtpSenderPackets_Type = Counter64
_RtpSenderPackets_Object = MibTableColumn
rtpSenderPackets = _RtpSenderPackets_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 4),
    _RtpSenderPackets_Type()
)
rtpSenderPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSenderPackets.setStatus("current")
_RtpSenderOctets_Type = Counter64
_RtpSenderOctets_Object = MibTableColumn
rtpSenderOctets = _RtpSenderOctets_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 5),
    _RtpSenderOctets_Type()
)
rtpSenderOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSenderOctets.setStatus("current")


class _RtpSenderTool_Type(Utf8String):
    """Custom type rtpSenderTool based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RtpSenderTool_Type.__name__ = "Utf8String"
_RtpSenderTool_Object = MibTableColumn
rtpSenderTool = _RtpSenderTool_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 6),
    _RtpSenderTool_Type()
)
rtpSenderTool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSenderTool.setStatus("current")
_RtpSenderSRs_Type = Counter32
_RtpSenderSRs_Object = MibTableColumn
rtpSenderSRs = _RtpSenderSRs_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 7),
    _RtpSenderSRs_Type()
)
rtpSenderSRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSenderSRs.setStatus("current")
_RtpSenderSRTime_Type = TimeStamp
_RtpSenderSRTime_Object = MibTableColumn
rtpSenderSRTime = _RtpSenderSRTime_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 8),
    _RtpSenderSRTime_Type()
)
rtpSenderSRTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSenderSRTime.setStatus("current")


class _RtpSenderPT_Type(Integer32):
    """Custom type rtpSenderPT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RtpSenderPT_Type.__name__ = "Integer32"
_RtpSenderPT_Object = MibTableColumn
rtpSenderPT = _RtpSenderPT_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 9),
    _RtpSenderPT_Type()
)
rtpSenderPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSenderPT.setStatus("current")
_RtpSenderStartTime_Type = TimeStamp
_RtpSenderStartTime_Object = MibTableColumn
rtpSenderStartTime = _RtpSenderStartTime_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 5, 1, 10),
    _RtpSenderStartTime_Type()
)
rtpSenderStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpSenderStartTime.setStatus("current")
_RtpRcvrInverseTable_Object = MibTable
rtpRcvrInverseTable = _RtpRcvrInverseTable_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 6)
)
if mibBuilder.loadTexts:
    rtpRcvrInverseTable.setStatus("current")
_RtpRcvrInverseEntry_Object = MibTableRow
rtpRcvrInverseEntry = _RtpRcvrInverseEntry_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 6, 1)
)
rtpRcvrInverseEntry.setIndexNames(
    (0, "RTP-MIB", "rtpSessionDomain"),
    (0, "RTP-MIB", "rtpRcvrAddr"),
    (0, "RTP-MIB", "rtpSessionIndex"),
    (0, "RTP-MIB", "rtpRcvrSRCSSRC"),
    (0, "RTP-MIB", "rtpRcvrSSRC"),
)
if mibBuilder.loadTexts:
    rtpRcvrInverseEntry.setStatus("current")
_RtpRcvrInverseStartTime_Type = TimeStamp
_RtpRcvrInverseStartTime_Object = MibTableColumn
rtpRcvrInverseStartTime = _RtpRcvrInverseStartTime_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 6, 1, 1),
    _RtpRcvrInverseStartTime_Type()
)
rtpRcvrInverseStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrInverseStartTime.setStatus("current")
_RtpRcvrTable_Object = MibTable
rtpRcvrTable = _RtpRcvrTable_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7)
)
if mibBuilder.loadTexts:
    rtpRcvrTable.setStatus("current")
_RtpRcvrEntry_Object = MibTableRow
rtpRcvrEntry = _RtpRcvrEntry_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1)
)
rtpRcvrEntry.setIndexNames(
    (0, "RTP-MIB", "rtpSessionIndex"),
    (0, "RTP-MIB", "rtpRcvrSRCSSRC"),
    (0, "RTP-MIB", "rtpRcvrSSRC"),
)
if mibBuilder.loadTexts:
    rtpRcvrEntry.setStatus("current")
_RtpRcvrSRCSSRC_Type = Unsigned32
_RtpRcvrSRCSSRC_Object = MibTableColumn
rtpRcvrSRCSSRC = _RtpRcvrSRCSSRC_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 1),
    _RtpRcvrSRCSSRC_Type()
)
rtpRcvrSRCSSRC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtpRcvrSRCSSRC.setStatus("current")
_RtpRcvrSSRC_Type = Unsigned32
_RtpRcvrSSRC_Object = MibTableColumn
rtpRcvrSSRC = _RtpRcvrSSRC_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 2),
    _RtpRcvrSSRC_Type()
)
rtpRcvrSSRC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rtpRcvrSSRC.setStatus("current")
_RtpRcvrCNAME_Type = Utf8String
_RtpRcvrCNAME_Object = MibTableColumn
rtpRcvrCNAME = _RtpRcvrCNAME_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 3),
    _RtpRcvrCNAME_Type()
)
rtpRcvrCNAME.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrCNAME.setStatus("current")
_RtpRcvrAddr_Type = TAddress
_RtpRcvrAddr_Object = MibTableColumn
rtpRcvrAddr = _RtpRcvrAddr_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 4),
    _RtpRcvrAddr_Type()
)
rtpRcvrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrAddr.setStatus("current")
_RtpRcvrRTT_Type = Gauge32
_RtpRcvrRTT_Object = MibTableColumn
rtpRcvrRTT = _RtpRcvrRTT_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 5),
    _RtpRcvrRTT_Type()
)
rtpRcvrRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrRTT.setStatus("current")
_RtpRcvrLostPackets_Type = Counter64
_RtpRcvrLostPackets_Object = MibTableColumn
rtpRcvrLostPackets = _RtpRcvrLostPackets_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 6),
    _RtpRcvrLostPackets_Type()
)
rtpRcvrLostPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrLostPackets.setStatus("current")
_RtpRcvrJitter_Type = Gauge32
_RtpRcvrJitter_Object = MibTableColumn
rtpRcvrJitter = _RtpRcvrJitter_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 7),
    _RtpRcvrJitter_Type()
)
rtpRcvrJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrJitter.setStatus("current")


class _RtpRcvrTool_Type(Utf8String):
    """Custom type rtpRcvrTool based on Utf8String"""
    subtypeSpec = Utf8String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RtpRcvrTool_Type.__name__ = "Utf8String"
_RtpRcvrTool_Object = MibTableColumn
rtpRcvrTool = _RtpRcvrTool_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 8),
    _RtpRcvrTool_Type()
)
rtpRcvrTool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrTool.setStatus("current")
_RtpRcvrRRs_Type = Counter32
_RtpRcvrRRs_Object = MibTableColumn
rtpRcvrRRs = _RtpRcvrRRs_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 9),
    _RtpRcvrRRs_Type()
)
rtpRcvrRRs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrRRs.setStatus("current")
_RtpRcvrRRTime_Type = TimeStamp
_RtpRcvrRRTime_Object = MibTableColumn
rtpRcvrRRTime = _RtpRcvrRRTime_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 10),
    _RtpRcvrRRTime_Type()
)
rtpRcvrRRTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrRRTime.setStatus("current")


class _RtpRcvrPT_Type(Integer32):
    """Custom type rtpRcvrPT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RtpRcvrPT_Type.__name__ = "Integer32"
_RtpRcvrPT_Object = MibTableColumn
rtpRcvrPT = _RtpRcvrPT_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 11),
    _RtpRcvrPT_Type()
)
rtpRcvrPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrPT.setStatus("current")
_RtpRcvrPackets_Type = Counter64
_RtpRcvrPackets_Object = MibTableColumn
rtpRcvrPackets = _RtpRcvrPackets_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 12),
    _RtpRcvrPackets_Type()
)
rtpRcvrPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrPackets.setStatus("current")
_RtpRcvrOctets_Type = Counter64
_RtpRcvrOctets_Object = MibTableColumn
rtpRcvrOctets = _RtpRcvrOctets_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 13),
    _RtpRcvrOctets_Type()
)
rtpRcvrOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrOctets.setStatus("current")
_RtpRcvrStartTime_Type = TimeStamp
_RtpRcvrStartTime_Object = MibTableColumn
rtpRcvrStartTime = _RtpRcvrStartTime_Object(
    (1, 3, 6, 1, 2, 1, 87, 1, 7, 1, 14),
    _RtpRcvrStartTime_Type()
)
rtpRcvrStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rtpRcvrStartTime.setStatus("current")
_RtpConformance_ObjectIdentity = ObjectIdentity
rtpConformance = _RtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 87, 2)
)
_RtpGroups_ObjectIdentity = ObjectIdentity
rtpGroups = _RtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 87, 2, 1)
)
_RtpCompliances_ObjectIdentity = ObjectIdentity
rtpCompliances = _RtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 87, 2, 2)
)

# Managed Objects groups

rtpSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 87, 2, 1, 1)
)
rtpSystemGroup.setObjects(
      *(("RTP-MIB", "rtpSessionDomain"),
        ("RTP-MIB", "rtpSessionRemAddr"),
        ("RTP-MIB", "rtpSessionIfIndex"),
        ("RTP-MIB", "rtpSessionSenderJoins"),
        ("RTP-MIB", "rtpSessionReceiverJoins"),
        ("RTP-MIB", "rtpSessionStartTime"),
        ("RTP-MIB", "rtpSessionByes"),
        ("RTP-MIB", "rtpSessionMonitor"),
        ("RTP-MIB", "rtpSenderCNAME"),
        ("RTP-MIB", "rtpSenderAddr"),
        ("RTP-MIB", "rtpSenderPackets"),
        ("RTP-MIB", "rtpSenderOctets"),
        ("RTP-MIB", "rtpSenderTool"),
        ("RTP-MIB", "rtpSenderSRs"),
        ("RTP-MIB", "rtpSenderSRTime"),
        ("RTP-MIB", "rtpSenderStartTime"),
        ("RTP-MIB", "rtpRcvrCNAME"),
        ("RTP-MIB", "rtpRcvrAddr"),
        ("RTP-MIB", "rtpRcvrLostPackets"),
        ("RTP-MIB", "rtpRcvrJitter"),
        ("RTP-MIB", "rtpRcvrTool"),
        ("RTP-MIB", "rtpRcvrRRs"),
        ("RTP-MIB", "rtpRcvrRRTime"),
        ("RTP-MIB", "rtpRcvrStartTime"))
)
if mibBuilder.loadTexts:
    rtpSystemGroup.setStatus("current")

rtpHostGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 87, 2, 1, 2)
)
rtpHostGroup.setObjects(
      *(("RTP-MIB", "rtpSessionLocAddr"),
        ("RTP-MIB", "rtpSenderPT"),
        ("RTP-MIB", "rtpRcvrPT"),
        ("RTP-MIB", "rtpRcvrRTT"),
        ("RTP-MIB", "rtpRcvrOctets"),
        ("RTP-MIB", "rtpRcvrPackets"))
)
if mibBuilder.loadTexts:
    rtpHostGroup.setStatus("current")

rtpMonitorGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 87, 2, 1, 3)
)
rtpMonitorGroup.setObjects(
      *(("RTP-MIB", "rtpSessionNewIndex"),
        ("RTP-MIB", "rtpSessionRowStatus"))
)
if mibBuilder.loadTexts:
    rtpMonitorGroup.setStatus("current")

rtpInverseGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 87, 2, 1, 4)
)
rtpInverseGroup.setObjects(
      *(("RTP-MIB", "rtpSessionInverseStartTime"),
        ("RTP-MIB", "rtpSenderInverseStartTime"),
        ("RTP-MIB", "rtpRcvrInverseStartTime"))
)
if mibBuilder.loadTexts:
    rtpInverseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rtpHostCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 87, 2, 2, 1)
)
if mibBuilder.loadTexts:
    rtpHostCompliance.setStatus(
        "current"
    )

rtpMonitorCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 87, 2, 2, 2)
)
if mibBuilder.loadTexts:
    rtpMonitorCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RTP-MIB",
    **{"rtpMIB": rtpMIB,
       "rtpMIBObjects": rtpMIBObjects,
       "rtpSessionNewIndex": rtpSessionNewIndex,
       "rtpSessionInverseTable": rtpSessionInverseTable,
       "rtpSessionInverseEntry": rtpSessionInverseEntry,
       "rtpSessionInverseStartTime": rtpSessionInverseStartTime,
       "rtpSessionTable": rtpSessionTable,
       "rtpSessionEntry": rtpSessionEntry,
       "rtpSessionIndex": rtpSessionIndex,
       "rtpSessionDomain": rtpSessionDomain,
       "rtpSessionRemAddr": rtpSessionRemAddr,
       "rtpSessionLocAddr": rtpSessionLocAddr,
       "rtpSessionIfIndex": rtpSessionIfIndex,
       "rtpSessionSenderJoins": rtpSessionSenderJoins,
       "rtpSessionReceiverJoins": rtpSessionReceiverJoins,
       "rtpSessionByes": rtpSessionByes,
       "rtpSessionStartTime": rtpSessionStartTime,
       "rtpSessionMonitor": rtpSessionMonitor,
       "rtpSessionRowStatus": rtpSessionRowStatus,
       "rtpSenderInverseTable": rtpSenderInverseTable,
       "rtpSenderInverseEntry": rtpSenderInverseEntry,
       "rtpSenderInverseStartTime": rtpSenderInverseStartTime,
       "rtpSenderTable": rtpSenderTable,
       "rtpSenderEntry": rtpSenderEntry,
       "rtpSenderSSRC": rtpSenderSSRC,
       "rtpSenderCNAME": rtpSenderCNAME,
       "rtpSenderAddr": rtpSenderAddr,
       "rtpSenderPackets": rtpSenderPackets,
       "rtpSenderOctets": rtpSenderOctets,
       "rtpSenderTool": rtpSenderTool,
       "rtpSenderSRs": rtpSenderSRs,
       "rtpSenderSRTime": rtpSenderSRTime,
       "rtpSenderPT": rtpSenderPT,
       "rtpSenderStartTime": rtpSenderStartTime,
       "rtpRcvrInverseTable": rtpRcvrInverseTable,
       "rtpRcvrInverseEntry": rtpRcvrInverseEntry,
       "rtpRcvrInverseStartTime": rtpRcvrInverseStartTime,
       "rtpRcvrTable": rtpRcvrTable,
       "rtpRcvrEntry": rtpRcvrEntry,
       "rtpRcvrSRCSSRC": rtpRcvrSRCSSRC,
       "rtpRcvrSSRC": rtpRcvrSSRC,
       "rtpRcvrCNAME": rtpRcvrCNAME,
       "rtpRcvrAddr": rtpRcvrAddr,
       "rtpRcvrRTT": rtpRcvrRTT,
       "rtpRcvrLostPackets": rtpRcvrLostPackets,
       "rtpRcvrJitter": rtpRcvrJitter,
       "rtpRcvrTool": rtpRcvrTool,
       "rtpRcvrRRs": rtpRcvrRRs,
       "rtpRcvrRRTime": rtpRcvrRRTime,
       "rtpRcvrPT": rtpRcvrPT,
       "rtpRcvrPackets": rtpRcvrPackets,
       "rtpRcvrOctets": rtpRcvrOctets,
       "rtpRcvrStartTime": rtpRcvrStartTime,
       "rtpConformance": rtpConformance,
       "rtpGroups": rtpGroups,
       "rtpSystemGroup": rtpSystemGroup,
       "rtpHostGroup": rtpHostGroup,
       "rtpMonitorGroup": rtpMonitorGroup,
       "rtpInverseGroup": rtpInverseGroup,
       "rtpCompliances": rtpCompliances,
       "rtpHostCompliance": rtpHostCompliance,
       "rtpMonitorCompliance": rtpMonitorCompliance}
)
