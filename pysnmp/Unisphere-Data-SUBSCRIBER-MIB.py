# SNMP MIB module (Unisphere-Data-SUBSCRIBER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-SUBSCRIBER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:42 2024
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

usdSubscriberMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49)
)
usdSubscriberMIB.setRevisions(
        ("2002-05-10 19:53",
         "2000-11-16 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdSubscrEncaps(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              19)
        )
    )
    namedValues = NamedValues(
        *(("bridgedEthernet", 19),
          ("ip", 0))
    )



# MIB Managed Objects in the order of their OIDs

_UsdSubscrObjects_ObjectIdentity = ObjectIdentity
usdSubscrObjects = _UsdSubscrObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1)
)
_UsdSubscrLocal_ObjectIdentity = ObjectIdentity
usdSubscrLocal = _UsdSubscrLocal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1)
)
_UsdSubscrLocalTable_Object = MibTable
usdSubscrLocalTable = _UsdSubscrLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdSubscrLocalTable.setStatus("current")
_UsdSubscrLocalEntry_Object = MibTableRow
usdSubscrLocalEntry = _UsdSubscrLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1)
)
usdSubscrLocalEntry.setIndexNames(
    (0, "Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalIfIndex"),
    (0, "Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalEncaps"),
)
if mibBuilder.loadTexts:
    usdSubscrLocalEntry.setStatus("current")
_UsdSubscrLocalIfIndex_Type = InterfaceIndex
_UsdSubscrLocalIfIndex_Object = MibTableColumn
usdSubscrLocalIfIndex = _UsdSubscrLocalIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 1),
    _UsdSubscrLocalIfIndex_Type()
)
usdSubscrLocalIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdSubscrLocalIfIndex.setStatus("current")
_UsdSubscrLocalEncaps_Type = UsdSubscrEncaps
_UsdSubscrLocalEncaps_Object = MibTableColumn
usdSubscrLocalEncaps = _UsdSubscrLocalEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 2),
    _UsdSubscrLocalEncaps_Type()
)
usdSubscrLocalEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdSubscrLocalEncaps.setStatus("current")


class _UsdSubscrLocalControl_Type(Integer32):
    """Custom type usdSubscrLocalControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("ok", 0))
    )


_UsdSubscrLocalControl_Type.__name__ = "Integer32"
_UsdSubscrLocalControl_Object = MibTableColumn
usdSubscrLocalControl = _UsdSubscrLocalControl_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 3),
    _UsdSubscrLocalControl_Type()
)
usdSubscrLocalControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSubscrLocalControl.setStatus("current")
_UsdSubscrLocalNamePrefix_Type = UsdEnable
_UsdSubscrLocalNamePrefix_Object = MibTableColumn
usdSubscrLocalNamePrefix = _UsdSubscrLocalNamePrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 4),
    _UsdSubscrLocalNamePrefix_Type()
)
usdSubscrLocalNamePrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSubscrLocalNamePrefix.setStatus("current")


class _UsdSubscrLocalName_Type(DisplayString):
    """Custom type usdSubscrLocalName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UsdSubscrLocalName_Type.__name__ = "DisplayString"
_UsdSubscrLocalName_Object = MibTableColumn
usdSubscrLocalName = _UsdSubscrLocalName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 5),
    _UsdSubscrLocalName_Type()
)
usdSubscrLocalName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSubscrLocalName.setStatus("current")
_UsdSubscrLocalPasswordPrefix_Type = UsdEnable
_UsdSubscrLocalPasswordPrefix_Object = MibTableColumn
usdSubscrLocalPasswordPrefix = _UsdSubscrLocalPasswordPrefix_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 6),
    _UsdSubscrLocalPasswordPrefix_Type()
)
usdSubscrLocalPasswordPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSubscrLocalPasswordPrefix.setStatus("current")


class _UsdSubscrLocalPassword_Type(DisplayString):
    """Custom type usdSubscrLocalPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UsdSubscrLocalPassword_Type.__name__ = "DisplayString"
_UsdSubscrLocalPassword_Object = MibTableColumn
usdSubscrLocalPassword = _UsdSubscrLocalPassword_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 7),
    _UsdSubscrLocalPassword_Type()
)
usdSubscrLocalPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSubscrLocalPassword.setStatus("current")


class _UsdSubscrLocalDomain_Type(DisplayString):
    """Custom type usdSubscrLocalDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_UsdSubscrLocalDomain_Type.__name__ = "DisplayString"
_UsdSubscrLocalDomain_Object = MibTableColumn
usdSubscrLocalDomain = _UsdSubscrLocalDomain_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 8),
    _UsdSubscrLocalDomain_Type()
)
usdSubscrLocalDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSubscrLocalDomain.setStatus("current")


class _UsdSubscrLocalAuthentication_Type(UsdEnable):
    """Custom type usdSubscrLocalAuthentication based on UsdEnable"""


_UsdSubscrLocalAuthentication_Object = MibTableColumn
usdSubscrLocalAuthentication = _UsdSubscrLocalAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 1, 1, 1, 1, 9),
    _UsdSubscrLocalAuthentication_Type()
)
usdSubscrLocalAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdSubscrLocalAuthentication.setStatus("current")
_UsdSubscriberMIBConformance_ObjectIdentity = ObjectIdentity
usdSubscriberMIBConformance = _UsdSubscriberMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4)
)
_UsdSubscriberMIBCompliances_ObjectIdentity = ObjectIdentity
usdSubscriberMIBCompliances = _UsdSubscriberMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1)
)
_UsdSubscriberMIBGroups_ObjectIdentity = ObjectIdentity
usdSubscriberMIBGroups = _UsdSubscriberMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2)
)

# Managed Objects groups

usdSubscriberLocalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 1)
)
usdSubscriberLocalGroup.setObjects(
      *(("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalControl"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalNamePrefix"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalName"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPasswordPrefix"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPassword"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalDomain"))
)
if mibBuilder.loadTexts:
    usdSubscriberLocalGroup.setStatus("obsolete")

usdSubscriberLocalGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 2, 2)
)
usdSubscriberLocalGroup2.setObjects(
      *(("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalControl"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalNamePrefix"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalName"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPasswordPrefix"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalPassword"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalDomain"),
        ("Unisphere-Data-SUBSCRIBER-MIB", "usdSubscrLocalAuthentication"))
)
if mibBuilder.loadTexts:
    usdSubscriberLocalGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdSubscriberCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdSubscriberCompliance.setStatus(
        "obsolete"
    )

usdSubscriberCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 49, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdSubscriberCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-SUBSCRIBER-MIB",
    **{"UsdSubscrEncaps": UsdSubscrEncaps,
       "usdSubscriberMIB": usdSubscriberMIB,
       "usdSubscrObjects": usdSubscrObjects,
       "usdSubscrLocal": usdSubscrLocal,
       "usdSubscrLocalTable": usdSubscrLocalTable,
       "usdSubscrLocalEntry": usdSubscrLocalEntry,
       "usdSubscrLocalIfIndex": usdSubscrLocalIfIndex,
       "usdSubscrLocalEncaps": usdSubscrLocalEncaps,
       "usdSubscrLocalControl": usdSubscrLocalControl,
       "usdSubscrLocalNamePrefix": usdSubscrLocalNamePrefix,
       "usdSubscrLocalName": usdSubscrLocalName,
       "usdSubscrLocalPasswordPrefix": usdSubscrLocalPasswordPrefix,
       "usdSubscrLocalPassword": usdSubscrLocalPassword,
       "usdSubscrLocalDomain": usdSubscrLocalDomain,
       "usdSubscrLocalAuthentication": usdSubscrLocalAuthentication,
       "usdSubscriberMIBConformance": usdSubscriberMIBConformance,
       "usdSubscriberMIBCompliances": usdSubscriberMIBCompliances,
       "usdSubscriberCompliance": usdSubscriberCompliance,
       "usdSubscriberCompliance2": usdSubscriberCompliance2,
       "usdSubscriberMIBGroups": usdSubscriberMIBGroups,
       "usdSubscriberLocalGroup": usdSubscriberLocalGroup,
       "usdSubscriberLocalGroup2": usdSubscriberLocalGroup2}
)
