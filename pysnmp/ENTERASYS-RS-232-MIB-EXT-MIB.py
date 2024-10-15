# SNMP MIB module (ENTERASYS-RS-232-MIB-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-RS-232-MIB-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:30 2024
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(rs232PortEntry,) = mibBuilder.importSymbols(
    "RS-232-MIB",
    "rs232PortEntry")

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

etsysRs232MibExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77)
)
etsysRs232MibExtMIB.setRevisions(
        ("2011-06-22 14:50",
         "2010-11-09 20:07")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysRs232MibExtObjects_ObjectIdentity = ObjectIdentity
etsysRs232MibExtObjects = _EtsysRs232MibExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1)
)
_EtsysRs232MibExtVt100_ObjectIdentity = ObjectIdentity
etsysRs232MibExtVt100 = _EtsysRs232MibExtVt100_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 1)
)
_EtsysRs232Vt100ExtTable_Object = MibTable
etsysRs232Vt100ExtTable = _EtsysRs232Vt100ExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysRs232Vt100ExtTable.setStatus("current")
_EtsysRs232Vt100ExtEntry_Object = MibTableRow
etsysRs232Vt100ExtEntry = _EtsysRs232Vt100ExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    etsysRs232Vt100ExtEntry.setStatus("current")


class _EtsysRs232Vt100DsrEnableState_Type(EnabledStatus):
    """Custom type etsysRs232Vt100DsrEnableState based on EnabledStatus"""


_EtsysRs232Vt100DsrEnableState_Object = MibTableColumn
etsysRs232Vt100DsrEnableState = _EtsysRs232Vt100DsrEnableState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 1, 1, 1, 1),
    _EtsysRs232Vt100DsrEnableState_Type()
)
etsysRs232Vt100DsrEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRs232Vt100DsrEnableState.setStatus("current")


class _EtsysRs232Vt100DsrTimeout_Type(Integer32):
    """Custom type etsysRs232Vt100DsrTimeout based on Integer32"""
    defaultValue = 3


_EtsysRs232Vt100DsrTimeout_Object = MibTableColumn
etsysRs232Vt100DsrTimeout = _EtsysRs232Vt100DsrTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 1, 1, 1, 2),
    _EtsysRs232Vt100DsrTimeout_Type()
)
etsysRs232Vt100DsrTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRs232Vt100DsrTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysRs232Vt100DsrTimeout.setUnits("seconds")
_EtsysRs232MibExtCtsLink_ObjectIdentity = ObjectIdentity
etsysRs232MibExtCtsLink = _EtsysRs232MibExtCtsLink_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 2)
)
_EtsysRs232CtsLinkExtTable_Object = MibTable
etsysRs232CtsLinkExtTable = _EtsysRs232CtsLinkExtTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysRs232CtsLinkExtTable.setStatus("current")
_EtsysRs232CtsLinkExtEntry_Object = MibTableRow
etsysRs232CtsLinkExtEntry = _EtsysRs232CtsLinkExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysRs232CtsLinkExtEntry.setStatus("current")


class _EtsysRs232CtsLinkEnableState_Type(EnabledStatus):
    """Custom type etsysRs232CtsLinkEnableState based on EnabledStatus"""


_EtsysRs232CtsLinkEnableState_Object = MibTableColumn
etsysRs232CtsLinkEnableState = _EtsysRs232CtsLinkEnableState_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 1, 2, 1, 1, 1),
    _EtsysRs232CtsLinkEnableState_Type()
)
etsysRs232CtsLinkEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRs232CtsLinkEnableState.setStatus("current")
_EtsysRs232MibExtConformance_ObjectIdentity = ObjectIdentity
etsysRs232MibExtConformance = _EtsysRs232MibExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2)
)
_EtsysRs232MibExtGroups_ObjectIdentity = ObjectIdentity
etsysRs232MibExtGroups = _EtsysRs232MibExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 1)
)
_EtsysRs232MibExtCompliances_ObjectIdentity = ObjectIdentity
etsysRs232MibExtCompliances = _EtsysRs232MibExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 2)
)
rs232PortEntry.registerAugmentions(
    ("ENTERASYS-RS-232-MIB-EXT-MIB",
     "etsysRs232Vt100ExtEntry")
)
etsysRs232Vt100ExtEntry.setIndexNames(*rs232PortEntry.getIndexNames())
rs232PortEntry.registerAugmentions(
    ("ENTERASYS-RS-232-MIB-EXT-MIB",
     "etsysRs232CtsLinkExtEntry")
)
etsysRs232CtsLinkExtEntry.setIndexNames(*rs232PortEntry.getIndexNames())

# Managed Objects groups

etsysRs232MibExtVt100DsrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 1, 1)
)
etsysRs232MibExtVt100DsrGroup.setObjects(
      *(("ENTERASYS-RS-232-MIB-EXT-MIB", "etsysRs232Vt100DsrEnableState"),
        ("ENTERASYS-RS-232-MIB-EXT-MIB", "etsysRs232Vt100DsrTimeout"))
)
if mibBuilder.loadTexts:
    etsysRs232MibExtVt100DsrGroup.setStatus("current")

etsysRs232MibExtCtsLinkGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 1, 2)
)
etsysRs232MibExtCtsLinkGroup.setObjects(
    ("ENTERASYS-RS-232-MIB-EXT-MIB", "etsysRs232CtsLinkEnableState")
)
if mibBuilder.loadTexts:
    etsysRs232MibExtCtsLinkGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysRs232MibExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysRs232MibExtCompliance.setStatus(
        "current"
    )

etsysRs232MibCtsExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 77, 2, 2, 2)
)
if mibBuilder.loadTexts:
    etsysRs232MibCtsExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-RS-232-MIB-EXT-MIB",
    **{"etsysRs232MibExtMIB": etsysRs232MibExtMIB,
       "etsysRs232MibExtObjects": etsysRs232MibExtObjects,
       "etsysRs232MibExtVt100": etsysRs232MibExtVt100,
       "etsysRs232Vt100ExtTable": etsysRs232Vt100ExtTable,
       "etsysRs232Vt100ExtEntry": etsysRs232Vt100ExtEntry,
       "etsysRs232Vt100DsrEnableState": etsysRs232Vt100DsrEnableState,
       "etsysRs232Vt100DsrTimeout": etsysRs232Vt100DsrTimeout,
       "etsysRs232MibExtCtsLink": etsysRs232MibExtCtsLink,
       "etsysRs232CtsLinkExtTable": etsysRs232CtsLinkExtTable,
       "etsysRs232CtsLinkExtEntry": etsysRs232CtsLinkExtEntry,
       "etsysRs232CtsLinkEnableState": etsysRs232CtsLinkEnableState,
       "etsysRs232MibExtConformance": etsysRs232MibExtConformance,
       "etsysRs232MibExtGroups": etsysRs232MibExtGroups,
       "etsysRs232MibExtVt100DsrGroup": etsysRs232MibExtVt100DsrGroup,
       "etsysRs232MibExtCtsLinkGroup": etsysRs232MibExtCtsLinkGroup,
       "etsysRs232MibExtCompliances": etsysRs232MibExtCompliances,
       "etsysRs232MibExtCompliance": etsysRs232MibExtCompliance,
       "etsysRs232MibCtsExtCompliance": etsysRs232MibCtsExtCompliance}
)
