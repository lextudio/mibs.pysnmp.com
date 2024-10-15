# SNMP MIB module (MITEL-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MITEL-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:22:16 2024
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

(DisplayString,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

mitelRouterDhcpGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3)
)
mitelRouterDhcpGroup.setRevisions(
        ("2005-11-07 12:00",
         "2003-03-21 12:31",
         "1999-03-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class MitelDhcpServerProtocol(Integer32, TextualConvention):
    status = "current"
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
        *(("bootp", 2),
          ("bootp-or-dhcp", 4),
          ("dhcp", 3),
          ("none", 1))
    )



class MitelDhcpServerOptionList(Integer32, TextualConvention):
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
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76)
        )
    )
    namedValues = NamedValues(
        *(("all-subnets-are-local", 27),
          ("arp-cache-timeout", 35),
          ("boot-file-size", 13),
          ("bootfile-name", 67),
          ("broadcast-address", 28),
          ("client-identifier", 61),
          ("cookie-server", 8),
          ("default-ip-time-to-live", 23),
          ("default-router", 3),
          ("dns-server", 6),
          ("domain-name", 15),
          ("ethernet-encapsulation", 36),
          ("extension-path", 18),
          ("finger-server", 73),
          ("host-name", 12),
          ("impress-server", 10),
          ("interface-MTU-value", 26),
          ("ip-forwarding", 19),
          ("irc-server", 74),
          ("lease-time", 51),
          ("log-server", 7),
          ("lpr-server", 9),
          ("mask-supplier", 30),
          ("max-datagram-reassembly", 22),
          ("max-dhcp-message-size", 57),
          ("merit-dump-file-name", 14),
          ("message", 56),
          ("message-type", 53),
          ("mobile-ip-home-agent", 68),
          ("name-server", 5),
          ("netbios-ip-dgram-distrib-server", 45),
          ("netbios-ip-name-server", 44),
          ("netbios-ip-node-type", 46),
          ("netbios-ip-scope", 47),
          ("nis-domain-name", 40),
          ("nis-plus-domain", 64),
          ("nis-plus-server", 65),
          ("nis-server", 41),
          ("nntp-server", 71),
          ("non-local-source-routing", 20),
          ("ntp-server", 42),
          ("option-overload", 52),
          ("parameter-request-list", 55),
          ("path-MTU-aging-timeout", 24),
          ("path-MTU-plateau-table", 25),
          ("perform-mask-discovery", 29),
          ("perform-router-discovery", 31),
          ("policy-filter", 21),
          ("pop3-server", 70),
          ("rebinding-time-value-t2", 59),
          ("renewal-time-value-t1", 58),
          ("requested-ip", 50),
          ("resource-location-server", 11),
          ("root-path", 17),
          ("router-solicitation-address", 32),
          ("server-identifier", 54),
          ("smtp-server", 69),
          ("static-route", 33),
          ("streettalk-directory-assistance-server", 76),
          ("streettalk-server", 75),
          ("subnet-mask", 1),
          ("swap-server", 16),
          ("tcp-default-ttl", 37),
          ("tcp-keepalive-garbage", 39),
          ("tcp-keepalive-interval", 38),
          ("tftp-server-name", 66),
          ("time-offset", 2),
          ("time-server", 4),
          ("trailer-encapsulation", 34),
          ("vendor-class-identifier", 60),
          ("vendor-specific-information", 43),
          ("www-server", 72),
          ("x-window-display-manager", 49),
          ("x-window-font-server", 48))
    )



# MIB Managed Objects in the order of their OIDs

_Mitel_ObjectIdentity = ObjectIdentity
mitel = _Mitel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027)
)
_MitelIdentification_ObjectIdentity = ObjectIdentity
mitelIdentification = _MitelIdentification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1)
)
_MitelIdCallServers_ObjectIdentity = ObjectIdentity
mitelIdCallServers = _MitelIdCallServers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2)
)
_MitelIdCsIpera1000_ObjectIdentity = ObjectIdentity
mitelIdCsIpera1000 = _MitelIdCsIpera1000_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4)
)
_MitelProprietary_ObjectIdentity = ObjectIdentity
mitelProprietary = _MitelProprietary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4)
)
_MitelPropIpNetworking_ObjectIdentity = ObjectIdentity
mitelPropIpNetworking = _MitelPropIpNetworking_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8)
)
_MitelIpNetRouter_ObjectIdentity = ObjectIdentity
mitelIpNetRouter = _MitelIpNetRouter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1)
)


class _MitelDhcpRelayAgentEnable_Type(Integer32):
    """Custom type mitelDhcpRelayAgentEnable based on Integer32"""
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


_MitelDhcpRelayAgentEnable_Type.__name__ = "Integer32"
_MitelDhcpRelayAgentEnable_Object = MibScalar
mitelDhcpRelayAgentEnable = _MitelDhcpRelayAgentEnable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 1),
    _MitelDhcpRelayAgentEnable_Type()
)
mitelDhcpRelayAgentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpRelayAgentEnable.setStatus("current")


class _MitelDhcpRelayAgentMaxHops_Type(Integer32):
    """Custom type mitelDhcpRelayAgentMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_MitelDhcpRelayAgentMaxHops_Type.__name__ = "Integer32"
_MitelDhcpRelayAgentMaxHops_Object = MibScalar
mitelDhcpRelayAgentMaxHops = _MitelDhcpRelayAgentMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 2),
    _MitelDhcpRelayAgentMaxHops_Type()
)
mitelDhcpRelayAgentMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpRelayAgentMaxHops.setStatus("current")
_MitelDhcpRelayAgentServerTable_Object = MibTable
mitelDhcpRelayAgentServerTable = _MitelDhcpRelayAgentServerTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 3)
)
if mibBuilder.loadTexts:
    mitelDhcpRelayAgentServerTable.setStatus("current")
_MitelDhcpRelayAgentServerEntry_Object = MibTableRow
mitelDhcpRelayAgentServerEntry = _MitelDhcpRelayAgentServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 3, 1)
)
mitelDhcpRelayAgentServerEntry.setIndexNames(
    (0, "MITEL-DHCP-MIB", "mitelDhcpRelayAgentServerAddr"),
)
if mibBuilder.loadTexts:
    mitelDhcpRelayAgentServerEntry.setStatus("current")
_MitelDhcpRelayAgentServerAddr_Type = IpAddress
_MitelDhcpRelayAgentServerAddr_Object = MibTableColumn
mitelDhcpRelayAgentServerAddr = _MitelDhcpRelayAgentServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 3, 1, 1),
    _MitelDhcpRelayAgentServerAddr_Type()
)
mitelDhcpRelayAgentServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpRelayAgentServerAddr.setStatus("current")


class _MitelDhcpRelayAgentServerName_Type(DisplayString):
    """Custom type mitelDhcpRelayAgentServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MitelDhcpRelayAgentServerName_Type.__name__ = "DisplayString"
_MitelDhcpRelayAgentServerName_Object = MibTableColumn
mitelDhcpRelayAgentServerName = _MitelDhcpRelayAgentServerName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 3, 1, 2),
    _MitelDhcpRelayAgentServerName_Type()
)
mitelDhcpRelayAgentServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpRelayAgentServerName.setStatus("current")
_MitelDhcpRelayAgentServerStatus_Type = RowStatus
_MitelDhcpRelayAgentServerStatus_Object = MibTableColumn
mitelDhcpRelayAgentServerStatus = _MitelDhcpRelayAgentServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 3, 1, 3),
    _MitelDhcpRelayAgentServerStatus_Type()
)
mitelDhcpRelayAgentServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelDhcpRelayAgentServerStatus.setStatus("current")


class _MitelDhcpRelayAgentBroadcast_Type(Integer32):
    """Custom type mitelDhcpRelayAgentBroadcast based on Integer32"""
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


_MitelDhcpRelayAgentBroadcast_Type.__name__ = "Integer32"
_MitelDhcpRelayAgentBroadcast_Object = MibScalar
mitelDhcpRelayAgentBroadcast = _MitelDhcpRelayAgentBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 4),
    _MitelDhcpRelayAgentBroadcast_Type()
)
mitelDhcpRelayAgentBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpRelayAgentBroadcast.setStatus("current")
_MitelDhcpServerGroup_ObjectIdentity = ObjectIdentity
mitelDhcpServerGroup = _MitelDhcpServerGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5)
)
_MitelDhcpServerGeneralGroup_ObjectIdentity = ObjectIdentity
mitelDhcpServerGeneralGroup = _MitelDhcpServerGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 1)
)


class _MitelDhcpServerGeneralEnable_Type(Integer32):
    """Custom type mitelDhcpServerGeneralEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoconfig", 3),
          ("disabled", 2),
          ("enabled", 1))
    )


_MitelDhcpServerGeneralEnable_Type.__name__ = "Integer32"
_MitelDhcpServerGeneralEnable_Object = MibScalar
mitelDhcpServerGeneralEnable = _MitelDhcpServerGeneralEnable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 1, 1),
    _MitelDhcpServerGeneralEnable_Type()
)
mitelDhcpServerGeneralEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerGeneralEnable.setStatus("current")


class _MitelDhcpServerGeneralGateway_Type(Integer32):
    """Custom type mitelDhcpServerGeneralGateway based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-this-if", 3),
          ("this-if-first", 1),
          ("this-if-last", 2))
    )


_MitelDhcpServerGeneralGateway_Type.__name__ = "Integer32"
_MitelDhcpServerGeneralGateway_Object = MibScalar
mitelDhcpServerGeneralGateway = _MitelDhcpServerGeneralGateway_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 1, 2),
    _MitelDhcpServerGeneralGateway_Type()
)
mitelDhcpServerGeneralGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerGeneralGateway.setStatus("current")
_MitelDhcpServerGeneralRefDhcpServer_Type = IpAddress
_MitelDhcpServerGeneralRefDhcpServer_Object = MibScalar
mitelDhcpServerGeneralRefDhcpServer = _MitelDhcpServerGeneralRefDhcpServer_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 1, 3),
    _MitelDhcpServerGeneralRefDhcpServer_Type()
)
mitelDhcpServerGeneralRefDhcpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerGeneralRefDhcpServer.setStatus("current")


class _MitelDhcpServerGeneralPingStatus_Type(Integer32):
    """Custom type mitelDhcpServerGeneralPingStatus based on Integer32"""
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


_MitelDhcpServerGeneralPingStatus_Type.__name__ = "Integer32"
_MitelDhcpServerGeneralPingStatus_Object = MibScalar
mitelDhcpServerGeneralPingStatus = _MitelDhcpServerGeneralPingStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 1, 4),
    _MitelDhcpServerGeneralPingStatus_Type()
)
mitelDhcpServerGeneralPingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerGeneralPingStatus.setStatus("current")
_MitelDhcpServerSubnetTable_Object = MibTable
mitelDhcpServerSubnetTable = _MitelDhcpServerSubnetTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 2)
)
if mibBuilder.loadTexts:
    mitelDhcpServerSubnetTable.setStatus("current")
_MitelDhcpServerSubnetEntry_Object = MibTableRow
mitelDhcpServerSubnetEntry = _MitelDhcpServerSubnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 2, 1)
)
mitelDhcpServerSubnetEntry.setIndexNames(
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerSubnetAddr"),
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerSubnetSharedNet"),
)
if mibBuilder.loadTexts:
    mitelDhcpServerSubnetEntry.setStatus("current")
_MitelDhcpServerSubnetAddr_Type = IpAddress
_MitelDhcpServerSubnetAddr_Object = MibTableColumn
mitelDhcpServerSubnetAddr = _MitelDhcpServerSubnetAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 2, 1, 1),
    _MitelDhcpServerSubnetAddr_Type()
)
mitelDhcpServerSubnetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerSubnetAddr.setStatus("current")
_MitelDhcpServerSubnetSharedNet_Type = IpAddress
_MitelDhcpServerSubnetSharedNet_Object = MibTableColumn
mitelDhcpServerSubnetSharedNet = _MitelDhcpServerSubnetSharedNet_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 2, 1, 2),
    _MitelDhcpServerSubnetSharedNet_Type()
)
mitelDhcpServerSubnetSharedNet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerSubnetSharedNet.setStatus("current")
_MitelDhcpServerSubnetMask_Type = IpAddress
_MitelDhcpServerSubnetMask_Object = MibTableColumn
mitelDhcpServerSubnetMask = _MitelDhcpServerSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 2, 1, 3),
    _MitelDhcpServerSubnetMask_Type()
)
mitelDhcpServerSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerSubnetMask.setStatus("current")


class _MitelDhcpServerSubnetGateway_Type(Integer32):
    """Custom type mitelDhcpServerSubnetGateway based on Integer32"""
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
        *(("default", 4),
          ("not-this-if", 3),
          ("this-if-first", 1),
          ("this-if-last", 2))
    )


_MitelDhcpServerSubnetGateway_Type.__name__ = "Integer32"
_MitelDhcpServerSubnetGateway_Object = MibTableColumn
mitelDhcpServerSubnetGateway = _MitelDhcpServerSubnetGateway_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 2, 1, 4),
    _MitelDhcpServerSubnetGateway_Type()
)
mitelDhcpServerSubnetGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerSubnetGateway.setStatus("current")


class _MitelDhcpServerSubnetName_Type(DisplayString):
    """Custom type mitelDhcpServerSubnetName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MitelDhcpServerSubnetName_Type.__name__ = "DisplayString"
_MitelDhcpServerSubnetName_Object = MibTableColumn
mitelDhcpServerSubnetName = _MitelDhcpServerSubnetName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 2, 1, 5),
    _MitelDhcpServerSubnetName_Type()
)
mitelDhcpServerSubnetName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerSubnetName.setStatus("current")


class _MitelDhcpServerSubnetDeleteTree_Type(Integer32):
    """Custom type mitelDhcpServerSubnetDeleteTree based on Integer32"""
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


_MitelDhcpServerSubnetDeleteTree_Type.__name__ = "Integer32"
_MitelDhcpServerSubnetDeleteTree_Object = MibTableColumn
mitelDhcpServerSubnetDeleteTree = _MitelDhcpServerSubnetDeleteTree_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 2, 1, 6),
    _MitelDhcpServerSubnetDeleteTree_Type()
)
mitelDhcpServerSubnetDeleteTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerSubnetDeleteTree.setStatus("current")
_MitelDhcpServerSubnetStatus_Type = RowStatus
_MitelDhcpServerSubnetStatus_Object = MibTableColumn
mitelDhcpServerSubnetStatus = _MitelDhcpServerSubnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 2, 1, 7),
    _MitelDhcpServerSubnetStatus_Type()
)
mitelDhcpServerSubnetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelDhcpServerSubnetStatus.setStatus("current")
_MitelDhcpServerRangeTable_Object = MibTable
mitelDhcpServerRangeTable = _MitelDhcpServerRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3)
)
if mibBuilder.loadTexts:
    mitelDhcpServerRangeTable.setStatus("current")
_MitelDhcpServerRangeEntry_Object = MibTableRow
mitelDhcpServerRangeEntry = _MitelDhcpServerRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1)
)
mitelDhcpServerRangeEntry.setIndexNames(
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerRangeStart"),
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerRangeEnd"),
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerRangeSubnet"),
)
if mibBuilder.loadTexts:
    mitelDhcpServerRangeEntry.setStatus("current")
_MitelDhcpServerRangeStart_Type = IpAddress
_MitelDhcpServerRangeStart_Object = MibTableColumn
mitelDhcpServerRangeStart = _MitelDhcpServerRangeStart_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1, 1),
    _MitelDhcpServerRangeStart_Type()
)
mitelDhcpServerRangeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerRangeStart.setStatus("current")
_MitelDhcpServerRangeEnd_Type = IpAddress
_MitelDhcpServerRangeEnd_Object = MibTableColumn
mitelDhcpServerRangeEnd = _MitelDhcpServerRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1, 2),
    _MitelDhcpServerRangeEnd_Type()
)
mitelDhcpServerRangeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerRangeEnd.setStatus("current")
_MitelDhcpServerRangeSubnet_Type = IpAddress
_MitelDhcpServerRangeSubnet_Object = MibTableColumn
mitelDhcpServerRangeSubnet = _MitelDhcpServerRangeSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1, 3),
    _MitelDhcpServerRangeSubnet_Type()
)
mitelDhcpServerRangeSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerRangeSubnet.setStatus("current")
_MitelDhcpServerRangeProtocol_Type = MitelDhcpServerProtocol
_MitelDhcpServerRangeProtocol_Object = MibTableColumn
mitelDhcpServerRangeProtocol = _MitelDhcpServerRangeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1, 4),
    _MitelDhcpServerRangeProtocol_Type()
)
mitelDhcpServerRangeProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerRangeProtocol.setStatus("current")


class _MitelDhcpServerRangeGateway_Type(Integer32):
    """Custom type mitelDhcpServerRangeGateway based on Integer32"""
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
        *(("default", 4),
          ("not-this-if", 3),
          ("this-if-first", 1),
          ("this-if-last", 2))
    )


_MitelDhcpServerRangeGateway_Type.__name__ = "Integer32"
_MitelDhcpServerRangeGateway_Object = MibTableColumn
mitelDhcpServerRangeGateway = _MitelDhcpServerRangeGateway_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1, 5),
    _MitelDhcpServerRangeGateway_Type()
)
mitelDhcpServerRangeGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerRangeGateway.setStatus("current")
_MitelDhcpServerRangeLeaseTime_Type = Integer32
_MitelDhcpServerRangeLeaseTime_Object = MibTableColumn
mitelDhcpServerRangeLeaseTime = _MitelDhcpServerRangeLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1, 6),
    _MitelDhcpServerRangeLeaseTime_Type()
)
mitelDhcpServerRangeLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerRangeLeaseTime.setStatus("current")


class _MitelDhcpServerRangeName_Type(DisplayString):
    """Custom type mitelDhcpServerRangeName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MitelDhcpServerRangeName_Type.__name__ = "DisplayString"
_MitelDhcpServerRangeName_Object = MibTableColumn
mitelDhcpServerRangeName = _MitelDhcpServerRangeName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1, 7),
    _MitelDhcpServerRangeName_Type()
)
mitelDhcpServerRangeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerRangeName.setStatus("current")


class _MitelDhcpServerRangeMatchClassId_Type(Integer32):
    """Custom type mitelDhcpServerRangeMatchClassId based on Integer32"""
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


_MitelDhcpServerRangeMatchClassId_Type.__name__ = "Integer32"
_MitelDhcpServerRangeMatchClassId_Object = MibTableColumn
mitelDhcpServerRangeMatchClassId = _MitelDhcpServerRangeMatchClassId_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1, 8),
    _MitelDhcpServerRangeMatchClassId_Type()
)
mitelDhcpServerRangeMatchClassId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerRangeMatchClassId.setStatus("current")


class _MitelDhcpServerRangeDeleteTree_Type(Integer32):
    """Custom type mitelDhcpServerRangeDeleteTree based on Integer32"""
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


_MitelDhcpServerRangeDeleteTree_Type.__name__ = "Integer32"
_MitelDhcpServerRangeDeleteTree_Object = MibTableColumn
mitelDhcpServerRangeDeleteTree = _MitelDhcpServerRangeDeleteTree_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1, 9),
    _MitelDhcpServerRangeDeleteTree_Type()
)
mitelDhcpServerRangeDeleteTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerRangeDeleteTree.setStatus("current")
_MitelDhcpServerRangeStatus_Type = RowStatus
_MitelDhcpServerRangeStatus_Object = MibTableColumn
mitelDhcpServerRangeStatus = _MitelDhcpServerRangeStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 3, 1, 10),
    _MitelDhcpServerRangeStatus_Type()
)
mitelDhcpServerRangeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelDhcpServerRangeStatus.setStatus("current")
_MitelDhcpServerStaticIpTable_Object = MibTable
mitelDhcpServerStaticIpTable = _MitelDhcpServerStaticIpTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4)
)
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpTable.setStatus("current")
_MitelDhcpServerStaticIpEntry_Object = MibTableRow
mitelDhcpServerStaticIpEntry = _MitelDhcpServerStaticIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4, 1)
)
mitelDhcpServerStaticIpEntry.setIndexNames(
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerStaticIpAddr"),
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerStaticIpSubnet"),
)
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpEntry.setStatus("current")
_MitelDhcpServerStaticIpAddr_Type = IpAddress
_MitelDhcpServerStaticIpAddr_Object = MibTableColumn
mitelDhcpServerStaticIpAddr = _MitelDhcpServerStaticIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4, 1, 1),
    _MitelDhcpServerStaticIpAddr_Type()
)
mitelDhcpServerStaticIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpAddr.setStatus("current")
_MitelDhcpServerStaticIpSubnet_Type = IpAddress
_MitelDhcpServerStaticIpSubnet_Object = MibTableColumn
mitelDhcpServerStaticIpSubnet = _MitelDhcpServerStaticIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4, 1, 2),
    _MitelDhcpServerStaticIpSubnet_Type()
)
mitelDhcpServerStaticIpSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpSubnet.setStatus("current")
_MitelDhcpServerStaticIpProtocol_Type = MitelDhcpServerProtocol
_MitelDhcpServerStaticIpProtocol_Object = MibTableColumn
mitelDhcpServerStaticIpProtocol = _MitelDhcpServerStaticIpProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4, 1, 3),
    _MitelDhcpServerStaticIpProtocol_Type()
)
mitelDhcpServerStaticIpProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpProtocol.setStatus("current")


class _MitelDhcpServerStaticIpGateway_Type(Integer32):
    """Custom type mitelDhcpServerStaticIpGateway based on Integer32"""
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
        *(("default", 4),
          ("not-this-if", 3),
          ("this-if-first", 1),
          ("this-if-last", 2))
    )


_MitelDhcpServerStaticIpGateway_Type.__name__ = "Integer32"
_MitelDhcpServerStaticIpGateway_Object = MibTableColumn
mitelDhcpServerStaticIpGateway = _MitelDhcpServerStaticIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4, 1, 4),
    _MitelDhcpServerStaticIpGateway_Type()
)
mitelDhcpServerStaticIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpGateway.setStatus("current")


class _MitelDhcpServerStaticIpMacAddress_Type(OctetString):
    """Custom type mitelDhcpServerStaticIpMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MitelDhcpServerStaticIpMacAddress_Type.__name__ = "OctetString"
_MitelDhcpServerStaticIpMacAddress_Object = MibTableColumn
mitelDhcpServerStaticIpMacAddress = _MitelDhcpServerStaticIpMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4, 1, 5),
    _MitelDhcpServerStaticIpMacAddress_Type()
)
mitelDhcpServerStaticIpMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpMacAddress.setStatus("current")


class _MitelDhcpServerStaticIpClientId_Type(OctetString):
    """Custom type mitelDhcpServerStaticIpClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MitelDhcpServerStaticIpClientId_Type.__name__ = "OctetString"
_MitelDhcpServerStaticIpClientId_Object = MibTableColumn
mitelDhcpServerStaticIpClientId = _MitelDhcpServerStaticIpClientId_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4, 1, 6),
    _MitelDhcpServerStaticIpClientId_Type()
)
mitelDhcpServerStaticIpClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpClientId.setStatus("current")


class _MitelDhcpServerStaticIpName_Type(DisplayString):
    """Custom type mitelDhcpServerStaticIpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_MitelDhcpServerStaticIpName_Type.__name__ = "DisplayString"
_MitelDhcpServerStaticIpName_Object = MibTableColumn
mitelDhcpServerStaticIpName = _MitelDhcpServerStaticIpName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4, 1, 7),
    _MitelDhcpServerStaticIpName_Type()
)
mitelDhcpServerStaticIpName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpName.setStatus("current")


class _MitelDhcpServerStaticIpDeleteTree_Type(Integer32):
    """Custom type mitelDhcpServerStaticIpDeleteTree based on Integer32"""
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


_MitelDhcpServerStaticIpDeleteTree_Type.__name__ = "Integer32"
_MitelDhcpServerStaticIpDeleteTree_Object = MibTableColumn
mitelDhcpServerStaticIpDeleteTree = _MitelDhcpServerStaticIpDeleteTree_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4, 1, 8),
    _MitelDhcpServerStaticIpDeleteTree_Type()
)
mitelDhcpServerStaticIpDeleteTree.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpDeleteTree.setStatus("current")
_MitelDhcpServerStaticIpStatus_Type = RowStatus
_MitelDhcpServerStaticIpStatus_Object = MibTableColumn
mitelDhcpServerStaticIpStatus = _MitelDhcpServerStaticIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 4, 1, 9),
    _MitelDhcpServerStaticIpStatus_Type()
)
mitelDhcpServerStaticIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelDhcpServerStaticIpStatus.setStatus("current")
_MitelDhcpServerOptionTable_Object = MibTable
mitelDhcpServerOptionTable = _MitelDhcpServerOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 5)
)
if mibBuilder.loadTexts:
    mitelDhcpServerOptionTable.setStatus("current")
_MitelDhcpServerOptionEntry_Object = MibTableRow
mitelDhcpServerOptionEntry = _MitelDhcpServerOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 5, 1)
)
mitelDhcpServerOptionEntry.setIndexNames(
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerOptionAddr"),
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerOptionNumber"),
)
if mibBuilder.loadTexts:
    mitelDhcpServerOptionEntry.setStatus("current")
_MitelDhcpServerOptionAddr_Type = IpAddress
_MitelDhcpServerOptionAddr_Object = MibTableColumn
mitelDhcpServerOptionAddr = _MitelDhcpServerOptionAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 5, 1, 1),
    _MitelDhcpServerOptionAddr_Type()
)
mitelDhcpServerOptionAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerOptionAddr.setStatus("current")
_MitelDhcpServerOptionNumber_Type = MitelDhcpServerOptionList
_MitelDhcpServerOptionNumber_Object = MibTableColumn
mitelDhcpServerOptionNumber = _MitelDhcpServerOptionNumber_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 5, 1, 2),
    _MitelDhcpServerOptionNumber_Type()
)
mitelDhcpServerOptionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerOptionNumber.setStatus("current")


class _MitelDhcpServerOptionDisplayFormat_Type(Integer32):
    """Custom type mitelDhcpServerOptionDisplayFormat based on Integer32"""
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
        *(("ascii-string", 3),
          ("default", 1),
          ("integer", 4),
          ("ip-address", 2),
          ("octet-string", 5))
    )


_MitelDhcpServerOptionDisplayFormat_Type.__name__ = "Integer32"
_MitelDhcpServerOptionDisplayFormat_Object = MibTableColumn
mitelDhcpServerOptionDisplayFormat = _MitelDhcpServerOptionDisplayFormat_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 5, 1, 3),
    _MitelDhcpServerOptionDisplayFormat_Type()
)
mitelDhcpServerOptionDisplayFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerOptionDisplayFormat.setStatus("current")


class _MitelDhcpServerOptionValue_Type(OctetString):
    """Custom type mitelDhcpServerOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MitelDhcpServerOptionValue_Type.__name__ = "OctetString"
_MitelDhcpServerOptionValue_Object = MibTableColumn
mitelDhcpServerOptionValue = _MitelDhcpServerOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 5, 1, 4),
    _MitelDhcpServerOptionValue_Type()
)
mitelDhcpServerOptionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerOptionValue.setStatus("current")
_MitelDhcpServerOptionStatus_Type = RowStatus
_MitelDhcpServerOptionStatus_Object = MibTableColumn
mitelDhcpServerOptionStatus = _MitelDhcpServerOptionStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 5, 1, 5),
    _MitelDhcpServerOptionStatus_Type()
)
mitelDhcpServerOptionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelDhcpServerOptionStatus.setStatus("current")
_MitelDhcpServerLeaseTable_Object = MibTable
mitelDhcpServerLeaseTable = _MitelDhcpServerLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6)
)
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseTable.setStatus("current")
_MitelDhcpServerLeaseEntry_Object = MibTableRow
mitelDhcpServerLeaseEntry = _MitelDhcpServerLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1)
)
mitelDhcpServerLeaseEntry.setIndexNames(
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerLeaseAddr"),
)
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseEntry.setStatus("current")
_MitelDhcpServerLeaseAddr_Type = IpAddress
_MitelDhcpServerLeaseAddr_Object = MibTableColumn
mitelDhcpServerLeaseAddr = _MitelDhcpServerLeaseAddr_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 1),
    _MitelDhcpServerLeaseAddr_Type()
)
mitelDhcpServerLeaseAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseAddr.setStatus("current")
_MitelDhcpServerLeaseSubnet_Type = IpAddress
_MitelDhcpServerLeaseSubnet_Object = MibTableColumn
mitelDhcpServerLeaseSubnet = _MitelDhcpServerLeaseSubnet_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 2),
    _MitelDhcpServerLeaseSubnet_Type()
)
mitelDhcpServerLeaseSubnet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseSubnet.setStatus("current")
_MitelDhcpServerLeaseRange_Type = IpAddress
_MitelDhcpServerLeaseRange_Object = MibTableColumn
mitelDhcpServerLeaseRange = _MitelDhcpServerLeaseRange_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 3),
    _MitelDhcpServerLeaseRange_Type()
)
mitelDhcpServerLeaseRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseRange.setStatus("current")


class _MitelDhcpServerLeaseType_Type(Integer32):
    """Custom type mitelDhcpServerLeaseType based on Integer32"""
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
        *(("configuration-reserved", 3),
          ("dynamic", 2),
          ("server-reserved", 4),
          ("static", 1))
    )


_MitelDhcpServerLeaseType_Type.__name__ = "Integer32"
_MitelDhcpServerLeaseType_Object = MibTableColumn
mitelDhcpServerLeaseType = _MitelDhcpServerLeaseType_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 4),
    _MitelDhcpServerLeaseType_Type()
)
mitelDhcpServerLeaseType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseType.setStatus("current")
_MitelDhcpServerLeaseEndTime_Type = TimeTicks
_MitelDhcpServerLeaseEndTime_Object = MibTableColumn
mitelDhcpServerLeaseEndTime = _MitelDhcpServerLeaseEndTime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 5),
    _MitelDhcpServerLeaseEndTime_Type()
)
mitelDhcpServerLeaseEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseEndTime.setStatus("current")


class _MitelDhcpServerLeaseAllowedProtocol_Type(Integer32):
    """Custom type mitelDhcpServerLeaseAllowedProtocol based on Integer32"""
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
        *(("bootp", 2),
          ("bootp-or-dhcp", 4),
          ("dhcp", 3),
          ("none", 1))
    )


_MitelDhcpServerLeaseAllowedProtocol_Type.__name__ = "Integer32"
_MitelDhcpServerLeaseAllowedProtocol_Object = MibTableColumn
mitelDhcpServerLeaseAllowedProtocol = _MitelDhcpServerLeaseAllowedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 6),
    _MitelDhcpServerLeaseAllowedProtocol_Type()
)
mitelDhcpServerLeaseAllowedProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseAllowedProtocol.setStatus("current")


class _MitelDhcpServerLeaseServedProtocol_Type(Integer32):
    """Custom type mitelDhcpServerLeaseServedProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bootp", 2),
          ("dhcp", 3),
          ("none", 1))
    )


_MitelDhcpServerLeaseServedProtocol_Type.__name__ = "Integer32"
_MitelDhcpServerLeaseServedProtocol_Object = MibTableColumn
mitelDhcpServerLeaseServedProtocol = _MitelDhcpServerLeaseServedProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 7),
    _MitelDhcpServerLeaseServedProtocol_Type()
)
mitelDhcpServerLeaseServedProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseServedProtocol.setStatus("current")


class _MitelDhcpServerLeaseMacAddress_Type(OctetString):
    """Custom type mitelDhcpServerLeaseMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MitelDhcpServerLeaseMacAddress_Type.__name__ = "OctetString"
_MitelDhcpServerLeaseMacAddress_Object = MibTableColumn
mitelDhcpServerLeaseMacAddress = _MitelDhcpServerLeaseMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 8),
    _MitelDhcpServerLeaseMacAddress_Type()
)
mitelDhcpServerLeaseMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseMacAddress.setStatus("current")


class _MitelDhcpServerLeaseClientId_Type(OctetString):
    """Custom type mitelDhcpServerLeaseClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MitelDhcpServerLeaseClientId_Type.__name__ = "OctetString"
_MitelDhcpServerLeaseClientId_Object = MibTableColumn
mitelDhcpServerLeaseClientId = _MitelDhcpServerLeaseClientId_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 9),
    _MitelDhcpServerLeaseClientId_Type()
)
mitelDhcpServerLeaseClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseClientId.setStatus("current")


class _MitelDhcpServerLeaseHostName_Type(DisplayString):
    """Custom type mitelDhcpServerLeaseHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_MitelDhcpServerLeaseHostName_Type.__name__ = "DisplayString"
_MitelDhcpServerLeaseHostName_Object = MibTableColumn
mitelDhcpServerLeaseHostName = _MitelDhcpServerLeaseHostName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 10),
    _MitelDhcpServerLeaseHostName_Type()
)
mitelDhcpServerLeaseHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseHostName.setStatus("current")


class _MitelDhcpServerLeaseDomainName_Type(DisplayString):
    """Custom type mitelDhcpServerLeaseDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MitelDhcpServerLeaseDomainName_Type.__name__ = "DisplayString"
_MitelDhcpServerLeaseDomainName_Object = MibTableColumn
mitelDhcpServerLeaseDomainName = _MitelDhcpServerLeaseDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 11),
    _MitelDhcpServerLeaseDomainName_Type()
)
mitelDhcpServerLeaseDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseDomainName.setStatus("current")
_MitelDhcpServerLeaseServedTime_Type = Integer32
_MitelDhcpServerLeaseServedTime_Object = MibTableColumn
mitelDhcpServerLeaseServedTime = _MitelDhcpServerLeaseServedTime_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 12),
    _MitelDhcpServerLeaseServedTime_Type()
)
mitelDhcpServerLeaseServedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseServedTime.setStatus("current")
_MitelDhcpServerLeaseStatus_Type = RowStatus
_MitelDhcpServerLeaseStatus_Object = MibTableColumn
mitelDhcpServerLeaseStatus = _MitelDhcpServerLeaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 6, 1, 13),
    _MitelDhcpServerLeaseStatus_Type()
)
mitelDhcpServerLeaseStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelDhcpServerLeaseStatus.setStatus("current")
_MitelDhcpServerStatsGroup_ObjectIdentity = ObjectIdentity
mitelDhcpServerStatsGroup = _MitelDhcpServerStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 7)
)
_MitelDhcpServerStatsNumServers_Type = Integer32
_MitelDhcpServerStatsNumServers_Object = MibScalar
mitelDhcpServerStatsNumServers = _MitelDhcpServerStatsNumServers_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 7, 1),
    _MitelDhcpServerStatsNumServers_Type()
)
mitelDhcpServerStatsNumServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerStatsNumServers.setStatus("current")
_MitelDhcpServerStatsConfSubnets_Type = Integer32
_MitelDhcpServerStatsConfSubnets_Object = MibScalar
mitelDhcpServerStatsConfSubnets = _MitelDhcpServerStatsConfSubnets_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 7, 2),
    _MitelDhcpServerStatsConfSubnets_Type()
)
mitelDhcpServerStatsConfSubnets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerStatsConfSubnets.setStatus("current")
_MitelDhcpServerStatsConfRanges_Type = Integer32
_MitelDhcpServerStatsConfRanges_Object = MibScalar
mitelDhcpServerStatsConfRanges = _MitelDhcpServerStatsConfRanges_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 7, 3),
    _MitelDhcpServerStatsConfRanges_Type()
)
mitelDhcpServerStatsConfRanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerStatsConfRanges.setStatus("current")
_MitelDhcpServerStatsConfStatic_Type = Integer32
_MitelDhcpServerStatsConfStatic_Object = MibScalar
mitelDhcpServerStatsConfStatic = _MitelDhcpServerStatsConfStatic_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 7, 4),
    _MitelDhcpServerStatsConfStatic_Type()
)
mitelDhcpServerStatsConfStatic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerStatsConfStatic.setStatus("current")
_MitelDhcpServerStatsConfOptions_Type = Integer32
_MitelDhcpServerStatsConfOptions_Object = MibScalar
mitelDhcpServerStatsConfOptions = _MitelDhcpServerStatsConfOptions_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 7, 5),
    _MitelDhcpServerStatsConfOptions_Type()
)
mitelDhcpServerStatsConfOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerStatsConfOptions.setStatus("current")
_MitelDhcpServerStatsConfLeases_Type = Integer32
_MitelDhcpServerStatsConfLeases_Object = MibScalar
mitelDhcpServerStatsConfLeases = _MitelDhcpServerStatsConfLeases_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 7, 6),
    _MitelDhcpServerStatsConfLeases_Type()
)
mitelDhcpServerStatsConfLeases.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerStatsConfLeases.setStatus("current")
_MitelDhcpServerVendorInfoTable_Object = MibTable
mitelDhcpServerVendorInfoTable = _MitelDhcpServerVendorInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 8)
)
if mibBuilder.loadTexts:
    mitelDhcpServerVendorInfoTable.setStatus("current")
_MitelDhcpServerVendorInfoEntry_Object = MibTableRow
mitelDhcpServerVendorInfoEntry = _MitelDhcpServerVendorInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 8, 1)
)
mitelDhcpServerVendorInfoEntry.setIndexNames(
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerOptionAddr"),
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerOptionNumber"),
    (0, "MITEL-DHCP-MIB", "mitelDhcpServerVendorInfoID"),
)
if mibBuilder.loadTexts:
    mitelDhcpServerVendorInfoEntry.setStatus("current")


class _MitelDhcpServerVendorInfoID_Type(DisplayString):
    """Custom type mitelDhcpServerVendorInfoID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MitelDhcpServerVendorInfoID_Type.__name__ = "DisplayString"
_MitelDhcpServerVendorInfoID_Object = MibTableColumn
mitelDhcpServerVendorInfoID = _MitelDhcpServerVendorInfoID_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 8, 1, 1),
    _MitelDhcpServerVendorInfoID_Type()
)
mitelDhcpServerVendorInfoID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerVendorInfoID.setStatus("current")


class _MitelDhcpServerVendorInfoName_Type(DisplayString):
    """Custom type mitelDhcpServerVendorInfoName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MitelDhcpServerVendorInfoName_Type.__name__ = "DisplayString"
_MitelDhcpServerVendorInfoName_Object = MibTableColumn
mitelDhcpServerVendorInfoName = _MitelDhcpServerVendorInfoName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 8, 1, 2),
    _MitelDhcpServerVendorInfoName_Type()
)
mitelDhcpServerVendorInfoName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpServerVendorInfoName.setStatus("current")


class _MitelDhcpServerVendorInfoOptionDisplayFormat_Type(Integer32):
    """Custom type mitelDhcpServerVendorInfoOptionDisplayFormat based on Integer32"""
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
        *(("ascii-string", 3),
          ("default", 1),
          ("integer", 4),
          ("ip-address", 2),
          ("octet-string", 5))
    )


_MitelDhcpServerVendorInfoOptionDisplayFormat_Type.__name__ = "Integer32"
_MitelDhcpServerVendorInfoOptionDisplayFormat_Object = MibTableColumn
mitelDhcpServerVendorInfoOptionDisplayFormat = _MitelDhcpServerVendorInfoOptionDisplayFormat_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 8, 1, 3),
    _MitelDhcpServerVendorInfoOptionDisplayFormat_Type()
)
mitelDhcpServerVendorInfoOptionDisplayFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerVendorInfoOptionDisplayFormat.setStatus("current")


class _MitelDhcpServerVendorInfoOptionValue_Type(OctetString):
    """Custom type mitelDhcpServerVendorInfoOptionValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_MitelDhcpServerVendorInfoOptionValue_Type.__name__ = "OctetString"
_MitelDhcpServerVendorInfoOptionValue_Object = MibScalar
mitelDhcpServerVendorInfoOptionValue = _MitelDhcpServerVendorInfoOptionValue_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 8, 1, 4),
    _MitelDhcpServerVendorInfoOptionValue_Type()
)
mitelDhcpServerVendorInfoOptionValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpServerVendorInfoOptionValue.setStatus("current")
_MitelDhcpServerVendorInfoStatus_Type = RowStatus
_MitelDhcpServerVendorInfoStatus_Object = MibTableColumn
mitelDhcpServerVendorInfoStatus = _MitelDhcpServerVendorInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 5, 8, 1, 5),
    _MitelDhcpServerVendorInfoStatus_Type()
)
mitelDhcpServerVendorInfoStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mitelDhcpServerVendorInfoStatus.setStatus("current")
_MitelDhcpClientTable_Object = MibTable
mitelDhcpClientTable = _MitelDhcpClientTable_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6)
)
if mibBuilder.loadTexts:
    mitelDhcpClientTable.setStatus("current")
_MitelDhcpClientEntry_Object = MibTableRow
mitelDhcpClientEntry = _MitelDhcpClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1)
)
mitelDhcpClientEntry.setIndexNames(
    (0, "MITEL-DHCP-MIB", "mitelDhcpClientIndex"),
)
if mibBuilder.loadTexts:
    mitelDhcpClientEntry.setStatus("current")
_MitelDhcpClientIndex_Type = Integer32
_MitelDhcpClientIndex_Object = MibTableColumn
mitelDhcpClientIndex = _MitelDhcpClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 1),
    _MitelDhcpClientIndex_Type()
)
mitelDhcpClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientIndex.setStatus("current")
_MitelDhcpClientId_Type = OctetString
_MitelDhcpClientId_Object = MibTableColumn
mitelDhcpClientId = _MitelDhcpClientId_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 2),
    _MitelDhcpClientId_Type()
)
mitelDhcpClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mitelDhcpClientId.setStatus("current")


class _MitelDhcpClientLeaseAction_Type(Integer32):
    """Custom type mitelDhcpClientLeaseAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("release", 2),
          ("renew", 3))
    )


_MitelDhcpClientLeaseAction_Type.__name__ = "Integer32"
_MitelDhcpClientLeaseAction_Object = MibTableColumn
mitelDhcpClientLeaseAction = _MitelDhcpClientLeaseAction_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 3),
    _MitelDhcpClientLeaseAction_Type()
)
mitelDhcpClientLeaseAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientLeaseAction.setStatus("current")
_MitelDhcpClientIpAddress_Type = IpAddress
_MitelDhcpClientIpAddress_Object = MibTableColumn
mitelDhcpClientIpAddress = _MitelDhcpClientIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 4),
    _MitelDhcpClientIpAddress_Type()
)
mitelDhcpClientIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientIpAddress.setStatus("current")
_MitelDhcpClientLeaseObtained_Type = TimeTicks
_MitelDhcpClientLeaseObtained_Object = MibTableColumn
mitelDhcpClientLeaseObtained = _MitelDhcpClientLeaseObtained_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 5),
    _MitelDhcpClientLeaseObtained_Type()
)
mitelDhcpClientLeaseObtained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientLeaseObtained.setStatus("current")
_MitelDhcpClientLeaseExpired_Type = TimeTicks
_MitelDhcpClientLeaseExpired_Object = MibTableColumn
mitelDhcpClientLeaseExpired = _MitelDhcpClientLeaseExpired_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 6),
    _MitelDhcpClientLeaseExpired_Type()
)
mitelDhcpClientLeaseExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientLeaseExpired.setStatus("current")
_MitelDhcpClientDefaultGateway_Type = IpAddress
_MitelDhcpClientDefaultGateway_Object = MibTableColumn
mitelDhcpClientDefaultGateway = _MitelDhcpClientDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 7),
    _MitelDhcpClientDefaultGateway_Type()
)
mitelDhcpClientDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientDefaultGateway.setStatus("current")
_MitelDhcpClientServerIp_Type = IpAddress
_MitelDhcpClientServerIp_Object = MibTableColumn
mitelDhcpClientServerIp = _MitelDhcpClientServerIp_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 8),
    _MitelDhcpClientServerIp_Type()
)
mitelDhcpClientServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientServerIp.setStatus("current")
_MitelDhcpClientPrimaryDns_Type = IpAddress
_MitelDhcpClientPrimaryDns_Object = MibTableColumn
mitelDhcpClientPrimaryDns = _MitelDhcpClientPrimaryDns_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 9),
    _MitelDhcpClientPrimaryDns_Type()
)
mitelDhcpClientPrimaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientPrimaryDns.setStatus("current")
_MitelDhcpClientSecondaryDns_Type = IpAddress
_MitelDhcpClientSecondaryDns_Object = MibTableColumn
mitelDhcpClientSecondaryDns = _MitelDhcpClientSecondaryDns_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 10),
    _MitelDhcpClientSecondaryDns_Type()
)
mitelDhcpClientSecondaryDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientSecondaryDns.setStatus("current")
_MitelDhcpClientPrimaryWins_Type = IpAddress
_MitelDhcpClientPrimaryWins_Object = MibTableColumn
mitelDhcpClientPrimaryWins = _MitelDhcpClientPrimaryWins_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 11),
    _MitelDhcpClientPrimaryWins_Type()
)
mitelDhcpClientPrimaryWins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientPrimaryWins.setStatus("current")
_MitelDhcpClientSecondaryWins_Type = IpAddress
_MitelDhcpClientSecondaryWins_Object = MibTableColumn
mitelDhcpClientSecondaryWins = _MitelDhcpClientSecondaryWins_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 12),
    _MitelDhcpClientSecondaryWins_Type()
)
mitelDhcpClientSecondaryWins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientSecondaryWins.setStatus("current")
_MitelDhcpClientDomainName_Type = OctetString
_MitelDhcpClientDomainName_Object = MibTableColumn
mitelDhcpClientDomainName = _MitelDhcpClientDomainName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 13),
    _MitelDhcpClientDomainName_Type()
)
mitelDhcpClientDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientDomainName.setStatus("current")
_MitelDhcpClientName_Type = OctetString
_MitelDhcpClientName_Object = MibTableColumn
mitelDhcpClientName = _MitelDhcpClientName_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 14),
    _MitelDhcpClientName_Type()
)
mitelDhcpClientName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientName.setStatus("current")


class _MitelDhcpClientAdminState_Type(Integer32):
    """Custom type mitelDhcpClientAdminState based on Integer32"""
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


_MitelDhcpClientAdminState_Type.__name__ = "Integer32"
_MitelDhcpClientAdminState_Object = MibTableColumn
mitelDhcpClientAdminState = _MitelDhcpClientAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1027, 4, 8, 1, 3, 6, 1, 15),
    _MitelDhcpClientAdminState_Type()
)
mitelDhcpClientAdminState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mitelDhcpClientAdminState.setStatus("current")

# Managed Objects groups


# Notification objects

mitelDhcpClientObtainedIp = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 404)
)
mitelDhcpClientObtainedIp.setObjects(
      *(("MITEL-DHCP-MIB", "mitelDhcpClientIndex"),
        ("MITEL-DHCP-MIB", "mitelDhcpClientIpAddress"),
        ("MITEL-DHCP-MIB", "mitelDhcpClientServerIp"))
)
if mibBuilder.loadTexts:
    mitelDhcpClientObtainedIp.setStatus(
        "current"
    )

mitelDhcpClientLeaseExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0, 405)
)
mitelDhcpClientLeaseExpiry.setObjects(
    ("MITEL-DHCP-MIB", "mitelDhcpClientIndex")
)
if mibBuilder.loadTexts:
    mitelDhcpClientLeaseExpiry.setStatus(
        "current"
    )


# Notifications groups

mitelIpera1000Notifications = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1027, 1, 2, 4, 0)
)
mitelIpera1000Notifications.setObjects(
      *(("MITEL-DHCP-MIB", "mitelDhcpClientObtainedIp"),
        ("MITEL-DHCP-MIB", "mitelDhcpClientLeaseExpiry"))
)
if mibBuilder.loadTexts:
    mitelIpera1000Notifications.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MITEL-DHCP-MIB",
    **{"MitelDhcpServerProtocol": MitelDhcpServerProtocol,
       "MitelDhcpServerOptionList": MitelDhcpServerOptionList,
       "mitel": mitel,
       "mitelIdentification": mitelIdentification,
       "mitelIdCallServers": mitelIdCallServers,
       "mitelIdCsIpera1000": mitelIdCsIpera1000,
       "mitelIpera1000Notifications": mitelIpera1000Notifications,
       "mitelDhcpClientObtainedIp": mitelDhcpClientObtainedIp,
       "mitelDhcpClientLeaseExpiry": mitelDhcpClientLeaseExpiry,
       "mitelProprietary": mitelProprietary,
       "mitelPropIpNetworking": mitelPropIpNetworking,
       "mitelIpNetRouter": mitelIpNetRouter,
       "mitelRouterDhcpGroup": mitelRouterDhcpGroup,
       "mitelDhcpRelayAgentEnable": mitelDhcpRelayAgentEnable,
       "mitelDhcpRelayAgentMaxHops": mitelDhcpRelayAgentMaxHops,
       "mitelDhcpRelayAgentServerTable": mitelDhcpRelayAgentServerTable,
       "mitelDhcpRelayAgentServerEntry": mitelDhcpRelayAgentServerEntry,
       "mitelDhcpRelayAgentServerAddr": mitelDhcpRelayAgentServerAddr,
       "mitelDhcpRelayAgentServerName": mitelDhcpRelayAgentServerName,
       "mitelDhcpRelayAgentServerStatus": mitelDhcpRelayAgentServerStatus,
       "mitelDhcpRelayAgentBroadcast": mitelDhcpRelayAgentBroadcast,
       "mitelDhcpServerGroup": mitelDhcpServerGroup,
       "mitelDhcpServerGeneralGroup": mitelDhcpServerGeneralGroup,
       "mitelDhcpServerGeneralEnable": mitelDhcpServerGeneralEnable,
       "mitelDhcpServerGeneralGateway": mitelDhcpServerGeneralGateway,
       "mitelDhcpServerGeneralRefDhcpServer": mitelDhcpServerGeneralRefDhcpServer,
       "mitelDhcpServerGeneralPingStatus": mitelDhcpServerGeneralPingStatus,
       "mitelDhcpServerSubnetTable": mitelDhcpServerSubnetTable,
       "mitelDhcpServerSubnetEntry": mitelDhcpServerSubnetEntry,
       "mitelDhcpServerSubnetAddr": mitelDhcpServerSubnetAddr,
       "mitelDhcpServerSubnetSharedNet": mitelDhcpServerSubnetSharedNet,
       "mitelDhcpServerSubnetMask": mitelDhcpServerSubnetMask,
       "mitelDhcpServerSubnetGateway": mitelDhcpServerSubnetGateway,
       "mitelDhcpServerSubnetName": mitelDhcpServerSubnetName,
       "mitelDhcpServerSubnetDeleteTree": mitelDhcpServerSubnetDeleteTree,
       "mitelDhcpServerSubnetStatus": mitelDhcpServerSubnetStatus,
       "mitelDhcpServerRangeTable": mitelDhcpServerRangeTable,
       "mitelDhcpServerRangeEntry": mitelDhcpServerRangeEntry,
       "mitelDhcpServerRangeStart": mitelDhcpServerRangeStart,
       "mitelDhcpServerRangeEnd": mitelDhcpServerRangeEnd,
       "mitelDhcpServerRangeSubnet": mitelDhcpServerRangeSubnet,
       "mitelDhcpServerRangeProtocol": mitelDhcpServerRangeProtocol,
       "mitelDhcpServerRangeGateway": mitelDhcpServerRangeGateway,
       "mitelDhcpServerRangeLeaseTime": mitelDhcpServerRangeLeaseTime,
       "mitelDhcpServerRangeName": mitelDhcpServerRangeName,
       "mitelDhcpServerRangeMatchClassId": mitelDhcpServerRangeMatchClassId,
       "mitelDhcpServerRangeDeleteTree": mitelDhcpServerRangeDeleteTree,
       "mitelDhcpServerRangeStatus": mitelDhcpServerRangeStatus,
       "mitelDhcpServerStaticIpTable": mitelDhcpServerStaticIpTable,
       "mitelDhcpServerStaticIpEntry": mitelDhcpServerStaticIpEntry,
       "mitelDhcpServerStaticIpAddr": mitelDhcpServerStaticIpAddr,
       "mitelDhcpServerStaticIpSubnet": mitelDhcpServerStaticIpSubnet,
       "mitelDhcpServerStaticIpProtocol": mitelDhcpServerStaticIpProtocol,
       "mitelDhcpServerStaticIpGateway": mitelDhcpServerStaticIpGateway,
       "mitelDhcpServerStaticIpMacAddress": mitelDhcpServerStaticIpMacAddress,
       "mitelDhcpServerStaticIpClientId": mitelDhcpServerStaticIpClientId,
       "mitelDhcpServerStaticIpName": mitelDhcpServerStaticIpName,
       "mitelDhcpServerStaticIpDeleteTree": mitelDhcpServerStaticIpDeleteTree,
       "mitelDhcpServerStaticIpStatus": mitelDhcpServerStaticIpStatus,
       "mitelDhcpServerOptionTable": mitelDhcpServerOptionTable,
       "mitelDhcpServerOptionEntry": mitelDhcpServerOptionEntry,
       "mitelDhcpServerOptionAddr": mitelDhcpServerOptionAddr,
       "mitelDhcpServerOptionNumber": mitelDhcpServerOptionNumber,
       "mitelDhcpServerOptionDisplayFormat": mitelDhcpServerOptionDisplayFormat,
       "mitelDhcpServerOptionValue": mitelDhcpServerOptionValue,
       "mitelDhcpServerOptionStatus": mitelDhcpServerOptionStatus,
       "mitelDhcpServerLeaseTable": mitelDhcpServerLeaseTable,
       "mitelDhcpServerLeaseEntry": mitelDhcpServerLeaseEntry,
       "mitelDhcpServerLeaseAddr": mitelDhcpServerLeaseAddr,
       "mitelDhcpServerLeaseSubnet": mitelDhcpServerLeaseSubnet,
       "mitelDhcpServerLeaseRange": mitelDhcpServerLeaseRange,
       "mitelDhcpServerLeaseType": mitelDhcpServerLeaseType,
       "mitelDhcpServerLeaseEndTime": mitelDhcpServerLeaseEndTime,
       "mitelDhcpServerLeaseAllowedProtocol": mitelDhcpServerLeaseAllowedProtocol,
       "mitelDhcpServerLeaseServedProtocol": mitelDhcpServerLeaseServedProtocol,
       "mitelDhcpServerLeaseMacAddress": mitelDhcpServerLeaseMacAddress,
       "mitelDhcpServerLeaseClientId": mitelDhcpServerLeaseClientId,
       "mitelDhcpServerLeaseHostName": mitelDhcpServerLeaseHostName,
       "mitelDhcpServerLeaseDomainName": mitelDhcpServerLeaseDomainName,
       "mitelDhcpServerLeaseServedTime": mitelDhcpServerLeaseServedTime,
       "mitelDhcpServerLeaseStatus": mitelDhcpServerLeaseStatus,
       "mitelDhcpServerStatsGroup": mitelDhcpServerStatsGroup,
       "mitelDhcpServerStatsNumServers": mitelDhcpServerStatsNumServers,
       "mitelDhcpServerStatsConfSubnets": mitelDhcpServerStatsConfSubnets,
       "mitelDhcpServerStatsConfRanges": mitelDhcpServerStatsConfRanges,
       "mitelDhcpServerStatsConfStatic": mitelDhcpServerStatsConfStatic,
       "mitelDhcpServerStatsConfOptions": mitelDhcpServerStatsConfOptions,
       "mitelDhcpServerStatsConfLeases": mitelDhcpServerStatsConfLeases,
       "mitelDhcpServerVendorInfoTable": mitelDhcpServerVendorInfoTable,
       "mitelDhcpServerVendorInfoEntry": mitelDhcpServerVendorInfoEntry,
       "mitelDhcpServerVendorInfoID": mitelDhcpServerVendorInfoID,
       "mitelDhcpServerVendorInfoName": mitelDhcpServerVendorInfoName,
       "mitelDhcpServerVendorInfoOptionDisplayFormat": mitelDhcpServerVendorInfoOptionDisplayFormat,
       "mitelDhcpServerVendorInfoOptionValue": mitelDhcpServerVendorInfoOptionValue,
       "mitelDhcpServerVendorInfoStatus": mitelDhcpServerVendorInfoStatus,
       "mitelDhcpClientTable": mitelDhcpClientTable,
       "mitelDhcpClientEntry": mitelDhcpClientEntry,
       "mitelDhcpClientIndex": mitelDhcpClientIndex,
       "mitelDhcpClientId": mitelDhcpClientId,
       "mitelDhcpClientLeaseAction": mitelDhcpClientLeaseAction,
       "mitelDhcpClientIpAddress": mitelDhcpClientIpAddress,
       "mitelDhcpClientLeaseObtained": mitelDhcpClientLeaseObtained,
       "mitelDhcpClientLeaseExpired": mitelDhcpClientLeaseExpired,
       "mitelDhcpClientDefaultGateway": mitelDhcpClientDefaultGateway,
       "mitelDhcpClientServerIp": mitelDhcpClientServerIp,
       "mitelDhcpClientPrimaryDns": mitelDhcpClientPrimaryDns,
       "mitelDhcpClientSecondaryDns": mitelDhcpClientSecondaryDns,
       "mitelDhcpClientPrimaryWins": mitelDhcpClientPrimaryWins,
       "mitelDhcpClientSecondaryWins": mitelDhcpClientSecondaryWins,
       "mitelDhcpClientDomainName": mitelDhcpClientDomainName,
       "mitelDhcpClientName": mitelDhcpClientName,
       "mitelDhcpClientAdminState": mitelDhcpClientAdminState}
)
