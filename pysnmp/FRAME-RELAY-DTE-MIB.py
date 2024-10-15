# SNMP MIB module (FRAME-RELAY-DTE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FRAME-RELAY-DTE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:18 2024
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
 transmission) = mibBuilder.importSymbols(
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
    "transmission")

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

frameRelayDTE = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 32)
)
frameRelayDTE.setRevisions(
        ("1997-05-01 02:29",
         "1992-04-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DLCI(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8388607),
    )



# MIB Managed Objects in the order of their OIDs

_FrameRelayTraps_ObjectIdentity = ObjectIdentity
frameRelayTraps = _FrameRelayTraps_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 32, 0)
)
_FrDlcmiTable_Object = MibTable
frDlcmiTable = _FrDlcmiTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1)
)
if mibBuilder.loadTexts:
    frDlcmiTable.setStatus("current")
_FrDlcmiEntry_Object = MibTableRow
frDlcmiEntry = _FrDlcmiEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1)
)
frDlcmiEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frDlcmiIfIndex"),
)
if mibBuilder.loadTexts:
    frDlcmiEntry.setStatus("current")
_FrDlcmiIfIndex_Type = InterfaceIndex
_FrDlcmiIfIndex_Object = MibTableColumn
frDlcmiIfIndex = _FrDlcmiIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 1),
    _FrDlcmiIfIndex_Type()
)
frDlcmiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDlcmiIfIndex.setStatus("current")


class _FrDlcmiState_Type(Integer32):
    """Custom type frDlcmiState based on Integer32"""
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


_FrDlcmiState_Type.__name__ = "Integer32"
_FrDlcmiState_Object = MibTableColumn
frDlcmiState = _FrDlcmiState_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 2),
    _FrDlcmiState_Type()
)
frDlcmiState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frDlcmiState.setStatus("current")


class _FrDlcmiAddress_Type(Integer32):
    """Custom type frDlcmiAddress based on Integer32"""
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


_FrDlcmiAddress_Type.__name__ = "Integer32"
_FrDlcmiAddress_Object = MibTableColumn
frDlcmiAddress = _FrDlcmiAddress_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 3),
    _FrDlcmiAddress_Type()
)
frDlcmiAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frDlcmiAddress.setStatus("current")


class _FrDlcmiAddressLen_Type(Integer32):
    """Custom type frDlcmiAddressLen based on Integer32"""
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


_FrDlcmiAddressLen_Type.__name__ = "Integer32"
_FrDlcmiAddressLen_Object = MibTableColumn
frDlcmiAddressLen = _FrDlcmiAddressLen_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 4),
    _FrDlcmiAddressLen_Type()
)
frDlcmiAddressLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frDlcmiAddressLen.setStatus("current")


class _FrDlcmiPollingInterval_Type(Integer32):
    """Custom type frDlcmiPollingInterval based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 30),
    )


_FrDlcmiPollingInterval_Type.__name__ = "Integer32"
_FrDlcmiPollingInterval_Object = MibTableColumn
frDlcmiPollingInterval = _FrDlcmiPollingInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 5),
    _FrDlcmiPollingInterval_Type()
)
frDlcmiPollingInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frDlcmiPollingInterval.setStatus("current")
if mibBuilder.loadTexts:
    frDlcmiPollingInterval.setUnits("seconds")


class _FrDlcmiFullEnquiryInterval_Type(Integer32):
    """Custom type frDlcmiFullEnquiryInterval based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FrDlcmiFullEnquiryInterval_Type.__name__ = "Integer32"
_FrDlcmiFullEnquiryInterval_Object = MibTableColumn
frDlcmiFullEnquiryInterval = _FrDlcmiFullEnquiryInterval_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 6),
    _FrDlcmiFullEnquiryInterval_Type()
)
frDlcmiFullEnquiryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frDlcmiFullEnquiryInterval.setStatus("current")


class _FrDlcmiErrorThreshold_Type(Integer32):
    """Custom type frDlcmiErrorThreshold based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrDlcmiErrorThreshold_Type.__name__ = "Integer32"
_FrDlcmiErrorThreshold_Object = MibTableColumn
frDlcmiErrorThreshold = _FrDlcmiErrorThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 7),
    _FrDlcmiErrorThreshold_Type()
)
frDlcmiErrorThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frDlcmiErrorThreshold.setStatus("current")


class _FrDlcmiMonitoredEvents_Type(Integer32):
    """Custom type frDlcmiMonitoredEvents based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FrDlcmiMonitoredEvents_Type.__name__ = "Integer32"
_FrDlcmiMonitoredEvents_Object = MibTableColumn
frDlcmiMonitoredEvents = _FrDlcmiMonitoredEvents_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 8),
    _FrDlcmiMonitoredEvents_Type()
)
frDlcmiMonitoredEvents.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frDlcmiMonitoredEvents.setStatus("current")
_FrDlcmiMaxSupportedVCs_Type = DLCI
_FrDlcmiMaxSupportedVCs_Object = MibTableColumn
frDlcmiMaxSupportedVCs = _FrDlcmiMaxSupportedVCs_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 9),
    _FrDlcmiMaxSupportedVCs_Type()
)
frDlcmiMaxSupportedVCs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frDlcmiMaxSupportedVCs.setStatus("current")


class _FrDlcmiMulticast_Type(Integer32):
    """Custom type frDlcmiMulticast based on Integer32"""
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


_FrDlcmiMulticast_Type.__name__ = "Integer32"
_FrDlcmiMulticast_Object = MibTableColumn
frDlcmiMulticast = _FrDlcmiMulticast_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 10),
    _FrDlcmiMulticast_Type()
)
frDlcmiMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frDlcmiMulticast.setStatus("current")


class _FrDlcmiStatus_Type(Integer32):
    """Custom type frDlcmiStatus based on Integer32"""
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


_FrDlcmiStatus_Type.__name__ = "Integer32"
_FrDlcmiStatus_Object = MibTableColumn
frDlcmiStatus = _FrDlcmiStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 11),
    _FrDlcmiStatus_Type()
)
frDlcmiStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frDlcmiStatus.setStatus("current")
_FrDlcmiRowStatus_Type = RowStatus
_FrDlcmiRowStatus_Object = MibTableColumn
frDlcmiRowStatus = _FrDlcmiRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 1, 1, 12),
    _FrDlcmiRowStatus_Type()
)
frDlcmiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frDlcmiRowStatus.setStatus("current")
_FrCircuitTable_Object = MibTable
frCircuitTable = _FrCircuitTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2)
)
if mibBuilder.loadTexts:
    frCircuitTable.setStatus("current")
_FrCircuitEntry_Object = MibTableRow
frCircuitEntry = _FrCircuitEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1)
)
frCircuitEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    frCircuitEntry.setStatus("current")
_FrCircuitIfIndex_Type = InterfaceIndex
_FrCircuitIfIndex_Object = MibTableColumn
frCircuitIfIndex = _FrCircuitIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 1),
    _FrCircuitIfIndex_Type()
)
frCircuitIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitIfIndex.setStatus("current")
_FrCircuitDlci_Type = DLCI
_FrCircuitDlci_Object = MibTableColumn
frCircuitDlci = _FrCircuitDlci_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 2),
    _FrCircuitDlci_Type()
)
frCircuitDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitDlci.setStatus("current")


class _FrCircuitState_Type(Integer32):
    """Custom type frCircuitState based on Integer32"""
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


_FrCircuitState_Type.__name__ = "Integer32"
_FrCircuitState_Object = MibTableColumn
frCircuitState = _FrCircuitState_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 3),
    _FrCircuitState_Type()
)
frCircuitState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frCircuitState.setStatus("current")
_FrCircuitReceivedFECNs_Type = Counter32
_FrCircuitReceivedFECNs_Object = MibTableColumn
frCircuitReceivedFECNs = _FrCircuitReceivedFECNs_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 4),
    _FrCircuitReceivedFECNs_Type()
)
frCircuitReceivedFECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedFECNs.setStatus("current")
_FrCircuitReceivedBECNs_Type = Counter32
_FrCircuitReceivedBECNs_Object = MibTableColumn
frCircuitReceivedBECNs = _FrCircuitReceivedBECNs_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 5),
    _FrCircuitReceivedBECNs_Type()
)
frCircuitReceivedBECNs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedBECNs.setStatus("current")
_FrCircuitSentFrames_Type = Counter32
_FrCircuitSentFrames_Object = MibTableColumn
frCircuitSentFrames = _FrCircuitSentFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 6),
    _FrCircuitSentFrames_Type()
)
frCircuitSentFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitSentFrames.setStatus("current")
_FrCircuitSentOctets_Type = Counter32
_FrCircuitSentOctets_Object = MibTableColumn
frCircuitSentOctets = _FrCircuitSentOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 7),
    _FrCircuitSentOctets_Type()
)
frCircuitSentOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitSentOctets.setStatus("current")
_FrCircuitReceivedFrames_Type = Counter32
_FrCircuitReceivedFrames_Object = MibTableColumn
frCircuitReceivedFrames = _FrCircuitReceivedFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 8),
    _FrCircuitReceivedFrames_Type()
)
frCircuitReceivedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedFrames.setStatus("current")
_FrCircuitReceivedOctets_Type = Counter32
_FrCircuitReceivedOctets_Object = MibTableColumn
frCircuitReceivedOctets = _FrCircuitReceivedOctets_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 9),
    _FrCircuitReceivedOctets_Type()
)
frCircuitReceivedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedOctets.setStatus("current")
_FrCircuitCreationTime_Type = TimeStamp
_FrCircuitCreationTime_Object = MibTableColumn
frCircuitCreationTime = _FrCircuitCreationTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 10),
    _FrCircuitCreationTime_Type()
)
frCircuitCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitCreationTime.setStatus("current")
_FrCircuitLastTimeChange_Type = TimeStamp
_FrCircuitLastTimeChange_Object = MibTableColumn
frCircuitLastTimeChange = _FrCircuitLastTimeChange_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 11),
    _FrCircuitLastTimeChange_Type()
)
frCircuitLastTimeChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitLastTimeChange.setStatus("current")


class _FrCircuitCommittedBurst_Type(Integer32):
    """Custom type frCircuitCommittedBurst based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrCircuitCommittedBurst_Type.__name__ = "Integer32"
_FrCircuitCommittedBurst_Object = MibTableColumn
frCircuitCommittedBurst = _FrCircuitCommittedBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 12),
    _FrCircuitCommittedBurst_Type()
)
frCircuitCommittedBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frCircuitCommittedBurst.setStatus("current")


class _FrCircuitExcessBurst_Type(Integer32):
    """Custom type frCircuitExcessBurst based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrCircuitExcessBurst_Type.__name__ = "Integer32"
_FrCircuitExcessBurst_Object = MibTableColumn
frCircuitExcessBurst = _FrCircuitExcessBurst_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 13),
    _FrCircuitExcessBurst_Type()
)
frCircuitExcessBurst.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frCircuitExcessBurst.setStatus("current")


class _FrCircuitThroughput_Type(Integer32):
    """Custom type frCircuitThroughput based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FrCircuitThroughput_Type.__name__ = "Integer32"
_FrCircuitThroughput_Object = MibTableColumn
frCircuitThroughput = _FrCircuitThroughput_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 14),
    _FrCircuitThroughput_Type()
)
frCircuitThroughput.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frCircuitThroughput.setStatus("current")


class _FrCircuitMulticast_Type(Integer32):
    """Custom type frCircuitMulticast based on Integer32"""
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


_FrCircuitMulticast_Type.__name__ = "Integer32"
_FrCircuitMulticast_Object = MibTableColumn
frCircuitMulticast = _FrCircuitMulticast_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 15),
    _FrCircuitMulticast_Type()
)
frCircuitMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frCircuitMulticast.setStatus("current")


class _FrCircuitType_Type(Integer32):
    """Custom type frCircuitType based on Integer32"""
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


_FrCircuitType_Type.__name__ = "Integer32"
_FrCircuitType_Object = MibTableColumn
frCircuitType = _FrCircuitType_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 16),
    _FrCircuitType_Type()
)
frCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitType.setStatus("current")
_FrCircuitDiscards_Type = Counter32
_FrCircuitDiscards_Object = MibTableColumn
frCircuitDiscards = _FrCircuitDiscards_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 17),
    _FrCircuitDiscards_Type()
)
frCircuitDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitDiscards.setStatus("current")
_FrCircuitReceivedDEs_Type = Counter32
_FrCircuitReceivedDEs_Object = MibTableColumn
frCircuitReceivedDEs = _FrCircuitReceivedDEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 18),
    _FrCircuitReceivedDEs_Type()
)
frCircuitReceivedDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitReceivedDEs.setStatus("current")
_FrCircuitSentDEs_Type = Counter32
_FrCircuitSentDEs_Object = MibTableColumn
frCircuitSentDEs = _FrCircuitSentDEs_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 19),
    _FrCircuitSentDEs_Type()
)
frCircuitSentDEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frCircuitSentDEs.setStatus("current")
_FrCircuitLogicalIfIndex_Type = InterfaceIndex
_FrCircuitLogicalIfIndex_Object = MibTableColumn
frCircuitLogicalIfIndex = _FrCircuitLogicalIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 20),
    _FrCircuitLogicalIfIndex_Type()
)
frCircuitLogicalIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frCircuitLogicalIfIndex.setStatus("current")
_FrCircuitRowStatus_Type = RowStatus
_FrCircuitRowStatus_Object = MibTableColumn
frCircuitRowStatus = _FrCircuitRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 2, 1, 21),
    _FrCircuitRowStatus_Type()
)
frCircuitRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    frCircuitRowStatus.setStatus("current")
_FrErrTable_Object = MibTable
frErrTable = _FrErrTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3)
)
if mibBuilder.loadTexts:
    frErrTable.setStatus("current")
_FrErrEntry_Object = MibTableRow
frErrEntry = _FrErrEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1)
)
frErrEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frErrIfIndex"),
)
if mibBuilder.loadTexts:
    frErrEntry.setStatus("current")
_FrErrIfIndex_Type = InterfaceIndex
_FrErrIfIndex_Object = MibTableColumn
frErrIfIndex = _FrErrIfIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 1),
    _FrErrIfIndex_Type()
)
frErrIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrIfIndex.setStatus("current")


class _FrErrType_Type(Integer32):
    """Custom type frErrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("dlcmiProtoErr", 6),
          ("dlcmiSequenceErr", 8),
          ("dlcmiUnknownIE", 7),
          ("dlcmiUnknownRpt", 9),
          ("illegalAddress", 4),
          ("noErrorSinceReset", 10),
          ("receiveLong", 3),
          ("receiveShort", 2),
          ("unknownAddress", 5),
          ("unknownError", 1))
    )


_FrErrType_Type.__name__ = "Integer32"
_FrErrType_Object = MibTableColumn
frErrType = _FrErrType_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 2),
    _FrErrType_Type()
)
frErrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrType.setStatus("current")


class _FrErrData_Type(OctetString):
    """Custom type frErrData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1600),
    )


_FrErrData_Type.__name__ = "OctetString"
_FrErrData_Object = MibTableColumn
frErrData = _FrErrData_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 3),
    _FrErrData_Type()
)
frErrData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrData.setStatus("current")
_FrErrTime_Type = TimeStamp
_FrErrTime_Object = MibTableColumn
frErrTime = _FrErrTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 4),
    _FrErrTime_Type()
)
frErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrTime.setStatus("current")
_FrErrFaults_Type = Counter32
_FrErrFaults_Object = MibTableColumn
frErrFaults = _FrErrFaults_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 5),
    _FrErrFaults_Type()
)
frErrFaults.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrFaults.setStatus("current")
_FrErrFaultTime_Type = TimeStamp
_FrErrFaultTime_Object = MibTableColumn
frErrFaultTime = _FrErrFaultTime_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 3, 1, 6),
    _FrErrFaultTime_Type()
)
frErrFaultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    frErrFaultTime.setStatus("current")
_FrameRelayTrapControl_ObjectIdentity = ObjectIdentity
frameRelayTrapControl = _FrameRelayTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 32, 4)
)


class _FrTrapState_Type(Integer32):
    """Custom type frTrapState based on Integer32"""
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


_FrTrapState_Type.__name__ = "Integer32"
_FrTrapState_Object = MibScalar
frTrapState = _FrTrapState_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 4, 1),
    _FrTrapState_Type()
)
frTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frTrapState.setStatus("current")


class _FrTrapMaxRate_Type(Integer32):
    """Custom type frTrapMaxRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600000),
    )


_FrTrapMaxRate_Type.__name__ = "Integer32"
_FrTrapMaxRate_Object = MibScalar
frTrapMaxRate = _FrTrapMaxRate_Object(
    (1, 3, 6, 1, 2, 1, 10, 32, 4, 2),
    _FrTrapMaxRate_Type()
)
frTrapMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    frTrapMaxRate.setStatus("current")
_FrConformance_ObjectIdentity = ObjectIdentity
frConformance = _FrConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 32, 6)
)
_FrGroups_ObjectIdentity = ObjectIdentity
frGroups = _FrGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 1)
)
_FrCompliances_ObjectIdentity = ObjectIdentity
frCompliances = _FrCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 2)
)

# Managed Objects groups

frPortGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 1)
)
frPortGroup.setObjects(
      *(("FRAME-RELAY-DTE-MIB", "frDlcmiIfIndex"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiState"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiAddress"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiAddressLen"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiPollingInterval"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiFullEnquiryInterval"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiErrorThreshold"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiMonitoredEvents"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiMaxSupportedVCs"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiMulticast"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiStatus"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiRowStatus"))
)
if mibBuilder.loadTexts:
    frPortGroup.setStatus("current")

frCircuitGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 2)
)
frCircuitGroup.setObjects(
      *(("FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitState"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitReceivedFECNs"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitReceivedBECNs"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitSentFrames"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitSentOctets"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitReceivedFrames"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitReceivedOctets"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitCreationTime"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitLastTimeChange"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitCommittedBurst"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitExcessBurst"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitThroughput"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitMulticast"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitType"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitDiscards"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitReceivedDEs"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitSentDEs"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitLogicalIfIndex"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitRowStatus"))
)
if mibBuilder.loadTexts:
    frCircuitGroup.setStatus("current")

frTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 3)
)
frTrapGroup.setObjects(
      *(("FRAME-RELAY-DTE-MIB", "frTrapState"),
        ("FRAME-RELAY-DTE-MIB", "frTrapMaxRate"))
)
if mibBuilder.loadTexts:
    frTrapGroup.setStatus("current")

frErrGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 4)
)
frErrGroup.setObjects(
      *(("FRAME-RELAY-DTE-MIB", "frErrIfIndex"),
        ("FRAME-RELAY-DTE-MIB", "frErrType"),
        ("FRAME-RELAY-DTE-MIB", "frErrData"),
        ("FRAME-RELAY-DTE-MIB", "frErrTime"),
        ("FRAME-RELAY-DTE-MIB", "frErrFaults"),
        ("FRAME-RELAY-DTE-MIB", "frErrFaultTime"))
)
if mibBuilder.loadTexts:
    frErrGroup.setStatus("current")

frPortGroup0 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 6)
)
frPortGroup0.setObjects(
      *(("FRAME-RELAY-DTE-MIB", "frDlcmiIfIndex"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiState"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiAddress"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiAddressLen"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiPollingInterval"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiFullEnquiryInterval"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiErrorThreshold"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiMonitoredEvents"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiMaxSupportedVCs"),
        ("FRAME-RELAY-DTE-MIB", "frDlcmiMulticast"))
)
if mibBuilder.loadTexts:
    frPortGroup0.setStatus("current")

frCircuitGroup0 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 7)
)
frCircuitGroup0.setObjects(
      *(("FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitState"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitReceivedFECNs"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitReceivedBECNs"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitSentFrames"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitSentOctets"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitReceivedFrames"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitReceivedOctets"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitCreationTime"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitLastTimeChange"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitCommittedBurst"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitExcessBurst"),
        ("FRAME-RELAY-DTE-MIB", "frCircuitThroughput"))
)
if mibBuilder.loadTexts:
    frCircuitGroup0.setStatus("current")

frErrGroup0 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 8)
)
frErrGroup0.setObjects(
      *(("FRAME-RELAY-DTE-MIB", "frErrIfIndex"),
        ("FRAME-RELAY-DTE-MIB", "frErrType"),
        ("FRAME-RELAY-DTE-MIB", "frErrData"),
        ("FRAME-RELAY-DTE-MIB", "frErrTime"))
)
if mibBuilder.loadTexts:
    frErrGroup0.setStatus("current")

frTrapGroup0 = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 9)
)
frTrapGroup0.setObjects(
    ("FRAME-RELAY-DTE-MIB", "frTrapState")
)
if mibBuilder.loadTexts:
    frTrapGroup0.setStatus("current")


# Notification objects

frDLCIStatusChange = NotificationType(
    (1, 3, 6, 1, 2, 1, 10, 32, 0, 1)
)
frDLCIStatusChange.setObjects(
    ("FRAME-RELAY-DTE-MIB", "frCircuitState")
)
if mibBuilder.loadTexts:
    frDLCIStatusChange.setStatus(
        "current"
    )


# Notifications groups

frNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 1, 5)
)
frNotificationGroup.setObjects(
    ("FRAME-RELAY-DTE-MIB", "frDLCIStatusChange")
)
if mibBuilder.loadTexts:
    frNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

frCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 2, 1)
)
if mibBuilder.loadTexts:
    frCompliance.setStatus(
        "current"
    )

frCompliance0 = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 32, 6, 2, 2)
)
if mibBuilder.loadTexts:
    frCompliance0.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FRAME-RELAY-DTE-MIB",
    **{"DLCI": DLCI,
       "frameRelayDTE": frameRelayDTE,
       "frameRelayTraps": frameRelayTraps,
       "frDLCIStatusChange": frDLCIStatusChange,
       "frDlcmiTable": frDlcmiTable,
       "frDlcmiEntry": frDlcmiEntry,
       "frDlcmiIfIndex": frDlcmiIfIndex,
       "frDlcmiState": frDlcmiState,
       "frDlcmiAddress": frDlcmiAddress,
       "frDlcmiAddressLen": frDlcmiAddressLen,
       "frDlcmiPollingInterval": frDlcmiPollingInterval,
       "frDlcmiFullEnquiryInterval": frDlcmiFullEnquiryInterval,
       "frDlcmiErrorThreshold": frDlcmiErrorThreshold,
       "frDlcmiMonitoredEvents": frDlcmiMonitoredEvents,
       "frDlcmiMaxSupportedVCs": frDlcmiMaxSupportedVCs,
       "frDlcmiMulticast": frDlcmiMulticast,
       "frDlcmiStatus": frDlcmiStatus,
       "frDlcmiRowStatus": frDlcmiRowStatus,
       "frCircuitTable": frCircuitTable,
       "frCircuitEntry": frCircuitEntry,
       "frCircuitIfIndex": frCircuitIfIndex,
       "frCircuitDlci": frCircuitDlci,
       "frCircuitState": frCircuitState,
       "frCircuitReceivedFECNs": frCircuitReceivedFECNs,
       "frCircuitReceivedBECNs": frCircuitReceivedBECNs,
       "frCircuitSentFrames": frCircuitSentFrames,
       "frCircuitSentOctets": frCircuitSentOctets,
       "frCircuitReceivedFrames": frCircuitReceivedFrames,
       "frCircuitReceivedOctets": frCircuitReceivedOctets,
       "frCircuitCreationTime": frCircuitCreationTime,
       "frCircuitLastTimeChange": frCircuitLastTimeChange,
       "frCircuitCommittedBurst": frCircuitCommittedBurst,
       "frCircuitExcessBurst": frCircuitExcessBurst,
       "frCircuitThroughput": frCircuitThroughput,
       "frCircuitMulticast": frCircuitMulticast,
       "frCircuitType": frCircuitType,
       "frCircuitDiscards": frCircuitDiscards,
       "frCircuitReceivedDEs": frCircuitReceivedDEs,
       "frCircuitSentDEs": frCircuitSentDEs,
       "frCircuitLogicalIfIndex": frCircuitLogicalIfIndex,
       "frCircuitRowStatus": frCircuitRowStatus,
       "frErrTable": frErrTable,
       "frErrEntry": frErrEntry,
       "frErrIfIndex": frErrIfIndex,
       "frErrType": frErrType,
       "frErrData": frErrData,
       "frErrTime": frErrTime,
       "frErrFaults": frErrFaults,
       "frErrFaultTime": frErrFaultTime,
       "frameRelayTrapControl": frameRelayTrapControl,
       "frTrapState": frTrapState,
       "frTrapMaxRate": frTrapMaxRate,
       "frConformance": frConformance,
       "frGroups": frGroups,
       "frPortGroup": frPortGroup,
       "frCircuitGroup": frCircuitGroup,
       "frTrapGroup": frTrapGroup,
       "frErrGroup": frErrGroup,
       "frNotificationGroup": frNotificationGroup,
       "frPortGroup0": frPortGroup0,
       "frCircuitGroup0": frCircuitGroup0,
       "frErrGroup0": frErrGroup0,
       "frTrapGroup0": frTrapGroup0,
       "frCompliances": frCompliances,
       "frCompliance": frCompliance,
       "frCompliance0": frCompliance0}
)
