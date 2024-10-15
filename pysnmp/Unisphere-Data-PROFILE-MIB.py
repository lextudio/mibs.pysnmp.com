# SNMP MIB module (Unisphere-Data-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:11:24 2024
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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")


# MODULE-IDENTITY

usdProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25)
)
usdProfileMIB.setRevisions(
        ("2002-11-19 20:47",
         "2001-04-04 12:50",
         "2000-04-20 00:00",
         "1999-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdProfileIfEncaps(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              17,
              19,
              127)
        )
    )
    namedValues = NamedValues(
        *(("any", 127),
          ("bridgedEthernet", 19),
          ("ip", 0),
          ("ppp", 1),
          ("pppoe", 17))
    )



# MIB Managed Objects in the order of their OIDs

_UsdProfileObjects_ObjectIdentity = ObjectIdentity
usdProfileObjects = _UsdProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1)
)
_UsdProfileName_ObjectIdentity = ObjectIdentity
usdProfileName = _UsdProfileName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1)
)
_UsdProfileNameTable_Object = MibTable
usdProfileNameTable = _UsdProfileNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1)
)
if mibBuilder.loadTexts:
    usdProfileNameTable.setStatus("current")
_UsdProfileNameEntry_Object = MibTableRow
usdProfileNameEntry = _UsdProfileNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1)
)
usdProfileNameEntry.setIndexNames(
    (1, "Unisphere-Data-PROFILE-MIB", "usdProfileNameName"),
)
if mibBuilder.loadTexts:
    usdProfileNameEntry.setStatus("current")


class _UsdProfileNameName_Type(DisplayString):
    """Custom type usdProfileNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_UsdProfileNameName_Type.__name__ = "DisplayString"
_UsdProfileNameName_Object = MibTableColumn
usdProfileNameName = _UsdProfileNameName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 1),
    _UsdProfileNameName_Type()
)
usdProfileNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdProfileNameName.setStatus("current")
_UsdProfileNameRowStatus_Type = RowStatus
_UsdProfileNameRowStatus_Object = MibTableColumn
usdProfileNameRowStatus = _UsdProfileNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 2),
    _UsdProfileNameRowStatus_Type()
)
usdProfileNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdProfileNameRowStatus.setStatus("current")
_UsdProfileNameId_Type = Unsigned32
_UsdProfileNameId_Object = MibTableColumn
usdProfileNameId = _UsdProfileNameId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 3),
    _UsdProfileNameId_Type()
)
usdProfileNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdProfileNameId.setStatus("current")
_UsdProfileIdTable_Object = MibTable
usdProfileIdTable = _UsdProfileIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2)
)
if mibBuilder.loadTexts:
    usdProfileIdTable.setStatus("current")
_UsdProfileIdEntry_Object = MibTableRow
usdProfileIdEntry = _UsdProfileIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1)
)
usdProfileIdEntry.setIndexNames(
    (0, "Unisphere-Data-PROFILE-MIB", "usdProfileIdId"),
)
if mibBuilder.loadTexts:
    usdProfileIdEntry.setStatus("current")
_UsdProfileIdId_Type = Unsigned32
_UsdProfileIdId_Object = MibTableColumn
usdProfileIdId = _UsdProfileIdId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1, 1),
    _UsdProfileIdId_Type()
)
usdProfileIdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdProfileIdId.setStatus("current")


class _UsdProfileIdName_Type(DisplayString):
    """Custom type usdProfileIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_UsdProfileIdName_Type.__name__ = "DisplayString"
_UsdProfileIdName_Object = MibTableColumn
usdProfileIdName = _UsdProfileIdName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1, 2),
    _UsdProfileIdName_Type()
)
usdProfileIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdProfileIdName.setStatus("current")
_UsdProfileAssign_ObjectIdentity = ObjectIdentity
usdProfileAssign = _UsdProfileAssign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2)
)
_UsdProfAssignIf_ObjectIdentity = ObjectIdentity
usdProfAssignIf = _UsdProfAssignIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1)
)
_UsdProfAssignIfTable_Object = MibTable
usdProfAssignIfTable = _UsdProfAssignIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    usdProfAssignIfTable.setStatus("current")
_UsdProfAssignIfEntry_Object = MibTableRow
usdProfAssignIfEntry = _UsdProfAssignIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1)
)
usdProfAssignIfEntry.setIndexNames(
    (0, "Unisphere-Data-PROFILE-MIB", "usdProfAssignIfIndex"),
    (0, "Unisphere-Data-PROFILE-MIB", "usdProfAssignIfEncaps"),
)
if mibBuilder.loadTexts:
    usdProfAssignIfEntry.setStatus("current")
_UsdProfAssignIfIndex_Type = InterfaceIndex
_UsdProfAssignIfIndex_Object = MibTableColumn
usdProfAssignIfIndex = _UsdProfAssignIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 1),
    _UsdProfAssignIfIndex_Type()
)
usdProfAssignIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdProfAssignIfIndex.setStatus("current")
_UsdProfAssignIfEncaps_Type = UsdProfileIfEncaps
_UsdProfAssignIfEncaps_Object = MibTableColumn
usdProfAssignIfEncaps = _UsdProfAssignIfEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 2),
    _UsdProfAssignIfEncaps_Type()
)
usdProfAssignIfEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdProfAssignIfEncaps.setStatus("current")
_UsdProfAssignIfRowStatus_Type = RowStatus
_UsdProfAssignIfRowStatus_Object = MibTableColumn
usdProfAssignIfRowStatus = _UsdProfAssignIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 3),
    _UsdProfAssignIfRowStatus_Type()
)
usdProfAssignIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdProfAssignIfRowStatus.setStatus("current")
_UsdProfAssignIfProfileId_Type = Unsigned32
_UsdProfAssignIfProfileId_Object = MibTableColumn
usdProfAssignIfProfileId = _UsdProfAssignIfProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 4),
    _UsdProfAssignIfProfileId_Type()
)
usdProfAssignIfProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdProfAssignIfProfileId.setStatus("current")
_UsdProfToIfMapTable_Object = MibTable
usdProfToIfMapTable = _UsdProfToIfMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    usdProfToIfMapTable.setStatus("current")
_UsdProfToIfMapEntry_Object = MibTableRow
usdProfToIfMapEntry = _UsdProfToIfMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1)
)
usdProfToIfMapEntry.setIndexNames(
    (0, "Unisphere-Data-PROFILE-MIB", "usdProfToIfMapProfileId"),
    (0, "Unisphere-Data-PROFILE-MIB", "usdProfToIfMapIndex"),
    (0, "Unisphere-Data-PROFILE-MIB", "usdProfToIfMapEncaps"),
)
if mibBuilder.loadTexts:
    usdProfToIfMapEntry.setStatus("current")
_UsdProfToIfMapProfileId_Type = Unsigned32
_UsdProfToIfMapProfileId_Object = MibTableColumn
usdProfToIfMapProfileId = _UsdProfToIfMapProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 1),
    _UsdProfToIfMapProfileId_Type()
)
usdProfToIfMapProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdProfToIfMapProfileId.setStatus("current")
_UsdProfToIfMapIndex_Type = InterfaceIndex
_UsdProfToIfMapIndex_Object = MibTableColumn
usdProfToIfMapIndex = _UsdProfToIfMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 2),
    _UsdProfToIfMapIndex_Type()
)
usdProfToIfMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdProfToIfMapIndex.setStatus("current")
_UsdProfToIfMapEncaps_Type = UsdProfileIfEncaps
_UsdProfToIfMapEncaps_Object = MibTableColumn
usdProfToIfMapEncaps = _UsdProfToIfMapEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 3),
    _UsdProfToIfMapEncaps_Type()
)
usdProfToIfMapEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdProfToIfMapEncaps.setStatus("current")
_UsdProfileMIBConformance_ObjectIdentity = ObjectIdentity
usdProfileMIBConformance = _UsdProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4)
)
_UsdProfileMIBCompliances_ObjectIdentity = ObjectIdentity
usdProfileMIBCompliances = _UsdProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1)
)
_UsdProfileMIBGroups_ObjectIdentity = ObjectIdentity
usdProfileMIBGroups = _UsdProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2)
)

# Managed Objects groups

usdProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2, 1)
)
usdProfileGroup.setObjects(
      *(("Unisphere-Data-PROFILE-MIB", "usdProfileNameName"),
        ("Unisphere-Data-PROFILE-MIB", "usdProfileNameRowStatus"),
        ("Unisphere-Data-PROFILE-MIB", "usdProfileNameId"),
        ("Unisphere-Data-PROFILE-MIB", "usdProfileIdName"))
)
if mibBuilder.loadTexts:
    usdProfileGroup.setStatus("current")

usdProfileIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2, 2)
)
usdProfileIfGroup.setObjects(
      *(("Unisphere-Data-PROFILE-MIB", "usdProfAssignIfRowStatus"),
        ("Unisphere-Data-PROFILE-MIB", "usdProfAssignIfProfileId"),
        ("Unisphere-Data-PROFILE-MIB", "usdProfToIfMapEncaps"))
)
if mibBuilder.loadTexts:
    usdProfileIfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdProfileCompliance.setStatus(
        "obsolete"
    )

usdProfileCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdProfileCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-PROFILE-MIB",
    **{"UsdProfileIfEncaps": UsdProfileIfEncaps,
       "usdProfileMIB": usdProfileMIB,
       "usdProfileObjects": usdProfileObjects,
       "usdProfileName": usdProfileName,
       "usdProfileNameTable": usdProfileNameTable,
       "usdProfileNameEntry": usdProfileNameEntry,
       "usdProfileNameName": usdProfileNameName,
       "usdProfileNameRowStatus": usdProfileNameRowStatus,
       "usdProfileNameId": usdProfileNameId,
       "usdProfileIdTable": usdProfileIdTable,
       "usdProfileIdEntry": usdProfileIdEntry,
       "usdProfileIdId": usdProfileIdId,
       "usdProfileIdName": usdProfileIdName,
       "usdProfileAssign": usdProfileAssign,
       "usdProfAssignIf": usdProfAssignIf,
       "usdProfAssignIfTable": usdProfAssignIfTable,
       "usdProfAssignIfEntry": usdProfAssignIfEntry,
       "usdProfAssignIfIndex": usdProfAssignIfIndex,
       "usdProfAssignIfEncaps": usdProfAssignIfEncaps,
       "usdProfAssignIfRowStatus": usdProfAssignIfRowStatus,
       "usdProfAssignIfProfileId": usdProfAssignIfProfileId,
       "usdProfToIfMapTable": usdProfToIfMapTable,
       "usdProfToIfMapEntry": usdProfToIfMapEntry,
       "usdProfToIfMapProfileId": usdProfToIfMapProfileId,
       "usdProfToIfMapIndex": usdProfToIfMapIndex,
       "usdProfToIfMapEncaps": usdProfToIfMapEncaps,
       "usdProfileMIBConformance": usdProfileMIBConformance,
       "usdProfileMIBCompliances": usdProfileMIBCompliances,
       "usdProfileCompliance": usdProfileCompliance,
       "usdProfileCompliance2": usdProfileCompliance2,
       "usdProfileMIBGroups": usdProfileMIBGroups,
       "usdProfileGroup": usdProfileGroup,
       "usdProfileIfGroup": usdProfileIfGroup}
)
