# SNMP MIB module (Wellfleet-CONSOLE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/Wellfleet-CONSOLE-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 23:15:57 2024
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

(wfSerialPortGroup,
 wfServices) = mibBuilder.importSymbols(
    "Wellfleet-COMMON-MIB",
    "wfSerialPortGroup",
    "wfServices")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WfConsole_ObjectIdentity = ObjectIdentity
wfConsole = _WfConsole_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1)
)


class _WfBaudRate_Type(Integer32):
    """Custom type wfBaudRate based on Integer32"""
    defaultValue = 9600


_WfBaudRate_Object = MibScalar
wfBaudRate = _WfBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 1),
    _WfBaudRate_Type()
)
wfBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfBaudRate.setStatus("obsolete")


class _WfDataBits_Type(Integer32):
    """Custom type wfDataBits based on Integer32"""
    defaultValue = 8


_WfDataBits_Object = MibScalar
wfDataBits = _WfDataBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 2),
    _WfDataBits_Type()
)
wfDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfDataBits.setStatus("obsolete")


class _WfParity_Type(Integer32):
    """Custom type wfParity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_WfParity_Type.__name__ = "Integer32"
_WfParity_Object = MibScalar
wfParity = _WfParity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 3),
    _WfParity_Type()
)
wfParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfParity.setStatus("obsolete")


class _WfStopBits_Type(Integer32):
    """Custom type wfStopBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("s15bit", 2),
          ("s1bit", 1),
          ("s2bit", 3))
    )


_WfStopBits_Type.__name__ = "Integer32"
_WfStopBits_Object = MibScalar
wfStopBits = _WfStopBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 4),
    _WfStopBits_Type()
)
wfStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfStopBits.setStatus("obsolete")


class _WfModemEnable_Type(Integer32):
    """Custom type wfModemEnable based on Integer32"""
    defaultValue = 2

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


_WfModemEnable_Type.__name__ = "Integer32"
_WfModemEnable_Object = MibScalar
wfModemEnable = _WfModemEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 5),
    _WfModemEnable_Type()
)
wfModemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfModemEnable.setStatus("obsolete")


class _WfLinesPerScreen_Type(Integer32):
    """Custom type wfLinesPerScreen based on Integer32"""
    defaultValue = 24


_WfLinesPerScreen_Object = MibScalar
wfLinesPerScreen = _WfLinesPerScreen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 6),
    _WfLinesPerScreen_Type()
)
wfLinesPerScreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLinesPerScreen.setStatus("obsolete")


class _WfMoreEnable_Type(Integer32):
    """Custom type wfMoreEnable based on Integer32"""
    defaultValue = 1

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


_WfMoreEnable_Type.__name__ = "Integer32"
_WfMoreEnable_Object = MibScalar
wfMoreEnable = _WfMoreEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 7),
    _WfMoreEnable_Type()
)
wfMoreEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfMoreEnable.setStatus("obsolete")
_WfPrompt_Type = DisplayString
_WfPrompt_Object = MibScalar
wfPrompt = _WfPrompt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 8),
    _WfPrompt_Type()
)
wfPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPrompt.setStatus("obsolete")


class _WfLoginTimeOut_Type(Integer32):
    """Custom type wfLoginTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfLoginTimeOut_Type.__name__ = "Integer32"
_WfLoginTimeOut_Object = MibScalar
wfLoginTimeOut = _WfLoginTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 9),
    _WfLoginTimeOut_Type()
)
wfLoginTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLoginTimeOut.setStatus("obsolete")


class _WfPasswordTimeOut_Type(Integer32):
    """Custom type wfPasswordTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfPasswordTimeOut_Type.__name__ = "Integer32"
_WfPasswordTimeOut_Object = MibScalar
wfPasswordTimeOut = _WfPasswordTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 10),
    _WfPasswordTimeOut_Type()
)
wfPasswordTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfPasswordTimeOut.setStatus("obsolete")


class _WfCommandTimeOut_Type(Integer32):
    """Custom type wfCommandTimeOut based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfCommandTimeOut_Type.__name__ = "Integer32"
_WfCommandTimeOut_Object = MibScalar
wfCommandTimeOut = _WfCommandTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 11),
    _WfCommandTimeOut_Type()
)
wfCommandTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfCommandTimeOut.setStatus("obsolete")


class _WfLoginRetries_Type(Integer32):
    """Custom type wfLoginRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfLoginRetries_Type.__name__ = "Integer32"
_WfLoginRetries_Object = MibScalar
wfLoginRetries = _WfLoginRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 12),
    _WfLoginRetries_Type()
)
wfLoginRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfLoginRetries.setStatus("obsolete")
_WfTotalLogins_Type = Counter32
_WfTotalLogins_Object = MibScalar
wfTotalLogins = _WfTotalLogins_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 13),
    _WfTotalLogins_Type()
)
wfTotalLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTotalLogins.setStatus("obsolete")
_WfUserLoginErrors_Type = Counter32
_WfUserLoginErrors_Object = MibScalar
wfUserLoginErrors = _WfUserLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 14),
    _WfUserLoginErrors_Type()
)
wfUserLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfUserLoginErrors.setStatus("obsolete")
_WfManagerLoginErrors_Type = Counter32
_WfManagerLoginErrors_Object = MibScalar
wfManagerLoginErrors = _WfManagerLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 15),
    _WfManagerLoginErrors_Type()
)
wfManagerLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfManagerLoginErrors.setStatus("obsolete")
_WfOtherLoginErrors_Type = Counter32
_WfOtherLoginErrors_Object = MibScalar
wfOtherLoginErrors = _WfOtherLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 16),
    _WfOtherLoginErrors_Type()
)
wfOtherLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfOtherLoginErrors.setStatus("obsolete")
_WfTtyFrameErrors_Type = Counter32
_WfTtyFrameErrors_Object = MibScalar
wfTtyFrameErrors = _WfTtyFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 17),
    _WfTtyFrameErrors_Type()
)
wfTtyFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTtyFrameErrors.setStatus("obsolete")
_WfTtyOverrunErrors_Type = Counter32
_WfTtyOverrunErrors_Object = MibScalar
wfTtyOverrunErrors = _WfTtyOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 18),
    _WfTtyOverrunErrors_Type()
)
wfTtyOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTtyOverrunErrors.setStatus("obsolete")
_WfTtyParityErrors_Type = Counter32
_WfTtyParityErrors_Object = MibScalar
wfTtyParityErrors = _WfTtyParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 19),
    _WfTtyParityErrors_Type()
)
wfTtyParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTtyParityErrors.setStatus("obsolete")
_WfTtyInfifoErrors_Type = Counter32
_WfTtyInfifoErrors_Object = MibScalar
wfTtyInfifoErrors = _WfTtyInfifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 1, 20),
    _WfTtyInfifoErrors_Type()
)
wfTtyInfifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfTtyInfifoErrors.setStatus("obsolete")
_WfSerialPortTable_Object = MibTable
wfSerialPortTable = _WfSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1)
)
if mibBuilder.loadTexts:
    wfSerialPortTable.setStatus("mandatory")
_WfSerialPortEntry_Object = MibTableRow
wfSerialPortEntry = _WfSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1)
)
wfSerialPortEntry.setIndexNames(
    (0, "Wellfleet-CONSOLE-MIB", "wfSerialPortNumber"),
)
if mibBuilder.loadTexts:
    wfSerialPortEntry.setStatus("mandatory")


class _WfSerialPortDelete_Type(Integer32):
    """Custom type wfSerialPortDelete based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("created", 1),
          ("deleted", 2))
    )


_WfSerialPortDelete_Type.__name__ = "Integer32"
_WfSerialPortDelete_Object = MibTableColumn
wfSerialPortDelete = _WfSerialPortDelete_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 1),
    _WfSerialPortDelete_Type()
)
wfSerialPortDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortDelete.setStatus("mandatory")


class _WfSerialPortDisable_Type(Integer32):
    """Custom type wfSerialPortDisable based on Integer32"""
    defaultValue = 1

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


_WfSerialPortDisable_Type.__name__ = "Integer32"
_WfSerialPortDisable_Object = MibTableColumn
wfSerialPortDisable = _WfSerialPortDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 2),
    _WfSerialPortDisable_Type()
)
wfSerialPortDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortDisable.setStatus("mandatory")


class _WfSerialPortState_Type(Integer32):
    """Custom type wfSerialPortState based on Integer32"""
    defaultValue = 4

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
        *(("down", 2),
          ("init", 3),
          ("notpresent", 4),
          ("up", 1))
    )


_WfSerialPortState_Type.__name__ = "Integer32"
_WfSerialPortState_Object = MibTableColumn
wfSerialPortState = _WfSerialPortState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 3),
    _WfSerialPortState_Type()
)
wfSerialPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortState.setStatus("mandatory")
_WfSerialPortNumber_Type = Integer32
_WfSerialPortNumber_Object = MibTableColumn
wfSerialPortNumber = _WfSerialPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 4),
    _WfSerialPortNumber_Type()
)
wfSerialPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortNumber.setStatus("mandatory")
_WfSerialPortName_Type = DisplayString
_WfSerialPortName_Object = MibTableColumn
wfSerialPortName = _WfSerialPortName_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 5),
    _WfSerialPortName_Type()
)
wfSerialPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortName.setStatus("mandatory")


class _WfSerialPortSlot_Type(Integer32):
    """Custom type wfSerialPortSlot based on Integer32"""
    defaultValue = 0


_WfSerialPortSlot_Object = MibTableColumn
wfSerialPortSlot = _WfSerialPortSlot_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 6),
    _WfSerialPortSlot_Type()
)
wfSerialPortSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortSlot.setStatus("mandatory")


class _WfSerialPortType_Type(Integer32):
    """Custom type wfSerialPortType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("printer", 2),
          ("rtelnet", 3),
          ("ti", 1))
    )


_WfSerialPortType_Type.__name__ = "Integer32"
_WfSerialPortType_Object = MibTableColumn
wfSerialPortType = _WfSerialPortType_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 7),
    _WfSerialPortType_Type()
)
wfSerialPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortType.setStatus("mandatory")


class _WfSerialPortBaudRate_Type(Integer32):
    """Custom type wfSerialPortBaudRate based on Integer32"""
    defaultValue = 9600


_WfSerialPortBaudRate_Object = MibTableColumn
wfSerialPortBaudRate = _WfSerialPortBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 8),
    _WfSerialPortBaudRate_Type()
)
wfSerialPortBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortBaudRate.setStatus("mandatory")


class _WfSerialPortDataBits_Type(Integer32):
    """Custom type wfSerialPortDataBits based on Integer32"""
    defaultValue = 8


_WfSerialPortDataBits_Object = MibTableColumn
wfSerialPortDataBits = _WfSerialPortDataBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 9),
    _WfSerialPortDataBits_Type()
)
wfSerialPortDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortDataBits.setStatus("mandatory")


class _WfSerialPortParity_Type(Integer32):
    """Custom type wfSerialPortParity based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("even", 3),
          ("none", 1),
          ("odd", 2))
    )


_WfSerialPortParity_Type.__name__ = "Integer32"
_WfSerialPortParity_Object = MibTableColumn
wfSerialPortParity = _WfSerialPortParity_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 10),
    _WfSerialPortParity_Type()
)
wfSerialPortParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortParity.setStatus("mandatory")


class _WfSerialPortStopBits_Type(Integer32):
    """Custom type wfSerialPortStopBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("s15bit", 2),
          ("s1bit", 1),
          ("s2bit", 3))
    )


_WfSerialPortStopBits_Type.__name__ = "Integer32"
_WfSerialPortStopBits_Object = MibTableColumn
wfSerialPortStopBits = _WfSerialPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 11),
    _WfSerialPortStopBits_Type()
)
wfSerialPortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortStopBits.setStatus("mandatory")


class _WfSerialPortModemEnable_Type(Integer32):
    """Custom type wfSerialPortModemEnable based on Integer32"""
    defaultValue = 2

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


_WfSerialPortModemEnable_Type.__name__ = "Integer32"
_WfSerialPortModemEnable_Object = MibTableColumn
wfSerialPortModemEnable = _WfSerialPortModemEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 12),
    _WfSerialPortModemEnable_Type()
)
wfSerialPortModemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortModemEnable.setStatus("mandatory")


class _WfSerialPortLinesPerScreen_Type(Integer32):
    """Custom type wfSerialPortLinesPerScreen based on Integer32"""
    defaultValue = 24


_WfSerialPortLinesPerScreen_Object = MibTableColumn
wfSerialPortLinesPerScreen = _WfSerialPortLinesPerScreen_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 13),
    _WfSerialPortLinesPerScreen_Type()
)
wfSerialPortLinesPerScreen.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortLinesPerScreen.setStatus("mandatory")


class _WfSerialPortMoreEnable_Type(Integer32):
    """Custom type wfSerialPortMoreEnable based on Integer32"""
    defaultValue = 1

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


_WfSerialPortMoreEnable_Type.__name__ = "Integer32"
_WfSerialPortMoreEnable_Object = MibTableColumn
wfSerialPortMoreEnable = _WfSerialPortMoreEnable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 14),
    _WfSerialPortMoreEnable_Type()
)
wfSerialPortMoreEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortMoreEnable.setStatus("mandatory")
_WfSerialPortPrompt_Type = DisplayString
_WfSerialPortPrompt_Object = MibTableColumn
wfSerialPortPrompt = _WfSerialPortPrompt_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 15),
    _WfSerialPortPrompt_Type()
)
wfSerialPortPrompt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortPrompt.setStatus("mandatory")


class _WfSerialPortLoginTimeOut_Type(Integer32):
    """Custom type wfSerialPortLoginTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfSerialPortLoginTimeOut_Type.__name__ = "Integer32"
_WfSerialPortLoginTimeOut_Object = MibTableColumn
wfSerialPortLoginTimeOut = _WfSerialPortLoginTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 16),
    _WfSerialPortLoginTimeOut_Type()
)
wfSerialPortLoginTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortLoginTimeOut.setStatus("mandatory")


class _WfSerialPortPasswordTimeOut_Type(Integer32):
    """Custom type wfSerialPortPasswordTimeOut based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfSerialPortPasswordTimeOut_Type.__name__ = "Integer32"
_WfSerialPortPasswordTimeOut_Object = MibTableColumn
wfSerialPortPasswordTimeOut = _WfSerialPortPasswordTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 17),
    _WfSerialPortPasswordTimeOut_Type()
)
wfSerialPortPasswordTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortPasswordTimeOut.setStatus("mandatory")


class _WfSerialPortCommandTimeOut_Type(Integer32):
    """Custom type wfSerialPortCommandTimeOut based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfSerialPortCommandTimeOut_Type.__name__ = "Integer32"
_WfSerialPortCommandTimeOut_Object = MibTableColumn
wfSerialPortCommandTimeOut = _WfSerialPortCommandTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 18),
    _WfSerialPortCommandTimeOut_Type()
)
wfSerialPortCommandTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortCommandTimeOut.setStatus("mandatory")


class _WfSerialPortLoginRetries_Type(Integer32):
    """Custom type wfSerialPortLoginRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_WfSerialPortLoginRetries_Type.__name__ = "Integer32"
_WfSerialPortLoginRetries_Object = MibTableColumn
wfSerialPortLoginRetries = _WfSerialPortLoginRetries_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 19),
    _WfSerialPortLoginRetries_Type()
)
wfSerialPortLoginRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortLoginRetries.setStatus("mandatory")
_WfSerialPortTotalLogins_Type = Counter32
_WfSerialPortTotalLogins_Object = MibTableColumn
wfSerialPortTotalLogins = _WfSerialPortTotalLogins_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 20),
    _WfSerialPortTotalLogins_Type()
)
wfSerialPortTotalLogins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortTotalLogins.setStatus("mandatory")
_WfSerialPortUserLoginErrors_Type = Counter32
_WfSerialPortUserLoginErrors_Object = MibTableColumn
wfSerialPortUserLoginErrors = _WfSerialPortUserLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 21),
    _WfSerialPortUserLoginErrors_Type()
)
wfSerialPortUserLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortUserLoginErrors.setStatus("mandatory")
_WfSerialPortManagerLoginErrors_Type = Counter32
_WfSerialPortManagerLoginErrors_Object = MibTableColumn
wfSerialPortManagerLoginErrors = _WfSerialPortManagerLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 22),
    _WfSerialPortManagerLoginErrors_Type()
)
wfSerialPortManagerLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortManagerLoginErrors.setStatus("mandatory")
_WfSerialPortOtherLoginErrors_Type = Counter32
_WfSerialPortOtherLoginErrors_Object = MibTableColumn
wfSerialPortOtherLoginErrors = _WfSerialPortOtherLoginErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 23),
    _WfSerialPortOtherLoginErrors_Type()
)
wfSerialPortOtherLoginErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortOtherLoginErrors.setStatus("mandatory")
_WfSerialPortTtyFrameErrors_Type = Counter32
_WfSerialPortTtyFrameErrors_Object = MibTableColumn
wfSerialPortTtyFrameErrors = _WfSerialPortTtyFrameErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 24),
    _WfSerialPortTtyFrameErrors_Type()
)
wfSerialPortTtyFrameErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortTtyFrameErrors.setStatus("mandatory")
_WfSerialPortTtyOverrunErrors_Type = Counter32
_WfSerialPortTtyOverrunErrors_Object = MibTableColumn
wfSerialPortTtyOverrunErrors = _WfSerialPortTtyOverrunErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 25),
    _WfSerialPortTtyOverrunErrors_Type()
)
wfSerialPortTtyOverrunErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortTtyOverrunErrors.setStatus("mandatory")
_WfSerialPortTtyParityErrors_Type = Counter32
_WfSerialPortTtyParityErrors_Object = MibTableColumn
wfSerialPortTtyParityErrors = _WfSerialPortTtyParityErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 26),
    _WfSerialPortTtyParityErrors_Type()
)
wfSerialPortTtyParityErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortTtyParityErrors.setStatus("mandatory")
_WfSerialPortTtyInfifoErrors_Type = Counter32
_WfSerialPortTtyInfifoErrors_Object = MibTableColumn
wfSerialPortTtyInfifoErrors = _WfSerialPortTtyInfifoErrors_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 27),
    _WfSerialPortTtyInfifoErrors_Type()
)
wfSerialPortTtyInfifoErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortTtyInfifoErrors.setStatus("mandatory")
_WfSerialPortInitialSearchPath_Type = DisplayString
_WfSerialPortInitialSearchPath_Object = MibTableColumn
wfSerialPortInitialSearchPath = _WfSerialPortInitialSearchPath_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 28),
    _WfSerialPortInitialSearchPath_Type()
)
wfSerialPortInitialSearchPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortInitialSearchPath.setStatus("obsolete")
_WfSerialPortManagerAutoScript_Type = DisplayString
_WfSerialPortManagerAutoScript_Object = MibTableColumn
wfSerialPortManagerAutoScript = _WfSerialPortManagerAutoScript_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 29),
    _WfSerialPortManagerAutoScript_Type()
)
wfSerialPortManagerAutoScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortManagerAutoScript.setStatus("mandatory")
_WfSerialPortUserAutoScript_Type = DisplayString
_WfSerialPortUserAutoScript_Object = MibTableColumn
wfSerialPortUserAutoScript = _WfSerialPortUserAutoScript_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 30),
    _WfSerialPortUserAutoScript_Type()
)
wfSerialPortUserAutoScript.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortUserAutoScript.setStatus("mandatory")


class _WfSerialPortUserAbortLogoutDisable_Type(Integer32):
    """Custom type wfSerialPortUserAbortLogoutDisable based on Integer32"""
    defaultValue = 2

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


_WfSerialPortUserAbortLogoutDisable_Type.__name__ = "Integer32"
_WfSerialPortUserAbortLogoutDisable_Object = MibTableColumn
wfSerialPortUserAbortLogoutDisable = _WfSerialPortUserAbortLogoutDisable_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 31),
    _WfSerialPortUserAbortLogoutDisable_Type()
)
wfSerialPortUserAbortLogoutDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortUserAbortLogoutDisable.setStatus("mandatory")


class _WfSerialPortHistoryDepth_Type(Integer32):
    """Custom type wfSerialPortHistoryDepth based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_WfSerialPortHistoryDepth_Type.__name__ = "Integer32"
_WfSerialPortHistoryDepth_Object = MibTableColumn
wfSerialPortHistoryDepth = _WfSerialPortHistoryDepth_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 32),
    _WfSerialPortHistoryDepth_Type()
)
wfSerialPortHistoryDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortHistoryDepth.setStatus("mandatory")


class _WfSerialPortAutoSaveNumFiles_Type(Integer32):
    """Custom type wfSerialPortAutoSaveNumFiles based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_WfSerialPortAutoSaveNumFiles_Type.__name__ = "Integer32"
_WfSerialPortAutoSaveNumFiles_Object = MibTableColumn
wfSerialPortAutoSaveNumFiles = _WfSerialPortAutoSaveNumFiles_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 33),
    _WfSerialPortAutoSaveNumFiles_Type()
)
wfSerialPortAutoSaveNumFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortAutoSaveNumFiles.setStatus("mandatory")
_WfSerialPortAutoSaveVolume_Type = DisplayString
_WfSerialPortAutoSaveVolume_Object = MibTableColumn
wfSerialPortAutoSaveVolume = _WfSerialPortAutoSaveVolume_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 34),
    _WfSerialPortAutoSaveVolume_Type()
)
wfSerialPortAutoSaveVolume.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortAutoSaveVolume.setStatus("mandatory")


class _WfSerialPortModemIdSwRev_Type(DisplayString):
    """Custom type wfSerialPortModemIdSwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_WfSerialPortModemIdSwRev_Type.__name__ = "DisplayString"
_WfSerialPortModemIdSwRev_Object = MibTableColumn
wfSerialPortModemIdSwRev = _WfSerialPortModemIdSwRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 35),
    _WfSerialPortModemIdSwRev_Type()
)
wfSerialPortModemIdSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortModemIdSwRev.setStatus("mandatory")


class _WfSerialPortModemIdHwRev_Type(DisplayString):
    """Custom type wfSerialPortModemIdHwRev based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 79),
    )


_WfSerialPortModemIdHwRev_Type.__name__ = "DisplayString"
_WfSerialPortModemIdHwRev_Object = MibTableColumn
wfSerialPortModemIdHwRev = _WfSerialPortModemIdHwRev_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 36),
    _WfSerialPortModemIdHwRev_Type()
)
wfSerialPortModemIdHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortModemIdHwRev.setStatus("mandatory")


class _WfSerialPortModemLineState_Type(Integer32):
    """Custom type wfSerialPortModemLineState based on Integer32"""
    defaultValue = 1

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
        *(("busiedOut", 5),
          ("connected", 4),
          ("offHook", 3),
          ("onHook", 2),
          ("reset", 6),
          ("unknown", 1))
    )


_WfSerialPortModemLineState_Type.__name__ = "Integer32"
_WfSerialPortModemLineState_Object = MibTableColumn
wfSerialPortModemLineState = _WfSerialPortModemLineState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 37),
    _WfSerialPortModemLineState_Type()
)
wfSerialPortModemLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortModemLineState.setStatus("mandatory")


class _WfSerialPortModemCfgFactoryDefaults_Type(Integer32):
    """Custom type wfSerialPortModemCfgFactoryDefaults based on Integer32"""
    defaultValue = 1

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


_WfSerialPortModemCfgFactoryDefaults_Type.__name__ = "Integer32"
_WfSerialPortModemCfgFactoryDefaults_Object = MibTableColumn
wfSerialPortModemCfgFactoryDefaults = _WfSerialPortModemCfgFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 38),
    _WfSerialPortModemCfgFactoryDefaults_Type()
)
wfSerialPortModemCfgFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortModemCfgFactoryDefaults.setStatus("mandatory")
_WfSerialPortModemCfgInitString_Type = DisplayString
_WfSerialPortModemCfgInitString_Object = MibTableColumn
wfSerialPortModemCfgInitString = _WfSerialPortModemCfgInitString_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 39),
    _WfSerialPortModemCfgInitString_Type()
)
wfSerialPortModemCfgInitString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortModemCfgInitString.setStatus("mandatory")
_WfSerialPortModemCfgDefaultString_Type = DisplayString
_WfSerialPortModemCfgDefaultString_Object = MibTableColumn
wfSerialPortModemCfgDefaultString = _WfSerialPortModemCfgDefaultString_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 40),
    _WfSerialPortModemCfgDefaultString_Type()
)
wfSerialPortModemCfgDefaultString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortModemCfgDefaultString.setStatus("mandatory")
_WfSerialPortModemCfgResultCodeString_Type = DisplayString
_WfSerialPortModemCfgResultCodeString_Object = MibTableColumn
wfSerialPortModemCfgResultCodeString = _WfSerialPortModemCfgResultCodeString_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 41),
    _WfSerialPortModemCfgResultCodeString_Type()
)
wfSerialPortModemCfgResultCodeString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortModemCfgResultCodeString.setStatus("mandatory")


class _WfSerialPortModemCfgState_Type(Integer32):
    """Custom type wfSerialPortModemCfgState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cfgIdle", 1),
          ("cfgInProgress", 2),
          ("cfgResponseReturned", 3))
    )


_WfSerialPortModemCfgState_Type.__name__ = "Integer32"
_WfSerialPortModemCfgState_Object = MibTableColumn
wfSerialPortModemCfgState = _WfSerialPortModemCfgState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 42),
    _WfSerialPortModemCfgState_Type()
)
wfSerialPortModemCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortModemCfgState.setStatus("mandatory")


class _WfSerialPortModemCfgCountry_Type(Integer32):
    """Custom type wfSerialPortModemCfgCountry based on Integer32"""
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
        *(("germany", 4),
          ("japan", 2),
          ("northAmerica", 1),
          ("uk", 3))
    )


_WfSerialPortModemCfgCountry_Type.__name__ = "Integer32"
_WfSerialPortModemCfgCountry_Object = MibTableColumn
wfSerialPortModemCfgCountry = _WfSerialPortModemCfgCountry_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 43),
    _WfSerialPortModemCfgCountry_Type()
)
wfSerialPortModemCfgCountry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wfSerialPortModemCfgCountry.setStatus("mandatory")


class _WfSerialPortModemInitState_Type(Integer32):
    """Custom type wfSerialPortModemInitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3,
              4,
              5,
              8)
        )
    )
    namedValues = NamedValues(
        *(("getInfo", 3),
          ("initComplete", 8),
          ("initialization", 5),
          ("setDefaults", 4),
          ("startup", 1))
    )


_WfSerialPortModemInitState_Type.__name__ = "Integer32"
_WfSerialPortModemInitState_Object = MibTableColumn
wfSerialPortModemInitState = _WfSerialPortModemInitState_Object(
    (1, 3, 6, 1, 4, 1, 18, 3, 3, 2, 11, 1, 1, 44),
    _WfSerialPortModemInitState_Type()
)
wfSerialPortModemInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wfSerialPortModemInitState.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Wellfleet-CONSOLE-MIB",
    **{"wfConsole": wfConsole,
       "wfBaudRate": wfBaudRate,
       "wfDataBits": wfDataBits,
       "wfParity": wfParity,
       "wfStopBits": wfStopBits,
       "wfModemEnable": wfModemEnable,
       "wfLinesPerScreen": wfLinesPerScreen,
       "wfMoreEnable": wfMoreEnable,
       "wfPrompt": wfPrompt,
       "wfLoginTimeOut": wfLoginTimeOut,
       "wfPasswordTimeOut": wfPasswordTimeOut,
       "wfCommandTimeOut": wfCommandTimeOut,
       "wfLoginRetries": wfLoginRetries,
       "wfTotalLogins": wfTotalLogins,
       "wfUserLoginErrors": wfUserLoginErrors,
       "wfManagerLoginErrors": wfManagerLoginErrors,
       "wfOtherLoginErrors": wfOtherLoginErrors,
       "wfTtyFrameErrors": wfTtyFrameErrors,
       "wfTtyOverrunErrors": wfTtyOverrunErrors,
       "wfTtyParityErrors": wfTtyParityErrors,
       "wfTtyInfifoErrors": wfTtyInfifoErrors,
       "wfSerialPortTable": wfSerialPortTable,
       "wfSerialPortEntry": wfSerialPortEntry,
       "wfSerialPortDelete": wfSerialPortDelete,
       "wfSerialPortDisable": wfSerialPortDisable,
       "wfSerialPortState": wfSerialPortState,
       "wfSerialPortNumber": wfSerialPortNumber,
       "wfSerialPortName": wfSerialPortName,
       "wfSerialPortSlot": wfSerialPortSlot,
       "wfSerialPortType": wfSerialPortType,
       "wfSerialPortBaudRate": wfSerialPortBaudRate,
       "wfSerialPortDataBits": wfSerialPortDataBits,
       "wfSerialPortParity": wfSerialPortParity,
       "wfSerialPortStopBits": wfSerialPortStopBits,
       "wfSerialPortModemEnable": wfSerialPortModemEnable,
       "wfSerialPortLinesPerScreen": wfSerialPortLinesPerScreen,
       "wfSerialPortMoreEnable": wfSerialPortMoreEnable,
       "wfSerialPortPrompt": wfSerialPortPrompt,
       "wfSerialPortLoginTimeOut": wfSerialPortLoginTimeOut,
       "wfSerialPortPasswordTimeOut": wfSerialPortPasswordTimeOut,
       "wfSerialPortCommandTimeOut": wfSerialPortCommandTimeOut,
       "wfSerialPortLoginRetries": wfSerialPortLoginRetries,
       "wfSerialPortTotalLogins": wfSerialPortTotalLogins,
       "wfSerialPortUserLoginErrors": wfSerialPortUserLoginErrors,
       "wfSerialPortManagerLoginErrors": wfSerialPortManagerLoginErrors,
       "wfSerialPortOtherLoginErrors": wfSerialPortOtherLoginErrors,
       "wfSerialPortTtyFrameErrors": wfSerialPortTtyFrameErrors,
       "wfSerialPortTtyOverrunErrors": wfSerialPortTtyOverrunErrors,
       "wfSerialPortTtyParityErrors": wfSerialPortTtyParityErrors,
       "wfSerialPortTtyInfifoErrors": wfSerialPortTtyInfifoErrors,
       "wfSerialPortInitialSearchPath": wfSerialPortInitialSearchPath,
       "wfSerialPortManagerAutoScript": wfSerialPortManagerAutoScript,
       "wfSerialPortUserAutoScript": wfSerialPortUserAutoScript,
       "wfSerialPortUserAbortLogoutDisable": wfSerialPortUserAbortLogoutDisable,
       "wfSerialPortHistoryDepth": wfSerialPortHistoryDepth,
       "wfSerialPortAutoSaveNumFiles": wfSerialPortAutoSaveNumFiles,
       "wfSerialPortAutoSaveVolume": wfSerialPortAutoSaveVolume,
       "wfSerialPortModemIdSwRev": wfSerialPortModemIdSwRev,
       "wfSerialPortModemIdHwRev": wfSerialPortModemIdHwRev,
       "wfSerialPortModemLineState": wfSerialPortModemLineState,
       "wfSerialPortModemCfgFactoryDefaults": wfSerialPortModemCfgFactoryDefaults,
       "wfSerialPortModemCfgInitString": wfSerialPortModemCfgInitString,
       "wfSerialPortModemCfgDefaultString": wfSerialPortModemCfgDefaultString,
       "wfSerialPortModemCfgResultCodeString": wfSerialPortModemCfgResultCodeString,
       "wfSerialPortModemCfgState": wfSerialPortModemCfgState,
       "wfSerialPortModemCfgCountry": wfSerialPortModemCfgCountry,
       "wfSerialPortModemInitState": wfSerialPortModemInitState}
)
