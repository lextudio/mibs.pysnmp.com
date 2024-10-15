# SNMP MIB module (ZHONE-MAU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/ZHONE-MAU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:20:37 2024
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

(InterfaceIndexOrZero,
 ifAdminStatus,
 ifIndex,
 ifName,
 ifOperStatus) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifAdminStatus",
    "ifIndex",
    "ifName",
    "ifOperStatus")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention",
    "TruthValue")

(zhoneEnet,
 zhoneModules) = mibBuilder.importSymbols(
    "Zhone",
    "zhoneEnet",
    "zhoneModules")


# MODULE-IDENTITY

phyEnetMauMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 6, 8)
)
phyEnetMauMib.setRevisions(
        ("2013-10-13 17:08",
         "2012-05-25 14:55",
         "2009-02-03 01:39",
         "2009-01-19 21:44",
         "2008-08-14 07:17",
         "2008-03-10 12:03",
         "2007-11-01 14:37",
         "2007-06-24 23:11",
         "2007-05-22 16:05",
         "2005-10-13 16:55",
         "2000-09-12 18:01")
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZhoneIfMauTable_Object = MibTable
zhoneIfMauTable = _ZhoneIfMauTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1)
)
if mibBuilder.loadTexts:
    zhoneIfMauTable.setStatus("current")
_ZhoneIfMauEntry_Object = MibTableRow
zhoneIfMauEntry = _ZhoneIfMauEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1)
)
zhoneIfMauEntry.setIndexNames(
    (0, "ZHONE-MAU-MIB", "zhoneMauIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneIfMauEntry.setStatus("current")


class _ZhoneMauIfIndex_Type(Integer32):
    """Custom type zhoneMauIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZhoneMauIfIndex_Type.__name__ = "Integer32"
_ZhoneMauIfIndex_Object = MibTableColumn
zhoneMauIfIndex = _ZhoneMauIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 1),
    _ZhoneMauIfIndex_Type()
)
zhoneMauIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauIfIndex.setStatus("current")


class _ZhoneMauType_Type(Integer32):
    """Custom type zhoneMauType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              10,
              11,
              15,
              16,
              22,
              23,
              25,
              26,
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
              40)
        )
    )
    namedValues = NamedValues(
        *(("mau1000BaseLXFD", 23),
          ("mau1000BaseLXHD", 22),
          ("mau1000BaseSXFD", 26),
          ("mau1000BaseSXHD", 25),
          ("mau1000BaseTFD", 30),
          ("mau1000BaseTHD", 29),
          ("mau100BaseTXFD", 16),
          ("mau100BaseTXHD", 15),
          ("mau10BaseT", 5),
          ("mau10BaseTFD", 11),
          ("mau10BaseTHD", 10),
          ("mau10gBaseER", 39),
          ("mau10gBaseEW", 40),
          ("mau10gBaseLR", 37),
          ("mau10gBaseLW", 38),
          ("mau10gBaseLX4", 34),
          ("mau10gBaseR", 32),
          ("mau10gBaseSR", 35),
          ("mau10gBaseSW", 36),
          ("mau10gBaseW", 33),
          ("mau10gBaseX", 31),
          ("mauOther", 1))
    )


_ZhoneMauType_Type.__name__ = "Integer32"
_ZhoneMauType_Object = MibTableColumn
zhoneMauType = _ZhoneMauType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 2),
    _ZhoneMauType_Type()
)
zhoneMauType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauType.setStatus("current")


class _ZhoneMauOperStatus_Type(Integer32):
    """Custom type zhoneMauOperStatus based on Integer32"""
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
        *(("operational", 3),
          ("other", 1),
          ("reset", 6),
          ("shutdown", 5),
          ("standby", 4),
          ("unknown", 2))
    )


_ZhoneMauOperStatus_Type.__name__ = "Integer32"
_ZhoneMauOperStatus_Object = MibTableColumn
zhoneMauOperStatus = _ZhoneMauOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 3),
    _ZhoneMauOperStatus_Type()
)
zhoneMauOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauOperStatus.setStatus("current")


class _ZhoneMauMediaAvailable_Type(Integer32):
    """Custom type zhoneMauMediaAvailable based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("autoNegError", 11),
          ("available", 3),
          ("invalidSignal", 6),
          ("notAvailable", 4),
          ("offline", 10),
          ("other", 1),
          ("remoteFault", 5),
          ("remoteJabber", 7),
          ("remoteLinkLoss", 8),
          ("remoteTest", 9),
          ("unknown", 2))
    )


_ZhoneMauMediaAvailable_Type.__name__ = "Integer32"
_ZhoneMauMediaAvailable_Object = MibTableColumn
zhoneMauMediaAvailable = _ZhoneMauMediaAvailable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 4),
    _ZhoneMauMediaAvailable_Type()
)
zhoneMauMediaAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauMediaAvailable.setStatus("current")
_ZhoneMauMediaAvailStateExits_Type = Counter32
_ZhoneMauMediaAvailStateExits_Object = MibTableColumn
zhoneMauMediaAvailStateExits = _ZhoneMauMediaAvailStateExits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 5),
    _ZhoneMauMediaAvailStateExits_Type()
)
zhoneMauMediaAvailStateExits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauMediaAvailStateExits.setStatus("current")


class _ZhoneMauJabberState_Type(Integer32):
    """Custom type zhoneMauJabberState based on Integer32"""
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
        *(("jabbering", 4),
          ("noJabber", 3),
          ("other", 1),
          ("unknown", 2))
    )


_ZhoneMauJabberState_Type.__name__ = "Integer32"
_ZhoneMauJabberState_Object = MibTableColumn
zhoneMauJabberState = _ZhoneMauJabberState_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 6),
    _ZhoneMauJabberState_Type()
)
zhoneMauJabberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauJabberState.setStatus("current")
_ZhoneMauJabberingStateEnters_Type = Counter32
_ZhoneMauJabberingStateEnters_Object = MibTableColumn
zhoneMauJabberingStateEnters = _ZhoneMauJabberingStateEnters_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 7),
    _ZhoneMauJabberingStateEnters_Type()
)
zhoneMauJabberingStateEnters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauJabberingStateEnters.setStatus("current")
_ZhoneMauFalseCarriers_Type = Counter32
_ZhoneMauFalseCarriers_Object = MibTableColumn
zhoneMauFalseCarriers = _ZhoneMauFalseCarriers_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 8),
    _ZhoneMauFalseCarriers_Type()
)
zhoneMauFalseCarriers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauFalseCarriers.setStatus("current")


class _ZhoneMauDefaultType_Type(Integer32):
    """Custom type zhoneMauDefaultType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              10,
              11,
              15,
              16,
              22,
              23,
              25,
              26,
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
              40)
        )
    )
    namedValues = NamedValues(
        *(("mau1000BaseLXFD", 23),
          ("mau1000BaseLXHD", 22),
          ("mau1000BaseSXFD", 26),
          ("mau1000BaseSXHD", 25),
          ("mau1000BaseTFD", 30),
          ("mau1000BaseTHD", 29),
          ("mau100BaseTXFD", 16),
          ("mau100BaseTXHD", 15),
          ("mau10BaseT", 5),
          ("mau10BaseTFD", 11),
          ("mau10BaseTHD", 10),
          ("mau10gBaseER", 39),
          ("mau10gBaseEW", 40),
          ("mau10gBaseLR", 37),
          ("mau10gBaseLW", 38),
          ("mau10gBaseLX4", 34),
          ("mau10gBaseR", 32),
          ("mau10gBaseSR", 35),
          ("mau10gBaseSW", 36),
          ("mau10gBaseW", 33),
          ("mau10gBaseX", 31),
          ("mauOther", 1))
    )


_ZhoneMauDefaultType_Type.__name__ = "Integer32"
_ZhoneMauDefaultType_Object = MibTableColumn
zhoneMauDefaultType = _ZhoneMauDefaultType_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 9),
    _ZhoneMauDefaultType_Type()
)
zhoneMauDefaultType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauDefaultType.setStatus("current")
_ZhoneMauAutoNegSupported_Type = TruthValue
_ZhoneMauAutoNegSupported_Object = MibTableColumn
zhoneMauAutoNegSupported = _ZhoneMauAutoNegSupported_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 10),
    _ZhoneMauAutoNegSupported_Type()
)
zhoneMauAutoNegSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauAutoNegSupported.setStatus("current")


class _ZhoneMauTypeListBits_Type(Bits):
    """Custom type zhoneMauTypeListBits based on Bits"""
    namedValues = NamedValues(
        *(("b1000baseCXFD", 28),
          ("b1000baseCXHD", 27),
          ("b1000baseLXFD", 24),
          ("b1000baseLXHD", 23),
          ("b1000baseSXFD", 26),
          ("b1000baseSXHD", 25),
          ("b1000baseTFD", 30),
          ("b1000baseTHD", 29),
          ("b1000baseXFD", 22),
          ("b1000baseXHD", 21),
          ("b100baseFXFD", 18),
          ("b100baseFXHD", 17),
          ("b100baseT2FD", 20),
          ("b100baseT2HD", 19),
          ("b100baseT4", 14),
          ("b100baseTXFD", 16),
          ("b100baseTXHD", 15),
          ("b10base2", 4),
          ("b10base5", 2),
          ("b10baseFB", 7),
          ("b10baseFL", 8),
          ("b10baseFLFD", 13),
          ("b10baseFLHD", 12),
          ("b10baseFP", 6),
          ("b10baseT", 5),
          ("b10baseTFD", 11),
          ("b10baseTHD", 10),
          ("b10broad36", 9),
          ("b10gbaseER", 39),
          ("b10gbaseEW", 40),
          ("b10gbaseLR", 37),
          ("b10gbaseLW", 38),
          ("b10gbaseLX4", 34),
          ("b10gbaseR", 32),
          ("b10gbaseSR", 35),
          ("b10gbaseSW", 36),
          ("b10gbaseW", 33),
          ("b10gbaseX", 31),
          ("bAUI", 1),
          ("bFoirl", 3),
          ("bOther", 0))
    )

_ZhoneMauTypeListBits_Type.__name__ = "Bits"
_ZhoneMauTypeListBits_Object = MibTableColumn
zhoneMauTypeListBits = _ZhoneMauTypeListBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 11),
    _ZhoneMauTypeListBits_Type()
)
zhoneMauTypeListBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauTypeListBits.setStatus("current")


class _ZhoneMauClkSrc_Type(Integer32):
    """Custom type zhoneMauClkSrc based on Integer32"""
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
        *(("automatic", 2),
          ("master", 3),
          ("slave", 4),
          ("unused", 1))
    )


_ZhoneMauClkSrc_Type.__name__ = "Integer32"
_ZhoneMauClkSrc_Object = MibTableColumn
zhoneMauClkSrc = _ZhoneMauClkSrc_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 12),
    _ZhoneMauClkSrc_Type()
)
zhoneMauClkSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauClkSrc.setStatus("current")


class _ZhoneMauPauseFlowControl_Type(Integer32):
    """Custom type zhoneMauPauseFlowControl based on Integer32"""
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
        *(("asymmetricRx", 3),
          ("asymmetricTx", 2),
          ("disabled", 1),
          ("passthrough", 5),
          ("symmetric", 4))
    )


_ZhoneMauPauseFlowControl_Type.__name__ = "Integer32"
_ZhoneMauPauseFlowControl_Object = MibTableColumn
zhoneMauPauseFlowControl = _ZhoneMauPauseFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 13),
    _ZhoneMauPauseFlowControl_Type()
)
zhoneMauPauseFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauPauseFlowControl.setStatus("current")


class _ZhoneMauAggregationMode_Type(Integer32):
    """Custom type zhoneMauAggregationMode based on Integer32"""
    defaultValue = 1

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
        *(("active", 4),
          ("off", 2),
          ("on", 1),
          ("passive", 3))
    )


_ZhoneMauAggregationMode_Type.__name__ = "Integer32"
_ZhoneMauAggregationMode_Object = MibTableColumn
zhoneMauAggregationMode = _ZhoneMauAggregationMode_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 14),
    _ZhoneMauAggregationMode_Type()
)
zhoneMauAggregationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauAggregationMode.setStatus("current")


class _ZhoneMauLinkStateMirror_Type(InterfaceIndexOrZero):
    """Custom type zhoneMauLinkStateMirror based on InterfaceIndexOrZero"""
    defaultValue = 0


_ZhoneMauLinkStateMirror_Object = MibTableColumn
zhoneMauLinkStateMirror = _ZhoneMauLinkStateMirror_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 15),
    _ZhoneMauLinkStateMirror_Type()
)
zhoneMauLinkStateMirror.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauLinkStateMirror.setStatus("current")


class _ZhoneMauSetPauseTime_Type(Integer32):
    """Custom type zhoneMauSetPauseTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZhoneMauSetPauseTime_Type.__name__ = "Integer32"
_ZhoneMauSetPauseTime_Object = MibTableColumn
zhoneMauSetPauseTime = _ZhoneMauSetPauseTime_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 16),
    _ZhoneMauSetPauseTime_Type()
)
zhoneMauSetPauseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauSetPauseTime.setStatus("current")


class _ZhoneMauMaxFrameSize_Type(Integer32):
    """Custom type zhoneMauMaxFrameSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15360),
    )


_ZhoneMauMaxFrameSize_Type.__name__ = "Integer32"
_ZhoneMauMaxFrameSize_Object = MibTableColumn
zhoneMauMaxFrameSize = _ZhoneMauMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 17),
    _ZhoneMauMaxFrameSize_Type()
)
zhoneMauMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauMaxFrameSize.setStatus("current")


class _ZhoneMauIngressRate_Type(Integer32):
    """Custom type zhoneMauIngressRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240000),
    )


_ZhoneMauIngressRate_Type.__name__ = "Integer32"
_ZhoneMauIngressRate_Object = MibTableColumn
zhoneMauIngressRate = _ZhoneMauIngressRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 18),
    _ZhoneMauIngressRate_Type()
)
zhoneMauIngressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauIngressRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneMauIngressRate.setUnits("Kbps")


class _ZhoneMauIngressBurstSize_Type(Integer32):
    """Custom type zhoneMauIngressBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512000),
    )


_ZhoneMauIngressBurstSize_Type.__name__ = "Integer32"
_ZhoneMauIngressBurstSize_Object = MibTableColumn
zhoneMauIngressBurstSize = _ZhoneMauIngressBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 19),
    _ZhoneMauIngressBurstSize_Type()
)
zhoneMauIngressBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauIngressBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    zhoneMauIngressBurstSize.setUnits("Kbits")


class _ZhoneMauEgressRate_Type(Integer32):
    """Custom type zhoneMauEgressRate based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10240000),
    )


_ZhoneMauEgressRate_Type.__name__ = "Integer32"
_ZhoneMauEgressRate_Object = MibTableColumn
zhoneMauEgressRate = _ZhoneMauEgressRate_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 20),
    _ZhoneMauEgressRate_Type()
)
zhoneMauEgressRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauEgressRate.setStatus("current")
if mibBuilder.loadTexts:
    zhoneMauEgressRate.setUnits("Kbps")


class _ZhoneMauEgressBurstSize_Type(Integer32):
    """Custom type zhoneMauEgressBurstSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 512000),
    )


_ZhoneMauEgressBurstSize_Type.__name__ = "Integer32"
_ZhoneMauEgressBurstSize_Object = MibTableColumn
zhoneMauEgressBurstSize = _ZhoneMauEgressBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 1, 1, 21),
    _ZhoneMauEgressBurstSize_Type()
)
zhoneMauEgressBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauEgressBurstSize.setStatus("current")
if mibBuilder.loadTexts:
    zhoneMauEgressBurstSize.setUnits("Kbits")
_ZhoneMauAutoNegTable_Object = MibTable
zhoneMauAutoNegTable = _ZhoneMauAutoNegTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2)
)
if mibBuilder.loadTexts:
    zhoneMauAutoNegTable.setStatus("current")
_ZhoneMauAutoNegEntry_Object = MibTableRow
zhoneMauAutoNegEntry = _ZhoneMauAutoNegEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2, 1)
)
zhoneMauAutoNegEntry.setIndexNames(
    (0, "ZHONE-MAU-MIB", "zhoneMauIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneMauAutoNegEntry.setStatus("current")


class _ZhoneMauAutoNegAdminStatus_Type(Integer32):
    """Custom type zhoneMauAutoNegAdminStatus based on Integer32"""
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


_ZhoneMauAutoNegAdminStatus_Type.__name__ = "Integer32"
_ZhoneMauAutoNegAdminStatus_Object = MibTableColumn
zhoneMauAutoNegAdminStatus = _ZhoneMauAutoNegAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2, 1, 1),
    _ZhoneMauAutoNegAdminStatus_Type()
)
zhoneMauAutoNegAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauAutoNegAdminStatus.setStatus("current")


class _ZhoneMauAutoNegRemoteSignaling_Type(Integer32):
    """Custom type zhoneMauAutoNegRemoteSignaling based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("detected", 1),
          ("notdetected", 2))
    )


_ZhoneMauAutoNegRemoteSignaling_Type.__name__ = "Integer32"
_ZhoneMauAutoNegRemoteSignaling_Object = MibTableColumn
zhoneMauAutoNegRemoteSignaling = _ZhoneMauAutoNegRemoteSignaling_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2, 1, 2),
    _ZhoneMauAutoNegRemoteSignaling_Type()
)
zhoneMauAutoNegRemoteSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauAutoNegRemoteSignaling.setStatus("current")


class _ZhoneMauAutoNegConfig_Type(Integer32):
    """Custom type zhoneMauAutoNegConfig based on Integer32"""
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
        *(("complete", 3),
          ("configuring", 2),
          ("disabled", 4),
          ("other", 1),
          ("parallelDetectFail", 5))
    )


_ZhoneMauAutoNegConfig_Type.__name__ = "Integer32"
_ZhoneMauAutoNegConfig_Object = MibTableColumn
zhoneMauAutoNegConfig = _ZhoneMauAutoNegConfig_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2, 1, 3),
    _ZhoneMauAutoNegConfig_Type()
)
zhoneMauAutoNegConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauAutoNegConfig.setStatus("current")


class _ZhoneMauAutoNegRestart_Type(Integer32):
    """Custom type zhoneMauAutoNegRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("norestart", 2),
          ("restart", 1))
    )


_ZhoneMauAutoNegRestart_Type.__name__ = "Integer32"
_ZhoneMauAutoNegRestart_Object = MibTableColumn
zhoneMauAutoNegRestart = _ZhoneMauAutoNegRestart_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2, 1, 4),
    _ZhoneMauAutoNegRestart_Type()
)
zhoneMauAutoNegRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauAutoNegRestart.setStatus("current")


class _ZhoneMauAutoNegCapabilityBits_Type(Bits):
    """Custom type zhoneMauAutoNegCapabilityBits based on Bits"""
    namedValues = NamedValues(
        *(("b1000baseT", 14),
          ("b1000baseTFD", 15),
          ("b1000baseX", 12),
          ("b1000baseXFD", 13),
          ("b100baseT2", 6),
          ("b100baseT2FD", 7),
          ("b100baseT4", 3),
          ("b100baseTX", 4),
          ("b100baseTXFD", 5),
          ("b10baseT", 1),
          ("b10baseTFD", 2),
          ("b10gbaseER", 24),
          ("b10gbaseEW", 25),
          ("b10gbaseLR", 22),
          ("b10gbaseLW", 23),
          ("b10gbaseLX4", 19),
          ("b10gbaseR", 17),
          ("b10gbaseSR", 20),
          ("b10gbaseSW", 21),
          ("b10gbaseW", 18),
          ("b10gbaseX", 16),
          ("bOther", 0),
          ("bfdxAPause", 9),
          ("bfdxBPause", 11),
          ("bfdxPause", 8),
          ("bfdxSPause", 10))
    )

_ZhoneMauAutoNegCapabilityBits_Type.__name__ = "Bits"
_ZhoneMauAutoNegCapabilityBits_Object = MibTableColumn
zhoneMauAutoNegCapabilityBits = _ZhoneMauAutoNegCapabilityBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2, 1, 5),
    _ZhoneMauAutoNegCapabilityBits_Type()
)
zhoneMauAutoNegCapabilityBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauAutoNegCapabilityBits.setStatus("current")


class _ZhoneMauAutoNegCapAdvertBits_Type(Bits):
    """Custom type zhoneMauAutoNegCapAdvertBits based on Bits"""
    namedValues = NamedValues(
        *(("b1000baseT", 14),
          ("b1000baseTFD", 15),
          ("b1000baseX", 12),
          ("b1000baseXFD", 13),
          ("b100baseT2", 6),
          ("b100baseT2FD", 7),
          ("b100baseT4", 3),
          ("b100baseTX", 4),
          ("b100baseTXFD", 5),
          ("b10baseT", 1),
          ("b10baseTFD", 2),
          ("b10gbaseER", 24),
          ("b10gbaseEW", 25),
          ("b10gbaseLR", 22),
          ("b10gbaseLW", 23),
          ("b10gbaseLX4", 19),
          ("b10gbaseR", 17),
          ("b10gbaseSR", 20),
          ("b10gbaseSW", 21),
          ("b10gbaseW", 18),
          ("b10gbaseX", 16),
          ("bFdxAPause", 9),
          ("bFdxBPause", 11),
          ("bFdxPause", 8),
          ("bFdxSPause", 10),
          ("bOther", 0))
    )

_ZhoneMauAutoNegCapAdvertBits_Type.__name__ = "Bits"
_ZhoneMauAutoNegCapAdvertBits_Object = MibTableColumn
zhoneMauAutoNegCapAdvertBits = _ZhoneMauAutoNegCapAdvertBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2, 1, 6),
    _ZhoneMauAutoNegCapAdvertBits_Type()
)
zhoneMauAutoNegCapAdvertBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauAutoNegCapAdvertBits.setStatus("current")


class _ZhoneMauAutoNegCapRecvBits_Type(Bits):
    """Custom type zhoneMauAutoNegCapRecvBits based on Bits"""
    namedValues = NamedValues(
        *(("b1000baseT", 14),
          ("b1000baseTFD", 15),
          ("b1000baseX", 12),
          ("b1000baseXFD", 13),
          ("b100baseT2", 6),
          ("b100baseT2FD", 7),
          ("b100baseT4", 3),
          ("b100baseTX", 4),
          ("b100baseTXFD", 5),
          ("b10baseT", 1),
          ("b10baseTFD", 2),
          ("b10gbaseER", 24),
          ("b10gbaseEW", 25),
          ("b10gbaseLR", 22),
          ("b10gbaseLW", 23),
          ("b10gbaseLX4", 19),
          ("b10gbaseR", 17),
          ("b10gbaseSR", 20),
          ("b10gbaseSW", 21),
          ("b10gbaseW", 18),
          ("b10gbaseX", 16),
          ("bFdxAPause", 9),
          ("bFdxBPause", 11),
          ("bFdxPause", 8),
          ("bFdxSPause", 10),
          ("bOther", 0))
    )

_ZhoneMauAutoNegCapRecvBits_Type.__name__ = "Bits"
_ZhoneMauAutoNegCapRecvBits_Object = MibTableColumn
zhoneMauAutoNegCapRecvBits = _ZhoneMauAutoNegCapRecvBits_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2, 1, 7),
    _ZhoneMauAutoNegCapRecvBits_Type()
)
zhoneMauAutoNegCapRecvBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauAutoNegCapRecvBits.setStatus("current")


class _ZhoneMauAutoNegRemoteFaultAdvert_Type(Integer32):
    """Custom type zhoneMauAutoNegRemoteFaultAdvert based on Integer32"""
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
        *(("autoNegError", 4),
          ("linkFailure", 3),
          ("noError", 1),
          ("offline", 2))
    )


_ZhoneMauAutoNegRemoteFaultAdvert_Type.__name__ = "Integer32"
_ZhoneMauAutoNegRemoteFaultAdvert_Object = MibTableColumn
zhoneMauAutoNegRemoteFaultAdvert = _ZhoneMauAutoNegRemoteFaultAdvert_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2, 1, 8),
    _ZhoneMauAutoNegRemoteFaultAdvert_Type()
)
zhoneMauAutoNegRemoteFaultAdvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zhoneMauAutoNegRemoteFaultAdvert.setStatus("current")


class _ZhoneMauAutoNegRemoteFaultRecv_Type(Integer32):
    """Custom type zhoneMauAutoNegRemoteFaultRecv based on Integer32"""
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
        *(("autoNegError", 4),
          ("linkFailure", 3),
          ("noError", 1),
          ("offline", 2))
    )


_ZhoneMauAutoNegRemoteFaultRecv_Type.__name__ = "Integer32"
_ZhoneMauAutoNegRemoteFaultRecv_Object = MibTableColumn
zhoneMauAutoNegRemoteFaultRecv = _ZhoneMauAutoNegRemoteFaultRecv_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 2, 1, 9),
    _ZhoneMauAutoNegRemoteFaultRecv_Type()
)
zhoneMauAutoNegRemoteFaultRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneMauAutoNegRemoteFaultRecv.setStatus("current")
_ZhoneEnetTraps_ObjectIdentity = ObjectIdentity
zhoneEnetTraps = _ZhoneEnetTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 3)
)
if mibBuilder.loadTexts:
    zhoneEnetTraps.setStatus("current")
_EnetV2Traps_ObjectIdentity = ObjectIdentity
enetV2Traps = _EnetV2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 3, 0)
)
if mibBuilder.loadTexts:
    enetV2Traps.setStatus("current")
_ZhoneLinkAggTable_Object = MibTable
zhoneLinkAggTable = _ZhoneLinkAggTable_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 4)
)
if mibBuilder.loadTexts:
    zhoneLinkAggTable.setStatus("current")
_ZhoneLinkAggEntry_Object = MibTableRow
zhoneLinkAggEntry = _ZhoneLinkAggEntry_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 4, 1)
)
zhoneLinkAggEntry.setIndexNames(
    (0, "ZHONE-MAU-MIB", "zhoneLinkAggIfIndex"),
)
if mibBuilder.loadTexts:
    zhoneLinkAggEntry.setStatus("current")


class _ZhoneLinkAggIfIndex_Type(Integer32):
    """Custom type zhoneLinkAggIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ZhoneLinkAggIfIndex_Type.__name__ = "Integer32"
_ZhoneLinkAggIfIndex_Object = MibTableColumn
zhoneLinkAggIfIndex = _ZhoneLinkAggIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 4, 1, 1),
    _ZhoneLinkAggIfIndex_Type()
)
zhoneLinkAggIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneLinkAggIfIndex.setStatus("current")


class _ZhoneLinkAggPartnerSystem_Type(OctetString):
    """Custom type zhoneLinkAggPartnerSystem based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_ZhoneLinkAggPartnerSystem_Type.__name__ = "OctetString"
_ZhoneLinkAggPartnerSystem_Object = MibTableColumn
zhoneLinkAggPartnerSystem = _ZhoneLinkAggPartnerSystem_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 4, 1, 2),
    _ZhoneLinkAggPartnerSystem_Type()
)
zhoneLinkAggPartnerSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneLinkAggPartnerSystem.setStatus("current")
_ZhoneLinkAggPartnerSystemPriority_Type = Integer32
_ZhoneLinkAggPartnerSystemPriority_Object = MibTableColumn
zhoneLinkAggPartnerSystemPriority = _ZhoneLinkAggPartnerSystemPriority_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 4, 1, 3),
    _ZhoneLinkAggPartnerSystemPriority_Type()
)
zhoneLinkAggPartnerSystemPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneLinkAggPartnerSystemPriority.setStatus("current")
_ZhoneLinkAggPartnerGroupId_Type = Integer32
_ZhoneLinkAggPartnerGroupId_Object = MibTableColumn
zhoneLinkAggPartnerGroupId = _ZhoneLinkAggPartnerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 4, 1, 4),
    _ZhoneLinkAggPartnerGroupId_Type()
)
zhoneLinkAggPartnerGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zhoneLinkAggPartnerGroupId.setStatus("current")

# Managed Objects groups


# Notification objects

rprEastSpanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 3, 0, 1)
)
rprEastSpanTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    rprEastSpanTrap.setStatus(
        "current"
    )

rprWestSpanTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 3, 0, 2)
)
rprWestSpanTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("IF-MIB", "ifAdminStatus"),
        ("IF-MIB", "ifOperStatus"),
        ("IF-MIB", "ifName"))
)
if mibBuilder.loadTexts:
    rprWestSpanTrap.setStatus(
        "current"
    )

linkAggLink1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 3, 0, 3)
)
if mibBuilder.loadTexts:
    linkAggLink1Trap.setStatus(
        "current"
    )

linkAggLink2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 3, 0, 4)
)
if mibBuilder.loadTexts:
    linkAggLink2Trap.setStatus(
        "current"
    )


# Notifications groups

rprSpanGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 3, 2)
)
rprSpanGroup.setObjects(
      *(("ZHONE-MAU-MIB", "rprEastSpanTrap"),
        ("ZHONE-MAU-MIB", "rprWestSpanTrap"))
)
if mibBuilder.loadTexts:
    rprSpanGroup.setStatus(
        "current"
    )

linkAggLinkGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5504, 5, 1, 3, 3)
)
linkAggLinkGroup.setObjects(
      *(("ZHONE-MAU-MIB", "linkAggLink1Trap"),
        ("ZHONE-MAU-MIB", "linkAggLink2Trap"))
)
if mibBuilder.loadTexts:
    linkAggLinkGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZHONE-MAU-MIB",
    **{"zhoneIfMauTable": zhoneIfMauTable,
       "zhoneIfMauEntry": zhoneIfMauEntry,
       "zhoneMauIfIndex": zhoneMauIfIndex,
       "zhoneMauType": zhoneMauType,
       "zhoneMauOperStatus": zhoneMauOperStatus,
       "zhoneMauMediaAvailable": zhoneMauMediaAvailable,
       "zhoneMauMediaAvailStateExits": zhoneMauMediaAvailStateExits,
       "zhoneMauJabberState": zhoneMauJabberState,
       "zhoneMauJabberingStateEnters": zhoneMauJabberingStateEnters,
       "zhoneMauFalseCarriers": zhoneMauFalseCarriers,
       "zhoneMauDefaultType": zhoneMauDefaultType,
       "zhoneMauAutoNegSupported": zhoneMauAutoNegSupported,
       "zhoneMauTypeListBits": zhoneMauTypeListBits,
       "zhoneMauClkSrc": zhoneMauClkSrc,
       "zhoneMauPauseFlowControl": zhoneMauPauseFlowControl,
       "zhoneMauAggregationMode": zhoneMauAggregationMode,
       "zhoneMauLinkStateMirror": zhoneMauLinkStateMirror,
       "zhoneMauSetPauseTime": zhoneMauSetPauseTime,
       "zhoneMauMaxFrameSize": zhoneMauMaxFrameSize,
       "zhoneMauIngressRate": zhoneMauIngressRate,
       "zhoneMauIngressBurstSize": zhoneMauIngressBurstSize,
       "zhoneMauEgressRate": zhoneMauEgressRate,
       "zhoneMauEgressBurstSize": zhoneMauEgressBurstSize,
       "zhoneMauAutoNegTable": zhoneMauAutoNegTable,
       "zhoneMauAutoNegEntry": zhoneMauAutoNegEntry,
       "zhoneMauAutoNegAdminStatus": zhoneMauAutoNegAdminStatus,
       "zhoneMauAutoNegRemoteSignaling": zhoneMauAutoNegRemoteSignaling,
       "zhoneMauAutoNegConfig": zhoneMauAutoNegConfig,
       "zhoneMauAutoNegRestart": zhoneMauAutoNegRestart,
       "zhoneMauAutoNegCapabilityBits": zhoneMauAutoNegCapabilityBits,
       "zhoneMauAutoNegCapAdvertBits": zhoneMauAutoNegCapAdvertBits,
       "zhoneMauAutoNegCapRecvBits": zhoneMauAutoNegCapRecvBits,
       "zhoneMauAutoNegRemoteFaultAdvert": zhoneMauAutoNegRemoteFaultAdvert,
       "zhoneMauAutoNegRemoteFaultRecv": zhoneMauAutoNegRemoteFaultRecv,
       "zhoneEnetTraps": zhoneEnetTraps,
       "enetV2Traps": enetV2Traps,
       "rprEastSpanTrap": rprEastSpanTrap,
       "rprWestSpanTrap": rprWestSpanTrap,
       "linkAggLink1Trap": linkAggLink1Trap,
       "linkAggLink2Trap": linkAggLink2Trap,
       "rprSpanGroup": rprSpanGroup,
       "linkAggLinkGroup": linkAggLinkGroup,
       "zhoneLinkAggTable": zhoneLinkAggTable,
       "zhoneLinkAggEntry": zhoneLinkAggEntry,
       "zhoneLinkAggIfIndex": zhoneLinkAggIfIndex,
       "zhoneLinkAggPartnerSystem": zhoneLinkAggPartnerSystem,
       "zhoneLinkAggPartnerSystemPriority": zhoneLinkAggPartnerSystemPriority,
       "zhoneLinkAggPartnerGroupId": zhoneLinkAggPartnerGroupId,
       "phyEnetMauMib": phyEnetMauMib}
)
