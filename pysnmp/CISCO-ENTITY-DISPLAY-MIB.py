# SNMP MIB module (CISCO-ENTITY-DISPLAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-ENTITY-DISPLAY-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:59:34 2024
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

ciscoEntityDisplayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 344)
)
ciscoEntityDisplayMIB.setRevisions(
        ("2009-10-05 00:00",
         "2003-03-20 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class CDisplayType(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("alphanumeric", 2),
          ("led", 1))
    )



class CDisplayColor(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("amber", 6),
          ("blue", 7),
          ("green", 4),
          ("greenAndAmber", 8),
          ("red", 3),
          ("unknown", 1),
          ("white", 2),
          ("yellow", 5))
    )



class CDisplayState(Integer32, TextualConvention):
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
        *(("blinking", 4),
          ("off", 2),
          ("on", 3),
          ("unknown", 1))
    )



# MIB Managed Objects in the order of their OIDs

_CiscoEntityDisplayMIBObjects_ObjectIdentity = ObjectIdentity
ciscoEntityDisplayMIBObjects = _CiscoEntityDisplayMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1)
)
_CeDisplayTable_Object = MibTable
ceDisplayTable = _CeDisplayTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1)
)
if mibBuilder.loadTexts:
    ceDisplayTable.setStatus("current")
_CeDisplayEntry_Object = MibTableRow
ceDisplayEntry = _CeDisplayEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1)
)
ceDisplayEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-DISPLAY-MIB", "ceDisplayIndex"),
)
if mibBuilder.loadTexts:
    ceDisplayEntry.setStatus("current")


class _CeDisplayIndex_Type(Unsigned32):
    """Custom type ceDisplayIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_CeDisplayIndex_Type.__name__ = "Unsigned32"
_CeDisplayIndex_Object = MibTableColumn
ceDisplayIndex = _CeDisplayIndex_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 1),
    _CeDisplayIndex_Type()
)
ceDisplayIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ceDisplayIndex.setStatus("current")
_CeDisplayType_Type = CDisplayType
_CeDisplayType_Object = MibTableColumn
ceDisplayType = _CeDisplayType_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 2),
    _CeDisplayType_Type()
)
ceDisplayType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDisplayType.setStatus("current")
_CeDisplayName_Type = SnmpAdminString
_CeDisplayName_Object = MibTableColumn
ceDisplayName = _CeDisplayName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 3),
    _CeDisplayName_Type()
)
ceDisplayName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDisplayName.setStatus("current")
_CeDisplayState_Type = CDisplayState
_CeDisplayState_Object = MibTableColumn
ceDisplayState = _CeDisplayState_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 4),
    _CeDisplayState_Type()
)
ceDisplayState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDisplayState.setStatus("current")
_CeDisplayColor_Type = CDisplayColor
_CeDisplayColor_Object = MibTableColumn
ceDisplayColor = _CeDisplayColor_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 5),
    _CeDisplayColor_Type()
)
ceDisplayColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDisplayColor.setStatus("current")
_CeDisplayText_Type = SnmpAdminString
_CeDisplayText_Object = MibTableColumn
ceDisplayText = _CeDisplayText_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 1, 1, 6),
    _CeDisplayText_Type()
)
ceDisplayText.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ceDisplayText.setStatus("current")
_CeDisplayBeaconTable_Object = MibTable
ceDisplayBeaconTable = _CeDisplayBeaconTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2)
)
if mibBuilder.loadTexts:
    ceDisplayBeaconTable.setStatus("current")
_CeDisplayBeaconEntry_Object = MibTableRow
ceDisplayBeaconEntry = _CeDisplayBeaconEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2, 1)
)
ceDisplayBeaconEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "CISCO-ENTITY-DISPLAY-MIB", "ceDisplayIndex"),
)
if mibBuilder.loadTexts:
    ceDisplayBeaconEntry.setStatus("current")
_CeDisplayBeaconEnabled_Type = TruthValue
_CeDisplayBeaconEnabled_Object = MibTableColumn
ceDisplayBeaconEnabled = _CeDisplayBeaconEnabled_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 1, 2, 1, 1),
    _CeDisplayBeaconEnabled_Type()
)
ceDisplayBeaconEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ceDisplayBeaconEnabled.setStatus("current")
_CeDisplayMIBConformance_ObjectIdentity = ObjectIdentity
ceDisplayMIBConformance = _CeDisplayMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 2)
)
_CeDisplayMIBCompliances_ObjectIdentity = ObjectIdentity
ceDisplayMIBCompliances = _CeDisplayMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1)
)
_CeDisplayMIBGroups_ObjectIdentity = ObjectIdentity
ceDisplayMIBGroups = _CeDisplayMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2)
)

# Managed Objects groups

ceDisplayGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 1)
)
ceDisplayGroup.setObjects(
      *(("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayType"),
        ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayName"),
        ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayState"))
)
if mibBuilder.loadTexts:
    ceDisplayGroup.setStatus("current")

ceDisplayLEDGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 2)
)
ceDisplayLEDGroup.setObjects(
    ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayColor")
)
if mibBuilder.loadTexts:
    ceDisplayLEDGroup.setStatus("current")

ceDisplayAlphaNumericGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 3)
)
ceDisplayAlphaNumericGroup.setObjects(
    ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayText")
)
if mibBuilder.loadTexts:
    ceDisplayAlphaNumericGroup.setStatus("current")

ceDisplayBeaconGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 2, 4)
)
ceDisplayBeaconGroup.setObjects(
    ("CISCO-ENTITY-DISPLAY-MIB", "ceDisplayBeaconEnabled")
)
if mibBuilder.loadTexts:
    ceDisplayBeaconGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ceDisplayMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ceDisplayMIBCompliance.setStatus(
        "deprecated"
    )

ceDisplayMIBCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 344, 2, 1, 2)
)
if mibBuilder.loadTexts:
    ceDisplayMIBCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-ENTITY-DISPLAY-MIB",
    **{"CDisplayType": CDisplayType,
       "CDisplayColor": CDisplayColor,
       "CDisplayState": CDisplayState,
       "ciscoEntityDisplayMIB": ciscoEntityDisplayMIB,
       "ciscoEntityDisplayMIBObjects": ciscoEntityDisplayMIBObjects,
       "ceDisplayTable": ceDisplayTable,
       "ceDisplayEntry": ceDisplayEntry,
       "ceDisplayIndex": ceDisplayIndex,
       "ceDisplayType": ceDisplayType,
       "ceDisplayName": ceDisplayName,
       "ceDisplayState": ceDisplayState,
       "ceDisplayColor": ceDisplayColor,
       "ceDisplayText": ceDisplayText,
       "ceDisplayBeaconTable": ceDisplayBeaconTable,
       "ceDisplayBeaconEntry": ceDisplayBeaconEntry,
       "ceDisplayBeaconEnabled": ceDisplayBeaconEnabled,
       "ceDisplayMIBConformance": ceDisplayMIBConformance,
       "ceDisplayMIBCompliances": ceDisplayMIBCompliances,
       "ceDisplayMIBCompliance": ceDisplayMIBCompliance,
       "ceDisplayMIBCompliance2": ceDisplayMIBCompliance2,
       "ceDisplayMIBGroups": ceDisplayMIBGroups,
       "ceDisplayGroup": ceDisplayGroup,
       "ceDisplayLEDGroup": ceDisplayLEDGroup,
       "ceDisplayAlphaNumericGroup": ceDisplayAlphaNumericGroup,
       "ceDisplayBeaconGroup": ceDisplayBeaconGroup}
)
