# SNMP MIB module (CISCO-FC-PM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-FC-PM-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:00:16 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoFcPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997)
)
ciscoFcPmMIB.setRevisions(
        ("2005-02-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoFcPmMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoFcPmMIBNotifs = _CiscoFcPmMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 0)
)
_CiscoFcPmMIBObjects_ObjectIdentity = ObjectIdentity
ciscoFcPmMIBObjects = _CiscoFcPmMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1)
)
_CfcpmPortPerfStatus_ObjectIdentity = ObjectIdentity
cfcpmPortPerfStatus = _CfcpmPortPerfStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 1)
)
_CfcpmPortPerfStatusTable_Object = MibTable
cfcpmPortPerfStatusTable = _CfcpmPortPerfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfcpmPortPerfStatusTable.setStatus("current")
_CfcpmPortPerfStatusEntry_Object = MibTableRow
cfcpmPortPerfStatusEntry = _CfcpmPortPerfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 1, 1, 1)
)
cfcpmPortPerfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfcpmPortPerfStatusEntry.setStatus("current")


class _CfcpmTimeElapsed_Type(Integer32):
    """Custom type cfcpmTimeElapsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 899),
    )


_CfcpmTimeElapsed_Type.__name__ = "Integer32"
_CfcpmTimeElapsed_Object = MibTableColumn
cfcpmTimeElapsed = _CfcpmTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 1, 1, 1, 1),
    _CfcpmTimeElapsed_Type()
)
cfcpmTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmTimeElapsed.setStatus("current")


class _CfcpmValidIntervals_Type(Integer32):
    """Custom type cfcpmValidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CfcpmValidIntervals_Type.__name__ = "Integer32"
_CfcpmValidIntervals_Object = MibTableColumn
cfcpmValidIntervals = _CfcpmValidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 1, 1, 1, 2),
    _CfcpmValidIntervals_Type()
)
cfcpmValidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmValidIntervals.setStatus("current")


class _CfcpmInvalidIntervals_Type(Integer32):
    """Custom type cfcpmInvalidIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_CfcpmInvalidIntervals_Type.__name__ = "Integer32"
_CfcpmInvalidIntervals_Object = MibTableColumn
cfcpmInvalidIntervals = _CfcpmInvalidIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 1, 1, 1, 3),
    _CfcpmInvalidIntervals_Type()
)
cfcpmInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmInvalidIntervals.setStatus("current")
_CfcpmPortErrorStatusBlock_ObjectIdentity = ObjectIdentity
cfcpmPortErrorStatusBlock = _CfcpmPortErrorStatusBlock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2)
)
_CfcpmTotalPortErrorTable_Object = MibTable
cfcpmTotalPortErrorTable = _CfcpmTotalPortErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfcpmTotalPortErrorTable.setStatus("current")
_CfcpmTotalPortErrorEntry_Object = MibTableRow
cfcpmTotalPortErrorEntry = _CfcpmTotalPortErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1)
)
cfcpmTotalPortErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfcpmTotalPortErrorEntry.setStatus("current")
_CfcpmtPortRxLinkResets_Type = PerfTotalCount
_CfcpmtPortRxLinkResets_Object = MibTableColumn
cfcpmtPortRxLinkResets = _CfcpmtPortRxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 1),
    _CfcpmtPortRxLinkResets_Type()
)
cfcpmtPortRxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortRxLinkResets.setStatus("current")
_CfcpmtPortTxLinkResets_Type = PerfTotalCount
_CfcpmtPortTxLinkResets_Object = MibTableColumn
cfcpmtPortTxLinkResets = _CfcpmtPortTxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 2),
    _CfcpmtPortTxLinkResets_Type()
)
cfcpmtPortTxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortTxLinkResets.setStatus("current")
_CfcpmtPortLinkResets_Type = PerfTotalCount
_CfcpmtPortLinkResets_Object = MibTableColumn
cfcpmtPortLinkResets = _CfcpmtPortLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 3),
    _CfcpmtPortLinkResets_Type()
)
cfcpmtPortLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortLinkResets.setStatus("current")
_CfcpmtPortRxOfflineSequences_Type = PerfTotalCount
_CfcpmtPortRxOfflineSequences_Object = MibTableColumn
cfcpmtPortRxOfflineSequences = _CfcpmtPortRxOfflineSequences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 4),
    _CfcpmtPortRxOfflineSequences_Type()
)
cfcpmtPortRxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortRxOfflineSequences.setStatus("current")
_CfcpmtPortTxOfflineSequences_Type = PerfTotalCount
_CfcpmtPortTxOfflineSequences_Object = MibTableColumn
cfcpmtPortTxOfflineSequences = _CfcpmtPortTxOfflineSequences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 5),
    _CfcpmtPortTxOfflineSequences_Type()
)
cfcpmtPortTxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortTxOfflineSequences.setStatus("current")
_CfcpmtPortLinkFailures_Type = PerfTotalCount
_CfcpmtPortLinkFailures_Object = MibTableColumn
cfcpmtPortLinkFailures = _CfcpmtPortLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 6),
    _CfcpmtPortLinkFailures_Type()
)
cfcpmtPortLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortLinkFailures.setStatus("current")
_CfcpmtPortSynchLosses_Type = PerfTotalCount
_CfcpmtPortSynchLosses_Object = MibTableColumn
cfcpmtPortSynchLosses = _CfcpmtPortSynchLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 7),
    _CfcpmtPortSynchLosses_Type()
)
cfcpmtPortSynchLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortSynchLosses.setStatus("current")
_CfcpmtPortSignalLosses_Type = PerfTotalCount
_CfcpmtPortSignalLosses_Object = MibTableColumn
cfcpmtPortSignalLosses = _CfcpmtPortSignalLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 8),
    _CfcpmtPortSignalLosses_Type()
)
cfcpmtPortSignalLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortSignalLosses.setStatus("current")
_CfcpmtPortPrimSeqProtocolErrors_Type = PerfTotalCount
_CfcpmtPortPrimSeqProtocolErrors_Object = MibTableColumn
cfcpmtPortPrimSeqProtocolErrors = _CfcpmtPortPrimSeqProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 9),
    _CfcpmtPortPrimSeqProtocolErrors_Type()
)
cfcpmtPortPrimSeqProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortPrimSeqProtocolErrors.setStatus("current")
_CfcpmtPortInvalidTxWords_Type = PerfTotalCount
_CfcpmtPortInvalidTxWords_Object = MibTableColumn
cfcpmtPortInvalidTxWords = _CfcpmtPortInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 10),
    _CfcpmtPortInvalidTxWords_Type()
)
cfcpmtPortInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortInvalidTxWords.setStatus("current")
_CfcpmtPortInvalidCRCs_Type = PerfTotalCount
_CfcpmtPortInvalidCRCs_Object = MibTableColumn
cfcpmtPortInvalidCRCs = _CfcpmtPortInvalidCRCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 11),
    _CfcpmtPortInvalidCRCs_Type()
)
cfcpmtPortInvalidCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortInvalidCRCs.setStatus("current")
_CfcpmtPortInvalidOrderedSets_Type = PerfTotalCount
_CfcpmtPortInvalidOrderedSets_Object = MibTableColumn
cfcpmtPortInvalidOrderedSets = _CfcpmtPortInvalidOrderedSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 12),
    _CfcpmtPortInvalidOrderedSets_Type()
)
cfcpmtPortInvalidOrderedSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortInvalidOrderedSets.setStatus("current")
_CfcpmtPortFramesTooLong_Type = PerfTotalCount
_CfcpmtPortFramesTooLong_Object = MibTableColumn
cfcpmtPortFramesTooLong = _CfcpmtPortFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 13),
    _CfcpmtPortFramesTooLong_Type()
)
cfcpmtPortFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortFramesTooLong.setStatus("current")
_CfcpmtPortTruncatedFrames_Type = PerfTotalCount
_CfcpmtPortTruncatedFrames_Object = MibTableColumn
cfcpmtPortTruncatedFrames = _CfcpmtPortTruncatedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 14),
    _CfcpmtPortTruncatedFrames_Type()
)
cfcpmtPortTruncatedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortTruncatedFrames.setStatus("current")
_CfcpmtPortAddressErrors_Type = PerfTotalCount
_CfcpmtPortAddressErrors_Object = MibTableColumn
cfcpmtPortAddressErrors = _CfcpmtPortAddressErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 15),
    _CfcpmtPortAddressErrors_Type()
)
cfcpmtPortAddressErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortAddressErrors.setStatus("current")
_CfcpmtPortDelimiterErrors_Type = PerfTotalCount
_CfcpmtPortDelimiterErrors_Object = MibTableColumn
cfcpmtPortDelimiterErrors = _CfcpmtPortDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 16),
    _CfcpmtPortDelimiterErrors_Type()
)
cfcpmtPortDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortDelimiterErrors.setStatus("current")
_CfcpmtPortEncDisparityErrors_Type = PerfTotalCount
_CfcpmtPortEncDisparityErrors_Object = MibTableColumn
cfcpmtPortEncDisparityErrors = _CfcpmtPortEncDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 17),
    _CfcpmtPortEncDisparityErrors_Type()
)
cfcpmtPortEncDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortEncDisparityErrors.setStatus("current")
_CfcpmtPortOtherErrors_Type = PerfTotalCount
_CfcpmtPortOtherErrors_Object = MibTableColumn
cfcpmtPortOtherErrors = _CfcpmtPortOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 1, 1, 18),
    _CfcpmtPortOtherErrors_Type()
)
cfcpmtPortOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmtPortOtherErrors.setStatus("current")
_CfcpmCurrentPortErrorTable_Object = MibTable
cfcpmCurrentPortErrorTable = _CfcpmCurrentPortErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cfcpmCurrentPortErrorTable.setStatus("current")
_CfcpmCurrentPortErrorEntry_Object = MibTableRow
cfcpmCurrentPortErrorEntry = _CfcpmCurrentPortErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1)
)
cfcpmCurrentPortErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cfcpmCurrentPortErrorEntry.setStatus("current")
_CfcpmcPortRxLinkResets_Type = PerfCurrentCount
_CfcpmcPortRxLinkResets_Object = MibTableColumn
cfcpmcPortRxLinkResets = _CfcpmcPortRxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 1),
    _CfcpmcPortRxLinkResets_Type()
)
cfcpmcPortRxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortRxLinkResets.setStatus("current")
_CfcpmcPortTxLinkResets_Type = PerfCurrentCount
_CfcpmcPortTxLinkResets_Object = MibTableColumn
cfcpmcPortTxLinkResets = _CfcpmcPortTxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 2),
    _CfcpmcPortTxLinkResets_Type()
)
cfcpmcPortTxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortTxLinkResets.setStatus("current")
_CfcpmcPortLinkResets_Type = PerfCurrentCount
_CfcpmcPortLinkResets_Object = MibTableColumn
cfcpmcPortLinkResets = _CfcpmcPortLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 3),
    _CfcpmcPortLinkResets_Type()
)
cfcpmcPortLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortLinkResets.setStatus("current")
_CfcpmcPortRxOfflineSequences_Type = PerfCurrentCount
_CfcpmcPortRxOfflineSequences_Object = MibTableColumn
cfcpmcPortRxOfflineSequences = _CfcpmcPortRxOfflineSequences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 4),
    _CfcpmcPortRxOfflineSequences_Type()
)
cfcpmcPortRxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortRxOfflineSequences.setStatus("current")
_CfcpmcPortTxOfflineSequences_Type = PerfCurrentCount
_CfcpmcPortTxOfflineSequences_Object = MibTableColumn
cfcpmcPortTxOfflineSequences = _CfcpmcPortTxOfflineSequences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 5),
    _CfcpmcPortTxOfflineSequences_Type()
)
cfcpmcPortTxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortTxOfflineSequences.setStatus("current")
_CfcpmcPortLinkFailures_Type = PerfCurrentCount
_CfcpmcPortLinkFailures_Object = MibTableColumn
cfcpmcPortLinkFailures = _CfcpmcPortLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 6),
    _CfcpmcPortLinkFailures_Type()
)
cfcpmcPortLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortLinkFailures.setStatus("current")
_CfcpmcPortSynchLosses_Type = PerfCurrentCount
_CfcpmcPortSynchLosses_Object = MibTableColumn
cfcpmcPortSynchLosses = _CfcpmcPortSynchLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 7),
    _CfcpmcPortSynchLosses_Type()
)
cfcpmcPortSynchLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortSynchLosses.setStatus("current")
_CfcpmcPortSignalLosses_Type = PerfCurrentCount
_CfcpmcPortSignalLosses_Object = MibTableColumn
cfcpmcPortSignalLosses = _CfcpmcPortSignalLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 8),
    _CfcpmcPortSignalLosses_Type()
)
cfcpmcPortSignalLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortSignalLosses.setStatus("current")
_CfcpmcPortPrimSeqProtocolErrors_Type = PerfCurrentCount
_CfcpmcPortPrimSeqProtocolErrors_Object = MibTableColumn
cfcpmcPortPrimSeqProtocolErrors = _CfcpmcPortPrimSeqProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 9),
    _CfcpmcPortPrimSeqProtocolErrors_Type()
)
cfcpmcPortPrimSeqProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortPrimSeqProtocolErrors.setStatus("current")
_CfcpmcPortInvalidTxWords_Type = PerfCurrentCount
_CfcpmcPortInvalidTxWords_Object = MibTableColumn
cfcpmcPortInvalidTxWords = _CfcpmcPortInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 10),
    _CfcpmcPortInvalidTxWords_Type()
)
cfcpmcPortInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortInvalidTxWords.setStatus("current")
_CfcpmcPortInvalidCRCs_Type = PerfCurrentCount
_CfcpmcPortInvalidCRCs_Object = MibTableColumn
cfcpmcPortInvalidCRCs = _CfcpmcPortInvalidCRCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 11),
    _CfcpmcPortInvalidCRCs_Type()
)
cfcpmcPortInvalidCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortInvalidCRCs.setStatus("current")
_CfcpmcPortInvalidOrderedSets_Type = PerfCurrentCount
_CfcpmcPortInvalidOrderedSets_Object = MibTableColumn
cfcpmcPortInvalidOrderedSets = _CfcpmcPortInvalidOrderedSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 12),
    _CfcpmcPortInvalidOrderedSets_Type()
)
cfcpmcPortInvalidOrderedSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortInvalidOrderedSets.setStatus("current")
_CfcpmcPortFramesTooLong_Type = PerfCurrentCount
_CfcpmcPortFramesTooLong_Object = MibTableColumn
cfcpmcPortFramesTooLong = _CfcpmcPortFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 13),
    _CfcpmcPortFramesTooLong_Type()
)
cfcpmcPortFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortFramesTooLong.setStatus("current")
_CfcpmcPortTruncatedFrames_Type = PerfCurrentCount
_CfcpmcPortTruncatedFrames_Object = MibTableColumn
cfcpmcPortTruncatedFrames = _CfcpmcPortTruncatedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 14),
    _CfcpmcPortTruncatedFrames_Type()
)
cfcpmcPortTruncatedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortTruncatedFrames.setStatus("current")
_CfcpmcPortAddressErrors_Type = PerfCurrentCount
_CfcpmcPortAddressErrors_Object = MibTableColumn
cfcpmcPortAddressErrors = _CfcpmcPortAddressErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 15),
    _CfcpmcPortAddressErrors_Type()
)
cfcpmcPortAddressErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortAddressErrors.setStatus("current")
_CfcpmcPortDelimiterErrors_Type = PerfCurrentCount
_CfcpmcPortDelimiterErrors_Object = MibTableColumn
cfcpmcPortDelimiterErrors = _CfcpmcPortDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 16),
    _CfcpmcPortDelimiterErrors_Type()
)
cfcpmcPortDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortDelimiterErrors.setStatus("current")
_CfcpmcPortEncDisparityErrors_Type = PerfCurrentCount
_CfcpmcPortEncDisparityErrors_Object = MibTableColumn
cfcpmcPortEncDisparityErrors = _CfcpmcPortEncDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 17),
    _CfcpmcPortEncDisparityErrors_Type()
)
cfcpmcPortEncDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortEncDisparityErrors.setStatus("current")
_CfcpmcPortOtherErrors_Type = PerfCurrentCount
_CfcpmcPortOtherErrors_Object = MibTableColumn
cfcpmcPortOtherErrors = _CfcpmcPortOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 2, 1, 18),
    _CfcpmcPortOtherErrors_Type()
)
cfcpmcPortOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmcPortOtherErrors.setStatus("current")
_CfcpmIntervalPortErrorTable_Object = MibTable
cfcpmIntervalPortErrorTable = _CfcpmIntervalPortErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cfcpmIntervalPortErrorTable.setStatus("current")
_CfcpmIntervalPortErrorEntry_Object = MibTableRow
cfcpmIntervalPortErrorEntry = _CfcpmIntervalPortErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1)
)
cfcpmIntervalPortErrorEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-FC-PM-MIB", "cfcpmiPortErrorIntervalNumber"),
)
if mibBuilder.loadTexts:
    cfcpmIntervalPortErrorEntry.setStatus("current")


class _CfcpmiPortErrorIntervalNumber_Type(Unsigned32):
    """Custom type cfcpmiPortErrorIntervalNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_CfcpmiPortErrorIntervalNumber_Type.__name__ = "Unsigned32"
_CfcpmiPortErrorIntervalNumber_Object = MibTableColumn
cfcpmiPortErrorIntervalNumber = _CfcpmiPortErrorIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 1),
    _CfcpmiPortErrorIntervalNumber_Type()
)
cfcpmiPortErrorIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfcpmiPortErrorIntervalNumber.setStatus("current")
_CfcpmiPortRxLinkResets_Type = PerfIntervalCount
_CfcpmiPortRxLinkResets_Object = MibTableColumn
cfcpmiPortRxLinkResets = _CfcpmiPortRxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 2),
    _CfcpmiPortRxLinkResets_Type()
)
cfcpmiPortRxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortRxLinkResets.setStatus("current")
_CfcpmiPortTxLinkResets_Type = PerfIntervalCount
_CfcpmiPortTxLinkResets_Object = MibTableColumn
cfcpmiPortTxLinkResets = _CfcpmiPortTxLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 3),
    _CfcpmiPortTxLinkResets_Type()
)
cfcpmiPortTxLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortTxLinkResets.setStatus("current")
_CfcpmiPortLinkResets_Type = PerfIntervalCount
_CfcpmiPortLinkResets_Object = MibTableColumn
cfcpmiPortLinkResets = _CfcpmiPortLinkResets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 4),
    _CfcpmiPortLinkResets_Type()
)
cfcpmiPortLinkResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortLinkResets.setStatus("current")
_CfcpmiPortRxOfflineSequences_Type = PerfIntervalCount
_CfcpmiPortRxOfflineSequences_Object = MibTableColumn
cfcpmiPortRxOfflineSequences = _CfcpmiPortRxOfflineSequences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 5),
    _CfcpmiPortRxOfflineSequences_Type()
)
cfcpmiPortRxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortRxOfflineSequences.setStatus("current")
_CfcpmiPortTxOfflineSequences_Type = PerfIntervalCount
_CfcpmiPortTxOfflineSequences_Object = MibTableColumn
cfcpmiPortTxOfflineSequences = _CfcpmiPortTxOfflineSequences_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 6),
    _CfcpmiPortTxOfflineSequences_Type()
)
cfcpmiPortTxOfflineSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortTxOfflineSequences.setStatus("current")
_CfcpmiPortLinkFailures_Type = PerfIntervalCount
_CfcpmiPortLinkFailures_Object = MibTableColumn
cfcpmiPortLinkFailures = _CfcpmiPortLinkFailures_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 7),
    _CfcpmiPortLinkFailures_Type()
)
cfcpmiPortLinkFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortLinkFailures.setStatus("current")
_CfcpmiPortSynchLosses_Type = PerfIntervalCount
_CfcpmiPortSynchLosses_Object = MibTableColumn
cfcpmiPortSynchLosses = _CfcpmiPortSynchLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 8),
    _CfcpmiPortSynchLosses_Type()
)
cfcpmiPortSynchLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortSynchLosses.setStatus("current")
_CfcpmiPortSignalLosses_Type = PerfIntervalCount
_CfcpmiPortSignalLosses_Object = MibTableColumn
cfcpmiPortSignalLosses = _CfcpmiPortSignalLosses_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 9),
    _CfcpmiPortSignalLosses_Type()
)
cfcpmiPortSignalLosses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortSignalLosses.setStatus("current")
_CfcpmiPortPrimSeqProtocolErrors_Type = PerfIntervalCount
_CfcpmiPortPrimSeqProtocolErrors_Object = MibTableColumn
cfcpmiPortPrimSeqProtocolErrors = _CfcpmiPortPrimSeqProtocolErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 10),
    _CfcpmiPortPrimSeqProtocolErrors_Type()
)
cfcpmiPortPrimSeqProtocolErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortPrimSeqProtocolErrors.setStatus("current")
_CfcpmiPortInvalidTxWords_Type = PerfIntervalCount
_CfcpmiPortInvalidTxWords_Object = MibTableColumn
cfcpmiPortInvalidTxWords = _CfcpmiPortInvalidTxWords_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 11),
    _CfcpmiPortInvalidTxWords_Type()
)
cfcpmiPortInvalidTxWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortInvalidTxWords.setStatus("current")
_CfcpmiPortInvalidCRCs_Type = PerfIntervalCount
_CfcpmiPortInvalidCRCs_Object = MibTableColumn
cfcpmiPortInvalidCRCs = _CfcpmiPortInvalidCRCs_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 12),
    _CfcpmiPortInvalidCRCs_Type()
)
cfcpmiPortInvalidCRCs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortInvalidCRCs.setStatus("current")
_CfcpmiPortInvalidOrderedSets_Type = PerfIntervalCount
_CfcpmiPortInvalidOrderedSets_Object = MibTableColumn
cfcpmiPortInvalidOrderedSets = _CfcpmiPortInvalidOrderedSets_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 13),
    _CfcpmiPortInvalidOrderedSets_Type()
)
cfcpmiPortInvalidOrderedSets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortInvalidOrderedSets.setStatus("current")
_CfcpmiPortFramesTooLong_Type = PerfIntervalCount
_CfcpmiPortFramesTooLong_Object = MibTableColumn
cfcpmiPortFramesTooLong = _CfcpmiPortFramesTooLong_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 14),
    _CfcpmiPortFramesTooLong_Type()
)
cfcpmiPortFramesTooLong.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortFramesTooLong.setStatus("current")
_CfcpmiPortTruncatedFrames_Type = PerfIntervalCount
_CfcpmiPortTruncatedFrames_Object = MibTableColumn
cfcpmiPortTruncatedFrames = _CfcpmiPortTruncatedFrames_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 15),
    _CfcpmiPortTruncatedFrames_Type()
)
cfcpmiPortTruncatedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortTruncatedFrames.setStatus("current")
_CfcpmiPortAddressErrors_Type = PerfIntervalCount
_CfcpmiPortAddressErrors_Object = MibTableColumn
cfcpmiPortAddressErrors = _CfcpmiPortAddressErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 16),
    _CfcpmiPortAddressErrors_Type()
)
cfcpmiPortAddressErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortAddressErrors.setStatus("current")
_CfcpmiPortDelimiterErrors_Type = PerfIntervalCount
_CfcpmiPortDelimiterErrors_Object = MibTableColumn
cfcpmiPortDelimiterErrors = _CfcpmiPortDelimiterErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 17),
    _CfcpmiPortDelimiterErrors_Type()
)
cfcpmiPortDelimiterErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortDelimiterErrors.setStatus("current")
_CfcpmiPortEncDisparityErrors_Type = PerfIntervalCount
_CfcpmiPortEncDisparityErrors_Object = MibTableColumn
cfcpmiPortEncDisparityErrors = _CfcpmiPortEncDisparityErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 18),
    _CfcpmiPortEncDisparityErrors_Type()
)
cfcpmiPortEncDisparityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortEncDisparityErrors.setStatus("current")
_CfcpmiPortOtherErrors_Type = PerfIntervalCount
_CfcpmiPortOtherErrors_Object = MibTableColumn
cfcpmiPortOtherErrors = _CfcpmiPortOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 19),
    _CfcpmiPortOtherErrors_Type()
)
cfcpmiPortOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortOtherErrors.setStatus("current")
_CfcpmiPortValidData_Type = TruthValue
_CfcpmiPortValidData_Object = MibTableColumn
cfcpmiPortValidData = _CfcpmiPortValidData_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 1, 2, 3, 1, 20),
    _CfcpmiPortValidData_Type()
)
cfcpmiPortValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfcpmiPortValidData.setStatus("current")
_CiscoFcPmMIBConform_ObjectIdentity = ObjectIdentity
ciscoFcPmMIBConform = _CiscoFcPmMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 2)
)
_CfcpmMibCompliances_ObjectIdentity = ObjectIdentity
cfcpmMibCompliances = _CfcpmMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 2, 1)
)
_CfcpmMibGroups_ObjectIdentity = ObjectIdentity
cfcpmMibGroups = _CfcpmMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 2, 2)
)

# Managed Objects groups

cfcpmPortStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 2, 2, 1)
)
cfcpmPortStatusGroup.setObjects(
      *(("CISCO-FC-PM-MIB", "cfcpmTimeElapsed"),
        ("CISCO-FC-PM-MIB", "cfcpmValidIntervals"),
        ("CISCO-FC-PM-MIB", "cfcpmInvalidIntervals"))
)
if mibBuilder.loadTexts:
    cfcpmPortStatusGroup.setStatus("current")

cfcpmMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 2, 2, 2)
)
cfcpmMandatoryGroup.setObjects(
      *(("CISCO-FC-PM-MIB", "cfcpmtPortPrimSeqProtocolErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortPrimSeqProtocolErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortPrimSeqProtocolErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortValidData"))
)
if mibBuilder.loadTexts:
    cfcpmMandatoryGroup.setStatus("current")

cfcpmOptionalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 2, 2, 3)
)
cfcpmOptionalGroup.setObjects(
      *(("CISCO-FC-PM-MIB", "cfcpmtPortRxLinkResets"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortTxLinkResets"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortLinkResets"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortRxOfflineSequences"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortTxOfflineSequences"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortLinkFailures"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortSynchLosses"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortSignalLosses"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortInvalidTxWords"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortInvalidCRCs"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortInvalidOrderedSets"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortFramesTooLong"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortTruncatedFrames"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortAddressErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortDelimiterErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortEncDisparityErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmtPortOtherErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortRxLinkResets"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortTxLinkResets"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortLinkResets"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortRxOfflineSequences"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortTxOfflineSequences"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortLinkFailures"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortSynchLosses"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortSignalLosses"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortInvalidTxWords"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortInvalidCRCs"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortInvalidOrderedSets"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortFramesTooLong"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortTruncatedFrames"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortAddressErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortDelimiterErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortEncDisparityErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmcPortOtherErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortRxLinkResets"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortTxLinkResets"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortLinkResets"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortRxOfflineSequences"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortTxOfflineSequences"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortLinkFailures"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortSynchLosses"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortSignalLosses"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortInvalidTxWords"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortInvalidCRCs"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortInvalidOrderedSets"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortFramesTooLong"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortTruncatedFrames"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortAddressErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortDelimiterErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortEncDisparityErrors"),
        ("CISCO-FC-PM-MIB", "cfcpmiPortOtherErrors"))
)
if mibBuilder.loadTexts:
    cfcpmOptionalGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cfcpmMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 99997, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cfcpmMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-FC-PM-MIB",
    **{"ciscoFcPmMIB": ciscoFcPmMIB,
       "ciscoFcPmMIBNotifs": ciscoFcPmMIBNotifs,
       "ciscoFcPmMIBObjects": ciscoFcPmMIBObjects,
       "cfcpmPortPerfStatus": cfcpmPortPerfStatus,
       "cfcpmPortPerfStatusTable": cfcpmPortPerfStatusTable,
       "cfcpmPortPerfStatusEntry": cfcpmPortPerfStatusEntry,
       "cfcpmTimeElapsed": cfcpmTimeElapsed,
       "cfcpmValidIntervals": cfcpmValidIntervals,
       "cfcpmInvalidIntervals": cfcpmInvalidIntervals,
       "cfcpmPortErrorStatusBlock": cfcpmPortErrorStatusBlock,
       "cfcpmTotalPortErrorTable": cfcpmTotalPortErrorTable,
       "cfcpmTotalPortErrorEntry": cfcpmTotalPortErrorEntry,
       "cfcpmtPortRxLinkResets": cfcpmtPortRxLinkResets,
       "cfcpmtPortTxLinkResets": cfcpmtPortTxLinkResets,
       "cfcpmtPortLinkResets": cfcpmtPortLinkResets,
       "cfcpmtPortRxOfflineSequences": cfcpmtPortRxOfflineSequences,
       "cfcpmtPortTxOfflineSequences": cfcpmtPortTxOfflineSequences,
       "cfcpmtPortLinkFailures": cfcpmtPortLinkFailures,
       "cfcpmtPortSynchLosses": cfcpmtPortSynchLosses,
       "cfcpmtPortSignalLosses": cfcpmtPortSignalLosses,
       "cfcpmtPortPrimSeqProtocolErrors": cfcpmtPortPrimSeqProtocolErrors,
       "cfcpmtPortInvalidTxWords": cfcpmtPortInvalidTxWords,
       "cfcpmtPortInvalidCRCs": cfcpmtPortInvalidCRCs,
       "cfcpmtPortInvalidOrderedSets": cfcpmtPortInvalidOrderedSets,
       "cfcpmtPortFramesTooLong": cfcpmtPortFramesTooLong,
       "cfcpmtPortTruncatedFrames": cfcpmtPortTruncatedFrames,
       "cfcpmtPortAddressErrors": cfcpmtPortAddressErrors,
       "cfcpmtPortDelimiterErrors": cfcpmtPortDelimiterErrors,
       "cfcpmtPortEncDisparityErrors": cfcpmtPortEncDisparityErrors,
       "cfcpmtPortOtherErrors": cfcpmtPortOtherErrors,
       "cfcpmCurrentPortErrorTable": cfcpmCurrentPortErrorTable,
       "cfcpmCurrentPortErrorEntry": cfcpmCurrentPortErrorEntry,
       "cfcpmcPortRxLinkResets": cfcpmcPortRxLinkResets,
       "cfcpmcPortTxLinkResets": cfcpmcPortTxLinkResets,
       "cfcpmcPortLinkResets": cfcpmcPortLinkResets,
       "cfcpmcPortRxOfflineSequences": cfcpmcPortRxOfflineSequences,
       "cfcpmcPortTxOfflineSequences": cfcpmcPortTxOfflineSequences,
       "cfcpmcPortLinkFailures": cfcpmcPortLinkFailures,
       "cfcpmcPortSynchLosses": cfcpmcPortSynchLosses,
       "cfcpmcPortSignalLosses": cfcpmcPortSignalLosses,
       "cfcpmcPortPrimSeqProtocolErrors": cfcpmcPortPrimSeqProtocolErrors,
       "cfcpmcPortInvalidTxWords": cfcpmcPortInvalidTxWords,
       "cfcpmcPortInvalidCRCs": cfcpmcPortInvalidCRCs,
       "cfcpmcPortInvalidOrderedSets": cfcpmcPortInvalidOrderedSets,
       "cfcpmcPortFramesTooLong": cfcpmcPortFramesTooLong,
       "cfcpmcPortTruncatedFrames": cfcpmcPortTruncatedFrames,
       "cfcpmcPortAddressErrors": cfcpmcPortAddressErrors,
       "cfcpmcPortDelimiterErrors": cfcpmcPortDelimiterErrors,
       "cfcpmcPortEncDisparityErrors": cfcpmcPortEncDisparityErrors,
       "cfcpmcPortOtherErrors": cfcpmcPortOtherErrors,
       "cfcpmIntervalPortErrorTable": cfcpmIntervalPortErrorTable,
       "cfcpmIntervalPortErrorEntry": cfcpmIntervalPortErrorEntry,
       "cfcpmiPortErrorIntervalNumber": cfcpmiPortErrorIntervalNumber,
       "cfcpmiPortRxLinkResets": cfcpmiPortRxLinkResets,
       "cfcpmiPortTxLinkResets": cfcpmiPortTxLinkResets,
       "cfcpmiPortLinkResets": cfcpmiPortLinkResets,
       "cfcpmiPortRxOfflineSequences": cfcpmiPortRxOfflineSequences,
       "cfcpmiPortTxOfflineSequences": cfcpmiPortTxOfflineSequences,
       "cfcpmiPortLinkFailures": cfcpmiPortLinkFailures,
       "cfcpmiPortSynchLosses": cfcpmiPortSynchLosses,
       "cfcpmiPortSignalLosses": cfcpmiPortSignalLosses,
       "cfcpmiPortPrimSeqProtocolErrors": cfcpmiPortPrimSeqProtocolErrors,
       "cfcpmiPortInvalidTxWords": cfcpmiPortInvalidTxWords,
       "cfcpmiPortInvalidCRCs": cfcpmiPortInvalidCRCs,
       "cfcpmiPortInvalidOrderedSets": cfcpmiPortInvalidOrderedSets,
       "cfcpmiPortFramesTooLong": cfcpmiPortFramesTooLong,
       "cfcpmiPortTruncatedFrames": cfcpmiPortTruncatedFrames,
       "cfcpmiPortAddressErrors": cfcpmiPortAddressErrors,
       "cfcpmiPortDelimiterErrors": cfcpmiPortDelimiterErrors,
       "cfcpmiPortEncDisparityErrors": cfcpmiPortEncDisparityErrors,
       "cfcpmiPortOtherErrors": cfcpmiPortOtherErrors,
       "cfcpmiPortValidData": cfcpmiPortValidData,
       "ciscoFcPmMIBConform": ciscoFcPmMIBConform,
       "cfcpmMibCompliances": cfcpmMibCompliances,
       "cfcpmMibCompliance": cfcpmMibCompliance,
       "cfcpmMibGroups": cfcpmMibGroups,
       "cfcpmPortStatusGroup": cfcpmPortStatusGroup,
       "cfcpmMandatoryGroup": cfcpmMandatoryGroup,
       "cfcpmOptionalGroup": cfcpmOptionalGroup}
)
