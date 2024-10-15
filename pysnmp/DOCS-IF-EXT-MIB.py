# SNMP MIB module (DOCS-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/DOCS-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:32:32 2024
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

(docsIfCmtsCmStatusEntry,
 docsIfMib) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsCmStatusEntry",
    "docsIfMib")

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

docsIfExtMib = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 21)
)
docsIfExtMib.setRevisions(
        ("1900-10-08 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class DocsisVersion(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("docsis10", 1),
          ("docsis11", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DocsIfDocsisCapability_Type = DocsisVersion
_DocsIfDocsisCapability_Object = MibScalar
docsIfDocsisCapability = _DocsIfDocsisCapability_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 1),
    _DocsIfDocsisCapability_Type()
)
docsIfDocsisCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfDocsisCapability.setStatus("current")
_DocsIfDocsisOperMode_Type = DocsisVersion
_DocsIfDocsisOperMode_Object = MibScalar
docsIfDocsisOperMode = _DocsIfDocsisOperMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 2),
    _DocsIfDocsisOperMode_Type()
)
docsIfDocsisOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfDocsisOperMode.setStatus("current")
_DocsIfCmtsCmStatusExtTable_Object = MibTable
docsIfCmtsCmStatusExtTable = _DocsIfCmtsCmStatusExtTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 3)
)
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusExtTable.setStatus("current")
_DocsIfCmtsCmStatusExtEntry_Object = MibTableRow
docsIfCmtsCmStatusExtEntry = _DocsIfCmtsCmStatusExtEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 3, 1)
)
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusExtEntry.setStatus("current")
_DocsIfCmtsCmStatusDocsisMode_Type = DocsisVersion
_DocsIfCmtsCmStatusDocsisMode_Object = MibTableColumn
docsIfCmtsCmStatusDocsisMode = _DocsIfCmtsCmStatusDocsisMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 3, 1, 1),
    _DocsIfCmtsCmStatusDocsisMode_Type()
)
docsIfCmtsCmStatusDocsisMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsIfCmtsCmStatusDocsisMode.setStatus("current")
_DocsIfExtConformance_ObjectIdentity = ObjectIdentity
docsIfExtConformance = _DocsIfExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 4)
)
_DocsIfExtCompliances_ObjectIdentity = ObjectIdentity
docsIfExtCompliances = _DocsIfExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1)
)
_DocsIfExtGroups_ObjectIdentity = ObjectIdentity
docsIfExtGroups = _DocsIfExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2)
)
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("DOCS-IF-EXT-MIB",
     "docsIfCmtsCmStatusExtEntry")
)
docsIfCmtsCmStatusExtEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())

# Managed Objects groups

docsIfDocsisVersionGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2, 1)
)
docsIfDocsisVersionGroup.setObjects(
      *(("DOCS-IF-EXT-MIB", "docsIfDocsisCapability"),
        ("DOCS-IF-EXT-MIB", "docsIfDocsisOperMode"))
)
if mibBuilder.loadTexts:
    docsIfDocsisVersionGroup.setStatus("current")

docsIfExtGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 2, 2)
)
docsIfExtGroup.setObjects(
    ("DOCS-IF-EXT-MIB", "docsIfCmtsCmStatusDocsisMode")
)
if mibBuilder.loadTexts:
    docsIfExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsIfExtCmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1, 1)
)
if mibBuilder.loadTexts:
    docsIfExtCmCompliance.setStatus(
        "current"
    )

docsIfExtCmtsCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 127, 21, 4, 1, 2)
)
if mibBuilder.loadTexts:
    docsIfExtCmtsCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-IF-EXT-MIB",
    **{"DocsisVersion": DocsisVersion,
       "docsIfExtMib": docsIfExtMib,
       "docsIfDocsisCapability": docsIfDocsisCapability,
       "docsIfDocsisOperMode": docsIfDocsisOperMode,
       "docsIfCmtsCmStatusExtTable": docsIfCmtsCmStatusExtTable,
       "docsIfCmtsCmStatusExtEntry": docsIfCmtsCmStatusExtEntry,
       "docsIfCmtsCmStatusDocsisMode": docsIfCmtsCmStatusDocsisMode,
       "docsIfExtConformance": docsIfExtConformance,
       "docsIfExtCompliances": docsIfExtCompliances,
       "docsIfExtCmCompliance": docsIfExtCmCompliance,
       "docsIfExtCmtsCompliance": docsIfExtCmtsCompliance,
       "docsIfExtGroups": docsIfExtGroups,
       "docsIfDocsisVersionGroup": docsIfDocsisVersionGroup,
       "docsIfExtGroup": docsIfExtGroup}
)
