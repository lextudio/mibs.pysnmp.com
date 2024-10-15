# SNMP MIB module (AVAYA-RTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/AVAYA-RTP-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:44:33 2024
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

(InetAddress,
 InetAddressIPv6,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressIPv6",
    "InetAddressType",
    "InetPortNumber")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DateAndTime,
 DisplayString,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

avRtpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class AvRtpItuPerceivedSeverity(Integer32, TextualConvention):
    status = "current"
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
        *(("cleared", 1),
          ("critical", 3),
          ("indeterminate", 2),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )



class AvRtpLoss(Integer32, TextualConvention):
    status = "current"
    displayHint = "d-1%"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 1000),
    )



class AvRtpSilenceSupp(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("complex", 4),
          ("disabled", 1),
          ("noRtp", 2),
          ("notSupported", 0),
          ("silenceFrames", 3))
    )



# MIB Managed Objects in the order of their OIDs

_Avaya_ObjectIdentity = ObjectIdentity
avaya = _Avaya_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889)
)
_Mibs_ObjectIdentity = ObjectIdentity
mibs = _Mibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2)
)
_AvRtpNotification_ObjectIdentity = ObjectIdentity
avRtpNotification = _AvRtpNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 0)
)
_AvRtpConfig_ObjectIdentity = ObjectIdentity
avRtpConfig = _AvRtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1)
)
_AvRtpThresholdTable_Object = MibTable
avRtpThresholdTable = _AvRtpThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1)
)
if mibBuilder.loadTexts:
    avRtpThresholdTable.setStatus("current")
_AvRtpThresholdEntry_Object = MibTableRow
avRtpThresholdEntry = _AvRtpThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1)
)
avRtpThresholdEntry.setIndexNames(
    (0, "AVAYA-RTP-MIB", "avRtpThresholdSet"),
)
if mibBuilder.loadTexts:
    avRtpThresholdEntry.setStatus("current")
_AvRtpThresholdSet_Type = Integer32
_AvRtpThresholdSet_Object = MibTableColumn
avRtpThresholdSet = _AvRtpThresholdSet_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 1),
    _AvRtpThresholdSet_Type()
)
avRtpThresholdSet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpThresholdSet.setStatus("current")


class _AvRtpThresholdMinStatWin_Type(Integer32):
    """Custom type avRtpThresholdMinStatWin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AvRtpThresholdMinStatWin_Type.__name__ = "Integer32"
_AvRtpThresholdMinStatWin_Object = MibTableColumn
avRtpThresholdMinStatWin = _AvRtpThresholdMinStatWin_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 2),
    _AvRtpThresholdMinStatWin_Type()
)
avRtpThresholdMinStatWin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdMinStatWin.setStatus("current")
_AvRtpThresholdRxCodecLoss_Type = AvRtpLoss
_AvRtpThresholdRxCodecLoss_Object = MibTableColumn
avRtpThresholdRxCodecLoss = _AvRtpThresholdRxCodecLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 3),
    _AvRtpThresholdRxCodecLoss_Type()
)
avRtpThresholdRxCodecLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRxCodecLoss.setStatus("current")
_AvRtpThresholdRxAvgCodecLoss_Type = AvRtpLoss
_AvRtpThresholdRxAvgCodecLoss_Object = MibTableColumn
avRtpThresholdRxAvgCodecLoss = _AvRtpThresholdRxAvgCodecLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 4),
    _AvRtpThresholdRxAvgCodecLoss_Type()
)
avRtpThresholdRxAvgCodecLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRxAvgCodecLoss.setStatus("current")


class _AvRtpThresholdRxCodecLossEv_Type(Integer32):
    """Custom type avRtpThresholdRxCodecLossEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AvRtpThresholdRxCodecLossEv_Type.__name__ = "Integer32"
_AvRtpThresholdRxCodecLossEv_Object = MibTableColumn
avRtpThresholdRxCodecLossEv = _AvRtpThresholdRxCodecLossEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 5),
    _AvRtpThresholdRxCodecLossEv_Type()
)
avRtpThresholdRxCodecLossEv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRxCodecLossEv.setStatus("current")


class _AvRtpThresholdCodecRtt_Type(Integer32):
    """Custom type avRtpThresholdCodecRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AvRtpThresholdCodecRtt_Type.__name__ = "Integer32"
_AvRtpThresholdCodecRtt_Object = MibTableColumn
avRtpThresholdCodecRtt = _AvRtpThresholdCodecRtt_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 6),
    _AvRtpThresholdCodecRtt_Type()
)
avRtpThresholdCodecRtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdCodecRtt.setStatus("current")


class _AvRtpThresholdCodecRttEv_Type(Integer32):
    """Custom type avRtpThresholdCodecRttEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AvRtpThresholdCodecRttEv_Type.__name__ = "Integer32"
_AvRtpThresholdCodecRttEv_Object = MibTableColumn
avRtpThresholdCodecRttEv = _AvRtpThresholdCodecRttEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 7),
    _AvRtpThresholdCodecRttEv_Type()
)
avRtpThresholdCodecRttEv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdCodecRttEv.setStatus("current")


class _AvRtpThresholdEcReturnLoss_Type(Integer32):
    """Custom type avRtpThresholdEcReturnLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AvRtpThresholdEcReturnLoss_Type.__name__ = "Integer32"
_AvRtpThresholdEcReturnLoss_Object = MibTableColumn
avRtpThresholdEcReturnLoss = _AvRtpThresholdEcReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 8),
    _AvRtpThresholdEcReturnLoss_Type()
)
avRtpThresholdEcReturnLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdEcReturnLoss.setStatus("current")


class _AvRtpThresholdEcReturnLossEv_Type(Integer32):
    """Custom type avRtpThresholdEcReturnLossEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AvRtpThresholdEcReturnLossEv_Type.__name__ = "Integer32"
_AvRtpThresholdEcReturnLossEv_Object = MibTableColumn
avRtpThresholdEcReturnLossEv = _AvRtpThresholdEcReturnLossEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 9),
    _AvRtpThresholdEcReturnLossEv_Type()
)
avRtpThresholdEcReturnLossEv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdEcReturnLossEv.setStatus("current")
_AvRtpThresholdRxLoss_Type = AvRtpLoss
_AvRtpThresholdRxLoss_Object = MibTableColumn
avRtpThresholdRxLoss = _AvRtpThresholdRxLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 10),
    _AvRtpThresholdRxLoss_Type()
)
avRtpThresholdRxLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRxLoss.setStatus("current")


class _AvRtpThresholdRxLossEv_Type(Integer32):
    """Custom type avRtpThresholdRxLossEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AvRtpThresholdRxLossEv_Type.__name__ = "Integer32"
_AvRtpThresholdRxLossEv_Object = MibTableColumn
avRtpThresholdRxLossEv = _AvRtpThresholdRxLossEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 11),
    _AvRtpThresholdRxLossEv_Type()
)
avRtpThresholdRxLossEv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRxLossEv.setStatus("current")
_AvRtpThresholdRemLoss_Type = AvRtpLoss
_AvRtpThresholdRemLoss_Object = MibTableColumn
avRtpThresholdRemLoss = _AvRtpThresholdRemLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 12),
    _AvRtpThresholdRemLoss_Type()
)
avRtpThresholdRemLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRemLoss.setStatus("current")


class _AvRtpThresholdRemLossEv_Type(Integer32):
    """Custom type avRtpThresholdRemLossEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AvRtpThresholdRemLossEv_Type.__name__ = "Integer32"
_AvRtpThresholdRemLossEv_Object = MibTableColumn
avRtpThresholdRemLossEv = _AvRtpThresholdRemLossEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 13),
    _AvRtpThresholdRemLossEv_Type()
)
avRtpThresholdRemLossEv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRemLossEv.setStatus("current")
_AvRtpThresholdAvgRxLoss_Type = AvRtpLoss
_AvRtpThresholdAvgRxLoss_Object = MibTableColumn
avRtpThresholdAvgRxLoss = _AvRtpThresholdAvgRxLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 14),
    _AvRtpThresholdAvgRxLoss_Type()
)
avRtpThresholdAvgRxLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdAvgRxLoss.setStatus("current")
_AvRtpThresholdAvgRemLoss_Type = AvRtpLoss
_AvRtpThresholdAvgRemLoss_Object = MibTableColumn
avRtpThresholdAvgRemLoss = _AvRtpThresholdAvgRemLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 15),
    _AvRtpThresholdAvgRemLoss_Type()
)
avRtpThresholdAvgRemLoss.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdAvgRemLoss.setStatus("current")


class _AvRtpThresholdRxJitter_Type(Integer32):
    """Custom type avRtpThresholdRxJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AvRtpThresholdRxJitter_Type.__name__ = "Integer32"
_AvRtpThresholdRxJitter_Object = MibTableColumn
avRtpThresholdRxJitter = _AvRtpThresholdRxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 16),
    _AvRtpThresholdRxJitter_Type()
)
avRtpThresholdRxJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRxJitter.setStatus("current")


class _AvRtpThresholdRxJitterEv_Type(Integer32):
    """Custom type avRtpThresholdRxJitterEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AvRtpThresholdRxJitterEv_Type.__name__ = "Integer32"
_AvRtpThresholdRxJitterEv_Object = MibTableColumn
avRtpThresholdRxJitterEv = _AvRtpThresholdRxJitterEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 17),
    _AvRtpThresholdRxJitterEv_Type()
)
avRtpThresholdRxJitterEv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRxJitterEv.setStatus("current")


class _AvRtpThresholdRemJitter_Type(Integer32):
    """Custom type avRtpThresholdRemJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AvRtpThresholdRemJitter_Type.__name__ = "Integer32"
_AvRtpThresholdRemJitter_Object = MibTableColumn
avRtpThresholdRemJitter = _AvRtpThresholdRemJitter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 18),
    _AvRtpThresholdRemJitter_Type()
)
avRtpThresholdRemJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRemJitter.setStatus("current")


class _AvRtpThresholdRemJitterEv_Type(Integer32):
    """Custom type avRtpThresholdRemJitterEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AvRtpThresholdRemJitterEv_Type.__name__ = "Integer32"
_AvRtpThresholdRemJitterEv_Object = MibTableColumn
avRtpThresholdRemJitterEv = _AvRtpThresholdRemJitterEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 19),
    _AvRtpThresholdRemJitterEv_Type()
)
avRtpThresholdRemJitterEv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRemJitterEv.setStatus("current")


class _AvRtpThresholdRtt_Type(Integer32):
    """Custom type avRtpThresholdRtt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5000),
    )


_AvRtpThresholdRtt_Type.__name__ = "Integer32"
_AvRtpThresholdRtt_Object = MibTableColumn
avRtpThresholdRtt = _AvRtpThresholdRtt_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 20),
    _AvRtpThresholdRtt_Type()
)
avRtpThresholdRtt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRtt.setStatus("current")


class _AvRtpThresholdRttEv_Type(Integer32):
    """Custom type avRtpThresholdRttEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AvRtpThresholdRttEv_Type.__name__ = "Integer32"
_AvRtpThresholdRttEv_Object = MibTableColumn
avRtpThresholdRttEv = _AvRtpThresholdRttEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 21),
    _AvRtpThresholdRttEv_Type()
)
avRtpThresholdRttEv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRttEv.setStatus("current")


class _AvRtpThresholdRxSsrcChangeEv_Type(Integer32):
    """Custom type avRtpThresholdRxSsrcChangeEv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AvRtpThresholdRxSsrcChangeEv_Type.__name__ = "Integer32"
_AvRtpThresholdRxSsrcChangeEv_Object = MibTableColumn
avRtpThresholdRxSsrcChangeEv = _AvRtpThresholdRxSsrcChangeEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 1, 1, 22),
    _AvRtpThresholdRxSsrcChangeEv_Type()
)
avRtpThresholdRxSsrcChangeEv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpThresholdRxSsrcChangeEv.setStatus("current")
_AvRtpEnable_Type = TruthValue
_AvRtpEnable_Object = MibScalar
avRtpEnable = _AvRtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 2),
    _AvRtpEnable_Type()
)
avRtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpEnable.setStatus("current")
_AvRtpQoSTrapEnable_Type = TruthValue
_AvRtpQoSTrapEnable_Object = MibScalar
avRtpQoSTrapEnable = _AvRtpQoSTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 3),
    _AvRtpQoSTrapEnable_Type()
)
avRtpQoSTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpQoSTrapEnable.setStatus("current")
_AvRtpQoSFaultTrapEnable_Type = TruthValue
_AvRtpQoSFaultTrapEnable_Object = MibScalar
avRtpQoSFaultTrapEnable = _AvRtpQoSFaultTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 4),
    _AvRtpQoSFaultTrapEnable_Type()
)
avRtpQoSFaultTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpQoSFaultTrapEnable.setStatus("current")


class _AvRtpQoSFaultTh_Type(Integer32):
    """Custom type avRtpQoSFaultTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AvRtpQoSFaultTh_Type.__name__ = "Integer32"
_AvRtpQoSFaultTh_Object = MibScalar
avRtpQoSFaultTh = _AvRtpQoSFaultTh_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 5),
    _AvRtpQoSFaultTh_Type()
)
avRtpQoSFaultTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpQoSFaultTh.setStatus("current")


class _AvRtpQoSClearTh_Type(Integer32):
    """Custom type avRtpQoSClearTh based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_AvRtpQoSClearTh_Type.__name__ = "Integer32"
_AvRtpQoSClearTh_Object = MibScalar
avRtpQoSClearTh = _AvRtpQoSClearTh_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 6),
    _AvRtpQoSClearTh_Type()
)
avRtpQoSClearTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpQoSClearTh.setStatus("current")
_AvRtpTxQoSTraps_Type = Counter32
_AvRtpTxQoSTraps_Object = MibScalar
avRtpTxQoSTraps = _AvRtpTxQoSTraps_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 7),
    _AvRtpTxQoSTraps_Type()
)
avRtpTxQoSTraps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpTxQoSTraps.setStatus("current")
_AvRtpQoSTrapsDrop_Type = Counter32
_AvRtpQoSTrapsDrop_Object = MibScalar
avRtpQoSTrapsDrop = _AvRtpQoSTrapsDrop_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 8),
    _AvRtpQoSTrapsDrop_Type()
)
avRtpQoSTrapsDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpQoSTrapsDrop.setStatus("current")


class _AvRtpQoSTrapTokenInterval_Type(TimeInterval):
    """Custom type avRtpQoSTrapTokenInterval based on TimeInterval"""
    defaultValue = 1000

    subtypeSpec = TimeInterval.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 1000000),
    )


_AvRtpQoSTrapTokenInterval_Type.__name__ = "TimeInterval"
_AvRtpQoSTrapTokenInterval_Object = MibScalar
avRtpQoSTrapTokenInterval = _AvRtpQoSTrapTokenInterval_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 9),
    _AvRtpQoSTrapTokenInterval_Type()
)
avRtpQoSTrapTokenInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpQoSTrapTokenInterval.setStatus("current")


class _AvRtpQoSTrapBucketSize_Type(Integer32):
    """Custom type avRtpQoSTrapBucketSize based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_AvRtpQoSTrapBucketSize_Type.__name__ = "Integer32"
_AvRtpQoSTrapBucketSize_Object = MibScalar
avRtpQoSTrapBucketSize = _AvRtpQoSTrapBucketSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 10),
    _AvRtpQoSTrapBucketSize_Type()
)
avRtpQoSTrapBucketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpQoSTrapBucketSize.setStatus("current")
_AvRtpDateAndTime_Type = DateAndTime
_AvRtpDateAndTime_Object = MibScalar
avRtpDateAndTime = _AvRtpDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 11),
    _AvRtpDateAndTime_Type()
)
avRtpDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpDateAndTime.setStatus("current")
_AvRtpMaxSessionTableSize_Type = Integer32
_AvRtpMaxSessionTableSize_Object = MibScalar
avRtpMaxSessionTableSize = _AvRtpMaxSessionTableSize_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 12),
    _AvRtpMaxSessionTableSize_Type()
)
avRtpMaxSessionTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpMaxSessionTableSize.setStatus("current")
_AvRtpReservedSessionTableRows_Type = Integer32
_AvRtpReservedSessionTableRows_Object = MibScalar
avRtpReservedSessionTableRows = _AvRtpReservedSessionTableRows_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 13),
    _AvRtpReservedSessionTableRows_Type()
)
avRtpReservedSessionTableRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpReservedSessionTableRows.setStatus("current")
_AvRtpClear_Type = TruthValue
_AvRtpClear_Object = MibScalar
avRtpClear = _AvRtpClear_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 14),
    _AvRtpClear_Type()
)
avRtpClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpClear.setStatus("current")


class _AvRtpFaultMask_Type(OctetString):
    """Custom type avRtpFaultMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1),
    )


_AvRtpFaultMask_Type.__name__ = "OctetString"
_AvRtpFaultMask_Object = MibScalar
avRtpFaultMask = _AvRtpFaultMask_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 1, 15),
    _AvRtpFaultMask_Type()
)
avRtpFaultMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpFaultMask.setStatus("current")
_AvRtpSessionTable_Object = MibTable
avRtpSessionTable = _AvRtpSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2)
)
if mibBuilder.loadTexts:
    avRtpSessionTable.setStatus("current")
_AvRtpSessionEntry_Object = MibTableRow
avRtpSessionEntry = _AvRtpSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1)
)
avRtpSessionEntry.setIndexNames(
    (0, "AVAYA-RTP-MIB", "avRtpSessionState"),
    (0, "AVAYA-RTP-MIB", "avRtpSessionID"),
)
if mibBuilder.loadTexts:
    avRtpSessionEntry.setStatus("current")


class _AvRtpSessionState_Type(Integer32):
    """Custom type avRtpSessionState based on Integer32"""
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
        *(("active", 1),
          ("activeWithEvent", 2),
          ("terminated", 3),
          ("terminatedWithEvent", 4))
    )


_AvRtpSessionState_Type.__name__ = "Integer32"
_AvRtpSessionState_Object = MibTableColumn
avRtpSessionState = _AvRtpSessionState_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 1),
    _AvRtpSessionState_Type()
)
avRtpSessionState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionState.setStatus("current")
_AvRtpSessionID_Type = Integer32
_AvRtpSessionID_Object = MibTableColumn
avRtpSessionID = _AvRtpSessionID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 2),
    _AvRtpSessionID_Type()
)
avRtpSessionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionID.setStatus("current")
_AvRtpSessionEngineID_Type = Integer32
_AvRtpSessionEngineID_Object = MibTableColumn
avRtpSessionEngineID = _AvRtpSessionEngineID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 3),
    _AvRtpSessionEngineID_Type()
)
avRtpSessionEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionEngineID.setStatus("current")
_AvRtpSessionLocAddrType_Type = InetAddressType
_AvRtpSessionLocAddrType_Object = MibTableColumn
avRtpSessionLocAddrType = _AvRtpSessionLocAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 4),
    _AvRtpSessionLocAddrType_Type()
)
avRtpSessionLocAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionLocAddrType.setStatus("current")
_AvRtpSessionLocAddr_Type = InetAddress
_AvRtpSessionLocAddr_Object = MibTableColumn
avRtpSessionLocAddr = _AvRtpSessionLocAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 5),
    _AvRtpSessionLocAddr_Type()
)
avRtpSessionLocAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionLocAddr.setStatus("current")
_AvRtpSessionLocAddrV4_Type = IpAddress
_AvRtpSessionLocAddrV4_Object = MibTableColumn
avRtpSessionLocAddrV4 = _AvRtpSessionLocAddrV4_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 6),
    _AvRtpSessionLocAddrV4_Type()
)
avRtpSessionLocAddrV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionLocAddrV4.setStatus("current")
_AvRtpSessionLocAddrV6_Type = InetAddressIPv6
_AvRtpSessionLocAddrV6_Object = MibTableColumn
avRtpSessionLocAddrV6 = _AvRtpSessionLocAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 7),
    _AvRtpSessionLocAddrV6_Type()
)
avRtpSessionLocAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionLocAddrV6.setStatus("current")
_AvRtpSessionRemAddrType_Type = InetAddressType
_AvRtpSessionRemAddrType_Object = MibTableColumn
avRtpSessionRemAddrType = _AvRtpSessionRemAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 8),
    _AvRtpSessionRemAddrType_Type()
)
avRtpSessionRemAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemAddrType.setStatus("current")
_AvRtpSessionRemAddr_Type = InetAddress
_AvRtpSessionRemAddr_Object = MibTableColumn
avRtpSessionRemAddr = _AvRtpSessionRemAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 9),
    _AvRtpSessionRemAddr_Type()
)
avRtpSessionRemAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemAddr.setStatus("current")
_AvRtpSessionRemAddrV4_Type = IpAddress
_AvRtpSessionRemAddrV4_Object = MibTableColumn
avRtpSessionRemAddrV4 = _AvRtpSessionRemAddrV4_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 10),
    _AvRtpSessionRemAddrV4_Type()
)
avRtpSessionRemAddrV4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemAddrV4.setStatus("current")
_AvRtpSessionRemAddrV6_Type = InetAddressIPv6
_AvRtpSessionRemAddrV6_Object = MibTableColumn
avRtpSessionRemAddrV6 = _AvRtpSessionRemAddrV6_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 11),
    _AvRtpSessionRemAddrV6_Type()
)
avRtpSessionRemAddrV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemAddrV6.setStatus("current")
_AvRtpSessionLocPort_Type = InetPortNumber
_AvRtpSessionLocPort_Object = MibTableColumn
avRtpSessionLocPort = _AvRtpSessionLocPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 12),
    _AvRtpSessionLocPort_Type()
)
avRtpSessionLocPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionLocPort.setStatus("current")
_AvRtpSessionRemPort_Type = InetPortNumber
_AvRtpSessionRemPort_Object = MibTableColumn
avRtpSessionRemPort = _AvRtpSessionRemPort_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 13),
    _AvRtpSessionRemPort_Type()
)
avRtpSessionRemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemPort.setStatus("current")
_AvRtpSessionStartTime_Type = DateAndTime
_AvRtpSessionStartTime_Object = MibTableColumn
avRtpSessionStartTime = _AvRtpSessionStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 14),
    _AvRtpSessionStartTime_Type()
)
avRtpSessionStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionStartTime.setStatus("current")
_AvRtpSessionEndTime_Type = DateAndTime
_AvRtpSessionEndTime_Object = MibTableColumn
avRtpSessionEndTime = _AvRtpSessionEndTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 15),
    _AvRtpSessionEndTime_Type()
)
avRtpSessionEndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionEndTime.setStatus("current")
_AvRtpSessionDuration_Type = TimeInterval
_AvRtpSessionDuration_Object = MibTableColumn
avRtpSessionDuration = _AvRtpSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 16),
    _AvRtpSessionDuration_Type()
)
avRtpSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionDuration.setStatus("current")


class _AvRtpSessionCname_Type(DisplayString):
    """Custom type avRtpSessionCname based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AvRtpSessionCname_Type.__name__ = "DisplayString"
_AvRtpSessionCname_Object = MibTableColumn
avRtpSessionCname = _AvRtpSessionCname_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 17),
    _AvRtpSessionCname_Type()
)
avRtpSessionCname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionCname.setStatus("current")


class _AvRtpSessionPhone_Type(DisplayString):
    """Custom type avRtpSessionPhone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 22),
    )


_AvRtpSessionPhone_Type.__name__ = "DisplayString"
_AvRtpSessionPhone_Object = MibTableColumn
avRtpSessionPhone = _AvRtpSessionPhone_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 18),
    _AvRtpSessionPhone_Type()
)
avRtpSessionPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionPhone.setStatus("current")


class _AvRtpSessionSeverity_Type(Integer32):
    """Custom type avRtpSessionSeverity based on Integer32"""
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
        *(("cleared", 1),
          ("critical", 3),
          ("indeterminate", 2),
          ("major", 4),
          ("minor", 5),
          ("warning", 6))
    )


_AvRtpSessionSeverity_Type.__name__ = "Integer32"
_AvRtpSessionSeverity_Object = MibTableColumn
avRtpSessionSeverity = _AvRtpSessionSeverity_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 19),
    _AvRtpSessionSeverity_Type()
)
avRtpSessionSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionSeverity.setStatus("current")
_AvRtpSessionTxLen_Type = Integer32
_AvRtpSessionTxLen_Object = MibTableColumn
avRtpSessionTxLen = _AvRtpSessionTxLen_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 20),
    _AvRtpSessionTxLen_Type()
)
avRtpSessionTxLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxLen.setStatus("current")


class _AvRtpSessionType_Type(Integer32):
    """Custom type avRtpSessionType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              4,
              8,
              9,
              15,
              18,
              128,
              129,
              130,
              131,
              132,
              133,
              134,
              135,
              136,
              137,
              138,
              139,
              255)
        )
    )
    namedValues = NamedValues(
        *(("avayaFaxRelay", 128),
          ("clearChannel", 135),
          ("faxPassThru", 130),
          ("g711a", 8),
          ("g711u", 0),
          ("g722", 9),
          ("g723", 4),
          ("g726a32", 139),
          ("g728", 15),
          ("g729", 18),
          ("g729a", 136),
          ("g729ab", 137),
          ("g729b", 138),
          ("modemPassThru", 134),
          ("modemRelay", 133),
          ("t38fax", 129),
          ("ttyPassThru", 132),
          ("ttyRelay", 131),
          ("unspecified", 255))
    )


_AvRtpSessionType_Type.__name__ = "Integer32"
_AvRtpSessionType_Object = MibTableColumn
avRtpSessionType = _AvRtpSessionType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 21),
    _AvRtpSessionType_Type()
)
avRtpSessionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionType.setStatus("current")
_AvRtpSessionTxInterval_Type = Integer32
_AvRtpSessionTxInterval_Object = MibTableColumn
avRtpSessionTxInterval = _AvRtpSessionTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 22),
    _AvRtpSessionTxInterval_Type()
)
avRtpSessionTxInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxInterval.setStatus("current")


class _AvRtpSessionTxEncryp_Type(Integer32):
    """Custom type avRtpSessionTxEncryp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1,
              2,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("encryptionAEAv2", 1),
          ("encryptionAES", 2),
          ("encryptionOff", 0),
          ("srtp", 10),
          ("srtpAesCm128", 4),
          ("srtpAesCm128HmacSha132", 6),
          ("srtpAesCm128HmacSha180", 5),
          ("srtpF8128HmacSha180", 7),
          ("srtpHmacSha132", 9),
          ("srtpHmacSha180", 8),
          ("unknown", -1))
    )


_AvRtpSessionTxEncryp_Type.__name__ = "Integer32"
_AvRtpSessionTxEncryp_Object = MibTableColumn
avRtpSessionTxEncryp = _AvRtpSessionTxEncryp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 23),
    _AvRtpSessionTxEncryp_Type()
)
avRtpSessionTxEncryp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxEncryp.setStatus("current")


class _AvRtpSessionTxDscp_Type(Integer32):
    """Custom type avRtpSessionTxDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AvRtpSessionTxDscp_Type.__name__ = "Integer32"
_AvRtpSessionTxDscp_Object = MibTableColumn
avRtpSessionTxDscp = _AvRtpSessionTxDscp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 24),
    _AvRtpSessionTxDscp_Type()
)
avRtpSessionTxDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxDscp.setStatus("current")


class _AvRtpSessionTxVlan_Type(Integer32):
    """Custom type avRtpSessionTxVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4095),
    )


_AvRtpSessionTxVlan_Type.__name__ = "Integer32"
_AvRtpSessionTxVlan_Object = MibTableColumn
avRtpSessionTxVlan = _AvRtpSessionTxVlan_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 25),
    _AvRtpSessionTxVlan_Type()
)
avRtpSessionTxVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxVlan.setStatus("current")


class _AvRtpSessionTxL2Pri_Type(Integer32):
    """Custom type avRtpSessionTxL2Pri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AvRtpSessionTxL2Pri_Type.__name__ = "Integer32"
_AvRtpSessionTxL2Pri_Object = MibTableColumn
avRtpSessionTxL2Pri = _AvRtpSessionTxL2Pri_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 26),
    _AvRtpSessionTxL2Pri_Type()
)
avRtpSessionTxL2Pri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxL2Pri.setStatus("current")
_AvRtpSessionTxSilenceSupp_Type = AvRtpSilenceSupp
_AvRtpSessionTxSilenceSupp_Object = MibTableColumn
avRtpSessionTxSilenceSupp = _AvRtpSessionTxSilenceSupp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 27),
    _AvRtpSessionTxSilenceSupp_Type()
)
avRtpSessionTxSilenceSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxSilenceSupp.setStatus("current")
_AvRtpSessionTxSsrc_Type = Unsigned32
_AvRtpSessionTxSsrc_Object = MibTableColumn
avRtpSessionTxSsrc = _AvRtpSessionTxSsrc_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 28),
    _AvRtpSessionTxSsrc_Type()
)
avRtpSessionTxSsrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxSsrc.setStatus("current")


class _AvRtpSessionTxRsvp_Type(Integer32):
    """Custom type avRtpSessionTxRsvp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("failed", 3),
          ("pending", 2),
          ("reserved", 4),
          ("unused", 0))
    )


_AvRtpSessionTxRsvp_Type.__name__ = "Integer32"
_AvRtpSessionTxRsvp_Object = MibTableColumn
avRtpSessionTxRsvp = _AvRtpSessionTxRsvp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 29),
    _AvRtpSessionTxRsvp_Type()
)
avRtpSessionTxRsvp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxRsvp.setStatus("current")
_AvRtpSessionTxResvFail_Type = Gauge32
_AvRtpSessionTxResvFail_Object = MibTableColumn
avRtpSessionTxResvFail = _AvRtpSessionTxResvFail_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 30),
    _AvRtpSessionTxResvFail_Type()
)
avRtpSessionTxResvFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxResvFail.setStatus("current")
_AvRtpSessionStatInterval_Type = TimeInterval
_AvRtpSessionStatInterval_Object = MibTableColumn
avRtpSessionStatInterval = _AvRtpSessionStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 31),
    _AvRtpSessionStatInterval_Type()
)
avRtpSessionStatInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionStatInterval.setStatus("current")
_AvRtpSessionRxCodecPlayTime_Type = Counter32
_AvRtpSessionRxCodecPlayTime_Object = MibTableColumn
avRtpSessionRxCodecPlayTime = _AvRtpSessionRxCodecPlayTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 32),
    _AvRtpSessionRxCodecPlayTime_Type()
)
avRtpSessionRxCodecPlayTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxCodecPlayTime.setStatus("current")
_AvRtpSessionRxCodecLossCount_Type = Counter32
_AvRtpSessionRxCodecLossCount_Object = MibTableColumn
avRtpSessionRxCodecLossCount = _AvRtpSessionRxCodecLossCount_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 33),
    _AvRtpSessionRxCodecLossCount_Type()
)
avRtpSessionRxCodecLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxCodecLossCount.setStatus("current")
_AvRtpSessionRxCodecLoss_Type = AvRtpLoss
_AvRtpSessionRxCodecLoss_Object = MibTableColumn
avRtpSessionRxCodecLoss = _AvRtpSessionRxCodecLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 34),
    _AvRtpSessionRxCodecLoss_Type()
)
avRtpSessionRxCodecLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxCodecLoss.setStatus("current")
_AvRtpSessionRxAvgCodecLoss_Type = AvRtpLoss
_AvRtpSessionRxAvgCodecLoss_Object = MibTableColumn
avRtpSessionRxAvgCodecLoss = _AvRtpSessionRxAvgCodecLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 35),
    _AvRtpSessionRxAvgCodecLoss_Type()
)
avRtpSessionRxAvgCodecLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxAvgCodecLoss.setStatus("current")
_AvRtpSessionRxCodecLossEv_Type = Counter32
_AvRtpSessionRxCodecLossEv_Object = MibTableColumn
avRtpSessionRxCodecLossEv = _AvRtpSessionRxCodecLossEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 36),
    _AvRtpSessionRxCodecLossEv_Type()
)
avRtpSessionRxCodecLossEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxCodecLossEv.setStatus("current")
_AvRtpSessionRxLoss_Type = AvRtpLoss
_AvRtpSessionRxLoss_Object = MibTableColumn
avRtpSessionRxLoss = _AvRtpSessionRxLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 37),
    _AvRtpSessionRxLoss_Type()
)
avRtpSessionRxLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxLoss.setStatus("current")
_AvRtpSessionRxAvgLoss_Type = AvRtpLoss
_AvRtpSessionRxAvgLoss_Object = MibTableColumn
avRtpSessionRxAvgLoss = _AvRtpSessionRxAvgLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 38),
    _AvRtpSessionRxAvgLoss_Type()
)
avRtpSessionRxAvgLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxAvgLoss.setStatus("current")
_AvRtpSessionRxLossEv_Type = Counter32
_AvRtpSessionRxLossEv_Object = MibTableColumn
avRtpSessionRxLossEv = _AvRtpSessionRxLossEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 39),
    _AvRtpSessionRxLossEv_Type()
)
avRtpSessionRxLossEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxLossEv.setStatus("current")
_AvRtpSessionRx_Type = Counter32
_AvRtpSessionRx_Object = MibTableColumn
avRtpSessionRx = _AvRtpSessionRx_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 40),
    _AvRtpSessionRx_Type()
)
avRtpSessionRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRx.setStatus("current")
_AvRtpSessionRxLossCount_Type = Counter32
_AvRtpSessionRxLossCount_Object = MibTableColumn
avRtpSessionRxLossCount = _AvRtpSessionRxLossCount_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 41),
    _AvRtpSessionRxLossCount_Type()
)
avRtpSessionRxLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxLossCount.setStatus("current")
_AvRtpSessionRxSeqFall_Type = Counter32
_AvRtpSessionRxSeqFall_Object = MibTableColumn
avRtpSessionRxSeqFall = _AvRtpSessionRxSeqFall_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 42),
    _AvRtpSessionRxSeqFall_Type()
)
avRtpSessionRxSeqFall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxSeqFall.setStatus("current")
_AvRtpSessionRxDup_Type = Counter32
_AvRtpSessionRxDup_Object = MibTableColumn
avRtpSessionRxDup = _AvRtpSessionRxDup_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 43),
    _AvRtpSessionRxDup_Type()
)
avRtpSessionRxDup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxDup.setStatus("current")
_AvRtpSessionRxJBufUnderruns_Type = Gauge32
_AvRtpSessionRxJBufUnderruns_Object = MibTableColumn
avRtpSessionRxJBufUnderruns = _AvRtpSessionRxJBufUnderruns_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 44),
    _AvRtpSessionRxJBufUnderruns_Type()
)
avRtpSessionRxJBufUnderruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxJBufUnderruns.setStatus("current")
_AvRtpSessionRxJBufOverruns_Type = Gauge32
_AvRtpSessionRxJBufOverruns_Object = MibTableColumn
avRtpSessionRxJBufOverruns = _AvRtpSessionRxJBufOverruns_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 45),
    _AvRtpSessionRxJBufOverruns_Type()
)
avRtpSessionRxJBufOverruns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxJBufOverruns.setStatus("current")
_AvRtpSessionRxJBufDelay_Type = Integer32
_AvRtpSessionRxJBufDelay_Object = MibTableColumn
avRtpSessionRxJBufDelay = _AvRtpSessionRxJBufDelay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 46),
    _AvRtpSessionRxJBufDelay_Type()
)
avRtpSessionRxJBufDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxJBufDelay.setStatus("current")
_AvRtpSessionRxMaxJBufDelay_Type = Integer32
_AvRtpSessionRxMaxJBufDelay_Object = MibTableColumn
avRtpSessionRxMaxJBufDelay = _AvRtpSessionRxMaxJBufDelay_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 47),
    _AvRtpSessionRxMaxJBufDelay_Type()
)
avRtpSessionRxMaxJBufDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxMaxJBufDelay.setStatus("current")
_AvRtpSessionRxJitter_Type = Integer32
_AvRtpSessionRxJitter_Object = MibTableColumn
avRtpSessionRxJitter = _AvRtpSessionRxJitter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 48),
    _AvRtpSessionRxJitter_Type()
)
avRtpSessionRxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxJitter.setStatus("current")
_AvRtpSessionRxAvgJitter_Type = Integer32
_AvRtpSessionRxAvgJitter_Object = MibTableColumn
avRtpSessionRxAvgJitter = _AvRtpSessionRxAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 49),
    _AvRtpSessionRxAvgJitter_Type()
)
avRtpSessionRxAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxAvgJitter.setStatus("current")
_AvRtpSessionRxJitterEv_Type = Counter32
_AvRtpSessionRxJitterEv_Object = MibTableColumn
avRtpSessionRxJitterEv = _AvRtpSessionRxJitterEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 50),
    _AvRtpSessionRxJitterEv_Type()
)
avRtpSessionRxJitterEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxJitterEv.setStatus("current")


class _AvRtpSessionRxTtl_Type(Integer32):
    """Custom type avRtpSessionRxTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AvRtpSessionRxTtl_Type.__name__ = "Integer32"
_AvRtpSessionRxTtl_Object = MibTableColumn
avRtpSessionRxTtl = _AvRtpSessionRxTtl_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 51),
    _AvRtpSessionRxTtl_Type()
)
avRtpSessionRxTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxTtl.setStatus("current")


class _AvRtpSessionRxMinTtl_Type(Integer32):
    """Custom type avRtpSessionRxMinTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AvRtpSessionRxMinTtl_Type.__name__ = "Integer32"
_AvRtpSessionRxMinTtl_Object = MibTableColumn
avRtpSessionRxMinTtl = _AvRtpSessionRxMinTtl_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 52),
    _AvRtpSessionRxMinTtl_Type()
)
avRtpSessionRxMinTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxMinTtl.setStatus("current")


class _AvRtpSessionRxMaxTtl_Type(Integer32):
    """Custom type avRtpSessionRxMaxTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AvRtpSessionRxMaxTtl_Type.__name__ = "Integer32"
_AvRtpSessionRxMaxTtl_Object = MibTableColumn
avRtpSessionRxMaxTtl = _AvRtpSessionRxMaxTtl_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 53),
    _AvRtpSessionRxMaxTtl_Type()
)
avRtpSessionRxMaxTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxMaxTtl.setStatus("current")


class _AvRtpSessionRxDscp_Type(Integer32):
    """Custom type avRtpSessionRxDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AvRtpSessionRxDscp_Type.__name__ = "Integer32"
_AvRtpSessionRxDscp_Object = MibTableColumn
avRtpSessionRxDscp = _AvRtpSessionRxDscp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 54),
    _AvRtpSessionRxDscp_Type()
)
avRtpSessionRxDscp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxDscp.setStatus("current")


class _AvRtpSessionRxL2Pri_Type(Integer32):
    """Custom type avRtpSessionRxL2Pri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 7),
    )


_AvRtpSessionRxL2Pri_Type.__name__ = "Integer32"
_AvRtpSessionRxL2Pri_Object = MibTableColumn
avRtpSessionRxL2Pri = _AvRtpSessionRxL2Pri_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 55),
    _AvRtpSessionRxL2Pri_Type()
)
avRtpSessionRxL2Pri.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxL2Pri.setStatus("current")
_AvRtpSessionRxSilenceSupp_Type = AvRtpSilenceSupp
_AvRtpSessionRxSilenceSupp_Object = MibTableColumn
avRtpSessionRxSilenceSupp = _AvRtpSessionRxSilenceSupp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 56),
    _AvRtpSessionRxSilenceSupp_Type()
)
avRtpSessionRxSilenceSupp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxSilenceSupp.setStatus("current")
_AvRtpSessionRxSsrc_Type = Unsigned32
_AvRtpSessionRxSsrc_Object = MibTableColumn
avRtpSessionRxSsrc = _AvRtpSessionRxSsrc_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 57),
    _AvRtpSessionRxSsrc_Type()
)
avRtpSessionRxSsrc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxSsrc.setStatus("current")
_AvRtpSessionRxSsrcChange_Type = Counter32
_AvRtpSessionRxSsrcChange_Object = MibTableColumn
avRtpSessionRxSsrcChange = _AvRtpSessionRxSsrcChange_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 58),
    _AvRtpSessionRxSsrcChange_Type()
)
avRtpSessionRxSsrcChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxSsrcChange.setStatus("current")
_AvRtpSessionTxRtcp_Type = Counter32
_AvRtpSessionTxRtcp_Object = MibTableColumn
avRtpSessionTxRtcp = _AvRtpSessionTxRtcp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 59),
    _AvRtpSessionTxRtcp_Type()
)
avRtpSessionTxRtcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxRtcp.setStatus("current")
_AvRtpSessionRxRtcp_Type = Counter32
_AvRtpSessionRxRtcp_Object = MibTableColumn
avRtpSessionRxRtcp = _AvRtpSessionRxRtcp_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 60),
    _AvRtpSessionRxRtcp_Type()
)
avRtpSessionRxRtcp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxRtcp.setStatus("current")
_AvRtpSessionCodecRtt_Type = Integer32
_AvRtpSessionCodecRtt_Object = MibTableColumn
avRtpSessionCodecRtt = _AvRtpSessionCodecRtt_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 61),
    _AvRtpSessionCodecRtt_Type()
)
avRtpSessionCodecRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionCodecRtt.setStatus("current")
_AvRtpSessionAvgCodecRtt_Type = Integer32
_AvRtpSessionAvgCodecRtt_Object = MibTableColumn
avRtpSessionAvgCodecRtt = _AvRtpSessionAvgCodecRtt_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 62),
    _AvRtpSessionAvgCodecRtt_Type()
)
avRtpSessionAvgCodecRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionAvgCodecRtt.setStatus("current")
_AvRtpSessionCodecRttEv_Type = Counter32
_AvRtpSessionCodecRttEv_Object = MibTableColumn
avRtpSessionCodecRttEv = _AvRtpSessionCodecRttEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 63),
    _AvRtpSessionCodecRttEv_Type()
)
avRtpSessionCodecRttEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionCodecRttEv.setStatus("current")
_AvRtpSessionRtt_Type = Integer32
_AvRtpSessionRtt_Object = MibTableColumn
avRtpSessionRtt = _AvRtpSessionRtt_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 64),
    _AvRtpSessionRtt_Type()
)
avRtpSessionRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRtt.setStatus("current")
_AvRtpSessionAvgRtt_Type = Integer32
_AvRtpSessionAvgRtt_Object = MibTableColumn
avRtpSessionAvgRtt = _AvRtpSessionAvgRtt_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 65),
    _AvRtpSessionAvgRtt_Type()
)
avRtpSessionAvgRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionAvgRtt.setStatus("current")
_AvRtpSessionRttEv_Type = Counter32
_AvRtpSessionRttEv_Object = MibTableColumn
avRtpSessionRttEv = _AvRtpSessionRttEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 66),
    _AvRtpSessionRttEv_Type()
)
avRtpSessionRttEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRttEv.setStatus("current")
_AvRtpSessionRemLoss_Type = AvRtpLoss
_AvRtpSessionRemLoss_Object = MibTableColumn
avRtpSessionRemLoss = _AvRtpSessionRemLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 67),
    _AvRtpSessionRemLoss_Type()
)
avRtpSessionRemLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemLoss.setStatus("current")
_AvRtpSessionRemAvgLoss_Type = AvRtpLoss
_AvRtpSessionRemAvgLoss_Object = MibTableColumn
avRtpSessionRemAvgLoss = _AvRtpSessionRemAvgLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 68),
    _AvRtpSessionRemAvgLoss_Type()
)
avRtpSessionRemAvgLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemAvgLoss.setStatus("current")
_AvRtpSessionRemLossEv_Type = Counter32
_AvRtpSessionRemLossEv_Object = MibTableColumn
avRtpSessionRemLossEv = _AvRtpSessionRemLossEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 69),
    _AvRtpSessionRemLossEv_Type()
)
avRtpSessionRemLossEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemLossEv.setStatus("current")
_AvRtpSessionRemJitter_Type = Integer32
_AvRtpSessionRemJitter_Object = MibTableColumn
avRtpSessionRemJitter = _AvRtpSessionRemJitter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 70),
    _AvRtpSessionRemJitter_Type()
)
avRtpSessionRemJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemJitter.setStatus("current")
_AvRtpSessionRemAvgJitter_Type = Integer32
_AvRtpSessionRemAvgJitter_Object = MibTableColumn
avRtpSessionRemAvgJitter = _AvRtpSessionRemAvgJitter_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 71),
    _AvRtpSessionRemAvgJitter_Type()
)
avRtpSessionRemAvgJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemAvgJitter.setStatus("current")
_AvRtpSessionRemJitterEv_Type = Counter32
_AvRtpSessionRemJitterEv_Object = MibTableColumn
avRtpSessionRemJitterEv = _AvRtpSessionRemJitterEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 72),
    _AvRtpSessionRemJitterEv_Type()
)
avRtpSessionRemJitterEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRemJitterEv.setStatus("current")
_AvRtpSessionEcTailLen_Type = Integer32
_AvRtpSessionEcTailLen_Object = MibTableColumn
avRtpSessionEcTailLen = _AvRtpSessionEcTailLen_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 73),
    _AvRtpSessionEcTailLen_Type()
)
avRtpSessionEcTailLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionEcTailLen.setStatus("current")


class _AvRtpSessionEcReturnLoss_Type(Integer32):
    """Custom type avRtpSessionEcReturnLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AvRtpSessionEcReturnLoss_Type.__name__ = "Integer32"
_AvRtpSessionEcReturnLoss_Object = MibTableColumn
avRtpSessionEcReturnLoss = _AvRtpSessionEcReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 74),
    _AvRtpSessionEcReturnLoss_Type()
)
avRtpSessionEcReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionEcReturnLoss.setStatus("current")
_AvRtpSessionEcReturnLossEv_Type = Counter32
_AvRtpSessionEcReturnLossEv_Object = MibTableColumn
avRtpSessionEcReturnLossEv = _AvRtpSessionEcReturnLossEv_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 75),
    _AvRtpSessionEcReturnLossEv_Type()
)
avRtpSessionEcReturnLossEv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionEcReturnLossEv.setStatus("current")


class _AvRtpSessionAEC_Type(Integer32):
    """Custom type avRtpSessionAEC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("aec", 4),
          ("fullDuplex", 3),
          ("halfDuplex", 2),
          ("none", 1),
          ("notSupported", 0))
    )


_AvRtpSessionAEC_Type.__name__ = "Integer32"
_AvRtpSessionAEC_Object = MibTableColumn
avRtpSessionAEC = _AvRtpSessionAEC_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 76),
    _AvRtpSessionAEC_Type()
)
avRtpSessionAEC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionAEC.setStatus("current")


class _AvRtpSessionDebugStr_Type(DisplayString):
    """Custom type avRtpSessionDebugStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AvRtpSessionDebugStr_Type.__name__ = "DisplayString"
_AvRtpSessionDebugStr_Object = MibTableColumn
avRtpSessionDebugStr = _AvRtpSessionDebugStr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 77),
    _AvRtpSessionDebugStr_Type()
)
avRtpSessionDebugStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionDebugStr.setStatus("current")


class _AvRtpSessionTxFlowLabel_Type(Integer32):
    """Custom type avRtpSessionTxFlowLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_AvRtpSessionTxFlowLabel_Type.__name__ = "Integer32"
_AvRtpSessionTxFlowLabel_Object = MibTableColumn
avRtpSessionTxFlowLabel = _AvRtpSessionTxFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 78),
    _AvRtpSessionTxFlowLabel_Type()
)
avRtpSessionTxFlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionTxFlowLabel.setStatus("current")


class _AvRtpSessionRxFlowLabel_Type(Integer32):
    """Custom type avRtpSessionRxFlowLabel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_AvRtpSessionRxFlowLabel_Type.__name__ = "Integer32"
_AvRtpSessionRxFlowLabel_Object = MibTableColumn
avRtpSessionRxFlowLabel = _AvRtpSessionRxFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 2, 1, 79),
    _AvRtpSessionRxFlowLabel_Type()
)
avRtpSessionRxFlowLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSessionRxFlowLabel.setStatus("current")
_AvRtpSumTable_Object = MibTable
avRtpSumTable = _AvRtpSumTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3)
)
if mibBuilder.loadTexts:
    avRtpSumTable.setStatus("current")
_AvRtpSumEntry_Object = MibTableRow
avRtpSumEntry = _AvRtpSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1)
)
avRtpSumEntry.setIndexNames(
    (0, "AVAYA-RTP-MIB", "avRtpSumEngineID"),
)
if mibBuilder.loadTexts:
    avRtpSumEntry.setStatus("current")
_AvRtpSumEngineID_Type = Integer32
_AvRtpSumEngineID_Object = MibTableColumn
avRtpSumEngineID = _AvRtpSumEngineID_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1, 1),
    _AvRtpSumEngineID_Type()
)
avRtpSumEngineID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSumEngineID.setStatus("current")


class _AvRtpSumEngineDescr_Type(DisplayString):
    """Custom type avRtpSumEngineDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvRtpSumEngineDescr_Type.__name__ = "DisplayString"
_AvRtpSumEngineDescr_Object = MibTableColumn
avRtpSumEngineDescr = _AvRtpSumEngineDescr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1, 2),
    _AvRtpSumEngineDescr_Type()
)
avRtpSumEngineDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSumEngineDescr.setStatus("current")
_AvRtpSumPeriod_Type = TimeInterval
_AvRtpSumPeriod_Object = MibTableColumn
avRtpSumPeriod = _AvRtpSumPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1, 3),
    _AvRtpSumPeriod_Type()
)
avRtpSumPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSumPeriod.setStatus("current")
_AvRtpSumActiveFlows_Type = Integer32
_AvRtpSumActiveFlows_Object = MibTableColumn
avRtpSumActiveFlows = _AvRtpSumActiveFlows_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1, 4),
    _AvRtpSumActiveFlows_Type()
)
avRtpSumActiveFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSumActiveFlows.setStatus("current")
_AvRtpSumActiveQosEvents_Type = Integer32
_AvRtpSumActiveQosEvents_Object = MibTableColumn
avRtpSumActiveQosEvents = _AvRtpSumActiveQosEvents_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1, 5),
    _AvRtpSumActiveQosEvents_Type()
)
avRtpSumActiveQosEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSumActiveQosEvents.setStatus("current")
_AvRtpSumTotalFlows_Type = Counter32
_AvRtpSumTotalFlows_Object = MibTableColumn
avRtpSumTotalFlows = _AvRtpSumTotalFlows_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1, 6),
    _AvRtpSumTotalFlows_Type()
)
avRtpSumTotalFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSumTotalFlows.setStatus("current")
_AvRtpSumTotalFlowsQoSEvents_Type = Counter32
_AvRtpSumTotalFlowsQoSEvents_Object = MibTableColumn
avRtpSumTotalFlowsQoSEvents = _AvRtpSumTotalFlowsQoSEvents_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1, 7),
    _AvRtpSumTotalFlowsQoSEvents_Type()
)
avRtpSumTotalFlowsQoSEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSumTotalFlowsQoSEvents.setStatus("current")


class _AvRtpSumTxTTL_Type(Integer32):
    """Custom type avRtpSumTxTTL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AvRtpSumTxTTL_Type.__name__ = "Integer32"
_AvRtpSumTxTTL_Object = MibTableColumn
avRtpSumTxTTL = _AvRtpSumTxTTL_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1, 8),
    _AvRtpSumTxTTL_Type()
)
avRtpSumTxTTL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSumTxTTL.setStatus("current")
_AvRtpSumSessionDuration_Type = Counter32
_AvRtpSumSessionDuration_Object = MibTableColumn
avRtpSumSessionDuration = _AvRtpSumSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1, 9),
    _AvRtpSumSessionDuration_Type()
)
avRtpSumSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpSumSessionDuration.setStatus("current")
_AvRtpSumClear_Type = TruthValue
_AvRtpSumClear_Object = MibTableColumn
avRtpSumClear = _AvRtpSumClear_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 3, 1, 10),
    _AvRtpSumClear_Type()
)
avRtpSumClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avRtpSumClear.setStatus("current")
_AvRtpLookupTable_Object = MibTable
avRtpLookupTable = _AvRtpLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 4)
)
if mibBuilder.loadTexts:
    avRtpLookupTable.setStatus("current")
_AvRtpLookupEntry_Object = MibTableRow
avRtpLookupEntry = _AvRtpLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 4, 1)
)
avRtpLookupEntry.setIndexNames(
    (0, "AVAYA-RTP-MIB", "avRtpSessionRemAddrType"),
    (0, "AVAYA-RTP-MIB", "avRtpSessionRemAddr"),
    (0, "AVAYA-RTP-MIB", "avRtpSessionState"),
    (0, "AVAYA-RTP-MIB", "avRtpSessionID"),
)
if mibBuilder.loadTexts:
    avRtpLookupEntry.setStatus("current")
_AvRtpLookupStartTime_Type = DateAndTime
_AvRtpLookupStartTime_Object = MibTableColumn
avRtpLookupStartTime = _AvRtpLookupStartTime_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 4, 1, 1),
    _AvRtpLookupStartTime_Type()
)
avRtpLookupStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avRtpLookupStartTime.setStatus("current")
_AvRtpNotificationVarbinds_ObjectIdentity = ObjectIdentity
avRtpNotificationVarbinds = _AvRtpNotificationVarbinds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 5)
)
if mibBuilder.loadTexts:
    avRtpNotificationVarbinds.setStatus("current")
_AvRtpSessionLocInetAddrType_Type = InetAddressType
_AvRtpSessionLocInetAddrType_Object = MibScalar
avRtpSessionLocInetAddrType = _AvRtpSessionLocInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 5, 1),
    _AvRtpSessionLocInetAddrType_Type()
)
avRtpSessionLocInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avRtpSessionLocInetAddrType.setStatus("current")
_AvRtpSessionLocInetAddr_Type = InetAddress
_AvRtpSessionLocInetAddr_Object = MibScalar
avRtpSessionLocInetAddr = _AvRtpSessionLocInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 5, 2),
    _AvRtpSessionLocInetAddr_Type()
)
avRtpSessionLocInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avRtpSessionLocInetAddr.setStatus("current")
_AvRtpSessionRemInetAddrType_Type = InetAddressType
_AvRtpSessionRemInetAddrType_Object = MibScalar
avRtpSessionRemInetAddrType = _AvRtpSessionRemInetAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 5, 3),
    _AvRtpSessionRemInetAddrType_Type()
)
avRtpSessionRemInetAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avRtpSessionRemInetAddrType.setStatus("current")
_AvRtpSessionRemInetAddr_Type = InetAddress
_AvRtpSessionRemInetAddr_Object = MibScalar
avRtpSessionRemInetAddr = _AvRtpSessionRemInetAddr_Object(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 5, 4),
    _AvRtpSessionRemInetAddr_Type()
)
avRtpSessionRemInetAddr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avRtpSessionRemInetAddr.setStatus("current")

# Managed Objects groups


# Notification objects

avRtpQoSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 0, 1)
)
avRtpQoSTrap.setObjects(
      *(("AVAYA-RTP-MIB", "avRtpSessionLocAddrV4"),
        ("AVAYA-RTP-MIB", "avRtpSessionRemAddrV4"),
        ("AVAYA-RTP-MIB", "avRtpSessionDuration"),
        ("AVAYA-RTP-MIB", "avRtpSessionCname"),
        ("AVAYA-RTP-MIB", "avRtpSessionPhone"),
        ("AVAYA-RTP-MIB", "avRtpSessionSeverity"),
        ("AVAYA-RTP-MIB", "avRtpSessionDebugStr"))
)
if mibBuilder.loadTexts:
    avRtpQoSTrap.setStatus(
        "current"
    )

avRtpQoSFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 0, 2)
)
avRtpQoSFault.setObjects(
      *(("AVAYA-RTP-MIB", "avRtpQoSFaultTh"),
        ("AVAYA-RTP-MIB", "avRtpQoSClearTh"),
        ("AVAYA-RTP-MIB", "avRtpSessionSeverity"))
)
if mibBuilder.loadTexts:
    avRtpQoSFault.setStatus(
        "current"
    )

avRtpQoSClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 0, 3)
)
avRtpQoSClear.setObjects(
      *(("AVAYA-RTP-MIB", "avRtpQoSFaultTh"),
        ("AVAYA-RTP-MIB", "avRtpQoSClearTh"),
        ("AVAYA-RTP-MIB", "avRtpSessionSeverity"))
)
if mibBuilder.loadTexts:
    avRtpQoSClear.setStatus(
        "current"
    )

avRtpQoSInetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6889, 2, 7, 0, 4)
)
avRtpQoSInetTrap.setObjects(
      *(("AVAYA-RTP-MIB", "avRtpSessionLocInetAddrType"),
        ("AVAYA-RTP-MIB", "avRtpSessionLocInetAddr"),
        ("AVAYA-RTP-MIB", "avRtpSessionRemInetAddrType"),
        ("AVAYA-RTP-MIB", "avRtpSessionRemInetAddr"),
        ("AVAYA-RTP-MIB", "avRtpSessionDuration"),
        ("AVAYA-RTP-MIB", "avRtpSessionCname"),
        ("AVAYA-RTP-MIB", "avRtpSessionPhone"),
        ("AVAYA-RTP-MIB", "avRtpSessionSeverity"),
        ("AVAYA-RTP-MIB", "avRtpSessionDebugStr"))
)
if mibBuilder.loadTexts:
    avRtpQoSInetTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-RTP-MIB",
    **{"AvRtpItuPerceivedSeverity": AvRtpItuPerceivedSeverity,
       "AvRtpLoss": AvRtpLoss,
       "AvRtpSilenceSupp": AvRtpSilenceSupp,
       "avaya": avaya,
       "mibs": mibs,
       "avRtpMib": avRtpMib,
       "avRtpNotification": avRtpNotification,
       "avRtpQoSTrap": avRtpQoSTrap,
       "avRtpQoSFault": avRtpQoSFault,
       "avRtpQoSClear": avRtpQoSClear,
       "avRtpQoSInetTrap": avRtpQoSInetTrap,
       "avRtpConfig": avRtpConfig,
       "avRtpThresholdTable": avRtpThresholdTable,
       "avRtpThresholdEntry": avRtpThresholdEntry,
       "avRtpThresholdSet": avRtpThresholdSet,
       "avRtpThresholdMinStatWin": avRtpThresholdMinStatWin,
       "avRtpThresholdRxCodecLoss": avRtpThresholdRxCodecLoss,
       "avRtpThresholdRxAvgCodecLoss": avRtpThresholdRxAvgCodecLoss,
       "avRtpThresholdRxCodecLossEv": avRtpThresholdRxCodecLossEv,
       "avRtpThresholdCodecRtt": avRtpThresholdCodecRtt,
       "avRtpThresholdCodecRttEv": avRtpThresholdCodecRttEv,
       "avRtpThresholdEcReturnLoss": avRtpThresholdEcReturnLoss,
       "avRtpThresholdEcReturnLossEv": avRtpThresholdEcReturnLossEv,
       "avRtpThresholdRxLoss": avRtpThresholdRxLoss,
       "avRtpThresholdRxLossEv": avRtpThresholdRxLossEv,
       "avRtpThresholdRemLoss": avRtpThresholdRemLoss,
       "avRtpThresholdRemLossEv": avRtpThresholdRemLossEv,
       "avRtpThresholdAvgRxLoss": avRtpThresholdAvgRxLoss,
       "avRtpThresholdAvgRemLoss": avRtpThresholdAvgRemLoss,
       "avRtpThresholdRxJitter": avRtpThresholdRxJitter,
       "avRtpThresholdRxJitterEv": avRtpThresholdRxJitterEv,
       "avRtpThresholdRemJitter": avRtpThresholdRemJitter,
       "avRtpThresholdRemJitterEv": avRtpThresholdRemJitterEv,
       "avRtpThresholdRtt": avRtpThresholdRtt,
       "avRtpThresholdRttEv": avRtpThresholdRttEv,
       "avRtpThresholdRxSsrcChangeEv": avRtpThresholdRxSsrcChangeEv,
       "avRtpEnable": avRtpEnable,
       "avRtpQoSTrapEnable": avRtpQoSTrapEnable,
       "avRtpQoSFaultTrapEnable": avRtpQoSFaultTrapEnable,
       "avRtpQoSFaultTh": avRtpQoSFaultTh,
       "avRtpQoSClearTh": avRtpQoSClearTh,
       "avRtpTxQoSTraps": avRtpTxQoSTraps,
       "avRtpQoSTrapsDrop": avRtpQoSTrapsDrop,
       "avRtpQoSTrapTokenInterval": avRtpQoSTrapTokenInterval,
       "avRtpQoSTrapBucketSize": avRtpQoSTrapBucketSize,
       "avRtpDateAndTime": avRtpDateAndTime,
       "avRtpMaxSessionTableSize": avRtpMaxSessionTableSize,
       "avRtpReservedSessionTableRows": avRtpReservedSessionTableRows,
       "avRtpClear": avRtpClear,
       "avRtpFaultMask": avRtpFaultMask,
       "avRtpSessionTable": avRtpSessionTable,
       "avRtpSessionEntry": avRtpSessionEntry,
       "avRtpSessionState": avRtpSessionState,
       "avRtpSessionID": avRtpSessionID,
       "avRtpSessionEngineID": avRtpSessionEngineID,
       "avRtpSessionLocAddrType": avRtpSessionLocAddrType,
       "avRtpSessionLocAddr": avRtpSessionLocAddr,
       "avRtpSessionLocAddrV4": avRtpSessionLocAddrV4,
       "avRtpSessionLocAddrV6": avRtpSessionLocAddrV6,
       "avRtpSessionRemAddrType": avRtpSessionRemAddrType,
       "avRtpSessionRemAddr": avRtpSessionRemAddr,
       "avRtpSessionRemAddrV4": avRtpSessionRemAddrV4,
       "avRtpSessionRemAddrV6": avRtpSessionRemAddrV6,
       "avRtpSessionLocPort": avRtpSessionLocPort,
       "avRtpSessionRemPort": avRtpSessionRemPort,
       "avRtpSessionStartTime": avRtpSessionStartTime,
       "avRtpSessionEndTime": avRtpSessionEndTime,
       "avRtpSessionDuration": avRtpSessionDuration,
       "avRtpSessionCname": avRtpSessionCname,
       "avRtpSessionPhone": avRtpSessionPhone,
       "avRtpSessionSeverity": avRtpSessionSeverity,
       "avRtpSessionTxLen": avRtpSessionTxLen,
       "avRtpSessionType": avRtpSessionType,
       "avRtpSessionTxInterval": avRtpSessionTxInterval,
       "avRtpSessionTxEncryp": avRtpSessionTxEncryp,
       "avRtpSessionTxDscp": avRtpSessionTxDscp,
       "avRtpSessionTxVlan": avRtpSessionTxVlan,
       "avRtpSessionTxL2Pri": avRtpSessionTxL2Pri,
       "avRtpSessionTxSilenceSupp": avRtpSessionTxSilenceSupp,
       "avRtpSessionTxSsrc": avRtpSessionTxSsrc,
       "avRtpSessionTxRsvp": avRtpSessionTxRsvp,
       "avRtpSessionTxResvFail": avRtpSessionTxResvFail,
       "avRtpSessionStatInterval": avRtpSessionStatInterval,
       "avRtpSessionRxCodecPlayTime": avRtpSessionRxCodecPlayTime,
       "avRtpSessionRxCodecLossCount": avRtpSessionRxCodecLossCount,
       "avRtpSessionRxCodecLoss": avRtpSessionRxCodecLoss,
       "avRtpSessionRxAvgCodecLoss": avRtpSessionRxAvgCodecLoss,
       "avRtpSessionRxCodecLossEv": avRtpSessionRxCodecLossEv,
       "avRtpSessionRxLoss": avRtpSessionRxLoss,
       "avRtpSessionRxAvgLoss": avRtpSessionRxAvgLoss,
       "avRtpSessionRxLossEv": avRtpSessionRxLossEv,
       "avRtpSessionRx": avRtpSessionRx,
       "avRtpSessionRxLossCount": avRtpSessionRxLossCount,
       "avRtpSessionRxSeqFall": avRtpSessionRxSeqFall,
       "avRtpSessionRxDup": avRtpSessionRxDup,
       "avRtpSessionRxJBufUnderruns": avRtpSessionRxJBufUnderruns,
       "avRtpSessionRxJBufOverruns": avRtpSessionRxJBufOverruns,
       "avRtpSessionRxJBufDelay": avRtpSessionRxJBufDelay,
       "avRtpSessionRxMaxJBufDelay": avRtpSessionRxMaxJBufDelay,
       "avRtpSessionRxJitter": avRtpSessionRxJitter,
       "avRtpSessionRxAvgJitter": avRtpSessionRxAvgJitter,
       "avRtpSessionRxJitterEv": avRtpSessionRxJitterEv,
       "avRtpSessionRxTtl": avRtpSessionRxTtl,
       "avRtpSessionRxMinTtl": avRtpSessionRxMinTtl,
       "avRtpSessionRxMaxTtl": avRtpSessionRxMaxTtl,
       "avRtpSessionRxDscp": avRtpSessionRxDscp,
       "avRtpSessionRxL2Pri": avRtpSessionRxL2Pri,
       "avRtpSessionRxSilenceSupp": avRtpSessionRxSilenceSupp,
       "avRtpSessionRxSsrc": avRtpSessionRxSsrc,
       "avRtpSessionRxSsrcChange": avRtpSessionRxSsrcChange,
       "avRtpSessionTxRtcp": avRtpSessionTxRtcp,
       "avRtpSessionRxRtcp": avRtpSessionRxRtcp,
       "avRtpSessionCodecRtt": avRtpSessionCodecRtt,
       "avRtpSessionAvgCodecRtt": avRtpSessionAvgCodecRtt,
       "avRtpSessionCodecRttEv": avRtpSessionCodecRttEv,
       "avRtpSessionRtt": avRtpSessionRtt,
       "avRtpSessionAvgRtt": avRtpSessionAvgRtt,
       "avRtpSessionRttEv": avRtpSessionRttEv,
       "avRtpSessionRemLoss": avRtpSessionRemLoss,
       "avRtpSessionRemAvgLoss": avRtpSessionRemAvgLoss,
       "avRtpSessionRemLossEv": avRtpSessionRemLossEv,
       "avRtpSessionRemJitter": avRtpSessionRemJitter,
       "avRtpSessionRemAvgJitter": avRtpSessionRemAvgJitter,
       "avRtpSessionRemJitterEv": avRtpSessionRemJitterEv,
       "avRtpSessionEcTailLen": avRtpSessionEcTailLen,
       "avRtpSessionEcReturnLoss": avRtpSessionEcReturnLoss,
       "avRtpSessionEcReturnLossEv": avRtpSessionEcReturnLossEv,
       "avRtpSessionAEC": avRtpSessionAEC,
       "avRtpSessionDebugStr": avRtpSessionDebugStr,
       "avRtpSessionTxFlowLabel": avRtpSessionTxFlowLabel,
       "avRtpSessionRxFlowLabel": avRtpSessionRxFlowLabel,
       "avRtpSumTable": avRtpSumTable,
       "avRtpSumEntry": avRtpSumEntry,
       "avRtpSumEngineID": avRtpSumEngineID,
       "avRtpSumEngineDescr": avRtpSumEngineDescr,
       "avRtpSumPeriod": avRtpSumPeriod,
       "avRtpSumActiveFlows": avRtpSumActiveFlows,
       "avRtpSumActiveQosEvents": avRtpSumActiveQosEvents,
       "avRtpSumTotalFlows": avRtpSumTotalFlows,
       "avRtpSumTotalFlowsQoSEvents": avRtpSumTotalFlowsQoSEvents,
       "avRtpSumTxTTL": avRtpSumTxTTL,
       "avRtpSumSessionDuration": avRtpSumSessionDuration,
       "avRtpSumClear": avRtpSumClear,
       "avRtpLookupTable": avRtpLookupTable,
       "avRtpLookupEntry": avRtpLookupEntry,
       "avRtpLookupStartTime": avRtpLookupStartTime,
       "avRtpNotificationVarbinds": avRtpNotificationVarbinds,
       "avRtpSessionLocInetAddrType": avRtpSessionLocInetAddrType,
       "avRtpSessionLocInetAddr": avRtpSessionLocInetAddr,
       "avRtpSessionRemInetAddrType": avRtpSessionRemInetAddrType,
       "avRtpSessionRemInetAddr": avRtpSessionRemInetAddr}
)
