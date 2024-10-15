# SNMP MIB module (S5-ETHERNET-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/S5-ETHERNET-COMMON-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:49:06 2024
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

(s5EnCfg,
 s5EnStat) = mibBuilder.importSymbols(
    "S5-ETHERNET-MIB",
    "s5EnCfg",
    "s5EnStat")

(AttId,
 SrcIndx,
 TimeIntervalSec) = mibBuilder.importSymbols(
    "S5-TCS-MIB",
    "AttId",
    "SrcIndx",
    "TimeIntervalSec")

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

s5EthernetCommonMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 0)
)
s5EthernetCommonMib.setRevisions(
        ("2004-07-20 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_S5EnPortTable_Object = MibTable
s5EnPortTable = _S5EnPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 1)
)
if mibBuilder.loadTexts:
    s5EnPortTable.setStatus("current")
_S5EnPortEntry_Object = MibTableRow
s5EnPortEntry = _S5EnPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 1, 1)
)
s5EnPortEntry.setIndexNames(
    (0, "S5-ETHERNET-COMMON-MIB", "s5EnPortBrdIndx"),
    (0, "S5-ETHERNET-COMMON-MIB", "s5EnPortIndx"),
)
if mibBuilder.loadTexts:
    s5EnPortEntry.setStatus("current")


class _S5EnPortBrdIndx_Type(Integer32):
    """Custom type s5EnPortBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5EnPortBrdIndx_Type.__name__ = "Integer32"
_S5EnPortBrdIndx_Object = MibTableColumn
s5EnPortBrdIndx = _S5EnPortBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 1, 1, 1),
    _S5EnPortBrdIndx_Type()
)
s5EnPortBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortBrdIndx.setStatus("current")


class _S5EnPortIndx_Type(Integer32):
    """Custom type s5EnPortIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5EnPortIndx_Type.__name__ = "Integer32"
_S5EnPortIndx_Object = MibTableColumn
s5EnPortIndx = _S5EnPortIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 1, 1, 2),
    _S5EnPortIndx_Type()
)
s5EnPortIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortIndx.setStatus("current")


class _S5EnPortPartStatus_Type(Integer32):
    """Custom type s5EnPortPartStatus based on Integer32"""
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
        *(("autoPartition", 4),
          ("enabled", 2),
          ("other", 1),
          ("partition", 3),
          ("timedPartition", 5))
    )


_S5EnPortPartStatus_Type.__name__ = "Integer32"
_S5EnPortPartStatus_Object = MibTableColumn
s5EnPortPartStatus = _S5EnPortPartStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 1, 1, 3),
    _S5EnPortPartStatus_Type()
)
s5EnPortPartStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnPortPartStatus.setStatus("current")
_S5EnPortPartTime_Type = TimeIntervalSec
_S5EnPortPartTime_Object = MibTableColumn
s5EnPortPartTime = _S5EnPortPartTime_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 1, 1, 4),
    _S5EnPortPartTime_Type()
)
s5EnPortPartTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnPortPartTime.setStatus("current")


class _S5EnPortLinkStatus_Type(Integer32):
    """Custom type s5EnPortLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 3),
          ("other", 1))
    )


_S5EnPortLinkStatus_Type.__name__ = "Integer32"
_S5EnPortLinkStatus_Object = MibTableColumn
s5EnPortLinkStatus = _S5EnPortLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 1, 1, 5),
    _S5EnPortLinkStatus_Type()
)
s5EnPortLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortLinkStatus.setStatus("current")


class _S5EnPortJabberStatus_Type(Integer32):
    """Custom type s5EnPortJabberStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("jabbering", 2),
          ("ok", 3),
          ("other", 1))
    )


_S5EnPortJabberStatus_Type.__name__ = "Integer32"
_S5EnPortJabberStatus_Object = MibTableColumn
s5EnPortJabberStatus = _S5EnPortJabberStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 1, 1, 6),
    _S5EnPortJabberStatus_Type()
)
s5EnPortJabberStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortJabberStatus.setStatus("current")
_S5EnPortExtTable_Object = MibTable
s5EnPortExtTable = _S5EnPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3)
)
if mibBuilder.loadTexts:
    s5EnPortExtTable.setStatus("current")
_S5EnPortExtEntry_Object = MibTableRow
s5EnPortExtEntry = _S5EnPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1)
)
s5EnPortExtEntry.setIndexNames(
    (0, "S5-ETHERNET-COMMON-MIB", "s5EnPortExtBrdIndx"),
    (0, "S5-ETHERNET-COMMON-MIB", "s5EnPortExtIndx"),
)
if mibBuilder.loadTexts:
    s5EnPortExtEntry.setStatus("current")


class _S5EnPortExtBrdIndx_Type(Integer32):
    """Custom type s5EnPortExtBrdIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5EnPortExtBrdIndx_Type.__name__ = "Integer32"
_S5EnPortExtBrdIndx_Object = MibTableColumn
s5EnPortExtBrdIndx = _S5EnPortExtBrdIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 1),
    _S5EnPortExtBrdIndx_Type()
)
s5EnPortExtBrdIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortExtBrdIndx.setStatus("current")


class _S5EnPortExtIndx_Type(Integer32):
    """Custom type s5EnPortExtIndx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_S5EnPortExtIndx_Type.__name__ = "Integer32"
_S5EnPortExtIndx_Object = MibTableColumn
s5EnPortExtIndx = _S5EnPortExtIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 2),
    _S5EnPortExtIndx_Type()
)
s5EnPortExtIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortExtIndx.setStatus("current")


class _S5EnPortExtHwCapability_Type(OctetString):
    """Custom type s5EnPortExtHwCapability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_S5EnPortExtHwCapability_Type.__name__ = "OctetString"
_S5EnPortExtHwCapability_Object = MibTableColumn
s5EnPortExtHwCapability = _S5EnPortExtHwCapability_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 3),
    _S5EnPortExtHwCapability_Type()
)
s5EnPortExtHwCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortExtHwCapability.setStatus("current")


class _S5EnPortExtAutoNegAdv_Type(OctetString):
    """Custom type s5EnPortExtAutoNegAdv based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_S5EnPortExtAutoNegAdv_Type.__name__ = "OctetString"
_S5EnPortExtAutoNegAdv_Object = MibTableColumn
s5EnPortExtAutoNegAdv = _S5EnPortExtAutoNegAdv_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 4),
    _S5EnPortExtAutoNegAdv_Type()
)
s5EnPortExtAutoNegAdv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnPortExtAutoNegAdv.setStatus("current")


class _S5EnPortExtAutoNegRcvd_Type(OctetString):
    """Custom type s5EnPortExtAutoNegRcvd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_S5EnPortExtAutoNegRcvd_Type.__name__ = "OctetString"
_S5EnPortExtAutoNegRcvd_Object = MibTableColumn
s5EnPortExtAutoNegRcvd = _S5EnPortExtAutoNegRcvd_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 5),
    _S5EnPortExtAutoNegRcvd_Type()
)
s5EnPortExtAutoNegRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortExtAutoNegRcvd.setStatus("current")
_S5EnPortExt10MbSegAttCfg_Type = AttId
_S5EnPortExt10MbSegAttCfg_Object = MibTableColumn
s5EnPortExt10MbSegAttCfg = _S5EnPortExt10MbSegAttCfg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 6),
    _S5EnPortExt10MbSegAttCfg_Type()
)
s5EnPortExt10MbSegAttCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnPortExt10MbSegAttCfg.setStatus("current")
_S5EnPortExt100MbSegAttCfg_Type = AttId
_S5EnPortExt100MbSegAttCfg_Object = MibTableColumn
s5EnPortExt100MbSegAttCfg = _S5EnPortExt100MbSegAttCfg_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 7),
    _S5EnPortExt100MbSegAttCfg_Type()
)
s5EnPortExt100MbSegAttCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    s5EnPortExt100MbSegAttCfg.setStatus("current")


class _S5EnPortExt10MbSegConnCapability_Type(OctetString):
    """Custom type s5EnPortExt10MbSegConnCapability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_S5EnPortExt10MbSegConnCapability_Type.__name__ = "OctetString"
_S5EnPortExt10MbSegConnCapability_Object = MibTableColumn
s5EnPortExt10MbSegConnCapability = _S5EnPortExt10MbSegConnCapability_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 8),
    _S5EnPortExt10MbSegConnCapability_Type()
)
s5EnPortExt10MbSegConnCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortExt10MbSegConnCapability.setStatus("current")


class _S5EnPortExt100MbSegConnCapability_Type(OctetString):
    """Custom type s5EnPortExt100MbSegConnCapability based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_S5EnPortExt100MbSegConnCapability_Type.__name__ = "OctetString"
_S5EnPortExt100MbSegConnCapability_Object = MibTableColumn
s5EnPortExt100MbSegConnCapability = _S5EnPortExt100MbSegConnCapability_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 9),
    _S5EnPortExt100MbSegConnCapability_Type()
)
s5EnPortExt100MbSegConnCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortExt100MbSegConnCapability.setStatus("current")


class _S5EnPortExtActiveSpeed_Type(Integer32):
    """Custom type s5EnPortExtActiveSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bps100M", 3),
          ("bps10M", 2),
          ("unknown", 1))
    )


_S5EnPortExtActiveSpeed_Type.__name__ = "Integer32"
_S5EnPortExtActiveSpeed_Object = MibTableColumn
s5EnPortExtActiveSpeed = _S5EnPortExtActiveSpeed_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 10),
    _S5EnPortExtActiveSpeed_Type()
)
s5EnPortExtActiveSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortExtActiveSpeed.setStatus("current")


class _S5EnPortExtCurDuplexMode_Type(Integer32):
    """Custom type s5EnPortExtCurDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullDuplex", 3),
          ("halfDuplex", 2),
          ("unknown", 1))
    )


_S5EnPortExtCurDuplexMode_Type.__name__ = "Integer32"
_S5EnPortExtCurDuplexMode_Object = MibTableColumn
s5EnPortExtCurDuplexMode = _S5EnPortExtCurDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 1, 3, 1, 11),
    _S5EnPortExtCurDuplexMode_Type()
)
s5EnPortExtCurDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPortExtCurDuplexMode.setStatus("current")
_S5EnBStatTable_Object = MibTable
s5EnBStatTable = _S5EnBStatTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1)
)
if mibBuilder.loadTexts:
    s5EnBStatTable.setStatus("current")
_S5EnBStatEntry_Object = MibTableRow
s5EnBStatEntry = _S5EnBStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1)
)
s5EnBStatEntry.setIndexNames(
    (0, "S5-ETHERNET-COMMON-MIB", "s5EnBStatSrcIndx"),
)
if mibBuilder.loadTexts:
    s5EnBStatEntry.setStatus("current")
_S5EnBStatSrcIndx_Type = SrcIndx
_S5EnBStatSrcIndx_Object = MibTableColumn
s5EnBStatSrcIndx = _S5EnBStatSrcIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 1),
    _S5EnBStatSrcIndx_Type()
)
s5EnBStatSrcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatSrcIndx.setStatus("current")
_S5EnBStatGoodOctets_Type = Counter32
_S5EnBStatGoodOctets_Object = MibTableColumn
s5EnBStatGoodOctets = _S5EnBStatGoodOctets_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 2),
    _S5EnBStatGoodOctets_Type()
)
s5EnBStatGoodOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatGoodOctets.setStatus("current")
_S5EnBStatGoodFrms_Type = Counter32
_S5EnBStatGoodFrms_Object = MibTableColumn
s5EnBStatGoodFrms = _S5EnBStatGoodFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 3),
    _S5EnBStatGoodFrms_Type()
)
s5EnBStatGoodFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatGoodFrms.setStatus("current")
_S5EnBStatBcastFrms_Type = Counter32
_S5EnBStatBcastFrms_Object = MibTableColumn
s5EnBStatBcastFrms = _S5EnBStatBcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 4),
    _S5EnBStatBcastFrms_Type()
)
s5EnBStatBcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatBcastFrms.setStatus("current")
_S5EnBStatMcastFrms_Type = Counter32
_S5EnBStatMcastFrms_Object = MibTableColumn
s5EnBStatMcastFrms = _S5EnBStatMcastFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 5),
    _S5EnBStatMcastFrms_Type()
)
s5EnBStatMcastFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatMcastFrms.setStatus("current")
_S5EnBStatAlignErrors_Type = Counter32
_S5EnBStatAlignErrors_Object = MibTableColumn
s5EnBStatAlignErrors = _S5EnBStatAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 6),
    _S5EnBStatAlignErrors_Type()
)
s5EnBStatAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatAlignErrors.setStatus("current")
_S5EnBStatFcsErrors_Type = Counter32
_S5EnBStatFcsErrors_Object = MibTableColumn
s5EnBStatFcsErrors = _S5EnBStatFcsErrors_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 7),
    _S5EnBStatFcsErrors_Type()
)
s5EnBStatFcsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatFcsErrors.setStatus("current")
_S5EnBStatRunts_Type = Counter32
_S5EnBStatRunts_Object = MibTableColumn
s5EnBStatRunts = _S5EnBStatRunts_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 8),
    _S5EnBStatRunts_Type()
)
s5EnBStatRunts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatRunts.setStatus("current")
_S5EnBStatTooLongFrms_Type = Counter32
_S5EnBStatTooLongFrms_Object = MibTableColumn
s5EnBStatTooLongFrms = _S5EnBStatTooLongFrms_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 9),
    _S5EnBStatTooLongFrms_Type()
)
s5EnBStatTooLongFrms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatTooLongFrms.setStatus("current")
_S5EnBStatFragments_Type = Counter32
_S5EnBStatFragments_Object = MibTableColumn
s5EnBStatFragments = _S5EnBStatFragments_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 10),
    _S5EnBStatFragments_Type()
)
s5EnBStatFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatFragments.setStatus("current")
_S5EnBStatVeryLongEvents_Type = Counter32
_S5EnBStatVeryLongEvents_Object = MibTableColumn
s5EnBStatVeryLongEvents = _S5EnBStatVeryLongEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 11),
    _S5EnBStatVeryLongEvents_Type()
)
s5EnBStatVeryLongEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatVeryLongEvents.setStatus("current")
_S5EnBStatColls_Type = Counter32
_S5EnBStatColls_Object = MibTableColumn
s5EnBStatColls = _S5EnBStatColls_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 12),
    _S5EnBStatColls_Type()
)
s5EnBStatColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatColls.setStatus("current")
_S5EnBStatLateColls_Type = Counter32
_S5EnBStatLateColls_Object = MibTableColumn
s5EnBStatLateColls = _S5EnBStatLateColls_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 13),
    _S5EnBStatLateColls_Type()
)
s5EnBStatLateColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatLateColls.setStatus("current")
_S5EnBStatShortEvents_Type = Counter32
_S5EnBStatShortEvents_Object = MibTableColumn
s5EnBStatShortEvents = _S5EnBStatShortEvents_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 14),
    _S5EnBStatShortEvents_Type()
)
s5EnBStatShortEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatShortEvents.setStatus("current")
_S5EnBStatRateMismatches_Type = Counter32
_S5EnBStatRateMismatches_Object = MibTableColumn
s5EnBStatRateMismatches = _S5EnBStatRateMismatches_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 15),
    _S5EnBStatRateMismatches_Type()
)
s5EnBStatRateMismatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatRateMismatches.setStatus("current")
_S5EnBStatBackOffFailures_Type = Counter32
_S5EnBStatBackOffFailures_Object = MibTableColumn
s5EnBStatBackOffFailures = _S5EnBStatBackOffFailures_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 16),
    _S5EnBStatBackOffFailures_Type()
)
s5EnBStatBackOffFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatBackOffFailures.setStatus("current")
_S5EnBStatAutoPartitions_Type = Counter32
_S5EnBStatAutoPartitions_Object = MibTableColumn
s5EnBStatAutoPartitions = _S5EnBStatAutoPartitions_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 17),
    _S5EnBStatAutoPartitions_Type()
)
s5EnBStatAutoPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatAutoPartitions.setStatus("current")
_S5EnBStatShortIPGs_Type = Counter32
_S5EnBStatShortIPGs_Object = MibTableColumn
s5EnBStatShortIPGs = _S5EnBStatShortIPGs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 18),
    _S5EnBStatShortIPGs_Type()
)
s5EnBStatShortIPGs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatShortIPGs.setStatus("current")
_S5EnBStatNullFrames_Type = Counter32
_S5EnBStatNullFrames_Object = MibTableColumn
s5EnBStatNullFrames = _S5EnBStatNullFrames_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 1, 1, 19),
    _S5EnBStatNullFrames_Type()
)
s5EnBStatNullFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnBStatNullFrames.setStatus("current")
_S5EnPStatTable_Object = MibTable
s5EnPStatTable = _S5EnPStatTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 2)
)
if mibBuilder.loadTexts:
    s5EnPStatTable.setStatus("current")
_S5EnPStatEntry_Object = MibTableRow
s5EnPStatEntry = _S5EnPStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 2, 1)
)
s5EnPStatEntry.setIndexNames(
    (0, "S5-ETHERNET-COMMON-MIB", "s5EnPStatSrcIndx"),
)
if mibBuilder.loadTexts:
    s5EnPStatEntry.setStatus("current")
_S5EnPStatSrcIndx_Type = SrcIndx
_S5EnPStatSrcIndx_Object = MibTableColumn
s5EnPStatSrcIndx = _S5EnPStatSrcIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 2, 1, 1),
    _S5EnPStatSrcIndx_Type()
)
s5EnPStatSrcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPStatSrcIndx.setStatus("current")
_S5EnPStatSourceAddrChngs_Type = Counter32
_S5EnPStatSourceAddrChngs_Object = MibTableColumn
s5EnPStatSourceAddrChngs = _S5EnPStatSourceAddrChngs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 2, 1, 2),
    _S5EnPStatSourceAddrChngs_Type()
)
s5EnPStatSourceAddrChngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPStatSourceAddrChngs.setStatus("current")
_S5EnPStatLinkStatusChngs_Type = Counter32
_S5EnPStatLinkStatusChngs_Object = MibTableColumn
s5EnPStatLinkStatusChngs = _S5EnPStatLinkStatusChngs_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 2, 1, 3),
    _S5EnPStatLinkStatusChngs_Type()
)
s5EnPStatLinkStatusChngs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPStatLinkStatusChngs.setStatus("current")


class _S5EnPStatLastSourceAddr_Type(OctetString):
    """Custom type s5EnPStatLastSourceAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 6),
    )


_S5EnPStatLastSourceAddr_Type.__name__ = "OctetString"
_S5EnPStatLastSourceAddr_Object = MibTableColumn
s5EnPStatLastSourceAddr = _S5EnPStatLastSourceAddr_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 2, 1, 4),
    _S5EnPStatLastSourceAddr_Type()
)
s5EnPStatLastSourceAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnPStatLastSourceAddr.setStatus("current")
_S5EnSStatTable_Object = MibTable
s5EnSStatTable = _S5EnSStatTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 3)
)
if mibBuilder.loadTexts:
    s5EnSStatTable.setStatus("current")
_S5EnSStatEntry_Object = MibTableRow
s5EnSStatEntry = _S5EnSStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 3, 1)
)
s5EnSStatEntry.setIndexNames(
    (0, "S5-ETHERNET-COMMON-MIB", "s5EnSStatSrcIndx"),
)
if mibBuilder.loadTexts:
    s5EnSStatEntry.setStatus("current")
_S5EnSStatSrcIndx_Type = SrcIndx
_S5EnSStatSrcIndx_Object = MibTableColumn
s5EnSStatSrcIndx = _S5EnSStatSrcIndx_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 3, 1, 1),
    _S5EnSStatSrcIndx_Type()
)
s5EnSStatSrcIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnSStatSrcIndx.setStatus("current")
_S5EnSStatSegColls_Type = Counter32
_S5EnSStatSegColls_Object = MibTableColumn
s5EnSStatSegColls = _S5EnSStatSegColls_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 3, 1, 2),
    _S5EnSStatSegColls_Type()
)
s5EnSStatSegColls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnSStatSegColls.setStatus("current")


class _S5EnSStatSegRate_Type(Integer32):
    """Custom type s5EnSStatSegRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bps100m", 3),
          ("bps10m", 2),
          ("unknown", 1))
    )


_S5EnSStatSegRate_Type.__name__ = "Integer32"
_S5EnSStatSegRate_Object = MibTableColumn
s5EnSStatSegRate = _S5EnSStatSegRate_Object(
    (1, 3, 6, 1, 4, 1, 45, 1, 6, 6, 2, 3, 1, 3),
    _S5EnSStatSegRate_Type()
)
s5EnSStatSegRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    s5EnSStatSegRate.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "S5-ETHERNET-COMMON-MIB",
    **{"s5EthernetCommonMib": s5EthernetCommonMib,
       "s5EnPortTable": s5EnPortTable,
       "s5EnPortEntry": s5EnPortEntry,
       "s5EnPortBrdIndx": s5EnPortBrdIndx,
       "s5EnPortIndx": s5EnPortIndx,
       "s5EnPortPartStatus": s5EnPortPartStatus,
       "s5EnPortPartTime": s5EnPortPartTime,
       "s5EnPortLinkStatus": s5EnPortLinkStatus,
       "s5EnPortJabberStatus": s5EnPortJabberStatus,
       "s5EnPortExtTable": s5EnPortExtTable,
       "s5EnPortExtEntry": s5EnPortExtEntry,
       "s5EnPortExtBrdIndx": s5EnPortExtBrdIndx,
       "s5EnPortExtIndx": s5EnPortExtIndx,
       "s5EnPortExtHwCapability": s5EnPortExtHwCapability,
       "s5EnPortExtAutoNegAdv": s5EnPortExtAutoNegAdv,
       "s5EnPortExtAutoNegRcvd": s5EnPortExtAutoNegRcvd,
       "s5EnPortExt10MbSegAttCfg": s5EnPortExt10MbSegAttCfg,
       "s5EnPortExt100MbSegAttCfg": s5EnPortExt100MbSegAttCfg,
       "s5EnPortExt10MbSegConnCapability": s5EnPortExt10MbSegConnCapability,
       "s5EnPortExt100MbSegConnCapability": s5EnPortExt100MbSegConnCapability,
       "s5EnPortExtActiveSpeed": s5EnPortExtActiveSpeed,
       "s5EnPortExtCurDuplexMode": s5EnPortExtCurDuplexMode,
       "s5EnBStatTable": s5EnBStatTable,
       "s5EnBStatEntry": s5EnBStatEntry,
       "s5EnBStatSrcIndx": s5EnBStatSrcIndx,
       "s5EnBStatGoodOctets": s5EnBStatGoodOctets,
       "s5EnBStatGoodFrms": s5EnBStatGoodFrms,
       "s5EnBStatBcastFrms": s5EnBStatBcastFrms,
       "s5EnBStatMcastFrms": s5EnBStatMcastFrms,
       "s5EnBStatAlignErrors": s5EnBStatAlignErrors,
       "s5EnBStatFcsErrors": s5EnBStatFcsErrors,
       "s5EnBStatRunts": s5EnBStatRunts,
       "s5EnBStatTooLongFrms": s5EnBStatTooLongFrms,
       "s5EnBStatFragments": s5EnBStatFragments,
       "s5EnBStatVeryLongEvents": s5EnBStatVeryLongEvents,
       "s5EnBStatColls": s5EnBStatColls,
       "s5EnBStatLateColls": s5EnBStatLateColls,
       "s5EnBStatShortEvents": s5EnBStatShortEvents,
       "s5EnBStatRateMismatches": s5EnBStatRateMismatches,
       "s5EnBStatBackOffFailures": s5EnBStatBackOffFailures,
       "s5EnBStatAutoPartitions": s5EnBStatAutoPartitions,
       "s5EnBStatShortIPGs": s5EnBStatShortIPGs,
       "s5EnBStatNullFrames": s5EnBStatNullFrames,
       "s5EnPStatTable": s5EnPStatTable,
       "s5EnPStatEntry": s5EnPStatEntry,
       "s5EnPStatSrcIndx": s5EnPStatSrcIndx,
       "s5EnPStatSourceAddrChngs": s5EnPStatSourceAddrChngs,
       "s5EnPStatLinkStatusChngs": s5EnPStatLinkStatusChngs,
       "s5EnPStatLastSourceAddr": s5EnPStatLastSourceAddr,
       "s5EnSStatTable": s5EnSStatTable,
       "s5EnSStatEntry": s5EnSStatEntry,
       "s5EnSStatSrcIndx": s5EnSStatSrcIndx,
       "s5EnSStatSegColls": s5EnSStatSegColls,
       "s5EnSStatSegRate": s5EnSStatSegRate}
)
