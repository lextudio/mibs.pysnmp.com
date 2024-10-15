# SNMP MIB module (EBN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/EBN-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:36:25 2024
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

(SnaControlPointName,) = mibBuilder.importSymbols(
    "APPN-MIB",
    "SnaControlPointName")

(snanauMIB,) = mibBuilder.importSymbols(
    "SNA-NAU-MIB",
    "snanauMIB")

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

ebnMIB = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SnaNAUWildcardName(DisplayString, TextualConvention):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )



# MIB Managed Objects in the order of their OIDs

_EbnObjects_ObjectIdentity = ObjectIdentity
ebnObjects = _EbnObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7, 1)
)
_EbnDir_ObjectIdentity = ObjectIdentity
ebnDir = _EbnDir_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 1)
)
_EbnDirTable_Object = MibTable
ebnDirTable = _EbnDirTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ebnDirTable.setStatus("current")
_EbnDirEntry_Object = MibTableRow
ebnDirEntry = _EbnDirEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 1, 1, 1)
)
ebnDirEntry.setIndexNames(
    (0, "EBN-MIB", "ebnDirLuName"),
)
if mibBuilder.loadTexts:
    ebnDirEntry.setStatus("current")
_EbnDirLuName_Type = SnaNAUWildcardName
_EbnDirLuName_Object = MibTableColumn
ebnDirLuName = _EbnDirLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 1, 1, 1, 1),
    _EbnDirLuName_Type()
)
ebnDirLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ebnDirLuName.setStatus("current")


class _EbnDirSubnetAffiliation_Type(Integer32):
    """Custom type ebnDirSubnetAffiliation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("native", 1),
          ("nonNative", 2),
          ("subarea", 3))
    )


_EbnDirSubnetAffiliation_Type.__name__ = "Integer32"
_EbnDirSubnetAffiliation_Object = MibTableColumn
ebnDirSubnetAffiliation = _EbnDirSubnetAffiliation_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 1, 1, 1, 2),
    _EbnDirSubnetAffiliation_Type()
)
ebnDirSubnetAffiliation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnDirSubnetAffiliation.setStatus("current")
_EbnIsRscv_ObjectIdentity = ObjectIdentity
ebnIsRscv = _EbnIsRscv_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 2)
)
_EbnIsRscvTable_Object = MibTable
ebnIsRscvTable = _EbnIsRscvTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ebnIsRscvTable.setStatus("current")
_EbnIsRscvEntry_Object = MibTableRow
ebnIsRscvEntry = _EbnIsRscvEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1, 1)
)
ebnIsRscvEntry.setIndexNames(
    (0, "EBN-MIB", "ebnIsRscvCpName"),
    (0, "EBN-MIB", "ebnIsRscvPcid"),
)
if mibBuilder.loadTexts:
    ebnIsRscvEntry.setStatus("current")
_EbnIsRscvCpName_Type = SnaControlPointName
_EbnIsRscvCpName_Object = MibTableColumn
ebnIsRscvCpName = _EbnIsRscvCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1, 1, 1),
    _EbnIsRscvCpName_Type()
)
ebnIsRscvCpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ebnIsRscvCpName.setStatus("current")


class _EbnIsRscvPcid_Type(OctetString):
    """Custom type ebnIsRscvPcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_EbnIsRscvPcid_Type.__name__ = "OctetString"
_EbnIsRscvPcid_Object = MibTableColumn
ebnIsRscvPcid = _EbnIsRscvPcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1, 1, 2),
    _EbnIsRscvPcid_Type()
)
ebnIsRscvPcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ebnIsRscvPcid.setStatus("current")


class _EbnIsRscvDestinationRoute_Type(OctetString):
    """Custom type ebnIsRscvDestinationRoute based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EbnIsRscvDestinationRoute_Type.__name__ = "OctetString"
_EbnIsRscvDestinationRoute_Object = MibTableColumn
ebnIsRscvDestinationRoute = _EbnIsRscvDestinationRoute_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1, 1, 3),
    _EbnIsRscvDestinationRoute_Type()
)
ebnIsRscvDestinationRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnIsRscvDestinationRoute.setStatus("current")


class _EbnIsRscvDestinationCos_Type(DisplayString):
    """Custom type ebnIsRscvDestinationCos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_EbnIsRscvDestinationCos_Type.__name__ = "DisplayString"
_EbnIsRscvDestinationCos_Object = MibTableColumn
ebnIsRscvDestinationCos = _EbnIsRscvDestinationCos_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 2, 1, 1, 4),
    _EbnIsRscvDestinationCos_Type()
)
ebnIsRscvDestinationCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnIsRscvDestinationCos.setStatus("current")
_EbnDirConfig_ObjectIdentity = ObjectIdentity
ebnDirConfig = _EbnDirConfig_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 3)
)
_EbnSearchCacheTime_Type = Unsigned32
_EbnSearchCacheTime_Object = MibScalar
ebnSearchCacheTime = _EbnSearchCacheTime_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 3, 1),
    _EbnSearchCacheTime_Type()
)
ebnSearchCacheTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnSearchCacheTime.setStatus("current")
if mibBuilder.loadTexts:
    ebnSearchCacheTime.setUnits("minutes")
_EbnMaxSearchCache_Type = Unsigned32
_EbnMaxSearchCache_Object = MibScalar
ebnMaxSearchCache = _EbnMaxSearchCache_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 3, 2),
    _EbnMaxSearchCache_Type()
)
ebnMaxSearchCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnMaxSearchCache.setStatus("current")
if mibBuilder.loadTexts:
    ebnMaxSearchCache.setUnits("entries")
_EbnDefaultSubnetVisitCount_Type = Unsigned32
_EbnDefaultSubnetVisitCount_Object = MibScalar
ebnDefaultSubnetVisitCount = _EbnDefaultSubnetVisitCount_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 3, 3),
    _EbnDefaultSubnetVisitCount_Type()
)
ebnDefaultSubnetVisitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnDefaultSubnetVisitCount.setStatus("current")
if mibBuilder.loadTexts:
    ebnDefaultSubnetVisitCount.setUnits("topology subnetworks")
_EbnCOS_ObjectIdentity = ObjectIdentity
ebnCOS = _EbnCOS_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 4)
)
_EbnCosMapTable_Object = MibTable
ebnCosMapTable = _EbnCosMapTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ebnCosMapTable.setStatus("current")
_EbnCosMapEntry_Object = MibTableRow
ebnCosMapEntry = _EbnCosMapEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 4, 1, 1)
)
ebnCosMapEntry.setIndexNames(
    (0, "EBN-MIB", "ebnCosMapCpName"),
    (0, "EBN-MIB", "ebnCosMapNonNativeCos"),
)
if mibBuilder.loadTexts:
    ebnCosMapEntry.setStatus("current")
_EbnCosMapCpName_Type = SnaNAUWildcardName
_EbnCosMapCpName_Object = MibTableColumn
ebnCosMapCpName = _EbnCosMapCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 4, 1, 1, 1),
    _EbnCosMapCpName_Type()
)
ebnCosMapCpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ebnCosMapCpName.setStatus("current")


class _EbnCosMapNonNativeCos_Type(DisplayString):
    """Custom type ebnCosMapNonNativeCos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_EbnCosMapNonNativeCos_Type.__name__ = "DisplayString"
_EbnCosMapNonNativeCos_Object = MibTableColumn
ebnCosMapNonNativeCos = _EbnCosMapNonNativeCos_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 4, 1, 1, 2),
    _EbnCosMapNonNativeCos_Type()
)
ebnCosMapNonNativeCos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ebnCosMapNonNativeCos.setStatus("current")


class _EbnCosMapNativeCos_Type(DisplayString):
    """Custom type ebnCosMapNativeCos based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_EbnCosMapNativeCos_Type.__name__ = "DisplayString"
_EbnCosMapNativeCos_Object = MibTableColumn
ebnCosMapNativeCos = _EbnCosMapNativeCos_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 4, 1, 1, 3),
    _EbnCosMapNativeCos_Type()
)
ebnCosMapNativeCos.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnCosMapNativeCos.setStatus("current")
_EbnSubnetRoutingList_ObjectIdentity = ObjectIdentity
ebnSubnetRoutingList = _EbnSubnetRoutingList_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5)
)
_EbnSubnetSearchTable_Object = MibTable
ebnSubnetSearchTable = _EbnSubnetSearchTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ebnSubnetSearchTable.setStatus("current")
_EbnSubnetSearchEntry_Object = MibTableRow
ebnSubnetSearchEntry = _EbnSubnetSearchEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 1, 1)
)
ebnSubnetSearchEntry.setIndexNames(
    (0, "EBN-MIB", "ebnSubnetSearchLuName"),
)
if mibBuilder.loadTexts:
    ebnSubnetSearchEntry.setStatus("current")
_EbnSubnetSearchLuName_Type = SnaNAUWildcardName
_EbnSubnetSearchLuName_Object = MibTableColumn
ebnSubnetSearchLuName = _EbnSubnetSearchLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 1, 1, 1),
    _EbnSubnetSearchLuName_Type()
)
ebnSubnetSearchLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ebnSubnetSearchLuName.setStatus("current")


class _EbnSubnetSearchDynamics_Type(Integer32):
    """Custom type ebnSubnetSearchDynamics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 3),
          ("limited", 2),
          ("none", 1))
    )


_EbnSubnetSearchDynamics_Type.__name__ = "Integer32"
_EbnSubnetSearchDynamics_Object = MibTableColumn
ebnSubnetSearchDynamics = _EbnSubnetSearchDynamics_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 1, 1, 2),
    _EbnSubnetSearchDynamics_Type()
)
ebnSubnetSearchDynamics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnSubnetSearchDynamics.setStatus("current")


class _EbnSubnetSearchOrdering_Type(Integer32):
    """Custom type ebnSubnetSearchOrdering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defined", 2),
          ("priority", 1))
    )


_EbnSubnetSearchOrdering_Type.__name__ = "Integer32"
_EbnSubnetSearchOrdering_Object = MibTableColumn
ebnSubnetSearchOrdering = _EbnSubnetSearchOrdering_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 1, 1, 3),
    _EbnSubnetSearchOrdering_Type()
)
ebnSubnetSearchOrdering.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnSubnetSearchOrdering.setStatus("current")
_EbnSearchTable_Object = MibTable
ebnSearchTable = _EbnSearchTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2)
)
if mibBuilder.loadTexts:
    ebnSearchTable.setStatus("current")
_EbnSearchEntry_Object = MibTableRow
ebnSearchEntry = _EbnSearchEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2, 1)
)
ebnSearchEntry.setIndexNames(
    (0, "EBN-MIB", "ebnSearchLuName"),
    (0, "EBN-MIB", "ebnSearchIndex"),
)
if mibBuilder.loadTexts:
    ebnSearchEntry.setStatus("current")
_EbnSearchLuName_Type = SnaNAUWildcardName
_EbnSearchLuName_Object = MibTableColumn
ebnSearchLuName = _EbnSearchLuName_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2, 1, 1),
    _EbnSearchLuName_Type()
)
ebnSearchLuName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ebnSearchLuName.setStatus("current")
_EbnSearchIndex_Type = Unsigned32
_EbnSearchIndex_Object = MibTableColumn
ebnSearchIndex = _EbnSearchIndex_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2, 1, 2),
    _EbnSearchIndex_Type()
)
ebnSearchIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ebnSearchIndex.setStatus("current")


class _EbnSearchCpName_Type(DisplayString):
    """Custom type ebnSearchCpName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 17),
    )


_EbnSearchCpName_Type.__name__ = "DisplayString"
_EbnSearchCpName_Object = MibTableColumn
ebnSearchCpName = _EbnSearchCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2, 1, 3),
    _EbnSearchCpName_Type()
)
ebnSearchCpName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnSearchCpName.setStatus("current")
_EbnSearchSNVC_Type = Unsigned32
_EbnSearchSNVC_Object = MibTableColumn
ebnSearchSNVC = _EbnSearchSNVC_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 5, 2, 1, 4),
    _EbnSearchSNVC_Type()
)
ebnSearchSNVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ebnSearchSNVC.setStatus("current")
_Hbn_ObjectIdentity = ObjectIdentity
hbn = _Hbn_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 6)
)
_HbnIsInTable_Object = MibTable
hbnIsInTable = _HbnIsInTable_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hbnIsInTable.setStatus("current")
_HbnIsInEntry_Object = MibTableRow
hbnIsInEntry = _HbnIsInEntry_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1, 1)
)
hbnIsInEntry.setIndexNames(
    (0, "EBN-MIB", "hbnIsInFqCpName"),
    (0, "EBN-MIB", "hbnIsInPcid"),
)
if mibBuilder.loadTexts:
    hbnIsInEntry.setStatus("current")
_HbnIsInFqCpName_Type = SnaControlPointName
_HbnIsInFqCpName_Object = MibTableColumn
hbnIsInFqCpName = _HbnIsInFqCpName_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1, 1, 1),
    _HbnIsInFqCpName_Type()
)
hbnIsInFqCpName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hbnIsInFqCpName.setStatus("current")


class _HbnIsInPcid_Type(OctetString):
    """Custom type hbnIsInPcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HbnIsInPcid_Type.__name__ = "OctetString"
_HbnIsInPcid_Object = MibTableColumn
hbnIsInPcid = _HbnIsInPcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1, 1, 2),
    _HbnIsInPcid_Type()
)
hbnIsInPcid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hbnIsInPcid.setStatus("current")


class _HbnIsInRtpNceId_Type(OctetString):
    """Custom type hbnIsInRtpNceId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_HbnIsInRtpNceId_Type.__name__ = "OctetString"
_HbnIsInRtpNceId_Object = MibTableColumn
hbnIsInRtpNceId = _HbnIsInRtpNceId_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1, 1, 3),
    _HbnIsInRtpNceId_Type()
)
hbnIsInRtpNceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbnIsInRtpNceId.setStatus("current")


class _HbnIsInRtpTcid_Type(OctetString):
    """Custom type hbnIsInRtpTcid based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_HbnIsInRtpTcid_Type.__name__ = "OctetString"
_HbnIsInRtpTcid_Object = MibTableColumn
hbnIsInRtpTcid = _HbnIsInRtpTcid_Object(
    (1, 3, 6, 1, 2, 1, 34, 7, 1, 6, 1, 1, 4),
    _HbnIsInRtpTcid_Type()
)
hbnIsInRtpTcid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hbnIsInRtpTcid.setStatus("current")
_EbnConformance_ObjectIdentity = ObjectIdentity
ebnConformance = _EbnConformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7, 2)
)
_EbnCompliances_ObjectIdentity = ObjectIdentity
ebnCompliances = _EbnCompliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7, 2, 1)
)
_EbnGroups_ObjectIdentity = ObjectIdentity
ebnGroups = _EbnGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 34, 7, 2, 2)
)

# Managed Objects groups

ebnDirectoryGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 1)
)
ebnDirectoryGroup.setObjects(
    ("EBN-MIB", "ebnDirSubnetAffiliation")
)
if mibBuilder.loadTexts:
    ebnDirectoryGroup.setStatus("current")

ebnIsRscvGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 2)
)
ebnIsRscvGroup.setObjects(
      *(("EBN-MIB", "ebnIsRscvDestinationRoute"),
        ("EBN-MIB", "ebnIsRscvDestinationCos"))
)
if mibBuilder.loadTexts:
    ebnIsRscvGroup.setStatus("current")

ebnDirectoryConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 3)
)
ebnDirectoryConfigGroup.setObjects(
      *(("EBN-MIB", "ebnSearchCacheTime"),
        ("EBN-MIB", "ebnMaxSearchCache"),
        ("EBN-MIB", "ebnDefaultSubnetVisitCount"))
)
if mibBuilder.loadTexts:
    ebnDirectoryConfigGroup.setStatus("current")

ebnCosMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 4)
)
ebnCosMappingGroup.setObjects(
    ("EBN-MIB", "ebnCosMapNativeCos")
)
if mibBuilder.loadTexts:
    ebnCosMappingGroup.setStatus("current")

ebnSubnetRoutingListGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 5)
)
ebnSubnetRoutingListGroup.setObjects(
      *(("EBN-MIB", "ebnSubnetSearchDynamics"),
        ("EBN-MIB", "ebnSubnetSearchOrdering"),
        ("EBN-MIB", "ebnSearchCpName"),
        ("EBN-MIB", "ebnSearchSNVC"))
)
if mibBuilder.loadTexts:
    ebnSubnetRoutingListGroup.setStatus("current")

hbnIsInGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 34, 7, 2, 2, 6)
)
hbnIsInGroup.setObjects(
      *(("EBN-MIB", "hbnIsInRtpNceId"),
        ("EBN-MIB", "hbnIsInRtpTcid"))
)
if mibBuilder.loadTexts:
    hbnIsInGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ebnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 34, 7, 2, 1, 1)
)
if mibBuilder.loadTexts:
    ebnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EBN-MIB",
    **{"SnaNAUWildcardName": SnaNAUWildcardName,
       "ebnMIB": ebnMIB,
       "ebnObjects": ebnObjects,
       "ebnDir": ebnDir,
       "ebnDirTable": ebnDirTable,
       "ebnDirEntry": ebnDirEntry,
       "ebnDirLuName": ebnDirLuName,
       "ebnDirSubnetAffiliation": ebnDirSubnetAffiliation,
       "ebnIsRscv": ebnIsRscv,
       "ebnIsRscvTable": ebnIsRscvTable,
       "ebnIsRscvEntry": ebnIsRscvEntry,
       "ebnIsRscvCpName": ebnIsRscvCpName,
       "ebnIsRscvPcid": ebnIsRscvPcid,
       "ebnIsRscvDestinationRoute": ebnIsRscvDestinationRoute,
       "ebnIsRscvDestinationCos": ebnIsRscvDestinationCos,
       "ebnDirConfig": ebnDirConfig,
       "ebnSearchCacheTime": ebnSearchCacheTime,
       "ebnMaxSearchCache": ebnMaxSearchCache,
       "ebnDefaultSubnetVisitCount": ebnDefaultSubnetVisitCount,
       "ebnCOS": ebnCOS,
       "ebnCosMapTable": ebnCosMapTable,
       "ebnCosMapEntry": ebnCosMapEntry,
       "ebnCosMapCpName": ebnCosMapCpName,
       "ebnCosMapNonNativeCos": ebnCosMapNonNativeCos,
       "ebnCosMapNativeCos": ebnCosMapNativeCos,
       "ebnSubnetRoutingList": ebnSubnetRoutingList,
       "ebnSubnetSearchTable": ebnSubnetSearchTable,
       "ebnSubnetSearchEntry": ebnSubnetSearchEntry,
       "ebnSubnetSearchLuName": ebnSubnetSearchLuName,
       "ebnSubnetSearchDynamics": ebnSubnetSearchDynamics,
       "ebnSubnetSearchOrdering": ebnSubnetSearchOrdering,
       "ebnSearchTable": ebnSearchTable,
       "ebnSearchEntry": ebnSearchEntry,
       "ebnSearchLuName": ebnSearchLuName,
       "ebnSearchIndex": ebnSearchIndex,
       "ebnSearchCpName": ebnSearchCpName,
       "ebnSearchSNVC": ebnSearchSNVC,
       "hbn": hbn,
       "hbnIsInTable": hbnIsInTable,
       "hbnIsInEntry": hbnIsInEntry,
       "hbnIsInFqCpName": hbnIsInFqCpName,
       "hbnIsInPcid": hbnIsInPcid,
       "hbnIsInRtpNceId": hbnIsInRtpNceId,
       "hbnIsInRtpTcid": hbnIsInRtpTcid,
       "ebnConformance": ebnConformance,
       "ebnCompliances": ebnCompliances,
       "ebnCompliance": ebnCompliance,
       "ebnGroups": ebnGroups,
       "ebnDirectoryGroup": ebnDirectoryGroup,
       "ebnIsRscvGroup": ebnIsRscvGroup,
       "ebnDirectoryConfigGroup": ebnDirectoryConfigGroup,
       "ebnCosMappingGroup": ebnCosMappingGroup,
       "ebnSubnetRoutingListGroup": ebnSubnetRoutingListGroup,
       "hbnIsInGroup": hbnIsInGroup}
)
