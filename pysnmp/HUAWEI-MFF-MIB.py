# SNMP MIB module (HUAWEI-MFF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HUAWEI-MFF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:04:56 2024
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

(hwDatacomm,) = mibBuilder.importSymbols(
    "HUAWEI-MIB",
    "hwDatacomm")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hwMffMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170)
)
hwMffMIB.setRevisions(
        ("2008-07-02 18:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HwMffObjects_ObjectIdentity = ObjectIdentity
hwMffObjects = _HwMffObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1)
)
_HwMffGlobal_Type = EnabledStatus
_HwMffGlobal_Object = MibScalar
hwMffGlobal = _HwMffGlobal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 1),
    _HwMffGlobal_Type()
)
hwMffGlobal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwMffGlobal.setStatus("current")
_HwMffVlanCfgTable_Object = MibTable
hwMffVlanCfgTable = _HwMffVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 2)
)
if mibBuilder.loadTexts:
    hwMffVlanCfgTable.setStatus("current")
_HwMffVlanCfgEntry_Object = MibTableRow
hwMffVlanCfgEntry = _HwMffVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 2, 1)
)
hwMffVlanCfgEntry.setIndexNames(
    (0, "HUAWEI-MFF-MIB", "hwMffVlanIndex"),
)
if mibBuilder.loadTexts:
    hwMffVlanCfgEntry.setStatus("current")
_HwMffVlanIndex_Type = VlanId
_HwMffVlanIndex_Object = MibTableColumn
hwMffVlanIndex = _HwMffVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 2, 1, 1),
    _HwMffVlanIndex_Type()
)
hwMffVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMffVlanIndex.setStatus("current")
_HwMffStaticGatewayIpAddr_Type = IpAddress
_HwMffStaticGatewayIpAddr_Object = MibTableColumn
hwMffStaticGatewayIpAddr = _HwMffStaticGatewayIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 2, 1, 2),
    _HwMffStaticGatewayIpAddr_Type()
)
hwMffStaticGatewayIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMffStaticGatewayIpAddr.setStatus("current")


class _HwMffGatewayDetect_Type(EnabledStatus):
    """Custom type hwMffGatewayDetect based on EnabledStatus"""


_HwMffGatewayDetect_Object = MibTableColumn
hwMffGatewayDetect = _HwMffGatewayDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 2, 1, 3),
    _HwMffGatewayDetect_Type()
)
hwMffGatewayDetect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMffGatewayDetect.setStatus("current")
_HwMffVlanCfgRowStatus_Type = RowStatus
_HwMffVlanCfgRowStatus_Object = MibTableColumn
hwMffVlanCfgRowStatus = _HwMffVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 2, 1, 100),
    _HwMffVlanCfgRowStatus_Type()
)
hwMffVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMffVlanCfgRowStatus.setStatus("current")
_HwMffNetworkPortTable_Object = MibTable
hwMffNetworkPortTable = _HwMffNetworkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 3)
)
if mibBuilder.loadTexts:
    hwMffNetworkPortTable.setStatus("current")
_HwMffNetworkPortEntry_Object = MibTableRow
hwMffNetworkPortEntry = _HwMffNetworkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 3, 1)
)
hwMffNetworkPortEntry.setIndexNames(
    (0, "HUAWEI-MFF-MIB", "hwMffPortIndex"),
)
if mibBuilder.loadTexts:
    hwMffNetworkPortEntry.setStatus("current")


class _HwMffPortIndex_Type(Integer32):
    """Custom type hwMffPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMffPortIndex_Type.__name__ = "Integer32"
_HwMffPortIndex_Object = MibTableColumn
hwMffPortIndex = _HwMffPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 3, 1, 1),
    _HwMffPortIndex_Type()
)
hwMffPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMffPortIndex.setStatus("current")
_HwMffNetworkPortRowStatus_Type = RowStatus
_HwMffNetworkPortRowStatus_Object = MibTableColumn
hwMffNetworkPortRowStatus = _HwMffNetworkPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 3, 1, 100),
    _HwMffNetworkPortRowStatus_Type()
)
hwMffNetworkPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMffNetworkPortRowStatus.setStatus("current")
_HwMffServerCfgTable_Object = MibTable
hwMffServerCfgTable = _HwMffServerCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 4)
)
if mibBuilder.loadTexts:
    hwMffServerCfgTable.setStatus("current")
_HwMffServerCfgEntry_Object = MibTableRow
hwMffServerCfgEntry = _HwMffServerCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 4, 1)
)
hwMffServerCfgEntry.setIndexNames(
    (0, "HUAWEI-MFF-MIB", "hwMffServerVlanIndex"),
    (0, "HUAWEI-MFF-MIB", "hwMffIpIndex"),
)
if mibBuilder.loadTexts:
    hwMffServerCfgEntry.setStatus("current")
_HwMffServerVlanIndex_Type = VlanId
_HwMffServerVlanIndex_Object = MibTableColumn
hwMffServerVlanIndex = _HwMffServerVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 4, 1, 1),
    _HwMffServerVlanIndex_Type()
)
hwMffServerVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMffServerVlanIndex.setStatus("current")
_HwMffIpIndex_Type = IpAddress
_HwMffIpIndex_Object = MibTableColumn
hwMffIpIndex = _HwMffIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 4, 1, 2),
    _HwMffIpIndex_Type()
)
hwMffIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMffIpIndex.setStatus("current")
_HwMffServerIpRowStatus_Type = RowStatus
_HwMffServerIpRowStatus_Object = MibTableColumn
hwMffServerIpRowStatus = _HwMffServerIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 4, 1, 100),
    _HwMffServerIpRowStatus_Type()
)
hwMffServerIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMffServerIpRowStatus.setStatus("current")
_HwMffUserGatewayTable_Object = MibTable
hwMffUserGatewayTable = _HwMffUserGatewayTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 5)
)
if mibBuilder.loadTexts:
    hwMffUserGatewayTable.setStatus("current")
_HwMffUserGatewayEntry_Object = MibTableRow
hwMffUserGatewayEntry = _HwMffUserGatewayEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 5, 1)
)
hwMffUserGatewayEntry.setIndexNames(
    (0, "HUAWEI-MFF-MIB", "hwMffUserGatewayVlanIndex"),
    (0, "HUAWEI-MFF-MIB", "hwMffUserIpIndex"),
    (0, "HUAWEI-MFF-MIB", "hwMffGatewayIpIndex"),
)
if mibBuilder.loadTexts:
    hwMffUserGatewayEntry.setStatus("current")
_HwMffUserGatewayVlanIndex_Type = VlanId
_HwMffUserGatewayVlanIndex_Object = MibTableColumn
hwMffUserGatewayVlanIndex = _HwMffUserGatewayVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 5, 1, 1),
    _HwMffUserGatewayVlanIndex_Type()
)
hwMffUserGatewayVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMffUserGatewayVlanIndex.setStatus("current")
_HwMffUserIpIndex_Type = IpAddress
_HwMffUserIpIndex_Object = MibTableColumn
hwMffUserIpIndex = _HwMffUserIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 5, 1, 2),
    _HwMffUserIpIndex_Type()
)
hwMffUserIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMffUserIpIndex.setStatus("current")
_HwMffGatewayIpIndex_Type = IpAddress
_HwMffGatewayIpIndex_Object = MibTableColumn
hwMffGatewayIpIndex = _HwMffGatewayIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 5, 1, 3),
    _HwMffGatewayIpIndex_Type()
)
hwMffGatewayIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMffGatewayIpIndex.setStatus("current")
_HwMffUserMacAddr_Type = MacAddress
_HwMffUserMacAddr_Object = MibTableColumn
hwMffUserMacAddr = _HwMffUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 5, 1, 20),
    _HwMffUserMacAddr_Type()
)
hwMffUserMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMffUserMacAddr.setStatus("current")
_HwMffGatewayMacAddr_Type = MacAddress
_HwMffGatewayMacAddr_Object = MibTableColumn
hwMffGatewayMacAddr = _HwMffGatewayMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 5, 1, 21),
    _HwMffGatewayMacAddr_Type()
)
hwMffGatewayMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwMffGatewayMacAddr.setStatus("current")
_HwMffModUserTable_Object = MibTable
hwMffModUserTable = _HwMffModUserTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 6)
)
if mibBuilder.loadTexts:
    hwMffModUserTable.setStatus("current")
_HwMffModUserEntry_Object = MibTableRow
hwMffModUserEntry = _HwMffModUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 6, 1)
)
hwMffModUserEntry.setIndexNames(
    (0, "HUAWEI-MFF-MIB", "hwMffModUserVlanIndex"),
    (0, "HUAWEI-MFF-MIB", "hwMffModUserIpAddrIndex"),
)
if mibBuilder.loadTexts:
    hwMffModUserEntry.setStatus("current")
_HwMffModUserVlanIndex_Type = VlanId
_HwMffModUserVlanIndex_Object = MibTableColumn
hwMffModUserVlanIndex = _HwMffModUserVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 6, 1, 1),
    _HwMffModUserVlanIndex_Type()
)
hwMffModUserVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMffModUserVlanIndex.setStatus("current")
_HwMffModUserIpAddrIndex_Type = IpAddress
_HwMffModUserIpAddrIndex_Object = MibTableColumn
hwMffModUserIpAddrIndex = _HwMffModUserIpAddrIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 6, 1, 2),
    _HwMffModUserIpAddrIndex_Type()
)
hwMffModUserIpAddrIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwMffModUserIpAddrIndex.setStatus("current")
_HwMffModUserMacAddr_Type = MacAddress
_HwMffModUserMacAddr_Object = MibTableColumn
hwMffModUserMacAddr = _HwMffModUserMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 6, 1, 3),
    _HwMffModUserMacAddr_Type()
)
hwMffModUserMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMffModUserMacAddr.setStatus("current")


class _HwMffModUserPort_Type(Integer32):
    """Custom type hwMffModUserPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwMffModUserPort_Type.__name__ = "Integer32"
_HwMffModUserPort_Object = MibTableColumn
hwMffModUserPort = _HwMffModUserPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 6, 1, 4),
    _HwMffModUserPort_Type()
)
hwMffModUserPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMffModUserPort.setStatus("current")
_HwMffModUserGatewayIp_Type = IpAddress
_HwMffModUserGatewayIp_Object = MibTableColumn
hwMffModUserGatewayIp = _HwMffModUserGatewayIp_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 6, 1, 5),
    _HwMffModUserGatewayIp_Type()
)
hwMffModUserGatewayIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMffModUserGatewayIp.setStatus("current")
_HwMffModUserGatewayMacAddr_Type = MacAddress
_HwMffModUserGatewayMacAddr_Object = MibTableColumn
hwMffModUserGatewayMacAddr = _HwMffModUserGatewayMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 6, 1, 6),
    _HwMffModUserGatewayMacAddr_Type()
)
hwMffModUserGatewayMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMffModUserGatewayMacAddr.setStatus("current")
_HwMffModUserRowStatus_Type = RowStatus
_HwMffModUserRowStatus_Object = MibTableColumn
hwMffModUserRowStatus = _HwMffModUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 1, 6, 1, 100),
    _HwMffModUserRowStatus_Type()
)
hwMffModUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hwMffModUserRowStatus.setStatus("current")
_HwMffConformance_ObjectIdentity = ObjectIdentity
hwMffConformance = _HwMffConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 2)
)
_HwMffCompliances_ObjectIdentity = ObjectIdentity
hwMffCompliances = _HwMffCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 2, 1)
)
_HwMffMIBGroups_ObjectIdentity = ObjectIdentity
hwMffMIBGroups = _HwMffMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 2, 2)
)

# Managed Objects groups

hwMffGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 2, 2, 1)
)
hwMffGlobalGroup.setObjects(
    ("HUAWEI-MFF-MIB", "hwMffGlobal")
)
if mibBuilder.loadTexts:
    hwMffGlobalGroup.setStatus("current")

hwMffVlanCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 2, 2, 2)
)
hwMffVlanCfgGroup.setObjects(
      *(("HUAWEI-MFF-MIB", "hwMffStaticGatewayIpAddr"),
        ("HUAWEI-MFF-MIB", "hwMffGatewayDetect"),
        ("HUAWEI-MFF-MIB", "hwMffVlanCfgRowStatus"))
)
if mibBuilder.loadTexts:
    hwMffVlanCfgGroup.setStatus("current")

hwMffNetworkPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 2, 2, 3)
)
hwMffNetworkPortGroup.setObjects(
    ("HUAWEI-MFF-MIB", "hwMffNetworkPortRowStatus")
)
if mibBuilder.loadTexts:
    hwMffNetworkPortGroup.setStatus("current")

hwMffServerCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 2, 2, 4)
)
hwMffServerCfgGroup.setObjects(
    ("HUAWEI-MFF-MIB", "hwMffServerIpRowStatus")
)
if mibBuilder.loadTexts:
    hwMffServerCfgGroup.setStatus("current")

hwMffUserGatewayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 2, 2, 5)
)
hwMffUserGatewayGroup.setObjects(
      *(("HUAWEI-MFF-MIB", "hwMffUserMacAddr"),
        ("HUAWEI-MFF-MIB", "hwMffGatewayMacAddr"))
)
if mibBuilder.loadTexts:
    hwMffUserGatewayGroup.setStatus("current")

hwMffModUserGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 2, 2, 6)
)
hwMffModUserGroup.setObjects(
      *(("HUAWEI-MFF-MIB", "hwMffModUserMacAddr"),
        ("HUAWEI-MFF-MIB", "hwMffModUserPort"),
        ("HUAWEI-MFF-MIB", "hwMffModUserGatewayIp"),
        ("HUAWEI-MFF-MIB", "hwMffModUserGatewayMacAddr"),
        ("HUAWEI-MFF-MIB", "hwMffModUserRowStatus"))
)
if mibBuilder.loadTexts:
    hwMffModUserGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hwMffCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 5, 25, 170, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwMffCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-MFF-MIB",
    **{"hwMffMIB": hwMffMIB,
       "hwMffObjects": hwMffObjects,
       "hwMffGlobal": hwMffGlobal,
       "hwMffVlanCfgTable": hwMffVlanCfgTable,
       "hwMffVlanCfgEntry": hwMffVlanCfgEntry,
       "hwMffVlanIndex": hwMffVlanIndex,
       "hwMffStaticGatewayIpAddr": hwMffStaticGatewayIpAddr,
       "hwMffGatewayDetect": hwMffGatewayDetect,
       "hwMffVlanCfgRowStatus": hwMffVlanCfgRowStatus,
       "hwMffNetworkPortTable": hwMffNetworkPortTable,
       "hwMffNetworkPortEntry": hwMffNetworkPortEntry,
       "hwMffPortIndex": hwMffPortIndex,
       "hwMffNetworkPortRowStatus": hwMffNetworkPortRowStatus,
       "hwMffServerCfgTable": hwMffServerCfgTable,
       "hwMffServerCfgEntry": hwMffServerCfgEntry,
       "hwMffServerVlanIndex": hwMffServerVlanIndex,
       "hwMffIpIndex": hwMffIpIndex,
       "hwMffServerIpRowStatus": hwMffServerIpRowStatus,
       "hwMffUserGatewayTable": hwMffUserGatewayTable,
       "hwMffUserGatewayEntry": hwMffUserGatewayEntry,
       "hwMffUserGatewayVlanIndex": hwMffUserGatewayVlanIndex,
       "hwMffUserIpIndex": hwMffUserIpIndex,
       "hwMffGatewayIpIndex": hwMffGatewayIpIndex,
       "hwMffUserMacAddr": hwMffUserMacAddr,
       "hwMffGatewayMacAddr": hwMffGatewayMacAddr,
       "hwMffModUserTable": hwMffModUserTable,
       "hwMffModUserEntry": hwMffModUserEntry,
       "hwMffModUserVlanIndex": hwMffModUserVlanIndex,
       "hwMffModUserIpAddrIndex": hwMffModUserIpAddrIndex,
       "hwMffModUserMacAddr": hwMffModUserMacAddr,
       "hwMffModUserPort": hwMffModUserPort,
       "hwMffModUserGatewayIp": hwMffModUserGatewayIp,
       "hwMffModUserGatewayMacAddr": hwMffModUserGatewayMacAddr,
       "hwMffModUserRowStatus": hwMffModUserRowStatus,
       "hwMffConformance": hwMffConformance,
       "hwMffCompliances": hwMffCompliances,
       "hwMffCompliance": hwMffCompliance,
       "hwMffMIBGroups": hwMffMIBGroups,
       "hwMffGlobalGroup": hwMffGlobalGroup,
       "hwMffVlanCfgGroup": hwMffVlanCfgGroup,
       "hwMffNetworkPortGroup": hwMffNetworkPortGroup,
       "hwMffServerCfgGroup": hwMffServerCfgGroup,
       "hwMffUserGatewayGroup": hwMffUserGatewayGroup,
       "hwMffModUserGroup": hwMffModUserGroup}
)
