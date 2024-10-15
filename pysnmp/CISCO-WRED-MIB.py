# SNMP MIB module (CISCO-WRED-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-WRED-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:13:45 2024
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

ciscoWredMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 83)
)
ciscoWredMIB.setRevisions(
        ("1997-07-18 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoWredMIBObjects_ObjectIdentity = ObjectIdentity
ciscoWredMIBObjects = _CiscoWredMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1)
)
_CwredConfig_ObjectIdentity = ObjectIdentity
cwredConfig = _CwredConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1)
)
_CwredConfigGlobTable_Object = MibTable
cwredConfigGlobTable = _CwredConfigGlobTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cwredConfigGlobTable.setStatus("current")
_CwredConfigGlobEntry_Object = MibTableRow
cwredConfigGlobEntry = _CwredConfigGlobEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 1, 1)
)
cwredConfigGlobEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cwredConfigGlobEntry.setStatus("current")
_CwredConfigGlobQueueWeight_Type = Integer32
_CwredConfigGlobQueueWeight_Object = MibTableColumn
cwredConfigGlobQueueWeight = _CwredConfigGlobQueueWeight_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 1, 1, 1),
    _CwredConfigGlobQueueWeight_Type()
)
cwredConfigGlobQueueWeight.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwredConfigGlobQueueWeight.setStatus("current")
_CwredConfigPrecedTable_Object = MibTable
cwredConfigPrecedTable = _CwredConfigPrecedTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cwredConfigPrecedTable.setStatus("current")
_CwredConfigPrecedEntry_Object = MibTableRow
cwredConfigPrecedEntry = _CwredConfigPrecedEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2, 1)
)
cwredConfigPrecedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "CISCO-WRED-MIB", "cwredConfigPrecedPrecedence"),
)
if mibBuilder.loadTexts:
    cwredConfigPrecedEntry.setStatus("current")


class _CwredConfigPrecedPrecedence_Type(Integer32):
    """Custom type cwredConfigPrecedPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CwredConfigPrecedPrecedence_Type.__name__ = "Integer32"
_CwredConfigPrecedPrecedence_Object = MibTableColumn
cwredConfigPrecedPrecedence = _CwredConfigPrecedPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2, 1, 1),
    _CwredConfigPrecedPrecedence_Type()
)
cwredConfigPrecedPrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwredConfigPrecedPrecedence.setStatus("current")
_CwredConfigPrecedMinDepthThreshold_Type = Integer32
_CwredConfigPrecedMinDepthThreshold_Object = MibTableColumn
cwredConfigPrecedMinDepthThreshold = _CwredConfigPrecedMinDepthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2, 1, 2),
    _CwredConfigPrecedMinDepthThreshold_Type()
)
cwredConfigPrecedMinDepthThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwredConfigPrecedMinDepthThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwredConfigPrecedMinDepthThreshold.setUnits("packets")
_CwredConfigPrecedMaxDepthThreshold_Type = Integer32
_CwredConfigPrecedMaxDepthThreshold_Object = MibTableColumn
cwredConfigPrecedMaxDepthThreshold = _CwredConfigPrecedMaxDepthThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2, 1, 3),
    _CwredConfigPrecedMaxDepthThreshold_Type()
)
cwredConfigPrecedMaxDepthThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwredConfigPrecedMaxDepthThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cwredConfigPrecedMaxDepthThreshold.setUnits("packets")
_CwredConfigPrecedPktsDropFraction_Type = Integer32
_CwredConfigPrecedPktsDropFraction_Object = MibTableColumn
cwredConfigPrecedPktsDropFraction = _CwredConfigPrecedPktsDropFraction_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 1, 2, 1, 4),
    _CwredConfigPrecedPktsDropFraction_Type()
)
cwredConfigPrecedPktsDropFraction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwredConfigPrecedPktsDropFraction.setStatus("current")
_CwredStats_ObjectIdentity = ObjectIdentity
cwredStats = _CwredStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2)
)
_CwredQueueTable_Object = MibTable
cwredQueueTable = _CwredQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cwredQueueTable.setStatus("current")
_CwredQueueEntry_Object = MibTableRow
cwredQueueEntry = _CwredQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    cwredQueueEntry.setStatus("current")
_CwredQueueAverage_Type = Gauge32
_CwredQueueAverage_Object = MibTableColumn
cwredQueueAverage = _CwredQueueAverage_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 1, 1, 1),
    _CwredQueueAverage_Type()
)
cwredQueueAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwredQueueAverage.setStatus("current")
if mibBuilder.loadTexts:
    cwredQueueAverage.setUnits("packets")
_CwredQueueDepth_Type = Gauge32
_CwredQueueDepth_Object = MibTableColumn
cwredQueueDepth = _CwredQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 1, 1, 2),
    _CwredQueueDepth_Type()
)
cwredQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwredQueueDepth.setStatus("current")
if mibBuilder.loadTexts:
    cwredQueueDepth.setUnits("packets")
_CwredStatTable_Object = MibTable
cwredStatTable = _CwredStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cwredStatTable.setStatus("current")
_CwredStatEntry_Object = MibTableRow
cwredStatEntry = _CwredStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    cwredStatEntry.setStatus("current")
_CwredStatSwitchedPkts_Type = Counter32
_CwredStatSwitchedPkts_Object = MibTableColumn
cwredStatSwitchedPkts = _CwredStatSwitchedPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 2, 1, 1),
    _CwredStatSwitchedPkts_Type()
)
cwredStatSwitchedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwredStatSwitchedPkts.setStatus("current")
if mibBuilder.loadTexts:
    cwredStatSwitchedPkts.setUnits("packets")
_CwredStatRandomFilteredPkts_Type = Counter32
_CwredStatRandomFilteredPkts_Object = MibTableColumn
cwredStatRandomFilteredPkts = _CwredStatRandomFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 2, 1, 2),
    _CwredStatRandomFilteredPkts_Type()
)
cwredStatRandomFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwredStatRandomFilteredPkts.setStatus("current")
if mibBuilder.loadTexts:
    cwredStatRandomFilteredPkts.setUnits("packets")
_CwredStatMaxFilteredPkts_Type = Counter32
_CwredStatMaxFilteredPkts_Object = MibTableColumn
cwredStatMaxFilteredPkts = _CwredStatMaxFilteredPkts_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 1, 2, 2, 1, 3),
    _CwredStatMaxFilteredPkts_Type()
)
cwredStatMaxFilteredPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwredStatMaxFilteredPkts.setStatus("current")
if mibBuilder.loadTexts:
    cwredStatMaxFilteredPkts.setUnits("packets")
_CiscoWredMIBConformance_ObjectIdentity = ObjectIdentity
ciscoWredMIBConformance = _CiscoWredMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 3)
)
_CiscoWredMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoWredMIBCompliances = _CiscoWredMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 3, 1)
)
_CiscoWredMIBGroups_ObjectIdentity = ObjectIdentity
ciscoWredMIBGroups = _CiscoWredMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 3, 2)
)
cwredConfigGlobEntry.registerAugmentions(
    ("CISCO-WRED-MIB",
     "cwredQueueEntry")
)
cwredQueueEntry.setIndexNames(*cwredConfigGlobEntry.getIndexNames())
cwredConfigPrecedEntry.registerAugmentions(
    ("CISCO-WRED-MIB",
     "cwredStatEntry")
)
cwredStatEntry.setIndexNames(*cwredConfigPrecedEntry.getIndexNames())

# Managed Objects groups

ciscoWredMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 3, 2, 1)
)
ciscoWredMIBGroup.setObjects(
      *(("CISCO-WRED-MIB", "cwredConfigGlobQueueWeight"),
        ("CISCO-WRED-MIB", "cwredConfigPrecedMinDepthThreshold"),
        ("CISCO-WRED-MIB", "cwredConfigPrecedMaxDepthThreshold"),
        ("CISCO-WRED-MIB", "cwredConfigPrecedPktsDropFraction"),
        ("CISCO-WRED-MIB", "cwredQueueAverage"),
        ("CISCO-WRED-MIB", "cwredQueueDepth"),
        ("CISCO-WRED-MIB", "cwredStatSwitchedPkts"),
        ("CISCO-WRED-MIB", "cwredStatRandomFilteredPkts"),
        ("CISCO-WRED-MIB", "cwredStatMaxFilteredPkts"))
)
if mibBuilder.loadTexts:
    ciscoWredMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoWredMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 83, 3, 1, 1)
)
if mibBuilder.loadTexts:
    ciscoWredMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-WRED-MIB",
    **{"ciscoWredMIB": ciscoWredMIB,
       "ciscoWredMIBObjects": ciscoWredMIBObjects,
       "cwredConfig": cwredConfig,
       "cwredConfigGlobTable": cwredConfigGlobTable,
       "cwredConfigGlobEntry": cwredConfigGlobEntry,
       "cwredConfigGlobQueueWeight": cwredConfigGlobQueueWeight,
       "cwredConfigPrecedTable": cwredConfigPrecedTable,
       "cwredConfigPrecedEntry": cwredConfigPrecedEntry,
       "cwredConfigPrecedPrecedence": cwredConfigPrecedPrecedence,
       "cwredConfigPrecedMinDepthThreshold": cwredConfigPrecedMinDepthThreshold,
       "cwredConfigPrecedMaxDepthThreshold": cwredConfigPrecedMaxDepthThreshold,
       "cwredConfigPrecedPktsDropFraction": cwredConfigPrecedPktsDropFraction,
       "cwredStats": cwredStats,
       "cwredQueueTable": cwredQueueTable,
       "cwredQueueEntry": cwredQueueEntry,
       "cwredQueueAverage": cwredQueueAverage,
       "cwredQueueDepth": cwredQueueDepth,
       "cwredStatTable": cwredStatTable,
       "cwredStatEntry": cwredStatEntry,
       "cwredStatSwitchedPkts": cwredStatSwitchedPkts,
       "cwredStatRandomFilteredPkts": cwredStatRandomFilteredPkts,
       "cwredStatMaxFilteredPkts": cwredStatMaxFilteredPkts,
       "ciscoWredMIBConformance": ciscoWredMIBConformance,
       "ciscoWredMIBCompliances": ciscoWredMIBCompliances,
       "ciscoWredMIBCompliance": ciscoWredMIBCompliance,
       "ciscoWredMIBGroups": ciscoWredMIBGroups,
       "ciscoWredMIBGroup": ciscoWredMIBGroup}
)
