# SNMP MIB module (HPN-ICF-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HPN-ICF-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:00:40 2024
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

(hpnicfCommon,) = mibBuilder.importSymbols(
    "HPN-ICF-OID-MIB",
    "hpnicfCommon")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpnicfIpx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_HpnicfIpxConfig_ObjectIdentity = ObjectIdentity
hpnicfIpxConfig = _HpnicfIpxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1)
)


class _HpnicfIpxStatus_Type(EnabledStatus):
    """Custom type hpnicfIpxStatus based on EnabledStatus"""


_HpnicfIpxStatus_Object = MibScalar
hpnicfIpxStatus = _HpnicfIpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 1),
    _HpnicfIpxStatus_Type()
)
hpnicfIpxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpxStatus.setStatus("current")
_HpnicfIpxIfConfigTable_Object = MibTable
hpnicfIpxIfConfigTable = _HpnicfIpxIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2)
)
if mibBuilder.loadTexts:
    hpnicfIpxIfConfigTable.setStatus("current")
_HpnicfIpxIfConfigEntry_Object = MibTableRow
hpnicfIpxIfConfigEntry = _HpnicfIpxIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1)
)
hpnicfIpxIfConfigEntry.setIndexNames(
    (0, "HPN-ICF-IPX-MIB", "hpnicfIpxIfIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIpxIfConfigEntry.setStatus("current")


class _HpnicfIpxIfIndex_Type(Integer32):
    """Custom type hpnicfIpxIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIpxIfIndex_Type.__name__ = "Integer32"
_HpnicfIpxIfIndex_Object = MibTableColumn
hpnicfIpxIfIndex = _HpnicfIpxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 1),
    _HpnicfIpxIfIndex_Type()
)
hpnicfIpxIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpxIfIndex.setStatus("current")


class _HpnicfIpxIfNetId_Type(OctetString):
    """Custom type hpnicfIpxIfNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HpnicfIpxIfNetId_Type.__name__ = "OctetString"
_HpnicfIpxIfNetId_Object = MibTableColumn
hpnicfIpxIfNetId = _HpnicfIpxIfNetId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 2),
    _HpnicfIpxIfNetId_Type()
)
hpnicfIpxIfNetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxIfNetId.setStatus("current")


class _HpnicfIpxIfNodeId_Type(OctetString):
    """Custom type hpnicfIpxIfNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnicfIpxIfNodeId_Type.__name__ = "OctetString"
_HpnicfIpxIfNodeId_Object = MibTableColumn
hpnicfIpxIfNodeId = _HpnicfIpxIfNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 3),
    _HpnicfIpxIfNodeId_Type()
)
hpnicfIpxIfNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfNodeId.setStatus("current")


class _HpnicfIpxIfSplitHorizon_Type(EnabledStatus):
    """Custom type hpnicfIpxIfSplitHorizon based on EnabledStatus"""


_HpnicfIpxIfSplitHorizon_Object = MibTableColumn
hpnicfIpxIfSplitHorizon = _HpnicfIpxIfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 4),
    _HpnicfIpxIfSplitHorizon_Type()
)
hpnicfIpxIfSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxIfSplitHorizon.setStatus("current")


class _HpnicfIPxIfTick_Type(Integer32):
    """Custom type hpnicfIPxIfTick based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30000),
    )


_HpnicfIPxIfTick_Type.__name__ = "Integer32"
_HpnicfIPxIfTick_Object = MibTableColumn
hpnicfIPxIfTick = _HpnicfIPxIfTick_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 5),
    _HpnicfIPxIfTick_Type()
)
hpnicfIPxIfTick.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIPxIfTick.setStatus("current")


class _HpnicfIpxIfUpdateChangeOnly_Type(EnabledStatus):
    """Custom type hpnicfIpxIfUpdateChangeOnly based on EnabledStatus"""


_HpnicfIpxIfUpdateChangeOnly_Object = MibTableColumn
hpnicfIpxIfUpdateChangeOnly = _HpnicfIpxIfUpdateChangeOnly_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 6),
    _HpnicfIpxIfUpdateChangeOnly_Type()
)
hpnicfIpxIfUpdateChangeOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxIfUpdateChangeOnly.setStatus("current")


class _HpnicfIpxIfRipMtu_Type(Integer32):
    """Custom type hpnicfIpxIfRipMtu based on Integer32"""
    defaultValue = 432

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(432, 1500),
    )


_HpnicfIpxIfRipMtu_Type.__name__ = "Integer32"
_HpnicfIpxIfRipMtu_Object = MibTableColumn
hpnicfIpxIfRipMtu = _HpnicfIpxIfRipMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 7),
    _HpnicfIpxIfRipMtu_Type()
)
hpnicfIpxIfRipMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxIfRipMtu.setStatus("current")


class _HpnicfIpxIfEncapsuleType_Type(Integer32):
    """Custom type hpnicfIpxIfEncapsuleType based on Integer32"""
    defaultValue = 2

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
        *(("dot2", 1),
          ("dot3", 2),
          ("ethernet-2", 3),
          ("snap", 4),
          ("unkown", 5))
    )


_HpnicfIpxIfEncapsuleType_Type.__name__ = "Integer32"
_HpnicfIpxIfEncapsuleType_Object = MibTableColumn
hpnicfIpxIfEncapsuleType = _HpnicfIpxIfEncapsuleType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 8),
    _HpnicfIpxIfEncapsuleType_Type()
)
hpnicfIpxIfEncapsuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxIfEncapsuleType.setStatus("current")


class _HpnicfIpxIfNetbiosPropagation_Type(EnabledStatus):
    """Custom type hpnicfIpxIfNetbiosPropagation based on EnabledStatus"""


_HpnicfIpxIfNetbiosPropagation_Object = MibTableColumn
hpnicfIpxIfNetbiosPropagation = _HpnicfIpxIfNetbiosPropagation_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 9),
    _HpnicfIpxIfNetbiosPropagation_Type()
)
hpnicfIpxIfNetbiosPropagation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxIfNetbiosPropagation.setStatus("current")


class _HpnicfIpxIfSapStatus_Type(EnabledStatus):
    """Custom type hpnicfIpxIfSapStatus based on EnabledStatus"""


_HpnicfIpxIfSapStatus_Object = MibTableColumn
hpnicfIpxIfSapStatus = _HpnicfIpxIfSapStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 10),
    _HpnicfIpxIfSapStatus_Type()
)
hpnicfIpxIfSapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxIfSapStatus.setStatus("current")


class _HpnicfIpxIfSapMtu_Type(Integer32):
    """Custom type hpnicfIpxIfSapMtu based on Integer32"""
    defaultValue = 480

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(480, 1500),
    )


_HpnicfIpxIfSapMtu_Type.__name__ = "Integer32"
_HpnicfIpxIfSapMtu_Object = MibTableColumn
hpnicfIpxIfSapMtu = _HpnicfIpxIfSapMtu_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 11),
    _HpnicfIpxIfSapMtu_Type()
)
hpnicfIpxIfSapMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxIfSapMtu.setStatus("current")


class _HpnicfIpxIfGnsReply_Type(EnabledStatus):
    """Custom type hpnicfIpxIfGnsReply based on EnabledStatus"""


_HpnicfIpxIfGnsReply_Object = MibTableColumn
hpnicfIpxIfGnsReply = _HpnicfIpxIfGnsReply_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 12),
    _HpnicfIpxIfGnsReply_Type()
)
hpnicfIpxIfGnsReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxIfGnsReply.setStatus("current")
_HpnicfIpxIfRowStatus_Type = RowStatus
_HpnicfIpxIfRowStatus_Object = MibTableColumn
hpnicfIpxIfRowStatus = _HpnicfIpxIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 1, 2, 1, 13),
    _HpnicfIpxIfRowStatus_Type()
)
hpnicfIpxIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxIfRowStatus.setStatus("current")
_HpnicfIpxRip_ObjectIdentity = ObjectIdentity
hpnicfIpxRip = _HpnicfIpxRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2)
)


class _HpnicfIpxRouteMultiplier_Type(Integer32):
    """Custom type hpnicfIpxRouteMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HpnicfIpxRouteMultiplier_Type.__name__ = "Integer32"
_HpnicfIpxRouteMultiplier_Object = MibScalar
hpnicfIpxRouteMultiplier = _HpnicfIpxRouteMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 1),
    _HpnicfIpxRouteMultiplier_Type()
)
hpnicfIpxRouteMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpxRouteMultiplier.setStatus("current")


class _HpnicfIpxRouteUpdateTimer_Type(Integer32):
    """Custom type hpnicfIpxRouteUpdateTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60000),
    )


_HpnicfIpxRouteUpdateTimer_Type.__name__ = "Integer32"
_HpnicfIpxRouteUpdateTimer_Object = MibScalar
hpnicfIpxRouteUpdateTimer = _HpnicfIpxRouteUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 2),
    _HpnicfIpxRouteUpdateTimer_Type()
)
hpnicfIpxRouteUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpxRouteUpdateTimer.setStatus("current")


class _HpnicfIpxRouteImpRouteStatic_Type(EnabledStatus):
    """Custom type hpnicfIpxRouteImpRouteStatic based on EnabledStatus"""


_HpnicfIpxRouteImpRouteStatic_Object = MibScalar
hpnicfIpxRouteImpRouteStatic = _HpnicfIpxRouteImpRouteStatic_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 3),
    _HpnicfIpxRouteImpRouteStatic_Type()
)
hpnicfIpxRouteImpRouteStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpxRouteImpRouteStatic.setStatus("current")


class _HpnicfIpxRouteLoadBalancePaths_Type(Integer32):
    """Custom type hpnicfIpxRouteLoadBalancePaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HpnicfIpxRouteLoadBalancePaths_Type.__name__ = "Integer32"
_HpnicfIpxRouteLoadBalancePaths_Object = MibScalar
hpnicfIpxRouteLoadBalancePaths = _HpnicfIpxRouteLoadBalancePaths_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 4),
    _HpnicfIpxRouteLoadBalancePaths_Type()
)
hpnicfIpxRouteLoadBalancePaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpxRouteLoadBalancePaths.setStatus("current")


class _HpnicfIpxRouteMaxResPaths_Type(Integer32):
    """Custom type hpnicfIpxRouteMaxResPaths based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfIpxRouteMaxResPaths_Type.__name__ = "Integer32"
_HpnicfIpxRouteMaxResPaths_Object = MibScalar
hpnicfIpxRouteMaxResPaths = _HpnicfIpxRouteMaxResPaths_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 5),
    _HpnicfIpxRouteMaxResPaths_Type()
)
hpnicfIpxRouteMaxResPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpxRouteMaxResPaths.setStatus("current")
_HpnicfIpxRouteTable_Object = MibTable
hpnicfIpxRouteTable = _HpnicfIpxRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6)
)
if mibBuilder.loadTexts:
    hpnicfIpxRouteTable.setStatus("current")
_HpnicfIpxRouteEntry_Object = MibTableRow
hpnicfIpxRouteEntry = _HpnicfIpxRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6, 1)
)
hpnicfIpxRouteEntry.setIndexNames(
    (0, "HPN-ICF-IPX-MIB", "hpnicfIpxRouteIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIpxRouteEntry.setStatus("current")
_HpnicfIpxRouteIndex_Type = Integer32
_HpnicfIpxRouteIndex_Object = MibTableColumn
hpnicfIpxRouteIndex = _HpnicfIpxRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6, 1, 1),
    _HpnicfIpxRouteIndex_Type()
)
hpnicfIpxRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpxRouteIndex.setStatus("current")


class _HpnicfIpxRouteDestNetId_Type(OctetString):
    """Custom type hpnicfIpxRouteDestNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HpnicfIpxRouteDestNetId_Type.__name__ = "OctetString"
_HpnicfIpxRouteDestNetId_Object = MibTableColumn
hpnicfIpxRouteDestNetId = _HpnicfIpxRouteDestNetId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6, 1, 2),
    _HpnicfIpxRouteDestNetId_Type()
)
hpnicfIpxRouteDestNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteDestNetId.setStatus("current")


class _HpnicfIpxRouteNextHop_Type(OctetString):
    """Custom type hpnicfIpxRouteNextHop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HpnicfIpxRouteNextHop_Type.__name__ = "OctetString"
_HpnicfIpxRouteNextHop_Object = MibTableColumn
hpnicfIpxRouteNextHop = _HpnicfIpxRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6, 1, 3),
    _HpnicfIpxRouteNextHop_Type()
)
hpnicfIpxRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteNextHop.setStatus("current")


class _HpnicfIpxRoutePro_Type(Integer32):
    """Custom type hpnicfIpxRoutePro based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("rip", 2))
    )


_HpnicfIpxRoutePro_Type.__name__ = "Integer32"
_HpnicfIpxRoutePro_Object = MibTableColumn
hpnicfIpxRoutePro = _HpnicfIpxRoutePro_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6, 1, 4),
    _HpnicfIpxRoutePro_Type()
)
hpnicfIpxRoutePro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRoutePro.setStatus("current")
_HpnicfIpxRoutePre_Type = Integer32
_HpnicfIpxRoutePre_Object = MibTableColumn
hpnicfIpxRoutePre = _HpnicfIpxRoutePre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6, 1, 5),
    _HpnicfIpxRoutePre_Type()
)
hpnicfIpxRoutePre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRoutePre.setStatus("current")


class _HpnicfIpxRouteTicks_Type(Integer32):
    """Custom type hpnicfIpxRouteTicks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_HpnicfIpxRouteTicks_Type.__name__ = "Integer32"
_HpnicfIpxRouteTicks_Object = MibTableColumn
hpnicfIpxRouteTicks = _HpnicfIpxRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6, 1, 6),
    _HpnicfIpxRouteTicks_Type()
)
hpnicfIpxRouteTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteTicks.setStatus("current")


class _HpnicfIpxRouteHops_Type(Integer32):
    """Custom type hpnicfIpxRouteHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfIpxRouteHops_Type.__name__ = "Integer32"
_HpnicfIpxRouteHops_Object = MibTableColumn
hpnicfIpxRouteHops = _HpnicfIpxRouteHops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6, 1, 7),
    _HpnicfIpxRouteHops_Type()
)
hpnicfIpxRouteHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteHops.setStatus("current")


class _HpnicfIpxRouteTime_Type(Integer32):
    """Custom type hpnicfIpxRouteTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_HpnicfIpxRouteTime_Type.__name__ = "Integer32"
_HpnicfIpxRouteTime_Object = MibTableColumn
hpnicfIpxRouteTime = _HpnicfIpxRouteTime_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6, 1, 8),
    _HpnicfIpxRouteTime_Type()
)
hpnicfIpxRouteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteTime.setStatus("current")


class _HpnicfIpxRouteOutInterface_Type(OctetString):
    """Custom type hpnicfIpxRouteOutInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HpnicfIpxRouteOutInterface_Type.__name__ = "OctetString"
_HpnicfIpxRouteOutInterface_Object = MibTableColumn
hpnicfIpxRouteOutInterface = _HpnicfIpxRouteOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 6, 1, 9),
    _HpnicfIpxRouteOutInterface_Type()
)
hpnicfIpxRouteOutInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteOutInterface.setStatus("current")
_HpnicfIpxStaticRouteTable_Object = MibTable
hpnicfIpxStaticRouteTable = _HpnicfIpxStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 7)
)
if mibBuilder.loadTexts:
    hpnicfIpxStaticRouteTable.setStatus("current")
_HpnicfIpxStaticRouteEntry_Object = MibTableRow
hpnicfIpxStaticRouteEntry = _HpnicfIpxStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 7, 1)
)
hpnicfIpxStaticRouteEntry.setIndexNames(
    (0, "HPN-ICF-IPX-MIB", "hpnicfIpxStaticRouteDestNetId"),
    (0, "HPN-ICF-IPX-MIB", "hpnicfIpxStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    hpnicfIpxStaticRouteEntry.setStatus("current")


class _HpnicfIpxStaticRouteDestNetId_Type(OctetString):
    """Custom type hpnicfIpxStaticRouteDestNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HpnicfIpxStaticRouteDestNetId_Type.__name__ = "OctetString"
_HpnicfIpxStaticRouteDestNetId_Object = MibTableColumn
hpnicfIpxStaticRouteDestNetId = _HpnicfIpxStaticRouteDestNetId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 7, 1, 1),
    _HpnicfIpxStaticRouteDestNetId_Type()
)
hpnicfIpxStaticRouteDestNetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpxStaticRouteDestNetId.setStatus("current")


class _HpnicfIpxStaticRouteNextHop_Type(OctetString):
    """Custom type hpnicfIpxStaticRouteNextHop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_HpnicfIpxStaticRouteNextHop_Type.__name__ = "OctetString"
_HpnicfIpxStaticRouteNextHop_Object = MibTableColumn
hpnicfIpxStaticRouteNextHop = _HpnicfIpxStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 7, 1, 2),
    _HpnicfIpxStaticRouteNextHop_Type()
)
hpnicfIpxStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpxStaticRouteNextHop.setStatus("current")


class _HpnicfIpxStaticRoutePre_Type(Integer32):
    """Custom type hpnicfIpxStaticRoutePre based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfIpxStaticRoutePre_Type.__name__ = "Integer32"
_HpnicfIpxStaticRoutePre_Object = MibTableColumn
hpnicfIpxStaticRoutePre = _HpnicfIpxStaticRoutePre_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 7, 1, 3),
    _HpnicfIpxStaticRoutePre_Type()
)
hpnicfIpxStaticRoutePre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticRoutePre.setStatus("current")


class _HpnicfIpxStaticRouteOutIf_Type(OctetString):
    """Custom type hpnicfIpxStaticRouteOutIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HpnicfIpxStaticRouteOutIf_Type.__name__ = "OctetString"
_HpnicfIpxStaticRouteOutIf_Object = MibTableColumn
hpnicfIpxStaticRouteOutIf = _HpnicfIpxStaticRouteOutIf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 7, 1, 4),
    _HpnicfIpxStaticRouteOutIf_Type()
)
hpnicfIpxStaticRouteOutIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticRouteOutIf.setStatus("current")


class _HpnicfIpxStaticRouteTicks_Type(Integer32):
    """Custom type hpnicfIpxStaticRouteTicks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_HpnicfIpxStaticRouteTicks_Type.__name__ = "Integer32"
_HpnicfIpxStaticRouteTicks_Object = MibTableColumn
hpnicfIpxStaticRouteTicks = _HpnicfIpxStaticRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 7, 1, 5),
    _HpnicfIpxStaticRouteTicks_Type()
)
hpnicfIpxStaticRouteTicks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticRouteTicks.setStatus("current")


class _HpnicfIpxStaticRouteHops_Type(Integer32):
    """Custom type hpnicfIpxStaticRouteHops based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpnicfIpxStaticRouteHops_Type.__name__ = "Integer32"
_HpnicfIpxStaticRouteHops_Object = MibTableColumn
hpnicfIpxStaticRouteHops = _HpnicfIpxStaticRouteHops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 7, 1, 6),
    _HpnicfIpxStaticRouteHops_Type()
)
hpnicfIpxStaticRouteHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticRouteHops.setStatus("current")


class _HpnicfIpxStaticRouteStatus_Type(Integer32):
    """Custom type hpnicfIpxStaticRouteStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HpnicfIpxStaticRouteStatus_Type.__name__ = "Integer32"
_HpnicfIpxStaticRouteStatus_Object = MibTableColumn
hpnicfIpxStaticRouteStatus = _HpnicfIpxStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 7, 1, 7),
    _HpnicfIpxStaticRouteStatus_Type()
)
hpnicfIpxStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticRouteStatus.setStatus("current")
_HpnicfIpxStaticRouteRowStatus_Type = RowStatus
_HpnicfIpxStaticRouteRowStatus_Object = MibTableColumn
hpnicfIpxStaticRouteRowStatus = _HpnicfIpxStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 7, 1, 8),
    _HpnicfIpxStaticRouteRowStatus_Type()
)
hpnicfIpxStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticRouteRowStatus.setStatus("current")
_HpnicfIpxRouteStatTable_Object = MibTable
hpnicfIpxRouteStatTable = _HpnicfIpxRouteStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 8)
)
if mibBuilder.loadTexts:
    hpnicfIpxRouteStatTable.setStatus("current")
_HpnicfIpxRouteStatEntry_Object = MibTableRow
hpnicfIpxRouteStatEntry = _HpnicfIpxRouteStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 8, 1)
)
hpnicfIpxRouteStatEntry.setIndexNames(
    (0, "HPN-ICF-IPX-MIB", "hpnicfIpxRouteStatPro"),
)
if mibBuilder.loadTexts:
    hpnicfIpxRouteStatEntry.setStatus("current")


class _HpnicfIpxRouteStatPro_Type(Integer32):
    """Custom type hpnicfIpxRouteStatPro based on Integer32"""
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
        *(("default", 4),
          ("direct", 1),
          ("rip", 3),
          ("static", 2),
          ("total", 5))
    )


_HpnicfIpxRouteStatPro_Type.__name__ = "Integer32"
_HpnicfIpxRouteStatPro_Object = MibTableColumn
hpnicfIpxRouteStatPro = _HpnicfIpxRouteStatPro_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 8, 1, 1),
    _HpnicfIpxRouteStatPro_Type()
)
hpnicfIpxRouteStatPro.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpxRouteStatPro.setStatus("current")
_HpnicfIpxRouteStatRoutes_Type = Counter32
_HpnicfIpxRouteStatRoutes_Object = MibTableColumn
hpnicfIpxRouteStatRoutes = _HpnicfIpxRouteStatRoutes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 8, 1, 2),
    _HpnicfIpxRouteStatRoutes_Type()
)
hpnicfIpxRouteStatRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteStatRoutes.setStatus("current")
_HpnicfIpxRouteStatActives_Type = Counter32
_HpnicfIpxRouteStatActives_Object = MibTableColumn
hpnicfIpxRouteStatActives = _HpnicfIpxRouteStatActives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 8, 1, 3),
    _HpnicfIpxRouteStatActives_Type()
)
hpnicfIpxRouteStatActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteStatActives.setStatus("current")
_HpnicfIpxRouteStatAddeds_Type = Counter32
_HpnicfIpxRouteStatAddeds_Object = MibTableColumn
hpnicfIpxRouteStatAddeds = _HpnicfIpxRouteStatAddeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 8, 1, 4),
    _HpnicfIpxRouteStatAddeds_Type()
)
hpnicfIpxRouteStatAddeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteStatAddeds.setStatus("current")
_HpnicfIpxRouteStatDeleteds_Type = Counter32
_HpnicfIpxRouteStatDeleteds_Object = MibTableColumn
hpnicfIpxRouteStatDeleteds = _HpnicfIpxRouteStatDeleteds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 8, 1, 5),
    _HpnicfIpxRouteStatDeleteds_Type()
)
hpnicfIpxRouteStatDeleteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteStatDeleteds.setStatus("current")
_HpnicfIpxRouteStatFreeds_Type = Counter32
_HpnicfIpxRouteStatFreeds_Object = MibTableColumn
hpnicfIpxRouteStatFreeds = _HpnicfIpxRouteStatFreeds_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 2, 8, 1, 6),
    _HpnicfIpxRouteStatFreeds_Type()
)
hpnicfIpxRouteStatFreeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxRouteStatFreeds.setStatus("current")
_HpnicfIpxSap_ObjectIdentity = ObjectIdentity
hpnicfIpxSap = _HpnicfIpxSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3)
)


class _HpnicfIpxSapMultiplier_Type(Integer32):
    """Custom type hpnicfIpxSapMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_HpnicfIpxSapMultiplier_Type.__name__ = "Integer32"
_HpnicfIpxSapMultiplier_Object = MibScalar
hpnicfIpxSapMultiplier = _HpnicfIpxSapMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 1),
    _HpnicfIpxSapMultiplier_Type()
)
hpnicfIpxSapMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpxSapMultiplier.setStatus("current")


class _HpnicfIpxSapUpdateTimer_Type(Integer32):
    """Custom type hpnicfIpxSapUpdateTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60000),
    )


_HpnicfIpxSapUpdateTimer_Type.__name__ = "Integer32"
_HpnicfIpxSapUpdateTimer_Object = MibScalar
hpnicfIpxSapUpdateTimer = _HpnicfIpxSapUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 2),
    _HpnicfIpxSapUpdateTimer_Type()
)
hpnicfIpxSapUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpxSapUpdateTimer.setStatus("current")


class _HpnicfIpxSapGnsLoadBalance_Type(EnabledStatus):
    """Custom type hpnicfIpxSapGnsLoadBalance based on EnabledStatus"""


_HpnicfIpxSapGnsLoadBalance_Object = MibScalar
hpnicfIpxSapGnsLoadBalance = _HpnicfIpxSapGnsLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 3),
    _HpnicfIpxSapGnsLoadBalance_Type()
)
hpnicfIpxSapGnsLoadBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpxSapGnsLoadBalance.setStatus("current")


class _HpnicfIpxSapMaxResServers_Type(Integer32):
    """Custom type hpnicfIpxSapMaxResServers based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_HpnicfIpxSapMaxResServers_Type.__name__ = "Integer32"
_HpnicfIpxSapMaxResServers_Object = MibScalar
hpnicfIpxSapMaxResServers = _HpnicfIpxSapMaxResServers_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 4),
    _HpnicfIpxSapMaxResServers_Type()
)
hpnicfIpxSapMaxResServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpnicfIpxSapMaxResServers.setStatus("current")
_HpnicfIpxServiceTable_Object = MibTable
hpnicfIpxServiceTable = _HpnicfIpxServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5)
)
if mibBuilder.loadTexts:
    hpnicfIpxServiceTable.setStatus("current")
_HpnicfIpxServiceEntry_Object = MibTableRow
hpnicfIpxServiceEntry = _HpnicfIpxServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5, 1)
)
hpnicfIpxServiceEntry.setIndexNames(
    (0, "HPN-ICF-IPX-MIB", "hpnicfIpxServiceIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIpxServiceEntry.setStatus("current")
_HpnicfIpxServiceIndex_Type = Integer32
_HpnicfIpxServiceIndex_Object = MibTableColumn
hpnicfIpxServiceIndex = _HpnicfIpxServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5, 1, 1),
    _HpnicfIpxServiceIndex_Type()
)
hpnicfIpxServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpxServiceIndex.setStatus("current")


class _HpnicfIpxServiceName_Type(OctetString):
    """Custom type hpnicfIpxServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HpnicfIpxServiceName_Type.__name__ = "OctetString"
_HpnicfIpxServiceName_Object = MibTableColumn
hpnicfIpxServiceName = _HpnicfIpxServiceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5, 1, 2),
    _HpnicfIpxServiceName_Type()
)
hpnicfIpxServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxServiceName.setStatus("current")


class _HpnicfIpxServiceType_Type(OctetString):
    """Custom type hpnicfIpxServiceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HpnicfIpxServiceType_Type.__name__ = "OctetString"
_HpnicfIpxServiceType_Object = MibTableColumn
hpnicfIpxServiceType = _HpnicfIpxServiceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5, 1, 3),
    _HpnicfIpxServiceType_Type()
)
hpnicfIpxServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxServiceType.setStatus("current")


class _HpnicfIpxServiceNetId_Type(OctetString):
    """Custom type hpnicfIpxServiceNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HpnicfIpxServiceNetId_Type.__name__ = "OctetString"
_HpnicfIpxServiceNetId_Object = MibTableColumn
hpnicfIpxServiceNetId = _HpnicfIpxServiceNetId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5, 1, 4),
    _HpnicfIpxServiceNetId_Type()
)
hpnicfIpxServiceNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxServiceNetId.setStatus("current")


class _HpnicfIpxServiceNodeId_Type(OctetString):
    """Custom type hpnicfIpxServiceNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnicfIpxServiceNodeId_Type.__name__ = "OctetString"
_HpnicfIpxServiceNodeId_Object = MibTableColumn
hpnicfIpxServiceNodeId = _HpnicfIpxServiceNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5, 1, 5),
    _HpnicfIpxServiceNodeId_Type()
)
hpnicfIpxServiceNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxServiceNodeId.setStatus("current")


class _HpnicfIpxServiceSocketNo_Type(OctetString):
    """Custom type hpnicfIpxServiceSocketNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HpnicfIpxServiceSocketNo_Type.__name__ = "OctetString"
_HpnicfIpxServiceSocketNo_Object = MibTableColumn
hpnicfIpxServiceSocketNo = _HpnicfIpxServiceSocketNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5, 1, 6),
    _HpnicfIpxServiceSocketNo_Type()
)
hpnicfIpxServiceSocketNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxServiceSocketNo.setStatus("current")
_HpnicfIpxServicePreference_Type = Integer32
_HpnicfIpxServicePreference_Object = MibTableColumn
hpnicfIpxServicePreference = _HpnicfIpxServicePreference_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5, 1, 7),
    _HpnicfIpxServicePreference_Type()
)
hpnicfIpxServicePreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxServicePreference.setStatus("current")


class _HpnicfIpxServiceHops_Type(Integer32):
    """Custom type hpnicfIpxServiceHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_HpnicfIpxServiceHops_Type.__name__ = "Integer32"
_HpnicfIpxServiceHops_Object = MibTableColumn
hpnicfIpxServiceHops = _HpnicfIpxServiceHops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5, 1, 8),
    _HpnicfIpxServiceHops_Type()
)
hpnicfIpxServiceHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxServiceHops.setStatus("current")


class _HpnicfIpxServiceRecvIf_Type(OctetString):
    """Custom type hpnicfIpxServiceRecvIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_HpnicfIpxServiceRecvIf_Type.__name__ = "OctetString"
_HpnicfIpxServiceRecvIf_Object = MibTableColumn
hpnicfIpxServiceRecvIf = _HpnicfIpxServiceRecvIf_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 5, 1, 9),
    _HpnicfIpxServiceRecvIf_Type()
)
hpnicfIpxServiceRecvIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxServiceRecvIf.setStatus("current")
_HpnicfIpxStaticServiceTable_Object = MibTable
hpnicfIpxStaticServiceTable = _HpnicfIpxStaticServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6)
)
if mibBuilder.loadTexts:
    hpnicfIpxStaticServiceTable.setStatus("current")
_HpnicfIpxStaticServiceEntry_Object = MibTableRow
hpnicfIpxStaticServiceEntry = _HpnicfIpxStaticServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6, 1)
)
hpnicfIpxStaticServiceEntry.setIndexNames(
    (0, "HPN-ICF-IPX-MIB", "hpnicfIpxStaticServiceType"),
    (0, "HPN-ICF-IPX-MIB", "hpnicfIpxStaticServiceName"),
    (0, "HPN-ICF-IPX-MIB", "hpnicfIpxStaticServiceNetId"),
)
if mibBuilder.loadTexts:
    hpnicfIpxStaticServiceEntry.setStatus("current")


class _HpnicfIpxStaticServiceType_Type(OctetString):
    """Custom type hpnicfIpxStaticServiceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HpnicfIpxStaticServiceType_Type.__name__ = "OctetString"
_HpnicfIpxStaticServiceType_Object = MibTableColumn
hpnicfIpxStaticServiceType = _HpnicfIpxStaticServiceType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6, 1, 1),
    _HpnicfIpxStaticServiceType_Type()
)
hpnicfIpxStaticServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpxStaticServiceType.setStatus("current")


class _HpnicfIpxStaticServiceName_Type(OctetString):
    """Custom type hpnicfIpxStaticServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_HpnicfIpxStaticServiceName_Type.__name__ = "OctetString"
_HpnicfIpxStaticServiceName_Object = MibTableColumn
hpnicfIpxStaticServiceName = _HpnicfIpxStaticServiceName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6, 1, 2),
    _HpnicfIpxStaticServiceName_Type()
)
hpnicfIpxStaticServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpxStaticServiceName.setStatus("current")


class _HpnicfIpxStaticServiceNetId_Type(OctetString):
    """Custom type hpnicfIpxStaticServiceNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HpnicfIpxStaticServiceNetId_Type.__name__ = "OctetString"
_HpnicfIpxStaticServiceNetId_Object = MibTableColumn
hpnicfIpxStaticServiceNetId = _HpnicfIpxStaticServiceNetId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6, 1, 3),
    _HpnicfIpxStaticServiceNetId_Type()
)
hpnicfIpxStaticServiceNetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpxStaticServiceNetId.setStatus("current")


class _HpnicfIpxStaticServiceNodeId_Type(OctetString):
    """Custom type hpnicfIpxStaticServiceNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnicfIpxStaticServiceNodeId_Type.__name__ = "OctetString"
_HpnicfIpxStaticServiceNodeId_Object = MibTableColumn
hpnicfIpxStaticServiceNodeId = _HpnicfIpxStaticServiceNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6, 1, 4),
    _HpnicfIpxStaticServiceNodeId_Type()
)
hpnicfIpxStaticServiceNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticServiceNodeId.setStatus("current")


class _HpnicfIpxStatciServiceSocketNo_Type(OctetString):
    """Custom type hpnicfIpxStatciServiceSocketNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_HpnicfIpxStatciServiceSocketNo_Type.__name__ = "OctetString"
_HpnicfIpxStatciServiceSocketNo_Object = MibTableColumn
hpnicfIpxStatciServiceSocketNo = _HpnicfIpxStatciServiceSocketNo_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6, 1, 5),
    _HpnicfIpxStatciServiceSocketNo_Type()
)
hpnicfIpxStatciServiceSocketNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStatciServiceSocketNo.setStatus("current")


class _HpnicfIpxStaticServicePreference_Type(Integer32):
    """Custom type hpnicfIpxStaticServicePreference based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HpnicfIpxStaticServicePreference_Type.__name__ = "Integer32"
_HpnicfIpxStaticServicePreference_Object = MibTableColumn
hpnicfIpxStaticServicePreference = _HpnicfIpxStaticServicePreference_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6, 1, 6),
    _HpnicfIpxStaticServicePreference_Type()
)
hpnicfIpxStaticServicePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticServicePreference.setStatus("current")


class _HpnicfIpxStaticServiceHops_Type(Integer32):
    """Custom type hpnicfIpxStaticServiceHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_HpnicfIpxStaticServiceHops_Type.__name__ = "Integer32"
_HpnicfIpxStaticServiceHops_Object = MibTableColumn
hpnicfIpxStaticServiceHops = _HpnicfIpxStaticServiceHops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6, 1, 7),
    _HpnicfIpxStaticServiceHops_Type()
)
hpnicfIpxStaticServiceHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticServiceHops.setStatus("current")


class _HpnicfIpxStaticServiceStatus_Type(Integer32):
    """Custom type hpnicfIpxStaticServiceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_HpnicfIpxStaticServiceStatus_Type.__name__ = "Integer32"
_HpnicfIpxStaticServiceStatus_Object = MibTableColumn
hpnicfIpxStaticServiceStatus = _HpnicfIpxStaticServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6, 1, 8),
    _HpnicfIpxStaticServiceStatus_Type()
)
hpnicfIpxStaticServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticServiceStatus.setStatus("current")
_HpnicfIpxStaticServiceRowStatus_Type = RowStatus
_HpnicfIpxStaticServiceRowStatus_Object = MibTableColumn
hpnicfIpxStaticServiceRowStatus = _HpnicfIpxStaticServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 3, 6, 1, 9),
    _HpnicfIpxStaticServiceRowStatus_Type()
)
hpnicfIpxStaticServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpnicfIpxStaticServiceRowStatus.setStatus("current")
_HpnicfIpxStat_ObjectIdentity = ObjectIdentity
hpnicfIpxStat = _HpnicfIpxStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4)
)
_HpnicfIpxStatGlobal_ObjectIdentity = ObjectIdentity
hpnicfIpxStatGlobal = _HpnicfIpxStatGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1)
)
_HpnicfIpxStatTotalReceives_Type = Counter32
_HpnicfIpxStatTotalReceives_Object = MibScalar
hpnicfIpxStatTotalReceives = _HpnicfIpxStatTotalReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 1),
    _HpnicfIpxStatTotalReceives_Type()
)
hpnicfIpxStatTotalReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatTotalReceives.setStatus("current")
_HpnicfIpxStatPitchs_Type = Counter32
_HpnicfIpxStatPitchs_Object = MibScalar
hpnicfIpxStatPitchs = _HpnicfIpxStatPitchs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 2),
    _HpnicfIpxStatPitchs_Type()
)
hpnicfIpxStatPitchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatPitchs.setStatus("current")
_HpnicfIpxStatLenErrors_Type = Counter32
_HpnicfIpxStatLenErrors_Object = MibScalar
hpnicfIpxStatLenErrors = _HpnicfIpxStatLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 3),
    _HpnicfIpxStatLenErrors_Type()
)
hpnicfIpxStatLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatLenErrors.setStatus("current")
_HpnicfIpxStatFormatErrors_Type = Counter32
_HpnicfIpxStatFormatErrors_Object = MibScalar
hpnicfIpxStatFormatErrors = _HpnicfIpxStatFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 4),
    _HpnicfIpxStatFormatErrors_Type()
)
hpnicfIpxStatFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatFormatErrors.setStatus("current")
_HpnicfIpxStatBadHops_Type = Counter32
_HpnicfIpxStatBadHops_Object = MibScalar
hpnicfIpxStatBadHops = _HpnicfIpxStatBadHops_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 5),
    _HpnicfIpxStatBadHops_Type()
)
hpnicfIpxStatBadHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatBadHops.setStatus("current")
_HpnicfIpxStatHopsDiscards_Type = Counter32
_HpnicfIpxStatHopsDiscards_Object = MibScalar
hpnicfIpxStatHopsDiscards = _HpnicfIpxStatHopsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 6),
    _HpnicfIpxStatHopsDiscards_Type()
)
hpnicfIpxStatHopsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatHopsDiscards.setStatus("current")
_HpnicfIpxStatOtherErrors_Type = Counter32
_HpnicfIpxStatOtherErrors_Object = MibScalar
hpnicfIpxStatOtherErrors = _HpnicfIpxStatOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 7),
    _HpnicfIpxStatOtherErrors_Type()
)
hpnicfIpxStatOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatOtherErrors.setStatus("current")
_HpnicfIpxStatLocalDests_Type = Counter32
_HpnicfIpxStatLocalDests_Object = MibScalar
hpnicfIpxStatLocalDests = _HpnicfIpxStatLocalDests_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 8),
    _HpnicfIpxStatLocalDests_Type()
)
hpnicfIpxStatLocalDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatLocalDests.setStatus("current")
_HpnicfIpxStatCantDeals_Type = Counter32
_HpnicfIpxStatCantDeals_Object = MibScalar
hpnicfIpxStatCantDeals = _HpnicfIpxStatCantDeals_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 9),
    _HpnicfIpxStatCantDeals_Type()
)
hpnicfIpxStatCantDeals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatCantDeals.setStatus("current")
_HpnicfIpxStatForwards_Type = Counter32
_HpnicfIpxStatForwards_Object = MibScalar
hpnicfIpxStatForwards = _HpnicfIpxStatForwards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 10),
    _HpnicfIpxStatForwards_Type()
)
hpnicfIpxStatForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatForwards.setStatus("current")
_HpnicfIpxStatGenerates_Type = Counter32
_HpnicfIpxStatGenerates_Object = MibScalar
hpnicfIpxStatGenerates = _HpnicfIpxStatGenerates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 11),
    _HpnicfIpxStatGenerates_Type()
)
hpnicfIpxStatGenerates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatGenerates.setStatus("current")
_HpnicfIpxStatNoRoutes_Type = Counter32
_HpnicfIpxStatNoRoutes_Object = MibScalar
hpnicfIpxStatNoRoutes = _HpnicfIpxStatNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 12),
    _HpnicfIpxStatNoRoutes_Type()
)
hpnicfIpxStatNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatNoRoutes.setStatus("current")
_HpnicfIpxStatOutDiscards_Type = Counter32
_HpnicfIpxStatOutDiscards_Object = MibScalar
hpnicfIpxStatOutDiscards = _HpnicfIpxStatOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 13),
    _HpnicfIpxStatOutDiscards_Type()
)
hpnicfIpxStatOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatOutDiscards.setStatus("current")
_HpnicfIpxStatRipSends_Type = Counter32
_HpnicfIpxStatRipSends_Object = MibScalar
hpnicfIpxStatRipSends = _HpnicfIpxStatRipSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 14),
    _HpnicfIpxStatRipSends_Type()
)
hpnicfIpxStatRipSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatRipSends.setStatus("current")
_HpnicfIpxStatRipReceives_Type = Counter32
_HpnicfIpxStatRipReceives_Object = MibScalar
hpnicfIpxStatRipReceives = _HpnicfIpxStatRipReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 15),
    _HpnicfIpxStatRipReceives_Type()
)
hpnicfIpxStatRipReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatRipReceives.setStatus("current")
_HpnicfIpxStaRipRspSends_Type = Counter32
_HpnicfIpxStaRipRspSends_Object = MibScalar
hpnicfIpxStaRipRspSends = _HpnicfIpxStaRipRspSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 16),
    _HpnicfIpxStaRipRspSends_Type()
)
hpnicfIpxStaRipRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStaRipRspSends.setStatus("current")
_HpnicfIpxStaRipRspReceives_Type = Counter32
_HpnicfIpxStaRipRspReceives_Object = MibScalar
hpnicfIpxStaRipRspReceives = _HpnicfIpxStaRipRspReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 17),
    _HpnicfIpxStaRipRspReceives_Type()
)
hpnicfIpxStaRipRspReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStaRipRspReceives.setStatus("current")
_HpnicfIpxStatRipReqReceives_Type = Counter32
_HpnicfIpxStatRipReqReceives_Object = MibScalar
hpnicfIpxStatRipReqReceives = _HpnicfIpxStatRipReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 18),
    _HpnicfIpxStatRipReqReceives_Type()
)
hpnicfIpxStatRipReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatRipReqReceives.setStatus("current")
_HpnicfIpxStatRipReqDeals_Type = Counter32
_HpnicfIpxStatRipReqDeals_Object = MibScalar
hpnicfIpxStatRipReqDeals = _HpnicfIpxStatRipReqDeals_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 19),
    _HpnicfIpxStatRipReqDeals_Type()
)
hpnicfIpxStatRipReqDeals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatRipReqDeals.setStatus("current")
_HpnicfIpxStatRipReqSends_Type = Counter32
_HpnicfIpxStatRipReqSends_Object = MibScalar
hpnicfIpxStatRipReqSends = _HpnicfIpxStatRipReqSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 20),
    _HpnicfIpxStatRipReqSends_Type()
)
hpnicfIpxStatRipReqSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatRipReqSends.setStatus("current")
_HpnicfIpxStatRipPeriUpdates_Type = Counter32
_HpnicfIpxStatRipPeriUpdates_Object = MibScalar
hpnicfIpxStatRipPeriUpdates = _HpnicfIpxStatRipPeriUpdates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 21),
    _HpnicfIpxStatRipPeriUpdates_Type()
)
hpnicfIpxStatRipPeriUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatRipPeriUpdates.setStatus("current")
_HpnicfIpxStatSapGenReqReceives_Type = Counter32
_HpnicfIpxStatSapGenReqReceives_Object = MibScalar
hpnicfIpxStatSapGenReqReceives = _HpnicfIpxStatSapGenReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 22),
    _HpnicfIpxStatSapGenReqReceives_Type()
)
hpnicfIpxStatSapGenReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatSapGenReqReceives.setStatus("current")
_HpnicfIpxStatSapSpecReqReceives_Type = Counter32
_HpnicfIpxStatSapSpecReqReceives_Object = MibScalar
hpnicfIpxStatSapSpecReqReceives = _HpnicfIpxStatSapSpecReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 23),
    _HpnicfIpxStatSapSpecReqReceives_Type()
)
hpnicfIpxStatSapSpecReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatSapSpecReqReceives.setStatus("current")
_HpnicfIpxStatSapGnsReqReceives_Type = Counter32
_HpnicfIpxStatSapGnsReqReceives_Object = MibScalar
hpnicfIpxStatSapGnsReqReceives = _HpnicfIpxStatSapGnsReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 24),
    _HpnicfIpxStatSapGnsReqReceives_Type()
)
hpnicfIpxStatSapGnsReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatSapGnsReqReceives.setStatus("current")
_HpnicfIpxStatSapGenRspSends_Type = Counter32
_HpnicfIpxStatSapGenRspSends_Object = MibScalar
hpnicfIpxStatSapGenRspSends = _HpnicfIpxStatSapGenRspSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 25),
    _HpnicfIpxStatSapGenRspSends_Type()
)
hpnicfIpxStatSapGenRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatSapGenRspSends.setStatus("current")
_HpnicfIpxStatSapSpecRspSends_Type = Counter32
_HpnicfIpxStatSapSpecRspSends_Object = MibScalar
hpnicfIpxStatSapSpecRspSends = _HpnicfIpxStatSapSpecRspSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 26),
    _HpnicfIpxStatSapSpecRspSends_Type()
)
hpnicfIpxStatSapSpecRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatSapSpecRspSends.setStatus("current")
_HpnicfIpxStatSapGnsRspSends_Type = Counter32
_HpnicfIpxStatSapGnsRspSends_Object = MibScalar
hpnicfIpxStatSapGnsRspSends = _HpnicfIpxStatSapGnsRspSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 27),
    _HpnicfIpxStatSapGnsRspSends_Type()
)
hpnicfIpxStatSapGnsRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatSapGnsRspSends.setStatus("current")
_HpnicfIpxStatSapPeriUpdates_Type = Counter32
_HpnicfIpxStatSapPeriUpdates_Object = MibScalar
hpnicfIpxStatSapPeriUpdates = _HpnicfIpxStatSapPeriUpdates_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 28),
    _HpnicfIpxStatSapPeriUpdates_Type()
)
hpnicfIpxStatSapPeriUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatSapPeriUpdates.setStatus("current")
_HpnicfIpxStatSapInPktErrors_Type = Counter32
_HpnicfIpxStatSapInPktErrors_Object = MibScalar
hpnicfIpxStatSapInPktErrors = _HpnicfIpxStatSapInPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 1, 29),
    _HpnicfIpxStatSapInPktErrors_Type()
)
hpnicfIpxStatSapInPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxStatSapInPktErrors.setStatus("current")
_HpnicfIpxStatInterface_ObjectIdentity = ObjectIdentity
hpnicfIpxStatInterface = _HpnicfIpxStatInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2)
)
_HpnicfIpxIfStatTable_Object = MibTable
hpnicfIpxIfStatTable = _HpnicfIpxIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hpnicfIpxIfStatTable.setStatus("current")
_HpnicfIpxIfStatEntry_Object = MibTableRow
hpnicfIpxIfStatEntry = _HpnicfIpxIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1)
)
hpnicfIpxIfStatEntry.setIndexNames(
    (0, "HPN-ICF-IPX-MIB", "hpnicfIpxIfStatIndex"),
)
if mibBuilder.loadTexts:
    hpnicfIpxIfStatEntry.setStatus("current")


class _HpnicfIpxIfStatIndex_Type(Integer32):
    """Custom type hpnicfIpxIfStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HpnicfIpxIfStatIndex_Type.__name__ = "Integer32"
_HpnicfIpxIfStatIndex_Object = MibTableColumn
hpnicfIpxIfStatIndex = _HpnicfIpxIfStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 1),
    _HpnicfIpxIfStatIndex_Type()
)
hpnicfIpxIfStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatIndex.setStatus("current")


class _HpnicfIpxIfStatNetId_Type(OctetString):
    """Custom type hpnicfIpxIfStatNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_HpnicfIpxIfStatNetId_Type.__name__ = "OctetString"
_HpnicfIpxIfStatNetId_Object = MibTableColumn
hpnicfIpxIfStatNetId = _HpnicfIpxIfStatNetId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 2),
    _HpnicfIpxIfStatNetId_Type()
)
hpnicfIpxIfStatNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatNetId.setStatus("current")


class _HpnicfIpxIfStatNodeId_Type(OctetString):
    """Custom type hpnicfIpxIfStatNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_HpnicfIpxIfStatNodeId_Type.__name__ = "OctetString"
_HpnicfIpxIfStatNodeId_Object = MibTableColumn
hpnicfIpxIfStatNodeId = _HpnicfIpxIfStatNodeId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 3),
    _HpnicfIpxIfStatNodeId_Type()
)
hpnicfIpxIfStatNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatNodeId.setStatus("current")
_HpnicfIpxIfStatIpxReceives_Type = Counter32
_HpnicfIpxIfStatIpxReceives_Object = MibTableColumn
hpnicfIpxIfStatIpxReceives = _HpnicfIpxIfStatIpxReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 4),
    _HpnicfIpxIfStatIpxReceives_Type()
)
hpnicfIpxIfStatIpxReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatIpxReceives.setStatus("current")
_HpnicfIpxIfStatIpxSends_Type = Counter32
_HpnicfIpxIfStatIpxSends_Object = MibTableColumn
hpnicfIpxIfStatIpxSends = _HpnicfIpxIfStatIpxSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 5),
    _HpnicfIpxIfStatIpxSends_Type()
)
hpnicfIpxIfStatIpxSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatIpxSends.setStatus("current")
_HpnicfIpxIfStatIpxRecvBytes_Type = Counter32
_HpnicfIpxIfStatIpxRecvBytes_Object = MibTableColumn
hpnicfIpxIfStatIpxRecvBytes = _HpnicfIpxIfStatIpxRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 6),
    _HpnicfIpxIfStatIpxRecvBytes_Type()
)
hpnicfIpxIfStatIpxRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatIpxRecvBytes.setStatus("current")
_HpnicfIpxIfStatIpxSendBytes_Type = Counter32
_HpnicfIpxIfStatIpxSendBytes_Object = MibTableColumn
hpnicfIpxIfStatIpxSendBytes = _HpnicfIpxIfStatIpxSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 7),
    _HpnicfIpxIfStatIpxSendBytes_Type()
)
hpnicfIpxIfStatIpxSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatIpxSendBytes.setStatus("current")
_HpnicfIpxIfStatRipReceives_Type = Counter32
_HpnicfIpxIfStatRipReceives_Object = MibTableColumn
hpnicfIpxIfStatRipReceives = _HpnicfIpxIfStatRipReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 8),
    _HpnicfIpxIfStatRipReceives_Type()
)
hpnicfIpxIfStatRipReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatRipReceives.setStatus("current")
_HpnicfIpxIfStatRipSends_Type = Counter32
_HpnicfIpxIfStatRipSends_Object = MibTableColumn
hpnicfIpxIfStatRipSends = _HpnicfIpxIfStatRipSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 9),
    _HpnicfIpxIfStatRipSends_Type()
)
hpnicfIpxIfStatRipSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatRipSends.setStatus("current")
_HpnicfIpxIfStatRipDiscards_Type = Counter32
_HpnicfIpxIfStatRipDiscards_Object = MibTableColumn
hpnicfIpxIfStatRipDiscards = _HpnicfIpxIfStatRipDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 10),
    _HpnicfIpxIfStatRipDiscards_Type()
)
hpnicfIpxIfStatRipDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatRipDiscards.setStatus("current")
_HpnicfIpxIfStatRipSpecReqReceives_Type = Counter32
_HpnicfIpxIfStatRipSpecReqReceives_Object = MibTableColumn
hpnicfIpxIfStatRipSpecReqReceives = _HpnicfIpxIfStatRipSpecReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 11),
    _HpnicfIpxIfStatRipSpecReqReceives_Type()
)
hpnicfIpxIfStatRipSpecReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatRipSpecReqReceives.setStatus("current")
_HpnicfIpxIfStatRipSpecRspSends_Type = Counter32
_HpnicfIpxIfStatRipSpecRspSends_Object = MibTableColumn
hpnicfIpxIfStatRipSpecRspSends = _HpnicfIpxIfStatRipSpecRspSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 12),
    _HpnicfIpxIfStatRipSpecRspSends_Type()
)
hpnicfIpxIfStatRipSpecRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatRipSpecRspSends.setStatus("current")
_HpnicfIpxIfStatRipGenReqReceives_Type = Counter32
_HpnicfIpxIfStatRipGenReqReceives_Object = MibTableColumn
hpnicfIpxIfStatRipGenReqReceives = _HpnicfIpxIfStatRipGenReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 13),
    _HpnicfIpxIfStatRipGenReqReceives_Type()
)
hpnicfIpxIfStatRipGenReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatRipGenReqReceives.setStatus("current")
_HpnicfIpxIfStatRipGenRspSends_Type = Counter32
_HpnicfIpxIfStatRipGenRspSends_Object = MibTableColumn
hpnicfIpxIfStatRipGenRspSends = _HpnicfIpxIfStatRipGenRspSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 14),
    _HpnicfIpxIfStatRipGenRspSends_Type()
)
hpnicfIpxIfStatRipGenRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatRipGenRspSends.setStatus("current")
_HpnicfIpxIfStatSapReceives_Type = Counter32
_HpnicfIpxIfStatSapReceives_Object = MibTableColumn
hpnicfIpxIfStatSapReceives = _HpnicfIpxIfStatSapReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 15),
    _HpnicfIpxIfStatSapReceives_Type()
)
hpnicfIpxIfStatSapReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatSapReceives.setStatus("current")
_HpnicfIpxIfStatSapSends_Type = Counter32
_HpnicfIpxIfStatSapSends_Object = MibTableColumn
hpnicfIpxIfStatSapSends = _HpnicfIpxIfStatSapSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 16),
    _HpnicfIpxIfStatSapSends_Type()
)
hpnicfIpxIfStatSapSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatSapSends.setStatus("current")
_HpnicfIpxIfStatSapDiscards_Type = Counter32
_HpnicfIpxIfStatSapDiscards_Object = MibTableColumn
hpnicfIpxIfStatSapDiscards = _HpnicfIpxIfStatSapDiscards_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 17),
    _HpnicfIpxIfStatSapDiscards_Type()
)
hpnicfIpxIfStatSapDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatSapDiscards.setStatus("current")
_HpnicfIpxIfStatSapGnsReqReceives_Type = Counter32
_HpnicfIpxIfStatSapGnsReqReceives_Object = MibTableColumn
hpnicfIpxIfStatSapGnsReqReceives = _HpnicfIpxIfStatSapGnsReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 18),
    _HpnicfIpxIfStatSapGnsReqReceives_Type()
)
hpnicfIpxIfStatSapGnsReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatSapGnsReqReceives.setStatus("current")
_HpnicfIpxIfStatSapGnsRspSends_Type = Counter32
_HpnicfIpxIfStatSapGnsRspSends_Object = MibTableColumn
hpnicfIpxIfStatSapGnsRspSends = _HpnicfIpxIfStatSapGnsRspSends_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 15, 2, 34, 4, 2, 1, 1, 19),
    _HpnicfIpxIfStatSapGnsRspSends_Type()
)
hpnicfIpxIfStatSapGnsRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpnicfIpxIfStatSapGnsRspSends.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HPN-ICF-IPX-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hpnicfIpx": hpnicfIpx,
       "hpnicfIpxConfig": hpnicfIpxConfig,
       "hpnicfIpxStatus": hpnicfIpxStatus,
       "hpnicfIpxIfConfigTable": hpnicfIpxIfConfigTable,
       "hpnicfIpxIfConfigEntry": hpnicfIpxIfConfigEntry,
       "hpnicfIpxIfIndex": hpnicfIpxIfIndex,
       "hpnicfIpxIfNetId": hpnicfIpxIfNetId,
       "hpnicfIpxIfNodeId": hpnicfIpxIfNodeId,
       "hpnicfIpxIfSplitHorizon": hpnicfIpxIfSplitHorizon,
       "hpnicfIPxIfTick": hpnicfIPxIfTick,
       "hpnicfIpxIfUpdateChangeOnly": hpnicfIpxIfUpdateChangeOnly,
       "hpnicfIpxIfRipMtu": hpnicfIpxIfRipMtu,
       "hpnicfIpxIfEncapsuleType": hpnicfIpxIfEncapsuleType,
       "hpnicfIpxIfNetbiosPropagation": hpnicfIpxIfNetbiosPropagation,
       "hpnicfIpxIfSapStatus": hpnicfIpxIfSapStatus,
       "hpnicfIpxIfSapMtu": hpnicfIpxIfSapMtu,
       "hpnicfIpxIfGnsReply": hpnicfIpxIfGnsReply,
       "hpnicfIpxIfRowStatus": hpnicfIpxIfRowStatus,
       "hpnicfIpxRip": hpnicfIpxRip,
       "hpnicfIpxRouteMultiplier": hpnicfIpxRouteMultiplier,
       "hpnicfIpxRouteUpdateTimer": hpnicfIpxRouteUpdateTimer,
       "hpnicfIpxRouteImpRouteStatic": hpnicfIpxRouteImpRouteStatic,
       "hpnicfIpxRouteLoadBalancePaths": hpnicfIpxRouteLoadBalancePaths,
       "hpnicfIpxRouteMaxResPaths": hpnicfIpxRouteMaxResPaths,
       "hpnicfIpxRouteTable": hpnicfIpxRouteTable,
       "hpnicfIpxRouteEntry": hpnicfIpxRouteEntry,
       "hpnicfIpxRouteIndex": hpnicfIpxRouteIndex,
       "hpnicfIpxRouteDestNetId": hpnicfIpxRouteDestNetId,
       "hpnicfIpxRouteNextHop": hpnicfIpxRouteNextHop,
       "hpnicfIpxRoutePro": hpnicfIpxRoutePro,
       "hpnicfIpxRoutePre": hpnicfIpxRoutePre,
       "hpnicfIpxRouteTicks": hpnicfIpxRouteTicks,
       "hpnicfIpxRouteHops": hpnicfIpxRouteHops,
       "hpnicfIpxRouteTime": hpnicfIpxRouteTime,
       "hpnicfIpxRouteOutInterface": hpnicfIpxRouteOutInterface,
       "hpnicfIpxStaticRouteTable": hpnicfIpxStaticRouteTable,
       "hpnicfIpxStaticRouteEntry": hpnicfIpxStaticRouteEntry,
       "hpnicfIpxStaticRouteDestNetId": hpnicfIpxStaticRouteDestNetId,
       "hpnicfIpxStaticRouteNextHop": hpnicfIpxStaticRouteNextHop,
       "hpnicfIpxStaticRoutePre": hpnicfIpxStaticRoutePre,
       "hpnicfIpxStaticRouteOutIf": hpnicfIpxStaticRouteOutIf,
       "hpnicfIpxStaticRouteTicks": hpnicfIpxStaticRouteTicks,
       "hpnicfIpxStaticRouteHops": hpnicfIpxStaticRouteHops,
       "hpnicfIpxStaticRouteStatus": hpnicfIpxStaticRouteStatus,
       "hpnicfIpxStaticRouteRowStatus": hpnicfIpxStaticRouteRowStatus,
       "hpnicfIpxRouteStatTable": hpnicfIpxRouteStatTable,
       "hpnicfIpxRouteStatEntry": hpnicfIpxRouteStatEntry,
       "hpnicfIpxRouteStatPro": hpnicfIpxRouteStatPro,
       "hpnicfIpxRouteStatRoutes": hpnicfIpxRouteStatRoutes,
       "hpnicfIpxRouteStatActives": hpnicfIpxRouteStatActives,
       "hpnicfIpxRouteStatAddeds": hpnicfIpxRouteStatAddeds,
       "hpnicfIpxRouteStatDeleteds": hpnicfIpxRouteStatDeleteds,
       "hpnicfIpxRouteStatFreeds": hpnicfIpxRouteStatFreeds,
       "hpnicfIpxSap": hpnicfIpxSap,
       "hpnicfIpxSapMultiplier": hpnicfIpxSapMultiplier,
       "hpnicfIpxSapUpdateTimer": hpnicfIpxSapUpdateTimer,
       "hpnicfIpxSapGnsLoadBalance": hpnicfIpxSapGnsLoadBalance,
       "hpnicfIpxSapMaxResServers": hpnicfIpxSapMaxResServers,
       "hpnicfIpxServiceTable": hpnicfIpxServiceTable,
       "hpnicfIpxServiceEntry": hpnicfIpxServiceEntry,
       "hpnicfIpxServiceIndex": hpnicfIpxServiceIndex,
       "hpnicfIpxServiceName": hpnicfIpxServiceName,
       "hpnicfIpxServiceType": hpnicfIpxServiceType,
       "hpnicfIpxServiceNetId": hpnicfIpxServiceNetId,
       "hpnicfIpxServiceNodeId": hpnicfIpxServiceNodeId,
       "hpnicfIpxServiceSocketNo": hpnicfIpxServiceSocketNo,
       "hpnicfIpxServicePreference": hpnicfIpxServicePreference,
       "hpnicfIpxServiceHops": hpnicfIpxServiceHops,
       "hpnicfIpxServiceRecvIf": hpnicfIpxServiceRecvIf,
       "hpnicfIpxStaticServiceTable": hpnicfIpxStaticServiceTable,
       "hpnicfIpxStaticServiceEntry": hpnicfIpxStaticServiceEntry,
       "hpnicfIpxStaticServiceType": hpnicfIpxStaticServiceType,
       "hpnicfIpxStaticServiceName": hpnicfIpxStaticServiceName,
       "hpnicfIpxStaticServiceNetId": hpnicfIpxStaticServiceNetId,
       "hpnicfIpxStaticServiceNodeId": hpnicfIpxStaticServiceNodeId,
       "hpnicfIpxStatciServiceSocketNo": hpnicfIpxStatciServiceSocketNo,
       "hpnicfIpxStaticServicePreference": hpnicfIpxStaticServicePreference,
       "hpnicfIpxStaticServiceHops": hpnicfIpxStaticServiceHops,
       "hpnicfIpxStaticServiceStatus": hpnicfIpxStaticServiceStatus,
       "hpnicfIpxStaticServiceRowStatus": hpnicfIpxStaticServiceRowStatus,
       "hpnicfIpxStat": hpnicfIpxStat,
       "hpnicfIpxStatGlobal": hpnicfIpxStatGlobal,
       "hpnicfIpxStatTotalReceives": hpnicfIpxStatTotalReceives,
       "hpnicfIpxStatPitchs": hpnicfIpxStatPitchs,
       "hpnicfIpxStatLenErrors": hpnicfIpxStatLenErrors,
       "hpnicfIpxStatFormatErrors": hpnicfIpxStatFormatErrors,
       "hpnicfIpxStatBadHops": hpnicfIpxStatBadHops,
       "hpnicfIpxStatHopsDiscards": hpnicfIpxStatHopsDiscards,
       "hpnicfIpxStatOtherErrors": hpnicfIpxStatOtherErrors,
       "hpnicfIpxStatLocalDests": hpnicfIpxStatLocalDests,
       "hpnicfIpxStatCantDeals": hpnicfIpxStatCantDeals,
       "hpnicfIpxStatForwards": hpnicfIpxStatForwards,
       "hpnicfIpxStatGenerates": hpnicfIpxStatGenerates,
       "hpnicfIpxStatNoRoutes": hpnicfIpxStatNoRoutes,
       "hpnicfIpxStatOutDiscards": hpnicfIpxStatOutDiscards,
       "hpnicfIpxStatRipSends": hpnicfIpxStatRipSends,
       "hpnicfIpxStatRipReceives": hpnicfIpxStatRipReceives,
       "hpnicfIpxStaRipRspSends": hpnicfIpxStaRipRspSends,
       "hpnicfIpxStaRipRspReceives": hpnicfIpxStaRipRspReceives,
       "hpnicfIpxStatRipReqReceives": hpnicfIpxStatRipReqReceives,
       "hpnicfIpxStatRipReqDeals": hpnicfIpxStatRipReqDeals,
       "hpnicfIpxStatRipReqSends": hpnicfIpxStatRipReqSends,
       "hpnicfIpxStatRipPeriUpdates": hpnicfIpxStatRipPeriUpdates,
       "hpnicfIpxStatSapGenReqReceives": hpnicfIpxStatSapGenReqReceives,
       "hpnicfIpxStatSapSpecReqReceives": hpnicfIpxStatSapSpecReqReceives,
       "hpnicfIpxStatSapGnsReqReceives": hpnicfIpxStatSapGnsReqReceives,
       "hpnicfIpxStatSapGenRspSends": hpnicfIpxStatSapGenRspSends,
       "hpnicfIpxStatSapSpecRspSends": hpnicfIpxStatSapSpecRspSends,
       "hpnicfIpxStatSapGnsRspSends": hpnicfIpxStatSapGnsRspSends,
       "hpnicfIpxStatSapPeriUpdates": hpnicfIpxStatSapPeriUpdates,
       "hpnicfIpxStatSapInPktErrors": hpnicfIpxStatSapInPktErrors,
       "hpnicfIpxStatInterface": hpnicfIpxStatInterface,
       "hpnicfIpxIfStatTable": hpnicfIpxIfStatTable,
       "hpnicfIpxIfStatEntry": hpnicfIpxIfStatEntry,
       "hpnicfIpxIfStatIndex": hpnicfIpxIfStatIndex,
       "hpnicfIpxIfStatNetId": hpnicfIpxIfStatNetId,
       "hpnicfIpxIfStatNodeId": hpnicfIpxIfStatNodeId,
       "hpnicfIpxIfStatIpxReceives": hpnicfIpxIfStatIpxReceives,
       "hpnicfIpxIfStatIpxSends": hpnicfIpxIfStatIpxSends,
       "hpnicfIpxIfStatIpxRecvBytes": hpnicfIpxIfStatIpxRecvBytes,
       "hpnicfIpxIfStatIpxSendBytes": hpnicfIpxIfStatIpxSendBytes,
       "hpnicfIpxIfStatRipReceives": hpnicfIpxIfStatRipReceives,
       "hpnicfIpxIfStatRipSends": hpnicfIpxIfStatRipSends,
       "hpnicfIpxIfStatRipDiscards": hpnicfIpxIfStatRipDiscards,
       "hpnicfIpxIfStatRipSpecReqReceives": hpnicfIpxIfStatRipSpecReqReceives,
       "hpnicfIpxIfStatRipSpecRspSends": hpnicfIpxIfStatRipSpecRspSends,
       "hpnicfIpxIfStatRipGenReqReceives": hpnicfIpxIfStatRipGenReqReceives,
       "hpnicfIpxIfStatRipGenRspSends": hpnicfIpxIfStatRipGenRspSends,
       "hpnicfIpxIfStatSapReceives": hpnicfIpxIfStatSapReceives,
       "hpnicfIpxIfStatSapSends": hpnicfIpxIfStatSapSends,
       "hpnicfIpxIfStatSapDiscards": hpnicfIpxIfStatSapDiscards,
       "hpnicfIpxIfStatSapGnsReqReceives": hpnicfIpxIfStatSapGnsReqReceives,
       "hpnicfIpxIfStatSapGnsRspSends": hpnicfIpxIfStatSapGnsRspSends}
)
