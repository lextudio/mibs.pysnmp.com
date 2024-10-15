# SNMP MIB module (MERU-GLOBAL-STATISTICS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-GLOBAL-STATISTICS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:12 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwStatistics,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwStatistics")

(MwlBandType,
 MwlNodeType) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlBandType",
    "MwlNodeType")

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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwGlobalStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwIf80211StatsTable_Object = MibTable
mwIf80211StatsTable = _MwIf80211StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    mwIf80211StatsTable.setStatus("current")
_MwIf80211StatsEntry_Object = MibTableRow
mwIf80211StatsEntry = _MwIf80211StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1)
)
mwIf80211StatsEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwIf80211StatsTableIndex"),
)
if mibBuilder.loadTexts:
    mwIf80211StatsEntry.setStatus("current")
_MwIf80211StatsTableIndex_Type = Integer32
_MwIf80211StatsTableIndex_Object = MibTableColumn
mwIf80211StatsTableIndex = _MwIf80211StatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 1),
    _MwIf80211StatsTableIndex_Type()
)
mwIf80211StatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwIf80211StatsTableIndex.setStatus("current")
_MwIf80211StatsNodeId_Type = Unsigned32
_MwIf80211StatsNodeId_Object = MibTableColumn
mwIf80211StatsNodeId = _MwIf80211StatsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 2),
    _MwIf80211StatsNodeId_Type()
)
mwIf80211StatsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsNodeId.setStatus("current")
_MwIf80211StatsIfIndex_Type = Integer32
_MwIf80211StatsIfIndex_Object = MibTableColumn
mwIf80211StatsIfIndex = _MwIf80211StatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 3),
    _MwIf80211StatsIfIndex_Type()
)
mwIf80211StatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsIfIndex.setStatus("current")
_MwIf80211StatsNodeName_Type = DisplayString
_MwIf80211StatsNodeName_Object = MibTableColumn
mwIf80211StatsNodeName = _MwIf80211StatsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 4),
    _MwIf80211StatsNodeName_Type()
)
mwIf80211StatsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsNodeName.setStatus("current")
_MwIf80211StatsThroughput_Type = Counter64
_MwIf80211StatsThroughput_Object = MibTableColumn
mwIf80211StatsThroughput = _MwIf80211StatsThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 5),
    _MwIf80211StatsThroughput_Type()
)
mwIf80211StatsThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsThroughput.setStatus("current")
_MwIf80211StatsNoiseLevel_Type = Integer32
_MwIf80211StatsNoiseLevel_Object = MibTableColumn
mwIf80211StatsNoiseLevel = _MwIf80211StatsNoiseLevel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 6),
    _MwIf80211StatsNoiseLevel_Type()
)
mwIf80211StatsNoiseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsNoiseLevel.setStatus("current")
_MwIf80211StatsFailedCount_Type = Counter64
_MwIf80211StatsFailedCount_Object = MibTableColumn
mwIf80211StatsFailedCount = _MwIf80211StatsFailedCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 7),
    _MwIf80211StatsFailedCount_Type()
)
mwIf80211StatsFailedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsFailedCount.setStatus("current")
_MwIf80211StatsTxFragCount_Type = Counter64
_MwIf80211StatsTxFragCount_Object = MibTableColumn
mwIf80211StatsTxFragCount = _MwIf80211StatsTxFragCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 8),
    _MwIf80211StatsTxFragCount_Type()
)
mwIf80211StatsTxFragCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxFragCount.setStatus("current")
_MwIf80211StatsRxByteCount_Type = Counter64
_MwIf80211StatsRxByteCount_Object = MibTableColumn
mwIf80211StatsRxByteCount = _MwIf80211StatsRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 9),
    _MwIf80211StatsRxByteCount_Type()
)
mwIf80211StatsRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRxByteCount.setStatus("current")
_MwIf80211StatsTxByteCount_Type = Counter64
_MwIf80211StatsTxByteCount_Object = MibTableColumn
mwIf80211StatsTxByteCount = _MwIf80211StatsTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 10),
    _MwIf80211StatsTxByteCount_Type()
)
mwIf80211StatsTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxByteCount.setStatus("current")
_MwIf80211StatsIfRetryCount_Type = Counter64
_MwIf80211StatsIfRetryCount_Object = MibTableColumn
mwIf80211StatsIfRetryCount = _MwIf80211StatsIfRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 11),
    _MwIf80211StatsIfRetryCount_Type()
)
mwIf80211StatsIfRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsIfRetryCount.setStatus("current")
_MwIf80211StatsTxFrameCount_Type = Counter64
_MwIf80211StatsTxFrameCount_Object = MibTableColumn
mwIf80211StatsTxFrameCount = _MwIf80211StatsTxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 12),
    _MwIf80211StatsTxFrameCount_Type()
)
mwIf80211StatsTxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxFrameCount.setStatus("current")
_MwIf80211StatsRcvFragCount_Type = Counter64
_MwIf80211StatsRcvFragCount_Object = MibTableColumn
mwIf80211StatsRcvFragCount = _MwIf80211StatsRcvFragCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 13),
    _MwIf80211StatsRcvFragCount_Type()
)
mwIf80211StatsRcvFragCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRcvFragCount.setStatus("current")
_MwIf80211StatsTxAMSDUCount_Type = Counter64
_MwIf80211StatsTxAMSDUCount_Object = MibTableColumn
mwIf80211StatsTxAMSDUCount = _MwIf80211StatsTxAMSDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 14),
    _MwIf80211StatsTxAMSDUCount_Type()
)
mwIf80211StatsTxAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxAMSDUCount.setStatus("current")
_MwIf80211StatsRxAMSDUCount_Type = Counter64
_MwIf80211StatsRxAMSDUCount_Object = MibTableColumn
mwIf80211StatsRxAMSDUCount = _MwIf80211StatsRxAMSDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 15),
    _MwIf80211StatsRxAMSDUCount_Type()
)
mwIf80211StatsRxAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRxAMSDUCount.setStatus("current")
_MwIf80211StatsTxAMPDUCount_Type = Counter64
_MwIf80211StatsTxAMPDUCount_Object = MibTableColumn
mwIf80211StatsTxAMPDUCount = _MwIf80211StatsTxAMPDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 16),
    _MwIf80211StatsTxAMPDUCount_Type()
)
mwIf80211StatsTxAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxAMPDUCount.setStatus("current")
_MwIf80211StatsRxAMPDUCount_Type = Counter64
_MwIf80211StatsRxAMPDUCount_Object = MibTableColumn
mwIf80211StatsRxAMPDUCount = _MwIf80211StatsRxAMPDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 17),
    _MwIf80211StatsRxAMPDUCount_Type()
)
mwIf80211StatsRxAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRxAMPDUCount.setStatus("current")
_MwIf80211StatsFrameDupCount_Type = Counter64
_MwIf80211StatsFrameDupCount_Object = MibTableColumn
mwIf80211StatsFrameDupCount = _MwIf80211StatsFrameDupCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 18),
    _MwIf80211StatsFrameDupCount_Type()
)
mwIf80211StatsFrameDupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsFrameDupCount.setStatus("current")
_MwIf80211StatsFcsErrorCount_Type = Counter64
_MwIf80211StatsFcsErrorCount_Object = MibTableColumn
mwIf80211StatsFcsErrorCount = _MwIf80211StatsFcsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 19),
    _MwIf80211StatsFcsErrorCount_Type()
)
mwIf80211StatsFcsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsFcsErrorCount.setStatus("current")
_MwIf80211StatsPlcpErrorCount_Type = Counter64
_MwIf80211StatsPlcpErrorCount_Object = MibTableColumn
mwIf80211StatsPlcpErrorCount = _MwIf80211StatsPlcpErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 20),
    _MwIf80211StatsPlcpErrorCount_Type()
)
mwIf80211StatsPlcpErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsPlcpErrorCount.setStatus("current")
_MwIf80211StatsLossPercentage_Type = Integer32
_MwIf80211StatsLossPercentage_Object = MibTableColumn
mwIf80211StatsLossPercentage = _MwIf80211StatsLossPercentage_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 21),
    _MwIf80211StatsLossPercentage_Type()
)
mwIf80211StatsLossPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsLossPercentage.setStatus("current")
_MwIf80211StatsRtsSuccessCount_Type = Counter64
_MwIf80211StatsRtsSuccessCount_Object = MibTableColumn
mwIf80211StatsRtsSuccessCount = _MwIf80211StatsRtsSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 22),
    _MwIf80211StatsRtsSuccessCount_Type()
)
mwIf80211StatsRtsSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRtsSuccessCount.setStatus("current")
_MwIf80211StatsRtsFailureCount_Type = Counter64
_MwIf80211StatsRtsFailureCount_Object = MibTableColumn
mwIf80211StatsRtsFailureCount = _MwIf80211StatsRtsFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 23),
    _MwIf80211StatsRtsFailureCount_Type()
)
mwIf80211StatsRtsFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRtsFailureCount.setStatus("current")
_MwIf80211StatsAckFailureCount_Type = Counter64
_MwIf80211StatsAckFailureCount_Object = MibTableColumn
mwIf80211StatsAckFailureCount = _MwIf80211StatsAckFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 24),
    _MwIf80211StatsAckFailureCount_Type()
)
mwIf80211StatsAckFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsAckFailureCount.setStatus("current")
_MwIf80211StatsRetryAMSDUCount_Type = Counter64
_MwIf80211StatsRetryAMSDUCount_Object = MibTableColumn
mwIf80211StatsRetryAMSDUCount = _MwIf80211StatsRetryAMSDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 25),
    _MwIf80211StatsRetryAMSDUCount_Type()
)
mwIf80211StatsRetryAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRetryAMSDUCount.setStatus("current")
_MwIf80211StatsTxRetryCountBAR_Type = Counter64
_MwIf80211StatsTxRetryCountBAR_Object = MibTableColumn
mwIf80211StatsTxRetryCountBAR = _MwIf80211StatsTxRetryCountBAR_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 26),
    _MwIf80211StatsTxRetryCountBAR_Type()
)
mwIf80211StatsTxRetryCountBAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxRetryCountBAR.setStatus("current")
_MwIf80211StatsFailedAMSDUCount_Type = Counter64
_MwIf80211StatsFailedAMSDUCount_Object = MibTableColumn
mwIf80211StatsFailedAMSDUCount = _MwIf80211StatsFailedAMSDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 27),
    _MwIf80211StatsFailedAMSDUCount_Type()
)
mwIf80211StatsFailedAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsFailedAMSDUCount.setStatus("current")
_MwIf80211StatsPSMPSuccessCount_Type = Counter64
_MwIf80211StatsPSMPSuccessCount_Object = MibTableColumn
mwIf80211StatsPSMPSuccessCount = _MwIf80211StatsPSMPSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 28),
    _MwIf80211StatsPSMPSuccessCount_Type()
)
mwIf80211StatsPSMPSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsPSMPSuccessCount.setStatus("current")
_MwIf80211StatsPSMPFailureCount_Type = Counter64
_MwIf80211StatsPSMPFailureCount_Object = MibTableColumn
mwIf80211StatsPSMPFailureCount = _MwIf80211StatsPSMPFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 29),
    _MwIf80211StatsPSMPFailureCount_Type()
)
mwIf80211StatsPSMPFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsPSMPFailureCount.setStatus("current")
_MwIf80211StatsBeamformingCount_Type = Counter64
_MwIf80211StatsBeamformingCount_Object = MibTableColumn
mwIf80211StatsBeamformingCount = _MwIf80211StatsBeamformingCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 30),
    _MwIf80211StatsBeamformingCount_Type()
)
mwIf80211StatsBeamformingCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsBeamformingCount.setStatus("current")
_MwIf80211StatsMcastTxFrameCount_Type = Counter64
_MwIf80211StatsMcastTxFrameCount_Object = MibTableColumn
mwIf80211StatsMcastTxFrameCount = _MwIf80211StatsMcastTxFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 31),
    _MwIf80211StatsMcastTxFrameCount_Type()
)
mwIf80211StatsMcastTxFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsMcastTxFrameCount.setStatus("current")
_MwIf80211StatsQosCFPollsRxCount_Type = Counter64
_MwIf80211StatsQosCFPollsRxCount_Object = MibTableColumn
mwIf80211StatsQosCFPollsRxCount = _MwIf80211StatsQosCFPollsRxCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 32),
    _MwIf80211StatsQosCFPollsRxCount_Type()
)
mwIf80211StatsQosCFPollsRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsQosCFPollsRxCount.setStatus("current")
_MwIf80211StatsAMSDUAckFailCount_Type = Counter64
_MwIf80211StatsAMSDUAckFailCount_Object = MibTableColumn
mwIf80211StatsAMSDUAckFailCount = _MwIf80211StatsAMSDUAckFailCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 33),
    _MwIf80211StatsAMSDUAckFailCount_Type()
)
mwIf80211StatsAMSDUAckFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsAMSDUAckFailCount.setStatus("current")
_MwIf80211StatsFrame20MhzTxCount_Type = Counter64
_MwIf80211StatsFrame20MhzTxCount_Object = MibTableColumn
mwIf80211StatsFrame20MhzTxCount = _MwIf80211StatsFrame20MhzTxCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 34),
    _MwIf80211StatsFrame20MhzTxCount_Type()
)
mwIf80211StatsFrame20MhzTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsFrame20MhzTxCount.setStatus("current")
_MwIf80211StatsFrame40MhzTxCount_Type = Counter64
_MwIf80211StatsFrame40MhzTxCount_Object = MibTableColumn
mwIf80211StatsFrame40MhzTxCount = _MwIf80211StatsFrame40MhzTxCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 35),
    _MwIf80211StatsFrame40MhzTxCount_Type()
)
mwIf80211StatsFrame40MhzTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsFrame40MhzTxCount.setStatus("current")
_MwIf80211StatsFrame20MhzRxCount_Type = Counter64
_MwIf80211StatsFrame20MhzRxCount_Object = MibTableColumn
mwIf80211StatsFrame20MhzRxCount = _MwIf80211StatsFrame20MhzRxCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 36),
    _MwIf80211StatsFrame20MhzRxCount_Type()
)
mwIf80211StatsFrame20MhzRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsFrame20MhzRxCount.setStatus("current")
_MwIf80211StatsFrame40MhzRxCount_Type = Counter64
_MwIf80211StatsFrame40MhzRxCount_Object = MibTableColumn
mwIf80211StatsFrame40MhzRxCount = _MwIf80211StatsFrame40MhzRxCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 37),
    _MwIf80211StatsFrame40MhzRxCount_Type()
)
mwIf80211StatsFrame40MhzRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsFrame40MhzRxCount.setStatus("current")
_MwIf80211StatsGrantRDGUsedCount_Type = Counter64
_MwIf80211StatsGrantRDGUsedCount_Object = MibTableColumn
mwIf80211StatsGrantRDGUsedCount = _MwIf80211StatsGrantRDGUsedCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 38),
    _MwIf80211StatsGrantRDGUsedCount_Type()
)
mwIf80211StatsGrantRDGUsedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsGrantRDGUsedCount.setStatus("current")
_MwIf80211StatsMultipleRetryCount_Type = Counter64
_MwIf80211StatsMultipleRetryCount_Object = MibTableColumn
mwIf80211StatsMultipleRetryCount = _MwIf80211StatsMultipleRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 39),
    _MwIf80211StatsMultipleRetryCount_Type()
)
mwIf80211StatsMultipleRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsMultipleRetryCount.setStatus("current")
_MwIf80211StatsMcastRcvFrameCount_Type = Counter64
_MwIf80211StatsMcastRcvFrameCount_Object = MibTableColumn
mwIf80211StatsMcastRcvFrameCount = _MwIf80211StatsMcastRcvFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 40),
    _MwIf80211StatsMcastRcvFrameCount_Type()
)
mwIf80211StatsMcastRcvFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsMcastRcvFrameCount.setStatus("current")
_MwIf80211StatsChannelUtilization_Type = Counter64
_MwIf80211StatsChannelUtilization_Object = MibTableColumn
mwIf80211StatsChannelUtilization = _MwIf80211StatsChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 41),
    _MwIf80211StatsChannelUtilization_Type()
)
mwIf80211StatsChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsChannelUtilization.setStatus("current")
_MwIf80211StatsTxMPDUInAMPDUCount_Type = Counter64
_MwIf80211StatsTxMPDUInAMPDUCount_Object = MibTableColumn
mwIf80211StatsTxMPDUInAMPDUCount = _MwIf80211StatsTxMPDUInAMPDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 42),
    _MwIf80211StatsTxMPDUInAMPDUCount_Type()
)
mwIf80211StatsTxMPDUInAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxMPDUInAMPDUCount.setStatus("current")
_MwIf80211StatsMPDUInRxAMPDUCount_Type = Counter64
_MwIf80211StatsMPDUInRxAMPDUCount_Object = MibTableColumn
mwIf80211StatsMPDUInRxAMPDUCount = _MwIf80211StatsMPDUInRxAMPDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 43),
    _MwIf80211StatsMPDUInRxAMPDUCount_Type()
)
mwIf80211StatsMPDUInRxAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsMPDUInRxAMPDUCount.setStatus("current")
_MwIf80211StatsTxRetryCountUnaggr_Type = Counter64
_MwIf80211StatsTxRetryCountUnaggr_Object = MibTableColumn
mwIf80211StatsTxRetryCountUnaggr = _MwIf80211StatsTxRetryCountUnaggr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 44),
    _MwIf80211StatsTxRetryCountUnaggr_Type()
)
mwIf80211StatsTxRetryCountUnaggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxRetryCountUnaggr.setStatus("current")
_MwIf80211StatsRxRetriedFrameCount_Type = Counter64
_MwIf80211StatsRxRetriedFrameCount_Object = MibTableColumn
mwIf80211StatsRxRetriedFrameCount = _MwIf80211StatsRxRetriedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 45),
    _MwIf80211StatsRxRetriedFrameCount_Type()
)
mwIf80211StatsRxRetriedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRxRetriedFrameCount.setStatus("current")
_MwIf80211StatsRxUnicastFrameCount_Type = Counter64
_MwIf80211StatsRxUnicastFrameCount_Object = MibTableColumn
mwIf80211StatsRxUnicastFrameCount = _MwIf80211StatsRxUnicastFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 46),
    _MwIf80211StatsRxUnicastFrameCount_Type()
)
mwIf80211StatsRxUnicastFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRxUnicastFrameCount.setStatus("current")
_MwIf80211StatsQosCFPollsLostCount_Type = Counter64
_MwIf80211StatsQosCFPollsLostCount_Object = MibTableColumn
mwIf80211StatsQosCFPollsLostCount = _MwIf80211StatsQosCFPollsLostCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 47),
    _MwIf80211StatsQosCFPollsLostCount_Type()
)
mwIf80211StatsQosCFPollsLostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsQosCFPollsLostCount.setStatus("current")
_MwIf80211StatsGrantRDGUnusedCount_Type = Counter64
_MwIf80211StatsGrantRDGUnusedCount_Object = MibTableColumn
mwIf80211StatsGrantRDGUnusedCount = _MwIf80211StatsGrantRDGUnusedCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 48),
    _MwIf80211StatsGrantRDGUnusedCount_Type()
)
mwIf80211StatsGrantRDGUnusedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsGrantRDGUnusedCount.setStatus("current")
_MwIf80211StatsDualCTSSuccessCount_Type = Counter64
_MwIf80211StatsDualCTSSuccessCount_Object = MibTableColumn
mwIf80211StatsDualCTSSuccessCount = _MwIf80211StatsDualCTSSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 49),
    _MwIf80211StatsDualCTSSuccessCount_Type()
)
mwIf80211StatsDualCTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsDualCTSSuccessCount.setStatus("current")
_MwIf80211StatsDualCTSFailureCount_Type = Counter64
_MwIf80211StatsDualCTSFailureCount_Object = MibTableColumn
mwIf80211StatsDualCTSFailureCount = _MwIf80211StatsDualCTSFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 50),
    _MwIf80211StatsDualCTSFailureCount_Type()
)
mwIf80211StatsDualCTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsDualCTSFailureCount.setStatus("current")
_MwIf80211StatsSTBCCTSSuccessCount_Type = Counter64
_MwIf80211StatsSTBCCTSSuccessCount_Object = MibTableColumn
mwIf80211StatsSTBCCTSSuccessCount = _MwIf80211StatsSTBCCTSSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 51),
    _MwIf80211StatsSTBCCTSSuccessCount_Type()
)
mwIf80211StatsSTBCCTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsSTBCCTSSuccessCount.setStatus("current")
_MwIf80211StatsSTBCCTSFailureCount_Type = Counter64
_MwIf80211StatsSTBCCTSFailureCount_Object = MibTableColumn
mwIf80211StatsSTBCCTSFailureCount = _MwIf80211StatsSTBCCTSFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 52),
    _MwIf80211StatsSTBCCTSFailureCount_Type()
)
mwIf80211StatsSTBCCTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsSTBCCTSFailureCount.setStatus("current")
_MwIf80211StatsRTSLSIGSuccessCount_Type = Counter64
_MwIf80211StatsRTSLSIGSuccessCount_Object = MibTableColumn
mwIf80211StatsRTSLSIGSuccessCount = _MwIf80211StatsRTSLSIGSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 53),
    _MwIf80211StatsRTSLSIGSuccessCount_Type()
)
mwIf80211StatsRTSLSIGSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRTSLSIGSuccessCount.setStatus("current")
_MwIf80211StatsRTSLSIGFailureCount_Type = Counter64
_MwIf80211StatsRTSLSIGFailureCount_Object = MibTableColumn
mwIf80211StatsRTSLSIGFailureCount = _MwIf80211StatsRTSLSIGFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 54),
    _MwIf80211StatsRTSLSIGFailureCount_Type()
)
mwIf80211StatsRTSLSIGFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRTSLSIGFailureCount.setStatus("current")
_MwIf80211StatsAssignedStationCount_Type = Counter64
_MwIf80211StatsAssignedStationCount_Object = MibTableColumn
mwIf80211StatsAssignedStationCount = _MwIf80211StatsAssignedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 55),
    _MwIf80211StatsAssignedStationCount_Type()
)
mwIf80211StatsAssignedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsAssignedStationCount.setStatus("current")
_MwIf80211StatsMultiRetryAMSDUCount_Type = Counter64
_MwIf80211StatsMultiRetryAMSDUCount_Object = MibTableColumn
mwIf80211StatsMultiRetryAMSDUCount = _MwIf80211StatsMultiRetryAMSDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 56),
    _MwIf80211StatsMultiRetryAMSDUCount_Type()
)
mwIf80211StatsMultiRetryAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsMultiRetryAMSDUCount.setStatus("current")
_MwIf80211StatsTxOctetsInAMSDUCount_Type = Counter64
_MwIf80211StatsTxOctetsInAMSDUCount_Object = MibTableColumn
mwIf80211StatsTxOctetsInAMSDUCount = _MwIf80211StatsTxOctetsInAMSDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 57),
    _MwIf80211StatsTxOctetsInAMSDUCount_Type()
)
mwIf80211StatsTxOctetsInAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxOctetsInAMSDUCount.setStatus("current")
_MwIf80211StatsRxOctetsInAMSDUCount_Type = Counter64
_MwIf80211StatsRxOctetsInAMSDUCount_Object = MibTableColumn
mwIf80211StatsRxOctetsInAMSDUCount = _MwIf80211StatsRxOctetsInAMSDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 58),
    _MwIf80211StatsRxOctetsInAMSDUCount_Type()
)
mwIf80211StatsRxOctetsInAMSDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRxOctetsInAMSDUCount.setStatus("current")
_MwIf80211StatsTxOctetsInAMPDUCount_Type = Counter64
_MwIf80211StatsTxOctetsInAMPDUCount_Object = MibTableColumn
mwIf80211StatsTxOctetsInAMPDUCount = _MwIf80211StatsTxOctetsInAMPDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 59),
    _MwIf80211StatsTxOctetsInAMPDUCount_Type()
)
mwIf80211StatsTxOctetsInAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxOctetsInAMPDUCount.setStatus("current")
_MwIf80211StatsRxOctetsInAMPDUCount_Type = Counter64
_MwIf80211StatsRxOctetsInAMPDUCount_Object = MibTableColumn
mwIf80211StatsRxOctetsInAMPDUCount = _MwIf80211StatsRxOctetsInAMPDUCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 60),
    _MwIf80211StatsRxOctetsInAMPDUCount_Type()
)
mwIf80211StatsRxOctetsInAMPDUCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRxOctetsInAMPDUCount.setStatus("current")
_MwIf80211StatsImplicitBARFailCount_Type = Counter64
_MwIf80211StatsImplicitBARFailCount_Object = MibTableColumn
mwIf80211StatsImplicitBARFailCount = _MwIf80211StatsImplicitBARFailCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 61),
    _MwIf80211StatsImplicitBARFailCount_Type()
)
mwIf80211StatsImplicitBARFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsImplicitBARFailCount.setStatus("current")
_MwIf80211StatsExplicitBARFailCount_Type = Counter64
_MwIf80211StatsExplicitBARFailCount_Object = MibTableColumn
mwIf80211StatsExplicitBARFailCount = _MwIf80211StatsExplicitBARFailCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 62),
    _MwIf80211StatsExplicitBARFailCount_Type()
)
mwIf80211StatsExplicitBARFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsExplicitBARFailCount.setStatus("current")
_MwIf80211StatsChanWidthSwitchCount_Type = Counter64
_MwIf80211StatsChanWidthSwitchCount_Object = MibTableColumn
mwIf80211StatsChanWidthSwitchCount = _MwIf80211StatsChanWidthSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 63),
    _MwIf80211StatsChanWidthSwitchCount_Type()
)
mwIf80211StatsChanWidthSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsChanWidthSwitchCount.setStatus("current")
_MwIf80211StatsTxMultiRetryCountBAR_Type = Counter64
_MwIf80211StatsTxMultiRetryCountBAR_Object = MibTableColumn
mwIf80211StatsTxMultiRetryCountBAR = _MwIf80211StatsTxMultiRetryCountBAR_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 64),
    _MwIf80211StatsTxMultiRetryCountBAR_Type()
)
mwIf80211StatsTxMultiRetryCountBAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxMultiRetryCountBAR.setStatus("current")
_MwIf80211StatsWepUndecryptableCount_Type = Counter64
_MwIf80211StatsWepUndecryptableCount_Object = MibTableColumn
mwIf80211StatsWepUndecryptableCount = _MwIf80211StatsWepUndecryptableCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 65),
    _MwIf80211StatsWepUndecryptableCount_Type()
)
mwIf80211StatsWepUndecryptableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsWepUndecryptableCount.setStatus("current")
_MwIf80211StatsQosDiscardedFragCount_Type = Counter64
_MwIf80211StatsQosDiscardedFragCount_Object = MibTableColumn
mwIf80211StatsQosDiscardedFragCount = _MwIf80211StatsQosDiscardedFragCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 66),
    _MwIf80211StatsQosDiscardedFragCount_Type()
)
mwIf80211StatsQosDiscardedFragCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsQosDiscardedFragCount.setStatus("current")
_MwIf80211StatsQosCFPollsUnusedCount_Type = Counter64
_MwIf80211StatsQosCFPollsUnusedCount_Object = MibTableColumn
mwIf80211StatsQosCFPollsUnusedCount = _MwIf80211StatsQosCFPollsUnusedCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 67),
    _MwIf80211StatsQosCFPollsUnusedCount_Type()
)
mwIf80211StatsQosCFPollsUnusedCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsQosCFPollsUnusedCount.setStatus("current")
_MwIf80211StatsAMPDUDelCRCErrorCount_Type = Counter64
_MwIf80211StatsAMPDUDelCRCErrorCount_Object = MibTableColumn
mwIf80211StatsAMPDUDelCRCErrorCount = _MwIf80211StatsAMPDUDelCRCErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 68),
    _MwIf80211StatsAMPDUDelCRCErrorCount_Type()
)
mwIf80211StatsAMPDUDelCRCErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsAMPDUDelCRCErrorCount.setStatus("current")
_MwIf80211StatsTxRetryCountSubfrAggr_Type = Counter64
_MwIf80211StatsTxRetryCountSubfrAggr_Object = MibTableColumn
mwIf80211StatsTxRetryCountSubfrAggr = _MwIf80211StatsTxRetryCountSubfrAggr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 69),
    _MwIf80211StatsTxRetryCountSubfrAggr_Type()
)
mwIf80211StatsTxRetryCountSubfrAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxRetryCountSubfrAggr.setStatus("current")
_MwIf80211StatsAssociatedStationCount_Type = Counter64
_MwIf80211StatsAssociatedStationCount_Object = MibTableColumn
mwIf80211StatsAssociatedStationCount = _MwIf80211StatsAssociatedStationCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 70),
    _MwIf80211StatsAssociatedStationCount_Type()
)
mwIf80211StatsAssociatedStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsAssociatedStationCount.setStatus("current")
_MwIf80211StatsDiscoveredStationCount_Type = Counter64
_MwIf80211StatsDiscoveredStationCount_Object = MibTableColumn
mwIf80211StatsDiscoveredStationCount = _MwIf80211StatsDiscoveredStationCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 71),
    _MwIf80211StatsDiscoveredStationCount_Type()
)
mwIf80211StatsDiscoveredStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsDiscoveredStationCount.setStatus("current")
_MwIf80211StatsTxFrameInGrantRDGCount_Type = Counter64
_MwIf80211StatsTxFrameInGrantRDGCount_Object = MibTableColumn
mwIf80211StatsTxFrameInGrantRDGCount = _MwIf80211StatsTxFrameInGrantRDGCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 72),
    _MwIf80211StatsTxFrameInGrantRDGCount_Type()
)
mwIf80211StatsTxFrameInGrantRDGCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxFrameInGrantRDGCount.setStatus("current")
_MwIf80211StatsTxOctetInGrantRDGCount_Type = Counter64
_MwIf80211StatsTxOctetInGrantRDGCount_Object = MibTableColumn
mwIf80211StatsTxOctetInGrantRDGCount = _MwIf80211StatsTxOctetInGrantRDGCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 73),
    _MwIf80211StatsTxOctetInGrantRDGCount_Type()
)
mwIf80211StatsTxOctetInGrantRDGCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxOctetInGrantRDGCount.setStatus("current")
_MwIf80211StatsNonSTBCCTSSuccessCount_Type = Counter64
_MwIf80211StatsNonSTBCCTSSuccessCount_Object = MibTableColumn
mwIf80211StatsNonSTBCCTSSuccessCount = _MwIf80211StatsNonSTBCCTSSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 74),
    _MwIf80211StatsNonSTBCCTSSuccessCount_Type()
)
mwIf80211StatsNonSTBCCTSSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsNonSTBCCTSSuccessCount.setStatus("current")
_MwIf80211StatsNonSTBCCTSFailureCount_Type = Counter64
_MwIf80211StatsNonSTBCCTSFailureCount_Object = MibTableColumn
mwIf80211StatsNonSTBCCTSFailureCount = _MwIf80211StatsNonSTBCCTSFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 75),
    _MwIf80211StatsNonSTBCCTSFailureCount_Type()
)
mwIf80211StatsNonSTBCCTSFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsNonSTBCCTSFailureCount.setStatus("current")
_MwIf80211StatsTxRetryLimitExCountBAR_Type = Counter64
_MwIf80211StatsTxRetryLimitExCountBAR_Object = MibTableColumn
mwIf80211StatsTxRetryLimitExCountBAR = _MwIf80211StatsTxRetryLimitExCountBAR_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 76),
    _MwIf80211StatsTxRetryLimitExCountBAR_Type()
)
mwIf80211StatsTxRetryLimitExCountBAR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxRetryLimitExCountBAR.setStatus("current")
_MwIf80211StatsQosCFPollsUnusableCount_Type = Counter64
_MwIf80211StatsQosCFPollsUnusableCount_Object = MibTableColumn
mwIf80211StatsQosCFPollsUnusableCount = _MwIf80211StatsQosCFPollsUnusableCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 77),
    _MwIf80211StatsQosCFPollsUnusableCount_Type()
)
mwIf80211StatsQosCFPollsUnusableCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsQosCFPollsUnusableCount.setStatus("current")
_MwIf80211StatsTxRetryLimitExCountAggr_Type = Counter64
_MwIf80211StatsTxRetryLimitExCountAggr_Object = MibTableColumn
mwIf80211StatsTxRetryLimitExCountAggr = _MwIf80211StatsTxRetryLimitExCountAggr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 78),
    _MwIf80211StatsTxRetryLimitExCountAggr_Type()
)
mwIf80211StatsTxRetryLimitExCountAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxRetryLimitExCountAggr.setStatus("current")
_MwIf80211StatsTxMultiRetryCountUnaggr_Type = Counter64
_MwIf80211StatsTxMultiRetryCountUnaggr_Object = MibTableColumn
mwIf80211StatsTxMultiRetryCountUnaggr = _MwIf80211StatsTxMultiRetryCountUnaggr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 79),
    _MwIf80211StatsTxMultiRetryCountUnaggr_Type()
)
mwIf80211StatsTxMultiRetryCountUnaggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxMultiRetryCountUnaggr.setStatus("current")
_MwIf80211StatsTxRetryLimitExCountUnaggr_Type = Counter64
_MwIf80211StatsTxRetryLimitExCountUnaggr_Object = MibTableColumn
mwIf80211StatsTxRetryLimitExCountUnaggr = _MwIf80211StatsTxRetryLimitExCountUnaggr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 81),
    _MwIf80211StatsTxRetryLimitExCountUnaggr_Type()
)
mwIf80211StatsTxRetryLimitExCountUnaggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxRetryLimitExCountUnaggr.setStatus("current")
_MwIf80211StatsTxMultiRetryCountSubfrAggr_Type = Counter64
_MwIf80211StatsTxMultiRetryCountSubfrAggr_Object = MibTableColumn
mwIf80211StatsTxMultiRetryCountSubfrAggr = _MwIf80211StatsTxMultiRetryCountSubfrAggr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 82),
    _MwIf80211StatsTxMultiRetryCountSubfrAggr_Type()
)
mwIf80211StatsTxMultiRetryCountSubfrAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxMultiRetryCountSubfrAggr.setStatus("current")
_MwIf80211StatsTxRetryLimitExCountSubfrAggr_Type = Counter64
_MwIf80211StatsTxRetryLimitExCountSubfrAggr_Object = MibTableColumn
mwIf80211StatsTxRetryLimitExCountSubfrAggr = _MwIf80211StatsTxRetryLimitExCountSubfrAggr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 83),
    _MwIf80211StatsTxRetryLimitExCountSubfrAggr_Type()
)
mwIf80211StatsTxRetryLimitExCountSubfrAggr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxRetryLimitExCountSubfrAggr.setStatus("current")
_MwIf80211StatsUnicastBeaconLossThrExceeded_Type = Counter64
_MwIf80211StatsUnicastBeaconLossThrExceeded_Object = MibTableColumn
mwIf80211StatsUnicastBeaconLossThrExceeded = _MwIf80211StatsUnicastBeaconLossThrExceeded_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 84),
    _MwIf80211StatsUnicastBeaconLossThrExceeded_Type()
)
mwIf80211StatsUnicastBeaconLossThrExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsUnicastBeaconLossThrExceeded.setStatus("current")
_MwIf80211StatsTxFailedHwRetryExceeded_Type = Counter64
_MwIf80211StatsTxFailedHwRetryExceeded_Object = MibTableColumn
mwIf80211StatsTxFailedHwRetryExceeded = _MwIf80211StatsTxFailedHwRetryExceeded_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 85),
    _MwIf80211StatsTxFailedHwRetryExceeded_Type()
)
mwIf80211StatsTxFailedHwRetryExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxFailedHwRetryExceeded.setStatus("current")
_MwIf80211StatsRxDataForAssignedStations_Type = Unsigned32
_MwIf80211StatsRxDataForAssignedStations_Object = MibTableColumn
mwIf80211StatsRxDataForAssignedStations = _MwIf80211StatsRxDataForAssignedStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 86),
    _MwIf80211StatsRxDataForAssignedStations_Type()
)
mwIf80211StatsRxDataForAssignedStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRxDataForAssignedStations.setStatus("current")
_MwIf80211StatsRxMgmtFramesForAssignedStations_Type = Unsigned32
_MwIf80211StatsRxMgmtFramesForAssignedStations_Object = MibTableColumn
mwIf80211StatsRxMgmtFramesForAssignedStations = _MwIf80211StatsRxMgmtFramesForAssignedStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 87),
    _MwIf80211StatsRxMgmtFramesForAssignedStations_Type()
)
mwIf80211StatsRxMgmtFramesForAssignedStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRxMgmtFramesForAssignedStations.setStatus("current")
_MwIf80211StatsTotalRxMgmtFrames_Type = Unsigned32
_MwIf80211StatsTotalRxMgmtFrames_Object = MibTableColumn
mwIf80211StatsTotalRxMgmtFrames = _MwIf80211StatsTotalRxMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 88),
    _MwIf80211StatsTotalRxMgmtFrames_Type()
)
mwIf80211StatsTotalRxMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTotalRxMgmtFrames.setStatus("current")
_MwIf80211StatsTotalRxControlFrames_Type = Unsigned32
_MwIf80211StatsTotalRxControlFrames_Object = MibTableColumn
mwIf80211StatsTotalRxControlFrames = _MwIf80211StatsTotalRxControlFrames_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 89),
    _MwIf80211StatsTotalRxControlFrames_Type()
)
mwIf80211StatsTotalRxControlFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTotalRxControlFrames.setStatus("current")
_MwIf80211StatsMgmtFrameOverheadInAirtime_Type = Unsigned32
_MwIf80211StatsMgmtFrameOverheadInAirtime_Object = MibTableColumn
mwIf80211StatsMgmtFrameOverheadInAirtime = _MwIf80211StatsMgmtFrameOverheadInAirtime_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 90),
    _MwIf80211StatsMgmtFrameOverheadInAirtime_Type()
)
mwIf80211StatsMgmtFrameOverheadInAirtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsMgmtFrameOverheadInAirtime.setStatus("current")
_MwIf80211StatsTxUnicastFrameCount_Type = Counter64
_MwIf80211StatsTxUnicastFrameCount_Object = MibTableColumn
mwIf80211StatsTxUnicastFrameCount = _MwIf80211StatsTxUnicastFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 91),
    _MwIf80211StatsTxUnicastFrameCount_Type()
)
mwIf80211StatsTxUnicastFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsTxUnicastFrameCount.setStatus("current")
_MwIf80211StatsRxAllDataFrameCount_Type = Counter64
_MwIf80211StatsRxAllDataFrameCount_Object = MibTableColumn
mwIf80211StatsRxAllDataFrameCount = _MwIf80211StatsRxAllDataFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 92),
    _MwIf80211StatsRxAllDataFrameCount_Type()
)
mwIf80211StatsRxAllDataFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRxAllDataFrameCount.setStatus("current")
_MwIf80211StatsRfBarrierActions_Type = Counter64
_MwIf80211StatsRfBarrierActions_Object = MibTableColumn
mwIf80211StatsRfBarrierActions = _MwIf80211StatsRfBarrierActions_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 93),
    _MwIf80211StatsRfBarrierActions_Type()
)
mwIf80211StatsRfBarrierActions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRfBarrierActions.setStatus("current")
_MwIf80211StatsBeaconOverhead_Type = Integer32
_MwIf80211StatsBeaconOverhead_Object = MibTableColumn
mwIf80211StatsBeaconOverhead = _MwIf80211StatsBeaconOverhead_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 94),
    _MwIf80211StatsBeaconOverhead_Type()
)
mwIf80211StatsBeaconOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsBeaconOverhead.setStatus("current")
_MwIf80211StatsProbeReqRespOverhead_Type = Integer32
_MwIf80211StatsProbeReqRespOverhead_Object = MibTableColumn
mwIf80211StatsProbeReqRespOverhead = _MwIf80211StatsProbeReqRespOverhead_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 95),
    _MwIf80211StatsProbeReqRespOverhead_Type()
)
mwIf80211StatsProbeReqRespOverhead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsProbeReqRespOverhead.setStatus("current")
_MwIf80211StatsNeighborhoodCounter_Type = Unsigned32
_MwIf80211StatsNeighborhoodCounter_Object = MibTableColumn
mwIf80211StatsNeighborhoodCounter = _MwIf80211StatsNeighborhoodCounter_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 96),
    _MwIf80211StatsNeighborhoodCounter_Type()
)
mwIf80211StatsNeighborhoodCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsNeighborhoodCounter.setStatus("current")
_MwIf80211StatsPotentialBeaconCollisionCounter_Type = Unsigned32
_MwIf80211StatsPotentialBeaconCollisionCounter_Object = MibTableColumn
mwIf80211StatsPotentialBeaconCollisionCounter = _MwIf80211StatsPotentialBeaconCollisionCounter_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 97),
    _MwIf80211StatsPotentialBeaconCollisionCounter_Type()
)
mwIf80211StatsPotentialBeaconCollisionCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsPotentialBeaconCollisionCounter.setStatus("current")
_MwIf80211StatsProfileBeaconDataRate_Type = DisplayString
_MwIf80211StatsProfileBeaconDataRate_Object = MibTableColumn
mwIf80211StatsProfileBeaconDataRate = _MwIf80211StatsProfileBeaconDataRate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 98),
    _MwIf80211StatsProfileBeaconDataRate_Type()
)
mwIf80211StatsProfileBeaconDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsProfileBeaconDataRate.setStatus("current")
_MwIf80211StatsRetryPercentage_Type = Integer32
_MwIf80211StatsRetryPercentage_Object = MibTableColumn
mwIf80211StatsRetryPercentage = _MwIf80211StatsRetryPercentage_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 99),
    _MwIf80211StatsRetryPercentage_Type()
)
mwIf80211StatsRetryPercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsRetryPercentage.setStatus("current")
_MwIf80211StatsChannel_Type = Unsigned32
_MwIf80211StatsChannel_Object = MibTableColumn
mwIf80211StatsChannel = _MwIf80211StatsChannel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 100),
    _MwIf80211StatsChannel_Type()
)
mwIf80211StatsChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIf80211StatsChannel.setStatus("current")
_MwIf80211StatsRowStatus_Type = RowStatus
_MwIf80211StatsRowStatus_Object = MibTableColumn
mwIf80211StatsRowStatus = _MwIf80211StatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 1, 1, 103),
    _MwIf80211StatsRowStatus_Type()
)
mwIf80211StatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwIf80211StatsRowStatus.setStatus("current")
_MwIfStatsTable_Object = MibTable
mwIfStatsTable = _MwIfStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    mwIfStatsTable.setStatus("current")
_MwIfStatsEntry_Object = MibTableRow
mwIfStatsEntry = _MwIfStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1)
)
mwIfStatsEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwIfStatsTableIndex"),
)
if mibBuilder.loadTexts:
    mwIfStatsEntry.setStatus("current")
_MwIfStatsTableIndex_Type = Integer32
_MwIfStatsTableIndex_Object = MibTableColumn
mwIfStatsTableIndex = _MwIfStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 1),
    _MwIfStatsTableIndex_Type()
)
mwIfStatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwIfStatsTableIndex.setStatus("current")
_MwIfStatsIfIndex_Type = Integer32
_MwIfStatsIfIndex_Object = MibTableColumn
mwIfStatsIfIndex = _MwIfStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 2),
    _MwIfStatsIfIndex_Type()
)
mwIfStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfIndex.setStatus("current")
_MwIfStatsIfDescr_Type = DisplayString
_MwIfStatsIfDescr_Object = MibTableColumn
mwIfStatsIfDescr = _MwIfStatsIfDescr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 3),
    _MwIfStatsIfDescr_Type()
)
mwIfStatsIfDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfDescr.setStatus("current")
_MwIfStatsIfNodeId_Type = Integer32
_MwIfStatsIfNodeId_Object = MibTableColumn
mwIfStatsIfNodeId = _MwIfStatsIfNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 4),
    _MwIfStatsIfNodeId_Type()
)
mwIfStatsIfNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfNodeId.setStatus("current")
_MwIfStatsIfOutQLen_Type = Counter64
_MwIfStatsIfOutQLen_Object = MibTableColumn
mwIfStatsIfOutQLen = _MwIfStatsIfOutQLen_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 5),
    _MwIfStatsIfOutQLen_Type()
)
mwIfStatsIfOutQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfOutQLen.setStatus("current")
_MwIfStatsIfNodeName_Type = DisplayString
_MwIfStatsIfNodeName_Object = MibTableColumn
mwIfStatsIfNodeName = _MwIfStatsIfNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 6),
    _MwIfStatsIfNodeName_Type()
)
mwIfStatsIfNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfNodeName.setStatus("current")
_MwIfStatsIfNodeType_Type = MwlNodeType
_MwIfStatsIfNodeType_Object = MibTableColumn
mwIfStatsIfNodeType = _MwIfStatsIfNodeType_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 7),
    _MwIfStatsIfNodeType_Type()
)
mwIfStatsIfNodeType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfNodeType.setStatus("current")
_MwIfStatsIfInOctets_Type = Counter64
_MwIfStatsIfInOctets_Object = MibTableColumn
mwIfStatsIfInOctets = _MwIfStatsIfInOctets_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 8),
    _MwIfStatsIfInOctets_Type()
)
mwIfStatsIfInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfInOctets.setStatus("current")
_MwIfStatsIfInErrors_Type = Counter64
_MwIfStatsIfInErrors_Object = MibTableColumn
mwIfStatsIfInErrors = _MwIfStatsIfInErrors_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 9),
    _MwIfStatsIfInErrors_Type()
)
mwIfStatsIfInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfInErrors.setStatus("current")
_MwIfStatsIfOutOctets_Type = Counter64
_MwIfStatsIfOutOctets_Object = MibTableColumn
mwIfStatsIfOutOctets = _MwIfStatsIfOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 10),
    _MwIfStatsIfOutOctets_Type()
)
mwIfStatsIfOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfOutOctets.setStatus("current")
_MwIfStatsIfOutErrors_Type = Counter64
_MwIfStatsIfOutErrors_Object = MibTableColumn
mwIfStatsIfOutErrors = _MwIfStatsIfOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 11),
    _MwIfStatsIfOutErrors_Type()
)
mwIfStatsIfOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfOutErrors.setStatus("current")
_MwIfStatsIfInDiscards_Type = Counter64
_MwIfStatsIfInDiscards_Object = MibTableColumn
mwIfStatsIfInDiscards = _MwIfStatsIfInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 12),
    _MwIfStatsIfInDiscards_Type()
)
mwIfStatsIfInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfInDiscards.setStatus("current")
_MwIfStatsIfInUcastPkts_Type = Counter64
_MwIfStatsIfInUcastPkts_Object = MibTableColumn
mwIfStatsIfInUcastPkts = _MwIfStatsIfInUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 13),
    _MwIfStatsIfInUcastPkts_Type()
)
mwIfStatsIfInUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfInUcastPkts.setStatus("current")
_MwIfStatsIfOutDiscards_Type = Counter64
_MwIfStatsIfOutDiscards_Object = MibTableColumn
mwIfStatsIfOutDiscards = _MwIfStatsIfOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 14),
    _MwIfStatsIfOutDiscards_Type()
)
mwIfStatsIfOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfOutDiscards.setStatus("current")
_MwIfStatsIfInNUcastPkts_Type = Counter64
_MwIfStatsIfInNUcastPkts_Object = MibTableColumn
mwIfStatsIfInNUcastPkts = _MwIfStatsIfInNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 15),
    _MwIfStatsIfInNUcastPkts_Type()
)
mwIfStatsIfInNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfInNUcastPkts.setStatus("current")
_MwIfStatsIfOutUcastPkts_Type = Counter64
_MwIfStatsIfOutUcastPkts_Object = MibTableColumn
mwIfStatsIfOutUcastPkts = _MwIfStatsIfOutUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 16),
    _MwIfStatsIfOutUcastPkts_Type()
)
mwIfStatsIfOutUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfOutUcastPkts.setStatus("current")
_MwIfStatsIfOutNUcastPkts_Type = Counter64
_MwIfStatsIfOutNUcastPkts_Object = MibTableColumn
mwIfStatsIfOutNUcastPkts = _MwIfStatsIfOutNUcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 17),
    _MwIfStatsIfOutNUcastPkts_Type()
)
mwIfStatsIfOutNUcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfOutNUcastPkts.setStatus("current")
_MwIfStatsIfInUnknownProtos_Type = Counter64
_MwIfStatsIfInUnknownProtos_Object = MibTableColumn
mwIfStatsIfInUnknownProtos = _MwIfStatsIfInUnknownProtos_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 18),
    _MwIfStatsIfInUnknownProtos_Type()
)
mwIfStatsIfInUnknownProtos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwIfStatsIfInUnknownProtos.setStatus("current")
_MwIfStatsRowStatus_Type = RowStatus
_MwIfStatsRowStatus_Object = MibTableColumn
mwIfStatsRowStatus = _MwIfStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 2, 1, 19),
    _MwIfStatsRowStatus_Type()
)
mwIfStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwIfStatsRowStatus.setStatus("current")
_MwAuthStats_ObjectIdentity = ObjectIdentity
mwAuthStats = _MwAuthStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 3)
)
_MwAuthStatsAuth8021xRequestCount_Type = Unsigned32
_MwAuthStatsAuth8021xRequestCount_Object = MibScalar
mwAuthStatsAuth8021xRequestCount = _MwAuthStatsAuth8021xRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 3, 1),
    _MwAuthStatsAuth8021xRequestCount_Type()
)
mwAuthStatsAuth8021xRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAuthStatsAuth8021xRequestCount.setStatus("current")
_MwAuthStatsAuth8021xSuccessCount_Type = Unsigned32
_MwAuthStatsAuth8021xSuccessCount_Object = MibScalar
mwAuthStatsAuth8021xSuccessCount = _MwAuthStatsAuth8021xSuccessCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 3, 2),
    _MwAuthStatsAuth8021xSuccessCount_Type()
)
mwAuthStatsAuth8021xSuccessCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAuthStatsAuth8021xSuccessCount.setStatus("current")
_MwAuthStatsAuth8021xFailureCount_Type = Unsigned32
_MwAuthStatsAuth8021xFailureCount_Object = MibScalar
mwAuthStatsAuth8021xFailureCount = _MwAuthStatsAuth8021xFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 3, 3),
    _MwAuthStatsAuth8021xFailureCount_Type()
)
mwAuthStatsAuth8021xFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAuthStatsAuth8021xFailureCount.setStatus("current")
_MwAuthStatsAuth8021xStationCount_Type = Unsigned32
_MwAuthStatsAuth8021xStationCount_Object = MibScalar
mwAuthStatsAuth8021xStationCount = _MwAuthStatsAuth8021xStationCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 3, 4),
    _MwAuthStatsAuth8021xStationCount_Type()
)
mwAuthStatsAuth8021xStationCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAuthStatsAuth8021xStationCount.setStatus("current")
_MwQosStats_ObjectIdentity = ObjectIdentity
mwQosStats = _MwQosStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4)
)
_MwQosStatsSessionCount_Type = Counter64
_MwQosStatsSessionCount_Object = MibScalar
mwQosStatsSessionCount = _MwQosStatsSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 1),
    _MwQosStatsSessionCount_Type()
)
mwQosStatsSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsSessionCount.setStatus("current")
_MwQosStatsH323SessionCount_Type = Counter64
_MwQosStatsH323SessionCount_Object = MibScalar
mwQosStatsH323SessionCount = _MwQosStatsH323SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 2),
    _MwQosStatsH323SessionCount_Type()
)
mwQosStatsH323SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsH323SessionCount.setStatus("current")
_MwQosStatsSipSessionCount_Type = Counter64
_MwQosStatsSipSessionCount_Object = MibScalar
mwQosStatsSipSessionCount = _MwQosStatsSipSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 3),
    _MwQosStatsSipSessionCount_Type()
)
mwQosStatsSipSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsSipSessionCount.setStatus("current")
_MwQosStatsSccpSessionCount_Type = Counter64
_MwQosStatsSccpSessionCount_Object = MibScalar
mwQosStatsSccpSessionCount = _MwQosStatsSccpSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 4),
    _MwQosStatsSccpSessionCount_Type()
)
mwQosStatsSccpSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsSccpSessionCount.setStatus("current")
_MwQosStatsRejectedSessionCount_Type = Counter64
_MwQosStatsRejectedSessionCount_Object = MibScalar
mwQosStatsRejectedSessionCount = _MwQosStatsRejectedSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 5),
    _MwQosStatsRejectedSessionCount_Type()
)
mwQosStatsRejectedSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsRejectedSessionCount.setStatus("current")
_MwQosStatsRejectedH323SessionCount_Type = Counter64
_MwQosStatsRejectedH323SessionCount_Object = MibScalar
mwQosStatsRejectedH323SessionCount = _MwQosStatsRejectedH323SessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 6),
    _MwQosStatsRejectedH323SessionCount_Type()
)
mwQosStatsRejectedH323SessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsRejectedH323SessionCount.setStatus("current")
_MwQosStatsRejectedSipSessionCount_Type = Counter64
_MwQosStatsRejectedSipSessionCount_Object = MibScalar
mwQosStatsRejectedSipSessionCount = _MwQosStatsRejectedSipSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 7),
    _MwQosStatsRejectedSipSessionCount_Type()
)
mwQosStatsRejectedSipSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsRejectedSipSessionCount.setStatus("current")
_MwQosStatsRejectedSccpSessionCount_Type = Counter64
_MwQosStatsRejectedSccpSessionCount_Object = MibScalar
mwQosStatsRejectedSccpSessionCount = _MwQosStatsRejectedSccpSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 8),
    _MwQosStatsRejectedSccpSessionCount_Type()
)
mwQosStatsRejectedSccpSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsRejectedSccpSessionCount.setStatus("current")
_MwQosStatsPendingSessionCount_Type = Counter64
_MwQosStatsPendingSessionCount_Object = MibScalar
mwQosStatsPendingSessionCount = _MwQosStatsPendingSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 9),
    _MwQosStatsPendingSessionCount_Type()
)
mwQosStatsPendingSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsPendingSessionCount.setStatus("current")
_MwQosStatsH323PendingSessionCount_Type = Counter64
_MwQosStatsH323PendingSessionCount_Object = MibScalar
mwQosStatsH323PendingSessionCount = _MwQosStatsH323PendingSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 10),
    _MwQosStatsH323PendingSessionCount_Type()
)
mwQosStatsH323PendingSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsH323PendingSessionCount.setStatus("current")
_MwQosStatsSipPendingSessionCount_Type = Counter64
_MwQosStatsSipPendingSessionCount_Object = MibScalar
mwQosStatsSipPendingSessionCount = _MwQosStatsSipPendingSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 11),
    _MwQosStatsSipPendingSessionCount_Type()
)
mwQosStatsSipPendingSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsSipPendingSessionCount.setStatus("current")
_MwQosStatsSccpPendingSessionCount_Type = Counter64
_MwQosStatsSccpPendingSessionCount_Object = MibScalar
mwQosStatsSccpPendingSessionCount = _MwQosStatsSccpPendingSessionCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 12),
    _MwQosStatsSccpPendingSessionCount_Type()
)
mwQosStatsSccpPendingSessionCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsSccpPendingSessionCount.setStatus("current")
_MwQosStatsQosActiveFlowCount_Type = Counter64
_MwQosStatsQosActiveFlowCount_Object = MibScalar
mwQosStatsQosActiveFlowCount = _MwQosStatsQosActiveFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 13),
    _MwQosStatsQosActiveFlowCount_Type()
)
mwQosStatsQosActiveFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsQosActiveFlowCount.setStatus("current")
_MwQosStatsQosPendingFlowCount_Type = Counter64
_MwQosStatsQosPendingFlowCount_Object = MibScalar
mwQosStatsQosPendingFlowCount = _MwQosStatsQosPendingFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 4, 14),
    _MwQosStatsQosPendingFlowCount_Type()
)
mwQosStatsQosPendingFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwQosStatsQosPendingFlowCount.setStatus("current")
_MwStationStatsTable_Object = MibTable
mwStationStatsTable = _MwStationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6)
)
if mibBuilder.loadTexts:
    mwStationStatsTable.setStatus("current")
_MwStationStatsEntry_Object = MibTableRow
mwStationStatsEntry = _MwStationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1)
)
mwStationStatsEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwStationStatsTableIndex"),
)
if mibBuilder.loadTexts:
    mwStationStatsEntry.setStatus("current")
_MwStationStatsTableIndex_Type = Integer32
_MwStationStatsTableIndex_Object = MibTableColumn
mwStationStatsTableIndex = _MwStationStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 1),
    _MwStationStatsTableIndex_Type()
)
mwStationStatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwStationStatsTableIndex.setStatus("current")
_MwStationStatsMacAddress_Type = MacAddress
_MwStationStatsMacAddress_Object = MibTableColumn
mwStationStatsMacAddress = _MwStationStatsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 2),
    _MwStationStatsMacAddress_Type()
)
mwStationStatsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsMacAddress.setStatus("current")
_MwStationStatsDhcpRequestCount_Type = Counter64
_MwStationStatsDhcpRequestCount_Object = MibTableColumn
mwStationStatsDhcpRequestCount = _MwStationStatsDhcpRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 3),
    _MwStationStatsDhcpRequestCount_Type()
)
mwStationStatsDhcpRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsDhcpRequestCount.setStatus("current")
_MwStationStatsSipVideoBandwidth_Type = Counter64
_MwStationStatsSipVideoBandwidth_Object = MibTableColumn
mwStationStatsSipVideoBandwidth = _MwStationStatsSipVideoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 4),
    _MwStationStatsSipVideoBandwidth_Type()
)
mwStationStatsSipVideoBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSipVideoBandwidth.setStatus("current")
_MwStationStatsSipVideoFlowCount_Type = Counter64
_MwStationStatsSipVideoFlowCount_Object = MibTableColumn
mwStationStatsSipVideoFlowCount = _MwStationStatsSipVideoFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 5),
    _MwStationStatsSipVideoFlowCount_Type()
)
mwStationStatsSipVideoFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSipVideoFlowCount.setStatus("current")
_MwStationStatsSipAudioBandwidth_Type = Counter64
_MwStationStatsSipAudioBandwidth_Object = MibTableColumn
mwStationStatsSipAudioBandwidth = _MwStationStatsSipAudioBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 6),
    _MwStationStatsSipAudioBandwidth_Type()
)
mwStationStatsSipAudioBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSipAudioBandwidth.setStatus("current")
_MwStationStatsSipAudioFlowCount_Type = Counter64
_MwStationStatsSipAudioFlowCount_Object = MibTableColumn
mwStationStatsSipAudioFlowCount = _MwStationStatsSipAudioFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 7),
    _MwStationStatsSipAudioFlowCount_Type()
)
mwStationStatsSipAudioFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSipAudioFlowCount.setStatus("current")
_MwStationStatsAddressChangeCount_Type = Counter64
_MwStationStatsAddressChangeCount_Object = MibTableColumn
mwStationStatsAddressChangeCount = _MwStationStatsAddressChangeCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 8),
    _MwStationStatsAddressChangeCount_Type()
)
mwStationStatsAddressChangeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsAddressChangeCount.setStatus("current")
_MwStationStatsQosActiveFlowCount_Type = Counter64
_MwStationStatsQosActiveFlowCount_Object = MibTableColumn
mwStationStatsQosActiveFlowCount = _MwStationStatsQosActiveFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 9),
    _MwStationStatsQosActiveFlowCount_Type()
)
mwStationStatsQosActiveFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsQosActiveFlowCount.setStatus("current")
_MwStationStatsH323VideoBandwidth_Type = Counter64
_MwStationStatsH323VideoBandwidth_Object = MibTableColumn
mwStationStatsH323VideoBandwidth = _MwStationStatsH323VideoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 10),
    _MwStationStatsH323VideoBandwidth_Type()
)
mwStationStatsH323VideoBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsH323VideoBandwidth.setStatus("current")
_MwStationStatsH323VideoFlowCount_Type = Counter64
_MwStationStatsH323VideoFlowCount_Object = MibTableColumn
mwStationStatsH323VideoFlowCount = _MwStationStatsH323VideoFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 11),
    _MwStationStatsH323VideoFlowCount_Type()
)
mwStationStatsH323VideoFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsH323VideoFlowCount.setStatus("current")
_MwStationStatsH323AudioBandwidth_Type = Counter64
_MwStationStatsH323AudioBandwidth_Object = MibTableColumn
mwStationStatsH323AudioBandwidth = _MwStationStatsH323AudioBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 12),
    _MwStationStatsH323AudioBandwidth_Type()
)
mwStationStatsH323AudioBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsH323AudioBandwidth.setStatus("current")
_MwStationStatsH323AudioFlowCount_Type = Counter64
_MwStationStatsH323AudioFlowCount_Object = MibTableColumn
mwStationStatsH323AudioFlowCount = _MwStationStatsH323AudioFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 13),
    _MwStationStatsH323AudioFlowCount_Type()
)
mwStationStatsH323AudioFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsH323AudioFlowCount.setStatus("current")
_MwStationStatsSccpVideoBandwidth_Type = Unsigned32
_MwStationStatsSccpVideoBandwidth_Object = MibTableColumn
mwStationStatsSccpVideoBandwidth = _MwStationStatsSccpVideoBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 14),
    _MwStationStatsSccpVideoBandwidth_Type()
)
mwStationStatsSccpVideoBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSccpVideoBandwidth.setStatus("current")
_MwStationStatsSccpVideoFlowCount_Type = Unsigned32
_MwStationStatsSccpVideoFlowCount_Object = MibTableColumn
mwStationStatsSccpVideoFlowCount = _MwStationStatsSccpVideoFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 15),
    _MwStationStatsSccpVideoFlowCount_Type()
)
mwStationStatsSccpVideoFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSccpVideoFlowCount.setStatus("current")
_MwStationStatsSccpAudioBandwidth_Type = Unsigned32
_MwStationStatsSccpAudioBandwidth_Object = MibTableColumn
mwStationStatsSccpAudioBandwidth = _MwStationStatsSccpAudioBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 16),
    _MwStationStatsSccpAudioBandwidth_Type()
)
mwStationStatsSccpAudioBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSccpAudioBandwidth.setStatus("current")
_MwStationStatsSccpAudioFlowCount_Type = Unsigned32
_MwStationStatsSccpAudioFlowCount_Object = MibTableColumn
mwStationStatsSccpAudioFlowCount = _MwStationStatsSccpAudioFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 17),
    _MwStationStatsSccpAudioFlowCount_Type()
)
mwStationStatsSccpAudioFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSccpAudioFlowCount.setStatus("current")
_MwStationStatsQosPendingFlowCount_Type = Counter64
_MwStationStatsQosPendingFlowCount_Object = MibTableColumn
mwStationStatsQosPendingFlowCount = _MwStationStatsQosPendingFlowCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 18),
    _MwStationStatsQosPendingFlowCount_Type()
)
mwStationStatsQosPendingFlowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsQosPendingFlowCount.setStatus("current")
_MwStationStatsSipVideoRsvBandwidth_Type = Counter64
_MwStationStatsSipVideoRsvBandwidth_Object = MibTableColumn
mwStationStatsSipVideoRsvBandwidth = _MwStationStatsSipVideoRsvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 19),
    _MwStationStatsSipVideoRsvBandwidth_Type()
)
mwStationStatsSipVideoRsvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSipVideoRsvBandwidth.setStatus("current")
_MwStationStatsSipAudioRsvBandwidth_Type = Counter64
_MwStationStatsSipAudioRsvBandwidth_Object = MibTableColumn
mwStationStatsSipAudioRsvBandwidth = _MwStationStatsSipAudioRsvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 20),
    _MwStationStatsSipAudioRsvBandwidth_Type()
)
mwStationStatsSipAudioRsvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSipAudioRsvBandwidth.setStatus("current")
_MwStationStatsVoluntaryHandoffCount_Type = Counter64
_MwStationStatsVoluntaryHandoffCount_Object = MibTableColumn
mwStationStatsVoluntaryHandoffCount = _MwStationStatsVoluntaryHandoffCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 21),
    _MwStationStatsVoluntaryHandoffCount_Type()
)
mwStationStatsVoluntaryHandoffCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsVoluntaryHandoffCount.setStatus("current")
_MwStationStatsH323VideoRsvBandwidth_Type = Counter64
_MwStationStatsH323VideoRsvBandwidth_Object = MibTableColumn
mwStationStatsH323VideoRsvBandwidth = _MwStationStatsH323VideoRsvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 22),
    _MwStationStatsH323VideoRsvBandwidth_Type()
)
mwStationStatsH323VideoRsvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsH323VideoRsvBandwidth.setStatus("current")
_MwStationStatsH323AudioRsvBandwidth_Type = Counter64
_MwStationStatsH323AudioRsvBandwidth_Object = MibTableColumn
mwStationStatsH323AudioRsvBandwidth = _MwStationStatsH323AudioRsvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 23),
    _MwStationStatsH323AudioRsvBandwidth_Type()
)
mwStationStatsH323AudioRsvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsH323AudioRsvBandwidth.setStatus("current")
_MwStationStatsSccpVideoRsvBandwidth_Type = Unsigned32
_MwStationStatsSccpVideoRsvBandwidth_Object = MibTableColumn
mwStationStatsSccpVideoRsvBandwidth = _MwStationStatsSccpVideoRsvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 24),
    _MwStationStatsSccpVideoRsvBandwidth_Type()
)
mwStationStatsSccpVideoRsvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSccpVideoRsvBandwidth.setStatus("current")
_MwStationStatsSccpAudioRsvBandwidth_Type = Unsigned32
_MwStationStatsSccpAudioRsvBandwidth_Object = MibTableColumn
mwStationStatsSccpAudioRsvBandwidth = _MwStationStatsSccpAudioRsvBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 25),
    _MwStationStatsSccpAudioRsvBandwidth_Type()
)
mwStationStatsSccpAudioRsvBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsSccpAudioRsvBandwidth.setStatus("current")
_MwStationStatsInvoluntaryHandoffCount_Type = Counter64
_MwStationStatsInvoluntaryHandoffCount_Object = MibTableColumn
mwStationStatsInvoluntaryHandoffCount = _MwStationStatsInvoluntaryHandoffCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 6, 1, 26),
    _MwStationStatsInvoluntaryHandoffCount_Type()
)
mwStationStatsInvoluntaryHandoffCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwStationStatsInvoluntaryHandoffCount.setStatus("current")
_MwApStationStatsTable_Object = MibTable
mwApStationStatsTable = _MwApStationStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7)
)
if mibBuilder.loadTexts:
    mwApStationStatsTable.setStatus("current")
_MwApStationStatsEntry_Object = MibTableRow
mwApStationStatsEntry = _MwApStationStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1)
)
mwApStationStatsEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwApStationStatsTableIndex"),
)
if mibBuilder.loadTexts:
    mwApStationStatsEntry.setStatus("current")
_MwApStationStatsTableIndex_Type = Integer32
_MwApStationStatsTableIndex_Object = MibTableColumn
mwApStationStatsTableIndex = _MwApStationStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 1),
    _MwApStationStatsTableIndex_Type()
)
mwApStationStatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwApStationStatsTableIndex.setStatus("current")
_MwApStationStatsEssId_Type = DisplayString
_MwApStationStatsEssId_Object = MibTableColumn
mwApStationStatsEssId = _MwApStationStatsEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 2),
    _MwApStationStatsEssId_Type()
)
mwApStationStatsEssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsEssId.setStatus("current")
_MwApStationStatsBssId_Type = MacAddress
_MwApStationStatsBssId_Object = MibTableColumn
mwApStationStatsBssId = _MwApStationStatsBssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 3),
    _MwApStationStatsBssId_Type()
)
mwApStationStatsBssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsBssId.setStatus("current")
_MwApStationStatsApName_Type = DisplayString
_MwApStationStatsApName_Object = MibTableColumn
mwApStationStatsApName = _MwApStationStatsApName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 4),
    _MwApStationStatsApName_Type()
)
mwApStationStatsApName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsApName.setStatus("current")
_MwApStationStatsIfIndex_Type = Integer32
_MwApStationStatsIfIndex_Object = MibTableColumn
mwApStationStatsIfIndex = _MwApStationStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 5),
    _MwApStationStatsIfIndex_Type()
)
mwApStationStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsIfIndex.setStatus("current")
_MwApStationStatsWepErrors_Type = Counter64
_MwApStationStatsWepErrors_Object = MibTableColumn
mwApStationStatsWepErrors = _MwApStationStatsWepErrors_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 6),
    _MwApStationStatsWepErrors_Type()
)
mwApStationStatsWepErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsWepErrors.setStatus("current")
_MwApStationStatsRxDataRate_Type = Counter64
_MwApStationStatsRxDataRate_Object = MibTableColumn
mwApStationStatsRxDataRate = _MwApStationStatsRxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 7),
    _MwApStationStatsRxDataRate_Type()
)
mwApStationStatsRxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsRxDataRate.setStatus("current")
_MwApStationStatsTxDataRate_Type = Counter64
_MwApStationStatsTxDataRate_Object = MibTableColumn
mwApStationStatsTxDataRate = _MwApStationStatsTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 8),
    _MwApStationStatsTxDataRate_Type()
)
mwApStationStatsTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsTxDataRate.setStatus("current")
_MwApStationStatsNmsApNodeId_Type = Integer32
_MwApStationStatsNmsApNodeId_Object = MibTableColumn
mwApStationStatsNmsApNodeId = _MwApStationStatsNmsApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 9),
    _MwApStationStatsNmsApNodeId_Type()
)
mwApStationStatsNmsApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsNmsApNodeId.setStatus("current")
_MwApStationStatsRxByteCount_Type = Counter64
_MwApStationStatsRxByteCount_Object = MibTableColumn
mwApStationStatsRxByteCount = _MwApStationStatsRxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 10),
    _MwApStationStatsRxByteCount_Type()
)
mwApStationStatsRxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsRxByteCount.setStatus("current")
_MwApStationStatsTxByteCount_Type = Counter64
_MwApStationStatsTxByteCount_Object = MibTableColumn
mwApStationStatsTxByteCount = _MwApStationStatsTxByteCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 11),
    _MwApStationStatsTxByteCount_Type()
)
mwApStationStatsTxByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsTxByteCount.setStatus("current")
_MwApStationStatsRxPacketCount_Type = Counter64
_MwApStationStatsRxPacketCount_Object = MibTableColumn
mwApStationStatsRxPacketCount = _MwApStationStatsRxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 12),
    _MwApStationStatsRxPacketCount_Type()
)
mwApStationStatsRxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsRxPacketCount.setStatus("current")
_MwApStationStatsTxPacketCount_Type = Counter64
_MwApStationStatsTxPacketCount_Object = MibTableColumn
mwApStationStatsTxPacketCount = _MwApStationStatsTxPacketCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 13),
    _MwApStationStatsTxPacketCount_Type()
)
mwApStationStatsTxPacketCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsTxPacketCount.setStatus("current")
_MwApStationStatsTxAckMissCount_Type = Counter64
_MwApStationStatsTxAckMissCount_Object = MibTableColumn
mwApStationStatsTxAckMissCount = _MwApStationStatsTxAckMissCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 14),
    _MwApStationStatsTxAckMissCount_Type()
)
mwApStationStatsTxAckMissCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsTxAckMissCount.setStatus("current")
_MwApStationStatsDhcpErrorCount_Type = Counter64
_MwApStationStatsDhcpErrorCount_Object = MibTableColumn
mwApStationStatsDhcpErrorCount = _MwApStationStatsDhcpErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 15),
    _MwApStationStatsDhcpErrorCount_Type()
)
mwApStationStatsDhcpErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsDhcpErrorCount.setStatus("current")
_MwApStationStatsRxFcsErrorCount_Type = Counter64
_MwApStationStatsRxFcsErrorCount_Object = MibTableColumn
mwApStationStatsRxFcsErrorCount = _MwApStationStatsRxFcsErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 16),
    _MwApStationStatsRxFcsErrorCount_Type()
)
mwApStationStatsRxFcsErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsRxFcsErrorCount.setStatus("current")
_MwApStationStatsStationIPAddress_Type = IpAddress
_MwApStationStatsStationIPAddress_Object = MibTableColumn
mwApStationStatsStationIPAddress = _MwApStationStatsStationIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 17),
    _MwApStationStatsStationIPAddress_Type()
)
mwApStationStatsStationIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsStationIPAddress.setStatus("current")
_MwApStationStatsRxDuplicateCount_Type = Counter64
_MwApStationStatsRxDuplicateCount_Object = MibTableColumn
mwApStationStatsRxDuplicateCount = _MwApStationStatsRxDuplicateCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 18),
    _MwApStationStatsRxDuplicateCount_Type()
)
mwApStationStatsRxDuplicateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsRxDuplicateCount.setStatus("current")
_MwApStationStatsDhcpRequestCount_Type = Counter64
_MwApStationStatsDhcpRequestCount_Object = MibTableColumn
mwApStationStatsDhcpRequestCount = _MwApStationStatsDhcpRequestCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 19),
    _MwApStationStatsDhcpRequestCount_Type()
)
mwApStationStatsDhcpRequestCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsDhcpRequestCount.setStatus("current")
_MwApStationStatsStationMacAddress_Type = MacAddress
_MwApStationStatsStationMacAddress_Object = MibTableColumn
mwApStationStatsStationMacAddress = _MwApStationStatsStationMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 20),
    _MwApStationStatsStationMacAddress_Type()
)
mwApStationStatsStationMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsStationMacAddress.setStatus("current")
_MwApStationStatsChannelUtilization_Type = Counter64
_MwApStationStatsChannelUtilization_Object = MibTableColumn
mwApStationStatsChannelUtilization = _MwApStationStatsChannelUtilization_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 21),
    _MwApStationStatsChannelUtilization_Type()
)
mwApStationStatsChannelUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsChannelUtilization.setStatus("current")
_MwApStationStatsRxRetriedFrameCount_Type = Counter64
_MwApStationStatsRxRetriedFrameCount_Object = MibTableColumn
mwApStationStatsRxRetriedFrameCount = _MwApStationStatsRxRetriedFrameCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 22),
    _MwApStationStatsRxRetriedFrameCount_Type()
)
mwApStationStatsRxRetriedFrameCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsRxRetriedFrameCount.setStatus("current")
_MwApStationStatsRxAverageAggrLength_Type = Counter64
_MwApStationStatsRxAverageAggrLength_Object = MibTableColumn
mwApStationStatsRxAverageAggrLength = _MwApStationStatsRxAverageAggrLength_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 23),
    _MwApStationStatsRxAverageAggrLength_Type()
)
mwApStationStatsRxAverageAggrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsRxAverageAggrLength.setStatus("current")
_MwApStationStatsTxAverageAggrLength_Type = Counter64
_MwApStationStatsTxAverageAggrLength_Object = MibTableColumn
mwApStationStatsTxAverageAggrLength = _MwApStationStatsTxAverageAggrLength_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 24),
    _MwApStationStatsTxAverageAggrLength_Type()
)
mwApStationStatsTxAverageAggrLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsTxAverageAggrLength.setStatus("current")
_MwApStationStatsTotalPowerSaveTransitions_Type = Counter64
_MwApStationStatsTotalPowerSaveTransitions_Object = MibTableColumn
mwApStationStatsTotalPowerSaveTransitions = _MwApStationStatsTotalPowerSaveTransitions_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 25),
    _MwApStationStatsTotalPowerSaveTransitions_Type()
)
mwApStationStatsTotalPowerSaveTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsTotalPowerSaveTransitions.setStatus("current")
_MwApStationStatsStationQueueOverflow_Type = Counter64
_MwApStationStatsStationQueueOverflow_Object = MibTableColumn
mwApStationStatsStationQueueOverflow = _MwApStationStatsStationQueueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 26),
    _MwApStationStatsStationQueueOverflow_Type()
)
mwApStationStatsStationQueueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsStationQueueOverflow.setStatus("current")
_MwApStationStatsPowerSaveQueueOverflow_Type = Counter64
_MwApStationStatsPowerSaveQueueOverflow_Object = MibTableColumn
mwApStationStatsPowerSaveQueueOverflow = _MwApStationStatsPowerSaveQueueOverflow_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 27),
    _MwApStationStatsPowerSaveQueueOverflow_Type()
)
mwApStationStatsPowerSaveQueueOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsPowerSaveQueueOverflow.setStatus("current")
_MwApStationStatsPSPollFramesRxCount_Type = Counter64
_MwApStationStatsPSPollFramesRxCount_Object = MibTableColumn
mwApStationStatsPSPollFramesRxCount = _MwApStationStatsPSPollFramesRxCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 28),
    _MwApStationStatsPSPollFramesRxCount_Type()
)
mwApStationStatsPSPollFramesRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsPSPollFramesRxCount.setStatus("current")
_MwApStationStatsSWEncryptionFramesCount_Type = Counter64
_MwApStationStatsSWEncryptionFramesCount_Object = MibTableColumn
mwApStationStatsSWEncryptionFramesCount = _MwApStationStatsSWEncryptionFramesCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 29),
    _MwApStationStatsSWEncryptionFramesCount_Type()
)
mwApStationStatsSWEncryptionFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsSWEncryptionFramesCount.setStatus("current")
_MwApStationStatsSWDecryptionFramesCount_Type = Counter64
_MwApStationStatsSWDecryptionFramesCount_Object = MibTableColumn
mwApStationStatsSWDecryptionFramesCount = _MwApStationStatsSWDecryptionFramesCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 30),
    _MwApStationStatsSWDecryptionFramesCount_Type()
)
mwApStationStatsSWDecryptionFramesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsSWDecryptionFramesCount.setStatus("current")
_MwApStationStatsLRUSwapCounter_Type = Counter64
_MwApStationStatsLRUSwapCounter_Object = MibTableColumn
mwApStationStatsLRUSwapCounter = _MwApStationStatsLRUSwapCounter_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 31),
    _MwApStationStatsLRUSwapCounter_Type()
)
mwApStationStatsLRUSwapCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsLRUSwapCounter.setStatus("current")
_MwApStationStatsTxFailedHwRetryExceeded_Type = Counter64
_MwApStationStatsTxFailedHwRetryExceeded_Object = MibTableColumn
mwApStationStatsTxFailedHwRetryExceeded = _MwApStationStatsTxFailedHwRetryExceeded_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 7, 1, 32),
    _MwApStationStatsTxFailedHwRetryExceeded_Type()
)
mwApStationStatsTxFailedHwRetryExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwApStationStatsTxFailedHwRetryExceeded.setStatus("current")
_MwCacApStatsTable_Object = MibTable
mwCacApStatsTable = _MwCacApStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 8)
)
if mibBuilder.loadTexts:
    mwCacApStatsTable.setStatus("current")
_MwCacApStatsEntry_Object = MibTableRow
mwCacApStatsEntry = _MwCacApStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 8, 1)
)
mwCacApStatsEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwCacApStatsTableIndex"),
)
if mibBuilder.loadTexts:
    mwCacApStatsEntry.setStatus("current")
_MwCacApStatsTableIndex_Type = Integer32
_MwCacApStatsTableIndex_Object = MibTableColumn
mwCacApStatsTableIndex = _MwCacApStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 8, 1, 1),
    _MwCacApStatsTableIndex_Type()
)
mwCacApStatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwCacApStatsTableIndex.setStatus("current")
_MwCacApStatsNmsApNodeId_Type = Integer32
_MwCacApStatsNmsApNodeId_Object = MibTableColumn
mwCacApStatsNmsApNodeId = _MwCacApStatsNmsApNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 8, 1, 2),
    _MwCacApStatsNmsApNodeId_Type()
)
mwCacApStatsNmsApNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwCacApStatsNmsApNodeId.setStatus("current")
_MwCacApStatsCurrentCalls_Type = Unsigned32
_MwCacApStatsCurrentCalls_Object = MibTableColumn
mwCacApStatsCurrentCalls = _MwCacApStatsCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 8, 1, 3),
    _MwCacApStatsCurrentCalls_Type()
)
mwCacApStatsCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwCacApStatsCurrentCalls.setStatus("current")
_MwCacApStatsRejectedCalls_Type = Unsigned32
_MwCacApStatsRejectedCalls_Object = MibTableColumn
mwCacApStatsRejectedCalls = _MwCacApStatsRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 8, 1, 4),
    _MwCacApStatsRejectedCalls_Type()
)
mwCacApStatsRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwCacApStatsRejectedCalls.setStatus("current")
_MwCacBssStatsTable_Object = MibTable
mwCacBssStatsTable = _MwCacBssStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 9)
)
if mibBuilder.loadTexts:
    mwCacBssStatsTable.setStatus("current")
_MwCacBssStatsEntry_Object = MibTableRow
mwCacBssStatsEntry = _MwCacBssStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 9, 1)
)
mwCacBssStatsEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwCacBssStatsTableIndex"),
)
if mibBuilder.loadTexts:
    mwCacBssStatsEntry.setStatus("current")
_MwCacBssStatsTableIndex_Type = Integer32
_MwCacBssStatsTableIndex_Object = MibTableColumn
mwCacBssStatsTableIndex = _MwCacBssStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 9, 1, 1),
    _MwCacBssStatsTableIndex_Type()
)
mwCacBssStatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwCacBssStatsTableIndex.setStatus("current")
_MwCacBssStatsBssId_Type = MacAddress
_MwCacBssStatsBssId_Object = MibTableColumn
mwCacBssStatsBssId = _MwCacBssStatsBssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 9, 1, 2),
    _MwCacBssStatsBssId_Type()
)
mwCacBssStatsBssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwCacBssStatsBssId.setStatus("current")
_MwCacBssStatsCurrentCalls_Type = Unsigned32
_MwCacBssStatsCurrentCalls_Object = MibTableColumn
mwCacBssStatsCurrentCalls = _MwCacBssStatsCurrentCalls_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 9, 1, 3),
    _MwCacBssStatsCurrentCalls_Type()
)
mwCacBssStatsCurrentCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwCacBssStatsCurrentCalls.setStatus("current")
_MwCacBssStatsRejectedCalls_Type = Unsigned32
_MwCacBssStatsRejectedCalls_Object = MibTableColumn
mwCacBssStatsRejectedCalls = _MwCacBssStatsRejectedCalls_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 9, 1, 4),
    _MwCacBssStatsRejectedCalls_Type()
)
mwCacBssStatsRejectedCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwCacBssStatsRejectedCalls.setStatus("current")
_MwRf6DiagStatsTable_Object = MibTable
mwRf6DiagStatsTable = _MwRf6DiagStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10)
)
if mibBuilder.loadTexts:
    mwRf6DiagStatsTable.setStatus("current")
_MwRf6DiagStatsEntry_Object = MibTableRow
mwRf6DiagStatsEntry = _MwRf6DiagStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1)
)
mwRf6DiagStatsEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwRf6DiagStatsTableIndex"),
)
if mibBuilder.loadTexts:
    mwRf6DiagStatsEntry.setStatus("current")
_MwRf6DiagStatsTableIndex_Type = Integer32
_MwRf6DiagStatsTableIndex_Object = MibTableColumn
mwRf6DiagStatsTableIndex = _MwRf6DiagStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 1),
    _MwRf6DiagStatsTableIndex_Type()
)
mwRf6DiagStatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwRf6DiagStatsTableIndex.setStatus("current")
_MwRf6DiagStatsNodeId_Type = Unsigned32
_MwRf6DiagStatsNodeId_Object = MibTableColumn
mwRf6DiagStatsNodeId = _MwRf6DiagStatsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 2),
    _MwRf6DiagStatsNodeId_Type()
)
mwRf6DiagStatsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsNodeId.setStatus("current")
_MwRf6DiagStatsIfIndex_Type = Integer32
_MwRf6DiagStatsIfIndex_Object = MibTableColumn
mwRf6DiagStatsIfIndex = _MwRf6DiagStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 3),
    _MwRf6DiagStatsIfIndex_Type()
)
mwRf6DiagStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsIfIndex.setStatus("current")
_MwRf6DiagStatsNodeName_Type = DisplayString
_MwRf6DiagStatsNodeName_Object = MibTableColumn
mwRf6DiagStatsNodeName = _MwRf6DiagStatsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 4),
    _MwRf6DiagStatsNodeName_Type()
)
mwRf6DiagStatsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsNodeName.setStatus("current")
_MwRf6DiagStatsFatalHwErrorINTs_Type = Counter64
_MwRf6DiagStatsFatalHwErrorINTs_Object = MibTableColumn
mwRf6DiagStatsFatalHwErrorINTs = _MwRf6DiagStatsFatalHwErrorINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 5),
    _MwRf6DiagStatsFatalHwErrorINTs_Type()
)
mwRf6DiagStatsFatalHwErrorINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsFatalHwErrorINTs.setStatus("current")
_MwRf6DiagStatsBeaconMissCount_Type = Counter64
_MwRf6DiagStatsBeaconMissCount_Object = MibTableColumn
mwRf6DiagStatsBeaconMissCount = _MwRf6DiagStatsBeaconMissCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 6),
    _MwRf6DiagStatsBeaconMissCount_Type()
)
mwRf6DiagStatsBeaconMissCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsBeaconMissCount.setStatus("current")
_MwRf6DiagStatsBeaconBufferNullCount_Type = Counter64
_MwRf6DiagStatsBeaconBufferNullCount_Object = MibTableColumn
mwRf6DiagStatsBeaconBufferNullCount = _MwRf6DiagStatsBeaconBufferNullCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 7),
    _MwRf6DiagStatsBeaconBufferNullCount_Type()
)
mwRf6DiagStatsBeaconBufferNullCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsBeaconBufferNullCount.setStatus("current")
_MwRf6DiagStatsNoSkBufferForBeacon_Type = Counter64
_MwRf6DiagStatsNoSkBufferForBeacon_Object = MibTableColumn
mwRf6DiagStatsNoSkBufferForBeacon = _MwRf6DiagStatsNoSkBufferForBeacon_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 8),
    _MwRf6DiagStatsNoSkBufferForBeacon_Type()
)
mwRf6DiagStatsNoSkBufferForBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsNoSkBufferForBeacon.setStatus("current")
_MwRf6DiagStatsTxUnderrunINTs_Type = Counter64
_MwRf6DiagStatsTxUnderrunINTs_Object = MibTableColumn
mwRf6DiagStatsTxUnderrunINTs = _MwRf6DiagStatsTxUnderrunINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 9),
    _MwRf6DiagStatsTxUnderrunINTs_Type()
)
mwRf6DiagStatsTxUnderrunINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsTxUnderrunINTs.setStatus("current")
_MwRf6DiagStatsTxTimeoutINTs_Type = Counter64
_MwRf6DiagStatsTxTimeoutINTs_Object = MibTableColumn
mwRf6DiagStatsTxTimeoutINTs = _MwRf6DiagStatsTxTimeoutINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 10),
    _MwRf6DiagStatsTxTimeoutINTs_Type()
)
mwRf6DiagStatsTxTimeoutINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsTxTimeoutINTs.setStatus("current")
_MwRf6DiagStatsTxFailedByNoTxBuffer_Type = Counter64
_MwRf6DiagStatsTxFailedByNoTxBuffer_Object = MibTableColumn
mwRf6DiagStatsTxFailedByNoTxBuffer = _MwRf6DiagStatsTxFailedByNoTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 11),
    _MwRf6DiagStatsTxFailedByNoTxBuffer_Type()
)
mwRf6DiagStatsTxFailedByNoTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsTxFailedByNoTxBuffer.setStatus("current")
_MwRf6DiagStatsTxFailedByFIFOUnderrun_Type = Counter64
_MwRf6DiagStatsTxFailedByFIFOUnderrun_Object = MibTableColumn
mwRf6DiagStatsTxFailedByFIFOUnderrun = _MwRf6DiagStatsTxFailedByFIFOUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 12),
    _MwRf6DiagStatsTxFailedByFIFOUnderrun_Type()
)
mwRf6DiagStatsTxFailedByFIFOUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsTxFailedByFIFOUnderrun.setStatus("current")
_MwRf6DiagStatsTxAggrDescriptorConfigError_Type = Counter64
_MwRf6DiagStatsTxAggrDescriptorConfigError_Object = MibTableColumn
mwRf6DiagStatsTxAggrDescriptorConfigError = _MwRf6DiagStatsTxAggrDescriptorConfigError_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 13),
    _MwRf6DiagStatsTxAggrDescriptorConfigError_Type()
)
mwRf6DiagStatsTxAggrDescriptorConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsTxAggrDescriptorConfigError.setStatus("current")
_MwRf6DiagStatsTxAggrDataUnderrun_Type = Counter64
_MwRf6DiagStatsTxAggrDataUnderrun_Object = MibTableColumn
mwRf6DiagStatsTxAggrDataUnderrun = _MwRf6DiagStatsTxAggrDataUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 14),
    _MwRf6DiagStatsTxAggrDataUnderrun_Type()
)
mwRf6DiagStatsTxAggrDataUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsTxAggrDataUnderrun.setStatus("current")
_MwRf6DiagStatsTxAggrDelimiterUnderrun_Type = Counter64
_MwRf6DiagStatsTxAggrDelimiterUnderrun_Object = MibTableColumn
mwRf6DiagStatsTxAggrDelimiterUnderrun = _MwRf6DiagStatsTxAggrDelimiterUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 15),
    _MwRf6DiagStatsTxAggrDelimiterUnderrun_Type()
)
mwRf6DiagStatsTxAggrDelimiterUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsTxAggrDelimiterUnderrun.setStatus("current")
_MwRf6DiagStatsTotalTidResetCnt_Type = Counter64
_MwRf6DiagStatsTotalTidResetCnt_Object = MibTableColumn
mwRf6DiagStatsTotalTidResetCnt = _MwRf6DiagStatsTotalTidResetCnt_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 16),
    _MwRf6DiagStatsTotalTidResetCnt_Type()
)
mwRf6DiagStatsTotalTidResetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsTotalTidResetCnt.setStatus("current")
_MwRf6DiagStatsCarrierSenseTimeoutINTs_Type = Counter64
_MwRf6DiagStatsCarrierSenseTimeoutINTs_Object = MibTableColumn
mwRf6DiagStatsCarrierSenseTimeoutINTs = _MwRf6DiagStatsCarrierSenseTimeoutINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 17),
    _MwRf6DiagStatsCarrierSenseTimeoutINTs_Type()
)
mwRf6DiagStatsCarrierSenseTimeoutINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsCarrierSenseTimeoutINTs.setStatus("current")
_MwRf6DiagStatsIsSlamTxNoAckAddr_Type = Counter64
_MwRf6DiagStatsIsSlamTxNoAckAddr_Object = MibTableColumn
mwRf6DiagStatsIsSlamTxNoAckAddr = _MwRf6DiagStatsIsSlamTxNoAckAddr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 18),
    _MwRf6DiagStatsIsSlamTxNoAckAddr_Type()
)
mwRf6DiagStatsIsSlamTxNoAckAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsIsSlamTxNoAckAddr.setStatus("current")
_MwRf6DiagStatsRxOverrunINTs_Type = Counter64
_MwRf6DiagStatsRxOverrunINTs_Object = MibTableColumn
mwRf6DiagStatsRxOverrunINTs = _MwRf6DiagStatsRxOverrunINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 19),
    _MwRf6DiagStatsRxOverrunINTs_Type()
)
mwRf6DiagStatsRxOverrunINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRxOverrunINTs.setStatus("current")
_MwRf6DiagStatsRxEolINTs_Type = Counter64
_MwRf6DiagStatsRxEolINTs_Object = MibTableColumn
mwRf6DiagStatsRxEolINTs = _MwRf6DiagStatsRxEolINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 20),
    _MwRf6DiagStatsRxEolINTs_Type()
)
mwRf6DiagStatsRxEolINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRxEolINTs.setStatus("current")
_MwRf6DiagStatsRxPacketsBadVersion_Type = Counter64
_MwRf6DiagStatsRxPacketsBadVersion_Object = MibTableColumn
mwRf6DiagStatsRxPacketsBadVersion = _MwRf6DiagStatsRxPacketsBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 21),
    _MwRf6DiagStatsRxPacketsBadVersion_Type()
)
mwRf6DiagStatsRxPacketsBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRxPacketsBadVersion.setStatus("current")
_MwRf6DiagStatsRadioResetBeaconStuck_Type = Counter64
_MwRf6DiagStatsRadioResetBeaconStuck_Object = MibTableColumn
mwRf6DiagStatsRadioResetBeaconStuck = _MwRf6DiagStatsRadioResetBeaconStuck_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 22),
    _MwRf6DiagStatsRadioResetBeaconStuck_Type()
)
mwRf6DiagStatsRadioResetBeaconStuck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRadioResetBeaconStuck.setStatus("current")
_MwRf6DiagStatsRadioResetTPScale_Type = Counter64
_MwRf6DiagStatsRadioResetTPScale_Object = MibTableColumn
mwRf6DiagStatsRadioResetTPScale = _MwRf6DiagStatsRadioResetTPScale_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 23),
    _MwRf6DiagStatsRadioResetTPScale_Type()
)
mwRf6DiagStatsRadioResetTPScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRadioResetTPScale.setStatus("current")
_MwRf6DiagStatsRadioResetFatalTasklet_Type = Counter64
_MwRf6DiagStatsRadioResetFatalTasklet_Object = MibTableColumn
mwRf6DiagStatsRadioResetFatalTasklet = _MwRf6DiagStatsRadioResetFatalTasklet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 24),
    _MwRf6DiagStatsRadioResetFatalTasklet_Type()
)
mwRf6DiagStatsRadioResetFatalTasklet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRadioResetFatalTasklet.setStatus("current")
_MwRf6DiagStatsRadioResetRxornTasklet_Type = Counter64
_MwRf6DiagStatsRadioResetRxornTasklet_Object = MibTableColumn
mwRf6DiagStatsRadioResetRxornTasklet = _MwRf6DiagStatsRadioResetRxornTasklet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 25),
    _MwRf6DiagStatsRadioResetRxornTasklet_Type()
)
mwRf6DiagStatsRadioResetRxornTasklet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRadioResetRxornTasklet.setStatus("current")
_MwRf6DiagStatsRadioResetCalibrate_Type = Counter64
_MwRf6DiagStatsRadioResetCalibrate_Object = MibTableColumn
mwRf6DiagStatsRadioResetCalibrate = _MwRf6DiagStatsRadioResetCalibrate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 26),
    _MwRf6DiagStatsRadioResetCalibrate_Type()
)
mwRf6DiagStatsRadioResetCalibrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRadioResetCalibrate.setStatus("current")
_MwRf6DiagStatsRadioResetTxAntennaSwitch_Type = Counter64
_MwRf6DiagStatsRadioResetTxAntennaSwitch_Object = MibTableColumn
mwRf6DiagStatsRadioResetTxAntennaSwitch = _MwRf6DiagStatsRadioResetTxAntennaSwitch_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 27),
    _MwRf6DiagStatsRadioResetTxAntennaSwitch_Type()
)
mwRf6DiagStatsRadioResetTxAntennaSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRadioResetTxAntennaSwitch.setStatus("current")
_MwRf6DiagStatsRadioResetRxChain_Type = Counter64
_MwRf6DiagStatsRadioResetRxChain_Object = MibTableColumn
mwRf6DiagStatsRadioResetRxChain = _MwRf6DiagStatsRadioResetRxChain_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 28),
    _MwRf6DiagStatsRadioResetRxChain_Type()
)
mwRf6DiagStatsRadioResetRxChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRadioResetRxChain.setStatus("current")
_MwRf6DiagStatsRadioResetNoTxFrames_Type = Counter64
_MwRf6DiagStatsRadioResetNoTxFrames_Object = MibTableColumn
mwRf6DiagStatsRadioResetNoTxFrames = _MwRf6DiagStatsRadioResetNoTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 29),
    _MwRf6DiagStatsRadioResetNoTxFrames_Type()
)
mwRf6DiagStatsRadioResetNoTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRadioResetNoTxFrames.setStatus("current")
_MwRf6DiagStatsTotalRadioResetCnt_Type = Counter64
_MwRf6DiagStatsTotalRadioResetCnt_Object = MibTableColumn
mwRf6DiagStatsTotalRadioResetCnt = _MwRf6DiagStatsTotalRadioResetCnt_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 30),
    _MwRf6DiagStatsTotalRadioResetCnt_Type()
)
mwRf6DiagStatsTotalRadioResetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwRf6DiagStatsTotalRadioResetCnt.setStatus("current")
_MwRf6DiagStatsRowStatus_Type = RowStatus
_MwRf6DiagStatsRowStatus_Object = MibTableColumn
mwRf6DiagStatsRowStatus = _MwRf6DiagStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 10, 1, 31),
    _MwRf6DiagStatsRowStatus_Type()
)
mwRf6DiagStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwRf6DiagStatsRowStatus.setStatus("current")
_MwAp1000DiagStatsTable_Object = MibTable
mwAp1000DiagStatsTable = _MwAp1000DiagStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11)
)
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTable.setStatus("current")
_MwAp1000DiagStatsEntry_Object = MibTableRow
mwAp1000DiagStatsEntry = _MwAp1000DiagStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1)
)
mwAp1000DiagStatsEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwAp1000DiagStatsTableIndex"),
)
if mibBuilder.loadTexts:
    mwAp1000DiagStatsEntry.setStatus("current")
_MwAp1000DiagStatsTableIndex_Type = Integer32
_MwAp1000DiagStatsTableIndex_Object = MibTableColumn
mwAp1000DiagStatsTableIndex = _MwAp1000DiagStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 1),
    _MwAp1000DiagStatsTableIndex_Type()
)
mwAp1000DiagStatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTableIndex.setStatus("current")
_MwAp1000DiagStatsNodeId_Type = Unsigned32
_MwAp1000DiagStatsNodeId_Object = MibTableColumn
mwAp1000DiagStatsNodeId = _MwAp1000DiagStatsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 2),
    _MwAp1000DiagStatsNodeId_Type()
)
mwAp1000DiagStatsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsNodeId.setStatus("current")
_MwAp1000DiagStatsIfIndex_Type = Integer32
_MwAp1000DiagStatsIfIndex_Object = MibTableColumn
mwAp1000DiagStatsIfIndex = _MwAp1000DiagStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 3),
    _MwAp1000DiagStatsIfIndex_Type()
)
mwAp1000DiagStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsIfIndex.setStatus("current")
_MwAp1000DiagStatsNodeName_Type = DisplayString
_MwAp1000DiagStatsNodeName_Object = MibTableColumn
mwAp1000DiagStatsNodeName = _MwAp1000DiagStatsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 4),
    _MwAp1000DiagStatsNodeName_Type()
)
mwAp1000DiagStatsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsNodeName.setStatus("current")
_MwAp1000DiagStatsFatalHwErrorINTs_Type = Counter64
_MwAp1000DiagStatsFatalHwErrorINTs_Object = MibTableColumn
mwAp1000DiagStatsFatalHwErrorINTs = _MwAp1000DiagStatsFatalHwErrorINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 5),
    _MwAp1000DiagStatsFatalHwErrorINTs_Type()
)
mwAp1000DiagStatsFatalHwErrorINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsFatalHwErrorINTs.setStatus("current")
_MwAp1000DiagStatsBeaconMissCount_Type = Counter64
_MwAp1000DiagStatsBeaconMissCount_Object = MibTableColumn
mwAp1000DiagStatsBeaconMissCount = _MwAp1000DiagStatsBeaconMissCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 6),
    _MwAp1000DiagStatsBeaconMissCount_Type()
)
mwAp1000DiagStatsBeaconMissCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsBeaconMissCount.setStatus("current")
_MwAp1000DiagStatsTxUnderrunINTs_Type = Counter64
_MwAp1000DiagStatsTxUnderrunINTs_Object = MibTableColumn
mwAp1000DiagStatsTxUnderrunINTs = _MwAp1000DiagStatsTxUnderrunINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 7),
    _MwAp1000DiagStatsTxUnderrunINTs_Type()
)
mwAp1000DiagStatsTxUnderrunINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxUnderrunINTs.setStatus("current")
_MwAp1000DiagStatsTxTimeoutINTs_Type = Counter64
_MwAp1000DiagStatsTxTimeoutINTs_Object = MibTableColumn
mwAp1000DiagStatsTxTimeoutINTs = _MwAp1000DiagStatsTxTimeoutINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 8),
    _MwAp1000DiagStatsTxTimeoutINTs_Type()
)
mwAp1000DiagStatsTxTimeoutINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxTimeoutINTs.setStatus("current")
_MwAp1000DiagStatsTxFailedByNoTxBuffer_Type = Counter64
_MwAp1000DiagStatsTxFailedByNoTxBuffer_Object = MibTableColumn
mwAp1000DiagStatsTxFailedByNoTxBuffer = _MwAp1000DiagStatsTxFailedByNoTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 9),
    _MwAp1000DiagStatsTxFailedByNoTxBuffer_Type()
)
mwAp1000DiagStatsTxFailedByNoTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxFailedByNoTxBuffer.setStatus("current")
_MwAp1000DiagStatsTxFailedByFIFOUnderrun_Type = Counter64
_MwAp1000DiagStatsTxFailedByFIFOUnderrun_Object = MibTableColumn
mwAp1000DiagStatsTxFailedByFIFOUnderrun = _MwAp1000DiagStatsTxFailedByFIFOUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 10),
    _MwAp1000DiagStatsTxFailedByFIFOUnderrun_Type()
)
mwAp1000DiagStatsTxFailedByFIFOUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxFailedByFIFOUnderrun.setStatus("current")
_MwAp1000DiagStatsTotalTidResetCnt_Type = Counter64
_MwAp1000DiagStatsTotalTidResetCnt_Object = MibTableColumn
mwAp1000DiagStatsTotalTidResetCnt = _MwAp1000DiagStatsTotalTidResetCnt_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 11),
    _MwAp1000DiagStatsTotalTidResetCnt_Type()
)
mwAp1000DiagStatsTotalTidResetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTotalTidResetCnt.setStatus("current")
_MwAp1000DiagStatsRxOverrunINTs_Type = Counter64
_MwAp1000DiagStatsRxOverrunINTs_Object = MibTableColumn
mwAp1000DiagStatsRxOverrunINTs = _MwAp1000DiagStatsRxOverrunINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 12),
    _MwAp1000DiagStatsRxOverrunINTs_Type()
)
mwAp1000DiagStatsRxOverrunINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsRxOverrunINTs.setStatus("current")
_MwAp1000DiagStatsRxEolINTs_Type = Counter64
_MwAp1000DiagStatsRxEolINTs_Object = MibTableColumn
mwAp1000DiagStatsRxEolINTs = _MwAp1000DiagStatsRxEolINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 13),
    _MwAp1000DiagStatsRxEolINTs_Type()
)
mwAp1000DiagStatsRxEolINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsRxEolINTs.setStatus("current")
_MwAp1000DiagStatsRxPacketsBadVersion_Type = Counter64
_MwAp1000DiagStatsRxPacketsBadVersion_Object = MibTableColumn
mwAp1000DiagStatsRxPacketsBadVersion = _MwAp1000DiagStatsRxPacketsBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 14),
    _MwAp1000DiagStatsRxPacketsBadVersion_Type()
)
mwAp1000DiagStatsRxPacketsBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsRxPacketsBadVersion.setStatus("current")
_MwAp1000DiagStatsTotalRadioResetCnt_Type = Counter64
_MwAp1000DiagStatsTotalRadioResetCnt_Object = MibTableColumn
mwAp1000DiagStatsTotalRadioResetCnt = _MwAp1000DiagStatsTotalRadioResetCnt_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 15),
    _MwAp1000DiagStatsTotalRadioResetCnt_Type()
)
mwAp1000DiagStatsTotalRadioResetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTotalRadioResetCnt.setStatus("current")
_MwAp1000DiagStatsTxPhyError_Type = Counter64
_MwAp1000DiagStatsTxPhyError_Object = MibTableColumn
mwAp1000DiagStatsTxPhyError = _MwAp1000DiagStatsTxPhyError_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 16),
    _MwAp1000DiagStatsTxPhyError_Type()
)
mwAp1000DiagStatsTxPhyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxPhyError.setStatus("current")
_MwAp1000DiagStatsRxNoBuf_Type = Counter64
_MwAp1000DiagStatsRxNoBuf_Object = MibTableColumn
mwAp1000DiagStatsRxNoBuf = _MwAp1000DiagStatsRxNoBuf_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 17),
    _MwAp1000DiagStatsRxNoBuf_Type()
)
mwAp1000DiagStatsRxNoBuf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsRxNoBuf.setStatus("current")
_MwAp1000DiagStatsTxChanRej_Type = Counter64
_MwAp1000DiagStatsTxChanRej_Object = MibTableColumn
mwAp1000DiagStatsTxChanRej = _MwAp1000DiagStatsTxChanRej_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 18),
    _MwAp1000DiagStatsTxChanRej_Type()
)
mwAp1000DiagStatsTxChanRej.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxChanRej.setStatus("current")
_MwAp1000DiagStatsDmaDE_Type = Counter64
_MwAp1000DiagStatsDmaDE_Object = MibTableColumn
mwAp1000DiagStatsDmaDE = _MwAp1000DiagStatsDmaDE_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 19),
    _MwAp1000DiagStatsDmaDE_Type()
)
mwAp1000DiagStatsDmaDE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsDmaDE.setStatus("current")
_MwAp1000DiagStatsDmaDA_Type = Counter64
_MwAp1000DiagStatsDmaDA_Object = MibTableColumn
mwAp1000DiagStatsDmaDA = _MwAp1000DiagStatsDmaDA_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 20),
    _MwAp1000DiagStatsDmaDA_Type()
)
mwAp1000DiagStatsDmaDA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsDmaDA.setStatus("current")
_MwAp1000DiagStatsTxTplunfl_Type = Counter64
_MwAp1000DiagStatsTxTplunfl_Object = MibTableColumn
mwAp1000DiagStatsTxTplunfl = _MwAp1000DiagStatsTxTplunfl_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 21),
    _MwAp1000DiagStatsTxTplunfl_Type()
)
mwAp1000DiagStatsTxTplunfl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxTplunfl.setStatus("current")
_MwAp1000DiagStatsBcnTxFailed_Type = Counter64
_MwAp1000DiagStatsBcnTxFailed_Object = MibTableColumn
mwAp1000DiagStatsBcnTxFailed = _MwAp1000DiagStatsBcnTxFailed_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 22),
    _MwAp1000DiagStatsBcnTxFailed_Type()
)
mwAp1000DiagStatsBcnTxFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsBcnTxFailed.setStatus("current")
_MwAp1000DiagStatsTxError_Type = Counter64
_MwAp1000DiagStatsTxError_Object = MibTableColumn
mwAp1000DiagStatsTxError = _MwAp1000DiagStatsTxError_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 23),
    _MwAp1000DiagStatsTxError_Type()
)
mwAp1000DiagStatsTxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxError.setStatus("current")
_MwAp1000DiagStatsRxStuck_Type = Counter64
_MwAp1000DiagStatsRxStuck_Object = MibTableColumn
mwAp1000DiagStatsRxStuck = _MwAp1000DiagStatsRxStuck_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 24),
    _MwAp1000DiagStatsRxStuck_Type()
)
mwAp1000DiagStatsRxStuck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsRxStuck.setStatus("current")
_MwAp1000DiagStatsRxError_Type = Counter64
_MwAp1000DiagStatsRxError_Object = MibTableColumn
mwAp1000DiagStatsRxError = _MwAp1000DiagStatsRxError_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 25),
    _MwAp1000DiagStatsRxError_Type()
)
mwAp1000DiagStatsRxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsRxError.setStatus("current")
_MwAp1000DiagStatsTxFfiFull_Type = Counter64
_MwAp1000DiagStatsTxFfiFull_Object = MibTableColumn
mwAp1000DiagStatsTxFfiFull = _MwAp1000DiagStatsTxFfiFull_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 26),
    _MwAp1000DiagStatsTxFfiFull_Type()
)
mwAp1000DiagStatsTxFfiFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxFfiFull.setStatus("current")
_MwAp1000DiagStatsTxDrop_Type = Counter64
_MwAp1000DiagStatsTxDrop_Object = MibTableColumn
mwAp1000DiagStatsTxDrop = _MwAp1000DiagStatsTxDrop_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 27),
    _MwAp1000DiagStatsTxDrop_Type()
)
mwAp1000DiagStatsTxDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxDrop.setStatus("current")
_MwAp1000DiagStatsTxqOverflow_Type = Counter64
_MwAp1000DiagStatsTxqOverflow_Object = MibTableColumn
mwAp1000DiagStatsTxqOverflow = _MwAp1000DiagStatsTxqOverflow_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 28),
    _MwAp1000DiagStatsTxqOverflow_Type()
)
mwAp1000DiagStatsTxqOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsTxqOverflow.setStatus("current")
_MwAp1000DiagStatsPmgOverflow_Type = Counter64
_MwAp1000DiagStatsPmgOverflow_Object = MibTableColumn
mwAp1000DiagStatsPmgOverflow = _MwAp1000DiagStatsPmgOverflow_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 29),
    _MwAp1000DiagStatsPmgOverflow_Type()
)
mwAp1000DiagStatsPmgOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsPmgOverflow.setStatus("current")
_MwAp1000DiagStatsRxCgprqrm_Type = Counter64
_MwAp1000DiagStatsRxCgprqrm_Object = MibTableColumn
mwAp1000DiagStatsRxCgprqrm = _MwAp1000DiagStatsRxCgprqrm_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 30),
    _MwAp1000DiagStatsRxCgprqrm_Type()
)
mwAp1000DiagStatsRxCgprqrm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsRxCgprqrm.setStatus("current")
_MwAp1000DiagStatsRowStatus_Type = RowStatus
_MwAp1000DiagStatsRowStatus_Object = MibTableColumn
mwAp1000DiagStatsRowStatus = _MwAp1000DiagStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 11, 1, 31),
    _MwAp1000DiagStatsRowStatus_Type()
)
mwAp1000DiagStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAp1000DiagStatsRowStatus.setStatus("current")
_MwAp400DiagStatsTable_Object = MibTable
mwAp400DiagStatsTable = _MwAp400DiagStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12)
)
if mibBuilder.loadTexts:
    mwAp400DiagStatsTable.setStatus("current")
_MwAp400DiagStatsEntry_Object = MibTableRow
mwAp400DiagStatsEntry = _MwAp400DiagStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1)
)
mwAp400DiagStatsEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwAp400DiagStatsTableIndex"),
)
if mibBuilder.loadTexts:
    mwAp400DiagStatsEntry.setStatus("current")
_MwAp400DiagStatsTableIndex_Type = Integer32
_MwAp400DiagStatsTableIndex_Object = MibTableColumn
mwAp400DiagStatsTableIndex = _MwAp400DiagStatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 1),
    _MwAp400DiagStatsTableIndex_Type()
)
mwAp400DiagStatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwAp400DiagStatsTableIndex.setStatus("current")
_MwAp400DiagStatsNodeId_Type = Unsigned32
_MwAp400DiagStatsNodeId_Object = MibTableColumn
mwAp400DiagStatsNodeId = _MwAp400DiagStatsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 2),
    _MwAp400DiagStatsNodeId_Type()
)
mwAp400DiagStatsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsNodeId.setStatus("current")
_MwAp400DiagStatsIfIndex_Type = Integer32
_MwAp400DiagStatsIfIndex_Object = MibTableColumn
mwAp400DiagStatsIfIndex = _MwAp400DiagStatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 3),
    _MwAp400DiagStatsIfIndex_Type()
)
mwAp400DiagStatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsIfIndex.setStatus("current")
_MwAp400DiagStatsNodeName_Type = DisplayString
_MwAp400DiagStatsNodeName_Object = MibTableColumn
mwAp400DiagStatsNodeName = _MwAp400DiagStatsNodeName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 4),
    _MwAp400DiagStatsNodeName_Type()
)
mwAp400DiagStatsNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsNodeName.setStatus("current")
_MwAp400DiagStatsFatalHwErrorINTs_Type = Counter64
_MwAp400DiagStatsFatalHwErrorINTs_Object = MibTableColumn
mwAp400DiagStatsFatalHwErrorINTs = _MwAp400DiagStatsFatalHwErrorINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 5),
    _MwAp400DiagStatsFatalHwErrorINTs_Type()
)
mwAp400DiagStatsFatalHwErrorINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsFatalHwErrorINTs.setStatus("current")
_MwAp400DiagStatsBeaconMissCount_Type = Counter64
_MwAp400DiagStatsBeaconMissCount_Object = MibTableColumn
mwAp400DiagStatsBeaconMissCount = _MwAp400DiagStatsBeaconMissCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 6),
    _MwAp400DiagStatsBeaconMissCount_Type()
)
mwAp400DiagStatsBeaconMissCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsBeaconMissCount.setStatus("current")
_MwAp400DiagStatsBeaconBufferNullCount_Type = Counter64
_MwAp400DiagStatsBeaconBufferNullCount_Object = MibTableColumn
mwAp400DiagStatsBeaconBufferNullCount = _MwAp400DiagStatsBeaconBufferNullCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 7),
    _MwAp400DiagStatsBeaconBufferNullCount_Type()
)
mwAp400DiagStatsBeaconBufferNullCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsBeaconBufferNullCount.setStatus("current")
_MwAp400DiagStatsNoSkBufferForBeacon_Type = Counter64
_MwAp400DiagStatsNoSkBufferForBeacon_Object = MibTableColumn
mwAp400DiagStatsNoSkBufferForBeacon = _MwAp400DiagStatsNoSkBufferForBeacon_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 8),
    _MwAp400DiagStatsNoSkBufferForBeacon_Type()
)
mwAp400DiagStatsNoSkBufferForBeacon.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsNoSkBufferForBeacon.setStatus("current")
_MwAp400DiagStatsTxUnderrunINTs_Type = Counter64
_MwAp400DiagStatsTxUnderrunINTs_Object = MibTableColumn
mwAp400DiagStatsTxUnderrunINTs = _MwAp400DiagStatsTxUnderrunINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 9),
    _MwAp400DiagStatsTxUnderrunINTs_Type()
)
mwAp400DiagStatsTxUnderrunINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsTxUnderrunINTs.setStatus("current")
_MwAp400DiagStatsTxTimeoutINTs_Type = Counter64
_MwAp400DiagStatsTxTimeoutINTs_Object = MibTableColumn
mwAp400DiagStatsTxTimeoutINTs = _MwAp400DiagStatsTxTimeoutINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 10),
    _MwAp400DiagStatsTxTimeoutINTs_Type()
)
mwAp400DiagStatsTxTimeoutINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsTxTimeoutINTs.setStatus("current")
_MwAp400DiagStatsTxFailedByNoTxBuffer_Type = Counter64
_MwAp400DiagStatsTxFailedByNoTxBuffer_Object = MibTableColumn
mwAp400DiagStatsTxFailedByNoTxBuffer = _MwAp400DiagStatsTxFailedByNoTxBuffer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 11),
    _MwAp400DiagStatsTxFailedByNoTxBuffer_Type()
)
mwAp400DiagStatsTxFailedByNoTxBuffer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsTxFailedByNoTxBuffer.setStatus("current")
_MwAp400DiagStatsTxFailedByFIFOUnderrun_Type = Counter64
_MwAp400DiagStatsTxFailedByFIFOUnderrun_Object = MibTableColumn
mwAp400DiagStatsTxFailedByFIFOUnderrun = _MwAp400DiagStatsTxFailedByFIFOUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 12),
    _MwAp400DiagStatsTxFailedByFIFOUnderrun_Type()
)
mwAp400DiagStatsTxFailedByFIFOUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsTxFailedByFIFOUnderrun.setStatus("current")
_MwAp400DiagStatsTxAggrDescriptorConfigError_Type = Counter64
_MwAp400DiagStatsTxAggrDescriptorConfigError_Object = MibTableColumn
mwAp400DiagStatsTxAggrDescriptorConfigError = _MwAp400DiagStatsTxAggrDescriptorConfigError_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 13),
    _MwAp400DiagStatsTxAggrDescriptorConfigError_Type()
)
mwAp400DiagStatsTxAggrDescriptorConfigError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsTxAggrDescriptorConfigError.setStatus("current")
_MwAp400DiagStatsTxAggrDataUnderrun_Type = Counter64
_MwAp400DiagStatsTxAggrDataUnderrun_Object = MibTableColumn
mwAp400DiagStatsTxAggrDataUnderrun = _MwAp400DiagStatsTxAggrDataUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 14),
    _MwAp400DiagStatsTxAggrDataUnderrun_Type()
)
mwAp400DiagStatsTxAggrDataUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsTxAggrDataUnderrun.setStatus("current")
_MwAp400DiagStatsTxAggrDelimiterUnderrun_Type = Counter64
_MwAp400DiagStatsTxAggrDelimiterUnderrun_Object = MibTableColumn
mwAp400DiagStatsTxAggrDelimiterUnderrun = _MwAp400DiagStatsTxAggrDelimiterUnderrun_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 15),
    _MwAp400DiagStatsTxAggrDelimiterUnderrun_Type()
)
mwAp400DiagStatsTxAggrDelimiterUnderrun.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsTxAggrDelimiterUnderrun.setStatus("current")
_MwAp400DiagStatsTotalTidResetCnt_Type = Counter64
_MwAp400DiagStatsTotalTidResetCnt_Object = MibTableColumn
mwAp400DiagStatsTotalTidResetCnt = _MwAp400DiagStatsTotalTidResetCnt_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 16),
    _MwAp400DiagStatsTotalTidResetCnt_Type()
)
mwAp400DiagStatsTotalTidResetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsTotalTidResetCnt.setStatus("current")
_MwAp400DiagStatsCarrierSenseTimeoutINTs_Type = Counter64
_MwAp400DiagStatsCarrierSenseTimeoutINTs_Object = MibTableColumn
mwAp400DiagStatsCarrierSenseTimeoutINTs = _MwAp400DiagStatsCarrierSenseTimeoutINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 17),
    _MwAp400DiagStatsCarrierSenseTimeoutINTs_Type()
)
mwAp400DiagStatsCarrierSenseTimeoutINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsCarrierSenseTimeoutINTs.setStatus("current")
_MwAp400DiagStatsIsSlamTxNoAckAddr_Type = Counter64
_MwAp400DiagStatsIsSlamTxNoAckAddr_Object = MibTableColumn
mwAp400DiagStatsIsSlamTxNoAckAddr = _MwAp400DiagStatsIsSlamTxNoAckAddr_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 18),
    _MwAp400DiagStatsIsSlamTxNoAckAddr_Type()
)
mwAp400DiagStatsIsSlamTxNoAckAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsIsSlamTxNoAckAddr.setStatus("current")
_MwAp400DiagStatsRxOverrunINTs_Type = Counter64
_MwAp400DiagStatsRxOverrunINTs_Object = MibTableColumn
mwAp400DiagStatsRxOverrunINTs = _MwAp400DiagStatsRxOverrunINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 19),
    _MwAp400DiagStatsRxOverrunINTs_Type()
)
mwAp400DiagStatsRxOverrunINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRxOverrunINTs.setStatus("current")
_MwAp400DiagStatsRxEolINTs_Type = Counter64
_MwAp400DiagStatsRxEolINTs_Object = MibTableColumn
mwAp400DiagStatsRxEolINTs = _MwAp400DiagStatsRxEolINTs_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 20),
    _MwAp400DiagStatsRxEolINTs_Type()
)
mwAp400DiagStatsRxEolINTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRxEolINTs.setStatus("current")
_MwAp400DiagStatsRxPacketsBadVersion_Type = Counter64
_MwAp400DiagStatsRxPacketsBadVersion_Object = MibTableColumn
mwAp400DiagStatsRxPacketsBadVersion = _MwAp400DiagStatsRxPacketsBadVersion_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 21),
    _MwAp400DiagStatsRxPacketsBadVersion_Type()
)
mwAp400DiagStatsRxPacketsBadVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRxPacketsBadVersion.setStatus("current")
_MwAp400DiagStatsRadioResetBeaconStuck_Type = Counter64
_MwAp400DiagStatsRadioResetBeaconStuck_Object = MibTableColumn
mwAp400DiagStatsRadioResetBeaconStuck = _MwAp400DiagStatsRadioResetBeaconStuck_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 22),
    _MwAp400DiagStatsRadioResetBeaconStuck_Type()
)
mwAp400DiagStatsRadioResetBeaconStuck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRadioResetBeaconStuck.setStatus("current")
_MwAp400DiagStatsRadioResetTPScale_Type = Counter64
_MwAp400DiagStatsRadioResetTPScale_Object = MibTableColumn
mwAp400DiagStatsRadioResetTPScale = _MwAp400DiagStatsRadioResetTPScale_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 23),
    _MwAp400DiagStatsRadioResetTPScale_Type()
)
mwAp400DiagStatsRadioResetTPScale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRadioResetTPScale.setStatus("current")
_MwAp400DiagStatsRadioResetFatalTasklet_Type = Counter64
_MwAp400DiagStatsRadioResetFatalTasklet_Object = MibTableColumn
mwAp400DiagStatsRadioResetFatalTasklet = _MwAp400DiagStatsRadioResetFatalTasklet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 24),
    _MwAp400DiagStatsRadioResetFatalTasklet_Type()
)
mwAp400DiagStatsRadioResetFatalTasklet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRadioResetFatalTasklet.setStatus("current")
_MwAp400DiagStatsRadioResetRxornTasklet_Type = Counter64
_MwAp400DiagStatsRadioResetRxornTasklet_Object = MibTableColumn
mwAp400DiagStatsRadioResetRxornTasklet = _MwAp400DiagStatsRadioResetRxornTasklet_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 25),
    _MwAp400DiagStatsRadioResetRxornTasklet_Type()
)
mwAp400DiagStatsRadioResetRxornTasklet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRadioResetRxornTasklet.setStatus("current")
_MwAp400DiagStatsRadioResetCalibrate_Type = Counter64
_MwAp400DiagStatsRadioResetCalibrate_Object = MibTableColumn
mwAp400DiagStatsRadioResetCalibrate = _MwAp400DiagStatsRadioResetCalibrate_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 26),
    _MwAp400DiagStatsRadioResetCalibrate_Type()
)
mwAp400DiagStatsRadioResetCalibrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRadioResetCalibrate.setStatus("current")
_MwAp400DiagStatsRadioResetTxAntennaSwitch_Type = Counter64
_MwAp400DiagStatsRadioResetTxAntennaSwitch_Object = MibTableColumn
mwAp400DiagStatsRadioResetTxAntennaSwitch = _MwAp400DiagStatsRadioResetTxAntennaSwitch_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 27),
    _MwAp400DiagStatsRadioResetTxAntennaSwitch_Type()
)
mwAp400DiagStatsRadioResetTxAntennaSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRadioResetTxAntennaSwitch.setStatus("current")
_MwAp400DiagStatsRadioResetRxChain_Type = Counter64
_MwAp400DiagStatsRadioResetRxChain_Object = MibTableColumn
mwAp400DiagStatsRadioResetRxChain = _MwAp400DiagStatsRadioResetRxChain_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 28),
    _MwAp400DiagStatsRadioResetRxChain_Type()
)
mwAp400DiagStatsRadioResetRxChain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRadioResetRxChain.setStatus("current")
_MwAp400DiagStatsRadioResetNoTxFrames_Type = Counter64
_MwAp400DiagStatsRadioResetNoTxFrames_Object = MibTableColumn
mwAp400DiagStatsRadioResetNoTxFrames = _MwAp400DiagStatsRadioResetNoTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 29),
    _MwAp400DiagStatsRadioResetNoTxFrames_Type()
)
mwAp400DiagStatsRadioResetNoTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRadioResetNoTxFrames.setStatus("current")
_MwAp400DiagStatsTotalRadioResetCnt_Type = Counter64
_MwAp400DiagStatsTotalRadioResetCnt_Object = MibTableColumn
mwAp400DiagStatsTotalRadioResetCnt = _MwAp400DiagStatsTotalRadioResetCnt_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 30),
    _MwAp400DiagStatsTotalRadioResetCnt_Type()
)
mwAp400DiagStatsTotalRadioResetCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsTotalRadioResetCnt.setStatus("current")
_MwAp400DiagStatsRxPhyError_Type = Counter64
_MwAp400DiagStatsRxPhyError_Object = MibTableColumn
mwAp400DiagStatsRxPhyError = _MwAp400DiagStatsRxPhyError_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 31),
    _MwAp400DiagStatsRxPhyError_Type()
)
mwAp400DiagStatsRxPhyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRxPhyError.setStatus("current")
_MwAp400DiagStatsRowStatus_Type = RowStatus
_MwAp400DiagStatsRowStatus_Object = MibTableColumn
mwAp400DiagStatsRowStatus = _MwAp400DiagStatsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 12, 1, 32),
    _MwAp400DiagStatsRowStatus_Type()
)
mwAp400DiagStatsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwAp400DiagStatsRowStatus.setStatus("current")
_MwSystemGeneral_ObjectIdentity = ObjectIdentity
mwSystemGeneral = _MwSystemGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13)
)
_MwSystemGeneralName_Type = DisplayString
_MwSystemGeneralName_Object = MibScalar
mwSystemGeneralName = _MwSystemGeneralName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 1),
    _MwSystemGeneralName_Type()
)
mwSystemGeneralName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralName.setStatus("current")
_MwSystemGeneralModel_Type = DisplayString
_MwSystemGeneralModel_Object = MibScalar
mwSystemGeneralModel = _MwSystemGeneralModel_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 2),
    _MwSystemGeneralModel_Type()
)
mwSystemGeneralModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralModel.setStatus("current")
_MwSystemGeneralVersion_Type = DisplayString
_MwSystemGeneralVersion_Object = MibScalar
mwSystemGeneralVersion = _MwSystemGeneralVersion_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 3),
    _MwSystemGeneralVersion_Type()
)
mwSystemGeneralVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralVersion.setStatus("current")
_MwSystemGeneralUptime_Type = TimeTicks
_MwSystemGeneralUptime_Object = MibScalar
mwSystemGeneralUptime = _MwSystemGeneralUptime_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 4),
    _MwSystemGeneralUptime_Type()
)
mwSystemGeneralUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralUptime.setStatus("current")
_MwSystemGeneralMaxApLimit_Type = Unsigned32
_MwSystemGeneralMaxApLimit_Object = MibScalar
mwSystemGeneralMaxApLimit = _MwSystemGeneralMaxApLimit_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 5),
    _MwSystemGeneralMaxApLimit_Type()
)
mwSystemGeneralMaxApLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralMaxApLimit.setStatus("current")
_MwSystemGeneralMaxClientLimit_Type = Unsigned32
_MwSystemGeneralMaxClientLimit_Object = MibScalar
mwSystemGeneralMaxClientLimit = _MwSystemGeneralMaxClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 6),
    _MwSystemGeneralMaxClientLimit_Type()
)
mwSystemGeneralMaxClientLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralMaxClientLimit.setStatus("current")
_MwSystemGeneralInstalledApLicenses_Type = Unsigned32
_MwSystemGeneralInstalledApLicenses_Object = MibScalar
mwSystemGeneralInstalledApLicenses = _MwSystemGeneralInstalledApLicenses_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 7),
    _MwSystemGeneralInstalledApLicenses_Type()
)
mwSystemGeneralInstalledApLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralInstalledApLicenses.setStatus("current")
_MwSystemGeneralInUseApLicenses_Type = Unsigned32
_MwSystemGeneralInUseApLicenses_Object = MibScalar
mwSystemGeneralInUseApLicenses = _MwSystemGeneralInUseApLicenses_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 8),
    _MwSystemGeneralInUseApLicenses_Type()
)
mwSystemGeneralInUseApLicenses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralInUseApLicenses.setStatus("current")
_MwSystemGeneralTotalOnlineAps_Type = Unsigned32
_MwSystemGeneralTotalOnlineAps_Object = MibScalar
mwSystemGeneralTotalOnlineAps = _MwSystemGeneralTotalOnlineAps_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 9),
    _MwSystemGeneralTotalOnlineAps_Type()
)
mwSystemGeneralTotalOnlineAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalOnlineAps.setStatus("current")
_MwSystemGeneralTotalOfflineAps_Type = Unsigned32
_MwSystemGeneralTotalOfflineAps_Object = MibScalar
mwSystemGeneralTotalOfflineAps = _MwSystemGeneralTotalOfflineAps_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 10),
    _MwSystemGeneralTotalOfflineAps_Type()
)
mwSystemGeneralTotalOfflineAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalOfflineAps.setStatus("current")
_MwSystemGeneralTotalWirelessStations_Type = Unsigned32
_MwSystemGeneralTotalWirelessStations_Object = MibScalar
mwSystemGeneralTotalWirelessStations = _MwSystemGeneralTotalWirelessStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 11),
    _MwSystemGeneralTotalWirelessStations_Type()
)
mwSystemGeneralTotalWirelessStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalWirelessStations.setStatus("current")
_MwSystemGeneralTotal24GStations_Type = Unsigned32
_MwSystemGeneralTotal24GStations_Object = MibScalar
mwSystemGeneralTotal24GStations = _MwSystemGeneralTotal24GStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 12),
    _MwSystemGeneralTotal24GStations_Type()
)
mwSystemGeneralTotal24GStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotal24GStations.setStatus("current")
_MwSystemGeneralTotal5GStations_Type = Unsigned32
_MwSystemGeneralTotal5GStations_Object = MibScalar
mwSystemGeneralTotal5GStations = _MwSystemGeneralTotal5GStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 13),
    _MwSystemGeneralTotal5GStations_Type()
)
mwSystemGeneralTotal5GStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotal5GStations.setStatus("current")
_MwSystemGeneralTotalWiredStations_Type = Unsigned32
_MwSystemGeneralTotalWiredStations_Object = MibScalar
mwSystemGeneralTotalWiredStations = _MwSystemGeneralTotalWiredStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 14),
    _MwSystemGeneralTotalWiredStations_Type()
)
mwSystemGeneralTotalWiredStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalWiredStations.setStatus("current")
_MwSystemGeneralTotalAlarms_Type = Unsigned32
_MwSystemGeneralTotalAlarms_Object = MibScalar
mwSystemGeneralTotalAlarms = _MwSystemGeneralTotalAlarms_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 15),
    _MwSystemGeneralTotalAlarms_Type()
)
mwSystemGeneralTotalAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalAlarms.setStatus("current")
_MwSystemGeneralTotalCritAlarms_Type = Unsigned32
_MwSystemGeneralTotalCritAlarms_Object = MibScalar
mwSystemGeneralTotalCritAlarms = _MwSystemGeneralTotalCritAlarms_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 16),
    _MwSystemGeneralTotalCritAlarms_Type()
)
mwSystemGeneralTotalCritAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalCritAlarms.setStatus("current")
_MwSystemGeneralTotalMajorAlarms_Type = Unsigned32
_MwSystemGeneralTotalMajorAlarms_Object = MibScalar
mwSystemGeneralTotalMajorAlarms = _MwSystemGeneralTotalMajorAlarms_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 17),
    _MwSystemGeneralTotalMajorAlarms_Type()
)
mwSystemGeneralTotalMajorAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalMajorAlarms.setStatus("current")
_MwSystemGeneralTotalMinorAlarms_Type = Unsigned32
_MwSystemGeneralTotalMinorAlarms_Object = MibScalar
mwSystemGeneralTotalMinorAlarms = _MwSystemGeneralTotalMinorAlarms_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 18),
    _MwSystemGeneralTotalMinorAlarms_Type()
)
mwSystemGeneralTotalMinorAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalMinorAlarms.setStatus("current")
_MwSystemGeneralTotalRogueAps_Type = Unsigned32
_MwSystemGeneralTotalRogueAps_Object = MibScalar
mwSystemGeneralTotalRogueAps = _MwSystemGeneralTotalRogueAps_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 19),
    _MwSystemGeneralTotalRogueAps_Type()
)
mwSystemGeneralTotalRogueAps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalRogueAps.setStatus("current")
_MwSystemGeneralTotalRogueStations_Type = Unsigned32
_MwSystemGeneralTotalRogueStations_Object = MibScalar
mwSystemGeneralTotalRogueStations = _MwSystemGeneralTotalRogueStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 20),
    _MwSystemGeneralTotalRogueStations_Type()
)
mwSystemGeneralTotalRogueStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalRogueStations.setStatus("current")
_MwSystemGeneralTotalRogueUnknownDevices_Type = Unsigned32
_MwSystemGeneralTotalRogueUnknownDevices_Object = MibScalar
mwSystemGeneralTotalRogueUnknownDevices = _MwSystemGeneralTotalRogueUnknownDevices_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 21),
    _MwSystemGeneralTotalRogueUnknownDevices_Type()
)
mwSystemGeneralTotalRogueUnknownDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalRogueUnknownDevices.setStatus("current")
_MwSystemGeneralTotalClearEssProfiles_Type = Unsigned32
_MwSystemGeneralTotalClearEssProfiles_Object = MibScalar
mwSystemGeneralTotalClearEssProfiles = _MwSystemGeneralTotalClearEssProfiles_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 22),
    _MwSystemGeneralTotalClearEssProfiles_Type()
)
mwSystemGeneralTotalClearEssProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalClearEssProfiles.setStatus("current")
_MwSystemGeneralTotalSecureEssProfiles_Type = Unsigned32
_MwSystemGeneralTotalSecureEssProfiles_Object = MibScalar
mwSystemGeneralTotalSecureEssProfiles = _MwSystemGeneralTotalSecureEssProfiles_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 23),
    _MwSystemGeneralTotalSecureEssProfiles_Type()
)
mwSystemGeneralTotalSecureEssProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalSecureEssProfiles.setStatus("current")
_MwSystemGeneralTotalCaptivePortalEssProfiles_Type = Unsigned32
_MwSystemGeneralTotalCaptivePortalEssProfiles_Object = MibScalar
mwSystemGeneralTotalCaptivePortalEssProfiles = _MwSystemGeneralTotalCaptivePortalEssProfiles_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 13, 24),
    _MwSystemGeneralTotalCaptivePortalEssProfiles_Type()
)
mwSystemGeneralTotalCaptivePortalEssProfiles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemGeneralTotalCaptivePortalEssProfiles.setStatus("current")
_MwSystemResource_ObjectIdentity = ObjectIdentity
mwSystemResource = _MwSystemResource_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14)
)
_MwSystemResourceCpuUsagePercentageUser_Type = Integer32
_MwSystemResourceCpuUsagePercentageUser_Object = MibScalar
mwSystemResourceCpuUsagePercentageUser = _MwSystemResourceCpuUsagePercentageUser_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14, 1),
    _MwSystemResourceCpuUsagePercentageUser_Type()
)
mwSystemResourceCpuUsagePercentageUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemResourceCpuUsagePercentageUser.setStatus("current")
_MwSystemResourceCpuUsagePercentageSystem_Type = Integer32
_MwSystemResourceCpuUsagePercentageSystem_Object = MibScalar
mwSystemResourceCpuUsagePercentageSystem = _MwSystemResourceCpuUsagePercentageSystem_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14, 2),
    _MwSystemResourceCpuUsagePercentageSystem_Type()
)
mwSystemResourceCpuUsagePercentageSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemResourceCpuUsagePercentageSystem.setStatus("current")
_MwSystemResourceCpuUsagePercentageIdle_Type = Integer32
_MwSystemResourceCpuUsagePercentageIdle_Object = MibScalar
mwSystemResourceCpuUsagePercentageIdle = _MwSystemResourceCpuUsagePercentageIdle_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14, 3),
    _MwSystemResourceCpuUsagePercentageIdle_Type()
)
mwSystemResourceCpuUsagePercentageIdle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemResourceCpuUsagePercentageIdle.setStatus("current")
_MwSystemResourceMemoryTotalSize_Type = Unsigned32
_MwSystemResourceMemoryTotalSize_Object = MibScalar
mwSystemResourceMemoryTotalSize = _MwSystemResourceMemoryTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14, 4),
    _MwSystemResourceMemoryTotalSize_Type()
)
mwSystemResourceMemoryTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemResourceMemoryTotalSize.setStatus("current")
_MwSystemResourceMemoryUsedSize_Type = Unsigned32
_MwSystemResourceMemoryUsedSize_Object = MibScalar
mwSystemResourceMemoryUsedSize = _MwSystemResourceMemoryUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14, 5),
    _MwSystemResourceMemoryUsedSize_Type()
)
mwSystemResourceMemoryUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemResourceMemoryUsedSize.setStatus("current")
_MwSystemResourceMemoryFreeSize_Type = Unsigned32
_MwSystemResourceMemoryFreeSize_Object = MibScalar
mwSystemResourceMemoryFreeSize = _MwSystemResourceMemoryFreeSize_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14, 6),
    _MwSystemResourceMemoryFreeSize_Type()
)
mwSystemResourceMemoryFreeSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemResourceMemoryFreeSize.setStatus("current")
_MwSystemResourceRootFileSystemTotalSize_Type = Unsigned32
_MwSystemResourceRootFileSystemTotalSize_Object = MibScalar
mwSystemResourceRootFileSystemTotalSize = _MwSystemResourceRootFileSystemTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14, 7),
    _MwSystemResourceRootFileSystemTotalSize_Type()
)
mwSystemResourceRootFileSystemTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemResourceRootFileSystemTotalSize.setStatus("current")
_MwSystemResourceRootFileSystemUsedSize_Type = Unsigned32
_MwSystemResourceRootFileSystemUsedSize_Object = MibScalar
mwSystemResourceRootFileSystemUsedSize = _MwSystemResourceRootFileSystemUsedSize_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14, 8),
    _MwSystemResourceRootFileSystemUsedSize_Type()
)
mwSystemResourceRootFileSystemUsedSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemResourceRootFileSystemUsedSize.setStatus("current")
_MwSystemResourceRootFileSystemAvailSize_Type = Unsigned32
_MwSystemResourceRootFileSystemAvailSize_Object = MibScalar
mwSystemResourceRootFileSystemAvailSize = _MwSystemResourceRootFileSystemAvailSize_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14, 9),
    _MwSystemResourceRootFileSystemAvailSize_Type()
)
mwSystemResourceRootFileSystemAvailSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemResourceRootFileSystemAvailSize.setStatus("current")
_MwSystemResourceRootFileSystemUsagePercentage_Type = Integer32
_MwSystemResourceRootFileSystemUsagePercentage_Object = MibScalar
mwSystemResourceRootFileSystemUsagePercentage = _MwSystemResourceRootFileSystemUsagePercentage_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 14, 10),
    _MwSystemResourceRootFileSystemUsagePercentage_Type()
)
mwSystemResourceRootFileSystemUsagePercentage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemResourceRootFileSystemUsagePercentage.setStatus("current")
_MwSystemStation_ObjectIdentity = ObjectIdentity
mwSystemStation = _MwSystemStation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15)
)
_MwSystemStationTotal11aStations_Type = Unsigned32
_MwSystemStationTotal11aStations_Object = MibScalar
mwSystemStationTotal11aStations = _MwSystemStationTotal11aStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 1),
    _MwSystemStationTotal11aStations_Type()
)
mwSystemStationTotal11aStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotal11aStations.setStatus("current")
_MwSystemStationTotal11an1Stations_Type = Unsigned32
_MwSystemStationTotal11an1Stations_Object = MibScalar
mwSystemStationTotal11an1Stations = _MwSystemStationTotal11an1Stations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 2),
    _MwSystemStationTotal11an1Stations_Type()
)
mwSystemStationTotal11an1Stations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotal11an1Stations.setStatus("current")
_MwSystemStationTotal11an2Stations_Type = Unsigned32
_MwSystemStationTotal11an2Stations_Object = MibScalar
mwSystemStationTotal11an2Stations = _MwSystemStationTotal11an2Stations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 3),
    _MwSystemStationTotal11an2Stations_Type()
)
mwSystemStationTotal11an2Stations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotal11an2Stations.setStatus("current")
_MwSystemStationTotal11an3Stations_Type = Unsigned32
_MwSystemStationTotal11an3Stations_Object = MibScalar
mwSystemStationTotal11an3Stations = _MwSystemStationTotal11an3Stations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 4),
    _MwSystemStationTotal11an3Stations_Type()
)
mwSystemStationTotal11an3Stations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotal11an3Stations.setStatus("current")
_MwSystemStationTotal11bStations_Type = Unsigned32
_MwSystemStationTotal11bStations_Object = MibScalar
mwSystemStationTotal11bStations = _MwSystemStationTotal11bStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 5),
    _MwSystemStationTotal11bStations_Type()
)
mwSystemStationTotal11bStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotal11bStations.setStatus("current")
_MwSystemStationTotal11bgStations_Type = Unsigned32
_MwSystemStationTotal11bgStations_Object = MibScalar
mwSystemStationTotal11bgStations = _MwSystemStationTotal11bgStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 6),
    _MwSystemStationTotal11bgStations_Type()
)
mwSystemStationTotal11bgStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotal11bgStations.setStatus("current")
_MwSystemStationTotal11gn1Stations_Type = Unsigned32
_MwSystemStationTotal11gn1Stations_Object = MibScalar
mwSystemStationTotal11gn1Stations = _MwSystemStationTotal11gn1Stations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 7),
    _MwSystemStationTotal11gn1Stations_Type()
)
mwSystemStationTotal11gn1Stations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotal11gn1Stations.setStatus("current")
_MwSystemStationTotal11gn2Stations_Type = Unsigned32
_MwSystemStationTotal11gn2Stations_Object = MibScalar
mwSystemStationTotal11gn2Stations = _MwSystemStationTotal11gn2Stations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 8),
    _MwSystemStationTotal11gn2Stations_Type()
)
mwSystemStationTotal11gn2Stations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotal11gn2Stations.setStatus("current")
_MwSystemStationTotal11gn3Stations_Type = Unsigned32
_MwSystemStationTotal11gn3Stations_Object = MibScalar
mwSystemStationTotal11gn3Stations = _MwSystemStationTotal11gn3Stations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 9),
    _MwSystemStationTotal11gn3Stations_Type()
)
mwSystemStationTotal11gn3Stations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotal11gn3Stations.setStatus("current")
_MwSystemStationTotalDataStations_Type = Unsigned32
_MwSystemStationTotalDataStations_Object = MibScalar
mwSystemStationTotalDataStations = _MwSystemStationTotalDataStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 10),
    _MwSystemStationTotalDataStations_Type()
)
mwSystemStationTotalDataStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotalDataStations.setStatus("current")
_MwSystemStationTotalPhoneStations_Type = Unsigned32
_MwSystemStationTotalPhoneStations_Object = MibScalar
mwSystemStationTotalPhoneStations = _MwSystemStationTotalPhoneStations_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 15, 11),
    _MwSystemStationTotalPhoneStations_Type()
)
mwSystemStationTotalPhoneStations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemStationTotalPhoneStations.setStatus("current")
_MwSystemThruput_ObjectIdentity = ObjectIdentity
mwSystemThruput = _MwSystemThruput_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 16)
)
_MwSystemThruputTotalControllerRxBytes_Type = Counter64
_MwSystemThruputTotalControllerRxBytes_Object = MibScalar
mwSystemThruputTotalControllerRxBytes = _MwSystemThruputTotalControllerRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 16, 1),
    _MwSystemThruputTotalControllerRxBytes_Type()
)
mwSystemThruputTotalControllerRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemThruputTotalControllerRxBytes.setStatus("current")
_MwSystemThruputTotalControllerTxBytes_Type = Counter64
_MwSystemThruputTotalControllerTxBytes_Object = MibScalar
mwSystemThruputTotalControllerTxBytes = _MwSystemThruputTotalControllerTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 16, 2),
    _MwSystemThruputTotalControllerTxBytes_Type()
)
mwSystemThruputTotalControllerTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemThruputTotalControllerTxBytes.setStatus("current")
_MwSystemThruputControllerRxThroughput_Type = Unsigned32
_MwSystemThruputControllerRxThroughput_Object = MibScalar
mwSystemThruputControllerRxThroughput = _MwSystemThruputControllerRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 16, 3),
    _MwSystemThruputControllerRxThroughput_Type()
)
mwSystemThruputControllerRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemThruputControllerRxThroughput.setStatus("current")
_MwSystemThruputControllerTxThroughput_Type = Unsigned32
_MwSystemThruputControllerTxThroughput_Object = MibScalar
mwSystemThruputControllerTxThroughput = _MwSystemThruputControllerTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 16, 4),
    _MwSystemThruputControllerTxThroughput_Type()
)
mwSystemThruputControllerTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemThruputControllerTxThroughput.setStatus("current")
_MwSystemThruputTotalWlanSystemRxBytes_Type = Counter64
_MwSystemThruputTotalWlanSystemRxBytes_Object = MibScalar
mwSystemThruputTotalWlanSystemRxBytes = _MwSystemThruputTotalWlanSystemRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 16, 5),
    _MwSystemThruputTotalWlanSystemRxBytes_Type()
)
mwSystemThruputTotalWlanSystemRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemThruputTotalWlanSystemRxBytes.setStatus("current")
_MwSystemThruputTotalWlanSystemTxBytes_Type = Counter64
_MwSystemThruputTotalWlanSystemTxBytes_Object = MibScalar
mwSystemThruputTotalWlanSystemTxBytes = _MwSystemThruputTotalWlanSystemTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 16, 6),
    _MwSystemThruputTotalWlanSystemTxBytes_Type()
)
mwSystemThruputTotalWlanSystemTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemThruputTotalWlanSystemTxBytes.setStatus("current")
_MwSystemThruputWlanRxThroughput_Type = Unsigned32
_MwSystemThruputWlanRxThroughput_Object = MibScalar
mwSystemThruputWlanRxThroughput = _MwSystemThruputWlanRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 16, 7),
    _MwSystemThruputWlanRxThroughput_Type()
)
mwSystemThruputWlanRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemThruputWlanRxThroughput.setStatus("current")
_MwSystemThruputWlanTxThroughput_Type = Unsigned32
_MwSystemThruputWlanTxThroughput_Object = MibScalar
mwSystemThruputWlanTxThroughput = _MwSystemThruputWlanTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 16, 8),
    _MwSystemThruputWlanTxThroughput_Type()
)
mwSystemThruputWlanTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwSystemThruputWlanTxThroughput.setStatus("current")
_MwPerEss80211StatsTable_Object = MibTable
mwPerEss80211StatsTable = _MwPerEss80211StatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17)
)
if mibBuilder.loadTexts:
    mwPerEss80211StatsTable.setStatus("current")
_MwPerEss80211StatsEntry_Object = MibTableRow
mwPerEss80211StatsEntry = _MwPerEss80211StatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1)
)
mwPerEss80211StatsEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwPerEss80211StatsTableIndex"),
)
if mibBuilder.loadTexts:
    mwPerEss80211StatsEntry.setStatus("current")
_MwPerEss80211StatsTableIndex_Type = Integer32
_MwPerEss80211StatsTableIndex_Object = MibTableColumn
mwPerEss80211StatsTableIndex = _MwPerEss80211StatsTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 1),
    _MwPerEss80211StatsTableIndex_Type()
)
mwPerEss80211StatsTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTableIndex.setStatus("current")
_MwPerEss80211StatsNodeId_Type = Unsigned32
_MwPerEss80211StatsNodeId_Object = MibTableColumn
mwPerEss80211StatsNodeId = _MwPerEss80211StatsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 2),
    _MwPerEss80211StatsNodeId_Type()
)
mwPerEss80211StatsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsNodeId.setStatus("current")
_MwPerEss80211StatsIfIndex_Type = Integer32
_MwPerEss80211StatsIfIndex_Object = MibTableColumn
mwPerEss80211StatsIfIndex = _MwPerEss80211StatsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 3),
    _MwPerEss80211StatsIfIndex_Type()
)
mwPerEss80211StatsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsIfIndex.setStatus("current")


class _MwPerEss80211StatsEssId_Type(DisplayString):
    """Custom type mwPerEss80211StatsEssId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwPerEss80211StatsEssId_Type.__name__ = "DisplayString"
_MwPerEss80211StatsEssId_Object = MibTableColumn
mwPerEss80211StatsEssId = _MwPerEss80211StatsEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 4),
    _MwPerEss80211StatsEssId_Type()
)
mwPerEss80211StatsEssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsEssId.setStatus("current")
_MwPerEss80211StatsBssid_Type = MacAddress
_MwPerEss80211StatsBssid_Object = MibTableColumn
mwPerEss80211StatsBssid = _MwPerEss80211StatsBssid_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 5),
    _MwPerEss80211StatsBssid_Type()
)
mwPerEss80211StatsBssid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsBssid.setStatus("current")
_MwPerEss80211StatsRxThroughput_Type = Unsigned32
_MwPerEss80211StatsRxThroughput_Object = MibTableColumn
mwPerEss80211StatsRxThroughput = _MwPerEss80211StatsRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 6),
    _MwPerEss80211StatsRxThroughput_Type()
)
mwPerEss80211StatsRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsRxThroughput.setStatus("current")
_MwPerEss80211StatsTxThroughput_Type = Unsigned32
_MwPerEss80211StatsTxThroughput_Object = MibTableColumn
mwPerEss80211StatsTxThroughput = _MwPerEss80211StatsTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 7),
    _MwPerEss80211StatsTxThroughput_Type()
)
mwPerEss80211StatsTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTxThroughput.setStatus("current")
_MwPerEss80211StatsTotalThroughput_Type = Unsigned32
_MwPerEss80211StatsTotalThroughput_Object = MibTableColumn
mwPerEss80211StatsTotalThroughput = _MwPerEss80211StatsTotalThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 8),
    _MwPerEss80211StatsTotalThroughput_Type()
)
mwPerEss80211StatsTotalThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalThroughput.setStatus("current")
_MwPerEss80211StatsTotalRxBytes_Type = Counter64
_MwPerEss80211StatsTotalRxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalRxBytes = _MwPerEss80211StatsTotalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 11),
    _MwPerEss80211StatsTotalRxBytes_Type()
)
mwPerEss80211StatsTotalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalRxBytes.setStatus("current")
_MwPerEss80211StatsTotalTxBytes_Type = Counter64
_MwPerEss80211StatsTotalTxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalTxBytes = _MwPerEss80211StatsTotalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 12),
    _MwPerEss80211StatsTotalTxBytes_Type()
)
mwPerEss80211StatsTotalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalTxBytes.setStatus("current")
_MwPerEss80211StatsTotalVideoRxBytes_Type = Counter64
_MwPerEss80211StatsTotalVideoRxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalVideoRxBytes = _MwPerEss80211StatsTotalVideoRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 13),
    _MwPerEss80211StatsTotalVideoRxBytes_Type()
)
mwPerEss80211StatsTotalVideoRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalVideoRxBytes.setStatus("current")
_MwPerEss80211StatsTotalVideoTxBytes_Type = Counter64
_MwPerEss80211StatsTotalVideoTxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalVideoTxBytes = _MwPerEss80211StatsTotalVideoTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 14),
    _MwPerEss80211StatsTotalVideoTxBytes_Type()
)
mwPerEss80211StatsTotalVideoTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalVideoTxBytes.setStatus("current")
_MwPerEss80211StatsTotalVoiceRxBytes_Type = Counter64
_MwPerEss80211StatsTotalVoiceRxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalVoiceRxBytes = _MwPerEss80211StatsTotalVoiceRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 15),
    _MwPerEss80211StatsTotalVoiceRxBytes_Type()
)
mwPerEss80211StatsTotalVoiceRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalVoiceRxBytes.setStatus("current")
_MwPerEss80211StatsTotalVoiceTxBytes_Type = Counter64
_MwPerEss80211StatsTotalVoiceTxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalVoiceTxBytes = _MwPerEss80211StatsTotalVoiceTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 16),
    _MwPerEss80211StatsTotalVoiceTxBytes_Type()
)
mwPerEss80211StatsTotalVoiceTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalVoiceTxBytes.setStatus("current")
_MwPerEss80211StatsTotalBestEffortRxBytes_Type = Counter64
_MwPerEss80211StatsTotalBestEffortRxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalBestEffortRxBytes = _MwPerEss80211StatsTotalBestEffortRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 17),
    _MwPerEss80211StatsTotalBestEffortRxBytes_Type()
)
mwPerEss80211StatsTotalBestEffortRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalBestEffortRxBytes.setStatus("current")
_MwPerEss80211StatsTotalBestEffortTxBytes_Type = Counter64
_MwPerEss80211StatsTotalBestEffortTxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalBestEffortTxBytes = _MwPerEss80211StatsTotalBestEffortTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 18),
    _MwPerEss80211StatsTotalBestEffortTxBytes_Type()
)
mwPerEss80211StatsTotalBestEffortTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalBestEffortTxBytes.setStatus("current")
_MwPerEss80211StatsTotalBackgroundRxBytes_Type = Counter64
_MwPerEss80211StatsTotalBackgroundRxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalBackgroundRxBytes = _MwPerEss80211StatsTotalBackgroundRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 19),
    _MwPerEss80211StatsTotalBackgroundRxBytes_Type()
)
mwPerEss80211StatsTotalBackgroundRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalBackgroundRxBytes.setStatus("current")
_MwPerEss80211StatsTotalBackgroundTxBytes_Type = Counter64
_MwPerEss80211StatsTotalBackgroundTxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalBackgroundTxBytes = _MwPerEss80211StatsTotalBackgroundTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 20),
    _MwPerEss80211StatsTotalBackgroundTxBytes_Type()
)
mwPerEss80211StatsTotalBackgroundTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalBackgroundTxBytes.setStatus("current")
_MwPerEss80211StatsTotalUnicastRxBytes_Type = Counter64
_MwPerEss80211StatsTotalUnicastRxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalUnicastRxBytes = _MwPerEss80211StatsTotalUnicastRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 21),
    _MwPerEss80211StatsTotalUnicastRxBytes_Type()
)
mwPerEss80211StatsTotalUnicastRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalUnicastRxBytes.setStatus("current")
_MwPerEss80211StatsTotalUnicastTxBytes_Type = Counter64
_MwPerEss80211StatsTotalUnicastTxBytes_Object = MibTableColumn
mwPerEss80211StatsTotalUnicastTxBytes = _MwPerEss80211StatsTotalUnicastTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 22),
    _MwPerEss80211StatsTotalUnicastTxBytes_Type()
)
mwPerEss80211StatsTotalUnicastTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalUnicastTxBytes.setStatus("current")
_MwPerEss80211StatsTotalBroadcastDataBytes_Type = Counter64
_MwPerEss80211StatsTotalBroadcastDataBytes_Object = MibTableColumn
mwPerEss80211StatsTotalBroadcastDataBytes = _MwPerEss80211StatsTotalBroadcastDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 23),
    _MwPerEss80211StatsTotalBroadcastDataBytes_Type()
)
mwPerEss80211StatsTotalBroadcastDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalBroadcastDataBytes.setStatus("current")
_MwPerEss80211StatsTotalMulticastDataBytes_Type = Counter64
_MwPerEss80211StatsTotalMulticastDataBytes_Object = MibTableColumn
mwPerEss80211StatsTotalMulticastDataBytes = _MwPerEss80211StatsTotalMulticastDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 24),
    _MwPerEss80211StatsTotalMulticastDataBytes_Type()
)
mwPerEss80211StatsTotalMulticastDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsTotalMulticastDataBytes.setStatus("current")
_MwPerEss80211StatsAssociatedStationNum_Type = Integer32
_MwPerEss80211StatsAssociatedStationNum_Object = MibTableColumn
mwPerEss80211StatsAssociatedStationNum = _MwPerEss80211StatsAssociatedStationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 39),
    _MwPerEss80211StatsAssociatedStationNum_Type()
)
mwPerEss80211StatsAssociatedStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsAssociatedStationNum.setStatus("current")
_MwPerEss80211StatsAssociated11bStationNum_Type = Integer32
_MwPerEss80211StatsAssociated11bStationNum_Object = MibTableColumn
mwPerEss80211StatsAssociated11bStationNum = _MwPerEss80211StatsAssociated11bStationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 40),
    _MwPerEss80211StatsAssociated11bStationNum_Type()
)
mwPerEss80211StatsAssociated11bStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsAssociated11bStationNum.setStatus("current")
_MwPerEss80211StatsAssociated11bgStationNum_Type = Integer32
_MwPerEss80211StatsAssociated11bgStationNum_Object = MibTableColumn
mwPerEss80211StatsAssociated11bgStationNum = _MwPerEss80211StatsAssociated11bgStationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 41),
    _MwPerEss80211StatsAssociated11bgStationNum_Type()
)
mwPerEss80211StatsAssociated11bgStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsAssociated11bgStationNum.setStatus("current")
_MwPerEss80211StatsAssociated11bgn1StationNum_Type = Integer32
_MwPerEss80211StatsAssociated11bgn1StationNum_Object = MibTableColumn
mwPerEss80211StatsAssociated11bgn1StationNum = _MwPerEss80211StatsAssociated11bgn1StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 42),
    _MwPerEss80211StatsAssociated11bgn1StationNum_Type()
)
mwPerEss80211StatsAssociated11bgn1StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsAssociated11bgn1StationNum.setStatus("current")
_MwPerEss80211StatsAssociated11bgn2StationNum_Type = Integer32
_MwPerEss80211StatsAssociated11bgn2StationNum_Object = MibTableColumn
mwPerEss80211StatsAssociated11bgn2StationNum = _MwPerEss80211StatsAssociated11bgn2StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 43),
    _MwPerEss80211StatsAssociated11bgn2StationNum_Type()
)
mwPerEss80211StatsAssociated11bgn2StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsAssociated11bgn2StationNum.setStatus("current")
_MwPerEss80211StatsAssociated11bgn3StationNum_Type = Integer32
_MwPerEss80211StatsAssociated11bgn3StationNum_Object = MibTableColumn
mwPerEss80211StatsAssociated11bgn3StationNum = _MwPerEss80211StatsAssociated11bgn3StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 44),
    _MwPerEss80211StatsAssociated11bgn3StationNum_Type()
)
mwPerEss80211StatsAssociated11bgn3StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsAssociated11bgn3StationNum.setStatus("current")
_MwPerEss80211StatsAssociated11aStationNum_Type = Integer32
_MwPerEss80211StatsAssociated11aStationNum_Object = MibTableColumn
mwPerEss80211StatsAssociated11aStationNum = _MwPerEss80211StatsAssociated11aStationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 45),
    _MwPerEss80211StatsAssociated11aStationNum_Type()
)
mwPerEss80211StatsAssociated11aStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsAssociated11aStationNum.setStatus("current")
_MwPerEss80211StatsAssociated11an1StationNum_Type = Integer32
_MwPerEss80211StatsAssociated11an1StationNum_Object = MibTableColumn
mwPerEss80211StatsAssociated11an1StationNum = _MwPerEss80211StatsAssociated11an1StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 46),
    _MwPerEss80211StatsAssociated11an1StationNum_Type()
)
mwPerEss80211StatsAssociated11an1StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsAssociated11an1StationNum.setStatus("current")
_MwPerEss80211StatsAssociated11an2StationNum_Type = Integer32
_MwPerEss80211StatsAssociated11an2StationNum_Object = MibTableColumn
mwPerEss80211StatsAssociated11an2StationNum = _MwPerEss80211StatsAssociated11an2StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 47),
    _MwPerEss80211StatsAssociated11an2StationNum_Type()
)
mwPerEss80211StatsAssociated11an2StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsAssociated11an2StationNum.setStatus("current")
_MwPerEss80211StatsAssociated11an3StationNum_Type = Integer32
_MwPerEss80211StatsAssociated11an3StationNum_Object = MibTableColumn
mwPerEss80211StatsAssociated11an3StationNum = _MwPerEss80211StatsAssociated11an3StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 17, 1, 48),
    _MwPerEss80211StatsAssociated11an3StationNum_Type()
)
mwPerEss80211StatsAssociated11an3StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwPerEss80211StatsAssociated11an3StationNum.setStatus("current")
_MwEssStatsSummaryTable_Object = MibTable
mwEssStatsSummaryTable = _MwEssStatsSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18)
)
if mibBuilder.loadTexts:
    mwEssStatsSummaryTable.setStatus("current")
_MwEssStatsSummaryEntry_Object = MibTableRow
mwEssStatsSummaryEntry = _MwEssStatsSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1)
)
mwEssStatsSummaryEntry.setIndexNames(
    (0, "MERU-GLOBAL-STATISTICS-MIB", "mwEssStatsSummaryTableIndex"),
)
if mibBuilder.loadTexts:
    mwEssStatsSummaryEntry.setStatus("current")
_MwEssStatsSummaryTableIndex_Type = Integer32
_MwEssStatsSummaryTableIndex_Object = MibTableColumn
mwEssStatsSummaryTableIndex = _MwEssStatsSummaryTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 1),
    _MwEssStatsSummaryTableIndex_Type()
)
mwEssStatsSummaryTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwEssStatsSummaryTableIndex.setStatus("current")


class _MwEssStatsSummaryEssId_Type(DisplayString):
    """Custom type mwEssStatsSummaryEssId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MwEssStatsSummaryEssId_Type.__name__ = "DisplayString"
_MwEssStatsSummaryEssId_Object = MibTableColumn
mwEssStatsSummaryEssId = _MwEssStatsSummaryEssId_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 2),
    _MwEssStatsSummaryEssId_Type()
)
mwEssStatsSummaryEssId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryEssId.setStatus("current")
_MwEssStatsSummaryRFBand_Type = MwlBandType
_MwEssStatsSummaryRFBand_Object = MibTableColumn
mwEssStatsSummaryRFBand = _MwEssStatsSummaryRFBand_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 3),
    _MwEssStatsSummaryRFBand_Type()
)
mwEssStatsSummaryRFBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mwEssStatsSummaryRFBand.setStatus("current")
_MwEssStatsSummaryRadioCount_Type = Integer32
_MwEssStatsSummaryRadioCount_Object = MibTableColumn
mwEssStatsSummaryRadioCount = _MwEssStatsSummaryRadioCount_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 4),
    _MwEssStatsSummaryRadioCount_Type()
)
mwEssStatsSummaryRadioCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryRadioCount.setStatus("current")
_MwEssStatsSummaryRxThroughput_Type = Unsigned32
_MwEssStatsSummaryRxThroughput_Object = MibTableColumn
mwEssStatsSummaryRxThroughput = _MwEssStatsSummaryRxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 5),
    _MwEssStatsSummaryRxThroughput_Type()
)
mwEssStatsSummaryRxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryRxThroughput.setStatus("current")
_MwEssStatsSummaryTxThroughput_Type = Unsigned32
_MwEssStatsSummaryTxThroughput_Object = MibTableColumn
mwEssStatsSummaryTxThroughput = _MwEssStatsSummaryTxThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 6),
    _MwEssStatsSummaryTxThroughput_Type()
)
mwEssStatsSummaryTxThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryTxThroughput.setStatus("current")
_MwEssStatsSummaryTotalThroughput_Type = Unsigned32
_MwEssStatsSummaryTotalThroughput_Object = MibTableColumn
mwEssStatsSummaryTotalThroughput = _MwEssStatsSummaryTotalThroughput_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 7),
    _MwEssStatsSummaryTotalThroughput_Type()
)
mwEssStatsSummaryTotalThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryTotalThroughput.setStatus("current")
_MwEssStatsSummaryTotalStationNum_Type = Integer32
_MwEssStatsSummaryTotalStationNum_Object = MibTableColumn
mwEssStatsSummaryTotalStationNum = _MwEssStatsSummaryTotalStationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 10),
    _MwEssStatsSummaryTotalStationNum_Type()
)
mwEssStatsSummaryTotalStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryTotalStationNum.setStatus("current")
_MwEssStatsSummaryBStationNum_Type = Integer32
_MwEssStatsSummaryBStationNum_Object = MibTableColumn
mwEssStatsSummaryBStationNum = _MwEssStatsSummaryBStationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 11),
    _MwEssStatsSummaryBStationNum_Type()
)
mwEssStatsSummaryBStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryBStationNum.setStatus("current")
_MwEssStatsSummaryBGStationNum_Type = Integer32
_MwEssStatsSummaryBGStationNum_Object = MibTableColumn
mwEssStatsSummaryBGStationNum = _MwEssStatsSummaryBGStationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 12),
    _MwEssStatsSummaryBGStationNum_Type()
)
mwEssStatsSummaryBGStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryBGStationNum.setStatus("current")
_MwEssStatsSummaryGN1StationNum_Type = Integer32
_MwEssStatsSummaryGN1StationNum_Object = MibTableColumn
mwEssStatsSummaryGN1StationNum = _MwEssStatsSummaryGN1StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 13),
    _MwEssStatsSummaryGN1StationNum_Type()
)
mwEssStatsSummaryGN1StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryGN1StationNum.setStatus("current")
_MwEssStatsSummaryGN2StationNum_Type = Integer32
_MwEssStatsSummaryGN2StationNum_Object = MibTableColumn
mwEssStatsSummaryGN2StationNum = _MwEssStatsSummaryGN2StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 14),
    _MwEssStatsSummaryGN2StationNum_Type()
)
mwEssStatsSummaryGN2StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryGN2StationNum.setStatus("current")
_MwEssStatsSummaryGN3StationNum_Type = Integer32
_MwEssStatsSummaryGN3StationNum_Object = MibTableColumn
mwEssStatsSummaryGN3StationNum = _MwEssStatsSummaryGN3StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 15),
    _MwEssStatsSummaryGN3StationNum_Type()
)
mwEssStatsSummaryGN3StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryGN3StationNum.setStatus("current")
_MwEssStatsSummaryAStationNum_Type = Integer32
_MwEssStatsSummaryAStationNum_Object = MibTableColumn
mwEssStatsSummaryAStationNum = _MwEssStatsSummaryAStationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 16),
    _MwEssStatsSummaryAStationNum_Type()
)
mwEssStatsSummaryAStationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryAStationNum.setStatus("current")
_MwEssStatsSummaryAN1StationNum_Type = Integer32
_MwEssStatsSummaryAN1StationNum_Object = MibTableColumn
mwEssStatsSummaryAN1StationNum = _MwEssStatsSummaryAN1StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 17),
    _MwEssStatsSummaryAN1StationNum_Type()
)
mwEssStatsSummaryAN1StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryAN1StationNum.setStatus("current")
_MwEssStatsSummaryAN2StationNum_Type = Integer32
_MwEssStatsSummaryAN2StationNum_Object = MibTableColumn
mwEssStatsSummaryAN2StationNum = _MwEssStatsSummaryAN2StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 18),
    _MwEssStatsSummaryAN2StationNum_Type()
)
mwEssStatsSummaryAN2StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryAN2StationNum.setStatus("current")
_MwEssStatsSummaryAN3StationNum_Type = Integer32
_MwEssStatsSummaryAN3StationNum_Object = MibTableColumn
mwEssStatsSummaryAN3StationNum = _MwEssStatsSummaryAN3StationNum_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 3, 1, 18, 1, 19),
    _MwEssStatsSummaryAN3StationNum_Type()
)
mwEssStatsSummaryAN3StationNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwEssStatsSummaryAN3StationNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-GLOBAL-STATISTICS-MIB",
    **{"mwGlobalStatistics": mwGlobalStatistics,
       "mwIf80211StatsTable": mwIf80211StatsTable,
       "mwIf80211StatsEntry": mwIf80211StatsEntry,
       "mwIf80211StatsTableIndex": mwIf80211StatsTableIndex,
       "mwIf80211StatsNodeId": mwIf80211StatsNodeId,
       "mwIf80211StatsIfIndex": mwIf80211StatsIfIndex,
       "mwIf80211StatsNodeName": mwIf80211StatsNodeName,
       "mwIf80211StatsThroughput": mwIf80211StatsThroughput,
       "mwIf80211StatsNoiseLevel": mwIf80211StatsNoiseLevel,
       "mwIf80211StatsFailedCount": mwIf80211StatsFailedCount,
       "mwIf80211StatsTxFragCount": mwIf80211StatsTxFragCount,
       "mwIf80211StatsRxByteCount": mwIf80211StatsRxByteCount,
       "mwIf80211StatsTxByteCount": mwIf80211StatsTxByteCount,
       "mwIf80211StatsIfRetryCount": mwIf80211StatsIfRetryCount,
       "mwIf80211StatsTxFrameCount": mwIf80211StatsTxFrameCount,
       "mwIf80211StatsRcvFragCount": mwIf80211StatsRcvFragCount,
       "mwIf80211StatsTxAMSDUCount": mwIf80211StatsTxAMSDUCount,
       "mwIf80211StatsRxAMSDUCount": mwIf80211StatsRxAMSDUCount,
       "mwIf80211StatsTxAMPDUCount": mwIf80211StatsTxAMPDUCount,
       "mwIf80211StatsRxAMPDUCount": mwIf80211StatsRxAMPDUCount,
       "mwIf80211StatsFrameDupCount": mwIf80211StatsFrameDupCount,
       "mwIf80211StatsFcsErrorCount": mwIf80211StatsFcsErrorCount,
       "mwIf80211StatsPlcpErrorCount": mwIf80211StatsPlcpErrorCount,
       "mwIf80211StatsLossPercentage": mwIf80211StatsLossPercentage,
       "mwIf80211StatsRtsSuccessCount": mwIf80211StatsRtsSuccessCount,
       "mwIf80211StatsRtsFailureCount": mwIf80211StatsRtsFailureCount,
       "mwIf80211StatsAckFailureCount": mwIf80211StatsAckFailureCount,
       "mwIf80211StatsRetryAMSDUCount": mwIf80211StatsRetryAMSDUCount,
       "mwIf80211StatsTxRetryCountBAR": mwIf80211StatsTxRetryCountBAR,
       "mwIf80211StatsFailedAMSDUCount": mwIf80211StatsFailedAMSDUCount,
       "mwIf80211StatsPSMPSuccessCount": mwIf80211StatsPSMPSuccessCount,
       "mwIf80211StatsPSMPFailureCount": mwIf80211StatsPSMPFailureCount,
       "mwIf80211StatsBeamformingCount": mwIf80211StatsBeamformingCount,
       "mwIf80211StatsMcastTxFrameCount": mwIf80211StatsMcastTxFrameCount,
       "mwIf80211StatsQosCFPollsRxCount": mwIf80211StatsQosCFPollsRxCount,
       "mwIf80211StatsAMSDUAckFailCount": mwIf80211StatsAMSDUAckFailCount,
       "mwIf80211StatsFrame20MhzTxCount": mwIf80211StatsFrame20MhzTxCount,
       "mwIf80211StatsFrame40MhzTxCount": mwIf80211StatsFrame40MhzTxCount,
       "mwIf80211StatsFrame20MhzRxCount": mwIf80211StatsFrame20MhzRxCount,
       "mwIf80211StatsFrame40MhzRxCount": mwIf80211StatsFrame40MhzRxCount,
       "mwIf80211StatsGrantRDGUsedCount": mwIf80211StatsGrantRDGUsedCount,
       "mwIf80211StatsMultipleRetryCount": mwIf80211StatsMultipleRetryCount,
       "mwIf80211StatsMcastRcvFrameCount": mwIf80211StatsMcastRcvFrameCount,
       "mwIf80211StatsChannelUtilization": mwIf80211StatsChannelUtilization,
       "mwIf80211StatsTxMPDUInAMPDUCount": mwIf80211StatsTxMPDUInAMPDUCount,
       "mwIf80211StatsMPDUInRxAMPDUCount": mwIf80211StatsMPDUInRxAMPDUCount,
       "mwIf80211StatsTxRetryCountUnaggr": mwIf80211StatsTxRetryCountUnaggr,
       "mwIf80211StatsRxRetriedFrameCount": mwIf80211StatsRxRetriedFrameCount,
       "mwIf80211StatsRxUnicastFrameCount": mwIf80211StatsRxUnicastFrameCount,
       "mwIf80211StatsQosCFPollsLostCount": mwIf80211StatsQosCFPollsLostCount,
       "mwIf80211StatsGrantRDGUnusedCount": mwIf80211StatsGrantRDGUnusedCount,
       "mwIf80211StatsDualCTSSuccessCount": mwIf80211StatsDualCTSSuccessCount,
       "mwIf80211StatsDualCTSFailureCount": mwIf80211StatsDualCTSFailureCount,
       "mwIf80211StatsSTBCCTSSuccessCount": mwIf80211StatsSTBCCTSSuccessCount,
       "mwIf80211StatsSTBCCTSFailureCount": mwIf80211StatsSTBCCTSFailureCount,
       "mwIf80211StatsRTSLSIGSuccessCount": mwIf80211StatsRTSLSIGSuccessCount,
       "mwIf80211StatsRTSLSIGFailureCount": mwIf80211StatsRTSLSIGFailureCount,
       "mwIf80211StatsAssignedStationCount": mwIf80211StatsAssignedStationCount,
       "mwIf80211StatsMultiRetryAMSDUCount": mwIf80211StatsMultiRetryAMSDUCount,
       "mwIf80211StatsTxOctetsInAMSDUCount": mwIf80211StatsTxOctetsInAMSDUCount,
       "mwIf80211StatsRxOctetsInAMSDUCount": mwIf80211StatsRxOctetsInAMSDUCount,
       "mwIf80211StatsTxOctetsInAMPDUCount": mwIf80211StatsTxOctetsInAMPDUCount,
       "mwIf80211StatsRxOctetsInAMPDUCount": mwIf80211StatsRxOctetsInAMPDUCount,
       "mwIf80211StatsImplicitBARFailCount": mwIf80211StatsImplicitBARFailCount,
       "mwIf80211StatsExplicitBARFailCount": mwIf80211StatsExplicitBARFailCount,
       "mwIf80211StatsChanWidthSwitchCount": mwIf80211StatsChanWidthSwitchCount,
       "mwIf80211StatsTxMultiRetryCountBAR": mwIf80211StatsTxMultiRetryCountBAR,
       "mwIf80211StatsWepUndecryptableCount": mwIf80211StatsWepUndecryptableCount,
       "mwIf80211StatsQosDiscardedFragCount": mwIf80211StatsQosDiscardedFragCount,
       "mwIf80211StatsQosCFPollsUnusedCount": mwIf80211StatsQosCFPollsUnusedCount,
       "mwIf80211StatsAMPDUDelCRCErrorCount": mwIf80211StatsAMPDUDelCRCErrorCount,
       "mwIf80211StatsTxRetryCountSubfrAggr": mwIf80211StatsTxRetryCountSubfrAggr,
       "mwIf80211StatsAssociatedStationCount": mwIf80211StatsAssociatedStationCount,
       "mwIf80211StatsDiscoveredStationCount": mwIf80211StatsDiscoveredStationCount,
       "mwIf80211StatsTxFrameInGrantRDGCount": mwIf80211StatsTxFrameInGrantRDGCount,
       "mwIf80211StatsTxOctetInGrantRDGCount": mwIf80211StatsTxOctetInGrantRDGCount,
       "mwIf80211StatsNonSTBCCTSSuccessCount": mwIf80211StatsNonSTBCCTSSuccessCount,
       "mwIf80211StatsNonSTBCCTSFailureCount": mwIf80211StatsNonSTBCCTSFailureCount,
       "mwIf80211StatsTxRetryLimitExCountBAR": mwIf80211StatsTxRetryLimitExCountBAR,
       "mwIf80211StatsQosCFPollsUnusableCount": mwIf80211StatsQosCFPollsUnusableCount,
       "mwIf80211StatsTxRetryLimitExCountAggr": mwIf80211StatsTxRetryLimitExCountAggr,
       "mwIf80211StatsTxMultiRetryCountUnaggr": mwIf80211StatsTxMultiRetryCountUnaggr,
       "mwIf80211StatsTxRetryLimitExCountUnaggr": mwIf80211StatsTxRetryLimitExCountUnaggr,
       "mwIf80211StatsTxMultiRetryCountSubfrAggr": mwIf80211StatsTxMultiRetryCountSubfrAggr,
       "mwIf80211StatsTxRetryLimitExCountSubfrAggr": mwIf80211StatsTxRetryLimitExCountSubfrAggr,
       "mwIf80211StatsUnicastBeaconLossThrExceeded": mwIf80211StatsUnicastBeaconLossThrExceeded,
       "mwIf80211StatsTxFailedHwRetryExceeded": mwIf80211StatsTxFailedHwRetryExceeded,
       "mwIf80211StatsRxDataForAssignedStations": mwIf80211StatsRxDataForAssignedStations,
       "mwIf80211StatsRxMgmtFramesForAssignedStations": mwIf80211StatsRxMgmtFramesForAssignedStations,
       "mwIf80211StatsTotalRxMgmtFrames": mwIf80211StatsTotalRxMgmtFrames,
       "mwIf80211StatsTotalRxControlFrames": mwIf80211StatsTotalRxControlFrames,
       "mwIf80211StatsMgmtFrameOverheadInAirtime": mwIf80211StatsMgmtFrameOverheadInAirtime,
       "mwIf80211StatsTxUnicastFrameCount": mwIf80211StatsTxUnicastFrameCount,
       "mwIf80211StatsRxAllDataFrameCount": mwIf80211StatsRxAllDataFrameCount,
       "mwIf80211StatsRfBarrierActions": mwIf80211StatsRfBarrierActions,
       "mwIf80211StatsBeaconOverhead": mwIf80211StatsBeaconOverhead,
       "mwIf80211StatsProbeReqRespOverhead": mwIf80211StatsProbeReqRespOverhead,
       "mwIf80211StatsNeighborhoodCounter": mwIf80211StatsNeighborhoodCounter,
       "mwIf80211StatsPotentialBeaconCollisionCounter": mwIf80211StatsPotentialBeaconCollisionCounter,
       "mwIf80211StatsProfileBeaconDataRate": mwIf80211StatsProfileBeaconDataRate,
       "mwIf80211StatsRetryPercentage": mwIf80211StatsRetryPercentage,
       "mwIf80211StatsChannel": mwIf80211StatsChannel,
       "mwIf80211StatsRowStatus": mwIf80211StatsRowStatus,
       "mwIfStatsTable": mwIfStatsTable,
       "mwIfStatsEntry": mwIfStatsEntry,
       "mwIfStatsTableIndex": mwIfStatsTableIndex,
       "mwIfStatsIfIndex": mwIfStatsIfIndex,
       "mwIfStatsIfDescr": mwIfStatsIfDescr,
       "mwIfStatsIfNodeId": mwIfStatsIfNodeId,
       "mwIfStatsIfOutQLen": mwIfStatsIfOutQLen,
       "mwIfStatsIfNodeName": mwIfStatsIfNodeName,
       "mwIfStatsIfNodeType": mwIfStatsIfNodeType,
       "mwIfStatsIfInOctets": mwIfStatsIfInOctets,
       "mwIfStatsIfInErrors": mwIfStatsIfInErrors,
       "mwIfStatsIfOutOctets": mwIfStatsIfOutOctets,
       "mwIfStatsIfOutErrors": mwIfStatsIfOutErrors,
       "mwIfStatsIfInDiscards": mwIfStatsIfInDiscards,
       "mwIfStatsIfInUcastPkts": mwIfStatsIfInUcastPkts,
       "mwIfStatsIfOutDiscards": mwIfStatsIfOutDiscards,
       "mwIfStatsIfInNUcastPkts": mwIfStatsIfInNUcastPkts,
       "mwIfStatsIfOutUcastPkts": mwIfStatsIfOutUcastPkts,
       "mwIfStatsIfOutNUcastPkts": mwIfStatsIfOutNUcastPkts,
       "mwIfStatsIfInUnknownProtos": mwIfStatsIfInUnknownProtos,
       "mwIfStatsRowStatus": mwIfStatsRowStatus,
       "mwAuthStats": mwAuthStats,
       "mwAuthStatsAuth8021xRequestCount": mwAuthStatsAuth8021xRequestCount,
       "mwAuthStatsAuth8021xSuccessCount": mwAuthStatsAuth8021xSuccessCount,
       "mwAuthStatsAuth8021xFailureCount": mwAuthStatsAuth8021xFailureCount,
       "mwAuthStatsAuth8021xStationCount": mwAuthStatsAuth8021xStationCount,
       "mwQosStats": mwQosStats,
       "mwQosStatsSessionCount": mwQosStatsSessionCount,
       "mwQosStatsH323SessionCount": mwQosStatsH323SessionCount,
       "mwQosStatsSipSessionCount": mwQosStatsSipSessionCount,
       "mwQosStatsSccpSessionCount": mwQosStatsSccpSessionCount,
       "mwQosStatsRejectedSessionCount": mwQosStatsRejectedSessionCount,
       "mwQosStatsRejectedH323SessionCount": mwQosStatsRejectedH323SessionCount,
       "mwQosStatsRejectedSipSessionCount": mwQosStatsRejectedSipSessionCount,
       "mwQosStatsRejectedSccpSessionCount": mwQosStatsRejectedSccpSessionCount,
       "mwQosStatsPendingSessionCount": mwQosStatsPendingSessionCount,
       "mwQosStatsH323PendingSessionCount": mwQosStatsH323PendingSessionCount,
       "mwQosStatsSipPendingSessionCount": mwQosStatsSipPendingSessionCount,
       "mwQosStatsSccpPendingSessionCount": mwQosStatsSccpPendingSessionCount,
       "mwQosStatsQosActiveFlowCount": mwQosStatsQosActiveFlowCount,
       "mwQosStatsQosPendingFlowCount": mwQosStatsQosPendingFlowCount,
       "mwStationStatsTable": mwStationStatsTable,
       "mwStationStatsEntry": mwStationStatsEntry,
       "mwStationStatsTableIndex": mwStationStatsTableIndex,
       "mwStationStatsMacAddress": mwStationStatsMacAddress,
       "mwStationStatsDhcpRequestCount": mwStationStatsDhcpRequestCount,
       "mwStationStatsSipVideoBandwidth": mwStationStatsSipVideoBandwidth,
       "mwStationStatsSipVideoFlowCount": mwStationStatsSipVideoFlowCount,
       "mwStationStatsSipAudioBandwidth": mwStationStatsSipAudioBandwidth,
       "mwStationStatsSipAudioFlowCount": mwStationStatsSipAudioFlowCount,
       "mwStationStatsAddressChangeCount": mwStationStatsAddressChangeCount,
       "mwStationStatsQosActiveFlowCount": mwStationStatsQosActiveFlowCount,
       "mwStationStatsH323VideoBandwidth": mwStationStatsH323VideoBandwidth,
       "mwStationStatsH323VideoFlowCount": mwStationStatsH323VideoFlowCount,
       "mwStationStatsH323AudioBandwidth": mwStationStatsH323AudioBandwidth,
       "mwStationStatsH323AudioFlowCount": mwStationStatsH323AudioFlowCount,
       "mwStationStatsSccpVideoBandwidth": mwStationStatsSccpVideoBandwidth,
       "mwStationStatsSccpVideoFlowCount": mwStationStatsSccpVideoFlowCount,
       "mwStationStatsSccpAudioBandwidth": mwStationStatsSccpAudioBandwidth,
       "mwStationStatsSccpAudioFlowCount": mwStationStatsSccpAudioFlowCount,
       "mwStationStatsQosPendingFlowCount": mwStationStatsQosPendingFlowCount,
       "mwStationStatsSipVideoRsvBandwidth": mwStationStatsSipVideoRsvBandwidth,
       "mwStationStatsSipAudioRsvBandwidth": mwStationStatsSipAudioRsvBandwidth,
       "mwStationStatsVoluntaryHandoffCount": mwStationStatsVoluntaryHandoffCount,
       "mwStationStatsH323VideoRsvBandwidth": mwStationStatsH323VideoRsvBandwidth,
       "mwStationStatsH323AudioRsvBandwidth": mwStationStatsH323AudioRsvBandwidth,
       "mwStationStatsSccpVideoRsvBandwidth": mwStationStatsSccpVideoRsvBandwidth,
       "mwStationStatsSccpAudioRsvBandwidth": mwStationStatsSccpAudioRsvBandwidth,
       "mwStationStatsInvoluntaryHandoffCount": mwStationStatsInvoluntaryHandoffCount,
       "mwApStationStatsTable": mwApStationStatsTable,
       "mwApStationStatsEntry": mwApStationStatsEntry,
       "mwApStationStatsTableIndex": mwApStationStatsTableIndex,
       "mwApStationStatsEssId": mwApStationStatsEssId,
       "mwApStationStatsBssId": mwApStationStatsBssId,
       "mwApStationStatsApName": mwApStationStatsApName,
       "mwApStationStatsIfIndex": mwApStationStatsIfIndex,
       "mwApStationStatsWepErrors": mwApStationStatsWepErrors,
       "mwApStationStatsRxDataRate": mwApStationStatsRxDataRate,
       "mwApStationStatsTxDataRate": mwApStationStatsTxDataRate,
       "mwApStationStatsNmsApNodeId": mwApStationStatsNmsApNodeId,
       "mwApStationStatsRxByteCount": mwApStationStatsRxByteCount,
       "mwApStationStatsTxByteCount": mwApStationStatsTxByteCount,
       "mwApStationStatsRxPacketCount": mwApStationStatsRxPacketCount,
       "mwApStationStatsTxPacketCount": mwApStationStatsTxPacketCount,
       "mwApStationStatsTxAckMissCount": mwApStationStatsTxAckMissCount,
       "mwApStationStatsDhcpErrorCount": mwApStationStatsDhcpErrorCount,
       "mwApStationStatsRxFcsErrorCount": mwApStationStatsRxFcsErrorCount,
       "mwApStationStatsStationIPAddress": mwApStationStatsStationIPAddress,
       "mwApStationStatsRxDuplicateCount": mwApStationStatsRxDuplicateCount,
       "mwApStationStatsDhcpRequestCount": mwApStationStatsDhcpRequestCount,
       "mwApStationStatsStationMacAddress": mwApStationStatsStationMacAddress,
       "mwApStationStatsChannelUtilization": mwApStationStatsChannelUtilization,
       "mwApStationStatsRxRetriedFrameCount": mwApStationStatsRxRetriedFrameCount,
       "mwApStationStatsRxAverageAggrLength": mwApStationStatsRxAverageAggrLength,
       "mwApStationStatsTxAverageAggrLength": mwApStationStatsTxAverageAggrLength,
       "mwApStationStatsTotalPowerSaveTransitions": mwApStationStatsTotalPowerSaveTransitions,
       "mwApStationStatsStationQueueOverflow": mwApStationStatsStationQueueOverflow,
       "mwApStationStatsPowerSaveQueueOverflow": mwApStationStatsPowerSaveQueueOverflow,
       "mwApStationStatsPSPollFramesRxCount": mwApStationStatsPSPollFramesRxCount,
       "mwApStationStatsSWEncryptionFramesCount": mwApStationStatsSWEncryptionFramesCount,
       "mwApStationStatsSWDecryptionFramesCount": mwApStationStatsSWDecryptionFramesCount,
       "mwApStationStatsLRUSwapCounter": mwApStationStatsLRUSwapCounter,
       "mwApStationStatsTxFailedHwRetryExceeded": mwApStationStatsTxFailedHwRetryExceeded,
       "mwCacApStatsTable": mwCacApStatsTable,
       "mwCacApStatsEntry": mwCacApStatsEntry,
       "mwCacApStatsTableIndex": mwCacApStatsTableIndex,
       "mwCacApStatsNmsApNodeId": mwCacApStatsNmsApNodeId,
       "mwCacApStatsCurrentCalls": mwCacApStatsCurrentCalls,
       "mwCacApStatsRejectedCalls": mwCacApStatsRejectedCalls,
       "mwCacBssStatsTable": mwCacBssStatsTable,
       "mwCacBssStatsEntry": mwCacBssStatsEntry,
       "mwCacBssStatsTableIndex": mwCacBssStatsTableIndex,
       "mwCacBssStatsBssId": mwCacBssStatsBssId,
       "mwCacBssStatsCurrentCalls": mwCacBssStatsCurrentCalls,
       "mwCacBssStatsRejectedCalls": mwCacBssStatsRejectedCalls,
       "mwRf6DiagStatsTable": mwRf6DiagStatsTable,
       "mwRf6DiagStatsEntry": mwRf6DiagStatsEntry,
       "mwRf6DiagStatsTableIndex": mwRf6DiagStatsTableIndex,
       "mwRf6DiagStatsNodeId": mwRf6DiagStatsNodeId,
       "mwRf6DiagStatsIfIndex": mwRf6DiagStatsIfIndex,
       "mwRf6DiagStatsNodeName": mwRf6DiagStatsNodeName,
       "mwRf6DiagStatsFatalHwErrorINTs": mwRf6DiagStatsFatalHwErrorINTs,
       "mwRf6DiagStatsBeaconMissCount": mwRf6DiagStatsBeaconMissCount,
       "mwRf6DiagStatsBeaconBufferNullCount": mwRf6DiagStatsBeaconBufferNullCount,
       "mwRf6DiagStatsNoSkBufferForBeacon": mwRf6DiagStatsNoSkBufferForBeacon,
       "mwRf6DiagStatsTxUnderrunINTs": mwRf6DiagStatsTxUnderrunINTs,
       "mwRf6DiagStatsTxTimeoutINTs": mwRf6DiagStatsTxTimeoutINTs,
       "mwRf6DiagStatsTxFailedByNoTxBuffer": mwRf6DiagStatsTxFailedByNoTxBuffer,
       "mwRf6DiagStatsTxFailedByFIFOUnderrun": mwRf6DiagStatsTxFailedByFIFOUnderrun,
       "mwRf6DiagStatsTxAggrDescriptorConfigError": mwRf6DiagStatsTxAggrDescriptorConfigError,
       "mwRf6DiagStatsTxAggrDataUnderrun": mwRf6DiagStatsTxAggrDataUnderrun,
       "mwRf6DiagStatsTxAggrDelimiterUnderrun": mwRf6DiagStatsTxAggrDelimiterUnderrun,
       "mwRf6DiagStatsTotalTidResetCnt": mwRf6DiagStatsTotalTidResetCnt,
       "mwRf6DiagStatsCarrierSenseTimeoutINTs": mwRf6DiagStatsCarrierSenseTimeoutINTs,
       "mwRf6DiagStatsIsSlamTxNoAckAddr": mwRf6DiagStatsIsSlamTxNoAckAddr,
       "mwRf6DiagStatsRxOverrunINTs": mwRf6DiagStatsRxOverrunINTs,
       "mwRf6DiagStatsRxEolINTs": mwRf6DiagStatsRxEolINTs,
       "mwRf6DiagStatsRxPacketsBadVersion": mwRf6DiagStatsRxPacketsBadVersion,
       "mwRf6DiagStatsRadioResetBeaconStuck": mwRf6DiagStatsRadioResetBeaconStuck,
       "mwRf6DiagStatsRadioResetTPScale": mwRf6DiagStatsRadioResetTPScale,
       "mwRf6DiagStatsRadioResetFatalTasklet": mwRf6DiagStatsRadioResetFatalTasklet,
       "mwRf6DiagStatsRadioResetRxornTasklet": mwRf6DiagStatsRadioResetRxornTasklet,
       "mwRf6DiagStatsRadioResetCalibrate": mwRf6DiagStatsRadioResetCalibrate,
       "mwRf6DiagStatsRadioResetTxAntennaSwitch": mwRf6DiagStatsRadioResetTxAntennaSwitch,
       "mwRf6DiagStatsRadioResetRxChain": mwRf6DiagStatsRadioResetRxChain,
       "mwRf6DiagStatsRadioResetNoTxFrames": mwRf6DiagStatsRadioResetNoTxFrames,
       "mwRf6DiagStatsTotalRadioResetCnt": mwRf6DiagStatsTotalRadioResetCnt,
       "mwRf6DiagStatsRowStatus": mwRf6DiagStatsRowStatus,
       "mwAp1000DiagStatsTable": mwAp1000DiagStatsTable,
       "mwAp1000DiagStatsEntry": mwAp1000DiagStatsEntry,
       "mwAp1000DiagStatsTableIndex": mwAp1000DiagStatsTableIndex,
       "mwAp1000DiagStatsNodeId": mwAp1000DiagStatsNodeId,
       "mwAp1000DiagStatsIfIndex": mwAp1000DiagStatsIfIndex,
       "mwAp1000DiagStatsNodeName": mwAp1000DiagStatsNodeName,
       "mwAp1000DiagStatsFatalHwErrorINTs": mwAp1000DiagStatsFatalHwErrorINTs,
       "mwAp1000DiagStatsBeaconMissCount": mwAp1000DiagStatsBeaconMissCount,
       "mwAp1000DiagStatsTxUnderrunINTs": mwAp1000DiagStatsTxUnderrunINTs,
       "mwAp1000DiagStatsTxTimeoutINTs": mwAp1000DiagStatsTxTimeoutINTs,
       "mwAp1000DiagStatsTxFailedByNoTxBuffer": mwAp1000DiagStatsTxFailedByNoTxBuffer,
       "mwAp1000DiagStatsTxFailedByFIFOUnderrun": mwAp1000DiagStatsTxFailedByFIFOUnderrun,
       "mwAp1000DiagStatsTotalTidResetCnt": mwAp1000DiagStatsTotalTidResetCnt,
       "mwAp1000DiagStatsRxOverrunINTs": mwAp1000DiagStatsRxOverrunINTs,
       "mwAp1000DiagStatsRxEolINTs": mwAp1000DiagStatsRxEolINTs,
       "mwAp1000DiagStatsRxPacketsBadVersion": mwAp1000DiagStatsRxPacketsBadVersion,
       "mwAp1000DiagStatsTotalRadioResetCnt": mwAp1000DiagStatsTotalRadioResetCnt,
       "mwAp1000DiagStatsTxPhyError": mwAp1000DiagStatsTxPhyError,
       "mwAp1000DiagStatsRxNoBuf": mwAp1000DiagStatsRxNoBuf,
       "mwAp1000DiagStatsTxChanRej": mwAp1000DiagStatsTxChanRej,
       "mwAp1000DiagStatsDmaDE": mwAp1000DiagStatsDmaDE,
       "mwAp1000DiagStatsDmaDA": mwAp1000DiagStatsDmaDA,
       "mwAp1000DiagStatsTxTplunfl": mwAp1000DiagStatsTxTplunfl,
       "mwAp1000DiagStatsBcnTxFailed": mwAp1000DiagStatsBcnTxFailed,
       "mwAp1000DiagStatsTxError": mwAp1000DiagStatsTxError,
       "mwAp1000DiagStatsRxStuck": mwAp1000DiagStatsRxStuck,
       "mwAp1000DiagStatsRxError": mwAp1000DiagStatsRxError,
       "mwAp1000DiagStatsTxFfiFull": mwAp1000DiagStatsTxFfiFull,
       "mwAp1000DiagStatsTxDrop": mwAp1000DiagStatsTxDrop,
       "mwAp1000DiagStatsTxqOverflow": mwAp1000DiagStatsTxqOverflow,
       "mwAp1000DiagStatsPmgOverflow": mwAp1000DiagStatsPmgOverflow,
       "mwAp1000DiagStatsRxCgprqrm": mwAp1000DiagStatsRxCgprqrm,
       "mwAp1000DiagStatsRowStatus": mwAp1000DiagStatsRowStatus,
       "mwAp400DiagStatsTable": mwAp400DiagStatsTable,
       "mwAp400DiagStatsEntry": mwAp400DiagStatsEntry,
       "mwAp400DiagStatsTableIndex": mwAp400DiagStatsTableIndex,
       "mwAp400DiagStatsNodeId": mwAp400DiagStatsNodeId,
       "mwAp400DiagStatsIfIndex": mwAp400DiagStatsIfIndex,
       "mwAp400DiagStatsNodeName": mwAp400DiagStatsNodeName,
       "mwAp400DiagStatsFatalHwErrorINTs": mwAp400DiagStatsFatalHwErrorINTs,
       "mwAp400DiagStatsBeaconMissCount": mwAp400DiagStatsBeaconMissCount,
       "mwAp400DiagStatsBeaconBufferNullCount": mwAp400DiagStatsBeaconBufferNullCount,
       "mwAp400DiagStatsNoSkBufferForBeacon": mwAp400DiagStatsNoSkBufferForBeacon,
       "mwAp400DiagStatsTxUnderrunINTs": mwAp400DiagStatsTxUnderrunINTs,
       "mwAp400DiagStatsTxTimeoutINTs": mwAp400DiagStatsTxTimeoutINTs,
       "mwAp400DiagStatsTxFailedByNoTxBuffer": mwAp400DiagStatsTxFailedByNoTxBuffer,
       "mwAp400DiagStatsTxFailedByFIFOUnderrun": mwAp400DiagStatsTxFailedByFIFOUnderrun,
       "mwAp400DiagStatsTxAggrDescriptorConfigError": mwAp400DiagStatsTxAggrDescriptorConfigError,
       "mwAp400DiagStatsTxAggrDataUnderrun": mwAp400DiagStatsTxAggrDataUnderrun,
       "mwAp400DiagStatsTxAggrDelimiterUnderrun": mwAp400DiagStatsTxAggrDelimiterUnderrun,
       "mwAp400DiagStatsTotalTidResetCnt": mwAp400DiagStatsTotalTidResetCnt,
       "mwAp400DiagStatsCarrierSenseTimeoutINTs": mwAp400DiagStatsCarrierSenseTimeoutINTs,
       "mwAp400DiagStatsIsSlamTxNoAckAddr": mwAp400DiagStatsIsSlamTxNoAckAddr,
       "mwAp400DiagStatsRxOverrunINTs": mwAp400DiagStatsRxOverrunINTs,
       "mwAp400DiagStatsRxEolINTs": mwAp400DiagStatsRxEolINTs,
       "mwAp400DiagStatsRxPacketsBadVersion": mwAp400DiagStatsRxPacketsBadVersion,
       "mwAp400DiagStatsRadioResetBeaconStuck": mwAp400DiagStatsRadioResetBeaconStuck,
       "mwAp400DiagStatsRadioResetTPScale": mwAp400DiagStatsRadioResetTPScale,
       "mwAp400DiagStatsRadioResetFatalTasklet": mwAp400DiagStatsRadioResetFatalTasklet,
       "mwAp400DiagStatsRadioResetRxornTasklet": mwAp400DiagStatsRadioResetRxornTasklet,
       "mwAp400DiagStatsRadioResetCalibrate": mwAp400DiagStatsRadioResetCalibrate,
       "mwAp400DiagStatsRadioResetTxAntennaSwitch": mwAp400DiagStatsRadioResetTxAntennaSwitch,
       "mwAp400DiagStatsRadioResetRxChain": mwAp400DiagStatsRadioResetRxChain,
       "mwAp400DiagStatsRadioResetNoTxFrames": mwAp400DiagStatsRadioResetNoTxFrames,
       "mwAp400DiagStatsTotalRadioResetCnt": mwAp400DiagStatsTotalRadioResetCnt,
       "mwAp400DiagStatsRxPhyError": mwAp400DiagStatsRxPhyError,
       "mwAp400DiagStatsRowStatus": mwAp400DiagStatsRowStatus,
       "mwSystemGeneral": mwSystemGeneral,
       "mwSystemGeneralName": mwSystemGeneralName,
       "mwSystemGeneralModel": mwSystemGeneralModel,
       "mwSystemGeneralVersion": mwSystemGeneralVersion,
       "mwSystemGeneralUptime": mwSystemGeneralUptime,
       "mwSystemGeneralMaxApLimit": mwSystemGeneralMaxApLimit,
       "mwSystemGeneralMaxClientLimit": mwSystemGeneralMaxClientLimit,
       "mwSystemGeneralInstalledApLicenses": mwSystemGeneralInstalledApLicenses,
       "mwSystemGeneralInUseApLicenses": mwSystemGeneralInUseApLicenses,
       "mwSystemGeneralTotalOnlineAps": mwSystemGeneralTotalOnlineAps,
       "mwSystemGeneralTotalOfflineAps": mwSystemGeneralTotalOfflineAps,
       "mwSystemGeneralTotalWirelessStations": mwSystemGeneralTotalWirelessStations,
       "mwSystemGeneralTotal24GStations": mwSystemGeneralTotal24GStations,
       "mwSystemGeneralTotal5GStations": mwSystemGeneralTotal5GStations,
       "mwSystemGeneralTotalWiredStations": mwSystemGeneralTotalWiredStations,
       "mwSystemGeneralTotalAlarms": mwSystemGeneralTotalAlarms,
       "mwSystemGeneralTotalCritAlarms": mwSystemGeneralTotalCritAlarms,
       "mwSystemGeneralTotalMajorAlarms": mwSystemGeneralTotalMajorAlarms,
       "mwSystemGeneralTotalMinorAlarms": mwSystemGeneralTotalMinorAlarms,
       "mwSystemGeneralTotalRogueAps": mwSystemGeneralTotalRogueAps,
       "mwSystemGeneralTotalRogueStations": mwSystemGeneralTotalRogueStations,
       "mwSystemGeneralTotalRogueUnknownDevices": mwSystemGeneralTotalRogueUnknownDevices,
       "mwSystemGeneralTotalClearEssProfiles": mwSystemGeneralTotalClearEssProfiles,
       "mwSystemGeneralTotalSecureEssProfiles": mwSystemGeneralTotalSecureEssProfiles,
       "mwSystemGeneralTotalCaptivePortalEssProfiles": mwSystemGeneralTotalCaptivePortalEssProfiles,
       "mwSystemResource": mwSystemResource,
       "mwSystemResourceCpuUsagePercentageUser": mwSystemResourceCpuUsagePercentageUser,
       "mwSystemResourceCpuUsagePercentageSystem": mwSystemResourceCpuUsagePercentageSystem,
       "mwSystemResourceCpuUsagePercentageIdle": mwSystemResourceCpuUsagePercentageIdle,
       "mwSystemResourceMemoryTotalSize": mwSystemResourceMemoryTotalSize,
       "mwSystemResourceMemoryUsedSize": mwSystemResourceMemoryUsedSize,
       "mwSystemResourceMemoryFreeSize": mwSystemResourceMemoryFreeSize,
       "mwSystemResourceRootFileSystemTotalSize": mwSystemResourceRootFileSystemTotalSize,
       "mwSystemResourceRootFileSystemUsedSize": mwSystemResourceRootFileSystemUsedSize,
       "mwSystemResourceRootFileSystemAvailSize": mwSystemResourceRootFileSystemAvailSize,
       "mwSystemResourceRootFileSystemUsagePercentage": mwSystemResourceRootFileSystemUsagePercentage,
       "mwSystemStation": mwSystemStation,
       "mwSystemStationTotal11aStations": mwSystemStationTotal11aStations,
       "mwSystemStationTotal11an1Stations": mwSystemStationTotal11an1Stations,
       "mwSystemStationTotal11an2Stations": mwSystemStationTotal11an2Stations,
       "mwSystemStationTotal11an3Stations": mwSystemStationTotal11an3Stations,
       "mwSystemStationTotal11bStations": mwSystemStationTotal11bStations,
       "mwSystemStationTotal11bgStations": mwSystemStationTotal11bgStations,
       "mwSystemStationTotal11gn1Stations": mwSystemStationTotal11gn1Stations,
       "mwSystemStationTotal11gn2Stations": mwSystemStationTotal11gn2Stations,
       "mwSystemStationTotal11gn3Stations": mwSystemStationTotal11gn3Stations,
       "mwSystemStationTotalDataStations": mwSystemStationTotalDataStations,
       "mwSystemStationTotalPhoneStations": mwSystemStationTotalPhoneStations,
       "mwSystemThruput": mwSystemThruput,
       "mwSystemThruputTotalControllerRxBytes": mwSystemThruputTotalControllerRxBytes,
       "mwSystemThruputTotalControllerTxBytes": mwSystemThruputTotalControllerTxBytes,
       "mwSystemThruputControllerRxThroughput": mwSystemThruputControllerRxThroughput,
       "mwSystemThruputControllerTxThroughput": mwSystemThruputControllerTxThroughput,
       "mwSystemThruputTotalWlanSystemRxBytes": mwSystemThruputTotalWlanSystemRxBytes,
       "mwSystemThruputTotalWlanSystemTxBytes": mwSystemThruputTotalWlanSystemTxBytes,
       "mwSystemThruputWlanRxThroughput": mwSystemThruputWlanRxThroughput,
       "mwSystemThruputWlanTxThroughput": mwSystemThruputWlanTxThroughput,
       "mwPerEss80211StatsTable": mwPerEss80211StatsTable,
       "mwPerEss80211StatsEntry": mwPerEss80211StatsEntry,
       "mwPerEss80211StatsTableIndex": mwPerEss80211StatsTableIndex,
       "mwPerEss80211StatsNodeId": mwPerEss80211StatsNodeId,
       "mwPerEss80211StatsIfIndex": mwPerEss80211StatsIfIndex,
       "mwPerEss80211StatsEssId": mwPerEss80211StatsEssId,
       "mwPerEss80211StatsBssid": mwPerEss80211StatsBssid,
       "mwPerEss80211StatsRxThroughput": mwPerEss80211StatsRxThroughput,
       "mwPerEss80211StatsTxThroughput": mwPerEss80211StatsTxThroughput,
       "mwPerEss80211StatsTotalThroughput": mwPerEss80211StatsTotalThroughput,
       "mwPerEss80211StatsTotalRxBytes": mwPerEss80211StatsTotalRxBytes,
       "mwPerEss80211StatsTotalTxBytes": mwPerEss80211StatsTotalTxBytes,
       "mwPerEss80211StatsTotalVideoRxBytes": mwPerEss80211StatsTotalVideoRxBytes,
       "mwPerEss80211StatsTotalVideoTxBytes": mwPerEss80211StatsTotalVideoTxBytes,
       "mwPerEss80211StatsTotalVoiceRxBytes": mwPerEss80211StatsTotalVoiceRxBytes,
       "mwPerEss80211StatsTotalVoiceTxBytes": mwPerEss80211StatsTotalVoiceTxBytes,
       "mwPerEss80211StatsTotalBestEffortRxBytes": mwPerEss80211StatsTotalBestEffortRxBytes,
       "mwPerEss80211StatsTotalBestEffortTxBytes": mwPerEss80211StatsTotalBestEffortTxBytes,
       "mwPerEss80211StatsTotalBackgroundRxBytes": mwPerEss80211StatsTotalBackgroundRxBytes,
       "mwPerEss80211StatsTotalBackgroundTxBytes": mwPerEss80211StatsTotalBackgroundTxBytes,
       "mwPerEss80211StatsTotalUnicastRxBytes": mwPerEss80211StatsTotalUnicastRxBytes,
       "mwPerEss80211StatsTotalUnicastTxBytes": mwPerEss80211StatsTotalUnicastTxBytes,
       "mwPerEss80211StatsTotalBroadcastDataBytes": mwPerEss80211StatsTotalBroadcastDataBytes,
       "mwPerEss80211StatsTotalMulticastDataBytes": mwPerEss80211StatsTotalMulticastDataBytes,
       "mwPerEss80211StatsAssociatedStationNum": mwPerEss80211StatsAssociatedStationNum,
       "mwPerEss80211StatsAssociated11bStationNum": mwPerEss80211StatsAssociated11bStationNum,
       "mwPerEss80211StatsAssociated11bgStationNum": mwPerEss80211StatsAssociated11bgStationNum,
       "mwPerEss80211StatsAssociated11bgn1StationNum": mwPerEss80211StatsAssociated11bgn1StationNum,
       "mwPerEss80211StatsAssociated11bgn2StationNum": mwPerEss80211StatsAssociated11bgn2StationNum,
       "mwPerEss80211StatsAssociated11bgn3StationNum": mwPerEss80211StatsAssociated11bgn3StationNum,
       "mwPerEss80211StatsAssociated11aStationNum": mwPerEss80211StatsAssociated11aStationNum,
       "mwPerEss80211StatsAssociated11an1StationNum": mwPerEss80211StatsAssociated11an1StationNum,
       "mwPerEss80211StatsAssociated11an2StationNum": mwPerEss80211StatsAssociated11an2StationNum,
       "mwPerEss80211StatsAssociated11an3StationNum": mwPerEss80211StatsAssociated11an3StationNum,
       "mwEssStatsSummaryTable": mwEssStatsSummaryTable,
       "mwEssStatsSummaryEntry": mwEssStatsSummaryEntry,
       "mwEssStatsSummaryTableIndex": mwEssStatsSummaryTableIndex,
       "mwEssStatsSummaryEssId": mwEssStatsSummaryEssId,
       "mwEssStatsSummaryRFBand": mwEssStatsSummaryRFBand,
       "mwEssStatsSummaryRadioCount": mwEssStatsSummaryRadioCount,
       "mwEssStatsSummaryRxThroughput": mwEssStatsSummaryRxThroughput,
       "mwEssStatsSummaryTxThroughput": mwEssStatsSummaryTxThroughput,
       "mwEssStatsSummaryTotalThroughput": mwEssStatsSummaryTotalThroughput,
       "mwEssStatsSummaryTotalStationNum": mwEssStatsSummaryTotalStationNum,
       "mwEssStatsSummaryBStationNum": mwEssStatsSummaryBStationNum,
       "mwEssStatsSummaryBGStationNum": mwEssStatsSummaryBGStationNum,
       "mwEssStatsSummaryGN1StationNum": mwEssStatsSummaryGN1StationNum,
       "mwEssStatsSummaryGN2StationNum": mwEssStatsSummaryGN2StationNum,
       "mwEssStatsSummaryGN3StationNum": mwEssStatsSummaryGN3StationNum,
       "mwEssStatsSummaryAStationNum": mwEssStatsSummaryAStationNum,
       "mwEssStatsSummaryAN1StationNum": mwEssStatsSummaryAN1StationNum,
       "mwEssStatsSummaryAN2StationNum": mwEssStatsSummaryAN2StationNum,
       "mwEssStatsSummaryAN3StationNum": mwEssStatsSummaryAN3StationNum}
)
