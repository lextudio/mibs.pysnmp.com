# SNMP MIB module (HUAWEI-BGP-VPN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-BGP-VPN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:02:55 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(ifIndex,
 ifName) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex",
    "ifName")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(mplsL3VpnVrfConfMidRteThresh,
 mplsL3VpnVrfPerfCurrNumRoutes) = mibBuilder.importSymbols(
    "MPLS-L3VPN-STD-MIB",
    "mplsL3VpnVrfConfMidRteThresh",
    "mplsL3VpnVrfPerfCurrNumRoutes")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

hwBgpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177)
)
hwBgpMIB.setRevisions(
        ("2015-02-10 10:10",
         "2015-01-31 14:35",
         "2015-01-19 11:15",
         "2014-11-20 11:15",
         "2014-06-18 11:40",
         "2014-05-30 15:40",
         "2014-03-18 15:02",
         "2014-03-10 09:55",
         "2008-12-26 09:55")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class HWBgpAfi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              25,
              196)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2),
          ("l2vpn", 196),
          ("vpls", 25))
    )



class HWBgpSafi(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              65,
              66,
              128,
              132)
        )
    )
    namedValues = NamedValues(
        *(("mcast-vpn", 5),
          ("mdt", 66),
          ("mpls", 4),
          ("multicast", 2),
          ("route-target", 132),
          ("unicast", 1),
          ("vpls", 65),
          ("vpn", 128))
    )



class MplsL3VpnName(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )



# MIB Managed Objects in the order of their OIDs

_HwBgpObjects_ObjectIdentity = ObjectIdentity
hwBgpObjects = _HwBgpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1)
)
_HwBgpPeers_ObjectIdentity = ObjectIdentity
hwBgpPeers = _HwBgpPeers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1)
)
_HwBgpPeerAddrFamilyTable_Object = MibTable
hwBgpPeerAddrFamilyTable = _HwBgpPeerAddrFamilyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwBgpPeerAddrFamilyTable.setStatus("current")
_HwBgpPeerAddrFamilyEntry_Object = MibTableRow
hwBgpPeerAddrFamilyEntry = _HwBgpPeerAddrFamilyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 1, 1)
)
hwBgpPeerAddrFamilyEntry.setIndexNames(
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpPeerInstanceId"),
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpPeerAddrFamilyAfi"),
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpPeerAddrFamilySafi"),
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpPeerType"),
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpPeerIPAddr"),
)
if mibBuilder.loadTexts:
    hwBgpPeerAddrFamilyEntry.setStatus("current")
_HwBgpPeerInstanceId_Type = Unsigned32
_HwBgpPeerInstanceId_Object = MibTableColumn
hwBgpPeerInstanceId = _HwBgpPeerInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 1, 1, 1),
    _HwBgpPeerInstanceId_Type()
)
hwBgpPeerInstanceId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpPeerInstanceId.setStatus("current")
_HwBgpPeerAddrFamilyAfi_Type = HWBgpAfi
_HwBgpPeerAddrFamilyAfi_Object = MibTableColumn
hwBgpPeerAddrFamilyAfi = _HwBgpPeerAddrFamilyAfi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 1, 1, 2),
    _HwBgpPeerAddrFamilyAfi_Type()
)
hwBgpPeerAddrFamilyAfi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpPeerAddrFamilyAfi.setStatus("current")
_HwBgpPeerAddrFamilySafi_Type = HWBgpSafi
_HwBgpPeerAddrFamilySafi_Object = MibTableColumn
hwBgpPeerAddrFamilySafi = _HwBgpPeerAddrFamilySafi_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 1, 1, 3),
    _HwBgpPeerAddrFamilySafi_Type()
)
hwBgpPeerAddrFamilySafi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpPeerAddrFamilySafi.setStatus("current")
_HwBgpPeerType_Type = InetAddressType
_HwBgpPeerType_Object = MibTableColumn
hwBgpPeerType = _HwBgpPeerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 1, 1, 4),
    _HwBgpPeerType_Type()
)
hwBgpPeerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpPeerType.setStatus("current")
_HwBgpPeerIPAddr_Type = InetAddress
_HwBgpPeerIPAddr_Object = MibTableColumn
hwBgpPeerIPAddr = _HwBgpPeerIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 1, 1, 5),
    _HwBgpPeerIPAddr_Type()
)
hwBgpPeerIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpPeerIPAddr.setStatus("current")
_HwBgpPeerVrfName_Type = OctetString
_HwBgpPeerVrfName_Object = MibTableColumn
hwBgpPeerVrfName = _HwBgpPeerVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 1, 1, 6),
    _HwBgpPeerVrfName_Type()
)
hwBgpPeerVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerVrfName.setStatus("current")
_HwBgpPeerTable_Object = MibTable
hwBgpPeerTable = _HwBgpPeerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwBgpPeerTable.setStatus("current")
_HwBgpPeerEntry_Object = MibTableRow
hwBgpPeerEntry = _HwBgpPeerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hwBgpPeerEntry.setStatus("current")
_HwBgpPeerNegotiatedVersion_Type = Unsigned32
_HwBgpPeerNegotiatedVersion_Object = MibTableColumn
hwBgpPeerNegotiatedVersion = _HwBgpPeerNegotiatedVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2, 1, 1),
    _HwBgpPeerNegotiatedVersion_Type()
)
hwBgpPeerNegotiatedVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerNegotiatedVersion.setStatus("current")
_HwBgpPeerRemoteAs_Type = Unsigned32
_HwBgpPeerRemoteAs_Object = MibTableColumn
hwBgpPeerRemoteAs = _HwBgpPeerRemoteAs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2, 1, 2),
    _HwBgpPeerRemoteAs_Type()
)
hwBgpPeerRemoteAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerRemoteAs.setStatus("current")
_HwBgpPeerRemoteAddr_Type = InetAddress
_HwBgpPeerRemoteAddr_Object = MibTableColumn
hwBgpPeerRemoteAddr = _HwBgpPeerRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2, 1, 4),
    _HwBgpPeerRemoteAddr_Type()
)
hwBgpPeerRemoteAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerRemoteAddr.setStatus("current")


class _HwBgpPeerState_Type(Integer32):
    """Custom type hwBgpPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("connect", 2),
          ("established", 6),
          ("idle", 1),
          ("openconfirm", 5),
          ("opensent", 4))
    )


_HwBgpPeerState_Type.__name__ = "Integer32"
_HwBgpPeerState_Object = MibTableColumn
hwBgpPeerState = _HwBgpPeerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2, 1, 5),
    _HwBgpPeerState_Type()
)
hwBgpPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerState.setStatus("current")
_HwBgpPeerFsmEstablishedCounter_Type = Unsigned32
_HwBgpPeerFsmEstablishedCounter_Object = MibTableColumn
hwBgpPeerFsmEstablishedCounter = _HwBgpPeerFsmEstablishedCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2, 1, 6),
    _HwBgpPeerFsmEstablishedCounter_Type()
)
hwBgpPeerFsmEstablishedCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBgpPeerFsmEstablishedCounter.setStatus("current")
_HwBgpPeerFsmEstablishedTime_Type = Gauge32
_HwBgpPeerFsmEstablishedTime_Object = MibTableColumn
hwBgpPeerFsmEstablishedTime = _HwBgpPeerFsmEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2, 1, 7),
    _HwBgpPeerFsmEstablishedTime_Type()
)
hwBgpPeerFsmEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerFsmEstablishedTime.setStatus("current")


class _HwBgpPeerGRStatus_Type(Integer32):
    """Custom type hwBgpPeerGRStatus based on Integer32"""
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
        *(("peerFinishRestart", 3),
          ("peerHelping", 4),
          ("peerNotBeingHelped", 1),
          ("peerRestarting", 2))
    )


_HwBgpPeerGRStatus_Type.__name__ = "Integer32"
_HwBgpPeerGRStatus_Object = MibTableColumn
hwBgpPeerGRStatus = _HwBgpPeerGRStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2, 1, 8),
    _HwBgpPeerGRStatus_Type()
)
hwBgpPeerGRStatus.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBgpPeerGRStatus.setStatus("current")
_HwBgpPeerLastError_Type = OctetString
_HwBgpPeerLastError_Object = MibTableColumn
hwBgpPeerLastError = _HwBgpPeerLastError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2, 1, 9),
    _HwBgpPeerLastError_Type()
)
hwBgpPeerLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerLastError.setStatus("current")
_HwBgpPeerUnAvaiReason_Type = Unsigned32
_HwBgpPeerUnAvaiReason_Object = MibTableColumn
hwBgpPeerUnAvaiReason = _HwBgpPeerUnAvaiReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 2, 1, 10),
    _HwBgpPeerUnAvaiReason_Type()
)
hwBgpPeerUnAvaiReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerUnAvaiReason.setStatus("current")
_HwBgpPeerRouteTable_Object = MibTable
hwBgpPeerRouteTable = _HwBgpPeerRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwBgpPeerRouteTable.setStatus("current")
_HwBgpPeerRouteEntry_Object = MibTableRow
hwBgpPeerRouteEntry = _HwBgpPeerRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwBgpPeerRouteEntry.setStatus("current")
_HwBgpPeerPrefixRcvCounter_Type = Counter32
_HwBgpPeerPrefixRcvCounter_Object = MibTableColumn
hwBgpPeerPrefixRcvCounter = _HwBgpPeerPrefixRcvCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 3, 1, 1),
    _HwBgpPeerPrefixRcvCounter_Type()
)
hwBgpPeerPrefixRcvCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerPrefixRcvCounter.setStatus("current")
_HwBgpPeerPrefixActiveCounter_Type = Counter32
_HwBgpPeerPrefixActiveCounter_Object = MibTableColumn
hwBgpPeerPrefixActiveCounter = _HwBgpPeerPrefixActiveCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 3, 1, 2),
    _HwBgpPeerPrefixActiveCounter_Type()
)
hwBgpPeerPrefixActiveCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerPrefixActiveCounter.setStatus("current")
_HwBgpPeerPrefixAdvCounter_Type = Counter32
_HwBgpPeerPrefixAdvCounter_Object = MibTableColumn
hwBgpPeerPrefixAdvCounter = _HwBgpPeerPrefixAdvCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 3, 1, 3),
    _HwBgpPeerPrefixAdvCounter_Type()
)
hwBgpPeerPrefixAdvCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerPrefixAdvCounter.setStatus("current")
_HwBgpPeerMessageTable_Object = MibTable
hwBgpPeerMessageTable = _HwBgpPeerMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hwBgpPeerMessageTable.setStatus("current")
_HwBgpPeerMessageEntry_Object = MibTableRow
hwBgpPeerMessageEntry = _HwBgpPeerMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    hwBgpPeerMessageEntry.setStatus("current")
_HwBgpPeerInTotalMsgCounter_Type = Counter32
_HwBgpPeerInTotalMsgCounter_Object = MibTableColumn
hwBgpPeerInTotalMsgCounter = _HwBgpPeerInTotalMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 1),
    _HwBgpPeerInTotalMsgCounter_Type()
)
hwBgpPeerInTotalMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerInTotalMsgCounter.setStatus("current")
_HwBgpPeerOutTotalMsgCounter_Type = Counter32
_HwBgpPeerOutTotalMsgCounter_Object = MibTableColumn
hwBgpPeerOutTotalMsgCounter = _HwBgpPeerOutTotalMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 2),
    _HwBgpPeerOutTotalMsgCounter_Type()
)
hwBgpPeerOutTotalMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerOutTotalMsgCounter.setStatus("current")
_HwBgpPeerInOpenMsgCounter_Type = Counter32
_HwBgpPeerInOpenMsgCounter_Object = MibTableColumn
hwBgpPeerInOpenMsgCounter = _HwBgpPeerInOpenMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 3),
    _HwBgpPeerInOpenMsgCounter_Type()
)
hwBgpPeerInOpenMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerInOpenMsgCounter.setStatus("current")
_HwBgpPeerInUpdateMsgCounter_Type = Counter32
_HwBgpPeerInUpdateMsgCounter_Object = MibTableColumn
hwBgpPeerInUpdateMsgCounter = _HwBgpPeerInUpdateMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 4),
    _HwBgpPeerInUpdateMsgCounter_Type()
)
hwBgpPeerInUpdateMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerInUpdateMsgCounter.setStatus("current")
_HwBgpPeerInNotificationMsgCounter_Type = Counter32
_HwBgpPeerInNotificationMsgCounter_Object = MibTableColumn
hwBgpPeerInNotificationMsgCounter = _HwBgpPeerInNotificationMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 5),
    _HwBgpPeerInNotificationMsgCounter_Type()
)
hwBgpPeerInNotificationMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerInNotificationMsgCounter.setStatus("current")
_HwBgpPeerInKeepAliveMsgCounter_Type = Counter32
_HwBgpPeerInKeepAliveMsgCounter_Object = MibTableColumn
hwBgpPeerInKeepAliveMsgCounter = _HwBgpPeerInKeepAliveMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 6),
    _HwBgpPeerInKeepAliveMsgCounter_Type()
)
hwBgpPeerInKeepAliveMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerInKeepAliveMsgCounter.setStatus("current")
_HwBgpPeerInRouteFreshMsgCounter_Type = Counter32
_HwBgpPeerInRouteFreshMsgCounter_Object = MibTableColumn
hwBgpPeerInRouteFreshMsgCounter = _HwBgpPeerInRouteFreshMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 7),
    _HwBgpPeerInRouteFreshMsgCounter_Type()
)
hwBgpPeerInRouteFreshMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerInRouteFreshMsgCounter.setStatus("current")
_HwBgpPeerOutOpenMsgCounter_Type = Counter32
_HwBgpPeerOutOpenMsgCounter_Object = MibTableColumn
hwBgpPeerOutOpenMsgCounter = _HwBgpPeerOutOpenMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 8),
    _HwBgpPeerOutOpenMsgCounter_Type()
)
hwBgpPeerOutOpenMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerOutOpenMsgCounter.setStatus("current")
_HwBgpPeerOutUpdateMsgCounter_Type = Counter32
_HwBgpPeerOutUpdateMsgCounter_Object = MibTableColumn
hwBgpPeerOutUpdateMsgCounter = _HwBgpPeerOutUpdateMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 9),
    _HwBgpPeerOutUpdateMsgCounter_Type()
)
hwBgpPeerOutUpdateMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerOutUpdateMsgCounter.setStatus("current")
_HwBgpPeerOutNotificationMsgCounter_Type = Counter32
_HwBgpPeerOutNotificationMsgCounter_Object = MibTableColumn
hwBgpPeerOutNotificationMsgCounter = _HwBgpPeerOutNotificationMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 10),
    _HwBgpPeerOutNotificationMsgCounter_Type()
)
hwBgpPeerOutNotificationMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerOutNotificationMsgCounter.setStatus("current")
_HwBgpPeerOutKeepAliveMsgCounter_Type = Counter32
_HwBgpPeerOutKeepAliveMsgCounter_Object = MibTableColumn
hwBgpPeerOutKeepAliveMsgCounter = _HwBgpPeerOutKeepAliveMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 11),
    _HwBgpPeerOutKeepAliveMsgCounter_Type()
)
hwBgpPeerOutKeepAliveMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerOutKeepAliveMsgCounter.setStatus("current")
_HwBgpPeerOutRouteFreshMsgCounter_Type = Counter32
_HwBgpPeerOutRouteFreshMsgCounter_Object = MibTableColumn
hwBgpPeerOutRouteFreshMsgCounter = _HwBgpPeerOutRouteFreshMsgCounter_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 4, 1, 12),
    _HwBgpPeerOutRouteFreshMsgCounter_Type()
)
hwBgpPeerOutRouteFreshMsgCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerOutRouteFreshMsgCounter.setStatus("current")
_HwBgpPeerConfigTable_Object = MibTable
hwBgpPeerConfigTable = _HwBgpPeerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hwBgpPeerConfigTable.setStatus("current")
_HwBgpPeerConfigEntry_Object = MibTableRow
hwBgpPeerConfigEntry = _HwBgpPeerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwBgpPeerConfigEntry.setStatus("current")
_HwBgpPeerConfigRouteLimitNum_Type = Unsigned32
_HwBgpPeerConfigRouteLimitNum_Object = MibTableColumn
hwBgpPeerConfigRouteLimitNum = _HwBgpPeerConfigRouteLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 5, 1, 1),
    _HwBgpPeerConfigRouteLimitNum_Type()
)
hwBgpPeerConfigRouteLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerConfigRouteLimitNum.setStatus("current")


class _HwBgpPeerConfigRouteLimitThreshold_Type(Unsigned32):
    """Custom type hwBgpPeerConfigRouteLimitThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwBgpPeerConfigRouteLimitThreshold_Type.__name__ = "Unsigned32"
_HwBgpPeerConfigRouteLimitThreshold_Object = MibTableColumn
hwBgpPeerConfigRouteLimitThreshold = _HwBgpPeerConfigRouteLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 5, 1, 2),
    _HwBgpPeerConfigRouteLimitThreshold_Type()
)
hwBgpPeerConfigRouteLimitThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerConfigRouteLimitThreshold.setStatus("current")
_HwBgpPeerSessionTable_Object = MibTable
hwBgpPeerSessionTable = _HwBgpPeerSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hwBgpPeerSessionTable.setStatus("current")
_HwBgpPeerSessionEntry_Object = MibTableRow
hwBgpPeerSessionEntry = _HwBgpPeerSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 6, 1)
)
hwBgpPeerSessionEntry.setIndexNames(
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionVrfName"),
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionRemoteAddrType"),
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionRemoteAddr"),
)
if mibBuilder.loadTexts:
    hwBgpPeerSessionEntry.setStatus("current")
_HwBgpPeerSessionVrfName_Type = OctetString
_HwBgpPeerSessionVrfName_Object = MibTableColumn
hwBgpPeerSessionVrfName = _HwBgpPeerSessionVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 6, 1, 1),
    _HwBgpPeerSessionVrfName_Type()
)
hwBgpPeerSessionVrfName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBgpPeerSessionVrfName.setStatus("current")
_HwBgpPeerSessionRemoteAddrType_Type = InetAddressType
_HwBgpPeerSessionRemoteAddrType_Object = MibTableColumn
hwBgpPeerSessionRemoteAddrType = _HwBgpPeerSessionRemoteAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 6, 1, 2),
    _HwBgpPeerSessionRemoteAddrType_Type()
)
hwBgpPeerSessionRemoteAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBgpPeerSessionRemoteAddrType.setStatus("current")
_HwBgpPeerSessionRemoteAddr_Type = InetAddress
_HwBgpPeerSessionRemoteAddr_Object = MibTableColumn
hwBgpPeerSessionRemoteAddr = _HwBgpPeerSessionRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 6, 1, 3),
    _HwBgpPeerSessionRemoteAddr_Type()
)
hwBgpPeerSessionRemoteAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBgpPeerSessionRemoteAddr.setStatus("current")
_HwBgpPeerSessionLocalAddrType_Type = InetAddressType
_HwBgpPeerSessionLocalAddrType_Object = MibTableColumn
hwBgpPeerSessionLocalAddrType = _HwBgpPeerSessionLocalAddrType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 6, 1, 4),
    _HwBgpPeerSessionLocalAddrType_Type()
)
hwBgpPeerSessionLocalAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerSessionLocalAddrType.setStatus("current")
_HwBgpPeerSessionLocalAddr_Type = InetAddress
_HwBgpPeerSessionLocalAddr_Object = MibTableColumn
hwBgpPeerSessionLocalAddr = _HwBgpPeerSessionLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 6, 1, 5),
    _HwBgpPeerSessionLocalAddr_Type()
)
hwBgpPeerSessionLocalAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerSessionLocalAddr.setStatus("current")


class _HwBgpPeerSessionUnavailableType_Type(Integer32):
    """Custom type hwBgpPeerSessionUnavailableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alwaysdown", 2),
          ("uptodown", 1))
    )


_HwBgpPeerSessionUnavailableType_Type.__name__ = "Integer32"
_HwBgpPeerSessionUnavailableType_Object = MibTableColumn
hwBgpPeerSessionUnavailableType = _HwBgpPeerSessionUnavailableType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 6, 1, 6),
    _HwBgpPeerSessionUnavailableType_Type()
)
hwBgpPeerSessionUnavailableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerSessionUnavailableType.setStatus("current")
_HwBgpPeerSessionLocalIfName_Type = OctetString
_HwBgpPeerSessionLocalIfName_Object = MibTableColumn
hwBgpPeerSessionLocalIfName = _HwBgpPeerSessionLocalIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 6, 1, 7),
    _HwBgpPeerSessionLocalIfName_Type()
)
hwBgpPeerSessionLocalIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerSessionLocalIfName.setStatus("current")


class _HwBgpPeerSessionReason_Type(Integer32):
    """Custom type hwBgpPeerSessionReason based on Integer32"""
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
              100)
        )
    )
    namedValues = NamedValues(
        *(("alarmClear", 100),
          ("configurationLeadPeerDown", 1),
          ("directConnectInterfaceDown", 6),
          ("holdTimerExpire", 4),
          ("peerIsNotUpForASpecifiedPeriodOfTime", 8),
          ("receiveErrorPacket", 3),
          ("receiveNotification", 2),
          ("remotePeerNotReachable", 5),
          ("routeLimit", 7))
    )


_HwBgpPeerSessionReason_Type.__name__ = "Integer32"
_HwBgpPeerSessionReason_Object = MibTableColumn
hwBgpPeerSessionReason = _HwBgpPeerSessionReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 1, 6, 1, 8),
    _HwBgpPeerSessionReason_Type()
)
hwBgpPeerSessionReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerSessionReason.setStatus("current")
_HwBgpRoute_ObjectIdentity = ObjectIdentity
hwBgpRoute = _HwBgpRoute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 2)
)
_HwBgpRouteLimitTable_ObjectIdentity = ObjectIdentity
hwBgpRouteLimitTable = _HwBgpRouteLimitTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 2, 1)
)


class _HwBgpRouteLimitindex_Type(Integer32):
    """Custom type hwBgpRouteLimitindex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv4public", 5),
          ("ipv4vrf", 3),
          ("ipv6", 2),
          ("ipv6public", 6),
          ("ipv6vrf", 4),
          ("l2ad", 7))
    )


_HwBgpRouteLimitindex_Type.__name__ = "Integer32"
_HwBgpRouteLimitindex_Object = MibScalar
hwBgpRouteLimitindex = _HwBgpRouteLimitindex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 2, 1, 1),
    _HwBgpRouteLimitindex_Type()
)
hwBgpRouteLimitindex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBgpRouteLimitindex.setStatus("current")
_HwBgpRouteCurNum_Type = Unsigned32
_HwBgpRouteCurNum_Object = MibScalar
hwBgpRouteCurNum = _HwBgpRouteCurNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 2, 1, 2),
    _HwBgpRouteCurNum_Type()
)
hwBgpRouteCurNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBgpRouteCurNum.setStatus("current")
_HwBgpRouteMaxNum_Type = Unsigned32
_HwBgpRouteMaxNum_Object = MibScalar
hwBgpRouteMaxNum = _HwBgpRouteMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 2, 1, 3),
    _HwBgpRouteMaxNum_Type()
)
hwBgpRouteMaxNum.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBgpRouteMaxNum.setStatus("current")
_HwBgpRouteThreshold_Type = Unsigned32
_HwBgpRouteThreshold_Object = MibScalar
hwBgpRouteThreshold = _HwBgpRouteThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 2, 1, 4),
    _HwBgpRouteThreshold_Type()
)
hwBgpRouteThreshold.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwBgpRouteThreshold.setStatus("current")
_HwBgpTraps_ObjectIdentity = ObjectIdentity
hwBgpTraps = _HwBgpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3)
)
_HwBgpScalars_ObjectIdentity = ObjectIdentity
hwBgpScalars = _HwBgpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 4)
)
_HwBgpPeerSessionNum_Type = Unsigned32
_HwBgpPeerSessionNum_Object = MibScalar
hwBgpPeerSessionNum = _HwBgpPeerSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 4, 1),
    _HwBgpPeerSessionNum_Type()
)
hwBgpPeerSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerSessionNum.setStatus("current")
_HwIBgpPeerSessionNum_Type = Unsigned32
_HwIBgpPeerSessionNum_Object = MibScalar
hwIBgpPeerSessionNum = _HwIBgpPeerSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 4, 2),
    _HwIBgpPeerSessionNum_Type()
)
hwIBgpPeerSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwIBgpPeerSessionNum.setStatus("current")
_HwEBgpPeerSessionNum_Type = Unsigned32
_HwEBgpPeerSessionNum_Object = MibScalar
hwEBgpPeerSessionNum = _HwEBgpPeerSessionNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 4, 3),
    _HwEBgpPeerSessionNum_Type()
)
hwEBgpPeerSessionNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwEBgpPeerSessionNum.setStatus("current")
_HwBgpPeerSessionMaxNum_Type = Unsigned32
_HwBgpPeerSessionMaxNum_Object = MibScalar
hwBgpPeerSessionMaxNum = _HwBgpPeerSessionMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 4, 4),
    _HwBgpPeerSessionMaxNum_Type()
)
hwBgpPeerSessionMaxNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpPeerSessionMaxNum.setStatus("current")
_HwBgpVpnObjects_ObjectIdentity = ObjectIdentity
hwBgpVpnObjects = _HwBgpVpnObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2)
)
_HwBgpVpnTunnelTable_Object = MibTable
hwBgpVpnTunnelTable = _HwBgpVpnTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1)
)
if mibBuilder.loadTexts:
    hwBgpVpnTunnelTable.setStatus("current")
_HwBgpVpnTunnelEntry_Object = MibTableRow
hwBgpVpnTunnelEntry = _HwBgpVpnTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1)
)
hwBgpVpnTunnelEntry.setIndexNames(
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelVrfName"),
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelPublicNetNextHop"),
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelId"),
)
if mibBuilder.loadTexts:
    hwBgpVpnTunnelEntry.setStatus("current")


class _HwBgpVpnTunnelVrfName_Type(OctetString):
    """Custom type hwBgpVpnTunnelVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwBgpVpnTunnelVrfName_Type.__name__ = "OctetString"
_HwBgpVpnTunnelVrfName_Object = MibTableColumn
hwBgpVpnTunnelVrfName = _HwBgpVpnTunnelVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 1),
    _HwBgpVpnTunnelVrfName_Type()
)
hwBgpVpnTunnelVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelVrfName.setStatus("current")
_HwBgpVpnTunnelPublicNetNextHop_Type = IpAddress
_HwBgpVpnTunnelPublicNetNextHop_Object = MibTableColumn
hwBgpVpnTunnelPublicNetNextHop = _HwBgpVpnTunnelPublicNetNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 2),
    _HwBgpVpnTunnelPublicNetNextHop_Type()
)
hwBgpVpnTunnelPublicNetNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelPublicNetNextHop.setStatus("current")
_HwBgpVpnTunnelId_Type = Unsigned32
_HwBgpVpnTunnelId_Object = MibTableColumn
hwBgpVpnTunnelId = _HwBgpVpnTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 3),
    _HwBgpVpnTunnelId_Type()
)
hwBgpVpnTunnelId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelId.setStatus("current")
_HwBgpVpnTunnelDestAddr_Type = IpAddress
_HwBgpVpnTunnelDestAddr_Object = MibTableColumn
hwBgpVpnTunnelDestAddr = _HwBgpVpnTunnelDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 4),
    _HwBgpVpnTunnelDestAddr_Type()
)
hwBgpVpnTunnelDestAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelDestAddr.setStatus("current")
_HwBgpVpnTunnelType_Type = Unsigned32
_HwBgpVpnTunnelType_Object = MibTableColumn
hwBgpVpnTunnelType = _HwBgpVpnTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 5),
    _HwBgpVpnTunnelType_Type()
)
hwBgpVpnTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelType.setStatus("current")
_HwBgpVpnTunnelSrcAddr_Type = IpAddress
_HwBgpVpnTunnelSrcAddr_Object = MibTableColumn
hwBgpVpnTunnelSrcAddr = _HwBgpVpnTunnelSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 6),
    _HwBgpVpnTunnelSrcAddr_Type()
)
hwBgpVpnTunnelSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelSrcAddr.setStatus("current")


class _HwBgpVpnTunnelOutIfName_Type(OctetString):
    """Custom type hwBgpVpnTunnelOutIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwBgpVpnTunnelOutIfName_Type.__name__ = "OctetString"
_HwBgpVpnTunnelOutIfName_Object = MibTableColumn
hwBgpVpnTunnelOutIfName = _HwBgpVpnTunnelOutIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 7),
    _HwBgpVpnTunnelOutIfName_Type()
)
hwBgpVpnTunnelOutIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelOutIfName.setStatus("current")
_HwBgpVpnTunnelIsLoadBalance_Type = Unsigned32
_HwBgpVpnTunnelIsLoadBalance_Object = MibTableColumn
hwBgpVpnTunnelIsLoadBalance = _HwBgpVpnTunnelIsLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 8),
    _HwBgpVpnTunnelIsLoadBalance_Type()
)
hwBgpVpnTunnelIsLoadBalance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelIsLoadBalance.setStatus("current")
_HwBgpVpnTunnelLspIndex_Type = Unsigned32
_HwBgpVpnTunnelLspIndex_Object = MibTableColumn
hwBgpVpnTunnelLspIndex = _HwBgpVpnTunnelLspIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 9),
    _HwBgpVpnTunnelLspIndex_Type()
)
hwBgpVpnTunnelLspIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelLspIndex.setStatus("current")


class _HwBgpVpnTunnelLspOutIfName_Type(OctetString):
    """Custom type hwBgpVpnTunnelLspOutIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwBgpVpnTunnelLspOutIfName_Type.__name__ = "OctetString"
_HwBgpVpnTunnelLspOutIfName_Object = MibTableColumn
hwBgpVpnTunnelLspOutIfName = _HwBgpVpnTunnelLspOutIfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 10),
    _HwBgpVpnTunnelLspOutIfName_Type()
)
hwBgpVpnTunnelLspOutIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelLspOutIfName.setStatus("current")
_HwBgpVpnTunnelLspOutLabel_Type = Unsigned32
_HwBgpVpnTunnelLspOutLabel_Object = MibTableColumn
hwBgpVpnTunnelLspOutLabel = _HwBgpVpnTunnelLspOutLabel_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 11),
    _HwBgpVpnTunnelLspOutLabel_Type()
)
hwBgpVpnTunnelLspOutLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelLspOutLabel.setStatus("current")
_HwBgpVpnTunnelLspNextHop_Type = IpAddress
_HwBgpVpnTunnelLspNextHop_Object = MibTableColumn
hwBgpVpnTunnelLspNextHop = _HwBgpVpnTunnelLspNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 12),
    _HwBgpVpnTunnelLspNextHop_Type()
)
hwBgpVpnTunnelLspNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelLspNextHop.setStatus("current")
_HwBgpVpnTunnelLspFec_Type = IpAddress
_HwBgpVpnTunnelLspFec_Object = MibTableColumn
hwBgpVpnTunnelLspFec = _HwBgpVpnTunnelLspFec_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 13),
    _HwBgpVpnTunnelLspFec_Type()
)
hwBgpVpnTunnelLspFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelLspFec.setStatus("current")
_HwBgpVpnTunnelLspFecPfxLen_Type = IpAddress
_HwBgpVpnTunnelLspFecPfxLen_Object = MibTableColumn
hwBgpVpnTunnelLspFecPfxLen = _HwBgpVpnTunnelLspFecPfxLen_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 14),
    _HwBgpVpnTunnelLspFecPfxLen_Type()
)
hwBgpVpnTunnelLspFecPfxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelLspFecPfxLen.setStatus("current")
_HwBgpVpnTunnelLspIsBackup_Type = Unsigned32
_HwBgpVpnTunnelLspIsBackup_Object = MibTableColumn
hwBgpVpnTunnelLspIsBackup = _HwBgpVpnTunnelLspIsBackup_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 15),
    _HwBgpVpnTunnelLspIsBackup_Type()
)
hwBgpVpnTunnelLspIsBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelLspIsBackup.setStatus("current")
_HwBgpVpnTunnelSignalProtocol_Type = Integer32
_HwBgpVpnTunnelSignalProtocol_Object = MibTableColumn
hwBgpVpnTunnelSignalProtocol = _HwBgpVpnTunnelSignalProtocol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 16),
    _HwBgpVpnTunnelSignalProtocol_Type()
)
hwBgpVpnTunnelSignalProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelSignalProtocol.setStatus("current")
_HwBgpVpnTunnelSessionTunnelId_Type = Integer32
_HwBgpVpnTunnelSessionTunnelId_Object = MibTableColumn
hwBgpVpnTunnelSessionTunnelId = _HwBgpVpnTunnelSessionTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 17),
    _HwBgpVpnTunnelSessionTunnelId_Type()
)
hwBgpVpnTunnelSessionTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelSessionTunnelId.setStatus("current")


class _HwBgpVpnTunnelTunnelName_Type(OctetString):
    """Custom type hwBgpVpnTunnelTunnelName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_HwBgpVpnTunnelTunnelName_Type.__name__ = "OctetString"
_HwBgpVpnTunnelTunnelName_Object = MibTableColumn
hwBgpVpnTunnelTunnelName = _HwBgpVpnTunnelTunnelName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 1, 1, 18),
    _HwBgpVpnTunnelTunnelName_Type()
)
hwBgpVpnTunnelTunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpVpnTunnelTunnelName.setStatus("current")
_HwBgpVpnServiceIdTable_Object = MibTable
hwBgpVpnServiceIdTable = _HwBgpVpnServiceIdTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 2)
)
if mibBuilder.loadTexts:
    hwBgpVpnServiceIdTable.setStatus("current")
_HwBgpVpnServiceIdEntry_Object = MibTableRow
hwBgpVpnServiceIdEntry = _HwBgpVpnServiceIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 2, 1)
)
hwBgpVpnServiceIdEntry.setIndexNames(
    (0, "HUAWEI-BGP-VPN-MIB", "hwBgpVpnServiceIdVrfName"),
)
if mibBuilder.loadTexts:
    hwBgpVpnServiceIdEntry.setStatus("current")


class _HwBgpVpnServiceIdVrfName_Type(OctetString):
    """Custom type hwBgpVpnServiceIdVrfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwBgpVpnServiceIdVrfName_Type.__name__ = "OctetString"
_HwBgpVpnServiceIdVrfName_Object = MibTableColumn
hwBgpVpnServiceIdVrfName = _HwBgpVpnServiceIdVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 2, 1, 1),
    _HwBgpVpnServiceIdVrfName_Type()
)
hwBgpVpnServiceIdVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBgpVpnServiceIdVrfName.setStatus("current")


class _HwBgpVpnServiceIdValue_Type(Unsigned32):
    """Custom type hwBgpVpnServiceIdValue based on Unsigned32"""
    defaultBinValue = 0


_HwBgpVpnServiceIdValue_Object = MibTableColumn
hwBgpVpnServiceIdValue = _HwBgpVpnServiceIdValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 2, 1, 2),
    _HwBgpVpnServiceIdValue_Type()
)
hwBgpVpnServiceIdValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBgpVpnServiceIdValue.setStatus("current")
_HwBgpVpnScalars_ObjectIdentity = ObjectIdentity
hwBgpVpnScalars = _HwBgpVpnScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 3)
)
_HwConfiguredVrfs_Type = Unsigned32
_HwConfiguredVrfs_Object = MibScalar
hwConfiguredVrfs = _HwConfiguredVrfs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 3, 1),
    _HwConfiguredVrfs_Type()
)
hwConfiguredVrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConfiguredVrfs.setStatus("current")
_HwConfiguredIpv4Vrfs_Type = Unsigned32
_HwConfiguredIpv4Vrfs_Object = MibScalar
hwConfiguredIpv4Vrfs = _HwConfiguredIpv4Vrfs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 3, 2),
    _HwConfiguredIpv4Vrfs_Type()
)
hwConfiguredIpv4Vrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConfiguredIpv4Vrfs.setStatus("current")
_HwConfiguredIpv6Vrfs_Type = Unsigned32
_HwConfiguredIpv6Vrfs_Object = MibScalar
hwConfiguredIpv6Vrfs = _HwConfiguredIpv6Vrfs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 2, 3, 3),
    _HwConfiguredIpv6Vrfs_Type()
)
hwConfiguredIpv6Vrfs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwConfiguredIpv6Vrfs.setStatus("current")
_HwBgpConformance_ObjectIdentity = ObjectIdentity
hwBgpConformance = _HwBgpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 3)
)
_HwBgpCompliances_ObjectIdentity = ObjectIdentity
hwBgpCompliances = _HwBgpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 3, 1)
)
_HwBgpGroups_ObjectIdentity = ObjectIdentity
hwBgpGroups = _HwBgpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 3, 2)
)
_HwBgpVpnConformance_ObjectIdentity = ObjectIdentity
hwBgpVpnConformance = _HwBgpVpnConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 5)
)
_HwBgpVpnCompliances_ObjectIdentity = ObjectIdentity
hwBgpVpnCompliances = _HwBgpVpnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 5, 1)
)
_HwBgpVpnExtGroups_ObjectIdentity = ObjectIdentity
hwBgpVpnExtGroups = _HwBgpVpnExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 5, 2)
)
_HwTnl2VpnTrapObjects_ObjectIdentity = ObjectIdentity
hwTnl2VpnTrapObjects = _HwTnl2VpnTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 6)
)
_HwTnl2VpnTrapTable_Object = MibTable
hwTnl2VpnTrapTable = _HwTnl2VpnTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 6, 1)
)
if mibBuilder.loadTexts:
    hwTnl2VpnTrapTable.setStatus("current")
_HwTnl2VpnTrapEntry_Object = MibTableRow
hwTnl2VpnTrapEntry = _HwTnl2VpnTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 6, 1, 1)
)
hwTnl2VpnTrapEntry.setIndexNames(
    (0, "HUAWEI-BGP-VPN-MIB", "hwVpnId"),
)
if mibBuilder.loadTexts:
    hwTnl2VpnTrapEntry.setStatus("current")
_HwVpnId_Type = Unsigned32
_HwVpnId_Object = MibTableColumn
hwVpnId = _HwVpnId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 6, 1, 1, 1),
    _HwVpnId_Type()
)
hwVpnId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVpnId.setStatus("current")
_HwVpnPublicNextHop_Type = IpAddress
_HwVpnPublicNextHop_Object = MibTableColumn
hwVpnPublicNextHop = _HwVpnPublicNextHop_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 6, 1, 1, 2),
    _HwVpnPublicNextHop_Type()
)
hwVpnPublicNextHop.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVpnPublicNextHop.setStatus("current")


class _HwTunnelReachablityEvent_Type(Unsigned32):
    """Custom type hwTunnelReachablityEvent based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_HwTunnelReachablityEvent_Type.__name__ = "Unsigned32"
_HwTunnelReachablityEvent_Object = MibTableColumn
hwTunnelReachablityEvent = _HwTunnelReachablityEvent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 6, 1, 1, 3),
    _HwTunnelReachablityEvent_Type()
)
hwTunnelReachablityEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwTunnelReachablityEvent.setStatus("current")
_HwVpnTrapCkeyValue_Type = Unsigned32
_HwVpnTrapCkeyValue_Object = MibTableColumn
hwVpnTrapCkeyValue = _HwVpnTrapCkeyValue_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 6, 1, 1, 4),
    _HwVpnTrapCkeyValue_Type()
)
hwVpnTrapCkeyValue.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwVpnTrapCkeyValue.setStatus("current")
_HwTnl2VpnTrapConformance_ObjectIdentity = ObjectIdentity
hwTnl2VpnTrapConformance = _HwTnl2VpnTrapConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 7)
)
_HwTnl2VpnTrapConformances_ObjectIdentity = ObjectIdentity
hwTnl2VpnTrapConformances = _HwTnl2VpnTrapConformances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 7, 1)
)
_HwTnl2VpnTrapGroups_ObjectIdentity = ObjectIdentity
hwTnl2VpnTrapGroups = _HwTnl2VpnTrapGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 7, 2)
)
_HwTnl2VpnTrapNotification_ObjectIdentity = ObjectIdentity
hwTnl2VpnTrapNotification = _HwTnl2VpnTrapNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 8)
)
_HwPeerDistributeObjects_ObjectIdentity = ObjectIdentity
hwPeerDistributeObjects = _HwPeerDistributeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9)
)
_HwBgpTotalRouteNumber_Type = Unsigned32
_HwBgpTotalRouteNumber_Object = MibScalar
hwBgpTotalRouteNumber = _HwBgpTotalRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 1),
    _HwBgpTotalRouteNumber_Type()
)
hwBgpTotalRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBgpTotalRouteNumber.setStatus("current")
_HwOsNodeTable_Object = MibTable
hwOsNodeTable = _HwOsNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 2)
)
if mibBuilder.loadTexts:
    hwOsNodeTable.setStatus("current")
_HwOsNodeEntry_Object = MibTableRow
hwOsNodeEntry = _HwOsNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 2, 1)
)
hwOsNodeEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    hwOsNodeEntry.setStatus("current")
_HwCurrSlot_Type = Unsigned32
_HwCurrSlot_Object = MibTableColumn
hwCurrSlot = _HwCurrSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 2, 1, 1),
    _HwCurrSlot_Type()
)
hwCurrSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCurrSlot.setStatus("current")
_HwPeerNumber_Type = Unsigned32
_HwPeerNumber_Object = MibTableColumn
hwPeerNumber = _HwPeerNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 2, 1, 4),
    _HwPeerNumber_Type()
)
hwPeerNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPeerNumber.setStatus("current")
_HwRouteNumber_Type = Unsigned32
_HwRouteNumber_Object = MibTableColumn
hwRouteNumber = _HwRouteNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 2, 1, 5),
    _HwRouteNumber_Type()
)
hwRouteNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRouteNumber.setStatus("current")
_HwDistributeTable_Object = MibTable
hwDistributeTable = _HwDistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 3)
)
if mibBuilder.loadTexts:
    hwDistributeTable.setStatus("current")
_HwDistributeEntry_Object = MibTableRow
hwDistributeEntry = _HwDistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 3, 1)
)
hwDistributeEntry.setIndexNames(
    (0, "HUAWEI-BGP-VPN-MIB", "hwDistributeName"),
)
if mibBuilder.loadTexts:
    hwDistributeEntry.setStatus("current")
_HwDistributeLocId_Type = Unsigned32
_HwDistributeLocId_Object = MibTableColumn
hwDistributeLocId = _HwDistributeLocId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 3, 1, 1),
    _HwDistributeLocId_Type()
)
hwDistributeLocId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDistributeLocId.setStatus("current")


class _HwDistributeName_Type(OctetString):
    """Custom type hwDistributeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwDistributeName_Type.__name__ = "OctetString"
_HwDistributeName_Object = MibTableColumn
hwDistributeName = _HwDistributeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 3, 1, 2),
    _HwDistributeName_Type()
)
hwDistributeName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwDistributeName.setStatus("current")


class _HwMigrateSrcSlot_Type(OctetString):
    """Custom type hwMigrateSrcSlot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwMigrateSrcSlot_Type.__name__ = "OctetString"
_HwMigrateSrcSlot_Object = MibTableColumn
hwMigrateSrcSlot = _HwMigrateSrcSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 3, 1, 3),
    _HwMigrateSrcSlot_Type()
)
hwMigrateSrcSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMigrateSrcSlot.setStatus("current")


class _HwMigrateDestSlot_Type(OctetString):
    """Custom type hwMigrateDestSlot based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_HwMigrateDestSlot_Type.__name__ = "OctetString"
_HwMigrateDestSlot_Object = MibTableColumn
hwMigrateDestSlot = _HwMigrateDestSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 3, 1, 4),
    _HwMigrateDestSlot_Type()
)
hwMigrateDestSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMigrateDestSlot.setStatus("current")


class _HwMigrateReason_Type(Integer32):
    """Custom type hwMigrateReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cpuoverload", 2),
          ("memoryoverload", 1))
    )


_HwMigrateReason_Type.__name__ = "Integer32"
_HwMigrateReason_Object = MibTableColumn
hwMigrateReason = _HwMigrateReason_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 3, 1, 5),
    _HwMigrateReason_Type()
)
hwMigrateReason.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    hwMigrateReason.setStatus("current")
_HwPeerDistributeTraps_ObjectIdentity = ObjectIdentity
hwPeerDistributeTraps = _HwPeerDistributeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 9, 4)
)
_HwRpkiObjects_ObjectIdentity = ObjectIdentity
hwRpkiObjects = _HwRpkiObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11)
)
_HwRpkiSessions_ObjectIdentity = ObjectIdentity
hwRpkiSessions = _HwRpkiSessions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 1)
)
_HwRpkiSessionTable_Object = MibTable
hwRpkiSessionTable = _HwRpkiSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 1, 1)
)
if mibBuilder.loadTexts:
    hwRpkiSessionTable.setStatus("current")
_HwRpkiSessionEntry_Object = MibTableRow
hwRpkiSessionEntry = _HwRpkiSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 1, 1, 1)
)
hwRpkiSessionEntry.setIndexNames(
    (0, "HUAWEI-BGP-VPN-MIB", "hwRpkiSessionVrfName"),
    (0, "HUAWEI-BGP-VPN-MIB", "hwRpkiSessionType"),
    (0, "HUAWEI-BGP-VPN-MIB", "hwSessionIPAddr"),
)
if mibBuilder.loadTexts:
    hwRpkiSessionEntry.setStatus("current")
_HwRpkiSessionVrfName_Type = MplsL3VpnName
_HwRpkiSessionVrfName_Object = MibTableColumn
hwRpkiSessionVrfName = _HwRpkiSessionVrfName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 1, 1, 1, 1),
    _HwRpkiSessionVrfName_Type()
)
hwRpkiSessionVrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRpkiSessionVrfName.setStatus("current")
_HwRpkiSessionType_Type = InetAddressType
_HwRpkiSessionType_Object = MibTableColumn
hwRpkiSessionType = _HwRpkiSessionType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 1, 1, 1, 2),
    _HwRpkiSessionType_Type()
)
hwRpkiSessionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwRpkiSessionType.setStatus("current")
_HwSessionIPAddr_Type = InetAddress
_HwSessionIPAddr_Object = MibTableColumn
hwSessionIPAddr = _HwSessionIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 1, 1, 1, 3),
    _HwSessionIPAddr_Type()
)
hwSessionIPAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSessionIPAddr.setStatus("current")
_HwRpkiSessionRoaLimitNum_Type = Unsigned32
_HwRpkiSessionRoaLimitNum_Object = MibTableColumn
hwRpkiSessionRoaLimitNum = _HwRpkiSessionRoaLimitNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 1, 1, 1, 4),
    _HwRpkiSessionRoaLimitNum_Type()
)
hwRpkiSessionRoaLimitNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRpkiSessionRoaLimitNum.setStatus("current")
_HwRpkiTraps_ObjectIdentity = ObjectIdentity
hwRpkiTraps = _HwRpkiTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 2)
)
_HwRpkiConformance_ObjectIdentity = ObjectIdentity
hwRpkiConformance = _HwRpkiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 3)
)
_HwRpkiCompliances_ObjectIdentity = ObjectIdentity
hwRpkiCompliances = _HwRpkiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 3, 1)
)
_HwRpkiGroups_ObjectIdentity = ObjectIdentity
hwRpkiGroups = _HwRpkiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 3, 2)
)
hwBgpPeerAddrFamilyEntry.registerAugmentions(
    ("HUAWEI-BGP-VPN-MIB",
     "hwBgpPeerEntry")
)
hwBgpPeerEntry.setIndexNames(*hwBgpPeerAddrFamilyEntry.getIndexNames())
hwBgpPeerAddrFamilyEntry.registerAugmentions(
    ("HUAWEI-BGP-VPN-MIB",
     "hwBgpPeerRouteEntry")
)
hwBgpPeerRouteEntry.setIndexNames(*hwBgpPeerAddrFamilyEntry.getIndexNames())
hwBgpPeerAddrFamilyEntry.registerAugmentions(
    ("HUAWEI-BGP-VPN-MIB",
     "hwBgpPeerMessageEntry")
)
hwBgpPeerMessageEntry.setIndexNames(*hwBgpPeerAddrFamilyEntry.getIndexNames())
hwBgpPeerAddrFamilyEntry.registerAugmentions(
    ("HUAWEI-BGP-VPN-MIB",
     "hwBgpPeerConfigEntry")
)
hwBgpPeerConfigEntry.setIndexNames(*hwBgpPeerAddrFamilyEntry.getIndexNames())

# Managed Objects groups

hwBgpPeerAddrFamily = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 3, 2, 1)
)
hwBgpPeerAddrFamily.setObjects(
    ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerVrfName")
)
if mibBuilder.loadTexts:
    hwBgpPeerAddrFamily.setStatus("current")

hwBgpPeer = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 3, 2, 2)
)
hwBgpPeer.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerNegotiatedVersion"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerRemoteAs"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerRemoteAddr"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerState"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerFsmEstablishedCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerGRStatus"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerFsmEstablishedTime"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerLastError"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerUnAvaiReason"))
)
if mibBuilder.loadTexts:
    hwBgpPeer.setStatus("current")

hwBgpPeerRoute = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 3, 2, 3)
)
hwBgpPeerRoute.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerPrefixRcvCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerPrefixActiveCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerPrefixAdvCounter"))
)
if mibBuilder.loadTexts:
    hwBgpPeerRoute.setStatus("current")

hwBgpPeerMessage = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 3, 2, 4)
)
hwBgpPeerMessage.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerInTotalMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerOutTotalMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerInOpenMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerInUpdateMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerInNotificationMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerInKeepAliveMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerInRouteFreshMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerOutOpenMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerOutUpdateMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerOutNotificationMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerOutKeepAliveMsgCounter"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerOutRouteFreshMsgCounter"))
)
if mibBuilder.loadTexts:
    hwBgpPeerMessage.setStatus("current")

hwBgpPeerConfig = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 3, 2, 5)
)
hwBgpPeerConfig.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerConfigRouteLimitNum"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerConfigRouteLimitThreshold"))
)
if mibBuilder.loadTexts:
    hwBgpPeerConfig.setStatus("current")

hwBgpVpnTunnelGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 5, 2, 1)
)
hwBgpVpnTunnelGroup.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelDestAddr"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelType"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelSrcAddr"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelIsLoadBalance"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelLspIndex"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelLspOutLabel"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelLspNextHop"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelLspFec"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelLspFecPfxLen"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelOutIfName"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelLspOutIfName"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelLspIsBackup"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelTunnelName"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelSessionTunnelId"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnTunnelSignalProtocol"))
)
if mibBuilder.loadTexts:
    hwBgpVpnTunnelGroup.setStatus("current")

hwBgpVpnServiceIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 5, 2, 2)
)
hwBgpVpnServiceIdGroup.setObjects(
    ("HUAWEI-BGP-VPN-MIB", "hwBgpVpnServiceIdValue")
)
if mibBuilder.loadTexts:
    hwBgpVpnServiceIdGroup.setStatus("current")

hwTnl2VpnTrapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 7, 2, 1)
)
hwTnl2VpnTrapGroup.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwVpnId"),
        ("HUAWEI-BGP-VPN-MIB", "hwVpnPublicNextHop"),
        ("HUAWEI-BGP-VPN-MIB", "hwVpnTrapCkeyValue"),
        ("HUAWEI-BGP-VPN-MIB", "hwTunnelReachablityEvent"))
)
if mibBuilder.loadTexts:
    hwTnl2VpnTrapGroup.setStatus("current")

hwRpkiSession = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 3, 2, 1)
)
hwRpkiSession.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwRpkiSessionVrfName"),
        ("HUAWEI-BGP-VPN-MIB", "hwRpkiSessionType"),
        ("HUAWEI-BGP-VPN-MIB", "hwSessionIPAddr"),
        ("HUAWEI-BGP-VPN-MIB", "hwRpkiSessionRoaLimitNum"))
)
if mibBuilder.loadTexts:
    hwRpkiSession.setStatus("current")


# Notification objects

hwBgpPeerRouteNumThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 1)
)
hwBgpPeerRouteNumThresholdExceed.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerConfigRouteLimitNum"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerConfigRouteLimitThreshold"))
)
if mibBuilder.loadTexts:
    hwBgpPeerRouteNumThresholdExceed.setStatus(
        "current"
    )

hwBgpPeerRouteNumThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 2)
)
hwBgpPeerRouteNumThresholdClear.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerConfigRouteLimitNum"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerConfigRouteLimitThreshold"))
)
if mibBuilder.loadTexts:
    hwBgpPeerRouteNumThresholdClear.setStatus(
        "current"
    )

hwBgpPeerGRStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 3)
)
hwBgpPeerGRStatusChange.setObjects(
    ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerGRStatus")
)
if mibBuilder.loadTexts:
    hwBgpPeerGRStatusChange.setStatus(
        "current"
    )

hwBgpPeerUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 4)
)
hwBgpPeerUnavailable.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionLocalAddrType"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionLocalAddr"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionUnavailableType"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionLocalIfName"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionReason"))
)
if mibBuilder.loadTexts:
    hwBgpPeerUnavailable.setStatus(
        "current"
    )

hwBgpPeerAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 5)
)
hwBgpPeerAvailable.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionLocalAddrType"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionLocalAddr"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionUnavailableType"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionLocalIfName"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionReason"))
)
if mibBuilder.loadTexts:
    hwBgpPeerAvailable.setStatus(
        "current"
    )

hwBgpPeerRouteExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 6)
)
hwBgpPeerRouteExceed.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerConfigRouteLimitNum"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerConfigRouteLimitThreshold"))
)
if mibBuilder.loadTexts:
    hwBgpPeerRouteExceed.setStatus(
        "current"
    )

hwBgpPeerRouteExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 7)
)
hwBgpPeerRouteExceedClear.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerConfigRouteLimitNum"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerConfigRouteLimitThreshold"))
)
if mibBuilder.loadTexts:
    hwBgpPeerRouteExceedClear.setStatus(
        "current"
    )

hwL3vpnVrfRouteMidThreshCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 8)
)
hwL3vpnVrfRouteMidThreshCleared.setObjects(
      *(("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfPerfCurrNumRoutes"),
        ("MPLS-L3VPN-STD-MIB", "mplsL3VpnVrfConfMidRteThresh"))
)
if mibBuilder.loadTexts:
    hwL3vpnVrfRouteMidThreshCleared.setStatus(
        "current"
    )

hwBgpPeerEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 9)
)
hwBgpPeerEstablished.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerLastError"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerState"))
)
if mibBuilder.loadTexts:
    hwBgpPeerEstablished.setStatus(
        "current"
    )

hwBgpPeerBackwardTransition = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 10)
)
hwBgpPeerBackwardTransition.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerLastError"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerState"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerUnAvaiReason"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    hwBgpPeerBackwardTransition.setStatus(
        "current"
    )

hwBgpRouteThresholdExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 11)
)
hwBgpRouteThresholdExceed.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpRouteLimitindex"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpRouteCurNum"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpRouteThreshold"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpRouteMaxNum"))
)
if mibBuilder.loadTexts:
    hwBgpRouteThresholdExceed.setStatus(
        "current"
    )

hwBgpRouteThresholdClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 12)
)
hwBgpRouteThresholdClear.setObjects(
    ("HUAWEI-BGP-VPN-MIB", "hwBgpRouteLimitindex")
)
if mibBuilder.loadTexts:
    hwBgpRouteThresholdClear.setStatus(
        "current"
    )

hwBgpRouteMaxExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 13)
)
hwBgpRouteMaxExceed.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpRouteLimitindex"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpRouteMaxNum"))
)
if mibBuilder.loadTexts:
    hwBgpRouteMaxExceed.setStatus(
        "current"
    )

hwBgpRouteMaxClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 14)
)
hwBgpRouteMaxClear.setObjects(
    ("HUAWEI-BGP-VPN-MIB", "hwBgpRouteLimitindex")
)
if mibBuilder.loadTexts:
    hwBgpRouteMaxClear.setStatus(
        "current"
    )

hwBgpPeerSessionExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 15)
)
hwBgpPeerSessionExceed.setObjects(
    ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionMaxNum")
)
if mibBuilder.loadTexts:
    hwBgpPeerSessionExceed.setStatus(
        "current"
    )

hwBgpPeerSessionExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 1, 3, 16)
)
hwBgpPeerSessionExceedClear.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionMaxNum"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerSessionNum"))
)
if mibBuilder.loadTexts:
    hwBgpPeerSessionExceedClear.setStatus(
        "current"
    )

hwTnl2VpnTrapEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 8, 1)
)
hwTnl2VpnTrapEvent.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwVpnId"),
        ("HUAWEI-BGP-VPN-MIB", "hwVpnPublicNextHop"),
        ("HUAWEI-BGP-VPN-MIB", "hwVpnTrapCkeyValue"),
        ("HUAWEI-BGP-VPN-MIB", "hwTunnelReachablityEvent"))
)
if mibBuilder.loadTexts:
    hwTnl2VpnTrapEvent.setStatus(
        "current"
    )

hwRpkiSessionRoaExceed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 2, 1)
)
hwRpkiSessionRoaExceed.setObjects(
    ("HUAWEI-BGP-VPN-MIB", "hwRpkiSessionRoaLimitNum")
)
if mibBuilder.loadTexts:
    hwRpkiSessionRoaExceed.setStatus(
        "current"
    )

hwRpkiSessionRoaExceedClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 2, 2)
)
hwRpkiSessionRoaExceedClear.setObjects(
    ("HUAWEI-BGP-VPN-MIB", "hwRpkiSessionRoaLimitNum")
)
if mibBuilder.loadTexts:
    hwRpkiSessionRoaExceedClear.setStatus(
        "current"
    )


# Notifications groups

hwBgpTrap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 3, 2, 6)
)
hwBgpTrap.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwBgpPeerRouteNumThresholdExceed"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerRouteNumThresholdClear"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerGRStatusChange"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerEstablished"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerBackwardTransition"),
        ("HUAWEI-BGP-VPN-MIB", "hwL3vpnVrfRouteMidThreshCleared"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerUnavailable"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerRouteExceed"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerRouteExceedClear"),
        ("HUAWEI-BGP-VPN-MIB", "hwBgpPeerAvailable"))
)
if mibBuilder.loadTexts:
    hwBgpTrap.setStatus(
        "current"
    )

hwTnl2VpnTrapNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 7, 2, 2)
)
hwTnl2VpnTrapNotificationGroup.setObjects(
    ("HUAWEI-BGP-VPN-MIB", "hwTnl2VpnTrapEvent")
)
if mibBuilder.loadTexts:
    hwTnl2VpnTrapNotificationGroup.setStatus(
        "current"
    )

hwRpkiTrap = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 3, 2, 2)
)
hwRpkiTrap.setObjects(
      *(("HUAWEI-BGP-VPN-MIB", "hwRpkiSessionRoaExceed"),
        ("HUAWEI-BGP-VPN-MIB", "hwRpkiSessionRoaExceedClear"))
)
if mibBuilder.loadTexts:
    hwRpkiTrap.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwBgpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwBgpCompliance.setStatus(
        "current"
    )

hwBgpVpnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 5, 1, 1)
)
if mibBuilder.loadTexts:
    hwBgpVpnCompliance.setStatus(
        "current"
    )

hwTnl2VpnTrapCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 7, 1, 1)
)
if mibBuilder.loadTexts:
    hwTnl2VpnTrapCompliance.setStatus(
        "current"
    )

hwRpkiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 177, 11, 3, 1, 1)
)
if mibBuilder.loadTexts:
    hwRpkiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-BGP-VPN-MIB",
    **{"HWBgpAfi": HWBgpAfi,
       "HWBgpSafi": HWBgpSafi,
       "MplsL3VpnName": MplsL3VpnName,
       "hwBgpMIB": hwBgpMIB,
       "hwBgpObjects": hwBgpObjects,
       "hwBgpPeers": hwBgpPeers,
       "hwBgpPeerAddrFamilyTable": hwBgpPeerAddrFamilyTable,
       "hwBgpPeerAddrFamilyEntry": hwBgpPeerAddrFamilyEntry,
       "hwBgpPeerInstanceId": hwBgpPeerInstanceId,
       "hwBgpPeerAddrFamilyAfi": hwBgpPeerAddrFamilyAfi,
       "hwBgpPeerAddrFamilySafi": hwBgpPeerAddrFamilySafi,
       "hwBgpPeerType": hwBgpPeerType,
       "hwBgpPeerIPAddr": hwBgpPeerIPAddr,
       "hwBgpPeerVrfName": hwBgpPeerVrfName,
       "hwBgpPeerTable": hwBgpPeerTable,
       "hwBgpPeerEntry": hwBgpPeerEntry,
       "hwBgpPeerNegotiatedVersion": hwBgpPeerNegotiatedVersion,
       "hwBgpPeerRemoteAs": hwBgpPeerRemoteAs,
       "hwBgpPeerRemoteAddr": hwBgpPeerRemoteAddr,
       "hwBgpPeerState": hwBgpPeerState,
       "hwBgpPeerFsmEstablishedCounter": hwBgpPeerFsmEstablishedCounter,
       "hwBgpPeerFsmEstablishedTime": hwBgpPeerFsmEstablishedTime,
       "hwBgpPeerGRStatus": hwBgpPeerGRStatus,
       "hwBgpPeerLastError": hwBgpPeerLastError,
       "hwBgpPeerUnAvaiReason": hwBgpPeerUnAvaiReason,
       "hwBgpPeerRouteTable": hwBgpPeerRouteTable,
       "hwBgpPeerRouteEntry": hwBgpPeerRouteEntry,
       "hwBgpPeerPrefixRcvCounter": hwBgpPeerPrefixRcvCounter,
       "hwBgpPeerPrefixActiveCounter": hwBgpPeerPrefixActiveCounter,
       "hwBgpPeerPrefixAdvCounter": hwBgpPeerPrefixAdvCounter,
       "hwBgpPeerMessageTable": hwBgpPeerMessageTable,
       "hwBgpPeerMessageEntry": hwBgpPeerMessageEntry,
       "hwBgpPeerInTotalMsgCounter": hwBgpPeerInTotalMsgCounter,
       "hwBgpPeerOutTotalMsgCounter": hwBgpPeerOutTotalMsgCounter,
       "hwBgpPeerInOpenMsgCounter": hwBgpPeerInOpenMsgCounter,
       "hwBgpPeerInUpdateMsgCounter": hwBgpPeerInUpdateMsgCounter,
       "hwBgpPeerInNotificationMsgCounter": hwBgpPeerInNotificationMsgCounter,
       "hwBgpPeerInKeepAliveMsgCounter": hwBgpPeerInKeepAliveMsgCounter,
       "hwBgpPeerInRouteFreshMsgCounter": hwBgpPeerInRouteFreshMsgCounter,
       "hwBgpPeerOutOpenMsgCounter": hwBgpPeerOutOpenMsgCounter,
       "hwBgpPeerOutUpdateMsgCounter": hwBgpPeerOutUpdateMsgCounter,
       "hwBgpPeerOutNotificationMsgCounter": hwBgpPeerOutNotificationMsgCounter,
       "hwBgpPeerOutKeepAliveMsgCounter": hwBgpPeerOutKeepAliveMsgCounter,
       "hwBgpPeerOutRouteFreshMsgCounter": hwBgpPeerOutRouteFreshMsgCounter,
       "hwBgpPeerConfigTable": hwBgpPeerConfigTable,
       "hwBgpPeerConfigEntry": hwBgpPeerConfigEntry,
       "hwBgpPeerConfigRouteLimitNum": hwBgpPeerConfigRouteLimitNum,
       "hwBgpPeerConfigRouteLimitThreshold": hwBgpPeerConfigRouteLimitThreshold,
       "hwBgpPeerSessionTable": hwBgpPeerSessionTable,
       "hwBgpPeerSessionEntry": hwBgpPeerSessionEntry,
       "hwBgpPeerSessionVrfName": hwBgpPeerSessionVrfName,
       "hwBgpPeerSessionRemoteAddrType": hwBgpPeerSessionRemoteAddrType,
       "hwBgpPeerSessionRemoteAddr": hwBgpPeerSessionRemoteAddr,
       "hwBgpPeerSessionLocalAddrType": hwBgpPeerSessionLocalAddrType,
       "hwBgpPeerSessionLocalAddr": hwBgpPeerSessionLocalAddr,
       "hwBgpPeerSessionUnavailableType": hwBgpPeerSessionUnavailableType,
       "hwBgpPeerSessionLocalIfName": hwBgpPeerSessionLocalIfName,
       "hwBgpPeerSessionReason": hwBgpPeerSessionReason,
       "hwBgpRoute": hwBgpRoute,
       "hwBgpRouteLimitTable": hwBgpRouteLimitTable,
       "hwBgpRouteLimitindex": hwBgpRouteLimitindex,
       "hwBgpRouteCurNum": hwBgpRouteCurNum,
       "hwBgpRouteMaxNum": hwBgpRouteMaxNum,
       "hwBgpRouteThreshold": hwBgpRouteThreshold,
       "hwBgpTraps": hwBgpTraps,
       "hwBgpPeerRouteNumThresholdExceed": hwBgpPeerRouteNumThresholdExceed,
       "hwBgpPeerRouteNumThresholdClear": hwBgpPeerRouteNumThresholdClear,
       "hwBgpPeerGRStatusChange": hwBgpPeerGRStatusChange,
       "hwBgpPeerUnavailable": hwBgpPeerUnavailable,
       "hwBgpPeerAvailable": hwBgpPeerAvailable,
       "hwBgpPeerRouteExceed": hwBgpPeerRouteExceed,
       "hwBgpPeerRouteExceedClear": hwBgpPeerRouteExceedClear,
       "hwL3vpnVrfRouteMidThreshCleared": hwL3vpnVrfRouteMidThreshCleared,
       "hwBgpPeerEstablished": hwBgpPeerEstablished,
       "hwBgpPeerBackwardTransition": hwBgpPeerBackwardTransition,
       "hwBgpRouteThresholdExceed": hwBgpRouteThresholdExceed,
       "hwBgpRouteThresholdClear": hwBgpRouteThresholdClear,
       "hwBgpRouteMaxExceed": hwBgpRouteMaxExceed,
       "hwBgpRouteMaxClear": hwBgpRouteMaxClear,
       "hwBgpPeerSessionExceed": hwBgpPeerSessionExceed,
       "hwBgpPeerSessionExceedClear": hwBgpPeerSessionExceedClear,
       "hwBgpScalars": hwBgpScalars,
       "hwBgpPeerSessionNum": hwBgpPeerSessionNum,
       "hwIBgpPeerSessionNum": hwIBgpPeerSessionNum,
       "hwEBgpPeerSessionNum": hwEBgpPeerSessionNum,
       "hwBgpPeerSessionMaxNum": hwBgpPeerSessionMaxNum,
       "hwBgpVpnObjects": hwBgpVpnObjects,
       "hwBgpVpnTunnelTable": hwBgpVpnTunnelTable,
       "hwBgpVpnTunnelEntry": hwBgpVpnTunnelEntry,
       "hwBgpVpnTunnelVrfName": hwBgpVpnTunnelVrfName,
       "hwBgpVpnTunnelPublicNetNextHop": hwBgpVpnTunnelPublicNetNextHop,
       "hwBgpVpnTunnelId": hwBgpVpnTunnelId,
       "hwBgpVpnTunnelDestAddr": hwBgpVpnTunnelDestAddr,
       "hwBgpVpnTunnelType": hwBgpVpnTunnelType,
       "hwBgpVpnTunnelSrcAddr": hwBgpVpnTunnelSrcAddr,
       "hwBgpVpnTunnelOutIfName": hwBgpVpnTunnelOutIfName,
       "hwBgpVpnTunnelIsLoadBalance": hwBgpVpnTunnelIsLoadBalance,
       "hwBgpVpnTunnelLspIndex": hwBgpVpnTunnelLspIndex,
       "hwBgpVpnTunnelLspOutIfName": hwBgpVpnTunnelLspOutIfName,
       "hwBgpVpnTunnelLspOutLabel": hwBgpVpnTunnelLspOutLabel,
       "hwBgpVpnTunnelLspNextHop": hwBgpVpnTunnelLspNextHop,
       "hwBgpVpnTunnelLspFec": hwBgpVpnTunnelLspFec,
       "hwBgpVpnTunnelLspFecPfxLen": hwBgpVpnTunnelLspFecPfxLen,
       "hwBgpVpnTunnelLspIsBackup": hwBgpVpnTunnelLspIsBackup,
       "hwBgpVpnTunnelSignalProtocol": hwBgpVpnTunnelSignalProtocol,
       "hwBgpVpnTunnelSessionTunnelId": hwBgpVpnTunnelSessionTunnelId,
       "hwBgpVpnTunnelTunnelName": hwBgpVpnTunnelTunnelName,
       "hwBgpVpnServiceIdTable": hwBgpVpnServiceIdTable,
       "hwBgpVpnServiceIdEntry": hwBgpVpnServiceIdEntry,
       "hwBgpVpnServiceIdVrfName": hwBgpVpnServiceIdVrfName,
       "hwBgpVpnServiceIdValue": hwBgpVpnServiceIdValue,
       "hwBgpVpnScalars": hwBgpVpnScalars,
       "hwConfiguredVrfs": hwConfiguredVrfs,
       "hwConfiguredIpv4Vrfs": hwConfiguredIpv4Vrfs,
       "hwConfiguredIpv6Vrfs": hwConfiguredIpv6Vrfs,
       "hwBgpConformance": hwBgpConformance,
       "hwBgpCompliances": hwBgpCompliances,
       "hwBgpCompliance": hwBgpCompliance,
       "hwBgpGroups": hwBgpGroups,
       "hwBgpPeerAddrFamily": hwBgpPeerAddrFamily,
       "hwBgpPeer": hwBgpPeer,
       "hwBgpPeerRoute": hwBgpPeerRoute,
       "hwBgpPeerMessage": hwBgpPeerMessage,
       "hwBgpPeerConfig": hwBgpPeerConfig,
       "hwBgpTrap": hwBgpTrap,
       "hwBgpVpnConformance": hwBgpVpnConformance,
       "hwBgpVpnCompliances": hwBgpVpnCompliances,
       "hwBgpVpnCompliance": hwBgpVpnCompliance,
       "hwBgpVpnExtGroups": hwBgpVpnExtGroups,
       "hwBgpVpnTunnelGroup": hwBgpVpnTunnelGroup,
       "hwBgpVpnServiceIdGroup": hwBgpVpnServiceIdGroup,
       "hwTnl2VpnTrapObjects": hwTnl2VpnTrapObjects,
       "hwTnl2VpnTrapTable": hwTnl2VpnTrapTable,
       "hwTnl2VpnTrapEntry": hwTnl2VpnTrapEntry,
       "hwVpnId": hwVpnId,
       "hwVpnPublicNextHop": hwVpnPublicNextHop,
       "hwTunnelReachablityEvent": hwTunnelReachablityEvent,
       "hwVpnTrapCkeyValue": hwVpnTrapCkeyValue,
       "hwTnl2VpnTrapConformance": hwTnl2VpnTrapConformance,
       "hwTnl2VpnTrapConformances": hwTnl2VpnTrapConformances,
       "hwTnl2VpnTrapCompliance": hwTnl2VpnTrapCompliance,
       "hwTnl2VpnTrapGroups": hwTnl2VpnTrapGroups,
       "hwTnl2VpnTrapGroup": hwTnl2VpnTrapGroup,
       "hwTnl2VpnTrapNotificationGroup": hwTnl2VpnTrapNotificationGroup,
       "hwTnl2VpnTrapNotification": hwTnl2VpnTrapNotification,
       "hwTnl2VpnTrapEvent": hwTnl2VpnTrapEvent,
       "hwPeerDistributeObjects": hwPeerDistributeObjects,
       "hwBgpTotalRouteNumber": hwBgpTotalRouteNumber,
       "hwOsNodeTable": hwOsNodeTable,
       "hwOsNodeEntry": hwOsNodeEntry,
       "hwCurrSlot": hwCurrSlot,
       "hwPeerNumber": hwPeerNumber,
       "hwRouteNumber": hwRouteNumber,
       "hwDistributeTable": hwDistributeTable,
       "hwDistributeEntry": hwDistributeEntry,
       "hwDistributeLocId": hwDistributeLocId,
       "hwDistributeName": hwDistributeName,
       "hwMigrateSrcSlot": hwMigrateSrcSlot,
       "hwMigrateDestSlot": hwMigrateDestSlot,
       "hwMigrateReason": hwMigrateReason,
       "hwPeerDistributeTraps": hwPeerDistributeTraps,
       "hwRpkiObjects": hwRpkiObjects,
       "hwRpkiSessions": hwRpkiSessions,
       "hwRpkiSessionTable": hwRpkiSessionTable,
       "hwRpkiSessionEntry": hwRpkiSessionEntry,
       "hwRpkiSessionVrfName": hwRpkiSessionVrfName,
       "hwRpkiSessionType": hwRpkiSessionType,
       "hwSessionIPAddr": hwSessionIPAddr,
       "hwRpkiSessionRoaLimitNum": hwRpkiSessionRoaLimitNum,
       "hwRpkiTraps": hwRpkiTraps,
       "hwRpkiSessionRoaExceed": hwRpkiSessionRoaExceed,
       "hwRpkiSessionRoaExceedClear": hwRpkiSessionRoaExceedClear,
       "hwRpkiConformance": hwRpkiConformance,
       "hwRpkiCompliances": hwRpkiCompliances,
       "hwRpkiCompliance": hwRpkiCompliance,
       "hwRpkiGroups": hwRpkiGroups,
       "hwRpkiSession": hwRpkiSession,
       "hwRpkiTrap": hwRpkiTrap}
)
