# SNMP MIB module (WWP-LEOS-RAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/WWP-LEOS-RAPS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:06 2024
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
 MacAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(wwpModules,
 wwpModulesLeos) = mibBuilder.importSymbols(
    "WWP-SMI",
    "wwpModules",
    "wwpModulesLeos")


# MODULE-IDENTITY

wwpLeosRapsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47)
)
wwpLeosRapsMIB.setRevisions(
        ("2010-09-16 17:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WwpLeosRapsMIBObjects_ObjectIdentity = ObjectIdentity
wwpLeosRapsMIBObjects = _WwpLeosRapsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1)
)
_WwpLeosRapsGlobal_ObjectIdentity = ObjectIdentity
wwpLeosRapsGlobal = _WwpLeosRapsGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1)
)
_WwpLeosRapsGlobalAttrs_ObjectIdentity = ObjectIdentity
wwpLeosRapsGlobalAttrs = _WwpLeosRapsGlobalAttrs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1, 1)
)


class _WwpLeosRapsState_Type(Integer32):
    """Custom type wwpLeosRapsState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_WwpLeosRapsState_Type.__name__ = "Integer32"
_WwpLeosRapsState_Object = MibScalar
wwpLeosRapsState = _WwpLeosRapsState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1, 1, 1),
    _WwpLeosRapsState_Type()
)
wwpLeosRapsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsState.setStatus("current")
_WwpLeosRapsNodeId_Type = MacAddress
_WwpLeosRapsNodeId_Object = MibScalar
wwpLeosRapsNodeId = _WwpLeosRapsNodeId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1, 1, 2),
    _WwpLeosRapsNodeId_Type()
)
wwpLeosRapsNodeId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsNodeId.setStatus("current")


class _WwpLeosRapsEtherType_Type(OctetString):
    """Custom type wwpLeosRapsEtherType based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_WwpLeosRapsEtherType_Type.__name__ = "OctetString"
_WwpLeosRapsEtherType_Object = MibScalar
wwpLeosRapsEtherType = _WwpLeosRapsEtherType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1, 1, 3),
    _WwpLeosRapsEtherType_Type()
)
wwpLeosRapsEtherType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsEtherType.setStatus("current")


class _WwpLeosRapsNumberOfRings_Type(Integer32):
    """Custom type wwpLeosRapsNumberOfRings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosRapsNumberOfRings_Type.__name__ = "Integer32"
_WwpLeosRapsNumberOfRings_Object = MibScalar
wwpLeosRapsNumberOfRings = _WwpLeosRapsNumberOfRings_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 1, 1, 4),
    _WwpLeosRapsNumberOfRings_Type()
)
wwpLeosRapsNumberOfRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsNumberOfRings.setStatus("current")
_WwpLeosRapsLogicalRing_ObjectIdentity = ObjectIdentity
wwpLeosRapsLogicalRing = _WwpLeosRapsLogicalRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2)
)
_WwpLeosRapsLogicalRingTable_Object = MibTable
wwpLeosRapsLogicalRingTable = _WwpLeosRapsLogicalRingTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1)
)
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingTable.setStatus("current")
_WwpLeosRapsLogicalRingEntry_Object = MibTableRow
wwpLeosRapsLogicalRingEntry = _WwpLeosRapsLogicalRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1)
)
wwpLeosRapsLogicalRingEntry.setIndexNames(
    (0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsLogicalRingIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingEntry.setStatus("current")


class _WwpLeosRapsLogicalRingIndex_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_WwpLeosRapsLogicalRingIndex_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingIndex_Object = MibTableColumn
wwpLeosRapsLogicalRingIndex = _WwpLeosRapsLogicalRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 1),
    _WwpLeosRapsLogicalRingIndex_Type()
)
wwpLeosRapsLogicalRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingIndex.setStatus("current")


class _WwpLeosRapsLogicalRingName_Type(OctetString):
    """Custom type wwpLeosRapsLogicalRingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLeosRapsLogicalRingName_Type.__name__ = "OctetString"
_WwpLeosRapsLogicalRingName_Object = MibTableColumn
wwpLeosRapsLogicalRingName = _WwpLeosRapsLogicalRingName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 2),
    _WwpLeosRapsLogicalRingName_Type()
)
wwpLeosRapsLogicalRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingName.setStatus("current")


class _WwpLeosRapsLogicalRingId_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WwpLeosRapsLogicalRingId_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingId_Object = MibTableColumn
wwpLeosRapsLogicalRingId = _WwpLeosRapsLogicalRingId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 3),
    _WwpLeosRapsLogicalRingId_Type()
)
wwpLeosRapsLogicalRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingId.setStatus("current")


class _WwpLeosRapsLogicalRingGuardTime_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingGuardTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_WwpLeosRapsLogicalRingGuardTime_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingGuardTime_Object = MibTableColumn
wwpLeosRapsLogicalRingGuardTime = _WwpLeosRapsLogicalRingGuardTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 4),
    _WwpLeosRapsLogicalRingGuardTime_Type()
)
wwpLeosRapsLogicalRingGuardTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingGuardTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingGuardTime.setUnits("milliseconds")


class _WwpLeosRapsLogicalRingWtr_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingWtr based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_WwpLeosRapsLogicalRingWtr_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingWtr_Object = MibTableColumn
wwpLeosRapsLogicalRingWtr = _WwpLeosRapsLogicalRingWtr_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 5),
    _WwpLeosRapsLogicalRingWtr_Type()
)
wwpLeosRapsLogicalRingWtr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingWtr.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingWtr.setUnits("minutes")
_WwpLeosRapsLogicalRingWtb_Type = Integer32
_WwpLeosRapsLogicalRingWtb_Object = MibTableColumn
wwpLeosRapsLogicalRingWtb = _WwpLeosRapsLogicalRingWtb_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 6),
    _WwpLeosRapsLogicalRingWtb_Type()
)
wwpLeosRapsLogicalRingWtb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingWtb.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingWtb.setUnits("minutes")


class _WwpLeosRapsLogicalRingWestPortId_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingWestPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosRapsLogicalRingWestPortId_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingWestPortId_Object = MibTableColumn
wwpLeosRapsLogicalRingWestPortId = _WwpLeosRapsLogicalRingWestPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 7),
    _WwpLeosRapsLogicalRingWestPortId_Type()
)
wwpLeosRapsLogicalRingWestPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingWestPortId.setStatus("current")


class _WwpLeosRapsLogicalRingWestHoldOffTime_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingWestHoldOffTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WwpLeosRapsLogicalRingWestHoldOffTime_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingWestHoldOffTime_Object = MibTableColumn
wwpLeosRapsLogicalRingWestHoldOffTime = _WwpLeosRapsLogicalRingWestHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 8),
    _WwpLeosRapsLogicalRingWestHoldOffTime_Type()
)
wwpLeosRapsLogicalRingWestHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingWestHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingWestHoldOffTime.setUnits("milliseconds")


class _WwpLeosRapsLogicalRingWestForce_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingWestForce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WwpLeosRapsLogicalRingWestForce_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingWestForce_Object = MibTableColumn
wwpLeosRapsLogicalRingWestForce = _WwpLeosRapsLogicalRingWestForce_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 9),
    _WwpLeosRapsLogicalRingWestForce_Type()
)
wwpLeosRapsLogicalRingWestForce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingWestForce.setStatus("current")


class _WwpLeosRapsLogicalRingWestCfmService_Type(OctetString):
    """Custom type wwpLeosRapsLogicalRingWestCfmService based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLeosRapsLogicalRingWestCfmService_Type.__name__ = "OctetString"
_WwpLeosRapsLogicalRingWestCfmService_Object = MibTableColumn
wwpLeosRapsLogicalRingWestCfmService = _WwpLeosRapsLogicalRingWestCfmService_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 10),
    _WwpLeosRapsLogicalRingWestCfmService_Type()
)
wwpLeosRapsLogicalRingWestCfmService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingWestCfmService.setStatus("current")


class _WwpLeosRapsLogicalRingEastPortId_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingEastPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_WwpLeosRapsLogicalRingEastPortId_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingEastPortId_Object = MibTableColumn
wwpLeosRapsLogicalRingEastPortId = _WwpLeosRapsLogicalRingEastPortId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 11),
    _WwpLeosRapsLogicalRingEastPortId_Type()
)
wwpLeosRapsLogicalRingEastPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingEastPortId.setStatus("current")


class _WwpLeosRapsLogicalRingEastHoldOffTime_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingEastHoldOffTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_WwpLeosRapsLogicalRingEastHoldOffTime_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingEastHoldOffTime_Object = MibTableColumn
wwpLeosRapsLogicalRingEastHoldOffTime = _WwpLeosRapsLogicalRingEastHoldOffTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 12),
    _WwpLeosRapsLogicalRingEastHoldOffTime_Type()
)
wwpLeosRapsLogicalRingEastHoldOffTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingEastHoldOffTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingEastHoldOffTime.setUnits("milliseconds")


class _WwpLeosRapsLogicalRingEastForce_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingEastForce based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WwpLeosRapsLogicalRingEastForce_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingEastForce_Object = MibTableColumn
wwpLeosRapsLogicalRingEastForce = _WwpLeosRapsLogicalRingEastForce_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 13),
    _WwpLeosRapsLogicalRingEastForce_Type()
)
wwpLeosRapsLogicalRingEastForce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingEastForce.setStatus("current")


class _WwpLeosRapsLogicalRingEastCfmService_Type(OctetString):
    """Custom type wwpLeosRapsLogicalRingEastCfmService based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLeosRapsLogicalRingEastCfmService_Type.__name__ = "OctetString"
_WwpLeosRapsLogicalRingEastCfmService_Object = MibTableColumn
wwpLeosRapsLogicalRingEastCfmService = _WwpLeosRapsLogicalRingEastCfmService_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 14),
    _WwpLeosRapsLogicalRingEastCfmService_Type()
)
wwpLeosRapsLogicalRingEastCfmService.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingEastCfmService.setStatus("current")


class _WwpLeosRapsLogicalRingNumberOfVirtualRings_Type(Integer32):
    """Custom type wwpLeosRapsLogicalRingNumberOfVirtualRings based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosRapsLogicalRingNumberOfVirtualRings_Type.__name__ = "Integer32"
_WwpLeosRapsLogicalRingNumberOfVirtualRings_Object = MibTableColumn
wwpLeosRapsLogicalRingNumberOfVirtualRings = _WwpLeosRapsLogicalRingNumberOfVirtualRings_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 2, 1, 1, 15),
    _WwpLeosRapsLogicalRingNumberOfVirtualRings_Type()
)
wwpLeosRapsLogicalRingNumberOfVirtualRings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsLogicalRingNumberOfVirtualRings.setStatus("current")
_WwpLeosRapsVirtualRing_ObjectIdentity = ObjectIdentity
wwpLeosRapsVirtualRing = _WwpLeosRapsVirtualRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3)
)
_WwpLeosRapsVirtualRingTable_Object = MibTable
wwpLeosRapsVirtualRingTable = _WwpLeosRapsVirtualRingTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1)
)
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingTable.setStatus("current")
_WwpLeosRapsVirtualRingEntry_Object = MibTableRow
wwpLeosRapsVirtualRingEntry = _WwpLeosRapsVirtualRingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1)
)
wwpLeosRapsVirtualRingEntry.setIndexNames(
    (0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingIndex"),
)
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEntry.setStatus("current")


class _WwpLeosRapsVirtualRingIndex_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_WwpLeosRapsVirtualRingIndex_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingIndex_Object = MibTableColumn
wwpLeosRapsVirtualRingIndex = _WwpLeosRapsVirtualRingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 1),
    _WwpLeosRapsVirtualRingIndex_Type()
)
wwpLeosRapsVirtualRingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingIndex.setStatus("current")


class _WwpLeosRapsVirtualRingName_Type(OctetString):
    """Custom type wwpLeosRapsVirtualRingName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_WwpLeosRapsVirtualRingName_Type.__name__ = "OctetString"
_WwpLeosRapsVirtualRingName_Object = MibTableColumn
wwpLeosRapsVirtualRingName = _WwpLeosRapsVirtualRingName_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 2),
    _WwpLeosRapsVirtualRingName_Type()
)
wwpLeosRapsVirtualRingName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingName.setStatus("current")


class _WwpLeosRapsVirtualRingVid_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_WwpLeosRapsVirtualRingVid_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingVid_Object = MibTableColumn
wwpLeosRapsVirtualRingVid = _WwpLeosRapsVirtualRingVid_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 3),
    _WwpLeosRapsVirtualRingVid_Type()
)
wwpLeosRapsVirtualRingVid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingVid.setStatus("current")


class _WwpLeosRapsVirtualRingLogicalRingId_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingLogicalRingId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_WwpLeosRapsVirtualRingLogicalRingId_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingLogicalRingId_Object = MibTableColumn
wwpLeosRapsVirtualRingLogicalRingId = _WwpLeosRapsVirtualRingLogicalRingId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 4),
    _WwpLeosRapsVirtualRingLogicalRingId_Type()
)
wwpLeosRapsVirtualRingLogicalRingId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingLogicalRingId.setStatus("current")


class _WwpLeosRapsVirtualRingMel_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingMel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_WwpLeosRapsVirtualRingMel_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingMel_Object = MibTableColumn
wwpLeosRapsVirtualRingMel = _WwpLeosRapsVirtualRingMel_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 5),
    _WwpLeosRapsVirtualRingMel_Type()
)
wwpLeosRapsVirtualRingMel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingMel.setStatus("current")


class _WwpLeosRapsVirtualRingRevertive_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingRevertive based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_WwpLeosRapsVirtualRingRevertive_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingRevertive_Object = MibTableColumn
wwpLeosRapsVirtualRingRevertive = _WwpLeosRapsVirtualRingRevertive_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 6),
    _WwpLeosRapsVirtualRingRevertive_Type()
)
wwpLeosRapsVirtualRingRevertive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingRevertive.setStatus("current")


class _WwpLeosRapsVirtualRingState_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("adminDisabled", 1),
          ("ok", 2),
          ("protecting", 3),
          ("recovering", 4))
    )


_WwpLeosRapsVirtualRingState_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingState_Object = MibTableColumn
wwpLeosRapsVirtualRingState = _WwpLeosRapsVirtualRingState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 7),
    _WwpLeosRapsVirtualRingState_Type()
)
wwpLeosRapsVirtualRingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingState.setStatus("current")


class _WwpLeosRapsVirtualRingStatus_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("localForceSwitch", 3),
          ("localSignalFail", 2),
          ("provisioningMismatch", 6),
          ("remoteOrOtherPortForceSwitch", 5),
          ("remoteOrOtherPortSignalFail", 4))
    )


_WwpLeosRapsVirtualRingStatus_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingStatus_Object = MibTableColumn
wwpLeosRapsVirtualRingStatus = _WwpLeosRapsVirtualRingStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 8),
    _WwpLeosRapsVirtualRingStatus_Type()
)
wwpLeosRapsVirtualRingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingStatus.setStatus("current")


class _WwpLeosRapsVirtualRingAlarm_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("protectionSwitching", 2),
          ("provisionMismatch", 3))
    )


_WwpLeosRapsVirtualRingAlarm_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingAlarm_Object = MibTableColumn
wwpLeosRapsVirtualRingAlarm = _WwpLeosRapsVirtualRingAlarm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 9),
    _WwpLeosRapsVirtualRingAlarm_Type()
)
wwpLeosRapsVirtualRingAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingAlarm.setStatus("current")


class _WwpLeosRapsVirtualRingNumOfSwitchOvers_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingNumOfSwitchOvers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WwpLeosRapsVirtualRingNumOfSwitchOvers_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingNumOfSwitchOvers_Object = MibTableColumn
wwpLeosRapsVirtualRingNumOfSwitchOvers = _WwpLeosRapsVirtualRingNumOfSwitchOvers_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 10),
    _WwpLeosRapsVirtualRingNumOfSwitchOvers_Type()
)
wwpLeosRapsVirtualRingNumOfSwitchOvers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingNumOfSwitchOvers.setStatus("current")
_WwpLeosRapsVirtualRingUptimeFromLastFailure_Type = Counter32
_WwpLeosRapsVirtualRingUptimeFromLastFailure_Object = MibTableColumn
wwpLeosRapsVirtualRingUptimeFromLastFailure = _WwpLeosRapsVirtualRingUptimeFromLastFailure_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 11),
    _WwpLeosRapsVirtualRingUptimeFromLastFailure_Type()
)
wwpLeosRapsVirtualRingUptimeFromLastFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingUptimeFromLastFailure.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingUptimeFromLastFailure.setUnits("seconds")
_WwpLeosRapsVirtualRingTotalDownTime_Type = Counter32
_WwpLeosRapsVirtualRingTotalDownTime_Object = MibTableColumn
wwpLeosRapsVirtualRingTotalDownTime = _WwpLeosRapsVirtualRingTotalDownTime_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 12),
    _WwpLeosRapsVirtualRingTotalDownTime_Type()
)
wwpLeosRapsVirtualRingTotalDownTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingTotalDownTime.setStatus("current")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingTotalDownTime.setUnits("seconds")


class _WwpLeosRapsVirtualRingWestPortRpl_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingWestPortRpl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("owner", 2))
    )


_WwpLeosRapsVirtualRingWestPortRpl_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingWestPortRpl_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortRpl = _WwpLeosRapsVirtualRingWestPortRpl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 13),
    _WwpLeosRapsVirtualRingWestPortRpl_Type()
)
wwpLeosRapsVirtualRingWestPortRpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortRpl.setStatus("current")


class _WwpLeosRapsVirtualRingWestPortState_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingWestPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("disabled", 1),
          ("forwarding", 2))
    )


_WwpLeosRapsVirtualRingWestPortState_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingWestPortState_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortState = _WwpLeosRapsVirtualRingWestPortState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 14),
    _WwpLeosRapsVirtualRingWestPortState_Type()
)
wwpLeosRapsVirtualRingWestPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortState.setStatus("current")


class _WwpLeosRapsVirtualRingWestPortStatus_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingWestPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ccmFailure", 3),
          ("down", 2),
          ("localForceSwitch", 4),
          ("oK", 1),
          ("remoteForceSwitch", 5),
          ("remoteSignalFailure", 6))
    )


_WwpLeosRapsVirtualRingWestPortStatus_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingWestPortStatus_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortStatus = _WwpLeosRapsVirtualRingWestPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 15),
    _WwpLeosRapsVirtualRingWestPortStatus_Type()
)
wwpLeosRapsVirtualRingWestPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortStatus.setStatus("current")
_WwpLeosRapsVirtualRingWestPortNrRxd_Type = Counter32
_WwpLeosRapsVirtualRingWestPortNrRxd_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortNrRxd = _WwpLeosRapsVirtualRingWestPortNrRxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 16),
    _WwpLeosRapsVirtualRingWestPortNrRxd_Type()
)
wwpLeosRapsVirtualRingWestPortNrRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortNrRxd.setStatus("current")
_WwpLeosRapsVirtualRingWestPortNrTxd_Type = Counter32
_WwpLeosRapsVirtualRingWestPortNrTxd_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortNrTxd = _WwpLeosRapsVirtualRingWestPortNrTxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 17),
    _WwpLeosRapsVirtualRingWestPortNrTxd_Type()
)
wwpLeosRapsVirtualRingWestPortNrTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortNrTxd.setStatus("current")
_WwpLeosRapsVirtualRingWestPortSfRxd_Type = Counter32
_WwpLeosRapsVirtualRingWestPortSfRxd_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortSfRxd = _WwpLeosRapsVirtualRingWestPortSfRxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 18),
    _WwpLeosRapsVirtualRingWestPortSfRxd_Type()
)
wwpLeosRapsVirtualRingWestPortSfRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortSfRxd.setStatus("current")
_WwpLeosRapsVirtualRingWestPortSfTxd_Type = Counter32
_WwpLeosRapsVirtualRingWestPortSfTxd_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortSfTxd = _WwpLeosRapsVirtualRingWestPortSfTxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 19),
    _WwpLeosRapsVirtualRingWestPortSfTxd_Type()
)
wwpLeosRapsVirtualRingWestPortSfTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortSfTxd.setStatus("current")
_WwpLeosRapsVirtualRingWestPortFsRxd_Type = Counter32
_WwpLeosRapsVirtualRingWestPortFsRxd_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortFsRxd = _WwpLeosRapsVirtualRingWestPortFsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 20),
    _WwpLeosRapsVirtualRingWestPortFsRxd_Type()
)
wwpLeosRapsVirtualRingWestPortFsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortFsRxd.setStatus("current")
_WwpLeosRapsVirtualRingWestPortFsTxd_Type = Counter32
_WwpLeosRapsVirtualRingWestPortFsTxd_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortFsTxd = _WwpLeosRapsVirtualRingWestPortFsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 21),
    _WwpLeosRapsVirtualRingWestPortFsTxd_Type()
)
wwpLeosRapsVirtualRingWestPortFsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortFsTxd.setStatus("current")
_WwpLeosRapsVirtualRingWestPortNrRbRxd_Type = Counter32
_WwpLeosRapsVirtualRingWestPortNrRbRxd_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortNrRbRxd = _WwpLeosRapsVirtualRingWestPortNrRbRxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 22),
    _WwpLeosRapsVirtualRingWestPortNrRbRxd_Type()
)
wwpLeosRapsVirtualRingWestPortNrRbRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortNrRbRxd.setStatus("current")
_WwpLeosRapsVirtualRingWestPortNrRbTxd_Type = Counter32
_WwpLeosRapsVirtualRingWestPortNrRbTxd_Object = MibTableColumn
wwpLeosRapsVirtualRingWestPortNrRbTxd = _WwpLeosRapsVirtualRingWestPortNrRbTxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 23),
    _WwpLeosRapsVirtualRingWestPortNrRbTxd_Type()
)
wwpLeosRapsVirtualRingWestPortNrRbTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingWestPortNrRbTxd.setStatus("current")


class _WwpLeosRapsVirtualRingEastPortRpl_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingEastPortRpl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("owner", 2))
    )


_WwpLeosRapsVirtualRingEastPortRpl_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingEastPortRpl_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortRpl = _WwpLeosRapsVirtualRingEastPortRpl_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 24),
    _WwpLeosRapsVirtualRingEastPortRpl_Type()
)
wwpLeosRapsVirtualRingEastPortRpl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortRpl.setStatus("current")


class _WwpLeosRapsVirtualRingEastPortState_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingEastPortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("blocked", 3),
          ("disabled", 1),
          ("forwarding", 2))
    )


_WwpLeosRapsVirtualRingEastPortState_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingEastPortState_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortState = _WwpLeosRapsVirtualRingEastPortState_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 25),
    _WwpLeosRapsVirtualRingEastPortState_Type()
)
wwpLeosRapsVirtualRingEastPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortState.setStatus("current")


class _WwpLeosRapsVirtualRingEastPortStatus_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingEastPortStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("ccmFailure", 3),
          ("down", 2),
          ("localForceSwitch", 4),
          ("ok", 1),
          ("remoteForceSwitch", 5),
          ("remoteSignalFailure", 6))
    )


_WwpLeosRapsVirtualRingEastPortStatus_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingEastPortStatus_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortStatus = _WwpLeosRapsVirtualRingEastPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 26),
    _WwpLeosRapsVirtualRingEastPortStatus_Type()
)
wwpLeosRapsVirtualRingEastPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortStatus.setStatus("current")
_WwpLeosRapsVirtualRingEastPortNrRxd_Type = Counter32
_WwpLeosRapsVirtualRingEastPortNrRxd_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortNrRxd = _WwpLeosRapsVirtualRingEastPortNrRxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 27),
    _WwpLeosRapsVirtualRingEastPortNrRxd_Type()
)
wwpLeosRapsVirtualRingEastPortNrRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortNrRxd.setStatus("current")
_WwpLeosRapsVirtualRingEastPortNrTxd_Type = Counter32
_WwpLeosRapsVirtualRingEastPortNrTxd_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortNrTxd = _WwpLeosRapsVirtualRingEastPortNrTxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 28),
    _WwpLeosRapsVirtualRingEastPortNrTxd_Type()
)
wwpLeosRapsVirtualRingEastPortNrTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortNrTxd.setStatus("current")
_WwpLeosRapsVirtualRingEastPortSfRxd_Type = Counter32
_WwpLeosRapsVirtualRingEastPortSfRxd_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortSfRxd = _WwpLeosRapsVirtualRingEastPortSfRxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 29),
    _WwpLeosRapsVirtualRingEastPortSfRxd_Type()
)
wwpLeosRapsVirtualRingEastPortSfRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortSfRxd.setStatus("current")
_WwpLeosRapsVirtualRingEastPortSfTxd_Type = Counter32
_WwpLeosRapsVirtualRingEastPortSfTxd_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortSfTxd = _WwpLeosRapsVirtualRingEastPortSfTxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 30),
    _WwpLeosRapsVirtualRingEastPortSfTxd_Type()
)
wwpLeosRapsVirtualRingEastPortSfTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortSfTxd.setStatus("current")
_WwpLeosRapsVirtualRingEastPortFsRxd_Type = Counter32
_WwpLeosRapsVirtualRingEastPortFsRxd_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortFsRxd = _WwpLeosRapsVirtualRingEastPortFsRxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 31),
    _WwpLeosRapsVirtualRingEastPortFsRxd_Type()
)
wwpLeosRapsVirtualRingEastPortFsRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortFsRxd.setStatus("current")
_WwpLeosRapsVirtualRingEastPortFsTxd_Type = Counter32
_WwpLeosRapsVirtualRingEastPortFsTxd_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortFsTxd = _WwpLeosRapsVirtualRingEastPortFsTxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 32),
    _WwpLeosRapsVirtualRingEastPortFsTxd_Type()
)
wwpLeosRapsVirtualRingEastPortFsTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortFsTxd.setStatus("current")
_WwpLeosRapsVirtualRingEastPortNrRbRxd_Type = Counter32
_WwpLeosRapsVirtualRingEastPortNrRbRxd_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortNrRbRxd = _WwpLeosRapsVirtualRingEastPortNrRbRxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 33),
    _WwpLeosRapsVirtualRingEastPortNrRbRxd_Type()
)
wwpLeosRapsVirtualRingEastPortNrRbRxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortNrRbRxd.setStatus("current")
_WwpLeosRapsVirtualRingEastPortNrRbTxd_Type = Counter32
_WwpLeosRapsVirtualRingEastPortNrRbTxd_Object = MibTableColumn
wwpLeosRapsVirtualRingEastPortNrRbTxd = _WwpLeosRapsVirtualRingEastPortNrRbTxd_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 34),
    _WwpLeosRapsVirtualRingEastPortNrRbTxd_Type()
)
wwpLeosRapsVirtualRingEastPortNrRbTxd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingEastPortNrRbTxd.setStatus("current")


class _WwpLeosRapsVirtualRingType_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("majorRing", 1),
          ("subRing", 2))
    )


_WwpLeosRapsVirtualRingType_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingType_Object = MibTableColumn
wwpLeosRapsVirtualRingType = _WwpLeosRapsVirtualRingType_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 35),
    _WwpLeosRapsVirtualRingType_Type()
)
wwpLeosRapsVirtualRingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingType.setStatus("current")


class _WwpLeosRapsVirtualRingSubRingPortTerm_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingSubRingPortTerm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("eastPortTerminate", 3),
          ("noTerminate", 1),
          ("westPortTerminate", 2))
    )


_WwpLeosRapsVirtualRingSubRingPortTerm_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingSubRingPortTerm_Object = MibTableColumn
wwpLeosRapsVirtualRingSubRingPortTerm = _WwpLeosRapsVirtualRingSubRingPortTerm_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 3, 1, 1, 36),
    _WwpLeosRapsVirtualRingSubRingPortTerm_Type()
)
wwpLeosRapsVirtualRingSubRingPortTerm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingSubRingPortTerm.setStatus("current")
_WwpLeosRapsVirtualRingMember_ObjectIdentity = ObjectIdentity
wwpLeosRapsVirtualRingMember = _WwpLeosRapsVirtualRingMember_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4)
)
_WwpLeosRapsVirtualRingMemberTable_Object = MibTable
wwpLeosRapsVirtualRingMemberTable = _WwpLeosRapsVirtualRingMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 1)
)
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingMemberTable.setStatus("current")
_WwpLeosRapsVirtualRingMemberEntry_Object = MibTableRow
wwpLeosRapsVirtualRingMemberEntry = _WwpLeosRapsVirtualRingMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 1, 1)
)
wwpLeosRapsVirtualRingMemberEntry.setIndexNames(
    (0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingIndex"),
    (0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingMemberVlanId"),
)
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingMemberEntry.setStatus("current")


class _WwpLeosRapsVirtualRingMemberVlanId_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingMemberVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_WwpLeosRapsVirtualRingMemberVlanId_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingMemberVlanId_Object = MibTableColumn
wwpLeosRapsVirtualRingMemberVlanId = _WwpLeosRapsVirtualRingMemberVlanId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 1, 1, 2),
    _WwpLeosRapsVirtualRingMemberVlanId_Type()
)
wwpLeosRapsVirtualRingMemberVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingMemberVlanId.setStatus("current")
_WwpLeosRapsVirtualRingMemberVsTable_Object = MibTable
wwpLeosRapsVirtualRingMemberVsTable = _WwpLeosRapsVirtualRingMemberVsTable_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 2)
)
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingMemberVsTable.setStatus("current")
_WwpLeosRapsVirtualRingMemberVsEntry_Object = MibTableRow
wwpLeosRapsVirtualRingMemberVsEntry = _WwpLeosRapsVirtualRingMemberVsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 2, 1)
)
wwpLeosRapsVirtualRingMemberVsEntry.setIndexNames(
    (0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingIndex"),
    (0, "WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingMemberVsId"),
)
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingMemberVsEntry.setStatus("current")


class _WwpLeosRapsVirtualRingMemberVsId_Type(Integer32):
    """Custom type wwpLeosRapsVirtualRingMemberVsId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_WwpLeosRapsVirtualRingMemberVsId_Type.__name__ = "Integer32"
_WwpLeosRapsVirtualRingMemberVsId_Object = MibTableColumn
wwpLeosRapsVirtualRingMemberVsId = _WwpLeosRapsVirtualRingMemberVsId_Object(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 1, 4, 2, 1, 1),
    _WwpLeosRapsVirtualRingMemberVsId_Type()
)
wwpLeosRapsVirtualRingMemberVsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wwpLeosRapsVirtualRingMemberVsId.setStatus("current")
_WwpLeosRapsMIBNotificationPrefix_ObjectIdentity = ObjectIdentity
wwpLeosRapsMIBNotificationPrefix = _WwpLeosRapsMIBNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 2)
)
_WwpLeosRapsMIBNotifications_ObjectIdentity = ObjectIdentity
wwpLeosRapsMIBNotifications = _WwpLeosRapsMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 2, 0)
)
_WwpLeosRapsMIBConformance_ObjectIdentity = ObjectIdentity
wwpLeosRapsMIBConformance = _WwpLeosRapsMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 3)
)
_WwpLeosRapsMIBCompliances_ObjectIdentity = ObjectIdentity
wwpLeosRapsMIBCompliances = _WwpLeosRapsMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 3, 1)
)
_WwpLeosRapsMIBGroups_ObjectIdentity = ObjectIdentity
wwpLeosRapsMIBGroups = _WwpLeosRapsMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 3, 2)
)

# Managed Objects groups


# Notification objects

wwpLeosRapsAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 6141, 2, 60, 47, 2, 0, 1)
)
wwpLeosRapsAlarm.setObjects(
      *(("WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingName"),
        ("WWP-LEOS-RAPS-MIB", "wwpLeosRapsVirtualRingAlarm"))
)
if mibBuilder.loadTexts:
    wwpLeosRapsAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WWP-LEOS-RAPS-MIB",
    **{"wwpLeosRapsMIB": wwpLeosRapsMIB,
       "wwpLeosRapsMIBObjects": wwpLeosRapsMIBObjects,
       "wwpLeosRapsGlobal": wwpLeosRapsGlobal,
       "wwpLeosRapsGlobalAttrs": wwpLeosRapsGlobalAttrs,
       "wwpLeosRapsState": wwpLeosRapsState,
       "wwpLeosRapsNodeId": wwpLeosRapsNodeId,
       "wwpLeosRapsEtherType": wwpLeosRapsEtherType,
       "wwpLeosRapsNumberOfRings": wwpLeosRapsNumberOfRings,
       "wwpLeosRapsLogicalRing": wwpLeosRapsLogicalRing,
       "wwpLeosRapsLogicalRingTable": wwpLeosRapsLogicalRingTable,
       "wwpLeosRapsLogicalRingEntry": wwpLeosRapsLogicalRingEntry,
       "wwpLeosRapsLogicalRingIndex": wwpLeosRapsLogicalRingIndex,
       "wwpLeosRapsLogicalRingName": wwpLeosRapsLogicalRingName,
       "wwpLeosRapsLogicalRingId": wwpLeosRapsLogicalRingId,
       "wwpLeosRapsLogicalRingGuardTime": wwpLeosRapsLogicalRingGuardTime,
       "wwpLeosRapsLogicalRingWtr": wwpLeosRapsLogicalRingWtr,
       "wwpLeosRapsLogicalRingWtb": wwpLeosRapsLogicalRingWtb,
       "wwpLeosRapsLogicalRingWestPortId": wwpLeosRapsLogicalRingWestPortId,
       "wwpLeosRapsLogicalRingWestHoldOffTime": wwpLeosRapsLogicalRingWestHoldOffTime,
       "wwpLeosRapsLogicalRingWestForce": wwpLeosRapsLogicalRingWestForce,
       "wwpLeosRapsLogicalRingWestCfmService": wwpLeosRapsLogicalRingWestCfmService,
       "wwpLeosRapsLogicalRingEastPortId": wwpLeosRapsLogicalRingEastPortId,
       "wwpLeosRapsLogicalRingEastHoldOffTime": wwpLeosRapsLogicalRingEastHoldOffTime,
       "wwpLeosRapsLogicalRingEastForce": wwpLeosRapsLogicalRingEastForce,
       "wwpLeosRapsLogicalRingEastCfmService": wwpLeosRapsLogicalRingEastCfmService,
       "wwpLeosRapsLogicalRingNumberOfVirtualRings": wwpLeosRapsLogicalRingNumberOfVirtualRings,
       "wwpLeosRapsVirtualRing": wwpLeosRapsVirtualRing,
       "wwpLeosRapsVirtualRingTable": wwpLeosRapsVirtualRingTable,
       "wwpLeosRapsVirtualRingEntry": wwpLeosRapsVirtualRingEntry,
       "wwpLeosRapsVirtualRingIndex": wwpLeosRapsVirtualRingIndex,
       "wwpLeosRapsVirtualRingName": wwpLeosRapsVirtualRingName,
       "wwpLeosRapsVirtualRingVid": wwpLeosRapsVirtualRingVid,
       "wwpLeosRapsVirtualRingLogicalRingId": wwpLeosRapsVirtualRingLogicalRingId,
       "wwpLeosRapsVirtualRingMel": wwpLeosRapsVirtualRingMel,
       "wwpLeosRapsVirtualRingRevertive": wwpLeosRapsVirtualRingRevertive,
       "wwpLeosRapsVirtualRingState": wwpLeosRapsVirtualRingState,
       "wwpLeosRapsVirtualRingStatus": wwpLeosRapsVirtualRingStatus,
       "wwpLeosRapsVirtualRingAlarm": wwpLeosRapsVirtualRingAlarm,
       "wwpLeosRapsVirtualRingNumOfSwitchOvers": wwpLeosRapsVirtualRingNumOfSwitchOvers,
       "wwpLeosRapsVirtualRingUptimeFromLastFailure": wwpLeosRapsVirtualRingUptimeFromLastFailure,
       "wwpLeosRapsVirtualRingTotalDownTime": wwpLeosRapsVirtualRingTotalDownTime,
       "wwpLeosRapsVirtualRingWestPortRpl": wwpLeosRapsVirtualRingWestPortRpl,
       "wwpLeosRapsVirtualRingWestPortState": wwpLeosRapsVirtualRingWestPortState,
       "wwpLeosRapsVirtualRingWestPortStatus": wwpLeosRapsVirtualRingWestPortStatus,
       "wwpLeosRapsVirtualRingWestPortNrRxd": wwpLeosRapsVirtualRingWestPortNrRxd,
       "wwpLeosRapsVirtualRingWestPortNrTxd": wwpLeosRapsVirtualRingWestPortNrTxd,
       "wwpLeosRapsVirtualRingWestPortSfRxd": wwpLeosRapsVirtualRingWestPortSfRxd,
       "wwpLeosRapsVirtualRingWestPortSfTxd": wwpLeosRapsVirtualRingWestPortSfTxd,
       "wwpLeosRapsVirtualRingWestPortFsRxd": wwpLeosRapsVirtualRingWestPortFsRxd,
       "wwpLeosRapsVirtualRingWestPortFsTxd": wwpLeosRapsVirtualRingWestPortFsTxd,
       "wwpLeosRapsVirtualRingWestPortNrRbRxd": wwpLeosRapsVirtualRingWestPortNrRbRxd,
       "wwpLeosRapsVirtualRingWestPortNrRbTxd": wwpLeosRapsVirtualRingWestPortNrRbTxd,
       "wwpLeosRapsVirtualRingEastPortRpl": wwpLeosRapsVirtualRingEastPortRpl,
       "wwpLeosRapsVirtualRingEastPortState": wwpLeosRapsVirtualRingEastPortState,
       "wwpLeosRapsVirtualRingEastPortStatus": wwpLeosRapsVirtualRingEastPortStatus,
       "wwpLeosRapsVirtualRingEastPortNrRxd": wwpLeosRapsVirtualRingEastPortNrRxd,
       "wwpLeosRapsVirtualRingEastPortNrTxd": wwpLeosRapsVirtualRingEastPortNrTxd,
       "wwpLeosRapsVirtualRingEastPortSfRxd": wwpLeosRapsVirtualRingEastPortSfRxd,
       "wwpLeosRapsVirtualRingEastPortSfTxd": wwpLeosRapsVirtualRingEastPortSfTxd,
       "wwpLeosRapsVirtualRingEastPortFsRxd": wwpLeosRapsVirtualRingEastPortFsRxd,
       "wwpLeosRapsVirtualRingEastPortFsTxd": wwpLeosRapsVirtualRingEastPortFsTxd,
       "wwpLeosRapsVirtualRingEastPortNrRbRxd": wwpLeosRapsVirtualRingEastPortNrRbRxd,
       "wwpLeosRapsVirtualRingEastPortNrRbTxd": wwpLeosRapsVirtualRingEastPortNrRbTxd,
       "wwpLeosRapsVirtualRingType": wwpLeosRapsVirtualRingType,
       "wwpLeosRapsVirtualRingSubRingPortTerm": wwpLeosRapsVirtualRingSubRingPortTerm,
       "wwpLeosRapsVirtualRingMember": wwpLeosRapsVirtualRingMember,
       "wwpLeosRapsVirtualRingMemberTable": wwpLeosRapsVirtualRingMemberTable,
       "wwpLeosRapsVirtualRingMemberEntry": wwpLeosRapsVirtualRingMemberEntry,
       "wwpLeosRapsVirtualRingMemberVlanId": wwpLeosRapsVirtualRingMemberVlanId,
       "wwpLeosRapsVirtualRingMemberVsTable": wwpLeosRapsVirtualRingMemberVsTable,
       "wwpLeosRapsVirtualRingMemberVsEntry": wwpLeosRapsVirtualRingMemberVsEntry,
       "wwpLeosRapsVirtualRingMemberVsId": wwpLeosRapsVirtualRingMemberVsId,
       "wwpLeosRapsMIBNotificationPrefix": wwpLeosRapsMIBNotificationPrefix,
       "wwpLeosRapsMIBNotifications": wwpLeosRapsMIBNotifications,
       "wwpLeosRapsAlarm": wwpLeosRapsAlarm,
       "wwpLeosRapsMIBConformance": wwpLeosRapsMIBConformance,
       "wwpLeosRapsMIBCompliances": wwpLeosRapsMIBCompliances,
       "wwpLeosRapsMIBGroups": wwpLeosRapsMIBGroups}
)
