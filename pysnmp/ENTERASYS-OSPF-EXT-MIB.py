# SNMP MIB module (ENTERASYS-OSPF-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ENTERASYS-OSPF-EXT-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:39:19 2024
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(AreaID,
 Status,
 ospfAreaEntry,
 ospfIfEntry,
 ospfLocalLsdbEntry,
 ospfNbrEntry,
 ospfVirtIfEntry,
 ospfVirtNbrEntry) = mibBuilder.importSymbols(
    "OSPF-MIB",
    "AreaID",
    "Status",
    "ospfAreaEntry",
    "ospfIfEntry",
    "ospfLocalLsdbEntry",
    "ospfNbrEntry",
    "ospfVirtIfEntry",
    "ospfVirtNbrEntry")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(Bits,
 Bits,
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysOspfExtMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65)
)
etsysOspfExtMIB.setRevisions(
        ("2009-02-27 19:34",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EtsysOspfOperStatus(Integer32, TextualConvention):
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

_EtsysOspfExtObjects_ObjectIdentity = ObjectIdentity
etsysOspfExtObjects = _EtsysOspfExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1)
)
_EtsysOspfExtGlobals_ObjectIdentity = ObjectIdentity
etsysOspfExtGlobals = _EtsysOspfExtGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1)
)
_EtsysOspfExtOperStatus_Type = EtsysOspfOperStatus
_EtsysOspfExtOperStatus_Object = MibScalar
etsysOspfExtOperStatus = _EtsysOspfExtOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 1),
    _EtsysOspfExtOperStatus_Type()
)
etsysOspfExtOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtOperStatus.setStatus("current")


class _EtsysOspfExtCalcMaxDelay_Type(Unsigned32):
    """Custom type etsysOspfExtCalcMaxDelay based on Unsigned32"""
    defaultValue = 5000


_EtsysOspfExtCalcMaxDelay_Object = MibScalar
etsysOspfExtCalcMaxDelay = _EtsysOspfExtCalcMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 2),
    _EtsysOspfExtCalcMaxDelay_Type()
)
etsysOspfExtCalcMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtCalcMaxDelay.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtCalcMaxDelay.setUnits("milliseconds")


class _EtsysOspfExtCalcThrshUpdStart_Type(Integer32):
    """Custom type etsysOspfExtCalcThrshUpdStart based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysOspfExtCalcThrshUpdStart_Type.__name__ = "Integer32"
_EtsysOspfExtCalcThrshUpdStart_Object = MibScalar
etsysOspfExtCalcThrshUpdStart = _EtsysOspfExtCalcThrshUpdStart_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 3),
    _EtsysOspfExtCalcThrshUpdStart_Type()
)
etsysOspfExtCalcThrshUpdStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtCalcThrshUpdStart.setStatus("current")


class _EtsysOspfExtCalcThrshUpdRestart_Type(Integer32):
    """Custom type etsysOspfExtCalcThrshUpdRestart based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysOspfExtCalcThrshUpdRestart_Type.__name__ = "Integer32"
_EtsysOspfExtCalcThrshUpdRestart_Object = MibScalar
etsysOspfExtCalcThrshUpdRestart = _EtsysOspfExtCalcThrshUpdRestart_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 4),
    _EtsysOspfExtCalcThrshUpdRestart_Type()
)
etsysOspfExtCalcThrshUpdRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtCalcThrshUpdRestart.setStatus("current")


class _EtsysOspfExtCalcThrshIncUpdates_Type(Integer32):
    """Custom type etsysOspfExtCalcThrshIncUpdates based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysOspfExtCalcThrshIncUpdates_Type.__name__ = "Integer32"
_EtsysOspfExtCalcThrshIncUpdates_Object = MibScalar
etsysOspfExtCalcThrshIncUpdates = _EtsysOspfExtCalcThrshIncUpdates_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 5),
    _EtsysOspfExtCalcThrshIncUpdates_Type()
)
etsysOspfExtCalcThrshIncUpdates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtCalcThrshIncUpdates.setStatus("current")


class _EtsysOspfExtCalcThrshIncSpfUpd_Type(Integer32):
    """Custom type etsysOspfExtCalcThrshIncSpfUpd based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysOspfExtCalcThrshIncSpfUpd_Type.__name__ = "Integer32"
_EtsysOspfExtCalcThrshIncSpfUpd_Object = MibScalar
etsysOspfExtCalcThrshIncSpfUpd = _EtsysOspfExtCalcThrshIncSpfUpd_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 6),
    _EtsysOspfExtCalcThrshIncSpfUpd_Type()
)
etsysOspfExtCalcThrshIncSpfUpd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtCalcThrshIncSpfUpd.setStatus("current")


class _EtsysOspfExtCalcPauseFreq_Type(Integer32):
    """Custom type etsysOspfExtCalcPauseFreq based on Integer32"""
    defaultValue = 10000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysOspfExtCalcPauseFreq_Type.__name__ = "Integer32"
_EtsysOspfExtCalcPauseFreq_Object = MibScalar
etsysOspfExtCalcPauseFreq = _EtsysOspfExtCalcPauseFreq_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 7),
    _EtsysOspfExtCalcPauseFreq_Type()
)
etsysOspfExtCalcPauseFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtCalcPauseFreq.setStatus("current")


class _EtsysOspfExtRteMaxEqCostPaths_Type(Unsigned32):
    """Custom type etsysOspfExtRteMaxEqCostPaths based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_EtsysOspfExtRteMaxEqCostPaths_Type.__name__ = "Unsigned32"
_EtsysOspfExtRteMaxEqCostPaths_Object = MibScalar
etsysOspfExtRteMaxEqCostPaths = _EtsysOspfExtRteMaxEqCostPaths_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 8),
    _EtsysOspfExtRteMaxEqCostPaths_Type()
)
etsysOspfExtRteMaxEqCostPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtRteMaxEqCostPaths.setStatus("current")


class _EtsysOspfExtCheckAge_Type(Unsigned32):
    """Custom type etsysOspfExtCheckAge based on Unsigned32"""
    defaultValue = 300


_EtsysOspfExtCheckAge_Object = MibScalar
etsysOspfExtCheckAge = _EtsysOspfExtCheckAge_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 9),
    _EtsysOspfExtCheckAge_Type()
)
etsysOspfExtCheckAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtCheckAge.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtCheckAge.setUnits("seconds")


class _EtsysOspfExtExtLsaRfshIntvl_Type(Unsigned32):
    """Custom type etsysOspfExtExtLsaRfshIntvl based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_EtsysOspfExtExtLsaRfshIntvl_Type.__name__ = "Unsigned32"
_EtsysOspfExtExtLsaRfshIntvl_Object = MibScalar
etsysOspfExtExtLsaRfshIntvl = _EtsysOspfExtExtLsaRfshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 10),
    _EtsysOspfExtExtLsaRfshIntvl_Type()
)
etsysOspfExtExtLsaRfshIntvl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtExtLsaRfshIntvl.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtExtLsaRfshIntvl.setUnits("seconds")
_EtsysOspfExtExternOpLsaCount_Type = Gauge32
_EtsysOspfExtExternOpLsaCount_Object = MibScalar
etsysOspfExtExternOpLsaCount = _EtsysOspfExtExternOpLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 11),
    _EtsysOspfExtExternOpLsaCount_Type()
)
etsysOspfExtExternOpLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtExternOpLsaCount.setStatus("current")
_EtsysOspfExtExternOpLsaCksumSum_Type = Unsigned32
_EtsysOspfExtExternOpLsaCksumSum_Object = MibScalar
etsysOspfExtExternOpLsaCksumSum = _EtsysOspfExtExternOpLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 12),
    _EtsysOspfExtExternOpLsaCksumSum_Type()
)
etsysOspfExtExternOpLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtExternOpLsaCksumSum.setStatus("current")
_EtsysOspfExtNumUpdPending_Type = Gauge32
_EtsysOspfExtNumUpdPending_Object = MibScalar
etsysOspfExtNumUpdPending = _EtsysOspfExtNumUpdPending_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 13),
    _EtsysOspfExtNumUpdPending_Type()
)
etsysOspfExtNumUpdPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtNumUpdPending.setStatus("current")
_EtsysOspfExtNumUpdMerged_Type = Gauge32
_EtsysOspfExtNumUpdMerged_Object = MibScalar
etsysOspfExtNumUpdMerged = _EtsysOspfExtNumUpdMerged_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 14),
    _EtsysOspfExtNumUpdMerged_Type()
)
etsysOspfExtNumUpdMerged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtNumUpdMerged.setStatus("current")
_EtsysOspfExtNumCksumsPending_Type = Gauge32
_EtsysOspfExtNumCksumsPending_Object = MibScalar
etsysOspfExtNumCksumsPending = _EtsysOspfExtNumCksumsPending_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 15),
    _EtsysOspfExtNumCksumsPending_Type()
)
etsysOspfExtNumCksumsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtNumCksumsPending.setStatus("current")


class _EtsysOspfExtDoGraceHitless_Type(TruthValue):
    """Custom type etsysOspfExtDoGraceHitless based on TruthValue"""


_EtsysOspfExtDoGraceHitless_Object = MibScalar
etsysOspfExtDoGraceHitless = _EtsysOspfExtDoGraceHitless_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 16),
    _EtsysOspfExtDoGraceHitless_Type()
)
etsysOspfExtDoGraceHitless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtDoGraceHitless.setStatus("current")


class _EtsysOspfExtDoGraceUnplannedHitless_Type(TruthValue):
    """Custom type etsysOspfExtDoGraceUnplannedHitless based on TruthValue"""


_EtsysOspfExtDoGraceUnplannedHitless_Object = MibScalar
etsysOspfExtDoGraceUnplannedHitless = _EtsysOspfExtDoGraceUnplannedHitless_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 17),
    _EtsysOspfExtDoGraceUnplannedHitless_Type()
)
etsysOspfExtDoGraceUnplannedHitless.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtDoGraceUnplannedHitless.setStatus("current")


class _EtsysOspfExtHitlessGracePeriod_Type(Unsigned32):
    """Custom type etsysOspfExtHitlessGracePeriod based on Unsigned32"""
    defaultValue = 120

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1800),
    )


_EtsysOspfExtHitlessGracePeriod_Type.__name__ = "Unsigned32"
_EtsysOspfExtHitlessGracePeriod_Object = MibScalar
etsysOspfExtHitlessGracePeriod = _EtsysOspfExtHitlessGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 1, 18),
    _EtsysOspfExtHitlessGracePeriod_Type()
)
etsysOspfExtHitlessGracePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysOspfExtHitlessGracePeriod.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtHitlessGracePeriod.setUnits("seconds")
_EtsysOspfExtTables_ObjectIdentity = ObjectIdentity
etsysOspfExtTables = _EtsysOspfExtTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2)
)
_EtsysOspfExtAreaTable_Object = MibTable
etsysOspfExtAreaTable = _EtsysOspfExtAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysOspfExtAreaTable.setStatus("current")
_EtsysOspfExtAreaEntry_Object = MibTableRow
etsysOspfExtAreaEntry = _EtsysOspfExtAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    etsysOspfExtAreaEntry.setStatus("current")


class _EtsysOspfExtAreaAdminStatus_Type(Status):
    """Custom type etsysOspfExtAreaAdminStatus based on Status"""


_EtsysOspfExtAreaAdminStatus_Object = MibTableColumn
etsysOspfExtAreaAdminStatus = _EtsysOspfExtAreaAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 1),
    _EtsysOspfExtAreaAdminStatus_Type()
)
etsysOspfExtAreaAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtAreaAdminStatus.setStatus("current")
_EtsysOspfExtAreaOperStatus_Type = EtsysOspfOperStatus
_EtsysOspfExtAreaOperStatus_Object = MibTableColumn
etsysOspfExtAreaOperStatus = _EtsysOspfExtAreaOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 2),
    _EtsysOspfExtAreaOperStatus_Type()
)
etsysOspfExtAreaOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaOperStatus.setStatus("current")


class _EtsysOspfExtAreaTransitCapability_Type(TruthValue):
    """Custom type etsysOspfExtAreaTransitCapability based on TruthValue"""


_EtsysOspfExtAreaTransitCapability_Object = MibTableColumn
etsysOspfExtAreaTransitCapability = _EtsysOspfExtAreaTransitCapability_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 3),
    _EtsysOspfExtAreaTransitCapability_Type()
)
etsysOspfExtAreaTransitCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaTransitCapability.setStatus("current")


class _EtsysOspfExtAreaLsaRfshIntvl_Type(Unsigned32):
    """Custom type etsysOspfExtAreaLsaRfshIntvl based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_EtsysOspfExtAreaLsaRfshIntvl_Type.__name__ = "Unsigned32"
_EtsysOspfExtAreaLsaRfshIntvl_Object = MibTableColumn
etsysOspfExtAreaLsaRfshIntvl = _EtsysOspfExtAreaLsaRfshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 4),
    _EtsysOspfExtAreaLsaRfshIntvl_Type()
)
etsysOspfExtAreaLsaRfshIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtAreaLsaRfshIntvl.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtAreaLsaRfshIntvl.setUnits("seconds")
_EtsysOspfExtAreaRtrLsaCount_Type = Gauge32
_EtsysOspfExtAreaRtrLsaCount_Object = MibTableColumn
etsysOspfExtAreaRtrLsaCount = _EtsysOspfExtAreaRtrLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 5),
    _EtsysOspfExtAreaRtrLsaCount_Type()
)
etsysOspfExtAreaRtrLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaRtrLsaCount.setStatus("current")
_EtsysOspfExtAreaRtrLsaCksumSum_Type = Unsigned32
_EtsysOspfExtAreaRtrLsaCksumSum_Object = MibTableColumn
etsysOspfExtAreaRtrLsaCksumSum = _EtsysOspfExtAreaRtrLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 6),
    _EtsysOspfExtAreaRtrLsaCksumSum_Type()
)
etsysOspfExtAreaRtrLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaRtrLsaCksumSum.setStatus("current")
_EtsysOspfExtAreaNetLsaCount_Type = Gauge32
_EtsysOspfExtAreaNetLsaCount_Object = MibTableColumn
etsysOspfExtAreaNetLsaCount = _EtsysOspfExtAreaNetLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 7),
    _EtsysOspfExtAreaNetLsaCount_Type()
)
etsysOspfExtAreaNetLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaNetLsaCount.setStatus("current")
_EtsysOspfExtAreaNetLsaCksumSum_Type = Unsigned32
_EtsysOspfExtAreaNetLsaCksumSum_Object = MibTableColumn
etsysOspfExtAreaNetLsaCksumSum = _EtsysOspfExtAreaNetLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 8),
    _EtsysOspfExtAreaNetLsaCksumSum_Type()
)
etsysOspfExtAreaNetLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaNetLsaCksumSum.setStatus("current")
_EtsysOspfExtAreaSummLsaCount_Type = Gauge32
_EtsysOspfExtAreaSummLsaCount_Object = MibTableColumn
etsysOspfExtAreaSummLsaCount = _EtsysOspfExtAreaSummLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 9),
    _EtsysOspfExtAreaSummLsaCount_Type()
)
etsysOspfExtAreaSummLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaSummLsaCount.setStatus("current")
_EtsysOspfExtAreaSummLsaCksumSum_Type = Unsigned32
_EtsysOspfExtAreaSummLsaCksumSum_Object = MibTableColumn
etsysOspfExtAreaSummLsaCksumSum = _EtsysOspfExtAreaSummLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 10),
    _EtsysOspfExtAreaSummLsaCksumSum_Type()
)
etsysOspfExtAreaSummLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaSummLsaCksumSum.setStatus("current")
_EtsysOspfExtAreaSummAsLsaCount_Type = Gauge32
_EtsysOspfExtAreaSummAsLsaCount_Object = MibTableColumn
etsysOspfExtAreaSummAsLsaCount = _EtsysOspfExtAreaSummAsLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 11),
    _EtsysOspfExtAreaSummAsLsaCount_Type()
)
etsysOspfExtAreaSummAsLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaSummAsLsaCount.setStatus("current")
_EtsysOspfExtAreaSummAsLsaCksumSum_Type = Unsigned32
_EtsysOspfExtAreaSummAsLsaCksumSum_Object = MibTableColumn
etsysOspfExtAreaSummAsLsaCksumSum = _EtsysOspfExtAreaSummAsLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 12),
    _EtsysOspfExtAreaSummAsLsaCksumSum_Type()
)
etsysOspfExtAreaSummAsLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaSummAsLsaCksumSum.setStatus("current")
_EtsysOspfExtAreaNssaLsaCount_Type = Gauge32
_EtsysOspfExtAreaNssaLsaCount_Object = MibTableColumn
etsysOspfExtAreaNssaLsaCount = _EtsysOspfExtAreaNssaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 13),
    _EtsysOspfExtAreaNssaLsaCount_Type()
)
etsysOspfExtAreaNssaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaNssaLsaCount.setStatus("current")
_EtsysOspfExtAreaNssaLsaCksumSum_Type = Unsigned32
_EtsysOspfExtAreaNssaLsaCksumSum_Object = MibTableColumn
etsysOspfExtAreaNssaLsaCksumSum = _EtsysOspfExtAreaNssaLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 14),
    _EtsysOspfExtAreaNssaLsaCksumSum_Type()
)
etsysOspfExtAreaNssaLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaNssaLsaCksumSum.setStatus("current")
_EtsysOspfExtAreaOpLsaCount_Type = Gauge32
_EtsysOspfExtAreaOpLsaCount_Object = MibTableColumn
etsysOspfExtAreaOpLsaCount = _EtsysOspfExtAreaOpLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 15),
    _EtsysOspfExtAreaOpLsaCount_Type()
)
etsysOspfExtAreaOpLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaOpLsaCount.setStatus("current")
_EtsysOspfExtAreaOpLsaCksumSum_Type = Unsigned32
_EtsysOspfExtAreaOpLsaCksumSum_Object = MibTableColumn
etsysOspfExtAreaOpLsaCksumSum = _EtsysOspfExtAreaOpLsaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 1, 1, 16),
    _EtsysOspfExtAreaOpLsaCksumSum_Type()
)
etsysOspfExtAreaOpLsaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtAreaOpLsaCksumSum.setStatus("current")
_EtsysOspfExtIfTable_Object = MibTable
etsysOspfExtIfTable = _EtsysOspfExtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2)
)
if mibBuilder.loadTexts:
    etsysOspfExtIfTable.setStatus("current")
_EtsysOspfExtIfEntry_Object = MibTableRow
etsysOspfExtIfEntry = _EtsysOspfExtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysOspfExtIfEntry.setStatus("current")
_EtsysOspfExtIfOperStatus_Type = EtsysOspfOperStatus
_EtsysOspfExtIfOperStatus_Object = MibTableColumn
etsysOspfExtIfOperStatus = _EtsysOspfExtIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 1),
    _EtsysOspfExtIfOperStatus_Type()
)
etsysOspfExtIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtIfOperStatus.setStatus("current")
_EtsysOspfExtIfNetMask_Type = IpAddress
_EtsysOspfExtIfNetMask_Object = MibTableColumn
etsysOspfExtIfNetMask = _EtsysOspfExtIfNetMask_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 2),
    _EtsysOspfExtIfNetMask_Type()
)
etsysOspfExtIfNetMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfNetMask.setStatus("current")


class _EtsysOspfExtIfTransmitTimerDelay_Type(Unsigned32):
    """Custom type etsysOspfExtIfTransmitTimerDelay based on Unsigned32"""
    defaultValue = 100


_EtsysOspfExtIfTransmitTimerDelay_Object = MibTableColumn
etsysOspfExtIfTransmitTimerDelay = _EtsysOspfExtIfTransmitTimerDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 3),
    _EtsysOspfExtIfTransmitTimerDelay_Type()
)
etsysOspfExtIfTransmitTimerDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfTransmitTimerDelay.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtIfTransmitTimerDelay.setUnits("milliseconds")


class _EtsysOspfExtIfIPMaxPacketSize_Type(Unsigned32):
    """Custom type etsysOspfExtIfIPMaxPacketSize based on Unsigned32"""
    defaultValue = 576


_EtsysOspfExtIfIPMaxPacketSize_Object = MibTableColumn
etsysOspfExtIfIPMaxPacketSize = _EtsysOspfExtIfIPMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 4),
    _EtsysOspfExtIfIPMaxPacketSize_Type()
)
etsysOspfExtIfIPMaxPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfIPMaxPacketSize.setStatus("current")


class _EtsysOspfExtIfPassive_Type(TruthValue):
    """Custom type etsysOspfExtIfPassive based on TruthValue"""


_EtsysOspfExtIfPassive_Object = MibTableColumn
etsysOspfExtIfPassive = _EtsysOspfExtIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 5),
    _EtsysOspfExtIfPassive_Type()
)
etsysOspfExtIfPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfPassive.setStatus("current")


class _EtsysOspfExtIfLsaRefreshIntvl_Type(Unsigned32):
    """Custom type etsysOspfExtIfLsaRefreshIntvl based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_EtsysOspfExtIfLsaRefreshIntvl_Type.__name__ = "Unsigned32"
_EtsysOspfExtIfLsaRefreshIntvl_Object = MibTableColumn
etsysOspfExtIfLsaRefreshIntvl = _EtsysOspfExtIfLsaRefreshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 6),
    _EtsysOspfExtIfLsaRefreshIntvl_Type()
)
etsysOspfExtIfLsaRefreshIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfLsaRefreshIntvl.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtIfLsaRefreshIntvl.setUnits("seconds")


class _EtsysOspfExtIfHelperModePolicy_Type(Bits):
    """Custom type etsysOspfExtIfHelperModePolicy based on Bits"""
    defaultBinValue = "1111"

    namedValues = NamedValues(
        *(("reasonSoftwareReload", 2),
          ("reasonSoftwareRestart", 1),
          ("reasonSwitchToBackup", 3),
          ("reasonUnknown", 0))
    )

_EtsysOspfExtIfHelperModePolicy_Type.__name__ = "Bits"
_EtsysOspfExtIfHelperModePolicy_Object = MibTableColumn
etsysOspfExtIfHelperModePolicy = _EtsysOspfExtIfHelperModePolicy_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 7),
    _EtsysOspfExtIfHelperModePolicy_Type()
)
etsysOspfExtIfHelperModePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfHelperModePolicy.setStatus("current")


class _EtsysOspfExtIfMaxHitlessGracePeriod_Type(Unsigned32):
    """Custom type etsysOspfExtIfMaxHitlessGracePeriod based on Unsigned32"""
    defaultValue = 120


_EtsysOspfExtIfMaxHitlessGracePeriod_Object = MibTableColumn
etsysOspfExtIfMaxHitlessGracePeriod = _EtsysOspfExtIfMaxHitlessGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 8),
    _EtsysOspfExtIfMaxHitlessGracePeriod_Type()
)
etsysOspfExtIfMaxHitlessGracePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfMaxHitlessGracePeriod.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtIfMaxHitlessGracePeriod.setUnits("seconds")


class _EtsysOspfExtIfAuthUserData_Type(OctetString):
    """Custom type etsysOspfExtIfAuthUserData based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_EtsysOspfExtIfAuthUserData_Type.__name__ = "OctetString"
_EtsysOspfExtIfAuthUserData_Object = MibTableColumn
etsysOspfExtIfAuthUserData = _EtsysOspfExtIfAuthUserData_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 9),
    _EtsysOspfExtIfAuthUserData_Type()
)
etsysOspfExtIfAuthUserData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfAuthUserData.setStatus("current")


class _EtsysOspfExtIfFastHelloMultiplier_Type(Unsigned32):
    """Custom type etsysOspfExtIfFastHelloMultiplier based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_EtsysOspfExtIfFastHelloMultiplier_Type.__name__ = "Unsigned32"
_EtsysOspfExtIfFastHelloMultiplier_Object = MibTableColumn
etsysOspfExtIfFastHelloMultiplier = _EtsysOspfExtIfFastHelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 10),
    _EtsysOspfExtIfFastHelloMultiplier_Type()
)
etsysOspfExtIfFastHelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfFastHelloMultiplier.setStatus("current")


class _EtsysOspfExtIfAutoDeleteNbr_Type(TruthValue):
    """Custom type etsysOspfExtIfAutoDeleteNbr based on TruthValue"""


_EtsysOspfExtIfAutoDeleteNbr_Object = MibTableColumn
etsysOspfExtIfAutoDeleteNbr = _EtsysOspfExtIfAutoDeleteNbr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 11),
    _EtsysOspfExtIfAutoDeleteNbr_Type()
)
etsysOspfExtIfAutoDeleteNbr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfAutoDeleteNbr.setStatus("current")


class _EtsysOspfExtIfMtuIgnore_Type(TruthValue):
    """Custom type etsysOspfExtIfMtuIgnore based on TruthValue"""


_EtsysOspfExtIfMtuIgnore_Object = MibTableColumn
etsysOspfExtIfMtuIgnore = _EtsysOspfExtIfMtuIgnore_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 2, 1, 12),
    _EtsysOspfExtIfMtuIgnore_Type()
)
etsysOspfExtIfMtuIgnore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtIfMtuIgnore.setStatus("current")
_EtsysOspfExtVirtIfTable_Object = MibTable
etsysOspfExtVirtIfTable = _EtsysOspfExtVirtIfTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3)
)
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfTable.setStatus("current")
_EtsysOspfExtVirtIfEntry_Object = MibTableRow
etsysOspfExtVirtIfEntry = _EtsysOspfExtVirtIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1)
)
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfEntry.setStatus("current")


class _EtsysOspfExtVirtIfAdminStatus_Type(Status):
    """Custom type etsysOspfExtVirtIfAdminStatus based on Status"""


_EtsysOspfExtVirtIfAdminStatus_Object = MibTableColumn
etsysOspfExtVirtIfAdminStatus = _EtsysOspfExtVirtIfAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1, 1),
    _EtsysOspfExtVirtIfAdminStatus_Type()
)
etsysOspfExtVirtIfAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfAdminStatus.setStatus("current")
_EtsysOspfExtVirtIfOperStatus_Type = EtsysOspfOperStatus
_EtsysOspfExtVirtIfOperStatus_Object = MibTableColumn
etsysOspfExtVirtIfOperStatus = _EtsysOspfExtVirtIfOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1, 2),
    _EtsysOspfExtVirtIfOperStatus_Type()
)
etsysOspfExtVirtIfOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfOperStatus.setStatus("current")


class _EtsysOspfExtVirtIfTransmitTimerDelay_Type(Unsigned32):
    """Custom type etsysOspfExtVirtIfTransmitTimerDelay based on Unsigned32"""
    defaultValue = 100


_EtsysOspfExtVirtIfTransmitTimerDelay_Object = MibTableColumn
etsysOspfExtVirtIfTransmitTimerDelay = _EtsysOspfExtVirtIfTransmitTimerDelay_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1, 3),
    _EtsysOspfExtVirtIfTransmitTimerDelay_Type()
)
etsysOspfExtVirtIfTransmitTimerDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfTransmitTimerDelay.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfTransmitTimerDelay.setUnits("milliseconds")


class _EtsysOspfExtVirtIfIPMaxPacketSize_Type(Unsigned32):
    """Custom type etsysOspfExtVirtIfIPMaxPacketSize based on Unsigned32"""
    defaultValue = 576


_EtsysOspfExtVirtIfIPMaxPacketSize_Object = MibTableColumn
etsysOspfExtVirtIfIPMaxPacketSize = _EtsysOspfExtVirtIfIPMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1, 4),
    _EtsysOspfExtVirtIfIPMaxPacketSize_Type()
)
etsysOspfExtVirtIfIPMaxPacketSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfIPMaxPacketSize.setStatus("current")


class _EtsysOspfExtVirtIfPassive_Type(TruthValue):
    """Custom type etsysOspfExtVirtIfPassive based on TruthValue"""


_EtsysOspfExtVirtIfPassive_Object = MibTableColumn
etsysOspfExtVirtIfPassive = _EtsysOspfExtVirtIfPassive_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1, 5),
    _EtsysOspfExtVirtIfPassive_Type()
)
etsysOspfExtVirtIfPassive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfPassive.setStatus("current")


class _EtsysOspfExtVirtIfLsaRefreshIntvl_Type(Unsigned32):
    """Custom type etsysOspfExtVirtIfLsaRefreshIntvl based on Unsigned32"""
    defaultValue = 1800

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3599),
    )


_EtsysOspfExtVirtIfLsaRefreshIntvl_Type.__name__ = "Unsigned32"
_EtsysOspfExtVirtIfLsaRefreshIntvl_Object = MibTableColumn
etsysOspfExtVirtIfLsaRefreshIntvl = _EtsysOspfExtVirtIfLsaRefreshIntvl_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1, 6),
    _EtsysOspfExtVirtIfLsaRefreshIntvl_Type()
)
etsysOspfExtVirtIfLsaRefreshIntvl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfLsaRefreshIntvl.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfLsaRefreshIntvl.setUnits("seconds")


class _EtsysOspfExtVirtIfHelperModePolicy_Type(Bits):
    """Custom type etsysOspfExtVirtIfHelperModePolicy based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("reasonSoftwareReload", 2),
          ("reasonSoftwareRestart", 1),
          ("reasonSwitchToBackup", 3),
          ("reasonUnknown", 0))
    )

_EtsysOspfExtVirtIfHelperModePolicy_Type.__name__ = "Bits"
_EtsysOspfExtVirtIfHelperModePolicy_Object = MibTableColumn
etsysOspfExtVirtIfHelperModePolicy = _EtsysOspfExtVirtIfHelperModePolicy_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1, 7),
    _EtsysOspfExtVirtIfHelperModePolicy_Type()
)
etsysOspfExtVirtIfHelperModePolicy.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfHelperModePolicy.setStatus("current")


class _EtsysOspfExtVirtIfMaxHtlssGracePeriod_Type(Unsigned32):
    """Custom type etsysOspfExtVirtIfMaxHtlssGracePeriod based on Unsigned32"""
    defaultValue = 120


_EtsysOspfExtVirtIfMaxHtlssGracePeriod_Object = MibTableColumn
etsysOspfExtVirtIfMaxHtlssGracePeriod = _EtsysOspfExtVirtIfMaxHtlssGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1, 8),
    _EtsysOspfExtVirtIfMaxHtlssGracePeriod_Type()
)
etsysOspfExtVirtIfMaxHtlssGracePeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfMaxHtlssGracePeriod.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfMaxHtlssGracePeriod.setUnits("seconds")


class _EtsysOspfExtVirtIfFastHelloMultiplier_Type(Unsigned32):
    """Custom type etsysOspfExtVirtIfFastHelloMultiplier based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 20),
    )


_EtsysOspfExtVirtIfFastHelloMultiplier_Type.__name__ = "Unsigned32"
_EtsysOspfExtVirtIfFastHelloMultiplier_Object = MibTableColumn
etsysOspfExtVirtIfFastHelloMultiplier = _EtsysOspfExtVirtIfFastHelloMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1, 9),
    _EtsysOspfExtVirtIfFastHelloMultiplier_Type()
)
etsysOspfExtVirtIfFastHelloMultiplier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfFastHelloMultiplier.setStatus("current")


class _EtsysOspfExtVirtIfMtuIgnore_Type(TruthValue):
    """Custom type etsysOspfExtVirtIfMtuIgnore based on TruthValue"""


_EtsysOspfExtVirtIfMtuIgnore_Object = MibTableColumn
etsysOspfExtVirtIfMtuIgnore = _EtsysOspfExtVirtIfMtuIgnore_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 3, 1, 10),
    _EtsysOspfExtVirtIfMtuIgnore_Type()
)
etsysOspfExtVirtIfMtuIgnore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfMtuIgnore.setStatus("current")
_EtsysOspfExtNbrTable_Object = MibTable
etsysOspfExtNbrTable = _EtsysOspfExtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 4)
)
if mibBuilder.loadTexts:
    etsysOspfExtNbrTable.setStatus("current")
_EtsysOspfExtNbrEntry_Object = MibTableRow
etsysOspfExtNbrEntry = _EtsysOspfExtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 4, 1)
)
if mibBuilder.loadTexts:
    etsysOspfExtNbrEntry.setStatus("current")


class _EtsysOspfExtNbrAdminStatus_Type(Status):
    """Custom type etsysOspfExtNbrAdminStatus based on Status"""


_EtsysOspfExtNbrAdminStatus_Object = MibTableColumn
etsysOspfExtNbrAdminStatus = _EtsysOspfExtNbrAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 4, 1, 1),
    _EtsysOspfExtNbrAdminStatus_Type()
)
etsysOspfExtNbrAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtNbrAdminStatus.setStatus("current")
_EtsysOspfExtNbrOperStatus_Type = EtsysOspfOperStatus
_EtsysOspfExtNbrOperStatus_Object = MibTableColumn
etsysOspfExtNbrOperStatus = _EtsysOspfExtNbrOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 4, 1, 2),
    _EtsysOspfExtNbrOperStatus_Type()
)
etsysOspfExtNbrOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtNbrOperStatus.setStatus("current")
_EtsysOspfExtNbrNumRequests_Type = Gauge32
_EtsysOspfExtNbrNumRequests_Object = MibTableColumn
etsysOspfExtNbrNumRequests = _EtsysOspfExtNbrNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 4, 1, 3),
    _EtsysOspfExtNbrNumRequests_Type()
)
etsysOspfExtNbrNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtNbrNumRequests.setStatus("current")


class _EtsysOspfExtNbrIfIpAddr_Type(IpAddress):
    """Custom type etsysOspfExtNbrIfIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_EtsysOspfExtNbrIfIpAddr_Object = MibTableColumn
etsysOspfExtNbrIfIpAddr = _EtsysOspfExtNbrIfIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 4, 1, 4),
    _EtsysOspfExtNbrIfIpAddr_Type()
)
etsysOspfExtNbrIfIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysOspfExtNbrIfIpAddr.setStatus("current")


class _EtsysOspfExtNbrDeadTime_Type(Unsigned32):
    """Custom type etsysOspfExtNbrDeadTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysOspfExtNbrDeadTime_Type.__name__ = "Unsigned32"
_EtsysOspfExtNbrDeadTime_Object = MibTableColumn
etsysOspfExtNbrDeadTime = _EtsysOspfExtNbrDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 4, 1, 5),
    _EtsysOspfExtNbrDeadTime_Type()
)
etsysOspfExtNbrDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtNbrDeadTime.setStatus("current")
if mibBuilder.loadTexts:
    etsysOspfExtNbrDeadTime.setUnits("seconds")
_EtsysOspfExtNbrAreaId_Type = AreaID
_EtsysOspfExtNbrAreaId_Object = MibTableColumn
etsysOspfExtNbrAreaId = _EtsysOspfExtNbrAreaId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 4, 1, 6),
    _EtsysOspfExtNbrAreaId_Type()
)
etsysOspfExtNbrAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtNbrAreaId.setStatus("current")
_EtsysOspfExtVirtNbrTable_Object = MibTable
etsysOspfExtVirtNbrTable = _EtsysOspfExtVirtNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 5)
)
if mibBuilder.loadTexts:
    etsysOspfExtVirtNbrTable.setStatus("current")
_EtsysOspfExtVirtNbrEntry_Object = MibTableRow
etsysOspfExtVirtNbrEntry = _EtsysOspfExtVirtNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 5, 1)
)
if mibBuilder.loadTexts:
    etsysOspfExtVirtNbrEntry.setStatus("current")
_EtsysOspfExtVirtNbrNumRequests_Type = Gauge32
_EtsysOspfExtVirtNbrNumRequests_Object = MibTableColumn
etsysOspfExtVirtNbrNumRequests = _EtsysOspfExtVirtNbrNumRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 5, 1, 1),
    _EtsysOspfExtVirtNbrNumRequests_Type()
)
etsysOspfExtVirtNbrNumRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtVirtNbrNumRequests.setStatus("current")


class _EtsysOspfExtVirtNbrDeadTime_Type(Unsigned32):
    """Custom type etsysOspfExtVirtNbrDeadTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_EtsysOspfExtVirtNbrDeadTime_Type.__name__ = "Unsigned32"
_EtsysOspfExtVirtNbrDeadTime_Object = MibTableColumn
etsysOspfExtVirtNbrDeadTime = _EtsysOspfExtVirtNbrDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 5, 1, 2),
    _EtsysOspfExtVirtNbrDeadTime_Type()
)
etsysOspfExtVirtNbrDeadTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtVirtNbrDeadTime.setStatus("current")
_EtsysOspfExtLocalLsdbTable_Object = MibTable
etsysOspfExtLocalLsdbTable = _EtsysOspfExtLocalLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 6)
)
if mibBuilder.loadTexts:
    etsysOspfExtLocalLsdbTable.setStatus("current")
_EtsysOspfExtLocalLsdbEntry_Object = MibTableRow
etsysOspfExtLocalLsdbEntry = _EtsysOspfExtLocalLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 6, 1)
)
if mibBuilder.loadTexts:
    etsysOspfExtLocalLsdbEntry.setStatus("current")
_EtsysOspfExtLocalLsdbAreaId_Type = AreaID
_EtsysOspfExtLocalLsdbAreaId_Object = MibTableColumn
etsysOspfExtLocalLsdbAreaId = _EtsysOspfExtLocalLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 1, 2, 6, 1, 1),
    _EtsysOspfExtLocalLsdbAreaId_Type()
)
etsysOspfExtLocalLsdbAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysOspfExtLocalLsdbAreaId.setStatus("current")
_EtsysOspfExtConformance_ObjectIdentity = ObjectIdentity
etsysOspfExtConformance = _EtsysOspfExtConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2)
)
_EtsysOspfExtGroups_ObjectIdentity = ObjectIdentity
etsysOspfExtGroups = _EtsysOspfExtGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2, 1)
)
_EtsysOspfExtCompliances_ObjectIdentity = ObjectIdentity
etsysOspfExtCompliances = _EtsysOspfExtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2, 2)
)
ospfAreaEntry.registerAugmentions(
    ("ENTERASYS-OSPF-EXT-MIB",
     "etsysOspfExtAreaEntry")
)
etsysOspfExtAreaEntry.setIndexNames(*ospfAreaEntry.getIndexNames())
ospfIfEntry.registerAugmentions(
    ("ENTERASYS-OSPF-EXT-MIB",
     "etsysOspfExtIfEntry")
)
etsysOspfExtIfEntry.setIndexNames(*ospfIfEntry.getIndexNames())
ospfVirtIfEntry.registerAugmentions(
    ("ENTERASYS-OSPF-EXT-MIB",
     "etsysOspfExtVirtIfEntry")
)
etsysOspfExtVirtIfEntry.setIndexNames(*ospfVirtIfEntry.getIndexNames())
ospfNbrEntry.registerAugmentions(
    ("ENTERASYS-OSPF-EXT-MIB",
     "etsysOspfExtNbrEntry")
)
etsysOspfExtNbrEntry.setIndexNames(*ospfNbrEntry.getIndexNames())
ospfVirtNbrEntry.registerAugmentions(
    ("ENTERASYS-OSPF-EXT-MIB",
     "etsysOspfExtVirtNbrEntry")
)
etsysOspfExtVirtNbrEntry.setIndexNames(*ospfVirtNbrEntry.getIndexNames())
ospfLocalLsdbEntry.registerAugmentions(
    ("ENTERASYS-OSPF-EXT-MIB",
     "etsysOspfExtLocalLsdbEntry")
)
etsysOspfExtLocalLsdbEntry.setIndexNames(*ospfLocalLsdbEntry.getIndexNames())

# Managed Objects groups

etsysOspfExtGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2, 1, 1)
)
etsysOspfExtGlobalGroup.setObjects(
      *(("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtOperStatus"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtCalcMaxDelay"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtCalcThrshUpdStart"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtCalcThrshUpdRestart"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtCalcThrshIncUpdates"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtCalcThrshIncSpfUpd"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtCalcPauseFreq"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtRteMaxEqCostPaths"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtCheckAge"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtExtLsaRfshIntvl"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtExternOpLsaCount"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtExternOpLsaCksumSum"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtNumUpdPending"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtNumUpdMerged"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtNumCksumsPending"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtDoGraceHitless"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtDoGraceUnplannedHitless"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtHitlessGracePeriod"))
)
if mibBuilder.loadTexts:
    etsysOspfExtGlobalGroup.setStatus("current")

etsysOspfExtAreaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2, 1, 2)
)
etsysOspfExtAreaGroup.setObjects(
      *(("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaAdminStatus"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaOperStatus"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaTransitCapability"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaLsaRfshIntvl"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaRtrLsaCount"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaRtrLsaCksumSum"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaNetLsaCount"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaNetLsaCksumSum"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaSummLsaCount"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaSummLsaCksumSum"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaSummAsLsaCount"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaSummAsLsaCksumSum"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaNssaLsaCount"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaNssaLsaCksumSum"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaOpLsaCount"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtAreaOpLsaCksumSum"))
)
if mibBuilder.loadTexts:
    etsysOspfExtAreaGroup.setStatus("current")

etsysOspfExtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2, 1, 3)
)
etsysOspfExtIfGroup.setObjects(
      *(("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfOperStatus"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfNetMask"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfTransmitTimerDelay"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfIPMaxPacketSize"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfPassive"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfLsaRefreshIntvl"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfHelperModePolicy"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfMaxHitlessGracePeriod"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfAuthUserData"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfFastHelloMultiplier"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfAutoDeleteNbr"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtIfMtuIgnore"))
)
if mibBuilder.loadTexts:
    etsysOspfExtIfGroup.setStatus("current")

etsysOspfExtVirtIfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2, 1, 4)
)
etsysOspfExtVirtIfGroup.setObjects(
      *(("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtIfAdminStatus"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtIfOperStatus"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtIfTransmitTimerDelay"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtIfIPMaxPacketSize"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtIfPassive"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtIfLsaRefreshIntvl"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtIfHelperModePolicy"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtIfMaxHtlssGracePeriod"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtIfFastHelloMultiplier"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtIfMtuIgnore"))
)
if mibBuilder.loadTexts:
    etsysOspfExtVirtIfGroup.setStatus("current")

etsysOspfExtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2, 1, 5)
)
etsysOspfExtNbrGroup.setObjects(
      *(("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtNbrAdminStatus"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtNbrOperStatus"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtNbrNumRequests"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtNbrIfIpAddr"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtNbrDeadTime"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtNbrAreaId"))
)
if mibBuilder.loadTexts:
    etsysOspfExtNbrGroup.setStatus("current")

etsysOspfExtVirtNbrGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2, 1, 6)
)
etsysOspfExtVirtNbrGroup.setObjects(
      *(("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtNbrNumRequests"),
        ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtVirtNbrDeadTime"))
)
if mibBuilder.loadTexts:
    etsysOspfExtVirtNbrGroup.setStatus("current")

etsysOspfExtLocalLsdbGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2, 1, 7)
)
etsysOspfExtLocalLsdbGroup.setObjects(
    ("ENTERASYS-OSPF-EXT-MIB", "etsysOspfExtLocalLsdbAreaId")
)
if mibBuilder.loadTexts:
    etsysOspfExtLocalLsdbGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysOspfExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 65, 2, 2, 1)
)
if mibBuilder.loadTexts:
    etsysOspfExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-OSPF-EXT-MIB",
    **{"EtsysOspfOperStatus": EtsysOspfOperStatus,
       "etsysOspfExtMIB": etsysOspfExtMIB,
       "etsysOspfExtObjects": etsysOspfExtObjects,
       "etsysOspfExtGlobals": etsysOspfExtGlobals,
       "etsysOspfExtOperStatus": etsysOspfExtOperStatus,
       "etsysOspfExtCalcMaxDelay": etsysOspfExtCalcMaxDelay,
       "etsysOspfExtCalcThrshUpdStart": etsysOspfExtCalcThrshUpdStart,
       "etsysOspfExtCalcThrshUpdRestart": etsysOspfExtCalcThrshUpdRestart,
       "etsysOspfExtCalcThrshIncUpdates": etsysOspfExtCalcThrshIncUpdates,
       "etsysOspfExtCalcThrshIncSpfUpd": etsysOspfExtCalcThrshIncSpfUpd,
       "etsysOspfExtCalcPauseFreq": etsysOspfExtCalcPauseFreq,
       "etsysOspfExtRteMaxEqCostPaths": etsysOspfExtRteMaxEqCostPaths,
       "etsysOspfExtCheckAge": etsysOspfExtCheckAge,
       "etsysOspfExtExtLsaRfshIntvl": etsysOspfExtExtLsaRfshIntvl,
       "etsysOspfExtExternOpLsaCount": etsysOspfExtExternOpLsaCount,
       "etsysOspfExtExternOpLsaCksumSum": etsysOspfExtExternOpLsaCksumSum,
       "etsysOspfExtNumUpdPending": etsysOspfExtNumUpdPending,
       "etsysOspfExtNumUpdMerged": etsysOspfExtNumUpdMerged,
       "etsysOspfExtNumCksumsPending": etsysOspfExtNumCksumsPending,
       "etsysOspfExtDoGraceHitless": etsysOspfExtDoGraceHitless,
       "etsysOspfExtDoGraceUnplannedHitless": etsysOspfExtDoGraceUnplannedHitless,
       "etsysOspfExtHitlessGracePeriod": etsysOspfExtHitlessGracePeriod,
       "etsysOspfExtTables": etsysOspfExtTables,
       "etsysOspfExtAreaTable": etsysOspfExtAreaTable,
       "etsysOspfExtAreaEntry": etsysOspfExtAreaEntry,
       "etsysOspfExtAreaAdminStatus": etsysOspfExtAreaAdminStatus,
       "etsysOspfExtAreaOperStatus": etsysOspfExtAreaOperStatus,
       "etsysOspfExtAreaTransitCapability": etsysOspfExtAreaTransitCapability,
       "etsysOspfExtAreaLsaRfshIntvl": etsysOspfExtAreaLsaRfshIntvl,
       "etsysOspfExtAreaRtrLsaCount": etsysOspfExtAreaRtrLsaCount,
       "etsysOspfExtAreaRtrLsaCksumSum": etsysOspfExtAreaRtrLsaCksumSum,
       "etsysOspfExtAreaNetLsaCount": etsysOspfExtAreaNetLsaCount,
       "etsysOspfExtAreaNetLsaCksumSum": etsysOspfExtAreaNetLsaCksumSum,
       "etsysOspfExtAreaSummLsaCount": etsysOspfExtAreaSummLsaCount,
       "etsysOspfExtAreaSummLsaCksumSum": etsysOspfExtAreaSummLsaCksumSum,
       "etsysOspfExtAreaSummAsLsaCount": etsysOspfExtAreaSummAsLsaCount,
       "etsysOspfExtAreaSummAsLsaCksumSum": etsysOspfExtAreaSummAsLsaCksumSum,
       "etsysOspfExtAreaNssaLsaCount": etsysOspfExtAreaNssaLsaCount,
       "etsysOspfExtAreaNssaLsaCksumSum": etsysOspfExtAreaNssaLsaCksumSum,
       "etsysOspfExtAreaOpLsaCount": etsysOspfExtAreaOpLsaCount,
       "etsysOspfExtAreaOpLsaCksumSum": etsysOspfExtAreaOpLsaCksumSum,
       "etsysOspfExtIfTable": etsysOspfExtIfTable,
       "etsysOspfExtIfEntry": etsysOspfExtIfEntry,
       "etsysOspfExtIfOperStatus": etsysOspfExtIfOperStatus,
       "etsysOspfExtIfNetMask": etsysOspfExtIfNetMask,
       "etsysOspfExtIfTransmitTimerDelay": etsysOspfExtIfTransmitTimerDelay,
       "etsysOspfExtIfIPMaxPacketSize": etsysOspfExtIfIPMaxPacketSize,
       "etsysOspfExtIfPassive": etsysOspfExtIfPassive,
       "etsysOspfExtIfLsaRefreshIntvl": etsysOspfExtIfLsaRefreshIntvl,
       "etsysOspfExtIfHelperModePolicy": etsysOspfExtIfHelperModePolicy,
       "etsysOspfExtIfMaxHitlessGracePeriod": etsysOspfExtIfMaxHitlessGracePeriod,
       "etsysOspfExtIfAuthUserData": etsysOspfExtIfAuthUserData,
       "etsysOspfExtIfFastHelloMultiplier": etsysOspfExtIfFastHelloMultiplier,
       "etsysOspfExtIfAutoDeleteNbr": etsysOspfExtIfAutoDeleteNbr,
       "etsysOspfExtIfMtuIgnore": etsysOspfExtIfMtuIgnore,
       "etsysOspfExtVirtIfTable": etsysOspfExtVirtIfTable,
       "etsysOspfExtVirtIfEntry": etsysOspfExtVirtIfEntry,
       "etsysOspfExtVirtIfAdminStatus": etsysOspfExtVirtIfAdminStatus,
       "etsysOspfExtVirtIfOperStatus": etsysOspfExtVirtIfOperStatus,
       "etsysOspfExtVirtIfTransmitTimerDelay": etsysOspfExtVirtIfTransmitTimerDelay,
       "etsysOspfExtVirtIfIPMaxPacketSize": etsysOspfExtVirtIfIPMaxPacketSize,
       "etsysOspfExtVirtIfPassive": etsysOspfExtVirtIfPassive,
       "etsysOspfExtVirtIfLsaRefreshIntvl": etsysOspfExtVirtIfLsaRefreshIntvl,
       "etsysOspfExtVirtIfHelperModePolicy": etsysOspfExtVirtIfHelperModePolicy,
       "etsysOspfExtVirtIfMaxHtlssGracePeriod": etsysOspfExtVirtIfMaxHtlssGracePeriod,
       "etsysOspfExtVirtIfFastHelloMultiplier": etsysOspfExtVirtIfFastHelloMultiplier,
       "etsysOspfExtVirtIfMtuIgnore": etsysOspfExtVirtIfMtuIgnore,
       "etsysOspfExtNbrTable": etsysOspfExtNbrTable,
       "etsysOspfExtNbrEntry": etsysOspfExtNbrEntry,
       "etsysOspfExtNbrAdminStatus": etsysOspfExtNbrAdminStatus,
       "etsysOspfExtNbrOperStatus": etsysOspfExtNbrOperStatus,
       "etsysOspfExtNbrNumRequests": etsysOspfExtNbrNumRequests,
       "etsysOspfExtNbrIfIpAddr": etsysOspfExtNbrIfIpAddr,
       "etsysOspfExtNbrDeadTime": etsysOspfExtNbrDeadTime,
       "etsysOspfExtNbrAreaId": etsysOspfExtNbrAreaId,
       "etsysOspfExtVirtNbrTable": etsysOspfExtVirtNbrTable,
       "etsysOspfExtVirtNbrEntry": etsysOspfExtVirtNbrEntry,
       "etsysOspfExtVirtNbrNumRequests": etsysOspfExtVirtNbrNumRequests,
       "etsysOspfExtVirtNbrDeadTime": etsysOspfExtVirtNbrDeadTime,
       "etsysOspfExtLocalLsdbTable": etsysOspfExtLocalLsdbTable,
       "etsysOspfExtLocalLsdbEntry": etsysOspfExtLocalLsdbEntry,
       "etsysOspfExtLocalLsdbAreaId": etsysOspfExtLocalLsdbAreaId,
       "etsysOspfExtConformance": etsysOspfExtConformance,
       "etsysOspfExtGroups": etsysOspfExtGroups,
       "etsysOspfExtGlobalGroup": etsysOspfExtGlobalGroup,
       "etsysOspfExtAreaGroup": etsysOspfExtAreaGroup,
       "etsysOspfExtIfGroup": etsysOspfExtIfGroup,
       "etsysOspfExtVirtIfGroup": etsysOspfExtVirtIfGroup,
       "etsysOspfExtNbrGroup": etsysOspfExtNbrGroup,
       "etsysOspfExtVirtNbrGroup": etsysOspfExtVirtNbrGroup,
       "etsysOspfExtLocalLsdbGroup": etsysOspfExtLocalLsdbGroup,
       "etsysOspfExtCompliances": etsysOspfExtCompliances,
       "etsysOspfExtCompliance": etsysOspfExtCompliance}
)
