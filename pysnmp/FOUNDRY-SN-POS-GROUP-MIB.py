# SNMP MIB module (FOUNDRY-SN-POS-GROUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/FOUNDRY-SN-POS-GROUP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:46:03 2024
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

(router,) = mibBuilder.importSymbols(
    "FOUNDRY-SN-ROOT-MIB",
    "router")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

snPOS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14)
)
snPOS.setRevisions(
        ("2010-06-02 00:00",
         "2009-09-30 00:00")
)


# Types definitions


# TEXTUAL-CONVENTIONS



class POSStatus(Integer32, TextualConvention):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_SnPOSInfo_ObjectIdentity = ObjectIdentity
snPOSInfo = _SnPOSInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1)
)
_SnPOSInfoTable_Object = MibTable
snPOSInfoTable = _SnPOSInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1)
)
if mibBuilder.loadTexts:
    snPOSInfoTable.setStatus("current")
_SnPOSInfoEntry_Object = MibTableRow
snPOSInfoEntry = _SnPOSInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1)
)
snPOSInfoEntry.setIndexNames(
    (0, "FOUNDRY-SN-POS-GROUP-MIB", "snPOSInfoPortNum"),
)
if mibBuilder.loadTexts:
    snPOSInfoEntry.setStatus("current")
_SnPOSInfoPortNum_Type = Integer32
_SnPOSInfoPortNum_Object = MibTableColumn
snPOSInfoPortNum = _SnPOSInfoPortNum_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 1),
    _SnPOSInfoPortNum_Type()
)
snPOSInfoPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSInfoPortNum.setStatus("current")
_SnPOSIfIndex_Type = Integer32
_SnPOSIfIndex_Object = MibTableColumn
snPOSIfIndex = _SnPOSIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 2),
    _SnPOSIfIndex_Type()
)
snPOSIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSIfIndex.setStatus("current")
_SnPOSDescr_Type = DisplayString
_SnPOSDescr_Object = MibTableColumn
snPOSDescr = _SnPOSDescr_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 3),
    _SnPOSDescr_Type()
)
snPOSDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSDescr.setStatus("current")


class _SnPOSName_Type(DisplayString):
    """Custom type snPOSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SnPOSName_Type.__name__ = "DisplayString"
_SnPOSName_Object = MibTableColumn
snPOSName = _SnPOSName_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 4),
    _SnPOSName_Type()
)
snPOSName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSName.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 5),
    _SnPOSInfoSpeed_Type()
)
snPOSInfoSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoSpeed.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 6),
    _SnPOSInfoAdminStatus_Type()
)
snPOSInfoAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoAdminStatus.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 7),
    _SnPOSInfoLinkStatus_Type()
)
snPOSInfoLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSInfoLinkStatus.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 8),
    _SnPOSInfoClock_Type()
)
snPOSInfoClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoClock.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 9),
    _SnPOSInfoLoopBack_Type()
)
snPOSInfoLoopBack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoLoopBack.setStatus("current")
_SnPOSInfoScrambleATM_Type = POSStatus
_SnPOSInfoScrambleATM_Object = MibTableColumn
snPOSInfoScrambleATM = _SnPOSInfoScrambleATM_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 10),
    _SnPOSInfoScrambleATM_Type()
)
snPOSInfoScrambleATM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoScrambleATM.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 11),
    _SnPOSInfoFraming_Type()
)
snPOSInfoFraming.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoFraming.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 12),
    _SnPOSInfoCRC_Type()
)
snPOSInfoCRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoCRC.setStatus("current")


class _SnPOSInfoKeepAlive_Type(Integer32):
    """Custom type snPOSInfoKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_SnPOSInfoKeepAlive_Type.__name__ = "Integer32"
_SnPOSInfoKeepAlive_Object = MibTableColumn
snPOSInfoKeepAlive = _SnPOSInfoKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 13),
    _SnPOSInfoKeepAlive_Type()
)
snPOSInfoKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoKeepAlive.setStatus("current")


class _SnPOSInfoFlagC2_Type(Integer32):
    """Custom type snPOSInfoFlagC2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnPOSInfoFlagC2_Type.__name__ = "Integer32"
_SnPOSInfoFlagC2_Object = MibTableColumn
snPOSInfoFlagC2 = _SnPOSInfoFlagC2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 14),
    _SnPOSInfoFlagC2_Type()
)
snPOSInfoFlagC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoFlagC2.setStatus("current")


class _SnPOSInfoFlagJ0_Type(Integer32):
    """Custom type snPOSInfoFlagJ0 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnPOSInfoFlagJ0_Type.__name__ = "Integer32"
_SnPOSInfoFlagJ0_Object = MibTableColumn
snPOSInfoFlagJ0 = _SnPOSInfoFlagJ0_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 15),
    _SnPOSInfoFlagJ0_Type()
)
snPOSInfoFlagJ0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoFlagJ0.setStatus("current")


class _SnPOSInfoFlagH1_Type(Integer32):
    """Custom type snPOSInfoFlagH1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnPOSInfoFlagH1_Type.__name__ = "Integer32"
_SnPOSInfoFlagH1_Object = MibTableColumn
snPOSInfoFlagH1 = _SnPOSInfoFlagH1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 16),
    _SnPOSInfoFlagH1_Type()
)
snPOSInfoFlagH1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfoFlagH1.setStatus("current")
_SnPOSStatsInFrames_Type = Counter32
_SnPOSStatsInFrames_Object = MibTableColumn
snPOSStatsInFrames = _SnPOSStatsInFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 17),
    _SnPOSStatsInFrames_Type()
)
snPOSStatsInFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsInFrames.setStatus("current")
_SnPOSStatsOutFrames_Type = Counter32
_SnPOSStatsOutFrames_Object = MibTableColumn
snPOSStatsOutFrames = _SnPOSStatsOutFrames_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 18),
    _SnPOSStatsOutFrames_Type()
)
snPOSStatsOutFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsOutFrames.setStatus("current")
_SnPOSStatsAlignErrors_Type = Counter32
_SnPOSStatsAlignErrors_Object = MibTableColumn
snPOSStatsAlignErrors = _SnPOSStatsAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 19),
    _SnPOSStatsAlignErrors_Type()
)
snPOSStatsAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsAlignErrors.setStatus("current")
_SnPOSStatsFCSErrors_Type = Counter32
_SnPOSStatsFCSErrors_Object = MibTableColumn
snPOSStatsFCSErrors = _SnPOSStatsFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 20),
    _SnPOSStatsFCSErrors_Type()
)
snPOSStatsFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsFCSErrors.setStatus("current")
_SnPOSStatsFrameTooLongs_Type = Counter32
_SnPOSStatsFrameTooLongs_Object = MibTableColumn
snPOSStatsFrameTooLongs = _SnPOSStatsFrameTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 21),
    _SnPOSStatsFrameTooLongs_Type()
)
snPOSStatsFrameTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsFrameTooLongs.setStatus("current")
_SnPOSStatsFrameTooShorts_Type = Counter32
_SnPOSStatsFrameTooShorts_Object = MibTableColumn
snPOSStatsFrameTooShorts = _SnPOSStatsFrameTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 22),
    _SnPOSStatsFrameTooShorts_Type()
)
snPOSStatsFrameTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsFrameTooShorts.setStatus("current")
_SnPOSStatsInDiscard_Type = Counter32
_SnPOSStatsInDiscard_Object = MibTableColumn
snPOSStatsInDiscard = _SnPOSStatsInDiscard_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 23),
    _SnPOSStatsInDiscard_Type()
)
snPOSStatsInDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsInDiscard.setStatus("current")
_SnPOSStatsOutDiscard_Type = Counter32
_SnPOSStatsOutDiscard_Object = MibTableColumn
snPOSStatsOutDiscard = _SnPOSStatsOutDiscard_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 24),
    _SnPOSStatsOutDiscard_Type()
)
snPOSStatsOutDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsOutDiscard.setStatus("current")


class _SnPOSInOctets_Type(OctetString):
    """Custom type snPOSInOctets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SnPOSInOctets_Type.__name__ = "OctetString"
_SnPOSInOctets_Object = MibTableColumn
snPOSInOctets = _SnPOSInOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 25),
    _SnPOSInOctets_Type()
)
snPOSInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSInOctets.setStatus("current")


class _SnPOSOutOctets_Type(OctetString):
    """Custom type snPOSOutOctets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )


_SnPOSOutOctets_Type.__name__ = "OctetString"
_SnPOSOutOctets_Object = MibTableColumn
snPOSOutOctets = _SnPOSOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 26),
    _SnPOSOutOctets_Type()
)
snPOSOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSOutOctets.setStatus("current")
_SnPOSStatsInBitsPerSec_Type = Gauge32
_SnPOSStatsInBitsPerSec_Object = MibTableColumn
snPOSStatsInBitsPerSec = _SnPOSStatsInBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 27),
    _SnPOSStatsInBitsPerSec_Type()
)
snPOSStatsInBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsInBitsPerSec.setStatus("current")
_SnPOSStatsOutBitsPerSec_Type = Gauge32
_SnPOSStatsOutBitsPerSec_Object = MibTableColumn
snPOSStatsOutBitsPerSec = _SnPOSStatsOutBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 28),
    _SnPOSStatsOutBitsPerSec_Type()
)
snPOSStatsOutBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsOutBitsPerSec.setStatus("current")
_SnPOSStatsInPktsPerSec_Type = Gauge32
_SnPOSStatsInPktsPerSec_Object = MibTableColumn
snPOSStatsInPktsPerSec = _SnPOSStatsInPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 29),
    _SnPOSStatsInPktsPerSec_Type()
)
snPOSStatsInPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsInPktsPerSec.setStatus("current")
_SnPOSStatsOutPktsPerSec_Type = Gauge32
_SnPOSStatsOutPktsPerSec_Object = MibTableColumn
snPOSStatsOutPktsPerSec = _SnPOSStatsOutPktsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 30),
    _SnPOSStatsOutPktsPerSec_Type()
)
snPOSStatsOutPktsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsOutPktsPerSec.setStatus("current")


class _SnPOSStatsInUtilization_Type(Integer32):
    """Custom type snPOSStatsInUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SnPOSStatsInUtilization_Type.__name__ = "Integer32"
_SnPOSStatsInUtilization_Object = MibTableColumn
snPOSStatsInUtilization = _SnPOSStatsInUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 31),
    _SnPOSStatsInUtilization_Type()
)
snPOSStatsInUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsInUtilization.setStatus("current")


class _SnPOSStatsOutUtilization_Type(Integer32):
    """Custom type snPOSStatsOutUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_SnPOSStatsOutUtilization_Type.__name__ = "Integer32"
_SnPOSStatsOutUtilization_Object = MibTableColumn
snPOSStatsOutUtilization = _SnPOSStatsOutUtilization_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 32),
    _SnPOSStatsOutUtilization_Type()
)
snPOSStatsOutUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsOutUtilization.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 33),
    _SnPOSTagType_Type()
)
snPOSTagType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSTagType.setStatus("current")
_SnPOSStatsB1_Type = Counter32
_SnPOSStatsB1_Object = MibTableColumn
snPOSStatsB1 = _SnPOSStatsB1_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 34),
    _SnPOSStatsB1_Type()
)
snPOSStatsB1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsB1.setStatus("current")
_SnPOSStatsB2_Type = Counter32
_SnPOSStatsB2_Object = MibTableColumn
snPOSStatsB2 = _SnPOSStatsB2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 35),
    _SnPOSStatsB2_Type()
)
snPOSStatsB2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsB2.setStatus("current")
_SnPOSStatsB3_Type = Counter32
_SnPOSStatsB3_Object = MibTableColumn
snPOSStatsB3 = _SnPOSStatsB3_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 36),
    _SnPOSStatsB3_Type()
)
snPOSStatsB3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsB3.setStatus("current")
_SnPOSStatsAIS_Type = Counter32
_SnPOSStatsAIS_Object = MibTableColumn
snPOSStatsAIS = _SnPOSStatsAIS_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 37),
    _SnPOSStatsAIS_Type()
)
snPOSStatsAIS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsAIS.setStatus("current")
_SnPOSStatsRDI_Type = Counter32
_SnPOSStatsRDI_Object = MibTableColumn
snPOSStatsRDI = _SnPOSStatsRDI_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 38),
    _SnPOSStatsRDI_Type()
)
snPOSStatsRDI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsRDI.setStatus("current")
_SnPOSStatsLOP_Type = Counter32
_SnPOSStatsLOP_Object = MibTableColumn
snPOSStatsLOP = _SnPOSStatsLOP_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 39),
    _SnPOSStatsLOP_Type()
)
snPOSStatsLOP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsLOP.setStatus("current")
_SnPOSStatsLOF_Type = Counter32
_SnPOSStatsLOF_Object = MibTableColumn
snPOSStatsLOF = _SnPOSStatsLOF_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 40),
    _SnPOSStatsLOF_Type()
)
snPOSStatsLOF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsLOF.setStatus("current")
_SnPOSStatsLOS_Type = Counter32
_SnPOSStatsLOS_Object = MibTableColumn
snPOSStatsLOS = _SnPOSStatsLOS_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 1, 1, 41),
    _SnPOSStatsLOS_Type()
)
snPOSStatsLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOSStatsLOS.setStatus("current")
_SnPOSInfo2Table_Object = MibTable
snPOSInfo2Table = _SnPOSInfo2Table_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2)
)
if mibBuilder.loadTexts:
    snPOSInfo2Table.setStatus("current")
_SnPOSInfo2Entry_Object = MibTableRow
snPOSInfo2Entry = _SnPOSInfo2Entry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1)
)
snPOSInfo2Entry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    snPOSInfo2Entry.setStatus("current")


class _SnPOSInfo2Clock_Type(Integer32):
    """Custom type snPOSInfo2Clock based on Integer32"""
    defaultValue = 1

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


_SnPOSInfo2Clock_Type.__name__ = "Integer32"
_SnPOSInfo2Clock_Object = MibTableColumn
snPOSInfo2Clock = _SnPOSInfo2Clock_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 1),
    _SnPOSInfo2Clock_Type()
)
snPOSInfo2Clock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2Clock.setStatus("current")


class _SnPOSInfo2ScrambleATM_Type(POSStatus):
    """Custom type snPOSInfo2ScrambleATM based on POSStatus"""


_SnPOSInfo2ScrambleATM_Object = MibTableColumn
snPOSInfo2ScrambleATM = _SnPOSInfo2ScrambleATM_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 2),
    _SnPOSInfo2ScrambleATM_Type()
)
snPOSInfo2ScrambleATM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2ScrambleATM.setStatus("current")


class _SnPOSInfo2CRC_Type(Integer32):
    """Custom type snPOSInfo2CRC based on Integer32"""
    defaultValue = 1

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


_SnPOSInfo2CRC_Type.__name__ = "Integer32"
_SnPOSInfo2CRC_Object = MibTableColumn
snPOSInfo2CRC = _SnPOSInfo2CRC_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 3),
    _SnPOSInfo2CRC_Type()
)
snPOSInfo2CRC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2CRC.setStatus("current")


class _SnPOSInfo2KeepAlive_Type(Unsigned32):
    """Custom type snPOSInfo2KeepAlive based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SnPOSInfo2KeepAlive_Type.__name__ = "Unsigned32"
_SnPOSInfo2KeepAlive_Object = MibTableColumn
snPOSInfo2KeepAlive = _SnPOSInfo2KeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 4),
    _SnPOSInfo2KeepAlive_Type()
)
snPOSInfo2KeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2KeepAlive.setStatus("current")


class _SnPOSInfo2FlagC2_Type(Unsigned32):
    """Custom type snPOSInfo2FlagC2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SnPOSInfo2FlagC2_Type.__name__ = "Unsigned32"
_SnPOSInfo2FlagC2_Object = MibTableColumn
snPOSInfo2FlagC2 = _SnPOSInfo2FlagC2_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 5),
    _SnPOSInfo2FlagC2_Type()
)
snPOSInfo2FlagC2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2FlagC2.setStatus("current")


class _SnPOSInfo2SSM_Type(Integer32):
    """Custom type snPOSInfo2SSM based on Integer32"""
    defaultValue = 2

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
              14)
        )
    )
    namedValues = NamedValues(
        *(("e1SdhDus", 11),
          ("e1SdhSsmLocalG812", 13),
          ("e1SdhSsmPrimaryReferenceClockG811", 12),
          ("e1SdhSsmSyncEquipmentTimingSource", 14),
          ("e1SdhSsmTransitNodeClockG812", 10),
          ("e1SdhTraceabilityUnknown", 9),
          ("t1SonetDus", 8),
          ("t1SonetMinClockTraceable", 7),
          ("t1SonetPrimaryReferenceSource", 1),
          ("t1SonetStratum2Traceable", 3),
          ("t1SonetStratum3Traceable", 6),
          ("t1SonetStratum3eTraceable", 5),
          ("t1SonetTraceabilityUnknown", 2),
          ("t1SonetTransitNodeClock", 4))
    )


_SnPOSInfo2SSM_Type.__name__ = "Integer32"
_SnPOSInfo2SSM_Object = MibTableColumn
snPOSInfo2SSM = _SnPOSInfo2SSM_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 6),
    _SnPOSInfo2SSM_Type()
)
snPOSInfo2SSM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2SSM.setStatus("current")


class _SnPOSInfo2Encapsulation_Type(Integer32):
    """Custom type snPOSInfo2Encapsulation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("hdlc", 2),
          ("ppp", 1))
    )


_SnPOSInfo2Encapsulation_Type.__name__ = "Integer32"
_SnPOSInfo2Encapsulation_Object = MibTableColumn
snPOSInfo2Encapsulation = _SnPOSInfo2Encapsulation_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 7),
    _SnPOSInfo2Encapsulation_Type()
)
snPOSInfo2Encapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2Encapsulation.setStatus("current")


class _SnPOSInfo2AlarmMonitoring_Type(Integer32):
    """Custom type snPOSInfo2AlarmMonitoring based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_SnPOSInfo2AlarmMonitoring_Type.__name__ = "Integer32"
_SnPOSInfo2AlarmMonitoring_Object = MibTableColumn
snPOSInfo2AlarmMonitoring = _SnPOSInfo2AlarmMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 8),
    _SnPOSInfo2AlarmMonitoring_Type()
)
snPOSInfo2AlarmMonitoring.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2AlarmMonitoring.setStatus("current")


class _SnPOSInfo2OverheadJ0ExpectedMessage_Type(OctetString):
    """Custom type snPOSInfo2OverheadJ0ExpectedMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SnPOSInfo2OverheadJ0ExpectedMessage_Type.__name__ = "OctetString"
_SnPOSInfo2OverheadJ0ExpectedMessage_Object = MibTableColumn
snPOSInfo2OverheadJ0ExpectedMessage = _SnPOSInfo2OverheadJ0ExpectedMessage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 9),
    _SnPOSInfo2OverheadJ0ExpectedMessage_Type()
)
snPOSInfo2OverheadJ0ExpectedMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2OverheadJ0ExpectedMessage.setStatus("current")


class _SnPOSInfo2OverheadJ0TransmitMessage_Type(OctetString):
    """Custom type snPOSInfo2OverheadJ0TransmitMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )


_SnPOSInfo2OverheadJ0TransmitMessage_Type.__name__ = "OctetString"
_SnPOSInfo2OverheadJ0TransmitMessage_Object = MibTableColumn
snPOSInfo2OverheadJ0TransmitMessage = _SnPOSInfo2OverheadJ0TransmitMessage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 10),
    _SnPOSInfo2OverheadJ0TransmitMessage_Type()
)
snPOSInfo2OverheadJ0TransmitMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2OverheadJ0TransmitMessage.setStatus("current")


class _SnPOSInfo2OverheadJ1ExpectedMessage_Type(OctetString):
    """Custom type snPOSInfo2OverheadJ1ExpectedMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 64),
    )


_SnPOSInfo2OverheadJ1ExpectedMessage_Type.__name__ = "OctetString"
_SnPOSInfo2OverheadJ1ExpectedMessage_Object = MibTableColumn
snPOSInfo2OverheadJ1ExpectedMessage = _SnPOSInfo2OverheadJ1ExpectedMessage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 11),
    _SnPOSInfo2OverheadJ1ExpectedMessage_Type()
)
snPOSInfo2OverheadJ1ExpectedMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2OverheadJ1ExpectedMessage.setStatus("current")


class _SnPOSInfo2OverheadJ1MessageLength_Type(Integer32):
    """Custom type snPOSInfo2OverheadJ1MessageLength based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              64)
        )
    )
    namedValues = NamedValues(
        *(("s16", 16),
          ("s64", 64))
    )


_SnPOSInfo2OverheadJ1MessageLength_Type.__name__ = "Integer32"
_SnPOSInfo2OverheadJ1MessageLength_Object = MibTableColumn
snPOSInfo2OverheadJ1MessageLength = _SnPOSInfo2OverheadJ1MessageLength_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 12),
    _SnPOSInfo2OverheadJ1MessageLength_Type()
)
snPOSInfo2OverheadJ1MessageLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2OverheadJ1MessageLength.setStatus("current")


class _SnPOSInfo2OverheadJ1TransmitMessage_Type(OctetString):
    """Custom type snPOSInfo2OverheadJ1TransmitMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 64),
    )


_SnPOSInfo2OverheadJ1TransmitMessage_Type.__name__ = "OctetString"
_SnPOSInfo2OverheadJ1TransmitMessage_Object = MibTableColumn
snPOSInfo2OverheadJ1TransmitMessage = _SnPOSInfo2OverheadJ1TransmitMessage_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 2, 1, 13),
    _SnPOSInfo2OverheadJ1TransmitMessage_Type()
)
snPOSInfo2OverheadJ1TransmitMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    snPOSInfo2OverheadJ1TransmitMessage.setStatus("current")
_SnPOSPPPTable_Object = MibTable
snPOSPPPTable = _SnPOSPPPTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 3)
)
if mibBuilder.loadTexts:
    snPOSPPPTable.setStatus("current")
_SnPOSPPPEntry_Object = MibTableRow
snPOSPPPEntry = _SnPOSPPPEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 3, 1)
)
snPOSPPPEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    snPOSPPPEntry.setStatus("current")


class _SnPosPppLcp_Type(DisplayString):
    """Custom type snPosPppLcp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnPosPppLcp_Type.__name__ = "DisplayString"
_SnPosPppLcp_Object = MibTableColumn
snPosPppLcp = _SnPosPppLcp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 3, 1, 1),
    _SnPosPppLcp_Type()
)
snPosPppLcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPosPppLcp.setStatus("current")


class _SnPosPppIpCp_Type(DisplayString):
    """Custom type snPosPppIpCp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnPosPppIpCp_Type.__name__ = "DisplayString"
_SnPosPppIpCp_Object = MibTableColumn
snPosPppIpCp = _SnPosPppIpCp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 3, 1, 2),
    _SnPosPppIpCp_Type()
)
snPosPppIpCp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPosPppIpCp.setStatus("current")


class _SnPosPppIpv6Cp_Type(DisplayString):
    """Custom type snPosPppIpv6Cp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnPosPppIpv6Cp_Type.__name__ = "DisplayString"
_SnPosPppIpv6Cp_Object = MibTableColumn
snPosPppIpv6Cp = _SnPosPppIpv6Cp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 3, 1, 3),
    _SnPosPppIpv6Cp_Type()
)
snPosPppIpv6Cp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPosPppIpv6Cp.setStatus("current")


class _SnPosPppOsInLcp_Type(DisplayString):
    """Custom type snPosPppOsInLcp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnPosPppOsInLcp_Type.__name__ = "DisplayString"
_SnPosPppOsInLcp_Object = MibTableColumn
snPosPppOsInLcp = _SnPosPppOsInLcp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 3, 1, 4),
    _SnPosPppOsInLcp_Type()
)
snPosPppOsInLcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPosPppOsInLcp.setStatus("current")


class _SnPosPppMpLscp_Type(DisplayString):
    """Custom type snPosPppMpLscp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SnPosPppMpLscp_Type.__name__ = "DisplayString"
_SnPosPppMpLscp_Object = MibTableColumn
snPosPppMpLscp = _SnPosPppMpLscp_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 3, 1, 5),
    _SnPosPppMpLscp_Type()
)
snPosPppMpLscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPosPppMpLscp.setStatus("current")
_SnPOScHDLCTable_Object = MibTable
snPOScHDLCTable = _SnPOScHDLCTable_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 4)
)
if mibBuilder.loadTexts:
    snPOScHDLCTable.setStatus("current")
_SnPOScHDLCEntry_Object = MibTableRow
snPOScHDLCEntry = _SnPOScHDLCEntry_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 4, 1)
)
snPOScHDLCEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    snPOScHDLCEntry.setStatus("current")


class _SnPOScHDLCLineState_Type(Integer32):
    """Custom type snPOScHDLCLineState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("unknown", 2),
          ("up", 1))
    )


_SnPOScHDLCLineState_Type.__name__ = "Integer32"
_SnPOScHDLCLineState_Object = MibTableColumn
snPOScHDLCLineState = _SnPOScHDLCLineState_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 4, 1, 1),
    _SnPOScHDLCLineState_Type()
)
snPOScHDLCLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOScHDLCLineState.setStatus("current")


class _SnPOScHDLCInLoopback_Type(Integer32):
    """Custom type snPOScHDLCInLoopback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("unknown", 2),
          ("yes", 1))
    )


_SnPOScHDLCInLoopback_Type.__name__ = "Integer32"
_SnPOScHDLCInLoopback_Object = MibTableColumn
snPOScHDLCInLoopback = _SnPOScHDLCInLoopback_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 4, 1, 2),
    _SnPOScHDLCInLoopback_Type()
)
snPOScHDLCInLoopback.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOScHDLCInLoopback.setStatus("current")
_SnPOScHDLCMySeq_Type = Unsigned32
_SnPOScHDLCMySeq_Object = MibTableColumn
snPOScHDLCMySeq = _SnPOScHDLCMySeq_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 4, 1, 3),
    _SnPOScHDLCMySeq_Type()
)
snPOScHDLCMySeq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOScHDLCMySeq.setStatus("current")
_SnPOScHDLCMySeqSeen_Type = Unsigned32
_SnPOScHDLCMySeqSeen_Object = MibTableColumn
snPOScHDLCMySeqSeen = _SnPOScHDLCMySeqSeen_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 4, 1, 4),
    _SnPOScHDLCMySeqSeen_Type()
)
snPOScHDLCMySeqSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOScHDLCMySeqSeen.setStatus("current")
_SnPOScHDLCPeerSeqSeen_Type = Unsigned32
_SnPOScHDLCPeerSeqSeen_Object = MibTableColumn
snPOScHDLCPeerSeqSeen = _SnPOScHDLCPeerSeqSeen_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 4, 1, 5),
    _SnPOScHDLCPeerSeqSeen_Type()
)
snPOScHDLCPeerSeqSeen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOScHDLCPeerSeqSeen.setStatus("current")
_SnPOScHDLCUniqueSent_Type = Unsigned32
_SnPOScHDLCUniqueSent_Object = MibTableColumn
snPOScHDLCUniqueSent = _SnPOScHDLCUniqueSent_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 4, 1, 6),
    _SnPOScHDLCUniqueSent_Type()
)
snPOScHDLCUniqueSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOScHDLCUniqueSent.setStatus("current")
_SnPOScHDLCUniqueReceived_Type = Unsigned32
_SnPOScHDLCUniqueReceived_Object = MibTableColumn
snPOScHDLCUniqueReceived = _SnPOScHDLCUniqueReceived_Object(
    (1, 3, 6, 1, 4, 1, 1991, 1, 2, 14, 1, 4, 1, 7),
    _SnPOScHDLCUniqueReceived_Type()
)
snPOScHDLCUniqueReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snPOScHDLCUniqueReceived.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FOUNDRY-SN-POS-GROUP-MIB",
    **{"POSStatus": POSStatus,
       "snPOS": snPOS,
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
       "snPOSStatsLOS": snPOSStatsLOS,
       "snPOSInfo2Table": snPOSInfo2Table,
       "snPOSInfo2Entry": snPOSInfo2Entry,
       "snPOSInfo2Clock": snPOSInfo2Clock,
       "snPOSInfo2ScrambleATM": snPOSInfo2ScrambleATM,
       "snPOSInfo2CRC": snPOSInfo2CRC,
       "snPOSInfo2KeepAlive": snPOSInfo2KeepAlive,
       "snPOSInfo2FlagC2": snPOSInfo2FlagC2,
       "snPOSInfo2SSM": snPOSInfo2SSM,
       "snPOSInfo2Encapsulation": snPOSInfo2Encapsulation,
       "snPOSInfo2AlarmMonitoring": snPOSInfo2AlarmMonitoring,
       "snPOSInfo2OverheadJ0ExpectedMessage": snPOSInfo2OverheadJ0ExpectedMessage,
       "snPOSInfo2OverheadJ0TransmitMessage": snPOSInfo2OverheadJ0TransmitMessage,
       "snPOSInfo2OverheadJ1ExpectedMessage": snPOSInfo2OverheadJ1ExpectedMessage,
       "snPOSInfo2OverheadJ1MessageLength": snPOSInfo2OverheadJ1MessageLength,
       "snPOSInfo2OverheadJ1TransmitMessage": snPOSInfo2OverheadJ1TransmitMessage,
       "snPOSPPPTable": snPOSPPPTable,
       "snPOSPPPEntry": snPOSPPPEntry,
       "snPosPppLcp": snPosPppLcp,
       "snPosPppIpCp": snPosPppIpCp,
       "snPosPppIpv6Cp": snPosPppIpv6Cp,
       "snPosPppOsInLcp": snPosPppOsInLcp,
       "snPosPppMpLscp": snPosPppMpLscp,
       "snPOScHDLCTable": snPOScHDLCTable,
       "snPOScHDLCEntry": snPOScHDLCEntry,
       "snPOScHDLCLineState": snPOScHDLCLineState,
       "snPOScHDLCInLoopback": snPOScHDLCInLoopback,
       "snPOScHDLCMySeq": snPOScHDLCMySeq,
       "snPOScHDLCMySeqSeen": snPOScHDLCMySeqSeen,
       "snPOScHDLCPeerSeqSeen": snPOScHDLCPeerSeqSeen,
       "snPOScHDLCUniqueSent": snPOScHDLCUniqueSent,
       "snPOScHDLCUniqueReceived": snPOScHDLCUniqueReceived}
)
