# SNMP MIB module (TRAFFIC-TEMPLATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/TRAFFIC-TEMPLATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:07:18 2024
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfTrafficTemplateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72)
)
hpicfTrafficTemplateMIB.setRevisions(
        ("2012-02-02 00:00",
         "2010-03-04 12:30")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfTrafficTemplateObjects_ObjectIdentity = ObjectIdentity
hpicfTrafficTemplateObjects = _HpicfTrafficTemplateObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1)
)
_HpicfTrafficTemplateScalars_ObjectIdentity = ObjectIdentity
hpicfTrafficTemplateScalars = _HpicfTrafficTemplateScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 1)
)


class _HpSwitchTrafficTemplateSystemDefaultName_Type(OctetString):
    """Custom type hpSwitchTrafficTemplateSystemDefaultName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchTrafficTemplateSystemDefaultName_Type.__name__ = "OctetString"
_HpSwitchTrafficTemplateSystemDefaultName_Object = MibScalar
hpSwitchTrafficTemplateSystemDefaultName = _HpSwitchTrafficTemplateSystemDefaultName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 1, 1),
    _HpSwitchTrafficTemplateSystemDefaultName_Type()
)
hpSwitchTrafficTemplateSystemDefaultName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTrafficTemplateSystemDefaultName.setStatus("current")
_HpSwitchTrafficTemplate_ObjectIdentity = ObjectIdentity
hpSwitchTrafficTemplate = _HpSwitchTrafficTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2)
)
_HpSwitchTrafficTemplateTable_Object = MibTable
hpSwitchTrafficTemplateTable = _HpSwitchTrafficTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpSwitchTrafficTemplateTable.setStatus("current")
_HpSwitchTrafficTemplateEntry_Object = MibTableRow
hpSwitchTrafficTemplateEntry = _HpSwitchTrafficTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1)
)
hpSwitchTrafficTemplateEntry.setIndexNames(
    (0, "TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateName"),
)
if mibBuilder.loadTexts:
    hpSwitchTrafficTemplateEntry.setStatus("current")


class _HpSwitchTrafficTemplateName_Type(DisplayString):
    """Custom type hpSwitchTrafficTemplateName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HpSwitchTrafficTemplateName_Type.__name__ = "DisplayString"
_HpSwitchTrafficTemplateName_Object = MibTableColumn
hpSwitchTrafficTemplateName = _HpSwitchTrafficTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1, 1),
    _HpSwitchTrafficTemplateName_Type()
)
hpSwitchTrafficTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchTrafficTemplateName.setStatus("current")
_HpSwitchTrafficTemplateMappedPorts_Type = PortList
_HpSwitchTrafficTemplateMappedPorts_Object = MibTableColumn
hpSwitchTrafficTemplateMappedPorts = _HpSwitchTrafficTemplateMappedPorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1, 2),
    _HpSwitchTrafficTemplateMappedPorts_Type()
)
hpSwitchTrafficTemplateMappedPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchTrafficTemplateMappedPorts.setStatus("current")
_HpSwitchTrafficTemplateRowStatus_Type = RowStatus
_HpSwitchTrafficTemplateRowStatus_Object = MibTableColumn
hpSwitchTrafficTemplateRowStatus = _HpSwitchTrafficTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1, 3),
    _HpSwitchTrafficTemplateRowStatus_Type()
)
hpSwitchTrafficTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpSwitchTrafficTemplateRowStatus.setStatus("current")


class _HpSwitchTrafficTemplateNumQueues_Type(Integer32):
    """Custom type hpSwitchTrafficTemplateNumQueues based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9000),
    )


_HpSwitchTrafficTemplateNumQueues_Type.__name__ = "Integer32"
_HpSwitchTrafficTemplateNumQueues_Object = MibTableColumn
hpSwitchTrafficTemplateNumQueues = _HpSwitchTrafficTemplateNumQueues_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1, 4),
    _HpSwitchTrafficTemplateNumQueues_Type()
)
hpSwitchTrafficTemplateNumQueues.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTrafficTemplateNumQueues.setStatus("current")
_HpSwitchTrafficTemplatePredefined_Type = TruthValue
_HpSwitchTrafficTemplatePredefined_Object = MibTableColumn
hpSwitchTrafficTemplatePredefined = _HpSwitchTrafficTemplatePredefined_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 1, 1, 5),
    _HpSwitchTrafficTemplatePredefined_Type()
)
hpSwitchTrafficTemplatePredefined.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpSwitchTrafficTemplatePredefined.setStatus("current")
_HpSwitchTrafficGroupTable_Object = MibTable
hpSwitchTrafficGroupTable = _HpSwitchTrafficGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2)
)
if mibBuilder.loadTexts:
    hpSwitchTrafficGroupTable.setStatus("current")
_HpSwitchTrafficGroupEntry_Object = MibTableRow
hpSwitchTrafficGroupEntry = _HpSwitchTrafficGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1)
)
hpSwitchTrafficGroupEntry.setIndexNames(
    (0, "TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateName"),
    (0, "TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficQueue"),
)
if mibBuilder.loadTexts:
    hpSwitchTrafficGroupEntry.setStatus("current")


class _HpSwitchTrafficQueue_Type(Integer32):
    """Custom type hpSwitchTrafficQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9000),
    )


_HpSwitchTrafficQueue_Type.__name__ = "Integer32"
_HpSwitchTrafficQueue_Object = MibTableColumn
hpSwitchTrafficQueue = _HpSwitchTrafficQueue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 1),
    _HpSwitchTrafficQueue_Type()
)
hpSwitchTrafficQueue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpSwitchTrafficQueue.setStatus("current")


class _HpSwitchTrafficGroupID_Type(Integer32):
    """Custom type hpSwitchTrafficGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpSwitchTrafficGroupID_Type.__name__ = "Integer32"
_HpSwitchTrafficGroupID_Object = MibTableColumn
hpSwitchTrafficGroupID = _HpSwitchTrafficGroupID_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 2),
    _HpSwitchTrafficGroupID_Type()
)
hpSwitchTrafficGroupID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTrafficGroupID.setStatus("current")


class _HpSwitchTrafficGroupName_Type(OctetString):
    """Custom type hpSwitchTrafficGroupName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HpSwitchTrafficGroupName_Type.__name__ = "OctetString"
_HpSwitchTrafficGroupName_Object = MibTableColumn
hpSwitchTrafficGroupName = _HpSwitchTrafficGroupName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 3),
    _HpSwitchTrafficGroupName_Type()
)
hpSwitchTrafficGroupName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTrafficGroupName.setStatus("current")


class _HpSwitchTrafficGroupPriorityMap_Type(Bits):
    """Custom type hpSwitchTrafficGroupPriorityMap based on Bits"""
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority10", 10),
          ("priority11", 11),
          ("priority12", 12),
          ("priority13", 13),
          ("priority14", 14),
          ("priority15", 15),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7),
          ("priority8", 8),
          ("priority9", 9))
    )

_HpSwitchTrafficGroupPriorityMap_Type.__name__ = "Bits"
_HpSwitchTrafficGroupPriorityMap_Object = MibTableColumn
hpSwitchTrafficGroupPriorityMap = _HpSwitchTrafficGroupPriorityMap_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 4),
    _HpSwitchTrafficGroupPriorityMap_Type()
)
hpSwitchTrafficGroupPriorityMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTrafficGroupPriorityMap.setStatus("current")
_HpSwitchTrafficGroupLossless_Type = TruthValue
_HpSwitchTrafficGroupLossless_Object = MibTableColumn
hpSwitchTrafficGroupLossless = _HpSwitchTrafficGroupLossless_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 5),
    _HpSwitchTrafficGroupLossless_Type()
)
hpSwitchTrafficGroupLossless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTrafficGroupLossless.setStatus("current")


class _HpSwitchTrafficGroupEgressDiscardThreshold_Type(Integer32):
    """Custom type hpSwitchTrafficGroupEgressDiscardThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 3),
          ("low", 1),
          ("medium", 2))
    )


_HpSwitchTrafficGroupEgressDiscardThreshold_Type.__name__ = "Integer32"
_HpSwitchTrafficGroupEgressDiscardThreshold_Object = MibTableColumn
hpSwitchTrafficGroupEgressDiscardThreshold = _HpSwitchTrafficGroupEgressDiscardThreshold_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 1, 2, 2, 1, 6),
    _HpSwitchTrafficGroupEgressDiscardThreshold_Type()
)
hpSwitchTrafficGroupEgressDiscardThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpSwitchTrafficGroupEgressDiscardThreshold.setStatus("current")
_HpicfTrafficTempalteConformance_ObjectIdentity = ObjectIdentity
hpicfTrafficTempalteConformance = _HpicfTrafficTempalteConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2)
)
_HpicfTrafficTemplateGroups_ObjectIdentity = ObjectIdentity
hpicfTrafficTemplateGroups = _HpicfTrafficTemplateGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1)
)
_HpicfTrafficTemplateCompliances_ObjectIdentity = ObjectIdentity
hpicfTrafficTemplateCompliances = _HpicfTrafficTemplateCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 2)
)

# Managed Objects groups

hpicfTrafficTemplateScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1, 1)
)
hpicfTrafficTemplateScalarGroup.setObjects(
    ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateSystemDefaultName")
)
if mibBuilder.loadTexts:
    hpicfTrafficTemplateScalarGroup.setStatus("current")

hpicfTrafficTemplateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1, 2)
)
hpicfTrafficTemplateGroup.setObjects(
      *(("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateMappedPorts"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfTrafficTemplateGroup.setStatus("deprecated")

hpicfTrafficGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1, 3)
)
hpicfTrafficGroup.setObjects(
      *(("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupID"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupName"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupPriorityMap"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupLossless"))
)
if mibBuilder.loadTexts:
    hpicfTrafficGroup.setStatus("deprecated")

hpicfTrafficTemplateGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1, 4)
)
hpicfTrafficTemplateGroup2.setObjects(
      *(("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateMappedPorts"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateRowStatus"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplateNumQueues"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficTemplatePredefined"))
)
if mibBuilder.loadTexts:
    hpicfTrafficTemplateGroup2.setStatus("current")

hpicfTrafficGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 1, 5)
)
hpicfTrafficGroup2.setObjects(
      *(("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupID"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupName"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupPriorityMap"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupLossless"),
        ("TRAFFIC-TEMPLATE-MIB", "hpSwitchTrafficGroupEgressDiscardThreshold"))
)
if mibBuilder.loadTexts:
    hpicfTrafficGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfTrafficTemplateCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfTrafficTemplateCompliance.setStatus(
        "deprecated"
    )

hpicfTrafficTemplateCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 72, 2, 2, 2)
)
if mibBuilder.loadTexts:
    hpicfTrafficTemplateCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAFFIC-TEMPLATE-MIB",
    **{"hpicfTrafficTemplateMIB": hpicfTrafficTemplateMIB,
       "hpicfTrafficTemplateObjects": hpicfTrafficTemplateObjects,
       "hpicfTrafficTemplateScalars": hpicfTrafficTemplateScalars,
       "hpSwitchTrafficTemplateSystemDefaultName": hpSwitchTrafficTemplateSystemDefaultName,
       "hpSwitchTrafficTemplate": hpSwitchTrafficTemplate,
       "hpSwitchTrafficTemplateTable": hpSwitchTrafficTemplateTable,
       "hpSwitchTrafficTemplateEntry": hpSwitchTrafficTemplateEntry,
       "hpSwitchTrafficTemplateName": hpSwitchTrafficTemplateName,
       "hpSwitchTrafficTemplateMappedPorts": hpSwitchTrafficTemplateMappedPorts,
       "hpSwitchTrafficTemplateRowStatus": hpSwitchTrafficTemplateRowStatus,
       "hpSwitchTrafficTemplateNumQueues": hpSwitchTrafficTemplateNumQueues,
       "hpSwitchTrafficTemplatePredefined": hpSwitchTrafficTemplatePredefined,
       "hpSwitchTrafficGroupTable": hpSwitchTrafficGroupTable,
       "hpSwitchTrafficGroupEntry": hpSwitchTrafficGroupEntry,
       "hpSwitchTrafficQueue": hpSwitchTrafficQueue,
       "hpSwitchTrafficGroupID": hpSwitchTrafficGroupID,
       "hpSwitchTrafficGroupName": hpSwitchTrafficGroupName,
       "hpSwitchTrafficGroupPriorityMap": hpSwitchTrafficGroupPriorityMap,
       "hpSwitchTrafficGroupLossless": hpSwitchTrafficGroupLossless,
       "hpSwitchTrafficGroupEgressDiscardThreshold": hpSwitchTrafficGroupEgressDiscardThreshold,
       "hpicfTrafficTempalteConformance": hpicfTrafficTempalteConformance,
       "hpicfTrafficTemplateGroups": hpicfTrafficTemplateGroups,
       "hpicfTrafficTemplateScalarGroup": hpicfTrafficTemplateScalarGroup,
       "hpicfTrafficTemplateGroup": hpicfTrafficTemplateGroup,
       "hpicfTrafficGroup": hpicfTrafficGroup,
       "hpicfTrafficTemplateGroup2": hpicfTrafficTemplateGroup2,
       "hpicfTrafficGroup2": hpicfTrafficGroup2,
       "hpicfTrafficTemplateCompliances": hpicfTrafficTemplateCompliances,
       "hpicfTrafficTemplateCompliance": hpicfTrafficTemplateCompliance,
       "hpicfTrafficTemplateCompliance2": hpicfTrafficTemplateCompliance2}
)
