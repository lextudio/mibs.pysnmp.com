# SNMP MIB module (JNX-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/JNX-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:12:44 2024
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

(Ipv6AddressIfIdentifier,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6AddressIfIdentifier")

(jnxPppMibRoot,) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxPppMibRoot")

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

jnxPppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1)
)
jnxPppMIB.setRevisions(
        ("2013-09-19 00:00",
         "2013-06-13 00:00",
         "2012-06-08 00:00",
         "2011-11-29 00:00",
         "2010-07-22 09:42")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxPppAuthentication(Integer32, TextualConvention):
    status = "deprecated"
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



class JnxPppMlPppBundleName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 60),
    )



class JnxPppAuthentication2(Integer32, TextualConvention):
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
        *(("chap", 2),
          ("eap", 3),
          ("none", 0),
          ("pap", 1))
    )



class JnxNibbleConfig(Integer32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JnxPPPObjects_ObjectIdentity = ObjectIdentity
jnxPPPObjects = _JnxPPPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1)
)
_JnxPppLcp_ObjectIdentity = ObjectIdentity
jnxPppLcp = _JnxPppLcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1)
)
_JnxPppLinkStatusTable_Object = MibTable
jnxPppLinkStatusTable = _JnxPppLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    jnxPppLinkStatusTable.setStatus("current")
_JnxPppLinkStatusEntry_Object = MibTableRow
jnxPppLinkStatusEntry = _JnxPppLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1)
)
jnxPppLinkStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPppLinkStatusEntry.setStatus("current")


class _JnxPppLinkStatusTerminateReason_Type(Integer32):
    """Custom type jnxPppLinkStatusTerminateReason based on Integer32"""
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


_JnxPppLinkStatusTerminateReason_Type.__name__ = "Integer32"
_JnxPppLinkStatusTerminateReason_Object = MibTableColumn
jnxPppLinkStatusTerminateReason = _JnxPppLinkStatusTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 1),
    _JnxPppLinkStatusTerminateReason_Type()
)
jnxPppLinkStatusTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusTerminateReason.setStatus("current")


class _JnxPppLinkStatusTerminateNegFailOption_Type(Integer32):
    """Custom type jnxPppLinkStatusTerminateNegFailOption based on Integer32"""
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


_JnxPppLinkStatusTerminateNegFailOption_Type.__name__ = "Integer32"
_JnxPppLinkStatusTerminateNegFailOption_Object = MibTableColumn
jnxPppLinkStatusTerminateNegFailOption = _JnxPppLinkStatusTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 2),
    _JnxPppLinkStatusTerminateNegFailOption_Type()
)
jnxPppLinkStatusTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusTerminateNegFailOption.setStatus("current")
_JnxPppLinkStatusInKeepaliveRequests_Type = Counter32
_JnxPppLinkStatusInKeepaliveRequests_Object = MibTableColumn
jnxPppLinkStatusInKeepaliveRequests = _JnxPppLinkStatusInKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 3),
    _JnxPppLinkStatusInKeepaliveRequests_Type()
)
jnxPppLinkStatusInKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusInKeepaliveRequests.setStatus("current")
_JnxPppLinkStatusOutKeepaliveRequests_Type = Counter32
_JnxPppLinkStatusOutKeepaliveRequests_Object = MibTableColumn
jnxPppLinkStatusOutKeepaliveRequests = _JnxPppLinkStatusOutKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 4),
    _JnxPppLinkStatusOutKeepaliveRequests_Type()
)
jnxPppLinkStatusOutKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusOutKeepaliveRequests.setStatus("current")
_JnxPppLinkStatusInKeepaliveReplies_Type = Counter32
_JnxPppLinkStatusInKeepaliveReplies_Object = MibTableColumn
jnxPppLinkStatusInKeepaliveReplies = _JnxPppLinkStatusInKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 5),
    _JnxPppLinkStatusInKeepaliveReplies_Type()
)
jnxPppLinkStatusInKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusInKeepaliveReplies.setStatus("current")
_JnxPppLinkStatusOutKeepaliveReplies_Type = Counter32
_JnxPppLinkStatusOutKeepaliveReplies_Object = MibTableColumn
jnxPppLinkStatusOutKeepaliveReplies = _JnxPppLinkStatusOutKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 6),
    _JnxPppLinkStatusOutKeepaliveReplies_Type()
)
jnxPppLinkStatusOutKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusOutKeepaliveReplies.setStatus("current")
_JnxPppLinkStatusKeepaliveFailures_Type = Counter32
_JnxPppLinkStatusKeepaliveFailures_Object = MibTableColumn
jnxPppLinkStatusKeepaliveFailures = _JnxPppLinkStatusKeepaliveFailures_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 7),
    _JnxPppLinkStatusKeepaliveFailures_Type()
)
jnxPppLinkStatusKeepaliveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusKeepaliveFailures.setStatus("current")
_JnxPppLinkStatusLocalMagicNumber_Type = Integer32
_JnxPppLinkStatusLocalMagicNumber_Object = MibTableColumn
jnxPppLinkStatusLocalMagicNumber = _JnxPppLinkStatusLocalMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 8),
    _JnxPppLinkStatusLocalMagicNumber_Type()
)
jnxPppLinkStatusLocalMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusLocalMagicNumber.setStatus("deprecated")
_JnxPppLinkStatusRemoteMagicNumber_Type = Integer32
_JnxPppLinkStatusRemoteMagicNumber_Object = MibTableColumn
jnxPppLinkStatusRemoteMagicNumber = _JnxPppLinkStatusRemoteMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 9),
    _JnxPppLinkStatusRemoteMagicNumber_Type()
)
jnxPppLinkStatusRemoteMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusRemoteMagicNumber.setStatus("deprecated")
_JnxPppLinkStatusLocalAuthentication_Type = JnxPppAuthentication2
_JnxPppLinkStatusLocalAuthentication_Object = MibTableColumn
jnxPppLinkStatusLocalAuthentication = _JnxPppLinkStatusLocalAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 10),
    _JnxPppLinkStatusLocalAuthentication_Type()
)
jnxPppLinkStatusLocalAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusLocalAuthentication.setStatus("current")
_JnxPppLinkStatusTunnelIfIndex_Type = InterfaceIndexOrZero
_JnxPppLinkStatusTunnelIfIndex_Object = MibTableColumn
jnxPppLinkStatusTunnelIfIndex = _JnxPppLinkStatusTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 11),
    _JnxPppLinkStatusTunnelIfIndex_Type()
)
jnxPppLinkStatusTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusTunnelIfIndex.setStatus("current")
_JnxPppLinkStatuslcpRenegoTerminates_Type = Counter32
_JnxPppLinkStatuslcpRenegoTerminates_Object = MibTableColumn
jnxPppLinkStatuslcpRenegoTerminates = _JnxPppLinkStatuslcpRenegoTerminates_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 12),
    _JnxPppLinkStatuslcpRenegoTerminates_Type()
)
jnxPppLinkStatuslcpRenegoTerminates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatuslcpRenegoTerminates.setStatus("current")
_JnxPppLinkStatusLocalMagicNumber1_Type = Unsigned32
_JnxPppLinkStatusLocalMagicNumber1_Object = MibTableColumn
jnxPppLinkStatusLocalMagicNumber1 = _JnxPppLinkStatusLocalMagicNumber1_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 13),
    _JnxPppLinkStatusLocalMagicNumber1_Type()
)
jnxPppLinkStatusLocalMagicNumber1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusLocalMagicNumber1.setStatus("current")
_JnxPppLinkStatusRemoteMagicNumber1_Type = Unsigned32
_JnxPppLinkStatusRemoteMagicNumber1_Object = MibTableColumn
jnxPppLinkStatusRemoteMagicNumber1 = _JnxPppLinkStatusRemoteMagicNumber1_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 1, 1, 14),
    _JnxPppLinkStatusRemoteMagicNumber1_Type()
)
jnxPppLinkStatusRemoteMagicNumber1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkStatusRemoteMagicNumber1.setStatus("current")
_JnxPppLinkConfigTable_Object = MibTable
jnxPppLinkConfigTable = _JnxPppLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    jnxPppLinkConfigTable.setStatus("current")
_JnxPppLinkConfigEntry_Object = MibTableRow
jnxPppLinkConfigEntry = _JnxPppLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1)
)
jnxPppLinkConfigEntry.setIndexNames(
    (0, "JNX-PPP-MIB", "jnxPppLinkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    jnxPppLinkConfigEntry.setStatus("current")
_JnxPppLinkConfigIfIndex_Type = InterfaceIndex
_JnxPppLinkConfigIfIndex_Object = MibTableColumn
jnxPppLinkConfigIfIndex = _JnxPppLinkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 1),
    _JnxPppLinkConfigIfIndex_Type()
)
jnxPppLinkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPppLinkConfigIfIndex.setStatus("current")
_JnxPppLinkConfigRowStatus_Type = RowStatus
_JnxPppLinkConfigRowStatus_Object = MibTableColumn
jnxPppLinkConfigRowStatus = _JnxPppLinkConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 2),
    _JnxPppLinkConfigRowStatus_Type()
)
jnxPppLinkConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigRowStatus.setStatus("current")
_JnxPppLinkConfigLowerIfIndex_Type = InterfaceIndexOrZero
_JnxPppLinkConfigLowerIfIndex_Object = MibTableColumn
jnxPppLinkConfigLowerIfIndex = _JnxPppLinkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 3),
    _JnxPppLinkConfigLowerIfIndex_Type()
)
jnxPppLinkConfigLowerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigLowerIfIndex.setStatus("current")


class _JnxPppLinkConfigKeepalive_Type(Integer32):
    """Custom type jnxPppLinkConfigKeepalive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64800),
    )


_JnxPppLinkConfigKeepalive_Type.__name__ = "Integer32"
_JnxPppLinkConfigKeepalive_Object = MibTableColumn
jnxPppLinkConfigKeepalive = _JnxPppLinkConfigKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 4),
    _JnxPppLinkConfigKeepalive_Type()
)
jnxPppLinkConfigKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    jnxPppLinkConfigKeepalive.setUnits("seconds")


class _JnxPppLinkConfigAuthentication_Type(JnxPppAuthentication):
    """Custom type jnxPppLinkConfigAuthentication based on JnxPppAuthentication"""


_JnxPppLinkConfigAuthentication_Object = MibTableColumn
jnxPppLinkConfigAuthentication = _JnxPppLinkConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 5),
    _JnxPppLinkConfigAuthentication_Type()
)
jnxPppLinkConfigAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigAuthentication.setStatus("deprecated")


class _JnxPppLinkConfigMaxAuthenRetries_Type(Integer32):
    """Custom type jnxPppLinkConfigMaxAuthenRetries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_JnxPppLinkConfigMaxAuthenRetries_Type.__name__ = "Integer32"
_JnxPppLinkConfigMaxAuthenRetries_Object = MibTableColumn
jnxPppLinkConfigMaxAuthenRetries = _JnxPppLinkConfigMaxAuthenRetries_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 6),
    _JnxPppLinkConfigMaxAuthenRetries_Type()
)
jnxPppLinkConfigMaxAuthenRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigMaxAuthenRetries.setStatus("current")
_JnxPppLinkConfigStandardIfIndex_Type = InterfaceIndex
_JnxPppLinkConfigStandardIfIndex_Object = MibTableColumn
jnxPppLinkConfigStandardIfIndex = _JnxPppLinkConfigStandardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 7),
    _JnxPppLinkConfigStandardIfIndex_Type()
)
jnxPppLinkConfigStandardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigStandardIfIndex.setStatus("current")


class _JnxPppLinkConfigChapMinChallengeLength_Type(Integer32):
    """Custom type jnxPppLinkConfigChapMinChallengeLength based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_JnxPppLinkConfigChapMinChallengeLength_Type.__name__ = "Integer32"
_JnxPppLinkConfigChapMinChallengeLength_Object = MibTableColumn
jnxPppLinkConfigChapMinChallengeLength = _JnxPppLinkConfigChapMinChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 8),
    _JnxPppLinkConfigChapMinChallengeLength_Type()
)
jnxPppLinkConfigChapMinChallengeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigChapMinChallengeLength.setStatus("current")


class _JnxPppLinkConfigChapMaxChallengeLength_Type(Integer32):
    """Custom type jnxPppLinkConfigChapMaxChallengeLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_JnxPppLinkConfigChapMaxChallengeLength_Type.__name__ = "Integer32"
_JnxPppLinkConfigChapMaxChallengeLength_Object = MibTableColumn
jnxPppLinkConfigChapMaxChallengeLength = _JnxPppLinkConfigChapMaxChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 9),
    _JnxPppLinkConfigChapMaxChallengeLength_Type()
)
jnxPppLinkConfigChapMaxChallengeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigChapMaxChallengeLength.setStatus("current")


class _JnxPppLinkConfigPassiveMode_Type(Integer32):
    """Custom type jnxPppLinkConfigPassiveMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppLinkConfigPassiveMode_Type.__name__ = "Integer32"
_JnxPppLinkConfigPassiveMode_Object = MibTableColumn
jnxPppLinkConfigPassiveMode = _JnxPppLinkConfigPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 10),
    _JnxPppLinkConfigPassiveMode_Type()
)
jnxPppLinkConfigPassiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigPassiveMode.setStatus("current")
_JnxPppLinkConfigAuthenticatorLogicalSystem_Type = OctetString
_JnxPppLinkConfigAuthenticatorLogicalSystem_Object = MibTableColumn
jnxPppLinkConfigAuthenticatorLogicalSystem = _JnxPppLinkConfigAuthenticatorLogicalSystem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 11),
    _JnxPppLinkConfigAuthenticatorLogicalSystem_Type()
)
jnxPppLinkConfigAuthenticatorLogicalSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigAuthenticatorLogicalSystem.setStatus("current")
_JnxPppLinkConfigAuthenticatorRoutingInstance_Type = OctetString
_JnxPppLinkConfigAuthenticatorRoutingInstance_Object = MibTableColumn
jnxPppLinkConfigAuthenticatorRoutingInstance = _JnxPppLinkConfigAuthenticatorRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 12),
    _JnxPppLinkConfigAuthenticatorRoutingInstance_Type()
)
jnxPppLinkConfigAuthenticatorRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigAuthenticatorRoutingInstance.setStatus("current")
_JnxPppLinkConfigAaaProfile_Type = OctetString
_JnxPppLinkConfigAaaProfile_Object = MibTableColumn
jnxPppLinkConfigAaaProfile = _JnxPppLinkConfigAaaProfile_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 13),
    _JnxPppLinkConfigAaaProfile_Type()
)
jnxPppLinkConfigAaaProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigAaaProfile.setStatus("current")


class _JnxPppLinkConfigAuthentication2_Type(JnxNibbleConfig):
    """Custom type jnxPppLinkConfigAuthentication2 based on JnxNibbleConfig"""
    defaultValue = 0


_JnxPppLinkConfigAuthentication2_Object = MibTableColumn
jnxPppLinkConfigAuthentication2 = _JnxPppLinkConfigAuthentication2_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 14),
    _JnxPppLinkConfigAuthentication2_Type()
)
jnxPppLinkConfigAuthentication2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigAuthentication2.setStatus("current")


class _JnxPppLinkConfigIgnoreMagicNumberMismatch_Type(Integer32):
    """Custom type jnxPppLinkConfigIgnoreMagicNumberMismatch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppLinkConfigIgnoreMagicNumberMismatch_Type.__name__ = "Integer32"
_JnxPppLinkConfigIgnoreMagicNumberMismatch_Object = MibTableColumn
jnxPppLinkConfigIgnoreMagicNumberMismatch = _JnxPppLinkConfigIgnoreMagicNumberMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 15),
    _JnxPppLinkConfigIgnoreMagicNumberMismatch_Type()
)
jnxPppLinkConfigIgnoreMagicNumberMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigIgnoreMagicNumberMismatch.setStatus("current")


class _JnxPppLinkConfigMaxLcpRenegotiation_Type(Integer32):
    """Custom type jnxPppLinkConfigMaxLcpRenegotiation based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxPppLinkConfigMaxLcpRenegotiation_Type.__name__ = "Integer32"
_JnxPppLinkConfigMaxLcpRenegotiation_Object = MibTableColumn
jnxPppLinkConfigMaxLcpRenegotiation = _JnxPppLinkConfigMaxLcpRenegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 2, 1, 16),
    _JnxPppLinkConfigMaxLcpRenegotiation_Type()
)
jnxPppLinkConfigMaxLcpRenegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppLinkConfigMaxLcpRenegotiation.setStatus("current")
_JnxPppNextIfIndex_Type = InterfaceIndexOrZero
_JnxPppNextIfIndex_Object = MibScalar
jnxPppNextIfIndex = _JnxPppNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 1, 3),
    _JnxPppNextIfIndex_Type()
)
jnxPppNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppNextIfIndex.setStatus("current")
_JnxPppSec_ObjectIdentity = ObjectIdentity
jnxPppSec = _JnxPppSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 2)
)
_JnxPppIp_ObjectIdentity = ObjectIdentity
jnxPppIp = _JnxPppIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3)
)
_JnxPppIpTable_Object = MibTable
jnxPppIpTable = _JnxPppIpTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    jnxPppIpTable.setStatus("current")
_JnxPppIpEntry_Object = MibTableRow
jnxPppIpEntry = _JnxPppIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1)
)
jnxPppIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPppIpEntry.setStatus("current")


class _JnxPppIpServiceStatus_Type(Integer32):
    """Custom type jnxPppIpServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppIpServiceStatus_Type.__name__ = "Integer32"
_JnxPppIpServiceStatus_Object = MibTableColumn
jnxPppIpServiceStatus = _JnxPppIpServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1, 1),
    _JnxPppIpServiceStatus_Type()
)
jnxPppIpServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpServiceStatus.setStatus("current")


class _JnxPppIpTerminateReason_Type(Integer32):
    """Custom type jnxPppIpTerminateReason based on Integer32"""
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


_JnxPppIpTerminateReason_Type.__name__ = "Integer32"
_JnxPppIpTerminateReason_Object = MibTableColumn
jnxPppIpTerminateReason = _JnxPppIpTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1, 2),
    _JnxPppIpTerminateReason_Type()
)
jnxPppIpTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpTerminateReason.setStatus("current")


class _JnxPppIpTerminateNegFailOption_Type(Integer32):
    """Custom type jnxPppIpTerminateNegFailOption based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("localIpAddress", 2),
          ("localIpAddressMask", 8),
          ("none", 0),
          ("other", 1),
          ("remoteIpAddress", 3),
          ("remoteIpAddressMask", 9),
          ("remotePrimaryDnsAddress", 4),
          ("remotePrimaryWinsAddress", 6),
          ("remoteSecondaryDnsAddress", 5),
          ("remoteSecondaryWinsAddress", 7))
    )


_JnxPppIpTerminateNegFailOption_Type.__name__ = "Integer32"
_JnxPppIpTerminateNegFailOption_Object = MibTableColumn
jnxPppIpTerminateNegFailOption = _JnxPppIpTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1, 3),
    _JnxPppIpTerminateNegFailOption_Type()
)
jnxPppIpTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpTerminateNegFailOption.setStatus("current")
_JnxPppIpLocalIpAddress_Type = IpAddress
_JnxPppIpLocalIpAddress_Object = MibTableColumn
jnxPppIpLocalIpAddress = _JnxPppIpLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1, 4),
    _JnxPppIpLocalIpAddress_Type()
)
jnxPppIpLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpLocalIpAddress.setStatus("current")
_JnxPppIpRemoteIpAddress_Type = IpAddress
_JnxPppIpRemoteIpAddress_Object = MibTableColumn
jnxPppIpRemoteIpAddress = _JnxPppIpRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1, 5),
    _JnxPppIpRemoteIpAddress_Type()
)
jnxPppIpRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpRemoteIpAddress.setStatus("current")
_JnxPppIpRemotePrimaryDnsAddress_Type = IpAddress
_JnxPppIpRemotePrimaryDnsAddress_Object = MibTableColumn
jnxPppIpRemotePrimaryDnsAddress = _JnxPppIpRemotePrimaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1, 6),
    _JnxPppIpRemotePrimaryDnsAddress_Type()
)
jnxPppIpRemotePrimaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpRemotePrimaryDnsAddress.setStatus("current")
_JnxPppIpRemoteSecondaryDnsAddress_Type = IpAddress
_JnxPppIpRemoteSecondaryDnsAddress_Object = MibTableColumn
jnxPppIpRemoteSecondaryDnsAddress = _JnxPppIpRemoteSecondaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1, 7),
    _JnxPppIpRemoteSecondaryDnsAddress_Type()
)
jnxPppIpRemoteSecondaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpRemoteSecondaryDnsAddress.setStatus("current")
_JnxPppIpRemotePrimaryWinsAddress_Type = IpAddress
_JnxPppIpRemotePrimaryWinsAddress_Object = MibTableColumn
jnxPppIpRemotePrimaryWinsAddress = _JnxPppIpRemotePrimaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1, 8),
    _JnxPppIpRemotePrimaryWinsAddress_Type()
)
jnxPppIpRemotePrimaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpRemotePrimaryWinsAddress.setStatus("current")
_JnxPppIpRemoteSecondaryWinsAddress_Type = IpAddress
_JnxPppIpRemoteSecondaryWinsAddress_Object = MibTableColumn
jnxPppIpRemoteSecondaryWinsAddress = _JnxPppIpRemoteSecondaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1, 9),
    _JnxPppIpRemoteSecondaryWinsAddress_Type()
)
jnxPppIpRemoteSecondaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpRemoteSecondaryWinsAddress.setStatus("current")
_JnxPppIpNetworkStatusIpcpRenegoTerminates_Type = Counter32
_JnxPppIpNetworkStatusIpcpRenegoTerminates_Object = MibTableColumn
jnxPppIpNetworkStatusIpcpRenegoTerminates = _JnxPppIpNetworkStatusIpcpRenegoTerminates_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 1, 1, 10),
    _JnxPppIpNetworkStatusIpcpRenegoTerminates_Type()
)
jnxPppIpNetworkStatusIpcpRenegoTerminates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpNetworkStatusIpcpRenegoTerminates.setStatus("current")
_JnxPppIpConfigTable_Object = MibTable
jnxPppIpConfigTable = _JnxPppIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    jnxPppIpConfigTable.setStatus("current")
_JnxPppIpConfigEntry_Object = MibTableRow
jnxPppIpConfigEntry = _JnxPppIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 2, 1)
)
jnxPppIpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPppIpConfigEntry.setStatus("current")


class _JnxPppIpConfigPeerDnsPriority_Type(Integer32):
    """Custom type jnxPppIpConfigPeerDnsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppIpConfigPeerDnsPriority_Type.__name__ = "Integer32"
_JnxPppIpConfigPeerDnsPriority_Object = MibTableColumn
jnxPppIpConfigPeerDnsPriority = _JnxPppIpConfigPeerDnsPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 2, 1, 1),
    _JnxPppIpConfigPeerDnsPriority_Type()
)
jnxPppIpConfigPeerDnsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpConfigPeerDnsPriority.setStatus("current")


class _JnxPppIpConfigPeerWinsPriority_Type(Integer32):
    """Custom type jnxPppIpConfigPeerWinsPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppIpConfigPeerWinsPriority_Type.__name__ = "Integer32"
_JnxPppIpConfigPeerWinsPriority_Object = MibTableColumn
jnxPppIpConfigPeerWinsPriority = _JnxPppIpConfigPeerWinsPriority_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 2, 1, 2),
    _JnxPppIpConfigPeerWinsPriority_Type()
)
jnxPppIpConfigPeerWinsPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpConfigPeerWinsPriority.setStatus("current")


class _JnxPppIpConfigIpcpNetmask_Type(Integer32):
    """Custom type jnxPppIpConfigIpcpNetmask based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppIpConfigIpcpNetmask_Type.__name__ = "Integer32"
_JnxPppIpConfigIpcpNetmask_Object = MibTableColumn
jnxPppIpConfigIpcpNetmask = _JnxPppIpConfigIpcpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 2, 1, 3),
    _JnxPppIpConfigIpcpNetmask_Type()
)
jnxPppIpConfigIpcpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpConfigIpcpNetmask.setStatus("current")


class _JnxPppIpConfigInitiateIp_Type(Integer32):
    """Custom type jnxPppIpConfigInitiateIp based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppIpConfigInitiateIp_Type.__name__ = "Integer32"
_JnxPppIpConfigInitiateIp_Object = MibTableColumn
jnxPppIpConfigInitiateIp = _JnxPppIpConfigInitiateIp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 2, 1, 4),
    _JnxPppIpConfigInitiateIp_Type()
)
jnxPppIpConfigInitiateIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpConfigInitiateIp.setStatus("current")


class _JnxPppIpConfigMaxIpcpRenegotiation_Type(Integer32):
    """Custom type jnxPppIpConfigMaxIpcpRenegotiation based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxPppIpConfigMaxIpcpRenegotiation_Type.__name__ = "Integer32"
_JnxPppIpConfigMaxIpcpRenegotiation_Object = MibTableColumn
jnxPppIpConfigMaxIpcpRenegotiation = _JnxPppIpConfigMaxIpcpRenegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 2, 1, 5),
    _JnxPppIpConfigMaxIpcpRenegotiation_Type()
)
jnxPppIpConfigMaxIpcpRenegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpConfigMaxIpcpRenegotiation.setStatus("current")


class _JnxPppIpConfigPromptIpcpDnsOption_Type(Integer32):
    """Custom type jnxPppIpConfigPromptIpcpDnsOption based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppIpConfigPromptIpcpDnsOption_Type.__name__ = "Integer32"
_JnxPppIpConfigPromptIpcpDnsOption_Object = MibTableColumn
jnxPppIpConfigPromptIpcpDnsOption = _JnxPppIpConfigPromptIpcpDnsOption_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 2, 1, 6),
    _JnxPppIpConfigPromptIpcpDnsOption_Type()
)
jnxPppIpConfigPromptIpcpDnsOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpConfigPromptIpcpDnsOption.setStatus("current")


class _JnxPppIpConfigIpcpLockout_Type(Integer32):
    """Custom type jnxPppIpConfigIpcpLockout based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppIpConfigIpcpLockout_Type.__name__ = "Integer32"
_JnxPppIpConfigIpcpLockout_Object = MibTableColumn
jnxPppIpConfigIpcpLockout = _JnxPppIpConfigIpcpLockout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 3, 2, 1, 7),
    _JnxPppIpConfigIpcpLockout_Type()
)
jnxPppIpConfigIpcpLockout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpConfigIpcpLockout.setStatus("current")
_JnxPppOsi_ObjectIdentity = ObjectIdentity
jnxPppOsi = _JnxPppOsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4)
)
_JnxPppOsiTable_Object = MibTable
jnxPppOsiTable = _JnxPppOsiTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    jnxPppOsiTable.setStatus("current")
_JnxPppOsiEntry_Object = MibTableRow
jnxPppOsiEntry = _JnxPppOsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 1, 1)
)
jnxPppOsiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPppOsiEntry.setStatus("current")


class _JnxPppOsiServiceStatus_Type(Integer32):
    """Custom type jnxPppOsiServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppOsiServiceStatus_Type.__name__ = "Integer32"
_JnxPppOsiServiceStatus_Object = MibTableColumn
jnxPppOsiServiceStatus = _JnxPppOsiServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 1, 1, 1),
    _JnxPppOsiServiceStatus_Type()
)
jnxPppOsiServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppOsiServiceStatus.setStatus("current")


class _JnxPppOsiOperStatus_Type(Integer32):
    """Custom type jnxPppOsiOperStatus based on Integer32"""
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


_JnxPppOsiOperStatus_Type.__name__ = "Integer32"
_JnxPppOsiOperStatus_Object = MibTableColumn
jnxPppOsiOperStatus = _JnxPppOsiOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 1, 1, 2),
    _JnxPppOsiOperStatus_Type()
)
jnxPppOsiOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppOsiOperStatus.setStatus("current")


class _JnxPppOsiTerminateReason_Type(Integer32):
    """Custom type jnxPppOsiTerminateReason based on Integer32"""
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


_JnxPppOsiTerminateReason_Type.__name__ = "Integer32"
_JnxPppOsiTerminateReason_Object = MibTableColumn
jnxPppOsiTerminateReason = _JnxPppOsiTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 1, 1, 3),
    _JnxPppOsiTerminateReason_Type()
)
jnxPppOsiTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppOsiTerminateReason.setStatus("current")


class _JnxPppOsiTerminateNegFailOption_Type(Integer32):
    """Custom type jnxPppOsiTerminateNegFailOption based on Integer32"""
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


_JnxPppOsiTerminateNegFailOption_Type.__name__ = "Integer32"
_JnxPppOsiTerminateNegFailOption_Object = MibTableColumn
jnxPppOsiTerminateNegFailOption = _JnxPppOsiTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 1, 1, 4),
    _JnxPppOsiTerminateNegFailOption_Type()
)
jnxPppOsiTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppOsiTerminateNegFailOption.setStatus("current")


class _JnxPppOsiLocalAlignNpdu_Type(Integer32):
    """Custom type jnxPppOsiLocalAlignNpdu based on Integer32"""
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


_JnxPppOsiLocalAlignNpdu_Type.__name__ = "Integer32"
_JnxPppOsiLocalAlignNpdu_Object = MibTableColumn
jnxPppOsiLocalAlignNpdu = _JnxPppOsiLocalAlignNpdu_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 1, 1, 5),
    _JnxPppOsiLocalAlignNpdu_Type()
)
jnxPppOsiLocalAlignNpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppOsiLocalAlignNpdu.setStatus("current")


class _JnxPppOsiRemoteAlignNpdu_Type(Integer32):
    """Custom type jnxPppOsiRemoteAlignNpdu based on Integer32"""
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


_JnxPppOsiRemoteAlignNpdu_Type.__name__ = "Integer32"
_JnxPppOsiRemoteAlignNpdu_Object = MibTableColumn
jnxPppOsiRemoteAlignNpdu = _JnxPppOsiRemoteAlignNpdu_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 1, 1, 6),
    _JnxPppOsiRemoteAlignNpdu_Type()
)
jnxPppOsiRemoteAlignNpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppOsiRemoteAlignNpdu.setStatus("current")
_JnxPppOsiConfigTable_Object = MibTable
jnxPppOsiConfigTable = _JnxPppOsiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 2)
)
if mibBuilder.loadTexts:
    jnxPppOsiConfigTable.setStatus("current")
_JnxPppOsiConfigEntry_Object = MibTableRow
jnxPppOsiConfigEntry = _JnxPppOsiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 2, 1)
)
jnxPppOsiConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPppOsiConfigEntry.setStatus("current")


class _JnxPppOsiConfigAdminStatus_Type(Integer32):
    """Custom type jnxPppOsiConfigAdminStatus based on Integer32"""
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


_JnxPppOsiConfigAdminStatus_Type.__name__ = "Integer32"
_JnxPppOsiConfigAdminStatus_Object = MibTableColumn
jnxPppOsiConfigAdminStatus = _JnxPppOsiConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 4, 2, 1, 1),
    _JnxPppOsiConfigAdminStatus_Type()
)
jnxPppOsiConfigAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppOsiConfigAdminStatus.setStatus("current")
_JnxPppSession_ObjectIdentity = ObjectIdentity
jnxPppSession = _JnxPppSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5)
)
_JnxPppSessionTable_Object = MibTable
jnxPppSessionTable = _JnxPppSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    jnxPppSessionTable.setStatus("current")
_JnxPppSessionEntry_Object = MibTableRow
jnxPppSessionEntry = _JnxPppSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1)
)
jnxPppSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPppSessionEntry.setStatus("current")
_JnxPppSessionGrant_Type = TruthValue
_JnxPppSessionGrant_Object = MibTableColumn
jnxPppSessionGrant = _JnxPppSessionGrant_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 1),
    _JnxPppSessionGrant_Type()
)
jnxPppSessionGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionGrant.setStatus("current")


class _JnxPppSessionTerminateReason_Type(Integer32):
    """Custom type jnxPppSessionTerminateReason based on Integer32"""
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


_JnxPppSessionTerminateReason_Type.__name__ = "Integer32"
_JnxPppSessionTerminateReason_Object = MibTableColumn
jnxPppSessionTerminateReason = _JnxPppSessionTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 2),
    _JnxPppSessionTerminateReason_Type()
)
jnxPppSessionTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionTerminateReason.setStatus("current")
_JnxPppSessionStartTime_Type = TimeTicks
_JnxPppSessionStartTime_Object = MibTableColumn
jnxPppSessionStartTime = _JnxPppSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 3),
    _JnxPppSessionStartTime_Type()
)
jnxPppSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionStartTime.setStatus("current")
_JnxPppSessionInOctets_Type = Counter32
_JnxPppSessionInOctets_Object = MibTableColumn
jnxPppSessionInOctets = _JnxPppSessionInOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 4),
    _JnxPppSessionInOctets_Type()
)
jnxPppSessionInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionInOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxPppSessionInOctets.setUnits("octets")
_JnxPppSessionOutOctets_Type = Counter32
_JnxPppSessionOutOctets_Object = MibTableColumn
jnxPppSessionOutOctets = _JnxPppSessionOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 5),
    _JnxPppSessionOutOctets_Type()
)
jnxPppSessionOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionOutOctets.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxPppSessionOutOctets.setUnits("octets")
_JnxPppSessionInPackets_Type = Counter32
_JnxPppSessionInPackets_Object = MibTableColumn
jnxPppSessionInPackets = _JnxPppSessionInPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 6),
    _JnxPppSessionInPackets_Type()
)
jnxPppSessionInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionInPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxPppSessionInPackets.setUnits("packets")
_JnxPppSessionOutPackets_Type = Counter32
_JnxPppSessionOutPackets_Object = MibTableColumn
jnxPppSessionOutPackets = _JnxPppSessionOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 7),
    _JnxPppSessionOutPackets_Type()
)
jnxPppSessionOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionOutPackets.setStatus("deprecated")
if mibBuilder.loadTexts:
    jnxPppSessionOutPackets.setUnits("packets")


class _JnxPppSessionSessionTimeout_Type(Integer32):
    """Custom type jnxPppSessionSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxPppSessionSessionTimeout_Type.__name__ = "Integer32"
_JnxPppSessionSessionTimeout_Object = MibTableColumn
jnxPppSessionSessionTimeout = _JnxPppSessionSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 8),
    _JnxPppSessionSessionTimeout_Type()
)
jnxPppSessionSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    jnxPppSessionSessionTimeout.setUnits("milliseconds")


class _JnxPppSessionInactivityTimeout_Type(Integer32):
    """Custom type jnxPppSessionInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxPppSessionInactivityTimeout_Type.__name__ = "Integer32"
_JnxPppSessionInactivityTimeout_Object = MibTableColumn
jnxPppSessionInactivityTimeout = _JnxPppSessionInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 9),
    _JnxPppSessionInactivityTimeout_Type()
)
jnxPppSessionInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    jnxPppSessionInactivityTimeout.setUnits("milliseconds")


class _JnxPppSessionAccountingInterval_Type(Integer32):
    """Custom type jnxPppSessionAccountingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JnxPppSessionAccountingInterval_Type.__name__ = "Integer32"
_JnxPppSessionAccountingInterval_Object = MibTableColumn
jnxPppSessionAccountingInterval = _JnxPppSessionAccountingInterval_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 10),
    _JnxPppSessionAccountingInterval_Type()
)
jnxPppSessionAccountingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionAccountingInterval.setStatus("current")
if mibBuilder.loadTexts:
    jnxPppSessionAccountingInterval.setUnits("milliseconds")
_JnxPppSessionRemoteIpAddress_Type = IpAddress
_JnxPppSessionRemoteIpAddress_Object = MibTableColumn
jnxPppSessionRemoteIpAddress = _JnxPppSessionRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 11),
    _JnxPppSessionRemoteIpAddress_Type()
)
jnxPppSessionRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionRemoteIpAddress.setStatus("current")
_JnxPppSessionRemotePrimaryDnsAddress_Type = IpAddress
_JnxPppSessionRemotePrimaryDnsAddress_Object = MibTableColumn
jnxPppSessionRemotePrimaryDnsAddress = _JnxPppSessionRemotePrimaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 12),
    _JnxPppSessionRemotePrimaryDnsAddress_Type()
)
jnxPppSessionRemotePrimaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionRemotePrimaryDnsAddress.setStatus("current")
_JnxPppSessionRemoteSecondaryDnsAddress_Type = IpAddress
_JnxPppSessionRemoteSecondaryDnsAddress_Object = MibTableColumn
jnxPppSessionRemoteSecondaryDnsAddress = _JnxPppSessionRemoteSecondaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 13),
    _JnxPppSessionRemoteSecondaryDnsAddress_Type()
)
jnxPppSessionRemoteSecondaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionRemoteSecondaryDnsAddress.setStatus("current")
_JnxPppSessionRemotePrimaryWinsAddress_Type = IpAddress
_JnxPppSessionRemotePrimaryWinsAddress_Object = MibTableColumn
jnxPppSessionRemotePrimaryWinsAddress = _JnxPppSessionRemotePrimaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 14),
    _JnxPppSessionRemotePrimaryWinsAddress_Type()
)
jnxPppSessionRemotePrimaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionRemotePrimaryWinsAddress.setStatus("current")
_JnxPppSessionRemoteSecondaryWinsAddress_Type = IpAddress
_JnxPppSessionRemoteSecondaryWinsAddress_Object = MibTableColumn
jnxPppSessionRemoteSecondaryWinsAddress = _JnxPppSessionRemoteSecondaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 15),
    _JnxPppSessionRemoteSecondaryWinsAddress_Type()
)
jnxPppSessionRemoteSecondaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionRemoteSecondaryWinsAddress.setStatus("current")
_JnxPppSessionRemoteIpv6AddressIfIdentifier_Type = Ipv6AddressIfIdentifier
_JnxPppSessionRemoteIpv6AddressIfIdentifier_Object = MibTableColumn
jnxPppSessionRemoteIpv6AddressIfIdentifier = _JnxPppSessionRemoteIpv6AddressIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 16),
    _JnxPppSessionRemoteIpv6AddressIfIdentifier_Type()
)
jnxPppSessionRemoteIpv6AddressIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionRemoteIpv6AddressIfIdentifier.setStatus("current")


class _JnxPppSessionInhibitIp_Type(Integer32):
    """Custom type jnxPppSessionInhibitIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppSessionInhibitIp_Type.__name__ = "Integer32"
_JnxPppSessionInhibitIp_Object = MibTableColumn
jnxPppSessionInhibitIp = _JnxPppSessionInhibitIp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 17),
    _JnxPppSessionInhibitIp_Type()
)
jnxPppSessionInhibitIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionInhibitIp.setStatus("current")


class _JnxPppSessionInhibitIpv6_Type(Integer32):
    """Custom type jnxPppSessionInhibitIpv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppSessionInhibitIpv6_Type.__name__ = "Integer32"
_JnxPppSessionInhibitIpv6_Object = MibTableColumn
jnxPppSessionInhibitIpv6 = _JnxPppSessionInhibitIpv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 18),
    _JnxPppSessionInhibitIpv6_Type()
)
jnxPppSessionInhibitIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionInhibitIpv6.setStatus("current")
_JnxPppSessionInOctets64_Type = Counter64
_JnxPppSessionInOctets64_Object = MibTableColumn
jnxPppSessionInOctets64 = _JnxPppSessionInOctets64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 19),
    _JnxPppSessionInOctets64_Type()
)
jnxPppSessionInOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionInOctets64.setStatus("current")
if mibBuilder.loadTexts:
    jnxPppSessionInOctets64.setUnits("octets")
_JnxPppSessionOutOctets64_Type = Counter64
_JnxPppSessionOutOctets64_Object = MibTableColumn
jnxPppSessionOutOctets64 = _JnxPppSessionOutOctets64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 20),
    _JnxPppSessionOutOctets64_Type()
)
jnxPppSessionOutOctets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionOutOctets64.setStatus("current")
if mibBuilder.loadTexts:
    jnxPppSessionOutOctets64.setUnits("octets")
_JnxPppSessionInPackets64_Type = Counter64
_JnxPppSessionInPackets64_Object = MibTableColumn
jnxPppSessionInPackets64 = _JnxPppSessionInPackets64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 21),
    _JnxPppSessionInPackets64_Type()
)
jnxPppSessionInPackets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionInPackets64.setStatus("current")
if mibBuilder.loadTexts:
    jnxPppSessionInPackets64.setUnits("packets")
_JnxPppSessionOutPackets64_Type = Counter64
_JnxPppSessionOutPackets64_Object = MibTableColumn
jnxPppSessionOutPackets64 = _JnxPppSessionOutPackets64_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 5, 1, 1, 22),
    _JnxPppSessionOutPackets64_Type()
)
jnxPppSessionOutPackets64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSessionOutPackets64.setStatus("current")
if mibBuilder.loadTexts:
    jnxPppSessionOutPackets64.setUnits("packets")
_JnxPppMlPpp_ObjectIdentity = ObjectIdentity
jnxPppMlPpp = _JnxPppMlPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6)
)
_JnxPppMlPppBundleTable_Object = MibTable
jnxPppMlPppBundleTable = _JnxPppMlPppBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    jnxPppMlPppBundleTable.setStatus("current")
_JnxPppMlPppBundleEntry_Object = MibTableRow
jnxPppMlPppBundleEntry = _JnxPppMlPppBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 1, 1)
)
jnxPppMlPppBundleEntry.setIndexNames(
    (0, "JNX-PPP-MIB", "jnxPppMlPppBundleName"),
)
if mibBuilder.loadTexts:
    jnxPppMlPppBundleEntry.setStatus("current")
_JnxPppMlPppBundleName_Type = JnxPppMlPppBundleName
_JnxPppMlPppBundleName_Object = MibTableColumn
jnxPppMlPppBundleName = _JnxPppMlPppBundleName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 1, 1, 1),
    _JnxPppMlPppBundleName_Type()
)
jnxPppMlPppBundleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPppMlPppBundleName.setStatus("current")
_JnxPppMlPppBundleRowStatus_Type = RowStatus
_JnxPppMlPppBundleRowStatus_Object = MibTableColumn
jnxPppMlPppBundleRowStatus = _JnxPppMlPppBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 1, 1, 2),
    _JnxPppMlPppBundleRowStatus_Type()
)
jnxPppMlPppBundleRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppBundleRowStatus.setStatus("current")
_JnxPppMlPppBundleNetworkIfIndex_Type = InterfaceIndex
_JnxPppMlPppBundleNetworkIfIndex_Object = MibTableColumn
jnxPppMlPppBundleNetworkIfIndex = _JnxPppMlPppBundleNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 1, 1, 3),
    _JnxPppMlPppBundleNetworkIfIndex_Type()
)
jnxPppMlPppBundleNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppBundleNetworkIfIndex.setStatus("current")
_JnxPppMlPppNextLinkIfIndex_Type = InterfaceIndexOrZero
_JnxPppMlPppNextLinkIfIndex_Object = MibScalar
jnxPppMlPppNextLinkIfIndex = _JnxPppMlPppNextLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 2),
    _JnxPppMlPppNextLinkIfIndex_Type()
)
jnxPppMlPppNextLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppNextLinkIfIndex.setStatus("current")
_JnxPppMlPppLinkConfigTable_Object = MibTable
jnxPppMlPppLinkConfigTable = _JnxPppMlPppLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3)
)
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigTable.setStatus("current")
_JnxPppMlPppLinkConfigEntry_Object = MibTableRow
jnxPppMlPppLinkConfigEntry = _JnxPppMlPppLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1)
)
jnxPppMlPppLinkConfigEntry.setIndexNames(
    (0, "JNX-PPP-MIB", "jnxPppMlPppLinkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigEntry.setStatus("current")
_JnxPppMlPppLinkConfigIfIndex_Type = InterfaceIndex
_JnxPppMlPppLinkConfigIfIndex_Object = MibTableColumn
jnxPppMlPppLinkConfigIfIndex = _JnxPppMlPppLinkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 1),
    _JnxPppMlPppLinkConfigIfIndex_Type()
)
jnxPppMlPppLinkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigIfIndex.setStatus("current")
_JnxPppMlPppLinkConfigLowerIfIndex_Type = InterfaceIndexOrZero
_JnxPppMlPppLinkConfigLowerIfIndex_Object = MibTableColumn
jnxPppMlPppLinkConfigLowerIfIndex = _JnxPppMlPppLinkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 2),
    _JnxPppMlPppLinkConfigLowerIfIndex_Type()
)
jnxPppMlPppLinkConfigLowerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigLowerIfIndex.setStatus("current")


class _JnxPppMlPppLinkConfigKeepalive_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigKeepalive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 64800),
    )


_JnxPppMlPppLinkConfigKeepalive_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigKeepalive_Object = MibTableColumn
jnxPppMlPppLinkConfigKeepalive = _JnxPppMlPppLinkConfigKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 4),
    _JnxPppMlPppLinkConfigKeepalive_Type()
)
jnxPppMlPppLinkConfigKeepalive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigKeepalive.setUnits("seconds")


class _JnxPppMlPppLinkConfigAuthentication_Type(JnxPppAuthentication):
    """Custom type jnxPppMlPppLinkConfigAuthentication based on JnxPppAuthentication"""


_JnxPppMlPppLinkConfigAuthentication_Object = MibTableColumn
jnxPppMlPppLinkConfigAuthentication = _JnxPppMlPppLinkConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 5),
    _JnxPppMlPppLinkConfigAuthentication_Type()
)
jnxPppMlPppLinkConfigAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigAuthentication.setStatus("deprecated")


class _JnxPppMlPppLinkConfigMaxAuthenRetries_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigMaxAuthenRetries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_JnxPppMlPppLinkConfigMaxAuthenRetries_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigMaxAuthenRetries_Object = MibTableColumn
jnxPppMlPppLinkConfigMaxAuthenRetries = _JnxPppMlPppLinkConfigMaxAuthenRetries_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 6),
    _JnxPppMlPppLinkConfigMaxAuthenRetries_Type()
)
jnxPppMlPppLinkConfigMaxAuthenRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigMaxAuthenRetries.setStatus("current")
_JnxPppMlPppLinkConfigRowStatus_Type = RowStatus
_JnxPppMlPppLinkConfigRowStatus_Object = MibTableColumn
jnxPppMlPppLinkConfigRowStatus = _JnxPppMlPppLinkConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 7),
    _JnxPppMlPppLinkConfigRowStatus_Type()
)
jnxPppMlPppLinkConfigRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigRowStatus.setStatus("current")
_JnxPppMlPppLinkConfigAaaProfile_Type = OctetString
_JnxPppMlPppLinkConfigAaaProfile_Object = MibTableColumn
jnxPppMlPppLinkConfigAaaProfile = _JnxPppMlPppLinkConfigAaaProfile_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 8),
    _JnxPppMlPppLinkConfigAaaProfile_Type()
)
jnxPppMlPppLinkConfigAaaProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigAaaProfile.setStatus("current")


class _JnxPppMlPppLinkConfigChapMinChallengeLength_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigChapMinChallengeLength based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_JnxPppMlPppLinkConfigChapMinChallengeLength_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigChapMinChallengeLength_Object = MibTableColumn
jnxPppMlPppLinkConfigChapMinChallengeLength = _JnxPppMlPppLinkConfigChapMinChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 9),
    _JnxPppMlPppLinkConfigChapMinChallengeLength_Type()
)
jnxPppMlPppLinkConfigChapMinChallengeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigChapMinChallengeLength.setStatus("current")


class _JnxPppMlPppLinkConfigChapMaxChallengeLength_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigChapMaxChallengeLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_JnxPppMlPppLinkConfigChapMaxChallengeLength_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigChapMaxChallengeLength_Object = MibTableColumn
jnxPppMlPppLinkConfigChapMaxChallengeLength = _JnxPppMlPppLinkConfigChapMaxChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 10),
    _JnxPppMlPppLinkConfigChapMaxChallengeLength_Type()
)
jnxPppMlPppLinkConfigChapMaxChallengeLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigChapMaxChallengeLength.setStatus("current")


class _JnxPppMlPppLinkConfigPassiveMode_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigPassiveMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppMlPppLinkConfigPassiveMode_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigPassiveMode_Object = MibTableColumn
jnxPppMlPppLinkConfigPassiveMode = _JnxPppMlPppLinkConfigPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 11),
    _JnxPppMlPppLinkConfigPassiveMode_Type()
)
jnxPppMlPppLinkConfigPassiveMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigPassiveMode.setStatus("current")
_JnxPppMlPppLinkConfigAuthenticatorLogicalSystem_Type = OctetString
_JnxPppMlPppLinkConfigAuthenticatorLogicalSystem_Object = MibTableColumn
jnxPppMlPppLinkConfigAuthenticatorLogicalSystem = _JnxPppMlPppLinkConfigAuthenticatorLogicalSystem_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 12),
    _JnxPppMlPppLinkConfigAuthenticatorLogicalSystem_Type()
)
jnxPppMlPppLinkConfigAuthenticatorLogicalSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigAuthenticatorLogicalSystem.setStatus("current")
_JnxPppMlPppLinkConfigAuthenticatorRoutingInstance_Type = OctetString
_JnxPppMlPppLinkConfigAuthenticatorRoutingInstance_Object = MibTableColumn
jnxPppMlPppLinkConfigAuthenticatorRoutingInstance = _JnxPppMlPppLinkConfigAuthenticatorRoutingInstance_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 13),
    _JnxPppMlPppLinkConfigAuthenticatorRoutingInstance_Type()
)
jnxPppMlPppLinkConfigAuthenticatorRoutingInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigAuthenticatorRoutingInstance.setStatus("current")


class _JnxPppMlPppLinkConfigFragmentation_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigFragmentation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppMlPppLinkConfigFragmentation_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigFragmentation_Object = MibTableColumn
jnxPppMlPppLinkConfigFragmentation = _JnxPppMlPppLinkConfigFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 14),
    _JnxPppMlPppLinkConfigFragmentation_Type()
)
jnxPppMlPppLinkConfigFragmentation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigFragmentation.setStatus("current")


class _JnxPppMlPppLinkConfigReassembly_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigReassembly based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppMlPppLinkConfigReassembly_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigReassembly_Object = MibTableColumn
jnxPppMlPppLinkConfigReassembly = _JnxPppMlPppLinkConfigReassembly_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 15),
    _JnxPppMlPppLinkConfigReassembly_Type()
)
jnxPppMlPppLinkConfigReassembly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigReassembly.setStatus("current")


class _JnxPppMlPppLinkConfigMaxReceiveReconstructedUnit_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigMaxReceiveReconstructedUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(64, 65535),
    )


_JnxPppMlPppLinkConfigMaxReceiveReconstructedUnit_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigMaxReceiveReconstructedUnit_Object = MibTableColumn
jnxPppMlPppLinkConfigMaxReceiveReconstructedUnit = _JnxPppMlPppLinkConfigMaxReceiveReconstructedUnit_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 16),
    _JnxPppMlPppLinkConfigMaxReceiveReconstructedUnit_Type()
)
jnxPppMlPppLinkConfigMaxReceiveReconstructedUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigMaxReceiveReconstructedUnit.setStatus("current")


class _JnxPppMlPppLinkConfigFragmentSize_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigFragmentSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(128, 65535),
    )


_JnxPppMlPppLinkConfigFragmentSize_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigFragmentSize_Object = MibTableColumn
jnxPppMlPppLinkConfigFragmentSize = _JnxPppMlPppLinkConfigFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 17),
    _JnxPppMlPppLinkConfigFragmentSize_Type()
)
jnxPppMlPppLinkConfigFragmentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigFragmentSize.setStatus("current")


class _JnxPppMlPppLinkConfigHashLinkSelection_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigHashLinkSelection based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppMlPppLinkConfigHashLinkSelection_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigHashLinkSelection_Object = MibTableColumn
jnxPppMlPppLinkConfigHashLinkSelection = _JnxPppMlPppLinkConfigHashLinkSelection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 18),
    _JnxPppMlPppLinkConfigHashLinkSelection_Type()
)
jnxPppMlPppLinkConfigHashLinkSelection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigHashLinkSelection.setStatus("current")


class _JnxPppMlPppLinkConfigAuthentication2_Type(JnxNibbleConfig):
    """Custom type jnxPppMlPppLinkConfigAuthentication2 based on JnxNibbleConfig"""
    defaultValue = 0


_JnxPppMlPppLinkConfigAuthentication2_Object = MibTableColumn
jnxPppMlPppLinkConfigAuthentication2 = _JnxPppMlPppLinkConfigAuthentication2_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 19),
    _JnxPppMlPppLinkConfigAuthentication2_Type()
)
jnxPppMlPppLinkConfigAuthentication2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigAuthentication2.setStatus("current")


class _JnxPppMlPppLinkConfigIgnoreMagicNumberMismatch_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigIgnoreMagicNumberMismatch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppMlPppLinkConfigIgnoreMagicNumberMismatch_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigIgnoreMagicNumberMismatch_Object = MibTableColumn
jnxPppMlPppLinkConfigIgnoreMagicNumberMismatch = _JnxPppMlPppLinkConfigIgnoreMagicNumberMismatch_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 20),
    _JnxPppMlPppLinkConfigIgnoreMagicNumberMismatch_Type()
)
jnxPppMlPppLinkConfigIgnoreMagicNumberMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigIgnoreMagicNumberMismatch.setStatus("current")


class _JnxPppMlPppLinkConfigMultilinkMulticlass_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigMultilinkMulticlass based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppMlPppLinkConfigMultilinkMulticlass_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigMultilinkMulticlass_Object = MibTableColumn
jnxPppMlPppLinkConfigMultilinkMulticlass = _JnxPppMlPppLinkConfigMultilinkMulticlass_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 21),
    _JnxPppMlPppLinkConfigMultilinkMulticlass_Type()
)
jnxPppMlPppLinkConfigMultilinkMulticlass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigMultilinkMulticlass.setStatus("current")


class _JnxPppMlPppLinkConfigMultilinkMaxMultiClasses_Type(Integer32):
    """Custom type jnxPppMlPppLinkConfigMultilinkMaxMultiClasses based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_JnxPppMlPppLinkConfigMultilinkMaxMultiClasses_Type.__name__ = "Integer32"
_JnxPppMlPppLinkConfigMultilinkMaxMultiClasses_Object = MibTableColumn
jnxPppMlPppLinkConfigMultilinkMaxMultiClasses = _JnxPppMlPppLinkConfigMultilinkMaxMultiClasses_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 3, 1, 22),
    _JnxPppMlPppLinkConfigMultilinkMaxMultiClasses_Type()
)
jnxPppMlPppLinkConfigMultilinkMaxMultiClasses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppLinkConfigMultilinkMaxMultiClasses.setStatus("current")
_JnxPppMlPppNextNetworkIfIndex_Type = InterfaceIndexOrZero
_JnxPppMlPppNextNetworkIfIndex_Object = MibScalar
jnxPppMlPppNextNetworkIfIndex = _JnxPppMlPppNextNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 4),
    _JnxPppMlPppNextNetworkIfIndex_Type()
)
jnxPppMlPppNextNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppNextNetworkIfIndex.setStatus("current")
_JnxPppMlPppNetworkConfigTable_Object = MibTable
jnxPppMlPppNetworkConfigTable = _JnxPppMlPppNetworkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 5)
)
if mibBuilder.loadTexts:
    jnxPppMlPppNetworkConfigTable.setStatus("current")
_JnxPppMlPppNetworkConfigEntry_Object = MibTableRow
jnxPppMlPppNetworkConfigEntry = _JnxPppMlPppNetworkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 5, 1)
)
jnxPppMlPppNetworkConfigEntry.setIndexNames(
    (0, "JNX-PPP-MIB", "jnxPppMlPppNetworkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    jnxPppMlPppNetworkConfigEntry.setStatus("current")
_JnxPppMlPppNetworkConfigIfIndex_Type = InterfaceIndex
_JnxPppMlPppNetworkConfigIfIndex_Object = MibTableColumn
jnxPppMlPppNetworkConfigIfIndex = _JnxPppMlPppNetworkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 5, 1, 1),
    _JnxPppMlPppNetworkConfigIfIndex_Type()
)
jnxPppMlPppNetworkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPppMlPppNetworkConfigIfIndex.setStatus("current")
_JnxPppMlPppNetworkConfigLowerIfIndex_Type = InterfaceIndex
_JnxPppMlPppNetworkConfigLowerIfIndex_Object = MibTableColumn
jnxPppMlPppNetworkConfigLowerIfIndex = _JnxPppMlPppNetworkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 5, 1, 2),
    _JnxPppMlPppNetworkConfigLowerIfIndex_Type()
)
jnxPppMlPppNetworkConfigLowerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppNetworkConfigLowerIfIndex.setStatus("current")
_JnxPppMlPppNetworkBundleName_Type = JnxPppMlPppBundleName
_JnxPppMlPppNetworkBundleName_Object = MibTableColumn
jnxPppMlPppNetworkBundleName = _JnxPppMlPppNetworkBundleName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 5, 1, 3),
    _JnxPppMlPppNetworkBundleName_Type()
)
jnxPppMlPppNetworkBundleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppNetworkBundleName.setStatus("current")
_JnxPppMlPppNetworkRowStatus_Type = RowStatus
_JnxPppMlPppNetworkRowStatus_Object = MibTableColumn
jnxPppMlPppNetworkRowStatus = _JnxPppMlPppNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 5, 1, 4),
    _JnxPppMlPppNetworkRowStatus_Type()
)
jnxPppMlPppNetworkRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppNetworkRowStatus.setStatus("current")
_JnxPppMlPppLinkBindTable_Object = MibTable
jnxPppMlPppLinkBindTable = _JnxPppMlPppLinkBindTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 6)
)
if mibBuilder.loadTexts:
    jnxPppMlPppLinkBindTable.setStatus("current")
_JnxPppMlPppLinkBindEntry_Object = MibTableRow
jnxPppMlPppLinkBindEntry = _JnxPppMlPppLinkBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 6, 1)
)
jnxPppMlPppLinkBindEntry.setIndexNames(
    (0, "JNX-PPP-MIB", "jnxPppMlPppBindNetworkIfIndex"),
    (0, "JNX-PPP-MIB", "jnxPppMlPppBindLinkIfIndex"),
)
if mibBuilder.loadTexts:
    jnxPppMlPppLinkBindEntry.setStatus("current")
_JnxPppMlPppBindNetworkIfIndex_Type = InterfaceIndex
_JnxPppMlPppBindNetworkIfIndex_Object = MibTableColumn
jnxPppMlPppBindNetworkIfIndex = _JnxPppMlPppBindNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 6, 1, 1),
    _JnxPppMlPppBindNetworkIfIndex_Type()
)
jnxPppMlPppBindNetworkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPppMlPppBindNetworkIfIndex.setStatus("current")
_JnxPppMlPppBindLinkIfIndex_Type = InterfaceIndex
_JnxPppMlPppBindLinkIfIndex_Object = MibTableColumn
jnxPppMlPppBindLinkIfIndex = _JnxPppMlPppBindLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 6, 1, 2),
    _JnxPppMlPppBindLinkIfIndex_Type()
)
jnxPppMlPppBindLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxPppMlPppBindLinkIfIndex.setStatus("current")
_JnxPppMlPppBindRowStatus_Type = RowStatus
_JnxPppMlPppBindRowStatus_Object = MibTableColumn
jnxPppMlPppBindRowStatus = _JnxPppMlPppBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 6, 6, 1, 3),
    _JnxPppMlPppBindRowStatus_Type()
)
jnxPppMlPppBindRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppMlPppBindRowStatus.setStatus("current")
_JnxPppSummary_ObjectIdentity = ObjectIdentity
jnxPppSummary = _JnxPppSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7)
)
_JnxPppSummaryPppInterfaceCount_Type = Integer32
_JnxPppSummaryPppInterfaceCount_Object = MibScalar
jnxPppSummaryPppInterfaceCount = _JnxPppSummaryPppInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 1),
    _JnxPppSummaryPppInterfaceCount_Type()
)
jnxPppSummaryPppInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppInterfaceCount.setStatus("current")
_JnxPppSummaryPppIpNCPs_Type = Integer32
_JnxPppSummaryPppIpNCPs_Object = MibScalar
jnxPppSummaryPppIpNCPs = _JnxPppSummaryPppIpNCPs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 2),
    _JnxPppSummaryPppIpNCPs_Type()
)
jnxPppSummaryPppIpNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpNCPs.setStatus("current")
_JnxPppSummaryPppOsiNCPs_Type = Integer32
_JnxPppSummaryPppOsiNCPs_Object = MibScalar
jnxPppSummaryPppOsiNCPs = _JnxPppSummaryPppOsiNCPs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 3),
    _JnxPppSummaryPppOsiNCPs_Type()
)
jnxPppSummaryPppOsiNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppOsiNCPs.setStatus("current")
_JnxPppSummaryPppIfAdminUp_Type = Integer32
_JnxPppSummaryPppIfAdminUp_Object = MibScalar
jnxPppSummaryPppIfAdminUp = _JnxPppSummaryPppIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 4),
    _JnxPppSummaryPppIfAdminUp_Type()
)
jnxPppSummaryPppIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIfAdminUp.setStatus("current")
_JnxPppSummaryPppIfAdminDown_Type = Integer32
_JnxPppSummaryPppIfAdminDown_Object = MibScalar
jnxPppSummaryPppIfAdminDown = _JnxPppSummaryPppIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 5),
    _JnxPppSummaryPppIfAdminDown_Type()
)
jnxPppSummaryPppIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIfAdminDown.setStatus("current")
_JnxPppSummaryPppIfOperUp_Type = Integer32
_JnxPppSummaryPppIfOperUp_Object = MibScalar
jnxPppSummaryPppIfOperUp = _JnxPppSummaryPppIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 7),
    _JnxPppSummaryPppIfOperUp_Type()
)
jnxPppSummaryPppIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIfOperUp.setStatus("current")
_JnxPppSummaryPppIfOperDown_Type = Integer32
_JnxPppSummaryPppIfOperDown_Object = MibScalar
jnxPppSummaryPppIfOperDown = _JnxPppSummaryPppIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 8),
    _JnxPppSummaryPppIfOperDown_Type()
)
jnxPppSummaryPppIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIfOperDown.setStatus("current")
_JnxPppSummaryPppIfOperDormant_Type = Integer32
_JnxPppSummaryPppIfOperDormant_Object = MibScalar
jnxPppSummaryPppIfOperDormant = _JnxPppSummaryPppIfOperDormant_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 9),
    _JnxPppSummaryPppIfOperDormant_Type()
)
jnxPppSummaryPppIfOperDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIfOperDormant.setStatus("current")
_JnxPppSummaryPppIfNotPresent_Type = Integer32
_JnxPppSummaryPppIfNotPresent_Object = MibScalar
jnxPppSummaryPppIfNotPresent = _JnxPppSummaryPppIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 10),
    _JnxPppSummaryPppIfNotPresent_Type()
)
jnxPppSummaryPppIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIfNotPresent.setStatus("current")
_JnxPppSummaryPppIfLowerLayerDown_Type = Integer32
_JnxPppSummaryPppIfLowerLayerDown_Object = MibScalar
jnxPppSummaryPppIfLowerLayerDown = _JnxPppSummaryPppIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 11),
    _JnxPppSummaryPppIfLowerLayerDown_Type()
)
jnxPppSummaryPppIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIfLowerLayerDown.setStatus("current")
_JnxPppSummaryPppIpNcpOpened_Type = Integer32
_JnxPppSummaryPppIpNcpOpened_Object = MibScalar
jnxPppSummaryPppIpNcpOpened = _JnxPppSummaryPppIpNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 12),
    _JnxPppSummaryPppIpNcpOpened_Type()
)
jnxPppSummaryPppIpNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpNcpOpened.setStatus("current")
_JnxPppSummaryPppIpNcpClosed_Type = Integer32
_JnxPppSummaryPppIpNcpClosed_Object = MibScalar
jnxPppSummaryPppIpNcpClosed = _JnxPppSummaryPppIpNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 13),
    _JnxPppSummaryPppIpNcpClosed_Type()
)
jnxPppSummaryPppIpNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpNcpClosed.setStatus("current")
_JnxPppSummaryPppOsiNcpOpened_Type = Integer32
_JnxPppSummaryPppOsiNcpOpened_Object = MibScalar
jnxPppSummaryPppOsiNcpOpened = _JnxPppSummaryPppOsiNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 14),
    _JnxPppSummaryPppOsiNcpOpened_Type()
)
jnxPppSummaryPppOsiNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppOsiNcpOpened.setStatus("current")
_JnxPppSummaryPppOsiNcpClosed_Type = Integer32
_JnxPppSummaryPppOsiNcpClosed_Object = MibScalar
jnxPppSummaryPppOsiNcpClosed = _JnxPppSummaryPppOsiNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 15),
    _JnxPppSummaryPppOsiNcpClosed_Type()
)
jnxPppSummaryPppOsiNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppOsiNcpClosed.setStatus("current")
_JnxPppSummaryPppIfLastChangeTime_Type = TimeTicks
_JnxPppSummaryPppIfLastChangeTime_Object = MibScalar
jnxPppSummaryPppIfLastChangeTime = _JnxPppSummaryPppIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 16),
    _JnxPppSummaryPppIfLastChangeTime_Type()
)
jnxPppSummaryPppIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIfLastChangeTime.setStatus("current")
_JnxPppSummaryPppLinkInterfaceCount_Type = Integer32
_JnxPppSummaryPppLinkInterfaceCount_Object = MibScalar
jnxPppSummaryPppLinkInterfaceCount = _JnxPppSummaryPppLinkInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 17),
    _JnxPppSummaryPppLinkInterfaceCount_Type()
)
jnxPppSummaryPppLinkInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppLinkInterfaceCount.setStatus("current")
_JnxPppSummaryPppLinkIfAdminUp_Type = Integer32
_JnxPppSummaryPppLinkIfAdminUp_Object = MibScalar
jnxPppSummaryPppLinkIfAdminUp = _JnxPppSummaryPppLinkIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 18),
    _JnxPppSummaryPppLinkIfAdminUp_Type()
)
jnxPppSummaryPppLinkIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppLinkIfAdminUp.setStatus("current")
_JnxPppSummaryPppLinkIfAdminDown_Type = Integer32
_JnxPppSummaryPppLinkIfAdminDown_Object = MibScalar
jnxPppSummaryPppLinkIfAdminDown = _JnxPppSummaryPppLinkIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 19),
    _JnxPppSummaryPppLinkIfAdminDown_Type()
)
jnxPppSummaryPppLinkIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppLinkIfAdminDown.setStatus("current")
_JnxPppSummaryPppLinkIfOperUp_Type = Integer32
_JnxPppSummaryPppLinkIfOperUp_Object = MibScalar
jnxPppSummaryPppLinkIfOperUp = _JnxPppSummaryPppLinkIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 20),
    _JnxPppSummaryPppLinkIfOperUp_Type()
)
jnxPppSummaryPppLinkIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppLinkIfOperUp.setStatus("current")
_JnxPppSummaryPppLinkIfOperDown_Type = Integer32
_JnxPppSummaryPppLinkIfOperDown_Object = MibScalar
jnxPppSummaryPppLinkIfOperDown = _JnxPppSummaryPppLinkIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 21),
    _JnxPppSummaryPppLinkIfOperDown_Type()
)
jnxPppSummaryPppLinkIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppLinkIfOperDown.setStatus("current")
_JnxPppSummaryPppLinkIfOperDormant_Type = Integer32
_JnxPppSummaryPppLinkIfOperDormant_Object = MibScalar
jnxPppSummaryPppLinkIfOperDormant = _JnxPppSummaryPppLinkIfOperDormant_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 22),
    _JnxPppSummaryPppLinkIfOperDormant_Type()
)
jnxPppSummaryPppLinkIfOperDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppLinkIfOperDormant.setStatus("current")
_JnxPppSummaryPppLinkIfNotPresent_Type = Integer32
_JnxPppSummaryPppLinkIfNotPresent_Object = MibScalar
jnxPppSummaryPppLinkIfNotPresent = _JnxPppSummaryPppLinkIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 23),
    _JnxPppSummaryPppLinkIfNotPresent_Type()
)
jnxPppSummaryPppLinkIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppLinkIfNotPresent.setStatus("current")
_JnxPppSummaryPppLinkIfLowerLayerDown_Type = Integer32
_JnxPppSummaryPppLinkIfLowerLayerDown_Object = MibScalar
jnxPppSummaryPppLinkIfLowerLayerDown = _JnxPppSummaryPppLinkIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 24),
    _JnxPppSummaryPppLinkIfLowerLayerDown_Type()
)
jnxPppSummaryPppLinkIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppLinkIfLowerLayerDown.setStatus("current")
_JnxPppSummaryPppLinkIfLastChangeTime_Type = TimeTicks
_JnxPppSummaryPppLinkIfLastChangeTime_Object = MibScalar
jnxPppSummaryPppLinkIfLastChangeTime = _JnxPppSummaryPppLinkIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 25),
    _JnxPppSummaryPppLinkIfLastChangeTime_Type()
)
jnxPppSummaryPppLinkIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppLinkIfLastChangeTime.setStatus("current")
_JnxPppSummaryPppNetworkInterfaceCount_Type = Integer32
_JnxPppSummaryPppNetworkInterfaceCount_Object = MibScalar
jnxPppSummaryPppNetworkInterfaceCount = _JnxPppSummaryPppNetworkInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 26),
    _JnxPppSummaryPppNetworkInterfaceCount_Type()
)
jnxPppSummaryPppNetworkInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkInterfaceCount.setStatus("current")
_JnxPppSummaryPppNetworkIpNCPs_Type = Integer32
_JnxPppSummaryPppNetworkIpNCPs_Object = MibScalar
jnxPppSummaryPppNetworkIpNCPs = _JnxPppSummaryPppNetworkIpNCPs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 27),
    _JnxPppSummaryPppNetworkIpNCPs_Type()
)
jnxPppSummaryPppNetworkIpNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpNCPs.setStatus("current")
_JnxPppSummaryPppNetworkOsiNCPs_Type = Integer32
_JnxPppSummaryPppNetworkOsiNCPs_Object = MibScalar
jnxPppSummaryPppNetworkOsiNCPs = _JnxPppSummaryPppNetworkOsiNCPs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 28),
    _JnxPppSummaryPppNetworkOsiNCPs_Type()
)
jnxPppSummaryPppNetworkOsiNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkOsiNCPs.setStatus("current")
_JnxPppSummaryPppNetworkIfAdminUp_Type = Integer32
_JnxPppSummaryPppNetworkIfAdminUp_Object = MibScalar
jnxPppSummaryPppNetworkIfAdminUp = _JnxPppSummaryPppNetworkIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 29),
    _JnxPppSummaryPppNetworkIfAdminUp_Type()
)
jnxPppSummaryPppNetworkIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIfAdminUp.setStatus("current")
_JnxPppSummaryPppNetworkIfAdminDown_Type = Integer32
_JnxPppSummaryPppNetworkIfAdminDown_Object = MibScalar
jnxPppSummaryPppNetworkIfAdminDown = _JnxPppSummaryPppNetworkIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 30),
    _JnxPppSummaryPppNetworkIfAdminDown_Type()
)
jnxPppSummaryPppNetworkIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIfAdminDown.setStatus("current")
_JnxPppSummaryPppNetworkIfOperUp_Type = Integer32
_JnxPppSummaryPppNetworkIfOperUp_Object = MibScalar
jnxPppSummaryPppNetworkIfOperUp = _JnxPppSummaryPppNetworkIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 31),
    _JnxPppSummaryPppNetworkIfOperUp_Type()
)
jnxPppSummaryPppNetworkIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIfOperUp.setStatus("current")
_JnxPppSummaryPppNetworkIfOperDown_Type = Integer32
_JnxPppSummaryPppNetworkIfOperDown_Object = MibScalar
jnxPppSummaryPppNetworkIfOperDown = _JnxPppSummaryPppNetworkIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 32),
    _JnxPppSummaryPppNetworkIfOperDown_Type()
)
jnxPppSummaryPppNetworkIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIfOperDown.setStatus("current")
_JnxPppSummaryPppNetworkIfOperDormant_Type = Integer32
_JnxPppSummaryPppNetworkIfOperDormant_Object = MibScalar
jnxPppSummaryPppNetworkIfOperDormant = _JnxPppSummaryPppNetworkIfOperDormant_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 33),
    _JnxPppSummaryPppNetworkIfOperDormant_Type()
)
jnxPppSummaryPppNetworkIfOperDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIfOperDormant.setStatus("current")
_JnxPppSummaryPppNetworkIfNotPresent_Type = Integer32
_JnxPppSummaryPppNetworkIfNotPresent_Object = MibScalar
jnxPppSummaryPppNetworkIfNotPresent = _JnxPppSummaryPppNetworkIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 34),
    _JnxPppSummaryPppNetworkIfNotPresent_Type()
)
jnxPppSummaryPppNetworkIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIfNotPresent.setStatus("current")
_JnxPppSummaryPppNetworkIfLowerLayerDown_Type = Integer32
_JnxPppSummaryPppNetworkIfLowerLayerDown_Object = MibScalar
jnxPppSummaryPppNetworkIfLowerLayerDown = _JnxPppSummaryPppNetworkIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 35),
    _JnxPppSummaryPppNetworkIfLowerLayerDown_Type()
)
jnxPppSummaryPppNetworkIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIfLowerLayerDown.setStatus("current")
_JnxPppSummaryPppNetworkIpNcpOpened_Type = Integer32
_JnxPppSummaryPppNetworkIpNcpOpened_Object = MibScalar
jnxPppSummaryPppNetworkIpNcpOpened = _JnxPppSummaryPppNetworkIpNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 36),
    _JnxPppSummaryPppNetworkIpNcpOpened_Type()
)
jnxPppSummaryPppNetworkIpNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpNcpOpened.setStatus("current")
_JnxPppSummaryPppNetworkIpNcpClosed_Type = Integer32
_JnxPppSummaryPppNetworkIpNcpClosed_Object = MibScalar
jnxPppSummaryPppNetworkIpNcpClosed = _JnxPppSummaryPppNetworkIpNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 37),
    _JnxPppSummaryPppNetworkIpNcpClosed_Type()
)
jnxPppSummaryPppNetworkIpNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpNcpClosed.setStatus("current")
_JnxPppSummaryPppNetworkOsiNcpOpened_Type = Integer32
_JnxPppSummaryPppNetworkOsiNcpOpened_Object = MibScalar
jnxPppSummaryPppNetworkOsiNcpOpened = _JnxPppSummaryPppNetworkOsiNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 38),
    _JnxPppSummaryPppNetworkOsiNcpOpened_Type()
)
jnxPppSummaryPppNetworkOsiNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkOsiNcpOpened.setStatus("current")
_JnxPppSummaryPppNetworkOsiNcpClosed_Type = Integer32
_JnxPppSummaryPppNetworkOsiNcpClosed_Object = MibScalar
jnxPppSummaryPppNetworkOsiNcpClosed = _JnxPppSummaryPppNetworkOsiNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 39),
    _JnxPppSummaryPppNetworkOsiNcpClosed_Type()
)
jnxPppSummaryPppNetworkOsiNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkOsiNcpClosed.setStatus("current")
_JnxPppSummaryPppNetworkIfLastChangeTime_Type = TimeTicks
_JnxPppSummaryPppNetworkIfLastChangeTime_Object = MibScalar
jnxPppSummaryPppNetworkIfLastChangeTime = _JnxPppSummaryPppNetworkIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 40),
    _JnxPppSummaryPppNetworkIfLastChangeTime_Type()
)
jnxPppSummaryPppNetworkIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIfLastChangeTime.setStatus("current")
_JnxPppSummaryPppIpv6NCPs_Type = Integer32
_JnxPppSummaryPppIpv6NCPs_Object = MibScalar
jnxPppSummaryPppIpv6NCPs = _JnxPppSummaryPppIpv6NCPs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 41),
    _JnxPppSummaryPppIpv6NCPs_Type()
)
jnxPppSummaryPppIpv6NCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpv6NCPs.setStatus("current")
_JnxPppSummaryPppIpv6NcpOpened_Type = Integer32
_JnxPppSummaryPppIpv6NcpOpened_Object = MibScalar
jnxPppSummaryPppIpv6NcpOpened = _JnxPppSummaryPppIpv6NcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 42),
    _JnxPppSummaryPppIpv6NcpOpened_Type()
)
jnxPppSummaryPppIpv6NcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpv6NcpOpened.setStatus("current")
_JnxPppSummaryPppIpv6NcpClosed_Type = Integer32
_JnxPppSummaryPppIpv6NcpClosed_Object = MibScalar
jnxPppSummaryPppIpv6NcpClosed = _JnxPppSummaryPppIpv6NcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 43),
    _JnxPppSummaryPppIpv6NcpClosed_Type()
)
jnxPppSummaryPppIpv6NcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpv6NcpClosed.setStatus("current")
_JnxPppSummaryPppNetworkIpv6NCPs_Type = Integer32
_JnxPppSummaryPppNetworkIpv6NCPs_Object = MibScalar
jnxPppSummaryPppNetworkIpv6NCPs = _JnxPppSummaryPppNetworkIpv6NCPs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 44),
    _JnxPppSummaryPppNetworkIpv6NCPs_Type()
)
jnxPppSummaryPppNetworkIpv6NCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpv6NCPs.setStatus("current")
_JnxPppSummaryPppNetworkIpv6NcpOpened_Type = Integer32
_JnxPppSummaryPppNetworkIpv6NcpOpened_Object = MibScalar
jnxPppSummaryPppNetworkIpv6NcpOpened = _JnxPppSummaryPppNetworkIpv6NcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 45),
    _JnxPppSummaryPppNetworkIpv6NcpOpened_Type()
)
jnxPppSummaryPppNetworkIpv6NcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpv6NcpOpened.setStatus("current")
_JnxPppSummaryPppNetworkIpv6NcpClosed_Type = Integer32
_JnxPppSummaryPppNetworkIpv6NcpClosed_Object = MibScalar
jnxPppSummaryPppNetworkIpv6NcpClosed = _JnxPppSummaryPppNetworkIpv6NcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 46),
    _JnxPppSummaryPppNetworkIpv6NcpClosed_Type()
)
jnxPppSummaryPppNetworkIpv6NcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpv6NcpClosed.setStatus("current")
_JnxPppSummaryPppStaticInterfaceCount_Type = Integer32
_JnxPppSummaryPppStaticInterfaceCount_Object = MibScalar
jnxPppSummaryPppStaticInterfaceCount = _JnxPppSummaryPppStaticInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 47),
    _JnxPppSummaryPppStaticInterfaceCount_Type()
)
jnxPppSummaryPppStaticInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppStaticInterfaceCount.setStatus("current")
_JnxPppSummaryPppMplsNCPs_Type = Integer32
_JnxPppSummaryPppMplsNCPs_Object = MibScalar
jnxPppSummaryPppMplsNCPs = _JnxPppSummaryPppMplsNCPs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 48),
    _JnxPppSummaryPppMplsNCPs_Type()
)
jnxPppSummaryPppMplsNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppMplsNCPs.setStatus("current")
_JnxPppSummaryPppIpAdminOpen_Type = Integer32
_JnxPppSummaryPppIpAdminOpen_Object = MibScalar
jnxPppSummaryPppIpAdminOpen = _JnxPppSummaryPppIpAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 49),
    _JnxPppSummaryPppIpAdminOpen_Type()
)
jnxPppSummaryPppIpAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpAdminOpen.setStatus("current")
_JnxPppSummaryPppIpAdminClose_Type = Integer32
_JnxPppSummaryPppIpAdminClose_Object = MibScalar
jnxPppSummaryPppIpAdminClose = _JnxPppSummaryPppIpAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 50),
    _JnxPppSummaryPppIpAdminClose_Type()
)
jnxPppSummaryPppIpAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpAdminClose.setStatus("current")
_JnxPppSummaryPppIpv6AdminOpen_Type = Integer32
_JnxPppSummaryPppIpv6AdminOpen_Object = MibScalar
jnxPppSummaryPppIpv6AdminOpen = _JnxPppSummaryPppIpv6AdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 51),
    _JnxPppSummaryPppIpv6AdminOpen_Type()
)
jnxPppSummaryPppIpv6AdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpv6AdminOpen.setStatus("current")
_JnxPppSummaryPppIpv6AdminClose_Type = Integer32
_JnxPppSummaryPppIpv6AdminClose_Object = MibScalar
jnxPppSummaryPppIpv6AdminClose = _JnxPppSummaryPppIpv6AdminClose_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 52),
    _JnxPppSummaryPppIpv6AdminClose_Type()
)
jnxPppSummaryPppIpv6AdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpv6AdminClose.setStatus("current")
_JnxPppSummaryPppOsiAdminOpen_Type = Integer32
_JnxPppSummaryPppOsiAdminOpen_Object = MibScalar
jnxPppSummaryPppOsiAdminOpen = _JnxPppSummaryPppOsiAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 53),
    _JnxPppSummaryPppOsiAdminOpen_Type()
)
jnxPppSummaryPppOsiAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppOsiAdminOpen.setStatus("current")
_JnxPppSummaryPppOsiAdminClose_Type = Integer32
_JnxPppSummaryPppOsiAdminClose_Object = MibScalar
jnxPppSummaryPppOsiAdminClose = _JnxPppSummaryPppOsiAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 54),
    _JnxPppSummaryPppOsiAdminClose_Type()
)
jnxPppSummaryPppOsiAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppOsiAdminClose.setStatus("current")
_JnxPppSummaryPppMplsAdminOpen_Type = Integer32
_JnxPppSummaryPppMplsAdminOpen_Object = MibScalar
jnxPppSummaryPppMplsAdminOpen = _JnxPppSummaryPppMplsAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 55),
    _JnxPppSummaryPppMplsAdminOpen_Type()
)
jnxPppSummaryPppMplsAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppMplsAdminOpen.setStatus("current")
_JnxPppSummaryPppMplsAdminClose_Type = Integer32
_JnxPppSummaryPppMplsAdminClose_Object = MibScalar
jnxPppSummaryPppMplsAdminClose = _JnxPppSummaryPppMplsAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 56),
    _JnxPppSummaryPppMplsAdminClose_Type()
)
jnxPppSummaryPppMplsAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppMplsAdminClose.setStatus("current")
_JnxPppSummaryPppIpNcpNotPresent_Type = Integer32
_JnxPppSummaryPppIpNcpNotPresent_Object = MibScalar
jnxPppSummaryPppIpNcpNotPresent = _JnxPppSummaryPppIpNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 57),
    _JnxPppSummaryPppIpNcpNotPresent_Type()
)
jnxPppSummaryPppIpNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpNcpNotPresent.setStatus("current")
_JnxPppSummaryPppIpNcpNoResources_Type = Integer32
_JnxPppSummaryPppIpNcpNoResources_Object = MibScalar
jnxPppSummaryPppIpNcpNoResources = _JnxPppSummaryPppIpNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 58),
    _JnxPppSummaryPppIpNcpNoResources_Type()
)
jnxPppSummaryPppIpNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpNcpNoResources.setStatus("current")
_JnxPppSummaryPppIpv6NcpNotPresent_Type = Integer32
_JnxPppSummaryPppIpv6NcpNotPresent_Object = MibScalar
jnxPppSummaryPppIpv6NcpNotPresent = _JnxPppSummaryPppIpv6NcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 59),
    _JnxPppSummaryPppIpv6NcpNotPresent_Type()
)
jnxPppSummaryPppIpv6NcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpv6NcpNotPresent.setStatus("current")
_JnxPppSummaryPppIpv6NcpNoResources_Type = Integer32
_JnxPppSummaryPppIpv6NcpNoResources_Object = MibScalar
jnxPppSummaryPppIpv6NcpNoResources = _JnxPppSummaryPppIpv6NcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 60),
    _JnxPppSummaryPppIpv6NcpNoResources_Type()
)
jnxPppSummaryPppIpv6NcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppIpv6NcpNoResources.setStatus("current")
_JnxPppSummaryPppOsiNcpNotPresent_Type = Integer32
_JnxPppSummaryPppOsiNcpNotPresent_Object = MibScalar
jnxPppSummaryPppOsiNcpNotPresent = _JnxPppSummaryPppOsiNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 61),
    _JnxPppSummaryPppOsiNcpNotPresent_Type()
)
jnxPppSummaryPppOsiNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppOsiNcpNotPresent.setStatus("current")
_JnxPppSummaryPppOsiNcpNoResources_Type = Integer32
_JnxPppSummaryPppOsiNcpNoResources_Object = MibScalar
jnxPppSummaryPppOsiNcpNoResources = _JnxPppSummaryPppOsiNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 62),
    _JnxPppSummaryPppOsiNcpNoResources_Type()
)
jnxPppSummaryPppOsiNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppOsiNcpNoResources.setStatus("current")
_JnxPppSummaryPppMplsNcpOpened_Type = Integer32
_JnxPppSummaryPppMplsNcpOpened_Object = MibScalar
jnxPppSummaryPppMplsNcpOpened = _JnxPppSummaryPppMplsNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 63),
    _JnxPppSummaryPppMplsNcpOpened_Type()
)
jnxPppSummaryPppMplsNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppMplsNcpOpened.setStatus("current")
_JnxPppSummaryPppMplsNcpClosed_Type = Integer32
_JnxPppSummaryPppMplsNcpClosed_Object = MibScalar
jnxPppSummaryPppMplsNcpClosed = _JnxPppSummaryPppMplsNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 64),
    _JnxPppSummaryPppMplsNcpClosed_Type()
)
jnxPppSummaryPppMplsNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppMplsNcpClosed.setStatus("current")
_JnxPppSummaryPppMplsNcpNotPresent_Type = Integer32
_JnxPppSummaryPppMplsNcpNotPresent_Object = MibScalar
jnxPppSummaryPppMplsNcpNotPresent = _JnxPppSummaryPppMplsNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 65),
    _JnxPppSummaryPppMplsNcpNotPresent_Type()
)
jnxPppSummaryPppMplsNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppMplsNcpNotPresent.setStatus("current")
_JnxPppSummaryPppMplsNcpNoResources_Type = Integer32
_JnxPppSummaryPppMplsNcpNoResources_Object = MibScalar
jnxPppSummaryPppMplsNcpNoResources = _JnxPppSummaryPppMplsNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 66),
    _JnxPppSummaryPppMplsNcpNoResources_Type()
)
jnxPppSummaryPppMplsNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppMplsNcpNoResources.setStatus("current")
_JnxPppSummaryPppLinkStaticInterfaceCount_Type = Integer32
_JnxPppSummaryPppLinkStaticInterfaceCount_Object = MibScalar
jnxPppSummaryPppLinkStaticInterfaceCount = _JnxPppSummaryPppLinkStaticInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 67),
    _JnxPppSummaryPppLinkStaticInterfaceCount_Type()
)
jnxPppSummaryPppLinkStaticInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppLinkStaticInterfaceCount.setStatus("current")
_JnxPppSummaryPppNetworkStaticInterfaceCount_Type = Integer32
_JnxPppSummaryPppNetworkStaticInterfaceCount_Object = MibScalar
jnxPppSummaryPppNetworkStaticInterfaceCount = _JnxPppSummaryPppNetworkStaticInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 68),
    _JnxPppSummaryPppNetworkStaticInterfaceCount_Type()
)
jnxPppSummaryPppNetworkStaticInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkStaticInterfaceCount.setStatus("current")
_JnxPppSummaryPppNetworkMplsNCPs_Type = Integer32
_JnxPppSummaryPppNetworkMplsNCPs_Object = MibScalar
jnxPppSummaryPppNetworkMplsNCPs = _JnxPppSummaryPppNetworkMplsNCPs_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 69),
    _JnxPppSummaryPppNetworkMplsNCPs_Type()
)
jnxPppSummaryPppNetworkMplsNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkMplsNCPs.setStatus("current")
_JnxPppSummaryPppNetworkIpAdminOpen_Type = Integer32
_JnxPppSummaryPppNetworkIpAdminOpen_Object = MibScalar
jnxPppSummaryPppNetworkIpAdminOpen = _JnxPppSummaryPppNetworkIpAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 70),
    _JnxPppSummaryPppNetworkIpAdminOpen_Type()
)
jnxPppSummaryPppNetworkIpAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpAdminOpen.setStatus("current")
_JnxPppSummaryPppNetworkIpAdminClose_Type = Integer32
_JnxPppSummaryPppNetworkIpAdminClose_Object = MibScalar
jnxPppSummaryPppNetworkIpAdminClose = _JnxPppSummaryPppNetworkIpAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 71),
    _JnxPppSummaryPppNetworkIpAdminClose_Type()
)
jnxPppSummaryPppNetworkIpAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpAdminClose.setStatus("current")
_JnxPppSummaryPppNetworkIpv6AdminOpen_Type = Integer32
_JnxPppSummaryPppNetworkIpv6AdminOpen_Object = MibScalar
jnxPppSummaryPppNetworkIpv6AdminOpen = _JnxPppSummaryPppNetworkIpv6AdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 72),
    _JnxPppSummaryPppNetworkIpv6AdminOpen_Type()
)
jnxPppSummaryPppNetworkIpv6AdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpv6AdminOpen.setStatus("current")
_JnxPppSummaryPppNetworkIpv6AdminClose_Type = Integer32
_JnxPppSummaryPppNetworkIpv6AdminClose_Object = MibScalar
jnxPppSummaryPppNetworkIpv6AdminClose = _JnxPppSummaryPppNetworkIpv6AdminClose_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 73),
    _JnxPppSummaryPppNetworkIpv6AdminClose_Type()
)
jnxPppSummaryPppNetworkIpv6AdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpv6AdminClose.setStatus("current")
_JnxPppSummaryPppNetworkOsiAdminOpen_Type = Integer32
_JnxPppSummaryPppNetworkOsiAdminOpen_Object = MibScalar
jnxPppSummaryPppNetworkOsiAdminOpen = _JnxPppSummaryPppNetworkOsiAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 74),
    _JnxPppSummaryPppNetworkOsiAdminOpen_Type()
)
jnxPppSummaryPppNetworkOsiAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkOsiAdminOpen.setStatus("current")
_JnxPppSummaryPppNetworkOsiAdminClose_Type = Integer32
_JnxPppSummaryPppNetworkOsiAdminClose_Object = MibScalar
jnxPppSummaryPppNetworkOsiAdminClose = _JnxPppSummaryPppNetworkOsiAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 75),
    _JnxPppSummaryPppNetworkOsiAdminClose_Type()
)
jnxPppSummaryPppNetworkOsiAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkOsiAdminClose.setStatus("current")
_JnxPppSummaryPppNetworkMplsAdminOpen_Type = Integer32
_JnxPppSummaryPppNetworkMplsAdminOpen_Object = MibScalar
jnxPppSummaryPppNetworkMplsAdminOpen = _JnxPppSummaryPppNetworkMplsAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 76),
    _JnxPppSummaryPppNetworkMplsAdminOpen_Type()
)
jnxPppSummaryPppNetworkMplsAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkMplsAdminOpen.setStatus("current")
_JnxPppSummaryPppNetworkMplsAdminClose_Type = Integer32
_JnxPppSummaryPppNetworkMplsAdminClose_Object = MibScalar
jnxPppSummaryPppNetworkMplsAdminClose = _JnxPppSummaryPppNetworkMplsAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 77),
    _JnxPppSummaryPppNetworkMplsAdminClose_Type()
)
jnxPppSummaryPppNetworkMplsAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkMplsAdminClose.setStatus("current")
_JnxPppSummaryPppNetworkIpNcpNotPresent_Type = Integer32
_JnxPppSummaryPppNetworkIpNcpNotPresent_Object = MibScalar
jnxPppSummaryPppNetworkIpNcpNotPresent = _JnxPppSummaryPppNetworkIpNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 78),
    _JnxPppSummaryPppNetworkIpNcpNotPresent_Type()
)
jnxPppSummaryPppNetworkIpNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpNcpNotPresent.setStatus("current")
_JnxPppSummaryPppNetworkIpNcpNoResources_Type = Integer32
_JnxPppSummaryPppNetworkIpNcpNoResources_Object = MibScalar
jnxPppSummaryPppNetworkIpNcpNoResources = _JnxPppSummaryPppNetworkIpNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 79),
    _JnxPppSummaryPppNetworkIpNcpNoResources_Type()
)
jnxPppSummaryPppNetworkIpNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpNcpNoResources.setStatus("current")
_JnxPppSummaryPppNetworkIpv6NcpNotPresent_Type = Integer32
_JnxPppSummaryPppNetworkIpv6NcpNotPresent_Object = MibScalar
jnxPppSummaryPppNetworkIpv6NcpNotPresent = _JnxPppSummaryPppNetworkIpv6NcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 80),
    _JnxPppSummaryPppNetworkIpv6NcpNotPresent_Type()
)
jnxPppSummaryPppNetworkIpv6NcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpv6NcpNotPresent.setStatus("current")
_JnxPppSummaryPppNetworkIpv6NcpNoResources_Type = Integer32
_JnxPppSummaryPppNetworkIpv6NcpNoResources_Object = MibScalar
jnxPppSummaryPppNetworkIpv6NcpNoResources = _JnxPppSummaryPppNetworkIpv6NcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 81),
    _JnxPppSummaryPppNetworkIpv6NcpNoResources_Type()
)
jnxPppSummaryPppNetworkIpv6NcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkIpv6NcpNoResources.setStatus("current")
_JnxPppSummaryPppNetworkOsiNcpNotPresent_Type = Integer32
_JnxPppSummaryPppNetworkOsiNcpNotPresent_Object = MibScalar
jnxPppSummaryPppNetworkOsiNcpNotPresent = _JnxPppSummaryPppNetworkOsiNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 82),
    _JnxPppSummaryPppNetworkOsiNcpNotPresent_Type()
)
jnxPppSummaryPppNetworkOsiNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkOsiNcpNotPresent.setStatus("current")
_JnxPppSummaryPppNetworkOsiNcpNoResources_Type = Integer32
_JnxPppSummaryPppNetworkOsiNcpNoResources_Object = MibScalar
jnxPppSummaryPppNetworkOsiNcpNoResources = _JnxPppSummaryPppNetworkOsiNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 83),
    _JnxPppSummaryPppNetworkOsiNcpNoResources_Type()
)
jnxPppSummaryPppNetworkOsiNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkOsiNcpNoResources.setStatus("current")
_JnxPppSummaryPppNetworkMplsNcpOpened_Type = Integer32
_JnxPppSummaryPppNetworkMplsNcpOpened_Object = MibScalar
jnxPppSummaryPppNetworkMplsNcpOpened = _JnxPppSummaryPppNetworkMplsNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 84),
    _JnxPppSummaryPppNetworkMplsNcpOpened_Type()
)
jnxPppSummaryPppNetworkMplsNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkMplsNcpOpened.setStatus("current")
_JnxPppSummaryPppNetworkMplsNcpClosed_Type = Integer32
_JnxPppSummaryPppNetworkMplsNcpClosed_Object = MibScalar
jnxPppSummaryPppNetworkMplsNcpClosed = _JnxPppSummaryPppNetworkMplsNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 85),
    _JnxPppSummaryPppNetworkMplsNcpClosed_Type()
)
jnxPppSummaryPppNetworkMplsNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkMplsNcpClosed.setStatus("current")
_JnxPppSummaryPppNetworkMplsNcpNotPresent_Type = Integer32
_JnxPppSummaryPppNetworkMplsNcpNotPresent_Object = MibScalar
jnxPppSummaryPppNetworkMplsNcpNotPresent = _JnxPppSummaryPppNetworkMplsNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 86),
    _JnxPppSummaryPppNetworkMplsNcpNotPresent_Type()
)
jnxPppSummaryPppNetworkMplsNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkMplsNcpNotPresent.setStatus("current")
_JnxPppSummaryPppNetworkMplsNcpNoResources_Type = Integer32
_JnxPppSummaryPppNetworkMplsNcpNoResources_Object = MibScalar
jnxPppSummaryPppNetworkMplsNcpNoResources = _JnxPppSummaryPppNetworkMplsNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 7, 87),
    _JnxPppSummaryPppNetworkMplsNcpNoResources_Type()
)
jnxPppSummaryPppNetworkMplsNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppSummaryPppNetworkMplsNcpNoResources.setStatus("current")
_JnxPppIpv6_ObjectIdentity = ObjectIdentity
jnxPppIpv6 = _JnxPppIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8)
)
_JnxPppIpv6Table_Object = MibTable
jnxPppIpv6Table = _JnxPppIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 1)
)
if mibBuilder.loadTexts:
    jnxPppIpv6Table.setStatus("current")
_JnxPppIpv6Entry_Object = MibTableRow
jnxPppIpv6Entry = _JnxPppIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 1, 1)
)
jnxPppIpv6Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPppIpv6Entry.setStatus("current")


class _JnxPppIpv6ServiceStatus_Type(Integer32):
    """Custom type jnxPppIpv6ServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppIpv6ServiceStatus_Type.__name__ = "Integer32"
_JnxPppIpv6ServiceStatus_Object = MibTableColumn
jnxPppIpv6ServiceStatus = _JnxPppIpv6ServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 1, 1, 1),
    _JnxPppIpv6ServiceStatus_Type()
)
jnxPppIpv6ServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpv6ServiceStatus.setStatus("current")


class _JnxPppIpv6OperStatus_Type(Integer32):
    """Custom type jnxPppIpv6OperStatus based on Integer32"""
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


_JnxPppIpv6OperStatus_Type.__name__ = "Integer32"
_JnxPppIpv6OperStatus_Object = MibTableColumn
jnxPppIpv6OperStatus = _JnxPppIpv6OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 1, 1, 2),
    _JnxPppIpv6OperStatus_Type()
)
jnxPppIpv6OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpv6OperStatus.setStatus("current")


class _JnxPppIpv6TerminateReason_Type(Integer32):
    """Custom type jnxPppIpv6TerminateReason based on Integer32"""
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


_JnxPppIpv6TerminateReason_Type.__name__ = "Integer32"
_JnxPppIpv6TerminateReason_Object = MibTableColumn
jnxPppIpv6TerminateReason = _JnxPppIpv6TerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 1, 1, 3),
    _JnxPppIpv6TerminateReason_Type()
)
jnxPppIpv6TerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpv6TerminateReason.setStatus("current")


class _JnxPppIpv6TerminateNegFailOption_Type(Integer32):
    """Custom type jnxPppIpv6TerminateNegFailOption based on Integer32"""
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
        *(("localIpv6AddressIfIdentifier", 2),
          ("none", 0),
          ("other", 1),
          ("remoteIpv6AddressIfIdentifier", 3))
    )


_JnxPppIpv6TerminateNegFailOption_Type.__name__ = "Integer32"
_JnxPppIpv6TerminateNegFailOption_Object = MibTableColumn
jnxPppIpv6TerminateNegFailOption = _JnxPppIpv6TerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 1, 1, 4),
    _JnxPppIpv6TerminateNegFailOption_Type()
)
jnxPppIpv6TerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpv6TerminateNegFailOption.setStatus("current")
_JnxPppIpv6LocalIpv6AddressIfIdentifier_Type = Ipv6AddressIfIdentifier
_JnxPppIpv6LocalIpv6AddressIfIdentifier_Object = MibTableColumn
jnxPppIpv6LocalIpv6AddressIfIdentifier = _JnxPppIpv6LocalIpv6AddressIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 1, 1, 5),
    _JnxPppIpv6LocalIpv6AddressIfIdentifier_Type()
)
jnxPppIpv6LocalIpv6AddressIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpv6LocalIpv6AddressIfIdentifier.setStatus("current")
_JnxPppIpv6RemoteIpv6AddressIfIdentifier_Type = Ipv6AddressIfIdentifier
_JnxPppIpv6RemoteIpv6AddressIfIdentifier_Object = MibTableColumn
jnxPppIpv6RemoteIpv6AddressIfIdentifier = _JnxPppIpv6RemoteIpv6AddressIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 1, 1, 6),
    _JnxPppIpv6RemoteIpv6AddressIfIdentifier_Type()
)
jnxPppIpv6RemoteIpv6AddressIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpv6RemoteIpv6AddressIfIdentifier.setStatus("current")
_JnxPppIpv6NetworkStatusIpv6cpRenegoTerminates_Type = Counter32
_JnxPppIpv6NetworkStatusIpv6cpRenegoTerminates_Object = MibTableColumn
jnxPppIpv6NetworkStatusIpv6cpRenegoTerminates = _JnxPppIpv6NetworkStatusIpv6cpRenegoTerminates_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 1, 1, 7),
    _JnxPppIpv6NetworkStatusIpv6cpRenegoTerminates_Type()
)
jnxPppIpv6NetworkStatusIpv6cpRenegoTerminates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpv6NetworkStatusIpv6cpRenegoTerminates.setStatus("current")
_JnxPppIpv6ConfigTable_Object = MibTable
jnxPppIpv6ConfigTable = _JnxPppIpv6ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    jnxPppIpv6ConfigTable.setStatus("current")
_JnxPppIpv6ConfigEntry_Object = MibTableRow
jnxPppIpv6ConfigEntry = _JnxPppIpv6ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 2, 1)
)
jnxPppIpv6ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    jnxPppIpv6ConfigEntry.setStatus("current")


class _JnxPppIpv6ConfigAdminStatus_Type(Integer32):
    """Custom type jnxPppIpv6ConfigAdminStatus based on Integer32"""
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


_JnxPppIpv6ConfigAdminStatus_Type.__name__ = "Integer32"
_JnxPppIpv6ConfigAdminStatus_Object = MibTableColumn
jnxPppIpv6ConfigAdminStatus = _JnxPppIpv6ConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 2, 1, 1),
    _JnxPppIpv6ConfigAdminStatus_Type()
)
jnxPppIpv6ConfigAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpv6ConfigAdminStatus.setStatus("current")


class _JnxPppIpv6ConfigInitiateIpv6_Type(Integer32):
    """Custom type jnxPppIpv6ConfigInitiateIpv6 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppIpv6ConfigInitiateIpv6_Type.__name__ = "Integer32"
_JnxPppIpv6ConfigInitiateIpv6_Object = MibTableColumn
jnxPppIpv6ConfigInitiateIpv6 = _JnxPppIpv6ConfigInitiateIpv6_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 2, 1, 2),
    _JnxPppIpv6ConfigInitiateIpv6_Type()
)
jnxPppIpv6ConfigInitiateIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpv6ConfigInitiateIpv6.setStatus("current")


class _JnxPppIpv6ConfigMaxIpv6cpRenegotiation_Type(Integer32):
    """Custom type jnxPppIpv6ConfigMaxIpv6cpRenegotiation based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JnxPppIpv6ConfigMaxIpv6cpRenegotiation_Type.__name__ = "Integer32"
_JnxPppIpv6ConfigMaxIpv6cpRenegotiation_Object = MibTableColumn
jnxPppIpv6ConfigMaxIpv6cpRenegotiation = _JnxPppIpv6ConfigMaxIpv6cpRenegotiation_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 8, 2, 1, 3),
    _JnxPppIpv6ConfigMaxIpv6cpRenegotiation_Type()
)
jnxPppIpv6ConfigMaxIpv6cpRenegotiation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppIpv6ConfigMaxIpv6cpRenegotiation.setStatus("current")
_JnxPppGlobalConfig_ObjectIdentity = ObjectIdentity
jnxPppGlobalConfig = _JnxPppGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 9)
)


class _JnxPppPeerIpAddressOptional_Type(Integer32):
    """Custom type jnxPppPeerIpAddressOptional based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_JnxPppPeerIpAddressOptional_Type.__name__ = "Integer32"
_JnxPppPeerIpAddressOptional_Object = MibScalar
jnxPppPeerIpAddressOptional = _JnxPppPeerIpAddressOptional_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 68, 1, 1, 9, 1),
    _JnxPppPeerIpAddressOptional_Type()
)
jnxPppPeerIpAddressOptional.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxPppPeerIpAddressOptional.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JNX-PPP-MIB",
    **{"JnxPppAuthentication": JnxPppAuthentication,
       "JnxPppMlPppBundleName": JnxPppMlPppBundleName,
       "JnxPppAuthentication2": JnxPppAuthentication2,
       "JnxNibbleConfig": JnxNibbleConfig,
       "jnxPppMIB": jnxPppMIB,
       "jnxPPPObjects": jnxPPPObjects,
       "jnxPppLcp": jnxPppLcp,
       "jnxPppLinkStatusTable": jnxPppLinkStatusTable,
       "jnxPppLinkStatusEntry": jnxPppLinkStatusEntry,
       "jnxPppLinkStatusTerminateReason": jnxPppLinkStatusTerminateReason,
       "jnxPppLinkStatusTerminateNegFailOption": jnxPppLinkStatusTerminateNegFailOption,
       "jnxPppLinkStatusInKeepaliveRequests": jnxPppLinkStatusInKeepaliveRequests,
       "jnxPppLinkStatusOutKeepaliveRequests": jnxPppLinkStatusOutKeepaliveRequests,
       "jnxPppLinkStatusInKeepaliveReplies": jnxPppLinkStatusInKeepaliveReplies,
       "jnxPppLinkStatusOutKeepaliveReplies": jnxPppLinkStatusOutKeepaliveReplies,
       "jnxPppLinkStatusKeepaliveFailures": jnxPppLinkStatusKeepaliveFailures,
       "jnxPppLinkStatusLocalMagicNumber": jnxPppLinkStatusLocalMagicNumber,
       "jnxPppLinkStatusRemoteMagicNumber": jnxPppLinkStatusRemoteMagicNumber,
       "jnxPppLinkStatusLocalAuthentication": jnxPppLinkStatusLocalAuthentication,
       "jnxPppLinkStatusTunnelIfIndex": jnxPppLinkStatusTunnelIfIndex,
       "jnxPppLinkStatuslcpRenegoTerminates": jnxPppLinkStatuslcpRenegoTerminates,
       "jnxPppLinkStatusLocalMagicNumber1": jnxPppLinkStatusLocalMagicNumber1,
       "jnxPppLinkStatusRemoteMagicNumber1": jnxPppLinkStatusRemoteMagicNumber1,
       "jnxPppLinkConfigTable": jnxPppLinkConfigTable,
       "jnxPppLinkConfigEntry": jnxPppLinkConfigEntry,
       "jnxPppLinkConfigIfIndex": jnxPppLinkConfigIfIndex,
       "jnxPppLinkConfigRowStatus": jnxPppLinkConfigRowStatus,
       "jnxPppLinkConfigLowerIfIndex": jnxPppLinkConfigLowerIfIndex,
       "jnxPppLinkConfigKeepalive": jnxPppLinkConfigKeepalive,
       "jnxPppLinkConfigAuthentication": jnxPppLinkConfigAuthentication,
       "jnxPppLinkConfigMaxAuthenRetries": jnxPppLinkConfigMaxAuthenRetries,
       "jnxPppLinkConfigStandardIfIndex": jnxPppLinkConfigStandardIfIndex,
       "jnxPppLinkConfigChapMinChallengeLength": jnxPppLinkConfigChapMinChallengeLength,
       "jnxPppLinkConfigChapMaxChallengeLength": jnxPppLinkConfigChapMaxChallengeLength,
       "jnxPppLinkConfigPassiveMode": jnxPppLinkConfigPassiveMode,
       "jnxPppLinkConfigAuthenticatorLogicalSystem": jnxPppLinkConfigAuthenticatorLogicalSystem,
       "jnxPppLinkConfigAuthenticatorRoutingInstance": jnxPppLinkConfigAuthenticatorRoutingInstance,
       "jnxPppLinkConfigAaaProfile": jnxPppLinkConfigAaaProfile,
       "jnxPppLinkConfigAuthentication2": jnxPppLinkConfigAuthentication2,
       "jnxPppLinkConfigIgnoreMagicNumberMismatch": jnxPppLinkConfigIgnoreMagicNumberMismatch,
       "jnxPppLinkConfigMaxLcpRenegotiation": jnxPppLinkConfigMaxLcpRenegotiation,
       "jnxPppNextIfIndex": jnxPppNextIfIndex,
       "jnxPppSec": jnxPppSec,
       "jnxPppIp": jnxPppIp,
       "jnxPppIpTable": jnxPppIpTable,
       "jnxPppIpEntry": jnxPppIpEntry,
       "jnxPppIpServiceStatus": jnxPppIpServiceStatus,
       "jnxPppIpTerminateReason": jnxPppIpTerminateReason,
       "jnxPppIpTerminateNegFailOption": jnxPppIpTerminateNegFailOption,
       "jnxPppIpLocalIpAddress": jnxPppIpLocalIpAddress,
       "jnxPppIpRemoteIpAddress": jnxPppIpRemoteIpAddress,
       "jnxPppIpRemotePrimaryDnsAddress": jnxPppIpRemotePrimaryDnsAddress,
       "jnxPppIpRemoteSecondaryDnsAddress": jnxPppIpRemoteSecondaryDnsAddress,
       "jnxPppIpRemotePrimaryWinsAddress": jnxPppIpRemotePrimaryWinsAddress,
       "jnxPppIpRemoteSecondaryWinsAddress": jnxPppIpRemoteSecondaryWinsAddress,
       "jnxPppIpNetworkStatusIpcpRenegoTerminates": jnxPppIpNetworkStatusIpcpRenegoTerminates,
       "jnxPppIpConfigTable": jnxPppIpConfigTable,
       "jnxPppIpConfigEntry": jnxPppIpConfigEntry,
       "jnxPppIpConfigPeerDnsPriority": jnxPppIpConfigPeerDnsPriority,
       "jnxPppIpConfigPeerWinsPriority": jnxPppIpConfigPeerWinsPriority,
       "jnxPppIpConfigIpcpNetmask": jnxPppIpConfigIpcpNetmask,
       "jnxPppIpConfigInitiateIp": jnxPppIpConfigInitiateIp,
       "jnxPppIpConfigMaxIpcpRenegotiation": jnxPppIpConfigMaxIpcpRenegotiation,
       "jnxPppIpConfigPromptIpcpDnsOption": jnxPppIpConfigPromptIpcpDnsOption,
       "jnxPppIpConfigIpcpLockout": jnxPppIpConfigIpcpLockout,
       "jnxPppOsi": jnxPppOsi,
       "jnxPppOsiTable": jnxPppOsiTable,
       "jnxPppOsiEntry": jnxPppOsiEntry,
       "jnxPppOsiServiceStatus": jnxPppOsiServiceStatus,
       "jnxPppOsiOperStatus": jnxPppOsiOperStatus,
       "jnxPppOsiTerminateReason": jnxPppOsiTerminateReason,
       "jnxPppOsiTerminateNegFailOption": jnxPppOsiTerminateNegFailOption,
       "jnxPppOsiLocalAlignNpdu": jnxPppOsiLocalAlignNpdu,
       "jnxPppOsiRemoteAlignNpdu": jnxPppOsiRemoteAlignNpdu,
       "jnxPppOsiConfigTable": jnxPppOsiConfigTable,
       "jnxPppOsiConfigEntry": jnxPppOsiConfigEntry,
       "jnxPppOsiConfigAdminStatus": jnxPppOsiConfigAdminStatus,
       "jnxPppSession": jnxPppSession,
       "jnxPppSessionTable": jnxPppSessionTable,
       "jnxPppSessionEntry": jnxPppSessionEntry,
       "jnxPppSessionGrant": jnxPppSessionGrant,
       "jnxPppSessionTerminateReason": jnxPppSessionTerminateReason,
       "jnxPppSessionStartTime": jnxPppSessionStartTime,
       "jnxPppSessionInOctets": jnxPppSessionInOctets,
       "jnxPppSessionOutOctets": jnxPppSessionOutOctets,
       "jnxPppSessionInPackets": jnxPppSessionInPackets,
       "jnxPppSessionOutPackets": jnxPppSessionOutPackets,
       "jnxPppSessionSessionTimeout": jnxPppSessionSessionTimeout,
       "jnxPppSessionInactivityTimeout": jnxPppSessionInactivityTimeout,
       "jnxPppSessionAccountingInterval": jnxPppSessionAccountingInterval,
       "jnxPppSessionRemoteIpAddress": jnxPppSessionRemoteIpAddress,
       "jnxPppSessionRemotePrimaryDnsAddress": jnxPppSessionRemotePrimaryDnsAddress,
       "jnxPppSessionRemoteSecondaryDnsAddress": jnxPppSessionRemoteSecondaryDnsAddress,
       "jnxPppSessionRemotePrimaryWinsAddress": jnxPppSessionRemotePrimaryWinsAddress,
       "jnxPppSessionRemoteSecondaryWinsAddress": jnxPppSessionRemoteSecondaryWinsAddress,
       "jnxPppSessionRemoteIpv6AddressIfIdentifier": jnxPppSessionRemoteIpv6AddressIfIdentifier,
       "jnxPppSessionInhibitIp": jnxPppSessionInhibitIp,
       "jnxPppSessionInhibitIpv6": jnxPppSessionInhibitIpv6,
       "jnxPppSessionInOctets64": jnxPppSessionInOctets64,
       "jnxPppSessionOutOctets64": jnxPppSessionOutOctets64,
       "jnxPppSessionInPackets64": jnxPppSessionInPackets64,
       "jnxPppSessionOutPackets64": jnxPppSessionOutPackets64,
       "jnxPppMlPpp": jnxPppMlPpp,
       "jnxPppMlPppBundleTable": jnxPppMlPppBundleTable,
       "jnxPppMlPppBundleEntry": jnxPppMlPppBundleEntry,
       "jnxPppMlPppBundleName": jnxPppMlPppBundleName,
       "jnxPppMlPppBundleRowStatus": jnxPppMlPppBundleRowStatus,
       "jnxPppMlPppBundleNetworkIfIndex": jnxPppMlPppBundleNetworkIfIndex,
       "jnxPppMlPppNextLinkIfIndex": jnxPppMlPppNextLinkIfIndex,
       "jnxPppMlPppLinkConfigTable": jnxPppMlPppLinkConfigTable,
       "jnxPppMlPppLinkConfigEntry": jnxPppMlPppLinkConfigEntry,
       "jnxPppMlPppLinkConfigIfIndex": jnxPppMlPppLinkConfigIfIndex,
       "jnxPppMlPppLinkConfigLowerIfIndex": jnxPppMlPppLinkConfigLowerIfIndex,
       "jnxPppMlPppLinkConfigKeepalive": jnxPppMlPppLinkConfigKeepalive,
       "jnxPppMlPppLinkConfigAuthentication": jnxPppMlPppLinkConfigAuthentication,
       "jnxPppMlPppLinkConfigMaxAuthenRetries": jnxPppMlPppLinkConfigMaxAuthenRetries,
       "jnxPppMlPppLinkConfigRowStatus": jnxPppMlPppLinkConfigRowStatus,
       "jnxPppMlPppLinkConfigAaaProfile": jnxPppMlPppLinkConfigAaaProfile,
       "jnxPppMlPppLinkConfigChapMinChallengeLength": jnxPppMlPppLinkConfigChapMinChallengeLength,
       "jnxPppMlPppLinkConfigChapMaxChallengeLength": jnxPppMlPppLinkConfigChapMaxChallengeLength,
       "jnxPppMlPppLinkConfigPassiveMode": jnxPppMlPppLinkConfigPassiveMode,
       "jnxPppMlPppLinkConfigAuthenticatorLogicalSystem": jnxPppMlPppLinkConfigAuthenticatorLogicalSystem,
       "jnxPppMlPppLinkConfigAuthenticatorRoutingInstance": jnxPppMlPppLinkConfigAuthenticatorRoutingInstance,
       "jnxPppMlPppLinkConfigFragmentation": jnxPppMlPppLinkConfigFragmentation,
       "jnxPppMlPppLinkConfigReassembly": jnxPppMlPppLinkConfigReassembly,
       "jnxPppMlPppLinkConfigMaxReceiveReconstructedUnit": jnxPppMlPppLinkConfigMaxReceiveReconstructedUnit,
       "jnxPppMlPppLinkConfigFragmentSize": jnxPppMlPppLinkConfigFragmentSize,
       "jnxPppMlPppLinkConfigHashLinkSelection": jnxPppMlPppLinkConfigHashLinkSelection,
       "jnxPppMlPppLinkConfigAuthentication2": jnxPppMlPppLinkConfigAuthentication2,
       "jnxPppMlPppLinkConfigIgnoreMagicNumberMismatch": jnxPppMlPppLinkConfigIgnoreMagicNumberMismatch,
       "jnxPppMlPppLinkConfigMultilinkMulticlass": jnxPppMlPppLinkConfigMultilinkMulticlass,
       "jnxPppMlPppLinkConfigMultilinkMaxMultiClasses": jnxPppMlPppLinkConfigMultilinkMaxMultiClasses,
       "jnxPppMlPppNextNetworkIfIndex": jnxPppMlPppNextNetworkIfIndex,
       "jnxPppMlPppNetworkConfigTable": jnxPppMlPppNetworkConfigTable,
       "jnxPppMlPppNetworkConfigEntry": jnxPppMlPppNetworkConfigEntry,
       "jnxPppMlPppNetworkConfigIfIndex": jnxPppMlPppNetworkConfigIfIndex,
       "jnxPppMlPppNetworkConfigLowerIfIndex": jnxPppMlPppNetworkConfigLowerIfIndex,
       "jnxPppMlPppNetworkBundleName": jnxPppMlPppNetworkBundleName,
       "jnxPppMlPppNetworkRowStatus": jnxPppMlPppNetworkRowStatus,
       "jnxPppMlPppLinkBindTable": jnxPppMlPppLinkBindTable,
       "jnxPppMlPppLinkBindEntry": jnxPppMlPppLinkBindEntry,
       "jnxPppMlPppBindNetworkIfIndex": jnxPppMlPppBindNetworkIfIndex,
       "jnxPppMlPppBindLinkIfIndex": jnxPppMlPppBindLinkIfIndex,
       "jnxPppMlPppBindRowStatus": jnxPppMlPppBindRowStatus,
       "jnxPppSummary": jnxPppSummary,
       "jnxPppSummaryPppInterfaceCount": jnxPppSummaryPppInterfaceCount,
       "jnxPppSummaryPppIpNCPs": jnxPppSummaryPppIpNCPs,
       "jnxPppSummaryPppOsiNCPs": jnxPppSummaryPppOsiNCPs,
       "jnxPppSummaryPppIfAdminUp": jnxPppSummaryPppIfAdminUp,
       "jnxPppSummaryPppIfAdminDown": jnxPppSummaryPppIfAdminDown,
       "jnxPppSummaryPppIfOperUp": jnxPppSummaryPppIfOperUp,
       "jnxPppSummaryPppIfOperDown": jnxPppSummaryPppIfOperDown,
       "jnxPppSummaryPppIfOperDormant": jnxPppSummaryPppIfOperDormant,
       "jnxPppSummaryPppIfNotPresent": jnxPppSummaryPppIfNotPresent,
       "jnxPppSummaryPppIfLowerLayerDown": jnxPppSummaryPppIfLowerLayerDown,
       "jnxPppSummaryPppIpNcpOpened": jnxPppSummaryPppIpNcpOpened,
       "jnxPppSummaryPppIpNcpClosed": jnxPppSummaryPppIpNcpClosed,
       "jnxPppSummaryPppOsiNcpOpened": jnxPppSummaryPppOsiNcpOpened,
       "jnxPppSummaryPppOsiNcpClosed": jnxPppSummaryPppOsiNcpClosed,
       "jnxPppSummaryPppIfLastChangeTime": jnxPppSummaryPppIfLastChangeTime,
       "jnxPppSummaryPppLinkInterfaceCount": jnxPppSummaryPppLinkInterfaceCount,
       "jnxPppSummaryPppLinkIfAdminUp": jnxPppSummaryPppLinkIfAdminUp,
       "jnxPppSummaryPppLinkIfAdminDown": jnxPppSummaryPppLinkIfAdminDown,
       "jnxPppSummaryPppLinkIfOperUp": jnxPppSummaryPppLinkIfOperUp,
       "jnxPppSummaryPppLinkIfOperDown": jnxPppSummaryPppLinkIfOperDown,
       "jnxPppSummaryPppLinkIfOperDormant": jnxPppSummaryPppLinkIfOperDormant,
       "jnxPppSummaryPppLinkIfNotPresent": jnxPppSummaryPppLinkIfNotPresent,
       "jnxPppSummaryPppLinkIfLowerLayerDown": jnxPppSummaryPppLinkIfLowerLayerDown,
       "jnxPppSummaryPppLinkIfLastChangeTime": jnxPppSummaryPppLinkIfLastChangeTime,
       "jnxPppSummaryPppNetworkInterfaceCount": jnxPppSummaryPppNetworkInterfaceCount,
       "jnxPppSummaryPppNetworkIpNCPs": jnxPppSummaryPppNetworkIpNCPs,
       "jnxPppSummaryPppNetworkOsiNCPs": jnxPppSummaryPppNetworkOsiNCPs,
       "jnxPppSummaryPppNetworkIfAdminUp": jnxPppSummaryPppNetworkIfAdminUp,
       "jnxPppSummaryPppNetworkIfAdminDown": jnxPppSummaryPppNetworkIfAdminDown,
       "jnxPppSummaryPppNetworkIfOperUp": jnxPppSummaryPppNetworkIfOperUp,
       "jnxPppSummaryPppNetworkIfOperDown": jnxPppSummaryPppNetworkIfOperDown,
       "jnxPppSummaryPppNetworkIfOperDormant": jnxPppSummaryPppNetworkIfOperDormant,
       "jnxPppSummaryPppNetworkIfNotPresent": jnxPppSummaryPppNetworkIfNotPresent,
       "jnxPppSummaryPppNetworkIfLowerLayerDown": jnxPppSummaryPppNetworkIfLowerLayerDown,
       "jnxPppSummaryPppNetworkIpNcpOpened": jnxPppSummaryPppNetworkIpNcpOpened,
       "jnxPppSummaryPppNetworkIpNcpClosed": jnxPppSummaryPppNetworkIpNcpClosed,
       "jnxPppSummaryPppNetworkOsiNcpOpened": jnxPppSummaryPppNetworkOsiNcpOpened,
       "jnxPppSummaryPppNetworkOsiNcpClosed": jnxPppSummaryPppNetworkOsiNcpClosed,
       "jnxPppSummaryPppNetworkIfLastChangeTime": jnxPppSummaryPppNetworkIfLastChangeTime,
       "jnxPppSummaryPppIpv6NCPs": jnxPppSummaryPppIpv6NCPs,
       "jnxPppSummaryPppIpv6NcpOpened": jnxPppSummaryPppIpv6NcpOpened,
       "jnxPppSummaryPppIpv6NcpClosed": jnxPppSummaryPppIpv6NcpClosed,
       "jnxPppSummaryPppNetworkIpv6NCPs": jnxPppSummaryPppNetworkIpv6NCPs,
       "jnxPppSummaryPppNetworkIpv6NcpOpened": jnxPppSummaryPppNetworkIpv6NcpOpened,
       "jnxPppSummaryPppNetworkIpv6NcpClosed": jnxPppSummaryPppNetworkIpv6NcpClosed,
       "jnxPppSummaryPppStaticInterfaceCount": jnxPppSummaryPppStaticInterfaceCount,
       "jnxPppSummaryPppMplsNCPs": jnxPppSummaryPppMplsNCPs,
       "jnxPppSummaryPppIpAdminOpen": jnxPppSummaryPppIpAdminOpen,
       "jnxPppSummaryPppIpAdminClose": jnxPppSummaryPppIpAdminClose,
       "jnxPppSummaryPppIpv6AdminOpen": jnxPppSummaryPppIpv6AdminOpen,
       "jnxPppSummaryPppIpv6AdminClose": jnxPppSummaryPppIpv6AdminClose,
       "jnxPppSummaryPppOsiAdminOpen": jnxPppSummaryPppOsiAdminOpen,
       "jnxPppSummaryPppOsiAdminClose": jnxPppSummaryPppOsiAdminClose,
       "jnxPppSummaryPppMplsAdminOpen": jnxPppSummaryPppMplsAdminOpen,
       "jnxPppSummaryPppMplsAdminClose": jnxPppSummaryPppMplsAdminClose,
       "jnxPppSummaryPppIpNcpNotPresent": jnxPppSummaryPppIpNcpNotPresent,
       "jnxPppSummaryPppIpNcpNoResources": jnxPppSummaryPppIpNcpNoResources,
       "jnxPppSummaryPppIpv6NcpNotPresent": jnxPppSummaryPppIpv6NcpNotPresent,
       "jnxPppSummaryPppIpv6NcpNoResources": jnxPppSummaryPppIpv6NcpNoResources,
       "jnxPppSummaryPppOsiNcpNotPresent": jnxPppSummaryPppOsiNcpNotPresent,
       "jnxPppSummaryPppOsiNcpNoResources": jnxPppSummaryPppOsiNcpNoResources,
       "jnxPppSummaryPppMplsNcpOpened": jnxPppSummaryPppMplsNcpOpened,
       "jnxPppSummaryPppMplsNcpClosed": jnxPppSummaryPppMplsNcpClosed,
       "jnxPppSummaryPppMplsNcpNotPresent": jnxPppSummaryPppMplsNcpNotPresent,
       "jnxPppSummaryPppMplsNcpNoResources": jnxPppSummaryPppMplsNcpNoResources,
       "jnxPppSummaryPppLinkStaticInterfaceCount": jnxPppSummaryPppLinkStaticInterfaceCount,
       "jnxPppSummaryPppNetworkStaticInterfaceCount": jnxPppSummaryPppNetworkStaticInterfaceCount,
       "jnxPppSummaryPppNetworkMplsNCPs": jnxPppSummaryPppNetworkMplsNCPs,
       "jnxPppSummaryPppNetworkIpAdminOpen": jnxPppSummaryPppNetworkIpAdminOpen,
       "jnxPppSummaryPppNetworkIpAdminClose": jnxPppSummaryPppNetworkIpAdminClose,
       "jnxPppSummaryPppNetworkIpv6AdminOpen": jnxPppSummaryPppNetworkIpv6AdminOpen,
       "jnxPppSummaryPppNetworkIpv6AdminClose": jnxPppSummaryPppNetworkIpv6AdminClose,
       "jnxPppSummaryPppNetworkOsiAdminOpen": jnxPppSummaryPppNetworkOsiAdminOpen,
       "jnxPppSummaryPppNetworkOsiAdminClose": jnxPppSummaryPppNetworkOsiAdminClose,
       "jnxPppSummaryPppNetworkMplsAdminOpen": jnxPppSummaryPppNetworkMplsAdminOpen,
       "jnxPppSummaryPppNetworkMplsAdminClose": jnxPppSummaryPppNetworkMplsAdminClose,
       "jnxPppSummaryPppNetworkIpNcpNotPresent": jnxPppSummaryPppNetworkIpNcpNotPresent,
       "jnxPppSummaryPppNetworkIpNcpNoResources": jnxPppSummaryPppNetworkIpNcpNoResources,
       "jnxPppSummaryPppNetworkIpv6NcpNotPresent": jnxPppSummaryPppNetworkIpv6NcpNotPresent,
       "jnxPppSummaryPppNetworkIpv6NcpNoResources": jnxPppSummaryPppNetworkIpv6NcpNoResources,
       "jnxPppSummaryPppNetworkOsiNcpNotPresent": jnxPppSummaryPppNetworkOsiNcpNotPresent,
       "jnxPppSummaryPppNetworkOsiNcpNoResources": jnxPppSummaryPppNetworkOsiNcpNoResources,
       "jnxPppSummaryPppNetworkMplsNcpOpened": jnxPppSummaryPppNetworkMplsNcpOpened,
       "jnxPppSummaryPppNetworkMplsNcpClosed": jnxPppSummaryPppNetworkMplsNcpClosed,
       "jnxPppSummaryPppNetworkMplsNcpNotPresent": jnxPppSummaryPppNetworkMplsNcpNotPresent,
       "jnxPppSummaryPppNetworkMplsNcpNoResources": jnxPppSummaryPppNetworkMplsNcpNoResources,
       "jnxPppIpv6": jnxPppIpv6,
       "jnxPppIpv6Table": jnxPppIpv6Table,
       "jnxPppIpv6Entry": jnxPppIpv6Entry,
       "jnxPppIpv6ServiceStatus": jnxPppIpv6ServiceStatus,
       "jnxPppIpv6OperStatus": jnxPppIpv6OperStatus,
       "jnxPppIpv6TerminateReason": jnxPppIpv6TerminateReason,
       "jnxPppIpv6TerminateNegFailOption": jnxPppIpv6TerminateNegFailOption,
       "jnxPppIpv6LocalIpv6AddressIfIdentifier": jnxPppIpv6LocalIpv6AddressIfIdentifier,
       "jnxPppIpv6RemoteIpv6AddressIfIdentifier": jnxPppIpv6RemoteIpv6AddressIfIdentifier,
       "jnxPppIpv6NetworkStatusIpv6cpRenegoTerminates": jnxPppIpv6NetworkStatusIpv6cpRenegoTerminates,
       "jnxPppIpv6ConfigTable": jnxPppIpv6ConfigTable,
       "jnxPppIpv6ConfigEntry": jnxPppIpv6ConfigEntry,
       "jnxPppIpv6ConfigAdminStatus": jnxPppIpv6ConfigAdminStatus,
       "jnxPppIpv6ConfigInitiateIpv6": jnxPppIpv6ConfigInitiateIpv6,
       "jnxPppIpv6ConfigMaxIpv6cpRenegotiation": jnxPppIpv6ConfigMaxIpv6cpRenegotiation,
       "jnxPppGlobalConfig": jnxPppGlobalConfig,
       "jnxPppPeerIpAddressOptional": jnxPppPeerIpAddressOptional}
)
