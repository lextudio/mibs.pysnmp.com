# SNMP MIB module (X25W-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/X25W-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:17:39 2024
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
 enterprises,
 experimental,
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
    "enterprises",
    "experimental",
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

_Usr_ObjectIdentity = ObjectIdentity
usr = _Usr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429)
)
_Nas_ObjectIdentity = ObjectIdentity
nas = _Nas_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1)
)
_X25w_ObjectIdentity = ObjectIdentity
x25w = _X25w_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 8)
)
_X25wanAdmn_ObjectIdentity = ObjectIdentity
x25wanAdmn = _X25wanAdmn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 1)
)
_X25wanAdmnTable_Object = MibTable
x25wanAdmnTable = _X25wanAdmnTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 1, 1)
)
if mibBuilder.loadTexts:
    x25wanAdmnTable.setStatus("mandatory")
_X25wanAdmnEntry_Object = MibTableRow
x25wanAdmnEntry = _X25wanAdmnEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 1, 1, 1)
)
x25wanAdmnEntry.setIndexNames(
    (0, "X25W-MIB", "x25wanAdmnIndex"),
)
if mibBuilder.loadTexts:
    x25wanAdmnEntry.setStatus("mandatory")
_X25wanAdmnIndex_Type = Integer32
_X25wanAdmnIndex_Object = MibTableColumn
x25wanAdmnIndex = _X25wanAdmnIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 1, 1, 1, 1),
    _X25wanAdmnIndex_Type()
)
x25wanAdmnIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanAdmnIndex.setStatus("mandatory")


class _X25wanAdmnType_Type(Integer32):
    """Custom type x25wanAdmnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 1),
          ("v35", 2))
    )


_X25wanAdmnType_Type.__name__ = "Integer32"
_X25wanAdmnType_Object = MibTableColumn
x25wanAdmnType = _X25wanAdmnType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 1, 1, 1, 2),
    _X25wanAdmnType_Type()
)
x25wanAdmnType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25wanAdmnType.setStatus("mandatory")


class _X25wanAdmnSpeed_Type(Integer32):
    """Custom type x25wanAdmnSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 393216),
    )


_X25wanAdmnSpeed_Type.__name__ = "Integer32"
_X25wanAdmnSpeed_Object = MibTableColumn
x25wanAdmnSpeed = _X25wanAdmnSpeed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 1, 1, 1, 3),
    _X25wanAdmnSpeed_Type()
)
x25wanAdmnSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25wanAdmnSpeed.setStatus("mandatory")


class _X25wanAdmnLinkAvailable_Type(Integer32):
    """Custom type x25wanAdmnLinkAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcd", 2),
          ("dsr", 1))
    )


_X25wanAdmnLinkAvailable_Type.__name__ = "Integer32"
_X25wanAdmnLinkAvailable_Object = MibTableColumn
x25wanAdmnLinkAvailable = _X25wanAdmnLinkAvailable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 1, 1, 1, 4),
    _X25wanAdmnLinkAvailable_Type()
)
x25wanAdmnLinkAvailable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25wanAdmnLinkAvailable.setStatus("mandatory")


class _X25wanAdmnClockSouce_Type(Integer32):
    """Custom type x25wanAdmnClockSouce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("brgRxTx", 3),
          ("dceRxOnly", 2),
          ("dceRxTx", 1))
    )


_X25wanAdmnClockSouce_Type.__name__ = "Integer32"
_X25wanAdmnClockSouce_Object = MibTableColumn
x25wanAdmnClockSouce = _X25wanAdmnClockSouce_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 1, 1, 1, 5),
    _X25wanAdmnClockSouce_Type()
)
x25wanAdmnClockSouce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25wanAdmnClockSouce.setStatus("mandatory")


class _X25wanAdmnMaxFrmSize_Type(Integer32):
    """Custom type x25wanAdmnMaxFrmSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 519),
    )


_X25wanAdmnMaxFrmSize_Type.__name__ = "Integer32"
_X25wanAdmnMaxFrmSize_Object = MibTableColumn
x25wanAdmnMaxFrmSize = _X25wanAdmnMaxFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 1, 1, 1, 6),
    _X25wanAdmnMaxFrmSize_Type()
)
x25wanAdmnMaxFrmSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25wanAdmnMaxFrmSize.setStatus("mandatory")
_X25wanOper_ObjectIdentity = ObjectIdentity
x25wanOper = _X25wanOper_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 2)
)
_X25wanOperTable_Object = MibTable
x25wanOperTable = _X25wanOperTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 2, 1)
)
if mibBuilder.loadTexts:
    x25wanOperTable.setStatus("mandatory")
_X25wanOperEntry_Object = MibTableRow
x25wanOperEntry = _X25wanOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 2, 1, 1)
)
x25wanOperEntry.setIndexNames(
    (0, "X25W-MIB", "x25wanOperIndex"),
)
if mibBuilder.loadTexts:
    x25wanOperEntry.setStatus("mandatory")
_X25wanOperIndex_Type = Integer32
_X25wanOperIndex_Object = MibTableColumn
x25wanOperIndex = _X25wanOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 2, 1, 1, 1),
    _X25wanOperIndex_Type()
)
x25wanOperIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanOperIndex.setStatus("mandatory")


class _X25wanOperType_Type(Integer32):
    """Custom type x25wanOperType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs232", 1),
          ("v35", 2))
    )


_X25wanOperType_Type.__name__ = "Integer32"
_X25wanOperType_Object = MibTableColumn
x25wanOperType = _X25wanOperType_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 2, 1, 1, 2),
    _X25wanOperType_Type()
)
x25wanOperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanOperType.setStatus("mandatory")


class _X25wanOperSpeed_Type(Integer32):
    """Custom type x25wanOperSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 393216),
    )


_X25wanOperSpeed_Type.__name__ = "Integer32"
_X25wanOperSpeed_Object = MibTableColumn
x25wanOperSpeed = _X25wanOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 2, 1, 1, 3),
    _X25wanOperSpeed_Type()
)
x25wanOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanOperSpeed.setStatus("mandatory")


class _X25wanOperLinkAvailable_Type(Integer32):
    """Custom type x25wanOperLinkAvailable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dcd", 2),
          ("dsr", 1))
    )


_X25wanOperLinkAvailable_Type.__name__ = "Integer32"
_X25wanOperLinkAvailable_Object = MibTableColumn
x25wanOperLinkAvailable = _X25wanOperLinkAvailable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 2, 1, 1, 4),
    _X25wanOperLinkAvailable_Type()
)
x25wanOperLinkAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanOperLinkAvailable.setStatus("mandatory")


class _X25wanOperClockSource_Type(Integer32):
    """Custom type x25wanOperClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("brgRxTx", 3),
          ("dceRxOnly", 2),
          ("dceRxTx", 1))
    )


_X25wanOperClockSource_Type.__name__ = "Integer32"
_X25wanOperClockSource_Object = MibTableColumn
x25wanOperClockSource = _X25wanOperClockSource_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 2, 1, 1, 5),
    _X25wanOperClockSource_Type()
)
x25wanOperClockSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanOperClockSource.setStatus("mandatory")


class _X25wanOperMaxFrmSize_Type(Integer32):
    """Custom type x25wanOperMaxFrmSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 519),
    )


_X25wanOperMaxFrmSize_Type.__name__ = "Integer32"
_X25wanOperMaxFrmSize_Object = MibTableColumn
x25wanOperMaxFrmSize = _X25wanOperMaxFrmSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 2, 1, 1, 6),
    _X25wanOperMaxFrmSize_Type()
)
x25wanOperMaxFrmSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanOperMaxFrmSize.setStatus("mandatory")
_X25wanStats_ObjectIdentity = ObjectIdentity
x25wanStats = _X25wanStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3)
)
_X25wanStatsTable_Object = MibTable
x25wanStatsTable = _X25wanStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1)
)
if mibBuilder.loadTexts:
    x25wanStatsTable.setStatus("mandatory")
_X25wanStatsEntry_Object = MibTableRow
x25wanStatsEntry = _X25wanStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1)
)
x25wanStatsEntry.setIndexNames(
    (0, "X25W-MIB", "x25wanStatsIndex"),
)
if mibBuilder.loadTexts:
    x25wanStatsEntry.setStatus("mandatory")
_X25wanStatsIndex_Type = Integer32
_X25wanStatsIndex_Object = MibTableColumn
x25wanStatsIndex = _X25wanStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 1),
    _X25wanStatsIndex_Type()
)
x25wanStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsIndex.setStatus("mandatory")
_X25wanStatsGoodFramesTxs_Type = Counter32
_X25wanStatsGoodFramesTxs_Object = MibTableColumn
x25wanStatsGoodFramesTxs = _X25wanStatsGoodFramesTxs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 2),
    _X25wanStatsGoodFramesTxs_Type()
)
x25wanStatsGoodFramesTxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsGoodFramesTxs.setStatus("mandatory")
_X25wanStatsGoodFramesRxs_Type = Counter32
_X25wanStatsGoodFramesRxs_Object = MibTableColumn
x25wanStatsGoodFramesRxs = _X25wanStatsGoodFramesRxs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 3),
    _X25wanStatsGoodFramesRxs_Type()
)
x25wanStatsGoodFramesRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsGoodFramesRxs.setStatus("mandatory")
_X25wanStatsTxUnderruns_Type = Counter32
_X25wanStatsTxUnderruns_Object = MibTableColumn
x25wanStatsTxUnderruns = _X25wanStatsTxUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 4),
    _X25wanStatsTxUnderruns_Type()
)
x25wanStatsTxUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsTxUnderruns.setStatus("mandatory")
_X25wanStatsRxOverruns_Type = Counter32
_X25wanStatsRxOverruns_Object = MibTableColumn
x25wanStatsRxOverruns = _X25wanStatsRxOverruns_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 5),
    _X25wanStatsRxOverruns_Type()
)
x25wanStatsRxOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsRxOverruns.setStatus("mandatory")
_X25wanStatsRxCrcErrs_Type = Counter32
_X25wanStatsRxCrcErrs_Object = MibTableColumn
x25wanStatsRxCrcErrs = _X25wanStatsRxCrcErrs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 6),
    _X25wanStatsRxCrcErrs_Type()
)
x25wanStatsRxCrcErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsRxCrcErrs.setStatus("mandatory")
_X25wanStatsRxFrameNoBufs_Type = Counter32
_X25wanStatsRxFrameNoBufs_Object = MibTableColumn
x25wanStatsRxFrameNoBufs = _X25wanStatsRxFrameNoBufs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 7),
    _X25wanStatsRxFrameNoBufs_Type()
)
x25wanStatsRxFrameNoBufs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsRxFrameNoBufs.setStatus("mandatory")
_X25wanStatsUnrecoveredRxs_Type = Counter32
_X25wanStatsUnrecoveredRxs_Object = MibTableColumn
x25wanStatsUnrecoveredRxs = _X25wanStatsUnrecoveredRxs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 8),
    _X25wanStatsUnrecoveredRxs_Type()
)
x25wanStatsUnrecoveredRxs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsUnrecoveredRxs.setStatus("mandatory")
_X25wanStatsRxOverflows_Type = Counter32
_X25wanStatsRxOverflows_Object = MibTableColumn
x25wanStatsRxOverflows = _X25wanStatsRxOverflows_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 9),
    _X25wanStatsRxOverflows_Type()
)
x25wanStatsRxOverflows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsRxOverflows.setStatus("mandatory")
_X25wanStatsRxAborts_Type = Counter32
_X25wanStatsRxAborts_Object = MibTableColumn
x25wanStatsRxAborts = _X25wanStatsRxAborts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 10),
    _X25wanStatsRxAborts_Type()
)
x25wanStatsRxAborts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsRxAborts.setStatus("mandatory")
_X25wanStatsRxTooLongs_Type = Counter32
_X25wanStatsRxTooLongs_Object = MibTableColumn
x25wanStatsRxTooLongs = _X25wanStatsRxTooLongs_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 11),
    _X25wanStatsRxTooLongs_Type()
)
x25wanStatsRxTooLongs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsRxTooLongs.setStatus("mandatory")
_X25wanStatsTxTooShorts_Type = Counter32
_X25wanStatsTxTooShorts_Object = MibTableColumn
x25wanStatsTxTooShorts = _X25wanStatsTxTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 12),
    _X25wanStatsTxTooShorts_Type()
)
x25wanStatsTxTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsTxTooShorts.setStatus("mandatory")
_X25wanStatsRxTooShorts_Type = Counter32
_X25wanStatsRxTooShorts_Object = MibTableColumn
x25wanStatsRxTooShorts = _X25wanStatsRxTooShorts_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 13),
    _X25wanStatsRxTooShorts_Type()
)
x25wanStatsRxTooShorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsRxTooShorts.setStatus("mandatory")
_X25wanStatsTxBadPackets_Type = Counter32
_X25wanStatsTxBadPackets_Object = MibTableColumn
x25wanStatsTxBadPackets = _X25wanStatsTxBadPackets_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 14),
    _X25wanStatsTxBadPackets_Type()
)
x25wanStatsTxBadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsTxBadPackets.setStatus("mandatory")
_X25wanStatsTxRingQFulls_Type = Counter32
_X25wanStatsTxRingQFulls_Object = MibTableColumn
x25wanStatsTxRingQFulls = _X25wanStatsTxRingQFulls_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 15),
    _X25wanStatsTxRingQFulls_Type()
)
x25wanStatsTxRingQFulls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsTxRingQFulls.setStatus("mandatory")
_X25wanStatsRxRingQSize_Type = Integer32
_X25wanStatsRxRingQSize_Object = MibTableColumn
x25wanStatsRxRingQSize = _X25wanStatsRxRingQSize_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 16),
    _X25wanStatsRxRingQSize_Type()
)
x25wanStatsRxRingQSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsRxRingQSize.setStatus("mandatory")


class _X25wanStatsDSR_Type(Integer32):
    """Custom type x25wanStatsDSR based on Integer32"""
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


_X25wanStatsDSR_Type.__name__ = "Integer32"
_X25wanStatsDSR_Object = MibTableColumn
x25wanStatsDSR = _X25wanStatsDSR_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 17),
    _X25wanStatsDSR_Type()
)
x25wanStatsDSR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsDSR.setStatus("mandatory")


class _X25wanStatsCTS_Type(Integer32):
    """Custom type x25wanStatsCTS based on Integer32"""
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


_X25wanStatsCTS_Type.__name__ = "Integer32"
_X25wanStatsCTS_Object = MibTableColumn
x25wanStatsCTS = _X25wanStatsCTS_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 18),
    _X25wanStatsCTS_Type()
)
x25wanStatsCTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsCTS.setStatus("mandatory")


class _X25wanStatsDCD_Type(Integer32):
    """Custom type x25wanStatsDCD based on Integer32"""
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


_X25wanStatsDCD_Type.__name__ = "Integer32"
_X25wanStatsDCD_Object = MibTableColumn
x25wanStatsDCD = _X25wanStatsDCD_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 3, 1, 1, 19),
    _X25wanStatsDCD_Type()
)
x25wanStatsDCD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanStatsDCD.setStatus("mandatory")
_X25wanTrapEna_ObjectIdentity = ObjectIdentity
x25wanTrapEna = _X25wanTrapEna_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 4)
)
_X25wanTrapEnaTable_Object = MibTable
x25wanTrapEnaTable = _X25wanTrapEnaTable_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    x25wanTrapEnaTable.setStatus("mandatory")
_X25wanTrapEnaEntry_Object = MibTableRow
x25wanTrapEnaEntry = _X25wanTrapEnaEntry_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 4, 1, 1)
)
x25wanTrapEnaEntry.setIndexNames(
    (0, "X25W-MIB", "x25wanTrapEnaIndex"),
)
if mibBuilder.loadTexts:
    x25wanTrapEnaEntry.setStatus("mandatory")
_X25wanTrapEnaIndex_Type = Integer32
_X25wanTrapEnaIndex_Object = MibTableColumn
x25wanTrapEnaIndex = _X25wanTrapEnaIndex_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 4, 1, 1, 1),
    _X25wanTrapEnaIndex_Type()
)
x25wanTrapEnaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    x25wanTrapEnaIndex.setStatus("mandatory")


class _X25wanTrapEnaOutOfSvc_Type(Integer32):
    """Custom type x25wanTrapEnaOutOfSvc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_X25wanTrapEnaOutOfSvc_Type.__name__ = "Integer32"
_X25wanTrapEnaOutOfSvc_Object = MibTableColumn
x25wanTrapEnaOutOfSvc = _X25wanTrapEnaOutOfSvc_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 4, 1, 1, 2),
    _X25wanTrapEnaOutOfSvc_Type()
)
x25wanTrapEnaOutOfSvc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25wanTrapEnaOutOfSvc.setStatus("mandatory")


class _X25wanTrapEnaLinkActive_Type(Integer32):
    """Custom type x25wanTrapEnaLinkActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 2),
          ("enable", 1))
    )


_X25wanTrapEnaLinkActive_Type.__name__ = "Integer32"
_X25wanTrapEnaLinkActive_Object = MibTableColumn
x25wanTrapEnaLinkActive = _X25wanTrapEnaLinkActive_Object(
    (1, 3, 6, 1, 4, 1, 429, 1, 8, 4, 1, 1, 3),
    _X25wanTrapEnaLinkActive_Type()
)
x25wanTrapEnaLinkActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    x25wanTrapEnaLinkActive.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "X25W-MIB",
    **{"usr": usr,
       "nas": nas,
       "x25w": x25w,
       "x25wanAdmn": x25wanAdmn,
       "x25wanAdmnTable": x25wanAdmnTable,
       "x25wanAdmnEntry": x25wanAdmnEntry,
       "x25wanAdmnIndex": x25wanAdmnIndex,
       "x25wanAdmnType": x25wanAdmnType,
       "x25wanAdmnSpeed": x25wanAdmnSpeed,
       "x25wanAdmnLinkAvailable": x25wanAdmnLinkAvailable,
       "x25wanAdmnClockSouce": x25wanAdmnClockSouce,
       "x25wanAdmnMaxFrmSize": x25wanAdmnMaxFrmSize,
       "x25wanOper": x25wanOper,
       "x25wanOperTable": x25wanOperTable,
       "x25wanOperEntry": x25wanOperEntry,
       "x25wanOperIndex": x25wanOperIndex,
       "x25wanOperType": x25wanOperType,
       "x25wanOperSpeed": x25wanOperSpeed,
       "x25wanOperLinkAvailable": x25wanOperLinkAvailable,
       "x25wanOperClockSource": x25wanOperClockSource,
       "x25wanOperMaxFrmSize": x25wanOperMaxFrmSize,
       "x25wanStats": x25wanStats,
       "x25wanStatsTable": x25wanStatsTable,
       "x25wanStatsEntry": x25wanStatsEntry,
       "x25wanStatsIndex": x25wanStatsIndex,
       "x25wanStatsGoodFramesTxs": x25wanStatsGoodFramesTxs,
       "x25wanStatsGoodFramesRxs": x25wanStatsGoodFramesRxs,
       "x25wanStatsTxUnderruns": x25wanStatsTxUnderruns,
       "x25wanStatsRxOverruns": x25wanStatsRxOverruns,
       "x25wanStatsRxCrcErrs": x25wanStatsRxCrcErrs,
       "x25wanStatsRxFrameNoBufs": x25wanStatsRxFrameNoBufs,
       "x25wanStatsUnrecoveredRxs": x25wanStatsUnrecoveredRxs,
       "x25wanStatsRxOverflows": x25wanStatsRxOverflows,
       "x25wanStatsRxAborts": x25wanStatsRxAborts,
       "x25wanStatsRxTooLongs": x25wanStatsRxTooLongs,
       "x25wanStatsTxTooShorts": x25wanStatsTxTooShorts,
       "x25wanStatsRxTooShorts": x25wanStatsRxTooShorts,
       "x25wanStatsTxBadPackets": x25wanStatsTxBadPackets,
       "x25wanStatsTxRingQFulls": x25wanStatsTxRingQFulls,
       "x25wanStatsRxRingQSize": x25wanStatsRxRingQSize,
       "x25wanStatsDSR": x25wanStatsDSR,
       "x25wanStatsCTS": x25wanStatsCTS,
       "x25wanStatsDCD": x25wanStatsDCD,
       "x25wanTrapEna": x25wanTrapEna,
       "x25wanTrapEnaTable": x25wanTrapEnaTable,
       "x25wanTrapEnaEntry": x25wanTrapEnaEntry,
       "x25wanTrapEnaIndex": x25wanTrapEnaIndex,
       "x25wanTrapEnaOutOfSvc": x25wanTrapEnaOutOfSvc,
       "x25wanTrapEnaLinkActive": x25wanTrapEnaLinkActive}
)
