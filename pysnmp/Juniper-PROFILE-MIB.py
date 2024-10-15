# SNMP MIB module (Juniper-PROFILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-PROFILE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:40 2024
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

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

juniProfileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25)
)
juniProfileMIB.setRevisions(
        ("2003-01-31 21:18",
         "2003-01-31 21:03",
         "2002-11-19 20:47",
         "2001-04-04 12:50",
         "2000-04-20 00:00",
         "1999-06-01 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniProfileIfEncaps(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              11,
              17,
              19,
              127)
        )
    )
    namedValues = NamedValues(
        *(("any", 127),
          ("atm1483", 11),
          ("bridgedEthernet", 19),
          ("ip", 0),
          ("ppp", 1),
          ("pppoe", 17))
    )



class JuniProfileRangeId(Unsigned32, TextualConvention):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_JuniProfileObjects_ObjectIdentity = ObjectIdentity
juniProfileObjects = _JuniProfileObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1)
)
_JuniProfileName_ObjectIdentity = ObjectIdentity
juniProfileName = _JuniProfileName_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1)
)
_JuniProfileNameTable_Object = MibTable
juniProfileNameTable = _JuniProfileNameTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1)
)
if mibBuilder.loadTexts:
    juniProfileNameTable.setStatus("current")
_JuniProfileNameEntry_Object = MibTableRow
juniProfileNameEntry = _JuniProfileNameEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1)
)
juniProfileNameEntry.setIndexNames(
    (1, "Juniper-PROFILE-MIB", "juniProfileNameName"),
)
if mibBuilder.loadTexts:
    juniProfileNameEntry.setStatus("current")


class _JuniProfileNameName_Type(DisplayString):
    """Custom type juniProfileNameName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JuniProfileNameName_Type.__name__ = "DisplayString"
_JuniProfileNameName_Object = MibTableColumn
juniProfileNameName = _JuniProfileNameName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 1),
    _JuniProfileNameName_Type()
)
juniProfileNameName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniProfileNameName.setStatus("current")
_JuniProfileNameRowStatus_Type = RowStatus
_JuniProfileNameRowStatus_Object = MibTableColumn
juniProfileNameRowStatus = _JuniProfileNameRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 2),
    _JuniProfileNameRowStatus_Type()
)
juniProfileNameRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniProfileNameRowStatus.setStatus("current")
_JuniProfileNameId_Type = Unsigned32
_JuniProfileNameId_Object = MibTableColumn
juniProfileNameId = _JuniProfileNameId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 1, 1, 3),
    _JuniProfileNameId_Type()
)
juniProfileNameId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniProfileNameId.setStatus("current")
_JuniProfileIdTable_Object = MibTable
juniProfileIdTable = _JuniProfileIdTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2)
)
if mibBuilder.loadTexts:
    juniProfileIdTable.setStatus("current")
_JuniProfileIdEntry_Object = MibTableRow
juniProfileIdEntry = _JuniProfileIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1)
)
juniProfileIdEntry.setIndexNames(
    (0, "Juniper-PROFILE-MIB", "juniProfileIdId"),
)
if mibBuilder.loadTexts:
    juniProfileIdEntry.setStatus("current")
_JuniProfileIdId_Type = Unsigned32
_JuniProfileIdId_Object = MibTableColumn
juniProfileIdId = _JuniProfileIdId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1, 1),
    _JuniProfileIdId_Type()
)
juniProfileIdId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfileIdId.setStatus("current")


class _JuniProfileIdName_Type(DisplayString):
    """Custom type juniProfileIdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_JuniProfileIdName_Type.__name__ = "DisplayString"
_JuniProfileIdName_Object = MibTableColumn
juniProfileIdName = _JuniProfileIdName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 1, 2, 1, 2),
    _JuniProfileIdName_Type()
)
juniProfileIdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniProfileIdName.setStatus("current")
_JuniProfileAssign_ObjectIdentity = ObjectIdentity
juniProfileAssign = _JuniProfileAssign_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2)
)
_JuniProfAssignIf_ObjectIdentity = ObjectIdentity
juniProfAssignIf = _JuniProfAssignIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1)
)
_JuniProfAssignIfTable_Object = MibTable
juniProfAssignIfTable = _JuniProfAssignIfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    juniProfAssignIfTable.setStatus("current")
_JuniProfAssignIfEntry_Object = MibTableRow
juniProfAssignIfEntry = _JuniProfAssignIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1)
)
juniProfAssignIfEntry.setIndexNames(
    (0, "Juniper-PROFILE-MIB", "juniProfAssignIfIndex"),
    (0, "Juniper-PROFILE-MIB", "juniProfAssignIfEncaps"),
)
if mibBuilder.loadTexts:
    juniProfAssignIfEntry.setStatus("current")
_JuniProfAssignIfIndex_Type = InterfaceIndex
_JuniProfAssignIfIndex_Object = MibTableColumn
juniProfAssignIfIndex = _JuniProfAssignIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 1),
    _JuniProfAssignIfIndex_Type()
)
juniProfAssignIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfAssignIfIndex.setStatus("current")
_JuniProfAssignIfEncaps_Type = JuniProfileIfEncaps
_JuniProfAssignIfEncaps_Object = MibTableColumn
juniProfAssignIfEncaps = _JuniProfAssignIfEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 2),
    _JuniProfAssignIfEncaps_Type()
)
juniProfAssignIfEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfAssignIfEncaps.setStatus("current")
_JuniProfAssignIfRowStatus_Type = RowStatus
_JuniProfAssignIfRowStatus_Object = MibTableColumn
juniProfAssignIfRowStatus = _JuniProfAssignIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 3),
    _JuniProfAssignIfRowStatus_Type()
)
juniProfAssignIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniProfAssignIfRowStatus.setStatus("current")
_JuniProfAssignIfProfileId_Type = Unsigned32
_JuniProfAssignIfProfileId_Object = MibTableColumn
juniProfAssignIfProfileId = _JuniProfAssignIfProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 1, 1, 4),
    _JuniProfAssignIfProfileId_Type()
)
juniProfAssignIfProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniProfAssignIfProfileId.setStatus("current")
_JuniProfToIfMapTable_Object = MibTable
juniProfToIfMapTable = _JuniProfToIfMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    juniProfToIfMapTable.setStatus("current")
_JuniProfToIfMapEntry_Object = MibTableRow
juniProfToIfMapEntry = _JuniProfToIfMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1)
)
juniProfToIfMapEntry.setIndexNames(
    (0, "Juniper-PROFILE-MIB", "juniProfToIfMapProfileId"),
    (0, "Juniper-PROFILE-MIB", "juniProfToIfMapIndex"),
    (0, "Juniper-PROFILE-MIB", "juniProfToIfMapEncaps"),
)
if mibBuilder.loadTexts:
    juniProfToIfMapEntry.setStatus("current")
_JuniProfToIfMapProfileId_Type = Unsigned32
_JuniProfToIfMapProfileId_Object = MibTableColumn
juniProfToIfMapProfileId = _JuniProfToIfMapProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 1),
    _JuniProfToIfMapProfileId_Type()
)
juniProfToIfMapProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfToIfMapProfileId.setStatus("current")
_JuniProfToIfMapIndex_Type = InterfaceIndex
_JuniProfToIfMapIndex_Object = MibTableColumn
juniProfToIfMapIndex = _JuniProfToIfMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 2),
    _JuniProfToIfMapIndex_Type()
)
juniProfToIfMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfToIfMapIndex.setStatus("current")
_JuniProfToIfMapEncaps_Type = JuniProfileIfEncaps
_JuniProfToIfMapEncaps_Object = MibTableColumn
juniProfToIfMapEncaps = _JuniProfToIfMapEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 1, 2, 1, 3),
    _JuniProfToIfMapEncaps_Type()
)
juniProfToIfMapEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniProfToIfMapEncaps.setStatus("current")
_JuniProfAssignIfRange_ObjectIdentity = ObjectIdentity
juniProfAssignIfRange = _JuniProfAssignIfRange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2)
)
_JuniProfAssignIfRangeTable_Object = MibTable
juniProfAssignIfRangeTable = _JuniProfAssignIfRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    juniProfAssignIfRangeTable.setStatus("current")
_JuniProfAssignIfRangeEntry_Object = MibTableRow
juniProfAssignIfRangeEntry = _JuniProfAssignIfRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 1, 1)
)
juniProfAssignIfRangeEntry.setIndexNames(
    (0, "Juniper-PROFILE-MIB", "juniProfAssignIfRangeIndex"),
    (0, "Juniper-PROFILE-MIB", "juniProfAssignIfRangeEncaps"),
    (0, "Juniper-PROFILE-MIB", "juniProfAssignIfRangeRangeId"),
)
if mibBuilder.loadTexts:
    juniProfAssignIfRangeEntry.setStatus("current")
_JuniProfAssignIfRangeIndex_Type = InterfaceIndex
_JuniProfAssignIfRangeIndex_Object = MibTableColumn
juniProfAssignIfRangeIndex = _JuniProfAssignIfRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 1, 1, 1),
    _JuniProfAssignIfRangeIndex_Type()
)
juniProfAssignIfRangeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfAssignIfRangeIndex.setStatus("current")
_JuniProfAssignIfRangeEncaps_Type = JuniProfileIfEncaps
_JuniProfAssignIfRangeEncaps_Object = MibTableColumn
juniProfAssignIfRangeEncaps = _JuniProfAssignIfRangeEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 1, 1, 2),
    _JuniProfAssignIfRangeEncaps_Type()
)
juniProfAssignIfRangeEncaps.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfAssignIfRangeEncaps.setStatus("current")
_JuniProfAssignIfRangeRangeId_Type = JuniProfileRangeId
_JuniProfAssignIfRangeRangeId_Object = MibTableColumn
juniProfAssignIfRangeRangeId = _JuniProfAssignIfRangeRangeId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 1, 1, 3),
    _JuniProfAssignIfRangeRangeId_Type()
)
juniProfAssignIfRangeRangeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfAssignIfRangeRangeId.setStatus("current")
_JuniProfAssignIfRangeRowStatus_Type = RowStatus
_JuniProfAssignIfRangeRowStatus_Object = MibTableColumn
juniProfAssignIfRangeRowStatus = _JuniProfAssignIfRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 1, 1, 4),
    _JuniProfAssignIfRangeRowStatus_Type()
)
juniProfAssignIfRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniProfAssignIfRangeRowStatus.setStatus("current")
_JuniProfAssignIfRangeProfileId_Type = Unsigned32
_JuniProfAssignIfRangeProfileId_Object = MibTableColumn
juniProfAssignIfRangeProfileId = _JuniProfAssignIfRangeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 1, 1, 5),
    _JuniProfAssignIfRangeProfileId_Type()
)
juniProfAssignIfRangeProfileId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniProfAssignIfRangeProfileId.setStatus("current")
_JuniProfToIfRangeMapTable_Object = MibTable
juniProfToIfRangeMapTable = _JuniProfToIfRangeMapTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    juniProfToIfRangeMapTable.setStatus("current")
_JuniProfToIfRangeMapEntry_Object = MibTableRow
juniProfToIfRangeMapEntry = _JuniProfToIfRangeMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 2, 1)
)
juniProfToIfRangeMapEntry.setIndexNames(
    (0, "Juniper-PROFILE-MIB", "juniProfToIfRangeMapProfileId"),
    (0, "Juniper-PROFILE-MIB", "juniProfToIfRangeMapIndex"),
    (0, "Juniper-PROFILE-MIB", "juniProfToIfRangeMapEncaps"),
    (0, "Juniper-PROFILE-MIB", "juniProfToIfRangeMapRangeId"),
)
if mibBuilder.loadTexts:
    juniProfToIfRangeMapEntry.setStatus("current")
_JuniProfToIfRangeMapProfileId_Type = Unsigned32
_JuniProfToIfRangeMapProfileId_Object = MibTableColumn
juniProfToIfRangeMapProfileId = _JuniProfToIfRangeMapProfileId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 2, 1, 1),
    _JuniProfToIfRangeMapProfileId_Type()
)
juniProfToIfRangeMapProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfToIfRangeMapProfileId.setStatus("current")
_JuniProfToIfRangeMapIndex_Type = InterfaceIndex
_JuniProfToIfRangeMapIndex_Object = MibTableColumn
juniProfToIfRangeMapIndex = _JuniProfToIfRangeMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 2, 1, 2),
    _JuniProfToIfRangeMapIndex_Type()
)
juniProfToIfRangeMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfToIfRangeMapIndex.setStatus("current")
_JuniProfToIfRangeMapEncaps_Type = JuniProfileIfEncaps
_JuniProfToIfRangeMapEncaps_Object = MibTableColumn
juniProfToIfRangeMapEncaps = _JuniProfToIfRangeMapEncaps_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 2, 1, 3),
    _JuniProfToIfRangeMapEncaps_Type()
)
juniProfToIfRangeMapEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniProfToIfRangeMapEncaps.setStatus("current")
_JuniProfToIfRangeMapRangeId_Type = JuniProfileRangeId
_JuniProfToIfRangeMapRangeId_Object = MibTableColumn
juniProfToIfRangeMapRangeId = _JuniProfToIfRangeMapRangeId_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 1, 2, 2, 2, 1, 4),
    _JuniProfToIfRangeMapRangeId_Type()
)
juniProfToIfRangeMapRangeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniProfToIfRangeMapRangeId.setStatus("current")
_JuniProfileMIBConformance_ObjectIdentity = ObjectIdentity
juniProfileMIBConformance = _JuniProfileMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4)
)
_JuniProfileMIBCompliances_ObjectIdentity = ObjectIdentity
juniProfileMIBCompliances = _JuniProfileMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1)
)
_JuniProfileMIBGroups_ObjectIdentity = ObjectIdentity
juniProfileMIBGroups = _JuniProfileMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2)
)

# Managed Objects groups

juniProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2, 1)
)
juniProfileGroup.setObjects(
      *(("Juniper-PROFILE-MIB", "juniProfileNameName"),
        ("Juniper-PROFILE-MIB", "juniProfileNameRowStatus"),
        ("Juniper-PROFILE-MIB", "juniProfileNameId"),
        ("Juniper-PROFILE-MIB", "juniProfileIdName"))
)
if mibBuilder.loadTexts:
    juniProfileGroup.setStatus("current")

juniProfileIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2, 2)
)
juniProfileIfGroup.setObjects(
      *(("Juniper-PROFILE-MIB", "juniProfAssignIfRowStatus"),
        ("Juniper-PROFILE-MIB", "juniProfAssignIfProfileId"),
        ("Juniper-PROFILE-MIB", "juniProfToIfMapEncaps"))
)
if mibBuilder.loadTexts:
    juniProfileIfGroup.setStatus("obsolete")

juniProfileIfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 2, 3)
)
juniProfileIfGroup2.setObjects(
      *(("Juniper-PROFILE-MIB", "juniProfAssignIfRowStatus"),
        ("Juniper-PROFILE-MIB", "juniProfAssignIfProfileId"),
        ("Juniper-PROFILE-MIB", "juniProfToIfMapEncaps"),
        ("Juniper-PROFILE-MIB", "juniProfAssignIfRangeRowStatus"),
        ("Juniper-PROFILE-MIB", "juniProfAssignIfRangeProfileId"),
        ("Juniper-PROFILE-MIB", "juniProfToIfRangeMapEncaps"))
)
if mibBuilder.loadTexts:
    juniProfileIfGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniProfileCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniProfileCompliance.setStatus(
        "obsolete"
    )

juniProfileCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniProfileCompliance2.setStatus(
        "obsolete"
    )

juniProfileCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 25, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniProfileCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-PROFILE-MIB",
    **{"JuniProfileIfEncaps": JuniProfileIfEncaps,
       "JuniProfileRangeId": JuniProfileRangeId,
       "juniProfileMIB": juniProfileMIB,
       "juniProfileObjects": juniProfileObjects,
       "juniProfileName": juniProfileName,
       "juniProfileNameTable": juniProfileNameTable,
       "juniProfileNameEntry": juniProfileNameEntry,
       "juniProfileNameName": juniProfileNameName,
       "juniProfileNameRowStatus": juniProfileNameRowStatus,
       "juniProfileNameId": juniProfileNameId,
       "juniProfileIdTable": juniProfileIdTable,
       "juniProfileIdEntry": juniProfileIdEntry,
       "juniProfileIdId": juniProfileIdId,
       "juniProfileIdName": juniProfileIdName,
       "juniProfileAssign": juniProfileAssign,
       "juniProfAssignIf": juniProfAssignIf,
       "juniProfAssignIfTable": juniProfAssignIfTable,
       "juniProfAssignIfEntry": juniProfAssignIfEntry,
       "juniProfAssignIfIndex": juniProfAssignIfIndex,
       "juniProfAssignIfEncaps": juniProfAssignIfEncaps,
       "juniProfAssignIfRowStatus": juniProfAssignIfRowStatus,
       "juniProfAssignIfProfileId": juniProfAssignIfProfileId,
       "juniProfToIfMapTable": juniProfToIfMapTable,
       "juniProfToIfMapEntry": juniProfToIfMapEntry,
       "juniProfToIfMapProfileId": juniProfToIfMapProfileId,
       "juniProfToIfMapIndex": juniProfToIfMapIndex,
       "juniProfToIfMapEncaps": juniProfToIfMapEncaps,
       "juniProfAssignIfRange": juniProfAssignIfRange,
       "juniProfAssignIfRangeTable": juniProfAssignIfRangeTable,
       "juniProfAssignIfRangeEntry": juniProfAssignIfRangeEntry,
       "juniProfAssignIfRangeIndex": juniProfAssignIfRangeIndex,
       "juniProfAssignIfRangeEncaps": juniProfAssignIfRangeEncaps,
       "juniProfAssignIfRangeRangeId": juniProfAssignIfRangeRangeId,
       "juniProfAssignIfRangeRowStatus": juniProfAssignIfRangeRowStatus,
       "juniProfAssignIfRangeProfileId": juniProfAssignIfRangeProfileId,
       "juniProfToIfRangeMapTable": juniProfToIfRangeMapTable,
       "juniProfToIfRangeMapEntry": juniProfToIfRangeMapEntry,
       "juniProfToIfRangeMapProfileId": juniProfToIfRangeMapProfileId,
       "juniProfToIfRangeMapIndex": juniProfToIfRangeMapIndex,
       "juniProfToIfRangeMapEncaps": juniProfToIfRangeMapEncaps,
       "juniProfToIfRangeMapRangeId": juniProfToIfRangeMapRangeId,
       "juniProfileMIBConformance": juniProfileMIBConformance,
       "juniProfileMIBCompliances": juniProfileMIBCompliances,
       "juniProfileCompliance": juniProfileCompliance,
       "juniProfileCompliance2": juniProfileCompliance2,
       "juniProfileCompliance3": juniProfileCompliance3,
       "juniProfileMIBGroups": juniProfileMIBGroups,
       "juniProfileGroup": juniProfileGroup,
       "juniProfileIfGroup": juniProfileIfGroup,
       "juniProfileIfGroup2": juniProfileIfGroup2}
)
