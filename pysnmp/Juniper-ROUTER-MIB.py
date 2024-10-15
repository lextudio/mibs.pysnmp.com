# SNMP MIB module (Juniper-ROUTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Juniper-ROUTER-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:14:35 2024
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

(JuniIpPolicyExtendedCommunity,
 JuniIpPolicyName) = mibBuilder.importSymbols(
    "Juniper-IP-POLICY-MIB",
    "JuniIpPolicyExtendedCommunity",
    "JuniIpPolicyName")

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(JuniName,) = mibBuilder.importSymbols(
    "Juniper-TC",
    "JuniName")

(SnmpEngineID,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpEngineID")

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


# MODULE-IDENTITY

juniRouterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32)
)
juniRouterMIB.setRevisions(
        ("2004-05-06 20:30",
         "2003-09-24 17:31",
         "2003-05-22 15:52",
         "2003-05-10 20:54",
         "2003-04-24 13:25",
         "2002-05-10 18:16",
         "2001-01-24 18:25",
         "2000-01-21 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniNextRouterIndex(Unsigned32, TextualConvention):
    status = "current"


class JuniRouterProtocolIndex(Integer32, TextualConvention):
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
              28,
              29,
              30,
              31,
              32)
        )
    )
    namedValues = NamedValues(
        *(("bgp", 7),
          ("cops", 20),
          ("dhcpLocalServer", 28),
          ("dhcpProxy", 15),
          ("dhcpRelay", 16),
          ("dhcpv6LocalServer", 31),
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
          ("radiusDisconnect", 30),
          ("radiusProxy", 32),
          ("rip", 10),
          ("snmp", 11),
          ("sscClient", 19),
          ("tacacsPlus", 29),
          ("tcp", 5),
          ("udp", 6))
    )



# MIB Managed Objects in the order of their OIDs

_JuniRouterObjects_ObjectIdentity = ObjectIdentity
juniRouterObjects = _JuniRouterObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1)
)
_JuniRouterNextRouterIndex_Type = JuniNextRouterIndex
_JuniRouterNextRouterIndex_Object = MibScalar
juniRouterNextRouterIndex = _JuniRouterNextRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 1),
    _JuniRouterNextRouterIndex_Type()
)
juniRouterNextRouterIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRouterNextRouterIndex.setStatus("current")
_JuniRouterTable_Object = MibTable
juniRouterTable = _JuniRouterTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2)
)
if mibBuilder.loadTexts:
    juniRouterTable.setStatus("current")
_JuniRouterEntry_Object = MibTableRow
juniRouterEntry = _JuniRouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1)
)
juniRouterEntry.setIndexNames(
    (0, "Juniper-ROUTER-MIB", "juniRouterIndex"),
)
if mibBuilder.loadTexts:
    juniRouterEntry.setStatus("current")
_JuniRouterIndex_Type = Unsigned32
_JuniRouterIndex_Object = MibTableColumn
juniRouterIndex = _JuniRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 1),
    _JuniRouterIndex_Type()
)
juniRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRouterIndex.setStatus("current")
_JuniRouterName_Type = JuniName
_JuniRouterName_Object = MibTableColumn
juniRouterName = _JuniRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 2),
    _JuniRouterName_Type()
)
juniRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterName.setStatus("current")
_JuniRouterRowStatus_Type = RowStatus
_JuniRouterRowStatus_Object = MibTableColumn
juniRouterRowStatus = _JuniRouterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 3),
    _JuniRouterRowStatus_Type()
)
juniRouterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterRowStatus.setStatus("current")
_JuniRouterVrf_Type = TruthValue
_JuniRouterVrf_Object = MibTableColumn
juniRouterVrf = _JuniRouterVrf_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 4),
    _JuniRouterVrf_Type()
)
juniRouterVrf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRouterVrf.setStatus("current")


class _JuniRouterContextName_Type(OctetString):
    """Custom type juniRouterContextName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(7, 14),
    )


_JuniRouterContextName_Type.__name__ = "OctetString"
_JuniRouterContextName_Object = MibTableColumn
juniRouterContextName = _JuniRouterContextName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 5),
    _JuniRouterContextName_Type()
)
juniRouterContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRouterContextName.setStatus("current")
_JuniRouterContextEngineID_Type = SnmpEngineID
_JuniRouterContextEngineID_Object = MibTableColumn
juniRouterContextEngineID = _JuniRouterContextEngineID_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 6),
    _JuniRouterContextEngineID_Type()
)
juniRouterContextEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRouterContextEngineID.setStatus("current")
_JuniRouterSummaryVRFCount_Type = Counter32
_JuniRouterSummaryVRFCount_Object = MibTableColumn
juniRouterSummaryVRFCount = _JuniRouterSummaryVRFCount_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 2, 1, 7),
    _JuniRouterSummaryVRFCount_Type()
)
juniRouterSummaryVRFCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRouterSummaryVRFCount.setStatus("current")
_JuniRouterProtocolTable_Object = MibTable
juniRouterProtocolTable = _JuniRouterProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3)
)
if mibBuilder.loadTexts:
    juniRouterProtocolTable.setStatus("current")
_JuniRouterProtocolEntry_Object = MibTableRow
juniRouterProtocolEntry = _JuniRouterProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1)
)
juniRouterProtocolEntry.setIndexNames(
    (0, "Juniper-ROUTER-MIB", "juniRouterProtocolRouterIndex"),
    (0, "Juniper-ROUTER-MIB", "juniRouterProtocolProtocolIndex"),
)
if mibBuilder.loadTexts:
    juniRouterProtocolEntry.setStatus("current")
_JuniRouterProtocolRouterIndex_Type = Unsigned32
_JuniRouterProtocolRouterIndex_Object = MibTableColumn
juniRouterProtocolRouterIndex = _JuniRouterProtocolRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1, 1),
    _JuniRouterProtocolRouterIndex_Type()
)
juniRouterProtocolRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRouterProtocolRouterIndex.setStatus("current")
_JuniRouterProtocolProtocolIndex_Type = JuniRouterProtocolIndex
_JuniRouterProtocolProtocolIndex_Object = MibTableColumn
juniRouterProtocolProtocolIndex = _JuniRouterProtocolProtocolIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1, 2),
    _JuniRouterProtocolProtocolIndex_Type()
)
juniRouterProtocolProtocolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRouterProtocolProtocolIndex.setStatus("current")
_JuniRouterProtocolRowStatus_Type = RowStatus
_JuniRouterProtocolRowStatus_Object = MibTableColumn
juniRouterProtocolRowStatus = _JuniRouterProtocolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 3, 1, 3),
    _JuniRouterProtocolRowStatus_Type()
)
juniRouterProtocolRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRouterProtocolRowStatus.setStatus("current")
_JuniRouterVrfTable_Object = MibTable
juniRouterVrfTable = _JuniRouterVrfTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4)
)
if mibBuilder.loadTexts:
    juniRouterVrfTable.setStatus("current")
_JuniRouterVrfEntry_Object = MibTableRow
juniRouterVrfEntry = _JuniRouterVrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1)
)
juniRouterVrfEntry.setIndexNames(
    (0, "Juniper-ROUTER-MIB", "juniRouterVrfRouterIndex"),
    (0, "Juniper-ROUTER-MIB", "juniRouterVrfRouterVrfIndex"),
)
if mibBuilder.loadTexts:
    juniRouterVrfEntry.setStatus("current")
_JuniRouterVrfRouterIndex_Type = Unsigned32
_JuniRouterVrfRouterIndex_Object = MibTableColumn
juniRouterVrfRouterIndex = _JuniRouterVrfRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 1),
    _JuniRouterVrfRouterIndex_Type()
)
juniRouterVrfRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRouterVrfRouterIndex.setStatus("current")
_JuniRouterVrfRouterVrfIndex_Type = Unsigned32
_JuniRouterVrfRouterVrfIndex_Object = MibTableColumn
juniRouterVrfRouterVrfIndex = _JuniRouterVrfRouterVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 2),
    _JuniRouterVrfRouterVrfIndex_Type()
)
juniRouterVrfRouterVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRouterVrfRouterVrfIndex.setStatus("current")
_JuniRouterVrfIpv4UnicastImportRouteMap_Type = JuniIpPolicyName
_JuniRouterVrfIpv4UnicastImportRouteMap_Object = MibTableColumn
juniRouterVrfIpv4UnicastImportRouteMap = _JuniRouterVrfIpv4UnicastImportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 3),
    _JuniRouterVrfIpv4UnicastImportRouteMap_Type()
)
juniRouterVrfIpv4UnicastImportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv4UnicastImportRouteMap.setStatus("current")
_JuniRouterVrfIpv4UnicastExportRouteMap_Type = JuniIpPolicyName
_JuniRouterVrfIpv4UnicastExportRouteMap_Object = MibTableColumn
juniRouterVrfIpv4UnicastExportRouteMap = _JuniRouterVrfIpv4UnicastExportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 4),
    _JuniRouterVrfIpv4UnicastExportRouteMap_Type()
)
juniRouterVrfIpv4UnicastExportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv4UnicastExportRouteMap.setStatus("current")
_JuniRouterVrfRouteDistinguisher_Type = JuniIpPolicyExtendedCommunity
_JuniRouterVrfRouteDistinguisher_Object = MibTableColumn
juniRouterVrfRouteDistinguisher = _JuniRouterVrfRouteDistinguisher_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 5),
    _JuniRouterVrfRouteDistinguisher_Type()
)
juniRouterVrfRouteDistinguisher.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfRouteDistinguisher.setStatus("current")
_JuniRouterVrfRowStatus_Type = RowStatus
_JuniRouterVrfRowStatus_Object = MibTableColumn
juniRouterVrfRowStatus = _JuniRouterVrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 7),
    _JuniRouterVrfRowStatus_Type()
)
juniRouterVrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfRowStatus.setStatus("current")
_JuniRouterVrfRouterName_Type = JuniName
_JuniRouterVrfRouterName_Object = MibTableColumn
juniRouterVrfRouterName = _JuniRouterVrfRouterName_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 8),
    _JuniRouterVrfRouterName_Type()
)
juniRouterVrfRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfRouterName.setStatus("current")


class _JuniRouterVrfRouterDescription_Type(DisplayString):
    """Custom type juniRouterVrfRouterDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_JuniRouterVrfRouterDescription_Type.__name__ = "DisplayString"
_JuniRouterVrfRouterDescription_Object = MibTableColumn
juniRouterVrfRouterDescription = _JuniRouterVrfRouterDescription_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 9),
    _JuniRouterVrfRouterDescription_Type()
)
juniRouterVrfRouterDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfRouterDescription.setStatus("current")
_JuniRouterVrfIpv4UnicastGlobalExportRouteMap_Type = JuniIpPolicyName
_JuniRouterVrfIpv4UnicastGlobalExportRouteMap_Object = MibTableColumn
juniRouterVrfIpv4UnicastGlobalExportRouteMap = _JuniRouterVrfIpv4UnicastGlobalExportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 10),
    _JuniRouterVrfIpv4UnicastGlobalExportRouteMap_Type()
)
juniRouterVrfIpv4UnicastGlobalExportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv4UnicastGlobalExportRouteMap.setStatus("current")


class _JuniRouterVrfIpv4UnicastExportRouteMapFilter_Type(TruthValue):
    """Custom type juniRouterVrfIpv4UnicastExportRouteMapFilter based on TruthValue"""


_JuniRouterVrfIpv4UnicastExportRouteMapFilter_Object = MibTableColumn
juniRouterVrfIpv4UnicastExportRouteMapFilter = _JuniRouterVrfIpv4UnicastExportRouteMapFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 11),
    _JuniRouterVrfIpv4UnicastExportRouteMapFilter_Type()
)
juniRouterVrfIpv4UnicastExportRouteMapFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv4UnicastExportRouteMapFilter.setStatus("current")
_JuniRouterVrfIpv6UnicastImportRouteMap_Type = JuniIpPolicyName
_JuniRouterVrfIpv6UnicastImportRouteMap_Object = MibTableColumn
juniRouterVrfIpv6UnicastImportRouteMap = _JuniRouterVrfIpv6UnicastImportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 12),
    _JuniRouterVrfIpv6UnicastImportRouteMap_Type()
)
juniRouterVrfIpv6UnicastImportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv6UnicastImportRouteMap.setStatus("current")
_JuniRouterVrfIpv6UnicastExportRouteMap_Type = JuniIpPolicyName
_JuniRouterVrfIpv6UnicastExportRouteMap_Object = MibTableColumn
juniRouterVrfIpv6UnicastExportRouteMap = _JuniRouterVrfIpv6UnicastExportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 13),
    _JuniRouterVrfIpv6UnicastExportRouteMap_Type()
)
juniRouterVrfIpv6UnicastExportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv6UnicastExportRouteMap.setStatus("current")
_JuniRouterVrfIpv6UnicastGlobalExportRouteMap_Type = JuniIpPolicyName
_JuniRouterVrfIpv6UnicastGlobalExportRouteMap_Object = MibTableColumn
juniRouterVrfIpv6UnicastGlobalExportRouteMap = _JuniRouterVrfIpv6UnicastGlobalExportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 14),
    _JuniRouterVrfIpv6UnicastGlobalExportRouteMap_Type()
)
juniRouterVrfIpv6UnicastGlobalExportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv6UnicastGlobalExportRouteMap.setStatus("current")


class _JuniRouterVrfIpv6UnicastExportRouteMapFilter_Type(TruthValue):
    """Custom type juniRouterVrfIpv6UnicastExportRouteMapFilter based on TruthValue"""


_JuniRouterVrfIpv6UnicastExportRouteMapFilter_Object = MibTableColumn
juniRouterVrfIpv6UnicastExportRouteMapFilter = _JuniRouterVrfIpv6UnicastExportRouteMapFilter_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 15),
    _JuniRouterVrfIpv6UnicastExportRouteMapFilter_Type()
)
juniRouterVrfIpv6UnicastExportRouteMapFilter.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv6UnicastExportRouteMapFilter.setStatus("current")
_JuniRouterVrfIpv4UnicastGlobalImportRouteMap_Type = JuniIpPolicyName
_JuniRouterVrfIpv4UnicastGlobalImportRouteMap_Object = MibTableColumn
juniRouterVrfIpv4UnicastGlobalImportRouteMap = _JuniRouterVrfIpv4UnicastGlobalImportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 16),
    _JuniRouterVrfIpv4UnicastGlobalImportRouteMap_Type()
)
juniRouterVrfIpv4UnicastGlobalImportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv4UnicastGlobalImportRouteMap.setStatus("current")


class _JuniRouterVrfIpv4UnicastGlobalImportMaxRoutes_Type(Unsigned32):
    """Custom type juniRouterVrfIpv4UnicastGlobalImportMaxRoutes based on Unsigned32"""
    defaultValue = 100


_JuniRouterVrfIpv4UnicastGlobalImportMaxRoutes_Object = MibTableColumn
juniRouterVrfIpv4UnicastGlobalImportMaxRoutes = _JuniRouterVrfIpv4UnicastGlobalImportMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 17),
    _JuniRouterVrfIpv4UnicastGlobalImportMaxRoutes_Type()
)
juniRouterVrfIpv4UnicastGlobalImportMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv4UnicastGlobalImportMaxRoutes.setStatus("current")
_JuniRouterVrfIpv6UnicastGlobalImportRouteMap_Type = JuniIpPolicyName
_JuniRouterVrfIpv6UnicastGlobalImportRouteMap_Object = MibTableColumn
juniRouterVrfIpv6UnicastGlobalImportRouteMap = _JuniRouterVrfIpv6UnicastGlobalImportRouteMap_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 18),
    _JuniRouterVrfIpv6UnicastGlobalImportRouteMap_Type()
)
juniRouterVrfIpv6UnicastGlobalImportRouteMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv6UnicastGlobalImportRouteMap.setStatus("current")


class _JuniRouterVrfIpv6UnicastGlobalImportMaxRoutes_Type(Unsigned32):
    """Custom type juniRouterVrfIpv6UnicastGlobalImportMaxRoutes based on Unsigned32"""
    defaultValue = 100


_JuniRouterVrfIpv6UnicastGlobalImportMaxRoutes_Object = MibTableColumn
juniRouterVrfIpv6UnicastGlobalImportMaxRoutes = _JuniRouterVrfIpv6UnicastGlobalImportMaxRoutes_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 4, 1, 19),
    _JuniRouterVrfIpv6UnicastGlobalImportMaxRoutes_Type()
)
juniRouterVrfIpv6UnicastGlobalImportMaxRoutes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfIpv6UnicastGlobalImportMaxRoutes.setStatus("current")
_JuniRouterVrfRouteTargetTable_Object = MibTable
juniRouterVrfRouteTargetTable = _JuniRouterVrfRouteTargetTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5)
)
if mibBuilder.loadTexts:
    juniRouterVrfRouteTargetTable.setStatus("current")
_JuniRouterVrfRouteTargetEntry_Object = MibTableRow
juniRouterVrfRouteTargetEntry = _JuniRouterVrfRouteTargetEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1)
)
juniRouterVrfRouteTargetEntry.setIndexNames(
    (0, "Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetRouterIndex"),
    (0, "Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetRouterVrfIndex"),
    (0, "Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetAddrFormat"),
    (0, "Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetRouteTarget"),
)
if mibBuilder.loadTexts:
    juniRouterVrfRouteTargetEntry.setStatus("current")
_JuniRouterVrfRouteTargetRouterIndex_Type = Unsigned32
_JuniRouterVrfRouteTargetRouterIndex_Object = MibTableColumn
juniRouterVrfRouteTargetRouterIndex = _JuniRouterVrfRouteTargetRouterIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 1),
    _JuniRouterVrfRouteTargetRouterIndex_Type()
)
juniRouterVrfRouteTargetRouterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRouterVrfRouteTargetRouterIndex.setStatus("current")
_JuniRouterVrfRouteTargetRouterVrfIndex_Type = Unsigned32
_JuniRouterVrfRouteTargetRouterVrfIndex_Object = MibTableColumn
juniRouterVrfRouteTargetRouterVrfIndex = _JuniRouterVrfRouteTargetRouterVrfIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 2),
    _JuniRouterVrfRouteTargetRouterVrfIndex_Type()
)
juniRouterVrfRouteTargetRouterVrfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRouterVrfRouteTargetRouterVrfIndex.setStatus("current")


class _JuniRouterVrfRouteTargetAddrFormat_Type(Integer32):
    """Custom type juniRouterVrfRouteTargetAddrFormat based on Integer32"""
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


_JuniRouterVrfRouteTargetAddrFormat_Type.__name__ = "Integer32"
_JuniRouterVrfRouteTargetAddrFormat_Object = MibTableColumn
juniRouterVrfRouteTargetAddrFormat = _JuniRouterVrfRouteTargetAddrFormat_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 3),
    _JuniRouterVrfRouteTargetAddrFormat_Type()
)
juniRouterVrfRouteTargetAddrFormat.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRouterVrfRouteTargetAddrFormat.setStatus("current")
_JuniRouterVrfRouteTargetRouteTarget_Type = JuniIpPolicyExtendedCommunity
_JuniRouterVrfRouteTargetRouteTarget_Object = MibTableColumn
juniRouterVrfRouteTargetRouteTarget = _JuniRouterVrfRouteTargetRouteTarget_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 4),
    _JuniRouterVrfRouteTargetRouteTarget_Type()
)
juniRouterVrfRouteTargetRouteTarget.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRouterVrfRouteTargetRouteTarget.setStatus("current")


class _JuniRouterVrfRouteTargetType_Type(Integer32):
    """Custom type juniRouterVrfRouteTargetType based on Integer32"""
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


_JuniRouterVrfRouteTargetType_Type.__name__ = "Integer32"
_JuniRouterVrfRouteTargetType_Object = MibTableColumn
juniRouterVrfRouteTargetType = _JuniRouterVrfRouteTargetType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 5),
    _JuniRouterVrfRouteTargetType_Type()
)
juniRouterVrfRouteTargetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfRouteTargetType.setStatus("current")
_JuniRouterVrfRouteTargetRowStatus_Type = RowStatus
_JuniRouterVrfRouteTargetRowStatus_Object = MibTableColumn
juniRouterVrfRouteTargetRowStatus = _JuniRouterVrfRouteTargetRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 5, 1, 6),
    _JuniRouterVrfRouteTargetRowStatus_Type()
)
juniRouterVrfRouteTargetRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    juniRouterVrfRouteTargetRowStatus.setStatus("current")
_JuniRouterSummaryCounts_ObjectIdentity = ObjectIdentity
juniRouterSummaryCounts = _JuniRouterSummaryCounts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 6)
)
_JuniRouterSummaryScalars_ObjectIdentity = ObjectIdentity
juniRouterSummaryScalars = _JuniRouterSummaryScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 6, 1)
)
_JuniRouterSummaryNonParentVRsConfigured_Type = Counter32
_JuniRouterSummaryNonParentVRsConfigured_Object = MibScalar
juniRouterSummaryNonParentVRsConfigured = _JuniRouterSummaryNonParentVRsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 6, 1, 1),
    _JuniRouterSummaryNonParentVRsConfigured_Type()
)
juniRouterSummaryNonParentVRsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRouterSummaryNonParentVRsConfigured.setStatus("current")
_JuniRouterSummaryParentVRsConfigured_Type = Counter32
_JuniRouterSummaryParentVRsConfigured_Object = MibScalar
juniRouterSummaryParentVRsConfigured = _JuniRouterSummaryParentVRsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 6, 1, 2),
    _JuniRouterSummaryParentVRsConfigured_Type()
)
juniRouterSummaryParentVRsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRouterSummaryParentVRsConfigured.setStatus("current")
_JuniRouterSummaryVRFsConfigured_Type = Counter32
_JuniRouterSummaryVRFsConfigured_Object = MibScalar
juniRouterSummaryVRFsConfigured = _JuniRouterSummaryVRFsConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 6, 1, 3),
    _JuniRouterSummaryVRFsConfigured_Type()
)
juniRouterSummaryVRFsConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRouterSummaryVRFsConfigured.setStatus("current")
_JuniRouterSummaryTotalConfigured_Type = Counter32
_JuniRouterSummaryTotalConfigured_Object = MibScalar
juniRouterSummaryTotalConfigured = _JuniRouterSummaryTotalConfigured_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 1, 6, 1, 4),
    _JuniRouterSummaryTotalConfigured_Type()
)
juniRouterSummaryTotalConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRouterSummaryTotalConfigured.setStatus("current")
_JuniRouterConformance_ObjectIdentity = ObjectIdentity
juniRouterConformance = _JuniRouterConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4)
)
_JuniRouterCompliances_ObjectIdentity = ObjectIdentity
juniRouterCompliances = _JuniRouterCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1)
)
_JuniRouterGroups_ObjectIdentity = ObjectIdentity
juniRouterGroups = _JuniRouterGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2)
)

# Managed Objects groups

juniRouterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 1)
)
juniRouterGroup.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterNextRouterIndex"),
        ("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-ROUTER-MIB", "juniRouterRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterProtocolRowStatus"))
)
if mibBuilder.loadTexts:
    juniRouterGroup.setStatus("obsolete")

juniRouterGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 2)
)
juniRouterGroup2.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterNextRouterIndex"),
        ("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-ROUTER-MIB", "juniRouterRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterVrf"),
        ("Juniper-ROUTER-MIB", "juniRouterProtocolRowStatus"))
)
if mibBuilder.loadTexts:
    juniRouterGroup2.setStatus("obsolete")

juniRouterVrfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 3)
)
juniRouterVrfGroup.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastImportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastExportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteDistinguisher"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouterName"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetType"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetRowStatus"))
)
if mibBuilder.loadTexts:
    juniRouterVrfGroup.setStatus("obsolete")

juniRouterGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 4)
)
juniRouterGroup3.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterNextRouterIndex"),
        ("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-ROUTER-MIB", "juniRouterRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterVrf"),
        ("Juniper-ROUTER-MIB", "juniRouterProtocolRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterContextName"))
)
if mibBuilder.loadTexts:
    juniRouterGroup3.setStatus("obsolete")

juniRouterVrfGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 5)
)
juniRouterVrfGroup2.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastImportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastExportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteDistinguisher"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouterName"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouterDescription"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetType"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetRowStatus"))
)
if mibBuilder.loadTexts:
    juniRouterVrfGroup2.setStatus("obsolete")

juniRouterGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 6)
)
juniRouterGroup4.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterNextRouterIndex"),
        ("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-ROUTER-MIB", "juniRouterRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterVrf"),
        ("Juniper-ROUTER-MIB", "juniRouterProtocolRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterContextName"),
        ("Juniper-ROUTER-MIB", "juniRouterContextEngineID"))
)
if mibBuilder.loadTexts:
    juniRouterGroup4.setStatus("obsolete")

juniRouterVrfGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 7)
)
juniRouterVrfGroup3.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastImportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastExportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteDistinguisher"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouterName"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouterDescription"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastGlobalExportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastExportRouteMapFilter"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetType"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetRowStatus"))
)
if mibBuilder.loadTexts:
    juniRouterVrfGroup3.setStatus("obsolete")

juniRouterGroup5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 8)
)
juniRouterGroup5.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterNextRouterIndex"),
        ("Juniper-ROUTER-MIB", "juniRouterName"),
        ("Juniper-ROUTER-MIB", "juniRouterRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterVrf"),
        ("Juniper-ROUTER-MIB", "juniRouterProtocolRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterContextName"),
        ("Juniper-ROUTER-MIB", "juniRouterContextEngineID"),
        ("Juniper-ROUTER-MIB", "juniRouterSummaryVRFCount"))
)
if mibBuilder.loadTexts:
    juniRouterGroup5.setStatus("current")

juniRouterSummaryScalarsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 9)
)
juniRouterSummaryScalarsGroup.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterSummaryNonParentVRsConfigured"),
        ("Juniper-ROUTER-MIB", "juniRouterSummaryParentVRsConfigured"),
        ("Juniper-ROUTER-MIB", "juniRouterSummaryVRFsConfigured"),
        ("Juniper-ROUTER-MIB", "juniRouterSummaryTotalConfigured"))
)
if mibBuilder.loadTexts:
    juniRouterSummaryScalarsGroup.setStatus("current")

juniRouterVrfGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 2, 10)
)
juniRouterVrfGroup4.setObjects(
      *(("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastImportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastExportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteDistinguisher"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRowStatus"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouterName"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouterDescription"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastGlobalExportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastExportRouteMapFilter"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv6UnicastImportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv6UnicastExportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv6UnicastGlobalExportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv6UnicastExportRouteMapFilter"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastGlobalImportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv4UnicastGlobalImportMaxRoutes"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv6UnicastGlobalImportRouteMap"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfIpv6UnicastGlobalImportMaxRoutes"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetType"),
        ("Juniper-ROUTER-MIB", "juniRouterVrfRouteTargetRowStatus"))
)
if mibBuilder.loadTexts:
    juniRouterVrfGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

juniRouterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 1)
)
if mibBuilder.loadTexts:
    juniRouterCompliance.setStatus(
        "obsolete"
    )

juniRouterCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 2)
)
if mibBuilder.loadTexts:
    juniRouterCompliance2.setStatus(
        "obsolete"
    )

juniRouterCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 3)
)
if mibBuilder.loadTexts:
    juniRouterCompliance3.setStatus(
        "obsolete"
    )

juniRouterCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 4)
)
if mibBuilder.loadTexts:
    juniRouterCompliance4.setStatus(
        "obsolete"
    )

juniRouterCompliance5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 5)
)
if mibBuilder.loadTexts:
    juniRouterCompliance5.setStatus(
        "obsolete"
    )

juniRouterCompliance6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 7)
)
if mibBuilder.loadTexts:
    juniRouterCompliance6.setStatus(
        "obsolete"
    )

juniRouterCompliance7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 32, 4, 1, 8)
)
if mibBuilder.loadTexts:
    juniRouterCompliance7.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-ROUTER-MIB",
    **{"JuniNextRouterIndex": JuniNextRouterIndex,
       "JuniRouterProtocolIndex": JuniRouterProtocolIndex,
       "juniRouterMIB": juniRouterMIB,
       "juniRouterObjects": juniRouterObjects,
       "juniRouterNextRouterIndex": juniRouterNextRouterIndex,
       "juniRouterTable": juniRouterTable,
       "juniRouterEntry": juniRouterEntry,
       "juniRouterIndex": juniRouterIndex,
       "juniRouterName": juniRouterName,
       "juniRouterRowStatus": juniRouterRowStatus,
       "juniRouterVrf": juniRouterVrf,
       "juniRouterContextName": juniRouterContextName,
       "juniRouterContextEngineID": juniRouterContextEngineID,
       "juniRouterSummaryVRFCount": juniRouterSummaryVRFCount,
       "juniRouterProtocolTable": juniRouterProtocolTable,
       "juniRouterProtocolEntry": juniRouterProtocolEntry,
       "juniRouterProtocolRouterIndex": juniRouterProtocolRouterIndex,
       "juniRouterProtocolProtocolIndex": juniRouterProtocolProtocolIndex,
       "juniRouterProtocolRowStatus": juniRouterProtocolRowStatus,
       "juniRouterVrfTable": juniRouterVrfTable,
       "juniRouterVrfEntry": juniRouterVrfEntry,
       "juniRouterVrfRouterIndex": juniRouterVrfRouterIndex,
       "juniRouterVrfRouterVrfIndex": juniRouterVrfRouterVrfIndex,
       "juniRouterVrfIpv4UnicastImportRouteMap": juniRouterVrfIpv4UnicastImportRouteMap,
       "juniRouterVrfIpv4UnicastExportRouteMap": juniRouterVrfIpv4UnicastExportRouteMap,
       "juniRouterVrfRouteDistinguisher": juniRouterVrfRouteDistinguisher,
       "juniRouterVrfRowStatus": juniRouterVrfRowStatus,
       "juniRouterVrfRouterName": juniRouterVrfRouterName,
       "juniRouterVrfRouterDescription": juniRouterVrfRouterDescription,
       "juniRouterVrfIpv4UnicastGlobalExportRouteMap": juniRouterVrfIpv4UnicastGlobalExportRouteMap,
       "juniRouterVrfIpv4UnicastExportRouteMapFilter": juniRouterVrfIpv4UnicastExportRouteMapFilter,
       "juniRouterVrfIpv6UnicastImportRouteMap": juniRouterVrfIpv6UnicastImportRouteMap,
       "juniRouterVrfIpv6UnicastExportRouteMap": juniRouterVrfIpv6UnicastExportRouteMap,
       "juniRouterVrfIpv6UnicastGlobalExportRouteMap": juniRouterVrfIpv6UnicastGlobalExportRouteMap,
       "juniRouterVrfIpv6UnicastExportRouteMapFilter": juniRouterVrfIpv6UnicastExportRouteMapFilter,
       "juniRouterVrfIpv4UnicastGlobalImportRouteMap": juniRouterVrfIpv4UnicastGlobalImportRouteMap,
       "juniRouterVrfIpv4UnicastGlobalImportMaxRoutes": juniRouterVrfIpv4UnicastGlobalImportMaxRoutes,
       "juniRouterVrfIpv6UnicastGlobalImportRouteMap": juniRouterVrfIpv6UnicastGlobalImportRouteMap,
       "juniRouterVrfIpv6UnicastGlobalImportMaxRoutes": juniRouterVrfIpv6UnicastGlobalImportMaxRoutes,
       "juniRouterVrfRouteTargetTable": juniRouterVrfRouteTargetTable,
       "juniRouterVrfRouteTargetEntry": juniRouterVrfRouteTargetEntry,
       "juniRouterVrfRouteTargetRouterIndex": juniRouterVrfRouteTargetRouterIndex,
       "juniRouterVrfRouteTargetRouterVrfIndex": juniRouterVrfRouteTargetRouterVrfIndex,
       "juniRouterVrfRouteTargetAddrFormat": juniRouterVrfRouteTargetAddrFormat,
       "juniRouterVrfRouteTargetRouteTarget": juniRouterVrfRouteTargetRouteTarget,
       "juniRouterVrfRouteTargetType": juniRouterVrfRouteTargetType,
       "juniRouterVrfRouteTargetRowStatus": juniRouterVrfRouteTargetRowStatus,
       "juniRouterSummaryCounts": juniRouterSummaryCounts,
       "juniRouterSummaryScalars": juniRouterSummaryScalars,
       "juniRouterSummaryNonParentVRsConfigured": juniRouterSummaryNonParentVRsConfigured,
       "juniRouterSummaryParentVRsConfigured": juniRouterSummaryParentVRsConfigured,
       "juniRouterSummaryVRFsConfigured": juniRouterSummaryVRFsConfigured,
       "juniRouterSummaryTotalConfigured": juniRouterSummaryTotalConfigured,
       "juniRouterConformance": juniRouterConformance,
       "juniRouterCompliances": juniRouterCompliances,
       "juniRouterCompliance": juniRouterCompliance,
       "juniRouterCompliance2": juniRouterCompliance2,
       "juniRouterCompliance3": juniRouterCompliance3,
       "juniRouterCompliance4": juniRouterCompliance4,
       "juniRouterCompliance5": juniRouterCompliance5,
       "juniRouterCompliance6": juniRouterCompliance6,
       "juniRouterCompliance7": juniRouterCompliance7,
       "juniRouterGroups": juniRouterGroups,
       "juniRouterGroup": juniRouterGroup,
       "juniRouterGroup2": juniRouterGroup2,
       "juniRouterVrfGroup": juniRouterVrfGroup,
       "juniRouterGroup3": juniRouterGroup3,
       "juniRouterVrfGroup2": juniRouterVrfGroup2,
       "juniRouterGroup4": juniRouterGroup4,
       "juniRouterVrfGroup3": juniRouterVrfGroup3,
       "juniRouterGroup5": juniRouterGroup5,
       "juniRouterSummaryScalarsGroup": juniRouterSummaryScalarsGroup,
       "juniRouterVrfGroup4": juniRouterVrfGroup4}
)
