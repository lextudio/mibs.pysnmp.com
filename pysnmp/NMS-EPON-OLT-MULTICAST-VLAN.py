# SNMP MIB module (NMS-EPON-OLT-MULTICAST-VLAN) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/NMS-EPON-OLT-MULTICAST-VLAN
# Produced by pysmi-1.5.4 at Mon Oct 14 22:27:44 2024
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

(nmsEPONGroup,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsEPONGroup")

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


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsEponOltMulticastVlan_ObjectIdentity = ObjectIdentity
nmsEponOltMulticastVlan = _NmsEponOltMulticastVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 5)
)
_NmseponoltmulticastvlanTable_Object = MibTable
nmseponoltmulticastvlanTable = _NmseponoltmulticastvlanTable_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 5, 1)
)
if mibBuilder.loadTexts:
    nmseponoltmulticastvlanTable.setStatus("mandatory")
_NmsEponOltMulticastVlanEntry_Object = MibTableRow
nmsEponOltMulticastVlanEntry = _NmsEponOltMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 5, 1, 1)
)
nmsEponOltMulticastVlanEntry.setIndexNames(
    (0, "NMS-EPON-OLT-MULTICAST-VLAN", "oltMcVlanId"),
    (0, "NMS-EPON-OLT-MULTICAST-VLAN", "oltMcIpAddress"),
)
if mibBuilder.loadTexts:
    nmsEponOltMulticastVlanEntry.setStatus("mandatory")


class _OltMcVlanId_Type(Integer32):
    """Custom type oltMcVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_OltMcVlanId_Type.__name__ = "Integer32"
_OltMcVlanId_Object = MibTableColumn
oltMcVlanId = _OltMcVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 5, 1, 1, 1),
    _OltMcVlanId_Type()
)
oltMcVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltMcVlanId.setStatus("mandatory")
_OltMcVlanIpAddress_Type = IpAddress
_OltMcVlanIpAddress_Object = MibTableColumn
oltMcVlanIpAddress = _OltMcVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 5, 1, 1, 2),
    _OltMcVlanIpAddress_Type()
)
oltMcVlanIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oltMcVlanIpAddress.setStatus("mandatory")
_OltMcVlanRowStatus_Type = RowStatus
_OltMcVlanRowStatus_Object = MibTableColumn
oltMcVlanRowStatus = _OltMcVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11606, 10, 101, 5, 1, 1, 3),
    _OltMcVlanRowStatus_Type()
)
oltMcVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oltMcVlanRowStatus.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-EPON-OLT-MULTICAST-VLAN",
    **{"nmsEponOltMulticastVlan": nmsEponOltMulticastVlan,
       "nmseponoltmulticastvlanTable": nmseponoltmulticastvlanTable,
       "nmsEponOltMulticastVlanEntry": nmsEponOltMulticastVlanEntry,
       "oltMcVlanId": oltMcVlanId,
       "oltMcVlanIpAddress": oltMcVlanIpAddress,
       "oltMcVlanRowStatus": oltMcVlanRowStatus}
)
