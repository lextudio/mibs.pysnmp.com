# SNMP MIB module (RFC1252-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RFC1252-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:47:15 2024
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
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class AreaID(IpAddress):
    """Custom type AreaID based on IpAddress"""




class RouterID(IpAddress):
    """Custom type RouterID based on IpAddress"""




class Metric(Integer32):
    """Custom type Metric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class BigMetric(Integer32):
    """Custom type BigMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777215),
    )





class TruthValue(Integer32):
    """Custom type TruthValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 2),
          ("true", 1))
    )





class Status(Integer32):
    """Custom type Status based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1))
    )





class Validation(Integer32):
    """Custom type Validation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 2),
          ("valid", 1))
    )





class PositiveInteger(Integer32):
    """Custom type PositiveInteger based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )





class HelloRange(Integer32):
    """Custom type HelloRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )





class UpToMaxAge(Integer32):
    """Custom type UpToMaxAge based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3600),
    )





class InterfaceIndex(Integer32):
    """Custom type InterfaceIndex based on Integer32"""




class DesignatedRouterPriority(Integer32):
    """Custom type DesignatedRouterPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class TOSType(Integer32):
    """Custom type TOSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Ospf_ObjectIdentity = ObjectIdentity
ospf = _Ospf_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13)
)
_OspfGeneralGroup_ObjectIdentity = ObjectIdentity
ospfGeneralGroup = _OspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 13, 1)
)
_OspfRouterId_Type = RouterID
_OspfRouterId_Object = MibScalar
ospfRouterId = _OspfRouterId_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 1),
    _OspfRouterId_Type()
)
ospfRouterId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRouterId.setStatus("mandatory")
_OspfAdminStat_Type = Status
_OspfAdminStat_Object = MibScalar
ospfAdminStat = _OspfAdminStat_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 2),
    _OspfAdminStat_Type()
)
ospfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAdminStat.setStatus("mandatory")


class _OspfVersionNumber_Type(Integer32):
    """Custom type ospfVersionNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            2
        )
    )
    namedValues = NamedValues(
        ("version2", 2)
    )


_OspfVersionNumber_Type.__name__ = "Integer32"
_OspfVersionNumber_Object = MibScalar
ospfVersionNumber = _OspfVersionNumber_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 3),
    _OspfVersionNumber_Type()
)
ospfVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVersionNumber.setStatus("mandatory")
_OspfAreaBdrRtrStatus_Type = TruthValue
_OspfAreaBdrRtrStatus_Object = MibScalar
ospfAreaBdrRtrStatus = _OspfAreaBdrRtrStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 4),
    _OspfAreaBdrRtrStatus_Type()
)
ospfAreaBdrRtrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaBdrRtrStatus.setStatus("mandatory")
_OspfASBdrRtrStatus_Type = TruthValue
_OspfASBdrRtrStatus_Object = MibScalar
ospfASBdrRtrStatus = _OspfASBdrRtrStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 5),
    _OspfASBdrRtrStatus_Type()
)
ospfASBdrRtrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfASBdrRtrStatus.setStatus("mandatory")
_OspfExternLSACount_Type = Gauge32
_OspfExternLSACount_Object = MibScalar
ospfExternLSACount = _OspfExternLSACount_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 6),
    _OspfExternLSACount_Type()
)
ospfExternLSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternLSACount.setStatus("mandatory")
_OspfExternLSACksumSum_Type = Integer32
_OspfExternLSACksumSum_Object = MibScalar
ospfExternLSACksumSum = _OspfExternLSACksumSum_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 7),
    _OspfExternLSACksumSum_Type()
)
ospfExternLSACksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternLSACksumSum.setStatus("mandatory")
_OspfTOSSupport_Type = TruthValue
_OspfTOSSupport_Object = MibScalar
ospfTOSSupport = _OspfTOSSupport_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 8),
    _OspfTOSSupport_Type()
)
ospfTOSSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfTOSSupport.setStatus("mandatory")
_OspfOriginateNewLSAs_Type = Counter32
_OspfOriginateNewLSAs_Object = MibScalar
ospfOriginateNewLSAs = _OspfOriginateNewLSAs_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 9),
    _OspfOriginateNewLSAs_Type()
)
ospfOriginateNewLSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfOriginateNewLSAs.setStatus("mandatory")
_OspfRxNewLSAs_Type = Counter32
_OspfRxNewLSAs_Object = MibScalar
ospfRxNewLSAs = _OspfRxNewLSAs_Object(
    (1, 3, 6, 1, 2, 1, 13, 1, 10),
    _OspfRxNewLSAs_Type()
)
ospfRxNewLSAs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRxNewLSAs.setStatus("mandatory")
_OspfAreaTable_Object = MibTable
ospfAreaTable = _OspfAreaTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 2)
)
if mibBuilder.loadTexts:
    ospfAreaTable.setStatus("mandatory")
_OspfAreaEntry_Object = MibTableRow
ospfAreaEntry = _OspfAreaEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1)
)
ospfAreaEntry.setIndexNames(
    (0, "RFC1252-MIB", "ospfAreaID"),
)
if mibBuilder.loadTexts:
    ospfAreaEntry.setStatus("mandatory")
_OspfAreaId_Type = AreaID
_OspfAreaId_Object = MibTableColumn
ospfAreaId = _OspfAreaId_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 1),
    _OspfAreaId_Type()
)
ospfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaId.setStatus("mandatory")


class _OspfAuthType_Type(Integer32):
    """Custom type ospfAuthType based on Integer32"""
    defaultValue = 0


_OspfAuthType_Object = MibTableColumn
ospfAuthType = _OspfAuthType_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 2),
    _OspfAuthType_Type()
)
ospfAuthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAuthType.setStatus("mandatory")


class _OspfImportASExtern_Type(TruthValue):
    """Custom type ospfImportASExtern based on TruthValue"""


_OspfImportASExtern_Object = MibTableColumn
ospfImportASExtern = _OspfImportASExtern_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 3),
    _OspfImportASExtern_Type()
)
ospfImportASExtern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfImportASExtern.setStatus("mandatory")


class _OspfSpfRuns_Type(Counter32):
    """Custom type ospfSpfRuns based on Counter32"""
    defaultValue = 0


_OspfSpfRuns_Object = MibTableColumn
ospfSpfRuns = _OspfSpfRuns_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 4),
    _OspfSpfRuns_Type()
)
ospfSpfRuns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfSpfRuns.setStatus("mandatory")


class _OspfAreaBdrRtrCount_Type(Gauge32):
    """Custom type ospfAreaBdrRtrCount based on Gauge32"""
    defaultValue = 0


_OspfAreaBdrRtrCount_Object = MibTableColumn
ospfAreaBdrRtrCount = _OspfAreaBdrRtrCount_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 5),
    _OspfAreaBdrRtrCount_Type()
)
ospfAreaBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaBdrRtrCount.setStatus("mandatory")


class _OspfASBdrRtrCount_Type(Gauge32):
    """Custom type ospfASBdrRtrCount based on Gauge32"""
    defaultValue = 0


_OspfASBdrRtrCount_Object = MibTableColumn
ospfASBdrRtrCount = _OspfASBdrRtrCount_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 6),
    _OspfASBdrRtrCount_Type()
)
ospfASBdrRtrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfASBdrRtrCount.setStatus("mandatory")


class _OspfAreaLSACount_Type(Gauge32):
    """Custom type ospfAreaLSACount based on Gauge32"""
    defaultValue = 0


_OspfAreaLSACount_Object = MibScalar
ospfAreaLSACount = _OspfAreaLSACount_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 7),
    _OspfAreaLSACount_Type()
)
ospfAreaLSACount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaLSACount.setStatus("mandatory")


class _OspfAreaLSACksumSum_Type(Integer32):
    """Custom type ospfAreaLSACksumSum based on Integer32"""
    defaultValue = 0


_OspfAreaLSACksumSum_Object = MibTableColumn
ospfAreaLSACksumSum = _OspfAreaLSACksumSum_Object(
    (1, 3, 6, 1, 2, 1, 13, 2, 1, 8),
    _OspfAreaLSACksumSum_Type()
)
ospfAreaLSACksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaLSACksumSum.setStatus("mandatory")
_OspfStubAreaTable_Object = MibTable
ospfStubAreaTable = _OspfStubAreaTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 3)
)
if mibBuilder.loadTexts:
    ospfStubAreaTable.setStatus("mandatory")
_OspfStubAreaEntry_Object = MibTableRow
ospfStubAreaEntry = _OspfStubAreaEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1)
)
ospfStubAreaEntry.setIndexNames(
    (0, "RFC1252-MIB", "ospfStubAreaID"),
    (0, "RFC1252-MIB", "ospfStubTOS"),
)
if mibBuilder.loadTexts:
    ospfStubAreaEntry.setStatus("mandatory")
_OspfStubAreaID_Type = AreaID
_OspfStubAreaID_Object = MibTableColumn
ospfStubAreaID = _OspfStubAreaID_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 1),
    _OspfStubAreaID_Type()
)
ospfStubAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfStubAreaID.setStatus("mandatory")
_OspfStubTOS_Type = TOSType
_OspfStubTOS_Object = MibTableColumn
ospfStubTOS = _OspfStubTOS_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 2),
    _OspfStubTOS_Type()
)
ospfStubTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfStubTOS.setStatus("mandatory")
_OspfStubMetric_Type = BigMetric
_OspfStubMetric_Object = MibTableColumn
ospfStubMetric = _OspfStubMetric_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 3),
    _OspfStubMetric_Type()
)
ospfStubMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfStubMetric.setStatus("mandatory")


class _OspfStubStatus_Type(Validation):
    """Custom type ospfStubStatus based on Validation"""


_OspfStubStatus_Object = MibTableColumn
ospfStubStatus = _OspfStubStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 3, 1, 4),
    _OspfStubStatus_Type()
)
ospfStubStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfStubStatus.setStatus("mandatory")
_OspfLsdbTable_Object = MibTable
ospfLsdbTable = _OspfLsdbTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 4)
)
if mibBuilder.loadTexts:
    ospfLsdbTable.setStatus("mandatory")
_OspfLsdbEntry_Object = MibTableRow
ospfLsdbEntry = _OspfLsdbEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1)
)
ospfLsdbEntry.setIndexNames(
    (0, "RFC1252-MIB", "ospfLsdbAreaId"),
    (0, "RFC1252-MIB", "ospfLsdbType"),
    (0, "RFC1252-MIB", "ospfLsdbLSID"),
    (0, "RFC1252-MIB", "ospfLsdbRouterId"),
)
if mibBuilder.loadTexts:
    ospfLsdbEntry.setStatus("mandatory")
_OspfLsdbAreaId_Type = AreaID
_OspfLsdbAreaId_Object = MibTableColumn
ospfLsdbAreaId = _OspfLsdbAreaId_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1, 1),
    _OspfLsdbAreaId_Type()
)
ospfLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbAreaId.setStatus("mandatory")


class _OspfLsdbType_Type(Integer32):
    """Custom type ospfLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("asExternalLink", 5),
          ("asSummaryLink", 4),
          ("networkLink", 2),
          ("routerLink", 1),
          ("summaryLink", 3))
    )


_OspfLsdbType_Type.__name__ = "Integer32"
_OspfLsdbType_Object = MibTableColumn
ospfLsdbType = _OspfLsdbType_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1, 2),
    _OspfLsdbType_Type()
)
ospfLsdbType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbType.setStatus("mandatory")
_OspfLsdbLSID_Type = IpAddress
_OspfLsdbLSID_Object = MibTableColumn
ospfLsdbLSID = _OspfLsdbLSID_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1, 3),
    _OspfLsdbLSID_Type()
)
ospfLsdbLSID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbLSID.setStatus("mandatory")
_OspfLsdbRouterId_Type = RouterID
_OspfLsdbRouterId_Object = MibTableColumn
ospfLsdbRouterId = _OspfLsdbRouterId_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1, 4),
    _OspfLsdbRouterId_Type()
)
ospfLsdbRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbRouterId.setStatus("mandatory")
_OspfLsdbSequence_Type = Integer32
_OspfLsdbSequence_Object = MibTableColumn
ospfLsdbSequence = _OspfLsdbSequence_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1, 5),
    _OspfLsdbSequence_Type()
)
ospfLsdbSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbSequence.setStatus("mandatory")
_OspfLsdbAge_Type = Integer32
_OspfLsdbAge_Object = MibTableColumn
ospfLsdbAge = _OspfLsdbAge_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1, 6),
    _OspfLsdbAge_Type()
)
ospfLsdbAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbAge.setStatus("mandatory")
_OspfLsdbChecksum_Type = Integer32
_OspfLsdbChecksum_Object = MibTableColumn
ospfLsdbChecksum = _OspfLsdbChecksum_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1, 7),
    _OspfLsdbChecksum_Type()
)
ospfLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbChecksum.setStatus("mandatory")
_OspfLsdbAdvertisement_Type = OctetString
_OspfLsdbAdvertisement_Object = MibTableColumn
ospfLsdbAdvertisement = _OspfLsdbAdvertisement_Object(
    (1, 3, 6, 1, 2, 1, 13, 4, 1, 8),
    _OspfLsdbAdvertisement_Type()
)
ospfLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfLsdbAdvertisement.setStatus("mandatory")
_OspfAreaRangeTable_Object = MibTable
ospfAreaRangeTable = _OspfAreaRangeTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 5)
)
if mibBuilder.loadTexts:
    ospfAreaRangeTable.setStatus("mandatory")
_OspfAreaRangeEntry_Object = MibTableRow
ospfAreaRangeEntry = _OspfAreaRangeEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1)
)
ospfAreaRangeEntry.setIndexNames(
    (0, "RFC1252-MIB", "ospfAreaRangeAreaID"),
    (0, "RFC1252-MIB", "ospfAreaRangeNet"),
)
if mibBuilder.loadTexts:
    ospfAreaRangeEntry.setStatus("mandatory")
_OspfAreaRangeAreaID_Type = AreaID
_OspfAreaRangeAreaID_Object = MibTableColumn
ospfAreaRangeAreaID = _OspfAreaRangeAreaID_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 1),
    _OspfAreaRangeAreaID_Type()
)
ospfAreaRangeAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaRangeAreaID.setStatus("mandatory")
_OspfAreaRangeNet_Type = IpAddress
_OspfAreaRangeNet_Object = MibTableColumn
ospfAreaRangeNet = _OspfAreaRangeNet_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 2),
    _OspfAreaRangeNet_Type()
)
ospfAreaRangeNet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaRangeNet.setStatus("mandatory")
_OspfAreaRangeMask_Type = IpAddress
_OspfAreaRangeMask_Object = MibTableColumn
ospfAreaRangeMask = _OspfAreaRangeMask_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 3),
    _OspfAreaRangeMask_Type()
)
ospfAreaRangeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaRangeMask.setStatus("mandatory")


class _OspfAreaRangeStatus_Type(Validation):
    """Custom type ospfAreaRangeStatus based on Validation"""


_OspfAreaRangeStatus_Object = MibTableColumn
ospfAreaRangeStatus = _OspfAreaRangeStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 5, 1, 4),
    _OspfAreaRangeStatus_Type()
)
ospfAreaRangeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAreaRangeStatus.setStatus("mandatory")
_OspfHostTable_Object = MibTable
ospfHostTable = _OspfHostTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 6)
)
if mibBuilder.loadTexts:
    ospfHostTable.setStatus("mandatory")
_OspfHostEntry_Object = MibTableRow
ospfHostEntry = _OspfHostEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1)
)
ospfHostEntry.setIndexNames(
    (0, "RFC1252-MIB", "ospfHostIpAddress"),
    (0, "RFC1252-MIB", "ospfHostTOS"),
)
if mibBuilder.loadTexts:
    ospfHostEntry.setStatus("mandatory")
_OspfHostIpAddress_Type = IpAddress
_OspfHostIpAddress_Object = MibTableColumn
ospfHostIpAddress = _OspfHostIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 1),
    _OspfHostIpAddress_Type()
)
ospfHostIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfHostIpAddress.setStatus("mandatory")
_OspfHostTOS_Type = TOSType
_OspfHostTOS_Object = MibTableColumn
ospfHostTOS = _OspfHostTOS_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 2),
    _OspfHostTOS_Type()
)
ospfHostTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfHostTOS.setStatus("mandatory")
_OspfHostMetric_Type = Metric
_OspfHostMetric_Object = MibTableColumn
ospfHostMetric = _OspfHostMetric_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 3),
    _OspfHostMetric_Type()
)
ospfHostMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfHostMetric.setStatus("mandatory")


class _OspfHostStatus_Type(Validation):
    """Custom type ospfHostStatus based on Validation"""


_OspfHostStatus_Object = MibTableColumn
ospfHostStatus = _OspfHostStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 6, 1, 4),
    _OspfHostStatus_Type()
)
ospfHostStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfHostStatus.setStatus("mandatory")
_OspfIfTable_Object = MibTable
ospfIfTable = _OspfIfTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 7)
)
if mibBuilder.loadTexts:
    ospfIfTable.setStatus("mandatory")
_OspfIfEntry_Object = MibTableRow
ospfIfEntry = _OspfIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1)
)
ospfIfEntry.setIndexNames(
    (0, "RFC1252-MIB", "ospfIfIpAddress"),
    (0, "RFC1252-MIB", "ospfAddressLessIf"),
)
if mibBuilder.loadTexts:
    ospfIfEntry.setStatus("mandatory")
_OspfIfIpAddress_Type = IpAddress
_OspfIfIpAddress_Object = MibTableColumn
ospfIfIpAddress = _OspfIfIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 1),
    _OspfIfIpAddress_Type()
)
ospfIfIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfIpAddress.setStatus("mandatory")
_OspfAddressLessIf_Type = Integer32
_OspfAddressLessIf_Object = MibTableColumn
ospfAddressLessIf = _OspfAddressLessIf_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 2),
    _OspfAddressLessIf_Type()
)
ospfAddressLessIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAddressLessIf.setStatus("mandatory")


class _OspfIfAreaId_Type(AreaID):
    """Custom type ospfIfAreaId based on AreaID"""
    defaultHexValue = "00000000"


_OspfIfAreaId_Object = MibTableColumn
ospfIfAreaId = _OspfIfAreaId_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 3),
    _OspfIfAreaId_Type()
)
ospfIfAreaId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfAreaId.setStatus("mandatory")


class _OspfIfType_Type(Integer32):
    """Custom type ospfIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("broadcast", 1),
          ("nbma", 2),
          ("pointToPoint", 3))
    )


_OspfIfType_Type.__name__ = "Integer32"
_OspfIfType_Object = MibTableColumn
ospfIfType = _OspfIfType_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 4),
    _OspfIfType_Type()
)
ospfIfType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfType.setStatus("mandatory")


class _OspfIfAdminStat_Type(Status):
    """Custom type ospfIfAdminStat based on Status"""


_OspfIfAdminStat_Object = MibTableColumn
ospfIfAdminStat = _OspfIfAdminStat_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 5),
    _OspfIfAdminStat_Type()
)
ospfIfAdminStat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfAdminStat.setStatus("mandatory")


class _OspfIfRtrPriority_Type(DesignatedRouterPriority):
    """Custom type ospfIfRtrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_OspfIfRtrPriority_Object = MibTableColumn
ospfIfRtrPriority = _OspfIfRtrPriority_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 6),
    _OspfIfRtrPriority_Type()
)
ospfIfRtrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfRtrPriority.setStatus("mandatory")


class _OspfIfTransitDelay_Type(UpToMaxAge):
    """Custom type ospfIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_OspfIfTransitDelay_Object = MibTableColumn
ospfIfTransitDelay = _OspfIfTransitDelay_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 7),
    _OspfIfTransitDelay_Type()
)
ospfIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfTransitDelay.setStatus("mandatory")


class _OspfIfRetransInterval_Type(UpToMaxAge):
    """Custom type ospfIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_OspfIfRetransInterval_Object = MibTableColumn
ospfIfRetransInterval = _OspfIfRetransInterval_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 8),
    _OspfIfRetransInterval_Type()
)
ospfIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfRetransInterval.setStatus("mandatory")


class _OspfIfHelloInterval_Type(HelloRange):
    """Custom type ospfIfHelloInterval based on HelloRange"""
    defaultValue = 10


_OspfIfHelloInterval_Object = MibTableColumn
ospfIfHelloInterval = _OspfIfHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 9),
    _OspfIfHelloInterval_Type()
)
ospfIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfHelloInterval.setStatus("mandatory")


class _OspfIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type ospfIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 40


_OspfIfRtrDeadInterval_Object = MibTableColumn
ospfIfRtrDeadInterval = _OspfIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 10),
    _OspfIfRtrDeadInterval_Type()
)
ospfIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfRtrDeadInterval.setStatus("mandatory")


class _OspfIfPollInterval_Type(PositiveInteger):
    """Custom type ospfIfPollInterval based on PositiveInteger"""
    defaultValue = 120


_OspfIfPollInterval_Object = MibTableColumn
ospfIfPollInterval = _OspfIfPollInterval_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 11),
    _OspfIfPollInterval_Type()
)
ospfIfPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfPollInterval.setStatus("mandatory")


class _OspfIfState_Type(Integer32):
    """Custom type ospfIfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("backupDesignatedRouter", 6),
          ("designatedRouter", 5),
          ("down", 1),
          ("loopback", 2),
          ("otherDesignatedRouter", 7),
          ("pointToPoint", 4),
          ("waiting", 3))
    )


_OspfIfState_Type.__name__ = "Integer32"
_OspfIfState_Object = MibTableColumn
ospfIfState = _OspfIfState_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 12),
    _OspfIfState_Type()
)
ospfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfState.setStatus("mandatory")


class _OspfIfDesignatedRouter_Type(IpAddress):
    """Custom type ospfIfDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_OspfIfDesignatedRouter_Object = MibTableColumn
ospfIfDesignatedRouter = _OspfIfDesignatedRouter_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 13),
    _OspfIfDesignatedRouter_Type()
)
ospfIfDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfDesignatedRouter.setStatus("mandatory")


class _OspfIfBackupDesignatedRouter_Type(IpAddress):
    """Custom type ospfIfBackupDesignatedRouter based on IpAddress"""
    defaultHexValue = "00000000"


_OspfIfBackupDesignatedRouter_Object = MibTableColumn
ospfIfBackupDesignatedRouter = _OspfIfBackupDesignatedRouter_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 14),
    _OspfIfBackupDesignatedRouter_Type()
)
ospfIfBackupDesignatedRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfBackupDesignatedRouter.setStatus("mandatory")


class _OspfIfEvents_Type(Counter32):
    """Custom type ospfIfEvents based on Counter32"""
    defaultValue = 0


_OspfIfEvents_Object = MibTableColumn
ospfIfEvents = _OspfIfEvents_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 15),
    _OspfIfEvents_Type()
)
ospfIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfIfEvents.setStatus("mandatory")


class _OspfIfAuthKey_Type(OctetString):
    """Custom type ospfIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"


_OspfIfAuthKey_Object = MibTableColumn
ospfIfAuthKey = _OspfIfAuthKey_Object(
    (1, 3, 6, 1, 2, 1, 13, 7, 1, 16),
    _OspfIfAuthKey_Type()
)
ospfIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfAuthKey.setStatus("mandatory")
_OspfIfMetricTable_Object = MibTable
ospfIfMetricTable = _OspfIfMetricTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 8)
)
if mibBuilder.loadTexts:
    ospfIfMetricTable.setStatus("mandatory")
_OspfIfMetricEntry_Object = MibTableRow
ospfIfMetricEntry = _OspfIfMetricEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1)
)
ospfIfMetricEntry.setIndexNames(
    (0, "RFC1252-MIB", "ospfIfMetricIpAddress"),
    (0, "RFC1252-MIB", "ospfIfMetricAddressLessIf"),
    (0, "RFC1252-MIB", "ospfIfMetricTOS"),
)
if mibBuilder.loadTexts:
    ospfIfMetricEntry.setStatus("mandatory")
_OspfIfMetricIpAddress_Type = IpAddress
_OspfIfMetricIpAddress_Object = MibTableColumn
ospfIfMetricIpAddress = _OspfIfMetricIpAddress_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 1),
    _OspfIfMetricIpAddress_Type()
)
ospfIfMetricIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfMetricIpAddress.setStatus("mandatory")
_OspfIfMetricAddressLessIf_Type = Integer32
_OspfIfMetricAddressLessIf_Object = MibTableColumn
ospfIfMetricAddressLessIf = _OspfIfMetricAddressLessIf_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 2),
    _OspfIfMetricAddressLessIf_Type()
)
ospfIfMetricAddressLessIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfMetricAddressLessIf.setStatus("mandatory")
_OspfIfMetricTOS_Type = TOSType
_OspfIfMetricTOS_Object = MibTableColumn
ospfIfMetricTOS = _OspfIfMetricTOS_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 3),
    _OspfIfMetricTOS_Type()
)
ospfIfMetricTOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfMetricTOS.setStatus("mandatory")
_OspfIfMetricMetric_Type = Metric
_OspfIfMetricMetric_Object = MibTableColumn
ospfIfMetricMetric = _OspfIfMetricMetric_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 4),
    _OspfIfMetricMetric_Type()
)
ospfIfMetricMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfMetricMetric.setStatus("mandatory")


class _OspfIfMetricStatus_Type(Validation):
    """Custom type ospfIfMetricStatus based on Validation"""


_OspfIfMetricStatus_Object = MibTableColumn
ospfIfMetricStatus = _OspfIfMetricStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 8, 1, 5),
    _OspfIfMetricStatus_Type()
)
ospfIfMetricStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfIfMetricStatus.setStatus("mandatory")
_OspfVirtIfTable_Object = MibTable
ospfVirtIfTable = _OspfVirtIfTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 9)
)
if mibBuilder.loadTexts:
    ospfVirtIfTable.setStatus("mandatory")
_OspfVirtIfEntry_Object = MibTableRow
ospfVirtIfEntry = _OspfVirtIfEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1)
)
ospfVirtIfEntry.setIndexNames(
    (0, "RFC1252-MIB", "ospfVirtIfAreaID"),
    (0, "RFC1252-MIB", "ospfVirtIfNeighbor"),
)
if mibBuilder.loadTexts:
    ospfVirtIfEntry.setStatus("mandatory")
_OspfVirtIfAreaID_Type = AreaID
_OspfVirtIfAreaID_Object = MibTableColumn
ospfVirtIfAreaID = _OspfVirtIfAreaID_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1, 1),
    _OspfVirtIfAreaID_Type()
)
ospfVirtIfAreaID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIfAreaID.setStatus("mandatory")
_OspfVirtIfNeighbor_Type = RouterID
_OspfVirtIfNeighbor_Object = MibTableColumn
ospfVirtIfNeighbor = _OspfVirtIfNeighbor_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1, 2),
    _OspfVirtIfNeighbor_Type()
)
ospfVirtIfNeighbor.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIfNeighbor.setStatus("mandatory")


class _OspfVirtIfTransitDelay_Type(UpToMaxAge):
    """Custom type ospfVirtIfTransitDelay based on UpToMaxAge"""
    defaultValue = 1


_OspfVirtIfTransitDelay_Object = MibTableColumn
ospfVirtIfTransitDelay = _OspfVirtIfTransitDelay_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1, 3),
    _OspfVirtIfTransitDelay_Type()
)
ospfVirtIfTransitDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIfTransitDelay.setStatus("mandatory")


class _OspfVirtIfRetransInterval_Type(UpToMaxAge):
    """Custom type ospfVirtIfRetransInterval based on UpToMaxAge"""
    defaultValue = 5


_OspfVirtIfRetransInterval_Object = MibTableColumn
ospfVirtIfRetransInterval = _OspfVirtIfRetransInterval_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1, 4),
    _OspfVirtIfRetransInterval_Type()
)
ospfVirtIfRetransInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIfRetransInterval.setStatus("mandatory")


class _OspfVirtIfHelloInterval_Type(HelloRange):
    """Custom type ospfVirtIfHelloInterval based on HelloRange"""
    defaultValue = 10


_OspfVirtIfHelloInterval_Object = MibTableColumn
ospfVirtIfHelloInterval = _OspfVirtIfHelloInterval_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1, 5),
    _OspfVirtIfHelloInterval_Type()
)
ospfVirtIfHelloInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIfHelloInterval.setStatus("mandatory")


class _OspfVirtIfRtrDeadInterval_Type(PositiveInteger):
    """Custom type ospfVirtIfRtrDeadInterval based on PositiveInteger"""
    defaultValue = 60


_OspfVirtIfRtrDeadInterval_Object = MibTableColumn
ospfVirtIfRtrDeadInterval = _OspfVirtIfRtrDeadInterval_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1, 6),
    _OspfVirtIfRtrDeadInterval_Type()
)
ospfVirtIfRtrDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIfRtrDeadInterval.setStatus("mandatory")


class _OspfVirtIfState_Type(Integer32):
    """Custom type ospfVirtIfState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              4)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("pointToPoint", 4))
    )


_OspfVirtIfState_Type.__name__ = "Integer32"
_OspfVirtIfState_Object = MibTableColumn
ospfVirtIfState = _OspfVirtIfState_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1, 7),
    _OspfVirtIfState_Type()
)
ospfVirtIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIfState.setStatus("mandatory")


class _OspfVirtIfEvents_Type(Counter32):
    """Custom type ospfVirtIfEvents based on Counter32"""
    defaultValue = 0


_OspfVirtIfEvents_Object = MibTableColumn
ospfVirtIfEvents = _OspfVirtIfEvents_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1, 8),
    _OspfVirtIfEvents_Type()
)
ospfVirtIfEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtIfEvents.setStatus("mandatory")


class _OspfVirtIfAuthKey_Type(OctetString):
    """Custom type ospfVirtIfAuthKey based on OctetString"""
    defaultHexValue = "0000000000000000"


_OspfVirtIfAuthKey_Object = MibTableColumn
ospfVirtIfAuthKey = _OspfVirtIfAuthKey_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1, 9),
    _OspfVirtIfAuthKey_Type()
)
ospfVirtIfAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIfAuthKey.setStatus("mandatory")


class _OspfVirtIfStatus_Type(Validation):
    """Custom type ospfVirtIfStatus based on Validation"""


_OspfVirtIfStatus_Object = MibTableColumn
ospfVirtIfStatus = _OspfVirtIfStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 9, 1, 10),
    _OspfVirtIfStatus_Type()
)
ospfVirtIfStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfVirtIfStatus.setStatus("mandatory")
_OspfNbrTable_Object = MibTable
ospfNbrTable = _OspfNbrTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 10)
)
if mibBuilder.loadTexts:
    ospfNbrTable.setStatus("mandatory")
_OspfNbrEntry_Object = MibTableRow
ospfNbrEntry = _OspfNbrEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1)
)
ospfNbrEntry.setIndexNames(
    (0, "RFC1252-MIB", "ospfNbrIpAddr"),
    (0, "RFC1252-MIB", "ospfNbrAddressLessIndex"),
)
if mibBuilder.loadTexts:
    ospfNbrEntry.setStatus("mandatory")
_OspfNbrIpAddr_Type = IpAddress
_OspfNbrIpAddr_Object = MibTableColumn
ospfNbrIpAddr = _OspfNbrIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1, 1),
    _OspfNbrIpAddr_Type()
)
ospfNbrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNbrIpAddr.setStatus("mandatory")
_OspfNbrAddressLessIndex_Type = InterfaceIndex
_OspfNbrAddressLessIndex_Object = MibTableColumn
ospfNbrAddressLessIndex = _OspfNbrAddressLessIndex_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1, 2),
    _OspfNbrAddressLessIndex_Type()
)
ospfNbrAddressLessIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNbrAddressLessIndex.setStatus("mandatory")


class _OspfNbrRtrId_Type(RouterID):
    """Custom type ospfNbrRtrId based on RouterID"""
    defaultHexValue = "00000000"


_OspfNbrRtrId_Object = MibTableColumn
ospfNbrRtrId = _OspfNbrRtrId_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1, 3),
    _OspfNbrRtrId_Type()
)
ospfNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrRtrId.setStatus("mandatory")


class _OspfNbrOptions_Type(Integer32):
    """Custom type ospfNbrOptions based on Integer32"""
    defaultValue = 0


_OspfNbrOptions_Object = MibTableColumn
ospfNbrOptions = _OspfNbrOptions_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1, 4),
    _OspfNbrOptions_Type()
)
ospfNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrOptions.setStatus("mandatory")


class _OspfNbrPriority_Type(DesignatedRouterPriority):
    """Custom type ospfNbrPriority based on DesignatedRouterPriority"""
    defaultValue = 1


_OspfNbrPriority_Object = MibTableColumn
ospfNbrPriority = _OspfNbrPriority_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1, 5),
    _OspfNbrPriority_Type()
)
ospfNbrPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNbrPriority.setStatus("mandatory")


class _OspfNbrState_Type(Integer32):
    """Custom type ospfNbrState based on Integer32"""
    defaultValue = 1

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
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangeStart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoWay", 4))
    )


_OspfNbrState_Type.__name__ = "Integer32"
_OspfNbrState_Object = MibTableColumn
ospfNbrState = _OspfNbrState_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1, 6),
    _OspfNbrState_Type()
)
ospfNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrState.setStatus("mandatory")


class _OspfNbrEvents_Type(Counter32):
    """Custom type ospfNbrEvents based on Counter32"""
    defaultValue = 0


_OspfNbrEvents_Object = MibTableColumn
ospfNbrEvents = _OspfNbrEvents_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1, 7),
    _OspfNbrEvents_Type()
)
ospfNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrEvents.setStatus("mandatory")


class _OspfNbrLSRetransQLen_Type(Gauge32):
    """Custom type ospfNbrLSRetransQLen based on Gauge32"""
    defaultValue = 0


_OspfNbrLSRetransQLen_Object = MibTableColumn
ospfNbrLSRetransQLen = _OspfNbrLSRetransQLen_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1, 8),
    _OspfNbrLSRetransQLen_Type()
)
ospfNbrLSRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNbrLSRetransQLen.setStatus("mandatory")


class _OspfNBMANbrStatus_Type(Validation):
    """Custom type ospfNBMANbrStatus based on Validation"""


_OspfNBMANbrStatus_Object = MibTableColumn
ospfNBMANbrStatus = _OspfNBMANbrStatus_Object(
    (1, 3, 6, 1, 2, 1, 13, 10, 1, 9),
    _OspfNBMANbrStatus_Type()
)
ospfNBMANbrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfNBMANbrStatus.setStatus("mandatory")
_OspfVirtNbrTable_Object = MibTable
ospfVirtNbrTable = _OspfVirtNbrTable_Object(
    (1, 3, 6, 1, 2, 1, 13, 11)
)
if mibBuilder.loadTexts:
    ospfVirtNbrTable.setStatus("mandatory")
_OspfVirtNbrEntry_Object = MibTableRow
ospfVirtNbrEntry = _OspfVirtNbrEntry_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 1)
)
ospfVirtNbrEntry.setIndexNames(
    (0, "RFC1252-MIB", "ospfVirtNbrArea"),
    (0, "RFC1252-MIB", "ospfVirtNbrRtrId"),
)
if mibBuilder.loadTexts:
    ospfVirtNbrEntry.setStatus("mandatory")
_OspfVirtNbrArea_Type = AreaID
_OspfVirtNbrArea_Object = MibTableColumn
ospfVirtNbrArea = _OspfVirtNbrArea_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 1, 1),
    _OspfVirtNbrArea_Type()
)
ospfVirtNbrArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrArea.setStatus("mandatory")
_OspfVirtNbrRtrId_Type = RouterID
_OspfVirtNbrRtrId_Object = MibTableColumn
ospfVirtNbrRtrId = _OspfVirtNbrRtrId_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 1, 2),
    _OspfVirtNbrRtrId_Type()
)
ospfVirtNbrRtrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrRtrId.setStatus("mandatory")
_OspfVirtNbrIpAddr_Type = IpAddress
_OspfVirtNbrIpAddr_Object = MibTableColumn
ospfVirtNbrIpAddr = _OspfVirtNbrIpAddr_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 1, 3),
    _OspfVirtNbrIpAddr_Type()
)
ospfVirtNbrIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrIpAddr.setStatus("mandatory")
_OspfVirtNbrOptions_Type = Integer32
_OspfVirtNbrOptions_Object = MibTableColumn
ospfVirtNbrOptions = _OspfVirtNbrOptions_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 1, 4),
    _OspfVirtNbrOptions_Type()
)
ospfVirtNbrOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrOptions.setStatus("mandatory")


class _OspfVirtNbrState_Type(Integer32):
    """Custom type ospfVirtNbrState based on Integer32"""
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
        *(("attempt", 2),
          ("down", 1),
          ("exchange", 6),
          ("exchangeStart", 5),
          ("full", 8),
          ("init", 3),
          ("loading", 7),
          ("twoWay", 4))
    )


_OspfVirtNbrState_Type.__name__ = "Integer32"
_OspfVirtNbrState_Object = MibTableColumn
ospfVirtNbrState = _OspfVirtNbrState_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 1, 5),
    _OspfVirtNbrState_Type()
)
ospfVirtNbrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrState.setStatus("mandatory")
_OspfVirtNbrEvents_Type = Counter32
_OspfVirtNbrEvents_Object = MibTableColumn
ospfVirtNbrEvents = _OspfVirtNbrEvents_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 1, 6),
    _OspfVirtNbrEvents_Type()
)
ospfVirtNbrEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrEvents.setStatus("mandatory")
_OspfVirtNbrLSRetransQLen_Type = Gauge32
_OspfVirtNbrLSRetransQLen_Object = MibTableColumn
ospfVirtNbrLSRetransQLen = _OspfVirtNbrLSRetransQLen_Object(
    (1, 3, 6, 1, 2, 1, 13, 11, 1, 7),
    _OspfVirtNbrLSRetransQLen_Type()
)
ospfVirtNbrLSRetransQLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfVirtNbrLSRetransQLen.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RFC1252-MIB",
    **{"AreaID": AreaID,
       "RouterID": RouterID,
       "Metric": Metric,
       "BigMetric": BigMetric,
       "TruthValue": TruthValue,
       "Status": Status,
       "Validation": Validation,
       "PositiveInteger": PositiveInteger,
       "HelloRange": HelloRange,
       "UpToMaxAge": UpToMaxAge,
       "InterfaceIndex": InterfaceIndex,
       "DesignatedRouterPriority": DesignatedRouterPriority,
       "TOSType": TOSType,
       "ospf": ospf,
       "ospfGeneralGroup": ospfGeneralGroup,
       "ospfRouterId": ospfRouterId,
       "ospfAdminStat": ospfAdminStat,
       "ospfVersionNumber": ospfVersionNumber,
       "ospfAreaBdrRtrStatus": ospfAreaBdrRtrStatus,
       "ospfASBdrRtrStatus": ospfASBdrRtrStatus,
       "ospfExternLSACount": ospfExternLSACount,
       "ospfExternLSACksumSum": ospfExternLSACksumSum,
       "ospfTOSSupport": ospfTOSSupport,
       "ospfOriginateNewLSAs": ospfOriginateNewLSAs,
       "ospfRxNewLSAs": ospfRxNewLSAs,
       "ospfAreaTable": ospfAreaTable,
       "ospfAreaEntry": ospfAreaEntry,
       "ospfAreaId": ospfAreaId,
       "ospfAuthType": ospfAuthType,
       "ospfImportASExtern": ospfImportASExtern,
       "ospfSpfRuns": ospfSpfRuns,
       "ospfAreaBdrRtrCount": ospfAreaBdrRtrCount,
       "ospfASBdrRtrCount": ospfASBdrRtrCount,
       "ospfAreaLSACount": ospfAreaLSACount,
       "ospfAreaLSACksumSum": ospfAreaLSACksumSum,
       "ospfStubAreaTable": ospfStubAreaTable,
       "ospfStubAreaEntry": ospfStubAreaEntry,
       "ospfStubAreaID": ospfStubAreaID,
       "ospfStubTOS": ospfStubTOS,
       "ospfStubMetric": ospfStubMetric,
       "ospfStubStatus": ospfStubStatus,
       "ospfLsdbTable": ospfLsdbTable,
       "ospfLsdbEntry": ospfLsdbEntry,
       "ospfLsdbAreaId": ospfLsdbAreaId,
       "ospfLsdbType": ospfLsdbType,
       "ospfLsdbLSID": ospfLsdbLSID,
       "ospfLsdbRouterId": ospfLsdbRouterId,
       "ospfLsdbSequence": ospfLsdbSequence,
       "ospfLsdbAge": ospfLsdbAge,
       "ospfLsdbChecksum": ospfLsdbChecksum,
       "ospfLsdbAdvertisement": ospfLsdbAdvertisement,
       "ospfAreaRangeTable": ospfAreaRangeTable,
       "ospfAreaRangeEntry": ospfAreaRangeEntry,
       "ospfAreaRangeAreaID": ospfAreaRangeAreaID,
       "ospfAreaRangeNet": ospfAreaRangeNet,
       "ospfAreaRangeMask": ospfAreaRangeMask,
       "ospfAreaRangeStatus": ospfAreaRangeStatus,
       "ospfHostTable": ospfHostTable,
       "ospfHostEntry": ospfHostEntry,
       "ospfHostIpAddress": ospfHostIpAddress,
       "ospfHostTOS": ospfHostTOS,
       "ospfHostMetric": ospfHostMetric,
       "ospfHostStatus": ospfHostStatus,
       "ospfIfTable": ospfIfTable,
       "ospfIfEntry": ospfIfEntry,
       "ospfIfIpAddress": ospfIfIpAddress,
       "ospfAddressLessIf": ospfAddressLessIf,
       "ospfIfAreaId": ospfIfAreaId,
       "ospfIfType": ospfIfType,
       "ospfIfAdminStat": ospfIfAdminStat,
       "ospfIfRtrPriority": ospfIfRtrPriority,
       "ospfIfTransitDelay": ospfIfTransitDelay,
       "ospfIfRetransInterval": ospfIfRetransInterval,
       "ospfIfHelloInterval": ospfIfHelloInterval,
       "ospfIfRtrDeadInterval": ospfIfRtrDeadInterval,
       "ospfIfPollInterval": ospfIfPollInterval,
       "ospfIfState": ospfIfState,
       "ospfIfDesignatedRouter": ospfIfDesignatedRouter,
       "ospfIfBackupDesignatedRouter": ospfIfBackupDesignatedRouter,
       "ospfIfEvents": ospfIfEvents,
       "ospfIfAuthKey": ospfIfAuthKey,
       "ospfIfMetricTable": ospfIfMetricTable,
       "ospfIfMetricEntry": ospfIfMetricEntry,
       "ospfIfMetricIpAddress": ospfIfMetricIpAddress,
       "ospfIfMetricAddressLessIf": ospfIfMetricAddressLessIf,
       "ospfIfMetricTOS": ospfIfMetricTOS,
       "ospfIfMetricMetric": ospfIfMetricMetric,
       "ospfIfMetricStatus": ospfIfMetricStatus,
       "ospfVirtIfTable": ospfVirtIfTable,
       "ospfVirtIfEntry": ospfVirtIfEntry,
       "ospfVirtIfAreaID": ospfVirtIfAreaID,
       "ospfVirtIfNeighbor": ospfVirtIfNeighbor,
       "ospfVirtIfTransitDelay": ospfVirtIfTransitDelay,
       "ospfVirtIfRetransInterval": ospfVirtIfRetransInterval,
       "ospfVirtIfHelloInterval": ospfVirtIfHelloInterval,
       "ospfVirtIfRtrDeadInterval": ospfVirtIfRtrDeadInterval,
       "ospfVirtIfState": ospfVirtIfState,
       "ospfVirtIfEvents": ospfVirtIfEvents,
       "ospfVirtIfAuthKey": ospfVirtIfAuthKey,
       "ospfVirtIfStatus": ospfVirtIfStatus,
       "ospfNbrTable": ospfNbrTable,
       "ospfNbrEntry": ospfNbrEntry,
       "ospfNbrIpAddr": ospfNbrIpAddr,
       "ospfNbrAddressLessIndex": ospfNbrAddressLessIndex,
       "ospfNbrRtrId": ospfNbrRtrId,
       "ospfNbrOptions": ospfNbrOptions,
       "ospfNbrPriority": ospfNbrPriority,
       "ospfNbrState": ospfNbrState,
       "ospfNbrEvents": ospfNbrEvents,
       "ospfNbrLSRetransQLen": ospfNbrLSRetransQLen,
       "ospfNBMANbrStatus": ospfNBMANbrStatus,
       "ospfVirtNbrTable": ospfVirtNbrTable,
       "ospfVirtNbrEntry": ospfVirtNbrEntry,
       "ospfVirtNbrArea": ospfVirtNbrArea,
       "ospfVirtNbrRtrId": ospfVirtNbrRtrId,
       "ospfVirtNbrIpAddr": ospfVirtNbrIpAddr,
       "ospfVirtNbrOptions": ospfVirtNbrOptions,
       "ospfVirtNbrState": ospfVirtNbrState,
       "ospfVirtNbrEvents": ospfVirtNbrEvents,
       "ospfVirtNbrLSRetransQLen": ospfVirtNbrLSRetransQLen}
)
