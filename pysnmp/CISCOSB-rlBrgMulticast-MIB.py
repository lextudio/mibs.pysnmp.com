# SNMP MIB module (CISCOSB-rlBrgMulticast-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCOSB-rlBrgMulticast-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:15:16 2024
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

(MacAddress,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "MacAddress")

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "CISCOSB-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

(rlBrgMulticast,
 rndNotifications,
 switch001) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "rlBrgMulticast",
    "rndNotifications",
    "switch001")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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

rlMacMulticast = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55)
)
rlMacMulticast.setRevisions(
        ("2011-05-30 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IgmpVersion(Integer32, TextualConvention):
    status = "current"
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
        *(("none", 0),
          ("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )



class DynamicCmdType(Integer32, TextualConvention):
    status = "current"
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
        *(("addPorts", 2),
          ("createEntry", 0),
          ("deleteEntry", 1),
          ("deletePorts", 3))
    )



# MIB Managed Objects in the order of their OIDs

_RlMacMulticastEnable_Type = TruthValue
_RlMacMulticastEnable_Object = MibScalar
rlMacMulticastEnable = _RlMacMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 1),
    _RlMacMulticastEnable_Type()
)
rlMacMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacMulticastEnable.setStatus("current")
_RlIgmpSnoop_ObjectIdentity = ObjectIdentity
rlIgmpSnoop = _RlIgmpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2)
)
_RlIgmpSnoopMibVersion_Type = Integer32
_RlIgmpSnoopMibVersion_Object = MibScalar
rlIgmpSnoopMibVersion = _RlIgmpSnoopMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 1),
    _RlIgmpSnoopMibVersion_Type()
)
rlIgmpSnoopMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMibVersion.setStatus("current")
_RlIgmpSnoopEnable_Type = TruthValue
_RlIgmpSnoopEnable_Object = MibScalar
rlIgmpSnoopEnable = _RlIgmpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 2),
    _RlIgmpSnoopEnable_Type()
)
rlIgmpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopEnable.setStatus("current")


class _RlIgmpSnoopHostAgingTime_Type(Integer32):
    """Custom type rlIgmpSnoopHostAgingTime based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlIgmpSnoopHostAgingTime_Type.__name__ = "Integer32"
_RlIgmpSnoopHostAgingTime_Object = MibScalar
rlIgmpSnoopHostAgingTime = _RlIgmpSnoopHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 3),
    _RlIgmpSnoopHostAgingTime_Type()
)
rlIgmpSnoopHostAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopHostAgingTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpSnoopHostAgingTime.setUnits("seconds")


class _RlIgmpSnoopRouterAgingTime_Type(Integer32):
    """Custom type rlIgmpSnoopRouterAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlIgmpSnoopRouterAgingTime_Type.__name__ = "Integer32"
_RlIgmpSnoopRouterAgingTime_Object = MibScalar
rlIgmpSnoopRouterAgingTime = _RlIgmpSnoopRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 4),
    _RlIgmpSnoopRouterAgingTime_Type()
)
rlIgmpSnoopRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopRouterAgingTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpSnoopRouterAgingTime.setUnits("seconds")
_RlIgmpSnoopVlanTable_Object = MibTable
rlIgmpSnoopVlanTable = _RlIgmpSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7)
)
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanTable.setStatus("obsolete")
_RlIgmpSnoopVlanEntry_Object = MibTableRow
rlIgmpSnoopVlanEntry = _RlIgmpSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7, 1)
)
rlIgmpSnoopVlanEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpSnoopVlanTag"),
)
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanEntry.setStatus("obsolete")
_RlIgmpSnoopVlanTag_Type = Integer32
_RlIgmpSnoopVlanTag_Object = MibTableColumn
rlIgmpSnoopVlanTag = _RlIgmpSnoopVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7, 1, 1),
    _RlIgmpSnoopVlanTag_Type()
)
rlIgmpSnoopVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanTag.setStatus("obsolete")
_RlIgmpSnoopVlanEnable_Type = TruthValue
_RlIgmpSnoopVlanEnable_Object = MibTableColumn
rlIgmpSnoopVlanEnable = _RlIgmpSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7, 1, 2),
    _RlIgmpSnoopVlanEnable_Type()
)
rlIgmpSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanEnable.setStatus("obsolete")
_RlIgmpSnoopVlanRouterLearn_Type = TruthValue
_RlIgmpSnoopVlanRouterLearn_Object = MibTableColumn
rlIgmpSnoopVlanRouterLearn = _RlIgmpSnoopVlanRouterLearn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7, 1, 3),
    _RlIgmpSnoopVlanRouterLearn_Type()
)
rlIgmpSnoopVlanRouterLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanRouterLearn.setStatus("obsolete")


class _RlIgmpSnoopVlanHostTimeOut_Type(Integer32):
    """Custom type rlIgmpSnoopVlanHostTimeOut based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlIgmpSnoopVlanHostTimeOut_Type.__name__ = "Integer32"
_RlIgmpSnoopVlanHostTimeOut_Object = MibTableColumn
rlIgmpSnoopVlanHostTimeOut = _RlIgmpSnoopVlanHostTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7, 1, 4),
    _RlIgmpSnoopVlanHostTimeOut_Type()
)
rlIgmpSnoopVlanHostTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanHostTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanHostTimeOut.setUnits("seconds")


class _RlIgmpSnoopVlanQuerierTimeOut_Type(Integer32):
    """Custom type rlIgmpSnoopVlanQuerierTimeOut based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlIgmpSnoopVlanQuerierTimeOut_Type.__name__ = "Integer32"
_RlIgmpSnoopVlanQuerierTimeOut_Object = MibTableColumn
rlIgmpSnoopVlanQuerierTimeOut = _RlIgmpSnoopVlanQuerierTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7, 1, 5),
    _RlIgmpSnoopVlanQuerierTimeOut_Type()
)
rlIgmpSnoopVlanQuerierTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanQuerierTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanQuerierTimeOut.setUnits("seconds")


class _RlIgmpSnoopVlanRouterTimeOut_Type(Integer32):
    """Custom type rlIgmpSnoopVlanRouterTimeOut based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlIgmpSnoopVlanRouterTimeOut_Type.__name__ = "Integer32"
_RlIgmpSnoopVlanRouterTimeOut_Object = MibTableColumn
rlIgmpSnoopVlanRouterTimeOut = _RlIgmpSnoopVlanRouterTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7, 1, 6),
    _RlIgmpSnoopVlanRouterTimeOut_Type()
)
rlIgmpSnoopVlanRouterTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanRouterTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanRouterTimeOut.setUnits("seconds")


class _RlIgmpSnoopVlanLeaveTimeOut_Type(Integer32):
    """Custom type rlIgmpSnoopVlanLeaveTimeOut based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlIgmpSnoopVlanLeaveTimeOut_Type.__name__ = "Integer32"
_RlIgmpSnoopVlanLeaveTimeOut_Object = MibTableColumn
rlIgmpSnoopVlanLeaveTimeOut = _RlIgmpSnoopVlanLeaveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7, 1, 7),
    _RlIgmpSnoopVlanLeaveTimeOut_Type()
)
rlIgmpSnoopVlanLeaveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanLeaveTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanLeaveTimeOut.setUnits("seconds")
_RlIgmpSnoopVlanIgmpVersion_Type = IgmpVersion
_RlIgmpSnoopVlanIgmpVersion_Object = MibTableColumn
rlIgmpSnoopVlanIgmpVersion = _RlIgmpSnoopVlanIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7, 1, 8),
    _RlIgmpSnoopVlanIgmpVersion_Type()
)
rlIgmpSnoopVlanIgmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanIgmpVersion.setStatus("obsolete")
_RlIgmpSnoopVlanRouterPortlist_Type = PortList
_RlIgmpSnoopVlanRouterPortlist_Object = MibTableColumn
rlIgmpSnoopVlanRouterPortlist = _RlIgmpSnoopVlanRouterPortlist_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 7, 1, 9),
    _RlIgmpSnoopVlanRouterPortlist_Type()
)
rlIgmpSnoopVlanRouterPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanRouterPortlist.setStatus("obsolete")


class _RlIgmpSnoopIGMP224ReportsHandle_Type(Integer32):
    """Custom type rlIgmpSnoopIGMP224ReportsHandle based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("ignore", 2))
    )


_RlIgmpSnoopIGMP224ReportsHandle_Type.__name__ = "Integer32"
_RlIgmpSnoopIGMP224ReportsHandle_Object = MibScalar
rlIgmpSnoopIGMP224ReportsHandle = _RlIgmpSnoopIGMP224ReportsHandle_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 8),
    _RlIgmpSnoopIGMP224ReportsHandle_Type()
)
rlIgmpSnoopIGMP224ReportsHandle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopIGMP224ReportsHandle.setStatus("current")
_RlIgmpSnoopMulticastTvTable_Object = MibTable
rlIgmpSnoopMulticastTvTable = _RlIgmpSnoopMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 10)
)
if mibBuilder.loadTexts:
    rlIgmpSnoopMulticastTvTable.setStatus("current")
_RlIgmpSnoopMulticastTvEntry_Object = MibTableRow
rlIgmpSnoopMulticastTvEntry = _RlIgmpSnoopMulticastTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 10, 1)
)
rlIgmpSnoopMulticastTvEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpSnoopMulticastTvVID"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpSnoopMulticastTvGroup"),
)
if mibBuilder.loadTexts:
    rlIgmpSnoopMulticastTvEntry.setStatus("current")
_RlIgmpSnoopMulticastTvVID_Type = VlanIndex
_RlIgmpSnoopMulticastTvVID_Object = MibTableColumn
rlIgmpSnoopMulticastTvVID = _RlIgmpSnoopMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 10, 1, 1),
    _RlIgmpSnoopMulticastTvVID_Type()
)
rlIgmpSnoopMulticastTvVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMulticastTvVID.setStatus("current")
_RlIgmpSnoopMulticastTvGroup_Type = IpAddress
_RlIgmpSnoopMulticastTvGroup_Object = MibTableColumn
rlIgmpSnoopMulticastTvGroup = _RlIgmpSnoopMulticastTvGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 10, 1, 2),
    _RlIgmpSnoopMulticastTvGroup_Type()
)
rlIgmpSnoopMulticastTvGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMulticastTvGroup.setStatus("current")
_RlIgmpSnoopMulticastTvStatus_Type = RowStatus
_RlIgmpSnoopMulticastTvStatus_Object = MibTableColumn
rlIgmpSnoopMulticastTvStatus = _RlIgmpSnoopMulticastTvStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 10, 1, 3),
    _RlIgmpSnoopMulticastTvStatus_Type()
)
rlIgmpSnoopMulticastTvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopMulticastTvStatus.setStatus("current")
_RlIgmpSnoopMembershipTable_Object = MibTable
rlIgmpSnoopMembershipTable = _RlIgmpSnoopMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 11)
)
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipTable.setStatus("current")
_RlIgmpSnoopMembershipEntry_Object = MibTableRow
rlIgmpSnoopMembershipEntry = _RlIgmpSnoopMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 11, 1)
)
rlIgmpSnoopMembershipEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpSnoopMembershipVlanTag"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpSnoopMembershipGroupIpAddress"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpSnoopMembershipSourceIpAddress"),
)
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipEntry.setStatus("current")
_RlIgmpSnoopMembershipVlanTag_Type = VlanIndex
_RlIgmpSnoopMembershipVlanTag_Object = MibTableColumn
rlIgmpSnoopMembershipVlanTag = _RlIgmpSnoopMembershipVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 11, 1, 1),
    _RlIgmpSnoopMembershipVlanTag_Type()
)
rlIgmpSnoopMembershipVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipVlanTag.setStatus("current")
_RlIgmpSnoopMembershipGroupIpAddress_Type = IpAddress
_RlIgmpSnoopMembershipGroupIpAddress_Object = MibTableColumn
rlIgmpSnoopMembershipGroupIpAddress = _RlIgmpSnoopMembershipGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 11, 1, 2),
    _RlIgmpSnoopMembershipGroupIpAddress_Type()
)
rlIgmpSnoopMembershipGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipGroupIpAddress.setStatus("current")
_RlIgmpSnoopMembershipSourceIpAddress_Type = IpAddress
_RlIgmpSnoopMembershipSourceIpAddress_Object = MibTableColumn
rlIgmpSnoopMembershipSourceIpAddress = _RlIgmpSnoopMembershipSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 11, 1, 3),
    _RlIgmpSnoopMembershipSourceIpAddress_Type()
)
rlIgmpSnoopMembershipSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipSourceIpAddress.setStatus("current")
_RlIgmpSnoopMembershipIncPortlist_Type = PortList
_RlIgmpSnoopMembershipIncPortlist_Object = MibTableColumn
rlIgmpSnoopMembershipIncPortlist = _RlIgmpSnoopMembershipIncPortlist_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 11, 1, 4),
    _RlIgmpSnoopMembershipIncPortlist_Type()
)
rlIgmpSnoopMembershipIncPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipIncPortlist.setStatus("current")
_RlIgmpSnoopMembershipExcPortlist_Type = PortList
_RlIgmpSnoopMembershipExcPortlist_Object = MibTableColumn
rlIgmpSnoopMembershipExcPortlist = _RlIgmpSnoopMembershipExcPortlist_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 11, 1, 5),
    _RlIgmpSnoopMembershipExcPortlist_Type()
)
rlIgmpSnoopMembershipExcPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipExcPortlist.setStatus("current")
_RlIgmpSnoopMembershipExpiryTime_Type = Integer32
_RlIgmpSnoopMembershipExpiryTime_Object = MibTableColumn
rlIgmpSnoopMembershipExpiryTime = _RlIgmpSnoopMembershipExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 11, 1, 6),
    _RlIgmpSnoopMembershipExpiryTime_Type()
)
rlIgmpSnoopMembershipExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipExpiryTime.setStatus("obsolete")
_RlIgmpSnoopMembershipCompatibilityMode_Type = IgmpVersion
_RlIgmpSnoopMembershipCompatibilityMode_Object = MibTableColumn
rlIgmpSnoopMembershipCompatibilityMode = _RlIgmpSnoopMembershipCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 11, 1, 7),
    _RlIgmpSnoopMembershipCompatibilityMode_Type()
)
rlIgmpSnoopMembershipCompatibilityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipCompatibilityMode.setStatus("current")
_RlIgmpSnoopQuerierVlanTable_Object = MibTable
rlIgmpSnoopQuerierVlanTable = _RlIgmpSnoopQuerierVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 12)
)
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierVlanTable.setStatus("current")
_RlIgmpSnoopQuerierVlanEntry_Object = MibTableRow
rlIgmpSnoopQuerierVlanEntry = _RlIgmpSnoopQuerierVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 12, 1)
)
rlIgmpSnoopQuerierVlanEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpSnoopQuerierVlanTag"),
)
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierVlanEntry.setStatus("current")
_RlIgmpSnoopQuerierVlanTag_Type = VlanIndex
_RlIgmpSnoopQuerierVlanTag_Object = MibTableColumn
rlIgmpSnoopQuerierVlanTag = _RlIgmpSnoopQuerierVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 12, 1, 1),
    _RlIgmpSnoopQuerierVlanTag_Type()
)
rlIgmpSnoopQuerierVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierVlanTag.setStatus("current")
_RlIgmpSnoopQuerierAdminEnable_Type = TruthValue
_RlIgmpSnoopQuerierAdminEnable_Object = MibTableColumn
rlIgmpSnoopQuerierAdminEnable = _RlIgmpSnoopQuerierAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 12, 1, 2),
    _RlIgmpSnoopQuerierAdminEnable_Type()
)
rlIgmpSnoopQuerierAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierAdminEnable.setStatus("current")
_RlIgmpSnoopQuerierOperEnable_Type = TruthValue
_RlIgmpSnoopQuerierOperEnable_Object = MibTableColumn
rlIgmpSnoopQuerierOperEnable = _RlIgmpSnoopQuerierOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 12, 1, 3),
    _RlIgmpSnoopQuerierOperEnable_Type()
)
rlIgmpSnoopQuerierOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierOperEnable.setStatus("current")
_RlIgmpSnoopQuerierAdminAddr_Type = IpAddress
_RlIgmpSnoopQuerierAdminAddr_Object = MibTableColumn
rlIgmpSnoopQuerierAdminAddr = _RlIgmpSnoopQuerierAdminAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 12, 1, 4),
    _RlIgmpSnoopQuerierAdminAddr_Type()
)
rlIgmpSnoopQuerierAdminAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierAdminAddr.setStatus("current")
_RlIgmpSnoopQuerierOperAddr_Type = IpAddress
_RlIgmpSnoopQuerierOperAddr_Object = MibTableColumn
rlIgmpSnoopQuerierOperAddr = _RlIgmpSnoopQuerierOperAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 12, 1, 5),
    _RlIgmpSnoopQuerierOperAddr_Type()
)
rlIgmpSnoopQuerierOperAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierOperAddr.setStatus("current")
_RlIgmpSnoopQuerierAdminVersionNumber_Type = IgmpVersion
_RlIgmpSnoopQuerierAdminVersionNumber_Object = MibTableColumn
rlIgmpSnoopQuerierAdminVersionNumber = _RlIgmpSnoopQuerierAdminVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 12, 1, 6),
    _RlIgmpSnoopQuerierAdminVersionNumber_Type()
)
rlIgmpSnoopQuerierAdminVersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierAdminVersionNumber.setStatus("current")
_RlIgmpSnoopQuerierOperVersionNumber_Type = IgmpVersion
_RlIgmpSnoopQuerierOperVersionNumber_Object = MibTableColumn
rlIgmpSnoopQuerierOperVersionNumber = _RlIgmpSnoopQuerierOperVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 2, 12, 1, 7),
    _RlIgmpSnoopQuerierOperVersionNumber_Type()
)
rlIgmpSnoopQuerierOperVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierOperVersionNumber.setStatus("current")
_RlMacMulticastMaxEntriesNum_Type = Integer32
_RlMacMulticastMaxEntriesNum_Object = MibScalar
rlMacMulticastMaxEntriesNum = _RlMacMulticastMaxEntriesNum_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 3),
    _RlMacMulticastMaxEntriesNum_Type()
)
rlMacMulticastMaxEntriesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMacMulticastMaxEntriesNum.setStatus("current")
_RlMacMulticastFilter_ObjectIdentity = ObjectIdentity
rlMacMulticastFilter = _RlMacMulticastFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 4)
)
_RlMacMulticastUnregFilterEnable_Type = PortList
_RlMacMulticastUnregFilterEnable_Object = MibScalar
rlMacMulticastUnregFilterEnable = _RlMacMulticastUnregFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 4, 1),
    _RlMacMulticastUnregFilterEnable_Type()
)
rlMacMulticastUnregFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacMulticastUnregFilterEnable.setStatus("current")
_RlMldSnoop_ObjectIdentity = ObjectIdentity
rlMldSnoop = _RlMldSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5)
)
_RlMldSnoopEnable_Type = TruthValue
_RlMldSnoopEnable_Object = MibScalar
rlMldSnoopEnable = _RlMldSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 1),
    _RlMldSnoopEnable_Type()
)
rlMldSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMldSnoopEnable.setStatus("current")


class _RlMldSnoopHostAgingTime_Type(Integer32):
    """Custom type rlMldSnoopHostAgingTime based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2147483647),
    )


_RlMldSnoopHostAgingTime_Type.__name__ = "Integer32"
_RlMldSnoopHostAgingTime_Object = MibScalar
rlMldSnoopHostAgingTime = _RlMldSnoopHostAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 2),
    _RlMldSnoopHostAgingTime_Type()
)
rlMldSnoopHostAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMldSnoopHostAgingTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlMldSnoopHostAgingTime.setUnits("seconds")


class _RlMldSnoopRouterAgingTime_Type(Integer32):
    """Custom type rlMldSnoopRouterAgingTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlMldSnoopRouterAgingTime_Type.__name__ = "Integer32"
_RlMldSnoopRouterAgingTime_Object = MibScalar
rlMldSnoopRouterAgingTime = _RlMldSnoopRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 3),
    _RlMldSnoopRouterAgingTime_Type()
)
rlMldSnoopRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMldSnoopRouterAgingTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlMldSnoopRouterAgingTime.setUnits("seconds")
_RlIgmpMldSnoopMembershipTable_Object = MibTable
rlIgmpMldSnoopMembershipTable = _RlIgmpMldSnoopMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4)
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipTable.setStatus("current")
_RlIgmpMldSnoopMembershipEntry_Object = MibTableRow
rlIgmpMldSnoopMembershipEntry = _RlIgmpMldSnoopMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4, 1)
)
rlIgmpMldSnoopMembershipEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopMembershipVlanTag"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopMembershipGroupIpAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopMembershipGroupIpAddress"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopMembershipSourceIpAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopMembershipSourceIpAddress"),
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipEntry.setStatus("current")
_RlIgmpMldSnoopMembershipVlanTag_Type = VlanIndex
_RlIgmpMldSnoopMembershipVlanTag_Object = MibTableColumn
rlIgmpMldSnoopMembershipVlanTag = _RlIgmpMldSnoopMembershipVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4, 1, 1),
    _RlIgmpMldSnoopMembershipVlanTag_Type()
)
rlIgmpMldSnoopMembershipVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipVlanTag.setStatus("current")
_RlIgmpMldSnoopMembershipGroupIpAddressType_Type = InetAddressType
_RlIgmpMldSnoopMembershipGroupIpAddressType_Object = MibTableColumn
rlIgmpMldSnoopMembershipGroupIpAddressType = _RlIgmpMldSnoopMembershipGroupIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4, 1, 2),
    _RlIgmpMldSnoopMembershipGroupIpAddressType_Type()
)
rlIgmpMldSnoopMembershipGroupIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipGroupIpAddressType.setStatus("current")
_RlIgmpMldSnoopMembershipGroupIpAddress_Type = InetAddress
_RlIgmpMldSnoopMembershipGroupIpAddress_Object = MibTableColumn
rlIgmpMldSnoopMembershipGroupIpAddress = _RlIgmpMldSnoopMembershipGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4, 1, 3),
    _RlIgmpMldSnoopMembershipGroupIpAddress_Type()
)
rlIgmpMldSnoopMembershipGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipGroupIpAddress.setStatus("current")
_RlIgmpMldSnoopMembershipSourceIpAddressType_Type = InetAddressType
_RlIgmpMldSnoopMembershipSourceIpAddressType_Object = MibTableColumn
rlIgmpMldSnoopMembershipSourceIpAddressType = _RlIgmpMldSnoopMembershipSourceIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4, 1, 4),
    _RlIgmpMldSnoopMembershipSourceIpAddressType_Type()
)
rlIgmpMldSnoopMembershipSourceIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipSourceIpAddressType.setStatus("current")
_RlIgmpMldSnoopMembershipSourceIpAddress_Type = InetAddress
_RlIgmpMldSnoopMembershipSourceIpAddress_Object = MibTableColumn
rlIgmpMldSnoopMembershipSourceIpAddress = _RlIgmpMldSnoopMembershipSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4, 1, 5),
    _RlIgmpMldSnoopMembershipSourceIpAddress_Type()
)
rlIgmpMldSnoopMembershipSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipSourceIpAddress.setStatus("current")
_RlIgmpMldSnoopMembershipIncPortlist_Type = PortList
_RlIgmpMldSnoopMembershipIncPortlist_Object = MibTableColumn
rlIgmpMldSnoopMembershipIncPortlist = _RlIgmpMldSnoopMembershipIncPortlist_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4, 1, 6),
    _RlIgmpMldSnoopMembershipIncPortlist_Type()
)
rlIgmpMldSnoopMembershipIncPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipIncPortlist.setStatus("current")
_RlIgmpMldSnoopMembershipExcPortlist_Type = PortList
_RlIgmpMldSnoopMembershipExcPortlist_Object = MibTableColumn
rlIgmpMldSnoopMembershipExcPortlist = _RlIgmpMldSnoopMembershipExcPortlist_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4, 1, 7),
    _RlIgmpMldSnoopMembershipExcPortlist_Type()
)
rlIgmpMldSnoopMembershipExcPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipExcPortlist.setStatus("current")
_RlIgmpMldSnoopMembershipExpiryTime_Type = Integer32
_RlIgmpMldSnoopMembershipExpiryTime_Object = MibTableColumn
rlIgmpMldSnoopMembershipExpiryTime = _RlIgmpMldSnoopMembershipExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4, 1, 8),
    _RlIgmpMldSnoopMembershipExpiryTime_Type()
)
rlIgmpMldSnoopMembershipExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipExpiryTime.setStatus("obsolete")
_RlIgmpMldSnoopMembershipCompatibilityMode_Type = IgmpVersion
_RlIgmpMldSnoopMembershipCompatibilityMode_Object = MibTableColumn
rlIgmpMldSnoopMembershipCompatibilityMode = _RlIgmpMldSnoopMembershipCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 4, 1, 9),
    _RlIgmpMldSnoopMembershipCompatibilityMode_Type()
)
rlIgmpMldSnoopMembershipCompatibilityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipCompatibilityMode.setStatus("current")
_RlIgmpMldSnoopVlanTable_Object = MibTable
rlIgmpMldSnoopVlanTable = _RlIgmpMldSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5)
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanTable.setStatus("current")
_RlIgmpMldSnoopVlanEntry_Object = MibTableRow
rlIgmpMldSnoopVlanEntry = _RlIgmpMldSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1)
)
rlIgmpMldSnoopVlanEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopVlanInetAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopVlanTag"),
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanEntry.setStatus("current")
_RlIgmpMldSnoopVlanInetAddressType_Type = InetAddressType
_RlIgmpMldSnoopVlanInetAddressType_Object = MibTableColumn
rlIgmpMldSnoopVlanInetAddressType = _RlIgmpMldSnoopVlanInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 1),
    _RlIgmpMldSnoopVlanInetAddressType_Type()
)
rlIgmpMldSnoopVlanInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanInetAddressType.setStatus("current")
_RlIgmpMldSnoopVlanTag_Type = Integer32
_RlIgmpMldSnoopVlanTag_Object = MibTableColumn
rlIgmpMldSnoopVlanTag = _RlIgmpMldSnoopVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 2),
    _RlIgmpMldSnoopVlanTag_Type()
)
rlIgmpMldSnoopVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanTag.setStatus("current")
_RlIgmpMldSnoopVlanEnable_Type = TruthValue
_RlIgmpMldSnoopVlanEnable_Object = MibTableColumn
rlIgmpMldSnoopVlanEnable = _RlIgmpMldSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 3),
    _RlIgmpMldSnoopVlanEnable_Type()
)
rlIgmpMldSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanEnable.setStatus("current")
_RlIgmpMldSnoopVlanRouterLearn_Type = TruthValue
_RlIgmpMldSnoopVlanRouterLearn_Object = MibTableColumn
rlIgmpMldSnoopVlanRouterLearn = _RlIgmpMldSnoopVlanRouterLearn_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 4),
    _RlIgmpMldSnoopVlanRouterLearn_Type()
)
rlIgmpMldSnoopVlanRouterLearn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanRouterLearn.setStatus("current")


class _RlIgmpMldSnoopVlanHostTimeOut_Type(Integer32):
    """Custom type rlIgmpMldSnoopVlanHostTimeOut based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2147483647),
    )


_RlIgmpMldSnoopVlanHostTimeOut_Type.__name__ = "Integer32"
_RlIgmpMldSnoopVlanHostTimeOut_Object = MibTableColumn
rlIgmpMldSnoopVlanHostTimeOut = _RlIgmpMldSnoopVlanHostTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 5),
    _RlIgmpMldSnoopVlanHostTimeOut_Type()
)
rlIgmpMldSnoopVlanHostTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanHostTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanHostTimeOut.setUnits("seconds")


class _RlIgmpMldSnoopVlanQuerierTimeOut_Type(Integer32):
    """Custom type rlIgmpMldSnoopVlanQuerierTimeOut based on Integer32"""
    defaultValue = 260

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlIgmpMldSnoopVlanQuerierTimeOut_Type.__name__ = "Integer32"
_RlIgmpMldSnoopVlanQuerierTimeOut_Object = MibTableColumn
rlIgmpMldSnoopVlanQuerierTimeOut = _RlIgmpMldSnoopVlanQuerierTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 6),
    _RlIgmpMldSnoopVlanQuerierTimeOut_Type()
)
rlIgmpMldSnoopVlanQuerierTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanQuerierTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanQuerierTimeOut.setUnits("seconds")


class _RlIgmpMldSnoopVlanRouterTimeOut_Type(Integer32):
    """Custom type rlIgmpMldSnoopVlanRouterTimeOut based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RlIgmpMldSnoopVlanRouterTimeOut_Type.__name__ = "Integer32"
_RlIgmpMldSnoopVlanRouterTimeOut_Object = MibTableColumn
rlIgmpMldSnoopVlanRouterTimeOut = _RlIgmpMldSnoopVlanRouterTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 7),
    _RlIgmpMldSnoopVlanRouterTimeOut_Type()
)
rlIgmpMldSnoopVlanRouterTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanRouterTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanRouterTimeOut.setUnits("seconds")


class _RlIgmpMldSnoopVlanLeaveTimeOut_Type(Integer32):
    """Custom type rlIgmpMldSnoopVlanLeaveTimeOut based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlIgmpMldSnoopVlanLeaveTimeOut_Type.__name__ = "Integer32"
_RlIgmpMldSnoopVlanLeaveTimeOut_Object = MibTableColumn
rlIgmpMldSnoopVlanLeaveTimeOut = _RlIgmpMldSnoopVlanLeaveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 8),
    _RlIgmpMldSnoopVlanLeaveTimeOut_Type()
)
rlIgmpMldSnoopVlanLeaveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanLeaveTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanLeaveTimeOut.setUnits("seconds")
_RlIgmpMldSnoopVlanIgmpVersion_Type = IgmpVersion
_RlIgmpMldSnoopVlanIgmpVersion_Object = MibTableColumn
rlIgmpMldSnoopVlanIgmpVersion = _RlIgmpMldSnoopVlanIgmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 9),
    _RlIgmpMldSnoopVlanIgmpVersion_Type()
)
rlIgmpMldSnoopVlanIgmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanIgmpVersion.setStatus("current")
_RlIgmpMldSnoopVlanRouterPortlist_Type = PortList
_RlIgmpMldSnoopVlanRouterPortlist_Object = MibTableColumn
rlIgmpMldSnoopVlanRouterPortlist = _RlIgmpMldSnoopVlanRouterPortlist_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 10),
    _RlIgmpMldSnoopVlanRouterPortlist_Type()
)
rlIgmpMldSnoopVlanRouterPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanRouterPortlist.setStatus("current")
_RlIgmpMldSnoopVlanRouterStaticPortlist_Type = PortList
_RlIgmpMldSnoopVlanRouterStaticPortlist_Object = MibTableColumn
rlIgmpMldSnoopVlanRouterStaticPortlist = _RlIgmpMldSnoopVlanRouterStaticPortlist_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 11),
    _RlIgmpMldSnoopVlanRouterStaticPortlist_Type()
)
rlIgmpMldSnoopVlanRouterStaticPortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanRouterStaticPortlist.setStatus("current")
_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Type = PortList
_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Object = MibTableColumn
rlIgmpMldSnoopVlanRouterForbiddenPortlist = _RlIgmpMldSnoopVlanRouterForbiddenPortlist_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 12),
    _RlIgmpMldSnoopVlanRouterForbiddenPortlist_Type()
)
rlIgmpMldSnoopVlanRouterForbiddenPortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanRouterForbiddenPortlist.setStatus("current")
_RlIgmpMldSnoopVlanQueryOverride_Type = TruthValue
_RlIgmpMldSnoopVlanQueryOverride_Object = MibTableColumn
rlIgmpMldSnoopVlanQueryOverride = _RlIgmpMldSnoopVlanQueryOverride_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 13),
    _RlIgmpMldSnoopVlanQueryOverride_Type()
)
rlIgmpMldSnoopVlanQueryOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanQueryOverride.setStatus("current")


class _RlIgmpMldSnoopVlanOperRobustness_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanOperRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlIgmpMldSnoopVlanOperRobustness_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanOperRobustness_Object = MibTableColumn
rlIgmpMldSnoopVlanOperRobustness = _RlIgmpMldSnoopVlanOperRobustness_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 14),
    _RlIgmpMldSnoopVlanOperRobustness_Type()
)
rlIgmpMldSnoopVlanOperRobustness.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperRobustness.setStatus("current")


class _RlIgmpMldSnoopVlanOperQueryInterval_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanOperQueryInterval based on Unsigned32"""
    defaultValue = 125000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 31744000),
    )


_RlIgmpMldSnoopVlanOperQueryInterval_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanOperQueryInterval_Object = MibTableColumn
rlIgmpMldSnoopVlanOperQueryInterval = _RlIgmpMldSnoopVlanOperQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 15),
    _RlIgmpMldSnoopVlanOperQueryInterval_Type()
)
rlIgmpMldSnoopVlanOperQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperQueryInterval.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanOperQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8387584),
    )


_RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Object = MibTableColumn
rlIgmpMldSnoopVlanOperQueryMaxResponseTime = _RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 16),
    _RlIgmpMldSnoopVlanOperQueryMaxResponseTime_Type()
)
rlIgmpMldSnoopVlanOperQueryMaxResponseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperQueryMaxResponseTime.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanOperLastMemberQueryInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8387584),
    )


_RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Object = MibTableColumn
rlIgmpMldSnoopVlanOperLastMemberQueryInterval = _RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 17),
    _RlIgmpMldSnoopVlanOperLastMemberQueryInterval_Type()
)
rlIgmpMldSnoopVlanOperLastMemberQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperLastMemberQueryInterval.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanOperLastMemberQueryCount_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanOperLastMemberQueryCount based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlIgmpMldSnoopVlanOperLastMemberQueryCount_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanOperLastMemberQueryCount_Object = MibTableColumn
rlIgmpMldSnoopVlanOperLastMemberQueryCount = _RlIgmpMldSnoopVlanOperLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 18),
    _RlIgmpMldSnoopVlanOperLastMemberQueryCount_Type()
)
rlIgmpMldSnoopVlanOperLastMemberQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperLastMemberQueryCount.setStatus("current")


class _RlIgmpMldSnoopVlanOperStartupQueryInterval_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanOperStartupQueryInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31744000),
    )


_RlIgmpMldSnoopVlanOperStartupQueryInterval_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanOperStartupQueryInterval_Object = MibTableColumn
rlIgmpMldSnoopVlanOperStartupQueryInterval = _RlIgmpMldSnoopVlanOperStartupQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 19),
    _RlIgmpMldSnoopVlanOperStartupQueryInterval_Type()
)
rlIgmpMldSnoopVlanOperStartupQueryInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperStartupQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperStartupQueryInterval.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanOperStartupQueryCount_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanOperStartupQueryCount based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlIgmpMldSnoopVlanOperStartupQueryCount_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanOperStartupQueryCount_Object = MibTableColumn
rlIgmpMldSnoopVlanOperStartupQueryCount = _RlIgmpMldSnoopVlanOperStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 20),
    _RlIgmpMldSnoopVlanOperStartupQueryCount_Type()
)
rlIgmpMldSnoopVlanOperStartupQueryCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperStartupQueryCount.setStatus("current")


class _RlIgmpMldSnoopVlanOperHostTimeOut_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanOperHostTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlIgmpMldSnoopVlanOperHostTimeOut_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanOperHostTimeOut_Object = MibTableColumn
rlIgmpMldSnoopVlanOperHostTimeOut = _RlIgmpMldSnoopVlanOperHostTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 21),
    _RlIgmpMldSnoopVlanOperHostTimeOut_Type()
)
rlIgmpMldSnoopVlanOperHostTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperHostTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperHostTimeOut.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanOperRouterTimeOut_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanOperRouterTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlIgmpMldSnoopVlanOperRouterTimeOut_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanOperRouterTimeOut_Object = MibTableColumn
rlIgmpMldSnoopVlanOperRouterTimeOut = _RlIgmpMldSnoopVlanOperRouterTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 22),
    _RlIgmpMldSnoopVlanOperRouterTimeOut_Type()
)
rlIgmpMldSnoopVlanOperRouterTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperRouterTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperRouterTimeOut.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanOperLeaveTimeOut_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanOperLeaveTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlIgmpMldSnoopVlanOperLeaveTimeOut_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanOperLeaveTimeOut_Object = MibTableColumn
rlIgmpMldSnoopVlanOperLeaveTimeOut = _RlIgmpMldSnoopVlanOperLeaveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 23),
    _RlIgmpMldSnoopVlanOperLeaveTimeOut_Type()
)
rlIgmpMldSnoopVlanOperLeaveTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperLeaveTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanOperLeaveTimeOut.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanAdminRobustness_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanAdminRobustness based on Unsigned32"""
    defaultValue = 2

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_RlIgmpMldSnoopVlanAdminRobustness_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminRobustness_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminRobustness = _RlIgmpMldSnoopVlanAdminRobustness_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 24),
    _RlIgmpMldSnoopVlanAdminRobustness_Type()
)
rlIgmpMldSnoopVlanAdminRobustness.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminRobustness.setStatus("current")


class _RlIgmpMldSnoopVlanAdminQueryInterval_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanAdminQueryInterval based on Unsigned32"""
    defaultValue = 125000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 18000000),
    )


_RlIgmpMldSnoopVlanAdminQueryInterval_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminQueryInterval_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminQueryInterval = _RlIgmpMldSnoopVlanAdminQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 25),
    _RlIgmpMldSnoopVlanAdminQueryInterval_Type()
)
rlIgmpMldSnoopVlanAdminQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminQueryInterval.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanAdminQueryMaxResponseTime based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1000, 20000),
    )


_RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminQueryMaxResponseTime = _RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 26),
    _RlIgmpMldSnoopVlanAdminQueryMaxResponseTime_Type()
)
rlIgmpMldSnoopVlanAdminQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminQueryMaxResponseTime.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminQueryMaxResponseTime.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanAdminLastMemberQueryInterval based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 25500),
    )


_RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminLastMemberQueryInterval = _RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 27),
    _RlIgmpMldSnoopVlanAdminLastMemberQueryInterval_Type()
)
rlIgmpMldSnoopVlanAdminLastMemberQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminLastMemberQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminLastMemberQueryInterval.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanAdminLastMemberQueryCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminLastMemberQueryCount = _RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 28),
    _RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Type()
)
rlIgmpMldSnoopVlanAdminLastMemberQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminLastMemberQueryCount.setStatus("current")


class _RlIgmpMldSnoopVlanAdminStartupQueryInterval_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanAdminStartupQueryInterval based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4500000),
    )


_RlIgmpMldSnoopVlanAdminStartupQueryInterval_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminStartupQueryInterval_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminStartupQueryInterval = _RlIgmpMldSnoopVlanAdminStartupQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 29),
    _RlIgmpMldSnoopVlanAdminStartupQueryInterval_Type()
)
rlIgmpMldSnoopVlanAdminStartupQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminStartupQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminStartupQueryInterval.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanAdminStartupQueryCount_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanAdminStartupQueryCount based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_RlIgmpMldSnoopVlanAdminStartupQueryCount_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminStartupQueryCount_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminStartupQueryCount = _RlIgmpMldSnoopVlanAdminStartupQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 30),
    _RlIgmpMldSnoopVlanAdminStartupQueryCount_Type()
)
rlIgmpMldSnoopVlanAdminStartupQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminStartupQueryCount.setStatus("current")


class _RlIgmpMldSnoopVlanAdminHostTimeOut_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanAdminHostTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlIgmpMldSnoopVlanAdminHostTimeOut_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminHostTimeOut_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminHostTimeOut = _RlIgmpMldSnoopVlanAdminHostTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 31),
    _RlIgmpMldSnoopVlanAdminHostTimeOut_Type()
)
rlIgmpMldSnoopVlanAdminHostTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminHostTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminHostTimeOut.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanAdminRouterTimeOut_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanAdminRouterTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlIgmpMldSnoopVlanAdminRouterTimeOut_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminRouterTimeOut_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminRouterTimeOut = _RlIgmpMldSnoopVlanAdminRouterTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 32),
    _RlIgmpMldSnoopVlanAdminRouterTimeOut_Type()
)
rlIgmpMldSnoopVlanAdminRouterTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminRouterTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminRouterTimeOut.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanAdminLeaveTimeOut_Type(Unsigned32):
    """Custom type rlIgmpMldSnoopVlanAdminLeaveTimeOut based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlIgmpMldSnoopVlanAdminLeaveTimeOut_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminLeaveTimeOut_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminLeaveTimeOut = _RlIgmpMldSnoopVlanAdminLeaveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 33),
    _RlIgmpMldSnoopVlanAdminLeaveTimeOut_Type()
)
rlIgmpMldSnoopVlanAdminLeaveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminLeaveTimeOut.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanAdminLeaveTimeOut.setUnits("milliseconds")


class _RlIgmpMldSnoopVlanIsImmediateLeave_Type(TruthValue):
    """Custom type rlIgmpMldSnoopVlanIsImmediateLeave based on TruthValue"""


_RlIgmpMldSnoopVlanIsImmediateLeave_Object = MibTableColumn
rlIgmpMldSnoopVlanIsImmediateLeave = _RlIgmpMldSnoopVlanIsImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 5, 1, 34),
    _RlIgmpMldSnoopVlanIsImmediateLeave_Type()
)
rlIgmpMldSnoopVlanIsImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanIsImmediateLeave.setStatus("current")
_RlIgmpMldSnoopMulticastTvTable_Object = MibTable
rlIgmpMldSnoopMulticastTvTable = _RlIgmpMldSnoopMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 6)
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvTable.setStatus("current")
_RlIgmpMldSnoopMulticastTvEntry_Object = MibTableRow
rlIgmpMldSnoopMulticastTvEntry = _RlIgmpMldSnoopMulticastTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 6, 1)
)
rlIgmpMldSnoopMulticastTvEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopMulticastTvInetAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopMulticastTvVID"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopMulticastTvGroupAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopMulticastTvGroup"),
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvEntry.setStatus("current")
_RlIgmpMldSnoopMulticastTvInetAddressType_Type = InetAddressType
_RlIgmpMldSnoopMulticastTvInetAddressType_Object = MibTableColumn
rlIgmpMldSnoopMulticastTvInetAddressType = _RlIgmpMldSnoopMulticastTvInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 6, 1, 1),
    _RlIgmpMldSnoopMulticastTvInetAddressType_Type()
)
rlIgmpMldSnoopMulticastTvInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvInetAddressType.setStatus("current")
_RlIgmpMldSnoopMulticastTvVID_Type = VlanIndex
_RlIgmpMldSnoopMulticastTvVID_Object = MibTableColumn
rlIgmpMldSnoopMulticastTvVID = _RlIgmpMldSnoopMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 6, 1, 2),
    _RlIgmpMldSnoopMulticastTvVID_Type()
)
rlIgmpMldSnoopMulticastTvVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvVID.setStatus("current")
_RlIgmpMldSnoopMulticastTvGroupAddressType_Type = InetAddressType
_RlIgmpMldSnoopMulticastTvGroupAddressType_Object = MibTableColumn
rlIgmpMldSnoopMulticastTvGroupAddressType = _RlIgmpMldSnoopMulticastTvGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 6, 1, 3),
    _RlIgmpMldSnoopMulticastTvGroupAddressType_Type()
)
rlIgmpMldSnoopMulticastTvGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvGroupAddressType.setStatus("current")
_RlIgmpMldSnoopMulticastTvGroup_Type = InetAddress
_RlIgmpMldSnoopMulticastTvGroup_Object = MibTableColumn
rlIgmpMldSnoopMulticastTvGroup = _RlIgmpMldSnoopMulticastTvGroup_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 6, 1, 4),
    _RlIgmpMldSnoopMulticastTvGroup_Type()
)
rlIgmpMldSnoopMulticastTvGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvGroup.setStatus("current")
_RlIgmpMldSnoopMulticastTvStatus_Type = RowStatus
_RlIgmpMldSnoopMulticastTvStatus_Object = MibTableColumn
rlIgmpMldSnoopMulticastTvStatus = _RlIgmpMldSnoopMulticastTvStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 6, 1, 5),
    _RlIgmpMldSnoopMulticastTvStatus_Type()
)
rlIgmpMldSnoopMulticastTvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvStatus.setStatus("current")
_RlIgmpMldSnoopQuerierVlanTable_Object = MibTable
rlIgmpMldSnoopQuerierVlanTable = _RlIgmpMldSnoopQuerierVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7)
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierVlanTable.setStatus("current")
_RlIgmpMldSnoopQuerierVlanEntry_Object = MibTableRow
rlIgmpMldSnoopQuerierVlanEntry = _RlIgmpMldSnoopQuerierVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7, 1)
)
rlIgmpMldSnoopQuerierVlanEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlIgmpMldSnoopQuerierVlanTag"),
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierVlanEntry.setStatus("current")
_RlIgmpMldSnoopQuerierVlanTag_Type = VlanIndex
_RlIgmpMldSnoopQuerierVlanTag_Object = MibTableColumn
rlIgmpMldSnoopQuerierVlanTag = _RlIgmpMldSnoopQuerierVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7, 1, 1),
    _RlIgmpMldSnoopQuerierVlanTag_Type()
)
rlIgmpMldSnoopQuerierVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierVlanTag.setStatus("current")
_RlIgmpMldSnoopQuerierAdminEnable_Type = TruthValue
_RlIgmpMldSnoopQuerierAdminEnable_Object = MibTableColumn
rlIgmpMldSnoopQuerierAdminEnable = _RlIgmpMldSnoopQuerierAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7, 1, 2),
    _RlIgmpMldSnoopQuerierAdminEnable_Type()
)
rlIgmpMldSnoopQuerierAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierAdminEnable.setStatus("current")
_RlIgmpMldSnoopQuerierOperEnable_Type = TruthValue
_RlIgmpMldSnoopQuerierOperEnable_Object = MibTableColumn
rlIgmpMldSnoopQuerierOperEnable = _RlIgmpMldSnoopQuerierOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7, 1, 3),
    _RlIgmpMldSnoopQuerierOperEnable_Type()
)
rlIgmpMldSnoopQuerierOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierOperEnable.setStatus("current")
_RlIgmpMldSnoopQuerierAdminAddrInetAddressType_Type = InetAddressType
_RlIgmpMldSnoopQuerierAdminAddrInetAddressType_Object = MibTableColumn
rlIgmpMldSnoopQuerierAdminAddrInetAddressType = _RlIgmpMldSnoopQuerierAdminAddrInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7, 1, 4),
    _RlIgmpMldSnoopQuerierAdminAddrInetAddressType_Type()
)
rlIgmpMldSnoopQuerierAdminAddrInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierAdminAddrInetAddressType.setStatus("current")
_RlIgmpMldSnoopQuerierAdminAddr_Type = InetAddress
_RlIgmpMldSnoopQuerierAdminAddr_Object = MibTableColumn
rlIgmpMldSnoopQuerierAdminAddr = _RlIgmpMldSnoopQuerierAdminAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7, 1, 5),
    _RlIgmpMldSnoopQuerierAdminAddr_Type()
)
rlIgmpMldSnoopQuerierAdminAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierAdminAddr.setStatus("current")
_RlIgmpMldSnoopQuerierOperAddrInetAddressType_Type = InetAddressType
_RlIgmpMldSnoopQuerierOperAddrInetAddressType_Object = MibTableColumn
rlIgmpMldSnoopQuerierOperAddrInetAddressType = _RlIgmpMldSnoopQuerierOperAddrInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7, 1, 6),
    _RlIgmpMldSnoopQuerierOperAddrInetAddressType_Type()
)
rlIgmpMldSnoopQuerierOperAddrInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierOperAddrInetAddressType.setStatus("current")
_RlIgmpMldSnoopQuerierOperAddr_Type = InetAddress
_RlIgmpMldSnoopQuerierOperAddr_Object = MibTableColumn
rlIgmpMldSnoopQuerierOperAddr = _RlIgmpMldSnoopQuerierOperAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7, 1, 7),
    _RlIgmpMldSnoopQuerierOperAddr_Type()
)
rlIgmpMldSnoopQuerierOperAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierOperAddr.setStatus("current")
_RlIgmpMldSnoopQuerierAdminVersionNumber_Type = IgmpVersion
_RlIgmpMldSnoopQuerierAdminVersionNumber_Object = MibTableColumn
rlIgmpMldSnoopQuerierAdminVersionNumber = _RlIgmpMldSnoopQuerierAdminVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7, 1, 8),
    _RlIgmpMldSnoopQuerierAdminVersionNumber_Type()
)
rlIgmpMldSnoopQuerierAdminVersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierAdminVersionNumber.setStatus("current")
_RlIgmpMldSnoopQuerierOperVersionNumber_Type = IgmpVersion
_RlIgmpMldSnoopQuerierOperVersionNumber_Object = MibTableColumn
rlIgmpMldSnoopQuerierOperVersionNumber = _RlIgmpMldSnoopQuerierOperVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 55, 5, 7, 1, 9),
    _RlIgmpMldSnoopQuerierOperVersionNumber_Type()
)
rlIgmpMldSnoopQuerierOperVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierOperVersionNumber.setStatus("current")
_RlBrgMulticastMibVersion_Type = Integer32
_RlBrgMulticastMibVersion_Object = MibScalar
rlBrgMulticastMibVersion = _RlBrgMulticastMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 1),
    _RlBrgMulticastMibVersion_Type()
)
rlBrgMulticastMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgMulticastMibVersion.setStatus("current")
_RlBrgStaticIpMulticastTable_Object = MibTable
rlBrgStaticIpMulticastTable = _RlBrgStaticIpMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 3)
)
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastTable.setStatus("current")
_RlBrgStaticIpMulticastEntry_Object = MibTableRow
rlBrgStaticIpMulticastEntry = _RlBrgStaticIpMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 3, 1)
)
rlBrgStaticIpMulticastEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgStaticIpMulticastVlanTag"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgStaticIpMulticastGroupAddress"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgStaticIpMulticastSourceAddress"),
)
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastEntry.setStatus("current")
_RlBrgStaticIpMulticastVlanTag_Type = VlanIndex
_RlBrgStaticIpMulticastVlanTag_Object = MibTableColumn
rlBrgStaticIpMulticastVlanTag = _RlBrgStaticIpMulticastVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 3, 1, 1),
    _RlBrgStaticIpMulticastVlanTag_Type()
)
rlBrgStaticIpMulticastVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastVlanTag.setStatus("current")
_RlBrgStaticIpMulticastGroupAddress_Type = IpAddress
_RlBrgStaticIpMulticastGroupAddress_Object = MibTableColumn
rlBrgStaticIpMulticastGroupAddress = _RlBrgStaticIpMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 3, 1, 2),
    _RlBrgStaticIpMulticastGroupAddress_Type()
)
rlBrgStaticIpMulticastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastGroupAddress.setStatus("current")
_RlBrgStaticIpMulticastSourceAddress_Type = IpAddress
_RlBrgStaticIpMulticastSourceAddress_Object = MibTableColumn
rlBrgStaticIpMulticastSourceAddress = _RlBrgStaticIpMulticastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 3, 1, 3),
    _RlBrgStaticIpMulticastSourceAddress_Type()
)
rlBrgStaticIpMulticastSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastSourceAddress.setStatus("current")
_RlBrgStaticIpMulticastFrwPorts_Type = PortList
_RlBrgStaticIpMulticastFrwPorts_Object = MibTableColumn
rlBrgStaticIpMulticastFrwPorts = _RlBrgStaticIpMulticastFrwPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 3, 1, 4),
    _RlBrgStaticIpMulticastFrwPorts_Type()
)
rlBrgStaticIpMulticastFrwPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastFrwPorts.setStatus("current")
_RlBrgStaticIpMulticastForbiddenPorts_Type = PortList
_RlBrgStaticIpMulticastForbiddenPorts_Object = MibTableColumn
rlBrgStaticIpMulticastForbiddenPorts = _RlBrgStaticIpMulticastForbiddenPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 3, 1, 5),
    _RlBrgStaticIpMulticastForbiddenPorts_Type()
)
rlBrgStaticIpMulticastForbiddenPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastForbiddenPorts.setStatus("current")
_RlBrgStaticIpMulticastStatus_Type = RowStatus
_RlBrgStaticIpMulticastStatus_Object = MibTableColumn
rlBrgStaticIpMulticastStatus = _RlBrgStaticIpMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 3, 1, 6),
    _RlBrgStaticIpMulticastStatus_Type()
)
rlBrgStaticIpMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticIpMulticastStatus.setStatus("current")
_RlBrgIpMulticastTable_Object = MibTable
rlBrgIpMulticastTable = _RlBrgIpMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 4)
)
if mibBuilder.loadTexts:
    rlBrgIpMulticastTable.setStatus("current")
_RlBrgIpMulticastEntry_Object = MibTableRow
rlBrgIpMulticastEntry = _RlBrgIpMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 4, 1)
)
rlBrgIpMulticastEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgIpMulticastVlanTag"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgIpMulticastGroupAddress"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgIpMulticastSourceAddress"),
)
if mibBuilder.loadTexts:
    rlBrgIpMulticastEntry.setStatus("current")
_RlBrgIpMulticastVlanTag_Type = VlanIndex
_RlBrgIpMulticastVlanTag_Object = MibTableColumn
rlBrgIpMulticastVlanTag = _RlBrgIpMulticastVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 4, 1, 1),
    _RlBrgIpMulticastVlanTag_Type()
)
rlBrgIpMulticastVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpMulticastVlanTag.setStatus("current")
_RlBrgIpMulticastGroupAddress_Type = IpAddress
_RlBrgIpMulticastGroupAddress_Object = MibTableColumn
rlBrgIpMulticastGroupAddress = _RlBrgIpMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 4, 1, 2),
    _RlBrgIpMulticastGroupAddress_Type()
)
rlBrgIpMulticastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpMulticastGroupAddress.setStatus("current")
_RlBrgIpMulticastSourceAddress_Type = IpAddress
_RlBrgIpMulticastSourceAddress_Object = MibTableColumn
rlBrgIpMulticastSourceAddress = _RlBrgIpMulticastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 4, 1, 3),
    _RlBrgIpMulticastSourceAddress_Type()
)
rlBrgIpMulticastSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpMulticastSourceAddress.setStatus("current")
_RlBrgIpMulticastEgressPorts_Type = PortList
_RlBrgIpMulticastEgressPorts_Object = MibTableColumn
rlBrgIpMulticastEgressPorts = _RlBrgIpMulticastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 4, 1, 4),
    _RlBrgIpMulticastEgressPorts_Type()
)
rlBrgIpMulticastEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgIpMulticastEgressPorts.setStatus("current")
_RlBrgIpMulticastLearntPorts_Type = PortList
_RlBrgIpMulticastLearntPorts_Object = MibTableColumn
rlBrgIpMulticastLearntPorts = _RlBrgIpMulticastLearntPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 4, 1, 5),
    _RlBrgIpMulticastLearntPorts_Type()
)
rlBrgIpMulticastLearntPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgIpMulticastLearntPorts.setStatus("current")
_RlBrgStaticInetMulticastTable_Object = MibTable
rlBrgStaticInetMulticastTable = _RlBrgStaticInetMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 5)
)
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastTable.setStatus("current")
_RlBrgStaticInetMulticastEntry_Object = MibTableRow
rlBrgStaticInetMulticastEntry = _RlBrgStaticInetMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 5, 1)
)
rlBrgStaticInetMulticastEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastVlanTag"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastGroupAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastGroupAddress"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastSourceAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgStaticInetMulticastSourceAddress"),
)
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastEntry.setStatus("current")
_RlBrgStaticInetMulticastVlanTag_Type = VlanIndex
_RlBrgStaticInetMulticastVlanTag_Object = MibTableColumn
rlBrgStaticInetMulticastVlanTag = _RlBrgStaticInetMulticastVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 5, 1, 1),
    _RlBrgStaticInetMulticastVlanTag_Type()
)
rlBrgStaticInetMulticastVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastVlanTag.setStatus("current")
_RlBrgStaticInetMulticastGroupAddressType_Type = InetAddressType
_RlBrgStaticInetMulticastGroupAddressType_Object = MibTableColumn
rlBrgStaticInetMulticastGroupAddressType = _RlBrgStaticInetMulticastGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 5, 1, 2),
    _RlBrgStaticInetMulticastGroupAddressType_Type()
)
rlBrgStaticInetMulticastGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastGroupAddressType.setStatus("current")
_RlBrgStaticInetMulticastGroupAddress_Type = InetAddress
_RlBrgStaticInetMulticastGroupAddress_Object = MibTableColumn
rlBrgStaticInetMulticastGroupAddress = _RlBrgStaticInetMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 5, 1, 3),
    _RlBrgStaticInetMulticastGroupAddress_Type()
)
rlBrgStaticInetMulticastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastGroupAddress.setStatus("current")
_RlBrgStaticInetMulticastSourceAddressType_Type = InetAddressType
_RlBrgStaticInetMulticastSourceAddressType_Object = MibTableColumn
rlBrgStaticInetMulticastSourceAddressType = _RlBrgStaticInetMulticastSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 5, 1, 4),
    _RlBrgStaticInetMulticastSourceAddressType_Type()
)
rlBrgStaticInetMulticastSourceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastSourceAddressType.setStatus("current")
_RlBrgStaticInetMulticastSourceAddress_Type = InetAddress
_RlBrgStaticInetMulticastSourceAddress_Object = MibTableColumn
rlBrgStaticInetMulticastSourceAddress = _RlBrgStaticInetMulticastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 5, 1, 5),
    _RlBrgStaticInetMulticastSourceAddress_Type()
)
rlBrgStaticInetMulticastSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastSourceAddress.setStatus("current")
_RlBrgStaticInetMulticastFrwPorts_Type = PortList
_RlBrgStaticInetMulticastFrwPorts_Object = MibTableColumn
rlBrgStaticInetMulticastFrwPorts = _RlBrgStaticInetMulticastFrwPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 5, 1, 6),
    _RlBrgStaticInetMulticastFrwPorts_Type()
)
rlBrgStaticInetMulticastFrwPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastFrwPorts.setStatus("current")
_RlBrgStaticInetMulticastForbiddenPorts_Type = PortList
_RlBrgStaticInetMulticastForbiddenPorts_Object = MibTableColumn
rlBrgStaticInetMulticastForbiddenPorts = _RlBrgStaticInetMulticastForbiddenPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 5, 1, 7),
    _RlBrgStaticInetMulticastForbiddenPorts_Type()
)
rlBrgStaticInetMulticastForbiddenPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastForbiddenPorts.setStatus("current")
_RlBrgStaticInetMulticastStatus_Type = RowStatus
_RlBrgStaticInetMulticastStatus_Object = MibTableColumn
rlBrgStaticInetMulticastStatus = _RlBrgStaticInetMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 5, 1, 8),
    _RlBrgStaticInetMulticastStatus_Type()
)
rlBrgStaticInetMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgStaticInetMulticastStatus.setStatus("current")
_RlBrgInetMulticastTable_Object = MibTable
rlBrgInetMulticastTable = _RlBrgInetMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 6)
)
if mibBuilder.loadTexts:
    rlBrgInetMulticastTable.setStatus("current")
_RlBrgInetMulticastEntry_Object = MibTableRow
rlBrgInetMulticastEntry = _RlBrgInetMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 6, 1)
)
rlBrgInetMulticastEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgInetMulticastVlanTag"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgInetMulticastGroupAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgInetMulticastGroupAddress"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgInetMulticastSourceAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgInetMulticastSourceAddress"),
)
if mibBuilder.loadTexts:
    rlBrgInetMulticastEntry.setStatus("current")
_RlBrgInetMulticastVlanTag_Type = VlanIndex
_RlBrgInetMulticastVlanTag_Object = MibTableColumn
rlBrgInetMulticastVlanTag = _RlBrgInetMulticastVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 6, 1, 1),
    _RlBrgInetMulticastVlanTag_Type()
)
rlBrgInetMulticastVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgInetMulticastVlanTag.setStatus("current")
_RlBrgInetMulticastGroupAddressType_Type = InetAddressType
_RlBrgInetMulticastGroupAddressType_Object = MibTableColumn
rlBrgInetMulticastGroupAddressType = _RlBrgInetMulticastGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 6, 1, 2),
    _RlBrgInetMulticastGroupAddressType_Type()
)
rlBrgInetMulticastGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgInetMulticastGroupAddressType.setStatus("current")
_RlBrgInetMulticastGroupAddress_Type = InetAddress
_RlBrgInetMulticastGroupAddress_Object = MibTableColumn
rlBrgInetMulticastGroupAddress = _RlBrgInetMulticastGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 6, 1, 3),
    _RlBrgInetMulticastGroupAddress_Type()
)
rlBrgInetMulticastGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgInetMulticastGroupAddress.setStatus("current")
_RlBrgInetMulticastSourceAddressType_Type = InetAddressType
_RlBrgInetMulticastSourceAddressType_Object = MibTableColumn
rlBrgInetMulticastSourceAddressType = _RlBrgInetMulticastSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 6, 1, 4),
    _RlBrgInetMulticastSourceAddressType_Type()
)
rlBrgInetMulticastSourceAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgInetMulticastSourceAddressType.setStatus("current")
_RlBrgInetMulticastSourceAddress_Type = InetAddress
_RlBrgInetMulticastSourceAddress_Object = MibTableColumn
rlBrgInetMulticastSourceAddress = _RlBrgInetMulticastSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 6, 1, 5),
    _RlBrgInetMulticastSourceAddress_Type()
)
rlBrgInetMulticastSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgInetMulticastSourceAddress.setStatus("current")
_RlBrgInetMulticastEgressPorts_Type = PortList
_RlBrgInetMulticastEgressPorts_Object = MibTableColumn
rlBrgInetMulticastEgressPorts = _RlBrgInetMulticastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 6, 1, 6),
    _RlBrgInetMulticastEgressPorts_Type()
)
rlBrgInetMulticastEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgInetMulticastEgressPorts.setStatus("current")
_RlBrgInetMulticastLearntPorts_Type = PortList
_RlBrgInetMulticastLearntPorts_Object = MibTableColumn
rlBrgInetMulticastLearntPorts = _RlBrgInetMulticastLearntPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 6, 1, 7),
    _RlBrgInetMulticastLearntPorts_Type()
)
rlBrgInetMulticastLearntPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgInetMulticastLearntPorts.setStatus("current")
_RlBrgIpmFdbRefTable_Object = MibTable
rlBrgIpmFdbRefTable = _RlBrgIpmFdbRefTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 7)
)
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefTable.setStatus("current")
_RlBrgIpmFdbRefEntry_Object = MibTableRow
rlBrgIpmFdbRefEntry = _RlBrgIpmFdbRefEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 7, 1)
)
rlBrgIpmFdbRefEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgIpmFdbRefVlanTag"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgIpmFdbRefGroupAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgIpmFdbRefGroupAddress"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgIpmFdbRefSourceAddressType"),
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgIpmFdbRefSourceAddress"),
)
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefEntry.setStatus("current")
_RlBrgIpmFdbRefVlanTag_Type = VlanIndex
_RlBrgIpmFdbRefVlanTag_Object = MibTableColumn
rlBrgIpmFdbRefVlanTag = _RlBrgIpmFdbRefVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 7, 1, 1),
    _RlBrgIpmFdbRefVlanTag_Type()
)
rlBrgIpmFdbRefVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefVlanTag.setStatus("current")
_RlBrgIpmFdbRefGroupAddressType_Type = InetAddressType
_RlBrgIpmFdbRefGroupAddressType_Object = MibTableColumn
rlBrgIpmFdbRefGroupAddressType = _RlBrgIpmFdbRefGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 7, 1, 2),
    _RlBrgIpmFdbRefGroupAddressType_Type()
)
rlBrgIpmFdbRefGroupAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefGroupAddressType.setStatus("current")
_RlBrgIpmFdbRefGroupAddress_Type = InetAddress
_RlBrgIpmFdbRefGroupAddress_Object = MibTableColumn
rlBrgIpmFdbRefGroupAddress = _RlBrgIpmFdbRefGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 7, 1, 3),
    _RlBrgIpmFdbRefGroupAddress_Type()
)
rlBrgIpmFdbRefGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefGroupAddress.setStatus("current")
_RlBrgIpmFdbRefSourceAddressType_Type = InetAddressType
_RlBrgIpmFdbRefSourceAddressType_Object = MibTableColumn
rlBrgIpmFdbRefSourceAddressType = _RlBrgIpmFdbRefSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 7, 1, 4),
    _RlBrgIpmFdbRefSourceAddressType_Type()
)
rlBrgIpmFdbRefSourceAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefSourceAddressType.setStatus("current")
_RlBrgIpmFdbRefSourceAddress_Type = InetAddress
_RlBrgIpmFdbRefSourceAddress_Object = MibTableColumn
rlBrgIpmFdbRefSourceAddress = _RlBrgIpmFdbRefSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 7, 1, 5),
    _RlBrgIpmFdbRefSourceAddress_Type()
)
rlBrgIpmFdbRefSourceAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefSourceAddress.setStatus("current")
_RlBrgIpmFdbRefPorts_Type = PortList
_RlBrgIpmFdbRefPorts_Object = MibTableColumn
rlBrgIpmFdbRefPorts = _RlBrgIpmFdbRefPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 7, 1, 6),
    _RlBrgIpmFdbRefPorts_Type()
)
rlBrgIpmFdbRefPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlBrgIpmFdbRefPorts.setStatus("current")
_RlBrgDynamicCmdTable_Object = MibTable
rlBrgDynamicCmdTable = _RlBrgDynamicCmdTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 8)
)
if mibBuilder.loadTexts:
    rlBrgDynamicCmdTable.setStatus("current")
_RlBrgDynamicCmdEntry_Object = MibTableRow
rlBrgDynamicCmdEntry = _RlBrgDynamicCmdEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 8, 1)
)
rlBrgDynamicCmdEntry.setIndexNames(
    (0, "CISCOSB-rlBrgMulticast-MIB", "rlBrgDynamicCmdKey"),
)
if mibBuilder.loadTexts:
    rlBrgDynamicCmdEntry.setStatus("current")


class _RlBrgDynamicCmdKey_Type(Integer32):
    """Custom type rlBrgDynamicCmdKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_RlBrgDynamicCmdKey_Type.__name__ = "Integer32"
_RlBrgDynamicCmdKey_Object = MibTableColumn
rlBrgDynamicCmdKey = _RlBrgDynamicCmdKey_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 8, 1, 1),
    _RlBrgDynamicCmdKey_Type()
)
rlBrgDynamicCmdKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdKey.setStatus("current")
_RlBrgDynamicCmdVlanTag_Type = VlanIndex
_RlBrgDynamicCmdVlanTag_Object = MibTableColumn
rlBrgDynamicCmdVlanTag = _RlBrgDynamicCmdVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 8, 1, 2),
    _RlBrgDynamicCmdVlanTag_Type()
)
rlBrgDynamicCmdVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdVlanTag.setStatus("current")
_RlBrgDynamicCmdGroupAddressType_Type = InetAddressType
_RlBrgDynamicCmdGroupAddressType_Object = MibTableColumn
rlBrgDynamicCmdGroupAddressType = _RlBrgDynamicCmdGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 8, 1, 3),
    _RlBrgDynamicCmdGroupAddressType_Type()
)
rlBrgDynamicCmdGroupAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdGroupAddressType.setStatus("current")
_RlBrgDynamicCmdGroupAddress_Type = InetAddress
_RlBrgDynamicCmdGroupAddress_Object = MibTableColumn
rlBrgDynamicCmdGroupAddress = _RlBrgDynamicCmdGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 8, 1, 4),
    _RlBrgDynamicCmdGroupAddress_Type()
)
rlBrgDynamicCmdGroupAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdGroupAddress.setStatus("current")
_RlBrgDynamicCmdSourceAddressType_Type = InetAddressType
_RlBrgDynamicCmdSourceAddressType_Object = MibTableColumn
rlBrgDynamicCmdSourceAddressType = _RlBrgDynamicCmdSourceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 8, 1, 5),
    _RlBrgDynamicCmdSourceAddressType_Type()
)
rlBrgDynamicCmdSourceAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdSourceAddressType.setStatus("current")
_RlBrgDynamicCmdSourceAddress_Type = InetAddress
_RlBrgDynamicCmdSourceAddress_Object = MibTableColumn
rlBrgDynamicCmdSourceAddress = _RlBrgDynamicCmdSourceAddress_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 8, 1, 6),
    _RlBrgDynamicCmdSourceAddress_Type()
)
rlBrgDynamicCmdSourceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdSourceAddress.setStatus("current")
_RlBrgDynamicCmdPorts_Type = PortList
_RlBrgDynamicCmdPorts_Object = MibTableColumn
rlBrgDynamicCmdPorts = _RlBrgDynamicCmdPorts_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 8, 1, 7),
    _RlBrgDynamicCmdPorts_Type()
)
rlBrgDynamicCmdPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdPorts.setStatus("current")
_RlBrgDynamicCmdType_Type = DynamicCmdType
_RlBrgDynamicCmdType_Object = MibTableColumn
rlBrgDynamicCmdType = _RlBrgDynamicCmdType_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 116, 8, 1, 8),
    _RlBrgDynamicCmdType_Type()
)
rlBrgDynamicCmdType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlBrgDynamicCmdType.setStatus("current")

# Managed Objects groups


# Notification objects

rlMacMulticastUnregFilterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 1)
)
rlMacMulticastUnregFilterFailed.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlMacMulticastUnregFilterFailed.setStatus(
        ""
    )

rlIgmpMldSnoopTriplePlayPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 0, 208)
)
rlIgmpMldSnoopTriplePlayPort.setObjects(
      *(("CISCOSB-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("CISCOSB-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopTriplePlayPort.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-rlBrgMulticast-MIB",
    **{"IgmpVersion": IgmpVersion,
       "DynamicCmdType": DynamicCmdType,
       "rlMacMulticastUnregFilterFailed": rlMacMulticastUnregFilterFailed,
       "rlIgmpMldSnoopTriplePlayPort": rlIgmpMldSnoopTriplePlayPort,
       "rlMacMulticast": rlMacMulticast,
       "rlMacMulticastEnable": rlMacMulticastEnable,
       "rlIgmpSnoop": rlIgmpSnoop,
       "rlIgmpSnoopMibVersion": rlIgmpSnoopMibVersion,
       "rlIgmpSnoopEnable": rlIgmpSnoopEnable,
       "rlIgmpSnoopHostAgingTime": rlIgmpSnoopHostAgingTime,
       "rlIgmpSnoopRouterAgingTime": rlIgmpSnoopRouterAgingTime,
       "rlIgmpSnoopVlanTable": rlIgmpSnoopVlanTable,
       "rlIgmpSnoopVlanEntry": rlIgmpSnoopVlanEntry,
       "rlIgmpSnoopVlanTag": rlIgmpSnoopVlanTag,
       "rlIgmpSnoopVlanEnable": rlIgmpSnoopVlanEnable,
       "rlIgmpSnoopVlanRouterLearn": rlIgmpSnoopVlanRouterLearn,
       "rlIgmpSnoopVlanHostTimeOut": rlIgmpSnoopVlanHostTimeOut,
       "rlIgmpSnoopVlanQuerierTimeOut": rlIgmpSnoopVlanQuerierTimeOut,
       "rlIgmpSnoopVlanRouterTimeOut": rlIgmpSnoopVlanRouterTimeOut,
       "rlIgmpSnoopVlanLeaveTimeOut": rlIgmpSnoopVlanLeaveTimeOut,
       "rlIgmpSnoopVlanIgmpVersion": rlIgmpSnoopVlanIgmpVersion,
       "rlIgmpSnoopVlanRouterPortlist": rlIgmpSnoopVlanRouterPortlist,
       "rlIgmpSnoopIGMP224ReportsHandle": rlIgmpSnoopIGMP224ReportsHandle,
       "rlIgmpSnoopMulticastTvTable": rlIgmpSnoopMulticastTvTable,
       "rlIgmpSnoopMulticastTvEntry": rlIgmpSnoopMulticastTvEntry,
       "rlIgmpSnoopMulticastTvVID": rlIgmpSnoopMulticastTvVID,
       "rlIgmpSnoopMulticastTvGroup": rlIgmpSnoopMulticastTvGroup,
       "rlIgmpSnoopMulticastTvStatus": rlIgmpSnoopMulticastTvStatus,
       "rlIgmpSnoopMembershipTable": rlIgmpSnoopMembershipTable,
       "rlIgmpSnoopMembershipEntry": rlIgmpSnoopMembershipEntry,
       "rlIgmpSnoopMembershipVlanTag": rlIgmpSnoopMembershipVlanTag,
       "rlIgmpSnoopMembershipGroupIpAddress": rlIgmpSnoopMembershipGroupIpAddress,
       "rlIgmpSnoopMembershipSourceIpAddress": rlIgmpSnoopMembershipSourceIpAddress,
       "rlIgmpSnoopMembershipIncPortlist": rlIgmpSnoopMembershipIncPortlist,
       "rlIgmpSnoopMembershipExcPortlist": rlIgmpSnoopMembershipExcPortlist,
       "rlIgmpSnoopMembershipExpiryTime": rlIgmpSnoopMembershipExpiryTime,
       "rlIgmpSnoopMembershipCompatibilityMode": rlIgmpSnoopMembershipCompatibilityMode,
       "rlIgmpSnoopQuerierVlanTable": rlIgmpSnoopQuerierVlanTable,
       "rlIgmpSnoopQuerierVlanEntry": rlIgmpSnoopQuerierVlanEntry,
       "rlIgmpSnoopQuerierVlanTag": rlIgmpSnoopQuerierVlanTag,
       "rlIgmpSnoopQuerierAdminEnable": rlIgmpSnoopQuerierAdminEnable,
       "rlIgmpSnoopQuerierOperEnable": rlIgmpSnoopQuerierOperEnable,
       "rlIgmpSnoopQuerierAdminAddr": rlIgmpSnoopQuerierAdminAddr,
       "rlIgmpSnoopQuerierOperAddr": rlIgmpSnoopQuerierOperAddr,
       "rlIgmpSnoopQuerierAdminVersionNumber": rlIgmpSnoopQuerierAdminVersionNumber,
       "rlIgmpSnoopQuerierOperVersionNumber": rlIgmpSnoopQuerierOperVersionNumber,
       "rlMacMulticastMaxEntriesNum": rlMacMulticastMaxEntriesNum,
       "rlMacMulticastFilter": rlMacMulticastFilter,
       "rlMacMulticastUnregFilterEnable": rlMacMulticastUnregFilterEnable,
       "rlMldSnoop": rlMldSnoop,
       "rlMldSnoopEnable": rlMldSnoopEnable,
       "rlMldSnoopHostAgingTime": rlMldSnoopHostAgingTime,
       "rlMldSnoopRouterAgingTime": rlMldSnoopRouterAgingTime,
       "rlIgmpMldSnoopMembershipTable": rlIgmpMldSnoopMembershipTable,
       "rlIgmpMldSnoopMembershipEntry": rlIgmpMldSnoopMembershipEntry,
       "rlIgmpMldSnoopMembershipVlanTag": rlIgmpMldSnoopMembershipVlanTag,
       "rlIgmpMldSnoopMembershipGroupIpAddressType": rlIgmpMldSnoopMembershipGroupIpAddressType,
       "rlIgmpMldSnoopMembershipGroupIpAddress": rlIgmpMldSnoopMembershipGroupIpAddress,
       "rlIgmpMldSnoopMembershipSourceIpAddressType": rlIgmpMldSnoopMembershipSourceIpAddressType,
       "rlIgmpMldSnoopMembershipSourceIpAddress": rlIgmpMldSnoopMembershipSourceIpAddress,
       "rlIgmpMldSnoopMembershipIncPortlist": rlIgmpMldSnoopMembershipIncPortlist,
       "rlIgmpMldSnoopMembershipExcPortlist": rlIgmpMldSnoopMembershipExcPortlist,
       "rlIgmpMldSnoopMembershipExpiryTime": rlIgmpMldSnoopMembershipExpiryTime,
       "rlIgmpMldSnoopMembershipCompatibilityMode": rlIgmpMldSnoopMembershipCompatibilityMode,
       "rlIgmpMldSnoopVlanTable": rlIgmpMldSnoopVlanTable,
       "rlIgmpMldSnoopVlanEntry": rlIgmpMldSnoopVlanEntry,
       "rlIgmpMldSnoopVlanInetAddressType": rlIgmpMldSnoopVlanInetAddressType,
       "rlIgmpMldSnoopVlanTag": rlIgmpMldSnoopVlanTag,
       "rlIgmpMldSnoopVlanEnable": rlIgmpMldSnoopVlanEnable,
       "rlIgmpMldSnoopVlanRouterLearn": rlIgmpMldSnoopVlanRouterLearn,
       "rlIgmpMldSnoopVlanHostTimeOut": rlIgmpMldSnoopVlanHostTimeOut,
       "rlIgmpMldSnoopVlanQuerierTimeOut": rlIgmpMldSnoopVlanQuerierTimeOut,
       "rlIgmpMldSnoopVlanRouterTimeOut": rlIgmpMldSnoopVlanRouterTimeOut,
       "rlIgmpMldSnoopVlanLeaveTimeOut": rlIgmpMldSnoopVlanLeaveTimeOut,
       "rlIgmpMldSnoopVlanIgmpVersion": rlIgmpMldSnoopVlanIgmpVersion,
       "rlIgmpMldSnoopVlanRouterPortlist": rlIgmpMldSnoopVlanRouterPortlist,
       "rlIgmpMldSnoopVlanRouterStaticPortlist": rlIgmpMldSnoopVlanRouterStaticPortlist,
       "rlIgmpMldSnoopVlanRouterForbiddenPortlist": rlIgmpMldSnoopVlanRouterForbiddenPortlist,
       "rlIgmpMldSnoopVlanQueryOverride": rlIgmpMldSnoopVlanQueryOverride,
       "rlIgmpMldSnoopVlanOperRobustness": rlIgmpMldSnoopVlanOperRobustness,
       "rlIgmpMldSnoopVlanOperQueryInterval": rlIgmpMldSnoopVlanOperQueryInterval,
       "rlIgmpMldSnoopVlanOperQueryMaxResponseTime": rlIgmpMldSnoopVlanOperQueryMaxResponseTime,
       "rlIgmpMldSnoopVlanOperLastMemberQueryInterval": rlIgmpMldSnoopVlanOperLastMemberQueryInterval,
       "rlIgmpMldSnoopVlanOperLastMemberQueryCount": rlIgmpMldSnoopVlanOperLastMemberQueryCount,
       "rlIgmpMldSnoopVlanOperStartupQueryInterval": rlIgmpMldSnoopVlanOperStartupQueryInterval,
       "rlIgmpMldSnoopVlanOperStartupQueryCount": rlIgmpMldSnoopVlanOperStartupQueryCount,
       "rlIgmpMldSnoopVlanOperHostTimeOut": rlIgmpMldSnoopVlanOperHostTimeOut,
       "rlIgmpMldSnoopVlanOperRouterTimeOut": rlIgmpMldSnoopVlanOperRouterTimeOut,
       "rlIgmpMldSnoopVlanOperLeaveTimeOut": rlIgmpMldSnoopVlanOperLeaveTimeOut,
       "rlIgmpMldSnoopVlanAdminRobustness": rlIgmpMldSnoopVlanAdminRobustness,
       "rlIgmpMldSnoopVlanAdminQueryInterval": rlIgmpMldSnoopVlanAdminQueryInterval,
       "rlIgmpMldSnoopVlanAdminQueryMaxResponseTime": rlIgmpMldSnoopVlanAdminQueryMaxResponseTime,
       "rlIgmpMldSnoopVlanAdminLastMemberQueryInterval": rlIgmpMldSnoopVlanAdminLastMemberQueryInterval,
       "rlIgmpMldSnoopVlanAdminLastMemberQueryCount": rlIgmpMldSnoopVlanAdminLastMemberQueryCount,
       "rlIgmpMldSnoopVlanAdminStartupQueryInterval": rlIgmpMldSnoopVlanAdminStartupQueryInterval,
       "rlIgmpMldSnoopVlanAdminStartupQueryCount": rlIgmpMldSnoopVlanAdminStartupQueryCount,
       "rlIgmpMldSnoopVlanAdminHostTimeOut": rlIgmpMldSnoopVlanAdminHostTimeOut,
       "rlIgmpMldSnoopVlanAdminRouterTimeOut": rlIgmpMldSnoopVlanAdminRouterTimeOut,
       "rlIgmpMldSnoopVlanAdminLeaveTimeOut": rlIgmpMldSnoopVlanAdminLeaveTimeOut,
       "rlIgmpMldSnoopVlanIsImmediateLeave": rlIgmpMldSnoopVlanIsImmediateLeave,
       "rlIgmpMldSnoopMulticastTvTable": rlIgmpMldSnoopMulticastTvTable,
       "rlIgmpMldSnoopMulticastTvEntry": rlIgmpMldSnoopMulticastTvEntry,
       "rlIgmpMldSnoopMulticastTvInetAddressType": rlIgmpMldSnoopMulticastTvInetAddressType,
       "rlIgmpMldSnoopMulticastTvVID": rlIgmpMldSnoopMulticastTvVID,
       "rlIgmpMldSnoopMulticastTvGroupAddressType": rlIgmpMldSnoopMulticastTvGroupAddressType,
       "rlIgmpMldSnoopMulticastTvGroup": rlIgmpMldSnoopMulticastTvGroup,
       "rlIgmpMldSnoopMulticastTvStatus": rlIgmpMldSnoopMulticastTvStatus,
       "rlIgmpMldSnoopQuerierVlanTable": rlIgmpMldSnoopQuerierVlanTable,
       "rlIgmpMldSnoopQuerierVlanEntry": rlIgmpMldSnoopQuerierVlanEntry,
       "rlIgmpMldSnoopQuerierVlanTag": rlIgmpMldSnoopQuerierVlanTag,
       "rlIgmpMldSnoopQuerierAdminEnable": rlIgmpMldSnoopQuerierAdminEnable,
       "rlIgmpMldSnoopQuerierOperEnable": rlIgmpMldSnoopQuerierOperEnable,
       "rlIgmpMldSnoopQuerierAdminAddrInetAddressType": rlIgmpMldSnoopQuerierAdminAddrInetAddressType,
       "rlIgmpMldSnoopQuerierAdminAddr": rlIgmpMldSnoopQuerierAdminAddr,
       "rlIgmpMldSnoopQuerierOperAddrInetAddressType": rlIgmpMldSnoopQuerierOperAddrInetAddressType,
       "rlIgmpMldSnoopQuerierOperAddr": rlIgmpMldSnoopQuerierOperAddr,
       "rlIgmpMldSnoopQuerierAdminVersionNumber": rlIgmpMldSnoopQuerierAdminVersionNumber,
       "rlIgmpMldSnoopQuerierOperVersionNumber": rlIgmpMldSnoopQuerierOperVersionNumber,
       "rlBrgMulticastMibVersion": rlBrgMulticastMibVersion,
       "rlBrgStaticIpMulticastTable": rlBrgStaticIpMulticastTable,
       "rlBrgStaticIpMulticastEntry": rlBrgStaticIpMulticastEntry,
       "rlBrgStaticIpMulticastVlanTag": rlBrgStaticIpMulticastVlanTag,
       "rlBrgStaticIpMulticastGroupAddress": rlBrgStaticIpMulticastGroupAddress,
       "rlBrgStaticIpMulticastSourceAddress": rlBrgStaticIpMulticastSourceAddress,
       "rlBrgStaticIpMulticastFrwPorts": rlBrgStaticIpMulticastFrwPorts,
       "rlBrgStaticIpMulticastForbiddenPorts": rlBrgStaticIpMulticastForbiddenPorts,
       "rlBrgStaticIpMulticastStatus": rlBrgStaticIpMulticastStatus,
       "rlBrgIpMulticastTable": rlBrgIpMulticastTable,
       "rlBrgIpMulticastEntry": rlBrgIpMulticastEntry,
       "rlBrgIpMulticastVlanTag": rlBrgIpMulticastVlanTag,
       "rlBrgIpMulticastGroupAddress": rlBrgIpMulticastGroupAddress,
       "rlBrgIpMulticastSourceAddress": rlBrgIpMulticastSourceAddress,
       "rlBrgIpMulticastEgressPorts": rlBrgIpMulticastEgressPorts,
       "rlBrgIpMulticastLearntPorts": rlBrgIpMulticastLearntPorts,
       "rlBrgStaticInetMulticastTable": rlBrgStaticInetMulticastTable,
       "rlBrgStaticInetMulticastEntry": rlBrgStaticInetMulticastEntry,
       "rlBrgStaticInetMulticastVlanTag": rlBrgStaticInetMulticastVlanTag,
       "rlBrgStaticInetMulticastGroupAddressType": rlBrgStaticInetMulticastGroupAddressType,
       "rlBrgStaticInetMulticastGroupAddress": rlBrgStaticInetMulticastGroupAddress,
       "rlBrgStaticInetMulticastSourceAddressType": rlBrgStaticInetMulticastSourceAddressType,
       "rlBrgStaticInetMulticastSourceAddress": rlBrgStaticInetMulticastSourceAddress,
       "rlBrgStaticInetMulticastFrwPorts": rlBrgStaticInetMulticastFrwPorts,
       "rlBrgStaticInetMulticastForbiddenPorts": rlBrgStaticInetMulticastForbiddenPorts,
       "rlBrgStaticInetMulticastStatus": rlBrgStaticInetMulticastStatus,
       "rlBrgInetMulticastTable": rlBrgInetMulticastTable,
       "rlBrgInetMulticastEntry": rlBrgInetMulticastEntry,
       "rlBrgInetMulticastVlanTag": rlBrgInetMulticastVlanTag,
       "rlBrgInetMulticastGroupAddressType": rlBrgInetMulticastGroupAddressType,
       "rlBrgInetMulticastGroupAddress": rlBrgInetMulticastGroupAddress,
       "rlBrgInetMulticastSourceAddressType": rlBrgInetMulticastSourceAddressType,
       "rlBrgInetMulticastSourceAddress": rlBrgInetMulticastSourceAddress,
       "rlBrgInetMulticastEgressPorts": rlBrgInetMulticastEgressPorts,
       "rlBrgInetMulticastLearntPorts": rlBrgInetMulticastLearntPorts,
       "rlBrgIpmFdbRefTable": rlBrgIpmFdbRefTable,
       "rlBrgIpmFdbRefEntry": rlBrgIpmFdbRefEntry,
       "rlBrgIpmFdbRefVlanTag": rlBrgIpmFdbRefVlanTag,
       "rlBrgIpmFdbRefGroupAddressType": rlBrgIpmFdbRefGroupAddressType,
       "rlBrgIpmFdbRefGroupAddress": rlBrgIpmFdbRefGroupAddress,
       "rlBrgIpmFdbRefSourceAddressType": rlBrgIpmFdbRefSourceAddressType,
       "rlBrgIpmFdbRefSourceAddress": rlBrgIpmFdbRefSourceAddress,
       "rlBrgIpmFdbRefPorts": rlBrgIpmFdbRefPorts,
       "rlBrgDynamicCmdTable": rlBrgDynamicCmdTable,
       "rlBrgDynamicCmdEntry": rlBrgDynamicCmdEntry,
       "rlBrgDynamicCmdKey": rlBrgDynamicCmdKey,
       "rlBrgDynamicCmdVlanTag": rlBrgDynamicCmdVlanTag,
       "rlBrgDynamicCmdGroupAddressType": rlBrgDynamicCmdGroupAddressType,
       "rlBrgDynamicCmdGroupAddress": rlBrgDynamicCmdGroupAddress,
       "rlBrgDynamicCmdSourceAddressType": rlBrgDynamicCmdSourceAddressType,
       "rlBrgDynamicCmdSourceAddress": rlBrgDynamicCmdSourceAddress,
       "rlBrgDynamicCmdPorts": rlBrgDynamicCmdPorts,
       "rlBrgDynamicCmdType": rlBrgDynamicCmdType}
)
