# SNMP MIB module (NETWORK-ALCHEMY-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NETWORK-ALCHEMY-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:17 2024
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

(netalModules,
 vpn) = mibBuilder.importSymbols(
    "NETAL-SMI",
    "netalModules",
    "vpn")

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

networkAlchemyVPNMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2972, 5, 5)
)
networkAlchemyVPNMIB.setRevisions(
        ("2000-10-25 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VpnL2TPTunnels_Type = Integer32
_VpnL2TPTunnels_Object = MibScalar
vpnL2TPTunnels = _VpnL2TPTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 1),
    _VpnL2TPTunnels_Type()
)
vpnL2TPTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnL2TPTunnels.setStatus("current")
_VpnActiveL2TPTunnels_Type = Integer32
_VpnActiveL2TPTunnels_Object = MibScalar
vpnActiveL2TPTunnels = _VpnActiveL2TPTunnels_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 2),
    _VpnActiveL2TPTunnels_Type()
)
vpnActiveL2TPTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnActiveL2TPTunnels.setStatus("current")
_VpnL2TPSessions_Type = Integer32
_VpnL2TPSessions_Object = MibScalar
vpnL2TPSessions = _VpnL2TPSessions_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 3),
    _VpnL2TPSessions_Type()
)
vpnL2TPSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnL2TPSessions.setStatus("current")
_VpnActiveL2TPSessions_Type = Integer32
_VpnActiveL2TPSessions_Object = MibScalar
vpnActiveL2TPSessions = _VpnActiveL2TPSessions_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 4),
    _VpnActiveL2TPSessions_Type()
)
vpnActiveL2TPSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnActiveL2TPSessions.setStatus("current")
_VpnPPTPTS_Type = Integer32
_VpnPPTPTS_Object = MibScalar
vpnPPTPTS = _VpnPPTPTS_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 5),
    _VpnPPTPTS_Type()
)
vpnPPTPTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnPPTPTS.setStatus("current")
_VpnActivePPTPTS_Type = Integer32
_VpnActivePPTPTS_Object = MibScalar
vpnActivePPTPTS = _VpnActivePPTPTS_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 6),
    _VpnActivePPTPTS_Type()
)
vpnActivePPTPTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnActivePPTPTS.setStatus("current")
_VpnTunnelTable_Object = MibTable
vpnTunnelTable = _VpnTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 7)
)
if mibBuilder.loadTexts:
    vpnTunnelTable.setStatus("current")
_VpnTunnelEntry_Object = MibTableRow
vpnTunnelEntry = _VpnTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 7, 1)
)
vpnTunnelEntry.setIndexNames(
    (0, "NETWORK-ALCHEMY-VPN-MIB", "vpnTunnelLocalID"),
    (0, "NETWORK-ALCHEMY-VPN-MIB", "vpnTunnelIPAddress"),
)
if mibBuilder.loadTexts:
    vpnTunnelEntry.setStatus("current")
_VpnTunnelLocalID_Type = Integer32
_VpnTunnelLocalID_Object = MibTableColumn
vpnTunnelLocalID = _VpnTunnelLocalID_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 7, 1, 1),
    _VpnTunnelLocalID_Type()
)
vpnTunnelLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelLocalID.setStatus("current")
_VpnTunnelIPAddress_Type = IpAddress
_VpnTunnelIPAddress_Object = MibTableColumn
vpnTunnelIPAddress = _VpnTunnelIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 7, 1, 2),
    _VpnTunnelIPAddress_Type()
)
vpnTunnelIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelIPAddress.setStatus("current")
_VpnTunnelRemoteID_Type = Integer32
_VpnTunnelRemoteID_Object = MibTableColumn
vpnTunnelRemoteID = _VpnTunnelRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 7, 1, 3),
    _VpnTunnelRemoteID_Type()
)
vpnTunnelRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelRemoteID.setStatus("current")


class _VpnTunnelType_Type(Integer32):
    """Custom type vpnTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("any", 0),
          ("l2tp", 1),
          ("pptp", 2))
    )


_VpnTunnelType_Type.__name__ = "Integer32"
_VpnTunnelType_Object = MibTableColumn
vpnTunnelType = _VpnTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 7, 1, 4),
    _VpnTunnelType_Type()
)
vpnTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelType.setStatus("current")


class _VpnTunnelActive_Type(Integer32):
    """Custom type vpnTunnelActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_VpnTunnelActive_Type.__name__ = "Integer32"
_VpnTunnelActive_Object = MibTableColumn
vpnTunnelActive = _VpnTunnelActive_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 7, 1, 5),
    _VpnTunnelActive_Type()
)
vpnTunnelActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelActive.setStatus("current")


class _VpnTunnelState_Type(Integer32):
    """Custom type vpnTunnelState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_VpnTunnelState_Type.__name__ = "Integer32"
_VpnTunnelState_Object = MibTableColumn
vpnTunnelState = _VpnTunnelState_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 7, 1, 6),
    _VpnTunnelState_Type()
)
vpnTunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnTunnelState.setStatus("current")
_VpnSessionTable_Object = MibTable
vpnSessionTable = _VpnSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8)
)
if mibBuilder.loadTexts:
    vpnSessionTable.setStatus("current")
_VpnSessionEntry_Object = MibTableRow
vpnSessionEntry = _VpnSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1)
)
vpnSessionEntry.setIndexNames(
    (0, "NETWORK-ALCHEMY-VPN-MIB", "vpnTunnelLocalID"),
    (0, "NETWORK-ALCHEMY-VPN-MIB", "vpnTunnelIPAddress"),
    (0, "NETWORK-ALCHEMY-VPN-MIB", "vpnSessionLocalID"),
    (0, "NETWORK-ALCHEMY-VPN-MIB", "vpnSessionIPAddress"),
)
if mibBuilder.loadTexts:
    vpnSessionEntry.setStatus("current")
_VpnSessionLocalID_Type = Integer32
_VpnSessionLocalID_Object = MibTableColumn
vpnSessionLocalID = _VpnSessionLocalID_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 1),
    _VpnSessionLocalID_Type()
)
vpnSessionLocalID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionLocalID.setStatus("current")
_VpnSessionIPAddress_Type = IpAddress
_VpnSessionIPAddress_Object = MibTableColumn
vpnSessionIPAddress = _VpnSessionIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 2),
    _VpnSessionIPAddress_Type()
)
vpnSessionIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionIPAddress.setStatus("current")
_VpnSessionRemoteID_Type = Integer32
_VpnSessionRemoteID_Object = MibTableColumn
vpnSessionRemoteID = _VpnSessionRemoteID_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 3),
    _VpnSessionRemoteID_Type()
)
vpnSessionRemoteID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionRemoteID.setStatus("current")
_VpnSessionPacketsIn_Type = Integer32
_VpnSessionPacketsIn_Object = MibTableColumn
vpnSessionPacketsIn = _VpnSessionPacketsIn_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 4),
    _VpnSessionPacketsIn_Type()
)
vpnSessionPacketsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionPacketsIn.setStatus("current")
_VpnSessionPacketsOut_Type = Integer32
_VpnSessionPacketsOut_Object = MibTableColumn
vpnSessionPacketsOut = _VpnSessionPacketsOut_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 5),
    _VpnSessionPacketsOut_Type()
)
vpnSessionPacketsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionPacketsOut.setStatus("current")


class _VpnSessionActive_Type(Integer32):
    """Custom type vpnSessionActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 0))
    )


_VpnSessionActive_Type.__name__ = "Integer32"
_VpnSessionActive_Object = MibTableColumn
vpnSessionActive = _VpnSessionActive_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 6),
    _VpnSessionActive_Type()
)
vpnSessionActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionActive.setStatus("current")


class _VpnSessionState_Type(Integer32):
    """Custom type vpnSessionState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 2),
          ("inactive", 0),
          ("suspended", 1))
    )


_VpnSessionState_Type.__name__ = "Integer32"
_VpnSessionState_Object = MibTableColumn
vpnSessionState = _VpnSessionState_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 7),
    _VpnSessionState_Type()
)
vpnSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionState.setStatus("current")


class _VpnSessionAuthType_Type(Integer32):
    """Custom type vpnSessionAuthType based on Integer32"""
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
        *(("chap", 1),
          ("mschap", 2),
          ("none", 0),
          ("pap", 3))
    )


_VpnSessionAuthType_Type.__name__ = "Integer32"
_VpnSessionAuthType_Object = MibTableColumn
vpnSessionAuthType = _VpnSessionAuthType_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 8),
    _VpnSessionAuthType_Type()
)
vpnSessionAuthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionAuthType.setStatus("current")
_VpnSessionSendFlags_Type = Integer32
_VpnSessionSendFlags_Object = MibTableColumn
vpnSessionSendFlags = _VpnSessionSendFlags_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 9),
    _VpnSessionSendFlags_Type()
)
vpnSessionSendFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionSendFlags.setStatus("current")
_VpnSessionRecvFlags_Type = Integer32
_VpnSessionRecvFlags_Object = MibTableColumn
vpnSessionRecvFlags = _VpnSessionRecvFlags_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 10),
    _VpnSessionRecvFlags_Type()
)
vpnSessionRecvFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionRecvFlags.setStatus("current")
_VpnSessionUsername_Type = DisplayString
_VpnSessionUsername_Object = MibTableColumn
vpnSessionUsername = _VpnSessionUsername_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 11),
    _VpnSessionUsername_Type()
)
vpnSessionUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionUsername.setStatus("current")
_VpnSessionLifetimeSeconds_Type = Integer32
_VpnSessionLifetimeSeconds_Object = MibTableColumn
vpnSessionLifetimeSeconds = _VpnSessionLifetimeSeconds_Object(
    (1, 3, 6, 1, 4, 1, 2972, 2, 4, 8, 1, 12),
    _VpnSessionLifetimeSeconds_Type()
)
vpnSessionLifetimeSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpnSessionLifetimeSeconds.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETWORK-ALCHEMY-VPN-MIB",
    **{"vpnL2TPTunnels": vpnL2TPTunnels,
       "vpnActiveL2TPTunnels": vpnActiveL2TPTunnels,
       "vpnL2TPSessions": vpnL2TPSessions,
       "vpnActiveL2TPSessions": vpnActiveL2TPSessions,
       "vpnPPTPTS": vpnPPTPTS,
       "vpnActivePPTPTS": vpnActivePPTPTS,
       "vpnTunnelTable": vpnTunnelTable,
       "vpnTunnelEntry": vpnTunnelEntry,
       "vpnTunnelLocalID": vpnTunnelLocalID,
       "vpnTunnelIPAddress": vpnTunnelIPAddress,
       "vpnTunnelRemoteID": vpnTunnelRemoteID,
       "vpnTunnelType": vpnTunnelType,
       "vpnTunnelActive": vpnTunnelActive,
       "vpnTunnelState": vpnTunnelState,
       "vpnSessionTable": vpnSessionTable,
       "vpnSessionEntry": vpnSessionEntry,
       "vpnSessionLocalID": vpnSessionLocalID,
       "vpnSessionIPAddress": vpnSessionIPAddress,
       "vpnSessionRemoteID": vpnSessionRemoteID,
       "vpnSessionPacketsIn": vpnSessionPacketsIn,
       "vpnSessionPacketsOut": vpnSessionPacketsOut,
       "vpnSessionActive": vpnSessionActive,
       "vpnSessionState": vpnSessionState,
       "vpnSessionAuthType": vpnSessionAuthType,
       "vpnSessionSendFlags": vpnSessionSendFlags,
       "vpnSessionRecvFlags": vpnSessionRecvFlags,
       "vpnSessionUsername": vpnSessionUsername,
       "vpnSessionLifetimeSeconds": vpnSessionLifetimeSeconds,
       "networkAlchemyVPNMIB": networkAlchemyVPNMIB}
)
