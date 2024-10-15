# SNMP MIB module (Unisphere-Data-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Unisphere-Data-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:10:17 2024
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(UsdIpPolicyExtendedCommunity,
 UsdIpPolicyName) = mibBuilder.importSymbols(
    "Unisphere-Data-IP-POLICY-MIB",
    "UsdIpPolicyExtendedCommunity",
    "UsdIpPolicyName")

(usDataMibs,) = mibBuilder.importSymbols(
    "Unisphere-Data-MIBs",
    "usDataMibs")

(UsdName,) = mibBuilder.importSymbols(
    "Unisphere-Data-TC",
    "UsdName")


# MODULE-IDENTITY

usdRouterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32)
)
usdRouterMIB.setRevisions(
        ("2002-05-10 18:16",
         "2001-01-24 18:25",
         "2000-01-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class UsdNextRouterIndex(Unsigned32, TextualConvention):
    status = "current"


class UsdRouterProtocolIndex(Integer32, TextualConvention):
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
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 7),
          ("cops", 20),
          ("dhcpLocalServer", 28),
          ("dhcpProxy", 15),
          ("dhcpRelay", 16),
          ("dvmrp", 22),
          ("generator", 13),
          ("icmp", 3),
          ("igmp", 4),
          ("ip", 1),
          ("isis", 9),
          ("localAddressServer", 14),
          ("mgtm", 21),
          ("mpls", 25),
          ("mplsMgr", 27),
          ("msdp", 24),
          ("nameResolver", 17),
          ("ntp", 12),
          ("osi", 2),
          ("ospf", 8),
          ("pim", 23),
          ("policyManager", 18),
          ("radius", 26),
          ("rip", 10),
          ("snmp", 11),
          ("sscClient", 19),
          ("tcp", 5),
          ("udp", 6))
    )



# MIB Managed Objects in the order of their OIDs

_UsdRouterObjects_ObjectIdentity = ObjectIdentity
usdRouterObjects = _UsdRouterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1)
)
_UsdRouterNextRouterIndex_Type = UsdNextRouterIndex
_UsdRouterNextRouterIndex_Object = MibScalar
usdRouterNextRouterIndex = _UsdRouterNextRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 1),
    _UsdRouterNextRouterIndex_Type()
)
usdRouterNextRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRouterNextRouterIndex.setStatus("current")
_UsdRouterTable_Object = MibTable
usdRouterTable = _UsdRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2)
)
if mibBuilder.loadTexts:
    usdRouterTable.setStatus("current")
_UsdRouterEntry_Object = MibTableRow
usdRouterEntry = _UsdRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1)
)
usdRouterEntry.setIndexNames(
    (0, "Unisphere-Data-ROUTER-MIB", "usdRouterIndex"),
)
if mibBuilder.loadTexts:
    usdRouterEntry.setStatus("current")
_UsdRouterIndex_Type = Unsigned32
_UsdRouterIndex_Object = MibTableColumn
usdRouterIndex = _UsdRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 1),
    _UsdRouterIndex_Type()
)
usdRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRouterIndex.setStatus("current")
_UsdRouterName_Type = UsdName
_UsdRouterName_Object = MibTableColumn
usdRouterName = _UsdRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 2),
    _UsdRouterName_Type()
)
usdRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRouterName.setStatus("current")
_UsdRouterRowStatus_Type = RowStatus
_UsdRouterRowStatus_Object = MibTableColumn
usdRouterRowStatus = _UsdRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 3),
    _UsdRouterRowStatus_Type()
)
usdRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRouterRowStatus.setStatus("current")
_UsdRouterVrf_Type = TruthValue
_UsdRouterVrf_Object = MibTableColumn
usdRouterVrf = _UsdRouterVrf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 4),
    _UsdRouterVrf_Type()
)
usdRouterVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRouterVrf.setStatus("current")


class _UsdRouterContextName_Type(OctetString):
    """Custom type usdRouterContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 14),
    )


_UsdRouterContextName_Type.__name__ = "OctetString"
_UsdRouterContextName_Object = MibTableColumn
usdRouterContextName = _UsdRouterContextName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 5),
    _UsdRouterContextName_Type()
)
usdRouterContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    usdRouterContextName.setStatus("current")
_UsdRouterProtocolTable_Object = MibTable
usdRouterProtocolTable = _UsdRouterProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3)
)
if mibBuilder.loadTexts:
    usdRouterProtocolTable.setStatus("current")
_UsdRouterProtocolEntry_Object = MibTableRow
usdRouterProtocolEntry = _UsdRouterProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1)
)
usdRouterProtocolEntry.setIndexNames(
    (0, "Unisphere-Data-ROUTER-MIB", "usdRouterProtocolRouterIndex"),
    (0, "Unisphere-Data-ROUTER-MIB", "usdRouterProtocolProtocolIndex"),
)
if mibBuilder.loadTexts:
    usdRouterProtocolEntry.setStatus("current")
_UsdRouterProtocolRouterIndex_Type = Unsigned32
_UsdRouterProtocolRouterIndex_Object = MibTableColumn
usdRouterProtocolRouterIndex = _UsdRouterProtocolRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1, 1),
    _UsdRouterProtocolRouterIndex_Type()
)
usdRouterProtocolRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRouterProtocolRouterIndex.setStatus("current")
_UsdRouterProtocolProtocolIndex_Type = UsdRouterProtocolIndex
_UsdRouterProtocolProtocolIndex_Object = MibTableColumn
usdRouterProtocolProtocolIndex = _UsdRouterProtocolProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1, 2),
    _UsdRouterProtocolProtocolIndex_Type()
)
usdRouterProtocolProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRouterProtocolProtocolIndex.setStatus("current")
_UsdRouterProtocolRowStatus_Type = RowStatus
_UsdRouterProtocolRowStatus_Object = MibTableColumn
usdRouterProtocolRowStatus = _UsdRouterProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1, 3),
    _UsdRouterProtocolRowStatus_Type()
)
usdRouterProtocolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    usdRouterProtocolRowStatus.setStatus("current")
_UsdRouterVrfTable_Object = MibTable
usdRouterVrfTable = _UsdRouterVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4)
)
if mibBuilder.loadTexts:
    usdRouterVrfTable.setStatus("current")
_UsdRouterVrfEntry_Object = MibTableRow
usdRouterVrfEntry = _UsdRouterVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1)
)
usdRouterVrfEntry.setIndexNames(
    (0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouterIndex"),
    (0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouterVrfIndex"),
)
if mibBuilder.loadTexts:
    usdRouterVrfEntry.setStatus("current")
_UsdRouterVrfRouterIndex_Type = Unsigned32
_UsdRouterVrfRouterIndex_Object = MibTableColumn
usdRouterVrfRouterIndex = _UsdRouterVrfRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 1),
    _UsdRouterVrfRouterIndex_Type()
)
usdRouterVrfRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRouterVrfRouterIndex.setStatus("current")
_UsdRouterVrfRouterVrfIndex_Type = Unsigned32
_UsdRouterVrfRouterVrfIndex_Object = MibTableColumn
usdRouterVrfRouterVrfIndex = _UsdRouterVrfRouterVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 2),
    _UsdRouterVrfRouterVrfIndex_Type()
)
usdRouterVrfRouterVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRouterVrfRouterVrfIndex.setStatus("current")
_UsdRouterVrfImportRouteMap_Type = UsdIpPolicyName
_UsdRouterVrfImportRouteMap_Object = MibTableColumn
usdRouterVrfImportRouteMap = _UsdRouterVrfImportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 3),
    _UsdRouterVrfImportRouteMap_Type()
)
usdRouterVrfImportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRouterVrfImportRouteMap.setStatus("current")
_UsdRouterVrfExportRouteMap_Type = UsdIpPolicyName
_UsdRouterVrfExportRouteMap_Object = MibTableColumn
usdRouterVrfExportRouteMap = _UsdRouterVrfExportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 4),
    _UsdRouterVrfExportRouteMap_Type()
)
usdRouterVrfExportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRouterVrfExportRouteMap.setStatus("current")
_UsdRouterVrfRouteDistinguisher_Type = UsdIpPolicyExtendedCommunity
_UsdRouterVrfRouteDistinguisher_Object = MibTableColumn
usdRouterVrfRouteDistinguisher = _UsdRouterVrfRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 5),
    _UsdRouterVrfRouteDistinguisher_Type()
)
usdRouterVrfRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRouterVrfRouteDistinguisher.setStatus("current")
_UsdRouterVrfRowStatus_Type = RowStatus
_UsdRouterVrfRowStatus_Object = MibTableColumn
usdRouterVrfRowStatus = _UsdRouterVrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 7),
    _UsdRouterVrfRowStatus_Type()
)
usdRouterVrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRouterVrfRowStatus.setStatus("current")
_UsdRouterVrfRouterName_Type = UsdName
_UsdRouterVrfRouterName_Object = MibTableColumn
usdRouterVrfRouterName = _UsdRouterVrfRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 8),
    _UsdRouterVrfRouterName_Type()
)
usdRouterVrfRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRouterVrfRouterName.setStatus("current")


class _UsdRouterVrfRouterDescription_Type(DisplayString):
    """Custom type usdRouterVrfRouterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_UsdRouterVrfRouterDescription_Type.__name__ = "DisplayString"
_UsdRouterVrfRouterDescription_Object = MibTableColumn
usdRouterVrfRouterDescription = _UsdRouterVrfRouterDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 9),
    _UsdRouterVrfRouterDescription_Type()
)
usdRouterVrfRouterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRouterVrfRouterDescription.setStatus("current")
_UsdRouterVrfRouteTargetTable_Object = MibTable
usdRouterVrfRouteTargetTable = _UsdRouterVrfRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5)
)
if mibBuilder.loadTexts:
    usdRouterVrfRouteTargetTable.setStatus("current")
_UsdRouterVrfRouteTargetEntry_Object = MibTableRow
usdRouterVrfRouteTargetEntry = _UsdRouterVrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1)
)
usdRouterVrfRouteTargetEntry.setIndexNames(
    (0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetRouterIndex"),
    (0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetRouterVrfIndex"),
    (0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetAddrFormat"),
    (0, "Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetRouteTarget"),
)
if mibBuilder.loadTexts:
    usdRouterVrfRouteTargetEntry.setStatus("current")
_UsdRouterVrfRouteTargetRouterIndex_Type = Unsigned32
_UsdRouterVrfRouteTargetRouterIndex_Object = MibTableColumn
usdRouterVrfRouteTargetRouterIndex = _UsdRouterVrfRouteTargetRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 1),
    _UsdRouterVrfRouteTargetRouterIndex_Type()
)
usdRouterVrfRouteTargetRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRouterVrfRouteTargetRouterIndex.setStatus("current")
_UsdRouterVrfRouteTargetRouterVrfIndex_Type = Unsigned32
_UsdRouterVrfRouteTargetRouterVrfIndex_Object = MibTableColumn
usdRouterVrfRouteTargetRouterVrfIndex = _UsdRouterVrfRouteTargetRouterVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 2),
    _UsdRouterVrfRouteTargetRouterVrfIndex_Type()
)
usdRouterVrfRouteTargetRouterVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRouterVrfRouteTargetRouterVrfIndex.setStatus("current")


class _UsdRouterVrfRouteTargetAddrFormat_Type(Integer32):
    """Custom type usdRouterVrfRouteTargetAddrFormat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("routeTargetFormatAsn", 0),
          ("routeTargetFormateIp", 1))
    )


_UsdRouterVrfRouteTargetAddrFormat_Type.__name__ = "Integer32"
_UsdRouterVrfRouteTargetAddrFormat_Object = MibTableColumn
usdRouterVrfRouteTargetAddrFormat = _UsdRouterVrfRouteTargetAddrFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 3),
    _UsdRouterVrfRouteTargetAddrFormat_Type()
)
usdRouterVrfRouteTargetAddrFormat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRouterVrfRouteTargetAddrFormat.setStatus("current")
_UsdRouterVrfRouteTargetRouteTarget_Type = UsdIpPolicyExtendedCommunity
_UsdRouterVrfRouteTargetRouteTarget_Object = MibTableColumn
usdRouterVrfRouteTargetRouteTarget = _UsdRouterVrfRouteTargetRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 4),
    _UsdRouterVrfRouteTargetRouteTarget_Type()
)
usdRouterVrfRouteTargetRouteTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    usdRouterVrfRouteTargetRouteTarget.setStatus("current")


class _UsdRouterVrfRouteTargetType_Type(Integer32):
    """Custom type usdRouterVrfRouteTargetType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("routeTargetBoth", 3),
          ("routeTargetExport", 2),
          ("routeTargetImport", 1),
          ("routeTargetInvalid", 0))
    )


_UsdRouterVrfRouteTargetType_Type.__name__ = "Integer32"
_UsdRouterVrfRouteTargetType_Object = MibTableColumn
usdRouterVrfRouteTargetType = _UsdRouterVrfRouteTargetType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 5),
    _UsdRouterVrfRouteTargetType_Type()
)
usdRouterVrfRouteTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRouterVrfRouteTargetType.setStatus("current")
_UsdRouterVrfRouteTargetRowStatus_Type = RowStatus
_UsdRouterVrfRouteTargetRowStatus_Object = MibTableColumn
usdRouterVrfRouteTargetRowStatus = _UsdRouterVrfRouteTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 6),
    _UsdRouterVrfRouteTargetRowStatus_Type()
)
usdRouterVrfRouteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    usdRouterVrfRouteTargetRowStatus.setStatus("current")
_UsdRouterConformance_ObjectIdentity = ObjectIdentity
usdRouterConformance = _UsdRouterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4)
)
_UsdRouterCompliances_ObjectIdentity = ObjectIdentity
usdRouterCompliances = _UsdRouterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1)
)
_UsdRouterGroups_ObjectIdentity = ObjectIdentity
usdRouterGroups = _UsdRouterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2)
)

# Managed Objects groups

usdRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 1)
)
usdRouterGroup.setObjects(
      *(("Unisphere-Data-ROUTER-MIB", "usdRouterNextRouterIndex"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterName"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterRowStatus"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterProtocolRowStatus"))
)
if mibBuilder.loadTexts:
    usdRouterGroup.setStatus("obsolete")

usdRouterGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 2)
)
usdRouterGroup2.setObjects(
      *(("Unisphere-Data-ROUTER-MIB", "usdRouterNextRouterIndex"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterName"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterRowStatus"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrf"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterProtocolRowStatus"))
)
if mibBuilder.loadTexts:
    usdRouterGroup2.setStatus("obsolete")

usdRouterVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 3)
)
usdRouterVrfGroup.setObjects(
      *(("Unisphere-Data-ROUTER-MIB", "usdRouterVrfImportRouteMap"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfExportRouteMap"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteDistinguisher"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRowStatus"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouterName"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetType"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetRowStatus"))
)
if mibBuilder.loadTexts:
    usdRouterVrfGroup.setStatus("obsolete")

usdRouterGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 4)
)
usdRouterGroup3.setObjects(
      *(("Unisphere-Data-ROUTER-MIB", "usdRouterNextRouterIndex"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterName"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterRowStatus"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrf"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterProtocolRowStatus"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterContextName"))
)
if mibBuilder.loadTexts:
    usdRouterGroup3.setStatus("current")

usdRouterVrfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 5)
)
usdRouterVrfGroup2.setObjects(
      *(("Unisphere-Data-ROUTER-MIB", "usdRouterVrfImportRouteMap"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfExportRouteMap"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteDistinguisher"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRowStatus"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouterName"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouterDescription"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetType"),
        ("Unisphere-Data-ROUTER-MIB", "usdRouterVrfRouteTargetRowStatus"))
)
if mibBuilder.loadTexts:
    usdRouterVrfGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

usdRouterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 1)
)
if mibBuilder.loadTexts:
    usdRouterCompliance.setStatus(
        "obsolete"
    )

usdRouterCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 2)
)
if mibBuilder.loadTexts:
    usdRouterCompliance2.setStatus(
        "obsolete"
    )

usdRouterCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 3)
)
if mibBuilder.loadTexts:
    usdRouterCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Unisphere-Data-ROUTER-MIB",
    **{"UsdNextRouterIndex": UsdNextRouterIndex,
       "UsdRouterProtocolIndex": UsdRouterProtocolIndex,
       "usdRouterMIB": usdRouterMIB,
       "usdRouterObjects": usdRouterObjects,
       "usdRouterNextRouterIndex": usdRouterNextRouterIndex,
       "usdRouterTable": usdRouterTable,
       "usdRouterEntry": usdRouterEntry,
       "usdRouterIndex": usdRouterIndex,
       "usdRouterName": usdRouterName,
       "usdRouterRowStatus": usdRouterRowStatus,
       "usdRouterVrf": usdRouterVrf,
       "usdRouterContextName": usdRouterContextName,
       "usdRouterProtocolTable": usdRouterProtocolTable,
       "usdRouterProtocolEntry": usdRouterProtocolEntry,
       "usdRouterProtocolRouterIndex": usdRouterProtocolRouterIndex,
       "usdRouterProtocolProtocolIndex": usdRouterProtocolProtocolIndex,
       "usdRouterProtocolRowStatus": usdRouterProtocolRowStatus,
       "usdRouterVrfTable": usdRouterVrfTable,
       "usdRouterVrfEntry": usdRouterVrfEntry,
       "usdRouterVrfRouterIndex": usdRouterVrfRouterIndex,
       "usdRouterVrfRouterVrfIndex": usdRouterVrfRouterVrfIndex,
       "usdRouterVrfImportRouteMap": usdRouterVrfImportRouteMap,
       "usdRouterVrfExportRouteMap": usdRouterVrfExportRouteMap,
       "usdRouterVrfRouteDistinguisher": usdRouterVrfRouteDistinguisher,
       "usdRouterVrfRowStatus": usdRouterVrfRowStatus,
       "usdRouterVrfRouterName": usdRouterVrfRouterName,
       "usdRouterVrfRouterDescription": usdRouterVrfRouterDescription,
       "usdRouterVrfRouteTargetTable": usdRouterVrfRouteTargetTable,
       "usdRouterVrfRouteTargetEntry": usdRouterVrfRouteTargetEntry,
       "usdRouterVrfRouteTargetRouterIndex": usdRouterVrfRouteTargetRouterIndex,
       "usdRouterVrfRouteTargetRouterVrfIndex": usdRouterVrfRouteTargetRouterVrfIndex,
       "usdRouterVrfRouteTargetAddrFormat": usdRouterVrfRouteTargetAddrFormat,
       "usdRouterVrfRouteTargetRouteTarget": usdRouterVrfRouteTargetRouteTarget,
       "usdRouterVrfRouteTargetType": usdRouterVrfRouteTargetType,
       "usdRouterVrfRouteTargetRowStatus": usdRouterVrfRouteTargetRowStatus,
       "usdRouterConformance": usdRouterConformance,
       "usdRouterCompliances": usdRouterCompliances,
       "usdRouterCompliance": usdRouterCompliance,
       "usdRouterCompliance2": usdRouterCompliance2,
       "usdRouterCompliance3": usdRouterCompliance3,
       "usdRouterGroups": usdRouterGroups,
       "usdRouterGroup": usdRouterGroup,
       "usdRouterGroup2": usdRouterGroup2,
       "usdRouterVrfGroup": usdRouterVrfGroup,
       "usdRouterGroup3": usdRouterGroup3,
       "usdRouterVrfGroup2": usdRouterVrfGroup2}
)
