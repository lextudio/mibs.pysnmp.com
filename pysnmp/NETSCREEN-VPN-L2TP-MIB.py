# SNMP MIB module (NETSCREEN-VPN-L2TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETSCREEN-VPN-L2TP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:04 2024
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

(netscreenVpn,
 netscreenVpnMibModule) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenVpn",
    "netscreenVpnMibModule")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

netscreenVpnL2tpMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 0, 8)
)
netscreenVpnL2tpMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2000-08-27 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsVpnL2TP_ObjectIdentity = ObjectIdentity
nsVpnL2TP = _NsVpnL2TP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8)
)
_NsVpnL2tpDefTable_Object = MibTable
nsVpnL2tpDefTable = _NsVpnL2tpDefTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1)
)
if mibBuilder.loadTexts:
    nsVpnL2tpDefTable.setStatus("current")
_NsVpnL2tpDefEntry_Object = MibTableRow
nsVpnL2tpDefEntry = _NsVpnL2tpDefEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1, 1)
)
nsVpnL2tpDefEntry.setIndexNames(
    (0, "NETSCREEN-VPN-L2TP-MIB", "nsVpnL2tpDefVsys"),
)
if mibBuilder.loadTexts:
    nsVpnL2tpDefEntry.setStatus("current")


class _NsVpnL2tpDefVsys_Type(Integer32):
    """Custom type nsVpnL2tpDefVsys based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnL2tpDefVsys_Type.__name__ = "Integer32"
_NsVpnL2tpDefVsys_Object = MibTableColumn
nsVpnL2tpDefVsys = _NsVpnL2tpDefVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1, 1, 1),
    _NsVpnL2tpDefVsys_Type()
)
nsVpnL2tpDefVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpDefVsys.setStatus("current")


class _NsVpnL2tpDefPool_Type(DisplayString):
    """Custom type nsVpnL2tpDefPool based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnL2tpDefPool_Type.__name__ = "DisplayString"
_NsVpnL2tpDefPool_Object = MibTableColumn
nsVpnL2tpDefPool = _NsVpnL2tpDefPool_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1, 1, 2),
    _NsVpnL2tpDefPool_Type()
)
nsVpnL2tpDefPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpDefPool.setStatus("current")


class _NsVpnL2tpDefAuthDb_Type(Integer32):
    """Custom type nsVpnL2tpDefAuthDb based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("local", 0),
          ("radius", 1))
    )


_NsVpnL2tpDefAuthDb_Type.__name__ = "Integer32"
_NsVpnL2tpDefAuthDb_Object = MibTableColumn
nsVpnL2tpDefAuthDb = _NsVpnL2tpDefAuthDb_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1, 1, 3),
    _NsVpnL2tpDefAuthDb_Type()
)
nsVpnL2tpDefAuthDb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpDefAuthDb.setStatus("current")


class _NsVpnL2tpDefPPPAuth_Type(Integer32):
    """Custom type nsVpnL2tpDefPPPAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("any", 3),
          ("chap", 2),
          ("pap", 1))
    )


_NsVpnL2tpDefPPPAuth_Type.__name__ = "Integer32"
_NsVpnL2tpDefPPPAuth_Object = MibTableColumn
nsVpnL2tpDefPPPAuth = _NsVpnL2tpDefPPPAuth_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1, 1, 4),
    _NsVpnL2tpDefPPPAuth_Type()
)
nsVpnL2tpDefPPPAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpDefPPPAuth.setStatus("current")


class _NsVpnL2tpDefRadServer_Type(DisplayString):
    """Custom type nsVpnL2tpDefRadServer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnL2tpDefRadServer_Type.__name__ = "DisplayString"
_NsVpnL2tpDefRadServer_Object = MibTableColumn
nsVpnL2tpDefRadServer = _NsVpnL2tpDefRadServer_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1, 1, 5),
    _NsVpnL2tpDefRadServer_Type()
)
nsVpnL2tpDefRadServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpDefRadServer.setStatus("current")
_NsVpnL2tpDefPriDns_Type = IpAddress
_NsVpnL2tpDefPriDns_Object = MibTableColumn
nsVpnL2tpDefPriDns = _NsVpnL2tpDefPriDns_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1, 1, 6),
    _NsVpnL2tpDefPriDns_Type()
)
nsVpnL2tpDefPriDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpDefPriDns.setStatus("current")
_NsVpnL2tpDefSecDns_Type = IpAddress
_NsVpnL2tpDefSecDns_Object = MibTableColumn
nsVpnL2tpDefSecDns = _NsVpnL2tpDefSecDns_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1, 1, 7),
    _NsVpnL2tpDefSecDns_Type()
)
nsVpnL2tpDefSecDns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpDefSecDns.setStatus("current")
_NsVpnL2tpDefPriWins_Type = IpAddress
_NsVpnL2tpDefPriWins_Object = MibTableColumn
nsVpnL2tpDefPriWins = _NsVpnL2tpDefPriWins_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1, 1, 8),
    _NsVpnL2tpDefPriWins_Type()
)
nsVpnL2tpDefPriWins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpDefPriWins.setStatus("current")
_NsVpnL2tpDefSecWins_Type = IpAddress
_NsVpnL2tpDefSecWins_Object = MibTableColumn
nsVpnL2tpDefSecWins = _NsVpnL2tpDefSecWins_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 1, 1, 9),
    _NsVpnL2tpDefSecWins_Type()
)
nsVpnL2tpDefSecWins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpDefSecWins.setStatus("current")
_NsVpnL2tpTunnelTable_Object = MibTable
nsVpnL2tpTunnelTable = _NsVpnL2tpTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 2)
)
if mibBuilder.loadTexts:
    nsVpnL2tpTunnelTable.setStatus("current")
_NsVpnL2tpTunnelEntry_Object = MibTableRow
nsVpnL2tpTunnelEntry = _NsVpnL2tpTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 2, 1)
)
nsVpnL2tpTunnelEntry.setIndexNames(
    (0, "NETSCREEN-VPN-L2TP-MIB", "nsVpnL2tpTunIndex"),
)
if mibBuilder.loadTexts:
    nsVpnL2tpTunnelEntry.setStatus("current")


class _NsVpnL2tpTunIndex_Type(Integer32):
    """Custom type nsVpnL2tpTunIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_NsVpnL2tpTunIndex_Type.__name__ = "Integer32"
_NsVpnL2tpTunIndex_Object = MibTableColumn
nsVpnL2tpTunIndex = _NsVpnL2tpTunIndex_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 2, 1, 1),
    _NsVpnL2tpTunIndex_Type()
)
nsVpnL2tpTunIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpTunIndex.setStatus("current")
_NsVpnL2tpTunId_Type = Integer32
_NsVpnL2tpTunId_Object = MibTableColumn
nsVpnL2tpTunId = _NsVpnL2tpTunId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 2, 1, 2),
    _NsVpnL2tpTunId_Type()
)
nsVpnL2tpTunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpTunId.setStatus("current")


class _NsVpnL2tpTunName_Type(DisplayString):
    """Custom type nsVpnL2tpTunName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnL2tpTunName_Type.__name__ = "DisplayString"
_NsVpnL2tpTunName_Object = MibTableColumn
nsVpnL2tpTunName = _NsVpnL2tpTunName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 2, 1, 3),
    _NsVpnL2tpTunName_Type()
)
nsVpnL2tpTunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpTunName.setStatus("current")


class _NsVpnL2tpTunUsrOrGroup_Type(DisplayString):
    """Custom type nsVpnL2tpTunUsrOrGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnL2tpTunUsrOrGroup_Type.__name__ = "DisplayString"
_NsVpnL2tpTunUsrOrGroup_Object = MibTableColumn
nsVpnL2tpTunUsrOrGroup = _NsVpnL2tpTunUsrOrGroup_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 2, 1, 4),
    _NsVpnL2tpTunUsrOrGroup_Type()
)
nsVpnL2tpTunUsrOrGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpTunUsrOrGroup.setStatus("current")
_NsVpnL2tpTunPeerIp_Type = IpAddress
_NsVpnL2tpTunPeerIp_Object = MibTableColumn
nsVpnL2tpTunPeerIp = _NsVpnL2tpTunPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 2, 1, 5),
    _NsVpnL2tpTunPeerIp_Type()
)
nsVpnL2tpTunPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpTunPeerIp.setStatus("current")


class _NsVpnL2tpTunHost_Type(DisplayString):
    """Custom type nsVpnL2tpTunHost based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NsVpnL2tpTunHost_Type.__name__ = "DisplayString"
_NsVpnL2tpTunHost_Object = MibTableColumn
nsVpnL2tpTunHost = _NsVpnL2tpTunHost_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 2, 1, 6),
    _NsVpnL2tpTunHost_Type()
)
nsVpnL2tpTunHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpTunHost.setStatus("current")
_NsVpnL2tpTunKeepAlive_Type = Integer32
_NsVpnL2tpTunKeepAlive_Object = MibTableColumn
nsVpnL2tpTunKeepAlive = _NsVpnL2tpTunKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 2, 1, 7),
    _NsVpnL2tpTunKeepAlive_Type()
)
nsVpnL2tpTunKeepAlive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpTunKeepAlive.setStatus("current")
_NsVpnL2tpTunVsys_Type = Integer32
_NsVpnL2tpTunVsys_Object = MibTableColumn
nsVpnL2tpTunVsys = _NsVpnL2tpTunVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 2, 1, 8),
    _NsVpnL2tpTunVsys_Type()
)
nsVpnL2tpTunVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpTunVsys.setStatus("current")
_NsVpnL2tpMonTunnelTable_Object = MibTable
nsVpnL2tpMonTunnelTable = _NsVpnL2tpMonTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3)
)
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunnelTable.setStatus("current")
_NsVpnL2tpMonTunnelEntry_Object = MibTableRow
nsVpnL2tpMonTunnelEntry = _NsVpnL2tpMonTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3, 1)
)
nsVpnL2tpMonTunnelEntry.setIndexNames(
    (0, "NETSCREEN-VPN-L2TP-MIB", "nsVpnL2tpMonTunId"),
)
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunnelEntry.setStatus("current")
_NsVpnL2tpMonTunId_Type = Integer32
_NsVpnL2tpMonTunId_Object = MibTableColumn
nsVpnL2tpMonTunId = _NsVpnL2tpMonTunId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3, 1, 1),
    _NsVpnL2tpMonTunId_Type()
)
nsVpnL2tpMonTunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunId.setStatus("current")
_NsVpnL2tpMonTunPeerId_Type = Integer32
_NsVpnL2tpMonTunPeerId_Object = MibTableColumn
nsVpnL2tpMonTunPeerId = _NsVpnL2tpMonTunPeerId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3, 1, 2),
    _NsVpnL2tpMonTunPeerId_Type()
)
nsVpnL2tpMonTunPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunPeerId.setStatus("current")
_NsVpnL2tpMonTunName_Type = DisplayString
_NsVpnL2tpMonTunName_Object = MibTableColumn
nsVpnL2tpMonTunName = _NsVpnL2tpMonTunName_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3, 1, 3),
    _NsVpnL2tpMonTunName_Type()
)
nsVpnL2tpMonTunName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunName.setStatus("current")
_NsVpnL2tpMonTunPeerIp_Type = IpAddress
_NsVpnL2tpMonTunPeerIp_Object = MibTableColumn
nsVpnL2tpMonTunPeerIp = _NsVpnL2tpMonTunPeerIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3, 1, 4),
    _NsVpnL2tpMonTunPeerIp_Type()
)
nsVpnL2tpMonTunPeerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunPeerIp.setStatus("current")
_NsVpnL2tpMonTunPort_Type = Integer32
_NsVpnL2tpMonTunPort_Object = MibTableColumn
nsVpnL2tpMonTunPort = _NsVpnL2tpMonTunPort_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3, 1, 5),
    _NsVpnL2tpMonTunPort_Type()
)
nsVpnL2tpMonTunPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunPort.setStatus("current")
_NsVpnL2tpMonTunPeerHost_Type = DisplayString
_NsVpnL2tpMonTunPeerHost_Object = MibTableColumn
nsVpnL2tpMonTunPeerHost = _NsVpnL2tpMonTunPeerHost_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3, 1, 6),
    _NsVpnL2tpMonTunPeerHost_Type()
)
nsVpnL2tpMonTunPeerHost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunPeerHost.setStatus("current")
_NsVpnL2tpMonTunCalls_Type = Integer32
_NsVpnL2tpMonTunCalls_Object = MibTableColumn
nsVpnL2tpMonTunCalls = _NsVpnL2tpMonTunCalls_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3, 1, 7),
    _NsVpnL2tpMonTunCalls_Type()
)
nsVpnL2tpMonTunCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunCalls.setStatus("current")


class _NsVpnL2tpMonTunState_Type(Integer32):
    """Custom type nsVpnL2tpMonTunState based on Integer32"""
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
        *(("dead", 5),
          ("establish", 4),
          ("idle", 1),
          ("wait-conn", 3),
          ("wait-reply", 2))
    )


_NsVpnL2tpMonTunState_Type.__name__ = "Integer32"
_NsVpnL2tpMonTunState_Object = MibTableColumn
nsVpnL2tpMonTunState = _NsVpnL2tpMonTunState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3, 1, 8),
    _NsVpnL2tpMonTunState_Type()
)
nsVpnL2tpMonTunState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunState.setStatus("current")
_NsVpnL2tpMonTunVsys_Type = Integer32
_NsVpnL2tpMonTunVsys_Object = MibTableColumn
nsVpnL2tpMonTunVsys = _NsVpnL2tpMonTunVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 3, 1, 9),
    _NsVpnL2tpMonTunVsys_Type()
)
nsVpnL2tpMonTunVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonTunVsys.setStatus("current")
_NsVpnL2tpMonCallTable_Object = MibTable
nsVpnL2tpMonCallTable = _NsVpnL2tpMonCallTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4)
)
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallTable.setStatus("current")
_NsVpnL2tpMonCallEntry_Object = MibTableRow
nsVpnL2tpMonCallEntry = _NsVpnL2tpMonCallEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4, 1)
)
nsVpnL2tpMonCallEntry.setIndexNames(
    (0, "NETSCREEN-VPN-L2TP-MIB", "nsVpnL2tpMonCallTunId"),
    (0, "NETSCREEN-VPN-L2TP-MIB", "nsVpnL2tpMonCallId"),
)
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallEntry.setStatus("current")
_NsVpnL2tpMonCallTunId_Type = Integer32
_NsVpnL2tpMonCallTunId_Object = MibTableColumn
nsVpnL2tpMonCallTunId = _NsVpnL2tpMonCallTunId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4, 1, 1),
    _NsVpnL2tpMonCallTunId_Type()
)
nsVpnL2tpMonCallTunId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallTunId.setStatus("current")
_NsVpnL2tpMonCallId_Type = Integer32
_NsVpnL2tpMonCallId_Object = MibTableColumn
nsVpnL2tpMonCallId = _NsVpnL2tpMonCallId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4, 1, 2),
    _NsVpnL2tpMonCallId_Type()
)
nsVpnL2tpMonCallId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallId.setStatus("current")
_NsVpnL2tpMonCallPeerId_Type = Integer32
_NsVpnL2tpMonCallPeerId_Object = MibTableColumn
nsVpnL2tpMonCallPeerId = _NsVpnL2tpMonCallPeerId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4, 1, 3),
    _NsVpnL2tpMonCallPeerId_Type()
)
nsVpnL2tpMonCallPeerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallPeerId.setStatus("current")
_NsVpnL2tpMonCallIp_Type = IpAddress
_NsVpnL2tpMonCallIp_Object = MibTableColumn
nsVpnL2tpMonCallIp = _NsVpnL2tpMonCallIp_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4, 1, 4),
    _NsVpnL2tpMonCallIp_Type()
)
nsVpnL2tpMonCallIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallIp.setStatus("current")
_NsVpnL2tpMonCallUser_Type = DisplayString
_NsVpnL2tpMonCallUser_Object = MibTableColumn
nsVpnL2tpMonCallUser = _NsVpnL2tpMonCallUser_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4, 1, 5),
    _NsVpnL2tpMonCallUser_Type()
)
nsVpnL2tpMonCallUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallUser.setStatus("current")


class _NsVpnL2tpMonCallType_Type(Integer32):
    """Custom type nsVpnL2tpMonCallType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("incoming", 2),
          ("none", 1),
          ("outgoing", 3))
    )


_NsVpnL2tpMonCallType_Type.__name__ = "Integer32"
_NsVpnL2tpMonCallType_Object = MibTableColumn
nsVpnL2tpMonCallType = _NsVpnL2tpMonCallType_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4, 1, 6),
    _NsVpnL2tpMonCallType_Type()
)
nsVpnL2tpMonCallType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallType.setStatus("current")


class _NsVpnL2tpMonCallState_Type(Integer32):
    """Custom type nsVpnL2tpMonCallState based on Integer32"""
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
        *(("establish", 3),
          ("idle", 1),
          ("wait-conn", 2),
          ("wait-reply", 5),
          ("wait-tunnel", 4))
    )


_NsVpnL2tpMonCallState_Type.__name__ = "Integer32"
_NsVpnL2tpMonCallState_Object = MibTableColumn
nsVpnL2tpMonCallState = _NsVpnL2tpMonCallState_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4, 1, 7),
    _NsVpnL2tpMonCallState_Type()
)
nsVpnL2tpMonCallState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallState.setStatus("current")
_NsVpnL2tpMonCallEstTime_Type = TimeTicks
_NsVpnL2tpMonCallEstTime_Object = MibTableColumn
nsVpnL2tpMonCallEstTime = _NsVpnL2tpMonCallEstTime_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4, 1, 8),
    _NsVpnL2tpMonCallEstTime_Type()
)
nsVpnL2tpMonCallEstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallEstTime.setStatus("current")
_NsVpnL2tpMonCallVsys_Type = Integer32
_NsVpnL2tpMonCallVsys_Object = MibTableColumn
nsVpnL2tpMonCallVsys = _NsVpnL2tpMonCallVsys_Object(
    (1, 3, 6, 1, 4, 1, 3224, 4, 8, 4, 1, 9),
    _NsVpnL2tpMonCallVsys_Type()
)
nsVpnL2tpMonCallVsys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsVpnL2tpMonCallVsys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-VPN-L2TP-MIB",
    **{"netscreenVpnL2tpMibModule": netscreenVpnL2tpMibModule,
       "nsVpnL2TP": nsVpnL2TP,
       "nsVpnL2tpDefTable": nsVpnL2tpDefTable,
       "nsVpnL2tpDefEntry": nsVpnL2tpDefEntry,
       "nsVpnL2tpDefVsys": nsVpnL2tpDefVsys,
       "nsVpnL2tpDefPool": nsVpnL2tpDefPool,
       "nsVpnL2tpDefAuthDb": nsVpnL2tpDefAuthDb,
       "nsVpnL2tpDefPPPAuth": nsVpnL2tpDefPPPAuth,
       "nsVpnL2tpDefRadServer": nsVpnL2tpDefRadServer,
       "nsVpnL2tpDefPriDns": nsVpnL2tpDefPriDns,
       "nsVpnL2tpDefSecDns": nsVpnL2tpDefSecDns,
       "nsVpnL2tpDefPriWins": nsVpnL2tpDefPriWins,
       "nsVpnL2tpDefSecWins": nsVpnL2tpDefSecWins,
       "nsVpnL2tpTunnelTable": nsVpnL2tpTunnelTable,
       "nsVpnL2tpTunnelEntry": nsVpnL2tpTunnelEntry,
       "nsVpnL2tpTunIndex": nsVpnL2tpTunIndex,
       "nsVpnL2tpTunId": nsVpnL2tpTunId,
       "nsVpnL2tpTunName": nsVpnL2tpTunName,
       "nsVpnL2tpTunUsrOrGroup": nsVpnL2tpTunUsrOrGroup,
       "nsVpnL2tpTunPeerIp": nsVpnL2tpTunPeerIp,
       "nsVpnL2tpTunHost": nsVpnL2tpTunHost,
       "nsVpnL2tpTunKeepAlive": nsVpnL2tpTunKeepAlive,
       "nsVpnL2tpTunVsys": nsVpnL2tpTunVsys,
       "nsVpnL2tpMonTunnelTable": nsVpnL2tpMonTunnelTable,
       "nsVpnL2tpMonTunnelEntry": nsVpnL2tpMonTunnelEntry,
       "nsVpnL2tpMonTunId": nsVpnL2tpMonTunId,
       "nsVpnL2tpMonTunPeerId": nsVpnL2tpMonTunPeerId,
       "nsVpnL2tpMonTunName": nsVpnL2tpMonTunName,
       "nsVpnL2tpMonTunPeerIp": nsVpnL2tpMonTunPeerIp,
       "nsVpnL2tpMonTunPort": nsVpnL2tpMonTunPort,
       "nsVpnL2tpMonTunPeerHost": nsVpnL2tpMonTunPeerHost,
       "nsVpnL2tpMonTunCalls": nsVpnL2tpMonTunCalls,
       "nsVpnL2tpMonTunState": nsVpnL2tpMonTunState,
       "nsVpnL2tpMonTunVsys": nsVpnL2tpMonTunVsys,
       "nsVpnL2tpMonCallTable": nsVpnL2tpMonCallTable,
       "nsVpnL2tpMonCallEntry": nsVpnL2tpMonCallEntry,
       "nsVpnL2tpMonCallTunId": nsVpnL2tpMonCallTunId,
       "nsVpnL2tpMonCallId": nsVpnL2tpMonCallId,
       "nsVpnL2tpMonCallPeerId": nsVpnL2tpMonCallPeerId,
       "nsVpnL2tpMonCallIp": nsVpnL2tpMonCallIp,
       "nsVpnL2tpMonCallUser": nsVpnL2tpMonCallUser,
       "nsVpnL2tpMonCallType": nsVpnL2tpMonCallType,
       "nsVpnL2tpMonCallState": nsVpnL2tpMonCallState,
       "nsVpnL2tpMonCallEstTime": nsVpnL2tpMonCallEstTime,
       "nsVpnL2tpMonCallVsys": nsVpnL2tpMonCallVsys}
)
