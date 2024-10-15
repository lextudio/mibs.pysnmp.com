# SNMP MIB module (RS232-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/RS232-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:48:24 2024
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

_Rs232_ObjectIdentity = ObjectIdentity
rs232 = _Rs232_ObjectIdentity(
    (1, 3, 6, 1, 3, 20)
)
_Rs232Number_Type = Integer32
_Rs232Number_Object = MibScalar
rs232Number = _Rs232Number_Object(
    (1, 3, 6, 1, 3, 20, 1),
    _Rs232Number_Type()
)
rs232Number.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232Number.setStatus("mandatory")
_Rs232PortTable_Object = MibTable
rs232PortTable = _Rs232PortTable_Object(
    (1, 3, 6, 1, 3, 20, 2)
)
if mibBuilder.loadTexts:
    rs232PortTable.setStatus("mandatory")
_Rs232PortEntry_Object = MibTableRow
rs232PortEntry = _Rs232PortEntry_Object(
    (1, 3, 6, 1, 3, 20, 2, 1)
)
rs232PortEntry.setIndexNames(
    (0, "RS232-MIB", "rs232PortIndex"),
)
if mibBuilder.loadTexts:
    rs232PortEntry.setStatus("mandatory")
_Rs232PortIndex_Type = Integer32
_Rs232PortIndex_Object = MibTableColumn
rs232PortIndex = _Rs232PortIndex_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 1),
    _Rs232PortIndex_Type()
)
rs232PortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortIndex.setStatus("mandatory")


class _Rs232PortType_Type(Integer32):
    """Custom type rs232PortType based on Integer32"""
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
        *(("other", 1),
          ("rs232", 2),
          ("rs422", 3),
          ("rs423", 4),
          ("v35", 5))
    )


_Rs232PortType_Type.__name__ = "Integer32"
_Rs232PortType_Object = MibTableColumn
rs232PortType = _Rs232PortType_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 2),
    _Rs232PortType_Type()
)
rs232PortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortType.setStatus("mandatory")
_Rs232PortInSigNumber_Type = Integer32
_Rs232PortInSigNumber_Object = MibTableColumn
rs232PortInSigNumber = _Rs232PortInSigNumber_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 3),
    _Rs232PortInSigNumber_Type()
)
rs232PortInSigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortInSigNumber.setStatus("mandatory")
_Rs232PortOutSigNumber_Type = Integer32
_Rs232PortOutSigNumber_Object = MibTableColumn
rs232PortOutSigNumber = _Rs232PortOutSigNumber_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 4),
    _Rs232PortOutSigNumber_Type()
)
rs232PortOutSigNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232PortOutSigNumber.setStatus("mandatory")
_Rs232PortInSpeed_Type = Integer32
_Rs232PortInSpeed_Object = MibTableColumn
rs232PortInSpeed = _Rs232PortInSpeed_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 5),
    _Rs232PortInSpeed_Type()
)
rs232PortInSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PortInSpeed.setStatus("mandatory")
_Rs232PortOutSpeed_Type = Integer32
_Rs232PortOutSpeed_Object = MibTableColumn
rs232PortOutSpeed = _Rs232PortOutSpeed_Object(
    (1, 3, 6, 1, 3, 20, 2, 1, 6),
    _Rs232PortOutSpeed_Type()
)
rs232PortOutSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232PortOutSpeed.setStatus("mandatory")
_Rs232AsyncPortTable_Object = MibTable
rs232AsyncPortTable = _Rs232AsyncPortTable_Object(
    (1, 3, 6, 1, 3, 20, 3)
)
if mibBuilder.loadTexts:
    rs232AsyncPortTable.setStatus("mandatory")
_Rs232AsyncPortEntry_Object = MibTableRow
rs232AsyncPortEntry = _Rs232AsyncPortEntry_Object(
    (1, 3, 6, 1, 3, 20, 3, 1)
)
rs232AsyncPortEntry.setIndexNames(
    (0, "RS232-MIB", "rs232AsyncPortIndex"),
)
if mibBuilder.loadTexts:
    rs232AsyncPortEntry.setStatus("mandatory")
_Rs232AsyncPortIndex_Type = Integer32
_Rs232AsyncPortIndex_Object = MibTableColumn
rs232AsyncPortIndex = _Rs232AsyncPortIndex_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 1),
    _Rs232AsyncPortIndex_Type()
)
rs232AsyncPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortIndex.setStatus("mandatory")


class _Rs232AsyncPortBits_Type(Integer32):
    """Custom type rs232AsyncPortBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_Rs232AsyncPortBits_Type.__name__ = "Integer32"
_Rs232AsyncPortBits_Object = MibTableColumn
rs232AsyncPortBits = _Rs232AsyncPortBits_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 2),
    _Rs232AsyncPortBits_Type()
)
rs232AsyncPortBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortBits.setStatus("mandatory")


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
          ("one-and-half", 3),
          ("two", 2))
    )


_Rs232AsyncPortStopBits_Type.__name__ = "Integer32"
_Rs232AsyncPortStopBits_Object = MibTableColumn
rs232AsyncPortStopBits = _Rs232AsyncPortStopBits_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 3),
    _Rs232AsyncPortStopBits_Type()
)
rs232AsyncPortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortStopBits.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 20, 3, 1, 4),
    _Rs232AsyncPortParity_Type()
)
rs232AsyncPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortParity.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 20, 3, 1, 5),
    _Rs232AsyncPortAutobaud_Type()
)
rs232AsyncPortAutobaud.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232AsyncPortAutobaud.setStatus("mandatory")
_Rs232AsyncPortParityErrs_Type = Counter32
_Rs232AsyncPortParityErrs_Object = MibTableColumn
rs232AsyncPortParityErrs = _Rs232AsyncPortParityErrs_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 6),
    _Rs232AsyncPortParityErrs_Type()
)
rs232AsyncPortParityErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortParityErrs.setStatus("mandatory")
_Rs232AsyncPortFramingErrs_Type = Counter32
_Rs232AsyncPortFramingErrs_Object = MibTableColumn
rs232AsyncPortFramingErrs = _Rs232AsyncPortFramingErrs_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 7),
    _Rs232AsyncPortFramingErrs_Type()
)
rs232AsyncPortFramingErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortFramingErrs.setStatus("mandatory")
_Rs232AsyncPortOverrunErrs_Type = Counter32
_Rs232AsyncPortOverrunErrs_Object = MibTableColumn
rs232AsyncPortOverrunErrs = _Rs232AsyncPortOverrunErrs_Object(
    (1, 3, 6, 1, 3, 20, 3, 1, 8),
    _Rs232AsyncPortOverrunErrs_Type()
)
rs232AsyncPortOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232AsyncPortOverrunErrs.setStatus("mandatory")
_Rs232SyncPortTable_Object = MibTable
rs232SyncPortTable = _Rs232SyncPortTable_Object(
    (1, 3, 6, 1, 3, 20, 4)
)
if mibBuilder.loadTexts:
    rs232SyncPortTable.setStatus("mandatory")
_Rs232SyncPortEntry_Object = MibTableRow
rs232SyncPortEntry = _Rs232SyncPortEntry_Object(
    (1, 3, 6, 1, 3, 20, 4, 1)
)
rs232SyncPortEntry.setIndexNames(
    (0, "RS232-MIB", "rs232SyncPortIndex"),
)
if mibBuilder.loadTexts:
    rs232SyncPortEntry.setStatus("mandatory")
_Rs232SyncPortIndex_Type = Integer32
_Rs232SyncPortIndex_Object = MibTableColumn
rs232SyncPortIndex = _Rs232SyncPortIndex_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 1),
    _Rs232SyncPortIndex_Type()
)
rs232SyncPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 20, 4, 1, 2),
    _Rs232SyncPortClockSource_Type()
)
rs232SyncPortClockSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rs232SyncPortClockSource.setStatus("mandatory")
_Rs232SyncPortFrameCheckErrs_Type = Counter32
_Rs232SyncPortFrameCheckErrs_Object = MibTableColumn
rs232SyncPortFrameCheckErrs = _Rs232SyncPortFrameCheckErrs_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 3),
    _Rs232SyncPortFrameCheckErrs_Type()
)
rs232SyncPortFrameCheckErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortFrameCheckErrs.setStatus("mandatory")
_Rs232SyncPortTransmitUnderrunErrs_Type = Counter32
_Rs232SyncPortTransmitUnderrunErrs_Object = MibTableColumn
rs232SyncPortTransmitUnderrunErrs = _Rs232SyncPortTransmitUnderrunErrs_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 4),
    _Rs232SyncPortTransmitUnderrunErrs_Type()
)
rs232SyncPortTransmitUnderrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortTransmitUnderrunErrs.setStatus("mandatory")
_Rs232SyncPortReceiveOverrunErrs_Type = Counter32
_Rs232SyncPortReceiveOverrunErrs_Object = MibTableColumn
rs232SyncPortReceiveOverrunErrs = _Rs232SyncPortReceiveOverrunErrs_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 5),
    _Rs232SyncPortReceiveOverrunErrs_Type()
)
rs232SyncPortReceiveOverrunErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortReceiveOverrunErrs.setStatus("mandatory")
_Rs232SyncPortInterruptedFrames_Type = Counter32
_Rs232SyncPortInterruptedFrames_Object = MibTableColumn
rs232SyncPortInterruptedFrames = _Rs232SyncPortInterruptedFrames_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 6),
    _Rs232SyncPortInterruptedFrames_Type()
)
rs232SyncPortInterruptedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortInterruptedFrames.setStatus("mandatory")
_Rs232SyncPortAbortedFrames_Type = Counter32
_Rs232SyncPortAbortedFrames_Object = MibTableColumn
rs232SyncPortAbortedFrames = _Rs232SyncPortAbortedFrames_Object(
    (1, 3, 6, 1, 3, 20, 4, 1, 7),
    _Rs232SyncPortAbortedFrames_Type()
)
rs232SyncPortAbortedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232SyncPortAbortedFrames.setStatus("mandatory")
_Rs232InSigTable_Object = MibTable
rs232InSigTable = _Rs232InSigTable_Object(
    (1, 3, 6, 1, 3, 20, 5)
)
if mibBuilder.loadTexts:
    rs232InSigTable.setStatus("mandatory")
_Rs232InSigEntry_Object = MibTableRow
rs232InSigEntry = _Rs232InSigEntry_Object(
    (1, 3, 6, 1, 3, 20, 5, 1)
)
rs232InSigEntry.setIndexNames(
    (0, "RS232-MIB", "rs232InSigPortIndex"),
    (0, "RS232-MIB", "rs232InSigName"),
)
if mibBuilder.loadTexts:
    rs232InSigEntry.setStatus("mandatory")
_Rs232InSigPortIndex_Type = Integer32
_Rs232InSigPortIndex_Object = MibTableColumn
rs232InSigPortIndex = _Rs232InSigPortIndex_Object(
    (1, 3, 6, 1, 3, 20, 5, 1, 1),
    _Rs232InSigPortIndex_Type()
)
rs232InSigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigPortIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 20, 5, 1, 2),
    _Rs232InSigName_Type()
)
rs232InSigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigName.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 20, 5, 1, 3),
    _Rs232InSigState_Type()
)
rs232InSigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigState.setStatus("mandatory")
_Rs232InSigChanges_Type = Counter32
_Rs232InSigChanges_Object = MibTableColumn
rs232InSigChanges = _Rs232InSigChanges_Object(
    (1, 3, 6, 1, 3, 20, 5, 1, 4),
    _Rs232InSigChanges_Type()
)
rs232InSigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232InSigChanges.setStatus("mandatory")
_Rs232OutSigTable_Object = MibTable
rs232OutSigTable = _Rs232OutSigTable_Object(
    (1, 3, 6, 1, 3, 20, 6)
)
if mibBuilder.loadTexts:
    rs232OutSigTable.setStatus("mandatory")
_Rs232OutSigEntry_Object = MibTableRow
rs232OutSigEntry = _Rs232OutSigEntry_Object(
    (1, 3, 6, 1, 3, 20, 6, 1)
)
rs232OutSigEntry.setIndexNames(
    (0, "RS232-MIB", "rs232OutSigPortIndex"),
    (0, "RS232-MIB", "rs232OutSigName"),
)
if mibBuilder.loadTexts:
    rs232OutSigEntry.setStatus("mandatory")
_Rs232OutSigPortIndex_Type = Integer32
_Rs232OutSigPortIndex_Object = MibTableColumn
rs232OutSigPortIndex = _Rs232OutSigPortIndex_Object(
    (1, 3, 6, 1, 3, 20, 6, 1, 1),
    _Rs232OutSigPortIndex_Type()
)
rs232OutSigPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigPortIndex.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 20, 6, 1, 2),
    _Rs232OutSigName_Type()
)
rs232OutSigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigName.setStatus("mandatory")


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
    (1, 3, 6, 1, 3, 20, 6, 1, 3),
    _Rs232OutSigState_Type()
)
rs232OutSigState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigState.setStatus("mandatory")
_Rs232OutSigChanges_Type = Counter32
_Rs232OutSigChanges_Object = MibTableColumn
rs232OutSigChanges = _Rs232OutSigChanges_Object(
    (1, 3, 6, 1, 3, 20, 6, 1, 4),
    _Rs232OutSigChanges_Type()
)
rs232OutSigChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rs232OutSigChanges.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RS232-MIB",
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
       "rs232OutSigChanges": rs232OutSigChanges}
)
