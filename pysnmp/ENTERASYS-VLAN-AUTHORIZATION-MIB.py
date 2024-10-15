# SNMP MIB module (ENTERASYS-VLAN-AUTHORIZATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-VLAN-AUTHORIZATION-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:41 2024
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

(dot1dBasePortEntry,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePortEntry")

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

etsysVlanAuthorizationMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48)
)
etsysVlanAuthorizationMIB.setRevisions(
        ("2004-06-02 19:22",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanAuthEgressStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("dynamic", 4),
          ("none", 1),
          ("tagged", 2),
          ("untagged", 3))
    )



# MIB Managed Objects in the order of their OIDs

_EtsysVlanAuthorizationObjects_ObjectIdentity = ObjectIdentity
etsysVlanAuthorizationObjects = _EtsysVlanAuthorizationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1)
)
_EtsysVlanAuthorizationSystem_ObjectIdentity = ObjectIdentity
etsysVlanAuthorizationSystem = _EtsysVlanAuthorizationSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 1)
)


class _EtsysVlanAuthorizationEnable_Type(EnabledStatus):
    """Custom type etsysVlanAuthorizationEnable based on EnabledStatus"""


_EtsysVlanAuthorizationEnable_Object = MibScalar
etsysVlanAuthorizationEnable = _EtsysVlanAuthorizationEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 1, 1),
    _EtsysVlanAuthorizationEnable_Type()
)
etsysVlanAuthorizationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVlanAuthorizationEnable.setStatus("current")
_EtsysVlanAuthorizationPorts_ObjectIdentity = ObjectIdentity
etsysVlanAuthorizationPorts = _EtsysVlanAuthorizationPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2)
)
_EtsysVlanAuthorizationTable_Object = MibTable
etsysVlanAuthorizationTable = _EtsysVlanAuthorizationTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysVlanAuthorizationTable.setStatus("current")
_EtsysVlanAuthorizationEntry_Object = MibTableRow
etsysVlanAuthorizationEntry = _EtsysVlanAuthorizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysVlanAuthorizationEntry.setStatus("current")


class _EtsysVlanAuthorizationStatus_Type(EnabledStatus):
    """Custom type etsysVlanAuthorizationStatus based on EnabledStatus"""


_EtsysVlanAuthorizationStatus_Object = MibTableColumn
etsysVlanAuthorizationStatus = _EtsysVlanAuthorizationStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 1),
    _EtsysVlanAuthorizationStatus_Type()
)
etsysVlanAuthorizationStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVlanAuthorizationStatus.setStatus("current")


class _EtsysVlanAuthorizationAdminEgress_Type(VlanAuthEgressStatus):
    """Custom type etsysVlanAuthorizationAdminEgress based on VlanAuthEgressStatus"""


_EtsysVlanAuthorizationAdminEgress_Object = MibTableColumn
etsysVlanAuthorizationAdminEgress = _EtsysVlanAuthorizationAdminEgress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 2),
    _EtsysVlanAuthorizationAdminEgress_Type()
)
etsysVlanAuthorizationAdminEgress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysVlanAuthorizationAdminEgress.setStatus("current")


class _EtsysVlanAuthorizationOperEgress_Type(VlanAuthEgressStatus):
    """Custom type etsysVlanAuthorizationOperEgress based on VlanAuthEgressStatus"""


_EtsysVlanAuthorizationOperEgress_Object = MibTableColumn
etsysVlanAuthorizationOperEgress = _EtsysVlanAuthorizationOperEgress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 3),
    _EtsysVlanAuthorizationOperEgress_Type()
)
etsysVlanAuthorizationOperEgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVlanAuthorizationOperEgress.setStatus("current")


class _EtsysVlanAuthorizationVlanID_Type(Integer32):
    """Custom type etsysVlanAuthorizationVlanID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4095, 4095),
    )


_EtsysVlanAuthorizationVlanID_Type.__name__ = "Integer32"
_EtsysVlanAuthorizationVlanID_Object = MibTableColumn
etsysVlanAuthorizationVlanID = _EtsysVlanAuthorizationVlanID_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 1, 2, 1, 1, 4),
    _EtsysVlanAuthorizationVlanID_Type()
)
etsysVlanAuthorizationVlanID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysVlanAuthorizationVlanID.setStatus("current")
_EtsysVlanAuthorizationConformance_ObjectIdentity = ObjectIdentity
etsysVlanAuthorizationConformance = _EtsysVlanAuthorizationConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2)
)
_EtsysVlanAuthorizationGroups_ObjectIdentity = ObjectIdentity
etsysVlanAuthorizationGroups = _EtsysVlanAuthorizationGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 1)
)
_EtsysVlanAuthorizationCompliances_ObjectIdentity = ObjectIdentity
etsysVlanAuthorizationCompliances = _EtsysVlanAuthorizationCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 2)
)
dot1dBasePortEntry.registerAugmentions(
    ("ENTERASYS-VLAN-AUTHORIZATION-MIB",
     "etsysVlanAuthorizationEntry")
)
etsysVlanAuthorizationEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups

etsysVlanAuthorizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 1, 1)
)
etsysVlanAuthorizationGroup.setObjects(
      *(("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationEnable"),
        ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationStatus"),
        ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationAdminEgress"),
        ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationOperEgress"),
        ("ENTERASYS-VLAN-AUTHORIZATION-MIB", "etsysVlanAuthorizationVlanID"))
)
if mibBuilder.loadTexts:
    etsysVlanAuthorizationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysVlanAuthorizationCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 48, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysVlanAuthorizationCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-VLAN-AUTHORIZATION-MIB",
    **{"VlanAuthEgressStatus": VlanAuthEgressStatus,
       "etsysVlanAuthorizationMIB": etsysVlanAuthorizationMIB,
       "etsysVlanAuthorizationObjects": etsysVlanAuthorizationObjects,
       "etsysVlanAuthorizationSystem": etsysVlanAuthorizationSystem,
       "etsysVlanAuthorizationEnable": etsysVlanAuthorizationEnable,
       "etsysVlanAuthorizationPorts": etsysVlanAuthorizationPorts,
       "etsysVlanAuthorizationTable": etsysVlanAuthorizationTable,
       "etsysVlanAuthorizationEntry": etsysVlanAuthorizationEntry,
       "etsysVlanAuthorizationStatus": etsysVlanAuthorizationStatus,
       "etsysVlanAuthorizationAdminEgress": etsysVlanAuthorizationAdminEgress,
       "etsysVlanAuthorizationOperEgress": etsysVlanAuthorizationOperEgress,
       "etsysVlanAuthorizationVlanID": etsysVlanAuthorizationVlanID,
       "etsysVlanAuthorizationConformance": etsysVlanAuthorizationConformance,
       "etsysVlanAuthorizationGroups": etsysVlanAuthorizationGroups,
       "etsysVlanAuthorizationGroup": etsysVlanAuthorizationGroup,
       "etsysVlanAuthorizationCompliances": etsysVlanAuthorizationCompliances,
       "etsysVlanAuthorizationCompliance": etsysVlanAuthorizationCompliance}
)
