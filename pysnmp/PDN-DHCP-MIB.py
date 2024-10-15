# SNMP MIB module (PDN-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-DHCP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:27 2024
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

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(SwitchState,) = mibBuilder.importSymbols(
    "PDN-TC",
    "SwitchState")

(dot1qVlanStaticEntry,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qVlanStaticEntry")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

pdnDhcpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57)
)
pdnDhcpMIB.setRevisions(
        ("2004-09-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnDhcpNotifications_ObjectIdentity = ObjectIdentity
pdnDhcpNotifications = _PdnDhcpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 0)
)
_PdnDhcpObjects_ObjectIdentity = ObjectIdentity
pdnDhcpObjects = _PdnDhcpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 1)
)
_PdnDhcpVlanConfigTable_Object = MibTable
pdnDhcpVlanConfigTable = _PdnDhcpVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 1, 1)
)
if mibBuilder.loadTexts:
    pdnDhcpVlanConfigTable.setStatus("current")
_PdnDhcpVlanConfigEntry_Object = MibTableRow
pdnDhcpVlanConfigEntry = _PdnDhcpVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnDhcpVlanConfigEntry.setStatus("current")


class _PdnDhcpVlanConfigOption82_Type(SwitchState):
    """Custom type pdnDhcpVlanConfigOption82 based on SwitchState"""


_PdnDhcpVlanConfigOption82_Object = MibTableColumn
pdnDhcpVlanConfigOption82 = _PdnDhcpVlanConfigOption82_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 1, 1, 1, 1),
    _PdnDhcpVlanConfigOption82_Type()
)
pdnDhcpVlanConfigOption82.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDhcpVlanConfigOption82.setStatus("current")
_PdnDhcpAFNs_ObjectIdentity = ObjectIdentity
pdnDhcpAFNs = _PdnDhcpAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 2)
)
_PdnDhcpConformance_ObjectIdentity = ObjectIdentity
pdnDhcpConformance = _PdnDhcpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3)
)
_PdnDhcpCompliances_ObjectIdentity = ObjectIdentity
pdnDhcpCompliances = _PdnDhcpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 1)
)
_PdnDhcpGroups_ObjectIdentity = ObjectIdentity
pdnDhcpGroups = _PdnDhcpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 2)
)
_PdnDhcpObjGroups_ObjectIdentity = ObjectIdentity
pdnDhcpObjGroups = _PdnDhcpObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 2, 1)
)
_PdnDhcpAfnGroups_ObjectIdentity = ObjectIdentity
pdnDhcpAfnGroups = _PdnDhcpAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 2, 2)
)
_PdnDhcpNtfyGroups_ObjectIdentity = ObjectIdentity
pdnDhcpNtfyGroups = _PdnDhcpNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 2, 3)
)
dot1qVlanStaticEntry.registerAugmentions(
    ("PDN-DHCP-MIB",
     "pdnDhcpVlanConfigEntry")
)
pdnDhcpVlanConfigEntry.setIndexNames(*dot1qVlanStaticEntry.getIndexNames())

# Managed Objects groups

pdnDhcpVlanConfigOpt82Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 2, 1, 2)
)
pdnDhcpVlanConfigOpt82Group.setObjects(
    ("PDN-DHCP-MIB", "pdnDhcpVlanConfigOption82")
)
if mibBuilder.loadTexts:
    pdnDhcpVlanConfigOpt82Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnDhcpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 57, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnDhcpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-DHCP-MIB",
    **{"pdnDhcpMIB": pdnDhcpMIB,
       "pdnDhcpNotifications": pdnDhcpNotifications,
       "pdnDhcpObjects": pdnDhcpObjects,
       "pdnDhcpVlanConfigTable": pdnDhcpVlanConfigTable,
       "pdnDhcpVlanConfigEntry": pdnDhcpVlanConfigEntry,
       "pdnDhcpVlanConfigOption82": pdnDhcpVlanConfigOption82,
       "pdnDhcpAFNs": pdnDhcpAFNs,
       "pdnDhcpConformance": pdnDhcpConformance,
       "pdnDhcpCompliances": pdnDhcpCompliances,
       "pdnDhcpCompliance": pdnDhcpCompliance,
       "pdnDhcpGroups": pdnDhcpGroups,
       "pdnDhcpObjGroups": pdnDhcpObjGroups,
       "pdnDhcpVlanConfigOpt82Group": pdnDhcpVlanConfigOpt82Group,
       "pdnDhcpAfnGroups": pdnDhcpAfnGroups,
       "pdnDhcpNtfyGroups": pdnDhcpNtfyGroups}
)
