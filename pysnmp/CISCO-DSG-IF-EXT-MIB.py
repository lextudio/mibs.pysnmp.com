# SNMP MIB module (CISCO-DSG-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-DSG-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:08 2024
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

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(dsgIfClassifierEntry,
 dsgIfDownstreamEntry) = mibBuilder.importSymbols(
    "DSG-IF-MIB",
    "dsgIfClassifierEntry",
    "dsgIfDownstreamEntry")

(InetAddressDNS,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressDNS")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoDsgIfExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 777)
)
ciscoDsgIfExtMIB.setRevisions(
        ("2011-08-15 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoDsgIfExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoDsgIfExtMIBNotifs = _CiscoDsgIfExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 0)
)
_CiscoDsgIfExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoDsgIfExtMIBObjects = _CiscoDsgIfExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 1)
)
_CdsgIfExtClassifierTable_Object = MibTable
cdsgIfExtClassifierTable = _CdsgIfExtClassifierTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 1)
)
if mibBuilder.loadTexts:
    cdsgIfExtClassifierTable.setStatus("current")
_CdsgIfExtClassifierEntry_Object = MibTableRow
cdsgIfExtClassifierEntry = _CdsgIfExtClassifierEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cdsgIfExtClassifierEntry.setStatus("current")
_CdsgIfExtClassSrcHostName_Type = InetAddressDNS
_CdsgIfExtClassSrcHostName_Object = MibTableColumn
cdsgIfExtClassSrcHostName = _CdsgIfExtClassSrcHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 1, 1, 1),
    _CdsgIfExtClassSrcHostName_Type()
)
cdsgIfExtClassSrcHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsgIfExtClassSrcHostName.setStatus("current")
_CdsgIfExtClassDestHostName_Type = InetAddressDNS
_CdsgIfExtClassDestHostName_Object = MibTableColumn
cdsgIfExtClassDestHostName = _CdsgIfExtClassDestHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 1, 1, 2),
    _CdsgIfExtClassDestHostName_Type()
)
cdsgIfExtClassDestHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsgIfExtClassDestHostName.setStatus("current")
_CdsgIfExtDownstreamTable_Object = MibTable
cdsgIfExtDownstreamTable = _CdsgIfExtDownstreamTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 2)
)
if mibBuilder.loadTexts:
    cdsgIfExtDownstreamTable.setStatus("current")
_CdsgIfExtDownstreamEntry_Object = MibTableRow
cdsgIfExtDownstreamEntry = _CdsgIfExtDownstreamEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cdsgIfExtDownstreamEntry.setStatus("current")


class _CdsgIfExtDownDsgDisable_Type(TruthValue):
    """Custom type cdsgIfExtDownDsgDisable based on TruthValue"""


_CdsgIfExtDownDsgDisable_Object = MibTableColumn
cdsgIfExtDownDsgDisable = _CdsgIfExtDownDsgDisable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 1, 2, 1, 1),
    _CdsgIfExtDownDsgDisable_Type()
)
cdsgIfExtDownDsgDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cdsgIfExtDownDsgDisable.setStatus("current")
_CiscoDsgIfExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoDsgIfExtMIBConform = _CiscoDsgIfExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 2)
)
_CiscoDsgIfExtMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoDsgIfExtMIBCompliances = _CiscoDsgIfExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 2, 1)
)
_CiscoDsgIfExtMIBGroups_ObjectIdentity = ObjectIdentity
ciscoDsgIfExtMIBGroups = _CiscoDsgIfExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 2, 2)
)
dsgIfClassifierEntry.registerAugmentions(
    ("CISCO-DSG-IF-EXT-MIB",
     "cdsgIfExtClassifierEntry")
)
cdsgIfExtClassifierEntry.setIndexNames(*dsgIfClassifierEntry.getIndexNames())
dsgIfDownstreamEntry.registerAugmentions(
    ("CISCO-DSG-IF-EXT-MIB",
     "cdsgIfExtDownstreamEntry")
)
cdsgIfExtDownstreamEntry.setIndexNames(*dsgIfDownstreamEntry.getIndexNames())

# Managed Objects groups

cdsgIfExtHostGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 2, 2, 1)
)
cdsgIfExtHostGroup.setObjects(
      *(("CISCO-DSG-IF-EXT-MIB", "cdsgIfExtClassSrcHostName"),
        ("CISCO-DSG-IF-EXT-MIB", "cdsgIfExtClassDestHostName"))
)
if mibBuilder.loadTexts:
    cdsgIfExtHostGroup.setStatus("current")

cdsgIfExtDownControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 2, 2, 2)
)
cdsgIfExtDownControlGroup.setObjects(
    ("CISCO-DSG-IF-EXT-MIB", "cdsgIfExtDownDsgDisable")
)
if mibBuilder.loadTexts:
    cdsgIfExtDownControlGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoDsgIfExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 777, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoDsgIfExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-DSG-IF-EXT-MIB",
    **{"ciscoDsgIfExtMIB": ciscoDsgIfExtMIB,
       "ciscoDsgIfExtMIBNotifs": ciscoDsgIfExtMIBNotifs,
       "ciscoDsgIfExtMIBObjects": ciscoDsgIfExtMIBObjects,
       "cdsgIfExtClassifierTable": cdsgIfExtClassifierTable,
       "cdsgIfExtClassifierEntry": cdsgIfExtClassifierEntry,
       "cdsgIfExtClassSrcHostName": cdsgIfExtClassSrcHostName,
       "cdsgIfExtClassDestHostName": cdsgIfExtClassDestHostName,
       "cdsgIfExtDownstreamTable": cdsgIfExtDownstreamTable,
       "cdsgIfExtDownstreamEntry": cdsgIfExtDownstreamEntry,
       "cdsgIfExtDownDsgDisable": cdsgIfExtDownDsgDisable,
       "ciscoDsgIfExtMIBConform": ciscoDsgIfExtMIBConform,
       "ciscoDsgIfExtMIBCompliances": ciscoDsgIfExtMIBCompliances,
       "ciscoDsgIfExtMIBCompliance": ciscoDsgIfExtMIBCompliance,
       "ciscoDsgIfExtMIBGroups": ciscoDsgIfExtMIBGroups,
       "cdsgIfExtHostGroup": cdsgIfExtHostGroup,
       "cdsgIfExtDownControlGroup": cdsgIfExtDownControlGroup}
)
