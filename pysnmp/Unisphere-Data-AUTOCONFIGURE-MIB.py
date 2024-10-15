# SNMP MIB module (Unisphere-Data-AUTOCONFIGURE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-AUTOCONFIGURE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:19 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdEnable,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdEnable")


# MODULE-IDENTITY

usdAutoConfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48)
)
usdAutoConfMIB.setRevisions(
        ("2002-11-18 00:00",
         "2000-11-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdAutoConfEncaps(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              17,
              19)
        )
    )
    namedValues = NamedValues(
        *(("bridgedEthernet", 19),
          ("ip", 0),
          ("ppp", 1),
          ("pppoe", 17))
    )



# MIB Managed Objects in the order of their OIDs

_UsdAutoConfObjects_ObjectIdentity = ObjectIdentity
usdAutoConfObjects = _UsdAutoConfObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1)
)
_UsdAutoConf_ObjectIdentity = ObjectIdentity
usdAutoConf = _UsdAutoConf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1)
)
_UsdAutoConfTable_Object = MibTable
usdAutoConfTable = _UsdAutoConfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdAutoConfTable.setStatus("current")
_UsdAutoConfEntry_Object = MibTableRow
usdAutoConfEntry = _UsdAutoConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1)
)
usdAutoConfEntry.setIndexNames(
    (0, "Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfIfIndex"),
    (0, "Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfEncaps"),
)
if mibBuilder.loadTexts:
    usdAutoConfEntry.setStatus("current")
_UsdAutoConfIfIndex_Type = InterfaceIndex
_UsdAutoConfIfIndex_Object = MibTableColumn
usdAutoConfIfIndex = _UsdAutoConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 1),
    _UsdAutoConfIfIndex_Type()
)
usdAutoConfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAutoConfIfIndex.setStatus("current")
_UsdAutoConfEncaps_Type = UsdAutoConfEncaps
_UsdAutoConfEncaps_Object = MibTableColumn
usdAutoConfEncaps = _UsdAutoConfEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 2),
    _UsdAutoConfEncaps_Type()
)
usdAutoConfEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdAutoConfEncaps.setStatus("current")
_UsdAutoConfEnable_Type = UsdEnable
_UsdAutoConfEnable_Object = MibTableColumn
usdAutoConfEnable = _UsdAutoConfEnable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 1, 1, 1, 1, 3),
    _UsdAutoConfEnable_Type()
)
usdAutoConfEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdAutoConfEnable.setStatus("current")
_UsdAutoConfMIBConformance_ObjectIdentity = ObjectIdentity
usdAutoConfMIBConformance = _UsdAutoConfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4)
)
_UsdAutoConfMIBCompliances_ObjectIdentity = ObjectIdentity
usdAutoConfMIBCompliances = _UsdAutoConfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1)
)
_UsdAutoConfMIBGroups_ObjectIdentity = ObjectIdentity
usdAutoConfMIBGroups = _UsdAutoConfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2)
)

# Managed Objects groups

usdAutoConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 2, 1)
)
usdAutoConfGroup.setObjects(
    ("Unisphere-Data-AUTOCONFIGURE-MIB", "usdAutoConfEnable")
)
if mibBuilder.loadTexts:
    usdAutoConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdAutoConfCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 48, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdAutoConfCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-AUTOCONFIGURE-MIB",
    **{"UsdAutoConfEncaps": UsdAutoConfEncaps,
       "usdAutoConfMIB": usdAutoConfMIB,
       "usdAutoConfObjects": usdAutoConfObjects,
       "usdAutoConf": usdAutoConf,
       "usdAutoConfTable": usdAutoConfTable,
       "usdAutoConfEntry": usdAutoConfEntry,
       "usdAutoConfIfIndex": usdAutoConfIfIndex,
       "usdAutoConfEncaps": usdAutoConfEncaps,
       "usdAutoConfEnable": usdAutoConfEnable,
       "usdAutoConfMIBConformance": usdAutoConfMIBConformance,
       "usdAutoConfMIBCompliances": usdAutoConfMIBCompliances,
       "usdAutoConfCompliance": usdAutoConfCompliance,
       "usdAutoConfMIBGroups": usdAutoConfMIBGroups,
       "usdAutoConfGroup": usdAutoConfGroup}
)
