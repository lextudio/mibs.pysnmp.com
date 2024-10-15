# SNMP MIB module (REDSTONE-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/REDSTONE-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:46:43 2024
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

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(rsMgmt,) = mibBuilder.importSymbols(
    "REDSTONE-SMI",
    "rsMgmt")

(RsEnable,
 RsNextIfIndex) = mibBuilder.importSymbols(
    "REDSTONE-TC",
    "RsEnable",
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsPppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11)
)
rsPppMIB.setRevisions(
        ("1999-07-01 00:00",
         "1998-01-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RsPppAuthentication(Integer32, TextualConvention):
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
        *(("chap", 2),
          ("chapPap", 4),
          ("none", 0),
          ("pap", 1),
          ("papChap", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RsPppObjects_ObjectIdentity = ObjectIdentity
rsPppObjects = _RsPppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1)
)
_RsPppLcp_ObjectIdentity = ObjectIdentity
rsPppLcp = _RsPppLcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1)
)
_RsPppLinkStatusTable_Object = MibTable
rsPppLinkStatusTable = _RsPppLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    rsPppLinkStatusTable.setStatus("current")
_RsPppLinkStatusEntry_Object = MibTableRow
rsPppLinkStatusEntry = _RsPppLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1)
)
rsPppLinkStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsPppLinkStatusEntry.setStatus("current")


class _RsPppLinkStatusTerminateReason_Type(Integer32):
    """Custom type rsPppLinkStatusTerminateReason based on Integer32"""
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
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("addressLeaseExpired", 13),
          ("adminDisable", 2),
          ("adminLogout", 14),
          ("authenticationFailure", 5),
          ("inactivityTimeout", 12),
          ("keepaliveFailure", 10),
          ("lowerLayerDown", 3),
          ("maxRetriesExceeded", 8),
          ("negotiationFailure", 9),
          ("noUpperInterface", 4),
          ("none", 0),
          ("other", 1),
          ("peerRenegotiated", 7),
          ("peerTerminated", 6),
          ("sessionTimeout", 11))
    )


_RsPppLinkStatusTerminateReason_Type.__name__ = "Integer32"
_RsPppLinkStatusTerminateReason_Object = MibTableColumn
rsPppLinkStatusTerminateReason = _RsPppLinkStatusTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 1),
    _RsPppLinkStatusTerminateReason_Type()
)
rsPppLinkStatusTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppLinkStatusTerminateReason.setStatus("current")


class _RsPppLinkStatusTerminateNegFailOption_Type(Integer32):
    """Custom type rsPppLinkStatusTerminateNegFailOption based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("localAuthentication", 6),
          ("localMagicNumber", 4),
          ("localMru", 2),
          ("localToRemoteACCompression", 8),
          ("localToRemoteProtocolCompression", 7),
          ("none", 0),
          ("other", 1),
          ("remoteMagicNumber", 5),
          ("remoteMru", 3))
    )


_RsPppLinkStatusTerminateNegFailOption_Type.__name__ = "Integer32"
_RsPppLinkStatusTerminateNegFailOption_Object = MibTableColumn
rsPppLinkStatusTerminateNegFailOption = _RsPppLinkStatusTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 2),
    _RsPppLinkStatusTerminateNegFailOption_Type()
)
rsPppLinkStatusTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppLinkStatusTerminateNegFailOption.setStatus("current")
_RsPppLinkStatusInKeepaliveRequests_Type = Counter32
_RsPppLinkStatusInKeepaliveRequests_Object = MibTableColumn
rsPppLinkStatusInKeepaliveRequests = _RsPppLinkStatusInKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 3),
    _RsPppLinkStatusInKeepaliveRequests_Type()
)
rsPppLinkStatusInKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppLinkStatusInKeepaliveRequests.setStatus("current")
_RsPppLinkStatusOutKeepaliveRequests_Type = Counter32
_RsPppLinkStatusOutKeepaliveRequests_Object = MibTableColumn
rsPppLinkStatusOutKeepaliveRequests = _RsPppLinkStatusOutKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 4),
    _RsPppLinkStatusOutKeepaliveRequests_Type()
)
rsPppLinkStatusOutKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppLinkStatusOutKeepaliveRequests.setStatus("current")
_RsPppLinkStatusInKeepaliveReplies_Type = Counter32
_RsPppLinkStatusInKeepaliveReplies_Object = MibTableColumn
rsPppLinkStatusInKeepaliveReplies = _RsPppLinkStatusInKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 5),
    _RsPppLinkStatusInKeepaliveReplies_Type()
)
rsPppLinkStatusInKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppLinkStatusInKeepaliveReplies.setStatus("current")
_RsPppLinkStatusOutKeepaliveReplies_Type = Counter32
_RsPppLinkStatusOutKeepaliveReplies_Object = MibTableColumn
rsPppLinkStatusOutKeepaliveReplies = _RsPppLinkStatusOutKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 6),
    _RsPppLinkStatusOutKeepaliveReplies_Type()
)
rsPppLinkStatusOutKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppLinkStatusOutKeepaliveReplies.setStatus("current")
_RsPppLinkStatusKeepaliveFailures_Type = Counter32
_RsPppLinkStatusKeepaliveFailures_Object = MibTableColumn
rsPppLinkStatusKeepaliveFailures = _RsPppLinkStatusKeepaliveFailures_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 7),
    _RsPppLinkStatusKeepaliveFailures_Type()
)
rsPppLinkStatusKeepaliveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppLinkStatusKeepaliveFailures.setStatus("current")
_RsPppLinkStatusLocalMagicNumber_Type = Integer32
_RsPppLinkStatusLocalMagicNumber_Object = MibTableColumn
rsPppLinkStatusLocalMagicNumber = _RsPppLinkStatusLocalMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 8),
    _RsPppLinkStatusLocalMagicNumber_Type()
)
rsPppLinkStatusLocalMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppLinkStatusLocalMagicNumber.setStatus("current")
_RsPppLinkStatusRemoteMagicNumber_Type = Integer32
_RsPppLinkStatusRemoteMagicNumber_Object = MibTableColumn
rsPppLinkStatusRemoteMagicNumber = _RsPppLinkStatusRemoteMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 9),
    _RsPppLinkStatusRemoteMagicNumber_Type()
)
rsPppLinkStatusRemoteMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppLinkStatusRemoteMagicNumber.setStatus("current")
_RsPppLinkStatusLocalAuthentication_Type = RsPppAuthentication
_RsPppLinkStatusLocalAuthentication_Object = MibTableColumn
rsPppLinkStatusLocalAuthentication = _RsPppLinkStatusLocalAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 1, 1, 10),
    _RsPppLinkStatusLocalAuthentication_Type()
)
rsPppLinkStatusLocalAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppLinkStatusLocalAuthentication.setStatus("current")
_RsPppLinkConfigTable_Object = MibTable
rsPppLinkConfigTable = _RsPppLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rsPppLinkConfigTable.setStatus("current")
_RsPppLinkConfigEntry_Object = MibTableRow
rsPppLinkConfigEntry = _RsPppLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1)
)
rsPppLinkConfigEntry.setIndexNames(
    (0, "REDSTONE-PPP-MIB", "rsPppLinkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    rsPppLinkConfigEntry.setStatus("current")
_RsPppLinkConfigIfIndex_Type = InterfaceIndex
_RsPppLinkConfigIfIndex_Object = MibTableColumn
rsPppLinkConfigIfIndex = _RsPppLinkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 1),
    _RsPppLinkConfigIfIndex_Type()
)
rsPppLinkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rsPppLinkConfigIfIndex.setStatus("current")
_RsPppLinkConfigRowStatus_Type = RowStatus
_RsPppLinkConfigRowStatus_Object = MibTableColumn
rsPppLinkConfigRowStatus = _RsPppLinkConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 2),
    _RsPppLinkConfigRowStatus_Type()
)
rsPppLinkConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPppLinkConfigRowStatus.setStatus("current")
_RsPppLinkConfigLowerIfIndex_Type = InterfaceIndexOrZero
_RsPppLinkConfigLowerIfIndex_Object = MibTableColumn
rsPppLinkConfigLowerIfIndex = _RsPppLinkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 3),
    _RsPppLinkConfigLowerIfIndex_Type()
)
rsPppLinkConfigLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPppLinkConfigLowerIfIndex.setStatus("current")


class _RsPppLinkConfigKeepalive_Type(Integer32):
    """Custom type rsPppLinkConfigKeepalive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 300),
    )


_RsPppLinkConfigKeepalive_Type.__name__ = "Integer32"
_RsPppLinkConfigKeepalive_Object = MibTableColumn
rsPppLinkConfigKeepalive = _RsPppLinkConfigKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 4),
    _RsPppLinkConfigKeepalive_Type()
)
rsPppLinkConfigKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPppLinkConfigKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    rsPppLinkConfigKeepalive.setUnits("seconds")


class _RsPppLinkConfigAuthentication_Type(RsPppAuthentication):
    """Custom type rsPppLinkConfigAuthentication based on RsPppAuthentication"""


_RsPppLinkConfigAuthentication_Object = MibTableColumn
rsPppLinkConfigAuthentication = _RsPppLinkConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 5),
    _RsPppLinkConfigAuthentication_Type()
)
rsPppLinkConfigAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPppLinkConfigAuthentication.setStatus("current")


class _RsPppLinkConfigMaxAuthenRetries_Type(Integer32):
    """Custom type rsPppLinkConfigMaxAuthenRetries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RsPppLinkConfigMaxAuthenRetries_Type.__name__ = "Integer32"
_RsPppLinkConfigMaxAuthenRetries_Object = MibTableColumn
rsPppLinkConfigMaxAuthenRetries = _RsPppLinkConfigMaxAuthenRetries_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 2, 1, 6),
    _RsPppLinkConfigMaxAuthenRetries_Type()
)
rsPppLinkConfigMaxAuthenRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rsPppLinkConfigMaxAuthenRetries.setStatus("current")
_RsPppNextIfIndex_Type = RsNextIfIndex
_RsPppNextIfIndex_Object = MibScalar
rsPppNextIfIndex = _RsPppNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 1, 3),
    _RsPppNextIfIndex_Type()
)
rsPppNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppNextIfIndex.setStatus("current")
_RsPppSec_ObjectIdentity = ObjectIdentity
rsPppSec = _RsPppSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 2)
)
_RsPppIp_ObjectIdentity = ObjectIdentity
rsPppIp = _RsPppIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3)
)
_RsPppIpTable_Object = MibTable
rsPppIpTable = _RsPppIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    rsPppIpTable.setStatus("current")
_RsPppIpEntry_Object = MibTableRow
rsPppIpEntry = _RsPppIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1)
)
rsPppIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsPppIpEntry.setStatus("current")
_RsPppIpServiceStatus_Type = RsEnable
_RsPppIpServiceStatus_Object = MibTableColumn
rsPppIpServiceStatus = _RsPppIpServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 1),
    _RsPppIpServiceStatus_Type()
)
rsPppIpServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppIpServiceStatus.setStatus("current")


class _RsPppIpTerminateReason_Type(Integer32):
    """Custom type rsPppIpTerminateReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("admin", 3),
          ("linkDown", 4),
          ("maxRetriesExceeded", 7),
          ("negotiationFailure", 8),
          ("noService", 2),
          ("none", 0),
          ("other", 1),
          ("peerRenegotiated", 6),
          ("peerTerminated", 5))
    )


_RsPppIpTerminateReason_Type.__name__ = "Integer32"
_RsPppIpTerminateReason_Object = MibTableColumn
rsPppIpTerminateReason = _RsPppIpTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 2),
    _RsPppIpTerminateReason_Type()
)
rsPppIpTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppIpTerminateReason.setStatus("current")


class _RsPppIpTerminateNegFailOption_Type(Integer32):
    """Custom type rsPppIpTerminateNegFailOption based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("localIpAddress", 2),
          ("none", 0),
          ("other", 1),
          ("remoteIpAddress", 3),
          ("remotePrimaryDnsAddress", 4),
          ("remotePrimaryWinsAddress", 6),
          ("remoteSecondaryDnsAddress", 5),
          ("remoteSecondaryWinsAddress", 7))
    )


_RsPppIpTerminateNegFailOption_Type.__name__ = "Integer32"
_RsPppIpTerminateNegFailOption_Object = MibTableColumn
rsPppIpTerminateNegFailOption = _RsPppIpTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 3),
    _RsPppIpTerminateNegFailOption_Type()
)
rsPppIpTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppIpTerminateNegFailOption.setStatus("current")
_RsPppIpLocalIpAddress_Type = IpAddress
_RsPppIpLocalIpAddress_Object = MibTableColumn
rsPppIpLocalIpAddress = _RsPppIpLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 4),
    _RsPppIpLocalIpAddress_Type()
)
rsPppIpLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppIpLocalIpAddress.setStatus("current")
_RsPppIpRemoteIpAddress_Type = IpAddress
_RsPppIpRemoteIpAddress_Object = MibTableColumn
rsPppIpRemoteIpAddress = _RsPppIpRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 5),
    _RsPppIpRemoteIpAddress_Type()
)
rsPppIpRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppIpRemoteIpAddress.setStatus("current")
_RsPppIpRemotePrimaryDnsAddress_Type = IpAddress
_RsPppIpRemotePrimaryDnsAddress_Object = MibTableColumn
rsPppIpRemotePrimaryDnsAddress = _RsPppIpRemotePrimaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 6),
    _RsPppIpRemotePrimaryDnsAddress_Type()
)
rsPppIpRemotePrimaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppIpRemotePrimaryDnsAddress.setStatus("current")
_RsPppIpRemoteSecondaryDnsAddress_Type = IpAddress
_RsPppIpRemoteSecondaryDnsAddress_Object = MibTableColumn
rsPppIpRemoteSecondaryDnsAddress = _RsPppIpRemoteSecondaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 7),
    _RsPppIpRemoteSecondaryDnsAddress_Type()
)
rsPppIpRemoteSecondaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppIpRemoteSecondaryDnsAddress.setStatus("current")
_RsPppIpRemotePrimaryWinsAddress_Type = IpAddress
_RsPppIpRemotePrimaryWinsAddress_Object = MibTableColumn
rsPppIpRemotePrimaryWinsAddress = _RsPppIpRemotePrimaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 8),
    _RsPppIpRemotePrimaryWinsAddress_Type()
)
rsPppIpRemotePrimaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppIpRemotePrimaryWinsAddress.setStatus("current")
_RsPppIpRemoteSecondaryWinsAddress_Type = IpAddress
_RsPppIpRemoteSecondaryWinsAddress_Object = MibTableColumn
rsPppIpRemoteSecondaryWinsAddress = _RsPppIpRemoteSecondaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 1, 1, 9),
    _RsPppIpRemoteSecondaryWinsAddress_Type()
)
rsPppIpRemoteSecondaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppIpRemoteSecondaryWinsAddress.setStatus("current")
_RsPppIpConfigTable_Object = MibTable
rsPppIpConfigTable = _RsPppIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 2)
)
if mibBuilder.loadTexts:
    rsPppIpConfigTable.setStatus("current")
_RsPppIpConfigEntry_Object = MibTableRow
rsPppIpConfigEntry = _RsPppIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 2, 1)
)
rsPppIpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsPppIpConfigEntry.setStatus("current")
_RsPppIpConfigPeerDnsPriority_Type = RsEnable
_RsPppIpConfigPeerDnsPriority_Object = MibTableColumn
rsPppIpConfigPeerDnsPriority = _RsPppIpConfigPeerDnsPriority_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 2, 1, 1),
    _RsPppIpConfigPeerDnsPriority_Type()
)
rsPppIpConfigPeerDnsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPppIpConfigPeerDnsPriority.setStatus("current")
_RsPppIpConfigPeerWinsPriority_Type = RsEnable
_RsPppIpConfigPeerWinsPriority_Object = MibTableColumn
rsPppIpConfigPeerWinsPriority = _RsPppIpConfigPeerWinsPriority_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 3, 2, 1, 2),
    _RsPppIpConfigPeerWinsPriority_Type()
)
rsPppIpConfigPeerWinsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPppIpConfigPeerWinsPriority.setStatus("current")
_RsPppOsi_ObjectIdentity = ObjectIdentity
rsPppOsi = _RsPppOsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4)
)
_RsPppOsiTable_Object = MibTable
rsPppOsiTable = _RsPppOsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    rsPppOsiTable.setStatus("current")
_RsPppOsiEntry_Object = MibTableRow
rsPppOsiEntry = _RsPppOsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1)
)
rsPppOsiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsPppOsiEntry.setStatus("current")
_RsPppOsiServiceStatus_Type = RsEnable
_RsPppOsiServiceStatus_Object = MibTableColumn
rsPppOsiServiceStatus = _RsPppOsiServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 1),
    _RsPppOsiServiceStatus_Type()
)
rsPppOsiServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppOsiServiceStatus.setStatus("current")


class _RsPppOsiOperStatus_Type(Integer32):
    """Custom type rsPppOsiOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-opened", 2),
          ("opened", 1))
    )


_RsPppOsiOperStatus_Type.__name__ = "Integer32"
_RsPppOsiOperStatus_Object = MibTableColumn
rsPppOsiOperStatus = _RsPppOsiOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 2),
    _RsPppOsiOperStatus_Type()
)
rsPppOsiOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppOsiOperStatus.setStatus("current")


class _RsPppOsiTerminateReason_Type(Integer32):
    """Custom type rsPppOsiTerminateReason based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("admin", 3),
          ("linkDown", 4),
          ("maxRetriesExceeded", 7),
          ("negotiationFailure", 8),
          ("noService", 2),
          ("none", 0),
          ("other", 1),
          ("peerRenegotiated", 6),
          ("peerTerminated", 5))
    )


_RsPppOsiTerminateReason_Type.__name__ = "Integer32"
_RsPppOsiTerminateReason_Object = MibTableColumn
rsPppOsiTerminateReason = _RsPppOsiTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 3),
    _RsPppOsiTerminateReason_Type()
)
rsPppOsiTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppOsiTerminateReason.setStatus("current")


class _RsPppOsiTerminateNegFailOption_Type(Integer32):
    """Custom type rsPppOsiTerminateNegFailOption based on Integer32"""
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
        *(("localAlignNpdu", 2),
          ("none", 0),
          ("other", 1),
          ("remoteAlignNpdu", 3))
    )


_RsPppOsiTerminateNegFailOption_Type.__name__ = "Integer32"
_RsPppOsiTerminateNegFailOption_Object = MibTableColumn
rsPppOsiTerminateNegFailOption = _RsPppOsiTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 4),
    _RsPppOsiTerminateNegFailOption_Type()
)
rsPppOsiTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppOsiTerminateNegFailOption.setStatus("current")


class _RsPppOsiLocalAlignNpdu_Type(Integer32):
    """Custom type rsPppOsiLocalAlignNpdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("even", 254),
          ("fourModulo4", 4),
          ("none", 0),
          ("odd", 255),
          ("oneModulo4", 1),
          ("threeModulo4", 3),
          ("twoModulo4", 2))
    )


_RsPppOsiLocalAlignNpdu_Type.__name__ = "Integer32"
_RsPppOsiLocalAlignNpdu_Object = MibTableColumn
rsPppOsiLocalAlignNpdu = _RsPppOsiLocalAlignNpdu_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 5),
    _RsPppOsiLocalAlignNpdu_Type()
)
rsPppOsiLocalAlignNpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppOsiLocalAlignNpdu.setStatus("current")


class _RsPppOsiRemoteAlignNpdu_Type(Integer32):
    """Custom type rsPppOsiRemoteAlignNpdu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("even", 254),
          ("fourModulo4", 4),
          ("none", 0),
          ("odd", 255),
          ("oneModulo4", 1),
          ("threeModulo4", 3),
          ("twoModulo4", 2))
    )


_RsPppOsiRemoteAlignNpdu_Type.__name__ = "Integer32"
_RsPppOsiRemoteAlignNpdu_Object = MibTableColumn
rsPppOsiRemoteAlignNpdu = _RsPppOsiRemoteAlignNpdu_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 1, 1, 6),
    _RsPppOsiRemoteAlignNpdu_Type()
)
rsPppOsiRemoteAlignNpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppOsiRemoteAlignNpdu.setStatus("current")
_RsPppOsiConfigTable_Object = MibTable
rsPppOsiConfigTable = _RsPppOsiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 2)
)
if mibBuilder.loadTexts:
    rsPppOsiConfigTable.setStatus("current")
_RsPppOsiConfigEntry_Object = MibTableRow
rsPppOsiConfigEntry = _RsPppOsiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 2, 1)
)
rsPppOsiConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsPppOsiConfigEntry.setStatus("current")


class _RsPppOsiConfigAdminStatus_Type(Integer32):
    """Custom type rsPppOsiConfigAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("close", 2),
          ("open", 1))
    )


_RsPppOsiConfigAdminStatus_Type.__name__ = "Integer32"
_RsPppOsiConfigAdminStatus_Object = MibTableColumn
rsPppOsiConfigAdminStatus = _RsPppOsiConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 4, 2, 1, 1),
    _RsPppOsiConfigAdminStatus_Type()
)
rsPppOsiConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsPppOsiConfigAdminStatus.setStatus("current")
_RsPppSession_ObjectIdentity = ObjectIdentity
rsPppSession = _RsPppSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5)
)
_RsPppSessionTable_Object = MibTable
rsPppSessionTable = _RsPppSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1)
)
if mibBuilder.loadTexts:
    rsPppSessionTable.setStatus("current")
_RsPppSessionEntry_Object = MibTableRow
rsPppSessionEntry = _RsPppSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1)
)
rsPppSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rsPppSessionEntry.setStatus("current")
_RsPppSessionGrant_Type = TruthValue
_RsPppSessionGrant_Object = MibTableColumn
rsPppSessionGrant = _RsPppSessionGrant_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 1),
    _RsPppSessionGrant_Type()
)
rsPppSessionGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionGrant.setStatus("current")


class _RsPppSessionTerminateReason_Type(Integer32):
    """Custom type rsPppSessionTerminateReason based on Integer32"""
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
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("addressLeaseExpired", 16),
          ("adminDisable", 6),
          ("adminLogout", 17),
          ("authenticatorTimeout", 15),
          ("challengeTimeout", 13),
          ("deny", 9),
          ("inactivityTimeout", 5),
          ("keepaliveFailure", 3),
          ("lowerLayerDown", 7),
          ("noHardware", 10),
          ("noInterface", 12),
          ("noResources", 11),
          ("noUpperInterface", 8),
          ("none", 0),
          ("requestTimeout", 14),
          ("sessionTimeout", 4),
          ("unknown", 1),
          ("userRequest", 2))
    )


_RsPppSessionTerminateReason_Type.__name__ = "Integer32"
_RsPppSessionTerminateReason_Object = MibTableColumn
rsPppSessionTerminateReason = _RsPppSessionTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 2),
    _RsPppSessionTerminateReason_Type()
)
rsPppSessionTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionTerminateReason.setStatus("current")
_RsPppSessionStartTime_Type = TimeTicks
_RsPppSessionStartTime_Object = MibTableColumn
rsPppSessionStartTime = _RsPppSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 3),
    _RsPppSessionStartTime_Type()
)
rsPppSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionStartTime.setStatus("current")
_RsPppSessionInOctets_Type = Counter32
_RsPppSessionInOctets_Object = MibTableColumn
rsPppSessionInOctets = _RsPppSessionInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 4),
    _RsPppSessionInOctets_Type()
)
rsPppSessionInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionInOctets.setStatus("current")
_RsPppSessionOutOctets_Type = Counter32
_RsPppSessionOutOctets_Object = MibTableColumn
rsPppSessionOutOctets = _RsPppSessionOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 5),
    _RsPppSessionOutOctets_Type()
)
rsPppSessionOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionOutOctets.setStatus("current")
_RsPppSessionInPackets_Type = Counter32
_RsPppSessionInPackets_Object = MibTableColumn
rsPppSessionInPackets = _RsPppSessionInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 6),
    _RsPppSessionInPackets_Type()
)
rsPppSessionInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionInPackets.setStatus("current")
_RsPppSessionOutPackets_Type = Counter32
_RsPppSessionOutPackets_Object = MibTableColumn
rsPppSessionOutPackets = _RsPppSessionOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 7),
    _RsPppSessionOutPackets_Type()
)
rsPppSessionOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionOutPackets.setStatus("current")
_RsPppSessionSessionTimeout_Type = Integer32
_RsPppSessionSessionTimeout_Object = MibTableColumn
rsPppSessionSessionTimeout = _RsPppSessionSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 8),
    _RsPppSessionSessionTimeout_Type()
)
rsPppSessionSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rsPppSessionSessionTimeout.setUnits("milliseconds")
_RsPppSessionInactivityTimeout_Type = Integer32
_RsPppSessionInactivityTimeout_Object = MibTableColumn
rsPppSessionInactivityTimeout = _RsPppSessionInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 9),
    _RsPppSessionInactivityTimeout_Type()
)
rsPppSessionInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rsPppSessionInactivityTimeout.setUnits("milliseconds")
_RsPppSessionAccountingInterval_Type = Integer32
_RsPppSessionAccountingInterval_Object = MibTableColumn
rsPppSessionAccountingInterval = _RsPppSessionAccountingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 10),
    _RsPppSessionAccountingInterval_Type()
)
rsPppSessionAccountingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionAccountingInterval.setStatus("current")
if mibBuilder.loadTexts:
    rsPppSessionAccountingInterval.setUnits("milliseconds")
_RsPppSessionRemoteIpAddress_Type = IpAddress
_RsPppSessionRemoteIpAddress_Object = MibTableColumn
rsPppSessionRemoteIpAddress = _RsPppSessionRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 11),
    _RsPppSessionRemoteIpAddress_Type()
)
rsPppSessionRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionRemoteIpAddress.setStatus("current")
_RsPppSessionRemotePrimaryDnsAddress_Type = IpAddress
_RsPppSessionRemotePrimaryDnsAddress_Object = MibTableColumn
rsPppSessionRemotePrimaryDnsAddress = _RsPppSessionRemotePrimaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 12),
    _RsPppSessionRemotePrimaryDnsAddress_Type()
)
rsPppSessionRemotePrimaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionRemotePrimaryDnsAddress.setStatus("current")
_RsPppSessionRemoteSecondaryDnsAddress_Type = IpAddress
_RsPppSessionRemoteSecondaryDnsAddress_Object = MibTableColumn
rsPppSessionRemoteSecondaryDnsAddress = _RsPppSessionRemoteSecondaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 13),
    _RsPppSessionRemoteSecondaryDnsAddress_Type()
)
rsPppSessionRemoteSecondaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionRemoteSecondaryDnsAddress.setStatus("current")
_RsPppSessionRemotePrimaryWinsAddress_Type = IpAddress
_RsPppSessionRemotePrimaryWinsAddress_Object = MibTableColumn
rsPppSessionRemotePrimaryWinsAddress = _RsPppSessionRemotePrimaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 14),
    _RsPppSessionRemotePrimaryWinsAddress_Type()
)
rsPppSessionRemotePrimaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionRemotePrimaryWinsAddress.setStatus("current")
_RsPppSessionRemoteSecondaryWinsAddress_Type = IpAddress
_RsPppSessionRemoteSecondaryWinsAddress_Object = MibTableColumn
rsPppSessionRemoteSecondaryWinsAddress = _RsPppSessionRemoteSecondaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 1, 5, 1, 1, 15),
    _RsPppSessionRemoteSecondaryWinsAddress_Type()
)
rsPppSessionRemoteSecondaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsPppSessionRemoteSecondaryWinsAddress.setStatus("current")
_RsPppConformance_ObjectIdentity = ObjectIdentity
rsPppConformance = _RsPppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4)
)
_RsPppCompliances_ObjectIdentity = ObjectIdentity
rsPppCompliances = _RsPppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 1)
)
_RsPppGroups_ObjectIdentity = ObjectIdentity
rsPppGroups = _RsPppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2)
)

# Managed Objects groups

rsPppLcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 1)
)
rsPppLcpGroup.setObjects(
      *(("REDSTONE-PPP-MIB", "rsPppLinkConfigRowStatus"),
        ("REDSTONE-PPP-MIB", "rsPppLinkConfigLowerIfIndex"),
        ("REDSTONE-PPP-MIB", "rsPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    rsPppLcpGroup.setStatus("current")

rsPppIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 2)
)
rsPppIpGroup.setObjects(
    ("REDSTONE-PPP-MIB", "rsPppIpServiceStatus")
)
if mibBuilder.loadTexts:
    rsPppIpGroup.setStatus("current")

rsPppOsiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 3)
)
rsPppOsiGroup.setObjects(
      *(("REDSTONE-PPP-MIB", "rsPppOsiServiceStatus"),
        ("REDSTONE-PPP-MIB", "rsPppOsiOperStatus"),
        ("REDSTONE-PPP-MIB", "rsPppOsiConfigAdminStatus"))
)
if mibBuilder.loadTexts:
    rsPppOsiGroup.setStatus("current")

rsPppLcpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 4)
)
rsPppLcpGroup2.setObjects(
      *(("REDSTONE-PPP-MIB", "rsPppLinkStatusTerminateReason"),
        ("REDSTONE-PPP-MIB", "rsPppLinkStatusTerminateNegFailOption"),
        ("REDSTONE-PPP-MIB", "rsPppLinkStatusInKeepaliveRequests"),
        ("REDSTONE-PPP-MIB", "rsPppLinkStatusOutKeepaliveRequests"),
        ("REDSTONE-PPP-MIB", "rsPppLinkStatusInKeepaliveReplies"),
        ("REDSTONE-PPP-MIB", "rsPppLinkStatusOutKeepaliveReplies"),
        ("REDSTONE-PPP-MIB", "rsPppLinkStatusKeepaliveFailures"),
        ("REDSTONE-PPP-MIB", "rsPppLinkStatusLocalMagicNumber"),
        ("REDSTONE-PPP-MIB", "rsPppLinkStatusRemoteMagicNumber"),
        ("REDSTONE-PPP-MIB", "rsPppLinkStatusLocalAuthentication"),
        ("REDSTONE-PPP-MIB", "rsPppLinkConfigRowStatus"),
        ("REDSTONE-PPP-MIB", "rsPppLinkConfigLowerIfIndex"),
        ("REDSTONE-PPP-MIB", "rsPppLinkConfigKeepalive"),
        ("REDSTONE-PPP-MIB", "rsPppLinkConfigAuthentication"),
        ("REDSTONE-PPP-MIB", "rsPppLinkConfigMaxAuthenRetries"),
        ("REDSTONE-PPP-MIB", "rsPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    rsPppLcpGroup2.setStatus("current")

rsPppIpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 5)
)
rsPppIpGroup2.setObjects(
      *(("REDSTONE-PPP-MIB", "rsPppIpServiceStatus"),
        ("REDSTONE-PPP-MIB", "rsPppIpTerminateReason"),
        ("REDSTONE-PPP-MIB", "rsPppIpTerminateNegFailOption"),
        ("REDSTONE-PPP-MIB", "rsPppIpRemoteIpAddress"),
        ("REDSTONE-PPP-MIB", "rsPppIpRemotePrimaryDnsAddress"),
        ("REDSTONE-PPP-MIB", "rsPppIpRemoteSecondaryDnsAddress"),
        ("REDSTONE-PPP-MIB", "rsPppIpRemotePrimaryWinsAddress"),
        ("REDSTONE-PPP-MIB", "rsPppIpRemoteSecondaryWinsAddress"),
        ("REDSTONE-PPP-MIB", "rsPppIpConfigPeerDnsPriority"),
        ("REDSTONE-PPP-MIB", "rsPppIpConfigPeerWinsPriority"))
)
if mibBuilder.loadTexts:
    rsPppIpGroup2.setStatus("current")

rsPppOsiGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 6)
)
rsPppOsiGroup2.setObjects(
      *(("REDSTONE-PPP-MIB", "rsPppOsiServiceStatus"),
        ("REDSTONE-PPP-MIB", "rsPppOsiOperStatus"),
        ("REDSTONE-PPP-MIB", "rsPppOsiTerminateReason"),
        ("REDSTONE-PPP-MIB", "rsPppOsiTerminateNegFailOption"),
        ("REDSTONE-PPP-MIB", "rsPppOsiLocalAlignNpdu"),
        ("REDSTONE-PPP-MIB", "rsPppOsiRemoteAlignNpdu"),
        ("REDSTONE-PPP-MIB", "rsPppOsiConfigAdminStatus"))
)
if mibBuilder.loadTexts:
    rsPppOsiGroup2.setStatus("current")

rsPppSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 2, 7)
)
rsPppSessionGroup.setObjects(
      *(("REDSTONE-PPP-MIB", "rsPppSessionGrant"),
        ("REDSTONE-PPP-MIB", "rsPppSessionTerminateReason"),
        ("REDSTONE-PPP-MIB", "rsPppSessionStartTime"),
        ("REDSTONE-PPP-MIB", "rsPppSessionInOctets"),
        ("REDSTONE-PPP-MIB", "rsPppSessionOutOctets"),
        ("REDSTONE-PPP-MIB", "rsPppSessionInPackets"),
        ("REDSTONE-PPP-MIB", "rsPppSessionOutPackets"),
        ("REDSTONE-PPP-MIB", "rsPppSessionSessionTimeout"),
        ("REDSTONE-PPP-MIB", "rsPppSessionInactivityTimeout"),
        ("REDSTONE-PPP-MIB", "rsPppSessionAccountingInterval"),
        ("REDSTONE-PPP-MIB", "rsPppSessionRemoteIpAddress"),
        ("REDSTONE-PPP-MIB", "rsPppSessionRemotePrimaryDnsAddress"),
        ("REDSTONE-PPP-MIB", "rsPppSessionRemoteSecondaryDnsAddress"),
        ("REDSTONE-PPP-MIB", "rsPppSessionRemotePrimaryWinsAddress"),
        ("REDSTONE-PPP-MIB", "rsPppSessionRemoteSecondaryWinsAddress"))
)
if mibBuilder.loadTexts:
    rsPppSessionGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rsPppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 1, 1)
)
if mibBuilder.loadTexts:
    rsPppCompliance.setStatus(
        "current"
    )

rsPppCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2773, 2, 11, 4, 1, 2)
)
if mibBuilder.loadTexts:
    rsPppCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "REDSTONE-PPP-MIB",
    **{"RsPppAuthentication": RsPppAuthentication,
       "rsPppMIB": rsPppMIB,
       "rsPppObjects": rsPppObjects,
       "rsPppLcp": rsPppLcp,
       "rsPppLinkStatusTable": rsPppLinkStatusTable,
       "rsPppLinkStatusEntry": rsPppLinkStatusEntry,
       "rsPppLinkStatusTerminateReason": rsPppLinkStatusTerminateReason,
       "rsPppLinkStatusTerminateNegFailOption": rsPppLinkStatusTerminateNegFailOption,
       "rsPppLinkStatusInKeepaliveRequests": rsPppLinkStatusInKeepaliveRequests,
       "rsPppLinkStatusOutKeepaliveRequests": rsPppLinkStatusOutKeepaliveRequests,
       "rsPppLinkStatusInKeepaliveReplies": rsPppLinkStatusInKeepaliveReplies,
       "rsPppLinkStatusOutKeepaliveReplies": rsPppLinkStatusOutKeepaliveReplies,
       "rsPppLinkStatusKeepaliveFailures": rsPppLinkStatusKeepaliveFailures,
       "rsPppLinkStatusLocalMagicNumber": rsPppLinkStatusLocalMagicNumber,
       "rsPppLinkStatusRemoteMagicNumber": rsPppLinkStatusRemoteMagicNumber,
       "rsPppLinkStatusLocalAuthentication": rsPppLinkStatusLocalAuthentication,
       "rsPppLinkConfigTable": rsPppLinkConfigTable,
       "rsPppLinkConfigEntry": rsPppLinkConfigEntry,
       "rsPppLinkConfigIfIndex": rsPppLinkConfigIfIndex,
       "rsPppLinkConfigRowStatus": rsPppLinkConfigRowStatus,
       "rsPppLinkConfigLowerIfIndex": rsPppLinkConfigLowerIfIndex,
       "rsPppLinkConfigKeepalive": rsPppLinkConfigKeepalive,
       "rsPppLinkConfigAuthentication": rsPppLinkConfigAuthentication,
       "rsPppLinkConfigMaxAuthenRetries": rsPppLinkConfigMaxAuthenRetries,
       "rsPppNextIfIndex": rsPppNextIfIndex,
       "rsPppSec": rsPppSec,
       "rsPppIp": rsPppIp,
       "rsPppIpTable": rsPppIpTable,
       "rsPppIpEntry": rsPppIpEntry,
       "rsPppIpServiceStatus": rsPppIpServiceStatus,
       "rsPppIpTerminateReason": rsPppIpTerminateReason,
       "rsPppIpTerminateNegFailOption": rsPppIpTerminateNegFailOption,
       "rsPppIpLocalIpAddress": rsPppIpLocalIpAddress,
       "rsPppIpRemoteIpAddress": rsPppIpRemoteIpAddress,
       "rsPppIpRemotePrimaryDnsAddress": rsPppIpRemotePrimaryDnsAddress,
       "rsPppIpRemoteSecondaryDnsAddress": rsPppIpRemoteSecondaryDnsAddress,
       "rsPppIpRemotePrimaryWinsAddress": rsPppIpRemotePrimaryWinsAddress,
       "rsPppIpRemoteSecondaryWinsAddress": rsPppIpRemoteSecondaryWinsAddress,
       "rsPppIpConfigTable": rsPppIpConfigTable,
       "rsPppIpConfigEntry": rsPppIpConfigEntry,
       "rsPppIpConfigPeerDnsPriority": rsPppIpConfigPeerDnsPriority,
       "rsPppIpConfigPeerWinsPriority": rsPppIpConfigPeerWinsPriority,
       "rsPppOsi": rsPppOsi,
       "rsPppOsiTable": rsPppOsiTable,
       "rsPppOsiEntry": rsPppOsiEntry,
       "rsPppOsiServiceStatus": rsPppOsiServiceStatus,
       "rsPppOsiOperStatus": rsPppOsiOperStatus,
       "rsPppOsiTerminateReason": rsPppOsiTerminateReason,
       "rsPppOsiTerminateNegFailOption": rsPppOsiTerminateNegFailOption,
       "rsPppOsiLocalAlignNpdu": rsPppOsiLocalAlignNpdu,
       "rsPppOsiRemoteAlignNpdu": rsPppOsiRemoteAlignNpdu,
       "rsPppOsiConfigTable": rsPppOsiConfigTable,
       "rsPppOsiConfigEntry": rsPppOsiConfigEntry,
       "rsPppOsiConfigAdminStatus": rsPppOsiConfigAdminStatus,
       "rsPppSession": rsPppSession,
       "rsPppSessionTable": rsPppSessionTable,
       "rsPppSessionEntry": rsPppSessionEntry,
       "rsPppSessionGrant": rsPppSessionGrant,
       "rsPppSessionTerminateReason": rsPppSessionTerminateReason,
       "rsPppSessionStartTime": rsPppSessionStartTime,
       "rsPppSessionInOctets": rsPppSessionInOctets,
       "rsPppSessionOutOctets": rsPppSessionOutOctets,
       "rsPppSessionInPackets": rsPppSessionInPackets,
       "rsPppSessionOutPackets": rsPppSessionOutPackets,
       "rsPppSessionSessionTimeout": rsPppSessionSessionTimeout,
       "rsPppSessionInactivityTimeout": rsPppSessionInactivityTimeout,
       "rsPppSessionAccountingInterval": rsPppSessionAccountingInterval,
       "rsPppSessionRemoteIpAddress": rsPppSessionRemoteIpAddress,
       "rsPppSessionRemotePrimaryDnsAddress": rsPppSessionRemotePrimaryDnsAddress,
       "rsPppSessionRemoteSecondaryDnsAddress": rsPppSessionRemoteSecondaryDnsAddress,
       "rsPppSessionRemotePrimaryWinsAddress": rsPppSessionRemotePrimaryWinsAddress,
       "rsPppSessionRemoteSecondaryWinsAddress": rsPppSessionRemoteSecondaryWinsAddress,
       "rsPppConformance": rsPppConformance,
       "rsPppCompliances": rsPppCompliances,
       "rsPppCompliance": rsPppCompliance,
       "rsPppCompliance2": rsPppCompliance2,
       "rsPppGroups": rsPppGroups,
       "rsPppLcpGroup": rsPppLcpGroup,
       "rsPppIpGroup": rsPppIpGroup,
       "rsPppOsiGroup": rsPppOsiGroup,
       "rsPppLcpGroup2": rsPppLcpGroup2,
       "rsPppIpGroup2": rsPppIpGroup2,
       "rsPppOsiGroup2": rsPppOsiGroup2,
       "rsPppSessionGroup": rsPppSessionGroup}
)
