# SNMP MIB module (COM21-HCXTX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/COM21-HCXTX-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:16:39 2024
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

(com21,
 com21Hcx,
 com21Traps) = mibBuilder.importSymbols(
    "COM21-HCX-MIB",
    "com21",
    "com21Hcx",
    "com21Traps")

(hcxAlmSeverity,
 hcxEventLogTime) = mibBuilder.importSymbols(
    "COM21-HCXALM-MIB",
    "hcxAlmSeverity",
    "hcxEventLogTime")

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
 MacAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "TextualConvention")


# MODULE-IDENTITY

com21HcxTx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 20)
)


# Types definitions



class Gain(Integer32):
    """Custom type Gain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class PrimServiceState(Integer32):
    """Custom type PrimServiceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("is", 1),
          ("oos", 2))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Com21HcxDnstrmPortGroup_ObjectIdentity = ObjectIdentity
com21HcxDnstrmPortGroup = _Com21HcxDnstrmPortGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 21)
)
_HcxDownstreamPortId_Type = Integer32
_HcxDownstreamPortId_Object = MibScalar
hcxDownstreamPortId = _HcxDownstreamPortId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 21, 1),
    _HcxDownstreamPortId_Type()
)
hcxDownstreamPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDownstreamPortId.setStatus("current")


class _HcxXmitFrequency_Type(Integer32):
    """Custom type hcxXmitFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(88000, 800000),
    )


_HcxXmitFrequency_Type.__name__ = "Integer32"
_HcxXmitFrequency_Object = MibScalar
hcxXmitFrequency = _HcxXmitFrequency_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 21, 2),
    _HcxXmitFrequency_Type()
)
hcxXmitFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxXmitFrequency.setStatus("current")


class _HcxXmitGain_Type(Integer32):
    """Custom type hcxXmitGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(45, 60),
    )


_HcxXmitGain_Type.__name__ = "Integer32"
_HcxXmitGain_Object = MibScalar
hcxXmitGain = _HcxXmitGain_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 21, 3),
    _HcxXmitGain_Type()
)
hcxXmitGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxXmitGain.setStatus("current")
_Com21HcxDnstrmStatsGroup_ObjectIdentity = ObjectIdentity
com21HcxDnstrmStatsGroup = _Com21HcxDnstrmStatsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 22)
)
_HcxStatsCurrMinTxCells_Type = Gauge32
_HcxStatsCurrMinTxCells_Object = MibScalar
hcxStatsCurrMinTxCells = _HcxStatsCurrMinTxCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 22, 1),
    _HcxStatsCurrMinTxCells_Type()
)
hcxStatsCurrMinTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsCurrMinTxCells.setStatus("current")
_HcxStatsCurrMinTxNullCells_Type = Gauge32
_HcxStatsCurrMinTxNullCells_Object = MibScalar
hcxStatsCurrMinTxNullCells = _HcxStatsCurrMinTxNullCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 22, 2),
    _HcxStatsCurrMinTxNullCells_Type()
)
hcxStatsCurrMinTxNullCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsCurrMinTxNullCells.setStatus("current")
_HcxStatsPrevMinTxCells_Type = Gauge32
_HcxStatsPrevMinTxCells_Object = MibScalar
hcxStatsPrevMinTxCells = _HcxStatsPrevMinTxCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 22, 3),
    _HcxStatsPrevMinTxCells_Type()
)
hcxStatsPrevMinTxCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsPrevMinTxCells.setStatus("current")
_HcxStatsPrevMinTxNullCells_Type = Gauge32
_HcxStatsPrevMinTxNullCells_Object = MibScalar
hcxStatsPrevMinTxNullCells = _HcxStatsPrevMinTxNullCells_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 22, 4),
    _HcxStatsPrevMinTxNullCells_Type()
)
hcxStatsPrevMinTxNullCells.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxStatsPrevMinTxNullCells.setStatus("current")
_HcxDownstreamUtil_Type = Gauge32
_HcxDownstreamUtil_Object = MibScalar
hcxDownstreamUtil = _HcxDownstreamUtil_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 22, 5),
    _HcxDownstreamUtil_Type()
)
hcxDownstreamUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDownstreamUtil.setStatus("current")


class _HcxStatsClearTxCurrStats_Type(Integer32):
    """Custom type hcxStatsClearTxCurrStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 2),
          ("nil", 1))
    )


_HcxStatsClearTxCurrStats_Type.__name__ = "Integer32"
_HcxStatsClearTxCurrStats_Object = MibScalar
hcxStatsClearTxCurrStats = _HcxStatsClearTxCurrStats_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 22, 6),
    _HcxStatsClearTxCurrStats_Type()
)
hcxStatsClearTxCurrStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxStatsClearTxCurrStats.setStatus("current")
_Com21HcxDnstrmUnitGroup_ObjectIdentity = ObjectIdentity
com21HcxDnstrmUnitGroup = _Com21HcxDnstrmUnitGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23)
)


class _HcxDownstreamShelfId_Type(Integer32):
    """Custom type hcxDownstreamShelfId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_HcxDownstreamShelfId_Type.__name__ = "Integer32"
_HcxDownstreamShelfId_Object = MibScalar
hcxDownstreamShelfId = _HcxDownstreamShelfId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 1),
    _HcxDownstreamShelfId_Type()
)
hcxDownstreamShelfId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDownstreamShelfId.setStatus("current")
_HcxDownstreamSlotId_Type = Integer32
_HcxDownstreamSlotId_Object = MibScalar
hcxDownstreamSlotId = _HcxDownstreamSlotId_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 2),
    _HcxDownstreamSlotId_Type()
)
hcxDownstreamSlotId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDownstreamSlotId.setStatus("current")


class _HcxDownstreamHardwareVersion_Type(DisplayString):
    """Custom type hcxDownstreamHardwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxDownstreamHardwareVersion_Type.__name__ = "DisplayString"
_HcxDownstreamHardwareVersion_Object = MibScalar
hcxDownstreamHardwareVersion = _HcxDownstreamHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 3),
    _HcxDownstreamHardwareVersion_Type()
)
hcxDownstreamHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDownstreamHardwareVersion.setStatus("current")


class _HcxDownstreamBootVersion_Type(DisplayString):
    """Custom type hcxDownstreamBootVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxDownstreamBootVersion_Type.__name__ = "DisplayString"
_HcxDownstreamBootVersion_Object = MibScalar
hcxDownstreamBootVersion = _HcxDownstreamBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 4),
    _HcxDownstreamBootVersion_Type()
)
hcxDownstreamBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDownstreamBootVersion.setStatus("current")
_HcxDnstreamUnitPrimServState_Type = PrimServiceState
_HcxDnstreamUnitPrimServState_Object = MibScalar
hcxDnstreamUnitPrimServState = _HcxDnstreamUnitPrimServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 5),
    _HcxDnstreamUnitPrimServState_Type()
)
hcxDnstreamUnitPrimServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDnstreamUnitPrimServState.setStatus("current")


class _HcxDnstreamUnitSecServState_Type(DisplayString):
    """Custom type hcxDnstreamUnitSecServState based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxDnstreamUnitSecServState_Type.__name__ = "DisplayString"
_HcxDnstreamUnitSecServState_Object = MibScalar
hcxDnstreamUnitSecServState = _HcxDnstreamUnitSecServState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 6),
    _HcxDnstreamUnitSecServState_Type()
)
hcxDnstreamUnitSecServState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDnstreamUnitSecServState.setStatus("current")


class _HcxDnUnitConfigState_Type(Integer32):
    """Custom type hcxDnUnitConfigState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2000,
              2001,
              2002,
              2003)
        )
    )
    namedValues = NamedValues(
        *(("offline", 2000),
          ("online", 2001),
          ("standby", 2003),
          ("test", 2002))
    )


_HcxDnUnitConfigState_Type.__name__ = "Integer32"
_HcxDnUnitConfigState_Object = MibScalar
hcxDnUnitConfigState = _HcxDnUnitConfigState_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 7),
    _HcxDnUnitConfigState_Type()
)
hcxDnUnitConfigState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDnUnitConfigState.setStatus("current")


class _HcxDnUnitRestartAction_Type(Integer32):
    """Custom type hcxDnUnitRestartAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nil", 1),
          ("restart", 2))
    )


_HcxDnUnitRestartAction_Type.__name__ = "Integer32"
_HcxDnUnitRestartAction_Object = MibScalar
hcxDnUnitRestartAction = _HcxDnUnitRestartAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 8),
    _HcxDnUnitRestartAction_Type()
)
hcxDnUnitRestartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDnUnitRestartAction.setStatus("current")


class _HcxDnDiagTestAction_Type(Integer32):
    """Custom type hcxDnDiagTestAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("execute", 2),
          ("nil", 1))
    )


_HcxDnDiagTestAction_Type.__name__ = "Integer32"
_HcxDnDiagTestAction_Object = MibScalar
hcxDnDiagTestAction = _HcxDnDiagTestAction_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 9),
    _HcxDnDiagTestAction_Type()
)
hcxDnDiagTestAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hcxDnDiagTestAction.setStatus("current")


class _HcxDnDiagTestResult_Type(Integer32):
    """Custom type hcxDnDiagTestResult based on Integer32"""
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
        *(("failure", 3),
          ("inprogress", 1),
          ("invalidState", 4),
          ("success", 2))
    )


_HcxDnDiagTestResult_Type.__name__ = "Integer32"
_HcxDnDiagTestResult_Object = MibScalar
hcxDnDiagTestResult = _HcxDnDiagTestResult_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 10),
    _HcxDnDiagTestResult_Type()
)
hcxDnDiagTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDnDiagTestResult.setStatus("current")


class _HcxDnTestStatusLed_Type(Integer32):
    """Custom type hcxDnTestStatusLed based on Integer32"""
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


_HcxDnTestStatusLed_Type.__name__ = "Integer32"
_HcxDnTestStatusLed_Object = MibScalar
hcxDnTestStatusLed = _HcxDnTestStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 11),
    _HcxDnTestStatusLed_Type()
)
hcxDnTestStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDnTestStatusLed.setStatus("current")


class _HcxDnFaultStatusLed_Type(Integer32):
    """Custom type hcxDnFaultStatusLed based on Integer32"""
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


_HcxDnFaultStatusLed_Type.__name__ = "Integer32"
_HcxDnFaultStatusLed_Object = MibScalar
hcxDnFaultStatusLed = _HcxDnFaultStatusLed_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 12),
    _HcxDnFaultStatusLed_Type()
)
hcxDnFaultStatusLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDnFaultStatusLed.setStatus("current")


class _HcxDownstreamSerialNumber_Type(DisplayString):
    """Custom type hcxDownstreamSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )


_HcxDownstreamSerialNumber_Type.__name__ = "DisplayString"
_HcxDownstreamSerialNumber_Object = MibScalar
hcxDownstreamSerialNumber = _HcxDownstreamSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 1141, 2, 23, 13),
    _HcxDownstreamSerialNumber_Type()
)
hcxDownstreamSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hcxDownstreamSerialNumber.setStatus("current")

# Managed Objects groups


# Notification objects

hcxDnstrmUnitPrimStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 60)
)
hcxDnstrmUnitPrimStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTX-MIB", "hcxDownstreamShelfId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamSlotId"),
        ("COM21-HCXTX-MIB", "hcxDnstreamUnitPrimServState"))
)
if mibBuilder.loadTexts:
    hcxDnstrmUnitPrimStateChange.setStatus(
        "current"
    )

hcxDnstrmUnitSecStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 61)
)
hcxDnstrmUnitSecStateChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTX-MIB", "hcxDownstreamShelfId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamSlotId"),
        ("COM21-HCXTX-MIB", "hcxDnstreamUnitSecServState"))
)
if mibBuilder.loadTexts:
    hcxDnstrmUnitSecStateChange.setStatus(
        "current"
    )

hcxDnDiagTestComplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 62)
)
hcxDnDiagTestComplete.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTX-MIB", "hcxDownstreamShelfId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamSlotId"),
        ("COM21-HCXTX-MIB", "hcxDnDiagTestResult"))
)
if mibBuilder.loadTexts:
    hcxDnDiagTestComplete.setStatus(
        "current"
    )

hcxDnTestStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 63)
)
hcxDnTestStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTX-MIB", "hcxDownstreamShelfId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamSlotId"),
        ("COM21-HCXTX-MIB", "hcxDnTestStatusLed"))
)
if mibBuilder.loadTexts:
    hcxDnTestStatusLedChange.setStatus(
        "current"
    )

hcxDnFaultStatusLedChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 64)
)
hcxDnFaultStatusLedChange.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTX-MIB", "hcxDownstreamShelfId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamSlotId"),
        ("COM21-HCXTX-MIB", "hcxDnFaultStatusLed"))
)
if mibBuilder.loadTexts:
    hcxDnFaultStatusLedChange.setStatus(
        "current"
    )

hcxDnOperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 65)
)
hcxDnOperationFailure.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTX-MIB", "hcxDownstreamShelfId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamSlotId"))
)
if mibBuilder.loadTexts:
    hcxDnOperationFailure.setStatus(
        "current"
    )

hcxSynthLockLossDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 68)
)
hcxSynthLockLossDetected.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTX-MIB", "hcxDownstreamShelfId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamSlotId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamPortId"))
)
if mibBuilder.loadTexts:
    hcxSynthLockLossDetected.setStatus(
        "current"
    )

hcxSynthLockLossClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 69)
)
hcxSynthLockLossClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTX-MIB", "hcxDownstreamShelfId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamSlotId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamPortId"))
)
if mibBuilder.loadTexts:
    hcxSynthLockLossClear.setStatus(
        "current"
    )

hcxLossOfFrameClkDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 70)
)
hcxLossOfFrameClkDetected.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTX-MIB", "hcxDownstreamShelfId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamSlotId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamPortId"))
)
if mibBuilder.loadTexts:
    hcxLossOfFrameClkDetected.setStatus(
        "current"
    )

hcxLossOfFrameClkClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 1141, 4, 71)
)
hcxLossOfFrameClkClear.setObjects(
      *(("COM21-HCXALM-MIB", "hcxAlmSeverity"),
        ("COM21-HCXALM-MIB", "hcxEventLogTime"),
        ("COM21-HCXTX-MIB", "hcxDownstreamShelfId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamSlotId"),
        ("COM21-HCXTX-MIB", "hcxDownstreamPortId"))
)
if mibBuilder.loadTexts:
    hcxLossOfFrameClkClear.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "COM21-HCXTX-MIB",
    **{"Gain": Gain,
       "PrimServiceState": PrimServiceState,
       "com21HcxTx": com21HcxTx,
       "com21HcxDnstrmPortGroup": com21HcxDnstrmPortGroup,
       "hcxDownstreamPortId": hcxDownstreamPortId,
       "hcxXmitFrequency": hcxXmitFrequency,
       "hcxXmitGain": hcxXmitGain,
       "com21HcxDnstrmStatsGroup": com21HcxDnstrmStatsGroup,
       "hcxStatsCurrMinTxCells": hcxStatsCurrMinTxCells,
       "hcxStatsCurrMinTxNullCells": hcxStatsCurrMinTxNullCells,
       "hcxStatsPrevMinTxCells": hcxStatsPrevMinTxCells,
       "hcxStatsPrevMinTxNullCells": hcxStatsPrevMinTxNullCells,
       "hcxDownstreamUtil": hcxDownstreamUtil,
       "hcxStatsClearTxCurrStats": hcxStatsClearTxCurrStats,
       "com21HcxDnstrmUnitGroup": com21HcxDnstrmUnitGroup,
       "hcxDownstreamShelfId": hcxDownstreamShelfId,
       "hcxDownstreamSlotId": hcxDownstreamSlotId,
       "hcxDownstreamHardwareVersion": hcxDownstreamHardwareVersion,
       "hcxDownstreamBootVersion": hcxDownstreamBootVersion,
       "hcxDnstreamUnitPrimServState": hcxDnstreamUnitPrimServState,
       "hcxDnstreamUnitSecServState": hcxDnstreamUnitSecServState,
       "hcxDnUnitConfigState": hcxDnUnitConfigState,
       "hcxDnUnitRestartAction": hcxDnUnitRestartAction,
       "hcxDnDiagTestAction": hcxDnDiagTestAction,
       "hcxDnDiagTestResult": hcxDnDiagTestResult,
       "hcxDnTestStatusLed": hcxDnTestStatusLed,
       "hcxDnFaultStatusLed": hcxDnFaultStatusLed,
       "hcxDownstreamSerialNumber": hcxDownstreamSerialNumber,
       "hcxDnstrmUnitPrimStateChange": hcxDnstrmUnitPrimStateChange,
       "hcxDnstrmUnitSecStateChange": hcxDnstrmUnitSecStateChange,
       "hcxDnDiagTestComplete": hcxDnDiagTestComplete,
       "hcxDnTestStatusLedChange": hcxDnTestStatusLedChange,
       "hcxDnFaultStatusLedChange": hcxDnFaultStatusLedChange,
       "hcxDnOperationFailure": hcxDnOperationFailure,
       "hcxSynthLockLossDetected": hcxSynthLockLossDetected,
       "hcxSynthLockLossClear": hcxSynthLockLossClear,
       "hcxLossOfFrameClkDetected": hcxLossOfFrameClkDetected,
       "hcxLossOfFrameClkClear": hcxLossOfFrameClkClear}
)
