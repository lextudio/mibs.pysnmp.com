# SNMP MIB module (HP-SN-POS-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/HP-SN-MIBS
# Produced by pysmi-1.5.4 at Mon Oct 14 21:58:47 2024
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

(snPOS,) = mibBuilder.importSymbols(
    "HP-SN-ROOT-MIB",
    "snPOS")

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



class POSStatus(Integer32):
    """Custom type POSStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )





class DisplayString(OctetString):
    """Custom type DisplayString based on OctetString"""



# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnPOSInfo_ObjectIdentity = ObjectIdentity
snPOSInfo = _SnPOSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1)
)
_SnPOSInfoTable_Object = MibTable
snPOSInfoTable = _SnPOSInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    snPOSInfoTable.setStatus("mandatory")
_SnPOSInfoEntry_Object = MibTableRow
snPOSInfoEntry = _SnPOSInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1)
)
snPOSInfoEntry.setIndexNames(
    (0, "HP-SN-POS-GROUP-MIB", "snPOSInfoPortNum"),
)
if mibBuilder.loadTexts:
    snPOSInfoEntry.setStatus("mandatory")
_SnPOSInfoPortNum_Type = Integer32
_SnPOSInfoPortNum_Object = MibTableColumn
snPOSInfoPortNum = _SnPOSInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 1),
    _SnPOSInfoPortNum_Type()
)
snPOSInfoPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSInfoPortNum.setStatus("mandatory")
_SnPOSIfIndex_Type = Integer32
_SnPOSIfIndex_Object = MibTableColumn
snPOSIfIndex = _SnPOSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 2),
    _SnPOSIfIndex_Type()
)
snPOSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSIfIndex.setStatus("mandatory")
_SnPOSDescr_Type = DisplayString
_SnPOSDescr_Object = MibTableColumn
snPOSDescr = _SnPOSDescr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 3),
    _SnPOSDescr_Type()
)
snPOSDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSDescr.setStatus("mandatory")


class _SnPOSName_Type(DisplayString):
    """Custom type snPOSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnPOSName_Type.__name__ = "DisplayString"
_SnPOSName_Object = MibTableColumn
snPOSName = _SnPOSName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 4),
    _SnPOSName_Type()
)
snPOSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSName.setStatus("mandatory")


class _SnPOSInfoSpeed_Type(Integer32):
    """Custom type snPOSInfoSpeed based on Integer32"""
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
        *(("other", 3),
          ("s155000", 1),
          ("s2488000", 4),
          ("s622000", 2))
    )


_SnPOSInfoSpeed_Type.__name__ = "Integer32"
_SnPOSInfoSpeed_Object = MibTableColumn
snPOSInfoSpeed = _SnPOSInfoSpeed_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 5),
    _SnPOSInfoSpeed_Type()
)
snPOSInfoSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoSpeed.setStatus("mandatory")


class _SnPOSInfoAdminStatus_Type(Integer32):
    """Custom type snPOSInfoAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_SnPOSInfoAdminStatus_Type.__name__ = "Integer32"
_SnPOSInfoAdminStatus_Object = MibTableColumn
snPOSInfoAdminStatus = _SnPOSInfoAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 6),
    _SnPOSInfoAdminStatus_Type()
)
snPOSInfoAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoAdminStatus.setStatus("mandatory")


class _SnPOSInfoLinkStatus_Type(Integer32):
    """Custom type snPOSInfoLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("testing", 3),
          ("up", 1))
    )


_SnPOSInfoLinkStatus_Type.__name__ = "Integer32"
_SnPOSInfoLinkStatus_Object = MibTableColumn
snPOSInfoLinkStatus = _SnPOSInfoLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 7),
    _SnPOSInfoLinkStatus_Type()
)
snPOSInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSInfoLinkStatus.setStatus("mandatory")


class _SnPOSInfoClock_Type(Integer32):
    """Custom type snPOSInfoClock based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("line", 2))
    )


_SnPOSInfoClock_Type.__name__ = "Integer32"
_SnPOSInfoClock_Object = MibTableColumn
snPOSInfoClock = _SnPOSInfoClock_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 8),
    _SnPOSInfoClock_Type()
)
snPOSInfoClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoClock.setStatus("mandatory")


class _SnPOSInfoLoopBack_Type(Integer32):
    """Custom type snPOSInfoLoopBack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internal", 2),
          ("line", 1),
          ("none", 3))
    )


_SnPOSInfoLoopBack_Type.__name__ = "Integer32"
_SnPOSInfoLoopBack_Object = MibTableColumn
snPOSInfoLoopBack = _SnPOSInfoLoopBack_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 9),
    _SnPOSInfoLoopBack_Type()
)
snPOSInfoLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoLoopBack.setStatus("mandatory")
_SnPOSInfoScrambleATM_Type = POSStatus
_SnPOSInfoScrambleATM_Object = MibTableColumn
snPOSInfoScrambleATM = _SnPOSInfoScrambleATM_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 10),
    _SnPOSInfoScrambleATM_Type()
)
snPOSInfoScrambleATM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoScrambleATM.setStatus("mandatory")


class _SnPOSInfoFraming_Type(Integer32):
    """Custom type snPOSInfoFraming based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sdh", 2),
          ("sonet", 1))
    )


_SnPOSInfoFraming_Type.__name__ = "Integer32"
_SnPOSInfoFraming_Object = MibTableColumn
snPOSInfoFraming = _SnPOSInfoFraming_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 11),
    _SnPOSInfoFraming_Type()
)
snPOSInfoFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoFraming.setStatus("mandatory")


class _SnPOSInfoCRC_Type(Integer32):
    """Custom type snPOSInfoCRC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("crc16bits", 2),
          ("crc32bits", 1))
    )


_SnPOSInfoCRC_Type.__name__ = "Integer32"
_SnPOSInfoCRC_Object = MibTableColumn
snPOSInfoCRC = _SnPOSInfoCRC_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 12),
    _SnPOSInfoCRC_Type()
)
snPOSInfoCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoCRC.setStatus("mandatory")


class _SnPOSInfoKeepAlive_Type(Integer32):
    """Custom type snPOSInfoKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_SnPOSInfoKeepAlive_Type.__name__ = "Integer32"
_SnPOSInfoKeepAlive_Object = MibTableColumn
snPOSInfoKeepAlive = _SnPOSInfoKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 13),
    _SnPOSInfoKeepAlive_Type()
)
snPOSInfoKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoKeepAlive.setStatus("mandatory")


class _SnPOSInfoFlagC2_Type(Integer32):
    """Custom type snPOSInfoFlagC2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnPOSInfoFlagC2_Type.__name__ = "Integer32"
_SnPOSInfoFlagC2_Object = MibTableColumn
snPOSInfoFlagC2 = _SnPOSInfoFlagC2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 14),
    _SnPOSInfoFlagC2_Type()
)
snPOSInfoFlagC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoFlagC2.setStatus("mandatory")


class _SnPOSInfoFlagJ0_Type(Integer32):
    """Custom type snPOSInfoFlagJ0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnPOSInfoFlagJ0_Type.__name__ = "Integer32"
_SnPOSInfoFlagJ0_Object = MibTableColumn
snPOSInfoFlagJ0 = _SnPOSInfoFlagJ0_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 15),
    _SnPOSInfoFlagJ0_Type()
)
snPOSInfoFlagJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoFlagJ0.setStatus("mandatory")


class _SnPOSInfoFlagH1_Type(Integer32):
    """Custom type snPOSInfoFlagH1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnPOSInfoFlagH1_Type.__name__ = "Integer32"
_SnPOSInfoFlagH1_Object = MibTableColumn
snPOSInfoFlagH1 = _SnPOSInfoFlagH1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 16),
    _SnPOSInfoFlagH1_Type()
)
snPOSInfoFlagH1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoFlagH1.setStatus("mandatory")
_SnPOSStatsInFrames_Type = Counter32
_SnPOSStatsInFrames_Object = MibTableColumn
snPOSStatsInFrames = _SnPOSStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 17),
    _SnPOSStatsInFrames_Type()
)
snPOSStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsInFrames.setStatus("mandatory")
_SnPOSStatsOutFrames_Type = Counter32
_SnPOSStatsOutFrames_Object = MibTableColumn
snPOSStatsOutFrames = _SnPOSStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 18),
    _SnPOSStatsOutFrames_Type()
)
snPOSStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsOutFrames.setStatus("mandatory")
_SnPOSStatsAlignErrors_Type = Counter32
_SnPOSStatsAlignErrors_Object = MibTableColumn
snPOSStatsAlignErrors = _SnPOSStatsAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 19),
    _SnPOSStatsAlignErrors_Type()
)
snPOSStatsAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsAlignErrors.setStatus("mandatory")
_SnPOSStatsFCSErrors_Type = Counter32
_SnPOSStatsFCSErrors_Object = MibTableColumn
snPOSStatsFCSErrors = _SnPOSStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 20),
    _SnPOSStatsFCSErrors_Type()
)
snPOSStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsFCSErrors.setStatus("mandatory")
_SnPOSStatsFrameTooLongs_Type = Counter32
_SnPOSStatsFrameTooLongs_Object = MibTableColumn
snPOSStatsFrameTooLongs = _SnPOSStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 21),
    _SnPOSStatsFrameTooLongs_Type()
)
snPOSStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsFrameTooLongs.setStatus("mandatory")
_SnPOSStatsFrameTooShorts_Type = Counter32
_SnPOSStatsFrameTooShorts_Object = MibTableColumn
snPOSStatsFrameTooShorts = _SnPOSStatsFrameTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 22),
    _SnPOSStatsFrameTooShorts_Type()
)
snPOSStatsFrameTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsFrameTooShorts.setStatus("mandatory")
_SnPOSStatsInDiscard_Type = Counter32
_SnPOSStatsInDiscard_Object = MibTableColumn
snPOSStatsInDiscard = _SnPOSStatsInDiscard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 23),
    _SnPOSStatsInDiscard_Type()
)
snPOSStatsInDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsInDiscard.setStatus("mandatory")
_SnPOSStatsOutDiscard_Type = Counter32
_SnPOSStatsOutDiscard_Object = MibTableColumn
snPOSStatsOutDiscard = _SnPOSStatsOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 24),
    _SnPOSStatsOutDiscard_Type()
)
snPOSStatsOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsOutDiscard.setStatus("mandatory")


class _SnPOSInOctets_Type(OctetString):
    """Custom type snPOSInOctets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SnPOSInOctets_Type.__name__ = "OctetString"
_SnPOSInOctets_Object = MibTableColumn
snPOSInOctets = _SnPOSInOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 25),
    _SnPOSInOctets_Type()
)
snPOSInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSInOctets.setStatus("mandatory")


class _SnPOSOutOctets_Type(OctetString):
    """Custom type snPOSOutOctets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SnPOSOutOctets_Type.__name__ = "OctetString"
_SnPOSOutOctets_Object = MibTableColumn
snPOSOutOctets = _SnPOSOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 26),
    _SnPOSOutOctets_Type()
)
snPOSOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSOutOctets.setStatus("mandatory")
_SnPOSStatsInBitsPerSec_Type = Gauge32
_SnPOSStatsInBitsPerSec_Object = MibTableColumn
snPOSStatsInBitsPerSec = _SnPOSStatsInBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 27),
    _SnPOSStatsInBitsPerSec_Type()
)
snPOSStatsInBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsInBitsPerSec.setStatus("mandatory")
_SnPOSStatsOutBitsPerSec_Type = Gauge32
_SnPOSStatsOutBitsPerSec_Object = MibTableColumn
snPOSStatsOutBitsPerSec = _SnPOSStatsOutBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 28),
    _SnPOSStatsOutBitsPerSec_Type()
)
snPOSStatsOutBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsOutBitsPerSec.setStatus("mandatory")
_SnPOSStatsInPktsPerSec_Type = Gauge32
_SnPOSStatsInPktsPerSec_Object = MibTableColumn
snPOSStatsInPktsPerSec = _SnPOSStatsInPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 29),
    _SnPOSStatsInPktsPerSec_Type()
)
snPOSStatsInPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsInPktsPerSec.setStatus("mandatory")
_SnPOSStatsOutPktsPerSec_Type = Gauge32
_SnPOSStatsOutPktsPerSec_Object = MibTableColumn
snPOSStatsOutPktsPerSec = _SnPOSStatsOutPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 30),
    _SnPOSStatsOutPktsPerSec_Type()
)
snPOSStatsOutPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsOutPktsPerSec.setStatus("mandatory")


class _SnPOSStatsInUtilization_Type(Integer32):
    """Custom type snPOSStatsInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SnPOSStatsInUtilization_Type.__name__ = "Integer32"
_SnPOSStatsInUtilization_Object = MibTableColumn
snPOSStatsInUtilization = _SnPOSStatsInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 31),
    _SnPOSStatsInUtilization_Type()
)
snPOSStatsInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsInUtilization.setStatus("mandatory")


class _SnPOSStatsOutUtilization_Type(Integer32):
    """Custom type snPOSStatsOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SnPOSStatsOutUtilization_Type.__name__ = "Integer32"
_SnPOSStatsOutUtilization_Object = MibTableColumn
snPOSStatsOutUtilization = _SnPOSStatsOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 32),
    _SnPOSStatsOutUtilization_Type()
)
snPOSStatsOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsOutUtilization.setStatus("mandatory")


class _SnPOSTagType_Type(Integer32):
    """Custom type snPOSTagType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_SnPOSTagType_Type.__name__ = "Integer32"
_SnPOSTagType_Object = MibTableColumn
snPOSTagType = _SnPOSTagType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 33),
    _SnPOSTagType_Type()
)
snPOSTagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSTagType.setStatus("mandatory")
_SnPOSStatsB1_Type = Counter32
_SnPOSStatsB1_Object = MibTableColumn
snPOSStatsB1 = _SnPOSStatsB1_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 34),
    _SnPOSStatsB1_Type()
)
snPOSStatsB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsB1.setStatus("mandatory")
_SnPOSStatsB2_Type = Counter32
_SnPOSStatsB2_Object = MibTableColumn
snPOSStatsB2 = _SnPOSStatsB2_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 35),
    _SnPOSStatsB2_Type()
)
snPOSStatsB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsB2.setStatus("mandatory")
_SnPOSStatsB3_Type = Counter32
_SnPOSStatsB3_Object = MibTableColumn
snPOSStatsB3 = _SnPOSStatsB3_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 36),
    _SnPOSStatsB3_Type()
)
snPOSStatsB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsB3.setStatus("mandatory")
_SnPOSStatsAIS_Type = Counter32
_SnPOSStatsAIS_Object = MibTableColumn
snPOSStatsAIS = _SnPOSStatsAIS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 37),
    _SnPOSStatsAIS_Type()
)
snPOSStatsAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsAIS.setStatus("mandatory")
_SnPOSStatsRDI_Type = Counter32
_SnPOSStatsRDI_Object = MibTableColumn
snPOSStatsRDI = _SnPOSStatsRDI_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 38),
    _SnPOSStatsRDI_Type()
)
snPOSStatsRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsRDI.setStatus("mandatory")
_SnPOSStatsLOP_Type = Counter32
_SnPOSStatsLOP_Object = MibTableColumn
snPOSStatsLOP = _SnPOSStatsLOP_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 39),
    _SnPOSStatsLOP_Type()
)
snPOSStatsLOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsLOP.setStatus("mandatory")
_SnPOSStatsLOF_Type = Counter32
_SnPOSStatsLOF_Object = MibTableColumn
snPOSStatsLOF = _SnPOSStatsLOF_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 40),
    _SnPOSStatsLOF_Type()
)
snPOSStatsLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsLOF.setStatus("mandatory")
_SnPOSStatsLOS_Type = Counter32
_SnPOSStatsLOS_Object = MibTableColumn
snPOSStatsLOS = _SnPOSStatsLOS_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 14, 1, 1, 1, 41),
    _SnPOSStatsLOS_Type()
)
snPOSStatsLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsLOS.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-SN-POS-GROUP-MIB",
    **{"POSStatus": POSStatus,
       "DisplayString": DisplayString,
       "snPOSInfo": snPOSInfo,
       "snPOSInfoTable": snPOSInfoTable,
       "snPOSInfoEntry": snPOSInfoEntry,
       "snPOSInfoPortNum": snPOSInfoPortNum,
       "snPOSIfIndex": snPOSIfIndex,
       "snPOSDescr": snPOSDescr,
       "snPOSName": snPOSName,
       "snPOSInfoSpeed": snPOSInfoSpeed,
       "snPOSInfoAdminStatus": snPOSInfoAdminStatus,
       "snPOSInfoLinkStatus": snPOSInfoLinkStatus,
       "snPOSInfoClock": snPOSInfoClock,
       "snPOSInfoLoopBack": snPOSInfoLoopBack,
       "snPOSInfoScrambleATM": snPOSInfoScrambleATM,
       "snPOSInfoFraming": snPOSInfoFraming,
       "snPOSInfoCRC": snPOSInfoCRC,
       "snPOSInfoKeepAlive": snPOSInfoKeepAlive,
       "snPOSInfoFlagC2": snPOSInfoFlagC2,
       "snPOSInfoFlagJ0": snPOSInfoFlagJ0,
       "snPOSInfoFlagH1": snPOSInfoFlagH1,
       "snPOSStatsInFrames": snPOSStatsInFrames,
       "snPOSStatsOutFrames": snPOSStatsOutFrames,
       "snPOSStatsAlignErrors": snPOSStatsAlignErrors,
       "snPOSStatsFCSErrors": snPOSStatsFCSErrors,
       "snPOSStatsFrameTooLongs": snPOSStatsFrameTooLongs,
       "snPOSStatsFrameTooShorts": snPOSStatsFrameTooShorts,
       "snPOSStatsInDiscard": snPOSStatsInDiscard,
       "snPOSStatsOutDiscard": snPOSStatsOutDiscard,
       "snPOSInOctets": snPOSInOctets,
       "snPOSOutOctets": snPOSOutOctets,
       "snPOSStatsInBitsPerSec": snPOSStatsInBitsPerSec,
       "snPOSStatsOutBitsPerSec": snPOSStatsOutBitsPerSec,
       "snPOSStatsInPktsPerSec": snPOSStatsInPktsPerSec,
       "snPOSStatsOutPktsPerSec": snPOSStatsOutPktsPerSec,
       "snPOSStatsInUtilization": snPOSStatsInUtilization,
       "snPOSStatsOutUtilization": snPOSStatsOutUtilization,
       "snPOSTagType": snPOSTagType,
       "snPOSStatsB1": snPOSStatsB1,
       "snPOSStatsB2": snPOSStatsB2,
       "snPOSStatsB3": snPOSStatsB3,
       "snPOSStatsAIS": snPOSStatsAIS,
       "snPOSStatsRDI": snPOSStatsRDI,
       "snPOSStatsLOP": snPOSStatsLOP,
       "snPOSStatsLOF": snPOSStatsLOF,
       "snPOSStatsLOS": snPOSStatsLOS}
)
