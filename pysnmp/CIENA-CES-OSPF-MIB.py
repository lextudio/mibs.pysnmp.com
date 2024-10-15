# SNMP MIB module (CIENA-CES-OSPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CIENA-CES-OSPF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:55:03 2024
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

(cienaCesConfig,) = mibBuilder.importSymbols(
    "CIENA-SMI",
    "cienaCesConfig")

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


# MODULE-IDENTITY

cienaCesOspfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19)
)
cienaCesOspfMIB.setRevisions(
        ("2013-04-18 00:00",
         "2011-02-02 00:00")
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

_CienaCesOspfMIBObjects_ObjectIdentity = ObjectIdentity
cienaCesOspfMIBObjects = _CienaCesOspfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1)
)
_CienaCesOspfGeneralGroup_ObjectIdentity = ObjectIdentity
cienaCesOspfGeneralGroup = _CienaCesOspfGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1)
)


class _CienaCesOspfRFC1583Comp_Type(TruthValue):
    """Custom type cienaCesOspfRFC1583Comp based on TruthValue"""


_CienaCesOspfRFC1583Comp_Object = MibScalar
cienaCesOspfRFC1583Comp = _CienaCesOspfRFC1583Comp_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 1),
    _CienaCesOspfRFC1583Comp_Type()
)
cienaCesOspfRFC1583Comp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfRFC1583Comp.setStatus("current")
_CienaCesOspfOperStatus_Type = OspfOperStatus
_CienaCesOspfOperStatus_Object = MibScalar
cienaCesOspfOperStatus = _CienaCesOspfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 2),
    _CienaCesOspfOperStatus_Type()
)
cienaCesOspfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfOperStatus.setStatus("current")


class _CienaCesOspfOpaqueLsaSupport_Type(TruthValue):
    """Custom type cienaCesOspfOpaqueLsaSupport based on TruthValue"""


_CienaCesOspfOpaqueLsaSupport_Object = MibScalar
cienaCesOspfOpaqueLsaSupport = _CienaCesOspfOpaqueLsaSupport_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 3),
    _CienaCesOspfOpaqueLsaSupport_Type()
)
cienaCesOspfOpaqueLsaSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfOpaqueLsaSupport.setStatus("current")


class _CienaCesOspfTrafficEngSupport_Type(TruthValue):
    """Custom type cienaCesOspfTrafficEngSupport based on TruthValue"""


_CienaCesOspfTrafficEngSupport_Object = MibScalar
cienaCesOspfTrafficEngSupport = _CienaCesOspfTrafficEngSupport_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 4),
    _CienaCesOspfTrafficEngSupport_Type()
)
cienaCesOspfTrafficEngSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfTrafficEngSupport.setStatus("current")
_CienaCesOspfExtOpLsaCount_Type = Gauge32
_CienaCesOspfExtOpLsaCount_Object = MibScalar
cienaCesOspfExtOpLsaCount = _CienaCesOspfExtOpLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 5),
    _CienaCesOspfExtOpLsaCount_Type()
)
cienaCesOspfExtOpLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfExtOpLsaCount.setStatus("current")
_CienaCesOspfExtOpLsaCksumSum_Type = Integer32
_CienaCesOspfExtOpLsaCksumSum_Object = MibScalar
cienaCesOspfExtOpLsaCksumSum = _CienaCesOspfExtOpLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 6),
    _CienaCesOspfExtOpLsaCksumSum_Type()
)
cienaCesOspfExtOpLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfExtOpLsaCksumSum.setStatus("current")
_CienaCesOspfNumUpdPending_Type = Unsigned32
_CienaCesOspfNumUpdPending_Object = MibScalar
cienaCesOspfNumUpdPending = _CienaCesOspfNumUpdPending_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 7),
    _CienaCesOspfNumUpdPending_Type()
)
cienaCesOspfNumUpdPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfNumUpdPending.setStatus("current")
_CienaCesOspfNumUpdMerged_Type = Unsigned32
_CienaCesOspfNumUpdMerged_Object = MibScalar
cienaCesOspfNumUpdMerged = _CienaCesOspfNumUpdMerged_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 8),
    _CienaCesOspfNumUpdMerged_Type()
)
cienaCesOspfNumUpdMerged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfNumUpdMerged.setStatus("current")
_CienaCesOspfNumCksumsPending_Type = Unsigned32
_CienaCesOspfNumCksumsPending_Object = MibScalar
cienaCesOspfNumCksumsPending = _CienaCesOspfNumCksumsPending_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 9),
    _CienaCesOspfNumCksumsPending_Type()
)
cienaCesOspfNumCksumsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfNumCksumsPending.setStatus("current")


class _CienaCesOspfCalcMaxDelay_Type(Unsigned32):
    """Custom type cienaCesOspfCalcMaxDelay based on Unsigned32"""
    defaultValue = 5000


_CienaCesOspfCalcMaxDelay_Object = MibScalar
cienaCesOspfCalcMaxDelay = _CienaCesOspfCalcMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 10),
    _CienaCesOspfCalcMaxDelay_Type()
)
cienaCesOspfCalcMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfCalcMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOspfCalcMaxDelay.setUnits("milliseconds")
_CienaCesOspfRouterId_Type = IpAddress
_CienaCesOspfRouterId_Object = MibScalar
cienaCesOspfRouterId = _CienaCesOspfRouterId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 1, 11),
    _CienaCesOspfRouterId_Type()
)
cienaCesOspfRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfRouterId.setStatus("current")
_CienaCesOspf_ObjectIdentity = ObjectIdentity
cienaCesOspf = _CienaCesOspf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2)
)
_CienaCesOspfAreaTable_Object = MibTable
cienaCesOspfAreaTable = _CienaCesOspfAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cienaCesOspfAreaTable.setStatus("current")
_CienaCesOspfAreaEntry_Object = MibTableRow
cienaCesOspfAreaEntry = _CienaCesOspfAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1)
)
cienaCesOspfAreaEntry.setIndexNames(
    (0, "CIENA-CES-OSPF-MIB", "cienaCesOspfAreaId"),
)
if mibBuilder.loadTexts:
    cienaCesOspfAreaEntry.setStatus("current")
_CienaCesOspfAreaId_Type = AreaID
_CienaCesOspfAreaId_Object = MibTableColumn
cienaCesOspfAreaId = _CienaCesOspfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 1),
    _CienaCesOspfAreaId_Type()
)
cienaCesOspfAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOspfAreaId.setStatus("current")


class _CienaCesOspfAreaTransitCapability_Type(TruthValue):
    """Custom type cienaCesOspfAreaTransitCapability based on TruthValue"""


_CienaCesOspfAreaTransitCapability_Object = MibTableColumn
cienaCesOspfAreaTransitCapability = _CienaCesOspfAreaTransitCapability_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 2),
    _CienaCesOspfAreaTransitCapability_Type()
)
cienaCesOspfAreaTransitCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaTransitCapability.setStatus("current")
_CienaCesOspfAreaRtrLsaCount_Type = Gauge32
_CienaCesOspfAreaRtrLsaCount_Object = MibTableColumn
cienaCesOspfAreaRtrLsaCount = _CienaCesOspfAreaRtrLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 3),
    _CienaCesOspfAreaRtrLsaCount_Type()
)
cienaCesOspfAreaRtrLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaRtrLsaCount.setStatus("current")
_CienaCesOspfAreaRtrLsaCksumSum_Type = Integer32
_CienaCesOspfAreaRtrLsaCksumSum_Object = MibTableColumn
cienaCesOspfAreaRtrLsaCksumSum = _CienaCesOspfAreaRtrLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 4),
    _CienaCesOspfAreaRtrLsaCksumSum_Type()
)
cienaCesOspfAreaRtrLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaRtrLsaCksumSum.setStatus("current")
_CienaCesOspfAreaNetLsaCount_Type = Gauge32
_CienaCesOspfAreaNetLsaCount_Object = MibTableColumn
cienaCesOspfAreaNetLsaCount = _CienaCesOspfAreaNetLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 5),
    _CienaCesOspfAreaNetLsaCount_Type()
)
cienaCesOspfAreaNetLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaNetLsaCount.setStatus("current")
_CienaCesOspfAreaNetLsaCksumSum_Type = Integer32
_CienaCesOspfAreaNetLsaCksumSum_Object = MibTableColumn
cienaCesOspfAreaNetLsaCksumSum = _CienaCesOspfAreaNetLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 6),
    _CienaCesOspfAreaNetLsaCksumSum_Type()
)
cienaCesOspfAreaNetLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaNetLsaCksumSum.setStatus("current")
_CienaCesOspfAreaSummLsaCount_Type = Gauge32
_CienaCesOspfAreaSummLsaCount_Object = MibTableColumn
cienaCesOspfAreaSummLsaCount = _CienaCesOspfAreaSummLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 7),
    _CienaCesOspfAreaSummLsaCount_Type()
)
cienaCesOspfAreaSummLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaSummLsaCount.setStatus("current")
_CienaCesOspfAreaSummLsaCksumSum_Type = Integer32
_CienaCesOspfAreaSummLsaCksumSum_Object = MibTableColumn
cienaCesOspfAreaSummLsaCksumSum = _CienaCesOspfAreaSummLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 8),
    _CienaCesOspfAreaSummLsaCksumSum_Type()
)
cienaCesOspfAreaSummLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaSummLsaCksumSum.setStatus("current")
_CienaCesOspfAreaSummAsLsaCount_Type = Gauge32
_CienaCesOspfAreaSummAsLsaCount_Object = MibTableColumn
cienaCesOspfAreaSummAsLsaCount = _CienaCesOspfAreaSummAsLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 9),
    _CienaCesOspfAreaSummAsLsaCount_Type()
)
cienaCesOspfAreaSummAsLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaSummAsLsaCount.setStatus("current")
_CienaCesOspfAreaSummAsLsaCksumSum_Type = Integer32
_CienaCesOspfAreaSummAsLsaCksumSum_Object = MibTableColumn
cienaCesOspfAreaSummAsLsaCksumSum = _CienaCesOspfAreaSummAsLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 10),
    _CienaCesOspfAreaSummAsLsaCksumSum_Type()
)
cienaCesOspfAreaSummAsLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaSummAsLsaCksumSum.setStatus("current")
_CienaCesOspfAreaNssaLsaCount_Type = Gauge32
_CienaCesOspfAreaNssaLsaCount_Object = MibTableColumn
cienaCesOspfAreaNssaLsaCount = _CienaCesOspfAreaNssaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 11),
    _CienaCesOspfAreaNssaLsaCount_Type()
)
cienaCesOspfAreaNssaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaNssaLsaCount.setStatus("current")
_CienaCesOspfAreaNssaLsaCksumSum_Type = Integer32
_CienaCesOspfAreaNssaLsaCksumSum_Object = MibTableColumn
cienaCesOspfAreaNssaLsaCksumSum = _CienaCesOspfAreaNssaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 12),
    _CienaCesOspfAreaNssaLsaCksumSum_Type()
)
cienaCesOspfAreaNssaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaNssaLsaCksumSum.setStatus("current")
_CienaCesOspfAreaOpLsaCount_Type = Gauge32
_CienaCesOspfAreaOpLsaCount_Object = MibTableColumn
cienaCesOspfAreaOpLsaCount = _CienaCesOspfAreaOpLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 13),
    _CienaCesOspfAreaOpLsaCount_Type()
)
cienaCesOspfAreaOpLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaOpLsaCount.setStatus("current")
_CienaCesOspfAreaOpLsaCksumSum_Type = Integer32
_CienaCesOspfAreaOpLsaCksumSum_Object = MibTableColumn
cienaCesOspfAreaOpLsaCksumSum = _CienaCesOspfAreaOpLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 1, 1, 14),
    _CienaCesOspfAreaOpLsaCksumSum_Type()
)
cienaCesOspfAreaOpLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfAreaOpLsaCksumSum.setStatus("current")
_CienaCesOspfIfTable_Object = MibTable
cienaCesOspfIfTable = _CienaCesOspfIfTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 2)
)
if mibBuilder.loadTexts:
    cienaCesOspfIfTable.setStatus("current")
_CienaCesOspfIfEntry_Object = MibTableRow
cienaCesOspfIfEntry = _CienaCesOspfIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 2, 1)
)
cienaCesOspfIfEntry.setIndexNames(
    (0, "CIENA-CES-OSPF-MIB", "cienaCesOspfIfIpAddress"),
    (0, "CIENA-CES-OSPF-MIB", "cienaCesOspfAddressLessIf"),
)
if mibBuilder.loadTexts:
    cienaCesOspfIfEntry.setStatus("current")
_CienaCesOspfIfIpAddress_Type = IpAddress
_CienaCesOspfIfIpAddress_Object = MibTableColumn
cienaCesOspfIfIpAddress = _CienaCesOspfIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 2, 1, 1),
    _CienaCesOspfIfIpAddress_Type()
)
cienaCesOspfIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOspfIfIpAddress.setStatus("current")


class _CienaCesOspfAddressLessIf_Type(Integer32):
    """Custom type cienaCesOspfAddressLessIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CienaCesOspfAddressLessIf_Type.__name__ = "Integer32"
_CienaCesOspfAddressLessIf_Object = MibTableColumn
cienaCesOspfAddressLessIf = _CienaCesOspfAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 2, 1, 2),
    _CienaCesOspfAddressLessIf_Type()
)
cienaCesOspfAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cienaCesOspfAddressLessIf.setStatus("current")
_CienaCesOspfIfLsaCount_Type = Gauge32
_CienaCesOspfIfLsaCount_Object = MibTableColumn
cienaCesOspfIfLsaCount = _CienaCesOspfIfLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 2, 1, 3),
    _CienaCesOspfIfLsaCount_Type()
)
cienaCesOspfIfLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfIfLsaCount.setStatus("current")
_CienaCesOspfIfLsaCksumSum_Type = Integer32
_CienaCesOspfIfLsaCksumSum_Object = MibTableColumn
cienaCesOspfIfLsaCksumSum = _CienaCesOspfIfLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 2, 1, 4),
    _CienaCesOspfIfLsaCksumSum_Type()
)
cienaCesOspfIfLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfIfLsaCksumSum.setStatus("current")
_CienaCesOspfIfOperStatus_Type = OspfOperStatus
_CienaCesOspfIfOperStatus_Object = MibTableColumn
cienaCesOspfIfOperStatus = _CienaCesOspfIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 2, 1, 5),
    _CienaCesOspfIfOperStatus_Type()
)
cienaCesOspfIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfIfOperStatus.setStatus("current")
_CienaCesOspfIfNetMask_Type = IpAddress
_CienaCesOspfIfNetMask_Object = MibTableColumn
cienaCesOspfIfNetMask = _CienaCesOspfIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 2, 1, 6),
    _CienaCesOspfIfNetMask_Type()
)
cienaCesOspfIfNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfIfNetMask.setStatus("current")


class _CienaCesOspfIfTransmitTimerDelay_Type(Integer32):
    """Custom type cienaCesOspfIfTransmitTimerDelay based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 429496799),
    )


_CienaCesOspfIfTransmitTimerDelay_Type.__name__ = "Integer32"
_CienaCesOspfIfTransmitTimerDelay_Object = MibTableColumn
cienaCesOspfIfTransmitTimerDelay = _CienaCesOspfIfTransmitTimerDelay_Object(
    (1, 3, 6, 1, 4, 1, 1271, 2, 1, 19, 1, 2, 2, 1, 7),
    _CienaCesOspfIfTransmitTimerDelay_Type()
)
cienaCesOspfIfTransmitTimerDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cienaCesOspfIfTransmitTimerDelay.setStatus("current")
if mibBuilder.loadTexts:
    cienaCesOspfIfTransmitTimerDelay.setUnits("milliseconds")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-CES-OSPF-MIB",
    **{"OspfOperStatus": OspfOperStatus,
       "cienaCesOspfMIB": cienaCesOspfMIB,
       "cienaCesOspfMIBObjects": cienaCesOspfMIBObjects,
       "cienaCesOspfGeneralGroup": cienaCesOspfGeneralGroup,
       "cienaCesOspfRFC1583Comp": cienaCesOspfRFC1583Comp,
       "cienaCesOspfOperStatus": cienaCesOspfOperStatus,
       "cienaCesOspfOpaqueLsaSupport": cienaCesOspfOpaqueLsaSupport,
       "cienaCesOspfTrafficEngSupport": cienaCesOspfTrafficEngSupport,
       "cienaCesOspfExtOpLsaCount": cienaCesOspfExtOpLsaCount,
       "cienaCesOspfExtOpLsaCksumSum": cienaCesOspfExtOpLsaCksumSum,
       "cienaCesOspfNumUpdPending": cienaCesOspfNumUpdPending,
       "cienaCesOspfNumUpdMerged": cienaCesOspfNumUpdMerged,
       "cienaCesOspfNumCksumsPending": cienaCesOspfNumCksumsPending,
       "cienaCesOspfCalcMaxDelay": cienaCesOspfCalcMaxDelay,
       "cienaCesOspfRouterId": cienaCesOspfRouterId,
       "cienaCesOspf": cienaCesOspf,
       "cienaCesOspfAreaTable": cienaCesOspfAreaTable,
       "cienaCesOspfAreaEntry": cienaCesOspfAreaEntry,
       "cienaCesOspfAreaId": cienaCesOspfAreaId,
       "cienaCesOspfAreaTransitCapability": cienaCesOspfAreaTransitCapability,
       "cienaCesOspfAreaRtrLsaCount": cienaCesOspfAreaRtrLsaCount,
       "cienaCesOspfAreaRtrLsaCksumSum": cienaCesOspfAreaRtrLsaCksumSum,
       "cienaCesOspfAreaNetLsaCount": cienaCesOspfAreaNetLsaCount,
       "cienaCesOspfAreaNetLsaCksumSum": cienaCesOspfAreaNetLsaCksumSum,
       "cienaCesOspfAreaSummLsaCount": cienaCesOspfAreaSummLsaCount,
       "cienaCesOspfAreaSummLsaCksumSum": cienaCesOspfAreaSummLsaCksumSum,
       "cienaCesOspfAreaSummAsLsaCount": cienaCesOspfAreaSummAsLsaCount,
       "cienaCesOspfAreaSummAsLsaCksumSum": cienaCesOspfAreaSummAsLsaCksumSum,
       "cienaCesOspfAreaNssaLsaCount": cienaCesOspfAreaNssaLsaCount,
       "cienaCesOspfAreaNssaLsaCksumSum": cienaCesOspfAreaNssaLsaCksumSum,
       "cienaCesOspfAreaOpLsaCount": cienaCesOspfAreaOpLsaCount,
       "cienaCesOspfAreaOpLsaCksumSum": cienaCesOspfAreaOpLsaCksumSum,
       "cienaCesOspfIfTable": cienaCesOspfIfTable,
       "cienaCesOspfIfEntry": cienaCesOspfIfEntry,
       "cienaCesOspfIfIpAddress": cienaCesOspfIfIpAddress,
       "cienaCesOspfAddressLessIf": cienaCesOspfAddressLessIf,
       "cienaCesOspfIfLsaCount": cienaCesOspfIfLsaCount,
       "cienaCesOspfIfLsaCksumSum": cienaCesOspfIfLsaCksumSum,
       "cienaCesOspfIfOperStatus": cienaCesOspfIfOperStatus,
       "cienaCesOspfIfNetMask": cienaCesOspfIfNetMask,
       "cienaCesOspfIfTransmitTimerDelay": cienaCesOspfIfTransmitTimerDelay}
)
