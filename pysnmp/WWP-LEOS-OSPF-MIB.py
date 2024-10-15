# SNMP MIB module (WWP-LEOS-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:01 2024
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

(AreaID,) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID")

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

(wwpModulesLeos,) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosOspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31)
)
wwpLeosOspfMIB.setRevisions(
        ("2001-04-03 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OspfOperStatus(Integer32, TextualConvention):
    status = "current"
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
        *(("operStatusActFailed", 5),
          ("operStatusDown", 2),
          ("operStatusGoingDown", 4),
          ("operStatusGoingUp", 3),
          ("operStatusUp", 1))
    )



# MIB Managed Objects in the order of their OIDs

_WwpLeosOspfMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosOspfMIBObjects = _WwpLeosOspfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1)
)
_WwpLeosOspfGeneralGroup_ObjectIdentity = ObjectIdentity
wwpLeosOspfGeneralGroup = _WwpLeosOspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1)
)


class _WwpLeosOspfRFC1583Comp_Type(TruthValue):
    """Custom type wwpLeosOspfRFC1583Comp based on TruthValue"""


_WwpLeosOspfRFC1583Comp_Object = MibScalar
wwpLeosOspfRFC1583Comp = _WwpLeosOspfRFC1583Comp_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1, 1),
    _WwpLeosOspfRFC1583Comp_Type()
)
wwpLeosOspfRFC1583Comp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOspfRFC1583Comp.setStatus("current")
_WwpLeosOspfOperStatus_Type = OspfOperStatus
_WwpLeosOspfOperStatus_Object = MibScalar
wwpLeosOspfOperStatus = _WwpLeosOspfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1, 2),
    _WwpLeosOspfOperStatus_Type()
)
wwpLeosOspfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfOperStatus.setStatus("current")


class _WwpLeosOspfOpaqueLsaSupport_Type(TruthValue):
    """Custom type wwpLeosOspfOpaqueLsaSupport based on TruthValue"""


_WwpLeosOspfOpaqueLsaSupport_Object = MibScalar
wwpLeosOspfOpaqueLsaSupport = _WwpLeosOspfOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1, 3),
    _WwpLeosOspfOpaqueLsaSupport_Type()
)
wwpLeosOspfOpaqueLsaSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOspfOpaqueLsaSupport.setStatus("current")


class _WwpLeosOspfTrafficEngSupport_Type(TruthValue):
    """Custom type wwpLeosOspfTrafficEngSupport based on TruthValue"""


_WwpLeosOspfTrafficEngSupport_Object = MibScalar
wwpLeosOspfTrafficEngSupport = _WwpLeosOspfTrafficEngSupport_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1, 4),
    _WwpLeosOspfTrafficEngSupport_Type()
)
wwpLeosOspfTrafficEngSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfTrafficEngSupport.setStatus("current")
_WwpLeosOspfExtOpLsaCount_Type = Gauge32
_WwpLeosOspfExtOpLsaCount_Object = MibScalar
wwpLeosOspfExtOpLsaCount = _WwpLeosOspfExtOpLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1, 5),
    _WwpLeosOspfExtOpLsaCount_Type()
)
wwpLeosOspfExtOpLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfExtOpLsaCount.setStatus("current")
_WwpLeosOspfExtOpLsaCksumSum_Type = Integer32
_WwpLeosOspfExtOpLsaCksumSum_Object = MibScalar
wwpLeosOspfExtOpLsaCksumSum = _WwpLeosOspfExtOpLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1, 6),
    _WwpLeosOspfExtOpLsaCksumSum_Type()
)
wwpLeosOspfExtOpLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfExtOpLsaCksumSum.setStatus("current")
_WwpLeosOspfNumUpdPending_Type = Unsigned32
_WwpLeosOspfNumUpdPending_Object = MibScalar
wwpLeosOspfNumUpdPending = _WwpLeosOspfNumUpdPending_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1, 7),
    _WwpLeosOspfNumUpdPending_Type()
)
wwpLeosOspfNumUpdPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfNumUpdPending.setStatus("current")
_WwpLeosOspfNumUpdMerged_Type = Unsigned32
_WwpLeosOspfNumUpdMerged_Object = MibScalar
wwpLeosOspfNumUpdMerged = _WwpLeosOspfNumUpdMerged_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1, 8),
    _WwpLeosOspfNumUpdMerged_Type()
)
wwpLeosOspfNumUpdMerged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfNumUpdMerged.setStatus("current")
_WwpLeosOspfNumCksumsPending_Type = Unsigned32
_WwpLeosOspfNumCksumsPending_Object = MibScalar
wwpLeosOspfNumCksumsPending = _WwpLeosOspfNumCksumsPending_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1, 9),
    _WwpLeosOspfNumCksumsPending_Type()
)
wwpLeosOspfNumCksumsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfNumCksumsPending.setStatus("current")


class _WwpLeosOspfCalcMaxDelay_Type(Unsigned32):
    """Custom type wwpLeosOspfCalcMaxDelay based on Unsigned32"""
    defaultValue = 5000


_WwpLeosOspfCalcMaxDelay_Object = MibScalar
wwpLeosOspfCalcMaxDelay = _WwpLeosOspfCalcMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 1, 10),
    _WwpLeosOspfCalcMaxDelay_Type()
)
wwpLeosOspfCalcMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOspfCalcMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOspfCalcMaxDelay.setUnits("milliseconds")
_WwpLeosOspf_ObjectIdentity = ObjectIdentity
wwpLeosOspf = _WwpLeosOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2)
)
_WwpLeosOspfAreaTable_Object = MibTable
wwpLeosOspfAreaTable = _WwpLeosOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosOspfAreaTable.setStatus("current")
_WwpLeosOspfAreaEntry_Object = MibTableRow
wwpLeosOspfAreaEntry = _WwpLeosOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1)
)
wwpLeosOspfAreaEntry.setIndexNames(
    (0, "WWP-LEOS-OSPF-MIB", "wwpLeosOspfAreaId"),
)
if mibBuilder.loadTexts:
    wwpLeosOspfAreaEntry.setStatus("current")
_WwpLeosOspfAreaId_Type = AreaID
_WwpLeosOspfAreaId_Object = MibTableColumn
wwpLeosOspfAreaId = _WwpLeosOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 1),
    _WwpLeosOspfAreaId_Type()
)
wwpLeosOspfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaId.setStatus("current")


class _WwpLeosOspfAreaTransitCapability_Type(TruthValue):
    """Custom type wwpLeosOspfAreaTransitCapability based on TruthValue"""


_WwpLeosOspfAreaTransitCapability_Object = MibTableColumn
wwpLeosOspfAreaTransitCapability = _WwpLeosOspfAreaTransitCapability_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 2),
    _WwpLeosOspfAreaTransitCapability_Type()
)
wwpLeosOspfAreaTransitCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaTransitCapability.setStatus("current")
_WwpLeosOspfAreaRtrLsaCount_Type = Gauge32
_WwpLeosOspfAreaRtrLsaCount_Object = MibTableColumn
wwpLeosOspfAreaRtrLsaCount = _WwpLeosOspfAreaRtrLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 3),
    _WwpLeosOspfAreaRtrLsaCount_Type()
)
wwpLeosOspfAreaRtrLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaRtrLsaCount.setStatus("current")
_WwpLeosOspfAreaRtrLsaCksumSum_Type = Integer32
_WwpLeosOspfAreaRtrLsaCksumSum_Object = MibTableColumn
wwpLeosOspfAreaRtrLsaCksumSum = _WwpLeosOspfAreaRtrLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 4),
    _WwpLeosOspfAreaRtrLsaCksumSum_Type()
)
wwpLeosOspfAreaRtrLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaRtrLsaCksumSum.setStatus("current")
_WwpLeosOspfAreaNetLsaCount_Type = Gauge32
_WwpLeosOspfAreaNetLsaCount_Object = MibTableColumn
wwpLeosOspfAreaNetLsaCount = _WwpLeosOspfAreaNetLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 5),
    _WwpLeosOspfAreaNetLsaCount_Type()
)
wwpLeosOspfAreaNetLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaNetLsaCount.setStatus("current")
_WwpLeosOspfAreaNetLsaCksumSum_Type = Integer32
_WwpLeosOspfAreaNetLsaCksumSum_Object = MibTableColumn
wwpLeosOspfAreaNetLsaCksumSum = _WwpLeosOspfAreaNetLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 6),
    _WwpLeosOspfAreaNetLsaCksumSum_Type()
)
wwpLeosOspfAreaNetLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaNetLsaCksumSum.setStatus("current")
_WwpLeosOspfAreaSummLsaCount_Type = Gauge32
_WwpLeosOspfAreaSummLsaCount_Object = MibTableColumn
wwpLeosOspfAreaSummLsaCount = _WwpLeosOspfAreaSummLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 7),
    _WwpLeosOspfAreaSummLsaCount_Type()
)
wwpLeosOspfAreaSummLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaSummLsaCount.setStatus("current")
_WwpLeosOspfAreaSummLsaCksumSum_Type = Integer32
_WwpLeosOspfAreaSummLsaCksumSum_Object = MibTableColumn
wwpLeosOspfAreaSummLsaCksumSum = _WwpLeosOspfAreaSummLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 8),
    _WwpLeosOspfAreaSummLsaCksumSum_Type()
)
wwpLeosOspfAreaSummLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaSummLsaCksumSum.setStatus("current")
_WwpLeosOspfAreaSummAsLsaCount_Type = Gauge32
_WwpLeosOspfAreaSummAsLsaCount_Object = MibTableColumn
wwpLeosOspfAreaSummAsLsaCount = _WwpLeosOspfAreaSummAsLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 9),
    _WwpLeosOspfAreaSummAsLsaCount_Type()
)
wwpLeosOspfAreaSummAsLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaSummAsLsaCount.setStatus("current")
_WwpLeosOspfAreaSummAsLsaCksumSum_Type = Integer32
_WwpLeosOspfAreaSummAsLsaCksumSum_Object = MibTableColumn
wwpLeosOspfAreaSummAsLsaCksumSum = _WwpLeosOspfAreaSummAsLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 10),
    _WwpLeosOspfAreaSummAsLsaCksumSum_Type()
)
wwpLeosOspfAreaSummAsLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaSummAsLsaCksumSum.setStatus("current")
_WwpLeosOspfAreaNssaLsaCount_Type = Gauge32
_WwpLeosOspfAreaNssaLsaCount_Object = MibTableColumn
wwpLeosOspfAreaNssaLsaCount = _WwpLeosOspfAreaNssaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 11),
    _WwpLeosOspfAreaNssaLsaCount_Type()
)
wwpLeosOspfAreaNssaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaNssaLsaCount.setStatus("current")
_WwpLeosOspfAreaNssaLsaCksumSum_Type = Integer32
_WwpLeosOspfAreaNssaLsaCksumSum_Object = MibTableColumn
wwpLeosOspfAreaNssaLsaCksumSum = _WwpLeosOspfAreaNssaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 12),
    _WwpLeosOspfAreaNssaLsaCksumSum_Type()
)
wwpLeosOspfAreaNssaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaNssaLsaCksumSum.setStatus("current")
_WwpLeosOspfAreaOpLsaCount_Type = Gauge32
_WwpLeosOspfAreaOpLsaCount_Object = MibTableColumn
wwpLeosOspfAreaOpLsaCount = _WwpLeosOspfAreaOpLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 13),
    _WwpLeosOspfAreaOpLsaCount_Type()
)
wwpLeosOspfAreaOpLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaOpLsaCount.setStatus("current")
_WwpLeosOspfAreaOpLsaCksumSum_Type = Integer32
_WwpLeosOspfAreaOpLsaCksumSum_Object = MibTableColumn
wwpLeosOspfAreaOpLsaCksumSum = _WwpLeosOspfAreaOpLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 1, 1, 14),
    _WwpLeosOspfAreaOpLsaCksumSum_Type()
)
wwpLeosOspfAreaOpLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfAreaOpLsaCksumSum.setStatus("current")
_WwpLeosOspfIfTable_Object = MibTable
wwpLeosOspfIfTable = _WwpLeosOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 2)
)
if mibBuilder.loadTexts:
    wwpLeosOspfIfTable.setStatus("current")
_WwpLeosOspfIfEntry_Object = MibTableRow
wwpLeosOspfIfEntry = _WwpLeosOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 2, 1)
)
wwpLeosOspfIfEntry.setIndexNames(
    (0, "WWP-LEOS-OSPF-MIB", "wwpLeosOspfIfIpAddress"),
    (0, "WWP-LEOS-OSPF-MIB", "wwpLeosOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    wwpLeosOspfIfEntry.setStatus("current")
_WwpLeosOspfIfIpAddress_Type = IpAddress
_WwpLeosOspfIfIpAddress_Object = MibTableColumn
wwpLeosOspfIfIpAddress = _WwpLeosOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 2, 1, 1),
    _WwpLeosOspfIfIpAddress_Type()
)
wwpLeosOspfIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosOspfIfIpAddress.setStatus("current")
_WwpLeosOspfAddressLessIf_Type = Integer32
_WwpLeosOspfAddressLessIf_Object = MibTableColumn
wwpLeosOspfAddressLessIf = _WwpLeosOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 2, 1, 2),
    _WwpLeosOspfAddressLessIf_Type()
)
wwpLeosOspfAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosOspfAddressLessIf.setStatus("current")
_WwpLeosOspfIfLsaCount_Type = Gauge32
_WwpLeosOspfIfLsaCount_Object = MibTableColumn
wwpLeosOspfIfLsaCount = _WwpLeosOspfIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 2, 1, 3),
    _WwpLeosOspfIfLsaCount_Type()
)
wwpLeosOspfIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfIfLsaCount.setStatus("current")
_WwpLeosOspfIfLsaCksumSum_Type = Integer32
_WwpLeosOspfIfLsaCksumSum_Object = MibTableColumn
wwpLeosOspfIfLsaCksumSum = _WwpLeosOspfIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 2, 1, 4),
    _WwpLeosOspfIfLsaCksumSum_Type()
)
wwpLeosOspfIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfIfLsaCksumSum.setStatus("current")
_WwpLeosOspfIfOperStatus_Type = OspfOperStatus
_WwpLeosOspfIfOperStatus_Object = MibTableColumn
wwpLeosOspfIfOperStatus = _WwpLeosOspfIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 2, 1, 5),
    _WwpLeosOspfIfOperStatus_Type()
)
wwpLeosOspfIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfIfOperStatus.setStatus("current")
_WwpLeosOspfIfNetMask_Type = IpAddress
_WwpLeosOspfIfNetMask_Object = MibTableColumn
wwpLeosOspfIfNetMask = _WwpLeosOspfIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 2, 1, 6),
    _WwpLeosOspfIfNetMask_Type()
)
wwpLeosOspfIfNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosOspfIfNetMask.setStatus("current")


class _WwpLeosOspfIfTransmitTimerDelay_Type(Integer32):
    """Custom type wwpLeosOspfIfTransmitTimerDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496999),
    )


_WwpLeosOspfIfTransmitTimerDelay_Type.__name__ = "Integer32"
_WwpLeosOspfIfTransmitTimerDelay_Object = MibTableColumn
wwpLeosOspfIfTransmitTimerDelay = _WwpLeosOspfIfTransmitTimerDelay_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 31, 1, 2, 2, 1, 7),
    _WwpLeosOspfIfTransmitTimerDelay_Type()
)
wwpLeosOspfIfTransmitTimerDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wwpLeosOspfIfTransmitTimerDelay.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosOspfIfTransmitTimerDelay.setUnits("milliseconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-OSPF-MIB",
    **{"OspfOperStatus": OspfOperStatus,
       "wwpLeosOspfMIB": wwpLeosOspfMIB,
       "wwpLeosOspfMIBObjects": wwpLeosOspfMIBObjects,
       "wwpLeosOspfGeneralGroup": wwpLeosOspfGeneralGroup,
       "wwpLeosOspfRFC1583Comp": wwpLeosOspfRFC1583Comp,
       "wwpLeosOspfOperStatus": wwpLeosOspfOperStatus,
       "wwpLeosOspfOpaqueLsaSupport": wwpLeosOspfOpaqueLsaSupport,
       "wwpLeosOspfTrafficEngSupport": wwpLeosOspfTrafficEngSupport,
       "wwpLeosOspfExtOpLsaCount": wwpLeosOspfExtOpLsaCount,
       "wwpLeosOspfExtOpLsaCksumSum": wwpLeosOspfExtOpLsaCksumSum,
       "wwpLeosOspfNumUpdPending": wwpLeosOspfNumUpdPending,
       "wwpLeosOspfNumUpdMerged": wwpLeosOspfNumUpdMerged,
       "wwpLeosOspfNumCksumsPending": wwpLeosOspfNumCksumsPending,
       "wwpLeosOspfCalcMaxDelay": wwpLeosOspfCalcMaxDelay,
       "wwpLeosOspf": wwpLeosOspf,
       "wwpLeosOspfAreaTable": wwpLeosOspfAreaTable,
       "wwpLeosOspfAreaEntry": wwpLeosOspfAreaEntry,
       "wwpLeosOspfAreaId": wwpLeosOspfAreaId,
       "wwpLeosOspfAreaTransitCapability": wwpLeosOspfAreaTransitCapability,
       "wwpLeosOspfAreaRtrLsaCount": wwpLeosOspfAreaRtrLsaCount,
       "wwpLeosOspfAreaRtrLsaCksumSum": wwpLeosOspfAreaRtrLsaCksumSum,
       "wwpLeosOspfAreaNetLsaCount": wwpLeosOspfAreaNetLsaCount,
       "wwpLeosOspfAreaNetLsaCksumSum": wwpLeosOspfAreaNetLsaCksumSum,
       "wwpLeosOspfAreaSummLsaCount": wwpLeosOspfAreaSummLsaCount,
       "wwpLeosOspfAreaSummLsaCksumSum": wwpLeosOspfAreaSummLsaCksumSum,
       "wwpLeosOspfAreaSummAsLsaCount": wwpLeosOspfAreaSummAsLsaCount,
       "wwpLeosOspfAreaSummAsLsaCksumSum": wwpLeosOspfAreaSummAsLsaCksumSum,
       "wwpLeosOspfAreaNssaLsaCount": wwpLeosOspfAreaNssaLsaCount,
       "wwpLeosOspfAreaNssaLsaCksumSum": wwpLeosOspfAreaNssaLsaCksumSum,
       "wwpLeosOspfAreaOpLsaCount": wwpLeosOspfAreaOpLsaCount,
       "wwpLeosOspfAreaOpLsaCksumSum": wwpLeosOspfAreaOpLsaCksumSum,
       "wwpLeosOspfIfTable": wwpLeosOspfIfTable,
       "wwpLeosOspfIfEntry": wwpLeosOspfIfEntry,
       "wwpLeosOspfIfIpAddress": wwpLeosOspfIfIpAddress,
       "wwpLeosOspfAddressLessIf": wwpLeosOspfAddressLessIf,
       "wwpLeosOspfIfLsaCount": wwpLeosOspfIfLsaCount,
       "wwpLeosOspfIfLsaCksumSum": wwpLeosOspfIfLsaCksumSum,
       "wwpLeosOspfIfOperStatus": wwpLeosOspfIfOperStatus,
       "wwpLeosOspfIfNetMask": wwpLeosOspfIfNetMask,
       "wwpLeosOspfIfTransmitTimerDelay": wwpLeosOspfIfTransmitTimerDelay}
)
