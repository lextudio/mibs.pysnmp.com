# SNMP MIB module (ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:55 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(dot3adAggPortEntry,) = mibBuilder.importSymbols(
    "IEEE8023-LAG-MIB",
    "dot3adAggPortEntry")

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

etsysIeee8023LagMibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35)
)
etsysIeee8023LagMibExtMIB.setRevisions(
        ("2004-09-03 15:14",
         "2003-01-31 23:16")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysIeee8023LagMibExt_ObjectIdentity = ObjectIdentity
etsysIeee8023LagMibExt = _EtsysIeee8023LagMibExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1)
)
_EtsysDot3adAggGlobal_ObjectIdentity = ObjectIdentity
etsysDot3adAggGlobal = _EtsysDot3adAggGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 1)
)


class _EtsysDot3adAggGlobalEnable_Type(EnabledStatus):
    """Custom type etsysDot3adAggGlobalEnable based on EnabledStatus"""


_EtsysDot3adAggGlobalEnable_Object = MibScalar
etsysDot3adAggGlobalEnable = _EtsysDot3adAggGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 1, 1),
    _EtsysDot3adAggGlobalEnable_Type()
)
etsysDot3adAggGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot3adAggGlobalEnable.setStatus("current")


class _EtsysDot3adAggGlobalFormSinglePortLags_Type(EnabledStatus):
    """Custom type etsysDot3adAggGlobalFormSinglePortLags based on EnabledStatus"""


_EtsysDot3adAggGlobalFormSinglePortLags_Object = MibScalar
etsysDot3adAggGlobalFormSinglePortLags = _EtsysDot3adAggGlobalFormSinglePortLags_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 1, 2),
    _EtsysDot3adAggGlobalFormSinglePortLags_Type()
)
etsysDot3adAggGlobalFormSinglePortLags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot3adAggGlobalFormSinglePortLags.setStatus("current")
_EtsysDot3adAggPort_ObjectIdentity = ObjectIdentity
etsysDot3adAggPort = _EtsysDot3adAggPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2)
)
_EtsysDot3adAggPortTable_Object = MibTable
etsysDot3adAggPortTable = _EtsysDot3adAggPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysDot3adAggPortTable.setStatus("current")
_EtsysDot3adAggPortEntry_Object = MibTableRow
etsysDot3adAggPortEntry = _EtsysDot3adAggPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysDot3adAggPortEntry.setStatus("current")


class _EtsysDot3adAggPortEnable_Type(EnabledStatus):
    """Custom type etsysDot3adAggPortEnable based on EnabledStatus"""


_EtsysDot3adAggPortEnable_Object = MibTableColumn
etsysDot3adAggPortEnable = _EtsysDot3adAggPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 1, 2, 1, 1, 1),
    _EtsysDot3adAggPortEnable_Type()
)
etsysDot3adAggPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysDot3adAggPortEnable.setStatus("current")
_EtsysIeee8023LagConformance_ObjectIdentity = ObjectIdentity
etsysIeee8023LagConformance = _EtsysIeee8023LagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2)
)
_EtsysIeee8023LagGroups_ObjectIdentity = ObjectIdentity
etsysIeee8023LagGroups = _EtsysIeee8023LagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1)
)
_EtsysIeee8023LagCompliances_ObjectIdentity = ObjectIdentity
etsysIeee8023LagCompliances = _EtsysIeee8023LagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 2)
)
dot3adAggPortEntry.registerAugmentions(
    ("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB",
     "etsysDot3adAggPortEntry")
)
etsysDot3adAggPortEntry.setIndexNames(*dot3adAggPortEntry.getIndexNames())

# Managed Objects groups

etsysDot3adAggGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1, 1)
)
etsysDot3adAggGlobalGroup.setObjects(
    ("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggGlobalEnable")
)
if mibBuilder.loadTexts:
    etsysDot3adAggGlobalGroup.setStatus("current")

etsysDot3adAggPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1, 2)
)
etsysDot3adAggPortGroup.setObjects(
    ("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggPortEnable")
)
if mibBuilder.loadTexts:
    etsysDot3adAggPortGroup.setStatus("current")

etsysDot3adAggGlobalSinglePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 1, 3)
)
etsysDot3adAggGlobalSinglePortGroup.setObjects(
    ("ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB", "etsysDot3adAggGlobalFormSinglePortLags")
)
if mibBuilder.loadTexts:
    etsysDot3adAggGlobalSinglePortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysIeee8023LagCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 35, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysIeee8023LagCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-IEEE8023-LAG-MIB-EXT-MIB",
    **{"etsysIeee8023LagMibExtMIB": etsysIeee8023LagMibExtMIB,
       "etsysIeee8023LagMibExt": etsysIeee8023LagMibExt,
       "etsysDot3adAggGlobal": etsysDot3adAggGlobal,
       "etsysDot3adAggGlobalEnable": etsysDot3adAggGlobalEnable,
       "etsysDot3adAggGlobalFormSinglePortLags": etsysDot3adAggGlobalFormSinglePortLags,
       "etsysDot3adAggPort": etsysDot3adAggPort,
       "etsysDot3adAggPortTable": etsysDot3adAggPortTable,
       "etsysDot3adAggPortEntry": etsysDot3adAggPortEntry,
       "etsysDot3adAggPortEnable": etsysDot3adAggPortEnable,
       "etsysIeee8023LagConformance": etsysIeee8023LagConformance,
       "etsysIeee8023LagGroups": etsysIeee8023LagGroups,
       "etsysDot3adAggGlobalGroup": etsysDot3adAggGlobalGroup,
       "etsysDot3adAggPortGroup": etsysDot3adAggPortGroup,
       "etsysDot3adAggGlobalSinglePortGroup": etsysDot3adAggGlobalSinglePortGroup,
       "etsysIeee8023LagCompliances": etsysIeee8023LagCompliances,
       "etsysIeee8023LagCompliance": etsysIeee8023LagCompliance}
)
