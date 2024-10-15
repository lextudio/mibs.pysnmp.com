# SNMP MIB module (DC-BGP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DC-BGP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:52:22 2024
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

(BfdSessionStatus,) = mibBuilder.importSymbols(
    "DC-MASTER-TC",
    "BfdSessionStatus")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

bgpMib = ModuleIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1)
)
bgpMib.setRevisions(
        ("2013-08-29 00:00",
         "2013-04-02 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class BgpIdentifier(OctetString, TextualConvention):
    status = "current"
    displayHint = "4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class BgpAfi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              25)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("l2vpn", 25),
          ("other", 0))
    )



class BgpSafi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              65,
              128)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("labeled", 4),
          ("mplsBgpVpn", 128),
          ("multicast", 2),
          ("none", 0),
          ("unicast", 1),
          ("vpls", 65))
    )



class BgpAutonomousSystemNumber(Unsigned32, TextualConvention):
    status = "current"


class BgpAsSize(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fourOctet", 2),
          ("twoOctet", 1))
    )



class BgpAdminStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("adminStatusDown", 2),
          ("adminStatusUp", 1))
    )



class BgpOperStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )



class BgpOriginCode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("originEgp", 1),
          ("originIgp", 0),
          ("originIncomplete", 2))
    )



class BgpMedDeltaType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("decrement", 2),
          ("increment", 1))
    )



class BgpIpMatchType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nextHopAddr", 3),
          ("nlriAddr", 1),
          ("sourceAddr", 2))
    )



class BgpPermitOrDeny(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deny", 2),
          ("permit", 1))
    )



class BgpDropOrWarn(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("warn", 2))
    )



class BgpIbgpOrEbgp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ebgp", 2),
          ("ebgpconfed", 3),
          ("ibgp", 1))
    )



class BgpPeerOrAfm(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("afmIndex", 2),
          ("peerIndex", 1))
    )



class BgpAsPathAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("remMatch", 2),
          ("remMatchAndSet", 3),
          ("set", 1))
    )



class BgpAggregateOptions(Integer32, TextualConvention):
    status = "current"
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
        *(("asAppend", 5),
          ("asSet", 3),
          ("none", 1),
          ("summary", 2),
          ("summaryAsAppend", 6),
          ("summaryAsSet", 4))
    )



class BgpMjStatus(Integer32, TextualConvention):
    status = "current"
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
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("mjFailed", 10),
          ("mjFailedToRegister", 8),
          ("mjFailingOver", 9),
          ("mjJoinActive", 4),
          ("mjJoinGone", 7),
          ("mjNoPartner", 11),
          ("mjNotJoined", 1),
          ("mjSentAddJoin", 2),
          ("mjSentDelJoin", 5),
          ("mjSentRegister", 3),
          ("mjSentUnregister", 6))
    )



class BgpSjStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sjFailed", 7),
          ("sjFailingOver", 6),
          ("sjJoinActive", 3),
          ("sjJoinGone", 5),
          ("sjJoinUnreg", 4),
          ("sjJoined", 2),
          ("sjNotJoined", 1))
    )



class BgpPeerStates(Integer32, TextualConvention):
    status = "current"
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
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openconfirm", 5),
          ("opensent", 4))
    )



class BgpPeerEvents(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("connectRetryTimer", 7),
          ("holdTimer", 8),
          ("keepaliverTimer", 9),
          ("noEvent", 0),
          ("recvKeepAlive", 11),
          ("recvNotification", 13),
          ("recvOpen", 10),
          ("recvUpdate", 12),
          ("start", 1),
          ("stop", 2),
          ("transportClosed", 4),
          ("transportFatalError", 6),
          ("transportOpen", 3),
          ("transportOpenFailed", 5))
    )



class BgpCapabilities(Bits, TextualConvention):
    status = "current"


class BgpPeerRestartSupport(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("awareOnly", 2),
          ("enabled", 3),
          ("none", 1))
    )



class BgpPeerRestartStatus(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notRestarting", 1),
          ("restartTimerRunning", 2),
          ("stalePathTimerRunning", 3))
    )



class BgpPeerLastFailure(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notifyRecv", 3),
          ("notifySent", 2),
          ("other", 1))
    )



class BgpCeaseErrorSubcode(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("adminReset", 4),
          ("adminShutdown", 2),
          ("configChange", 6),
          ("noResource", 8),
          ("none", 0),
          ("peerUnconfig", 3))
    )



class BgpPeerReflectorClientType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("meshedClient", 2),
          ("nonClient", 0))
    )



class BgpComponentId(Integer32, TextualConvention):
    status = "current"
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
        *(("componentBfd", 6),
          ("componentIpSockets", 3),
          ("componentNm", 2),
          ("componentRm", 1),
          ("componentRtm", 4),
          ("componentVmIpv4", 5))
    )



class BgpCommunity(OctetString, TextualConvention):
    status = "current"
    displayHint = "4x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )



class BgpExtendedCommunity(OctetString, TextualConvention):
    status = "current"
    displayHint = "8x"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )



class BgpCommunityAction(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("removeAll", 1),
          ("removeAllAndSet", 4),
          ("removeSpecific", 2),
          ("setSpecific", 3))
    )



class BgpPathAttrAtomicAggPresence(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("atomicAggregateMissing", 2),
          ("atomicAggregatePresent", 1))
    )



class BgpOrfType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              64)
        )
    )
    namedValues = NamedValues(
        *(("community", 1),
          ("extCommunity", 2),
          ("prefix", 64))
    )



class BgpOrfSendReceive(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("both", 3),
          ("receive", 1),
          ("send", 2))
    )



class BgpOrfAssociation(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("noAssociation", 0),
          ("remote", 2))
    )



class BgpPeeringType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("biLateral", 3),
          ("customer", 2),
          ("provider", 1),
          ("unspecified", 0))
    )



class BgpAfiSafiBits(Bits, TextualConvention):
    status = "current"


class BgpNlriIsActiveFlag(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("notTracked", 1))
    )



# MIB Managed Objects in the order of their OIDs

_BgpNotifications_ObjectIdentity = ObjectIdentity
bgpNotifications = _BgpNotifications_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 1)
)
_BgpBaseNotifications_ObjectIdentity = ObjectIdentity
bgpBaseNotifications = _BgpBaseNotifications_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 1, 0)
)
_BgpRm_ObjectIdentity = ObjectIdentity
bgpRm = _BgpRm_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2)
)
_BgpRmEntTable_Object = MibTable
bgpRmEntTable = _BgpRmEntTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1)
)
if mibBuilder.loadTexts:
    bgpRmEntTable.setStatus("current")
_BgpRmEntEntry_Object = MibTableRow
bgpRmEntEntry = _BgpRmEntEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1)
)
bgpRmEntEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
)
if mibBuilder.loadTexts:
    bgpRmEntEntry.setStatus("current")
_BgpRmEntIndex_Type = Unsigned32
_BgpRmEntIndex_Object = MibTableColumn
bgpRmEntIndex = _BgpRmEntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 1),
    _BgpRmEntIndex_Type()
)
bgpRmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRmEntIndex.setStatus("current")
_BgpRmEntRowStatus_Type = RowStatus
_BgpRmEntRowStatus_Object = MibTableColumn
bgpRmEntRowStatus = _BgpRmEntRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 2),
    _BgpRmEntRowStatus_Type()
)
bgpRmEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntRowStatus.setStatus("current")


class _BgpRmEntAdminStatus_Type(BgpAdminStatus):
    """Custom type bgpRmEntAdminStatus based on BgpAdminStatus"""


_BgpRmEntAdminStatus_Object = MibTableColumn
bgpRmEntAdminStatus = _BgpRmEntAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 3),
    _BgpRmEntAdminStatus_Type()
)
bgpRmEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntAdminStatus.setStatus("current")
_BgpRmEntOperStatus_Type = BgpOperStatus
_BgpRmEntOperStatus_Object = MibTableColumn
bgpRmEntOperStatus = _BgpRmEntOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 4),
    _BgpRmEntOperStatus_Type()
)
bgpRmEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntOperStatus.setStatus("current")


class _BgpRmEntAsSize_Type(BgpAsSize):
    """Custom type bgpRmEntAsSize based on BgpAsSize"""


_BgpRmEntAsSize_Object = MibTableColumn
bgpRmEntAsSize = _BgpRmEntAsSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 5),
    _BgpRmEntAsSize_Type()
)
bgpRmEntAsSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntAsSize.setStatus("current")
_BgpRmEntLocalAs_Type = BgpAutonomousSystemNumber
_BgpRmEntLocalAs_Object = MibTableColumn
bgpRmEntLocalAs = _BgpRmEntLocalAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 6),
    _BgpRmEntLocalAs_Type()
)
bgpRmEntLocalAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntLocalAs.setStatus("current")


class _BgpRmEntLocalMbrAs_Type(BgpAutonomousSystemNumber):
    """Custom type bgpRmEntLocalMbrAs based on BgpAutonomousSystemNumber"""
    defaultValue = 0


_BgpRmEntLocalMbrAs_Object = MibTableColumn
bgpRmEntLocalMbrAs = _BgpRmEntLocalMbrAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 7),
    _BgpRmEntLocalMbrAs_Type()
)
bgpRmEntLocalMbrAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntLocalMbrAs.setStatus("current")
_BgpRmEntLocalIdentifier_Type = BgpIdentifier
_BgpRmEntLocalIdentifier_Object = MibTableColumn
bgpRmEntLocalIdentifier = _BgpRmEntLocalIdentifier_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 8),
    _BgpRmEntLocalIdentifier_Type()
)
bgpRmEntLocalIdentifier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntLocalIdentifier.setStatus("current")


class _BgpRmEntClusterId_Type(BgpIdentifier):
    """Custom type bgpRmEntClusterId based on BgpIdentifier"""
    defaultHexValue = "00000000"


_BgpRmEntClusterId_Object = MibTableColumn
bgpRmEntClusterId = _BgpRmEntClusterId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 9),
    _BgpRmEntClusterId_Type()
)
bgpRmEntClusterId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntClusterId.setStatus("current")


class _BgpRmEntIpv4MultiSupport_Type(TruthValue):
    """Custom type bgpRmEntIpv4MultiSupport based on TruthValue"""


_BgpRmEntIpv4MultiSupport_Object = MibTableColumn
bgpRmEntIpv4MultiSupport = _BgpRmEntIpv4MultiSupport_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 10),
    _BgpRmEntIpv4MultiSupport_Type()
)
bgpRmEntIpv4MultiSupport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntIpv4MultiSupport.setStatus("obsolete")


class _BgpRmEntVpnIpv4Support_Type(TruthValue):
    """Custom type bgpRmEntVpnIpv4Support based on TruthValue"""


_BgpRmEntVpnIpv4Support_Object = MibTableColumn
bgpRmEntVpnIpv4Support = _BgpRmEntVpnIpv4Support_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 11),
    _BgpRmEntVpnIpv4Support_Type()
)
bgpRmEntVpnIpv4Support.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntVpnIpv4Support.setStatus("obsolete")


class _BgpRmEntFlapDeltat_Type(Unsigned32):
    """Custom type bgpRmEntFlapDeltat based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BgpRmEntFlapDeltat_Type.__name__ = "Unsigned32"
_BgpRmEntFlapDeltat_Object = MibTableColumn
bgpRmEntFlapDeltat = _BgpRmEntFlapDeltat_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 12),
    _BgpRmEntFlapDeltat_Type()
)
bgpRmEntFlapDeltat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntFlapDeltat.setStatus("current")
if mibBuilder.loadTexts:
    bgpRmEntFlapDeltat.setUnits("seconds")


class _BgpRmEntFlapReusemax_Type(Unsigned32):
    """Custom type bgpRmEntFlapReusemax based on Unsigned32"""
    defaultValue = 3600

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpRmEntFlapReusemax_Type.__name__ = "Unsigned32"
_BgpRmEntFlapReusemax_Object = MibTableColumn
bgpRmEntFlapReusemax = _BgpRmEntFlapReusemax_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 13),
    _BgpRmEntFlapReusemax_Type()
)
bgpRmEntFlapReusemax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntFlapReusemax.setStatus("current")
if mibBuilder.loadTexts:
    bgpRmEntFlapReusemax.setUnits("seconds")


class _BgpRmEntFlapReusesize_Type(Unsigned32):
    """Custom type bgpRmEntFlapReusesize based on Unsigned32"""
    defaultValue = 256

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpRmEntFlapReusesize_Type.__name__ = "Unsigned32"
_BgpRmEntFlapReusesize_Object = MibTableColumn
bgpRmEntFlapReusesize = _BgpRmEntFlapReusesize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 14),
    _BgpRmEntFlapReusesize_Type()
)
bgpRmEntFlapReusesize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntFlapReusesize.setStatus("current")


class _BgpRmEntFlapReusearray_Type(Unsigned32):
    """Custom type bgpRmEntFlapReusearray based on Unsigned32"""
    defaultValue = 1024


_BgpRmEntFlapReusearray_Object = MibTableColumn
bgpRmEntFlapReusearray = _BgpRmEntFlapReusearray_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 15),
    _BgpRmEntFlapReusearray_Type()
)
bgpRmEntFlapReusearray.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntFlapReusearray.setStatus("current")


class _BgpRmEntFlapFreemax_Type(Unsigned32):
    """Custom type bgpRmEntFlapFreemax based on Unsigned32"""
    defaultValue = 3600


_BgpRmEntFlapFreemax_Object = MibTableColumn
bgpRmEntFlapFreemax = _BgpRmEntFlapFreemax_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 16),
    _BgpRmEntFlapFreemax_Type()
)
bgpRmEntFlapFreemax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntFlapFreemax.setStatus("current")
if mibBuilder.loadTexts:
    bgpRmEntFlapFreemax.setUnits("seconds")


class _BgpRmEntNoRefresh_Type(TruthValue):
    """Custom type bgpRmEntNoRefresh based on TruthValue"""


_BgpRmEntNoRefresh_Object = MibTableColumn
bgpRmEntNoRefresh = _BgpRmEntNoRefresh_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 17),
    _BgpRmEntNoRefresh_Type()
)
bgpRmEntNoRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntNoRefresh.setStatus("current")


class _BgpRmEntDefLocalPref_Type(Unsigned32):
    """Custom type bgpRmEntDefLocalPref based on Unsigned32"""
    defaultValue = 100


_BgpRmEntDefLocalPref_Object = MibTableColumn
bgpRmEntDefLocalPref = _BgpRmEntDefLocalPref_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 18),
    _BgpRmEntDefLocalPref_Type()
)
bgpRmEntDefLocalPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntDefLocalPref.setStatus("current")


class _BgpRmEntAlwaysCompMed_Type(TruthValue):
    """Custom type bgpRmEntAlwaysCompMed based on TruthValue"""


_BgpRmEntAlwaysCompMed_Object = MibTableColumn
bgpRmEntAlwaysCompMed = _BgpRmEntAlwaysCompMed_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 19),
    _BgpRmEntAlwaysCompMed_Type()
)
bgpRmEntAlwaysCompMed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntAlwaysCompMed.setStatus("current")


class _BgpRmEntAggregateMed_Type(TruthValue):
    """Custom type bgpRmEntAggregateMed based on TruthValue"""


_BgpRmEntAggregateMed_Object = MibTableColumn
bgpRmEntAggregateMed = _BgpRmEntAggregateMed_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 20),
    _BgpRmEntAggregateMed_Type()
)
bgpRmEntAggregateMed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntAggregateMed.setStatus("current")


class _BgpRmEntDeterministicMed_Type(TruthValue):
    """Custom type bgpRmEntDeterministicMed based on TruthValue"""


_BgpRmEntDeterministicMed_Object = MibTableColumn
bgpRmEntDeterministicMed = _BgpRmEntDeterministicMed_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 21),
    _BgpRmEntDeterministicMed_Type()
)
bgpRmEntDeterministicMed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntDeterministicMed.setStatus("current")
_BgpRmEntNhrJoinStatus_Type = BgpMjStatus
_BgpRmEntNhrJoinStatus_Object = MibTableColumn
bgpRmEntNhrJoinStatus = _BgpRmEntNhrJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 22),
    _BgpRmEntNhrJoinStatus_Type()
)
bgpRmEntNhrJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntNhrJoinStatus.setStatus("obsolete")
_BgpRmEntNhrEntIndex_Type = Unsigned32
_BgpRmEntNhrEntIndex_Object = MibTableColumn
bgpRmEntNhrEntIndex = _BgpRmEntNhrEntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 23),
    _BgpRmEntNhrEntIndex_Type()
)
bgpRmEntNhrEntIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntNhrEntIndex.setStatus("obsolete")
_BgpRmEntI3JoinStatus_Type = BgpMjStatus
_BgpRmEntI3JoinStatus_Object = MibTableColumn
bgpRmEntI3JoinStatus = _BgpRmEntI3JoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 24),
    _BgpRmEntI3JoinStatus_Type()
)
bgpRmEntI3JoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntI3JoinStatus.setStatus("current")
_BgpRmEntI3EntIndex_Type = Unsigned32
_BgpRmEntI3EntIndex_Object = MibTableColumn
bgpRmEntI3EntIndex = _BgpRmEntI3EntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 25),
    _BgpRmEntI3EntIndex_Type()
)
bgpRmEntI3EntIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntI3EntIndex.setStatus("current")


class _BgpRmEntPauseThreshold_Type(Unsigned32):
    """Custom type bgpRmEntPauseThreshold based on Unsigned32"""
    defaultValue = 2000


_BgpRmEntPauseThreshold_Object = MibTableColumn
bgpRmEntPauseThreshold = _BgpRmEntPauseThreshold_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 26),
    _BgpRmEntPauseThreshold_Type()
)
bgpRmEntPauseThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntPauseThreshold.setStatus("current")


class _BgpRmEntMaxIBgpEcmpRoutes_Type(Unsigned32):
    """Custom type bgpRmEntMaxIBgpEcmpRoutes based on Unsigned32"""
    defaultValue = 4


_BgpRmEntMaxIBgpEcmpRoutes_Object = MibTableColumn
bgpRmEntMaxIBgpEcmpRoutes = _BgpRmEntMaxIBgpEcmpRoutes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 27),
    _BgpRmEntMaxIBgpEcmpRoutes_Type()
)
bgpRmEntMaxIBgpEcmpRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntMaxIBgpEcmpRoutes.setStatus("current")


class _BgpRmEntMaxEBgpEcmpRoutes_Type(Unsigned32):
    """Custom type bgpRmEntMaxEBgpEcmpRoutes based on Unsigned32"""
    defaultValue = 4


_BgpRmEntMaxEBgpEcmpRoutes_Object = MibTableColumn
bgpRmEntMaxEBgpEcmpRoutes = _BgpRmEntMaxEBgpEcmpRoutes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 28),
    _BgpRmEntMaxEBgpEcmpRoutes_Type()
)
bgpRmEntMaxEBgpEcmpRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntMaxEBgpEcmpRoutes.setStatus("current")


class _BgpRmEntRestartSupported_Type(TruthValue):
    """Custom type bgpRmEntRestartSupported based on TruthValue"""


_BgpRmEntRestartSupported_Object = MibTableColumn
bgpRmEntRestartSupported = _BgpRmEntRestartSupported_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 29),
    _BgpRmEntRestartSupported_Type()
)
bgpRmEntRestartSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntRestartSupported.setStatus("current")


class _BgpRmEntMaxRestartTime_Type(Unsigned32):
    """Custom type bgpRmEntMaxRestartTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_BgpRmEntMaxRestartTime_Type.__name__ = "Unsigned32"
_BgpRmEntMaxRestartTime_Object = MibTableColumn
bgpRmEntMaxRestartTime = _BgpRmEntMaxRestartTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 30),
    _BgpRmEntMaxRestartTime_Type()
)
bgpRmEntMaxRestartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntMaxRestartTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpRmEntMaxRestartTime.setUnits("seconds")


class _BgpRmEntRecoveryTime_Type(Unsigned32):
    """Custom type bgpRmEntRecoveryTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_BgpRmEntRecoveryTime_Type.__name__ = "Unsigned32"
_BgpRmEntRecoveryTime_Object = MibTableColumn
bgpRmEntRecoveryTime = _BgpRmEntRecoveryTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 31),
    _BgpRmEntRecoveryTime_Type()
)
bgpRmEntRecoveryTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntRecoveryTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpRmEntRecoveryTime.setUnits("seconds")


class _BgpRmEntRestarting_Type(TruthValue):
    """Custom type bgpRmEntRestarting based on TruthValue"""


_BgpRmEntRestarting_Object = MibTableColumn
bgpRmEntRestarting = _BgpRmEntRestarting_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 32),
    _BgpRmEntRestarting_Type()
)
bgpRmEntRestarting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntRestarting.setStatus("current")


class _BgpRmEntIpv4UniFwdPrsrvd_Type(TruthValue):
    """Custom type bgpRmEntIpv4UniFwdPrsrvd based on TruthValue"""


_BgpRmEntIpv4UniFwdPrsrvd_Object = MibTableColumn
bgpRmEntIpv4UniFwdPrsrvd = _BgpRmEntIpv4UniFwdPrsrvd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 33),
    _BgpRmEntIpv4UniFwdPrsrvd_Type()
)
bgpRmEntIpv4UniFwdPrsrvd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntIpv4UniFwdPrsrvd.setStatus("obsolete")


class _BgpRmEntIpv4MultiFwdPrsrvd_Type(TruthValue):
    """Custom type bgpRmEntIpv4MultiFwdPrsrvd based on TruthValue"""


_BgpRmEntIpv4MultiFwdPrsrvd_Object = MibTableColumn
bgpRmEntIpv4MultiFwdPrsrvd = _BgpRmEntIpv4MultiFwdPrsrvd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 34),
    _BgpRmEntIpv4MultiFwdPrsrvd_Type()
)
bgpRmEntIpv4MultiFwdPrsrvd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntIpv4MultiFwdPrsrvd.setStatus("obsolete")


class _BgpRmEntVpnIpv4FwdPrsrvd_Type(TruthValue):
    """Custom type bgpRmEntVpnIpv4FwdPrsrvd based on TruthValue"""


_BgpRmEntVpnIpv4FwdPrsrvd_Object = MibTableColumn
bgpRmEntVpnIpv4FwdPrsrvd = _BgpRmEntVpnIpv4FwdPrsrvd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 35),
    _BgpRmEntVpnIpv4FwdPrsrvd_Type()
)
bgpRmEntVpnIpv4FwdPrsrvd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntVpnIpv4FwdPrsrvd.setStatus("obsolete")
_BgpRmEntIpv4ArinhJoinStatus_Type = BgpSjStatus
_BgpRmEntIpv4ArinhJoinStatus_Object = MibTableColumn
bgpRmEntIpv4ArinhJoinStatus = _BgpRmEntIpv4ArinhJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 36),
    _BgpRmEntIpv4ArinhJoinStatus_Type()
)
bgpRmEntIpv4ArinhJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntIpv4ArinhJoinStatus.setStatus("current")
_BgpRmEntIpv4ArinhEntIndex_Type = Unsigned32
_BgpRmEntIpv4ArinhEntIndex_Object = MibTableColumn
bgpRmEntIpv4ArinhEntIndex = _BgpRmEntIpv4ArinhEntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 37),
    _BgpRmEntIpv4ArinhEntIndex_Type()
)
bgpRmEntIpv4ArinhEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntIpv4ArinhEntIndex.setStatus("current")
_BgpRmEntIpv6ArinhJoinStatus_Type = BgpSjStatus
_BgpRmEntIpv6ArinhJoinStatus_Object = MibTableColumn
bgpRmEntIpv6ArinhJoinStatus = _BgpRmEntIpv6ArinhJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 38),
    _BgpRmEntIpv6ArinhJoinStatus_Type()
)
bgpRmEntIpv6ArinhJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntIpv6ArinhJoinStatus.setStatus("current")
_BgpRmEntIpv6ArinhEntIndex_Type = Unsigned32
_BgpRmEntIpv6ArinhEntIndex_Object = MibTableColumn
bgpRmEntIpv6ArinhEntIndex = _BgpRmEntIpv6ArinhEntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 39),
    _BgpRmEntIpv6ArinhEntIndex_Type()
)
bgpRmEntIpv6ArinhEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntIpv6ArinhEntIndex.setStatus("current")


class _BgpRmEntSupportIpv6_Type(TruthValue):
    """Custom type bgpRmEntSupportIpv6 based on TruthValue"""


_BgpRmEntSupportIpv6_Object = MibTableColumn
bgpRmEntSupportIpv6 = _BgpRmEntSupportIpv6_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 40),
    _BgpRmEntSupportIpv6_Type()
)
bgpRmEntSupportIpv6.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntSupportIpv6.setStatus("current")


class _BgpRmEntStrictConfed_Type(TruthValue):
    """Custom type bgpRmEntStrictConfed based on TruthValue"""


_BgpRmEntStrictConfed_Object = MibTableColumn
bgpRmEntStrictConfed = _BgpRmEntStrictConfed_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 41),
    _BgpRmEntStrictConfed_Type()
)
bgpRmEntStrictConfed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntStrictConfed.setStatus("current")


class _BgpRmEntOrfSupported_Type(TruthValue):
    """Custom type bgpRmEntOrfSupported based on TruthValue"""


_BgpRmEntOrfSupported_Object = MibTableColumn
bgpRmEntOrfSupported = _BgpRmEntOrfSupported_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 42),
    _BgpRmEntOrfSupported_Type()
)
bgpRmEntOrfSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntOrfSupported.setStatus("current")


class _BgpRmEntCiscoPrefixSupported_Type(TruthValue):
    """Custom type bgpRmEntCiscoPrefixSupported based on TruthValue"""


_BgpRmEntCiscoPrefixSupported_Object = MibTableColumn
bgpRmEntCiscoPrefixSupported = _BgpRmEntCiscoPrefixSupported_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 43),
    _BgpRmEntCiscoPrefixSupported_Type()
)
bgpRmEntCiscoPrefixSupported.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntCiscoPrefixSupported.setStatus("current")


class _BgpRmEntSelectDeferTime_Type(Unsigned32):
    """Custom type bgpRmEntSelectDeferTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_BgpRmEntSelectDeferTime_Type.__name__ = "Unsigned32"
_BgpRmEntSelectDeferTime_Object = MibTableColumn
bgpRmEntSelectDeferTime = _BgpRmEntSelectDeferTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 44),
    _BgpRmEntSelectDeferTime_Type()
)
bgpRmEntSelectDeferTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntSelectDeferTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpRmEntSelectDeferTime.setUnits("seconds")


class _BgpRmEntStalePathTime_Type(Unsigned32):
    """Custom type bgpRmEntStalePathTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )


_BgpRmEntStalePathTime_Type.__name__ = "Unsigned32"
_BgpRmEntStalePathTime_Object = MibTableColumn
bgpRmEntStalePathTime = _BgpRmEntStalePathTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 45),
    _BgpRmEntStalePathTime_Type()
)
bgpRmEntStalePathTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntStalePathTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpRmEntStalePathTime.setUnits("seconds")


class _BgpRmEntNonPersistentAros_Type(TruthValue):
    """Custom type bgpRmEntNonPersistentAros based on TruthValue"""


_BgpRmEntNonPersistentAros_Object = MibTableColumn
bgpRmEntNonPersistentAros = _BgpRmEntNonPersistentAros_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 46),
    _BgpRmEntNonPersistentAros_Type()
)
bgpRmEntNonPersistentAros.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntNonPersistentAros.setStatus("current")


class _BgpRmEntAroRouteThreshold_Type(Unsigned32):
    """Custom type bgpRmEntAroRouteThreshold based on Unsigned32"""
    defaultValue = 1000000


_BgpRmEntAroRouteThreshold_Object = MibTableColumn
bgpRmEntAroRouteThreshold = _BgpRmEntAroRouteThreshold_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 47),
    _BgpRmEntAroRouteThreshold_Type()
)
bgpRmEntAroRouteThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntAroRouteThreshold.setStatus("current")


class _BgpRmEntMaxActiveAroGroups_Type(Unsigned32):
    """Custom type bgpRmEntMaxActiveAroGroups based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BgpRmEntMaxActiveAroGroups_Type.__name__ = "Unsigned32"
_BgpRmEntMaxActiveAroGroups_Object = MibTableColumn
bgpRmEntMaxActiveAroGroups = _BgpRmEntMaxActiveAroGroups_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 48),
    _BgpRmEntMaxActiveAroGroups_Type()
)
bgpRmEntMaxActiveAroGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntMaxActiveAroGroups.setStatus("current")


class _BgpRmEntNumArosInGroup_Type(Unsigned32):
    """Custom type bgpRmEntNumArosInGroup based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_BgpRmEntNumArosInGroup_Type.__name__ = "Unsigned32"
_BgpRmEntNumArosInGroup_Object = MibTableColumn
bgpRmEntNumArosInGroup = _BgpRmEntNumArosInGroup_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 49),
    _BgpRmEntNumArosInGroup_Type()
)
bgpRmEntNumArosInGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntNumArosInGroup.setStatus("current")
_BgpRmEntNumAroRoutes_Type = Counter32
_BgpRmEntNumAroRoutes_Object = MibTableColumn
bgpRmEntNumAroRoutes = _BgpRmEntNumAroRoutes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 50),
    _BgpRmEntNumAroRoutes_Type()
)
bgpRmEntNumAroRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntNumAroRoutes.setStatus("current")
_BgpRmEntPeakNumAroRoutes_Type = Counter32
_BgpRmEntPeakNumAroRoutes_Object = MibTableColumn
bgpRmEntPeakNumAroRoutes = _BgpRmEntPeakNumAroRoutes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 51),
    _BgpRmEntPeakNumAroRoutes_Type()
)
bgpRmEntPeakNumAroRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntPeakNumAroRoutes.setStatus("current")


class _BgpRmEntClearStats_Type(TruthValue):
    """Custom type bgpRmEntClearStats based on TruthValue"""


_BgpRmEntClearStats_Object = MibTableColumn
bgpRmEntClearStats = _BgpRmEntClearStats_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 52),
    _BgpRmEntClearStats_Type()
)
bgpRmEntClearStats.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntClearStats.setStatus("current")


class _BgpRmEntFastExtFallover_Type(TruthValue):
    """Custom type bgpRmEntFastExtFallover based on TruthValue"""


_BgpRmEntFastExtFallover_Object = MibTableColumn
bgpRmEntFastExtFallover = _BgpRmEntFastExtFallover_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 53),
    _BgpRmEntFastExtFallover_Type()
)
bgpRmEntFastExtFallover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntFastExtFallover.setStatus("current")
_BgpRmEntRemainDelayTime_Type = TimeInterval
_BgpRmEntRemainDelayTime_Object = MibTableColumn
bgpRmEntRemainDelayTime = _BgpRmEntRemainDelayTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 54),
    _BgpRmEntRemainDelayTime_Type()
)
bgpRmEntRemainDelayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntRemainDelayTime.setStatus("current")
_BgpRmEntPathAttrs_Type = Gauge32
_BgpRmEntPathAttrs_Object = MibTableColumn
bgpRmEntPathAttrs = _BgpRmEntPathAttrs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 55),
    _BgpRmEntPathAttrs_Type()
)
bgpRmEntPathAttrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmEntPathAttrs.setStatus("current")


class _BgpRmEntAggSplitHorizon_Type(TruthValue):
    """Custom type bgpRmEntAggSplitHorizon based on TruthValue"""


_BgpRmEntAggSplitHorizon_Object = MibTableColumn
bgpRmEntAggSplitHorizon = _BgpRmEntAggSplitHorizon_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 56),
    _BgpRmEntAggSplitHorizon_Type()
)
bgpRmEntAggSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntAggSplitHorizon.setStatus("current")


class _BgpRmEntAggAdvSuppr_Type(TruthValue):
    """Custom type bgpRmEntAggAdvSuppr based on TruthValue"""


_BgpRmEntAggAdvSuppr_Object = MibTableColumn
bgpRmEntAggAdvSuppr = _BgpRmEntAggAdvSuppr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 57),
    _BgpRmEntAggAdvSuppr_Type()
)
bgpRmEntAggAdvSuppr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntAggAdvSuppr.setStatus("current")


class _BgpRmEntUpdateGroups_Type(TruthValue):
    """Custom type bgpRmEntUpdateGroups based on TruthValue"""


_BgpRmEntUpdateGroups_Object = MibTableColumn
bgpRmEntUpdateGroups = _BgpRmEntUpdateGroups_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 58),
    _BgpRmEntUpdateGroups_Type()
)
bgpRmEntUpdateGroups.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntUpdateGroups.setStatus("current")


class _BgpRmEntPhase3DelayTime_Type(Unsigned32):
    """Custom type bgpRmEntPhase3DelayTime based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_BgpRmEntPhase3DelayTime_Type.__name__ = "Unsigned32"
_BgpRmEntPhase3DelayTime_Object = MibTableColumn
bgpRmEntPhase3DelayTime = _BgpRmEntPhase3DelayTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 59),
    _BgpRmEntPhase3DelayTime_Type()
)
bgpRmEntPhase3DelayTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntPhase3DelayTime.setStatus("current")


class _BgpRmEntTrapOperState_Type(TruthValue):
    """Custom type bgpRmEntTrapOperState based on TruthValue"""


_BgpRmEntTrapOperState_Object = MibTableColumn
bgpRmEntTrapOperState = _BgpRmEntTrapOperState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 1, 1, 60),
    _BgpRmEntTrapOperState_Type()
)
bgpRmEntTrapOperState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmEntTrapOperState.setStatus("current")
_BgpRmAfiSafiTable_Object = MibTable
bgpRmAfiSafiTable = _BgpRmAfiSafiTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2)
)
if mibBuilder.loadTexts:
    bgpRmAfiSafiTable.setStatus("current")
_BgpRmAfiSafiEntry_Object = MibTableRow
bgpRmAfiSafiEntry = _BgpRmAfiSafiEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1)
)
bgpRmAfiSafiEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpRmAfiSafiAfi"),
    (0, "DC-BGP-MIB", "bgpRmAfiSafiSafi"),
)
if mibBuilder.loadTexts:
    bgpRmAfiSafiEntry.setStatus("current")
_BgpRmAfiSafiAfi_Type = BgpAfi
_BgpRmAfiSafiAfi_Object = MibTableColumn
bgpRmAfiSafiAfi = _BgpRmAfiSafiAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 2),
    _BgpRmAfiSafiAfi_Type()
)
bgpRmAfiSafiAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRmAfiSafiAfi.setStatus("current")
_BgpRmAfiSafiSafi_Type = BgpSafi
_BgpRmAfiSafiSafi_Object = MibTableColumn
bgpRmAfiSafiSafi = _BgpRmAfiSafiSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 3),
    _BgpRmAfiSafiSafi_Type()
)
bgpRmAfiSafiSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRmAfiSafiSafi.setStatus("current")


class _BgpRmAfiSafiAdminStatus_Type(BgpAdminStatus):
    """Custom type bgpRmAfiSafiAdminStatus based on BgpAdminStatus"""


_BgpRmAfiSafiAdminStatus_Object = MibTableColumn
bgpRmAfiSafiAdminStatus = _BgpRmAfiSafiAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 4),
    _BgpRmAfiSafiAdminStatus_Type()
)
bgpRmAfiSafiAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfiSafiAdminStatus.setStatus("current")


class _BgpRmAfiSafiStateKept_Type(TruthValue):
    """Custom type bgpRmAfiSafiStateKept based on TruthValue"""


_BgpRmAfiSafiStateKept_Object = MibTableColumn
bgpRmAfiSafiStateKept = _BgpRmAfiSafiStateKept_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 5),
    _BgpRmAfiSafiStateKept_Type()
)
bgpRmAfiSafiStateKept.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfiSafiStateKept.setStatus("current")


class _BgpRmAfiSafiAfmRequired_Type(TruthValue):
    """Custom type bgpRmAfiSafiAfmRequired based on TruthValue"""


_BgpRmAfiSafiAfmRequired_Object = MibTableColumn
bgpRmAfiSafiAfmRequired = _BgpRmAfiSafiAfmRequired_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 6),
    _BgpRmAfiSafiAfmRequired_Type()
)
bgpRmAfiSafiAfmRequired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfiSafiAfmRequired.setStatus("current")
_BgpRmAfiSafiLocRibBlocked_Type = TruthValue
_BgpRmAfiSafiLocRibBlocked_Object = MibTableColumn
bgpRmAfiSafiLocRibBlocked = _BgpRmAfiSafiLocRibBlocked_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 7),
    _BgpRmAfiSafiLocRibBlocked_Type()
)
bgpRmAfiSafiLocRibBlocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiLocRibBlocked.setStatus("current")


class _BgpRmAfiSafiAdvertiseInactive_Type(TruthValue):
    """Custom type bgpRmAfiSafiAdvertiseInactive based on TruthValue"""


_BgpRmAfiSafiAdvertiseInactive_Object = MibTableColumn
bgpRmAfiSafiAdvertiseInactive = _BgpRmAfiSafiAdvertiseInactive_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 8),
    _BgpRmAfiSafiAdvertiseInactive_Type()
)
bgpRmAfiSafiAdvertiseInactive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfiSafiAdvertiseInactive.setStatus("current")


class _BgpRmAfiSafiUserData_Type(OctetString):
    """Custom type bgpRmAfiSafiUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BgpRmAfiSafiUserData_Type.__name__ = "OctetString"
_BgpRmAfiSafiUserData_Object = MibTableColumn
bgpRmAfiSafiUserData = _BgpRmAfiSafiUserData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 9),
    _BgpRmAfiSafiUserData_Type()
)
bgpRmAfiSafiUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiUserData.setStatus("current")
_BgpRmAfiSafiIbgpPrefixes_Type = Gauge32
_BgpRmAfiSafiIbgpPrefixes_Object = MibTableColumn
bgpRmAfiSafiIbgpPrefixes = _BgpRmAfiSafiIbgpPrefixes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 10),
    _BgpRmAfiSafiIbgpPrefixes_Type()
)
bgpRmAfiSafiIbgpPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiIbgpPrefixes.setStatus("current")
_BgpRmAfiSafiEbgpPrefixes_Type = Gauge32
_BgpRmAfiSafiEbgpPrefixes_Object = MibTableColumn
bgpRmAfiSafiEbgpPrefixes = _BgpRmAfiSafiEbgpPrefixes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 11),
    _BgpRmAfiSafiEbgpPrefixes_Type()
)
bgpRmAfiSafiEbgpPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiEbgpPrefixes.setStatus("current")
_BgpRmAfiSafiRedistPrefixes_Type = Gauge32
_BgpRmAfiSafiRedistPrefixes_Object = MibTableColumn
bgpRmAfiSafiRedistPrefixes = _BgpRmAfiSafiRedistPrefixes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 12),
    _BgpRmAfiSafiRedistPrefixes_Type()
)
bgpRmAfiSafiRedistPrefixes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiRedistPrefixes.setStatus("current")
_BgpRmAfiSafiInPrfxes_Type = Gauge32
_BgpRmAfiSafiInPrfxes_Object = MibTableColumn
bgpRmAfiSafiInPrfxes = _BgpRmAfiSafiInPrfxes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 13),
    _BgpRmAfiSafiInPrfxes_Type()
)
bgpRmAfiSafiInPrfxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiInPrfxes.setStatus("current")
_BgpRmAfiSafiInPrfxesAccepted_Type = Gauge32
_BgpRmAfiSafiInPrfxesAccepted_Object = MibTableColumn
bgpRmAfiSafiInPrfxesAccepted = _BgpRmAfiSafiInPrfxesAccepted_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 14),
    _BgpRmAfiSafiInPrfxesAccepted_Type()
)
bgpRmAfiSafiInPrfxesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiInPrfxesAccepted.setStatus("current")
_BgpRmAfiSafiInPrfxesRejected_Type = Gauge32
_BgpRmAfiSafiInPrfxesRejected_Object = MibTableColumn
bgpRmAfiSafiInPrfxesRejected = _BgpRmAfiSafiInPrfxesRejected_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 15),
    _BgpRmAfiSafiInPrfxesRejected_Type()
)
bgpRmAfiSafiInPrfxesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiInPrfxesRejected.setStatus("current")
_BgpRmAfiSafiOutPrfxes_Type = Gauge32
_BgpRmAfiSafiOutPrfxes_Object = MibTableColumn
bgpRmAfiSafiOutPrfxes = _BgpRmAfiSafiOutPrfxes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 16),
    _BgpRmAfiSafiOutPrfxes_Type()
)
bgpRmAfiSafiOutPrfxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiOutPrfxes.setStatus("current")
_BgpRmAfiSafiOutPrfxesAdvertised_Type = Gauge32
_BgpRmAfiSafiOutPrfxesAdvertised_Object = MibTableColumn
bgpRmAfiSafiOutPrfxesAdvertised = _BgpRmAfiSafiOutPrfxesAdvertised_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 17),
    _BgpRmAfiSafiOutPrfxesAdvertised_Type()
)
bgpRmAfiSafiOutPrfxesAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiOutPrfxesAdvertised.setStatus("current")
_BgpRmAfiSafiInPrfxesActive_Type = Gauge32
_BgpRmAfiSafiInPrfxesActive_Object = MibTableColumn
bgpRmAfiSafiInPrfxesActive = _BgpRmAfiSafiInPrfxesActive_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 18),
    _BgpRmAfiSafiInPrfxesActive_Type()
)
bgpRmAfiSafiInPrfxesActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiInPrfxesActive.setStatus("current")
_BgpRmAfiSafiInPrfxesFlapped_Type = Gauge32
_BgpRmAfiSafiInPrfxesFlapped_Object = MibTableColumn
bgpRmAfiSafiInPrfxesFlapped = _BgpRmAfiSafiInPrfxesFlapped_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 19),
    _BgpRmAfiSafiInPrfxesFlapped_Type()
)
bgpRmAfiSafiInPrfxesFlapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiInPrfxesFlapped.setStatus("current")
_BgpRmAfiSafiInPrfxesFlapSuppr_Type = Gauge32
_BgpRmAfiSafiInPrfxesFlapSuppr_Object = MibTableColumn
bgpRmAfiSafiInPrfxesFlapSuppr = _BgpRmAfiSafiInPrfxesFlapSuppr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 20),
    _BgpRmAfiSafiInPrfxesFlapSuppr_Type()
)
bgpRmAfiSafiInPrfxesFlapSuppr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiInPrfxesFlapSuppr.setStatus("current")
_BgpRmAfiSafiInPrfxesFlapHistory_Type = Gauge32
_BgpRmAfiSafiInPrfxesFlapHistory_Object = MibTableColumn
bgpRmAfiSafiInPrfxesFlapHistory = _BgpRmAfiSafiInPrfxesFlapHistory_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 21),
    _BgpRmAfiSafiInPrfxesFlapHistory_Type()
)
bgpRmAfiSafiInPrfxesFlapHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiInPrfxesFlapHistory.setStatus("current")


class _BgpRmAfiSafiDefaultImportRule_Type(BgpPermitOrDeny):
    """Custom type bgpRmAfiSafiDefaultImportRule based on BgpPermitOrDeny"""


_BgpRmAfiSafiDefaultImportRule_Object = MibTableColumn
bgpRmAfiSafiDefaultImportRule = _BgpRmAfiSafiDefaultImportRule_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 22),
    _BgpRmAfiSafiDefaultImportRule_Type()
)
bgpRmAfiSafiDefaultImportRule.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfiSafiDefaultImportRule.setStatus("current")
_BgpRmAfiSafiInPrfxesDeniedByPol_Type = Gauge32
_BgpRmAfiSafiInPrfxesDeniedByPol_Object = MibTableColumn
bgpRmAfiSafiInPrfxesDeniedByPol = _BgpRmAfiSafiInPrfxesDeniedByPol_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 23),
    _BgpRmAfiSafiInPrfxesDeniedByPol_Type()
)
bgpRmAfiSafiInPrfxesDeniedByPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiInPrfxesDeniedByPol.setStatus("current")
_BgpRmAfiSafiNumLocRibRoutes_Type = Gauge32
_BgpRmAfiSafiNumLocRibRoutes_Object = MibTableColumn
bgpRmAfiSafiNumLocRibRoutes = _BgpRmAfiSafiNumLocRibRoutes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 24),
    _BgpRmAfiSafiNumLocRibRoutes_Type()
)
bgpRmAfiSafiNumLocRibRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfiSafiNumLocRibRoutes.setStatus("current")


class _BgpRmAfiSafiNextHopSafi_Type(BgpSafi):
    """Custom type bgpRmAfiSafiNextHopSafi based on BgpSafi"""


_BgpRmAfiSafiNextHopSafi_Object = MibTableColumn
bgpRmAfiSafiNextHopSafi = _BgpRmAfiSafiNextHopSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 2, 2, 1, 25),
    _BgpRmAfiSafiNextHopSafi_Type()
)
bgpRmAfiSafiNextHopSafi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfiSafiNextHopSafi.setStatus("current")
_BgpPeer_ObjectIdentity = ObjectIdentity
bgpPeer = _BgpPeer_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3)
)
_BgpPeerData_ObjectIdentity = ObjectIdentity
bgpPeerData = _BgpPeerData_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1)
)
_BgpPeerTable_Object = MibTable
bgpPeerTable = _BgpPeerTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    bgpPeerTable.setStatus("current")
_BgpPeerEntry_Object = MibTableRow
bgpPeerEntry = _BgpPeerEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1)
)
bgpPeerEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpPeerLocalAddrType"),
    (0, "DC-BGP-MIB", "bgpPeerLocalAddr"),
    (0, "DC-BGP-MIB", "bgpPeerLocalPort"),
    (0, "DC-BGP-MIB", "bgpPeerRemoteAddrType"),
    (0, "DC-BGP-MIB", "bgpPeerRemoteAddr"),
    (0, "DC-BGP-MIB", "bgpPeerRemotePort"),
    (0, "DC-BGP-MIB", "bgpPeerLocalAddrScopeId"),
)
if mibBuilder.loadTexts:
    bgpPeerEntry.setStatus("current")
_BgpPeerIdentifier_Type = BgpIdentifier
_BgpPeerIdentifier_Object = MibTableColumn
bgpPeerIdentifier = _BgpPeerIdentifier_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 2),
    _BgpPeerIdentifier_Type()
)
bgpPeerIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerIdentifier.setStatus("current")
_BgpPeerState_Type = BgpPeerStates
_BgpPeerState_Object = MibTableColumn
bgpPeerState = _BgpPeerState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 3),
    _BgpPeerState_Type()
)
bgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerState.setStatus("current")
_BgpPeerRowStatus_Type = RowStatus
_BgpPeerRowStatus_Object = MibTableColumn
bgpPeerRowStatus = _BgpPeerRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 4),
    _BgpPeerRowStatus_Type()
)
bgpPeerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerRowStatus.setStatus("current")


class _BgpPeerAdminStatus_Type(BgpAdminStatus):
    """Custom type bgpPeerAdminStatus based on BgpAdminStatus"""


_BgpPeerAdminStatus_Object = MibTableColumn
bgpPeerAdminStatus = _BgpPeerAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 5),
    _BgpPeerAdminStatus_Type()
)
bgpPeerAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAdminStatus.setStatus("current")
_BgpPeerOperStatus_Type = BgpOperStatus
_BgpPeerOperStatus_Object = MibTableColumn
bgpPeerOperStatus = _BgpPeerOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 6),
    _BgpPeerOperStatus_Type()
)
bgpPeerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerOperStatus.setStatus("current")
_BgpPeerLocalAddrType_Type = InetAddressType
_BgpPeerLocalAddrType_Object = MibTableColumn
bgpPeerLocalAddrType = _BgpPeerLocalAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 7),
    _BgpPeerLocalAddrType_Type()
)
bgpPeerLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLocalAddrType.setStatus("current")


class _BgpPeerLocalAddr_Type(InetAddress):
    """Custom type bgpPeerLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpPeerLocalAddr_Type.__name__ = "InetAddress"
_BgpPeerLocalAddr_Object = MibTableColumn
bgpPeerLocalAddr = _BgpPeerLocalAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 8),
    _BgpPeerLocalAddr_Type()
)
bgpPeerLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLocalAddr.setStatus("current")
_BgpPeerLocalPort_Type = InetPortNumber
_BgpPeerLocalPort_Object = MibTableColumn
bgpPeerLocalPort = _BgpPeerLocalPort_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 9),
    _BgpPeerLocalPort_Type()
)
bgpPeerLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerLocalPort.setStatus("current")
_BgpPeerLocalNm_Type = Integer32
_BgpPeerLocalNm_Object = MibTableColumn
bgpPeerLocalNm = _BgpPeerLocalNm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 10),
    _BgpPeerLocalNm_Type()
)
bgpPeerLocalNm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerLocalNm.setStatus("current")
_BgpPeerRemoteAddrType_Type = InetAddressType
_BgpPeerRemoteAddrType_Object = MibTableColumn
bgpPeerRemoteAddrType = _BgpPeerRemoteAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 11),
    _BgpPeerRemoteAddrType_Type()
)
bgpPeerRemoteAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRemoteAddrType.setStatus("current")


class _BgpPeerRemoteAddr_Type(InetAddress):
    """Custom type bgpPeerRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpPeerRemoteAddr_Type.__name__ = "InetAddress"
_BgpPeerRemoteAddr_Object = MibTableColumn
bgpPeerRemoteAddr = _BgpPeerRemoteAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 12),
    _BgpPeerRemoteAddr_Type()
)
bgpPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRemoteAddr.setStatus("current")
_BgpPeerRemotePort_Type = InetPortNumber
_BgpPeerRemotePort_Object = MibTableColumn
bgpPeerRemotePort = _BgpPeerRemotePort_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 13),
    _BgpPeerRemotePort_Type()
)
bgpPeerRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRemotePort.setStatus("current")
_BgpPeerRemoteAs_Type = BgpAutonomousSystemNumber
_BgpPeerRemoteAs_Object = MibTableColumn
bgpPeerRemoteAs = _BgpPeerRemoteAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 14),
    _BgpPeerRemoteAs_Type()
)
bgpPeerRemoteAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerRemoteAs.setStatus("current")
_BgpPeerIndex_Type = Unsigned32
_BgpPeerIndex_Object = MibTableColumn
bgpPeerIndex = _BgpPeerIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 15),
    _BgpPeerIndex_Type()
)
bgpPeerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerIndex.setStatus("current")


class _BgpPeerConfedMember_Type(TruthValue):
    """Custom type bgpPeerConfedMember based on TruthValue"""


_BgpPeerConfedMember_Object = MibTableColumn
bgpPeerConfedMember = _BgpPeerConfedMember_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 16),
    _BgpPeerConfedMember_Type()
)
bgpPeerConfedMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfedMember.setStatus("current")


class _BgpPeerReflectorClient_Type(BgpPeerReflectorClientType):
    """Custom type bgpPeerReflectorClient based on BgpPeerReflectorClientType"""


_BgpPeerReflectorClient_Object = MibTableColumn
bgpPeerReflectorClient = _BgpPeerReflectorClient_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 17),
    _BgpPeerReflectorClient_Type()
)
bgpPeerReflectorClient.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerReflectorClient.setStatus("current")


class _BgpPeerTrapEstab_Type(TruthValue):
    """Custom type bgpPeerTrapEstab based on TruthValue"""


_BgpPeerTrapEstab_Object = MibTableColumn
bgpPeerTrapEstab = _BgpPeerTrapEstab_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 18),
    _BgpPeerTrapEstab_Type()
)
bgpPeerTrapEstab.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerTrapEstab.setStatus("current")


class _BgpPeerTrapBackw_Type(TruthValue):
    """Custom type bgpPeerTrapBackw based on TruthValue"""


_BgpPeerTrapBackw_Object = MibTableColumn
bgpPeerTrapBackw = _BgpPeerTrapBackw_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 19),
    _BgpPeerTrapBackw_Type()
)
bgpPeerTrapBackw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerTrapBackw.setStatus("current")
_BgpPeerCapsSupport_Type = TruthValue
_BgpPeerCapsSupport_Object = MibTableColumn
bgpPeerCapsSupport = _BgpPeerCapsSupport_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 20),
    _BgpPeerCapsSupport_Type()
)
bgpPeerCapsSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerCapsSupport.setStatus("current")


class _BgpPeerLastError_Type(OctetString):
    """Custom type bgpPeerLastError based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BgpPeerLastError_Type.__name__ = "OctetString"
_BgpPeerLastError_Object = MibTableColumn
bgpPeerLastError = _BgpPeerLastError_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 21),
    _BgpPeerLastError_Type()
)
bgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastError.setStatus("current")


class _BgpPeerLastErrorDataLen_Type(Unsigned32):
    """Custom type bgpPeerLastErrorDataLen based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_BgpPeerLastErrorDataLen_Type.__name__ = "Unsigned32"
_BgpPeerLastErrorDataLen_Object = MibTableColumn
bgpPeerLastErrorDataLen = _BgpPeerLastErrorDataLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 22),
    _BgpPeerLastErrorDataLen_Type()
)
bgpPeerLastErrorDataLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastErrorDataLen.setStatus("current")


class _BgpPeerLastErrorData_Type(OctetString):
    """Custom type bgpPeerLastErrorData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(128, 128),
    )


_BgpPeerLastErrorData_Type.__name__ = "OctetString"
_BgpPeerLastErrorData_Object = MibTableColumn
bgpPeerLastErrorData = _BgpPeerLastErrorData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 23),
    _BgpPeerLastErrorData_Type()
)
bgpPeerLastErrorData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastErrorData.setStatus("current")
_BgpPeerFsmEstablishedTime_Type = Gauge32
_BgpPeerFsmEstablishedTime_Object = MibTableColumn
bgpPeerFsmEstablishedTime = _BgpPeerFsmEstablishedTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 24),
    _BgpPeerFsmEstablishedTime_Type()
)
bgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerFsmEstablishedTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerFsmEstablishedTime.setUnits("seconds")
_BgpPeerInUpdatesElapsedTime_Type = Gauge32
_BgpPeerInUpdatesElapsedTime_Object = MibTableColumn
bgpPeerInUpdatesElapsedTime = _BgpPeerInUpdatesElapsedTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 25),
    _BgpPeerInUpdatesElapsedTime_Type()
)
bgpPeerInUpdatesElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerInUpdatesElapsedTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerInUpdatesElapsedTime.setUnits("seconds")


class _BgpPeerConnectRetryInterval_Type(Unsigned32):
    """Custom type bgpPeerConnectRetryInterval based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpPeerConnectRetryInterval_Type.__name__ = "Unsigned32"
_BgpPeerConnectRetryInterval_Object = MibTableColumn
bgpPeerConnectRetryInterval = _BgpPeerConnectRetryInterval_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 26),
    _BgpPeerConnectRetryInterval_Type()
)
bgpPeerConnectRetryInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConnectRetryInterval.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerConnectRetryInterval.setUnits("seconds")


class _BgpPeerHoldTimeConfigd_Type(Unsigned32):
    """Custom type bgpPeerHoldTimeConfigd based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_BgpPeerHoldTimeConfigd_Type.__name__ = "Unsigned32"
_BgpPeerHoldTimeConfigd_Object = MibTableColumn
bgpPeerHoldTimeConfigd = _BgpPeerHoldTimeConfigd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 27),
    _BgpPeerHoldTimeConfigd_Type()
)
bgpPeerHoldTimeConfigd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerHoldTimeConfigd.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerHoldTimeConfigd.setUnits("seconds")


class _BgpPeerKeepAliveConfigd_Type(Unsigned32):
    """Custom type bgpPeerKeepAliveConfigd based on Unsigned32"""
    defaultValue = 30

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_BgpPeerKeepAliveConfigd_Type.__name__ = "Unsigned32"
_BgpPeerKeepAliveConfigd_Object = MibTableColumn
bgpPeerKeepAliveConfigd = _BgpPeerKeepAliveConfigd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 28),
    _BgpPeerKeepAliveConfigd_Type()
)
bgpPeerKeepAliveConfigd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerKeepAliveConfigd.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerKeepAliveConfigd.setUnits("seconds")


class _BgpPeerMinASOriginationInterval_Type(Unsigned32):
    """Custom type bgpPeerMinASOriginationInterval based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpPeerMinASOriginationInterval_Type.__name__ = "Unsigned32"
_BgpPeerMinASOriginationInterval_Object = MibTableColumn
bgpPeerMinASOriginationInterval = _BgpPeerMinASOriginationInterval_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 29),
    _BgpPeerMinASOriginationInterval_Type()
)
bgpPeerMinASOriginationInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerMinASOriginationInterval.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerMinASOriginationInterval.setUnits("seconds")


class _BgpPeerMinRouteAdvertiseInterval_Type(Unsigned32):
    """Custom type bgpPeerMinRouteAdvertiseInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BgpPeerMinRouteAdvertiseInterval_Type.__name__ = "Unsigned32"
_BgpPeerMinRouteAdvertiseInterval_Object = MibTableColumn
bgpPeerMinRouteAdvertiseInterval = _BgpPeerMinRouteAdvertiseInterval_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 30),
    _BgpPeerMinRouteAdvertiseInterval_Type()
)
bgpPeerMinRouteAdvertiseInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerMinRouteAdvertiseInterval.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerMinRouteAdvertiseInterval.setUnits("seconds")


class _BgpPeerHoldTime_Type(Integer32):
    """Custom type bgpPeerHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 65535),
    )


_BgpPeerHoldTime_Type.__name__ = "Integer32"
_BgpPeerHoldTime_Object = MibTableColumn
bgpPeerHoldTime = _BgpPeerHoldTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 31),
    _BgpPeerHoldTime_Type()
)
bgpPeerHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerHoldTime.setUnits("seconds")


class _BgpPeerKeepAlive_Type(Integer32):
    """Custom type bgpPeerKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 21845),
    )


_BgpPeerKeepAlive_Type.__name__ = "Integer32"
_BgpPeerKeepAlive_Object = MibTableColumn
bgpPeerKeepAlive = _BgpPeerKeepAlive_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 32),
    _BgpPeerKeepAlive_Type()
)
bgpPeerKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerKeepAlive.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerKeepAlive.setUnits("seconds")
_BgpPeerInUpdates_Type = Counter32
_BgpPeerInUpdates_Object = MibTableColumn
bgpPeerInUpdates = _BgpPeerInUpdates_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 33),
    _BgpPeerInUpdates_Type()
)
bgpPeerInUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerInUpdates.setStatus("current")
_BgpPeerOutUpdates_Type = Counter32
_BgpPeerOutUpdates_Object = MibTableColumn
bgpPeerOutUpdates = _BgpPeerOutUpdates_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 34),
    _BgpPeerOutUpdates_Type()
)
bgpPeerOutUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerOutUpdates.setStatus("current")
_BgpPeerInTotalMessages_Type = Counter32
_BgpPeerInTotalMessages_Object = MibTableColumn
bgpPeerInTotalMessages = _BgpPeerInTotalMessages_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 35),
    _BgpPeerInTotalMessages_Type()
)
bgpPeerInTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerInTotalMessages.setStatus("current")
_BgpPeerOutTotalMessages_Type = Counter32
_BgpPeerOutTotalMessages_Object = MibTableColumn
bgpPeerOutTotalMessages = _BgpPeerOutTotalMessages_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 36),
    _BgpPeerOutTotalMessages_Type()
)
bgpPeerOutTotalMessages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerOutTotalMessages.setStatus("current")
_BgpPeerFsmEstablishedTransitions_Type = Counter32
_BgpPeerFsmEstablishedTransitions_Object = MibTableColumn
bgpPeerFsmEstablishedTransitions = _BgpPeerFsmEstablishedTransitions_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 37),
    _BgpPeerFsmEstablishedTransitions_Type()
)
bgpPeerFsmEstablishedTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerFsmEstablishedTransitions.setStatus("current")
_BgpPeerConnectRetryCount_Type = Counter32
_BgpPeerConnectRetryCount_Object = MibTableColumn
bgpPeerConnectRetryCount = _BgpPeerConnectRetryCount_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 38),
    _BgpPeerConnectRetryCount_Type()
)
bgpPeerConnectRetryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerConnectRetryCount.setStatus("current")


class _BgpPeerClearCnts_Type(TruthValue):
    """Custom type bgpPeerClearCnts based on TruthValue"""


_BgpPeerClearCnts_Object = MibTableColumn
bgpPeerClearCnts = _BgpPeerClearCnts_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 39),
    _BgpPeerClearCnts_Type()
)
bgpPeerClearCnts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerClearCnts.setStatus("current")


class _BgpPeerConfigPeergr_Type(Unsigned32):
    """Custom type bgpPeerConfigPeergr based on Unsigned32"""
    defaultValue = 0


_BgpPeerConfigPeergr_Object = MibTableColumn
bgpPeerConfigPeergr = _BgpPeerConfigPeergr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 40),
    _BgpPeerConfigPeergr_Type()
)
bgpPeerConfigPeergr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfigPeergr.setStatus("current")


class _BgpPeerConfigIndex_Type(Unsigned32):
    """Custom type bgpPeerConfigIndex based on Unsigned32"""
    defaultValue = 0


_BgpPeerConfigIndex_Object = MibTableColumn
bgpPeerConfigIndex = _BgpPeerConfigIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 41),
    _BgpPeerConfigIndex_Type()
)
bgpPeerConfigIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfigIndex.setStatus("current")


class _BgpPeerConfigRtRefresh_Type(TruthValue):
    """Custom type bgpPeerConfigRtRefresh based on TruthValue"""


_BgpPeerConfigRtRefresh_Object = MibTableColumn
bgpPeerConfigRtRefresh = _BgpPeerConfigRtRefresh_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 42),
    _BgpPeerConfigRtRefresh_Type()
)
bgpPeerConfigRtRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfigRtRefresh.setStatus("current")


class _BgpPeerConfigMaxPrfx_Type(Integer32):
    """Custom type bgpPeerConfigMaxPrfx based on Integer32"""
    defaultValue = 0


_BgpPeerConfigMaxPrfx_Object = MibTableColumn
bgpPeerConfigMaxPrfx = _BgpPeerConfigMaxPrfx_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 43),
    _BgpPeerConfigMaxPrfx_Type()
)
bgpPeerConfigMaxPrfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfigMaxPrfx.setStatus("current")


class _BgpPeerConfigDropWarn_Type(BgpDropOrWarn):
    """Custom type bgpPeerConfigDropWarn based on BgpDropOrWarn"""


_BgpPeerConfigDropWarn_Object = MibTableColumn
bgpPeerConfigDropWarn = _BgpPeerConfigDropWarn_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 44),
    _BgpPeerConfigDropWarn_Type()
)
bgpPeerConfigDropWarn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfigDropWarn.setStatus("current")


class _BgpPeerConfigPassive_Type(TruthValue):
    """Custom type bgpPeerConfigPassive based on TruthValue"""


_BgpPeerConfigPassive_Object = MibTableColumn
bgpPeerConfigPassive = _BgpPeerConfigPassive_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 45),
    _BgpPeerConfigPassive_Type()
)
bgpPeerConfigPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfigPassive.setStatus("current")


class _BgpPeerConfigOpenDelay_Type(Unsigned32):
    """Custom type bgpPeerConfigOpenDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_BgpPeerConfigOpenDelay_Type.__name__ = "Unsigned32"
_BgpPeerConfigOpenDelay_Object = MibTableColumn
bgpPeerConfigOpenDelay = _BgpPeerConfigOpenDelay_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 46),
    _BgpPeerConfigOpenDelay_Type()
)
bgpPeerConfigOpenDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfigOpenDelay.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerConfigOpenDelay.setUnits("seconds")


class _BgpPeerConfigIdleHold_Type(Unsigned32):
    """Custom type bgpPeerConfigIdleHold based on Unsigned32"""
    defaultValue = 15

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_BgpPeerConfigIdleHold_Type.__name__ = "Unsigned32"
_BgpPeerConfigIdleHold_Object = MibTableColumn
bgpPeerConfigIdleHold = _BgpPeerConfigIdleHold_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 47),
    _BgpPeerConfigIdleHold_Type()
)
bgpPeerConfigIdleHold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfigIdleHold.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerConfigIdleHold.setUnits("seconds")


class _BgpPeerPassword_Type(OctetString):
    """Custom type bgpPeerPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BgpPeerPassword_Type.__name__ = "OctetString"
_BgpPeerPassword_Object = MibTableColumn
bgpPeerPassword = _BgpPeerPassword_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 48),
    _BgpPeerPassword_Type()
)
bgpPeerPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerPassword.setStatus("current")


class _BgpPeerTtl_Type(Integer32):
    """Custom type bgpPeerTtl based on Integer32"""
    defaultValue = 0


_BgpPeerTtl_Object = MibTableColumn
bgpPeerTtl = _BgpPeerTtl_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 49),
    _BgpPeerTtl_Type()
)
bgpPeerTtl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerTtl.setStatus("current")


class _BgpPeerCheckFirstAsNum_Type(TruthValue):
    """Custom type bgpPeerCheckFirstAsNum based on TruthValue"""


_BgpPeerCheckFirstAsNum_Object = MibTableColumn
bgpPeerCheckFirstAsNum = _BgpPeerCheckFirstAsNum_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 50),
    _BgpPeerCheckFirstAsNum_Type()
)
bgpPeerCheckFirstAsNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerCheckFirstAsNum.setStatus("current")


class _BgpPeerAggrInclConfedAS_Type(TruthValue):
    """Custom type bgpPeerAggrInclConfedAS based on TruthValue"""


_BgpPeerAggrInclConfedAS_Object = MibTableColumn
bgpPeerAggrInclConfedAS = _BgpPeerAggrInclConfedAS_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 51),
    _BgpPeerAggrInclConfedAS_Type()
)
bgpPeerAggrInclConfedAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAggrInclConfedAS.setStatus("current")


class _BgpPeerMinRouteWithdrawInterval_Type(Unsigned32):
    """Custom type bgpPeerMinRouteWithdrawInterval based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BgpPeerMinRouteWithdrawInterval_Type.__name__ = "Unsigned32"
_BgpPeerMinRouteWithdrawInterval_Object = MibTableColumn
bgpPeerMinRouteWithdrawInterval = _BgpPeerMinRouteWithdrawInterval_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 52),
    _BgpPeerMinRouteWithdrawInterval_Type()
)
bgpPeerMinRouteWithdrawInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerMinRouteWithdrawInterval.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerMinRouteWithdrawInterval.setUnits("seconds")


class _BgpPeerStalePathTime_Type(Unsigned32):
    """Custom type bgpPeerStalePathTime based on Unsigned32"""
    defaultValue = 30


_BgpPeerStalePathTime_Object = MibTableColumn
bgpPeerStalePathTime = _BgpPeerStalePathTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 53),
    _BgpPeerStalePathTime_Type()
)
bgpPeerStalePathTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerStalePathTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpPeerStalePathTime.setUnits("seconds")


class _BgpPeerCheckNextHop_Type(TruthValue):
    """Custom type bgpPeerCheckNextHop based on TruthValue"""


_BgpPeerCheckNextHop_Object = MibTableColumn
bgpPeerCheckNextHop = _BgpPeerCheckNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 54),
    _BgpPeerCheckNextHop_Type()
)
bgpPeerCheckNextHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerCheckNextHop.setStatus("current")
_BgpPeerLocalAddrScopeId_Type = Unsigned32
_BgpPeerLocalAddrScopeId_Object = MibTableColumn
bgpPeerLocalAddrScopeId = _BgpPeerLocalAddrScopeId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 55),
    _BgpPeerLocalAddrScopeId_Type()
)
bgpPeerLocalAddrScopeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerLocalAddrScopeId.setStatus("current")


class _BgpPeerMaxOrfEntries_Type(Unsigned32):
    """Custom type bgpPeerMaxOrfEntries based on Unsigned32"""
    defaultValue = 100000


_BgpPeerMaxOrfEntries_Object = MibTableColumn
bgpPeerMaxOrfEntries = _BgpPeerMaxOrfEntries_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 56),
    _BgpPeerMaxOrfEntries_Type()
)
bgpPeerMaxOrfEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerMaxOrfEntries.setStatus("current")
_BgpPeerOrfEntryCount_Type = Counter32
_BgpPeerOrfEntryCount_Object = MibTableColumn
bgpPeerOrfEntryCount = _BgpPeerOrfEntryCount_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 57),
    _BgpPeerOrfEntryCount_Type()
)
bgpPeerOrfEntryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerOrfEntryCount.setStatus("current")


class _BgpPeerPeeringType_Type(BgpPeeringType):
    """Custom type bgpPeerPeeringType based on BgpPeeringType"""


_BgpPeerPeeringType_Object = MibTableColumn
bgpPeerPeeringType = _BgpPeerPeeringType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 58),
    _BgpPeerPeeringType_Type()
)
bgpPeerPeeringType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerPeeringType.setStatus("current")


class _BgpPeerSoftResetWithStoredInfo_Type(TruthValue):
    """Custom type bgpPeerSoftResetWithStoredInfo based on TruthValue"""


_BgpPeerSoftResetWithStoredInfo_Object = MibTableColumn
bgpPeerSoftResetWithStoredInfo = _BgpPeerSoftResetWithStoredInfo_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 59),
    _BgpPeerSoftResetWithStoredInfo_Type()
)
bgpPeerSoftResetWithStoredInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerSoftResetWithStoredInfo.setStatus("current")


class _BgpPeerAllowLocalAs_Type(Unsigned32):
    """Custom type bgpPeerAllowLocalAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpPeerAllowLocalAs_Type.__name__ = "Unsigned32"
_BgpPeerAllowLocalAs_Object = MibTableColumn
bgpPeerAllowLocalAs = _BgpPeerAllowLocalAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 60),
    _BgpPeerAllowLocalAs_Type()
)
bgpPeerAllowLocalAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAllowLocalAs.setStatus("current")


class _BgpPeerDisableSenderLoopDetect_Type(TruthValue):
    """Custom type bgpPeerDisableSenderLoopDetect based on TruthValue"""


_BgpPeerDisableSenderLoopDetect_Object = MibTableColumn
bgpPeerDisableSenderLoopDetect = _BgpPeerDisableSenderLoopDetect_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 61),
    _BgpPeerDisableSenderLoopDetect_Type()
)
bgpPeerDisableSenderLoopDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerDisableSenderLoopDetect.setStatus("current")


class _BgpPeerDisableRouteRefresh_Type(TruthValue):
    """Custom type bgpPeerDisableRouteRefresh based on TruthValue"""


_BgpPeerDisableRouteRefresh_Object = MibTableColumn
bgpPeerDisableRouteRefresh = _BgpPeerDisableRouteRefresh_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 62),
    _BgpPeerDisableRouteRefresh_Type()
)
bgpPeerDisableRouteRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerDisableRouteRefresh.setStatus("current")


class _BgpPeerFlapStatsClearStat_Type(TruthValue):
    """Custom type bgpPeerFlapStatsClearStat based on TruthValue"""


_BgpPeerFlapStatsClearStat_Object = MibTableColumn
bgpPeerFlapStatsClearStat = _BgpPeerFlapStatsClearStat_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 63),
    _BgpPeerFlapStatsClearStat_Type()
)
bgpPeerFlapStatsClearStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerFlapStatsClearStat.setStatus("current")


class _BgpPeerFlapStatsClearMap_Type(Unsigned32):
    """Custom type bgpPeerFlapStatsClearMap based on Unsigned32"""
    defaultValue = 0


_BgpPeerFlapStatsClearMap_Object = MibTableColumn
bgpPeerFlapStatsClearMap = _BgpPeerFlapStatsClearMap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 64),
    _BgpPeerFlapStatsClearMap_Type()
)
bgpPeerFlapStatsClearMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerFlapStatsClearMap.setStatus("current")


class _BgpPeerLastErrorRcvd_Type(OctetString):
    """Custom type bgpPeerLastErrorRcvd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BgpPeerLastErrorRcvd_Type.__name__ = "OctetString"
_BgpPeerLastErrorRcvd_Object = MibTableColumn
bgpPeerLastErrorRcvd = _BgpPeerLastErrorRcvd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 65),
    _BgpPeerLastErrorRcvd_Type()
)
bgpPeerLastErrorRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastErrorRcvd.setStatus("current")
_BgpPeerLastErrorRcvdTime_Type = TimeStamp
_BgpPeerLastErrorRcvdTime_Object = MibTableColumn
bgpPeerLastErrorRcvdTime = _BgpPeerLastErrorRcvdTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 66),
    _BgpPeerLastErrorRcvdTime_Type()
)
bgpPeerLastErrorRcvdTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastErrorRcvdTime.setStatus("current")


class _BgpPeerLastErrorSent_Type(OctetString):
    """Custom type bgpPeerLastErrorSent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_BgpPeerLastErrorSent_Type.__name__ = "OctetString"
_BgpPeerLastErrorSent_Object = MibTableColumn
bgpPeerLastErrorSent = _BgpPeerLastErrorSent_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 67),
    _BgpPeerLastErrorSent_Type()
)
bgpPeerLastErrorSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastErrorSent.setStatus("current")
_BgpPeerLastErrorSentTime_Type = TimeStamp
_BgpPeerLastErrorSentTime_Object = MibTableColumn
bgpPeerLastErrorSentTime = _BgpPeerLastErrorSentTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 68),
    _BgpPeerLastErrorSentTime_Type()
)
bgpPeerLastErrorSentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastErrorSentTime.setStatus("current")
_BgpPeerLastState_Type = BgpPeerStates
_BgpPeerLastState_Object = MibTableColumn
bgpPeerLastState = _BgpPeerLastState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 69),
    _BgpPeerLastState_Type()
)
bgpPeerLastState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastState.setStatus("current")
_BgpPeerLastEvent_Type = BgpPeerEvents
_BgpPeerLastEvent_Object = MibTableColumn
bgpPeerLastEvent = _BgpPeerLastEvent_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 70),
    _BgpPeerLastEvent_Type()
)
bgpPeerLastEvent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerLastEvent.setStatus("current")
_BgpPeerCapsSent_Type = BgpCapabilities
_BgpPeerCapsSent_Object = MibTableColumn
bgpPeerCapsSent = _BgpPeerCapsSent_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 71),
    _BgpPeerCapsSent_Type()
)
bgpPeerCapsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerCapsSent.setStatus("current")
_BgpPeerCapsRcvd_Type = BgpCapabilities
_BgpPeerCapsRcvd_Object = MibTableColumn
bgpPeerCapsRcvd = _BgpPeerCapsRcvd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 72),
    _BgpPeerCapsRcvd_Type()
)
bgpPeerCapsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerCapsRcvd.setStatus("current")
_BgpPeerCapsNegotiated_Type = BgpCapabilities
_BgpPeerCapsNegotiated_Object = MibTableColumn
bgpPeerCapsNegotiated = _BgpPeerCapsNegotiated_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 73),
    _BgpPeerCapsNegotiated_Type()
)
bgpPeerCapsNegotiated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerCapsNegotiated.setStatus("current")
_BgpPeerRstrSupport_Type = BgpPeerRestartSupport
_BgpPeerRstrSupport_Object = MibTableColumn
bgpPeerRstrSupport = _BgpPeerRstrSupport_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 74),
    _BgpPeerRstrSupport_Type()
)
bgpPeerRstrSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRstrSupport.setStatus("current")
_BgpPeerRstrFamily_Type = BgpAfiSafiBits
_BgpPeerRstrFamily_Object = MibTableColumn
bgpPeerRstrFamily = _BgpPeerRstrFamily_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 75),
    _BgpPeerRstrFamily_Type()
)
bgpPeerRstrFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRstrFamily.setStatus("current")
_BgpPeerRstrRestarting_Type = TruthValue
_BgpPeerRstrRestarting_Object = MibTableColumn
bgpPeerRstrRestarting = _BgpPeerRstrRestarting_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 76),
    _BgpPeerRstrRestarting_Type()
)
bgpPeerRstrRestarting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRstrRestarting.setStatus("current")
_BgpPeerRstrStatus_Type = BgpPeerRestartStatus
_BgpPeerRstrStatus_Object = MibTableColumn
bgpPeerRstrStatus = _BgpPeerRstrStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 77),
    _BgpPeerRstrStatus_Type()
)
bgpPeerRstrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRstrStatus.setStatus("current")
_BgpPeerRstrRemTime_Type = TimeInterval
_BgpPeerRstrRemTime_Object = MibTableColumn
bgpPeerRstrRemTime = _BgpPeerRstrRemTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 78),
    _BgpPeerRstrRemTime_Type()
)
bgpPeerRstrRemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRstrRemTime.setStatus("current")
_BgpPeerRcvdMsgElapsedTime_Type = TimeInterval
_BgpPeerRcvdMsgElapsedTime_Object = MibTableColumn
bgpPeerRcvdMsgElapsedTime = _BgpPeerRcvdMsgElapsedTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 79),
    _BgpPeerRcvdMsgElapsedTime_Type()
)
bgpPeerRcvdMsgElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRcvdMsgElapsedTime.setStatus("current")
_BgpPeerIdleHoldRemTime_Type = TimeInterval
_BgpPeerIdleHoldRemTime_Object = MibTableColumn
bgpPeerIdleHoldRemTime = _BgpPeerIdleHoldRemTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 80),
    _BgpPeerIdleHoldRemTime_Type()
)
bgpPeerIdleHoldRemTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerIdleHoldRemTime.setStatus("current")
_BgpPeerRouteRefrSent_Type = Counter32
_BgpPeerRouteRefrSent_Object = MibTableColumn
bgpPeerRouteRefrSent = _BgpPeerRouteRefrSent_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 81),
    _BgpPeerRouteRefrSent_Type()
)
bgpPeerRouteRefrSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRouteRefrSent.setStatus("current")
_BgpPeerRouteRefrRcvd_Type = Counter32
_BgpPeerRouteRefrRcvd_Object = MibTableColumn
bgpPeerRouteRefrRcvd = _BgpPeerRouteRefrRcvd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 82),
    _BgpPeerRouteRefrRcvd_Type()
)
bgpPeerRouteRefrRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerRouteRefrRcvd.setStatus("current")


class _BgpPeerNxtHopSlf_Type(TruthValue):
    """Custom type bgpPeerNxtHopSlf based on TruthValue"""


_BgpPeerNxtHopSlf_Object = MibTableColumn
bgpPeerNxtHopSlf = _BgpPeerNxtHopSlf_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 83),
    _BgpPeerNxtHopSlf_Type()
)
bgpPeerNxtHopSlf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerNxtHopSlf.setStatus("current")


class _BgpPeerThirdPtyNxtHop_Type(TruthValue):
    """Custom type bgpPeerThirdPtyNxtHop based on TruthValue"""


_BgpPeerThirdPtyNxtHop_Object = MibTableColumn
bgpPeerThirdPtyNxtHop = _BgpPeerThirdPtyNxtHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 84),
    _BgpPeerThirdPtyNxtHop_Type()
)
bgpPeerThirdPtyNxtHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerThirdPtyNxtHop.setStatus("current")


class _BgpPeerNxtHopPeer_Type(TruthValue):
    """Custom type bgpPeerNxtHopPeer based on TruthValue"""


_BgpPeerNxtHopPeer_Object = MibTableColumn
bgpPeerNxtHopPeer = _BgpPeerNxtHopPeer_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 85),
    _BgpPeerNxtHopPeer_Type()
)
bgpPeerNxtHopPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerNxtHopPeer.setStatus("current")


class _BgpPeerTrapPrefix_Type(TruthValue):
    """Custom type bgpPeerTrapPrefix based on TruthValue"""


_BgpPeerTrapPrefix_Object = MibTableColumn
bgpPeerTrapPrefix = _BgpPeerTrapPrefix_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 86),
    _BgpPeerTrapPrefix_Type()
)
bgpPeerTrapPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerTrapPrefix.setStatus("current")


class _BgpPeerConfigThreshold_Type(Unsigned32):
    """Custom type bgpPeerConfigThreshold based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BgpPeerConfigThreshold_Type.__name__ = "Unsigned32"
_BgpPeerConfigThreshold_Object = MibTableColumn
bgpPeerConfigThreshold = _BgpPeerConfigThreshold_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 87),
    _BgpPeerConfigThreshold_Type()
)
bgpPeerConfigThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfigThreshold.setStatus("current")


class _BgpPeerMaxPrfxHold_Type(Unsigned32):
    """Custom type bgpPeerMaxPrfxHold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_BgpPeerMaxPrfxHold_Type.__name__ = "Unsigned32"
_BgpPeerMaxPrfxHold_Object = MibTableColumn
bgpPeerMaxPrfxHold = _BgpPeerMaxPrfxHold_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 88),
    _BgpPeerMaxPrfxHold_Type()
)
bgpPeerMaxPrfxHold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerMaxPrfxHold.setStatus("current")
_BgpPeerSelectedLocalAddrType_Type = InetAddressType
_BgpPeerSelectedLocalAddrType_Object = MibTableColumn
bgpPeerSelectedLocalAddrType = _BgpPeerSelectedLocalAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 89),
    _BgpPeerSelectedLocalAddrType_Type()
)
bgpPeerSelectedLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerSelectedLocalAddrType.setStatus("current")


class _BgpPeerSelectedLocalAddr_Type(InetAddress):
    """Custom type bgpPeerSelectedLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpPeerSelectedLocalAddr_Type.__name__ = "InetAddress"
_BgpPeerSelectedLocalAddr_Object = MibTableColumn
bgpPeerSelectedLocalAddr = _BgpPeerSelectedLocalAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 90),
    _BgpPeerSelectedLocalAddr_Type()
)
bgpPeerSelectedLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerSelectedLocalAddr.setStatus("current")
_BgpPeerSelectedLocalPort_Type = InetPortNumber
_BgpPeerSelectedLocalPort_Object = MibTableColumn
bgpPeerSelectedLocalPort = _BgpPeerSelectedLocalPort_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 91),
    _BgpPeerSelectedLocalPort_Type()
)
bgpPeerSelectedLocalPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerSelectedLocalPort.setStatus("current")
_BgpPeerSelectedRemotePort_Type = InetPortNumber
_BgpPeerSelectedRemotePort_Object = MibTableColumn
bgpPeerSelectedRemotePort = _BgpPeerSelectedRemotePort_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 92),
    _BgpPeerSelectedRemotePort_Type()
)
bgpPeerSelectedRemotePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerSelectedRemotePort.setStatus("current")


class _BgpPeerBfdDesired_Type(TruthValue):
    """Custom type bgpPeerBfdDesired based on TruthValue"""


_BgpPeerBfdDesired_Object = MibTableColumn
bgpPeerBfdDesired = _BgpPeerBfdDesired_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 93),
    _BgpPeerBfdDesired_Type()
)
bgpPeerBfdDesired.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerBfdDesired.setStatus("current")
_BgpPeerBfdStatus_Type = BfdSessionStatus
_BgpPeerBfdStatus_Object = MibTableColumn
bgpPeerBfdStatus = _BgpPeerBfdStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 94),
    _BgpPeerBfdStatus_Type()
)
bgpPeerBfdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerBfdStatus.setStatus("current")


class _BgpPeerCeaseErrorSubcode_Type(BgpCeaseErrorSubcode):
    """Custom type bgpPeerCeaseErrorSubcode based on BgpCeaseErrorSubcode"""


_BgpPeerCeaseErrorSubcode_Object = MibTableColumn
bgpPeerCeaseErrorSubcode = _BgpPeerCeaseErrorSubcode_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 95),
    _BgpPeerCeaseErrorSubcode_Type()
)
bgpPeerCeaseErrorSubcode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerCeaseErrorSubcode.setStatus("current")


class _BgpPeerConfAltLocalAs_Type(BgpAutonomousSystemNumber):
    """Custom type bgpPeerConfAltLocalAs based on BgpAutonomousSystemNumber"""
    defaultValue = 0


_BgpPeerConfAltLocalAs_Object = MibTableColumn
bgpPeerConfAltLocalAs = _BgpPeerConfAltLocalAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 96),
    _BgpPeerConfAltLocalAs_Type()
)
bgpPeerConfAltLocalAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerConfAltLocalAs.setStatus("current")
_BgpPeerSelectedLocalAs_Type = BgpAutonomousSystemNumber
_BgpPeerSelectedLocalAs_Object = MibTableColumn
bgpPeerSelectedLocalAs = _BgpPeerSelectedLocalAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 97),
    _BgpPeerSelectedLocalAs_Type()
)
bgpPeerSelectedLocalAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerSelectedLocalAs.setStatus("current")
_BgpPeerSelectedRemoteAs_Type = BgpAutonomousSystemNumber
_BgpPeerSelectedRemoteAs_Object = MibTableColumn
bgpPeerSelectedRemoteAs = _BgpPeerSelectedRemoteAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 98),
    _BgpPeerSelectedRemoteAs_Type()
)
bgpPeerSelectedRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerSelectedRemoteAs.setStatus("current")
_BgpPeerInPrfxes_Type = Gauge32
_BgpPeerInPrfxes_Object = MibTableColumn
bgpPeerInPrfxes = _BgpPeerInPrfxes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 99),
    _BgpPeerInPrfxes_Type()
)
bgpPeerInPrfxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerInPrfxes.setStatus("current")
_BgpPeerOutPrfxes_Type = Gauge32
_BgpPeerOutPrfxes_Object = MibTableColumn
bgpPeerOutPrfxes = _BgpPeerOutPrfxes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 100),
    _BgpPeerOutPrfxes_Type()
)
bgpPeerOutPrfxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerOutPrfxes.setStatus("current")
_BgpPeerOutPrfxesAdvertised_Type = Gauge32
_BgpPeerOutPrfxesAdvertised_Object = MibTableColumn
bgpPeerOutPrfxesAdvertised = _BgpPeerOutPrfxesAdvertised_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 101),
    _BgpPeerOutPrfxesAdvertised_Type()
)
bgpPeerOutPrfxesAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerOutPrfxesAdvertised.setStatus("current")


class _BgpPeerTrapGrHelperState_Type(TruthValue):
    """Custom type bgpPeerTrapGrHelperState based on TruthValue"""


_BgpPeerTrapGrHelperState_Object = MibTableColumn
bgpPeerTrapGrHelperState = _BgpPeerTrapGrHelperState_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 102),
    _BgpPeerTrapGrHelperState_Type()
)
bgpPeerTrapGrHelperState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerTrapGrHelperState.setStatus("current")


class _BgpPeerEnableAttributeDiscard_Type(TruthValue):
    """Custom type bgpPeerEnableAttributeDiscard based on TruthValue"""


_BgpPeerEnableAttributeDiscard_Object = MibTableColumn
bgpPeerEnableAttributeDiscard = _BgpPeerEnableAttributeDiscard_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 1, 1, 103),
    _BgpPeerEnableAttributeDiscard_Type()
)
bgpPeerEnableAttributeDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerEnableAttributeDiscard.setStatus("current")
_BgpPeerAfiSafiTable_Object = MibTable
bgpPeerAfiSafiTable = _BgpPeerAfiSafiTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    bgpPeerAfiSafiTable.setStatus("current")
_BgpPeerAfiSafiEntry_Object = MibTableRow
bgpPeerAfiSafiEntry = _BgpPeerAfiSafiEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1)
)
bgpPeerAfiSafiEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpPeerLocalAddrType"),
    (0, "DC-BGP-MIB", "bgpPeerLocalAddr"),
    (0, "DC-BGP-MIB", "bgpPeerLocalPort"),
    (0, "DC-BGP-MIB", "bgpPeerRemoteAddrType"),
    (0, "DC-BGP-MIB", "bgpPeerRemoteAddr"),
    (0, "DC-BGP-MIB", "bgpPeerRemotePort"),
    (0, "DC-BGP-MIB", "bgpPeerLocalAddrScopeId"),
    (0, "DC-BGP-MIB", "bgpPeerAfiSafiAfi"),
    (0, "DC-BGP-MIB", "bgpPeerAfiSafiSafi"),
)
if mibBuilder.loadTexts:
    bgpPeerAfiSafiEntry.setStatus("current")
_BgpPeerAfiSafiAfi_Type = BgpAfi
_BgpPeerAfiSafiAfi_Object = MibTableColumn
bgpPeerAfiSafiAfi = _BgpPeerAfiSafiAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 8),
    _BgpPeerAfiSafiAfi_Type()
)
bgpPeerAfiSafiAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiAfi.setStatus("current")
_BgpPeerAfiSafiSafi_Type = BgpSafi
_BgpPeerAfiSafiSafi_Object = MibTableColumn
bgpPeerAfiSafiSafi = _BgpPeerAfiSafiSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 9),
    _BgpPeerAfiSafiSafi_Type()
)
bgpPeerAfiSafiSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiSafi.setStatus("current")


class _BgpPeerAfiSafiDisable_Type(TruthValue):
    """Custom type bgpPeerAfiSafiDisable based on TruthValue"""


_BgpPeerAfiSafiDisable_Object = MibTableColumn
bgpPeerAfiSafiDisable = _BgpPeerAfiSafiDisable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 10),
    _BgpPeerAfiSafiDisable_Type()
)
bgpPeerAfiSafiDisable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiDisable.setStatus("current")


class _BgpPeerAfiSafiConfigRtRefresh_Type(TruthValue):
    """Custom type bgpPeerAfiSafiConfigRtRefresh based on TruthValue"""


_BgpPeerAfiSafiConfigRtRefresh_Object = MibTableColumn
bgpPeerAfiSafiConfigRtRefresh = _BgpPeerAfiSafiConfigRtRefresh_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 11),
    _BgpPeerAfiSafiConfigRtRefresh_Type()
)
bgpPeerAfiSafiConfigRtRefresh.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiConfigRtRefresh.setStatus("current")


class _BgpPeerAfiSafiAllowLocalAs_Type(Unsigned32):
    """Custom type bgpPeerAfiSafiAllowLocalAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpPeerAfiSafiAllowLocalAs_Type.__name__ = "Unsigned32"
_BgpPeerAfiSafiAllowLocalAs_Object = MibTableColumn
bgpPeerAfiSafiAllowLocalAs = _BgpPeerAfiSafiAllowLocalAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 12),
    _BgpPeerAfiSafiAllowLocalAs_Type()
)
bgpPeerAfiSafiAllowLocalAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiAllowLocalAs.setStatus("current")


class _BgpPeerAfiSafiDisableSndLpDetect_Type(TruthValue):
    """Custom type bgpPeerAfiSafiDisableSndLpDetect based on TruthValue"""


_BgpPeerAfiSafiDisableSndLpDetect_Object = MibTableColumn
bgpPeerAfiSafiDisableSndLpDetect = _BgpPeerAfiSafiDisableSndLpDetect_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 13),
    _BgpPeerAfiSafiDisableSndLpDetect_Type()
)
bgpPeerAfiSafiDisableSndLpDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiDisableSndLpDetect.setStatus("current")


class _BgpPeerAfiSafiNxtHopSlf_Type(TruthValue):
    """Custom type bgpPeerAfiSafiNxtHopSlf based on TruthValue"""


_BgpPeerAfiSafiNxtHopSlf_Object = MibTableColumn
bgpPeerAfiSafiNxtHopSlf = _BgpPeerAfiSafiNxtHopSlf_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 14),
    _BgpPeerAfiSafiNxtHopSlf_Type()
)
bgpPeerAfiSafiNxtHopSlf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiNxtHopSlf.setStatus("current")


class _BgpPeerAfiSafiOrigDefault_Type(TruthValue):
    """Custom type bgpPeerAfiSafiOrigDefault based on TruthValue"""


_BgpPeerAfiSafiOrigDefault_Object = MibTableColumn
bgpPeerAfiSafiOrigDefault = _BgpPeerAfiSafiOrigDefault_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 15),
    _BgpPeerAfiSafiOrigDefault_Type()
)
bgpPeerAfiSafiOrigDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiOrigDefault.setStatus("current")


class _BgpPeerAfiSafiOrigDefaultRtMap_Type(Unsigned32):
    """Custom type bgpPeerAfiSafiOrigDefaultRtMap based on Unsigned32"""
    defaultValue = 0


_BgpPeerAfiSafiOrigDefaultRtMap_Object = MibTableColumn
bgpPeerAfiSafiOrigDefaultRtMap = _BgpPeerAfiSafiOrigDefaultRtMap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 16),
    _BgpPeerAfiSafiOrigDefaultRtMap_Type()
)
bgpPeerAfiSafiOrigDefaultRtMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiOrigDefaultRtMap.setStatus("current")


class _BgpPeerAfiSafiSoftResetStore_Type(TruthValue):
    """Custom type bgpPeerAfiSafiSoftResetStore based on TruthValue"""


_BgpPeerAfiSafiSoftResetStore_Object = MibTableColumn
bgpPeerAfiSafiSoftResetStore = _BgpPeerAfiSafiSoftResetStore_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 17),
    _BgpPeerAfiSafiSoftResetStore_Type()
)
bgpPeerAfiSafiSoftResetStore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiSoftResetStore.setStatus("current")


class _BgpPeerAfiSafiConfigMaxPrfx_Type(Unsigned32):
    """Custom type bgpPeerAfiSafiConfigMaxPrfx based on Unsigned32"""
    defaultValue = 0


_BgpPeerAfiSafiConfigMaxPrfx_Object = MibTableColumn
bgpPeerAfiSafiConfigMaxPrfx = _BgpPeerAfiSafiConfigMaxPrfx_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 18),
    _BgpPeerAfiSafiConfigMaxPrfx_Type()
)
bgpPeerAfiSafiConfigMaxPrfx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiConfigMaxPrfx.setStatus("current")


class _BgpPeerAfiSafiConfigDropWarn_Type(BgpDropOrWarn):
    """Custom type bgpPeerAfiSafiConfigDropWarn based on BgpDropOrWarn"""


_BgpPeerAfiSafiConfigDropWarn_Object = MibTableColumn
bgpPeerAfiSafiConfigDropWarn = _BgpPeerAfiSafiConfigDropWarn_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 19),
    _BgpPeerAfiSafiConfigDropWarn_Type()
)
bgpPeerAfiSafiConfigDropWarn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiConfigDropWarn.setStatus("current")


class _BgpPeerAfiSafiTrapPrefix_Type(TruthValue):
    """Custom type bgpPeerAfiSafiTrapPrefix based on TruthValue"""


_BgpPeerAfiSafiTrapPrefix_Object = MibTableColumn
bgpPeerAfiSafiTrapPrefix = _BgpPeerAfiSafiTrapPrefix_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 20),
    _BgpPeerAfiSafiTrapPrefix_Type()
)
bgpPeerAfiSafiTrapPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiTrapPrefix.setStatus("current")


class _BgpPeerAfiSafiConfigThreshold_Type(Unsigned32):
    """Custom type bgpPeerAfiSafiConfigThreshold based on Unsigned32"""
    defaultValue = 75

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_BgpPeerAfiSafiConfigThreshold_Type.__name__ = "Unsigned32"
_BgpPeerAfiSafiConfigThreshold_Object = MibTableColumn
bgpPeerAfiSafiConfigThreshold = _BgpPeerAfiSafiConfigThreshold_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 21),
    _BgpPeerAfiSafiConfigThreshold_Type()
)
bgpPeerAfiSafiConfigThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiConfigThreshold.setStatus("current")


class _BgpPeerAfiSafiMaxPrfxHold_Type(Unsigned32):
    """Custom type bgpPeerAfiSafiMaxPrfxHold based on Unsigned32"""
    defaultValue = 90

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_BgpPeerAfiSafiMaxPrfxHold_Type.__name__ = "Unsigned32"
_BgpPeerAfiSafiMaxPrfxHold_Object = MibTableColumn
bgpPeerAfiSafiMaxPrfxHold = _BgpPeerAfiSafiMaxPrfxHold_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 22),
    _BgpPeerAfiSafiMaxPrfxHold_Type()
)
bgpPeerAfiSafiMaxPrfxHold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiMaxPrfxHold.setStatus("current")


class _BgpPeerAfiSafiMaxOrfEntries_Type(Unsigned32):
    """Custom type bgpPeerAfiSafiMaxOrfEntries based on Unsigned32"""
    defaultValue = 0


_BgpPeerAfiSafiMaxOrfEntries_Object = MibTableColumn
bgpPeerAfiSafiMaxOrfEntries = _BgpPeerAfiSafiMaxOrfEntries_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 2, 1, 23),
    _BgpPeerAfiSafiMaxOrfEntries_Type()
)
bgpPeerAfiSafiMaxOrfEntries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerAfiSafiMaxOrfEntries.setStatus("current")
_BgpPeerOrfCapabilityTable_Object = MibTable
bgpPeerOrfCapabilityTable = _BgpPeerOrfCapabilityTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 3)
)
if mibBuilder.loadTexts:
    bgpPeerOrfCapabilityTable.setStatus("current")
_BgpPeerOrfCapabilityEntry_Object = MibTableRow
bgpPeerOrfCapabilityEntry = _BgpPeerOrfCapabilityEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 3, 1)
)
bgpPeerOrfCapabilityEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpPeerLocalAddrType"),
    (0, "DC-BGP-MIB", "bgpPeerLocalAddr"),
    (0, "DC-BGP-MIB", "bgpPeerLocalPort"),
    (0, "DC-BGP-MIB", "bgpPeerRemoteAddrType"),
    (0, "DC-BGP-MIB", "bgpPeerRemoteAddr"),
    (0, "DC-BGP-MIB", "bgpPeerRemotePort"),
    (0, "DC-BGP-MIB", "bgpPeerLocalAddrScopeId"),
    (0, "DC-BGP-MIB", "bgpPeerOrfCapabilityAfi"),
    (0, "DC-BGP-MIB", "bgpPeerOrfCapabilitySafi"),
    (0, "DC-BGP-MIB", "bgpPeerOrfCapabilityOrfType"),
)
if mibBuilder.loadTexts:
    bgpPeerOrfCapabilityEntry.setStatus("current")
_BgpPeerOrfCapabilityAfi_Type = BgpAfi
_BgpPeerOrfCapabilityAfi_Object = MibTableColumn
bgpPeerOrfCapabilityAfi = _BgpPeerOrfCapabilityAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 3, 1, 8),
    _BgpPeerOrfCapabilityAfi_Type()
)
bgpPeerOrfCapabilityAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerOrfCapabilityAfi.setStatus("current")
_BgpPeerOrfCapabilitySafi_Type = BgpSafi
_BgpPeerOrfCapabilitySafi_Object = MibTableColumn
bgpPeerOrfCapabilitySafi = _BgpPeerOrfCapabilitySafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 3, 1, 9),
    _BgpPeerOrfCapabilitySafi_Type()
)
bgpPeerOrfCapabilitySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerOrfCapabilitySafi.setStatus("current")
_BgpPeerOrfCapabilityOrfType_Type = BgpOrfType
_BgpPeerOrfCapabilityOrfType_Object = MibTableColumn
bgpPeerOrfCapabilityOrfType = _BgpPeerOrfCapabilityOrfType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 3, 1, 10),
    _BgpPeerOrfCapabilityOrfType_Type()
)
bgpPeerOrfCapabilityOrfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerOrfCapabilityOrfType.setStatus("current")


class _BgpPeerOrfCapabilityAdminStatus_Type(BgpAdminStatus):
    """Custom type bgpPeerOrfCapabilityAdminStatus based on BgpAdminStatus"""


_BgpPeerOrfCapabilityAdminStatus_Object = MibTableColumn
bgpPeerOrfCapabilityAdminStatus = _BgpPeerOrfCapabilityAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 3, 1, 11),
    _BgpPeerOrfCapabilityAdminStatus_Type()
)
bgpPeerOrfCapabilityAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerOrfCapabilityAdminStatus.setStatus("current")


class _BgpPeerOrfCapabilitySendReceive_Type(BgpOrfSendReceive):
    """Custom type bgpPeerOrfCapabilitySendReceive based on BgpOrfSendReceive"""


_BgpPeerOrfCapabilitySendReceive_Object = MibTableColumn
bgpPeerOrfCapabilitySendReceive = _BgpPeerOrfCapabilitySendReceive_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 1, 3, 1, 12),
    _BgpPeerOrfCapabilitySendReceive_Type()
)
bgpPeerOrfCapabilitySendReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeerOrfCapabilitySendReceive.setStatus("current")
_BgpPeerCaps_ObjectIdentity = ObjectIdentity
bgpPeerCaps = _BgpPeerCaps_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2)
)
_BgpPeerCapsRcvdTable_Object = MibTable
bgpPeerCapsRcvdTable = _BgpPeerCapsRcvdTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2, 1)
)
if mibBuilder.loadTexts:
    bgpPeerCapsRcvdTable.setStatus("current")
_BgpPeerCapsRcvdEntry_Object = MibTableRow
bgpPeerCapsRcvdEntry = _BgpPeerCapsRcvdEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2, 1, 1)
)
bgpPeerCapsRcvdEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpPeerIndex"),
    (0, "DC-BGP-MIB", "bgpPeerCapRcvdCode"),
    (0, "DC-BGP-MIB", "bgpPeerCapRcvdIndex"),
)
if mibBuilder.loadTexts:
    bgpPeerCapsRcvdEntry.setStatus("current")


class _BgpPeerCapRcvdCode_Type(Unsigned32):
    """Custom type bgpPeerCapRcvdCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpPeerCapRcvdCode_Type.__name__ = "Unsigned32"
_BgpPeerCapRcvdCode_Object = MibTableColumn
bgpPeerCapRcvdCode = _BgpPeerCapRcvdCode_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2, 1, 1, 3),
    _BgpPeerCapRcvdCode_Type()
)
bgpPeerCapRcvdCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerCapRcvdCode.setStatus("current")


class _BgpPeerCapRcvdIndex_Type(Unsigned32):
    """Custom type bgpPeerCapRcvdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BgpPeerCapRcvdIndex_Type.__name__ = "Unsigned32"
_BgpPeerCapRcvdIndex_Object = MibTableColumn
bgpPeerCapRcvdIndex = _BgpPeerCapRcvdIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2, 1, 1, 4),
    _BgpPeerCapRcvdIndex_Type()
)
bgpPeerCapRcvdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerCapRcvdIndex.setStatus("current")


class _BgpPeerCapRcvdValue_Type(OctetString):
    """Custom type bgpPeerCapRcvdValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BgpPeerCapRcvdValue_Type.__name__ = "OctetString"
_BgpPeerCapRcvdValue_Object = MibTableColumn
bgpPeerCapRcvdValue = _BgpPeerCapRcvdValue_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2, 1, 1, 5),
    _BgpPeerCapRcvdValue_Type()
)
bgpPeerCapRcvdValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerCapRcvdValue.setStatus("current")
_BgpPeerCapsSentTable_Object = MibTable
bgpPeerCapsSentTable = _BgpPeerCapsSentTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    bgpPeerCapsSentTable.setStatus("current")
_BgpPeerCapsSentEntry_Object = MibTableRow
bgpPeerCapsSentEntry = _BgpPeerCapsSentEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2, 2, 1)
)
bgpPeerCapsSentEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpPeerIndex"),
    (0, "DC-BGP-MIB", "bgpPeerCapSentCode"),
    (0, "DC-BGP-MIB", "bgpPeerCapSentIndex"),
)
if mibBuilder.loadTexts:
    bgpPeerCapsSentEntry.setStatus("current")


class _BgpPeerCapSentCode_Type(Unsigned32):
    """Custom type bgpPeerCapSentCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpPeerCapSentCode_Type.__name__ = "Unsigned32"
_BgpPeerCapSentCode_Object = MibTableColumn
bgpPeerCapSentCode = _BgpPeerCapSentCode_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2, 2, 1, 3),
    _BgpPeerCapSentCode_Type()
)
bgpPeerCapSentCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerCapSentCode.setStatus("current")


class _BgpPeerCapSentIndex_Type(Unsigned32):
    """Custom type bgpPeerCapSentIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_BgpPeerCapSentIndex_Type.__name__ = "Unsigned32"
_BgpPeerCapSentIndex_Object = MibTableColumn
bgpPeerCapSentIndex = _BgpPeerCapSentIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2, 2, 1, 4),
    _BgpPeerCapSentIndex_Type()
)
bgpPeerCapSentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeerCapSentIndex.setStatus("current")


class _BgpPeerCapSentValue_Type(OctetString):
    """Custom type bgpPeerCapSentValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_BgpPeerCapSentValue_Type.__name__ = "OctetString"
_BgpPeerCapSentValue_Object = MibTableColumn
bgpPeerCapSentValue = _BgpPeerCapSentValue_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 2, 2, 1, 5),
    _BgpPeerCapSentValue_Type()
)
bgpPeerCapSentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPeerCapSentValue.setStatus("current")
_BgpPeerCntrs_ObjectIdentity = ObjectIdentity
bgpPeerCntrs = _BgpPeerCntrs_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3)
)
_BgpPrfxCntrsTable_Object = MibTable
bgpPrfxCntrsTable = _BgpPrfxCntrsTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1)
)
if mibBuilder.loadTexts:
    bgpPrfxCntrsTable.setStatus("current")
_BgpPrfxCntrsEntry_Object = MibTableRow
bgpPrfxCntrsEntry = _BgpPrfxCntrsEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1)
)
bgpPrfxCntrsEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpPeerIndex"),
    (0, "DC-BGP-MIB", "bgpPrfxCntrsAfi"),
    (0, "DC-BGP-MIB", "bgpPrfxCntrsSafi"),
)
if mibBuilder.loadTexts:
    bgpPrfxCntrsEntry.setStatus("current")
_BgpPrfxCntrsAfi_Type = BgpAfi
_BgpPrfxCntrsAfi_Object = MibTableColumn
bgpPrfxCntrsAfi = _BgpPrfxCntrsAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 3),
    _BgpPrfxCntrsAfi_Type()
)
bgpPrfxCntrsAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPrfxCntrsAfi.setStatus("current")
_BgpPrfxCntrsSafi_Type = BgpSafi
_BgpPrfxCntrsSafi_Object = MibTableColumn
bgpPrfxCntrsSafi = _BgpPrfxCntrsSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 4),
    _BgpPrfxCntrsSafi_Type()
)
bgpPrfxCntrsSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPrfxCntrsSafi.setStatus("current")
_BgpPrfxInPrfxes_Type = Gauge32
_BgpPrfxInPrfxes_Object = MibTableColumn
bgpPrfxInPrfxes = _BgpPrfxInPrfxes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 5),
    _BgpPrfxInPrfxes_Type()
)
bgpPrfxInPrfxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxInPrfxes.setStatus("current")
_BgpPrfxInPrfxesAccepted_Type = Gauge32
_BgpPrfxInPrfxesAccepted_Object = MibTableColumn
bgpPrfxInPrfxesAccepted = _BgpPrfxInPrfxesAccepted_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 6),
    _BgpPrfxInPrfxesAccepted_Type()
)
bgpPrfxInPrfxesAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxInPrfxesAccepted.setStatus("current")
_BgpPrfxInPrfxesRejected_Type = Gauge32
_BgpPrfxInPrfxesRejected_Object = MibTableColumn
bgpPrfxInPrfxesRejected = _BgpPrfxInPrfxesRejected_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 7),
    _BgpPrfxInPrfxesRejected_Type()
)
bgpPrfxInPrfxesRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxInPrfxesRejected.setStatus("current")
_BgpPrfxOutPrfxes_Type = Gauge32
_BgpPrfxOutPrfxes_Object = MibTableColumn
bgpPrfxOutPrfxes = _BgpPrfxOutPrfxes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 8),
    _BgpPrfxOutPrfxes_Type()
)
bgpPrfxOutPrfxes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxOutPrfxes.setStatus("current")
_BgpPrfxOutPrfxesAdvertised_Type = Gauge32
_BgpPrfxOutPrfxesAdvertised_Object = MibTableColumn
bgpPrfxOutPrfxesAdvertised = _BgpPrfxOutPrfxesAdvertised_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 9),
    _BgpPrfxOutPrfxesAdvertised_Type()
)
bgpPrfxOutPrfxesAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxOutPrfxesAdvertised.setStatus("current")


class _BgpPrfxCntrsUserData_Type(OctetString):
    """Custom type bgpPrfxCntrsUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BgpPrfxCntrsUserData_Type.__name__ = "OctetString"
_BgpPrfxCntrsUserData_Object = MibTableColumn
bgpPrfxCntrsUserData = _BgpPrfxCntrsUserData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 10),
    _BgpPrfxCntrsUserData_Type()
)
bgpPrfxCntrsUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxCntrsUserData.setStatus("current")
_BgpPrfxInPrfxesFlapped_Type = Gauge32
_BgpPrfxInPrfxesFlapped_Object = MibTableColumn
bgpPrfxInPrfxesFlapped = _BgpPrfxInPrfxesFlapped_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 11),
    _BgpPrfxInPrfxesFlapped_Type()
)
bgpPrfxInPrfxesFlapped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxInPrfxesFlapped.setStatus("current")
_BgpPrfxInPrfxesFlapSuppressed_Type = Gauge32
_BgpPrfxInPrfxesFlapSuppressed_Object = MibTableColumn
bgpPrfxInPrfxesFlapSuppressed = _BgpPrfxInPrfxesFlapSuppressed_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 12),
    _BgpPrfxInPrfxesFlapSuppressed_Type()
)
bgpPrfxInPrfxesFlapSuppressed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxInPrfxesFlapSuppressed.setStatus("current")
_BgpPrfxInPrfxesFlapHistory_Type = Gauge32
_BgpPrfxInPrfxesFlapHistory_Object = MibTableColumn
bgpPrfxInPrfxesFlapHistory = _BgpPrfxInPrfxesFlapHistory_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 13),
    _BgpPrfxInPrfxesFlapHistory_Type()
)
bgpPrfxInPrfxesFlapHistory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxInPrfxesFlapHistory.setStatus("current")
_BgpPrfxInPrfxesActive_Type = Gauge32
_BgpPrfxInPrfxesActive_Object = MibTableColumn
bgpPrfxInPrfxesActive = _BgpPrfxInPrfxesActive_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 14),
    _BgpPrfxInPrfxesActive_Type()
)
bgpPrfxInPrfxesActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxInPrfxesActive.setStatus("current")
_BgpPrfxInPrfxesDeniedByPol_Type = Gauge32
_BgpPrfxInPrfxesDeniedByPol_Object = MibTableColumn
bgpPrfxInPrfxesDeniedByPol = _BgpPrfxInPrfxesDeniedByPol_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 15),
    _BgpPrfxInPrfxesDeniedByPol_Type()
)
bgpPrfxInPrfxesDeniedByPol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxInPrfxesDeniedByPol.setStatus("current")
_BgpPrfxNumLocRibRoutes_Type = Gauge32
_BgpPrfxNumLocRibRoutes_Object = MibTableColumn
bgpPrfxNumLocRibRoutes = _BgpPrfxNumLocRibRoutes_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 3, 3, 1, 1, 16),
    _BgpPrfxNumLocRibRoutes_Type()
)
bgpPrfxNumLocRibRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPrfxNumLocRibRoutes.setStatus("current")
_BgpRib_ObjectIdentity = ObjectIdentity
bgpRib = _BgpRib_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4)
)
_BgpNlriTable_Object = MibTable
bgpNlriTable = _BgpNlriTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1)
)
if mibBuilder.loadTexts:
    bgpNlriTable.setStatus("current")
_BgpNlriEntry_Object = MibTableRow
bgpNlriEntry = _BgpNlriEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1)
)
bgpNlriEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpNlriPeerOrAfm"),
    (0, "DC-BGP-MIB", "bgpNlriPeerAfmIndex"),
    (0, "DC-BGP-MIB", "bgpNlriAfi"),
    (0, "DC-BGP-MIB", "bgpNlriSafi"),
    (0, "DC-BGP-MIB", "bgpNlriPrfx"),
    (0, "DC-BGP-MIB", "bgpNlriPrfxLen"),
)
if mibBuilder.loadTexts:
    bgpNlriEntry.setStatus("current")
_BgpNlriPeerOrAfm_Type = BgpPeerOrAfm
_BgpNlriPeerOrAfm_Object = MibTableColumn
bgpNlriPeerOrAfm = _BgpNlriPeerOrAfm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 2),
    _BgpNlriPeerOrAfm_Type()
)
bgpNlriPeerOrAfm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPeerOrAfm.setStatus("current")
_BgpNlriPeerAfmIndex_Type = Unsigned32
_BgpNlriPeerAfmIndex_Object = MibTableColumn
bgpNlriPeerAfmIndex = _BgpNlriPeerAfmIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 3),
    _BgpNlriPeerAfmIndex_Type()
)
bgpNlriPeerAfmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPeerAfmIndex.setStatus("current")
_BgpNlriAfi_Type = BgpAfi
_BgpNlriAfi_Object = MibTableColumn
bgpNlriAfi = _BgpNlriAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 4),
    _BgpNlriAfi_Type()
)
bgpNlriAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriAfi.setStatus("current")
_BgpNlriSafi_Type = BgpSafi
_BgpNlriSafi_Object = MibTableColumn
bgpNlriSafi = _BgpNlriSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 5),
    _BgpNlriSafi_Type()
)
bgpNlriSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriSafi.setStatus("current")


class _BgpNlriPrfx_Type(InetAddress):
    """Custom type bgpNlriPrfx based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpNlriPrfx_Type.__name__ = "InetAddress"
_BgpNlriPrfx_Object = MibTableColumn
bgpNlriPrfx = _BgpNlriPrfx_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 6),
    _BgpNlriPrfx_Type()
)
bgpNlriPrfx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPrfx.setStatus("current")
_BgpNlriPrfxLen_Type = InetAddressPrefixLength
_BgpNlriPrfxLen_Object = MibTableColumn
bgpNlriPrfxLen = _BgpNlriPrfxLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 7),
    _BgpNlriPrfxLen_Type()
)
bgpNlriPrfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPrfxLen.setStatus("current")
_BgpNlriBest_Type = TruthValue
_BgpNlriBest_Object = MibTableColumn
bgpNlriBest = _BgpNlriBest_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 8),
    _BgpNlriBest_Type()
)
bgpNlriBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriBest.setStatus("current")
_BgpNlriAsSize_Type = BgpAsSize
_BgpNlriAsSize_Object = MibTableColumn
bgpNlriAsSize = _BgpNlriAsSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 9),
    _BgpNlriAsSize_Type()
)
bgpNlriAsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriAsSize.setStatus("current")


class _BgpNlriASPathStr_Type(OctetString):
    """Custom type bgpNlriASPathStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BgpNlriASPathStr_Type.__name__ = "OctetString"
_BgpNlriASPathStr_Object = MibTableColumn
bgpNlriASPathStr = _BgpNlriASPathStr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 10),
    _BgpNlriASPathStr_Type()
)
bgpNlriASPathStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriASPathStr.setStatus("current")
_BgpPathAttrOrigin_Type = BgpOriginCode
_BgpPathAttrOrigin_Object = MibTableColumn
bgpPathAttrOrigin = _BgpPathAttrOrigin_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 11),
    _BgpPathAttrOrigin_Type()
)
bgpPathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrOrigin.setStatus("current")


class _BgpPathAttrNextHop_Type(InetAddress):
    """Custom type bgpPathAttrNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpPathAttrNextHop_Type.__name__ = "InetAddress"
_BgpPathAttrNextHop_Object = MibTableColumn
bgpPathAttrNextHop = _BgpPathAttrNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 12),
    _BgpPathAttrNextHop_Type()
)
bgpPathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrNextHop.setStatus("current")
_BgpPathAttrMultiExitDisc_Type = Unsigned32
_BgpPathAttrMultiExitDisc_Object = MibTableColumn
bgpPathAttrMultiExitDisc = _BgpPathAttrMultiExitDisc_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 13),
    _BgpPathAttrMultiExitDisc_Type()
)
bgpPathAttrMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrMultiExitDisc.setStatus("current")
_BgpPathAttrLocalPref_Type = Unsigned32
_BgpPathAttrLocalPref_Object = MibTableColumn
bgpPathAttrLocalPref = _BgpPathAttrLocalPref_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 14),
    _BgpPathAttrLocalPref_Type()
)
bgpPathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrLocalPref.setStatus("current")
_BgpPathAttrAtomicAggregate_Type = BgpPathAttrAtomicAggPresence
_BgpPathAttrAtomicAggregate_Object = MibTableColumn
bgpPathAttrAtomicAggregate = _BgpPathAttrAtomicAggregate_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 15),
    _BgpPathAttrAtomicAggregate_Type()
)
bgpPathAttrAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrAtomicAggregate.setStatus("current")
_BgpPathAttrAggregatorAS_Type = BgpAutonomousSystemNumber
_BgpPathAttrAggregatorAS_Object = MibTableColumn
bgpPathAttrAggregatorAS = _BgpPathAttrAggregatorAS_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 16),
    _BgpPathAttrAggregatorAS_Type()
)
bgpPathAttrAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrAggregatorAS.setStatus("current")
_BgpPathAttrAggregatorAddr_Type = BgpIdentifier
_BgpPathAttrAggregatorAddr_Object = MibTableColumn
bgpPathAttrAggregatorAddr = _BgpPathAttrAggregatorAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 17),
    _BgpPathAttrAggregatorAddr_Type()
)
bgpPathAttrAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrAggregatorAddr.setStatus("current")
_BgpPathAttrCalcLocalPref_Type = Unsigned32
_BgpPathAttrCalcLocalPref_Object = MibTableColumn
bgpPathAttrCalcLocalPref = _BgpPathAttrCalcLocalPref_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 18),
    _BgpPathAttrCalcLocalPref_Type()
)
bgpPathAttrCalcLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrCalcLocalPref.setStatus("current")
_BgpPathAttrOrigId_Type = BgpIdentifier
_BgpPathAttrOrigId_Object = MibTableColumn
bgpPathAttrOrigId = _BgpPathAttrOrigId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 19),
    _BgpPathAttrOrigId_Type()
)
bgpPathAttrOrigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrOrigId.setStatus("current")
_BgpPathAttrWeight_Type = Unsigned32
_BgpPathAttrWeight_Object = MibTableColumn
bgpPathAttrWeight = _BgpPathAttrWeight_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 20),
    _BgpPathAttrWeight_Type()
)
bgpPathAttrWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrWeight.setStatus("current")
_BgpFlapStatsConfig_Type = Unsigned32
_BgpFlapStatsConfig_Object = MibTableColumn
bgpFlapStatsConfig = _BgpFlapStatsConfig_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 21),
    _BgpFlapStatsConfig_Type()
)
bgpFlapStatsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpFlapStatsConfig.setStatus("current")
_BgpFlapStatsPenalty_Type = Unsigned32
_BgpFlapStatsPenalty_Object = MibTableColumn
bgpFlapStatsPenalty = _BgpFlapStatsPenalty_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 22),
    _BgpFlapStatsPenalty_Type()
)
bgpFlapStatsPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpFlapStatsPenalty.setStatus("current")
_BgpFlapStatsFlapcnt_Type = Unsigned32
_BgpFlapStatsFlapcnt_Object = MibTableColumn
bgpFlapStatsFlapcnt = _BgpFlapStatsFlapcnt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 23),
    _BgpFlapStatsFlapcnt_Type()
)
bgpFlapStatsFlapcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpFlapStatsFlapcnt.setStatus("current")
_BgpFlapStatsSupprsd_Type = TruthValue
_BgpFlapStatsSupprsd_Object = MibTableColumn
bgpFlapStatsSupprsd = _BgpFlapStatsSupprsd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 24),
    _BgpFlapStatsSupprsd_Type()
)
bgpFlapStatsSupprsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpFlapStatsSupprsd.setStatus("current")
_BgpFlapStatsTimeleft_Type = Unsigned32
_BgpFlapStatsTimeleft_Object = MibTableColumn
bgpFlapStatsTimeleft = _BgpFlapStatsTimeleft_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 25),
    _BgpFlapStatsTimeleft_Type()
)
bgpFlapStatsTimeleft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpFlapStatsTimeleft.setStatus("current")
if mibBuilder.loadTexts:
    bgpFlapStatsTimeleft.setUnits("seconds")


class _BgpFlapStatsCleardamp_Type(TruthValue):
    """Custom type bgpFlapStatsCleardamp based on TruthValue"""


_BgpFlapStatsCleardamp_Object = MibTableColumn
bgpFlapStatsCleardamp = _BgpFlapStatsCleardamp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 26),
    _BgpFlapStatsCleardamp_Type()
)
bgpFlapStatsCleardamp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpFlapStatsCleardamp.setStatus("current")


class _BgpFlapStatsClearstat_Type(TruthValue):
    """Custom type bgpFlapStatsClearstat based on TruthValue"""


_BgpFlapStatsClearstat_Object = MibTableColumn
bgpFlapStatsClearstat = _BgpFlapStatsClearstat_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 27),
    _BgpFlapStatsClearstat_Type()
)
bgpFlapStatsClearstat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpFlapStatsClearstat.setStatus("current")
_BgpNlriEcmp_Type = TruthValue
_BgpNlriEcmp_Object = MibTableColumn
bgpNlriEcmp = _BgpNlriEcmp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 28),
    _BgpNlriEcmp_Type()
)
bgpNlriEcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriEcmp.setStatus("current")
_BgpPathAttrAsPathLimAs_Type = BgpAutonomousSystemNumber
_BgpPathAttrAsPathLimAs_Object = MibTableColumn
bgpPathAttrAsPathLimAs = _BgpPathAttrAsPathLimAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 29),
    _BgpPathAttrAsPathLimAs_Type()
)
bgpPathAttrAsPathLimAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrAsPathLimAs.setStatus("current")


class _BgpPathAttrAsPathLimUpper_Type(Unsigned32):
    """Custom type bgpPathAttrAsPathLimUpper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpPathAttrAsPathLimUpper_Type.__name__ = "Unsigned32"
_BgpPathAttrAsPathLimUpper_Object = MibTableColumn
bgpPathAttrAsPathLimUpper = _BgpPathAttrAsPathLimUpper_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 30),
    _BgpPathAttrAsPathLimUpper_Type()
)
bgpPathAttrAsPathLimUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrAsPathLimUpper.setStatus("current")
_BgpNlriIsActive_Type = BgpNlriIsActiveFlag
_BgpNlriIsActive_Object = MibTableColumn
bgpNlriIsActive = _BgpNlriIsActive_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 31),
    _BgpNlriIsActive_Type()
)
bgpNlriIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriIsActive.setStatus("current")


class _BgpNlriUserData_Type(OctetString):
    """Custom type bgpNlriUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BgpNlriUserData_Type.__name__ = "OctetString"
_BgpNlriUserData_Object = MibTableColumn
bgpNlriUserData = _BgpNlriUserData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 32),
    _BgpNlriUserData_Type()
)
bgpNlriUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriUserData.setStatus("current")
_BgpNlriStale_Type = TruthValue
_BgpNlriStale_Object = MibTableColumn
bgpNlriStale = _BgpNlriStale_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 33),
    _BgpNlriStale_Type()
)
bgpNlriStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriStale.setStatus("current")
_BgpNlriFlapStartTime_Type = TimeStamp
_BgpNlriFlapStartTime_Object = MibTableColumn
bgpNlriFlapStartTime = _BgpNlriFlapStartTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 34),
    _BgpNlriFlapStartTime_Type()
)
bgpNlriFlapStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriFlapStartTime.setStatus("current")


class _BgpNlriLinkLocalNextHop_Type(InetAddress):
    """Custom type bgpNlriLinkLocalNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpNlriLinkLocalNextHop_Type.__name__ = "InetAddress"
_BgpNlriLinkLocalNextHop_Object = MibTableColumn
bgpNlriLinkLocalNextHop = _BgpNlriLinkLocalNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 1, 1, 35),
    _BgpNlriLinkLocalNextHop_Type()
)
bgpNlriLinkLocalNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriLinkLocalNextHop.setStatus("current")
_BgpPathAttrUnknownTable_Object = MibTable
bgpPathAttrUnknownTable = _BgpPathAttrUnknownTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 2)
)
if mibBuilder.loadTexts:
    bgpPathAttrUnknownTable.setStatus("current")
_BgpPathAttrUnknownEntry_Object = MibTableRow
bgpPathAttrUnknownEntry = _BgpPathAttrUnknownEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 2, 1)
)
bgpPathAttrUnknownEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpNlriPeerOrAfm"),
    (0, "DC-BGP-MIB", "bgpNlriPeerAfmIndex"),
    (0, "DC-BGP-MIB", "bgpNlriAfi"),
    (0, "DC-BGP-MIB", "bgpNlriSafi"),
    (0, "DC-BGP-MIB", "bgpNlriPrfx"),
    (0, "DC-BGP-MIB", "bgpNlriPrfxLen"),
    (0, "DC-BGP-MIB", "bgpPathAttrUnknownType"),
)
if mibBuilder.loadTexts:
    bgpPathAttrUnknownEntry.setStatus("current")
_BgpPathAttrUnknownType_Type = Unsigned32
_BgpPathAttrUnknownType_Object = MibTableColumn
bgpPathAttrUnknownType = _BgpPathAttrUnknownType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 2, 1, 8),
    _BgpPathAttrUnknownType_Type()
)
bgpPathAttrUnknownType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPathAttrUnknownType.setStatus("current")


class _BgpPathAttrUnknownValue_Type(OctetString):
    """Custom type bgpPathAttrUnknownValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BgpPathAttrUnknownValue_Type.__name__ = "OctetString"
_BgpPathAttrUnknownValue_Object = MibTableColumn
bgpPathAttrUnknownValue = _BgpPathAttrUnknownValue_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 2, 1, 9),
    _BgpPathAttrUnknownValue_Type()
)
bgpPathAttrUnknownValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrUnknownValue.setStatus("current")


class _BgpPathAttrUnknownUserData_Type(OctetString):
    """Custom type bgpPathAttrUnknownUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BgpPathAttrUnknownUserData_Type.__name__ = "OctetString"
_BgpPathAttrUnknownUserData_Object = MibTableColumn
bgpPathAttrUnknownUserData = _BgpPathAttrUnknownUserData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 2, 1, 10),
    _BgpPathAttrUnknownUserData_Type()
)
bgpPathAttrUnknownUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrUnknownUserData.setStatus("current")
_BgpPathAttrExtensions_ObjectIdentity = ObjectIdentity
bgpPathAttrExtensions = _BgpPathAttrExtensions_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3)
)
_BgpPathAttrNonCapExts_ObjectIdentity = ObjectIdentity
bgpPathAttrNonCapExts = _BgpPathAttrNonCapExts_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1)
)
_BgpPathAttrRouteReflectionExts_ObjectIdentity = ObjectIdentity
bgpPathAttrRouteReflectionExts = _BgpPathAttrRouteReflectionExts_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1966)
)
_BgpPathAttrClusterTable_Object = MibTable
bgpPathAttrClusterTable = _BgpPathAttrClusterTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1966, 2)
)
if mibBuilder.loadTexts:
    bgpPathAttrClusterTable.setStatus("current")
_BgpPathAttrClusterEntry_Object = MibTableRow
bgpPathAttrClusterEntry = _BgpPathAttrClusterEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1966, 2, 1)
)
bgpPathAttrClusterEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpNlriPeerOrAfm"),
    (0, "DC-BGP-MIB", "bgpNlriPeerAfmIndex"),
    (0, "DC-BGP-MIB", "bgpNlriAfi"),
    (0, "DC-BGP-MIB", "bgpNlriSafi"),
    (0, "DC-BGP-MIB", "bgpNlriPrfx"),
    (0, "DC-BGP-MIB", "bgpNlriPrfxLen"),
    (0, "DC-BGP-MIB", "bgpPathAttrClusterIndex"),
)
if mibBuilder.loadTexts:
    bgpPathAttrClusterEntry.setStatus("current")
_BgpPathAttrClusterIndex_Type = Unsigned32
_BgpPathAttrClusterIndex_Object = MibTableColumn
bgpPathAttrClusterIndex = _BgpPathAttrClusterIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1966, 2, 1, 8),
    _BgpPathAttrClusterIndex_Type()
)
bgpPathAttrClusterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPathAttrClusterIndex.setStatus("current")
_BgpPathAttrClusterValue_Type = Unsigned32
_BgpPathAttrClusterValue_Object = MibTableColumn
bgpPathAttrClusterValue = _BgpPathAttrClusterValue_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1966, 2, 1, 9),
    _BgpPathAttrClusterValue_Type()
)
bgpPathAttrClusterValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrClusterValue.setStatus("current")


class _BgpPathAttrClusterUserData_Type(OctetString):
    """Custom type bgpPathAttrClusterUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BgpPathAttrClusterUserData_Type.__name__ = "OctetString"
_BgpPathAttrClusterUserData_Object = MibTableColumn
bgpPathAttrClusterUserData = _BgpPathAttrClusterUserData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1966, 2, 1, 10),
    _BgpPathAttrClusterUserData_Type()
)
bgpPathAttrClusterUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrClusterUserData.setStatus("current")
_BgpPathAttrCommunityExts_ObjectIdentity = ObjectIdentity
bgpPathAttrCommunityExts = _BgpPathAttrCommunityExts_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1997)
)
_BgpPathAttrCommTable_Object = MibTable
bgpPathAttrCommTable = _BgpPathAttrCommTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1997, 1)
)
if mibBuilder.loadTexts:
    bgpPathAttrCommTable.setStatus("current")
_BgpPathAttrCommEntry_Object = MibTableRow
bgpPathAttrCommEntry = _BgpPathAttrCommEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1997, 1, 1)
)
bgpPathAttrCommEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpNlriPeerOrAfm"),
    (0, "DC-BGP-MIB", "bgpNlriPeerAfmIndex"),
    (0, "DC-BGP-MIB", "bgpNlriAfi"),
    (0, "DC-BGP-MIB", "bgpNlriSafi"),
    (0, "DC-BGP-MIB", "bgpNlriPrfx"),
    (0, "DC-BGP-MIB", "bgpNlriPrfxLen"),
    (0, "DC-BGP-MIB", "bgpPathAttrCommIndex"),
)
if mibBuilder.loadTexts:
    bgpPathAttrCommEntry.setStatus("current")
_BgpPathAttrCommIndex_Type = Unsigned32
_BgpPathAttrCommIndex_Object = MibTableColumn
bgpPathAttrCommIndex = _BgpPathAttrCommIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1997, 1, 1, 8),
    _BgpPathAttrCommIndex_Type()
)
bgpPathAttrCommIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPathAttrCommIndex.setStatus("current")
_BgpPathAttrCommValue_Type = BgpCommunity
_BgpPathAttrCommValue_Object = MibTableColumn
bgpPathAttrCommValue = _BgpPathAttrCommValue_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1997, 1, 1, 9),
    _BgpPathAttrCommValue_Type()
)
bgpPathAttrCommValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrCommValue.setStatus("current")


class _BgpPathAttrCommUserData_Type(OctetString):
    """Custom type bgpPathAttrCommUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BgpPathAttrCommUserData_Type.__name__ = "OctetString"
_BgpPathAttrCommUserData_Object = MibTableColumn
bgpPathAttrCommUserData = _BgpPathAttrCommUserData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 1997, 1, 1, 10),
    _BgpPathAttrCommUserData_Type()
)
bgpPathAttrCommUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrCommUserData.setStatus("current")
_BgpPathAttrExtCommunityExts_ObjectIdentity = ObjectIdentity
bgpPathAttrExtCommunityExts = _BgpPathAttrExtCommunityExts_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 2547)
)
_BgpPathAttrExtCommTable_Object = MibTable
bgpPathAttrExtCommTable = _BgpPathAttrExtCommTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 2547, 1)
)
if mibBuilder.loadTexts:
    bgpPathAttrExtCommTable.setStatus("current")
_BgpPathAttrExtCommEntry_Object = MibTableRow
bgpPathAttrExtCommEntry = _BgpPathAttrExtCommEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 2547, 1, 1)
)
bgpPathAttrExtCommEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpNlriPeerOrAfm"),
    (0, "DC-BGP-MIB", "bgpNlriPeerAfmIndex"),
    (0, "DC-BGP-MIB", "bgpNlriAfi"),
    (0, "DC-BGP-MIB", "bgpNlriSafi"),
    (0, "DC-BGP-MIB", "bgpNlriPrfx"),
    (0, "DC-BGP-MIB", "bgpNlriPrfxLen"),
    (0, "DC-BGP-MIB", "bgpPathAttrExtCommIndex"),
)
if mibBuilder.loadTexts:
    bgpPathAttrExtCommEntry.setStatus("current")
_BgpPathAttrExtCommIndex_Type = Unsigned32
_BgpPathAttrExtCommIndex_Object = MibTableColumn
bgpPathAttrExtCommIndex = _BgpPathAttrExtCommIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 2547, 1, 1, 8),
    _BgpPathAttrExtCommIndex_Type()
)
bgpPathAttrExtCommIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPathAttrExtCommIndex.setStatus("current")
_BgpPathAttrExtCommValue_Type = BgpExtendedCommunity
_BgpPathAttrExtCommValue_Object = MibTableColumn
bgpPathAttrExtCommValue = _BgpPathAttrExtCommValue_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 2547, 1, 1, 9),
    _BgpPathAttrExtCommValue_Type()
)
bgpPathAttrExtCommValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrExtCommValue.setStatus("current")


class _BgpPathAttrExtCommUserData_Type(OctetString):
    """Custom type bgpPathAttrExtCommUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BgpPathAttrExtCommUserData_Type.__name__ = "OctetString"
_BgpPathAttrExtCommUserData_Object = MibTableColumn
bgpPathAttrExtCommUserData = _BgpPathAttrExtCommUserData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 1, 2547, 1, 1, 10),
    _BgpPathAttrExtCommUserData_Type()
)
bgpPathAttrExtCommUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpPathAttrExtCommUserData.setStatus("current")
_BgpPathAttrCapExts_ObjectIdentity = ObjectIdentity
bgpPathAttrCapExts = _BgpPathAttrCapExts_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 3, 2)
)
_BgpAdjRibOutTable_Object = MibTable
bgpAdjRibOutTable = _BgpAdjRibOutTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4)
)
if mibBuilder.loadTexts:
    bgpAdjRibOutTable.setStatus("current")
_BgpAdjRibOutEntry_Object = MibTableRow
bgpAdjRibOutEntry = _BgpAdjRibOutEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1)
)
bgpAdjRibOutEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpPeerIndex"),
    (0, "DC-BGP-MIB", "bgpAdjRibOutAfi"),
    (0, "DC-BGP-MIB", "bgpAdjRibOutSafi"),
    (0, "DC-BGP-MIB", "bgpAdjRibOutPrfx"),
    (0, "DC-BGP-MIB", "bgpAdjRibOutPrfxLen"),
)
if mibBuilder.loadTexts:
    bgpAdjRibOutEntry.setStatus("current")
_BgpAdjRibOutAfi_Type = BgpAfi
_BgpAdjRibOutAfi_Object = MibTableColumn
bgpAdjRibOutAfi = _BgpAdjRibOutAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 3),
    _BgpAdjRibOutAfi_Type()
)
bgpAdjRibOutAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAdjRibOutAfi.setStatus("current")
_BgpAdjRibOutSafi_Type = BgpSafi
_BgpAdjRibOutSafi_Object = MibTableColumn
bgpAdjRibOutSafi = _BgpAdjRibOutSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 4),
    _BgpAdjRibOutSafi_Type()
)
bgpAdjRibOutSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAdjRibOutSafi.setStatus("current")


class _BgpAdjRibOutPrfx_Type(InetAddress):
    """Custom type bgpAdjRibOutPrfx based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpAdjRibOutPrfx_Type.__name__ = "InetAddress"
_BgpAdjRibOutPrfx_Object = MibTableColumn
bgpAdjRibOutPrfx = _BgpAdjRibOutPrfx_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 5),
    _BgpAdjRibOutPrfx_Type()
)
bgpAdjRibOutPrfx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAdjRibOutPrfx.setStatus("current")
_BgpAdjRibOutPrfxLen_Type = InetAddressPrefixLength
_BgpAdjRibOutPrfxLen_Object = MibTableColumn
bgpAdjRibOutPrfxLen = _BgpAdjRibOutPrfxLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 6),
    _BgpAdjRibOutPrfxLen_Type()
)
bgpAdjRibOutPrfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAdjRibOutPrfxLen.setStatus("current")


class _BgpAdjRibOutAdvertStatus_Type(Integer32):
    """Custom type bgpAdjRibOutAdvertStatus based on Integer32"""
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
        *(("advertised", 1),
          ("pendingWithdrawal", 3),
          ("suppressed", 2),
          ("withdrawn", 4))
    )


_BgpAdjRibOutAdvertStatus_Type.__name__ = "Integer32"
_BgpAdjRibOutAdvertStatus_Object = MibTableColumn
bgpAdjRibOutAdvertStatus = _BgpAdjRibOutAdvertStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 7),
    _BgpAdjRibOutAdvertStatus_Type()
)
bgpAdjRibOutAdvertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutAdvertStatus.setStatus("current")


class _BgpAdjRibOutLocalAggrType_Type(Integer32):
    """Custom type bgpAdjRibOutLocalAggrType based on Integer32"""
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
        *(("aggregateRoute", 2),
          ("noAggregation", 1),
          ("suppressedAggregatedRoute", 4),
          ("unsuppAggregatedRoute", 3))
    )


_BgpAdjRibOutLocalAggrType_Type.__name__ = "Integer32"
_BgpAdjRibOutLocalAggrType_Object = MibTableColumn
bgpAdjRibOutLocalAggrType = _BgpAdjRibOutLocalAggrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 8),
    _BgpAdjRibOutLocalAggrType_Type()
)
bgpAdjRibOutLocalAggrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutLocalAggrType.setStatus("current")
_BgpAdjRibOutAsSize_Type = BgpAsSize
_BgpAdjRibOutAsSize_Object = MibTableColumn
bgpAdjRibOutAsSize = _BgpAdjRibOutAsSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 9),
    _BgpAdjRibOutAsSize_Type()
)
bgpAdjRibOutAsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutAsSize.setStatus("current")


class _BgpAdjRibOutASPathStr_Type(OctetString):
    """Custom type bgpAdjRibOutASPathStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BgpAdjRibOutASPathStr_Type.__name__ = "OctetString"
_BgpAdjRibOutASPathStr_Object = MibTableColumn
bgpAdjRibOutASPathStr = _BgpAdjRibOutASPathStr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 10),
    _BgpAdjRibOutASPathStr_Type()
)
bgpAdjRibOutASPathStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutASPathStr.setStatus("current")
_BgpAdjRibOutOrigin_Type = BgpOriginCode
_BgpAdjRibOutOrigin_Object = MibTableColumn
bgpAdjRibOutOrigin = _BgpAdjRibOutOrigin_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 11),
    _BgpAdjRibOutOrigin_Type()
)
bgpAdjRibOutOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutOrigin.setStatus("current")


class _BgpAdjRibOutNextHop_Type(InetAddress):
    """Custom type bgpAdjRibOutNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpAdjRibOutNextHop_Type.__name__ = "InetAddress"
_BgpAdjRibOutNextHop_Object = MibTableColumn
bgpAdjRibOutNextHop = _BgpAdjRibOutNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 12),
    _BgpAdjRibOutNextHop_Type()
)
bgpAdjRibOutNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutNextHop.setStatus("current")
_BgpAdjRibOutMultiExitDisc_Type = Unsigned32
_BgpAdjRibOutMultiExitDisc_Object = MibTableColumn
bgpAdjRibOutMultiExitDisc = _BgpAdjRibOutMultiExitDisc_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 13),
    _BgpAdjRibOutMultiExitDisc_Type()
)
bgpAdjRibOutMultiExitDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutMultiExitDisc.setStatus("current")
_BgpAdjRibOutLocalPref_Type = Unsigned32
_BgpAdjRibOutLocalPref_Object = MibTableColumn
bgpAdjRibOutLocalPref = _BgpAdjRibOutLocalPref_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 14),
    _BgpAdjRibOutLocalPref_Type()
)
bgpAdjRibOutLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutLocalPref.setStatus("current")
_BgpAdjRibOutAtomicAggregate_Type = BgpPathAttrAtomicAggPresence
_BgpAdjRibOutAtomicAggregate_Object = MibTableColumn
bgpAdjRibOutAtomicAggregate = _BgpAdjRibOutAtomicAggregate_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 15),
    _BgpAdjRibOutAtomicAggregate_Type()
)
bgpAdjRibOutAtomicAggregate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutAtomicAggregate.setStatus("current")
_BgpAdjRibOutAggregatorAS_Type = BgpAutonomousSystemNumber
_BgpAdjRibOutAggregatorAS_Object = MibTableColumn
bgpAdjRibOutAggregatorAS = _BgpAdjRibOutAggregatorAS_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 16),
    _BgpAdjRibOutAggregatorAS_Type()
)
bgpAdjRibOutAggregatorAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutAggregatorAS.setStatus("current")
_BgpAdjRibOutAggregatorAddr_Type = BgpIdentifier
_BgpAdjRibOutAggregatorAddr_Object = MibTableColumn
bgpAdjRibOutAggregatorAddr = _BgpAdjRibOutAggregatorAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 17),
    _BgpAdjRibOutAggregatorAddr_Type()
)
bgpAdjRibOutAggregatorAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutAggregatorAddr.setStatus("current")
_BgpAdjRibOutOrigId_Type = BgpIdentifier
_BgpAdjRibOutOrigId_Object = MibTableColumn
bgpAdjRibOutOrigId = _BgpAdjRibOutOrigId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 18),
    _BgpAdjRibOutOrigId_Type()
)
bgpAdjRibOutOrigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutOrigId.setStatus("current")
_BgpAdjRibOutAsLimAs_Type = BgpAutonomousSystemNumber
_BgpAdjRibOutAsLimAs_Object = MibTableColumn
bgpAdjRibOutAsLimAs = _BgpAdjRibOutAsLimAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 19),
    _BgpAdjRibOutAsLimAs_Type()
)
bgpAdjRibOutAsLimAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutAsLimAs.setStatus("current")


class _BgpAdjRibOutAsLimUpper_Type(Unsigned32):
    """Custom type bgpAdjRibOutAsLimUpper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpAdjRibOutAsLimUpper_Type.__name__ = "Unsigned32"
_BgpAdjRibOutAsLimUpper_Object = MibTableColumn
bgpAdjRibOutAsLimUpper = _BgpAdjRibOutAsLimUpper_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 20),
    _BgpAdjRibOutAsLimUpper_Type()
)
bgpAdjRibOutAsLimUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutAsLimUpper.setStatus("current")


class _BgpAdjRibOutUserData_Type(OctetString):
    """Custom type bgpAdjRibOutUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BgpAdjRibOutUserData_Type.__name__ = "OctetString"
_BgpAdjRibOutUserData_Object = MibTableColumn
bgpAdjRibOutUserData = _BgpAdjRibOutUserData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 21),
    _BgpAdjRibOutUserData_Type()
)
bgpAdjRibOutUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutUserData.setStatus("current")
_BgpAdjRibOutEcmp_Type = TruthValue
_BgpAdjRibOutEcmp_Object = MibTableColumn
bgpAdjRibOutEcmp = _BgpAdjRibOutEcmp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 22),
    _BgpAdjRibOutEcmp_Type()
)
bgpAdjRibOutEcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutEcmp.setStatus("current")
_BgpAdjRibOutStale_Type = TruthValue
_BgpAdjRibOutStale_Object = MibTableColumn
bgpAdjRibOutStale = _BgpAdjRibOutStale_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 23),
    _BgpAdjRibOutStale_Type()
)
bgpAdjRibOutStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutStale.setStatus("current")


class _BgpAdjRibOutLinkLocalNextHop_Type(InetAddress):
    """Custom type bgpAdjRibOutLinkLocalNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpAdjRibOutLinkLocalNextHop_Type.__name__ = "InetAddress"
_BgpAdjRibOutLinkLocalNextHop_Object = MibTableColumn
bgpAdjRibOutLinkLocalNextHop = _BgpAdjRibOutLinkLocalNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 4, 1, 24),
    _BgpAdjRibOutLinkLocalNextHop_Type()
)
bgpAdjRibOutLinkLocalNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpAdjRibOutLinkLocalNextHop.setStatus("current")
_BgpNlriPrefixTable_Object = MibTable
bgpNlriPrefixTable = _BgpNlriPrefixTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5)
)
if mibBuilder.loadTexts:
    bgpNlriPrefixTable.setStatus("current")
_BgpNlriPrefixEntry_Object = MibTableRow
bgpNlriPrefixEntry = _BgpNlriPrefixEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1)
)
bgpNlriPrefixEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpNlriPrefixAfi"),
    (0, "DC-BGP-MIB", "bgpNlriPrefixSafi"),
    (0, "DC-BGP-MIB", "bgpNlriPrefixPrfx"),
    (0, "DC-BGP-MIB", "bgpNlriPrefixPrfxLen"),
    (0, "DC-BGP-MIB", "bgpNlriPrefixPeerOrAfm"),
    (0, "DC-BGP-MIB", "bgpNlriPrefixPeerAfmIndex"),
)
if mibBuilder.loadTexts:
    bgpNlriPrefixEntry.setStatus("current")
_BgpNlriPrefixPeerOrAfm_Type = BgpPeerOrAfm
_BgpNlriPrefixPeerOrAfm_Object = MibTableColumn
bgpNlriPrefixPeerOrAfm = _BgpNlriPrefixPeerOrAfm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 2),
    _BgpNlriPrefixPeerOrAfm_Type()
)
bgpNlriPrefixPeerOrAfm.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPrefixPeerOrAfm.setStatus("current")
_BgpNlriPrefixPeerAfmIndex_Type = Unsigned32
_BgpNlriPrefixPeerAfmIndex_Object = MibTableColumn
bgpNlriPrefixPeerAfmIndex = _BgpNlriPrefixPeerAfmIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 3),
    _BgpNlriPrefixPeerAfmIndex_Type()
)
bgpNlriPrefixPeerAfmIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPrefixPeerAfmIndex.setStatus("current")
_BgpNlriPrefixAfi_Type = BgpAfi
_BgpNlriPrefixAfi_Object = MibTableColumn
bgpNlriPrefixAfi = _BgpNlriPrefixAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 4),
    _BgpNlriPrefixAfi_Type()
)
bgpNlriPrefixAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPrefixAfi.setStatus("current")
_BgpNlriPrefixSafi_Type = BgpSafi
_BgpNlriPrefixSafi_Object = MibTableColumn
bgpNlriPrefixSafi = _BgpNlriPrefixSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 5),
    _BgpNlriPrefixSafi_Type()
)
bgpNlriPrefixSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPrefixSafi.setStatus("current")


class _BgpNlriPrefixPrfx_Type(InetAddress):
    """Custom type bgpNlriPrefixPrfx based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpNlriPrefixPrfx_Type.__name__ = "InetAddress"
_BgpNlriPrefixPrfx_Object = MibTableColumn
bgpNlriPrefixPrfx = _BgpNlriPrefixPrfx_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 6),
    _BgpNlriPrefixPrfx_Type()
)
bgpNlriPrefixPrfx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPrefixPrfx.setStatus("current")
_BgpNlriPrefixPrfxLen_Type = InetAddressPrefixLength
_BgpNlriPrefixPrfxLen_Object = MibTableColumn
bgpNlriPrefixPrfxLen = _BgpNlriPrefixPrfxLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 7),
    _BgpNlriPrefixPrfxLen_Type()
)
bgpNlriPrefixPrfxLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNlriPrefixPrfxLen.setStatus("current")
_BgpNlriPrefixBest_Type = TruthValue
_BgpNlriPrefixBest_Object = MibTableColumn
bgpNlriPrefixBest = _BgpNlriPrefixBest_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 8),
    _BgpNlriPrefixBest_Type()
)
bgpNlriPrefixBest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixBest.setStatus("current")
_BgpNlriPrefixAsSize_Type = BgpAsSize
_BgpNlriPrefixAsSize_Object = MibTableColumn
bgpNlriPrefixAsSize = _BgpNlriPrefixAsSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 9),
    _BgpNlriPrefixAsSize_Type()
)
bgpNlriPrefixAsSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixAsSize.setStatus("current")


class _BgpNlriPrefixASPathStr_Type(OctetString):
    """Custom type bgpNlriPrefixASPathStr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BgpNlriPrefixASPathStr_Type.__name__ = "OctetString"
_BgpNlriPrefixASPathStr_Object = MibTableColumn
bgpNlriPrefixASPathStr = _BgpNlriPrefixASPathStr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 10),
    _BgpNlriPrefixASPathStr_Type()
)
bgpNlriPrefixASPathStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixASPathStr.setStatus("current")
_BgpNlriPrefixPathAttrOrigin_Type = BgpOriginCode
_BgpNlriPrefixPathAttrOrigin_Object = MibTableColumn
bgpNlriPrefixPathAttrOrigin = _BgpNlriPrefixPathAttrOrigin_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 11),
    _BgpNlriPrefixPathAttrOrigin_Type()
)
bgpNlriPrefixPathAttrOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrOrigin.setStatus("current")


class _BgpNlriPrefixPathAttrNextHop_Type(InetAddress):
    """Custom type bgpNlriPrefixPathAttrNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpNlriPrefixPathAttrNextHop_Type.__name__ = "InetAddress"
_BgpNlriPrefixPathAttrNextHop_Object = MibTableColumn
bgpNlriPrefixPathAttrNextHop = _BgpNlriPrefixPathAttrNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 12),
    _BgpNlriPrefixPathAttrNextHop_Type()
)
bgpNlriPrefixPathAttrNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrNextHop.setStatus("current")
_BgpNlriPrefixPathAttrMultExtDisc_Type = Unsigned32
_BgpNlriPrefixPathAttrMultExtDisc_Object = MibTableColumn
bgpNlriPrefixPathAttrMultExtDisc = _BgpNlriPrefixPathAttrMultExtDisc_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 13),
    _BgpNlriPrefixPathAttrMultExtDisc_Type()
)
bgpNlriPrefixPathAttrMultExtDisc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrMultExtDisc.setStatus("current")
_BgpNlriPrefixPathAttrLocalPref_Type = Unsigned32
_BgpNlriPrefixPathAttrLocalPref_Object = MibTableColumn
bgpNlriPrefixPathAttrLocalPref = _BgpNlriPrefixPathAttrLocalPref_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 14),
    _BgpNlriPrefixPathAttrLocalPref_Type()
)
bgpNlriPrefixPathAttrLocalPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrLocalPref.setStatus("current")
_BgpNlriPrefixPathAttrAtomicAgg_Type = BgpPathAttrAtomicAggPresence
_BgpNlriPrefixPathAttrAtomicAgg_Object = MibTableColumn
bgpNlriPrefixPathAttrAtomicAgg = _BgpNlriPrefixPathAttrAtomicAgg_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 15),
    _BgpNlriPrefixPathAttrAtomicAgg_Type()
)
bgpNlriPrefixPathAttrAtomicAgg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrAtomicAgg.setStatus("current")
_BgpNlriPrefixPathAttrAggAS_Type = BgpAutonomousSystemNumber
_BgpNlriPrefixPathAttrAggAS_Object = MibTableColumn
bgpNlriPrefixPathAttrAggAS = _BgpNlriPrefixPathAttrAggAS_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 16),
    _BgpNlriPrefixPathAttrAggAS_Type()
)
bgpNlriPrefixPathAttrAggAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrAggAS.setStatus("current")
_BgpNlriPrefixPathAttrAggAddr_Type = BgpIdentifier
_BgpNlriPrefixPathAttrAggAddr_Object = MibTableColumn
bgpNlriPrefixPathAttrAggAddr = _BgpNlriPrefixPathAttrAggAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 17),
    _BgpNlriPrefixPathAttrAggAddr_Type()
)
bgpNlriPrefixPathAttrAggAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrAggAddr.setStatus("current")
_BgpNlriPrefixPathAttrCalcLclPref_Type = Unsigned32
_BgpNlriPrefixPathAttrCalcLclPref_Object = MibTableColumn
bgpNlriPrefixPathAttrCalcLclPref = _BgpNlriPrefixPathAttrCalcLclPref_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 18),
    _BgpNlriPrefixPathAttrCalcLclPref_Type()
)
bgpNlriPrefixPathAttrCalcLclPref.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrCalcLclPref.setStatus("current")
_BgpNlriPrefixPathAttrOrigId_Type = BgpIdentifier
_BgpNlriPrefixPathAttrOrigId_Object = MibTableColumn
bgpNlriPrefixPathAttrOrigId = _BgpNlriPrefixPathAttrOrigId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 19),
    _BgpNlriPrefixPathAttrOrigId_Type()
)
bgpNlriPrefixPathAttrOrigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrOrigId.setStatus("current")
_BgpNlriPrefixPathAttrWeight_Type = Unsigned32
_BgpNlriPrefixPathAttrWeight_Object = MibTableColumn
bgpNlriPrefixPathAttrWeight = _BgpNlriPrefixPathAttrWeight_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 20),
    _BgpNlriPrefixPathAttrWeight_Type()
)
bgpNlriPrefixPathAttrWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrWeight.setStatus("current")
_BgpNlriPrefixFlapStatsConfig_Type = Unsigned32
_BgpNlriPrefixFlapStatsConfig_Object = MibTableColumn
bgpNlriPrefixFlapStatsConfig = _BgpNlriPrefixFlapStatsConfig_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 21),
    _BgpNlriPrefixFlapStatsConfig_Type()
)
bgpNlriPrefixFlapStatsConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixFlapStatsConfig.setStatus("current")
_BgpNlriPrefixFlapStatsPenalty_Type = Unsigned32
_BgpNlriPrefixFlapStatsPenalty_Object = MibTableColumn
bgpNlriPrefixFlapStatsPenalty = _BgpNlriPrefixFlapStatsPenalty_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 22),
    _BgpNlriPrefixFlapStatsPenalty_Type()
)
bgpNlriPrefixFlapStatsPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixFlapStatsPenalty.setStatus("current")
_BgpNlriPrefixFlapStatsFlapcnt_Type = Unsigned32
_BgpNlriPrefixFlapStatsFlapcnt_Object = MibTableColumn
bgpNlriPrefixFlapStatsFlapcnt = _BgpNlriPrefixFlapStatsFlapcnt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 23),
    _BgpNlriPrefixFlapStatsFlapcnt_Type()
)
bgpNlriPrefixFlapStatsFlapcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixFlapStatsFlapcnt.setStatus("current")
_BgpNlriPrefixFlapStatsSupprsd_Type = TruthValue
_BgpNlriPrefixFlapStatsSupprsd_Object = MibTableColumn
bgpNlriPrefixFlapStatsSupprsd = _BgpNlriPrefixFlapStatsSupprsd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 24),
    _BgpNlriPrefixFlapStatsSupprsd_Type()
)
bgpNlriPrefixFlapStatsSupprsd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixFlapStatsSupprsd.setStatus("current")
_BgpNlriPrefixFlapStatsTimeleft_Type = Unsigned32
_BgpNlriPrefixFlapStatsTimeleft_Object = MibTableColumn
bgpNlriPrefixFlapStatsTimeleft = _BgpNlriPrefixFlapStatsTimeleft_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 25),
    _BgpNlriPrefixFlapStatsTimeleft_Type()
)
bgpNlriPrefixFlapStatsTimeleft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixFlapStatsTimeleft.setStatus("current")
if mibBuilder.loadTexts:
    bgpNlriPrefixFlapStatsTimeleft.setUnits("seconds")


class _BgpNlriPrefixFlapStatsCleardamp_Type(TruthValue):
    """Custom type bgpNlriPrefixFlapStatsCleardamp based on TruthValue"""


_BgpNlriPrefixFlapStatsCleardamp_Object = MibTableColumn
bgpNlriPrefixFlapStatsCleardamp = _BgpNlriPrefixFlapStatsCleardamp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 26),
    _BgpNlriPrefixFlapStatsCleardamp_Type()
)
bgpNlriPrefixFlapStatsCleardamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixFlapStatsCleardamp.setStatus("current")


class _BgpNlriPrefixFlapStatsClearstat_Type(TruthValue):
    """Custom type bgpNlriPrefixFlapStatsClearstat based on TruthValue"""


_BgpNlriPrefixFlapStatsClearstat_Object = MibTableColumn
bgpNlriPrefixFlapStatsClearstat = _BgpNlriPrefixFlapStatsClearstat_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 27),
    _BgpNlriPrefixFlapStatsClearstat_Type()
)
bgpNlriPrefixFlapStatsClearstat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixFlapStatsClearstat.setStatus("current")
_BgpNlriPrefixEcmp_Type = TruthValue
_BgpNlriPrefixEcmp_Object = MibTableColumn
bgpNlriPrefixEcmp = _BgpNlriPrefixEcmp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 28),
    _BgpNlriPrefixEcmp_Type()
)
bgpNlriPrefixEcmp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixEcmp.setStatus("current")
_BgpNlriPrefixPathAttrAsPathLimAs_Type = BgpAutonomousSystemNumber
_BgpNlriPrefixPathAttrAsPathLimAs_Object = MibTableColumn
bgpNlriPrefixPathAttrAsPathLimAs = _BgpNlriPrefixPathAttrAsPathLimAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 29),
    _BgpNlriPrefixPathAttrAsPathLimAs_Type()
)
bgpNlriPrefixPathAttrAsPathLimAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPathAttrAsPathLimAs.setStatus("current")


class _BgpNlriPrefixPthAttAsPthLimUpper_Type(Unsigned32):
    """Custom type bgpNlriPrefixPthAttAsPthLimUpper based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpNlriPrefixPthAttAsPthLimUpper_Type.__name__ = "Unsigned32"
_BgpNlriPrefixPthAttAsPthLimUpper_Object = MibTableColumn
bgpNlriPrefixPthAttAsPthLimUpper = _BgpNlriPrefixPthAttAsPthLimUpper_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 30),
    _BgpNlriPrefixPthAttAsPthLimUpper_Type()
)
bgpNlriPrefixPthAttAsPthLimUpper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixPthAttAsPthLimUpper.setStatus("current")
_BgpNlriPrefixIsActive_Type = BgpNlriIsActiveFlag
_BgpNlriPrefixIsActive_Object = MibTableColumn
bgpNlriPrefixIsActive = _BgpNlriPrefixIsActive_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 31),
    _BgpNlriPrefixIsActive_Type()
)
bgpNlriPrefixIsActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixIsActive.setStatus("current")


class _BgpNlriPrefixUserData_Type(OctetString):
    """Custom type bgpNlriPrefixUserData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_BgpNlriPrefixUserData_Type.__name__ = "OctetString"
_BgpNlriPrefixUserData_Object = MibTableColumn
bgpNlriPrefixUserData = _BgpNlriPrefixUserData_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 32),
    _BgpNlriPrefixUserData_Type()
)
bgpNlriPrefixUserData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixUserData.setStatus("current")
_BgpNlriPrefixStale_Type = TruthValue
_BgpNlriPrefixStale_Object = MibTableColumn
bgpNlriPrefixStale = _BgpNlriPrefixStale_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 33),
    _BgpNlriPrefixStale_Type()
)
bgpNlriPrefixStale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixStale.setStatus("current")
_BgpNlriPrefixFlapStartTime_Type = TimeStamp
_BgpNlriPrefixFlapStartTime_Object = MibTableColumn
bgpNlriPrefixFlapStartTime = _BgpNlriPrefixFlapStartTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 34),
    _BgpNlriPrefixFlapStartTime_Type()
)
bgpNlriPrefixFlapStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixFlapStartTime.setStatus("current")


class _BgpNlriPrefixLinkLocalNextHop_Type(InetAddress):
    """Custom type bgpNlriPrefixLinkLocalNextHop based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpNlriPrefixLinkLocalNextHop_Type.__name__ = "InetAddress"
_BgpNlriPrefixLinkLocalNextHop_Object = MibTableColumn
bgpNlriPrefixLinkLocalNextHop = _BgpNlriPrefixLinkLocalNextHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 4, 5, 1, 35),
    _BgpNlriPrefixLinkLocalNextHop_Type()
)
bgpNlriPrefixLinkLocalNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNlriPrefixLinkLocalNextHop.setStatus("current")
_BgpPib_ObjectIdentity = ObjectIdentity
bgpPib = _BgpPib_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5)
)
_BgpRouteMapTable_Object = MibTable
bgpRouteMapTable = _BgpRouteMapTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1)
)
if mibBuilder.loadTexts:
    bgpRouteMapTable.setStatus("current")
_BgpRouteMapEntry_Object = MibTableRow
bgpRouteMapEntry = _BgpRouteMapEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1)
)
bgpRouteMapEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpRouteMapIndex"),
    (0, "DC-BGP-MIB", "bgpRouteMapNumber"),
)
if mibBuilder.loadTexts:
    bgpRouteMapEntry.setStatus("current")


class _BgpRouteMapIndex_Type(Unsigned32):
    """Custom type bgpRouteMapIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4278190079),
    )


_BgpRouteMapIndex_Type.__name__ = "Unsigned32"
_BgpRouteMapIndex_Object = MibTableColumn
bgpRouteMapIndex = _BgpRouteMapIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 2),
    _BgpRouteMapIndex_Type()
)
bgpRouteMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRouteMapIndex.setStatus("current")
_BgpRouteMapNumber_Type = Unsigned32
_BgpRouteMapNumber_Object = MibTableColumn
bgpRouteMapNumber = _BgpRouteMapNumber_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 3),
    _BgpRouteMapNumber_Type()
)
bgpRouteMapNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRouteMapNumber.setStatus("current")
_BgpRouteMapRowStatus_Type = RowStatus
_BgpRouteMapRowStatus_Object = MibTableColumn
bgpRouteMapRowStatus = _BgpRouteMapRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 4),
    _BgpRouteMapRowStatus_Type()
)
bgpRouteMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapRowStatus.setStatus("current")


class _BgpRouteMapMaAfi_Type(BgpAfi):
    """Custom type bgpRouteMapMaAfi based on BgpAfi"""


_BgpRouteMapMaAfi_Object = MibTableColumn
bgpRouteMapMaAfi = _BgpRouteMapMaAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 5),
    _BgpRouteMapMaAfi_Type()
)
bgpRouteMapMaAfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaAfi.setStatus("current")


class _BgpRouteMapMaAfiDef_Type(TruthValue):
    """Custom type bgpRouteMapMaAfiDef based on TruthValue"""


_BgpRouteMapMaAfiDef_Object = MibTableColumn
bgpRouteMapMaAfiDef = _BgpRouteMapMaAfiDef_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 6),
    _BgpRouteMapMaAfiDef_Type()
)
bgpRouteMapMaAfiDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaAfiDef.setStatus("current")


class _BgpRouteMapMaSafi_Type(BgpSafi):
    """Custom type bgpRouteMapMaSafi based on BgpSafi"""


_BgpRouteMapMaSafi_Object = MibTableColumn
bgpRouteMapMaSafi = _BgpRouteMapMaSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 7),
    _BgpRouteMapMaSafi_Type()
)
bgpRouteMapMaSafi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaSafi.setStatus("current")


class _BgpRouteMapMaSafiDef_Type(TruthValue):
    """Custom type bgpRouteMapMaSafiDef based on TruthValue"""


_BgpRouteMapMaSafiDef_Object = MibTableColumn
bgpRouteMapMaSafiDef = _BgpRouteMapMaSafiDef_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 8),
    _BgpRouteMapMaSafiDef_Type()
)
bgpRouteMapMaSafiDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaSafiDef.setStatus("current")


class _BgpRouteMapMaAs_Type(DisplayString):
    """Custom type bgpRouteMapMaAs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BgpRouteMapMaAs_Type.__name__ = "DisplayString"
_BgpRouteMapMaAs_Object = MibTableColumn
bgpRouteMapMaAs = _BgpRouteMapMaAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 9),
    _BgpRouteMapMaAs_Type()
)
bgpRouteMapMaAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaAs.setStatus("current")


class _BgpRouteMapMaComm_Type(DisplayString):
    """Custom type bgpRouteMapMaComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BgpRouteMapMaComm_Type.__name__ = "DisplayString"
_BgpRouteMapMaComm_Object = MibTableColumn
bgpRouteMapMaComm = _BgpRouteMapMaComm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 10),
    _BgpRouteMapMaComm_Type()
)
bgpRouteMapMaComm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaComm.setStatus("current")


class _BgpRouteMapMaExtComm_Type(DisplayString):
    """Custom type bgpRouteMapMaExtComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BgpRouteMapMaExtComm_Type.__name__ = "DisplayString"
_BgpRouteMapMaExtComm_Object = MibTableColumn
bgpRouteMapMaExtComm = _BgpRouteMapMaExtComm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 11),
    _BgpRouteMapMaExtComm_Type()
)
bgpRouteMapMaExtComm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaExtComm.setStatus("current")


class _BgpRouteMapMaAddr_Type(TruthValue):
    """Custom type bgpRouteMapMaAddr based on TruthValue"""


_BgpRouteMapMaAddr_Object = MibTableColumn
bgpRouteMapMaAddr = _BgpRouteMapMaAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 12),
    _BgpRouteMapMaAddr_Type()
)
bgpRouteMapMaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRouteMapMaAddr.setStatus("current")


class _BgpRouteMapMaNext_Type(TruthValue):
    """Custom type bgpRouteMapMaNext based on TruthValue"""


_BgpRouteMapMaNext_Object = MibTableColumn
bgpRouteMapMaNext = _BgpRouteMapMaNext_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 13),
    _BgpRouteMapMaNext_Type()
)
bgpRouteMapMaNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRouteMapMaNext.setStatus("current")


class _BgpRouteMapMaSource_Type(TruthValue):
    """Custom type bgpRouteMapMaSource based on TruthValue"""


_BgpRouteMapMaSource_Object = MibTableColumn
bgpRouteMapMaSource = _BgpRouteMapMaSource_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 14),
    _BgpRouteMapMaSource_Type()
)
bgpRouteMapMaSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRouteMapMaSource.setStatus("current")


class _BgpRouteMapMaMed_Type(Unsigned32):
    """Custom type bgpRouteMapMaMed based on Unsigned32"""
    defaultValue = 0


_BgpRouteMapMaMed_Object = MibTableColumn
bgpRouteMapMaMed = _BgpRouteMapMaMed_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 15),
    _BgpRouteMapMaMed_Type()
)
bgpRouteMapMaMed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaMed.setStatus("current")


class _BgpRouteMapMaMedDef_Type(TruthValue):
    """Custom type bgpRouteMapMaMedDef based on TruthValue"""


_BgpRouteMapMaMedDef_Object = MibTableColumn
bgpRouteMapMaMedDef = _BgpRouteMapMaMedDef_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 16),
    _BgpRouteMapMaMedDef_Type()
)
bgpRouteMapMaMedDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaMedDef.setStatus("current")


class _BgpRouteMapMaUser_Type(TruthValue):
    """Custom type bgpRouteMapMaUser based on TruthValue"""


_BgpRouteMapMaUser_Object = MibTableColumn
bgpRouteMapMaUser = _BgpRouteMapMaUser_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 17),
    _BgpRouteMapMaUser_Type()
)
bgpRouteMapMaUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaUser.setStatus("current")


class _BgpRouteMapSeAs_Type(Integer32):
    """Custom type bgpRouteMapSeAs based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpRouteMapSeAs_Type.__name__ = "Integer32"
_BgpRouteMapSeAs_Object = MibTableColumn
bgpRouteMapSeAs = _BgpRouteMapSeAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 18),
    _BgpRouteMapSeAs_Type()
)
bgpRouteMapSeAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeAs.setStatus("current")


class _BgpRouteMapSeAsAct_Type(BgpAsPathAction):
    """Custom type bgpRouteMapSeAsAct based on BgpAsPathAction"""


_BgpRouteMapSeAsAct_Object = MibTableColumn
bgpRouteMapSeAsAct = _BgpRouteMapSeAsAct_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 19),
    _BgpRouteMapSeAsAct_Type()
)
bgpRouteMapSeAsAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeAsAct.setStatus("current")


class _BgpRouteMapSeComm_Type(DisplayString):
    """Custom type bgpRouteMapSeComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BgpRouteMapSeComm_Type.__name__ = "DisplayString"
_BgpRouteMapSeComm_Object = MibTableColumn
bgpRouteMapSeComm = _BgpRouteMapSeComm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 20),
    _BgpRouteMapSeComm_Type()
)
bgpRouteMapSeComm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeComm.setStatus("current")


class _BgpRouteMapSeCommAct_Type(BgpCommunityAction):
    """Custom type bgpRouteMapSeCommAct based on BgpCommunityAction"""


_BgpRouteMapSeCommAct_Object = MibTableColumn
bgpRouteMapSeCommAct = _BgpRouteMapSeCommAct_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 21),
    _BgpRouteMapSeCommAct_Type()
)
bgpRouteMapSeCommAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeCommAct.setStatus("current")


class _BgpRouteMapSeExtComm_Type(DisplayString):
    """Custom type bgpRouteMapSeExtComm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_BgpRouteMapSeExtComm_Type.__name__ = "DisplayString"
_BgpRouteMapSeExtComm_Object = MibTableColumn
bgpRouteMapSeExtComm = _BgpRouteMapSeExtComm_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 22),
    _BgpRouteMapSeExtComm_Type()
)
bgpRouteMapSeExtComm.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeExtComm.setStatus("current")


class _BgpRouteMapSeExtCommAct_Type(BgpCommunityAction):
    """Custom type bgpRouteMapSeExtCommAct based on BgpCommunityAction"""


_BgpRouteMapSeExtCommAct_Object = MibTableColumn
bgpRouteMapSeExtCommAct = _BgpRouteMapSeExtCommAct_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 23),
    _BgpRouteMapSeExtCommAct_Type()
)
bgpRouteMapSeExtCommAct.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeExtCommAct.setStatus("current")


class _BgpRouteMapSeLocPref_Type(Integer32):
    """Custom type bgpRouteMapSeLocPref based on Integer32"""
    defaultValue = 0


_BgpRouteMapSeLocPref_Object = MibTableColumn
bgpRouteMapSeLocPref = _BgpRouteMapSeLocPref_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 24),
    _BgpRouteMapSeLocPref_Type()
)
bgpRouteMapSeLocPref.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeLocPref.setStatus("current")


class _BgpRouteMapSeLocPrefDef_Type(TruthValue):
    """Custom type bgpRouteMapSeLocPrefDef based on TruthValue"""


_BgpRouteMapSeLocPrefDef_Object = MibTableColumn
bgpRouteMapSeLocPrefDef = _BgpRouteMapSeLocPrefDef_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 25),
    _BgpRouteMapSeLocPrefDef_Type()
)
bgpRouteMapSeLocPrefDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeLocPrefDef.setStatus("current")


class _BgpRouteMapSeMed_Type(Unsigned32):
    """Custom type bgpRouteMapSeMed based on Unsigned32"""
    defaultValue = 0


_BgpRouteMapSeMed_Object = MibTableColumn
bgpRouteMapSeMed = _BgpRouteMapSeMed_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 26),
    _BgpRouteMapSeMed_Type()
)
bgpRouteMapSeMed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeMed.setStatus("current")


class _BgpRouteMapSeMedDef_Type(TruthValue):
    """Custom type bgpRouteMapSeMedDef based on TruthValue"""


_BgpRouteMapSeMedDef_Object = MibTableColumn
bgpRouteMapSeMedDef = _BgpRouteMapSeMedDef_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 27),
    _BgpRouteMapSeMedDef_Type()
)
bgpRouteMapSeMedDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeMedDef.setStatus("current")


class _BgpRouteMapSeNext_Type(InetAddress):
    """Custom type bgpRouteMapSeNext based on InetAddress"""
    defaultHexValue = "00"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpRouteMapSeNext_Type.__name__ = "InetAddress"
_BgpRouteMapSeNext_Object = MibTableColumn
bgpRouteMapSeNext = _BgpRouteMapSeNext_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 28),
    _BgpRouteMapSeNext_Type()
)
bgpRouteMapSeNext.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeNext.setStatus("current")


class _BgpRouteMapSeOrigin_Type(BgpOriginCode):
    """Custom type bgpRouteMapSeOrigin based on BgpOriginCode"""


_BgpRouteMapSeOrigin_Object = MibTableColumn
bgpRouteMapSeOrigin = _BgpRouteMapSeOrigin_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 29),
    _BgpRouteMapSeOrigin_Type()
)
bgpRouteMapSeOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeOrigin.setStatus("current")


class _BgpRouteMapSeOriginDef_Type(TruthValue):
    """Custom type bgpRouteMapSeOriginDef based on TruthValue"""


_BgpRouteMapSeOriginDef_Object = MibTableColumn
bgpRouteMapSeOriginDef = _BgpRouteMapSeOriginDef_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 30),
    _BgpRouteMapSeOriginDef_Type()
)
bgpRouteMapSeOriginDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeOriginDef.setStatus("current")


class _BgpRouteMapSeWeight_Type(Integer32):
    """Custom type bgpRouteMapSeWeight based on Integer32"""
    defaultValue = 0


_BgpRouteMapSeWeight_Object = MibTableColumn
bgpRouteMapSeWeight = _BgpRouteMapSeWeight_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 31),
    _BgpRouteMapSeWeight_Type()
)
bgpRouteMapSeWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeWeight.setStatus("current")


class _BgpRouteMapSeWeightDef_Type(TruthValue):
    """Custom type bgpRouteMapSeWeightDef based on TruthValue"""


_BgpRouteMapSeWeightDef_Object = MibTableColumn
bgpRouteMapSeWeightDef = _BgpRouteMapSeWeightDef_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 32),
    _BgpRouteMapSeWeightDef_Type()
)
bgpRouteMapSeWeightDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeWeightDef.setStatus("current")


class _BgpRouteMapSeFlap_Type(Unsigned32):
    """Custom type bgpRouteMapSeFlap based on Unsigned32"""
    defaultValue = 0


_BgpRouteMapSeFlap_Object = MibTableColumn
bgpRouteMapSeFlap = _BgpRouteMapSeFlap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 33),
    _BgpRouteMapSeFlap_Type()
)
bgpRouteMapSeFlap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeFlap.setStatus("current")


class _BgpRouteMapSeUser_Type(TruthValue):
    """Custom type bgpRouteMapSeUser based on TruthValue"""


_BgpRouteMapSeUser_Object = MibTableColumn
bgpRouteMapSeUser = _BgpRouteMapSeUser_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 34),
    _BgpRouteMapSeUser_Type()
)
bgpRouteMapSeUser.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeUser.setStatus("current")
_BgpRouteMapHitcnt_Type = Integer32
_BgpRouteMapHitcnt_Object = MibTableColumn
bgpRouteMapHitcnt = _BgpRouteMapHitcnt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 35),
    _BgpRouteMapHitcnt_Type()
)
bgpRouteMapHitcnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRouteMapHitcnt.setStatus("current")


class _BgpRouteMapClearcnt_Type(TruthValue):
    """Custom type bgpRouteMapClearcnt based on TruthValue"""


_BgpRouteMapClearcnt_Object = MibTableColumn
bgpRouteMapClearcnt = _BgpRouteMapClearcnt_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 36),
    _BgpRouteMapClearcnt_Type()
)
bgpRouteMapClearcnt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapClearcnt.setStatus("current")


class _BgpRouteMapUserInfo_Type(OctetString):
    """Custom type bgpRouteMapUserInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(255, 255),
    )


_BgpRouteMapUserInfo_Type.__name__ = "OctetString"
_BgpRouteMapUserInfo_Object = MibTableColumn
bgpRouteMapUserInfo = _BgpRouteMapUserInfo_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 37),
    _BgpRouteMapUserInfo_Type()
)
bgpRouteMapUserInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapUserInfo.setStatus("current")


class _BgpRouteMapType_Type(BgpPermitOrDeny):
    """Custom type bgpRouteMapType based on BgpPermitOrDeny"""


_BgpRouteMapType_Object = MibTableColumn
bgpRouteMapType = _BgpRouteMapType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 38),
    _BgpRouteMapType_Type()
)
bgpRouteMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapType.setStatus("current")


class _BgpRouteMapContinue_Type(Unsigned32):
    """Custom type bgpRouteMapContinue based on Unsigned32"""
    defaultValue = 0


_BgpRouteMapContinue_Object = MibTableColumn
bgpRouteMapContinue = _BgpRouteMapContinue_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 39),
    _BgpRouteMapContinue_Type()
)
bgpRouteMapContinue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapContinue.setStatus("current")


class _BgpRouteMapOrfAssoc_Type(BgpOrfAssociation):
    """Custom type bgpRouteMapOrfAssoc based on BgpOrfAssociation"""


_BgpRouteMapOrfAssoc_Object = MibTableColumn
bgpRouteMapOrfAssoc = _BgpRouteMapOrfAssoc_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 40),
    _BgpRouteMapOrfAssoc_Type()
)
bgpRouteMapOrfAssoc.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapOrfAssoc.setStatus("current")


class _BgpRouteMapSeAsLimUpper_Type(Unsigned32):
    """Custom type bgpRouteMapSeAsLimUpper based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpRouteMapSeAsLimUpper_Type.__name__ = "Unsigned32"
_BgpRouteMapSeAsLimUpper_Object = MibTableColumn
bgpRouteMapSeAsLimUpper = _BgpRouteMapSeAsLimUpper_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 41),
    _BgpRouteMapSeAsLimUpper_Type()
)
bgpRouteMapSeAsLimUpper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeAsLimUpper.setStatus("current")


class _BgpRouteMapSeAsLimDef_Type(TruthValue):
    """Custom type bgpRouteMapSeAsLimDef based on TruthValue"""


_BgpRouteMapSeAsLimDef_Object = MibTableColumn
bgpRouteMapSeAsLimDef = _BgpRouteMapSeAsLimDef_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 42),
    _BgpRouteMapSeAsLimDef_Type()
)
bgpRouteMapSeAsLimDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeAsLimDef.setStatus("current")


class _BgpRouteMapMaOrigin_Type(BgpOriginCode):
    """Custom type bgpRouteMapMaOrigin based on BgpOriginCode"""


_BgpRouteMapMaOrigin_Object = MibTableColumn
bgpRouteMapMaOrigin = _BgpRouteMapMaOrigin_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 43),
    _BgpRouteMapMaOrigin_Type()
)
bgpRouteMapMaOrigin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaOrigin.setStatus("current")


class _BgpRouteMapMaOriginDef_Type(TruthValue):
    """Custom type bgpRouteMapMaOriginDef based on TruthValue"""


_BgpRouteMapMaOriginDef_Object = MibTableColumn
bgpRouteMapMaOriginDef = _BgpRouteMapMaOriginDef_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 44),
    _BgpRouteMapMaOriginDef_Type()
)
bgpRouteMapMaOriginDef.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaOriginDef.setStatus("current")


class _BgpRouteMapSeMedDelta_Type(Unsigned32):
    """Custom type bgpRouteMapSeMedDelta based on Unsigned32"""
    defaultValue = 0


_BgpRouteMapSeMedDelta_Object = MibTableColumn
bgpRouteMapSeMedDelta = _BgpRouteMapSeMedDelta_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 45),
    _BgpRouteMapSeMedDelta_Type()
)
bgpRouteMapSeMedDelta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeMedDelta.setStatus("current")


class _BgpRouteMapSeMedDeltaTyp_Type(BgpMedDeltaType):
    """Custom type bgpRouteMapSeMedDeltaTyp based on BgpMedDeltaType"""


_BgpRouteMapSeMedDeltaTyp_Object = MibTableColumn
bgpRouteMapSeMedDeltaTyp = _BgpRouteMapSeMedDeltaTyp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 46),
    _BgpRouteMapSeMedDeltaTyp_Type()
)
bgpRouteMapSeMedDeltaTyp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeMedDeltaTyp.setStatus("current")


class _BgpRouteMapSeMedIgp_Type(TruthValue):
    """Custom type bgpRouteMapSeMedIgp based on TruthValue"""


_BgpRouteMapSeMedIgp_Object = MibTableColumn
bgpRouteMapSeMedIgp = _BgpRouteMapSeMedIgp_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 47),
    _BgpRouteMapSeMedIgp_Type()
)
bgpRouteMapSeMedIgp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeMedIgp.setStatus("current")


class _BgpRouteMapSeAsPrependCount_Type(Unsigned32):
    """Custom type bgpRouteMapSeAsPrependCount based on Unsigned32"""
    defaultValue = 0


_BgpRouteMapSeAsPrependCount_Object = MibTableColumn
bgpRouteMapSeAsPrependCount = _BgpRouteMapSeAsPrependCount_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 48),
    _BgpRouteMapSeAsPrependCount_Type()
)
bgpRouteMapSeAsPrependCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeAsPrependCount.setStatus("current")


class _BgpRouteMapSeAsPrependSize_Type(BgpAsSize):
    """Custom type bgpRouteMapSeAsPrependSize based on BgpAsSize"""


_BgpRouteMapSeAsPrependSize_Object = MibTableColumn
bgpRouteMapSeAsPrependSize = _BgpRouteMapSeAsPrependSize_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 49),
    _BgpRouteMapSeAsPrependSize_Type()
)
bgpRouteMapSeAsPrependSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeAsPrependSize.setStatus("current")


class _BgpRouteMapSeAsPrependAsVals_Type(OctetString):
    """Custom type bgpRouteMapSeAsPrependAsVals based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_BgpRouteMapSeAsPrependAsVals_Type.__name__ = "OctetString"
_BgpRouteMapSeAsPrependAsVals_Object = MibTableColumn
bgpRouteMapSeAsPrependAsVals = _BgpRouteMapSeAsPrependAsVals_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 50),
    _BgpRouteMapSeAsPrependAsVals_Type()
)
bgpRouteMapSeAsPrependAsVals.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapSeAsPrependAsVals.setStatus("current")


class _BgpRouteMapMaAnd_Type(TruthValue):
    """Custom type bgpRouteMapMaAnd based on TruthValue"""


_BgpRouteMapMaAnd_Object = MibTableColumn
bgpRouteMapMaAnd = _BgpRouteMapMaAnd_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 1, 1, 51),
    _BgpRouteMapMaAnd_Type()
)
bgpRouteMapMaAnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRouteMapMaAnd.setStatus("current")
_BgpIpPreTable_Object = MibTable
bgpIpPreTable = _BgpIpPreTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2)
)
if mibBuilder.loadTexts:
    bgpIpPreTable.setStatus("current")
_BgpIpPreEntry_Object = MibTableRow
bgpIpPreEntry = _BgpIpPreEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1)
)
bgpIpPreEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpRouteMapIndex"),
    (0, "DC-BGP-MIB", "bgpRouteMapNumber"),
    (0, "DC-BGP-MIB", "bgpIpPreMatch"),
    (0, "DC-BGP-MIB", "bgpIpPreNumber"),
)
if mibBuilder.loadTexts:
    bgpIpPreEntry.setStatus("current")
_BgpIpPreMatch_Type = BgpIpMatchType
_BgpIpPreMatch_Object = MibTableColumn
bgpIpPreMatch = _BgpIpPreMatch_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1, 4),
    _BgpIpPreMatch_Type()
)
bgpIpPreMatch.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpIpPreMatch.setStatus("current")
_BgpIpPreNumber_Type = Unsigned32
_BgpIpPreNumber_Object = MibTableColumn
bgpIpPreNumber = _BgpIpPreNumber_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1, 5),
    _BgpIpPreNumber_Type()
)
bgpIpPreNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpIpPreNumber.setStatus("current")
_BgpIpPreRowStatus_Type = RowStatus
_BgpIpPreRowStatus_Object = MibTableColumn
bgpIpPreRowStatus = _BgpIpPreRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1, 6),
    _BgpIpPreRowStatus_Type()
)
bgpIpPreRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpIpPreRowStatus.setStatus("current")


class _BgpIpPreAfi_Type(BgpAfi):
    """Custom type bgpIpPreAfi based on BgpAfi"""


_BgpIpPreAfi_Object = MibTableColumn
bgpIpPreAfi = _BgpIpPreAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1, 7),
    _BgpIpPreAfi_Type()
)
bgpIpPreAfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpIpPreAfi.setStatus("current")


class _BgpIpPreSafi_Type(BgpSafi):
    """Custom type bgpIpPreSafi based on BgpSafi"""


_BgpIpPreSafi_Object = MibTableColumn
bgpIpPreSafi = _BgpIpPreSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1, 8),
    _BgpIpPreSafi_Type()
)
bgpIpPreSafi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpIpPreSafi.setStatus("current")


class _BgpIpPreAddr_Type(InetAddress):
    """Custom type bgpIpPreAddr based on InetAddress"""
    defaultHexValue = "00"

    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpIpPreAddr_Type.__name__ = "InetAddress"
_BgpIpPreAddr_Object = MibTableColumn
bgpIpPreAddr = _BgpIpPreAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1, 9),
    _BgpIpPreAddr_Type()
)
bgpIpPreAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpIpPreAddr.setStatus("current")


class _BgpIpPreLen_Type(InetAddressPrefixLength):
    """Custom type bgpIpPreLen based on InetAddressPrefixLength"""
    defaultValue = 0


_BgpIpPreLen_Object = MibTableColumn
bgpIpPreLen = _BgpIpPreLen_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1, 10),
    _BgpIpPreLen_Type()
)
bgpIpPreLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpIpPreLen.setStatus("current")


class _BgpIpPreGe_Type(Integer32):
    """Custom type bgpIpPreGe based on Integer32"""
    defaultValue = 0


_BgpIpPreGe_Object = MibTableColumn
bgpIpPreGe = _BgpIpPreGe_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1, 11),
    _BgpIpPreGe_Type()
)
bgpIpPreGe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpIpPreGe.setStatus("current")


class _BgpIpPreLe_Type(Integer32):
    """Custom type bgpIpPreLe based on Integer32"""
    defaultValue = 0


_BgpIpPreLe_Object = MibTableColumn
bgpIpPreLe = _BgpIpPreLe_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1, 12),
    _BgpIpPreLe_Type()
)
bgpIpPreLe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpIpPreLe.setStatus("current")


class _BgpIpPreType_Type(BgpPermitOrDeny):
    """Custom type bgpIpPreType based on BgpPermitOrDeny"""


_BgpIpPreType_Object = MibTableColumn
bgpIpPreType = _BgpIpPreType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 2, 1, 13),
    _BgpIpPreType_Type()
)
bgpIpPreType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpIpPreType.setStatus("current")
_BgpPeergrTable_Object = MibTable
bgpPeergrTable = _BgpPeergrTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7)
)
if mibBuilder.loadTexts:
    bgpPeergrTable.setStatus("current")
_BgpPeergrEntry_Object = MibTableRow
bgpPeergrEntry = _BgpPeergrEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1)
)
bgpPeergrEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpPeergrIndex"),
)
if mibBuilder.loadTexts:
    bgpPeergrEntry.setStatus("current")
_BgpPeergrIndex_Type = Unsigned32
_BgpPeergrIndex_Object = MibTableColumn
bgpPeergrIndex = _BgpPeergrIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 2),
    _BgpPeergrIndex_Type()
)
bgpPeergrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeergrIndex.setStatus("current")
_BgpPeergrRowStatus_Type = RowStatus
_BgpPeergrRowStatus_Object = MibTableColumn
bgpPeergrRowStatus = _BgpPeergrRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 3),
    _BgpPeergrRowStatus_Type()
)
bgpPeergrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrRowStatus.setStatus("current")
_BgpPeergrConfig_Type = Unsigned32
_BgpPeergrConfig_Object = MibTableColumn
bgpPeergrConfig = _BgpPeergrConfig_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 4),
    _BgpPeergrConfig_Type()
)
bgpPeergrConfig.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrConfig.setStatus("current")


class _BgpPeergrArea_Type(BgpIbgpOrEbgp):
    """Custom type bgpPeergrArea based on BgpIbgpOrEbgp"""


_BgpPeergrArea_Object = MibTableColumn
bgpPeergrArea = _BgpPeergrArea_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 5),
    _BgpPeergrArea_Type()
)
bgpPeergrArea.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrArea.setStatus("current")


class _BgpPeergrAggrConfedAS_Type(TruthValue):
    """Custom type bgpPeergrAggrConfedAS based on TruthValue"""


_BgpPeergrAggrConfedAS_Object = MibTableColumn
bgpPeergrAggrConfedAS = _BgpPeergrAggrConfedAS_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 6),
    _BgpPeergrAggrConfedAS_Type()
)
bgpPeergrAggrConfedAS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrAggrConfedAS.setStatus("current")


class _BgpPeergrSoftResetWithStoredInfo_Type(TruthValue):
    """Custom type bgpPeergrSoftResetWithStoredInfo based on TruthValue"""


_BgpPeergrSoftResetWithStoredInfo_Object = MibTableColumn
bgpPeergrSoftResetWithStoredInfo = _BgpPeergrSoftResetWithStoredInfo_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 7),
    _BgpPeergrSoftResetWithStoredInfo_Type()
)
bgpPeergrSoftResetWithStoredInfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrSoftResetWithStoredInfo.setStatus("current")


class _BgpPeergrAllowLocalAs_Type(Unsigned32):
    """Custom type bgpPeergrAllowLocalAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpPeergrAllowLocalAs_Type.__name__ = "Unsigned32"
_BgpPeergrAllowLocalAs_Object = MibTableColumn
bgpPeergrAllowLocalAs = _BgpPeergrAllowLocalAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 8),
    _BgpPeergrAllowLocalAs_Type()
)
bgpPeergrAllowLocalAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrAllowLocalAs.setStatus("current")


class _BgpPeergrDisableSenderLoopDetect_Type(TruthValue):
    """Custom type bgpPeergrDisableSenderLoopDetect based on TruthValue"""


_BgpPeergrDisableSenderLoopDetect_Object = MibTableColumn
bgpPeergrDisableSenderLoopDetect = _BgpPeergrDisableSenderLoopDetect_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 9),
    _BgpPeergrDisableSenderLoopDetect_Type()
)
bgpPeergrDisableSenderLoopDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrDisableSenderLoopDetect.setStatus("current")


class _BgpPeergrNxtHopSlf_Type(TruthValue):
    """Custom type bgpPeergrNxtHopSlf based on TruthValue"""


_BgpPeergrNxtHopSlf_Object = MibTableColumn
bgpPeergrNxtHopSlf = _BgpPeergrNxtHopSlf_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 10),
    _BgpPeergrNxtHopSlf_Type()
)
bgpPeergrNxtHopSlf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrNxtHopSlf.setStatus("current")


class _BgpPeergrThirdPtyNxtHop_Type(TruthValue):
    """Custom type bgpPeergrThirdPtyNxtHop based on TruthValue"""


_BgpPeergrThirdPtyNxtHop_Object = MibTableColumn
bgpPeergrThirdPtyNxtHop = _BgpPeergrThirdPtyNxtHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 11),
    _BgpPeergrThirdPtyNxtHop_Type()
)
bgpPeergrThirdPtyNxtHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrThirdPtyNxtHop.setStatus("current")


class _BgpPeergrNxtHopPeer_Type(TruthValue):
    """Custom type bgpPeergrNxtHopPeer based on TruthValue"""


_BgpPeergrNxtHopPeer_Object = MibTableColumn
bgpPeergrNxtHopPeer = _BgpPeergrNxtHopPeer_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 12),
    _BgpPeergrNxtHopPeer_Type()
)
bgpPeergrNxtHopPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrNxtHopPeer.setStatus("current")


class _BgpPeergrEnableAttributeDiscard_Type(TruthValue):
    """Custom type bgpPeergrEnableAttributeDiscard based on TruthValue"""


_BgpPeergrEnableAttributeDiscard_Object = MibTableColumn
bgpPeergrEnableAttributeDiscard = _BgpPeergrEnableAttributeDiscard_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 7, 1, 13),
    _BgpPeergrEnableAttributeDiscard_Type()
)
bgpPeergrEnableAttributeDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrEnableAttributeDiscard.setStatus("current")
_BgpConfigTable_Object = MibTable
bgpConfigTable = _BgpConfigTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8)
)
if mibBuilder.loadTexts:
    bgpConfigTable.setStatus("current")
_BgpConfigEntry_Object = MibTableRow
bgpConfigEntry = _BgpConfigEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1)
)
bgpConfigEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpConfigIndex"),
)
if mibBuilder.loadTexts:
    bgpConfigEntry.setStatus("current")
_BgpConfigIndex_Type = Unsigned32
_BgpConfigIndex_Object = MibTableColumn
bgpConfigIndex = _BgpConfigIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 2),
    _BgpConfigIndex_Type()
)
bgpConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpConfigIndex.setStatus("current")
_BgpConfigRowStatus_Type = RowStatus
_BgpConfigRowStatus_Object = MibTableColumn
bgpConfigRowStatus = _BgpConfigRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 3),
    _BgpConfigRowStatus_Type()
)
bgpConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigRowStatus.setStatus("current")


class _BgpConfigRtgrimpe_Type(Unsigned32):
    """Custom type bgpConfigRtgrimpe based on Unsigned32"""
    defaultValue = 0


_BgpConfigRtgrimpe_Object = MibTableColumn
bgpConfigRtgrimpe = _BgpConfigRtgrimpe_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 4),
    _BgpConfigRtgrimpe_Type()
)
bgpConfigRtgrimpe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigRtgrimpe.setStatus("obsolete")


class _BgpConfigRtgrimde_Type(Unsigned32):
    """Custom type bgpConfigRtgrimde based on Unsigned32"""
    defaultValue = 0


_BgpConfigRtgrimde_Object = MibTableColumn
bgpConfigRtgrimde = _BgpConfigRtgrimde_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 5),
    _BgpConfigRtgrimde_Type()
)
bgpConfigRtgrimde.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigRtgrimde.setStatus("obsolete")


class _BgpConfigRtgrexpe_Type(Unsigned32):
    """Custom type bgpConfigRtgrexpe based on Unsigned32"""
    defaultValue = 0


_BgpConfigRtgrexpe_Object = MibTableColumn
bgpConfigRtgrexpe = _BgpConfigRtgrexpe_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 6),
    _BgpConfigRtgrexpe_Type()
)
bgpConfigRtgrexpe.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigRtgrexpe.setStatus("obsolete")


class _BgpConfigRtgrexde_Type(Unsigned32):
    """Custom type bgpConfigRtgrexde based on Unsigned32"""
    defaultValue = 0


_BgpConfigRtgrexde_Object = MibTableColumn
bgpConfigRtgrexde = _BgpConfigRtgrexde_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 7),
    _BgpConfigRtgrexde_Type()
)
bgpConfigRtgrexde.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigRtgrexde.setStatus("obsolete")


class _BgpConfigDefImport_Type(BgpPermitOrDeny):
    """Custom type bgpConfigDefImport based on BgpPermitOrDeny"""


_BgpConfigDefImport_Object = MibTableColumn
bgpConfigDefImport = _BgpConfigDefImport_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 8),
    _BgpConfigDefImport_Type()
)
bgpConfigDefImport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigDefImport.setStatus("obsolete")


class _BgpConfigDefExport_Type(BgpPermitOrDeny):
    """Custom type bgpConfigDefExport based on BgpPermitOrDeny"""


_BgpConfigDefExport_Object = MibTableColumn
bgpConfigDefExport = _BgpConfigDefExport_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 9),
    _BgpConfigDefExport_Type()
)
bgpConfigDefExport.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigDefExport.setStatus("obsolete")


class _BgpConfigNxtHopSlf_Type(TruthValue):
    """Custom type bgpConfigNxtHopSlf based on TruthValue"""


_BgpConfigNxtHopSlf_Object = MibTableColumn
bgpConfigNxtHopSlf = _BgpConfigNxtHopSlf_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 10),
    _BgpConfigNxtHopSlf_Type()
)
bgpConfigNxtHopSlf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigNxtHopSlf.setStatus("obsolete")


class _BgpConfigRemove_Type(TruthValue):
    """Custom type bgpConfigRemove based on TruthValue"""


_BgpConfigRemove_Object = MibTableColumn
bgpConfigRemove = _BgpConfigRemove_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 11),
    _BgpConfigRemove_Type()
)
bgpConfigRemove.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigRemove.setStatus("current")


class _BgpConfigImportMap_Type(Unsigned32):
    """Custom type bgpConfigImportMap based on Unsigned32"""
    defaultValue = 0


_BgpConfigImportMap_Object = MibTableColumn
bgpConfigImportMap = _BgpConfigImportMap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 12),
    _BgpConfigImportMap_Type()
)
bgpConfigImportMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigImportMap.setStatus("current")


class _BgpConfigExportMap_Type(Unsigned32):
    """Custom type bgpConfigExportMap based on Unsigned32"""
    defaultValue = 0


_BgpConfigExportMap_Object = MibTableColumn
bgpConfigExportMap = _BgpConfigExportMap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 13),
    _BgpConfigExportMap_Type()
)
bgpConfigExportMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigExportMap.setStatus("current")


class _BgpConfigAdvertiseMap_Type(Unsigned32):
    """Custom type bgpConfigAdvertiseMap based on Unsigned32"""
    defaultValue = 0


_BgpConfigAdvertiseMap_Object = MibTableColumn
bgpConfigAdvertiseMap = _BgpConfigAdvertiseMap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 14),
    _BgpConfigAdvertiseMap_Type()
)
bgpConfigAdvertiseMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigAdvertiseMap.setStatus("current")


class _BgpConfigNonExistMap_Type(Unsigned32):
    """Custom type bgpConfigNonExistMap based on Unsigned32"""
    defaultValue = 0


_BgpConfigNonExistMap_Object = MibTableColumn
bgpConfigNonExistMap = _BgpConfigNonExistMap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 15),
    _BgpConfigNonExistMap_Type()
)
bgpConfigNonExistMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigNonExistMap.setStatus("current")
_BgpConfigBlockCondAdv_Type = TruthValue
_BgpConfigBlockCondAdv_Object = MibTableColumn
bgpConfigBlockCondAdv = _BgpConfigBlockCondAdv_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 16),
    _BgpConfigBlockCondAdv_Type()
)
bgpConfigBlockCondAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpConfigBlockCondAdv.setStatus("current")


class _BgpConfigThirdPtyNxtHop_Type(TruthValue):
    """Custom type bgpConfigThirdPtyNxtHop based on TruthValue"""


_BgpConfigThirdPtyNxtHop_Object = MibTableColumn
bgpConfigThirdPtyNxtHop = _BgpConfigThirdPtyNxtHop_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 17),
    _BgpConfigThirdPtyNxtHop_Type()
)
bgpConfigThirdPtyNxtHop.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigThirdPtyNxtHop.setStatus("obsolete")


class _BgpConfigNxtHopPeer_Type(TruthValue):
    """Custom type bgpConfigNxtHopPeer based on TruthValue"""


_BgpConfigNxtHopPeer_Object = MibTableColumn
bgpConfigNxtHopPeer = _BgpConfigNxtHopPeer_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 18),
    _BgpConfigNxtHopPeer_Type()
)
bgpConfigNxtHopPeer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigNxtHopPeer.setStatus("obsolete")


class _BgpConfigCondAdvOn_Type(TruthValue):
    """Custom type bgpConfigCondAdvOn based on TruthValue"""


_BgpConfigCondAdvOn_Object = MibTableColumn
bgpConfigCondAdvOn = _BgpConfigCondAdvOn_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 8, 1, 19),
    _BgpConfigCondAdvOn_Type()
)
bgpConfigCondAdvOn.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpConfigCondAdvOn.setStatus("current")
_BgpFlapConfigTable_Object = MibTable
bgpFlapConfigTable = _BgpFlapConfigTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9)
)
if mibBuilder.loadTexts:
    bgpFlapConfigTable.setStatus("current")
_BgpFlapConfigEntry_Object = MibTableRow
bgpFlapConfigEntry = _BgpFlapConfigEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9, 1)
)
bgpFlapConfigEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpFlapConfigIndex"),
)
if mibBuilder.loadTexts:
    bgpFlapConfigEntry.setStatus("current")
_BgpFlapConfigIndex_Type = Unsigned32
_BgpFlapConfigIndex_Object = MibTableColumn
bgpFlapConfigIndex = _BgpFlapConfigIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9, 1, 2),
    _BgpFlapConfigIndex_Type()
)
bgpFlapConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpFlapConfigIndex.setStatus("current")
_BgpFlapConfigRowStatus_Type = RowStatus
_BgpFlapConfigRowStatus_Object = MibTableColumn
bgpFlapConfigRowStatus = _BgpFlapConfigRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9, 1, 3),
    _BgpFlapConfigRowStatus_Type()
)
bgpFlapConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpFlapConfigRowStatus.setStatus("current")


class _BgpFlapConfigCut_Type(Integer32):
    """Custom type bgpFlapConfigCut based on Integer32"""
    defaultValue = 125


_BgpFlapConfigCut_Object = MibTableColumn
bgpFlapConfigCut = _BgpFlapConfigCut_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9, 1, 4),
    _BgpFlapConfigCut_Type()
)
bgpFlapConfigCut.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpFlapConfigCut.setStatus("current")


class _BgpFlapConfigReuse_Type(Integer32):
    """Custom type bgpFlapConfigReuse based on Integer32"""
    defaultValue = 50


_BgpFlapConfigReuse_Object = MibTableColumn
bgpFlapConfigReuse = _BgpFlapConfigReuse_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9, 1, 5),
    _BgpFlapConfigReuse_Type()
)
bgpFlapConfigReuse.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpFlapConfigReuse.setStatus("current")


class _BgpFlapConfigThold_Type(Integer32):
    """Custom type bgpFlapConfigThold based on Integer32"""
    defaultValue = 900


_BgpFlapConfigThold_Object = MibTableColumn
bgpFlapConfigThold = _BgpFlapConfigThold_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9, 1, 6),
    _BgpFlapConfigThold_Type()
)
bgpFlapConfigThold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpFlapConfigThold.setStatus("current")
if mibBuilder.loadTexts:
    bgpFlapConfigThold.setUnits("seconds")


class _BgpFlapConfigDecayok_Type(Integer32):
    """Custom type bgpFlapConfigDecayok based on Integer32"""
    defaultValue = 300


_BgpFlapConfigDecayok_Object = MibTableColumn
bgpFlapConfigDecayok = _BgpFlapConfigDecayok_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9, 1, 7),
    _BgpFlapConfigDecayok_Type()
)
bgpFlapConfigDecayok.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpFlapConfigDecayok.setStatus("current")
if mibBuilder.loadTexts:
    bgpFlapConfigDecayok.setUnits("seconds")


class _BgpFlapConfigDecayng_Type(Integer32):
    """Custom type bgpFlapConfigDecayng based on Integer32"""
    defaultValue = 900


_BgpFlapConfigDecayng_Object = MibTableColumn
bgpFlapConfigDecayng = _BgpFlapConfigDecayng_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9, 1, 8),
    _BgpFlapConfigDecayng_Type()
)
bgpFlapConfigDecayng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpFlapConfigDecayng.setStatus("current")
if mibBuilder.loadTexts:
    bgpFlapConfigDecayng.setUnits("seconds")


class _BgpFlapConfigTmaxok_Type(Integer32):
    """Custom type bgpFlapConfigTmaxok based on Integer32"""
    defaultValue = 900


_BgpFlapConfigTmaxok_Object = MibTableColumn
bgpFlapConfigTmaxok = _BgpFlapConfigTmaxok_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9, 1, 9),
    _BgpFlapConfigTmaxok_Type()
)
bgpFlapConfigTmaxok.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpFlapConfigTmaxok.setStatus("current")
if mibBuilder.loadTexts:
    bgpFlapConfigTmaxok.setUnits("seconds")


class _BgpFlapConfigTmaxng_Type(Integer32):
    """Custom type bgpFlapConfigTmaxng based on Integer32"""
    defaultValue = 1800


_BgpFlapConfigTmaxng_Object = MibTableColumn
bgpFlapConfigTmaxng = _BgpFlapConfigTmaxng_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 9, 1, 10),
    _BgpFlapConfigTmaxng_Type()
)
bgpFlapConfigTmaxng.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpFlapConfigTmaxng.setStatus("current")
if mibBuilder.loadTexts:
    bgpFlapConfigTmaxng.setUnits("seconds")
_BgpAggregateTable_Object = MibTable
bgpAggregateTable = _BgpAggregateTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10)
)
if mibBuilder.loadTexts:
    bgpAggregateTable.setStatus("current")
_BgpAggregateEntry_Object = MibTableRow
bgpAggregateEntry = _BgpAggregateEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1)
)
bgpAggregateEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpAggrAfi"),
    (0, "DC-BGP-MIB", "bgpAggrSafi"),
    (0, "DC-BGP-MIB", "bgpAggrPrefix"),
    (0, "DC-BGP-MIB", "bgpAggrPrefixLength"),
)
if mibBuilder.loadTexts:
    bgpAggregateEntry.setStatus("current")
_BgpAggrAfi_Type = BgpAfi
_BgpAggrAfi_Object = MibTableColumn
bgpAggrAfi = _BgpAggrAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1, 2),
    _BgpAggrAfi_Type()
)
bgpAggrAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAggrAfi.setStatus("current")
_BgpAggrSafi_Type = BgpSafi
_BgpAggrSafi_Object = MibTableColumn
bgpAggrSafi = _BgpAggrSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1, 3),
    _BgpAggrSafi_Type()
)
bgpAggrSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAggrSafi.setStatus("current")


class _BgpAggrPrefix_Type(InetAddress):
    """Custom type bgpAggrPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpAggrPrefix_Type.__name__ = "InetAddress"
_BgpAggrPrefix_Object = MibTableColumn
bgpAggrPrefix = _BgpAggrPrefix_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1, 4),
    _BgpAggrPrefix_Type()
)
bgpAggrPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAggrPrefix.setStatus("current")
_BgpAggrPrefixLength_Type = InetAddressPrefixLength
_BgpAggrPrefixLength_Object = MibTableColumn
bgpAggrPrefixLength = _BgpAggrPrefixLength_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1, 5),
    _BgpAggrPrefixLength_Type()
)
bgpAggrPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpAggrPrefixLength.setStatus("current")
_BgpAggrRowStatus_Type = RowStatus
_BgpAggrRowStatus_Object = MibTableColumn
bgpAggrRowStatus = _BgpAggrRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1, 6),
    _BgpAggrRowStatus_Type()
)
bgpAggrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpAggrRowStatus.setStatus("current")


class _BgpAggrOptions_Type(BgpAggregateOptions):
    """Custom type bgpAggrOptions based on BgpAggregateOptions"""


_BgpAggrOptions_Object = MibTableColumn
bgpAggrOptions = _BgpAggrOptions_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1, 7),
    _BgpAggrOptions_Type()
)
bgpAggrOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpAggrOptions.setStatus("current")


class _BgpAggrSuppressMap_Type(Unsigned32):
    """Custom type bgpAggrSuppressMap based on Unsigned32"""
    defaultValue = 0


_BgpAggrSuppressMap_Object = MibTableColumn
bgpAggrSuppressMap = _BgpAggrSuppressMap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1, 8),
    _BgpAggrSuppressMap_Type()
)
bgpAggrSuppressMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpAggrSuppressMap.setStatus("current")


class _BgpAggrAdvertiseMap_Type(Unsigned32):
    """Custom type bgpAggrAdvertiseMap based on Unsigned32"""
    defaultValue = 0


_BgpAggrAdvertiseMap_Object = MibTableColumn
bgpAggrAdvertiseMap = _BgpAggrAdvertiseMap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1, 9),
    _BgpAggrAdvertiseMap_Type()
)
bgpAggrAdvertiseMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpAggrAdvertiseMap.setStatus("current")


class _BgpAggrAttributeMap_Type(Unsigned32):
    """Custom type bgpAggrAttributeMap based on Unsigned32"""
    defaultValue = 0


_BgpAggrAttributeMap_Object = MibTableColumn
bgpAggrAttributeMap = _BgpAggrAttributeMap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1, 10),
    _BgpAggrAttributeMap_Type()
)
bgpAggrAttributeMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpAggrAttributeMap.setStatus("current")


class _BgpAggrPermanent_Type(TruthValue):
    """Custom type bgpAggrPermanent based on TruthValue"""


_BgpAggrPermanent_Object = MibTableColumn
bgpAggrPermanent = _BgpAggrPermanent_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 10, 1, 11),
    _BgpAggrPermanent_Type()
)
bgpAggrPermanent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpAggrPermanent.setStatus("current")
_BgpOrfCapabilityTable_Object = MibTable
bgpOrfCapabilityTable = _BgpOrfCapabilityTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 11)
)
if mibBuilder.loadTexts:
    bgpOrfCapabilityTable.setStatus("current")
_BgpOrfCapabilityEntry_Object = MibTableRow
bgpOrfCapabilityEntry = _BgpOrfCapabilityEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 11, 1)
)
bgpOrfCapabilityEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpOrfCapabilityAfi"),
    (0, "DC-BGP-MIB", "bgpOrfCapabilitySafi"),
    (0, "DC-BGP-MIB", "bgpOrfCapabilityOrfType"),
)
if mibBuilder.loadTexts:
    bgpOrfCapabilityEntry.setStatus("current")
_BgpOrfCapabilityAfi_Type = BgpAfi
_BgpOrfCapabilityAfi_Object = MibTableColumn
bgpOrfCapabilityAfi = _BgpOrfCapabilityAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 11, 1, 2),
    _BgpOrfCapabilityAfi_Type()
)
bgpOrfCapabilityAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpOrfCapabilityAfi.setStatus("current")
_BgpOrfCapabilitySafi_Type = BgpSafi
_BgpOrfCapabilitySafi_Object = MibTableColumn
bgpOrfCapabilitySafi = _BgpOrfCapabilitySafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 11, 1, 3),
    _BgpOrfCapabilitySafi_Type()
)
bgpOrfCapabilitySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpOrfCapabilitySafi.setStatus("current")
_BgpOrfCapabilityOrfType_Type = BgpOrfType
_BgpOrfCapabilityOrfType_Object = MibTableColumn
bgpOrfCapabilityOrfType = _BgpOrfCapabilityOrfType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 11, 1, 4),
    _BgpOrfCapabilityOrfType_Type()
)
bgpOrfCapabilityOrfType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpOrfCapabilityOrfType.setStatus("current")


class _BgpOrfCapabilityAdminStatus_Type(BgpAdminStatus):
    """Custom type bgpOrfCapabilityAdminStatus based on BgpAdminStatus"""


_BgpOrfCapabilityAdminStatus_Object = MibTableColumn
bgpOrfCapabilityAdminStatus = _BgpOrfCapabilityAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 11, 1, 5),
    _BgpOrfCapabilityAdminStatus_Type()
)
bgpOrfCapabilityAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpOrfCapabilityAdminStatus.setStatus("current")


class _BgpOrfCapabilitySendReceive_Type(BgpOrfSendReceive):
    """Custom type bgpOrfCapabilitySendReceive based on BgpOrfSendReceive"""


_BgpOrfCapabilitySendReceive_Object = MibTableColumn
bgpOrfCapabilitySendReceive = _BgpOrfCapabilitySendReceive_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 11, 1, 6),
    _BgpOrfCapabilitySendReceive_Type()
)
bgpOrfCapabilitySendReceive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpOrfCapabilitySendReceive.setStatus("current")
_BgpPeergrAfiSafiTable_Object = MibTable
bgpPeergrAfiSafiTable = _BgpPeergrAfiSafiTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 12)
)
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiTable.setStatus("current")
_BgpPeergrAfiSafiEntry_Object = MibTableRow
bgpPeergrAfiSafiEntry = _BgpPeergrAfiSafiEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 12, 1)
)
bgpPeergrAfiSafiEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpPeergrIndex"),
    (0, "DC-BGP-MIB", "bgpPeergrAfiSafiAfi"),
    (0, "DC-BGP-MIB", "bgpPeergrAfiSafiSafi"),
)
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiEntry.setStatus("current")
_BgpPeergrAfiSafiAfi_Type = BgpAfi
_BgpPeergrAfiSafiAfi_Object = MibTableColumn
bgpPeergrAfiSafiAfi = _BgpPeergrAfiSafiAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 12, 1, 3),
    _BgpPeergrAfiSafiAfi_Type()
)
bgpPeergrAfiSafiAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiAfi.setStatus("current")
_BgpPeergrAfiSafiSafi_Type = BgpSafi
_BgpPeergrAfiSafiSafi_Object = MibTableColumn
bgpPeergrAfiSafiSafi = _BgpPeergrAfiSafiSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 12, 1, 4),
    _BgpPeergrAfiSafiSafi_Type()
)
bgpPeergrAfiSafiSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiSafi.setStatus("current")


class _BgpPeergrAfiSafiAllowLocalAs_Type(Unsigned32):
    """Custom type bgpPeergrAfiSafiAllowLocalAs based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_BgpPeergrAfiSafiAllowLocalAs_Type.__name__ = "Unsigned32"
_BgpPeergrAfiSafiAllowLocalAs_Object = MibTableColumn
bgpPeergrAfiSafiAllowLocalAs = _BgpPeergrAfiSafiAllowLocalAs_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 12, 1, 5),
    _BgpPeergrAfiSafiAllowLocalAs_Type()
)
bgpPeergrAfiSafiAllowLocalAs.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiAllowLocalAs.setStatus("current")


class _BgpPeergrAfiSafiDisSndLpDetect_Type(TruthValue):
    """Custom type bgpPeergrAfiSafiDisSndLpDetect based on TruthValue"""


_BgpPeergrAfiSafiDisSndLpDetect_Object = MibTableColumn
bgpPeergrAfiSafiDisSndLpDetect = _BgpPeergrAfiSafiDisSndLpDetect_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 12, 1, 6),
    _BgpPeergrAfiSafiDisSndLpDetect_Type()
)
bgpPeergrAfiSafiDisSndLpDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiDisSndLpDetect.setStatus("current")


class _BgpPeergrAfiSafiNxtHopSlf_Type(TruthValue):
    """Custom type bgpPeergrAfiSafiNxtHopSlf based on TruthValue"""


_BgpPeergrAfiSafiNxtHopSlf_Object = MibTableColumn
bgpPeergrAfiSafiNxtHopSlf = _BgpPeergrAfiSafiNxtHopSlf_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 12, 1, 7),
    _BgpPeergrAfiSafiNxtHopSlf_Type()
)
bgpPeergrAfiSafiNxtHopSlf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiNxtHopSlf.setStatus("current")


class _BgpPeergrAfiSafiOrigDefault_Type(TruthValue):
    """Custom type bgpPeergrAfiSafiOrigDefault based on TruthValue"""


_BgpPeergrAfiSafiOrigDefault_Object = MibTableColumn
bgpPeergrAfiSafiOrigDefault = _BgpPeergrAfiSafiOrigDefault_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 12, 1, 8),
    _BgpPeergrAfiSafiOrigDefault_Type()
)
bgpPeergrAfiSafiOrigDefault.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiOrigDefault.setStatus("current")


class _BgpPeergrAfiSafiOrigDefaultRtMap_Type(Unsigned32):
    """Custom type bgpPeergrAfiSafiOrigDefaultRtMap based on Unsigned32"""
    defaultValue = 0


_BgpPeergrAfiSafiOrigDefaultRtMap_Object = MibTableColumn
bgpPeergrAfiSafiOrigDefaultRtMap = _BgpPeergrAfiSafiOrigDefaultRtMap_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 12, 1, 9),
    _BgpPeergrAfiSafiOrigDefaultRtMap_Type()
)
bgpPeergrAfiSafiOrigDefaultRtMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiOrigDefaultRtMap.setStatus("current")


class _BgpPeergrAfiSafiSoftResetStore_Type(TruthValue):
    """Custom type bgpPeergrAfiSafiSoftResetStore based on TruthValue"""


_BgpPeergrAfiSafiSoftResetStore_Object = MibTableColumn
bgpPeergrAfiSafiSoftResetStore = _BgpPeergrAfiSafiSoftResetStore_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 5, 12, 1, 10),
    _BgpPeergrAfiSafiSoftResetStore_Type()
)
bgpPeergrAfiSafiSoftResetStore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiSoftResetStore.setStatus("current")
_BgpHaf_ObjectIdentity = ObjectIdentity
bgpHaf = _BgpHaf_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6)
)
_BgpRmAfmJoinTable_Object = MibTable
bgpRmAfmJoinTable = _BgpRmAfmJoinTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1)
)
if mibBuilder.loadTexts:
    bgpRmAfmJoinTable.setStatus("current")
_BgpRmAfmJoinEntry_Object = MibTableRow
bgpRmAfmJoinEntry = _BgpRmAfmJoinEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1, 1)
)
bgpRmAfmJoinEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpRmAfmJoin"),
)
if mibBuilder.loadTexts:
    bgpRmAfmJoinEntry.setStatus("current")
_BgpRmAfmJoin_Type = Unsigned32
_BgpRmAfmJoin_Object = MibTableColumn
bgpRmAfmJoin = _BgpRmAfmJoin_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1, 1, 2),
    _BgpRmAfmJoin_Type()
)
bgpRmAfmJoin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRmAfmJoin.setStatus("current")
_BgpRmAfmRowStatus_Type = RowStatus
_BgpRmAfmRowStatus_Object = MibTableColumn
bgpRmAfmRowStatus = _BgpRmAfmRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1, 1, 3),
    _BgpRmAfmRowStatus_Type()
)
bgpRmAfmRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfmRowStatus.setStatus("current")


class _BgpRmAfmAdminStatus_Type(BgpAdminStatus):
    """Custom type bgpRmAfmAdminStatus based on BgpAdminStatus"""


_BgpRmAfmAdminStatus_Object = MibTableColumn
bgpRmAfmAdminStatus = _BgpRmAfmAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1, 1, 4),
    _BgpRmAfmAdminStatus_Type()
)
bgpRmAfmAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfmAdminStatus.setStatus("current")
_BgpRmAfmOperStatus_Type = BgpOperStatus
_BgpRmAfmOperStatus_Object = MibTableColumn
bgpRmAfmOperStatus = _BgpRmAfmOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1, 1, 5),
    _BgpRmAfmOperStatus_Type()
)
bgpRmAfmOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfmOperStatus.setStatus("current")


class _BgpRmAfmPartnerIndex_Type(Unsigned32):
    """Custom type bgpRmAfmPartnerIndex based on Unsigned32"""
    defaultValue = 0


_BgpRmAfmPartnerIndex_Object = MibTableColumn
bgpRmAfmPartnerIndex = _BgpRmAfmPartnerIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1, 1, 6),
    _BgpRmAfmPartnerIndex_Type()
)
bgpRmAfmPartnerIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfmPartnerIndex.setStatus("current")


class _BgpRmAfmAfi_Type(BgpAfi):
    """Custom type bgpRmAfmAfi based on BgpAfi"""


_BgpRmAfmAfi_Object = MibTableColumn
bgpRmAfmAfi = _BgpRmAfmAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1, 1, 7),
    _BgpRmAfmAfi_Type()
)
bgpRmAfmAfi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfmAfi.setStatus("current")


class _BgpRmAfmSafi_Type(BgpSafi):
    """Custom type bgpRmAfmSafi based on BgpSafi"""


_BgpRmAfmSafi_Object = MibTableColumn
bgpRmAfmSafi = _BgpRmAfmSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1, 1, 8),
    _BgpRmAfmSafi_Type()
)
bgpRmAfmSafi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfmSafi.setStatus("current")
_BgpRmAfmJoinStatus_Type = BgpMjStatus
_BgpRmAfmJoinStatus_Object = MibTableColumn
bgpRmAfmJoinStatus = _BgpRmAfmJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1, 1, 9),
    _BgpRmAfmJoinStatus_Type()
)
bgpRmAfmJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmAfmJoinStatus.setStatus("current")


class _BgpRmAfmRestartTime_Type(Unsigned32):
    """Custom type bgpRmAfmRestartTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_BgpRmAfmRestartTime_Type.__name__ = "Unsigned32"
_BgpRmAfmRestartTime_Object = MibTableColumn
bgpRmAfmRestartTime = _BgpRmAfmRestartTime_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 1, 1, 10),
    _BgpRmAfmRestartTime_Type()
)
bgpRmAfmRestartTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpRmAfmRestartTime.setStatus("current")
if mibBuilder.loadTexts:
    bgpRmAfmRestartTime.setUnits("seconds")
_BgpRmNmTable_Object = MibTable
bgpRmNmTable = _BgpRmNmTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 2)
)
if mibBuilder.loadTexts:
    bgpRmNmTable.setStatus("current")
_BgpRmNmEntry_Object = MibTableRow
bgpRmNmEntry = _BgpRmNmEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 2, 1)
)
bgpRmNmEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpRmNmMasterIndex"),
)
if mibBuilder.loadTexts:
    bgpRmNmEntry.setStatus("current")
_BgpRmNmMasterIndex_Type = Unsigned32
_BgpRmNmMasterIndex_Object = MibTableColumn
bgpRmNmMasterIndex = _BgpRmNmMasterIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 2, 1, 2),
    _BgpRmNmMasterIndex_Type()
)
bgpRmNmMasterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRmNmMasterIndex.setStatus("current")
_BgpRmNmJoinStatus_Type = BgpSjStatus
_BgpRmNmJoinStatus_Object = MibTableColumn
bgpRmNmJoinStatus = _BgpRmNmJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 2, 1, 3),
    _BgpRmNmJoinStatus_Type()
)
bgpRmNmJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmNmJoinStatus.setStatus("current")
_BgpNmMjTable_Object = MibTable
bgpNmMjTable = _BgpNmMjTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 3)
)
if mibBuilder.loadTexts:
    bgpNmMjTable.setStatus("current")
_BgpNmMjEntry_Object = MibTableRow
bgpNmMjEntry = _BgpNmMjEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 3, 1)
)
bgpNmMjEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpNmMjEntity"),
    (0, "DC-BGP-MIB", "bgpNmMjJoin"),
)
if mibBuilder.loadTexts:
    bgpNmMjEntry.setStatus("current")
_BgpNmMjEntity_Type = Unsigned32
_BgpNmMjEntity_Object = MibTableColumn
bgpNmMjEntity = _BgpNmMjEntity_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 3, 1, 1),
    _BgpNmMjEntity_Type()
)
bgpNmMjEntity.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNmMjEntity.setStatus("current")


class _BgpNmMjJoin_Type(Unsigned32):
    """Custom type bgpNmMjJoin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_BgpNmMjJoin_Type.__name__ = "Unsigned32"
_BgpNmMjJoin_Object = MibTableColumn
bgpNmMjJoin = _BgpNmMjJoin_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 3, 1, 2),
    _BgpNmMjJoin_Type()
)
bgpNmMjJoin.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNmMjJoin.setStatus("current")
_BgpNmMjJoinPartner_Type = BgpComponentId
_BgpNmMjJoinPartner_Object = MibTableColumn
bgpNmMjJoinPartner = _BgpNmMjJoinPartner_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 3, 1, 3),
    _BgpNmMjJoinPartner_Type()
)
bgpNmMjJoinPartner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNmMjJoinPartner.setStatus("current")
_BgpNmMjPartnerIndex_Type = Unsigned32
_BgpNmMjPartnerIndex_Object = MibTableColumn
bgpNmMjPartnerIndex = _BgpNmMjPartnerIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 3, 1, 4),
    _BgpNmMjPartnerIndex_Type()
)
bgpNmMjPartnerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNmMjPartnerIndex.setStatus("current")
_BgpNmMjJoinStatus_Type = BgpMjStatus
_BgpNmMjJoinStatus_Object = MibTableColumn
bgpNmMjJoinStatus = _BgpNmMjJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 3, 1, 5),
    _BgpNmMjJoinStatus_Type()
)
bgpNmMjJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNmMjJoinStatus.setStatus("current")
_BgpRmArinhJoinTable_Object = MibTable
bgpRmArinhJoinTable = _BgpRmArinhJoinTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 4)
)
if mibBuilder.loadTexts:
    bgpRmArinhJoinTable.setStatus("current")
_BgpRmArinhJoinEntry_Object = MibTableRow
bgpRmArinhJoinEntry = _BgpRmArinhJoinEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 4, 1)
)
bgpRmArinhJoinEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpRmEntIndex"),
    (0, "DC-BGP-MIB", "bgpRmArinhAfi"),
    (0, "DC-BGP-MIB", "bgpRmArinhSafi"),
)
if mibBuilder.loadTexts:
    bgpRmArinhJoinEntry.setStatus("current")
_BgpRmArinhAfi_Type = BgpAfi
_BgpRmArinhAfi_Object = MibTableColumn
bgpRmArinhAfi = _BgpRmArinhAfi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 4, 1, 2),
    _BgpRmArinhAfi_Type()
)
bgpRmArinhAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRmArinhAfi.setStatus("current")
_BgpRmArinhSafi_Type = BgpSafi
_BgpRmArinhSafi_Object = MibTableColumn
bgpRmArinhSafi = _BgpRmArinhSafi_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 4, 1, 3),
    _BgpRmArinhSafi_Type()
)
bgpRmArinhSafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpRmArinhSafi.setStatus("current")
_BgpRmArinhJoinStatus_Type = BgpSjStatus
_BgpRmArinhJoinStatus_Object = MibTableColumn
bgpRmArinhJoinStatus = _BgpRmArinhJoinStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 4, 1, 4),
    _BgpRmArinhJoinStatus_Type()
)
bgpRmArinhJoinStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmArinhJoinStatus.setStatus("current")
_BgpRmArinhEntIndex_Type = Unsigned32
_BgpRmArinhEntIndex_Object = MibTableColumn
bgpRmArinhEntIndex = _BgpRmArinhEntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 6, 4, 1, 5),
    _BgpRmArinhEntIndex_Type()
)
bgpRmArinhEntIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpRmArinhEntIndex.setStatus("current")
_BgpNm_ObjectIdentity = ObjectIdentity
bgpNm = _BgpNm_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7)
)
_BgpNmEntTable_Object = MibTable
bgpNmEntTable = _BgpNmEntTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 1)
)
if mibBuilder.loadTexts:
    bgpNmEntTable.setStatus("current")
_BgpNmEntEntry_Object = MibTableRow
bgpNmEntEntry = _BgpNmEntEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 1, 1)
)
bgpNmEntEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpNmEntIndex"),
)
if mibBuilder.loadTexts:
    bgpNmEntEntry.setStatus("current")
_BgpNmEntIndex_Type = Unsigned32
_BgpNmEntIndex_Object = MibTableColumn
bgpNmEntIndex = _BgpNmEntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 1, 1, 1),
    _BgpNmEntIndex_Type()
)
bgpNmEntIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNmEntIndex.setStatus("current")
_BgpNmEntRowStatus_Type = RowStatus
_BgpNmEntRowStatus_Object = MibTableColumn
bgpNmEntRowStatus = _BgpNmEntRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 1, 1, 2),
    _BgpNmEntRowStatus_Type()
)
bgpNmEntRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmEntRowStatus.setStatus("current")


class _BgpNmEntAdminStatus_Type(BgpAdminStatus):
    """Custom type bgpNmEntAdminStatus based on BgpAdminStatus"""


_BgpNmEntAdminStatus_Object = MibTableColumn
bgpNmEntAdminStatus = _BgpNmEntAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 1, 1, 3),
    _BgpNmEntAdminStatus_Type()
)
bgpNmEntAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmEntAdminStatus.setStatus("current")
_BgpNmEntOperStatus_Type = BgpOperStatus
_BgpNmEntOperStatus_Object = MibTableColumn
bgpNmEntOperStatus = _BgpNmEntOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 1, 1, 4),
    _BgpNmEntOperStatus_Type()
)
bgpNmEntOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNmEntOperStatus.setStatus("current")
_BgpNmEntRmIndex_Type = Unsigned32
_BgpNmEntRmIndex_Object = MibTableColumn
bgpNmEntRmIndex = _BgpNmEntRmIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 1, 1, 5),
    _BgpNmEntRmIndex_Type()
)
bgpNmEntRmIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmEntRmIndex.setStatus("current")


class _BgpNmEntSckIndex_Type(Unsigned32):
    """Custom type bgpNmEntSckIndex based on Unsigned32"""
    defaultValue = 1


_BgpNmEntSckIndex_Object = MibTableColumn
bgpNmEntSckIndex = _BgpNmEntSckIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 1, 1, 6),
    _BgpNmEntSckIndex_Type()
)
bgpNmEntSckIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmEntSckIndex.setStatus("current")


class _BgpNmEntBfdEntityIndex_Type(Unsigned32):
    """Custom type bgpNmEntBfdEntityIndex based on Unsigned32"""
    defaultValue = 0


_BgpNmEntBfdEntityIndex_Object = MibTableColumn
bgpNmEntBfdEntityIndex = _BgpNmEntBfdEntityIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 1, 1, 7),
    _BgpNmEntBfdEntityIndex_Type()
)
bgpNmEntBfdEntityIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmEntBfdEntityIndex.setStatus("current")
_BgpNmListenTable_Object = MibTable
bgpNmListenTable = _BgpNmListenTable_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2)
)
if mibBuilder.loadTexts:
    bgpNmListenTable.setStatus("current")
_BgpNmListenEntry_Object = MibTableRow
bgpNmListenEntry = _BgpNmListenEntry_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2, 1)
)
bgpNmListenEntry.setIndexNames(
    (0, "DC-BGP-MIB", "bgpNmEntIndex"),
    (0, "DC-BGP-MIB", "bgpNmListenIndex"),
)
if mibBuilder.loadTexts:
    bgpNmListenEntry.setStatus("current")
_BgpNmListenIndex_Type = Unsigned32
_BgpNmListenIndex_Object = MibTableColumn
bgpNmListenIndex = _BgpNmListenIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2, 1, 2),
    _BgpNmListenIndex_Type()
)
bgpNmListenIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bgpNmListenIndex.setStatus("current")
_BgpNmListenRowStatus_Type = RowStatus
_BgpNmListenRowStatus_Object = MibTableColumn
bgpNmListenRowStatus = _BgpNmListenRowStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2, 1, 3),
    _BgpNmListenRowStatus_Type()
)
bgpNmListenRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmListenRowStatus.setStatus("current")


class _BgpNmListenAdminStatus_Type(BgpAdminStatus):
    """Custom type bgpNmListenAdminStatus based on BgpAdminStatus"""


_BgpNmListenAdminStatus_Object = MibTableColumn
bgpNmListenAdminStatus = _BgpNmListenAdminStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2, 1, 4),
    _BgpNmListenAdminStatus_Type()
)
bgpNmListenAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmListenAdminStatus.setStatus("current")
_BgpNmListenOperStatus_Type = BgpOperStatus
_BgpNmListenOperStatus_Object = MibTableColumn
bgpNmListenOperStatus = _BgpNmListenOperStatus_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2, 1, 5),
    _BgpNmListenOperStatus_Type()
)
bgpNmListenOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bgpNmListenOperStatus.setStatus("current")
_BgpNmListenAddrType_Type = InetAddressType
_BgpNmListenAddrType_Object = MibTableColumn
bgpNmListenAddrType = _BgpNmListenAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2, 1, 6),
    _BgpNmListenAddrType_Type()
)
bgpNmListenAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmListenAddrType.setStatus("current")


class _BgpNmListenAddr_Type(InetAddress):
    """Custom type bgpNmListenAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpNmListenAddr_Type.__name__ = "InetAddress"
_BgpNmListenAddr_Object = MibTableColumn
bgpNmListenAddr = _BgpNmListenAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2, 1, 7),
    _BgpNmListenAddr_Type()
)
bgpNmListenAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmListenAddr.setStatus("current")


class _BgpNmListenPort_Type(InetPortNumber):
    """Custom type bgpNmListenPort based on InetPortNumber"""
    defaultValue = 179


_BgpNmListenPort_Object = MibTableColumn
bgpNmListenPort = _BgpNmListenPort_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2, 1, 8),
    _BgpNmListenPort_Type()
)
bgpNmListenPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmListenPort.setStatus("current")


class _BgpNmListenAcceptAll_Type(TruthValue):
    """Custom type bgpNmListenAcceptAll based on TruthValue"""


_BgpNmListenAcceptAll_Object = MibTableColumn
bgpNmListenAcceptAll = _BgpNmListenAcceptAll_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2, 1, 9),
    _BgpNmListenAcceptAll_Type()
)
bgpNmListenAcceptAll.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmListenAcceptAll.setStatus("current")
_BgpNmListenAddrScopeId_Type = Unsigned32
_BgpNmListenAddrScopeId_Object = MibTableColumn
bgpNmListenAddrScopeId = _BgpNmListenAddrScopeId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 7, 2, 1, 10),
    _BgpNmListenAddrScopeId_Type()
)
bgpNmListenAddrScopeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bgpNmListenAddrScopeId.setStatus("current")
_BgpNotification_ObjectIdentity = ObjectIdentity
bgpNotification = _BgpNotification_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8)
)
_BgpNotificationEntry_ObjectIdentity = ObjectIdentity
bgpNotificationEntry = _BgpNotificationEntry_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8, 1)
)
_BgpNotifPeerLocalAddrType_Type = InetAddressType
_BgpNotifPeerLocalAddrType_Object = MibScalar
bgpNotifPeerLocalAddrType = _BgpNotifPeerLocalAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8, 1, 1),
    _BgpNotifPeerLocalAddrType_Type()
)
bgpNotifPeerLocalAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bgpNotifPeerLocalAddrType.setStatus("current")


class _BgpNotifPeerLocalAddr_Type(InetAddress):
    """Custom type bgpNotifPeerLocalAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpNotifPeerLocalAddr_Type.__name__ = "InetAddress"
_BgpNotifPeerLocalAddr_Object = MibScalar
bgpNotifPeerLocalAddr = _BgpNotifPeerLocalAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8, 1, 2),
    _BgpNotifPeerLocalAddr_Type()
)
bgpNotifPeerLocalAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bgpNotifPeerLocalAddr.setStatus("current")
_BgpNotifPeerRemoteAddrType_Type = InetAddressType
_BgpNotifPeerRemoteAddrType_Object = MibScalar
bgpNotifPeerRemoteAddrType = _BgpNotifPeerRemoteAddrType_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8, 1, 3),
    _BgpNotifPeerRemoteAddrType_Type()
)
bgpNotifPeerRemoteAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bgpNotifPeerRemoteAddrType.setStatus("current")


class _BgpNotifPeerRemoteAddr_Type(InetAddress):
    """Custom type bgpNotifPeerRemoteAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_BgpNotifPeerRemoteAddr_Type.__name__ = "InetAddress"
_BgpNotifPeerRemoteAddr_Object = MibScalar
bgpNotifPeerRemoteAddr = _BgpNotifPeerRemoteAddr_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8, 1, 4),
    _BgpNotifPeerRemoteAddr_Type()
)
bgpNotifPeerRemoteAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bgpNotifPeerRemoteAddr.setStatus("current")
_BgpNotifRmEntIndex_Type = Unsigned32
_BgpNotifRmEntIndex_Object = MibScalar
bgpNotifRmEntIndex = _BgpNotifRmEntIndex_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8, 1, 5),
    _BgpNotifRmEntIndex_Type()
)
bgpNotifRmEntIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bgpNotifRmEntIndex.setStatus("current")
_BgpNotifPeerLocalPort_Type = InetPortNumber
_BgpNotifPeerLocalPort_Object = MibScalar
bgpNotifPeerLocalPort = _BgpNotifPeerLocalPort_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8, 1, 6),
    _BgpNotifPeerLocalPort_Type()
)
bgpNotifPeerLocalPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bgpNotifPeerLocalPort.setStatus("current")
_BgpNotifPeerRemotePort_Type = InetPortNumber
_BgpNotifPeerRemotePort_Object = MibScalar
bgpNotifPeerRemotePort = _BgpNotifPeerRemotePort_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8, 1, 7),
    _BgpNotifPeerRemotePort_Type()
)
bgpNotifPeerRemotePort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bgpNotifPeerRemotePort.setStatus("current")
_BgpPeerLastFailureCause_Type = BgpPeerLastFailure
_BgpPeerLastFailureCause_Object = MibScalar
bgpPeerLastFailureCause = _BgpPeerLastFailureCause_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8, 1, 8),
    _BgpPeerLastFailureCause_Type()
)
bgpPeerLastFailureCause.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bgpPeerLastFailureCause.setStatus("current")
_BgpNotifPeerLocalAddrScopeId_Type = Unsigned32
_BgpNotifPeerLocalAddrScopeId_Object = MibScalar
bgpNotifPeerLocalAddrScopeId = _BgpNotifPeerLocalAddrScopeId_Object(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 8, 1, 9),
    _BgpNotifPeerLocalAddrScopeId_Type()
)
bgpNotifPeerLocalAddrScopeId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    bgpNotifPeerLocalAddrScopeId.setStatus("current")
_BgpConformance_ObjectIdentity = ObjectIdentity
bgpConformance = _BgpConformance_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9)
)
_BgpCompliances_ObjectIdentity = ObjectIdentity
bgpCompliances = _BgpCompliances_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 1)
)
_BgpGroups_ObjectIdentity = ObjectIdentity
bgpGroups = _BgpGroups_ObjectIdentity(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2)
)

# Managed Objects groups

bgpRmEntityGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 1)
)
bgpRmEntityGroup.setObjects(
      *(("DC-BGP-MIB", "bgpRmEntRowStatus"),
        ("DC-BGP-MIB", "bgpRmEntAdminStatus"),
        ("DC-BGP-MIB", "bgpRmEntOperStatus"),
        ("DC-BGP-MIB", "bgpRmEntAsSize"),
        ("DC-BGP-MIB", "bgpRmEntLocalAs"),
        ("DC-BGP-MIB", "bgpRmEntLocalIdentifier"),
        ("DC-BGP-MIB", "bgpRmEntI3JoinStatus"),
        ("DC-BGP-MIB", "bgpRmEntI3EntIndex"),
        ("DC-BGP-MIB", "bgpRmEntLocalMbrAs"),
        ("DC-BGP-MIB", "bgpRmEntIpv4ArinhJoinStatus"),
        ("DC-BGP-MIB", "bgpRmEntIpv4ArinhEntIndex"),
        ("DC-BGP-MIB", "bgpRmEntIpv6ArinhJoinStatus"),
        ("DC-BGP-MIB", "bgpRmEntIpv6ArinhEntIndex"),
        ("DC-BGP-MIB", "bgpRmEntNumAroRoutes"),
        ("DC-BGP-MIB", "bgpRmEntPeakNumAroRoutes"))
)
if mibBuilder.loadTexts:
    bgpRmEntityGroup.setStatus("current")

bgpRmAfmJoinGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 2)
)
bgpRmAfmJoinGroup.setObjects(
      *(("DC-BGP-MIB", "bgpRmAfmRowStatus"),
        ("DC-BGP-MIB", "bgpRmAfmAdminStatus"),
        ("DC-BGP-MIB", "bgpRmAfmOperStatus"),
        ("DC-BGP-MIB", "bgpRmAfmJoinStatus"),
        ("DC-BGP-MIB", "bgpRmAfmRestartTime"))
)
if mibBuilder.loadTexts:
    bgpRmAfmJoinGroup.setStatus("current")

bgpRmNmGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 3)
)
bgpRmNmGroup.setObjects(
    ("DC-BGP-MIB", "bgpRmNmJoinStatus")
)
if mibBuilder.loadTexts:
    bgpRmNmGroup.setStatus("current")

bgpNmMjGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 4)
)
bgpNmMjGroup.setObjects(
      *(("DC-BGP-MIB", "bgpNmMjJoinPartner"),
        ("DC-BGP-MIB", "bgpNmMjPartnerIndex"),
        ("DC-BGP-MIB", "bgpNmMjJoinStatus"))
)
if mibBuilder.loadTexts:
    bgpNmMjGroup.setStatus("current")

bgpNmEntGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 5)
)
bgpNmEntGroup.setObjects(
      *(("DC-BGP-MIB", "bgpNmEntRowStatus"),
        ("DC-BGP-MIB", "bgpNmEntAdminStatus"),
        ("DC-BGP-MIB", "bgpNmEntOperStatus"),
        ("DC-BGP-MIB", "bgpNmEntRmIndex"),
        ("DC-BGP-MIB", "bgpNmEntSckIndex"))
)
if mibBuilder.loadTexts:
    bgpNmEntGroup.setStatus("current")

bgpNmListenGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 6)
)
bgpNmListenGroup.setObjects(
      *(("DC-BGP-MIB", "bgpNmListenRowStatus"),
        ("DC-BGP-MIB", "bgpNmListenAdminStatus"),
        ("DC-BGP-MIB", "bgpNmListenOperStatus"),
        ("DC-BGP-MIB", "bgpNmListenAddrType"),
        ("DC-BGP-MIB", "bgpNmListenAddr"))
)
if mibBuilder.loadTexts:
    bgpNmListenGroup.setStatus("current")

bgpPeerGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 7)
)
bgpPeerGroup.setObjects(
      *(("DC-BGP-MIB", "bgpPeerIdentifier"),
        ("DC-BGP-MIB", "bgpPeerState"),
        ("DC-BGP-MIB", "bgpPeerRowStatus"),
        ("DC-BGP-MIB", "bgpPeerAdminStatus"),
        ("DC-BGP-MIB", "bgpPeerOperStatus"),
        ("DC-BGP-MIB", "bgpPeerLocalNm"),
        ("DC-BGP-MIB", "bgpPeerRemoteAs"),
        ("DC-BGP-MIB", "bgpPeerIndex"),
        ("DC-BGP-MIB", "bgpPeerCapsSupport"),
        ("DC-BGP-MIB", "bgpPeerLastError"),
        ("DC-BGP-MIB", "bgpPeerLastErrorDataLen"),
        ("DC-BGP-MIB", "bgpPeerLastErrorData"),
        ("DC-BGP-MIB", "bgpPeerFsmEstablishedTime"),
        ("DC-BGP-MIB", "bgpPeerInUpdatesElapsedTime"),
        ("DC-BGP-MIB", "bgpPeerHoldTime"),
        ("DC-BGP-MIB", "bgpPeerKeepAlive"),
        ("DC-BGP-MIB", "bgpPeerInUpdates"),
        ("DC-BGP-MIB", "bgpPeerOutUpdates"),
        ("DC-BGP-MIB", "bgpPeerInTotalMessages"),
        ("DC-BGP-MIB", "bgpPeerOutTotalMessages"),
        ("DC-BGP-MIB", "bgpPeerFsmEstablishedTransitions"),
        ("DC-BGP-MIB", "bgpPeerConnectRetryCount"),
        ("DC-BGP-MIB", "bgpPeerCapRcvdValue"),
        ("DC-BGP-MIB", "bgpPeerCapSentValue"),
        ("DC-BGP-MIB", "bgpPeerSelectedLocalAddrType"),
        ("DC-BGP-MIB", "bgpPeerSelectedLocalAddr"),
        ("DC-BGP-MIB", "bgpPeerSelectedLocalPort"),
        ("DC-BGP-MIB", "bgpPeerSelectedRemotePort"),
        ("DC-BGP-MIB", "bgpPeerBfdStatus"),
        ("DC-BGP-MIB", "bgpPrfxInPrfxes"),
        ("DC-BGP-MIB", "bgpPrfxInPrfxesAccepted"),
        ("DC-BGP-MIB", "bgpPrfxInPrfxesRejected"),
        ("DC-BGP-MIB", "bgpPrfxOutPrfxes"),
        ("DC-BGP-MIB", "bgpPrfxOutPrfxesAdvertised"),
        ("DC-BGP-MIB", "bgpPrfxInPrfxesFlapped"),
        ("DC-BGP-MIB", "bgpPrfxInPrfxesFlapSuppressed"),
        ("DC-BGP-MIB", "bgpPrfxInPrfxesFlapHistory"),
        ("DC-BGP-MIB", "bgpPrfxInPrfxesActive"),
        ("DC-BGP-MIB", "bgpPrfxCntrsUserData"),
        ("DC-BGP-MIB", "bgpPrfxInPrfxesDeniedByPol"),
        ("DC-BGP-MIB", "bgpPrfxNumLocRibRoutes"))
)
if mibBuilder.loadTexts:
    bgpPeerGroup.setStatus("current")

bgpPathAttributesGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 8)
)
bgpPathAttributesGroup.setObjects(
      *(("DC-BGP-MIB", "bgpNlriBest"),
        ("DC-BGP-MIB", "bgpNlriAsSize"),
        ("DC-BGP-MIB", "bgpNlriASPathStr"),
        ("DC-BGP-MIB", "bgpPathAttrOrigin"),
        ("DC-BGP-MIB", "bgpPathAttrNextHop"),
        ("DC-BGP-MIB", "bgpPathAttrMultiExitDisc"),
        ("DC-BGP-MIB", "bgpPathAttrLocalPref"),
        ("DC-BGP-MIB", "bgpPathAttrAtomicAggregate"),
        ("DC-BGP-MIB", "bgpPathAttrAggregatorAS"),
        ("DC-BGP-MIB", "bgpPathAttrAggregatorAddr"),
        ("DC-BGP-MIB", "bgpPathAttrCalcLocalPref"),
        ("DC-BGP-MIB", "bgpPathAttrOrigId"),
        ("DC-BGP-MIB", "bgpPathAttrWeight"),
        ("DC-BGP-MIB", "bgpFlapStatsConfig"),
        ("DC-BGP-MIB", "bgpFlapStatsPenalty"),
        ("DC-BGP-MIB", "bgpFlapStatsFlapcnt"),
        ("DC-BGP-MIB", "bgpFlapStatsSupprsd"),
        ("DC-BGP-MIB", "bgpFlapStatsTimeleft"),
        ("DC-BGP-MIB", "bgpPathAttrUnknownValue"),
        ("DC-BGP-MIB", "bgpPathAttrUnknownUserData"),
        ("DC-BGP-MIB", "bgpPathAttrClusterValue"),
        ("DC-BGP-MIB", "bgpPathAttrClusterUserData"),
        ("DC-BGP-MIB", "bgpPathAttrCommValue"),
        ("DC-BGP-MIB", "bgpPathAttrCommUserData"),
        ("DC-BGP-MIB", "bgpPathAttrExtCommValue"),
        ("DC-BGP-MIB", "bgpPathAttrExtCommUserData"),
        ("DC-BGP-MIB", "bgpNlriEcmp"),
        ("DC-BGP-MIB", "bgpPathAttrAsPathLimAs"),
        ("DC-BGP-MIB", "bgpPathAttrAsPathLimUpper"),
        ("DC-BGP-MIB", "bgpNlriIsActive"),
        ("DC-BGP-MIB", "bgpNlriStale"),
        ("DC-BGP-MIB", "bgpNlriFlapStartTime"),
        ("DC-BGP-MIB", "bgpNlriLinkLocalNextHop"),
        ("DC-BGP-MIB", "bgpNlriUserData"),
        ("DC-BGP-MIB", "bgpNlriPrefixBest"),
        ("DC-BGP-MIB", "bgpNlriPrefixAsSize"),
        ("DC-BGP-MIB", "bgpNlriPrefixASPathStr"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrOrigin"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrNextHop"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrMultExtDisc"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrLocalPref"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrAtomicAgg"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrAggAS"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrAggAddr"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrCalcLclPref"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrOrigId"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrWeight"),
        ("DC-BGP-MIB", "bgpNlriPrefixFlapStatsConfig"),
        ("DC-BGP-MIB", "bgpNlriPrefixFlapStatsPenalty"),
        ("DC-BGP-MIB", "bgpNlriPrefixFlapStatsFlapcnt"),
        ("DC-BGP-MIB", "bgpNlriPrefixFlapStatsSupprsd"),
        ("DC-BGP-MIB", "bgpNlriPrefixFlapStatsTimeleft"),
        ("DC-BGP-MIB", "bgpNlriPrefixFlapStatsCleardamp"),
        ("DC-BGP-MIB", "bgpNlriPrefixFlapStatsClearstat"),
        ("DC-BGP-MIB", "bgpNlriPrefixEcmp"),
        ("DC-BGP-MIB", "bgpNlriPrefixPathAttrAsPathLimAs"),
        ("DC-BGP-MIB", "bgpNlriPrefixPthAttAsPthLimUpper"),
        ("DC-BGP-MIB", "bgpNlriPrefixIsActive"),
        ("DC-BGP-MIB", "bgpNlriPrefixStale"),
        ("DC-BGP-MIB", "bgpNlriPrefixFlapStartTime"),
        ("DC-BGP-MIB", "bgpNlriPrefixUserData"),
        ("DC-BGP-MIB", "bgpNlriPrefixLinkLocalNextHop"))
)
if mibBuilder.loadTexts:
    bgpPathAttributesGroup.setStatus("current")

bgpPolicyGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 9)
)
bgpPolicyGroup.setObjects(
      *(("DC-BGP-MIB", "bgpRouteMapRowStatus"),
        ("DC-BGP-MIB", "bgpRouteMapMaAs"),
        ("DC-BGP-MIB", "bgpRouteMapMaComm"),
        ("DC-BGP-MIB", "bgpRouteMapMaExtComm"),
        ("DC-BGP-MIB", "bgpRouteMapMaAddr"),
        ("DC-BGP-MIB", "bgpRouteMapMaNext"),
        ("DC-BGP-MIB", "bgpRouteMapMaSource"),
        ("DC-BGP-MIB", "bgpRouteMapHitcnt"),
        ("DC-BGP-MIB", "bgpIpPreRowStatus"),
        ("DC-BGP-MIB", "bgpPeergrRowStatus"),
        ("DC-BGP-MIB", "bgpPeergrConfig"),
        ("DC-BGP-MIB", "bgpConfigRowStatus"),
        ("DC-BGP-MIB", "bgpFlapConfigRowStatus"),
        ("DC-BGP-MIB", "bgpAggrRowStatus"))
)
if mibBuilder.loadTexts:
    bgpPolicyGroup.setStatus("current")

bgpRmEntityOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 10)
)
bgpRmEntityOptionalGroup.setObjects(
      *(("DC-BGP-MIB", "bgpRmEntAsSize"),
        ("DC-BGP-MIB", "bgpRmEntClusterId"),
        ("DC-BGP-MIB", "bgpRmEntFlapDeltat"),
        ("DC-BGP-MIB", "bgpRmEntFlapReusemax"),
        ("DC-BGP-MIB", "bgpRmEntFlapReusesize"),
        ("DC-BGP-MIB", "bgpRmEntFlapReusearray"),
        ("DC-BGP-MIB", "bgpRmEntFlapFreemax"),
        ("DC-BGP-MIB", "bgpRmEntNoRefresh"),
        ("DC-BGP-MIB", "bgpRmEntDefLocalPref"),
        ("DC-BGP-MIB", "bgpRmEntAlwaysCompMed"),
        ("DC-BGP-MIB", "bgpRmEntPauseThreshold"),
        ("DC-BGP-MIB", "bgpRmEntAggregateMed"),
        ("DC-BGP-MIB", "bgpRmEntDeterministicMed"),
        ("DC-BGP-MIB", "bgpRmEntMaxIBgpEcmpRoutes"),
        ("DC-BGP-MIB", "bgpRmEntMaxEBgpEcmpRoutes"),
        ("DC-BGP-MIB", "bgpRmEntRestartSupported"),
        ("DC-BGP-MIB", "bgpRmEntMaxRestartTime"),
        ("DC-BGP-MIB", "bgpRmEntRecoveryTime"),
        ("DC-BGP-MIB", "bgpRmEntRestarting"),
        ("DC-BGP-MIB", "bgpRmEntSupportIpv6"),
        ("DC-BGP-MIB", "bgpRmEntStrictConfed"),
        ("DC-BGP-MIB", "bgpRmEntOrfSupported"),
        ("DC-BGP-MIB", "bgpRmEntCiscoPrefixSupported"),
        ("DC-BGP-MIB", "bgpRmEntSelectDeferTime"),
        ("DC-BGP-MIB", "bgpRmEntStalePathTime"),
        ("DC-BGP-MIB", "bgpRmEntNonPersistentAros"),
        ("DC-BGP-MIB", "bgpRmEntAroRouteThreshold"),
        ("DC-BGP-MIB", "bgpRmEntMaxActiveAroGroups"),
        ("DC-BGP-MIB", "bgpRmEntNumArosInGroup"),
        ("DC-BGP-MIB", "bgpRmEntClearStats"),
        ("DC-BGP-MIB", "bgpRmEntFastExtFallover"),
        ("DC-BGP-MIB", "bgpRmEntRemainDelayTime"),
        ("DC-BGP-MIB", "bgpRmEntPathAttrs"),
        ("DC-BGP-MIB", "bgpRmEntAggSplitHorizon"),
        ("DC-BGP-MIB", "bgpRmEntAggAdvSuppr"),
        ("DC-BGP-MIB", "bgpRmEntUpdateGroups"),
        ("DC-BGP-MIB", "bgpRmEntPhase3DelayTime"),
        ("DC-BGP-MIB", "bgpRmEntTrapOperState"))
)
if mibBuilder.loadTexts:
    bgpRmEntityOptionalGroup.setStatus("current")

bgpRmAfmJoinOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 11)
)
bgpRmAfmJoinOptionalGroup.setObjects(
      *(("DC-BGP-MIB", "bgpRmAfmPartnerIndex"),
        ("DC-BGP-MIB", "bgpRmAfmAfi"),
        ("DC-BGP-MIB", "bgpRmAfmSafi"))
)
if mibBuilder.loadTexts:
    bgpRmAfmJoinOptionalGroup.setStatus("current")

bgpNmListenOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 12)
)
bgpNmListenOptionalGroup.setObjects(
      *(("DC-BGP-MIB", "bgpNmListenPort"),
        ("DC-BGP-MIB", "bgpNmListenAcceptAll"),
        ("DC-BGP-MIB", "bgpNmListenAddrScopeId"))
)
if mibBuilder.loadTexts:
    bgpNmListenOptionalGroup.setStatus("current")

bgpPeerOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 13)
)
bgpPeerOptionalGroup.setObjects(
      *(("DC-BGP-MIB", "bgpPeerReflectorClient"),
        ("DC-BGP-MIB", "bgpPeerTrapEstab"),
        ("DC-BGP-MIB", "bgpPeerTrapBackw"),
        ("DC-BGP-MIB", "bgpPeerConnectRetryInterval"),
        ("DC-BGP-MIB", "bgpPeerHoldTimeConfigd"),
        ("DC-BGP-MIB", "bgpPeerKeepAliveConfigd"),
        ("DC-BGP-MIB", "bgpPeerMinASOriginationInterval"),
        ("DC-BGP-MIB", "bgpPeerMinRouteAdvertiseInterval"),
        ("DC-BGP-MIB", "bgpPeerClearCnts"),
        ("DC-BGP-MIB", "bgpPeerConfigPeergr"),
        ("DC-BGP-MIB", "bgpPeerConfigIndex"),
        ("DC-BGP-MIB", "bgpPeerConfigRtRefresh"),
        ("DC-BGP-MIB", "bgpPeerConfigMaxPrfx"),
        ("DC-BGP-MIB", "bgpPeerConfigDropWarn"),
        ("DC-BGP-MIB", "bgpPeerPassword"),
        ("DC-BGP-MIB", "bgpPeerTtl"),
        ("DC-BGP-MIB", "bgpPeerConfedMember"),
        ("DC-BGP-MIB", "bgpPeerConfigPassive"),
        ("DC-BGP-MIB", "bgpPeerConfigOpenDelay"),
        ("DC-BGP-MIB", "bgpPeerConfigIdleHold"),
        ("DC-BGP-MIB", "bgpPeerCheckFirstAsNum"),
        ("DC-BGP-MIB", "bgpPeerAggrInclConfedAS"),
        ("DC-BGP-MIB", "bgpPeerMinRouteWithdrawInterval"),
        ("DC-BGP-MIB", "bgpPeerStalePathTime"),
        ("DC-BGP-MIB", "bgpPeerCheckNextHop"),
        ("DC-BGP-MIB", "bgpPeerMaxOrfEntries"),
        ("DC-BGP-MIB", "bgpPeerOrfEntryCount"),
        ("DC-BGP-MIB", "bgpPeerPeeringType"),
        ("DC-BGP-MIB", "bgpPeerSoftResetWithStoredInfo"),
        ("DC-BGP-MIB", "bgpPeerAllowLocalAs"),
        ("DC-BGP-MIB", "bgpPeerDisableSenderLoopDetect"),
        ("DC-BGP-MIB", "bgpPeerDisableRouteRefresh"),
        ("DC-BGP-MIB", "bgpPeerFlapStatsClearStat"),
        ("DC-BGP-MIB", "bgpPeerFlapStatsClearMap"),
        ("DC-BGP-MIB", "bgpPeerLastErrorRcvd"),
        ("DC-BGP-MIB", "bgpPeerLastErrorRcvdTime"),
        ("DC-BGP-MIB", "bgpPeerLastErrorSent"),
        ("DC-BGP-MIB", "bgpPeerLastErrorSentTime"),
        ("DC-BGP-MIB", "bgpPeerLastState"),
        ("DC-BGP-MIB", "bgpPeerLastEvent"),
        ("DC-BGP-MIB", "bgpPeerCapsSent"),
        ("DC-BGP-MIB", "bgpPeerCapsRcvd"),
        ("DC-BGP-MIB", "bgpPeerCapsNegotiated"),
        ("DC-BGP-MIB", "bgpPeerRstrSupport"),
        ("DC-BGP-MIB", "bgpPeerRstrFamily"),
        ("DC-BGP-MIB", "bgpPeerRstrRestarting"),
        ("DC-BGP-MIB", "bgpPeerRstrStatus"),
        ("DC-BGP-MIB", "bgpPeerRstrRemTime"),
        ("DC-BGP-MIB", "bgpPeerRcvdMsgElapsedTime"),
        ("DC-BGP-MIB", "bgpPeerIdleHoldRemTime"),
        ("DC-BGP-MIB", "bgpPeerRouteRefrSent"),
        ("DC-BGP-MIB", "bgpPeerRouteRefrRcvd"),
        ("DC-BGP-MIB", "bgpPeerLastFailureCause"),
        ("DC-BGP-MIB", "bgpPeerNxtHopSlf"),
        ("DC-BGP-MIB", "bgpPeerThirdPtyNxtHop"),
        ("DC-BGP-MIB", "bgpPeerNxtHopPeer"),
        ("DC-BGP-MIB", "bgpPeerTrapPrefix"),
        ("DC-BGP-MIB", "bgpPeerConfigThreshold"),
        ("DC-BGP-MIB", "bgpPeerMaxPrfxHold"),
        ("DC-BGP-MIB", "bgpPeerBfdDesired"),
        ("DC-BGP-MIB", "bgpPeerCeaseErrorSubcode"),
        ("DC-BGP-MIB", "bgpPeerConfAltLocalAs"),
        ("DC-BGP-MIB", "bgpPeerSelectedLocalAs"),
        ("DC-BGP-MIB", "bgpPeerSelectedRemoteAs"),
        ("DC-BGP-MIB", "bgpPeerInPrfxes"),
        ("DC-BGP-MIB", "bgpPeerOutPrfxes"),
        ("DC-BGP-MIB", "bgpPeerOutPrfxesAdvertised"),
        ("DC-BGP-MIB", "bgpPeerTrapGrHelperState"),
        ("DC-BGP-MIB", "bgpPeerEnableAttributeDiscard"))
)
if mibBuilder.loadTexts:
    bgpPeerOptionalGroup.setStatus("current")

bgpPathAttributesOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 14)
)
bgpPathAttributesOptionalGroup.setObjects(
      *(("DC-BGP-MIB", "bgpFlapStatsCleardamp"),
        ("DC-BGP-MIB", "bgpFlapStatsClearstat"))
)
if mibBuilder.loadTexts:
    bgpPathAttributesOptionalGroup.setStatus("current")

bgpPolicyOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 15)
)
bgpPolicyOptionalGroup.setObjects(
      *(("DC-BGP-MIB", "bgpRouteMapMaAfi"),
        ("DC-BGP-MIB", "bgpRouteMapMaAfiDef"),
        ("DC-BGP-MIB", "bgpRouteMapMaSafi"),
        ("DC-BGP-MIB", "bgpRouteMapMaSafiDef"),
        ("DC-BGP-MIB", "bgpRouteMapMaMed"),
        ("DC-BGP-MIB", "bgpRouteMapMaMedDef"),
        ("DC-BGP-MIB", "bgpRouteMapMaUser"),
        ("DC-BGP-MIB", "bgpRouteMapSeAs"),
        ("DC-BGP-MIB", "bgpRouteMapSeAsAct"),
        ("DC-BGP-MIB", "bgpRouteMapSeComm"),
        ("DC-BGP-MIB", "bgpRouteMapSeCommAct"),
        ("DC-BGP-MIB", "bgpRouteMapSeExtComm"),
        ("DC-BGP-MIB", "bgpRouteMapSeExtCommAct"),
        ("DC-BGP-MIB", "bgpRouteMapSeLocPref"),
        ("DC-BGP-MIB", "bgpRouteMapSeLocPrefDef"),
        ("DC-BGP-MIB", "bgpRouteMapSeMed"),
        ("DC-BGP-MIB", "bgpRouteMapSeMedDef"),
        ("DC-BGP-MIB", "bgpRouteMapSeNext"),
        ("DC-BGP-MIB", "bgpRouteMapSeOrigin"),
        ("DC-BGP-MIB", "bgpRouteMapSeOriginDef"),
        ("DC-BGP-MIB", "bgpRouteMapSeWeight"),
        ("DC-BGP-MIB", "bgpRouteMapSeWeightDef"),
        ("DC-BGP-MIB", "bgpRouteMapSeFlap"),
        ("DC-BGP-MIB", "bgpRouteMapSeUser"),
        ("DC-BGP-MIB", "bgpRouteMapClearcnt"),
        ("DC-BGP-MIB", "bgpRouteMapUserInfo"),
        ("DC-BGP-MIB", "bgpRouteMapType"),
        ("DC-BGP-MIB", "bgpRouteMapContinue"),
        ("DC-BGP-MIB", "bgpRouteMapOrfAssoc"),
        ("DC-BGP-MIB", "bgpRouteMapSeAsLimUpper"),
        ("DC-BGP-MIB", "bgpRouteMapSeAsLimDef"),
        ("DC-BGP-MIB", "bgpRouteMapMaOrigin"),
        ("DC-BGP-MIB", "bgpRouteMapMaOriginDef"),
        ("DC-BGP-MIB", "bgpRouteMapSeMedDelta"),
        ("DC-BGP-MIB", "bgpRouteMapSeMedDeltaTyp"),
        ("DC-BGP-MIB", "bgpRouteMapSeMedIgp"),
        ("DC-BGP-MIB", "bgpRouteMapSeAsPrependCount"),
        ("DC-BGP-MIB", "bgpRouteMapSeAsPrependSize"),
        ("DC-BGP-MIB", "bgpRouteMapSeAsPrependAsVals"),
        ("DC-BGP-MIB", "bgpRouteMapMaAnd"),
        ("DC-BGP-MIB", "bgpIpPreAfi"),
        ("DC-BGP-MIB", "bgpIpPreSafi"),
        ("DC-BGP-MIB", "bgpIpPreAddr"),
        ("DC-BGP-MIB", "bgpIpPreLen"),
        ("DC-BGP-MIB", "bgpIpPreGe"),
        ("DC-BGP-MIB", "bgpIpPreLe"),
        ("DC-BGP-MIB", "bgpIpPreType"),
        ("DC-BGP-MIB", "bgpPeergrArea"),
        ("DC-BGP-MIB", "bgpPeergrAggrConfedAS"),
        ("DC-BGP-MIB", "bgpPeergrSoftResetWithStoredInfo"),
        ("DC-BGP-MIB", "bgpPeergrAllowLocalAs"),
        ("DC-BGP-MIB", "bgpPeergrDisableSenderLoopDetect"),
        ("DC-BGP-MIB", "bgpPeergrNxtHopSlf"),
        ("DC-BGP-MIB", "bgpPeergrThirdPtyNxtHop"),
        ("DC-BGP-MIB", "bgpPeergrNxtHopPeer"),
        ("DC-BGP-MIB", "bgpPeergrEnableAttributeDiscard"),
        ("DC-BGP-MIB", "bgpConfigImportMap"),
        ("DC-BGP-MIB", "bgpConfigExportMap"),
        ("DC-BGP-MIB", "bgpConfigAdvertiseMap"),
        ("DC-BGP-MIB", "bgpConfigNonExistMap"),
        ("DC-BGP-MIB", "bgpConfigBlockCondAdv"),
        ("DC-BGP-MIB", "bgpConfigRemove"),
        ("DC-BGP-MIB", "bgpConfigCondAdvOn"),
        ("DC-BGP-MIB", "bgpFlapConfigCut"),
        ("DC-BGP-MIB", "bgpFlapConfigReuse"),
        ("DC-BGP-MIB", "bgpFlapConfigThold"),
        ("DC-BGP-MIB", "bgpFlapConfigDecayok"),
        ("DC-BGP-MIB", "bgpFlapConfigDecayng"),
        ("DC-BGP-MIB", "bgpFlapConfigTmaxok"),
        ("DC-BGP-MIB", "bgpFlapConfigTmaxng"),
        ("DC-BGP-MIB", "bgpAggrOptions"),
        ("DC-BGP-MIB", "bgpAggrSuppressMap"),
        ("DC-BGP-MIB", "bgpAggrAdvertiseMap"),
        ("DC-BGP-MIB", "bgpAggrAttributeMap"),
        ("DC-BGP-MIB", "bgpAggrPermanent"))
)
if mibBuilder.loadTexts:
    bgpPolicyOptionalGroup.setStatus("current")

bgpObsoleteGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 17)
)
bgpObsoleteGroup.setObjects(
      *(("DC-BGP-MIB", "bgpConfigRtgrimpe"),
        ("DC-BGP-MIB", "bgpConfigRtgrimde"),
        ("DC-BGP-MIB", "bgpConfigRtgrexpe"),
        ("DC-BGP-MIB", "bgpConfigRtgrexde"),
        ("DC-BGP-MIB", "bgpConfigDefImport"),
        ("DC-BGP-MIB", "bgpConfigDefExport"),
        ("DC-BGP-MIB", "bgpConfigNxtHopSlf"),
        ("DC-BGP-MIB", "bgpConfigThirdPtyNxtHop"),
        ("DC-BGP-MIB", "bgpConfigNxtHopPeer"),
        ("DC-BGP-MIB", "bgpRmEntNhrJoinStatus"),
        ("DC-BGP-MIB", "bgpRmEntNhrEntIndex"),
        ("DC-BGP-MIB", "bgpRmEntIpv4UniFwdPrsrvd"),
        ("DC-BGP-MIB", "bgpRmEntIpv4MultiFwdPrsrvd"),
        ("DC-BGP-MIB", "bgpRmEntVpnIpv4FwdPrsrvd"),
        ("DC-BGP-MIB", "bgpRmEntIpv4MultiSupport"),
        ("DC-BGP-MIB", "bgpRmEntVpnIpv4Support"))
)
if mibBuilder.loadTexts:
    bgpObsoleteGroup.setStatus("obsolete")

bgpRmAfiSafiGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 18)
)
bgpRmAfiSafiGroup.setObjects(
      *(("DC-BGP-MIB", "bgpRmAfiSafiAdminStatus"),
        ("DC-BGP-MIB", "bgpRmAfiSafiLocRibBlocked"),
        ("DC-BGP-MIB", "bgpRmAfiSafiAdvertiseInactive"),
        ("DC-BGP-MIB", "bgpRmAfiSafiIbgpPrefixes"),
        ("DC-BGP-MIB", "bgpRmAfiSafiEbgpPrefixes"),
        ("DC-BGP-MIB", "bgpRmAfiSafiRedistPrefixes"),
        ("DC-BGP-MIB", "bgpRmAfiSafiInPrfxes"),
        ("DC-BGP-MIB", "bgpRmAfiSafiInPrfxesAccepted"),
        ("DC-BGP-MIB", "bgpRmAfiSafiInPrfxesRejected"),
        ("DC-BGP-MIB", "bgpRmAfiSafiOutPrfxes"),
        ("DC-BGP-MIB", "bgpRmAfiSafiOutPrfxesAdvertised"),
        ("DC-BGP-MIB", "bgpRmAfiSafiInPrfxesActive"),
        ("DC-BGP-MIB", "bgpRmAfiSafiInPrfxesFlapped"),
        ("DC-BGP-MIB", "bgpRmAfiSafiInPrfxesFlapSuppr"),
        ("DC-BGP-MIB", "bgpRmAfiSafiInPrfxesFlapHistory"),
        ("DC-BGP-MIB", "bgpRmAfiSafiDefaultImportRule"),
        ("DC-BGP-MIB", "bgpRmAfiSafiUserData"),
        ("DC-BGP-MIB", "bgpRmAfiSafiInPrfxesDeniedByPol"),
        ("DC-BGP-MIB", "bgpRmAfiSafiNumLocRibRoutes"),
        ("DC-BGP-MIB", "bgpRmAfiSafiNextHopSafi"))
)
if mibBuilder.loadTexts:
    bgpRmAfiSafiGroup.setStatus("current")

bgpRmAfiSafiOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 19)
)
bgpRmAfiSafiOptionalGroup.setObjects(
      *(("DC-BGP-MIB", "bgpRmAfiSafiStateKept"),
        ("DC-BGP-MIB", "bgpRmAfiSafiAfmRequired"))
)
if mibBuilder.loadTexts:
    bgpRmAfiSafiOptionalGroup.setStatus("current")

bgpAdjRibOutGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 20)
)
bgpAdjRibOutGroup.setObjects(
      *(("DC-BGP-MIB", "bgpAdjRibOutAdvertStatus"),
        ("DC-BGP-MIB", "bgpAdjRibOutLocalAggrType"),
        ("DC-BGP-MIB", "bgpAdjRibOutAsSize"),
        ("DC-BGP-MIB", "bgpAdjRibOutASPathStr"),
        ("DC-BGP-MIB", "bgpAdjRibOutOrigin"),
        ("DC-BGP-MIB", "bgpAdjRibOutNextHop"),
        ("DC-BGP-MIB", "bgpAdjRibOutMultiExitDisc"),
        ("DC-BGP-MIB", "bgpAdjRibOutLocalPref"),
        ("DC-BGP-MIB", "bgpAdjRibOutAtomicAggregate"),
        ("DC-BGP-MIB", "bgpAdjRibOutAggregatorAS"),
        ("DC-BGP-MIB", "bgpAdjRibOutAggregatorAddr"),
        ("DC-BGP-MIB", "bgpAdjRibOutOrigId"),
        ("DC-BGP-MIB", "bgpAdjRibOutAsLimAs"),
        ("DC-BGP-MIB", "bgpAdjRibOutAsLimUpper"),
        ("DC-BGP-MIB", "bgpAdjRibOutUserData"),
        ("DC-BGP-MIB", "bgpAdjRibOutEcmp"),
        ("DC-BGP-MIB", "bgpAdjRibOutStale"),
        ("DC-BGP-MIB", "bgpAdjRibOutLinkLocalNextHop"))
)
if mibBuilder.loadTexts:
    bgpAdjRibOutGroup.setStatus("current")

bgpOrfCapabilityGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 21)
)
bgpOrfCapabilityGroup.setObjects(
    ("DC-BGP-MIB", "bgpOrfCapabilityAdminStatus")
)
if mibBuilder.loadTexts:
    bgpOrfCapabilityGroup.setStatus("current")

bgpOrfCapabilityOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 22)
)
bgpOrfCapabilityOptionalGroup.setObjects(
    ("DC-BGP-MIB", "bgpOrfCapabilitySendReceive")
)
if mibBuilder.loadTexts:
    bgpOrfCapabilityOptionalGroup.setStatus("current")

bgpPeerAfiSafiOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 23)
)
bgpPeerAfiSafiOptionalGroup.setObjects(
      *(("DC-BGP-MIB", "bgpPeerAfiSafiDisable"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiConfigRtRefresh"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiAllowLocalAs"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiDisableSndLpDetect"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiNxtHopSlf"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiOrigDefault"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiOrigDefaultRtMap"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiSoftResetStore"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiConfigMaxPrfx"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiConfigDropWarn"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiTrapPrefix"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiConfigThreshold"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiMaxPrfxHold"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiMaxOrfEntries"))
)
if mibBuilder.loadTexts:
    bgpPeerAfiSafiOptionalGroup.setStatus("current")

bgpPeergrAfiSafiOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 24)
)
bgpPeergrAfiSafiOptionalGroup.setObjects(
      *(("DC-BGP-MIB", "bgpPeergrAfiSafiAllowLocalAs"),
        ("DC-BGP-MIB", "bgpPeergrAfiSafiDisSndLpDetect"),
        ("DC-BGP-MIB", "bgpPeergrAfiSafiNxtHopSlf"),
        ("DC-BGP-MIB", "bgpPeergrAfiSafiOrigDefault"),
        ("DC-BGP-MIB", "bgpPeergrAfiSafiOrigDefaultRtMap"),
        ("DC-BGP-MIB", "bgpPeergrAfiSafiSoftResetStore"))
)
if mibBuilder.loadTexts:
    bgpPeergrAfiSafiOptionalGroup.setStatus("current")

bgpPeerOrfCapabilityGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 25)
)
bgpPeerOrfCapabilityGroup.setObjects(
    ("DC-BGP-MIB", "bgpPeerOrfCapabilityAdminStatus")
)
if mibBuilder.loadTexts:
    bgpPeerOrfCapabilityGroup.setStatus("current")

bgpPeerOrfCapabilityOptionalGrp = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 26)
)
bgpPeerOrfCapabilityOptionalGrp.setObjects(
    ("DC-BGP-MIB", "bgpPeerOrfCapabilitySendReceive")
)
if mibBuilder.loadTexts:
    bgpPeerOrfCapabilityOptionalGrp.setStatus("current")

bgpRmArinhJoinGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 27)
)
bgpRmArinhJoinGroup.setObjects(
      *(("DC-BGP-MIB", "bgpRmArinhJoinStatus"),
        ("DC-BGP-MIB", "bgpRmArinhEntIndex"))
)
if mibBuilder.loadTexts:
    bgpRmArinhJoinGroup.setStatus("current")

bgpNmEntOptionalGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 28)
)
bgpNmEntOptionalGroup.setObjects(
    ("DC-BGP-MIB", "bgpNmEntBfdEntityIndex")
)
if mibBuilder.loadTexts:
    bgpNmEntOptionalGroup.setStatus("current")

bgpNotificationObjectGroup = ObjectGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 29)
)
bgpNotificationObjectGroup.setObjects(
      *(("DC-BGP-MIB", "bgpNotifPeerLocalAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrType"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddrType"),
        ("DC-BGP-MIB", "bgpNotifRmEntIndex"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalPort"),
        ("DC-BGP-MIB", "bgpNotifPeerRemotePort"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrScopeId"))
)
if mibBuilder.loadTexts:
    bgpNotificationObjectGroup.setStatus("current")


# Notification objects

bgpTrapData = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 1, 0, 1)
)
bgpTrapData.setObjects(
      *(("DC-BGP-MIB", "bgpNotifPeerLocalAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrType"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddrType"),
        ("DC-BGP-MIB", "bgpPeerLastError"),
        ("DC-BGP-MIB", "bgpPeerState"),
        ("DC-BGP-MIB", "bgpPeerLocalNm"),
        ("DC-BGP-MIB", "bgpNotifRmEntIndex"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalPort"),
        ("DC-BGP-MIB", "bgpNotifPeerRemotePort"),
        ("DC-BGP-MIB", "bgpPeerLastFailureCause"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrScopeId"),
        ("DC-BGP-MIB", "bgpPeerRstrStatus"))
)
if mibBuilder.loadTexts:
    bgpTrapData.setStatus(
        "current"
    )

bgpEntTrapData = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 1, 0, 2)
)
bgpEntTrapData.setObjects(
      *(("DC-BGP-MIB", "bgpNotifRmEntIndex"),
        ("DC-BGP-MIB", "bgpRmEntOperStatus"))
)
if mibBuilder.loadTexts:
    bgpEntTrapData.setStatus(
        "current"
    )

bgpPeerSessionEstablished = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 1, 0, 3)
)
bgpPeerSessionEstablished.setObjects(
      *(("DC-BGP-MIB", "bgpNotifPeerLocalAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrType"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddrType"),
        ("DC-BGP-MIB", "bgpPeerLastError"),
        ("DC-BGP-MIB", "bgpPeerState"),
        ("DC-BGP-MIB", "bgpPeerLocalNm"),
        ("DC-BGP-MIB", "bgpNotifRmEntIndex"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalPort"),
        ("DC-BGP-MIB", "bgpNotifPeerRemotePort"),
        ("DC-BGP-MIB", "bgpPeerLastFailureCause"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrScopeId"),
        ("DC-BGP-MIB", "bgpPeerRstrStatus"))
)
if mibBuilder.loadTexts:
    bgpPeerSessionEstablished.setStatus(
        "current"
    )

bgpPeerSessionBackward = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 1, 0, 4)
)
bgpPeerSessionBackward.setObjects(
      *(("DC-BGP-MIB", "bgpNotifPeerLocalAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrType"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddrType"),
        ("DC-BGP-MIB", "bgpPeerLastError"),
        ("DC-BGP-MIB", "bgpPeerState"),
        ("DC-BGP-MIB", "bgpPeerLocalNm"),
        ("DC-BGP-MIB", "bgpNotifRmEntIndex"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalPort"),
        ("DC-BGP-MIB", "bgpNotifPeerRemotePort"),
        ("DC-BGP-MIB", "bgpPeerLastFailureCause"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrScopeId"),
        ("DC-BGP-MIB", "bgpPeerRstrStatus"))
)
if mibBuilder.loadTexts:
    bgpPeerSessionBackward.setStatus(
        "current"
    )

bgpPeerAfiSafiMaxPrefix = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 1, 0, 5)
)
bgpPeerAfiSafiMaxPrefix.setObjects(
      *(("DC-BGP-MIB", "bgpNotifPeerLocalAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrType"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddrType"),
        ("DC-BGP-MIB", "bgpPeerLastError"),
        ("DC-BGP-MIB", "bgpPeerState"),
        ("DC-BGP-MIB", "bgpPeerLocalNm"),
        ("DC-BGP-MIB", "bgpNotifRmEntIndex"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalPort"),
        ("DC-BGP-MIB", "bgpNotifPeerRemotePort"),
        ("DC-BGP-MIB", "bgpPeerLastFailureCause"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrScopeId"),
        ("DC-BGP-MIB", "bgpPeerRstrStatus"))
)
if mibBuilder.loadTexts:
    bgpPeerAfiSafiMaxPrefix.setStatus(
        "current"
    )

bgpPeerAfiSafiPrefixThreshold = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 1, 0, 6)
)
bgpPeerAfiSafiPrefixThreshold.setObjects(
      *(("DC-BGP-MIB", "bgpNotifPeerLocalAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrType"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddrType"),
        ("DC-BGP-MIB", "bgpPeerLastError"),
        ("DC-BGP-MIB", "bgpPeerState"),
        ("DC-BGP-MIB", "bgpPeerLocalNm"),
        ("DC-BGP-MIB", "bgpNotifRmEntIndex"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalPort"),
        ("DC-BGP-MIB", "bgpNotifPeerRemotePort"),
        ("DC-BGP-MIB", "bgpPeerLastFailureCause"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrScopeId"),
        ("DC-BGP-MIB", "bgpPeerRstrStatus"))
)
if mibBuilder.loadTexts:
    bgpPeerAfiSafiPrefixThreshold.setStatus(
        "current"
    )

bgpEntOperStatusChange = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 1, 0, 7)
)
bgpEntOperStatusChange.setObjects(
      *(("DC-BGP-MIB", "bgpNotifRmEntIndex"),
        ("DC-BGP-MIB", "bgpRmEntOperStatus"))
)
if mibBuilder.loadTexts:
    bgpEntOperStatusChange.setStatus(
        "current"
    )

bgpEntRestartHelperChange = NotificationType(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 1, 0, 8)
)
bgpEntRestartHelperChange.setObjects(
      *(("DC-BGP-MIB", "bgpNotifPeerLocalAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrType"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddr"),
        ("DC-BGP-MIB", "bgpNotifPeerRemoteAddrType"),
        ("DC-BGP-MIB", "bgpPeerLastError"),
        ("DC-BGP-MIB", "bgpPeerState"),
        ("DC-BGP-MIB", "bgpPeerLocalNm"),
        ("DC-BGP-MIB", "bgpNotifRmEntIndex"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalPort"),
        ("DC-BGP-MIB", "bgpNotifPeerRemotePort"),
        ("DC-BGP-MIB", "bgpPeerLastFailureCause"),
        ("DC-BGP-MIB", "bgpNotifPeerLocalAddrScopeId"),
        ("DC-BGP-MIB", "bgpPeerRstrStatus"))
)
if mibBuilder.loadTexts:
    bgpEntRestartHelperChange.setStatus(
        "current"
    )


# Notifications groups

bgpNotificationsGroup = NotificationGroup(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 2, 16)
)
bgpNotificationsGroup.setObjects(
      *(("DC-BGP-MIB", "bgpTrapData"),
        ("DC-BGP-MIB", "bgpEntTrapData"),
        ("DC-BGP-MIB", "bgpPeerSessionEstablished"),
        ("DC-BGP-MIB", "bgpPeerSessionBackward"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiMaxPrefix"),
        ("DC-BGP-MIB", "bgpPeerAfiSafiPrefixThreshold"),
        ("DC-BGP-MIB", "bgpEntOperStatusChange"),
        ("DC-BGP-MIB", "bgpEntRestartHelperChange"))
)
if mibBuilder.loadTexts:
    bgpNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

bgpCompliance = ModuleCompliance(
    (1, 2, 826, 0, 1, 1578918, 5, 65, 1, 9, 1, 1)
)
if mibBuilder.loadTexts:
    bgpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DC-BGP-MIB",
    **{"BgpIdentifier": BgpIdentifier,
       "BgpAfi": BgpAfi,
       "BgpSafi": BgpSafi,
       "BgpAutonomousSystemNumber": BgpAutonomousSystemNumber,
       "BgpAsSize": BgpAsSize,
       "BgpAdminStatus": BgpAdminStatus,
       "BgpOperStatus": BgpOperStatus,
       "BgpOriginCode": BgpOriginCode,
       "BgpMedDeltaType": BgpMedDeltaType,
       "BgpIpMatchType": BgpIpMatchType,
       "BgpPermitOrDeny": BgpPermitOrDeny,
       "BgpDropOrWarn": BgpDropOrWarn,
       "BgpIbgpOrEbgp": BgpIbgpOrEbgp,
       "BgpPeerOrAfm": BgpPeerOrAfm,
       "BgpAsPathAction": BgpAsPathAction,
       "BgpAggregateOptions": BgpAggregateOptions,
       "BgpMjStatus": BgpMjStatus,
       "BgpSjStatus": BgpSjStatus,
       "BgpPeerStates": BgpPeerStates,
       "BgpPeerEvents": BgpPeerEvents,
       "BgpCapabilities": BgpCapabilities,
       "BgpPeerRestartSupport": BgpPeerRestartSupport,
       "BgpPeerRestartStatus": BgpPeerRestartStatus,
       "BgpPeerLastFailure": BgpPeerLastFailure,
       "BgpCeaseErrorSubcode": BgpCeaseErrorSubcode,
       "BgpPeerReflectorClientType": BgpPeerReflectorClientType,
       "BgpComponentId": BgpComponentId,
       "BgpCommunity": BgpCommunity,
       "BgpExtendedCommunity": BgpExtendedCommunity,
       "BgpCommunityAction": BgpCommunityAction,
       "BgpPathAttrAtomicAggPresence": BgpPathAttrAtomicAggPresence,
       "BgpOrfType": BgpOrfType,
       "BgpOrfSendReceive": BgpOrfSendReceive,
       "BgpOrfAssociation": BgpOrfAssociation,
       "BgpPeeringType": BgpPeeringType,
       "BgpAfiSafiBits": BgpAfiSafiBits,
       "BgpNlriIsActiveFlag": BgpNlriIsActiveFlag,
       "bgpMib": bgpMib,
       "bgpNotifications": bgpNotifications,
       "bgpBaseNotifications": bgpBaseNotifications,
       "bgpTrapData": bgpTrapData,
       "bgpEntTrapData": bgpEntTrapData,
       "bgpPeerSessionEstablished": bgpPeerSessionEstablished,
       "bgpPeerSessionBackward": bgpPeerSessionBackward,
       "bgpPeerAfiSafiMaxPrefix": bgpPeerAfiSafiMaxPrefix,
       "bgpPeerAfiSafiPrefixThreshold": bgpPeerAfiSafiPrefixThreshold,
       "bgpEntOperStatusChange": bgpEntOperStatusChange,
       "bgpEntRestartHelperChange": bgpEntRestartHelperChange,
       "bgpRm": bgpRm,
       "bgpRmEntTable": bgpRmEntTable,
       "bgpRmEntEntry": bgpRmEntEntry,
       "bgpRmEntIndex": bgpRmEntIndex,
       "bgpRmEntRowStatus": bgpRmEntRowStatus,
       "bgpRmEntAdminStatus": bgpRmEntAdminStatus,
       "bgpRmEntOperStatus": bgpRmEntOperStatus,
       "bgpRmEntAsSize": bgpRmEntAsSize,
       "bgpRmEntLocalAs": bgpRmEntLocalAs,
       "bgpRmEntLocalMbrAs": bgpRmEntLocalMbrAs,
       "bgpRmEntLocalIdentifier": bgpRmEntLocalIdentifier,
       "bgpRmEntClusterId": bgpRmEntClusterId,
       "bgpRmEntIpv4MultiSupport": bgpRmEntIpv4MultiSupport,
       "bgpRmEntVpnIpv4Support": bgpRmEntVpnIpv4Support,
       "bgpRmEntFlapDeltat": bgpRmEntFlapDeltat,
       "bgpRmEntFlapReusemax": bgpRmEntFlapReusemax,
       "bgpRmEntFlapReusesize": bgpRmEntFlapReusesize,
       "bgpRmEntFlapReusearray": bgpRmEntFlapReusearray,
       "bgpRmEntFlapFreemax": bgpRmEntFlapFreemax,
       "bgpRmEntNoRefresh": bgpRmEntNoRefresh,
       "bgpRmEntDefLocalPref": bgpRmEntDefLocalPref,
       "bgpRmEntAlwaysCompMed": bgpRmEntAlwaysCompMed,
       "bgpRmEntAggregateMed": bgpRmEntAggregateMed,
       "bgpRmEntDeterministicMed": bgpRmEntDeterministicMed,
       "bgpRmEntNhrJoinStatus": bgpRmEntNhrJoinStatus,
       "bgpRmEntNhrEntIndex": bgpRmEntNhrEntIndex,
       "bgpRmEntI3JoinStatus": bgpRmEntI3JoinStatus,
       "bgpRmEntI3EntIndex": bgpRmEntI3EntIndex,
       "bgpRmEntPauseThreshold": bgpRmEntPauseThreshold,
       "bgpRmEntMaxIBgpEcmpRoutes": bgpRmEntMaxIBgpEcmpRoutes,
       "bgpRmEntMaxEBgpEcmpRoutes": bgpRmEntMaxEBgpEcmpRoutes,
       "bgpRmEntRestartSupported": bgpRmEntRestartSupported,
       "bgpRmEntMaxRestartTime": bgpRmEntMaxRestartTime,
       "bgpRmEntRecoveryTime": bgpRmEntRecoveryTime,
       "bgpRmEntRestarting": bgpRmEntRestarting,
       "bgpRmEntIpv4UniFwdPrsrvd": bgpRmEntIpv4UniFwdPrsrvd,
       "bgpRmEntIpv4MultiFwdPrsrvd": bgpRmEntIpv4MultiFwdPrsrvd,
       "bgpRmEntVpnIpv4FwdPrsrvd": bgpRmEntVpnIpv4FwdPrsrvd,
       "bgpRmEntIpv4ArinhJoinStatus": bgpRmEntIpv4ArinhJoinStatus,
       "bgpRmEntIpv4ArinhEntIndex": bgpRmEntIpv4ArinhEntIndex,
       "bgpRmEntIpv6ArinhJoinStatus": bgpRmEntIpv6ArinhJoinStatus,
       "bgpRmEntIpv6ArinhEntIndex": bgpRmEntIpv6ArinhEntIndex,
       "bgpRmEntSupportIpv6": bgpRmEntSupportIpv6,
       "bgpRmEntStrictConfed": bgpRmEntStrictConfed,
       "bgpRmEntOrfSupported": bgpRmEntOrfSupported,
       "bgpRmEntCiscoPrefixSupported": bgpRmEntCiscoPrefixSupported,
       "bgpRmEntSelectDeferTime": bgpRmEntSelectDeferTime,
       "bgpRmEntStalePathTime": bgpRmEntStalePathTime,
       "bgpRmEntNonPersistentAros": bgpRmEntNonPersistentAros,
       "bgpRmEntAroRouteThreshold": bgpRmEntAroRouteThreshold,
       "bgpRmEntMaxActiveAroGroups": bgpRmEntMaxActiveAroGroups,
       "bgpRmEntNumArosInGroup": bgpRmEntNumArosInGroup,
       "bgpRmEntNumAroRoutes": bgpRmEntNumAroRoutes,
       "bgpRmEntPeakNumAroRoutes": bgpRmEntPeakNumAroRoutes,
       "bgpRmEntClearStats": bgpRmEntClearStats,
       "bgpRmEntFastExtFallover": bgpRmEntFastExtFallover,
       "bgpRmEntRemainDelayTime": bgpRmEntRemainDelayTime,
       "bgpRmEntPathAttrs": bgpRmEntPathAttrs,
       "bgpRmEntAggSplitHorizon": bgpRmEntAggSplitHorizon,
       "bgpRmEntAggAdvSuppr": bgpRmEntAggAdvSuppr,
       "bgpRmEntUpdateGroups": bgpRmEntUpdateGroups,
       "bgpRmEntPhase3DelayTime": bgpRmEntPhase3DelayTime,
       "bgpRmEntTrapOperState": bgpRmEntTrapOperState,
       "bgpRmAfiSafiTable": bgpRmAfiSafiTable,
       "bgpRmAfiSafiEntry": bgpRmAfiSafiEntry,
       "bgpRmAfiSafiAfi": bgpRmAfiSafiAfi,
       "bgpRmAfiSafiSafi": bgpRmAfiSafiSafi,
       "bgpRmAfiSafiAdminStatus": bgpRmAfiSafiAdminStatus,
       "bgpRmAfiSafiStateKept": bgpRmAfiSafiStateKept,
       "bgpRmAfiSafiAfmRequired": bgpRmAfiSafiAfmRequired,
       "bgpRmAfiSafiLocRibBlocked": bgpRmAfiSafiLocRibBlocked,
       "bgpRmAfiSafiAdvertiseInactive": bgpRmAfiSafiAdvertiseInactive,
       "bgpRmAfiSafiUserData": bgpRmAfiSafiUserData,
       "bgpRmAfiSafiIbgpPrefixes": bgpRmAfiSafiIbgpPrefixes,
       "bgpRmAfiSafiEbgpPrefixes": bgpRmAfiSafiEbgpPrefixes,
       "bgpRmAfiSafiRedistPrefixes": bgpRmAfiSafiRedistPrefixes,
       "bgpRmAfiSafiInPrfxes": bgpRmAfiSafiInPrfxes,
       "bgpRmAfiSafiInPrfxesAccepted": bgpRmAfiSafiInPrfxesAccepted,
       "bgpRmAfiSafiInPrfxesRejected": bgpRmAfiSafiInPrfxesRejected,
       "bgpRmAfiSafiOutPrfxes": bgpRmAfiSafiOutPrfxes,
       "bgpRmAfiSafiOutPrfxesAdvertised": bgpRmAfiSafiOutPrfxesAdvertised,
       "bgpRmAfiSafiInPrfxesActive": bgpRmAfiSafiInPrfxesActive,
       "bgpRmAfiSafiInPrfxesFlapped": bgpRmAfiSafiInPrfxesFlapped,
       "bgpRmAfiSafiInPrfxesFlapSuppr": bgpRmAfiSafiInPrfxesFlapSuppr,
       "bgpRmAfiSafiInPrfxesFlapHistory": bgpRmAfiSafiInPrfxesFlapHistory,
       "bgpRmAfiSafiDefaultImportRule": bgpRmAfiSafiDefaultImportRule,
       "bgpRmAfiSafiInPrfxesDeniedByPol": bgpRmAfiSafiInPrfxesDeniedByPol,
       "bgpRmAfiSafiNumLocRibRoutes": bgpRmAfiSafiNumLocRibRoutes,
       "bgpRmAfiSafiNextHopSafi": bgpRmAfiSafiNextHopSafi,
       "bgpPeer": bgpPeer,
       "bgpPeerData": bgpPeerData,
       "bgpPeerTable": bgpPeerTable,
       "bgpPeerEntry": bgpPeerEntry,
       "bgpPeerIdentifier": bgpPeerIdentifier,
       "bgpPeerState": bgpPeerState,
       "bgpPeerRowStatus": bgpPeerRowStatus,
       "bgpPeerAdminStatus": bgpPeerAdminStatus,
       "bgpPeerOperStatus": bgpPeerOperStatus,
       "bgpPeerLocalAddrType": bgpPeerLocalAddrType,
       "bgpPeerLocalAddr": bgpPeerLocalAddr,
       "bgpPeerLocalPort": bgpPeerLocalPort,
       "bgpPeerLocalNm": bgpPeerLocalNm,
       "bgpPeerRemoteAddrType": bgpPeerRemoteAddrType,
       "bgpPeerRemoteAddr": bgpPeerRemoteAddr,
       "bgpPeerRemotePort": bgpPeerRemotePort,
       "bgpPeerRemoteAs": bgpPeerRemoteAs,
       "bgpPeerIndex": bgpPeerIndex,
       "bgpPeerConfedMember": bgpPeerConfedMember,
       "bgpPeerReflectorClient": bgpPeerReflectorClient,
       "bgpPeerTrapEstab": bgpPeerTrapEstab,
       "bgpPeerTrapBackw": bgpPeerTrapBackw,
       "bgpPeerCapsSupport": bgpPeerCapsSupport,
       "bgpPeerLastError": bgpPeerLastError,
       "bgpPeerLastErrorDataLen": bgpPeerLastErrorDataLen,
       "bgpPeerLastErrorData": bgpPeerLastErrorData,
       "bgpPeerFsmEstablishedTime": bgpPeerFsmEstablishedTime,
       "bgpPeerInUpdatesElapsedTime": bgpPeerInUpdatesElapsedTime,
       "bgpPeerConnectRetryInterval": bgpPeerConnectRetryInterval,
       "bgpPeerHoldTimeConfigd": bgpPeerHoldTimeConfigd,
       "bgpPeerKeepAliveConfigd": bgpPeerKeepAliveConfigd,
       "bgpPeerMinASOriginationInterval": bgpPeerMinASOriginationInterval,
       "bgpPeerMinRouteAdvertiseInterval": bgpPeerMinRouteAdvertiseInterval,
       "bgpPeerHoldTime": bgpPeerHoldTime,
       "bgpPeerKeepAlive": bgpPeerKeepAlive,
       "bgpPeerInUpdates": bgpPeerInUpdates,
       "bgpPeerOutUpdates": bgpPeerOutUpdates,
       "bgpPeerInTotalMessages": bgpPeerInTotalMessages,
       "bgpPeerOutTotalMessages": bgpPeerOutTotalMessages,
       "bgpPeerFsmEstablishedTransitions": bgpPeerFsmEstablishedTransitions,
       "bgpPeerConnectRetryCount": bgpPeerConnectRetryCount,
       "bgpPeerClearCnts": bgpPeerClearCnts,
       "bgpPeerConfigPeergr": bgpPeerConfigPeergr,
       "bgpPeerConfigIndex": bgpPeerConfigIndex,
       "bgpPeerConfigRtRefresh": bgpPeerConfigRtRefresh,
       "bgpPeerConfigMaxPrfx": bgpPeerConfigMaxPrfx,
       "bgpPeerConfigDropWarn": bgpPeerConfigDropWarn,
       "bgpPeerConfigPassive": bgpPeerConfigPassive,
       "bgpPeerConfigOpenDelay": bgpPeerConfigOpenDelay,
       "bgpPeerConfigIdleHold": bgpPeerConfigIdleHold,
       "bgpPeerPassword": bgpPeerPassword,
       "bgpPeerTtl": bgpPeerTtl,
       "bgpPeerCheckFirstAsNum": bgpPeerCheckFirstAsNum,
       "bgpPeerAggrInclConfedAS": bgpPeerAggrInclConfedAS,
       "bgpPeerMinRouteWithdrawInterval": bgpPeerMinRouteWithdrawInterval,
       "bgpPeerStalePathTime": bgpPeerStalePathTime,
       "bgpPeerCheckNextHop": bgpPeerCheckNextHop,
       "bgpPeerLocalAddrScopeId": bgpPeerLocalAddrScopeId,
       "bgpPeerMaxOrfEntries": bgpPeerMaxOrfEntries,
       "bgpPeerOrfEntryCount": bgpPeerOrfEntryCount,
       "bgpPeerPeeringType": bgpPeerPeeringType,
       "bgpPeerSoftResetWithStoredInfo": bgpPeerSoftResetWithStoredInfo,
       "bgpPeerAllowLocalAs": bgpPeerAllowLocalAs,
       "bgpPeerDisableSenderLoopDetect": bgpPeerDisableSenderLoopDetect,
       "bgpPeerDisableRouteRefresh": bgpPeerDisableRouteRefresh,
       "bgpPeerFlapStatsClearStat": bgpPeerFlapStatsClearStat,
       "bgpPeerFlapStatsClearMap": bgpPeerFlapStatsClearMap,
       "bgpPeerLastErrorRcvd": bgpPeerLastErrorRcvd,
       "bgpPeerLastErrorRcvdTime": bgpPeerLastErrorRcvdTime,
       "bgpPeerLastErrorSent": bgpPeerLastErrorSent,
       "bgpPeerLastErrorSentTime": bgpPeerLastErrorSentTime,
       "bgpPeerLastState": bgpPeerLastState,
       "bgpPeerLastEvent": bgpPeerLastEvent,
       "bgpPeerCapsSent": bgpPeerCapsSent,
       "bgpPeerCapsRcvd": bgpPeerCapsRcvd,
       "bgpPeerCapsNegotiated": bgpPeerCapsNegotiated,
       "bgpPeerRstrSupport": bgpPeerRstrSupport,
       "bgpPeerRstrFamily": bgpPeerRstrFamily,
       "bgpPeerRstrRestarting": bgpPeerRstrRestarting,
       "bgpPeerRstrStatus": bgpPeerRstrStatus,
       "bgpPeerRstrRemTime": bgpPeerRstrRemTime,
       "bgpPeerRcvdMsgElapsedTime": bgpPeerRcvdMsgElapsedTime,
       "bgpPeerIdleHoldRemTime": bgpPeerIdleHoldRemTime,
       "bgpPeerRouteRefrSent": bgpPeerRouteRefrSent,
       "bgpPeerRouteRefrRcvd": bgpPeerRouteRefrRcvd,
       "bgpPeerNxtHopSlf": bgpPeerNxtHopSlf,
       "bgpPeerThirdPtyNxtHop": bgpPeerThirdPtyNxtHop,
       "bgpPeerNxtHopPeer": bgpPeerNxtHopPeer,
       "bgpPeerTrapPrefix": bgpPeerTrapPrefix,
       "bgpPeerConfigThreshold": bgpPeerConfigThreshold,
       "bgpPeerMaxPrfxHold": bgpPeerMaxPrfxHold,
       "bgpPeerSelectedLocalAddrType": bgpPeerSelectedLocalAddrType,
       "bgpPeerSelectedLocalAddr": bgpPeerSelectedLocalAddr,
       "bgpPeerSelectedLocalPort": bgpPeerSelectedLocalPort,
       "bgpPeerSelectedRemotePort": bgpPeerSelectedRemotePort,
       "bgpPeerBfdDesired": bgpPeerBfdDesired,
       "bgpPeerBfdStatus": bgpPeerBfdStatus,
       "bgpPeerCeaseErrorSubcode": bgpPeerCeaseErrorSubcode,
       "bgpPeerConfAltLocalAs": bgpPeerConfAltLocalAs,
       "bgpPeerSelectedLocalAs": bgpPeerSelectedLocalAs,
       "bgpPeerSelectedRemoteAs": bgpPeerSelectedRemoteAs,
       "bgpPeerInPrfxes": bgpPeerInPrfxes,
       "bgpPeerOutPrfxes": bgpPeerOutPrfxes,
       "bgpPeerOutPrfxesAdvertised": bgpPeerOutPrfxesAdvertised,
       "bgpPeerTrapGrHelperState": bgpPeerTrapGrHelperState,
       "bgpPeerEnableAttributeDiscard": bgpPeerEnableAttributeDiscard,
       "bgpPeerAfiSafiTable": bgpPeerAfiSafiTable,
       "bgpPeerAfiSafiEntry": bgpPeerAfiSafiEntry,
       "bgpPeerAfiSafiAfi": bgpPeerAfiSafiAfi,
       "bgpPeerAfiSafiSafi": bgpPeerAfiSafiSafi,
       "bgpPeerAfiSafiDisable": bgpPeerAfiSafiDisable,
       "bgpPeerAfiSafiConfigRtRefresh": bgpPeerAfiSafiConfigRtRefresh,
       "bgpPeerAfiSafiAllowLocalAs": bgpPeerAfiSafiAllowLocalAs,
       "bgpPeerAfiSafiDisableSndLpDetect": bgpPeerAfiSafiDisableSndLpDetect,
       "bgpPeerAfiSafiNxtHopSlf": bgpPeerAfiSafiNxtHopSlf,
       "bgpPeerAfiSafiOrigDefault": bgpPeerAfiSafiOrigDefault,
       "bgpPeerAfiSafiOrigDefaultRtMap": bgpPeerAfiSafiOrigDefaultRtMap,
       "bgpPeerAfiSafiSoftResetStore": bgpPeerAfiSafiSoftResetStore,
       "bgpPeerAfiSafiConfigMaxPrfx": bgpPeerAfiSafiConfigMaxPrfx,
       "bgpPeerAfiSafiConfigDropWarn": bgpPeerAfiSafiConfigDropWarn,
       "bgpPeerAfiSafiTrapPrefix": bgpPeerAfiSafiTrapPrefix,
       "bgpPeerAfiSafiConfigThreshold": bgpPeerAfiSafiConfigThreshold,
       "bgpPeerAfiSafiMaxPrfxHold": bgpPeerAfiSafiMaxPrfxHold,
       "bgpPeerAfiSafiMaxOrfEntries": bgpPeerAfiSafiMaxOrfEntries,
       "bgpPeerOrfCapabilityTable": bgpPeerOrfCapabilityTable,
       "bgpPeerOrfCapabilityEntry": bgpPeerOrfCapabilityEntry,
       "bgpPeerOrfCapabilityAfi": bgpPeerOrfCapabilityAfi,
       "bgpPeerOrfCapabilitySafi": bgpPeerOrfCapabilitySafi,
       "bgpPeerOrfCapabilityOrfType": bgpPeerOrfCapabilityOrfType,
       "bgpPeerOrfCapabilityAdminStatus": bgpPeerOrfCapabilityAdminStatus,
       "bgpPeerOrfCapabilitySendReceive": bgpPeerOrfCapabilitySendReceive,
       "bgpPeerCaps": bgpPeerCaps,
       "bgpPeerCapsRcvdTable": bgpPeerCapsRcvdTable,
       "bgpPeerCapsRcvdEntry": bgpPeerCapsRcvdEntry,
       "bgpPeerCapRcvdCode": bgpPeerCapRcvdCode,
       "bgpPeerCapRcvdIndex": bgpPeerCapRcvdIndex,
       "bgpPeerCapRcvdValue": bgpPeerCapRcvdValue,
       "bgpPeerCapsSentTable": bgpPeerCapsSentTable,
       "bgpPeerCapsSentEntry": bgpPeerCapsSentEntry,
       "bgpPeerCapSentCode": bgpPeerCapSentCode,
       "bgpPeerCapSentIndex": bgpPeerCapSentIndex,
       "bgpPeerCapSentValue": bgpPeerCapSentValue,
       "bgpPeerCntrs": bgpPeerCntrs,
       "bgpPrfxCntrsTable": bgpPrfxCntrsTable,
       "bgpPrfxCntrsEntry": bgpPrfxCntrsEntry,
       "bgpPrfxCntrsAfi": bgpPrfxCntrsAfi,
       "bgpPrfxCntrsSafi": bgpPrfxCntrsSafi,
       "bgpPrfxInPrfxes": bgpPrfxInPrfxes,
       "bgpPrfxInPrfxesAccepted": bgpPrfxInPrfxesAccepted,
       "bgpPrfxInPrfxesRejected": bgpPrfxInPrfxesRejected,
       "bgpPrfxOutPrfxes": bgpPrfxOutPrfxes,
       "bgpPrfxOutPrfxesAdvertised": bgpPrfxOutPrfxesAdvertised,
       "bgpPrfxCntrsUserData": bgpPrfxCntrsUserData,
       "bgpPrfxInPrfxesFlapped": bgpPrfxInPrfxesFlapped,
       "bgpPrfxInPrfxesFlapSuppressed": bgpPrfxInPrfxesFlapSuppressed,
       "bgpPrfxInPrfxesFlapHistory": bgpPrfxInPrfxesFlapHistory,
       "bgpPrfxInPrfxesActive": bgpPrfxInPrfxesActive,
       "bgpPrfxInPrfxesDeniedByPol": bgpPrfxInPrfxesDeniedByPol,
       "bgpPrfxNumLocRibRoutes": bgpPrfxNumLocRibRoutes,
       "bgpRib": bgpRib,
       "bgpNlriTable": bgpNlriTable,
       "bgpNlriEntry": bgpNlriEntry,
       "bgpNlriPeerOrAfm": bgpNlriPeerOrAfm,
       "bgpNlriPeerAfmIndex": bgpNlriPeerAfmIndex,
       "bgpNlriAfi": bgpNlriAfi,
       "bgpNlriSafi": bgpNlriSafi,
       "bgpNlriPrfx": bgpNlriPrfx,
       "bgpNlriPrfxLen": bgpNlriPrfxLen,
       "bgpNlriBest": bgpNlriBest,
       "bgpNlriAsSize": bgpNlriAsSize,
       "bgpNlriASPathStr": bgpNlriASPathStr,
       "bgpPathAttrOrigin": bgpPathAttrOrigin,
       "bgpPathAttrNextHop": bgpPathAttrNextHop,
       "bgpPathAttrMultiExitDisc": bgpPathAttrMultiExitDisc,
       "bgpPathAttrLocalPref": bgpPathAttrLocalPref,
       "bgpPathAttrAtomicAggregate": bgpPathAttrAtomicAggregate,
       "bgpPathAttrAggregatorAS": bgpPathAttrAggregatorAS,
       "bgpPathAttrAggregatorAddr": bgpPathAttrAggregatorAddr,
       "bgpPathAttrCalcLocalPref": bgpPathAttrCalcLocalPref,
       "bgpPathAttrOrigId": bgpPathAttrOrigId,
       "bgpPathAttrWeight": bgpPathAttrWeight,
       "bgpFlapStatsConfig": bgpFlapStatsConfig,
       "bgpFlapStatsPenalty": bgpFlapStatsPenalty,
       "bgpFlapStatsFlapcnt": bgpFlapStatsFlapcnt,
       "bgpFlapStatsSupprsd": bgpFlapStatsSupprsd,
       "bgpFlapStatsTimeleft": bgpFlapStatsTimeleft,
       "bgpFlapStatsCleardamp": bgpFlapStatsCleardamp,
       "bgpFlapStatsClearstat": bgpFlapStatsClearstat,
       "bgpNlriEcmp": bgpNlriEcmp,
       "bgpPathAttrAsPathLimAs": bgpPathAttrAsPathLimAs,
       "bgpPathAttrAsPathLimUpper": bgpPathAttrAsPathLimUpper,
       "bgpNlriIsActive": bgpNlriIsActive,
       "bgpNlriUserData": bgpNlriUserData,
       "bgpNlriStale": bgpNlriStale,
       "bgpNlriFlapStartTime": bgpNlriFlapStartTime,
       "bgpNlriLinkLocalNextHop": bgpNlriLinkLocalNextHop,
       "bgpPathAttrUnknownTable": bgpPathAttrUnknownTable,
       "bgpPathAttrUnknownEntry": bgpPathAttrUnknownEntry,
       "bgpPathAttrUnknownType": bgpPathAttrUnknownType,
       "bgpPathAttrUnknownValue": bgpPathAttrUnknownValue,
       "bgpPathAttrUnknownUserData": bgpPathAttrUnknownUserData,
       "bgpPathAttrExtensions": bgpPathAttrExtensions,
       "bgpPathAttrNonCapExts": bgpPathAttrNonCapExts,
       "bgpPathAttrRouteReflectionExts": bgpPathAttrRouteReflectionExts,
       "bgpPathAttrClusterTable": bgpPathAttrClusterTable,
       "bgpPathAttrClusterEntry": bgpPathAttrClusterEntry,
       "bgpPathAttrClusterIndex": bgpPathAttrClusterIndex,
       "bgpPathAttrClusterValue": bgpPathAttrClusterValue,
       "bgpPathAttrClusterUserData": bgpPathAttrClusterUserData,
       "bgpPathAttrCommunityExts": bgpPathAttrCommunityExts,
       "bgpPathAttrCommTable": bgpPathAttrCommTable,
       "bgpPathAttrCommEntry": bgpPathAttrCommEntry,
       "bgpPathAttrCommIndex": bgpPathAttrCommIndex,
       "bgpPathAttrCommValue": bgpPathAttrCommValue,
       "bgpPathAttrCommUserData": bgpPathAttrCommUserData,
       "bgpPathAttrExtCommunityExts": bgpPathAttrExtCommunityExts,
       "bgpPathAttrExtCommTable": bgpPathAttrExtCommTable,
       "bgpPathAttrExtCommEntry": bgpPathAttrExtCommEntry,
       "bgpPathAttrExtCommIndex": bgpPathAttrExtCommIndex,
       "bgpPathAttrExtCommValue": bgpPathAttrExtCommValue,
       "bgpPathAttrExtCommUserData": bgpPathAttrExtCommUserData,
       "bgpPathAttrCapExts": bgpPathAttrCapExts,
       "bgpAdjRibOutTable": bgpAdjRibOutTable,
       "bgpAdjRibOutEntry": bgpAdjRibOutEntry,
       "bgpAdjRibOutAfi": bgpAdjRibOutAfi,
       "bgpAdjRibOutSafi": bgpAdjRibOutSafi,
       "bgpAdjRibOutPrfx": bgpAdjRibOutPrfx,
       "bgpAdjRibOutPrfxLen": bgpAdjRibOutPrfxLen,
       "bgpAdjRibOutAdvertStatus": bgpAdjRibOutAdvertStatus,
       "bgpAdjRibOutLocalAggrType": bgpAdjRibOutLocalAggrType,
       "bgpAdjRibOutAsSize": bgpAdjRibOutAsSize,
       "bgpAdjRibOutASPathStr": bgpAdjRibOutASPathStr,
       "bgpAdjRibOutOrigin": bgpAdjRibOutOrigin,
       "bgpAdjRibOutNextHop": bgpAdjRibOutNextHop,
       "bgpAdjRibOutMultiExitDisc": bgpAdjRibOutMultiExitDisc,
       "bgpAdjRibOutLocalPref": bgpAdjRibOutLocalPref,
       "bgpAdjRibOutAtomicAggregate": bgpAdjRibOutAtomicAggregate,
       "bgpAdjRibOutAggregatorAS": bgpAdjRibOutAggregatorAS,
       "bgpAdjRibOutAggregatorAddr": bgpAdjRibOutAggregatorAddr,
       "bgpAdjRibOutOrigId": bgpAdjRibOutOrigId,
       "bgpAdjRibOutAsLimAs": bgpAdjRibOutAsLimAs,
       "bgpAdjRibOutAsLimUpper": bgpAdjRibOutAsLimUpper,
       "bgpAdjRibOutUserData": bgpAdjRibOutUserData,
       "bgpAdjRibOutEcmp": bgpAdjRibOutEcmp,
       "bgpAdjRibOutStale": bgpAdjRibOutStale,
       "bgpAdjRibOutLinkLocalNextHop": bgpAdjRibOutLinkLocalNextHop,
       "bgpNlriPrefixTable": bgpNlriPrefixTable,
       "bgpNlriPrefixEntry": bgpNlriPrefixEntry,
       "bgpNlriPrefixPeerOrAfm": bgpNlriPrefixPeerOrAfm,
       "bgpNlriPrefixPeerAfmIndex": bgpNlriPrefixPeerAfmIndex,
       "bgpNlriPrefixAfi": bgpNlriPrefixAfi,
       "bgpNlriPrefixSafi": bgpNlriPrefixSafi,
       "bgpNlriPrefixPrfx": bgpNlriPrefixPrfx,
       "bgpNlriPrefixPrfxLen": bgpNlriPrefixPrfxLen,
       "bgpNlriPrefixBest": bgpNlriPrefixBest,
       "bgpNlriPrefixAsSize": bgpNlriPrefixAsSize,
       "bgpNlriPrefixASPathStr": bgpNlriPrefixASPathStr,
       "bgpNlriPrefixPathAttrOrigin": bgpNlriPrefixPathAttrOrigin,
       "bgpNlriPrefixPathAttrNextHop": bgpNlriPrefixPathAttrNextHop,
       "bgpNlriPrefixPathAttrMultExtDisc": bgpNlriPrefixPathAttrMultExtDisc,
       "bgpNlriPrefixPathAttrLocalPref": bgpNlriPrefixPathAttrLocalPref,
       "bgpNlriPrefixPathAttrAtomicAgg": bgpNlriPrefixPathAttrAtomicAgg,
       "bgpNlriPrefixPathAttrAggAS": bgpNlriPrefixPathAttrAggAS,
       "bgpNlriPrefixPathAttrAggAddr": bgpNlriPrefixPathAttrAggAddr,
       "bgpNlriPrefixPathAttrCalcLclPref": bgpNlriPrefixPathAttrCalcLclPref,
       "bgpNlriPrefixPathAttrOrigId": bgpNlriPrefixPathAttrOrigId,
       "bgpNlriPrefixPathAttrWeight": bgpNlriPrefixPathAttrWeight,
       "bgpNlriPrefixFlapStatsConfig": bgpNlriPrefixFlapStatsConfig,
       "bgpNlriPrefixFlapStatsPenalty": bgpNlriPrefixFlapStatsPenalty,
       "bgpNlriPrefixFlapStatsFlapcnt": bgpNlriPrefixFlapStatsFlapcnt,
       "bgpNlriPrefixFlapStatsSupprsd": bgpNlriPrefixFlapStatsSupprsd,
       "bgpNlriPrefixFlapStatsTimeleft": bgpNlriPrefixFlapStatsTimeleft,
       "bgpNlriPrefixFlapStatsCleardamp": bgpNlriPrefixFlapStatsCleardamp,
       "bgpNlriPrefixFlapStatsClearstat": bgpNlriPrefixFlapStatsClearstat,
       "bgpNlriPrefixEcmp": bgpNlriPrefixEcmp,
       "bgpNlriPrefixPathAttrAsPathLimAs": bgpNlriPrefixPathAttrAsPathLimAs,
       "bgpNlriPrefixPthAttAsPthLimUpper": bgpNlriPrefixPthAttAsPthLimUpper,
       "bgpNlriPrefixIsActive": bgpNlriPrefixIsActive,
       "bgpNlriPrefixUserData": bgpNlriPrefixUserData,
       "bgpNlriPrefixStale": bgpNlriPrefixStale,
       "bgpNlriPrefixFlapStartTime": bgpNlriPrefixFlapStartTime,
       "bgpNlriPrefixLinkLocalNextHop": bgpNlriPrefixLinkLocalNextHop,
       "bgpPib": bgpPib,
       "bgpRouteMapTable": bgpRouteMapTable,
       "bgpRouteMapEntry": bgpRouteMapEntry,
       "bgpRouteMapIndex": bgpRouteMapIndex,
       "bgpRouteMapNumber": bgpRouteMapNumber,
       "bgpRouteMapRowStatus": bgpRouteMapRowStatus,
       "bgpRouteMapMaAfi": bgpRouteMapMaAfi,
       "bgpRouteMapMaAfiDef": bgpRouteMapMaAfiDef,
       "bgpRouteMapMaSafi": bgpRouteMapMaSafi,
       "bgpRouteMapMaSafiDef": bgpRouteMapMaSafiDef,
       "bgpRouteMapMaAs": bgpRouteMapMaAs,
       "bgpRouteMapMaComm": bgpRouteMapMaComm,
       "bgpRouteMapMaExtComm": bgpRouteMapMaExtComm,
       "bgpRouteMapMaAddr": bgpRouteMapMaAddr,
       "bgpRouteMapMaNext": bgpRouteMapMaNext,
       "bgpRouteMapMaSource": bgpRouteMapMaSource,
       "bgpRouteMapMaMed": bgpRouteMapMaMed,
       "bgpRouteMapMaMedDef": bgpRouteMapMaMedDef,
       "bgpRouteMapMaUser": bgpRouteMapMaUser,
       "bgpRouteMapSeAs": bgpRouteMapSeAs,
       "bgpRouteMapSeAsAct": bgpRouteMapSeAsAct,
       "bgpRouteMapSeComm": bgpRouteMapSeComm,
       "bgpRouteMapSeCommAct": bgpRouteMapSeCommAct,
       "bgpRouteMapSeExtComm": bgpRouteMapSeExtComm,
       "bgpRouteMapSeExtCommAct": bgpRouteMapSeExtCommAct,
       "bgpRouteMapSeLocPref": bgpRouteMapSeLocPref,
       "bgpRouteMapSeLocPrefDef": bgpRouteMapSeLocPrefDef,
       "bgpRouteMapSeMed": bgpRouteMapSeMed,
       "bgpRouteMapSeMedDef": bgpRouteMapSeMedDef,
       "bgpRouteMapSeNext": bgpRouteMapSeNext,
       "bgpRouteMapSeOrigin": bgpRouteMapSeOrigin,
       "bgpRouteMapSeOriginDef": bgpRouteMapSeOriginDef,
       "bgpRouteMapSeWeight": bgpRouteMapSeWeight,
       "bgpRouteMapSeWeightDef": bgpRouteMapSeWeightDef,
       "bgpRouteMapSeFlap": bgpRouteMapSeFlap,
       "bgpRouteMapSeUser": bgpRouteMapSeUser,
       "bgpRouteMapHitcnt": bgpRouteMapHitcnt,
       "bgpRouteMapClearcnt": bgpRouteMapClearcnt,
       "bgpRouteMapUserInfo": bgpRouteMapUserInfo,
       "bgpRouteMapType": bgpRouteMapType,
       "bgpRouteMapContinue": bgpRouteMapContinue,
       "bgpRouteMapOrfAssoc": bgpRouteMapOrfAssoc,
       "bgpRouteMapSeAsLimUpper": bgpRouteMapSeAsLimUpper,
       "bgpRouteMapSeAsLimDef": bgpRouteMapSeAsLimDef,
       "bgpRouteMapMaOrigin": bgpRouteMapMaOrigin,
       "bgpRouteMapMaOriginDef": bgpRouteMapMaOriginDef,
       "bgpRouteMapSeMedDelta": bgpRouteMapSeMedDelta,
       "bgpRouteMapSeMedDeltaTyp": bgpRouteMapSeMedDeltaTyp,
       "bgpRouteMapSeMedIgp": bgpRouteMapSeMedIgp,
       "bgpRouteMapSeAsPrependCount": bgpRouteMapSeAsPrependCount,
       "bgpRouteMapSeAsPrependSize": bgpRouteMapSeAsPrependSize,
       "bgpRouteMapSeAsPrependAsVals": bgpRouteMapSeAsPrependAsVals,
       "bgpRouteMapMaAnd": bgpRouteMapMaAnd,
       "bgpIpPreTable": bgpIpPreTable,
       "bgpIpPreEntry": bgpIpPreEntry,
       "bgpIpPreMatch": bgpIpPreMatch,
       "bgpIpPreNumber": bgpIpPreNumber,
       "bgpIpPreRowStatus": bgpIpPreRowStatus,
       "bgpIpPreAfi": bgpIpPreAfi,
       "bgpIpPreSafi": bgpIpPreSafi,
       "bgpIpPreAddr": bgpIpPreAddr,
       "bgpIpPreLen": bgpIpPreLen,
       "bgpIpPreGe": bgpIpPreGe,
       "bgpIpPreLe": bgpIpPreLe,
       "bgpIpPreType": bgpIpPreType,
       "bgpPeergrTable": bgpPeergrTable,
       "bgpPeergrEntry": bgpPeergrEntry,
       "bgpPeergrIndex": bgpPeergrIndex,
       "bgpPeergrRowStatus": bgpPeergrRowStatus,
       "bgpPeergrConfig": bgpPeergrConfig,
       "bgpPeergrArea": bgpPeergrArea,
       "bgpPeergrAggrConfedAS": bgpPeergrAggrConfedAS,
       "bgpPeergrSoftResetWithStoredInfo": bgpPeergrSoftResetWithStoredInfo,
       "bgpPeergrAllowLocalAs": bgpPeergrAllowLocalAs,
       "bgpPeergrDisableSenderLoopDetect": bgpPeergrDisableSenderLoopDetect,
       "bgpPeergrNxtHopSlf": bgpPeergrNxtHopSlf,
       "bgpPeergrThirdPtyNxtHop": bgpPeergrThirdPtyNxtHop,
       "bgpPeergrNxtHopPeer": bgpPeergrNxtHopPeer,
       "bgpPeergrEnableAttributeDiscard": bgpPeergrEnableAttributeDiscard,
       "bgpConfigTable": bgpConfigTable,
       "bgpConfigEntry": bgpConfigEntry,
       "bgpConfigIndex": bgpConfigIndex,
       "bgpConfigRowStatus": bgpConfigRowStatus,
       "bgpConfigRtgrimpe": bgpConfigRtgrimpe,
       "bgpConfigRtgrimde": bgpConfigRtgrimde,
       "bgpConfigRtgrexpe": bgpConfigRtgrexpe,
       "bgpConfigRtgrexde": bgpConfigRtgrexde,
       "bgpConfigDefImport": bgpConfigDefImport,
       "bgpConfigDefExport": bgpConfigDefExport,
       "bgpConfigNxtHopSlf": bgpConfigNxtHopSlf,
       "bgpConfigRemove": bgpConfigRemove,
       "bgpConfigImportMap": bgpConfigImportMap,
       "bgpConfigExportMap": bgpConfigExportMap,
       "bgpConfigAdvertiseMap": bgpConfigAdvertiseMap,
       "bgpConfigNonExistMap": bgpConfigNonExistMap,
       "bgpConfigBlockCondAdv": bgpConfigBlockCondAdv,
       "bgpConfigThirdPtyNxtHop": bgpConfigThirdPtyNxtHop,
       "bgpConfigNxtHopPeer": bgpConfigNxtHopPeer,
       "bgpConfigCondAdvOn": bgpConfigCondAdvOn,
       "bgpFlapConfigTable": bgpFlapConfigTable,
       "bgpFlapConfigEntry": bgpFlapConfigEntry,
       "bgpFlapConfigIndex": bgpFlapConfigIndex,
       "bgpFlapConfigRowStatus": bgpFlapConfigRowStatus,
       "bgpFlapConfigCut": bgpFlapConfigCut,
       "bgpFlapConfigReuse": bgpFlapConfigReuse,
       "bgpFlapConfigThold": bgpFlapConfigThold,
       "bgpFlapConfigDecayok": bgpFlapConfigDecayok,
       "bgpFlapConfigDecayng": bgpFlapConfigDecayng,
       "bgpFlapConfigTmaxok": bgpFlapConfigTmaxok,
       "bgpFlapConfigTmaxng": bgpFlapConfigTmaxng,
       "bgpAggregateTable": bgpAggregateTable,
       "bgpAggregateEntry": bgpAggregateEntry,
       "bgpAggrAfi": bgpAggrAfi,
       "bgpAggrSafi": bgpAggrSafi,
       "bgpAggrPrefix": bgpAggrPrefix,
       "bgpAggrPrefixLength": bgpAggrPrefixLength,
       "bgpAggrRowStatus": bgpAggrRowStatus,
       "bgpAggrOptions": bgpAggrOptions,
       "bgpAggrSuppressMap": bgpAggrSuppressMap,
       "bgpAggrAdvertiseMap": bgpAggrAdvertiseMap,
       "bgpAggrAttributeMap": bgpAggrAttributeMap,
       "bgpAggrPermanent": bgpAggrPermanent,
       "bgpOrfCapabilityTable": bgpOrfCapabilityTable,
       "bgpOrfCapabilityEntry": bgpOrfCapabilityEntry,
       "bgpOrfCapabilityAfi": bgpOrfCapabilityAfi,
       "bgpOrfCapabilitySafi": bgpOrfCapabilitySafi,
       "bgpOrfCapabilityOrfType": bgpOrfCapabilityOrfType,
       "bgpOrfCapabilityAdminStatus": bgpOrfCapabilityAdminStatus,
       "bgpOrfCapabilitySendReceive": bgpOrfCapabilitySendReceive,
       "bgpPeergrAfiSafiTable": bgpPeergrAfiSafiTable,
       "bgpPeergrAfiSafiEntry": bgpPeergrAfiSafiEntry,
       "bgpPeergrAfiSafiAfi": bgpPeergrAfiSafiAfi,
       "bgpPeergrAfiSafiSafi": bgpPeergrAfiSafiSafi,
       "bgpPeergrAfiSafiAllowLocalAs": bgpPeergrAfiSafiAllowLocalAs,
       "bgpPeergrAfiSafiDisSndLpDetect": bgpPeergrAfiSafiDisSndLpDetect,
       "bgpPeergrAfiSafiNxtHopSlf": bgpPeergrAfiSafiNxtHopSlf,
       "bgpPeergrAfiSafiOrigDefault": bgpPeergrAfiSafiOrigDefault,
       "bgpPeergrAfiSafiOrigDefaultRtMap": bgpPeergrAfiSafiOrigDefaultRtMap,
       "bgpPeergrAfiSafiSoftResetStore": bgpPeergrAfiSafiSoftResetStore,
       "bgpHaf": bgpHaf,
       "bgpRmAfmJoinTable": bgpRmAfmJoinTable,
       "bgpRmAfmJoinEntry": bgpRmAfmJoinEntry,
       "bgpRmAfmJoin": bgpRmAfmJoin,
       "bgpRmAfmRowStatus": bgpRmAfmRowStatus,
       "bgpRmAfmAdminStatus": bgpRmAfmAdminStatus,
       "bgpRmAfmOperStatus": bgpRmAfmOperStatus,
       "bgpRmAfmPartnerIndex": bgpRmAfmPartnerIndex,
       "bgpRmAfmAfi": bgpRmAfmAfi,
       "bgpRmAfmSafi": bgpRmAfmSafi,
       "bgpRmAfmJoinStatus": bgpRmAfmJoinStatus,
       "bgpRmAfmRestartTime": bgpRmAfmRestartTime,
       "bgpRmNmTable": bgpRmNmTable,
       "bgpRmNmEntry": bgpRmNmEntry,
       "bgpRmNmMasterIndex": bgpRmNmMasterIndex,
       "bgpRmNmJoinStatus": bgpRmNmJoinStatus,
       "bgpNmMjTable": bgpNmMjTable,
       "bgpNmMjEntry": bgpNmMjEntry,
       "bgpNmMjEntity": bgpNmMjEntity,
       "bgpNmMjJoin": bgpNmMjJoin,
       "bgpNmMjJoinPartner": bgpNmMjJoinPartner,
       "bgpNmMjPartnerIndex": bgpNmMjPartnerIndex,
       "bgpNmMjJoinStatus": bgpNmMjJoinStatus,
       "bgpRmArinhJoinTable": bgpRmArinhJoinTable,
       "bgpRmArinhJoinEntry": bgpRmArinhJoinEntry,
       "bgpRmArinhAfi": bgpRmArinhAfi,
       "bgpRmArinhSafi": bgpRmArinhSafi,
       "bgpRmArinhJoinStatus": bgpRmArinhJoinStatus,
       "bgpRmArinhEntIndex": bgpRmArinhEntIndex,
       "bgpNm": bgpNm,
       "bgpNmEntTable": bgpNmEntTable,
       "bgpNmEntEntry": bgpNmEntEntry,
       "bgpNmEntIndex": bgpNmEntIndex,
       "bgpNmEntRowStatus": bgpNmEntRowStatus,
       "bgpNmEntAdminStatus": bgpNmEntAdminStatus,
       "bgpNmEntOperStatus": bgpNmEntOperStatus,
       "bgpNmEntRmIndex": bgpNmEntRmIndex,
       "bgpNmEntSckIndex": bgpNmEntSckIndex,
       "bgpNmEntBfdEntityIndex": bgpNmEntBfdEntityIndex,
       "bgpNmListenTable": bgpNmListenTable,
       "bgpNmListenEntry": bgpNmListenEntry,
       "bgpNmListenIndex": bgpNmListenIndex,
       "bgpNmListenRowStatus": bgpNmListenRowStatus,
       "bgpNmListenAdminStatus": bgpNmListenAdminStatus,
       "bgpNmListenOperStatus": bgpNmListenOperStatus,
       "bgpNmListenAddrType": bgpNmListenAddrType,
       "bgpNmListenAddr": bgpNmListenAddr,
       "bgpNmListenPort": bgpNmListenPort,
       "bgpNmListenAcceptAll": bgpNmListenAcceptAll,
       "bgpNmListenAddrScopeId": bgpNmListenAddrScopeId,
       "bgpNotification": bgpNotification,
       "bgpNotificationEntry": bgpNotificationEntry,
       "bgpNotifPeerLocalAddrType": bgpNotifPeerLocalAddrType,
       "bgpNotifPeerLocalAddr": bgpNotifPeerLocalAddr,
       "bgpNotifPeerRemoteAddrType": bgpNotifPeerRemoteAddrType,
       "bgpNotifPeerRemoteAddr": bgpNotifPeerRemoteAddr,
       "bgpNotifRmEntIndex": bgpNotifRmEntIndex,
       "bgpNotifPeerLocalPort": bgpNotifPeerLocalPort,
       "bgpNotifPeerRemotePort": bgpNotifPeerRemotePort,
       "bgpPeerLastFailureCause": bgpPeerLastFailureCause,
       "bgpNotifPeerLocalAddrScopeId": bgpNotifPeerLocalAddrScopeId,
       "bgpConformance": bgpConformance,
       "bgpCompliances": bgpCompliances,
       "bgpCompliance": bgpCompliance,
       "bgpGroups": bgpGroups,
       "bgpRmEntityGroup": bgpRmEntityGroup,
       "bgpRmAfmJoinGroup": bgpRmAfmJoinGroup,
       "bgpRmNmGroup": bgpRmNmGroup,
       "bgpNmMjGroup": bgpNmMjGroup,
       "bgpNmEntGroup": bgpNmEntGroup,
       "bgpNmListenGroup": bgpNmListenGroup,
       "bgpPeerGroup": bgpPeerGroup,
       "bgpPathAttributesGroup": bgpPathAttributesGroup,
       "bgpPolicyGroup": bgpPolicyGroup,
       "bgpRmEntityOptionalGroup": bgpRmEntityOptionalGroup,
       "bgpRmAfmJoinOptionalGroup": bgpRmAfmJoinOptionalGroup,
       "bgpNmListenOptionalGroup": bgpNmListenOptionalGroup,
       "bgpPeerOptionalGroup": bgpPeerOptionalGroup,
       "bgpPathAttributesOptionalGroup": bgpPathAttributesOptionalGroup,
       "bgpPolicyOptionalGroup": bgpPolicyOptionalGroup,
       "bgpNotificationsGroup": bgpNotificationsGroup,
       "bgpObsoleteGroup": bgpObsoleteGroup,
       "bgpRmAfiSafiGroup": bgpRmAfiSafiGroup,
       "bgpRmAfiSafiOptionalGroup": bgpRmAfiSafiOptionalGroup,
       "bgpAdjRibOutGroup": bgpAdjRibOutGroup,
       "bgpOrfCapabilityGroup": bgpOrfCapabilityGroup,
       "bgpOrfCapabilityOptionalGroup": bgpOrfCapabilityOptionalGroup,
       "bgpPeerAfiSafiOptionalGroup": bgpPeerAfiSafiOptionalGroup,
       "bgpPeergrAfiSafiOptionalGroup": bgpPeergrAfiSafiOptionalGroup,
       "bgpPeerOrfCapabilityGroup": bgpPeerOrfCapabilityGroup,
       "bgpPeerOrfCapabilityOptionalGrp": bgpPeerOrfCapabilityOptionalGrp,
       "bgpRmArinhJoinGroup": bgpRmArinhJoinGroup,
       "bgpNmEntOptionalGroup": bgpNmEntOptionalGroup,
       "bgpNotificationObjectGroup": bgpNotificationObjectGroup}
)
