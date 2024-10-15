# SNMP MIB module (CIG-CLIENTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIG-CLIENTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:13 2024
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

cigClients = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Avaya_ObjectIdentity = ObjectIdentity
avaya = _Avaya_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2)
)
_Lsg_ObjectIdentity = ObjectIdentity
lsg = _Lsg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1)
)
_CigDhcpClients_ObjectIdentity = ObjectIdentity
cigDhcpClients = _CigDhcpClients_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1)
)
_CigDhcpClientsNotification_ObjectIdentity = ObjectIdentity
cigDhcpClientsNotification = _CigDhcpClientsNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 0)
)
_CigDhcpClientsTable_Object = MibTable
cigDhcpClientsTable = _CigDhcpClientsTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1)
)
if mibBuilder.loadTexts:
    cigDhcpClientsTable.setStatus("current")
_CigDhcpClientsEntry_Object = MibTableRow
cigDhcpClientsEntry = _CigDhcpClientsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1)
)
cigDhcpClientsEntry.setIndexNames(
    (0, "CIG-CLIENTS-MIB", "cigDhcpClientsIfIndex"),
)
if mibBuilder.loadTexts:
    cigDhcpClientsEntry.setStatus("current")
_CigDhcpClientsIfIndex_Type = Integer32
_CigDhcpClientsIfIndex_Object = MibTableColumn
cigDhcpClientsIfIndex = _CigDhcpClientsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 1),
    _CigDhcpClientsIfIndex_Type()
)
cigDhcpClientsIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsIfIndex.setStatus("current")
_CigDhcpClientsRowStatus_Type = RowStatus
_CigDhcpClientsRowStatus_Object = MibTableColumn
cigDhcpClientsRowStatus = _CigDhcpClientsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 2),
    _CigDhcpClientsRowStatus_Type()
)
cigDhcpClientsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpClientsRowStatus.setStatus("current")


class _CigDhcpClientsIfAlias_Type(DisplayString):
    """Custom type cigDhcpClientsIfAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CigDhcpClientsIfAlias_Type.__name__ = "DisplayString"
_CigDhcpClientsIfAlias_Object = MibTableColumn
cigDhcpClientsIfAlias = _CigDhcpClientsIfAlias_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 3),
    _CigDhcpClientsIfAlias_Type()
)
cigDhcpClientsIfAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsIfAlias.setStatus("current")


class _CigDhcpClientsIPAddress_Type(IpAddress):
    """Custom type cigDhcpClientsIPAddress based on IpAddress"""
    defaultHexValue = "00000000"


_CigDhcpClientsIPAddress_Object = MibTableColumn
cigDhcpClientsIPAddress = _CigDhcpClientsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 4),
    _CigDhcpClientsIPAddress_Type()
)
cigDhcpClientsIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsIPAddress.setStatus("current")
_CigDhcpClientsSubnetMask_Type = IpAddress
_CigDhcpClientsSubnetMask_Object = MibTableColumn
cigDhcpClientsSubnetMask = _CigDhcpClientsSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 5),
    _CigDhcpClientsSubnetMask_Type()
)
cigDhcpClientsSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsSubnetMask.setStatus("current")


class _CigDhcpClientsClientId_Type(OctetString):
    """Custom type cigDhcpClientsClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CigDhcpClientsClientId_Type.__name__ = "OctetString"
_CigDhcpClientsClientId_Object = MibTableColumn
cigDhcpClientsClientId = _CigDhcpClientsClientId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 6),
    _CigDhcpClientsClientId_Type()
)
cigDhcpClientsClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpClientsClientId.setStatus("current")


class _CigDhcpClientsHostName_Type(DisplayString):
    """Custom type cigDhcpClientsHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_CigDhcpClientsHostName_Type.__name__ = "DisplayString"
_CigDhcpClientsHostName_Object = MibTableColumn
cigDhcpClientsHostName = _CigDhcpClientsHostName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 7),
    _CigDhcpClientsHostName_Type()
)
cigDhcpClientsHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpClientsHostName.setStatus("current")


class _CigDhcpClientsRequestLeaseTime_Type(Unsigned32):
    """Custom type cigDhcpClientsRequestLeaseTime based on Unsigned32"""
    defaultValue = 0


_CigDhcpClientsRequestLeaseTime_Object = MibTableColumn
cigDhcpClientsRequestLeaseTime = _CigDhcpClientsRequestLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 8),
    _CigDhcpClientsRequestLeaseTime_Type()
)
cigDhcpClientsRequestLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpClientsRequestLeaseTime.setStatus("current")


class _CigDhcpClientsReceiveLeaseTime_Type(Unsigned32):
    """Custom type cigDhcpClientsReceiveLeaseTime based on Unsigned32"""
    defaultValue = 0


_CigDhcpClientsReceiveLeaseTime_Object = MibTableColumn
cigDhcpClientsReceiveLeaseTime = _CigDhcpClientsReceiveLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 9),
    _CigDhcpClientsReceiveLeaseTime_Type()
)
cigDhcpClientsReceiveLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsReceiveLeaseTime.setStatus("current")


class _CigDhcpClientsRemainLeaseTime_Type(Unsigned32):
    """Custom type cigDhcpClientsRemainLeaseTime based on Unsigned32"""
    defaultValue = 0


_CigDhcpClientsRemainLeaseTime_Object = MibTableColumn
cigDhcpClientsRemainLeaseTime = _CigDhcpClientsRemainLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 10),
    _CigDhcpClientsRemainLeaseTime_Type()
)
cigDhcpClientsRemainLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsRemainLeaseTime.setStatus("current")


class _CigDhcpClientsRenewLeaseTime_Type(Unsigned32):
    """Custom type cigDhcpClientsRenewLeaseTime based on Unsigned32"""
    defaultValue = 0


_CigDhcpClientsRenewLeaseTime_Object = MibTableColumn
cigDhcpClientsRenewLeaseTime = _CigDhcpClientsRenewLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 11),
    _CigDhcpClientsRenewLeaseTime_Type()
)
cigDhcpClientsRenewLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsRenewLeaseTime.setStatus("current")


class _CigDhcpClientsRebindLeaseTime_Type(Unsigned32):
    """Custom type cigDhcpClientsRebindLeaseTime based on Unsigned32"""
    defaultValue = 0


_CigDhcpClientsRebindLeaseTime_Object = MibTableColumn
cigDhcpClientsRebindLeaseTime = _CigDhcpClientsRebindLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 12),
    _CigDhcpClientsRebindLeaseTime_Type()
)
cigDhcpClientsRebindLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsRebindLeaseTime.setStatus("current")


class _CigDhcpClientsDefaultGatewayList_Type(DisplayString):
    """Custom type cigDhcpClientsDefaultGatewayList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CigDhcpClientsDefaultGatewayList_Type.__name__ = "DisplayString"
_CigDhcpClientsDefaultGatewayList_Object = MibTableColumn
cigDhcpClientsDefaultGatewayList = _CigDhcpClientsDefaultGatewayList_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 13),
    _CigDhcpClientsDefaultGatewayList_Type()
)
cigDhcpClientsDefaultGatewayList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsDefaultGatewayList.setStatus("current")


class _CigDhcpClientsDnsServerList_Type(DisplayString):
    """Custom type cigDhcpClientsDnsServerList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CigDhcpClientsDnsServerList_Type.__name__ = "DisplayString"
_CigDhcpClientsDnsServerList_Object = MibTableColumn
cigDhcpClientsDnsServerList = _CigDhcpClientsDnsServerList_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 14),
    _CigDhcpClientsDnsServerList_Type()
)
cigDhcpClientsDnsServerList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsDnsServerList.setStatus("current")


class _CigDhcpClientsDomainName_Type(DisplayString):
    """Custom type cigDhcpClientsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_CigDhcpClientsDomainName_Type.__name__ = "DisplayString"
_CigDhcpClientsDomainName_Object = MibTableColumn
cigDhcpClientsDomainName = _CigDhcpClientsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 15),
    _CigDhcpClientsDomainName_Type()
)
cigDhcpClientsDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsDomainName.setStatus("current")
_CigDhcpClientsServerIpAddr_Type = IpAddress
_CigDhcpClientsServerIpAddr_Object = MibTableColumn
cigDhcpClientsServerIpAddr = _CigDhcpClientsServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 16),
    _CigDhcpClientsServerIpAddr_Type()
)
cigDhcpClientsServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsServerIpAddr.setStatus("current")


class _CigDhcpClientsOperations_Type(Integer32):
    """Custom type cigDhcpClientsOperations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("idle", 1),
          ("release", 2),
          ("renew", 3))
    )


_CigDhcpClientsOperations_Type.__name__ = "Integer32"
_CigDhcpClientsOperations_Object = MibTableColumn
cigDhcpClientsOperations = _CigDhcpClientsOperations_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 17),
    _CigDhcpClientsOperations_Type()
)
cigDhcpClientsOperations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpClientsOperations.setStatus("current")


class _CigDhcpClientsStatus_Type(Integer32):
    """Custom type cigDhcpClientsStatus based on Integer32"""
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
              255)
        )
    )
    namedValues = NamedValues(
        *(("bound", 3),
          ("decline", 7),
          ("idle", 9),
          ("notSupported", 255),
          ("rebind", 4),
          ("reboot", 8),
          ("release", 6),
          ("renew", 5),
          ("request", 2),
          ("select", 1))
    )


_CigDhcpClientsStatus_Type.__name__ = "Integer32"
_CigDhcpClientsStatus_Object = MibTableColumn
cigDhcpClientsStatus = _CigDhcpClientsStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 18),
    _CigDhcpClientsStatus_Type()
)
cigDhcpClientsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDhcpClientsStatus.setStatus("current")


class _CigDhcpClientsRequestBitmap_Type(OctetString):
    """Custom type cigDhcpClientsRequestBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_CigDhcpClientsRequestBitmap_Type.__name__ = "OctetString"
_CigDhcpClientsRequestBitmap_Object = MibTableColumn
cigDhcpClientsRequestBitmap = _CigDhcpClientsRequestBitmap_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 19),
    _CigDhcpClientsRequestBitmap_Type()
)
cigDhcpClientsRequestBitmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpClientsRequestBitmap.setStatus("current")


class _CigDhcpClientsDefaultRouterTrackId_Type(Unsigned32):
    """Custom type cigDhcpClientsDefaultRouterTrackId based on Unsigned32"""
    defaultValue = 0


_CigDhcpClientsDefaultRouterTrackId_Object = MibTableColumn
cigDhcpClientsDefaultRouterTrackId = _CigDhcpClientsDefaultRouterTrackId_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 1, 1, 20),
    _CigDhcpClientsDefaultRouterTrackId_Type()
)
cigDhcpClientsDefaultRouterTrackId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDhcpClientsDefaultRouterTrackId.setStatus("current")
_CigDnsResolver_ObjectIdentity = ObjectIdentity
cigDnsResolver = _CigDnsResolver_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2)
)
_CigDnsResolverGenConfig_ObjectIdentity = ObjectIdentity
cigDnsResolverGenConfig = _CigDnsResolverGenConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 1)
)


class _CigDnsResolverMode_Type(TruthValue):
    """Custom type cigDnsResolverMode based on TruthValue"""


_CigDnsResolverMode_Object = MibScalar
cigDnsResolverMode = _CigDnsResolverMode_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 1, 1),
    _CigDnsResolverMode_Type()
)
cigDnsResolverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverMode.setStatus("current")


class _CigDnsResolverRetry_Type(Unsigned32):
    """Custom type cigDnsResolverRetry based on Unsigned32"""
    defaultValue = 2


_CigDnsResolverRetry_Object = MibScalar
cigDnsResolverRetry = _CigDnsResolverRetry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 1, 2),
    _CigDnsResolverRetry_Type()
)
cigDnsResolverRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverRetry.setStatus("current")


class _CigDnsResolverTimeout_Type(Unsigned32):
    """Custom type cigDnsResolverTimeout based on Unsigned32"""
    defaultValue = 3


_CigDnsResolverTimeout_Object = MibScalar
cigDnsResolverTimeout = _CigDnsResolverTimeout_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 1, 3),
    _CigDnsResolverTimeout_Type()
)
cigDnsResolverTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverTimeout.setStatus("current")


class _CigDnsResolverOperations_Type(Integer32):
    """Custom type cigDnsResolverOperations based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clearDNSCache", 3),
          ("clearDynamicServers", 2),
          ("idle", 1))
    )


_CigDnsResolverOperations_Type.__name__ = "Integer32"
_CigDnsResolverOperations_Object = MibScalar
cigDnsResolverOperations = _CigDnsResolverOperations_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 1, 4),
    _CigDnsResolverOperations_Type()
)
cigDnsResolverOperations.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverOperations.setStatus("current")
_CigDnsResolverDnsServersListTable_Object = MibTable
cigDnsResolverDnsServersListTable = _CigDnsResolverDnsServersListTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 2)
)
if mibBuilder.loadTexts:
    cigDnsResolverDnsServersListTable.setStatus("current")
_CigDnsResolverDnsServersListEntry_Object = MibTableRow
cigDnsResolverDnsServersListEntry = _CigDnsResolverDnsServersListEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 2, 1)
)
cigDnsResolverDnsServersListEntry.setIndexNames(
    (0, "CIG-CLIENTS-MIB", "cigDnsResolverDnsServersListIndex"),
)
if mibBuilder.loadTexts:
    cigDnsResolverDnsServersListEntry.setStatus("current")
_CigDnsResolverDnsServersListIndex_Type = Integer32
_CigDnsResolverDnsServersListIndex_Object = MibTableColumn
cigDnsResolverDnsServersListIndex = _CigDnsResolverDnsServersListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 2, 1, 1),
    _CigDnsResolverDnsServersListIndex_Type()
)
cigDnsResolverDnsServersListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServersListIndex.setStatus("current")


class _CigDnsResolverDnsServersListDescription_Type(DisplayString):
    """Custom type cigDnsResolverDnsServersListDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CigDnsResolverDnsServersListDescription_Type.__name__ = "DisplayString"
_CigDnsResolverDnsServersListDescription_Object = MibTableColumn
cigDnsResolverDnsServersListDescription = _CigDnsResolverDnsServersListDescription_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 2, 1, 2),
    _CigDnsResolverDnsServersListDescription_Type()
)
cigDnsResolverDnsServersListDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServersListDescription.setStatus("current")
_CigDnsResolverDnsServersListRowStatus_Type = RowStatus
_CigDnsResolverDnsServersListRowStatus_Object = MibTableColumn
cigDnsResolverDnsServersListRowStatus = _CigDnsResolverDnsServersListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 2, 1, 3),
    _CigDnsResolverDnsServersListRowStatus_Type()
)
cigDnsResolverDnsServersListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServersListRowStatus.setStatus("current")
_CigDnsResolverDnsServerTable_Object = MibTable
cigDnsResolverDnsServerTable = _CigDnsResolverDnsServerTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 3)
)
if mibBuilder.loadTexts:
    cigDnsResolverDnsServerTable.setStatus("current")
_CigDnsResolverDnsServerEntry_Object = MibTableRow
cigDnsResolverDnsServerEntry = _CigDnsResolverDnsServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 3, 1)
)
cigDnsResolverDnsServerEntry.setIndexNames(
    (0, "CIG-CLIENTS-MIB", "cigDnsResolverDnsServerListIndex"),
    (0, "CIG-CLIENTS-MIB", "cigDnsResolverDnsServerIndex"),
)
if mibBuilder.loadTexts:
    cigDnsResolverDnsServerEntry.setStatus("current")
_CigDnsResolverDnsServerListIndex_Type = Integer32
_CigDnsResolverDnsServerListIndex_Object = MibTableColumn
cigDnsResolverDnsServerListIndex = _CigDnsResolverDnsServerListIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 3, 1, 1),
    _CigDnsResolverDnsServerListIndex_Type()
)
cigDnsResolverDnsServerListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServerListIndex.setStatus("current")
_CigDnsResolverDnsServerIndex_Type = Integer32
_CigDnsResolverDnsServerIndex_Object = MibTableColumn
cigDnsResolverDnsServerIndex = _CigDnsResolverDnsServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 3, 1, 2),
    _CigDnsResolverDnsServerIndex_Type()
)
cigDnsResolverDnsServerIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServerIndex.setStatus("current")
_CigDnsResolverDnsServerIpAddress_Type = IpAddress
_CigDnsResolverDnsServerIpAddress_Object = MibTableColumn
cigDnsResolverDnsServerIpAddress = _CigDnsResolverDnsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 3, 1, 3),
    _CigDnsResolverDnsServerIpAddress_Type()
)
cigDnsResolverDnsServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServerIpAddress.setStatus("current")
_CigDnsResolverDnsServerIfIndex_Type = Integer32
_CigDnsResolverDnsServerIfIndex_Object = MibTableColumn
cigDnsResolverDnsServerIfIndex = _CigDnsResolverDnsServerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 3, 1, 4),
    _CigDnsResolverDnsServerIfIndex_Type()
)
cigDnsResolverDnsServerIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServerIfIndex.setStatus("current")


class _CigDnsResolverDnsServerType_Type(Integer32):
    """Custom type cigDnsResolverDnsServerType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic-dhcp", 2),
          ("dynamic-ppp", 3),
          ("static", 1))
    )


_CigDnsResolverDnsServerType_Type.__name__ = "Integer32"
_CigDnsResolverDnsServerType_Object = MibTableColumn
cigDnsResolverDnsServerType = _CigDnsResolverDnsServerType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 3, 1, 5),
    _CigDnsResolverDnsServerType_Type()
)
cigDnsResolverDnsServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServerType.setStatus("current")
_CigDnsResolverDnsServerRowStatus_Type = RowStatus
_CigDnsResolverDnsServerRowStatus_Object = MibTableColumn
cigDnsResolverDnsServerRowStatus = _CigDnsResolverDnsServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 3, 1, 6),
    _CigDnsResolverDnsServerRowStatus_Type()
)
cigDnsResolverDnsServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServerRowStatus.setStatus("current")
_CigDnsResolverDnsServerInetAddressType_Type = InetAddressType
_CigDnsResolverDnsServerInetAddressType_Object = MibTableColumn
cigDnsResolverDnsServerInetAddressType = _CigDnsResolverDnsServerInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 3, 1, 7),
    _CigDnsResolverDnsServerInetAddressType_Type()
)
cigDnsResolverDnsServerInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServerInetAddressType.setStatus("current")
_CigDnsResolverDnsServerInetAddress_Type = InetAddress
_CigDnsResolverDnsServerInetAddress_Object = MibTableColumn
cigDnsResolverDnsServerInetAddress = _CigDnsResolverDnsServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 3, 1, 8),
    _CigDnsResolverDnsServerInetAddress_Type()
)
cigDnsResolverDnsServerInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverDnsServerInetAddress.setStatus("current")
_CigDnsResolverDomainTable_Object = MibTable
cigDnsResolverDomainTable = _CigDnsResolverDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 4)
)
if mibBuilder.loadTexts:
    cigDnsResolverDomainTable.setStatus("current")
_CigDnsResolverDomainEntry_Object = MibTableRow
cigDnsResolverDomainEntry = _CigDnsResolverDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 4, 1)
)
cigDnsResolverDomainEntry.setIndexNames(
    (0, "CIG-CLIENTS-MIB", "cigDnsResolverDomainIndex"),
)
if mibBuilder.loadTexts:
    cigDnsResolverDomainEntry.setStatus("current")
_CigDnsResolverDomainIndex_Type = Integer32
_CigDnsResolverDomainIndex_Object = MibTableColumn
cigDnsResolverDomainIndex = _CigDnsResolverDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 4, 1, 1),
    _CigDnsResolverDomainIndex_Type()
)
cigDnsResolverDomainIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cigDnsResolverDomainIndex.setStatus("current")


class _CigDnsResolverDomain_Type(DisplayString):
    """Custom type cigDnsResolverDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_CigDnsResolverDomain_Type.__name__ = "DisplayString"
_CigDnsResolverDomain_Object = MibTableColumn
cigDnsResolverDomain = _CigDnsResolverDomain_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 4, 1, 2),
    _CigDnsResolverDomain_Type()
)
cigDnsResolverDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverDomain.setStatus("current")
_CigDnsResolverDomainRowStatus_Type = RowStatus
_CigDnsResolverDomainRowStatus_Object = MibTableColumn
cigDnsResolverDomainRowStatus = _CigDnsResolverDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 2, 4, 1, 3),
    _CigDnsResolverDomainRowStatus_Type()
)
cigDnsResolverDomainRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cigDnsResolverDomainRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects

cigDhcpClientsConflictDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 1, 17, 1, 0, 1)
)
cigDhcpClientsConflictDetectionTrap.setObjects(
      *(("CIG-CLIENTS-MIB", "cigDhcpClientsIfAlias"),
        ("CIG-CLIENTS-MIB", "cigDhcpClientsIPAddress"),
        ("CIG-CLIENTS-MIB", "cigDhcpClientsHostName"),
        ("CIG-CLIENTS-MIB", "cigDhcpClientsClientId"),
        ("CIG-CLIENTS-MIB", "cigDhcpClientsServerIpAddr"))
)
if mibBuilder.loadTexts:
    cigDhcpClientsConflictDetectionTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIG-CLIENTS-MIB",
    **{"avaya": avaya,
       "mibs": mibs,
       "lsg": lsg,
       "cigClients": cigClients,
       "cigDhcpClients": cigDhcpClients,
       "cigDhcpClientsNotification": cigDhcpClientsNotification,
       "cigDhcpClientsConflictDetectionTrap": cigDhcpClientsConflictDetectionTrap,
       "cigDhcpClientsTable": cigDhcpClientsTable,
       "cigDhcpClientsEntry": cigDhcpClientsEntry,
       "cigDhcpClientsIfIndex": cigDhcpClientsIfIndex,
       "cigDhcpClientsRowStatus": cigDhcpClientsRowStatus,
       "cigDhcpClientsIfAlias": cigDhcpClientsIfAlias,
       "cigDhcpClientsIPAddress": cigDhcpClientsIPAddress,
       "cigDhcpClientsSubnetMask": cigDhcpClientsSubnetMask,
       "cigDhcpClientsClientId": cigDhcpClientsClientId,
       "cigDhcpClientsHostName": cigDhcpClientsHostName,
       "cigDhcpClientsRequestLeaseTime": cigDhcpClientsRequestLeaseTime,
       "cigDhcpClientsReceiveLeaseTime": cigDhcpClientsReceiveLeaseTime,
       "cigDhcpClientsRemainLeaseTime": cigDhcpClientsRemainLeaseTime,
       "cigDhcpClientsRenewLeaseTime": cigDhcpClientsRenewLeaseTime,
       "cigDhcpClientsRebindLeaseTime": cigDhcpClientsRebindLeaseTime,
       "cigDhcpClientsDefaultGatewayList": cigDhcpClientsDefaultGatewayList,
       "cigDhcpClientsDnsServerList": cigDhcpClientsDnsServerList,
       "cigDhcpClientsDomainName": cigDhcpClientsDomainName,
       "cigDhcpClientsServerIpAddr": cigDhcpClientsServerIpAddr,
       "cigDhcpClientsOperations": cigDhcpClientsOperations,
       "cigDhcpClientsStatus": cigDhcpClientsStatus,
       "cigDhcpClientsRequestBitmap": cigDhcpClientsRequestBitmap,
       "cigDhcpClientsDefaultRouterTrackId": cigDhcpClientsDefaultRouterTrackId,
       "cigDnsResolver": cigDnsResolver,
       "cigDnsResolverGenConfig": cigDnsResolverGenConfig,
       "cigDnsResolverMode": cigDnsResolverMode,
       "cigDnsResolverRetry": cigDnsResolverRetry,
       "cigDnsResolverTimeout": cigDnsResolverTimeout,
       "cigDnsResolverOperations": cigDnsResolverOperations,
       "cigDnsResolverDnsServersListTable": cigDnsResolverDnsServersListTable,
       "cigDnsResolverDnsServersListEntry": cigDnsResolverDnsServersListEntry,
       "cigDnsResolverDnsServersListIndex": cigDnsResolverDnsServersListIndex,
       "cigDnsResolverDnsServersListDescription": cigDnsResolverDnsServersListDescription,
       "cigDnsResolverDnsServersListRowStatus": cigDnsResolverDnsServersListRowStatus,
       "cigDnsResolverDnsServerTable": cigDnsResolverDnsServerTable,
       "cigDnsResolverDnsServerEntry": cigDnsResolverDnsServerEntry,
       "cigDnsResolverDnsServerListIndex": cigDnsResolverDnsServerListIndex,
       "cigDnsResolverDnsServerIndex": cigDnsResolverDnsServerIndex,
       "cigDnsResolverDnsServerIpAddress": cigDnsResolverDnsServerIpAddress,
       "cigDnsResolverDnsServerIfIndex": cigDnsResolverDnsServerIfIndex,
       "cigDnsResolverDnsServerType": cigDnsResolverDnsServerType,
       "cigDnsResolverDnsServerRowStatus": cigDnsResolverDnsServerRowStatus,
       "cigDnsResolverDnsServerInetAddressType": cigDnsResolverDnsServerInetAddressType,
       "cigDnsResolverDnsServerInetAddress": cigDnsResolverDnsServerInetAddress,
       "cigDnsResolverDomainTable": cigDnsResolverDomainTable,
       "cigDnsResolverDomainEntry": cigDnsResolverDomainEntry,
       "cigDnsResolverDomainIndex": cigDnsResolverDomainIndex,
       "cigDnsResolverDomain": cigDnsResolverDomain,
       "cigDnsResolverDomainRowStatus": cigDnsResolverDomainRowStatus}
)
