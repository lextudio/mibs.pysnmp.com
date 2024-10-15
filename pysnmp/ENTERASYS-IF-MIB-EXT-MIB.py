# SNMP MIB module (ENTERASYS-IF-MIB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-IF-MIB-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:38:59 2024
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

(ifEntry,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifEntry")

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

etsysIfMibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57)
)
etsysIfMibExtMIB.setRevisions(
        ("2011-05-12 14:15",
         "2005-01-13 21:35")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysIfOperStatusCauses(Bits, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_EtsysIfMibExtObjects_ObjectIdentity = ObjectIdentity
etsysIfMibExtObjects = _EtsysIfMibExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1)
)
_EtsysIfMibExtSystem_ObjectIdentity = ObjectIdentity
etsysIfMibExtSystem = _EtsysIfMibExtSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 1)
)


class _EtsysIfOperStateLinkChange_Type(EnabledStatus):
    """Custom type etsysIfOperStateLinkChange based on EnabledStatus"""


_EtsysIfOperStateLinkChange_Object = MibScalar
etsysIfOperStateLinkChange = _EtsysIfOperStateLinkChange_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 1, 1),
    _EtsysIfOperStateLinkChange_Type()
)
etsysIfOperStateLinkChange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysIfOperStateLinkChange.setStatus("current")
_EtsysIfMibExtInterface_ObjectIdentity = ObjectIdentity
etsysIfMibExtInterface = _EtsysIfMibExtInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2)
)
_EtsysInterfaceExtTable_Object = MibTable
etsysInterfaceExtTable = _EtsysInterfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysInterfaceExtTable.setStatus("current")
_EtsysInterfaceExtEntry_Object = MibTableRow
etsysInterfaceExtEntry = _EtsysInterfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysInterfaceExtEntry.setStatus("current")
_EtsysIfOperStatusCause_Type = EtsysIfOperStatusCauses
_EtsysIfOperStatusCause_Object = MibTableColumn
etsysIfOperStatusCause = _EtsysIfOperStatusCause_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 1, 2, 1, 1, 1),
    _EtsysIfOperStatusCause_Type()
)
etsysIfOperStatusCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysIfOperStatusCause.setStatus("current")
_EtsysIfMibExtConformance_ObjectIdentity = ObjectIdentity
etsysIfMibExtConformance = _EtsysIfMibExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2)
)
_EtsysIfMibExtGroups_ObjectIdentity = ObjectIdentity
etsysIfMibExtGroups = _EtsysIfMibExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1)
)
_EtsysIfMibExtCompliances_ObjectIdentity = ObjectIdentity
etsysIfMibExtCompliances = _EtsysIfMibExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 2)
)
ifEntry.registerAugmentions(
    ("ENTERASYS-IF-MIB-EXT-MIB",
     "etsysInterfaceExtEntry")
)
etsysInterfaceExtEntry.setIndexNames(*ifEntry.getIndexNames())

# Managed Objects groups

etsysIfMibExtOperLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1, 1)
)
etsysIfMibExtOperLinkGroup.setObjects(
    ("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfOperStateLinkChange")
)
if mibBuilder.loadTexts:
    etsysIfMibExtOperLinkGroup.setStatus("current")

etsysIfMibExtOperStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 1, 2)
)
etsysIfMibExtOperStatusGroup.setObjects(
    ("ENTERASYS-IF-MIB-EXT-MIB", "etsysIfOperStatusCause")
)
if mibBuilder.loadTexts:
    etsysIfMibExtOperStatusGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysIfMibExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 57, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysIfMibExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-IF-MIB-EXT-MIB",
    **{"EtsysIfOperStatusCauses": EtsysIfOperStatusCauses,
       "etsysIfMibExtMIB": etsysIfMibExtMIB,
       "etsysIfMibExtObjects": etsysIfMibExtObjects,
       "etsysIfMibExtSystem": etsysIfMibExtSystem,
       "etsysIfOperStateLinkChange": etsysIfOperStateLinkChange,
       "etsysIfMibExtInterface": etsysIfMibExtInterface,
       "etsysInterfaceExtTable": etsysInterfaceExtTable,
       "etsysInterfaceExtEntry": etsysInterfaceExtEntry,
       "etsysIfOperStatusCause": etsysIfOperStatusCause,
       "etsysIfMibExtConformance": etsysIfMibExtConformance,
       "etsysIfMibExtGroups": etsysIfMibExtGroups,
       "etsysIfMibExtOperLinkGroup": etsysIfMibExtOperLinkGroup,
       "etsysIfMibExtOperStatusGroup": etsysIfMibExtOperStatusGroup,
       "etsysIfMibExtCompliances": etsysIfMibExtCompliances,
       "etsysIfMibExtCompliance": etsysIfMibExtCompliance}
)
