# SNMP MIB module (RADLAN-rlMacMulticast-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RADLAN-rlMacMulticast-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:09 2024
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
 InetAddressType,
 InetVersion) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetVersion")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

(rndErrorDesc,
 rndErrorSeverity) = mibBuilder.importSymbols(
    "RADLAN-DEVICEPARAMS-MIB",
    "rndErrorDesc",
    "rndErrorSeverity")

(rlMacMulticast,
 rnd,
 rndNotifications) = mibBuilder.importSymbols(
    "RADLAN-MIB",
    "rlMacMulticast",
    "rnd",
    "rndNotifications")

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



class MldVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("v1", 1),
          ("v2", 2))
    )



# MIB Managed Objects in the order of their OIDs

_RlMacMulticastEnable_Type = TruthValue
_RlMacMulticastEnable_Object = MibScalar
rlMacMulticastEnable = _RlMacMulticastEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 1),
    _RlMacMulticastEnable_Type()
)
rlMacMulticastEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacMulticastEnable.setStatus("current")
_RlIgmpSnoop_ObjectIdentity = ObjectIdentity
rlIgmpSnoop = _RlIgmpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 55, 2)
)
_RlIgmpSnoopMibVersion_Type = Integer32
_RlIgmpSnoopMibVersion_Object = MibScalar
rlIgmpSnoopMibVersion = _RlIgmpSnoopMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 1),
    _RlIgmpSnoopMibVersion_Type()
)
rlIgmpSnoopMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMibVersion.setStatus("current")
_RlIgmpSnoopEnable_Type = TruthValue
_RlIgmpSnoopEnable_Object = MibScalar
rlIgmpSnoopEnable = _RlIgmpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 4),
    _RlIgmpSnoopRouterAgingTime_Type()
)
rlIgmpSnoopRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopRouterAgingTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlIgmpSnoopRouterAgingTime.setUnits("seconds")
_RlIgmpSnoopVlanTable_Object = MibTable
rlIgmpSnoopVlanTable = _RlIgmpSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7)
)
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanTable.setStatus("obsolete")
_RlIgmpSnoopVlanEntry_Object = MibTableRow
rlIgmpSnoopVlanEntry = _RlIgmpSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7, 1)
)
rlIgmpSnoopVlanEntry.setIndexNames(
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpSnoopVlanTag"),
)
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanEntry.setStatus("obsolete")
_RlIgmpSnoopVlanTag_Type = Integer32
_RlIgmpSnoopVlanTag_Object = MibTableColumn
rlIgmpSnoopVlanTag = _RlIgmpSnoopVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7, 1, 1),
    _RlIgmpSnoopVlanTag_Type()
)
rlIgmpSnoopVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanTag.setStatus("obsolete")
_RlIgmpSnoopVlanEnable_Type = TruthValue
_RlIgmpSnoopVlanEnable_Object = MibTableColumn
rlIgmpSnoopVlanEnable = _RlIgmpSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7, 1, 2),
    _RlIgmpSnoopVlanEnable_Type()
)
rlIgmpSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanEnable.setStatus("obsolete")
_RlIgmpSnoopVlanRouterLearn_Type = TruthValue
_RlIgmpSnoopVlanRouterLearn_Object = MibTableColumn
rlIgmpSnoopVlanRouterLearn = _RlIgmpSnoopVlanRouterLearn_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7, 1, 8),
    _RlIgmpSnoopVlanIgmpVersion_Type()
)
rlIgmpSnoopVlanIgmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopVlanIgmpVersion.setStatus("obsolete")
_RlIgmpSnoopVlanRouterPortlist_Type = PortList
_RlIgmpSnoopVlanRouterPortlist_Object = MibTableColumn
rlIgmpSnoopVlanRouterPortlist = _RlIgmpSnoopVlanRouterPortlist_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 7, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 8),
    _RlIgmpSnoopIGMP224ReportsHandle_Type()
)
rlIgmpSnoopIGMP224ReportsHandle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopIGMP224ReportsHandle.setStatus("current")
_RlIgmpSnoopMulticastTvTable_Object = MibTable
rlIgmpSnoopMulticastTvTable = _RlIgmpSnoopMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 10)
)
if mibBuilder.loadTexts:
    rlIgmpSnoopMulticastTvTable.setStatus("current")
_RlIgmpSnoopMulticastTvEntry_Object = MibTableRow
rlIgmpSnoopMulticastTvEntry = _RlIgmpSnoopMulticastTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 10, 1)
)
rlIgmpSnoopMulticastTvEntry.setIndexNames(
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpSnoopMulticastTvVID"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpSnoopMulticastTvGroup"),
)
if mibBuilder.loadTexts:
    rlIgmpSnoopMulticastTvEntry.setStatus("current")
_RlIgmpSnoopMulticastTvVID_Type = VlanIndex
_RlIgmpSnoopMulticastTvVID_Object = MibTableColumn
rlIgmpSnoopMulticastTvVID = _RlIgmpSnoopMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 10, 1, 1),
    _RlIgmpSnoopMulticastTvVID_Type()
)
rlIgmpSnoopMulticastTvVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMulticastTvVID.setStatus("current")
_RlIgmpSnoopMulticastTvGroup_Type = IpAddress
_RlIgmpSnoopMulticastTvGroup_Object = MibTableColumn
rlIgmpSnoopMulticastTvGroup = _RlIgmpSnoopMulticastTvGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 10, 1, 2),
    _RlIgmpSnoopMulticastTvGroup_Type()
)
rlIgmpSnoopMulticastTvGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMulticastTvGroup.setStatus("current")
_RlIgmpSnoopMulticastTvStatus_Type = RowStatus
_RlIgmpSnoopMulticastTvStatus_Object = MibTableColumn
rlIgmpSnoopMulticastTvStatus = _RlIgmpSnoopMulticastTvStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 10, 1, 3),
    _RlIgmpSnoopMulticastTvStatus_Type()
)
rlIgmpSnoopMulticastTvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopMulticastTvStatus.setStatus("current")
_RlIgmpSnoopMembershipTable_Object = MibTable
rlIgmpSnoopMembershipTable = _RlIgmpSnoopMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 11)
)
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipTable.setStatus("current")
_RlIgmpSnoopMembershipEntry_Object = MibTableRow
rlIgmpSnoopMembershipEntry = _RlIgmpSnoopMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 11, 1)
)
rlIgmpSnoopMembershipEntry.setIndexNames(
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpSnoopMembershipVlanTag"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpSnoopMembershipGroupIpAddress"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpSnoopMembershipSourceIpAddress"),
)
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipEntry.setStatus("current")
_RlIgmpSnoopMembershipVlanTag_Type = VlanIndex
_RlIgmpSnoopMembershipVlanTag_Object = MibTableColumn
rlIgmpSnoopMembershipVlanTag = _RlIgmpSnoopMembershipVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 11, 1, 1),
    _RlIgmpSnoopMembershipVlanTag_Type()
)
rlIgmpSnoopMembershipVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipVlanTag.setStatus("current")
_RlIgmpSnoopMembershipGroupIpAddress_Type = IpAddress
_RlIgmpSnoopMembershipGroupIpAddress_Object = MibTableColumn
rlIgmpSnoopMembershipGroupIpAddress = _RlIgmpSnoopMembershipGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 11, 1, 2),
    _RlIgmpSnoopMembershipGroupIpAddress_Type()
)
rlIgmpSnoopMembershipGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipGroupIpAddress.setStatus("current")
_RlIgmpSnoopMembershipSourceIpAddress_Type = IpAddress
_RlIgmpSnoopMembershipSourceIpAddress_Object = MibTableColumn
rlIgmpSnoopMembershipSourceIpAddress = _RlIgmpSnoopMembershipSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 11, 1, 3),
    _RlIgmpSnoopMembershipSourceIpAddress_Type()
)
rlIgmpSnoopMembershipSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipSourceIpAddress.setStatus("current")
_RlIgmpSnoopMembershipIncPortlist_Type = PortList
_RlIgmpSnoopMembershipIncPortlist_Object = MibTableColumn
rlIgmpSnoopMembershipIncPortlist = _RlIgmpSnoopMembershipIncPortlist_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 11, 1, 4),
    _RlIgmpSnoopMembershipIncPortlist_Type()
)
rlIgmpSnoopMembershipIncPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipIncPortlist.setStatus("current")
_RlIgmpSnoopMembershipExcPortlist_Type = PortList
_RlIgmpSnoopMembershipExcPortlist_Object = MibTableColumn
rlIgmpSnoopMembershipExcPortlist = _RlIgmpSnoopMembershipExcPortlist_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 11, 1, 5),
    _RlIgmpSnoopMembershipExcPortlist_Type()
)
rlIgmpSnoopMembershipExcPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipExcPortlist.setStatus("current")
_RlIgmpSnoopMembershipExpiryTime_Type = Integer32
_RlIgmpSnoopMembershipExpiryTime_Object = MibTableColumn
rlIgmpSnoopMembershipExpiryTime = _RlIgmpSnoopMembershipExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 11, 1, 6),
    _RlIgmpSnoopMembershipExpiryTime_Type()
)
rlIgmpSnoopMembershipExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipExpiryTime.setStatus("obsolete")
_RlIgmpSnoopMembershipCompatibilityMode_Type = IgmpVersion
_RlIgmpSnoopMembershipCompatibilityMode_Object = MibTableColumn
rlIgmpSnoopMembershipCompatibilityMode = _RlIgmpSnoopMembershipCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 11, 1, 7),
    _RlIgmpSnoopMembershipCompatibilityMode_Type()
)
rlIgmpSnoopMembershipCompatibilityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopMembershipCompatibilityMode.setStatus("current")
_RlIgmpSnoopQuerierVlanTable_Object = MibTable
rlIgmpSnoopQuerierVlanTable = _RlIgmpSnoopQuerierVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 12)
)
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierVlanTable.setStatus("current")
_RlIgmpSnoopQuerierVlanEntry_Object = MibTableRow
rlIgmpSnoopQuerierVlanEntry = _RlIgmpSnoopQuerierVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 12, 1)
)
rlIgmpSnoopQuerierVlanEntry.setIndexNames(
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpSnoopQuerierVlanTag"),
)
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierVlanEntry.setStatus("current")
_RlIgmpSnoopQuerierVlanTag_Type = VlanIndex
_RlIgmpSnoopQuerierVlanTag_Object = MibTableColumn
rlIgmpSnoopQuerierVlanTag = _RlIgmpSnoopQuerierVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 12, 1, 1),
    _RlIgmpSnoopQuerierVlanTag_Type()
)
rlIgmpSnoopQuerierVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierVlanTag.setStatus("current")
_RlIgmpSnoopQuerierAdminEnable_Type = TruthValue
_RlIgmpSnoopQuerierAdminEnable_Object = MibTableColumn
rlIgmpSnoopQuerierAdminEnable = _RlIgmpSnoopQuerierAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 12, 1, 2),
    _RlIgmpSnoopQuerierAdminEnable_Type()
)
rlIgmpSnoopQuerierAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierAdminEnable.setStatus("current")
_RlIgmpSnoopQuerierOperEnable_Type = TruthValue
_RlIgmpSnoopQuerierOperEnable_Object = MibTableColumn
rlIgmpSnoopQuerierOperEnable = _RlIgmpSnoopQuerierOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 12, 1, 3),
    _RlIgmpSnoopQuerierOperEnable_Type()
)
rlIgmpSnoopQuerierOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierOperEnable.setStatus("current")
_RlIgmpSnoopQuerierAdminAddr_Type = IpAddress
_RlIgmpSnoopQuerierAdminAddr_Object = MibTableColumn
rlIgmpSnoopQuerierAdminAddr = _RlIgmpSnoopQuerierAdminAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 12, 1, 4),
    _RlIgmpSnoopQuerierAdminAddr_Type()
)
rlIgmpSnoopQuerierAdminAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierAdminAddr.setStatus("current")
_RlIgmpSnoopQuerierOperAddr_Type = IpAddress
_RlIgmpSnoopQuerierOperAddr_Object = MibTableColumn
rlIgmpSnoopQuerierOperAddr = _RlIgmpSnoopQuerierOperAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 12, 1, 5),
    _RlIgmpSnoopQuerierOperAddr_Type()
)
rlIgmpSnoopQuerierOperAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierOperAddr.setStatus("current")
_RlIgmpSnoopQuerierAdminVersionNumber_Type = IgmpVersion
_RlIgmpSnoopQuerierAdminVersionNumber_Object = MibTableColumn
rlIgmpSnoopQuerierAdminVersionNumber = _RlIgmpSnoopQuerierAdminVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 12, 1, 6),
    _RlIgmpSnoopQuerierAdminVersionNumber_Type()
)
rlIgmpSnoopQuerierAdminVersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierAdminVersionNumber.setStatus("current")
_RlIgmpSnoopQuerierOperVersionNumber_Type = IgmpVersion
_RlIgmpSnoopQuerierOperVersionNumber_Object = MibTableColumn
rlIgmpSnoopQuerierOperVersionNumber = _RlIgmpSnoopQuerierOperVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 12, 1, 7),
    _RlIgmpSnoopQuerierOperVersionNumber_Type()
)
rlIgmpSnoopQuerierOperVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierOperVersionNumber.setStatus("current")
_RlIgmpSnoopQuerierElectionEnable_Type = TruthValue
_RlIgmpSnoopQuerierElectionEnable_Object = MibTableColumn
rlIgmpSnoopQuerierElectionEnable = _RlIgmpSnoopQuerierElectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 12, 1, 8),
    _RlIgmpSnoopQuerierElectionEnable_Type()
)
rlIgmpSnoopQuerierElectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierElectionEnable.setStatus("current")
_RlIgmpSnoopQuerierEnable_Type = TruthValue
_RlIgmpSnoopQuerierEnable_Object = MibScalar
rlIgmpSnoopQuerierEnable = _RlIgmpSnoopQuerierEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 2, 13),
    _RlIgmpSnoopQuerierEnable_Type()
)
rlIgmpSnoopQuerierEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpSnoopQuerierEnable.setStatus("current")
_RlMacMulticastMaxEntriesNum_Type = Integer32
_RlMacMulticastMaxEntriesNum_Object = MibScalar
rlMacMulticastMaxEntriesNum = _RlMacMulticastMaxEntriesNum_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 3),
    _RlMacMulticastMaxEntriesNum_Type()
)
rlMacMulticastMaxEntriesNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMacMulticastMaxEntriesNum.setStatus("current")
_RlMacMulticastFilter_ObjectIdentity = ObjectIdentity
rlMacMulticastFilter = _RlMacMulticastFilter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 55, 4)
)
_RlMacMulticastUnregFilterEnable_Type = PortList
_RlMacMulticastUnregFilterEnable_Object = MibScalar
rlMacMulticastUnregFilterEnable = _RlMacMulticastUnregFilterEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 4, 1),
    _RlMacMulticastUnregFilterEnable_Type()
)
rlMacMulticastUnregFilterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMacMulticastUnregFilterEnable.setStatus("current")
_RlMldSnoop_ObjectIdentity = ObjectIdentity
rlMldSnoop = _RlMldSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 89, 55, 5)
)
_RlMldSnoopEnable_Type = TruthValue
_RlMldSnoopEnable_Object = MibScalar
rlMldSnoopEnable = _RlMldSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 3),
    _RlMldSnoopRouterAgingTime_Type()
)
rlMldSnoopRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMldSnoopRouterAgingTime.setStatus("obsolete")
if mibBuilder.loadTexts:
    rlMldSnoopRouterAgingTime.setUnits("seconds")
_RlIgmpMldSnoopMembershipTable_Object = MibTable
rlIgmpMldSnoopMembershipTable = _RlIgmpMldSnoopMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4)
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipTable.setStatus("current")
_RlIgmpMldSnoopMembershipEntry_Object = MibTableRow
rlIgmpMldSnoopMembershipEntry = _RlIgmpMldSnoopMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4, 1)
)
rlIgmpMldSnoopMembershipEntry.setIndexNames(
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopMembershipVlanTag"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopMembershipGroupIpAddressType"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopMembershipGroupIpAddress"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopMembershipSourceIpAddressType"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopMembershipSourceIpAddress"),
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipEntry.setStatus("current")
_RlIgmpMldSnoopMembershipVlanTag_Type = VlanIndex
_RlIgmpMldSnoopMembershipVlanTag_Object = MibTableColumn
rlIgmpMldSnoopMembershipVlanTag = _RlIgmpMldSnoopMembershipVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4, 1, 1),
    _RlIgmpMldSnoopMembershipVlanTag_Type()
)
rlIgmpMldSnoopMembershipVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipVlanTag.setStatus("current")
_RlIgmpMldSnoopMembershipGroupIpAddressType_Type = InetAddressType
_RlIgmpMldSnoopMembershipGroupIpAddressType_Object = MibTableColumn
rlIgmpMldSnoopMembershipGroupIpAddressType = _RlIgmpMldSnoopMembershipGroupIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4, 1, 2),
    _RlIgmpMldSnoopMembershipGroupIpAddressType_Type()
)
rlIgmpMldSnoopMembershipGroupIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipGroupIpAddressType.setStatus("current")
_RlIgmpMldSnoopMembershipGroupIpAddress_Type = InetAddress
_RlIgmpMldSnoopMembershipGroupIpAddress_Object = MibTableColumn
rlIgmpMldSnoopMembershipGroupIpAddress = _RlIgmpMldSnoopMembershipGroupIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4, 1, 3),
    _RlIgmpMldSnoopMembershipGroupIpAddress_Type()
)
rlIgmpMldSnoopMembershipGroupIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipGroupIpAddress.setStatus("current")
_RlIgmpMldSnoopMembershipSourceIpAddressType_Type = InetAddressType
_RlIgmpMldSnoopMembershipSourceIpAddressType_Object = MibTableColumn
rlIgmpMldSnoopMembershipSourceIpAddressType = _RlIgmpMldSnoopMembershipSourceIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4, 1, 4),
    _RlIgmpMldSnoopMembershipSourceIpAddressType_Type()
)
rlIgmpMldSnoopMembershipSourceIpAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipSourceIpAddressType.setStatus("current")
_RlIgmpMldSnoopMembershipSourceIpAddress_Type = InetAddress
_RlIgmpMldSnoopMembershipSourceIpAddress_Object = MibTableColumn
rlIgmpMldSnoopMembershipSourceIpAddress = _RlIgmpMldSnoopMembershipSourceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4, 1, 5),
    _RlIgmpMldSnoopMembershipSourceIpAddress_Type()
)
rlIgmpMldSnoopMembershipSourceIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipSourceIpAddress.setStatus("current")
_RlIgmpMldSnoopMembershipIncPortlist_Type = PortList
_RlIgmpMldSnoopMembershipIncPortlist_Object = MibTableColumn
rlIgmpMldSnoopMembershipIncPortlist = _RlIgmpMldSnoopMembershipIncPortlist_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4, 1, 6),
    _RlIgmpMldSnoopMembershipIncPortlist_Type()
)
rlIgmpMldSnoopMembershipIncPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipIncPortlist.setStatus("current")
_RlIgmpMldSnoopMembershipExcPortlist_Type = PortList
_RlIgmpMldSnoopMembershipExcPortlist_Object = MibTableColumn
rlIgmpMldSnoopMembershipExcPortlist = _RlIgmpMldSnoopMembershipExcPortlist_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4, 1, 7),
    _RlIgmpMldSnoopMembershipExcPortlist_Type()
)
rlIgmpMldSnoopMembershipExcPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipExcPortlist.setStatus("current")
_RlIgmpMldSnoopMembershipExpiryTime_Type = Integer32
_RlIgmpMldSnoopMembershipExpiryTime_Object = MibTableColumn
rlIgmpMldSnoopMembershipExpiryTime = _RlIgmpMldSnoopMembershipExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4, 1, 8),
    _RlIgmpMldSnoopMembershipExpiryTime_Type()
)
rlIgmpMldSnoopMembershipExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipExpiryTime.setStatus("obsolete")
_RlIgmpMldSnoopMembershipCompatibilityMode_Type = IgmpVersion
_RlIgmpMldSnoopMembershipCompatibilityMode_Object = MibTableColumn
rlIgmpMldSnoopMembershipCompatibilityMode = _RlIgmpMldSnoopMembershipCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 4, 1, 9),
    _RlIgmpMldSnoopMembershipCompatibilityMode_Type()
)
rlIgmpMldSnoopMembershipCompatibilityMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMembershipCompatibilityMode.setStatus("current")
_RlIgmpMldSnoopVlanTable_Object = MibTable
rlIgmpMldSnoopVlanTable = _RlIgmpMldSnoopVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5)
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanTable.setStatus("current")
_RlIgmpMldSnoopVlanEntry_Object = MibTableRow
rlIgmpMldSnoopVlanEntry = _RlIgmpMldSnoopVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1)
)
rlIgmpMldSnoopVlanEntry.setIndexNames(
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopVlanInetAddressType"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopVlanTag"),
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanEntry.setStatus("current")
_RlIgmpMldSnoopVlanInetAddressType_Type = InetAddressType
_RlIgmpMldSnoopVlanInetAddressType_Object = MibTableColumn
rlIgmpMldSnoopVlanInetAddressType = _RlIgmpMldSnoopVlanInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 1),
    _RlIgmpMldSnoopVlanInetAddressType_Type()
)
rlIgmpMldSnoopVlanInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanInetAddressType.setStatus("current")
_RlIgmpMldSnoopVlanTag_Type = Integer32
_RlIgmpMldSnoopVlanTag_Object = MibTableColumn
rlIgmpMldSnoopVlanTag = _RlIgmpMldSnoopVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 2),
    _RlIgmpMldSnoopVlanTag_Type()
)
rlIgmpMldSnoopVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanTag.setStatus("current")
_RlIgmpMldSnoopVlanEnable_Type = TruthValue
_RlIgmpMldSnoopVlanEnable_Object = MibTableColumn
rlIgmpMldSnoopVlanEnable = _RlIgmpMldSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 3),
    _RlIgmpMldSnoopVlanEnable_Type()
)
rlIgmpMldSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanEnable.setStatus("current")
_RlIgmpMldSnoopVlanRouterLearn_Type = TruthValue
_RlIgmpMldSnoopVlanRouterLearn_Object = MibTableColumn
rlIgmpMldSnoopVlanRouterLearn = _RlIgmpMldSnoopVlanRouterLearn_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 9),
    _RlIgmpMldSnoopVlanIgmpVersion_Type()
)
rlIgmpMldSnoopVlanIgmpVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanIgmpVersion.setStatus("current")
_RlIgmpMldSnoopVlanRouterPortlist_Type = PortList
_RlIgmpMldSnoopVlanRouterPortlist_Object = MibTableColumn
rlIgmpMldSnoopVlanRouterPortlist = _RlIgmpMldSnoopVlanRouterPortlist_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 10),
    _RlIgmpMldSnoopVlanRouterPortlist_Type()
)
rlIgmpMldSnoopVlanRouterPortlist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanRouterPortlist.setStatus("current")
_RlIgmpMldSnoopVlanRouterStaticPortlist_Type = PortList
_RlIgmpMldSnoopVlanRouterStaticPortlist_Object = MibTableColumn
rlIgmpMldSnoopVlanRouterStaticPortlist = _RlIgmpMldSnoopVlanRouterStaticPortlist_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 11),
    _RlIgmpMldSnoopVlanRouterStaticPortlist_Type()
)
rlIgmpMldSnoopVlanRouterStaticPortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanRouterStaticPortlist.setStatus("current")
_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Type = PortList
_RlIgmpMldSnoopVlanRouterForbiddenPortlist_Object = MibTableColumn
rlIgmpMldSnoopVlanRouterForbiddenPortlist = _RlIgmpMldSnoopVlanRouterForbiddenPortlist_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 12),
    _RlIgmpMldSnoopVlanRouterForbiddenPortlist_Type()
)
rlIgmpMldSnoopVlanRouterForbiddenPortlist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanRouterForbiddenPortlist.setStatus("current")
_RlIgmpMldSnoopVlanQueryOverride_Type = TruthValue
_RlIgmpMldSnoopVlanQueryOverride_Object = MibTableColumn
rlIgmpMldSnoopVlanQueryOverride = _RlIgmpMldSnoopVlanQueryOverride_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 19),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 21),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 22),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 23),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 24),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 25),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 26),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 27),
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
        ValueRangeConstraint(0, 7),
    )


_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Type.__name__ = "Unsigned32"
_RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Object = MibTableColumn
rlIgmpMldSnoopVlanAdminLastMemberQueryCount = _RlIgmpMldSnoopVlanAdminLastMemberQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 28),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 29),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 30),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 31),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 32),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 33),
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
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 5, 1, 34),
    _RlIgmpMldSnoopVlanIsImmediateLeave_Type()
)
rlIgmpMldSnoopVlanIsImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopVlanIsImmediateLeave.setStatus("current")
_RlIgmpMldSnoopMulticastTvTable_Object = MibTable
rlIgmpMldSnoopMulticastTvTable = _RlIgmpMldSnoopMulticastTvTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 6)
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvTable.setStatus("current")
_RlIgmpMldSnoopMulticastTvEntry_Object = MibTableRow
rlIgmpMldSnoopMulticastTvEntry = _RlIgmpMldSnoopMulticastTvEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 6, 1)
)
rlIgmpMldSnoopMulticastTvEntry.setIndexNames(
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopMulticastTvInetAddressType"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopMulticastTvVID"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopMulticastTvGroupAddressType"),
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopMulticastTvGroup"),
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvEntry.setStatus("current")
_RlIgmpMldSnoopMulticastTvInetAddressType_Type = InetAddressType
_RlIgmpMldSnoopMulticastTvInetAddressType_Object = MibTableColumn
rlIgmpMldSnoopMulticastTvInetAddressType = _RlIgmpMldSnoopMulticastTvInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 6, 1, 1),
    _RlIgmpMldSnoopMulticastTvInetAddressType_Type()
)
rlIgmpMldSnoopMulticastTvInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvInetAddressType.setStatus("current")
_RlIgmpMldSnoopMulticastTvVID_Type = VlanIndex
_RlIgmpMldSnoopMulticastTvVID_Object = MibTableColumn
rlIgmpMldSnoopMulticastTvVID = _RlIgmpMldSnoopMulticastTvVID_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 6, 1, 2),
    _RlIgmpMldSnoopMulticastTvVID_Type()
)
rlIgmpMldSnoopMulticastTvVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvVID.setStatus("current")
_RlIgmpMldSnoopMulticastTvGroupAddressType_Type = InetAddressType
_RlIgmpMldSnoopMulticastTvGroupAddressType_Object = MibTableColumn
rlIgmpMldSnoopMulticastTvGroupAddressType = _RlIgmpMldSnoopMulticastTvGroupAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 6, 1, 3),
    _RlIgmpMldSnoopMulticastTvGroupAddressType_Type()
)
rlIgmpMldSnoopMulticastTvGroupAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvGroupAddressType.setStatus("current")
_RlIgmpMldSnoopMulticastTvGroup_Type = InetAddress
_RlIgmpMldSnoopMulticastTvGroup_Object = MibTableColumn
rlIgmpMldSnoopMulticastTvGroup = _RlIgmpMldSnoopMulticastTvGroup_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 6, 1, 4),
    _RlIgmpMldSnoopMulticastTvGroup_Type()
)
rlIgmpMldSnoopMulticastTvGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvGroup.setStatus("current")
_RlIgmpMldSnoopMulticastTvStatus_Type = RowStatus
_RlIgmpMldSnoopMulticastTvStatus_Object = MibTableColumn
rlIgmpMldSnoopMulticastTvStatus = _RlIgmpMldSnoopMulticastTvStatus_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 6, 1, 5),
    _RlIgmpMldSnoopMulticastTvStatus_Type()
)
rlIgmpMldSnoopMulticastTvStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopMulticastTvStatus.setStatus("current")
_RlMldSnoopQuerierVlanTable_Object = MibTable
rlMldSnoopQuerierVlanTable = _RlMldSnoopQuerierVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7)
)
if mibBuilder.loadTexts:
    rlMldSnoopQuerierVlanTable.setStatus("current")
_RlMldSnoopQuerierVlanEntry_Object = MibTableRow
rlMldSnoopQuerierVlanEntry = _RlMldSnoopQuerierVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1)
)
rlMldSnoopQuerierVlanEntry.setIndexNames(
    (0, "RADLAN-rlMacMulticast-MIB", "rlMldSnoopQuerierVlanTag"),
)
if mibBuilder.loadTexts:
    rlMldSnoopQuerierVlanEntry.setStatus("current")
_RlMldSnoopQuerierVlanTag_Type = VlanIndex
_RlMldSnoopQuerierVlanTag_Object = MibTableColumn
rlMldSnoopQuerierVlanTag = _RlMldSnoopQuerierVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1, 1),
    _RlMldSnoopQuerierVlanTag_Type()
)
rlMldSnoopQuerierVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierVlanTag.setStatus("current")
_RlMldSnoopQuerierAdminEnable_Type = TruthValue
_RlMldSnoopQuerierAdminEnable_Object = MibTableColumn
rlMldSnoopQuerierAdminEnable = _RlMldSnoopQuerierAdminEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1, 2),
    _RlMldSnoopQuerierAdminEnable_Type()
)
rlMldSnoopQuerierAdminEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierAdminEnable.setStatus("current")
_RlMldSnoopQuerierOperEnable_Type = TruthValue
_RlMldSnoopQuerierOperEnable_Object = MibTableColumn
rlMldSnoopQuerierOperEnable = _RlMldSnoopQuerierOperEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1, 3),
    _RlMldSnoopQuerierOperEnable_Type()
)
rlMldSnoopQuerierOperEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierOperEnable.setStatus("current")
_RlMldSnoopQuerierAdminAddrInetAddressType_Type = InetAddressType
_RlMldSnoopQuerierAdminAddrInetAddressType_Object = MibTableColumn
rlMldSnoopQuerierAdminAddrInetAddressType = _RlMldSnoopQuerierAdminAddrInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1, 4),
    _RlMldSnoopQuerierAdminAddrInetAddressType_Type()
)
rlMldSnoopQuerierAdminAddrInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierAdminAddrInetAddressType.setStatus("current")
_RlMldSnoopQuerierAdminAddr_Type = InetAddress
_RlMldSnoopQuerierAdminAddr_Object = MibTableColumn
rlMldSnoopQuerierAdminAddr = _RlMldSnoopQuerierAdminAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1, 5),
    _RlMldSnoopQuerierAdminAddr_Type()
)
rlMldSnoopQuerierAdminAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierAdminAddr.setStatus("current")
_RlMldSnoopQuerierOperAddrInetAddressType_Type = InetAddressType
_RlMldSnoopQuerierOperAddrInetAddressType_Object = MibTableColumn
rlMldSnoopQuerierOperAddrInetAddressType = _RlMldSnoopQuerierOperAddrInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1, 6),
    _RlMldSnoopQuerierOperAddrInetAddressType_Type()
)
rlMldSnoopQuerierOperAddrInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierOperAddrInetAddressType.setStatus("current")
_RlMldSnoopQuerierOperAddr_Type = InetAddress
_RlMldSnoopQuerierOperAddr_Object = MibTableColumn
rlMldSnoopQuerierOperAddr = _RlMldSnoopQuerierOperAddr_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1, 7),
    _RlMldSnoopQuerierOperAddr_Type()
)
rlMldSnoopQuerierOperAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierOperAddr.setStatus("current")
_RlMldSnoopQuerierAdminVersionNumber_Type = MldVersion
_RlMldSnoopQuerierAdminVersionNumber_Object = MibTableColumn
rlMldSnoopQuerierAdminVersionNumber = _RlMldSnoopQuerierAdminVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1, 8),
    _RlMldSnoopQuerierAdminVersionNumber_Type()
)
rlMldSnoopQuerierAdminVersionNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierAdminVersionNumber.setStatus("current")
_RlMldSnoopQuerierOperVersionNumber_Type = MldVersion
_RlMldSnoopQuerierOperVersionNumber_Object = MibTableColumn
rlMldSnoopQuerierOperVersionNumber = _RlMldSnoopQuerierOperVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1, 9),
    _RlMldSnoopQuerierOperVersionNumber_Type()
)
rlMldSnoopQuerierOperVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierOperVersionNumber.setStatus("current")
_RlMldSnoopQuerierElectionEnable_Type = TruthValue
_RlMldSnoopQuerierElectionEnable_Object = MibTableColumn
rlMldSnoopQuerierElectionEnable = _RlMldSnoopQuerierElectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 7, 1, 10),
    _RlMldSnoopQuerierElectionEnable_Type()
)
rlMldSnoopQuerierElectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierElectionEnable.setStatus("current")
_RlMldSnoopQuerierEnable_Type = TruthValue
_RlMldSnoopQuerierEnable_Object = MibScalar
rlMldSnoopQuerierEnable = _RlMldSnoopQuerierEnable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 8),
    _RlMldSnoopQuerierEnable_Type()
)
rlMldSnoopQuerierEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlMldSnoopQuerierEnable.setStatus("current")
_RlIgmpMldSnoopQuerierGlobalAddressTable_Object = MibTable
rlIgmpMldSnoopQuerierGlobalAddressTable = _RlIgmpMldSnoopQuerierGlobalAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 9)
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierGlobalAddressTable.setStatus("current")
_RlIgmpMldSnoopQuerierGlobalAddressEntry_Object = MibTableRow
rlIgmpMldSnoopQuerierGlobalAddressEntry = _RlIgmpMldSnoopQuerierGlobalAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 9, 1)
)
rlIgmpMldSnoopQuerierGlobalAddressEntry.setIndexNames(
    (0, "RADLAN-rlMacMulticast-MIB", "rlIgmpMldSnoopQuerierGlobalAddressIPVersion"),
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierGlobalAddressEntry.setStatus("current")
_RlIgmpMldSnoopQuerierGlobalAddressIPVersion_Type = InetVersion
_RlIgmpMldSnoopQuerierGlobalAddressIPVersion_Object = MibTableColumn
rlIgmpMldSnoopQuerierGlobalAddressIPVersion = _RlIgmpMldSnoopQuerierGlobalAddressIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 9, 1, 1),
    _RlIgmpMldSnoopQuerierGlobalAddressIPVersion_Type()
)
rlIgmpMldSnoopQuerierGlobalAddressIPVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierGlobalAddressIPVersion.setStatus("current")
_RlIgmpMldSnoopQuerierGlobalAddressType_Type = InetAddressType
_RlIgmpMldSnoopQuerierGlobalAddressType_Object = MibTableColumn
rlIgmpMldSnoopQuerierGlobalAddressType = _RlIgmpMldSnoopQuerierGlobalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 9, 1, 2),
    _RlIgmpMldSnoopQuerierGlobalAddressType_Type()
)
rlIgmpMldSnoopQuerierGlobalAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierGlobalAddressType.setStatus("current")
_RlIgmpMldSnoopQuerierGlobalAddress_Type = InetAddress
_RlIgmpMldSnoopQuerierGlobalAddress_Object = MibTableColumn
rlIgmpMldSnoopQuerierGlobalAddress = _RlIgmpMldSnoopQuerierGlobalAddress_Object(
    (1, 3, 6, 1, 4, 1, 89, 55, 5, 9, 1, 3),
    _RlIgmpMldSnoopQuerierGlobalAddress_Type()
)
rlIgmpMldSnoopQuerierGlobalAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIgmpMldSnoopQuerierGlobalAddress.setStatus("current")

# Managed Objects groups


# Notification objects

rlMacMulticastUnregFilterFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 1)
)
rlMacMulticastUnregFilterFailed.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlMacMulticastUnregFilterFailed.setStatus(
        ""
    )

rlIgmpMldSnoopTriplePlayPort = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 208)
)
rlIgmpMldSnoopTriplePlayPort.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlIgmpMldSnoopTriplePlayPort.setStatus(
        "current"
    )

rlbrgIgmpSnoopQrrDuplicateIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 89, 0, 227)
)
rlbrgIgmpSnoopQrrDuplicateIP.setObjects(
      *(("RADLAN-DEVICEPARAMS-MIB", "rndErrorDesc"),
        ("RADLAN-DEVICEPARAMS-MIB", "rndErrorSeverity"))
)
if mibBuilder.loadTexts:
    rlbrgIgmpSnoopQrrDuplicateIP.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RADLAN-rlMacMulticast-MIB",
    **{"IgmpVersion": IgmpVersion,
       "MldVersion": MldVersion,
       "rlMacMulticastUnregFilterFailed": rlMacMulticastUnregFilterFailed,
       "rlIgmpMldSnoopTriplePlayPort": rlIgmpMldSnoopTriplePlayPort,
       "rlbrgIgmpSnoopQrrDuplicateIP": rlbrgIgmpSnoopQrrDuplicateIP,
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
       "rlIgmpSnoopQuerierElectionEnable": rlIgmpSnoopQuerierElectionEnable,
       "rlIgmpSnoopQuerierEnable": rlIgmpSnoopQuerierEnable,
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
       "rlMldSnoopQuerierVlanTable": rlMldSnoopQuerierVlanTable,
       "rlMldSnoopQuerierVlanEntry": rlMldSnoopQuerierVlanEntry,
       "rlMldSnoopQuerierVlanTag": rlMldSnoopQuerierVlanTag,
       "rlMldSnoopQuerierAdminEnable": rlMldSnoopQuerierAdminEnable,
       "rlMldSnoopQuerierOperEnable": rlMldSnoopQuerierOperEnable,
       "rlMldSnoopQuerierAdminAddrInetAddressType": rlMldSnoopQuerierAdminAddrInetAddressType,
       "rlMldSnoopQuerierAdminAddr": rlMldSnoopQuerierAdminAddr,
       "rlMldSnoopQuerierOperAddrInetAddressType": rlMldSnoopQuerierOperAddrInetAddressType,
       "rlMldSnoopQuerierOperAddr": rlMldSnoopQuerierOperAddr,
       "rlMldSnoopQuerierAdminVersionNumber": rlMldSnoopQuerierAdminVersionNumber,
       "rlMldSnoopQuerierOperVersionNumber": rlMldSnoopQuerierOperVersionNumber,
       "rlMldSnoopQuerierElectionEnable": rlMldSnoopQuerierElectionEnable,
       "rlMldSnoopQuerierEnable": rlMldSnoopQuerierEnable,
       "rlIgmpMldSnoopQuerierGlobalAddressTable": rlIgmpMldSnoopQuerierGlobalAddressTable,
       "rlIgmpMldSnoopQuerierGlobalAddressEntry": rlIgmpMldSnoopQuerierGlobalAddressEntry,
       "rlIgmpMldSnoopQuerierGlobalAddressIPVersion": rlIgmpMldSnoopQuerierGlobalAddressIPVersion,
       "rlIgmpMldSnoopQuerierGlobalAddressType": rlIgmpMldSnoopQuerierGlobalAddressType,
       "rlIgmpMldSnoopQuerierGlobalAddress": rlIgmpMldSnoopQuerierGlobalAddress}
)
