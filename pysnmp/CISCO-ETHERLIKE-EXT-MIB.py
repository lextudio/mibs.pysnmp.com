# SNMP MIB module (CISCO-ETHERLIKE-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ETHERLIKE-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:59 2024
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

(dot3StatsIndex,) = mibBuilder.importSymbols(
    "EtherLike-MIB",
    "dot3StatsIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

ciscoEtherExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 645)
)
ciscoEtherExtMIB.setRevisions(
        ("2010-06-04 00:00",
         "2008-10-15 00:00",
         "2008-01-09 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoEtherExtMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoEtherExtMIBNotifs = _CiscoEtherExtMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 0)
)
_CiscoEtherExtMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEtherExtMIBObjects = _CiscoEtherExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 1)
)
_CeeDot3PauseExt_ObjectIdentity = ObjectIdentity
ceeDot3PauseExt = _CeeDot3PauseExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1)
)
_CeeDot3PauseExtTable_Object = MibTable
ceeDot3PauseExtTable = _CeeDot3PauseExtTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ceeDot3PauseExtTable.setStatus("current")
_CeeDot3PauseExtEntry_Object = MibTableRow
ceeDot3PauseExtEntry = _CeeDot3PauseExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1)
)
ceeDot3PauseExtEntry.setIndexNames(
    (0, "EtherLike-MIB", "dot3StatsIndex"),
)
if mibBuilder.loadTexts:
    ceeDot3PauseExtEntry.setStatus("current")


class _CeeDot3PauseExtAdminMode_Type(Bits):
    """Custom type ceeDot3PauseExtAdminMode based on Bits"""
    namedValues = NamedValues(
        *(("rxDesired", 1),
          ("txDesired", 0))
    )

_CeeDot3PauseExtAdminMode_Type.__name__ = "Bits"
_CeeDot3PauseExtAdminMode_Object = MibTableColumn
ceeDot3PauseExtAdminMode = _CeeDot3PauseExtAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1, 1),
    _CeeDot3PauseExtAdminMode_Type()
)
ceeDot3PauseExtAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceeDot3PauseExtAdminMode.setStatus("current")


class _CeeDot3PauseExtOperMode_Type(Bits):
    """Custom type ceeDot3PauseExtOperMode based on Bits"""
    namedValues = NamedValues(
        *(("rxDesired", 3),
          ("rxDisagree", 1),
          ("txDesired", 2),
          ("txDisagree", 0))
    )

_CeeDot3PauseExtOperMode_Type.__name__ = "Bits"
_CeeDot3PauseExtOperMode_Object = MibTableColumn
ceeDot3PauseExtOperMode = _CeeDot3PauseExtOperMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 1, 1, 1, 2),
    _CeeDot3PauseExtOperMode_Type()
)
ceeDot3PauseExtOperMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceeDot3PauseExtOperMode.setStatus("current")
_CeeSubIf_ObjectIdentity = ObjectIdentity
ceeSubIf = _CeeSubIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2)
)
_CeeSubInterfaceTable_Object = MibTable
ceeSubInterfaceTable = _CeeSubInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ceeSubInterfaceTable.setStatus("current")
_CeeSubInterfaceEntry_Object = MibTableRow
ceeSubInterfaceEntry = _CeeSubInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1, 1)
)
ceeSubInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ceeSubInterfaceEntry.setStatus("current")


class _CeeSubInterfaceCount_Type(Unsigned32):
    """Custom type ceeSubInterfaceCount based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_CeeSubInterfaceCount_Type.__name__ = "Unsigned32"
_CeeSubInterfaceCount_Object = MibTableColumn
ceeSubInterfaceCount = _CeeSubInterfaceCount_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 1, 2, 1, 1, 1),
    _CeeSubInterfaceCount_Type()
)
ceeSubInterfaceCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceeSubInterfaceCount.setStatus("current")
if mibBuilder.loadTexts:
    ceeSubInterfaceCount.setUnits("subifs")
_CiscoEtherExtMIBConform_ObjectIdentity = ObjectIdentity
ciscoEtherExtMIBConform = _CiscoEtherExtMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 2)
)
_CeeEtherExtMIBCompliances_ObjectIdentity = ObjectIdentity
ceeEtherExtMIBCompliances = _CeeEtherExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1)
)
_CeeEtherExtMIBGroups_ObjectIdentity = ObjectIdentity
ceeEtherExtMIBGroups = _CeeEtherExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2)
)

# Managed Objects groups

ciscoEtherExtPauseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2, 1)
)
ciscoEtherExtPauseGroup.setObjects(
      *(("CISCO-ETHERLIKE-EXT-MIB", "ceeDot3PauseExtAdminMode"),
        ("CISCO-ETHERLIKE-EXT-MIB", "ceeDot3PauseExtOperMode"))
)
if mibBuilder.loadTexts:
    ciscoEtherExtPauseGroup.setStatus("current")

ciscoEtherExtSubIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 2, 2)
)
ciscoEtherExtSubIfGroup.setObjects(
    ("CISCO-ETHERLIKE-EXT-MIB", "ceeSubInterfaceCount")
)
if mibBuilder.loadTexts:
    ciscoEtherExtSubIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ceeEtherExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ceeEtherExtMIBCompliance.setStatus(
        "deprecated"
    )

ceeEtherExtMIBComplianceR01 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 645, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ceeEtherExtMIBComplianceR01.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ETHERLIKE-EXT-MIB",
    **{"ciscoEtherExtMIB": ciscoEtherExtMIB,
       "ciscoEtherExtMIBNotifs": ciscoEtherExtMIBNotifs,
       "ciscoEtherExtMIBObjects": ciscoEtherExtMIBObjects,
       "ceeDot3PauseExt": ceeDot3PauseExt,
       "ceeDot3PauseExtTable": ceeDot3PauseExtTable,
       "ceeDot3PauseExtEntry": ceeDot3PauseExtEntry,
       "ceeDot3PauseExtAdminMode": ceeDot3PauseExtAdminMode,
       "ceeDot3PauseExtOperMode": ceeDot3PauseExtOperMode,
       "ceeSubIf": ceeSubIf,
       "ceeSubInterfaceTable": ceeSubInterfaceTable,
       "ceeSubInterfaceEntry": ceeSubInterfaceEntry,
       "ceeSubInterfaceCount": ceeSubInterfaceCount,
       "ciscoEtherExtMIBConform": ciscoEtherExtMIBConform,
       "ceeEtherExtMIBCompliances": ceeEtherExtMIBCompliances,
       "ceeEtherExtMIBCompliance": ceeEtherExtMIBCompliance,
       "ceeEtherExtMIBComplianceR01": ceeEtherExtMIBComplianceR01,
       "ceeEtherExtMIBGroups": ceeEtherExtMIBGroups,
       "ciscoEtherExtPauseGroup": ciscoEtherExtPauseGroup,
       "ciscoEtherExtSubIfGroup": ciscoEtherExtSubIfGroup}
)
