# SNMP MIB module (A3COM0503-PORTINFO) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/A3COM0503-PORTINFO
# Produced by pysmi-1.5.4 at Mon Oct 14 20:31:23 2024
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

(a3ComVlanGroup,) = mibBuilder.importSymbols(
    "GENERIC-3COM-VLAN-MIB-1-0-7",
    "a3ComVlanGroup")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
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


# Types definitions



class VlanList(OctetString):
    """Custom type VlanList based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PortInfoTable_Object = MibTable
portInfoTable = _PortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    portInfoTable.setStatus("current")
_PortInfoEntry_Object = MibTableRow
portInfoEntry = _PortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1)
)
portInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    portInfoEntry.setStatus("current")
_PortInfoEgressVlans_Type = VlanList
_PortInfoEgressVlans_Object = MibTableColumn
portInfoEgressVlans = _PortInfoEgressVlans_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 1),
    _PortInfoEgressVlans_Type()
)
portInfoEgressVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoEgressVlans.setStatus("current")
_PortInfoForbiddenEgressVlans_Type = VlanList
_PortInfoForbiddenEgressVlans_Object = MibTableColumn
portInfoForbiddenEgressVlans = _PortInfoForbiddenEgressVlans_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 2),
    _PortInfoForbiddenEgressVlans_Type()
)
portInfoForbiddenEgressVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoForbiddenEgressVlans.setStatus("current")
_PortInfoUntaggedVlans_Type = VlanList
_PortInfoUntaggedVlans_Object = MibTableColumn
portInfoUntaggedVlans = _PortInfoUntaggedVlans_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 3),
    _PortInfoUntaggedVlans_Type()
)
portInfoUntaggedVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoUntaggedVlans.setStatus("current")


class _PortInfoStpPortPriority_Type(Integer32):
    """Custom type portInfoStpPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PortInfoStpPortPriority_Type.__name__ = "Integer32"
_PortInfoStpPortPriority_Object = MibTableColumn
portInfoStpPortPriority = _PortInfoStpPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 4),
    _PortInfoStpPortPriority_Type()
)
portInfoStpPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoStpPortPriority.setStatus("current")


class _PortInfoStpPortEnable_Type(Integer32):
    """Custom type portInfoStpPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )


_PortInfoStpPortEnable_Type.__name__ = "Integer32"
_PortInfoStpPortEnable_Object = MibTableColumn
portInfoStpPortEnable = _PortInfoStpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 5),
    _PortInfoStpPortEnable_Type()
)
portInfoStpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoStpPortEnable.setStatus("current")


class _PortInfoPvid_Type(VlanIndex):
    """Custom type portInfoPvid based on VlanIndex"""
    defaultValue = 1


_PortInfoPvid_Object = MibTableColumn
portInfoPvid = _PortInfoPvid_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 6),
    _PortInfoPvid_Type()
)
portInfoPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoPvid.setStatus("current")


class _PortInfoAcceptableFrameTypes_Type(Integer32):
    """Custom type portInfoAcceptableFrameTypes based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("admitAll", 1),
          ("admitOnlyVlanTagged", 2))
    )


_PortInfoAcceptableFrameTypes_Type.__name__ = "Integer32"
_PortInfoAcceptableFrameTypes_Object = MibTableColumn
portInfoAcceptableFrameTypes = _PortInfoAcceptableFrameTypes_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 7),
    _PortInfoAcceptableFrameTypes_Type()
)
portInfoAcceptableFrameTypes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoAcceptableFrameTypes.setStatus("current")


class _PortInfoIngressFiltering_Type(TruthValue):
    """Custom type portInfoIngressFiltering based on TruthValue"""


_PortInfoIngressFiltering_Object = MibTableColumn
portInfoIngressFiltering = _PortInfoIngressFiltering_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 3, 1, 8),
    _PortInfoIngressFiltering_Type()
)
portInfoIngressFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portInfoIngressFiltering.setStatus("current")
_PortInfoFdbTable_Object = MibTable
portInfoFdbTable = _PortInfoFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4)
)
if mibBuilder.loadTexts:
    portInfoFdbTable.setStatus("mandatory")
_PortInfoFdbEntry_Object = MibTableRow
portInfoFdbEntry = _PortInfoFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1)
)
portInfoFdbEntry.setIndexNames(
    (0, "A3COM0503-PORTINFO", "portInfoFdbIndex"),
    (0, "A3COM0503-PORTINFO", "portInfoFdbVlan"),
    (0, "A3COM0503-PORTINFO", "portInfoFdbAddress"),
)
if mibBuilder.loadTexts:
    portInfoFdbEntry.setStatus("mandatory")


class _PortInfoFdbIndex_Type(Integer32):
    """Custom type portInfoFdbIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortInfoFdbIndex_Type.__name__ = "Integer32"
_PortInfoFdbIndex_Object = MibTableColumn
portInfoFdbIndex = _PortInfoFdbIndex_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 1),
    _PortInfoFdbIndex_Type()
)
portInfoFdbIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portInfoFdbIndex.setStatus("mandatory")
_PortInfoFdbVlan_Type = VlanIndex
_PortInfoFdbVlan_Object = MibTableColumn
portInfoFdbVlan = _PortInfoFdbVlan_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 2),
    _PortInfoFdbVlan_Type()
)
portInfoFdbVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portInfoFdbVlan.setStatus("mandatory")
_PortInfoFdbAddress_Type = MacAddress
_PortInfoFdbAddress_Object = MibTableColumn
portInfoFdbAddress = _PortInfoFdbAddress_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 3),
    _PortInfoFdbAddress_Type()
)
portInfoFdbAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portInfoFdbAddress.setStatus("mandatory")
_PortInfoFdbStatus_Type = RowStatus
_PortInfoFdbStatus_Object = MibTableColumn
portInfoFdbStatus = _PortInfoFdbStatus_Object(
    (1, 3, 6, 1, 4, 1, 43, 10, 1, 14, 1, 4, 1, 4),
    _PortInfoFdbStatus_Type()
)
portInfoFdbStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInfoFdbStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "A3COM0503-PORTINFO",
    **{"VlanList": VlanList,
       "portInfoTable": portInfoTable,
       "portInfoEntry": portInfoEntry,
       "portInfoEgressVlans": portInfoEgressVlans,
       "portInfoForbiddenEgressVlans": portInfoForbiddenEgressVlans,
       "portInfoUntaggedVlans": portInfoUntaggedVlans,
       "portInfoStpPortPriority": portInfoStpPortPriority,
       "portInfoStpPortEnable": portInfoStpPortEnable,
       "portInfoPvid": portInfoPvid,
       "portInfoAcceptableFrameTypes": portInfoAcceptableFrameTypes,
       "portInfoIngressFiltering": portInfoIngressFiltering,
       "portInfoFdbTable": portInfoFdbTable,
       "portInfoFdbEntry": portInfoFdbEntry,
       "portInfoFdbIndex": portInfoFdbIndex,
       "portInfoFdbVlan": portInfoFdbVlan,
       "portInfoFdbAddress": portInfoFdbAddress,
       "portInfoFdbStatus": portInfoFdbStatus}
)
