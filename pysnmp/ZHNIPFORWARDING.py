# SNMP MIB module (ZHNIPFORWARDING) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHNIPFORWARDING
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:00 2024
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

(DisplayString,
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zhoneWtn,) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneWtn")

(ZhoneRowStatus,) = mibBuilder.importSymbols(
    "Zhone-TC",
    "ZhoneRowStatus")


# MODULE-IDENTITY

zhnIpForwarding = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44)
)
zhnIpForwarding.setRevisions(
        ("2012-01-27 12:00",
         "2012-04-20 12:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhnIpForwardingObjects_ObjectIdentity = ObjectIdentity
zhnIpForwardingObjects = _ZhnIpForwardingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1)
)
_IpForwardingTable_Object = MibTable
ipForwardingTable = _IpForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1, 1)
)
if mibBuilder.loadTexts:
    ipForwardingTable.setStatus("current")
_IpForwardingEntry_Object = MibTableRow
ipForwardingEntry = _IpForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1, 1, 1)
)
ipForwardingEntry.setIndexNames(
    (0, "ZHNIPFORWARDING", "ipForwardingIndex"),
)
if mibBuilder.loadTexts:
    ipForwardingEntry.setStatus("current")
_IpForwardingIndex_Type = Unsigned32
_IpForwardingIndex_Object = MibTableColumn
ipForwardingIndex = _IpForwardingIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1, 1, 1, 1),
    _IpForwardingIndex_Type()
)
ipForwardingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipForwardingIndex.setStatus("current")
_IpForwardingIPVersion_Type = Unsigned32
_IpForwardingIPVersion_Object = MibTableColumn
ipForwardingIPVersion = _IpForwardingIPVersion_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1, 1, 1, 2),
    _IpForwardingIPVersion_Type()
)
ipForwardingIPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipForwardingIPVersion.setStatus("current")
_IpForwardingDestIPAddress_Type = IpAddress
_IpForwardingDestIPAddress_Object = MibTableColumn
ipForwardingDestIPAddress = _IpForwardingDestIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1, 1, 1, 3),
    _IpForwardingDestIPAddress_Type()
)
ipForwardingDestIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardingDestIPAddress.setStatus("current")
_IpForwardingDestSubnetMask_Type = IpAddress
_IpForwardingDestSubnetMask_Object = MibTableColumn
ipForwardingDestSubnetMask = _IpForwardingDestSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1, 1, 1, 4),
    _IpForwardingDestSubnetMask_Type()
)
ipForwardingDestSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardingDestSubnetMask.setStatus("current")
_IpForwardingInterface_Type = OctetString
_IpForwardingInterface_Object = MibTableColumn
ipForwardingInterface = _IpForwardingInterface_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1, 1, 1, 5),
    _IpForwardingInterface_Type()
)
ipForwardingInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardingInterface.setStatus("current")
_IpForwardingGatewayIPAddress_Type = IpAddress
_IpForwardingGatewayIPAddress_Object = MibTableColumn
ipForwardingGatewayIPAddress = _IpForwardingGatewayIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1, 1, 1, 6),
    _IpForwardingGatewayIPAddress_Type()
)
ipForwardingGatewayIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardingGatewayIPAddress.setStatus("current")


class _IpForwardingForwardingMetric_Type(Integer32):
    """Custom type ipForwardingForwardingMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_IpForwardingForwardingMetric_Type.__name__ = "Integer32"
_IpForwardingForwardingMetric_Object = MibTableColumn
ipForwardingForwardingMetric = _IpForwardingForwardingMetric_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1, 1, 1, 7),
    _IpForwardingForwardingMetric_Type()
)
ipForwardingForwardingMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardingForwardingMetric.setStatus("current")
_IpForwardingTableRowStatus_Type = ZhoneRowStatus
_IpForwardingTableRowStatus_Object = MibTableColumn
ipForwardingTableRowStatus = _IpForwardingTableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 1, 1, 1, 8),
    _IpForwardingTableRowStatus_Type()
)
ipForwardingTableRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipForwardingTableRowStatus.setStatus("current")
_ZhnIpForwardingConformance_ObjectIdentity = ObjectIdentity
zhnIpForwardingConformance = _ZhnIpForwardingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 2)
)
_ZhnIpForwardingGroups_ObjectIdentity = ObjectIdentity
zhnIpForwardingGroups = _ZhnIpForwardingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 2, 1)
)
_ZhnIpForwardingCompliances_ObjectIdentity = ObjectIdentity
zhnIpForwardingCompliances = _ZhnIpForwardingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 2, 2)
)

# Managed Objects groups

zhnIpForwardingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 2, 1, 1)
)
zhnIpForwardingGroup.setObjects(
      *(("ZHNIPFORWARDING", "ipForwardingIPVersion"),
        ("ZHNIPFORWARDING", "ipForwardingDestIPAddress"),
        ("ZHNIPFORWARDING", "ipForwardingDestSubnetMask"),
        ("ZHNIPFORWARDING", "ipForwardingInterface"),
        ("ZHNIPFORWARDING", "ipForwardingGatewayIPAddress"),
        ("ZHNIPFORWARDING", "ipForwardingForwardingMetric"),
        ("ZHNIPFORWARDING", "ipForwardingTableRowStatus"))
)
if mibBuilder.loadTexts:
    zhnIpForwardingGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

zhnIpForwardingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5504, 2, 5, 44, 2, 2, 1)
)
if mibBuilder.loadTexts:
    zhnIpForwardingCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHNIPFORWARDING",
    **{"zhnIpForwarding": zhnIpForwarding,
       "zhnIpForwardingObjects": zhnIpForwardingObjects,
       "ipForwardingTable": ipForwardingTable,
       "ipForwardingEntry": ipForwardingEntry,
       "ipForwardingIndex": ipForwardingIndex,
       "ipForwardingIPVersion": ipForwardingIPVersion,
       "ipForwardingDestIPAddress": ipForwardingDestIPAddress,
       "ipForwardingDestSubnetMask": ipForwardingDestSubnetMask,
       "ipForwardingInterface": ipForwardingInterface,
       "ipForwardingGatewayIPAddress": ipForwardingGatewayIPAddress,
       "ipForwardingForwardingMetric": ipForwardingForwardingMetric,
       "ipForwardingTableRowStatus": ipForwardingTableRowStatus,
       "zhnIpForwardingConformance": zhnIpForwardingConformance,
       "zhnIpForwardingGroups": zhnIpForwardingGroups,
       "zhnIpForwardingGroup": zhnIpForwardingGroup,
       "zhnIpForwardingCompliances": zhnIpForwardingCompliances,
       "zhnIpForwardingCompliance": zhnIpForwardingCompliance}
)
