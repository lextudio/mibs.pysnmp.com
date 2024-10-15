# SNMP MIB module (ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:58 2024
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

etsysIetfpBridgeMibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33)
)
etsysIetfpBridgeMibExtMIB.setRevisions(
        ("2002-12-20 22:16",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysIetfpBridgeMibExt_ObjectIdentity = ObjectIdentity
etsysIetfpBridgeMibExt = _EtsysIetfpBridgeMibExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1)
)
_EtsysDot1dPriority_ObjectIdentity = ObjectIdentity
etsysDot1dPriority = _EtsysDot1dPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1)
)
_EtsysDot1dPortPriorityTable_Object = MibTable
etsysDot1dPortPriorityTable = _EtsysDot1dPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysDot1dPortPriorityTable.setStatus("current")
_EtsysDot1dPortPriorityEntry_Object = MibTableRow
etsysDot1dPortPriorityEntry = _EtsysDot1dPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysDot1dPortPriorityEntry.setStatus("current")


class _EtsysDot1dPortPriorityRewrite_Type(EnabledStatus):
    """Custom type etsysDot1dPortPriorityRewrite based on EnabledStatus"""


_EtsysDot1dPortPriorityRewrite_Object = MibTableColumn
etsysDot1dPortPriorityRewrite = _EtsysDot1dPortPriorityRewrite_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 1, 1, 1, 1, 1),
    _EtsysDot1dPortPriorityRewrite_Type()
)
etsysDot1dPortPriorityRewrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot1dPortPriorityRewrite.setStatus("current")
_EtsysIetfpBridgeConformance_ObjectIdentity = ObjectIdentity
etsysIetfpBridgeConformance = _EtsysIetfpBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2)
)
_EtsysIetfpBridgeGroups_ObjectIdentity = ObjectIdentity
etsysIetfpBridgeGroups = _EtsysIetfpBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 1)
)
_EtsysIetfpBridgeCompliances_ObjectIdentity = ObjectIdentity
etsysIetfpBridgeCompliances = _EtsysIetfpBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 2)
)
dot1dBasePortEntry.registerAugmentions(
    ("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB",
     "etsysDot1dPortPriorityEntry")
)
etsysDot1dPortPriorityEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())

# Managed Objects groups

etsysDot1dPriorityRewriteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 1, 1)
)
etsysDot1dPriorityRewriteGroup.setObjects(
    ("ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB", "etsysDot1dPortPriorityRewrite")
)
if mibBuilder.loadTexts:
    etsysDot1dPriorityRewriteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysIetfpBridgeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 33, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysIetfpBridgeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-IETF-P-BRIDGE-MIB-EXT-MIB",
    **{"etsysIetfpBridgeMibExtMIB": etsysIetfpBridgeMibExtMIB,
       "etsysIetfpBridgeMibExt": etsysIetfpBridgeMibExt,
       "etsysDot1dPriority": etsysDot1dPriority,
       "etsysDot1dPortPriorityTable": etsysDot1dPortPriorityTable,
       "etsysDot1dPortPriorityEntry": etsysDot1dPortPriorityEntry,
       "etsysDot1dPortPriorityRewrite": etsysDot1dPortPriorityRewrite,
       "etsysIetfpBridgeConformance": etsysIetfpBridgeConformance,
       "etsysIetfpBridgeGroups": etsysIetfpBridgeGroups,
       "etsysDot1dPriorityRewriteGroup": etsysDot1dPriorityRewriteGroup,
       "etsysIetfpBridgeCompliances": etsysIetfpBridgeCompliances,
       "etsysIetfpBridgeCompliance": etsysIetfpBridgeCompliance}
)
