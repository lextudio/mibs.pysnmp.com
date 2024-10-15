# SNMP MIB module (CXAsyncIo-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/CXAsyncIo-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 21:20:04 2024
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

(Alias,
 cxAsyncIo) = mibBuilder.importSymbols(
    "CXProduct-SMI",
    "Alias",
    "cxAsyncIo")

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
 NotificationType,
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
    "NotificationType",
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


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsioSapOprTable_Object = MibTable
asioSapOprTable = _AsioSapOprTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1)
)
if mibBuilder.loadTexts:
    asioSapOprTable.setStatus("mandatory")
_AsioSapOprEntry_Object = MibTableRow
asioSapOprEntry = _AsioSapOprEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1)
)
asioSapOprEntry.setIndexNames(
    (0, "CXAsyncIo-MIB", "asioSapOprNumber"),
)
if mibBuilder.loadTexts:
    asioSapOprEntry.setStatus("mandatory")
_AsioSapOprNumber_Type = Integer32
_AsioSapOprNumber_Object = MibTableColumn
asioSapOprNumber = _AsioSapOprNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 1),
    _AsioSapOprNumber_Type()
)
asioSapOprNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioSapOprNumber.setStatus("mandatory")
_AsioSapOprAlias_Type = Alias
_AsioSapOprAlias_Object = MibTableColumn
asioSapOprAlias = _AsioSapOprAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 2),
    _AsioSapOprAlias_Type()
)
asioSapOprAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioSapOprAlias.setStatus("mandatory")


class _AsioSapOprPortSpeed_Type(Integer32):
    """Custom type asioSapOprPortSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 115200),
    )


_AsioSapOprPortSpeed_Type.__name__ = "Integer32"
_AsioSapOprPortSpeed_Object = MibTableColumn
asioSapOprPortSpeed = _AsioSapOprPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 3),
    _AsioSapOprPortSpeed_Type()
)
asioSapOprPortSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioSapOprPortSpeed.setStatus("mandatory")


class _AsioSapOprPortCharacterSize_Type(Integer32):
    """Custom type asioSapOprPortCharacterSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_AsioSapOprPortCharacterSize_Type.__name__ = "Integer32"
_AsioSapOprPortCharacterSize_Object = MibTableColumn
asioSapOprPortCharacterSize = _AsioSapOprPortCharacterSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 5),
    _AsioSapOprPortCharacterSize_Type()
)
asioSapOprPortCharacterSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioSapOprPortCharacterSize.setStatus("mandatory")


class _AsioSapOprPortStopBits_Type(Integer32):
    """Custom type asioSapOprPortStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("one", 1),
          ("one-point-five", 2),
          ("two", 3))
    )


_AsioSapOprPortStopBits_Type.__name__ = "Integer32"
_AsioSapOprPortStopBits_Object = MibTableColumn
asioSapOprPortStopBits = _AsioSapOprPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 6),
    _AsioSapOprPortStopBits_Type()
)
asioSapOprPortStopBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioSapOprPortStopBits.setStatus("mandatory")


class _AsioSapOprPortBreakLength_Type(Integer32):
    """Custom type asioSapOprPortBreakLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AsioSapOprPortBreakLength_Type.__name__ = "Integer32"
_AsioSapOprPortBreakLength_Object = MibTableColumn
asioSapOprPortBreakLength = _AsioSapOprPortBreakLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 7),
    _AsioSapOprPortBreakLength_Type()
)
asioSapOprPortBreakLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioSapOprPortBreakLength.setStatus("mandatory")


class _AsioSapOprPortMaxQueueLength_Type(Integer32):
    """Custom type asioSapOprPortMaxQueueLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AsioSapOprPortMaxQueueLength_Type.__name__ = "Integer32"
_AsioSapOprPortMaxQueueLength_Object = MibTableColumn
asioSapOprPortMaxQueueLength = _AsioSapOprPortMaxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 8),
    _AsioSapOprPortMaxQueueLength_Type()
)
asioSapOprPortMaxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortMaxQueueLength.setStatus("mandatory")


class _AsioSapOprPortQueueUpperThreshold_Type(Integer32):
    """Custom type asioSapOprPortQueueUpperThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AsioSapOprPortQueueUpperThreshold_Type.__name__ = "Integer32"
_AsioSapOprPortQueueUpperThreshold_Object = MibTableColumn
asioSapOprPortQueueUpperThreshold = _AsioSapOprPortQueueUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 9),
    _AsioSapOprPortQueueUpperThreshold_Type()
)
asioSapOprPortQueueUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortQueueUpperThreshold.setStatus("mandatory")


class _AsioSapOprPortQueueLowerThreshold_Type(Integer32):
    """Custom type asioSapOprPortQueueLowerThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AsioSapOprPortQueueLowerThreshold_Type.__name__ = "Integer32"
_AsioSapOprPortQueueLowerThreshold_Object = MibTableColumn
asioSapOprPortQueueLowerThreshold = _AsioSapOprPortQueueLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 10),
    _AsioSapOprPortQueueLowerThreshold_Type()
)
asioSapOprPortQueueLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortQueueLowerThreshold.setStatus("mandatory")


class _AsioSapOprPortSignalDownTimer_Type(Integer32):
    """Custom type asioSapOprPortSignalDownTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsioSapOprPortSignalDownTimer_Type.__name__ = "Integer32"
_AsioSapOprPortSignalDownTimer_Object = MibTableColumn
asioSapOprPortSignalDownTimer = _AsioSapOprPortSignalDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 11),
    _AsioSapOprPortSignalDownTimer_Type()
)
asioSapOprPortSignalDownTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioSapOprPortSignalDownTimer.setStatus("mandatory")


class _AsioSapOprPortMaxTimeDelay_Type(Integer32):
    """Custom type asioSapOprPortMaxTimeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AsioSapOprPortMaxTimeDelay_Type.__name__ = "Integer32"
_AsioSapOprPortMaxTimeDelay_Object = MibTableColumn
asioSapOprPortMaxTimeDelay = _AsioSapOprPortMaxTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 12),
    _AsioSapOprPortMaxTimeDelay_Type()
)
asioSapOprPortMaxTimeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioSapOprPortMaxTimeDelay.setStatus("mandatory")


class _AsioSapOprPortMaxInterruptCharacters_Type(Integer32):
    """Custom type asioSapOprPortMaxInterruptCharacters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_AsioSapOprPortMaxInterruptCharacters_Type.__name__ = "Integer32"
_AsioSapOprPortMaxInterruptCharacters_Object = MibTableColumn
asioSapOprPortMaxInterruptCharacters = _AsioSapOprPortMaxInterruptCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 13),
    _AsioSapOprPortMaxInterruptCharacters_Type()
)
asioSapOprPortMaxInterruptCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortMaxInterruptCharacters.setStatus("obsolete")


class _AsioSapOprPortSignalSamplingPeriod_Type(Integer32):
    """Custom type asioSapOprPortSignalSamplingPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_AsioSapOprPortSignalSamplingPeriod_Type.__name__ = "Integer32"
_AsioSapOprPortSignalSamplingPeriod_Object = MibTableColumn
asioSapOprPortSignalSamplingPeriod = _AsioSapOprPortSignalSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 20),
    _AsioSapOprPortSignalSamplingPeriod_Type()
)
asioSapOprPortSignalSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortSignalSamplingPeriod.setStatus("mandatory")


class _AsioSapOprPortDcdDtrSignalSamples_Type(Integer32):
    """Custom type asioSapOprPortDcdDtrSignalSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsioSapOprPortDcdDtrSignalSamples_Type.__name__ = "Integer32"
_AsioSapOprPortDcdDtrSignalSamples_Object = MibTableColumn
asioSapOprPortDcdDtrSignalSamples = _AsioSapOprPortDcdDtrSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 21),
    _AsioSapOprPortDcdDtrSignalSamples_Type()
)
asioSapOprPortDcdDtrSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortDcdDtrSignalSamples.setStatus("mandatory")


class _AsioSapOprPortCtsRtsSignalSamples_Type(Integer32):
    """Custom type asioSapOprPortCtsRtsSignalSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsioSapOprPortCtsRtsSignalSamples_Type.__name__ = "Integer32"
_AsioSapOprPortCtsRtsSignalSamples_Object = MibTableColumn
asioSapOprPortCtsRtsSignalSamples = _AsioSapOprPortCtsRtsSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 22),
    _AsioSapOprPortCtsRtsSignalSamples_Type()
)
asioSapOprPortCtsRtsSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortCtsRtsSignalSamples.setStatus("mandatory")


class _AsioSapOprPortDsrDrsSignalSamples_Type(Integer32):
    """Custom type asioSapOprPortDsrDrsSignalSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsioSapOprPortDsrDrsSignalSamples_Type.__name__ = "Integer32"
_AsioSapOprPortDsrDrsSignalSamples_Object = MibTableColumn
asioSapOprPortDsrDrsSignalSamples = _AsioSapOprPortDsrDrsSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 23),
    _AsioSapOprPortDsrDrsSignalSamples_Type()
)
asioSapOprPortDsrDrsSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortDsrDrsSignalSamples.setStatus("mandatory")


class _AsioSapOprPortTmLlSignalSamples_Type(Integer32):
    """Custom type asioSapOprPortTmLlSignalSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsioSapOprPortTmLlSignalSamples_Type.__name__ = "Integer32"
_AsioSapOprPortTmLlSignalSamples_Object = MibTableColumn
asioSapOprPortTmLlSignalSamples = _AsioSapOprPortTmLlSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 24),
    _AsioSapOprPortTmLlSignalSamples_Type()
)
asioSapOprPortTmLlSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortTmLlSignalSamples.setStatus("mandatory")


class _AsioSapOprPortRiRlSignalSamples_Type(Integer32):
    """Custom type asioSapOprPortRiRlSignalSamples based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsioSapOprPortRiRlSignalSamples_Type.__name__ = "Integer32"
_AsioSapOprPortRiRlSignalSamples_Object = MibTableColumn
asioSapOprPortRiRlSignalSamples = _AsioSapOprPortRiRlSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 25),
    _AsioSapOprPortRiRlSignalSamples_Type()
)
asioSapOprPortRiRlSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortRiRlSignalSamples.setStatus("mandatory")


class _AsioSapOprPortStatisticsTimer_Type(Integer32):
    """Custom type asioSapOprPortStatisticsTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AsioSapOprPortStatisticsTimer_Type.__name__ = "Integer32"
_AsioSapOprPortStatisticsTimer_Object = MibTableColumn
asioSapOprPortStatisticsTimer = _AsioSapOprPortStatisticsTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 26),
    _AsioSapOprPortStatisticsTimer_Type()
)
asioSapOprPortStatisticsTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioSapOprPortStatisticsTimer.setStatus("mandatory")


class _AsioSapOprPortCarrierAction_Type(Integer32):
    """Custom type asioSapOprPortCarrierAction based on Integer32"""
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


_AsioSapOprPortCarrierAction_Type.__name__ = "Integer32"
_AsioSapOprPortCarrierAction_Object = MibTableColumn
asioSapOprPortCarrierAction = _AsioSapOprPortCarrierAction_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 27),
    _AsioSapOprPortCarrierAction_Type()
)
asioSapOprPortCarrierAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapOprPortCarrierAction.setStatus("mandatory")


class _AsioOprPortTrap_Type(Integer32):
    """Custom type asioOprPortTrap based on Integer32"""
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


_AsioOprPortTrap_Type.__name__ = "Integer32"
_AsioOprPortTrap_Object = MibTableColumn
asioOprPortTrap = _AsioOprPortTrap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 30),
    _AsioOprPortTrap_Type()
)
asioOprPortTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioOprPortTrap.setStatus("mandatory")


class _AsioOprControlLine_Type(Integer32):
    """Custom type asioOprControlLine based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forceDown", 1),
          ("forceReset", 3),
          ("forceUp", 2))
    )


_AsioOprControlLine_Type.__name__ = "Integer32"
_AsioOprControlLine_Object = MibTableColumn
asioOprControlLine = _AsioOprControlLine_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 34),
    _AsioOprControlLine_Type()
)
asioOprControlLine.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    asioOprControlLine.setStatus("mandatory")


class _AsioOprControlStats_Type(Integer32):
    """Custom type asioOprControlStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearSapStats", 1)
    )


_AsioOprControlStats_Type.__name__ = "Integer32"
_AsioOprControlStats_Object = MibTableColumn
asioOprControlStats = _AsioOprControlStats_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 35),
    _AsioOprControlStats_Type()
)
asioOprControlStats.setMaxAccess("write-only")
if mibBuilder.loadTexts:
    asioOprControlStats.setStatus("mandatory")


class _AsioStatOprPortType_Type(Integer32):
    """Custom type asioStatOprPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dce", 3),
          ("dte", 2),
          ("unknown", 1))
    )


_AsioStatOprPortType_Type.__name__ = "Integer32"
_AsioStatOprPortType_Object = MibTableColumn
asioStatOprPortType = _AsioStatOprPortType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 38),
    _AsioStatOprPortType_Type()
)
asioStatOprPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprPortType.setStatus("mandatory")


class _AsioStatOprPortInterfaceType_Type(Integer32):
    """Custom type asioStatOprPortInterfaceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rs232d", 2),
          ("unknown", 1))
    )


_AsioStatOprPortInterfaceType_Type.__name__ = "Integer32"
_AsioStatOprPortInterfaceType_Object = MibTableColumn
asioStatOprPortInterfaceType = _AsioStatOprPortInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 39),
    _AsioStatOprPortInterfaceType_Type()
)
asioStatOprPortInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprPortInterfaceType.setStatus("mandatory")


class _AsioStatOprPortState_Type(Integer32):
    """Custom type asioStatOprPortState based on Integer32"""
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
        *(("portDown", 2),
          ("portDownBadConfiguration", 4),
          ("portOutOfOrder", 5),
          ("portShutDown", 3),
          ("portUp", 1))
    )


_AsioStatOprPortState_Type.__name__ = "Integer32"
_AsioStatOprPortState_Object = MibTableColumn
asioStatOprPortState = _AsioStatOprPortState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 40),
    _AsioStatOprPortState_Type()
)
asioStatOprPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprPortState.setStatus("mandatory")


class _AsioStatOprDCDState_Type(Integer32):
    """Custom type asioStatOprDCDState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_AsioStatOprDCDState_Type.__name__ = "Integer32"
_AsioStatOprDCDState_Object = MibTableColumn
asioStatOprDCDState = _AsioStatOprDCDState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 45),
    _AsioStatOprDCDState_Type()
)
asioStatOprDCDState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprDCDState.setStatus("mandatory")


class _AsioStatOprDTRState_Type(Integer32):
    """Custom type asioStatOprDTRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_AsioStatOprDTRState_Type.__name__ = "Integer32"
_AsioStatOprDTRState_Object = MibTableColumn
asioStatOprDTRState = _AsioStatOprDTRState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 46),
    _AsioStatOprDTRState_Type()
)
asioStatOprDTRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprDTRState.setStatus("mandatory")


class _AsioStatOprRTSState_Type(Integer32):
    """Custom type asioStatOprRTSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_AsioStatOprRTSState_Type.__name__ = "Integer32"
_AsioStatOprRTSState_Object = MibTableColumn
asioStatOprRTSState = _AsioStatOprRTSState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 47),
    _AsioStatOprRTSState_Type()
)
asioStatOprRTSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRTSState.setStatus("mandatory")


class _AsioStatOprCTSState_Type(Integer32):
    """Custom type asioStatOprCTSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_AsioStatOprCTSState_Type.__name__ = "Integer32"
_AsioStatOprCTSState_Object = MibTableColumn
asioStatOprCTSState = _AsioStatOprCTSState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 48),
    _AsioStatOprCTSState_Type()
)
asioStatOprCTSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprCTSState.setStatus("mandatory")


class _AsioStatOprDSRState_Type(Integer32):
    """Custom type asioStatOprDSRState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_AsioStatOprDSRState_Type.__name__ = "Integer32"
_AsioStatOprDSRState_Object = MibTableColumn
asioStatOprDSRState = _AsioStatOprDSRState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 49),
    _AsioStatOprDSRState_Type()
)
asioStatOprDSRState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprDSRState.setStatus("mandatory")


class _AsioStatOprDRSState_Type(Integer32):
    """Custom type asioStatOprDRSState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_AsioStatOprDRSState_Type.__name__ = "Integer32"
_AsioStatOprDRSState_Object = MibTableColumn
asioStatOprDRSState = _AsioStatOprDRSState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 50),
    _AsioStatOprDRSState_Type()
)
asioStatOprDRSState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprDRSState.setStatus("mandatory")


class _AsioStatOprTMState_Type(Integer32):
    """Custom type asioStatOprTMState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_AsioStatOprTMState_Type.__name__ = "Integer32"
_AsioStatOprTMState_Object = MibTableColumn
asioStatOprTMState = _AsioStatOprTMState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 51),
    _AsioStatOprTMState_Type()
)
asioStatOprTMState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprTMState.setStatus("mandatory")


class _AsioStatOprLLState_Type(Integer32):
    """Custom type asioStatOprLLState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_AsioStatOprLLState_Type.__name__ = "Integer32"
_AsioStatOprLLState_Object = MibTableColumn
asioStatOprLLState = _AsioStatOprLLState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 52),
    _AsioStatOprLLState_Type()
)
asioStatOprLLState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprLLState.setStatus("mandatory")


class _AsioStatOprRIState_Type(Integer32):
    """Custom type asioStatOprRIState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_AsioStatOprRIState_Type.__name__ = "Integer32"
_AsioStatOprRIState_Object = MibTableColumn
asioStatOprRIState = _AsioStatOprRIState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 53),
    _AsioStatOprRIState_Type()
)
asioStatOprRIState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRIState.setStatus("mandatory")


class _AsioStatOprRLState_Type(Integer32):
    """Custom type asioStatOprRLState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 3),
          ("inactive", 2),
          ("unknown", 1))
    )


_AsioStatOprRLState_Type.__name__ = "Integer32"
_AsioStatOprRLState_Object = MibTableColumn
asioStatOprRLState = _AsioStatOprRLState_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 54),
    _AsioStatOprRLState_Type()
)
asioStatOprRLState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRLState.setStatus("mandatory")
_AsioStatOprTxBps_Type = Counter32
_AsioStatOprTxBps_Object = MibTableColumn
asioStatOprTxBps = _AsioStatOprTxBps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 59),
    _AsioStatOprTxBps_Type()
)
asioStatOprTxBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprTxBps.setStatus("mandatory")
_AsioStatOprRxBps_Type = Counter32
_AsioStatOprRxBps_Object = MibTableColumn
asioStatOprRxBps = _AsioStatOprRxBps_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 60),
    _AsioStatOprRxBps_Type()
)
asioStatOprRxBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRxBps.setStatus("mandatory")
_AsioStatOprTxBpsMax_Type = Counter32
_AsioStatOprTxBpsMax_Object = MibTableColumn
asioStatOprTxBpsMax = _AsioStatOprTxBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 61),
    _AsioStatOprTxBpsMax_Type()
)
asioStatOprTxBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprTxBpsMax.setStatus("mandatory")
_AsioStatOprRxBpsMax_Type = Counter32
_AsioStatOprRxBpsMax_Object = MibTableColumn
asioStatOprRxBpsMax = _AsioStatOprRxBpsMax_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 62),
    _AsioStatOprRxBpsMax_Type()
)
asioStatOprRxBpsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRxBpsMax.setStatus("mandatory")
_AsioStatOprTxCharacters_Type = Counter32
_AsioStatOprTxCharacters_Object = MibTableColumn
asioStatOprTxCharacters = _AsioStatOprTxCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 63),
    _AsioStatOprTxCharacters_Type()
)
asioStatOprTxCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprTxCharacters.setStatus("mandatory")
_AsioStatOprTxBadStateDiscards_Type = Counter32
_AsioStatOprTxBadStateDiscards_Object = MibTableColumn
asioStatOprTxBadStateDiscards = _AsioStatOprTxBadStateDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 64),
    _AsioStatOprTxBadStateDiscards_Type()
)
asioStatOprTxBadStateDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprTxBadStateDiscards.setStatus("mandatory")
_AsioStatOprTxResetDiscards_Type = Counter32
_AsioStatOprTxResetDiscards_Object = MibTableColumn
asioStatOprTxResetDiscards = _AsioStatOprTxResetDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 65),
    _AsioStatOprTxResetDiscards_Type()
)
asioStatOprTxResetDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprTxResetDiscards.setStatus("mandatory")
_AsioStatOprTxSysCongestionDiscards_Type = Counter32
_AsioStatOprTxSysCongestionDiscards_Object = MibTableColumn
asioStatOprTxSysCongestionDiscards = _AsioStatOprTxSysCongestionDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 66),
    _AsioStatOprTxSysCongestionDiscards_Type()
)
asioStatOprTxSysCongestionDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprTxSysCongestionDiscards.setStatus("mandatory")
_AsioStatOprRxCharacters_Type = Counter32
_AsioStatOprRxCharacters_Object = MibTableColumn
asioStatOprRxCharacters = _AsioStatOprRxCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 72),
    _AsioStatOprRxCharacters_Type()
)
asioStatOprRxCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRxCharacters.setStatus("mandatory")
_AsioStatOprRxOverrunErrorCharacters_Type = Counter32
_AsioStatOprRxOverrunErrorCharacters_Object = MibTableColumn
asioStatOprRxOverrunErrorCharacters = _AsioStatOprRxOverrunErrorCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 73),
    _AsioStatOprRxOverrunErrorCharacters_Type()
)
asioStatOprRxOverrunErrorCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRxOverrunErrorCharacters.setStatus("mandatory")
_AsioStatOprRxParityErrorCharacters_Type = Counter32
_AsioStatOprRxParityErrorCharacters_Object = MibTableColumn
asioStatOprRxParityErrorCharacters = _AsioStatOprRxParityErrorCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 74),
    _AsioStatOprRxParityErrorCharacters_Type()
)
asioStatOprRxParityErrorCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRxParityErrorCharacters.setStatus("mandatory")
_AsioStatOprRxFramingErrorCharacters_Type = Counter32
_AsioStatOprRxFramingErrorCharacters_Object = MibTableColumn
asioStatOprRxFramingErrorCharacters = _AsioStatOprRxFramingErrorCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 75),
    _AsioStatOprRxFramingErrorCharacters_Type()
)
asioStatOprRxFramingErrorCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRxFramingErrorCharacters.setStatus("mandatory")
_AsioStatOprRxNoiseErrorCharacters_Type = Counter32
_AsioStatOprRxNoiseErrorCharacters_Object = MibTableColumn
asioStatOprRxNoiseErrorCharacters = _AsioStatOprRxNoiseErrorCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 76),
    _AsioStatOprRxNoiseErrorCharacters_Type()
)
asioStatOprRxNoiseErrorCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRxNoiseErrorCharacters.setStatus("mandatory")
_AsioStatOprRxBreakCharacters_Type = Counter32
_AsioStatOprRxBreakCharacters_Object = MibTableColumn
asioStatOprRxBreakCharacters = _AsioStatOprRxBreakCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 77),
    _AsioStatOprRxBreakCharacters_Type()
)
asioStatOprRxBreakCharacters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRxBreakCharacters.setStatus("mandatory")
_AsioStatOprRxBadStateDiscards_Type = Counter32
_AsioStatOprRxBadStateDiscards_Object = MibTableColumn
asioStatOprRxBadStateDiscards = _AsioStatOprRxBadStateDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 78),
    _AsioStatOprRxBadStateDiscards_Type()
)
asioStatOprRxBadStateDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRxBadStateDiscards.setStatus("mandatory")
_AsioStatOprRxBusyDiscards_Type = Counter32
_AsioStatOprRxBusyDiscards_Object = MibTableColumn
asioStatOprRxBusyDiscards = _AsioStatOprRxBusyDiscards_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 79),
    _AsioStatOprRxBusyDiscards_Type()
)
asioStatOprRxBusyDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRxBusyDiscards.setStatus("mandatory")
_AsioStatOprPortStateChanges_Type = Counter32
_AsioStatOprPortStateChanges_Object = MibTableColumn
asioStatOprPortStateChanges = _AsioStatOprPortStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 85),
    _AsioStatOprPortStateChanges_Type()
)
asioStatOprPortStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprPortStateChanges.setStatus("mandatory")
_AsioStatOprDCDStateChanges_Type = Counter32
_AsioStatOprDCDStateChanges_Object = MibTableColumn
asioStatOprDCDStateChanges = _AsioStatOprDCDStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 86),
    _AsioStatOprDCDStateChanges_Type()
)
asioStatOprDCDStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprDCDStateChanges.setStatus("mandatory")
_AsioStatOprDTRStateChanges_Type = Counter32
_AsioStatOprDTRStateChanges_Object = MibTableColumn
asioStatOprDTRStateChanges = _AsioStatOprDTRStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 87),
    _AsioStatOprDTRStateChanges_Type()
)
asioStatOprDTRStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprDTRStateChanges.setStatus("mandatory")
_AsioStatOprRTSStateChanges_Type = Counter32
_AsioStatOprRTSStateChanges_Object = MibTableColumn
asioStatOprRTSStateChanges = _AsioStatOprRTSStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 88),
    _AsioStatOprRTSStateChanges_Type()
)
asioStatOprRTSStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRTSStateChanges.setStatus("mandatory")
_AsioStatOprCTSStateChanges_Type = Counter32
_AsioStatOprCTSStateChanges_Object = MibTableColumn
asioStatOprCTSStateChanges = _AsioStatOprCTSStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 89),
    _AsioStatOprCTSStateChanges_Type()
)
asioStatOprCTSStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprCTSStateChanges.setStatus("mandatory")
_AsioStatOprDSRStateChanges_Type = Counter32
_AsioStatOprDSRStateChanges_Object = MibTableColumn
asioStatOprDSRStateChanges = _AsioStatOprDSRStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 90),
    _AsioStatOprDSRStateChanges_Type()
)
asioStatOprDSRStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprDSRStateChanges.setStatus("mandatory")
_AsioStatOprDRSStateChanges_Type = Counter32
_AsioStatOprDRSStateChanges_Object = MibTableColumn
asioStatOprDRSStateChanges = _AsioStatOprDRSStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 91),
    _AsioStatOprDRSStateChanges_Type()
)
asioStatOprDRSStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprDRSStateChanges.setStatus("mandatory")
_AsioStatOprTMStateChanges_Type = Counter32
_AsioStatOprTMStateChanges_Object = MibTableColumn
asioStatOprTMStateChanges = _AsioStatOprTMStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 92),
    _AsioStatOprTMStateChanges_Type()
)
asioStatOprTMStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprTMStateChanges.setStatus("mandatory")
_AsioStatOprLLStateChanges_Type = Counter32
_AsioStatOprLLStateChanges_Object = MibTableColumn
asioStatOprLLStateChanges = _AsioStatOprLLStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 93),
    _AsioStatOprLLStateChanges_Type()
)
asioStatOprLLStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprLLStateChanges.setStatus("mandatory")
_AsioStatOprRIStateChanges_Type = Counter32
_AsioStatOprRIStateChanges_Object = MibTableColumn
asioStatOprRIStateChanges = _AsioStatOprRIStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 94),
    _AsioStatOprRIStateChanges_Type()
)
asioStatOprRIStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRIStateChanges.setStatus("mandatory")
_AsioStatOprRLStateChanges_Type = Counter32
_AsioStatOprRLStateChanges_Object = MibTableColumn
asioStatOprRLStateChanges = _AsioStatOprRLStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 95),
    _AsioStatOprRLStateChanges_Type()
)
asioStatOprRLStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprRLStateChanges.setStatus("mandatory")
_AsioStatOprPortResets_Type = Counter32
_AsioStatOprPortResets_Object = MibTableColumn
asioStatOprPortResets = _AsioStatOprPortResets_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 1, 1, 96),
    _AsioStatOprPortResets_Type()
)
asioStatOprPortResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioStatOprPortResets.setStatus("mandatory")
_AsioSapAdmTable_Object = MibTable
asioSapAdmTable = _AsioSapAdmTable_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2)
)
if mibBuilder.loadTexts:
    asioSapAdmTable.setStatus("mandatory")
_AsioSapAdmEntry_Object = MibTableRow
asioSapAdmEntry = _AsioSapAdmEntry_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1)
)
asioSapAdmEntry.setIndexNames(
    (0, "CXAsyncIo-MIB", "asioSapAdmNumber"),
)
if mibBuilder.loadTexts:
    asioSapAdmEntry.setStatus("mandatory")
_AsioSapAdmNumber_Type = Integer32
_AsioSapAdmNumber_Object = MibTableColumn
asioSapAdmNumber = _AsioSapAdmNumber_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 1),
    _AsioSapAdmNumber_Type()
)
asioSapAdmNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asioSapAdmNumber.setStatus("mandatory")
_AsioSapAdmAlias_Type = Alias
_AsioSapAdmAlias_Object = MibTableColumn
asioSapAdmAlias = _AsioSapAdmAlias_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 2),
    _AsioSapAdmAlias_Type()
)
asioSapAdmAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmAlias.setStatus("mandatory")


class _AsioSapAdmPortSpeed_Type(Integer32):
    """Custom type asioSapAdmPortSpeed based on Integer32"""
    defaultValue = 9600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 115200),
    )


_AsioSapAdmPortSpeed_Type.__name__ = "Integer32"
_AsioSapAdmPortSpeed_Object = MibTableColumn
asioSapAdmPortSpeed = _AsioSapAdmPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 3),
    _AsioSapAdmPortSpeed_Type()
)
asioSapAdmPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortSpeed.setStatus("mandatory")


class _AsioSapAdmPortCharacterSize_Type(Integer32):
    """Custom type asioSapAdmPortCharacterSize based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_AsioSapAdmPortCharacterSize_Type.__name__ = "Integer32"
_AsioSapAdmPortCharacterSize_Object = MibTableColumn
asioSapAdmPortCharacterSize = _AsioSapAdmPortCharacterSize_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 5),
    _AsioSapAdmPortCharacterSize_Type()
)
asioSapAdmPortCharacterSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortCharacterSize.setStatus("mandatory")


class _AsioSapAdmPortStopBits_Type(Integer32):
    """Custom type asioSapAdmPortStopBits based on Integer32"""
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
        *(("one", 1),
          ("one-point-five", 2),
          ("two", 3))
    )


_AsioSapAdmPortStopBits_Type.__name__ = "Integer32"
_AsioSapAdmPortStopBits_Object = MibTableColumn
asioSapAdmPortStopBits = _AsioSapAdmPortStopBits_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 6),
    _AsioSapAdmPortStopBits_Type()
)
asioSapAdmPortStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortStopBits.setStatus("mandatory")


class _AsioSapAdmPortBreakLength_Type(Integer32):
    """Custom type asioSapAdmPortBreakLength based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AsioSapAdmPortBreakLength_Type.__name__ = "Integer32"
_AsioSapAdmPortBreakLength_Object = MibTableColumn
asioSapAdmPortBreakLength = _AsioSapAdmPortBreakLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 7),
    _AsioSapAdmPortBreakLength_Type()
)
asioSapAdmPortBreakLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortBreakLength.setStatus("mandatory")


class _AsioSapAdmPortMaxQueueLength_Type(Integer32):
    """Custom type asioSapAdmPortMaxQueueLength based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AsioSapAdmPortMaxQueueLength_Type.__name__ = "Integer32"
_AsioSapAdmPortMaxQueueLength_Object = MibTableColumn
asioSapAdmPortMaxQueueLength = _AsioSapAdmPortMaxQueueLength_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 8),
    _AsioSapAdmPortMaxQueueLength_Type()
)
asioSapAdmPortMaxQueueLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortMaxQueueLength.setStatus("mandatory")


class _AsioSapAdmPortQueueUpperThreshold_Type(Integer32):
    """Custom type asioSapAdmPortQueueUpperThreshold based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AsioSapAdmPortQueueUpperThreshold_Type.__name__ = "Integer32"
_AsioSapAdmPortQueueUpperThreshold_Object = MibTableColumn
asioSapAdmPortQueueUpperThreshold = _AsioSapAdmPortQueueUpperThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 9),
    _AsioSapAdmPortQueueUpperThreshold_Type()
)
asioSapAdmPortQueueUpperThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortQueueUpperThreshold.setStatus("mandatory")


class _AsioSapAdmPortQueueLowerThreshold_Type(Integer32):
    """Custom type asioSapAdmPortQueueLowerThreshold based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AsioSapAdmPortQueueLowerThreshold_Type.__name__ = "Integer32"
_AsioSapAdmPortQueueLowerThreshold_Object = MibTableColumn
asioSapAdmPortQueueLowerThreshold = _AsioSapAdmPortQueueLowerThreshold_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 10),
    _AsioSapAdmPortQueueLowerThreshold_Type()
)
asioSapAdmPortQueueLowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortQueueLowerThreshold.setStatus("mandatory")


class _AsioSapAdmPortSignalDownTimer_Type(Integer32):
    """Custom type asioSapAdmPortSignalDownTimer based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AsioSapAdmPortSignalDownTimer_Type.__name__ = "Integer32"
_AsioSapAdmPortSignalDownTimer_Object = MibTableColumn
asioSapAdmPortSignalDownTimer = _AsioSapAdmPortSignalDownTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 11),
    _AsioSapAdmPortSignalDownTimer_Type()
)
asioSapAdmPortSignalDownTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortSignalDownTimer.setStatus("mandatory")


class _AsioSapAdmPortMaxTimeDelay_Type(Integer32):
    """Custom type asioSapAdmPortMaxTimeDelay based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_AsioSapAdmPortMaxTimeDelay_Type.__name__ = "Integer32"
_AsioSapAdmPortMaxTimeDelay_Object = MibTableColumn
asioSapAdmPortMaxTimeDelay = _AsioSapAdmPortMaxTimeDelay_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 12),
    _AsioSapAdmPortMaxTimeDelay_Type()
)
asioSapAdmPortMaxTimeDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortMaxTimeDelay.setStatus("mandatory")


class _AsioSapAdmPortMaxInterruptCharacters_Type(Integer32):
    """Custom type asioSapAdmPortMaxInterruptCharacters based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 40),
    )


_AsioSapAdmPortMaxInterruptCharacters_Type.__name__ = "Integer32"
_AsioSapAdmPortMaxInterruptCharacters_Object = MibTableColumn
asioSapAdmPortMaxInterruptCharacters = _AsioSapAdmPortMaxInterruptCharacters_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 13),
    _AsioSapAdmPortMaxInterruptCharacters_Type()
)
asioSapAdmPortMaxInterruptCharacters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortMaxInterruptCharacters.setStatus("obsolete")


class _AsioSapAdmPortSignalSamplingPeriod_Type(Integer32):
    """Custom type asioSapAdmPortSignalSamplingPeriod based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 100),
    )


_AsioSapAdmPortSignalSamplingPeriod_Type.__name__ = "Integer32"
_AsioSapAdmPortSignalSamplingPeriod_Object = MibTableColumn
asioSapAdmPortSignalSamplingPeriod = _AsioSapAdmPortSignalSamplingPeriod_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 20),
    _AsioSapAdmPortSignalSamplingPeriod_Type()
)
asioSapAdmPortSignalSamplingPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortSignalSamplingPeriod.setStatus("mandatory")


class _AsioSapAdmPortDcdDtrSignalSamples_Type(Integer32):
    """Custom type asioSapAdmPortDcdDtrSignalSamples based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsioSapAdmPortDcdDtrSignalSamples_Type.__name__ = "Integer32"
_AsioSapAdmPortDcdDtrSignalSamples_Object = MibTableColumn
asioSapAdmPortDcdDtrSignalSamples = _AsioSapAdmPortDcdDtrSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 21),
    _AsioSapAdmPortDcdDtrSignalSamples_Type()
)
asioSapAdmPortDcdDtrSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortDcdDtrSignalSamples.setStatus("mandatory")


class _AsioSapAdmPortCtsRtsSignalSamples_Type(Integer32):
    """Custom type asioSapAdmPortCtsRtsSignalSamples based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsioSapAdmPortCtsRtsSignalSamples_Type.__name__ = "Integer32"
_AsioSapAdmPortCtsRtsSignalSamples_Object = MibTableColumn
asioSapAdmPortCtsRtsSignalSamples = _AsioSapAdmPortCtsRtsSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 22),
    _AsioSapAdmPortCtsRtsSignalSamples_Type()
)
asioSapAdmPortCtsRtsSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortCtsRtsSignalSamples.setStatus("mandatory")


class _AsioSapAdmPortDsrDrsSignalSamples_Type(Integer32):
    """Custom type asioSapAdmPortDsrDrsSignalSamples based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsioSapAdmPortDsrDrsSignalSamples_Type.__name__ = "Integer32"
_AsioSapAdmPortDsrDrsSignalSamples_Object = MibTableColumn
asioSapAdmPortDsrDrsSignalSamples = _AsioSapAdmPortDsrDrsSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 23),
    _AsioSapAdmPortDsrDrsSignalSamples_Type()
)
asioSapAdmPortDsrDrsSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortDsrDrsSignalSamples.setStatus("mandatory")


class _AsioSapAdmPortTmLlSignalSamples_Type(Integer32):
    """Custom type asioSapAdmPortTmLlSignalSamples based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsioSapAdmPortTmLlSignalSamples_Type.__name__ = "Integer32"
_AsioSapAdmPortTmLlSignalSamples_Object = MibTableColumn
asioSapAdmPortTmLlSignalSamples = _AsioSapAdmPortTmLlSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 24),
    _AsioSapAdmPortTmLlSignalSamples_Type()
)
asioSapAdmPortTmLlSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortTmLlSignalSamples.setStatus("mandatory")


class _AsioSapAdmPortRiRlSignalSamples_Type(Integer32):
    """Custom type asioSapAdmPortRiRlSignalSamples based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AsioSapAdmPortRiRlSignalSamples_Type.__name__ = "Integer32"
_AsioSapAdmPortRiRlSignalSamples_Object = MibTableColumn
asioSapAdmPortRiRlSignalSamples = _AsioSapAdmPortRiRlSignalSamples_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 25),
    _AsioSapAdmPortRiRlSignalSamples_Type()
)
asioSapAdmPortRiRlSignalSamples.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortRiRlSignalSamples.setStatus("mandatory")


class _AsioSapAdmPortStatisticsTimer_Type(Integer32):
    """Custom type asioSapAdmPortStatisticsTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AsioSapAdmPortStatisticsTimer_Type.__name__ = "Integer32"
_AsioSapAdmPortStatisticsTimer_Object = MibTableColumn
asioSapAdmPortStatisticsTimer = _AsioSapAdmPortStatisticsTimer_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 26),
    _AsioSapAdmPortStatisticsTimer_Type()
)
asioSapAdmPortStatisticsTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortStatisticsTimer.setStatus("mandatory")


class _AsioSapAdmPortCarrierAction_Type(Integer32):
    """Custom type asioSapAdmPortCarrierAction based on Integer32"""
    defaultValue = 2

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


_AsioSapAdmPortCarrierAction_Type.__name__ = "Integer32"
_AsioSapAdmPortCarrierAction_Object = MibTableColumn
asioSapAdmPortCarrierAction = _AsioSapAdmPortCarrierAction_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 27),
    _AsioSapAdmPortCarrierAction_Type()
)
asioSapAdmPortCarrierAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioSapAdmPortCarrierAction.setStatus("mandatory")


class _AsioAdmPortTrap_Type(Integer32):
    """Custom type asioAdmPortTrap based on Integer32"""
    defaultValue = 1

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


_AsioAdmPortTrap_Type.__name__ = "Integer32"
_AsioAdmPortTrap_Object = MibTableColumn
asioAdmPortTrap = _AsioAdmPortTrap_Object(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 2, 1, 30),
    _AsioAdmPortTrap_Type()
)
asioAdmPortTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    asioAdmPortTrap.setStatus("mandatory")

# Managed Objects groups


# Notification objects

asioPortStatusChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 495, 2, 1, 6, 44, 0, 1)
)
asioPortStatusChange.setObjects(
      *(("CXAsyncIo-MIB", "asioSapOprNumber"),
        ("CXAsyncIo-MIB", "asioStatOprPortState"))
)
if mibBuilder.loadTexts:
    asioPortStatusChange.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CXAsyncIo-MIB",
    **{"asioPortStatusChange": asioPortStatusChange,
       "asioSapOprTable": asioSapOprTable,
       "asioSapOprEntry": asioSapOprEntry,
       "asioSapOprNumber": asioSapOprNumber,
       "asioSapOprAlias": asioSapOprAlias,
       "asioSapOprPortSpeed": asioSapOprPortSpeed,
       "asioSapOprPortCharacterSize": asioSapOprPortCharacterSize,
       "asioSapOprPortStopBits": asioSapOprPortStopBits,
       "asioSapOprPortBreakLength": asioSapOprPortBreakLength,
       "asioSapOprPortMaxQueueLength": asioSapOprPortMaxQueueLength,
       "asioSapOprPortQueueUpperThreshold": asioSapOprPortQueueUpperThreshold,
       "asioSapOprPortQueueLowerThreshold": asioSapOprPortQueueLowerThreshold,
       "asioSapOprPortSignalDownTimer": asioSapOprPortSignalDownTimer,
       "asioSapOprPortMaxTimeDelay": asioSapOprPortMaxTimeDelay,
       "asioSapOprPortMaxInterruptCharacters": asioSapOprPortMaxInterruptCharacters,
       "asioSapOprPortSignalSamplingPeriod": asioSapOprPortSignalSamplingPeriod,
       "asioSapOprPortDcdDtrSignalSamples": asioSapOprPortDcdDtrSignalSamples,
       "asioSapOprPortCtsRtsSignalSamples": asioSapOprPortCtsRtsSignalSamples,
       "asioSapOprPortDsrDrsSignalSamples": asioSapOprPortDsrDrsSignalSamples,
       "asioSapOprPortTmLlSignalSamples": asioSapOprPortTmLlSignalSamples,
       "asioSapOprPortRiRlSignalSamples": asioSapOprPortRiRlSignalSamples,
       "asioSapOprPortStatisticsTimer": asioSapOprPortStatisticsTimer,
       "asioSapOprPortCarrierAction": asioSapOprPortCarrierAction,
       "asioOprPortTrap": asioOprPortTrap,
       "asioOprControlLine": asioOprControlLine,
       "asioOprControlStats": asioOprControlStats,
       "asioStatOprPortType": asioStatOprPortType,
       "asioStatOprPortInterfaceType": asioStatOprPortInterfaceType,
       "asioStatOprPortState": asioStatOprPortState,
       "asioStatOprDCDState": asioStatOprDCDState,
       "asioStatOprDTRState": asioStatOprDTRState,
       "asioStatOprRTSState": asioStatOprRTSState,
       "asioStatOprCTSState": asioStatOprCTSState,
       "asioStatOprDSRState": asioStatOprDSRState,
       "asioStatOprDRSState": asioStatOprDRSState,
       "asioStatOprTMState": asioStatOprTMState,
       "asioStatOprLLState": asioStatOprLLState,
       "asioStatOprRIState": asioStatOprRIState,
       "asioStatOprRLState": asioStatOprRLState,
       "asioStatOprTxBps": asioStatOprTxBps,
       "asioStatOprRxBps": asioStatOprRxBps,
       "asioStatOprTxBpsMax": asioStatOprTxBpsMax,
       "asioStatOprRxBpsMax": asioStatOprRxBpsMax,
       "asioStatOprTxCharacters": asioStatOprTxCharacters,
       "asioStatOprTxBadStateDiscards": asioStatOprTxBadStateDiscards,
       "asioStatOprTxResetDiscards": asioStatOprTxResetDiscards,
       "asioStatOprTxSysCongestionDiscards": asioStatOprTxSysCongestionDiscards,
       "asioStatOprRxCharacters": asioStatOprRxCharacters,
       "asioStatOprRxOverrunErrorCharacters": asioStatOprRxOverrunErrorCharacters,
       "asioStatOprRxParityErrorCharacters": asioStatOprRxParityErrorCharacters,
       "asioStatOprRxFramingErrorCharacters": asioStatOprRxFramingErrorCharacters,
       "asioStatOprRxNoiseErrorCharacters": asioStatOprRxNoiseErrorCharacters,
       "asioStatOprRxBreakCharacters": asioStatOprRxBreakCharacters,
       "asioStatOprRxBadStateDiscards": asioStatOprRxBadStateDiscards,
       "asioStatOprRxBusyDiscards": asioStatOprRxBusyDiscards,
       "asioStatOprPortStateChanges": asioStatOprPortStateChanges,
       "asioStatOprDCDStateChanges": asioStatOprDCDStateChanges,
       "asioStatOprDTRStateChanges": asioStatOprDTRStateChanges,
       "asioStatOprRTSStateChanges": asioStatOprRTSStateChanges,
       "asioStatOprCTSStateChanges": asioStatOprCTSStateChanges,
       "asioStatOprDSRStateChanges": asioStatOprDSRStateChanges,
       "asioStatOprDRSStateChanges": asioStatOprDRSStateChanges,
       "asioStatOprTMStateChanges": asioStatOprTMStateChanges,
       "asioStatOprLLStateChanges": asioStatOprLLStateChanges,
       "asioStatOprRIStateChanges": asioStatOprRIStateChanges,
       "asioStatOprRLStateChanges": asioStatOprRLStateChanges,
       "asioStatOprPortResets": asioStatOprPortResets,
       "asioSapAdmTable": asioSapAdmTable,
       "asioSapAdmEntry": asioSapAdmEntry,
       "asioSapAdmNumber": asioSapAdmNumber,
       "asioSapAdmAlias": asioSapAdmAlias,
       "asioSapAdmPortSpeed": asioSapAdmPortSpeed,
       "asioSapAdmPortCharacterSize": asioSapAdmPortCharacterSize,
       "asioSapAdmPortStopBits": asioSapAdmPortStopBits,
       "asioSapAdmPortBreakLength": asioSapAdmPortBreakLength,
       "asioSapAdmPortMaxQueueLength": asioSapAdmPortMaxQueueLength,
       "asioSapAdmPortQueueUpperThreshold": asioSapAdmPortQueueUpperThreshold,
       "asioSapAdmPortQueueLowerThreshold": asioSapAdmPortQueueLowerThreshold,
       "asioSapAdmPortSignalDownTimer": asioSapAdmPortSignalDownTimer,
       "asioSapAdmPortMaxTimeDelay": asioSapAdmPortMaxTimeDelay,
       "asioSapAdmPortMaxInterruptCharacters": asioSapAdmPortMaxInterruptCharacters,
       "asioSapAdmPortSignalSamplingPeriod": asioSapAdmPortSignalSamplingPeriod,
       "asioSapAdmPortDcdDtrSignalSamples": asioSapAdmPortDcdDtrSignalSamples,
       "asioSapAdmPortCtsRtsSignalSamples": asioSapAdmPortCtsRtsSignalSamples,
       "asioSapAdmPortDsrDrsSignalSamples": asioSapAdmPortDsrDrsSignalSamples,
       "asioSapAdmPortTmLlSignalSamples": asioSapAdmPortTmLlSignalSamples,
       "asioSapAdmPortRiRlSignalSamples": asioSapAdmPortRiRlSignalSamples,
       "asioSapAdmPortStatisticsTimer": asioSapAdmPortStatisticsTimer,
       "asioSapAdmPortCarrierAction": asioSapAdmPortCarrierAction,
       "asioAdmPortTrap": asioAdmPortTrap}
)
