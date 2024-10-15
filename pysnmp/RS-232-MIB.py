# SNMP MIB module (RS-232-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RS-232-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 20:35:31 2024
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 iso,
 transmission) = mibBuilder.importSymbols(
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
    "iso",
    "transmission")

(DisplayString,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "TextualConvention")


# MODULE-IDENTITY

rs232 = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 33)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Rs232Number_Type = Integer32
_Rs232Number_Object = MibScalar
rs232Number = _Rs232Number_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 1),
    _Rs232Number_Type()
)
rs232Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232Number.setStatus("current")
_Rs232PortTable_Object = MibTable
rs232PortTable = _Rs232PortTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2)
)
if mibBuilder.loadTexts:
    rs232PortTable.setStatus("current")
_Rs232PortEntry_Object = MibTableRow
rs232PortEntry = _Rs232PortEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1)
)
rs232PortEntry.setIndexNames(
    (0, "RS-232-MIB", "rs232PortIndex"),
)
if mibBuilder.loadTexts:
    rs232PortEntry.setStatus("current")
_Rs232PortIndex_Type = InterfaceIndex
_Rs232PortIndex_Object = MibTableColumn
rs232PortIndex = _Rs232PortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 1),
    _Rs232PortIndex_Type()
)
rs232PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortIndex.setStatus("current")


class _Rs232PortType_Type(Integer32):
    """Custom type rs232PortType based on Integer32"""
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
        *(("other", 1),
          ("rs232", 2),
          ("rs422", 3),
          ("rs423", 4),
          ("v35", 5),
          ("x21", 6))
    )


_Rs232PortType_Type.__name__ = "Integer32"
_Rs232PortType_Object = MibTableColumn
rs232PortType = _Rs232PortType_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 2),
    _Rs232PortType_Type()
)
rs232PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortType.setStatus("current")
_Rs232PortInSigNumber_Type = Integer32
_Rs232PortInSigNumber_Object = MibTableColumn
rs232PortInSigNumber = _Rs232PortInSigNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 3),
    _Rs232PortInSigNumber_Type()
)
rs232PortInSigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortInSigNumber.setStatus("current")
_Rs232PortOutSigNumber_Type = Integer32
_Rs232PortOutSigNumber_Object = MibTableColumn
rs232PortOutSigNumber = _Rs232PortOutSigNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 4),
    _Rs232PortOutSigNumber_Type()
)
rs232PortOutSigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortOutSigNumber.setStatus("current")
_Rs232PortInSpeed_Type = Integer32
_Rs232PortInSpeed_Object = MibTableColumn
rs232PortInSpeed = _Rs232PortInSpeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 5),
    _Rs232PortInSpeed_Type()
)
rs232PortInSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PortInSpeed.setStatus("current")
_Rs232PortOutSpeed_Type = Integer32
_Rs232PortOutSpeed_Object = MibTableColumn
rs232PortOutSpeed = _Rs232PortOutSpeed_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 6),
    _Rs232PortOutSpeed_Type()
)
rs232PortOutSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PortOutSpeed.setStatus("current")


class _Rs232PortInFlowType_Type(Integer32):
    """Custom type rs232PortInFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctsRts", 2),
          ("dsrDtr", 3),
          ("none", 1))
    )


_Rs232PortInFlowType_Type.__name__ = "Integer32"
_Rs232PortInFlowType_Object = MibTableColumn
rs232PortInFlowType = _Rs232PortInFlowType_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 7),
    _Rs232PortInFlowType_Type()
)
rs232PortInFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PortInFlowType.setStatus("current")


class _Rs232PortOutFlowType_Type(Integer32):
    """Custom type rs232PortOutFlowType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ctsRts", 2),
          ("dsrDtr", 3),
          ("none", 1))
    )


_Rs232PortOutFlowType_Type.__name__ = "Integer32"
_Rs232PortOutFlowType_Object = MibTableColumn
rs232PortOutFlowType = _Rs232PortOutFlowType_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 2, 1, 8),
    _Rs232PortOutFlowType_Type()
)
rs232PortOutFlowType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PortOutFlowType.setStatus("current")
_Rs232AsyncPortTable_Object = MibTable
rs232AsyncPortTable = _Rs232AsyncPortTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3)
)
if mibBuilder.loadTexts:
    rs232AsyncPortTable.setStatus("current")
_Rs232AsyncPortEntry_Object = MibTableRow
rs232AsyncPortEntry = _Rs232AsyncPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1)
)
rs232AsyncPortEntry.setIndexNames(
    (0, "RS-232-MIB", "rs232AsyncPortIndex"),
)
if mibBuilder.loadTexts:
    rs232AsyncPortEntry.setStatus("current")
_Rs232AsyncPortIndex_Type = InterfaceIndex
_Rs232AsyncPortIndex_Object = MibTableColumn
rs232AsyncPortIndex = _Rs232AsyncPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 1),
    _Rs232AsyncPortIndex_Type()
)
rs232AsyncPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortIndex.setStatus("current")


class _Rs232AsyncPortBits_Type(Integer32):
    """Custom type rs232AsyncPortBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_Rs232AsyncPortBits_Type.__name__ = "Integer32"
_Rs232AsyncPortBits_Object = MibTableColumn
rs232AsyncPortBits = _Rs232AsyncPortBits_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 2),
    _Rs232AsyncPortBits_Type()
)
rs232AsyncPortBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortBits.setStatus("current")


class _Rs232AsyncPortStopBits_Type(Integer32):
    """Custom type rs232AsyncPortStopBits based on Integer32"""
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
        *(("dynamic", 4),
          ("one", 1),
          ("oneAndHalf", 3),
          ("two", 2))
    )


_Rs232AsyncPortStopBits_Type.__name__ = "Integer32"
_Rs232AsyncPortStopBits_Object = MibTableColumn
rs232AsyncPortStopBits = _Rs232AsyncPortStopBits_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 3),
    _Rs232AsyncPortStopBits_Type()
)
rs232AsyncPortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortStopBits.setStatus("current")


class _Rs232AsyncPortParity_Type(Integer32):
    """Custom type rs232AsyncPortParity based on Integer32"""
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


_Rs232AsyncPortParity_Type.__name__ = "Integer32"
_Rs232AsyncPortParity_Object = MibTableColumn
rs232AsyncPortParity = _Rs232AsyncPortParity_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 4),
    _Rs232AsyncPortParity_Type()
)
rs232AsyncPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortParity.setStatus("current")


class _Rs232AsyncPortAutobaud_Type(Integer32):
    """Custom type rs232AsyncPortAutobaud based on Integer32"""
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


_Rs232AsyncPortAutobaud_Type.__name__ = "Integer32"
_Rs232AsyncPortAutobaud_Object = MibTableColumn
rs232AsyncPortAutobaud = _Rs232AsyncPortAutobaud_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 5),
    _Rs232AsyncPortAutobaud_Type()
)
rs232AsyncPortAutobaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortAutobaud.setStatus("current")
_Rs232AsyncPortParityErrs_Type = Counter32
_Rs232AsyncPortParityErrs_Object = MibTableColumn
rs232AsyncPortParityErrs = _Rs232AsyncPortParityErrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 6),
    _Rs232AsyncPortParityErrs_Type()
)
rs232AsyncPortParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortParityErrs.setStatus("current")
_Rs232AsyncPortFramingErrs_Type = Counter32
_Rs232AsyncPortFramingErrs_Object = MibTableColumn
rs232AsyncPortFramingErrs = _Rs232AsyncPortFramingErrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 7),
    _Rs232AsyncPortFramingErrs_Type()
)
rs232AsyncPortFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortFramingErrs.setStatus("current")
_Rs232AsyncPortOverrunErrs_Type = Counter32
_Rs232AsyncPortOverrunErrs_Object = MibTableColumn
rs232AsyncPortOverrunErrs = _Rs232AsyncPortOverrunErrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 3, 1, 8),
    _Rs232AsyncPortOverrunErrs_Type()
)
rs232AsyncPortOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortOverrunErrs.setStatus("current")
_Rs232SyncPortTable_Object = MibTable
rs232SyncPortTable = _Rs232SyncPortTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4)
)
if mibBuilder.loadTexts:
    rs232SyncPortTable.setStatus("current")
_Rs232SyncPortEntry_Object = MibTableRow
rs232SyncPortEntry = _Rs232SyncPortEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1)
)
rs232SyncPortEntry.setIndexNames(
    (0, "RS-232-MIB", "rs232SyncPortIndex"),
)
if mibBuilder.loadTexts:
    rs232SyncPortEntry.setStatus("current")
_Rs232SyncPortIndex_Type = InterfaceIndex
_Rs232SyncPortIndex_Object = MibTableColumn
rs232SyncPortIndex = _Rs232SyncPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 1),
    _Rs232SyncPortIndex_Type()
)
rs232SyncPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortIndex.setStatus("current")


class _Rs232SyncPortClockSource_Type(Integer32):
    """Custom type rs232SyncPortClockSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("external", 2),
          ("internal", 1),
          ("split", 3))
    )


_Rs232SyncPortClockSource_Type.__name__ = "Integer32"
_Rs232SyncPortClockSource_Object = MibTableColumn
rs232SyncPortClockSource = _Rs232SyncPortClockSource_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 2),
    _Rs232SyncPortClockSource_Type()
)
rs232SyncPortClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232SyncPortClockSource.setStatus("current")
_Rs232SyncPortFrameCheckErrs_Type = Counter32
_Rs232SyncPortFrameCheckErrs_Object = MibTableColumn
rs232SyncPortFrameCheckErrs = _Rs232SyncPortFrameCheckErrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 3),
    _Rs232SyncPortFrameCheckErrs_Type()
)
rs232SyncPortFrameCheckErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortFrameCheckErrs.setStatus("current")
_Rs232SyncPortTransmitUnderrunErrs_Type = Counter32
_Rs232SyncPortTransmitUnderrunErrs_Object = MibTableColumn
rs232SyncPortTransmitUnderrunErrs = _Rs232SyncPortTransmitUnderrunErrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 4),
    _Rs232SyncPortTransmitUnderrunErrs_Type()
)
rs232SyncPortTransmitUnderrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortTransmitUnderrunErrs.setStatus("current")
_Rs232SyncPortReceiveOverrunErrs_Type = Counter32
_Rs232SyncPortReceiveOverrunErrs_Object = MibTableColumn
rs232SyncPortReceiveOverrunErrs = _Rs232SyncPortReceiveOverrunErrs_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 5),
    _Rs232SyncPortReceiveOverrunErrs_Type()
)
rs232SyncPortReceiveOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortReceiveOverrunErrs.setStatus("current")
_Rs232SyncPortInterruptedFrames_Type = Counter32
_Rs232SyncPortInterruptedFrames_Object = MibTableColumn
rs232SyncPortInterruptedFrames = _Rs232SyncPortInterruptedFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 6),
    _Rs232SyncPortInterruptedFrames_Type()
)
rs232SyncPortInterruptedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortInterruptedFrames.setStatus("current")
_Rs232SyncPortAbortedFrames_Type = Counter32
_Rs232SyncPortAbortedFrames_Object = MibTableColumn
rs232SyncPortAbortedFrames = _Rs232SyncPortAbortedFrames_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 7),
    _Rs232SyncPortAbortedFrames_Type()
)
rs232SyncPortAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortAbortedFrames.setStatus("current")


class _Rs232SyncPortRole_Type(Integer32):
    """Custom type rs232SyncPortRole based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dce", 2),
          ("dte", 1))
    )


_Rs232SyncPortRole_Type.__name__ = "Integer32"
_Rs232SyncPortRole_Object = MibTableColumn
rs232SyncPortRole = _Rs232SyncPortRole_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 8),
    _Rs232SyncPortRole_Type()
)
rs232SyncPortRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232SyncPortRole.setStatus("current")


class _Rs232SyncPortEncoding_Type(Integer32):
    """Custom type rs232SyncPortEncoding based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi", 2))
    )


_Rs232SyncPortEncoding_Type.__name__ = "Integer32"
_Rs232SyncPortEncoding_Object = MibTableColumn
rs232SyncPortEncoding = _Rs232SyncPortEncoding_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 9),
    _Rs232SyncPortEncoding_Type()
)
rs232SyncPortEncoding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232SyncPortEncoding.setStatus("current")


class _Rs232SyncPortRTSControl_Type(Integer32):
    """Custom type rs232SyncPortRTSControl based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constant", 2),
          ("controlled", 1))
    )


_Rs232SyncPortRTSControl_Type.__name__ = "Integer32"
_Rs232SyncPortRTSControl_Object = MibTableColumn
rs232SyncPortRTSControl = _Rs232SyncPortRTSControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 10),
    _Rs232SyncPortRTSControl_Type()
)
rs232SyncPortRTSControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232SyncPortRTSControl.setStatus("current")


class _Rs232SyncPortRTSCTSDelay_Type(Integer32):
    """Custom type rs232SyncPortRTSCTSDelay based on Integer32"""
    defaultValue = 0


_Rs232SyncPortRTSCTSDelay_Object = MibTableColumn
rs232SyncPortRTSCTSDelay = _Rs232SyncPortRTSCTSDelay_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 11),
    _Rs232SyncPortRTSCTSDelay_Type()
)
rs232SyncPortRTSCTSDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232SyncPortRTSCTSDelay.setStatus("current")


class _Rs232SyncPortMode_Type(Integer32):
    """Custom type rs232SyncPortMode based on Integer32"""
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
        *(("fdx", 1),
          ("hdx", 2),
          ("simplex-receive", 3),
          ("simplex-send", 4))
    )


_Rs232SyncPortMode_Type.__name__ = "Integer32"
_Rs232SyncPortMode_Object = MibTableColumn
rs232SyncPortMode = _Rs232SyncPortMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 12),
    _Rs232SyncPortMode_Type()
)
rs232SyncPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232SyncPortMode.setStatus("current")


class _Rs232SyncPortIdlePattern_Type(Integer32):
    """Custom type rs232SyncPortIdlePattern based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mark", 1),
          ("space", 2))
    )


_Rs232SyncPortIdlePattern_Type.__name__ = "Integer32"
_Rs232SyncPortIdlePattern_Object = MibTableColumn
rs232SyncPortIdlePattern = _Rs232SyncPortIdlePattern_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 13),
    _Rs232SyncPortIdlePattern_Type()
)
rs232SyncPortIdlePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232SyncPortIdlePattern.setStatus("current")


class _Rs232SyncPortMinFlags_Type(Integer32):
    """Custom type rs232SyncPortMinFlags based on Integer32"""
    defaultValue = 2


_Rs232SyncPortMinFlags_Object = MibTableColumn
rs232SyncPortMinFlags = _Rs232SyncPortMinFlags_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 4, 1, 14),
    _Rs232SyncPortMinFlags_Type()
)
rs232SyncPortMinFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232SyncPortMinFlags.setStatus("current")
_Rs232InSigTable_Object = MibTable
rs232InSigTable = _Rs232InSigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 5)
)
if mibBuilder.loadTexts:
    rs232InSigTable.setStatus("current")
_Rs232InSigEntry_Object = MibTableRow
rs232InSigEntry = _Rs232InSigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 5, 1)
)
rs232InSigEntry.setIndexNames(
    (0, "RS-232-MIB", "rs232InSigPortIndex"),
    (0, "RS-232-MIB", "rs232InSigName"),
)
if mibBuilder.loadTexts:
    rs232InSigEntry.setStatus("current")
_Rs232InSigPortIndex_Type = InterfaceIndex
_Rs232InSigPortIndex_Object = MibTableColumn
rs232InSigPortIndex = _Rs232InSigPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 1),
    _Rs232InSigPortIndex_Type()
)
rs232InSigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigPortIndex.setStatus("current")


class _Rs232InSigName_Type(Integer32):
    """Custom type rs232InSigName based on Integer32"""
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
        *(("cts", 2),
          ("dcd", 6),
          ("dsr", 3),
          ("dtr", 4),
          ("ri", 5),
          ("rts", 1),
          ("scts", 10),
          ("sdcd", 11),
          ("sq", 7),
          ("srs", 8),
          ("srts", 9))
    )


_Rs232InSigName_Type.__name__ = "Integer32"
_Rs232InSigName_Object = MibTableColumn
rs232InSigName = _Rs232InSigName_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 2),
    _Rs232InSigName_Type()
)
rs232InSigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigName.setStatus("current")


class _Rs232InSigState_Type(Integer32):
    """Custom type rs232InSigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off", 3),
          ("on", 2))
    )


_Rs232InSigState_Type.__name__ = "Integer32"
_Rs232InSigState_Object = MibTableColumn
rs232InSigState = _Rs232InSigState_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 3),
    _Rs232InSigState_Type()
)
rs232InSigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigState.setStatus("current")
_Rs232InSigChanges_Type = Counter32
_Rs232InSigChanges_Object = MibTableColumn
rs232InSigChanges = _Rs232InSigChanges_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 5, 1, 4),
    _Rs232InSigChanges_Type()
)
rs232InSigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigChanges.setStatus("current")
_Rs232OutSigTable_Object = MibTable
rs232OutSigTable = _Rs232OutSigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 6)
)
if mibBuilder.loadTexts:
    rs232OutSigTable.setStatus("current")
_Rs232OutSigEntry_Object = MibTableRow
rs232OutSigEntry = _Rs232OutSigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 6, 1)
)
rs232OutSigEntry.setIndexNames(
    (0, "RS-232-MIB", "rs232OutSigPortIndex"),
    (0, "RS-232-MIB", "rs232OutSigName"),
)
if mibBuilder.loadTexts:
    rs232OutSigEntry.setStatus("current")
_Rs232OutSigPortIndex_Type = InterfaceIndex
_Rs232OutSigPortIndex_Object = MibTableColumn
rs232OutSigPortIndex = _Rs232OutSigPortIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 1),
    _Rs232OutSigPortIndex_Type()
)
rs232OutSigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigPortIndex.setStatus("current")


class _Rs232OutSigName_Type(Integer32):
    """Custom type rs232OutSigName based on Integer32"""
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
        *(("cts", 2),
          ("dcd", 6),
          ("dsr", 3),
          ("dtr", 4),
          ("ri", 5),
          ("rts", 1),
          ("scts", 10),
          ("sdcd", 11),
          ("sq", 7),
          ("srs", 8),
          ("srts", 9))
    )


_Rs232OutSigName_Type.__name__ = "Integer32"
_Rs232OutSigName_Object = MibTableColumn
rs232OutSigName = _Rs232OutSigName_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 2),
    _Rs232OutSigName_Type()
)
rs232OutSigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigName.setStatus("current")


class _Rs232OutSigState_Type(Integer32):
    """Custom type rs232OutSigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("off", 3),
          ("on", 2))
    )


_Rs232OutSigState_Type.__name__ = "Integer32"
_Rs232OutSigState_Object = MibTableColumn
rs232OutSigState = _Rs232OutSigState_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 3),
    _Rs232OutSigState_Type()
)
rs232OutSigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigState.setStatus("current")
_Rs232OutSigChanges_Type = Counter32
_Rs232OutSigChanges_Object = MibTableColumn
rs232OutSigChanges = _Rs232OutSigChanges_Object(
    (1, 3, 6, 1, 2, 1, 10, 33, 6, 1, 4),
    _Rs232OutSigChanges_Type()
)
rs232OutSigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigChanges.setStatus("current")
_Rs232Conformance_ObjectIdentity = ObjectIdentity
rs232Conformance = _Rs232Conformance_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 33, 7)
)
_Rs232Groups_ObjectIdentity = ObjectIdentity
rs232Groups = _Rs232Groups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 33, 7, 1)
)
_Rs232Compliances_ObjectIdentity = ObjectIdentity
rs232Compliances = _Rs232Compliances_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 33, 7, 2)
)

# Managed Objects groups

rs232Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 1)
)
rs232Group.setObjects(
      *(("RS-232-MIB", "rs232Number"),
        ("RS-232-MIB", "rs232PortIndex"),
        ("RS-232-MIB", "rs232PortType"),
        ("RS-232-MIB", "rs232PortInSigNumber"),
        ("RS-232-MIB", "rs232PortOutSigNumber"),
        ("RS-232-MIB", "rs232PortInSpeed"),
        ("RS-232-MIB", "rs232PortOutSpeed"),
        ("RS-232-MIB", "rs232PortInFlowType"),
        ("RS-232-MIB", "rs232PortOutFlowType"),
        ("RS-232-MIB", "rs232InSigPortIndex"),
        ("RS-232-MIB", "rs232InSigName"),
        ("RS-232-MIB", "rs232InSigState"),
        ("RS-232-MIB", "rs232InSigChanges"),
        ("RS-232-MIB", "rs232OutSigPortIndex"),
        ("RS-232-MIB", "rs232OutSigName"),
        ("RS-232-MIB", "rs232OutSigState"),
        ("RS-232-MIB", "rs232OutSigChanges"))
)
if mibBuilder.loadTexts:
    rs232Group.setStatus("current")

rs232AsyncGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 2)
)
rs232AsyncGroup.setObjects(
      *(("RS-232-MIB", "rs232AsyncPortIndex"),
        ("RS-232-MIB", "rs232AsyncPortBits"),
        ("RS-232-MIB", "rs232AsyncPortStopBits"),
        ("RS-232-MIB", "rs232AsyncPortParity"),
        ("RS-232-MIB", "rs232AsyncPortAutobaud"),
        ("RS-232-MIB", "rs232AsyncPortParityErrs"),
        ("RS-232-MIB", "rs232AsyncPortFramingErrs"),
        ("RS-232-MIB", "rs232AsyncPortOverrunErrs"))
)
if mibBuilder.loadTexts:
    rs232AsyncGroup.setStatus("current")

rs232SyncGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 3)
)
rs232SyncGroup.setObjects(
      *(("RS-232-MIB", "rs232SyncPortIndex"),
        ("RS-232-MIB", "rs232SyncPortClockSource"),
        ("RS-232-MIB", "rs232SyncPortFrameCheckErrs"),
        ("RS-232-MIB", "rs232SyncPortTransmitUnderrunErrs"),
        ("RS-232-MIB", "rs232SyncPortReceiveOverrunErrs"),
        ("RS-232-MIB", "rs232SyncPortInterruptedFrames"),
        ("RS-232-MIB", "rs232SyncPortAbortedFrames"))
)
if mibBuilder.loadTexts:
    rs232SyncGroup.setStatus("current")

rs232SyncSDLCGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 33, 7, 1, 4)
)
rs232SyncSDLCGroup.setObjects(
      *(("RS-232-MIB", "rs232SyncPortRole"),
        ("RS-232-MIB", "rs232SyncPortEncoding"),
        ("RS-232-MIB", "rs232SyncPortRTSControl"),
        ("RS-232-MIB", "rs232SyncPortRTSCTSDelay"),
        ("RS-232-MIB", "rs232SyncPortMode"),
        ("RS-232-MIB", "rs232SyncPortIdlePattern"),
        ("RS-232-MIB", "rs232SyncPortMinFlags"))
)
if mibBuilder.loadTexts:
    rs232SyncSDLCGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

rs232Compliance = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 33, 7, 2, 1)
)
if mibBuilder.loadTexts:
    rs232Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RS-232-MIB",
    **{"rs232": rs232,
       "rs232Number": rs232Number,
       "rs232PortTable": rs232PortTable,
       "rs232PortEntry": rs232PortEntry,
       "rs232PortIndex": rs232PortIndex,
       "rs232PortType": rs232PortType,
       "rs232PortInSigNumber": rs232PortInSigNumber,
       "rs232PortOutSigNumber": rs232PortOutSigNumber,
       "rs232PortInSpeed": rs232PortInSpeed,
       "rs232PortOutSpeed": rs232PortOutSpeed,
       "rs232PortInFlowType": rs232PortInFlowType,
       "rs232PortOutFlowType": rs232PortOutFlowType,
       "rs232AsyncPortTable": rs232AsyncPortTable,
       "rs232AsyncPortEntry": rs232AsyncPortEntry,
       "rs232AsyncPortIndex": rs232AsyncPortIndex,
       "rs232AsyncPortBits": rs232AsyncPortBits,
       "rs232AsyncPortStopBits": rs232AsyncPortStopBits,
       "rs232AsyncPortParity": rs232AsyncPortParity,
       "rs232AsyncPortAutobaud": rs232AsyncPortAutobaud,
       "rs232AsyncPortParityErrs": rs232AsyncPortParityErrs,
       "rs232AsyncPortFramingErrs": rs232AsyncPortFramingErrs,
       "rs232AsyncPortOverrunErrs": rs232AsyncPortOverrunErrs,
       "rs232SyncPortTable": rs232SyncPortTable,
       "rs232SyncPortEntry": rs232SyncPortEntry,
       "rs232SyncPortIndex": rs232SyncPortIndex,
       "rs232SyncPortClockSource": rs232SyncPortClockSource,
       "rs232SyncPortFrameCheckErrs": rs232SyncPortFrameCheckErrs,
       "rs232SyncPortTransmitUnderrunErrs": rs232SyncPortTransmitUnderrunErrs,
       "rs232SyncPortReceiveOverrunErrs": rs232SyncPortReceiveOverrunErrs,
       "rs232SyncPortInterruptedFrames": rs232SyncPortInterruptedFrames,
       "rs232SyncPortAbortedFrames": rs232SyncPortAbortedFrames,
       "rs232SyncPortRole": rs232SyncPortRole,
       "rs232SyncPortEncoding": rs232SyncPortEncoding,
       "rs232SyncPortRTSControl": rs232SyncPortRTSControl,
       "rs232SyncPortRTSCTSDelay": rs232SyncPortRTSCTSDelay,
       "rs232SyncPortMode": rs232SyncPortMode,
       "rs232SyncPortIdlePattern": rs232SyncPortIdlePattern,
       "rs232SyncPortMinFlags": rs232SyncPortMinFlags,
       "rs232InSigTable": rs232InSigTable,
       "rs232InSigEntry": rs232InSigEntry,
       "rs232InSigPortIndex": rs232InSigPortIndex,
       "rs232InSigName": rs232InSigName,
       "rs232InSigState": rs232InSigState,
       "rs232InSigChanges": rs232InSigChanges,
       "rs232OutSigTable": rs232OutSigTable,
       "rs232OutSigEntry": rs232OutSigEntry,
       "rs232OutSigPortIndex": rs232OutSigPortIndex,
       "rs232OutSigName": rs232OutSigName,
       "rs232OutSigState": rs232OutSigState,
       "rs232OutSigChanges": rs232OutSigChanges,
       "rs232Conformance": rs232Conformance,
       "rs232Groups": rs232Groups,
       "rs232Group": rs232Group,
       "rs232AsyncGroup": rs232AsyncGroup,
       "rs232SyncGroup": rs232SyncGroup,
       "rs232SyncSDLCGroup": rs232SyncSDLCGroup,
       "rs232Compliances": rs232Compliances,
       "rs232Compliance": rs232Compliance}
)
