# SNMP MIB module (WATCHGUARD-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WATCHGUARD-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:13:31 2024
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

(DateAndTime,
 DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "TextualConvention")

(watchguard,) = mibBuilder.importSymbols(
    "WATCHGUARD-SMI",
    "watchguard")


# MODULE-IDENTITY

wgInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6)
)
wgInfoModule.setRevisions(
        ("2007-01-25 12:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WgClientMIB_ObjectIdentity = ObjectIdentity
wgClientMIB = _WgClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2)
)
if mibBuilder.loadTexts:
    wgClientMIB.setStatus("current")
_WgClientDHCPServer_ObjectIdentity = ObjectIdentity
wgClientDHCPServer = _WgClientDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1)
)
if mibBuilder.loadTexts:
    wgClientDHCPServer.setStatus("current")


class _WgClientDHCPServerEnable_Type(Integer32):
    """Custom type wgClientDHCPServerEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1),
          ("relay", 2))
    )


_WgClientDHCPServerEnable_Type.__name__ = "Integer32"
_WgClientDHCPServerEnable_Object = MibScalar
wgClientDHCPServerEnable = _WgClientDHCPServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 1),
    _WgClientDHCPServerEnable_Type()
)
wgClientDHCPServerEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerEnable.setStatus("current")
_WgClientDHCPServerStartIpAddress_Type = IpAddress
_WgClientDHCPServerStartIpAddress_Object = MibScalar
wgClientDHCPServerStartIpAddress = _WgClientDHCPServerStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 2),
    _WgClientDHCPServerStartIpAddress_Type()
)
wgClientDHCPServerStartIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerStartIpAddress.setStatus("current")
_WgClientDHCPServerEndIpAddress_Type = IpAddress
_WgClientDHCPServerEndIpAddress_Object = MibScalar
wgClientDHCPServerEndIpAddress = _WgClientDHCPServerEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 3),
    _WgClientDHCPServerEndIpAddress_Type()
)
wgClientDHCPServerEndIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerEndIpAddress.setStatus("current")
_WgClientDHCPServerLeaseTime_Type = TimeTicks
_WgClientDHCPServerLeaseTime_Object = MibScalar
wgClientDHCPServerLeaseTime = _WgClientDHCPServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 4),
    _WgClientDHCPServerLeaseTime_Type()
)
wgClientDHCPServerLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerLeaseTime.setStatus("current")
_WgClientDHCPServerNum_Type = Unsigned32
_WgClientDHCPServerNum_Object = MibScalar
wgClientDHCPServerNum = _WgClientDHCPServerNum_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 5),
    _WgClientDHCPServerNum_Type()
)
wgClientDHCPServerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerNum.setStatus("current")
_WgClientDHCPServerConnTable_Object = MibTable
wgClientDHCPServerConnTable = _WgClientDHCPServerConnTable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6)
)
if mibBuilder.loadTexts:
    wgClientDHCPServerConnTable.setStatus("current")
_WgClientDHCPServerConnEntry_Object = MibTableRow
wgClientDHCPServerConnEntry = _WgClientDHCPServerConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1)
)
wgClientDHCPServerConnEntry.setIndexNames(
    (0, "WATCHGUARD-CLIENT-MIB", "wgClientDHCPServerConnIPAddr"),
)
if mibBuilder.loadTexts:
    wgClientDHCPServerConnEntry.setStatus("current")
_WgClientDHCPServerConnClientHostName_Type = OctetString
_WgClientDHCPServerConnClientHostName_Object = MibTableColumn
wgClientDHCPServerConnClientHostName = _WgClientDHCPServerConnClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1, 1),
    _WgClientDHCPServerConnClientHostName_Type()
)
wgClientDHCPServerConnClientHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerConnClientHostName.setStatus("current")
_WgClientDHCPServerConnIPAddr_Type = IpAddress
_WgClientDHCPServerConnIPAddr_Object = MibTableColumn
wgClientDHCPServerConnIPAddr = _WgClientDHCPServerConnIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1, 2),
    _WgClientDHCPServerConnIPAddr_Type()
)
wgClientDHCPServerConnIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerConnIPAddr.setStatus("current")


class _WgClientDHCPServerConnMACAddr_Type(OctetString):
    """Custom type wgClientDHCPServerConnMACAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WgClientDHCPServerConnMACAddr_Type.__name__ = "OctetString"
_WgClientDHCPServerConnMACAddr_Object = MibTableColumn
wgClientDHCPServerConnMACAddr = _WgClientDHCPServerConnMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1, 3),
    _WgClientDHCPServerConnMACAddr_Type()
)
wgClientDHCPServerConnMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerConnMACAddr.setStatus("current")
_WgClientDHCPServerConnLeaseTimeStart_Type = DateAndTime
_WgClientDHCPServerConnLeaseTimeStart_Object = MibTableColumn
wgClientDHCPServerConnLeaseTimeStart = _WgClientDHCPServerConnLeaseTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1, 4),
    _WgClientDHCPServerConnLeaseTimeStart_Type()
)
wgClientDHCPServerConnLeaseTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerConnLeaseTimeStart.setStatus("current")
_WgClientDHCPServerConnLeaseTimeEnd_Type = DateAndTime
_WgClientDHCPServerConnLeaseTimeEnd_Object = MibTableColumn
wgClientDHCPServerConnLeaseTimeEnd = _WgClientDHCPServerConnLeaseTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 6, 1, 5),
    _WgClientDHCPServerConnLeaseTimeEnd_Type()
)
wgClientDHCPServerConnLeaseTimeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerConnLeaseTimeEnd.setStatus("current")
_WgClientDHCPServerRelayServer_Type = IpAddress
_WgClientDHCPServerRelayServer_Object = MibScalar
wgClientDHCPServerRelayServer = _WgClientDHCPServerRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 1, 7),
    _WgClientDHCPServerRelayServer_Type()
)
wgClientDHCPServerRelayServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPServerRelayServer.setStatus("current")
_WgClientDHCPClient_ObjectIdentity = ObjectIdentity
wgClientDHCPClient = _WgClientDHCPClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 2)
)
if mibBuilder.loadTexts:
    wgClientDHCPClient.setStatus("current")


class _WgClientDHCPClientEnable_Type(Integer32):
    """Custom type wgClientDHCPClientEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WgClientDHCPClientEnable_Type.__name__ = "Integer32"
_WgClientDHCPClientEnable_Object = MibScalar
wgClientDHCPClientEnable = _WgClientDHCPClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 2, 1),
    _WgClientDHCPClientEnable_Type()
)
wgClientDHCPClientEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPClientEnable.setStatus("current")
_WgClientDHCPClientDomainName_Type = OctetString
_WgClientDHCPClientDomainName_Object = MibScalar
wgClientDHCPClientDomainName = _WgClientDHCPClientDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 2, 2),
    _WgClientDHCPClientDomainName_Type()
)
wgClientDHCPClientDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPClientDomainName.setStatus("current")
_WgClientDHCPClientDefaultGateway_Type = IpAddress
_WgClientDHCPClientDefaultGateway_Object = MibScalar
wgClientDHCPClientDefaultGateway = _WgClientDHCPClientDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 2, 3),
    _WgClientDHCPClientDefaultGateway_Type()
)
wgClientDHCPClientDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPClientDefaultGateway.setStatus("current")
_WgClientDHCPClientDNSOne_Type = IpAddress
_WgClientDHCPClientDNSOne_Object = MibScalar
wgClientDHCPClientDNSOne = _WgClientDHCPClientDNSOne_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 2, 4),
    _WgClientDHCPClientDNSOne_Type()
)
wgClientDHCPClientDNSOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPClientDNSOne.setStatus("current")
_WgClientDHCPClientDNSTwo_Type = IpAddress
_WgClientDHCPClientDNSTwo_Object = MibScalar
wgClientDHCPClientDNSTwo = _WgClientDHCPClientDNSTwo_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 2, 5),
    _WgClientDHCPClientDNSTwo_Type()
)
wgClientDHCPClientDNSTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientDHCPClientDNSTwo.setStatus("current")
_WgClientPPPoEClient_ObjectIdentity = ObjectIdentity
wgClientPPPoEClient = _WgClientPPPoEClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 3)
)
if mibBuilder.loadTexts:
    wgClientPPPoEClient.setStatus("current")


class _WgClientPPPoEClientEnable_Type(Integer32):
    """Custom type wgClientPPPoEClientEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_WgClientPPPoEClientEnable_Type.__name__ = "Integer32"
_WgClientPPPoEClientEnable_Object = MibScalar
wgClientPPPoEClientEnable = _WgClientPPPoEClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 1),
    _WgClientPPPoEClientEnable_Type()
)
wgClientPPPoEClientEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientPPPoEClientEnable.setStatus("current")


class _WgClientPPPoEClientADSLStatus_Type(Integer32):
    """Custom type wgClientPPPoEClientADSLStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("authenticate", 3),
          ("disconnect", 0),
          ("establish", 2),
          ("initialize", 1),
          ("network", 4),
          ("running", 5))
    )


_WgClientPPPoEClientADSLStatus_Type.__name__ = "Integer32"
_WgClientPPPoEClientADSLStatus_Object = MibScalar
wgClientPPPoEClientADSLStatus = _WgClientPPPoEClientADSLStatus_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 2),
    _WgClientPPPoEClientADSLStatus_Type()
)
wgClientPPPoEClientADSLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientPPPoEClientADSLStatus.setStatus("current")
_WgClientPPPoEClientLocalIPAddr_Type = IpAddress
_WgClientPPPoEClientLocalIPAddr_Object = MibScalar
wgClientPPPoEClientLocalIPAddr = _WgClientPPPoEClientLocalIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 3),
    _WgClientPPPoEClientLocalIPAddr_Type()
)
wgClientPPPoEClientLocalIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientPPPoEClientLocalIPAddr.setStatus("current")
_WgClientPPPoEClientRemoteIPAddr_Type = IpAddress
_WgClientPPPoEClientRemoteIPAddr_Object = MibScalar
wgClientPPPoEClientRemoteIPAddr = _WgClientPPPoEClientRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 4),
    _WgClientPPPoEClientRemoteIPAddr_Type()
)
wgClientPPPoEClientRemoteIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientPPPoEClientRemoteIPAddr.setStatus("current")
_WgClientPPPoEClientNetMask_Type = IpAddress
_WgClientPPPoEClientNetMask_Object = MibScalar
wgClientPPPoEClientNetMask = _WgClientPPPoEClientNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 5),
    _WgClientPPPoEClientNetMask_Type()
)
wgClientPPPoEClientNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientPPPoEClientNetMask.setStatus("current")
_WgClientPPPoEClientDNSOne_Type = IpAddress
_WgClientPPPoEClientDNSOne_Object = MibScalar
wgClientPPPoEClientDNSOne = _WgClientPPPoEClientDNSOne_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 6),
    _WgClientPPPoEClientDNSOne_Type()
)
wgClientPPPoEClientDNSOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientPPPoEClientDNSOne.setStatus("current")
_WgClientPPPoEClientDNSTwo_Type = IpAddress
_WgClientPPPoEClientDNSTwo_Object = MibScalar
wgClientPPPoEClientDNSTwo = _WgClientPPPoEClientDNSTwo_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 7),
    _WgClientPPPoEClientDNSTwo_Type()
)
wgClientPPPoEClientDNSTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientPPPoEClientDNSTwo.setStatus("current")


class _WgClientPPPoEADSLPeerMACAddr_Type(OctetString):
    """Custom type wgClientPPPoEADSLPeerMACAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_WgClientPPPoEADSLPeerMACAddr_Type.__name__ = "OctetString"
_WgClientPPPoEADSLPeerMACAddr_Object = MibScalar
wgClientPPPoEADSLPeerMACAddr = _WgClientPPPoEADSLPeerMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 8),
    _WgClientPPPoEADSLPeerMACAddr_Type()
)
wgClientPPPoEADSLPeerMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientPPPoEADSLPeerMACAddr.setStatus("current")
_WgClientPPPoEClientConnTime_Type = TimeTicks
_WgClientPPPoEClientConnTime_Object = MibScalar
wgClientPPPoEClientConnTime = _WgClientPPPoEClientConnTime_Object(
    (1, 3, 6, 1, 4, 1, 3097, 6, 2, 3, 9),
    _WgClientPPPoEClientConnTime_Type()
)
wgClientPPPoEClientConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wgClientPPPoEClientConnTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WATCHGUARD-CLIENT-MIB",
    **{"wgInfoModule": wgInfoModule,
       "wgClientMIB": wgClientMIB,
       "wgClientDHCPServer": wgClientDHCPServer,
       "wgClientDHCPServerEnable": wgClientDHCPServerEnable,
       "wgClientDHCPServerStartIpAddress": wgClientDHCPServerStartIpAddress,
       "wgClientDHCPServerEndIpAddress": wgClientDHCPServerEndIpAddress,
       "wgClientDHCPServerLeaseTime": wgClientDHCPServerLeaseTime,
       "wgClientDHCPServerNum": wgClientDHCPServerNum,
       "wgClientDHCPServerConnTable": wgClientDHCPServerConnTable,
       "wgClientDHCPServerConnEntry": wgClientDHCPServerConnEntry,
       "wgClientDHCPServerConnClientHostName": wgClientDHCPServerConnClientHostName,
       "wgClientDHCPServerConnIPAddr": wgClientDHCPServerConnIPAddr,
       "wgClientDHCPServerConnMACAddr": wgClientDHCPServerConnMACAddr,
       "wgClientDHCPServerConnLeaseTimeStart": wgClientDHCPServerConnLeaseTimeStart,
       "wgClientDHCPServerConnLeaseTimeEnd": wgClientDHCPServerConnLeaseTimeEnd,
       "wgClientDHCPServerRelayServer": wgClientDHCPServerRelayServer,
       "wgClientDHCPClient": wgClientDHCPClient,
       "wgClientDHCPClientEnable": wgClientDHCPClientEnable,
       "wgClientDHCPClientDomainName": wgClientDHCPClientDomainName,
       "wgClientDHCPClientDefaultGateway": wgClientDHCPClientDefaultGateway,
       "wgClientDHCPClientDNSOne": wgClientDHCPClientDNSOne,
       "wgClientDHCPClientDNSTwo": wgClientDHCPClientDNSTwo,
       "wgClientPPPoEClient": wgClientPPPoEClient,
       "wgClientPPPoEClientEnable": wgClientPPPoEClientEnable,
       "wgClientPPPoEClientADSLStatus": wgClientPPPoEClientADSLStatus,
       "wgClientPPPoEClientLocalIPAddr": wgClientPPPoEClientLocalIPAddr,
       "wgClientPPPoEClientRemoteIPAddr": wgClientPPPoEClientRemoteIPAddr,
       "wgClientPPPoEClientNetMask": wgClientPPPoEClientNetMask,
       "wgClientPPPoEClientDNSOne": wgClientPPPoEClientDNSOne,
       "wgClientPPPoEClientDNSTwo": wgClientPPPoEClientDNSTwo,
       "wgClientPPPoEADSLPeerMACAddr": wgClientPPPoEADSLPeerMACAddr,
       "wgClientPPPoEClientConnTime": wgClientPPPoEClientConnTime}
)
