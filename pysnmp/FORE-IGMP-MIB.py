# SNMP MIB module (FORE-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FORE-IGMP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:45:30 2024
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

(preDot1qVlanMIB,) = mibBuilder.importSymbols(
    "Fore-Common-MIB",
    "preDot1qVlanMIB")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

foreIgmpModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IgmpIpmcTable_Object = MibTable
igmpIpmcTable = _IgmpIpmcTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    igmpIpmcTable.setStatus("current")
_IgmpIpmcEntry_Object = MibTableRow
igmpIpmcEntry = _IgmpIpmcEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 1, 1)
)
igmpIpmcEntry.setIndexNames(
    (0, "FORE-IGMP-MIB", "vlan"),
    (0, "FORE-IGMP-MIB", "ipMulticastAddress"),
)
if mibBuilder.loadTexts:
    igmpIpmcEntry.setStatus("current")
_IpMulticastAddress_Type = IpAddress
_IpMulticastAddress_Object = MibTableColumn
ipMulticastAddress = _IpMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 1, 1, 1),
    _IpMulticastAddress_Type()
)
ipMulticastAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipMulticastAddress.setStatus("current")


class _IpmcPortGroup_Type(DisplayString):
    """Custom type ipmcPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_IpmcPortGroup_Type.__name__ = "DisplayString"
_IpmcPortGroup_Object = MibTableColumn
ipmcPortGroup = _IpmcPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 1, 1, 2),
    _IpmcPortGroup_Type()
)
ipmcPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipmcPortGroup.setStatus("current")
_IgmpRouterTable_Object = MibTable
igmpRouterTable = _IgmpRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 2)
)
if mibBuilder.loadTexts:
    igmpRouterTable.setStatus("current")
_IgmpRouterEntry_Object = MibTableRow
igmpRouterEntry = _IgmpRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 2, 1)
)
igmpRouterEntry.setIndexNames(
    (0, "FORE-IGMP-MIB", "vlan"),
)
if mibBuilder.loadTexts:
    igmpRouterEntry.setStatus("current")


class _Vlan_Type(DisplayString):
    """Custom type vlan based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_Vlan_Type.__name__ = "DisplayString"
_Vlan_Object = MibTableColumn
vlan = _Vlan_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 2, 1, 1),
    _Vlan_Type()
)
vlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlan.setStatus("current")


class _RouterPortGroup_Type(DisplayString):
    """Custom type routerPortGroup based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 100),
    )


_RouterPortGroup_Type.__name__ = "DisplayString"
_RouterPortGroup_Object = MibTableColumn
routerPortGroup = _RouterPortGroup_Object(
    (1, 3, 6, 1, 4, 1, 326, 1, 8, 3, 2, 1, 2),
    _RouterPortGroup_Type()
)
routerPortGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    routerPortGroup.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FORE-IGMP-MIB",
    **{"foreIgmpModule": foreIgmpModule,
       "igmpIpmcTable": igmpIpmcTable,
       "igmpIpmcEntry": igmpIpmcEntry,
       "ipMulticastAddress": ipMulticastAddress,
       "ipmcPortGroup": ipmcPortGroup,
       "igmpRouterTable": igmpRouterTable,
       "igmpRouterEntry": igmpRouterEntry,
       "vlan": vlan,
       "routerPortGroup": routerPortGroup}
)
