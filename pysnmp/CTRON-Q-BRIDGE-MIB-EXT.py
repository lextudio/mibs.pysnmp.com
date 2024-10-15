# SNMP MIB module (CTRON-Q-BRIDGE-MIB-EXT) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CTRON-Q-BRIDGE-MIB-EXT
# Produced by pysmi-1.5.4 at Mon Oct 14 21:19:10 2024
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

(dot1dBasePort,
 dot1dBasePortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort",
    "dot1dBasePortEntry")

(ctVlanExt,) = mibBuilder.importSymbols(
    "CTRON-MIB-NAMES",
    "ctVlanExt")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 VlanIndex,
 dot1qFdbId,
 dot1qTpFdbAddress,
 dot1qVlanCurrentEntry,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex",
    "dot1qFdbId",
    "dot1qTpFdbAddress",
    "dot1qVlanCurrentEntry",
    "dot1qVlanIndex")

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

ctQBridgeMibExt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7)
)
ctQBridgeMibExt.setRevisions(
        ("2007-02-16 17:44",
         "2005-01-21 17:17",
         "2004-06-04 12:41",
         "2003-12-15 20:53",
         "2002-07-26 20:45",
         "2002-07-19 14:12",
         "2001-04-16 18:16",
         "2001-01-10 13:29",
         "1999-10-06 08:12")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CtQBridgeMIBObjects_ObjectIdentity = ObjectIdentity
ctQBridgeMIBObjects = _CtQBridgeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1)
)
_CtDot1qPortVlanExtTable_Object = MibTable
ctDot1qPortVlanExtTable = _CtDot1qPortVlanExtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1)
)
if mibBuilder.loadTexts:
    ctDot1qPortVlanExtTable.setStatus("current")
_CtDot1qPortVlanEntry_Object = MibTableRow
ctDot1qPortVlanEntry = _CtDot1qPortVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctDot1qPortVlanEntry.setStatus("current")


class _CtDot1qPortDefaultForwardMode_Type(Integer32):
    """Custom type ctDot1qPortDefaultForwardMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwardAllFramesAsTagged", 2),
          ("forwardAllFramesAsUntagged", 3),
          ("forwardNoFrames", 1))
    )


_CtDot1qPortDefaultForwardMode_Type.__name__ = "Integer32"
_CtDot1qPortDefaultForwardMode_Object = MibTableColumn
ctDot1qPortDefaultForwardMode = _CtDot1qPortDefaultForwardMode_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1, 1),
    _CtDot1qPortDefaultForwardMode_Type()
)
ctDot1qPortDefaultForwardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDot1qPortDefaultForwardMode.setStatus("current")


class _CtDot1qPortDiscardTagged_Type(EnabledStatus):
    """Custom type ctDot1qPortDiscardTagged based on EnabledStatus"""


_CtDot1qPortDiscardTagged_Object = MibTableColumn
ctDot1qPortDiscardTagged = _CtDot1qPortDiscardTagged_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1, 2),
    _CtDot1qPortDiscardTagged_Type()
)
ctDot1qPortDiscardTagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDot1qPortDiscardTagged.setStatus("current")


class _CtDot1qPortReplaceTCI_Type(EnabledStatus):
    """Custom type ctDot1qPortReplaceTCI based on EnabledStatus"""


_CtDot1qPortReplaceTCI_Object = MibTableColumn
ctDot1qPortReplaceTCI = _CtDot1qPortReplaceTCI_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1, 3),
    _CtDot1qPortReplaceTCI_Type()
)
ctDot1qPortReplaceTCI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDot1qPortReplaceTCI.setStatus("current")
_CtDot1qVlanDynamicEgressTable_Object = MibTable
ctDot1qVlanDynamicEgressTable = _CtDot1qVlanDynamicEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2)
)
if mibBuilder.loadTexts:
    ctDot1qVlanDynamicEgressTable.setStatus("current")
_CtDot1qVlanDynamicEgressEntry_Object = MibTableRow
ctDot1qVlanDynamicEgressEntry = _CtDot1qVlanDynamicEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2, 1)
)
ctDot1qVlanDynamicEgressEntry.setIndexNames(
    (0, "CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanDynamicEgressIndex"),
)
if mibBuilder.loadTexts:
    ctDot1qVlanDynamicEgressEntry.setStatus("current")
_CtDot1qVlanDynamicEgressIndex_Type = VlanIndex
_CtDot1qVlanDynamicEgressIndex_Object = MibTableColumn
ctDot1qVlanDynamicEgressIndex = _CtDot1qVlanDynamicEgressIndex_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2, 1, 1),
    _CtDot1qVlanDynamicEgressIndex_Type()
)
ctDot1qVlanDynamicEgressIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctDot1qVlanDynamicEgressIndex.setStatus("current")


class _CtDot1qVlanDynamicEgressStatus_Type(EnabledStatus):
    """Custom type ctDot1qVlanDynamicEgressStatus based on EnabledStatus"""


_CtDot1qVlanDynamicEgressStatus_Object = MibTableColumn
ctDot1qVlanDynamicEgressStatus = _CtDot1qVlanDynamicEgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2, 1, 2),
    _CtDot1qVlanDynamicEgressStatus_Type()
)
ctDot1qVlanDynamicEgressStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDot1qVlanDynamicEgressStatus.setStatus("current")
_CtDot1qVlanCurrentExtTable_Object = MibTable
ctDot1qVlanCurrentExtTable = _CtDot1qVlanCurrentExtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 3)
)
if mibBuilder.loadTexts:
    ctDot1qVlanCurrentExtTable.setStatus("current")
_CtDot1qVlanCurrentEntryExt_Object = MibTableRow
ctDot1qVlanCurrentEntryExt = _CtDot1qVlanCurrentEntryExt_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 3, 1)
)
if mibBuilder.loadTexts:
    ctDot1qVlanCurrentEntryExt.setStatus("current")
_CtDot1qVlanForbidEgressPorts_Type = PortList
_CtDot1qVlanForbidEgressPorts_Object = MibTableColumn
ctDot1qVlanForbidEgressPorts = _CtDot1qVlanForbidEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 3, 1, 1),
    _CtDot1qVlanForbidEgressPorts_Type()
)
ctDot1qVlanForbidEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDot1qVlanForbidEgressPorts.setStatus("current")
_CtDot1qPortVlanEgressTable_Object = MibTable
ctDot1qPortVlanEgressTable = _CtDot1qPortVlanEgressTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4)
)
if mibBuilder.loadTexts:
    ctDot1qPortVlanEgressTable.setStatus("current")
_CtDot1qPortVlanEgressEntry_Object = MibTableRow
ctDot1qPortVlanEgressEntry = _CtDot1qPortVlanEgressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4, 1)
)
ctDot1qPortVlanEgressEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
)
if mibBuilder.loadTexts:
    ctDot1qPortVlanEgressEntry.setStatus("current")


class _CtDot1qPortVlanEgressStatus_Type(Integer32):
    """Custom type ctDot1qPortVlanEgressStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ctDynamicEgress", 4),
          ("ctPortDefFwdMode", 6),
          ("etsysPolicyProfile", 5),
          ("gvrp", 3),
          ("other", 1),
          ("rfc3580VlanTunnelAttribute", 7),
          ("static", 2))
    )


_CtDot1qPortVlanEgressStatus_Type.__name__ = "Integer32"
_CtDot1qPortVlanEgressStatus_Object = MibTableColumn
ctDot1qPortVlanEgressStatus = _CtDot1qPortVlanEgressStatus_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4, 1, 1),
    _CtDot1qPortVlanEgressStatus_Type()
)
ctDot1qPortVlanEgressStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDot1qPortVlanEgressStatus.setStatus("current")


class _CtDot1qPortVlanEgressType_Type(Integer32):
    """Custom type ctDot1qPortVlanEgressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forbidden", 3),
          ("tagged", 1),
          ("untagged", 2))
    )


_CtDot1qPortVlanEgressType_Type.__name__ = "Integer32"
_CtDot1qPortVlanEgressType_Object = MibTableColumn
ctDot1qPortVlanEgressType = _CtDot1qPortVlanEgressType_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4, 1, 2),
    _CtDot1qPortVlanEgressType_Type()
)
ctDot1qPortVlanEgressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctDot1qPortVlanEgressType.setStatus("current")
_CtDot1qTpFdbExtTable_Object = MibTable
ctDot1qTpFdbExtTable = _CtDot1qTpFdbExtTable_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 5)
)
if mibBuilder.loadTexts:
    ctDot1qTpFdbExtTable.setStatus("current")
_CtDot1qTpFdbExtEntry_Object = MibTableRow
ctDot1qTpFdbExtEntry = _CtDot1qTpFdbExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 5, 1)
)
ctDot1qTpFdbExtEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qFdbId"),
    (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"),
)
if mibBuilder.loadTexts:
    ctDot1qTpFdbExtEntry.setStatus("current")


class _CtDot1qTpFdbRemoveAddress_Type(TruthValue):
    """Custom type ctDot1qTpFdbRemoveAddress based on TruthValue"""


_CtDot1qTpFdbRemoveAddress_Object = MibTableColumn
ctDot1qTpFdbRemoveAddress = _CtDot1qTpFdbRemoveAddress_Object(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 5, 1, 1),
    _CtDot1qTpFdbRemoveAddress_Type()
)
ctDot1qTpFdbRemoveAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ctDot1qTpFdbRemoveAddress.setStatus("current")
_CtQBridgeConformance_ObjectIdentity = ObjectIdentity
ctQBridgeConformance = _CtQBridgeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2)
)
_CtQBridgeGroups_ObjectIdentity = ObjectIdentity
ctQBridgeGroups = _CtQBridgeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1)
)
_CtQBridgeCompliances_ObjectIdentity = ObjectIdentity
ctQBridgeCompliances = _CtQBridgeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2)
)
dot1dBasePortEntry.registerAugmentions(
    ("CTRON-Q-BRIDGE-MIB-EXT",
     "ctDot1qPortVlanEntry")
)
ctDot1qPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
dot1qVlanCurrentEntry.registerAugmentions(
    ("CTRON-Q-BRIDGE-MIB-EXT",
     "ctDot1qVlanCurrentEntryExt")
)
ctDot1qVlanCurrentEntryExt.setIndexNames(*dot1qVlanCurrentEntry.getIndexNames())

# Managed Objects groups

ctQBridgePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 1)
)
ctQBridgePortGroup.setObjects(
    ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortDefaultForwardMode")
)
if mibBuilder.loadTexts:
    ctQBridgePortGroup.setStatus("deprecated")

ctQBridgeVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 2)
)
ctQBridgeVlanGroup.setObjects(
    ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanDynamicEgressStatus")
)
if mibBuilder.loadTexts:
    ctQBridgeVlanGroup.setStatus("current")

ctQBridgePortGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 3)
)
ctQBridgePortGroup2.setObjects(
      *(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortDefaultForwardMode"),
        ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortDiscardTagged"))
)
if mibBuilder.loadTexts:
    ctQBridgePortGroup2.setStatus("current")

ctQBridgeVlanCurrentForbidGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 4)
)
ctQBridgeVlanCurrentForbidGroup.setObjects(
    ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanForbidEgressPorts")
)
if mibBuilder.loadTexts:
    ctQBridgeVlanCurrentForbidGroup.setStatus("current")

ctQBridgePortReplaceTCIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 5)
)
ctQBridgePortReplaceTCIGroup.setObjects(
    ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortReplaceTCI")
)
if mibBuilder.loadTexts:
    ctQBridgePortReplaceTCIGroup.setStatus("current")

ctQBridgePortVlanEgressGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 6)
)
ctQBridgePortVlanEgressGroup.setObjects(
      *(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanEgressStatus"),
        ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanEgressType"))
)
if mibBuilder.loadTexts:
    ctQBridgePortVlanEgressGroup.setStatus("current")

ctQBridgeTpFdbTableExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 7)
)
ctQBridgeTpFdbTableExtGroup.setObjects(
    ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qTpFdbRemoveAddress")
)
if mibBuilder.loadTexts:
    ctQBridgeTpFdbTableExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ctDot1qVlan = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ctDot1qVlan.setStatus(
        "deprecated"
    )

ctDot1qVlan2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 2)
)
if mibBuilder.loadTexts:
    ctDot1qVlan2.setStatus(
        "current"
    )

ctDot1qVlanCurentCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 3)
)
if mibBuilder.loadTexts:
    ctDot1qVlanCurentCompliance.setStatus(
        "current"
    )

ctDot1qPortVlanEgressCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 4)
)
if mibBuilder.loadTexts:
    ctDot1qPortVlanEgressCompliance.setStatus(
        "current"
    )

ctDot1qTpFdbTableExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 5)
)
if mibBuilder.loadTexts:
    ctDot1qTpFdbTableExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CTRON-Q-BRIDGE-MIB-EXT",
    **{"ctQBridgeMibExt": ctQBridgeMibExt,
       "ctQBridgeMIBObjects": ctQBridgeMIBObjects,
       "ctDot1qPortVlanExtTable": ctDot1qPortVlanExtTable,
       "ctDot1qPortVlanEntry": ctDot1qPortVlanEntry,
       "ctDot1qPortDefaultForwardMode": ctDot1qPortDefaultForwardMode,
       "ctDot1qPortDiscardTagged": ctDot1qPortDiscardTagged,
       "ctDot1qPortReplaceTCI": ctDot1qPortReplaceTCI,
       "ctDot1qVlanDynamicEgressTable": ctDot1qVlanDynamicEgressTable,
       "ctDot1qVlanDynamicEgressEntry": ctDot1qVlanDynamicEgressEntry,
       "ctDot1qVlanDynamicEgressIndex": ctDot1qVlanDynamicEgressIndex,
       "ctDot1qVlanDynamicEgressStatus": ctDot1qVlanDynamicEgressStatus,
       "ctDot1qVlanCurrentExtTable": ctDot1qVlanCurrentExtTable,
       "ctDot1qVlanCurrentEntryExt": ctDot1qVlanCurrentEntryExt,
       "ctDot1qVlanForbidEgressPorts": ctDot1qVlanForbidEgressPorts,
       "ctDot1qPortVlanEgressTable": ctDot1qPortVlanEgressTable,
       "ctDot1qPortVlanEgressEntry": ctDot1qPortVlanEgressEntry,
       "ctDot1qPortVlanEgressStatus": ctDot1qPortVlanEgressStatus,
       "ctDot1qPortVlanEgressType": ctDot1qPortVlanEgressType,
       "ctDot1qTpFdbExtTable": ctDot1qTpFdbExtTable,
       "ctDot1qTpFdbExtEntry": ctDot1qTpFdbExtEntry,
       "ctDot1qTpFdbRemoveAddress": ctDot1qTpFdbRemoveAddress,
       "ctQBridgeConformance": ctQBridgeConformance,
       "ctQBridgeGroups": ctQBridgeGroups,
       "ctQBridgePortGroup": ctQBridgePortGroup,
       "ctQBridgeVlanGroup": ctQBridgeVlanGroup,
       "ctQBridgePortGroup2": ctQBridgePortGroup2,
       "ctQBridgeVlanCurrentForbidGroup": ctQBridgeVlanCurrentForbidGroup,
       "ctQBridgePortReplaceTCIGroup": ctQBridgePortReplaceTCIGroup,
       "ctQBridgePortVlanEgressGroup": ctQBridgePortVlanEgressGroup,
       "ctQBridgeTpFdbTableExtGroup": ctQBridgeTpFdbTableExtGroup,
       "ctQBridgeCompliances": ctQBridgeCompliances,
       "ctDot1qVlan": ctDot1qVlan,
       "ctDot1qVlan2": ctDot1qVlan2,
       "ctDot1qVlanCurentCompliance": ctDot1qVlanCurentCompliance,
       "ctDot1qPortVlanEgressCompliance": ctDot1qPortVlanEgressCompliance,
       "ctDot1qTpFdbTableExtCompliance": ctDot1qTpFdbTableExtCompliance}
)
