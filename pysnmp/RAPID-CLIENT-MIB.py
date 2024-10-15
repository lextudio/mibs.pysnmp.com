# SNMP MIB module (RAPID-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RAPID-CLIENT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:44:36 2024
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

(rapidstream,) = mibBuilder.importSymbols(
    "RAPID-MIB",
    "rapidstream")

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


# MODULE-IDENTITY

rsInfoModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6)
)
rsInfoModule.setRevisions(
        ("2001-04-20 12:00",
         "2002-11-01 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RsClientMIB_ObjectIdentity = ObjectIdentity
rsClientMIB = _RsClientMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2)
)
if mibBuilder.loadTexts:
    rsClientMIB.setStatus("current")
_RsClientDHCPServer_ObjectIdentity = ObjectIdentity
rsClientDHCPServer = _RsClientDHCPServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1)
)
if mibBuilder.loadTexts:
    rsClientDHCPServer.setStatus("current")


class _RsClientDHCPServerEnable_Type(Integer32):
    """Custom type rsClientDHCPServerEnable based on Integer32"""
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


_RsClientDHCPServerEnable_Type.__name__ = "Integer32"
_RsClientDHCPServerEnable_Object = MibScalar
rsClientDHCPServerEnable = _RsClientDHCPServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 1),
    _RsClientDHCPServerEnable_Type()
)
rsClientDHCPServerEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerEnable.setStatus("current")
_RsClientDHCPServerStartIpAddress_Type = IpAddress
_RsClientDHCPServerStartIpAddress_Object = MibScalar
rsClientDHCPServerStartIpAddress = _RsClientDHCPServerStartIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 2),
    _RsClientDHCPServerStartIpAddress_Type()
)
rsClientDHCPServerStartIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerStartIpAddress.setStatus("current")
_RsClientDHCPServerEndIpAddress_Type = IpAddress
_RsClientDHCPServerEndIpAddress_Object = MibScalar
rsClientDHCPServerEndIpAddress = _RsClientDHCPServerEndIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 3),
    _RsClientDHCPServerEndIpAddress_Type()
)
rsClientDHCPServerEndIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerEndIpAddress.setStatus("current")
_RsClientDHCPServerLeaseTime_Type = TimeTicks
_RsClientDHCPServerLeaseTime_Object = MibScalar
rsClientDHCPServerLeaseTime = _RsClientDHCPServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 4),
    _RsClientDHCPServerLeaseTime_Type()
)
rsClientDHCPServerLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerLeaseTime.setStatus("current")
_RsClientDHCPServerNum_Type = Unsigned32
_RsClientDHCPServerNum_Object = MibScalar
rsClientDHCPServerNum = _RsClientDHCPServerNum_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 5),
    _RsClientDHCPServerNum_Type()
)
rsClientDHCPServerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerNum.setStatus("current")
_RsClientDHCPServerConnTable_Object = MibTable
rsClientDHCPServerConnTable = _RsClientDHCPServerConnTable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6)
)
if mibBuilder.loadTexts:
    rsClientDHCPServerConnTable.setStatus("current")
_RsClientDHCPServerConnEntry_Object = MibTableRow
rsClientDHCPServerConnEntry = _RsClientDHCPServerConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1)
)
rsClientDHCPServerConnEntry.setIndexNames(
    (0, "RAPID-CLIENT-MIB", "rsClientDHCPServerConnIPAddr"),
)
if mibBuilder.loadTexts:
    rsClientDHCPServerConnEntry.setStatus("current")
_RsClientDHCPServerConnClientHostName_Type = OctetString
_RsClientDHCPServerConnClientHostName_Object = MibTableColumn
rsClientDHCPServerConnClientHostName = _RsClientDHCPServerConnClientHostName_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1, 1),
    _RsClientDHCPServerConnClientHostName_Type()
)
rsClientDHCPServerConnClientHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerConnClientHostName.setStatus("current")
_RsClientDHCPServerConnIPAddr_Type = IpAddress
_RsClientDHCPServerConnIPAddr_Object = MibTableColumn
rsClientDHCPServerConnIPAddr = _RsClientDHCPServerConnIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1, 2),
    _RsClientDHCPServerConnIPAddr_Type()
)
rsClientDHCPServerConnIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerConnIPAddr.setStatus("current")


class _RsClientDHCPServerConnMACAddr_Type(OctetString):
    """Custom type rsClientDHCPServerConnMACAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RsClientDHCPServerConnMACAddr_Type.__name__ = "OctetString"
_RsClientDHCPServerConnMACAddr_Object = MibTableColumn
rsClientDHCPServerConnMACAddr = _RsClientDHCPServerConnMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1, 3),
    _RsClientDHCPServerConnMACAddr_Type()
)
rsClientDHCPServerConnMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerConnMACAddr.setStatus("current")
_RsClientDHCPServerConnLeaseTimeStart_Type = DateAndTime
_RsClientDHCPServerConnLeaseTimeStart_Object = MibTableColumn
rsClientDHCPServerConnLeaseTimeStart = _RsClientDHCPServerConnLeaseTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1, 4),
    _RsClientDHCPServerConnLeaseTimeStart_Type()
)
rsClientDHCPServerConnLeaseTimeStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerConnLeaseTimeStart.setStatus("current")
_RsClientDHCPServerConnLeaseTimeEnd_Type = DateAndTime
_RsClientDHCPServerConnLeaseTimeEnd_Object = MibTableColumn
rsClientDHCPServerConnLeaseTimeEnd = _RsClientDHCPServerConnLeaseTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 6, 1, 5),
    _RsClientDHCPServerConnLeaseTimeEnd_Type()
)
rsClientDHCPServerConnLeaseTimeEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerConnLeaseTimeEnd.setStatus("current")
_RsClientDHCPServerRelayServer_Type = IpAddress
_RsClientDHCPServerRelayServer_Object = MibScalar
rsClientDHCPServerRelayServer = _RsClientDHCPServerRelayServer_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 1, 7),
    _RsClientDHCPServerRelayServer_Type()
)
rsClientDHCPServerRelayServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPServerRelayServer.setStatus("current")
_RsClientDHCPClient_ObjectIdentity = ObjectIdentity
rsClientDHCPClient = _RsClientDHCPClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 2)
)
if mibBuilder.loadTexts:
    rsClientDHCPClient.setStatus("current")


class _RsClientDHCPClientEnable_Type(Integer32):
    """Custom type rsClientDHCPClientEnable based on Integer32"""
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


_RsClientDHCPClientEnable_Type.__name__ = "Integer32"
_RsClientDHCPClientEnable_Object = MibScalar
rsClientDHCPClientEnable = _RsClientDHCPClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 2, 1),
    _RsClientDHCPClientEnable_Type()
)
rsClientDHCPClientEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPClientEnable.setStatus("current")
_RsClientDHCPClientDomainName_Type = OctetString
_RsClientDHCPClientDomainName_Object = MibScalar
rsClientDHCPClientDomainName = _RsClientDHCPClientDomainName_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 2, 2),
    _RsClientDHCPClientDomainName_Type()
)
rsClientDHCPClientDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPClientDomainName.setStatus("current")
_RsClientDHCPClientDefaultGateway_Type = IpAddress
_RsClientDHCPClientDefaultGateway_Object = MibScalar
rsClientDHCPClientDefaultGateway = _RsClientDHCPClientDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 2, 3),
    _RsClientDHCPClientDefaultGateway_Type()
)
rsClientDHCPClientDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPClientDefaultGateway.setStatus("current")
_RsClientDHCPClientDNSOne_Type = IpAddress
_RsClientDHCPClientDNSOne_Object = MibScalar
rsClientDHCPClientDNSOne = _RsClientDHCPClientDNSOne_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 2, 4),
    _RsClientDHCPClientDNSOne_Type()
)
rsClientDHCPClientDNSOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPClientDNSOne.setStatus("current")
_RsClientDHCPClientDNSTwo_Type = IpAddress
_RsClientDHCPClientDNSTwo_Object = MibScalar
rsClientDHCPClientDNSTwo = _RsClientDHCPClientDNSTwo_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 2, 5),
    _RsClientDHCPClientDNSTwo_Type()
)
rsClientDHCPClientDNSTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientDHCPClientDNSTwo.setStatus("current")
_RsClientPPPoEClient_ObjectIdentity = ObjectIdentity
rsClientPPPoEClient = _RsClientPPPoEClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 3)
)
if mibBuilder.loadTexts:
    rsClientPPPoEClient.setStatus("current")


class _RsClientPPPoEClientEnable_Type(Integer32):
    """Custom type rsClientPPPoEClientEnable based on Integer32"""
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


_RsClientPPPoEClientEnable_Type.__name__ = "Integer32"
_RsClientPPPoEClientEnable_Object = MibScalar
rsClientPPPoEClientEnable = _RsClientPPPoEClientEnable_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 1),
    _RsClientPPPoEClientEnable_Type()
)
rsClientPPPoEClientEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientPPPoEClientEnable.setStatus("current")


class _RsClientPPPoEClientADSLStatus_Type(Integer32):
    """Custom type rsClientPPPoEClientADSLStatus based on Integer32"""
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


_RsClientPPPoEClientADSLStatus_Type.__name__ = "Integer32"
_RsClientPPPoEClientADSLStatus_Object = MibScalar
rsClientPPPoEClientADSLStatus = _RsClientPPPoEClientADSLStatus_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 2),
    _RsClientPPPoEClientADSLStatus_Type()
)
rsClientPPPoEClientADSLStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientPPPoEClientADSLStatus.setStatus("current")
_RsClientPPPoEClientLocalIPAddr_Type = IpAddress
_RsClientPPPoEClientLocalIPAddr_Object = MibScalar
rsClientPPPoEClientLocalIPAddr = _RsClientPPPoEClientLocalIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 3),
    _RsClientPPPoEClientLocalIPAddr_Type()
)
rsClientPPPoEClientLocalIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientPPPoEClientLocalIPAddr.setStatus("current")
_RsClientPPPoEClientRemoteIPAddr_Type = IpAddress
_RsClientPPPoEClientRemoteIPAddr_Object = MibScalar
rsClientPPPoEClientRemoteIPAddr = _RsClientPPPoEClientRemoteIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 4),
    _RsClientPPPoEClientRemoteIPAddr_Type()
)
rsClientPPPoEClientRemoteIPAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientPPPoEClientRemoteIPAddr.setStatus("current")
_RsClientPPPoEClientNetMask_Type = IpAddress
_RsClientPPPoEClientNetMask_Object = MibScalar
rsClientPPPoEClientNetMask = _RsClientPPPoEClientNetMask_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 5),
    _RsClientPPPoEClientNetMask_Type()
)
rsClientPPPoEClientNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientPPPoEClientNetMask.setStatus("current")
_RsClientPPPoEClientDNSOne_Type = IpAddress
_RsClientPPPoEClientDNSOne_Object = MibScalar
rsClientPPPoEClientDNSOne = _RsClientPPPoEClientDNSOne_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 6),
    _RsClientPPPoEClientDNSOne_Type()
)
rsClientPPPoEClientDNSOne.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientPPPoEClientDNSOne.setStatus("current")
_RsClientPPPoEClientDNSTwo_Type = IpAddress
_RsClientPPPoEClientDNSTwo_Object = MibScalar
rsClientPPPoEClientDNSTwo = _RsClientPPPoEClientDNSTwo_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 7),
    _RsClientPPPoEClientDNSTwo_Type()
)
rsClientPPPoEClientDNSTwo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientPPPoEClientDNSTwo.setStatus("current")


class _RsClientPPPoEADSLPeerMACAddr_Type(OctetString):
    """Custom type rsClientPPPoEADSLPeerMACAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RsClientPPPoEADSLPeerMACAddr_Type.__name__ = "OctetString"
_RsClientPPPoEADSLPeerMACAddr_Object = MibScalar
rsClientPPPoEADSLPeerMACAddr = _RsClientPPPoEADSLPeerMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 8),
    _RsClientPPPoEADSLPeerMACAddr_Type()
)
rsClientPPPoEADSLPeerMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientPPPoEADSLPeerMACAddr.setStatus("current")
_RsClientPPPoEClientConnTime_Type = TimeTicks
_RsClientPPPoEClientConnTime_Object = MibScalar
rsClientPPPoEClientConnTime = _RsClientPPPoEClientConnTime_Object(
    (1, 3, 6, 1, 4, 1, 4355, 6, 2, 3, 9),
    _RsClientPPPoEClientConnTime_Type()
)
rsClientPPPoEClientConnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rsClientPPPoEClientConnTime.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAPID-CLIENT-MIB",
    **{"rsInfoModule": rsInfoModule,
       "rsClientMIB": rsClientMIB,
       "rsClientDHCPServer": rsClientDHCPServer,
       "rsClientDHCPServerEnable": rsClientDHCPServerEnable,
       "rsClientDHCPServerStartIpAddress": rsClientDHCPServerStartIpAddress,
       "rsClientDHCPServerEndIpAddress": rsClientDHCPServerEndIpAddress,
       "rsClientDHCPServerLeaseTime": rsClientDHCPServerLeaseTime,
       "rsClientDHCPServerNum": rsClientDHCPServerNum,
       "rsClientDHCPServerConnTable": rsClientDHCPServerConnTable,
       "rsClientDHCPServerConnEntry": rsClientDHCPServerConnEntry,
       "rsClientDHCPServerConnClientHostName": rsClientDHCPServerConnClientHostName,
       "rsClientDHCPServerConnIPAddr": rsClientDHCPServerConnIPAddr,
       "rsClientDHCPServerConnMACAddr": rsClientDHCPServerConnMACAddr,
       "rsClientDHCPServerConnLeaseTimeStart": rsClientDHCPServerConnLeaseTimeStart,
       "rsClientDHCPServerConnLeaseTimeEnd": rsClientDHCPServerConnLeaseTimeEnd,
       "rsClientDHCPServerRelayServer": rsClientDHCPServerRelayServer,
       "rsClientDHCPClient": rsClientDHCPClient,
       "rsClientDHCPClientEnable": rsClientDHCPClientEnable,
       "rsClientDHCPClientDomainName": rsClientDHCPClientDomainName,
       "rsClientDHCPClientDefaultGateway": rsClientDHCPClientDefaultGateway,
       "rsClientDHCPClientDNSOne": rsClientDHCPClientDNSOne,
       "rsClientDHCPClientDNSTwo": rsClientDHCPClientDNSTwo,
       "rsClientPPPoEClient": rsClientPPPoEClient,
       "rsClientPPPoEClientEnable": rsClientPPPoEClientEnable,
       "rsClientPPPoEClientADSLStatus": rsClientPPPoEClientADSLStatus,
       "rsClientPPPoEClientLocalIPAddr": rsClientPPPoEClientLocalIPAddr,
       "rsClientPPPoEClientRemoteIPAddr": rsClientPPPoEClientRemoteIPAddr,
       "rsClientPPPoEClientNetMask": rsClientPPPoEClientNetMask,
       "rsClientPPPoEClientDNSOne": rsClientPPPoEClientDNSOne,
       "rsClientPPPoEClientDNSTwo": rsClientPPPoEClientDNSTwo,
       "rsClientPPPoEADSLPeerMACAddr": rsClientPPPoEADSLPeerMACAddr,
       "rsClientPPPoEClientConnTime": rsClientPPPoEClientConnTime}
)
