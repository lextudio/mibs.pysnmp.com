# SNMP MIB module (Unisphere-Data-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:17 2024
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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,
 UsdName,
 UsdNextIfIndex) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable",
    "UsdName",
    "UsdNextIfIndex")


# MODULE-IDENTITY

usdPppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11)
)
usdPppMIB.setRevisions(
        ("2002-05-09 20:31",
         "2002-05-08 20:00",
         "2000-10-09 16:10",
         "2000-02-15 12:00",
         "1999-07-01 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdPppAuthentication(Integer32, TextualConvention):
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



class UsdPppMlPppBundleName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



# MIB Managed Objects in the order of their OIDs

_UsdPppObjects_ObjectIdentity = ObjectIdentity
usdPppObjects = _UsdPppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1)
)
_UsdPppLcp_ObjectIdentity = ObjectIdentity
usdPppLcp = _UsdPppLcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1)
)
_UsdPppLinkStatusTable_Object = MibTable
usdPppLinkStatusTable = _UsdPppLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdPppLinkStatusTable.setStatus("current")
_UsdPppLinkStatusEntry_Object = MibTableRow
usdPppLinkStatusEntry = _UsdPppLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1)
)
usdPppLinkStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    usdPppLinkStatusEntry.setStatus("current")


class _UsdPppLinkStatusTerminateReason_Type(Integer32):
    """Custom type usdPppLinkStatusTerminateReason based on Integer32"""
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
        *(("addressLeaseExpired", 13),
          ("adminDisable", 2),
          ("adminLogout", 14),
          ("authenticationFailure", 5),
          ("inactivityTimeout", 12),
          ("keepaliveFailure", 10),
          ("loopback", 17),
          ("lowerLayerDown", 3),
          ("maxRetriesExceeded", 8),
          ("negotiationFailure", 9),
          ("noUpperInterface", 4),
          ("none", 0),
          ("other", 1),
          ("peerRenegotiated", 7),
          ("peerTerminated", 6),
          ("sessionTimeout", 11),
          ("tunnelDisconnected", 16),
          ("tunnelFailed", 15))
    )


_UsdPppLinkStatusTerminateReason_Type.__name__ = "Integer32"
_UsdPppLinkStatusTerminateReason_Object = MibTableColumn
usdPppLinkStatusTerminateReason = _UsdPppLinkStatusTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 1),
    _UsdPppLinkStatusTerminateReason_Type()
)
usdPppLinkStatusTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusTerminateReason.setStatus("current")


class _UsdPppLinkStatusTerminateNegFailOption_Type(Integer32):
    """Custom type usdPppLinkStatusTerminateNegFailOption based on Integer32"""
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


_UsdPppLinkStatusTerminateNegFailOption_Type.__name__ = "Integer32"
_UsdPppLinkStatusTerminateNegFailOption_Object = MibTableColumn
usdPppLinkStatusTerminateNegFailOption = _UsdPppLinkStatusTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 2),
    _UsdPppLinkStatusTerminateNegFailOption_Type()
)
usdPppLinkStatusTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusTerminateNegFailOption.setStatus("current")
_UsdPppLinkStatusInKeepaliveRequests_Type = Counter32
_UsdPppLinkStatusInKeepaliveRequests_Object = MibTableColumn
usdPppLinkStatusInKeepaliveRequests = _UsdPppLinkStatusInKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 3),
    _UsdPppLinkStatusInKeepaliveRequests_Type()
)
usdPppLinkStatusInKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusInKeepaliveRequests.setStatus("current")
_UsdPppLinkStatusOutKeepaliveRequests_Type = Counter32
_UsdPppLinkStatusOutKeepaliveRequests_Object = MibTableColumn
usdPppLinkStatusOutKeepaliveRequests = _UsdPppLinkStatusOutKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 4),
    _UsdPppLinkStatusOutKeepaliveRequests_Type()
)
usdPppLinkStatusOutKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusOutKeepaliveRequests.setStatus("current")
_UsdPppLinkStatusInKeepaliveReplies_Type = Counter32
_UsdPppLinkStatusInKeepaliveReplies_Object = MibTableColumn
usdPppLinkStatusInKeepaliveReplies = _UsdPppLinkStatusInKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 5),
    _UsdPppLinkStatusInKeepaliveReplies_Type()
)
usdPppLinkStatusInKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusInKeepaliveReplies.setStatus("current")
_UsdPppLinkStatusOutKeepaliveReplies_Type = Counter32
_UsdPppLinkStatusOutKeepaliveReplies_Object = MibTableColumn
usdPppLinkStatusOutKeepaliveReplies = _UsdPppLinkStatusOutKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 6),
    _UsdPppLinkStatusOutKeepaliveReplies_Type()
)
usdPppLinkStatusOutKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusOutKeepaliveReplies.setStatus("current")
_UsdPppLinkStatusKeepaliveFailures_Type = Counter32
_UsdPppLinkStatusKeepaliveFailures_Object = MibTableColumn
usdPppLinkStatusKeepaliveFailures = _UsdPppLinkStatusKeepaliveFailures_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 7),
    _UsdPppLinkStatusKeepaliveFailures_Type()
)
usdPppLinkStatusKeepaliveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusKeepaliveFailures.setStatus("current")
_UsdPppLinkStatusLocalMagicNumber_Type = Integer32
_UsdPppLinkStatusLocalMagicNumber_Object = MibTableColumn
usdPppLinkStatusLocalMagicNumber = _UsdPppLinkStatusLocalMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 8),
    _UsdPppLinkStatusLocalMagicNumber_Type()
)
usdPppLinkStatusLocalMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusLocalMagicNumber.setStatus("current")
_UsdPppLinkStatusRemoteMagicNumber_Type = Integer32
_UsdPppLinkStatusRemoteMagicNumber_Object = MibTableColumn
usdPppLinkStatusRemoteMagicNumber = _UsdPppLinkStatusRemoteMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 9),
    _UsdPppLinkStatusRemoteMagicNumber_Type()
)
usdPppLinkStatusRemoteMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusRemoteMagicNumber.setStatus("current")
_UsdPppLinkStatusLocalAuthentication_Type = UsdPppAuthentication
_UsdPppLinkStatusLocalAuthentication_Object = MibTableColumn
usdPppLinkStatusLocalAuthentication = _UsdPppLinkStatusLocalAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 10),
    _UsdPppLinkStatusLocalAuthentication_Type()
)
usdPppLinkStatusLocalAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusLocalAuthentication.setStatus("current")
_UsdPppLinkStatusTunnelIfIndex_Type = InterfaceIndexOrZero
_UsdPppLinkStatusTunnelIfIndex_Object = MibTableColumn
usdPppLinkStatusTunnelIfIndex = _UsdPppLinkStatusTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 11),
    _UsdPppLinkStatusTunnelIfIndex_Type()
)
usdPppLinkStatusTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkStatusTunnelIfIndex.setStatus("current")
_UsdPppLinkConfigTable_Object = MibTable
usdPppLinkConfigTable = _UsdPppLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdPppLinkConfigTable.setStatus("current")
_UsdPppLinkConfigEntry_Object = MibTableRow
usdPppLinkConfigEntry = _UsdPppLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1)
)
usdPppLinkConfigEntry.setIndexNames(
    (0, "Unisphere-Data-PPP-MIB", "usdPppLinkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    usdPppLinkConfigEntry.setStatus("current")
_UsdPppLinkConfigIfIndex_Type = InterfaceIndex
_UsdPppLinkConfigIfIndex_Object = MibTableColumn
usdPppLinkConfigIfIndex = _UsdPppLinkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 1),
    _UsdPppLinkConfigIfIndex_Type()
)
usdPppLinkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPppLinkConfigIfIndex.setStatus("current")
_UsdPppLinkConfigRowStatus_Type = RowStatus
_UsdPppLinkConfigRowStatus_Object = MibTableColumn
usdPppLinkConfigRowStatus = _UsdPppLinkConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 2),
    _UsdPppLinkConfigRowStatus_Type()
)
usdPppLinkConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppLinkConfigRowStatus.setStatus("current")
_UsdPppLinkConfigLowerIfIndex_Type = InterfaceIndexOrZero
_UsdPppLinkConfigLowerIfIndex_Object = MibTableColumn
usdPppLinkConfigLowerIfIndex = _UsdPppLinkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 3),
    _UsdPppLinkConfigLowerIfIndex_Type()
)
usdPppLinkConfigLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppLinkConfigLowerIfIndex.setStatus("current")


class _UsdPppLinkConfigKeepalive_Type(Integer32):
    """Custom type usdPppLinkConfigKeepalive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 300),
    )


_UsdPppLinkConfigKeepalive_Type.__name__ = "Integer32"
_UsdPppLinkConfigKeepalive_Object = MibTableColumn
usdPppLinkConfigKeepalive = _UsdPppLinkConfigKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 4),
    _UsdPppLinkConfigKeepalive_Type()
)
usdPppLinkConfigKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppLinkConfigKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    usdPppLinkConfigKeepalive.setUnits("seconds")


class _UsdPppLinkConfigAuthentication_Type(UsdPppAuthentication):
    """Custom type usdPppLinkConfigAuthentication based on UsdPppAuthentication"""


_UsdPppLinkConfigAuthentication_Object = MibTableColumn
usdPppLinkConfigAuthentication = _UsdPppLinkConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 5),
    _UsdPppLinkConfigAuthentication_Type()
)
usdPppLinkConfigAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppLinkConfigAuthentication.setStatus("current")


class _UsdPppLinkConfigMaxAuthenRetries_Type(Integer32):
    """Custom type usdPppLinkConfigMaxAuthenRetries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_UsdPppLinkConfigMaxAuthenRetries_Type.__name__ = "Integer32"
_UsdPppLinkConfigMaxAuthenRetries_Object = MibTableColumn
usdPppLinkConfigMaxAuthenRetries = _UsdPppLinkConfigMaxAuthenRetries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 6),
    _UsdPppLinkConfigMaxAuthenRetries_Type()
)
usdPppLinkConfigMaxAuthenRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppLinkConfigMaxAuthenRetries.setStatus("current")
_UsdPppLinkConfigStandardIfIndex_Type = InterfaceIndex
_UsdPppLinkConfigStandardIfIndex_Object = MibTableColumn
usdPppLinkConfigStandardIfIndex = _UsdPppLinkConfigStandardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 7),
    _UsdPppLinkConfigStandardIfIndex_Type()
)
usdPppLinkConfigStandardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppLinkConfigStandardIfIndex.setStatus("current")


class _UsdPppLinkConfigChapMinChallengeLength_Type(Integer32):
    """Custom type usdPppLinkConfigChapMinChallengeLength based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_UsdPppLinkConfigChapMinChallengeLength_Type.__name__ = "Integer32"
_UsdPppLinkConfigChapMinChallengeLength_Object = MibTableColumn
usdPppLinkConfigChapMinChallengeLength = _UsdPppLinkConfigChapMinChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 8),
    _UsdPppLinkConfigChapMinChallengeLength_Type()
)
usdPppLinkConfigChapMinChallengeLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppLinkConfigChapMinChallengeLength.setStatus("current")


class _UsdPppLinkConfigChapMaxChallengeLength_Type(Integer32):
    """Custom type usdPppLinkConfigChapMaxChallengeLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_UsdPppLinkConfigChapMaxChallengeLength_Type.__name__ = "Integer32"
_UsdPppLinkConfigChapMaxChallengeLength_Object = MibTableColumn
usdPppLinkConfigChapMaxChallengeLength = _UsdPppLinkConfigChapMaxChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 9),
    _UsdPppLinkConfigChapMaxChallengeLength_Type()
)
usdPppLinkConfigChapMaxChallengeLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppLinkConfigChapMaxChallengeLength.setStatus("current")


class _UsdPppLinkConfigPassiveMode_Type(UsdEnable):
    """Custom type usdPppLinkConfigPassiveMode based on UsdEnable"""


_UsdPppLinkConfigPassiveMode_Object = MibTableColumn
usdPppLinkConfigPassiveMode = _UsdPppLinkConfigPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 10),
    _UsdPppLinkConfigPassiveMode_Type()
)
usdPppLinkConfigPassiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppLinkConfigPassiveMode.setStatus("current")
_UsdPppLinkConfigAuthenticatorVirtualRouter_Type = UsdName
_UsdPppLinkConfigAuthenticatorVirtualRouter_Object = MibTableColumn
usdPppLinkConfigAuthenticatorVirtualRouter = _UsdPppLinkConfigAuthenticatorVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 11),
    _UsdPppLinkConfigAuthenticatorVirtualRouter_Type()
)
usdPppLinkConfigAuthenticatorVirtualRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppLinkConfigAuthenticatorVirtualRouter.setStatus("current")
_UsdPppNextIfIndex_Type = UsdNextIfIndex
_UsdPppNextIfIndex_Object = MibScalar
usdPppNextIfIndex = _UsdPppNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 3),
    _UsdPppNextIfIndex_Type()
)
usdPppNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppNextIfIndex.setStatus("current")
_UsdPppSec_ObjectIdentity = ObjectIdentity
usdPppSec = _UsdPppSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 2)
)
_UsdPppIp_ObjectIdentity = ObjectIdentity
usdPppIp = _UsdPppIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3)
)
_UsdPppIpTable_Object = MibTable
usdPppIpTable = _UsdPppIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    usdPppIpTable.setStatus("current")
_UsdPppIpEntry_Object = MibTableRow
usdPppIpEntry = _UsdPppIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1)
)
usdPppIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    usdPppIpEntry.setStatus("current")
_UsdPppIpServiceStatus_Type = UsdEnable
_UsdPppIpServiceStatus_Object = MibTableColumn
usdPppIpServiceStatus = _UsdPppIpServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 1),
    _UsdPppIpServiceStatus_Type()
)
usdPppIpServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppIpServiceStatus.setStatus("current")


class _UsdPppIpTerminateReason_Type(Integer32):
    """Custom type usdPppIpTerminateReason based on Integer32"""
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


_UsdPppIpTerminateReason_Type.__name__ = "Integer32"
_UsdPppIpTerminateReason_Object = MibTableColumn
usdPppIpTerminateReason = _UsdPppIpTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 2),
    _UsdPppIpTerminateReason_Type()
)
usdPppIpTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppIpTerminateReason.setStatus("current")


class _UsdPppIpTerminateNegFailOption_Type(Integer32):
    """Custom type usdPppIpTerminateNegFailOption based on Integer32"""
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


_UsdPppIpTerminateNegFailOption_Type.__name__ = "Integer32"
_UsdPppIpTerminateNegFailOption_Object = MibTableColumn
usdPppIpTerminateNegFailOption = _UsdPppIpTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 3),
    _UsdPppIpTerminateNegFailOption_Type()
)
usdPppIpTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppIpTerminateNegFailOption.setStatus("current")
_UsdPppIpLocalIpAddress_Type = IpAddress
_UsdPppIpLocalIpAddress_Object = MibTableColumn
usdPppIpLocalIpAddress = _UsdPppIpLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 4),
    _UsdPppIpLocalIpAddress_Type()
)
usdPppIpLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppIpLocalIpAddress.setStatus("current")
_UsdPppIpRemoteIpAddress_Type = IpAddress
_UsdPppIpRemoteIpAddress_Object = MibTableColumn
usdPppIpRemoteIpAddress = _UsdPppIpRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 5),
    _UsdPppIpRemoteIpAddress_Type()
)
usdPppIpRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppIpRemoteIpAddress.setStatus("current")
_UsdPppIpRemotePrimaryDnsAddress_Type = IpAddress
_UsdPppIpRemotePrimaryDnsAddress_Object = MibTableColumn
usdPppIpRemotePrimaryDnsAddress = _UsdPppIpRemotePrimaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 6),
    _UsdPppIpRemotePrimaryDnsAddress_Type()
)
usdPppIpRemotePrimaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppIpRemotePrimaryDnsAddress.setStatus("current")
_UsdPppIpRemoteSecondaryDnsAddress_Type = IpAddress
_UsdPppIpRemoteSecondaryDnsAddress_Object = MibTableColumn
usdPppIpRemoteSecondaryDnsAddress = _UsdPppIpRemoteSecondaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 7),
    _UsdPppIpRemoteSecondaryDnsAddress_Type()
)
usdPppIpRemoteSecondaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppIpRemoteSecondaryDnsAddress.setStatus("current")
_UsdPppIpRemotePrimaryWinsAddress_Type = IpAddress
_UsdPppIpRemotePrimaryWinsAddress_Object = MibTableColumn
usdPppIpRemotePrimaryWinsAddress = _UsdPppIpRemotePrimaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 8),
    _UsdPppIpRemotePrimaryWinsAddress_Type()
)
usdPppIpRemotePrimaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppIpRemotePrimaryWinsAddress.setStatus("current")
_UsdPppIpRemoteSecondaryWinsAddress_Type = IpAddress
_UsdPppIpRemoteSecondaryWinsAddress_Object = MibTableColumn
usdPppIpRemoteSecondaryWinsAddress = _UsdPppIpRemoteSecondaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 9),
    _UsdPppIpRemoteSecondaryWinsAddress_Type()
)
usdPppIpRemoteSecondaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppIpRemoteSecondaryWinsAddress.setStatus("current")
_UsdPppIpConfigTable_Object = MibTable
usdPppIpConfigTable = _UsdPppIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2)
)
if mibBuilder.loadTexts:
    usdPppIpConfigTable.setStatus("current")
_UsdPppIpConfigEntry_Object = MibTableRow
usdPppIpConfigEntry = _UsdPppIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1)
)
usdPppIpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    usdPppIpConfigEntry.setStatus("current")
_UsdPppIpConfigPeerDnsPriority_Type = UsdEnable
_UsdPppIpConfigPeerDnsPriority_Object = MibTableColumn
usdPppIpConfigPeerDnsPriority = _UsdPppIpConfigPeerDnsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1, 1),
    _UsdPppIpConfigPeerDnsPriority_Type()
)
usdPppIpConfigPeerDnsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppIpConfigPeerDnsPriority.setStatus("current")
_UsdPppIpConfigPeerWinsPriority_Type = UsdEnable
_UsdPppIpConfigPeerWinsPriority_Object = MibTableColumn
usdPppIpConfigPeerWinsPriority = _UsdPppIpConfigPeerWinsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1, 2),
    _UsdPppIpConfigPeerWinsPriority_Type()
)
usdPppIpConfigPeerWinsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppIpConfigPeerWinsPriority.setStatus("current")


class _UsdPppIpConfigIpcpNetmask_Type(UsdEnable):
    """Custom type usdPppIpConfigIpcpNetmask based on UsdEnable"""


_UsdPppIpConfigIpcpNetmask_Object = MibTableColumn
usdPppIpConfigIpcpNetmask = _UsdPppIpConfigIpcpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1, 3),
    _UsdPppIpConfigIpcpNetmask_Type()
)
usdPppIpConfigIpcpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppIpConfigIpcpNetmask.setStatus("current")
_UsdPppOsi_ObjectIdentity = ObjectIdentity
usdPppOsi = _UsdPppOsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4)
)
_UsdPppOsiTable_Object = MibTable
usdPppOsiTable = _UsdPppOsiTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    usdPppOsiTable.setStatus("current")
_UsdPppOsiEntry_Object = MibTableRow
usdPppOsiEntry = _UsdPppOsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1)
)
usdPppOsiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    usdPppOsiEntry.setStatus("current")
_UsdPppOsiServiceStatus_Type = UsdEnable
_UsdPppOsiServiceStatus_Object = MibTableColumn
usdPppOsiServiceStatus = _UsdPppOsiServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 1),
    _UsdPppOsiServiceStatus_Type()
)
usdPppOsiServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppOsiServiceStatus.setStatus("current")


class _UsdPppOsiOperStatus_Type(Integer32):
    """Custom type usdPppOsiOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notOpened", 2),
          ("opened", 1))
    )


_UsdPppOsiOperStatus_Type.__name__ = "Integer32"
_UsdPppOsiOperStatus_Object = MibTableColumn
usdPppOsiOperStatus = _UsdPppOsiOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 2),
    _UsdPppOsiOperStatus_Type()
)
usdPppOsiOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppOsiOperStatus.setStatus("current")


class _UsdPppOsiTerminateReason_Type(Integer32):
    """Custom type usdPppOsiTerminateReason based on Integer32"""
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


_UsdPppOsiTerminateReason_Type.__name__ = "Integer32"
_UsdPppOsiTerminateReason_Object = MibTableColumn
usdPppOsiTerminateReason = _UsdPppOsiTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 3),
    _UsdPppOsiTerminateReason_Type()
)
usdPppOsiTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppOsiTerminateReason.setStatus("current")


class _UsdPppOsiTerminateNegFailOption_Type(Integer32):
    """Custom type usdPppOsiTerminateNegFailOption based on Integer32"""
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


_UsdPppOsiTerminateNegFailOption_Type.__name__ = "Integer32"
_UsdPppOsiTerminateNegFailOption_Object = MibTableColumn
usdPppOsiTerminateNegFailOption = _UsdPppOsiTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 4),
    _UsdPppOsiTerminateNegFailOption_Type()
)
usdPppOsiTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppOsiTerminateNegFailOption.setStatus("current")


class _UsdPppOsiLocalAlignNpdu_Type(Integer32):
    """Custom type usdPppOsiLocalAlignNpdu based on Integer32"""
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


_UsdPppOsiLocalAlignNpdu_Type.__name__ = "Integer32"
_UsdPppOsiLocalAlignNpdu_Object = MibTableColumn
usdPppOsiLocalAlignNpdu = _UsdPppOsiLocalAlignNpdu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 5),
    _UsdPppOsiLocalAlignNpdu_Type()
)
usdPppOsiLocalAlignNpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppOsiLocalAlignNpdu.setStatus("current")


class _UsdPppOsiRemoteAlignNpdu_Type(Integer32):
    """Custom type usdPppOsiRemoteAlignNpdu based on Integer32"""
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


_UsdPppOsiRemoteAlignNpdu_Type.__name__ = "Integer32"
_UsdPppOsiRemoteAlignNpdu_Object = MibTableColumn
usdPppOsiRemoteAlignNpdu = _UsdPppOsiRemoteAlignNpdu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 6),
    _UsdPppOsiRemoteAlignNpdu_Type()
)
usdPppOsiRemoteAlignNpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppOsiRemoteAlignNpdu.setStatus("current")
_UsdPppOsiConfigTable_Object = MibTable
usdPppOsiConfigTable = _UsdPppOsiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 2)
)
if mibBuilder.loadTexts:
    usdPppOsiConfigTable.setStatus("current")
_UsdPppOsiConfigEntry_Object = MibTableRow
usdPppOsiConfigEntry = _UsdPppOsiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 2, 1)
)
usdPppOsiConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    usdPppOsiConfigEntry.setStatus("current")


class _UsdPppOsiConfigAdminStatus_Type(Integer32):
    """Custom type usdPppOsiConfigAdminStatus based on Integer32"""
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


_UsdPppOsiConfigAdminStatus_Type.__name__ = "Integer32"
_UsdPppOsiConfigAdminStatus_Object = MibTableColumn
usdPppOsiConfigAdminStatus = _UsdPppOsiConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 2, 1, 1),
    _UsdPppOsiConfigAdminStatus_Type()
)
usdPppOsiConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdPppOsiConfigAdminStatus.setStatus("current")
_UsdPppSession_ObjectIdentity = ObjectIdentity
usdPppSession = _UsdPppSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5)
)
_UsdPppSessionTable_Object = MibTable
usdPppSessionTable = _UsdPppSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1)
)
if mibBuilder.loadTexts:
    usdPppSessionTable.setStatus("current")
_UsdPppSessionEntry_Object = MibTableRow
usdPppSessionEntry = _UsdPppSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1)
)
usdPppSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    usdPppSessionEntry.setStatus("current")
_UsdPppSessionGrant_Type = TruthValue
_UsdPppSessionGrant_Object = MibTableColumn
usdPppSessionGrant = _UsdPppSessionGrant_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 1),
    _UsdPppSessionGrant_Type()
)
usdPppSessionGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionGrant.setStatus("current")


class _UsdPppSessionTerminateReason_Type(Integer32):
    """Custom type usdPppSessionTerminateReason based on Integer32"""
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
              17,
              18)
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
          ("tunnelFailed", 18),
          ("unknown", 1),
          ("userRequest", 2))
    )


_UsdPppSessionTerminateReason_Type.__name__ = "Integer32"
_UsdPppSessionTerminateReason_Object = MibTableColumn
usdPppSessionTerminateReason = _UsdPppSessionTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 2),
    _UsdPppSessionTerminateReason_Type()
)
usdPppSessionTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionTerminateReason.setStatus("current")
_UsdPppSessionStartTime_Type = TimeTicks
_UsdPppSessionStartTime_Object = MibTableColumn
usdPppSessionStartTime = _UsdPppSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 3),
    _UsdPppSessionStartTime_Type()
)
usdPppSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionStartTime.setStatus("current")
_UsdPppSessionInOctets_Type = Counter32
_UsdPppSessionInOctets_Object = MibTableColumn
usdPppSessionInOctets = _UsdPppSessionInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 4),
    _UsdPppSessionInOctets_Type()
)
usdPppSessionInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionInOctets.setStatus("current")
if mibBuilder.loadTexts:
    usdPppSessionInOctets.setUnits("octets")
_UsdPppSessionOutOctets_Type = Counter32
_UsdPppSessionOutOctets_Object = MibTableColumn
usdPppSessionOutOctets = _UsdPppSessionOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 5),
    _UsdPppSessionOutOctets_Type()
)
usdPppSessionOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    usdPppSessionOutOctets.setUnits("octets")
_UsdPppSessionInPackets_Type = Counter32
_UsdPppSessionInPackets_Object = MibTableColumn
usdPppSessionInPackets = _UsdPppSessionInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 6),
    _UsdPppSessionInPackets_Type()
)
usdPppSessionInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionInPackets.setStatus("current")
if mibBuilder.loadTexts:
    usdPppSessionInPackets.setUnits("packets")
_UsdPppSessionOutPackets_Type = Counter32
_UsdPppSessionOutPackets_Object = MibTableColumn
usdPppSessionOutPackets = _UsdPppSessionOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 7),
    _UsdPppSessionOutPackets_Type()
)
usdPppSessionOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    usdPppSessionOutPackets.setUnits("packets")


class _UsdPppSessionSessionTimeout_Type(Integer32):
    """Custom type usdPppSessionSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPppSessionSessionTimeout_Type.__name__ = "Integer32"
_UsdPppSessionSessionTimeout_Object = MibTableColumn
usdPppSessionSessionTimeout = _UsdPppSessionSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 8),
    _UsdPppSessionSessionTimeout_Type()
)
usdPppSessionSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    usdPppSessionSessionTimeout.setUnits("milliseconds")


class _UsdPppSessionInactivityTimeout_Type(Integer32):
    """Custom type usdPppSessionInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPppSessionInactivityTimeout_Type.__name__ = "Integer32"
_UsdPppSessionInactivityTimeout_Object = MibTableColumn
usdPppSessionInactivityTimeout = _UsdPppSessionInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 9),
    _UsdPppSessionInactivityTimeout_Type()
)
usdPppSessionInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    usdPppSessionInactivityTimeout.setUnits("milliseconds")


class _UsdPppSessionAccountingInterval_Type(Integer32):
    """Custom type usdPppSessionAccountingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_UsdPppSessionAccountingInterval_Type.__name__ = "Integer32"
_UsdPppSessionAccountingInterval_Object = MibTableColumn
usdPppSessionAccountingInterval = _UsdPppSessionAccountingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 10),
    _UsdPppSessionAccountingInterval_Type()
)
usdPppSessionAccountingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionAccountingInterval.setStatus("current")
if mibBuilder.loadTexts:
    usdPppSessionAccountingInterval.setUnits("milliseconds")
_UsdPppSessionRemoteIpAddress_Type = IpAddress
_UsdPppSessionRemoteIpAddress_Object = MibTableColumn
usdPppSessionRemoteIpAddress = _UsdPppSessionRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 11),
    _UsdPppSessionRemoteIpAddress_Type()
)
usdPppSessionRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionRemoteIpAddress.setStatus("current")
_UsdPppSessionRemotePrimaryDnsAddress_Type = IpAddress
_UsdPppSessionRemotePrimaryDnsAddress_Object = MibTableColumn
usdPppSessionRemotePrimaryDnsAddress = _UsdPppSessionRemotePrimaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 12),
    _UsdPppSessionRemotePrimaryDnsAddress_Type()
)
usdPppSessionRemotePrimaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionRemotePrimaryDnsAddress.setStatus("current")
_UsdPppSessionRemoteSecondaryDnsAddress_Type = IpAddress
_UsdPppSessionRemoteSecondaryDnsAddress_Object = MibTableColumn
usdPppSessionRemoteSecondaryDnsAddress = _UsdPppSessionRemoteSecondaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 13),
    _UsdPppSessionRemoteSecondaryDnsAddress_Type()
)
usdPppSessionRemoteSecondaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionRemoteSecondaryDnsAddress.setStatus("current")
_UsdPppSessionRemotePrimaryWinsAddress_Type = IpAddress
_UsdPppSessionRemotePrimaryWinsAddress_Object = MibTableColumn
usdPppSessionRemotePrimaryWinsAddress = _UsdPppSessionRemotePrimaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 14),
    _UsdPppSessionRemotePrimaryWinsAddress_Type()
)
usdPppSessionRemotePrimaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionRemotePrimaryWinsAddress.setStatus("current")
_UsdPppSessionRemoteSecondaryWinsAddress_Type = IpAddress
_UsdPppSessionRemoteSecondaryWinsAddress_Object = MibTableColumn
usdPppSessionRemoteSecondaryWinsAddress = _UsdPppSessionRemoteSecondaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 15),
    _UsdPppSessionRemoteSecondaryWinsAddress_Type()
)
usdPppSessionRemoteSecondaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSessionRemoteSecondaryWinsAddress.setStatus("current")
_UsdPppMlPpp_ObjectIdentity = ObjectIdentity
usdPppMlPpp = _UsdPppMlPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6)
)
_UsdPppMlPppBundleTable_Object = MibTable
usdPppMlPppBundleTable = _UsdPppMlPppBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 1)
)
if mibBuilder.loadTexts:
    usdPppMlPppBundleTable.setStatus("current")
_UsdPppMlPppBundleEntry_Object = MibTableRow
usdPppMlPppBundleEntry = _UsdPppMlPppBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 1, 1)
)
usdPppMlPppBundleEntry.setIndexNames(
    (0, "Unisphere-Data-PPP-MIB", "usdPppMlPppBundleName"),
)
if mibBuilder.loadTexts:
    usdPppMlPppBundleEntry.setStatus("current")
_UsdPppMlPppBundleName_Type = UsdPppMlPppBundleName
_UsdPppMlPppBundleName_Object = MibTableColumn
usdPppMlPppBundleName = _UsdPppMlPppBundleName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 1, 1, 1),
    _UsdPppMlPppBundleName_Type()
)
usdPppMlPppBundleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPppMlPppBundleName.setStatus("current")
_UsdPppMlPppBundleRowStatus_Type = RowStatus
_UsdPppMlPppBundleRowStatus_Object = MibTableColumn
usdPppMlPppBundleRowStatus = _UsdPppMlPppBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 1, 1, 2),
    _UsdPppMlPppBundleRowStatus_Type()
)
usdPppMlPppBundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppMlPppBundleRowStatus.setStatus("current")
_UsdPppMlPppBundleNetworkIfIndex_Type = InterfaceIndex
_UsdPppMlPppBundleNetworkIfIndex_Object = MibTableColumn
usdPppMlPppBundleNetworkIfIndex = _UsdPppMlPppBundleNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 1, 1, 3),
    _UsdPppMlPppBundleNetworkIfIndex_Type()
)
usdPppMlPppBundleNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppMlPppBundleNetworkIfIndex.setStatus("current")
_UsdPppMlPppNextLinkIfIndex_Type = UsdNextIfIndex
_UsdPppMlPppNextLinkIfIndex_Object = MibScalar
usdPppMlPppNextLinkIfIndex = _UsdPppMlPppNextLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 2),
    _UsdPppMlPppNextLinkIfIndex_Type()
)
usdPppMlPppNextLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppMlPppNextLinkIfIndex.setStatus("current")
_UsdPppMlPppLinkConfigTable_Object = MibTable
usdPppMlPppLinkConfigTable = _UsdPppMlPppLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3)
)
if mibBuilder.loadTexts:
    usdPppMlPppLinkConfigTable.setStatus("current")
_UsdPppMlPppLinkConfigEntry_Object = MibTableRow
usdPppMlPppLinkConfigEntry = _UsdPppMlPppLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1)
)
usdPppMlPppLinkConfigEntry.setIndexNames(
    (0, "Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    usdPppMlPppLinkConfigEntry.setStatus("current")
_UsdPppMlPppLinkConfigIfIndex_Type = InterfaceIndex
_UsdPppMlPppLinkConfigIfIndex_Object = MibTableColumn
usdPppMlPppLinkConfigIfIndex = _UsdPppMlPppLinkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 1),
    _UsdPppMlPppLinkConfigIfIndex_Type()
)
usdPppMlPppLinkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPppMlPppLinkConfigIfIndex.setStatus("current")
_UsdPppMlPppLinkConfigLowerIfIndex_Type = InterfaceIndexOrZero
_UsdPppMlPppLinkConfigLowerIfIndex_Object = MibTableColumn
usdPppMlPppLinkConfigLowerIfIndex = _UsdPppMlPppLinkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 2),
    _UsdPppMlPppLinkConfigLowerIfIndex_Type()
)
usdPppMlPppLinkConfigLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppMlPppLinkConfigLowerIfIndex.setStatus("current")


class _UsdPppMlPppLinkConfigKeepalive_Type(Integer32):
    """Custom type usdPppMlPppLinkConfigKeepalive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 300),
    )


_UsdPppMlPppLinkConfigKeepalive_Type.__name__ = "Integer32"
_UsdPppMlPppLinkConfigKeepalive_Object = MibTableColumn
usdPppMlPppLinkConfigKeepalive = _UsdPppMlPppLinkConfigKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 4),
    _UsdPppMlPppLinkConfigKeepalive_Type()
)
usdPppMlPppLinkConfigKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppMlPppLinkConfigKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    usdPppMlPppLinkConfigKeepalive.setUnits("seconds")


class _UsdPppMlPppLinkConfigAuthentication_Type(UsdPppAuthentication):
    """Custom type usdPppMlPppLinkConfigAuthentication based on UsdPppAuthentication"""


_UsdPppMlPppLinkConfigAuthentication_Object = MibTableColumn
usdPppMlPppLinkConfigAuthentication = _UsdPppMlPppLinkConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 5),
    _UsdPppMlPppLinkConfigAuthentication_Type()
)
usdPppMlPppLinkConfigAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppMlPppLinkConfigAuthentication.setStatus("current")


class _UsdPppMlPppLinkConfigMaxAuthenRetries_Type(Integer32):
    """Custom type usdPppMlPppLinkConfigMaxAuthenRetries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_UsdPppMlPppLinkConfigMaxAuthenRetries_Type.__name__ = "Integer32"
_UsdPppMlPppLinkConfigMaxAuthenRetries_Object = MibTableColumn
usdPppMlPppLinkConfigMaxAuthenRetries = _UsdPppMlPppLinkConfigMaxAuthenRetries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 6),
    _UsdPppMlPppLinkConfigMaxAuthenRetries_Type()
)
usdPppMlPppLinkConfigMaxAuthenRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppMlPppLinkConfigMaxAuthenRetries.setStatus("current")
_UsdPppMlPppLinkConfigRowStatus_Type = RowStatus
_UsdPppMlPppLinkConfigRowStatus_Object = MibTableColumn
usdPppMlPppLinkConfigRowStatus = _UsdPppMlPppLinkConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 7),
    _UsdPppMlPppLinkConfigRowStatus_Type()
)
usdPppMlPppLinkConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppMlPppLinkConfigRowStatus.setStatus("current")
_UsdPppMlPppNextNetworkIfIndex_Type = UsdNextIfIndex
_UsdPppMlPppNextNetworkIfIndex_Object = MibScalar
usdPppMlPppNextNetworkIfIndex = _UsdPppMlPppNextNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 4),
    _UsdPppMlPppNextNetworkIfIndex_Type()
)
usdPppMlPppNextNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppMlPppNextNetworkIfIndex.setStatus("current")
_UsdPppMlPppNetworkConfigTable_Object = MibTable
usdPppMlPppNetworkConfigTable = _UsdPppMlPppNetworkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5)
)
if mibBuilder.loadTexts:
    usdPppMlPppNetworkConfigTable.setStatus("current")
_UsdPppMlPppNetworkConfigEntry_Object = MibTableRow
usdPppMlPppNetworkConfigEntry = _UsdPppMlPppNetworkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5, 1)
)
usdPppMlPppNetworkConfigEntry.setIndexNames(
    (0, "Unisphere-Data-PPP-MIB", "usdPppMlPppNetworkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    usdPppMlPppNetworkConfigEntry.setStatus("current")
_UsdPppMlPppNetworkConfigIfIndex_Type = InterfaceIndex
_UsdPppMlPppNetworkConfigIfIndex_Object = MibTableColumn
usdPppMlPppNetworkConfigIfIndex = _UsdPppMlPppNetworkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5, 1, 1),
    _UsdPppMlPppNetworkConfigIfIndex_Type()
)
usdPppMlPppNetworkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPppMlPppNetworkConfigIfIndex.setStatus("current")
_UsdPppMlPppNetworkConfigLowerIfIndex_Type = InterfaceIndex
_UsdPppMlPppNetworkConfigLowerIfIndex_Object = MibTableColumn
usdPppMlPppNetworkConfigLowerIfIndex = _UsdPppMlPppNetworkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5, 1, 2),
    _UsdPppMlPppNetworkConfigLowerIfIndex_Type()
)
usdPppMlPppNetworkConfigLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppMlPppNetworkConfigLowerIfIndex.setStatus("current")
_UsdPppMlPppNetworkBundleName_Type = UsdPppMlPppBundleName
_UsdPppMlPppNetworkBundleName_Object = MibTableColumn
usdPppMlPppNetworkBundleName = _UsdPppMlPppNetworkBundleName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5, 1, 3),
    _UsdPppMlPppNetworkBundleName_Type()
)
usdPppMlPppNetworkBundleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppMlPppNetworkBundleName.setStatus("current")
_UsdPppMlPppNetworkRowStatus_Type = RowStatus
_UsdPppMlPppNetworkRowStatus_Object = MibTableColumn
usdPppMlPppNetworkRowStatus = _UsdPppMlPppNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5, 1, 4),
    _UsdPppMlPppNetworkRowStatus_Type()
)
usdPppMlPppNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppMlPppNetworkRowStatus.setStatus("current")
_UsdPppMlPppLinkBindTable_Object = MibTable
usdPppMlPppLinkBindTable = _UsdPppMlPppLinkBindTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 6)
)
if mibBuilder.loadTexts:
    usdPppMlPppLinkBindTable.setStatus("current")
_UsdPppMlPppLinkBindEntry_Object = MibTableRow
usdPppMlPppLinkBindEntry = _UsdPppMlPppLinkBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 6, 1)
)
usdPppMlPppLinkBindEntry.setIndexNames(
    (0, "Unisphere-Data-PPP-MIB", "usdPppMlPppBindNetworkIfIndex"),
    (0, "Unisphere-Data-PPP-MIB", "usdPppMlPppBindLinkIfIndex"),
)
if mibBuilder.loadTexts:
    usdPppMlPppLinkBindEntry.setStatus("current")
_UsdPppMlPppBindNetworkIfIndex_Type = InterfaceIndex
_UsdPppMlPppBindNetworkIfIndex_Object = MibTableColumn
usdPppMlPppBindNetworkIfIndex = _UsdPppMlPppBindNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 6, 1, 1),
    _UsdPppMlPppBindNetworkIfIndex_Type()
)
usdPppMlPppBindNetworkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPppMlPppBindNetworkIfIndex.setStatus("current")
_UsdPppMlPppBindLinkIfIndex_Type = InterfaceIndex
_UsdPppMlPppBindLinkIfIndex_Object = MibTableColumn
usdPppMlPppBindLinkIfIndex = _UsdPppMlPppBindLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 6, 1, 2),
    _UsdPppMlPppBindLinkIfIndex_Type()
)
usdPppMlPppBindLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdPppMlPppBindLinkIfIndex.setStatus("current")
_UsdPppMlPppBindRowStatus_Type = RowStatus
_UsdPppMlPppBindRowStatus_Object = MibTableColumn
usdPppMlPppBindRowStatus = _UsdPppMlPppBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 6, 1, 3),
    _UsdPppMlPppBindRowStatus_Type()
)
usdPppMlPppBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdPppMlPppBindRowStatus.setStatus("current")
_UsdPppSummary_ObjectIdentity = ObjectIdentity
usdPppSummary = _UsdPppSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7)
)
_UsdPppSummaryPppInterfaceCount_Type = Integer32
_UsdPppSummaryPppInterfaceCount_Object = MibScalar
usdPppSummaryPppInterfaceCount = _UsdPppSummaryPppInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 1),
    _UsdPppSummaryPppInterfaceCount_Type()
)
usdPppSummaryPppInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppInterfaceCount.setStatus("current")
_UsdPppSummaryPppIpNCPs_Type = Integer32
_UsdPppSummaryPppIpNCPs_Object = MibScalar
usdPppSummaryPppIpNCPs = _UsdPppSummaryPppIpNCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 2),
    _UsdPppSummaryPppIpNCPs_Type()
)
usdPppSummaryPppIpNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIpNCPs.setStatus("current")
_UsdPppSummaryPppOsiNCPs_Type = Integer32
_UsdPppSummaryPppOsiNCPs_Object = MibScalar
usdPppSummaryPppOsiNCPs = _UsdPppSummaryPppOsiNCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 3),
    _UsdPppSummaryPppOsiNCPs_Type()
)
usdPppSummaryPppOsiNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppOsiNCPs.setStatus("current")
_UsdPppSummaryPppIfAdminUp_Type = Integer32
_UsdPppSummaryPppIfAdminUp_Object = MibScalar
usdPppSummaryPppIfAdminUp = _UsdPppSummaryPppIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 4),
    _UsdPppSummaryPppIfAdminUp_Type()
)
usdPppSummaryPppIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIfAdminUp.setStatus("current")
_UsdPppSummaryPppIfAdminDown_Type = Integer32
_UsdPppSummaryPppIfAdminDown_Object = MibScalar
usdPppSummaryPppIfAdminDown = _UsdPppSummaryPppIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 5),
    _UsdPppSummaryPppIfAdminDown_Type()
)
usdPppSummaryPppIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIfAdminDown.setStatus("current")
_UsdPppSummaryPppIfOperUp_Type = Integer32
_UsdPppSummaryPppIfOperUp_Object = MibScalar
usdPppSummaryPppIfOperUp = _UsdPppSummaryPppIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 7),
    _UsdPppSummaryPppIfOperUp_Type()
)
usdPppSummaryPppIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIfOperUp.setStatus("current")
_UsdPppSummaryPppIfOperDown_Type = Integer32
_UsdPppSummaryPppIfOperDown_Object = MibScalar
usdPppSummaryPppIfOperDown = _UsdPppSummaryPppIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 8),
    _UsdPppSummaryPppIfOperDown_Type()
)
usdPppSummaryPppIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIfOperDown.setStatus("current")
_UsdPppSummaryPppIfOperDormant_Type = Integer32
_UsdPppSummaryPppIfOperDormant_Object = MibScalar
usdPppSummaryPppIfOperDormant = _UsdPppSummaryPppIfOperDormant_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 9),
    _UsdPppSummaryPppIfOperDormant_Type()
)
usdPppSummaryPppIfOperDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIfOperDormant.setStatus("current")
_UsdPppSummaryPppIfNotPresent_Type = Integer32
_UsdPppSummaryPppIfNotPresent_Object = MibScalar
usdPppSummaryPppIfNotPresent = _UsdPppSummaryPppIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 10),
    _UsdPppSummaryPppIfNotPresent_Type()
)
usdPppSummaryPppIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIfNotPresent.setStatus("current")
_UsdPppSummaryPppIfLowerLayerDown_Type = Integer32
_UsdPppSummaryPppIfLowerLayerDown_Object = MibScalar
usdPppSummaryPppIfLowerLayerDown = _UsdPppSummaryPppIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 11),
    _UsdPppSummaryPppIfLowerLayerDown_Type()
)
usdPppSummaryPppIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIfLowerLayerDown.setStatus("current")
_UsdPppSummaryPppIpNcpOpened_Type = Integer32
_UsdPppSummaryPppIpNcpOpened_Object = MibScalar
usdPppSummaryPppIpNcpOpened = _UsdPppSummaryPppIpNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 12),
    _UsdPppSummaryPppIpNcpOpened_Type()
)
usdPppSummaryPppIpNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIpNcpOpened.setStatus("current")
_UsdPppSummaryPppIpNcpClosed_Type = Integer32
_UsdPppSummaryPppIpNcpClosed_Object = MibScalar
usdPppSummaryPppIpNcpClosed = _UsdPppSummaryPppIpNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 13),
    _UsdPppSummaryPppIpNcpClosed_Type()
)
usdPppSummaryPppIpNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIpNcpClosed.setStatus("current")
_UsdPppSummaryPppOsiNcpOpened_Type = Integer32
_UsdPppSummaryPppOsiNcpOpened_Object = MibScalar
usdPppSummaryPppOsiNcpOpened = _UsdPppSummaryPppOsiNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 14),
    _UsdPppSummaryPppOsiNcpOpened_Type()
)
usdPppSummaryPppOsiNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppOsiNcpOpened.setStatus("current")
_UsdPppSummaryPppOsiNcpClosed_Type = Integer32
_UsdPppSummaryPppOsiNcpClosed_Object = MibScalar
usdPppSummaryPppOsiNcpClosed = _UsdPppSummaryPppOsiNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 15),
    _UsdPppSummaryPppOsiNcpClosed_Type()
)
usdPppSummaryPppOsiNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppOsiNcpClosed.setStatus("current")
_UsdPppSummaryPppIfLastChangeTime_Type = TimeTicks
_UsdPppSummaryPppIfLastChangeTime_Object = MibScalar
usdPppSummaryPppIfLastChangeTime = _UsdPppSummaryPppIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 16),
    _UsdPppSummaryPppIfLastChangeTime_Type()
)
usdPppSummaryPppIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppIfLastChangeTime.setStatus("current")
_UsdPppSummaryPppLinkInterfaceCount_Type = Integer32
_UsdPppSummaryPppLinkInterfaceCount_Object = MibScalar
usdPppSummaryPppLinkInterfaceCount = _UsdPppSummaryPppLinkInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 17),
    _UsdPppSummaryPppLinkInterfaceCount_Type()
)
usdPppSummaryPppLinkInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppLinkInterfaceCount.setStatus("current")
_UsdPppSummaryPppLinkIfAdminUp_Type = Integer32
_UsdPppSummaryPppLinkIfAdminUp_Object = MibScalar
usdPppSummaryPppLinkIfAdminUp = _UsdPppSummaryPppLinkIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 18),
    _UsdPppSummaryPppLinkIfAdminUp_Type()
)
usdPppSummaryPppLinkIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppLinkIfAdminUp.setStatus("current")
_UsdPppSummaryPppLinkIfAdminDown_Type = Integer32
_UsdPppSummaryPppLinkIfAdminDown_Object = MibScalar
usdPppSummaryPppLinkIfAdminDown = _UsdPppSummaryPppLinkIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 19),
    _UsdPppSummaryPppLinkIfAdminDown_Type()
)
usdPppSummaryPppLinkIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppLinkIfAdminDown.setStatus("current")
_UsdPppSummaryPppLinkIfOperUp_Type = Integer32
_UsdPppSummaryPppLinkIfOperUp_Object = MibScalar
usdPppSummaryPppLinkIfOperUp = _UsdPppSummaryPppLinkIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 20),
    _UsdPppSummaryPppLinkIfOperUp_Type()
)
usdPppSummaryPppLinkIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppLinkIfOperUp.setStatus("current")
_UsdPppSummaryPppLinkIfOperDown_Type = Integer32
_UsdPppSummaryPppLinkIfOperDown_Object = MibScalar
usdPppSummaryPppLinkIfOperDown = _UsdPppSummaryPppLinkIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 21),
    _UsdPppSummaryPppLinkIfOperDown_Type()
)
usdPppSummaryPppLinkIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppLinkIfOperDown.setStatus("current")
_UsdPppSummaryPppLinkIfOperDormant_Type = Integer32
_UsdPppSummaryPppLinkIfOperDormant_Object = MibScalar
usdPppSummaryPppLinkIfOperDormant = _UsdPppSummaryPppLinkIfOperDormant_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 22),
    _UsdPppSummaryPppLinkIfOperDormant_Type()
)
usdPppSummaryPppLinkIfOperDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppLinkIfOperDormant.setStatus("current")
_UsdPppSummaryPppLinkIfNotPresent_Type = Integer32
_UsdPppSummaryPppLinkIfNotPresent_Object = MibScalar
usdPppSummaryPppLinkIfNotPresent = _UsdPppSummaryPppLinkIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 23),
    _UsdPppSummaryPppLinkIfNotPresent_Type()
)
usdPppSummaryPppLinkIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppLinkIfNotPresent.setStatus("current")
_UsdPppSummaryPppLinkIfLowerLayerDown_Type = Integer32
_UsdPppSummaryPppLinkIfLowerLayerDown_Object = MibScalar
usdPppSummaryPppLinkIfLowerLayerDown = _UsdPppSummaryPppLinkIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 24),
    _UsdPppSummaryPppLinkIfLowerLayerDown_Type()
)
usdPppSummaryPppLinkIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppLinkIfLowerLayerDown.setStatus("current")
_UsdPppSummaryPppLinkIfLastChangeTime_Type = TimeTicks
_UsdPppSummaryPppLinkIfLastChangeTime_Object = MibScalar
usdPppSummaryPppLinkIfLastChangeTime = _UsdPppSummaryPppLinkIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 25),
    _UsdPppSummaryPppLinkIfLastChangeTime_Type()
)
usdPppSummaryPppLinkIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppLinkIfLastChangeTime.setStatus("current")
_UsdPppSummaryPppNetworkInterfaceCount_Type = Integer32
_UsdPppSummaryPppNetworkInterfaceCount_Object = MibScalar
usdPppSummaryPppNetworkInterfaceCount = _UsdPppSummaryPppNetworkInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 26),
    _UsdPppSummaryPppNetworkInterfaceCount_Type()
)
usdPppSummaryPppNetworkInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkInterfaceCount.setStatus("current")
_UsdPppSummaryPppNetworkIpNCPs_Type = Integer32
_UsdPppSummaryPppNetworkIpNCPs_Object = MibScalar
usdPppSummaryPppNetworkIpNCPs = _UsdPppSummaryPppNetworkIpNCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 27),
    _UsdPppSummaryPppNetworkIpNCPs_Type()
)
usdPppSummaryPppNetworkIpNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIpNCPs.setStatus("current")
_UsdPppSummaryPppNetworkOsiNCPs_Type = Integer32
_UsdPppSummaryPppNetworkOsiNCPs_Object = MibScalar
usdPppSummaryPppNetworkOsiNCPs = _UsdPppSummaryPppNetworkOsiNCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 28),
    _UsdPppSummaryPppNetworkOsiNCPs_Type()
)
usdPppSummaryPppNetworkOsiNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkOsiNCPs.setStatus("current")
_UsdPppSummaryPppNetworkIfAdminUp_Type = Integer32
_UsdPppSummaryPppNetworkIfAdminUp_Object = MibScalar
usdPppSummaryPppNetworkIfAdminUp = _UsdPppSummaryPppNetworkIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 29),
    _UsdPppSummaryPppNetworkIfAdminUp_Type()
)
usdPppSummaryPppNetworkIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIfAdminUp.setStatus("current")
_UsdPppSummaryPppNetworkIfAdminDown_Type = Integer32
_UsdPppSummaryPppNetworkIfAdminDown_Object = MibScalar
usdPppSummaryPppNetworkIfAdminDown = _UsdPppSummaryPppNetworkIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 30),
    _UsdPppSummaryPppNetworkIfAdminDown_Type()
)
usdPppSummaryPppNetworkIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIfAdminDown.setStatus("current")
_UsdPppSummaryPppNetworkIfOperUp_Type = Integer32
_UsdPppSummaryPppNetworkIfOperUp_Object = MibScalar
usdPppSummaryPppNetworkIfOperUp = _UsdPppSummaryPppNetworkIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 31),
    _UsdPppSummaryPppNetworkIfOperUp_Type()
)
usdPppSummaryPppNetworkIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIfOperUp.setStatus("current")
_UsdPppSummaryPppNetworkIfOperDown_Type = Integer32
_UsdPppSummaryPppNetworkIfOperDown_Object = MibScalar
usdPppSummaryPppNetworkIfOperDown = _UsdPppSummaryPppNetworkIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 32),
    _UsdPppSummaryPppNetworkIfOperDown_Type()
)
usdPppSummaryPppNetworkIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIfOperDown.setStatus("current")
_UsdPppSummaryPppNetworkIfOperDormant_Type = Integer32
_UsdPppSummaryPppNetworkIfOperDormant_Object = MibScalar
usdPppSummaryPppNetworkIfOperDormant = _UsdPppSummaryPppNetworkIfOperDormant_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 33),
    _UsdPppSummaryPppNetworkIfOperDormant_Type()
)
usdPppSummaryPppNetworkIfOperDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIfOperDormant.setStatus("current")
_UsdPppSummaryPppNetworkIfNotPresent_Type = Integer32
_UsdPppSummaryPppNetworkIfNotPresent_Object = MibScalar
usdPppSummaryPppNetworkIfNotPresent = _UsdPppSummaryPppNetworkIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 34),
    _UsdPppSummaryPppNetworkIfNotPresent_Type()
)
usdPppSummaryPppNetworkIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIfNotPresent.setStatus("current")
_UsdPppSummaryPppNetworkIfLowerLayerDown_Type = Integer32
_UsdPppSummaryPppNetworkIfLowerLayerDown_Object = MibScalar
usdPppSummaryPppNetworkIfLowerLayerDown = _UsdPppSummaryPppNetworkIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 35),
    _UsdPppSummaryPppNetworkIfLowerLayerDown_Type()
)
usdPppSummaryPppNetworkIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIfLowerLayerDown.setStatus("current")
_UsdPppSummaryPppNetworkIpNcpOpened_Type = Integer32
_UsdPppSummaryPppNetworkIpNcpOpened_Object = MibScalar
usdPppSummaryPppNetworkIpNcpOpened = _UsdPppSummaryPppNetworkIpNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 36),
    _UsdPppSummaryPppNetworkIpNcpOpened_Type()
)
usdPppSummaryPppNetworkIpNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIpNcpOpened.setStatus("current")
_UsdPppSummaryPppNetworkIpNcpClosed_Type = Integer32
_UsdPppSummaryPppNetworkIpNcpClosed_Object = MibScalar
usdPppSummaryPppNetworkIpNcpClosed = _UsdPppSummaryPppNetworkIpNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 37),
    _UsdPppSummaryPppNetworkIpNcpClosed_Type()
)
usdPppSummaryPppNetworkIpNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIpNcpClosed.setStatus("current")
_UsdPppSummaryPppNetworkOsiNcpOpened_Type = Integer32
_UsdPppSummaryPppNetworkOsiNcpOpened_Object = MibScalar
usdPppSummaryPppNetworkOsiNcpOpened = _UsdPppSummaryPppNetworkOsiNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 38),
    _UsdPppSummaryPppNetworkOsiNcpOpened_Type()
)
usdPppSummaryPppNetworkOsiNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkOsiNcpOpened.setStatus("current")
_UsdPppSummaryPppNetworkOsiNcpClosed_Type = Integer32
_UsdPppSummaryPppNetworkOsiNcpClosed_Object = MibScalar
usdPppSummaryPppNetworkOsiNcpClosed = _UsdPppSummaryPppNetworkOsiNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 39),
    _UsdPppSummaryPppNetworkOsiNcpClosed_Type()
)
usdPppSummaryPppNetworkOsiNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkOsiNcpClosed.setStatus("current")
_UsdPppSummaryPppNetworkIfLastChangeTime_Type = TimeTicks
_UsdPppSummaryPppNetworkIfLastChangeTime_Object = MibScalar
usdPppSummaryPppNetworkIfLastChangeTime = _UsdPppSummaryPppNetworkIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 40),
    _UsdPppSummaryPppNetworkIfLastChangeTime_Type()
)
usdPppSummaryPppNetworkIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdPppSummaryPppNetworkIfLastChangeTime.setStatus("current")
_UsdPppConformance_ObjectIdentity = ObjectIdentity
usdPppConformance = _UsdPppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4)
)
_UsdPppCompliances_ObjectIdentity = ObjectIdentity
usdPppCompliances = _UsdPppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1)
)
_UsdPppGroups_ObjectIdentity = ObjectIdentity
usdPppGroups = _UsdPppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2)
)

# Managed Objects groups

usdPppLcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 1)
)
usdPppLcpGroup.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppLinkConfigRowStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigLowerIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    usdPppLcpGroup.setStatus("obsolete")

usdPppIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 2)
)
usdPppIpGroup.setObjects(
    ("Unisphere-Data-PPP-MIB", "usdPppIpServiceStatus")
)
if mibBuilder.loadTexts:
    usdPppIpGroup.setStatus("obsolete")

usdPppOsiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 3)
)
usdPppOsiGroup.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppOsiServiceStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppOsiOperStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppOsiConfigAdminStatus"))
)
if mibBuilder.loadTexts:
    usdPppOsiGroup.setStatus("obsolete")

usdPppLcpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 4)
)
usdPppLcpGroup2.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppLinkStatusTerminateReason"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusTerminateNegFailOption"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusInKeepaliveRequests"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusOutKeepaliveRequests"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusInKeepaliveReplies"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusOutKeepaliveReplies"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusKeepaliveFailures"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusLocalMagicNumber"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusRemoteMagicNumber"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusLocalAuthentication"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusTunnelIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigRowStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigLowerIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigKeepalive"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigAuthentication"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigMaxAuthenRetries"),
        ("Unisphere-Data-PPP-MIB", "usdPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    usdPppLcpGroup2.setStatus("obsolete")

usdPppIpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 5)
)
usdPppIpGroup2.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppIpServiceStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpTerminateReason"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpTerminateNegFailOption"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpLocalIpAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpRemoteIpAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpRemotePrimaryDnsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpRemoteSecondaryDnsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpRemotePrimaryWinsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpRemoteSecondaryWinsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpConfigPeerDnsPriority"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpConfigPeerWinsPriority"))
)
if mibBuilder.loadTexts:
    usdPppIpGroup2.setStatus("obsolete")

usdPppOsiGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 6)
)
usdPppOsiGroup2.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppOsiServiceStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppOsiOperStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppOsiTerminateReason"),
        ("Unisphere-Data-PPP-MIB", "usdPppOsiTerminateNegFailOption"),
        ("Unisphere-Data-PPP-MIB", "usdPppOsiLocalAlignNpdu"),
        ("Unisphere-Data-PPP-MIB", "usdPppOsiRemoteAlignNpdu"),
        ("Unisphere-Data-PPP-MIB", "usdPppOsiConfigAdminStatus"))
)
if mibBuilder.loadTexts:
    usdPppOsiGroup2.setStatus("current")

usdPppSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 7)
)
usdPppSessionGroup.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppSessionGrant"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionTerminateReason"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionStartTime"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionInOctets"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionOutOctets"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionInPackets"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionOutPackets"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionSessionTimeout"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionInactivityTimeout"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionAccountingInterval"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionRemoteIpAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionRemotePrimaryDnsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionRemoteSecondaryDnsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionRemotePrimaryWinsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppSessionRemoteSecondaryWinsAddress"))
)
if mibBuilder.loadTexts:
    usdPppSessionGroup.setStatus("current")

usdPppMlPppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 8)
)
usdPppMlPppGroup.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppMlPppBundleRowStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppNextLinkIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigLowerIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigKeepalive"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigAuthentication"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigMaxAuthenRetries"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigRowStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppNextNetworkIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppNetworkConfigLowerIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppNetworkBundleName"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppNetworkRowStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppBindRowStatus"))
)
if mibBuilder.loadTexts:
    usdPppMlPppGroup.setStatus("obsolete")

usdPppSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 9)
)
usdPppSummaryGroup.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppSummaryPppInterfaceCount"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIpNCPs"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppOsiNCPs"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfAdminUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfAdminDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfOperUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfOperDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfOperDormant"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfNotPresent"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfLowerLayerDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfLastChangeTime"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkInterfaceCount"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfAdminUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfAdminDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfOperUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfOperDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfOperDormant"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfNotPresent"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfLowerLayerDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfLastChangeTime"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkInterfaceCount"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIpNCPs"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkOsiNCPs"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfAdminUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfAdminDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfOperUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfOperDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfOperDormant"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfNotPresent"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfLowerLayerDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfLastChangeTime"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIpNcpOpened"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIpNcpClosed"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppOsiNcpOpened"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppOsiNcpClosed"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIpNcpOpened"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIpNcpClosed"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkOsiNcpOpened"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkOsiNcpClosed"))
)
if mibBuilder.loadTexts:
    usdPppSummaryGroup.setStatus("obsolete")

usdPppLcpGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 10)
)
usdPppLcpGroup3.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppLinkStatusTerminateReason"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusTerminateNegFailOption"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusInKeepaliveRequests"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusOutKeepaliveRequests"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusInKeepaliveReplies"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusOutKeepaliveReplies"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusKeepaliveFailures"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusLocalMagicNumber"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusRemoteMagicNumber"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusLocalAuthentication"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusTunnelIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigRowStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigLowerIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigKeepalive"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigAuthentication"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigMaxAuthenRetries"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigStandardIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    usdPppLcpGroup3.setStatus("obsolete")

usdPppSummaryBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 11)
)
usdPppSummaryBasicGroup.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppSummaryPppInterfaceCount"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIpNCPs"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppOsiNCPs"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfAdminUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfAdminDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfOperUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfOperDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfOperDormant"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfNotPresent"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfLowerLayerDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIfLastChangeTime"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIpNcpOpened"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppIpNcpClosed"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppOsiNcpOpened"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppOsiNcpClosed"))
)
if mibBuilder.loadTexts:
    usdPppSummaryBasicGroup.setStatus("current")

usdPppSummaryLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 12)
)
usdPppSummaryLinkGroup.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkInterfaceCount"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfAdminUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfAdminDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfOperUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfOperDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfOperDormant"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfNotPresent"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfLowerLayerDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppLinkIfLastChangeTime"))
)
if mibBuilder.loadTexts:
    usdPppSummaryLinkGroup.setStatus("current")

usdPppSummaryNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 13)
)
usdPppSummaryNetworkGroup.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkInterfaceCount"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIpNCPs"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkOsiNCPs"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfAdminUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfAdminDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfOperUp"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfOperDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfOperDormant"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfNotPresent"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfLowerLayerDown"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIfLastChangeTime"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIpNcpOpened"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkIpNcpClosed"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkOsiNcpOpened"),
        ("Unisphere-Data-PPP-MIB", "usdPppSummaryPppNetworkOsiNcpClosed"))
)
if mibBuilder.loadTexts:
    usdPppSummaryNetworkGroup.setStatus("current")

usdPppLcpGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 14)
)
usdPppLcpGroup4.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppLinkStatusTerminateReason"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusTerminateNegFailOption"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusInKeepaliveRequests"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusOutKeepaliveRequests"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusInKeepaliveReplies"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusOutKeepaliveReplies"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusKeepaliveFailures"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusLocalMagicNumber"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusRemoteMagicNumber"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusLocalAuthentication"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkStatusTunnelIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigRowStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigLowerIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigKeepalive"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigAuthentication"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigMaxAuthenRetries"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigStandardIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigChapMinChallengeLength"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigChapMaxChallengeLength"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigPassiveMode"),
        ("Unisphere-Data-PPP-MIB", "usdPppLinkConfigAuthenticatorVirtualRouter"),
        ("Unisphere-Data-PPP-MIB", "usdPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    usdPppLcpGroup4.setStatus("current")

usdPppIpGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 15)
)
usdPppIpGroup3.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppIpServiceStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpTerminateReason"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpTerminateNegFailOption"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpLocalIpAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpRemoteIpAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpRemotePrimaryDnsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpRemoteSecondaryDnsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpRemotePrimaryWinsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpRemoteSecondaryWinsAddress"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpConfigPeerDnsPriority"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpConfigPeerWinsPriority"),
        ("Unisphere-Data-PPP-MIB", "usdPppIpConfigIpcpNetmask"))
)
if mibBuilder.loadTexts:
    usdPppIpGroup3.setStatus("current")

usdPppMlPppGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 16)
)
usdPppMlPppGroup2.setObjects(
      *(("Unisphere-Data-PPP-MIB", "usdPppMlPppBundleRowStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppBundleNetworkIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppNextLinkIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigLowerIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigKeepalive"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigAuthentication"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigMaxAuthenRetries"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppLinkConfigRowStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppNetworkConfigLowerIfIndex"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppNetworkBundleName"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppNetworkRowStatus"),
        ("Unisphere-Data-PPP-MIB", "usdPppMlPppBindRowStatus"))
)
if mibBuilder.loadTexts:
    usdPppMlPppGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdPppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdPppCompliance.setStatus(
        "obsolete"
    )

usdPppCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdPppCompliance2.setStatus(
        "obsolete"
    )

usdPppCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdPppCompliance3.setStatus(
        "obsolete"
    )

usdPppCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 4)
)
if mibBuilder.loadTexts:
    usdPppCompliance4.setStatus(
        "obsolete"
    )

usdPppCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 5)
)
if mibBuilder.loadTexts:
    usdPppCompliance5.setStatus(
        "obsolete"
    )

usdPppCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 6)
)
if mibBuilder.loadTexts:
    usdPppCompliance6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-PPP-MIB",
    **{"UsdPppAuthentication": UsdPppAuthentication,
       "UsdPppMlPppBundleName": UsdPppMlPppBundleName,
       "usdPppMIB": usdPppMIB,
       "usdPppObjects": usdPppObjects,
       "usdPppLcp": usdPppLcp,
       "usdPppLinkStatusTable": usdPppLinkStatusTable,
       "usdPppLinkStatusEntry": usdPppLinkStatusEntry,
       "usdPppLinkStatusTerminateReason": usdPppLinkStatusTerminateReason,
       "usdPppLinkStatusTerminateNegFailOption": usdPppLinkStatusTerminateNegFailOption,
       "usdPppLinkStatusInKeepaliveRequests": usdPppLinkStatusInKeepaliveRequests,
       "usdPppLinkStatusOutKeepaliveRequests": usdPppLinkStatusOutKeepaliveRequests,
       "usdPppLinkStatusInKeepaliveReplies": usdPppLinkStatusInKeepaliveReplies,
       "usdPppLinkStatusOutKeepaliveReplies": usdPppLinkStatusOutKeepaliveReplies,
       "usdPppLinkStatusKeepaliveFailures": usdPppLinkStatusKeepaliveFailures,
       "usdPppLinkStatusLocalMagicNumber": usdPppLinkStatusLocalMagicNumber,
       "usdPppLinkStatusRemoteMagicNumber": usdPppLinkStatusRemoteMagicNumber,
       "usdPppLinkStatusLocalAuthentication": usdPppLinkStatusLocalAuthentication,
       "usdPppLinkStatusTunnelIfIndex": usdPppLinkStatusTunnelIfIndex,
       "usdPppLinkConfigTable": usdPppLinkConfigTable,
       "usdPppLinkConfigEntry": usdPppLinkConfigEntry,
       "usdPppLinkConfigIfIndex": usdPppLinkConfigIfIndex,
       "usdPppLinkConfigRowStatus": usdPppLinkConfigRowStatus,
       "usdPppLinkConfigLowerIfIndex": usdPppLinkConfigLowerIfIndex,
       "usdPppLinkConfigKeepalive": usdPppLinkConfigKeepalive,
       "usdPppLinkConfigAuthentication": usdPppLinkConfigAuthentication,
       "usdPppLinkConfigMaxAuthenRetries": usdPppLinkConfigMaxAuthenRetries,
       "usdPppLinkConfigStandardIfIndex": usdPppLinkConfigStandardIfIndex,
       "usdPppLinkConfigChapMinChallengeLength": usdPppLinkConfigChapMinChallengeLength,
       "usdPppLinkConfigChapMaxChallengeLength": usdPppLinkConfigChapMaxChallengeLength,
       "usdPppLinkConfigPassiveMode": usdPppLinkConfigPassiveMode,
       "usdPppLinkConfigAuthenticatorVirtualRouter": usdPppLinkConfigAuthenticatorVirtualRouter,
       "usdPppNextIfIndex": usdPppNextIfIndex,
       "usdPppSec": usdPppSec,
       "usdPppIp": usdPppIp,
       "usdPppIpTable": usdPppIpTable,
       "usdPppIpEntry": usdPppIpEntry,
       "usdPppIpServiceStatus": usdPppIpServiceStatus,
       "usdPppIpTerminateReason": usdPppIpTerminateReason,
       "usdPppIpTerminateNegFailOption": usdPppIpTerminateNegFailOption,
       "usdPppIpLocalIpAddress": usdPppIpLocalIpAddress,
       "usdPppIpRemoteIpAddress": usdPppIpRemoteIpAddress,
       "usdPppIpRemotePrimaryDnsAddress": usdPppIpRemotePrimaryDnsAddress,
       "usdPppIpRemoteSecondaryDnsAddress": usdPppIpRemoteSecondaryDnsAddress,
       "usdPppIpRemotePrimaryWinsAddress": usdPppIpRemotePrimaryWinsAddress,
       "usdPppIpRemoteSecondaryWinsAddress": usdPppIpRemoteSecondaryWinsAddress,
       "usdPppIpConfigTable": usdPppIpConfigTable,
       "usdPppIpConfigEntry": usdPppIpConfigEntry,
       "usdPppIpConfigPeerDnsPriority": usdPppIpConfigPeerDnsPriority,
       "usdPppIpConfigPeerWinsPriority": usdPppIpConfigPeerWinsPriority,
       "usdPppIpConfigIpcpNetmask": usdPppIpConfigIpcpNetmask,
       "usdPppOsi": usdPppOsi,
       "usdPppOsiTable": usdPppOsiTable,
       "usdPppOsiEntry": usdPppOsiEntry,
       "usdPppOsiServiceStatus": usdPppOsiServiceStatus,
       "usdPppOsiOperStatus": usdPppOsiOperStatus,
       "usdPppOsiTerminateReason": usdPppOsiTerminateReason,
       "usdPppOsiTerminateNegFailOption": usdPppOsiTerminateNegFailOption,
       "usdPppOsiLocalAlignNpdu": usdPppOsiLocalAlignNpdu,
       "usdPppOsiRemoteAlignNpdu": usdPppOsiRemoteAlignNpdu,
       "usdPppOsiConfigTable": usdPppOsiConfigTable,
       "usdPppOsiConfigEntry": usdPppOsiConfigEntry,
       "usdPppOsiConfigAdminStatus": usdPppOsiConfigAdminStatus,
       "usdPppSession": usdPppSession,
       "usdPppSessionTable": usdPppSessionTable,
       "usdPppSessionEntry": usdPppSessionEntry,
       "usdPppSessionGrant": usdPppSessionGrant,
       "usdPppSessionTerminateReason": usdPppSessionTerminateReason,
       "usdPppSessionStartTime": usdPppSessionStartTime,
       "usdPppSessionInOctets": usdPppSessionInOctets,
       "usdPppSessionOutOctets": usdPppSessionOutOctets,
       "usdPppSessionInPackets": usdPppSessionInPackets,
       "usdPppSessionOutPackets": usdPppSessionOutPackets,
       "usdPppSessionSessionTimeout": usdPppSessionSessionTimeout,
       "usdPppSessionInactivityTimeout": usdPppSessionInactivityTimeout,
       "usdPppSessionAccountingInterval": usdPppSessionAccountingInterval,
       "usdPppSessionRemoteIpAddress": usdPppSessionRemoteIpAddress,
       "usdPppSessionRemotePrimaryDnsAddress": usdPppSessionRemotePrimaryDnsAddress,
       "usdPppSessionRemoteSecondaryDnsAddress": usdPppSessionRemoteSecondaryDnsAddress,
       "usdPppSessionRemotePrimaryWinsAddress": usdPppSessionRemotePrimaryWinsAddress,
       "usdPppSessionRemoteSecondaryWinsAddress": usdPppSessionRemoteSecondaryWinsAddress,
       "usdPppMlPpp": usdPppMlPpp,
       "usdPppMlPppBundleTable": usdPppMlPppBundleTable,
       "usdPppMlPppBundleEntry": usdPppMlPppBundleEntry,
       "usdPppMlPppBundleName": usdPppMlPppBundleName,
       "usdPppMlPppBundleRowStatus": usdPppMlPppBundleRowStatus,
       "usdPppMlPppBundleNetworkIfIndex": usdPppMlPppBundleNetworkIfIndex,
       "usdPppMlPppNextLinkIfIndex": usdPppMlPppNextLinkIfIndex,
       "usdPppMlPppLinkConfigTable": usdPppMlPppLinkConfigTable,
       "usdPppMlPppLinkConfigEntry": usdPppMlPppLinkConfigEntry,
       "usdPppMlPppLinkConfigIfIndex": usdPppMlPppLinkConfigIfIndex,
       "usdPppMlPppLinkConfigLowerIfIndex": usdPppMlPppLinkConfigLowerIfIndex,
       "usdPppMlPppLinkConfigKeepalive": usdPppMlPppLinkConfigKeepalive,
       "usdPppMlPppLinkConfigAuthentication": usdPppMlPppLinkConfigAuthentication,
       "usdPppMlPppLinkConfigMaxAuthenRetries": usdPppMlPppLinkConfigMaxAuthenRetries,
       "usdPppMlPppLinkConfigRowStatus": usdPppMlPppLinkConfigRowStatus,
       "usdPppMlPppNextNetworkIfIndex": usdPppMlPppNextNetworkIfIndex,
       "usdPppMlPppNetworkConfigTable": usdPppMlPppNetworkConfigTable,
       "usdPppMlPppNetworkConfigEntry": usdPppMlPppNetworkConfigEntry,
       "usdPppMlPppNetworkConfigIfIndex": usdPppMlPppNetworkConfigIfIndex,
       "usdPppMlPppNetworkConfigLowerIfIndex": usdPppMlPppNetworkConfigLowerIfIndex,
       "usdPppMlPppNetworkBundleName": usdPppMlPppNetworkBundleName,
       "usdPppMlPppNetworkRowStatus": usdPppMlPppNetworkRowStatus,
       "usdPppMlPppLinkBindTable": usdPppMlPppLinkBindTable,
       "usdPppMlPppLinkBindEntry": usdPppMlPppLinkBindEntry,
       "usdPppMlPppBindNetworkIfIndex": usdPppMlPppBindNetworkIfIndex,
       "usdPppMlPppBindLinkIfIndex": usdPppMlPppBindLinkIfIndex,
       "usdPppMlPppBindRowStatus": usdPppMlPppBindRowStatus,
       "usdPppSummary": usdPppSummary,
       "usdPppSummaryPppInterfaceCount": usdPppSummaryPppInterfaceCount,
       "usdPppSummaryPppIpNCPs": usdPppSummaryPppIpNCPs,
       "usdPppSummaryPppOsiNCPs": usdPppSummaryPppOsiNCPs,
       "usdPppSummaryPppIfAdminUp": usdPppSummaryPppIfAdminUp,
       "usdPppSummaryPppIfAdminDown": usdPppSummaryPppIfAdminDown,
       "usdPppSummaryPppIfOperUp": usdPppSummaryPppIfOperUp,
       "usdPppSummaryPppIfOperDown": usdPppSummaryPppIfOperDown,
       "usdPppSummaryPppIfOperDormant": usdPppSummaryPppIfOperDormant,
       "usdPppSummaryPppIfNotPresent": usdPppSummaryPppIfNotPresent,
       "usdPppSummaryPppIfLowerLayerDown": usdPppSummaryPppIfLowerLayerDown,
       "usdPppSummaryPppIpNcpOpened": usdPppSummaryPppIpNcpOpened,
       "usdPppSummaryPppIpNcpClosed": usdPppSummaryPppIpNcpClosed,
       "usdPppSummaryPppOsiNcpOpened": usdPppSummaryPppOsiNcpOpened,
       "usdPppSummaryPppOsiNcpClosed": usdPppSummaryPppOsiNcpClosed,
       "usdPppSummaryPppIfLastChangeTime": usdPppSummaryPppIfLastChangeTime,
       "usdPppSummaryPppLinkInterfaceCount": usdPppSummaryPppLinkInterfaceCount,
       "usdPppSummaryPppLinkIfAdminUp": usdPppSummaryPppLinkIfAdminUp,
       "usdPppSummaryPppLinkIfAdminDown": usdPppSummaryPppLinkIfAdminDown,
       "usdPppSummaryPppLinkIfOperUp": usdPppSummaryPppLinkIfOperUp,
       "usdPppSummaryPppLinkIfOperDown": usdPppSummaryPppLinkIfOperDown,
       "usdPppSummaryPppLinkIfOperDormant": usdPppSummaryPppLinkIfOperDormant,
       "usdPppSummaryPppLinkIfNotPresent": usdPppSummaryPppLinkIfNotPresent,
       "usdPppSummaryPppLinkIfLowerLayerDown": usdPppSummaryPppLinkIfLowerLayerDown,
       "usdPppSummaryPppLinkIfLastChangeTime": usdPppSummaryPppLinkIfLastChangeTime,
       "usdPppSummaryPppNetworkInterfaceCount": usdPppSummaryPppNetworkInterfaceCount,
       "usdPppSummaryPppNetworkIpNCPs": usdPppSummaryPppNetworkIpNCPs,
       "usdPppSummaryPppNetworkOsiNCPs": usdPppSummaryPppNetworkOsiNCPs,
       "usdPppSummaryPppNetworkIfAdminUp": usdPppSummaryPppNetworkIfAdminUp,
       "usdPppSummaryPppNetworkIfAdminDown": usdPppSummaryPppNetworkIfAdminDown,
       "usdPppSummaryPppNetworkIfOperUp": usdPppSummaryPppNetworkIfOperUp,
       "usdPppSummaryPppNetworkIfOperDown": usdPppSummaryPppNetworkIfOperDown,
       "usdPppSummaryPppNetworkIfOperDormant": usdPppSummaryPppNetworkIfOperDormant,
       "usdPppSummaryPppNetworkIfNotPresent": usdPppSummaryPppNetworkIfNotPresent,
       "usdPppSummaryPppNetworkIfLowerLayerDown": usdPppSummaryPppNetworkIfLowerLayerDown,
       "usdPppSummaryPppNetworkIpNcpOpened": usdPppSummaryPppNetworkIpNcpOpened,
       "usdPppSummaryPppNetworkIpNcpClosed": usdPppSummaryPppNetworkIpNcpClosed,
       "usdPppSummaryPppNetworkOsiNcpOpened": usdPppSummaryPppNetworkOsiNcpOpened,
       "usdPppSummaryPppNetworkOsiNcpClosed": usdPppSummaryPppNetworkOsiNcpClosed,
       "usdPppSummaryPppNetworkIfLastChangeTime": usdPppSummaryPppNetworkIfLastChangeTime,
       "usdPppConformance": usdPppConformance,
       "usdPppCompliances": usdPppCompliances,
       "usdPppCompliance": usdPppCompliance,
       "usdPppCompliance2": usdPppCompliance2,
       "usdPppCompliance3": usdPppCompliance3,
       "usdPppCompliance4": usdPppCompliance4,
       "usdPppCompliance5": usdPppCompliance5,
       "usdPppCompliance6": usdPppCompliance6,
       "usdPppGroups": usdPppGroups,
       "usdPppLcpGroup": usdPppLcpGroup,
       "usdPppIpGroup": usdPppIpGroup,
       "usdPppOsiGroup": usdPppOsiGroup,
       "usdPppLcpGroup2": usdPppLcpGroup2,
       "usdPppIpGroup2": usdPppIpGroup2,
       "usdPppOsiGroup2": usdPppOsiGroup2,
       "usdPppSessionGroup": usdPppSessionGroup,
       "usdPppMlPppGroup": usdPppMlPppGroup,
       "usdPppSummaryGroup": usdPppSummaryGroup,
       "usdPppLcpGroup3": usdPppLcpGroup3,
       "usdPppSummaryBasicGroup": usdPppSummaryBasicGroup,
       "usdPppSummaryLinkGroup": usdPppSummaryLinkGroup,
       "usdPppSummaryNetworkGroup": usdPppSummaryNetworkGroup,
       "usdPppLcpGroup4": usdPppLcpGroup4,
       "usdPppIpGroup3": usdPppIpGroup3,
       "usdPppMlPppGroup2": usdPppMlPppGroup2}
)
