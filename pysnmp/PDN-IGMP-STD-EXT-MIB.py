# SNMP MIB module (PDN-IGMP-STD-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PDN-IGMP-STD-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:37:47 2024
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

(igmpCacheEntry,
 igmpInterfaceEntry) = mibBuilder.importSymbols(
    "IGMP-STD-MIB",
    "igmpCacheEntry",
    "igmpInterfaceEntry")

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(SwitchState,) = mibBuilder.importSymbols(
    "PDN-TC",
    "SwitchState")

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

pdnIgmpStdExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47)
)
pdnIgmpStdExtMIB.setRevisions(
        ("2004-08-17 00:00",
         "2004-01-08 00:00",
         "2003-05-06 00:00",
         "2003-05-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnIgmpStdExtNotifications_ObjectIdentity = ObjectIdentity
pdnIgmpStdExtNotifications = _PdnIgmpStdExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 0)
)
_PdnIgmpStdExtObjects_ObjectIdentity = ObjectIdentity
pdnIgmpStdExtObjects = _PdnIgmpStdExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1)
)
_PdnIgmpInterfaceExtTable_Object = MibTable
pdnIgmpInterfaceExtTable = _PdnIgmpInterfaceExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 1)
)
if mibBuilder.loadTexts:
    pdnIgmpInterfaceExtTable.setStatus("current")
_PdnIgmpInterfaceExtEntry_Object = MibTableRow
pdnIgmpInterfaceExtEntry = _PdnIgmpInterfaceExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnIgmpInterfaceExtEntry.setStatus("current")


class _PdnIgmpInterfaceSnoopEnableDisable_Type(SwitchState):
    """Custom type pdnIgmpInterfaceSnoopEnableDisable based on SwitchState"""


_PdnIgmpInterfaceSnoopEnableDisable_Object = MibTableColumn
pdnIgmpInterfaceSnoopEnableDisable = _PdnIgmpInterfaceSnoopEnableDisable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 1, 1, 1),
    _PdnIgmpInterfaceSnoopEnableDisable_Type()
)
pdnIgmpInterfaceSnoopEnableDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIgmpInterfaceSnoopEnableDisable.setStatus("current")


class _PdnIgmpInterfaceLeaveDelay_Type(Unsigned32):
    """Custom type pdnIgmpInterfaceLeaveDelay based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PdnIgmpInterfaceLeaveDelay_Type.__name__ = "Unsigned32"
_PdnIgmpInterfaceLeaveDelay_Object = MibTableColumn
pdnIgmpInterfaceLeaveDelay = _PdnIgmpInterfaceLeaveDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 1, 1, 2),
    _PdnIgmpInterfaceLeaveDelay_Type()
)
pdnIgmpInterfaceLeaveDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIgmpInterfaceLeaveDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnIgmpInterfaceLeaveDelay.setUnits("tenths of a second")


class _PdnIgmpInterfaceLeaveJoinForwardingDelay_Type(Unsigned32):
    """Custom type pdnIgmpInterfaceLeaveJoinForwardingDelay based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_PdnIgmpInterfaceLeaveJoinForwardingDelay_Type.__name__ = "Unsigned32"
_PdnIgmpInterfaceLeaveJoinForwardingDelay_Object = MibTableColumn
pdnIgmpInterfaceLeaveJoinForwardingDelay = _PdnIgmpInterfaceLeaveJoinForwardingDelay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 1, 1, 3),
    _PdnIgmpInterfaceLeaveJoinForwardingDelay_Type()
)
pdnIgmpInterfaceLeaveJoinForwardingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIgmpInterfaceLeaveJoinForwardingDelay.setStatus("current")
if mibBuilder.loadTexts:
    pdnIgmpInterfaceLeaveJoinForwardingDelay.setUnits("tenths of a second")
_PdnIgmpCacheExtTable_Object = MibTable
pdnIgmpCacheExtTable = _PdnIgmpCacheExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 2)
)
if mibBuilder.loadTexts:
    pdnIgmpCacheExtTable.setStatus("current")
_PdnIgmpCacheExtEntry_Object = MibTableRow
pdnIgmpCacheExtEntry = _PdnIgmpCacheExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 2, 1)
)
if mibBuilder.loadTexts:
    pdnIgmpCacheExtEntry.setStatus("current")
_PdnIgmpCacheStatsMulticastPktsIn_Type = Counter32
_PdnIgmpCacheStatsMulticastPktsIn_Object = MibTableColumn
pdnIgmpCacheStatsMulticastPktsIn = _PdnIgmpCacheStatsMulticastPktsIn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 2, 1, 1),
    _PdnIgmpCacheStatsMulticastPktsIn_Type()
)
pdnIgmpCacheStatsMulticastPktsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIgmpCacheStatsMulticastPktsIn.setStatus("current")
_PdnIgmpCacheStatsMulticastPktsOut_Type = Counter32
_PdnIgmpCacheStatsMulticastPktsOut_Object = MibTableColumn
pdnIgmpCacheStatsMulticastPktsOut = _PdnIgmpCacheStatsMulticastPktsOut_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 2, 1, 2),
    _PdnIgmpCacheStatsMulticastPktsOut_Type()
)
pdnIgmpCacheStatsMulticastPktsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIgmpCacheStatsMulticastPktsOut.setStatus("current")
_PdnIgmpCacheStatsIgmpQueriesIn_Type = Counter32
_PdnIgmpCacheStatsIgmpQueriesIn_Object = MibTableColumn
pdnIgmpCacheStatsIgmpQueriesIn = _PdnIgmpCacheStatsIgmpQueriesIn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 2, 1, 3),
    _PdnIgmpCacheStatsIgmpQueriesIn_Type()
)
pdnIgmpCacheStatsIgmpQueriesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIgmpCacheStatsIgmpQueriesIn.setStatus("current")
_PdnIgmpCacheStatsIgmpQueriesOut_Type = Counter32
_PdnIgmpCacheStatsIgmpQueriesOut_Object = MibTableColumn
pdnIgmpCacheStatsIgmpQueriesOut = _PdnIgmpCacheStatsIgmpQueriesOut_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 2, 1, 4),
    _PdnIgmpCacheStatsIgmpQueriesOut_Type()
)
pdnIgmpCacheStatsIgmpQueriesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIgmpCacheStatsIgmpQueriesOut.setStatus("current")
_PdnIgmpCacheStatsIgmpReportsIn_Type = Counter32
_PdnIgmpCacheStatsIgmpReportsIn_Object = MibTableColumn
pdnIgmpCacheStatsIgmpReportsIn = _PdnIgmpCacheStatsIgmpReportsIn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 2, 1, 5),
    _PdnIgmpCacheStatsIgmpReportsIn_Type()
)
pdnIgmpCacheStatsIgmpReportsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIgmpCacheStatsIgmpReportsIn.setStatus("current")
_PdnIgmpCacheStatsIgmpReportsOut_Type = Counter32
_PdnIgmpCacheStatsIgmpReportsOut_Object = MibTableColumn
pdnIgmpCacheStatsIgmpReportsOut = _PdnIgmpCacheStatsIgmpReportsOut_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 2, 1, 6),
    _PdnIgmpCacheStatsIgmpReportsOut_Type()
)
pdnIgmpCacheStatsIgmpReportsOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIgmpCacheStatsIgmpReportsOut.setStatus("current")
_PdnIgmpCacheStatsIgmpLeavesIn_Type = Counter32
_PdnIgmpCacheStatsIgmpLeavesIn_Object = MibTableColumn
pdnIgmpCacheStatsIgmpLeavesIn = _PdnIgmpCacheStatsIgmpLeavesIn_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 2, 1, 7),
    _PdnIgmpCacheStatsIgmpLeavesIn_Type()
)
pdnIgmpCacheStatsIgmpLeavesIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIgmpCacheStatsIgmpLeavesIn.setStatus("current")
_PdnIgmpCacheStatsIgmpLeavesOut_Type = Counter32
_PdnIgmpCacheStatsIgmpLeavesOut_Object = MibTableColumn
pdnIgmpCacheStatsIgmpLeavesOut = _PdnIgmpCacheStatsIgmpLeavesOut_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 2, 1, 8),
    _PdnIgmpCacheStatsIgmpLeavesOut_Type()
)
pdnIgmpCacheStatsIgmpLeavesOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnIgmpCacheStatsIgmpLeavesOut.setStatus("current")


class _PdnIgmpSnoopingSelection_Type(SwitchState):
    """Custom type pdnIgmpSnoopingSelection based on SwitchState"""


_PdnIgmpSnoopingSelection_Object = MibScalar
pdnIgmpSnoopingSelection = _PdnIgmpSnoopingSelection_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 3),
    _PdnIgmpSnoopingSelection_Type()
)
pdnIgmpSnoopingSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIgmpSnoopingSelection.setStatus("current")


class _PdnIgmpGeneralQueryInterval_Type(Unsigned32):
    """Custom type pdnIgmpGeneralQueryInterval based on Unsigned32"""
    defaultValue = 125


_PdnIgmpGeneralQueryInterval_Object = MibScalar
pdnIgmpGeneralQueryInterval = _PdnIgmpGeneralQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 1, 4),
    _PdnIgmpGeneralQueryInterval_Type()
)
pdnIgmpGeneralQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnIgmpGeneralQueryInterval.setStatus("current")
if mibBuilder.loadTexts:
    pdnIgmpGeneralQueryInterval.setUnits("seconds")
_PdnIgmpStdExtAFNs_ObjectIdentity = ObjectIdentity
pdnIgmpStdExtAFNs = _PdnIgmpStdExtAFNs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 2)
)
_PdnIgmpStdExtConformance_ObjectIdentity = ObjectIdentity
pdnIgmpStdExtConformance = _PdnIgmpStdExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3)
)
_PdnIgmpStdExtCompliances_ObjectIdentity = ObjectIdentity
pdnIgmpStdExtCompliances = _PdnIgmpStdExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 1)
)
_PdnIgmpStdExtGroups_ObjectIdentity = ObjectIdentity
pdnIgmpStdExtGroups = _PdnIgmpStdExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 2)
)
_PdnIgmpStdExtObjGroups_ObjectIdentity = ObjectIdentity
pdnIgmpStdExtObjGroups = _PdnIgmpStdExtObjGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 2, 1)
)
_PdnIgmpStdExtAfnGroups_ObjectIdentity = ObjectIdentity
pdnIgmpStdExtAfnGroups = _PdnIgmpStdExtAfnGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 2, 2)
)
_PdnIgmpStdExtNtfyGroups_ObjectIdentity = ObjectIdentity
pdnIgmpStdExtNtfyGroups = _PdnIgmpStdExtNtfyGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 2, 3)
)
igmpInterfaceEntry.registerAugmentions(
    ("PDN-IGMP-STD-EXT-MIB",
     "pdnIgmpInterfaceExtEntry")
)
pdnIgmpInterfaceExtEntry.setIndexNames(*igmpInterfaceEntry.getIndexNames())
igmpCacheEntry.registerAugmentions(
    ("PDN-IGMP-STD-EXT-MIB",
     "pdnIgmpCacheExtEntry")
)
pdnIgmpCacheExtEntry.setIndexNames(*igmpCacheEntry.getIndexNames())

# Managed Objects groups

pdnIgmpStdExtConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 2, 1, 1)
)
pdnIgmpStdExtConfigGroup.setObjects(
      *(("PDN-IGMP-STD-EXT-MIB", "pdnIgmpInterfaceSnoopEnableDisable"),
        ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpInterfaceLeaveDelay"),
        ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpInterfaceLeaveJoinForwardingDelay"))
)
if mibBuilder.loadTexts:
    pdnIgmpStdExtConfigGroup.setStatus("current")

pdnIgmpStdExtStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 2, 1, 2)
)
pdnIgmpStdExtStatsGroup.setObjects(
      *(("PDN-IGMP-STD-EXT-MIB", "pdnIgmpCacheStatsMulticastPktsIn"),
        ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpCacheStatsMulticastPktsOut"),
        ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpCacheStatsIgmpQueriesIn"),
        ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpCacheStatsIgmpQueriesOut"),
        ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpCacheStatsIgmpReportsIn"),
        ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpCacheStatsIgmpReportsOut"),
        ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpCacheStatsIgmpLeavesIn"),
        ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpCacheStatsIgmpLeavesOut"))
)
if mibBuilder.loadTexts:
    pdnIgmpStdExtStatsGroup.setStatus("current")

pdnIgmpStdExtGeneralConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 2, 1, 3)
)
pdnIgmpStdExtGeneralConfigGroup.setObjects(
    ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpSnoopingSelection")
)
if mibBuilder.loadTexts:
    pdnIgmpStdExtGeneralConfigGroup.setStatus("deprecated")

pdnIgmpStdExtGeneralConfigGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 2, 1, 4)
)
pdnIgmpStdExtGeneralConfigGroupV2.setObjects(
      *(("PDN-IGMP-STD-EXT-MIB", "pdnIgmpSnoopingSelection"),
        ("PDN-IGMP-STD-EXT-MIB", "pdnIgmpGeneralQueryInterval"))
)
if mibBuilder.loadTexts:
    pdnIgmpStdExtGeneralConfigGroupV2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pdnIgmpStdExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnIgmpStdExtMIBCompliance.setStatus(
        "deprecated"
    )

pdnIgmpStdExtMIBComplianceV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 47, 3, 1, 2)
)
if mibBuilder.loadTexts:
    pdnIgmpStdExtMIBComplianceV2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-IGMP-STD-EXT-MIB",
    **{"pdnIgmpStdExtMIB": pdnIgmpStdExtMIB,
       "pdnIgmpStdExtNotifications": pdnIgmpStdExtNotifications,
       "pdnIgmpStdExtObjects": pdnIgmpStdExtObjects,
       "pdnIgmpInterfaceExtTable": pdnIgmpInterfaceExtTable,
       "pdnIgmpInterfaceExtEntry": pdnIgmpInterfaceExtEntry,
       "pdnIgmpInterfaceSnoopEnableDisable": pdnIgmpInterfaceSnoopEnableDisable,
       "pdnIgmpInterfaceLeaveDelay": pdnIgmpInterfaceLeaveDelay,
       "pdnIgmpInterfaceLeaveJoinForwardingDelay": pdnIgmpInterfaceLeaveJoinForwardingDelay,
       "pdnIgmpCacheExtTable": pdnIgmpCacheExtTable,
       "pdnIgmpCacheExtEntry": pdnIgmpCacheExtEntry,
       "pdnIgmpCacheStatsMulticastPktsIn": pdnIgmpCacheStatsMulticastPktsIn,
       "pdnIgmpCacheStatsMulticastPktsOut": pdnIgmpCacheStatsMulticastPktsOut,
       "pdnIgmpCacheStatsIgmpQueriesIn": pdnIgmpCacheStatsIgmpQueriesIn,
       "pdnIgmpCacheStatsIgmpQueriesOut": pdnIgmpCacheStatsIgmpQueriesOut,
       "pdnIgmpCacheStatsIgmpReportsIn": pdnIgmpCacheStatsIgmpReportsIn,
       "pdnIgmpCacheStatsIgmpReportsOut": pdnIgmpCacheStatsIgmpReportsOut,
       "pdnIgmpCacheStatsIgmpLeavesIn": pdnIgmpCacheStatsIgmpLeavesIn,
       "pdnIgmpCacheStatsIgmpLeavesOut": pdnIgmpCacheStatsIgmpLeavesOut,
       "pdnIgmpSnoopingSelection": pdnIgmpSnoopingSelection,
       "pdnIgmpGeneralQueryInterval": pdnIgmpGeneralQueryInterval,
       "pdnIgmpStdExtAFNs": pdnIgmpStdExtAFNs,
       "pdnIgmpStdExtConformance": pdnIgmpStdExtConformance,
       "pdnIgmpStdExtCompliances": pdnIgmpStdExtCompliances,
       "pdnIgmpStdExtMIBCompliance": pdnIgmpStdExtMIBCompliance,
       "pdnIgmpStdExtMIBComplianceV2": pdnIgmpStdExtMIBComplianceV2,
       "pdnIgmpStdExtGroups": pdnIgmpStdExtGroups,
       "pdnIgmpStdExtObjGroups": pdnIgmpStdExtObjGroups,
       "pdnIgmpStdExtConfigGroup": pdnIgmpStdExtConfigGroup,
       "pdnIgmpStdExtStatsGroup": pdnIgmpStdExtStatsGroup,
       "pdnIgmpStdExtGeneralConfigGroup": pdnIgmpStdExtGeneralConfigGroup,
       "pdnIgmpStdExtGeneralConfigGroupV2": pdnIgmpStdExtGeneralConfigGroupV2,
       "pdnIgmpStdExtAfnGroups": pdnIgmpStdExtAfnGroups,
       "pdnIgmpStdExtNtfyGroups": pdnIgmpStdExtNtfyGroups}
)
