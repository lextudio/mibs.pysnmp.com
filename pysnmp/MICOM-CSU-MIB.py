# SNMP MIB module (MICOM-CSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MICOM-CSU-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:21:39 2024
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

(micom_oscar,) = mibBuilder.importSymbols(
    "MICOM-OSCAR-MIB",
    "micom-oscar")

(mcmSysAsciiTimeOfDay,) = mibBuilder.importSymbols(
    "MICOM-SYS-MIB",
    "mcmSysAsciiTimeOfDay")

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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Micom_csu_ObjectIdentity = ObjectIdentity
micom_csu = _Micom_csu_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29)
)
_Csu_configuration_ObjectIdentity = ObjectIdentity
csu_configuration = _Csu_configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1)
)
_McmT1E1CsuCfgTable_Object = MibTable
mcmT1E1CsuCfgTable = _McmT1E1CsuCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1)
)
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgTable.setStatus("mandatory")
_McmT1E1CsuCfgEntry_Object = MibTableRow
mcmT1E1CsuCfgEntry = _McmT1E1CsuCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1)
)
mcmT1E1CsuCfgEntry.setIndexNames(
    (0, "MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"),
)
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgEntry.setStatus("mandatory")


class _McmT1E1CsuCfgifIndex_Type(Integer32):
    """Custom type mcmT1E1CsuCfgifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmT1E1CsuCfgifIndex_Type.__name__ = "Integer32"
_McmT1E1CsuCfgifIndex_Object = MibTableColumn
mcmT1E1CsuCfgifIndex = _McmT1E1CsuCfgifIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 1),
    _McmT1E1CsuCfgifIndex_Type()
)
mcmT1E1CsuCfgifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgifIndex.setStatus("mandatory")


class _McmT1E1CsuCfgLineType_Type(Integer32):
    """Custom type mcmT1E1CsuCfgLineType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("e1Csu", 2),
          ("t1Csu", 1))
    )


_McmT1E1CsuCfgLineType_Type.__name__ = "Integer32"
_McmT1E1CsuCfgLineType_Object = MibTableColumn
mcmT1E1CsuCfgLineType = _McmT1E1CsuCfgLineType_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 2),
    _McmT1E1CsuCfgLineType_Type()
)
mcmT1E1CsuCfgLineType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgLineType.setStatus("mandatory")


class _McmT1E1CsuCfgLineSpeed_Type(Integer32):
    """Custom type mcmT1E1CsuCfgLineSpeed based on Integer32"""
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
              61)
        )
    )
    namedValues = NamedValues(
        *(("idle", 61),
          ("ls-10ds0Times56K-560K", 40),
          ("ls-10ds0Times64K-640K", 10),
          ("ls-11ds0Times56K-616K", 41),
          ("ls-11ds0Times64K-704K", 11),
          ("ls-12ds0Times56K-672K", 42),
          ("ls-12ds0Times64K-768K", 12),
          ("ls-13ds0Times56K-728K", 43),
          ("ls-13ds0Times64K-832K", 13),
          ("ls-14ds0Times56K-784K", 44),
          ("ls-14ds0Times64K-896K", 14),
          ("ls-15ds0Times56K-840K", 45),
          ("ls-15ds0Times64K-960K", 15),
          ("ls-16ds0Times56K-896K", 46),
          ("ls-16ds0Times64K-1024K", 16),
          ("ls-17ds0Times56K-952K", 47),
          ("ls-17ds0Times64K-1088K", 17),
          ("ls-18ds0Times56K-1008K", 48),
          ("ls-18ds0Times64K-1152K", 18),
          ("ls-19ds0Times56K-1064K", 49),
          ("ls-19ds0Times64K-1216K", 19),
          ("ls-1ds0Times56K-56K", 31),
          ("ls-1ds0Times64K-64K", 1),
          ("ls-20ds0Times56K-1120K", 50),
          ("ls-20ds0Times64K-1280K", 20),
          ("ls-21ds0Times56K-1176K", 51),
          ("ls-21ds0Times64K-1344K", 21),
          ("ls-22ds0Times56K-1232K", 52),
          ("ls-22ds0Times64K-1408K", 22),
          ("ls-23ds0Times56K-1288K", 53),
          ("ls-23ds0Times64K-1472K", 23),
          ("ls-24ds0Times56K-1344K", 54),
          ("ls-24ds0Times64K-1536K", 24),
          ("ls-25ds0Times56K-1400K", 55),
          ("ls-25ds0Times64K-1600K", 25),
          ("ls-26ds0Times56K-1456K", 56),
          ("ls-26ds0Times64K-1664K", 26),
          ("ls-27ds0Times56K-1512K", 57),
          ("ls-27ds0Times64K-1728K", 27),
          ("ls-28ds0Times56K-1568K", 58),
          ("ls-28ds0Times64K-1792K", 28),
          ("ls-29ds0Times56K-1624K", 59),
          ("ls-29ds0Times64K-1856K", 29),
          ("ls-2ds0Times56K-112K", 32),
          ("ls-2ds0Times64K-128K", 2),
          ("ls-30ds0Times56K-1680K", 60),
          ("ls-30ds0Times64K-1920K", 30),
          ("ls-3ds0Times56K-168K", 33),
          ("ls-3ds0Times64K-192K", 3),
          ("ls-4ds0Times56K-224K", 34),
          ("ls-4ds0Times64K-256K", 4),
          ("ls-5ds0Times56K-280K", 35),
          ("ls-5ds0Times64K-320K", 5),
          ("ls-6ds0Times56K-336K", 36),
          ("ls-6ds0Times64K-384K", 6),
          ("ls-7ds0Times56K-392K", 37),
          ("ls-7ds0Times64K-448K", 7),
          ("ls-8ds0Times56K-448K", 38),
          ("ls-8ds0Times64K-512K", 8),
          ("ls-9ds0Times56K-504K", 39),
          ("ls-9ds0Times64K-576K", 9))
    )


_McmT1E1CsuCfgLineSpeed_Type.__name__ = "Integer32"
_McmT1E1CsuCfgLineSpeed_Object = MibTableColumn
mcmT1E1CsuCfgLineSpeed = _McmT1E1CsuCfgLineSpeed_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 3),
    _McmT1E1CsuCfgLineSpeed_Type()
)
mcmT1E1CsuCfgLineSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgLineSpeed.setStatus("mandatory")


class _McmT1E1CsuCfgLineBuildOut_Type(Integer32):
    """Custom type mcmT1E1CsuCfgLineBuildOut based on Integer32"""
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
              15)
        )
    )
    namedValues = NamedValues(
        *(("dist-0-133-feet", 1),
          ("dist-133-266-feet", 2),
          ("dist-266-399-feet", 3),
          ("dist-399-533-feet", 4),
          ("dist-533-655-feet", 5),
          ("neg-15-db", 7),
          ("neg-22pt5-db", 8),
          ("neg-7pt5-db", 6),
          ("ohm-120-high-return-loss-1-1pt36-step-up", 15),
          ("ohm-120-normal", 10),
          ("ohm-120-protection-resistors", 12),
          ("ohm-75-high-return-loss-1-1pt15-step-up", 13),
          ("ohm-75-high-return-loss-1-1pt36-step-up", 14),
          ("ohm-75-normal", 9),
          ("ohm-75-protection-resistors", 11))
    )


_McmT1E1CsuCfgLineBuildOut_Type.__name__ = "Integer32"
_McmT1E1CsuCfgLineBuildOut_Object = MibTableColumn
mcmT1E1CsuCfgLineBuildOut = _McmT1E1CsuCfgLineBuildOut_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 4),
    _McmT1E1CsuCfgLineBuildOut_Type()
)
mcmT1E1CsuCfgLineBuildOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgLineBuildOut.setStatus("mandatory")


class _McmT1E1CsuCfgTxIdleCode_Type(Integer32):
    """Custom type mcmT1E1CsuCfgTxIdleCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CsuCfgTxIdleCode_Type.__name__ = "Integer32"
_McmT1E1CsuCfgTxIdleCode_Object = MibTableColumn
mcmT1E1CsuCfgTxIdleCode = _McmT1E1CsuCfgTxIdleCode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 5),
    _McmT1E1CsuCfgTxIdleCode_Type()
)
mcmT1E1CsuCfgTxIdleCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgTxIdleCode.setStatus("mandatory")


class _McmT1E1CsuCfgTxRxClkSource_Type(Integer32):
    """Custom type mcmT1E1CsuCfgTxRxClkSource based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalClockingSource", 2),
          ("internalClockingSource", 1))
    )


_McmT1E1CsuCfgTxRxClkSource_Type.__name__ = "Integer32"
_McmT1E1CsuCfgTxRxClkSource_Object = MibTableColumn
mcmT1E1CsuCfgTxRxClkSource = _McmT1E1CsuCfgTxRxClkSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 6),
    _McmT1E1CsuCfgTxRxClkSource_Type()
)
mcmT1E1CsuCfgTxRxClkSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgTxRxClkSource.setStatus("mandatory")


class _McmT1E1CsuCfgDS0BasicRate_Type(Integer32):
    """Custom type mcmT1E1CsuCfgDS0BasicRate based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("br56K-basicRate", 2),
          ("br64K-basicRate", 1))
    )


_McmT1E1CsuCfgDS0BasicRate_Type.__name__ = "Integer32"
_McmT1E1CsuCfgDS0BasicRate_Object = MibTableColumn
mcmT1E1CsuCfgDS0BasicRate = _McmT1E1CsuCfgDS0BasicRate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 7),
    _McmT1E1CsuCfgDS0BasicRate_Type()
)
mcmT1E1CsuCfgDS0BasicRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgDS0BasicRate.setStatus("mandatory")


class _McmT1E1CsuCfgLocalLoopback_Type(Integer32):
    """Custom type mcmT1E1CsuCfgLocalLoopback based on Integer32"""
    defaultValue = 1

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


_McmT1E1CsuCfgLocalLoopback_Type.__name__ = "Integer32"
_McmT1E1CsuCfgLocalLoopback_Object = MibTableColumn
mcmT1E1CsuCfgLocalLoopback = _McmT1E1CsuCfgLocalLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 8),
    _McmT1E1CsuCfgLocalLoopback_Type()
)
mcmT1E1CsuCfgLocalLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgLocalLoopback.setStatus("mandatory")


class _McmT1E1CsuCfgRemoteLoopback_Type(Integer32):
    """Custom type mcmT1E1CsuCfgRemoteLoopback based on Integer32"""
    defaultValue = 1

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


_McmT1E1CsuCfgRemoteLoopback_Type.__name__ = "Integer32"
_McmT1E1CsuCfgRemoteLoopback_Object = MibTableColumn
mcmT1E1CsuCfgRemoteLoopback = _McmT1E1CsuCfgRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 9),
    _McmT1E1CsuCfgRemoteLoopback_Type()
)
mcmT1E1CsuCfgRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgRemoteLoopback.setStatus("mandatory")


class _McmT1E1CsuCfgFramerLoopback_Type(Integer32):
    """Custom type mcmT1E1CsuCfgFramerLoopback based on Integer32"""
    defaultValue = 1

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


_McmT1E1CsuCfgFramerLoopback_Type.__name__ = "Integer32"
_McmT1E1CsuCfgFramerLoopback_Object = MibTableColumn
mcmT1E1CsuCfgFramerLoopback = _McmT1E1CsuCfgFramerLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 10),
    _McmT1E1CsuCfgFramerLoopback_Type()
)
mcmT1E1CsuCfgFramerLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgFramerLoopback.setStatus("mandatory")


class _McmT1E1CsuCfgTrapEnable_Type(Integer32):
    """Custom type mcmT1E1CsuCfgTrapEnable based on Integer32"""
    defaultValue = 2

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


_McmT1E1CsuCfgTrapEnable_Type.__name__ = "Integer32"
_McmT1E1CsuCfgTrapEnable_Object = MibTableColumn
mcmT1E1CsuCfgTrapEnable = _McmT1E1CsuCfgTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 11),
    _McmT1E1CsuCfgTrapEnable_Type()
)
mcmT1E1CsuCfgTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgTrapEnable.setStatus("mandatory")


class _McmT1E1CsuCfgFrameFmt_Type(Integer32):
    """Custom type mcmT1E1CsuCfgFrameFmt based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("d4FramingMode", 1),
          ("esfFramingMode", 2))
    )


_McmT1E1CsuCfgFrameFmt_Type.__name__ = "Integer32"
_McmT1E1CsuCfgFrameFmt_Object = MibTableColumn
mcmT1E1CsuCfgFrameFmt = _McmT1E1CsuCfgFrameFmt_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 12),
    _McmT1E1CsuCfgFrameFmt_Type()
)
mcmT1E1CsuCfgFrameFmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgFrameFmt.setStatus("mandatory")


class _McmT1E1CsuCfgTxRx0CodeSuppress_Type(Integer32):
    """Custom type mcmT1E1CsuCfgTxRx0CodeSuppress based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-b8zs", 1),
          ("enable-b8zs", 2))
    )


_McmT1E1CsuCfgTxRx0CodeSuppress_Type.__name__ = "Integer32"
_McmT1E1CsuCfgTxRx0CodeSuppress_Object = MibTableColumn
mcmT1E1CsuCfgTxRx0CodeSuppress = _McmT1E1CsuCfgTxRx0CodeSuppress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 13),
    _McmT1E1CsuCfgTxRx0CodeSuppress_Type()
)
mcmT1E1CsuCfgTxRx0CodeSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgTxRx0CodeSuppress.setStatus("mandatory")


class _McmT1E1CsuCfgTxB7ZeroSuppress_Type(Integer32):
    """Custom type mcmT1E1CsuCfgTxB7ZeroSuppress based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable-b7zs", 1),
          ("enable-b7zs", 2))
    )


_McmT1E1CsuCfgTxB7ZeroSuppress_Type.__name__ = "Integer32"
_McmT1E1CsuCfgTxB7ZeroSuppress_Object = MibTableColumn
mcmT1E1CsuCfgTxB7ZeroSuppress = _McmT1E1CsuCfgTxB7ZeroSuppress_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 14),
    _McmT1E1CsuCfgTxB7ZeroSuppress_Type()
)
mcmT1E1CsuCfgTxB7ZeroSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgTxB7ZeroSuppress.setStatus("mandatory")


class _McmT1E1CsuCfgPayloadLoopback_Type(Integer32):
    """Custom type mcmT1E1CsuCfgPayloadLoopback based on Integer32"""
    defaultValue = 1

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


_McmT1E1CsuCfgPayloadLoopback_Type.__name__ = "Integer32"
_McmT1E1CsuCfgPayloadLoopback_Object = MibTableColumn
mcmT1E1CsuCfgPayloadLoopback = _McmT1E1CsuCfgPayloadLoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 15),
    _McmT1E1CsuCfgPayloadLoopback_Type()
)
mcmT1E1CsuCfgPayloadLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgPayloadLoopback.setStatus("mandatory")


class _McmT1E1CsuCfgTransmitLoopUp_Type(Integer32):
    """Custom type mcmT1E1CsuCfgTransmitLoopUp based on Integer32"""
    defaultValue = 1

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


_McmT1E1CsuCfgTransmitLoopUp_Type.__name__ = "Integer32"
_McmT1E1CsuCfgTransmitLoopUp_Object = MibTableColumn
mcmT1E1CsuCfgTransmitLoopUp = _McmT1E1CsuCfgTransmitLoopUp_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 16),
    _McmT1E1CsuCfgTransmitLoopUp_Type()
)
mcmT1E1CsuCfgTransmitLoopUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgTransmitLoopUp.setStatus("mandatory")


class _McmT1E1CsuCfgTransmitLoopDown_Type(Integer32):
    """Custom type mcmT1E1CsuCfgTransmitLoopDown based on Integer32"""
    defaultValue = 1

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


_McmT1E1CsuCfgTransmitLoopDown_Type.__name__ = "Integer32"
_McmT1E1CsuCfgTransmitLoopDown_Object = MibTableColumn
mcmT1E1CsuCfgTransmitLoopDown = _McmT1E1CsuCfgTransmitLoopDown_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 17),
    _McmT1E1CsuCfgTransmitLoopDown_Type()
)
mcmT1E1CsuCfgTransmitLoopDown.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgTransmitLoopDown.setStatus("mandatory")


class _McmT1E1CsuCfgTxRxHDB3_Type(Integer32):
    """Custom type mcmT1E1CsuCfgTxRxHDB3 based on Integer32"""
    defaultValue = 2

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


_McmT1E1CsuCfgTxRxHDB3_Type.__name__ = "Integer32"
_McmT1E1CsuCfgTxRxHDB3_Object = MibTableColumn
mcmT1E1CsuCfgTxRxHDB3 = _McmT1E1CsuCfgTxRxHDB3_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 18),
    _McmT1E1CsuCfgTxRxHDB3_Type()
)
mcmT1E1CsuCfgTxRxHDB3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgTxRxHDB3.setStatus("mandatory")


class _McmT1E1CsuCfgTxRxCRC4_Type(Integer32):
    """Custom type mcmT1E1CsuCfgTxRxCRC4 based on Integer32"""
    defaultValue = 1

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


_McmT1E1CsuCfgTxRxCRC4_Type.__name__ = "Integer32"
_McmT1E1CsuCfgTxRxCRC4_Object = MibTableColumn
mcmT1E1CsuCfgTxRxCRC4 = _McmT1E1CsuCfgTxRxCRC4_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 19),
    _McmT1E1CsuCfgTxRxCRC4_Type()
)
mcmT1E1CsuCfgTxRxCRC4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgTxRxCRC4.setStatus("mandatory")


class _McmT1E1CsuCfgDS0Connection_Type(DisplayString):
    """Custom type mcmT1E1CsuCfgDS0Connection based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 83),
    )


_McmT1E1CsuCfgDS0Connection_Type.__name__ = "DisplayString"
_McmT1E1CsuCfgDS0Connection_Object = MibTableColumn
mcmT1E1CsuCfgDS0Connection = _McmT1E1CsuCfgDS0Connection_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 1, 1, 20),
    _McmT1E1CsuCfgDS0Connection_Type()
)
mcmT1E1CsuCfgDS0Connection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmT1E1CsuCfgDS0Connection.setStatus("mandatory")
_McmCsuCfgTable_Object = MibTable
mcmCsuCfgTable = _McmCsuCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2)
)
if mibBuilder.loadTexts:
    mcmCsuCfgTable.setStatus("mandatory")
_McmCsuCfgEntry_Object = MibTableRow
mcmCsuCfgEntry = _McmCsuCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1)
)
mcmCsuCfgEntry.setIndexNames(
    (0, "MICOM-CSU-MIB", "mcmCsuCfgifIndex"),
)
if mibBuilder.loadTexts:
    mcmCsuCfgEntry.setStatus("mandatory")


class _McmCsuCfgifIndex_Type(Integer32):
    """Custom type mcmCsuCfgifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmCsuCfgifIndex_Type.__name__ = "Integer32"
_McmCsuCfgifIndex_Object = MibTableColumn
mcmCsuCfgifIndex = _McmCsuCfgifIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 1),
    _McmCsuCfgifIndex_Type()
)
mcmCsuCfgifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmCsuCfgifIndex.setStatus("mandatory")


class _McmCsuCfgOperatingMode_Type(Integer32):
    """Custom type mcmCsuCfgOperatingMode based on Integer32"""
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
        *(("cc-64k-ClearChannel-64k", 3),
          ("dds-pri-2Wire-56k", 4),
          ("dds-pri-4Wire-56k", 1),
          ("dds-sc-WithSecondaryChannel-72k", 2))
    )


_McmCsuCfgOperatingMode_Type.__name__ = "Integer32"
_McmCsuCfgOperatingMode_Object = MibTableColumn
mcmCsuCfgOperatingMode = _McmCsuCfgOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 2),
    _McmCsuCfgOperatingMode_Type()
)
mcmCsuCfgOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmCsuCfgOperatingMode.setStatus("mandatory")


class _McmCsuCfgClockingSource_Type(Integer32):
    """Custom type mcmCsuCfgClockingSource based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("externalClock", 1),
          ("internalClock", 2))
    )


_McmCsuCfgClockingSource_Type.__name__ = "Integer32"
_McmCsuCfgClockingSource_Object = MibTableColumn
mcmCsuCfgClockingSource = _McmCsuCfgClockingSource_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 3),
    _McmCsuCfgClockingSource_Type()
)
mcmCsuCfgClockingSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmCsuCfgClockingSource.setStatus("mandatory")


class _McmCsuCfgTxOutOfFrame_Type(Integer32):
    """Custom type mcmCsuCfgTxOutOfFrame based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitOutOfFrame", 2))
    )


_McmCsuCfgTxOutOfFrame_Type.__name__ = "Integer32"
_McmCsuCfgTxOutOfFrame_Object = MibTableColumn
mcmCsuCfgTxOutOfFrame = _McmCsuCfgTxOutOfFrame_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 4),
    _McmCsuCfgTxOutOfFrame_Type()
)
mcmCsuCfgTxOutOfFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmCsuCfgTxOutOfFrame.setStatus("mandatory")


class _McmCsuCfgTxOutOfService_Type(Integer32):
    """Custom type mcmCsuCfgTxOutOfService based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitOutOfService", 2))
    )


_McmCsuCfgTxOutOfService_Type.__name__ = "Integer32"
_McmCsuCfgTxOutOfService_Object = MibTableColumn
mcmCsuCfgTxOutOfService = _McmCsuCfgTxOutOfService_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 5),
    _McmCsuCfgTxOutOfService_Type()
)
mcmCsuCfgTxOutOfService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmCsuCfgTxOutOfService.setStatus("mandatory")


class _McmCsuCfgTxControlModeIdle_Type(Integer32):
    """Custom type mcmCsuCfgTxControlModeIdle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitControlModeIdle", 2))
    )


_McmCsuCfgTxControlModeIdle_Type.__name__ = "Integer32"
_McmCsuCfgTxControlModeIdle_Object = MibTableColumn
mcmCsuCfgTxControlModeIdle = _McmCsuCfgTxControlModeIdle_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 6),
    _McmCsuCfgTxControlModeIdle_Type()
)
mcmCsuCfgTxControlModeIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmCsuCfgTxControlModeIdle.setStatus("mandatory")


class _McmCsuCfgZeroSuppressDisable_Type(Integer32):
    """Custom type mcmCsuCfgZeroSuppressDisable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("zeroSuppressionDisable", 2))
    )


_McmCsuCfgZeroSuppressDisable_Type.__name__ = "Integer32"
_McmCsuCfgZeroSuppressDisable_Object = MibTableColumn
mcmCsuCfgZeroSuppressDisable = _McmCsuCfgZeroSuppressDisable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 7),
    _McmCsuCfgZeroSuppressDisable_Type()
)
mcmCsuCfgZeroSuppressDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmCsuCfgZeroSuppressDisable.setStatus("mandatory")


class _McmCsuCfgTxIdle_Type(Integer32):
    """Custom type mcmCsuCfgTxIdle based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normalTransmitCondition", 1),
          ("transmitIdle", 2))
    )


_McmCsuCfgTxIdle_Type.__name__ = "Integer32"
_McmCsuCfgTxIdle_Object = MibTableColumn
mcmCsuCfgTxIdle = _McmCsuCfgTxIdle_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 8),
    _McmCsuCfgTxIdle_Type()
)
mcmCsuCfgTxIdle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmCsuCfgTxIdle.setStatus("mandatory")


class _McmCsuCfgCSULoopback_Type(Integer32):
    """Custom type mcmCsuCfgCSULoopback based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceCSUtoLoopback", 2),
          ("normalReceiveCondition", 1))
    )


_McmCsuCfgCSULoopback_Type.__name__ = "Integer32"
_McmCsuCfgCSULoopback_Object = MibTableColumn
mcmCsuCfgCSULoopback = _McmCsuCfgCSULoopback_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 9),
    _McmCsuCfgCSULoopback_Type()
)
mcmCsuCfgCSULoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmCsuCfgCSULoopback.setStatus("mandatory")


class _McmCsuCfgFilterForceEnable_Type(Integer32):
    """Custom type mcmCsuCfgFilterForceEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filterForceEnable", 2),
          ("normalReceiveCondition", 1))
    )


_McmCsuCfgFilterForceEnable_Type.__name__ = "Integer32"
_McmCsuCfgFilterForceEnable_Object = MibTableColumn
mcmCsuCfgFilterForceEnable = _McmCsuCfgFilterForceEnable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 10),
    _McmCsuCfgFilterForceEnable_Type()
)
mcmCsuCfgFilterForceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmCsuCfgFilterForceEnable.setStatus("mandatory")


class _McmCsuCfgFilterForcingCntl_Type(Integer32):
    """Custom type mcmCsuCfgFilterForcingCntl based on Integer32"""
    defaultValue = 16

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
              16)
        )
    )
    namedValues = NamedValues(
        *(("fg0db-FilterGain", 16),
          ("fg12db-FilterGain", 14),
          ("fg18db-FilterGain", 13),
          ("fg24db-FilterGain", 12),
          ("fg30db-FilterGain", 11),
          ("fg36db-FilterGain", 10),
          ("fg42db-FilterGain", 9),
          ("fg48db-FilterGain", 8),
          ("fg54db-FilterGain", 7),
          ("fg60db-FilterGain", 6),
          ("fg66db-FilterGain", 5),
          ("fg6db-FilterGain", 15),
          ("fg72db-FilterGain", 4),
          ("fg78db-FilterGain", 3),
          ("fg84db-FilterGain", 2),
          ("fg90db-FilterGain", 1))
    )


_McmCsuCfgFilterForcingCntl_Type.__name__ = "Integer32"
_McmCsuCfgFilterForcingCntl_Object = MibTableColumn
mcmCsuCfgFilterForcingCntl = _McmCsuCfgFilterForcingCntl_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 1, 2, 1, 11),
    _McmCsuCfgFilterForcingCntl_Type()
)
mcmCsuCfgFilterForcingCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcmCsuCfgFilterForcingCntl.setStatus("mandatory")
_Csu_status_ObjectIdentity = ObjectIdentity
csu_status = _Csu_status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2)
)
_McmT1E1CsuCntlRegStatusTable_Object = MibTable
mcmT1E1CsuCntlRegStatusTable = _McmT1E1CsuCntlRegStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1)
)
if mibBuilder.loadTexts:
    mcmT1E1CsuCntlRegStatusTable.setStatus("mandatory")
_McmT1E1CsuCntlRegStatusEntry_Object = MibTableRow
mcmT1E1CsuCntlRegStatusEntry = _McmT1E1CsuCntlRegStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1)
)
mcmT1E1CsuCntlRegStatusEntry.setIndexNames(
    (0, "MICOM-CSU-MIB", "mcmT1E1CSUStatusifIndex"),
)
if mibBuilder.loadTexts:
    mcmT1E1CsuCntlRegStatusEntry.setStatus("mandatory")


class _McmT1E1CSUStatusifIndex_Type(Integer32):
    """Custom type mcmT1E1CSUStatusifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmT1E1CSUStatusifIndex_Type.__name__ = "Integer32"
_McmT1E1CSUStatusifIndex_Object = MibTableColumn
mcmT1E1CSUStatusifIndex = _McmT1E1CSUStatusifIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 1),
    _McmT1E1CSUStatusifIndex_Type()
)
mcmT1E1CSUStatusifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusifIndex.setStatus("mandatory")


class _McmT1E1CSUStatusCntlReg1_Type(Integer32):
    """Custom type mcmT1E1CSUStatusCntlReg1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CSUStatusCntlReg1_Type.__name__ = "Integer32"
_McmT1E1CSUStatusCntlReg1_Object = MibTableColumn
mcmT1E1CSUStatusCntlReg1 = _McmT1E1CSUStatusCntlReg1_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 2),
    _McmT1E1CSUStatusCntlReg1_Type()
)
mcmT1E1CSUStatusCntlReg1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusCntlReg1.setStatus("mandatory")


class _McmT1E1CSUStatusCntlReg2_Type(Integer32):
    """Custom type mcmT1E1CSUStatusCntlReg2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CSUStatusCntlReg2_Type.__name__ = "Integer32"
_McmT1E1CSUStatusCntlReg2_Object = MibTableColumn
mcmT1E1CSUStatusCntlReg2 = _McmT1E1CSUStatusCntlReg2_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 3),
    _McmT1E1CSUStatusCntlReg2_Type()
)
mcmT1E1CSUStatusCntlReg2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusCntlReg2.setStatus("mandatory")


class _McmT1E1CSUStatusCntlReg3_Type(Integer32):
    """Custom type mcmT1E1CSUStatusCntlReg3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CSUStatusCntlReg3_Type.__name__ = "Integer32"
_McmT1E1CSUStatusCntlReg3_Object = MibTableColumn
mcmT1E1CSUStatusCntlReg3 = _McmT1E1CSUStatusCntlReg3_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 4),
    _McmT1E1CSUStatusCntlReg3_Type()
)
mcmT1E1CSUStatusCntlReg3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusCntlReg3.setStatus("mandatory")


class _McmT1E1CSUStatusCntlReg4_Type(Integer32):
    """Custom type mcmT1E1CSUStatusCntlReg4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CSUStatusCntlReg4_Type.__name__ = "Integer32"
_McmT1E1CSUStatusCntlReg4_Object = MibTableColumn
mcmT1E1CSUStatusCntlReg4 = _McmT1E1CSUStatusCntlReg4_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 5),
    _McmT1E1CSUStatusCntlReg4_Type()
)
mcmT1E1CSUStatusCntlReg4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusCntlReg4.setStatus("mandatory")


class _McmT1E1CSUStatusCntlReg5_Type(Integer32):
    """Custom type mcmT1E1CSUStatusCntlReg5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CSUStatusCntlReg5_Type.__name__ = "Integer32"
_McmT1E1CSUStatusCntlReg5_Object = MibTableColumn
mcmT1E1CSUStatusCntlReg5 = _McmT1E1CSUStatusCntlReg5_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 6),
    _McmT1E1CSUStatusCntlReg5_Type()
)
mcmT1E1CSUStatusCntlReg5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusCntlReg5.setStatus("mandatory")


class _McmT1E1CSUStatusCntlReg6_Type(Integer32):
    """Custom type mcmT1E1CSUStatusCntlReg6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CSUStatusCntlReg6_Type.__name__ = "Integer32"
_McmT1E1CSUStatusCntlReg6_Object = MibTableColumn
mcmT1E1CSUStatusCntlReg6 = _McmT1E1CSUStatusCntlReg6_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 7),
    _McmT1E1CSUStatusCntlReg6_Type()
)
mcmT1E1CSUStatusCntlReg6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusCntlReg6.setStatus("mandatory")


class _McmT1E1CSUStatusCntlReg7_Type(Integer32):
    """Custom type mcmT1E1CSUStatusCntlReg7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CSUStatusCntlReg7_Type.__name__ = "Integer32"
_McmT1E1CSUStatusCntlReg7_Object = MibTableColumn
mcmT1E1CSUStatusCntlReg7 = _McmT1E1CSUStatusCntlReg7_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 8),
    _McmT1E1CSUStatusCntlReg7_Type()
)
mcmT1E1CSUStatusCntlReg7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusCntlReg7.setStatus("mandatory")


class _McmT1E1CSUStatusCntlReg8_Type(Integer32):
    """Custom type mcmT1E1CSUStatusCntlReg8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CSUStatusCntlReg8_Type.__name__ = "Integer32"
_McmT1E1CSUStatusCntlReg8_Object = MibTableColumn
mcmT1E1CSUStatusCntlReg8 = _McmT1E1CSUStatusCntlReg8_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 9),
    _McmT1E1CSUStatusCntlReg8_Type()
)
mcmT1E1CSUStatusCntlReg8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusCntlReg8.setStatus("mandatory")


class _McmT1E1CSUStatusCntlReg9_Type(Integer32):
    """Custom type mcmT1E1CSUStatusCntlReg9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CSUStatusCntlReg9_Type.__name__ = "Integer32"
_McmT1E1CSUStatusCntlReg9_Object = MibTableColumn
mcmT1E1CSUStatusCntlReg9 = _McmT1E1CSUStatusCntlReg9_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 10),
    _McmT1E1CSUStatusCntlReg9_Type()
)
mcmT1E1CSUStatusCntlReg9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusCntlReg9.setStatus("mandatory")


class _McmT1E1CSUStatusCntlReg10_Type(Integer32):
    """Custom type mcmT1E1CSUStatusCntlReg10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmT1E1CSUStatusCntlReg10_Type.__name__ = "Integer32"
_McmT1E1CSUStatusCntlReg10_Object = MibTableColumn
mcmT1E1CSUStatusCntlReg10 = _McmT1E1CSUStatusCntlReg10_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 1, 1, 11),
    _McmT1E1CSUStatusCntlReg10_Type()
)
mcmT1E1CSUStatusCntlReg10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1E1CSUStatusCntlReg10.setStatus("mandatory")
_McmT1CsuGenStatusTable_Object = MibTable
mcmT1CsuGenStatusTable = _McmT1CsuGenStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2)
)
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusTable.setStatus("mandatory")
_McmT1CsuGenStatusEntry_Object = MibTableRow
mcmT1CsuGenStatusEntry = _McmT1CsuGenStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1)
)
mcmT1CsuGenStatusEntry.setIndexNames(
    (0, "MICOM-CSU-MIB", "mcmT1CsuGenStatusifIndex"),
)
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusEntry.setStatus("mandatory")


class _McmT1CsuGenStatusifIndex_Type(Integer32):
    """Custom type mcmT1CsuGenStatusifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmT1CsuGenStatusifIndex_Type.__name__ = "Integer32"
_McmT1CsuGenStatusifIndex_Object = MibTableColumn
mcmT1CsuGenStatusifIndex = _McmT1CsuGenStatusifIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 1),
    _McmT1CsuGenStatusifIndex_Type()
)
mcmT1CsuGenStatusifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusifIndex.setStatus("mandatory")


class _McmT1CsuGenStatusLineStatus_Type(Integer32):
    """Custom type mcmT1CsuGenStatusLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmMode", 2),
          ("operational", 1),
          ("testMode", 3))
    )


_McmT1CsuGenStatusLineStatus_Type.__name__ = "Integer32"
_McmT1CsuGenStatusLineStatus_Object = MibTableColumn
mcmT1CsuGenStatusLineStatus = _McmT1CsuGenStatusLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 2),
    _McmT1CsuGenStatusLineStatus_Type()
)
mcmT1CsuGenStatusLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusLineStatus.setStatus("mandatory")


class _McmT1CsuGenStatusRedAlarm_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRedAlarm", 2),
          ("redAlarm", 1))
    )


_McmT1CsuGenStatusRedAlarm_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRedAlarm_Object = MibTableColumn
mcmT1CsuGenStatusRedAlarm = _McmT1CsuGenStatusRedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 3),
    _McmT1CsuGenStatusRedAlarm_Type()
)
mcmT1CsuGenStatusRedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRedAlarm.setStatus("mandatory")


class _McmT1CsuGenStatusYellowAlarm_Type(Integer32):
    """Custom type mcmT1CsuGenStatusYellowAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noYellowAlarm", 2),
          ("yellowAlarm", 1))
    )


_McmT1CsuGenStatusYellowAlarm_Type.__name__ = "Integer32"
_McmT1CsuGenStatusYellowAlarm_Object = MibTableColumn
mcmT1CsuGenStatusYellowAlarm = _McmT1CsuGenStatusYellowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 4),
    _McmT1CsuGenStatusYellowAlarm_Type()
)
mcmT1CsuGenStatusYellowAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusYellowAlarm.setStatus("mandatory")


class _McmT1CsuGenStatusBlueAlarm_Type(Integer32):
    """Custom type mcmT1CsuGenStatusBlueAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blueAlarm", 1),
          ("noBlueAlarm", 2))
    )


_McmT1CsuGenStatusBlueAlarm_Type.__name__ = "Integer32"
_McmT1CsuGenStatusBlueAlarm_Object = MibTableColumn
mcmT1CsuGenStatusBlueAlarm = _McmT1CsuGenStatusBlueAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 5),
    _McmT1CsuGenStatusBlueAlarm_Type()
)
mcmT1CsuGenStatusBlueAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusBlueAlarm.setStatus("mandatory")


class _McmT1CsuGenStatusRxLevel_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxLevel based on Integer32"""
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
        *(("lessThan-neg22pt5db", 4),
          ("neg15db-to-neg22pt5db", 3),
          ("neg7pt5db-to-neg15db", 2),
          ("plus2db-to-neg7pt5db", 1))
    )


_McmT1CsuGenStatusRxLevel_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxLevel_Object = MibTableColumn
mcmT1CsuGenStatusRxLevel = _McmT1CsuGenStatusRxLevel_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 6),
    _McmT1CsuGenStatusRxLevel_Type()
)
mcmT1CsuGenStatusRxLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxLevel.setStatus("mandatory")


class _McmT1CsuGenStatusRxElasStrFull_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxElasStrFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmT1CsuGenStatusRxElasStrFull_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxElasStrFull_Object = MibTableColumn
mcmT1CsuGenStatusRxElasStrFull = _McmT1CsuGenStatusRxElasStrFull_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 7),
    _McmT1CsuGenStatusRxElasStrFull_Type()
)
mcmT1CsuGenStatusRxElasStrFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxElasStrFull.setStatus("mandatory")


class _McmT1CsuGenStatusRxElasStrEmpty_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxElasStrEmpty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmT1CsuGenStatusRxElasStrEmpty_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxElasStrEmpty_Object = MibTableColumn
mcmT1CsuGenStatusRxElasStrEmpty = _McmT1CsuGenStatusRxElasStrEmpty_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 8),
    _McmT1CsuGenStatusRxElasStrEmpty_Type()
)
mcmT1CsuGenStatusRxElasStrEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxElasStrEmpty.setStatus("mandatory")


class _McmT1CsuGenStatusRxPlsDensViolate_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxPlsDensViolate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmT1CsuGenStatusRxPlsDensViolate_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxPlsDensViolate_Object = MibTableColumn
mcmT1CsuGenStatusRxPlsDensViolate = _McmT1CsuGenStatusRxPlsDensViolate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 9),
    _McmT1CsuGenStatusRxPlsDensViolate_Type()
)
mcmT1CsuGenStatusRxPlsDensViolate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxPlsDensViolate.setStatus("mandatory")


class _McmT1CsuGenStatusTxPlsDensViolate_Type(Integer32):
    """Custom type mcmT1CsuGenStatusTxPlsDensViolate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmT1CsuGenStatusTxPlsDensViolate_Type.__name__ = "Integer32"
_McmT1CsuGenStatusTxPlsDensViolate_Object = MibTableColumn
mcmT1CsuGenStatusTxPlsDensViolate = _McmT1CsuGenStatusTxPlsDensViolate_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 10),
    _McmT1CsuGenStatusTxPlsDensViolate_Type()
)
mcmT1CsuGenStatusTxPlsDensViolate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusTxPlsDensViolate.setStatus("mandatory")


class _McmT1CsuGenStatusRxCarrierLoss_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxCarrierLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmT1CsuGenStatusRxCarrierLoss_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxCarrierLoss_Object = MibTableColumn
mcmT1CsuGenStatusRxCarrierLoss = _McmT1CsuGenStatusRxCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 11),
    _McmT1CsuGenStatusRxCarrierLoss_Type()
)
mcmT1CsuGenStatusRxCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxCarrierLoss.setStatus("mandatory")


class _McmT1CsuGenStatusRxSyncLoss_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxSyncLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmT1CsuGenStatusRxSyncLoss_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxSyncLoss_Object = MibTableColumn
mcmT1CsuGenStatusRxSyncLoss = _McmT1CsuGenStatusRxSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 12),
    _McmT1CsuGenStatusRxSyncLoss_Type()
)
mcmT1CsuGenStatusRxSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxSyncLoss.setStatus("mandatory")


class _McmT1CsuGenStatusLnCdViolations_Type(Integer32):
    """Custom type mcmT1CsuGenStatusLnCdViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmT1CsuGenStatusLnCdViolations_Type.__name__ = "Integer32"
_McmT1CsuGenStatusLnCdViolations_Object = MibTableColumn
mcmT1CsuGenStatusLnCdViolations = _McmT1CsuGenStatusLnCdViolations_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 13),
    _McmT1CsuGenStatusLnCdViolations_Type()
)
mcmT1CsuGenStatusLnCdViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusLnCdViolations.setStatus("mandatory")


class _McmT1CsuGenStatusRxLoopUpCdDetect_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxLoopUpCdDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmT1CsuGenStatusRxLoopUpCdDetect_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxLoopUpCdDetect_Object = MibTableColumn
mcmT1CsuGenStatusRxLoopUpCdDetect = _McmT1CsuGenStatusRxLoopUpCdDetect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 14),
    _McmT1CsuGenStatusRxLoopUpCdDetect_Type()
)
mcmT1CsuGenStatusRxLoopUpCdDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxLoopUpCdDetect.setStatus("mandatory")


class _McmT1CsuGenStatusRxLoopDnCdDetect_Type(Integer32):
    """Custom type mcmT1CsuGenStatusRxLoopDnCdDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmT1CsuGenStatusRxLoopDnCdDetect_Type.__name__ = "Integer32"
_McmT1CsuGenStatusRxLoopDnCdDetect_Object = MibTableColumn
mcmT1CsuGenStatusRxLoopDnCdDetect = _McmT1CsuGenStatusRxLoopDnCdDetect_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 2, 1, 15),
    _McmT1CsuGenStatusRxLoopDnCdDetect_Type()
)
mcmT1CsuGenStatusRxLoopDnCdDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmT1CsuGenStatusRxLoopDnCdDetect.setStatus("mandatory")
_McmE1CsuGenStatusTable_Object = MibTable
mcmE1CsuGenStatusTable = _McmE1CsuGenStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3)
)
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusTable.setStatus("mandatory")
_McmE1CsuGenStatusEntry_Object = MibTableRow
mcmE1CsuGenStatusEntry = _McmE1CsuGenStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1)
)
mcmE1CsuGenStatusEntry.setIndexNames(
    (0, "MICOM-CSU-MIB", "mcmE1CsuGenStatusifIndex"),
)
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusEntry.setStatus("mandatory")


class _McmE1CsuGenStatusifIndex_Type(Integer32):
    """Custom type mcmE1CsuGenStatusifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmE1CsuGenStatusifIndex_Type.__name__ = "Integer32"
_McmE1CsuGenStatusifIndex_Object = MibTableColumn
mcmE1CsuGenStatusifIndex = _McmE1CsuGenStatusifIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 1),
    _McmE1CsuGenStatusifIndex_Type()
)
mcmE1CsuGenStatusifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusifIndex.setStatus("mandatory")


class _McmE1CsuGenStatusLineStatus_Type(Integer32):
    """Custom type mcmE1CsuGenStatusLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("alarmMode", 2),
          ("operational", 1),
          ("testMode", 3))
    )


_McmE1CsuGenStatusLineStatus_Type.__name__ = "Integer32"
_McmE1CsuGenStatusLineStatus_Object = MibTableColumn
mcmE1CsuGenStatusLineStatus = _McmE1CsuGenStatusLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 2),
    _McmE1CsuGenStatusLineStatus_Type()
)
mcmE1CsuGenStatusLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusLineStatus.setStatus("mandatory")


class _McmE1CsuGenStatusRedAlarm_Type(Integer32):
    """Custom type mcmE1CsuGenStatusRedAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRedAlarm", 2),
          ("redAlarm", 1))
    )


_McmE1CsuGenStatusRedAlarm_Type.__name__ = "Integer32"
_McmE1CsuGenStatusRedAlarm_Object = MibTableColumn
mcmE1CsuGenStatusRedAlarm = _McmE1CsuGenStatusRedAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 3),
    _McmE1CsuGenStatusRedAlarm_Type()
)
mcmE1CsuGenStatusRedAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusRedAlarm.setStatus("mandatory")


class _McmE1CsuGenStatusRemoteAlarm_Type(Integer32):
    """Custom type mcmE1CsuGenStatusRemoteAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRemoteAlarm", 2),
          ("remoteAlarm", 1))
    )


_McmE1CsuGenStatusRemoteAlarm_Type.__name__ = "Integer32"
_McmE1CsuGenStatusRemoteAlarm_Object = MibTableColumn
mcmE1CsuGenStatusRemoteAlarm = _McmE1CsuGenStatusRemoteAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 4),
    _McmE1CsuGenStatusRemoteAlarm_Type()
)
mcmE1CsuGenStatusRemoteAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusRemoteAlarm.setStatus("mandatory")


class _McmE1CsuGenStatusAISAlarm_Type(Integer32):
    """Custom type mcmE1CsuGenStatusAISAlarm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aisAlarm", 1),
          ("noAISAlarm", 2))
    )


_McmE1CsuGenStatusAISAlarm_Type.__name__ = "Integer32"
_McmE1CsuGenStatusAISAlarm_Object = MibTableColumn
mcmE1CsuGenStatusAISAlarm = _McmE1CsuGenStatusAISAlarm_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 5),
    _McmE1CsuGenStatusAISAlarm_Type()
)
mcmE1CsuGenStatusAISAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusAISAlarm.setStatus("mandatory")


class _McmE1CsuGenStatusRxCarrierLoss_Type(Integer32):
    """Custom type mcmE1CsuGenStatusRxCarrierLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmE1CsuGenStatusRxCarrierLoss_Type.__name__ = "Integer32"
_McmE1CsuGenStatusRxCarrierLoss_Object = MibTableColumn
mcmE1CsuGenStatusRxCarrierLoss = _McmE1CsuGenStatusRxCarrierLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 6),
    _McmE1CsuGenStatusRxCarrierLoss_Type()
)
mcmE1CsuGenStatusRxCarrierLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusRxCarrierLoss.setStatus("mandatory")


class _McmE1CsuGenStatusRxSyncLoss_Type(Integer32):
    """Custom type mcmE1CsuGenStatusRxSyncLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmE1CsuGenStatusRxSyncLoss_Type.__name__ = "Integer32"
_McmE1CsuGenStatusRxSyncLoss_Object = MibTableColumn
mcmE1CsuGenStatusRxSyncLoss = _McmE1CsuGenStatusRxSyncLoss_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 7),
    _McmE1CsuGenStatusRxSyncLoss_Type()
)
mcmE1CsuGenStatusRxSyncLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusRxSyncLoss.setStatus("mandatory")


class _McmE1CsuGenStatusTxElasStrFull_Type(Integer32):
    """Custom type mcmE1CsuGenStatusTxElasStrFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmE1CsuGenStatusTxElasStrFull_Type.__name__ = "Integer32"
_McmE1CsuGenStatusTxElasStrFull_Object = MibTableColumn
mcmE1CsuGenStatusTxElasStrFull = _McmE1CsuGenStatusTxElasStrFull_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 8),
    _McmE1CsuGenStatusTxElasStrFull_Type()
)
mcmE1CsuGenStatusTxElasStrFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusTxElasStrFull.setStatus("mandatory")


class _McmE1CsuGenStatusTxElasStrEmpty_Type(Integer32):
    """Custom type mcmE1CsuGenStatusTxElasStrEmpty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmE1CsuGenStatusTxElasStrEmpty_Type.__name__ = "Integer32"
_McmE1CsuGenStatusTxElasStrEmpty_Object = MibTableColumn
mcmE1CsuGenStatusTxElasStrEmpty = _McmE1CsuGenStatusTxElasStrEmpty_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 9),
    _McmE1CsuGenStatusTxElasStrEmpty_Type()
)
mcmE1CsuGenStatusTxElasStrEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusTxElasStrEmpty.setStatus("mandatory")


class _McmE1CsuGenStatusRxElasStrFull_Type(Integer32):
    """Custom type mcmE1CsuGenStatusRxElasStrFull based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmE1CsuGenStatusRxElasStrFull_Type.__name__ = "Integer32"
_McmE1CsuGenStatusRxElasStrFull_Object = MibTableColumn
mcmE1CsuGenStatusRxElasStrFull = _McmE1CsuGenStatusRxElasStrFull_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 10),
    _McmE1CsuGenStatusRxElasStrFull_Type()
)
mcmE1CsuGenStatusRxElasStrFull.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusRxElasStrFull.setStatus("mandatory")


class _McmE1CsuGenStatusRxElasStrEmpty_Type(Integer32):
    """Custom type mcmE1CsuGenStatusRxElasStrEmpty based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmE1CsuGenStatusRxElasStrEmpty_Type.__name__ = "Integer32"
_McmE1CsuGenStatusRxElasStrEmpty_Object = MibTableColumn
mcmE1CsuGenStatusRxElasStrEmpty = _McmE1CsuGenStatusRxElasStrEmpty_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 11),
    _McmE1CsuGenStatusRxElasStrEmpty_Type()
)
mcmE1CsuGenStatusRxElasStrEmpty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusRxElasStrEmpty.setStatus("mandatory")


class _McmE1CsuGenStatusBpvOrLnCdViolations_Type(Integer32):
    """Custom type mcmE1CsuGenStatusBpvOrLnCdViolations based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_McmE1CsuGenStatusBpvOrLnCdViolations_Type.__name__ = "Integer32"
_McmE1CsuGenStatusBpvOrLnCdViolations_Object = MibTableColumn
mcmE1CsuGenStatusBpvOrLnCdViolations = _McmE1CsuGenStatusBpvOrLnCdViolations_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 12),
    _McmE1CsuGenStatusBpvOrLnCdViolations_Type()
)
mcmE1CsuGenStatusBpvOrLnCdViolations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusBpvOrLnCdViolations.setStatus("mandatory")


class _McmE1CsuGenStatusFASErrors_Type(Integer32):
    """Custom type mcmE1CsuGenStatusFASErrors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_McmE1CsuGenStatusFASErrors_Type.__name__ = "Integer32"
_McmE1CsuGenStatusFASErrors_Object = MibTableColumn
mcmE1CsuGenStatusFASErrors = _McmE1CsuGenStatusFASErrors_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 13),
    _McmE1CsuGenStatusFASErrors_Type()
)
mcmE1CsuGenStatusFASErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusFASErrors.setStatus("mandatory")


class _McmE1CsuGenStatusCRC4Errors_Type(Integer32):
    """Custom type mcmE1CsuGenStatusCRC4Errors based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_McmE1CsuGenStatusCRC4Errors_Type.__name__ = "Integer32"
_McmE1CsuGenStatusCRC4Errors_Object = MibTableColumn
mcmE1CsuGenStatusCRC4Errors = _McmE1CsuGenStatusCRC4Errors_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 3, 1, 14),
    _McmE1CsuGenStatusCRC4Errors_Type()
)
mcmE1CsuGenStatusCRC4Errors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmE1CsuGenStatusCRC4Errors.setStatus("mandatory")
_McmCsuStatusTable_Object = MibTable
mcmCsuStatusTable = _McmCsuStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 4)
)
if mibBuilder.loadTexts:
    mcmCsuStatusTable.setStatus("mandatory")
_McmCsuStatusEntry_Object = MibTableRow
mcmCsuStatusEntry = _McmCsuStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 4, 1)
)
mcmCsuStatusEntry.setIndexNames(
    (0, "MICOM-CSU-MIB", "mcmCsuStatusifIndex"),
)
if mibBuilder.loadTexts:
    mcmCsuStatusEntry.setStatus("mandatory")


class _McmCsuStatusifIndex_Type(Integer32):
    """Custom type mcmCsuStatusifIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_McmCsuStatusifIndex_Type.__name__ = "Integer32"
_McmCsuStatusifIndex_Object = MibTableColumn
mcmCsuStatusifIndex = _McmCsuStatusifIndex_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 4, 1, 1),
    _McmCsuStatusifIndex_Type()
)
mcmCsuStatusifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmCsuStatusifIndex.setStatus("mandatory")


class _McmCsuStatusLineStatus_Type(Integer32):
    """Custom type mcmCsuStatusLineStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkDown", 2),
          ("operational", 1),
          ("testMode", 3))
    )


_McmCsuStatusLineStatus_Type.__name__ = "Integer32"
_McmCsuStatusLineStatus_Object = MibTableColumn
mcmCsuStatusLineStatus = _McmCsuStatusLineStatus_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 4, 1, 2),
    _McmCsuStatusLineStatus_Type()
)
mcmCsuStatusLineStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmCsuStatusLineStatus.setStatus("mandatory")


class _McmCsuStatusRxLossOfSignal_Type(Integer32):
    """Custom type mcmCsuStatusRxLossOfSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmCsuStatusRxLossOfSignal_Type.__name__ = "Integer32"
_McmCsuStatusRxLossOfSignal_Object = MibTableColumn
mcmCsuStatusRxLossOfSignal = _McmCsuStatusRxLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 4, 1, 3),
    _McmCsuStatusRxLossOfSignal_Type()
)
mcmCsuStatusRxLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmCsuStatusRxLossOfSignal.setStatus("mandatory")


class _McmCsuStatusFAWSync_Type(Integer32):
    """Custom type mcmCsuStatusFAWSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmCsuStatusFAWSync_Type.__name__ = "Integer32"
_McmCsuStatusFAWSync_Object = MibTableColumn
mcmCsuStatusFAWSync = _McmCsuStatusFAWSync_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 4, 1, 4),
    _McmCsuStatusFAWSync_Type()
)
mcmCsuStatusFAWSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmCsuStatusFAWSync.setStatus("mandatory")


class _McmCsuStatusLoopPresent_Type(Integer32):
    """Custom type mcmCsuStatusLoopPresent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 1))
    )


_McmCsuStatusLoopPresent_Type.__name__ = "Integer32"
_McmCsuStatusLoopPresent_Object = MibTableColumn
mcmCsuStatusLoopPresent = _McmCsuStatusLoopPresent_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 4, 1, 5),
    _McmCsuStatusLoopPresent_Type()
)
mcmCsuStatusLoopPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmCsuStatusLoopPresent.setStatus("mandatory")


class _McmCsuStatusInsertLossLineLength_Type(Integer32):
    """Custom type mcmCsuStatusInsertLossLineLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15)
        )
    )
    namedValues = NamedValues(
        *(("iL0db-LL0km", 15),
          ("iL13pt6db-LL2pt1km", 13),
          ("iL19pt7db-LL3pt2km", 12),
          ("iL26pt0db-LL4pt2km", 11),
          ("iL32pt3db-LL5pt3km", 10),
          ("iL38pt4db-LL6pt4km", 9),
          ("iL44pt4db-LL7pt5km", 8),
          ("iL50pt5db-LL8pt5km", 7),
          ("iL7pt3db-LL1pt1km", 14))
    )


_McmCsuStatusInsertLossLineLength_Type.__name__ = "Integer32"
_McmCsuStatusInsertLossLineLength_Object = MibTableColumn
mcmCsuStatusInsertLossLineLength = _McmCsuStatusInsertLossLineLength_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 4, 1, 6),
    _McmCsuStatusInsertLossLineLength_Type()
)
mcmCsuStatusInsertLossLineLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmCsuStatusInsertLossLineLength.setStatus("mandatory")


class _McmCsuStatusRxSignalMag_Type(Integer32):
    """Custom type mcmCsuStatusRxSignalMag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmCsuStatusRxSignalMag_Type.__name__ = "Integer32"
_McmCsuStatusRxSignalMag_Object = MibTableColumn
mcmCsuStatusRxSignalMag = _McmCsuStatusRxSignalMag_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 4, 1, 7),
    _McmCsuStatusRxSignalMag_Type()
)
mcmCsuStatusRxSignalMag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmCsuStatusRxSignalMag.setStatus("mandatory")


class _McmCsuStatusInvalidBPVcounts_Type(Integer32):
    """Custom type mcmCsuStatusInvalidBPVcounts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_McmCsuStatusInvalidBPVcounts_Type.__name__ = "Integer32"
_McmCsuStatusInvalidBPVcounts_Object = MibTableColumn
mcmCsuStatusInvalidBPVcounts = _McmCsuStatusInvalidBPVcounts_Object(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 2, 4, 1, 8),
    _McmCsuStatusInvalidBPVcounts_Type()
)
mcmCsuStatusInvalidBPVcounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mcmCsuStatusInvalidBPVcounts.setStatus("mandatory")

# Managed Objects groups


# Notification objects

mcmT1CsuRedAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 1)
)
mcmT1CsuRedAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmT1CsuRedAlarmSet.setStatus(
        ""
    )

mcmT1CsuRedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 2)
)
mcmT1CsuRedAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmT1CsuRedAlarmClear.setStatus(
        ""
    )

mcmT1CsuYellowAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 3)
)
mcmT1CsuYellowAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmT1CsuYellowAlarmSet.setStatus(
        ""
    )

mcmT1CsuYellowAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 4)
)
mcmT1CsuYellowAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmT1CsuYellowAlarmClear.setStatus(
        ""
    )

mcmT1CsuBlueAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 5)
)
mcmT1CsuBlueAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmT1CsuBlueAlarmSet.setStatus(
        ""
    )

mcmT1CsuBlueAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 6)
)
mcmT1CsuBlueAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmT1CsuBlueAlarmClear.setStatus(
        ""
    )

mcmE1CsuRedAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 7)
)
mcmE1CsuRedAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmE1CsuRedAlarmSet.setStatus(
        ""
    )

mcmE1CsuRedAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 8)
)
mcmE1CsuRedAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmE1CsuRedAlarmClear.setStatus(
        ""
    )

mcmE1CsuRemoteAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 9)
)
mcmE1CsuRemoteAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmE1CsuRemoteAlarmSet.setStatus(
        ""
    )

mcmE1CsuRemoteAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 10)
)
mcmE1CsuRemoteAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmE1CsuRemoteAlarmClear.setStatus(
        ""
    )

mcmE1CsuAISAlarmSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 11)
)
mcmE1CsuAISAlarmSet.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmE1CsuAISAlarmSet.setStatus(
        ""
    )

mcmE1CsuAISAlarmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 335, 1, 4, 29, 0, 12)
)
mcmE1CsuAISAlarmClear.setObjects(
      *(("MICOM-SYS-MIB", "mcmSysAsciiTimeOfDay"),
        ("MICOM-CSU-MIB", "mcmT1E1CsuCfgifIndex"))
)
if mibBuilder.loadTexts:
    mcmE1CsuAISAlarmClear.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MICOM-CSU-MIB",
    **{"micom-csu": micom_csu,
       "mcmT1CsuRedAlarmSet": mcmT1CsuRedAlarmSet,
       "mcmT1CsuRedAlarmClear": mcmT1CsuRedAlarmClear,
       "mcmT1CsuYellowAlarmSet": mcmT1CsuYellowAlarmSet,
       "mcmT1CsuYellowAlarmClear": mcmT1CsuYellowAlarmClear,
       "mcmT1CsuBlueAlarmSet": mcmT1CsuBlueAlarmSet,
       "mcmT1CsuBlueAlarmClear": mcmT1CsuBlueAlarmClear,
       "mcmE1CsuRedAlarmSet": mcmE1CsuRedAlarmSet,
       "mcmE1CsuRedAlarmClear": mcmE1CsuRedAlarmClear,
       "mcmE1CsuRemoteAlarmSet": mcmE1CsuRemoteAlarmSet,
       "mcmE1CsuRemoteAlarmClear": mcmE1CsuRemoteAlarmClear,
       "mcmE1CsuAISAlarmSet": mcmE1CsuAISAlarmSet,
       "mcmE1CsuAISAlarmClear": mcmE1CsuAISAlarmClear,
       "csu-configuration": csu_configuration,
       "mcmT1E1CsuCfgTable": mcmT1E1CsuCfgTable,
       "mcmT1E1CsuCfgEntry": mcmT1E1CsuCfgEntry,
       "mcmT1E1CsuCfgifIndex": mcmT1E1CsuCfgifIndex,
       "mcmT1E1CsuCfgLineType": mcmT1E1CsuCfgLineType,
       "mcmT1E1CsuCfgLineSpeed": mcmT1E1CsuCfgLineSpeed,
       "mcmT1E1CsuCfgLineBuildOut": mcmT1E1CsuCfgLineBuildOut,
       "mcmT1E1CsuCfgTxIdleCode": mcmT1E1CsuCfgTxIdleCode,
       "mcmT1E1CsuCfgTxRxClkSource": mcmT1E1CsuCfgTxRxClkSource,
       "mcmT1E1CsuCfgDS0BasicRate": mcmT1E1CsuCfgDS0BasicRate,
       "mcmT1E1CsuCfgLocalLoopback": mcmT1E1CsuCfgLocalLoopback,
       "mcmT1E1CsuCfgRemoteLoopback": mcmT1E1CsuCfgRemoteLoopback,
       "mcmT1E1CsuCfgFramerLoopback": mcmT1E1CsuCfgFramerLoopback,
       "mcmT1E1CsuCfgTrapEnable": mcmT1E1CsuCfgTrapEnable,
       "mcmT1E1CsuCfgFrameFmt": mcmT1E1CsuCfgFrameFmt,
       "mcmT1E1CsuCfgTxRx0CodeSuppress": mcmT1E1CsuCfgTxRx0CodeSuppress,
       "mcmT1E1CsuCfgTxB7ZeroSuppress": mcmT1E1CsuCfgTxB7ZeroSuppress,
       "mcmT1E1CsuCfgPayloadLoopback": mcmT1E1CsuCfgPayloadLoopback,
       "mcmT1E1CsuCfgTransmitLoopUp": mcmT1E1CsuCfgTransmitLoopUp,
       "mcmT1E1CsuCfgTransmitLoopDown": mcmT1E1CsuCfgTransmitLoopDown,
       "mcmT1E1CsuCfgTxRxHDB3": mcmT1E1CsuCfgTxRxHDB3,
       "mcmT1E1CsuCfgTxRxCRC4": mcmT1E1CsuCfgTxRxCRC4,
       "mcmT1E1CsuCfgDS0Connection": mcmT1E1CsuCfgDS0Connection,
       "mcmCsuCfgTable": mcmCsuCfgTable,
       "mcmCsuCfgEntry": mcmCsuCfgEntry,
       "mcmCsuCfgifIndex": mcmCsuCfgifIndex,
       "mcmCsuCfgOperatingMode": mcmCsuCfgOperatingMode,
       "mcmCsuCfgClockingSource": mcmCsuCfgClockingSource,
       "mcmCsuCfgTxOutOfFrame": mcmCsuCfgTxOutOfFrame,
       "mcmCsuCfgTxOutOfService": mcmCsuCfgTxOutOfService,
       "mcmCsuCfgTxControlModeIdle": mcmCsuCfgTxControlModeIdle,
       "mcmCsuCfgZeroSuppressDisable": mcmCsuCfgZeroSuppressDisable,
       "mcmCsuCfgTxIdle": mcmCsuCfgTxIdle,
       "mcmCsuCfgCSULoopback": mcmCsuCfgCSULoopback,
       "mcmCsuCfgFilterForceEnable": mcmCsuCfgFilterForceEnable,
       "mcmCsuCfgFilterForcingCntl": mcmCsuCfgFilterForcingCntl,
       "csu-status": csu_status,
       "mcmT1E1CsuCntlRegStatusTable": mcmT1E1CsuCntlRegStatusTable,
       "mcmT1E1CsuCntlRegStatusEntry": mcmT1E1CsuCntlRegStatusEntry,
       "mcmT1E1CSUStatusifIndex": mcmT1E1CSUStatusifIndex,
       "mcmT1E1CSUStatusCntlReg1": mcmT1E1CSUStatusCntlReg1,
       "mcmT1E1CSUStatusCntlReg2": mcmT1E1CSUStatusCntlReg2,
       "mcmT1E1CSUStatusCntlReg3": mcmT1E1CSUStatusCntlReg3,
       "mcmT1E1CSUStatusCntlReg4": mcmT1E1CSUStatusCntlReg4,
       "mcmT1E1CSUStatusCntlReg5": mcmT1E1CSUStatusCntlReg5,
       "mcmT1E1CSUStatusCntlReg6": mcmT1E1CSUStatusCntlReg6,
       "mcmT1E1CSUStatusCntlReg7": mcmT1E1CSUStatusCntlReg7,
       "mcmT1E1CSUStatusCntlReg8": mcmT1E1CSUStatusCntlReg8,
       "mcmT1E1CSUStatusCntlReg9": mcmT1E1CSUStatusCntlReg9,
       "mcmT1E1CSUStatusCntlReg10": mcmT1E1CSUStatusCntlReg10,
       "mcmT1CsuGenStatusTable": mcmT1CsuGenStatusTable,
       "mcmT1CsuGenStatusEntry": mcmT1CsuGenStatusEntry,
       "mcmT1CsuGenStatusifIndex": mcmT1CsuGenStatusifIndex,
       "mcmT1CsuGenStatusLineStatus": mcmT1CsuGenStatusLineStatus,
       "mcmT1CsuGenStatusRedAlarm": mcmT1CsuGenStatusRedAlarm,
       "mcmT1CsuGenStatusYellowAlarm": mcmT1CsuGenStatusYellowAlarm,
       "mcmT1CsuGenStatusBlueAlarm": mcmT1CsuGenStatusBlueAlarm,
       "mcmT1CsuGenStatusRxLevel": mcmT1CsuGenStatusRxLevel,
       "mcmT1CsuGenStatusRxElasStrFull": mcmT1CsuGenStatusRxElasStrFull,
       "mcmT1CsuGenStatusRxElasStrEmpty": mcmT1CsuGenStatusRxElasStrEmpty,
       "mcmT1CsuGenStatusRxPlsDensViolate": mcmT1CsuGenStatusRxPlsDensViolate,
       "mcmT1CsuGenStatusTxPlsDensViolate": mcmT1CsuGenStatusTxPlsDensViolate,
       "mcmT1CsuGenStatusRxCarrierLoss": mcmT1CsuGenStatusRxCarrierLoss,
       "mcmT1CsuGenStatusRxSyncLoss": mcmT1CsuGenStatusRxSyncLoss,
       "mcmT1CsuGenStatusLnCdViolations": mcmT1CsuGenStatusLnCdViolations,
       "mcmT1CsuGenStatusRxLoopUpCdDetect": mcmT1CsuGenStatusRxLoopUpCdDetect,
       "mcmT1CsuGenStatusRxLoopDnCdDetect": mcmT1CsuGenStatusRxLoopDnCdDetect,
       "mcmE1CsuGenStatusTable": mcmE1CsuGenStatusTable,
       "mcmE1CsuGenStatusEntry": mcmE1CsuGenStatusEntry,
       "mcmE1CsuGenStatusifIndex": mcmE1CsuGenStatusifIndex,
       "mcmE1CsuGenStatusLineStatus": mcmE1CsuGenStatusLineStatus,
       "mcmE1CsuGenStatusRedAlarm": mcmE1CsuGenStatusRedAlarm,
       "mcmE1CsuGenStatusRemoteAlarm": mcmE1CsuGenStatusRemoteAlarm,
       "mcmE1CsuGenStatusAISAlarm": mcmE1CsuGenStatusAISAlarm,
       "mcmE1CsuGenStatusRxCarrierLoss": mcmE1CsuGenStatusRxCarrierLoss,
       "mcmE1CsuGenStatusRxSyncLoss": mcmE1CsuGenStatusRxSyncLoss,
       "mcmE1CsuGenStatusTxElasStrFull": mcmE1CsuGenStatusTxElasStrFull,
       "mcmE1CsuGenStatusTxElasStrEmpty": mcmE1CsuGenStatusTxElasStrEmpty,
       "mcmE1CsuGenStatusRxElasStrFull": mcmE1CsuGenStatusRxElasStrFull,
       "mcmE1CsuGenStatusRxElasStrEmpty": mcmE1CsuGenStatusRxElasStrEmpty,
       "mcmE1CsuGenStatusBpvOrLnCdViolations": mcmE1CsuGenStatusBpvOrLnCdViolations,
       "mcmE1CsuGenStatusFASErrors": mcmE1CsuGenStatusFASErrors,
       "mcmE1CsuGenStatusCRC4Errors": mcmE1CsuGenStatusCRC4Errors,
       "mcmCsuStatusTable": mcmCsuStatusTable,
       "mcmCsuStatusEntry": mcmCsuStatusEntry,
       "mcmCsuStatusifIndex": mcmCsuStatusifIndex,
       "mcmCsuStatusLineStatus": mcmCsuStatusLineStatus,
       "mcmCsuStatusRxLossOfSignal": mcmCsuStatusRxLossOfSignal,
       "mcmCsuStatusFAWSync": mcmCsuStatusFAWSync,
       "mcmCsuStatusLoopPresent": mcmCsuStatusLoopPresent,
       "mcmCsuStatusInsertLossLineLength": mcmCsuStatusInsertLossLineLength,
       "mcmCsuStatusRxSignalMag": mcmCsuStatusRxSignalMag,
       "mcmCsuStatusInvalidBPVcounts": mcmCsuStatusInvalidBPVcounts}
)
