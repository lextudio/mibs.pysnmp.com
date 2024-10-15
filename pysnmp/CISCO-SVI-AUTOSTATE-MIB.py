# SNMP MIB module (CISCO-SVI-AUTOSTATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CISCO-SVI-AUTOSTATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:09:02 2024
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

ciscoSVIAutostateMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 376)
)
ciscoSVIAutostateMIB.setRevisions(
        ("2004-04-06 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CiscoSVIAutostateMIBNotifs_ObjectIdentity = ObjectIdentity
ciscoSVIAutostateMIBNotifs = _CiscoSVIAutostateMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 0)
)
_CiscoSVIAutostateMIBObjects_ObjectIdentity = ObjectIdentity
ciscoSVIAutostateMIBObjects = _CiscoSVIAutostateMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 1)
)
_CsaGlobal_ObjectIdentity = ObjectIdentity
csaGlobal = _CsaGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1)
)
_CsaFeatureEnable_Type = TruthValue
_CsaFeatureEnable_Object = MibScalar
csaFeatureEnable = _CsaFeatureEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 1),
    _CsaFeatureEnable_Type()
)
csaFeatureEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csaFeatureEnable.setStatus("current")


class _CsaTrackedVlansLow_Type(OctetString):
    """Custom type csaTrackedVlansLow based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CsaTrackedVlansLow_Type.__name__ = "OctetString"
_CsaTrackedVlansLow_Object = MibScalar
csaTrackedVlansLow = _CsaTrackedVlansLow_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 2),
    _CsaTrackedVlansLow_Type()
)
csaTrackedVlansLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csaTrackedVlansLow.setStatus("current")


class _CsaTrackedVlansHigh_Type(OctetString):
    """Custom type csaTrackedVlansHigh based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_CsaTrackedVlansHigh_Type.__name__ = "OctetString"
_CsaTrackedVlansHigh_Object = MibScalar
csaTrackedVlansHigh = _CsaTrackedVlansHigh_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 3),
    _CsaTrackedVlansHigh_Type()
)
csaTrackedVlansHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csaTrackedVlansHigh.setStatus("current")
_CsaInterface_ObjectIdentity = ObjectIdentity
csaInterface = _CsaInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2)
)
_CsaIfConfigTable_Object = MibTable
csaIfConfigTable = _CsaIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1)
)
if mibBuilder.loadTexts:
    csaIfConfigTable.setStatus("current")
_CsaIfConfigEntry_Object = MibTableRow
csaIfConfigEntry = _CsaIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1)
)
csaIfConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    csaIfConfigEntry.setStatus("current")


class _CsaInterfaceMode_Type(Integer32):
    """Custom type csaInterfaceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("exclude", 2),
          ("normal", 1),
          ("track", 3))
    )


_CsaInterfaceMode_Type.__name__ = "Integer32"
_CsaInterfaceMode_Object = MibTableColumn
csaInterfaceMode = _CsaInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1, 1),
    _CsaInterfaceMode_Type()
)
csaInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    csaInterfaceMode.setStatus("current")
_CiscoSVIAutostateMIBConformance_ObjectIdentity = ObjectIdentity
ciscoSVIAutostateMIBConformance = _CiscoSVIAutostateMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 2)
)
_CsaMIBCompliances_ObjectIdentity = ObjectIdentity
csaMIBCompliances = _CsaMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1)
)
_CsaMIBGroups_ObjectIdentity = ObjectIdentity
csaMIBGroups = _CsaMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2)
)

# Managed Objects groups

ciscoSVIAutostateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 1)
)
ciscoSVIAutostateGroup.setObjects(
      *(("CISCO-SVI-AUTOSTATE-MIB", "csaFeatureEnable"),
        ("CISCO-SVI-AUTOSTATE-MIB", "csaInterfaceMode"))
)
if mibBuilder.loadTexts:
    ciscoSVIAutostateGroup.setStatus("current")

ciscoSVITrackedVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 2)
)
ciscoSVITrackedVlanGroup.setObjects(
      *(("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansLow"),
        ("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansHigh"))
)
if mibBuilder.loadTexts:
    ciscoSVITrackedVlanGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

csaMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1, 1)
)
if mibBuilder.loadTexts:
    csaMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-SVI-AUTOSTATE-MIB",
    **{"ciscoSVIAutostateMIB": ciscoSVIAutostateMIB,
       "ciscoSVIAutostateMIBNotifs": ciscoSVIAutostateMIBNotifs,
       "ciscoSVIAutostateMIBObjects": ciscoSVIAutostateMIBObjects,
       "csaGlobal": csaGlobal,
       "csaFeatureEnable": csaFeatureEnable,
       "csaTrackedVlansLow": csaTrackedVlansLow,
       "csaTrackedVlansHigh": csaTrackedVlansHigh,
       "csaInterface": csaInterface,
       "csaIfConfigTable": csaIfConfigTable,
       "csaIfConfigEntry": csaIfConfigEntry,
       "csaInterfaceMode": csaInterfaceMode,
       "ciscoSVIAutostateMIBConformance": ciscoSVIAutostateMIBConformance,
       "csaMIBCompliances": csaMIBCompliances,
       "csaMIBCompliance": csaMIBCompliance,
       "csaMIBGroups": csaMIBGroups,
       "ciscoSVIAutostateGroup": ciscoSVIAutostateGroup,
       "ciscoSVITrackedVlanGroup": ciscoSVITrackedVlanGroup}
)
