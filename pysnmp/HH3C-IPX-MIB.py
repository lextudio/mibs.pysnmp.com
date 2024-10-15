# SNMP MIB module (HH3C-IPX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HH3C-IPX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:53:40 2024
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

(hh3cCommon,) = mibBuilder.importSymbols(
    "HH3C-OID-MIB",
    "hh3cCommon")

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

hh3cIpx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34)
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

_Hh3cIpxConfig_ObjectIdentity = ObjectIdentity
hh3cIpxConfig = _Hh3cIpxConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1)
)


class _Hh3cIpxStatus_Type(EnabledStatus):
    """Custom type hh3cIpxStatus based on EnabledStatus"""


_Hh3cIpxStatus_Object = MibScalar
hh3cIpxStatus = _Hh3cIpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 1),
    _Hh3cIpxStatus_Type()
)
hh3cIpxStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpxStatus.setStatus("current")
_Hh3cIpxIfConfigTable_Object = MibTable
hh3cIpxIfConfigTable = _Hh3cIpxIfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2)
)
if mibBuilder.loadTexts:
    hh3cIpxIfConfigTable.setStatus("current")
_Hh3cIpxIfConfigEntry_Object = MibTableRow
hh3cIpxIfConfigEntry = _Hh3cIpxIfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1)
)
hh3cIpxIfConfigEntry.setIndexNames(
    (0, "HH3C-IPX-MIB", "hh3cIpxIfIndex"),
)
if mibBuilder.loadTexts:
    hh3cIpxIfConfigEntry.setStatus("current")


class _Hh3cIpxIfIndex_Type(Integer32):
    """Custom type hh3cIpxIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIpxIfIndex_Type.__name__ = "Integer32"
_Hh3cIpxIfIndex_Object = MibTableColumn
hh3cIpxIfIndex = _Hh3cIpxIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 1),
    _Hh3cIpxIfIndex_Type()
)
hh3cIpxIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpxIfIndex.setStatus("current")


class _Hh3cIpxIfNetId_Type(OctetString):
    """Custom type hh3cIpxIfNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Hh3cIpxIfNetId_Type.__name__ = "OctetString"
_Hh3cIpxIfNetId_Object = MibTableColumn
hh3cIpxIfNetId = _Hh3cIpxIfNetId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 2),
    _Hh3cIpxIfNetId_Type()
)
hh3cIpxIfNetId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxIfNetId.setStatus("current")


class _Hh3cIpxIfNodeId_Type(OctetString):
    """Custom type hh3cIpxIfNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Hh3cIpxIfNodeId_Type.__name__ = "OctetString"
_Hh3cIpxIfNodeId_Object = MibTableColumn
hh3cIpxIfNodeId = _Hh3cIpxIfNodeId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 3),
    _Hh3cIpxIfNodeId_Type()
)
hh3cIpxIfNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfNodeId.setStatus("current")


class _Hh3cIpxIfSplitHorizon_Type(EnabledStatus):
    """Custom type hh3cIpxIfSplitHorizon based on EnabledStatus"""


_Hh3cIpxIfSplitHorizon_Object = MibTableColumn
hh3cIpxIfSplitHorizon = _Hh3cIpxIfSplitHorizon_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 4),
    _Hh3cIpxIfSplitHorizon_Type()
)
hh3cIpxIfSplitHorizon.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxIfSplitHorizon.setStatus("current")


class _Hh3cIPxIfTick_Type(Integer32):
    """Custom type hh3cIPxIfTick based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30000),
    )


_Hh3cIPxIfTick_Type.__name__ = "Integer32"
_Hh3cIPxIfTick_Object = MibTableColumn
hh3cIPxIfTick = _Hh3cIPxIfTick_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 5),
    _Hh3cIPxIfTick_Type()
)
hh3cIPxIfTick.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIPxIfTick.setStatus("current")


class _Hh3cIpxIfUpdateChangeOnly_Type(EnabledStatus):
    """Custom type hh3cIpxIfUpdateChangeOnly based on EnabledStatus"""


_Hh3cIpxIfUpdateChangeOnly_Object = MibTableColumn
hh3cIpxIfUpdateChangeOnly = _Hh3cIpxIfUpdateChangeOnly_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 6),
    _Hh3cIpxIfUpdateChangeOnly_Type()
)
hh3cIpxIfUpdateChangeOnly.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxIfUpdateChangeOnly.setStatus("current")


class _Hh3cIpxIfRipMtu_Type(Integer32):
    """Custom type hh3cIpxIfRipMtu based on Integer32"""
    defaultValue = 432

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(432, 1500),
    )


_Hh3cIpxIfRipMtu_Type.__name__ = "Integer32"
_Hh3cIpxIfRipMtu_Object = MibTableColumn
hh3cIpxIfRipMtu = _Hh3cIpxIfRipMtu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 7),
    _Hh3cIpxIfRipMtu_Type()
)
hh3cIpxIfRipMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxIfRipMtu.setStatus("current")


class _Hh3cIpxIfEncapsuleType_Type(Integer32):
    """Custom type hh3cIpxIfEncapsuleType based on Integer32"""
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


_Hh3cIpxIfEncapsuleType_Type.__name__ = "Integer32"
_Hh3cIpxIfEncapsuleType_Object = MibTableColumn
hh3cIpxIfEncapsuleType = _Hh3cIpxIfEncapsuleType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 8),
    _Hh3cIpxIfEncapsuleType_Type()
)
hh3cIpxIfEncapsuleType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxIfEncapsuleType.setStatus("current")


class _Hh3cIpxIfNetbiosPropagation_Type(EnabledStatus):
    """Custom type hh3cIpxIfNetbiosPropagation based on EnabledStatus"""


_Hh3cIpxIfNetbiosPropagation_Object = MibTableColumn
hh3cIpxIfNetbiosPropagation = _Hh3cIpxIfNetbiosPropagation_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 9),
    _Hh3cIpxIfNetbiosPropagation_Type()
)
hh3cIpxIfNetbiosPropagation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxIfNetbiosPropagation.setStatus("current")


class _Hh3cIpxIfSapStatus_Type(EnabledStatus):
    """Custom type hh3cIpxIfSapStatus based on EnabledStatus"""


_Hh3cIpxIfSapStatus_Object = MibTableColumn
hh3cIpxIfSapStatus = _Hh3cIpxIfSapStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 10),
    _Hh3cIpxIfSapStatus_Type()
)
hh3cIpxIfSapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxIfSapStatus.setStatus("current")


class _Hh3cIpxIfSapMtu_Type(Integer32):
    """Custom type hh3cIpxIfSapMtu based on Integer32"""
    defaultValue = 480

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(480, 1500),
    )


_Hh3cIpxIfSapMtu_Type.__name__ = "Integer32"
_Hh3cIpxIfSapMtu_Object = MibTableColumn
hh3cIpxIfSapMtu = _Hh3cIpxIfSapMtu_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 11),
    _Hh3cIpxIfSapMtu_Type()
)
hh3cIpxIfSapMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxIfSapMtu.setStatus("current")


class _Hh3cIpxIfGnsReply_Type(EnabledStatus):
    """Custom type hh3cIpxIfGnsReply based on EnabledStatus"""


_Hh3cIpxIfGnsReply_Object = MibTableColumn
hh3cIpxIfGnsReply = _Hh3cIpxIfGnsReply_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 12),
    _Hh3cIpxIfGnsReply_Type()
)
hh3cIpxIfGnsReply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxIfGnsReply.setStatus("current")
_Hh3cIpxIfRowStatus_Type = RowStatus
_Hh3cIpxIfRowStatus_Object = MibTableColumn
hh3cIpxIfRowStatus = _Hh3cIpxIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 1, 2, 1, 13),
    _Hh3cIpxIfRowStatus_Type()
)
hh3cIpxIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxIfRowStatus.setStatus("current")
_Hh3cIpxRip_ObjectIdentity = ObjectIdentity
hh3cIpxRip = _Hh3cIpxRip_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2)
)


class _Hh3cIpxRouteMultiplier_Type(Integer32):
    """Custom type hh3cIpxRouteMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Hh3cIpxRouteMultiplier_Type.__name__ = "Integer32"
_Hh3cIpxRouteMultiplier_Object = MibScalar
hh3cIpxRouteMultiplier = _Hh3cIpxRouteMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 1),
    _Hh3cIpxRouteMultiplier_Type()
)
hh3cIpxRouteMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpxRouteMultiplier.setStatus("current")


class _Hh3cIpxRouteUpdateTimer_Type(Integer32):
    """Custom type hh3cIpxRouteUpdateTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60000),
    )


_Hh3cIpxRouteUpdateTimer_Type.__name__ = "Integer32"
_Hh3cIpxRouteUpdateTimer_Object = MibScalar
hh3cIpxRouteUpdateTimer = _Hh3cIpxRouteUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 2),
    _Hh3cIpxRouteUpdateTimer_Type()
)
hh3cIpxRouteUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpxRouteUpdateTimer.setStatus("current")


class _Hh3cIpxRouteImpRouteStatic_Type(EnabledStatus):
    """Custom type hh3cIpxRouteImpRouteStatic based on EnabledStatus"""


_Hh3cIpxRouteImpRouteStatic_Object = MibScalar
hh3cIpxRouteImpRouteStatic = _Hh3cIpxRouteImpRouteStatic_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 3),
    _Hh3cIpxRouteImpRouteStatic_Type()
)
hh3cIpxRouteImpRouteStatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpxRouteImpRouteStatic.setStatus("current")


class _Hh3cIpxRouteLoadBalancePaths_Type(Integer32):
    """Custom type hh3cIpxRouteLoadBalancePaths based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_Hh3cIpxRouteLoadBalancePaths_Type.__name__ = "Integer32"
_Hh3cIpxRouteLoadBalancePaths_Object = MibScalar
hh3cIpxRouteLoadBalancePaths = _Hh3cIpxRouteLoadBalancePaths_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 4),
    _Hh3cIpxRouteLoadBalancePaths_Type()
)
hh3cIpxRouteLoadBalancePaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpxRouteLoadBalancePaths.setStatus("current")


class _Hh3cIpxRouteMaxResPaths_Type(Integer32):
    """Custom type hh3cIpxRouteMaxResPaths based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cIpxRouteMaxResPaths_Type.__name__ = "Integer32"
_Hh3cIpxRouteMaxResPaths_Object = MibScalar
hh3cIpxRouteMaxResPaths = _Hh3cIpxRouteMaxResPaths_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 5),
    _Hh3cIpxRouteMaxResPaths_Type()
)
hh3cIpxRouteMaxResPaths.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpxRouteMaxResPaths.setStatus("current")
_Hh3cIpxRouteTable_Object = MibTable
hh3cIpxRouteTable = _Hh3cIpxRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6)
)
if mibBuilder.loadTexts:
    hh3cIpxRouteTable.setStatus("current")
_Hh3cIpxRouteEntry_Object = MibTableRow
hh3cIpxRouteEntry = _Hh3cIpxRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1)
)
hh3cIpxRouteEntry.setIndexNames(
    (0, "HH3C-IPX-MIB", "hh3cIpxRouteIndex"),
)
if mibBuilder.loadTexts:
    hh3cIpxRouteEntry.setStatus("current")
_Hh3cIpxRouteIndex_Type = Integer32
_Hh3cIpxRouteIndex_Object = MibTableColumn
hh3cIpxRouteIndex = _Hh3cIpxRouteIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 1),
    _Hh3cIpxRouteIndex_Type()
)
hh3cIpxRouteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpxRouteIndex.setStatus("current")


class _Hh3cIpxRouteDestNetId_Type(OctetString):
    """Custom type hh3cIpxRouteDestNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Hh3cIpxRouteDestNetId_Type.__name__ = "OctetString"
_Hh3cIpxRouteDestNetId_Object = MibTableColumn
hh3cIpxRouteDestNetId = _Hh3cIpxRouteDestNetId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 2),
    _Hh3cIpxRouteDestNetId_Type()
)
hh3cIpxRouteDestNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteDestNetId.setStatus("current")


class _Hh3cIpxRouteNextHop_Type(OctetString):
    """Custom type hh3cIpxRouteNextHop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Hh3cIpxRouteNextHop_Type.__name__ = "OctetString"
_Hh3cIpxRouteNextHop_Object = MibTableColumn
hh3cIpxRouteNextHop = _Hh3cIpxRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 3),
    _Hh3cIpxRouteNextHop_Type()
)
hh3cIpxRouteNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteNextHop.setStatus("current")


class _Hh3cIpxRoutePro_Type(Integer32):
    """Custom type hh3cIpxRoutePro based on Integer32"""
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


_Hh3cIpxRoutePro_Type.__name__ = "Integer32"
_Hh3cIpxRoutePro_Object = MibTableColumn
hh3cIpxRoutePro = _Hh3cIpxRoutePro_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 4),
    _Hh3cIpxRoutePro_Type()
)
hh3cIpxRoutePro.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRoutePro.setStatus("current")
_Hh3cIpxRoutePre_Type = Integer32
_Hh3cIpxRoutePre_Object = MibTableColumn
hh3cIpxRoutePre = _Hh3cIpxRoutePre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 5),
    _Hh3cIpxRoutePre_Type()
)
hh3cIpxRoutePre.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRoutePre.setStatus("current")


class _Hh3cIpxRouteTicks_Type(Integer32):
    """Custom type hh3cIpxRouteTicks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_Hh3cIpxRouteTicks_Type.__name__ = "Integer32"
_Hh3cIpxRouteTicks_Object = MibTableColumn
hh3cIpxRouteTicks = _Hh3cIpxRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 6),
    _Hh3cIpxRouteTicks_Type()
)
hh3cIpxRouteTicks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteTicks.setStatus("current")


class _Hh3cIpxRouteHops_Type(Integer32):
    """Custom type hh3cIpxRouteHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cIpxRouteHops_Type.__name__ = "Integer32"
_Hh3cIpxRouteHops_Object = MibTableColumn
hh3cIpxRouteHops = _Hh3cIpxRouteHops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 7),
    _Hh3cIpxRouteHops_Type()
)
hh3cIpxRouteHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteHops.setStatus("current")


class _Hh3cIpxRouteTime_Type(Integer32):
    """Custom type hh3cIpxRouteTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000000),
    )


_Hh3cIpxRouteTime_Type.__name__ = "Integer32"
_Hh3cIpxRouteTime_Object = MibTableColumn
hh3cIpxRouteTime = _Hh3cIpxRouteTime_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 8),
    _Hh3cIpxRouteTime_Type()
)
hh3cIpxRouteTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteTime.setStatus("current")


class _Hh3cIpxRouteOutInterface_Type(OctetString):
    """Custom type hh3cIpxRouteOutInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_Hh3cIpxRouteOutInterface_Type.__name__ = "OctetString"
_Hh3cIpxRouteOutInterface_Object = MibTableColumn
hh3cIpxRouteOutInterface = _Hh3cIpxRouteOutInterface_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 6, 1, 9),
    _Hh3cIpxRouteOutInterface_Type()
)
hh3cIpxRouteOutInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteOutInterface.setStatus("current")
_Hh3cIpxStaticRouteTable_Object = MibTable
hh3cIpxStaticRouteTable = _Hh3cIpxStaticRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7)
)
if mibBuilder.loadTexts:
    hh3cIpxStaticRouteTable.setStatus("current")
_Hh3cIpxStaticRouteEntry_Object = MibTableRow
hh3cIpxStaticRouteEntry = _Hh3cIpxStaticRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1)
)
hh3cIpxStaticRouteEntry.setIndexNames(
    (0, "HH3C-IPX-MIB", "hh3cIpxStaticRouteDestNetId"),
    (0, "HH3C-IPX-MIB", "hh3cIpxStaticRouteNextHop"),
)
if mibBuilder.loadTexts:
    hh3cIpxStaticRouteEntry.setStatus("current")


class _Hh3cIpxStaticRouteDestNetId_Type(OctetString):
    """Custom type hh3cIpxStaticRouteDestNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Hh3cIpxStaticRouteDestNetId_Type.__name__ = "OctetString"
_Hh3cIpxStaticRouteDestNetId_Object = MibTableColumn
hh3cIpxStaticRouteDestNetId = _Hh3cIpxStaticRouteDestNetId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 1),
    _Hh3cIpxStaticRouteDestNetId_Type()
)
hh3cIpxStaticRouteDestNetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpxStaticRouteDestNetId.setStatus("current")


class _Hh3cIpxStaticRouteNextHop_Type(OctetString):
    """Custom type hh3cIpxStaticRouteNextHop based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )


_Hh3cIpxStaticRouteNextHop_Type.__name__ = "OctetString"
_Hh3cIpxStaticRouteNextHop_Object = MibTableColumn
hh3cIpxStaticRouteNextHop = _Hh3cIpxStaticRouteNextHop_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 2),
    _Hh3cIpxStaticRouteNextHop_Type()
)
hh3cIpxStaticRouteNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpxStaticRouteNextHop.setStatus("current")


class _Hh3cIpxStaticRoutePre_Type(Integer32):
    """Custom type hh3cIpxStaticRoutePre based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cIpxStaticRoutePre_Type.__name__ = "Integer32"
_Hh3cIpxStaticRoutePre_Object = MibTableColumn
hh3cIpxStaticRoutePre = _Hh3cIpxStaticRoutePre_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 3),
    _Hh3cIpxStaticRoutePre_Type()
)
hh3cIpxStaticRoutePre.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticRoutePre.setStatus("current")


class _Hh3cIpxStaticRouteOutIf_Type(OctetString):
    """Custom type hh3cIpxStaticRouteOutIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_Hh3cIpxStaticRouteOutIf_Type.__name__ = "OctetString"
_Hh3cIpxStaticRouteOutIf_Object = MibTableColumn
hh3cIpxStaticRouteOutIf = _Hh3cIpxStaticRouteOutIf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 4),
    _Hh3cIpxStaticRouteOutIf_Type()
)
hh3cIpxStaticRouteOutIf.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticRouteOutIf.setStatus("current")


class _Hh3cIpxStaticRouteTicks_Type(Integer32):
    """Custom type hh3cIpxStaticRouteTicks based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65534),
    )


_Hh3cIpxStaticRouteTicks_Type.__name__ = "Integer32"
_Hh3cIpxStaticRouteTicks_Object = MibTableColumn
hh3cIpxStaticRouteTicks = _Hh3cIpxStaticRouteTicks_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 5),
    _Hh3cIpxStaticRouteTicks_Type()
)
hh3cIpxStaticRouteTicks.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticRouteTicks.setStatus("current")


class _Hh3cIpxStaticRouteHops_Type(Integer32):
    """Custom type hh3cIpxStaticRouteHops based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hh3cIpxStaticRouteHops_Type.__name__ = "Integer32"
_Hh3cIpxStaticRouteHops_Object = MibTableColumn
hh3cIpxStaticRouteHops = _Hh3cIpxStaticRouteHops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 6),
    _Hh3cIpxStaticRouteHops_Type()
)
hh3cIpxStaticRouteHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticRouteHops.setStatus("current")


class _Hh3cIpxStaticRouteStatus_Type(Integer32):
    """Custom type hh3cIpxStaticRouteStatus based on Integer32"""
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


_Hh3cIpxStaticRouteStatus_Type.__name__ = "Integer32"
_Hh3cIpxStaticRouteStatus_Object = MibTableColumn
hh3cIpxStaticRouteStatus = _Hh3cIpxStaticRouteStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 7),
    _Hh3cIpxStaticRouteStatus_Type()
)
hh3cIpxStaticRouteStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticRouteStatus.setStatus("current")
_Hh3cIpxStaticRouteRowStatus_Type = RowStatus
_Hh3cIpxStaticRouteRowStatus_Object = MibTableColumn
hh3cIpxStaticRouteRowStatus = _Hh3cIpxStaticRouteRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 7, 1, 8),
    _Hh3cIpxStaticRouteRowStatus_Type()
)
hh3cIpxStaticRouteRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticRouteRowStatus.setStatus("current")
_Hh3cIpxRouteStatTable_Object = MibTable
hh3cIpxRouteStatTable = _Hh3cIpxRouteStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8)
)
if mibBuilder.loadTexts:
    hh3cIpxRouteStatTable.setStatus("current")
_Hh3cIpxRouteStatEntry_Object = MibTableRow
hh3cIpxRouteStatEntry = _Hh3cIpxRouteStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1)
)
hh3cIpxRouteStatEntry.setIndexNames(
    (0, "HH3C-IPX-MIB", "hh3cIpxRouteStatPro"),
)
if mibBuilder.loadTexts:
    hh3cIpxRouteStatEntry.setStatus("current")


class _Hh3cIpxRouteStatPro_Type(Integer32):
    """Custom type hh3cIpxRouteStatPro based on Integer32"""
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


_Hh3cIpxRouteStatPro_Type.__name__ = "Integer32"
_Hh3cIpxRouteStatPro_Object = MibTableColumn
hh3cIpxRouteStatPro = _Hh3cIpxRouteStatPro_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 1),
    _Hh3cIpxRouteStatPro_Type()
)
hh3cIpxRouteStatPro.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpxRouteStatPro.setStatus("current")
_Hh3cIpxRouteStatRoutes_Type = Counter32
_Hh3cIpxRouteStatRoutes_Object = MibTableColumn
hh3cIpxRouteStatRoutes = _Hh3cIpxRouteStatRoutes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 2),
    _Hh3cIpxRouteStatRoutes_Type()
)
hh3cIpxRouteStatRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteStatRoutes.setStatus("current")
_Hh3cIpxRouteStatActives_Type = Counter32
_Hh3cIpxRouteStatActives_Object = MibTableColumn
hh3cIpxRouteStatActives = _Hh3cIpxRouteStatActives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 3),
    _Hh3cIpxRouteStatActives_Type()
)
hh3cIpxRouteStatActives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteStatActives.setStatus("current")
_Hh3cIpxRouteStatAddeds_Type = Counter32
_Hh3cIpxRouteStatAddeds_Object = MibTableColumn
hh3cIpxRouteStatAddeds = _Hh3cIpxRouteStatAddeds_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 4),
    _Hh3cIpxRouteStatAddeds_Type()
)
hh3cIpxRouteStatAddeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteStatAddeds.setStatus("current")
_Hh3cIpxRouteStatDeleteds_Type = Counter32
_Hh3cIpxRouteStatDeleteds_Object = MibTableColumn
hh3cIpxRouteStatDeleteds = _Hh3cIpxRouteStatDeleteds_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 5),
    _Hh3cIpxRouteStatDeleteds_Type()
)
hh3cIpxRouteStatDeleteds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteStatDeleteds.setStatus("current")
_Hh3cIpxRouteStatFreeds_Type = Counter32
_Hh3cIpxRouteStatFreeds_Object = MibTableColumn
hh3cIpxRouteStatFreeds = _Hh3cIpxRouteStatFreeds_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 2, 8, 1, 6),
    _Hh3cIpxRouteStatFreeds_Type()
)
hh3cIpxRouteStatFreeds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxRouteStatFreeds.setStatus("current")
_Hh3cIpxSap_ObjectIdentity = ObjectIdentity
hh3cIpxSap = _Hh3cIpxSap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3)
)


class _Hh3cIpxSapMultiplier_Type(Integer32):
    """Custom type hh3cIpxSapMultiplier based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_Hh3cIpxSapMultiplier_Type.__name__ = "Integer32"
_Hh3cIpxSapMultiplier_Object = MibScalar
hh3cIpxSapMultiplier = _Hh3cIpxSapMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 1),
    _Hh3cIpxSapMultiplier_Type()
)
hh3cIpxSapMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpxSapMultiplier.setStatus("current")


class _Hh3cIpxSapUpdateTimer_Type(Integer32):
    """Custom type hh3cIpxSapUpdateTimer based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 60000),
    )


_Hh3cIpxSapUpdateTimer_Type.__name__ = "Integer32"
_Hh3cIpxSapUpdateTimer_Object = MibScalar
hh3cIpxSapUpdateTimer = _Hh3cIpxSapUpdateTimer_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 2),
    _Hh3cIpxSapUpdateTimer_Type()
)
hh3cIpxSapUpdateTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpxSapUpdateTimer.setStatus("current")


class _Hh3cIpxSapGnsLoadBalance_Type(EnabledStatus):
    """Custom type hh3cIpxSapGnsLoadBalance based on EnabledStatus"""


_Hh3cIpxSapGnsLoadBalance_Object = MibScalar
hh3cIpxSapGnsLoadBalance = _Hh3cIpxSapGnsLoadBalance_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 3),
    _Hh3cIpxSapGnsLoadBalance_Type()
)
hh3cIpxSapGnsLoadBalance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpxSapGnsLoadBalance.setStatus("current")


class _Hh3cIpxSapMaxResServers_Type(Integer32):
    """Custom type hh3cIpxSapMaxResServers based on Integer32"""
    defaultValue = 2048

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )


_Hh3cIpxSapMaxResServers_Type.__name__ = "Integer32"
_Hh3cIpxSapMaxResServers_Object = MibScalar
hh3cIpxSapMaxResServers = _Hh3cIpxSapMaxResServers_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 4),
    _Hh3cIpxSapMaxResServers_Type()
)
hh3cIpxSapMaxResServers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hh3cIpxSapMaxResServers.setStatus("current")
_Hh3cIpxServiceTable_Object = MibTable
hh3cIpxServiceTable = _Hh3cIpxServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5)
)
if mibBuilder.loadTexts:
    hh3cIpxServiceTable.setStatus("current")
_Hh3cIpxServiceEntry_Object = MibTableRow
hh3cIpxServiceEntry = _Hh3cIpxServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1)
)
hh3cIpxServiceEntry.setIndexNames(
    (0, "HH3C-IPX-MIB", "hh3cIpxServiceIndex"),
)
if mibBuilder.loadTexts:
    hh3cIpxServiceEntry.setStatus("current")
_Hh3cIpxServiceIndex_Type = Integer32
_Hh3cIpxServiceIndex_Object = MibTableColumn
hh3cIpxServiceIndex = _Hh3cIpxServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 1),
    _Hh3cIpxServiceIndex_Type()
)
hh3cIpxServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpxServiceIndex.setStatus("current")


class _Hh3cIpxServiceName_Type(OctetString):
    """Custom type hh3cIpxServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_Hh3cIpxServiceName_Type.__name__ = "OctetString"
_Hh3cIpxServiceName_Object = MibTableColumn
hh3cIpxServiceName = _Hh3cIpxServiceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 2),
    _Hh3cIpxServiceName_Type()
)
hh3cIpxServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxServiceName.setStatus("current")


class _Hh3cIpxServiceType_Type(OctetString):
    """Custom type hh3cIpxServiceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hh3cIpxServiceType_Type.__name__ = "OctetString"
_Hh3cIpxServiceType_Object = MibTableColumn
hh3cIpxServiceType = _Hh3cIpxServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 3),
    _Hh3cIpxServiceType_Type()
)
hh3cIpxServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxServiceType.setStatus("current")


class _Hh3cIpxServiceNetId_Type(OctetString):
    """Custom type hh3cIpxServiceNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Hh3cIpxServiceNetId_Type.__name__ = "OctetString"
_Hh3cIpxServiceNetId_Object = MibTableColumn
hh3cIpxServiceNetId = _Hh3cIpxServiceNetId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 4),
    _Hh3cIpxServiceNetId_Type()
)
hh3cIpxServiceNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxServiceNetId.setStatus("current")


class _Hh3cIpxServiceNodeId_Type(OctetString):
    """Custom type hh3cIpxServiceNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Hh3cIpxServiceNodeId_Type.__name__ = "OctetString"
_Hh3cIpxServiceNodeId_Object = MibTableColumn
hh3cIpxServiceNodeId = _Hh3cIpxServiceNodeId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 5),
    _Hh3cIpxServiceNodeId_Type()
)
hh3cIpxServiceNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxServiceNodeId.setStatus("current")


class _Hh3cIpxServiceSocketNo_Type(OctetString):
    """Custom type hh3cIpxServiceSocketNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hh3cIpxServiceSocketNo_Type.__name__ = "OctetString"
_Hh3cIpxServiceSocketNo_Object = MibTableColumn
hh3cIpxServiceSocketNo = _Hh3cIpxServiceSocketNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 6),
    _Hh3cIpxServiceSocketNo_Type()
)
hh3cIpxServiceSocketNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxServiceSocketNo.setStatus("current")
_Hh3cIpxServicePreference_Type = Integer32
_Hh3cIpxServicePreference_Object = MibTableColumn
hh3cIpxServicePreference = _Hh3cIpxServicePreference_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 7),
    _Hh3cIpxServicePreference_Type()
)
hh3cIpxServicePreference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxServicePreference.setStatus("current")


class _Hh3cIpxServiceHops_Type(Integer32):
    """Custom type hh3cIpxServiceHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_Hh3cIpxServiceHops_Type.__name__ = "Integer32"
_Hh3cIpxServiceHops_Object = MibTableColumn
hh3cIpxServiceHops = _Hh3cIpxServiceHops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 8),
    _Hh3cIpxServiceHops_Type()
)
hh3cIpxServiceHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxServiceHops.setStatus("current")


class _Hh3cIpxServiceRecvIf_Type(OctetString):
    """Custom type hh3cIpxServiceRecvIf based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_Hh3cIpxServiceRecvIf_Type.__name__ = "OctetString"
_Hh3cIpxServiceRecvIf_Object = MibTableColumn
hh3cIpxServiceRecvIf = _Hh3cIpxServiceRecvIf_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 5, 1, 9),
    _Hh3cIpxServiceRecvIf_Type()
)
hh3cIpxServiceRecvIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxServiceRecvIf.setStatus("current")
_Hh3cIpxStaticServiceTable_Object = MibTable
hh3cIpxStaticServiceTable = _Hh3cIpxStaticServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6)
)
if mibBuilder.loadTexts:
    hh3cIpxStaticServiceTable.setStatus("current")
_Hh3cIpxStaticServiceEntry_Object = MibTableRow
hh3cIpxStaticServiceEntry = _Hh3cIpxStaticServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1)
)
hh3cIpxStaticServiceEntry.setIndexNames(
    (0, "HH3C-IPX-MIB", "hh3cIpxStaticServiceType"),
    (0, "HH3C-IPX-MIB", "hh3cIpxStaticServiceName"),
    (0, "HH3C-IPX-MIB", "hh3cIpxStaticServiceNetId"),
)
if mibBuilder.loadTexts:
    hh3cIpxStaticServiceEntry.setStatus("current")


class _Hh3cIpxStaticServiceType_Type(OctetString):
    """Custom type hh3cIpxStaticServiceType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hh3cIpxStaticServiceType_Type.__name__ = "OctetString"
_Hh3cIpxStaticServiceType_Object = MibTableColumn
hh3cIpxStaticServiceType = _Hh3cIpxStaticServiceType_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 1),
    _Hh3cIpxStaticServiceType_Type()
)
hh3cIpxStaticServiceType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpxStaticServiceType.setStatus("current")


class _Hh3cIpxStaticServiceName_Type(OctetString):
    """Custom type hh3cIpxStaticServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 47),
    )


_Hh3cIpxStaticServiceName_Type.__name__ = "OctetString"
_Hh3cIpxStaticServiceName_Object = MibTableColumn
hh3cIpxStaticServiceName = _Hh3cIpxStaticServiceName_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 2),
    _Hh3cIpxStaticServiceName_Type()
)
hh3cIpxStaticServiceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpxStaticServiceName.setStatus("current")


class _Hh3cIpxStaticServiceNetId_Type(OctetString):
    """Custom type hh3cIpxStaticServiceNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Hh3cIpxStaticServiceNetId_Type.__name__ = "OctetString"
_Hh3cIpxStaticServiceNetId_Object = MibTableColumn
hh3cIpxStaticServiceNetId = _Hh3cIpxStaticServiceNetId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 3),
    _Hh3cIpxStaticServiceNetId_Type()
)
hh3cIpxStaticServiceNetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpxStaticServiceNetId.setStatus("current")


class _Hh3cIpxStaticServiceNodeId_Type(OctetString):
    """Custom type hh3cIpxStaticServiceNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Hh3cIpxStaticServiceNodeId_Type.__name__ = "OctetString"
_Hh3cIpxStaticServiceNodeId_Object = MibTableColumn
hh3cIpxStaticServiceNodeId = _Hh3cIpxStaticServiceNodeId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 4),
    _Hh3cIpxStaticServiceNodeId_Type()
)
hh3cIpxStaticServiceNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticServiceNodeId.setStatus("current")


class _Hh3cIpxStatciServiceSocketNo_Type(OctetString):
    """Custom type hh3cIpxStatciServiceSocketNo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_Hh3cIpxStatciServiceSocketNo_Type.__name__ = "OctetString"
_Hh3cIpxStatciServiceSocketNo_Object = MibTableColumn
hh3cIpxStatciServiceSocketNo = _Hh3cIpxStatciServiceSocketNo_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 5),
    _Hh3cIpxStatciServiceSocketNo_Type()
)
hh3cIpxStatciServiceSocketNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStatciServiceSocketNo.setStatus("current")


class _Hh3cIpxStaticServicePreference_Type(Integer32):
    """Custom type hh3cIpxStaticServicePreference based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_Hh3cIpxStaticServicePreference_Type.__name__ = "Integer32"
_Hh3cIpxStaticServicePreference_Object = MibTableColumn
hh3cIpxStaticServicePreference = _Hh3cIpxStaticServicePreference_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 6),
    _Hh3cIpxStaticServicePreference_Type()
)
hh3cIpxStaticServicePreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticServicePreference.setStatus("current")


class _Hh3cIpxStaticServiceHops_Type(Integer32):
    """Custom type hh3cIpxStaticServiceHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_Hh3cIpxStaticServiceHops_Type.__name__ = "Integer32"
_Hh3cIpxStaticServiceHops_Object = MibTableColumn
hh3cIpxStaticServiceHops = _Hh3cIpxStaticServiceHops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 7),
    _Hh3cIpxStaticServiceHops_Type()
)
hh3cIpxStaticServiceHops.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticServiceHops.setStatus("current")


class _Hh3cIpxStaticServiceStatus_Type(Integer32):
    """Custom type hh3cIpxStaticServiceStatus based on Integer32"""
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


_Hh3cIpxStaticServiceStatus_Type.__name__ = "Integer32"
_Hh3cIpxStaticServiceStatus_Object = MibTableColumn
hh3cIpxStaticServiceStatus = _Hh3cIpxStaticServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 8),
    _Hh3cIpxStaticServiceStatus_Type()
)
hh3cIpxStaticServiceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticServiceStatus.setStatus("current")
_Hh3cIpxStaticServiceRowStatus_Type = RowStatus
_Hh3cIpxStaticServiceRowStatus_Object = MibTableColumn
hh3cIpxStaticServiceRowStatus = _Hh3cIpxStaticServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 3, 6, 1, 9),
    _Hh3cIpxStaticServiceRowStatus_Type()
)
hh3cIpxStaticServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hh3cIpxStaticServiceRowStatus.setStatus("current")
_Hh3cIpxStat_ObjectIdentity = ObjectIdentity
hh3cIpxStat = _Hh3cIpxStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4)
)
_Hh3cIpxStatGlobal_ObjectIdentity = ObjectIdentity
hh3cIpxStatGlobal = _Hh3cIpxStatGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1)
)
_Hh3cIpxStatTotalReceives_Type = Counter32
_Hh3cIpxStatTotalReceives_Object = MibScalar
hh3cIpxStatTotalReceives = _Hh3cIpxStatTotalReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 1),
    _Hh3cIpxStatTotalReceives_Type()
)
hh3cIpxStatTotalReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatTotalReceives.setStatus("current")
_Hh3cIpxStatPitchs_Type = Counter32
_Hh3cIpxStatPitchs_Object = MibScalar
hh3cIpxStatPitchs = _Hh3cIpxStatPitchs_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 2),
    _Hh3cIpxStatPitchs_Type()
)
hh3cIpxStatPitchs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatPitchs.setStatus("current")
_Hh3cIpxStatLenErrors_Type = Counter32
_Hh3cIpxStatLenErrors_Object = MibScalar
hh3cIpxStatLenErrors = _Hh3cIpxStatLenErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 3),
    _Hh3cIpxStatLenErrors_Type()
)
hh3cIpxStatLenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatLenErrors.setStatus("current")
_Hh3cIpxStatFormatErrors_Type = Counter32
_Hh3cIpxStatFormatErrors_Object = MibScalar
hh3cIpxStatFormatErrors = _Hh3cIpxStatFormatErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 4),
    _Hh3cIpxStatFormatErrors_Type()
)
hh3cIpxStatFormatErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatFormatErrors.setStatus("current")
_Hh3cIpxStatBadHops_Type = Counter32
_Hh3cIpxStatBadHops_Object = MibScalar
hh3cIpxStatBadHops = _Hh3cIpxStatBadHops_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 5),
    _Hh3cIpxStatBadHops_Type()
)
hh3cIpxStatBadHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatBadHops.setStatus("current")
_Hh3cIpxStatHopsDiscards_Type = Counter32
_Hh3cIpxStatHopsDiscards_Object = MibScalar
hh3cIpxStatHopsDiscards = _Hh3cIpxStatHopsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 6),
    _Hh3cIpxStatHopsDiscards_Type()
)
hh3cIpxStatHopsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatHopsDiscards.setStatus("current")
_Hh3cIpxStatOtherErrors_Type = Counter32
_Hh3cIpxStatOtherErrors_Object = MibScalar
hh3cIpxStatOtherErrors = _Hh3cIpxStatOtherErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 7),
    _Hh3cIpxStatOtherErrors_Type()
)
hh3cIpxStatOtherErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatOtherErrors.setStatus("current")
_Hh3cIpxStatLocalDests_Type = Counter32
_Hh3cIpxStatLocalDests_Object = MibScalar
hh3cIpxStatLocalDests = _Hh3cIpxStatLocalDests_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 8),
    _Hh3cIpxStatLocalDests_Type()
)
hh3cIpxStatLocalDests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatLocalDests.setStatus("current")
_Hh3cIpxStatCantDeals_Type = Counter32
_Hh3cIpxStatCantDeals_Object = MibScalar
hh3cIpxStatCantDeals = _Hh3cIpxStatCantDeals_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 9),
    _Hh3cIpxStatCantDeals_Type()
)
hh3cIpxStatCantDeals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatCantDeals.setStatus("current")
_Hh3cIpxStatForwards_Type = Counter32
_Hh3cIpxStatForwards_Object = MibScalar
hh3cIpxStatForwards = _Hh3cIpxStatForwards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 10),
    _Hh3cIpxStatForwards_Type()
)
hh3cIpxStatForwards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatForwards.setStatus("current")
_Hh3cIpxStatGenerates_Type = Counter32
_Hh3cIpxStatGenerates_Object = MibScalar
hh3cIpxStatGenerates = _Hh3cIpxStatGenerates_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 11),
    _Hh3cIpxStatGenerates_Type()
)
hh3cIpxStatGenerates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatGenerates.setStatus("current")
_Hh3cIpxStatNoRoutes_Type = Counter32
_Hh3cIpxStatNoRoutes_Object = MibScalar
hh3cIpxStatNoRoutes = _Hh3cIpxStatNoRoutes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 12),
    _Hh3cIpxStatNoRoutes_Type()
)
hh3cIpxStatNoRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatNoRoutes.setStatus("current")
_Hh3cIpxStatOutDiscards_Type = Counter32
_Hh3cIpxStatOutDiscards_Object = MibScalar
hh3cIpxStatOutDiscards = _Hh3cIpxStatOutDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 13),
    _Hh3cIpxStatOutDiscards_Type()
)
hh3cIpxStatOutDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatOutDiscards.setStatus("current")
_Hh3cIpxStatRipSends_Type = Counter32
_Hh3cIpxStatRipSends_Object = MibScalar
hh3cIpxStatRipSends = _Hh3cIpxStatRipSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 14),
    _Hh3cIpxStatRipSends_Type()
)
hh3cIpxStatRipSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatRipSends.setStatus("current")
_Hh3cIpxStatRipReceives_Type = Counter32
_Hh3cIpxStatRipReceives_Object = MibScalar
hh3cIpxStatRipReceives = _Hh3cIpxStatRipReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 15),
    _Hh3cIpxStatRipReceives_Type()
)
hh3cIpxStatRipReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatRipReceives.setStatus("current")
_Hh3cIpxStaRipRspSends_Type = Counter32
_Hh3cIpxStaRipRspSends_Object = MibScalar
hh3cIpxStaRipRspSends = _Hh3cIpxStaRipRspSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 16),
    _Hh3cIpxStaRipRspSends_Type()
)
hh3cIpxStaRipRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStaRipRspSends.setStatus("current")
_Hh3cIpxStaRipRspReceives_Type = Counter32
_Hh3cIpxStaRipRspReceives_Object = MibScalar
hh3cIpxStaRipRspReceives = _Hh3cIpxStaRipRspReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 17),
    _Hh3cIpxStaRipRspReceives_Type()
)
hh3cIpxStaRipRspReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStaRipRspReceives.setStatus("current")
_Hh3cIpxStatRipReqReceives_Type = Counter32
_Hh3cIpxStatRipReqReceives_Object = MibScalar
hh3cIpxStatRipReqReceives = _Hh3cIpxStatRipReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 18),
    _Hh3cIpxStatRipReqReceives_Type()
)
hh3cIpxStatRipReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatRipReqReceives.setStatus("current")
_Hh3cIpxStatRipReqDeals_Type = Counter32
_Hh3cIpxStatRipReqDeals_Object = MibScalar
hh3cIpxStatRipReqDeals = _Hh3cIpxStatRipReqDeals_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 19),
    _Hh3cIpxStatRipReqDeals_Type()
)
hh3cIpxStatRipReqDeals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatRipReqDeals.setStatus("current")
_Hh3cIpxStatRipReqSends_Type = Counter32
_Hh3cIpxStatRipReqSends_Object = MibScalar
hh3cIpxStatRipReqSends = _Hh3cIpxStatRipReqSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 20),
    _Hh3cIpxStatRipReqSends_Type()
)
hh3cIpxStatRipReqSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatRipReqSends.setStatus("current")
_Hh3cIpxStatRipPeriUpdates_Type = Counter32
_Hh3cIpxStatRipPeriUpdates_Object = MibScalar
hh3cIpxStatRipPeriUpdates = _Hh3cIpxStatRipPeriUpdates_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 21),
    _Hh3cIpxStatRipPeriUpdates_Type()
)
hh3cIpxStatRipPeriUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatRipPeriUpdates.setStatus("current")
_Hh3cIpxStatSapGenReqReceives_Type = Counter32
_Hh3cIpxStatSapGenReqReceives_Object = MibScalar
hh3cIpxStatSapGenReqReceives = _Hh3cIpxStatSapGenReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 22),
    _Hh3cIpxStatSapGenReqReceives_Type()
)
hh3cIpxStatSapGenReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatSapGenReqReceives.setStatus("current")
_Hh3cIpxStatSapSpecReqReceives_Type = Counter32
_Hh3cIpxStatSapSpecReqReceives_Object = MibScalar
hh3cIpxStatSapSpecReqReceives = _Hh3cIpxStatSapSpecReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 23),
    _Hh3cIpxStatSapSpecReqReceives_Type()
)
hh3cIpxStatSapSpecReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatSapSpecReqReceives.setStatus("current")
_Hh3cIpxStatSapGnsReqReceives_Type = Counter32
_Hh3cIpxStatSapGnsReqReceives_Object = MibScalar
hh3cIpxStatSapGnsReqReceives = _Hh3cIpxStatSapGnsReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 24),
    _Hh3cIpxStatSapGnsReqReceives_Type()
)
hh3cIpxStatSapGnsReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatSapGnsReqReceives.setStatus("current")
_Hh3cIpxStatSapGenRspSends_Type = Counter32
_Hh3cIpxStatSapGenRspSends_Object = MibScalar
hh3cIpxStatSapGenRspSends = _Hh3cIpxStatSapGenRspSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 25),
    _Hh3cIpxStatSapGenRspSends_Type()
)
hh3cIpxStatSapGenRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatSapGenRspSends.setStatus("current")
_Hh3cIpxStatSapSpecRspSends_Type = Counter32
_Hh3cIpxStatSapSpecRspSends_Object = MibScalar
hh3cIpxStatSapSpecRspSends = _Hh3cIpxStatSapSpecRspSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 26),
    _Hh3cIpxStatSapSpecRspSends_Type()
)
hh3cIpxStatSapSpecRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatSapSpecRspSends.setStatus("current")
_Hh3cIpxStatSapGnsRspSends_Type = Counter32
_Hh3cIpxStatSapGnsRspSends_Object = MibScalar
hh3cIpxStatSapGnsRspSends = _Hh3cIpxStatSapGnsRspSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 27),
    _Hh3cIpxStatSapGnsRspSends_Type()
)
hh3cIpxStatSapGnsRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatSapGnsRspSends.setStatus("current")
_Hh3cIpxStatSapPeriUpdates_Type = Counter32
_Hh3cIpxStatSapPeriUpdates_Object = MibScalar
hh3cIpxStatSapPeriUpdates = _Hh3cIpxStatSapPeriUpdates_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 28),
    _Hh3cIpxStatSapPeriUpdates_Type()
)
hh3cIpxStatSapPeriUpdates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatSapPeriUpdates.setStatus("current")
_Hh3cIpxStatSapInPktErrors_Type = Counter32
_Hh3cIpxStatSapInPktErrors_Object = MibScalar
hh3cIpxStatSapInPktErrors = _Hh3cIpxStatSapInPktErrors_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 1, 29),
    _Hh3cIpxStatSapInPktErrors_Type()
)
hh3cIpxStatSapInPktErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxStatSapInPktErrors.setStatus("current")
_Hh3cIpxStatInterface_ObjectIdentity = ObjectIdentity
hh3cIpxStatInterface = _Hh3cIpxStatInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2)
)
_Hh3cIpxIfStatTable_Object = MibTable
hh3cIpxIfStatTable = _Hh3cIpxIfStatTable_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1)
)
if mibBuilder.loadTexts:
    hh3cIpxIfStatTable.setStatus("current")
_Hh3cIpxIfStatEntry_Object = MibTableRow
hh3cIpxIfStatEntry = _Hh3cIpxIfStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1)
)
hh3cIpxIfStatEntry.setIndexNames(
    (0, "HH3C-IPX-MIB", "hh3cIpxIfStatIndex"),
)
if mibBuilder.loadTexts:
    hh3cIpxIfStatEntry.setStatus("current")


class _Hh3cIpxIfStatIndex_Type(Integer32):
    """Custom type hh3cIpxIfStatIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_Hh3cIpxIfStatIndex_Type.__name__ = "Integer32"
_Hh3cIpxIfStatIndex_Object = MibTableColumn
hh3cIpxIfStatIndex = _Hh3cIpxIfStatIndex_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 1),
    _Hh3cIpxIfStatIndex_Type()
)
hh3cIpxIfStatIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hh3cIpxIfStatIndex.setStatus("current")


class _Hh3cIpxIfStatNetId_Type(OctetString):
    """Custom type hh3cIpxIfStatNetId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )


_Hh3cIpxIfStatNetId_Type.__name__ = "OctetString"
_Hh3cIpxIfStatNetId_Object = MibTableColumn
hh3cIpxIfStatNetId = _Hh3cIpxIfStatNetId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 2),
    _Hh3cIpxIfStatNetId_Type()
)
hh3cIpxIfStatNetId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatNetId.setStatus("current")


class _Hh3cIpxIfStatNodeId_Type(OctetString):
    """Custom type hh3cIpxIfStatNodeId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_Hh3cIpxIfStatNodeId_Type.__name__ = "OctetString"
_Hh3cIpxIfStatNodeId_Object = MibTableColumn
hh3cIpxIfStatNodeId = _Hh3cIpxIfStatNodeId_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 3),
    _Hh3cIpxIfStatNodeId_Type()
)
hh3cIpxIfStatNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatNodeId.setStatus("current")
_Hh3cIpxIfStatIpxReceives_Type = Counter32
_Hh3cIpxIfStatIpxReceives_Object = MibTableColumn
hh3cIpxIfStatIpxReceives = _Hh3cIpxIfStatIpxReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 4),
    _Hh3cIpxIfStatIpxReceives_Type()
)
hh3cIpxIfStatIpxReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatIpxReceives.setStatus("current")
_Hh3cIpxIfStatIpxSends_Type = Counter32
_Hh3cIpxIfStatIpxSends_Object = MibTableColumn
hh3cIpxIfStatIpxSends = _Hh3cIpxIfStatIpxSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 5),
    _Hh3cIpxIfStatIpxSends_Type()
)
hh3cIpxIfStatIpxSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatIpxSends.setStatus("current")
_Hh3cIpxIfStatIpxRecvBytes_Type = Counter32
_Hh3cIpxIfStatIpxRecvBytes_Object = MibTableColumn
hh3cIpxIfStatIpxRecvBytes = _Hh3cIpxIfStatIpxRecvBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 6),
    _Hh3cIpxIfStatIpxRecvBytes_Type()
)
hh3cIpxIfStatIpxRecvBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatIpxRecvBytes.setStatus("current")
_Hh3cIpxIfStatIpxSendBytes_Type = Counter32
_Hh3cIpxIfStatIpxSendBytes_Object = MibTableColumn
hh3cIpxIfStatIpxSendBytes = _Hh3cIpxIfStatIpxSendBytes_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 7),
    _Hh3cIpxIfStatIpxSendBytes_Type()
)
hh3cIpxIfStatIpxSendBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatIpxSendBytes.setStatus("current")
_Hh3cIpxIfStatRipReceives_Type = Counter32
_Hh3cIpxIfStatRipReceives_Object = MibTableColumn
hh3cIpxIfStatRipReceives = _Hh3cIpxIfStatRipReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 8),
    _Hh3cIpxIfStatRipReceives_Type()
)
hh3cIpxIfStatRipReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatRipReceives.setStatus("current")
_Hh3cIpxIfStatRipSends_Type = Counter32
_Hh3cIpxIfStatRipSends_Object = MibTableColumn
hh3cIpxIfStatRipSends = _Hh3cIpxIfStatRipSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 9),
    _Hh3cIpxIfStatRipSends_Type()
)
hh3cIpxIfStatRipSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatRipSends.setStatus("current")
_Hh3cIpxIfStatRipDiscards_Type = Counter32
_Hh3cIpxIfStatRipDiscards_Object = MibTableColumn
hh3cIpxIfStatRipDiscards = _Hh3cIpxIfStatRipDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 10),
    _Hh3cIpxIfStatRipDiscards_Type()
)
hh3cIpxIfStatRipDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatRipDiscards.setStatus("current")
_Hh3cIpxIfStatRipSpecReqReceives_Type = Counter32
_Hh3cIpxIfStatRipSpecReqReceives_Object = MibTableColumn
hh3cIpxIfStatRipSpecReqReceives = _Hh3cIpxIfStatRipSpecReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 11),
    _Hh3cIpxIfStatRipSpecReqReceives_Type()
)
hh3cIpxIfStatRipSpecReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatRipSpecReqReceives.setStatus("current")
_Hh3cIpxIfStatRipSpecRspSends_Type = Counter32
_Hh3cIpxIfStatRipSpecRspSends_Object = MibTableColumn
hh3cIpxIfStatRipSpecRspSends = _Hh3cIpxIfStatRipSpecRspSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 12),
    _Hh3cIpxIfStatRipSpecRspSends_Type()
)
hh3cIpxIfStatRipSpecRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatRipSpecRspSends.setStatus("current")
_Hh3cIpxIfStatRipGenReqReceives_Type = Counter32
_Hh3cIpxIfStatRipGenReqReceives_Object = MibTableColumn
hh3cIpxIfStatRipGenReqReceives = _Hh3cIpxIfStatRipGenReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 13),
    _Hh3cIpxIfStatRipGenReqReceives_Type()
)
hh3cIpxIfStatRipGenReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatRipGenReqReceives.setStatus("current")
_Hh3cIpxIfStatRipGenRspSends_Type = Counter32
_Hh3cIpxIfStatRipGenRspSends_Object = MibTableColumn
hh3cIpxIfStatRipGenRspSends = _Hh3cIpxIfStatRipGenRspSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 14),
    _Hh3cIpxIfStatRipGenRspSends_Type()
)
hh3cIpxIfStatRipGenRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatRipGenRspSends.setStatus("current")
_Hh3cIpxIfStatSapReceives_Type = Counter32
_Hh3cIpxIfStatSapReceives_Object = MibTableColumn
hh3cIpxIfStatSapReceives = _Hh3cIpxIfStatSapReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 15),
    _Hh3cIpxIfStatSapReceives_Type()
)
hh3cIpxIfStatSapReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatSapReceives.setStatus("current")
_Hh3cIpxIfStatSapSends_Type = Counter32
_Hh3cIpxIfStatSapSends_Object = MibTableColumn
hh3cIpxIfStatSapSends = _Hh3cIpxIfStatSapSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 16),
    _Hh3cIpxIfStatSapSends_Type()
)
hh3cIpxIfStatSapSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatSapSends.setStatus("current")
_Hh3cIpxIfStatSapDiscards_Type = Counter32
_Hh3cIpxIfStatSapDiscards_Object = MibTableColumn
hh3cIpxIfStatSapDiscards = _Hh3cIpxIfStatSapDiscards_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 17),
    _Hh3cIpxIfStatSapDiscards_Type()
)
hh3cIpxIfStatSapDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatSapDiscards.setStatus("current")
_Hh3cIpxIfStatSapGnsReqReceives_Type = Counter32
_Hh3cIpxIfStatSapGnsReqReceives_Object = MibTableColumn
hh3cIpxIfStatSapGnsReqReceives = _Hh3cIpxIfStatSapGnsReqReceives_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 18),
    _Hh3cIpxIfStatSapGnsReqReceives_Type()
)
hh3cIpxIfStatSapGnsReqReceives.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatSapGnsReqReceives.setStatus("current")
_Hh3cIpxIfStatSapGnsRspSends_Type = Counter32
_Hh3cIpxIfStatSapGnsRspSends_Object = MibTableColumn
hh3cIpxIfStatSapGnsRspSends = _Hh3cIpxIfStatSapGnsRspSends_Object(
    (1, 3, 6, 1, 4, 1, 25506, 2, 34, 4, 2, 1, 1, 19),
    _Hh3cIpxIfStatSapGnsRspSends_Type()
)
hh3cIpxIfStatSapGnsRspSends.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hh3cIpxIfStatSapGnsRspSends.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HH3C-IPX-MIB",
    **{"EnabledStatus": EnabledStatus,
       "hh3cIpx": hh3cIpx,
       "hh3cIpxConfig": hh3cIpxConfig,
       "hh3cIpxStatus": hh3cIpxStatus,
       "hh3cIpxIfConfigTable": hh3cIpxIfConfigTable,
       "hh3cIpxIfConfigEntry": hh3cIpxIfConfigEntry,
       "hh3cIpxIfIndex": hh3cIpxIfIndex,
       "hh3cIpxIfNetId": hh3cIpxIfNetId,
       "hh3cIpxIfNodeId": hh3cIpxIfNodeId,
       "hh3cIpxIfSplitHorizon": hh3cIpxIfSplitHorizon,
       "hh3cIPxIfTick": hh3cIPxIfTick,
       "hh3cIpxIfUpdateChangeOnly": hh3cIpxIfUpdateChangeOnly,
       "hh3cIpxIfRipMtu": hh3cIpxIfRipMtu,
       "hh3cIpxIfEncapsuleType": hh3cIpxIfEncapsuleType,
       "hh3cIpxIfNetbiosPropagation": hh3cIpxIfNetbiosPropagation,
       "hh3cIpxIfSapStatus": hh3cIpxIfSapStatus,
       "hh3cIpxIfSapMtu": hh3cIpxIfSapMtu,
       "hh3cIpxIfGnsReply": hh3cIpxIfGnsReply,
       "hh3cIpxIfRowStatus": hh3cIpxIfRowStatus,
       "hh3cIpxRip": hh3cIpxRip,
       "hh3cIpxRouteMultiplier": hh3cIpxRouteMultiplier,
       "hh3cIpxRouteUpdateTimer": hh3cIpxRouteUpdateTimer,
       "hh3cIpxRouteImpRouteStatic": hh3cIpxRouteImpRouteStatic,
       "hh3cIpxRouteLoadBalancePaths": hh3cIpxRouteLoadBalancePaths,
       "hh3cIpxRouteMaxResPaths": hh3cIpxRouteMaxResPaths,
       "hh3cIpxRouteTable": hh3cIpxRouteTable,
       "hh3cIpxRouteEntry": hh3cIpxRouteEntry,
       "hh3cIpxRouteIndex": hh3cIpxRouteIndex,
       "hh3cIpxRouteDestNetId": hh3cIpxRouteDestNetId,
       "hh3cIpxRouteNextHop": hh3cIpxRouteNextHop,
       "hh3cIpxRoutePro": hh3cIpxRoutePro,
       "hh3cIpxRoutePre": hh3cIpxRoutePre,
       "hh3cIpxRouteTicks": hh3cIpxRouteTicks,
       "hh3cIpxRouteHops": hh3cIpxRouteHops,
       "hh3cIpxRouteTime": hh3cIpxRouteTime,
       "hh3cIpxRouteOutInterface": hh3cIpxRouteOutInterface,
       "hh3cIpxStaticRouteTable": hh3cIpxStaticRouteTable,
       "hh3cIpxStaticRouteEntry": hh3cIpxStaticRouteEntry,
       "hh3cIpxStaticRouteDestNetId": hh3cIpxStaticRouteDestNetId,
       "hh3cIpxStaticRouteNextHop": hh3cIpxStaticRouteNextHop,
       "hh3cIpxStaticRoutePre": hh3cIpxStaticRoutePre,
       "hh3cIpxStaticRouteOutIf": hh3cIpxStaticRouteOutIf,
       "hh3cIpxStaticRouteTicks": hh3cIpxStaticRouteTicks,
       "hh3cIpxStaticRouteHops": hh3cIpxStaticRouteHops,
       "hh3cIpxStaticRouteStatus": hh3cIpxStaticRouteStatus,
       "hh3cIpxStaticRouteRowStatus": hh3cIpxStaticRouteRowStatus,
       "hh3cIpxRouteStatTable": hh3cIpxRouteStatTable,
       "hh3cIpxRouteStatEntry": hh3cIpxRouteStatEntry,
       "hh3cIpxRouteStatPro": hh3cIpxRouteStatPro,
       "hh3cIpxRouteStatRoutes": hh3cIpxRouteStatRoutes,
       "hh3cIpxRouteStatActives": hh3cIpxRouteStatActives,
       "hh3cIpxRouteStatAddeds": hh3cIpxRouteStatAddeds,
       "hh3cIpxRouteStatDeleteds": hh3cIpxRouteStatDeleteds,
       "hh3cIpxRouteStatFreeds": hh3cIpxRouteStatFreeds,
       "hh3cIpxSap": hh3cIpxSap,
       "hh3cIpxSapMultiplier": hh3cIpxSapMultiplier,
       "hh3cIpxSapUpdateTimer": hh3cIpxSapUpdateTimer,
       "hh3cIpxSapGnsLoadBalance": hh3cIpxSapGnsLoadBalance,
       "hh3cIpxSapMaxResServers": hh3cIpxSapMaxResServers,
       "hh3cIpxServiceTable": hh3cIpxServiceTable,
       "hh3cIpxServiceEntry": hh3cIpxServiceEntry,
       "hh3cIpxServiceIndex": hh3cIpxServiceIndex,
       "hh3cIpxServiceName": hh3cIpxServiceName,
       "hh3cIpxServiceType": hh3cIpxServiceType,
       "hh3cIpxServiceNetId": hh3cIpxServiceNetId,
       "hh3cIpxServiceNodeId": hh3cIpxServiceNodeId,
       "hh3cIpxServiceSocketNo": hh3cIpxServiceSocketNo,
       "hh3cIpxServicePreference": hh3cIpxServicePreference,
       "hh3cIpxServiceHops": hh3cIpxServiceHops,
       "hh3cIpxServiceRecvIf": hh3cIpxServiceRecvIf,
       "hh3cIpxStaticServiceTable": hh3cIpxStaticServiceTable,
       "hh3cIpxStaticServiceEntry": hh3cIpxStaticServiceEntry,
       "hh3cIpxStaticServiceType": hh3cIpxStaticServiceType,
       "hh3cIpxStaticServiceName": hh3cIpxStaticServiceName,
       "hh3cIpxStaticServiceNetId": hh3cIpxStaticServiceNetId,
       "hh3cIpxStaticServiceNodeId": hh3cIpxStaticServiceNodeId,
       "hh3cIpxStatciServiceSocketNo": hh3cIpxStatciServiceSocketNo,
       "hh3cIpxStaticServicePreference": hh3cIpxStaticServicePreference,
       "hh3cIpxStaticServiceHops": hh3cIpxStaticServiceHops,
       "hh3cIpxStaticServiceStatus": hh3cIpxStaticServiceStatus,
       "hh3cIpxStaticServiceRowStatus": hh3cIpxStaticServiceRowStatus,
       "hh3cIpxStat": hh3cIpxStat,
       "hh3cIpxStatGlobal": hh3cIpxStatGlobal,
       "hh3cIpxStatTotalReceives": hh3cIpxStatTotalReceives,
       "hh3cIpxStatPitchs": hh3cIpxStatPitchs,
       "hh3cIpxStatLenErrors": hh3cIpxStatLenErrors,
       "hh3cIpxStatFormatErrors": hh3cIpxStatFormatErrors,
       "hh3cIpxStatBadHops": hh3cIpxStatBadHops,
       "hh3cIpxStatHopsDiscards": hh3cIpxStatHopsDiscards,
       "hh3cIpxStatOtherErrors": hh3cIpxStatOtherErrors,
       "hh3cIpxStatLocalDests": hh3cIpxStatLocalDests,
       "hh3cIpxStatCantDeals": hh3cIpxStatCantDeals,
       "hh3cIpxStatForwards": hh3cIpxStatForwards,
       "hh3cIpxStatGenerates": hh3cIpxStatGenerates,
       "hh3cIpxStatNoRoutes": hh3cIpxStatNoRoutes,
       "hh3cIpxStatOutDiscards": hh3cIpxStatOutDiscards,
       "hh3cIpxStatRipSends": hh3cIpxStatRipSends,
       "hh3cIpxStatRipReceives": hh3cIpxStatRipReceives,
       "hh3cIpxStaRipRspSends": hh3cIpxStaRipRspSends,
       "hh3cIpxStaRipRspReceives": hh3cIpxStaRipRspReceives,
       "hh3cIpxStatRipReqReceives": hh3cIpxStatRipReqReceives,
       "hh3cIpxStatRipReqDeals": hh3cIpxStatRipReqDeals,
       "hh3cIpxStatRipReqSends": hh3cIpxStatRipReqSends,
       "hh3cIpxStatRipPeriUpdates": hh3cIpxStatRipPeriUpdates,
       "hh3cIpxStatSapGenReqReceives": hh3cIpxStatSapGenReqReceives,
       "hh3cIpxStatSapSpecReqReceives": hh3cIpxStatSapSpecReqReceives,
       "hh3cIpxStatSapGnsReqReceives": hh3cIpxStatSapGnsReqReceives,
       "hh3cIpxStatSapGenRspSends": hh3cIpxStatSapGenRspSends,
       "hh3cIpxStatSapSpecRspSends": hh3cIpxStatSapSpecRspSends,
       "hh3cIpxStatSapGnsRspSends": hh3cIpxStatSapGnsRspSends,
       "hh3cIpxStatSapPeriUpdates": hh3cIpxStatSapPeriUpdates,
       "hh3cIpxStatSapInPktErrors": hh3cIpxStatSapInPktErrors,
       "hh3cIpxStatInterface": hh3cIpxStatInterface,
       "hh3cIpxIfStatTable": hh3cIpxIfStatTable,
       "hh3cIpxIfStatEntry": hh3cIpxIfStatEntry,
       "hh3cIpxIfStatIndex": hh3cIpxIfStatIndex,
       "hh3cIpxIfStatNetId": hh3cIpxIfStatNetId,
       "hh3cIpxIfStatNodeId": hh3cIpxIfStatNodeId,
       "hh3cIpxIfStatIpxReceives": hh3cIpxIfStatIpxReceives,
       "hh3cIpxIfStatIpxSends": hh3cIpxIfStatIpxSends,
       "hh3cIpxIfStatIpxRecvBytes": hh3cIpxIfStatIpxRecvBytes,
       "hh3cIpxIfStatIpxSendBytes": hh3cIpxIfStatIpxSendBytes,
       "hh3cIpxIfStatRipReceives": hh3cIpxIfStatRipReceives,
       "hh3cIpxIfStatRipSends": hh3cIpxIfStatRipSends,
       "hh3cIpxIfStatRipDiscards": hh3cIpxIfStatRipDiscards,
       "hh3cIpxIfStatRipSpecReqReceives": hh3cIpxIfStatRipSpecReqReceives,
       "hh3cIpxIfStatRipSpecRspSends": hh3cIpxIfStatRipSpecRspSends,
       "hh3cIpxIfStatRipGenReqReceives": hh3cIpxIfStatRipGenReqReceives,
       "hh3cIpxIfStatRipGenRspSends": hh3cIpxIfStatRipGenRspSends,
       "hh3cIpxIfStatSapReceives": hh3cIpxIfStatSapReceives,
       "hh3cIpxIfStatSapSends": hh3cIpxIfStatSapSends,
       "hh3cIpxIfStatSapDiscards": hh3cIpxIfStatSapDiscards,
       "hh3cIpxIfStatSapGnsReqReceives": hh3cIpxIfStatSapGnsReqReceives,
       "hh3cIpxIfStatSapGnsRspSends": hh3cIpxIfStatSapGnsRspSends}
)
