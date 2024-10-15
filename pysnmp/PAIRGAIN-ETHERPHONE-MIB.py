# SNMP MIB module (PAIRGAIN-ETHERPHONE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/PAIRGAIN-ETHERPHONE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:36:21 2024
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

(pgEPhoneLocUnit,
 pgEPhoneRemUnit) = mibBuilder.importSymbols(
    "PAIRGAIN-COMMON-HD-MIB",
    "pgEPhoneLocUnit",
    "pgEPhoneRemUnit")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class TempPgUnitType(Integer32):
    """Custom type TempPgUnitType based on Integer32"""
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
              45)
        )
    )
    namedValues = NamedValues(
        *(("clu", 4),
          ("clu-384-449", 30),
          ("clu-384-V35", 6),
          ("clu-DSX", 7),
          ("clu-E1-449", 11),
          ("clu-E1-V35", 10),
          ("clu-Flex", 9),
          ("clu-G120", 13),
          ("clu-G703", 12),
          ("clu-MM768", 38),
          ("clu-REX-384", 36),
          ("clu-REX-E1", 34),
          ("clu-REX-T1", 32),
          ("clu-T1-449", 8),
          ("clu-T1-V35", 5),
          ("clu-X21", 14),
          ("cmu", 3),
          ("cu-384-449", 31),
          ("cu-384-V35", 16),
          ("cu-DBL", 25),
          ("cu-DSX", 17),
          ("cu-E1-449", 21),
          ("cu-E1-V35", 20),
          ("cu-Flex", 19),
          ("cu-G120", 23),
          ("cu-G703", 22),
          ("cu-MM768", 39),
          ("cu-REX-384", 37),
          ("cu-REX-E1", 35),
          ("cu-REX-T1", 33),
          ("cu-T1-449", 18),
          ("cu-T1-V35", 15),
          ("cu-X21", 24),
          ("empty", 1),
          ("eph-220", 42),
          ("eph-RT", 45),
          ("eph-remote", 44),
          ("epw-220", 43),
          ("hlu", 27),
          ("hmu", 26),
          ("mm-220", 40),
          ("mm-768", 41),
          ("other", 2),
          ("ps-AC", 28),
          ("ps-DC", 29))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PgLocUnitEpTable_Object = MibTable
pgLocUnitEpTable = _PgLocUnitEpTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    pgLocUnitEpTable.setStatus("mandatory")
_PgLocUnitEpEntry_Object = MibTableRow
pgLocUnitEpEntry = _PgLocUnitEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1)
)
pgLocUnitEpEntry.setIndexNames(
    (0, "PAIRGAIN-ETHERPHONE-MIB", "pgLocUnitEpIndex"),
)
if mibBuilder.loadTexts:
    pgLocUnitEpEntry.setStatus("mandatory")
_PgLocUnitEpIndex_Type = Integer32
_PgLocUnitEpIndex_Object = MibTableColumn
pgLocUnitEpIndex = _PgLocUnitEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 1),
    _PgLocUnitEpIndex_Type()
)
pgLocUnitEpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpIndex.setStatus("mandatory")
_PgLocUnitEpUnitType_Type = TempPgUnitType
_PgLocUnitEpUnitType_Object = MibTableColumn
pgLocUnitEpUnitType = _PgLocUnitEpUnitType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 2),
    _PgLocUnitEpUnitType_Type()
)
pgLocUnitEpUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpUnitType.setStatus("mandatory")
_PgLocUnitEpHwConfig_Type = Integer32
_PgLocUnitEpHwConfig_Object = MibTableColumn
pgLocUnitEpHwConfig = _PgLocUnitEpHwConfig_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 3),
    _PgLocUnitEpHwConfig_Type()
)
pgLocUnitEpHwConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpHwConfig.setStatus("mandatory")


class _PgLocUnitEpXcvrType_Type(Integer32):
    """Custom type pgLocUnitEpXcvrType based on Integer32"""
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
        *(("afe", 4),
          ("hybrid256", 3),
          ("hybrid384", 2),
          ("hybrid768", 1))
    )


_PgLocUnitEpXcvrType_Type.__name__ = "Integer32"
_PgLocUnitEpXcvrType_Object = MibTableColumn
pgLocUnitEpXcvrType = _PgLocUnitEpXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 4),
    _PgLocUnitEpXcvrType_Type()
)
pgLocUnitEpXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpXcvrType.setStatus("mandatory")
_PgLocUnitEpAFE_Type = Integer32
_PgLocUnitEpAFE_Object = MibTableColumn
pgLocUnitEpAFE = _PgLocUnitEpAFE_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 5),
    _PgLocUnitEpAFE_Type()
)
pgLocUnitEpAFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocUnitEpAFE.setStatus("mandatory")
_PgLocUnitEpDS0IdleCode_Type = Integer32
_PgLocUnitEpDS0IdleCode_Object = MibTableColumn
pgLocUnitEpDS0IdleCode = _PgLocUnitEpDS0IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 6),
    _PgLocUnitEpDS0IdleCode_Type()
)
pgLocUnitEpDS0IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocUnitEpDS0IdleCode.setStatus("mandatory")
_PgLocUnitEpPOTSDS0Alloc_Type = Integer32
_PgLocUnitEpPOTSDS0Alloc_Object = MibTableColumn
pgLocUnitEpPOTSDS0Alloc = _PgLocUnitEpPOTSDS0Alloc_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 7),
    _PgLocUnitEpPOTSDS0Alloc_Type()
)
pgLocUnitEpPOTSDS0Alloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocUnitEpPOTSDS0Alloc.setStatus("mandatory")
_PgLocUnitEpEthernetDS0Alloc_Type = Integer32
_PgLocUnitEpEthernetDS0Alloc_Object = MibTableColumn
pgLocUnitEpEthernetDS0Alloc = _PgLocUnitEpEthernetDS0Alloc_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 8),
    _PgLocUnitEpEthernetDS0Alloc_Type()
)
pgLocUnitEpEthernetDS0Alloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocUnitEpEthernetDS0Alloc.setStatus("mandatory")


class _PgLocUnitEpPOTSType_Type(Integer32):
    """Custom type pgLocUnitEpPOTSType based on Integer32"""
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
        *(("fxO1", 2),
          ("fxO2", 4),
          ("fxS1", 3),
          ("fxS2", 5),
          ("noPOT", 1))
    )


_PgLocUnitEpPOTSType_Type.__name__ = "Integer32"
_PgLocUnitEpPOTSType_Object = MibTableColumn
pgLocUnitEpPOTSType = _PgLocUnitEpPOTSType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 9),
    _PgLocUnitEpPOTSType_Type()
)
pgLocUnitEpPOTSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpPOTSType.setStatus("mandatory")


class _PgLocUnitEpPOTSEnable1_Type(Integer32):
    """Custom type pgLocUnitEpPOTSEnable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PgLocUnitEpPOTSEnable1_Type.__name__ = "Integer32"
_PgLocUnitEpPOTSEnable1_Object = MibTableColumn
pgLocUnitEpPOTSEnable1 = _PgLocUnitEpPOTSEnable1_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 10),
    _PgLocUnitEpPOTSEnable1_Type()
)
pgLocUnitEpPOTSEnable1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocUnitEpPOTSEnable1.setStatus("mandatory")


class _PgLocUnitEpPOTSEnable2_Type(Integer32):
    """Custom type pgLocUnitEpPOTSEnable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PgLocUnitEpPOTSEnable2_Type.__name__ = "Integer32"
_PgLocUnitEpPOTSEnable2_Object = MibTableColumn
pgLocUnitEpPOTSEnable2 = _PgLocUnitEpPOTSEnable2_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 11),
    _PgLocUnitEpPOTSEnable2_Type()
)
pgLocUnitEpPOTSEnable2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocUnitEpPOTSEnable2.setStatus("mandatory")


class _PgLocUnitEpPOTSStatus1_Type(Integer32):
    """Custom type pgLocUnitEpPOTSStatus1 based on Integer32"""
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
        *(("lcfo", 4),
          ("off-hook", 5),
          ("on-hook", 3),
          ("ring", 2),
          ("undefined", 1))
    )


_PgLocUnitEpPOTSStatus1_Type.__name__ = "Integer32"
_PgLocUnitEpPOTSStatus1_Object = MibTableColumn
pgLocUnitEpPOTSStatus1 = _PgLocUnitEpPOTSStatus1_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 12),
    _PgLocUnitEpPOTSStatus1_Type()
)
pgLocUnitEpPOTSStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpPOTSStatus1.setStatus("mandatory")


class _PgLocUnitEpPOTSStatus2_Type(Integer32):
    """Custom type pgLocUnitEpPOTSStatus2 based on Integer32"""
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
        *(("lcfo", 4),
          ("off-hook", 5),
          ("on-hook", 3),
          ("ring", 2),
          ("undefined", 1))
    )


_PgLocUnitEpPOTSStatus2_Type.__name__ = "Integer32"
_PgLocUnitEpPOTSStatus2_Object = MibTableColumn
pgLocUnitEpPOTSStatus2 = _PgLocUnitEpPOTSStatus2_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 13),
    _PgLocUnitEpPOTSStatus2_Type()
)
pgLocUnitEpPOTSStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpPOTSStatus2.setStatus("mandatory")
_PgLocUnitEpBridgeSWVer_Type = Integer32
_PgLocUnitEpBridgeSWVer_Object = MibTableColumn
pgLocUnitEpBridgeSWVer = _PgLocUnitEpBridgeSWVer_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 14),
    _PgLocUnitEpBridgeSWVer_Type()
)
pgLocUnitEpBridgeSWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpBridgeSWVer.setStatus("mandatory")


class _PgLocUnitEpERateMultiplier_Type(Integer32):
    """Custom type pgLocUnitEpERateMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("r56", 1),
          ("r64", 2))
    )


_PgLocUnitEpERateMultiplier_Type.__name__ = "Integer32"
_PgLocUnitEpERateMultiplier_Object = MibTableColumn
pgLocUnitEpERateMultiplier = _PgLocUnitEpERateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 15),
    _PgLocUnitEpERateMultiplier_Type()
)
pgLocUnitEpERateMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocUnitEpERateMultiplier.setStatus("mandatory")
_PgLocUnitEpMACAddr_Type = OctetString
_PgLocUnitEpMACAddr_Object = MibTableColumn
pgLocUnitEpMACAddr = _PgLocUnitEpMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 16),
    _PgLocUnitEpMACAddr_Type()
)
pgLocUnitEpMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpMACAddr.setStatus("mandatory")


class _PgLocUnitEpSpanTreeMode_Type(Integer32):
    """Custom type pgLocUnitEpSpanTreeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PgLocUnitEpSpanTreeMode_Type.__name__ = "Integer32"
_PgLocUnitEpSpanTreeMode_Object = MibTableColumn
pgLocUnitEpSpanTreeMode = _PgLocUnitEpSpanTreeMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 17),
    _PgLocUnitEpSpanTreeMode_Type()
)
pgLocUnitEpSpanTreeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocUnitEpSpanTreeMode.setStatus("mandatory")


class _PgLocUnitEpEncapMode_Type(Integer32):
    """Custom type pgLocUnitEpEncapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 1),
          ("ppp", 2))
    )


_PgLocUnitEpEncapMode_Type.__name__ = "Integer32"
_PgLocUnitEpEncapMode_Object = MibTableColumn
pgLocUnitEpEncapMode = _PgLocUnitEpEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 18),
    _PgLocUnitEpEncapMode_Type()
)
pgLocUnitEpEncapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocUnitEpEncapMode.setStatus("mandatory")


class _PgLocUnitEp10BaseTLinkStatus_Type(Integer32):
    """Custom type pgLocUnitEp10BaseTLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 1),
          ("link-up", 2),
          ("other", 3))
    )


_PgLocUnitEp10BaseTLinkStatus_Type.__name__ = "Integer32"
_PgLocUnitEp10BaseTLinkStatus_Object = MibTableColumn
pgLocUnitEp10BaseTLinkStatus = _PgLocUnitEp10BaseTLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 19),
    _PgLocUnitEp10BaseTLinkStatus_Type()
)
pgLocUnitEp10BaseTLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEp10BaseTLinkStatus.setStatus("mandatory")


class _PgLocUnitEp10BaseTLinkAlarmMode_Type(Integer32):
    """Custom type pgLocUnitEp10BaseTLinkAlarmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PgLocUnitEp10BaseTLinkAlarmMode_Type.__name__ = "Integer32"
_PgLocUnitEp10BaseTLinkAlarmMode_Object = MibTableColumn
pgLocUnitEp10BaseTLinkAlarmMode = _PgLocUnitEp10BaseTLinkAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 20),
    _PgLocUnitEp10BaseTLinkAlarmMode_Type()
)
pgLocUnitEp10BaseTLinkAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgLocUnitEp10BaseTLinkAlarmMode.setStatus("mandatory")
_PgLocUnitEpEPortInFrames_Type = Counter32
_PgLocUnitEpEPortInFrames_Object = MibTableColumn
pgLocUnitEpEPortInFrames = _PgLocUnitEpEPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 21),
    _PgLocUnitEpEPortInFrames_Type()
)
pgLocUnitEpEPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpEPortInFrames.setStatus("mandatory")
_PgLocUnitEpEPortOutFrames_Type = Counter32
_PgLocUnitEpEPortOutFrames_Object = MibTableColumn
pgLocUnitEpEPortOutFrames = _PgLocUnitEpEPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 22),
    _PgLocUnitEpEPortOutFrames_Type()
)
pgLocUnitEpEPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpEPortOutFrames.setStatus("mandatory")
_PgLocUnitEpEPortInDiscards_Type = Counter32
_PgLocUnitEpEPortInDiscards_Object = MibTableColumn
pgLocUnitEpEPortInDiscards = _PgLocUnitEpEPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 23),
    _PgLocUnitEpEPortInDiscards_Type()
)
pgLocUnitEpEPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpEPortInDiscards.setStatus("mandatory")
_PgLocUnitEpEPortInErrors_Type = Counter32
_PgLocUnitEpEPortInErrors_Object = MibTableColumn
pgLocUnitEpEPortInErrors = _PgLocUnitEpEPortInErrors_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 24),
    _PgLocUnitEpEPortInErrors_Type()
)
pgLocUnitEpEPortInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpEPortInErrors.setStatus("mandatory")
_PgLocUnitEpDSLPortInFrames_Type = Counter32
_PgLocUnitEpDSLPortInFrames_Object = MibTableColumn
pgLocUnitEpDSLPortInFrames = _PgLocUnitEpDSLPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 25),
    _PgLocUnitEpDSLPortInFrames_Type()
)
pgLocUnitEpDSLPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpDSLPortInFrames.setStatus("mandatory")
_PgLocUnitEpDSLPortOutFrames_Type = Counter32
_PgLocUnitEpDSLPortOutFrames_Object = MibTableColumn
pgLocUnitEpDSLPortOutFrames = _PgLocUnitEpDSLPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 26),
    _PgLocUnitEpDSLPortOutFrames_Type()
)
pgLocUnitEpDSLPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpDSLPortOutFrames.setStatus("mandatory")
_PgLocUnitEpDSLPortInDiscards_Type = Counter32
_PgLocUnitEpDSLPortInDiscards_Object = MibTableColumn
pgLocUnitEpDSLPortInDiscards = _PgLocUnitEpDSLPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 27),
    _PgLocUnitEpDSLPortInDiscards_Type()
)
pgLocUnitEpDSLPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpDSLPortInDiscards.setStatus("mandatory")
_PgLocUnitEpDSLPortInErrors_Type = Counter32
_PgLocUnitEpDSLPortInErrors_Object = MibTableColumn
pgLocUnitEpDSLPortInErrors = _PgLocUnitEpDSLPortInErrors_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 2, 1, 1, 28),
    _PgLocUnitEpDSLPortInErrors_Type()
)
pgLocUnitEpDSLPortInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgLocUnitEpDSLPortInErrors.setStatus("mandatory")
_PgRemUnitEpTable_Object = MibTable
pgRemUnitEpTable = _PgRemUnitEpTable_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    pgRemUnitEpTable.setStatus("mandatory")
_PgRemUnitEpEntry_Object = MibTableRow
pgRemUnitEpEntry = _PgRemUnitEpEntry_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1)
)
pgRemUnitEpEntry.setIndexNames(
    (0, "PAIRGAIN-ETHERPHONE-MIB", "pgRemUnitEpIndex"),
)
if mibBuilder.loadTexts:
    pgRemUnitEpEntry.setStatus("mandatory")
_PgRemUnitEpIndex_Type = Integer32
_PgRemUnitEpIndex_Object = MibTableColumn
pgRemUnitEpIndex = _PgRemUnitEpIndex_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 1),
    _PgRemUnitEpIndex_Type()
)
pgRemUnitEpIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpIndex.setStatus("mandatory")
_PgRemUnitEpUnitType_Type = TempPgUnitType
_PgRemUnitEpUnitType_Object = MibTableColumn
pgRemUnitEpUnitType = _PgRemUnitEpUnitType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 2),
    _PgRemUnitEpUnitType_Type()
)
pgRemUnitEpUnitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpUnitType.setStatus("mandatory")
_PgRemUnitEpHwConfig_Type = Integer32
_PgRemUnitEpHwConfig_Object = MibTableColumn
pgRemUnitEpHwConfig = _PgRemUnitEpHwConfig_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 3),
    _PgRemUnitEpHwConfig_Type()
)
pgRemUnitEpHwConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpHwConfig.setStatus("mandatory")


class _PgRemUnitEpXcvrType_Type(Integer32):
    """Custom type pgRemUnitEpXcvrType based on Integer32"""
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
        *(("afe", 4),
          ("hybrid256", 3),
          ("hybrid384", 2),
          ("hybrid768", 1))
    )


_PgRemUnitEpXcvrType_Type.__name__ = "Integer32"
_PgRemUnitEpXcvrType_Object = MibTableColumn
pgRemUnitEpXcvrType = _PgRemUnitEpXcvrType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 4),
    _PgRemUnitEpXcvrType_Type()
)
pgRemUnitEpXcvrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpXcvrType.setStatus("mandatory")
_PgRemUnitEpAFE_Type = Integer32
_PgRemUnitEpAFE_Object = MibTableColumn
pgRemUnitEpAFE = _PgRemUnitEpAFE_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 5),
    _PgRemUnitEpAFE_Type()
)
pgRemUnitEpAFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgRemUnitEpAFE.setStatus("mandatory")
_PgRemUnitEpDS0IdleCode_Type = Integer32
_PgRemUnitEpDS0IdleCode_Object = MibTableColumn
pgRemUnitEpDS0IdleCode = _PgRemUnitEpDS0IdleCode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 6),
    _PgRemUnitEpDS0IdleCode_Type()
)
pgRemUnitEpDS0IdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgRemUnitEpDS0IdleCode.setStatus("mandatory")
_PgRemUnitEpPOTSDS0Alloc_Type = Integer32
_PgRemUnitEpPOTSDS0Alloc_Object = MibTableColumn
pgRemUnitEpPOTSDS0Alloc = _PgRemUnitEpPOTSDS0Alloc_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 7),
    _PgRemUnitEpPOTSDS0Alloc_Type()
)
pgRemUnitEpPOTSDS0Alloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgRemUnitEpPOTSDS0Alloc.setStatus("mandatory")
_PgRemUnitEpEthernetDS0Alloc_Type = Integer32
_PgRemUnitEpEthernetDS0Alloc_Object = MibTableColumn
pgRemUnitEpEthernetDS0Alloc = _PgRemUnitEpEthernetDS0Alloc_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 8),
    _PgRemUnitEpEthernetDS0Alloc_Type()
)
pgRemUnitEpEthernetDS0Alloc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgRemUnitEpEthernetDS0Alloc.setStatus("mandatory")


class _PgRemUnitEpPOTSType_Type(Integer32):
    """Custom type pgRemUnitEpPOTSType based on Integer32"""
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
        *(("fxO1", 2),
          ("fxO2", 4),
          ("fxS1", 3),
          ("fxS2", 5),
          ("noPOT", 1))
    )


_PgRemUnitEpPOTSType_Type.__name__ = "Integer32"
_PgRemUnitEpPOTSType_Object = MibTableColumn
pgRemUnitEpPOTSType = _PgRemUnitEpPOTSType_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 9),
    _PgRemUnitEpPOTSType_Type()
)
pgRemUnitEpPOTSType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpPOTSType.setStatus("mandatory")


class _PgRemUnitEpPOTSEnable1_Type(Integer32):
    """Custom type pgRemUnitEpPOTSEnable1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PgRemUnitEpPOTSEnable1_Type.__name__ = "Integer32"
_PgRemUnitEpPOTSEnable1_Object = MibTableColumn
pgRemUnitEpPOTSEnable1 = _PgRemUnitEpPOTSEnable1_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 10),
    _PgRemUnitEpPOTSEnable1_Type()
)
pgRemUnitEpPOTSEnable1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgRemUnitEpPOTSEnable1.setStatus("mandatory")


class _PgRemUnitEpPOTSEnable2_Type(Integer32):
    """Custom type pgRemUnitEpPOTSEnable2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PgRemUnitEpPOTSEnable2_Type.__name__ = "Integer32"
_PgRemUnitEpPOTSEnable2_Object = MibTableColumn
pgRemUnitEpPOTSEnable2 = _PgRemUnitEpPOTSEnable2_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 11),
    _PgRemUnitEpPOTSEnable2_Type()
)
pgRemUnitEpPOTSEnable2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgRemUnitEpPOTSEnable2.setStatus("mandatory")


class _PgRemUnitEpPOTSStatus1_Type(Integer32):
    """Custom type pgRemUnitEpPOTSStatus1 based on Integer32"""
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
        *(("lcfo", 4),
          ("off-hook", 5),
          ("on-hook", 3),
          ("ring", 2),
          ("undefined", 1))
    )


_PgRemUnitEpPOTSStatus1_Type.__name__ = "Integer32"
_PgRemUnitEpPOTSStatus1_Object = MibTableColumn
pgRemUnitEpPOTSStatus1 = _PgRemUnitEpPOTSStatus1_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 12),
    _PgRemUnitEpPOTSStatus1_Type()
)
pgRemUnitEpPOTSStatus1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpPOTSStatus1.setStatus("mandatory")


class _PgRemUnitEpPOTSStatus2_Type(Integer32):
    """Custom type pgRemUnitEpPOTSStatus2 based on Integer32"""
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
        *(("lcfo", 4),
          ("off-hook", 5),
          ("on-hook", 3),
          ("ring", 2),
          ("undefined", 1))
    )


_PgRemUnitEpPOTSStatus2_Type.__name__ = "Integer32"
_PgRemUnitEpPOTSStatus2_Object = MibTableColumn
pgRemUnitEpPOTSStatus2 = _PgRemUnitEpPOTSStatus2_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 13),
    _PgRemUnitEpPOTSStatus2_Type()
)
pgRemUnitEpPOTSStatus2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpPOTSStatus2.setStatus("mandatory")
_PgRemUnitEpBridgeSWVer_Type = Integer32
_PgRemUnitEpBridgeSWVer_Object = MibTableColumn
pgRemUnitEpBridgeSWVer = _PgRemUnitEpBridgeSWVer_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 14),
    _PgRemUnitEpBridgeSWVer_Type()
)
pgRemUnitEpBridgeSWVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpBridgeSWVer.setStatus("mandatory")


class _PgRemUnitEpERateMultiplier_Type(Integer32):
    """Custom type pgRemUnitEpERateMultiplier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("r56", 1),
          ("r64", 2))
    )


_PgRemUnitEpERateMultiplier_Type.__name__ = "Integer32"
_PgRemUnitEpERateMultiplier_Object = MibTableColumn
pgRemUnitEpERateMultiplier = _PgRemUnitEpERateMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 15),
    _PgRemUnitEpERateMultiplier_Type()
)
pgRemUnitEpERateMultiplier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgRemUnitEpERateMultiplier.setStatus("mandatory")
_PgRemUnitEpMACAddr_Type = OctetString
_PgRemUnitEpMACAddr_Object = MibTableColumn
pgRemUnitEpMACAddr = _PgRemUnitEpMACAddr_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 16),
    _PgRemUnitEpMACAddr_Type()
)
pgRemUnitEpMACAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpMACAddr.setStatus("mandatory")


class _PgRemUnitEpSpanTreeMode_Type(Integer32):
    """Custom type pgRemUnitEpSpanTreeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PgRemUnitEpSpanTreeMode_Type.__name__ = "Integer32"
_PgRemUnitEpSpanTreeMode_Object = MibTableColumn
pgRemUnitEpSpanTreeMode = _PgRemUnitEpSpanTreeMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 17),
    _PgRemUnitEpSpanTreeMode_Type()
)
pgRemUnitEpSpanTreeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgRemUnitEpSpanTreeMode.setStatus("mandatory")


class _PgRemUnitEpEncapMode_Type(Integer32):
    """Custom type pgRemUnitEpEncapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 1),
          ("ppp", 2))
    )


_PgRemUnitEpEncapMode_Type.__name__ = "Integer32"
_PgRemUnitEpEncapMode_Object = MibTableColumn
pgRemUnitEpEncapMode = _PgRemUnitEpEncapMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 18),
    _PgRemUnitEpEncapMode_Type()
)
pgRemUnitEpEncapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgRemUnitEpEncapMode.setStatus("mandatory")


class _PgRemUnitEp10BaseTLinkStatus_Type(Integer32):
    """Custom type pgRemUnitEp10BaseTLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("link-down", 1),
          ("link-up", 2),
          ("other", 3))
    )


_PgRemUnitEp10BaseTLinkStatus_Type.__name__ = "Integer32"
_PgRemUnitEp10BaseTLinkStatus_Object = MibTableColumn
pgRemUnitEp10BaseTLinkStatus = _PgRemUnitEp10BaseTLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 19),
    _PgRemUnitEp10BaseTLinkStatus_Type()
)
pgRemUnitEp10BaseTLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEp10BaseTLinkStatus.setStatus("mandatory")


class _PgRemUnitEp10BaseTLinkAlarmMode_Type(Integer32):
    """Custom type pgRemUnitEp10BaseTLinkAlarmMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_PgRemUnitEp10BaseTLinkAlarmMode_Type.__name__ = "Integer32"
_PgRemUnitEp10BaseTLinkAlarmMode_Object = MibTableColumn
pgRemUnitEp10BaseTLinkAlarmMode = _PgRemUnitEp10BaseTLinkAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 20),
    _PgRemUnitEp10BaseTLinkAlarmMode_Type()
)
pgRemUnitEp10BaseTLinkAlarmMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pgRemUnitEp10BaseTLinkAlarmMode.setStatus("mandatory")
_PgRemUnitEpEPortInFrames_Type = Counter32
_PgRemUnitEpEPortInFrames_Object = MibTableColumn
pgRemUnitEpEPortInFrames = _PgRemUnitEpEPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 21),
    _PgRemUnitEpEPortInFrames_Type()
)
pgRemUnitEpEPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpEPortInFrames.setStatus("mandatory")
_PgRemUnitEpEPortOutFrames_Type = Counter32
_PgRemUnitEpEPortOutFrames_Object = MibTableColumn
pgRemUnitEpEPortOutFrames = _PgRemUnitEpEPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 22),
    _PgRemUnitEpEPortOutFrames_Type()
)
pgRemUnitEpEPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpEPortOutFrames.setStatus("mandatory")
_PgRemUnitEpEPortInDiscards_Type = Counter32
_PgRemUnitEpEPortInDiscards_Object = MibTableColumn
pgRemUnitEpEPortInDiscards = _PgRemUnitEpEPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 23),
    _PgRemUnitEpEPortInDiscards_Type()
)
pgRemUnitEpEPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpEPortInDiscards.setStatus("mandatory")
_PgRemUnitEpEPortInErrors_Type = Counter32
_PgRemUnitEpEPortInErrors_Object = MibTableColumn
pgRemUnitEpEPortInErrors = _PgRemUnitEpEPortInErrors_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 24),
    _PgRemUnitEpEPortInErrors_Type()
)
pgRemUnitEpEPortInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpEPortInErrors.setStatus("mandatory")
_PgRemUnitEpDSLPortInFrames_Type = Counter32
_PgRemUnitEpDSLPortInFrames_Object = MibTableColumn
pgRemUnitEpDSLPortInFrames = _PgRemUnitEpDSLPortInFrames_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 25),
    _PgRemUnitEpDSLPortInFrames_Type()
)
pgRemUnitEpDSLPortInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpDSLPortInFrames.setStatus("mandatory")
_PgRemUnitEpDSLPortOutFrames_Type = Counter32
_PgRemUnitEpDSLPortOutFrames_Object = MibTableColumn
pgRemUnitEpDSLPortOutFrames = _PgRemUnitEpDSLPortOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 26),
    _PgRemUnitEpDSLPortOutFrames_Type()
)
pgRemUnitEpDSLPortOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpDSLPortOutFrames.setStatus("mandatory")
_PgRemUnitEpDSLPortInDiscards_Type = Counter32
_PgRemUnitEpDSLPortInDiscards_Object = MibTableColumn
pgRemUnitEpDSLPortInDiscards = _PgRemUnitEpDSLPortInDiscards_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 27),
    _PgRemUnitEpDSLPortInDiscards_Type()
)
pgRemUnitEpDSLPortInDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpDSLPortInDiscards.setStatus("mandatory")
_PgRemUnitEpDSLPortInErrors_Type = Counter32
_PgRemUnitEpDSLPortInErrors_Object = MibTableColumn
pgRemUnitEpDSLPortInErrors = _PgRemUnitEpDSLPortInErrors_Object(
    (1, 3, 6, 1, 4, 1, 927, 1, 8, 3, 1, 1, 28),
    _PgRemUnitEpDSLPortInErrors_Type()
)
pgRemUnitEpDSLPortInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pgRemUnitEpDSLPortInErrors.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PAIRGAIN-ETHERPHONE-MIB",
    **{"TempPgUnitType": TempPgUnitType,
       "pgLocUnitEpTable": pgLocUnitEpTable,
       "pgLocUnitEpEntry": pgLocUnitEpEntry,
       "pgLocUnitEpIndex": pgLocUnitEpIndex,
       "pgLocUnitEpUnitType": pgLocUnitEpUnitType,
       "pgLocUnitEpHwConfig": pgLocUnitEpHwConfig,
       "pgLocUnitEpXcvrType": pgLocUnitEpXcvrType,
       "pgLocUnitEpAFE": pgLocUnitEpAFE,
       "pgLocUnitEpDS0IdleCode": pgLocUnitEpDS0IdleCode,
       "pgLocUnitEpPOTSDS0Alloc": pgLocUnitEpPOTSDS0Alloc,
       "pgLocUnitEpEthernetDS0Alloc": pgLocUnitEpEthernetDS0Alloc,
       "pgLocUnitEpPOTSType": pgLocUnitEpPOTSType,
       "pgLocUnitEpPOTSEnable1": pgLocUnitEpPOTSEnable1,
       "pgLocUnitEpPOTSEnable2": pgLocUnitEpPOTSEnable2,
       "pgLocUnitEpPOTSStatus1": pgLocUnitEpPOTSStatus1,
       "pgLocUnitEpPOTSStatus2": pgLocUnitEpPOTSStatus2,
       "pgLocUnitEpBridgeSWVer": pgLocUnitEpBridgeSWVer,
       "pgLocUnitEpERateMultiplier": pgLocUnitEpERateMultiplier,
       "pgLocUnitEpMACAddr": pgLocUnitEpMACAddr,
       "pgLocUnitEpSpanTreeMode": pgLocUnitEpSpanTreeMode,
       "pgLocUnitEpEncapMode": pgLocUnitEpEncapMode,
       "pgLocUnitEp10BaseTLinkStatus": pgLocUnitEp10BaseTLinkStatus,
       "pgLocUnitEp10BaseTLinkAlarmMode": pgLocUnitEp10BaseTLinkAlarmMode,
       "pgLocUnitEpEPortInFrames": pgLocUnitEpEPortInFrames,
       "pgLocUnitEpEPortOutFrames": pgLocUnitEpEPortOutFrames,
       "pgLocUnitEpEPortInDiscards": pgLocUnitEpEPortInDiscards,
       "pgLocUnitEpEPortInErrors": pgLocUnitEpEPortInErrors,
       "pgLocUnitEpDSLPortInFrames": pgLocUnitEpDSLPortInFrames,
       "pgLocUnitEpDSLPortOutFrames": pgLocUnitEpDSLPortOutFrames,
       "pgLocUnitEpDSLPortInDiscards": pgLocUnitEpDSLPortInDiscards,
       "pgLocUnitEpDSLPortInErrors": pgLocUnitEpDSLPortInErrors,
       "pgRemUnitEpTable": pgRemUnitEpTable,
       "pgRemUnitEpEntry": pgRemUnitEpEntry,
       "pgRemUnitEpIndex": pgRemUnitEpIndex,
       "pgRemUnitEpUnitType": pgRemUnitEpUnitType,
       "pgRemUnitEpHwConfig": pgRemUnitEpHwConfig,
       "pgRemUnitEpXcvrType": pgRemUnitEpXcvrType,
       "pgRemUnitEpAFE": pgRemUnitEpAFE,
       "pgRemUnitEpDS0IdleCode": pgRemUnitEpDS0IdleCode,
       "pgRemUnitEpPOTSDS0Alloc": pgRemUnitEpPOTSDS0Alloc,
       "pgRemUnitEpEthernetDS0Alloc": pgRemUnitEpEthernetDS0Alloc,
       "pgRemUnitEpPOTSType": pgRemUnitEpPOTSType,
       "pgRemUnitEpPOTSEnable1": pgRemUnitEpPOTSEnable1,
       "pgRemUnitEpPOTSEnable2": pgRemUnitEpPOTSEnable2,
       "pgRemUnitEpPOTSStatus1": pgRemUnitEpPOTSStatus1,
       "pgRemUnitEpPOTSStatus2": pgRemUnitEpPOTSStatus2,
       "pgRemUnitEpBridgeSWVer": pgRemUnitEpBridgeSWVer,
       "pgRemUnitEpERateMultiplier": pgRemUnitEpERateMultiplier,
       "pgRemUnitEpMACAddr": pgRemUnitEpMACAddr,
       "pgRemUnitEpSpanTreeMode": pgRemUnitEpSpanTreeMode,
       "pgRemUnitEpEncapMode": pgRemUnitEpEncapMode,
       "pgRemUnitEp10BaseTLinkStatus": pgRemUnitEp10BaseTLinkStatus,
       "pgRemUnitEp10BaseTLinkAlarmMode": pgRemUnitEp10BaseTLinkAlarmMode,
       "pgRemUnitEpEPortInFrames": pgRemUnitEpEPortInFrames,
       "pgRemUnitEpEPortOutFrames": pgRemUnitEpEPortOutFrames,
       "pgRemUnitEpEPortInDiscards": pgRemUnitEpEPortInDiscards,
       "pgRemUnitEpEPortInErrors": pgRemUnitEpEPortInErrors,
       "pgRemUnitEpDSLPortInFrames": pgRemUnitEpDSLPortInFrames,
       "pgRemUnitEpDSLPortOutFrames": pgRemUnitEpDSLPortOutFrames,
       "pgRemUnitEpDSLPortInDiscards": pgRemUnitEpDSLPortInDiscards,
       "pgRemUnitEpDSLPortInErrors": pgRemUnitEpDSLPortInErrors}
)
