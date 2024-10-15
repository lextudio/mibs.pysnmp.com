# SNMP MIB module (CISCO-ATM-DUAL-PHY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ATM-DUAL-PHY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:50 2024
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "CISCO-TC",
    "InterfaceIndexOrZero")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 NotificationType,
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
    "NotificationType",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(TruthValue,) = mibBuilder.importSymbols(
    "SNMPv2-TC-v1",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoAtmDualPhyMIB_ObjectIdentity = ObjectIdentity
ciscoAtmDualPhyMIB = _CiscoAtmDualPhyMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 60)
)
_CiscoAtmDualPhyMIBObjects_ObjectIdentity = ObjectIdentity
ciscoAtmDualPhyMIBObjects = _CiscoAtmDualPhyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1)
)
_CadpStatistics_ObjectIdentity = ObjectIdentity
cadpStatistics = _CadpStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1)
)
_CadpStatTable_Object = MibTable
cadpStatTable = _CadpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cadpStatTable.setStatus("mandatory")
_CadpStatEntry_Object = MibTableRow
cadpStatEntry = _CadpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1)
)
cadpStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cadpStatEntry.setStatus("mandatory")
_CadpStatLossOfSignal_Type = TruthValue
_CadpStatLossOfSignal_Object = MibTableColumn
cadpStatLossOfSignal = _CadpStatLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 1),
    _CadpStatLossOfSignal_Type()
)
cadpStatLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatLossOfSignal.setStatus("mandatory")
_CadpStatFarEndReceiveFailure_Type = TruthValue
_CadpStatFarEndReceiveFailure_Object = MibTableColumn
cadpStatFarEndReceiveFailure = _CadpStatFarEndReceiveFailure_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 2),
    _CadpStatFarEndReceiveFailure_Type()
)
cadpStatFarEndReceiveFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatFarEndReceiveFailure.setStatus("mandatory")
_CadpStatActive_Type = TruthValue
_CadpStatActive_Object = MibTableColumn
cadpStatActive = _CadpStatActive_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 5),
    _CadpStatActive_Type()
)
cadpStatActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatActive.setStatus("mandatory")
_CadpStatSectionBIP8Errors_Type = Counter32
_CadpStatSectionBIP8Errors_Object = MibTableColumn
cadpStatSectionBIP8Errors = _CadpStatSectionBIP8Errors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 6),
    _CadpStatSectionBIP8Errors_Type()
)
cadpStatSectionBIP8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatSectionBIP8Errors.setStatus("mandatory")
_CadpStatLineBIP824Errors_Type = Counter32
_CadpStatLineBIP824Errors_Object = MibTableColumn
cadpStatLineBIP824Errors = _CadpStatLineBIP824Errors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 7),
    _CadpStatLineBIP824Errors_Type()
)
cadpStatLineBIP824Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatLineBIP824Errors.setStatus("mandatory")
_CadpStatLineFEBErrors_Type = Counter32
_CadpStatLineFEBErrors_Object = MibTableColumn
cadpStatLineFEBErrors = _CadpStatLineFEBErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 8),
    _CadpStatLineFEBErrors_Type()
)
cadpStatLineFEBErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatLineFEBErrors.setStatus("mandatory")
_CadpStatPathBIP8Errors_Type = Counter32
_CadpStatPathBIP8Errors_Object = MibTableColumn
cadpStatPathBIP8Errors = _CadpStatPathBIP8Errors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 9),
    _CadpStatPathBIP8Errors_Type()
)
cadpStatPathBIP8Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatPathBIP8Errors.setStatus("mandatory")
_CadpStatPathFEBErrors_Type = Counter32
_CadpStatPathFEBErrors_Object = MibTableColumn
cadpStatPathFEBErrors = _CadpStatPathFEBErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 10),
    _CadpStatPathFEBErrors_Type()
)
cadpStatPathFEBErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatPathFEBErrors.setStatus("mandatory")
_CadpStatCorrectableHCSErrors_Type = Counter32
_CadpStatCorrectableHCSErrors_Object = MibTableColumn
cadpStatCorrectableHCSErrors = _CadpStatCorrectableHCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 11),
    _CadpStatCorrectableHCSErrors_Type()
)
cadpStatCorrectableHCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatCorrectableHCSErrors.setStatus("mandatory")
_CadpStatUncorrectableHCSErrors_Type = Counter32
_CadpStatUncorrectableHCSErrors_Object = MibTableColumn
cadpStatUncorrectableHCSErrors = _CadpStatUncorrectableHCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 1, 1, 12),
    _CadpStatUncorrectableHCSErrors_Type()
)
cadpStatUncorrectableHCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatUncorrectableHCSErrors.setStatus("mandatory")
_CadpStatOperActivePhy_Type = InterfaceIndexOrZero
_CadpStatOperActivePhy_Object = MibScalar
cadpStatOperActivePhy = _CadpStatOperActivePhy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 2),
    _CadpStatOperActivePhy_Type()
)
cadpStatOperActivePhy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadpStatOperActivePhy.setStatus("mandatory")
_CadpStatAdminActivePhy_Type = InterfaceIndex
_CadpStatAdminActivePhy_Object = MibScalar
cadpStatAdminActivePhy = _CadpStatAdminActivePhy_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 1, 1, 3),
    _CadpStatAdminActivePhy_Type()
)
cadpStatAdminActivePhy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cadpStatAdminActivePhy.setStatus("mandatory")
_CiscoAtmDualPhyMIBTrapPrefix_ObjectIdentity = ObjectIdentity
ciscoAtmDualPhyMIBTrapPrefix = _CiscoAtmDualPhyMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 2)
)
_CiscoAtmDualPhyMIBTraps_ObjectIdentity = ObjectIdentity
ciscoAtmDualPhyMIBTraps = _CiscoAtmDualPhyMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 2, 0)
)
_CiscoAtmDualPhyMIBConformance_ObjectIdentity = ObjectIdentity
ciscoAtmDualPhyMIBConformance = _CiscoAtmDualPhyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 3)
)
_CiscoAtmDualPhyMIBCompliances_ObjectIdentity = ObjectIdentity
ciscoAtmDualPhyMIBCompliances = _CiscoAtmDualPhyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 3, 1)
)
_CiscoAtmDualPhyMIBCompliance_ObjectIdentity = ObjectIdentity
ciscoAtmDualPhyMIBCompliance = _CiscoAtmDualPhyMIBCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 3, 1, 1)
)
_CiscoAtmDualPhyMIBGroups_ObjectIdentity = ObjectIdentity
ciscoAtmDualPhyMIBGroups = _CiscoAtmDualPhyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 3, 2)
)
_CiscoAtmDualPhyMIBGroup_ObjectIdentity = ObjectIdentity
ciscoAtmDualPhyMIBGroup = _CiscoAtmDualPhyMIBGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 3, 2, 1)
)

# Managed Objects groups


# Notification objects

ciscoAtmDualPhyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 9, 9, 60, 2, 0, 1)
)
ciscoAtmDualPhyChange.setObjects(
    ("CISCO-ATM-DUAL-PHY-MIB", "cadpStatOperActivePhy")
)
if mibBuilder.loadTexts:
    ciscoAtmDualPhyChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ATM-DUAL-PHY-MIB",
    **{"ciscoAtmDualPhyMIB": ciscoAtmDualPhyMIB,
       "ciscoAtmDualPhyMIBObjects": ciscoAtmDualPhyMIBObjects,
       "cadpStatistics": cadpStatistics,
       "cadpStatTable": cadpStatTable,
       "cadpStatEntry": cadpStatEntry,
       "cadpStatLossOfSignal": cadpStatLossOfSignal,
       "cadpStatFarEndReceiveFailure": cadpStatFarEndReceiveFailure,
       "cadpStatActive": cadpStatActive,
       "cadpStatSectionBIP8Errors": cadpStatSectionBIP8Errors,
       "cadpStatLineBIP824Errors": cadpStatLineBIP824Errors,
       "cadpStatLineFEBErrors": cadpStatLineFEBErrors,
       "cadpStatPathBIP8Errors": cadpStatPathBIP8Errors,
       "cadpStatPathFEBErrors": cadpStatPathFEBErrors,
       "cadpStatCorrectableHCSErrors": cadpStatCorrectableHCSErrors,
       "cadpStatUncorrectableHCSErrors": cadpStatUncorrectableHCSErrors,
       "cadpStatOperActivePhy": cadpStatOperActivePhy,
       "cadpStatAdminActivePhy": cadpStatAdminActivePhy,
       "ciscoAtmDualPhyMIBTrapPrefix": ciscoAtmDualPhyMIBTrapPrefix,
       "ciscoAtmDualPhyMIBTraps": ciscoAtmDualPhyMIBTraps,
       "ciscoAtmDualPhyChange": ciscoAtmDualPhyChange,
       "ciscoAtmDualPhyMIBConformance": ciscoAtmDualPhyMIBConformance,
       "ciscoAtmDualPhyMIBCompliances": ciscoAtmDualPhyMIBCompliances,
       "ciscoAtmDualPhyMIBCompliance": ciscoAtmDualPhyMIBCompliance,
       "ciscoAtmDualPhyMIBGroups": ciscoAtmDualPhyMIBGroups,
       "ciscoAtmDualPhyMIBGroup": ciscoAtmDualPhyMIBGroup}
)
