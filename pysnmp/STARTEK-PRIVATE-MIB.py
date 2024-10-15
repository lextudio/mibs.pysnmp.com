# SNMP MIB module (STARTEK-PRIVATE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/STARTEK-PRIVATE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:57:54 2024
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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Startek_ObjectIdentity = ObjectIdentity
startek = _Startek_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1)
)
_M828Series_ObjectIdentity = ObjectIdentity
m828Series = _M828Series_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 1)
)
_M828Hubs_ObjectIdentity = ObjectIdentity
m828Hubs = _M828Hubs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1)
)
_M828HubNumber_Type = Integer32
_M828HubNumber_Object = MibScalar
m828HubNumber = _M828HubNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 1),
    _M828HubNumber_Type()
)
m828HubNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubNumber.setStatus("mandatory")
_M828HubTable_Object = MibTable
m828HubTable = _M828HubTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    m828HubTable.setStatus("mandatory")
_M828HubTableEntry_Object = MibTableRow
m828HubTableEntry = _M828HubTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1)
)
m828HubTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "m828HubTableIndex"),
)
if mibBuilder.loadTexts:
    m828HubTableEntry.setStatus("mandatory")
_M828HubTableIndex_Type = Integer32
_M828HubTableIndex_Object = MibTableColumn
m828HubTableIndex = _M828HubTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 1),
    _M828HubTableIndex_Type()
)
m828HubTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubTableIndex.setStatus("mandatory")


class _M828HubModel_Type(Integer32):
    """Custom type m828HubModel based on Integer32"""
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
        *(("model-4", 1),
          ("model-5", 2),
          ("model-6", 3),
          ("model-7", 4))
    )


_M828HubModel_Type.__name__ = "Integer32"
_M828HubModel_Object = MibTableColumn
m828HubModel = _M828HubModel_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 2),
    _M828HubModel_Type()
)
m828HubModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubModel.setStatus("mandatory")


class _M828Hub485Address_Type(OctetString):
    """Custom type m828Hub485Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_M828Hub485Address_Type.__name__ = "OctetString"
_M828Hub485Address_Object = MibTableColumn
m828Hub485Address = _M828Hub485Address_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 3),
    _M828Hub485Address_Type()
)
m828Hub485Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828Hub485Address.setStatus("mandatory")


class _M828HubRiFTolSw_Type(Integer32):
    """Custom type m828HubRiFTolSw based on Integer32"""
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


_M828HubRiFTolSw_Type.__name__ = "Integer32"
_M828HubRiFTolSw_Object = MibTableColumn
m828HubRiFTolSw = _M828HubRiFTolSw_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 4),
    _M828HubRiFTolSw_Type()
)
m828HubRiFTolSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubRiFTolSw.setStatus("mandatory")


class _M828HubRiFTolState_Type(Integer32):
    """Custom type m828HubRiFTolState based on Integer32"""
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


_M828HubRiFTolState_Type.__name__ = "Integer32"
_M828HubRiFTolState_Object = MibTableColumn
m828HubRiFTolState = _M828HubRiFTolState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 5),
    _M828HubRiFTolState_Type()
)
m828HubRiFTolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m828HubRiFTolState.setStatus("mandatory")


class _M828HubRiMask_Type(Integer32):
    """Custom type m828HubRiMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("isolate", 1))
    )


_M828HubRiMask_Type.__name__ = "Integer32"
_M828HubRiMask_Object = MibTableColumn
m828HubRiMask = _M828HubRiMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 6),
    _M828HubRiMask_Type()
)
m828HubRiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m828HubRiMask.setStatus("mandatory")


class _M828HubRiPhDet_Type(Integer32):
    """Custom type m828HubRiPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_M828HubRiPhDet_Type.__name__ = "Integer32"
_M828HubRiPhDet_Object = MibTableColumn
m828HubRiPhDet = _M828HubRiPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 7),
    _M828HubRiPhDet_Type()
)
m828HubRiPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubRiPhDet.setStatus("mandatory")


class _M828HubRiNsrtStatus_Type(Integer32):
    """Custom type m828HubRiNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_M828HubRiNsrtStatus_Type.__name__ = "Integer32"
_M828HubRiNsrtStatus_Object = MibTableColumn
m828HubRiNsrtStatus = _M828HubRiNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 8),
    _M828HubRiNsrtStatus_Type()
)
m828HubRiNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubRiNsrtStatus.setStatus("mandatory")


class _M828HubRiBcnRemStatus_Type(Integer32):
    """Custom type m828HubRiBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1))
    )


_M828HubRiBcnRemStatus_Type.__name__ = "Integer32"
_M828HubRiBcnRemStatus_Object = MibTableColumn
m828HubRiBcnRemStatus = _M828HubRiBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 9),
    _M828HubRiBcnRemStatus_Type()
)
m828HubRiBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubRiBcnRemStatus.setStatus("mandatory")


class _M828RiNeighborType_Type(Integer32):
    """Custom type m828RiNeighborType based on Integer32"""
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
        *(("fSeries", 2),
          ("none", 4),
          ("series828", 1),
          ("stackable", 5),
          ("tokenRingMAC", 3))
    )


_M828RiNeighborType_Type.__name__ = "Integer32"
_M828RiNeighborType_Object = MibTableColumn
m828RiNeighborType = _M828RiNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 10),
    _M828RiNeighborType_Type()
)
m828RiNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828RiNeighborType.setStatus("mandatory")


class _M828RiNeighborAddr_Type(OctetString):
    """Custom type m828RiNeighborAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 6),
    )


_M828RiNeighborAddr_Type.__name__ = "OctetString"
_M828RiNeighborAddr_Object = MibTableColumn
m828RiNeighborAddr = _M828RiNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 11),
    _M828RiNeighborAddr_Type()
)
m828RiNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828RiNeighborAddr.setStatus("mandatory")
_M828RiTimeStamp_Type = TimeTicks
_M828RiTimeStamp_Object = MibTableColumn
m828RiTimeStamp = _M828RiTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 12),
    _M828RiTimeStamp_Type()
)
m828RiTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828RiTimeStamp.setStatus("mandatory")


class _M828HubRoFTolSw_Type(Integer32):
    """Custom type m828HubRoFTolSw based on Integer32"""
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


_M828HubRoFTolSw_Type.__name__ = "Integer32"
_M828HubRoFTolSw_Object = MibTableColumn
m828HubRoFTolSw = _M828HubRoFTolSw_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 13),
    _M828HubRoFTolSw_Type()
)
m828HubRoFTolSw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubRoFTolSw.setStatus("mandatory")


class _M828HubRoFTolState_Type(Integer32):
    """Custom type m828HubRoFTolState based on Integer32"""
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


_M828HubRoFTolState_Type.__name__ = "Integer32"
_M828HubRoFTolState_Object = MibTableColumn
m828HubRoFTolState = _M828HubRoFTolState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 14),
    _M828HubRoFTolState_Type()
)
m828HubRoFTolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m828HubRoFTolState.setStatus("mandatory")


class _M828HubRoMask_Type(Integer32):
    """Custom type m828HubRoMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("isolate", 1))
    )


_M828HubRoMask_Type.__name__ = "Integer32"
_M828HubRoMask_Object = MibTableColumn
m828HubRoMask = _M828HubRoMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 15),
    _M828HubRoMask_Type()
)
m828HubRoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m828HubRoMask.setStatus("mandatory")


class _M828HubRoPhDet_Type(Integer32):
    """Custom type m828HubRoPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("phantOk", 2),
          ("wireFault", 1))
    )


_M828HubRoPhDet_Type.__name__ = "Integer32"
_M828HubRoPhDet_Object = MibTableColumn
m828HubRoPhDet = _M828HubRoPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 16),
    _M828HubRoPhDet_Type()
)
m828HubRoPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubRoPhDet.setStatus("mandatory")


class _M828HubRoNsrtStatus_Type(Integer32):
    """Custom type m828HubRoNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_M828HubRoNsrtStatus_Type.__name__ = "Integer32"
_M828HubRoNsrtStatus_Object = MibTableColumn
m828HubRoNsrtStatus = _M828HubRoNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 17),
    _M828HubRoNsrtStatus_Type()
)
m828HubRoNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubRoNsrtStatus.setStatus("mandatory")


class _M828HubRoBcnRemStatus_Type(Integer32):
    """Custom type m828HubRoBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1))
    )


_M828HubRoBcnRemStatus_Type.__name__ = "Integer32"
_M828HubRoBcnRemStatus_Object = MibTableColumn
m828HubRoBcnRemStatus = _M828HubRoBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 18),
    _M828HubRoBcnRemStatus_Type()
)
m828HubRoBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubRoBcnRemStatus.setStatus("mandatory")


class _M828RoNeighborType_Type(Integer32):
    """Custom type m828RoNeighborType based on Integer32"""
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
        *(("fSeries", 2),
          ("none", 4),
          ("series828", 1),
          ("stackable", 5),
          ("tokenRingMAC", 3))
    )


_M828RoNeighborType_Type.__name__ = "Integer32"
_M828RoNeighborType_Object = MibTableColumn
m828RoNeighborType = _M828RoNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 19),
    _M828RoNeighborType_Type()
)
m828RoNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828RoNeighborType.setStatus("mandatory")


class _M828RoNeighborAddr_Type(OctetString):
    """Custom type m828RoNeighborAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 6),
    )


_M828RoNeighborAddr_Type.__name__ = "OctetString"
_M828RoNeighborAddr_Object = MibTableColumn
m828RoNeighborAddr = _M828RoNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 20),
    _M828RoNeighborAddr_Type()
)
m828RoNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828RoNeighborAddr.setStatus("mandatory")
_M828RoTimeStamp_Type = TimeTicks
_M828RoTimeStamp_Object = MibTableColumn
m828RoTimeStamp = _M828RoTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 21),
    _M828RoTimeStamp_Type()
)
m828RoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828RoTimeStamp.setStatus("mandatory")


class _M828HubDataRateSwitch_Type(Integer32):
    """Custom type m828HubDataRateSwitch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noSwitch", 3),
          ("s16Mbps", 2),
          ("s4Mbps", 1))
    )


_M828HubDataRateSwitch_Type.__name__ = "Integer32"
_M828HubDataRateSwitch_Object = MibTableColumn
m828HubDataRateSwitch = _M828HubDataRateSwitch_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 22),
    _M828HubDataRateSwitch_Type()
)
m828HubDataRateSwitch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubDataRateSwitch.setStatus("mandatory")


class _M828HubDataRateState_Type(Integer32):
    """Custom type m828HubDataRateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoConfig", 3),
          ("s16Mbps", 2),
          ("s4Mbps", 1))
    )


_M828HubDataRateState_Type.__name__ = "Integer32"
_M828HubDataRateState_Object = MibTableColumn
m828HubDataRateState = _M828HubDataRateState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 23),
    _M828HubDataRateState_Type()
)
m828HubDataRateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m828HubDataRateState.setStatus("mandatory")
_M828HubDataRateTimeStamp_Type = TimeTicks
_M828HubDataRateTimeStamp_Object = MibTableColumn
m828HubDataRateTimeStamp = _M828HubDataRateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 24),
    _M828HubDataRateTimeStamp_Type()
)
m828HubDataRateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubDataRateTimeStamp.setStatus("mandatory")


class _M828HubMgmtStatus_Type(Integer32):
    """Custom type m828HubMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("operational", 1))
    )


_M828HubMgmtStatus_Type.__name__ = "Integer32"
_M828HubMgmtStatus_Object = MibTableColumn
m828HubMgmtStatus = _M828HubMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 25),
    _M828HubMgmtStatus_Type()
)
m828HubMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubMgmtStatus.setStatus("mandatory")


class _M828HubProxyAgentID_Type(OctetString):
    """Custom type m828HubProxyAgentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_M828HubProxyAgentID_Type.__name__ = "OctetString"
_M828HubProxyAgentID_Object = MibTableColumn
m828HubProxyAgentID = _M828HubProxyAgentID_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 26),
    _M828HubProxyAgentID_Type()
)
m828HubProxyAgentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubProxyAgentID.setStatus("mandatory")


class _M828HubCodeVersion_Type(OctetString):
    """Custom type m828HubCodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_M828HubCodeVersion_Type.__name__ = "OctetString"
_M828HubCodeVersion_Object = MibTableColumn
m828HubCodeVersion = _M828HubCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 27),
    _M828HubCodeVersion_Type()
)
m828HubCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubCodeVersion.setStatus("mandatory")


class _M828HubRawCommandData_Type(OctetString):
    """Custom type m828HubRawCommandData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_M828HubRawCommandData_Type.__name__ = "OctetString"
_M828HubRawCommandData_Object = MibTableColumn
m828HubRawCommandData = _M828HubRawCommandData_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 2, 1, 28),
    _M828HubRawCommandData_Type()
)
m828HubRawCommandData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m828HubRawCommandData.setStatus("mandatory")
_M828HubLobeNumber_Type = Integer32
_M828HubLobeNumber_Object = MibScalar
m828HubLobeNumber = _M828HubLobeNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 3),
    _M828HubLobeNumber_Type()
)
m828HubLobeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubLobeNumber.setStatus("mandatory")
_M828HubLobeTable_Object = MibTable
m828HubLobeTable = _M828HubLobeTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    m828HubLobeTable.setStatus("mandatory")
_M828HubLobeEntry_Object = MibTableRow
m828HubLobeEntry = _M828HubLobeEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 4, 1)
)
m828HubLobeEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "m828HubIndex"),
    (0, "STARTEK-PRIVATE-MIB", "m828HubLobePort"),
)
if mibBuilder.loadTexts:
    m828HubLobeEntry.setStatus("mandatory")
_M828HubIndex_Type = Integer32
_M828HubIndex_Object = MibTableColumn
m828HubIndex = _M828HubIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 4, 1, 1),
    _M828HubIndex_Type()
)
m828HubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubIndex.setStatus("mandatory")
_M828HubLobePort_Type = Integer32
_M828HubLobePort_Object = MibTableColumn
m828HubLobePort = _M828HubLobePort_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 4, 1, 2),
    _M828HubLobePort_Type()
)
m828HubLobePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubLobePort.setStatus("mandatory")


class _M828HubLobePhDet_Type(Integer32):
    """Custom type m828HubLobePhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_M828HubLobePhDet_Type.__name__ = "Integer32"
_M828HubLobePhDet_Object = MibTableColumn
m828HubLobePhDet = _M828HubLobePhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 4, 1, 3),
    _M828HubLobePhDet_Type()
)
m828HubLobePhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubLobePhDet.setStatus("mandatory")


class _M828HubLobeMask_Type(Integer32):
    """Custom type m828HubLobeMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("isolated", 1))
    )


_M828HubLobeMask_Type.__name__ = "Integer32"
_M828HubLobeMask_Object = MibTableColumn
m828HubLobeMask = _M828HubLobeMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 4, 1, 4),
    _M828HubLobeMask_Type()
)
m828HubLobeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    m828HubLobeMask.setStatus("mandatory")


class _M828HubLobeNsrtStatus_Type(Integer32):
    """Custom type m828HubLobeNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_M828HubLobeNsrtStatus_Type.__name__ = "Integer32"
_M828HubLobeNsrtStatus_Object = MibTableColumn
m828HubLobeNsrtStatus = _M828HubLobeNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 4, 1, 5),
    _M828HubLobeNsrtStatus_Type()
)
m828HubLobeNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubLobeNsrtStatus.setStatus("mandatory")


class _M828HubLobeMacAddr_Type(OctetString):
    """Custom type m828HubLobeMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_M828HubLobeMacAddr_Type.__name__ = "OctetString"
_M828HubLobeMacAddr_Object = MibTableColumn
m828HubLobeMacAddr = _M828HubLobeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 4, 1, 6),
    _M828HubLobeMacAddr_Type()
)
m828HubLobeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubLobeMacAddr.setStatus("mandatory")


class _M828HubLobeBcnRemStatus_Type(Integer32):
    """Custom type m828HubLobeBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_M828HubLobeBcnRemStatus_Type.__name__ = "Integer32"
_M828HubLobeBcnRemStatus_Object = MibTableColumn
m828HubLobeBcnRemStatus = _M828HubLobeBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 4, 1, 7),
    _M828HubLobeBcnRemStatus_Type()
)
m828HubLobeBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubLobeBcnRemStatus.setStatus("mandatory")
_M828HubLobeTimeStamp_Type = TimeTicks
_M828HubLobeTimeStamp_Object = MibTableColumn
m828HubLobeTimeStamp = _M828HubLobeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 1, 1, 4, 1, 8),
    _M828HubLobeTimeStamp_Type()
)
m828HubLobeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    m828HubLobeTimeStamp.setStatus("mandatory")
_FSeries_ObjectIdentity = ObjectIdentity
fSeries = _FSeries_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 2)
)
_FChassis_ObjectIdentity = ObjectIdentity
fChassis = _FChassis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 1)
)
_FChassisNumber_Type = Integer32
_FChassisNumber_Object = MibScalar
fChassisNumber = _FChassisNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 1, 1),
    _FChassisNumber_Type()
)
fChassisNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fChassisNumber.setStatus("mandatory")
_FChassisTable_Object = MibTable
fChassisTable = _FChassisTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 1, 2)
)
if mibBuilder.loadTexts:
    fChassisTable.setStatus("mandatory")
_FChassisTableEntry_Object = MibTableRow
fChassisTableEntry = _FChassisTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 1, 2, 1)
)
fChassisTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "fChassisIndex"),
)
if mibBuilder.loadTexts:
    fChassisTableEntry.setStatus("mandatory")
_FChassisIndex_Type = Integer32
_FChassisIndex_Object = MibTableColumn
fChassisIndex = _FChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 1, 2, 1, 1),
    _FChassisIndex_Type()
)
fChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fChassisIndex.setStatus("mandatory")


class _FChassisModel_Type(Integer32):
    """Custom type fChassisModel based on Integer32"""
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
        *(("fiveslot-10101", 2),
          ("fiveslotredundant-10102", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("twoslot-10100", 1))
    )


_FChassisModel_Type.__name__ = "Integer32"
_FChassisModel_Object = MibTableColumn
fChassisModel = _FChassisModel_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 1, 2, 1, 2),
    _FChassisModel_Type()
)
fChassisModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fChassisModel.setStatus("mandatory")


class _FChassisPowStatus_Type(Integer32):
    """Custom type fChassisPowStatus based on Integer32"""
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
        *(("dualSup-ASupBAD", 4),
          ("dualSup-BSupBAD", 3),
          ("dualSupOK", 2),
          ("illegal", 5),
          ("singleSupOK", 1))
    )


_FChassisPowStatus_Type.__name__ = "Integer32"
_FChassisPowStatus_Object = MibTableColumn
fChassisPowStatus = _FChassisPowStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 1, 2, 1, 3),
    _FChassisPowStatus_Type()
)
fChassisPowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fChassisPowStatus.setStatus("mandatory")


class _FChassisLocation_Type(Integer32):
    """Custom type fChassisLocation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("local", 1))
    )


_FChassisLocation_Type.__name__ = "Integer32"
_FChassisLocation_Object = MibTableColumn
fChassisLocation = _FChassisLocation_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 1, 2, 1, 4),
    _FChassisLocation_Type()
)
fChassisLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fChassisLocation.setStatus("mandatory")
_FTRMainRing_ObjectIdentity = ObjectIdentity
fTRMainRing = _FTRMainRing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2)
)
_FTRMainRingNumber_Type = Integer32
_FTRMainRingNumber_Object = MibScalar
fTRMainRingNumber = _FTRMainRingNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 1),
    _FTRMainRingNumber_Type()
)
fTRMainRingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingNumber.setStatus("mandatory")
_FTRMainRingTable_Object = MibTable
fTRMainRingTable = _FTRMainRingTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    fTRMainRingTable.setStatus("mandatory")
_FTRMainRingTableEntry_Object = MibTableRow
fTRMainRingTableEntry = _FTRMainRingTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1)
)
fTRMainRingTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "fTRMainRingTableIndex"),
)
if mibBuilder.loadTexts:
    fTRMainRingTableEntry.setStatus("mandatory")
_FTRMainRingTableIndex_Type = Integer32
_FTRMainRingTableIndex_Object = MibTableColumn
fTRMainRingTableIndex = _FTRMainRingTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 1),
    _FTRMainRingTableIndex_Type()
)
fTRMainRingTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingTableIndex.setStatus("mandatory")


class _FTRMainRingModel_Type(Integer32):
    """Custom type fTRMainRingModel based on Integer32"""
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
        *(("f10150RiRoExpModuleAgent", 3),
          ("f10151RiRoFiberExpModuleAgent", 4),
          ("f10154RiRoExpModule", 1),
          ("f10155RiRoFiberExpModule", 2))
    )


_FTRMainRingModel_Type.__name__ = "Integer32"
_FTRMainRingModel_Object = MibTableColumn
fTRMainRingModel = _FTRMainRingModel_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 2),
    _FTRMainRingModel_Type()
)
fTRMainRingModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingModel.setStatus("mandatory")


class _FTRMainRing485Address_Type(OctetString):
    """Custom type fTRMainRing485Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_FTRMainRing485Address_Type.__name__ = "OctetString"
_FTRMainRing485Address_Object = MibTableColumn
fTRMainRing485Address = _FTRMainRing485Address_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 3),
    _FTRMainRing485Address_Type()
)
fTRMainRing485Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRing485Address.setStatus("mandatory")
_FTRMainRingSlotIndex_Type = Integer32
_FTRMainRingSlotIndex_Object = MibTableColumn
fTRMainRingSlotIndex = _FTRMainRingSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 4),
    _FTRMainRingSlotIndex_Type()
)
fTRMainRingSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingSlotIndex.setStatus("mandatory")
_FTRMainRingChassisIndex_Type = Integer32
_FTRMainRingChassisIndex_Object = MibTableColumn
fTRMainRingChassisIndex = _FTRMainRingChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 5),
    _FTRMainRingChassisIndex_Type()
)
fTRMainRingChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingChassisIndex.setStatus("mandatory")


class _FTRMainRingRiFTolState_Type(Integer32):
    """Custom type fTRMainRingRiFTolState based on Integer32"""
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


_FTRMainRingRiFTolState_Type.__name__ = "Integer32"
_FTRMainRingRiFTolState_Object = MibTableColumn
fTRMainRingRiFTolState = _FTRMainRingRiFTolState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 6),
    _FTRMainRingRiFTolState_Type()
)
fTRMainRingRiFTolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingRiFTolState.setStatus("mandatory")


class _FTRMainRingRiMask_Type(Integer32):
    """Custom type fTRMainRingRiMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("isolate", 1))
    )


_FTRMainRingRiMask_Type.__name__ = "Integer32"
_FTRMainRingRiMask_Object = MibTableColumn
fTRMainRingRiMask = _FTRMainRingRiMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 7),
    _FTRMainRingRiMask_Type()
)
fTRMainRingRiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingRiMask.setStatus("mandatory")


class _FTRMainRingRiPhDet_Type(Integer32):
    """Custom type fTRMainRingRiPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_FTRMainRingRiPhDet_Type.__name__ = "Integer32"
_FTRMainRingRiPhDet_Object = MibTableColumn
fTRMainRingRiPhDet = _FTRMainRingRiPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 8),
    _FTRMainRingRiPhDet_Type()
)
fTRMainRingRiPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRiPhDet.setStatus("mandatory")


class _FTRMainRingRiNsrtStatus_Type(Integer32):
    """Custom type fTRMainRingRiNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_FTRMainRingRiNsrtStatus_Type.__name__ = "Integer32"
_FTRMainRingRiNsrtStatus_Object = MibTableColumn
fTRMainRingRiNsrtStatus = _FTRMainRingRiNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 9),
    _FTRMainRingRiNsrtStatus_Type()
)
fTRMainRingRiNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRiNsrtStatus.setStatus("mandatory")


class _FTRMainRingRiBcnRemStatus_Type(Integer32):
    """Custom type fTRMainRingRiBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1))
    )


_FTRMainRingRiBcnRemStatus_Type.__name__ = "Integer32"
_FTRMainRingRiBcnRemStatus_Object = MibTableColumn
fTRMainRingRiBcnRemStatus = _FTRMainRingRiBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 10),
    _FTRMainRingRiBcnRemStatus_Type()
)
fTRMainRingRiBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRiBcnRemStatus.setStatus("mandatory")


class _FTRMainRingRiCableType_Type(Integer32):
    """Custom type fTRMainRingRiCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_FTRMainRingRiCableType_Type.__name__ = "Integer32"
_FTRMainRingRiCableType_Object = MibTableColumn
fTRMainRingRiCableType = _FTRMainRingRiCableType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 11),
    _FTRMainRingRiCableType_Type()
)
fTRMainRingRiCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRiCableType.setStatus("mandatory")


class _FTRMainRingRiNghbrType_Type(Integer32):
    """Custom type fTRMainRingRiNghbrType based on Integer32"""
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
        *(("fSeries", 2),
          ("none", 4),
          ("series828", 1),
          ("stackable", 5),
          ("tokenRingMAC", 3))
    )


_FTRMainRingRiNghbrType_Type.__name__ = "Integer32"
_FTRMainRingRiNghbrType_Object = MibTableColumn
fTRMainRingRiNghbrType = _FTRMainRingRiNghbrType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 12),
    _FTRMainRingRiNghbrType_Type()
)
fTRMainRingRiNghbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRiNghbrType.setStatus("mandatory")


class _FTRMainRingRiNghbrAddr_Type(OctetString):
    """Custom type fTRMainRingRiNghbrAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 6),
    )


_FTRMainRingRiNghbrAddr_Type.__name__ = "OctetString"
_FTRMainRingRiNghbrAddr_Object = MibTableColumn
fTRMainRingRiNghbrAddr = _FTRMainRingRiNghbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 13),
    _FTRMainRingRiNghbrAddr_Type()
)
fTRMainRingRiNghbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRiNghbrAddr.setStatus("mandatory")
_FTRMainRingRiTimeStamp_Type = TimeTicks
_FTRMainRingRiTimeStamp_Object = MibTableColumn
fTRMainRingRiTimeStamp = _FTRMainRingRiTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 14),
    _FTRMainRingRiTimeStamp_Type()
)
fTRMainRingRiTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRiTimeStamp.setStatus("mandatory")


class _FTRMainRingRoFTolState_Type(Integer32):
    """Custom type fTRMainRingRoFTolState based on Integer32"""
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


_FTRMainRingRoFTolState_Type.__name__ = "Integer32"
_FTRMainRingRoFTolState_Object = MibTableColumn
fTRMainRingRoFTolState = _FTRMainRingRoFTolState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 15),
    _FTRMainRingRoFTolState_Type()
)
fTRMainRingRoFTolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingRoFTolState.setStatus("mandatory")


class _FTRMainRingRoMask_Type(Integer32):
    """Custom type fTRMainRingRoMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("isolate", 1))
    )


_FTRMainRingRoMask_Type.__name__ = "Integer32"
_FTRMainRingRoMask_Object = MibTableColumn
fTRMainRingRoMask = _FTRMainRingRoMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 16),
    _FTRMainRingRoMask_Type()
)
fTRMainRingRoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingRoMask.setStatus("mandatory")


class _FTRMainRingRoPhDet_Type(Integer32):
    """Custom type fTRMainRingRoPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("phantOk", 2),
          ("wireFault", 1))
    )


_FTRMainRingRoPhDet_Type.__name__ = "Integer32"
_FTRMainRingRoPhDet_Object = MibTableColumn
fTRMainRingRoPhDet = _FTRMainRingRoPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 17),
    _FTRMainRingRoPhDet_Type()
)
fTRMainRingRoPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRoPhDet.setStatus("mandatory")


class _FTRMainRingRoNsrtStatus_Type(Integer32):
    """Custom type fTRMainRingRoNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_FTRMainRingRoNsrtStatus_Type.__name__ = "Integer32"
_FTRMainRingRoNsrtStatus_Object = MibTableColumn
fTRMainRingRoNsrtStatus = _FTRMainRingRoNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 18),
    _FTRMainRingRoNsrtStatus_Type()
)
fTRMainRingRoNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRoNsrtStatus.setStatus("mandatory")


class _FTRMainRingRoBcnRemStatus_Type(Integer32):
    """Custom type fTRMainRingRoBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1))
    )


_FTRMainRingRoBcnRemStatus_Type.__name__ = "Integer32"
_FTRMainRingRoBcnRemStatus_Object = MibTableColumn
fTRMainRingRoBcnRemStatus = _FTRMainRingRoBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 19),
    _FTRMainRingRoBcnRemStatus_Type()
)
fTRMainRingRoBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRoBcnRemStatus.setStatus("mandatory")


class _FTRMainRingRoCableType_Type(Integer32):
    """Custom type fTRMainRingRoCableType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("copper", 1),
          ("fiber", 2))
    )


_FTRMainRingRoCableType_Type.__name__ = "Integer32"
_FTRMainRingRoCableType_Object = MibTableColumn
fTRMainRingRoCableType = _FTRMainRingRoCableType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 20),
    _FTRMainRingRoCableType_Type()
)
fTRMainRingRoCableType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRoCableType.setStatus("mandatory")


class _FTRMainRingRoNghbrType_Type(Integer32):
    """Custom type fTRMainRingRoNghbrType based on Integer32"""
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
        *(("fSeries", 2),
          ("none", 4),
          ("series828", 1),
          ("stackable", 5),
          ("tokenRingMAC", 3))
    )


_FTRMainRingRoNghbrType_Type.__name__ = "Integer32"
_FTRMainRingRoNghbrType_Object = MibTableColumn
fTRMainRingRoNghbrType = _FTRMainRingRoNghbrType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 21),
    _FTRMainRingRoNghbrType_Type()
)
fTRMainRingRoNghbrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRoNghbrType.setStatus("mandatory")


class _FTRMainRingRoNghbrAddr_Type(OctetString):
    """Custom type fTRMainRingRoNghbrAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 6),
    )


_FTRMainRingRoNghbrAddr_Type.__name__ = "OctetString"
_FTRMainRingRoNghbrAddr_Object = MibTableColumn
fTRMainRingRoNghbrAddr = _FTRMainRingRoNghbrAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 22),
    _FTRMainRingRoNghbrAddr_Type()
)
fTRMainRingRoNghbrAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRoNghbrAddr.setStatus("mandatory")
_FTRMainRingRoTimeStamp_Type = TimeTicks
_FTRMainRingRoTimeStamp_Object = MibTableColumn
fTRMainRingRoTimeStamp = _FTRMainRingRoTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 23),
    _FTRMainRingRoTimeStamp_Type()
)
fTRMainRingRoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingRoTimeStamp.setStatus("mandatory")


class _FTRMainRingDataRateState_Type(Integer32):
    """Custom type fTRMainRingDataRateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s16Mbps", 2),
          ("s4Mbps", 1))
    )


_FTRMainRingDataRateState_Type.__name__ = "Integer32"
_FTRMainRingDataRateState_Object = MibTableColumn
fTRMainRingDataRateState = _FTRMainRingDataRateState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 24),
    _FTRMainRingDataRateState_Type()
)
fTRMainRingDataRateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingDataRateState.setStatus("mandatory")
_FTRMainRingDataRateTimeStamp_Type = TimeTicks
_FTRMainRingDataRateTimeStamp_Object = MibTableColumn
fTRMainRingDataRateTimeStamp = _FTRMainRingDataRateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 25),
    _FTRMainRingDataRateTimeStamp_Type()
)
fTRMainRingDataRateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingDataRateTimeStamp.setStatus("mandatory")


class _FTRMainRingBkPlnNsrtState_Type(Integer32):
    """Custom type fTRMainRingBkPlnNsrtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 2),
          ("inserted", 1))
    )


_FTRMainRingBkPlnNsrtState_Type.__name__ = "Integer32"
_FTRMainRingBkPlnNsrtState_Object = MibTableColumn
fTRMainRingBkPlnNsrtState = _FTRMainRingBkPlnNsrtState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 26),
    _FTRMainRingBkPlnNsrtState_Type()
)
fTRMainRingBkPlnNsrtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingBkPlnNsrtState.setStatus("mandatory")
_FTRMainRingBkPlnTimeStamp_Type = TimeTicks
_FTRMainRingBkPlnTimeStamp_Object = MibTableColumn
fTRMainRingBkPlnTimeStamp = _FTRMainRingBkPlnTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 27),
    _FTRMainRingBkPlnTimeStamp_Type()
)
fTRMainRingBkPlnTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingBkPlnTimeStamp.setStatus("mandatory")


class _FTRMainRingLobePhDet_Type(Integer32):
    """Custom type fTRMainRingLobePhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_FTRMainRingLobePhDet_Type.__name__ = "Integer32"
_FTRMainRingLobePhDet_Object = MibTableColumn
fTRMainRingLobePhDet = _FTRMainRingLobePhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 28),
    _FTRMainRingLobePhDet_Type()
)
fTRMainRingLobePhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingLobePhDet.setStatus("mandatory")


class _FTRMainRingLobeMask_Type(Integer32):
    """Custom type fTRMainRingLobeMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("isolated", 1))
    )


_FTRMainRingLobeMask_Type.__name__ = "Integer32"
_FTRMainRingLobeMask_Object = MibTableColumn
fTRMainRingLobeMask = _FTRMainRingLobeMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 29),
    _FTRMainRingLobeMask_Type()
)
fTRMainRingLobeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingLobeMask.setStatus("mandatory")


class _FTRMainRingLobeNsrtStatus_Type(Integer32):
    """Custom type fTRMainRingLobeNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_FTRMainRingLobeNsrtStatus_Type.__name__ = "Integer32"
_FTRMainRingLobeNsrtStatus_Object = MibTableColumn
fTRMainRingLobeNsrtStatus = _FTRMainRingLobeNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 30),
    _FTRMainRingLobeNsrtStatus_Type()
)
fTRMainRingLobeNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingLobeNsrtStatus.setStatus("mandatory")


class _FTRMainRingLobeMacAddr_Type(OctetString):
    """Custom type fTRMainRingLobeMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_FTRMainRingLobeMacAddr_Type.__name__ = "OctetString"
_FTRMainRingLobeMacAddr_Object = MibTableColumn
fTRMainRingLobeMacAddr = _FTRMainRingLobeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 31),
    _FTRMainRingLobeMacAddr_Type()
)
fTRMainRingLobeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingLobeMacAddr.setStatus("mandatory")


class _FTRMainRingLobeBcnRemStatus_Type(Integer32):
    """Custom type fTRMainRingLobeBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_FTRMainRingLobeBcnRemStatus_Type.__name__ = "Integer32"
_FTRMainRingLobeBcnRemStatus_Object = MibTableColumn
fTRMainRingLobeBcnRemStatus = _FTRMainRingLobeBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 32),
    _FTRMainRingLobeBcnRemStatus_Type()
)
fTRMainRingLobeBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingLobeBcnRemStatus.setStatus("mandatory")
_FTRMainRingLobeTimeStamp_Type = TimeTicks
_FTRMainRingLobeTimeStamp_Object = MibTableColumn
fTRMainRingLobeTimeStamp = _FTRMainRingLobeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 33),
    _FTRMainRingLobeTimeStamp_Type()
)
fTRMainRingLobeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingLobeTimeStamp.setStatus("mandatory")


class _FTRMainRingMgmtStatus_Type(Integer32):
    """Custom type fTRMainRingMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("operational", 1))
    )


_FTRMainRingMgmtStatus_Type.__name__ = "Integer32"
_FTRMainRingMgmtStatus_Object = MibTableColumn
fTRMainRingMgmtStatus = _FTRMainRingMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 34),
    _FTRMainRingMgmtStatus_Type()
)
fTRMainRingMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingMgmtStatus.setStatus("mandatory")


class _FTRMainRingProxyAgentID_Type(OctetString):
    """Custom type fTRMainRingProxyAgentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_FTRMainRingProxyAgentID_Type.__name__ = "OctetString"
_FTRMainRingProxyAgentID_Object = MibTableColumn
fTRMainRingProxyAgentID = _FTRMainRingProxyAgentID_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 35),
    _FTRMainRingProxyAgentID_Type()
)
fTRMainRingProxyAgentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingProxyAgentID.setStatus("mandatory")


class _FTRMainRingAttachedAgentType_Type(Integer32):
    """Custom type fTRMainRingAttachedAgentType based on Integer32"""
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
        *(("none", 4),
          ("reserved", 3),
          ("tokenring", 1),
          ("tokenring-ethernet", 2))
    )


_FTRMainRingAttachedAgentType_Type.__name__ = "Integer32"
_FTRMainRingAttachedAgentType_Object = MibTableColumn
fTRMainRingAttachedAgentType = _FTRMainRingAttachedAgentType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 36),
    _FTRMainRingAttachedAgentType_Type()
)
fTRMainRingAttachedAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingAttachedAgentType.setStatus("mandatory")


class _FTRMainRingAttachedAgentState_Type(Integer32):
    """Custom type fTRMainRingAttachedAgentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-applicable", 3))
    )


_FTRMainRingAttachedAgentState_Type.__name__ = "Integer32"
_FTRMainRingAttachedAgentState_Object = MibTableColumn
fTRMainRingAttachedAgentState = _FTRMainRingAttachedAgentState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 37),
    _FTRMainRingAttachedAgentState_Type()
)
fTRMainRingAttachedAgentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingAttachedAgentState.setStatus("mandatory")


class _FTRMainRingTemperatureStatus_Type(Integer32):
    """Custom type fTRMainRingTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("ok", 1))
    )


_FTRMainRingTemperatureStatus_Type.__name__ = "Integer32"
_FTRMainRingTemperatureStatus_Object = MibTableColumn
fTRMainRingTemperatureStatus = _FTRMainRingTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 38),
    _FTRMainRingTemperatureStatus_Type()
)
fTRMainRingTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingTemperatureStatus.setStatus("mandatory")


class _FTRMainRingAutoRecovControl_Type(Integer32):
    """Custom type fTRMainRingAutoRecovControl based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("reset", 3),
          ("unknown", 4))
    )


_FTRMainRingAutoRecovControl_Type.__name__ = "Integer32"
_FTRMainRingAutoRecovControl_Object = MibTableColumn
fTRMainRingAutoRecovControl = _FTRMainRingAutoRecovControl_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 39),
    _FTRMainRingAutoRecovControl_Type()
)
fTRMainRingAutoRecovControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingAutoRecovControl.setStatus("mandatory")


class _FTRMainRingAutoRecovRetries_Type(Integer32):
    """Custom type fTRMainRingAutoRecovRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FTRMainRingAutoRecovRetries_Type.__name__ = "Integer32"
_FTRMainRingAutoRecovRetries_Object = MibTableColumn
fTRMainRingAutoRecovRetries = _FTRMainRingAutoRecovRetries_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 40),
    _FTRMainRingAutoRecovRetries_Type()
)
fTRMainRingAutoRecovRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingAutoRecovRetries.setStatus("mandatory")


class _FTRMainRingCodeVersion_Type(OctetString):
    """Custom type fTRMainRingCodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FTRMainRingCodeVersion_Type.__name__ = "OctetString"
_FTRMainRingCodeVersion_Object = MibTableColumn
fTRMainRingCodeVersion = _FTRMainRingCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 41),
    _FTRMainRingCodeVersion_Type()
)
fTRMainRingCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingCodeVersion.setStatus("mandatory")


class _FTRMainRingAutoRecovState_Type(Integer32):
    """Custom type fTRMainRingAutoRecovState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("halted", 3),
          ("in-recovery", 1),
          ("normal", 2))
    )


_FTRMainRingAutoRecovState_Type.__name__ = "Integer32"
_FTRMainRingAutoRecovState_Object = MibTableColumn
fTRMainRingAutoRecovState = _FTRMainRingAutoRecovState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 42),
    _FTRMainRingAutoRecovState_Type()
)
fTRMainRingAutoRecovState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingAutoRecovState.setStatus("mandatory")


class _FTRMainRingRawCommandData_Type(OctetString):
    """Custom type fTRMainRingRawCommandData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FTRMainRingRawCommandData_Type.__name__ = "OctetString"
_FTRMainRingRawCommandData_Object = MibTableColumn
fTRMainRingRawCommandData = _FTRMainRingRawCommandData_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 43),
    _FTRMainRingRawCommandData_Type()
)
fTRMainRingRawCommandData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingRawCommandData.setStatus("mandatory")


class _FTRMainRingPowerStatus_Type(Integer32):
    """Custom type fTRMainRingPowerStatus based on Integer32"""
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
        *(("dualSup-ASupBAD", 4),
          ("dualSup-BSupBAD", 3),
          ("dualSupOK", 2),
          ("illegal", 5),
          ("singleSupOK", 1))
    )


_FTRMainRingPowerStatus_Type.__name__ = "Integer32"
_FTRMainRingPowerStatus_Object = MibTableColumn
fTRMainRingPowerStatus = _FTRMainRingPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 44),
    _FTRMainRingPowerStatus_Type()
)
fTRMainRingPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingPowerStatus.setStatus("mandatory")


class _FTRMainRingCageType_Type(Integer32):
    """Custom type fTRMainRingCageType based on Integer32"""
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
        *(("fiveslot-10101", 2),
          ("fiveslotredundant-10102", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("twoslot-10100", 1))
    )


_FTRMainRingCageType_Type.__name__ = "Integer32"
_FTRMainRingCageType_Object = MibTableColumn
fTRMainRingCageType = _FTRMainRingCageType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 45),
    _FTRMainRingCageType_Type()
)
fTRMainRingCageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRMainRingCageType.setStatus("mandatory")


class _FTRMainRingAutoRecovMode_Type(Integer32):
    """Custom type fTRMainRingAutoRecovMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-selfEnabling", 2),
          ("selfEnabling", 1))
    )


_FTRMainRingAutoRecovMode_Type.__name__ = "Integer32"
_FTRMainRingAutoRecovMode_Object = MibTableColumn
fTRMainRingAutoRecovMode = _FTRMainRingAutoRecovMode_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 2, 2, 1, 46),
    _FTRMainRingAutoRecovMode_Type()
)
fTRMainRingAutoRecovMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRMainRingAutoRecovMode.setStatus("mandatory")
_FTRLobe_ObjectIdentity = ObjectIdentity
fTRLobe = _FTRLobe_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3)
)
_FTRLobeNumber_Type = Integer32
_FTRLobeNumber_Object = MibScalar
fTRLobeNumber = _FTRLobeNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 1),
    _FTRLobeNumber_Type()
)
fTRLobeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeNumber.setStatus("mandatory")
_FTRLobeTable_Object = MibTable
fTRLobeTable = _FTRLobeTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    fTRLobeTable.setStatus("mandatory")
_FTRLobeTableEntry_Object = MibTableRow
fTRLobeTableEntry = _FTRLobeTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1)
)
fTRLobeTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "fTRLobeTableIndex"),
)
if mibBuilder.loadTexts:
    fTRLobeTableEntry.setStatus("mandatory")
_FTRLobeTableIndex_Type = Integer32
_FTRLobeTableIndex_Object = MibTableColumn
fTRLobeTableIndex = _FTRLobeTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 1),
    _FTRLobeTableIndex_Type()
)
fTRLobeTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeTableIndex.setStatus("mandatory")


class _FTRLobeModel_Type(Integer32):
    """Custom type fTRLobeModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f10157trPassiveMau", 1),
          ("f10158trActiveMau", 2))
    )


_FTRLobeModel_Type.__name__ = "Integer32"
_FTRLobeModel_Object = MibTableColumn
fTRLobeModel = _FTRLobeModel_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 2),
    _FTRLobeModel_Type()
)
fTRLobeModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeModel.setStatus("mandatory")


class _FTRLobe485Address_Type(OctetString):
    """Custom type fTRLobe485Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_FTRLobe485Address_Type.__name__ = "OctetString"
_FTRLobe485Address_Object = MibTableColumn
fTRLobe485Address = _FTRLobe485Address_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 3),
    _FTRLobe485Address_Type()
)
fTRLobe485Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobe485Address.setStatus("mandatory")
_FTRLobeSlotIndex_Type = Integer32
_FTRLobeSlotIndex_Object = MibTableColumn
fTRLobeSlotIndex = _FTRLobeSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 4),
    _FTRLobeSlotIndex_Type()
)
fTRLobeSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeSlotIndex.setStatus("mandatory")
_FTRLobeChassisIndex_Type = Integer32
_FTRLobeChassisIndex_Object = MibTableColumn
fTRLobeChassisIndex = _FTRLobeChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 5),
    _FTRLobeChassisIndex_Type()
)
fTRLobeChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeChassisIndex.setStatus("mandatory")


class _FTRLobeDataRateState_Type(Integer32):
    """Custom type fTRLobeDataRateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("s16Mbps", 2),
          ("s4Mbps", 1))
    )


_FTRLobeDataRateState_Type.__name__ = "Integer32"
_FTRLobeDataRateState_Object = MibTableColumn
fTRLobeDataRateState = _FTRLobeDataRateState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 6),
    _FTRLobeDataRateState_Type()
)
fTRLobeDataRateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRLobeDataRateState.setStatus("mandatory")
_FTRLobeDataRateTimeStamp_Type = TimeTicks
_FTRLobeDataRateTimeStamp_Object = MibTableColumn
fTRLobeDataRateTimeStamp = _FTRLobeDataRateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 7),
    _FTRLobeDataRateTimeStamp_Type()
)
fTRLobeDataRateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeDataRateTimeStamp.setStatus("mandatory")


class _FTRLobeBkPlnNsrtState_Type(Integer32):
    """Custom type fTRLobeBkPlnNsrtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 2),
          ("inserted", 1))
    )


_FTRLobeBkPlnNsrtState_Type.__name__ = "Integer32"
_FTRLobeBkPlnNsrtState_Object = MibTableColumn
fTRLobeBkPlnNsrtState = _FTRLobeBkPlnNsrtState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 8),
    _FTRLobeBkPlnNsrtState_Type()
)
fTRLobeBkPlnNsrtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRLobeBkPlnNsrtState.setStatus("mandatory")
_FTRLobeBkPlnTimeStamp_Type = TimeTicks
_FTRLobeBkPlnTimeStamp_Object = MibTableColumn
fTRLobeBkPlnTimeStamp = _FTRLobeBkPlnTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 9),
    _FTRLobeBkPlnTimeStamp_Type()
)
fTRLobeBkPlnTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeBkPlnTimeStamp.setStatus("mandatory")


class _FTRLobeMgmtStatus_Type(Integer32):
    """Custom type fTRLobeMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("operational", 1))
    )


_FTRLobeMgmtStatus_Type.__name__ = "Integer32"
_FTRLobeMgmtStatus_Object = MibTableColumn
fTRLobeMgmtStatus = _FTRLobeMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 10),
    _FTRLobeMgmtStatus_Type()
)
fTRLobeMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeMgmtStatus.setStatus("mandatory")


class _FTRLobeProxyAgentID_Type(OctetString):
    """Custom type fTRLobeProxyAgentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_FTRLobeProxyAgentID_Type.__name__ = "OctetString"
_FTRLobeProxyAgentID_Object = MibTableColumn
fTRLobeProxyAgentID = _FTRLobeProxyAgentID_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 11),
    _FTRLobeProxyAgentID_Type()
)
fTRLobeProxyAgentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeProxyAgentID.setStatus("mandatory")


class _FTRLobeTemperatureStatus_Type(Integer32):
    """Custom type fTRLobeTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("ok", 1))
    )


_FTRLobeTemperatureStatus_Type.__name__ = "Integer32"
_FTRLobeTemperatureStatus_Object = MibTableColumn
fTRLobeTemperatureStatus = _FTRLobeTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 12),
    _FTRLobeTemperatureStatus_Type()
)
fTRLobeTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeTemperatureStatus.setStatus("mandatory")


class _FTRLobeAutoRecovControl_Type(Integer32):
    """Custom type fTRLobeAutoRecovControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("reset", 3))
    )


_FTRLobeAutoRecovControl_Type.__name__ = "Integer32"
_FTRLobeAutoRecovControl_Object = MibTableColumn
fTRLobeAutoRecovControl = _FTRLobeAutoRecovControl_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 13),
    _FTRLobeAutoRecovControl_Type()
)
fTRLobeAutoRecovControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRLobeAutoRecovControl.setStatus("mandatory")


class _FTRLobeAutoRecovMode_Type(Integer32):
    """Custom type fTRLobeAutoRecovMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-selfEnabling", 2),
          ("selfEnabling", 1))
    )


_FTRLobeAutoRecovMode_Type.__name__ = "Integer32"
_FTRLobeAutoRecovMode_Object = MibTableColumn
fTRLobeAutoRecovMode = _FTRLobeAutoRecovMode_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 14),
    _FTRLobeAutoRecovMode_Type()
)
fTRLobeAutoRecovMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRLobeAutoRecovMode.setStatus("mandatory")


class _FTRLobeAutoRecovRetries_Type(Integer32):
    """Custom type fTRLobeAutoRecovRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FTRLobeAutoRecovRetries_Type.__name__ = "Integer32"
_FTRLobeAutoRecovRetries_Object = MibTableColumn
fTRLobeAutoRecovRetries = _FTRLobeAutoRecovRetries_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 15),
    _FTRLobeAutoRecovRetries_Type()
)
fTRLobeAutoRecovRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRLobeAutoRecovRetries.setStatus("mandatory")


class _FTRLobeCodeVersion_Type(OctetString):
    """Custom type fTRLobeCodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FTRLobeCodeVersion_Type.__name__ = "OctetString"
_FTRLobeCodeVersion_Object = MibTableColumn
fTRLobeCodeVersion = _FTRLobeCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 16),
    _FTRLobeCodeVersion_Type()
)
fTRLobeCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeCodeVersion.setStatus("mandatory")


class _FTRLobeAutoRecovState_Type(Integer32):
    """Custom type fTRLobeAutoRecovState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("halted", 3),
          ("in-recovery", 1),
          ("normal", 2))
    )


_FTRLobeAutoRecovState_Type.__name__ = "Integer32"
_FTRLobeAutoRecovState_Object = MibTableColumn
fTRLobeAutoRecovState = _FTRLobeAutoRecovState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 17),
    _FTRLobeAutoRecovState_Type()
)
fTRLobeAutoRecovState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeAutoRecovState.setStatus("mandatory")


class _FTRLobeRawCommandData_Type(OctetString):
    """Custom type fTRLobeRawCommandData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FTRLobeRawCommandData_Type.__name__ = "OctetString"
_FTRLobeRawCommandData_Object = MibTableColumn
fTRLobeRawCommandData = _FTRLobeRawCommandData_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 18),
    _FTRLobeRawCommandData_Type()
)
fTRLobeRawCommandData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRLobeRawCommandData.setStatus("mandatory")


class _FTRLobePowerStatus_Type(Integer32):
    """Custom type fTRLobePowerStatus based on Integer32"""
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
        *(("dualSup-ASupBAD", 4),
          ("dualSup-BSupBAD", 3),
          ("dualSupOK", 2),
          ("illegal", 5),
          ("singleSupOK", 1))
    )


_FTRLobePowerStatus_Type.__name__ = "Integer32"
_FTRLobePowerStatus_Object = MibTableColumn
fTRLobePowerStatus = _FTRLobePowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 19),
    _FTRLobePowerStatus_Type()
)
fTRLobePowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobePowerStatus.setStatus("mandatory")


class _FTRLobeCageType_Type(Integer32):
    """Custom type fTRLobeCageType based on Integer32"""
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
        *(("fiveslot-10101", 2),
          ("fiveslotredundant-10102", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("twoslot-10100", 1))
    )


_FTRLobeCageType_Type.__name__ = "Integer32"
_FTRLobeCageType_Object = MibTableColumn
fTRLobeCageType = _FTRLobeCageType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 2, 1, 20),
    _FTRLobeCageType_Type()
)
fTRLobeCageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeCageType.setStatus("mandatory")
_FTRLobeConnectNumber_Type = Integer32
_FTRLobeConnectNumber_Object = MibScalar
fTRLobeConnectNumber = _FTRLobeConnectNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 3),
    _FTRLobeConnectNumber_Type()
)
fTRLobeConnectNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeConnectNumber.setStatus("mandatory")
_FTRLobeConnectTable_Object = MibTable
fTRLobeConnectTable = _FTRLobeConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4)
)
if mibBuilder.loadTexts:
    fTRLobeConnectTable.setStatus("mandatory")
_FTRLobeConnectEntry_Object = MibTableRow
fTRLobeConnectEntry = _FTRLobeConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4, 1)
)
fTRLobeConnectEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "fTRLobeIndex"),
    (0, "STARTEK-PRIVATE-MIB", "fTRLobeConnectPort"),
)
if mibBuilder.loadTexts:
    fTRLobeConnectEntry.setStatus("mandatory")
_FTRLobeIndex_Type = Integer32
_FTRLobeIndex_Object = MibTableColumn
fTRLobeIndex = _FTRLobeIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4, 1, 1),
    _FTRLobeIndex_Type()
)
fTRLobeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeIndex.setStatus("mandatory")
_FTRLobeConnectPort_Type = Integer32
_FTRLobeConnectPort_Object = MibTableColumn
fTRLobeConnectPort = _FTRLobeConnectPort_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4, 1, 2),
    _FTRLobeConnectPort_Type()
)
fTRLobeConnectPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeConnectPort.setStatus("mandatory")


class _FTRLobeConnectPhDet_Type(Integer32):
    """Custom type fTRLobeConnectPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_FTRLobeConnectPhDet_Type.__name__ = "Integer32"
_FTRLobeConnectPhDet_Object = MibTableColumn
fTRLobeConnectPhDet = _FTRLobeConnectPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4, 1, 3),
    _FTRLobeConnectPhDet_Type()
)
fTRLobeConnectPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeConnectPhDet.setStatus("mandatory")


class _FTRLobeConnectMask_Type(Integer32):
    """Custom type fTRLobeConnectMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("isolated", 1))
    )


_FTRLobeConnectMask_Type.__name__ = "Integer32"
_FTRLobeConnectMask_Object = MibTableColumn
fTRLobeConnectMask = _FTRLobeConnectMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4, 1, 4),
    _FTRLobeConnectMask_Type()
)
fTRLobeConnectMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fTRLobeConnectMask.setStatus("mandatory")


class _FTRLobeConnectNsrtStatus_Type(Integer32):
    """Custom type fTRLobeConnectNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_FTRLobeConnectNsrtStatus_Type.__name__ = "Integer32"
_FTRLobeConnectNsrtStatus_Object = MibTableColumn
fTRLobeConnectNsrtStatus = _FTRLobeConnectNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4, 1, 5),
    _FTRLobeConnectNsrtStatus_Type()
)
fTRLobeConnectNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeConnectNsrtStatus.setStatus("mandatory")


class _FTRLobeConnectMacAddr_Type(OctetString):
    """Custom type fTRLobeConnectMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_FTRLobeConnectMacAddr_Type.__name__ = "OctetString"
_FTRLobeConnectMacAddr_Object = MibTableColumn
fTRLobeConnectMacAddr = _FTRLobeConnectMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4, 1, 6),
    _FTRLobeConnectMacAddr_Type()
)
fTRLobeConnectMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeConnectMacAddr.setStatus("mandatory")


class _FTRLobeConnectBcnRemStatus_Type(Integer32):
    """Custom type fTRLobeConnectBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_FTRLobeConnectBcnRemStatus_Type.__name__ = "Integer32"
_FTRLobeConnectBcnRemStatus_Object = MibTableColumn
fTRLobeConnectBcnRemStatus = _FTRLobeConnectBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4, 1, 7),
    _FTRLobeConnectBcnRemStatus_Type()
)
fTRLobeConnectBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeConnectBcnRemStatus.setStatus("mandatory")


class _FTRLobeConnectBcnRemCause_Type(Integer32):
    """Custom type fTRLobeConnectBcnRemCause based on Integer32"""
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
        *(("bad-rate", 4),
          ("no-carrier", 3),
          ("no-removal", 1),
          ("phantom-error", 2),
          ("unknown", 5))
    )


_FTRLobeConnectBcnRemCause_Type.__name__ = "Integer32"
_FTRLobeConnectBcnRemCause_Object = MibTableColumn
fTRLobeConnectBcnRemCause = _FTRLobeConnectBcnRemCause_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4, 1, 8),
    _FTRLobeConnectBcnRemCause_Type()
)
fTRLobeConnectBcnRemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeConnectBcnRemCause.setStatus("mandatory")
_FTRLobeConnectTimeStamp_Type = TimeTicks
_FTRLobeConnectTimeStamp_Object = MibTableColumn
fTRLobeConnectTimeStamp = _FTRLobeConnectTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 3, 4, 1, 9),
    _FTRLobeConnectTimeStamp_Type()
)
fTRLobeConnectTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fTRLobeConnectTimeStamp.setStatus("mandatory")
_FEthernet_ObjectIdentity = ObjectIdentity
fEthernet = _FEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4)
)
_FEthernetNumber_Type = Integer32
_FEthernetNumber_Object = MibScalar
fEthernetNumber = _FEthernetNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 1),
    _FEthernetNumber_Type()
)
fEthernetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetNumber.setStatus("mandatory")
_FEthernetTable_Object = MibTable
fEthernetTable = _FEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2)
)
if mibBuilder.loadTexts:
    fEthernetTable.setStatus("mandatory")
_FEthernetTableEntry_Object = MibTableRow
fEthernetTableEntry = _FEthernetTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1)
)
fEthernetTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "fEthernetTableIndex"),
)
if mibBuilder.loadTexts:
    fEthernetTableEntry.setStatus("mandatory")
_FEthernetTableIndex_Type = Integer32
_FEthernetTableIndex_Object = MibTableColumn
fEthernetTableIndex = _FEthernetTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 1),
    _FEthernetTableIndex_Type()
)
fEthernetTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetTableIndex.setStatus("mandatory")


class _FEthernetModel_Type(Integer32):
    """Custom type fEthernetModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("f10160", 1),
          ("f10161", 2))
    )


_FEthernetModel_Type.__name__ = "Integer32"
_FEthernetModel_Object = MibTableColumn
fEthernetModel = _FEthernetModel_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 2),
    _FEthernetModel_Type()
)
fEthernetModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetModel.setStatus("mandatory")


class _FEthernet485Address_Type(OctetString):
    """Custom type fEthernet485Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_FEthernet485Address_Type.__name__ = "OctetString"
_FEthernet485Address_Object = MibTableColumn
fEthernet485Address = _FEthernet485Address_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 3),
    _FEthernet485Address_Type()
)
fEthernet485Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernet485Address.setStatus("mandatory")
_FEthernetSlotIndex_Type = Integer32
_FEthernetSlotIndex_Object = MibTableColumn
fEthernetSlotIndex = _FEthernetSlotIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 4),
    _FEthernetSlotIndex_Type()
)
fEthernetSlotIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetSlotIndex.setStatus("mandatory")
_FEthernetChassisIndex_Type = Integer32
_FEthernetChassisIndex_Object = MibTableColumn
fEthernetChassisIndex = _FEthernetChassisIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 5),
    _FEthernetChassisIndex_Type()
)
fEthernetChassisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetChassisIndex.setStatus("mandatory")


class _FEthernetBkPlnNsrtState_Type(Integer32):
    """Custom type fEthernetBkPlnNsrtState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 2),
          ("inserted", 1))
    )


_FEthernetBkPlnNsrtState_Type.__name__ = "Integer32"
_FEthernetBkPlnNsrtState_Object = MibTableColumn
fEthernetBkPlnNsrtState = _FEthernetBkPlnNsrtState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 6),
    _FEthernetBkPlnNsrtState_Type()
)
fEthernetBkPlnNsrtState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fEthernetBkPlnNsrtState.setStatus("mandatory")
_FEthernetBkPlnTimeStamp_Type = TimeTicks
_FEthernetBkPlnTimeStamp_Object = MibTableColumn
fEthernetBkPlnTimeStamp = _FEthernetBkPlnTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 7),
    _FEthernetBkPlnTimeStamp_Type()
)
fEthernetBkPlnTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetBkPlnTimeStamp.setStatus("mandatory")


class _FEthernetMgmtStatus_Type(Integer32):
    """Custom type fEthernetMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("operational", 1))
    )


_FEthernetMgmtStatus_Type.__name__ = "Integer32"
_FEthernetMgmtStatus_Object = MibTableColumn
fEthernetMgmtStatus = _FEthernetMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 8),
    _FEthernetMgmtStatus_Type()
)
fEthernetMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetMgmtStatus.setStatus("mandatory")


class _FEthernetProxyAgentID_Type(OctetString):
    """Custom type fEthernetProxyAgentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_FEthernetProxyAgentID_Type.__name__ = "OctetString"
_FEthernetProxyAgentID_Object = MibTableColumn
fEthernetProxyAgentID = _FEthernetProxyAgentID_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 9),
    _FEthernetProxyAgentID_Type()
)
fEthernetProxyAgentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetProxyAgentID.setStatus("mandatory")


class _FEthernetTemperatureStatus_Type(Integer32):
    """Custom type fEthernetTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("ok", 1))
    )


_FEthernetTemperatureStatus_Type.__name__ = "Integer32"
_FEthernetTemperatureStatus_Object = MibTableColumn
fEthernetTemperatureStatus = _FEthernetTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 10),
    _FEthernetTemperatureStatus_Type()
)
fEthernetTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetTemperatureStatus.setStatus("mandatory")


class _FEthernetCodeVersion_Type(OctetString):
    """Custom type fEthernetCodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_FEthernetCodeVersion_Type.__name__ = "OctetString"
_FEthernetCodeVersion_Object = MibTableColumn
fEthernetCodeVersion = _FEthernetCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 11),
    _FEthernetCodeVersion_Type()
)
fEthernetCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetCodeVersion.setStatus("mandatory")


class _FEthernetRawCommandData_Type(OctetString):
    """Custom type fEthernetRawCommandData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_FEthernetRawCommandData_Type.__name__ = "OctetString"
_FEthernetRawCommandData_Object = MibTableColumn
fEthernetRawCommandData = _FEthernetRawCommandData_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 12),
    _FEthernetRawCommandData_Type()
)
fEthernetRawCommandData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fEthernetRawCommandData.setStatus("mandatory")


class _FEthernetPowerStatus_Type(Integer32):
    """Custom type fEthernetPowerStatus based on Integer32"""
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
        *(("dualSup-ASupBAD", 4),
          ("dualSup-BSupBAD", 3),
          ("dualSupOK", 2),
          ("illegal", 5),
          ("singleSupOK", 1))
    )


_FEthernetPowerStatus_Type.__name__ = "Integer32"
_FEthernetPowerStatus_Object = MibTableColumn
fEthernetPowerStatus = _FEthernetPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 13),
    _FEthernetPowerStatus_Type()
)
fEthernetPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetPowerStatus.setStatus("mandatory")


class _FEthernetCageType_Type(Integer32):
    """Custom type fEthernetCageType based on Integer32"""
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
        *(("fiveslot-10101", 2),
          ("fiveslotredundant-10102", 3),
          ("reserved4", 4),
          ("reserved5", 5),
          ("reserved6", 6),
          ("reserved7", 7),
          ("reserved8", 8),
          ("twoslot-10100", 1))
    )


_FEthernetCageType_Type.__name__ = "Integer32"
_FEthernetCageType_Object = MibTableColumn
fEthernetCageType = _FEthernetCageType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 4, 2, 1, 14),
    _FEthernetCageType_Type()
)
fEthernetCageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fEthernetCageType.setStatus("mandatory")
_FFddi_ObjectIdentity = ObjectIdentity
fFddi = _FFddi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 5)
)
_FTwx_ObjectIdentity = ObjectIdentity
fTwx = _FTwx_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 6)
)
_RmonAgent_ObjectIdentity = ObjectIdentity
rmonAgent = _RmonAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7)
)


class _RmonAgentDescription_Type(DisplayString):
    """Custom type rmonAgentDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RmonAgentDescription_Type.__name__ = "DisplayString"
_RmonAgentDescription_Object = MibScalar
rmonAgentDescription = _RmonAgentDescription_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 1),
    _RmonAgentDescription_Type()
)
rmonAgentDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAgentDescription.setStatus("mandatory")


class _RmonAgentID_Type(OctetString):
    """Custom type rmonAgentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_RmonAgentID_Type.__name__ = "OctetString"
_RmonAgentID_Object = MibScalar
rmonAgentID = _RmonAgentID_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 2),
    _RmonAgentID_Type()
)
rmonAgentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentID.setStatus("mandatory")
_RmonAgentOOBNumber_Type = Integer32
_RmonAgentOOBNumber_Object = MibScalar
rmonAgentOOBNumber = _RmonAgentOOBNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 3),
    _RmonAgentOOBNumber_Type()
)
rmonAgentOOBNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentOOBNumber.setStatus("mandatory")
_RmonAgentOOBTable_Object = MibTable
rmonAgentOOBTable = _RmonAgentOOBTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 4)
)
if mibBuilder.loadTexts:
    rmonAgentOOBTable.setStatus("mandatory")
_RmonAgentOOBTableEntry_Object = MibTableRow
rmonAgentOOBTableEntry = _RmonAgentOOBTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 4, 1)
)
rmonAgentOOBTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "rmonAgentOOBTableIndex"),
)
if mibBuilder.loadTexts:
    rmonAgentOOBTableEntry.setStatus("mandatory")
_RmonAgentOOBTableIndex_Type = Integer32
_RmonAgentOOBTableIndex_Object = MibTableColumn
rmonAgentOOBTableIndex = _RmonAgentOOBTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 4, 1, 1),
    _RmonAgentOOBTableIndex_Type()
)
rmonAgentOOBTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentOOBTableIndex.setStatus("mandatory")


class _RmonAgentOOBTableDescription_Type(DisplayString):
    """Custom type rmonAgentOOBTableDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RmonAgentOOBTableDescription_Type.__name__ = "DisplayString"
_RmonAgentOOBTableDescription_Object = MibTableColumn
rmonAgentOOBTableDescription = _RmonAgentOOBTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 4, 1, 2),
    _RmonAgentOOBTableDescription_Type()
)
rmonAgentOOBTableDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAgentOOBTableDescription.setStatus("mandatory")
_RmonAgentOOBTableData_Type = Opaque
_RmonAgentOOBTableData_Object = MibTableColumn
rmonAgentOOBTableData = _RmonAgentOOBTableData_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 4, 1, 3),
    _RmonAgentOOBTableData_Type()
)
rmonAgentOOBTableData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentOOBTableData.setStatus("mandatory")


class _RmonAgentOOBRawDataCommand_Type(OctetString):
    """Custom type rmonAgentOOBRawDataCommand based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_RmonAgentOOBRawDataCommand_Type.__name__ = "OctetString"
_RmonAgentOOBRawDataCommand_Object = MibTableColumn
rmonAgentOOBRawDataCommand = _RmonAgentOOBRawDataCommand_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 4, 1, 4),
    _RmonAgentOOBRawDataCommand_Type()
)
rmonAgentOOBRawDataCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAgentOOBRawDataCommand.setStatus("mandatory")
_RmonAgentIBNumber_Type = Integer32
_RmonAgentIBNumber_Object = MibScalar
rmonAgentIBNumber = _RmonAgentIBNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 5),
    _RmonAgentIBNumber_Type()
)
rmonAgentIBNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBNumber.setStatus("mandatory")
_RmonAgentIBTable_Object = MibTable
rmonAgentIBTable = _RmonAgentIBTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6)
)
if mibBuilder.loadTexts:
    rmonAgentIBTable.setStatus("mandatory")
_RmonAgentIBTableEntry_Object = MibTableRow
rmonAgentIBTableEntry = _RmonAgentIBTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1)
)
rmonAgentIBTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "rmonAgentIBTableIndex"),
)
if mibBuilder.loadTexts:
    rmonAgentIBTableEntry.setStatus("mandatory")
_RmonAgentIBTableIndex_Type = Integer32
_RmonAgentIBTableIndex_Object = MibTableColumn
rmonAgentIBTableIndex = _RmonAgentIBTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 1),
    _RmonAgentIBTableIndex_Type()
)
rmonAgentIBTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBTableIndex.setStatus("mandatory")


class _RmonAgentIBTableDescription_Type(DisplayString):
    """Custom type rmonAgentIBTableDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RmonAgentIBTableDescription_Type.__name__ = "DisplayString"
_RmonAgentIBTableDescription_Object = MibTableColumn
rmonAgentIBTableDescription = _RmonAgentIBTableDescription_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 2),
    _RmonAgentIBTableDescription_Type()
)
rmonAgentIBTableDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAgentIBTableDescription.setStatus("mandatory")


class _RmonAgentIBNetworkType_Type(Integer32):
    """Custom type rmonAgentIBNetworkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ethernet", 2),
          ("fddi", 3),
          ("tokenring", 1))
    )


_RmonAgentIBNetworkType_Type.__name__ = "Integer32"
_RmonAgentIBNetworkType_Object = MibTableColumn
rmonAgentIBNetworkType = _RmonAgentIBNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 3),
    _RmonAgentIBNetworkType_Type()
)
rmonAgentIBNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBNetworkType.setStatus("mandatory")
_RmonAgentIBSampleInterval_Type = Counter32
_RmonAgentIBSampleInterval_Object = MibTableColumn
rmonAgentIBSampleInterval = _RmonAgentIBSampleInterval_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 4),
    _RmonAgentIBSampleInterval_Type()
)
rmonAgentIBSampleInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAgentIBSampleInterval.setStatus("mandatory")
_RmonAgentIBMacFrames_Type = Counter32
_RmonAgentIBMacFrames_Object = MibTableColumn
rmonAgentIBMacFrames = _RmonAgentIBMacFrames_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 5),
    _RmonAgentIBMacFrames_Type()
)
rmonAgentIBMacFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMacFrames.setStatus("mandatory")
_RmonAgentIBDataFrames_Type = Counter32
_RmonAgentIBDataFrames_Object = MibTableColumn
rmonAgentIBDataFrames = _RmonAgentIBDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 6),
    _RmonAgentIBDataFrames_Type()
)
rmonAgentIBDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBDataFrames.setStatus("mandatory")
_RmonAgentIBMacBytes_Type = Counter32
_RmonAgentIBMacBytes_Object = MibTableColumn
rmonAgentIBMacBytes = _RmonAgentIBMacBytes_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 7),
    _RmonAgentIBMacBytes_Type()
)
rmonAgentIBMacBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMacBytes.setStatus("mandatory")
_RmonAgentIBDataBytes_Type = Counter32
_RmonAgentIBDataBytes_Object = MibTableColumn
rmonAgentIBDataBytes = _RmonAgentIBDataBytes_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 8),
    _RmonAgentIBDataBytes_Type()
)
rmonAgentIBDataBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBDataBytes.setStatus("mandatory")
_RmonAgentIBUtilization_Type = Counter32
_RmonAgentIBUtilization_Object = MibTableColumn
rmonAgentIBUtilization = _RmonAgentIBUtilization_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 9),
    _RmonAgentIBUtilization_Type()
)
rmonAgentIBUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBUtilization.setStatus("mandatory")
_RmonAgentIBMACUtilization_Type = Counter32
_RmonAgentIBMACUtilization_Object = MibTableColumn
rmonAgentIBMACUtilization = _RmonAgentIBMACUtilization_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 10),
    _RmonAgentIBMACUtilization_Type()
)
rmonAgentIBMACUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACUtilization.setStatus("mandatory")
_RmonAgentIBNonMACUtilization_Type = Counter32
_RmonAgentIBNonMACUtilization_Object = MibTableColumn
rmonAgentIBNonMACUtilization = _RmonAgentIBNonMACUtilization_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 11),
    _RmonAgentIBNonMACUtilization_Type()
)
rmonAgentIBNonMACUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBNonMACUtilization.setStatus("mandatory")
_RmonAgentIBMACData0_Type = Opaque
_RmonAgentIBMACData0_Object = MibTableColumn
rmonAgentIBMACData0 = _RmonAgentIBMACData0_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 12),
    _RmonAgentIBMACData0_Type()
)
rmonAgentIBMACData0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData0.setStatus("mandatory")
_RmonAgentIBMACData1_Type = Opaque
_RmonAgentIBMACData1_Object = MibTableColumn
rmonAgentIBMACData1 = _RmonAgentIBMACData1_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 13),
    _RmonAgentIBMACData1_Type()
)
rmonAgentIBMACData1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData1.setStatus("mandatory")
_RmonAgentIBMACData2_Type = Opaque
_RmonAgentIBMACData2_Object = MibTableColumn
rmonAgentIBMACData2 = _RmonAgentIBMACData2_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 14),
    _RmonAgentIBMACData2_Type()
)
rmonAgentIBMACData2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData2.setStatus("mandatory")
_RmonAgentIBMACData3_Type = Opaque
_RmonAgentIBMACData3_Object = MibTableColumn
rmonAgentIBMACData3 = _RmonAgentIBMACData3_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 15),
    _RmonAgentIBMACData3_Type()
)
rmonAgentIBMACData3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData3.setStatus("mandatory")
_RmonAgentIBMACData4_Type = Opaque
_RmonAgentIBMACData4_Object = MibTableColumn
rmonAgentIBMACData4 = _RmonAgentIBMACData4_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 16),
    _RmonAgentIBMACData4_Type()
)
rmonAgentIBMACData4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData4.setStatus("mandatory")
_RmonAgentIBMACData5_Type = Opaque
_RmonAgentIBMACData5_Object = MibTableColumn
rmonAgentIBMACData5 = _RmonAgentIBMACData5_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 17),
    _RmonAgentIBMACData5_Type()
)
rmonAgentIBMACData5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData5.setStatus("mandatory")
_RmonAgentIBMACData6_Type = Opaque
_RmonAgentIBMACData6_Object = MibTableColumn
rmonAgentIBMACData6 = _RmonAgentIBMACData6_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 18),
    _RmonAgentIBMACData6_Type()
)
rmonAgentIBMACData6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData6.setStatus("mandatory")
_RmonAgentIBMACData7_Type = Opaque
_RmonAgentIBMACData7_Object = MibTableColumn
rmonAgentIBMACData7 = _RmonAgentIBMACData7_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 19),
    _RmonAgentIBMACData7_Type()
)
rmonAgentIBMACData7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData7.setStatus("mandatory")
_RmonAgentIBMACData8_Type = Opaque
_RmonAgentIBMACData8_Object = MibTableColumn
rmonAgentIBMACData8 = _RmonAgentIBMACData8_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 20),
    _RmonAgentIBMACData8_Type()
)
rmonAgentIBMACData8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData8.setStatus("mandatory")
_RmonAgentIBMACData9_Type = Opaque
_RmonAgentIBMACData9_Object = MibTableColumn
rmonAgentIBMACData9 = _RmonAgentIBMACData9_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 21),
    _RmonAgentIBMACData9_Type()
)
rmonAgentIBMACData9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData9.setStatus("mandatory")
_RmonAgentIBMACData10_Type = Opaque
_RmonAgentIBMACData10_Object = MibTableColumn
rmonAgentIBMACData10 = _RmonAgentIBMACData10_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 22),
    _RmonAgentIBMACData10_Type()
)
rmonAgentIBMACData10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData10.setStatus("mandatory")
_RmonAgentIBMACData11_Type = Opaque
_RmonAgentIBMACData11_Object = MibTableColumn
rmonAgentIBMACData11 = _RmonAgentIBMACData11_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 6, 1, 23),
    _RmonAgentIBMACData11_Type()
)
rmonAgentIBMACData11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentIBMACData11.setStatus("mandatory")


class _RmonAgentMonitorCommand_Type(DisplayString):
    """Custom type rmonAgentMonitorCommand based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RmonAgentMonitorCommand_Type.__name__ = "DisplayString"
_RmonAgentMonitorCommand_Object = MibScalar
rmonAgentMonitorCommand = _RmonAgentMonitorCommand_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 7),
    _RmonAgentMonitorCommand_Type()
)
rmonAgentMonitorCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAgentMonitorCommand.setStatus("mandatory")


class _RmonAgentMonitorResponse_Type(DisplayString):
    """Custom type rmonAgentMonitorResponse based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_RmonAgentMonitorResponse_Type.__name__ = "DisplayString"
_RmonAgentMonitorResponse_Object = MibScalar
rmonAgentMonitorResponse = _RmonAgentMonitorResponse_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 8),
    _RmonAgentMonitorResponse_Type()
)
rmonAgentMonitorResponse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentMonitorResponse.setStatus("mandatory")


class _RmonAgentDownloadData_Type(OctetString):
    """Custom type rmonAgentDownloadData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_RmonAgentDownloadData_Type.__name__ = "OctetString"
_RmonAgentDownloadData_Object = MibScalar
rmonAgentDownloadData = _RmonAgentDownloadData_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 9),
    _RmonAgentDownloadData_Type()
)
rmonAgentDownloadData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAgentDownloadData.setStatus("mandatory")
_RmonAgentNoMapOid_Type = ObjectIdentifier
_RmonAgentNoMapOid_Object = MibScalar
rmonAgentNoMapOid = _RmonAgentNoMapOid_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 10),
    _RmonAgentNoMapOid_Type()
)
rmonAgentNoMapOid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAgentNoMapOid.setStatus("mandatory")
_RmonAgentMACStatTable_Object = MibTable
rmonAgentMACStatTable = _RmonAgentMACStatTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 11)
)
if mibBuilder.loadTexts:
    rmonAgentMACStatTable.setStatus("mandatory")
_RmonAgentMACStatTableEntry_Object = MibTableRow
rmonAgentMACStatTableEntry = _RmonAgentMACStatTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 11, 1)
)
rmonAgentMACStatTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "pysmiFakeCol1"),
    (0, "STARTEK-PRIVATE-MIB", "pysmiFakeCol2"),
)
if mibBuilder.loadTexts:
    rmonAgentMACStatTableEntry.setStatus("mandatory")
_RmonAgentMACStatTableData_Type = Opaque
_RmonAgentMACStatTableData_Object = MibTableColumn
rmonAgentMACStatTableData = _RmonAgentMACStatTableData_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 11, 1, 1),
    _RmonAgentMACStatTableData_Type()
)
rmonAgentMACStatTableData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rmonAgentMACStatTableData.setStatus("mandatory")
_PysmiFakeCol2_Type = Integer32
_PysmiFakeCol2_Object = MibTableColumn
pysmiFakeCol2 = _PysmiFakeCol2_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 11, 1, 4294967294),
    _PysmiFakeCol2_Type()
)
pysmiFakeCol2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol2.setStatus("mandatory")
_PysmiFakeCol1_Type = Integer32
_PysmiFakeCol1_Object = MibTableColumn
pysmiFakeCol1 = _PysmiFakeCol1_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 11, 1, 4294967295),
    _PysmiFakeCol1_Type()
)
pysmiFakeCol1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol1.setStatus("mandatory")
_RmonAgentIPAdressControl_Type = Opaque
_RmonAgentIPAdressControl_Object = MibScalar
rmonAgentIPAdressControl = _RmonAgentIPAdressControl_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 2, 7, 12),
    _RmonAgentIPAdressControl_Type()
)
rmonAgentIPAdressControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rmonAgentIPAdressControl.setStatus("mandatory")
_Stackable_ObjectIdentity = ObjectIdentity
stackable = _Stackable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 3)
)
_StackableHubs_ObjectIdentity = ObjectIdentity
stackableHubs = _StackableHubs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1)
)
_StackableHubNumber_Type = Integer32
_StackableHubNumber_Object = MibScalar
stackableHubNumber = _StackableHubNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 1),
    _StackableHubNumber_Type()
)
stackableHubNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubNumber.setStatus("mandatory")
_StackableHubTable_Object = MibTable
stackableHubTable = _StackableHubTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    stackableHubTable.setStatus("mandatory")
_StackableHubTableEntry_Object = MibTableRow
stackableHubTableEntry = _StackableHubTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1)
)
stackableHubTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "stackableHubTableIndex"),
)
if mibBuilder.loadTexts:
    stackableHubTableEntry.setStatus("mandatory")
_StackableHubTableIndex_Type = Integer32
_StackableHubTableIndex_Object = MibTableColumn
stackableHubTableIndex = _StackableHubTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 1),
    _StackableHubTableIndex_Type()
)
stackableHubTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubTableIndex.setStatus("mandatory")


class _StackableHubModel_Type(Integer32):
    """Custom type stackableHubModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("standard-issue", 1)
    )


_StackableHubModel_Type.__name__ = "Integer32"
_StackableHubModel_Object = MibTableColumn
stackableHubModel = _StackableHubModel_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 2),
    _StackableHubModel_Type()
)
stackableHubModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubModel.setStatus("mandatory")


class _StackableHub485Address_Type(OctetString):
    """Custom type stackableHub485Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_StackableHub485Address_Type.__name__ = "OctetString"
_StackableHub485Address_Object = MibTableColumn
stackableHub485Address = _StackableHub485Address_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 3),
    _StackableHub485Address_Type()
)
stackableHub485Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHub485Address.setStatus("mandatory")


class _StackableHubRiFTolState_Type(Integer32):
    """Custom type stackableHubRiFTolState based on Integer32"""
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


_StackableHubRiFTolState_Type.__name__ = "Integer32"
_StackableHubRiFTolState_Object = MibTableColumn
stackableHubRiFTolState = _StackableHubRiFTolState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 4),
    _StackableHubRiFTolState_Type()
)
stackableHubRiFTolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubRiFTolState.setStatus("mandatory")


class _StackableHubRiMask_Type(Integer32):
    """Custom type stackableHubRiMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("isolate", 1))
    )


_StackableHubRiMask_Type.__name__ = "Integer32"
_StackableHubRiMask_Object = MibTableColumn
stackableHubRiMask = _StackableHubRiMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 5),
    _StackableHubRiMask_Type()
)
stackableHubRiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubRiMask.setStatus("mandatory")


class _StackableHubRiPhDet_Type(Integer32):
    """Custom type stackableHubRiPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_StackableHubRiPhDet_Type.__name__ = "Integer32"
_StackableHubRiPhDet_Object = MibTableColumn
stackableHubRiPhDet = _StackableHubRiPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 6),
    _StackableHubRiPhDet_Type()
)
stackableHubRiPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRiPhDet.setStatus("mandatory")


class _StackableHubRiNsrtStatus_Type(Integer32):
    """Custom type stackableHubRiNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_StackableHubRiNsrtStatus_Type.__name__ = "Integer32"
_StackableHubRiNsrtStatus_Object = MibTableColumn
stackableHubRiNsrtStatus = _StackableHubRiNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 7),
    _StackableHubRiNsrtStatus_Type()
)
stackableHubRiNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRiNsrtStatus.setStatus("mandatory")


class _StackableHubRiBcnRemStatus_Type(Integer32):
    """Custom type stackableHubRiBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1))
    )


_StackableHubRiBcnRemStatus_Type.__name__ = "Integer32"
_StackableHubRiBcnRemStatus_Object = MibTableColumn
stackableHubRiBcnRemStatus = _StackableHubRiBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 8),
    _StackableHubRiBcnRemStatus_Type()
)
stackableHubRiBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRiBcnRemStatus.setStatus("mandatory")


class _StackableHubRiNeighborType_Type(Integer32):
    """Custom type stackableHubRiNeighborType based on Integer32"""
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
        *(("fSeries", 2),
          ("none", 4),
          ("series828", 1),
          ("stackable", 5),
          ("tokenRingMAC", 3))
    )


_StackableHubRiNeighborType_Type.__name__ = "Integer32"
_StackableHubRiNeighborType_Object = MibTableColumn
stackableHubRiNeighborType = _StackableHubRiNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 9),
    _StackableHubRiNeighborType_Type()
)
stackableHubRiNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRiNeighborType.setStatus("mandatory")


class _StackableHubRiNeighborAddr_Type(OctetString):
    """Custom type stackableHubRiNeighborAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 6),
    )


_StackableHubRiNeighborAddr_Type.__name__ = "OctetString"
_StackableHubRiNeighborAddr_Object = MibTableColumn
stackableHubRiNeighborAddr = _StackableHubRiNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 10),
    _StackableHubRiNeighborAddr_Type()
)
stackableHubRiNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRiNeighborAddr.setStatus("mandatory")
_StackableHubRiTimeStamp_Type = TimeTicks
_StackableHubRiTimeStamp_Object = MibTableColumn
stackableHubRiTimeStamp = _StackableHubRiTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 11),
    _StackableHubRiTimeStamp_Type()
)
stackableHubRiTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRiTimeStamp.setStatus("mandatory")


class _StackableHubRoFTolState_Type(Integer32):
    """Custom type stackableHubRoFTolState based on Integer32"""
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


_StackableHubRoFTolState_Type.__name__ = "Integer32"
_StackableHubRoFTolState_Object = MibTableColumn
stackableHubRoFTolState = _StackableHubRoFTolState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 12),
    _StackableHubRoFTolState_Type()
)
stackableHubRoFTolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubRoFTolState.setStatus("mandatory")


class _StackableHubRoMask_Type(Integer32):
    """Custom type stackableHubRoMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("isolate", 1))
    )


_StackableHubRoMask_Type.__name__ = "Integer32"
_StackableHubRoMask_Object = MibTableColumn
stackableHubRoMask = _StackableHubRoMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 13),
    _StackableHubRoMask_Type()
)
stackableHubRoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubRoMask.setStatus("mandatory")


class _StackableHubRoPhDet_Type(Integer32):
    """Custom type stackableHubRoPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("phantOk", 2),
          ("wireFault", 1))
    )


_StackableHubRoPhDet_Type.__name__ = "Integer32"
_StackableHubRoPhDet_Object = MibTableColumn
stackableHubRoPhDet = _StackableHubRoPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 14),
    _StackableHubRoPhDet_Type()
)
stackableHubRoPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRoPhDet.setStatus("mandatory")


class _StackableHubRoNsrtStatus_Type(Integer32):
    """Custom type stackableHubRoNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_StackableHubRoNsrtStatus_Type.__name__ = "Integer32"
_StackableHubRoNsrtStatus_Object = MibTableColumn
stackableHubRoNsrtStatus = _StackableHubRoNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 15),
    _StackableHubRoNsrtStatus_Type()
)
stackableHubRoNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRoNsrtStatus.setStatus("mandatory")


class _StackableHubRoBcnRemStatus_Type(Integer32):
    """Custom type stackableHubRoBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1))
    )


_StackableHubRoBcnRemStatus_Type.__name__ = "Integer32"
_StackableHubRoBcnRemStatus_Object = MibTableColumn
stackableHubRoBcnRemStatus = _StackableHubRoBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 16),
    _StackableHubRoBcnRemStatus_Type()
)
stackableHubRoBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRoBcnRemStatus.setStatus("mandatory")


class _StackableHubRoNeighborType_Type(Integer32):
    """Custom type stackableHubRoNeighborType based on Integer32"""
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
        *(("fSeries", 2),
          ("none", 4),
          ("series828", 1),
          ("stackable", 5),
          ("tokenRingMAC", 3))
    )


_StackableHubRoNeighborType_Type.__name__ = "Integer32"
_StackableHubRoNeighborType_Object = MibTableColumn
stackableHubRoNeighborType = _StackableHubRoNeighborType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 17),
    _StackableHubRoNeighborType_Type()
)
stackableHubRoNeighborType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRoNeighborType.setStatus("mandatory")


class _StackableHubRoNeighborAddr_Type(OctetString):
    """Custom type stackableHubRoNeighborAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 6),
    )


_StackableHubRoNeighborAddr_Type.__name__ = "OctetString"
_StackableHubRoNeighborAddr_Object = MibTableColumn
stackableHubRoNeighborAddr = _StackableHubRoNeighborAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 18),
    _StackableHubRoNeighborAddr_Type()
)
stackableHubRoNeighborAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRoNeighborAddr.setStatus("mandatory")
_StackableHubRoTimeStamp_Type = TimeTicks
_StackableHubRoTimeStamp_Object = MibTableColumn
stackableHubRoTimeStamp = _StackableHubRoTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 19),
    _StackableHubRoTimeStamp_Type()
)
stackableHubRoTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubRoTimeStamp.setStatus("mandatory")


class _StackableHubDataRateState_Type(Integer32):
    """Custom type stackableHubDataRateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoConfig", 3),
          ("s16Mbps", 2),
          ("s4Mbps", 1))
    )


_StackableHubDataRateState_Type.__name__ = "Integer32"
_StackableHubDataRateState_Object = MibTableColumn
stackableHubDataRateState = _StackableHubDataRateState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 20),
    _StackableHubDataRateState_Type()
)
stackableHubDataRateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubDataRateState.setStatus("mandatory")
_StackableHubDataRateTimeStamp_Type = TimeTicks
_StackableHubDataRateTimeStamp_Object = MibTableColumn
stackableHubDataRateTimeStamp = _StackableHubDataRateTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 21),
    _StackableHubDataRateTimeStamp_Type()
)
stackableHubDataRateTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubDataRateTimeStamp.setStatus("mandatory")


class _StackableHubMgmtStatus_Type(Integer32):
    """Custom type stackableHubMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("operational", 1))
    )


_StackableHubMgmtStatus_Type.__name__ = "Integer32"
_StackableHubMgmtStatus_Object = MibTableColumn
stackableHubMgmtStatus = _StackableHubMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 22),
    _StackableHubMgmtStatus_Type()
)
stackableHubMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubMgmtStatus.setStatus("mandatory")


class _StackableHubProxyAgentID_Type(OctetString):
    """Custom type stackableHubProxyAgentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_StackableHubProxyAgentID_Type.__name__ = "OctetString"
_StackableHubProxyAgentID_Object = MibTableColumn
stackableHubProxyAgentID = _StackableHubProxyAgentID_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 23),
    _StackableHubProxyAgentID_Type()
)
stackableHubProxyAgentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubProxyAgentID.setStatus("mandatory")


class _StackableHubAttachedAgentType_Type(Integer32):
    """Custom type stackableHubAttachedAgentType based on Integer32"""
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
        *(("none", 4),
          ("reserved", 3),
          ("tokenring", 1),
          ("tokenring-ethernet", 2))
    )


_StackableHubAttachedAgentType_Type.__name__ = "Integer32"
_StackableHubAttachedAgentType_Object = MibTableColumn
stackableHubAttachedAgentType = _StackableHubAttachedAgentType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 24),
    _StackableHubAttachedAgentType_Type()
)
stackableHubAttachedAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubAttachedAgentType.setStatus("mandatory")


class _StackableHubAttachedAgentState_Type(Integer32):
    """Custom type stackableHubAttachedAgentState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 2),
          ("enabled", 1),
          ("not-applicable", 3))
    )


_StackableHubAttachedAgentState_Type.__name__ = "Integer32"
_StackableHubAttachedAgentState_Object = MibTableColumn
stackableHubAttachedAgentState = _StackableHubAttachedAgentState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 25),
    _StackableHubAttachedAgentState_Type()
)
stackableHubAttachedAgentState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubAttachedAgentState.setStatus("mandatory")


class _StackableHubTemperatureStatus_Type(Integer32):
    """Custom type stackableHubTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("ok", 1))
    )


_StackableHubTemperatureStatus_Type.__name__ = "Integer32"
_StackableHubTemperatureStatus_Object = MibTableColumn
stackableHubTemperatureStatus = _StackableHubTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 26),
    _StackableHubTemperatureStatus_Type()
)
stackableHubTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubTemperatureStatus.setStatus("mandatory")


class _StackableHubAutoRecovControl_Type(Integer32):
    """Custom type stackableHubAutoRecovControl based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("reset", 3),
          ("unknown", 4))
    )


_StackableHubAutoRecovControl_Type.__name__ = "Integer32"
_StackableHubAutoRecovControl_Object = MibTableColumn
stackableHubAutoRecovControl = _StackableHubAutoRecovControl_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 27),
    _StackableHubAutoRecovControl_Type()
)
stackableHubAutoRecovControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubAutoRecovControl.setStatus("mandatory")


class _StackableHubAutoRecovRetries_Type(Integer32):
    """Custom type stackableHubAutoRecovRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_StackableHubAutoRecovRetries_Type.__name__ = "Integer32"
_StackableHubAutoRecovRetries_Object = MibTableColumn
stackableHubAutoRecovRetries = _StackableHubAutoRecovRetries_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 28),
    _StackableHubAutoRecovRetries_Type()
)
stackableHubAutoRecovRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubAutoRecovRetries.setStatus("mandatory")


class _StackableHubCodeVersion_Type(OctetString):
    """Custom type stackableHubCodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_StackableHubCodeVersion_Type.__name__ = "OctetString"
_StackableHubCodeVersion_Object = MibTableColumn
stackableHubCodeVersion = _StackableHubCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 29),
    _StackableHubCodeVersion_Type()
)
stackableHubCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubCodeVersion.setStatus("mandatory")


class _StackableHubAutoRecovState_Type(Integer32):
    """Custom type stackableHubAutoRecovState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("halted", 3),
          ("in-recovery", 1),
          ("normal", 2))
    )


_StackableHubAutoRecovState_Type.__name__ = "Integer32"
_StackableHubAutoRecovState_Object = MibTableColumn
stackableHubAutoRecovState = _StackableHubAutoRecovState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 30),
    _StackableHubAutoRecovState_Type()
)
stackableHubAutoRecovState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubAutoRecovState.setStatus("mandatory")


class _StackableHubRawCommandData_Type(OctetString):
    """Custom type stackableHubRawCommandData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_StackableHubRawCommandData_Type.__name__ = "OctetString"
_StackableHubRawCommandData_Object = MibTableColumn
stackableHubRawCommandData = _StackableHubRawCommandData_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 31),
    _StackableHubRawCommandData_Type()
)
stackableHubRawCommandData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubRawCommandData.setStatus("mandatory")


class _StackableHubAutoRecovMode_Type(Integer32):
    """Custom type stackableHubAutoRecovMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-selfEnabling", 2),
          ("selfEnabling", 1))
    )


_StackableHubAutoRecovMode_Type.__name__ = "Integer32"
_StackableHubAutoRecovMode_Object = MibTableColumn
stackableHubAutoRecovMode = _StackableHubAutoRecovMode_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 2, 1, 32),
    _StackableHubAutoRecovMode_Type()
)
stackableHubAutoRecovMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubAutoRecovMode.setStatus("mandatory")
_StackableHubLobeNumber_Type = Integer32
_StackableHubLobeNumber_Object = MibScalar
stackableHubLobeNumber = _StackableHubLobeNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 3),
    _StackableHubLobeNumber_Type()
)
stackableHubLobeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubLobeNumber.setStatus("mandatory")
_StackableHubLobeTable_Object = MibTable
stackableHubLobeTable = _StackableHubLobeTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4)
)
if mibBuilder.loadTexts:
    stackableHubLobeTable.setStatus("mandatory")
_StackableHubLobeEntry_Object = MibTableRow
stackableHubLobeEntry = _StackableHubLobeEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4, 1)
)
stackableHubLobeEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "stackableHubIndex"),
    (0, "STARTEK-PRIVATE-MIB", "stackableHubLobePort"),
)
if mibBuilder.loadTexts:
    stackableHubLobeEntry.setStatus("mandatory")
_StackableHubIndex_Type = Integer32
_StackableHubIndex_Object = MibTableColumn
stackableHubIndex = _StackableHubIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4, 1, 1),
    _StackableHubIndex_Type()
)
stackableHubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubIndex.setStatus("mandatory")
_StackableHubLobePort_Type = Integer32
_StackableHubLobePort_Object = MibTableColumn
stackableHubLobePort = _StackableHubLobePort_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4, 1, 2),
    _StackableHubLobePort_Type()
)
stackableHubLobePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubLobePort.setStatus("mandatory")


class _StackableHubLobePhDet_Type(Integer32):
    """Custom type stackableHubLobePhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_StackableHubLobePhDet_Type.__name__ = "Integer32"
_StackableHubLobePhDet_Object = MibTableColumn
stackableHubLobePhDet = _StackableHubLobePhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4, 1, 3),
    _StackableHubLobePhDet_Type()
)
stackableHubLobePhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubLobePhDet.setStatus("mandatory")


class _StackableHubLobeMask_Type(Integer32):
    """Custom type stackableHubLobeMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("isolated", 1))
    )


_StackableHubLobeMask_Type.__name__ = "Integer32"
_StackableHubLobeMask_Object = MibTableColumn
stackableHubLobeMask = _StackableHubLobeMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4, 1, 4),
    _StackableHubLobeMask_Type()
)
stackableHubLobeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    stackableHubLobeMask.setStatus("mandatory")


class _StackableHubLobeNsrtStatus_Type(Integer32):
    """Custom type stackableHubLobeNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_StackableHubLobeNsrtStatus_Type.__name__ = "Integer32"
_StackableHubLobeNsrtStatus_Object = MibTableColumn
stackableHubLobeNsrtStatus = _StackableHubLobeNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4, 1, 5),
    _StackableHubLobeNsrtStatus_Type()
)
stackableHubLobeNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubLobeNsrtStatus.setStatus("mandatory")


class _StackableHubLobeMacAddr_Type(OctetString):
    """Custom type stackableHubLobeMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_StackableHubLobeMacAddr_Type.__name__ = "OctetString"
_StackableHubLobeMacAddr_Object = MibTableColumn
stackableHubLobeMacAddr = _StackableHubLobeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4, 1, 6),
    _StackableHubLobeMacAddr_Type()
)
stackableHubLobeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubLobeMacAddr.setStatus("mandatory")


class _StackableHubLobeBcnRemStatus_Type(Integer32):
    """Custom type stackableHubLobeBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_StackableHubLobeBcnRemStatus_Type.__name__ = "Integer32"
_StackableHubLobeBcnRemStatus_Object = MibTableColumn
stackableHubLobeBcnRemStatus = _StackableHubLobeBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4, 1, 7),
    _StackableHubLobeBcnRemStatus_Type()
)
stackableHubLobeBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubLobeBcnRemStatus.setStatus("mandatory")


class _StackableHubLobeBcnRemCause_Type(Integer32):
    """Custom type stackableHubLobeBcnRemCause based on Integer32"""
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
        *(("bad-rate", 4),
          ("no-carrier", 3),
          ("no-removal", 1),
          ("phantom-error", 2),
          ("unknown", 5))
    )


_StackableHubLobeBcnRemCause_Type.__name__ = "Integer32"
_StackableHubLobeBcnRemCause_Object = MibTableColumn
stackableHubLobeBcnRemCause = _StackableHubLobeBcnRemCause_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4, 1, 8),
    _StackableHubLobeBcnRemCause_Type()
)
stackableHubLobeBcnRemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubLobeBcnRemCause.setStatus("mandatory")
_StackableHubLobeTimeStamp_Type = TimeTicks
_StackableHubLobeTimeStamp_Object = MibTableColumn
stackableHubLobeTimeStamp = _StackableHubLobeTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 1, 4, 1, 9),
    _StackableHubLobeTimeStamp_Type()
)
stackableHubLobeTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    stackableHubLobeTimeStamp.setStatus("mandatory")
_SuperStackHubs_ObjectIdentity = ObjectIdentity
superStackHubs = _SuperStackHubs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2)
)
_SuperStackHubNumber_Type = Integer32
_SuperStackHubNumber_Object = MibScalar
superStackHubNumber = _SuperStackHubNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 1),
    _SuperStackHubNumber_Type()
)
superStackHubNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubNumber.setStatus("mandatory")
_SuperStackHubTable_Object = MibTable
superStackHubTable = _SuperStackHubTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2)
)
if mibBuilder.loadTexts:
    superStackHubTable.setStatus("mandatory")
_SuperStackHubTableEntry_Object = MibTableRow
superStackHubTableEntry = _SuperStackHubTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1)
)
superStackHubTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "superStackHubTableIndex"),
)
if mibBuilder.loadTexts:
    superStackHubTableEntry.setStatus("mandatory")
_SuperStackHubTableIndex_Type = Integer32
_SuperStackHubTableIndex_Object = MibTableColumn
superStackHubTableIndex = _SuperStackHubTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 1),
    _SuperStackHubTableIndex_Type()
)
superStackHubTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubTableIndex.setStatus("mandatory")


class _SuperStackHubModel_Type(Integer32):
    """Custom type superStackHubModel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active-12-port-base-mau", 1),
          ("active-24-port-expansion-mau", 2))
    )


_SuperStackHubModel_Type.__name__ = "Integer32"
_SuperStackHubModel_Object = MibTableColumn
superStackHubModel = _SuperStackHubModel_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 2),
    _SuperStackHubModel_Type()
)
superStackHubModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubModel.setStatus("mandatory")


class _SuperStackHub485Address_Type(OctetString):
    """Custom type superStackHub485Address based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )


_SuperStackHub485Address_Type.__name__ = "OctetString"
_SuperStackHub485Address_Object = MibTableColumn
superStackHub485Address = _SuperStackHub485Address_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 3),
    _SuperStackHub485Address_Type()
)
superStackHub485Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHub485Address.setStatus("mandatory")
_SuperStackHubStackPosition_Type = Integer32
_SuperStackHubStackPosition_Object = MibTableColumn
superStackHubStackPosition = _SuperStackHubStackPosition_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 4),
    _SuperStackHubStackPosition_Type()
)
superStackHubStackPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubStackPosition.setStatus("mandatory")


class _SuperStackRiConfiguration_Type(Integer32):
    """Custom type superStackRiConfiguration based on Integer32"""
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
        *(("copper-ring-in-configured", 2),
          ("copper-ring-in-disabled", 4),
          ("fiber-ring-in-configured", 3),
          ("fiber-ring-in-disabled", 5),
          ("no-ring-in-configured", 1))
    )


_SuperStackRiConfiguration_Type.__name__ = "Integer32"
_SuperStackRiConfiguration_Object = MibScalar
superStackRiConfiguration = _SuperStackRiConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 5),
    _SuperStackRiConfiguration_Type()
)
superStackRiConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackRiConfiguration.setStatus("mandatory")


class _SuperStackHubRiFTolState_Type(Integer32):
    """Custom type superStackHubRiFTolState based on Integer32"""
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


_SuperStackHubRiFTolState_Type.__name__ = "Integer32"
_SuperStackHubRiFTolState_Object = MibTableColumn
superStackHubRiFTolState = _SuperStackHubRiFTolState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 6),
    _SuperStackHubRiFTolState_Type()
)
superStackHubRiFTolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubRiFTolState.setStatus("mandatory")


class _SuperStackHubRiMask_Type(Integer32):
    """Custom type superStackHubRiMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("isolate", 1))
    )


_SuperStackHubRiMask_Type.__name__ = "Integer32"
_SuperStackHubRiMask_Object = MibTableColumn
superStackHubRiMask = _SuperStackHubRiMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 7),
    _SuperStackHubRiMask_Type()
)
superStackHubRiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubRiMask.setStatus("mandatory")


class _SuperStackHubRiPhDet_Type(Integer32):
    """Custom type superStackHubRiPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_SuperStackHubRiPhDet_Type.__name__ = "Integer32"
_SuperStackHubRiPhDet_Object = MibTableColumn
superStackHubRiPhDet = _SuperStackHubRiPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 8),
    _SuperStackHubRiPhDet_Type()
)
superStackHubRiPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRiPhDet.setStatus("mandatory")


class _SuperStackHubRiNsrtStatus_Type(Integer32):
    """Custom type superStackHubRiNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_SuperStackHubRiNsrtStatus_Type.__name__ = "Integer32"
_SuperStackHubRiNsrtStatus_Object = MibTableColumn
superStackHubRiNsrtStatus = _SuperStackHubRiNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 9),
    _SuperStackHubRiNsrtStatus_Type()
)
superStackHubRiNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRiNsrtStatus.setStatus("mandatory")


class _SuperStackHubRiBcnRemStatus_Type(Integer32):
    """Custom type superStackHubRiBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1))
    )


_SuperStackHubRiBcnRemStatus_Type.__name__ = "Integer32"
_SuperStackHubRiBcnRemStatus_Object = MibTableColumn
superStackHubRiBcnRemStatus = _SuperStackHubRiBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 10),
    _SuperStackHubRiBcnRemStatus_Type()
)
superStackHubRiBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRiBcnRemStatus.setStatus("mandatory")


class _SuperStackRoConfiguration_Type(Integer32):
    """Custom type superStackRoConfiguration based on Integer32"""
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
        *(("copper-ring-out-configured", 2),
          ("copper-ring-out-disabled", 4),
          ("fiber-ring-out-configured", 3),
          ("fiber-ring-out-disabled", 5),
          ("no-ring-out-configured", 1))
    )


_SuperStackRoConfiguration_Type.__name__ = "Integer32"
_SuperStackRoConfiguration_Object = MibScalar
superStackRoConfiguration = _SuperStackRoConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 11),
    _SuperStackRoConfiguration_Type()
)
superStackRoConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackRoConfiguration.setStatus("mandatory")


class _SuperStackHubRoFTolState_Type(Integer32):
    """Custom type superStackHubRoFTolState based on Integer32"""
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


_SuperStackHubRoFTolState_Type.__name__ = "Integer32"
_SuperStackHubRoFTolState_Object = MibTableColumn
superStackHubRoFTolState = _SuperStackHubRoFTolState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 12),
    _SuperStackHubRoFTolState_Type()
)
superStackHubRoFTolState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubRoFTolState.setStatus("mandatory")


class _SuperStackHubRoMask_Type(Integer32):
    """Custom type superStackHubRoMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("isolate", 1))
    )


_SuperStackHubRoMask_Type.__name__ = "Integer32"
_SuperStackHubRoMask_Object = MibTableColumn
superStackHubRoMask = _SuperStackHubRoMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 13),
    _SuperStackHubRoMask_Type()
)
superStackHubRoMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubRoMask.setStatus("mandatory")


class _SuperStackHubRoPhDet_Type(Integer32):
    """Custom type superStackHubRoPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_SuperStackHubRoPhDet_Type.__name__ = "Integer32"
_SuperStackHubRoPhDet_Object = MibTableColumn
superStackHubRoPhDet = _SuperStackHubRoPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 14),
    _SuperStackHubRoPhDet_Type()
)
superStackHubRoPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRoPhDet.setStatus("mandatory")


class _SuperStackHubRoNsrtStatus_Type(Integer32):
    """Custom type superStackHubRoNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_SuperStackHubRoNsrtStatus_Type.__name__ = "Integer32"
_SuperStackHubRoNsrtStatus_Object = MibTableColumn
superStackHubRoNsrtStatus = _SuperStackHubRoNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 15),
    _SuperStackHubRoNsrtStatus_Type()
)
superStackHubRoNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRoNsrtStatus.setStatus("mandatory")


class _SuperStackHubRoBcnRemStatus_Type(Integer32):
    """Custom type superStackHubRoBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1))
    )


_SuperStackHubRoBcnRemStatus_Type.__name__ = "Integer32"
_SuperStackHubRoBcnRemStatus_Object = MibTableColumn
superStackHubRoBcnRemStatus = _SuperStackHubRoBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 16),
    _SuperStackHubRoBcnRemStatus_Type()
)
superStackHubRoBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRoBcnRemStatus.setStatus("mandatory")


class _SuperStackHubCascadeUpMask_Type(Integer32):
    """Custom type superStackHubCascadeUpMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("isolate", 1))
    )


_SuperStackHubCascadeUpMask_Type.__name__ = "Integer32"
_SuperStackHubCascadeUpMask_Object = MibTableColumn
superStackHubCascadeUpMask = _SuperStackHubCascadeUpMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 17),
    _SuperStackHubCascadeUpMask_Type()
)
superStackHubCascadeUpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubCascadeUpMask.setStatus("mandatory")


class _SuperStackHubCascadeUpPhDet_Type(Integer32):
    """Custom type superStackHubCascadeUpPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_SuperStackHubCascadeUpPhDet_Type.__name__ = "Integer32"
_SuperStackHubCascadeUpPhDet_Object = MibTableColumn
superStackHubCascadeUpPhDet = _SuperStackHubCascadeUpPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 18),
    _SuperStackHubCascadeUpPhDet_Type()
)
superStackHubCascadeUpPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubCascadeUpPhDet.setStatus("mandatory")


class _SuperStackHubCascadeUpNsrtStatus_Type(Integer32):
    """Custom type superStackHubCascadeUpNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_SuperStackHubCascadeUpNsrtStatus_Type.__name__ = "Integer32"
_SuperStackHubCascadeUpNsrtStatus_Object = MibTableColumn
superStackHubCascadeUpNsrtStatus = _SuperStackHubCascadeUpNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 19),
    _SuperStackHubCascadeUpNsrtStatus_Type()
)
superStackHubCascadeUpNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubCascadeUpNsrtStatus.setStatus("mandatory")


class _SuperStackHubCascadeUpBcnRemStatus_Type(Integer32):
    """Custom type superStackHubCascadeUpBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1))
    )


_SuperStackHubCascadeUpBcnRemStatus_Type.__name__ = "Integer32"
_SuperStackHubCascadeUpBcnRemStatus_Object = MibTableColumn
superStackHubCascadeUpBcnRemStatus = _SuperStackHubCascadeUpBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 20),
    _SuperStackHubCascadeUpBcnRemStatus_Type()
)
superStackHubCascadeUpBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubCascadeUpBcnRemStatus.setStatus("mandatory")


class _SuperStackHubCascadeDownMask_Type(Integer32):
    """Custom type superStackHubCascadeDownMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 2),
          ("isolate", 1))
    )


_SuperStackHubCascadeDownMask_Type.__name__ = "Integer32"
_SuperStackHubCascadeDownMask_Object = MibTableColumn
superStackHubCascadeDownMask = _SuperStackHubCascadeDownMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 21),
    _SuperStackHubCascadeDownMask_Type()
)
superStackHubCascadeDownMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubCascadeDownMask.setStatus("mandatory")


class _SuperStackHubCascadeDownPhDet_Type(Integer32):
    """Custom type superStackHubCascadeDownPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_SuperStackHubCascadeDownPhDet_Type.__name__ = "Integer32"
_SuperStackHubCascadeDownPhDet_Object = MibTableColumn
superStackHubCascadeDownPhDet = _SuperStackHubCascadeDownPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 22),
    _SuperStackHubCascadeDownPhDet_Type()
)
superStackHubCascadeDownPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubCascadeDownPhDet.setStatus("mandatory")


class _SuperStackHubCascadeDownNsrtStatus_Type(Integer32):
    """Custom type superStackHubCascadeDownNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_SuperStackHubCascadeDownNsrtStatus_Type.__name__ = "Integer32"
_SuperStackHubCascadeDownNsrtStatus_Object = MibTableColumn
superStackHubCascadeDownNsrtStatus = _SuperStackHubCascadeDownNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 23),
    _SuperStackHubCascadeDownNsrtStatus_Type()
)
superStackHubCascadeDownNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubCascadeDownNsrtStatus.setStatus("mandatory")


class _SuperStackHubCascadeDownBcnRemStatus_Type(Integer32):
    """Custom type superStackHubCascadeDownBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1))
    )


_SuperStackHubCascadeDownBcnRemStatus_Type.__name__ = "Integer32"
_SuperStackHubCascadeDownBcnRemStatus_Object = MibTableColumn
superStackHubCascadeDownBcnRemStatus = _SuperStackHubCascadeDownBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 24),
    _SuperStackHubCascadeDownBcnRemStatus_Type()
)
superStackHubCascadeDownBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubCascadeDownBcnRemStatus.setStatus("mandatory")


class _SuperStackHubDataRateState_Type(Integer32):
    """Custom type superStackHubDataRateState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoConfig", 3),
          ("s16Mbps", 2),
          ("s4Mbps", 1))
    )


_SuperStackHubDataRateState_Type.__name__ = "Integer32"
_SuperStackHubDataRateState_Object = MibTableColumn
superStackHubDataRateState = _SuperStackHubDataRateState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 25),
    _SuperStackHubDataRateState_Type()
)
superStackHubDataRateState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubDataRateState.setStatus("mandatory")
_SuperStackHubDeviceTimeStamp_Type = TimeTicks
_SuperStackHubDeviceTimeStamp_Object = MibScalar
superStackHubDeviceTimeStamp = _SuperStackHubDeviceTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 26),
    _SuperStackHubDeviceTimeStamp_Type()
)
superStackHubDeviceTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubDeviceTimeStamp.setStatus("mandatory")


class _SuperStackHubMgmtStatus_Type(Integer32):
    """Custom type superStackHubMgmtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("operational", 1))
    )


_SuperStackHubMgmtStatus_Type.__name__ = "Integer32"
_SuperStackHubMgmtStatus_Object = MibTableColumn
superStackHubMgmtStatus = _SuperStackHubMgmtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 27),
    _SuperStackHubMgmtStatus_Type()
)
superStackHubMgmtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubMgmtStatus.setStatus("mandatory")


class _SuperStackHubProxyAgentID_Type(OctetString):
    """Custom type superStackHubProxyAgentID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SuperStackHubProxyAgentID_Type.__name__ = "OctetString"
_SuperStackHubProxyAgentID_Object = MibTableColumn
superStackHubProxyAgentID = _SuperStackHubProxyAgentID_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 28),
    _SuperStackHubProxyAgentID_Type()
)
superStackHubProxyAgentID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubProxyAgentID.setStatus("mandatory")


class _SuperStackHubAttachedAgentType_Type(Integer32):
    """Custom type superStackHubAttachedAgentType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("advanced-960", 4),
          ("basic-68000", 3),
          ("none", 1),
          ("reserved1", 5),
          ("reserved2", 6),
          ("reserved3", 7),
          ("reserved4", 8),
          ("reserved5", 9),
          ("unknown", 2))
    )


_SuperStackHubAttachedAgentType_Type.__name__ = "Integer32"
_SuperStackHubAttachedAgentType_Object = MibTableColumn
superStackHubAttachedAgentType = _SuperStackHubAttachedAgentType_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 29),
    _SuperStackHubAttachedAgentType_Type()
)
superStackHubAttachedAgentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubAttachedAgentType.setStatus("mandatory")


class _SuperStackHubAttachedAgentState_Type(Integer32):
    """Custom type superStackHubAttachedAgentState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("agent-MAC-auto-isolated", 6),
          ("agent-MAC-mgmt-isolated", 7),
          ("duplicate-detected", 3),
          ("hardware-faulted", 5),
          ("management-disabled", 4),
          ("normal", 2),
          ("not-applicable", 1),
          ("reserved1", 8),
          ("reserved2", 9),
          ("reserved3", 10),
          ("reserved4", 11),
          ("reserved5", 12))
    )


_SuperStackHubAttachedAgentState_Type.__name__ = "Integer32"
_SuperStackHubAttachedAgentState_Object = MibTableColumn
superStackHubAttachedAgentState = _SuperStackHubAttachedAgentState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 30),
    _SuperStackHubAttachedAgentState_Type()
)
superStackHubAttachedAgentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubAttachedAgentState.setStatus("mandatory")


class _SuperStackHubAttachedAgentControl_Type(Integer32):
    """Custom type superStackHubAttachedAgentControl based on Integer32"""
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
        *(("disable", 2),
          ("enable", 1),
          ("enable-MAC-insertion", 3),
          ("isolate-MAC-insertion", 4),
          ("read-value", 5))
    )


_SuperStackHubAttachedAgentControl_Type.__name__ = "Integer32"
_SuperStackHubAttachedAgentControl_Object = MibTableColumn
superStackHubAttachedAgentControl = _SuperStackHubAttachedAgentControl_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 31),
    _SuperStackHubAttachedAgentControl_Type()
)
superStackHubAttachedAgentControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubAttachedAgentControl.setStatus("mandatory")


class _SuperStackHubTemperatureStatus_Type(Integer32):
    """Custom type superStackHubTemperatureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bad", 2),
          ("ok", 1))
    )


_SuperStackHubTemperatureStatus_Type.__name__ = "Integer32"
_SuperStackHubTemperatureStatus_Object = MibTableColumn
superStackHubTemperatureStatus = _SuperStackHubTemperatureStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 32),
    _SuperStackHubTemperatureStatus_Type()
)
superStackHubTemperatureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubTemperatureStatus.setStatus("mandatory")


class _SuperStackHubPowerStatus_Type(Integer32):
    """Custom type superStackHubPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("non-redundant-DC-power", 3),
          ("normal-AC-power", 1),
          ("normal-redundant-DC-power", 2))
    )


_SuperStackHubPowerStatus_Type.__name__ = "Integer32"
_SuperStackHubPowerStatus_Object = MibTableColumn
superStackHubPowerStatus = _SuperStackHubPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 33),
    _SuperStackHubPowerStatus_Type()
)
superStackHubPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubPowerStatus.setStatus("mandatory")


class _SuperStackHubAutoRecovControl_Type(Integer32):
    """Custom type superStackHubAutoRecovControl based on Integer32"""
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
        *(("disabled", 2),
          ("enabled", 1),
          ("reset", 3),
          ("unknown", 4))
    )


_SuperStackHubAutoRecovControl_Type.__name__ = "Integer32"
_SuperStackHubAutoRecovControl_Object = MibTableColumn
superStackHubAutoRecovControl = _SuperStackHubAutoRecovControl_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 34),
    _SuperStackHubAutoRecovControl_Type()
)
superStackHubAutoRecovControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubAutoRecovControl.setStatus("mandatory")


class _SuperStackHubAutoRecovRetries_Type(Integer32):
    """Custom type superStackHubAutoRecovRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SuperStackHubAutoRecovRetries_Type.__name__ = "Integer32"
_SuperStackHubAutoRecovRetries_Object = MibTableColumn
superStackHubAutoRecovRetries = _SuperStackHubAutoRecovRetries_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 35),
    _SuperStackHubAutoRecovRetries_Type()
)
superStackHubAutoRecovRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubAutoRecovRetries.setStatus("mandatory")


class _SuperStackHubCodeVersion_Type(OctetString):
    """Custom type superStackHubCodeVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_SuperStackHubCodeVersion_Type.__name__ = "OctetString"
_SuperStackHubCodeVersion_Object = MibTableColumn
superStackHubCodeVersion = _SuperStackHubCodeVersion_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 36),
    _SuperStackHubCodeVersion_Type()
)
superStackHubCodeVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubCodeVersion.setStatus("mandatory")


class _SuperStackHubAutoRecovState_Type(Integer32):
    """Custom type superStackHubAutoRecovState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("halted", 3),
          ("in-recovery", 1),
          ("normal", 2))
    )


_SuperStackHubAutoRecovState_Type.__name__ = "Integer32"
_SuperStackHubAutoRecovState_Object = MibTableColumn
superStackHubAutoRecovState = _SuperStackHubAutoRecovState_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 37),
    _SuperStackHubAutoRecovState_Type()
)
superStackHubAutoRecovState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubAutoRecovState.setStatus("mandatory")


class _SuperStackHubRawCommandData_Type(OctetString):
    """Custom type superStackHubRawCommandData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_SuperStackHubRawCommandData_Type.__name__ = "OctetString"
_SuperStackHubRawCommandData_Object = MibTableColumn
superStackHubRawCommandData = _SuperStackHubRawCommandData_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 38),
    _SuperStackHubRawCommandData_Type()
)
superStackHubRawCommandData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubRawCommandData.setStatus("mandatory")


class _SuperStackHubAutoRecovMode_Type(Integer32):
    """Custom type superStackHubAutoRecovMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-selfEnabling", 2),
          ("selfEnabling", 1))
    )


_SuperStackHubAutoRecovMode_Type.__name__ = "Integer32"
_SuperStackHubAutoRecovMode_Object = MibTableColumn
superStackHubAutoRecovMode = _SuperStackHubAutoRecovMode_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 39),
    _SuperStackHubAutoRecovMode_Type()
)
superStackHubAutoRecovMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubAutoRecovMode.setStatus("mandatory")


class _SuperStackHubRouterPortPhDet_Type(Integer32):
    """Custom type superStackHubRouterPortPhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_SuperStackHubRouterPortPhDet_Type.__name__ = "Integer32"
_SuperStackHubRouterPortPhDet_Object = MibTableColumn
superStackHubRouterPortPhDet = _SuperStackHubRouterPortPhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 40),
    _SuperStackHubRouterPortPhDet_Type()
)
superStackHubRouterPortPhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRouterPortPhDet.setStatus("mandatory")


class _SuperStackHubRouterPortMask_Type(Integer32):
    """Custom type superStackHubRouterPortMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("isolated", 1))
    )


_SuperStackHubRouterPortMask_Type.__name__ = "Integer32"
_SuperStackHubRouterPortMask_Object = MibTableColumn
superStackHubRouterPortMask = _SuperStackHubRouterPortMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 41),
    _SuperStackHubRouterPortMask_Type()
)
superStackHubRouterPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubRouterPortMask.setStatus("mandatory")


class _SuperStackHubRouterPortNsrtStatus_Type(Integer32):
    """Custom type superStackHubRouterPortNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_SuperStackHubRouterPortNsrtStatus_Type.__name__ = "Integer32"
_SuperStackHubRouterPortNsrtStatus_Object = MibTableColumn
superStackHubRouterPortNsrtStatus = _SuperStackHubRouterPortNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 42),
    _SuperStackHubRouterPortNsrtStatus_Type()
)
superStackHubRouterPortNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRouterPortNsrtStatus.setStatus("mandatory")


class _SuperStackHubRouterPortMacAddr_Type(OctetString):
    """Custom type superStackHubRouterPortMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SuperStackHubRouterPortMacAddr_Type.__name__ = "OctetString"
_SuperStackHubRouterPortMacAddr_Object = MibTableColumn
superStackHubRouterPortMacAddr = _SuperStackHubRouterPortMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 43),
    _SuperStackHubRouterPortMacAddr_Type()
)
superStackHubRouterPortMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRouterPortMacAddr.setStatus("mandatory")


class _SuperStackHubRouterPortBcnRemStatus_Type(Integer32):
    """Custom type superStackHubRouterPortBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_SuperStackHubRouterPortBcnRemStatus_Type.__name__ = "Integer32"
_SuperStackHubRouterPortBcnRemStatus_Object = MibTableColumn
superStackHubRouterPortBcnRemStatus = _SuperStackHubRouterPortBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 44),
    _SuperStackHubRouterPortBcnRemStatus_Type()
)
superStackHubRouterPortBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRouterPortBcnRemStatus.setStatus("mandatory")


class _SuperStackHubRouterPortBcnRemCause_Type(Integer32):
    """Custom type superStackHubRouterPortBcnRemCause based on Integer32"""
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
        *(("bad-rate", 4),
          ("no-carrier", 3),
          ("no-removal", 1),
          ("phantom-error", 2),
          ("unknown", 5))
    )


_SuperStackHubRouterPortBcnRemCause_Type.__name__ = "Integer32"
_SuperStackHubRouterPortBcnRemCause_Object = MibTableColumn
superStackHubRouterPortBcnRemCause = _SuperStackHubRouterPortBcnRemCause_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 2, 1, 45),
    _SuperStackHubRouterPortBcnRemCause_Type()
)
superStackHubRouterPortBcnRemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubRouterPortBcnRemCause.setStatus("mandatory")
_SuperStackHubLobeNumber_Type = Integer32
_SuperStackHubLobeNumber_Object = MibScalar
superStackHubLobeNumber = _SuperStackHubLobeNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 3),
    _SuperStackHubLobeNumber_Type()
)
superStackHubLobeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubLobeNumber.setStatus("mandatory")
_SuperStackHubLobeTable_Object = MibTable
superStackHubLobeTable = _SuperStackHubLobeTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4)
)
if mibBuilder.loadTexts:
    superStackHubLobeTable.setStatus("mandatory")
_SuperStackHubLobeEntry_Object = MibTableRow
superStackHubLobeEntry = _SuperStackHubLobeEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4, 1)
)
superStackHubLobeEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "superStackHubIndex"),
    (0, "STARTEK-PRIVATE-MIB", "superStackHubLobePort"),
)
if mibBuilder.loadTexts:
    superStackHubLobeEntry.setStatus("mandatory")
_SuperStackHubIndex_Type = Integer32
_SuperStackHubIndex_Object = MibTableColumn
superStackHubIndex = _SuperStackHubIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4, 1, 1),
    _SuperStackHubIndex_Type()
)
superStackHubIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubIndex.setStatus("mandatory")
_SuperStackHubLobePort_Type = Integer32
_SuperStackHubLobePort_Object = MibTableColumn
superStackHubLobePort = _SuperStackHubLobePort_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4, 1, 2),
    _SuperStackHubLobePort_Type()
)
superStackHubLobePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubLobePort.setStatus("mandatory")


class _SuperStackHubLobeConfig_Type(Integer32):
    """Custom type superStackHubLobeConfig based on Integer32"""
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
        *(("ring-in-unused", 3),
          ("ring-out-unused", 2),
          ("unknown", 4),
          ("user-normal", 1))
    )


_SuperStackHubLobeConfig_Type.__name__ = "Integer32"
_SuperStackHubLobeConfig_Object = MibTableColumn
superStackHubLobeConfig = _SuperStackHubLobeConfig_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4, 1, 3),
    _SuperStackHubLobeConfig_Type()
)
superStackHubLobeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubLobeConfig.setStatus("mandatory")


class _SuperStackHubLobePhDet_Type(Integer32):
    """Custom type superStackHubLobePhDet based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noPhantom", 1),
          ("phantDetected", 2))
    )


_SuperStackHubLobePhDet_Type.__name__ = "Integer32"
_SuperStackHubLobePhDet_Object = MibTableColumn
superStackHubLobePhDet = _SuperStackHubLobePhDet_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4, 1, 4),
    _SuperStackHubLobePhDet_Type()
)
superStackHubLobePhDet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubLobePhDet.setStatus("mandatory")


class _SuperStackHubLobeMask_Type(Integer32):
    """Custom type superStackHubLobeMask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 2),
          ("isolated", 1))
    )


_SuperStackHubLobeMask_Type.__name__ = "Integer32"
_SuperStackHubLobeMask_Object = MibTableColumn
superStackHubLobeMask = _SuperStackHubLobeMask_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4, 1, 5),
    _SuperStackHubLobeMask_Type()
)
superStackHubLobeMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    superStackHubLobeMask.setStatus("mandatory")


class _SuperStackHubLobeNsrtStatus_Type(Integer32):
    """Custom type superStackHubLobeNsrtStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bypassed", 1),
          ("inserted", 2))
    )


_SuperStackHubLobeNsrtStatus_Type.__name__ = "Integer32"
_SuperStackHubLobeNsrtStatus_Object = MibTableColumn
superStackHubLobeNsrtStatus = _SuperStackHubLobeNsrtStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4, 1, 6),
    _SuperStackHubLobeNsrtStatus_Type()
)
superStackHubLobeNsrtStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubLobeNsrtStatus.setStatus("mandatory")


class _SuperStackHubLobeMacAddr_Type(OctetString):
    """Custom type superStackHubLobeMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SuperStackHubLobeMacAddr_Type.__name__ = "OctetString"
_SuperStackHubLobeMacAddr_Object = MibTableColumn
superStackHubLobeMacAddr = _SuperStackHubLobeMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4, 1, 7),
    _SuperStackHubLobeMacAddr_Type()
)
superStackHubLobeMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubLobeMacAddr.setStatus("mandatory")


class _SuperStackHubLobeBcnRemStatus_Type(Integer32):
    """Custom type superStackHubLobeBcnRemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoIsolated", 2),
          ("ok", 1),
          ("unknown", 3))
    )


_SuperStackHubLobeBcnRemStatus_Type.__name__ = "Integer32"
_SuperStackHubLobeBcnRemStatus_Object = MibTableColumn
superStackHubLobeBcnRemStatus = _SuperStackHubLobeBcnRemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4, 1, 8),
    _SuperStackHubLobeBcnRemStatus_Type()
)
superStackHubLobeBcnRemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubLobeBcnRemStatus.setStatus("mandatory")


class _SuperStackHubLobeBcnRemCause_Type(Integer32):
    """Custom type superStackHubLobeBcnRemCause based on Integer32"""
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
        *(("bad-rate", 4),
          ("no-carrier", 3),
          ("no-removal", 1),
          ("phantom-error", 2),
          ("unknown", 5))
    )


_SuperStackHubLobeBcnRemCause_Type.__name__ = "Integer32"
_SuperStackHubLobeBcnRemCause_Object = MibTableColumn
superStackHubLobeBcnRemCause = _SuperStackHubLobeBcnRemCause_Object(
    (1, 3, 6, 1, 4, 1, 260, 1, 3, 2, 4, 1, 9),
    _SuperStackHubLobeBcnRemCause_Type()
)
superStackHubLobeBcnRemCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    superStackHubLobeBcnRemCause.setStatus("mandatory")
_Maintenance_ObjectIdentity = ObjectIdentity
maintenance = _Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 2)
)
_Managers_ObjectIdentity = ObjectIdentity
managers = _Managers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 2, 1)
)
_MgrNumber_Type = Integer32
_MgrNumber_Object = MibScalar
mgrNumber = _MgrNumber_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 1),
    _MgrNumber_Type()
)
mgrNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mgrNumber.setStatus("mandatory")


class _MgrAutoAdd_Type(Integer32):
    """Custom type mgrAutoAdd based on Integer32"""
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


_MgrAutoAdd_Type.__name__ = "Integer32"
_MgrAutoAdd_Object = MibScalar
mgrAutoAdd = _MgrAutoAdd_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 2),
    _MgrAutoAdd_Type()
)
mgrAutoAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrAutoAdd.setStatus("mandatory")


class _MgrAutoAge_Type(Integer32):
    """Custom type mgrAutoAge based on Integer32"""
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


_MgrAutoAge_Type.__name__ = "Integer32"
_MgrAutoAge_Object = MibScalar
mgrAutoAge = _MgrAutoAge_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 3),
    _MgrAutoAge_Type()
)
mgrAutoAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrAutoAge.setStatus("mandatory")
_MgrAgeInterval_Type = TimeTicks
_MgrAgeInterval_Object = MibScalar
mgrAgeInterval = _MgrAgeInterval_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 4),
    _MgrAgeInterval_Type()
)
mgrAgeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrAgeInterval.setStatus("mandatory")
_MgrTable_Object = MibTable
mgrTable = _MgrTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 5)
)
if mibBuilder.loadTexts:
    mgrTable.setStatus("mandatory")
_MgrEntry_Object = MibTableRow
mgrEntry = _MgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 5, 1)
)
mgrEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "mgrIndex"),
)
if mibBuilder.loadTexts:
    mgrEntry.setStatus("mandatory")
_MgrIndex_Type = Integer32
_MgrIndex_Object = MibTableColumn
mgrIndex = _MgrIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 5, 1, 1),
    _MgrIndex_Type()
)
mgrIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrIndex.setStatus("mandatory")
_MgrIpAddr_Type = IpAddress
_MgrIpAddr_Object = MibTableColumn
mgrIpAddr = _MgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 5, 1, 2),
    _MgrIpAddr_Type()
)
mgrIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrIpAddr.setStatus("mandatory")


class _MgrCommunity_Type(DisplayString):
    """Custom type mgrCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_MgrCommunity_Type.__name__ = "DisplayString"
_MgrCommunity_Object = MibTableColumn
mgrCommunity = _MgrCommunity_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 5, 1, 3),
    _MgrCommunity_Type()
)
mgrCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrCommunity.setStatus("mandatory")
_MgrTimeStamp_Type = TimeTicks
_MgrTimeStamp_Object = MibTableColumn
mgrTimeStamp = _MgrTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 5, 1, 4),
    _MgrTimeStamp_Type()
)
mgrTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrTimeStamp.setStatus("mandatory")


class _MgrStatus_Type(Integer32):
    """Custom type mgrStatus based on Integer32"""
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


_MgrStatus_Type.__name__ = "Integer32"
_MgrStatus_Object = MibTableColumn
mgrStatus = _MgrStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 5, 1, 5),
    _MgrStatus_Type()
)
mgrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrStatus.setStatus("mandatory")


class _MgrPhysAddr_Type(OctetString):
    """Custom type mgrPhysAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_MgrPhysAddr_Type.__name__ = "OctetString"
_MgrPhysAddr_Object = MibTableColumn
mgrPhysAddr = _MgrPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 5, 1, 6),
    _MgrPhysAddr_Type()
)
mgrPhysAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrPhysAddr.setStatus("mandatory")
_MgrInterfaceIndex_Type = Integer32
_MgrInterfaceIndex_Object = MibTableColumn
mgrInterfaceIndex = _MgrInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 1, 5, 1, 7),
    _MgrInterfaceIndex_Type()
)
mgrInterfaceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mgrInterfaceIndex.setStatus("mandatory")
_Versions_ObjectIdentity = ObjectIdentity
versions = _Versions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 2, 2)
)


class _VersionHardware_Type(OctetString):
    """Custom type versionHardware based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VersionHardware_Type.__name__ = "OctetString"
_VersionHardware_Object = MibScalar
versionHardware = _VersionHardware_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 2, 1),
    _VersionHardware_Type()
)
versionHardware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionHardware.setStatus("mandatory")


class _VersionEPROMFirmware_Type(OctetString):
    """Custom type versionEPROMFirmware based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VersionEPROMFirmware_Type.__name__ = "OctetString"
_VersionEPROMFirmware_Object = MibScalar
versionEPROMFirmware = _VersionEPROMFirmware_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 2, 2),
    _VersionEPROMFirmware_Type()
)
versionEPROMFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionEPROMFirmware.setStatus("mandatory")


class _VersionFLASHFirmware_Type(OctetString):
    """Custom type versionFLASHFirmware based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )


_VersionFLASHFirmware_Type.__name__ = "OctetString"
_VersionFLASHFirmware_Object = MibScalar
versionFLASHFirmware = _VersionFLASHFirmware_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 2, 3),
    _VersionFLASHFirmware_Type()
)
versionFLASHFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    versionFLASHFirmware.setStatus("mandatory")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 2, 3)
)
_ConfigEPROMSize_Type = Integer32
_ConfigEPROMSize_Object = MibScalar
configEPROMSize = _ConfigEPROMSize_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 1),
    _ConfigEPROMSize_Type()
)
configEPROMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configEPROMSize.setStatus("mandatory")
_ConfigFLASHSize_Type = Integer32
_ConfigFLASHSize_Object = MibScalar
configFLASHSize = _ConfigFLASHSize_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 2),
    _ConfigFLASHSize_Type()
)
configFLASHSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFLASHSize.setStatus("mandatory")
_ConfigFLASHCount_Type = Integer32
_ConfigFLASHCount_Object = MibScalar
configFLASHCount = _ConfigFLASHCount_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 3),
    _ConfigFLASHCount_Type()
)
configFLASHCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configFLASHCount.setStatus("mandatory")
_ConfigDRAMSize_Type = Integer32
_ConfigDRAMSize_Object = MibScalar
configDRAMSize = _ConfigDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 4),
    _ConfigDRAMSize_Type()
)
configDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDRAMSize.setStatus("mandatory")
_ConfigDRAMCount_Type = Integer32
_ConfigDRAMCount_Object = MibScalar
configDRAMCount = _ConfigDRAMCount_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 5),
    _ConfigDRAMCount_Type()
)
configDRAMCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configDRAMCount.setStatus("mandatory")
_ConfigRS232Number_Type = Integer32
_ConfigRS232Number_Object = MibScalar
configRS232Number = _ConfigRS232Number_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 6),
    _ConfigRS232Number_Type()
)
configRS232Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRS232Number.setStatus("mandatory")
_ConfigRS232PortTable_Object = MibTable
configRS232PortTable = _ConfigRS232PortTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7)
)
if mibBuilder.loadTexts:
    configRS232PortTable.setStatus("mandatory")
_ConfigRS232PortEntry_Object = MibTableRow
configRS232PortEntry = _ConfigRS232PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7, 1)
)
configRS232PortEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "configRS232PortIndex"),
)
if mibBuilder.loadTexts:
    configRS232PortEntry.setStatus("mandatory")
_ConfigRS232PortIndex_Type = Integer32
_ConfigRS232PortIndex_Object = MibTableColumn
configRS232PortIndex = _ConfigRS232PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7, 1, 1),
    _ConfigRS232PortIndex_Type()
)
configRS232PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRS232PortIndex.setStatus("mandatory")
_ConfigRS232PortName_Type = DisplayString
_ConfigRS232PortName_Object = MibTableColumn
configRS232PortName = _ConfigRS232PortName_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7, 1, 2),
    _ConfigRS232PortName_Type()
)
configRS232PortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRS232PortName.setStatus("mandatory")


class _ConfigRS232BaudRate_Type(Integer32):
    """Custom type configRS232BaudRate based on Integer32"""
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
        *(("b1200", 1),
          ("b19200", 5),
          ("b2400", 2),
          ("b38400", 6),
          ("b4800", 3),
          ("b9600", 4))
    )


_ConfigRS232BaudRate_Type.__name__ = "Integer32"
_ConfigRS232BaudRate_Object = MibTableColumn
configRS232BaudRate = _ConfigRS232BaudRate_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7, 1, 3),
    _ConfigRS232BaudRate_Type()
)
configRS232BaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRS232BaudRate.setStatus("mandatory")


class _ConfigRS232ModemStatus_Type(Integer32):
    """Custom type configRS232ModemStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autobauding", 2),
          ("modemDetected", 1),
          ("noModemDetected", 3))
    )


_ConfigRS232ModemStatus_Type.__name__ = "Integer32"
_ConfigRS232ModemStatus_Object = MibTableColumn
configRS232ModemStatus = _ConfigRS232ModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7, 1, 4),
    _ConfigRS232ModemStatus_Type()
)
configRS232ModemStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRS232ModemStatus.setStatus("mandatory")


class _ConfigRS232ConnectionStatus_Type(Integer32):
    """Custom type configRS232ConnectionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 1),
          ("connectionWait", 2),
          ("unknown", 3))
    )


_ConfigRS232ConnectionStatus_Type.__name__ = "Integer32"
_ConfigRS232ConnectionStatus_Object = MibTableColumn
configRS232ConnectionStatus = _ConfigRS232ConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7, 1, 5),
    _ConfigRS232ConnectionStatus_Type()
)
configRS232ConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRS232ConnectionStatus.setStatus("mandatory")


class _ConfigRS232ModemConfigString_Type(DisplayString):
    """Custom type configRS232ModemConfigString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_ConfigRS232ModemConfigString_Type.__name__ = "DisplayString"
_ConfigRS232ModemConfigString_Object = MibTableColumn
configRS232ModemConfigString = _ConfigRS232ModemConfigString_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7, 1, 6),
    _ConfigRS232ModemConfigString_Type()
)
configRS232ModemConfigString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRS232ModemConfigString.setStatus("mandatory")


class _ConfigRS232OutputData_Type(OctetString):
    """Custom type configRS232OutputData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_ConfigRS232OutputData_Type.__name__ = "OctetString"
_ConfigRS232OutputData_Object = MibTableColumn
configRS232OutputData = _ConfigRS232OutputData_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7, 1, 7),
    _ConfigRS232OutputData_Type()
)
configRS232OutputData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRS232OutputData.setStatus("mandatory")


class _ConfigRS232InputData_Type(OctetString):
    """Custom type configRS232InputData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_ConfigRS232InputData_Type.__name__ = "OctetString"
_ConfigRS232InputData_Object = MibTableColumn
configRS232InputData = _ConfigRS232InputData_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7, 1, 8),
    _ConfigRS232InputData_Type()
)
configRS232InputData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configRS232InputData.setStatus("mandatory")


class _ConfigRS232HardwareFlowControl_Type(Integer32):
    """Custom type configRS232HardwareFlowControl based on Integer32"""
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


_ConfigRS232HardwareFlowControl_Type.__name__ = "Integer32"
_ConfigRS232HardwareFlowControl_Object = MibTableColumn
configRS232HardwareFlowControl = _ConfigRS232HardwareFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 7, 1, 9),
    _ConfigRS232HardwareFlowControl_Type()
)
configRS232HardwareFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRS232HardwareFlowControl.setStatus("mandatory")


class _ConfigMonitorMode_Type(Integer32):
    """Custom type configMonitorMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 1),
          ("slip", 2))
    )


_ConfigMonitorMode_Type.__name__ = "Integer32"
_ConfigMonitorMode_Object = MibScalar
configMonitorMode = _ConfigMonitorMode_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 8),
    _ConfigMonitorMode_Type()
)
configMonitorMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMonitorMode.setStatus("mandatory")


class _ConfigMonitorInput_Type(Integer32):
    """Custom type configMonitorInput based on Integer32"""
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


_ConfigMonitorInput_Type.__name__ = "Integer32"
_ConfigMonitorInput_Object = MibScalar
configMonitorInput = _ConfigMonitorInput_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 9),
    _ConfigMonitorInput_Type()
)
configMonitorInput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMonitorInput.setStatus("mandatory")


class _ConfigMonitorDiags_Type(Integer32):
    """Custom type configMonitorDiags based on Integer32"""
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


_ConfigMonitorDiags_Type.__name__ = "Integer32"
_ConfigMonitorDiags_Object = MibScalar
configMonitorDiags = _ConfigMonitorDiags_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 10),
    _ConfigMonitorDiags_Type()
)
configMonitorDiags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMonitorDiags.setStatus("mandatory")


class _ConfigParseControl_Type(Integer32):
    """Custom type configParseControl based on Integer32"""
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
        *(("parseAll", 1),
          ("parseLess", 3),
          ("parseMost", 2),
          ("parseNone", 4))
    )


_ConfigParseControl_Type.__name__ = "Integer32"
_ConfigParseControl_Object = MibScalar
configParseControl = _ConfigParseControl_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 11),
    _ConfigParseControl_Type()
)
configParseControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configParseControl.setStatus("mandatory")


class _ConfigBootSource_Type(Integer32):
    """Custom type configBootSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eprom", 1),
          ("flash", 2))
    )


_ConfigBootSource_Type.__name__ = "Integer32"
_ConfigBootSource_Object = MibScalar
configBootSource = _ConfigBootSource_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 3, 12),
    _ConfigBootSource_Type()
)
configBootSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    configBootSource.setStatus("mandatory")
_Security_ObjectIdentity = ObjectIdentity
security = _Security_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 2, 4)
)


class _SecurityControl_Type(Integer32):
    """Custom type securityControl based on Integer32"""
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


_SecurityControl_Type.__name__ = "Integer32"
_SecurityControl_Object = MibScalar
securityControl = _SecurityControl_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 4, 1),
    _SecurityControl_Type()
)
securityControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityControl.setStatus("mandatory")
_SecurityMacAddressTable_Object = MibTable
securityMacAddressTable = _SecurityMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 4, 2)
)
if mibBuilder.loadTexts:
    securityMacAddressTable.setStatus("mandatory")
_SecurityMacAddressTableEntry_Object = MibTableRow
securityMacAddressTableEntry = _SecurityMacAddressTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 4, 2, 1)
)
securityMacAddressTableEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "pysmiFakeCol3"),
)
if mibBuilder.loadTexts:
    securityMacAddressTableEntry.setStatus("mandatory")


class _SecurityMacAddress_Type(OctetString):
    """Custom type securityMacAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )


_SecurityMacAddress_Type.__name__ = "OctetString"
_SecurityMacAddress_Object = MibTableColumn
securityMacAddress = _SecurityMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 4, 2, 1, 1),
    _SecurityMacAddress_Type()
)
securityMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityMacAddress.setStatus("mandatory")


class _SecurityStatus_Type(Integer32):
    """Custom type securityStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allowed", 1),
          ("disallowed", 2))
    )


_SecurityStatus_Type.__name__ = "Integer32"
_SecurityStatus_Object = MibTableColumn
securityStatus = _SecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 4, 2, 1, 2),
    _SecurityStatus_Type()
)
securityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    securityStatus.setStatus("mandatory")
_SecurityLockoutCount_Type = Counter32
_SecurityLockoutCount_Object = MibTableColumn
securityLockoutCount = _SecurityLockoutCount_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 4, 2, 1, 3),
    _SecurityLockoutCount_Type()
)
securityLockoutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    securityLockoutCount.setStatus("mandatory")
_PysmiFakeCol3_Type = Integer32
_PysmiFakeCol3_Object = MibTableColumn
pysmiFakeCol3 = _PysmiFakeCol3_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 4, 2, 1, 4294967295),
    _PysmiFakeCol3_Type()
)
pysmiFakeCol3.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol3.setStatus("mandatory")
_Recovery_ObjectIdentity = ObjectIdentity
recovery = _Recovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 2, 5)
)


class _RecoveryControl_Type(Integer32):
    """Custom type recoveryControl based on Integer32"""
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


_RecoveryControl_Type.__name__ = "Integer32"
_RecoveryControl_Object = MibScalar
recoveryControl = _RecoveryControl_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 5, 1),
    _RecoveryControl_Type()
)
recoveryControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recoveryControl.setStatus("mandatory")


class _Recovery828Support_Type(Integer32):
    """Custom type recovery828Support based on Integer32"""
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


_Recovery828Support_Type.__name__ = "Integer32"
_Recovery828Support_Object = MibScalar
recovery828Support = _Recovery828Support_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 5, 2),
    _Recovery828Support_Type()
)
recovery828Support.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recovery828Support.setStatus("mandatory")
_RecoveryRetryLimit_Type = Integer32
_RecoveryRetryLimit_Object = MibScalar
recoveryRetryLimit = _RecoveryRetryLimit_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 5, 3),
    _RecoveryRetryLimit_Type()
)
recoveryRetryLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recoveryRetryLimit.setStatus("mandatory")
_RecoveryRetryTimePeriod_Type = Integer32
_RecoveryRetryTimePeriod_Object = MibScalar
recoveryRetryTimePeriod = _RecoveryRetryTimePeriod_Object(
    (1, 3, 6, 1, 4, 1, 260, 2, 5, 4),
    _RecoveryRetryTimePeriod_Type()
)
recoveryRetryTimePeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    recoveryRetryTimePeriod.setStatus("mandatory")
_Rmonextns_ObjectIdentity = ObjectIdentity
rmonextns = _Rmonextns_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 4)
)
_Stationstatistics_ObjectIdentity = ObjectIdentity
stationstatistics = _Stationstatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 4, 1)
)
_Stationhistory_ObjectIdentity = ObjectIdentity
stationhistory = _Stationhistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 4, 2)
)
_TrHistoryTable_Object = MibTable
trHistoryTable = _TrHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1)
)
if mibBuilder.loadTexts:
    trHistoryTable.setStatus("mandatory")
_TrHistoryEntry_Object = MibTableRow
trHistoryEntry = _TrHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1)
)
trHistoryEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "trHistoryIndex"),
    (0, "STARTEK-PRIVATE-MIB", "trHistorySampleIndex"),
)
if mibBuilder.loadTexts:
    trHistoryEntry.setStatus("mandatory")


class _TrHistoryIndex_Type(Integer32):
    """Custom type trHistoryIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrHistoryIndex_Type.__name__ = "Integer32"
_TrHistoryIndex_Object = MibTableColumn
trHistoryIndex = _TrHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 1),
    _TrHistoryIndex_Type()
)
trHistoryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryIndex.setStatus("mandatory")
_TrHistorySampleIndex_Type = Integer32
_TrHistorySampleIndex_Object = MibTableColumn
trHistorySampleIndex = _TrHistorySampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 2),
    _TrHistorySampleIndex_Type()
)
trHistorySampleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistorySampleIndex.setStatus("mandatory")
_TrHistoryIntervalStart_Type = TimeTicks
_TrHistoryIntervalStart_Object = MibTableColumn
trHistoryIntervalStart = _TrHistoryIntervalStart_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 3),
    _TrHistoryIntervalStart_Type()
)
trHistoryIntervalStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryIntervalStart.setStatus("mandatory")
_TrHistoryInPkts_Type = Counter32
_TrHistoryInPkts_Object = MibTableColumn
trHistoryInPkts = _TrHistoryInPkts_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 4),
    _TrHistoryInPkts_Type()
)
trHistoryInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryInPkts.setStatus("mandatory")
_TrHistoryOutPkts_Type = Counter32
_TrHistoryOutPkts_Object = MibTableColumn
trHistoryOutPkts = _TrHistoryOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 5),
    _TrHistoryOutPkts_Type()
)
trHistoryOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryOutPkts.setStatus("mandatory")
_TrHistoryInOctets_Type = Counter32
_TrHistoryInOctets_Object = MibTableColumn
trHistoryInOctets = _TrHistoryInOctets_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 6),
    _TrHistoryInOctets_Type()
)
trHistoryInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryInOctets.setStatus("mandatory")
_TrHistoryOutOctets_Type = Counter32
_TrHistoryOutOctets_Object = MibTableColumn
trHistoryOutOctets = _TrHistoryOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 7),
    _TrHistoryOutOctets_Type()
)
trHistoryOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryOutOctets.setStatus("mandatory")
_TrHistoryOutBroadcastPkts_Type = Counter32
_TrHistoryOutBroadcastPkts_Object = MibTableColumn
trHistoryOutBroadcastPkts = _TrHistoryOutBroadcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 8),
    _TrHistoryOutBroadcastPkts_Type()
)
trHistoryOutBroadcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryOutBroadcastPkts.setStatus("mandatory")
_TrHistoryOutMulticastPkts_Type = Counter32
_TrHistoryOutMulticastPkts_Object = MibTableColumn
trHistoryOutMulticastPkts = _TrHistoryOutMulticastPkts_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 9),
    _TrHistoryOutMulticastPkts_Type()
)
trHistoryOutMulticastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryOutMulticastPkts.setStatus("mandatory")
_TrHistoryClaimTokenPkts_Type = Counter32
_TrHistoryClaimTokenPkts_Object = MibTableColumn
trHistoryClaimTokenPkts = _TrHistoryClaimTokenPkts_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 10),
    _TrHistoryClaimTokenPkts_Type()
)
trHistoryClaimTokenPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryClaimTokenPkts.setStatus("mandatory")
_TrHistoryInLineErrors_Type = Counter32
_TrHistoryInLineErrors_Object = MibTableColumn
trHistoryInLineErrors = _TrHistoryInLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 11),
    _TrHistoryInLineErrors_Type()
)
trHistoryInLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryInLineErrors.setStatus("mandatory")
_TrHistoryOutLineErrors_Type = Counter32
_TrHistoryOutLineErrors_Object = MibTableColumn
trHistoryOutLineErrors = _TrHistoryOutLineErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 12),
    _TrHistoryOutLineErrors_Type()
)
trHistoryOutLineErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryOutLineErrors.setStatus("mandatory")
_TrHistoryInternalErrors_Type = Counter32
_TrHistoryInternalErrors_Object = MibTableColumn
trHistoryInternalErrors = _TrHistoryInternalErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 13),
    _TrHistoryInternalErrors_Type()
)
trHistoryInternalErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryInternalErrors.setStatus("mandatory")
_TrHistoryInBurstErrors_Type = Counter32
_TrHistoryInBurstErrors_Object = MibTableColumn
trHistoryInBurstErrors = _TrHistoryInBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 14),
    _TrHistoryInBurstErrors_Type()
)
trHistoryInBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryInBurstErrors.setStatus("mandatory")
_TrHistoryOutBurstErrors_Type = Counter32
_TrHistoryOutBurstErrors_Object = MibTableColumn
trHistoryOutBurstErrors = _TrHistoryOutBurstErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 15),
    _TrHistoryOutBurstErrors_Type()
)
trHistoryOutBurstErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryOutBurstErrors.setStatus("mandatory")
_TrHistoryACErrors_Type = Counter32
_TrHistoryACErrors_Object = MibTableColumn
trHistoryACErrors = _TrHistoryACErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 16),
    _TrHistoryACErrors_Type()
)
trHistoryACErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryACErrors.setStatus("mandatory")
_TrHistoryAbortErrors_Type = Counter32
_TrHistoryAbortErrors_Object = MibTableColumn
trHistoryAbortErrors = _TrHistoryAbortErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 17),
    _TrHistoryAbortErrors_Type()
)
trHistoryAbortErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryAbortErrors.setStatus("mandatory")
_TrHistoryLostFrameErrors_Type = Counter32
_TrHistoryLostFrameErrors_Object = MibTableColumn
trHistoryLostFrameErrors = _TrHistoryLostFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 18),
    _TrHistoryLostFrameErrors_Type()
)
trHistoryLostFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryLostFrameErrors.setStatus("mandatory")
_TrHistoryCongestionErrors_Type = Counter32
_TrHistoryCongestionErrors_Object = MibTableColumn
trHistoryCongestionErrors = _TrHistoryCongestionErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 19),
    _TrHistoryCongestionErrors_Type()
)
trHistoryCongestionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryCongestionErrors.setStatus("mandatory")
_TrHistoryFrameCopiedErrors_Type = Counter32
_TrHistoryFrameCopiedErrors_Object = MibTableColumn
trHistoryFrameCopiedErrors = _TrHistoryFrameCopiedErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 20),
    _TrHistoryFrameCopiedErrors_Type()
)
trHistoryFrameCopiedErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryFrameCopiedErrors.setStatus("mandatory")
_TrHistoryFrequencyErrors_Type = Counter32
_TrHistoryFrequencyErrors_Object = MibTableColumn
trHistoryFrequencyErrors = _TrHistoryFrequencyErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 21),
    _TrHistoryFrequencyErrors_Type()
)
trHistoryFrequencyErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryFrequencyErrors.setStatus("optional")
_TrHistoryTokenErrors_Type = Counter32
_TrHistoryTokenErrors_Object = MibTableColumn
trHistoryTokenErrors = _TrHistoryTokenErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 22),
    _TrHistoryTokenErrors_Type()
)
trHistoryTokenErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryTokenErrors.setStatus("mandatory")
_TrHistoryInBeaconErrors_Type = Counter32
_TrHistoryInBeaconErrors_Object = MibTableColumn
trHistoryInBeaconErrors = _TrHistoryInBeaconErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 23),
    _TrHistoryInBeaconErrors_Type()
)
trHistoryInBeaconErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryInBeaconErrors.setStatus("mandatory")
_TrHistoryOutBeaconErrors_Type = Counter32
_TrHistoryOutBeaconErrors_Object = MibTableColumn
trHistoryOutBeaconErrors = _TrHistoryOutBeaconErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 24),
    _TrHistoryOutBeaconErrors_Type()
)
trHistoryOutBeaconErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryOutBeaconErrors.setStatus("mandatory")
_TrHistoryInsertions_Type = Counter32
_TrHistoryInsertions_Object = MibTableColumn
trHistoryInsertions = _TrHistoryInsertions_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 25),
    _TrHistoryInsertions_Type()
)
trHistoryInsertions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryInsertions.setStatus("mandatory")
_TrHistorySoftErrors_Type = Counter32
_TrHistorySoftErrors_Object = MibTableColumn
trHistorySoftErrors = _TrHistorySoftErrors_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 1, 1, 26),
    _TrHistorySoftErrors_Type()
)
trHistorySoftErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistorySoftErrors.setStatus("mandatory")
_TrHistoryOpaqueTable_Object = MibTable
trHistoryOpaqueTable = _TrHistoryOpaqueTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 2)
)
if mibBuilder.loadTexts:
    trHistoryOpaqueTable.setStatus("mandatory")
_TrHistoryOpaqueEntry_Object = MibTableRow
trHistoryOpaqueEntry = _TrHistoryOpaqueEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 2, 1)
)
trHistoryOpaqueEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "pysmiFakeCol4"),
    (0, "STARTEK-PRIVATE-MIB", "pysmiFakeCol5"),
)
if mibBuilder.loadTexts:
    trHistoryOpaqueEntry.setStatus("mandatory")
_TrHistoryTableData_Type = Opaque
_TrHistoryTableData_Object = MibTableColumn
trHistoryTableData = _TrHistoryTableData_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 2, 1, 1),
    _TrHistoryTableData_Type()
)
trHistoryTableData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trHistoryTableData.setStatus("mandatory")
_PysmiFakeCol5_Type = Integer32
_PysmiFakeCol5_Object = MibTableColumn
pysmiFakeCol5 = _PysmiFakeCol5_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 2, 1, 4294967294),
    _PysmiFakeCol5_Type()
)
pysmiFakeCol5.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol5.setStatus("mandatory")
_PysmiFakeCol4_Type = Integer32
_PysmiFakeCol4_Object = MibTableColumn
pysmiFakeCol4 = _PysmiFakeCol4_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 2, 2, 1, 4294967295),
    _PysmiFakeCol4_Type()
)
pysmiFakeCol4.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pysmiFakeCol4.setStatus("mandatory")
_Protocolstatistics_ObjectIdentity = ObjectIdentity
protocolstatistics = _Protocolstatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 260, 4, 3)
)
_ProtocolData_Type = Opaque
_ProtocolData_Object = MibScalar
protocolData = _ProtocolData_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 3, 1),
    _ProtocolData_Type()
)
protocolData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolData.setStatus("mandatory")
_ProtocolStatsTable_Object = MibTable
protocolStatsTable = _ProtocolStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 3, 2)
)
if mibBuilder.loadTexts:
    protocolStatsTable.setStatus("mandatory")
_ProtocolStatsEntry_Object = MibTableRow
protocolStatsEntry = _ProtocolStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 3, 2, 1)
)
protocolStatsEntry.setIndexNames(
    (0, "STARTEK-PRIVATE-MIB", "protocolIfIndex"),
    (0, "STARTEK-PRIVATE-MIB", "protocolID"),
)
if mibBuilder.loadTexts:
    protocolStatsEntry.setStatus("mandatory")


class _ProtocolIfIndex_Type(Integer32):
    """Custom type protocolIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ProtocolIfIndex_Type.__name__ = "Integer32"
_ProtocolIfIndex_Object = MibTableColumn
protocolIfIndex = _ProtocolIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 3, 2, 1, 1),
    _ProtocolIfIndex_Type()
)
protocolIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolIfIndex.setStatus("mandatory")


class _ProtocolID_Type(Integer32):
    """Custom type protocolID based on Integer32"""
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
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51,
              52,
              53,
              54,
              55,
              56,
              57,
              58,
              59,
              60,
              61,
              62,
              63,
              64,
              65,
              66,
              67,
              68,
              69,
              70,
              71,
              72,
              73,
              74,
              75,
              76,
              77,
              78,
              79,
              80,
              81,
              82)
        )
    )
    namedValues = NamedValues(
        *(("all-packets", 1),
          ("appletalk", 40),
          ("arp", 19),
          ("banyan-vines", 36),
          ("chaosnet", 35),
          ("dec-lanbridge", 39),
          ("dec-lat", 38),
          ("decnet", 37),
          ("dix-ethernet-packets", 6),
          ("ieee8022-llc-protocol", 7),
          ("ieee8022-llc-snap", 8),
          ("ieee8025-mac-protocol", 3),
          ("ieee8025-nonsource-routed-packets", 5),
          ("ieee8025-source-routed-packets", 4),
          ("ip", 9),
          ("ip-chaos", 15),
          ("ip-egp", 13),
          ("ip-gcp", 11),
          ("ip-icmp", 10),
          ("ip-igp", 14),
          ("ip-other", 18),
          ("ip-tcp", 12),
          ("ip-tp4", 17),
          ("ip-udp", 16),
          ("ipx-echopacket", 44),
          ("ipx-errorpacket", 45),
          ("ipx-netwarecoreprotocol", 48),
          ("ipx-other", 49),
          ("ipx-packetexchangeprotocol", 46),
          ("ipx-routinginformationpacket", 43),
          ("ipx-sequencedpacketprotocol", 47),
          ("ipx-uknown", 42),
          ("llc-3com-xns-sap", 27),
          ("llc-arpanet-ip-sap", 26),
          ("llc-global-sap", 33),
          ("llc-group-lan-mgmt-sap", 30),
          ("llc-group-mgmt-sap", 23),
          ("llc-group-sna-path-ctrl-sap", 25),
          ("llc-individual-lan-mgmt-sap", 29),
          ("llc-individual-mgmt-sap", 22),
          ("llc-individual-sna-path-ctrl-sap", 24),
          ("llc-iso-network-layer-sap", 32),
          ("llc-netbios-sap", 28),
          ("llc-null-sap", 21),
          ("llc-remote-program-load-sap", 31),
          ("llc-startekdiscovery", 61),
          ("ncp", 50),
          ("ncp-create", 51),
          ("ncp-destroyserviceconnection", 54),
          ("ncp-other", 56),
          ("ncp-reply", 53),
          ("ncp-request", 52),
          ("ncp-requestinprogressresponse", 55),
          ("netware-ipx", 20),
          ("other-llc-sap", 34),
          ("reserved62", 62),
          ("reserved63", 63),
          ("reserved64", 64),
          ("reserved65", 65),
          ("reserved66", 66),
          ("reserved67", 67),
          ("reserved68", 68),
          ("reserved69", 69),
          ("reserved70", 70),
          ("reserved71", 71),
          ("reserved72", 72),
          ("reserved73", 73),
          ("reserved74", 74),
          ("reserved75", 75),
          ("reserved76", 76),
          ("reserved77", 77),
          ("reserved78", 78),
          ("reserved79", 79),
          ("reserved80", 80),
          ("reserved81", 81),
          ("reserved82", 82),
          ("sap-generalservicequery", 57),
          ("sap-generalserviceresponse", 58),
          ("sap-nearestserverquery", 59),
          ("sap-nearestserverresponse", 60),
          ("unknown-protocols", 2),
          ("xerox-3com", 41))
    )


_ProtocolID_Type.__name__ = "Integer32"
_ProtocolID_Object = MibTableColumn
protocolID = _ProtocolID_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 3, 2, 1, 2),
    _ProtocolID_Type()
)
protocolID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolID.setStatus("mandatory")
_ProtocolPkts_Type = Counter32
_ProtocolPkts_Object = MibTableColumn
protocolPkts = _ProtocolPkts_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 3, 2, 1, 3),
    _ProtocolPkts_Type()
)
protocolPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolPkts.setStatus("mandatory")
_ProtocolOctets_Type = Counter32
_ProtocolOctets_Object = MibTableColumn
protocolOctets = _ProtocolOctets_Object(
    (1, 3, 6, 1, 4, 1, 260, 4, 3, 2, 1, 4),
    _ProtocolOctets_Type()
)
protocolOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protocolOctets.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "STARTEK-PRIVATE-MIB",
    **{"startek": startek,
       "products": products,
       "m828Series": m828Series,
       "m828Hubs": m828Hubs,
       "m828HubNumber": m828HubNumber,
       "m828HubTable": m828HubTable,
       "m828HubTableEntry": m828HubTableEntry,
       "m828HubTableIndex": m828HubTableIndex,
       "m828HubModel": m828HubModel,
       "m828Hub485Address": m828Hub485Address,
       "m828HubRiFTolSw": m828HubRiFTolSw,
       "m828HubRiFTolState": m828HubRiFTolState,
       "m828HubRiMask": m828HubRiMask,
       "m828HubRiPhDet": m828HubRiPhDet,
       "m828HubRiNsrtStatus": m828HubRiNsrtStatus,
       "m828HubRiBcnRemStatus": m828HubRiBcnRemStatus,
       "m828RiNeighborType": m828RiNeighborType,
       "m828RiNeighborAddr": m828RiNeighborAddr,
       "m828RiTimeStamp": m828RiTimeStamp,
       "m828HubRoFTolSw": m828HubRoFTolSw,
       "m828HubRoFTolState": m828HubRoFTolState,
       "m828HubRoMask": m828HubRoMask,
       "m828HubRoPhDet": m828HubRoPhDet,
       "m828HubRoNsrtStatus": m828HubRoNsrtStatus,
       "m828HubRoBcnRemStatus": m828HubRoBcnRemStatus,
       "m828RoNeighborType": m828RoNeighborType,
       "m828RoNeighborAddr": m828RoNeighborAddr,
       "m828RoTimeStamp": m828RoTimeStamp,
       "m828HubDataRateSwitch": m828HubDataRateSwitch,
       "m828HubDataRateState": m828HubDataRateState,
       "m828HubDataRateTimeStamp": m828HubDataRateTimeStamp,
       "m828HubMgmtStatus": m828HubMgmtStatus,
       "m828HubProxyAgentID": m828HubProxyAgentID,
       "m828HubCodeVersion": m828HubCodeVersion,
       "m828HubRawCommandData": m828HubRawCommandData,
       "m828HubLobeNumber": m828HubLobeNumber,
       "m828HubLobeTable": m828HubLobeTable,
       "m828HubLobeEntry": m828HubLobeEntry,
       "m828HubIndex": m828HubIndex,
       "m828HubLobePort": m828HubLobePort,
       "m828HubLobePhDet": m828HubLobePhDet,
       "m828HubLobeMask": m828HubLobeMask,
       "m828HubLobeNsrtStatus": m828HubLobeNsrtStatus,
       "m828HubLobeMacAddr": m828HubLobeMacAddr,
       "m828HubLobeBcnRemStatus": m828HubLobeBcnRemStatus,
       "m828HubLobeTimeStamp": m828HubLobeTimeStamp,
       "fSeries": fSeries,
       "fChassis": fChassis,
       "fChassisNumber": fChassisNumber,
       "fChassisTable": fChassisTable,
       "fChassisTableEntry": fChassisTableEntry,
       "fChassisIndex": fChassisIndex,
       "fChassisModel": fChassisModel,
       "fChassisPowStatus": fChassisPowStatus,
       "fChassisLocation": fChassisLocation,
       "fTRMainRing": fTRMainRing,
       "fTRMainRingNumber": fTRMainRingNumber,
       "fTRMainRingTable": fTRMainRingTable,
       "fTRMainRingTableEntry": fTRMainRingTableEntry,
       "fTRMainRingTableIndex": fTRMainRingTableIndex,
       "fTRMainRingModel": fTRMainRingModel,
       "fTRMainRing485Address": fTRMainRing485Address,
       "fTRMainRingSlotIndex": fTRMainRingSlotIndex,
       "fTRMainRingChassisIndex": fTRMainRingChassisIndex,
       "fTRMainRingRiFTolState": fTRMainRingRiFTolState,
       "fTRMainRingRiMask": fTRMainRingRiMask,
       "fTRMainRingRiPhDet": fTRMainRingRiPhDet,
       "fTRMainRingRiNsrtStatus": fTRMainRingRiNsrtStatus,
       "fTRMainRingRiBcnRemStatus": fTRMainRingRiBcnRemStatus,
       "fTRMainRingRiCableType": fTRMainRingRiCableType,
       "fTRMainRingRiNghbrType": fTRMainRingRiNghbrType,
       "fTRMainRingRiNghbrAddr": fTRMainRingRiNghbrAddr,
       "fTRMainRingRiTimeStamp": fTRMainRingRiTimeStamp,
       "fTRMainRingRoFTolState": fTRMainRingRoFTolState,
       "fTRMainRingRoMask": fTRMainRingRoMask,
       "fTRMainRingRoPhDet": fTRMainRingRoPhDet,
       "fTRMainRingRoNsrtStatus": fTRMainRingRoNsrtStatus,
       "fTRMainRingRoBcnRemStatus": fTRMainRingRoBcnRemStatus,
       "fTRMainRingRoCableType": fTRMainRingRoCableType,
       "fTRMainRingRoNghbrType": fTRMainRingRoNghbrType,
       "fTRMainRingRoNghbrAddr": fTRMainRingRoNghbrAddr,
       "fTRMainRingRoTimeStamp": fTRMainRingRoTimeStamp,
       "fTRMainRingDataRateState": fTRMainRingDataRateState,
       "fTRMainRingDataRateTimeStamp": fTRMainRingDataRateTimeStamp,
       "fTRMainRingBkPlnNsrtState": fTRMainRingBkPlnNsrtState,
       "fTRMainRingBkPlnTimeStamp": fTRMainRingBkPlnTimeStamp,
       "fTRMainRingLobePhDet": fTRMainRingLobePhDet,
       "fTRMainRingLobeMask": fTRMainRingLobeMask,
       "fTRMainRingLobeNsrtStatus": fTRMainRingLobeNsrtStatus,
       "fTRMainRingLobeMacAddr": fTRMainRingLobeMacAddr,
       "fTRMainRingLobeBcnRemStatus": fTRMainRingLobeBcnRemStatus,
       "fTRMainRingLobeTimeStamp": fTRMainRingLobeTimeStamp,
       "fTRMainRingMgmtStatus": fTRMainRingMgmtStatus,
       "fTRMainRingProxyAgentID": fTRMainRingProxyAgentID,
       "fTRMainRingAttachedAgentType": fTRMainRingAttachedAgentType,
       "fTRMainRingAttachedAgentState": fTRMainRingAttachedAgentState,
       "fTRMainRingTemperatureStatus": fTRMainRingTemperatureStatus,
       "fTRMainRingAutoRecovControl": fTRMainRingAutoRecovControl,
       "fTRMainRingAutoRecovRetries": fTRMainRingAutoRecovRetries,
       "fTRMainRingCodeVersion": fTRMainRingCodeVersion,
       "fTRMainRingAutoRecovState": fTRMainRingAutoRecovState,
       "fTRMainRingRawCommandData": fTRMainRingRawCommandData,
       "fTRMainRingPowerStatus": fTRMainRingPowerStatus,
       "fTRMainRingCageType": fTRMainRingCageType,
       "fTRMainRingAutoRecovMode": fTRMainRingAutoRecovMode,
       "fTRLobe": fTRLobe,
       "fTRLobeNumber": fTRLobeNumber,
       "fTRLobeTable": fTRLobeTable,
       "fTRLobeTableEntry": fTRLobeTableEntry,
       "fTRLobeTableIndex": fTRLobeTableIndex,
       "fTRLobeModel": fTRLobeModel,
       "fTRLobe485Address": fTRLobe485Address,
       "fTRLobeSlotIndex": fTRLobeSlotIndex,
       "fTRLobeChassisIndex": fTRLobeChassisIndex,
       "fTRLobeDataRateState": fTRLobeDataRateState,
       "fTRLobeDataRateTimeStamp": fTRLobeDataRateTimeStamp,
       "fTRLobeBkPlnNsrtState": fTRLobeBkPlnNsrtState,
       "fTRLobeBkPlnTimeStamp": fTRLobeBkPlnTimeStamp,
       "fTRLobeMgmtStatus": fTRLobeMgmtStatus,
       "fTRLobeProxyAgentID": fTRLobeProxyAgentID,
       "fTRLobeTemperatureStatus": fTRLobeTemperatureStatus,
       "fTRLobeAutoRecovControl": fTRLobeAutoRecovControl,
       "fTRLobeAutoRecovMode": fTRLobeAutoRecovMode,
       "fTRLobeAutoRecovRetries": fTRLobeAutoRecovRetries,
       "fTRLobeCodeVersion": fTRLobeCodeVersion,
       "fTRLobeAutoRecovState": fTRLobeAutoRecovState,
       "fTRLobeRawCommandData": fTRLobeRawCommandData,
       "fTRLobePowerStatus": fTRLobePowerStatus,
       "fTRLobeCageType": fTRLobeCageType,
       "fTRLobeConnectNumber": fTRLobeConnectNumber,
       "fTRLobeConnectTable": fTRLobeConnectTable,
       "fTRLobeConnectEntry": fTRLobeConnectEntry,
       "fTRLobeIndex": fTRLobeIndex,
       "fTRLobeConnectPort": fTRLobeConnectPort,
       "fTRLobeConnectPhDet": fTRLobeConnectPhDet,
       "fTRLobeConnectMask": fTRLobeConnectMask,
       "fTRLobeConnectNsrtStatus": fTRLobeConnectNsrtStatus,
       "fTRLobeConnectMacAddr": fTRLobeConnectMacAddr,
       "fTRLobeConnectBcnRemStatus": fTRLobeConnectBcnRemStatus,
       "fTRLobeConnectBcnRemCause": fTRLobeConnectBcnRemCause,
       "fTRLobeConnectTimeStamp": fTRLobeConnectTimeStamp,
       "fEthernet": fEthernet,
       "fEthernetNumber": fEthernetNumber,
       "fEthernetTable": fEthernetTable,
       "fEthernetTableEntry": fEthernetTableEntry,
       "fEthernetTableIndex": fEthernetTableIndex,
       "fEthernetModel": fEthernetModel,
       "fEthernet485Address": fEthernet485Address,
       "fEthernetSlotIndex": fEthernetSlotIndex,
       "fEthernetChassisIndex": fEthernetChassisIndex,
       "fEthernetBkPlnNsrtState": fEthernetBkPlnNsrtState,
       "fEthernetBkPlnTimeStamp": fEthernetBkPlnTimeStamp,
       "fEthernetMgmtStatus": fEthernetMgmtStatus,
       "fEthernetProxyAgentID": fEthernetProxyAgentID,
       "fEthernetTemperatureStatus": fEthernetTemperatureStatus,
       "fEthernetCodeVersion": fEthernetCodeVersion,
       "fEthernetRawCommandData": fEthernetRawCommandData,
       "fEthernetPowerStatus": fEthernetPowerStatus,
       "fEthernetCageType": fEthernetCageType,
       "fFddi": fFddi,
       "fTwx": fTwx,
       "rmonAgent": rmonAgent,
       "rmonAgentDescription": rmonAgentDescription,
       "rmonAgentID": rmonAgentID,
       "rmonAgentOOBNumber": rmonAgentOOBNumber,
       "rmonAgentOOBTable": rmonAgentOOBTable,
       "rmonAgentOOBTableEntry": rmonAgentOOBTableEntry,
       "rmonAgentOOBTableIndex": rmonAgentOOBTableIndex,
       "rmonAgentOOBTableDescription": rmonAgentOOBTableDescription,
       "rmonAgentOOBTableData": rmonAgentOOBTableData,
       "rmonAgentOOBRawDataCommand": rmonAgentOOBRawDataCommand,
       "rmonAgentIBNumber": rmonAgentIBNumber,
       "rmonAgentIBTable": rmonAgentIBTable,
       "rmonAgentIBTableEntry": rmonAgentIBTableEntry,
       "rmonAgentIBTableIndex": rmonAgentIBTableIndex,
       "rmonAgentIBTableDescription": rmonAgentIBTableDescription,
       "rmonAgentIBNetworkType": rmonAgentIBNetworkType,
       "rmonAgentIBSampleInterval": rmonAgentIBSampleInterval,
       "rmonAgentIBMacFrames": rmonAgentIBMacFrames,
       "rmonAgentIBDataFrames": rmonAgentIBDataFrames,
       "rmonAgentIBMacBytes": rmonAgentIBMacBytes,
       "rmonAgentIBDataBytes": rmonAgentIBDataBytes,
       "rmonAgentIBUtilization": rmonAgentIBUtilization,
       "rmonAgentIBMACUtilization": rmonAgentIBMACUtilization,
       "rmonAgentIBNonMACUtilization": rmonAgentIBNonMACUtilization,
       "rmonAgentIBMACData0": rmonAgentIBMACData0,
       "rmonAgentIBMACData1": rmonAgentIBMACData1,
       "rmonAgentIBMACData2": rmonAgentIBMACData2,
       "rmonAgentIBMACData3": rmonAgentIBMACData3,
       "rmonAgentIBMACData4": rmonAgentIBMACData4,
       "rmonAgentIBMACData5": rmonAgentIBMACData5,
       "rmonAgentIBMACData6": rmonAgentIBMACData6,
       "rmonAgentIBMACData7": rmonAgentIBMACData7,
       "rmonAgentIBMACData8": rmonAgentIBMACData8,
       "rmonAgentIBMACData9": rmonAgentIBMACData9,
       "rmonAgentIBMACData10": rmonAgentIBMACData10,
       "rmonAgentIBMACData11": rmonAgentIBMACData11,
       "rmonAgentMonitorCommand": rmonAgentMonitorCommand,
       "rmonAgentMonitorResponse": rmonAgentMonitorResponse,
       "rmonAgentDownloadData": rmonAgentDownloadData,
       "rmonAgentNoMapOid": rmonAgentNoMapOid,
       "rmonAgentMACStatTable": rmonAgentMACStatTable,
       "rmonAgentMACStatTableEntry": rmonAgentMACStatTableEntry,
       "rmonAgentMACStatTableData": rmonAgentMACStatTableData,
       "pysmiFakeCol2": pysmiFakeCol2,
       "pysmiFakeCol1": pysmiFakeCol1,
       "rmonAgentIPAdressControl": rmonAgentIPAdressControl,
       "stackable": stackable,
       "stackableHubs": stackableHubs,
       "stackableHubNumber": stackableHubNumber,
       "stackableHubTable": stackableHubTable,
       "stackableHubTableEntry": stackableHubTableEntry,
       "stackableHubTableIndex": stackableHubTableIndex,
       "stackableHubModel": stackableHubModel,
       "stackableHub485Address": stackableHub485Address,
       "stackableHubRiFTolState": stackableHubRiFTolState,
       "stackableHubRiMask": stackableHubRiMask,
       "stackableHubRiPhDet": stackableHubRiPhDet,
       "stackableHubRiNsrtStatus": stackableHubRiNsrtStatus,
       "stackableHubRiBcnRemStatus": stackableHubRiBcnRemStatus,
       "stackableHubRiNeighborType": stackableHubRiNeighborType,
       "stackableHubRiNeighborAddr": stackableHubRiNeighborAddr,
       "stackableHubRiTimeStamp": stackableHubRiTimeStamp,
       "stackableHubRoFTolState": stackableHubRoFTolState,
       "stackableHubRoMask": stackableHubRoMask,
       "stackableHubRoPhDet": stackableHubRoPhDet,
       "stackableHubRoNsrtStatus": stackableHubRoNsrtStatus,
       "stackableHubRoBcnRemStatus": stackableHubRoBcnRemStatus,
       "stackableHubRoNeighborType": stackableHubRoNeighborType,
       "stackableHubRoNeighborAddr": stackableHubRoNeighborAddr,
       "stackableHubRoTimeStamp": stackableHubRoTimeStamp,
       "stackableHubDataRateState": stackableHubDataRateState,
       "stackableHubDataRateTimeStamp": stackableHubDataRateTimeStamp,
       "stackableHubMgmtStatus": stackableHubMgmtStatus,
       "stackableHubProxyAgentID": stackableHubProxyAgentID,
       "stackableHubAttachedAgentType": stackableHubAttachedAgentType,
       "stackableHubAttachedAgentState": stackableHubAttachedAgentState,
       "stackableHubTemperatureStatus": stackableHubTemperatureStatus,
       "stackableHubAutoRecovControl": stackableHubAutoRecovControl,
       "stackableHubAutoRecovRetries": stackableHubAutoRecovRetries,
       "stackableHubCodeVersion": stackableHubCodeVersion,
       "stackableHubAutoRecovState": stackableHubAutoRecovState,
       "stackableHubRawCommandData": stackableHubRawCommandData,
       "stackableHubAutoRecovMode": stackableHubAutoRecovMode,
       "stackableHubLobeNumber": stackableHubLobeNumber,
       "stackableHubLobeTable": stackableHubLobeTable,
       "stackableHubLobeEntry": stackableHubLobeEntry,
       "stackableHubIndex": stackableHubIndex,
       "stackableHubLobePort": stackableHubLobePort,
       "stackableHubLobePhDet": stackableHubLobePhDet,
       "stackableHubLobeMask": stackableHubLobeMask,
       "stackableHubLobeNsrtStatus": stackableHubLobeNsrtStatus,
       "stackableHubLobeMacAddr": stackableHubLobeMacAddr,
       "stackableHubLobeBcnRemStatus": stackableHubLobeBcnRemStatus,
       "stackableHubLobeBcnRemCause": stackableHubLobeBcnRemCause,
       "stackableHubLobeTimeStamp": stackableHubLobeTimeStamp,
       "superStackHubs": superStackHubs,
       "superStackHubNumber": superStackHubNumber,
       "superStackHubTable": superStackHubTable,
       "superStackHubTableEntry": superStackHubTableEntry,
       "superStackHubTableIndex": superStackHubTableIndex,
       "superStackHubModel": superStackHubModel,
       "superStackHub485Address": superStackHub485Address,
       "superStackHubStackPosition": superStackHubStackPosition,
       "superStackRiConfiguration": superStackRiConfiguration,
       "superStackHubRiFTolState": superStackHubRiFTolState,
       "superStackHubRiMask": superStackHubRiMask,
       "superStackHubRiPhDet": superStackHubRiPhDet,
       "superStackHubRiNsrtStatus": superStackHubRiNsrtStatus,
       "superStackHubRiBcnRemStatus": superStackHubRiBcnRemStatus,
       "superStackRoConfiguration": superStackRoConfiguration,
       "superStackHubRoFTolState": superStackHubRoFTolState,
       "superStackHubRoMask": superStackHubRoMask,
       "superStackHubRoPhDet": superStackHubRoPhDet,
       "superStackHubRoNsrtStatus": superStackHubRoNsrtStatus,
       "superStackHubRoBcnRemStatus": superStackHubRoBcnRemStatus,
       "superStackHubCascadeUpMask": superStackHubCascadeUpMask,
       "superStackHubCascadeUpPhDet": superStackHubCascadeUpPhDet,
       "superStackHubCascadeUpNsrtStatus": superStackHubCascadeUpNsrtStatus,
       "superStackHubCascadeUpBcnRemStatus": superStackHubCascadeUpBcnRemStatus,
       "superStackHubCascadeDownMask": superStackHubCascadeDownMask,
       "superStackHubCascadeDownPhDet": superStackHubCascadeDownPhDet,
       "superStackHubCascadeDownNsrtStatus": superStackHubCascadeDownNsrtStatus,
       "superStackHubCascadeDownBcnRemStatus": superStackHubCascadeDownBcnRemStatus,
       "superStackHubDataRateState": superStackHubDataRateState,
       "superStackHubDeviceTimeStamp": superStackHubDeviceTimeStamp,
       "superStackHubMgmtStatus": superStackHubMgmtStatus,
       "superStackHubProxyAgentID": superStackHubProxyAgentID,
       "superStackHubAttachedAgentType": superStackHubAttachedAgentType,
       "superStackHubAttachedAgentState": superStackHubAttachedAgentState,
       "superStackHubAttachedAgentControl": superStackHubAttachedAgentControl,
       "superStackHubTemperatureStatus": superStackHubTemperatureStatus,
       "superStackHubPowerStatus": superStackHubPowerStatus,
       "superStackHubAutoRecovControl": superStackHubAutoRecovControl,
       "superStackHubAutoRecovRetries": superStackHubAutoRecovRetries,
       "superStackHubCodeVersion": superStackHubCodeVersion,
       "superStackHubAutoRecovState": superStackHubAutoRecovState,
       "superStackHubRawCommandData": superStackHubRawCommandData,
       "superStackHubAutoRecovMode": superStackHubAutoRecovMode,
       "superStackHubRouterPortPhDet": superStackHubRouterPortPhDet,
       "superStackHubRouterPortMask": superStackHubRouterPortMask,
       "superStackHubRouterPortNsrtStatus": superStackHubRouterPortNsrtStatus,
       "superStackHubRouterPortMacAddr": superStackHubRouterPortMacAddr,
       "superStackHubRouterPortBcnRemStatus": superStackHubRouterPortBcnRemStatus,
       "superStackHubRouterPortBcnRemCause": superStackHubRouterPortBcnRemCause,
       "superStackHubLobeNumber": superStackHubLobeNumber,
       "superStackHubLobeTable": superStackHubLobeTable,
       "superStackHubLobeEntry": superStackHubLobeEntry,
       "superStackHubIndex": superStackHubIndex,
       "superStackHubLobePort": superStackHubLobePort,
       "superStackHubLobeConfig": superStackHubLobeConfig,
       "superStackHubLobePhDet": superStackHubLobePhDet,
       "superStackHubLobeMask": superStackHubLobeMask,
       "superStackHubLobeNsrtStatus": superStackHubLobeNsrtStatus,
       "superStackHubLobeMacAddr": superStackHubLobeMacAddr,
       "superStackHubLobeBcnRemStatus": superStackHubLobeBcnRemStatus,
       "superStackHubLobeBcnRemCause": superStackHubLobeBcnRemCause,
       "maintenance": maintenance,
       "managers": managers,
       "mgrNumber": mgrNumber,
       "mgrAutoAdd": mgrAutoAdd,
       "mgrAutoAge": mgrAutoAge,
       "mgrAgeInterval": mgrAgeInterval,
       "mgrTable": mgrTable,
       "mgrEntry": mgrEntry,
       "mgrIndex": mgrIndex,
       "mgrIpAddr": mgrIpAddr,
       "mgrCommunity": mgrCommunity,
       "mgrTimeStamp": mgrTimeStamp,
       "mgrStatus": mgrStatus,
       "mgrPhysAddr": mgrPhysAddr,
       "mgrInterfaceIndex": mgrInterfaceIndex,
       "versions": versions,
       "versionHardware": versionHardware,
       "versionEPROMFirmware": versionEPROMFirmware,
       "versionFLASHFirmware": versionFLASHFirmware,
       "configuration": configuration,
       "configEPROMSize": configEPROMSize,
       "configFLASHSize": configFLASHSize,
       "configFLASHCount": configFLASHCount,
       "configDRAMSize": configDRAMSize,
       "configDRAMCount": configDRAMCount,
       "configRS232Number": configRS232Number,
       "configRS232PortTable": configRS232PortTable,
       "configRS232PortEntry": configRS232PortEntry,
       "configRS232PortIndex": configRS232PortIndex,
       "configRS232PortName": configRS232PortName,
       "configRS232BaudRate": configRS232BaudRate,
       "configRS232ModemStatus": configRS232ModemStatus,
       "configRS232ConnectionStatus": configRS232ConnectionStatus,
       "configRS232ModemConfigString": configRS232ModemConfigString,
       "configRS232OutputData": configRS232OutputData,
       "configRS232InputData": configRS232InputData,
       "configRS232HardwareFlowControl": configRS232HardwareFlowControl,
       "configMonitorMode": configMonitorMode,
       "configMonitorInput": configMonitorInput,
       "configMonitorDiags": configMonitorDiags,
       "configParseControl": configParseControl,
       "configBootSource": configBootSource,
       "security": security,
       "securityControl": securityControl,
       "securityMacAddressTable": securityMacAddressTable,
       "securityMacAddressTableEntry": securityMacAddressTableEntry,
       "securityMacAddress": securityMacAddress,
       "securityStatus": securityStatus,
       "securityLockoutCount": securityLockoutCount,
       "pysmiFakeCol3": pysmiFakeCol3,
       "recovery": recovery,
       "recoveryControl": recoveryControl,
       "recovery828Support": recovery828Support,
       "recoveryRetryLimit": recoveryRetryLimit,
       "recoveryRetryTimePeriod": recoveryRetryTimePeriod,
       "rmonextns": rmonextns,
       "stationstatistics": stationstatistics,
       "stationhistory": stationhistory,
       "trHistoryTable": trHistoryTable,
       "trHistoryEntry": trHistoryEntry,
       "trHistoryIndex": trHistoryIndex,
       "trHistorySampleIndex": trHistorySampleIndex,
       "trHistoryIntervalStart": trHistoryIntervalStart,
       "trHistoryInPkts": trHistoryInPkts,
       "trHistoryOutPkts": trHistoryOutPkts,
       "trHistoryInOctets": trHistoryInOctets,
       "trHistoryOutOctets": trHistoryOutOctets,
       "trHistoryOutBroadcastPkts": trHistoryOutBroadcastPkts,
       "trHistoryOutMulticastPkts": trHistoryOutMulticastPkts,
       "trHistoryClaimTokenPkts": trHistoryClaimTokenPkts,
       "trHistoryInLineErrors": trHistoryInLineErrors,
       "trHistoryOutLineErrors": trHistoryOutLineErrors,
       "trHistoryInternalErrors": trHistoryInternalErrors,
       "trHistoryInBurstErrors": trHistoryInBurstErrors,
       "trHistoryOutBurstErrors": trHistoryOutBurstErrors,
       "trHistoryACErrors": trHistoryACErrors,
       "trHistoryAbortErrors": trHistoryAbortErrors,
       "trHistoryLostFrameErrors": trHistoryLostFrameErrors,
       "trHistoryCongestionErrors": trHistoryCongestionErrors,
       "trHistoryFrameCopiedErrors": trHistoryFrameCopiedErrors,
       "trHistoryFrequencyErrors": trHistoryFrequencyErrors,
       "trHistoryTokenErrors": trHistoryTokenErrors,
       "trHistoryInBeaconErrors": trHistoryInBeaconErrors,
       "trHistoryOutBeaconErrors": trHistoryOutBeaconErrors,
       "trHistoryInsertions": trHistoryInsertions,
       "trHistorySoftErrors": trHistorySoftErrors,
       "trHistoryOpaqueTable": trHistoryOpaqueTable,
       "trHistoryOpaqueEntry": trHistoryOpaqueEntry,
       "trHistoryTableData": trHistoryTableData,
       "pysmiFakeCol5": pysmiFakeCol5,
       "pysmiFakeCol4": pysmiFakeCol4,
       "protocolstatistics": protocolstatistics,
       "protocolData": protocolData,
       "protocolStatsTable": protocolStatsTable,
       "protocolStatsEntry": protocolStatsEntry,
       "protocolIfIndex": protocolIfIndex,
       "protocolID": protocolID,
       "protocolPkts": protocolPkts,
       "protocolOctets": protocolOctets}
)
