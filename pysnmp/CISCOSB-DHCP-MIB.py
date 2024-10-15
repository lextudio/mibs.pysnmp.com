# SNMP MIB module (CISCOSB-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:14:07 2024
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

(VlanList1,
 VlanList2,
 VlanList3,
 VlanList4) = mibBuilder.importSymbols(
    "CISCOSB-BRIDGEMIBOBJECTS-MIB",
    "VlanList1",
    "VlanList2",
    "VlanList3",
    "VlanList4")

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rsDHCP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38)
)
rsDHCP.setRevisions(
        ("2003-10-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlDhcpSrvOptionTypeEnum(Integer32, TextualConvention):
    status = "current"
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
        *(("ascii", 3),
          ("boolean", 1),
          ("hex", 5),
          ("integer", 2),
          ("ip", 4),
          ("ip-list", 6))
    )



# MIB Managed Objects in the order of their OIDs

_RsDhcpMibVersion_Type = Integer32
_RsDhcpMibVersion_Object = MibScalar
rsDhcpMibVersion = _RsDhcpMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 14),
    _RsDhcpMibVersion_Type()
)
rsDhcpMibVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rsDhcpMibVersion.setStatus("current")
_RlDhcpRelayMaximalNumberOfNonIpVlans_Type = Unsigned32
_RlDhcpRelayMaximalNumberOfNonIpVlans_Object = MibScalar
rlDhcpRelayMaximalNumberOfNonIpVlans = _RlDhcpRelayMaximalNumberOfNonIpVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 23),
    _RlDhcpRelayMaximalNumberOfNonIpVlans_Type()
)
rlDhcpRelayMaximalNumberOfNonIpVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpRelayMaximalNumberOfNonIpVlans.setStatus("current")
_RlDhcpRelayCurrentNumberOfNonIpVlans_Type = Unsigned32
_RlDhcpRelayCurrentNumberOfNonIpVlans_Object = MibScalar
rlDhcpRelayCurrentNumberOfNonIpVlans = _RlDhcpRelayCurrentNumberOfNonIpVlans_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 24),
    _RlDhcpRelayCurrentNumberOfNonIpVlans_Type()
)
rlDhcpRelayCurrentNumberOfNonIpVlans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpRelayCurrentNumberOfNonIpVlans.setStatus("current")
_RlDhcpRelayEnable_Type = TruthValue
_RlDhcpRelayEnable_Object = MibScalar
rlDhcpRelayEnable = _RlDhcpRelayEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 25),
    _RlDhcpRelayEnable_Type()
)
rlDhcpRelayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayEnable.setStatus("current")
_RlDhcpRelayExists_Type = TruthValue
_RlDhcpRelayExists_Object = MibScalar
rlDhcpRelayExists = _RlDhcpRelayExists_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 26),
    _RlDhcpRelayExists_Type()
)
rlDhcpRelayExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpRelayExists.setStatus("current")
_RlDhcpRelayNextServerTable_Object = MibTable
rlDhcpRelayNextServerTable = _RlDhcpRelayNextServerTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 27)
)
if mibBuilder.loadTexts:
    rlDhcpRelayNextServerTable.setStatus("current")
_RlDhcpRelayNextServerEntry_Object = MibTableRow
rlDhcpRelayNextServerEntry = _RlDhcpRelayNextServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 27, 1)
)
rlDhcpRelayNextServerEntry.setIndexNames(
    (0, "CISCOSB-DHCP-MIB", "rlDhcpRelayNextServerIpAddr"),
)
if mibBuilder.loadTexts:
    rlDhcpRelayNextServerEntry.setStatus("current")
_RlDhcpRelayNextServerIpAddr_Type = IpAddress
_RlDhcpRelayNextServerIpAddr_Object = MibTableColumn
rlDhcpRelayNextServerIpAddr = _RlDhcpRelayNextServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 27, 1, 1),
    _RlDhcpRelayNextServerIpAddr_Type()
)
rlDhcpRelayNextServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpRelayNextServerIpAddr.setStatus("current")
_RlDhcpRelayNextServerSecThreshold_Type = Unsigned32
_RlDhcpRelayNextServerSecThreshold_Object = MibTableColumn
rlDhcpRelayNextServerSecThreshold = _RlDhcpRelayNextServerSecThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 27, 1, 2),
    _RlDhcpRelayNextServerSecThreshold_Type()
)
rlDhcpRelayNextServerSecThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayNextServerSecThreshold.setStatus("current")
_RlDhcpRelayNextServerRowStatus_Type = RowStatus
_RlDhcpRelayNextServerRowStatus_Object = MibTableColumn
rlDhcpRelayNextServerRowStatus = _RlDhcpRelayNextServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 27, 1, 3),
    _RlDhcpRelayNextServerRowStatus_Type()
)
rlDhcpRelayNextServerRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayNextServerRowStatus.setStatus("current")
_RlDhcpRelayInterfaceTable_Object = MibTable
rlDhcpRelayInterfaceTable = _RlDhcpRelayInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 28)
)
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceTable.setStatus("current")
_RlDhcpRelayInterfaceEntry_Object = MibTableRow
rlDhcpRelayInterfaceEntry = _RlDhcpRelayInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 28, 1)
)
rlDhcpRelayInterfaceEntry.setIndexNames(
    (0, "CISCOSB-DHCP-MIB", "rlDhcpRelayInterfaceIfindex"),
)
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceEntry.setStatus("current")
_RlDhcpRelayInterfaceIfindex_Type = Integer32
_RlDhcpRelayInterfaceIfindex_Object = MibTableColumn
rlDhcpRelayInterfaceIfindex = _RlDhcpRelayInterfaceIfindex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 28, 1, 1),
    _RlDhcpRelayInterfaceIfindex_Type()
)
rlDhcpRelayInterfaceIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceIfindex.setStatus("current")
_RlDhcpRelayInterfaceUseGiaddr_Type = TruthValue
_RlDhcpRelayInterfaceUseGiaddr_Object = MibTableColumn
rlDhcpRelayInterfaceUseGiaddr = _RlDhcpRelayInterfaceUseGiaddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 28, 1, 2),
    _RlDhcpRelayInterfaceUseGiaddr_Type()
)
rlDhcpRelayInterfaceUseGiaddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceUseGiaddr.setStatus("current")
_RlDhcpRelayInterfaceRowStatus_Type = RowStatus
_RlDhcpRelayInterfaceRowStatus_Object = MibTableColumn
rlDhcpRelayInterfaceRowStatus = _RlDhcpRelayInterfaceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 28, 1, 3),
    _RlDhcpRelayInterfaceRowStatus_Type()
)
rlDhcpRelayInterfaceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceRowStatus.setStatus("current")
_RlDhcpRelayInterfaceListTable_Object = MibTable
rlDhcpRelayInterfaceListTable = _RlDhcpRelayInterfaceListTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 29)
)
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceListTable.setStatus("current")
_RlDhcpRelayInterfaceListEntry_Object = MibTableRow
rlDhcpRelayInterfaceListEntry = _RlDhcpRelayInterfaceListEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 29, 1)
)
rlDhcpRelayInterfaceListEntry.setIndexNames(
    (0, "CISCOSB-DHCP-MIB", "rlDhcpRelayInterfaceListIndex"),
)
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceListEntry.setStatus("current")
_RlDhcpRelayInterfaceListIndex_Type = Integer32
_RlDhcpRelayInterfaceListIndex_Object = MibTableColumn
rlDhcpRelayInterfaceListIndex = _RlDhcpRelayInterfaceListIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 29, 1, 1),
    _RlDhcpRelayInterfaceListIndex_Type()
)
rlDhcpRelayInterfaceListIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceListIndex.setStatus("current")
_RlDhcpRelayInterfaceListPortList_Type = PortList
_RlDhcpRelayInterfaceListPortList_Object = MibTableColumn
rlDhcpRelayInterfaceListPortList = _RlDhcpRelayInterfaceListPortList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 29, 1, 2),
    _RlDhcpRelayInterfaceListPortList_Type()
)
rlDhcpRelayInterfaceListPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceListPortList.setStatus("current")
_RlDhcpRelayInterfaceListVlanId1To1024_Type = VlanList1
_RlDhcpRelayInterfaceListVlanId1To1024_Object = MibTableColumn
rlDhcpRelayInterfaceListVlanId1To1024 = _RlDhcpRelayInterfaceListVlanId1To1024_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 29, 1, 3),
    _RlDhcpRelayInterfaceListVlanId1To1024_Type()
)
rlDhcpRelayInterfaceListVlanId1To1024.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceListVlanId1To1024.setStatus("current")
_RlDhcpRelayInterfaceListVlanId1025To2048_Type = VlanList2
_RlDhcpRelayInterfaceListVlanId1025To2048_Object = MibTableColumn
rlDhcpRelayInterfaceListVlanId1025To2048 = _RlDhcpRelayInterfaceListVlanId1025To2048_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 29, 1, 4),
    _RlDhcpRelayInterfaceListVlanId1025To2048_Type()
)
rlDhcpRelayInterfaceListVlanId1025To2048.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceListVlanId1025To2048.setStatus("current")
_RlDhcpRelayInterfaceListVlanId2049To3072_Type = VlanList3
_RlDhcpRelayInterfaceListVlanId2049To3072_Object = MibTableColumn
rlDhcpRelayInterfaceListVlanId2049To3072 = _RlDhcpRelayInterfaceListVlanId2049To3072_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 29, 1, 5),
    _RlDhcpRelayInterfaceListVlanId2049To3072_Type()
)
rlDhcpRelayInterfaceListVlanId2049To3072.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceListVlanId2049To3072.setStatus("current")
_RlDhcpRelayInterfaceListVlanId3073To4094_Type = VlanList4
_RlDhcpRelayInterfaceListVlanId3073To4094_Object = MibTableColumn
rlDhcpRelayInterfaceListVlanId3073To4094 = _RlDhcpRelayInterfaceListVlanId3073To4094_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 29, 1, 6),
    _RlDhcpRelayInterfaceListVlanId3073To4094_Type()
)
rlDhcpRelayInterfaceListVlanId3073To4094.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpRelayInterfaceListVlanId3073To4094.setStatus("current")


class _RlDhcpSrvEnable_Type(TruthValue):
    """Custom type rlDhcpSrvEnable based on TruthValue"""


_RlDhcpSrvEnable_Object = MibScalar
rlDhcpSrvEnable = _RlDhcpSrvEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 30),
    _RlDhcpSrvEnable_Type()
)
rlDhcpSrvEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvEnable.setStatus("current")
_RlDhcpSrvExists_Type = TruthValue
_RlDhcpSrvExists_Object = MibScalar
rlDhcpSrvExists = _RlDhcpSrvExists_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 31),
    _RlDhcpSrvExists_Type()
)
rlDhcpSrvExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvExists.setStatus("current")


class _RlDhcpSrvDbLocation_Type(Integer32):
    """Custom type rlDhcpSrvDbLocation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("flash", 2),
          ("nvram", 1))
    )


_RlDhcpSrvDbLocation_Type.__name__ = "Integer32"
_RlDhcpSrvDbLocation_Object = MibScalar
rlDhcpSrvDbLocation = _RlDhcpSrvDbLocation_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 32),
    _RlDhcpSrvDbLocation_Type()
)
rlDhcpSrvDbLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDbLocation.setStatus("obsolete")
_RlDhcpSrvMaxNumOfClients_Type = Unsigned32
_RlDhcpSrvMaxNumOfClients_Object = MibScalar
rlDhcpSrvMaxNumOfClients = _RlDhcpSrvMaxNumOfClients_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 33),
    _RlDhcpSrvMaxNumOfClients_Type()
)
rlDhcpSrvMaxNumOfClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvMaxNumOfClients.setStatus("current")
_RlDhcpSrvDbNumOfActiveEntries_Type = Unsigned32
_RlDhcpSrvDbNumOfActiveEntries_Object = MibScalar
rlDhcpSrvDbNumOfActiveEntries = _RlDhcpSrvDbNumOfActiveEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 34),
    _RlDhcpSrvDbNumOfActiveEntries_Type()
)
rlDhcpSrvDbNumOfActiveEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDbNumOfActiveEntries.setStatus("current")


class _RlDhcpSrvDbErase_Type(TruthValue):
    """Custom type rlDhcpSrvDbErase based on TruthValue"""


_RlDhcpSrvDbErase_Object = MibScalar
rlDhcpSrvDbErase = _RlDhcpSrvDbErase_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 35),
    _RlDhcpSrvDbErase_Type()
)
rlDhcpSrvDbErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDbErase.setStatus("obsolete")


class _RlDhcpSrvProbeEnable_Type(TruthValue):
    """Custom type rlDhcpSrvProbeEnable based on TruthValue"""


_RlDhcpSrvProbeEnable_Object = MibScalar
rlDhcpSrvProbeEnable = _RlDhcpSrvProbeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 36),
    _RlDhcpSrvProbeEnable_Type()
)
rlDhcpSrvProbeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvProbeEnable.setStatus("current")


class _RlDhcpSrvProbeTimeout_Type(Unsigned32):
    """Custom type rlDhcpSrvProbeTimeout based on Unsigned32"""
    defaultValue = 500

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 10000),
    )


_RlDhcpSrvProbeTimeout_Type.__name__ = "Unsigned32"
_RlDhcpSrvProbeTimeout_Object = MibScalar
rlDhcpSrvProbeTimeout = _RlDhcpSrvProbeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 37),
    _RlDhcpSrvProbeTimeout_Type()
)
rlDhcpSrvProbeTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvProbeTimeout.setStatus("current")


class _RlDhcpSrvProbeRetries_Type(Unsigned32):
    """Custom type rlDhcpSrvProbeRetries based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RlDhcpSrvProbeRetries_Type.__name__ = "Unsigned32"
_RlDhcpSrvProbeRetries_Object = MibScalar
rlDhcpSrvProbeRetries = _RlDhcpSrvProbeRetries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 38),
    _RlDhcpSrvProbeRetries_Type()
)
rlDhcpSrvProbeRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvProbeRetries.setStatus("current")


class _RlDhcpSrvDefaultNetworkPoolName_Type(DisplayString):
    """Custom type rlDhcpSrvDefaultNetworkPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpSrvDefaultNetworkPoolName_Type.__name__ = "DisplayString"
_RlDhcpSrvDefaultNetworkPoolName_Object = MibScalar
rlDhcpSrvDefaultNetworkPoolName = _RlDhcpSrvDefaultNetworkPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 39),
    _RlDhcpSrvDefaultNetworkPoolName_Type()
)
rlDhcpSrvDefaultNetworkPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDefaultNetworkPoolName.setStatus("current")
_RlDhcpSrvIpAddrTable_Object = MibTable
rlDhcpSrvIpAddrTable = _RlDhcpSrvIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45)
)
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrTable.setStatus("current")
_RlDhcpSrvIpAddrEntry_Object = MibTableRow
rlDhcpSrvIpAddrEntry = _RlDhcpSrvIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1)
)
rlDhcpSrvIpAddrEntry.setIndexNames(
    (0, "CISCOSB-DHCP-MIB", "rlDhcpSrvIpAddrIpAddr"),
)
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrEntry.setStatus("current")
_RlDhcpSrvIpAddrIpAddr_Type = IpAddress
_RlDhcpSrvIpAddrIpAddr_Object = MibTableColumn
rlDhcpSrvIpAddrIpAddr = _RlDhcpSrvIpAddrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 1),
    _RlDhcpSrvIpAddrIpAddr_Type()
)
rlDhcpSrvIpAddrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrIpAddr.setStatus("current")
_RlDhcpSrvIpAddrIpNetMask_Type = IpAddress
_RlDhcpSrvIpAddrIpNetMask_Object = MibTableColumn
rlDhcpSrvIpAddrIpNetMask = _RlDhcpSrvIpAddrIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 2),
    _RlDhcpSrvIpAddrIpNetMask_Type()
)
rlDhcpSrvIpAddrIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrIpNetMask.setStatus("current")


class _RlDhcpSrvIpAddrIdentifier_Type(OctetString):
    """Custom type rlDhcpSrvIpAddrIdentifier based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_RlDhcpSrvIpAddrIdentifier_Type.__name__ = "OctetString"
_RlDhcpSrvIpAddrIdentifier_Object = MibTableColumn
rlDhcpSrvIpAddrIdentifier = _RlDhcpSrvIpAddrIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 3),
    _RlDhcpSrvIpAddrIdentifier_Type()
)
rlDhcpSrvIpAddrIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrIdentifier.setStatus("current")


class _RlDhcpSrvIpAddrIdentifierType_Type(Integer32):
    """Custom type rlDhcpSrvIpAddrIdentifierType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clientId", 2),
          ("physAddr", 1))
    )


_RlDhcpSrvIpAddrIdentifierType_Type.__name__ = "Integer32"
_RlDhcpSrvIpAddrIdentifierType_Object = MibTableColumn
rlDhcpSrvIpAddrIdentifierType = _RlDhcpSrvIpAddrIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 4),
    _RlDhcpSrvIpAddrIdentifierType_Type()
)
rlDhcpSrvIpAddrIdentifierType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrIdentifierType.setStatus("current")


class _RlDhcpSrvIpAddrClnHostName_Type(SnmpAdminString):
    """Custom type rlDhcpSrvIpAddrClnHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvIpAddrClnHostName_Type.__name__ = "SnmpAdminString"
_RlDhcpSrvIpAddrClnHostName_Object = MibTableColumn
rlDhcpSrvIpAddrClnHostName = _RlDhcpSrvIpAddrClnHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 5),
    _RlDhcpSrvIpAddrClnHostName_Type()
)
rlDhcpSrvIpAddrClnHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrClnHostName.setStatus("current")


class _RlDhcpSrvIpAddrMechanism_Type(Integer32):
    """Custom type rlDhcpSrvIpAddrMechanism based on Integer32"""
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
        *(("automatic", 2),
          ("dynamic", 3),
          ("manual", 1))
    )


_RlDhcpSrvIpAddrMechanism_Type.__name__ = "Integer32"
_RlDhcpSrvIpAddrMechanism_Object = MibTableColumn
rlDhcpSrvIpAddrMechanism = _RlDhcpSrvIpAddrMechanism_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 6),
    _RlDhcpSrvIpAddrMechanism_Type()
)
rlDhcpSrvIpAddrMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrMechanism.setStatus("current")


class _RlDhcpSrvIpAddrAgeTime_Type(Unsigned32):
    """Custom type rlDhcpSrvIpAddrAgeTime based on Unsigned32"""
    defaultValue = 0


_RlDhcpSrvIpAddrAgeTime_Object = MibTableColumn
rlDhcpSrvIpAddrAgeTime = _RlDhcpSrvIpAddrAgeTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 7),
    _RlDhcpSrvIpAddrAgeTime_Type()
)
rlDhcpSrvIpAddrAgeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrAgeTime.setStatus("current")


class _RlDhcpSrvIpAddrPoolName_Type(DisplayString):
    """Custom type rlDhcpSrvIpAddrPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpSrvIpAddrPoolName_Type.__name__ = "DisplayString"
_RlDhcpSrvIpAddrPoolName_Object = MibTableColumn
rlDhcpSrvIpAddrPoolName = _RlDhcpSrvIpAddrPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 8),
    _RlDhcpSrvIpAddrPoolName_Type()
)
rlDhcpSrvIpAddrPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrPoolName.setStatus("current")


class _RlDhcpSrvIpAddrConfParamsName_Type(DisplayString):
    """Custom type rlDhcpSrvIpAddrConfParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvIpAddrConfParamsName_Type.__name__ = "DisplayString"
_RlDhcpSrvIpAddrConfParamsName_Object = MibTableColumn
rlDhcpSrvIpAddrConfParamsName = _RlDhcpSrvIpAddrConfParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 9),
    _RlDhcpSrvIpAddrConfParamsName_Type()
)
rlDhcpSrvIpAddrConfParamsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrConfParamsName.setStatus("current")
_RlDhcpSrvIpAddrRowStatus_Type = RowStatus
_RlDhcpSrvIpAddrRowStatus_Object = MibTableColumn
rlDhcpSrvIpAddrRowStatus = _RlDhcpSrvIpAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 10),
    _RlDhcpSrvIpAddrRowStatus_Type()
)
rlDhcpSrvIpAddrRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrRowStatus.setStatus("current")


class _RlDhcpSrvIpAddrLeaseTime_Type(Unsigned32):
    """Custom type rlDhcpSrvIpAddrLeaseTime based on Unsigned32"""
    defaultValue = 86400


_RlDhcpSrvIpAddrLeaseTime_Object = MibTableColumn
rlDhcpSrvIpAddrLeaseTime = _RlDhcpSrvIpAddrLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 11),
    _RlDhcpSrvIpAddrLeaseTime_Type()
)
rlDhcpSrvIpAddrLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrLeaseTime.setStatus("current")


class _RlDhcpSrvIpAddrState_Type(Integer32):
    """Custom type rlDhcpSrvIpAddrState based on Integer32"""
    defaultValue = 2

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
        *(("declined", 4),
          ("expired", 3),
          ("pre-allocated", 1),
          ("valid", 2))
    )


_RlDhcpSrvIpAddrState_Type.__name__ = "Integer32"
_RlDhcpSrvIpAddrState_Object = MibTableColumn
rlDhcpSrvIpAddrState = _RlDhcpSrvIpAddrState_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 12),
    _RlDhcpSrvIpAddrState_Type()
)
rlDhcpSrvIpAddrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrState.setStatus("current")


class _RlDhcpSrvIpAddrOptionParamsName_Type(DisplayString):
    """Custom type rlDhcpSrvIpAddrOptionParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvIpAddrOptionParamsName_Type.__name__ = "DisplayString"
_RlDhcpSrvIpAddrOptionParamsName_Object = MibTableColumn
rlDhcpSrvIpAddrOptionParamsName = _RlDhcpSrvIpAddrOptionParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 45, 1, 13),
    _RlDhcpSrvIpAddrOptionParamsName_Type()
)
rlDhcpSrvIpAddrOptionParamsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvIpAddrOptionParamsName.setStatus("current")
_RlDhcpSrvDynamicTable_Object = MibTable
rlDhcpSrvDynamicTable = _RlDhcpSrvDynamicTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46)
)
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicTable.setStatus("current")
_RlDhcpSrvDynamicEntry_Object = MibTableRow
rlDhcpSrvDynamicEntry = _RlDhcpSrvDynamicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1)
)
rlDhcpSrvDynamicEntry.setIndexNames(
    (0, "CISCOSB-DHCP-MIB", "rlDhcpSrvDynamicPoolName"),
)
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicEntry.setStatus("current")


class _RlDhcpSrvDynamicPoolName_Type(DisplayString):
    """Custom type rlDhcpSrvDynamicPoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpSrvDynamicPoolName_Type.__name__ = "DisplayString"
_RlDhcpSrvDynamicPoolName_Object = MibTableColumn
rlDhcpSrvDynamicPoolName = _RlDhcpSrvDynamicPoolName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 1),
    _RlDhcpSrvDynamicPoolName_Type()
)
rlDhcpSrvDynamicPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicPoolName.setStatus("current")
_RlDhcpSrvDynamicIpAddrFrom_Type = IpAddress
_RlDhcpSrvDynamicIpAddrFrom_Object = MibTableColumn
rlDhcpSrvDynamicIpAddrFrom = _RlDhcpSrvDynamicIpAddrFrom_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 2),
    _RlDhcpSrvDynamicIpAddrFrom_Type()
)
rlDhcpSrvDynamicIpAddrFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicIpAddrFrom.setStatus("current")
_RlDhcpSrvDynamicIpAddrTo_Type = IpAddress
_RlDhcpSrvDynamicIpAddrTo_Object = MibTableColumn
rlDhcpSrvDynamicIpAddrTo = _RlDhcpSrvDynamicIpAddrTo_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 3),
    _RlDhcpSrvDynamicIpAddrTo_Type()
)
rlDhcpSrvDynamicIpAddrTo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicIpAddrTo.setStatus("current")
_RlDhcpSrvDynamicIpNetMask_Type = IpAddress
_RlDhcpSrvDynamicIpNetMask_Object = MibTableColumn
rlDhcpSrvDynamicIpNetMask = _RlDhcpSrvDynamicIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 4),
    _RlDhcpSrvDynamicIpNetMask_Type()
)
rlDhcpSrvDynamicIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicIpNetMask.setStatus("current")


class _RlDhcpSrvDynamicLeaseTime_Type(Unsigned32):
    """Custom type rlDhcpSrvDynamicLeaseTime based on Unsigned32"""
    defaultValue = 86400


_RlDhcpSrvDynamicLeaseTime_Object = MibTableColumn
rlDhcpSrvDynamicLeaseTime = _RlDhcpSrvDynamicLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 5),
    _RlDhcpSrvDynamicLeaseTime_Type()
)
rlDhcpSrvDynamicLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicLeaseTime.setStatus("current")


class _RlDhcpSrvDynamicProbeEnable_Type(TruthValue):
    """Custom type rlDhcpSrvDynamicProbeEnable based on TruthValue"""


_RlDhcpSrvDynamicProbeEnable_Object = MibTableColumn
rlDhcpSrvDynamicProbeEnable = _RlDhcpSrvDynamicProbeEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 6),
    _RlDhcpSrvDynamicProbeEnable_Type()
)
rlDhcpSrvDynamicProbeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicProbeEnable.setStatus("current")
_RlDhcpSrvDynamicTotalNumOfAddr_Type = Unsigned32
_RlDhcpSrvDynamicTotalNumOfAddr_Object = MibTableColumn
rlDhcpSrvDynamicTotalNumOfAddr = _RlDhcpSrvDynamicTotalNumOfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 7),
    _RlDhcpSrvDynamicTotalNumOfAddr_Type()
)
rlDhcpSrvDynamicTotalNumOfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicTotalNumOfAddr.setStatus("current")
_RlDhcpSrvDynamicFreeNumOfAddr_Type = Unsigned32
_RlDhcpSrvDynamicFreeNumOfAddr_Object = MibTableColumn
rlDhcpSrvDynamicFreeNumOfAddr = _RlDhcpSrvDynamicFreeNumOfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 8),
    _RlDhcpSrvDynamicFreeNumOfAddr_Type()
)
rlDhcpSrvDynamicFreeNumOfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicFreeNumOfAddr.setStatus("current")


class _RlDhcpSrvDynamicConfParamsName_Type(DisplayString):
    """Custom type rlDhcpSrvDynamicConfParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvDynamicConfParamsName_Type.__name__ = "DisplayString"
_RlDhcpSrvDynamicConfParamsName_Object = MibTableColumn
rlDhcpSrvDynamicConfParamsName = _RlDhcpSrvDynamicConfParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 9),
    _RlDhcpSrvDynamicConfParamsName_Type()
)
rlDhcpSrvDynamicConfParamsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicConfParamsName.setStatus("current")
_RlDhcpSrvDynamicRowStatus_Type = RowStatus
_RlDhcpSrvDynamicRowStatus_Object = MibTableColumn
rlDhcpSrvDynamicRowStatus = _RlDhcpSrvDynamicRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 10),
    _RlDhcpSrvDynamicRowStatus_Type()
)
rlDhcpSrvDynamicRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicRowStatus.setStatus("current")
_RlDhcpSrvDynamicAvailableNumOfAddr_Type = Unsigned32
_RlDhcpSrvDynamicAvailableNumOfAddr_Object = MibTableColumn
rlDhcpSrvDynamicAvailableNumOfAddr = _RlDhcpSrvDynamicAvailableNumOfAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 11),
    _RlDhcpSrvDynamicAvailableNumOfAddr_Type()
)
rlDhcpSrvDynamicAvailableNumOfAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicAvailableNumOfAddr.setStatus("current")
_RlDhcpSrvDynamicNumOfPreallocatedAddr_Type = Unsigned32
_RlDhcpSrvDynamicNumOfPreallocatedAddr_Object = MibTableColumn
rlDhcpSrvDynamicNumOfPreallocatedAddr = _RlDhcpSrvDynamicNumOfPreallocatedAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 12),
    _RlDhcpSrvDynamicNumOfPreallocatedAddr_Type()
)
rlDhcpSrvDynamicNumOfPreallocatedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicNumOfPreallocatedAddr.setStatus("current")
_RlDhcpSrvDynamicNumOfValidAddr_Type = Unsigned32
_RlDhcpSrvDynamicNumOfValidAddr_Object = MibTableColumn
rlDhcpSrvDynamicNumOfValidAddr = _RlDhcpSrvDynamicNumOfValidAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 13),
    _RlDhcpSrvDynamicNumOfValidAddr_Type()
)
rlDhcpSrvDynamicNumOfValidAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicNumOfValidAddr.setStatus("current")
_RlDhcpSrvDynamicNumOfExpiredAddr_Type = Unsigned32
_RlDhcpSrvDynamicNumOfExpiredAddr_Object = MibTableColumn
rlDhcpSrvDynamicNumOfExpiredAddr = _RlDhcpSrvDynamicNumOfExpiredAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 14),
    _RlDhcpSrvDynamicNumOfExpiredAddr_Type()
)
rlDhcpSrvDynamicNumOfExpiredAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicNumOfExpiredAddr.setStatus("current")
_RlDhcpSrvDynamicNumOfDeclinedAddr_Type = Unsigned32
_RlDhcpSrvDynamicNumOfDeclinedAddr_Object = MibTableColumn
rlDhcpSrvDynamicNumOfDeclinedAddr = _RlDhcpSrvDynamicNumOfDeclinedAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 15),
    _RlDhcpSrvDynamicNumOfDeclinedAddr_Type()
)
rlDhcpSrvDynamicNumOfDeclinedAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicNumOfDeclinedAddr.setStatus("current")


class _RlDhcpSrvDynamicOptionParamsName_Type(DisplayString):
    """Custom type rlDhcpSrvDynamicOptionParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvDynamicOptionParamsName_Type.__name__ = "DisplayString"
_RlDhcpSrvDynamicOptionParamsName_Object = MibTableColumn
rlDhcpSrvDynamicOptionParamsName = _RlDhcpSrvDynamicOptionParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 46, 1, 16),
    _RlDhcpSrvDynamicOptionParamsName_Type()
)
rlDhcpSrvDynamicOptionParamsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvDynamicOptionParamsName.setStatus("current")
_RlDhcpSrvConfParamsTable_Object = MibTable
rlDhcpSrvConfParamsTable = _RlDhcpSrvConfParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47)
)
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsTable.setStatus("current")
_RlDhcpSrvConfParamsEntry_Object = MibTableRow
rlDhcpSrvConfParamsEntry = _RlDhcpSrvConfParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1)
)
rlDhcpSrvConfParamsEntry.setIndexNames(
    (0, "CISCOSB-DHCP-MIB", "rlDhcpSrvConfParamsName"),
)
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsEntry.setStatus("current")


class _RlDhcpSrvConfParamsName_Type(DisplayString):
    """Custom type rlDhcpSrvConfParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpSrvConfParamsName_Type.__name__ = "DisplayString"
_RlDhcpSrvConfParamsName_Object = MibTableColumn
rlDhcpSrvConfParamsName = _RlDhcpSrvConfParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 1),
    _RlDhcpSrvConfParamsName_Type()
)
rlDhcpSrvConfParamsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsName.setStatus("current")
_RlDhcpSrvConfParamsNextServerIp_Type = IpAddress
_RlDhcpSrvConfParamsNextServerIp_Object = MibTableColumn
rlDhcpSrvConfParamsNextServerIp = _RlDhcpSrvConfParamsNextServerIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 2),
    _RlDhcpSrvConfParamsNextServerIp_Type()
)
rlDhcpSrvConfParamsNextServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsNextServerIp.setStatus("current")


class _RlDhcpSrvConfParamsNextServerName_Type(DisplayString):
    """Custom type rlDhcpSrvConfParamsNextServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_RlDhcpSrvConfParamsNextServerName_Type.__name__ = "DisplayString"
_RlDhcpSrvConfParamsNextServerName_Object = MibTableColumn
rlDhcpSrvConfParamsNextServerName = _RlDhcpSrvConfParamsNextServerName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 3),
    _RlDhcpSrvConfParamsNextServerName_Type()
)
rlDhcpSrvConfParamsNextServerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsNextServerName.setStatus("current")


class _RlDhcpSrvConfParamsBootfileName_Type(DisplayString):
    """Custom type rlDhcpSrvConfParamsBootfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_RlDhcpSrvConfParamsBootfileName_Type.__name__ = "DisplayString"
_RlDhcpSrvConfParamsBootfileName_Object = MibTableColumn
rlDhcpSrvConfParamsBootfileName = _RlDhcpSrvConfParamsBootfileName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 4),
    _RlDhcpSrvConfParamsBootfileName_Type()
)
rlDhcpSrvConfParamsBootfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsBootfileName.setStatus("current")
_RlDhcpSrvConfParamsRoutersList_Type = DisplayString
_RlDhcpSrvConfParamsRoutersList_Object = MibTableColumn
rlDhcpSrvConfParamsRoutersList = _RlDhcpSrvConfParamsRoutersList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 5),
    _RlDhcpSrvConfParamsRoutersList_Type()
)
rlDhcpSrvConfParamsRoutersList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsRoutersList.setStatus("current")
_RlDhcpSrvConfParamsTimeSrvList_Type = DisplayString
_RlDhcpSrvConfParamsTimeSrvList_Object = MibTableColumn
rlDhcpSrvConfParamsTimeSrvList = _RlDhcpSrvConfParamsTimeSrvList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 6),
    _RlDhcpSrvConfParamsTimeSrvList_Type()
)
rlDhcpSrvConfParamsTimeSrvList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsTimeSrvList.setStatus("current")
_RlDhcpSrvConfParamsDnsList_Type = DisplayString
_RlDhcpSrvConfParamsDnsList_Object = MibTableColumn
rlDhcpSrvConfParamsDnsList = _RlDhcpSrvConfParamsDnsList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 7),
    _RlDhcpSrvConfParamsDnsList_Type()
)
rlDhcpSrvConfParamsDnsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsDnsList.setStatus("current")


class _RlDhcpSrvConfParamsDomainName_Type(SnmpAdminString):
    """Custom type rlDhcpSrvConfParamsDomainName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvConfParamsDomainName_Type.__name__ = "SnmpAdminString"
_RlDhcpSrvConfParamsDomainName_Object = MibTableColumn
rlDhcpSrvConfParamsDomainName = _RlDhcpSrvConfParamsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 8),
    _RlDhcpSrvConfParamsDomainName_Type()
)
rlDhcpSrvConfParamsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsDomainName.setStatus("current")
_RlDhcpSrvConfParamsNetbiosNameList_Type = DisplayString
_RlDhcpSrvConfParamsNetbiosNameList_Object = MibTableColumn
rlDhcpSrvConfParamsNetbiosNameList = _RlDhcpSrvConfParamsNetbiosNameList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 9),
    _RlDhcpSrvConfParamsNetbiosNameList_Type()
)
rlDhcpSrvConfParamsNetbiosNameList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsNetbiosNameList.setStatus("current")


class _RlDhcpSrvConfParamsNetbiosNodeType_Type(Integer32):
    """Custom type rlDhcpSrvConfParamsNetbiosNodeType based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8)
        )
    )
    namedValues = NamedValues(
        *(("b-node", 1),
          ("h-node", 8),
          ("m-node", 4),
          ("p-node", 2))
    )


_RlDhcpSrvConfParamsNetbiosNodeType_Type.__name__ = "Integer32"
_RlDhcpSrvConfParamsNetbiosNodeType_Object = MibTableColumn
rlDhcpSrvConfParamsNetbiosNodeType = _RlDhcpSrvConfParamsNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 10),
    _RlDhcpSrvConfParamsNetbiosNodeType_Type()
)
rlDhcpSrvConfParamsNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsNetbiosNodeType.setStatus("current")


class _RlDhcpSrvConfParamsCommunity_Type(DisplayString):
    """Custom type rlDhcpSrvConfParamsCommunity based on DisplayString"""
    defaultValue = OctetString("public")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RlDhcpSrvConfParamsCommunity_Type.__name__ = "DisplayString"
_RlDhcpSrvConfParamsCommunity_Object = MibTableColumn
rlDhcpSrvConfParamsCommunity = _RlDhcpSrvConfParamsCommunity_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 11),
    _RlDhcpSrvConfParamsCommunity_Type()
)
rlDhcpSrvConfParamsCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsCommunity.setStatus("obsolete")
_RlDhcpSrvConfParamsNmsIp_Type = IpAddress
_RlDhcpSrvConfParamsNmsIp_Object = MibTableColumn
rlDhcpSrvConfParamsNmsIp = _RlDhcpSrvConfParamsNmsIp_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 12),
    _RlDhcpSrvConfParamsNmsIp_Type()
)
rlDhcpSrvConfParamsNmsIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsNmsIp.setStatus("obsolete")
_RlDhcpSrvConfParamsOptionsList_Type = DisplayString
_RlDhcpSrvConfParamsOptionsList_Object = MibTableColumn
rlDhcpSrvConfParamsOptionsList = _RlDhcpSrvConfParamsOptionsList_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 13),
    _RlDhcpSrvConfParamsOptionsList_Type()
)
rlDhcpSrvConfParamsOptionsList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsOptionsList.setStatus("obsolete")
_RlDhcpSrvConfParamsRowStatus_Type = RowStatus
_RlDhcpSrvConfParamsRowStatus_Object = MibTableColumn
rlDhcpSrvConfParamsRowStatus = _RlDhcpSrvConfParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 47, 1, 14),
    _RlDhcpSrvConfParamsRowStatus_Type()
)
rlDhcpSrvConfParamsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvConfParamsRowStatus.setStatus("current")
_RlDhcpSrvNumOfNetworkPools_Type = Unsigned32
_RlDhcpSrvNumOfNetworkPools_Object = MibScalar
rlDhcpSrvNumOfNetworkPools = _RlDhcpSrvNumOfNetworkPools_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 48),
    _RlDhcpSrvNumOfNetworkPools_Type()
)
rlDhcpSrvNumOfNetworkPools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvNumOfNetworkPools.setStatus("current")
_RlDhcpSrvNumOfExcludedPools_Type = Unsigned32
_RlDhcpSrvNumOfExcludedPools_Object = MibScalar
rlDhcpSrvNumOfExcludedPools = _RlDhcpSrvNumOfExcludedPools_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 49),
    _RlDhcpSrvNumOfExcludedPools_Type()
)
rlDhcpSrvNumOfExcludedPools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvNumOfExcludedPools.setStatus("current")
_RlDhcpSrvNumOfHostPools_Type = Unsigned32
_RlDhcpSrvNumOfHostPools_Object = MibScalar
rlDhcpSrvNumOfHostPools = _RlDhcpSrvNumOfHostPools_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 50),
    _RlDhcpSrvNumOfHostPools_Type()
)
rlDhcpSrvNumOfHostPools.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvNumOfHostPools.setStatus("current")
_RlDhcpSrvNumOfDynamicEntries_Type = Unsigned32
_RlDhcpSrvNumOfDynamicEntries_Object = MibScalar
rlDhcpSrvNumOfDynamicEntries = _RlDhcpSrvNumOfDynamicEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 51),
    _RlDhcpSrvNumOfDynamicEntries_Type()
)
rlDhcpSrvNumOfDynamicEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvNumOfDynamicEntries.setStatus("current")
_RlDhcpSrvNumOfUsedEntries_Type = Unsigned32
_RlDhcpSrvNumOfUsedEntries_Object = MibScalar
rlDhcpSrvNumOfUsedEntries = _RlDhcpSrvNumOfUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 52),
    _RlDhcpSrvNumOfUsedEntries_Type()
)
rlDhcpSrvNumOfUsedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvNumOfUsedEntries.setStatus("current")
_RlDhcpSrvNumOfPreAllocatedEntries_Type = Unsigned32
_RlDhcpSrvNumOfPreAllocatedEntries_Object = MibScalar
rlDhcpSrvNumOfPreAllocatedEntries = _RlDhcpSrvNumOfPreAllocatedEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 53),
    _RlDhcpSrvNumOfPreAllocatedEntries_Type()
)
rlDhcpSrvNumOfPreAllocatedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvNumOfPreAllocatedEntries.setStatus("current")
_RlDhcpSrvNumOfExpiredEntries_Type = Unsigned32
_RlDhcpSrvNumOfExpiredEntries_Object = MibScalar
rlDhcpSrvNumOfExpiredEntries = _RlDhcpSrvNumOfExpiredEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 54),
    _RlDhcpSrvNumOfExpiredEntries_Type()
)
rlDhcpSrvNumOfExpiredEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvNumOfExpiredEntries.setStatus("current")
_RlDhcpSrvNumOfDeclinedEntries_Type = Unsigned32
_RlDhcpSrvNumOfDeclinedEntries_Object = MibScalar
rlDhcpSrvNumOfDeclinedEntries = _RlDhcpSrvNumOfDeclinedEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 55),
    _RlDhcpSrvNumOfDeclinedEntries_Type()
)
rlDhcpSrvNumOfDeclinedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvNumOfDeclinedEntries.setStatus("current")
_RlDhcpSrvNumOfAutomaticEntries_Type = Unsigned32
_RlDhcpSrvNumOfAutomaticEntries_Object = MibScalar
rlDhcpSrvNumOfAutomaticEntries = _RlDhcpSrvNumOfAutomaticEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 56),
    _RlDhcpSrvNumOfAutomaticEntries_Type()
)
rlDhcpSrvNumOfAutomaticEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvNumOfAutomaticEntries.setStatus("current")
_RlDhcpSrvOptionParamsTable_Object = MibTable
rlDhcpSrvOptionParamsTable = _RlDhcpSrvOptionParamsTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 57)
)
if mibBuilder.loadTexts:
    rlDhcpSrvOptionParamsTable.setStatus("current")
_RlDhcpSrvOptionParamsEntry_Object = MibTableRow
rlDhcpSrvOptionParamsEntry = _RlDhcpSrvOptionParamsEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 57, 1)
)
rlDhcpSrvOptionParamsEntry.setIndexNames(
    (0, "CISCOSB-DHCP-MIB", "rlDhcpSrvOptionParamsName"),
    (0, "CISCOSB-DHCP-MIB", "rlDhcpSrvOptionParamsCode"),
)
if mibBuilder.loadTexts:
    rlDhcpSrvOptionParamsEntry.setStatus("current")


class _RlDhcpSrvOptionParamsName_Type(DisplayString):
    """Custom type rlDhcpSrvOptionParamsName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_RlDhcpSrvOptionParamsName_Type.__name__ = "DisplayString"
_RlDhcpSrvOptionParamsName_Object = MibTableColumn
rlDhcpSrvOptionParamsName = _RlDhcpSrvOptionParamsName_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 57, 1, 1),
    _RlDhcpSrvOptionParamsName_Type()
)
rlDhcpSrvOptionParamsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvOptionParamsName.setStatus("current")


class _RlDhcpSrvOptionParamsCode_Type(Unsigned32):
    """Custom type rlDhcpSrvOptionParamsCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RlDhcpSrvOptionParamsCode_Type.__name__ = "Unsigned32"
_RlDhcpSrvOptionParamsCode_Object = MibTableColumn
rlDhcpSrvOptionParamsCode = _RlDhcpSrvOptionParamsCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 57, 1, 2),
    _RlDhcpSrvOptionParamsCode_Type()
)
rlDhcpSrvOptionParamsCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvOptionParamsCode.setStatus("current")
_RlDhcpSrvOptionParamsType_Type = RlDhcpSrvOptionTypeEnum
_RlDhcpSrvOptionParamsType_Object = MibTableColumn
rlDhcpSrvOptionParamsType = _RlDhcpSrvOptionParamsType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 57, 1, 3),
    _RlDhcpSrvOptionParamsType_Type()
)
rlDhcpSrvOptionParamsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvOptionParamsType.setStatus("current")
_RlDhcpSrvOptionParamsOrigString_Type = DisplayString
_RlDhcpSrvOptionParamsOrigString_Object = MibTableColumn
rlDhcpSrvOptionParamsOrigString = _RlDhcpSrvOptionParamsOrigString_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 57, 1, 4),
    _RlDhcpSrvOptionParamsOrigString_Type()
)
rlDhcpSrvOptionParamsOrigString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvOptionParamsOrigString.setStatus("current")
_RlDhcpSrvOptionParamsDescription_Type = DisplayString
_RlDhcpSrvOptionParamsDescription_Object = MibTableColumn
rlDhcpSrvOptionParamsDescription = _RlDhcpSrvOptionParamsDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 57, 1, 5),
    _RlDhcpSrvOptionParamsDescription_Type()
)
rlDhcpSrvOptionParamsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvOptionParamsDescription.setStatus("current")
_RlDhcpSrvOptionParamsRowStatus_Type = RowStatus
_RlDhcpSrvOptionParamsRowStatus_Object = MibTableColumn
rlDhcpSrvOptionParamsRowStatus = _RlDhcpSrvOptionParamsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 57, 1, 6),
    _RlDhcpSrvOptionParamsRowStatus_Type()
)
rlDhcpSrvOptionParamsRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlDhcpSrvOptionParamsRowStatus.setStatus("current")
_RlDhcpSrvAuxOptionTable_Object = MibTable
rlDhcpSrvAuxOptionTable = _RlDhcpSrvAuxOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 58)
)
if mibBuilder.loadTexts:
    rlDhcpSrvAuxOptionTable.setStatus("current")
_RlDhcpSrvAuxOptionEntry_Object = MibTableRow
rlDhcpSrvAuxOptionEntry = _RlDhcpSrvAuxOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 58, 1)
)
rlDhcpSrvAuxOptionEntry.setIndexNames(
    (0, "CISCOSB-DHCP-MIB", "rlDhcpSrvAuxOptionCode"),
    (0, "CISCOSB-DHCP-MIB", "rlDhcpSrvAuxOptionType"),
)
if mibBuilder.loadTexts:
    rlDhcpSrvAuxOptionEntry.setStatus("current")


class _RlDhcpSrvAuxOptionCode_Type(Unsigned32):
    """Custom type rlDhcpSrvAuxOptionCode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_RlDhcpSrvAuxOptionCode_Type.__name__ = "Unsigned32"
_RlDhcpSrvAuxOptionCode_Object = MibTableColumn
rlDhcpSrvAuxOptionCode = _RlDhcpSrvAuxOptionCode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 58, 1, 1),
    _RlDhcpSrvAuxOptionCode_Type()
)
rlDhcpSrvAuxOptionCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvAuxOptionCode.setStatus("current")
_RlDhcpSrvAuxOptionType_Type = RlDhcpSrvOptionTypeEnum
_RlDhcpSrvAuxOptionType_Object = MibTableColumn
rlDhcpSrvAuxOptionType = _RlDhcpSrvAuxOptionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 58, 1, 2),
    _RlDhcpSrvAuxOptionType_Type()
)
rlDhcpSrvAuxOptionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvAuxOptionType.setStatus("current")
_RlDhcpSrvAuxOptionMinVal_Type = Unsigned32
_RlDhcpSrvAuxOptionMinVal_Object = MibTableColumn
rlDhcpSrvAuxOptionMinVal = _RlDhcpSrvAuxOptionMinVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 58, 1, 3),
    _RlDhcpSrvAuxOptionMinVal_Type()
)
rlDhcpSrvAuxOptionMinVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvAuxOptionMinVal.setStatus("current")
_RlDhcpSrvAuxOptionMaxVal_Type = Unsigned32
_RlDhcpSrvAuxOptionMaxVal_Object = MibTableColumn
rlDhcpSrvAuxOptionMaxVal = _RlDhcpSrvAuxOptionMaxVal_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 38, 58, 1, 4),
    _RlDhcpSrvAuxOptionMaxVal_Type()
)
rlDhcpSrvAuxOptionMaxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlDhcpSrvAuxOptionMaxVal.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-DHCP-MIB",
    **{"RlDhcpSrvOptionTypeEnum": RlDhcpSrvOptionTypeEnum,
       "rsDHCP": rsDHCP,
       "rsDhcpMibVersion": rsDhcpMibVersion,
       "rlDhcpRelayMaximalNumberOfNonIpVlans": rlDhcpRelayMaximalNumberOfNonIpVlans,
       "rlDhcpRelayCurrentNumberOfNonIpVlans": rlDhcpRelayCurrentNumberOfNonIpVlans,
       "rlDhcpRelayEnable": rlDhcpRelayEnable,
       "rlDhcpRelayExists": rlDhcpRelayExists,
       "rlDhcpRelayNextServerTable": rlDhcpRelayNextServerTable,
       "rlDhcpRelayNextServerEntry": rlDhcpRelayNextServerEntry,
       "rlDhcpRelayNextServerIpAddr": rlDhcpRelayNextServerIpAddr,
       "rlDhcpRelayNextServerSecThreshold": rlDhcpRelayNextServerSecThreshold,
       "rlDhcpRelayNextServerRowStatus": rlDhcpRelayNextServerRowStatus,
       "rlDhcpRelayInterfaceTable": rlDhcpRelayInterfaceTable,
       "rlDhcpRelayInterfaceEntry": rlDhcpRelayInterfaceEntry,
       "rlDhcpRelayInterfaceIfindex": rlDhcpRelayInterfaceIfindex,
       "rlDhcpRelayInterfaceUseGiaddr": rlDhcpRelayInterfaceUseGiaddr,
       "rlDhcpRelayInterfaceRowStatus": rlDhcpRelayInterfaceRowStatus,
       "rlDhcpRelayInterfaceListTable": rlDhcpRelayInterfaceListTable,
       "rlDhcpRelayInterfaceListEntry": rlDhcpRelayInterfaceListEntry,
       "rlDhcpRelayInterfaceListIndex": rlDhcpRelayInterfaceListIndex,
       "rlDhcpRelayInterfaceListPortList": rlDhcpRelayInterfaceListPortList,
       "rlDhcpRelayInterfaceListVlanId1To1024": rlDhcpRelayInterfaceListVlanId1To1024,
       "rlDhcpRelayInterfaceListVlanId1025To2048": rlDhcpRelayInterfaceListVlanId1025To2048,
       "rlDhcpRelayInterfaceListVlanId2049To3072": rlDhcpRelayInterfaceListVlanId2049To3072,
       "rlDhcpRelayInterfaceListVlanId3073To4094": rlDhcpRelayInterfaceListVlanId3073To4094,
       "rlDhcpSrvEnable": rlDhcpSrvEnable,
       "rlDhcpSrvExists": rlDhcpSrvExists,
       "rlDhcpSrvDbLocation": rlDhcpSrvDbLocation,
       "rlDhcpSrvMaxNumOfClients": rlDhcpSrvMaxNumOfClients,
       "rlDhcpSrvDbNumOfActiveEntries": rlDhcpSrvDbNumOfActiveEntries,
       "rlDhcpSrvDbErase": rlDhcpSrvDbErase,
       "rlDhcpSrvProbeEnable": rlDhcpSrvProbeEnable,
       "rlDhcpSrvProbeTimeout": rlDhcpSrvProbeTimeout,
       "rlDhcpSrvProbeRetries": rlDhcpSrvProbeRetries,
       "rlDhcpSrvDefaultNetworkPoolName": rlDhcpSrvDefaultNetworkPoolName,
       "rlDhcpSrvIpAddrTable": rlDhcpSrvIpAddrTable,
       "rlDhcpSrvIpAddrEntry": rlDhcpSrvIpAddrEntry,
       "rlDhcpSrvIpAddrIpAddr": rlDhcpSrvIpAddrIpAddr,
       "rlDhcpSrvIpAddrIpNetMask": rlDhcpSrvIpAddrIpNetMask,
       "rlDhcpSrvIpAddrIdentifier": rlDhcpSrvIpAddrIdentifier,
       "rlDhcpSrvIpAddrIdentifierType": rlDhcpSrvIpAddrIdentifierType,
       "rlDhcpSrvIpAddrClnHostName": rlDhcpSrvIpAddrClnHostName,
       "rlDhcpSrvIpAddrMechanism": rlDhcpSrvIpAddrMechanism,
       "rlDhcpSrvIpAddrAgeTime": rlDhcpSrvIpAddrAgeTime,
       "rlDhcpSrvIpAddrPoolName": rlDhcpSrvIpAddrPoolName,
       "rlDhcpSrvIpAddrConfParamsName": rlDhcpSrvIpAddrConfParamsName,
       "rlDhcpSrvIpAddrRowStatus": rlDhcpSrvIpAddrRowStatus,
       "rlDhcpSrvIpAddrLeaseTime": rlDhcpSrvIpAddrLeaseTime,
       "rlDhcpSrvIpAddrState": rlDhcpSrvIpAddrState,
       "rlDhcpSrvIpAddrOptionParamsName": rlDhcpSrvIpAddrOptionParamsName,
       "rlDhcpSrvDynamicTable": rlDhcpSrvDynamicTable,
       "rlDhcpSrvDynamicEntry": rlDhcpSrvDynamicEntry,
       "rlDhcpSrvDynamicPoolName": rlDhcpSrvDynamicPoolName,
       "rlDhcpSrvDynamicIpAddrFrom": rlDhcpSrvDynamicIpAddrFrom,
       "rlDhcpSrvDynamicIpAddrTo": rlDhcpSrvDynamicIpAddrTo,
       "rlDhcpSrvDynamicIpNetMask": rlDhcpSrvDynamicIpNetMask,
       "rlDhcpSrvDynamicLeaseTime": rlDhcpSrvDynamicLeaseTime,
       "rlDhcpSrvDynamicProbeEnable": rlDhcpSrvDynamicProbeEnable,
       "rlDhcpSrvDynamicTotalNumOfAddr": rlDhcpSrvDynamicTotalNumOfAddr,
       "rlDhcpSrvDynamicFreeNumOfAddr": rlDhcpSrvDynamicFreeNumOfAddr,
       "rlDhcpSrvDynamicConfParamsName": rlDhcpSrvDynamicConfParamsName,
       "rlDhcpSrvDynamicRowStatus": rlDhcpSrvDynamicRowStatus,
       "rlDhcpSrvDynamicAvailableNumOfAddr": rlDhcpSrvDynamicAvailableNumOfAddr,
       "rlDhcpSrvDynamicNumOfPreallocatedAddr": rlDhcpSrvDynamicNumOfPreallocatedAddr,
       "rlDhcpSrvDynamicNumOfValidAddr": rlDhcpSrvDynamicNumOfValidAddr,
       "rlDhcpSrvDynamicNumOfExpiredAddr": rlDhcpSrvDynamicNumOfExpiredAddr,
       "rlDhcpSrvDynamicNumOfDeclinedAddr": rlDhcpSrvDynamicNumOfDeclinedAddr,
       "rlDhcpSrvDynamicOptionParamsName": rlDhcpSrvDynamicOptionParamsName,
       "rlDhcpSrvConfParamsTable": rlDhcpSrvConfParamsTable,
       "rlDhcpSrvConfParamsEntry": rlDhcpSrvConfParamsEntry,
       "rlDhcpSrvConfParamsName": rlDhcpSrvConfParamsName,
       "rlDhcpSrvConfParamsNextServerIp": rlDhcpSrvConfParamsNextServerIp,
       "rlDhcpSrvConfParamsNextServerName": rlDhcpSrvConfParamsNextServerName,
       "rlDhcpSrvConfParamsBootfileName": rlDhcpSrvConfParamsBootfileName,
       "rlDhcpSrvConfParamsRoutersList": rlDhcpSrvConfParamsRoutersList,
       "rlDhcpSrvConfParamsTimeSrvList": rlDhcpSrvConfParamsTimeSrvList,
       "rlDhcpSrvConfParamsDnsList": rlDhcpSrvConfParamsDnsList,
       "rlDhcpSrvConfParamsDomainName": rlDhcpSrvConfParamsDomainName,
       "rlDhcpSrvConfParamsNetbiosNameList": rlDhcpSrvConfParamsNetbiosNameList,
       "rlDhcpSrvConfParamsNetbiosNodeType": rlDhcpSrvConfParamsNetbiosNodeType,
       "rlDhcpSrvConfParamsCommunity": rlDhcpSrvConfParamsCommunity,
       "rlDhcpSrvConfParamsNmsIp": rlDhcpSrvConfParamsNmsIp,
       "rlDhcpSrvConfParamsOptionsList": rlDhcpSrvConfParamsOptionsList,
       "rlDhcpSrvConfParamsRowStatus": rlDhcpSrvConfParamsRowStatus,
       "rlDhcpSrvNumOfNetworkPools": rlDhcpSrvNumOfNetworkPools,
       "rlDhcpSrvNumOfExcludedPools": rlDhcpSrvNumOfExcludedPools,
       "rlDhcpSrvNumOfHostPools": rlDhcpSrvNumOfHostPools,
       "rlDhcpSrvNumOfDynamicEntries": rlDhcpSrvNumOfDynamicEntries,
       "rlDhcpSrvNumOfUsedEntries": rlDhcpSrvNumOfUsedEntries,
       "rlDhcpSrvNumOfPreAllocatedEntries": rlDhcpSrvNumOfPreAllocatedEntries,
       "rlDhcpSrvNumOfExpiredEntries": rlDhcpSrvNumOfExpiredEntries,
       "rlDhcpSrvNumOfDeclinedEntries": rlDhcpSrvNumOfDeclinedEntries,
       "rlDhcpSrvNumOfAutomaticEntries": rlDhcpSrvNumOfAutomaticEntries,
       "rlDhcpSrvOptionParamsTable": rlDhcpSrvOptionParamsTable,
       "rlDhcpSrvOptionParamsEntry": rlDhcpSrvOptionParamsEntry,
       "rlDhcpSrvOptionParamsName": rlDhcpSrvOptionParamsName,
       "rlDhcpSrvOptionParamsCode": rlDhcpSrvOptionParamsCode,
       "rlDhcpSrvOptionParamsType": rlDhcpSrvOptionParamsType,
       "rlDhcpSrvOptionParamsOrigString": rlDhcpSrvOptionParamsOrigString,
       "rlDhcpSrvOptionParamsDescription": rlDhcpSrvOptionParamsDescription,
       "rlDhcpSrvOptionParamsRowStatus": rlDhcpSrvOptionParamsRowStatus,
       "rlDhcpSrvAuxOptionTable": rlDhcpSrvAuxOptionTable,
       "rlDhcpSrvAuxOptionEntry": rlDhcpSrvAuxOptionEntry,
       "rlDhcpSrvAuxOptionCode": rlDhcpSrvAuxOptionCode,
       "rlDhcpSrvAuxOptionType": rlDhcpSrvAuxOptionType,
       "rlDhcpSrvAuxOptionMinVal": rlDhcpSrvAuxOptionMinVal,
       "rlDhcpSrvAuxOptionMaxVal": rlDhcpSrvAuxOptionMaxVal}
)
