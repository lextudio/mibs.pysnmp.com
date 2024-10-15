# SNMP MIB module (REDSTONE-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-FRAME-RELAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:38 2024
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

(DLCI,) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "DLCI")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsNextIfIndex,) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsNextIfIndex")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

rsFrameRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10)
)
rsFrameRelayMIB.setRevisions(
        ("1999-06-01 00:00",
         "1998-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsFrObjects_ObjectIdentity = ObjectIdentity
rsFrObjects = _RsFrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1)
)
_RsFrIfLayer_ObjectIdentity = ObjectIdentity
rsFrIfLayer = _RsFrIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1)
)
_RsFrNextIfIndex_Type = RsNextIfIndex
_RsFrNextIfIndex_Object = MibScalar
rsFrNextIfIndex = _RsFrNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 1),
    _RsFrNextIfIndex_Type()
)
rsFrNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrNextIfIndex.setStatus("current")
_RsFrDlcmiTable_Object = MibTable
rsFrDlcmiTable = _RsFrDlcmiTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsFrDlcmiTable.setStatus("current")
_RsFrDlcmiEntry_Object = MibTableRow
rsFrDlcmiEntry = _RsFrDlcmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1)
)
rsFrDlcmiEntry.setIndexNames(
    (0, "REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    rsFrDlcmiEntry.setStatus("current")
_RsFrDlcmiIfIndex_Type = InterfaceIndex
_RsFrDlcmiIfIndex_Object = MibTableColumn
rsFrDlcmiIfIndex = _RsFrDlcmiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 1),
    _RsFrDlcmiIfIndex_Type()
)
rsFrDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiIfIndex.setStatus("current")


class _RsFrDlcmiState_Type(Integer32):
    """Custom type rsFrDlcmiState based on Integer32"""
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
        *(("ansiT1617B", 4),
          ("ansiT1617D", 3),
          ("ansiT1617D1994", 6),
          ("itut933A", 5),
          ("lmiRev1", 2),
          ("noLmiConfigured", 1))
    )


_RsFrDlcmiState_Type.__name__ = "Integer32"
_RsFrDlcmiState_Object = MibTableColumn
rsFrDlcmiState = _RsFrDlcmiState_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 2),
    _RsFrDlcmiState_Type()
)
rsFrDlcmiState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiState.setStatus("current")


class _RsFrDlcmiAddress_Type(Integer32):
    """Custom type rsFrDlcmiAddress based on Integer32"""
    defaultValue = 4

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
        *(("q921", 1),
          ("q922", 4),
          ("q922March90", 2),
          ("q922November90", 3))
    )


_RsFrDlcmiAddress_Type.__name__ = "Integer32"
_RsFrDlcmiAddress_Object = MibTableColumn
rsFrDlcmiAddress = _RsFrDlcmiAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 3),
    _RsFrDlcmiAddress_Type()
)
rsFrDlcmiAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiAddress.setStatus("current")


class _RsFrDlcmiAddressLen_Type(Integer32):
    """Custom type rsFrDlcmiAddressLen based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("fourOctets", 4),
          ("threeOctets", 3),
          ("twoOctets", 2))
    )


_RsFrDlcmiAddressLen_Type.__name__ = "Integer32"
_RsFrDlcmiAddressLen_Object = MibTableColumn
rsFrDlcmiAddressLen = _RsFrDlcmiAddressLen_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 4),
    _RsFrDlcmiAddressLen_Type()
)
rsFrDlcmiAddressLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiAddressLen.setStatus("current")


class _RsFrDlcmiPollingInterval_Type(Integer32):
    """Custom type rsFrDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_RsFrDlcmiPollingInterval_Type.__name__ = "Integer32"
_RsFrDlcmiPollingInterval_Object = MibTableColumn
rsFrDlcmiPollingInterval = _RsFrDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 5),
    _RsFrDlcmiPollingInterval_Type()
)
rsFrDlcmiPollingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsFrDlcmiPollingInterval.setUnits("seconds")


class _RsFrDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type rsFrDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RsFrDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_RsFrDlcmiFullEnquiryInterval_Object = MibTableColumn
rsFrDlcmiFullEnquiryInterval = _RsFrDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 6),
    _RsFrDlcmiFullEnquiryInterval_Type()
)
rsFrDlcmiFullEnquiryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiFullEnquiryInterval.setStatus("current")


class _RsFrDlcmiErrorThreshold_Type(Integer32):
    """Custom type rsFrDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsFrDlcmiErrorThreshold_Type.__name__ = "Integer32"
_RsFrDlcmiErrorThreshold_Object = MibTableColumn
rsFrDlcmiErrorThreshold = _RsFrDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 7),
    _RsFrDlcmiErrorThreshold_Type()
)
rsFrDlcmiErrorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiErrorThreshold.setStatus("current")


class _RsFrDlcmiMonitoredEvents_Type(Integer32):
    """Custom type rsFrDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsFrDlcmiMonitoredEvents_Type.__name__ = "Integer32"
_RsFrDlcmiMonitoredEvents_Object = MibTableColumn
rsFrDlcmiMonitoredEvents = _RsFrDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 8),
    _RsFrDlcmiMonitoredEvents_Type()
)
rsFrDlcmiMonitoredEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiMonitoredEvents.setStatus("current")
_RsFrDlcmiMaxSupportedVCs_Type = DLCI
_RsFrDlcmiMaxSupportedVCs_Object = MibTableColumn
rsFrDlcmiMaxSupportedVCs = _RsFrDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 9),
    _RsFrDlcmiMaxSupportedVCs_Type()
)
rsFrDlcmiMaxSupportedVCs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiMaxSupportedVCs.setStatus("current")


class _RsFrDlcmiMulticast_Type(Integer32):
    """Custom type rsFrDlcmiMulticast based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 2),
          ("nonBroadcast", 1))
    )


_RsFrDlcmiMulticast_Type.__name__ = "Integer32"
_RsFrDlcmiMulticast_Object = MibTableColumn
rsFrDlcmiMulticast = _RsFrDlcmiMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 10),
    _RsFrDlcmiMulticast_Type()
)
rsFrDlcmiMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiMulticast.setStatus("current")


class _RsFrDlcmiStatus_Type(Integer32):
    """Custom type rsFrDlcmiStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fault", 2),
          ("initializing", 3),
          ("running", 1))
    )


_RsFrDlcmiStatus_Type.__name__ = "Integer32"
_RsFrDlcmiStatus_Object = MibTableColumn
rsFrDlcmiStatus = _RsFrDlcmiStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 11),
    _RsFrDlcmiStatus_Type()
)
rsFrDlcmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatus.setStatus("current")
_RsFrDlcmiRowStatus_Type = RowStatus
_RsFrDlcmiRowStatus_Object = MibTableColumn
rsFrDlcmiRowStatus = _RsFrDlcmiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 12),
    _RsFrDlcmiRowStatus_Type()
)
rsFrDlcmiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiRowStatus.setStatus("current")
_RsFrDlcmiLowerIfIndex_Type = InterfaceIndexOrZero
_RsFrDlcmiLowerIfIndex_Object = MibTableColumn
rsFrDlcmiLowerIfIndex = _RsFrDlcmiLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 13),
    _RsFrDlcmiLowerIfIndex_Type()
)
rsFrDlcmiLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiLowerIfIndex.setStatus("current")


class _RsFrDlcmiRole_Type(Integer32):
    """Custom type rsFrDlcmiRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 1),
          ("dte", 0),
          ("nni", 2))
    )


_RsFrDlcmiRole_Type.__name__ = "Integer32"
_RsFrDlcmiRole_Object = MibTableColumn
rsFrDlcmiRole = _RsFrDlcmiRole_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 14),
    _RsFrDlcmiRole_Type()
)
rsFrDlcmiRole.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiRole.setStatus("current")


class _RsFrDlcmiDcePollingInterval_Type(Integer32):
    """Custom type rsFrDlcmiDcePollingInterval based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_RsFrDlcmiDcePollingInterval_Type.__name__ = "Integer32"
_RsFrDlcmiDcePollingInterval_Object = MibTableColumn
rsFrDlcmiDcePollingInterval = _RsFrDlcmiDcePollingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 15),
    _RsFrDlcmiDcePollingInterval_Type()
)
rsFrDlcmiDcePollingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiDcePollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsFrDlcmiDcePollingInterval.setUnits("seconds")


class _RsFrDlcmiDceErrorThreshold_Type(Integer32):
    """Custom type rsFrDlcmiDceErrorThreshold based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsFrDlcmiDceErrorThreshold_Type.__name__ = "Integer32"
_RsFrDlcmiDceErrorThreshold_Object = MibTableColumn
rsFrDlcmiDceErrorThreshold = _RsFrDlcmiDceErrorThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 16),
    _RsFrDlcmiDceErrorThreshold_Type()
)
rsFrDlcmiDceErrorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiDceErrorThreshold.setStatus("current")


class _RsFrDlcmiDceMonitoredEvents_Type(Integer32):
    """Custom type rsFrDlcmiDceMonitoredEvents based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RsFrDlcmiDceMonitoredEvents_Type.__name__ = "Integer32"
_RsFrDlcmiDceMonitoredEvents_Object = MibTableColumn
rsFrDlcmiDceMonitoredEvents = _RsFrDlcmiDceMonitoredEvents_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 2, 1, 17),
    _RsFrDlcmiDceMonitoredEvents_Type()
)
rsFrDlcmiDceMonitoredEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrDlcmiDceMonitoredEvents.setStatus("current")
_RsFrDlcmiStatsTable_Object = MibTable
rsFrDlcmiStatsTable = _RsFrDlcmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3)
)
if mibBuilder.loadTexts:
    rsFrDlcmiStatsTable.setStatus("current")
_RsFrDlcmiStatsEntry_Object = MibTableRow
rsFrDlcmiStatsEntry = _RsFrDlcmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1)
)
rsFrDlcmiStatsEntry.setIndexNames(
    (0, "REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    rsFrDlcmiStatsEntry.setStatus("current")
_RsFrDlcmiStatsDteEnquiries_Type = Counter32
_RsFrDlcmiStatsDteEnquiries_Object = MibTableColumn
rsFrDlcmiStatsDteEnquiries = _RsFrDlcmiStatsDteEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 1),
    _RsFrDlcmiStatsDteEnquiries_Type()
)
rsFrDlcmiStatsDteEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDteEnquiries.setStatus("current")
_RsFrDlcmiStatsDteFullEnquiries_Type = Counter32
_RsFrDlcmiStatsDteFullEnquiries_Object = MibTableColumn
rsFrDlcmiStatsDteFullEnquiries = _RsFrDlcmiStatsDteFullEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 2),
    _RsFrDlcmiStatsDteFullEnquiries_Type()
)
rsFrDlcmiStatsDteFullEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDteFullEnquiries.setStatus("current")
_RsFrDlcmiStatsDteEnquiryResponses_Type = Counter32
_RsFrDlcmiStatsDteEnquiryResponses_Object = MibTableColumn
rsFrDlcmiStatsDteEnquiryResponses = _RsFrDlcmiStatsDteEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 3),
    _RsFrDlcmiStatsDteEnquiryResponses_Type()
)
rsFrDlcmiStatsDteEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDteEnquiryResponses.setStatus("current")
_RsFrDlcmiStatsDteFullEnquiryResponses_Type = Counter32
_RsFrDlcmiStatsDteFullEnquiryResponses_Object = MibTableColumn
rsFrDlcmiStatsDteFullEnquiryResponses = _RsFrDlcmiStatsDteFullEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 4),
    _RsFrDlcmiStatsDteFullEnquiryResponses_Type()
)
rsFrDlcmiStatsDteFullEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDteFullEnquiryResponses.setStatus("current")
_RsFrDlcmiStatsDteAsyncUpdates_Type = Counter32
_RsFrDlcmiStatsDteAsyncUpdates_Object = MibTableColumn
rsFrDlcmiStatsDteAsyncUpdates = _RsFrDlcmiStatsDteAsyncUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 5),
    _RsFrDlcmiStatsDteAsyncUpdates_Type()
)
rsFrDlcmiStatsDteAsyncUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDteAsyncUpdates.setStatus("current")
_RsFrDlcmiStatsDteUnknownRxMessages_Type = Counter32
_RsFrDlcmiStatsDteUnknownRxMessages_Object = MibTableColumn
rsFrDlcmiStatsDteUnknownRxMessages = _RsFrDlcmiStatsDteUnknownRxMessages_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 6),
    _RsFrDlcmiStatsDteUnknownRxMessages_Type()
)
rsFrDlcmiStatsDteUnknownRxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDteUnknownRxMessages.setStatus("current")
_RsFrDlcmiStatsDteLossOfSequences_Type = Counter32
_RsFrDlcmiStatsDteLossOfSequences_Object = MibTableColumn
rsFrDlcmiStatsDteLossOfSequences = _RsFrDlcmiStatsDteLossOfSequences_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 7),
    _RsFrDlcmiStatsDteLossOfSequences_Type()
)
rsFrDlcmiStatsDteLossOfSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDteLossOfSequences.setStatus("current")
_RsFrDlcmiStatsDteNoResponseTimeouts_Type = Counter32
_RsFrDlcmiStatsDteNoResponseTimeouts_Object = MibTableColumn
rsFrDlcmiStatsDteNoResponseTimeouts = _RsFrDlcmiStatsDteNoResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 8),
    _RsFrDlcmiStatsDteNoResponseTimeouts_Type()
)
rsFrDlcmiStatsDteNoResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDteNoResponseTimeouts.setStatus("current")
_RsFrDlcmiStatsDceEnquiries_Type = Counter32
_RsFrDlcmiStatsDceEnquiries_Object = MibTableColumn
rsFrDlcmiStatsDceEnquiries = _RsFrDlcmiStatsDceEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 9),
    _RsFrDlcmiStatsDceEnquiries_Type()
)
rsFrDlcmiStatsDceEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDceEnquiries.setStatus("current")
_RsFrDlcmiStatsDceFullEnquiries_Type = Counter32
_RsFrDlcmiStatsDceFullEnquiries_Object = MibTableColumn
rsFrDlcmiStatsDceFullEnquiries = _RsFrDlcmiStatsDceFullEnquiries_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 10),
    _RsFrDlcmiStatsDceFullEnquiries_Type()
)
rsFrDlcmiStatsDceFullEnquiries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDceFullEnquiries.setStatus("current")
_RsFrDlcmiStatsDceEnquiryResponses_Type = Counter32
_RsFrDlcmiStatsDceEnquiryResponses_Object = MibTableColumn
rsFrDlcmiStatsDceEnquiryResponses = _RsFrDlcmiStatsDceEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 11),
    _RsFrDlcmiStatsDceEnquiryResponses_Type()
)
rsFrDlcmiStatsDceEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDceEnquiryResponses.setStatus("current")
_RsFrDlcmiStatsDceFullEnquiryResponses_Type = Counter32
_RsFrDlcmiStatsDceFullEnquiryResponses_Object = MibTableColumn
rsFrDlcmiStatsDceFullEnquiryResponses = _RsFrDlcmiStatsDceFullEnquiryResponses_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 12),
    _RsFrDlcmiStatsDceFullEnquiryResponses_Type()
)
rsFrDlcmiStatsDceFullEnquiryResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDceFullEnquiryResponses.setStatus("current")
_RsFrDlcmiStatsDceAsyncUpdates_Type = Counter32
_RsFrDlcmiStatsDceAsyncUpdates_Object = MibTableColumn
rsFrDlcmiStatsDceAsyncUpdates = _RsFrDlcmiStatsDceAsyncUpdates_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 13),
    _RsFrDlcmiStatsDceAsyncUpdates_Type()
)
rsFrDlcmiStatsDceAsyncUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDceAsyncUpdates.setStatus("current")
_RsFrDlcmiStatsDceUnknownRxMessages_Type = Counter32
_RsFrDlcmiStatsDceUnknownRxMessages_Object = MibTableColumn
rsFrDlcmiStatsDceUnknownRxMessages = _RsFrDlcmiStatsDceUnknownRxMessages_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 14),
    _RsFrDlcmiStatsDceUnknownRxMessages_Type()
)
rsFrDlcmiStatsDceUnknownRxMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDceUnknownRxMessages.setStatus("current")
_RsFrDlcmiStatsDceLossOfSequences_Type = Counter32
_RsFrDlcmiStatsDceLossOfSequences_Object = MibTableColumn
rsFrDlcmiStatsDceLossOfSequences = _RsFrDlcmiStatsDceLossOfSequences_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 15),
    _RsFrDlcmiStatsDceLossOfSequences_Type()
)
rsFrDlcmiStatsDceLossOfSequences.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDceLossOfSequences.setStatus("current")
_RsFrDlcmiStatsDceNoResponseTimeouts_Type = Counter32
_RsFrDlcmiStatsDceNoResponseTimeouts_Object = MibTableColumn
rsFrDlcmiStatsDceNoResponseTimeouts = _RsFrDlcmiStatsDceNoResponseTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 16),
    _RsFrDlcmiStatsDceNoResponseTimeouts_Type()
)
rsFrDlcmiStatsDceNoResponseTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDceNoResponseTimeouts.setStatus("current")
_RsFrDlcmiStatsDiscontinuityTime_Type = TimeTicks
_RsFrDlcmiStatsDiscontinuityTime_Object = MibTableColumn
rsFrDlcmiStatsDiscontinuityTime = _RsFrDlcmiStatsDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 3, 1, 17),
    _RsFrDlcmiStatsDiscontinuityTime_Type()
)
rsFrDlcmiStatsDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrDlcmiStatsDiscontinuityTime.setStatus("current")
_RsFrCircuitTable_Object = MibTable
rsFrCircuitTable = _RsFrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4)
)
if mibBuilder.loadTexts:
    rsFrCircuitTable.setStatus("current")
_RsFrCircuitEntry_Object = MibTableRow
rsFrCircuitEntry = _RsFrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1)
)
rsFrCircuitEntry.setIndexNames(
    (0, "REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitIfIndex"),
    (0, "REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitDlci"),
)
if mibBuilder.loadTexts:
    rsFrCircuitEntry.setStatus("current")
_RsFrCircuitIfIndex_Type = InterfaceIndex
_RsFrCircuitIfIndex_Object = MibTableColumn
rsFrCircuitIfIndex = _RsFrCircuitIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 1),
    _RsFrCircuitIfIndex_Type()
)
rsFrCircuitIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsFrCircuitIfIndex.setStatus("current")
_RsFrCircuitDlci_Type = DLCI
_RsFrCircuitDlci_Object = MibTableColumn
rsFrCircuitDlci = _RsFrCircuitDlci_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 2),
    _RsFrCircuitDlci_Type()
)
rsFrCircuitDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsFrCircuitDlci.setStatus("current")


class _RsFrCircuitState_Type(Integer32):
    """Custom type rsFrCircuitState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 3),
          ("invalid", 1))
    )


_RsFrCircuitState_Type.__name__ = "Integer32"
_RsFrCircuitState_Object = MibTableColumn
rsFrCircuitState = _RsFrCircuitState_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 3),
    _RsFrCircuitState_Type()
)
rsFrCircuitState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrCircuitState.setStatus("current")
_RsFrCircuitReceivedFECNs_Type = Counter32
_RsFrCircuitReceivedFECNs_Object = MibTableColumn
rsFrCircuitReceivedFECNs = _RsFrCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 4),
    _RsFrCircuitReceivedFECNs_Type()
)
rsFrCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitReceivedFECNs.setStatus("current")
_RsFrCircuitReceivedBECNs_Type = Counter32
_RsFrCircuitReceivedBECNs_Object = MibTableColumn
rsFrCircuitReceivedBECNs = _RsFrCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 5),
    _RsFrCircuitReceivedBECNs_Type()
)
rsFrCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitReceivedBECNs.setStatus("current")
_RsFrCircuitSentFrames_Type = Counter32
_RsFrCircuitSentFrames_Object = MibTableColumn
rsFrCircuitSentFrames = _RsFrCircuitSentFrames_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 6),
    _RsFrCircuitSentFrames_Type()
)
rsFrCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitSentFrames.setStatus("current")
_RsFrCircuitSentOctets_Type = Counter32
_RsFrCircuitSentOctets_Object = MibTableColumn
rsFrCircuitSentOctets = _RsFrCircuitSentOctets_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 7),
    _RsFrCircuitSentOctets_Type()
)
rsFrCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitSentOctets.setStatus("current")
_RsFrCircuitReceivedFrames_Type = Counter32
_RsFrCircuitReceivedFrames_Object = MibTableColumn
rsFrCircuitReceivedFrames = _RsFrCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 8),
    _RsFrCircuitReceivedFrames_Type()
)
rsFrCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitReceivedFrames.setStatus("current")
_RsFrCircuitReceivedOctets_Type = Counter32
_RsFrCircuitReceivedOctets_Object = MibTableColumn
rsFrCircuitReceivedOctets = _RsFrCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 9),
    _RsFrCircuitReceivedOctets_Type()
)
rsFrCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitReceivedOctets.setStatus("current")
_RsFrCircuitCreationTime_Type = TimeStamp
_RsFrCircuitCreationTime_Object = MibTableColumn
rsFrCircuitCreationTime = _RsFrCircuitCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 10),
    _RsFrCircuitCreationTime_Type()
)
rsFrCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitCreationTime.setStatus("current")
_RsFrCircuitLastTimeChange_Type = TimeStamp
_RsFrCircuitLastTimeChange_Object = MibTableColumn
rsFrCircuitLastTimeChange = _RsFrCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 11),
    _RsFrCircuitLastTimeChange_Type()
)
rsFrCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitLastTimeChange.setStatus("current")


class _RsFrCircuitCommittedBurst_Type(Integer32):
    """Custom type rsFrCircuitCommittedBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsFrCircuitCommittedBurst_Type.__name__ = "Integer32"
_RsFrCircuitCommittedBurst_Object = MibTableColumn
rsFrCircuitCommittedBurst = _RsFrCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 12),
    _RsFrCircuitCommittedBurst_Type()
)
rsFrCircuitCommittedBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrCircuitCommittedBurst.setStatus("current")


class _RsFrCircuitExcessBurst_Type(Integer32):
    """Custom type rsFrCircuitExcessBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsFrCircuitExcessBurst_Type.__name__ = "Integer32"
_RsFrCircuitExcessBurst_Object = MibTableColumn
rsFrCircuitExcessBurst = _RsFrCircuitExcessBurst_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 13),
    _RsFrCircuitExcessBurst_Type()
)
rsFrCircuitExcessBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrCircuitExcessBurst.setStatus("current")


class _RsFrCircuitThroughput_Type(Integer32):
    """Custom type rsFrCircuitThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RsFrCircuitThroughput_Type.__name__ = "Integer32"
_RsFrCircuitThroughput_Object = MibTableColumn
rsFrCircuitThroughput = _RsFrCircuitThroughput_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 14),
    _RsFrCircuitThroughput_Type()
)
rsFrCircuitThroughput.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrCircuitThroughput.setStatus("current")


class _RsFrCircuitMulticast_Type(Integer32):
    """Custom type rsFrCircuitMulticast based on Integer32"""
    defaultValue = 1

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
        *(("nWay", 4),
          ("oneWay", 2),
          ("twoWay", 3),
          ("unicast", 1))
    )


_RsFrCircuitMulticast_Type.__name__ = "Integer32"
_RsFrCircuitMulticast_Object = MibTableColumn
rsFrCircuitMulticast = _RsFrCircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 15),
    _RsFrCircuitMulticast_Type()
)
rsFrCircuitMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrCircuitMulticast.setStatus("current")


class _RsFrCircuitType_Type(Integer32):
    """Custom type rsFrCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 2),
          ("static", 1))
    )


_RsFrCircuitType_Type.__name__ = "Integer32"
_RsFrCircuitType_Object = MibTableColumn
rsFrCircuitType = _RsFrCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 16),
    _RsFrCircuitType_Type()
)
rsFrCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitType.setStatus("current")
_RsFrCircuitDiscards_Type = Counter32
_RsFrCircuitDiscards_Object = MibTableColumn
rsFrCircuitDiscards = _RsFrCircuitDiscards_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 17),
    _RsFrCircuitDiscards_Type()
)
rsFrCircuitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitDiscards.setStatus("current")
_RsFrCircuitReceivedDEs_Type = Counter32
_RsFrCircuitReceivedDEs_Object = MibTableColumn
rsFrCircuitReceivedDEs = _RsFrCircuitReceivedDEs_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 18),
    _RsFrCircuitReceivedDEs_Type()
)
rsFrCircuitReceivedDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitReceivedDEs.setStatus("current")
_RsFrCircuitSentDEs_Type = Counter32
_RsFrCircuitSentDEs_Object = MibTableColumn
rsFrCircuitSentDEs = _RsFrCircuitSentDEs_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 19),
    _RsFrCircuitSentDEs_Type()
)
rsFrCircuitSentDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitSentDEs.setStatus("current")
_RsFrCircuitLogicalIfIndex_Type = InterfaceIndex
_RsFrCircuitLogicalIfIndex_Object = MibTableColumn
rsFrCircuitLogicalIfIndex = _RsFrCircuitLogicalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 20),
    _RsFrCircuitLogicalIfIndex_Type()
)
rsFrCircuitLogicalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrCircuitLogicalIfIndex.setStatus("current")
_RsFrCircuitRowStatus_Type = RowStatus
_RsFrCircuitRowStatus_Object = MibTableColumn
rsFrCircuitRowStatus = _RsFrCircuitRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 21),
    _RsFrCircuitRowStatus_Type()
)
rsFrCircuitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrCircuitRowStatus.setStatus("current")
_RsFrCircuitSentFECNs_Type = Counter32
_RsFrCircuitSentFECNs_Object = MibTableColumn
rsFrCircuitSentFECNs = _RsFrCircuitSentFECNs_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 22),
    _RsFrCircuitSentFECNs_Type()
)
rsFrCircuitSentFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitSentFECNs.setStatus("current")
_RsFrCircuitSentBECNs_Type = Counter32
_RsFrCircuitSentBECNs_Object = MibTableColumn
rsFrCircuitSentBECNs = _RsFrCircuitSentBECNs_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 1, 4, 1, 23),
    _RsFrCircuitSentBECNs_Type()
)
rsFrCircuitSentBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrCircuitSentBECNs.setStatus("current")
_RsFrSubIfLayer_ObjectIdentity = ObjectIdentity
rsFrSubIfLayer = _RsFrSubIfLayer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2)
)
_RsFrSubIfNextIfIndex_Type = RsNextIfIndex
_RsFrSubIfNextIfIndex_Object = MibScalar
rsFrSubIfNextIfIndex = _RsFrSubIfNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 1),
    _RsFrSubIfNextIfIndex_Type()
)
rsFrSubIfNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsFrSubIfNextIfIndex.setStatus("current")
_RsFrSubIfTable_Object = MibTable
rsFrSubIfTable = _RsFrSubIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rsFrSubIfTable.setStatus("current")
_RsFrSubIfEntry_Object = MibTableRow
rsFrSubIfEntry = _RsFrSubIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 2, 1)
)
rsFrSubIfEntry.setIndexNames(
    (0, "REDSTONE-FRAME-RELAY-MIB", "rsFrSubIfIndex"),
)
if mibBuilder.loadTexts:
    rsFrSubIfEntry.setStatus("current")
_RsFrSubIfIndex_Type = InterfaceIndex
_RsFrSubIfIndex_Object = MibTableColumn
rsFrSubIfIndex = _RsFrSubIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 2, 1, 1),
    _RsFrSubIfIndex_Type()
)
rsFrSubIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsFrSubIfIndex.setStatus("current")
_RsFrSubIfRowStatus_Type = RowStatus
_RsFrSubIfRowStatus_Object = MibTableColumn
rsFrSubIfRowStatus = _RsFrSubIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 2, 1, 2),
    _RsFrSubIfRowStatus_Type()
)
rsFrSubIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrSubIfRowStatus.setStatus("current")
_RsFrSubIfLowerIfIndex_Type = InterfaceIndexOrZero
_RsFrSubIfLowerIfIndex_Object = MibTableColumn
rsFrSubIfLowerIfIndex = _RsFrSubIfLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 2, 1, 3),
    _RsFrSubIfLowerIfIndex_Type()
)
rsFrSubIfLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrSubIfLowerIfIndex.setStatus("current")


class _RsFrSubIfId_Type(Integer32):
    """Custom type rsFrSubIfId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_RsFrSubIfId_Type.__name__ = "Integer32"
_RsFrSubIfId_Object = MibTableColumn
rsFrSubIfId = _RsFrSubIfId_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 2, 1, 4),
    _RsFrSubIfId_Type()
)
rsFrSubIfId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrSubIfId.setStatus("current")
_RsFrSubIfCktTable_Object = MibTable
rsFrSubIfCktTable = _RsFrSubIfCktTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 3)
)
if mibBuilder.loadTexts:
    rsFrSubIfCktTable.setStatus("current")
_RsFrSubIfCktEntry_Object = MibTableRow
rsFrSubIfCktEntry = _RsFrSubIfCktEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 3, 1)
)
rsFrSubIfCktEntry.setIndexNames(
    (0, "REDSTONE-FRAME-RELAY-MIB", "rsFrSubIfIndex"),
    (0, "REDSTONE-FRAME-RELAY-MIB", "rsFrSubIfCktDlci"),
)
if mibBuilder.loadTexts:
    rsFrSubIfCktEntry.setStatus("current")
_RsFrSubIfCktDlci_Type = DLCI
_RsFrSubIfCktDlci_Object = MibTableColumn
rsFrSubIfCktDlci = _RsFrSubIfCktDlci_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 3, 1, 1),
    _RsFrSubIfCktDlci_Type()
)
rsFrSubIfCktDlci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsFrSubIfCktDlci.setStatus("current")
_RsFrSubIfCktRowStatus_Type = RowStatus
_RsFrSubIfCktRowStatus_Object = MibTableColumn
rsFrSubIfCktRowStatus = _RsFrSubIfCktRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 1, 2, 3, 1, 2),
    _RsFrSubIfCktRowStatus_Type()
)
rsFrSubIfCktRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsFrSubIfCktRowStatus.setStatus("current")
_RsFrConformance_ObjectIdentity = ObjectIdentity
rsFrConformance = _RsFrConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 4)
)
_RsFrCompliances_ObjectIdentity = ObjectIdentity
rsFrCompliances = _RsFrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 4, 1)
)
_RsFrGroups_ObjectIdentity = ObjectIdentity
rsFrGroups = _RsFrGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 4, 2)
)

# Managed Objects groups

rsFrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 4, 2, 1)
)
rsFrGroup.setObjects(
      *(("REDSTONE-FRAME-RELAY-MIB", "rsFrNextIfIndex"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiIfIndex"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiState"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiAddress"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiAddressLen"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiPollingInterval"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiFullEnquiryInterval"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiErrorThreshold"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiMonitoredEvents"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiMaxSupportedVCs"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiMulticast"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatus"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiRowStatus"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiLowerIfIndex"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiRole"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiDcePollingInterval"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiDceErrorThreshold"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiDceMonitoredEvents"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDteEnquiries"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDteFullEnquiries"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDteEnquiryResponses"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDteFullEnquiryResponses"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDteAsyncUpdates"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDteUnknownRxMessages"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDteLossOfSequences"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDteNoResponseTimeouts"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDceEnquiries"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDceFullEnquiries"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDceEnquiryResponses"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDceFullEnquiryResponses"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDceAsyncUpdates"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDceUnknownRxMessages"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDceLossOfSequences"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDceNoResponseTimeouts"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrDlcmiStatsDiscontinuityTime"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitState"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitReceivedFECNs"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitReceivedBECNs"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitSentFrames"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitSentOctets"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitReceivedFrames"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitReceivedOctets"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitCreationTime"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitLastTimeChange"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitCommittedBurst"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitExcessBurst"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitThroughput"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitMulticast"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitType"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitDiscards"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitReceivedDEs"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitSentDEs"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitLogicalIfIndex"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitRowStatus"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitSentFECNs"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrCircuitSentBECNs"))
)
if mibBuilder.loadTexts:
    rsFrGroup.setStatus("current")

rsFrSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 4, 2, 2)
)
rsFrSubIfGroup.setObjects(
      *(("REDSTONE-FRAME-RELAY-MIB", "rsFrSubIfNextIfIndex"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrSubIfRowStatus"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrSubIfLowerIfIndex"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrSubIfId"),
        ("REDSTONE-FRAME-RELAY-MIB", "rsFrSubIfCktRowStatus"))
)
if mibBuilder.loadTexts:
    rsFrSubIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsFrCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 10, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsFrCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-FRAME-RELAY-MIB",
    **{"rsFrameRelayMIB": rsFrameRelayMIB,
       "rsFrObjects": rsFrObjects,
       "rsFrIfLayer": rsFrIfLayer,
       "rsFrNextIfIndex": rsFrNextIfIndex,
       "rsFrDlcmiTable": rsFrDlcmiTable,
       "rsFrDlcmiEntry": rsFrDlcmiEntry,
       "rsFrDlcmiIfIndex": rsFrDlcmiIfIndex,
       "rsFrDlcmiState": rsFrDlcmiState,
       "rsFrDlcmiAddress": rsFrDlcmiAddress,
       "rsFrDlcmiAddressLen": rsFrDlcmiAddressLen,
       "rsFrDlcmiPollingInterval": rsFrDlcmiPollingInterval,
       "rsFrDlcmiFullEnquiryInterval": rsFrDlcmiFullEnquiryInterval,
       "rsFrDlcmiErrorThreshold": rsFrDlcmiErrorThreshold,
       "rsFrDlcmiMonitoredEvents": rsFrDlcmiMonitoredEvents,
       "rsFrDlcmiMaxSupportedVCs": rsFrDlcmiMaxSupportedVCs,
       "rsFrDlcmiMulticast": rsFrDlcmiMulticast,
       "rsFrDlcmiStatus": rsFrDlcmiStatus,
       "rsFrDlcmiRowStatus": rsFrDlcmiRowStatus,
       "rsFrDlcmiLowerIfIndex": rsFrDlcmiLowerIfIndex,
       "rsFrDlcmiRole": rsFrDlcmiRole,
       "rsFrDlcmiDcePollingInterval": rsFrDlcmiDcePollingInterval,
       "rsFrDlcmiDceErrorThreshold": rsFrDlcmiDceErrorThreshold,
       "rsFrDlcmiDceMonitoredEvents": rsFrDlcmiDceMonitoredEvents,
       "rsFrDlcmiStatsTable": rsFrDlcmiStatsTable,
       "rsFrDlcmiStatsEntry": rsFrDlcmiStatsEntry,
       "rsFrDlcmiStatsDteEnquiries": rsFrDlcmiStatsDteEnquiries,
       "rsFrDlcmiStatsDteFullEnquiries": rsFrDlcmiStatsDteFullEnquiries,
       "rsFrDlcmiStatsDteEnquiryResponses": rsFrDlcmiStatsDteEnquiryResponses,
       "rsFrDlcmiStatsDteFullEnquiryResponses": rsFrDlcmiStatsDteFullEnquiryResponses,
       "rsFrDlcmiStatsDteAsyncUpdates": rsFrDlcmiStatsDteAsyncUpdates,
       "rsFrDlcmiStatsDteUnknownRxMessages": rsFrDlcmiStatsDteUnknownRxMessages,
       "rsFrDlcmiStatsDteLossOfSequences": rsFrDlcmiStatsDteLossOfSequences,
       "rsFrDlcmiStatsDteNoResponseTimeouts": rsFrDlcmiStatsDteNoResponseTimeouts,
       "rsFrDlcmiStatsDceEnquiries": rsFrDlcmiStatsDceEnquiries,
       "rsFrDlcmiStatsDceFullEnquiries": rsFrDlcmiStatsDceFullEnquiries,
       "rsFrDlcmiStatsDceEnquiryResponses": rsFrDlcmiStatsDceEnquiryResponses,
       "rsFrDlcmiStatsDceFullEnquiryResponses": rsFrDlcmiStatsDceFullEnquiryResponses,
       "rsFrDlcmiStatsDceAsyncUpdates": rsFrDlcmiStatsDceAsyncUpdates,
       "rsFrDlcmiStatsDceUnknownRxMessages": rsFrDlcmiStatsDceUnknownRxMessages,
       "rsFrDlcmiStatsDceLossOfSequences": rsFrDlcmiStatsDceLossOfSequences,
       "rsFrDlcmiStatsDceNoResponseTimeouts": rsFrDlcmiStatsDceNoResponseTimeouts,
       "rsFrDlcmiStatsDiscontinuityTime": rsFrDlcmiStatsDiscontinuityTime,
       "rsFrCircuitTable": rsFrCircuitTable,
       "rsFrCircuitEntry": rsFrCircuitEntry,
       "rsFrCircuitIfIndex": rsFrCircuitIfIndex,
       "rsFrCircuitDlci": rsFrCircuitDlci,
       "rsFrCircuitState": rsFrCircuitState,
       "rsFrCircuitReceivedFECNs": rsFrCircuitReceivedFECNs,
       "rsFrCircuitReceivedBECNs": rsFrCircuitReceivedBECNs,
       "rsFrCircuitSentFrames": rsFrCircuitSentFrames,
       "rsFrCircuitSentOctets": rsFrCircuitSentOctets,
       "rsFrCircuitReceivedFrames": rsFrCircuitReceivedFrames,
       "rsFrCircuitReceivedOctets": rsFrCircuitReceivedOctets,
       "rsFrCircuitCreationTime": rsFrCircuitCreationTime,
       "rsFrCircuitLastTimeChange": rsFrCircuitLastTimeChange,
       "rsFrCircuitCommittedBurst": rsFrCircuitCommittedBurst,
       "rsFrCircuitExcessBurst": rsFrCircuitExcessBurst,
       "rsFrCircuitThroughput": rsFrCircuitThroughput,
       "rsFrCircuitMulticast": rsFrCircuitMulticast,
       "rsFrCircuitType": rsFrCircuitType,
       "rsFrCircuitDiscards": rsFrCircuitDiscards,
       "rsFrCircuitReceivedDEs": rsFrCircuitReceivedDEs,
       "rsFrCircuitSentDEs": rsFrCircuitSentDEs,
       "rsFrCircuitLogicalIfIndex": rsFrCircuitLogicalIfIndex,
       "rsFrCircuitRowStatus": rsFrCircuitRowStatus,
       "rsFrCircuitSentFECNs": rsFrCircuitSentFECNs,
       "rsFrCircuitSentBECNs": rsFrCircuitSentBECNs,
       "rsFrSubIfLayer": rsFrSubIfLayer,
       "rsFrSubIfNextIfIndex": rsFrSubIfNextIfIndex,
       "rsFrSubIfTable": rsFrSubIfTable,
       "rsFrSubIfEntry": rsFrSubIfEntry,
       "rsFrSubIfIndex": rsFrSubIfIndex,
       "rsFrSubIfRowStatus": rsFrSubIfRowStatus,
       "rsFrSubIfLowerIfIndex": rsFrSubIfLowerIfIndex,
       "rsFrSubIfId": rsFrSubIfId,
       "rsFrSubIfCktTable": rsFrSubIfCktTable,
       "rsFrSubIfCktEntry": rsFrSubIfCktEntry,
       "rsFrSubIfCktDlci": rsFrSubIfCktDlci,
       "rsFrSubIfCktRowStatus": rsFrSubIfCktRowStatus,
       "rsFrConformance": rsFrConformance,
       "rsFrCompliances": rsFrCompliances,
       "rsFrCompliance": rsFrCompliance,
       "rsFrGroups": rsFrGroups,
       "rsFrGroup": rsFrGroup,
       "rsFrSubIfGroup": rsFrSubIfGroup}
)
