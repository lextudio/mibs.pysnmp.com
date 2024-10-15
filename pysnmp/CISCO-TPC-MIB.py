# SNMP MIB module (CISCO-TPC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-TPC-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:45 2024
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

(FcNameIdOrZero,) = mibBuilder.importSymbols(
    "CISCO-ST-TC",
    "FcNameIdOrZero")

(vsanIndex,) = mibBuilder.importSymbols(
    "CISCO-VSAN-MIB",
    "vsanIndex")

(PhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "PhysicalIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

ciscoTpcMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 460)
)
ciscoTpcMIB.setRevisions(
        ("2005-01-24 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class TpcTargetState(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("error", 3),
          ("initializing", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoTpcNotification_ObjectIdentity = ObjectIdentity
ciscoTpcNotification = _CiscoTpcNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 0)
)
_CiscoTpcObjects_ObjectIdentity = ObjectIdentity
ciscoTpcObjects = _CiscoTpcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1)
)
_CiscoTpcConfig_ObjectIdentity = ObjectIdentity
ciscoTpcConfig = _CiscoTpcConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1)
)
_CtpcModuleTable_Object = MibTable
ctpcModuleTable = _CtpcModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ctpcModuleTable.setStatus("current")
_CtpcModuleEntry_Object = MibTableRow
ctpcModuleEntry = _CtpcModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 1, 1)
)
ctpcModuleEntry.setIndexNames(
    (0, "CISCO-TPC-MIB", "ctpcModuleId"),
)
if mibBuilder.loadTexts:
    ctpcModuleEntry.setStatus("current")
_CtpcModuleId_Type = PhysicalIndex
_CtpcModuleId_Object = MibTableColumn
ctpcModuleId = _CtpcModuleId_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 1, 1, 1),
    _CtpcModuleId_Type()
)
ctpcModuleId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcModuleId.setStatus("current")
_CtpcVsanTable_Object = MibTable
ctpcVsanTable = _CtpcVsanTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ctpcVsanTable.setStatus("current")
_CtpcVsanEntry_Object = MibTableRow
ctpcVsanEntry = _CtpcVsanEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 2, 1)
)
ctpcVsanEntry.setIndexNames(
    (0, "CISCO-TPC-MIB", "ctpcModuleId"),
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
)
if mibBuilder.loadTexts:
    ctpcVsanEntry.setStatus("current")
_CtpcVsanRowStatus_Type = RowStatus
_CtpcVsanRowStatus_Object = MibTableColumn
ctpcVsanRowStatus = _CtpcVsanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 2, 1, 1),
    _CtpcVsanRowStatus_Type()
)
ctpcVsanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ctpcVsanRowStatus.setStatus("current")
_CtpcTargetTable_Object = MibTable
ctpcTargetTable = _CtpcTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 3)
)
if mibBuilder.loadTexts:
    ctpcTargetTable.setStatus("current")
_CtpcTargetEntry_Object = MibTableRow
ctpcTargetEntry = _CtpcTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 3, 1)
)
ctpcTargetEntry.setIndexNames(
    (0, "CISCO-TPC-MIB", "ctpcModuleId"),
    (0, "CISCO-VSAN-MIB", "vsanIndex"),
    (0, "CISCO-TPC-MIB", "ctpcTargetIndex"),
)
if mibBuilder.loadTexts:
    ctpcTargetEntry.setStatus("current")
_CtpcTargetIndex_Type = Unsigned32
_CtpcTargetIndex_Object = MibTableColumn
ctpcTargetIndex = _CtpcTargetIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 3, 1, 1),
    _CtpcTargetIndex_Type()
)
ctpcTargetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ctpcTargetIndex.setStatus("current")
_CtpcTargetNodeName_Type = FcNameIdOrZero
_CtpcTargetNodeName_Object = MibTableColumn
ctpcTargetNodeName = _CtpcTargetNodeName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 3, 1, 2),
    _CtpcTargetNodeName_Type()
)
ctpcTargetNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTargetNodeName.setStatus("current")
_CtpcTargetPortName_Type = FcNameIdOrZero
_CtpcTargetPortName_Object = MibTableColumn
ctpcTargetPortName = _CtpcTargetPortName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 3, 1, 3),
    _CtpcTargetPortName_Type()
)
ctpcTargetPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTargetPortName.setStatus("current")
_CtpcTargetState_Type = TpcTargetState
_CtpcTargetState_Object = MibTableColumn
ctpcTargetState = _CtpcTargetState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 3, 1, 4),
    _CtpcTargetState_Type()
)
ctpcTargetState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTargetState.setStatus("current")
_CtpcTargetNumXcopies_Type = Counter32
_CtpcTargetNumXcopies_Object = MibTableColumn
ctpcTargetNumXcopies = _CtpcTargetNumXcopies_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 3, 1, 5),
    _CtpcTargetNumXcopies_Type()
)
ctpcTargetNumXcopies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTargetNumXcopies.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTargetNumXcopies.setUnits("commands")
_CtpcTargetMinXcopy_Type = Gauge32
_CtpcTargetMinXcopy_Object = MibTableColumn
ctpcTargetMinXcopy = _CtpcTargetMinXcopy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 3, 1, 6),
    _CtpcTargetMinXcopy_Type()
)
ctpcTargetMinXcopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTargetMinXcopy.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTargetMinXcopy.setUnits("Kilobytes")
_CtpcTargetMaxXcopy_Type = Gauge32
_CtpcTargetMaxXcopy_Object = MibTableColumn
ctpcTargetMaxXcopy = _CtpcTargetMaxXcopy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 3, 1, 7),
    _CtpcTargetMaxXcopy_Type()
)
ctpcTargetMaxXcopy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTargetMaxXcopy.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTargetMaxXcopy.setUnits("Kilobytes")
_CtpcTargetAvgKbPerSec_Type = Gauge32
_CtpcTargetAvgKbPerSec_Object = MibTableColumn
ctpcTargetAvgKbPerSec = _CtpcTargetAvgKbPerSec_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 1, 1, 3, 1, 8),
    _CtpcTargetAvgKbPerSec_Type()
)
ctpcTargetAvgKbPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ctpcTargetAvgKbPerSec.setStatus("current")
if mibBuilder.loadTexts:
    ctpcTargetAvgKbPerSec.setUnits("Kilobytes/second")
_CiscoTpcMIBConformance_ObjectIdentity = ObjectIdentity
ciscoTpcMIBConformance = _CiscoTpcMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 2)
)
_CtpcMIBCompliances_ObjectIdentity = ObjectIdentity
ctpcMIBCompliances = _CtpcMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 2, 1)
)
_CtpcMIBGroups_ObjectIdentity = ObjectIdentity
ctpcMIBGroups = _CtpcMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 2, 2)
)

# Managed Objects groups

ctpcVsanTargetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 2, 2, 1)
)
ctpcVsanTargetGroup.setObjects(
      *(("CISCO-TPC-MIB", "ctpcModuleId"),
        ("CISCO-TPC-MIB", "ctpcVsanRowStatus"),
        ("CISCO-TPC-MIB", "ctpcTargetNodeName"),
        ("CISCO-TPC-MIB", "ctpcTargetPortName"),
        ("CISCO-TPC-MIB", "ctpcTargetState"),
        ("CISCO-TPC-MIB", "ctpcTargetNumXcopies"),
        ("CISCO-TPC-MIB", "ctpcTargetMinXcopy"),
        ("CISCO-TPC-MIB", "ctpcTargetMaxXcopy"),
        ("CISCO-TPC-MIB", "ctpcTargetAvgKbPerSec"))
)
if mibBuilder.loadTexts:
    ctpcVsanTargetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ctpcMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 460, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ctpcMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TPC-MIB",
    **{"TpcTargetState": TpcTargetState,
       "ciscoTpcMIB": ciscoTpcMIB,
       "ciscoTpcNotification": ciscoTpcNotification,
       "ciscoTpcObjects": ciscoTpcObjects,
       "ciscoTpcConfig": ciscoTpcConfig,
       "ctpcModuleTable": ctpcModuleTable,
       "ctpcModuleEntry": ctpcModuleEntry,
       "ctpcModuleId": ctpcModuleId,
       "ctpcVsanTable": ctpcVsanTable,
       "ctpcVsanEntry": ctpcVsanEntry,
       "ctpcVsanRowStatus": ctpcVsanRowStatus,
       "ctpcTargetTable": ctpcTargetTable,
       "ctpcTargetEntry": ctpcTargetEntry,
       "ctpcTargetIndex": ctpcTargetIndex,
       "ctpcTargetNodeName": ctpcTargetNodeName,
       "ctpcTargetPortName": ctpcTargetPortName,
       "ctpcTargetState": ctpcTargetState,
       "ctpcTargetNumXcopies": ctpcTargetNumXcopies,
       "ctpcTargetMinXcopy": ctpcTargetMinXcopy,
       "ctpcTargetMaxXcopy": ctpcTargetMaxXcopy,
       "ctpcTargetAvgKbPerSec": ctpcTargetAvgKbPerSec,
       "ciscoTpcMIBConformance": ciscoTpcMIBConformance,
       "ctpcMIBCompliances": ctpcMIBCompliances,
       "ctpcMIBCompliance": ctpcMIBCompliance,
       "ctpcMIBGroups": ctpcMIBGroups,
       "ctpcVsanTargetGroup": ctpcVsanTargetGroup}
)
