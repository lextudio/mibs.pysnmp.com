# SNMP MIB module (CADANT-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CADANT-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:53:09 2024
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

(cadLayer3,) = mibBuilder.importSymbols(
    "CADANT-PRODUCTS-MIB",
    "cadLayer3")

(cadVrIndex,) = mibBuilder.importSymbols(
    "CADANT-VIRTUAL-ROUTER-MIB",
    "cadVrIndex")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(AreaID,
 BigMetric,
 DesignatedRouterPriority,
 HelloRange,
 Metric,
 PositiveInteger,
 RouterID,
 Status,
 TOSType,
 UpToMaxAge) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "BigMetric",
    "DesignatedRouterPriority",
    "HelloRange",
    "Metric",
    "PositiveInteger",
    "RouterID",
    "Status",
    "TOSType",
    "UpToMaxAge")

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

cadOspf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5)
)
cadOspf.setRevisions(
        ("2003-03-01 00:00",
         "2003-06-25 00:00",
         "2004-02-13 00:00",
         "2004-04-12 00:00",
         "2004-06-30 00:00",
         "2004-11-18 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CadOspfRouteGroup_ObjectIdentity = ObjectIdentity
cadOspfRouteGroup = _CadOspfRouteGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 13)
)
_CadOspfIntraArea_ObjectIdentity = ObjectIdentity
cadOspfIntraArea = _CadOspfIntraArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 13, 1)
)
_CadOspfInterArea_ObjectIdentity = ObjectIdentity
cadOspfInterArea = _CadOspfInterArea_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 13, 2)
)
_CadOspfExternalType1_ObjectIdentity = ObjectIdentity
cadOspfExternalType1 = _CadOspfExternalType1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 13, 3)
)
_CadOspfExternalType2_ObjectIdentity = ObjectIdentity
cadOspfExternalType2 = _CadOspfExternalType2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 13, 4)
)
_CadOspfConformance_ObjectIdentity = ObjectIdentity
cadOspfConformance = _CadOspfConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 15)
)
_CadOspfGroups_ObjectIdentity = ObjectIdentity
cadOspfGroups = _CadOspfGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 15, 1)
)
_CadOspfCompliances_ObjectIdentity = ObjectIdentity
cadOspfCompliances = _CadOspfCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 15, 2)
)
_CadOspfNetworkEnableTable_Object = MibTable
cadOspfNetworkEnableTable = _CadOspfNetworkEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 20)
)
if mibBuilder.loadTexts:
    cadOspfNetworkEnableTable.setStatus("current")
_CadOspfNetworkEnableEntry_Object = MibTableRow
cadOspfNetworkEnableEntry = _CadOspfNetworkEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 20, 1)
)
cadOspfNetworkEnableEntry.setIndexNames(
    (0, "CADANT-VIRTUAL-ROUTER-MIB", "cadVrIndex"),
    (0, "CADANT-OSPF-MIB", "cadOspfNetworkEnableIpaddress"),
    (0, "CADANT-OSPF-MIB", "cadOspfNetworkEnableWildcard"),
)
if mibBuilder.loadTexts:
    cadOspfNetworkEnableEntry.setStatus("current")
_CadOspfNetworkEnableIpaddress_Type = IpAddress
_CadOspfNetworkEnableIpaddress_Object = MibTableColumn
cadOspfNetworkEnableIpaddress = _CadOspfNetworkEnableIpaddress_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 20, 1, 1),
    _CadOspfNetworkEnableIpaddress_Type()
)
cadOspfNetworkEnableIpaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadOspfNetworkEnableIpaddress.setStatus("current")
_CadOspfNetworkEnableWildcard_Type = IpAddress
_CadOspfNetworkEnableWildcard_Object = MibTableColumn
cadOspfNetworkEnableWildcard = _CadOspfNetworkEnableWildcard_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 20, 1, 2),
    _CadOspfNetworkEnableWildcard_Type()
)
cadOspfNetworkEnableWildcard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cadOspfNetworkEnableWildcard.setStatus("current")
_CadOspfNetworkEnableAreaId_Type = AreaID
_CadOspfNetworkEnableAreaId_Object = MibTableColumn
cadOspfNetworkEnableAreaId = _CadOspfNetworkEnableAreaId_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 20, 1, 3),
    _CadOspfNetworkEnableAreaId_Type()
)
cadOspfNetworkEnableAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadOspfNetworkEnableAreaId.setStatus("current")
_CadOspfNetworkEnableRowStatus_Type = RowStatus
_CadOspfNetworkEnableRowStatus_Object = MibTableColumn
cadOspfNetworkEnableRowStatus = _CadOspfNetworkEnableRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 4998, 1, 1, 25, 5, 20, 1, 4),
    _CadOspfNetworkEnableRowStatus_Type()
)
cadOspfNetworkEnableRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cadOspfNetworkEnableRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CADANT-OSPF-MIB",
    **{"cadOspf": cadOspf,
       "cadOspfRouteGroup": cadOspfRouteGroup,
       "cadOspfIntraArea": cadOspfIntraArea,
       "cadOspfInterArea": cadOspfInterArea,
       "cadOspfExternalType1": cadOspfExternalType1,
       "cadOspfExternalType2": cadOspfExternalType2,
       "cadOspfConformance": cadOspfConformance,
       "cadOspfGroups": cadOspfGroups,
       "cadOspfCompliances": cadOspfCompliances,
       "cadOspfNetworkEnableTable": cadOspfNetworkEnableTable,
       "cadOspfNetworkEnableEntry": cadOspfNetworkEnableEntry,
       "cadOspfNetworkEnableIpaddress": cadOspfNetworkEnableIpaddress,
       "cadOspfNetworkEnableWildcard": cadOspfNetworkEnableWildcard,
       "cadOspfNetworkEnableAreaId": cadOspfNetworkEnableAreaId,
       "cadOspfNetworkEnableRowStatus": cadOspfNetworkEnableRowStatus}
)
