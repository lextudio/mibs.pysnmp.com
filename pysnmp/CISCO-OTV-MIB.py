# SNMP MIB module (CISCO-OTV-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-OTV-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:06:34 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(Cisco2KVlanList,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "Cisco2KVlanList")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoOtvMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810)
)
ciscoOtvMIB.setRevisions(
        ("2013-08-05 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoOtvMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoOtvMIBNotifs = _CiscoOtvMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 0)
)
_CiscoOtvMIBObjects_ObjectIdentity = ObjectIdentity
ciscoOtvMIBObjects = _CiscoOtvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1)
)
_CotvGlobalObjects_ObjectIdentity = ObjectIdentity
cotvGlobalObjects = _CotvGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 1)
)
_CotvSiteObjects_ObjectIdentity = ObjectIdentity
cotvSiteObjects = _CotvSiteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 1, 1)
)


class _CotvSiteIdAdmin_Type(OctetString):
    """Custom type cotvSiteIdAdmin based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(6, 6),
    )


_CotvSiteIdAdmin_Type.__name__ = "OctetString"
_CotvSiteIdAdmin_Object = MibScalar
cotvSiteIdAdmin = _CotvSiteIdAdmin_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 1, 1, 1),
    _CotvSiteIdAdmin_Type()
)
cotvSiteIdAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cotvSiteIdAdmin.setStatus("current")


class _CotvSiteIdOper_Type(OctetString):
    """Custom type cotvSiteIdOper based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_CotvSiteIdOper_Type.__name__ = "OctetString"
_CotvSiteIdOper_Object = MibScalar
cotvSiteIdOper = _CotvSiteIdOper_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 1, 1, 2),
    _CotvSiteIdOper_Type()
)
cotvSiteIdOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvSiteIdOper.setStatus("current")
_CotvSiteVlan_Type = VlanIndex
_CotvSiteVlan_Object = MibScalar
cotvSiteVlan = _CotvSiteVlan_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 1, 1, 3),
    _CotvSiteVlan_Type()
)
cotvSiteVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cotvSiteVlan.setStatus("current")


class _CotvSiteVlanState_Type(Integer32):
    """Custom type cotvSiteVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )


_CotvSiteVlanState_Type.__name__ = "Integer32"
_CotvSiteVlanState_Object = MibScalar
cotvSiteVlanState = _CotvSiteVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 1, 1, 4),
    _CotvSiteVlanState_Type()
)
cotvSiteVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvSiteVlanState.setStatus("current")
_CotvGlobalStatsObjects_ObjectIdentity = ObjectIdentity
cotvGlobalStatsObjects = _CotvGlobalStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 1, 2)
)
_CotvOverlayObjects_ObjectIdentity = ObjectIdentity
cotvOverlayObjects = _CotvOverlayObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2)
)
_CotvOverlayTable_Object = MibTable
cotvOverlayTable = _CotvOverlayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cotvOverlayTable.setStatus("current")
_CotvOverlayEntry_Object = MibTableRow
cotvOverlayEntry = _CotvOverlayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1)
)
cotvOverlayEntry.setIndexNames(
    (0, "CISCO-OTV-MIB", "cotvOverlayNumber"),
)
if mibBuilder.loadTexts:
    cotvOverlayEntry.setStatus("current")
_CotvOverlayNumber_Type = Unsigned32
_CotvOverlayNumber_Object = MibTableColumn
cotvOverlayNumber = _CotvOverlayNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 1),
    _CotvOverlayNumber_Type()
)
cotvOverlayNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvOverlayNumber.setStatus("current")
_CotvOverlayVpnName_Type = SnmpAdminString
_CotvOverlayVpnName_Object = MibTableColumn
cotvOverlayVpnName = _CotvOverlayVpnName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 2),
    _CotvOverlayVpnName_Type()
)
cotvOverlayVpnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvOverlayVpnName.setStatus("current")


class _CotvOverlayVpnState_Type(Integer32):
    """Custom type cotvOverlayVpnState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("other", 0),
          ("up", 2))
    )


_CotvOverlayVpnState_Type.__name__ = "Integer32"
_CotvOverlayVpnState_Object = MibTableColumn
cotvOverlayVpnState = _CotvOverlayVpnState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 3),
    _CotvOverlayVpnState_Type()
)
cotvOverlayVpnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvOverlayVpnState.setStatus("current")


class _CotvOverlayVpnDownReason_Type(Integer32):
    """Custom type cotvOverlayVpnDownReason based on Integer32"""
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
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("adminDown", 8),
          ("changingControlGroup", 16),
          ("changingDeviceId", 18),
          ("changingSiteId", 15),
          ("cleanupInProgress", 19),
          ("configChange", 1),
          ("deleteHoldDown", 9),
          ("joinInterfaceDown", 7),
          ("missingControlGroup", 2),
          ("missingDataGroupRange", 3),
          ("missingDeviceId", 17),
          ("missingJoinInterfaceAddr", 6),
          ("missingJoinOrSourceInterface", 4),
          ("missingSiteId", 11),
          ("missingSourceInterfaceAddr", 13),
          ("missingVpnName", 5),
          ("other", 0),
          ("reinit", 10),
          ("siteIdMismatch", 12),
          ("sourceInterfaceDown", 14))
    )


_CotvOverlayVpnDownReason_Type.__name__ = "Integer32"
_CotvOverlayVpnDownReason_Object = MibTableColumn
cotvOverlayVpnDownReason = _CotvOverlayVpnDownReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 4),
    _CotvOverlayVpnDownReason_Type()
)
cotvOverlayVpnDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvOverlayVpnDownReason.setStatus("current")
_CotvOverlayVlansExtendedFirst2k_Type = Cisco2KVlanList
_CotvOverlayVlansExtendedFirst2k_Object = MibTableColumn
cotvOverlayVlansExtendedFirst2k = _CotvOverlayVlansExtendedFirst2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 5),
    _CotvOverlayVlansExtendedFirst2k_Type()
)
cotvOverlayVlansExtendedFirst2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayVlansExtendedFirst2k.setStatus("current")
_CotvOverlayVlansExtendedSecond2k_Type = Cisco2KVlanList
_CotvOverlayVlansExtendedSecond2k_Object = MibTableColumn
cotvOverlayVlansExtendedSecond2k = _CotvOverlayVlansExtendedSecond2k_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 6),
    _CotvOverlayVlansExtendedSecond2k_Type()
)
cotvOverlayVlansExtendedSecond2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayVlansExtendedSecond2k.setStatus("current")


class _CotvOverlayControlGroupAddrType_Type(InetAddressType):
    """Custom type cotvOverlayControlGroupAddrType based on InetAddressType"""


_CotvOverlayControlGroupAddrType_Object = MibTableColumn
cotvOverlayControlGroupAddrType = _CotvOverlayControlGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 7),
    _CotvOverlayControlGroupAddrType_Type()
)
cotvOverlayControlGroupAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayControlGroupAddrType.setStatus("current")
_CotvOverlayControlGroupAddr_Type = InetAddress
_CotvOverlayControlGroupAddr_Object = MibTableColumn
cotvOverlayControlGroupAddr = _CotvOverlayControlGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 8),
    _CotvOverlayControlGroupAddr_Type()
)
cotvOverlayControlGroupAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayControlGroupAddr.setStatus("current")


class _CotvOverlayBroadcastGroupAddrType_Type(InetAddressType):
    """Custom type cotvOverlayBroadcastGroupAddrType based on InetAddressType"""


_CotvOverlayBroadcastGroupAddrType_Object = MibTableColumn
cotvOverlayBroadcastGroupAddrType = _CotvOverlayBroadcastGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 9),
    _CotvOverlayBroadcastGroupAddrType_Type()
)
cotvOverlayBroadcastGroupAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayBroadcastGroupAddrType.setStatus("current")
_CotvOverlayBroadcastGroupAddr_Type = InetAddress
_CotvOverlayBroadcastGroupAddr_Object = MibTableColumn
cotvOverlayBroadcastGroupAddr = _CotvOverlayBroadcastGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 10),
    _CotvOverlayBroadcastGroupAddr_Type()
)
cotvOverlayBroadcastGroupAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayBroadcastGroupAddr.setStatus("current")


class _CotvOverlayJoinInterface_Type(InterfaceIndexOrZero):
    """Custom type cotvOverlayJoinInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_CotvOverlayJoinInterface_Object = MibTableColumn
cotvOverlayJoinInterface = _CotvOverlayJoinInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 11),
    _CotvOverlayJoinInterface_Type()
)
cotvOverlayJoinInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayJoinInterface.setStatus("current")


class _CotvOverlaySourceInterface_Type(InterfaceIndexOrZero):
    """Custom type cotvOverlaySourceInterface based on InterfaceIndexOrZero"""
    defaultValue = 0


_CotvOverlaySourceInterface_Object = MibTableColumn
cotvOverlaySourceInterface = _CotvOverlaySourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 12),
    _CotvOverlaySourceInterface_Type()
)
cotvOverlaySourceInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlaySourceInterface.setStatus("current")
_CotvOverlayAedCapable_Type = TruthValue
_CotvOverlayAedCapable_Object = MibTableColumn
cotvOverlayAedCapable = _CotvOverlayAedCapable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 13),
    _CotvOverlayAedCapable_Type()
)
cotvOverlayAedCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvOverlayAedCapable.setStatus("current")


class _CotvOverlayAedIncapableReason_Type(Integer32):
    """Custom type cotvOverlayAedIncapableReason based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("isisControlGroupSyncPending", 10),
          ("lspdbSyncIncomplete", 8),
          ("noExtendedVlanUp", 6),
          ("noOverlayAdjacencyUp", 7),
          ("other", 0),
          ("overlayDown", 1),
          ("overlayDownInProgress", 9),
          ("siteIdMismatch", 3),
          ("siteIdNotConfigured", 2),
          ("siteVlanDown", 5),
          ("versionMismatch", 4))
    )


_CotvOverlayAedIncapableReason_Type.__name__ = "Integer32"
_CotvOverlayAedIncapableReason_Object = MibTableColumn
cotvOverlayAedIncapableReason = _CotvOverlayAedIncapableReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 14),
    _CotvOverlayAedIncapableReason_Type()
)
cotvOverlayAedIncapableReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvOverlayAedIncapableReason.setStatus("current")


class _CotvOverlayAdjServerTransportType_Type(Integer32):
    """Custom type cotvOverlayAdjServerTransportType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("multicastAndUnicast", 1),
          ("unicastOnly", 2))
    )


_CotvOverlayAdjServerTransportType_Type.__name__ = "Integer32"
_CotvOverlayAdjServerTransportType_Object = MibTableColumn
cotvOverlayAdjServerTransportType = _CotvOverlayAdjServerTransportType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 15),
    _CotvOverlayAdjServerTransportType_Type()
)
cotvOverlayAdjServerTransportType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayAdjServerTransportType.setStatus("current")


class _CotvOverlayAdjServerEnable_Type(TruthValue):
    """Custom type cotvOverlayAdjServerEnable based on TruthValue"""


_CotvOverlayAdjServerEnable_Object = MibTableColumn
cotvOverlayAdjServerEnable = _CotvOverlayAdjServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 16),
    _CotvOverlayAdjServerEnable_Type()
)
cotvOverlayAdjServerEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayAdjServerEnable.setStatus("current")


class _CotvOverlayPrimaryAdjServerAddrType_Type(InetAddressType):
    """Custom type cotvOverlayPrimaryAdjServerAddrType based on InetAddressType"""


_CotvOverlayPrimaryAdjServerAddrType_Object = MibTableColumn
cotvOverlayPrimaryAdjServerAddrType = _CotvOverlayPrimaryAdjServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 17),
    _CotvOverlayPrimaryAdjServerAddrType_Type()
)
cotvOverlayPrimaryAdjServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayPrimaryAdjServerAddrType.setStatus("current")
_CotvOverlayPrimaryAdjServerAddr_Type = InetAddress
_CotvOverlayPrimaryAdjServerAddr_Object = MibTableColumn
cotvOverlayPrimaryAdjServerAddr = _CotvOverlayPrimaryAdjServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 18),
    _CotvOverlayPrimaryAdjServerAddr_Type()
)
cotvOverlayPrimaryAdjServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayPrimaryAdjServerAddr.setStatus("current")


class _CotvOverlaySecondaryAdjServerAddrType_Type(InetAddressType):
    """Custom type cotvOverlaySecondaryAdjServerAddrType based on InetAddressType"""


_CotvOverlaySecondaryAdjServerAddrType_Object = MibTableColumn
cotvOverlaySecondaryAdjServerAddrType = _CotvOverlaySecondaryAdjServerAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 19),
    _CotvOverlaySecondaryAdjServerAddrType_Type()
)
cotvOverlaySecondaryAdjServerAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlaySecondaryAdjServerAddrType.setStatus("current")
_CotvOverlaySecondaryAdjServerAddr_Type = InetAddress
_CotvOverlaySecondaryAdjServerAddr_Object = MibTableColumn
cotvOverlaySecondaryAdjServerAddr = _CotvOverlaySecondaryAdjServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 20),
    _CotvOverlaySecondaryAdjServerAddr_Type()
)
cotvOverlaySecondaryAdjServerAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlaySecondaryAdjServerAddr.setStatus("current")


class _CotvOverlaySuppressArpND_Type(TruthValue):
    """Custom type cotvOverlaySuppressArpND based on TruthValue"""


_CotvOverlaySuppressArpND_Object = MibTableColumn
cotvOverlaySuppressArpND = _CotvOverlaySuppressArpND_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 21),
    _CotvOverlaySuppressArpND_Type()
)
cotvOverlaySuppressArpND.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlaySuppressArpND.setStatus("current")


class _CotvOverlayStorageType_Type(StorageType):
    """Custom type cotvOverlayStorageType based on StorageType"""


_CotvOverlayStorageType_Object = MibTableColumn
cotvOverlayStorageType = _CotvOverlayStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 22),
    _CotvOverlayStorageType_Type()
)
cotvOverlayStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayStorageType.setStatus("current")
_CotvOverlayRowStatus_Type = RowStatus
_CotvOverlayRowStatus_Object = MibTableColumn
cotvOverlayRowStatus = _CotvOverlayRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 1, 1, 23),
    _CotvOverlayRowStatus_Type()
)
cotvOverlayRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvOverlayRowStatus.setStatus("current")
_CotvVlansTable_Object = MibTable
cotvVlansTable = _CotvVlansTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cotvVlansTable.setStatus("current")
_CotvVlansEntry_Object = MibTableRow
cotvVlansEntry = _CotvVlansEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 2, 1)
)
cotvVlansEntry.setIndexNames(
    (0, "CISCO-OTV-MIB", "cotvOverlayNumber"),
    (0, "CISCO-OTV-MIB", "cotvVlanId"),
)
if mibBuilder.loadTexts:
    cotvVlansEntry.setStatus("current")
_CotvVlanId_Type = VlanIndex
_CotvVlanId_Object = MibTableColumn
cotvVlanId = _CotvVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 2, 1, 1),
    _CotvVlanId_Type()
)
cotvVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvVlanId.setStatus("current")


class _CotvVlanState_Type(Integer32):
    """Custom type cotvVlanState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_CotvVlanState_Type.__name__ = "Integer32"
_CotvVlanState_Object = MibTableColumn
cotvVlanState = _CotvVlanState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 2, 1, 2),
    _CotvVlanState_Type()
)
cotvVlanState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvVlanState.setStatus("current")


class _CotvVlanInactiveReason_Type(Integer32):
    """Custom type cotvVlanInactiveReason based on Integer32"""
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
        *(("deleteHoldDown", 5),
          ("hwDown", 6),
          ("nonAed", 2),
          ("other", 1),
          ("overlayDown", 4),
          ("vlanDisabled", 3))
    )


_CotvVlanInactiveReason_Type.__name__ = "Integer32"
_CotvVlanInactiveReason_Object = MibTableColumn
cotvVlanInactiveReason = _CotvVlanInactiveReason_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 2, 1, 3),
    _CotvVlanInactiveReason_Type()
)
cotvVlanInactiveReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvVlanInactiveReason.setStatus("current")
_CotvVlanAedAddrType_Type = InetAddressType
_CotvVlanAedAddrType_Object = MibTableColumn
cotvVlanAedAddrType = _CotvVlanAedAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 2, 1, 4),
    _CotvVlanAedAddrType_Type()
)
cotvVlanAedAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvVlanAedAddrType.setStatus("current")
_CotvVlanAedAddr_Type = InetAddress
_CotvVlanAedAddr_Object = MibTableColumn
cotvVlanAedAddr = _CotvVlanAedAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 2, 1, 5),
    _CotvVlanAedAddr_Type()
)
cotvVlanAedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvVlanAedAddr.setStatus("current")
_CotvVlanEdgeDevIsAed_Type = TruthValue
_CotvVlanEdgeDevIsAed_Object = MibTableColumn
cotvVlanEdgeDevIsAed = _CotvVlanEdgeDevIsAed_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 2, 1, 6),
    _CotvVlanEdgeDevIsAed_Type()
)
cotvVlanEdgeDevIsAed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvVlanEdgeDevIsAed.setStatus("current")
_CotvDataGroupConfigTable_Object = MibTable
cotvDataGroupConfigTable = _CotvDataGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 3)
)
if mibBuilder.loadTexts:
    cotvDataGroupConfigTable.setStatus("current")
_CotvDataGroupConfigEntry_Object = MibTableRow
cotvDataGroupConfigEntry = _CotvDataGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 3, 1)
)
cotvDataGroupConfigEntry.setIndexNames(
    (0, "CISCO-OTV-MIB", "cotvOverlayNumber"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupMcastRangeAddrType"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupMcastRangeAddr"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupMcastRangePrefixLength"),
)
if mibBuilder.loadTexts:
    cotvDataGroupConfigEntry.setStatus("current")
_CotvDataGroupMcastRangeAddrType_Type = InetAddressType
_CotvDataGroupMcastRangeAddrType_Object = MibTableColumn
cotvDataGroupMcastRangeAddrType = _CotvDataGroupMcastRangeAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 3, 1, 1),
    _CotvDataGroupMcastRangeAddrType_Type()
)
cotvDataGroupMcastRangeAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupMcastRangeAddrType.setStatus("current")


class _CotvDataGroupMcastRangeAddr_Type(InetAddress):
    """Custom type cotvDataGroupMcastRangeAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CotvDataGroupMcastRangeAddr_Type.__name__ = "InetAddress"
_CotvDataGroupMcastRangeAddr_Object = MibTableColumn
cotvDataGroupMcastRangeAddr = _CotvDataGroupMcastRangeAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 3, 1, 2),
    _CotvDataGroupMcastRangeAddr_Type()
)
cotvDataGroupMcastRangeAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupMcastRangeAddr.setStatus("current")
_CotvDataGroupMcastRangePrefixLength_Type = InetAddressPrefixLength
_CotvDataGroupMcastRangePrefixLength_Object = MibTableColumn
cotvDataGroupMcastRangePrefixLength = _CotvDataGroupMcastRangePrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 3, 1, 3),
    _CotvDataGroupMcastRangePrefixLength_Type()
)
cotvDataGroupMcastRangePrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupMcastRangePrefixLength.setStatus("current")


class _CotvDataGroupStorageType_Type(StorageType):
    """Custom type cotvDataGroupStorageType based on StorageType"""


_CotvDataGroupStorageType_Object = MibTableColumn
cotvDataGroupStorageType = _CotvDataGroupStorageType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 3, 1, 4),
    _CotvDataGroupStorageType_Type()
)
cotvDataGroupStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvDataGroupStorageType.setStatus("current")
_CotvDataGroupRowStatus_Type = RowStatus
_CotvDataGroupRowStatus_Object = MibTableColumn
cotvDataGroupRowStatus = _CotvDataGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 3, 1, 5),
    _CotvDataGroupRowStatus_Type()
)
cotvDataGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cotvDataGroupRowStatus.setStatus("current")
_CotvDataGroupInfoTable_Object = MibTable
cotvDataGroupInfoTable = _CotvDataGroupInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4)
)
if mibBuilder.loadTexts:
    cotvDataGroupInfoTable.setStatus("current")
_CotvDataGroupInfoEntry_Object = MibTableRow
cotvDataGroupInfoEntry = _CotvDataGroupInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1)
)
cotvDataGroupInfoEntry.setIndexNames(
    (0, "CISCO-OTV-MIB", "cotvOverlayNumber"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupActiveSrcLocation"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupVlanId"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupActiveGroupAddrType"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupActiveGroupAddr"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupActiveSrcAddrType"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupActiveSrcAddr"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupDeliveryGroupAddrType"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupDeliveryGroupAddr"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupDeliverySrcAddrType"),
    (0, "CISCO-OTV-MIB", "cotvDataGroupDeliverySrcAddr"),
)
if mibBuilder.loadTexts:
    cotvDataGroupInfoEntry.setStatus("current")


class _CotvDataGroupActiveSrcLocation_Type(Integer32):
    """Custom type cotvDataGroupActiveSrcLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("remote", 2))
    )


_CotvDataGroupActiveSrcLocation_Type.__name__ = "Integer32"
_CotvDataGroupActiveSrcLocation_Object = MibTableColumn
cotvDataGroupActiveSrcLocation = _CotvDataGroupActiveSrcLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 1),
    _CotvDataGroupActiveSrcLocation_Type()
)
cotvDataGroupActiveSrcLocation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupActiveSrcLocation.setStatus("current")
_CotvDataGroupVlanId_Type = VlanIndex
_CotvDataGroupVlanId_Object = MibTableColumn
cotvDataGroupVlanId = _CotvDataGroupVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 2),
    _CotvDataGroupVlanId_Type()
)
cotvDataGroupVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupVlanId.setStatus("current")
_CotvDataGroupActiveGroupAddrType_Type = InetAddressType
_CotvDataGroupActiveGroupAddrType_Object = MibTableColumn
cotvDataGroupActiveGroupAddrType = _CotvDataGroupActiveGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 3),
    _CotvDataGroupActiveGroupAddrType_Type()
)
cotvDataGroupActiveGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupActiveGroupAddrType.setStatus("current")


class _CotvDataGroupActiveGroupAddr_Type(InetAddress):
    """Custom type cotvDataGroupActiveGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CotvDataGroupActiveGroupAddr_Type.__name__ = "InetAddress"
_CotvDataGroupActiveGroupAddr_Object = MibTableColumn
cotvDataGroupActiveGroupAddr = _CotvDataGroupActiveGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 4),
    _CotvDataGroupActiveGroupAddr_Type()
)
cotvDataGroupActiveGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupActiveGroupAddr.setStatus("current")
_CotvDataGroupActiveSrcAddrType_Type = InetAddressType
_CotvDataGroupActiveSrcAddrType_Object = MibTableColumn
cotvDataGroupActiveSrcAddrType = _CotvDataGroupActiveSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 5),
    _CotvDataGroupActiveSrcAddrType_Type()
)
cotvDataGroupActiveSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupActiveSrcAddrType.setStatus("current")


class _CotvDataGroupActiveSrcAddr_Type(InetAddress):
    """Custom type cotvDataGroupActiveSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CotvDataGroupActiveSrcAddr_Type.__name__ = "InetAddress"
_CotvDataGroupActiveSrcAddr_Object = MibTableColumn
cotvDataGroupActiveSrcAddr = _CotvDataGroupActiveSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 6),
    _CotvDataGroupActiveSrcAddr_Type()
)
cotvDataGroupActiveSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupActiveSrcAddr.setStatus("current")
_CotvDataGroupDeliveryGroupAddrType_Type = InetAddressType
_CotvDataGroupDeliveryGroupAddrType_Object = MibTableColumn
cotvDataGroupDeliveryGroupAddrType = _CotvDataGroupDeliveryGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 7),
    _CotvDataGroupDeliveryGroupAddrType_Type()
)
cotvDataGroupDeliveryGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupDeliveryGroupAddrType.setStatus("current")


class _CotvDataGroupDeliveryGroupAddr_Type(InetAddress):
    """Custom type cotvDataGroupDeliveryGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CotvDataGroupDeliveryGroupAddr_Type.__name__ = "InetAddress"
_CotvDataGroupDeliveryGroupAddr_Object = MibTableColumn
cotvDataGroupDeliveryGroupAddr = _CotvDataGroupDeliveryGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 8),
    _CotvDataGroupDeliveryGroupAddr_Type()
)
cotvDataGroupDeliveryGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupDeliveryGroupAddr.setStatus("current")
_CotvDataGroupDeliverySrcAddrType_Type = InetAddressType
_CotvDataGroupDeliverySrcAddrType_Object = MibTableColumn
cotvDataGroupDeliverySrcAddrType = _CotvDataGroupDeliverySrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 9),
    _CotvDataGroupDeliverySrcAddrType_Type()
)
cotvDataGroupDeliverySrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupDeliverySrcAddrType.setStatus("current")


class _CotvDataGroupDeliverySrcAddr_Type(InetAddress):
    """Custom type cotvDataGroupDeliverySrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CotvDataGroupDeliverySrcAddr_Type.__name__ = "InetAddress"
_CotvDataGroupDeliverySrcAddr_Object = MibTableColumn
cotvDataGroupDeliverySrcAddr = _CotvDataGroupDeliverySrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 10),
    _CotvDataGroupDeliverySrcAddr_Type()
)
cotvDataGroupDeliverySrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvDataGroupDeliverySrcAddr.setStatus("current")
_CotvDataGroupJoinInterface_Type = InterfaceIndexOrZero
_CotvDataGroupJoinInterface_Object = MibTableColumn
cotvDataGroupJoinInterface = _CotvDataGroupJoinInterface_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 11),
    _CotvDataGroupJoinInterface_Type()
)
cotvDataGroupJoinInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvDataGroupJoinInterface.setStatus("current")


class _CotvDataGroupLocalActiveSrcState_Type(Integer32):
    """Custom type cotvDataGroupLocalActiveSrcState based on Integer32"""
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
        *(("local", 2),
          ("none", 1),
          ("orphan", 4),
          ("remote", 3))
    )


_CotvDataGroupLocalActiveSrcState_Type.__name__ = "Integer32"
_CotvDataGroupLocalActiveSrcState_Object = MibTableColumn
cotvDataGroupLocalActiveSrcState = _CotvDataGroupLocalActiveSrcState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 2, 4, 1, 12),
    _CotvDataGroupLocalActiveSrcState_Type()
)
cotvDataGroupLocalActiveSrcState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvDataGroupLocalActiveSrcState.setStatus("current")
_CotvAdjacencyObjects_ObjectIdentity = ObjectIdentity
cotvAdjacencyObjects = _CotvAdjacencyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 3)
)
_CotvAdjacencyDatabaseTable_Object = MibTable
cotvAdjacencyDatabaseTable = _CotvAdjacencyDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 3, 1)
)
if mibBuilder.loadTexts:
    cotvAdjacencyDatabaseTable.setStatus("current")
_CotvAdjacencyDatabaseEntry_Object = MibTableRow
cotvAdjacencyDatabaseEntry = _CotvAdjacencyDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 3, 1, 1)
)
cotvAdjacencyDatabaseEntry.setIndexNames(
    (0, "CISCO-OTV-MIB", "cotvOverlayNumber"),
    (0, "CISCO-OTV-MIB", "cotvAdjacentDevAddrType"),
    (0, "CISCO-OTV-MIB", "cotvAdjacentDevAddr"),
)
if mibBuilder.loadTexts:
    cotvAdjacencyDatabaseEntry.setStatus("current")
_CotvAdjacentDevAddrType_Type = InetAddressType
_CotvAdjacentDevAddrType_Object = MibTableColumn
cotvAdjacentDevAddrType = _CotvAdjacentDevAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 3, 1, 1, 1),
    _CotvAdjacentDevAddrType_Type()
)
cotvAdjacentDevAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvAdjacentDevAddrType.setStatus("current")


class _CotvAdjacentDevAddr_Type(InetAddress):
    """Custom type cotvAdjacentDevAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_CotvAdjacentDevAddr_Type.__name__ = "InetAddress"
_CotvAdjacentDevAddr_Object = MibTableColumn
cotvAdjacentDevAddr = _CotvAdjacentDevAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 3, 1, 1, 2),
    _CotvAdjacentDevAddr_Type()
)
cotvAdjacentDevAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvAdjacentDevAddr.setStatus("current")


class _CotvAdjacentDevSystemID_Type(OctetString):
    """Custom type cotvAdjacentDevSystemID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(6, 6),
    )


_CotvAdjacentDevSystemID_Type.__name__ = "OctetString"
_CotvAdjacentDevSystemID_Object = MibTableColumn
cotvAdjacentDevSystemID = _CotvAdjacentDevSystemID_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 3, 1, 1, 3),
    _CotvAdjacentDevSystemID_Type()
)
cotvAdjacentDevSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvAdjacentDevSystemID.setStatus("current")
_CotvAdjacentDevName_Type = SnmpAdminString
_CotvAdjacentDevName_Object = MibTableColumn
cotvAdjacentDevName = _CotvAdjacentDevName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 3, 1, 1, 4),
    _CotvAdjacentDevName_Type()
)
cotvAdjacentDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvAdjacentDevName.setStatus("current")


class _CotvAdjacentDevState_Type(Integer32):
    """Custom type cotvAdjacentDevState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("other", 0),
          ("up", 1))
    )


_CotvAdjacentDevState_Type.__name__ = "Integer32"
_CotvAdjacentDevState_Object = MibTableColumn
cotvAdjacentDevState = _CotvAdjacentDevState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 3, 1, 1, 5),
    _CotvAdjacentDevState_Type()
)
cotvAdjacentDevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvAdjacentDevState.setStatus("current")
_CotvAdjacentDevUpTime_Type = Unsigned32
_CotvAdjacentDevUpTime_Object = MibTableColumn
cotvAdjacentDevUpTime = _CotvAdjacentDevUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 3, 1, 1, 6),
    _CotvAdjacentDevUpTime_Type()
)
cotvAdjacentDevUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvAdjacentDevUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cotvAdjacentDevUpTime.setUnits("seconds")
_CotvArpNdObjects_ObjectIdentity = ObjectIdentity
cotvArpNdObjects = _CotvArpNdObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 4)
)
_CotvArpNdCacheTable_Object = MibTable
cotvArpNdCacheTable = _CotvArpNdCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 4, 1)
)
if mibBuilder.loadTexts:
    cotvArpNdCacheTable.setStatus("current")
_CotvArpNdCacheEntry_Object = MibTableRow
cotvArpNdCacheEntry = _CotvArpNdCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 4, 1, 1)
)
cotvArpNdCacheEntry.setIndexNames(
    (0, "CISCO-OTV-MIB", "cotvOverlayNumber"),
    (0, "CISCO-OTV-MIB", "cotvVlanId"),
    (0, "CISCO-OTV-MIB", "cotvArpNdCacheL3AddrType"),
    (0, "CISCO-OTV-MIB", "cotvArpNdCacheL3Addr"),
)
if mibBuilder.loadTexts:
    cotvArpNdCacheEntry.setStatus("current")
_CotvArpNdCacheL3AddrType_Type = InetAddressType
_CotvArpNdCacheL3AddrType_Object = MibTableColumn
cotvArpNdCacheL3AddrType = _CotvArpNdCacheL3AddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 4, 1, 1, 1),
    _CotvArpNdCacheL3AddrType_Type()
)
cotvArpNdCacheL3AddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvArpNdCacheL3AddrType.setStatus("current")


class _CotvArpNdCacheL3Addr_Type(InetAddress):
    """Custom type cotvArpNdCacheL3Addr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_CotvArpNdCacheL3Addr_Type.__name__ = "InetAddress"
_CotvArpNdCacheL3Addr_Object = MibTableColumn
cotvArpNdCacheL3Addr = _CotvArpNdCacheL3Addr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 4, 1, 1, 2),
    _CotvArpNdCacheL3Addr_Type()
)
cotvArpNdCacheL3Addr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvArpNdCacheL3Addr.setStatus("current")
_CotvArpNdCacheMacAddr_Type = MacAddress
_CotvArpNdCacheMacAddr_Object = MibTableColumn
cotvArpNdCacheMacAddr = _CotvArpNdCacheMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 4, 1, 1, 3),
    _CotvArpNdCacheMacAddr_Type()
)
cotvArpNdCacheMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvArpNdCacheMacAddr.setStatus("current")
_CotvArpNdCacheAge_Type = Unsigned32
_CotvArpNdCacheAge_Object = MibTableColumn
cotvArpNdCacheAge = _CotvArpNdCacheAge_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 4, 1, 1, 4),
    _CotvArpNdCacheAge_Type()
)
cotvArpNdCacheAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvArpNdCacheAge.setStatus("current")
if mibBuilder.loadTexts:
    cotvArpNdCacheAge.setUnits("seconds")
_CotvArpNdCacheTimeToExpire_Type = Unsigned32
_CotvArpNdCacheTimeToExpire_Object = MibTableColumn
cotvArpNdCacheTimeToExpire = _CotvArpNdCacheTimeToExpire_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 4, 1, 1, 5),
    _CotvArpNdCacheTimeToExpire_Type()
)
cotvArpNdCacheTimeToExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvArpNdCacheTimeToExpire.setStatus("current")
if mibBuilder.loadTexts:
    cotvArpNdCacheTimeToExpire.setUnits("seconds")
_CotvRouteObjects_ObjectIdentity = ObjectIdentity
cotvRouteObjects = _CotvRouteObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5)
)
_CotvRouteTable_Object = MibTable
cotvRouteTable = _CotvRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 1)
)
if mibBuilder.loadTexts:
    cotvRouteTable.setStatus("current")
_CotvRouteEntry_Object = MibTableRow
cotvRouteEntry = _CotvRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 1, 1)
)
cotvRouteEntry.setIndexNames(
    (0, "CISCO-OTV-MIB", "cotvRouteVlanId"),
    (0, "CISCO-OTV-MIB", "cotvRouteMacAddr"),
)
if mibBuilder.loadTexts:
    cotvRouteEntry.setStatus("current")
_CotvRouteVlanId_Type = VlanIndex
_CotvRouteVlanId_Object = MibTableColumn
cotvRouteVlanId = _CotvRouteVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 1, 1, 1),
    _CotvRouteVlanId_Type()
)
cotvRouteVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvRouteVlanId.setStatus("current")
_CotvRouteMacAddr_Type = MacAddress
_CotvRouteMacAddr_Object = MibTableColumn
cotvRouteMacAddr = _CotvRouteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 1, 1, 2),
    _CotvRouteMacAddr_Type()
)
cotvRouteMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvRouteMacAddr.setStatus("current")
_CotvRouteMetric_Type = Unsigned32
_CotvRouteMetric_Object = MibTableColumn
cotvRouteMetric = _CotvRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 1, 1, 3),
    _CotvRouteMetric_Type()
)
cotvRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvRouteMetric.setStatus("current")
_CotvRouteUpTime_Type = Unsigned32
_CotvRouteUpTime_Object = MibTableColumn
cotvRouteUpTime = _CotvRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 1, 1, 4),
    _CotvRouteUpTime_Type()
)
cotvRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvRouteUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cotvRouteUpTime.setUnits("seconds")
_CotvRouteOwner_Type = SnmpAdminString
_CotvRouteOwner_Object = MibTableColumn
cotvRouteOwner = _CotvRouteOwner_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 1, 1, 5),
    _CotvRouteOwner_Type()
)
cotvRouteOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvRouteOwner.setStatus("current")
_CotvRouteNextHopIf_Type = InterfaceIndexOrZero
_CotvRouteNextHopIf_Object = MibTableColumn
cotvRouteNextHopIf = _CotvRouteNextHopIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 1, 1, 6),
    _CotvRouteNextHopIf_Type()
)
cotvRouteNextHopIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvRouteNextHopIf.setStatus("current")
_CotvRouteNextHopAddrType_Type = InetAddressType
_CotvRouteNextHopAddrType_Object = MibTableColumn
cotvRouteNextHopAddrType = _CotvRouteNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 1, 1, 7),
    _CotvRouteNextHopAddrType_Type()
)
cotvRouteNextHopAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvRouteNextHopAddrType.setStatus("current")
_CotvRouteNextHopAddr_Type = InetAddress
_CotvRouteNextHopAddr_Object = MibTableColumn
cotvRouteNextHopAddr = _CotvRouteNextHopAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 1, 1, 8),
    _CotvRouteNextHopAddr_Type()
)
cotvRouteNextHopAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvRouteNextHopAddr.setStatus("current")
_CotvMcastRouteTable_Object = MibTable
cotvMcastRouteTable = _CotvMcastRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 2)
)
if mibBuilder.loadTexts:
    cotvMcastRouteTable.setStatus("current")
_CotvMcastRouteEntry_Object = MibTableRow
cotvMcastRouteEntry = _CotvMcastRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 2, 1)
)
cotvMcastRouteEntry.setIndexNames(
    (0, "CISCO-OTV-MIB", "cotvMcastRouteVlanId"),
    (0, "CISCO-OTV-MIB", "cotvMcastRouteActiveSrcAddrType"),
    (0, "CISCO-OTV-MIB", "cotvMcastRouteActiveSrcAddr"),
    (0, "CISCO-OTV-MIB", "cotvMcastRouteActiveGroupAddrType"),
    (0, "CISCO-OTV-MIB", "cotvMcastRouteActiveGroupAddr"),
)
if mibBuilder.loadTexts:
    cotvMcastRouteEntry.setStatus("current")
_CotvMcastRouteVlanId_Type = VlanIndex
_CotvMcastRouteVlanId_Object = MibTableColumn
cotvMcastRouteVlanId = _CotvMcastRouteVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 2, 1, 1),
    _CotvMcastRouteVlanId_Type()
)
cotvMcastRouteVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteVlanId.setStatus("current")
_CotvMcastRouteActiveSrcAddrType_Type = InetAddressType
_CotvMcastRouteActiveSrcAddrType_Object = MibTableColumn
cotvMcastRouteActiveSrcAddrType = _CotvMcastRouteActiveSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 2, 1, 2),
    _CotvMcastRouteActiveSrcAddrType_Type()
)
cotvMcastRouteActiveSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteActiveSrcAddrType.setStatus("current")


class _CotvMcastRouteActiveSrcAddr_Type(InetAddress):
    """Custom type cotvMcastRouteActiveSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CotvMcastRouteActiveSrcAddr_Type.__name__ = "InetAddress"
_CotvMcastRouteActiveSrcAddr_Object = MibTableColumn
cotvMcastRouteActiveSrcAddr = _CotvMcastRouteActiveSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 2, 1, 3),
    _CotvMcastRouteActiveSrcAddr_Type()
)
cotvMcastRouteActiveSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteActiveSrcAddr.setStatus("current")
_CotvMcastRouteActiveGroupAddrType_Type = InetAddressType
_CotvMcastRouteActiveGroupAddrType_Object = MibTableColumn
cotvMcastRouteActiveGroupAddrType = _CotvMcastRouteActiveGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 2, 1, 4),
    _CotvMcastRouteActiveGroupAddrType_Type()
)
cotvMcastRouteActiveGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteActiveGroupAddrType.setStatus("current")


class _CotvMcastRouteActiveGroupAddr_Type(InetAddress):
    """Custom type cotvMcastRouteActiveGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CotvMcastRouteActiveGroupAddr_Type.__name__ = "InetAddress"
_CotvMcastRouteActiveGroupAddr_Object = MibTableColumn
cotvMcastRouteActiveGroupAddr = _CotvMcastRouteActiveGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 2, 1, 5),
    _CotvMcastRouteActiveGroupAddr_Type()
)
cotvMcastRouteActiveGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteActiveGroupAddr.setStatus("current")
_CotvMcastRouteOwners_Type = SnmpAdminString
_CotvMcastRouteOwners_Object = MibTableColumn
cotvMcastRouteOwners = _CotvMcastRouteOwners_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 2, 1, 6),
    _CotvMcastRouteOwners_Type()
)
cotvMcastRouteOwners.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvMcastRouteOwners.setStatus("current")
_CotvMcastRouteMetric_Type = Unsigned32
_CotvMcastRouteMetric_Object = MibTableColumn
cotvMcastRouteMetric = _CotvMcastRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 2, 1, 7),
    _CotvMcastRouteMetric_Type()
)
cotvMcastRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvMcastRouteMetric.setStatus("current")
_CotvMcastRouteUpTime_Type = Unsigned32
_CotvMcastRouteUpTime_Object = MibTableColumn
cotvMcastRouteUpTime = _CotvMcastRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 2, 1, 8),
    _CotvMcastRouteUpTime_Type()
)
cotvMcastRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvMcastRouteUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cotvMcastRouteUpTime.setUnits("seconds")
_CotvMcastRouteInfoTable_Object = MibTable
cotvMcastRouteInfoTable = _CotvMcastRouteInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3)
)
if mibBuilder.loadTexts:
    cotvMcastRouteInfoTable.setStatus("current")
_CotvMcastRouteInfoEntry_Object = MibTableRow
cotvMcastRouteInfoEntry = _CotvMcastRouteInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1)
)
cotvMcastRouteInfoEntry.setIndexNames(
    (0, "CISCO-OTV-MIB", "cotvMcastRouteInfoVlanId"),
    (0, "CISCO-OTV-MIB", "cotvMcastRouteInfoActiveSrcAddrType"),
    (0, "CISCO-OTV-MIB", "cotvMcastRouteInfoActiveSrcAddr"),
    (0, "CISCO-OTV-MIB", "cotvMcastRouteInfoActiveGroupAddrType"),
    (0, "CISCO-OTV-MIB", "cotvMcastRouteInfoActiveGroupAddr"),
    (0, "CISCO-OTV-MIB", "cotvMcastRouteInfoIf"),
)
if mibBuilder.loadTexts:
    cotvMcastRouteInfoEntry.setStatus("current")
_CotvMcastRouteInfoVlanId_Type = VlanIndex
_CotvMcastRouteInfoVlanId_Object = MibTableColumn
cotvMcastRouteInfoVlanId = _CotvMcastRouteInfoVlanId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 1),
    _CotvMcastRouteInfoVlanId_Type()
)
cotvMcastRouteInfoVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoVlanId.setStatus("current")
_CotvMcastRouteInfoActiveSrcAddrType_Type = InetAddressType
_CotvMcastRouteInfoActiveSrcAddrType_Object = MibTableColumn
cotvMcastRouteInfoActiveSrcAddrType = _CotvMcastRouteInfoActiveSrcAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 2),
    _CotvMcastRouteInfoActiveSrcAddrType_Type()
)
cotvMcastRouteInfoActiveSrcAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoActiveSrcAddrType.setStatus("current")


class _CotvMcastRouteInfoActiveSrcAddr_Type(InetAddress):
    """Custom type cotvMcastRouteInfoActiveSrcAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CotvMcastRouteInfoActiveSrcAddr_Type.__name__ = "InetAddress"
_CotvMcastRouteInfoActiveSrcAddr_Object = MibTableColumn
cotvMcastRouteInfoActiveSrcAddr = _CotvMcastRouteInfoActiveSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 3),
    _CotvMcastRouteInfoActiveSrcAddr_Type()
)
cotvMcastRouteInfoActiveSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoActiveSrcAddr.setStatus("current")
_CotvMcastRouteInfoActiveGroupAddrType_Type = InetAddressType
_CotvMcastRouteInfoActiveGroupAddrType_Object = MibTableColumn
cotvMcastRouteInfoActiveGroupAddrType = _CotvMcastRouteInfoActiveGroupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 4),
    _CotvMcastRouteInfoActiveGroupAddrType_Type()
)
cotvMcastRouteInfoActiveGroupAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoActiveGroupAddrType.setStatus("current")


class _CotvMcastRouteInfoActiveGroupAddr_Type(InetAddress):
    """Custom type cotvMcastRouteInfoActiveGroupAddr based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_CotvMcastRouteInfoActiveGroupAddr_Type.__name__ = "InetAddress"
_CotvMcastRouteInfoActiveGroupAddr_Object = MibTableColumn
cotvMcastRouteInfoActiveGroupAddr = _CotvMcastRouteInfoActiveGroupAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 5),
    _CotvMcastRouteInfoActiveGroupAddr_Type()
)
cotvMcastRouteInfoActiveGroupAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoActiveGroupAddr.setStatus("current")
_CotvMcastRouteInfoIf_Type = InterfaceIndexOrZero
_CotvMcastRouteInfoIf_Object = MibTableColumn
cotvMcastRouteInfoIf = _CotvMcastRouteInfoIf_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 6),
    _CotvMcastRouteInfoIf_Type()
)
cotvMcastRouteInfoIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoIf.setStatus("current")
_CotvMcastRouteInfoHostAddrType_Type = InetAddressType
_CotvMcastRouteInfoHostAddrType_Object = MibTableColumn
cotvMcastRouteInfoHostAddrType = _CotvMcastRouteInfoHostAddrType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 7),
    _CotvMcastRouteInfoHostAddrType_Type()
)
cotvMcastRouteInfoHostAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoHostAddrType.setStatus("current")
_CotvMcastRouteInfoHostAddr_Type = InetAddress
_CotvMcastRouteInfoHostAddr_Object = MibTableColumn
cotvMcastRouteInfoHostAddr = _CotvMcastRouteInfoHostAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 8),
    _CotvMcastRouteInfoHostAddr_Type()
)
cotvMcastRouteInfoHostAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoHostAddr.setStatus("current")
_CotvMcastRouteInfoProtocolOwners_Type = SnmpAdminString
_CotvMcastRouteInfoProtocolOwners_Object = MibTableColumn
cotvMcastRouteInfoProtocolOwners = _CotvMcastRouteInfoProtocolOwners_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 9),
    _CotvMcastRouteInfoProtocolOwners_Type()
)
cotvMcastRouteInfoProtocolOwners.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoProtocolOwners.setStatus("current")
_CotvMcastRouteInfoMetric_Type = Unsigned32
_CotvMcastRouteInfoMetric_Object = MibTableColumn
cotvMcastRouteInfoMetric = _CotvMcastRouteInfoMetric_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 10),
    _CotvMcastRouteInfoMetric_Type()
)
cotvMcastRouteInfoMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoMetric.setStatus("current")
_CotvMcastRouteInfoUpTime_Type = Unsigned32
_CotvMcastRouteInfoUpTime_Object = MibTableColumn
cotvMcastRouteInfoUpTime = _CotvMcastRouteInfoUpTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 1, 5, 3, 1, 11),
    _CotvMcastRouteInfoUpTime_Type()
)
cotvMcastRouteInfoUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoUpTime.setStatus("current")
if mibBuilder.loadTexts:
    cotvMcastRouteInfoUpTime.setUnits("seconds")
_CiscoOtvMIBConform_ObjectIdentity = ObjectIdentity
ciscoOtvMIBConform = _CiscoOtvMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2)
)
_CiscoOtvMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoOtvMIBCompliances = _CiscoOtvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 1)
)
_CiscoOtvMIBGroups_ObjectIdentity = ObjectIdentity
ciscoOtvMIBGroups = _CiscoOtvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2)
)

# Managed Objects groups

ciscoOtvSiteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2, 1)
)
ciscoOtvSiteGroup.setObjects(
      *(("CISCO-OTV-MIB", "cotvSiteIdAdmin"),
        ("CISCO-OTV-MIB", "cotvSiteIdOper"),
        ("CISCO-OTV-MIB", "cotvSiteVlan"),
        ("CISCO-OTV-MIB", "cotvSiteVlanState"))
)
if mibBuilder.loadTexts:
    ciscoOtvSiteGroup.setStatus("current")

ciscoOtvOverlayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2, 2)
)
ciscoOtvOverlayGroup.setObjects(
      *(("CISCO-OTV-MIB", "cotvOverlayVpnName"),
        ("CISCO-OTV-MIB", "cotvOverlayVpnState"),
        ("CISCO-OTV-MIB", "cotvOverlayVpnDownReason"),
        ("CISCO-OTV-MIB", "cotvOverlayVlansExtendedFirst2k"),
        ("CISCO-OTV-MIB", "cotvOverlayVlansExtendedSecond2k"),
        ("CISCO-OTV-MIB", "cotvOverlayControlGroupAddrType"),
        ("CISCO-OTV-MIB", "cotvOverlayControlGroupAddr"),
        ("CISCO-OTV-MIB", "cotvOverlayBroadcastGroupAddrType"),
        ("CISCO-OTV-MIB", "cotvOverlayBroadcastGroupAddr"),
        ("CISCO-OTV-MIB", "cotvOverlayJoinInterface"),
        ("CISCO-OTV-MIB", "cotvOverlaySourceInterface"),
        ("CISCO-OTV-MIB", "cotvOverlayAedCapable"),
        ("CISCO-OTV-MIB", "cotvOverlayAedIncapableReason"),
        ("CISCO-OTV-MIB", "cotvOverlayAdjServerTransportType"),
        ("CISCO-OTV-MIB", "cotvOverlayAdjServerEnable"),
        ("CISCO-OTV-MIB", "cotvOverlayPrimaryAdjServerAddrType"),
        ("CISCO-OTV-MIB", "cotvOverlayPrimaryAdjServerAddr"),
        ("CISCO-OTV-MIB", "cotvOverlaySecondaryAdjServerAddrType"),
        ("CISCO-OTV-MIB", "cotvOverlaySecondaryAdjServerAddr"),
        ("CISCO-OTV-MIB", "cotvOverlaySuppressArpND"),
        ("CISCO-OTV-MIB", "cotvOverlayStorageType"),
        ("CISCO-OTV-MIB", "cotvOverlayRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoOtvOverlayGroup.setStatus("current")

ciscoOtvVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2, 3)
)
ciscoOtvVlanGroup.setObjects(
      *(("CISCO-OTV-MIB", "cotvVlanState"),
        ("CISCO-OTV-MIB", "cotvVlanInactiveReason"),
        ("CISCO-OTV-MIB", "cotvVlanAedAddrType"),
        ("CISCO-OTV-MIB", "cotvVlanAedAddr"),
        ("CISCO-OTV-MIB", "cotvVlanEdgeDevIsAed"))
)
if mibBuilder.loadTexts:
    ciscoOtvVlanGroup.setStatus("current")

ciscoOtvDataGroupConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2, 4)
)
ciscoOtvDataGroupConfigGroup.setObjects(
      *(("CISCO-OTV-MIB", "cotvDataGroupStorageType"),
        ("CISCO-OTV-MIB", "cotvDataGroupRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoOtvDataGroupConfigGroup.setStatus("current")

ciscoOtvDataGroupInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2, 5)
)
ciscoOtvDataGroupInfoGroup.setObjects(
      *(("CISCO-OTV-MIB", "cotvDataGroupJoinInterface"),
        ("CISCO-OTV-MIB", "cotvDataGroupLocalActiveSrcState"))
)
if mibBuilder.loadTexts:
    ciscoOtvDataGroupInfoGroup.setStatus("current")

ciscoOtvAdjacencyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2, 6)
)
ciscoOtvAdjacencyGroup.setObjects(
      *(("CISCO-OTV-MIB", "cotvAdjacentDevSystemID"),
        ("CISCO-OTV-MIB", "cotvAdjacentDevName"),
        ("CISCO-OTV-MIB", "cotvAdjacentDevState"),
        ("CISCO-OTV-MIB", "cotvAdjacentDevUpTime"))
)
if mibBuilder.loadTexts:
    ciscoOtvAdjacencyGroup.setStatus("current")

ciscoOtvArpNdCacheGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2, 7)
)
ciscoOtvArpNdCacheGroup.setObjects(
      *(("CISCO-OTV-MIB", "cotvArpNdCacheMacAddr"),
        ("CISCO-OTV-MIB", "cotvArpNdCacheAge"),
        ("CISCO-OTV-MIB", "cotvArpNdCacheTimeToExpire"))
)
if mibBuilder.loadTexts:
    ciscoOtvArpNdCacheGroup.setStatus("current")

ciscoOtvRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2, 8)
)
ciscoOtvRouteGroup.setObjects(
      *(("CISCO-OTV-MIB", "cotvRouteMetric"),
        ("CISCO-OTV-MIB", "cotvRouteUpTime"),
        ("CISCO-OTV-MIB", "cotvRouteOwner"),
        ("CISCO-OTV-MIB", "cotvRouteNextHopIf"),
        ("CISCO-OTV-MIB", "cotvRouteNextHopAddrType"),
        ("CISCO-OTV-MIB", "cotvRouteNextHopAddr"))
)
if mibBuilder.loadTexts:
    ciscoOtvRouteGroup.setStatus("current")

ciscoOtvMcastRouteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2, 9)
)
ciscoOtvMcastRouteGroup.setObjects(
      *(("CISCO-OTV-MIB", "cotvMcastRouteOwners"),
        ("CISCO-OTV-MIB", "cotvMcastRouteMetric"),
        ("CISCO-OTV-MIB", "cotvMcastRouteUpTime"))
)
if mibBuilder.loadTexts:
    ciscoOtvMcastRouteGroup.setStatus("current")

ciscoOtvMcastRouteInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 2, 10)
)
ciscoOtvMcastRouteInfoGroup.setObjects(
      *(("CISCO-OTV-MIB", "cotvMcastRouteInfoHostAddrType"),
        ("CISCO-OTV-MIB", "cotvMcastRouteInfoHostAddr"),
        ("CISCO-OTV-MIB", "cotvMcastRouteInfoProtocolOwners"),
        ("CISCO-OTV-MIB", "cotvMcastRouteInfoMetric"),
        ("CISCO-OTV-MIB", "cotvMcastRouteInfoUpTime"))
)
if mibBuilder.loadTexts:
    ciscoOtvMcastRouteInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoOtvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 810, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoOtvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-OTV-MIB",
    **{"ciscoOtvMIB": ciscoOtvMIB,
       "ciscoOtvMIBNotifs": ciscoOtvMIBNotifs,
       "ciscoOtvMIBObjects": ciscoOtvMIBObjects,
       "cotvGlobalObjects": cotvGlobalObjects,
       "cotvSiteObjects": cotvSiteObjects,
       "cotvSiteIdAdmin": cotvSiteIdAdmin,
       "cotvSiteIdOper": cotvSiteIdOper,
       "cotvSiteVlan": cotvSiteVlan,
       "cotvSiteVlanState": cotvSiteVlanState,
       "cotvGlobalStatsObjects": cotvGlobalStatsObjects,
       "cotvOverlayObjects": cotvOverlayObjects,
       "cotvOverlayTable": cotvOverlayTable,
       "cotvOverlayEntry": cotvOverlayEntry,
       "cotvOverlayNumber": cotvOverlayNumber,
       "cotvOverlayVpnName": cotvOverlayVpnName,
       "cotvOverlayVpnState": cotvOverlayVpnState,
       "cotvOverlayVpnDownReason": cotvOverlayVpnDownReason,
       "cotvOverlayVlansExtendedFirst2k": cotvOverlayVlansExtendedFirst2k,
       "cotvOverlayVlansExtendedSecond2k": cotvOverlayVlansExtendedSecond2k,
       "cotvOverlayControlGroupAddrType": cotvOverlayControlGroupAddrType,
       "cotvOverlayControlGroupAddr": cotvOverlayControlGroupAddr,
       "cotvOverlayBroadcastGroupAddrType": cotvOverlayBroadcastGroupAddrType,
       "cotvOverlayBroadcastGroupAddr": cotvOverlayBroadcastGroupAddr,
       "cotvOverlayJoinInterface": cotvOverlayJoinInterface,
       "cotvOverlaySourceInterface": cotvOverlaySourceInterface,
       "cotvOverlayAedCapable": cotvOverlayAedCapable,
       "cotvOverlayAedIncapableReason": cotvOverlayAedIncapableReason,
       "cotvOverlayAdjServerTransportType": cotvOverlayAdjServerTransportType,
       "cotvOverlayAdjServerEnable": cotvOverlayAdjServerEnable,
       "cotvOverlayPrimaryAdjServerAddrType": cotvOverlayPrimaryAdjServerAddrType,
       "cotvOverlayPrimaryAdjServerAddr": cotvOverlayPrimaryAdjServerAddr,
       "cotvOverlaySecondaryAdjServerAddrType": cotvOverlaySecondaryAdjServerAddrType,
       "cotvOverlaySecondaryAdjServerAddr": cotvOverlaySecondaryAdjServerAddr,
       "cotvOverlaySuppressArpND": cotvOverlaySuppressArpND,
       "cotvOverlayStorageType": cotvOverlayStorageType,
       "cotvOverlayRowStatus": cotvOverlayRowStatus,
       "cotvVlansTable": cotvVlansTable,
       "cotvVlansEntry": cotvVlansEntry,
       "cotvVlanId": cotvVlanId,
       "cotvVlanState": cotvVlanState,
       "cotvVlanInactiveReason": cotvVlanInactiveReason,
       "cotvVlanAedAddrType": cotvVlanAedAddrType,
       "cotvVlanAedAddr": cotvVlanAedAddr,
       "cotvVlanEdgeDevIsAed": cotvVlanEdgeDevIsAed,
       "cotvDataGroupConfigTable": cotvDataGroupConfigTable,
       "cotvDataGroupConfigEntry": cotvDataGroupConfigEntry,
       "cotvDataGroupMcastRangeAddrType": cotvDataGroupMcastRangeAddrType,
       "cotvDataGroupMcastRangeAddr": cotvDataGroupMcastRangeAddr,
       "cotvDataGroupMcastRangePrefixLength": cotvDataGroupMcastRangePrefixLength,
       "cotvDataGroupStorageType": cotvDataGroupStorageType,
       "cotvDataGroupRowStatus": cotvDataGroupRowStatus,
       "cotvDataGroupInfoTable": cotvDataGroupInfoTable,
       "cotvDataGroupInfoEntry": cotvDataGroupInfoEntry,
       "cotvDataGroupActiveSrcLocation": cotvDataGroupActiveSrcLocation,
       "cotvDataGroupVlanId": cotvDataGroupVlanId,
       "cotvDataGroupActiveGroupAddrType": cotvDataGroupActiveGroupAddrType,
       "cotvDataGroupActiveGroupAddr": cotvDataGroupActiveGroupAddr,
       "cotvDataGroupActiveSrcAddrType": cotvDataGroupActiveSrcAddrType,
       "cotvDataGroupActiveSrcAddr": cotvDataGroupActiveSrcAddr,
       "cotvDataGroupDeliveryGroupAddrType": cotvDataGroupDeliveryGroupAddrType,
       "cotvDataGroupDeliveryGroupAddr": cotvDataGroupDeliveryGroupAddr,
       "cotvDataGroupDeliverySrcAddrType": cotvDataGroupDeliverySrcAddrType,
       "cotvDataGroupDeliverySrcAddr": cotvDataGroupDeliverySrcAddr,
       "cotvDataGroupJoinInterface": cotvDataGroupJoinInterface,
       "cotvDataGroupLocalActiveSrcState": cotvDataGroupLocalActiveSrcState,
       "cotvAdjacencyObjects": cotvAdjacencyObjects,
       "cotvAdjacencyDatabaseTable": cotvAdjacencyDatabaseTable,
       "cotvAdjacencyDatabaseEntry": cotvAdjacencyDatabaseEntry,
       "cotvAdjacentDevAddrType": cotvAdjacentDevAddrType,
       "cotvAdjacentDevAddr": cotvAdjacentDevAddr,
       "cotvAdjacentDevSystemID": cotvAdjacentDevSystemID,
       "cotvAdjacentDevName": cotvAdjacentDevName,
       "cotvAdjacentDevState": cotvAdjacentDevState,
       "cotvAdjacentDevUpTime": cotvAdjacentDevUpTime,
       "cotvArpNdObjects": cotvArpNdObjects,
       "cotvArpNdCacheTable": cotvArpNdCacheTable,
       "cotvArpNdCacheEntry": cotvArpNdCacheEntry,
       "cotvArpNdCacheL3AddrType": cotvArpNdCacheL3AddrType,
       "cotvArpNdCacheL3Addr": cotvArpNdCacheL3Addr,
       "cotvArpNdCacheMacAddr": cotvArpNdCacheMacAddr,
       "cotvArpNdCacheAge": cotvArpNdCacheAge,
       "cotvArpNdCacheTimeToExpire": cotvArpNdCacheTimeToExpire,
       "cotvRouteObjects": cotvRouteObjects,
       "cotvRouteTable": cotvRouteTable,
       "cotvRouteEntry": cotvRouteEntry,
       "cotvRouteVlanId": cotvRouteVlanId,
       "cotvRouteMacAddr": cotvRouteMacAddr,
       "cotvRouteMetric": cotvRouteMetric,
       "cotvRouteUpTime": cotvRouteUpTime,
       "cotvRouteOwner": cotvRouteOwner,
       "cotvRouteNextHopIf": cotvRouteNextHopIf,
       "cotvRouteNextHopAddrType": cotvRouteNextHopAddrType,
       "cotvRouteNextHopAddr": cotvRouteNextHopAddr,
       "cotvMcastRouteTable": cotvMcastRouteTable,
       "cotvMcastRouteEntry": cotvMcastRouteEntry,
       "cotvMcastRouteVlanId": cotvMcastRouteVlanId,
       "cotvMcastRouteActiveSrcAddrType": cotvMcastRouteActiveSrcAddrType,
       "cotvMcastRouteActiveSrcAddr": cotvMcastRouteActiveSrcAddr,
       "cotvMcastRouteActiveGroupAddrType": cotvMcastRouteActiveGroupAddrType,
       "cotvMcastRouteActiveGroupAddr": cotvMcastRouteActiveGroupAddr,
       "cotvMcastRouteOwners": cotvMcastRouteOwners,
       "cotvMcastRouteMetric": cotvMcastRouteMetric,
       "cotvMcastRouteUpTime": cotvMcastRouteUpTime,
       "cotvMcastRouteInfoTable": cotvMcastRouteInfoTable,
       "cotvMcastRouteInfoEntry": cotvMcastRouteInfoEntry,
       "cotvMcastRouteInfoVlanId": cotvMcastRouteInfoVlanId,
       "cotvMcastRouteInfoActiveSrcAddrType": cotvMcastRouteInfoActiveSrcAddrType,
       "cotvMcastRouteInfoActiveSrcAddr": cotvMcastRouteInfoActiveSrcAddr,
       "cotvMcastRouteInfoActiveGroupAddrType": cotvMcastRouteInfoActiveGroupAddrType,
       "cotvMcastRouteInfoActiveGroupAddr": cotvMcastRouteInfoActiveGroupAddr,
       "cotvMcastRouteInfoIf": cotvMcastRouteInfoIf,
       "cotvMcastRouteInfoHostAddrType": cotvMcastRouteInfoHostAddrType,
       "cotvMcastRouteInfoHostAddr": cotvMcastRouteInfoHostAddr,
       "cotvMcastRouteInfoProtocolOwners": cotvMcastRouteInfoProtocolOwners,
       "cotvMcastRouteInfoMetric": cotvMcastRouteInfoMetric,
       "cotvMcastRouteInfoUpTime": cotvMcastRouteInfoUpTime,
       "ciscoOtvMIBConform": ciscoOtvMIBConform,
       "ciscoOtvMIBCompliances": ciscoOtvMIBCompliances,
       "ciscoOtvMIBCompliance": ciscoOtvMIBCompliance,
       "ciscoOtvMIBGroups": ciscoOtvMIBGroups,
       "ciscoOtvSiteGroup": ciscoOtvSiteGroup,
       "ciscoOtvOverlayGroup": ciscoOtvOverlayGroup,
       "ciscoOtvVlanGroup": ciscoOtvVlanGroup,
       "ciscoOtvDataGroupConfigGroup": ciscoOtvDataGroupConfigGroup,
       "ciscoOtvDataGroupInfoGroup": ciscoOtvDataGroupInfoGroup,
       "ciscoOtvAdjacencyGroup": ciscoOtvAdjacencyGroup,
       "ciscoOtvArpNdCacheGroup": ciscoOtvArpNdCacheGroup,
       "ciscoOtvRouteGroup": ciscoOtvRouteGroup,
       "ciscoOtvMcastRouteGroup": ciscoOtvMcastRouteGroup,
       "ciscoOtvMcastRouteInfoGroup": ciscoOtvMcastRouteInfoGroup}
)
