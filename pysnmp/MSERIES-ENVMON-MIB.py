# SNMP MIB module (MSERIES-ENVMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MSERIES-ENVMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:55 2024
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

(mseries,) = mibBuilder.importSymbols(
    "MSERIES-MIB",
    "mseries")

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

smartEnvMon = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4)
)
smartEnvMon.setRevisions(
        ("2014-02-15 10:34",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SmartEnvMonObjects_ObjectIdentity = ObjectIdentity
smartEnvMonObjects = _SmartEnvMonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 1)
)
_SmartEnvMonTemperatureTable_Object = MibTable
smartEnvMonTemperatureTable = _SmartEnvMonTemperatureTable_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1)
)
if mibBuilder.loadTexts:
    smartEnvMonTemperatureTable.setStatus("current")
_SmartEnvMonTemperatureEntry_Object = MibTableRow
smartEnvMonTemperatureEntry = _SmartEnvMonTemperatureEntry_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1)
)
smartEnvMonTemperatureEntry.setIndexNames(
    (0, "MSERIES-ENVMON-MIB", "smartEnvMonTemperatureIndex"),
)
if mibBuilder.loadTexts:
    smartEnvMonTemperatureEntry.setStatus("current")


class _SmartEnvMonTemperatureIndex_Type(Unsigned32):
    """Custom type smartEnvMonTemperatureIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SmartEnvMonTemperatureIndex_Type.__name__ = "Unsigned32"
_SmartEnvMonTemperatureIndex_Object = MibTableColumn
smartEnvMonTemperatureIndex = _SmartEnvMonTemperatureIndex_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 1),
    _SmartEnvMonTemperatureIndex_Type()
)
smartEnvMonTemperatureIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartEnvMonTemperatureIndex.setStatus("current")
_SmartEnvMonTemperatureDescr_Type = DisplayString
_SmartEnvMonTemperatureDescr_Object = MibTableColumn
smartEnvMonTemperatureDescr = _SmartEnvMonTemperatureDescr_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 2),
    _SmartEnvMonTemperatureDescr_Type()
)
smartEnvMonTemperatureDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartEnvMonTemperatureDescr.setStatus("current")
_SmartEnvMonTemperatureValue_Type = Integer32
_SmartEnvMonTemperatureValue_Object = MibTableColumn
smartEnvMonTemperatureValue = _SmartEnvMonTemperatureValue_Object(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 1, 1, 1, 3),
    _SmartEnvMonTemperatureValue_Type()
)
smartEnvMonTemperatureValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smartEnvMonTemperatureValue.setStatus("current")
if mibBuilder.loadTexts:
    smartEnvMonTemperatureValue.setUnits("degrees Celsius")
_SmartEnvMonMIBConformance_ObjectIdentity = ObjectIdentity
smartEnvMonMIBConformance = _SmartEnvMonMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 2)
)
_SmartEnvMonGroups_ObjectIdentity = ObjectIdentity
smartEnvMonGroups = _SmartEnvMonGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 1)
)
_SmartEnvMonCompliances_ObjectIdentity = ObjectIdentity
smartEnvMonCompliances = _SmartEnvMonCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 2)
)

# Managed Objects groups

smartEnvMonTemperatureGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 1, 1)
)
smartEnvMonTemperatureGroupV1.setObjects(
      *(("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureIndex"),
        ("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureDescr"),
        ("MSERIES-ENVMON-MIB", "smartEnvMonTemperatureValue"))
)
if mibBuilder.loadTexts:
    smartEnvMonTemperatureGroupV1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

smartEnvMonBasicComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 30826, 1, 4, 2, 2, 1)
)
if mibBuilder.loadTexts:
    smartEnvMonBasicComplV1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MSERIES-ENVMON-MIB",
    **{"smartEnvMon": smartEnvMon,
       "smartEnvMonObjects": smartEnvMonObjects,
       "smartEnvMonTemperatureTable": smartEnvMonTemperatureTable,
       "smartEnvMonTemperatureEntry": smartEnvMonTemperatureEntry,
       "smartEnvMonTemperatureIndex": smartEnvMonTemperatureIndex,
       "smartEnvMonTemperatureDescr": smartEnvMonTemperatureDescr,
       "smartEnvMonTemperatureValue": smartEnvMonTemperatureValue,
       "smartEnvMonMIBConformance": smartEnvMonMIBConformance,
       "smartEnvMonGroups": smartEnvMonGroups,
       "smartEnvMonTemperatureGroupV1": smartEnvMonTemperatureGroupV1,
       "smartEnvMonCompliances": smartEnvMonCompliances,
       "smartEnvMonBasicComplV1": smartEnvMonBasicComplV1}
)
