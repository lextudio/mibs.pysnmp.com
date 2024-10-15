# SNMP MIB module (Juniper-PPP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-PPP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:15:57 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniEnable,
 JuniName,
 JuniNextIfIndex,
 JuniNibbleConfig) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniEnable",
    "JuniName",
    "JuniNextIfIndex",
    "JuniNibbleConfig")

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

juniPppMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11)
)
juniPppMIB.setRevisions(
        ("2010-02-09 11:06",
         "2009-09-18 07:24",
         "2009-08-10 14:23",
         "2008-08-27 11:20",
         "2007-07-12 12:15",
         "2005-10-19 16:26",
         "2004-10-05 22:17",
         "2004-10-01 21:41",
         "2004-08-25 12:12",
         "2004-08-25 12:12",
         "2004-08-25 12:12",
         "2004-08-25 12:12",
         "2002-08-30 20:36",
         "2002-05-09 20:31",
         "2001-12-12 21:47",
         "2000-10-09 16:10",
         "2000-02-15 12:00",
         "1999-07-01 00:00",
         "1998-11-13 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniPppAuthentication(Integer32, TextualConvention):
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



class JuniPppAuthentication2(Integer32, TextualConvention):
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



class JuniPppMlPppBundleName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class JuniPppMlPppMulticlassTcName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_JuniPppObjects_ObjectIdentity = ObjectIdentity
juniPppObjects = _JuniPppObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1)
)
_JuniPppLcp_ObjectIdentity = ObjectIdentity
juniPppLcp = _JuniPppLcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1)
)
_JuniPppLinkStatusTable_Object = MibTable
juniPppLinkStatusTable = _JuniPppLinkStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniPppLinkStatusTable.setStatus("current")
_JuniPppLinkStatusEntry_Object = MibTableRow
juniPppLinkStatusEntry = _JuniPppLinkStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1)
)
juniPppLinkStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniPppLinkStatusEntry.setStatus("current")


class _JuniPppLinkStatusTerminateReason_Type(Integer32):
    """Custom type juniPppLinkStatusTerminateReason based on Integer32"""
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


_JuniPppLinkStatusTerminateReason_Type.__name__ = "Integer32"
_JuniPppLinkStatusTerminateReason_Object = MibTableColumn
juniPppLinkStatusTerminateReason = _JuniPppLinkStatusTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 1),
    _JuniPppLinkStatusTerminateReason_Type()
)
juniPppLinkStatusTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusTerminateReason.setStatus("current")


class _JuniPppLinkStatusTerminateNegFailOption_Type(Integer32):
    """Custom type juniPppLinkStatusTerminateNegFailOption based on Integer32"""
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


_JuniPppLinkStatusTerminateNegFailOption_Type.__name__ = "Integer32"
_JuniPppLinkStatusTerminateNegFailOption_Object = MibTableColumn
juniPppLinkStatusTerminateNegFailOption = _JuniPppLinkStatusTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 2),
    _JuniPppLinkStatusTerminateNegFailOption_Type()
)
juniPppLinkStatusTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusTerminateNegFailOption.setStatus("current")
_JuniPppLinkStatusInKeepaliveRequests_Type = Counter32
_JuniPppLinkStatusInKeepaliveRequests_Object = MibTableColumn
juniPppLinkStatusInKeepaliveRequests = _JuniPppLinkStatusInKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 3),
    _JuniPppLinkStatusInKeepaliveRequests_Type()
)
juniPppLinkStatusInKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusInKeepaliveRequests.setStatus("current")
_JuniPppLinkStatusOutKeepaliveRequests_Type = Counter32
_JuniPppLinkStatusOutKeepaliveRequests_Object = MibTableColumn
juniPppLinkStatusOutKeepaliveRequests = _JuniPppLinkStatusOutKeepaliveRequests_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 4),
    _JuniPppLinkStatusOutKeepaliveRequests_Type()
)
juniPppLinkStatusOutKeepaliveRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusOutKeepaliveRequests.setStatus("current")
_JuniPppLinkStatusInKeepaliveReplies_Type = Counter32
_JuniPppLinkStatusInKeepaliveReplies_Object = MibTableColumn
juniPppLinkStatusInKeepaliveReplies = _JuniPppLinkStatusInKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 5),
    _JuniPppLinkStatusInKeepaliveReplies_Type()
)
juniPppLinkStatusInKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusInKeepaliveReplies.setStatus("current")
_JuniPppLinkStatusOutKeepaliveReplies_Type = Counter32
_JuniPppLinkStatusOutKeepaliveReplies_Object = MibTableColumn
juniPppLinkStatusOutKeepaliveReplies = _JuniPppLinkStatusOutKeepaliveReplies_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 6),
    _JuniPppLinkStatusOutKeepaliveReplies_Type()
)
juniPppLinkStatusOutKeepaliveReplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusOutKeepaliveReplies.setStatus("current")
_JuniPppLinkStatusKeepaliveFailures_Type = Counter32
_JuniPppLinkStatusKeepaliveFailures_Object = MibTableColumn
juniPppLinkStatusKeepaliveFailures = _JuniPppLinkStatusKeepaliveFailures_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 7),
    _JuniPppLinkStatusKeepaliveFailures_Type()
)
juniPppLinkStatusKeepaliveFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusKeepaliveFailures.setStatus("current")
_JuniPppLinkStatusLocalMagicNumber_Type = Integer32
_JuniPppLinkStatusLocalMagicNumber_Object = MibTableColumn
juniPppLinkStatusLocalMagicNumber = _JuniPppLinkStatusLocalMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 8),
    _JuniPppLinkStatusLocalMagicNumber_Type()
)
juniPppLinkStatusLocalMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusLocalMagicNumber.setStatus("current")
_JuniPppLinkStatusRemoteMagicNumber_Type = Integer32
_JuniPppLinkStatusRemoteMagicNumber_Object = MibTableColumn
juniPppLinkStatusRemoteMagicNumber = _JuniPppLinkStatusRemoteMagicNumber_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 9),
    _JuniPppLinkStatusRemoteMagicNumber_Type()
)
juniPppLinkStatusRemoteMagicNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusRemoteMagicNumber.setStatus("current")
_JuniPppLinkStatusLocalAuthentication_Type = JuniPppAuthentication2
_JuniPppLinkStatusLocalAuthentication_Object = MibTableColumn
juniPppLinkStatusLocalAuthentication = _JuniPppLinkStatusLocalAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 10),
    _JuniPppLinkStatusLocalAuthentication_Type()
)
juniPppLinkStatusLocalAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusLocalAuthentication.setStatus("current")
_JuniPppLinkStatusTunnelIfIndex_Type = InterfaceIndexOrZero
_JuniPppLinkStatusTunnelIfIndex_Object = MibTableColumn
juniPppLinkStatusTunnelIfIndex = _JuniPppLinkStatusTunnelIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 11),
    _JuniPppLinkStatusTunnelIfIndex_Type()
)
juniPppLinkStatusTunnelIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatusTunnelIfIndex.setStatus("current")
_JuniPppLinkStatuslcpRenegoTerminates_Type = Counter32
_JuniPppLinkStatuslcpRenegoTerminates_Object = MibTableColumn
juniPppLinkStatuslcpRenegoTerminates = _JuniPppLinkStatuslcpRenegoTerminates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 1, 1, 12),
    _JuniPppLinkStatuslcpRenegoTerminates_Type()
)
juniPppLinkStatuslcpRenegoTerminates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkStatuslcpRenegoTerminates.setStatus("current")
_JuniPppLinkConfigTable_Object = MibTable
juniPppLinkConfigTable = _JuniPppLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniPppLinkConfigTable.setStatus("current")
_JuniPppLinkConfigEntry_Object = MibTableRow
juniPppLinkConfigEntry = _JuniPppLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1)
)
juniPppLinkConfigEntry.setIndexNames(
    (0, "Juniper-PPP-MIB", "juniPppLinkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    juniPppLinkConfigEntry.setStatus("current")
_JuniPppLinkConfigIfIndex_Type = InterfaceIndex
_JuniPppLinkConfigIfIndex_Object = MibTableColumn
juniPppLinkConfigIfIndex = _JuniPppLinkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 1),
    _JuniPppLinkConfigIfIndex_Type()
)
juniPppLinkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppLinkConfigIfIndex.setStatus("current")
_JuniPppLinkConfigRowStatus_Type = RowStatus
_JuniPppLinkConfigRowStatus_Object = MibTableColumn
juniPppLinkConfigRowStatus = _JuniPppLinkConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 2),
    _JuniPppLinkConfigRowStatus_Type()
)
juniPppLinkConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigRowStatus.setStatus("current")
_JuniPppLinkConfigLowerIfIndex_Type = InterfaceIndexOrZero
_JuniPppLinkConfigLowerIfIndex_Object = MibTableColumn
juniPppLinkConfigLowerIfIndex = _JuniPppLinkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 3),
    _JuniPppLinkConfigLowerIfIndex_Type()
)
juniPppLinkConfigLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigLowerIfIndex.setStatus("current")


class _JuniPppLinkConfigKeepalive_Type(Integer32):
    """Custom type juniPppLinkConfigKeepalive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64800),
    )


_JuniPppLinkConfigKeepalive_Type.__name__ = "Integer32"
_JuniPppLinkConfigKeepalive_Object = MibTableColumn
juniPppLinkConfigKeepalive = _JuniPppLinkConfigKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 4),
    _JuniPppLinkConfigKeepalive_Type()
)
juniPppLinkConfigKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    juniPppLinkConfigKeepalive.setUnits("seconds")


class _JuniPppLinkConfigAuthentication_Type(JuniPppAuthentication):
    """Custom type juniPppLinkConfigAuthentication based on JuniPppAuthentication"""


_JuniPppLinkConfigAuthentication_Object = MibTableColumn
juniPppLinkConfigAuthentication = _JuniPppLinkConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 5),
    _JuniPppLinkConfigAuthentication_Type()
)
juniPppLinkConfigAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigAuthentication.setStatus("deprecated")


class _JuniPppLinkConfigMaxAuthenRetries_Type(Integer32):
    """Custom type juniPppLinkConfigMaxAuthenRetries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_JuniPppLinkConfigMaxAuthenRetries_Type.__name__ = "Integer32"
_JuniPppLinkConfigMaxAuthenRetries_Object = MibTableColumn
juniPppLinkConfigMaxAuthenRetries = _JuniPppLinkConfigMaxAuthenRetries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 6),
    _JuniPppLinkConfigMaxAuthenRetries_Type()
)
juniPppLinkConfigMaxAuthenRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigMaxAuthenRetries.setStatus("current")
_JuniPppLinkConfigStandardIfIndex_Type = InterfaceIndex
_JuniPppLinkConfigStandardIfIndex_Object = MibTableColumn
juniPppLinkConfigStandardIfIndex = _JuniPppLinkConfigStandardIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 7),
    _JuniPppLinkConfigStandardIfIndex_Type()
)
juniPppLinkConfigStandardIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppLinkConfigStandardIfIndex.setStatus("current")


class _JuniPppLinkConfigChapMinChallengeLength_Type(Integer32):
    """Custom type juniPppLinkConfigChapMinChallengeLength based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_JuniPppLinkConfigChapMinChallengeLength_Type.__name__ = "Integer32"
_JuniPppLinkConfigChapMinChallengeLength_Object = MibTableColumn
juniPppLinkConfigChapMinChallengeLength = _JuniPppLinkConfigChapMinChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 8),
    _JuniPppLinkConfigChapMinChallengeLength_Type()
)
juniPppLinkConfigChapMinChallengeLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigChapMinChallengeLength.setStatus("current")


class _JuniPppLinkConfigChapMaxChallengeLength_Type(Integer32):
    """Custom type juniPppLinkConfigChapMaxChallengeLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_JuniPppLinkConfigChapMaxChallengeLength_Type.__name__ = "Integer32"
_JuniPppLinkConfigChapMaxChallengeLength_Object = MibTableColumn
juniPppLinkConfigChapMaxChallengeLength = _JuniPppLinkConfigChapMaxChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 9),
    _JuniPppLinkConfigChapMaxChallengeLength_Type()
)
juniPppLinkConfigChapMaxChallengeLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigChapMaxChallengeLength.setStatus("current")


class _JuniPppLinkConfigPassiveMode_Type(JuniEnable):
    """Custom type juniPppLinkConfigPassiveMode based on JuniEnable"""


_JuniPppLinkConfigPassiveMode_Object = MibTableColumn
juniPppLinkConfigPassiveMode = _JuniPppLinkConfigPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 10),
    _JuniPppLinkConfigPassiveMode_Type()
)
juniPppLinkConfigPassiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigPassiveMode.setStatus("current")
_JuniPppLinkConfigAuthenticatorVirtualRouter_Type = JuniName
_JuniPppLinkConfigAuthenticatorVirtualRouter_Object = MibTableColumn
juniPppLinkConfigAuthenticatorVirtualRouter = _JuniPppLinkConfigAuthenticatorVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 11),
    _JuniPppLinkConfigAuthenticatorVirtualRouter_Type()
)
juniPppLinkConfigAuthenticatorVirtualRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigAuthenticatorVirtualRouter.setStatus("current")
_JuniPppLinkConfigAaaProfile_Type = JuniName
_JuniPppLinkConfigAaaProfile_Object = MibTableColumn
juniPppLinkConfigAaaProfile = _JuniPppLinkConfigAaaProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 12),
    _JuniPppLinkConfigAaaProfile_Type()
)
juniPppLinkConfigAaaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigAaaProfile.setStatus("current")


class _JuniPppLinkConfigAuthentication2_Type(JuniNibbleConfig):
    """Custom type juniPppLinkConfigAuthentication2 based on JuniNibbleConfig"""
    defaultValue = 0


_JuniPppLinkConfigAuthentication2_Object = MibTableColumn
juniPppLinkConfigAuthentication2 = _JuniPppLinkConfigAuthentication2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 13),
    _JuniPppLinkConfigAuthentication2_Type()
)
juniPppLinkConfigAuthentication2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigAuthentication2.setStatus("current")


class _JuniPppLinkConfigIgnoreMagicNumberMismatch_Type(JuniEnable):
    """Custom type juniPppLinkConfigIgnoreMagicNumberMismatch based on JuniEnable"""


_JuniPppLinkConfigIgnoreMagicNumberMismatch_Object = MibTableColumn
juniPppLinkConfigIgnoreMagicNumberMismatch = _JuniPppLinkConfigIgnoreMagicNumberMismatch_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 14),
    _JuniPppLinkConfigIgnoreMagicNumberMismatch_Type()
)
juniPppLinkConfigIgnoreMagicNumberMismatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigIgnoreMagicNumberMismatch.setStatus("current")


class _JuniPppLinkConfigMaxLcpRenegotiation_Type(Integer32):
    """Custom type juniPppLinkConfigMaxLcpRenegotiation based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniPppLinkConfigMaxLcpRenegotiation_Type.__name__ = "Integer32"
_JuniPppLinkConfigMaxLcpRenegotiation_Object = MibTableColumn
juniPppLinkConfigMaxLcpRenegotiation = _JuniPppLinkConfigMaxLcpRenegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 2, 1, 15),
    _JuniPppLinkConfigMaxLcpRenegotiation_Type()
)
juniPppLinkConfigMaxLcpRenegotiation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppLinkConfigMaxLcpRenegotiation.setStatus("current")
_JuniPppNextIfIndex_Type = JuniNextIfIndex
_JuniPppNextIfIndex_Object = MibScalar
juniPppNextIfIndex = _JuniPppNextIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 1, 3),
    _JuniPppNextIfIndex_Type()
)
juniPppNextIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppNextIfIndex.setStatus("current")
_JuniPppSec_ObjectIdentity = ObjectIdentity
juniPppSec = _JuniPppSec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 2)
)
_JuniPppIp_ObjectIdentity = ObjectIdentity
juniPppIp = _JuniPppIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3)
)
_JuniPppIpTable_Object = MibTable
juniPppIpTable = _JuniPppIpTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1)
)
if mibBuilder.loadTexts:
    juniPppIpTable.setStatus("current")
_JuniPppIpEntry_Object = MibTableRow
juniPppIpEntry = _JuniPppIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1)
)
juniPppIpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniPppIpEntry.setStatus("current")
_JuniPppIpServiceStatus_Type = JuniEnable
_JuniPppIpServiceStatus_Object = MibTableColumn
juniPppIpServiceStatus = _JuniPppIpServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 1),
    _JuniPppIpServiceStatus_Type()
)
juniPppIpServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpServiceStatus.setStatus("current")


class _JuniPppIpTerminateReason_Type(Integer32):
    """Custom type juniPppIpTerminateReason based on Integer32"""
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


_JuniPppIpTerminateReason_Type.__name__ = "Integer32"
_JuniPppIpTerminateReason_Object = MibTableColumn
juniPppIpTerminateReason = _JuniPppIpTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 2),
    _JuniPppIpTerminateReason_Type()
)
juniPppIpTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpTerminateReason.setStatus("current")


class _JuniPppIpTerminateNegFailOption_Type(Integer32):
    """Custom type juniPppIpTerminateNegFailOption based on Integer32"""
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


_JuniPppIpTerminateNegFailOption_Type.__name__ = "Integer32"
_JuniPppIpTerminateNegFailOption_Object = MibTableColumn
juniPppIpTerminateNegFailOption = _JuniPppIpTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 3),
    _JuniPppIpTerminateNegFailOption_Type()
)
juniPppIpTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpTerminateNegFailOption.setStatus("current")
_JuniPppIpLocalIpAddress_Type = IpAddress
_JuniPppIpLocalIpAddress_Object = MibTableColumn
juniPppIpLocalIpAddress = _JuniPppIpLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 4),
    _JuniPppIpLocalIpAddress_Type()
)
juniPppIpLocalIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpLocalIpAddress.setStatus("current")
_JuniPppIpRemoteIpAddress_Type = IpAddress
_JuniPppIpRemoteIpAddress_Object = MibTableColumn
juniPppIpRemoteIpAddress = _JuniPppIpRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 5),
    _JuniPppIpRemoteIpAddress_Type()
)
juniPppIpRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpRemoteIpAddress.setStatus("current")
_JuniPppIpRemotePrimaryDnsAddress_Type = IpAddress
_JuniPppIpRemotePrimaryDnsAddress_Object = MibTableColumn
juniPppIpRemotePrimaryDnsAddress = _JuniPppIpRemotePrimaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 6),
    _JuniPppIpRemotePrimaryDnsAddress_Type()
)
juniPppIpRemotePrimaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpRemotePrimaryDnsAddress.setStatus("current")
_JuniPppIpRemoteSecondaryDnsAddress_Type = IpAddress
_JuniPppIpRemoteSecondaryDnsAddress_Object = MibTableColumn
juniPppIpRemoteSecondaryDnsAddress = _JuniPppIpRemoteSecondaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 7),
    _JuniPppIpRemoteSecondaryDnsAddress_Type()
)
juniPppIpRemoteSecondaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpRemoteSecondaryDnsAddress.setStatus("current")
_JuniPppIpRemotePrimaryWinsAddress_Type = IpAddress
_JuniPppIpRemotePrimaryWinsAddress_Object = MibTableColumn
juniPppIpRemotePrimaryWinsAddress = _JuniPppIpRemotePrimaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 8),
    _JuniPppIpRemotePrimaryWinsAddress_Type()
)
juniPppIpRemotePrimaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpRemotePrimaryWinsAddress.setStatus("current")
_JuniPppIpRemoteSecondaryWinsAddress_Type = IpAddress
_JuniPppIpRemoteSecondaryWinsAddress_Object = MibTableColumn
juniPppIpRemoteSecondaryWinsAddress = _JuniPppIpRemoteSecondaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 9),
    _JuniPppIpRemoteSecondaryWinsAddress_Type()
)
juniPppIpRemoteSecondaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpRemoteSecondaryWinsAddress.setStatus("current")
_JuniPppIpNetworkStatusIpcpRenegoTerminates_Type = Counter32
_JuniPppIpNetworkStatusIpcpRenegoTerminates_Object = MibTableColumn
juniPppIpNetworkStatusIpcpRenegoTerminates = _JuniPppIpNetworkStatusIpcpRenegoTerminates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 1, 1, 10),
    _JuniPppIpNetworkStatusIpcpRenegoTerminates_Type()
)
juniPppIpNetworkStatusIpcpRenegoTerminates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpNetworkStatusIpcpRenegoTerminates.setStatus("current")
_JuniPppIpConfigTable_Object = MibTable
juniPppIpConfigTable = _JuniPppIpConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2)
)
if mibBuilder.loadTexts:
    juniPppIpConfigTable.setStatus("current")
_JuniPppIpConfigEntry_Object = MibTableRow
juniPppIpConfigEntry = _JuniPppIpConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1)
)
juniPppIpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniPppIpConfigEntry.setStatus("current")
_JuniPppIpConfigPeerDnsPriority_Type = JuniEnable
_JuniPppIpConfigPeerDnsPriority_Object = MibTableColumn
juniPppIpConfigPeerDnsPriority = _JuniPppIpConfigPeerDnsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1, 1),
    _JuniPppIpConfigPeerDnsPriority_Type()
)
juniPppIpConfigPeerDnsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppIpConfigPeerDnsPriority.setStatus("current")
_JuniPppIpConfigPeerWinsPriority_Type = JuniEnable
_JuniPppIpConfigPeerWinsPriority_Object = MibTableColumn
juniPppIpConfigPeerWinsPriority = _JuniPppIpConfigPeerWinsPriority_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1, 2),
    _JuniPppIpConfigPeerWinsPriority_Type()
)
juniPppIpConfigPeerWinsPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppIpConfigPeerWinsPriority.setStatus("current")


class _JuniPppIpConfigIpcpNetmask_Type(JuniEnable):
    """Custom type juniPppIpConfigIpcpNetmask based on JuniEnable"""


_JuniPppIpConfigIpcpNetmask_Object = MibTableColumn
juniPppIpConfigIpcpNetmask = _JuniPppIpConfigIpcpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1, 3),
    _JuniPppIpConfigIpcpNetmask_Type()
)
juniPppIpConfigIpcpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppIpConfigIpcpNetmask.setStatus("current")


class _JuniPppIpConfigInitiateIp_Type(JuniEnable):
    """Custom type juniPppIpConfigInitiateIp based on JuniEnable"""


_JuniPppIpConfigInitiateIp_Object = MibTableColumn
juniPppIpConfigInitiateIp = _JuniPppIpConfigInitiateIp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1, 4),
    _JuniPppIpConfigInitiateIp_Type()
)
juniPppIpConfigInitiateIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppIpConfigInitiateIp.setStatus("current")


class _JuniPppIpConfigMaxIpcpRenegotiation_Type(Integer32):
    """Custom type juniPppIpConfigMaxIpcpRenegotiation based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniPppIpConfigMaxIpcpRenegotiation_Type.__name__ = "Integer32"
_JuniPppIpConfigMaxIpcpRenegotiation_Object = MibTableColumn
juniPppIpConfigMaxIpcpRenegotiation = _JuniPppIpConfigMaxIpcpRenegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1, 5),
    _JuniPppIpConfigMaxIpcpRenegotiation_Type()
)
juniPppIpConfigMaxIpcpRenegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppIpConfigMaxIpcpRenegotiation.setStatus("current")


class _JuniPppIpConfigPromptIpcpDnsOption_Type(JuniEnable):
    """Custom type juniPppIpConfigPromptIpcpDnsOption based on JuniEnable"""


_JuniPppIpConfigPromptIpcpDnsOption_Object = MibTableColumn
juniPppIpConfigPromptIpcpDnsOption = _JuniPppIpConfigPromptIpcpDnsOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1, 6),
    _JuniPppIpConfigPromptIpcpDnsOption_Type()
)
juniPppIpConfigPromptIpcpDnsOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppIpConfigPromptIpcpDnsOption.setStatus("current")


class _JuniPppIpConfigIpcpLockout_Type(JuniEnable):
    """Custom type juniPppIpConfigIpcpLockout based on JuniEnable"""


_JuniPppIpConfigIpcpLockout_Object = MibTableColumn
juniPppIpConfigIpcpLockout = _JuniPppIpConfigIpcpLockout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 3, 2, 1, 7),
    _JuniPppIpConfigIpcpLockout_Type()
)
juniPppIpConfigIpcpLockout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppIpConfigIpcpLockout.setStatus("current")
_JuniPppOsi_ObjectIdentity = ObjectIdentity
juniPppOsi = _JuniPppOsi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4)
)
_JuniPppOsiTable_Object = MibTable
juniPppOsiTable = _JuniPppOsiTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1)
)
if mibBuilder.loadTexts:
    juniPppOsiTable.setStatus("current")
_JuniPppOsiEntry_Object = MibTableRow
juniPppOsiEntry = _JuniPppOsiEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1)
)
juniPppOsiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniPppOsiEntry.setStatus("current")
_JuniPppOsiServiceStatus_Type = JuniEnable
_JuniPppOsiServiceStatus_Object = MibTableColumn
juniPppOsiServiceStatus = _JuniPppOsiServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 1),
    _JuniPppOsiServiceStatus_Type()
)
juniPppOsiServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppOsiServiceStatus.setStatus("current")


class _JuniPppOsiOperStatus_Type(Integer32):
    """Custom type juniPppOsiOperStatus based on Integer32"""
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


_JuniPppOsiOperStatus_Type.__name__ = "Integer32"
_JuniPppOsiOperStatus_Object = MibTableColumn
juniPppOsiOperStatus = _JuniPppOsiOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 2),
    _JuniPppOsiOperStatus_Type()
)
juniPppOsiOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppOsiOperStatus.setStatus("current")


class _JuniPppOsiTerminateReason_Type(Integer32):
    """Custom type juniPppOsiTerminateReason based on Integer32"""
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


_JuniPppOsiTerminateReason_Type.__name__ = "Integer32"
_JuniPppOsiTerminateReason_Object = MibTableColumn
juniPppOsiTerminateReason = _JuniPppOsiTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 3),
    _JuniPppOsiTerminateReason_Type()
)
juniPppOsiTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppOsiTerminateReason.setStatus("current")


class _JuniPppOsiTerminateNegFailOption_Type(Integer32):
    """Custom type juniPppOsiTerminateNegFailOption based on Integer32"""
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


_JuniPppOsiTerminateNegFailOption_Type.__name__ = "Integer32"
_JuniPppOsiTerminateNegFailOption_Object = MibTableColumn
juniPppOsiTerminateNegFailOption = _JuniPppOsiTerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 4),
    _JuniPppOsiTerminateNegFailOption_Type()
)
juniPppOsiTerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppOsiTerminateNegFailOption.setStatus("current")


class _JuniPppOsiLocalAlignNpdu_Type(Integer32):
    """Custom type juniPppOsiLocalAlignNpdu based on Integer32"""
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


_JuniPppOsiLocalAlignNpdu_Type.__name__ = "Integer32"
_JuniPppOsiLocalAlignNpdu_Object = MibTableColumn
juniPppOsiLocalAlignNpdu = _JuniPppOsiLocalAlignNpdu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 5),
    _JuniPppOsiLocalAlignNpdu_Type()
)
juniPppOsiLocalAlignNpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppOsiLocalAlignNpdu.setStatus("current")


class _JuniPppOsiRemoteAlignNpdu_Type(Integer32):
    """Custom type juniPppOsiRemoteAlignNpdu based on Integer32"""
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


_JuniPppOsiRemoteAlignNpdu_Type.__name__ = "Integer32"
_JuniPppOsiRemoteAlignNpdu_Object = MibTableColumn
juniPppOsiRemoteAlignNpdu = _JuniPppOsiRemoteAlignNpdu_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 1, 1, 6),
    _JuniPppOsiRemoteAlignNpdu_Type()
)
juniPppOsiRemoteAlignNpdu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppOsiRemoteAlignNpdu.setStatus("current")
_JuniPppOsiConfigTable_Object = MibTable
juniPppOsiConfigTable = _JuniPppOsiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 2)
)
if mibBuilder.loadTexts:
    juniPppOsiConfigTable.setStatus("current")
_JuniPppOsiConfigEntry_Object = MibTableRow
juniPppOsiConfigEntry = _JuniPppOsiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 2, 1)
)
juniPppOsiConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniPppOsiConfigEntry.setStatus("current")


class _JuniPppOsiConfigAdminStatus_Type(Integer32):
    """Custom type juniPppOsiConfigAdminStatus based on Integer32"""
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


_JuniPppOsiConfigAdminStatus_Type.__name__ = "Integer32"
_JuniPppOsiConfigAdminStatus_Object = MibTableColumn
juniPppOsiConfigAdminStatus = _JuniPppOsiConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 4, 2, 1, 1),
    _JuniPppOsiConfigAdminStatus_Type()
)
juniPppOsiConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppOsiConfigAdminStatus.setStatus("current")
_JuniPppSession_ObjectIdentity = ObjectIdentity
juniPppSession = _JuniPppSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5)
)
_JuniPppSessionTable_Object = MibTable
juniPppSessionTable = _JuniPppSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1)
)
if mibBuilder.loadTexts:
    juniPppSessionTable.setStatus("current")
_JuniPppSessionEntry_Object = MibTableRow
juniPppSessionEntry = _JuniPppSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1)
)
juniPppSessionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniPppSessionEntry.setStatus("current")
_JuniPppSessionGrant_Type = TruthValue
_JuniPppSessionGrant_Object = MibTableColumn
juniPppSessionGrant = _JuniPppSessionGrant_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 1),
    _JuniPppSessionGrant_Type()
)
juniPppSessionGrant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionGrant.setStatus("current")


class _JuniPppSessionTerminateReason_Type(Integer32):
    """Custom type juniPppSessionTerminateReason based on Integer32"""
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


_JuniPppSessionTerminateReason_Type.__name__ = "Integer32"
_JuniPppSessionTerminateReason_Object = MibTableColumn
juniPppSessionTerminateReason = _JuniPppSessionTerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 2),
    _JuniPppSessionTerminateReason_Type()
)
juniPppSessionTerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionTerminateReason.setStatus("current")
_JuniPppSessionStartTime_Type = TimeTicks
_JuniPppSessionStartTime_Object = MibTableColumn
juniPppSessionStartTime = _JuniPppSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 3),
    _JuniPppSessionStartTime_Type()
)
juniPppSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionStartTime.setStatus("current")
_JuniPppSessionInOctets_Type = Counter32
_JuniPppSessionInOctets_Object = MibTableColumn
juniPppSessionInOctets = _JuniPppSessionInOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 4),
    _JuniPppSessionInOctets_Type()
)
juniPppSessionInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionInOctets.setStatus("current")
if mibBuilder.loadTexts:
    juniPppSessionInOctets.setUnits("octets")
_JuniPppSessionOutOctets_Type = Counter32
_JuniPppSessionOutOctets_Object = MibTableColumn
juniPppSessionOutOctets = _JuniPppSessionOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 5),
    _JuniPppSessionOutOctets_Type()
)
juniPppSessionOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    juniPppSessionOutOctets.setUnits("octets")
_JuniPppSessionInPackets_Type = Counter32
_JuniPppSessionInPackets_Object = MibTableColumn
juniPppSessionInPackets = _JuniPppSessionInPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 6),
    _JuniPppSessionInPackets_Type()
)
juniPppSessionInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionInPackets.setStatus("current")
if mibBuilder.loadTexts:
    juniPppSessionInPackets.setUnits("packets")
_JuniPppSessionOutPackets_Type = Counter32
_JuniPppSessionOutPackets_Object = MibTableColumn
juniPppSessionOutPackets = _JuniPppSessionOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 7),
    _JuniPppSessionOutPackets_Type()
)
juniPppSessionOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionOutPackets.setStatus("current")
if mibBuilder.loadTexts:
    juniPppSessionOutPackets.setUnits("packets")


class _JuniPppSessionSessionTimeout_Type(Integer32):
    """Custom type juniPppSessionSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPppSessionSessionTimeout_Type.__name__ = "Integer32"
_JuniPppSessionSessionTimeout_Object = MibTableColumn
juniPppSessionSessionTimeout = _JuniPppSessionSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 8),
    _JuniPppSessionSessionTimeout_Type()
)
juniPppSessionSessionTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionSessionTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniPppSessionSessionTimeout.setUnits("milliseconds")


class _JuniPppSessionInactivityTimeout_Type(Integer32):
    """Custom type juniPppSessionInactivityTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPppSessionInactivityTimeout_Type.__name__ = "Integer32"
_JuniPppSessionInactivityTimeout_Object = MibTableColumn
juniPppSessionInactivityTimeout = _JuniPppSessionInactivityTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 9),
    _JuniPppSessionInactivityTimeout_Type()
)
juniPppSessionInactivityTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionInactivityTimeout.setStatus("current")
if mibBuilder.loadTexts:
    juniPppSessionInactivityTimeout.setUnits("milliseconds")


class _JuniPppSessionAccountingInterval_Type(Integer32):
    """Custom type juniPppSessionAccountingInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_JuniPppSessionAccountingInterval_Type.__name__ = "Integer32"
_JuniPppSessionAccountingInterval_Object = MibTableColumn
juniPppSessionAccountingInterval = _JuniPppSessionAccountingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 10),
    _JuniPppSessionAccountingInterval_Type()
)
juniPppSessionAccountingInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionAccountingInterval.setStatus("current")
if mibBuilder.loadTexts:
    juniPppSessionAccountingInterval.setUnits("milliseconds")
_JuniPppSessionRemoteIpAddress_Type = IpAddress
_JuniPppSessionRemoteIpAddress_Object = MibTableColumn
juniPppSessionRemoteIpAddress = _JuniPppSessionRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 11),
    _JuniPppSessionRemoteIpAddress_Type()
)
juniPppSessionRemoteIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionRemoteIpAddress.setStatus("current")
_JuniPppSessionRemotePrimaryDnsAddress_Type = IpAddress
_JuniPppSessionRemotePrimaryDnsAddress_Object = MibTableColumn
juniPppSessionRemotePrimaryDnsAddress = _JuniPppSessionRemotePrimaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 12),
    _JuniPppSessionRemotePrimaryDnsAddress_Type()
)
juniPppSessionRemotePrimaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionRemotePrimaryDnsAddress.setStatus("current")
_JuniPppSessionRemoteSecondaryDnsAddress_Type = IpAddress
_JuniPppSessionRemoteSecondaryDnsAddress_Object = MibTableColumn
juniPppSessionRemoteSecondaryDnsAddress = _JuniPppSessionRemoteSecondaryDnsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 13),
    _JuniPppSessionRemoteSecondaryDnsAddress_Type()
)
juniPppSessionRemoteSecondaryDnsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionRemoteSecondaryDnsAddress.setStatus("current")
_JuniPppSessionRemotePrimaryWinsAddress_Type = IpAddress
_JuniPppSessionRemotePrimaryWinsAddress_Object = MibTableColumn
juniPppSessionRemotePrimaryWinsAddress = _JuniPppSessionRemotePrimaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 14),
    _JuniPppSessionRemotePrimaryWinsAddress_Type()
)
juniPppSessionRemotePrimaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionRemotePrimaryWinsAddress.setStatus("current")
_JuniPppSessionRemoteSecondaryWinsAddress_Type = IpAddress
_JuniPppSessionRemoteSecondaryWinsAddress_Object = MibTableColumn
juniPppSessionRemoteSecondaryWinsAddress = _JuniPppSessionRemoteSecondaryWinsAddress_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 15),
    _JuniPppSessionRemoteSecondaryWinsAddress_Type()
)
juniPppSessionRemoteSecondaryWinsAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionRemoteSecondaryWinsAddress.setStatus("current")
_JuniPppSessionRemoteIpv6AddressIfIdentifier_Type = Ipv6AddressIfIdentifier
_JuniPppSessionRemoteIpv6AddressIfIdentifier_Object = MibTableColumn
juniPppSessionRemoteIpv6AddressIfIdentifier = _JuniPppSessionRemoteIpv6AddressIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 16),
    _JuniPppSessionRemoteIpv6AddressIfIdentifier_Type()
)
juniPppSessionRemoteIpv6AddressIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionRemoteIpv6AddressIfIdentifier.setStatus("current")
_JuniPppSessionInhibitIp_Type = TruthValue
_JuniPppSessionInhibitIp_Object = MibTableColumn
juniPppSessionInhibitIp = _JuniPppSessionInhibitIp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 17),
    _JuniPppSessionInhibitIp_Type()
)
juniPppSessionInhibitIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionInhibitIp.setStatus("current")
_JuniPppSessionInhibitIpv6_Type = TruthValue
_JuniPppSessionInhibitIpv6_Object = MibTableColumn
juniPppSessionInhibitIpv6 = _JuniPppSessionInhibitIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 5, 1, 1, 18),
    _JuniPppSessionInhibitIpv6_Type()
)
juniPppSessionInhibitIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSessionInhibitIpv6.setStatus("current")
_JuniPppMlPpp_ObjectIdentity = ObjectIdentity
juniPppMlPpp = _JuniPppMlPpp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6)
)
_JuniPppMlPppBundleTable_Object = MibTable
juniPppMlPppBundleTable = _JuniPppMlPppBundleTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 1)
)
if mibBuilder.loadTexts:
    juniPppMlPppBundleTable.setStatus("current")
_JuniPppMlPppBundleEntry_Object = MibTableRow
juniPppMlPppBundleEntry = _JuniPppMlPppBundleEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 1, 1)
)
juniPppMlPppBundleEntry.setIndexNames(
    (0, "Juniper-PPP-MIB", "juniPppMlPppBundleName"),
)
if mibBuilder.loadTexts:
    juniPppMlPppBundleEntry.setStatus("current")
_JuniPppMlPppBundleName_Type = JuniPppMlPppBundleName
_JuniPppMlPppBundleName_Object = MibTableColumn
juniPppMlPppBundleName = _JuniPppMlPppBundleName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 1, 1, 1),
    _JuniPppMlPppBundleName_Type()
)
juniPppMlPppBundleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppMlPppBundleName.setStatus("current")
_JuniPppMlPppBundleRowStatus_Type = RowStatus
_JuniPppMlPppBundleRowStatus_Object = MibTableColumn
juniPppMlPppBundleRowStatus = _JuniPppMlPppBundleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 1, 1, 2),
    _JuniPppMlPppBundleRowStatus_Type()
)
juniPppMlPppBundleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppBundleRowStatus.setStatus("current")
_JuniPppMlPppBundleNetworkIfIndex_Type = InterfaceIndex
_JuniPppMlPppBundleNetworkIfIndex_Object = MibTableColumn
juniPppMlPppBundleNetworkIfIndex = _JuniPppMlPppBundleNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 1, 1, 3),
    _JuniPppMlPppBundleNetworkIfIndex_Type()
)
juniPppMlPppBundleNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppMlPppBundleNetworkIfIndex.setStatus("current")
_JuniPppMlPppNextLinkIfIndex_Type = JuniNextIfIndex
_JuniPppMlPppNextLinkIfIndex_Object = MibScalar
juniPppMlPppNextLinkIfIndex = _JuniPppMlPppNextLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 2),
    _JuniPppMlPppNextLinkIfIndex_Type()
)
juniPppMlPppNextLinkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppMlPppNextLinkIfIndex.setStatus("current")
_JuniPppMlPppLinkConfigTable_Object = MibTable
juniPppMlPppLinkConfigTable = _JuniPppMlPppLinkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3)
)
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigTable.setStatus("current")
_JuniPppMlPppLinkConfigEntry_Object = MibTableRow
juniPppMlPppLinkConfigEntry = _JuniPppMlPppLinkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1)
)
juniPppMlPppLinkConfigEntry.setIndexNames(
    (0, "Juniper-PPP-MIB", "juniPppMlPppLinkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigEntry.setStatus("current")
_JuniPppMlPppLinkConfigIfIndex_Type = InterfaceIndex
_JuniPppMlPppLinkConfigIfIndex_Object = MibTableColumn
juniPppMlPppLinkConfigIfIndex = _JuniPppMlPppLinkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 1),
    _JuniPppMlPppLinkConfigIfIndex_Type()
)
juniPppMlPppLinkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigIfIndex.setStatus("current")
_JuniPppMlPppLinkConfigLowerIfIndex_Type = InterfaceIndexOrZero
_JuniPppMlPppLinkConfigLowerIfIndex_Object = MibTableColumn
juniPppMlPppLinkConfigLowerIfIndex = _JuniPppMlPppLinkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 2),
    _JuniPppMlPppLinkConfigLowerIfIndex_Type()
)
juniPppMlPppLinkConfigLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigLowerIfIndex.setStatus("current")


class _JuniPppMlPppLinkConfigKeepalive_Type(Integer32):
    """Custom type juniPppMlPppLinkConfigKeepalive based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(10, 64800),
    )


_JuniPppMlPppLinkConfigKeepalive_Type.__name__ = "Integer32"
_JuniPppMlPppLinkConfigKeepalive_Object = MibTableColumn
juniPppMlPppLinkConfigKeepalive = _JuniPppMlPppLinkConfigKeepalive_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 4),
    _JuniPppMlPppLinkConfigKeepalive_Type()
)
juniPppMlPppLinkConfigKeepalive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigKeepalive.setStatus("current")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigKeepalive.setUnits("seconds")


class _JuniPppMlPppLinkConfigAuthentication_Type(JuniPppAuthentication):
    """Custom type juniPppMlPppLinkConfigAuthentication based on JuniPppAuthentication"""


_JuniPppMlPppLinkConfigAuthentication_Object = MibTableColumn
juniPppMlPppLinkConfigAuthentication = _JuniPppMlPppLinkConfigAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 5),
    _JuniPppMlPppLinkConfigAuthentication_Type()
)
juniPppMlPppLinkConfigAuthentication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigAuthentication.setStatus("deprecated")


class _JuniPppMlPppLinkConfigMaxAuthenRetries_Type(Integer32):
    """Custom type juniPppMlPppLinkConfigMaxAuthenRetries based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_JuniPppMlPppLinkConfigMaxAuthenRetries_Type.__name__ = "Integer32"
_JuniPppMlPppLinkConfigMaxAuthenRetries_Object = MibTableColumn
juniPppMlPppLinkConfigMaxAuthenRetries = _JuniPppMlPppLinkConfigMaxAuthenRetries_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 6),
    _JuniPppMlPppLinkConfigMaxAuthenRetries_Type()
)
juniPppMlPppLinkConfigMaxAuthenRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigMaxAuthenRetries.setStatus("current")
_JuniPppMlPppLinkConfigRowStatus_Type = RowStatus
_JuniPppMlPppLinkConfigRowStatus_Object = MibTableColumn
juniPppMlPppLinkConfigRowStatus = _JuniPppMlPppLinkConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 7),
    _JuniPppMlPppLinkConfigRowStatus_Type()
)
juniPppMlPppLinkConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigRowStatus.setStatus("current")
_JuniPppMlPppLinkConfigAaaProfile_Type = JuniName
_JuniPppMlPppLinkConfigAaaProfile_Object = MibTableColumn
juniPppMlPppLinkConfigAaaProfile = _JuniPppMlPppLinkConfigAaaProfile_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 8),
    _JuniPppMlPppLinkConfigAaaProfile_Type()
)
juniPppMlPppLinkConfigAaaProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigAaaProfile.setStatus("current")


class _JuniPppMlPppLinkConfigChapMinChallengeLength_Type(Integer32):
    """Custom type juniPppMlPppLinkConfigChapMinChallengeLength based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_JuniPppMlPppLinkConfigChapMinChallengeLength_Type.__name__ = "Integer32"
_JuniPppMlPppLinkConfigChapMinChallengeLength_Object = MibTableColumn
juniPppMlPppLinkConfigChapMinChallengeLength = _JuniPppMlPppLinkConfigChapMinChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 9),
    _JuniPppMlPppLinkConfigChapMinChallengeLength_Type()
)
juniPppMlPppLinkConfigChapMinChallengeLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigChapMinChallengeLength.setStatus("current")


class _JuniPppMlPppLinkConfigChapMaxChallengeLength_Type(Integer32):
    """Custom type juniPppMlPppLinkConfigChapMaxChallengeLength based on Integer32"""
    defaultValue = 32

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(8, 63),
    )


_JuniPppMlPppLinkConfigChapMaxChallengeLength_Type.__name__ = "Integer32"
_JuniPppMlPppLinkConfigChapMaxChallengeLength_Object = MibTableColumn
juniPppMlPppLinkConfigChapMaxChallengeLength = _JuniPppMlPppLinkConfigChapMaxChallengeLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 10),
    _JuniPppMlPppLinkConfigChapMaxChallengeLength_Type()
)
juniPppMlPppLinkConfigChapMaxChallengeLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigChapMaxChallengeLength.setStatus("current")


class _JuniPppMlPppLinkConfigPassiveMode_Type(JuniEnable):
    """Custom type juniPppMlPppLinkConfigPassiveMode based on JuniEnable"""


_JuniPppMlPppLinkConfigPassiveMode_Object = MibTableColumn
juniPppMlPppLinkConfigPassiveMode = _JuniPppMlPppLinkConfigPassiveMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 11),
    _JuniPppMlPppLinkConfigPassiveMode_Type()
)
juniPppMlPppLinkConfigPassiveMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigPassiveMode.setStatus("current")
_JuniPppMlPppLinkConfigAuthenticatorVirtualRouter_Type = JuniName
_JuniPppMlPppLinkConfigAuthenticatorVirtualRouter_Object = MibTableColumn
juniPppMlPppLinkConfigAuthenticatorVirtualRouter = _JuniPppMlPppLinkConfigAuthenticatorVirtualRouter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 12),
    _JuniPppMlPppLinkConfigAuthenticatorVirtualRouter_Type()
)
juniPppMlPppLinkConfigAuthenticatorVirtualRouter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigAuthenticatorVirtualRouter.setStatus("current")


class _JuniPppMlPppLinkConfigFragmentation_Type(JuniEnable):
    """Custom type juniPppMlPppLinkConfigFragmentation based on JuniEnable"""


_JuniPppMlPppLinkConfigFragmentation_Object = MibTableColumn
juniPppMlPppLinkConfigFragmentation = _JuniPppMlPppLinkConfigFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 13),
    _JuniPppMlPppLinkConfigFragmentation_Type()
)
juniPppMlPppLinkConfigFragmentation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigFragmentation.setStatus("current")


class _JuniPppMlPppLinkConfigReassembly_Type(JuniEnable):
    """Custom type juniPppMlPppLinkConfigReassembly based on JuniEnable"""


_JuniPppMlPppLinkConfigReassembly_Object = MibTableColumn
juniPppMlPppLinkConfigReassembly = _JuniPppMlPppLinkConfigReassembly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 14),
    _JuniPppMlPppLinkConfigReassembly_Type()
)
juniPppMlPppLinkConfigReassembly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigReassembly.setStatus("current")


class _JuniPppMlPppLinkConfigMaxReceiveReconstructedUnit_Type(Integer32):
    """Custom type juniPppMlPppLinkConfigMaxReceiveReconstructedUnit based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(64, 65535),
    )


_JuniPppMlPppLinkConfigMaxReceiveReconstructedUnit_Type.__name__ = "Integer32"
_JuniPppMlPppLinkConfigMaxReceiveReconstructedUnit_Object = MibTableColumn
juniPppMlPppLinkConfigMaxReceiveReconstructedUnit = _JuniPppMlPppLinkConfigMaxReceiveReconstructedUnit_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 15),
    _JuniPppMlPppLinkConfigMaxReceiveReconstructedUnit_Type()
)
juniPppMlPppLinkConfigMaxReceiveReconstructedUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigMaxReceiveReconstructedUnit.setStatus("current")


class _JuniPppMlPppLinkConfigFragmentSize_Type(Integer32):
    """Custom type juniPppMlPppLinkConfigFragmentSize based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
        ValueRangeConstraint(128, 65535),
    )


_JuniPppMlPppLinkConfigFragmentSize_Type.__name__ = "Integer32"
_JuniPppMlPppLinkConfigFragmentSize_Object = MibTableColumn
juniPppMlPppLinkConfigFragmentSize = _JuniPppMlPppLinkConfigFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 16),
    _JuniPppMlPppLinkConfigFragmentSize_Type()
)
juniPppMlPppLinkConfigFragmentSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigFragmentSize.setStatus("current")


class _JuniPppMlPppLinkConfigHashLinkSelection_Type(JuniEnable):
    """Custom type juniPppMlPppLinkConfigHashLinkSelection based on JuniEnable"""


_JuniPppMlPppLinkConfigHashLinkSelection_Object = MibTableColumn
juniPppMlPppLinkConfigHashLinkSelection = _JuniPppMlPppLinkConfigHashLinkSelection_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 17),
    _JuniPppMlPppLinkConfigHashLinkSelection_Type()
)
juniPppMlPppLinkConfigHashLinkSelection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigHashLinkSelection.setStatus("current")


class _JuniPppMlPppLinkConfigAuthentication2_Type(JuniNibbleConfig):
    """Custom type juniPppMlPppLinkConfigAuthentication2 based on JuniNibbleConfig"""
    defaultValue = 0


_JuniPppMlPppLinkConfigAuthentication2_Object = MibTableColumn
juniPppMlPppLinkConfigAuthentication2 = _JuniPppMlPppLinkConfigAuthentication2_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 18),
    _JuniPppMlPppLinkConfigAuthentication2_Type()
)
juniPppMlPppLinkConfigAuthentication2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigAuthentication2.setStatus("current")


class _JuniPppMlPppLinkConfigIgnoreMagicNumberMismatch_Type(JuniEnable):
    """Custom type juniPppMlPppLinkConfigIgnoreMagicNumberMismatch based on JuniEnable"""


_JuniPppMlPppLinkConfigIgnoreMagicNumberMismatch_Object = MibTableColumn
juniPppMlPppLinkConfigIgnoreMagicNumberMismatch = _JuniPppMlPppLinkConfigIgnoreMagicNumberMismatch_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 19),
    _JuniPppMlPppLinkConfigIgnoreMagicNumberMismatch_Type()
)
juniPppMlPppLinkConfigIgnoreMagicNumberMismatch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigIgnoreMagicNumberMismatch.setStatus("current")


class _JuniPppMlPppLinkConfigMultilinkMulticlass_Type(JuniEnable):
    """Custom type juniPppMlPppLinkConfigMultilinkMulticlass based on JuniEnable"""


_JuniPppMlPppLinkConfigMultilinkMulticlass_Object = MibTableColumn
juniPppMlPppLinkConfigMultilinkMulticlass = _JuniPppMlPppLinkConfigMultilinkMulticlass_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 20),
    _JuniPppMlPppLinkConfigMultilinkMulticlass_Type()
)
juniPppMlPppLinkConfigMultilinkMulticlass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigMultilinkMulticlass.setStatus("current")


class _JuniPppMlPppLinkConfigMultilinkMaxMultiClasses_Type(Integer32):
    """Custom type juniPppMlPppLinkConfigMultilinkMaxMultiClasses based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_JuniPppMlPppLinkConfigMultilinkMaxMultiClasses_Type.__name__ = "Integer32"
_JuniPppMlPppLinkConfigMultilinkMaxMultiClasses_Object = MibTableColumn
juniPppMlPppLinkConfigMultilinkMaxMultiClasses = _JuniPppMlPppLinkConfigMultilinkMaxMultiClasses_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 3, 1, 21),
    _JuniPppMlPppLinkConfigMultilinkMaxMultiClasses_Type()
)
juniPppMlPppLinkConfigMultilinkMaxMultiClasses.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppLinkConfigMultilinkMaxMultiClasses.setStatus("current")
_JuniPppMlPppNextNetworkIfIndex_Type = JuniNextIfIndex
_JuniPppMlPppNextNetworkIfIndex_Object = MibScalar
juniPppMlPppNextNetworkIfIndex = _JuniPppMlPppNextNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 4),
    _JuniPppMlPppNextNetworkIfIndex_Type()
)
juniPppMlPppNextNetworkIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppMlPppNextNetworkIfIndex.setStatus("current")
_JuniPppMlPppNetworkConfigTable_Object = MibTable
juniPppMlPppNetworkConfigTable = _JuniPppMlPppNetworkConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5)
)
if mibBuilder.loadTexts:
    juniPppMlPppNetworkConfigTable.setStatus("current")
_JuniPppMlPppNetworkConfigEntry_Object = MibTableRow
juniPppMlPppNetworkConfigEntry = _JuniPppMlPppNetworkConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5, 1)
)
juniPppMlPppNetworkConfigEntry.setIndexNames(
    (0, "Juniper-PPP-MIB", "juniPppMlPppNetworkConfigIfIndex"),
)
if mibBuilder.loadTexts:
    juniPppMlPppNetworkConfigEntry.setStatus("current")
_JuniPppMlPppNetworkConfigIfIndex_Type = InterfaceIndex
_JuniPppMlPppNetworkConfigIfIndex_Object = MibTableColumn
juniPppMlPppNetworkConfigIfIndex = _JuniPppMlPppNetworkConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5, 1, 1),
    _JuniPppMlPppNetworkConfigIfIndex_Type()
)
juniPppMlPppNetworkConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppMlPppNetworkConfigIfIndex.setStatus("current")
_JuniPppMlPppNetworkConfigLowerIfIndex_Type = InterfaceIndex
_JuniPppMlPppNetworkConfigLowerIfIndex_Object = MibTableColumn
juniPppMlPppNetworkConfigLowerIfIndex = _JuniPppMlPppNetworkConfigLowerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5, 1, 2),
    _JuniPppMlPppNetworkConfigLowerIfIndex_Type()
)
juniPppMlPppNetworkConfigLowerIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppNetworkConfigLowerIfIndex.setStatus("current")
_JuniPppMlPppNetworkBundleName_Type = JuniPppMlPppBundleName
_JuniPppMlPppNetworkBundleName_Object = MibTableColumn
juniPppMlPppNetworkBundleName = _JuniPppMlPppNetworkBundleName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5, 1, 3),
    _JuniPppMlPppNetworkBundleName_Type()
)
juniPppMlPppNetworkBundleName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppNetworkBundleName.setStatus("current")
_JuniPppMlPppNetworkRowStatus_Type = RowStatus
_JuniPppMlPppNetworkRowStatus_Object = MibTableColumn
juniPppMlPppNetworkRowStatus = _JuniPppMlPppNetworkRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 5, 1, 4),
    _JuniPppMlPppNetworkRowStatus_Type()
)
juniPppMlPppNetworkRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppNetworkRowStatus.setStatus("current")
_JuniPppMlPppLinkBindTable_Object = MibTable
juniPppMlPppLinkBindTable = _JuniPppMlPppLinkBindTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 6)
)
if mibBuilder.loadTexts:
    juniPppMlPppLinkBindTable.setStatus("current")
_JuniPppMlPppLinkBindEntry_Object = MibTableRow
juniPppMlPppLinkBindEntry = _JuniPppMlPppLinkBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 6, 1)
)
juniPppMlPppLinkBindEntry.setIndexNames(
    (0, "Juniper-PPP-MIB", "juniPppMlPppBindNetworkIfIndex"),
    (0, "Juniper-PPP-MIB", "juniPppMlPppBindLinkIfIndex"),
)
if mibBuilder.loadTexts:
    juniPppMlPppLinkBindEntry.setStatus("current")
_JuniPppMlPppBindNetworkIfIndex_Type = InterfaceIndex
_JuniPppMlPppBindNetworkIfIndex_Object = MibTableColumn
juniPppMlPppBindNetworkIfIndex = _JuniPppMlPppBindNetworkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 6, 1, 1),
    _JuniPppMlPppBindNetworkIfIndex_Type()
)
juniPppMlPppBindNetworkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppMlPppBindNetworkIfIndex.setStatus("current")
_JuniPppMlPppBindLinkIfIndex_Type = InterfaceIndex
_JuniPppMlPppBindLinkIfIndex_Object = MibTableColumn
juniPppMlPppBindLinkIfIndex = _JuniPppMlPppBindLinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 6, 1, 2),
    _JuniPppMlPppBindLinkIfIndex_Type()
)
juniPppMlPppBindLinkIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppMlPppBindLinkIfIndex.setStatus("current")
_JuniPppMlPppBindRowStatus_Type = RowStatus
_JuniPppMlPppBindRowStatus_Object = MibTableColumn
juniPppMlPppBindRowStatus = _JuniPppMlPppBindRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 6, 1, 3),
    _JuniPppMlPppBindRowStatus_Type()
)
juniPppMlPppBindRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniPppMlPppBindRowStatus.setStatus("current")
_JuniPppMlPppMulticlassTraffiClassTable_Object = MibTable
juniPppMlPppMulticlassTraffiClassTable = _JuniPppMlPppMulticlassTraffiClassTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 7)
)
if mibBuilder.loadTexts:
    juniPppMlPppMulticlassTraffiClassTable.setStatus("current")
_JuniPppMlPppMulticlassTrafficClassEntry_Object = MibTableRow
juniPppMlPppMulticlassTrafficClassEntry = _JuniPppMlPppMulticlassTrafficClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 7, 1)
)
juniPppMlPppMulticlassTrafficClassEntry.setIndexNames(
    (0, "Juniper-PPP-MIB", "juniPppMlPppMulticlassIfIndex"),
    (0, "Juniper-PPP-MIB", "juniPppMlPppMulticlassIndex"),
)
if mibBuilder.loadTexts:
    juniPppMlPppMulticlassTrafficClassEntry.setStatus("current")
_JuniPppMlPppMulticlassIfIndex_Type = InterfaceIndex
_JuniPppMlPppMulticlassIfIndex_Object = MibTableColumn
juniPppMlPppMulticlassIfIndex = _JuniPppMlPppMulticlassIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 7, 1, 1),
    _JuniPppMlPppMulticlassIfIndex_Type()
)
juniPppMlPppMulticlassIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppMlPppMulticlassIfIndex.setStatus("current")


class _JuniPppMlPppMulticlassIndex_Type(Integer32):
    """Custom type juniPppMlPppMulticlassIndex based on Integer32"""
    defaultValue = 15


_JuniPppMlPppMulticlassIndex_Object = MibTableColumn
juniPppMlPppMulticlassIndex = _JuniPppMlPppMulticlassIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 7, 1, 2),
    _JuniPppMlPppMulticlassIndex_Type()
)
juniPppMlPppMulticlassIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniPppMlPppMulticlassIndex.setStatus("current")
_JuniPppMlPppMulticlassTcName_Type = JuniPppMlPppMulticlassTcName
_JuniPppMlPppMulticlassTcName_Object = MibTableColumn
juniPppMlPppMulticlassTcName = _JuniPppMlPppMulticlassTcName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 7, 1, 3),
    _JuniPppMlPppMulticlassTcName_Type()
)
juniPppMlPppMulticlassTcName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppMlPppMulticlassTcName.setStatus("current")


class _JuniPppMlPppMulticlassFragmentation_Type(JuniEnable):
    """Custom type juniPppMlPppMulticlassFragmentation based on JuniEnable"""


_JuniPppMlPppMulticlassFragmentation_Object = MibTableColumn
juniPppMlPppMulticlassFragmentation = _JuniPppMlPppMulticlassFragmentation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 7, 1, 4),
    _JuniPppMlPppMulticlassFragmentation_Type()
)
juniPppMlPppMulticlassFragmentation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppMlPppMulticlassFragmentation.setStatus("current")


class _JuniPppMlPppMulticlassReassembly_Type(JuniEnable):
    """Custom type juniPppMlPppMulticlassReassembly based on JuniEnable"""


_JuniPppMlPppMulticlassReassembly_Object = MibTableColumn
juniPppMlPppMulticlassReassembly = _JuniPppMlPppMulticlassReassembly_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 6, 7, 1, 5),
    _JuniPppMlPppMulticlassReassembly_Type()
)
juniPppMlPppMulticlassReassembly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppMlPppMulticlassReassembly.setStatus("current")
_JuniPppSummary_ObjectIdentity = ObjectIdentity
juniPppSummary = _JuniPppSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7)
)
_JuniPppSummaryPppInterfaceCount_Type = Integer32
_JuniPppSummaryPppInterfaceCount_Object = MibScalar
juniPppSummaryPppInterfaceCount = _JuniPppSummaryPppInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 1),
    _JuniPppSummaryPppInterfaceCount_Type()
)
juniPppSummaryPppInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppInterfaceCount.setStatus("current")
_JuniPppSummaryPppIpNCPs_Type = Integer32
_JuniPppSummaryPppIpNCPs_Object = MibScalar
juniPppSummaryPppIpNCPs = _JuniPppSummaryPppIpNCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 2),
    _JuniPppSummaryPppIpNCPs_Type()
)
juniPppSummaryPppIpNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpNCPs.setStatus("current")
_JuniPppSummaryPppOsiNCPs_Type = Integer32
_JuniPppSummaryPppOsiNCPs_Object = MibScalar
juniPppSummaryPppOsiNCPs = _JuniPppSummaryPppOsiNCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 3),
    _JuniPppSummaryPppOsiNCPs_Type()
)
juniPppSummaryPppOsiNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppOsiNCPs.setStatus("current")
_JuniPppSummaryPppIfAdminUp_Type = Integer32
_JuniPppSummaryPppIfAdminUp_Object = MibScalar
juniPppSummaryPppIfAdminUp = _JuniPppSummaryPppIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 4),
    _JuniPppSummaryPppIfAdminUp_Type()
)
juniPppSummaryPppIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIfAdminUp.setStatus("current")
_JuniPppSummaryPppIfAdminDown_Type = Integer32
_JuniPppSummaryPppIfAdminDown_Object = MibScalar
juniPppSummaryPppIfAdminDown = _JuniPppSummaryPppIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 5),
    _JuniPppSummaryPppIfAdminDown_Type()
)
juniPppSummaryPppIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIfAdminDown.setStatus("current")
_JuniPppSummaryPppIfOperUp_Type = Integer32
_JuniPppSummaryPppIfOperUp_Object = MibScalar
juniPppSummaryPppIfOperUp = _JuniPppSummaryPppIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 7),
    _JuniPppSummaryPppIfOperUp_Type()
)
juniPppSummaryPppIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIfOperUp.setStatus("current")
_JuniPppSummaryPppIfOperDown_Type = Integer32
_JuniPppSummaryPppIfOperDown_Object = MibScalar
juniPppSummaryPppIfOperDown = _JuniPppSummaryPppIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 8),
    _JuniPppSummaryPppIfOperDown_Type()
)
juniPppSummaryPppIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIfOperDown.setStatus("current")
_JuniPppSummaryPppIfOperDormant_Type = Integer32
_JuniPppSummaryPppIfOperDormant_Object = MibScalar
juniPppSummaryPppIfOperDormant = _JuniPppSummaryPppIfOperDormant_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 9),
    _JuniPppSummaryPppIfOperDormant_Type()
)
juniPppSummaryPppIfOperDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIfOperDormant.setStatus("current")
_JuniPppSummaryPppIfNotPresent_Type = Integer32
_JuniPppSummaryPppIfNotPresent_Object = MibScalar
juniPppSummaryPppIfNotPresent = _JuniPppSummaryPppIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 10),
    _JuniPppSummaryPppIfNotPresent_Type()
)
juniPppSummaryPppIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIfNotPresent.setStatus("current")
_JuniPppSummaryPppIfLowerLayerDown_Type = Integer32
_JuniPppSummaryPppIfLowerLayerDown_Object = MibScalar
juniPppSummaryPppIfLowerLayerDown = _JuniPppSummaryPppIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 11),
    _JuniPppSummaryPppIfLowerLayerDown_Type()
)
juniPppSummaryPppIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIfLowerLayerDown.setStatus("current")
_JuniPppSummaryPppIpNcpOpened_Type = Integer32
_JuniPppSummaryPppIpNcpOpened_Object = MibScalar
juniPppSummaryPppIpNcpOpened = _JuniPppSummaryPppIpNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 12),
    _JuniPppSummaryPppIpNcpOpened_Type()
)
juniPppSummaryPppIpNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpNcpOpened.setStatus("current")
_JuniPppSummaryPppIpNcpClosed_Type = Integer32
_JuniPppSummaryPppIpNcpClosed_Object = MibScalar
juniPppSummaryPppIpNcpClosed = _JuniPppSummaryPppIpNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 13),
    _JuniPppSummaryPppIpNcpClosed_Type()
)
juniPppSummaryPppIpNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpNcpClosed.setStatus("current")
_JuniPppSummaryPppOsiNcpOpened_Type = Integer32
_JuniPppSummaryPppOsiNcpOpened_Object = MibScalar
juniPppSummaryPppOsiNcpOpened = _JuniPppSummaryPppOsiNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 14),
    _JuniPppSummaryPppOsiNcpOpened_Type()
)
juniPppSummaryPppOsiNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppOsiNcpOpened.setStatus("current")
_JuniPppSummaryPppOsiNcpClosed_Type = Integer32
_JuniPppSummaryPppOsiNcpClosed_Object = MibScalar
juniPppSummaryPppOsiNcpClosed = _JuniPppSummaryPppOsiNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 15),
    _JuniPppSummaryPppOsiNcpClosed_Type()
)
juniPppSummaryPppOsiNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppOsiNcpClosed.setStatus("current")
_JuniPppSummaryPppIfLastChangeTime_Type = TimeTicks
_JuniPppSummaryPppIfLastChangeTime_Object = MibScalar
juniPppSummaryPppIfLastChangeTime = _JuniPppSummaryPppIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 16),
    _JuniPppSummaryPppIfLastChangeTime_Type()
)
juniPppSummaryPppIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIfLastChangeTime.setStatus("current")
_JuniPppSummaryPppLinkInterfaceCount_Type = Integer32
_JuniPppSummaryPppLinkInterfaceCount_Object = MibScalar
juniPppSummaryPppLinkInterfaceCount = _JuniPppSummaryPppLinkInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 17),
    _JuniPppSummaryPppLinkInterfaceCount_Type()
)
juniPppSummaryPppLinkInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppLinkInterfaceCount.setStatus("current")
_JuniPppSummaryPppLinkIfAdminUp_Type = Integer32
_JuniPppSummaryPppLinkIfAdminUp_Object = MibScalar
juniPppSummaryPppLinkIfAdminUp = _JuniPppSummaryPppLinkIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 18),
    _JuniPppSummaryPppLinkIfAdminUp_Type()
)
juniPppSummaryPppLinkIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppLinkIfAdminUp.setStatus("current")
_JuniPppSummaryPppLinkIfAdminDown_Type = Integer32
_JuniPppSummaryPppLinkIfAdminDown_Object = MibScalar
juniPppSummaryPppLinkIfAdminDown = _JuniPppSummaryPppLinkIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 19),
    _JuniPppSummaryPppLinkIfAdminDown_Type()
)
juniPppSummaryPppLinkIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppLinkIfAdminDown.setStatus("current")
_JuniPppSummaryPppLinkIfOperUp_Type = Integer32
_JuniPppSummaryPppLinkIfOperUp_Object = MibScalar
juniPppSummaryPppLinkIfOperUp = _JuniPppSummaryPppLinkIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 20),
    _JuniPppSummaryPppLinkIfOperUp_Type()
)
juniPppSummaryPppLinkIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppLinkIfOperUp.setStatus("current")
_JuniPppSummaryPppLinkIfOperDown_Type = Integer32
_JuniPppSummaryPppLinkIfOperDown_Object = MibScalar
juniPppSummaryPppLinkIfOperDown = _JuniPppSummaryPppLinkIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 21),
    _JuniPppSummaryPppLinkIfOperDown_Type()
)
juniPppSummaryPppLinkIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppLinkIfOperDown.setStatus("current")
_JuniPppSummaryPppLinkIfOperDormant_Type = Integer32
_JuniPppSummaryPppLinkIfOperDormant_Object = MibScalar
juniPppSummaryPppLinkIfOperDormant = _JuniPppSummaryPppLinkIfOperDormant_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 22),
    _JuniPppSummaryPppLinkIfOperDormant_Type()
)
juniPppSummaryPppLinkIfOperDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppLinkIfOperDormant.setStatus("current")
_JuniPppSummaryPppLinkIfNotPresent_Type = Integer32
_JuniPppSummaryPppLinkIfNotPresent_Object = MibScalar
juniPppSummaryPppLinkIfNotPresent = _JuniPppSummaryPppLinkIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 23),
    _JuniPppSummaryPppLinkIfNotPresent_Type()
)
juniPppSummaryPppLinkIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppLinkIfNotPresent.setStatus("current")
_JuniPppSummaryPppLinkIfLowerLayerDown_Type = Integer32
_JuniPppSummaryPppLinkIfLowerLayerDown_Object = MibScalar
juniPppSummaryPppLinkIfLowerLayerDown = _JuniPppSummaryPppLinkIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 24),
    _JuniPppSummaryPppLinkIfLowerLayerDown_Type()
)
juniPppSummaryPppLinkIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppLinkIfLowerLayerDown.setStatus("current")
_JuniPppSummaryPppLinkIfLastChangeTime_Type = TimeTicks
_JuniPppSummaryPppLinkIfLastChangeTime_Object = MibScalar
juniPppSummaryPppLinkIfLastChangeTime = _JuniPppSummaryPppLinkIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 25),
    _JuniPppSummaryPppLinkIfLastChangeTime_Type()
)
juniPppSummaryPppLinkIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppLinkIfLastChangeTime.setStatus("current")
_JuniPppSummaryPppNetworkInterfaceCount_Type = Integer32
_JuniPppSummaryPppNetworkInterfaceCount_Object = MibScalar
juniPppSummaryPppNetworkInterfaceCount = _JuniPppSummaryPppNetworkInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 26),
    _JuniPppSummaryPppNetworkInterfaceCount_Type()
)
juniPppSummaryPppNetworkInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkInterfaceCount.setStatus("current")
_JuniPppSummaryPppNetworkIpNCPs_Type = Integer32
_JuniPppSummaryPppNetworkIpNCPs_Object = MibScalar
juniPppSummaryPppNetworkIpNCPs = _JuniPppSummaryPppNetworkIpNCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 27),
    _JuniPppSummaryPppNetworkIpNCPs_Type()
)
juniPppSummaryPppNetworkIpNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpNCPs.setStatus("current")
_JuniPppSummaryPppNetworkOsiNCPs_Type = Integer32
_JuniPppSummaryPppNetworkOsiNCPs_Object = MibScalar
juniPppSummaryPppNetworkOsiNCPs = _JuniPppSummaryPppNetworkOsiNCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 28),
    _JuniPppSummaryPppNetworkOsiNCPs_Type()
)
juniPppSummaryPppNetworkOsiNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkOsiNCPs.setStatus("current")
_JuniPppSummaryPppNetworkIfAdminUp_Type = Integer32
_JuniPppSummaryPppNetworkIfAdminUp_Object = MibScalar
juniPppSummaryPppNetworkIfAdminUp = _JuniPppSummaryPppNetworkIfAdminUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 29),
    _JuniPppSummaryPppNetworkIfAdminUp_Type()
)
juniPppSummaryPppNetworkIfAdminUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIfAdminUp.setStatus("current")
_JuniPppSummaryPppNetworkIfAdminDown_Type = Integer32
_JuniPppSummaryPppNetworkIfAdminDown_Object = MibScalar
juniPppSummaryPppNetworkIfAdminDown = _JuniPppSummaryPppNetworkIfAdminDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 30),
    _JuniPppSummaryPppNetworkIfAdminDown_Type()
)
juniPppSummaryPppNetworkIfAdminDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIfAdminDown.setStatus("current")
_JuniPppSummaryPppNetworkIfOperUp_Type = Integer32
_JuniPppSummaryPppNetworkIfOperUp_Object = MibScalar
juniPppSummaryPppNetworkIfOperUp = _JuniPppSummaryPppNetworkIfOperUp_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 31),
    _JuniPppSummaryPppNetworkIfOperUp_Type()
)
juniPppSummaryPppNetworkIfOperUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIfOperUp.setStatus("current")
_JuniPppSummaryPppNetworkIfOperDown_Type = Integer32
_JuniPppSummaryPppNetworkIfOperDown_Object = MibScalar
juniPppSummaryPppNetworkIfOperDown = _JuniPppSummaryPppNetworkIfOperDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 32),
    _JuniPppSummaryPppNetworkIfOperDown_Type()
)
juniPppSummaryPppNetworkIfOperDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIfOperDown.setStatus("current")
_JuniPppSummaryPppNetworkIfOperDormant_Type = Integer32
_JuniPppSummaryPppNetworkIfOperDormant_Object = MibScalar
juniPppSummaryPppNetworkIfOperDormant = _JuniPppSummaryPppNetworkIfOperDormant_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 33),
    _JuniPppSummaryPppNetworkIfOperDormant_Type()
)
juniPppSummaryPppNetworkIfOperDormant.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIfOperDormant.setStatus("current")
_JuniPppSummaryPppNetworkIfNotPresent_Type = Integer32
_JuniPppSummaryPppNetworkIfNotPresent_Object = MibScalar
juniPppSummaryPppNetworkIfNotPresent = _JuniPppSummaryPppNetworkIfNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 34),
    _JuniPppSummaryPppNetworkIfNotPresent_Type()
)
juniPppSummaryPppNetworkIfNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIfNotPresent.setStatus("current")
_JuniPppSummaryPppNetworkIfLowerLayerDown_Type = Integer32
_JuniPppSummaryPppNetworkIfLowerLayerDown_Object = MibScalar
juniPppSummaryPppNetworkIfLowerLayerDown = _JuniPppSummaryPppNetworkIfLowerLayerDown_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 35),
    _JuniPppSummaryPppNetworkIfLowerLayerDown_Type()
)
juniPppSummaryPppNetworkIfLowerLayerDown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIfLowerLayerDown.setStatus("current")
_JuniPppSummaryPppNetworkIpNcpOpened_Type = Integer32
_JuniPppSummaryPppNetworkIpNcpOpened_Object = MibScalar
juniPppSummaryPppNetworkIpNcpOpened = _JuniPppSummaryPppNetworkIpNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 36),
    _JuniPppSummaryPppNetworkIpNcpOpened_Type()
)
juniPppSummaryPppNetworkIpNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpNcpOpened.setStatus("current")
_JuniPppSummaryPppNetworkIpNcpClosed_Type = Integer32
_JuniPppSummaryPppNetworkIpNcpClosed_Object = MibScalar
juniPppSummaryPppNetworkIpNcpClosed = _JuniPppSummaryPppNetworkIpNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 37),
    _JuniPppSummaryPppNetworkIpNcpClosed_Type()
)
juniPppSummaryPppNetworkIpNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpNcpClosed.setStatus("current")
_JuniPppSummaryPppNetworkOsiNcpOpened_Type = Integer32
_JuniPppSummaryPppNetworkOsiNcpOpened_Object = MibScalar
juniPppSummaryPppNetworkOsiNcpOpened = _JuniPppSummaryPppNetworkOsiNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 38),
    _JuniPppSummaryPppNetworkOsiNcpOpened_Type()
)
juniPppSummaryPppNetworkOsiNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkOsiNcpOpened.setStatus("current")
_JuniPppSummaryPppNetworkOsiNcpClosed_Type = Integer32
_JuniPppSummaryPppNetworkOsiNcpClosed_Object = MibScalar
juniPppSummaryPppNetworkOsiNcpClosed = _JuniPppSummaryPppNetworkOsiNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 39),
    _JuniPppSummaryPppNetworkOsiNcpClosed_Type()
)
juniPppSummaryPppNetworkOsiNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkOsiNcpClosed.setStatus("current")
_JuniPppSummaryPppNetworkIfLastChangeTime_Type = TimeTicks
_JuniPppSummaryPppNetworkIfLastChangeTime_Object = MibScalar
juniPppSummaryPppNetworkIfLastChangeTime = _JuniPppSummaryPppNetworkIfLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 40),
    _JuniPppSummaryPppNetworkIfLastChangeTime_Type()
)
juniPppSummaryPppNetworkIfLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIfLastChangeTime.setStatus("current")
_JuniPppSummaryPppIpv6NCPs_Type = Integer32
_JuniPppSummaryPppIpv6NCPs_Object = MibScalar
juniPppSummaryPppIpv6NCPs = _JuniPppSummaryPppIpv6NCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 41),
    _JuniPppSummaryPppIpv6NCPs_Type()
)
juniPppSummaryPppIpv6NCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpv6NCPs.setStatus("current")
_JuniPppSummaryPppIpv6NcpOpened_Type = Integer32
_JuniPppSummaryPppIpv6NcpOpened_Object = MibScalar
juniPppSummaryPppIpv6NcpOpened = _JuniPppSummaryPppIpv6NcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 42),
    _JuniPppSummaryPppIpv6NcpOpened_Type()
)
juniPppSummaryPppIpv6NcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpv6NcpOpened.setStatus("current")
_JuniPppSummaryPppIpv6NcpClosed_Type = Integer32
_JuniPppSummaryPppIpv6NcpClosed_Object = MibScalar
juniPppSummaryPppIpv6NcpClosed = _JuniPppSummaryPppIpv6NcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 43),
    _JuniPppSummaryPppIpv6NcpClosed_Type()
)
juniPppSummaryPppIpv6NcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpv6NcpClosed.setStatus("current")
_JuniPppSummaryPppNetworkIpv6NCPs_Type = Integer32
_JuniPppSummaryPppNetworkIpv6NCPs_Object = MibScalar
juniPppSummaryPppNetworkIpv6NCPs = _JuniPppSummaryPppNetworkIpv6NCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 44),
    _JuniPppSummaryPppNetworkIpv6NCPs_Type()
)
juniPppSummaryPppNetworkIpv6NCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpv6NCPs.setStatus("current")
_JuniPppSummaryPppNetworkIpv6NcpOpened_Type = Integer32
_JuniPppSummaryPppNetworkIpv6NcpOpened_Object = MibScalar
juniPppSummaryPppNetworkIpv6NcpOpened = _JuniPppSummaryPppNetworkIpv6NcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 45),
    _JuniPppSummaryPppNetworkIpv6NcpOpened_Type()
)
juniPppSummaryPppNetworkIpv6NcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpv6NcpOpened.setStatus("current")
_JuniPppSummaryPppNetworkIpv6NcpClosed_Type = Integer32
_JuniPppSummaryPppNetworkIpv6NcpClosed_Object = MibScalar
juniPppSummaryPppNetworkIpv6NcpClosed = _JuniPppSummaryPppNetworkIpv6NcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 46),
    _JuniPppSummaryPppNetworkIpv6NcpClosed_Type()
)
juniPppSummaryPppNetworkIpv6NcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpv6NcpClosed.setStatus("current")
_JuniPppSummaryPppStaticInterfaceCount_Type = Integer32
_JuniPppSummaryPppStaticInterfaceCount_Object = MibScalar
juniPppSummaryPppStaticInterfaceCount = _JuniPppSummaryPppStaticInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 47),
    _JuniPppSummaryPppStaticInterfaceCount_Type()
)
juniPppSummaryPppStaticInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppStaticInterfaceCount.setStatus("current")
_JuniPppSummaryPppMplsNCPs_Type = Integer32
_JuniPppSummaryPppMplsNCPs_Object = MibScalar
juniPppSummaryPppMplsNCPs = _JuniPppSummaryPppMplsNCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 48),
    _JuniPppSummaryPppMplsNCPs_Type()
)
juniPppSummaryPppMplsNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppMplsNCPs.setStatus("current")
_JuniPppSummaryPppIpAdminOpen_Type = Integer32
_JuniPppSummaryPppIpAdminOpen_Object = MibScalar
juniPppSummaryPppIpAdminOpen = _JuniPppSummaryPppIpAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 49),
    _JuniPppSummaryPppIpAdminOpen_Type()
)
juniPppSummaryPppIpAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpAdminOpen.setStatus("current")
_JuniPppSummaryPppIpAdminClose_Type = Integer32
_JuniPppSummaryPppIpAdminClose_Object = MibScalar
juniPppSummaryPppIpAdminClose = _JuniPppSummaryPppIpAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 50),
    _JuniPppSummaryPppIpAdminClose_Type()
)
juniPppSummaryPppIpAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpAdminClose.setStatus("current")
_JuniPppSummaryPppIpv6AdminOpen_Type = Integer32
_JuniPppSummaryPppIpv6AdminOpen_Object = MibScalar
juniPppSummaryPppIpv6AdminOpen = _JuniPppSummaryPppIpv6AdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 51),
    _JuniPppSummaryPppIpv6AdminOpen_Type()
)
juniPppSummaryPppIpv6AdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpv6AdminOpen.setStatus("current")
_JuniPppSummaryPppIpv6AdminClose_Type = Integer32
_JuniPppSummaryPppIpv6AdminClose_Object = MibScalar
juniPppSummaryPppIpv6AdminClose = _JuniPppSummaryPppIpv6AdminClose_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 52),
    _JuniPppSummaryPppIpv6AdminClose_Type()
)
juniPppSummaryPppIpv6AdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpv6AdminClose.setStatus("current")
_JuniPppSummaryPppOsiAdminOpen_Type = Integer32
_JuniPppSummaryPppOsiAdminOpen_Object = MibScalar
juniPppSummaryPppOsiAdminOpen = _JuniPppSummaryPppOsiAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 53),
    _JuniPppSummaryPppOsiAdminOpen_Type()
)
juniPppSummaryPppOsiAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppOsiAdminOpen.setStatus("current")
_JuniPppSummaryPppOsiAdminClose_Type = Integer32
_JuniPppSummaryPppOsiAdminClose_Object = MibScalar
juniPppSummaryPppOsiAdminClose = _JuniPppSummaryPppOsiAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 54),
    _JuniPppSummaryPppOsiAdminClose_Type()
)
juniPppSummaryPppOsiAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppOsiAdminClose.setStatus("current")
_JuniPppSummaryPppMplsAdminOpen_Type = Integer32
_JuniPppSummaryPppMplsAdminOpen_Object = MibScalar
juniPppSummaryPppMplsAdminOpen = _JuniPppSummaryPppMplsAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 55),
    _JuniPppSummaryPppMplsAdminOpen_Type()
)
juniPppSummaryPppMplsAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppMplsAdminOpen.setStatus("current")
_JuniPppSummaryPppMplsAdminClose_Type = Integer32
_JuniPppSummaryPppMplsAdminClose_Object = MibScalar
juniPppSummaryPppMplsAdminClose = _JuniPppSummaryPppMplsAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 56),
    _JuniPppSummaryPppMplsAdminClose_Type()
)
juniPppSummaryPppMplsAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppMplsAdminClose.setStatus("current")
_JuniPppSummaryPppIpNcpNotPresent_Type = Integer32
_JuniPppSummaryPppIpNcpNotPresent_Object = MibScalar
juniPppSummaryPppIpNcpNotPresent = _JuniPppSummaryPppIpNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 57),
    _JuniPppSummaryPppIpNcpNotPresent_Type()
)
juniPppSummaryPppIpNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpNcpNotPresent.setStatus("current")
_JuniPppSummaryPppIpNcpNoResources_Type = Integer32
_JuniPppSummaryPppIpNcpNoResources_Object = MibScalar
juniPppSummaryPppIpNcpNoResources = _JuniPppSummaryPppIpNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 58),
    _JuniPppSummaryPppIpNcpNoResources_Type()
)
juniPppSummaryPppIpNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpNcpNoResources.setStatus("current")
_JuniPppSummaryPppIpv6NcpNotPresent_Type = Integer32
_JuniPppSummaryPppIpv6NcpNotPresent_Object = MibScalar
juniPppSummaryPppIpv6NcpNotPresent = _JuniPppSummaryPppIpv6NcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 59),
    _JuniPppSummaryPppIpv6NcpNotPresent_Type()
)
juniPppSummaryPppIpv6NcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpv6NcpNotPresent.setStatus("current")
_JuniPppSummaryPppIpv6NcpNoResources_Type = Integer32
_JuniPppSummaryPppIpv6NcpNoResources_Object = MibScalar
juniPppSummaryPppIpv6NcpNoResources = _JuniPppSummaryPppIpv6NcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 60),
    _JuniPppSummaryPppIpv6NcpNoResources_Type()
)
juniPppSummaryPppIpv6NcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppIpv6NcpNoResources.setStatus("current")
_JuniPppSummaryPppOsiNcpNotPresent_Type = Integer32
_JuniPppSummaryPppOsiNcpNotPresent_Object = MibScalar
juniPppSummaryPppOsiNcpNotPresent = _JuniPppSummaryPppOsiNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 61),
    _JuniPppSummaryPppOsiNcpNotPresent_Type()
)
juniPppSummaryPppOsiNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppOsiNcpNotPresent.setStatus("current")
_JuniPppSummaryPppOsiNcpNoResources_Type = Integer32
_JuniPppSummaryPppOsiNcpNoResources_Object = MibScalar
juniPppSummaryPppOsiNcpNoResources = _JuniPppSummaryPppOsiNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 62),
    _JuniPppSummaryPppOsiNcpNoResources_Type()
)
juniPppSummaryPppOsiNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppOsiNcpNoResources.setStatus("current")
_JuniPppSummaryPppMplsNcpOpened_Type = Integer32
_JuniPppSummaryPppMplsNcpOpened_Object = MibScalar
juniPppSummaryPppMplsNcpOpened = _JuniPppSummaryPppMplsNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 63),
    _JuniPppSummaryPppMplsNcpOpened_Type()
)
juniPppSummaryPppMplsNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppMplsNcpOpened.setStatus("current")
_JuniPppSummaryPppMplsNcpClosed_Type = Integer32
_JuniPppSummaryPppMplsNcpClosed_Object = MibScalar
juniPppSummaryPppMplsNcpClosed = _JuniPppSummaryPppMplsNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 64),
    _JuniPppSummaryPppMplsNcpClosed_Type()
)
juniPppSummaryPppMplsNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppMplsNcpClosed.setStatus("current")
_JuniPppSummaryPppMplsNcpNotPresent_Type = Integer32
_JuniPppSummaryPppMplsNcpNotPresent_Object = MibScalar
juniPppSummaryPppMplsNcpNotPresent = _JuniPppSummaryPppMplsNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 65),
    _JuniPppSummaryPppMplsNcpNotPresent_Type()
)
juniPppSummaryPppMplsNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppMplsNcpNotPresent.setStatus("current")
_JuniPppSummaryPppMplsNcpNoResources_Type = Integer32
_JuniPppSummaryPppMplsNcpNoResources_Object = MibScalar
juniPppSummaryPppMplsNcpNoResources = _JuniPppSummaryPppMplsNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 66),
    _JuniPppSummaryPppMplsNcpNoResources_Type()
)
juniPppSummaryPppMplsNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppMplsNcpNoResources.setStatus("current")
_JuniPppSummaryPppLinkStaticInterfaceCount_Type = Integer32
_JuniPppSummaryPppLinkStaticInterfaceCount_Object = MibScalar
juniPppSummaryPppLinkStaticInterfaceCount = _JuniPppSummaryPppLinkStaticInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 67),
    _JuniPppSummaryPppLinkStaticInterfaceCount_Type()
)
juniPppSummaryPppLinkStaticInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppLinkStaticInterfaceCount.setStatus("current")
_JuniPppSummaryPppNetworkStaticInterfaceCount_Type = Integer32
_JuniPppSummaryPppNetworkStaticInterfaceCount_Object = MibScalar
juniPppSummaryPppNetworkStaticInterfaceCount = _JuniPppSummaryPppNetworkStaticInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 68),
    _JuniPppSummaryPppNetworkStaticInterfaceCount_Type()
)
juniPppSummaryPppNetworkStaticInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkStaticInterfaceCount.setStatus("current")
_JuniPppSummaryPppNetworkMplsNCPs_Type = Integer32
_JuniPppSummaryPppNetworkMplsNCPs_Object = MibScalar
juniPppSummaryPppNetworkMplsNCPs = _JuniPppSummaryPppNetworkMplsNCPs_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 69),
    _JuniPppSummaryPppNetworkMplsNCPs_Type()
)
juniPppSummaryPppNetworkMplsNCPs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkMplsNCPs.setStatus("current")
_JuniPppSummaryPppNetworkIpAdminOpen_Type = Integer32
_JuniPppSummaryPppNetworkIpAdminOpen_Object = MibScalar
juniPppSummaryPppNetworkIpAdminOpen = _JuniPppSummaryPppNetworkIpAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 70),
    _JuniPppSummaryPppNetworkIpAdminOpen_Type()
)
juniPppSummaryPppNetworkIpAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpAdminOpen.setStatus("current")
_JuniPppSummaryPppNetworkIpAdminClose_Type = Integer32
_JuniPppSummaryPppNetworkIpAdminClose_Object = MibScalar
juniPppSummaryPppNetworkIpAdminClose = _JuniPppSummaryPppNetworkIpAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 71),
    _JuniPppSummaryPppNetworkIpAdminClose_Type()
)
juniPppSummaryPppNetworkIpAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpAdminClose.setStatus("current")
_JuniPppSummaryPppNetworkIpv6AdminOpen_Type = Integer32
_JuniPppSummaryPppNetworkIpv6AdminOpen_Object = MibScalar
juniPppSummaryPppNetworkIpv6AdminOpen = _JuniPppSummaryPppNetworkIpv6AdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 72),
    _JuniPppSummaryPppNetworkIpv6AdminOpen_Type()
)
juniPppSummaryPppNetworkIpv6AdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpv6AdminOpen.setStatus("current")
_JuniPppSummaryPppNetworkIpv6AdminClose_Type = Integer32
_JuniPppSummaryPppNetworkIpv6AdminClose_Object = MibScalar
juniPppSummaryPppNetworkIpv6AdminClose = _JuniPppSummaryPppNetworkIpv6AdminClose_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 73),
    _JuniPppSummaryPppNetworkIpv6AdminClose_Type()
)
juniPppSummaryPppNetworkIpv6AdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpv6AdminClose.setStatus("current")
_JuniPppSummaryPppNetworkOsiAdminOpen_Type = Integer32
_JuniPppSummaryPppNetworkOsiAdminOpen_Object = MibScalar
juniPppSummaryPppNetworkOsiAdminOpen = _JuniPppSummaryPppNetworkOsiAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 74),
    _JuniPppSummaryPppNetworkOsiAdminOpen_Type()
)
juniPppSummaryPppNetworkOsiAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkOsiAdminOpen.setStatus("current")
_JuniPppSummaryPppNetworkOsiAdminClose_Type = Integer32
_JuniPppSummaryPppNetworkOsiAdminClose_Object = MibScalar
juniPppSummaryPppNetworkOsiAdminClose = _JuniPppSummaryPppNetworkOsiAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 75),
    _JuniPppSummaryPppNetworkOsiAdminClose_Type()
)
juniPppSummaryPppNetworkOsiAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkOsiAdminClose.setStatus("current")
_JuniPppSummaryPppNetworkMplsAdminOpen_Type = Integer32
_JuniPppSummaryPppNetworkMplsAdminOpen_Object = MibScalar
juniPppSummaryPppNetworkMplsAdminOpen = _JuniPppSummaryPppNetworkMplsAdminOpen_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 76),
    _JuniPppSummaryPppNetworkMplsAdminOpen_Type()
)
juniPppSummaryPppNetworkMplsAdminOpen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkMplsAdminOpen.setStatus("current")
_JuniPppSummaryPppNetworkMplsAdminClose_Type = Integer32
_JuniPppSummaryPppNetworkMplsAdminClose_Object = MibScalar
juniPppSummaryPppNetworkMplsAdminClose = _JuniPppSummaryPppNetworkMplsAdminClose_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 77),
    _JuniPppSummaryPppNetworkMplsAdminClose_Type()
)
juniPppSummaryPppNetworkMplsAdminClose.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkMplsAdminClose.setStatus("current")
_JuniPppSummaryPppNetworkIpNcpNotPresent_Type = Integer32
_JuniPppSummaryPppNetworkIpNcpNotPresent_Object = MibScalar
juniPppSummaryPppNetworkIpNcpNotPresent = _JuniPppSummaryPppNetworkIpNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 78),
    _JuniPppSummaryPppNetworkIpNcpNotPresent_Type()
)
juniPppSummaryPppNetworkIpNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpNcpNotPresent.setStatus("current")
_JuniPppSummaryPppNetworkIpNcpNoResources_Type = Integer32
_JuniPppSummaryPppNetworkIpNcpNoResources_Object = MibScalar
juniPppSummaryPppNetworkIpNcpNoResources = _JuniPppSummaryPppNetworkIpNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 79),
    _JuniPppSummaryPppNetworkIpNcpNoResources_Type()
)
juniPppSummaryPppNetworkIpNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpNcpNoResources.setStatus("current")
_JuniPppSummaryPppNetworkIpv6NcpNotPresent_Type = Integer32
_JuniPppSummaryPppNetworkIpv6NcpNotPresent_Object = MibScalar
juniPppSummaryPppNetworkIpv6NcpNotPresent = _JuniPppSummaryPppNetworkIpv6NcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 80),
    _JuniPppSummaryPppNetworkIpv6NcpNotPresent_Type()
)
juniPppSummaryPppNetworkIpv6NcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpv6NcpNotPresent.setStatus("current")
_JuniPppSummaryPppNetworkIpv6NcpNoResources_Type = Integer32
_JuniPppSummaryPppNetworkIpv6NcpNoResources_Object = MibScalar
juniPppSummaryPppNetworkIpv6NcpNoResources = _JuniPppSummaryPppNetworkIpv6NcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 81),
    _JuniPppSummaryPppNetworkIpv6NcpNoResources_Type()
)
juniPppSummaryPppNetworkIpv6NcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkIpv6NcpNoResources.setStatus("current")
_JuniPppSummaryPppNetworkOsiNcpNotPresent_Type = Integer32
_JuniPppSummaryPppNetworkOsiNcpNotPresent_Object = MibScalar
juniPppSummaryPppNetworkOsiNcpNotPresent = _JuniPppSummaryPppNetworkOsiNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 82),
    _JuniPppSummaryPppNetworkOsiNcpNotPresent_Type()
)
juniPppSummaryPppNetworkOsiNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkOsiNcpNotPresent.setStatus("current")
_JuniPppSummaryPppNetworkOsiNcpNoResources_Type = Integer32
_JuniPppSummaryPppNetworkOsiNcpNoResources_Object = MibScalar
juniPppSummaryPppNetworkOsiNcpNoResources = _JuniPppSummaryPppNetworkOsiNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 83),
    _JuniPppSummaryPppNetworkOsiNcpNoResources_Type()
)
juniPppSummaryPppNetworkOsiNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkOsiNcpNoResources.setStatus("current")
_JuniPppSummaryPppNetworkMplsNcpOpened_Type = Integer32
_JuniPppSummaryPppNetworkMplsNcpOpened_Object = MibScalar
juniPppSummaryPppNetworkMplsNcpOpened = _JuniPppSummaryPppNetworkMplsNcpOpened_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 84),
    _JuniPppSummaryPppNetworkMplsNcpOpened_Type()
)
juniPppSummaryPppNetworkMplsNcpOpened.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkMplsNcpOpened.setStatus("current")
_JuniPppSummaryPppNetworkMplsNcpClosed_Type = Integer32
_JuniPppSummaryPppNetworkMplsNcpClosed_Object = MibScalar
juniPppSummaryPppNetworkMplsNcpClosed = _JuniPppSummaryPppNetworkMplsNcpClosed_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 85),
    _JuniPppSummaryPppNetworkMplsNcpClosed_Type()
)
juniPppSummaryPppNetworkMplsNcpClosed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkMplsNcpClosed.setStatus("current")
_JuniPppSummaryPppNetworkMplsNcpNotPresent_Type = Integer32
_JuniPppSummaryPppNetworkMplsNcpNotPresent_Object = MibScalar
juniPppSummaryPppNetworkMplsNcpNotPresent = _JuniPppSummaryPppNetworkMplsNcpNotPresent_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 86),
    _JuniPppSummaryPppNetworkMplsNcpNotPresent_Type()
)
juniPppSummaryPppNetworkMplsNcpNotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkMplsNcpNotPresent.setStatus("current")
_JuniPppSummaryPppNetworkMplsNcpNoResources_Type = Integer32
_JuniPppSummaryPppNetworkMplsNcpNoResources_Object = MibScalar
juniPppSummaryPppNetworkMplsNcpNoResources = _JuniPppSummaryPppNetworkMplsNcpNoResources_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 7, 87),
    _JuniPppSummaryPppNetworkMplsNcpNoResources_Type()
)
juniPppSummaryPppNetworkMplsNcpNoResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppSummaryPppNetworkMplsNcpNoResources.setStatus("current")
_JuniPppIpv6_ObjectIdentity = ObjectIdentity
juniPppIpv6 = _JuniPppIpv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8)
)
_JuniPppIpv6Table_Object = MibTable
juniPppIpv6Table = _JuniPppIpv6Table_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 1)
)
if mibBuilder.loadTexts:
    juniPppIpv6Table.setStatus("current")
_JuniPppIpv6Entry_Object = MibTableRow
juniPppIpv6Entry = _JuniPppIpv6Entry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 1, 1)
)
juniPppIpv6Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniPppIpv6Entry.setStatus("current")
_JuniPppIpv6ServiceStatus_Type = JuniEnable
_JuniPppIpv6ServiceStatus_Object = MibTableColumn
juniPppIpv6ServiceStatus = _JuniPppIpv6ServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 1, 1, 1),
    _JuniPppIpv6ServiceStatus_Type()
)
juniPppIpv6ServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpv6ServiceStatus.setStatus("current")


class _JuniPppIpv6OperStatus_Type(Integer32):
    """Custom type juniPppIpv6OperStatus based on Integer32"""
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


_JuniPppIpv6OperStatus_Type.__name__ = "Integer32"
_JuniPppIpv6OperStatus_Object = MibTableColumn
juniPppIpv6OperStatus = _JuniPppIpv6OperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 1, 1, 2),
    _JuniPppIpv6OperStatus_Type()
)
juniPppIpv6OperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpv6OperStatus.setStatus("current")


class _JuniPppIpv6TerminateReason_Type(Integer32):
    """Custom type juniPppIpv6TerminateReason based on Integer32"""
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


_JuniPppIpv6TerminateReason_Type.__name__ = "Integer32"
_JuniPppIpv6TerminateReason_Object = MibTableColumn
juniPppIpv6TerminateReason = _JuniPppIpv6TerminateReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 1, 1, 3),
    _JuniPppIpv6TerminateReason_Type()
)
juniPppIpv6TerminateReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpv6TerminateReason.setStatus("current")


class _JuniPppIpv6TerminateNegFailOption_Type(Integer32):
    """Custom type juniPppIpv6TerminateNegFailOption based on Integer32"""
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


_JuniPppIpv6TerminateNegFailOption_Type.__name__ = "Integer32"
_JuniPppIpv6TerminateNegFailOption_Object = MibTableColumn
juniPppIpv6TerminateNegFailOption = _JuniPppIpv6TerminateNegFailOption_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 1, 1, 4),
    _JuniPppIpv6TerminateNegFailOption_Type()
)
juniPppIpv6TerminateNegFailOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpv6TerminateNegFailOption.setStatus("current")
_JuniPppIpv6LocalIpv6AddressIfIdentifier_Type = Ipv6AddressIfIdentifier
_JuniPppIpv6LocalIpv6AddressIfIdentifier_Object = MibTableColumn
juniPppIpv6LocalIpv6AddressIfIdentifier = _JuniPppIpv6LocalIpv6AddressIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 1, 1, 5),
    _JuniPppIpv6LocalIpv6AddressIfIdentifier_Type()
)
juniPppIpv6LocalIpv6AddressIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpv6LocalIpv6AddressIfIdentifier.setStatus("current")
_JuniPppIpv6RemoteIpv6AddressIfIdentifier_Type = Ipv6AddressIfIdentifier
_JuniPppIpv6RemoteIpv6AddressIfIdentifier_Object = MibTableColumn
juniPppIpv6RemoteIpv6AddressIfIdentifier = _JuniPppIpv6RemoteIpv6AddressIfIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 1, 1, 6),
    _JuniPppIpv6RemoteIpv6AddressIfIdentifier_Type()
)
juniPppIpv6RemoteIpv6AddressIfIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpv6RemoteIpv6AddressIfIdentifier.setStatus("current")
_JuniPppIpv6NetworkStatusIpv6cpRenegoTerminates_Type = Counter32
_JuniPppIpv6NetworkStatusIpv6cpRenegoTerminates_Object = MibTableColumn
juniPppIpv6NetworkStatusIpv6cpRenegoTerminates = _JuniPppIpv6NetworkStatusIpv6cpRenegoTerminates_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 1, 1, 7),
    _JuniPppIpv6NetworkStatusIpv6cpRenegoTerminates_Type()
)
juniPppIpv6NetworkStatusIpv6cpRenegoTerminates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniPppIpv6NetworkStatusIpv6cpRenegoTerminates.setStatus("current")
_JuniPppIpv6ConfigTable_Object = MibTable
juniPppIpv6ConfigTable = _JuniPppIpv6ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 2)
)
if mibBuilder.loadTexts:
    juniPppIpv6ConfigTable.setStatus("current")
_JuniPppIpv6ConfigEntry_Object = MibTableRow
juniPppIpv6ConfigEntry = _JuniPppIpv6ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 2, 1)
)
juniPppIpv6ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    juniPppIpv6ConfigEntry.setStatus("current")


class _JuniPppIpv6ConfigAdminStatus_Type(Integer32):
    """Custom type juniPppIpv6ConfigAdminStatus based on Integer32"""
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


_JuniPppIpv6ConfigAdminStatus_Type.__name__ = "Integer32"
_JuniPppIpv6ConfigAdminStatus_Object = MibTableColumn
juniPppIpv6ConfigAdminStatus = _JuniPppIpv6ConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 2, 1, 1),
    _JuniPppIpv6ConfigAdminStatus_Type()
)
juniPppIpv6ConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppIpv6ConfigAdminStatus.setStatus("current")


class _JuniPppIpv6ConfigInitiateIpv6_Type(JuniEnable):
    """Custom type juniPppIpv6ConfigInitiateIpv6 based on JuniEnable"""


_JuniPppIpv6ConfigInitiateIpv6_Object = MibTableColumn
juniPppIpv6ConfigInitiateIpv6 = _JuniPppIpv6ConfigInitiateIpv6_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 2, 1, 2),
    _JuniPppIpv6ConfigInitiateIpv6_Type()
)
juniPppIpv6ConfigInitiateIpv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppIpv6ConfigInitiateIpv6.setStatus("current")


class _JuniPppIpv6ConfigMaxIpv6cpRenegotiation_Type(Integer32):
    """Custom type juniPppIpv6ConfigMaxIpv6cpRenegotiation based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_JuniPppIpv6ConfigMaxIpv6cpRenegotiation_Type.__name__ = "Integer32"
_JuniPppIpv6ConfigMaxIpv6cpRenegotiation_Object = MibTableColumn
juniPppIpv6ConfigMaxIpv6cpRenegotiation = _JuniPppIpv6ConfigMaxIpv6cpRenegotiation_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 8, 2, 1, 3),
    _JuniPppIpv6ConfigMaxIpv6cpRenegotiation_Type()
)
juniPppIpv6ConfigMaxIpv6cpRenegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppIpv6ConfigMaxIpv6cpRenegotiation.setStatus("current")
_JuniPppGlobalConfig_ObjectIdentity = ObjectIdentity
juniPppGlobalConfig = _JuniPppGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 9)
)
_JuniPppPeerIpAddressOptional_Type = JuniEnable
_JuniPppPeerIpAddressOptional_Object = MibScalar
juniPppPeerIpAddressOptional = _JuniPppPeerIpAddressOptional_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 1, 9, 1),
    _JuniPppPeerIpAddressOptional_Type()
)
juniPppPeerIpAddressOptional.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniPppPeerIpAddressOptional.setStatus("current")
_JuniPppConformance_ObjectIdentity = ObjectIdentity
juniPppConformance = _JuniPppConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4)
)
_JuniPppCompliances_ObjectIdentity = ObjectIdentity
juniPppCompliances = _JuniPppCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1)
)
_JuniPppGroups_ObjectIdentity = ObjectIdentity
juniPppGroups = _JuniPppGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2)
)

# Managed Objects groups

juniPppLcpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 1)
)
juniPppLcpGroup.setObjects(
      *(("Juniper-PPP-MIB", "juniPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    juniPppLcpGroup.setStatus("obsolete")

juniPppIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 2)
)
juniPppIpGroup.setObjects(
    ("Juniper-PPP-MIB", "juniPppIpServiceStatus")
)
if mibBuilder.loadTexts:
    juniPppIpGroup.setStatus("obsolete")

juniPppOsiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 3)
)
juniPppOsiGroup.setObjects(
      *(("Juniper-PPP-MIB", "juniPppOsiServiceStatus"),
        ("Juniper-PPP-MIB", "juniPppOsiOperStatus"),
        ("Juniper-PPP-MIB", "juniPppOsiConfigAdminStatus"))
)
if mibBuilder.loadTexts:
    juniPppOsiGroup.setStatus("obsolete")

juniPppLcpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 4)
)
juniPppLcpGroup2.setObjects(
      *(("Juniper-PPP-MIB", "juniPppLinkStatusTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusKeepaliveFailures"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusRemoteMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTunnelIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    juniPppLcpGroup2.setStatus("obsolete")

juniPppIpGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 5)
)
juniPppIpGroup2.setObjects(
      *(("Juniper-PPP-MIB", "juniPppIpServiceStatus"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppIpLocalIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerDnsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerWinsPriority"))
)
if mibBuilder.loadTexts:
    juniPppIpGroup2.setStatus("obsolete")

juniPppOsiGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 6)
)
juniPppOsiGroup2.setObjects(
      *(("Juniper-PPP-MIB", "juniPppOsiServiceStatus"),
        ("Juniper-PPP-MIB", "juniPppOsiOperStatus"),
        ("Juniper-PPP-MIB", "juniPppOsiTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppOsiTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppOsiLocalAlignNpdu"),
        ("Juniper-PPP-MIB", "juniPppOsiRemoteAlignNpdu"),
        ("Juniper-PPP-MIB", "juniPppOsiConfigAdminStatus"))
)
if mibBuilder.loadTexts:
    juniPppOsiGroup2.setStatus("current")

juniPppSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 7)
)
juniPppSessionGroup.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSessionGrant"),
        ("Juniper-PPP-MIB", "juniPppSessionTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppSessionStartTime"),
        ("Juniper-PPP-MIB", "juniPppSessionInOctets"),
        ("Juniper-PPP-MIB", "juniPppSessionOutOctets"),
        ("Juniper-PPP-MIB", "juniPppSessionInPackets"),
        ("Juniper-PPP-MIB", "juniPppSessionOutPackets"),
        ("Juniper-PPP-MIB", "juniPppSessionSessionTimeout"),
        ("Juniper-PPP-MIB", "juniPppSessionInactivityTimeout"),
        ("Juniper-PPP-MIB", "juniPppSessionAccountingInterval"),
        ("Juniper-PPP-MIB", "juniPppSessionRemoteIpAddress"),
        ("Juniper-PPP-MIB", "juniPppSessionRemotePrimaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppSessionRemoteSecondaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppSessionRemotePrimaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppSessionRemoteSecondaryWinsAddress"))
)
if mibBuilder.loadTexts:
    juniPppSessionGroup.setStatus("obsolete")

juniPppMlPppGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 8)
)
juniPppMlPppGroup.setObjects(
      *(("Juniper-PPP-MIB", "juniPppMlPppBundleRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextLinkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkBundleName"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBindRowStatus"))
)
if mibBuilder.loadTexts:
    juniPppMlPppGroup.setStatus("obsolete")

juniPppSummaryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 9)
)
juniPppSummaryGroup.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSummaryPppInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfLastChangeTime"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfLastChangeTime"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfLastChangeTime"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNcpClosed"))
)
if mibBuilder.loadTexts:
    juniPppSummaryGroup.setStatus("obsolete")

juniPppLcpGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 10)
)
juniPppLcpGroup3.setObjects(
      *(("Juniper-PPP-MIB", "juniPppLinkStatusTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusKeepaliveFailures"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusRemoteMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTunnelIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigStandardIfIndex"),
        ("Juniper-PPP-MIB", "juniPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    juniPppLcpGroup3.setStatus("obsolete")

juniPppSummaryBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 11)
)
juniPppSummaryBasicGroup.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSummaryPppInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfLastChangeTime"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNcpClosed"))
)
if mibBuilder.loadTexts:
    juniPppSummaryBasicGroup.setStatus("obsolete")

juniPppSummaryLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 12)
)
juniPppSummaryLinkGroup.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSummaryPppLinkInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfLastChangeTime"))
)
if mibBuilder.loadTexts:
    juniPppSummaryLinkGroup.setStatus("obsolete")

juniPppSummaryNetworkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 13)
)
juniPppSummaryNetworkGroup.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSummaryPppNetworkInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfLastChangeTime"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNcpClosed"))
)
if mibBuilder.loadTexts:
    juniPppSummaryNetworkGroup.setStatus("obsolete")

juniPppLcpGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 14)
)
juniPppLcpGroup4.setObjects(
      *(("Juniper-PPP-MIB", "juniPppLinkStatusTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusKeepaliveFailures"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusRemoteMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTunnelIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigStandardIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    juniPppLcpGroup4.setStatus("obsolete")

juniPppIpGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 15)
)
juniPppIpGroup3.setObjects(
      *(("Juniper-PPP-MIB", "juniPppIpServiceStatus"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppIpLocalIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerDnsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerWinsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigIpcpNetmask"))
)
if mibBuilder.loadTexts:
    juniPppIpGroup3.setStatus("obsolete")

juniPppMlPppGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 16)
)
juniPppMlPppGroup2.setObjects(
      *(("Juniper-PPP-MIB", "juniPppMlPppBundleRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBundleNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextLinkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkBundleName"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBindRowStatus"))
)
if mibBuilder.loadTexts:
    juniPppMlPppGroup2.setStatus("obsolete")

juniPppMlPppGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 17)
)
juniPppMlPppGroup3.setObjects(
      *(("Juniper-PPP-MIB", "juniPppMlPppBundleRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBundleNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextLinkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkBundleName"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBindRowStatus"))
)
if mibBuilder.loadTexts:
    juniPppMlPppGroup3.setStatus("obsolete")

juniPppLcpGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 18)
)
juniPppLcpGroup5.setObjects(
      *(("Juniper-PPP-MIB", "juniPppLinkStatusTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusKeepaliveFailures"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusRemoteMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTunnelIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigStandardIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    juniPppLcpGroup5.setStatus("obsolete")

juniPppMlPppGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 19)
)
juniPppMlPppGroup4.setObjects(
      *(("Juniper-PPP-MIB", "juniPppMlPppBundleRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBundleNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextLinkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkBundleName"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBindRowStatus"))
)
if mibBuilder.loadTexts:
    juniPppMlPppGroup4.setStatus("obsolete")

juniPppSummaryBasicGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 20)
)
juniPppSummaryBasicGroup2.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSummaryPppInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfLastChangeTime"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpv6NCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpv6NcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpv6NcpClosed"))
)
if mibBuilder.loadTexts:
    juniPppSummaryBasicGroup2.setStatus("obsolete")

juniPppSummaryNetworkGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 21)
)
juniPppSummaryNetworkGroup2.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSummaryPppNetworkInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfLastChangeTime"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpv6NCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpv6NcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpv6NcpClosed"))
)
if mibBuilder.loadTexts:
    juniPppSummaryNetworkGroup2.setStatus("obsolete")

juniPppIpGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 22)
)
juniPppIpGroup4.setObjects(
      *(("Juniper-PPP-MIB", "juniPppIpServiceStatus"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppIpLocalIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerDnsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerWinsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigIpcpNetmask"),
        ("Juniper-PPP-MIB", "juniPppIpConfigInitiateIp"))
)
if mibBuilder.loadTexts:
    juniPppIpGroup4.setStatus("obsolete")

juniPppIpv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 23)
)
juniPppIpv6Group.setObjects(
      *(("Juniper-PPP-MIB", "juniPppIpv6ServiceStatus"),
        ("Juniper-PPP-MIB", "juniPppIpv6OperStatus"),
        ("Juniper-PPP-MIB", "juniPppIpv6TerminateReason"),
        ("Juniper-PPP-MIB", "juniPppIpv6TerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppIpv6LocalIpv6AddressIfIdentifier"),
        ("Juniper-PPP-MIB", "juniPppIpv6RemoteIpv6AddressIfIdentifier"),
        ("Juniper-PPP-MIB", "juniPppIpv6ConfigAdminStatus"),
        ("Juniper-PPP-MIB", "juniPppIpv6ConfigInitiateIpv6"))
)
if mibBuilder.loadTexts:
    juniPppIpv6Group.setStatus("obsolete")

juniPppSessionGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 24)
)
juniPppSessionGroup2.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSessionGrant"),
        ("Juniper-PPP-MIB", "juniPppSessionTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppSessionStartTime"),
        ("Juniper-PPP-MIB", "juniPppSessionInOctets"),
        ("Juniper-PPP-MIB", "juniPppSessionOutOctets"),
        ("Juniper-PPP-MIB", "juniPppSessionInPackets"),
        ("Juniper-PPP-MIB", "juniPppSessionOutPackets"),
        ("Juniper-PPP-MIB", "juniPppSessionSessionTimeout"),
        ("Juniper-PPP-MIB", "juniPppSessionInactivityTimeout"),
        ("Juniper-PPP-MIB", "juniPppSessionAccountingInterval"),
        ("Juniper-PPP-MIB", "juniPppSessionRemoteIpAddress"),
        ("Juniper-PPP-MIB", "juniPppSessionRemotePrimaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppSessionRemoteSecondaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppSessionRemotePrimaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppSessionRemoteSecondaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppSessionRemoteIpv6AddressIfIdentifier"),
        ("Juniper-PPP-MIB", "juniPppSessionInhibitIp"),
        ("Juniper-PPP-MIB", "juniPppSessionInhibitIpv6"))
)
if mibBuilder.loadTexts:
    juniPppSessionGroup2.setStatus("current")

juniPppMlPppGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 25)
)
juniPppMlPppGroup5.setObjects(
      *(("Juniper-PPP-MIB", "juniPppMlPppBundleRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBundleNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextLinkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigFragmentation"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigReassembly"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigFragmentSize"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkBundleName"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBindRowStatus"))
)
if mibBuilder.loadTexts:
    juniPppMlPppGroup5.setStatus("obsolete")

juniPppSummaryBasicGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 26)
)
juniPppSummaryBasicGroup3.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSummaryPppInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppStaticInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpv6NCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppMplsNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpAdminOpen"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpAdminClose"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpv6AdminOpen"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpv6AdminClose"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiAdminOpen"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiAdminClose"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppMplsAdminOpen"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppMplsAdminClose"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNcpNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpNcpNoResources"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpv6NcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpv6NcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpv6NcpNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIpv6NcpNoResources"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNcpNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppOsiNcpNoResources"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppMplsNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppMplsNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppMplsNcpNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppMplsNcpNoResources"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppIfLastChangeTime"))
)
if mibBuilder.loadTexts:
    juniPppSummaryBasicGroup3.setStatus("current")

juniPppSummaryLinkGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 27)
)
juniPppSummaryLinkGroup2.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSummaryPppLinkInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkStaticInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppLinkIfLastChangeTime"))
)
if mibBuilder.loadTexts:
    juniPppSummaryLinkGroup2.setStatus("current")

juniPppSummaryNetworkGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 28)
)
juniPppSummaryNetworkGroup3.setObjects(
      *(("Juniper-PPP-MIB", "juniPppSummaryPppNetworkInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkStaticInterfaceCount"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpv6NCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkMplsNCPs"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfAdminUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfAdminDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpAdminOpen"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpAdminClose"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpv6AdminOpen"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpv6AdminClose"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiAdminOpen"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiAdminClose"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkMplsAdminOpen"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkMplsAdminClose"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperUp"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfOperDormant"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfLowerLayerDown"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNcpNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpNcpNoResources"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpv6NcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpv6NcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpv6NcpNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIpv6NcpNoResources"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNcpNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkOsiNcpNoResources"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkMplsNcpOpened"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkMplsNcpClosed"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkMplsNcpNotPresent"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkMplsNcpNoResources"),
        ("Juniper-PPP-MIB", "juniPppSummaryPppNetworkIfLastChangeTime"))
)
if mibBuilder.loadTexts:
    juniPppSummaryNetworkGroup3.setStatus("current")

juniPppMlPppGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 29)
)
juniPppMlPppGroup6.setObjects(
      *(("Juniper-PPP-MIB", "juniPppMlPppBundleRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBundleNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextLinkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigFragmentation"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigReassembly"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigFragmentSize"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigHashLinkSelection"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkBundleName"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBindRowStatus"))
)
if mibBuilder.loadTexts:
    juniPppMlPppGroup6.setStatus("obsolete")

juniPppLcpGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 30)
)
juniPppLcpGroup6.setObjects(
      *(("Juniper-PPP-MIB", "juniPppLinkStatusTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusKeepaliveFailures"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusRemoteMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTunnelIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigStandardIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthentication2"),
        ("Juniper-PPP-MIB", "juniPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    juniPppLcpGroup6.setStatus("obsolete")

juniPppMlPppGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 31)
)
juniPppMlPppGroup7.setObjects(
      *(("Juniper-PPP-MIB", "juniPppMlPppBundleRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBundleNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextLinkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigFragmentation"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigReassembly"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigFragmentSize"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigHashLinkSelection"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication2"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkBundleName"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkRowStatus"))
)
if mibBuilder.loadTexts:
    juniPppMlPppGroup7.setStatus("obsolete")

juniPppLcpGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 32)
)
juniPppLcpGroup7.setObjects(
      *(("Juniper-PPP-MIB", "juniPppLinkStatusTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusKeepaliveFailures"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusRemoteMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTunnelIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigStandardIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthentication2"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigIgnoreMagicNumberMismatch"),
        ("Juniper-PPP-MIB", "juniPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    juniPppLcpGroup7.setStatus("obsolete")

juniPppMlPppGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 33)
)
juniPppMlPppGroup8.setObjects(
      *(("Juniper-PPP-MIB", "juniPppMlPppBundleRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBundleNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextLinkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigFragmentation"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigReassembly"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigFragmentSize"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigHashLinkSelection"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication2"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigIgnoreMagicNumberMismatch"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkBundleName"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBindRowStatus"))
)
if mibBuilder.loadTexts:
    juniPppMlPppGroup8.setStatus("obsolete")

juniPppLcpGroup8 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 34)
)
juniPppLcpGroup8.setObjects(
      *(("Juniper-PPP-MIB", "juniPppLinkStatusTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveRequests"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusInKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusOutKeepaliveReplies"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusKeepaliveFailures"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusRemoteMagicNumber"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusLocalAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkStatusTunnelIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkStatuslcpRenegoTerminates"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigStandardIfIndex"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigAuthentication2"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigIgnoreMagicNumberMismatch"),
        ("Juniper-PPP-MIB", "juniPppLinkConfigMaxLcpRenegotiation"),
        ("Juniper-PPP-MIB", "juniPppNextIfIndex"))
)
if mibBuilder.loadTexts:
    juniPppLcpGroup8.setStatus("current")

juniPppIpGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 35)
)
juniPppIpGroup5.setObjects(
      *(("Juniper-PPP-MIB", "juniPppIpServiceStatus"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppIpLocalIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpNetworkStatusIpcpRenegoTerminates"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerDnsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerWinsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigIpcpNetmask"),
        ("Juniper-PPP-MIB", "juniPppIpConfigInitiateIp"),
        ("Juniper-PPP-MIB", "juniPppIpConfigMaxIpcpRenegotiation"))
)
if mibBuilder.loadTexts:
    juniPppIpGroup5.setStatus("obsolete")

juniPppIpv6Group2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 36)
)
juniPppIpv6Group2.setObjects(
      *(("Juniper-PPP-MIB", "juniPppIpv6ServiceStatus"),
        ("Juniper-PPP-MIB", "juniPppIpv6OperStatus"),
        ("Juniper-PPP-MIB", "juniPppIpv6TerminateReason"),
        ("Juniper-PPP-MIB", "juniPppIpv6TerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppIpv6LocalIpv6AddressIfIdentifier"),
        ("Juniper-PPP-MIB", "juniPppIpv6RemoteIpv6AddressIfIdentifier"),
        ("Juniper-PPP-MIB", "juniPppIpv6NetworkStatusIpv6cpRenegoTerminates"),
        ("Juniper-PPP-MIB", "juniPppIpv6ConfigAdminStatus"),
        ("Juniper-PPP-MIB", "juniPppIpv6ConfigInitiateIpv6"),
        ("Juniper-PPP-MIB", "juniPppIpv6ConfigMaxIpv6cpRenegotiation"))
)
if mibBuilder.loadTexts:
    juniPppIpv6Group2.setStatus("current")

juniPppIpGroup6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 37)
)
juniPppIpGroup6.setObjects(
      *(("Juniper-PPP-MIB", "juniPppIpServiceStatus"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppIpLocalIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpNetworkStatusIpcpRenegoTerminates"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerDnsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerWinsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigIpcpNetmask"),
        ("Juniper-PPP-MIB", "juniPppIpConfigInitiateIp"),
        ("Juniper-PPP-MIB", "juniPppIpConfigMaxIpcpRenegotiation"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPromptIpcpDnsOption"),
        ("Juniper-PPP-MIB", "juniPppIpConfigIpcpLockout"))
)
if mibBuilder.loadTexts:
    juniPppIpGroup6.setStatus("obsolete")

juniPppMlPppGroup9 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 38)
)
juniPppMlPppGroup9.setObjects(
      *(("Juniper-PPP-MIB", "juniPppMlPppBundleRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBundleNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextLinkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigKeepalive"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxAuthenRetries"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMinChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigChapMaxChallengeLength"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigPassiveMode"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthenticatorVirtualRouter"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAaaProfile"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigFragmentation"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigReassembly"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMaxReceiveReconstructedUnit"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigFragmentSize"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigHashLinkSelection"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigAuthentication2"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigIgnoreMagicNumberMismatch"),
        ("Juniper-PPP-MIB", "juniPppMlPppNextNetworkIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkConfigLowerIfIndex"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkBundleName"),
        ("Juniper-PPP-MIB", "juniPppMlPppNetworkRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppBindRowStatus"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMultilinkMulticlass"),
        ("Juniper-PPP-MIB", "juniPppMlPppLinkConfigMultilinkMaxMultiClasses"))
)
if mibBuilder.loadTexts:
    juniPppMlPppGroup9.setStatus("current")

juniPppMlPppMulticlassTcGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 39)
)
juniPppMlPppMulticlassTcGroup1.setObjects(
      *(("Juniper-PPP-MIB", "juniPppMlPppMulticlassTcName"),
        ("Juniper-PPP-MIB", "juniPppMlPppMulticlassFragmentation"),
        ("Juniper-PPP-MIB", "juniPppMlPppMulticlassReassembly"))
)
if mibBuilder.loadTexts:
    juniPppMlPppMulticlassTcGroup1.setStatus("current")

juniPppIpGroup7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 2, 40)
)
juniPppIpGroup7.setObjects(
      *(("Juniper-PPP-MIB", "juniPppIpServiceStatus"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateReason"),
        ("Juniper-PPP-MIB", "juniPppIpTerminateNegFailOption"),
        ("Juniper-PPP-MIB", "juniPppIpLocalIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteIpAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryDnsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemotePrimaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpRemoteSecondaryWinsAddress"),
        ("Juniper-PPP-MIB", "juniPppIpNetworkStatusIpcpRenegoTerminates"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerDnsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPeerWinsPriority"),
        ("Juniper-PPP-MIB", "juniPppIpConfigIpcpNetmask"),
        ("Juniper-PPP-MIB", "juniPppIpConfigInitiateIp"),
        ("Juniper-PPP-MIB", "juniPppIpConfigMaxIpcpRenegotiation"),
        ("Juniper-PPP-MIB", "juniPppIpConfigPromptIpcpDnsOption"),
        ("Juniper-PPP-MIB", "juniPppIpConfigIpcpLockout"),
        ("Juniper-PPP-MIB", "juniPppPeerIpAddressOptional"))
)
if mibBuilder.loadTexts:
    juniPppIpGroup7.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniPppCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniPppCompliance.setStatus(
        "obsolete"
    )

juniPppCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniPppCompliance2.setStatus(
        "obsolete"
    )

juniPppCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniPppCompliance3.setStatus(
        "obsolete"
    )

juniPppCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniPppCompliance4.setStatus(
        "obsolete"
    )

juniPppCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniPppCompliance5.setStatus(
        "obsolete"
    )

juniPppCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 6)
)
if mibBuilder.loadTexts:
    juniPppCompliance6.setStatus(
        "obsolete"
    )

juniPppCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 7)
)
if mibBuilder.loadTexts:
    juniPppCompliance7.setStatus(
        "obsolete"
    )

juniPppCompliance8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 8)
)
if mibBuilder.loadTexts:
    juniPppCompliance8.setStatus(
        "obsolete"
    )

juniPppCompliance9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 9)
)
if mibBuilder.loadTexts:
    juniPppCompliance9.setStatus(
        "obsolete"
    )

juniPppCompliance10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 10)
)
if mibBuilder.loadTexts:
    juniPppCompliance10.setStatus(
        "obsolete"
    )

juniPppCompliance11 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 11)
)
if mibBuilder.loadTexts:
    juniPppCompliance11.setStatus(
        "obsolete"
    )

juniPppCompliance12 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 12)
)
if mibBuilder.loadTexts:
    juniPppCompliance12.setStatus(
        "obsolete"
    )

juniPppCompliance13 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 13)
)
if mibBuilder.loadTexts:
    juniPppCompliance13.setStatus(
        "obsolete"
    )

juniPppCompliance14 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 14)
)
if mibBuilder.loadTexts:
    juniPppCompliance14.setStatus(
        "obsolete"
    )

juniPppCompliance15 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 15)
)
if mibBuilder.loadTexts:
    juniPppCompliance15.setStatus(
        "obsolete"
    )

juniPppCompliance16 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 16)
)
if mibBuilder.loadTexts:
    juniPppCompliance16.setStatus(
        "obsolete"
    )

juniPppCompliance17 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 11, 4, 1, 17)
)
if mibBuilder.loadTexts:
    juniPppCompliance17.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PPP-MIB",
    **{"JuniPppAuthentication": JuniPppAuthentication,
       "JuniPppAuthentication2": JuniPppAuthentication2,
       "JuniPppMlPppBundleName": JuniPppMlPppBundleName,
       "JuniPppMlPppMulticlassTcName": JuniPppMlPppMulticlassTcName,
       "juniPppMIB": juniPppMIB,
       "juniPppObjects": juniPppObjects,
       "juniPppLcp": juniPppLcp,
       "juniPppLinkStatusTable": juniPppLinkStatusTable,
       "juniPppLinkStatusEntry": juniPppLinkStatusEntry,
       "juniPppLinkStatusTerminateReason": juniPppLinkStatusTerminateReason,
       "juniPppLinkStatusTerminateNegFailOption": juniPppLinkStatusTerminateNegFailOption,
       "juniPppLinkStatusInKeepaliveRequests": juniPppLinkStatusInKeepaliveRequests,
       "juniPppLinkStatusOutKeepaliveRequests": juniPppLinkStatusOutKeepaliveRequests,
       "juniPppLinkStatusInKeepaliveReplies": juniPppLinkStatusInKeepaliveReplies,
       "juniPppLinkStatusOutKeepaliveReplies": juniPppLinkStatusOutKeepaliveReplies,
       "juniPppLinkStatusKeepaliveFailures": juniPppLinkStatusKeepaliveFailures,
       "juniPppLinkStatusLocalMagicNumber": juniPppLinkStatusLocalMagicNumber,
       "juniPppLinkStatusRemoteMagicNumber": juniPppLinkStatusRemoteMagicNumber,
       "juniPppLinkStatusLocalAuthentication": juniPppLinkStatusLocalAuthentication,
       "juniPppLinkStatusTunnelIfIndex": juniPppLinkStatusTunnelIfIndex,
       "juniPppLinkStatuslcpRenegoTerminates": juniPppLinkStatuslcpRenegoTerminates,
       "juniPppLinkConfigTable": juniPppLinkConfigTable,
       "juniPppLinkConfigEntry": juniPppLinkConfigEntry,
       "juniPppLinkConfigIfIndex": juniPppLinkConfigIfIndex,
       "juniPppLinkConfigRowStatus": juniPppLinkConfigRowStatus,
       "juniPppLinkConfigLowerIfIndex": juniPppLinkConfigLowerIfIndex,
       "juniPppLinkConfigKeepalive": juniPppLinkConfigKeepalive,
       "juniPppLinkConfigAuthentication": juniPppLinkConfigAuthentication,
       "juniPppLinkConfigMaxAuthenRetries": juniPppLinkConfigMaxAuthenRetries,
       "juniPppLinkConfigStandardIfIndex": juniPppLinkConfigStandardIfIndex,
       "juniPppLinkConfigChapMinChallengeLength": juniPppLinkConfigChapMinChallengeLength,
       "juniPppLinkConfigChapMaxChallengeLength": juniPppLinkConfigChapMaxChallengeLength,
       "juniPppLinkConfigPassiveMode": juniPppLinkConfigPassiveMode,
       "juniPppLinkConfigAuthenticatorVirtualRouter": juniPppLinkConfigAuthenticatorVirtualRouter,
       "juniPppLinkConfigAaaProfile": juniPppLinkConfigAaaProfile,
       "juniPppLinkConfigAuthentication2": juniPppLinkConfigAuthentication2,
       "juniPppLinkConfigIgnoreMagicNumberMismatch": juniPppLinkConfigIgnoreMagicNumberMismatch,
       "juniPppLinkConfigMaxLcpRenegotiation": juniPppLinkConfigMaxLcpRenegotiation,
       "juniPppNextIfIndex": juniPppNextIfIndex,
       "juniPppSec": juniPppSec,
       "juniPppIp": juniPppIp,
       "juniPppIpTable": juniPppIpTable,
       "juniPppIpEntry": juniPppIpEntry,
       "juniPppIpServiceStatus": juniPppIpServiceStatus,
       "juniPppIpTerminateReason": juniPppIpTerminateReason,
       "juniPppIpTerminateNegFailOption": juniPppIpTerminateNegFailOption,
       "juniPppIpLocalIpAddress": juniPppIpLocalIpAddress,
       "juniPppIpRemoteIpAddress": juniPppIpRemoteIpAddress,
       "juniPppIpRemotePrimaryDnsAddress": juniPppIpRemotePrimaryDnsAddress,
       "juniPppIpRemoteSecondaryDnsAddress": juniPppIpRemoteSecondaryDnsAddress,
       "juniPppIpRemotePrimaryWinsAddress": juniPppIpRemotePrimaryWinsAddress,
       "juniPppIpRemoteSecondaryWinsAddress": juniPppIpRemoteSecondaryWinsAddress,
       "juniPppIpNetworkStatusIpcpRenegoTerminates": juniPppIpNetworkStatusIpcpRenegoTerminates,
       "juniPppIpConfigTable": juniPppIpConfigTable,
       "juniPppIpConfigEntry": juniPppIpConfigEntry,
       "juniPppIpConfigPeerDnsPriority": juniPppIpConfigPeerDnsPriority,
       "juniPppIpConfigPeerWinsPriority": juniPppIpConfigPeerWinsPriority,
       "juniPppIpConfigIpcpNetmask": juniPppIpConfigIpcpNetmask,
       "juniPppIpConfigInitiateIp": juniPppIpConfigInitiateIp,
       "juniPppIpConfigMaxIpcpRenegotiation": juniPppIpConfigMaxIpcpRenegotiation,
       "juniPppIpConfigPromptIpcpDnsOption": juniPppIpConfigPromptIpcpDnsOption,
       "juniPppIpConfigIpcpLockout": juniPppIpConfigIpcpLockout,
       "juniPppOsi": juniPppOsi,
       "juniPppOsiTable": juniPppOsiTable,
       "juniPppOsiEntry": juniPppOsiEntry,
       "juniPppOsiServiceStatus": juniPppOsiServiceStatus,
       "juniPppOsiOperStatus": juniPppOsiOperStatus,
       "juniPppOsiTerminateReason": juniPppOsiTerminateReason,
       "juniPppOsiTerminateNegFailOption": juniPppOsiTerminateNegFailOption,
       "juniPppOsiLocalAlignNpdu": juniPppOsiLocalAlignNpdu,
       "juniPppOsiRemoteAlignNpdu": juniPppOsiRemoteAlignNpdu,
       "juniPppOsiConfigTable": juniPppOsiConfigTable,
       "juniPppOsiConfigEntry": juniPppOsiConfigEntry,
       "juniPppOsiConfigAdminStatus": juniPppOsiConfigAdminStatus,
       "juniPppSession": juniPppSession,
       "juniPppSessionTable": juniPppSessionTable,
       "juniPppSessionEntry": juniPppSessionEntry,
       "juniPppSessionGrant": juniPppSessionGrant,
       "juniPppSessionTerminateReason": juniPppSessionTerminateReason,
       "juniPppSessionStartTime": juniPppSessionStartTime,
       "juniPppSessionInOctets": juniPppSessionInOctets,
       "juniPppSessionOutOctets": juniPppSessionOutOctets,
       "juniPppSessionInPackets": juniPppSessionInPackets,
       "juniPppSessionOutPackets": juniPppSessionOutPackets,
       "juniPppSessionSessionTimeout": juniPppSessionSessionTimeout,
       "juniPppSessionInactivityTimeout": juniPppSessionInactivityTimeout,
       "juniPppSessionAccountingInterval": juniPppSessionAccountingInterval,
       "juniPppSessionRemoteIpAddress": juniPppSessionRemoteIpAddress,
       "juniPppSessionRemotePrimaryDnsAddress": juniPppSessionRemotePrimaryDnsAddress,
       "juniPppSessionRemoteSecondaryDnsAddress": juniPppSessionRemoteSecondaryDnsAddress,
       "juniPppSessionRemotePrimaryWinsAddress": juniPppSessionRemotePrimaryWinsAddress,
       "juniPppSessionRemoteSecondaryWinsAddress": juniPppSessionRemoteSecondaryWinsAddress,
       "juniPppSessionRemoteIpv6AddressIfIdentifier": juniPppSessionRemoteIpv6AddressIfIdentifier,
       "juniPppSessionInhibitIp": juniPppSessionInhibitIp,
       "juniPppSessionInhibitIpv6": juniPppSessionInhibitIpv6,
       "juniPppMlPpp": juniPppMlPpp,
       "juniPppMlPppBundleTable": juniPppMlPppBundleTable,
       "juniPppMlPppBundleEntry": juniPppMlPppBundleEntry,
       "juniPppMlPppBundleName": juniPppMlPppBundleName,
       "juniPppMlPppBundleRowStatus": juniPppMlPppBundleRowStatus,
       "juniPppMlPppBundleNetworkIfIndex": juniPppMlPppBundleNetworkIfIndex,
       "juniPppMlPppNextLinkIfIndex": juniPppMlPppNextLinkIfIndex,
       "juniPppMlPppLinkConfigTable": juniPppMlPppLinkConfigTable,
       "juniPppMlPppLinkConfigEntry": juniPppMlPppLinkConfigEntry,
       "juniPppMlPppLinkConfigIfIndex": juniPppMlPppLinkConfigIfIndex,
       "juniPppMlPppLinkConfigLowerIfIndex": juniPppMlPppLinkConfigLowerIfIndex,
       "juniPppMlPppLinkConfigKeepalive": juniPppMlPppLinkConfigKeepalive,
       "juniPppMlPppLinkConfigAuthentication": juniPppMlPppLinkConfigAuthentication,
       "juniPppMlPppLinkConfigMaxAuthenRetries": juniPppMlPppLinkConfigMaxAuthenRetries,
       "juniPppMlPppLinkConfigRowStatus": juniPppMlPppLinkConfigRowStatus,
       "juniPppMlPppLinkConfigAaaProfile": juniPppMlPppLinkConfigAaaProfile,
       "juniPppMlPppLinkConfigChapMinChallengeLength": juniPppMlPppLinkConfigChapMinChallengeLength,
       "juniPppMlPppLinkConfigChapMaxChallengeLength": juniPppMlPppLinkConfigChapMaxChallengeLength,
       "juniPppMlPppLinkConfigPassiveMode": juniPppMlPppLinkConfigPassiveMode,
       "juniPppMlPppLinkConfigAuthenticatorVirtualRouter": juniPppMlPppLinkConfigAuthenticatorVirtualRouter,
       "juniPppMlPppLinkConfigFragmentation": juniPppMlPppLinkConfigFragmentation,
       "juniPppMlPppLinkConfigReassembly": juniPppMlPppLinkConfigReassembly,
       "juniPppMlPppLinkConfigMaxReceiveReconstructedUnit": juniPppMlPppLinkConfigMaxReceiveReconstructedUnit,
       "juniPppMlPppLinkConfigFragmentSize": juniPppMlPppLinkConfigFragmentSize,
       "juniPppMlPppLinkConfigHashLinkSelection": juniPppMlPppLinkConfigHashLinkSelection,
       "juniPppMlPppLinkConfigAuthentication2": juniPppMlPppLinkConfigAuthentication2,
       "juniPppMlPppLinkConfigIgnoreMagicNumberMismatch": juniPppMlPppLinkConfigIgnoreMagicNumberMismatch,
       "juniPppMlPppLinkConfigMultilinkMulticlass": juniPppMlPppLinkConfigMultilinkMulticlass,
       "juniPppMlPppLinkConfigMultilinkMaxMultiClasses": juniPppMlPppLinkConfigMultilinkMaxMultiClasses,
       "juniPppMlPppNextNetworkIfIndex": juniPppMlPppNextNetworkIfIndex,
       "juniPppMlPppNetworkConfigTable": juniPppMlPppNetworkConfigTable,
       "juniPppMlPppNetworkConfigEntry": juniPppMlPppNetworkConfigEntry,
       "juniPppMlPppNetworkConfigIfIndex": juniPppMlPppNetworkConfigIfIndex,
       "juniPppMlPppNetworkConfigLowerIfIndex": juniPppMlPppNetworkConfigLowerIfIndex,
       "juniPppMlPppNetworkBundleName": juniPppMlPppNetworkBundleName,
       "juniPppMlPppNetworkRowStatus": juniPppMlPppNetworkRowStatus,
       "juniPppMlPppLinkBindTable": juniPppMlPppLinkBindTable,
       "juniPppMlPppLinkBindEntry": juniPppMlPppLinkBindEntry,
       "juniPppMlPppBindNetworkIfIndex": juniPppMlPppBindNetworkIfIndex,
       "juniPppMlPppBindLinkIfIndex": juniPppMlPppBindLinkIfIndex,
       "juniPppMlPppBindRowStatus": juniPppMlPppBindRowStatus,
       "juniPppMlPppMulticlassTraffiClassTable": juniPppMlPppMulticlassTraffiClassTable,
       "juniPppMlPppMulticlassTrafficClassEntry": juniPppMlPppMulticlassTrafficClassEntry,
       "juniPppMlPppMulticlassIfIndex": juniPppMlPppMulticlassIfIndex,
       "juniPppMlPppMulticlassIndex": juniPppMlPppMulticlassIndex,
       "juniPppMlPppMulticlassTcName": juniPppMlPppMulticlassTcName,
       "juniPppMlPppMulticlassFragmentation": juniPppMlPppMulticlassFragmentation,
       "juniPppMlPppMulticlassReassembly": juniPppMlPppMulticlassReassembly,
       "juniPppSummary": juniPppSummary,
       "juniPppSummaryPppInterfaceCount": juniPppSummaryPppInterfaceCount,
       "juniPppSummaryPppIpNCPs": juniPppSummaryPppIpNCPs,
       "juniPppSummaryPppOsiNCPs": juniPppSummaryPppOsiNCPs,
       "juniPppSummaryPppIfAdminUp": juniPppSummaryPppIfAdminUp,
       "juniPppSummaryPppIfAdminDown": juniPppSummaryPppIfAdminDown,
       "juniPppSummaryPppIfOperUp": juniPppSummaryPppIfOperUp,
       "juniPppSummaryPppIfOperDown": juniPppSummaryPppIfOperDown,
       "juniPppSummaryPppIfOperDormant": juniPppSummaryPppIfOperDormant,
       "juniPppSummaryPppIfNotPresent": juniPppSummaryPppIfNotPresent,
       "juniPppSummaryPppIfLowerLayerDown": juniPppSummaryPppIfLowerLayerDown,
       "juniPppSummaryPppIpNcpOpened": juniPppSummaryPppIpNcpOpened,
       "juniPppSummaryPppIpNcpClosed": juniPppSummaryPppIpNcpClosed,
       "juniPppSummaryPppOsiNcpOpened": juniPppSummaryPppOsiNcpOpened,
       "juniPppSummaryPppOsiNcpClosed": juniPppSummaryPppOsiNcpClosed,
       "juniPppSummaryPppIfLastChangeTime": juniPppSummaryPppIfLastChangeTime,
       "juniPppSummaryPppLinkInterfaceCount": juniPppSummaryPppLinkInterfaceCount,
       "juniPppSummaryPppLinkIfAdminUp": juniPppSummaryPppLinkIfAdminUp,
       "juniPppSummaryPppLinkIfAdminDown": juniPppSummaryPppLinkIfAdminDown,
       "juniPppSummaryPppLinkIfOperUp": juniPppSummaryPppLinkIfOperUp,
       "juniPppSummaryPppLinkIfOperDown": juniPppSummaryPppLinkIfOperDown,
       "juniPppSummaryPppLinkIfOperDormant": juniPppSummaryPppLinkIfOperDormant,
       "juniPppSummaryPppLinkIfNotPresent": juniPppSummaryPppLinkIfNotPresent,
       "juniPppSummaryPppLinkIfLowerLayerDown": juniPppSummaryPppLinkIfLowerLayerDown,
       "juniPppSummaryPppLinkIfLastChangeTime": juniPppSummaryPppLinkIfLastChangeTime,
       "juniPppSummaryPppNetworkInterfaceCount": juniPppSummaryPppNetworkInterfaceCount,
       "juniPppSummaryPppNetworkIpNCPs": juniPppSummaryPppNetworkIpNCPs,
       "juniPppSummaryPppNetworkOsiNCPs": juniPppSummaryPppNetworkOsiNCPs,
       "juniPppSummaryPppNetworkIfAdminUp": juniPppSummaryPppNetworkIfAdminUp,
       "juniPppSummaryPppNetworkIfAdminDown": juniPppSummaryPppNetworkIfAdminDown,
       "juniPppSummaryPppNetworkIfOperUp": juniPppSummaryPppNetworkIfOperUp,
       "juniPppSummaryPppNetworkIfOperDown": juniPppSummaryPppNetworkIfOperDown,
       "juniPppSummaryPppNetworkIfOperDormant": juniPppSummaryPppNetworkIfOperDormant,
       "juniPppSummaryPppNetworkIfNotPresent": juniPppSummaryPppNetworkIfNotPresent,
       "juniPppSummaryPppNetworkIfLowerLayerDown": juniPppSummaryPppNetworkIfLowerLayerDown,
       "juniPppSummaryPppNetworkIpNcpOpened": juniPppSummaryPppNetworkIpNcpOpened,
       "juniPppSummaryPppNetworkIpNcpClosed": juniPppSummaryPppNetworkIpNcpClosed,
       "juniPppSummaryPppNetworkOsiNcpOpened": juniPppSummaryPppNetworkOsiNcpOpened,
       "juniPppSummaryPppNetworkOsiNcpClosed": juniPppSummaryPppNetworkOsiNcpClosed,
       "juniPppSummaryPppNetworkIfLastChangeTime": juniPppSummaryPppNetworkIfLastChangeTime,
       "juniPppSummaryPppIpv6NCPs": juniPppSummaryPppIpv6NCPs,
       "juniPppSummaryPppIpv6NcpOpened": juniPppSummaryPppIpv6NcpOpened,
       "juniPppSummaryPppIpv6NcpClosed": juniPppSummaryPppIpv6NcpClosed,
       "juniPppSummaryPppNetworkIpv6NCPs": juniPppSummaryPppNetworkIpv6NCPs,
       "juniPppSummaryPppNetworkIpv6NcpOpened": juniPppSummaryPppNetworkIpv6NcpOpened,
       "juniPppSummaryPppNetworkIpv6NcpClosed": juniPppSummaryPppNetworkIpv6NcpClosed,
       "juniPppSummaryPppStaticInterfaceCount": juniPppSummaryPppStaticInterfaceCount,
       "juniPppSummaryPppMplsNCPs": juniPppSummaryPppMplsNCPs,
       "juniPppSummaryPppIpAdminOpen": juniPppSummaryPppIpAdminOpen,
       "juniPppSummaryPppIpAdminClose": juniPppSummaryPppIpAdminClose,
       "juniPppSummaryPppIpv6AdminOpen": juniPppSummaryPppIpv6AdminOpen,
       "juniPppSummaryPppIpv6AdminClose": juniPppSummaryPppIpv6AdminClose,
       "juniPppSummaryPppOsiAdminOpen": juniPppSummaryPppOsiAdminOpen,
       "juniPppSummaryPppOsiAdminClose": juniPppSummaryPppOsiAdminClose,
       "juniPppSummaryPppMplsAdminOpen": juniPppSummaryPppMplsAdminOpen,
       "juniPppSummaryPppMplsAdminClose": juniPppSummaryPppMplsAdminClose,
       "juniPppSummaryPppIpNcpNotPresent": juniPppSummaryPppIpNcpNotPresent,
       "juniPppSummaryPppIpNcpNoResources": juniPppSummaryPppIpNcpNoResources,
       "juniPppSummaryPppIpv6NcpNotPresent": juniPppSummaryPppIpv6NcpNotPresent,
       "juniPppSummaryPppIpv6NcpNoResources": juniPppSummaryPppIpv6NcpNoResources,
       "juniPppSummaryPppOsiNcpNotPresent": juniPppSummaryPppOsiNcpNotPresent,
       "juniPppSummaryPppOsiNcpNoResources": juniPppSummaryPppOsiNcpNoResources,
       "juniPppSummaryPppMplsNcpOpened": juniPppSummaryPppMplsNcpOpened,
       "juniPppSummaryPppMplsNcpClosed": juniPppSummaryPppMplsNcpClosed,
       "juniPppSummaryPppMplsNcpNotPresent": juniPppSummaryPppMplsNcpNotPresent,
       "juniPppSummaryPppMplsNcpNoResources": juniPppSummaryPppMplsNcpNoResources,
       "juniPppSummaryPppLinkStaticInterfaceCount": juniPppSummaryPppLinkStaticInterfaceCount,
       "juniPppSummaryPppNetworkStaticInterfaceCount": juniPppSummaryPppNetworkStaticInterfaceCount,
       "juniPppSummaryPppNetworkMplsNCPs": juniPppSummaryPppNetworkMplsNCPs,
       "juniPppSummaryPppNetworkIpAdminOpen": juniPppSummaryPppNetworkIpAdminOpen,
       "juniPppSummaryPppNetworkIpAdminClose": juniPppSummaryPppNetworkIpAdminClose,
       "juniPppSummaryPppNetworkIpv6AdminOpen": juniPppSummaryPppNetworkIpv6AdminOpen,
       "juniPppSummaryPppNetworkIpv6AdminClose": juniPppSummaryPppNetworkIpv6AdminClose,
       "juniPppSummaryPppNetworkOsiAdminOpen": juniPppSummaryPppNetworkOsiAdminOpen,
       "juniPppSummaryPppNetworkOsiAdminClose": juniPppSummaryPppNetworkOsiAdminClose,
       "juniPppSummaryPppNetworkMplsAdminOpen": juniPppSummaryPppNetworkMplsAdminOpen,
       "juniPppSummaryPppNetworkMplsAdminClose": juniPppSummaryPppNetworkMplsAdminClose,
       "juniPppSummaryPppNetworkIpNcpNotPresent": juniPppSummaryPppNetworkIpNcpNotPresent,
       "juniPppSummaryPppNetworkIpNcpNoResources": juniPppSummaryPppNetworkIpNcpNoResources,
       "juniPppSummaryPppNetworkIpv6NcpNotPresent": juniPppSummaryPppNetworkIpv6NcpNotPresent,
       "juniPppSummaryPppNetworkIpv6NcpNoResources": juniPppSummaryPppNetworkIpv6NcpNoResources,
       "juniPppSummaryPppNetworkOsiNcpNotPresent": juniPppSummaryPppNetworkOsiNcpNotPresent,
       "juniPppSummaryPppNetworkOsiNcpNoResources": juniPppSummaryPppNetworkOsiNcpNoResources,
       "juniPppSummaryPppNetworkMplsNcpOpened": juniPppSummaryPppNetworkMplsNcpOpened,
       "juniPppSummaryPppNetworkMplsNcpClosed": juniPppSummaryPppNetworkMplsNcpClosed,
       "juniPppSummaryPppNetworkMplsNcpNotPresent": juniPppSummaryPppNetworkMplsNcpNotPresent,
       "juniPppSummaryPppNetworkMplsNcpNoResources": juniPppSummaryPppNetworkMplsNcpNoResources,
       "juniPppIpv6": juniPppIpv6,
       "juniPppIpv6Table": juniPppIpv6Table,
       "juniPppIpv6Entry": juniPppIpv6Entry,
       "juniPppIpv6ServiceStatus": juniPppIpv6ServiceStatus,
       "juniPppIpv6OperStatus": juniPppIpv6OperStatus,
       "juniPppIpv6TerminateReason": juniPppIpv6TerminateReason,
       "juniPppIpv6TerminateNegFailOption": juniPppIpv6TerminateNegFailOption,
       "juniPppIpv6LocalIpv6AddressIfIdentifier": juniPppIpv6LocalIpv6AddressIfIdentifier,
       "juniPppIpv6RemoteIpv6AddressIfIdentifier": juniPppIpv6RemoteIpv6AddressIfIdentifier,
       "juniPppIpv6NetworkStatusIpv6cpRenegoTerminates": juniPppIpv6NetworkStatusIpv6cpRenegoTerminates,
       "juniPppIpv6ConfigTable": juniPppIpv6ConfigTable,
       "juniPppIpv6ConfigEntry": juniPppIpv6ConfigEntry,
       "juniPppIpv6ConfigAdminStatus": juniPppIpv6ConfigAdminStatus,
       "juniPppIpv6ConfigInitiateIpv6": juniPppIpv6ConfigInitiateIpv6,
       "juniPppIpv6ConfigMaxIpv6cpRenegotiation": juniPppIpv6ConfigMaxIpv6cpRenegotiation,
       "juniPppGlobalConfig": juniPppGlobalConfig,
       "juniPppPeerIpAddressOptional": juniPppPeerIpAddressOptional,
       "juniPppConformance": juniPppConformance,
       "juniPppCompliances": juniPppCompliances,
       "juniPppCompliance": juniPppCompliance,
       "juniPppCompliance2": juniPppCompliance2,
       "juniPppCompliance3": juniPppCompliance3,
       "juniPppCompliance4": juniPppCompliance4,
       "juniPppCompliance5": juniPppCompliance5,
       "juniPppCompliance6": juniPppCompliance6,
       "juniPppCompliance7": juniPppCompliance7,
       "juniPppCompliance8": juniPppCompliance8,
       "juniPppCompliance9": juniPppCompliance9,
       "juniPppCompliance10": juniPppCompliance10,
       "juniPppCompliance11": juniPppCompliance11,
       "juniPppCompliance12": juniPppCompliance12,
       "juniPppCompliance13": juniPppCompliance13,
       "juniPppCompliance14": juniPppCompliance14,
       "juniPppCompliance15": juniPppCompliance15,
       "juniPppCompliance16": juniPppCompliance16,
       "juniPppCompliance17": juniPppCompliance17,
       "juniPppGroups": juniPppGroups,
       "juniPppLcpGroup": juniPppLcpGroup,
       "juniPppIpGroup": juniPppIpGroup,
       "juniPppOsiGroup": juniPppOsiGroup,
       "juniPppLcpGroup2": juniPppLcpGroup2,
       "juniPppIpGroup2": juniPppIpGroup2,
       "juniPppOsiGroup2": juniPppOsiGroup2,
       "juniPppSessionGroup": juniPppSessionGroup,
       "juniPppMlPppGroup": juniPppMlPppGroup,
       "juniPppSummaryGroup": juniPppSummaryGroup,
       "juniPppLcpGroup3": juniPppLcpGroup3,
       "juniPppSummaryBasicGroup": juniPppSummaryBasicGroup,
       "juniPppSummaryLinkGroup": juniPppSummaryLinkGroup,
       "juniPppSummaryNetworkGroup": juniPppSummaryNetworkGroup,
       "juniPppLcpGroup4": juniPppLcpGroup4,
       "juniPppIpGroup3": juniPppIpGroup3,
       "juniPppMlPppGroup2": juniPppMlPppGroup2,
       "juniPppMlPppGroup3": juniPppMlPppGroup3,
       "juniPppLcpGroup5": juniPppLcpGroup5,
       "juniPppMlPppGroup4": juniPppMlPppGroup4,
       "juniPppSummaryBasicGroup2": juniPppSummaryBasicGroup2,
       "juniPppSummaryNetworkGroup2": juniPppSummaryNetworkGroup2,
       "juniPppIpGroup4": juniPppIpGroup4,
       "juniPppIpv6Group": juniPppIpv6Group,
       "juniPppSessionGroup2": juniPppSessionGroup2,
       "juniPppMlPppGroup5": juniPppMlPppGroup5,
       "juniPppSummaryBasicGroup3": juniPppSummaryBasicGroup3,
       "juniPppSummaryLinkGroup2": juniPppSummaryLinkGroup2,
       "juniPppSummaryNetworkGroup3": juniPppSummaryNetworkGroup3,
       "juniPppMlPppGroup6": juniPppMlPppGroup6,
       "juniPppLcpGroup6": juniPppLcpGroup6,
       "juniPppMlPppGroup7": juniPppMlPppGroup7,
       "juniPppLcpGroup7": juniPppLcpGroup7,
       "juniPppMlPppGroup8": juniPppMlPppGroup8,
       "juniPppLcpGroup8": juniPppLcpGroup8,
       "juniPppIpGroup5": juniPppIpGroup5,
       "juniPppIpv6Group2": juniPppIpv6Group2,
       "juniPppIpGroup6": juniPppIpGroup6,
       "juniPppMlPppGroup9": juniPppMlPppGroup9,
       "juniPppMlPppMulticlassTcGroup1": juniPppMlPppMulticlassTcGroup1,
       "juniPppIpGroup7": juniPppIpGroup7}
)
