# SNMP MIB module (CERENT-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CERENT-ENVMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:21 2024
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

(cerentGeneric,
 cerentModules,
 cerentRequirements) = mibBuilder.importSymbols(
    "CERENT-GLOBAL-REGISTRY",
    "cerentGeneric",
    "cerentModules",
    "cerentRequirements")

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

cerentEnvMonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10, 120)
)
cerentEnvMonMIB.setRevisions(
        ("2004-01-27 14:51",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CerentEnvMonObjects_ObjectIdentity = ObjectIdentity
cerentEnvMonObjects = _CerentEnvMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80)
)
if mibBuilder.loadTexts:
    cerentEnvMonObjects.setStatus("current")
_CerentEnvMonVoltageStatsTable_Object = MibTable
cerentEnvMonVoltageStatsTable = _CerentEnvMonVoltageStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 10)
)
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsTable.setStatus("current")
_CerentEnvMonVoltageStatsEntry_Object = MibTableRow
cerentEnvMonVoltageStatsEntry = _CerentEnvMonVoltageStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 10, 1)
)
cerentEnvMonVoltageStatsEntry.setIndexNames(
    (0, "CERENT-ENVMON-MIB", "cerentEnvMonVoltageStatsIndex"),
)
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsEntry.setStatus("current")


class _CerentEnvMonVoltageStatsIndex_Type(Integer32):
    """Custom type cerentEnvMonVoltageStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CerentEnvMonVoltageStatsIndex_Type.__name__ = "Integer32"
_CerentEnvMonVoltageStatsIndex_Object = MibTableColumn
cerentEnvMonVoltageStatsIndex = _CerentEnvMonVoltageStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 10, 1, 10),
    _CerentEnvMonVoltageStatsIndex_Type()
)
cerentEnvMonVoltageStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsIndex.setStatus("current")
_CerentEnvMonVoltageStatsDescr_Type = DisplayString
_CerentEnvMonVoltageStatsDescr_Object = MibTableColumn
cerentEnvMonVoltageStatsDescr = _CerentEnvMonVoltageStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 10, 1, 20),
    _CerentEnvMonVoltageStatsDescr_Type()
)
cerentEnvMonVoltageStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsDescr.setStatus("current")
_CerentEnvMonVoltageStatsCurrentValue_Type = Integer32
_CerentEnvMonVoltageStatsCurrentValue_Object = MibTableColumn
cerentEnvMonVoltageStatsCurrentValue = _CerentEnvMonVoltageStatsCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 10, 1, 30),
    _CerentEnvMonVoltageStatsCurrentValue_Type()
)
cerentEnvMonVoltageStatsCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsCurrentValue.setStatus("current")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsCurrentValue.setUnits("millivolts")
_CerentEnvMonVoltageStatsThresholdVeryHigh_Type = Integer32
_CerentEnvMonVoltageStatsThresholdVeryHigh_Object = MibTableColumn
cerentEnvMonVoltageStatsThresholdVeryHigh = _CerentEnvMonVoltageStatsThresholdVeryHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 10, 1, 40),
    _CerentEnvMonVoltageStatsThresholdVeryHigh_Type()
)
cerentEnvMonVoltageStatsThresholdVeryHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsThresholdVeryHigh.setStatus("current")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsThresholdVeryHigh.setUnits("millivolts")
_CerentEnvMonVoltageStatsThresholdHigh_Type = Integer32
_CerentEnvMonVoltageStatsThresholdHigh_Object = MibTableColumn
cerentEnvMonVoltageStatsThresholdHigh = _CerentEnvMonVoltageStatsThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 10, 1, 50),
    _CerentEnvMonVoltageStatsThresholdHigh_Type()
)
cerentEnvMonVoltageStatsThresholdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsThresholdHigh.setUnits("millivolts")
_CerentEnvMonVoltageStatsThresholdLow_Type = Integer32
_CerentEnvMonVoltageStatsThresholdLow_Object = MibTableColumn
cerentEnvMonVoltageStatsThresholdLow = _CerentEnvMonVoltageStatsThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 10, 1, 60),
    _CerentEnvMonVoltageStatsThresholdLow_Type()
)
cerentEnvMonVoltageStatsThresholdLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsThresholdLow.setStatus("current")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsThresholdLow.setUnits("millivolts")
_CerentEnvMonVoltageStatsThresholdVeryLow_Type = Integer32
_CerentEnvMonVoltageStatsThresholdVeryLow_Object = MibTableColumn
cerentEnvMonVoltageStatsThresholdVeryLow = _CerentEnvMonVoltageStatsThresholdVeryLow_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 10, 1, 70),
    _CerentEnvMonVoltageStatsThresholdVeryLow_Type()
)
cerentEnvMonVoltageStatsThresholdVeryLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsThresholdVeryLow.setStatus("current")
if mibBuilder.loadTexts:
    cerentEnvMonVoltageStatsThresholdVeryLow.setUnits("millivolts")
_CerentEnvMonTemperatureStatsTable_Object = MibTable
cerentEnvMonTemperatureStatsTable = _CerentEnvMonTemperatureStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 20)
)
if mibBuilder.loadTexts:
    cerentEnvMonTemperatureStatsTable.setStatus("current")
_CerentEnvMonTemperatureStatsEntry_Object = MibTableRow
cerentEnvMonTemperatureStatsEntry = _CerentEnvMonTemperatureStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 20, 1)
)
cerentEnvMonTemperatureStatsEntry.setIndexNames(
    (0, "CERENT-ENVMON-MIB", "cerentEnvMonTemperatureStatsIndex"),
)
if mibBuilder.loadTexts:
    cerentEnvMonTemperatureStatsEntry.setStatus("current")


class _CerentEnvMonTemperatureStatsIndex_Type(Integer32):
    """Custom type cerentEnvMonTemperatureStatsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CerentEnvMonTemperatureStatsIndex_Type.__name__ = "Integer32"
_CerentEnvMonTemperatureStatsIndex_Object = MibTableColumn
cerentEnvMonTemperatureStatsIndex = _CerentEnvMonTemperatureStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 20, 1, 10),
    _CerentEnvMonTemperatureStatsIndex_Type()
)
cerentEnvMonTemperatureStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cerentEnvMonTemperatureStatsIndex.setStatus("current")
_CerentEnvMonTemperatureStatsDescr_Type = DisplayString
_CerentEnvMonTemperatureStatsDescr_Object = MibTableColumn
cerentEnvMonTemperatureStatsDescr = _CerentEnvMonTemperatureStatsDescr_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 20, 1, 20),
    _CerentEnvMonTemperatureStatsDescr_Type()
)
cerentEnvMonTemperatureStatsDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentEnvMonTemperatureStatsDescr.setStatus("current")
_CerentEnvMonTemperatureStatsCurrentValue_Type = Gauge32
_CerentEnvMonTemperatureStatsCurrentValue_Object = MibTableColumn
cerentEnvMonTemperatureStatsCurrentValue = _CerentEnvMonTemperatureStatsCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 20, 1, 30),
    _CerentEnvMonTemperatureStatsCurrentValue_Type()
)
cerentEnvMonTemperatureStatsCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentEnvMonTemperatureStatsCurrentValue.setStatus("current")
if mibBuilder.loadTexts:
    cerentEnvMonTemperatureStatsCurrentValue.setUnits("Degree Celsius")
_CerentEnvMonTemperatureStatsThresholdHigh_Type = Gauge32
_CerentEnvMonTemperatureStatsThresholdHigh_Object = MibTableColumn
cerentEnvMonTemperatureStatsThresholdHigh = _CerentEnvMonTemperatureStatsThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 80, 20, 1, 40),
    _CerentEnvMonTemperatureStatsThresholdHigh_Type()
)
cerentEnvMonTemperatureStatsThresholdHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentEnvMonTemperatureStatsThresholdHigh.setStatus("current")
if mibBuilder.loadTexts:
    cerentEnvMonTemperatureStatsThresholdHigh.setUnits("Degree Celsius")
_CerentEnvMonMibConformance_ObjectIdentity = ObjectIdentity
cerentEnvMonMibConformance = _CerentEnvMonMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 70)
)
if mibBuilder.loadTexts:
    cerentEnvMonMibConformance.setStatus("current")
_CerentEnvMonMibCompliance_ObjectIdentity = ObjectIdentity
cerentEnvMonMibCompliance = _CerentEnvMonMibCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 70, 10)
)
if mibBuilder.loadTexts:
    cerentEnvMonMibCompliance.setStatus("current")
_CerentEnvMonMibGroups_ObjectIdentity = ObjectIdentity
cerentEnvMonMibGroups = _CerentEnvMonMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 70, 20)
)
if mibBuilder.loadTexts:
    cerentEnvMonMibGroups.setStatus("current")

# Managed Objects groups

cerentEnvMonMibObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 70, 20, 10)
)
cerentEnvMonMibObjectsGroup.setObjects(
      *(("CERENT-ENVMON-MIB", "cerentEnvMonVoltageStatsDescr"),
        ("CERENT-ENVMON-MIB", "cerentEnvMonVoltageStatsCurrentValue"),
        ("CERENT-ENVMON-MIB", "cerentEnvMonVoltageStatsThresholdVeryHigh"),
        ("CERENT-ENVMON-MIB", "cerentEnvMonVoltageStatsThresholdHigh"),
        ("CERENT-ENVMON-MIB", "cerentEnvMonVoltageStatsThresholdLow"),
        ("CERENT-ENVMON-MIB", "cerentEnvMonVoltageStatsThresholdVeryLow"),
        ("CERENT-ENVMON-MIB", "cerentEnvMonTemperatureStatsDescr"),
        ("CERENT-ENVMON-MIB", "cerentEnvMonTemperatureStatsCurrentValue"),
        ("CERENT-ENVMON-MIB", "cerentEnvMonTemperatureStatsThresholdHigh"))
)
if mibBuilder.loadTexts:
    cerentEnvMonMibObjectsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cerentEnvMonMibBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3607, 5, 70, 10, 10)
)
if mibBuilder.loadTexts:
    cerentEnvMonMibBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERENT-ENVMON-MIB",
    **{"cerentEnvMonMIB": cerentEnvMonMIB,
       "cerentEnvMonObjects": cerentEnvMonObjects,
       "cerentEnvMonVoltageStatsTable": cerentEnvMonVoltageStatsTable,
       "cerentEnvMonVoltageStatsEntry": cerentEnvMonVoltageStatsEntry,
       "cerentEnvMonVoltageStatsIndex": cerentEnvMonVoltageStatsIndex,
       "cerentEnvMonVoltageStatsDescr": cerentEnvMonVoltageStatsDescr,
       "cerentEnvMonVoltageStatsCurrentValue": cerentEnvMonVoltageStatsCurrentValue,
       "cerentEnvMonVoltageStatsThresholdVeryHigh": cerentEnvMonVoltageStatsThresholdVeryHigh,
       "cerentEnvMonVoltageStatsThresholdHigh": cerentEnvMonVoltageStatsThresholdHigh,
       "cerentEnvMonVoltageStatsThresholdLow": cerentEnvMonVoltageStatsThresholdLow,
       "cerentEnvMonVoltageStatsThresholdVeryLow": cerentEnvMonVoltageStatsThresholdVeryLow,
       "cerentEnvMonTemperatureStatsTable": cerentEnvMonTemperatureStatsTable,
       "cerentEnvMonTemperatureStatsEntry": cerentEnvMonTemperatureStatsEntry,
       "cerentEnvMonTemperatureStatsIndex": cerentEnvMonTemperatureStatsIndex,
       "cerentEnvMonTemperatureStatsDescr": cerentEnvMonTemperatureStatsDescr,
       "cerentEnvMonTemperatureStatsCurrentValue": cerentEnvMonTemperatureStatsCurrentValue,
       "cerentEnvMonTemperatureStatsThresholdHigh": cerentEnvMonTemperatureStatsThresholdHigh,
       "cerentEnvMonMibConformance": cerentEnvMonMibConformance,
       "cerentEnvMonMibCompliance": cerentEnvMonMibCompliance,
       "cerentEnvMonMibBasicCompliance": cerentEnvMonMibBasicCompliance,
       "cerentEnvMonMibGroups": cerentEnvMonMibGroups,
       "cerentEnvMonMibObjectsGroup": cerentEnvMonMibObjectsGroup}
)
