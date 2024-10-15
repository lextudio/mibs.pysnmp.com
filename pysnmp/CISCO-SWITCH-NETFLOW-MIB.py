# SNMP MIB module (CISCO-SWITCH-NETFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SWITCH-NETFLOW-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:13 2024
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

(Percent,) = mibBuilder.importSymbols(
    "CISCO-QOS-PIB-MIB",
    "Percent")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

(entPhysicalDescr,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalDescr",
    "entPhysicalIndex")

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

ciscoSwitchNetflowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737)
)
ciscoSwitchNetflowMIB.setRevisions(
        ("2010-05-26 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CsnNetflowDirectionTypes(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("egress", 3),
          ("ingress", 2),
          ("ingressAndEgress", 4),
          ("none", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoSwitchNetflowMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSwitchNetflowMIBNotifs = _CiscoSwitchNetflowMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 0)
)
_CiscoSwitchNetflowMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSwitchNetflowMIBObjects = _CiscoSwitchNetflowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1)
)
_CsnAccounting_ObjectIdentity = ObjectIdentity
csnAccounting = _CsnAccounting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1)
)
_CsnAccGlobal_ObjectIdentity = ObjectIdentity
csnAccGlobal = _CsnAccGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 1)
)
_CsnNetflowDirectionType_Type = CsnNetflowDirectionTypes
_CsnNetflowDirectionType_Object = MibScalar
csnNetflowDirectionType = _CsnNetflowDirectionType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 1, 1),
    _CsnNetflowDirectionType_Type()
)
csnNetflowDirectionType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csnNetflowDirectionType.setStatus("current")
_CsnAccNotifControl_ObjectIdentity = ObjectIdentity
csnAccNotifControl = _CsnAccNotifControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 2)
)
_CsnUsageThreshExceedNotifEnable_Type = TruthValue
_CsnUsageThreshExceedNotifEnable_Object = MibScalar
csnUsageThreshExceedNotifEnable = _CsnUsageThreshExceedNotifEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 2, 1),
    _CsnUsageThreshExceedNotifEnable_Type()
)
csnUsageThreshExceedNotifEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csnUsageThreshExceedNotifEnable.setStatus("current")
_CshAccUsageThresh_ObjectIdentity = ObjectIdentity
cshAccUsageThresh = _CshAccUsageThresh_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3)
)
_CsnUsageThreshTable_Object = MibTable
csnUsageThreshTable = _CsnUsageThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    csnUsageThreshTable.setStatus("current")
_CsnUsageThreshEntry_Object = MibTableRow
csnUsageThreshEntry = _CsnUsageThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3, 1, 1)
)
csnUsageThreshEntry.setIndexNames(
    (0, "CISCO-SWITCH-NETFLOW-MIB", "csnUsageDirection"),
)
if mibBuilder.loadTexts:
    csnUsageThreshEntry.setStatus("current")
_CsnUsageDirection_Type = CsnNetflowDirectionTypes
_CsnUsageDirection_Object = MibTableColumn
csnUsageDirection = _CsnUsageDirection_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3, 1, 1, 1),
    _CsnUsageDirection_Type()
)
csnUsageDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    csnUsageDirection.setStatus("current")
_CsnUsageThreshold_Type = Percent
_CsnUsageThreshold_Object = MibTableColumn
csnUsageThreshold = _CsnUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3, 1, 1, 2),
    _CsnUsageThreshold_Type()
)
csnUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csnUsageThreshold.setStatus("current")


class _CsnUsageInterval_Type(Unsigned32):
    """Custom type csnUsageInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_CsnUsageInterval_Type.__name__ = "Unsigned32"
_CsnUsageInterval_Object = MibTableColumn
csnUsageInterval = _CsnUsageInterval_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 3, 1, 1, 3),
    _CsnUsageInterval_Type()
)
csnUsageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csnUsageInterval.setStatus("current")
if mibBuilder.loadTexts:
    csnUsageInterval.setUnits("seconds")
_CsnAccUtilization_ObjectIdentity = ObjectIdentity
csnAccUtilization = _CsnAccUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 4)
)
_CsnUtilizationTable_Object = MibTable
csnUtilizationTable = _CsnUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    csnUtilizationTable.setStatus("current")
_CsnUtilizationEntry_Object = MibTableRow
csnUtilizationEntry = _CsnUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 4, 1, 1)
)
csnUtilizationEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-SWITCH-NETFLOW-MIB", "csnUsageDirection"),
)
if mibBuilder.loadTexts:
    csnUtilizationEntry.setStatus("current")
_CsnUtilization_Type = Percent
_CsnUtilization_Object = MibTableColumn
csnUtilization = _CsnUtilization_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 4, 1, 1, 1),
    _CsnUtilization_Type()
)
csnUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csnUtilization.setStatus("current")
_CsnAccNetflowTableSize_ObjectIdentity = ObjectIdentity
csnAccNetflowTableSize = _CsnAccNetflowTableSize_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 5)
)
_CsnNetflowTableSizeTable_Object = MibTable
csnNetflowTableSizeTable = _CsnNetflowTableSizeTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    csnNetflowTableSizeTable.setStatus("current")
_CsnNetflowTableSizeEntry_Object = MibTableRow
csnNetflowTableSizeEntry = _CsnNetflowTableSizeEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 5, 1, 1)
)
csnNetflowTableSizeEntry.setIndexNames(
    (0, "CISCO-SWITCH-NETFLOW-MIB", "csnUsageDirection"),
)
if mibBuilder.loadTexts:
    csnNetflowTableSizeEntry.setStatus("current")
_CsnNetflowTableTotalEntries_Type = Unsigned32
_CsnNetflowTableTotalEntries_Object = MibTableColumn
csnNetflowTableTotalEntries = _CsnNetflowTableTotalEntries_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 5, 1, 1, 1),
    _CsnNetflowTableTotalEntries_Type()
)
csnNetflowTableTotalEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csnNetflowTableTotalEntries.setStatus("current")
_CsnAccSampler_ObjectIdentity = ObjectIdentity
csnAccSampler = _CsnAccSampler_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 6)
)
_CsnSamplerTotal_Type = Unsigned32
_CsnSamplerTotal_Object = MibScalar
csnSamplerTotal = _CsnSamplerTotal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 6, 1),
    _CsnSamplerTotal_Type()
)
csnSamplerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csnSamplerTotal.setStatus("current")
_CsnSamplerAvailable_Type = Unsigned32
_CsnSamplerAvailable_Object = MibScalar
csnSamplerAvailable = _CsnSamplerAvailable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 1, 1, 6, 2),
    _CsnSamplerAvailable_Type()
)
csnSamplerAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    csnSamplerAvailable.setStatus("current")
_CiscoSwitchNetflowMIBConform_ObjectIdentity = ObjectIdentity
ciscoSwitchNetflowMIBConform = _CiscoSwitchNetflowMIBConform_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2)
)
_CsnMIBCompliances_ObjectIdentity = ObjectIdentity
csnMIBCompliances = _CsnMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 1)
)
_CsnMIBGroups_ObjectIdentity = ObjectIdentity
csnMIBGroups = _CsnMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2)
)

# Managed Objects groups

csnGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 1)
)
csnGlobalGroup.setObjects(
    ("CISCO-SWITCH-NETFLOW-MIB", "csnNetflowDirectionType")
)
if mibBuilder.loadTexts:
    csnGlobalGroup.setStatus("current")

csnUsageThreshNotifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 2)
)
csnUsageThreshNotifControlGroup.setObjects(
    ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshExceedNotifEnable")
)
if mibBuilder.loadTexts:
    csnUsageThreshNotifControlGroup.setStatus("current")

csnUsageThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 3)
)
csnUsageThreshGroup.setObjects(
      *(("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshold"),
        ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageInterval"))
)
if mibBuilder.loadTexts:
    csnUsageThreshGroup.setStatus("current")

csnUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 4)
)
csnUtilizationGroup.setObjects(
    ("CISCO-SWITCH-NETFLOW-MIB", "csnUtilization")
)
if mibBuilder.loadTexts:
    csnUtilizationGroup.setStatus("current")

csnNetflowTableSizeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 6)
)
csnNetflowTableSizeGroup.setObjects(
    ("CISCO-SWITCH-NETFLOW-MIB", "csnNetflowTableTotalEntries")
)
if mibBuilder.loadTexts:
    csnNetflowTableSizeGroup.setStatus("current")

csnSamplerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 7)
)
csnSamplerGroup.setObjects(
      *(("CISCO-SWITCH-NETFLOW-MIB", "csnSamplerTotal"),
        ("CISCO-SWITCH-NETFLOW-MIB", "csnSamplerAvailable"))
)
if mibBuilder.loadTexts:
    csnSamplerGroup.setStatus("current")


# Notification objects

csnUsageThreshExceededNotif = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 0, 1)
)
csnUsageThreshExceededNotif.setObjects(
      *(("ENTITY-MIB", "entPhysicalDescr"),
        ("CISCO-SWITCH-NETFLOW-MIB", "csnUtilization"),
        ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshold"),
        ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageInterval"))
)
if mibBuilder.loadTexts:
    csnUsageThreshExceededNotif.setStatus(
        "current"
    )


# Notifications groups

csnUsageThreshNotifGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 2, 5)
)
csnUsageThreshNotifGroup.setObjects(
    ("CISCO-SWITCH-NETFLOW-MIB", "csnUsageThreshExceededNotif")
)
if mibBuilder.loadTexts:
    csnUsageThreshNotifGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

csnMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 737, 2, 1, 1)
)
if mibBuilder.loadTexts:
    csnMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SWITCH-NETFLOW-MIB",
    **{"CsnNetflowDirectionTypes": CsnNetflowDirectionTypes,
       "ciscoSwitchNetflowMIB": ciscoSwitchNetflowMIB,
       "ciscoSwitchNetflowMIBNotifs": ciscoSwitchNetflowMIBNotifs,
       "csnUsageThreshExceededNotif": csnUsageThreshExceededNotif,
       "ciscoSwitchNetflowMIBObjects": ciscoSwitchNetflowMIBObjects,
       "csnAccounting": csnAccounting,
       "csnAccGlobal": csnAccGlobal,
       "csnNetflowDirectionType": csnNetflowDirectionType,
       "csnAccNotifControl": csnAccNotifControl,
       "csnUsageThreshExceedNotifEnable": csnUsageThreshExceedNotifEnable,
       "cshAccUsageThresh": cshAccUsageThresh,
       "csnUsageThreshTable": csnUsageThreshTable,
       "csnUsageThreshEntry": csnUsageThreshEntry,
       "csnUsageDirection": csnUsageDirection,
       "csnUsageThreshold": csnUsageThreshold,
       "csnUsageInterval": csnUsageInterval,
       "csnAccUtilization": csnAccUtilization,
       "csnUtilizationTable": csnUtilizationTable,
       "csnUtilizationEntry": csnUtilizationEntry,
       "csnUtilization": csnUtilization,
       "csnAccNetflowTableSize": csnAccNetflowTableSize,
       "csnNetflowTableSizeTable": csnNetflowTableSizeTable,
       "csnNetflowTableSizeEntry": csnNetflowTableSizeEntry,
       "csnNetflowTableTotalEntries": csnNetflowTableTotalEntries,
       "csnAccSampler": csnAccSampler,
       "csnSamplerTotal": csnSamplerTotal,
       "csnSamplerAvailable": csnSamplerAvailable,
       "ciscoSwitchNetflowMIBConform": ciscoSwitchNetflowMIBConform,
       "csnMIBCompliances": csnMIBCompliances,
       "csnMIBCompliance": csnMIBCompliance,
       "csnMIBGroups": csnMIBGroups,
       "csnGlobalGroup": csnGlobalGroup,
       "csnUsageThreshNotifControlGroup": csnUsageThreshNotifControlGroup,
       "csnUsageThreshGroup": csnUsageThreshGroup,
       "csnUtilizationGroup": csnUtilizationGroup,
       "csnUsageThreshNotifGroup": csnUsageThreshNotifGroup,
       "csnNetflowTableSizeGroup": csnNetflowTableSizeGroup,
       "csnSamplerGroup": csnSamplerGroup}
)
