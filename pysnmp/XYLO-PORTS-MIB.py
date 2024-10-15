# SNMP MIB module (XYLO-PORTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/XYLO-PORTS-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:19:34 2024
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")

(anxModem,
 anxsyncports,
 parallelport,
 ports) = mibBuilder.importSymbols(
    "XYLO-MIB-SMI",
    "anxModem",
    "anxsyncports",
    "parallelport",
    "ports")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TotalPorts_Type = Integer32
_TotalPorts_Object = MibScalar
totalPorts = _TotalPorts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 1),
    _TotalPorts_Type()
)
totalPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalPorts.setStatus("mandatory")
_TotalInChars_Type = Counter32
_TotalInChars_Object = MibScalar
totalInChars = _TotalInChars_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 2),
    _TotalInChars_Type()
)
totalInChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalInChars.setStatus("mandatory")
_TotalOutChars_Type = Counter32
_TotalOutChars_Object = MibScalar
totalOutChars = _TotalOutChars_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 3),
    _TotalOutChars_Type()
)
totalOutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOutChars.setStatus("mandatory")
_TotalParityErrs_Type = Counter32
_TotalParityErrs_Object = MibScalar
totalParityErrs = _TotalParityErrs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 4),
    _TotalParityErrs_Type()
)
totalParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalParityErrs.setStatus("mandatory")
_TotalOverrunErrs_Type = Counter32
_TotalOverrunErrs_Object = MibScalar
totalOverrunErrs = _TotalOverrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 5),
    _TotalOverrunErrs_Type()
)
totalOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalOverrunErrs.setStatus("mandatory")
_TotalFramingErrs_Type = Counter32
_TotalFramingErrs_Object = MibScalar
totalFramingErrs = _TotalFramingErrs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 6),
    _TotalFramingErrs_Type()
)
totalFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalFramingErrs.setStatus("mandatory")
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7)
)
if mibBuilder.loadTexts:
    portTable.setStatus("mandatory")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1)
)
portEntry.setIndexNames(
    (0, "XYLO-PORTS-MIB", "anxpPortIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("mandatory")
_AnxpPortIndex_Type = Integer32
_AnxpPortIndex_Object = MibTableColumn
anxpPortIndex = _AnxpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 1),
    _AnxpPortIndex_Type()
)
anxpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpPortIndex.setStatus("mandatory")


class _AnxpMode_Type(Integer32):
    """Custom type anxpMode based on Integer32"""
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
              18)
        )
    )
    namedValues = NamedValues(
        *(("adaptive", 3),
          ("arap", 8),
          ("auto-adapt", 11),
          ("auto-detect", 10),
          ("call", 14),
          ("cli", 1),
          ("connect", 15),
          ("dedicated", 6),
          ("invalid", 9),
          ("ipx", 13),
          ("ndp", 12),
          ("ppp", 7),
          ("rlogin", 16),
          ("slave", 2),
          ("slip", 5),
          ("telnet", 17),
          ("tn3270", 18),
          ("unused", 4))
    )


_AnxpMode_Type.__name__ = "Integer32"
_AnxpMode_Object = MibTableColumn
anxpMode = _AnxpMode_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 2),
    _AnxpMode_Type()
)
anxpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpMode.setStatus("mandatory")


class _AnxpCtrlLines_Type(Integer32):
    """Custom type anxpCtrlLines based on Integer32"""
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
        *(("both", 4),
          ("flowcontrol", 2),
          ("modemcontrol", 3),
          ("none", 1))
    )


_AnxpCtrlLines_Type.__name__ = "Integer32"
_AnxpCtrlLines_Object = MibTableColumn
anxpCtrlLines = _AnxpCtrlLines_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 3),
    _AnxpCtrlLines_Type()
)
anxpCtrlLines.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCtrlLines.setStatus("mandatory")


class _AnxpBidirModem_Type(Integer32):
    """Custom type anxpBidirModem based on Integer32"""
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


_AnxpBidirModem_Type.__name__ = "Integer32"
_AnxpBidirModem_Object = MibTableColumn
anxpBidirModem = _AnxpBidirModem_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 4),
    _AnxpBidirModem_Type()
)
anxpBidirModem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpBidirModem.setStatus("mandatory")


class _AnxpAllowBcast_Type(Integer32):
    """Custom type anxpAllowBcast based on Integer32"""
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


_AnxpAllowBcast_Type.__name__ = "Integer32"
_AnxpAllowBcast_Object = MibTableColumn
anxpAllowBcast = _AnxpAllowBcast_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 5),
    _AnxpAllowBcast_Type()
)
anxpAllowBcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAllowBcast.setStatus("mandatory")


class _AnxpBcastDirection_Type(Integer32):
    """Custom type anxpBcastDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 2),
          ("port", 1))
    )


_AnxpBcastDirection_Type.__name__ = "Integer32"
_AnxpBcastDirection_Object = MibTableColumn
anxpBcastDirection = _AnxpBcastDirection_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 6),
    _AnxpBcastDirection_Type()
)
anxpBcastDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpBcastDirection.setStatus("mandatory")


class _AnxpInputStartChar_Type(DisplayString):
    """Custom type anxpInputStartChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AnxpInputStartChar_Type.__name__ = "DisplayString"
_AnxpInputStartChar_Object = MibTableColumn
anxpInputStartChar = _AnxpInputStartChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 7),
    _AnxpInputStartChar_Type()
)
anxpInputStartChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpInputStartChar.setStatus("mandatory")


class _AnxpInputStopChar_Type(DisplayString):
    """Custom type anxpInputStopChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AnxpInputStopChar_Type.__name__ = "DisplayString"
_AnxpInputStopChar_Object = MibTableColumn
anxpInputStopChar = _AnxpInputStopChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 8),
    _AnxpInputStopChar_Type()
)
anxpInputStopChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpInputStopChar.setStatus("mandatory")


class _AnxpOutputStartChar_Type(DisplayString):
    """Custom type anxpOutputStartChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AnxpOutputStartChar_Type.__name__ = "DisplayString"
_AnxpOutputStartChar_Object = MibTableColumn
anxpOutputStartChar = _AnxpOutputStartChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 9),
    _AnxpOutputStartChar_Type()
)
anxpOutputStartChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpOutputStartChar.setStatus("mandatory")


class _AnxpOutputStopChar_Type(DisplayString):
    """Custom type anxpOutputStopChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AnxpOutputStopChar_Type.__name__ = "DisplayString"
_AnxpOutputStopChar_Object = MibTableColumn
anxpOutputStopChar = _AnxpOutputStopChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 10),
    _AnxpOutputStopChar_Type()
)
anxpOutputStopChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpOutputStopChar.setStatus("mandatory")


class _AnxpIxanyFlowCtl_Type(Integer32):
    """Custom type anxpIxanyFlowCtl based on Integer32"""
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


_AnxpIxanyFlowCtl_Type.__name__ = "Integer32"
_AnxpIxanyFlowCtl_Object = MibTableColumn
anxpIxanyFlowCtl = _AnxpIxanyFlowCtl_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 11),
    _AnxpIxanyFlowCtl_Type()
)
anxpIxanyFlowCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpIxanyFlowCtl.setStatus("mandatory")


class _AnxpLongBreak_Type(Integer32):
    """Custom type anxpLongBreak based on Integer32"""
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


_AnxpLongBreak_Type.__name__ = "Integer32"
_AnxpLongBreak_Object = MibTableColumn
anxpLongBreak = _AnxpLongBreak_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 12),
    _AnxpLongBreak_Type()
)
anxpLongBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpLongBreak.setStatus("mandatory")


class _AnxpShortBreak_Type(Integer32):
    """Custom type anxpShortBreak based on Integer32"""
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


_AnxpShortBreak_Type.__name__ = "Integer32"
_AnxpShortBreak_Object = MibTableColumn
anxpShortBreak = _AnxpShortBreak_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 13),
    _AnxpShortBreak_Type()
)
anxpShortBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpShortBreak.setStatus("mandatory")


class _AnxpForwardTimer_Type(Integer32):
    """Custom type anxpForwardTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpForwardTimer_Type.__name__ = "Integer32"
_AnxpForwardTimer_Object = MibTableColumn
anxpForwardTimer = _AnxpForwardTimer_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 14),
    _AnxpForwardTimer_Type()
)
anxpForwardTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpForwardTimer.setStatus("mandatory")


class _AnxpForwardCount_Type(Integer32):
    """Custom type anxpForwardCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpForwardCount_Type.__name__ = "Integer32"
_AnxpForwardCount_Object = MibTableColumn
anxpForwardCount = _AnxpForwardCount_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 15),
    _AnxpForwardCount_Type()
)
anxpForwardCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpForwardCount.setStatus("mandatory")


class _AnxpImask7Bits_Type(Integer32):
    """Custom type anxpImask7Bits based on Integer32"""
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


_AnxpImask7Bits_Type.__name__ = "Integer32"
_AnxpImask7Bits_Object = MibTableColumn
anxpImask7Bits = _AnxpImask7Bits_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 16),
    _AnxpImask7Bits_Type()
)
anxpImask7Bits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpImask7Bits.setStatus("mandatory")


class _AnxpAttnChar_Type(DisplayString):
    """Custom type anxpAttnChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpAttnChar_Type.__name__ = "DisplayString"
_AnxpAttnChar_Object = MibTableColumn
anxpAttnChar = _AnxpAttnChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 17),
    _AnxpAttnChar_Type()
)
anxpAttnChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAttnChar.setStatus("mandatory")


class _AnxpInputBufSize_Type(Integer32):
    """Custom type anxpInputBufSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AnxpInputBufSize_Type.__name__ = "Integer32"
_AnxpInputBufSize_Object = MibTableColumn
anxpInputBufSize = _AnxpInputBufSize_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 18),
    _AnxpInputBufSize_Type()
)
anxpInputBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpInputBufSize.setStatus("mandatory")


class _AnxpInputIsActivity_Type(Integer32):
    """Custom type anxpInputIsActivity based on Integer32"""
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


_AnxpInputIsActivity_Type.__name__ = "Integer32"
_AnxpInputIsActivity_Object = MibTableColumn
anxpInputIsActivity = _AnxpInputIsActivity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 19),
    _AnxpInputIsActivity_Type()
)
anxpInputIsActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpInputIsActivity.setStatus("mandatory")


class _AnxpOutputIsActivity_Type(Integer32):
    """Custom type anxpOutputIsActivity based on Integer32"""
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


_AnxpOutputIsActivity_Type.__name__ = "Integer32"
_AnxpOutputIsActivity_Object = MibTableColumn
anxpOutputIsActivity = _AnxpOutputIsActivity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 20),
    _AnxpOutputIsActivity_Type()
)
anxpOutputIsActivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpOutputIsActivity.setStatus("mandatory")


class _AnxpInactivityTimer_Type(Integer32):
    """Custom type anxpInactivityTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpInactivityTimer_Type.__name__ = "Integer32"
_AnxpInactivityTimer_Object = MibTableColumn
anxpInactivityTimer = _AnxpInactivityTimer_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 21),
    _AnxpInactivityTimer_Type()
)
anxpInactivityTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpInactivityTimer.setStatus("mandatory")


class _AnxpResetIdleTimer_Type(Integer32):
    """Custom type anxpResetIdleTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("input", 1),
          ("output", 2))
    )


_AnxpResetIdleTimer_Type.__name__ = "Integer32"
_AnxpResetIdleTimer_Object = MibTableColumn
anxpResetIdleTimer = _AnxpResetIdleTimer_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 22),
    _AnxpResetIdleTimer_Type()
)
anxpResetIdleTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpResetIdleTimer.setStatus("mandatory")


class _AnxpCliInactivity_Type(Integer32):
    """Custom type anxpCliInactivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpCliInactivity_Type.__name__ = "Integer32"
_AnxpCliInactivity_Object = MibTableColumn
anxpCliInactivity = _AnxpCliInactivity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 23),
    _AnxpCliInactivity_Type()
)
anxpCliInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCliInactivity.setStatus("mandatory")


class _AnxpCliSecurity_Type(Integer32):
    """Custom type anxpCliSecurity based on Integer32"""
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


_AnxpCliSecurity_Type.__name__ = "Integer32"
_AnxpCliSecurity_Object = MibTableColumn
anxpCliSecurity = _AnxpCliSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 24),
    _AnxpCliSecurity_Type()
)
anxpCliSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCliSecurity.setStatus("mandatory")


class _AnxpConnectSecurity_Type(Integer32):
    """Custom type anxpConnectSecurity based on Integer32"""
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


_AnxpConnectSecurity_Type.__name__ = "Integer32"
_AnxpConnectSecurity_Object = MibTableColumn
anxpConnectSecurity = _AnxpConnectSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 25),
    _AnxpConnectSecurity_Type()
)
anxpConnectSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpConnectSecurity.setStatus("mandatory")


class _AnxpPortServerSecurity_Type(Integer32):
    """Custom type anxpPortServerSecurity based on Integer32"""
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


_AnxpPortServerSecurity_Type.__name__ = "Integer32"
_AnxpPortServerSecurity_Object = MibTableColumn
anxpPortServerSecurity = _AnxpPortServerSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 26),
    _AnxpPortServerSecurity_Type()
)
anxpPortServerSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPortServerSecurity.setStatus("mandatory")


class _AnxpPortPassword_Type(DisplayString):
    """Custom type anxpPortPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxpPortPassword_Type.__name__ = "DisplayString"
_AnxpPortPassword_Object = MibTableColumn
anxpPortPassword = _AnxpPortPassword_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 27),
    _AnxpPortPassword_Type()
)
anxpPortPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPortPassword.setStatus("mandatory")


class _AnxpUserName_Type(DisplayString):
    """Custom type anxpUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpUserName_Type.__name__ = "DisplayString"
_AnxpUserName_Object = MibTableColumn
anxpUserName = _AnxpUserName_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 28),
    _AnxpUserName_Type()
)
anxpUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpUserName.setStatus("mandatory")
_AnxpDedicatedAddr_Type = IpAddress
_AnxpDedicatedAddr_Object = MibTableColumn
anxpDedicatedAddr = _AnxpDedicatedAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 29),
    _AnxpDedicatedAddr_Type()
)
anxpDedicatedAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpDedicatedAddr.setStatus("mandatory")


class _AnxpDedicatedPort_Type(DisplayString):
    """Custom type anxpDedicatedPort based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpDedicatedPort_Type.__name__ = "DisplayString"
_AnxpDedicatedPort_Object = MibTableColumn
anxpDedicatedPort = _AnxpDedicatedPort_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 30),
    _AnxpDedicatedPort_Type()
)
anxpDedicatedPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpDedicatedPort.setStatus("mandatory")


class _AnxpPrompt_Type(DisplayString):
    """Custom type anxpPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AnxpPrompt_Type.__name__ = "DisplayString"
_AnxpPrompt_Object = MibTableColumn
anxpPrompt = _AnxpPrompt_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 31),
    _AnxpPrompt_Type()
)
anxpPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPrompt.setStatus("mandatory")


class _AnxpTermVar_Type(DisplayString):
    """Custom type anxpTermVar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpTermVar_Type.__name__ = "DisplayString"
_AnxpTermVar_Object = MibTableColumn
anxpTermVar = _AnxpTermVar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 32),
    _AnxpTermVar_Type()
)
anxpTermVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpTermVar.setStatus("mandatory")


class _AnxpNewLineTerm_Type(Integer32):
    """Custom type anxpNewLineTerm based on Integer32"""
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


_AnxpNewLineTerm_Type.__name__ = "Integer32"
_AnxpNewLineTerm_Object = MibTableColumn
anxpNewLineTerm = _AnxpNewLineTerm_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 33),
    _AnxpNewLineTerm_Type()
)
anxpNewLineTerm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNewLineTerm.setStatus("mandatory")


class _AnxpEcho_Type(Integer32):
    """Custom type anxpEcho based on Integer32"""
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


_AnxpEcho_Type.__name__ = "Integer32"
_AnxpEcho_Object = MibTableColumn
anxpEcho = _AnxpEcho_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 34),
    _AnxpEcho_Type()
)
anxpEcho.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpEcho.setStatus("mandatory")


class _AnxpMapToLower_Type(Integer32):
    """Custom type anxpMapToLower based on Integer32"""
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


_AnxpMapToLower_Type.__name__ = "Integer32"
_AnxpMapToLower_Object = MibTableColumn
anxpMapToLower = _AnxpMapToLower_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 35),
    _AnxpMapToLower_Type()
)
anxpMapToLower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpMapToLower.setStatus("mandatory")


class _AnxpMapToUpper_Type(Integer32):
    """Custom type anxpMapToUpper based on Integer32"""
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


_AnxpMapToUpper_Type.__name__ = "Integer32"
_AnxpMapToUpper_Object = MibTableColumn
anxpMapToUpper = _AnxpMapToUpper_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 36),
    _AnxpMapToUpper_Type()
)
anxpMapToUpper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpMapToUpper.setStatus("mandatory")


class _AnxpHardwareTabs_Type(Integer32):
    """Custom type anxpHardwareTabs based on Integer32"""
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


_AnxpHardwareTabs_Type.__name__ = "Integer32"
_AnxpHardwareTabs_Object = MibTableColumn
anxpHardwareTabs = _AnxpHardwareTabs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 37),
    _AnxpHardwareTabs_Type()
)
anxpHardwareTabs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpHardwareTabs.setStatus("mandatory")


class _AnxpCharErase_Type(Integer32):
    """Custom type anxpCharErase based on Integer32"""
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


_AnxpCharErase_Type.__name__ = "Integer32"
_AnxpCharErase_Object = MibTableColumn
anxpCharErase = _AnxpCharErase_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 38),
    _AnxpCharErase_Type()
)
anxpCharErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCharErase.setStatus("mandatory")


class _AnxpLineErase_Type(Integer32):
    """Custom type anxpLineErase based on Integer32"""
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


_AnxpLineErase_Type.__name__ = "Integer32"
_AnxpLineErase_Object = MibTableColumn
anxpLineErase = _AnxpLineErase_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 39),
    _AnxpLineErase_Type()
)
anxpLineErase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpLineErase.setStatus("mandatory")


class _AnxpEraseChar_Type(DisplayString):
    """Custom type anxpEraseChar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AnxpEraseChar_Type.__name__ = "DisplayString"
_AnxpEraseChar_Object = MibTableColumn
anxpEraseChar = _AnxpEraseChar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 40),
    _AnxpEraseChar_Type()
)
anxpEraseChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpEraseChar.setStatus("mandatory")


class _AnxpEraseWord_Type(DisplayString):
    """Custom type anxpEraseWord based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AnxpEraseWord_Type.__name__ = "DisplayString"
_AnxpEraseWord_Object = MibTableColumn
anxpEraseWord = _AnxpEraseWord_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 41),
    _AnxpEraseWord_Type()
)
anxpEraseWord.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpEraseWord.setStatus("mandatory")


class _AnxpEraseLine_Type(DisplayString):
    """Custom type anxpEraseLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AnxpEraseLine_Type.__name__ = "DisplayString"
_AnxpEraseLine_Object = MibTableColumn
anxpEraseLine = _AnxpEraseLine_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 42),
    _AnxpEraseLine_Type()
)
anxpEraseLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpEraseLine.setStatus("mandatory")


class _AnxpRedisplayLine_Type(DisplayString):
    """Custom type anxpRedisplayLine based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AnxpRedisplayLine_Type.__name__ = "DisplayString"
_AnxpRedisplayLine_Object = MibTableColumn
anxpRedisplayLine = _AnxpRedisplayLine_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 43),
    _AnxpRedisplayLine_Type()
)
anxpRedisplayLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpRedisplayLine.setStatus("mandatory")


class _AnxpToggleOutput_Type(DisplayString):
    """Custom type anxpToggleOutput based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AnxpToggleOutput_Type.__name__ = "DisplayString"
_AnxpToggleOutput_Object = MibTableColumn
anxpToggleOutput = _AnxpToggleOutput_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 44),
    _AnxpToggleOutput_Type()
)
anxpToggleOutput.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpToggleOutput.setStatus("mandatory")


class _AnxpTelnetEscape_Type(DisplayString):
    """Custom type anxpTelnetEscape based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 2),
    )


_AnxpTelnetEscape_Type.__name__ = "DisplayString"
_AnxpTelnetEscape_Object = MibTableColumn
anxpTelnetEscape = _AnxpTelnetEscape_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 45),
    _AnxpTelnetEscape_Type()
)
anxpTelnetEscape.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpTelnetEscape.setStatus("mandatory")


class _AnxpNeedDsr_Type(Integer32):
    """Custom type anxpNeedDsr based on Integer32"""
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


_AnxpNeedDsr_Type.__name__ = "Integer32"
_AnxpNeedDsr_Object = MibTableColumn
anxpNeedDsr = _AnxpNeedDsr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 46),
    _AnxpNeedDsr_Type()
)
anxpNeedDsr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNeedDsr.setStatus("mandatory")


class _AnxpTelnetCRLF_Type(Integer32):
    """Custom type anxpTelnetCRLF based on Integer32"""
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


_AnxpTelnetCRLF_Type.__name__ = "Integer32"
_AnxpTelnetCRLF_Object = MibTableColumn
anxpTelnetCRLF = _AnxpTelnetCRLF_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 47),
    _AnxpTelnetCRLF_Type()
)
anxpTelnetCRLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpTelnetCRLF.setStatus("mandatory")


class _AnxpLatbEnable_Type(Integer32):
    """Custom type anxpLatbEnable based on Integer32"""
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


_AnxpLatbEnable_Type.__name__ = "Integer32"
_AnxpLatbEnable_Object = MibTableColumn
anxpLatbEnable = _AnxpLatbEnable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 48),
    _AnxpLatbEnable_Type()
)
anxpLatbEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpLatbEnable.setStatus("mandatory")


class _AnxpSlipSecure_Type(Integer32):
    """Custom type anxpSlipSecure based on Integer32"""
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


_AnxpSlipSecure_Type.__name__ = "Integer32"
_AnxpSlipSecure_Object = MibTableColumn
anxpSlipSecure = _AnxpSlipSecure_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 49),
    _AnxpSlipSecure_Type()
)
anxpSlipSecure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipSecure.setStatus("mandatory")
_AnxpNetLocalAddr_Type = IpAddress
_AnxpNetLocalAddr_Object = MibTableColumn
anxpNetLocalAddr = _AnxpNetLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 50),
    _AnxpNetLocalAddr_Type()
)
anxpNetLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNetLocalAddr.setStatus("mandatory")
_AnxpNetRemoteAddr_Type = IpAddress
_AnxpNetRemoteAddr_Object = MibTableColumn
anxpNetRemoteAddr = _AnxpNetRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 51),
    _AnxpNetRemoteAddr_Type()
)
anxpNetRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNetRemoteAddr.setStatus("mandatory")
_AnxpSlipSubnetMask_Type = IpAddress
_AnxpSlipSubnetMask_Object = MibTableColumn
anxpSlipSubnetMask = _AnxpSlipSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 52),
    _AnxpSlipSubnetMask_Type()
)
anxpSlipSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipSubnetMask.setStatus("mandatory")
_AnxpSlipLoadDumpHost_Type = IpAddress
_AnxpSlipLoadDumpHost_Object = MibTableColumn
anxpSlipLoadDumpHost = _AnxpSlipLoadDumpHost_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 53),
    _AnxpSlipLoadDumpHost_Type()
)
anxpSlipLoadDumpHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipLoadDumpHost.setStatus("mandatory")


class _AnxpNetMetric_Type(Integer32):
    """Custom type anxpNetMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AnxpNetMetric_Type.__name__ = "Integer32"
_AnxpNetMetric_Object = MibTableColumn
anxpNetMetric = _AnxpNetMetric_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 54),
    _AnxpNetMetric_Type()
)
anxpNetMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNetMetric.setStatus("mandatory")


class _AnxpSlipAllowDump_Type(Integer32):
    """Custom type anxpSlipAllowDump based on Integer32"""
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


_AnxpSlipAllowDump_Type.__name__ = "Integer32"
_AnxpSlipAllowDump_Object = MibTableColumn
anxpSlipAllowDump = _AnxpSlipAllowDump_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 55),
    _AnxpSlipAllowDump_Type()
)
anxpSlipAllowDump.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipAllowDump.setStatus("mandatory")


class _AnxpDoCompression_Type(Integer32):
    """Custom type anxpDoCompression based on Integer32"""
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


_AnxpDoCompression_Type.__name__ = "Integer32"
_AnxpDoCompression_Object = MibTableColumn
anxpDoCompression = _AnxpDoCompression_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 56),
    _AnxpDoCompression_Type()
)
anxpDoCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpDoCompression.setStatus("mandatory")


class _AnxpAllowCompression_Type(Integer32):
    """Custom type anxpAllowCompression based on Integer32"""
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


_AnxpAllowCompression_Type.__name__ = "Integer32"
_AnxpAllowCompression_Object = MibTableColumn
anxpAllowCompression = _AnxpAllowCompression_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 57),
    _AnxpAllowCompression_Type()
)
anxpAllowCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAllowCompression.setStatus("mandatory")


class _AnxpSlipMtuSize_Type(Integer32):
    """Custom type anxpSlipMtuSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("large", 1),
          ("small", 2))
    )


_AnxpSlipMtuSize_Type.__name__ = "Integer32"
_AnxpSlipMtuSize_Object = MibTableColumn
anxpSlipMtuSize = _AnxpSlipMtuSize_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 58),
    _AnxpSlipMtuSize_Type()
)
anxpSlipMtuSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipMtuSize.setStatus("mandatory")


class _AnxpSlipNoIcmp_Type(Integer32):
    """Custom type anxpSlipNoIcmp based on Integer32"""
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


_AnxpSlipNoIcmp_Type.__name__ = "Integer32"
_AnxpSlipNoIcmp_Object = MibTableColumn
anxpSlipNoIcmp = _AnxpSlipNoIcmp_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 59),
    _AnxpSlipNoIcmp_Type()
)
anxpSlipNoIcmp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipNoIcmp.setStatus("mandatory")


class _AnxpSlipTos_Type(Integer32):
    """Custom type anxpSlipTos based on Integer32"""
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


_AnxpSlipTos_Type.__name__ = "Integer32"
_AnxpSlipTos_Object = MibTableColumn
anxpSlipTos = _AnxpSlipTos_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 60),
    _AnxpSlipTos_Type()
)
anxpSlipTos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpSlipTos.setStatus("mandatory")


class _AnxpPppMru_Type(Integer32):
    """Custom type anxpPppMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_AnxpPppMru_Type.__name__ = "Integer32"
_AnxpPppMru_Object = MibTableColumn
anxpPppMru = _AnxpPppMru_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 61),
    _AnxpPppMru_Type()
)
anxpPppMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppMru.setStatus("mandatory")


class _AnxpPppAcm_Type(DisplayString):
    """Custom type anxpPppAcm based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 10),
    )


_AnxpPppAcm_Type.__name__ = "DisplayString"
_AnxpPppAcm_Object = MibTableColumn
anxpPppAcm = _AnxpPppAcm_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 62),
    _AnxpPppAcm_Type()
)
anxpPppAcm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppAcm.setStatus("mandatory")


class _AnxpPppSecurityProto_Type(Integer32):
    """Custom type anxpPppSecurityProto based on Integer32"""
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
        *(("chap", 3),
          ("chap-pap", 4),
          ("none", 1),
          ("pap", 2))
    )


_AnxpPppSecurityProto_Type.__name__ = "Integer32"
_AnxpPppSecurityProto_Object = MibTableColumn
anxpPppSecurityProto = _AnxpPppSecurityProto_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 63),
    _AnxpPppSecurityProto_Type()
)
anxpPppSecurityProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppSecurityProto.setStatus("mandatory")


class _AnxpPppUserRemote_Type(DisplayString):
    """Custom type anxpPppUserRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxpPppUserRemote_Type.__name__ = "DisplayString"
_AnxpPppUserRemote_Object = MibTableColumn
anxpPppUserRemote = _AnxpPppUserRemote_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 64),
    _AnxpPppUserRemote_Type()
)
anxpPppUserRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppUserRemote.setStatus("mandatory")


class _AnxpPppPasswdRemote_Type(DisplayString):
    """Custom type anxpPppPasswdRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxpPppPasswdRemote_Type.__name__ = "DisplayString"
_AnxpPppPasswdRemote_Object = MibTableColumn
anxpPppPasswdRemote = _AnxpPppPasswdRemote_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 65),
    _AnxpPppPasswdRemote_Type()
)
anxpPppPasswdRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppPasswdRemote.setStatus("mandatory")


class _AnxpLatAuthGroupVal_Type(DisplayString):
    """Custom type anxpLatAuthGroupVal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 610),
    )


_AnxpLatAuthGroupVal_Type.__name__ = "DisplayString"
_AnxpLatAuthGroupVal_Object = MibTableColumn
anxpLatAuthGroupVal = _AnxpLatAuthGroupVal_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 66),
    _AnxpLatAuthGroupVal_Type()
)
anxpLatAuthGroupVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpLatAuthGroupVal.setStatus("mandatory")


class _AnxpPppDialupAddr_Type(Integer32):
    """Custom type anxpPppDialupAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("authserver", 2),
          ("dhcp", 3),
          ("local", 1))
    )


_AnxpPppDialupAddr_Type.__name__ = "Integer32"
_AnxpPppDialupAddr_Object = MibTableColumn
anxpPppDialupAddr = _AnxpPppDialupAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 67),
    _AnxpPppDialupAddr_Type()
)
anxpPppDialupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppDialupAddr.setStatus("mandatory")


class _AnxpBanner_Type(Integer32):
    """Custom type anxpBanner based on Integer32"""
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
        *(("aftersec", 4),
          ("beforesec", 3),
          ("disabled", 2),
          ("enabled", 1),
          ("motd_after_sec", 6),
          ("motd_before_sec", 5))
    )


_AnxpBanner_Type.__name__ = "Integer32"
_AnxpBanner_Object = MibTableColumn
anxpBanner = _AnxpBanner_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 68),
    _AnxpBanner_Type()
)
anxpBanner.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpBanner.setStatus("mandatory")


class _AnxpPsHistory_Type(Integer32):
    """Custom type anxpPsHistory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AnxpPsHistory_Type.__name__ = "Integer32"
_AnxpPsHistory_Object = MibTableColumn
anxpPsHistory = _AnxpPsHistory_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 69),
    _AnxpPsHistory_Type()
)
anxpPsHistory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPsHistory.setStatus("mandatory")


class _AnxpLocation_Type(DisplayString):
    """Custom type anxpLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpLocation_Type.__name__ = "DisplayString"
_AnxpLocation_Object = MibTableColumn
anxpLocation = _AnxpLocation_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 70),
    _AnxpLocation_Type()
)
anxpLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpLocation.setStatus("mandatory")


class _AnxpType_Type(Integer32):
    """Custom type anxpType based on Integer32"""
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
        *(("dialin", 2),
          ("hardwired", 1),
          ("modem", 8),
          ("pc", 5),
          ("printer", 7),
          ("terminal", 6),
          ("tn3270", 4),
          ("x25", 3))
    )


_AnxpType_Type.__name__ = "Integer32"
_AnxpType_Object = MibTableColumn
anxpType = _AnxpType_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 71),
    _AnxpType_Type()
)
anxpType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpType.setStatus("mandatory")


class _AnxpCliImask7_Type(Integer32):
    """Custom type anxpCliImask7 based on Integer32"""
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


_AnxpCliImask7_Type.__name__ = "Integer32"
_AnxpCliImask7_Object = MibTableColumn
anxpCliImask7 = _AnxpCliImask7_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 72),
    _AnxpCliImask7_Type()
)
anxpCliImask7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCliImask7.setStatus("mandatory")


class _AnxpModemVar_Type(DisplayString):
    """Custom type anxpModemVar based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpModemVar_Type.__name__ = "DisplayString"
_AnxpModemVar_Object = MibTableColumn
anxpModemVar = _AnxpModemVar_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 73),
    _AnxpModemVar_Type()
)
anxpModemVar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpModemVar.setStatus("mandatory")


class _AnxpPppNcp_Type(Integer32):
    """Custom type anxpPppNcp based on Integer32"""
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
        *(("all", 3),
          ("atcp", 2),
          ("atcp-ccp", 10),
          ("atcp-ipxcp", 7),
          ("atcp-ipxcp-ccp", 14),
          ("ipcp", 1),
          ("ipcp-atcp", 5),
          ("ipcp-atcp-ccp", 12),
          ("ipcp-atcp-ipxcp", 8),
          ("ipcp-atcp-ipxcp-ccp", 15),
          ("ipcp-ccp", 9),
          ("ipcp-ipxcp", 6),
          ("ipcp-ipxcp-ccp", 13),
          ("ipxcp", 4),
          ("ipxcp-ccp", 11))
    )


_AnxpPppNcp_Type.__name__ = "Integer32"
_AnxpPppNcp_Object = MibTableColumn
anxpPppNcp = _AnxpPppNcp_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 74),
    _AnxpPppNcp_Type()
)
anxpPppNcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppNcp.setStatus("mandatory")


class _AnxpDemandDial_Type(Integer32):
    """Custom type anxpDemandDial based on Integer32"""
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


_AnxpDemandDial_Type.__name__ = "Integer32"
_AnxpDemandDial_Object = MibTableColumn
anxpDemandDial = _AnxpDemandDial_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 75),
    _AnxpDemandDial_Type()
)
anxpDemandDial.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpDemandDial.setStatus("deprecated")


class _AnxpPhoneNumber_Type(DisplayString):
    """Custom type anxpPhoneNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AnxpPhoneNumber_Type.__name__ = "DisplayString"
_AnxpPhoneNumber_Object = MibTableColumn
anxpPhoneNumber = _AnxpPhoneNumber_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 76),
    _AnxpPhoneNumber_Type()
)
anxpPhoneNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPhoneNumber.setStatus("mandatory")


class _AnxpNetInactivity_Type(Integer32):
    """Custom type anxpNetInactivity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpNetInactivity_Type.__name__ = "Integer32"
_AnxpNetInactivity_Object = MibTableColumn
anxpNetInactivity = _AnxpNetInactivity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 77),
    _AnxpNetInactivity_Type()
)
anxpNetInactivity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNetInactivity.setStatus("mandatory")


class _AnxpAtGuest_Type(Integer32):
    """Custom type anxpAtGuest based on Integer32"""
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


_AnxpAtGuest_Type.__name__ = "Integer32"
_AnxpAtGuest_Object = MibTableColumn
anxpAtGuest = _AnxpAtGuest_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 78),
    _AnxpAtGuest_Type()
)
anxpAtGuest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAtGuest.setStatus("mandatory")


class _AnxpAtNodeid_Type(DisplayString):
    """Custom type anxpAtNodeid based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 11),
    )


_AnxpAtNodeid_Type.__name__ = "DisplayString"
_AnxpAtNodeid_Object = MibTableColumn
anxpAtNodeid = _AnxpAtNodeid_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 79),
    _AnxpAtNodeid_Type()
)
anxpAtNodeid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAtNodeid.setStatus("mandatory")


class _AnxpAtSecurity_Type(Integer32):
    """Custom type anxpAtSecurity based on Integer32"""
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


_AnxpAtSecurity_Type.__name__ = "Integer32"
_AnxpAtSecurity_Object = MibTableColumn
anxpAtSecurity = _AnxpAtSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 80),
    _AnxpAtSecurity_Type()
)
anxpAtSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAtSecurity.setStatus("mandatory")


class _AnxpArapV42bis_Type(Integer32):
    """Custom type anxpArapV42bis based on Integer32"""
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


_AnxpArapV42bis_Type.__name__ = "Integer32"
_AnxpArapV42bis_Object = MibTableColumn
anxpArapV42bis = _AnxpArapV42bis_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 81),
    _AnxpArapV42bis_Type()
)
anxpArapV42bis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpArapV42bis.setStatus("mandatory")
_AnxpTn3270PrinterHost_Type = IpAddress
_AnxpTn3270PrinterHost_Object = MibTableColumn
anxpTn3270PrinterHost = _AnxpTn3270PrinterHost_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 82),
    _AnxpTn3270PrinterHost_Type()
)
anxpTn3270PrinterHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpTn3270PrinterHost.setStatus("mandatory")


class _AnxpTn3270PrinterName_Type(DisplayString):
    """Custom type anxpTn3270PrinterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpTn3270PrinterName_Type.__name__ = "DisplayString"
_AnxpTn3270PrinterName_Object = MibTableColumn
anxpTn3270PrinterName = _AnxpTn3270PrinterName_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 83),
    _AnxpTn3270PrinterName_Type()
)
anxpTn3270PrinterName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpTn3270PrinterName.setStatus("mandatory")


class _AnxpTcpKeepAlive_Type(Integer32):
    """Custom type anxpTcpKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpTcpKeepAlive_Type.__name__ = "Integer32"
_AnxpTcpKeepAlive_Object = MibTableColumn
anxpTcpKeepAlive = _AnxpTcpKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 84),
    _AnxpTcpKeepAlive_Type()
)
anxpTcpKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpTcpKeepAlive.setStatus("mandatory")


class _AnxpDtrSignal_Type(Integer32):
    """Custom type anxpDtrSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 3),
          ("unknown", 1))
    )


_AnxpDtrSignal_Type.__name__ = "Integer32"
_AnxpDtrSignal_Object = MibTableColumn
anxpDtrSignal = _AnxpDtrSignal_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 86),
    _AnxpDtrSignal_Type()
)
anxpDtrSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpDtrSignal.setStatus("mandatory")


class _AnxpRtsSignal_Type(Integer32):
    """Custom type anxpRtsSignal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("high", 2),
          ("low", 3),
          ("unknown", 1))
    )


_AnxpRtsSignal_Type.__name__ = "Integer32"
_AnxpRtsSignal_Object = MibTableColumn
anxpRtsSignal = _AnxpRtsSignal_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 87),
    _AnxpRtsSignal_Type()
)
anxpRtsSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpRtsSignal.setStatus("mandatory")


class _AnxpCliInterface_Type(Integer32):
    """Custom type anxpCliInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uci", 1),
          ("vci", 2))
    )


_AnxpCliInterface_Type.__name__ = "Integer32"
_AnxpCliInterface_Object = MibTableColumn
anxpCliInterface = _AnxpCliInterface_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 88),
    _AnxpCliInterface_Type()
)
anxpCliInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpCliInterface.setStatus("mandatory")


class _AnxpAutobaud_Type(Integer32):
    """Custom type anxpAutobaud based on Integer32"""
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


_AnxpAutobaud_Type.__name__ = "Integer32"
_AnxpAutobaud_Object = MibTableColumn
anxpAutobaud = _AnxpAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 89),
    _AnxpAutobaud_Type()
)
anxpAutobaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAutobaud.setStatus("mandatory")


class _AnxpDefSessMode_Type(Integer32):
    """Custom type anxpDefSessMode based on Integer32"""
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
        *(("interactive", 1),
          ("passall", 3),
          ("passthru", 2),
          ("transparent", 4))
    )


_AnxpDefSessMode_Type.__name__ = "Integer32"
_AnxpDefSessMode_Object = MibTableColumn
anxpDefSessMode = _AnxpDefSessMode_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 90),
    _AnxpDefSessMode_Type()
)
anxpDefSessMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpDefSessMode.setStatus("mandatory")


class _AnxpIpxSecurity_Type(Integer32):
    """Custom type anxpIpxSecurity based on Integer32"""
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


_AnxpIpxSecurity_Type.__name__ = "Integer32"
_AnxpIpxSecurity_Object = MibTableColumn
anxpIpxSecurity = _AnxpIpxSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 91),
    _AnxpIpxSecurity_Type()
)
anxpIpxSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpIpxSecurity.setStatus("mandatory")


class _AnxpIpsoClass_Type(Integer32):
    """Custom type anxpIpsoClass based on Integer32"""
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
        *(("confidential", 4),
          ("none", 1),
          ("secret", 2),
          ("topsecret", 3),
          ("unclassified", 5))
    )


_AnxpIpsoClass_Type.__name__ = "Integer32"
_AnxpIpsoClass_Object = MibTableColumn
anxpIpsoClass = _AnxpIpsoClass_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 92),
    _AnxpIpsoClass_Type()
)
anxpIpsoClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpIpsoClass.setStatus("mandatory")


class _AnxpVciLoginPortPasswd_Type(Integer32):
    """Custom type anxpVciLoginPortPasswd based on Integer32"""
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


_AnxpVciLoginPortPasswd_Type.__name__ = "Integer32"
_AnxpVciLoginPortPasswd_Object = MibTableColumn
anxpVciLoginPortPasswd = _AnxpVciLoginPortPasswd_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 93),
    _AnxpVciLoginPortPasswd_Type()
)
anxpVciLoginPortPasswd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpVciLoginPortPasswd.setStatus("mandatory")


class _AnxpVciLoginTimeout_Type(Integer32):
    """Custom type anxpVciLoginTimeout based on Integer32"""
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


_AnxpVciLoginTimeout_Type.__name__ = "Integer32"
_AnxpVciLoginTimeout_Object = MibTableColumn
anxpVciLoginTimeout = _AnxpVciLoginTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 94),
    _AnxpVciLoginTimeout_Type()
)
anxpVciLoginTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpVciLoginTimeout.setStatus("mandatory")


class _AnxpDedicatedArgs_Type(DisplayString):
    """Custom type anxpDedicatedArgs based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 100),
    )


_AnxpDedicatedArgs_Type.__name__ = "DisplayString"
_AnxpDedicatedArgs_Object = MibTableColumn
anxpDedicatedArgs = _AnxpDedicatedArgs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 95),
    _AnxpDedicatedArgs_Type()
)
anxpDedicatedArgs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpDedicatedArgs.setStatus("mandatory")


class _AnxpNetInactivityUnits_Type(Integer32):
    """Custom type anxpNetInactivityUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("minutes", 1),
          ("seconds", 2))
    )


_AnxpNetInactivityUnits_Type.__name__ = "Integer32"
_AnxpNetInactivityUnits_Object = MibTableColumn
anxpNetInactivityUnits = _AnxpNetInactivityUnits_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 96),
    _AnxpNetInactivityUnits_Type()
)
anxpNetInactivityUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpNetInactivityUnits.setStatus("mandatory")


class _AnxpResolveProtocol_Type(Integer32):
    """Custom type anxpResolveProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(15,
              17,
              19)
        )
    )
    namedValues = NamedValues(
        *(("any", 19),
          ("connect", 15),
          ("telnet", 17))
    )


_AnxpResolveProtocol_Type.__name__ = "Integer32"
_AnxpResolveProtocol_Object = MibTableColumn
anxpResolveProtocol = _AnxpResolveProtocol_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 97),
    _AnxpResolveProtocol_Type()
)
anxpResolveProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpResolveProtocol.setStatus("mandatory")


class _AnxpForwardKey_Type(DisplayString):
    """Custom type anxpForwardKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpForwardKey_Type.__name__ = "DisplayString"
_AnxpForwardKey_Object = MibTableColumn
anxpForwardKey = _AnxpForwardKey_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 98),
    _AnxpForwardKey_Type()
)
anxpForwardKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpForwardKey.setStatus("mandatory")


class _AnxpBackwardKey_Type(DisplayString):
    """Custom type anxpBackwardKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpBackwardKey_Type.__name__ = "DisplayString"
_AnxpBackwardKey_Object = MibTableColumn
anxpBackwardKey = _AnxpBackwardKey_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 99),
    _AnxpBackwardKey_Type()
)
anxpBackwardKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpBackwardKey.setStatus("mandatory")


class _AnxpPppIpxNetwork_Type(DisplayString):
    """Custom type anxpPppIpxNetwork based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AnxpPppIpxNetwork_Type.__name__ = "DisplayString"
_AnxpPppIpxNetwork_Object = MibTableColumn
anxpPppIpxNetwork = _AnxpPppIpxNetwork_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 100),
    _AnxpPppIpxNetwork_Type()
)
anxpPppIpxNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppIpxNetwork.setStatus("mandatory")


class _AnxpPppIpxNode_Type(DisplayString):
    """Custom type anxpPppIpxNode based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(11, 17),
    )


_AnxpPppIpxNode_Type.__name__ = "DisplayString"
_AnxpPppIpxNode_Object = MibTableColumn
anxpPppIpxNode = _AnxpPppIpxNode_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 101),
    _AnxpPppIpxNode_Type()
)
anxpPppIpxNode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpPppIpxNode.setStatus("mandatory")


class _AnxpLatAuthMap_Type(OctetString):
    """Custom type anxpLatAuthMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AnxpLatAuthMap_Type.__name__ = "OctetString"
_AnxpLatAuthMap_Object = MibTableColumn
anxpLatAuthMap = _AnxpLatAuthMap_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 102),
    _AnxpLatAuthMap_Type()
)
anxpLatAuthMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpLatAuthMap.setStatus("mandatory")


class _AnxpMultiSession_Type(Integer32):
    """Custom type anxpMultiSession based on Integer32"""
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


_AnxpMultiSession_Type.__name__ = "Integer32"
_AnxpMultiSession_Object = MibTableColumn
anxpMultiSession = _AnxpMultiSession_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 103),
    _AnxpMultiSession_Type()
)
anxpMultiSession.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpMultiSession.setStatus("mandatory")


class _AnxpAutoTimeout_Type(Integer32):
    """Custom type anxpAutoTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AnxpAutoTimeout_Type.__name__ = "Integer32"
_AnxpAutoTimeout_Object = MibTableColumn
anxpAutoTimeout = _AnxpAutoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 104),
    _AnxpAutoTimeout_Type()
)
anxpAutoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAutoTimeout.setStatus("mandatory")


class _AnxpAutoPPPSecurity_Type(Integer32):
    """Custom type anxpAutoPPPSecurity based on Integer32"""
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


_AnxpAutoPPPSecurity_Type.__name__ = "Integer32"
_AnxpAutoPPPSecurity_Object = MibTableColumn
anxpAutoPPPSecurity = _AnxpAutoPPPSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 7, 1, 105),
    _AnxpAutoPPPSecurity_Type()
)
anxpAutoPPPSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpAutoPPPSecurity.setStatus("mandatory")
_PortStatsTable_Object = MibTable
portStatsTable = _PortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 8)
)
if mibBuilder.loadTexts:
    portStatsTable.setStatus("mandatory")
_PortStatsEntry_Object = MibTableRow
portStatsEntry = _PortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 8, 1)
)
portStatsEntry.setIndexNames(
    (0, "XYLO-PORTS-MIB", "anxpPortStatsIndex"),
)
if mibBuilder.loadTexts:
    portStatsEntry.setStatus("mandatory")
_AnxpPortStatsIndex_Type = Integer32
_AnxpPortStatsIndex_Object = MibTableColumn
anxpPortStatsIndex = _AnxpPortStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 8, 1, 1),
    _AnxpPortStatsIndex_Type()
)
anxpPortStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpPortStatsIndex.setStatus("mandatory")


class _AnxpCurrentUserName_Type(DisplayString):
    """Custom type anxpCurrentUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AnxpCurrentUserName_Type.__name__ = "DisplayString"
_AnxpCurrentUserName_Object = MibTableColumn
anxpCurrentUserName = _AnxpCurrentUserName_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 8, 1, 2),
    _AnxpCurrentUserName_Type()
)
anxpCurrentUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpCurrentUserName.setStatus("mandatory")


class _AnxpPortIdleTime_Type(DisplayString):
    """Custom type anxpPortIdleTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpPortIdleTime_Type.__name__ = "DisplayString"
_AnxpPortIdleTime_Object = MibTableColumn
anxpPortIdleTime = _AnxpPortIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 8, 1, 3),
    _AnxpPortIdleTime_Type()
)
anxpPortIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpPortIdleTime.setStatus("mandatory")


class _AnxpPortLoginTime_Type(DisplayString):
    """Custom type anxpPortLoginTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxpPortLoginTime_Type.__name__ = "DisplayString"
_AnxpPortLoginTime_Object = MibTableColumn
anxpPortLoginTime = _AnxpPortLoginTime_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 8, 1, 4),
    _AnxpPortLoginTime_Type()
)
anxpPortLoginTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpPortLoginTime.setStatus("mandatory")


class _AnxpPortProto_Type(Integer32):
    """Custom type anxpPortProto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
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
        *(("arap", 10),
          ("cli", 1),
          ("dp", 6),
          ("dyndial", 14),
          ("ftp", 11),
          ("ipx", 13),
          ("lpd", 8),
          ("ndp", 12),
          ("ppp", 9),
          ("psvr", 2),
          ("slip", 7),
          ("vcli", 5))
    )


_AnxpPortProto_Type.__name__ = "Integer32"
_AnxpPortProto_Object = MibTableColumn
anxpPortProto = _AnxpPortProto_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 8, 1, 5),
    _AnxpPortProto_Type()
)
anxpPortProto.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpPortProto.setStatus("mandatory")
_AnxpPortJobs_Type = DisplayString
_AnxpPortJobs_Object = MibTableColumn
anxpPortJobs = _AnxpPortJobs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 3, 8, 1, 6),
    _AnxpPortJobs_Type()
)
anxpPortJobs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpPortJobs.setStatus("mandatory")
_AnxpParaPorts_Type = Integer32
_AnxpParaPorts_Object = MibScalar
anxpParaPorts = _AnxpParaPorts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 1),
    _AnxpParaPorts_Type()
)
anxpParaPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpParaPorts.setStatus("mandatory")
_AnxpParaPortTable_Object = MibTable
anxpParaPortTable = _AnxpParaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2)
)
if mibBuilder.loadTexts:
    anxpParaPortTable.setStatus("mandatory")
_AnxpParaPortEntry_Object = MibTableRow
anxpParaPortEntry = _AnxpParaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1)
)
anxpParaPortEntry.setIndexNames(
    (0, "XYLO-PORTS-MIB", "anxpParaPortIndex"),
)
if mibBuilder.loadTexts:
    anxpParaPortEntry.setStatus("mandatory")
_AnxpParaPortIndex_Type = Integer32
_AnxpParaPortIndex_Object = MibTableColumn
anxpParaPortIndex = _AnxpParaPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 1),
    _AnxpParaPortIndex_Type()
)
anxpParaPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpParaPortIndex.setStatus("mandatory")


class _AnxpParaPortHardwareTabs_Type(Integer32):
    """Custom type anxpParaPortHardwareTabs based on Integer32"""
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


_AnxpParaPortHardwareTabs_Type.__name__ = "Integer32"
_AnxpParaPortHardwareTabs_Object = MibTableColumn
anxpParaPortHardwareTabs = _AnxpParaPortHardwareTabs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 2),
    _AnxpParaPortHardwareTabs_Type()
)
anxpParaPortHardwareTabs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortHardwareTabs.setStatus("mandatory")


class _AnxpParaPortMapToUpper_Type(Integer32):
    """Custom type anxpParaPortMapToUpper based on Integer32"""
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


_AnxpParaPortMapToUpper_Type.__name__ = "Integer32"
_AnxpParaPortMapToUpper_Object = MibTableColumn
anxpParaPortMapToUpper = _AnxpParaPortMapToUpper_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 3),
    _AnxpParaPortMapToUpper_Type()
)
anxpParaPortMapToUpper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortMapToUpper.setStatus("mandatory")


class _AnxpParaPortPrinterWidth_Type(Integer32):
    """Custom type anxpParaPortPrinterWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 132),
    )


_AnxpParaPortPrinterWidth_Type.__name__ = "Integer32"
_AnxpParaPortPrinterWidth_Object = MibTableColumn
anxpParaPortPrinterWidth = _AnxpParaPortPrinterWidth_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 4),
    _AnxpParaPortPrinterWidth_Type()
)
anxpParaPortPrinterWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortPrinterWidth.setStatus("mandatory")


class _AnxpParaPortInterface_Type(Integer32):
    """Custom type anxpParaPortInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("centronics", 1),
          ("dataproducts", 2))
    )


_AnxpParaPortInterface_Type.__name__ = "Integer32"
_AnxpParaPortInterface_Object = MibTableColumn
anxpParaPortInterface = _AnxpParaPortInterface_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 5),
    _AnxpParaPortInterface_Type()
)
anxpParaPortInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortInterface.setStatus("mandatory")


class _AnxpParaPortSpeed_Type(Integer32):
    """Custom type anxpParaPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("high-speed", 2),
          ("normal", 1))
    )


_AnxpParaPortSpeed_Type.__name__ = "Integer32"
_AnxpParaPortSpeed_Object = MibTableColumn
anxpParaPortSpeed = _AnxpParaPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 6),
    _AnxpParaPortSpeed_Type()
)
anxpParaPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortSpeed.setStatus("mandatory")


class _AnxpParaPortCRLF_Type(Integer32):
    """Custom type anxpParaPortCRLF based on Integer32"""
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


_AnxpParaPortCRLF_Type.__name__ = "Integer32"
_AnxpParaPortCRLF_Object = MibTableColumn
anxpParaPortCRLF = _AnxpParaPortCRLF_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 7),
    _AnxpParaPortCRLF_Type()
)
anxpParaPortCRLF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortCRLF.setStatus("mandatory")


class _AnxpParaPortTcpKeepAlive_Type(Integer32):
    """Custom type anxpParaPortTcpKeepAlive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AnxpParaPortTcpKeepAlive_Type.__name__ = "Integer32"
_AnxpParaPortTcpKeepAlive_Object = MibTableColumn
anxpParaPortTcpKeepAlive = _AnxpParaPortTcpKeepAlive_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 4, 2, 1, 8),
    _AnxpParaPortTcpKeepAlive_Type()
)
anxpParaPortTcpKeepAlive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpParaPortTcpKeepAlive.setStatus("mandatory")
_TotalSyncPorts_Type = Integer32
_TotalSyncPorts_Object = MibScalar
totalSyncPorts = _TotalSyncPorts_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 1),
    _TotalSyncPorts_Type()
)
totalSyncPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSyncPorts.setStatus("mandatory")
_TotalSyncInChars_Type = Counter32
_TotalSyncInChars_Object = MibScalar
totalSyncInChars = _TotalSyncInChars_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 2),
    _TotalSyncInChars_Type()
)
totalSyncInChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSyncInChars.setStatus("mandatory")
_TotalSyncOutChars_Type = Counter32
_TotalSyncOutChars_Object = MibScalar
totalSyncOutChars = _TotalSyncOutChars_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 3),
    _TotalSyncOutChars_Type()
)
totalSyncOutChars.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSyncOutChars.setStatus("mandatory")
_TotalSyncFrameCheckErrs_Type = Counter32
_TotalSyncFrameCheckErrs_Object = MibScalar
totalSyncFrameCheckErrs = _TotalSyncFrameCheckErrs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 4),
    _TotalSyncFrameCheckErrs_Type()
)
totalSyncFrameCheckErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSyncFrameCheckErrs.setStatus("mandatory")
_TotalSyncXmitUnderrunErrs_Type = Counter32
_TotalSyncXmitUnderrunErrs_Object = MibScalar
totalSyncXmitUnderrunErrs = _TotalSyncXmitUnderrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 5),
    _TotalSyncXmitUnderrunErrs_Type()
)
totalSyncXmitUnderrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSyncXmitUnderrunErrs.setStatus("mandatory")
_TotalSyncRecvOverrunErrs_Type = Counter32
_TotalSyncRecvOverrunErrs_Object = MibScalar
totalSyncRecvOverrunErrs = _TotalSyncRecvOverrunErrs_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 6),
    _TotalSyncRecvOverrunErrs_Type()
)
totalSyncRecvOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    totalSyncRecvOverrunErrs.setStatus("mandatory")
_AnxSyncTable_Object = MibTable
anxSyncTable = _AnxSyncTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7)
)
if mibBuilder.loadTexts:
    anxSyncTable.setStatus("mandatory")
_AnxSyncEntry_Object = MibTableRow
anxSyncEntry = _AnxSyncEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1)
)
anxSyncEntry.setIndexNames(
    (0, "XYLO-PORTS-MIB", "anxSyncPortIndex"),
)
if mibBuilder.loadTexts:
    anxSyncEntry.setStatus("mandatory")
_AnxSyncPortIndex_Type = Integer32
_AnxSyncPortIndex_Object = MibTableColumn
anxSyncPortIndex = _AnxSyncPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 1),
    _AnxSyncPortIndex_Type()
)
anxSyncPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxSyncPortIndex.setStatus("mandatory")


class _AnxSyncMode_Type(Integer32):
    """Custom type anxSyncMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ppp", 2),
          ("unused", 1))
    )


_AnxSyncMode_Type.__name__ = "Integer32"
_AnxSyncMode_Object = MibTableColumn
anxSyncMode = _AnxSyncMode_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 2),
    _AnxSyncMode_Type()
)
anxSyncMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncMode.setStatus("mandatory")


class _AnxSyncClocking_Type(DisplayString):
    """Custom type anxSyncClocking based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 8),
    )


_AnxSyncClocking_Type.__name__ = "DisplayString"
_AnxSyncClocking_Object = MibTableColumn
anxSyncClocking = _AnxSyncClocking_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 3),
    _AnxSyncClocking_Type()
)
anxSyncClocking.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncClocking.setStatus("mandatory")


class _AnxSyncLocalUser_Type(DisplayString):
    """Custom type anxSyncLocalUser based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxSyncLocalUser_Type.__name__ = "DisplayString"
_AnxSyncLocalUser_Object = MibTableColumn
anxSyncLocalUser = _AnxSyncLocalUser_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 4),
    _AnxSyncLocalUser_Type()
)
anxSyncLocalUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncLocalUser.setStatus("mandatory")


class _AnxSyncPortPassword_Type(DisplayString):
    """Custom type anxSyncPortPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxSyncPortPassword_Type.__name__ = "DisplayString"
_AnxSyncPortPassword_Object = MibTableColumn
anxSyncPortPassword = _AnxSyncPortPassword_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 5),
    _AnxSyncPortPassword_Type()
)
anxSyncPortPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncPortPassword.setStatus("mandatory")
_AnxSyncLocalAddr_Type = IpAddress
_AnxSyncLocalAddr_Object = MibTableColumn
anxSyncLocalAddr = _AnxSyncLocalAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 6),
    _AnxSyncLocalAddr_Type()
)
anxSyncLocalAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncLocalAddr.setStatus("mandatory")
_AnxSyncRemoteAddr_Type = IpAddress
_AnxSyncRemoteAddr_Object = MibTableColumn
anxSyncRemoteAddr = _AnxSyncRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 7),
    _AnxSyncRemoteAddr_Type()
)
anxSyncRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncRemoteAddr.setStatus("mandatory")


class _AnxSyncMetric_Type(Integer32):
    """Custom type anxSyncMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AnxSyncMetric_Type.__name__ = "Integer32"
_AnxSyncMetric_Object = MibTableColumn
anxSyncMetric = _AnxSyncMetric_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 8),
    _AnxSyncMetric_Type()
)
anxSyncMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncMetric.setStatus("mandatory")


class _AnxSyncAllowCompression_Type(Integer32):
    """Custom type anxSyncAllowCompression based on Integer32"""
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


_AnxSyncAllowCompression_Type.__name__ = "Integer32"
_AnxSyncAllowCompression_Object = MibTableColumn
anxSyncAllowCompression = _AnxSyncAllowCompression_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 9),
    _AnxSyncAllowCompression_Type()
)
anxSyncAllowCompression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncAllowCompression.setStatus("mandatory")


class _AnxSyncPppMru_Type(Integer32):
    """Custom type anxSyncPppMru based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1500),
    )


_AnxSyncPppMru_Type.__name__ = "Integer32"
_AnxSyncPppMru_Object = MibTableColumn
anxSyncPppMru = _AnxSyncPppMru_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 10),
    _AnxSyncPppMru_Type()
)
anxSyncPppMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncPppMru.setStatus("mandatory")


class _AnxSyncPppSecurityProto_Type(Integer32):
    """Custom type anxSyncPppSecurityProto based on Integer32"""
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
        *(("chap", 3),
          ("chappap", 4),
          ("none", 1),
          ("pap", 2))
    )


_AnxSyncPppSecurityProto_Type.__name__ = "Integer32"
_AnxSyncPppSecurityProto_Object = MibTableColumn
anxSyncPppSecurityProto = _AnxSyncPppSecurityProto_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 11),
    _AnxSyncPppSecurityProto_Type()
)
anxSyncPppSecurityProto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncPppSecurityProto.setStatus("mandatory")


class _AnxSyncPppUserRemote_Type(DisplayString):
    """Custom type anxSyncPppUserRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxSyncPppUserRemote_Type.__name__ = "DisplayString"
_AnxSyncPppUserRemote_Object = MibTableColumn
anxSyncPppUserRemote = _AnxSyncPppUserRemote_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 12),
    _AnxSyncPppUserRemote_Type()
)
anxSyncPppUserRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncPppUserRemote.setStatus("mandatory")


class _AnxSyncPppPasswdRemote_Type(DisplayString):
    """Custom type anxSyncPppPasswdRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AnxSyncPppPasswdRemote_Type.__name__ = "DisplayString"
_AnxSyncPppPasswdRemote_Object = MibTableColumn
anxSyncPppPasswdRemote = _AnxSyncPppPasswdRemote_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 13),
    _AnxSyncPppPasswdRemote_Type()
)
anxSyncPppPasswdRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncPppPasswdRemote.setStatus("mandatory")


class _AnxSyncPppNcp_Type(Integer32):
    """Custom type anxSyncPppNcp based on Integer32"""
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
        *(("all", 3),
          ("atcp", 2),
          ("atcp-ccp", 10),
          ("atcp-ipxcp", 7),
          ("atcp-ipxcp-ccp", 14),
          ("ipcp", 1),
          ("ipcp-atcp", 5),
          ("ipcp-atcp-ccp", 12),
          ("ipcp-atcp-ipxcp", 8),
          ("ipcp-atcp-ipxcp-ccp", 15),
          ("ipcp-ccp", 9),
          ("ipcp-ipxcp", 6),
          ("ipcp-ipxcp-ccp", 13),
          ("ipxcp", 4),
          ("ipxcp-ccp", 11))
    )


_AnxSyncPppNcp_Type.__name__ = "Integer32"
_AnxSyncPppNcp_Object = MibTableColumn
anxSyncPppNcp = _AnxSyncPppNcp_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 14),
    _AnxSyncPppNcp_Type()
)
anxSyncPppNcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncPppNcp.setStatus("mandatory")


class _AnxSyncLocation_Type(DisplayString):
    """Custom type anxSyncLocation based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_AnxSyncLocation_Type.__name__ = "DisplayString"
_AnxSyncLocation_Object = MibTableColumn
anxSyncLocation = _AnxSyncLocation_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 15),
    _AnxSyncLocation_Type()
)
anxSyncLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncLocation.setStatus("mandatory")


class _AnxSyncForceCTS_Type(Integer32):
    """Custom type anxSyncForceCTS based on Integer32"""
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


_AnxSyncForceCTS_Type.__name__ = "Integer32"
_AnxSyncForceCTS_Object = MibTableColumn
anxSyncForceCTS = _AnxSyncForceCTS_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 16),
    _AnxSyncForceCTS_Type()
)
anxSyncForceCTS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncForceCTS.setStatus("mandatory")
_AnxSyncSubNetMask_Type = IpAddress
_AnxSyncSubNetMask_Object = MibTableColumn
anxSyncSubNetMask = _AnxSyncSubNetMask_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 17),
    _AnxSyncSubNetMask_Type()
)
anxSyncSubNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncSubNetMask.setStatus("mandatory")


class _AnxSyncDialupAddr_Type(Integer32):
    """Custom type anxSyncDialupAddr based on Integer32"""
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


_AnxSyncDialupAddr_Type.__name__ = "Integer32"
_AnxSyncDialupAddr_Object = MibTableColumn
anxSyncDialupAddr = _AnxSyncDialupAddr_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 18),
    _AnxSyncDialupAddr_Type()
)
anxSyncDialupAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncDialupAddr.setStatus("mandatory")


class _AnxSyncPppSecurity_Type(Integer32):
    """Custom type anxSyncPppSecurity based on Integer32"""
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


_AnxSyncPppSecurity_Type.__name__ = "Integer32"
_AnxSyncPppSecurity_Object = MibTableColumn
anxSyncPppSecurity = _AnxSyncPppSecurity_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 9, 7, 1, 19),
    _AnxSyncPppSecurity_Type()
)
anxSyncPppSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxSyncPppSecurity.setStatus("mandatory")
_AnxmStatsTable_Object = MibTable
anxmStatsTable = _AnxmStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 1)
)
if mibBuilder.loadTexts:
    anxmStatsTable.setStatus("deprecated")
_AnxmStatsEntry_Object = MibTableRow
anxmStatsEntry = _AnxmStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 1, 1)
)
anxmStatsEntry.setIndexNames(
    (0, "XYLO-PORTS-MIB", "anxmStatsIndex"),
)
if mibBuilder.loadTexts:
    anxmStatsEntry.setStatus("deprecated")
_AnxmStatsIndex_Type = Integer32
_AnxmStatsIndex_Object = MibTableColumn
anxmStatsIndex = _AnxmStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 1, 1, 1),
    _AnxmStatsIndex_Type()
)
anxmStatsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxmStatsIndex.setStatus("deprecated")
_AnxmStatsPort_Type = Integer32
_AnxmStatsPort_Object = MibTableColumn
anxmStatsPort = _AnxmStatsPort_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 1, 1, 2),
    _AnxmStatsPort_Type()
)
anxmStatsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxmStatsPort.setStatus("deprecated")


class _AnxmStatsModemType_Type(DisplayString):
    """Custom type anxmStatsModemType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AnxmStatsModemType_Type.__name__ = "DisplayString"
_AnxmStatsModemType_Object = MibTableColumn
anxmStatsModemType = _AnxmStatsModemType_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 1, 1, 3),
    _AnxmStatsModemType_Type()
)
anxmStatsModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxmStatsModemType.setStatus("deprecated")
_AnxmStatsTime_Type = DisplayString
_AnxmStatsTime_Object = MibTableColumn
anxmStatsTime = _AnxmStatsTime_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 1, 1, 4),
    _AnxmStatsTime_Type()
)
anxmStatsTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxmStatsTime.setStatus("deprecated")


class _AnxmStatsNumber_Type(DisplayString):
    """Custom type anxmStatsNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_AnxmStatsNumber_Type.__name__ = "DisplayString"
_AnxmStatsNumber_Object = MibTableColumn
anxmStatsNumber = _AnxmStatsNumber_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 1, 1, 5),
    _AnxmStatsNumber_Type()
)
anxmStatsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxmStatsNumber.setStatus("deprecated")
_AnxmStatsDuration_Type = TimeTicks
_AnxmStatsDuration_Object = MibTableColumn
anxmStatsDuration = _AnxmStatsDuration_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 1, 1, 6),
    _AnxmStatsDuration_Type()
)
anxmStatsDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxmStatsDuration.setStatus("deprecated")


class _AnxmStatsUsername_Type(DisplayString):
    """Custom type anxmStatsUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 32),
    )


_AnxmStatsUsername_Type.__name__ = "DisplayString"
_AnxmStatsUsername_Object = MibTableColumn
anxmStatsUsername = _AnxmStatsUsername_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 1, 1, 7),
    _AnxmStatsUsername_Type()
)
anxmStatsUsername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxmStatsUsername.setStatus("deprecated")


class _AnxmStatsStatus_Type(Integer32):
    """Custom type anxmStatsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("exitAbort", 3),
          ("exitNormal", 2))
    )


_AnxmStatsStatus_Type.__name__ = "Integer32"
_AnxmStatsStatus_Object = MibTableColumn
anxmStatsStatus = _AnxmStatsStatus_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 1, 1, 8),
    _AnxmStatsStatus_Type()
)
anxmStatsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxmStatsStatus.setStatus("deprecated")
_AnxpModemTable_Object = MibTable
anxpModemTable = _AnxpModemTable_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2)
)
if mibBuilder.loadTexts:
    anxpModemTable.setStatus("mandatory")
_AnxpModemEntry_Object = MibTableRow
anxpModemEntry = _AnxpModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1)
)
anxpModemEntry.setIndexNames(
    (0, "XYLO-PORTS-MIB", "anxpModemIndex"),
)
if mibBuilder.loadTexts:
    anxpModemEntry.setStatus("mandatory")
_AnxpModemIndex_Type = Integer32
_AnxpModemIndex_Object = MibTableColumn
anxpModemIndex = _AnxpModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 1),
    _AnxpModemIndex_Type()
)
anxpModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpModemIndex.setStatus("mandatory")


class _AnxpModemConfig_Type(Integer32):
    """Custom type anxpModemConfig based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("autoadapt", 9),
          ("autodetect", 8),
          ("dialin", 4),
          ("dialinautobaud", 3),
          ("dialinout", 6),
          ("dialinoutautobaud", 5),
          ("dialout", 7),
          ("ipx", 10),
          ("none", 2),
          ("unknown", 1))
    )


_AnxpModemConfig_Type.__name__ = "Integer32"
_AnxpModemConfig_Object = MibTableColumn
anxpModemConfig = _AnxpModemConfig_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 2),
    _AnxpModemConfig_Type()
)
anxpModemConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpModemConfig.setStatus("mandatory")


class _AnxpModemReset_Type(Integer32):
    """Custom type anxpModemReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("ready", 1))
    )


_AnxpModemReset_Type.__name__ = "Integer32"
_AnxpModemReset_Object = MibTableColumn
anxpModemReset = _AnxpModemReset_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 3),
    _AnxpModemReset_Type()
)
anxpModemReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpModemReset.setStatus("deprecated")


class _AnxpModemStatus_Type(Integer32):
    """Custom type anxpModemStatus based on Integer32"""
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
        *(("available", 1),
          ("busied-out", 2),
          ("failed", 3),
          ("used", 4))
    )


_AnxpModemStatus_Type.__name__ = "Integer32"
_AnxpModemStatus_Object = MibTableColumn
anxpModemStatus = _AnxpModemStatus_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 4),
    _AnxpModemStatus_Type()
)
anxpModemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    anxpModemStatus.setStatus("deprecated")
_AnxpModemBChannel_Type = Integer32
_AnxpModemBChannel_Object = MibTableColumn
anxpModemBChannel = _AnxpModemBChannel_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 5),
    _AnxpModemBChannel_Type()
)
anxpModemBChannel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpModemBChannel.setStatus("mandatory")
_AnxpModemWhenBusy_Type = Integer32
_AnxpModemWhenBusy_Object = MibTableColumn
anxpModemWhenBusy = _AnxpModemWhenBusy_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 6),
    _AnxpModemWhenBusy_Type()
)
anxpModemWhenBusy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpModemWhenBusy.setStatus("deprecated")
_AnxpModemTotalCalls_Type = Counter32
_AnxpModemTotalCalls_Object = MibTableColumn
anxpModemTotalCalls = _AnxpModemTotalCalls_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 7),
    _AnxpModemTotalCalls_Type()
)
anxpModemTotalCalls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpModemTotalCalls.setStatus("deprecated")
_AnxpModemRingFail_Type = Counter32
_AnxpModemRingFail_Object = MibTableColumn
anxpModemRingFail = _AnxpModemRingFail_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 8),
    _AnxpModemRingFail_Type()
)
anxpModemRingFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpModemRingFail.setStatus("mandatory")
_AnxpModemOffhookFail_Type = Counter32
_AnxpModemOffhookFail_Object = MibTableColumn
anxpModemOffhookFail = _AnxpModemOffhookFail_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 9),
    _AnxpModemOffhookFail_Type()
)
anxpModemOffhookFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpModemOffhookFail.setStatus("mandatory")
_AnxpModemDcdFail_Type = Counter32
_AnxpModemDcdFail_Object = MibTableColumn
anxpModemDcdFail = _AnxpModemDcdFail_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 10),
    _AnxpModemDcdFail_Type()
)
anxpModemDcdFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpModemDcdFail.setStatus("mandatory")
_AnxpModemConsecFail_Type = Counter32
_AnxpModemConsecFail_Object = MibTableColumn
anxpModemConsecFail = _AnxpModemConsecFail_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 11),
    _AnxpModemConsecFail_Type()
)
anxpModemConsecFail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpModemConsecFail.setStatus("mandatory")


class _AnxpModemFirmware_Type(DisplayString):
    """Custom type anxpModemFirmware based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AnxpModemFirmware_Type.__name__ = "DisplayString"
_AnxpModemFirmware_Object = MibTableColumn
anxpModemFirmware = _AnxpModemFirmware_Object(
    (1, 3, 6, 1, 4, 1, 15, 2, 100, 2, 1, 12),
    _AnxpModemFirmware_Type()
)
anxpModemFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    anxpModemFirmware.setStatus("deprecated")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XYLO-PORTS-MIB",
    **{"totalPorts": totalPorts,
       "totalInChars": totalInChars,
       "totalOutChars": totalOutChars,
       "totalParityErrs": totalParityErrs,
       "totalOverrunErrs": totalOverrunErrs,
       "totalFramingErrs": totalFramingErrs,
       "portTable": portTable,
       "portEntry": portEntry,
       "anxpPortIndex": anxpPortIndex,
       "anxpMode": anxpMode,
       "anxpCtrlLines": anxpCtrlLines,
       "anxpBidirModem": anxpBidirModem,
       "anxpAllowBcast": anxpAllowBcast,
       "anxpBcastDirection": anxpBcastDirection,
       "anxpInputStartChar": anxpInputStartChar,
       "anxpInputStopChar": anxpInputStopChar,
       "anxpOutputStartChar": anxpOutputStartChar,
       "anxpOutputStopChar": anxpOutputStopChar,
       "anxpIxanyFlowCtl": anxpIxanyFlowCtl,
       "anxpLongBreak": anxpLongBreak,
       "anxpShortBreak": anxpShortBreak,
       "anxpForwardTimer": anxpForwardTimer,
       "anxpForwardCount": anxpForwardCount,
       "anxpImask7Bits": anxpImask7Bits,
       "anxpAttnChar": anxpAttnChar,
       "anxpInputBufSize": anxpInputBufSize,
       "anxpInputIsActivity": anxpInputIsActivity,
       "anxpOutputIsActivity": anxpOutputIsActivity,
       "anxpInactivityTimer": anxpInactivityTimer,
       "anxpResetIdleTimer": anxpResetIdleTimer,
       "anxpCliInactivity": anxpCliInactivity,
       "anxpCliSecurity": anxpCliSecurity,
       "anxpConnectSecurity": anxpConnectSecurity,
       "anxpPortServerSecurity": anxpPortServerSecurity,
       "anxpPortPassword": anxpPortPassword,
       "anxpUserName": anxpUserName,
       "anxpDedicatedAddr": anxpDedicatedAddr,
       "anxpDedicatedPort": anxpDedicatedPort,
       "anxpPrompt": anxpPrompt,
       "anxpTermVar": anxpTermVar,
       "anxpNewLineTerm": anxpNewLineTerm,
       "anxpEcho": anxpEcho,
       "anxpMapToLower": anxpMapToLower,
       "anxpMapToUpper": anxpMapToUpper,
       "anxpHardwareTabs": anxpHardwareTabs,
       "anxpCharErase": anxpCharErase,
       "anxpLineErase": anxpLineErase,
       "anxpEraseChar": anxpEraseChar,
       "anxpEraseWord": anxpEraseWord,
       "anxpEraseLine": anxpEraseLine,
       "anxpRedisplayLine": anxpRedisplayLine,
       "anxpToggleOutput": anxpToggleOutput,
       "anxpTelnetEscape": anxpTelnetEscape,
       "anxpNeedDsr": anxpNeedDsr,
       "anxpTelnetCRLF": anxpTelnetCRLF,
       "anxpLatbEnable": anxpLatbEnable,
       "anxpSlipSecure": anxpSlipSecure,
       "anxpNetLocalAddr": anxpNetLocalAddr,
       "anxpNetRemoteAddr": anxpNetRemoteAddr,
       "anxpSlipSubnetMask": anxpSlipSubnetMask,
       "anxpSlipLoadDumpHost": anxpSlipLoadDumpHost,
       "anxpNetMetric": anxpNetMetric,
       "anxpSlipAllowDump": anxpSlipAllowDump,
       "anxpDoCompression": anxpDoCompression,
       "anxpAllowCompression": anxpAllowCompression,
       "anxpSlipMtuSize": anxpSlipMtuSize,
       "anxpSlipNoIcmp": anxpSlipNoIcmp,
       "anxpSlipTos": anxpSlipTos,
       "anxpPppMru": anxpPppMru,
       "anxpPppAcm": anxpPppAcm,
       "anxpPppSecurityProto": anxpPppSecurityProto,
       "anxpPppUserRemote": anxpPppUserRemote,
       "anxpPppPasswdRemote": anxpPppPasswdRemote,
       "anxpLatAuthGroupVal": anxpLatAuthGroupVal,
       "anxpPppDialupAddr": anxpPppDialupAddr,
       "anxpBanner": anxpBanner,
       "anxpPsHistory": anxpPsHistory,
       "anxpLocation": anxpLocation,
       "anxpType": anxpType,
       "anxpCliImask7": anxpCliImask7,
       "anxpModemVar": anxpModemVar,
       "anxpPppNcp": anxpPppNcp,
       "anxpDemandDial": anxpDemandDial,
       "anxpPhoneNumber": anxpPhoneNumber,
       "anxpNetInactivity": anxpNetInactivity,
       "anxpAtGuest": anxpAtGuest,
       "anxpAtNodeid": anxpAtNodeid,
       "anxpAtSecurity": anxpAtSecurity,
       "anxpArapV42bis": anxpArapV42bis,
       "anxpTn3270PrinterHost": anxpTn3270PrinterHost,
       "anxpTn3270PrinterName": anxpTn3270PrinterName,
       "anxpTcpKeepAlive": anxpTcpKeepAlive,
       "anxpDtrSignal": anxpDtrSignal,
       "anxpRtsSignal": anxpRtsSignal,
       "anxpCliInterface": anxpCliInterface,
       "anxpAutobaud": anxpAutobaud,
       "anxpDefSessMode": anxpDefSessMode,
       "anxpIpxSecurity": anxpIpxSecurity,
       "anxpIpsoClass": anxpIpsoClass,
       "anxpVciLoginPortPasswd": anxpVciLoginPortPasswd,
       "anxpVciLoginTimeout": anxpVciLoginTimeout,
       "anxpDedicatedArgs": anxpDedicatedArgs,
       "anxpNetInactivityUnits": anxpNetInactivityUnits,
       "anxpResolveProtocol": anxpResolveProtocol,
       "anxpForwardKey": anxpForwardKey,
       "anxpBackwardKey": anxpBackwardKey,
       "anxpPppIpxNetwork": anxpPppIpxNetwork,
       "anxpPppIpxNode": anxpPppIpxNode,
       "anxpLatAuthMap": anxpLatAuthMap,
       "anxpMultiSession": anxpMultiSession,
       "anxpAutoTimeout": anxpAutoTimeout,
       "anxpAutoPPPSecurity": anxpAutoPPPSecurity,
       "portStatsTable": portStatsTable,
       "portStatsEntry": portStatsEntry,
       "anxpPortStatsIndex": anxpPortStatsIndex,
       "anxpCurrentUserName": anxpCurrentUserName,
       "anxpPortIdleTime": anxpPortIdleTime,
       "anxpPortLoginTime": anxpPortLoginTime,
       "anxpPortProto": anxpPortProto,
       "anxpPortJobs": anxpPortJobs,
       "anxpParaPorts": anxpParaPorts,
       "anxpParaPortTable": anxpParaPortTable,
       "anxpParaPortEntry": anxpParaPortEntry,
       "anxpParaPortIndex": anxpParaPortIndex,
       "anxpParaPortHardwareTabs": anxpParaPortHardwareTabs,
       "anxpParaPortMapToUpper": anxpParaPortMapToUpper,
       "anxpParaPortPrinterWidth": anxpParaPortPrinterWidth,
       "anxpParaPortInterface": anxpParaPortInterface,
       "anxpParaPortSpeed": anxpParaPortSpeed,
       "anxpParaPortCRLF": anxpParaPortCRLF,
       "anxpParaPortTcpKeepAlive": anxpParaPortTcpKeepAlive,
       "totalSyncPorts": totalSyncPorts,
       "totalSyncInChars": totalSyncInChars,
       "totalSyncOutChars": totalSyncOutChars,
       "totalSyncFrameCheckErrs": totalSyncFrameCheckErrs,
       "totalSyncXmitUnderrunErrs": totalSyncXmitUnderrunErrs,
       "totalSyncRecvOverrunErrs": totalSyncRecvOverrunErrs,
       "anxSyncTable": anxSyncTable,
       "anxSyncEntry": anxSyncEntry,
       "anxSyncPortIndex": anxSyncPortIndex,
       "anxSyncMode": anxSyncMode,
       "anxSyncClocking": anxSyncClocking,
       "anxSyncLocalUser": anxSyncLocalUser,
       "anxSyncPortPassword": anxSyncPortPassword,
       "anxSyncLocalAddr": anxSyncLocalAddr,
       "anxSyncRemoteAddr": anxSyncRemoteAddr,
       "anxSyncMetric": anxSyncMetric,
       "anxSyncAllowCompression": anxSyncAllowCompression,
       "anxSyncPppMru": anxSyncPppMru,
       "anxSyncPppSecurityProto": anxSyncPppSecurityProto,
       "anxSyncPppUserRemote": anxSyncPppUserRemote,
       "anxSyncPppPasswdRemote": anxSyncPppPasswdRemote,
       "anxSyncPppNcp": anxSyncPppNcp,
       "anxSyncLocation": anxSyncLocation,
       "anxSyncForceCTS": anxSyncForceCTS,
       "anxSyncSubNetMask": anxSyncSubNetMask,
       "anxSyncDialupAddr": anxSyncDialupAddr,
       "anxSyncPppSecurity": anxSyncPppSecurity,
       "anxmStatsTable": anxmStatsTable,
       "anxmStatsEntry": anxmStatsEntry,
       "anxmStatsIndex": anxmStatsIndex,
       "anxmStatsPort": anxmStatsPort,
       "anxmStatsModemType": anxmStatsModemType,
       "anxmStatsTime": anxmStatsTime,
       "anxmStatsNumber": anxmStatsNumber,
       "anxmStatsDuration": anxmStatsDuration,
       "anxmStatsUsername": anxmStatsUsername,
       "anxmStatsStatus": anxmStatsStatus,
       "anxpModemTable": anxpModemTable,
       "anxpModemEntry": anxpModemEntry,
       "anxpModemIndex": anxpModemIndex,
       "anxpModemConfig": anxpModemConfig,
       "anxpModemReset": anxpModemReset,
       "anxpModemStatus": anxpModemStatus,
       "anxpModemBChannel": anxpModemBChannel,
       "anxpModemWhenBusy": anxpModemWhenBusy,
       "anxpModemTotalCalls": anxpModemTotalCalls,
       "anxpModemRingFail": anxpModemRingFail,
       "anxpModemOffhookFail": anxpModemOffhookFail,
       "anxpModemDcdFail": anxpModemDcdFail,
       "anxpModemConsecFail": anxpModemConsecFail,
       "anxpModemFirmware": anxpModemFirmware}
)
