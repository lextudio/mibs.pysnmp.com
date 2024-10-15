# SNMP MIB module (MRV-IR-CHAR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/MRV-IR-CHAR-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:23:47 2024
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

(TrapSeverity,
 mrvLx) = mibBuilder.importSymbols(
    "MRV-IR-SYSTEM-MIB",
    "TrapSeverity",
    "mrvLx")

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

irCharMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 2)
)


# Types definitions



class IrContactState(Integer32):
    """Custom type IrContactState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("closed", 2),
          ("open", 1))
    )





class IrControlState(Integer32):
    """Custom type IrControlState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("assert", 2),
          ("deassert", 1))
    )





class PortAccessType(Integer32):
    """Custom type PortAccessType based on Integer32"""
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
              16,
              17,
              18,
              19)
        )
    )
    namedValues = NamedValues(
        *(("apd", 6),
          ("control", 9),
          ("dataBuffer", 7),
          ("dynamic", 3),
          ("hdam", 16),
          ("ldam", 17),
          ("local", 1),
          ("lpd", 18),
          ("master", 10),
          ("none", 14),
          ("notify", 13),
          ("power", 4),
          ("ppp", 12),
          ("remote", 2),
          ("sensor", 5),
          ("slave", 11),
          ("tcpPipe", 8),
          ("ups", 19))
    )





class PortSpeed(Integer32):
    """Custom type PortSpeed based on Integer32"""
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
        *(("sp115200", 12),
          ("sp1200", 5),
          ("sp134", 1),
          ("sp19200", 9),
          ("sp200", 2),
          ("sp230400", 13),
          ("sp2400", 6),
          ("sp300", 3),
          ("sp38400", 10),
          ("sp460800", 14),
          ("sp4800", 7),
          ("sp57600", 11),
          ("sp600", 4),
          ("sp921600", 15),
          ("sp9600", 8))
    )





class PortAuthType(Integer32):
    """Custom type PortAuthType based on Integer32"""
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
        *(("ldap", 5),
          ("local", 6),
          ("none", 1),
          ("radius", 3),
          ("securid", 2),
          ("tacacs", 4))
    )





class SignalStatus(Integer32):
    """Custom type SignalStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 2),
          ("up", 1))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IrCharNumber_Type = Integer32
_IrCharNumber_Object = MibScalar
irCharNumber = _IrCharNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 1),
    _IrCharNumber_Type()
)
irCharNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharNumber.setStatus("current")
_IrCharPortTable_Object = MibTable
irCharPortTable = _IrCharPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2)
)
if mibBuilder.loadTexts:
    irCharPortTable.setStatus("current")
_IrCharPortEntry_Object = MibTableRow
irCharPortEntry = _IrCharPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1)
)
irCharPortEntry.setIndexNames(
    (0, "MRV-IR-CHAR-MIB", "irCharPortIndex"),
)
if mibBuilder.loadTexts:
    irCharPortEntry.setStatus("current")
_IrCharPortIndex_Type = Integer32
_IrCharPortIndex_Object = MibTableColumn
irCharPortIndex = _IrCharPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 1),
    _IrCharPortIndex_Type()
)
irCharPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortIndex.setStatus("current")
_IrCharPortAccessType_Type = PortAccessType
_IrCharPortAccessType_Object = MibTableColumn
irCharPortAccessType = _IrCharPortAccessType_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 2),
    _IrCharPortAccessType_Type()
)
irCharPortAccessType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortAccessType.setStatus("current")


class _IrCharPortFlowControl_Type(Integer32):
    """Custom type irCharPortFlowControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cts", 3),
          ("none", 1),
          ("xon", 2))
    )


_IrCharPortFlowControl_Type.__name__ = "Integer32"
_IrCharPortFlowControl_Object = MibTableColumn
irCharPortFlowControl = _IrCharPortFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 3),
    _IrCharPortFlowControl_Type()
)
irCharPortFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortFlowControl.setStatus("current")


class _IrCharPortStopBits_Type(Integer32):
    """Custom type irCharPortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IrCharPortStopBits_Type.__name__ = "Integer32"
_IrCharPortStopBits_Object = MibTableColumn
irCharPortStopBits = _IrCharPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 4),
    _IrCharPortStopBits_Type()
)
irCharPortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortStopBits.setStatus("current")


class _IrCharPortParity_Type(Integer32):
    """Custom type irCharPortParity based on Integer32"""
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
        *(("even", 3),
          ("mark", 4),
          ("none", 1),
          ("odd", 2),
          ("space", 5))
    )


_IrCharPortParity_Type.__name__ = "Integer32"
_IrCharPortParity_Object = MibTableColumn
irCharPortParity = _IrCharPortParity_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 5),
    _IrCharPortParity_Type()
)
irCharPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortParity.setStatus("current")


class _IrCharPortBitsPerChar_Type(Integer32):
    """Custom type irCharPortBitsPerChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(7, 8),
    )


_IrCharPortBitsPerChar_Type.__name__ = "Integer32"
_IrCharPortBitsPerChar_Object = MibTableColumn
irCharPortBitsPerChar = _IrCharPortBitsPerChar_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 6),
    _IrCharPortBitsPerChar_Type()
)
irCharPortBitsPerChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortBitsPerChar.setStatus("current")


class _IrCharPortAutoDial_Type(Integer32):
    """Custom type irCharPortAutoDial based on Integer32"""
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


_IrCharPortAutoDial_Type.__name__ = "Integer32"
_IrCharPortAutoDial_Object = MibTableColumn
irCharPortAutoDial = _IrCharPortAutoDial_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 7),
    _IrCharPortAutoDial_Type()
)
irCharPortAutoDial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortAutoDial.setStatus("deprecated")


class _IrCharPortAutoHangup_Type(Integer32):
    """Custom type irCharPortAutoHangup based on Integer32"""
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


_IrCharPortAutoHangup_Type.__name__ = "Integer32"
_IrCharPortAutoHangup_Object = MibTableColumn
irCharPortAutoHangup = _IrCharPortAutoHangup_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 8),
    _IrCharPortAutoHangup_Type()
)
irCharPortAutoHangup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortAutoHangup.setStatus("current")


class _IrCharPortAutobaud_Type(Integer32):
    """Custom type irCharPortAutobaud based on Integer32"""
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


_IrCharPortAutobaud_Type.__name__ = "Integer32"
_IrCharPortAutobaud_Object = MibTableColumn
irCharPortAutobaud = _IrCharPortAutobaud_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 9),
    _IrCharPortAutobaud_Type()
)
irCharPortAutobaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortAutobaud.setStatus("current")


class _IrCharPortAutobaudRetry_Type(Integer32):
    """Custom type irCharPortAutobaudRetry based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IrCharPortAutobaudRetry_Type.__name__ = "Integer32"
_IrCharPortAutobaudRetry_Object = MibTableColumn
irCharPortAutobaudRetry = _IrCharPortAutobaudRetry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 10),
    _IrCharPortAutobaudRetry_Type()
)
irCharPortAutobaudRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortAutobaudRetry.setStatus("current")
_IrCharPortInSignalCts_Type = SignalStatus
_IrCharPortInSignalCts_Object = MibTableColumn
irCharPortInSignalCts = _IrCharPortInSignalCts_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 11),
    _IrCharPortInSignalCts_Type()
)
irCharPortInSignalCts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortInSignalCts.setStatus("current")
_IrCharPortInSignalDsr_Type = SignalStatus
_IrCharPortInSignalDsr_Object = MibTableColumn
irCharPortInSignalDsr = _IrCharPortInSignalDsr_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 12),
    _IrCharPortInSignalDsr_Type()
)
irCharPortInSignalDsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortInSignalDsr.setStatus("current")
_IrCharPortInSignalDcd_Type = SignalStatus
_IrCharPortInSignalDcd_Object = MibTableColumn
irCharPortInSignalDcd = _IrCharPortInSignalDcd_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 13),
    _IrCharPortInSignalDcd_Type()
)
irCharPortInSignalDcd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortInSignalDcd.setStatus("current")
_IrCharPortOutSignalRts_Type = SignalStatus
_IrCharPortOutSignalRts_Object = MibTableColumn
irCharPortOutSignalRts = _IrCharPortOutSignalRts_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 14),
    _IrCharPortOutSignalRts_Type()
)
irCharPortOutSignalRts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortOutSignalRts.setStatus("current")
_IrCharPortOutSignalDtr_Type = SignalStatus
_IrCharPortOutSignalDtr_Object = MibTableColumn
irCharPortOutSignalDtr = _IrCharPortOutSignalDtr_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 15),
    _IrCharPortOutSignalDtr_Type()
)
irCharPortOutSignalDtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortOutSignalDtr.setStatus("current")
_IrCharPortSpeed_Type = PortSpeed
_IrCharPortSpeed_Object = MibTableColumn
irCharPortSpeed = _IrCharPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 16),
    _IrCharPortSpeed_Type()
)
irCharPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortSpeed.setStatus("current")


class _IrCharPortPrompt_Type(DisplayString):
    """Custom type irCharPortPrompt based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IrCharPortPrompt_Type.__name__ = "DisplayString"
_IrCharPortPrompt_Object = MibTableColumn
irCharPortPrompt = _IrCharPortPrompt_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 17),
    _IrCharPortPrompt_Type()
)
irCharPortPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortPrompt.setStatus("current")


class _IrCharPortBreak_Type(Integer32):
    """Custom type irCharPortBreak based on Integer32"""
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


_IrCharPortBreak_Type.__name__ = "Integer32"
_IrCharPortBreak_Object = MibTableColumn
irCharPortBreak = _IrCharPortBreak_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 18),
    _IrCharPortBreak_Type()
)
irCharPortBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortBreak.setStatus("current")


class _IrCharPortSpecialBreakString_Type(DisplayString):
    """Custom type irCharPortSpecialBreakString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 7),
    )


_IrCharPortSpecialBreakString_Type.__name__ = "DisplayString"
_IrCharPortSpecialBreakString_Object = MibTableColumn
irCharPortSpecialBreakString = _IrCharPortSpecialBreakString_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 19),
    _IrCharPortSpecialBreakString_Type()
)
irCharPortSpecialBreakString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortSpecialBreakString.setStatus("current")


class _IrCharPortSpecialBreak_Type(Integer32):
    """Custom type irCharPortSpecialBreak based on Integer32"""
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


_IrCharPortSpecialBreak_Type.__name__ = "Integer32"
_IrCharPortSpecialBreak_Object = MibTableColumn
irCharPortSpecialBreak = _IrCharPortSpecialBreak_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 20),
    _IrCharPortSpecialBreak_Type()
)
irCharPortSpecialBreak.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortSpecialBreak.setStatus("current")
_IrCharPortInboundAuth_Type = PortAuthType
_IrCharPortInboundAuth_Object = MibTableColumn
irCharPortInboundAuth = _IrCharPortInboundAuth_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 21),
    _IrCharPortInboundAuth_Type()
)
irCharPortInboundAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortInboundAuth.setStatus("current")
_IrCharPortOutboundAuth_Type = PortAuthType
_IrCharPortOutboundAuth_Object = MibTableColumn
irCharPortOutboundAuth = _IrCharPortOutboundAuth_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 22),
    _IrCharPortOutboundAuth_Type()
)
irCharPortOutboundAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortOutboundAuth.setStatus("current")


class _IrCharPortAuthFallback_Type(Integer32):
    """Custom type irCharPortAuthFallback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IrCharPortAuthFallback_Type.__name__ = "Integer32"
_IrCharPortAuthFallback_Object = MibTableColumn
irCharPortAuthFallback = _IrCharPortAuthFallback_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 23),
    _IrCharPortAuthFallback_Type()
)
irCharPortAuthFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortAuthFallback.setStatus("current")


class _IrCharPortRadiusAcct_Type(Integer32):
    """Custom type irCharPortRadiusAcct based on Integer32"""
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


_IrCharPortRadiusAcct_Type.__name__ = "Integer32"
_IrCharPortRadiusAcct_Object = MibTableColumn
irCharPortRadiusAcct = _IrCharPortRadiusAcct_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 24),
    _IrCharPortRadiusAcct_Type()
)
irCharPortRadiusAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortRadiusAcct.setStatus("current")


class _IrCharPortTacacsAcct_Type(Integer32):
    """Custom type irCharPortTacacsAcct based on Integer32"""
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


_IrCharPortTacacsAcct_Type.__name__ = "Integer32"
_IrCharPortTacacsAcct_Object = MibTableColumn
irCharPortTacacsAcct = _IrCharPortTacacsAcct_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 25),
    _IrCharPortTacacsAcct_Type()
)
irCharPortTacacsAcct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortTacacsAcct.setStatus("current")


class _IrCharPortTransparent_Type(Integer32):
    """Custom type irCharPortTransparent based on Integer32"""
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


_IrCharPortTransparent_Type.__name__ = "Integer32"
_IrCharPortTransparent_Object = MibTableColumn
irCharPortTransparent = _IrCharPortTransparent_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 26),
    _IrCharPortTransparent_Type()
)
irCharPortTransparent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortTransparent.setStatus("current")


class _IrCharPortDataBufferSize_Type(Integer32):
    """Custom type irCharPortDataBufferSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_IrCharPortDataBufferSize_Type.__name__ = "Integer32"
_IrCharPortDataBufferSize_Object = MibTableColumn
irCharPortDataBufferSize = _IrCharPortDataBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 27),
    _IrCharPortDataBufferSize_Type()
)
irCharPortDataBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortDataBufferSize.setStatus("current")


class _IrCharPortDataBufferSyslog_Type(Integer32):
    """Custom type irCharPortDataBufferSyslog based on Integer32"""
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


_IrCharPortDataBufferSyslog_Type.__name__ = "Integer32"
_IrCharPortDataBufferSyslog_Object = MibTableColumn
irCharPortDataBufferSyslog = _IrCharPortDataBufferSyslog_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 28),
    _IrCharPortDataBufferSyslog_Type()
)
irCharPortDataBufferSyslog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortDataBufferSyslog.setStatus("current")


class _IrCharPortDataBufferDisplay_Type(Integer32):
    """Custom type irCharPortDataBufferDisplay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2),
          ("prompt", 3))
    )


_IrCharPortDataBufferDisplay_Type.__name__ = "Integer32"
_IrCharPortDataBufferDisplay_Object = MibTableColumn
irCharPortDataBufferDisplay = _IrCharPortDataBufferDisplay_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 29),
    _IrCharPortDataBufferDisplay_Type()
)
irCharPortDataBufferDisplay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortDataBufferDisplay.setStatus("current")


class _IrCharPortDataBufferTimeStamp_Type(Integer32):
    """Custom type irCharPortDataBufferTimeStamp based on Integer32"""
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


_IrCharPortDataBufferTimeStamp_Type.__name__ = "Integer32"
_IrCharPortDataBufferTimeStamp_Object = MibTableColumn
irCharPortDataBufferTimeStamp = _IrCharPortDataBufferTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 30),
    _IrCharPortDataBufferTimeStamp_Type()
)
irCharPortDataBufferTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irCharPortDataBufferTimeStamp.setStatus("current")
_IrCharPortTelnetPort_Type = Integer32
_IrCharPortTelnetPort_Object = MibTableColumn
irCharPortTelnetPort = _IrCharPortTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 31),
    _IrCharPortTelnetPort_Type()
)
irCharPortTelnetPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortTelnetPort.setStatus("current")
_IrCharPortSshPort_Type = Integer32
_IrCharPortSshPort_Object = MibTableColumn
irCharPortSshPort = _IrCharPortSshPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 2, 1, 32),
    _IrCharPortSshPort_Type()
)
irCharPortSshPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortSshPort.setStatus("current")
_IrCharPortStatsTable_Object = MibTable
irCharPortStatsTable = _IrCharPortStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 3)
)
if mibBuilder.loadTexts:
    irCharPortStatsTable.setStatus("current")
_IrCharPortStatsEntry_Object = MibTableRow
irCharPortStatsEntry = _IrCharPortStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 3, 1)
)
if mibBuilder.loadTexts:
    irCharPortStatsEntry.setStatus("current")
_IrCharPortTransmitBytes_Type = Counter32
_IrCharPortTransmitBytes_Object = MibTableColumn
irCharPortTransmitBytes = _IrCharPortTransmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 3, 1, 1),
    _IrCharPortTransmitBytes_Type()
)
irCharPortTransmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortTransmitBytes.setStatus("current")
_IrCharPortReceiveBytes_Type = Counter32
_IrCharPortReceiveBytes_Object = MibTableColumn
irCharPortReceiveBytes = _IrCharPortReceiveBytes_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 3, 1, 2),
    _IrCharPortReceiveBytes_Type()
)
irCharPortReceiveBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortReceiveBytes.setStatus("current")
_IrCharPortFrameErrors_Type = Counter32
_IrCharPortFrameErrors_Object = MibTableColumn
irCharPortFrameErrors = _IrCharPortFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 3, 1, 3),
    _IrCharPortFrameErrors_Type()
)
irCharPortFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortFrameErrors.setStatus("current")
_IrCharPortOverrunErrors_Type = Counter32
_IrCharPortOverrunErrors_Object = MibTableColumn
irCharPortOverrunErrors = _IrCharPortOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 3, 1, 4),
    _IrCharPortOverrunErrors_Type()
)
irCharPortOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortOverrunErrors.setStatus("current")
_IrCharPortParityErrors_Type = Counter32
_IrCharPortParityErrors_Object = MibTableColumn
irCharPortParityErrors = _IrCharPortParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 3, 1, 5),
    _IrCharPortParityErrors_Type()
)
irCharPortParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irCharPortParityErrors.setStatus("current")
_IrTempSensorTable_Object = MibTable
irTempSensorTable = _IrTempSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 4)
)
if mibBuilder.loadTexts:
    irTempSensorTable.setStatus("current")
_IrTempSensorEntry_Object = MibTableRow
irTempSensorEntry = _IrTempSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 4, 1)
)
irTempSensorEntry.setIndexNames(
    (0, "MRV-IR-CHAR-MIB", "irTempPortIndex"),
    (0, "MRV-IR-CHAR-MIB", "irTempSensorIndex"),
)
if mibBuilder.loadTexts:
    irTempSensorEntry.setStatus("current")
_IrTempPortIndex_Type = Integer32
_IrTempPortIndex_Object = MibTableColumn
irTempPortIndex = _IrTempPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 4, 1, 1),
    _IrTempPortIndex_Type()
)
irTempPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irTempPortIndex.setStatus("current")
_IrTempSensorIndex_Type = Integer32
_IrTempSensorIndex_Object = MibTableColumn
irTempSensorIndex = _IrTempSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 4, 1, 2),
    _IrTempSensorIndex_Type()
)
irTempSensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irTempSensorIndex.setStatus("current")
_IrTempValue_Type = Integer32
_IrTempValue_Object = MibTableColumn
irTempValue = _IrTempValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 4, 1, 3),
    _IrTempValue_Type()
)
irTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irTempValue.setStatus("current")


class _IrTempValueUnits_Type(Integer32):
    """Custom type irTempValueUnits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("celsius", 1),
          ("fahrenheit", 2))
    )


_IrTempValueUnits_Type.__name__ = "Integer32"
_IrTempValueUnits_Object = MibTableColumn
irTempValueUnits = _IrTempValueUnits_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 4, 1, 4),
    _IrTempValueUnits_Type()
)
irTempValueUnits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irTempValueUnits.setStatus("current")
_IrTempThresholdHigh_Type = Integer32
_IrTempThresholdHigh_Object = MibTableColumn
irTempThresholdHigh = _IrTempThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 4, 1, 5),
    _IrTempThresholdHigh_Type()
)
irTempThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irTempThresholdHigh.setStatus("current")
_IrTempThresholdLow_Type = Integer32
_IrTempThresholdLow_Object = MibTableColumn
irTempThresholdLow = _IrTempThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 4, 1, 6),
    _IrTempThresholdLow_Type()
)
irTempThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irTempThresholdLow.setStatus("current")
_IrTempTrapSeverity_Type = TrapSeverity
_IrTempTrapSeverity_Object = MibTableColumn
irTempTrapSeverity = _IrTempTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 4, 1, 7),
    _IrTempTrapSeverity_Type()
)
irTempTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irTempTrapSeverity.setStatus("current")


class _IrTempHysteresis_Type(Integer32):
    """Custom type irTempHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_IrTempHysteresis_Type.__name__ = "Integer32"
_IrTempHysteresis_Object = MibTableColumn
irTempHysteresis = _IrTempHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 4, 1, 8),
    _IrTempHysteresis_Type()
)
irTempHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irTempHysteresis.setStatus("current")
_IrHumiditySensorTable_Object = MibTable
irHumiditySensorTable = _IrHumiditySensorTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 5)
)
if mibBuilder.loadTexts:
    irHumiditySensorTable.setStatus("current")
_IrHumiditySensorEntry_Object = MibTableRow
irHumiditySensorEntry = _IrHumiditySensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 5, 1)
)
irHumiditySensorEntry.setIndexNames(
    (0, "MRV-IR-CHAR-MIB", "irHumidityPortIndex"),
    (0, "MRV-IR-CHAR-MIB", "irHumiditySensorIndex"),
)
if mibBuilder.loadTexts:
    irHumiditySensorEntry.setStatus("current")
_IrHumidityPortIndex_Type = Integer32
_IrHumidityPortIndex_Object = MibTableColumn
irHumidityPortIndex = _IrHumidityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 5, 1, 1),
    _IrHumidityPortIndex_Type()
)
irHumidityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHumidityPortIndex.setStatus("current")
_IrHumiditySensorIndex_Type = Integer32
_IrHumiditySensorIndex_Object = MibTableColumn
irHumiditySensorIndex = _IrHumiditySensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 5, 1, 2),
    _IrHumiditySensorIndex_Type()
)
irHumiditySensorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHumiditySensorIndex.setStatus("current")
_IrHumidityValue_Type = Integer32
_IrHumidityValue_Object = MibTableColumn
irHumidityValue = _IrHumidityValue_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 5, 1, 3),
    _IrHumidityValue_Type()
)
irHumidityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irHumidityValue.setStatus("current")
_IrHumidityThresholdHigh_Type = Integer32
_IrHumidityThresholdHigh_Object = MibTableColumn
irHumidityThresholdHigh = _IrHumidityThresholdHigh_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 5, 1, 4),
    _IrHumidityThresholdHigh_Type()
)
irHumidityThresholdHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irHumidityThresholdHigh.setStatus("current")
_IrHumidityThresholdLow_Type = Integer32
_IrHumidityThresholdLow_Object = MibTableColumn
irHumidityThresholdLow = _IrHumidityThresholdLow_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 5, 1, 5),
    _IrHumidityThresholdLow_Type()
)
irHumidityThresholdLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irHumidityThresholdLow.setStatus("current")
_IrHumidityTrapSeverity_Type = TrapSeverity
_IrHumidityTrapSeverity_Object = MibTableColumn
irHumidityTrapSeverity = _IrHumidityTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 5, 1, 6),
    _IrHumidityTrapSeverity_Type()
)
irHumidityTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irHumidityTrapSeverity.setStatus("current")


class _IrHumidityHysteresis_Type(Integer32):
    """Custom type irHumidityHysteresis based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_IrHumidityHysteresis_Type.__name__ = "Integer32"
_IrHumidityHysteresis_Object = MibTableColumn
irHumidityHysteresis = _IrHumidityHysteresis_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 5, 1, 7),
    _IrHumidityHysteresis_Type()
)
irHumidityHysteresis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irHumidityHysteresis.setStatus("current")
_IrPowerTable_Object = MibTable
irPowerTable = _IrPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 6)
)
if mibBuilder.loadTexts:
    irPowerTable.setStatus("current")
_IrPowerEntry_Object = MibTableRow
irPowerEntry = _IrPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 6, 1)
)
if mibBuilder.loadTexts:
    irPowerEntry.setStatus("current")


class _IrPowerModuleType_Type(Integer32):
    """Custom type irPowerModuleType based on Integer32"""
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
        *(("module4800", 2),
          ("module5150", 1),
          ("module5210", 5),
          ("module5250", 3),
          ("moduleOther", 4))
    )


_IrPowerModuleType_Type.__name__ = "Integer32"
_IrPowerModuleType_Object = MibTableColumn
irPowerModuleType = _IrPowerModuleType_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 6, 1, 1),
    _IrPowerModuleType_Type()
)
irPowerModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerModuleType.setStatus("current")


class _IrPowerCurrentLoad_Type(DisplayString):
    """Custom type irPowerCurrentLoad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IrPowerCurrentLoad_Type.__name__ = "DisplayString"
_IrPowerCurrentLoad_Object = MibTableColumn
irPowerCurrentLoad = _IrPowerCurrentLoad_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 6, 1, 2),
    _IrPowerCurrentLoad_Type()
)
irPowerCurrentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerCurrentLoad.setStatus("current")


class _IrPowerOutletCount_Type(Integer32):
    """Custom type irPowerOutletCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_IrPowerOutletCount_Type.__name__ = "Integer32"
_IrPowerOutletCount_Object = MibTableColumn
irPowerOutletCount = _IrPowerOutletCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 6, 1, 4),
    _IrPowerOutletCount_Type()
)
irPowerOutletCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerOutletCount.setStatus("current")


class _IrPowerCurrentLoadA_Type(DisplayString):
    """Custom type irPowerCurrentLoadA based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IrPowerCurrentLoadA_Type.__name__ = "DisplayString"
_IrPowerCurrentLoadA_Object = MibTableColumn
irPowerCurrentLoadA = _IrPowerCurrentLoadA_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 6, 1, 5),
    _IrPowerCurrentLoadA_Type()
)
irPowerCurrentLoadA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerCurrentLoadA.setStatus("current")


class _IrPowerCurrentLoadB_Type(DisplayString):
    """Custom type irPowerCurrentLoadB based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IrPowerCurrentLoadB_Type.__name__ = "DisplayString"
_IrPowerCurrentLoadB_Object = MibTableColumn
irPowerCurrentLoadB = _IrPowerCurrentLoadB_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 6, 1, 6),
    _IrPowerCurrentLoadB_Type()
)
irPowerCurrentLoadB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerCurrentLoadB.setStatus("current")


class _IrPowerCurrentLoadC_Type(DisplayString):
    """Custom type irPowerCurrentLoadC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IrPowerCurrentLoadC_Type.__name__ = "DisplayString"
_IrPowerCurrentLoadC_Object = MibTableColumn
irPowerCurrentLoadC = _IrPowerCurrentLoadC_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 6, 1, 7),
    _IrPowerCurrentLoadC_Type()
)
irPowerCurrentLoadC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerCurrentLoadC.setStatus("current")
_IrPowerOutletTable_Object = MibTable
irPowerOutletTable = _IrPowerOutletTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 7)
)
if mibBuilder.loadTexts:
    irPowerOutletTable.setStatus("current")
_IrPowerOutletEntry_Object = MibTableRow
irPowerOutletEntry = _IrPowerOutletEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 7, 1)
)
irPowerOutletEntry.setIndexNames(
    (0, "MRV-IR-CHAR-MIB", "irPowerPortIndex"),
    (0, "MRV-IR-CHAR-MIB", "irPowerOutletIndex"),
)
if mibBuilder.loadTexts:
    irPowerOutletEntry.setStatus("current")
_IrPowerPortIndex_Type = Integer32
_IrPowerPortIndex_Object = MibTableColumn
irPowerPortIndex = _IrPowerPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 7, 1, 1),
    _IrPowerPortIndex_Type()
)
irPowerPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerPortIndex.setStatus("current")
_IrPowerOutletIndex_Type = Integer32
_IrPowerOutletIndex_Object = MibTableColumn
irPowerOutletIndex = _IrPowerOutletIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 7, 1, 2),
    _IrPowerOutletIndex_Type()
)
irPowerOutletIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerOutletIndex.setStatus("current")


class _IrPowerOutletName_Type(DisplayString):
    """Custom type irPowerOutletName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_IrPowerOutletName_Type.__name__ = "DisplayString"
_IrPowerOutletName_Object = MibTableColumn
irPowerOutletName = _IrPowerOutletName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 7, 1, 3),
    _IrPowerOutletName_Type()
)
irPowerOutletName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irPowerOutletName.setStatus("current")


class _IrPowerOutletStatus_Type(Integer32):
    """Custom type irPowerOutletStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 2),
          ("on", 1))
    )


_IrPowerOutletStatus_Type.__name__ = "Integer32"
_IrPowerOutletStatus_Object = MibTableColumn
irPowerOutletStatus = _IrPowerOutletStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 7, 1, 4),
    _IrPowerOutletStatus_Type()
)
irPowerOutletStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerOutletStatus.setStatus("current")


class _IrPowerOutletAction_Type(Integer32):
    """Custom type irPowerOutletAction based on Integer32"""
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
        *(("off", 3),
          ("on", 2),
          ("other", 1),
          ("reboot", 4))
    )


_IrPowerOutletAction_Type.__name__ = "Integer32"
_IrPowerOutletAction_Object = MibTableColumn
irPowerOutletAction = _IrPowerOutletAction_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 7, 1, 5),
    _IrPowerOutletAction_Type()
)
irPowerOutletAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irPowerOutletAction.setStatus("current")


class _IrPowerOutletCurrentLoad_Type(DisplayString):
    """Custom type irPowerOutletCurrentLoad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_IrPowerOutletCurrentLoad_Type.__name__ = "DisplayString"
_IrPowerOutletCurrentLoad_Object = MibTableColumn
irPowerOutletCurrentLoad = _IrPowerOutletCurrentLoad_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 7, 1, 6),
    _IrPowerOutletCurrentLoad_Type()
)
irPowerOutletCurrentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irPowerOutletCurrentLoad.setStatus("current")
_IrTcpPipeTable_Object = MibTable
irTcpPipeTable = _IrTcpPipeTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 8)
)
if mibBuilder.loadTexts:
    irTcpPipeTable.setStatus("current")
_IrTcpPipeEntry_Object = MibTableRow
irTcpPipeEntry = _IrTcpPipeEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 8, 1)
)
if mibBuilder.loadTexts:
    irTcpPipeEntry.setStatus("current")
_IrTcpPipeRemoteIpAddress_Type = IpAddress
_IrTcpPipeRemoteIpAddress_Object = MibTableColumn
irTcpPipeRemoteIpAddress = _IrTcpPipeRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 8, 1, 1),
    _IrTcpPipeRemoteIpAddress_Type()
)
irTcpPipeRemoteIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irTcpPipeRemoteIpAddress.setStatus("current")


class _IrTcpPipeRemoteTcpPort_Type(Integer32):
    """Custom type irTcpPipeRemoteTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2001, 9999),
    )


_IrTcpPipeRemoteTcpPort_Type.__name__ = "Integer32"
_IrTcpPipeRemoteTcpPort_Object = MibTableColumn
irTcpPipeRemoteTcpPort = _IrTcpPipeRemoteTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 8, 1, 2),
    _IrTcpPipeRemoteTcpPort_Type()
)
irTcpPipeRemoteTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irTcpPipeRemoteTcpPort.setStatus("current")


class _IrTcpPipeWindowSize_Type(Integer32):
    """Custom type irTcpPipeWindowSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 1400),
    )


_IrTcpPipeWindowSize_Type.__name__ = "Integer32"
_IrTcpPipeWindowSize_Object = MibTableColumn
irTcpPipeWindowSize = _IrTcpPipeWindowSize_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 8, 1, 3),
    _IrTcpPipeWindowSize_Type()
)
irTcpPipeWindowSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irTcpPipeWindowSize.setStatus("current")


class _IrTcpPipeConnRetryCount_Type(Integer32):
    """Custom type irTcpPipeConnRetryCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_IrTcpPipeConnRetryCount_Type.__name__ = "Integer32"
_IrTcpPipeConnRetryCount_Object = MibTableColumn
irTcpPipeConnRetryCount = _IrTcpPipeConnRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 8, 1, 4),
    _IrTcpPipeConnRetryCount_Type()
)
irTcpPipeConnRetryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irTcpPipeConnRetryCount.setStatus("current")


class _IrTcpPipeConnStatus_Type(Integer32):
    """Custom type irTcpPipeConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("connected", 2),
          ("connecting", 1),
          ("idle", 0),
          ("suspended", 3))
    )


_IrTcpPipeConnStatus_Type.__name__ = "Integer32"
_IrTcpPipeConnStatus_Object = MibTableColumn
irTcpPipeConnStatus = _IrTcpPipeConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 8, 1, 5),
    _IrTcpPipeConnStatus_Type()
)
irTcpPipeConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irTcpPipeConnStatus.setStatus("current")
_IrModem_ObjectIdentity = ObjectIdentity
irModem = _IrModem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9)
)
_IrModemCfgTable_Object = MibTable
irModemCfgTable = _IrModemCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 1)
)
if mibBuilder.loadTexts:
    irModemCfgTable.setStatus("current")
_IrModemCfgEntry_Object = MibTableRow
irModemCfgEntry = _IrModemCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 1, 1)
)
irModemCfgEntry.setIndexNames(
    (0, "MRV-IR-CHAR-MIB", "irModemIndex"),
)
if mibBuilder.loadTexts:
    irModemCfgEntry.setStatus("current")
_IrModemIndex_Type = Integer32
_IrModemIndex_Object = MibTableColumn
irModemIndex = _IrModemIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 1, 1, 1),
    _IrModemIndex_Type()
)
irModemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irModemIndex.setStatus("current")
_IrModemTimeout_Type = Integer32
_IrModemTimeout_Object = MibTableColumn
irModemTimeout = _IrModemTimeout_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 1, 1, 2),
    _IrModemTimeout_Type()
)
irModemTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irModemTimeout.setStatus("current")
_IrModemRetry_Type = Integer32
_IrModemRetry_Object = MibTableColumn
irModemRetry = _IrModemRetry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 1, 1, 3),
    _IrModemRetry_Type()
)
irModemRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irModemRetry.setStatus("current")


class _IrModemState_Type(Integer32):
    """Custom type irModemState based on Integer32"""
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


_IrModemState_Type.__name__ = "Integer32"
_IrModemState_Object = MibTableColumn
irModemState = _IrModemState_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 1, 1, 4),
    _IrModemState_Type()
)
irModemState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irModemState.setStatus("current")


class _IrModemPooling_Type(Integer32):
    """Custom type irModemPooling based on Integer32"""
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


_IrModemPooling_Type.__name__ = "Integer32"
_IrModemPooling_Object = MibTableColumn
irModemPooling = _IrModemPooling_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 1, 1, 5),
    _IrModemPooling_Type()
)
irModemPooling.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irModemPooling.setStatus("current")
_IrModemDialNumber_Type = DisplayString
_IrModemDialNumber_Object = MibTableColumn
irModemDialNumber = _IrModemDialNumber_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 1, 1, 6),
    _IrModemDialNumber_Type()
)
irModemDialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irModemDialNumber.setStatus("current")
_IrModemInitString_Type = DisplayString
_IrModemInitString_Object = MibTableColumn
irModemInitString = _IrModemInitString_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 1, 1, 7),
    _IrModemInitString_Type()
)
irModemInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irModemInitString.setStatus("current")
_IrInternalModemPort_Type = Integer32
_IrInternalModemPort_Object = MibScalar
irInternalModemPort = _IrInternalModemPort_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 2),
    _IrInternalModemPort_Type()
)
irInternalModemPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irInternalModemPort.setStatus("current")


class _IrInternalModemType_Type(Integer32):
    """Custom type irInternalModemType based on Integer32"""
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
        *(("gsmGprs", 4),
          ("none", 1),
          ("rs485", 3),
          ("v90", 2))
    )


_IrInternalModemType_Type.__name__ = "Integer32"
_IrInternalModemType_Object = MibScalar
irInternalModemType = _IrInternalModemType_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 9, 3),
    _IrInternalModemType_Type()
)
irInternalModemType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irInternalModemType.setStatus("current")
_IrLdAlarmConfigTable_Object = MibTable
irLdAlarmConfigTable = _IrLdAlarmConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10)
)
if mibBuilder.loadTexts:
    irLdAlarmConfigTable.setStatus("current")
_IrLdAlarmConfigEntry_Object = MibTableRow
irLdAlarmConfigEntry = _IrLdAlarmConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1)
)
irLdAlarmConfigEntry.setIndexNames(
    (0, "MRV-IR-CHAR-MIB", "irLdAlarmPortIndex"),
    (0, "MRV-IR-CHAR-MIB", "irLdAlarmPointIndex"),
)
if mibBuilder.loadTexts:
    irLdAlarmConfigEntry.setStatus("current")


class _IrLdAlarmPortIndex_Type(Integer32):
    """Custom type irLdAlarmPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IrLdAlarmPortIndex_Type.__name__ = "Integer32"
_IrLdAlarmPortIndex_Object = MibTableColumn
irLdAlarmPortIndex = _IrLdAlarmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1, 1),
    _IrLdAlarmPortIndex_Type()
)
irLdAlarmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irLdAlarmPortIndex.setStatus("current")


class _IrLdAlarmPointIndex_Type(Integer32):
    """Custom type irLdAlarmPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IrLdAlarmPointIndex_Type.__name__ = "Integer32"
_IrLdAlarmPointIndex_Object = MibTableColumn
irLdAlarmPointIndex = _IrLdAlarmPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1, 2),
    _IrLdAlarmPointIndex_Type()
)
irLdAlarmPointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irLdAlarmPointIndex.setStatus("current")


class _IrLdAlarmName_Type(DisplayString):
    """Custom type irLdAlarmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrLdAlarmName_Type.__name__ = "DisplayString"
_IrLdAlarmName_Object = MibTableColumn
irLdAlarmName = _IrLdAlarmName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1, 3),
    _IrLdAlarmName_Type()
)
irLdAlarmName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irLdAlarmName.setStatus("current")


class _IrLdAlarmDescription_Type(DisplayString):
    """Custom type irLdAlarmDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IrLdAlarmDescription_Type.__name__ = "DisplayString"
_IrLdAlarmDescription_Object = MibTableColumn
irLdAlarmDescription = _IrLdAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1, 4),
    _IrLdAlarmDescription_Type()
)
irLdAlarmDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irLdAlarmDescription.setStatus("current")
_IrLdAlarmContactState_Type = IrContactState
_IrLdAlarmContactState_Object = MibTableColumn
irLdAlarmContactState = _IrLdAlarmContactState_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1, 5),
    _IrLdAlarmContactState_Type()
)
irLdAlarmContactState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irLdAlarmContactState.setStatus("current")
_IrLdAlarmContactFaultState_Type = IrContactState
_IrLdAlarmContactFaultState_Object = MibTableColumn
irLdAlarmContactFaultState = _IrLdAlarmContactFaultState_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1, 6),
    _IrLdAlarmContactFaultState_Type()
)
irLdAlarmContactFaultState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irLdAlarmContactFaultState.setStatus("current")


class _IrLdAlarmTrapStatus_Type(Integer32):
    """Custom type irLdAlarmTrapStatus based on Integer32"""
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


_IrLdAlarmTrapStatus_Type.__name__ = "Integer32"
_IrLdAlarmTrapStatus_Object = MibTableColumn
irLdAlarmTrapStatus = _IrLdAlarmTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1, 7),
    _IrLdAlarmTrapStatus_Type()
)
irLdAlarmTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irLdAlarmTrapStatus.setStatus("current")
_IrLdAlarmTrapSeverity_Type = TrapSeverity
_IrLdAlarmTrapSeverity_Object = MibTableColumn
irLdAlarmTrapSeverity = _IrLdAlarmTrapSeverity_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1, 8),
    _IrLdAlarmTrapSeverity_Type()
)
irLdAlarmTrapSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irLdAlarmTrapSeverity.setStatus("current")
_IrLdAlarmCount_Type = Counter32
_IrLdAlarmCount_Object = MibTableColumn
irLdAlarmCount = _IrLdAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1, 9),
    _IrLdAlarmCount_Type()
)
irLdAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irLdAlarmCount.setStatus("current")


class _IrLdAlarmTimestamp_Type(DisplayString):
    """Custom type irLdAlarmTimestamp based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrLdAlarmTimestamp_Type.__name__ = "DisplayString"
_IrLdAlarmTimestamp_Object = MibTableColumn
irLdAlarmTimestamp = _IrLdAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 10, 1, 10),
    _IrLdAlarmTimestamp_Type()
)
irLdAlarmTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irLdAlarmTimestamp.setStatus("current")
_IrLdControlConfigTable_Object = MibTable
irLdControlConfigTable = _IrLdControlConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 11)
)
if mibBuilder.loadTexts:
    irLdControlConfigTable.setStatus("current")
_IrLdControlConfigEntry_Object = MibTableRow
irLdControlConfigEntry = _IrLdControlConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 11, 1)
)
irLdControlConfigEntry.setIndexNames(
    (0, "MRV-IR-CHAR-MIB", "irLdControlPortIndex"),
    (0, "MRV-IR-CHAR-MIB", "irLdControlPointIndex"),
)
if mibBuilder.loadTexts:
    irLdControlConfigEntry.setStatus("current")


class _IrLdControlPortIndex_Type(Integer32):
    """Custom type irLdControlPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 48),
    )


_IrLdControlPortIndex_Type.__name__ = "Integer32"
_IrLdControlPortIndex_Object = MibTableColumn
irLdControlPortIndex = _IrLdControlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 11, 1, 1),
    _IrLdControlPortIndex_Type()
)
irLdControlPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irLdControlPortIndex.setStatus("current")


class _IrLdControlPointIndex_Type(Integer32):
    """Custom type irLdControlPointIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_IrLdControlPointIndex_Type.__name__ = "Integer32"
_IrLdControlPointIndex_Object = MibTableColumn
irLdControlPointIndex = _IrLdControlPointIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 11, 1, 2),
    _IrLdControlPointIndex_Type()
)
irLdControlPointIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irLdControlPointIndex.setStatus("current")


class _IrLdControlName_Type(DisplayString):
    """Custom type irLdControlName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrLdControlName_Type.__name__ = "DisplayString"
_IrLdControlName_Object = MibTableColumn
irLdControlName = _IrLdControlName_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 11, 1, 3),
    _IrLdControlName_Type()
)
irLdControlName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irLdControlName.setStatus("current")


class _IrLdControlDescription_Type(DisplayString):
    """Custom type irLdControlDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_IrLdControlDescription_Type.__name__ = "DisplayString"
_IrLdControlDescription_Object = MibTableColumn
irLdControlDescription = _IrLdControlDescription_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 11, 1, 4),
    _IrLdControlDescription_Type()
)
irLdControlDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irLdControlDescription.setStatus("current")
_IrLdControlState_Type = IrControlState
_IrLdControlState_Object = MibTableColumn
irLdControlState = _IrLdControlState_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 11, 1, 5),
    _IrLdControlState_Type()
)
irLdControlState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irLdControlState.setStatus("current")
_IrLdControlEnergizedState_Type = IrControlState
_IrLdControlEnergizedState_Object = MibTableColumn
irLdControlEnergizedState = _IrLdControlEnergizedState_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 11, 1, 6),
    _IrLdControlEnergizedState_Type()
)
irLdControlEnergizedState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irLdControlEnergizedState.setStatus("current")
_IrRs485PortTable_Object = MibTable
irRs485PortTable = _IrRs485PortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 12)
)
if mibBuilder.loadTexts:
    irRs485PortTable.setStatus("current")
_IrRs485PortEntry_Object = MibTableRow
irRs485PortEntry = _IrRs485PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 12, 1)
)
irRs485PortEntry.setIndexNames(
    (0, "MRV-IR-CHAR-MIB", "irRs485PortIndex"),
)
if mibBuilder.loadTexts:
    irRs485PortEntry.setStatus("current")
_IrRs485PortIndex_Type = Integer32
_IrRs485PortIndex_Object = MibTableColumn
irRs485PortIndex = _IrRs485PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 12, 1, 1),
    _IrRs485PortIndex_Type()
)
irRs485PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irRs485PortIndex.setStatus("current")


class _IrRs485PortDuplexMode_Type(Integer32):
    """Custom type irRs485PortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2))
    )


_IrRs485PortDuplexMode_Type.__name__ = "Integer32"
_IrRs485PortDuplexMode_Object = MibTableColumn
irRs485PortDuplexMode = _IrRs485PortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 12, 1, 2),
    _IrRs485PortDuplexMode_Type()
)
irRs485PortDuplexMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irRs485PortDuplexMode.setStatus("current")


class _IrRs485PortEchoMode_Type(Integer32):
    """Custom type irRs485PortEchoMode based on Integer32"""
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


_IrRs485PortEchoMode_Type.__name__ = "Integer32"
_IrRs485PortEchoMode_Object = MibTableColumn
irRs485PortEchoMode = _IrRs485PortEchoMode_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 12, 1, 3),
    _IrRs485PortEchoMode_Type()
)
irRs485PortEchoMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irRs485PortEchoMode.setStatus("current")


class _IrRs485PortTransmitter_Type(Integer32):
    """Custom type irRs485PortTransmitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("rts", 2))
    )


_IrRs485PortTransmitter_Type.__name__ = "Integer32"
_IrRs485PortTransmitter_Object = MibTableColumn
irRs485PortTransmitter = _IrRs485PortTransmitter_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 12, 1, 4),
    _IrRs485PortTransmitter_Type()
)
irRs485PortTransmitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irRs485PortTransmitter.setStatus("current")
_IrGsmPortTable_Object = MibTable
irGsmPortTable = _IrGsmPortTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 13)
)
if mibBuilder.loadTexts:
    irGsmPortTable.setStatus("current")
_IrGsmPortEntry_Object = MibTableRow
irGsmPortEntry = _IrGsmPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 13, 1)
)
irGsmPortEntry.setIndexNames(
    (0, "MRV-IR-CHAR-MIB", "irGsmPortIndex"),
)
if mibBuilder.loadTexts:
    irGsmPortEntry.setStatus("current")
_IrGsmPortIndex_Type = Integer32
_IrGsmPortIndex_Object = MibTableColumn
irGsmPortIndex = _IrGsmPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 13, 1, 1),
    _IrGsmPortIndex_Type()
)
irGsmPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irGsmPortIndex.setStatus("current")


class _IrGsmPortRcvSigStrength_Type(Integer32):
    """Custom type irGsmPortRcvSigStrength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_IrGsmPortRcvSigStrength_Type.__name__ = "Integer32"
_IrGsmPortRcvSigStrength_Object = MibTableColumn
irGsmPortRcvSigStrength = _IrGsmPortRcvSigStrength_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 13, 1, 2),
    _IrGsmPortRcvSigStrength_Type()
)
irGsmPortRcvSigStrength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irGsmPortRcvSigStrength.setStatus("current")


class _IrGsmPortBitErrorRate_Type(Integer32):
    """Custom type irGsmPortBitErrorRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_IrGsmPortBitErrorRate_Type.__name__ = "Integer32"
_IrGsmPortBitErrorRate_Object = MibTableColumn
irGsmPortBitErrorRate = _IrGsmPortBitErrorRate_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 13, 1, 3),
    _IrGsmPortBitErrorRate_Type()
)
irGsmPortBitErrorRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irGsmPortBitErrorRate.setStatus("current")
_IrUpsTable_Object = MibTable
irUpsTable = _IrUpsTable_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 14)
)
if mibBuilder.loadTexts:
    irUpsTable.setStatus("current")
_IrUpsEntry_Object = MibTableRow
irUpsEntry = _IrUpsEntry_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 14, 1)
)
if mibBuilder.loadTexts:
    irUpsEntry.setStatus("current")


class _IrUpsType_Type(Integer32):
    """Custom type irUpsType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("simple", 2),
          ("smart", 1))
    )


_IrUpsType_Type.__name__ = "Integer32"
_IrUpsType_Object = MibTableColumn
irUpsType = _IrUpsType_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 14, 1, 1),
    _IrUpsType_Type()
)
irUpsType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    irUpsType.setStatus("current")


class _IrUpsStatus_Type(Integer32):
    """Custom type irUpsStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("offline", 1),
          ("online", 2))
    )


_IrUpsStatus_Type.__name__ = "Integer32"
_IrUpsStatus_Object = MibTableColumn
irUpsStatus = _IrUpsStatus_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 14, 1, 2),
    _IrUpsStatus_Type()
)
irUpsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irUpsStatus.setStatus("current")


class _IrUpsModel_Type(DisplayString):
    """Custom type irUpsModel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_IrUpsModel_Type.__name__ = "DisplayString"
_IrUpsModel_Object = MibTableColumn
irUpsModel = _IrUpsModel_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 14, 1, 3),
    _IrUpsModel_Type()
)
irUpsModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irUpsModel.setStatus("current")


class _IrUpsCharge_Type(DisplayString):
    """Custom type irUpsCharge based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_IrUpsCharge_Type.__name__ = "DisplayString"
_IrUpsCharge_Object = MibTableColumn
irUpsCharge = _IrUpsCharge_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 14, 1, 4),
    _IrUpsCharge_Type()
)
irUpsCharge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irUpsCharge.setStatus("current")


class _IrUpsLoad_Type(DisplayString):
    """Custom type irUpsLoad based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 3),
    )


_IrUpsLoad_Type.__name__ = "DisplayString"
_IrUpsLoad_Object = MibTableColumn
irUpsLoad = _IrUpsLoad_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 14, 1, 5),
    _IrUpsLoad_Type()
)
irUpsLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irUpsLoad.setStatus("current")


class _IrUpsLife_Type(DisplayString):
    """Custom type irUpsLife based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 4),
    )


_IrUpsLife_Type.__name__ = "DisplayString"
_IrUpsLife_Object = MibTableColumn
irUpsLife = _IrUpsLife_Object(
    (1, 3, 6, 1, 4, 1, 33, 100, 2, 14, 1, 6),
    _IrUpsLife_Type()
)
irUpsLife.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    irUpsLife.setStatus("current")
irCharPortEntry.registerAugmentions(
    ("MRV-IR-CHAR-MIB",
     "irCharPortStatsEntry")
)
irCharPortStatsEntry.setIndexNames(*irCharPortEntry.getIndexNames())
irCharPortEntry.registerAugmentions(
    ("MRV-IR-CHAR-MIB",
     "irPowerEntry")
)
irPowerEntry.setIndexNames(*irCharPortEntry.getIndexNames())
irCharPortEntry.registerAugmentions(
    ("MRV-IR-CHAR-MIB",
     "irTcpPipeEntry")
)
irTcpPipeEntry.setIndexNames(*irCharPortEntry.getIndexNames())
irCharPortEntry.registerAugmentions(
    ("MRV-IR-CHAR-MIB",
     "irUpsEntry")
)
irUpsEntry.setIndexNames(*irCharPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MRV-IR-CHAR-MIB",
    **{"IrContactState": IrContactState,
       "IrControlState": IrControlState,
       "PortAccessType": PortAccessType,
       "PortSpeed": PortSpeed,
       "PortAuthType": PortAuthType,
       "SignalStatus": SignalStatus,
       "irCharMib": irCharMib,
       "irCharNumber": irCharNumber,
       "irCharPortTable": irCharPortTable,
       "irCharPortEntry": irCharPortEntry,
       "irCharPortIndex": irCharPortIndex,
       "irCharPortAccessType": irCharPortAccessType,
       "irCharPortFlowControl": irCharPortFlowControl,
       "irCharPortStopBits": irCharPortStopBits,
       "irCharPortParity": irCharPortParity,
       "irCharPortBitsPerChar": irCharPortBitsPerChar,
       "irCharPortAutoDial": irCharPortAutoDial,
       "irCharPortAutoHangup": irCharPortAutoHangup,
       "irCharPortAutobaud": irCharPortAutobaud,
       "irCharPortAutobaudRetry": irCharPortAutobaudRetry,
       "irCharPortInSignalCts": irCharPortInSignalCts,
       "irCharPortInSignalDsr": irCharPortInSignalDsr,
       "irCharPortInSignalDcd": irCharPortInSignalDcd,
       "irCharPortOutSignalRts": irCharPortOutSignalRts,
       "irCharPortOutSignalDtr": irCharPortOutSignalDtr,
       "irCharPortSpeed": irCharPortSpeed,
       "irCharPortPrompt": irCharPortPrompt,
       "irCharPortBreak": irCharPortBreak,
       "irCharPortSpecialBreakString": irCharPortSpecialBreakString,
       "irCharPortSpecialBreak": irCharPortSpecialBreak,
       "irCharPortInboundAuth": irCharPortInboundAuth,
       "irCharPortOutboundAuth": irCharPortOutboundAuth,
       "irCharPortAuthFallback": irCharPortAuthFallback,
       "irCharPortRadiusAcct": irCharPortRadiusAcct,
       "irCharPortTacacsAcct": irCharPortTacacsAcct,
       "irCharPortTransparent": irCharPortTransparent,
       "irCharPortDataBufferSize": irCharPortDataBufferSize,
       "irCharPortDataBufferSyslog": irCharPortDataBufferSyslog,
       "irCharPortDataBufferDisplay": irCharPortDataBufferDisplay,
       "irCharPortDataBufferTimeStamp": irCharPortDataBufferTimeStamp,
       "irCharPortTelnetPort": irCharPortTelnetPort,
       "irCharPortSshPort": irCharPortSshPort,
       "irCharPortStatsTable": irCharPortStatsTable,
       "irCharPortStatsEntry": irCharPortStatsEntry,
       "irCharPortTransmitBytes": irCharPortTransmitBytes,
       "irCharPortReceiveBytes": irCharPortReceiveBytes,
       "irCharPortFrameErrors": irCharPortFrameErrors,
       "irCharPortOverrunErrors": irCharPortOverrunErrors,
       "irCharPortParityErrors": irCharPortParityErrors,
       "irTempSensorTable": irTempSensorTable,
       "irTempSensorEntry": irTempSensorEntry,
       "irTempPortIndex": irTempPortIndex,
       "irTempSensorIndex": irTempSensorIndex,
       "irTempValue": irTempValue,
       "irTempValueUnits": irTempValueUnits,
       "irTempThresholdHigh": irTempThresholdHigh,
       "irTempThresholdLow": irTempThresholdLow,
       "irTempTrapSeverity": irTempTrapSeverity,
       "irTempHysteresis": irTempHysteresis,
       "irHumiditySensorTable": irHumiditySensorTable,
       "irHumiditySensorEntry": irHumiditySensorEntry,
       "irHumidityPortIndex": irHumidityPortIndex,
       "irHumiditySensorIndex": irHumiditySensorIndex,
       "irHumidityValue": irHumidityValue,
       "irHumidityThresholdHigh": irHumidityThresholdHigh,
       "irHumidityThresholdLow": irHumidityThresholdLow,
       "irHumidityTrapSeverity": irHumidityTrapSeverity,
       "irHumidityHysteresis": irHumidityHysteresis,
       "irPowerTable": irPowerTable,
       "irPowerEntry": irPowerEntry,
       "irPowerModuleType": irPowerModuleType,
       "irPowerCurrentLoad": irPowerCurrentLoad,
       "irPowerOutletCount": irPowerOutletCount,
       "irPowerCurrentLoadA": irPowerCurrentLoadA,
       "irPowerCurrentLoadB": irPowerCurrentLoadB,
       "irPowerCurrentLoadC": irPowerCurrentLoadC,
       "irPowerOutletTable": irPowerOutletTable,
       "irPowerOutletEntry": irPowerOutletEntry,
       "irPowerPortIndex": irPowerPortIndex,
       "irPowerOutletIndex": irPowerOutletIndex,
       "irPowerOutletName": irPowerOutletName,
       "irPowerOutletStatus": irPowerOutletStatus,
       "irPowerOutletAction": irPowerOutletAction,
       "irPowerOutletCurrentLoad": irPowerOutletCurrentLoad,
       "irTcpPipeTable": irTcpPipeTable,
       "irTcpPipeEntry": irTcpPipeEntry,
       "irTcpPipeRemoteIpAddress": irTcpPipeRemoteIpAddress,
       "irTcpPipeRemoteTcpPort": irTcpPipeRemoteTcpPort,
       "irTcpPipeWindowSize": irTcpPipeWindowSize,
       "irTcpPipeConnRetryCount": irTcpPipeConnRetryCount,
       "irTcpPipeConnStatus": irTcpPipeConnStatus,
       "irModem": irModem,
       "irModemCfgTable": irModemCfgTable,
       "irModemCfgEntry": irModemCfgEntry,
       "irModemIndex": irModemIndex,
       "irModemTimeout": irModemTimeout,
       "irModemRetry": irModemRetry,
       "irModemState": irModemState,
       "irModemPooling": irModemPooling,
       "irModemDialNumber": irModemDialNumber,
       "irModemInitString": irModemInitString,
       "irInternalModemPort": irInternalModemPort,
       "irInternalModemType": irInternalModemType,
       "irLdAlarmConfigTable": irLdAlarmConfigTable,
       "irLdAlarmConfigEntry": irLdAlarmConfigEntry,
       "irLdAlarmPortIndex": irLdAlarmPortIndex,
       "irLdAlarmPointIndex": irLdAlarmPointIndex,
       "irLdAlarmName": irLdAlarmName,
       "irLdAlarmDescription": irLdAlarmDescription,
       "irLdAlarmContactState": irLdAlarmContactState,
       "irLdAlarmContactFaultState": irLdAlarmContactFaultState,
       "irLdAlarmTrapStatus": irLdAlarmTrapStatus,
       "irLdAlarmTrapSeverity": irLdAlarmTrapSeverity,
       "irLdAlarmCount": irLdAlarmCount,
       "irLdAlarmTimestamp": irLdAlarmTimestamp,
       "irLdControlConfigTable": irLdControlConfigTable,
       "irLdControlConfigEntry": irLdControlConfigEntry,
       "irLdControlPortIndex": irLdControlPortIndex,
       "irLdControlPointIndex": irLdControlPointIndex,
       "irLdControlName": irLdControlName,
       "irLdControlDescription": irLdControlDescription,
       "irLdControlState": irLdControlState,
       "irLdControlEnergizedState": irLdControlEnergizedState,
       "irRs485PortTable": irRs485PortTable,
       "irRs485PortEntry": irRs485PortEntry,
       "irRs485PortIndex": irRs485PortIndex,
       "irRs485PortDuplexMode": irRs485PortDuplexMode,
       "irRs485PortEchoMode": irRs485PortEchoMode,
       "irRs485PortTransmitter": irRs485PortTransmitter,
       "irGsmPortTable": irGsmPortTable,
       "irGsmPortEntry": irGsmPortEntry,
       "irGsmPortIndex": irGsmPortIndex,
       "irGsmPortRcvSigStrength": irGsmPortRcvSigStrength,
       "irGsmPortBitErrorRate": irGsmPortBitErrorRate,
       "irUpsTable": irUpsTable,
       "irUpsEntry": irUpsEntry,
       "irUpsType": irUpsType,
       "irUpsStatus": irUpsStatus,
       "irUpsModel": irUpsModel,
       "irUpsCharge": irUpsCharge,
       "irUpsLoad": irUpsLoad,
       "irUpsLife": irUpsLife}
)
