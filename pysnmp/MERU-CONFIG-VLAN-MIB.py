# SNMP MIB module (MERU-CONFIG-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MERU-CONFIG-VLAN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:10 2024
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

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

(mwConfiguration,) = mibBuilder.importSymbols(
    "MERU-SMI",
    "mwConfiguration")

(MwlOnOffSwitch,
 MwlProfileOwner) = mibBuilder.importSymbols(
    "MERU-TC",
    "MwlOnOffSwitch",
    "MwlProfileOwner")

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
 MacAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

mwConfigVlan = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MwVlanTable_Object = MibTable
mwVlanTable = _MwVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1)
)
if mibBuilder.loadTexts:
    mwVlanTable.setStatus("current")
_MwVlanEntry_Object = MibTableRow
mwVlanEntry = _MwVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1)
)
mwVlanEntry.setIndexNames(
    (0, "MERU-CONFIG-VLAN-MIB", "mwVlanTableIndex"),
)
if mibBuilder.loadTexts:
    mwVlanEntry.setStatus("current")
_MwVlanTableIndex_Type = Integer32
_MwVlanTableIndex_Object = MibTableColumn
mwVlanTableIndex = _MwVlanTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 1),
    _MwVlanTableIndex_Type()
)
mwVlanTableIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mwVlanTableIndex.setStatus("current")
_MwVlanTag_Type = Unsigned32
_MwVlanTag_Object = MibTableColumn
mwVlanTag = _MwVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 2),
    _MwVlanTag_Type()
)
mwVlanTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanTag.setStatus("current")


class _MwVlanName_Type(DisplayString):
    """Custom type mwVlanName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_MwVlanName_Type.__name__ = "DisplayString"
_MwVlanName_Object = MibTableColumn
mwVlanName = _MwVlanName_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 3),
    _MwVlanName_Type()
)
mwVlanName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanName.setStatus("current")
_MwVlanNetMask_Type = IpAddress
_MwVlanNetMask_Object = MibTableColumn
mwVlanNetMask = _MwVlanNetMask_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 4),
    _MwVlanNetMask_Type()
)
mwVlanNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanNetMask.setStatus("current")
_MwVlanIpAddress_Type = IpAddress
_MwVlanIpAddress_Object = MibTableColumn
mwVlanIpAddress = _MwVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 5),
    _MwVlanIpAddress_Type()
)
mwVlanIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanIpAddress.setStatus("current")
_MwVlanInterfaceIndex_Type = Unsigned32
_MwVlanInterfaceIndex_Object = MibTableColumn
mwVlanInterfaceIndex = _MwVlanInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 6),
    _MwVlanInterfaceIndex_Type()
)
mwVlanInterfaceIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanInterfaceIndex.setStatus("current")
_MwVlanDefaultGateway_Type = IpAddress
_MwVlanDefaultGateway_Object = MibTableColumn
mwVlanDefaultGateway = _MwVlanDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 7),
    _MwVlanDefaultGateway_Type()
)
mwVlanDefaultGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanDefaultGateway.setStatus("current")
_MwVlanDHCPServerIpAddress_Type = IpAddress
_MwVlanDHCPServerIpAddress_Object = MibTableColumn
mwVlanDHCPServerIpAddress = _MwVlanDHCPServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 8),
    _MwVlanDHCPServerIpAddress_Type()
)
mwVlanDHCPServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanDHCPServerIpAddress.setStatus("current")
_MwVlanDhcpRelayPassThroughFlag_Type = MwlOnOffSwitch
_MwVlanDhcpRelayPassThroughFlag_Object = MibTableColumn
mwVlanDhcpRelayPassThroughFlag = _MwVlanDhcpRelayPassThroughFlag_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 9),
    _MwVlanDhcpRelayPassThroughFlag_Type()
)
mwVlanDhcpRelayPassThroughFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanDhcpRelayPassThroughFlag.setStatus("current")
_MwVlanOverrideDefaultDHCPServer_Type = MwlOnOffSwitch
_MwVlanOverrideDefaultDHCPServer_Object = MibTableColumn
mwVlanOverrideDefaultDHCPServer = _MwVlanOverrideDefaultDHCPServer_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 10),
    _MwVlanOverrideDefaultDHCPServer_Type()
)
mwVlanOverrideDefaultDHCPServer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanOverrideDefaultDHCPServer.setStatus("current")
_MwVlanOwner_Type = MwlProfileOwner
_MwVlanOwner_Object = MibTableColumn
mwVlanOwner = _MwVlanOwner_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 11),
    _MwVlanOwner_Type()
)
mwVlanOwner.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mwVlanOwner.setStatus("current")
_MwVlanRowStatus_Type = RowStatus
_MwVlanRowStatus_Object = MibTableColumn
mwVlanRowStatus = _MwVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 15983, 1, 1, 4, 5, 1, 1, 14),
    _MwVlanRowStatus_Type()
)
mwVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mwVlanRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MERU-CONFIG-VLAN-MIB",
    **{"mwConfigVlan": mwConfigVlan,
       "mwVlanTable": mwVlanTable,
       "mwVlanEntry": mwVlanEntry,
       "mwVlanTableIndex": mwVlanTableIndex,
       "mwVlanTag": mwVlanTag,
       "mwVlanName": mwVlanName,
       "mwVlanNetMask": mwVlanNetMask,
       "mwVlanIpAddress": mwVlanIpAddress,
       "mwVlanInterfaceIndex": mwVlanInterfaceIndex,
       "mwVlanDefaultGateway": mwVlanDefaultGateway,
       "mwVlanDHCPServerIpAddress": mwVlanDHCPServerIpAddress,
       "mwVlanDhcpRelayPassThroughFlag": mwVlanDhcpRelayPassThroughFlag,
       "mwVlanOverrideDefaultDHCPServer": mwVlanOverrideDefaultDHCPServer,
       "mwVlanOwner": mwVlanOwner,
       "mwVlanRowStatus": mwVlanRowStatus}
)
