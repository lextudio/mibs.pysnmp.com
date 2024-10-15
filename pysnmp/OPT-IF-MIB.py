# SNMP MIB module (OPT-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file:///Users/lextm/pysnmp.com/mibs.pysnmp.com/asn1/OPT-IF-MIB
# Produced by pysmi-1.5.4 at Mon Oct 14 22:35:25 2024
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

optIfMibModule = ModuleIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133)
)
optIfMibModule.setRevisions(
        ("2003-08-13 00:00",)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class OptIfAcTI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )



class OptIfBitRateK(Integer32, TextualConvention):
    status = "current"


class OptIfDEGM(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )



class OptIfDEGThr(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )



class OptIfDirectionality(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bidirectional", 3),
          ("sink", 1),
          ("source", 2))
    )



class OptIfSinkOrSource(Integer32, TextualConvention):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sink", 1),
          ("source", 2))
    )



class OptIfExDAPI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class OptIfExSAPI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )



class OptIfIntervalNumber(Unsigned32, TextualConvention):
    status = "current"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )



class OptIfTIMDetMode(Integer32, TextualConvention):
    status = "current"
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
          ("dapi", 2),
          ("off", 1),
          ("sapi", 3))
    )



class OptIfTxTI(OctetString, TextualConvention):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )



# MIB Managed Objects in the order of their OIDs

_OptIfObjects_ObjectIdentity = ObjectIdentity
optIfObjects = _OptIfObjects_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 1)
)
_OptIfOTMn_ObjectIdentity = ObjectIdentity
optIfOTMn = _OptIfOTMn_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 1)
)
_OptIfOTMnTable_Object = MibTable
optIfOTMnTable = _OptIfOTMnTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 1, 1)
)
if mibBuilder.loadTexts:
    optIfOTMnTable.setStatus("current")
_OptIfOTMnEntry_Object = MibTableRow
optIfOTMnEntry = _OptIfOTMnEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 1, 1, 1)
)
optIfOTMnEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOTMnEntry.setStatus("current")


class _OptIfOTMnOrder_Type(Unsigned32):
    """Custom type optIfOTMnOrder based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_OptIfOTMnOrder_Type.__name__ = "Unsigned32"
_OptIfOTMnOrder_Object = MibTableColumn
optIfOTMnOrder = _OptIfOTMnOrder_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 1, 1, 1, 1),
    _OptIfOTMnOrder_Type()
)
optIfOTMnOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTMnOrder.setStatus("current")
_OptIfOTMnReduced_Type = TruthValue
_OptIfOTMnReduced_Object = MibTableColumn
optIfOTMnReduced = _OptIfOTMnReduced_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 1, 1, 1, 2),
    _OptIfOTMnReduced_Type()
)
optIfOTMnReduced.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTMnReduced.setStatus("current")


class _OptIfOTMnBitRates_Type(Bits):
    """Custom type optIfOTMnBitRates based on Bits"""
    namedValues = NamedValues(
        *(("bitRateK1", 0),
          ("bitRateK2", 1),
          ("bitRateK3", 2))
    )

_OptIfOTMnBitRates_Type.__name__ = "Bits"
_OptIfOTMnBitRates_Object = MibTableColumn
optIfOTMnBitRates = _OptIfOTMnBitRates_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 1, 1, 1, 3),
    _OptIfOTMnBitRates_Type()
)
optIfOTMnBitRates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTMnBitRates.setStatus("current")
_OptIfOTMnInterfaceType_Type = SnmpAdminString
_OptIfOTMnInterfaceType_Object = MibTableColumn
optIfOTMnInterfaceType = _OptIfOTMnInterfaceType_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 1, 1, 1, 4),
    _OptIfOTMnInterfaceType_Type()
)
optIfOTMnInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTMnInterfaceType.setStatus("current")


class _OptIfOTMnTcmMax_Type(Unsigned32):
    """Custom type optIfOTMnTcmMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_OptIfOTMnTcmMax_Type.__name__ = "Unsigned32"
_OptIfOTMnTcmMax_Object = MibTableColumn
optIfOTMnTcmMax = _OptIfOTMnTcmMax_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 1, 1, 1, 5),
    _OptIfOTMnTcmMax_Type()
)
optIfOTMnTcmMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTMnTcmMax.setStatus("current")


class _OptIfOTMnOpticalReach_Type(Integer32):
    """Custom type optIfOTMnOpticalReach based on Integer32"""
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
        *(("intraOffice", 1),
          ("longHaul", 3),
          ("shortHaul", 2),
          ("ultraLongHaul", 5),
          ("veryLongHaul", 4))
    )


_OptIfOTMnOpticalReach_Type.__name__ = "Integer32"
_OptIfOTMnOpticalReach_Object = MibTableColumn
optIfOTMnOpticalReach = _OptIfOTMnOpticalReach_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 1, 1, 1, 6),
    _OptIfOTMnOpticalReach_Type()
)
optIfOTMnOpticalReach.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTMnOpticalReach.setStatus("current")
_OptIfPerfMon_ObjectIdentity = ObjectIdentity
optIfPerfMon = _OptIfPerfMon_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 2)
)
_OptIfPerfMonIntervalTable_Object = MibTable
optIfPerfMonIntervalTable = _OptIfPerfMonIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 2, 1)
)
if mibBuilder.loadTexts:
    optIfPerfMonIntervalTable.setStatus("current")
_OptIfPerfMonIntervalEntry_Object = MibTableRow
optIfPerfMonIntervalEntry = _OptIfPerfMonIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 2, 1, 1)
)
optIfPerfMonIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfPerfMonIntervalEntry.setStatus("current")


class _OptIfPerfMonCurrentTimeElapsed_Type(Gauge32):
    """Custom type optIfPerfMonCurrentTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_OptIfPerfMonCurrentTimeElapsed_Type.__name__ = "Gauge32"
_OptIfPerfMonCurrentTimeElapsed_Object = MibTableColumn
optIfPerfMonCurrentTimeElapsed = _OptIfPerfMonCurrentTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 2, 1, 1, 1),
    _OptIfPerfMonCurrentTimeElapsed_Type()
)
optIfPerfMonCurrentTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfPerfMonCurrentTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    optIfPerfMonCurrentTimeElapsed.setUnits("seconds")


class _OptIfPerfMonCurDayTimeElapsed_Type(Gauge32):
    """Custom type optIfPerfMonCurDayTimeElapsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_OptIfPerfMonCurDayTimeElapsed_Type.__name__ = "Gauge32"
_OptIfPerfMonCurDayTimeElapsed_Object = MibTableColumn
optIfPerfMonCurDayTimeElapsed = _OptIfPerfMonCurDayTimeElapsed_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 2, 1, 1, 2),
    _OptIfPerfMonCurDayTimeElapsed_Type()
)
optIfPerfMonCurDayTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfPerfMonCurDayTimeElapsed.setStatus("current")
if mibBuilder.loadTexts:
    optIfPerfMonCurDayTimeElapsed.setUnits("seconds")


class _OptIfPerfMonIntervalNumIntervals_Type(Unsigned32):
    """Custom type optIfPerfMonIntervalNumIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_OptIfPerfMonIntervalNumIntervals_Type.__name__ = "Unsigned32"
_OptIfPerfMonIntervalNumIntervals_Object = MibTableColumn
optIfPerfMonIntervalNumIntervals = _OptIfPerfMonIntervalNumIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 2, 1, 1, 3),
    _OptIfPerfMonIntervalNumIntervals_Type()
)
optIfPerfMonIntervalNumIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfPerfMonIntervalNumIntervals.setStatus("current")


class _OptIfPerfMonIntervalNumInvalidIntervals_Type(Unsigned32):
    """Custom type optIfPerfMonIntervalNumInvalidIntervals based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 96),
    )


_OptIfPerfMonIntervalNumInvalidIntervals_Type.__name__ = "Unsigned32"
_OptIfPerfMonIntervalNumInvalidIntervals_Object = MibTableColumn
optIfPerfMonIntervalNumInvalidIntervals = _OptIfPerfMonIntervalNumInvalidIntervals_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 2, 1, 1, 4),
    _OptIfPerfMonIntervalNumInvalidIntervals_Type()
)
optIfPerfMonIntervalNumInvalidIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfPerfMonIntervalNumInvalidIntervals.setStatus("current")
_OptIfOTSn_ObjectIdentity = ObjectIdentity
optIfOTSn = _OptIfOTSn_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3)
)
_OptIfOTSnConfigTable_Object = MibTable
optIfOTSnConfigTable = _OptIfOTSnConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1)
)
if mibBuilder.loadTexts:
    optIfOTSnConfigTable.setStatus("current")
_OptIfOTSnConfigEntry_Object = MibTableRow
optIfOTSnConfigEntry = _OptIfOTSnConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1)
)
optIfOTSnConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOTSnConfigEntry.setStatus("current")
_OptIfOTSnDirectionality_Type = OptIfDirectionality
_OptIfOTSnDirectionality_Object = MibTableColumn
optIfOTSnDirectionality = _OptIfOTSnDirectionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1, 1),
    _OptIfOTSnDirectionality_Type()
)
optIfOTSnDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnDirectionality.setStatus("current")
_OptIfOTSnAprStatus_Type = SnmpAdminString
_OptIfOTSnAprStatus_Object = MibTableColumn
optIfOTSnAprStatus = _OptIfOTSnAprStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1, 2),
    _OptIfOTSnAprStatus_Type()
)
optIfOTSnAprStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnAprStatus.setStatus("current")
_OptIfOTSnAprControl_Type = SnmpAdminString
_OptIfOTSnAprControl_Object = MibTableColumn
optIfOTSnAprControl = _OptIfOTSnAprControl_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1, 3),
    _OptIfOTSnAprControl_Type()
)
optIfOTSnAprControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnAprControl.setStatus("current")
_OptIfOTSnTraceIdentifierTransmitted_Type = OptIfTxTI
_OptIfOTSnTraceIdentifierTransmitted_Object = MibTableColumn
optIfOTSnTraceIdentifierTransmitted = _OptIfOTSnTraceIdentifierTransmitted_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1, 4),
    _OptIfOTSnTraceIdentifierTransmitted_Type()
)
optIfOTSnTraceIdentifierTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnTraceIdentifierTransmitted.setStatus("current")
_OptIfOTSnDAPIExpected_Type = OptIfExDAPI
_OptIfOTSnDAPIExpected_Object = MibTableColumn
optIfOTSnDAPIExpected = _OptIfOTSnDAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1, 5),
    _OptIfOTSnDAPIExpected_Type()
)
optIfOTSnDAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnDAPIExpected.setStatus("current")
_OptIfOTSnSAPIExpected_Type = OptIfExSAPI
_OptIfOTSnSAPIExpected_Object = MibTableColumn
optIfOTSnSAPIExpected = _OptIfOTSnSAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1, 6),
    _OptIfOTSnSAPIExpected_Type()
)
optIfOTSnSAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnSAPIExpected.setStatus("current")
_OptIfOTSnTraceIdentifierAccepted_Type = OptIfAcTI
_OptIfOTSnTraceIdentifierAccepted_Object = MibTableColumn
optIfOTSnTraceIdentifierAccepted = _OptIfOTSnTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1, 7),
    _OptIfOTSnTraceIdentifierAccepted_Type()
)
optIfOTSnTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnTraceIdentifierAccepted.setStatus("current")
_OptIfOTSnTIMDetMode_Type = OptIfTIMDetMode
_OptIfOTSnTIMDetMode_Object = MibTableColumn
optIfOTSnTIMDetMode = _OptIfOTSnTIMDetMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1, 8),
    _OptIfOTSnTIMDetMode_Type()
)
optIfOTSnTIMDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnTIMDetMode.setStatus("current")
_OptIfOTSnTIMActEnabled_Type = TruthValue
_OptIfOTSnTIMActEnabled_Object = MibTableColumn
optIfOTSnTIMActEnabled = _OptIfOTSnTIMActEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1, 9),
    _OptIfOTSnTIMActEnabled_Type()
)
optIfOTSnTIMActEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnTIMActEnabled.setStatus("current")


class _OptIfOTSnCurrentStatus_Type(Bits):
    """Custom type optIfOTSnCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 2),
          ("bdiO", 1),
          ("bdiP", 0),
          ("los", 6),
          ("losO", 5),
          ("losP", 4),
          ("tim", 3))
    )

_OptIfOTSnCurrentStatus_Type.__name__ = "Bits"
_OptIfOTSnCurrentStatus_Object = MibTableColumn
optIfOTSnCurrentStatus = _OptIfOTSnCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 1, 1, 10),
    _OptIfOTSnCurrentStatus_Type()
)
optIfOTSnCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnCurrentStatus.setStatus("current")
_OptIfOTSnSinkCurrentTable_Object = MibTable
optIfOTSnSinkCurrentTable = _OptIfOTSnSinkCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2)
)
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentTable.setStatus("current")
_OptIfOTSnSinkCurrentEntry_Object = MibTableRow
optIfOTSnSinkCurrentEntry = _OptIfOTSnSinkCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1)
)
optIfOTSnSinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentEntry.setStatus("current")
_OptIfOTSnSinkCurrentSuspectedFlag_Type = TruthValue
_OptIfOTSnSinkCurrentSuspectedFlag_Object = MibTableColumn
optIfOTSnSinkCurrentSuspectedFlag = _OptIfOTSnSinkCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 1),
    _OptIfOTSnSinkCurrentSuspectedFlag_Type()
)
optIfOTSnSinkCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentSuspectedFlag.setStatus("current")
_OptIfOTSnSinkCurrentInputPower_Type = Integer32
_OptIfOTSnSinkCurrentInputPower_Object = MibTableColumn
optIfOTSnSinkCurrentInputPower = _OptIfOTSnSinkCurrentInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 2),
    _OptIfOTSnSinkCurrentInputPower_Type()
)
optIfOTSnSinkCurrentInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkCurrentLowInputPower_Type = Integer32
_OptIfOTSnSinkCurrentLowInputPower_Object = MibTableColumn
optIfOTSnSinkCurrentLowInputPower = _OptIfOTSnSinkCurrentLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 3),
    _OptIfOTSnSinkCurrentLowInputPower_Type()
)
optIfOTSnSinkCurrentLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentLowInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkCurrentHighInputPower_Type = Integer32
_OptIfOTSnSinkCurrentHighInputPower_Object = MibTableColumn
optIfOTSnSinkCurrentHighInputPower = _OptIfOTSnSinkCurrentHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 4),
    _OptIfOTSnSinkCurrentHighInputPower_Type()
)
optIfOTSnSinkCurrentHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentHighInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkCurrentLowerInputPowerThreshold_Type = Integer32
_OptIfOTSnSinkCurrentLowerInputPowerThreshold_Object = MibTableColumn
optIfOTSnSinkCurrentLowerInputPowerThreshold = _OptIfOTSnSinkCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 5),
    _OptIfOTSnSinkCurrentLowerInputPowerThreshold_Type()
)
optIfOTSnSinkCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOTSnSinkCurrentUpperInputPowerThreshold_Type = Integer32
_OptIfOTSnSinkCurrentUpperInputPowerThreshold_Object = MibTableColumn
optIfOTSnSinkCurrentUpperInputPowerThreshold = _OptIfOTSnSinkCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 6),
    _OptIfOTSnSinkCurrentUpperInputPowerThreshold_Type()
)
optIfOTSnSinkCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOTSnSinkCurrentOutputPower_Type = Integer32
_OptIfOTSnSinkCurrentOutputPower_Object = MibTableColumn
optIfOTSnSinkCurrentOutputPower = _OptIfOTSnSinkCurrentOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 7),
    _OptIfOTSnSinkCurrentOutputPower_Type()
)
optIfOTSnSinkCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkCurrentLowOutputPower_Type = Integer32
_OptIfOTSnSinkCurrentLowOutputPower_Object = MibTableColumn
optIfOTSnSinkCurrentLowOutputPower = _OptIfOTSnSinkCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 8),
    _OptIfOTSnSinkCurrentLowOutputPower_Type()
)
optIfOTSnSinkCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentLowOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkCurrentHighOutputPower_Type = Integer32
_OptIfOTSnSinkCurrentHighOutputPower_Object = MibTableColumn
optIfOTSnSinkCurrentHighOutputPower = _OptIfOTSnSinkCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 9),
    _OptIfOTSnSinkCurrentHighOutputPower_Type()
)
optIfOTSnSinkCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentHighOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkCurrentLowerOutputPowerThreshold_Type = Integer32
_OptIfOTSnSinkCurrentLowerOutputPowerThreshold_Object = MibTableColumn
optIfOTSnSinkCurrentLowerOutputPowerThreshold = _OptIfOTSnSinkCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 10),
    _OptIfOTSnSinkCurrentLowerOutputPowerThreshold_Type()
)
optIfOTSnSinkCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOTSnSinkCurrentUpperOutputPowerThreshold_Type = Integer32
_OptIfOTSnSinkCurrentUpperOutputPowerThreshold_Object = MibTableColumn
optIfOTSnSinkCurrentUpperOutputPowerThreshold = _OptIfOTSnSinkCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 2, 1, 11),
    _OptIfOTSnSinkCurrentUpperOutputPowerThreshold_Type()
)
optIfOTSnSinkCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOTSnSinkIntervalTable_Object = MibTable
optIfOTSnSinkIntervalTable = _OptIfOTSnSinkIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 3)
)
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalTable.setStatus("current")
_OptIfOTSnSinkIntervalEntry_Object = MibTableRow
optIfOTSnSinkIntervalEntry = _OptIfOTSnSinkIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 3, 1)
)
optIfOTSnSinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfOTSnSinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalEntry.setStatus("current")
_OptIfOTSnSinkIntervalNumber_Type = OptIfIntervalNumber
_OptIfOTSnSinkIntervalNumber_Object = MibTableColumn
optIfOTSnSinkIntervalNumber = _OptIfOTSnSinkIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 3, 1, 1),
    _OptIfOTSnSinkIntervalNumber_Type()
)
optIfOTSnSinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalNumber.setStatus("current")
_OptIfOTSnSinkIntervalSuspectedFlag_Type = TruthValue
_OptIfOTSnSinkIntervalSuspectedFlag_Object = MibTableColumn
optIfOTSnSinkIntervalSuspectedFlag = _OptIfOTSnSinkIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 3, 1, 2),
    _OptIfOTSnSinkIntervalSuspectedFlag_Type()
)
optIfOTSnSinkIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalSuspectedFlag.setStatus("current")
_OptIfOTSnSinkIntervalLastInputPower_Type = Integer32
_OptIfOTSnSinkIntervalLastInputPower_Object = MibTableColumn
optIfOTSnSinkIntervalLastInputPower = _OptIfOTSnSinkIntervalLastInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 3, 1, 3),
    _OptIfOTSnSinkIntervalLastInputPower_Type()
)
optIfOTSnSinkIntervalLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalLastInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkIntervalLowInputPower_Type = Integer32
_OptIfOTSnSinkIntervalLowInputPower_Object = MibTableColumn
optIfOTSnSinkIntervalLowInputPower = _OptIfOTSnSinkIntervalLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 3, 1, 4),
    _OptIfOTSnSinkIntervalLowInputPower_Type()
)
optIfOTSnSinkIntervalLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalLowInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkIntervalHighInputPower_Type = Integer32
_OptIfOTSnSinkIntervalHighInputPower_Object = MibTableColumn
optIfOTSnSinkIntervalHighInputPower = _OptIfOTSnSinkIntervalHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 3, 1, 5),
    _OptIfOTSnSinkIntervalHighInputPower_Type()
)
optIfOTSnSinkIntervalHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalHighInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkIntervalLastOutputPower_Type = Integer32
_OptIfOTSnSinkIntervalLastOutputPower_Object = MibTableColumn
optIfOTSnSinkIntervalLastOutputPower = _OptIfOTSnSinkIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 3, 1, 6),
    _OptIfOTSnSinkIntervalLastOutputPower_Type()
)
optIfOTSnSinkIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalLastOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkIntervalLowOutputPower_Type = Integer32
_OptIfOTSnSinkIntervalLowOutputPower_Object = MibTableColumn
optIfOTSnSinkIntervalLowOutputPower = _OptIfOTSnSinkIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 3, 1, 7),
    _OptIfOTSnSinkIntervalLowOutputPower_Type()
)
optIfOTSnSinkIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalLowOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkIntervalHighOutputPower_Type = Integer32
_OptIfOTSnSinkIntervalHighOutputPower_Object = MibTableColumn
optIfOTSnSinkIntervalHighOutputPower = _OptIfOTSnSinkIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 3, 1, 8),
    _OptIfOTSnSinkIntervalHighOutputPower_Type()
)
optIfOTSnSinkIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkIntervalHighOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkCurDayTable_Object = MibTable
optIfOTSnSinkCurDayTable = _OptIfOTSnSinkCurDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 4)
)
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDayTable.setStatus("current")
_OptIfOTSnSinkCurDayEntry_Object = MibTableRow
optIfOTSnSinkCurDayEntry = _OptIfOTSnSinkCurDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 4, 1)
)
optIfOTSnSinkCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDayEntry.setStatus("current")
_OptIfOTSnSinkCurDaySuspectedFlag_Type = TruthValue
_OptIfOTSnSinkCurDaySuspectedFlag_Object = MibTableColumn
optIfOTSnSinkCurDaySuspectedFlag = _OptIfOTSnSinkCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 4, 1, 1),
    _OptIfOTSnSinkCurDaySuspectedFlag_Type()
)
optIfOTSnSinkCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDaySuspectedFlag.setStatus("current")
_OptIfOTSnSinkCurDayLowInputPower_Type = Integer32
_OptIfOTSnSinkCurDayLowInputPower_Object = MibTableColumn
optIfOTSnSinkCurDayLowInputPower = _OptIfOTSnSinkCurDayLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 4, 1, 2),
    _OptIfOTSnSinkCurDayLowInputPower_Type()
)
optIfOTSnSinkCurDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDayLowInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkCurDayHighInputPower_Type = Integer32
_OptIfOTSnSinkCurDayHighInputPower_Object = MibTableColumn
optIfOTSnSinkCurDayHighInputPower = _OptIfOTSnSinkCurDayHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 4, 1, 3),
    _OptIfOTSnSinkCurDayHighInputPower_Type()
)
optIfOTSnSinkCurDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDayHighInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkCurDayLowOutputPower_Type = Integer32
_OptIfOTSnSinkCurDayLowOutputPower_Object = MibTableColumn
optIfOTSnSinkCurDayLowOutputPower = _OptIfOTSnSinkCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 4, 1, 4),
    _OptIfOTSnSinkCurDayLowOutputPower_Type()
)
optIfOTSnSinkCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkCurDayHighOutputPower_Type = Integer32
_OptIfOTSnSinkCurDayHighOutputPower_Object = MibTableColumn
optIfOTSnSinkCurDayHighOutputPower = _OptIfOTSnSinkCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 4, 1, 5),
    _OptIfOTSnSinkCurDayHighOutputPower_Type()
)
optIfOTSnSinkCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkCurDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkPrevDayTable_Object = MibTable
optIfOTSnSinkPrevDayTable = _OptIfOTSnSinkPrevDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 5)
)
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayTable.setStatus("current")
_OptIfOTSnSinkPrevDayEntry_Object = MibTableRow
optIfOTSnSinkPrevDayEntry = _OptIfOTSnSinkPrevDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 5, 1)
)
optIfOTSnSinkPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayEntry.setStatus("current")
_OptIfOTSnSinkPrevDaySuspectedFlag_Type = TruthValue
_OptIfOTSnSinkPrevDaySuspectedFlag_Object = MibTableColumn
optIfOTSnSinkPrevDaySuspectedFlag = _OptIfOTSnSinkPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 5, 1, 1),
    _OptIfOTSnSinkPrevDaySuspectedFlag_Type()
)
optIfOTSnSinkPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDaySuspectedFlag.setStatus("current")
_OptIfOTSnSinkPrevDayLastInputPower_Type = Integer32
_OptIfOTSnSinkPrevDayLastInputPower_Object = MibTableColumn
optIfOTSnSinkPrevDayLastInputPower = _OptIfOTSnSinkPrevDayLastInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 5, 1, 2),
    _OptIfOTSnSinkPrevDayLastInputPower_Type()
)
optIfOTSnSinkPrevDayLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayLastInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkPrevDayLowInputPower_Type = Integer32
_OptIfOTSnSinkPrevDayLowInputPower_Object = MibTableColumn
optIfOTSnSinkPrevDayLowInputPower = _OptIfOTSnSinkPrevDayLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 5, 1, 3),
    _OptIfOTSnSinkPrevDayLowInputPower_Type()
)
optIfOTSnSinkPrevDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayLowInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkPrevDayHighInputPower_Type = Integer32
_OptIfOTSnSinkPrevDayHighInputPower_Object = MibTableColumn
optIfOTSnSinkPrevDayHighInputPower = _OptIfOTSnSinkPrevDayHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 5, 1, 4),
    _OptIfOTSnSinkPrevDayHighInputPower_Type()
)
optIfOTSnSinkPrevDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayHighInputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkPrevDayLastOutputPower_Type = Integer32
_OptIfOTSnSinkPrevDayLastOutputPower_Object = MibTableColumn
optIfOTSnSinkPrevDayLastOutputPower = _OptIfOTSnSinkPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 5, 1, 5),
    _OptIfOTSnSinkPrevDayLastOutputPower_Type()
)
optIfOTSnSinkPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayLastOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkPrevDayLowOutputPower_Type = Integer32
_OptIfOTSnSinkPrevDayLowOutputPower_Object = MibTableColumn
optIfOTSnSinkPrevDayLowOutputPower = _OptIfOTSnSinkPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 5, 1, 6),
    _OptIfOTSnSinkPrevDayLowOutputPower_Type()
)
optIfOTSnSinkPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSinkPrevDayHighOutputPower_Type = Integer32
_OptIfOTSnSinkPrevDayHighOutputPower_Object = MibTableColumn
optIfOTSnSinkPrevDayHighOutputPower = _OptIfOTSnSinkPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 5, 1, 7),
    _OptIfOTSnSinkPrevDayHighOutputPower_Type()
)
optIfOTSnSinkPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSinkPrevDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurrentTable_Object = MibTable
optIfOTSnSrcCurrentTable = _OptIfOTSnSrcCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6)
)
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentTable.setStatus("current")
_OptIfOTSnSrcCurrentEntry_Object = MibTableRow
optIfOTSnSrcCurrentEntry = _OptIfOTSnSrcCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1)
)
optIfOTSnSrcCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentEntry.setStatus("current")
_OptIfOTSnSrcCurrentSuspectedFlag_Type = TruthValue
_OptIfOTSnSrcCurrentSuspectedFlag_Object = MibTableColumn
optIfOTSnSrcCurrentSuspectedFlag = _OptIfOTSnSrcCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 1),
    _OptIfOTSnSrcCurrentSuspectedFlag_Type()
)
optIfOTSnSrcCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentSuspectedFlag.setStatus("current")
_OptIfOTSnSrcCurrentOutputPower_Type = Integer32
_OptIfOTSnSrcCurrentOutputPower_Object = MibTableColumn
optIfOTSnSrcCurrentOutputPower = _OptIfOTSnSrcCurrentOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 2),
    _OptIfOTSnSrcCurrentOutputPower_Type()
)
optIfOTSnSrcCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurrentLowOutputPower_Type = Integer32
_OptIfOTSnSrcCurrentLowOutputPower_Object = MibTableColumn
optIfOTSnSrcCurrentLowOutputPower = _OptIfOTSnSrcCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 3),
    _OptIfOTSnSrcCurrentLowOutputPower_Type()
)
optIfOTSnSrcCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentLowOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurrentHighOutputPower_Type = Integer32
_OptIfOTSnSrcCurrentHighOutputPower_Object = MibTableColumn
optIfOTSnSrcCurrentHighOutputPower = _OptIfOTSnSrcCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 4),
    _OptIfOTSnSrcCurrentHighOutputPower_Type()
)
optIfOTSnSrcCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentHighOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurrentLowerOutputPowerThreshold_Type = Integer32
_OptIfOTSnSrcCurrentLowerOutputPowerThreshold_Object = MibTableColumn
optIfOTSnSrcCurrentLowerOutputPowerThreshold = _OptIfOTSnSrcCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 5),
    _OptIfOTSnSrcCurrentLowerOutputPowerThreshold_Type()
)
optIfOTSnSrcCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOTSnSrcCurrentUpperOutputPowerThreshold_Type = Integer32
_OptIfOTSnSrcCurrentUpperOutputPowerThreshold_Object = MibTableColumn
optIfOTSnSrcCurrentUpperOutputPowerThreshold = _OptIfOTSnSrcCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 6),
    _OptIfOTSnSrcCurrentUpperOutputPowerThreshold_Type()
)
optIfOTSnSrcCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOTSnSrcCurrentInputPower_Type = Integer32
_OptIfOTSnSrcCurrentInputPower_Object = MibTableColumn
optIfOTSnSrcCurrentInputPower = _OptIfOTSnSrcCurrentInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 7),
    _OptIfOTSnSrcCurrentInputPower_Type()
)
optIfOTSnSrcCurrentInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentInputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurrentLowInputPower_Type = Integer32
_OptIfOTSnSrcCurrentLowInputPower_Object = MibTableColumn
optIfOTSnSrcCurrentLowInputPower = _OptIfOTSnSrcCurrentLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 8),
    _OptIfOTSnSrcCurrentLowInputPower_Type()
)
optIfOTSnSrcCurrentLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentLowInputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurrentHighInputPower_Type = Integer32
_OptIfOTSnSrcCurrentHighInputPower_Object = MibTableColumn
optIfOTSnSrcCurrentHighInputPower = _OptIfOTSnSrcCurrentHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 9),
    _OptIfOTSnSrcCurrentHighInputPower_Type()
)
optIfOTSnSrcCurrentHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentHighInputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurrentLowerInputPowerThreshold_Type = Integer32
_OptIfOTSnSrcCurrentLowerInputPowerThreshold_Object = MibTableColumn
optIfOTSnSrcCurrentLowerInputPowerThreshold = _OptIfOTSnSrcCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 10),
    _OptIfOTSnSrcCurrentLowerInputPowerThreshold_Type()
)
optIfOTSnSrcCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOTSnSrcCurrentUpperInputPowerThreshold_Type = Integer32
_OptIfOTSnSrcCurrentUpperInputPowerThreshold_Object = MibTableColumn
optIfOTSnSrcCurrentUpperInputPowerThreshold = _OptIfOTSnSrcCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 6, 1, 11),
    _OptIfOTSnSrcCurrentUpperInputPowerThreshold_Type()
)
optIfOTSnSrcCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOTSnSrcIntervalTable_Object = MibTable
optIfOTSnSrcIntervalTable = _OptIfOTSnSrcIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 7)
)
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalTable.setStatus("current")
_OptIfOTSnSrcIntervalEntry_Object = MibTableRow
optIfOTSnSrcIntervalEntry = _OptIfOTSnSrcIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 7, 1)
)
optIfOTSnSrcIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfOTSnSrcIntervalNumber"),
)
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalEntry.setStatus("current")
_OptIfOTSnSrcIntervalNumber_Type = OptIfIntervalNumber
_OptIfOTSnSrcIntervalNumber_Object = MibTableColumn
optIfOTSnSrcIntervalNumber = _OptIfOTSnSrcIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 7, 1, 1),
    _OptIfOTSnSrcIntervalNumber_Type()
)
optIfOTSnSrcIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalNumber.setStatus("current")
_OptIfOTSnSrcIntervalSuspectedFlag_Type = TruthValue
_OptIfOTSnSrcIntervalSuspectedFlag_Object = MibTableColumn
optIfOTSnSrcIntervalSuspectedFlag = _OptIfOTSnSrcIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 7, 1, 2),
    _OptIfOTSnSrcIntervalSuspectedFlag_Type()
)
optIfOTSnSrcIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalSuspectedFlag.setStatus("current")
_OptIfOTSnSrcIntervalLastOutputPower_Type = Integer32
_OptIfOTSnSrcIntervalLastOutputPower_Object = MibTableColumn
optIfOTSnSrcIntervalLastOutputPower = _OptIfOTSnSrcIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 7, 1, 3),
    _OptIfOTSnSrcIntervalLastOutputPower_Type()
)
optIfOTSnSrcIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalLastOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcIntervalLowOutputPower_Type = Integer32
_OptIfOTSnSrcIntervalLowOutputPower_Object = MibTableColumn
optIfOTSnSrcIntervalLowOutputPower = _OptIfOTSnSrcIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 7, 1, 4),
    _OptIfOTSnSrcIntervalLowOutputPower_Type()
)
optIfOTSnSrcIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalLowOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcIntervalHighOutputPower_Type = Integer32
_OptIfOTSnSrcIntervalHighOutputPower_Object = MibTableColumn
optIfOTSnSrcIntervalHighOutputPower = _OptIfOTSnSrcIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 7, 1, 5),
    _OptIfOTSnSrcIntervalHighOutputPower_Type()
)
optIfOTSnSrcIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalHighOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcIntervalLastInputPower_Type = Integer32
_OptIfOTSnSrcIntervalLastInputPower_Object = MibTableColumn
optIfOTSnSrcIntervalLastInputPower = _OptIfOTSnSrcIntervalLastInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 7, 1, 6),
    _OptIfOTSnSrcIntervalLastInputPower_Type()
)
optIfOTSnSrcIntervalLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalLastInputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcIntervalLowInputPower_Type = Integer32
_OptIfOTSnSrcIntervalLowInputPower_Object = MibTableColumn
optIfOTSnSrcIntervalLowInputPower = _OptIfOTSnSrcIntervalLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 7, 1, 7),
    _OptIfOTSnSrcIntervalLowInputPower_Type()
)
optIfOTSnSrcIntervalLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalLowInputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcIntervalHighInputPower_Type = Integer32
_OptIfOTSnSrcIntervalHighInputPower_Object = MibTableColumn
optIfOTSnSrcIntervalHighInputPower = _OptIfOTSnSrcIntervalHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 7, 1, 8),
    _OptIfOTSnSrcIntervalHighInputPower_Type()
)
optIfOTSnSrcIntervalHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcIntervalHighInputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurDayTable_Object = MibTable
optIfOTSnSrcCurDayTable = _OptIfOTSnSrcCurDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 8)
)
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDayTable.setStatus("current")
_OptIfOTSnSrcCurDayEntry_Object = MibTableRow
optIfOTSnSrcCurDayEntry = _OptIfOTSnSrcCurDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 8, 1)
)
optIfOTSnSrcCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDayEntry.setStatus("current")
_OptIfOTSnSrcCurDaySuspectedFlag_Type = TruthValue
_OptIfOTSnSrcCurDaySuspectedFlag_Object = MibTableColumn
optIfOTSnSrcCurDaySuspectedFlag = _OptIfOTSnSrcCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 8, 1, 1),
    _OptIfOTSnSrcCurDaySuspectedFlag_Type()
)
optIfOTSnSrcCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDaySuspectedFlag.setStatus("current")
_OptIfOTSnSrcCurDayLowOutputPower_Type = Integer32
_OptIfOTSnSrcCurDayLowOutputPower_Object = MibTableColumn
optIfOTSnSrcCurDayLowOutputPower = _OptIfOTSnSrcCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 8, 1, 2),
    _OptIfOTSnSrcCurDayLowOutputPower_Type()
)
optIfOTSnSrcCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurDayHighOutputPower_Type = Integer32
_OptIfOTSnSrcCurDayHighOutputPower_Object = MibTableColumn
optIfOTSnSrcCurDayHighOutputPower = _OptIfOTSnSrcCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 8, 1, 3),
    _OptIfOTSnSrcCurDayHighOutputPower_Type()
)
optIfOTSnSrcCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurDayLowInputPower_Type = Integer32
_OptIfOTSnSrcCurDayLowInputPower_Object = MibTableColumn
optIfOTSnSrcCurDayLowInputPower = _OptIfOTSnSrcCurDayLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 8, 1, 4),
    _OptIfOTSnSrcCurDayLowInputPower_Type()
)
optIfOTSnSrcCurDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDayLowInputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcCurDayHighInputPower_Type = Integer32
_OptIfOTSnSrcCurDayHighInputPower_Object = MibTableColumn
optIfOTSnSrcCurDayHighInputPower = _OptIfOTSnSrcCurDayHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 8, 1, 5),
    _OptIfOTSnSrcCurDayHighInputPower_Type()
)
optIfOTSnSrcCurDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcCurDayHighInputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcPrevDayTable_Object = MibTable
optIfOTSnSrcPrevDayTable = _OptIfOTSnSrcPrevDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 9)
)
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayTable.setStatus("current")
_OptIfOTSnSrcPrevDayEntry_Object = MibTableRow
optIfOTSnSrcPrevDayEntry = _OptIfOTSnSrcPrevDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 9, 1)
)
optIfOTSnSrcPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayEntry.setStatus("current")
_OptIfOTSnSrcPrevDaySuspectedFlag_Type = TruthValue
_OptIfOTSnSrcPrevDaySuspectedFlag_Object = MibTableColumn
optIfOTSnSrcPrevDaySuspectedFlag = _OptIfOTSnSrcPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 9, 1, 1),
    _OptIfOTSnSrcPrevDaySuspectedFlag_Type()
)
optIfOTSnSrcPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDaySuspectedFlag.setStatus("current")
_OptIfOTSnSrcPrevDayLastOutputPower_Type = Integer32
_OptIfOTSnSrcPrevDayLastOutputPower_Object = MibTableColumn
optIfOTSnSrcPrevDayLastOutputPower = _OptIfOTSnSrcPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 9, 1, 2),
    _OptIfOTSnSrcPrevDayLastOutputPower_Type()
)
optIfOTSnSrcPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayLastOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcPrevDayLowOutputPower_Type = Integer32
_OptIfOTSnSrcPrevDayLowOutputPower_Object = MibTableColumn
optIfOTSnSrcPrevDayLowOutputPower = _OptIfOTSnSrcPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 9, 1, 3),
    _OptIfOTSnSrcPrevDayLowOutputPower_Type()
)
optIfOTSnSrcPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcPrevDayHighOutputPower_Type = Integer32
_OptIfOTSnSrcPrevDayHighOutputPower_Object = MibTableColumn
optIfOTSnSrcPrevDayHighOutputPower = _OptIfOTSnSrcPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 9, 1, 4),
    _OptIfOTSnSrcPrevDayHighOutputPower_Type()
)
optIfOTSnSrcPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcPrevDayLastInputPower_Type = Integer32
_OptIfOTSnSrcPrevDayLastInputPower_Object = MibTableColumn
optIfOTSnSrcPrevDayLastInputPower = _OptIfOTSnSrcPrevDayLastInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 9, 1, 5),
    _OptIfOTSnSrcPrevDayLastInputPower_Type()
)
optIfOTSnSrcPrevDayLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayLastInputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcPrevDayLowInputPower_Type = Integer32
_OptIfOTSnSrcPrevDayLowInputPower_Object = MibTableColumn
optIfOTSnSrcPrevDayLowInputPower = _OptIfOTSnSrcPrevDayLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 9, 1, 6),
    _OptIfOTSnSrcPrevDayLowInputPower_Type()
)
optIfOTSnSrcPrevDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayLowInputPower.setUnits("0.1 dbm")
_OptIfOTSnSrcPrevDayHighInputPower_Type = Integer32
_OptIfOTSnSrcPrevDayHighInputPower_Object = MibTableColumn
optIfOTSnSrcPrevDayHighInputPower = _OptIfOTSnSrcPrevDayHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 3, 9, 1, 7),
    _OptIfOTSnSrcPrevDayHighInputPower_Type()
)
optIfOTSnSrcPrevDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTSnSrcPrevDayHighInputPower.setUnits("0.1 dbm")
_OptIfOMSn_ObjectIdentity = ObjectIdentity
optIfOMSn = _OptIfOMSn_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4)
)
_OptIfOMSnConfigTable_Object = MibTable
optIfOMSnConfigTable = _OptIfOMSnConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 1)
)
if mibBuilder.loadTexts:
    optIfOMSnConfigTable.setStatus("current")
_OptIfOMSnConfigEntry_Object = MibTableRow
optIfOMSnConfigEntry = _OptIfOMSnConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 1, 1)
)
optIfOMSnConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOMSnConfigEntry.setStatus("current")
_OptIfOMSnDirectionality_Type = OptIfDirectionality
_OptIfOMSnDirectionality_Object = MibTableColumn
optIfOMSnDirectionality = _OptIfOMSnDirectionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 1, 1, 1),
    _OptIfOMSnDirectionality_Type()
)
optIfOMSnDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnDirectionality.setStatus("current")


class _OptIfOMSnCurrentStatus_Type(Bits):
    """Custom type optIfOMSnCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 5),
          ("bdiO", 4),
          ("bdiP", 3),
          ("losP", 6),
          ("ssf", 2),
          ("ssfO", 1),
          ("ssfP", 0))
    )

_OptIfOMSnCurrentStatus_Type.__name__ = "Bits"
_OptIfOMSnCurrentStatus_Object = MibTableColumn
optIfOMSnCurrentStatus = _OptIfOMSnCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 1, 1, 2),
    _OptIfOMSnCurrentStatus_Type()
)
optIfOMSnCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnCurrentStatus.setStatus("current")
_OptIfOMSnSinkCurrentTable_Object = MibTable
optIfOMSnSinkCurrentTable = _OptIfOMSnSinkCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2)
)
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentTable.setStatus("current")
_OptIfOMSnSinkCurrentEntry_Object = MibTableRow
optIfOMSnSinkCurrentEntry = _OptIfOMSnSinkCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1)
)
optIfOMSnSinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentEntry.setStatus("current")
_OptIfOMSnSinkCurrentSuspectedFlag_Type = TruthValue
_OptIfOMSnSinkCurrentSuspectedFlag_Object = MibTableColumn
optIfOMSnSinkCurrentSuspectedFlag = _OptIfOMSnSinkCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 1),
    _OptIfOMSnSinkCurrentSuspectedFlag_Type()
)
optIfOMSnSinkCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentSuspectedFlag.setStatus("current")
_OptIfOMSnSinkCurrentAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkCurrentAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkCurrentAggregatedInputPower = _OptIfOMSnSinkCurrentAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 2),
    _OptIfOMSnSinkCurrentAggregatedInputPower_Type()
)
optIfOMSnSinkCurrentAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkCurrentLowAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkCurrentLowAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkCurrentLowAggregatedInputPower = _OptIfOMSnSinkCurrentLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 3),
    _OptIfOMSnSinkCurrentLowAggregatedInputPower_Type()
)
optIfOMSnSinkCurrentLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkCurrentHighAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkCurrentHighAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkCurrentHighAggregatedInputPower = _OptIfOMSnSinkCurrentHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 4),
    _OptIfOMSnSinkCurrentHighAggregatedInputPower_Type()
)
optIfOMSnSinkCurrentHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkCurrentLowerInputPowerThreshold_Type = Integer32
_OptIfOMSnSinkCurrentLowerInputPowerThreshold_Object = MibTableColumn
optIfOMSnSinkCurrentLowerInputPowerThreshold = _OptIfOMSnSinkCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 5),
    _OptIfOMSnSinkCurrentLowerInputPowerThreshold_Type()
)
optIfOMSnSinkCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOMSnSinkCurrentUpperInputPowerThreshold_Type = Integer32
_OptIfOMSnSinkCurrentUpperInputPowerThreshold_Object = MibTableColumn
optIfOMSnSinkCurrentUpperInputPowerThreshold = _OptIfOMSnSinkCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 6),
    _OptIfOMSnSinkCurrentUpperInputPowerThreshold_Type()
)
optIfOMSnSinkCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOMSnSinkCurrentOutputPower_Type = Integer32
_OptIfOMSnSinkCurrentOutputPower_Object = MibTableColumn
optIfOMSnSinkCurrentOutputPower = _OptIfOMSnSinkCurrentOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 7),
    _OptIfOMSnSinkCurrentOutputPower_Type()
)
optIfOMSnSinkCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkCurrentLowOutputPower_Type = Integer32
_OptIfOMSnSinkCurrentLowOutputPower_Object = MibTableColumn
optIfOMSnSinkCurrentLowOutputPower = _OptIfOMSnSinkCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 8),
    _OptIfOMSnSinkCurrentLowOutputPower_Type()
)
optIfOMSnSinkCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentLowOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkCurrentHighOutputPower_Type = Integer32
_OptIfOMSnSinkCurrentHighOutputPower_Object = MibTableColumn
optIfOMSnSinkCurrentHighOutputPower = _OptIfOMSnSinkCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 9),
    _OptIfOMSnSinkCurrentHighOutputPower_Type()
)
optIfOMSnSinkCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentHighOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkCurrentLowerOutputPowerThreshold_Type = Integer32
_OptIfOMSnSinkCurrentLowerOutputPowerThreshold_Object = MibTableColumn
optIfOMSnSinkCurrentLowerOutputPowerThreshold = _OptIfOMSnSinkCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 10),
    _OptIfOMSnSinkCurrentLowerOutputPowerThreshold_Type()
)
optIfOMSnSinkCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOMSnSinkCurrentUpperOutputPowerThreshold_Type = Integer32
_OptIfOMSnSinkCurrentUpperOutputPowerThreshold_Object = MibTableColumn
optIfOMSnSinkCurrentUpperOutputPowerThreshold = _OptIfOMSnSinkCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 2, 1, 11),
    _OptIfOMSnSinkCurrentUpperOutputPowerThreshold_Type()
)
optIfOMSnSinkCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOMSnSinkIntervalTable_Object = MibTable
optIfOMSnSinkIntervalTable = _OptIfOMSnSinkIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 3)
)
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalTable.setStatus("current")
_OptIfOMSnSinkIntervalEntry_Object = MibTableRow
optIfOMSnSinkIntervalEntry = _OptIfOMSnSinkIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 3, 1)
)
optIfOMSnSinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfOMSnSinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalEntry.setStatus("current")
_OptIfOMSnSinkIntervalNumber_Type = OptIfIntervalNumber
_OptIfOMSnSinkIntervalNumber_Object = MibTableColumn
optIfOMSnSinkIntervalNumber = _OptIfOMSnSinkIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 3, 1, 1),
    _OptIfOMSnSinkIntervalNumber_Type()
)
optIfOMSnSinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalNumber.setStatus("current")
_OptIfOMSnSinkIntervalSuspectedFlag_Type = TruthValue
_OptIfOMSnSinkIntervalSuspectedFlag_Object = MibTableColumn
optIfOMSnSinkIntervalSuspectedFlag = _OptIfOMSnSinkIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 3, 1, 2),
    _OptIfOMSnSinkIntervalSuspectedFlag_Type()
)
optIfOMSnSinkIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalSuspectedFlag.setStatus("current")
_OptIfOMSnSinkIntervalLastAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkIntervalLastAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkIntervalLastAggregatedInputPower = _OptIfOMSnSinkIntervalLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 3, 1, 3),
    _OptIfOMSnSinkIntervalLastAggregatedInputPower_Type()
)
optIfOMSnSinkIntervalLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalLastAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkIntervalLowAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkIntervalLowAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkIntervalLowAggregatedInputPower = _OptIfOMSnSinkIntervalLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 3, 1, 4),
    _OptIfOMSnSinkIntervalLowAggregatedInputPower_Type()
)
optIfOMSnSinkIntervalLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkIntervalHighAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkIntervalHighAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkIntervalHighAggregatedInputPower = _OptIfOMSnSinkIntervalHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 3, 1, 5),
    _OptIfOMSnSinkIntervalHighAggregatedInputPower_Type()
)
optIfOMSnSinkIntervalHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkIntervalLastOutputPower_Type = Integer32
_OptIfOMSnSinkIntervalLastOutputPower_Object = MibTableColumn
optIfOMSnSinkIntervalLastOutputPower = _OptIfOMSnSinkIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 3, 1, 6),
    _OptIfOMSnSinkIntervalLastOutputPower_Type()
)
optIfOMSnSinkIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalLastOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkIntervalLowOutputPower_Type = Integer32
_OptIfOMSnSinkIntervalLowOutputPower_Object = MibTableColumn
optIfOMSnSinkIntervalLowOutputPower = _OptIfOMSnSinkIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 3, 1, 7),
    _OptIfOMSnSinkIntervalLowOutputPower_Type()
)
optIfOMSnSinkIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalLowOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkIntervalHighOutputPower_Type = Integer32
_OptIfOMSnSinkIntervalHighOutputPower_Object = MibTableColumn
optIfOMSnSinkIntervalHighOutputPower = _OptIfOMSnSinkIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 3, 1, 8),
    _OptIfOMSnSinkIntervalHighOutputPower_Type()
)
optIfOMSnSinkIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkIntervalHighOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkCurDayTable_Object = MibTable
optIfOMSnSinkCurDayTable = _OptIfOMSnSinkCurDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 4)
)
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDayTable.setStatus("current")
_OptIfOMSnSinkCurDayEntry_Object = MibTableRow
optIfOMSnSinkCurDayEntry = _OptIfOMSnSinkCurDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 4, 1)
)
optIfOMSnSinkCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDayEntry.setStatus("current")
_OptIfOMSnSinkCurDaySuspectedFlag_Type = TruthValue
_OptIfOMSnSinkCurDaySuspectedFlag_Object = MibTableColumn
optIfOMSnSinkCurDaySuspectedFlag = _OptIfOMSnSinkCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 4, 1, 1),
    _OptIfOMSnSinkCurDaySuspectedFlag_Type()
)
optIfOMSnSinkCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDaySuspectedFlag.setStatus("current")
_OptIfOMSnSinkCurDayLowAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkCurDayLowAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkCurDayLowAggregatedInputPower = _OptIfOMSnSinkCurDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 4, 1, 2),
    _OptIfOMSnSinkCurDayLowAggregatedInputPower_Type()
)
optIfOMSnSinkCurDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDayLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkCurDayHighAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkCurDayHighAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkCurDayHighAggregatedInputPower = _OptIfOMSnSinkCurDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 4, 1, 3),
    _OptIfOMSnSinkCurDayHighAggregatedInputPower_Type()
)
optIfOMSnSinkCurDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDayHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkCurDayLowOutputPower_Type = Integer32
_OptIfOMSnSinkCurDayLowOutputPower_Object = MibTableColumn
optIfOMSnSinkCurDayLowOutputPower = _OptIfOMSnSinkCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 4, 1, 4),
    _OptIfOMSnSinkCurDayLowOutputPower_Type()
)
optIfOMSnSinkCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkCurDayHighOutputPower_Type = Integer32
_OptIfOMSnSinkCurDayHighOutputPower_Object = MibTableColumn
optIfOMSnSinkCurDayHighOutputPower = _OptIfOMSnSinkCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 4, 1, 5),
    _OptIfOMSnSinkCurDayHighOutputPower_Type()
)
optIfOMSnSinkCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkCurDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkPrevDayTable_Object = MibTable
optIfOMSnSinkPrevDayTable = _OptIfOMSnSinkPrevDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 5)
)
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayTable.setStatus("current")
_OptIfOMSnSinkPrevDayEntry_Object = MibTableRow
optIfOMSnSinkPrevDayEntry = _OptIfOMSnSinkPrevDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 5, 1)
)
optIfOMSnSinkPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayEntry.setStatus("current")
_OptIfOMSnSinkPrevDaySuspectedFlag_Type = TruthValue
_OptIfOMSnSinkPrevDaySuspectedFlag_Object = MibTableColumn
optIfOMSnSinkPrevDaySuspectedFlag = _OptIfOMSnSinkPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 5, 1, 1),
    _OptIfOMSnSinkPrevDaySuspectedFlag_Type()
)
optIfOMSnSinkPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDaySuspectedFlag.setStatus("current")
_OptIfOMSnSinkPrevDayLastAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkPrevDayLastAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkPrevDayLastAggregatedInputPower = _OptIfOMSnSinkPrevDayLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 5, 1, 2),
    _OptIfOMSnSinkPrevDayLastAggregatedInputPower_Type()
)
optIfOMSnSinkPrevDayLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayLastAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkPrevDayLowAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkPrevDayLowAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkPrevDayLowAggregatedInputPower = _OptIfOMSnSinkPrevDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 5, 1, 3),
    _OptIfOMSnSinkPrevDayLowAggregatedInputPower_Type()
)
optIfOMSnSinkPrevDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkPrevDayHighAggregatedInputPower_Type = Integer32
_OptIfOMSnSinkPrevDayHighAggregatedInputPower_Object = MibTableColumn
optIfOMSnSinkPrevDayHighAggregatedInputPower = _OptIfOMSnSinkPrevDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 5, 1, 4),
    _OptIfOMSnSinkPrevDayHighAggregatedInputPower_Type()
)
optIfOMSnSinkPrevDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkPrevDayLastOutputPower_Type = Integer32
_OptIfOMSnSinkPrevDayLastOutputPower_Object = MibTableColumn
optIfOMSnSinkPrevDayLastOutputPower = _OptIfOMSnSinkPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 5, 1, 5),
    _OptIfOMSnSinkPrevDayLastOutputPower_Type()
)
optIfOMSnSinkPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayLastOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkPrevDayLowOutputPower_Type = Integer32
_OptIfOMSnSinkPrevDayLowOutputPower_Object = MibTableColumn
optIfOMSnSinkPrevDayLowOutputPower = _OptIfOMSnSinkPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 5, 1, 6),
    _OptIfOMSnSinkPrevDayLowOutputPower_Type()
)
optIfOMSnSinkPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSinkPrevDayHighOutputPower_Type = Integer32
_OptIfOMSnSinkPrevDayHighOutputPower_Object = MibTableColumn
optIfOMSnSinkPrevDayHighOutputPower = _OptIfOMSnSinkPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 5, 1, 7),
    _OptIfOMSnSinkPrevDayHighOutputPower_Type()
)
optIfOMSnSinkPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSinkPrevDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurrentTable_Object = MibTable
optIfOMSnSrcCurrentTable = _OptIfOMSnSrcCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6)
)
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentTable.setStatus("current")
_OptIfOMSnSrcCurrentEntry_Object = MibTableRow
optIfOMSnSrcCurrentEntry = _OptIfOMSnSrcCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1)
)
optIfOMSnSrcCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentEntry.setStatus("current")
_OptIfOMSnSrcCurrentSuspectedFlag_Type = TruthValue
_OptIfOMSnSrcCurrentSuspectedFlag_Object = MibTableColumn
optIfOMSnSrcCurrentSuspectedFlag = _OptIfOMSnSrcCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 1),
    _OptIfOMSnSrcCurrentSuspectedFlag_Type()
)
optIfOMSnSrcCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentSuspectedFlag.setStatus("current")
_OptIfOMSnSrcCurrentOutputPower_Type = Integer32
_OptIfOMSnSrcCurrentOutputPower_Object = MibTableColumn
optIfOMSnSrcCurrentOutputPower = _OptIfOMSnSrcCurrentOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 2),
    _OptIfOMSnSrcCurrentOutputPower_Type()
)
optIfOMSnSrcCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurrentLowOutputPower_Type = Integer32
_OptIfOMSnSrcCurrentLowOutputPower_Object = MibTableColumn
optIfOMSnSrcCurrentLowOutputPower = _OptIfOMSnSrcCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 3),
    _OptIfOMSnSrcCurrentLowOutputPower_Type()
)
optIfOMSnSrcCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentLowOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurrentHighOutputPower_Type = Integer32
_OptIfOMSnSrcCurrentHighOutputPower_Object = MibTableColumn
optIfOMSnSrcCurrentHighOutputPower = _OptIfOMSnSrcCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 4),
    _OptIfOMSnSrcCurrentHighOutputPower_Type()
)
optIfOMSnSrcCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentHighOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurrentLowerOutputPowerThreshold_Type = Integer32
_OptIfOMSnSrcCurrentLowerOutputPowerThreshold_Object = MibTableColumn
optIfOMSnSrcCurrentLowerOutputPowerThreshold = _OptIfOMSnSrcCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 5),
    _OptIfOMSnSrcCurrentLowerOutputPowerThreshold_Type()
)
optIfOMSnSrcCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOMSnSrcCurrentUpperOutputPowerThreshold_Type = Integer32
_OptIfOMSnSrcCurrentUpperOutputPowerThreshold_Object = MibTableColumn
optIfOMSnSrcCurrentUpperOutputPowerThreshold = _OptIfOMSnSrcCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 6),
    _OptIfOMSnSrcCurrentUpperOutputPowerThreshold_Type()
)
optIfOMSnSrcCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOMSnSrcCurrentAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcCurrentAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcCurrentAggregatedInputPower = _OptIfOMSnSrcCurrentAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 7),
    _OptIfOMSnSrcCurrentAggregatedInputPower_Type()
)
optIfOMSnSrcCurrentAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurrentLowAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcCurrentLowAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcCurrentLowAggregatedInputPower = _OptIfOMSnSrcCurrentLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 8),
    _OptIfOMSnSrcCurrentLowAggregatedInputPower_Type()
)
optIfOMSnSrcCurrentLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurrentHighAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcCurrentHighAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcCurrentHighAggregatedInputPower = _OptIfOMSnSrcCurrentHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 9),
    _OptIfOMSnSrcCurrentHighAggregatedInputPower_Type()
)
optIfOMSnSrcCurrentHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurrentLowerInputPowerThreshold_Type = Integer32
_OptIfOMSnSrcCurrentLowerInputPowerThreshold_Object = MibTableColumn
optIfOMSnSrcCurrentLowerInputPowerThreshold = _OptIfOMSnSrcCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 10),
    _OptIfOMSnSrcCurrentLowerInputPowerThreshold_Type()
)
optIfOMSnSrcCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOMSnSrcCurrentUpperInputPowerThreshold_Type = Integer32
_OptIfOMSnSrcCurrentUpperInputPowerThreshold_Object = MibTableColumn
optIfOMSnSrcCurrentUpperInputPowerThreshold = _OptIfOMSnSrcCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 6, 1, 11),
    _OptIfOMSnSrcCurrentUpperInputPowerThreshold_Type()
)
optIfOMSnSrcCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOMSnSrcIntervalTable_Object = MibTable
optIfOMSnSrcIntervalTable = _OptIfOMSnSrcIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 7)
)
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalTable.setStatus("current")
_OptIfOMSnSrcIntervalEntry_Object = MibTableRow
optIfOMSnSrcIntervalEntry = _OptIfOMSnSrcIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 7, 1)
)
optIfOMSnSrcIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfOMSnSrcIntervalNumber"),
)
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalEntry.setStatus("current")
_OptIfOMSnSrcIntervalNumber_Type = OptIfIntervalNumber
_OptIfOMSnSrcIntervalNumber_Object = MibTableColumn
optIfOMSnSrcIntervalNumber = _OptIfOMSnSrcIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 7, 1, 1),
    _OptIfOMSnSrcIntervalNumber_Type()
)
optIfOMSnSrcIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalNumber.setStatus("current")
_OptIfOMSnSrcIntervalSuspectedFlag_Type = TruthValue
_OptIfOMSnSrcIntervalSuspectedFlag_Object = MibTableColumn
optIfOMSnSrcIntervalSuspectedFlag = _OptIfOMSnSrcIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 7, 1, 2),
    _OptIfOMSnSrcIntervalSuspectedFlag_Type()
)
optIfOMSnSrcIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalSuspectedFlag.setStatus("current")
_OptIfOMSnSrcIntervalLastOutputPower_Type = Integer32
_OptIfOMSnSrcIntervalLastOutputPower_Object = MibTableColumn
optIfOMSnSrcIntervalLastOutputPower = _OptIfOMSnSrcIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 7, 1, 3),
    _OptIfOMSnSrcIntervalLastOutputPower_Type()
)
optIfOMSnSrcIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalLastOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcIntervalLowOutputPower_Type = Integer32
_OptIfOMSnSrcIntervalLowOutputPower_Object = MibTableColumn
optIfOMSnSrcIntervalLowOutputPower = _OptIfOMSnSrcIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 7, 1, 4),
    _OptIfOMSnSrcIntervalLowOutputPower_Type()
)
optIfOMSnSrcIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalLowOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcIntervalHighOutputPower_Type = Integer32
_OptIfOMSnSrcIntervalHighOutputPower_Object = MibTableColumn
optIfOMSnSrcIntervalHighOutputPower = _OptIfOMSnSrcIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 7, 1, 5),
    _OptIfOMSnSrcIntervalHighOutputPower_Type()
)
optIfOMSnSrcIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalHighOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcIntervalLastAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcIntervalLastAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcIntervalLastAggregatedInputPower = _OptIfOMSnSrcIntervalLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 7, 1, 6),
    _OptIfOMSnSrcIntervalLastAggregatedInputPower_Type()
)
optIfOMSnSrcIntervalLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalLastAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcIntervalLowAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcIntervalLowAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcIntervalLowAggregatedInputPower = _OptIfOMSnSrcIntervalLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 7, 1, 7),
    _OptIfOMSnSrcIntervalLowAggregatedInputPower_Type()
)
optIfOMSnSrcIntervalLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcIntervalHighAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcIntervalHighAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcIntervalHighAggregatedInputPower = _OptIfOMSnSrcIntervalHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 7, 1, 8),
    _OptIfOMSnSrcIntervalHighAggregatedInputPower_Type()
)
optIfOMSnSrcIntervalHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcIntervalHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurDayTable_Object = MibTable
optIfOMSnSrcCurDayTable = _OptIfOMSnSrcCurDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 8)
)
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDayTable.setStatus("current")
_OptIfOMSnSrcCurDayEntry_Object = MibTableRow
optIfOMSnSrcCurDayEntry = _OptIfOMSnSrcCurDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 8, 1)
)
optIfOMSnSrcCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDayEntry.setStatus("current")
_OptIfOMSnSrcCurDaySuspectedFlag_Type = TruthValue
_OptIfOMSnSrcCurDaySuspectedFlag_Object = MibTableColumn
optIfOMSnSrcCurDaySuspectedFlag = _OptIfOMSnSrcCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 8, 1, 1),
    _OptIfOMSnSrcCurDaySuspectedFlag_Type()
)
optIfOMSnSrcCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDaySuspectedFlag.setStatus("current")
_OptIfOMSnSrcCurDayLowOutputPower_Type = Integer32
_OptIfOMSnSrcCurDayLowOutputPower_Object = MibTableColumn
optIfOMSnSrcCurDayLowOutputPower = _OptIfOMSnSrcCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 8, 1, 2),
    _OptIfOMSnSrcCurDayLowOutputPower_Type()
)
optIfOMSnSrcCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurDayHighOutputPower_Type = Integer32
_OptIfOMSnSrcCurDayHighOutputPower_Object = MibTableColumn
optIfOMSnSrcCurDayHighOutputPower = _OptIfOMSnSrcCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 8, 1, 3),
    _OptIfOMSnSrcCurDayHighOutputPower_Type()
)
optIfOMSnSrcCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurDayLowAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcCurDayLowAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcCurDayLowAggregatedInputPower = _OptIfOMSnSrcCurDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 8, 1, 4),
    _OptIfOMSnSrcCurDayLowAggregatedInputPower_Type()
)
optIfOMSnSrcCurDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDayLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcCurDayHighAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcCurDayHighAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcCurDayHighAggregatedInputPower = _OptIfOMSnSrcCurDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 8, 1, 5),
    _OptIfOMSnSrcCurDayHighAggregatedInputPower_Type()
)
optIfOMSnSrcCurDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcCurDayHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcPrevDayTable_Object = MibTable
optIfOMSnSrcPrevDayTable = _OptIfOMSnSrcPrevDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 9)
)
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayTable.setStatus("current")
_OptIfOMSnSrcPrevDayEntry_Object = MibTableRow
optIfOMSnSrcPrevDayEntry = _OptIfOMSnSrcPrevDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 9, 1)
)
optIfOMSnSrcPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayEntry.setStatus("current")
_OptIfOMSnSrcPrevDaySuspectedFlag_Type = TruthValue
_OptIfOMSnSrcPrevDaySuspectedFlag_Object = MibTableColumn
optIfOMSnSrcPrevDaySuspectedFlag = _OptIfOMSnSrcPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 9, 1, 1),
    _OptIfOMSnSrcPrevDaySuspectedFlag_Type()
)
optIfOMSnSrcPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDaySuspectedFlag.setStatus("current")
_OptIfOMSnSrcPrevDayLastOutputPower_Type = Integer32
_OptIfOMSnSrcPrevDayLastOutputPower_Object = MibTableColumn
optIfOMSnSrcPrevDayLastOutputPower = _OptIfOMSnSrcPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 9, 1, 2),
    _OptIfOMSnSrcPrevDayLastOutputPower_Type()
)
optIfOMSnSrcPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayLastOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcPrevDayLowOutputPower_Type = Integer32
_OptIfOMSnSrcPrevDayLowOutputPower_Object = MibTableColumn
optIfOMSnSrcPrevDayLowOutputPower = _OptIfOMSnSrcPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 9, 1, 3),
    _OptIfOMSnSrcPrevDayLowOutputPower_Type()
)
optIfOMSnSrcPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcPrevDayHighOutputPower_Type = Integer32
_OptIfOMSnSrcPrevDayHighOutputPower_Object = MibTableColumn
optIfOMSnSrcPrevDayHighOutputPower = _OptIfOMSnSrcPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 9, 1, 4),
    _OptIfOMSnSrcPrevDayHighOutputPower_Type()
)
optIfOMSnSrcPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcPrevDayLastAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcPrevDayLastAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcPrevDayLastAggregatedInputPower = _OptIfOMSnSrcPrevDayLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 9, 1, 5),
    _OptIfOMSnSrcPrevDayLastAggregatedInputPower_Type()
)
optIfOMSnSrcPrevDayLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayLastAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcPrevDayLowAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcPrevDayLowAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcPrevDayLowAggregatedInputPower = _OptIfOMSnSrcPrevDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 9, 1, 6),
    _OptIfOMSnSrcPrevDayLowAggregatedInputPower_Type()
)
optIfOMSnSrcPrevDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOMSnSrcPrevDayHighAggregatedInputPower_Type = Integer32
_OptIfOMSnSrcPrevDayHighAggregatedInputPower_Object = MibTableColumn
optIfOMSnSrcPrevDayHighAggregatedInputPower = _OptIfOMSnSrcPrevDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 4, 9, 1, 7),
    _OptIfOMSnSrcPrevDayHighAggregatedInputPower_Type()
)
optIfOMSnSrcPrevDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOMSnSrcPrevDayHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroup_ObjectIdentity = ObjectIdentity
optIfOChGroup = _OptIfOChGroup_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5)
)
_OptIfOChGroupConfigTable_Object = MibTable
optIfOChGroupConfigTable = _OptIfOChGroupConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 1)
)
if mibBuilder.loadTexts:
    optIfOChGroupConfigTable.setStatus("current")
_OptIfOChGroupConfigEntry_Object = MibTableRow
optIfOChGroupConfigEntry = _OptIfOChGroupConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 1, 1)
)
optIfOChGroupConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChGroupConfigEntry.setStatus("current")
_OptIfOChGroupDirectionality_Type = OptIfDirectionality
_OptIfOChGroupDirectionality_Object = MibTableColumn
optIfOChGroupDirectionality = _OptIfOChGroupDirectionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 1, 1, 1),
    _OptIfOChGroupDirectionality_Type()
)
optIfOChGroupDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupDirectionality.setStatus("current")
_OptIfOChGroupSinkCurrentTable_Object = MibTable
optIfOChGroupSinkCurrentTable = _OptIfOChGroupSinkCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2)
)
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentTable.setStatus("current")
_OptIfOChGroupSinkCurrentEntry_Object = MibTableRow
optIfOChGroupSinkCurrentEntry = _OptIfOChGroupSinkCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1)
)
optIfOChGroupSinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentEntry.setStatus("current")
_OptIfOChGroupSinkCurrentSuspectedFlag_Type = TruthValue
_OptIfOChGroupSinkCurrentSuspectedFlag_Object = MibTableColumn
optIfOChGroupSinkCurrentSuspectedFlag = _OptIfOChGroupSinkCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 1),
    _OptIfOChGroupSinkCurrentSuspectedFlag_Type()
)
optIfOChGroupSinkCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentSuspectedFlag.setStatus("current")
_OptIfOChGroupSinkCurrentAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkCurrentAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkCurrentAggregatedInputPower = _OptIfOChGroupSinkCurrentAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 2),
    _OptIfOChGroupSinkCurrentAggregatedInputPower_Type()
)
optIfOChGroupSinkCurrentAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurrentLowAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkCurrentLowAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkCurrentLowAggregatedInputPower = _OptIfOChGroupSinkCurrentLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 3),
    _OptIfOChGroupSinkCurrentLowAggregatedInputPower_Type()
)
optIfOChGroupSinkCurrentLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurrentHighAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkCurrentHighAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkCurrentHighAggregatedInputPower = _OptIfOChGroupSinkCurrentHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 4),
    _OptIfOChGroupSinkCurrentHighAggregatedInputPower_Type()
)
optIfOChGroupSinkCurrentHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurrentLowerInputPowerThreshold_Type = Integer32
_OptIfOChGroupSinkCurrentLowerInputPowerThreshold_Object = MibTableColumn
optIfOChGroupSinkCurrentLowerInputPowerThreshold = _OptIfOChGroupSinkCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 5),
    _OptIfOChGroupSinkCurrentLowerInputPowerThreshold_Type()
)
optIfOChGroupSinkCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurrentUpperInputPowerThreshold_Type = Integer32
_OptIfOChGroupSinkCurrentUpperInputPowerThreshold_Object = MibTableColumn
optIfOChGroupSinkCurrentUpperInputPowerThreshold = _OptIfOChGroupSinkCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 6),
    _OptIfOChGroupSinkCurrentUpperInputPowerThreshold_Type()
)
optIfOChGroupSinkCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurrentOutputPower_Type = Integer32
_OptIfOChGroupSinkCurrentOutputPower_Object = MibTableColumn
optIfOChGroupSinkCurrentOutputPower = _OptIfOChGroupSinkCurrentOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 7),
    _OptIfOChGroupSinkCurrentOutputPower_Type()
)
optIfOChGroupSinkCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurrentLowOutputPower_Type = Integer32
_OptIfOChGroupSinkCurrentLowOutputPower_Object = MibTableColumn
optIfOChGroupSinkCurrentLowOutputPower = _OptIfOChGroupSinkCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 8),
    _OptIfOChGroupSinkCurrentLowOutputPower_Type()
)
optIfOChGroupSinkCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentLowOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurrentHighOutputPower_Type = Integer32
_OptIfOChGroupSinkCurrentHighOutputPower_Object = MibTableColumn
optIfOChGroupSinkCurrentHighOutputPower = _OptIfOChGroupSinkCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 9),
    _OptIfOChGroupSinkCurrentHighOutputPower_Type()
)
optIfOChGroupSinkCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentHighOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurrentLowerOutputPowerThreshold_Type = Integer32
_OptIfOChGroupSinkCurrentLowerOutputPowerThreshold_Object = MibTableColumn
optIfOChGroupSinkCurrentLowerOutputPowerThreshold = _OptIfOChGroupSinkCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 10),
    _OptIfOChGroupSinkCurrentLowerOutputPowerThreshold_Type()
)
optIfOChGroupSinkCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurrentUpperOutputPowerThreshold_Type = Integer32
_OptIfOChGroupSinkCurrentUpperOutputPowerThreshold_Object = MibTableColumn
optIfOChGroupSinkCurrentUpperOutputPowerThreshold = _OptIfOChGroupSinkCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 2, 1, 11),
    _OptIfOChGroupSinkCurrentUpperOutputPowerThreshold_Type()
)
optIfOChGroupSinkCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChGroupSinkIntervalTable_Object = MibTable
optIfOChGroupSinkIntervalTable = _OptIfOChGroupSinkIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 3)
)
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalTable.setStatus("current")
_OptIfOChGroupSinkIntervalEntry_Object = MibTableRow
optIfOChGroupSinkIntervalEntry = _OptIfOChGroupSinkIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 3, 1)
)
optIfOChGroupSinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfOChGroupSinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalEntry.setStatus("current")
_OptIfOChGroupSinkIntervalNumber_Type = OptIfIntervalNumber
_OptIfOChGroupSinkIntervalNumber_Object = MibTableColumn
optIfOChGroupSinkIntervalNumber = _OptIfOChGroupSinkIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 3, 1, 1),
    _OptIfOChGroupSinkIntervalNumber_Type()
)
optIfOChGroupSinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalNumber.setStatus("current")
_OptIfOChGroupSinkIntervalSuspectedFlag_Type = TruthValue
_OptIfOChGroupSinkIntervalSuspectedFlag_Object = MibTableColumn
optIfOChGroupSinkIntervalSuspectedFlag = _OptIfOChGroupSinkIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 3, 1, 2),
    _OptIfOChGroupSinkIntervalSuspectedFlag_Type()
)
optIfOChGroupSinkIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalSuspectedFlag.setStatus("current")
_OptIfOChGroupSinkIntervalLastAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkIntervalLastAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkIntervalLastAggregatedInputPower = _OptIfOChGroupSinkIntervalLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 3, 1, 3),
    _OptIfOChGroupSinkIntervalLastAggregatedInputPower_Type()
)
optIfOChGroupSinkIntervalLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalLastAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkIntervalLowAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkIntervalLowAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkIntervalLowAggregatedInputPower = _OptIfOChGroupSinkIntervalLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 3, 1, 4),
    _OptIfOChGroupSinkIntervalLowAggregatedInputPower_Type()
)
optIfOChGroupSinkIntervalLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkIntervalHighAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkIntervalHighAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkIntervalHighAggregatedInputPower = _OptIfOChGroupSinkIntervalHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 3, 1, 5),
    _OptIfOChGroupSinkIntervalHighAggregatedInputPower_Type()
)
optIfOChGroupSinkIntervalHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkIntervalLastOutputPower_Type = Integer32
_OptIfOChGroupSinkIntervalLastOutputPower_Object = MibTableColumn
optIfOChGroupSinkIntervalLastOutputPower = _OptIfOChGroupSinkIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 3, 1, 6),
    _OptIfOChGroupSinkIntervalLastOutputPower_Type()
)
optIfOChGroupSinkIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalLastOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkIntervalLowOutputPower_Type = Integer32
_OptIfOChGroupSinkIntervalLowOutputPower_Object = MibTableColumn
optIfOChGroupSinkIntervalLowOutputPower = _OptIfOChGroupSinkIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 3, 1, 7),
    _OptIfOChGroupSinkIntervalLowOutputPower_Type()
)
optIfOChGroupSinkIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalLowOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkIntervalHighOutputPower_Type = Integer32
_OptIfOChGroupSinkIntervalHighOutputPower_Object = MibTableColumn
optIfOChGroupSinkIntervalHighOutputPower = _OptIfOChGroupSinkIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 3, 1, 8),
    _OptIfOChGroupSinkIntervalHighOutputPower_Type()
)
optIfOChGroupSinkIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkIntervalHighOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurDayTable_Object = MibTable
optIfOChGroupSinkCurDayTable = _OptIfOChGroupSinkCurDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 4)
)
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDayTable.setStatus("current")
_OptIfOChGroupSinkCurDayEntry_Object = MibTableRow
optIfOChGroupSinkCurDayEntry = _OptIfOChGroupSinkCurDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 4, 1)
)
optIfOChGroupSinkCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDayEntry.setStatus("current")
_OptIfOChGroupSinkCurDaySuspectedFlag_Type = TruthValue
_OptIfOChGroupSinkCurDaySuspectedFlag_Object = MibTableColumn
optIfOChGroupSinkCurDaySuspectedFlag = _OptIfOChGroupSinkCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 4, 1, 1),
    _OptIfOChGroupSinkCurDaySuspectedFlag_Type()
)
optIfOChGroupSinkCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDaySuspectedFlag.setStatus("current")
_OptIfOChGroupSinkCurDayLowAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkCurDayLowAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkCurDayLowAggregatedInputPower = _OptIfOChGroupSinkCurDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 4, 1, 2),
    _OptIfOChGroupSinkCurDayLowAggregatedInputPower_Type()
)
optIfOChGroupSinkCurDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDayLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurDayHighAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkCurDayHighAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkCurDayHighAggregatedInputPower = _OptIfOChGroupSinkCurDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 4, 1, 3),
    _OptIfOChGroupSinkCurDayHighAggregatedInputPower_Type()
)
optIfOChGroupSinkCurDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDayHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurDayLowOutputPower_Type = Integer32
_OptIfOChGroupSinkCurDayLowOutputPower_Object = MibTableColumn
optIfOChGroupSinkCurDayLowOutputPower = _OptIfOChGroupSinkCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 4, 1, 4),
    _OptIfOChGroupSinkCurDayLowOutputPower_Type()
)
optIfOChGroupSinkCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkCurDayHighOutputPower_Type = Integer32
_OptIfOChGroupSinkCurDayHighOutputPower_Object = MibTableColumn
optIfOChGroupSinkCurDayHighOutputPower = _OptIfOChGroupSinkCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 4, 1, 5),
    _OptIfOChGroupSinkCurDayHighOutputPower_Type()
)
optIfOChGroupSinkCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkCurDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkPrevDayTable_Object = MibTable
optIfOChGroupSinkPrevDayTable = _OptIfOChGroupSinkPrevDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 5)
)
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayTable.setStatus("current")
_OptIfOChGroupSinkPrevDayEntry_Object = MibTableRow
optIfOChGroupSinkPrevDayEntry = _OptIfOChGroupSinkPrevDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 5, 1)
)
optIfOChGroupSinkPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayEntry.setStatus("current")
_OptIfOChGroupSinkPrevDaySuspectedFlag_Type = TruthValue
_OptIfOChGroupSinkPrevDaySuspectedFlag_Object = MibTableColumn
optIfOChGroupSinkPrevDaySuspectedFlag = _OptIfOChGroupSinkPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 5, 1, 1),
    _OptIfOChGroupSinkPrevDaySuspectedFlag_Type()
)
optIfOChGroupSinkPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDaySuspectedFlag.setStatus("current")
_OptIfOChGroupSinkPrevDayLastAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkPrevDayLastAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkPrevDayLastAggregatedInputPower = _OptIfOChGroupSinkPrevDayLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 5, 1, 2),
    _OptIfOChGroupSinkPrevDayLastAggregatedInputPower_Type()
)
optIfOChGroupSinkPrevDayLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayLastAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkPrevDayLowAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkPrevDayLowAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkPrevDayLowAggregatedInputPower = _OptIfOChGroupSinkPrevDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 5, 1, 3),
    _OptIfOChGroupSinkPrevDayLowAggregatedInputPower_Type()
)
optIfOChGroupSinkPrevDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkPrevDayHighAggregatedInputPower_Type = Integer32
_OptIfOChGroupSinkPrevDayHighAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSinkPrevDayHighAggregatedInputPower = _OptIfOChGroupSinkPrevDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 5, 1, 4),
    _OptIfOChGroupSinkPrevDayHighAggregatedInputPower_Type()
)
optIfOChGroupSinkPrevDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkPrevDayLastOutputPower_Type = Integer32
_OptIfOChGroupSinkPrevDayLastOutputPower_Object = MibTableColumn
optIfOChGroupSinkPrevDayLastOutputPower = _OptIfOChGroupSinkPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 5, 1, 5),
    _OptIfOChGroupSinkPrevDayLastOutputPower_Type()
)
optIfOChGroupSinkPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayLastOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkPrevDayLowOutputPower_Type = Integer32
_OptIfOChGroupSinkPrevDayLowOutputPower_Object = MibTableColumn
optIfOChGroupSinkPrevDayLowOutputPower = _OptIfOChGroupSinkPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 5, 1, 6),
    _OptIfOChGroupSinkPrevDayLowOutputPower_Type()
)
optIfOChGroupSinkPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSinkPrevDayHighOutputPower_Type = Integer32
_OptIfOChGroupSinkPrevDayHighOutputPower_Object = MibTableColumn
optIfOChGroupSinkPrevDayHighOutputPower = _OptIfOChGroupSinkPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 5, 1, 7),
    _OptIfOChGroupSinkPrevDayHighOutputPower_Type()
)
optIfOChGroupSinkPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSinkPrevDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurrentTable_Object = MibTable
optIfOChGroupSrcCurrentTable = _OptIfOChGroupSrcCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6)
)
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentTable.setStatus("current")
_OptIfOChGroupSrcCurrentEntry_Object = MibTableRow
optIfOChGroupSrcCurrentEntry = _OptIfOChGroupSrcCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1)
)
optIfOChGroupSrcCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentEntry.setStatus("current")
_OptIfOChGroupSrcCurrentSuspectedFlag_Type = TruthValue
_OptIfOChGroupSrcCurrentSuspectedFlag_Object = MibTableColumn
optIfOChGroupSrcCurrentSuspectedFlag = _OptIfOChGroupSrcCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 1),
    _OptIfOChGroupSrcCurrentSuspectedFlag_Type()
)
optIfOChGroupSrcCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentSuspectedFlag.setStatus("current")
_OptIfOChGroupSrcCurrentOutputPower_Type = Integer32
_OptIfOChGroupSrcCurrentOutputPower_Object = MibTableColumn
optIfOChGroupSrcCurrentOutputPower = _OptIfOChGroupSrcCurrentOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 2),
    _OptIfOChGroupSrcCurrentOutputPower_Type()
)
optIfOChGroupSrcCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurrentLowOutputPower_Type = Integer32
_OptIfOChGroupSrcCurrentLowOutputPower_Object = MibTableColumn
optIfOChGroupSrcCurrentLowOutputPower = _OptIfOChGroupSrcCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 3),
    _OptIfOChGroupSrcCurrentLowOutputPower_Type()
)
optIfOChGroupSrcCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentLowOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurrentHighOutputPower_Type = Integer32
_OptIfOChGroupSrcCurrentHighOutputPower_Object = MibTableColumn
optIfOChGroupSrcCurrentHighOutputPower = _OptIfOChGroupSrcCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 4),
    _OptIfOChGroupSrcCurrentHighOutputPower_Type()
)
optIfOChGroupSrcCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentHighOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurrentLowerOutputPowerThreshold_Type = Integer32
_OptIfOChGroupSrcCurrentLowerOutputPowerThreshold_Object = MibTableColumn
optIfOChGroupSrcCurrentLowerOutputPowerThreshold = _OptIfOChGroupSrcCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 5),
    _OptIfOChGroupSrcCurrentLowerOutputPowerThreshold_Type()
)
optIfOChGroupSrcCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurrentUpperOutputPowerThreshold_Type = Integer32
_OptIfOChGroupSrcCurrentUpperOutputPowerThreshold_Object = MibTableColumn
optIfOChGroupSrcCurrentUpperOutputPowerThreshold = _OptIfOChGroupSrcCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 6),
    _OptIfOChGroupSrcCurrentUpperOutputPowerThreshold_Type()
)
optIfOChGroupSrcCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurrentAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcCurrentAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcCurrentAggregatedInputPower = _OptIfOChGroupSrcCurrentAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 7),
    _OptIfOChGroupSrcCurrentAggregatedInputPower_Type()
)
optIfOChGroupSrcCurrentAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurrentLowAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcCurrentLowAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcCurrentLowAggregatedInputPower = _OptIfOChGroupSrcCurrentLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 8),
    _OptIfOChGroupSrcCurrentLowAggregatedInputPower_Type()
)
optIfOChGroupSrcCurrentLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurrentHighAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcCurrentHighAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcCurrentHighAggregatedInputPower = _OptIfOChGroupSrcCurrentHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 9),
    _OptIfOChGroupSrcCurrentHighAggregatedInputPower_Type()
)
optIfOChGroupSrcCurrentHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurrentLowerInputPowerThreshold_Type = Integer32
_OptIfOChGroupSrcCurrentLowerInputPowerThreshold_Object = MibTableColumn
optIfOChGroupSrcCurrentLowerInputPowerThreshold = _OptIfOChGroupSrcCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 10),
    _OptIfOChGroupSrcCurrentLowerInputPowerThreshold_Type()
)
optIfOChGroupSrcCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurrentUpperInputPowerThreshold_Type = Integer32
_OptIfOChGroupSrcCurrentUpperInputPowerThreshold_Object = MibTableColumn
optIfOChGroupSrcCurrentUpperInputPowerThreshold = _OptIfOChGroupSrcCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 6, 1, 11),
    _OptIfOChGroupSrcCurrentUpperInputPowerThreshold_Type()
)
optIfOChGroupSrcCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChGroupSrcIntervalTable_Object = MibTable
optIfOChGroupSrcIntervalTable = _OptIfOChGroupSrcIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 7)
)
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalTable.setStatus("current")
_OptIfOChGroupSrcIntervalEntry_Object = MibTableRow
optIfOChGroupSrcIntervalEntry = _OptIfOChGroupSrcIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 7, 1)
)
optIfOChGroupSrcIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfOChGroupSrcIntervalNumber"),
)
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalEntry.setStatus("current")
_OptIfOChGroupSrcIntervalNumber_Type = OptIfIntervalNumber
_OptIfOChGroupSrcIntervalNumber_Object = MibTableColumn
optIfOChGroupSrcIntervalNumber = _OptIfOChGroupSrcIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 7, 1, 1),
    _OptIfOChGroupSrcIntervalNumber_Type()
)
optIfOChGroupSrcIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalNumber.setStatus("current")
_OptIfOChGroupSrcIntervalSuspectedFlag_Type = TruthValue
_OptIfOChGroupSrcIntervalSuspectedFlag_Object = MibTableColumn
optIfOChGroupSrcIntervalSuspectedFlag = _OptIfOChGroupSrcIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 7, 1, 2),
    _OptIfOChGroupSrcIntervalSuspectedFlag_Type()
)
optIfOChGroupSrcIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalSuspectedFlag.setStatus("current")
_OptIfOChGroupSrcIntervalLastOutputPower_Type = Integer32
_OptIfOChGroupSrcIntervalLastOutputPower_Object = MibTableColumn
optIfOChGroupSrcIntervalLastOutputPower = _OptIfOChGroupSrcIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 7, 1, 3),
    _OptIfOChGroupSrcIntervalLastOutputPower_Type()
)
optIfOChGroupSrcIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalLastOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcIntervalLowOutputPower_Type = Integer32
_OptIfOChGroupSrcIntervalLowOutputPower_Object = MibTableColumn
optIfOChGroupSrcIntervalLowOutputPower = _OptIfOChGroupSrcIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 7, 1, 4),
    _OptIfOChGroupSrcIntervalLowOutputPower_Type()
)
optIfOChGroupSrcIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalLowOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcIntervalHighOutputPower_Type = Integer32
_OptIfOChGroupSrcIntervalHighOutputPower_Object = MibTableColumn
optIfOChGroupSrcIntervalHighOutputPower = _OptIfOChGroupSrcIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 7, 1, 5),
    _OptIfOChGroupSrcIntervalHighOutputPower_Type()
)
optIfOChGroupSrcIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalHighOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcIntervalLastAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcIntervalLastAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcIntervalLastAggregatedInputPower = _OptIfOChGroupSrcIntervalLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 7, 1, 6),
    _OptIfOChGroupSrcIntervalLastAggregatedInputPower_Type()
)
optIfOChGroupSrcIntervalLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalLastAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcIntervalLowAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcIntervalLowAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcIntervalLowAggregatedInputPower = _OptIfOChGroupSrcIntervalLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 7, 1, 7),
    _OptIfOChGroupSrcIntervalLowAggregatedInputPower_Type()
)
optIfOChGroupSrcIntervalLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcIntervalHighAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcIntervalHighAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcIntervalHighAggregatedInputPower = _OptIfOChGroupSrcIntervalHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 7, 1, 8),
    _OptIfOChGroupSrcIntervalHighAggregatedInputPower_Type()
)
optIfOChGroupSrcIntervalHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcIntervalHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurDayTable_Object = MibTable
optIfOChGroupSrcCurDayTable = _OptIfOChGroupSrcCurDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 8)
)
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDayTable.setStatus("current")
_OptIfOChGroupSrcCurDayEntry_Object = MibTableRow
optIfOChGroupSrcCurDayEntry = _OptIfOChGroupSrcCurDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 8, 1)
)
optIfOChGroupSrcCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDayEntry.setStatus("current")
_OptIfOChGroupSrcCurDaySuspectedFlag_Type = TruthValue
_OptIfOChGroupSrcCurDaySuspectedFlag_Object = MibTableColumn
optIfOChGroupSrcCurDaySuspectedFlag = _OptIfOChGroupSrcCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 8, 1, 1),
    _OptIfOChGroupSrcCurDaySuspectedFlag_Type()
)
optIfOChGroupSrcCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDaySuspectedFlag.setStatus("current")
_OptIfOChGroupSrcCurDayLowOutputPower_Type = Integer32
_OptIfOChGroupSrcCurDayLowOutputPower_Object = MibTableColumn
optIfOChGroupSrcCurDayLowOutputPower = _OptIfOChGroupSrcCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 8, 1, 2),
    _OptIfOChGroupSrcCurDayLowOutputPower_Type()
)
optIfOChGroupSrcCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurDayHighOutputPower_Type = Integer32
_OptIfOChGroupSrcCurDayHighOutputPower_Object = MibTableColumn
optIfOChGroupSrcCurDayHighOutputPower = _OptIfOChGroupSrcCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 8, 1, 3),
    _OptIfOChGroupSrcCurDayHighOutputPower_Type()
)
optIfOChGroupSrcCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurDayLowAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcCurDayLowAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcCurDayLowAggregatedInputPower = _OptIfOChGroupSrcCurDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 8, 1, 4),
    _OptIfOChGroupSrcCurDayLowAggregatedInputPower_Type()
)
optIfOChGroupSrcCurDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDayLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcCurDayHighAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcCurDayHighAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcCurDayHighAggregatedInputPower = _OptIfOChGroupSrcCurDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 8, 1, 5),
    _OptIfOChGroupSrcCurDayHighAggregatedInputPower_Type()
)
optIfOChGroupSrcCurDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcCurDayHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcPrevDayTable_Object = MibTable
optIfOChGroupSrcPrevDayTable = _OptIfOChGroupSrcPrevDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 9)
)
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayTable.setStatus("current")
_OptIfOChGroupSrcPrevDayEntry_Object = MibTableRow
optIfOChGroupSrcPrevDayEntry = _OptIfOChGroupSrcPrevDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 9, 1)
)
optIfOChGroupSrcPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayEntry.setStatus("current")
_OptIfOChGroupSrcPrevDaySuspectedFlag_Type = TruthValue
_OptIfOChGroupSrcPrevDaySuspectedFlag_Object = MibTableColumn
optIfOChGroupSrcPrevDaySuspectedFlag = _OptIfOChGroupSrcPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 9, 1, 1),
    _OptIfOChGroupSrcPrevDaySuspectedFlag_Type()
)
optIfOChGroupSrcPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDaySuspectedFlag.setStatus("current")
_OptIfOChGroupSrcPrevDayLastOutputPower_Type = Integer32
_OptIfOChGroupSrcPrevDayLastOutputPower_Object = MibTableColumn
optIfOChGroupSrcPrevDayLastOutputPower = _OptIfOChGroupSrcPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 9, 1, 2),
    _OptIfOChGroupSrcPrevDayLastOutputPower_Type()
)
optIfOChGroupSrcPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayLastOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcPrevDayLowOutputPower_Type = Integer32
_OptIfOChGroupSrcPrevDayLowOutputPower_Object = MibTableColumn
optIfOChGroupSrcPrevDayLowOutputPower = _OptIfOChGroupSrcPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 9, 1, 3),
    _OptIfOChGroupSrcPrevDayLowOutputPower_Type()
)
optIfOChGroupSrcPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcPrevDayHighOutputPower_Type = Integer32
_OptIfOChGroupSrcPrevDayHighOutputPower_Object = MibTableColumn
optIfOChGroupSrcPrevDayHighOutputPower = _OptIfOChGroupSrcPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 9, 1, 4),
    _OptIfOChGroupSrcPrevDayHighOutputPower_Type()
)
optIfOChGroupSrcPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcPrevDayLastAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcPrevDayLastAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcPrevDayLastAggregatedInputPower = _OptIfOChGroupSrcPrevDayLastAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 9, 1, 5),
    _OptIfOChGroupSrcPrevDayLastAggregatedInputPower_Type()
)
optIfOChGroupSrcPrevDayLastAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayLastAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayLastAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcPrevDayLowAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcPrevDayLowAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcPrevDayLowAggregatedInputPower = _OptIfOChGroupSrcPrevDayLowAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 9, 1, 6),
    _OptIfOChGroupSrcPrevDayLowAggregatedInputPower_Type()
)
optIfOChGroupSrcPrevDayLowAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayLowAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayLowAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOChGroupSrcPrevDayHighAggregatedInputPower_Type = Integer32
_OptIfOChGroupSrcPrevDayHighAggregatedInputPower_Object = MibTableColumn
optIfOChGroupSrcPrevDayHighAggregatedInputPower = _OptIfOChGroupSrcPrevDayHighAggregatedInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 5, 9, 1, 7),
    _OptIfOChGroupSrcPrevDayHighAggregatedInputPower_Type()
)
optIfOChGroupSrcPrevDayHighAggregatedInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayHighAggregatedInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChGroupSrcPrevDayHighAggregatedInputPower.setUnits("0.1 dbm")
_OptIfOCh_ObjectIdentity = ObjectIdentity
optIfOCh = _OptIfOCh_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6)
)
_OptIfOChConfigTable_Object = MibTable
optIfOChConfigTable = _OptIfOChConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 1)
)
if mibBuilder.loadTexts:
    optIfOChConfigTable.setStatus("current")
_OptIfOChConfigEntry_Object = MibTableRow
optIfOChConfigEntry = _OptIfOChConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 1, 1)
)
optIfOChConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChConfigEntry.setStatus("current")
_OptIfOChDirectionality_Type = OptIfDirectionality
_OptIfOChDirectionality_Object = MibTableColumn
optIfOChDirectionality = _OptIfOChDirectionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 1, 1, 1),
    _OptIfOChDirectionality_Type()
)
optIfOChDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChDirectionality.setStatus("current")


class _OptIfOChCurrentStatus_Type(Bits):
    """Custom type optIfOChCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("los", 1),
          ("losP", 0),
          ("oci", 2),
          ("ssf", 5),
          ("ssfO", 4),
          ("ssfP", 3))
    )

_OptIfOChCurrentStatus_Type.__name__ = "Bits"
_OptIfOChCurrentStatus_Object = MibTableColumn
optIfOChCurrentStatus = _OptIfOChCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 1, 1, 2),
    _OptIfOChCurrentStatus_Type()
)
optIfOChCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChCurrentStatus.setStatus("current")
_OptIfOChSinkCurrentTable_Object = MibTable
optIfOChSinkCurrentTable = _OptIfOChSinkCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 2)
)
if mibBuilder.loadTexts:
    optIfOChSinkCurrentTable.setStatus("current")
_OptIfOChSinkCurrentEntry_Object = MibTableRow
optIfOChSinkCurrentEntry = _OptIfOChSinkCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 2, 1)
)
optIfOChSinkCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChSinkCurrentEntry.setStatus("current")
_OptIfOChSinkCurrentSuspectedFlag_Type = TruthValue
_OptIfOChSinkCurrentSuspectedFlag_Object = MibTableColumn
optIfOChSinkCurrentSuspectedFlag = _OptIfOChSinkCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 2, 1, 1),
    _OptIfOChSinkCurrentSuspectedFlag_Type()
)
optIfOChSinkCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentSuspectedFlag.setStatus("current")
_OptIfOChSinkCurrentInputPower_Type = Integer32
_OptIfOChSinkCurrentInputPower_Object = MibTableColumn
optIfOChSinkCurrentInputPower = _OptIfOChSinkCurrentInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 2, 1, 2),
    _OptIfOChSinkCurrentInputPower_Type()
)
optIfOChSinkCurrentInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentInputPower.setUnits("0.1 dbm")
_OptIfOChSinkCurrentLowInputPower_Type = Integer32
_OptIfOChSinkCurrentLowInputPower_Object = MibTableColumn
optIfOChSinkCurrentLowInputPower = _OptIfOChSinkCurrentLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 2, 1, 3),
    _OptIfOChSinkCurrentLowInputPower_Type()
)
optIfOChSinkCurrentLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentLowInputPower.setUnits("0.1 dbm")
_OptIfOChSinkCurrentHighInputPower_Type = Integer32
_OptIfOChSinkCurrentHighInputPower_Object = MibTableColumn
optIfOChSinkCurrentHighInputPower = _OptIfOChSinkCurrentHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 2, 1, 4),
    _OptIfOChSinkCurrentHighInputPower_Type()
)
optIfOChSinkCurrentHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentHighInputPower.setUnits("0.1 dbm")
_OptIfOChSinkCurrentLowerInputPowerThreshold_Type = Integer32
_OptIfOChSinkCurrentLowerInputPowerThreshold_Object = MibTableColumn
optIfOChSinkCurrentLowerInputPowerThreshold = _OptIfOChSinkCurrentLowerInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 2, 1, 5),
    _OptIfOChSinkCurrentLowerInputPowerThreshold_Type()
)
optIfOChSinkCurrentLowerInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentLowerInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentLowerInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChSinkCurrentUpperInputPowerThreshold_Type = Integer32
_OptIfOChSinkCurrentUpperInputPowerThreshold_Object = MibTableColumn
optIfOChSinkCurrentUpperInputPowerThreshold = _OptIfOChSinkCurrentUpperInputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 2, 1, 6),
    _OptIfOChSinkCurrentUpperInputPowerThreshold_Type()
)
optIfOChSinkCurrentUpperInputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentUpperInputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkCurrentUpperInputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChSinkIntervalTable_Object = MibTable
optIfOChSinkIntervalTable = _OptIfOChSinkIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 3)
)
if mibBuilder.loadTexts:
    optIfOChSinkIntervalTable.setStatus("current")
_OptIfOChSinkIntervalEntry_Object = MibTableRow
optIfOChSinkIntervalEntry = _OptIfOChSinkIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 3, 1)
)
optIfOChSinkIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfOChSinkIntervalNumber"),
)
if mibBuilder.loadTexts:
    optIfOChSinkIntervalEntry.setStatus("current")
_OptIfOChSinkIntervalNumber_Type = OptIfIntervalNumber
_OptIfOChSinkIntervalNumber_Object = MibTableColumn
optIfOChSinkIntervalNumber = _OptIfOChSinkIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 3, 1, 1),
    _OptIfOChSinkIntervalNumber_Type()
)
optIfOChSinkIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfOChSinkIntervalNumber.setStatus("current")
_OptIfOChSinkIntervalSuspectedFlag_Type = TruthValue
_OptIfOChSinkIntervalSuspectedFlag_Object = MibTableColumn
optIfOChSinkIntervalSuspectedFlag = _OptIfOChSinkIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 3, 1, 2),
    _OptIfOChSinkIntervalSuspectedFlag_Type()
)
optIfOChSinkIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkIntervalSuspectedFlag.setStatus("current")
_OptIfOChSinkIntervalLastInputPower_Type = Integer32
_OptIfOChSinkIntervalLastInputPower_Object = MibTableColumn
optIfOChSinkIntervalLastInputPower = _OptIfOChSinkIntervalLastInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 3, 1, 3),
    _OptIfOChSinkIntervalLastInputPower_Type()
)
optIfOChSinkIntervalLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkIntervalLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkIntervalLastInputPower.setUnits("0.1 dbm")
_OptIfOChSinkIntervalLowInputPower_Type = Integer32
_OptIfOChSinkIntervalLowInputPower_Object = MibTableColumn
optIfOChSinkIntervalLowInputPower = _OptIfOChSinkIntervalLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 3, 1, 4),
    _OptIfOChSinkIntervalLowInputPower_Type()
)
optIfOChSinkIntervalLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkIntervalLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkIntervalLowInputPower.setUnits("0.1 dbm")
_OptIfOChSinkIntervalHighInputPower_Type = Integer32
_OptIfOChSinkIntervalHighInputPower_Object = MibTableColumn
optIfOChSinkIntervalHighInputPower = _OptIfOChSinkIntervalHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 3, 1, 5),
    _OptIfOChSinkIntervalHighInputPower_Type()
)
optIfOChSinkIntervalHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkIntervalHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkIntervalHighInputPower.setUnits("0.1 dbm")
_OptIfOChSinkCurDayTable_Object = MibTable
optIfOChSinkCurDayTable = _OptIfOChSinkCurDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 4)
)
if mibBuilder.loadTexts:
    optIfOChSinkCurDayTable.setStatus("current")
_OptIfOChSinkCurDayEntry_Object = MibTableRow
optIfOChSinkCurDayEntry = _OptIfOChSinkCurDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 4, 1)
)
optIfOChSinkCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChSinkCurDayEntry.setStatus("current")
_OptIfOChSinkCurDaySuspectedFlag_Type = TruthValue
_OptIfOChSinkCurDaySuspectedFlag_Object = MibTableColumn
optIfOChSinkCurDaySuspectedFlag = _OptIfOChSinkCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 4, 1, 1),
    _OptIfOChSinkCurDaySuspectedFlag_Type()
)
optIfOChSinkCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkCurDaySuspectedFlag.setStatus("current")
_OptIfOChSinkCurDayLowInputPower_Type = Integer32
_OptIfOChSinkCurDayLowInputPower_Object = MibTableColumn
optIfOChSinkCurDayLowInputPower = _OptIfOChSinkCurDayLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 4, 1, 2),
    _OptIfOChSinkCurDayLowInputPower_Type()
)
optIfOChSinkCurDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkCurDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkCurDayLowInputPower.setUnits("0.1 dbm")
_OptIfOChSinkCurDayHighInputPower_Type = Integer32
_OptIfOChSinkCurDayHighInputPower_Object = MibTableColumn
optIfOChSinkCurDayHighInputPower = _OptIfOChSinkCurDayHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 4, 1, 3),
    _OptIfOChSinkCurDayHighInputPower_Type()
)
optIfOChSinkCurDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkCurDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkCurDayHighInputPower.setUnits("0.1 dbm")
_OptIfOChSinkPrevDayTable_Object = MibTable
optIfOChSinkPrevDayTable = _OptIfOChSinkPrevDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 5)
)
if mibBuilder.loadTexts:
    optIfOChSinkPrevDayTable.setStatus("current")
_OptIfOChSinkPrevDayEntry_Object = MibTableRow
optIfOChSinkPrevDayEntry = _OptIfOChSinkPrevDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 5, 1)
)
optIfOChSinkPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChSinkPrevDayEntry.setStatus("current")
_OptIfOChSinkPrevDaySuspectedFlag_Type = TruthValue
_OptIfOChSinkPrevDaySuspectedFlag_Object = MibTableColumn
optIfOChSinkPrevDaySuspectedFlag = _OptIfOChSinkPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 5, 1, 1),
    _OptIfOChSinkPrevDaySuspectedFlag_Type()
)
optIfOChSinkPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkPrevDaySuspectedFlag.setStatus("current")
_OptIfOChSinkPrevDayLastInputPower_Type = Integer32
_OptIfOChSinkPrevDayLastInputPower_Object = MibTableColumn
optIfOChSinkPrevDayLastInputPower = _OptIfOChSinkPrevDayLastInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 5, 1, 2),
    _OptIfOChSinkPrevDayLastInputPower_Type()
)
optIfOChSinkPrevDayLastInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkPrevDayLastInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkPrevDayLastInputPower.setUnits("0.1 dbm")
_OptIfOChSinkPrevDayLowInputPower_Type = Integer32
_OptIfOChSinkPrevDayLowInputPower_Object = MibTableColumn
optIfOChSinkPrevDayLowInputPower = _OptIfOChSinkPrevDayLowInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 5, 1, 3),
    _OptIfOChSinkPrevDayLowInputPower_Type()
)
optIfOChSinkPrevDayLowInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkPrevDayLowInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkPrevDayLowInputPower.setUnits("0.1 dbm")
_OptIfOChSinkPrevDayHighInputPower_Type = Integer32
_OptIfOChSinkPrevDayHighInputPower_Object = MibTableColumn
optIfOChSinkPrevDayHighInputPower = _OptIfOChSinkPrevDayHighInputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 5, 1, 4),
    _OptIfOChSinkPrevDayHighInputPower_Type()
)
optIfOChSinkPrevDayHighInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSinkPrevDayHighInputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSinkPrevDayHighInputPower.setUnits("0.1 dbm")
_OptIfOChSrcCurrentTable_Object = MibTable
optIfOChSrcCurrentTable = _OptIfOChSrcCurrentTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 6)
)
if mibBuilder.loadTexts:
    optIfOChSrcCurrentTable.setStatus("current")
_OptIfOChSrcCurrentEntry_Object = MibTableRow
optIfOChSrcCurrentEntry = _OptIfOChSrcCurrentEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 6, 1)
)
optIfOChSrcCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChSrcCurrentEntry.setStatus("current")
_OptIfOChSrcCurrentSuspectedFlag_Type = TruthValue
_OptIfOChSrcCurrentSuspectedFlag_Object = MibTableColumn
optIfOChSrcCurrentSuspectedFlag = _OptIfOChSrcCurrentSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 6, 1, 1),
    _OptIfOChSrcCurrentSuspectedFlag_Type()
)
optIfOChSrcCurrentSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentSuspectedFlag.setStatus("current")
_OptIfOChSrcCurrentOutputPower_Type = Integer32
_OptIfOChSrcCurrentOutputPower_Object = MibTableColumn
optIfOChSrcCurrentOutputPower = _OptIfOChSrcCurrentOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 6, 1, 2),
    _OptIfOChSrcCurrentOutputPower_Type()
)
optIfOChSrcCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentOutputPower.setUnits("0.1 dbm")
_OptIfOChSrcCurrentLowOutputPower_Type = Integer32
_OptIfOChSrcCurrentLowOutputPower_Object = MibTableColumn
optIfOChSrcCurrentLowOutputPower = _OptIfOChSrcCurrentLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 6, 1, 3),
    _OptIfOChSrcCurrentLowOutputPower_Type()
)
optIfOChSrcCurrentLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentLowOutputPower.setUnits("0.1 dbm")
_OptIfOChSrcCurrentHighOutputPower_Type = Integer32
_OptIfOChSrcCurrentHighOutputPower_Object = MibTableColumn
optIfOChSrcCurrentHighOutputPower = _OptIfOChSrcCurrentHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 6, 1, 4),
    _OptIfOChSrcCurrentHighOutputPower_Type()
)
optIfOChSrcCurrentHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentHighOutputPower.setUnits("0.1 dbm")
_OptIfOChSrcCurrentLowerOutputPowerThreshold_Type = Integer32
_OptIfOChSrcCurrentLowerOutputPowerThreshold_Object = MibTableColumn
optIfOChSrcCurrentLowerOutputPowerThreshold = _OptIfOChSrcCurrentLowerOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 6, 1, 5),
    _OptIfOChSrcCurrentLowerOutputPowerThreshold_Type()
)
optIfOChSrcCurrentLowerOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentLowerOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentLowerOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChSrcCurrentUpperOutputPowerThreshold_Type = Integer32
_OptIfOChSrcCurrentUpperOutputPowerThreshold_Object = MibTableColumn
optIfOChSrcCurrentUpperOutputPowerThreshold = _OptIfOChSrcCurrentUpperOutputPowerThreshold_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 6, 1, 6),
    _OptIfOChSrcCurrentUpperOutputPowerThreshold_Type()
)
optIfOChSrcCurrentUpperOutputPowerThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentUpperOutputPowerThreshold.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcCurrentUpperOutputPowerThreshold.setUnits("0.1 dbm")
_OptIfOChSrcIntervalTable_Object = MibTable
optIfOChSrcIntervalTable = _OptIfOChSrcIntervalTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 7)
)
if mibBuilder.loadTexts:
    optIfOChSrcIntervalTable.setStatus("current")
_OptIfOChSrcIntervalEntry_Object = MibTableRow
optIfOChSrcIntervalEntry = _OptIfOChSrcIntervalEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 7, 1)
)
optIfOChSrcIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfOChSrcIntervalNumber"),
)
if mibBuilder.loadTexts:
    optIfOChSrcIntervalEntry.setStatus("current")
_OptIfOChSrcIntervalNumber_Type = OptIfIntervalNumber
_OptIfOChSrcIntervalNumber_Object = MibTableColumn
optIfOChSrcIntervalNumber = _OptIfOChSrcIntervalNumber_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 7, 1, 1),
    _OptIfOChSrcIntervalNumber_Type()
)
optIfOChSrcIntervalNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfOChSrcIntervalNumber.setStatus("current")
_OptIfOChSrcIntervalSuspectedFlag_Type = TruthValue
_OptIfOChSrcIntervalSuspectedFlag_Object = MibTableColumn
optIfOChSrcIntervalSuspectedFlag = _OptIfOChSrcIntervalSuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 7, 1, 2),
    _OptIfOChSrcIntervalSuspectedFlag_Type()
)
optIfOChSrcIntervalSuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcIntervalSuspectedFlag.setStatus("current")
_OptIfOChSrcIntervalLastOutputPower_Type = Integer32
_OptIfOChSrcIntervalLastOutputPower_Object = MibTableColumn
optIfOChSrcIntervalLastOutputPower = _OptIfOChSrcIntervalLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 7, 1, 3),
    _OptIfOChSrcIntervalLastOutputPower_Type()
)
optIfOChSrcIntervalLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcIntervalLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcIntervalLastOutputPower.setUnits("0.1 dbm")
_OptIfOChSrcIntervalLowOutputPower_Type = Integer32
_OptIfOChSrcIntervalLowOutputPower_Object = MibTableColumn
optIfOChSrcIntervalLowOutputPower = _OptIfOChSrcIntervalLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 7, 1, 4),
    _OptIfOChSrcIntervalLowOutputPower_Type()
)
optIfOChSrcIntervalLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcIntervalLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcIntervalLowOutputPower.setUnits("0.1 dbm")
_OptIfOChSrcIntervalHighOutputPower_Type = Integer32
_OptIfOChSrcIntervalHighOutputPower_Object = MibTableColumn
optIfOChSrcIntervalHighOutputPower = _OptIfOChSrcIntervalHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 7, 1, 5),
    _OptIfOChSrcIntervalHighOutputPower_Type()
)
optIfOChSrcIntervalHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcIntervalHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcIntervalHighOutputPower.setUnits("0.1 dbm")
_OptIfOChSrcCurDayTable_Object = MibTable
optIfOChSrcCurDayTable = _OptIfOChSrcCurDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 8)
)
if mibBuilder.loadTexts:
    optIfOChSrcCurDayTable.setStatus("current")
_OptIfOChSrcCurDayEntry_Object = MibTableRow
optIfOChSrcCurDayEntry = _OptIfOChSrcCurDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 8, 1)
)
optIfOChSrcCurDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChSrcCurDayEntry.setStatus("current")
_OptIfOChSrcCurDaySuspectedFlag_Type = TruthValue
_OptIfOChSrcCurDaySuspectedFlag_Object = MibTableColumn
optIfOChSrcCurDaySuspectedFlag = _OptIfOChSrcCurDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 8, 1, 1),
    _OptIfOChSrcCurDaySuspectedFlag_Type()
)
optIfOChSrcCurDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcCurDaySuspectedFlag.setStatus("current")
_OptIfOChSrcCurDayLowOutputPower_Type = Integer32
_OptIfOChSrcCurDayLowOutputPower_Object = MibTableColumn
optIfOChSrcCurDayLowOutputPower = _OptIfOChSrcCurDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 8, 1, 2),
    _OptIfOChSrcCurDayLowOutputPower_Type()
)
optIfOChSrcCurDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcCurDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcCurDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOChSrcCurDayHighOutputPower_Type = Integer32
_OptIfOChSrcCurDayHighOutputPower_Object = MibTableColumn
optIfOChSrcCurDayHighOutputPower = _OptIfOChSrcCurDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 8, 1, 3),
    _OptIfOChSrcCurDayHighOutputPower_Type()
)
optIfOChSrcCurDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcCurDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcCurDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOChSrcPrevDayTable_Object = MibTable
optIfOChSrcPrevDayTable = _OptIfOChSrcPrevDayTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 9)
)
if mibBuilder.loadTexts:
    optIfOChSrcPrevDayTable.setStatus("current")
_OptIfOChSrcPrevDayEntry_Object = MibTableRow
optIfOChSrcPrevDayEntry = _OptIfOChSrcPrevDayEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 9, 1)
)
optIfOChSrcPrevDayEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOChSrcPrevDayEntry.setStatus("current")
_OptIfOChSrcPrevDaySuspectedFlag_Type = TruthValue
_OptIfOChSrcPrevDaySuspectedFlag_Object = MibTableColumn
optIfOChSrcPrevDaySuspectedFlag = _OptIfOChSrcPrevDaySuspectedFlag_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 9, 1, 1),
    _OptIfOChSrcPrevDaySuspectedFlag_Type()
)
optIfOChSrcPrevDaySuspectedFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcPrevDaySuspectedFlag.setStatus("current")
_OptIfOChSrcPrevDayLastOutputPower_Type = Integer32
_OptIfOChSrcPrevDayLastOutputPower_Object = MibTableColumn
optIfOChSrcPrevDayLastOutputPower = _OptIfOChSrcPrevDayLastOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 9, 1, 2),
    _OptIfOChSrcPrevDayLastOutputPower_Type()
)
optIfOChSrcPrevDayLastOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcPrevDayLastOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcPrevDayLastOutputPower.setUnits("0.1 dbm")
_OptIfOChSrcPrevDayLowOutputPower_Type = Integer32
_OptIfOChSrcPrevDayLowOutputPower_Object = MibTableColumn
optIfOChSrcPrevDayLowOutputPower = _OptIfOChSrcPrevDayLowOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 9, 1, 3),
    _OptIfOChSrcPrevDayLowOutputPower_Type()
)
optIfOChSrcPrevDayLowOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcPrevDayLowOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcPrevDayLowOutputPower.setUnits("0.1 dbm")
_OptIfOChSrcPrevDayHighOutputPower_Type = Integer32
_OptIfOChSrcPrevDayHighOutputPower_Object = MibTableColumn
optIfOChSrcPrevDayHighOutputPower = _OptIfOChSrcPrevDayHighOutputPower_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 6, 9, 1, 4),
    _OptIfOChSrcPrevDayHighOutputPower_Type()
)
optIfOChSrcPrevDayHighOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOChSrcPrevDayHighOutputPower.setStatus("current")
if mibBuilder.loadTexts:
    optIfOChSrcPrevDayHighOutputPower.setUnits("0.1 dbm")
_OptIfOTUk_ObjectIdentity = ObjectIdentity
optIfOTUk = _OptIfOTUk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7)
)
_OptIfOTUkConfigTable_Object = MibTable
optIfOTUkConfigTable = _OptIfOTUkConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1)
)
if mibBuilder.loadTexts:
    optIfOTUkConfigTable.setStatus("current")
_OptIfOTUkConfigEntry_Object = MibTableRow
optIfOTUkConfigEntry = _OptIfOTUkConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1)
)
optIfOTUkConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfOTUkConfigEntry.setStatus("current")
_OptIfOTUkDirectionality_Type = OptIfDirectionality
_OptIfOTUkDirectionality_Object = MibTableColumn
optIfOTUkDirectionality = _OptIfOTUkDirectionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 1),
    _OptIfOTUkDirectionality_Type()
)
optIfOTUkDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTUkDirectionality.setStatus("current")
_OptIfOTUkBitRateK_Type = OptIfBitRateK
_OptIfOTUkBitRateK_Object = MibTableColumn
optIfOTUkBitRateK = _OptIfOTUkBitRateK_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 2),
    _OptIfOTUkBitRateK_Type()
)
optIfOTUkBitRateK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTUkBitRateK.setStatus("current")
_OptIfOTUkTraceIdentifierTransmitted_Type = OptIfTxTI
_OptIfOTUkTraceIdentifierTransmitted_Object = MibTableColumn
optIfOTUkTraceIdentifierTransmitted = _OptIfOTUkTraceIdentifierTransmitted_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 3),
    _OptIfOTUkTraceIdentifierTransmitted_Type()
)
optIfOTUkTraceIdentifierTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTUkTraceIdentifierTransmitted.setStatus("current")
_OptIfOTUkDAPIExpected_Type = OptIfExDAPI
_OptIfOTUkDAPIExpected_Object = MibTableColumn
optIfOTUkDAPIExpected = _OptIfOTUkDAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 4),
    _OptIfOTUkDAPIExpected_Type()
)
optIfOTUkDAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTUkDAPIExpected.setStatus("current")
_OptIfOTUkSAPIExpected_Type = OptIfExSAPI
_OptIfOTUkSAPIExpected_Object = MibTableColumn
optIfOTUkSAPIExpected = _OptIfOTUkSAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 5),
    _OptIfOTUkSAPIExpected_Type()
)
optIfOTUkSAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTUkSAPIExpected.setStatus("current")
_OptIfOTUkTraceIdentifierAccepted_Type = OptIfAcTI
_OptIfOTUkTraceIdentifierAccepted_Object = MibTableColumn
optIfOTUkTraceIdentifierAccepted = _OptIfOTUkTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 6),
    _OptIfOTUkTraceIdentifierAccepted_Type()
)
optIfOTUkTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTUkTraceIdentifierAccepted.setStatus("current")
_OptIfOTUkTIMDetMode_Type = OptIfTIMDetMode
_OptIfOTUkTIMDetMode_Object = MibTableColumn
optIfOTUkTIMDetMode = _OptIfOTUkTIMDetMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 7),
    _OptIfOTUkTIMDetMode_Type()
)
optIfOTUkTIMDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTUkTIMDetMode.setStatus("current")
_OptIfOTUkTIMActEnabled_Type = TruthValue
_OptIfOTUkTIMActEnabled_Object = MibTableColumn
optIfOTUkTIMActEnabled = _OptIfOTUkTIMActEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 8),
    _OptIfOTUkTIMActEnabled_Type()
)
optIfOTUkTIMActEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTUkTIMActEnabled.setStatus("current")
_OptIfOTUkDEGThr_Type = OptIfDEGThr
_OptIfOTUkDEGThr_Object = MibTableColumn
optIfOTUkDEGThr = _OptIfOTUkDEGThr_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 9),
    _OptIfOTUkDEGThr_Type()
)
optIfOTUkDEGThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTUkDEGThr.setStatus("current")
if mibBuilder.loadTexts:
    optIfOTUkDEGThr.setUnits("percentage")
_OptIfOTUkDEGM_Type = OptIfDEGM
_OptIfOTUkDEGM_Object = MibTableColumn
optIfOTUkDEGM = _OptIfOTUkDEGM_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 10),
    _OptIfOTUkDEGM_Type()
)
optIfOTUkDEGM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTUkDEGM.setStatus("current")
_OptIfOTUkSinkAdaptActive_Type = TruthValue
_OptIfOTUkSinkAdaptActive_Object = MibTableColumn
optIfOTUkSinkAdaptActive = _OptIfOTUkSinkAdaptActive_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 11),
    _OptIfOTUkSinkAdaptActive_Type()
)
optIfOTUkSinkAdaptActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTUkSinkAdaptActive.setStatus("current")
_OptIfOTUkSourceAdaptActive_Type = TruthValue
_OptIfOTUkSourceAdaptActive_Object = MibTableColumn
optIfOTUkSourceAdaptActive = _OptIfOTUkSourceAdaptActive_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 12),
    _OptIfOTUkSourceAdaptActive_Type()
)
optIfOTUkSourceAdaptActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTUkSourceAdaptActive.setStatus("current")
_OptIfOTUkSinkFECEnabled_Type = TruthValue
_OptIfOTUkSinkFECEnabled_Object = MibTableColumn
optIfOTUkSinkFECEnabled = _OptIfOTUkSinkFECEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 13),
    _OptIfOTUkSinkFECEnabled_Type()
)
optIfOTUkSinkFECEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfOTUkSinkFECEnabled.setStatus("current")


class _OptIfOTUkCurrentStatus_Type(Bits):
    """Custom type optIfOTUkCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("ais", 5),
          ("bdi", 2),
          ("deg", 1),
          ("lof", 4),
          ("lom", 6),
          ("ssf", 3),
          ("tim", 0))
    )

_OptIfOTUkCurrentStatus_Type.__name__ = "Bits"
_OptIfOTUkCurrentStatus_Object = MibTableColumn
optIfOTUkCurrentStatus = _OptIfOTUkCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 1, 1, 14),
    _OptIfOTUkCurrentStatus_Type()
)
optIfOTUkCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfOTUkCurrentStatus.setStatus("current")
_OptIfGCC0ConfigTable_Object = MibTable
optIfGCC0ConfigTable = _OptIfGCC0ConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 2)
)
if mibBuilder.loadTexts:
    optIfGCC0ConfigTable.setStatus("current")
_OptIfGCC0ConfigEntry_Object = MibTableRow
optIfGCC0ConfigEntry = _OptIfGCC0ConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 2, 1)
)
optIfGCC0ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfGCC0Directionality"),
)
if mibBuilder.loadTexts:
    optIfGCC0ConfigEntry.setStatus("current")
_OptIfGCC0Directionality_Type = OptIfDirectionality
_OptIfGCC0Directionality_Object = MibTableColumn
optIfGCC0Directionality = _OptIfGCC0Directionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 2, 1, 1),
    _OptIfGCC0Directionality_Type()
)
optIfGCC0Directionality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfGCC0Directionality.setStatus("current")
_OptIfGCC0Application_Type = SnmpAdminString
_OptIfGCC0Application_Object = MibTableColumn
optIfGCC0Application = _OptIfGCC0Application_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 2, 1, 2),
    _OptIfGCC0Application_Type()
)
optIfGCC0Application.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfGCC0Application.setStatus("current")
_OptIfGCC0RowStatus_Type = RowStatus
_OptIfGCC0RowStatus_Object = MibTableColumn
optIfGCC0RowStatus = _OptIfGCC0RowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 7, 2, 1, 3),
    _OptIfGCC0RowStatus_Type()
)
optIfGCC0RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfGCC0RowStatus.setStatus("current")
_OptIfODUk_ObjectIdentity = ObjectIdentity
optIfODUk = _OptIfODUk_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8)
)
_OptIfODUkConfigTable_Object = MibTable
optIfODUkConfigTable = _OptIfODUkConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 1)
)
if mibBuilder.loadTexts:
    optIfODUkConfigTable.setStatus("current")
_OptIfODUkConfigEntry_Object = MibTableRow
optIfODUkConfigEntry = _OptIfODUkConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 1, 1)
)
optIfODUkConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfODUkConfigEntry.setStatus("current")
_OptIfODUkDirectionality_Type = OptIfDirectionality
_OptIfODUkDirectionality_Object = MibTableColumn
optIfODUkDirectionality = _OptIfODUkDirectionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 1, 1, 1),
    _OptIfODUkDirectionality_Type()
)
optIfODUkDirectionality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkDirectionality.setStatus("current")
_OptIfODUkBitRateK_Type = OptIfBitRateK
_OptIfODUkBitRateK_Object = MibTableColumn
optIfODUkBitRateK = _OptIfODUkBitRateK_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 1, 1, 2),
    _OptIfODUkBitRateK_Type()
)
optIfODUkBitRateK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkBitRateK.setStatus("current")


class _OptIfODUkTcmFieldsInUse_Type(Bits):
    """Custom type optIfODUkTcmFieldsInUse based on Bits"""
    namedValues = NamedValues(
        *(("tcmField1", 0),
          ("tcmField2", 1),
          ("tcmField3", 2),
          ("tcmField4", 3),
          ("tcmField5", 4),
          ("tcmField6", 5))
    )

_OptIfODUkTcmFieldsInUse_Type.__name__ = "Bits"
_OptIfODUkTcmFieldsInUse_Object = MibTableColumn
optIfODUkTcmFieldsInUse = _OptIfODUkTcmFieldsInUse_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 1, 1, 3),
    _OptIfODUkTcmFieldsInUse_Type()
)
optIfODUkTcmFieldsInUse.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkTcmFieldsInUse.setStatus("current")
_OptIfODUkPositionSeqCurrentSize_Type = Unsigned32
_OptIfODUkPositionSeqCurrentSize_Object = MibTableColumn
optIfODUkPositionSeqCurrentSize = _OptIfODUkPositionSeqCurrentSize_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 1, 1, 4),
    _OptIfODUkPositionSeqCurrentSize_Type()
)
optIfODUkPositionSeqCurrentSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkPositionSeqCurrentSize.setStatus("current")
_OptIfODUkTtpPresent_Type = TruthValue
_OptIfODUkTtpPresent_Object = MibTableColumn
optIfODUkTtpPresent = _OptIfODUkTtpPresent_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 1, 1, 5),
    _OptIfODUkTtpPresent_Type()
)
optIfODUkTtpPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkTtpPresent.setStatus("current")
_OptIfODUkTtpConfigTable_Object = MibTable
optIfODUkTtpConfigTable = _OptIfODUkTtpConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2)
)
if mibBuilder.loadTexts:
    optIfODUkTtpConfigTable.setStatus("current")
_OptIfODUkTtpConfigEntry_Object = MibTableRow
optIfODUkTtpConfigEntry = _OptIfODUkTtpConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2, 1)
)
optIfODUkTtpConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    optIfODUkTtpConfigEntry.setStatus("current")
_OptIfODUkTtpTraceIdentifierTransmitted_Type = OptIfTxTI
_OptIfODUkTtpTraceIdentifierTransmitted_Object = MibTableColumn
optIfODUkTtpTraceIdentifierTransmitted = _OptIfODUkTtpTraceIdentifierTransmitted_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2, 1, 1),
    _OptIfODUkTtpTraceIdentifierTransmitted_Type()
)
optIfODUkTtpTraceIdentifierTransmitted.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfODUkTtpTraceIdentifierTransmitted.setStatus("current")
_OptIfODUkTtpDAPIExpected_Type = OptIfExDAPI
_OptIfODUkTtpDAPIExpected_Object = MibTableColumn
optIfODUkTtpDAPIExpected = _OptIfODUkTtpDAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2, 1, 2),
    _OptIfODUkTtpDAPIExpected_Type()
)
optIfODUkTtpDAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfODUkTtpDAPIExpected.setStatus("current")
_OptIfODUkTtpSAPIExpected_Type = OptIfExSAPI
_OptIfODUkTtpSAPIExpected_Object = MibTableColumn
optIfODUkTtpSAPIExpected = _OptIfODUkTtpSAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2, 1, 3),
    _OptIfODUkTtpSAPIExpected_Type()
)
optIfODUkTtpSAPIExpected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfODUkTtpSAPIExpected.setStatus("current")
_OptIfODUkTtpTraceIdentifierAccepted_Type = OptIfAcTI
_OptIfODUkTtpTraceIdentifierAccepted_Object = MibTableColumn
optIfODUkTtpTraceIdentifierAccepted = _OptIfODUkTtpTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2, 1, 4),
    _OptIfODUkTtpTraceIdentifierAccepted_Type()
)
optIfODUkTtpTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkTtpTraceIdentifierAccepted.setStatus("current")
_OptIfODUkTtpTIMDetMode_Type = OptIfTIMDetMode
_OptIfODUkTtpTIMDetMode_Object = MibTableColumn
optIfODUkTtpTIMDetMode = _OptIfODUkTtpTIMDetMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2, 1, 5),
    _OptIfODUkTtpTIMDetMode_Type()
)
optIfODUkTtpTIMDetMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfODUkTtpTIMDetMode.setStatus("current")
_OptIfODUkTtpTIMActEnabled_Type = TruthValue
_OptIfODUkTtpTIMActEnabled_Object = MibTableColumn
optIfODUkTtpTIMActEnabled = _OptIfODUkTtpTIMActEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2, 1, 6),
    _OptIfODUkTtpTIMActEnabled_Type()
)
optIfODUkTtpTIMActEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfODUkTtpTIMActEnabled.setStatus("current")
_OptIfODUkTtpDEGThr_Type = OptIfDEGThr
_OptIfODUkTtpDEGThr_Object = MibTableColumn
optIfODUkTtpDEGThr = _OptIfODUkTtpDEGThr_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2, 1, 7),
    _OptIfODUkTtpDEGThr_Type()
)
optIfODUkTtpDEGThr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfODUkTtpDEGThr.setStatus("current")
if mibBuilder.loadTexts:
    optIfODUkTtpDEGThr.setUnits("percentage")
_OptIfODUkTtpDEGM_Type = OptIfDEGM
_OptIfODUkTtpDEGM_Object = MibTableColumn
optIfODUkTtpDEGM = _OptIfODUkTtpDEGM_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2, 1, 8),
    _OptIfODUkTtpDEGM_Type()
)
optIfODUkTtpDEGM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optIfODUkTtpDEGM.setStatus("current")


class _OptIfODUkTtpCurrentStatus_Type(Bits):
    """Custom type optIfODUkTtpCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 4),
          ("deg", 3),
          ("lck", 1),
          ("oci", 0),
          ("ssf", 5),
          ("tim", 2))
    )

_OptIfODUkTtpCurrentStatus_Type.__name__ = "Bits"
_OptIfODUkTtpCurrentStatus_Object = MibTableColumn
optIfODUkTtpCurrentStatus = _OptIfODUkTtpCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 2, 1, 9),
    _OptIfODUkTtpCurrentStatus_Type()
)
optIfODUkTtpCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkTtpCurrentStatus.setStatus("current")
_OptIfODUkPositionSeqTable_Object = MibTable
optIfODUkPositionSeqTable = _OptIfODUkPositionSeqTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 3)
)
if mibBuilder.loadTexts:
    optIfODUkPositionSeqTable.setStatus("current")
_OptIfODUkPositionSeqEntry_Object = MibTableRow
optIfODUkPositionSeqEntry = _OptIfODUkPositionSeqEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 3, 1)
)
optIfODUkPositionSeqEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfODUkPositionSeqIndex"),
)
if mibBuilder.loadTexts:
    optIfODUkPositionSeqEntry.setStatus("current")


class _OptIfODUkPositionSeqIndex_Type(Unsigned32):
    """Custom type optIfODUkPositionSeqIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_OptIfODUkPositionSeqIndex_Type.__name__ = "Unsigned32"
_OptIfODUkPositionSeqIndex_Object = MibTableColumn
optIfODUkPositionSeqIndex = _OptIfODUkPositionSeqIndex_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 3, 1, 1),
    _OptIfODUkPositionSeqIndex_Type()
)
optIfODUkPositionSeqIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfODUkPositionSeqIndex.setStatus("current")
_OptIfODUkPositionSeqPosition_Type = Unsigned32
_OptIfODUkPositionSeqPosition_Object = MibTableColumn
optIfODUkPositionSeqPosition = _OptIfODUkPositionSeqPosition_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 3, 1, 2),
    _OptIfODUkPositionSeqPosition_Type()
)
optIfODUkPositionSeqPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkPositionSeqPosition.setStatus("current")
_OptIfODUkPositionSeqPointer_Type = RowPointer
_OptIfODUkPositionSeqPointer_Object = MibTableColumn
optIfODUkPositionSeqPointer = _OptIfODUkPositionSeqPointer_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 3, 1, 3),
    _OptIfODUkPositionSeqPointer_Type()
)
optIfODUkPositionSeqPointer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkPositionSeqPointer.setStatus("current")
_OptIfODUkNimConfigTable_Object = MibTable
optIfODUkNimConfigTable = _OptIfODUkNimConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4)
)
if mibBuilder.loadTexts:
    optIfODUkNimConfigTable.setStatus("current")
_OptIfODUkNimConfigEntry_Object = MibTableRow
optIfODUkNimConfigEntry = _OptIfODUkNimConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1)
)
optIfODUkNimConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfODUkNimDirectionality"),
)
if mibBuilder.loadTexts:
    optIfODUkNimConfigEntry.setStatus("current")
_OptIfODUkNimDirectionality_Type = OptIfSinkOrSource
_OptIfODUkNimDirectionality_Object = MibTableColumn
optIfODUkNimDirectionality = _OptIfODUkNimDirectionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1, 1),
    _OptIfODUkNimDirectionality_Type()
)
optIfODUkNimDirectionality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfODUkNimDirectionality.setStatus("current")
_OptIfODUkNimDAPIExpected_Type = OptIfExDAPI
_OptIfODUkNimDAPIExpected_Object = MibTableColumn
optIfODUkNimDAPIExpected = _OptIfODUkNimDAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1, 2),
    _OptIfODUkNimDAPIExpected_Type()
)
optIfODUkNimDAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkNimDAPIExpected.setStatus("current")
_OptIfODUkNimSAPIExpected_Type = OptIfExSAPI
_OptIfODUkNimSAPIExpected_Object = MibTableColumn
optIfODUkNimSAPIExpected = _OptIfODUkNimSAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1, 3),
    _OptIfODUkNimSAPIExpected_Type()
)
optIfODUkNimSAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkNimSAPIExpected.setStatus("current")
_OptIfODUkNimTraceIdentifierAccepted_Type = OptIfAcTI
_OptIfODUkNimTraceIdentifierAccepted_Object = MibTableColumn
optIfODUkNimTraceIdentifierAccepted = _OptIfODUkNimTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1, 4),
    _OptIfODUkNimTraceIdentifierAccepted_Type()
)
optIfODUkNimTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkNimTraceIdentifierAccepted.setStatus("current")
_OptIfODUkNimTIMDetMode_Type = OptIfTIMDetMode
_OptIfODUkNimTIMDetMode_Object = MibTableColumn
optIfODUkNimTIMDetMode = _OptIfODUkNimTIMDetMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1, 5),
    _OptIfODUkNimTIMDetMode_Type()
)
optIfODUkNimTIMDetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkNimTIMDetMode.setStatus("current")
_OptIfODUkNimTIMActEnabled_Type = TruthValue
_OptIfODUkNimTIMActEnabled_Object = MibTableColumn
optIfODUkNimTIMActEnabled = _OptIfODUkNimTIMActEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1, 6),
    _OptIfODUkNimTIMActEnabled_Type()
)
optIfODUkNimTIMActEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkNimTIMActEnabled.setStatus("current")
_OptIfODUkNimDEGThr_Type = OptIfDEGThr
_OptIfODUkNimDEGThr_Object = MibTableColumn
optIfODUkNimDEGThr = _OptIfODUkNimDEGThr_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1, 7),
    _OptIfODUkNimDEGThr_Type()
)
optIfODUkNimDEGThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkNimDEGThr.setStatus("current")
if mibBuilder.loadTexts:
    optIfODUkNimDEGThr.setUnits("percentage")
_OptIfODUkNimDEGM_Type = OptIfDEGM
_OptIfODUkNimDEGM_Object = MibTableColumn
optIfODUkNimDEGM = _OptIfODUkNimDEGM_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1, 8),
    _OptIfODUkNimDEGM_Type()
)
optIfODUkNimDEGM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkNimDEGM.setStatus("current")


class _OptIfODUkNimCurrentStatus_Type(Bits):
    """Custom type optIfODUkNimCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 4),
          ("deg", 3),
          ("lck", 1),
          ("oci", 0),
          ("ssf", 5),
          ("tim", 2))
    )

_OptIfODUkNimCurrentStatus_Type.__name__ = "Bits"
_OptIfODUkNimCurrentStatus_Object = MibTableColumn
optIfODUkNimCurrentStatus = _OptIfODUkNimCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1, 9),
    _OptIfODUkNimCurrentStatus_Type()
)
optIfODUkNimCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkNimCurrentStatus.setStatus("current")
_OptIfODUkNimRowStatus_Type = RowStatus
_OptIfODUkNimRowStatus_Object = MibTableColumn
optIfODUkNimRowStatus = _OptIfODUkNimRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 4, 1, 10),
    _OptIfODUkNimRowStatus_Type()
)
optIfODUkNimRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkNimRowStatus.setStatus("current")
_OptIfGCC12ConfigTable_Object = MibTable
optIfGCC12ConfigTable = _OptIfGCC12ConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 5)
)
if mibBuilder.loadTexts:
    optIfGCC12ConfigTable.setStatus("current")
_OptIfGCC12ConfigEntry_Object = MibTableRow
optIfGCC12ConfigEntry = _OptIfGCC12ConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 5, 1)
)
optIfGCC12ConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfGCC12Codirectional"),
    (0, "OPT-IF-MIB", "optIfGCC12GCCAccess"),
)
if mibBuilder.loadTexts:
    optIfGCC12ConfigEntry.setStatus("current")
_OptIfGCC12Codirectional_Type = TruthValue
_OptIfGCC12Codirectional_Object = MibTableColumn
optIfGCC12Codirectional = _OptIfGCC12Codirectional_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 5, 1, 1),
    _OptIfGCC12Codirectional_Type()
)
optIfGCC12Codirectional.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfGCC12Codirectional.setStatus("current")


class _OptIfGCC12GCCAccess_Type(Integer32):
    """Custom type optIfGCC12GCCAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("gcc1", 1),
          ("gcc1and2", 3),
          ("gcc2", 2))
    )


_OptIfGCC12GCCAccess_Type.__name__ = "Integer32"
_OptIfGCC12GCCAccess_Object = MibTableColumn
optIfGCC12GCCAccess = _OptIfGCC12GCCAccess_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 5, 1, 2),
    _OptIfGCC12GCCAccess_Type()
)
optIfGCC12GCCAccess.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfGCC12GCCAccess.setStatus("current")
_OptIfGCC12GCCPassThrough_Type = TruthValue
_OptIfGCC12GCCPassThrough_Object = MibTableColumn
optIfGCC12GCCPassThrough = _OptIfGCC12GCCPassThrough_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 5, 1, 3),
    _OptIfGCC12GCCPassThrough_Type()
)
optIfGCC12GCCPassThrough.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfGCC12GCCPassThrough.setStatus("current")
_OptIfGCC12Application_Type = SnmpAdminString
_OptIfGCC12Application_Object = MibTableColumn
optIfGCC12Application = _OptIfGCC12Application_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 5, 1, 4),
    _OptIfGCC12Application_Type()
)
optIfGCC12Application.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfGCC12Application.setStatus("current")
_OptIfGCC12RowStatus_Type = RowStatus
_OptIfGCC12RowStatus_Object = MibTableColumn
optIfGCC12RowStatus = _OptIfGCC12RowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 8, 5, 1, 5),
    _OptIfGCC12RowStatus_Type()
)
optIfGCC12RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfGCC12RowStatus.setStatus("current")
_OptIfODUkT_ObjectIdentity = ObjectIdentity
optIfODUkT = _OptIfODUkT_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9)
)
_OptIfODUkTConfigTable_Object = MibTable
optIfODUkTConfigTable = _OptIfODUkTConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1)
)
if mibBuilder.loadTexts:
    optIfODUkTConfigTable.setStatus("current")
_OptIfODUkTConfigEntry_Object = MibTableRow
optIfODUkTConfigEntry = _OptIfODUkTConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1)
)
optIfODUkTConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfODUkTTcmField"),
    (0, "OPT-IF-MIB", "optIfODUkTCodirectional"),
)
if mibBuilder.loadTexts:
    optIfODUkTConfigEntry.setStatus("current")


class _OptIfODUkTTcmField_Type(Unsigned32):
    """Custom type optIfODUkTTcmField based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_OptIfODUkTTcmField_Type.__name__ = "Unsigned32"
_OptIfODUkTTcmField_Object = MibTableColumn
optIfODUkTTcmField = _OptIfODUkTTcmField_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 1),
    _OptIfODUkTTcmField_Type()
)
optIfODUkTTcmField.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfODUkTTcmField.setStatus("current")
_OptIfODUkTCodirectional_Type = TruthValue
_OptIfODUkTCodirectional_Object = MibTableColumn
optIfODUkTCodirectional = _OptIfODUkTCodirectional_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 2),
    _OptIfODUkTCodirectional_Type()
)
optIfODUkTCodirectional.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfODUkTCodirectional.setStatus("current")
_OptIfODUkTTraceIdentifierTransmitted_Type = OptIfTxTI
_OptIfODUkTTraceIdentifierTransmitted_Object = MibTableColumn
optIfODUkTTraceIdentifierTransmitted = _OptIfODUkTTraceIdentifierTransmitted_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 3),
    _OptIfODUkTTraceIdentifierTransmitted_Type()
)
optIfODUkTTraceIdentifierTransmitted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTTraceIdentifierTransmitted.setStatus("current")
_OptIfODUkTDAPIExpected_Type = OptIfExDAPI
_OptIfODUkTDAPIExpected_Object = MibTableColumn
optIfODUkTDAPIExpected = _OptIfODUkTDAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 4),
    _OptIfODUkTDAPIExpected_Type()
)
optIfODUkTDAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTDAPIExpected.setStatus("current")
_OptIfODUkTSAPIExpected_Type = OptIfExSAPI
_OptIfODUkTSAPIExpected_Object = MibTableColumn
optIfODUkTSAPIExpected = _OptIfODUkTSAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 5),
    _OptIfODUkTSAPIExpected_Type()
)
optIfODUkTSAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTSAPIExpected.setStatus("current")
_OptIfODUkTTraceIdentifierAccepted_Type = OptIfAcTI
_OptIfODUkTTraceIdentifierAccepted_Object = MibTableColumn
optIfODUkTTraceIdentifierAccepted = _OptIfODUkTTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 6),
    _OptIfODUkTTraceIdentifierAccepted_Type()
)
optIfODUkTTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkTTraceIdentifierAccepted.setStatus("current")
_OptIfODUkTTIMDetMode_Type = OptIfTIMDetMode
_OptIfODUkTTIMDetMode_Object = MibTableColumn
optIfODUkTTIMDetMode = _OptIfODUkTTIMDetMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 7),
    _OptIfODUkTTIMDetMode_Type()
)
optIfODUkTTIMDetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTTIMDetMode.setStatus("current")
_OptIfODUkTTIMActEnabled_Type = TruthValue
_OptIfODUkTTIMActEnabled_Object = MibTableColumn
optIfODUkTTIMActEnabled = _OptIfODUkTTIMActEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 8),
    _OptIfODUkTTIMActEnabled_Type()
)
optIfODUkTTIMActEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTTIMActEnabled.setStatus("current")
_OptIfODUkTDEGThr_Type = OptIfDEGThr
_OptIfODUkTDEGThr_Object = MibTableColumn
optIfODUkTDEGThr = _OptIfODUkTDEGThr_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 9),
    _OptIfODUkTDEGThr_Type()
)
optIfODUkTDEGThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTDEGThr.setStatus("current")
if mibBuilder.loadTexts:
    optIfODUkTDEGThr.setUnits("percentage")
_OptIfODUkTDEGM_Type = OptIfDEGM
_OptIfODUkTDEGM_Object = MibTableColumn
optIfODUkTDEGM = _OptIfODUkTDEGM_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 10),
    _OptIfODUkTDEGM_Type()
)
optIfODUkTDEGM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTDEGM.setStatus("current")


class _OptIfODUkTSinkMode_Type(Integer32):
    """Custom type optIfODUkTSinkMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("monitor", 2),
          ("operational", 1))
    )


_OptIfODUkTSinkMode_Type.__name__ = "Integer32"
_OptIfODUkTSinkMode_Object = MibTableColumn
optIfODUkTSinkMode = _OptIfODUkTSinkMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 11),
    _OptIfODUkTSinkMode_Type()
)
optIfODUkTSinkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTSinkMode.setStatus("current")


class _OptIfODUkTSinkLockSignalAdminState_Type(Integer32):
    """Custom type optIfODUkTSinkLockSignalAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("normal", 2))
    )


_OptIfODUkTSinkLockSignalAdminState_Type.__name__ = "Integer32"
_OptIfODUkTSinkLockSignalAdminState_Object = MibTableColumn
optIfODUkTSinkLockSignalAdminState = _OptIfODUkTSinkLockSignalAdminState_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 12),
    _OptIfODUkTSinkLockSignalAdminState_Type()
)
optIfODUkTSinkLockSignalAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTSinkLockSignalAdminState.setStatus("current")


class _OptIfODUkTSourceLockSignalAdminState_Type(Integer32):
    """Custom type optIfODUkTSourceLockSignalAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("locked", 1),
          ("normal", 2))
    )


_OptIfODUkTSourceLockSignalAdminState_Type.__name__ = "Integer32"
_OptIfODUkTSourceLockSignalAdminState_Object = MibTableColumn
optIfODUkTSourceLockSignalAdminState = _OptIfODUkTSourceLockSignalAdminState_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 13),
    _OptIfODUkTSourceLockSignalAdminState_Type()
)
optIfODUkTSourceLockSignalAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTSourceLockSignalAdminState.setStatus("current")


class _OptIfODUkTCurrentStatus_Type(Bits):
    """Custom type optIfODUkTCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 4),
          ("deg", 3),
          ("lck", 1),
          ("oci", 0),
          ("ssf", 5),
          ("tim", 2))
    )

_OptIfODUkTCurrentStatus_Type.__name__ = "Bits"
_OptIfODUkTCurrentStatus_Object = MibTableColumn
optIfODUkTCurrentStatus = _OptIfODUkTCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 14),
    _OptIfODUkTCurrentStatus_Type()
)
optIfODUkTCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkTCurrentStatus.setStatus("current")
_OptIfODUkTRowStatus_Type = RowStatus
_OptIfODUkTRowStatus_Object = MibTableColumn
optIfODUkTRowStatus = _OptIfODUkTRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 1, 1, 15),
    _OptIfODUkTRowStatus_Type()
)
optIfODUkTRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTRowStatus.setStatus("current")
_OptIfODUkTNimConfigTable_Object = MibTable
optIfODUkTNimConfigTable = _OptIfODUkTNimConfigTable_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2)
)
if mibBuilder.loadTexts:
    optIfODUkTNimConfigTable.setStatus("current")
_OptIfODUkTNimConfigEntry_Object = MibTableRow
optIfODUkTNimConfigEntry = _OptIfODUkTNimConfigEntry_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1)
)
optIfODUkTNimConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "OPT-IF-MIB", "optIfODUkTNimTcmField"),
    (0, "OPT-IF-MIB", "optIfODUkTNimDirectionality"),
)
if mibBuilder.loadTexts:
    optIfODUkTNimConfigEntry.setStatus("current")


class _OptIfODUkTNimTcmField_Type(Unsigned32):
    """Custom type optIfODUkTNimTcmField based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_OptIfODUkTNimTcmField_Type.__name__ = "Unsigned32"
_OptIfODUkTNimTcmField_Object = MibTableColumn
optIfODUkTNimTcmField = _OptIfODUkTNimTcmField_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 1),
    _OptIfODUkTNimTcmField_Type()
)
optIfODUkTNimTcmField.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfODUkTNimTcmField.setStatus("current")
_OptIfODUkTNimDirectionality_Type = OptIfSinkOrSource
_OptIfODUkTNimDirectionality_Object = MibTableColumn
optIfODUkTNimDirectionality = _OptIfODUkTNimDirectionality_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 2),
    _OptIfODUkTNimDirectionality_Type()
)
optIfODUkTNimDirectionality.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    optIfODUkTNimDirectionality.setStatus("current")
_OptIfODUkTNimDAPIExpected_Type = OptIfExDAPI
_OptIfODUkTNimDAPIExpected_Object = MibTableColumn
optIfODUkTNimDAPIExpected = _OptIfODUkTNimDAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 3),
    _OptIfODUkTNimDAPIExpected_Type()
)
optIfODUkTNimDAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTNimDAPIExpected.setStatus("current")
_OptIfODUkTNimSAPIExpected_Type = OptIfExSAPI
_OptIfODUkTNimSAPIExpected_Object = MibTableColumn
optIfODUkTNimSAPIExpected = _OptIfODUkTNimSAPIExpected_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 4),
    _OptIfODUkTNimSAPIExpected_Type()
)
optIfODUkTNimSAPIExpected.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTNimSAPIExpected.setStatus("current")
_OptIfODUkTNimTraceIdentifierAccepted_Type = OptIfAcTI
_OptIfODUkTNimTraceIdentifierAccepted_Object = MibTableColumn
optIfODUkTNimTraceIdentifierAccepted = _OptIfODUkTNimTraceIdentifierAccepted_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 5),
    _OptIfODUkTNimTraceIdentifierAccepted_Type()
)
optIfODUkTNimTraceIdentifierAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkTNimTraceIdentifierAccepted.setStatus("current")
_OptIfODUkTNimTIMDetMode_Type = OptIfTIMDetMode
_OptIfODUkTNimTIMDetMode_Object = MibTableColumn
optIfODUkTNimTIMDetMode = _OptIfODUkTNimTIMDetMode_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 6),
    _OptIfODUkTNimTIMDetMode_Type()
)
optIfODUkTNimTIMDetMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTNimTIMDetMode.setStatus("current")
_OptIfODUkTNimTIMActEnabled_Type = TruthValue
_OptIfODUkTNimTIMActEnabled_Object = MibTableColumn
optIfODUkTNimTIMActEnabled = _OptIfODUkTNimTIMActEnabled_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 7),
    _OptIfODUkTNimTIMActEnabled_Type()
)
optIfODUkTNimTIMActEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTNimTIMActEnabled.setStatus("current")
_OptIfODUkTNimDEGThr_Type = OptIfDEGThr
_OptIfODUkTNimDEGThr_Object = MibTableColumn
optIfODUkTNimDEGThr = _OptIfODUkTNimDEGThr_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 8),
    _OptIfODUkTNimDEGThr_Type()
)
optIfODUkTNimDEGThr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTNimDEGThr.setStatus("current")
if mibBuilder.loadTexts:
    optIfODUkTNimDEGThr.setUnits("percentage")
_OptIfODUkTNimDEGM_Type = OptIfDEGM
_OptIfODUkTNimDEGM_Object = MibTableColumn
optIfODUkTNimDEGM = _OptIfODUkTNimDEGM_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 9),
    _OptIfODUkTNimDEGM_Type()
)
optIfODUkTNimDEGM.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTNimDEGM.setStatus("current")


class _OptIfODUkTNimCurrentStatus_Type(Bits):
    """Custom type optIfODUkTNimCurrentStatus based on Bits"""
    namedValues = NamedValues(
        *(("bdi", 4),
          ("deg", 3),
          ("lck", 1),
          ("oci", 0),
          ("ssf", 5),
          ("tim", 2))
    )

_OptIfODUkTNimCurrentStatus_Type.__name__ = "Bits"
_OptIfODUkTNimCurrentStatus_Object = MibTableColumn
optIfODUkTNimCurrentStatus = _OptIfODUkTNimCurrentStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 10),
    _OptIfODUkTNimCurrentStatus_Type()
)
optIfODUkTNimCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optIfODUkTNimCurrentStatus.setStatus("current")
_OptIfODUkTNimRowStatus_Type = RowStatus
_OptIfODUkTNimRowStatus_Object = MibTableColumn
optIfODUkTNimRowStatus = _OptIfODUkTNimRowStatus_Object(
    (1, 3, 6, 1, 2, 1, 10, 133, 1, 9, 2, 1, 11),
    _OptIfODUkTNimRowStatus_Type()
)
optIfODUkTNimRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optIfODUkTNimRowStatus.setStatus("current")
_OptIfConfs_ObjectIdentity = ObjectIdentity
optIfConfs = _OptIfConfs_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 2)
)
_OptIfGroups_ObjectIdentity = ObjectIdentity
optIfGroups = _OptIfGroups_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1)
)
_OptIfCompl_ObjectIdentity = ObjectIdentity
optIfCompl = _OptIfCompl_ObjectIdentity(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 2)
)

# Managed Objects groups

optIfOTMnGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 1)
)
optIfOTMnGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOTMnOrder"),
        ("OPT-IF-MIB", "optIfOTMnReduced"),
        ("OPT-IF-MIB", "optIfOTMnBitRates"),
        ("OPT-IF-MIB", "optIfOTMnInterfaceType"),
        ("OPT-IF-MIB", "optIfOTMnTcmMax"),
        ("OPT-IF-MIB", "optIfOTMnOpticalReach"))
)
if mibBuilder.loadTexts:
    optIfOTMnGroup.setStatus("current")

optIfPerfMonGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 2)
)
optIfPerfMonGroup.setObjects(
      *(("OPT-IF-MIB", "optIfPerfMonCurrentTimeElapsed"),
        ("OPT-IF-MIB", "optIfPerfMonCurDayTimeElapsed"),
        ("OPT-IF-MIB", "optIfPerfMonIntervalNumIntervals"),
        ("OPT-IF-MIB", "optIfPerfMonIntervalNumInvalidIntervals"))
)
if mibBuilder.loadTexts:
    optIfPerfMonGroup.setStatus("current")

optIfOTSnCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 3)
)
optIfOTSnCommonGroup.setObjects(
    ("OPT-IF-MIB", "optIfOTSnDirectionality")
)
if mibBuilder.loadTexts:
    optIfOTSnCommonGroup.setStatus("current")

optIfOTSnSourceGroupFull = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 4)
)
optIfOTSnSourceGroupFull.setObjects(
    ("OPT-IF-MIB", "optIfOTSnTraceIdentifierTransmitted")
)
if mibBuilder.loadTexts:
    optIfOTSnSourceGroupFull.setStatus("current")

optIfOTSnAPRStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 5)
)
optIfOTSnAPRStatusGroup.setObjects(
    ("OPT-IF-MIB", "optIfOTSnAprStatus")
)
if mibBuilder.loadTexts:
    optIfOTSnAPRStatusGroup.setStatus("current")

optIfOTSnAPRControlGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 6)
)
optIfOTSnAPRControlGroup.setObjects(
    ("OPT-IF-MIB", "optIfOTSnAprControl")
)
if mibBuilder.loadTexts:
    optIfOTSnAPRControlGroup.setStatus("current")

optIfOTSnSinkGroupBasic = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 7)
)
optIfOTSnSinkGroupBasic.setObjects(
    ("OPT-IF-MIB", "optIfOTSnCurrentStatus")
)
if mibBuilder.loadTexts:
    optIfOTSnSinkGroupBasic.setStatus("current")

optIfOTSnSinkGroupFull = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 8)
)
optIfOTSnSinkGroupFull.setObjects(
      *(("OPT-IF-MIB", "optIfOTSnDAPIExpected"),
        ("OPT-IF-MIB", "optIfOTSnSAPIExpected"),
        ("OPT-IF-MIB", "optIfOTSnTraceIdentifierAccepted"),
        ("OPT-IF-MIB", "optIfOTSnTIMDetMode"),
        ("OPT-IF-MIB", "optIfOTSnTIMActEnabled"))
)
if mibBuilder.loadTexts:
    optIfOTSnSinkGroupFull.setStatus("current")

optIfOTSnSinkPreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 9)
)
optIfOTSnSinkPreOtnPMGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOTSnSinkCurrentSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurrentInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurrentLowInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurrentHighInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurrentOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurrentLowOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurrentHighOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkIntervalSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOTSnSinkIntervalLastInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkIntervalLowInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkIntervalHighInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkIntervalLastOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkIntervalLowOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkIntervalHighOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurDayLowInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurDayHighInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurDayHighOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkPrevDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOTSnSinkPrevDayLastInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkPrevDayLowInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkPrevDayHighInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkPrevDayLastOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkPrevDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSinkPrevDayHighOutputPower"))
)
if mibBuilder.loadTexts:
    optIfOTSnSinkPreOtnPMGroup.setStatus("current")

optIfOTSnSinkPreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 10)
)
optIfOTSnSinkPreOtnPMThresholdGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOTSnSinkCurrentLowerInputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurrentUpperInputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurrentLowerOutputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOTSnSinkCurrentUpperOutputPowerThreshold"))
)
if mibBuilder.loadTexts:
    optIfOTSnSinkPreOtnPMThresholdGroup.setStatus("current")

optIfOTSnSourcePreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 11)
)
optIfOTSnSourcePreOtnPMGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOTSnSrcCurrentSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurrentOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurrentLowOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurrentHighOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurrentInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurrentLowInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurrentHighInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcIntervalSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOTSnSrcIntervalLastOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcIntervalLowOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcIntervalHighOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcIntervalLastInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcIntervalLowInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcIntervalHighInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurDayHighOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurDayLowInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurDayHighInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcPrevDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOTSnSrcPrevDayLastOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcPrevDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcPrevDayHighOutputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcPrevDayLastInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcPrevDayLowInputPower"),
        ("OPT-IF-MIB", "optIfOTSnSrcPrevDayHighInputPower"))
)
if mibBuilder.loadTexts:
    optIfOTSnSourcePreOtnPMGroup.setStatus("current")

optIfOTSnSourcePreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 12)
)
optIfOTSnSourcePreOtnPMThresholdGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOTSnSrcCurrentLowerOutputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurrentUpperOutputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurrentLowerInputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOTSnSrcCurrentUpperInputPowerThreshold"))
)
if mibBuilder.loadTexts:
    optIfOTSnSourcePreOtnPMThresholdGroup.setStatus("current")

optIfOMSnCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 13)
)
optIfOMSnCommonGroup.setObjects(
    ("OPT-IF-MIB", "optIfOMSnDirectionality")
)
if mibBuilder.loadTexts:
    optIfOMSnCommonGroup.setStatus("current")

optIfOMSnSinkGroupBasic = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 14)
)
optIfOMSnSinkGroupBasic.setObjects(
    ("OPT-IF-MIB", "optIfOMSnCurrentStatus")
)
if mibBuilder.loadTexts:
    optIfOMSnSinkGroupBasic.setStatus("current")

optIfOMSnSinkPreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 15)
)
optIfOMSnSinkPreOtnPMGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOMSnSinkCurrentSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurrentAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurrentLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurrentHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurrentOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurrentLowOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurrentHighOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkIntervalSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOMSnSinkIntervalLastAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkIntervalLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkIntervalHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkIntervalLastOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkIntervalLowOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkIntervalHighOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurDayLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurDayHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurDayHighOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkPrevDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOMSnSinkPrevDayLastAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkPrevDayLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkPrevDayHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkPrevDayLastOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkPrevDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSinkPrevDayHighOutputPower"))
)
if mibBuilder.loadTexts:
    optIfOMSnSinkPreOtnPMGroup.setStatus("current")

optIfOMSnSinkPreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 16)
)
optIfOMSnSinkPreOtnPMThresholdGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOMSnSinkCurrentLowerInputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurrentUpperInputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurrentLowerOutputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOMSnSinkCurrentUpperOutputPowerThreshold"))
)
if mibBuilder.loadTexts:
    optIfOMSnSinkPreOtnPMThresholdGroup.setStatus("current")

optIfOMSnSourcePreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 17)
)
optIfOMSnSourcePreOtnPMGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOMSnSrcCurrentSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurrentOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurrentLowOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurrentHighOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurrentAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurrentLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurrentHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcIntervalSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOMSnSrcIntervalLastOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcIntervalLowOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcIntervalHighOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcIntervalLastAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcIntervalLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcIntervalHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurDayHighOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurDayLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurDayHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcPrevDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOMSnSrcPrevDayLastOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcPrevDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcPrevDayHighOutputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcPrevDayLastAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcPrevDayLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOMSnSrcPrevDayHighAggregatedInputPower"))
)
if mibBuilder.loadTexts:
    optIfOMSnSourcePreOtnPMGroup.setStatus("current")

optIfOMSnSourcePreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 18)
)
optIfOMSnSourcePreOtnPMThresholdGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOMSnSrcCurrentLowerOutputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurrentUpperOutputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurrentLowerInputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOMSnSrcCurrentUpperInputPowerThreshold"))
)
if mibBuilder.loadTexts:
    optIfOMSnSourcePreOtnPMThresholdGroup.setStatus("current")

optIfOChGroupCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 19)
)
optIfOChGroupCommonGroup.setObjects(
    ("OPT-IF-MIB", "optIfOChGroupDirectionality")
)
if mibBuilder.loadTexts:
    optIfOChGroupCommonGroup.setStatus("current")

optIfOChGroupSinkPreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 20)
)
optIfOChGroupSinkPreOtnPMGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOChGroupSinkCurrentSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurrentAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurrentLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurrentHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurrentOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurrentLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurrentHighOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkIntervalSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChGroupSinkIntervalLastAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkIntervalLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkIntervalHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkIntervalLastOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkIntervalLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkIntervalHighOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurDayLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurDayHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurDayHighOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkPrevDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChGroupSinkPrevDayLastAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkPrevDayLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkPrevDayHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkPrevDayLastOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkPrevDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSinkPrevDayHighOutputPower"))
)
if mibBuilder.loadTexts:
    optIfOChGroupSinkPreOtnPMGroup.setStatus("current")

optIfOChGroupSinkPreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 21)
)
optIfOChGroupSinkPreOtnPMThresholdGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOChGroupSinkCurrentLowerInputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurrentUpperInputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurrentLowerOutputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOChGroupSinkCurrentUpperOutputPowerThreshold"))
)
if mibBuilder.loadTexts:
    optIfOChGroupSinkPreOtnPMThresholdGroup.setStatus("current")

optIfOChGroupSourcePreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 22)
)
optIfOChGroupSourcePreOtnPMGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOChGroupSrcCurrentSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurrentOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurrentLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurrentHighOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurrentAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurrentLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurrentHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcIntervalSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChGroupSrcIntervalLastOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcIntervalLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcIntervalHighOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcIntervalLastAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcIntervalLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcIntervalHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurDayHighOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurDayLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurDayHighAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcPrevDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChGroupSrcPrevDayLastOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcPrevDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcPrevDayHighOutputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcPrevDayLastAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcPrevDayLowAggregatedInputPower"),
        ("OPT-IF-MIB", "optIfOChGroupSrcPrevDayHighAggregatedInputPower"))
)
if mibBuilder.loadTexts:
    optIfOChGroupSourcePreOtnPMGroup.setStatus("current")

optIfOChGroupSourcePreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 23)
)
optIfOChGroupSourcePreOtnPMThresholdGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOChGroupSrcCurrentLowerOutputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurrentUpperOutputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurrentLowerInputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOChGroupSrcCurrentUpperInputPowerThreshold"))
)
if mibBuilder.loadTexts:
    optIfOChGroupSourcePreOtnPMThresholdGroup.setStatus("current")

optIfOChCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 24)
)
optIfOChCommonGroup.setObjects(
    ("OPT-IF-MIB", "optIfOChDirectionality")
)
if mibBuilder.loadTexts:
    optIfOChCommonGroup.setStatus("current")

optIfOChSinkGroupBasic = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 25)
)
optIfOChSinkGroupBasic.setObjects(
    ("OPT-IF-MIB", "optIfOChCurrentStatus")
)
if mibBuilder.loadTexts:
    optIfOChSinkGroupBasic.setStatus("current")

optIfOChSinkPreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 26)
)
optIfOChSinkPreOtnPMGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOChSinkCurrentSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChSinkCurrentInputPower"),
        ("OPT-IF-MIB", "optIfOChSinkCurrentLowInputPower"),
        ("OPT-IF-MIB", "optIfOChSinkCurrentHighInputPower"),
        ("OPT-IF-MIB", "optIfOChSinkIntervalSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChSinkIntervalLastInputPower"),
        ("OPT-IF-MIB", "optIfOChSinkIntervalLowInputPower"),
        ("OPT-IF-MIB", "optIfOChSinkIntervalHighInputPower"),
        ("OPT-IF-MIB", "optIfOChSinkCurDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChSinkCurDayLowInputPower"),
        ("OPT-IF-MIB", "optIfOChSinkCurDayHighInputPower"),
        ("OPT-IF-MIB", "optIfOChSinkPrevDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChSinkPrevDayLastInputPower"),
        ("OPT-IF-MIB", "optIfOChSinkPrevDayLowInputPower"),
        ("OPT-IF-MIB", "optIfOChSinkPrevDayHighInputPower"))
)
if mibBuilder.loadTexts:
    optIfOChSinkPreOtnPMGroup.setStatus("current")

optIfOChSinkPreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 27)
)
optIfOChSinkPreOtnPMThresholdGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOChSinkCurrentLowerInputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOChSinkCurrentUpperInputPowerThreshold"))
)
if mibBuilder.loadTexts:
    optIfOChSinkPreOtnPMThresholdGroup.setStatus("current")

optIfOChSourcePreOtnPMGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 28)
)
optIfOChSourcePreOtnPMGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOChSrcCurrentSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChSrcCurrentOutputPower"),
        ("OPT-IF-MIB", "optIfOChSrcCurrentLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChSrcCurrentHighOutputPower"),
        ("OPT-IF-MIB", "optIfOChSrcIntervalSuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChSrcIntervalLastOutputPower"),
        ("OPT-IF-MIB", "optIfOChSrcIntervalLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChSrcIntervalHighOutputPower"),
        ("OPT-IF-MIB", "optIfOChSrcCurDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChSrcCurDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChSrcCurDayHighOutputPower"),
        ("OPT-IF-MIB", "optIfOChSrcPrevDaySuspectedFlag"),
        ("OPT-IF-MIB", "optIfOChSrcPrevDayLastOutputPower"),
        ("OPT-IF-MIB", "optIfOChSrcPrevDayLowOutputPower"),
        ("OPT-IF-MIB", "optIfOChSrcPrevDayHighOutputPower"))
)
if mibBuilder.loadTexts:
    optIfOChSourcePreOtnPMGroup.setStatus("current")

optIfOChSourcePreOtnPMThresholdGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 29)
)
optIfOChSourcePreOtnPMThresholdGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOChSrcCurrentLowerOutputPowerThreshold"),
        ("OPT-IF-MIB", "optIfOChSrcCurrentUpperOutputPowerThreshold"))
)
if mibBuilder.loadTexts:
    optIfOChSourcePreOtnPMThresholdGroup.setStatus("current")

optIfOTUkCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 30)
)
optIfOTUkCommonGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOTUkDirectionality"),
        ("OPT-IF-MIB", "optIfOTUkBitRateK"))
)
if mibBuilder.loadTexts:
    optIfOTUkCommonGroup.setStatus("current")

optIfOTUkSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 31)
)
optIfOTUkSourceGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOTUkTraceIdentifierTransmitted"),
        ("OPT-IF-MIB", "optIfOTUkSourceAdaptActive"))
)
if mibBuilder.loadTexts:
    optIfOTUkSourceGroup.setStatus("current")

optIfOTUkSinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 32)
)
optIfOTUkSinkGroup.setObjects(
      *(("OPT-IF-MIB", "optIfOTUkDAPIExpected"),
        ("OPT-IF-MIB", "optIfOTUkSAPIExpected"),
        ("OPT-IF-MIB", "optIfOTUkTraceIdentifierAccepted"),
        ("OPT-IF-MIB", "optIfOTUkTIMDetMode"),
        ("OPT-IF-MIB", "optIfOTUkTIMActEnabled"),
        ("OPT-IF-MIB", "optIfOTUkDEGThr"),
        ("OPT-IF-MIB", "optIfOTUkDEGM"),
        ("OPT-IF-MIB", "optIfOTUkSinkAdaptActive"),
        ("OPT-IF-MIB", "optIfOTUkSinkFECEnabled"),
        ("OPT-IF-MIB", "optIfOTUkCurrentStatus"))
)
if mibBuilder.loadTexts:
    optIfOTUkSinkGroup.setStatus("current")

optIfGCC0Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 33)
)
optIfGCC0Group.setObjects(
      *(("OPT-IF-MIB", "optIfGCC0Application"),
        ("OPT-IF-MIB", "optIfGCC0RowStatus"))
)
if mibBuilder.loadTexts:
    optIfGCC0Group.setStatus("current")

optIfODUkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 34)
)
optIfODUkGroup.setObjects(
      *(("OPT-IF-MIB", "optIfODUkDirectionality"),
        ("OPT-IF-MIB", "optIfODUkBitRateK"),
        ("OPT-IF-MIB", "optIfODUkTcmFieldsInUse"),
        ("OPT-IF-MIB", "optIfODUkPositionSeqCurrentSize"),
        ("OPT-IF-MIB", "optIfODUkPositionSeqPosition"),
        ("OPT-IF-MIB", "optIfODUkPositionSeqPointer"),
        ("OPT-IF-MIB", "optIfODUkTtpPresent"))
)
if mibBuilder.loadTexts:
    optIfODUkGroup.setStatus("current")

optIfODUkTtpSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 35)
)
optIfODUkTtpSourceGroup.setObjects(
    ("OPT-IF-MIB", "optIfODUkTtpTraceIdentifierTransmitted")
)
if mibBuilder.loadTexts:
    optIfODUkTtpSourceGroup.setStatus("current")

optIfODUkTtpSinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 36)
)
optIfODUkTtpSinkGroup.setObjects(
      *(("OPT-IF-MIB", "optIfODUkTtpDAPIExpected"),
        ("OPT-IF-MIB", "optIfODUkTtpSAPIExpected"),
        ("OPT-IF-MIB", "optIfODUkTtpTraceIdentifierAccepted"),
        ("OPT-IF-MIB", "optIfODUkTtpTIMDetMode"),
        ("OPT-IF-MIB", "optIfODUkTtpTIMActEnabled"),
        ("OPT-IF-MIB", "optIfODUkTtpDEGThr"),
        ("OPT-IF-MIB", "optIfODUkTtpDEGM"),
        ("OPT-IF-MIB", "optIfODUkTtpCurrentStatus"))
)
if mibBuilder.loadTexts:
    optIfODUkTtpSinkGroup.setStatus("current")

optIfODUkNimGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 37)
)
optIfODUkNimGroup.setObjects(
      *(("OPT-IF-MIB", "optIfODUkNimDAPIExpected"),
        ("OPT-IF-MIB", "optIfODUkNimSAPIExpected"),
        ("OPT-IF-MIB", "optIfODUkNimTraceIdentifierAccepted"),
        ("OPT-IF-MIB", "optIfODUkNimTIMDetMode"),
        ("OPT-IF-MIB", "optIfODUkNimTIMActEnabled"),
        ("OPT-IF-MIB", "optIfODUkNimDEGThr"),
        ("OPT-IF-MIB", "optIfODUkNimDEGM"),
        ("OPT-IF-MIB", "optIfODUkNimCurrentStatus"),
        ("OPT-IF-MIB", "optIfODUkNimRowStatus"))
)
if mibBuilder.loadTexts:
    optIfODUkNimGroup.setStatus("current")

optIfGCC12Group = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 38)
)
optIfGCC12Group.setObjects(
      *(("OPT-IF-MIB", "optIfGCC12GCCPassThrough"),
        ("OPT-IF-MIB", "optIfGCC12Application"),
        ("OPT-IF-MIB", "optIfGCC12RowStatus"))
)
if mibBuilder.loadTexts:
    optIfGCC12Group.setStatus("current")

optIfODUkTCommonGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 39)
)
optIfODUkTCommonGroup.setObjects(
    ("OPT-IF-MIB", "optIfODUkTRowStatus")
)
if mibBuilder.loadTexts:
    optIfODUkTCommonGroup.setStatus("current")

optIfODUkTSourceGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 40)
)
optIfODUkTSourceGroup.setObjects(
      *(("OPT-IF-MIB", "optIfODUkTTraceIdentifierTransmitted"),
        ("OPT-IF-MIB", "optIfODUkTSourceLockSignalAdminState"))
)
if mibBuilder.loadTexts:
    optIfODUkTSourceGroup.setStatus("current")

optIfODUkTSinkGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 41)
)
optIfODUkTSinkGroup.setObjects(
      *(("OPT-IF-MIB", "optIfODUkTDAPIExpected"),
        ("OPT-IF-MIB", "optIfODUkTSAPIExpected"),
        ("OPT-IF-MIB", "optIfODUkTTraceIdentifierAccepted"),
        ("OPT-IF-MIB", "optIfODUkTTIMDetMode"),
        ("OPT-IF-MIB", "optIfODUkTTIMActEnabled"),
        ("OPT-IF-MIB", "optIfODUkTDEGThr"),
        ("OPT-IF-MIB", "optIfODUkTDEGM"),
        ("OPT-IF-MIB", "optIfODUkTCurrentStatus"))
)
if mibBuilder.loadTexts:
    optIfODUkTSinkGroup.setStatus("current")

optIfODUkTSinkGroupCtp = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 42)
)
optIfODUkTSinkGroupCtp.setObjects(
      *(("OPT-IF-MIB", "optIfODUkTSinkMode"),
        ("OPT-IF-MIB", "optIfODUkTSinkLockSignalAdminState"))
)
if mibBuilder.loadTexts:
    optIfODUkTSinkGroupCtp.setStatus("current")

optIfODUkTNimGroup = ObjectGroup(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 1, 43)
)
optIfODUkTNimGroup.setObjects(
      *(("OPT-IF-MIB", "optIfODUkTNimDAPIExpected"),
        ("OPT-IF-MIB", "optIfODUkTNimSAPIExpected"),
        ("OPT-IF-MIB", "optIfODUkTNimTraceIdentifierAccepted"),
        ("OPT-IF-MIB", "optIfODUkTNimTIMDetMode"),
        ("OPT-IF-MIB", "optIfODUkTNimTIMActEnabled"),
        ("OPT-IF-MIB", "optIfODUkTNimDEGThr"),
        ("OPT-IF-MIB", "optIfODUkTNimDEGM"),
        ("OPT-IF-MIB", "optIfODUkTNimCurrentStatus"),
        ("OPT-IF-MIB", "optIfODUkTNimRowStatus"))
)
if mibBuilder.loadTexts:
    optIfODUkTNimGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

optIfOtnConfigCompl = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 2, 1)
)
if mibBuilder.loadTexts:
    optIfOtnConfigCompl.setStatus(
        "current"
    )

optIfPreOtnPMCompl = ModuleCompliance(
    (1, 3, 6, 1, 2, 1, 10, 133, 2, 2, 2)
)
if mibBuilder.loadTexts:
    optIfPreOtnPMCompl.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OPT-IF-MIB",
    **{"OptIfAcTI": OptIfAcTI,
       "OptIfBitRateK": OptIfBitRateK,
       "OptIfDEGM": OptIfDEGM,
       "OptIfDEGThr": OptIfDEGThr,
       "OptIfDirectionality": OptIfDirectionality,
       "OptIfSinkOrSource": OptIfSinkOrSource,
       "OptIfExDAPI": OptIfExDAPI,
       "OptIfExSAPI": OptIfExSAPI,
       "OptIfIntervalNumber": OptIfIntervalNumber,
       "OptIfTIMDetMode": OptIfTIMDetMode,
       "OptIfTxTI": OptIfTxTI,
       "optIfMibModule": optIfMibModule,
       "optIfObjects": optIfObjects,
       "optIfOTMn": optIfOTMn,
       "optIfOTMnTable": optIfOTMnTable,
       "optIfOTMnEntry": optIfOTMnEntry,
       "optIfOTMnOrder": optIfOTMnOrder,
       "optIfOTMnReduced": optIfOTMnReduced,
       "optIfOTMnBitRates": optIfOTMnBitRates,
       "optIfOTMnInterfaceType": optIfOTMnInterfaceType,
       "optIfOTMnTcmMax": optIfOTMnTcmMax,
       "optIfOTMnOpticalReach": optIfOTMnOpticalReach,
       "optIfPerfMon": optIfPerfMon,
       "optIfPerfMonIntervalTable": optIfPerfMonIntervalTable,
       "optIfPerfMonIntervalEntry": optIfPerfMonIntervalEntry,
       "optIfPerfMonCurrentTimeElapsed": optIfPerfMonCurrentTimeElapsed,
       "optIfPerfMonCurDayTimeElapsed": optIfPerfMonCurDayTimeElapsed,
       "optIfPerfMonIntervalNumIntervals": optIfPerfMonIntervalNumIntervals,
       "optIfPerfMonIntervalNumInvalidIntervals": optIfPerfMonIntervalNumInvalidIntervals,
       "optIfOTSn": optIfOTSn,
       "optIfOTSnConfigTable": optIfOTSnConfigTable,
       "optIfOTSnConfigEntry": optIfOTSnConfigEntry,
       "optIfOTSnDirectionality": optIfOTSnDirectionality,
       "optIfOTSnAprStatus": optIfOTSnAprStatus,
       "optIfOTSnAprControl": optIfOTSnAprControl,
       "optIfOTSnTraceIdentifierTransmitted": optIfOTSnTraceIdentifierTransmitted,
       "optIfOTSnDAPIExpected": optIfOTSnDAPIExpected,
       "optIfOTSnSAPIExpected": optIfOTSnSAPIExpected,
       "optIfOTSnTraceIdentifierAccepted": optIfOTSnTraceIdentifierAccepted,
       "optIfOTSnTIMDetMode": optIfOTSnTIMDetMode,
       "optIfOTSnTIMActEnabled": optIfOTSnTIMActEnabled,
       "optIfOTSnCurrentStatus": optIfOTSnCurrentStatus,
       "optIfOTSnSinkCurrentTable": optIfOTSnSinkCurrentTable,
       "optIfOTSnSinkCurrentEntry": optIfOTSnSinkCurrentEntry,
       "optIfOTSnSinkCurrentSuspectedFlag": optIfOTSnSinkCurrentSuspectedFlag,
       "optIfOTSnSinkCurrentInputPower": optIfOTSnSinkCurrentInputPower,
       "optIfOTSnSinkCurrentLowInputPower": optIfOTSnSinkCurrentLowInputPower,
       "optIfOTSnSinkCurrentHighInputPower": optIfOTSnSinkCurrentHighInputPower,
       "optIfOTSnSinkCurrentLowerInputPowerThreshold": optIfOTSnSinkCurrentLowerInputPowerThreshold,
       "optIfOTSnSinkCurrentUpperInputPowerThreshold": optIfOTSnSinkCurrentUpperInputPowerThreshold,
       "optIfOTSnSinkCurrentOutputPower": optIfOTSnSinkCurrentOutputPower,
       "optIfOTSnSinkCurrentLowOutputPower": optIfOTSnSinkCurrentLowOutputPower,
       "optIfOTSnSinkCurrentHighOutputPower": optIfOTSnSinkCurrentHighOutputPower,
       "optIfOTSnSinkCurrentLowerOutputPowerThreshold": optIfOTSnSinkCurrentLowerOutputPowerThreshold,
       "optIfOTSnSinkCurrentUpperOutputPowerThreshold": optIfOTSnSinkCurrentUpperOutputPowerThreshold,
       "optIfOTSnSinkIntervalTable": optIfOTSnSinkIntervalTable,
       "optIfOTSnSinkIntervalEntry": optIfOTSnSinkIntervalEntry,
       "optIfOTSnSinkIntervalNumber": optIfOTSnSinkIntervalNumber,
       "optIfOTSnSinkIntervalSuspectedFlag": optIfOTSnSinkIntervalSuspectedFlag,
       "optIfOTSnSinkIntervalLastInputPower": optIfOTSnSinkIntervalLastInputPower,
       "optIfOTSnSinkIntervalLowInputPower": optIfOTSnSinkIntervalLowInputPower,
       "optIfOTSnSinkIntervalHighInputPower": optIfOTSnSinkIntervalHighInputPower,
       "optIfOTSnSinkIntervalLastOutputPower": optIfOTSnSinkIntervalLastOutputPower,
       "optIfOTSnSinkIntervalLowOutputPower": optIfOTSnSinkIntervalLowOutputPower,
       "optIfOTSnSinkIntervalHighOutputPower": optIfOTSnSinkIntervalHighOutputPower,
       "optIfOTSnSinkCurDayTable": optIfOTSnSinkCurDayTable,
       "optIfOTSnSinkCurDayEntry": optIfOTSnSinkCurDayEntry,
       "optIfOTSnSinkCurDaySuspectedFlag": optIfOTSnSinkCurDaySuspectedFlag,
       "optIfOTSnSinkCurDayLowInputPower": optIfOTSnSinkCurDayLowInputPower,
       "optIfOTSnSinkCurDayHighInputPower": optIfOTSnSinkCurDayHighInputPower,
       "optIfOTSnSinkCurDayLowOutputPower": optIfOTSnSinkCurDayLowOutputPower,
       "optIfOTSnSinkCurDayHighOutputPower": optIfOTSnSinkCurDayHighOutputPower,
       "optIfOTSnSinkPrevDayTable": optIfOTSnSinkPrevDayTable,
       "optIfOTSnSinkPrevDayEntry": optIfOTSnSinkPrevDayEntry,
       "optIfOTSnSinkPrevDaySuspectedFlag": optIfOTSnSinkPrevDaySuspectedFlag,
       "optIfOTSnSinkPrevDayLastInputPower": optIfOTSnSinkPrevDayLastInputPower,
       "optIfOTSnSinkPrevDayLowInputPower": optIfOTSnSinkPrevDayLowInputPower,
       "optIfOTSnSinkPrevDayHighInputPower": optIfOTSnSinkPrevDayHighInputPower,
       "optIfOTSnSinkPrevDayLastOutputPower": optIfOTSnSinkPrevDayLastOutputPower,
       "optIfOTSnSinkPrevDayLowOutputPower": optIfOTSnSinkPrevDayLowOutputPower,
       "optIfOTSnSinkPrevDayHighOutputPower": optIfOTSnSinkPrevDayHighOutputPower,
       "optIfOTSnSrcCurrentTable": optIfOTSnSrcCurrentTable,
       "optIfOTSnSrcCurrentEntry": optIfOTSnSrcCurrentEntry,
       "optIfOTSnSrcCurrentSuspectedFlag": optIfOTSnSrcCurrentSuspectedFlag,
       "optIfOTSnSrcCurrentOutputPower": optIfOTSnSrcCurrentOutputPower,
       "optIfOTSnSrcCurrentLowOutputPower": optIfOTSnSrcCurrentLowOutputPower,
       "optIfOTSnSrcCurrentHighOutputPower": optIfOTSnSrcCurrentHighOutputPower,
       "optIfOTSnSrcCurrentLowerOutputPowerThreshold": optIfOTSnSrcCurrentLowerOutputPowerThreshold,
       "optIfOTSnSrcCurrentUpperOutputPowerThreshold": optIfOTSnSrcCurrentUpperOutputPowerThreshold,
       "optIfOTSnSrcCurrentInputPower": optIfOTSnSrcCurrentInputPower,
       "optIfOTSnSrcCurrentLowInputPower": optIfOTSnSrcCurrentLowInputPower,
       "optIfOTSnSrcCurrentHighInputPower": optIfOTSnSrcCurrentHighInputPower,
       "optIfOTSnSrcCurrentLowerInputPowerThreshold": optIfOTSnSrcCurrentLowerInputPowerThreshold,
       "optIfOTSnSrcCurrentUpperInputPowerThreshold": optIfOTSnSrcCurrentUpperInputPowerThreshold,
       "optIfOTSnSrcIntervalTable": optIfOTSnSrcIntervalTable,
       "optIfOTSnSrcIntervalEntry": optIfOTSnSrcIntervalEntry,
       "optIfOTSnSrcIntervalNumber": optIfOTSnSrcIntervalNumber,
       "optIfOTSnSrcIntervalSuspectedFlag": optIfOTSnSrcIntervalSuspectedFlag,
       "optIfOTSnSrcIntervalLastOutputPower": optIfOTSnSrcIntervalLastOutputPower,
       "optIfOTSnSrcIntervalLowOutputPower": optIfOTSnSrcIntervalLowOutputPower,
       "optIfOTSnSrcIntervalHighOutputPower": optIfOTSnSrcIntervalHighOutputPower,
       "optIfOTSnSrcIntervalLastInputPower": optIfOTSnSrcIntervalLastInputPower,
       "optIfOTSnSrcIntervalLowInputPower": optIfOTSnSrcIntervalLowInputPower,
       "optIfOTSnSrcIntervalHighInputPower": optIfOTSnSrcIntervalHighInputPower,
       "optIfOTSnSrcCurDayTable": optIfOTSnSrcCurDayTable,
       "optIfOTSnSrcCurDayEntry": optIfOTSnSrcCurDayEntry,
       "optIfOTSnSrcCurDaySuspectedFlag": optIfOTSnSrcCurDaySuspectedFlag,
       "optIfOTSnSrcCurDayLowOutputPower": optIfOTSnSrcCurDayLowOutputPower,
       "optIfOTSnSrcCurDayHighOutputPower": optIfOTSnSrcCurDayHighOutputPower,
       "optIfOTSnSrcCurDayLowInputPower": optIfOTSnSrcCurDayLowInputPower,
       "optIfOTSnSrcCurDayHighInputPower": optIfOTSnSrcCurDayHighInputPower,
       "optIfOTSnSrcPrevDayTable": optIfOTSnSrcPrevDayTable,
       "optIfOTSnSrcPrevDayEntry": optIfOTSnSrcPrevDayEntry,
       "optIfOTSnSrcPrevDaySuspectedFlag": optIfOTSnSrcPrevDaySuspectedFlag,
       "optIfOTSnSrcPrevDayLastOutputPower": optIfOTSnSrcPrevDayLastOutputPower,
       "optIfOTSnSrcPrevDayLowOutputPower": optIfOTSnSrcPrevDayLowOutputPower,
       "optIfOTSnSrcPrevDayHighOutputPower": optIfOTSnSrcPrevDayHighOutputPower,
       "optIfOTSnSrcPrevDayLastInputPower": optIfOTSnSrcPrevDayLastInputPower,
       "optIfOTSnSrcPrevDayLowInputPower": optIfOTSnSrcPrevDayLowInputPower,
       "optIfOTSnSrcPrevDayHighInputPower": optIfOTSnSrcPrevDayHighInputPower,
       "optIfOMSn": optIfOMSn,
       "optIfOMSnConfigTable": optIfOMSnConfigTable,
       "optIfOMSnConfigEntry": optIfOMSnConfigEntry,
       "optIfOMSnDirectionality": optIfOMSnDirectionality,
       "optIfOMSnCurrentStatus": optIfOMSnCurrentStatus,
       "optIfOMSnSinkCurrentTable": optIfOMSnSinkCurrentTable,
       "optIfOMSnSinkCurrentEntry": optIfOMSnSinkCurrentEntry,
       "optIfOMSnSinkCurrentSuspectedFlag": optIfOMSnSinkCurrentSuspectedFlag,
       "optIfOMSnSinkCurrentAggregatedInputPower": optIfOMSnSinkCurrentAggregatedInputPower,
       "optIfOMSnSinkCurrentLowAggregatedInputPower": optIfOMSnSinkCurrentLowAggregatedInputPower,
       "optIfOMSnSinkCurrentHighAggregatedInputPower": optIfOMSnSinkCurrentHighAggregatedInputPower,
       "optIfOMSnSinkCurrentLowerInputPowerThreshold": optIfOMSnSinkCurrentLowerInputPowerThreshold,
       "optIfOMSnSinkCurrentUpperInputPowerThreshold": optIfOMSnSinkCurrentUpperInputPowerThreshold,
       "optIfOMSnSinkCurrentOutputPower": optIfOMSnSinkCurrentOutputPower,
       "optIfOMSnSinkCurrentLowOutputPower": optIfOMSnSinkCurrentLowOutputPower,
       "optIfOMSnSinkCurrentHighOutputPower": optIfOMSnSinkCurrentHighOutputPower,
       "optIfOMSnSinkCurrentLowerOutputPowerThreshold": optIfOMSnSinkCurrentLowerOutputPowerThreshold,
       "optIfOMSnSinkCurrentUpperOutputPowerThreshold": optIfOMSnSinkCurrentUpperOutputPowerThreshold,
       "optIfOMSnSinkIntervalTable": optIfOMSnSinkIntervalTable,
       "optIfOMSnSinkIntervalEntry": optIfOMSnSinkIntervalEntry,
       "optIfOMSnSinkIntervalNumber": optIfOMSnSinkIntervalNumber,
       "optIfOMSnSinkIntervalSuspectedFlag": optIfOMSnSinkIntervalSuspectedFlag,
       "optIfOMSnSinkIntervalLastAggregatedInputPower": optIfOMSnSinkIntervalLastAggregatedInputPower,
       "optIfOMSnSinkIntervalLowAggregatedInputPower": optIfOMSnSinkIntervalLowAggregatedInputPower,
       "optIfOMSnSinkIntervalHighAggregatedInputPower": optIfOMSnSinkIntervalHighAggregatedInputPower,
       "optIfOMSnSinkIntervalLastOutputPower": optIfOMSnSinkIntervalLastOutputPower,
       "optIfOMSnSinkIntervalLowOutputPower": optIfOMSnSinkIntervalLowOutputPower,
       "optIfOMSnSinkIntervalHighOutputPower": optIfOMSnSinkIntervalHighOutputPower,
       "optIfOMSnSinkCurDayTable": optIfOMSnSinkCurDayTable,
       "optIfOMSnSinkCurDayEntry": optIfOMSnSinkCurDayEntry,
       "optIfOMSnSinkCurDaySuspectedFlag": optIfOMSnSinkCurDaySuspectedFlag,
       "optIfOMSnSinkCurDayLowAggregatedInputPower": optIfOMSnSinkCurDayLowAggregatedInputPower,
       "optIfOMSnSinkCurDayHighAggregatedInputPower": optIfOMSnSinkCurDayHighAggregatedInputPower,
       "optIfOMSnSinkCurDayLowOutputPower": optIfOMSnSinkCurDayLowOutputPower,
       "optIfOMSnSinkCurDayHighOutputPower": optIfOMSnSinkCurDayHighOutputPower,
       "optIfOMSnSinkPrevDayTable": optIfOMSnSinkPrevDayTable,
       "optIfOMSnSinkPrevDayEntry": optIfOMSnSinkPrevDayEntry,
       "optIfOMSnSinkPrevDaySuspectedFlag": optIfOMSnSinkPrevDaySuspectedFlag,
       "optIfOMSnSinkPrevDayLastAggregatedInputPower": optIfOMSnSinkPrevDayLastAggregatedInputPower,
       "optIfOMSnSinkPrevDayLowAggregatedInputPower": optIfOMSnSinkPrevDayLowAggregatedInputPower,
       "optIfOMSnSinkPrevDayHighAggregatedInputPower": optIfOMSnSinkPrevDayHighAggregatedInputPower,
       "optIfOMSnSinkPrevDayLastOutputPower": optIfOMSnSinkPrevDayLastOutputPower,
       "optIfOMSnSinkPrevDayLowOutputPower": optIfOMSnSinkPrevDayLowOutputPower,
       "optIfOMSnSinkPrevDayHighOutputPower": optIfOMSnSinkPrevDayHighOutputPower,
       "optIfOMSnSrcCurrentTable": optIfOMSnSrcCurrentTable,
       "optIfOMSnSrcCurrentEntry": optIfOMSnSrcCurrentEntry,
       "optIfOMSnSrcCurrentSuspectedFlag": optIfOMSnSrcCurrentSuspectedFlag,
       "optIfOMSnSrcCurrentOutputPower": optIfOMSnSrcCurrentOutputPower,
       "optIfOMSnSrcCurrentLowOutputPower": optIfOMSnSrcCurrentLowOutputPower,
       "optIfOMSnSrcCurrentHighOutputPower": optIfOMSnSrcCurrentHighOutputPower,
       "optIfOMSnSrcCurrentLowerOutputPowerThreshold": optIfOMSnSrcCurrentLowerOutputPowerThreshold,
       "optIfOMSnSrcCurrentUpperOutputPowerThreshold": optIfOMSnSrcCurrentUpperOutputPowerThreshold,
       "optIfOMSnSrcCurrentAggregatedInputPower": optIfOMSnSrcCurrentAggregatedInputPower,
       "optIfOMSnSrcCurrentLowAggregatedInputPower": optIfOMSnSrcCurrentLowAggregatedInputPower,
       "optIfOMSnSrcCurrentHighAggregatedInputPower": optIfOMSnSrcCurrentHighAggregatedInputPower,
       "optIfOMSnSrcCurrentLowerInputPowerThreshold": optIfOMSnSrcCurrentLowerInputPowerThreshold,
       "optIfOMSnSrcCurrentUpperInputPowerThreshold": optIfOMSnSrcCurrentUpperInputPowerThreshold,
       "optIfOMSnSrcIntervalTable": optIfOMSnSrcIntervalTable,
       "optIfOMSnSrcIntervalEntry": optIfOMSnSrcIntervalEntry,
       "optIfOMSnSrcIntervalNumber": optIfOMSnSrcIntervalNumber,
       "optIfOMSnSrcIntervalSuspectedFlag": optIfOMSnSrcIntervalSuspectedFlag,
       "optIfOMSnSrcIntervalLastOutputPower": optIfOMSnSrcIntervalLastOutputPower,
       "optIfOMSnSrcIntervalLowOutputPower": optIfOMSnSrcIntervalLowOutputPower,
       "optIfOMSnSrcIntervalHighOutputPower": optIfOMSnSrcIntervalHighOutputPower,
       "optIfOMSnSrcIntervalLastAggregatedInputPower": optIfOMSnSrcIntervalLastAggregatedInputPower,
       "optIfOMSnSrcIntervalLowAggregatedInputPower": optIfOMSnSrcIntervalLowAggregatedInputPower,
       "optIfOMSnSrcIntervalHighAggregatedInputPower": optIfOMSnSrcIntervalHighAggregatedInputPower,
       "optIfOMSnSrcCurDayTable": optIfOMSnSrcCurDayTable,
       "optIfOMSnSrcCurDayEntry": optIfOMSnSrcCurDayEntry,
       "optIfOMSnSrcCurDaySuspectedFlag": optIfOMSnSrcCurDaySuspectedFlag,
       "optIfOMSnSrcCurDayLowOutputPower": optIfOMSnSrcCurDayLowOutputPower,
       "optIfOMSnSrcCurDayHighOutputPower": optIfOMSnSrcCurDayHighOutputPower,
       "optIfOMSnSrcCurDayLowAggregatedInputPower": optIfOMSnSrcCurDayLowAggregatedInputPower,
       "optIfOMSnSrcCurDayHighAggregatedInputPower": optIfOMSnSrcCurDayHighAggregatedInputPower,
       "optIfOMSnSrcPrevDayTable": optIfOMSnSrcPrevDayTable,
       "optIfOMSnSrcPrevDayEntry": optIfOMSnSrcPrevDayEntry,
       "optIfOMSnSrcPrevDaySuspectedFlag": optIfOMSnSrcPrevDaySuspectedFlag,
       "optIfOMSnSrcPrevDayLastOutputPower": optIfOMSnSrcPrevDayLastOutputPower,
       "optIfOMSnSrcPrevDayLowOutputPower": optIfOMSnSrcPrevDayLowOutputPower,
       "optIfOMSnSrcPrevDayHighOutputPower": optIfOMSnSrcPrevDayHighOutputPower,
       "optIfOMSnSrcPrevDayLastAggregatedInputPower": optIfOMSnSrcPrevDayLastAggregatedInputPower,
       "optIfOMSnSrcPrevDayLowAggregatedInputPower": optIfOMSnSrcPrevDayLowAggregatedInputPower,
       "optIfOMSnSrcPrevDayHighAggregatedInputPower": optIfOMSnSrcPrevDayHighAggregatedInputPower,
       "optIfOChGroup": optIfOChGroup,
       "optIfOChGroupConfigTable": optIfOChGroupConfigTable,
       "optIfOChGroupConfigEntry": optIfOChGroupConfigEntry,
       "optIfOChGroupDirectionality": optIfOChGroupDirectionality,
       "optIfOChGroupSinkCurrentTable": optIfOChGroupSinkCurrentTable,
       "optIfOChGroupSinkCurrentEntry": optIfOChGroupSinkCurrentEntry,
       "optIfOChGroupSinkCurrentSuspectedFlag": optIfOChGroupSinkCurrentSuspectedFlag,
       "optIfOChGroupSinkCurrentAggregatedInputPower": optIfOChGroupSinkCurrentAggregatedInputPower,
       "optIfOChGroupSinkCurrentLowAggregatedInputPower": optIfOChGroupSinkCurrentLowAggregatedInputPower,
       "optIfOChGroupSinkCurrentHighAggregatedInputPower": optIfOChGroupSinkCurrentHighAggregatedInputPower,
       "optIfOChGroupSinkCurrentLowerInputPowerThreshold": optIfOChGroupSinkCurrentLowerInputPowerThreshold,
       "optIfOChGroupSinkCurrentUpperInputPowerThreshold": optIfOChGroupSinkCurrentUpperInputPowerThreshold,
       "optIfOChGroupSinkCurrentOutputPower": optIfOChGroupSinkCurrentOutputPower,
       "optIfOChGroupSinkCurrentLowOutputPower": optIfOChGroupSinkCurrentLowOutputPower,
       "optIfOChGroupSinkCurrentHighOutputPower": optIfOChGroupSinkCurrentHighOutputPower,
       "optIfOChGroupSinkCurrentLowerOutputPowerThreshold": optIfOChGroupSinkCurrentLowerOutputPowerThreshold,
       "optIfOChGroupSinkCurrentUpperOutputPowerThreshold": optIfOChGroupSinkCurrentUpperOutputPowerThreshold,
       "optIfOChGroupSinkIntervalTable": optIfOChGroupSinkIntervalTable,
       "optIfOChGroupSinkIntervalEntry": optIfOChGroupSinkIntervalEntry,
       "optIfOChGroupSinkIntervalNumber": optIfOChGroupSinkIntervalNumber,
       "optIfOChGroupSinkIntervalSuspectedFlag": optIfOChGroupSinkIntervalSuspectedFlag,
       "optIfOChGroupSinkIntervalLastAggregatedInputPower": optIfOChGroupSinkIntervalLastAggregatedInputPower,
       "optIfOChGroupSinkIntervalLowAggregatedInputPower": optIfOChGroupSinkIntervalLowAggregatedInputPower,
       "optIfOChGroupSinkIntervalHighAggregatedInputPower": optIfOChGroupSinkIntervalHighAggregatedInputPower,
       "optIfOChGroupSinkIntervalLastOutputPower": optIfOChGroupSinkIntervalLastOutputPower,
       "optIfOChGroupSinkIntervalLowOutputPower": optIfOChGroupSinkIntervalLowOutputPower,
       "optIfOChGroupSinkIntervalHighOutputPower": optIfOChGroupSinkIntervalHighOutputPower,
       "optIfOChGroupSinkCurDayTable": optIfOChGroupSinkCurDayTable,
       "optIfOChGroupSinkCurDayEntry": optIfOChGroupSinkCurDayEntry,
       "optIfOChGroupSinkCurDaySuspectedFlag": optIfOChGroupSinkCurDaySuspectedFlag,
       "optIfOChGroupSinkCurDayLowAggregatedInputPower": optIfOChGroupSinkCurDayLowAggregatedInputPower,
       "optIfOChGroupSinkCurDayHighAggregatedInputPower": optIfOChGroupSinkCurDayHighAggregatedInputPower,
       "optIfOChGroupSinkCurDayLowOutputPower": optIfOChGroupSinkCurDayLowOutputPower,
       "optIfOChGroupSinkCurDayHighOutputPower": optIfOChGroupSinkCurDayHighOutputPower,
       "optIfOChGroupSinkPrevDayTable": optIfOChGroupSinkPrevDayTable,
       "optIfOChGroupSinkPrevDayEntry": optIfOChGroupSinkPrevDayEntry,
       "optIfOChGroupSinkPrevDaySuspectedFlag": optIfOChGroupSinkPrevDaySuspectedFlag,
       "optIfOChGroupSinkPrevDayLastAggregatedInputPower": optIfOChGroupSinkPrevDayLastAggregatedInputPower,
       "optIfOChGroupSinkPrevDayLowAggregatedInputPower": optIfOChGroupSinkPrevDayLowAggregatedInputPower,
       "optIfOChGroupSinkPrevDayHighAggregatedInputPower": optIfOChGroupSinkPrevDayHighAggregatedInputPower,
       "optIfOChGroupSinkPrevDayLastOutputPower": optIfOChGroupSinkPrevDayLastOutputPower,
       "optIfOChGroupSinkPrevDayLowOutputPower": optIfOChGroupSinkPrevDayLowOutputPower,
       "optIfOChGroupSinkPrevDayHighOutputPower": optIfOChGroupSinkPrevDayHighOutputPower,
       "optIfOChGroupSrcCurrentTable": optIfOChGroupSrcCurrentTable,
       "optIfOChGroupSrcCurrentEntry": optIfOChGroupSrcCurrentEntry,
       "optIfOChGroupSrcCurrentSuspectedFlag": optIfOChGroupSrcCurrentSuspectedFlag,
       "optIfOChGroupSrcCurrentOutputPower": optIfOChGroupSrcCurrentOutputPower,
       "optIfOChGroupSrcCurrentLowOutputPower": optIfOChGroupSrcCurrentLowOutputPower,
       "optIfOChGroupSrcCurrentHighOutputPower": optIfOChGroupSrcCurrentHighOutputPower,
       "optIfOChGroupSrcCurrentLowerOutputPowerThreshold": optIfOChGroupSrcCurrentLowerOutputPowerThreshold,
       "optIfOChGroupSrcCurrentUpperOutputPowerThreshold": optIfOChGroupSrcCurrentUpperOutputPowerThreshold,
       "optIfOChGroupSrcCurrentAggregatedInputPower": optIfOChGroupSrcCurrentAggregatedInputPower,
       "optIfOChGroupSrcCurrentLowAggregatedInputPower": optIfOChGroupSrcCurrentLowAggregatedInputPower,
       "optIfOChGroupSrcCurrentHighAggregatedInputPower": optIfOChGroupSrcCurrentHighAggregatedInputPower,
       "optIfOChGroupSrcCurrentLowerInputPowerThreshold": optIfOChGroupSrcCurrentLowerInputPowerThreshold,
       "optIfOChGroupSrcCurrentUpperInputPowerThreshold": optIfOChGroupSrcCurrentUpperInputPowerThreshold,
       "optIfOChGroupSrcIntervalTable": optIfOChGroupSrcIntervalTable,
       "optIfOChGroupSrcIntervalEntry": optIfOChGroupSrcIntervalEntry,
       "optIfOChGroupSrcIntervalNumber": optIfOChGroupSrcIntervalNumber,
       "optIfOChGroupSrcIntervalSuspectedFlag": optIfOChGroupSrcIntervalSuspectedFlag,
       "optIfOChGroupSrcIntervalLastOutputPower": optIfOChGroupSrcIntervalLastOutputPower,
       "optIfOChGroupSrcIntervalLowOutputPower": optIfOChGroupSrcIntervalLowOutputPower,
       "optIfOChGroupSrcIntervalHighOutputPower": optIfOChGroupSrcIntervalHighOutputPower,
       "optIfOChGroupSrcIntervalLastAggregatedInputPower": optIfOChGroupSrcIntervalLastAggregatedInputPower,
       "optIfOChGroupSrcIntervalLowAggregatedInputPower": optIfOChGroupSrcIntervalLowAggregatedInputPower,
       "optIfOChGroupSrcIntervalHighAggregatedInputPower": optIfOChGroupSrcIntervalHighAggregatedInputPower,
       "optIfOChGroupSrcCurDayTable": optIfOChGroupSrcCurDayTable,
       "optIfOChGroupSrcCurDayEntry": optIfOChGroupSrcCurDayEntry,
       "optIfOChGroupSrcCurDaySuspectedFlag": optIfOChGroupSrcCurDaySuspectedFlag,
       "optIfOChGroupSrcCurDayLowOutputPower": optIfOChGroupSrcCurDayLowOutputPower,
       "optIfOChGroupSrcCurDayHighOutputPower": optIfOChGroupSrcCurDayHighOutputPower,
       "optIfOChGroupSrcCurDayLowAggregatedInputPower": optIfOChGroupSrcCurDayLowAggregatedInputPower,
       "optIfOChGroupSrcCurDayHighAggregatedInputPower": optIfOChGroupSrcCurDayHighAggregatedInputPower,
       "optIfOChGroupSrcPrevDayTable": optIfOChGroupSrcPrevDayTable,
       "optIfOChGroupSrcPrevDayEntry": optIfOChGroupSrcPrevDayEntry,
       "optIfOChGroupSrcPrevDaySuspectedFlag": optIfOChGroupSrcPrevDaySuspectedFlag,
       "optIfOChGroupSrcPrevDayLastOutputPower": optIfOChGroupSrcPrevDayLastOutputPower,
       "optIfOChGroupSrcPrevDayLowOutputPower": optIfOChGroupSrcPrevDayLowOutputPower,
       "optIfOChGroupSrcPrevDayHighOutputPower": optIfOChGroupSrcPrevDayHighOutputPower,
       "optIfOChGroupSrcPrevDayLastAggregatedInputPower": optIfOChGroupSrcPrevDayLastAggregatedInputPower,
       "optIfOChGroupSrcPrevDayLowAggregatedInputPower": optIfOChGroupSrcPrevDayLowAggregatedInputPower,
       "optIfOChGroupSrcPrevDayHighAggregatedInputPower": optIfOChGroupSrcPrevDayHighAggregatedInputPower,
       "optIfOCh": optIfOCh,
       "optIfOChConfigTable": optIfOChConfigTable,
       "optIfOChConfigEntry": optIfOChConfigEntry,
       "optIfOChDirectionality": optIfOChDirectionality,
       "optIfOChCurrentStatus": optIfOChCurrentStatus,
       "optIfOChSinkCurrentTable": optIfOChSinkCurrentTable,
       "optIfOChSinkCurrentEntry": optIfOChSinkCurrentEntry,
       "optIfOChSinkCurrentSuspectedFlag": optIfOChSinkCurrentSuspectedFlag,
       "optIfOChSinkCurrentInputPower": optIfOChSinkCurrentInputPower,
       "optIfOChSinkCurrentLowInputPower": optIfOChSinkCurrentLowInputPower,
       "optIfOChSinkCurrentHighInputPower": optIfOChSinkCurrentHighInputPower,
       "optIfOChSinkCurrentLowerInputPowerThreshold": optIfOChSinkCurrentLowerInputPowerThreshold,
       "optIfOChSinkCurrentUpperInputPowerThreshold": optIfOChSinkCurrentUpperInputPowerThreshold,
       "optIfOChSinkIntervalTable": optIfOChSinkIntervalTable,
       "optIfOChSinkIntervalEntry": optIfOChSinkIntervalEntry,
       "optIfOChSinkIntervalNumber": optIfOChSinkIntervalNumber,
       "optIfOChSinkIntervalSuspectedFlag": optIfOChSinkIntervalSuspectedFlag,
       "optIfOChSinkIntervalLastInputPower": optIfOChSinkIntervalLastInputPower,
       "optIfOChSinkIntervalLowInputPower": optIfOChSinkIntervalLowInputPower,
       "optIfOChSinkIntervalHighInputPower": optIfOChSinkIntervalHighInputPower,
       "optIfOChSinkCurDayTable": optIfOChSinkCurDayTable,
       "optIfOChSinkCurDayEntry": optIfOChSinkCurDayEntry,
       "optIfOChSinkCurDaySuspectedFlag": optIfOChSinkCurDaySuspectedFlag,
       "optIfOChSinkCurDayLowInputPower": optIfOChSinkCurDayLowInputPower,
       "optIfOChSinkCurDayHighInputPower": optIfOChSinkCurDayHighInputPower,
       "optIfOChSinkPrevDayTable": optIfOChSinkPrevDayTable,
       "optIfOChSinkPrevDayEntry": optIfOChSinkPrevDayEntry,
       "optIfOChSinkPrevDaySuspectedFlag": optIfOChSinkPrevDaySuspectedFlag,
       "optIfOChSinkPrevDayLastInputPower": optIfOChSinkPrevDayLastInputPower,
       "optIfOChSinkPrevDayLowInputPower": optIfOChSinkPrevDayLowInputPower,
       "optIfOChSinkPrevDayHighInputPower": optIfOChSinkPrevDayHighInputPower,
       "optIfOChSrcCurrentTable": optIfOChSrcCurrentTable,
       "optIfOChSrcCurrentEntry": optIfOChSrcCurrentEntry,
       "optIfOChSrcCurrentSuspectedFlag": optIfOChSrcCurrentSuspectedFlag,
       "optIfOChSrcCurrentOutputPower": optIfOChSrcCurrentOutputPower,
       "optIfOChSrcCurrentLowOutputPower": optIfOChSrcCurrentLowOutputPower,
       "optIfOChSrcCurrentHighOutputPower": optIfOChSrcCurrentHighOutputPower,
       "optIfOChSrcCurrentLowerOutputPowerThreshold": optIfOChSrcCurrentLowerOutputPowerThreshold,
       "optIfOChSrcCurrentUpperOutputPowerThreshold": optIfOChSrcCurrentUpperOutputPowerThreshold,
       "optIfOChSrcIntervalTable": optIfOChSrcIntervalTable,
       "optIfOChSrcIntervalEntry": optIfOChSrcIntervalEntry,
       "optIfOChSrcIntervalNumber": optIfOChSrcIntervalNumber,
       "optIfOChSrcIntervalSuspectedFlag": optIfOChSrcIntervalSuspectedFlag,
       "optIfOChSrcIntervalLastOutputPower": optIfOChSrcIntervalLastOutputPower,
       "optIfOChSrcIntervalLowOutputPower": optIfOChSrcIntervalLowOutputPower,
       "optIfOChSrcIntervalHighOutputPower": optIfOChSrcIntervalHighOutputPower,
       "optIfOChSrcCurDayTable": optIfOChSrcCurDayTable,
       "optIfOChSrcCurDayEntry": optIfOChSrcCurDayEntry,
       "optIfOChSrcCurDaySuspectedFlag": optIfOChSrcCurDaySuspectedFlag,
       "optIfOChSrcCurDayLowOutputPower": optIfOChSrcCurDayLowOutputPower,
       "optIfOChSrcCurDayHighOutputPower": optIfOChSrcCurDayHighOutputPower,
       "optIfOChSrcPrevDayTable": optIfOChSrcPrevDayTable,
       "optIfOChSrcPrevDayEntry": optIfOChSrcPrevDayEntry,
       "optIfOChSrcPrevDaySuspectedFlag": optIfOChSrcPrevDaySuspectedFlag,
       "optIfOChSrcPrevDayLastOutputPower": optIfOChSrcPrevDayLastOutputPower,
       "optIfOChSrcPrevDayLowOutputPower": optIfOChSrcPrevDayLowOutputPower,
       "optIfOChSrcPrevDayHighOutputPower": optIfOChSrcPrevDayHighOutputPower,
       "optIfOTUk": optIfOTUk,
       "optIfOTUkConfigTable": optIfOTUkConfigTable,
       "optIfOTUkConfigEntry": optIfOTUkConfigEntry,
       "optIfOTUkDirectionality": optIfOTUkDirectionality,
       "optIfOTUkBitRateK": optIfOTUkBitRateK,
       "optIfOTUkTraceIdentifierTransmitted": optIfOTUkTraceIdentifierTransmitted,
       "optIfOTUkDAPIExpected": optIfOTUkDAPIExpected,
       "optIfOTUkSAPIExpected": optIfOTUkSAPIExpected,
       "optIfOTUkTraceIdentifierAccepted": optIfOTUkTraceIdentifierAccepted,
       "optIfOTUkTIMDetMode": optIfOTUkTIMDetMode,
       "optIfOTUkTIMActEnabled": optIfOTUkTIMActEnabled,
       "optIfOTUkDEGThr": optIfOTUkDEGThr,
       "optIfOTUkDEGM": optIfOTUkDEGM,
       "optIfOTUkSinkAdaptActive": optIfOTUkSinkAdaptActive,
       "optIfOTUkSourceAdaptActive": optIfOTUkSourceAdaptActive,
       "optIfOTUkSinkFECEnabled": optIfOTUkSinkFECEnabled,
       "optIfOTUkCurrentStatus": optIfOTUkCurrentStatus,
       "optIfGCC0ConfigTable": optIfGCC0ConfigTable,
       "optIfGCC0ConfigEntry": optIfGCC0ConfigEntry,
       "optIfGCC0Directionality": optIfGCC0Directionality,
       "optIfGCC0Application": optIfGCC0Application,
       "optIfGCC0RowStatus": optIfGCC0RowStatus,
       "optIfODUk": optIfODUk,
       "optIfODUkConfigTable": optIfODUkConfigTable,
       "optIfODUkConfigEntry": optIfODUkConfigEntry,
       "optIfODUkDirectionality": optIfODUkDirectionality,
       "optIfODUkBitRateK": optIfODUkBitRateK,
       "optIfODUkTcmFieldsInUse": optIfODUkTcmFieldsInUse,
       "optIfODUkPositionSeqCurrentSize": optIfODUkPositionSeqCurrentSize,
       "optIfODUkTtpPresent": optIfODUkTtpPresent,
       "optIfODUkTtpConfigTable": optIfODUkTtpConfigTable,
       "optIfODUkTtpConfigEntry": optIfODUkTtpConfigEntry,
       "optIfODUkTtpTraceIdentifierTransmitted": optIfODUkTtpTraceIdentifierTransmitted,
       "optIfODUkTtpDAPIExpected": optIfODUkTtpDAPIExpected,
       "optIfODUkTtpSAPIExpected": optIfODUkTtpSAPIExpected,
       "optIfODUkTtpTraceIdentifierAccepted": optIfODUkTtpTraceIdentifierAccepted,
       "optIfODUkTtpTIMDetMode": optIfODUkTtpTIMDetMode,
       "optIfODUkTtpTIMActEnabled": optIfODUkTtpTIMActEnabled,
       "optIfODUkTtpDEGThr": optIfODUkTtpDEGThr,
       "optIfODUkTtpDEGM": optIfODUkTtpDEGM,
       "optIfODUkTtpCurrentStatus": optIfODUkTtpCurrentStatus,
       "optIfODUkPositionSeqTable": optIfODUkPositionSeqTable,
       "optIfODUkPositionSeqEntry": optIfODUkPositionSeqEntry,
       "optIfODUkPositionSeqIndex": optIfODUkPositionSeqIndex,
       "optIfODUkPositionSeqPosition": optIfODUkPositionSeqPosition,
       "optIfODUkPositionSeqPointer": optIfODUkPositionSeqPointer,
       "optIfODUkNimConfigTable": optIfODUkNimConfigTable,
       "optIfODUkNimConfigEntry": optIfODUkNimConfigEntry,
       "optIfODUkNimDirectionality": optIfODUkNimDirectionality,
       "optIfODUkNimDAPIExpected": optIfODUkNimDAPIExpected,
       "optIfODUkNimSAPIExpected": optIfODUkNimSAPIExpected,
       "optIfODUkNimTraceIdentifierAccepted": optIfODUkNimTraceIdentifierAccepted,
       "optIfODUkNimTIMDetMode": optIfODUkNimTIMDetMode,
       "optIfODUkNimTIMActEnabled": optIfODUkNimTIMActEnabled,
       "optIfODUkNimDEGThr": optIfODUkNimDEGThr,
       "optIfODUkNimDEGM": optIfODUkNimDEGM,
       "optIfODUkNimCurrentStatus": optIfODUkNimCurrentStatus,
       "optIfODUkNimRowStatus": optIfODUkNimRowStatus,
       "optIfGCC12ConfigTable": optIfGCC12ConfigTable,
       "optIfGCC12ConfigEntry": optIfGCC12ConfigEntry,
       "optIfGCC12Codirectional": optIfGCC12Codirectional,
       "optIfGCC12GCCAccess": optIfGCC12GCCAccess,
       "optIfGCC12GCCPassThrough": optIfGCC12GCCPassThrough,
       "optIfGCC12Application": optIfGCC12Application,
       "optIfGCC12RowStatus": optIfGCC12RowStatus,
       "optIfODUkT": optIfODUkT,
       "optIfODUkTConfigTable": optIfODUkTConfigTable,
       "optIfODUkTConfigEntry": optIfODUkTConfigEntry,
       "optIfODUkTTcmField": optIfODUkTTcmField,
       "optIfODUkTCodirectional": optIfODUkTCodirectional,
       "optIfODUkTTraceIdentifierTransmitted": optIfODUkTTraceIdentifierTransmitted,
       "optIfODUkTDAPIExpected": optIfODUkTDAPIExpected,
       "optIfODUkTSAPIExpected": optIfODUkTSAPIExpected,
       "optIfODUkTTraceIdentifierAccepted": optIfODUkTTraceIdentifierAccepted,
       "optIfODUkTTIMDetMode": optIfODUkTTIMDetMode,
       "optIfODUkTTIMActEnabled": optIfODUkTTIMActEnabled,
       "optIfODUkTDEGThr": optIfODUkTDEGThr,
       "optIfODUkTDEGM": optIfODUkTDEGM,
       "optIfODUkTSinkMode": optIfODUkTSinkMode,
       "optIfODUkTSinkLockSignalAdminState": optIfODUkTSinkLockSignalAdminState,
       "optIfODUkTSourceLockSignalAdminState": optIfODUkTSourceLockSignalAdminState,
       "optIfODUkTCurrentStatus": optIfODUkTCurrentStatus,
       "optIfODUkTRowStatus": optIfODUkTRowStatus,
       "optIfODUkTNimConfigTable": optIfODUkTNimConfigTable,
       "optIfODUkTNimConfigEntry": optIfODUkTNimConfigEntry,
       "optIfODUkTNimTcmField": optIfODUkTNimTcmField,
       "optIfODUkTNimDirectionality": optIfODUkTNimDirectionality,
       "optIfODUkTNimDAPIExpected": optIfODUkTNimDAPIExpected,
       "optIfODUkTNimSAPIExpected": optIfODUkTNimSAPIExpected,
       "optIfODUkTNimTraceIdentifierAccepted": optIfODUkTNimTraceIdentifierAccepted,
       "optIfODUkTNimTIMDetMode": optIfODUkTNimTIMDetMode,
       "optIfODUkTNimTIMActEnabled": optIfODUkTNimTIMActEnabled,
       "optIfODUkTNimDEGThr": optIfODUkTNimDEGThr,
       "optIfODUkTNimDEGM": optIfODUkTNimDEGM,
       "optIfODUkTNimCurrentStatus": optIfODUkTNimCurrentStatus,
       "optIfODUkTNimRowStatus": optIfODUkTNimRowStatus,
       "optIfConfs": optIfConfs,
       "optIfGroups": optIfGroups,
       "optIfOTMnGroup": optIfOTMnGroup,
       "optIfPerfMonGroup": optIfPerfMonGroup,
       "optIfOTSnCommonGroup": optIfOTSnCommonGroup,
       "optIfOTSnSourceGroupFull": optIfOTSnSourceGroupFull,
       "optIfOTSnAPRStatusGroup": optIfOTSnAPRStatusGroup,
       "optIfOTSnAPRControlGroup": optIfOTSnAPRControlGroup,
       "optIfOTSnSinkGroupBasic": optIfOTSnSinkGroupBasic,
       "optIfOTSnSinkGroupFull": optIfOTSnSinkGroupFull,
       "optIfOTSnSinkPreOtnPMGroup": optIfOTSnSinkPreOtnPMGroup,
       "optIfOTSnSinkPreOtnPMThresholdGroup": optIfOTSnSinkPreOtnPMThresholdGroup,
       "optIfOTSnSourcePreOtnPMGroup": optIfOTSnSourcePreOtnPMGroup,
       "optIfOTSnSourcePreOtnPMThresholdGroup": optIfOTSnSourcePreOtnPMThresholdGroup,
       "optIfOMSnCommonGroup": optIfOMSnCommonGroup,
       "optIfOMSnSinkGroupBasic": optIfOMSnSinkGroupBasic,
       "optIfOMSnSinkPreOtnPMGroup": optIfOMSnSinkPreOtnPMGroup,
       "optIfOMSnSinkPreOtnPMThresholdGroup": optIfOMSnSinkPreOtnPMThresholdGroup,
       "optIfOMSnSourcePreOtnPMGroup": optIfOMSnSourcePreOtnPMGroup,
       "optIfOMSnSourcePreOtnPMThresholdGroup": optIfOMSnSourcePreOtnPMThresholdGroup,
       "optIfOChGroupCommonGroup": optIfOChGroupCommonGroup,
       "optIfOChGroupSinkPreOtnPMGroup": optIfOChGroupSinkPreOtnPMGroup,
       "optIfOChGroupSinkPreOtnPMThresholdGroup": optIfOChGroupSinkPreOtnPMThresholdGroup,
       "optIfOChGroupSourcePreOtnPMGroup": optIfOChGroupSourcePreOtnPMGroup,
       "optIfOChGroupSourcePreOtnPMThresholdGroup": optIfOChGroupSourcePreOtnPMThresholdGroup,
       "optIfOChCommonGroup": optIfOChCommonGroup,
       "optIfOChSinkGroupBasic": optIfOChSinkGroupBasic,
       "optIfOChSinkPreOtnPMGroup": optIfOChSinkPreOtnPMGroup,
       "optIfOChSinkPreOtnPMThresholdGroup": optIfOChSinkPreOtnPMThresholdGroup,
       "optIfOChSourcePreOtnPMGroup": optIfOChSourcePreOtnPMGroup,
       "optIfOChSourcePreOtnPMThresholdGroup": optIfOChSourcePreOtnPMThresholdGroup,
       "optIfOTUkCommonGroup": optIfOTUkCommonGroup,
       "optIfOTUkSourceGroup": optIfOTUkSourceGroup,
       "optIfOTUkSinkGroup": optIfOTUkSinkGroup,
       "optIfGCC0Group": optIfGCC0Group,
       "optIfODUkGroup": optIfODUkGroup,
       "optIfODUkTtpSourceGroup": optIfODUkTtpSourceGroup,
       "optIfODUkTtpSinkGroup": optIfODUkTtpSinkGroup,
       "optIfODUkNimGroup": optIfODUkNimGroup,
       "optIfGCC12Group": optIfGCC12Group,
       "optIfODUkTCommonGroup": optIfODUkTCommonGroup,
       "optIfODUkTSourceGroup": optIfODUkTSourceGroup,
       "optIfODUkTSinkGroup": optIfODUkTSinkGroup,
       "optIfODUkTSinkGroupCtp": optIfODUkTSinkGroupCtp,
       "optIfODUkTNimGroup": optIfODUkTNimGroup,
       "optIfCompl": optIfCompl,
       "optIfOtnConfigCompl": optIfOtnConfigCompl,
       "optIfPreOtnPMCompl": optIfPreOtnPMCompl}
)
