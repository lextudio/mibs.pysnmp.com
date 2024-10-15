# SNMP MIB module (CERENT-IF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CERENT-IF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:54:26 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

cerentIfExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 1, 10, 140)
)
cerentIfExtMIB.setRevisions(
        ("2005-11-14 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CerentIfExtMIBObjects_ObjectIdentity = ObjectIdentity
cerentIfExtMIBObjects = _CerentIfExtMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100)
)
_CerentIfExtTable_Object = MibTable
cerentIfExtTable = _CerentIfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100, 10)
)
if mibBuilder.loadTexts:
    cerentIfExtTable.setStatus("current")
_CerentIfExtEntry_Object = MibTableRow
cerentIfExtEntry = _CerentIfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1)
)
cerentIfExtEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    cerentIfExtEntry.setStatus("current")


class _CerentIfExtPreServiceAlarmSuppression_Type(TruthValue):
    """Custom type cerentIfExtPreServiceAlarmSuppression based on TruthValue"""


_CerentIfExtPreServiceAlarmSuppression_Object = MibTableColumn
cerentIfExtPreServiceAlarmSuppression = _CerentIfExtPreServiceAlarmSuppression_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 10),
    _CerentIfExtPreServiceAlarmSuppression_Type()
)
cerentIfExtPreServiceAlarmSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerentIfExtPreServiceAlarmSuppression.setStatus("current")


class _CerentIfExtConfiguredSoakTime_Type(Integer32):
    """Custom type cerentIfExtConfiguredSoakTime based on Integer32"""
    defaultValue = 480


_CerentIfExtConfiguredSoakTime_Object = MibTableColumn
cerentIfExtConfiguredSoakTime = _CerentIfExtConfiguredSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 20),
    _CerentIfExtConfiguredSoakTime_Type()
)
cerentIfExtConfiguredSoakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cerentIfExtConfiguredSoakTime.setStatus("current")
if mibBuilder.loadTexts:
    cerentIfExtConfiguredSoakTime.setUnits("minutes")
_CerentIfExtCurrentSoakTime_Type = Integer32
_CerentIfExtCurrentSoakTime_Object = MibTableColumn
cerentIfExtCurrentSoakTime = _CerentIfExtCurrentSoakTime_Object(
    (1, 3, 6, 1, 4, 1, 3607, 2, 100, 10, 1, 30),
    _CerentIfExtCurrentSoakTime_Type()
)
cerentIfExtCurrentSoakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cerentIfExtCurrentSoakTime.setStatus("current")
if mibBuilder.loadTexts:
    cerentIfExtCurrentSoakTime.setUnits("minutes")
_CerentIfExtMIBConformance_ObjectIdentity = ObjectIdentity
cerentIfExtMIBConformance = _CerentIfExtMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 90)
)
_CerentIfExtMIBCompliances_ObjectIdentity = ObjectIdentity
cerentIfExtMIBCompliances = _CerentIfExtMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 90, 1)
)
_CerentIfExtMIBGroups_ObjectIdentity = ObjectIdentity
cerentIfExtMIBGroups = _CerentIfExtMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3607, 5, 90, 2)
)

# Managed Objects groups

cerentIfExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3607, 5, 90, 2, 10)
)
cerentIfExtGroup.setObjects(
      *(("CERENT-IF-EXT-MIB", "cerentIfExtPreServiceAlarmSuppression"),
        ("CERENT-IF-EXT-MIB", "cerentIfExtConfiguredSoakTime"),
        ("CERENT-IF-EXT-MIB", "cerentIfExtCurrentSoakTime"))
)
if mibBuilder.loadTexts:
    cerentIfExtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cerentIfExtMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3607, 5, 90, 1, 1)
)
if mibBuilder.loadTexts:
    cerentIfExtMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CERENT-IF-EXT-MIB",
    **{"cerentIfExtMIB": cerentIfExtMIB,
       "cerentIfExtMIBObjects": cerentIfExtMIBObjects,
       "cerentIfExtTable": cerentIfExtTable,
       "cerentIfExtEntry": cerentIfExtEntry,
       "cerentIfExtPreServiceAlarmSuppression": cerentIfExtPreServiceAlarmSuppression,
       "cerentIfExtConfiguredSoakTime": cerentIfExtConfiguredSoakTime,
       "cerentIfExtCurrentSoakTime": cerentIfExtCurrentSoakTime,
       "cerentIfExtMIBConformance": cerentIfExtMIBConformance,
       "cerentIfExtMIBCompliances": cerentIfExtMIBCompliances,
       "cerentIfExtMIBCompliance": cerentIfExtMIBCompliance,
       "cerentIfExtMIBGroups": cerentIfExtMIBGroups,
       "cerentIfExtGroup": cerentIfExtGroup}
)
